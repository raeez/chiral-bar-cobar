# T12_MC5_BV_bar (415s, gpt-5.4)

- [CRITICAL] chapters/connections/bv_brst.tex:1932 — The core class-M mechanism, `\delta_r^{\mathrm{harm}} = c_r(\cA)\,m_0^{\lfloor r/2\rfloor-1}`, is introduced without proof or citation. In the files read, this factorization appears only in `thm:bv-bar-coderived`, its follow-up remark, and downstream restatements, so the theorem’s main engine is unproved.

- [CRITICAL] chapters/connections/bv_brst.tex:1945 — The proof treats `m_0\cdot x = d^2(x) \in \operatorname{Im}(d)` as enough to kill the obstruction in `D^{\mathrm{co}}`. But the appendix defines the coderived category as a Verdier quotient by coacyclic objects, not as “boundaries modulo `\operatorname{Im}(d)`” ([chapters/theory/coderived_models.tex:75]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:75), [chapters/theory/coderived_models.tex:545]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:545)). Worse, the manuscript itself says curved objects are *not* set to zero in the coderived category ([chapters/theory/bar_cobar_adjunction_inversion.tex:3355]( /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3355)). This is a direct logical failure in the coderived proof.

- [CRITICAL] chapters/connections/bv_brst.tex:1624 — The chapter says the higher-genus chain-level quasi-isomorphism remains open “even for free fields,” i.e. Heisenberg ([1636–1650]), but later upgrades class `G` to chain-level proved ([1821–1822]) and uses chain-level quasi-isomorphisms for `G/L/C` inside `thm:bv-bar-coderived` ([1938–1941]). The status surface is internally contradictory.

- [HIGH] chapters/connections/bv_brst.tex:1925 — For classes `G/L/C`, the theorem cites only `prop:chain-level-three-obstructions`. That proposition classifies obstructions; it does not construct the BV-to-bar chain map or prove a quasi-isomorphism. For `L` and `C`, its proof text only reaches genus `1` ([1741], [1759–1760]), while `thm:bv-bar-coderived` claims all `g\ge1`.

- [HIGH] chapters/connections/bv_brst.tex:1751 — The only support for class `C` is an untagged remark. Its Hodge argument says a quartic correction is a “5-form on a 2-manifold” ([1783–1788]), which uses the wrong domain for a quartic graph/configuration-space integral, and it then calls the “free `\beta\gamma` system” class `G` ([1799–1800]), contradicting the chapter’s own classification of `\beta\gamma` as class `C` ([1825–1826]). This does not support an unconditional proof.

- [HIGH] chapters/connections/bv_brst.tex:1677 — Obstruction (2) is only claimed resolved for theories whose partition function comes from a zeta-regularized determinant ([1682–1684]), but `thm:bv-bar-coderived` upgrades that to “resolved for all classes” ([1927–1929]) without importing any determinant hypothesis. That is scope inflation.

- [HIGH] chapters/connections/bv_brst.tex:1834 — The manuscript does not actually prove that class `M` is chain-level false. The only written reason is the heuristic nonholomorphic factor `\kappa/\mathrm{Im}(\tau)` not lying in the image of the holomorphic bar differential ([1834–1837], [1891–1894]). The same surface then rewrites the obstruction as `Q^{\mathrm{contact}}\cdot m_0` with `m_0=\kappa(\cA)\omega_g` ([1840], [1975–1977]) without proving a bridge between these different objects. So “false” is asserted, not established.

- [MEDIUM] chapters/connections/concordance.tex:7611 — The unsupported claims have propagated: concordance repeats “class `M` chain-level false,” “classes `G/L/C` chain-level proved,” and “every `\delta_r` is coderived-exact” ([7611], [10085–10124]); `en_koszul_duality.tex` reuses the same coderived-exactness mechanism ([3395–3397], [3445–3453]). The overclaim is not local to one theorem.

- [LOW] compute/lib/theorem_bv_sewing_engine.py:12 — The cited compute layer is not independent evidence. It hardcodes theorem-status assumptions, upgrades Heisenberg to a chain-level quasi-isomorphism absent from `thm:heisenberg-bv-bar-all-genera` ([41–45]), and gives a different `C/M` status split from the chapter.

**Status split from the files actually read**
- Analytic proved: `thm:general-hs-sewing` proves convergence under growth conditions; `thm:heisenberg-sewing` gives the explicit Heisenberg sewing/Fredholm model.
- Genus-0 algebraic proved: `thm:brst-bar-genus0`, packaged in `thm:algebraic-string-dictionary`.
- Higher-genus scalar proved: `thm:heisenberg-bv-bar-all-genera` proves only the scalar/free-energy identity, and explicitly says this is weaker than a chain-level quasi-isomorphism.
- Coderived lane: advertised as proved by `thm:bv-bar-coderived`, but the written proof fails.
- Class `M` chain-level false: not proved in the manuscript as read; only asserted heuristically.

## Summary
Instances checked: 28 | Violations found: 9 | Verdict: FAIL


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
session id: 019d8388-345d-78f3-964d-8d501e5a58af
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


MISSION: FALSIFY the proof of MC5: BV/bar identification. Status: analytic proved, coderived proved, chain conjectural. Check: (a) what exactly is proved at each level? (b) is class M chain-level really false? (c) is the coderived result correct?

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
Using `deep-beilinson-audit` for this turn because the task is an adversarial proof audit. I’m starting by reading the required constitutional surfaces and locating every `MC5` / BV-bar identification mention so I can lock the exact theorem, status boundary, and dependency chain before checking the proof line by line.
Plan update
  → Read required repo-wide audit surfaces and lock the exact MC5 claim surface
  • Locate the full MC5 theorem statement, proof, and all cited dependencies
  • Audit each proof step for logic, scope, hidden assumptions, and boundary failures
  • Check theorem status across analytic, coderived, and chain-level formulations
  • Re-verify findings and produce severity-ordered report
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

codex
I’ve loaded the audit skill and am now fixing the claim surface: the theorem label, current status text, and dependency graph. Next I’m pulling the concordance, theorem registry, red-team notes, and all `MC5` mentions so the audit is anchored to live source rather than folklore.
exec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "MC5|BV/bar|BV[''^[:alpha:]]*bar|bar[''^[:alpha:]]*BV|coderived|analytic proved|chain conjectural" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md chapters metadata' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
Total output lines: 820

archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
CLAUDE.md:773:AP73: BV=bar: PROVED G/L, CONDITIONAL C/M (harmonic decoupling).
CLAUDE.md:849:AP167: Topologization scope. thm:topologization is PROVED for affine KM V_k(g) at non-critical level k != -h^v (where Sugawara T = {Q,G} is explicit). For general chiral algebras with conformal vector: CONJECTURAL (conj:topologization-general). The proof is COHOMOLOGICAL (works on Q-cohomology, not on cochains). For class M (Virasoro), where chain-level BV/bar is false, the E_3 may exist only on cohomology. COUNTER: every topologization reference must carry scope qualifier "(proved for affine KM at non-critical level)."
metadata/theorem_registry.md:527:#### `chapters/theory/coderived_models.tex` (6)
metadata/theorem_registry.md:531:| `prop:coderived-adequacy` | `proposition` | 243 | Adequacy |
metadata/theorem_registry.md:2314:| `thm:heisenberg-bv-bar-all-genera` | `theorem` | 1400 | BV $=$ bar for the Heisenberg at all genera |
metadata/theorem_registry.md:2316:| `thm:bv-bar-coderived` | `theorem` | 1895 | BV$=$bar in the coderived category |
metadata/theorem_registry.md:2765:| `prop:thqg-X-coderived-fredholm-G` | `proposition` | 2107 | Coderived = Fredholm for class~G |
chapters/connections/concordance.tex:695: Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
chapters/connections/concordance.tex:696: in the coderived category $D^{\mathrm{co}}$ for all shadow classes
chapters/connections/concordance.tex:697: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
chapters/connections/concordance.tex:1943:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
chapters/connections/concordance.tex:1955: BV=bar in the coderived category is proved for all four shadow
chapters/connections/concordance.tex:1956: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/concordance.tex:1981:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
chapters/connections/concordance.tex:1983:BRST/bar, $D^{\mathrm{co}}$-level BV=bar for all shadow classes;
chapters/connections/concordance.tex:2889: & analytic bar coalgebra (MC5) \\[2pt]
exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
| `ProvedHere` | 2809 |
codex
The live status surfaces agree at the top level: concordance and `CLAUDE.md` both advertise `MC5` as analytic proved, coderived proved, chain-level conjectural. I’m now reading the actual `thm:bv-bar-coderived` block, the preceding chain-level landscape discussion, and every cited dependency to see whether that advertised split survives contact with the proof.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1650,2055p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:bv-bar-coderived|conj:master-bv-brst|rem:bv-sewing-chain-level-classes|rem:bv-bar-bridge|thm:heisenberg-bv-bar-all-genera|thm:algebraic-string-dictionary|prop:coderived-adequacy|def:provisional-coderived|def:coderived-fact|rem:derived-coderived-chiral-CDG|rem:curvature-coderived|thm:positselski-chiral-proved|thm:chiral-co-contra-correspondence|thm:general-hs-sewing|thm:heisenberg-sewing" chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1650	is a quasi-isomorphism, which is strictly stronger.
  1651	\end{remark}
  1652	
  1653	\begin{proposition}[Three chain-level obstructions;
  1654	\ClaimStatusProvedHere]
  1655	\label{prop:chain-level-three-obstructions}
  1656	\index{BV algebra!chain-level obstructions|textbf}
  1657	\index{chain-level BV/bar identification}
  1658	The chain-level identification
  1659	\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
  1660	at genus $g \geq 1$
  1661	faces three obstructions, classified by the shadow depth
  1662	of the algebra.
  1663	\begin{enumerate}[label=\textup{(\arabic*)},nosep]
  1664	\item \textbf{Propagator regularity.}
  1665	 The BV propagator $P(z,w) = \bar\partial^{-1}\delta(z,w)$
  1666	 is a distribution; the bar propagator
  1667	 $d\log E(z,w)$ is meromorphic.
  1668	 By Hodge decomposition, $P = d\log E + P_{\mathrm{ex}}
  1669	 + P_{\mathrm{harm}}$
 succeeded in 51ms:
chapters/theory/coderived_models.tex:121:specialization is Theorem~\ref{thm:chiral-co-contra-correspondence}.
chapters/theory/coderived_models.tex:170:\textup{(}Theorem~\ref{thm:positselski-chiral-proved}\textup{)} is the chiral
chapters/theory/coderived_models.tex:234:\label{def:provisional-coderived}
chapters/theory/coderived_models.tex:243:\label{prop:coderived-adequacy}
chapters/theory/coderived_models.tex:336:(Definition~\ref{def:provisional-coderived}) embeds into
chapters/theory/coderived_models.tex:546:\label{def:coderived-fact}
chapters/theory/coderived_models.tex:695:(Proposition~\ref{prop:coderived-adequacy}(b)) provides the
chapters/theory/coderived_models.tex:745:(Theorem~\ref{thm:chiral-co-contra-correspondence}) across
chapters/theory/coderived_models.tex:756:Theorem~\ref{thm:chiral-co-contra-correspondence} gives
chapters/connections/bv_brst.tex:31:for all four shadow classes (Theorem~\ref{thm:bv-bar-coderived}):
chapters/connections/bv_brst.tex:36:(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
chapters/connections/bv_brst.tex:42:\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
chapters/connections/bv_brst.tex:72:\label{rem:bv-bar-bridge}
chapters/connections/bv_brst.tex:1403:Conjecture~\ref{conj:master-bv-brst} at the scalar level
chapters/connections/bv_brst.tex:1409:\label{thm:heisenberg-bv-bar-all-genera}
chapters/connections/bv_brst.tex:1624:Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
chapters/connections/bv_brst.tex:1625:Conjecture~\ref{conj:master-bv-brst} at the \emph{scalar level}
chapters/connections/bv_brst.tex:1659:\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
chapters/connections/bv_brst.tex:1758:(Conjecture~\ref{conj:master-bv-brst})
chapters/connections/bv_brst.tex:1811:Conjecture~\ref{conj:master-bv-brst} at the scalar level for

thinking
**Searching for theorem details**

I need to find the full statement and proof of the theorem related to "thm:bv-bar-geometric." It seems the proof I have refers to this theorem at genus 0, but the user is focused on MC5 at a higher genus. I should confirm if the label exists and check its status. I’ll look into the full theorem statement and see if it relates to the user's needs based on genus distinctions.
exec
/bin/zsh -lc 'rg -n "thm:bv-bar-geometric|conj:master-bv-brst|thm:algebraic-string-dictionary|thm:general-hs-sewing|thm:heisenberg-bv-bar-all-genera|thm:heisenberg-sewing" chapters/connections/bv_brst.tex chapters/theory/higher_genus_foundations.tex chapters/connections/feynman_diagrams.tex chapters/connections/string_dictionary.tex chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1,350p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: chapters/connections/string_dictionary.tex: No such file or directory (os error 2)
chapters/connections/bv_brst.tex:36:(Conjecture~\ref{conj:master-bv-brst}; the classical-quantum bridge
chapters/connections/bv_brst.tex:42:\textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)}.
chapters/connections/bv_brst.tex:79: \textup{(}Theorem~\textup{\ref{thm:bv-bar-geometric}}, proved
chapters/connections/bv_brst.tex:92:Item~\textup{(i)} is Theorem~\ref{thm:bv-bar-geometric}. The scalar
chapters/connections/bv_brst.tex:181:\label{thm:bv-bar-geometric}
chapters/connections/bv_brst.tex:195:\begin{proof}[Geometric construction supporting \textup{Theorem~\ref{thm:bv-bar-geometric}}]
chapters/connections/bv_brst.tex:271:comparison of Theorem~\ref{thm:bv-bar-geometric}. Extending this to a
chapters/connections/bv_brst.tex:375:under the identification of Theorem~\ref{thm:bv-bar-geometric}.
chapters/connections/bv_brst.tex:1403:Conjecture~\ref{conj:master-bv-brst} at the scalar level
chapters/connections/bv_brst.tex:1409:\label{thm:heisenberg-bv-bar-all-genera}
chapters/connections/bv_brst.tex:1624:Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
chapters/connections/bv_brst.tex:1625:Conjecture~\ref{conj:master-bv-brst} at the \emph{scalar level}
chapters/connections/bv_brst.tex:1659:\textup{(}Conjecture~\ref{conj:master-bv-brst}\textup{)}
chapters/connections/bv_brst.tex:1758:(Conjecture~\ref{conj:master-bv-brst})
chapters/connections/bv_brst.tex:1811:Conjecture~\ref{conj:master-bv-brst} at the scalar level for
chapters/connections/bv_brst.tex:1846:This resolves Conjecture~\ref{conj:master-bv-brst} in
chapters/connections/bv_brst.tex:1923:Theorem~\ref{thm:bv-bar-geometric} and holds at the chain level.
chapters/theory/higher_genus_foundations.tex:864: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing})}.
chapters/theory/higher_genus_foundations.tex:932:(Theorem~\ref{thm:general-hs-sewing}) is a growth condition on
 succeeded in 50ms:
     1	\chapter{BV-BRST formalism and Gaiotto's perspective}
     2	\label{ch:bv-brst}
     3	\index{Batalin--Vilkovisky|see{BV algebra}}
     4	
     5	The physicist's BRST cohomology and the algebraist's bar resolution
     6	are not analogous: they are the same computation. The BV formalism
     7	is a machine for computing derived functors; the bar complex is a
     8	machine for computing derived functors; at genus~$0$, they are the
     9	same machine applied to the same input. Costello's formulation of
    10	perturbative QFT as the theory of derived moduli problems makes the
    11	identification inevitable: the BRST operator computes the derived
    12	space of gauge-equivalence classes, which is what the bar differential
    13	computes on the algebraic side. What requires proof is not the
    14	coincidence but the precise scope of the agreement.
    15	
    16	The BV Laplacian and the sewing operator agree at genus~$0$. The
    17	quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
    18	the BV formalism coincides on $\mathbb{P}^1$ with the bar
    19	differential $d_{\mathrm{bar}}$ of the chiral algebra: the
    20	BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the

thinking
**Searching for conjectures**

I need to locate the full statement and proof of the conjecture related to "master-bv-brst." It seems likely there’s a conjecture but no proof yet. So, I'll search around line 2300 to find relevant information. I'll take my time to read through it carefully to ensure I understand all the details. It’s important to clarify these points for accurate comprehension!
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2280,2385p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2280	genus-$0$ BRST presentation of the WZW model, so it remains to
  2281	identify the differentials on the PBW-associated graded.
  2282	
  2283	\emph{Step~2: PBW filtration and Chevalley--Eilenberg reduction.}
  2284	At generic level, Theorem~\ref{thm:km-chiral-koszul} and
  2285	Proposition~\ref{prop:km-generic-acyclicity} place $V_k(\fg)$ on the
  2286	chirally Koszul locus. On the BRST side, the associated graded
  2287	differential is the Chevalley--Eilenberg differential~$d_{\mathrm{CE}}$
  2288	of the current Lie algebra $\widehat{\fg}_{k,-}$ acting on the
  2289	vacuum module. On the bar side, the associated graded differential
  2290	is extracted from the simple-pole current OPE bracket
  2291	$J^a(z) J^b(w) \sim k\,\Omega^{ab}/(z-w) + f^{ab}{}_c J^c(w)/(z-w)$,
  2292	which is the same bracket that defines~$d_{\mathrm{CE}}$.
  2293	The filtered comparison therefore lifts the Chevalley--Eilenberg
  2294	identification to the full genus-$0$ complexes.
  2295	
  2296	\emph{Step~3: Degree propagation.}
  2297	Since $V_k(\fg)$ is chirally Koszul at generic level, the bar spectral
  2298	sequence collapses on the Koszul line and each finite-length summand of
  2299	$T^c(s^{-1}\overline{V_k(\fg)})$ is generated by the binary residue


thinking
**Assessing theorem registry and remarks**

I need to check the theorem registry because a remark might not be listed due to the absence of a ClaimStatus. In the theorem proof for class C chain-level vanishing, the reliance is solely on the remark. I should assess if this remark is not a proven claim and is more heuristic, which could be quite important. The line formatting needs inspection, as the remark title lacks a claim status tag. So, it appears it isn't a formally proven claim, but I should evaluate the logic further.
thinking
**Inspecting definitions in categories**

I need to look at the relevant definitions in coderived models and remarks related to bar cobar adjunction inversion or curved spaces. The theorem mentions quasi-isomorphic elements in the coderived category \(D^{co}(\mathcal{A})\), so I need to verify their existence and meaning. I'll dive into provisional coderived, adequacy, and coderived facts, along with remarks regarding derived-coderived reduction and curvature-derived concepts. I’m wondering if chiral co-contra correspondence is necessary, though the theorem proof doesn’t cite them.
codex
The proof is thinner than the concordance summary: `thm:bv-bar-coderived` itself only cites the genus-0 external theorem and the local obstruction proposition, then declares every higher discrepancy a power of `m_0`. I’m now checking whether that factorization is actually established anywhere, and whether the appendix definitions justify the move from `d^2 = m_0` to “the obstruction is exact in `D^{co}`.”
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '200,380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '520,780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '390,470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1290,1505p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3330,3368p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   200	\item $d \colon M \to M$ is a degree-$1$ map with
   201	 $d^2 = m_0 \in Z(M)$ for a central curvature element~$m_0$
   202	 (cf.\ the fiberwise differential $\dfib$ with $\dfib^{\,2} = \mcurv{g}$,
   203	 Convention~\textup{\ref{conv:higher-genus-differentials}});
   204	\item $\mathcal{F} = \{F^p M\}_{p \geq 0}$ is an exhaustive
   205	 decreasing filtration with $d(F^p) \subset F^p$,
   206	 $m_0 \in F^1$, and $\operatorname{gr}^0_{\mathcal{F}} d$ strict
   207	 ($(\operatorname{gr}^0 d)^2 = 0$).
   208	\end{enumerate}
   209	A morphism $f \colon (M, d, \mathcal{F}) \to (N, d', \mathcal{F}')$ is a
   210	filtration-preserving coalgebra map compatible with differentials and curvatures.
   211	\end{definition}
   212	
   213	\begin{definition}[Weak equivalence of curved models]
   214	\label{def:curved-weak-equiv}
   215	A morphism $f \colon M \to N$ of filtered curved factorization models
   216	is a \emph{weak equivalence} if it satisfies either of the following
   217	equivalent conditions:
   218	\begin{enumerate}[label=\textup{(\roman*)}]
   219	\item The associated graded map
 succeeded in 50ms:
   390	$D^{\mathrm{co}}(\bar{B}^{(g)}\text{-}\mathrm{CoMod})$~\cite[\S\S3--4]{Positselski11},
   391	which is why Theorem~\ref{thm:positselski-chiral} requires the
   392	coderived/contraderived setting.
   393	\end{remark}
   394	
   395	\begin{remark}[Derived--coderived reduction for chiral CDG-coalgebras]
   396	\label{rem:derived-coderived-chiral-CDG}
   397	\index{coderived category!derived reduction}
   398	\index{Positselski!derived--coderived reduction}
   399	The chiral bar complex $C = \bar{B}^{\mathrm{ch}}(\cA)$ is a CDG-coalgebra
   400	with curvature $h = m_0^{(g)}$. Three hypotheses govern the relationship
   401	between its coderived and ordinary derived categories:
   402	\begin{enumerate}[label=\textup{(H\arabic*)}]
   403	\item \emph{Conilpotency}: $C$ is conilpotent, i.e., the coaugmentation
   404	 filtration is exhaustive. This holds by
   405	 Theorem~\ref{thm:coalgebra-via-NAP}(4): the conformal weight grading
   406	 on $\bar{B}^{\mathrm{ch}}(\cA)$ provides an exhaustive
   407	 $\mathbb{N}$-filtration with $C = \bigcup_n F^n C$.
   408	\item \emph{Finite-type weight spaces}: each graded piece of $C$ is
   409	 finite-dimensional. This holds because $\cA$ is finitely generated
 succeeded in 51ms:
   520	\index{contraacyclic object!factorization|textbf}
   521	Let $(C, d, h)$ be a curved factorization coalgebra.
   522	\begin{enumerate}[label=\textup{(\roman*)}]
   523	\item A factorization CDG-comodule~$M$ is \emph{coacyclic} if it
   524	 belongs to the minimal thick subcategory
   525	 $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$
   526	 of the factorization homotopy category
   527	 $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
   528	 that contains the totalizations of all short exact sequences of
   529	 factorization CDG-comodules and is closed under
   530	 infinite direct sums.
   531	\item A factorization CDG-contramodule~$P$ is
   532	 \emph{contraacyclic} if it belongs to the minimal thick
   533	 subcategory
   534	 $\mathrm{Acycl}^{\mathrm{ctr}}_{\mathrm{fact}}$
   535	 with the dual closure: totalizations of exact triples and
   536	 infinite direct products.
   537	\end{enumerate}
   538	This is the factorization analogue of
   539	Definition~\ref{def:coacyclic-contraacyclic}. The factorization
 succeeded in 50ms:
  3330	loss of information. The adjunction
  3331	$\Omegach \dashv \barBch$ and the intertwining
  3332	$\mathbb{D}_{\operatorname{Ran}} \circ \barB_X \simeq \barB_X \circ
  3333	(-)^!$ are therefore two faces of a single structure: the bar functor
  3334	translates algebraic duality (Koszul) into geometric duality
  3335	(Verdier), and the cobar functor translates back. Every other
  3336	duality in the programme, whether Poincar\'e--Koszul on manifolds,
  3337	Serre on moduli, or the $c \mapsto 26 - c$ involution on the Virasoro
  3338	line, is a specialization of this single adjunction acting on
  3339	different geometric inputs.
  3340	\end{remark}
  3341	
  3342	\begin{remark}[Curvature and coderived categories]\label{rem:curvature-coderived}
  3343	\index{coderived category!bar-cobar}
  3344	\index{curvature!coderived category}
  3345	When curvature is present, i.e., when the genus-$1$ obstruction
  3346	$m_0^{(1)} = \kappa(\cA) \cdot \lambda_1 \neq 0$ (as it is for all
  3347	Koszul chiral algebras with $\kappa(\cA) \neq 0$; see
  3348	Theorem~\ref{thm:genus-universality}), the bar complex satisfies
  3349	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \mathrm{id}$ rather than $\dfib^{\,2} = 0$
 succeeded in 50ms:
  1290	Proposition~\ref{prop:chiral-inj-proj-resolutions}(a)--(b):
  1291	free graded contramodules are projective and cofree graded comodules
  1292	are injective, so $\Phi_C^{\mathrm{ch}}$ sends projective objects
  1293	to injective objects and vice versa.
  1294	\end{proof}
  1295	
  1296	\subsection{The chiral comodule-contramodule correspondence}
  1297	\label{subsec:chiral-co-contra-correspondence}
  1298	
  1299	\begin{theorem}[Chiral comodule-contramodule correspondence;
  1300	\ClaimStatusProvedHere]
  1301	\label{thm:chiral-co-contra-correspondence}
  1302	\index{comodule-contramodule correspondence!chiral|textbf}
  1303	\index{Positselski!chiral correspondence|textbf}
  1304	Let $(C, d, h)$ be a conilpotent chiral CDG-coalgebra on a smooth
  1305	curve $X$ with finite-dimensional graded pieces. The derived functors
  1306	\begin{align*}
  1307	\mathbb{L}\Phi_C^{\mathrm{ch}}\colon
  1308	D^{\mathrm{ctr}}(C\text{-}\mathrm{contra}^{\mathrm{ch}})
  1309	&\longrightarrow

thinking
**Evaluating curvature and proof claims**

I think I might need to read more lines after 3368, even if they aren't strictly necessary. A key remark mentions that in the coderived category, curvature isn't set to zero, which could conflict with the proof’s claim that m0 is exact or lies in Im(d) meaning curvature is negated. It seems I should check further up to line 3385 to clarify my understanding.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3342,3398p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  3342	\begin{remark}[Curvature and coderived categories]\label{rem:curvature-coderived}
  3343	\index{coderived category!bar-cobar}
  3344	\index{curvature!coderived category}
  3345	When curvature is present, i.e., when the genus-$1$ obstruction
  3346	$m_0^{(1)} = \kappa(\cA) \cdot \lambda_1 \neq 0$ (as it is for all
  3347	Koszul chiral algebras with $\kappa(\cA) \neq 0$; see
  3348	Theorem~\ref{thm:genus-universality}), the bar complex satisfies
  3349	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \mathrm{id}$ rather than $\dfib^{\,2} = 0$
  3350	(see Convention~\ref{conv:higher-genus-differentials} for the notation).
  3351	The ordinary derived category of $\cA$-modules is then the wrong
  3352	quotient: it erases the distinction between ``acyclic because of
  3353	$\dfib^{\,2} \neq 0$'' and ``acyclic because of genuine exactness.''
  3354	
  3355	The correct ambient category is the \emph{coderived category}
  3356	in the sense of Positselski~\cite{Positselski11}. In this category,
  3357	a curved complex $(M, d_M)$ with $d_M^2 = \kappa \cdot \mathrm{id}_M$
  3358	is \emph{not} set to zero; it represents a genuine object encoding the
  3359	curvature. On the intrinsic bar-coalgebra surface, the
  3360	Positselski comparison yields an equivalence
  3361	\[

thinking
**Analyzing curvature and morphism**

I’ve got proof showing that m0 is exact in Dco, but a remark says it’s not set to zero. I need to analyze this carefully. In the coderived category, an object with d^2 equals curvature remains nonzero, implying that m0 might be represented as a boundary. However, the remark insists that curvature isn't erased. I’m wondering if multiplication by curvature could be null-homotopic. I’ll check the definitions and search for “m0” exact in Im(d) elsewhere.
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"m_0 .*exact|m_0.*Im\\(d\\)|d\\"'^2 = m_0|m_0'"\\"'^k|coderived-trivial|coderived-exact|not set to zero|coacyclic" chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	
     2	\section{Coderived and contraderived categories}
     3	\label{app:coderived}
     4	\index{coderived category|textbf}
     5	\index{contraderived category|textbf}
     6	
     7	The bar-cobar adjunction at higher genus produces curved complexes
     8	($d^2 \neq 0$), for which ordinary cohomological derived methods
     9	are no longer the right invariant.
    10	Positselski's theory of coderived and contraderived
    11	categories~\cite{Positselski11} provides the correct
    12	replacement. This appendix collects the definitions and key results
    13	needed in this monograph; the chiral specialization appears in
    14	\S\ref{subsec:chiral-coderived-contraderived}.
    15	
    16	\subsection{Abstract definitions}
    17	\label{subsec:coderived-abstract}
    18	
    19	Let $\mathsf{A}$ be an abelian category with exact direct sums
    20	(for the coderived case) or exact direct products
 succeeded in 51ms:
chapters/connections/bv_brst.tex:1842:$D^{\mathrm{co}}$, so $\delta_4$ is coderived-trivial.
chapters/connections/bv_brst.tex:1946:$d^2 = m_0 \cdot \mathrm{id}$ holds by definition.
chapters/connections/bv_brst.tex:1955:since $m_0^k = d^{2k-1}(d(\cdot))$ is exact in $D^{\mathrm{co}}$
chapters/connections/bv_brst.tex:1979:($m_0^k \in \operatorname{Im}(d)$ for $k \geq 1$) is algebraic and
chapters/connections/bv_brst.tex:2033:$d^2 = m_0 \cdot \mathrm{id}$ is permitted. The bar complex
chapters/theory/coderived_models.tex:57:\label{def:coacyclic-contraacyclic}
chapters/theory/coderived_models.tex:58:\index{coacyclic object|textbf}
chapters/theory/coderived_models.tex:62:\item A CDG-comodule $M$ is \emph{coacyclic} if it belongs to the
chapters/theory/coderived_models.tex:93:object is coacyclic (resp.\ contraacyclic), so there are natural
chapters/theory/coderived_models.tex:130:CDG-comodule is coacyclic, so the coderived category coincides
chapters/theory/coderived_models.tex:201: $d^2 = m_0 \in Z(M)$ for a central curvature element~$m_0$
chapters/theory/coderived_models.tex:223:\item The induced map on coacyclic quotients
chapters/theory/coderived_models.tex:326: localization of the homotopy category at coacyclic objects, those
chapters/theory/coderived_models.tex:329: Definition~\ref{def:coacyclic-contraacyclic}).
chapters/theory/coderived_models.tex:518:\label{def:coacyclic-fact}
chapters/theory/coderived_models.tex:519:\index{coacyclic object!factorization|textbf}
chapters/theory/coderived_models.tex:523:\item A factorization CDG-comodule~$M$ is \emph{coacyclic} if it
chapters/theory/coderived_models.tex:539:Definition~\ref{def:coacyclic-contraacyclic}. The factorization
chapters/theory/coderived_models.tex:542:through any additional axiom on the coacyclicity condition.
chapters/theory/coderived_models.tex:609:triples and direct sums. Hence it sends coacyclic factorization
exec
/bin/zsh -lc "rg -n \"delta_4\\"'^'"\\{harm\\}|Q\\"'^'"\\{contact\\}|harmonic decoupling|Jacobi kills harmonic|quartic harmonic|not a coboundary|1/\\\\mathrm\\{Im\\}\\(\\\\tau\\)|m_0 \\cdot x = d\\"'^2|m_0'"\\"'^'"\\{\\\\lfloor r/2 \\\\rfloor - 1\\}|c_r\\(\\\\cA\\)|shadow depth r_\\{\\\\max\\} = 3|shadow depth r_\\{\\\\max\\} = 4|class~M.*false|chain-level.*false\" chapters/connections/bv_brst.tex chapters/connections/concordance.tex chapters/examples chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1388,1660p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:delta_4\^\{harm\}|Q\^\{contact\}|harmonic decoupling|Jacobi kills harmonic|quartic harmonic|not a coboundary|1/\mathrm\{Im\}\(\tau\)|m_0 \cdot x = d\^2|m_0\^\{\lfloor r/2 \rfloor - 1\}|c_r\(\cA\)|shadow depth r_\{\max\} = 3|shadow depth r_\{\max\} = 4|class~M.*false|chain-level.*false)
                                                                                                                      ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  1388	$(-1)$-shifted Poisson model for the deformation theory. The
  1389	unconditional shifted-symplectic statements used later in the
  1390	manuscript instead come from the Verdier pairing on
  1391	$C_g = R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$
  1392	\textup{(}Proposition~\ref{prop:ptvv-lagrangian}\textup{)} and from
  1393	the ambient cyclic deformation formal moduli problem
  1394	\textup{(}Theorem~\ref{thm:ambient-complementarity-fmp}\textup{)}.
  1395	\end{remark}
  1396	
  1397	\section{Resolution for the Heisenberg algebra at all genera}
  1398	\label{sec:bv-bar-heisenberg-all-genera}
  1399	\index{Heisenberg!BV/bar identification|textbf}
  1400	\index{BV algebra!bar complex identification!Heisenberg}
  1401	
  1402	The free-field case resolves
  1403	Conjecture~\ref{conj:master-bv-brst} at the scalar level
  1404	for the Heisenberg family. The proof uses four independent
  1405	arguments that all produce the same identity.
  1406	
  1407	\begin{theorem}[BV $=$ bar for the Heisenberg at all genera;



thinking
**Analyzing mathematical inconsistencies**

I see that remark 1624 suggests the Heisenberg theorem resolves only at a scalar level, while another part states that chain-level is proved for class G. That's puzzling! I need to check if the theorem and later propositions clarify this chain-level for G. The chain-level issues seem critical, especially since class G appears absent while classes L and C are resolved. I'll look into this potential contradiction more closely and verify everything around these claims.
thinking
**Investigating chain-level theorems**

I'm noticing a disagreement here: no theorem establishes chain-level for G, yet the earlier remark mentioned it's open. This might signal a significant status inflation. I need to dig deeper to see if the later proposition claims chain-level identification or simply mentions obstructions. It indicates that class G is absent, while L and C are resolved at genus 1, and class M is open. The proof from 1938-1941 suggests that obstructions vanish, but it doesn't prove quasi-isomorphism. There’s definitely an incomplete leap in reasoning!
thinking
**Searching for chain-level identification**

I need to take a closer look at the conj master-bv-brst statement to clarify what chain-level identification really means. I'm wondering if the label might be located elsewhere, possibly outside this chapter? It feels crucial to search the entire repository to find any relevant information. I want to ensure I gather all the necessary details to fully understand this concept, so let's dive in and explore!
codex
A stronger inconsistency has surfaced inside the chapter itself. `thm:heisenberg-bv-bar-all-genera` is explicitly labeled scalar-only at [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1624), but the later class table upgrades class `G` to chain-level proved at [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1821). I’m checking whether any actual chain-level theorem exists elsewhere, or whether the coderived proof is leaning on an unproved upgrade.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2055,2285p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{conj:master-bv-brst\\}|Conjecture~\\\\ref\\{conj:master-bv-brst\\}|master-bv-brst|chain-level quasi-isomorphism|BV Laplacian.*sewing operator|Delta_\\\\mathrm\\{BV\\} = d_\\\\mathrm\\{sew\\}|BV complex and the bar complex\" chapters metadata" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{conj:master-bv-brst\}|Conjecture~\ref\{conj:master-bv-brst\}|master-bv-brst|chain-level quasi-isomorphism|BV Laplacian.*sewing operator|Delta_\mathrm\{BV\} = d_\mathrm\{sew\}|BV complex and the bar complex)
                                                                                                                                                            ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  2055	\end{remark}
  2056	
  2057	\section{Non-Calabi--Yau local surfaces and the Burns datum}
  2058	\label{sec:non-cy-local-surfaces}
  2059	\index{Burns space|textbf}
  2060	\index{local surface!non-Calabi--Yau}
  2061	
  2062	The holomorphic-topological boundary VOAs of twisted supergravity
  2063	on non-Calabi--Yau local surfaces furnish a family of class~$\mathsf{C}$
  2064	algebras whose Koszul datum is controlled by a single integer
  2065	\textup{(}the rank of the characteristic lattice\textup{)}. The Burns
  2066	space is the simplest member.
  2067	
  2068	\begin{computation}[Burns space Koszul datum;
  2069	\ClaimStatusProvedElsewhere]
  2070	\label{comp:burns-koszul-datum}
  2071	\index{Burns space!Koszul datum}
  2072	\index{$\beta\gamma$ system!Burns}
  2073	The boundary VOA of the Burns space consists of four $\beta\gamma$
  2074	pairs with an $SO(8)$ global symmetry, giving:
exec
/bin/zsh -lc 'rg -n "conj:master-bv-brst|master-bv-brst" chapters metadata' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/deformation_quantization.tex:711:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
metadata/dependency_graph.dot:296:  conj_master_bv_brst [label="conj:master-bv-brst\nconjecture [Co]\nBV/BRST/bar identification", style=filled, fillcolor="#fff9c4"];
chapters/examples/free_fields.tex:4892:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
chapters/examples/free_fields.tex:4918:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
chapters/examples/free_fields.tex:5010:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
chapters/examples/free_fields.tex:5091:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
chapters/examples/free_fields.tex:5279:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
metadata/label_index.json:2550:  "conj:master-bv-brst": {
chapters/examples/kac_moody.tex:2062:(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
metadata/claims.jsonl:178:{"label": "prop:chain-level-three-obstructions", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1646, "title": "Three chain-level obstructions", "refs_in_block": ["conj:master-bv-brst", "rem:bv-bar-class-c-proof"]}
metadata/claims.jsonl:230:{"label": "conj:vol2-bv-functor-bridge", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/concordance.tex", "line": 4498, "title": "BV functor bridge", "refs_in_block": ["conj:master-bv-brst"]}
metadata/claims.jsonl:246:{"label": "rem:four-test-interface", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 7345, "title": "The four-test interface", "refs_in_block": ["thm:bar-modular-operad", "thm:quantum-diff-squares-zero", "thm:mc2-bar-intrinsic", "thm:modular-characteristic", "thm:algebraic-family-rigidity", "thm:quantum-complementarity-main", "thm:ambient-complementarity-fmp", "thm:general-hs-sewing", "rem:thqg-I-admissible", "thm:heisenberg-sewing", "op:multi-generator-universality", "thm:multi-weight-genus-expansion", "thm:heisenberg-bv-bar-all-genera", "conj:master-bv-brst", "conj:analytic-realization"]}
metadata/claims.jsonl:283:{"label": "conj:master-bv-brst", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 434, "title": "BV/BRST/bar identification", "refs_in_block": ["thm:bv-bar-coderived", "thm:master-pbw", "thm:master-theta", "conj:master-dk-kl", "conj:master-infinite-generator", "thm:algebraic-string-dictionary", "cor:string-amplitude-genus0"]}
metadata/claims.jsonl:317:{"label": "conj:bar-cobar-path-integral", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/feynman_connection.tex", "line": 182, "title": "Bar-cobar as worldsheet path integral: general case", "refs_in_block": ["thm:bar-cobar-path-integral-heisenberg", "conj:master-bv-brst"]}
metadata/claims.jsonl:357:{"label": "thm:kz-classical-quantum-bridge", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/frontier_modular_holography_platonic.tex", "line": 1781, "title": "Classical-to-quantum bridge: proved algebraic content", "refs_in_block": ["thm:collision-residue-twisting", "thm:w3-genus1-curvature", "thm:mc2-bar-intrinsic", "conj:master-bv-brst"], "cites_in_block": ["GLZ22", "KhanZeng25"]}
metadata/claims.jsonl:429:{"label": "conj:holographic-bar-cobar", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/genus_complete.tex", "line": 709, "title": "Holographic duality via bar-cobar", "refs_in_block": ["conj:master-bv-brst", "chap:concordance"], "cites_in_block": ["Wit89"]}
metadata/claims.jsonl:1099:{"label": "conj:deformation-holographic", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/deformation_quantization.tex", "line": 705, "title": "Holographic duality", "refs_in_block": ["conj:master-bv-brst"]}
metadata/claims.jsonl:1176:{"label": "conj:string-amplitude-higher-genus", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/free_fields.tex", "line": 4881, "title": "String amplitude correspondence,\n\\texorpdfstring{$g \\geq 1$}{g 1}", "refs_in_block": ["thm:genus-g-chiral-homology", "conj:master-bv-brst"]}
metadata/claims.jsonl:1177:{"label": "conj:bulk-boundary-correspondence", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/free_fields.tex", "line": 4913, "title": "Bulk-boundary correspondence", "refs_in_block": ["conj:master-bv-brst"]}
metadata/claims.jsonl:1180:{"label": "conj:loop-string-coupling", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/free_fields.tex", "line": 5005, "title": "Loop corrections as string coupling", "refs_in_block": ["conj:master-bv-brst"]}
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '404,470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/outlook.tex | sed -n '650,710p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   404	Corollary~\ref{cor:winfty-stage4-residue-four-channel}.
   405	
   406	On the standard type-$A$ Yangian side, the local coefficient packet is
   407	already closed on the factorization-side shared-seed locus. The
   408	canonical H-level target exists as the tangent Lie algebra of the
   409	factorization formal moduli problem
   410	(Proposition~\ref{prop:yangian-canonical-hlevel-target}), with
   411	canonical associative dg model
   412	(Proposition~\ref{prop:yangian-canonical-envelope}). The next step is
   413	to equip that dg model with the RTT-adapted package of
   414	Proposition~\ref{prop:yangian-typea-realization-criterion}, after
   415	which
   416	Corollary~\ref{cor:yangian-canonical-realization-to-spectral-seed}
   417	reduces the remaining input to the spectral vector-line realization
   418	package; on the equivariant multiplicative spectral realization locus,
   419	this is equivalently the standard spectral vector seed-and-shift
   420	datum. On the spectral vector-line locus,
   421	Corollary~\ref{thm:yangian-canonical-realization-plus-vector-line}
   422	closes DK-4/DK-5 on the canonical target; on the sharper equivariant
   423	multiplicative spectral realization locus,
 succeeded in 52ms:
   650	\label{sec:principal-contributions}
   651	\label{rem:four-levels}
   652	\label{subsec:anomaly-koszul}
   653	\label{subsec:vassiliev}
   654	\label{rem:en-scope}
   655	\label{rem:proof-roadmaps}
   656	\label{rem:structural-gaps}
   657	\label{rem:cat-o-generation-obstruction}
   658	
   659	% Concordance theorems/conjectures (full statements in editorial companion)
   660	\phantomsection\label{thm:family-index}
   661	\phantomsection\label{thm:universal-MC}
   662	\phantomsection\label{thm:volume-one-concrete-modular-datum}
   663	\phantomsection\label{thm:master-theta}
   664	\phantomsection\label{thm:master-pbw}
   665	\phantomsection\label{thm:discriminant-spectral}
   666	\phantomsection\label{thm:lagrangian-complementarity}
   667	\phantomsection\label{thm:anomaly-koszul}
   668	\phantomsection\label{conj:derived-drinfeld-kohno}
   669	\phantomsection\label{conj:categorical-modular-kd}
exec
/bin/zsh -lc "rg -n \"not a coboundary|quartic harmonic obstruction|quartic harmonic discrepancy|delta_4|Q\\"'^'"\\{contact\\}|harmonic-propagator correction|Fay trisecant|1/Im\\(\\\\tau\\)|non-holomorphic and hence not in the image|class~M chain-level false|chain-level identification remains false\" chapters metadata" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/dependency_graph.dot:2346:  prop_fay_trisecant [label="prop:fay-trisecant\nproposition [Pr]\nFay trisecant identity for the Szeg\H{o}...", style=filled, fillcolor="#bbdefb"];
chapters/examples/toroidal_elliptic.tex:19:the Fay trisecant identity and quasi-periodicity
chapters/examples/toroidal_elliptic.tex:25:generalizes to the Fay trisecant identity
chapters/examples/toroidal_elliptic.tex:54:The Arnold relation (Theorem~\ref{thm:arnold-relations}), which governs the genus-$0$ bar differential, admits two distinct generalizations. Direction~(a): via clutching morphisms and the shadow obstruction tower $\Theta_A^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), one passes to the modular regime on stable curves, recovering the higher-genus bar complex of Part~\ref{part:bar-complex} (Remark~\ref{rem:five-pieces}). Direction~(b): via the Fay trisecant identity (Theorem~\ref{thm:fay}), one replaces the additive (logarithmic) propagator $\omega = dz/(z-w)$ by the elliptic (multiplicative) propagator built from the Weierstrass $\sigma$-function, entering the toroidal regime. The present chapter develops direction~(b): the systematic passage from logarithmic to elliptic propagators and its consequences for bar-cobar duality.
chapters/examples/toroidal_elliptic.tex:90:\item The Fay trisecant identity for $\vartheta_1$ is the genus-$1$ MC equation $D^{(1)}\Theta + \tfrac{1}{2}[\Theta^{(0)}, \Theta^{(0)}] + \kappa\,\omega_1 = 0$.
chapters/examples/toroidal_elliptic.tex:377:\index{Fay trisecant identity|textbf}
chapters/examples/toroidal_elliptic.tex:379:satisfies the Fay trisecant identity:
chapters/examples/toroidal_elliptic.tex:383:This is a \emph{bilinear} identity (each term is a product of two theta functions), which at genus~1 is the degenerate case of the general Fay trisecant identity on higher-genus curves. The identity is equivalent to the Riemann addition formula and reduces to the Ptolemy relation $\sin(\alpha-\beta)\sin(\gamma-\delta) - \sin(\alpha-\gamma)\sin(\beta-\delta) + \sin(\alpha-\delta)\sin(\beta-\gamma) = 0$ in the rational limit $\tau \to i\infty$.
chapters/examples/toroidal_elliptic.tex:395:\index{Fay trisecant identity!and bar nilpotency}
chapters/examples/toroidal_elliptic.tex:397:$d^2 = 0$. The key algebraic input is the Fay trisecant identity
chapters/examples/toroidal_elliptic.tex:938:reduces to the Fay trisecant (Theorem~\ref{thm:fay}). The
chapters/examples/toroidal_elliptic.tex:1061:\index{Fay trisecant identity!and dynamical YBE}
chapters/examples/toroidal_elliptic.tex:1065:is equivalent to the Fay trisecant identity
chapters/examples/toroidal_elliptic.tex:1301:& Fay trisecant \\
chapters/examples/toroidal_elliptic.tex:1374:$d\log\theta_1$, the Fay trisecant relation governing $d^2 = 0$
chapters/examples/toroidal_elliptic.tex:2937:$\delta_3 = 600$, $\delta_4 = 8100$, matching the G\"ottsche
metadata/claims.jsonl:2249:{"label": "prop:fay-trisecant", "env_type": "proposition", "status": "ProvedElsewhere", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 2292, "title": "Fay trisecant identity for the Szeg\\H{o} kernel {\\cite[Corollary~2.5", "labels_in_block": ["prop:fay-trisecant", "eq:algebraic-fay"], "cites_in_block": ["Fay73"]}
chapters/frame/preface_sections10_13_draft.tex:368:MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera; the genus-$0$ algebraic BRST/bar comparison is proved; BV=bar in the coderived category is proved for all four shadow classes (including class~M). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional.
chapters/frame/preface_sections10_13_draft.tex:435:(Conjecture~\ref{conj:master-bv-brst}; class~M chain-level false).
chapters/connections/concordance.tex:3293: (class~M chain-level false; Conjecture~\ref{conj:master-bv-brst});

thinking
**Inspecting mathematical claims**

I need to look into the δ4 statement and the en_koszul_duality topic for potential repetitions. It might help to explore concordance lines around references 10082 and 10120, especially if the claim isn't accurately described as a coboundary or coderived. I'll also check line references like 7610 for similar issues. As requested, I’ll focus on chapters to ensure thoroughness, and aim to report findings accurately regarding any propagated issues. Let's read those sections carefully.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '10082,10130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7606,7620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3388,3444p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3440,3460p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7606	\label{rem:concordance-frontier-status-2026}
  7607	\index{open conjectures!frontier status 2026}
  7608	The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
  7609	\begin{enumerate}
  7610	\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
  7611	 \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
  7612	\item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  7613	 Restricted DK-4 on the evaluation-generated core is the next step.
  7614	\item \textup{Conjecture~\ref{conj:master-infinite-generator} (infinite-generator completion).}
  7615	 MC4 framework proved; example-specific $H$-level target identification remains. $\Walg_\infty$ side essentially closed.
  7616	\item \textup{Conjecture~\ref{conj:w-orbit-duality} (W-algebra orbit duality).}
  7617	 Non-abelian~$\mathfrak{n}_+$ obstruction. The $(3,2)$ partition in $\mathfrak{sl}_5$ is the first test case.
  7618	\item \textup{Conjecture~\ref{conj:grand-completion} (grand modular completion).}
  7619	 Model category equivalence extending genus-$0$ Quillen. Principal open structural problem.
  7620	\item \textup{Conjecture~\ref{conj:ds-kd-arbitrary-nilpotent} (DS--KD for arbitrary nilpotent).}
 succeeded in 51ms:
 10082	 (Conjecture~\ref{conj:master-bv-brst}).
 10083	
 10084	 \smallskip\noindent
 10085	 \emph{Resolution in $D^{\mathrm{co}}$.}
 10086	 \textbf{Resolved} in the coderived category
 10087	 (Theorem~\ref{thm:bv-bar-coderived}):
 10088	 for every chirally Koszul algebra~$\cA$, the BV complex and the
 10089	 bar complex are quasi-isomorphic in $D^{\mathrm{co}}(\cA)$ at
 10090	 all genera. The key mechanism for class~M: the degree-$r$
 10091	 chain-level obstruction satisfies
 10092	 $\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, and in
 10093	 $D^{\mathrm{co}}$ the curvature acts as
 10094	 $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$, so every
 10095	 $\delta_r$ is coderived-exact.
 10096	
 10097	 \smallskip\noindent
 10098	 \emph{Chain-level status.}
 10099	 For the Heisenberg algebra $\cH_\kappa$, the scalar-level
 10100	 identification
 10101	 $F_g^{\mathrm{BV}}(\cH_\kappa)
 succeeded in 51ms:
  3440	step~(iv) of
  3441	Remark~\ref{rem:topologization-chain-vs-cohomology} from
  3442	cohomology to a chain-level statement. The mechanism is uniform
  3443	across all four shadow classes: the obstruction to local constancy
  3444	of the factorization algebra on the holomorphic direction is a
  3445	polynomial in the fiberwise curvature $m_0 = \kappa(\cA) \cdot
  3446	\omega_g$; in $D^{\mathrm{co}}$, every positive power of $m_0$
  3447	is exact ($m_0^k = d^{2k-1}(d(\cdot)) \in \operatorname{Im}(d)$
  3448	for $k \geq 1$), so the obstruction is absorbed.
  3449	
  3450	For class~$\mathsf{M}$ (Virasoro, $\cW_N$), this is the only
  3451	available path to $\Ethree$: the chain-level $\Ethree$ does not
  3452	exist (the quartic discrepancy $\delta_4 = Q^{\mathrm{contact}}
  3453	\cdot m_0$ is not a coboundary in ordinary chain complexes),
  3454	and the cohomological $\Ethree$ requires $3$d gravity BRST
  3455	(Volume~II). The coderived $\Ethree$ would provide a purely
  3456	algebraic $\Ethree$-structure for class~$\mathsf{M}$ without
  3457	invoking the bulk gravity theory.
  3458	
  3459	Two obstructions to a proof must be addressed.
 succeeded in 51ms:
  3388	\item \textup{(Coderived local constancy.)}
  3389	  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  3390	  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
  3391	  is locally constant. Precisely: the
  3392	  $m_0$-curvature obstruction to local constancy at
  3393	  step~\textup{(iv)} of
  3394	  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
  3395	  lies in $\operatorname{Im}(d)$ in $D^{\mathrm{co}}$, by the
  3396	  same mechanism that absorbs $\delta_4$ in
  3397	  Theorem~\textup{\ref{thm:bv-bar-coderived}}.
  3398	\item \textup{(Coderived $\Ethree$.)}
  3399	  The locally-constant recognition principle
  3400	  \textup{(}Lurie~\cite{HA}\textup{)}, adapted to the
  3401	  coderived setting, equips the derived chiral center
  3402	  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ with an
  3403	  $\Etwo^{\mathrm{top}}$-structure in $D^{\mathrm{co}}$.
  3404	  Combined with the $\Eone^{\mathrm{top}}$-structure from
  3405	  the open color of $\mathsf{SC}^{\mathrm{ch,top}}$, Dunn
  3406	  additivity gives an $\Ethree^{\mathrm{top}}$-structure in
  3407	  $D^{\mathrm{co}}$.
codex
I have enough local evidence that the chapter is blurring three different things: scalar equalities, obstruction vanishing, and actual chain-level quasi-isomorphisms. I’m now reading the advertised analytic theorem and the genus-0 algebraic theorem so the final report can separate “proved analytic”, “proved scalar”, “proved chain”, and “proved only in `D^{co}`” precisely.
exec
/bin/zsh -lc "rg -n \"label\\{thm:general-hs-sewing\\}|label\\{thm:heisenberg-sewing\\}|label\\{thm:algebraic-string-dictionary\\}|algebraic-string-dictionary|general-hs-sewing|heisenberg-sewing\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '820,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "algebraic BRST/bar|BRST/bar comparison|string dictionary|genus-0.*BRST|BRST.*bar" chapters/connections chapters/examples chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/lattice_foundations.tex:161:Theorem~\ref{thm:general-hs-sewing} then gives HS-sewing
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
chapters/examples/heisenberg_eisenstein.tex:227:\begin{remark}\label{rem:heisenberg-sewing-status}
chapters/examples/heisenberg_eisenstein.tex:2041:\label{subsec:heisenberg-sewing-cocomposition}
chapters/examples/heisenberg_eisenstein.tex:2414:(\eqref{eq:thqg-X-polyakov}, Theorem~\ref{thm:thqg-X-heisenberg-sewing-full}(IV)),
chapters/examples/heisenberg_eisenstein.tex:2490: (Theorem~\ref{thm:heisenberg-sewing}): the sewing envelope is
chapters/examples/toroidal_elliptic.tex:3948: Theorem~\ref{thm:general-hs-sewing}.
chapters/examples/free_fields.tex:4745:\ClaimStatusProvedHere]\label{thm:algebraic-string-dictionary}
chapters/frame/preface_sections10_13_draft.tex:425:Theorem~\ref{thm:general-hs-sewing}), and the Heisenberg one-particle
chapters/frame/preface_sections10_13_draft.tex:429:(Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
chapters/frame/preface_sections10_13_draft.tex:563: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
chapters/connections/arithmetic_shadows.tex:1894: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)};
chapters/connections/arithmetic_shadows.tex:4822:\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
chapters/connections/arithmetic_shadows.tex:4990:\textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)},
chapters/connections/arithmetic_shadows.tex:8113: \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing}}\textup{)}.
chapters/connections/arithmetic_shadows.tex:8609:(Theorem~\ref{thm:general-hs-sewing}) gives polynomial growth.
chapters/connections/arithmetic_shadows.tex:8835: (Theorem~\ref{thm:general-hs-sewing}).
chapters/connections/arithmetic_shadows.tex:8871:(Theorem~\ref{thm:general-hs-sewing}) ensures
chapters/connections/arithmetic_shadows.tex:9905:(Theorem~\ref{thm:general-hs-sewing})
chapters/connections/holomorphic_topological.tex:1076: & \checkmark\;Thm~\ref{thm:general-hs-sewing} \\
 succeeded in 51ms:
   820	\begin{enumerate}[label=\textup{(\roman*)}]
   821	\item \emph{Algebraic \textup{(}bar $D^2=0$ at all genera\textup{)}.}\;
   822	 For \emph{any} chiral algebra $\cA$, the bar differential satisfies
   823	 $D_\cA^2 = 0$ at all genera, and the universal MC element
   824	 $\Theta_\cA := D_\cA - d_0 \in \MC(\gAmod)$ exists
   825	 unconditionally
   826	 \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
   827	 No finiteness or Koszulness condition is required: $D^2 = 0$
   828	 is a formal consequence of $\partial^2 = 0$ on
   829	 $\overline{\cM}_{g,n}$.
   830	
   831	\item \emph{Homotopical \textup{(}bar-cobar inversion in
   832	 $D^{\mathrm{co}}$\textup{)}.}\;
   833	 If $\cA$ has finite-dimensional weight spaces
   834	 \textup{(}the positive-energy axiom\textup{)}, then the
   835	 genus-$g$ bar-cobar adjunction
   836	 $\barBch_g \dashv \Omegach_g$ extends to an equivalence
   837	 in the coderived category $D^{\mathrm{co}}$
   838	 \textup{(}Appendix~\textup{\ref{app:coderived-models})}.
   839	 The positive-energy condition ensures the weight-by-weight
 succeeded in 50ms:
chapters/connections/typeA_baxter_rees_theta.tex:53:the BV/BRST/bar comparison; see Chapter~\ref{chap:concordance}. The
chapters/connections/physical_origins.tex:18:and the proved genus-$0$ BRST--bar quasi-isomorphism
chapters/examples/w_algebras_deep.tex:1415:says the BRST ghost complex \emph{is} the bar complex. The geometric
chapters/examples/w_algebras_deep.tex:1486:The two-step collapse $(\mathrm{BRST}$-$E_0, \mathrm{bar}$-$E_1)$
chapters/examples/w_algebras_deep.tex:2699:and apply BRST reduction at the end. The bare affine tower
chapters/examples/w_algebras_deep.tex:2729:the BRST reduction of the bar differential
chapters/connections/editorial_constitution.tex:49:BV/BRST/bar identification
chapters/connections/editorial_constitution.tex:149:MC5 & BV/BRST $=$ bar
chapters/connections/editorial_constitution.tex:184:Fredholm determinant\textup{)}. The remaining genuswise BV/BRST/bar
chapters/connections/editorial_constitution.tex:186:BRST/bar comparison is proved
chapters/connections/editorial_constitution.tex:433:\begin{conjecture}[BV/BRST/bar identification]
chapters/connections/editorial_constitution.tex:453:same logical level. Genus-$0$ algebraic BRST/bar comparison: proved
chapters/connections/editorial_constitution.tex:591:\item the genus-$0$ algebraic BRST/bar package and the higher-genus
chapters/connections/editorial_constitution.tex:597:standard towers outside the higher-genus BV/BRST/bar identification
chapters/connections/editorial_constitution.tex:647:packages. The only further content is the genuswise BV/BRST/bar
chapters/connections/editorial_constitution.tex:650:complexes in the sense of the genus-$0$ algebraic BRST/bar package of
chapters/connections/editorial_constitution.tex:681:\item the genus-$0$ algebraic BRST/bar package and the higher-genus
chapters/connections/editorial_constitution.tex:698:obstruction beyond the genuswise BV/BRST/bar comparison, and
chapters/connections/editorial_constitution.tex:820: & HS-sewing / convergence proved; BV/BRST-bar comparison,
chapters/connections/editorial_constitution.tex:897:component is \textbf{proved}, but the genuswise BV/BRST/bar
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '438,670p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '180,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '4728,4778p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:brst-bar-genus0\\}|label\\{thm:algebraic-string-dictionary\\}\" chapters/connections/bv_brst.tex chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   438	\section{The genus-\texorpdfstring{$0$}{0} BRST-bar chain map}
   439	\label{sec:brst-bar-chain-map}
   440	\index{BRST!bar complex chain map|textbf}
   441	
   442	\subsection{Setup: the BRST complex}
   443	
   444	Let $\cA$ be a conformal vertex algebra of central charge~$c$ on
   445	$X = \mathbb{P}^1$, and let $\cA_{\mathrm{gh}} = bc$ denote the
   446	$bc$-ghost system of weights $(2, -1)$ with $c_{\mathrm{gh}} = -26$.
   447	The \emph{BRST complex} of~$\cA$ is the vertex algebra
   448	$\cA_{\mathrm{tot}} = \cA \otimes \cA_{\mathrm{gh}}$ equipped with
   449	the BRST differential:
   450	\begin{equation}\label{eq:brst-differential}
   451	Q_{\mathrm{BRST}}
   452	= \oint \! c(z)\Bigl(T_{\cA}(z) + \tfrac{1}{2}\,T_{\mathrm{gh}}(z)\Bigr)\,dz
   453	= \sum_{n \in \mathbb{Z}} \Bigl(
   454	 \sum_m L^{\cA}_m\, c_{n-m}
   455	 + \tfrac{1}{2}\sum_{p+q=n}(p-q)\, {:}b_p\, c_q\, c_{n-p-q}{:}
   456	\Bigr)
   457	\end{equation}
 succeeded in 51ms:
   180	of the affine Heisenberg vertex algebra. This suggests that the
   181	sewing envelope (\S\ref{sec:analytic-completion}) of the algebraic
   182	Heisenberg VOA is exactly $\operatorname{Sym} A^2(D)$, making
   183	the Heisenberg the first model in which the entire analytic
   184	completion programme is explicit.
   185	\end{remark}
   186	
   187	\begin{theorem}[Heisenberg sewing theorem;
   188	\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
   189	\index{Heisenberg!sewing theorem}%
   190	Under the mode--Bergman correspondence~$\Theta$
   191	\textup{(}Remark~\textup{\ref{rem:heisenberg-mode-bergman}}\textup{)}:
   192	\begin{enumerate}[label=\textup{(\roman*)}]
   193	\item \textup{(\ClaimStatusProvedElsewhere, Moriwaki~\cite{Moriwaki26b})}
   194	 The sewing envelope of the algebraic Heisenberg VOA is exactly
   195	 $\operatorname{Sym} A^2(D)$.
   196	\item \textup{(\ClaimStatusProvedHere)}
   197	 The completed bar differential is the closure of the Gaussian
   198	 collision operator on Bergman tensors.
   199	\item \textup{(\ClaimStatusProvedHere)}
 succeeded in 50ms:
chapters/examples/free_fields.tex:4745:\ClaimStatusProvedHere]\label{thm:algebraic-string-dictionary}
chapters/connections/bv_brst.tex:487:\label{thm:brst-bar-genus0}
 succeeded in 52ms:
  4728	\end{conjecture}
  4729	
  4730	\begin{remark}[Evidence]
  4731	The proved input is Theorem~\ref{thm:brst-bar-genus0}, which compares
  4732	the relative BRST complex of the critical string with the genus-$0$ bar
  4733	complex. The additional steps needed to isolate the matter Virasoro
  4734	bar complex and treat the ghost sector as an explicit Koszul factor are
  4735	not established in the manuscript, so the displayed matter-only
  4736	isomorphism remains heuristic.
  4737	\end{remark}
  4738	 
  4739	
  4740	\subsection{String theory and holographic dualities}
  4741	
  4742	\subsubsection{The algebraic string theory dictionary}
  4743	
  4744	\begin{theorem}[Algebraic bar/BRST genus dictionary;
  4745	\ClaimStatusProvedHere]\label{thm:algebraic-string-dictionary}
  4746	\index{string theory!algebraic dictionary}
  4747	The algebraic package behind

thinking
**Searching for theorem proofs**

I'm looking for the theorem `general-hs-sewing`, focusing on statements and proofs. I need to check a resource, specifically searching for this theorem in `genus_complete`, possibly around line 1386. It seems I only need the statement for now. I'll read around that area to gather more context. Hopefully, this will give me the information I need to move forward. Let's see what I can find!
exec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1386,1468p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1386	\label{thm:general-hs-sewing}%
  1387	\index{HS-sewing!general criterion|textbf}%
  1388	Let\/ $\cA$ be a positive-energy chiral algebra with
  1389	\textup{(i)}~subexponential sector growth $\log\dim H_n = o(n)$
  1390	and \textup{(ii)}~polynomial OPE growth
  1391	$|C^{c,k}_{a,i;\,b,j}| \leq K(a+b+c+1)^N$.
  1392	Then $\cA$ satisfies HS-sewing for every $0 < q < 1$.
  1393	\end{theorem}
  1394	
  1395	\begin{proof}
  1396	\[
  1397	\|m_{a,b}^c\|_{\mathrm{HS}}^2
  1398	\;\leq\;
  1399	\dim H_a \cdot \dim H_b \cdot \dim H_c
  1400	\cdot K^2(a{+}b{+}c{+}1)^{2N}.
  1401	\]
  1402	By the power-mean inequality $(x+y+z)^p \leq 3^{p-1}(x^p + y^p + z^p)$
  1403	applied with $p = 2N$ and $x = a{+}1$, $y = b{+}1$, $z = c{+}1$:
  1404	\[
  1405	(a{+}b{+}c{+}1)^{2N} \;\leq\; (a{+}1 + b{+}1 + c{+}1)^{2N}


thinking
**Verifying contradictions**

I think there's a mistake that needs verifying. The text at line 1799 refers to "genus-1 trace of the free beta-gamma system (class G)," which is already resolved. However, it mentions that earlier, class C equals beta-gamma. So, there seems to be a contradiction here. I want to clarify specifically to address this inconsistency because it’s essential to stick to the details for accurate understanding!
thinking
**Searching for theorem proof**

I noticed that the key formula `δ_r^{harm}= c_r(A) * m_0^{floor(r/2)-1}` is mentioned without any proof, which is interesting and a bit concerning since the theorem relies on this unproven factorization. It seems crucial to look for any existing proof or support. My plan is to search for “c_r(A)” to see if it’s referenced elsewhere in the repository, as the search results so far only show the theorem and remarks.
exec
/bin/zsh -lc "rg -n \"c_r\\(\\\\cA\\)|m_0\\"'^'"\\{\\\\lfloor r/2 \\\\rfloor - 1\\}|lfloor r/2|delta_r\\"'^'"\\{harm\\}|degree-\\"'$r'"\\"'$ obstruction|degree-r obstruction" chapters metadata' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:c_r\(\cA\)|m_0\^\{\lfloor r/2 \rfloor - 1\}|lfloor r/2|delta_r\^\{harm\}|degree-$r$ obstruction|degree-r obstruction)
            ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n 'c_r\\(\\cA\\)' chapters metadata" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'lfloor r/2' chapters metadata" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'delta_r\\"'^'"\\{harm\\}' chapters metadata" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'degree-\\"'$r'"\\"'$ obstruction|degree-r obstruction'"' chapters metadata" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:c_r\(\cA\))
            ^^
error: unrecognized escape sequence
 exited 1 in 52ms:

 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:24628:g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1.
chapters/theory/higher_genus_modular_koszul.tex:24646:Both give $g_{\min} = \lfloor r/2 \rfloor + 1$.
chapters/theory/higher_genus_modular_koszul.tex:24724:g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1.
chapters/theory/higher_genus_modular_koszul.tex:24727:$\lfloor r/2 \rfloor + 1$, and two new shadow coefficients
chapters/theory/higher_genus_modular_koszul.tex:24904: the integrated planted-forest at genus~$\lfloor r/2 \rfloor + 1$.
chapters/theory/higher_genus_modular_koszul.tex:25768:$g_{\min}(S_r) = \lfloor r/2 \rfloor + 1$
chapters/theory/introduction.tex:129:g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
chapters/connections/bv_brst.tex:1844:$\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, which lies in
chapters/connections/bv_brst.tex:1934: \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
chapters/connections/bv_brst.tex:1952: \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
chapters/connections/bv_brst.tex:1968:$\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
chapters/connections/bv_brst.tex:2006:is $\delta_r = c_r \cdot P_{\mathrm{harm}}^{\lfloor r/2
chapters/connections/concordance.tex:4232:$g_{\min}(S_r) = \lfloor r/2 \rfloor + 1$
chapters/connections/concordance.tex:4240:$g_{\min}(S_r) = \lfloor r/2 \rfloor + 1$
chapters/connections/concordance.tex:10092: $\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, and in
chapters/connections/concordance.tex:11023: $\delta_r \propto m_0^{\lfloor r/2\rfloor - 1}$ is
 succeeded in 51ms:
chapters/connections/bv_brst.tex:1948:element~$x$. Each degree-$r$ obstruction is a multiple of a positive
exec
/bin/zsh -lc "rg -n -F 'c_r(\\cA)' chapters metadata" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex:1934: \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
chapters/connections/bv_brst.tex:1936:where $c_r(\cA)$ is a shadow coefficient
chapters/connections/bv_brst.tex:1952: \;=\; c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
chapters/connections/bv_brst.tex:1968:$\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}$
exec
/bin/zsh -lc "rg -n -F 'D"'^{'"\\mathrm{co}}(\\cA)' chapters metadata" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:3390:  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
chapters/theory/en_koszul_duality.tex:3463:the coderived category $D^{\mathrm{co}}(\cA)$ is stable
chapters/theory/bar_cobar_adjunction_inversion.tex:702:$D^{\mathrm{co}}(\cA)$ is therefore not an exotic generalization
chapters/connections/concordance.tex:10089: bar complex are quasi-isomorphic in $D^{\mathrm{co}}(\cA)$ at
chapters/connections/bv_brst.tex:33:$D^{\mathrm{co}}(\cA)$ for every chirally Koszul algebra. At the
chapters/connections/bv_brst.tex:1839:$D^{\mathrm{co}}(\cA)$ of Positselski, the obstruction is absorbed:
chapters/connections/bv_brst.tex:1909:$D^{\mathrm{co}}(\cA)$:
chapters/connections/bv_brst.tex:1945:in the coderived category $D^{\mathrm{co}}(\cA)$, the relation
chapters/connections/bv_brst.tex:2030:The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '688,710p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   688	\index{coderived category!status}%
   689	The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
   690	bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
   691	the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
   692	$\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
   693	(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
   694	and ordinary derived categories coincide.
   695	
   696	At genus $g \geq 1$, the situation changes: the curvature
   697	$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$ is nonzero for every algebra
   698	with $\kappa(\cA) \neq 0$. This curvature is \emph{not a failure of
   699	Koszulness}: a Koszul algebra has uncurved genus-$0$ bar
   700	($d^2 = 0$ on $\barB^{(0)}$) but curved genus-$g$ bar
   701	($d^2 = [m_0^{(g)}, -]$ on $\barB^{(g)}$). The coderived category
   702	$D^{\mathrm{co}}(\cA)$ is therefore not an exotic generalization
   703	but a necessity: it is the only categorical framework where the
   704	genus-$g$ shadow data of nontrivial modular Koszul algebras can live.
   705	
   706	The proved shadow obstruction tower $\Theta_\cA$ (Theorem~\ref{thm:mc2-bar-intrinsic})
   707	produces genus-$g$ classes via the convolution algebra, but proving that




thinking
**Analyzing theorem inconsistencies**

I could say that the class M "false at chain level" is reported, but it seems like there's no proof provided. Also, I notice an issue where the theorem uses conflicting descriptions for the same obstruction: `κ/Im(τ)` at lines 1834-1836 and `Q^contact·m0` at lines 1840/1956. This inconsistency makes me question the reliability of the theorem and how the information is presented. I should explore this further!
thinking
**Considering mathematical remarks**

I'm exploring a remark that says if the curved complex isn't set to zero, just being in the form of d² doesn't eliminate curvature. It’s interesting to think about how that impacts the overall mathematical theory or concept! This makes me reflect on the nuances in mathematical equations and their curvature properties. The relationships among these might be more complex than they seem at first glance. I'm curious to understand how it all ties together!
thinking
**Assessing class M proof status**

I’m considering whether class M is truly false in Dco. It seems there isn’t a clear proof against it, just assertions in the theorem. The manuscript doesn’t provide evidence of falsity, merely a heuristic non-holomorphic obstruction. So I think the status should be "unproved at best," rather than definitively false. I’ll check if other sources compute `delta_4` in class M, and maybe look into modular holography for more context.
thinking
**Searching for theorems**

I think I should look for relevant theorem labels throughout the repository. I want to ensure I avoid any false positives, so it might be good to search for specific terms like "class C proof" or "Jacobi." That could help me pinpoint the correct information more accurately without getting sidetracked. I’m curious to see what I’ll find and if it leads me to the right theorems!
exec
/bin/zsh -lc "rg -n \"BV\\"'$='"\\"'$bar|BV'"\\s*=\\s*bar|Delta_\\{\\\\mathrm\\{BV\\}\\} = d_\\{\\\\mathrm\\{sew\\}\\}|harmonic decoupling|Jacobi identity|class~\\\\mathsf\\{L\\}|class~\\\\mathsf\\{C\\}|chain-level BV/bar\" chapters/connections/bv_brst.tex chapters/examples chapters/theory chapters/connections | head -n 200" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1818,1985p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:BV$=$bar|BV\s*=\s*bar|Delta_\{\mathrm\{BV\}\} = d_\{\mathrm\{sew\}\}|harmonic decoupling|Jacobi identity|class~\mathsf\{L\}|class~\mathsf\{C\}|chain-level BV/bar)
                                     ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  1818	\toprule
  1819	Class & $r_{\max}$ & BV$=$bar (chain) & BV$=$bar ($D^{\mathrm{co}}$) & Mechanism \\
  1820	\midrule
  1821	\textsf{G} \textup{(}Heisenberg\textup{)}
  1822	 & $2$ & \textbf{proved} & \textbf{proved} & no interaction vertices \\
  1823	\textsf{L} \textup{(}affine KM\textup{)}
  1824	 & $3$ & \textbf{proved} & \textbf{proved} & Jacobi identity \\
  1825	\textsf{C} \textup{(}$\beta\gamma$\textup{)}
  1826	 & $4$ & \textbf{proved} & \textbf{proved} & harmonic decoupling \textup{(}above\textup{)} \\
  1827	\textsf{M} \textup{(}Virasoro, $\cW_N$\textup{)}
  1828	 & $\infty$ & \textbf{false} & \textbf{proved} & $\delta_r \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$ \\
  1829	\bottomrule
  1830	\end{tabular}
  1831	\end{center}
  1832	For class~M, the identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$
  1833	\emph{fails} at the ordinary chain level: the quartic harmonic
  1834	discrepancy $\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}}
  1835	\cdot \kappa / \mathrm{Im}(\tau)$ is \emph{not} a coboundary, because
  1836	$1/\mathrm{Im}(\tau)$ is non-holomorphic and hence not in the image
  1837	of the holomorphic bar differential. The Fay trisecant identity does

thinking
**Inspecting implementation details**

I'm considering inspecting the compute engine to check if class M and the related functionalities are implemented correctly. The skill involves interleaving reasoning with tools, but maybe I won't need that if there's already enough proof against gaps. However, it could be worthwhile to verify if the compute engine supports the theorem or just restates certain assumptions. I should quickly review the relevant parts of the file to ensure that the findings are grounded in the material I've examined.
codex
The proof gap is now clear enough that I’m checking the cited compute layer only to see whether it independently verifies anything substantive, or merely hardcodes the same status table. If it just mirrors the manuscript, it won’t count as evidence for the theorem.
exec
/bin/zsh -lc "nl -ba compute/lib/theorem_bv_sewing_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_bv_sewing_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "theorem_bv_sewing_engine|class M|coderived|delta_4|harmonic|proved|conditional|false|shadow class" compute/lib compute/tests' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Chain-level identification: Delta_BV = d_sew (both increment genus by 1).
     2	
     3	THEOREM (thm:bv-sewing-chain-level):
     4	  For a chirally Koszul algebra A, the BV Laplacian Delta_BV on Obs(Sigma_g, A)
     5	  and the sewing operator d_sew on the bar complex B(A) agree as chain-level
     6	  operators on the modular convolution algebra g^mod_A.  Both operations:
     7	    (a) increment genus by 1: (g,n) -> (g+1, n-2),
     8	    (b) contract a pair of inputs through the Bergman kernel / d log E(z,w),
     9	    (c) are controlled by the non-separating boundary divisor
    10	        delta^ns: M-bar_{g,n+2} -> M-bar_{g+1,n}.
    11	
    12	  The identification holds unconditionally for classes G and L
    13	  (Heisenberg, affine KM), and conditionally for classes C and M
    14	  (beta-gamma, Virasoro, W_N) subject to the harmonic-propagator
    15	  correction vanishing on bar cohomology at the quartic and higher levels.
    16	
    17	PROOF STRATEGY (four independent paths):
    18	
    19	  Path 1 (Operator definition):
    20	    Both Delta_BV and d_sew act on bar-complex elements by contracting
 succeeded in 51ms:
     1	r"""Tests for theorem_bv_sewing_engine: Delta_BV = d_sew chain-level identification.
     2	
     3	FOUR independent proof paths, each verified by multiple tests:
     4	  Path 1 (Operator definition): propagator decomposition, harmonic decoupling
     5	  Path 2 (Spectral sequence): E_1 and E_2 match across genera
     6	  Path 3 (Heisenberg extraction): explicit chain-level quasi-iso, genus-2 extension
     7	  Path 4 (Modular operad): Feynman transform identification, five-component D
     8	
     9	Cross-family verification across all standard families:
    10	  G (Heisenberg), L (affine KM), C (beta-gamma), M (Virasoro)
    11	
    12	Multi-path verification mandate (CLAUDE.md): every numerical claim
    13	verified by at least 3 independent paths.
    14	"""
    15	
    16	import pytest
    17	from sympy import Rational, Symbol, simplify
    18	
    19	from compute.lib.theorem_bv_sewing_engine import (
    20	    AlgebraData,
 succeeded in 51ms:
Total output lines: 9189

compute/tests/test_bc_topological_recursion_shadow_engine.py:334:        """Virasoro: class M, infinite tower, S_r != 0 for large r."""
compute/lib/theorem_hca_pillar_a_engine.py:458:            return "F_1 = d_M (Moore differential, not a shadow class)"
compute/lib/theorem_hca_pillar_a_engine.py:658:        if not self.is_finite_depth():  # infinite depth (class M)
compute/lib/theorem_hca_pillar_a_engine.py:668:        For class M: infinity
compute/lib/theorem_hca_pillar_a_engine.py:711:    For Virasoro (class M):
compute/lib/theorem_hca_pillar_a_engine.py:830:    STATUS: CONJECTURED (not proved in the monograph or in MS24).
compute/lib/theorem_hca_pillar_a_engine.py:962:    """Verify that Virasoro HCA is maximally non-strict (class M).
compute/lib/theorem_hca_pillar_a_engine.py:965:    - Shadow depth = infinity (class M)
compute/lib/theorem_hca_pillar_a_engine.py:983:        "shadow_depth": "infinity (class M)",
compute/lib/theorem_hca_pillar_a_engine.py:989:        "f5_nonzero": True,   # quintic forced (class M)
compute/lib/theorem_hca_pillar_a_engine.py:1118:            "I-adic completion, coderived categories, modular operad. "
compute/tests/test_shadow_period_integral_engine.py:8:  5. Shadow curve periods and branch points (Virasoro, class M)
compute/tests/test_shadow_period_integral_engine.py:493:# Section 10: Shadow curve periods (class M, transcendental)
compute/tests/test_shadow_period_integral_engine.py:513:        """For generic Virasoro (class M), branch points are complex."""
compute/tests/test_shadow_period_integral_engine.py:516:        # For class M, discriminant of Q_L as polynomial in t is negative
compute/tests/test_shadow_period_integral_engine.py:517:        assert disc_val < 0, "Virasoro c=1 should have negative discriminant (class M)"
compute/tests/test_shadow_period_integral_engine.py:523:            # All these are class M: disc < 0
compute/tests/test_shadow_period_integral_engine.py:536:        assert result['disc'] < 0  # class M






thinking
**Evaluating compute engine discrepancies**

I’m noticing that the compute engine mainly codifies statuses and contradictory class C/M statuses. Even though it may not be necessary, the user asked based on the file's contents. This output suggests that compute isn’t independent since the top docstring talks about a conditional for C and M. I need to look further into whether class C is indeed conditional and how it relates to class G/L. The contradictions in tests and claims are definitely worth cross-checking!
thinking
**Analyzing compute layer inconsistencies**

I’m realizing that the compute layer isn't independent and has inconsistencies with the manuscript. The user requested not to modify files, but I can note that the compute layer doesn't support the theorem either. I should consider mentioning how the compute engine restates unsupported assumptions and even contradicts manuscript statuses. I need to check specific lines around the Heisenberg theorem mentioned. It seems the compute engine makes stronger statements than what's actually supported, which is intriguing! Ultimately, I think my main focus should be on findings from the file lines.
thinking
**Planning a focused approach**

I want to make sure not to overwhelm the user. I might note the compute file as a lower priority and need to double-check the exact line numbers in the compute engine, especially around lines 40-45 and 12-15. Citing those could be helpful. I should also search the `claims.jsonl` for any flagged suspicious dependencies; it could serve as additional support, but I shouldn't modify any files. Lastly, checking the theorem registry for `thm:bv-bar-coderived` at line 1895 seems necessary too.
thinking
**Evaluating findings on factorization**

I’m considering splitting my findings into two key areas: one focusing on unproved factorization and the other on the misuse of Dco. Both seem critical to address, but I want to avoid overcounting. I think I need around 5-7 findings in total. For critical findings, I could highlight: 

a) the unproved factorization formula introduced here without any cited proof.
b) the incorrect use of the coderived category that contradicts curvature multiplication, supported by definitions.
thinking
**Evaluating summary structure**

I’ve checked 28 instances and the verdict is FAIL. I need to ensure my summary isn’t too lengthy—maybe 8 bullets plus a status split and a summary will work. Each bullet point should ideally be 1-2 sentences. I probably also should mention specific second-order failures, like the issues with concordance and the en_koszul propagated overclaim. Getting this right is important!
thinking
**Evaluating response structure**

I see a potential issue where a low bullet point count might be suggested if the final output becomes too long. The user specifically requested "Only READ and REPORT," so I’m trying to decide if showing the compute step is necessary. I'll probably stick to 8 bullets for clarity, include a status split, and summarize within 20-30 lines. I might mention checking 28 instances, but I want to keep it concise and avoid being too verbose. Let's prepare that markdown bullet list!
codex
- [CRITICAL] chapters/connections/bv_brst.tex:1932 — The core class-M mechanism, `\delta_r^{\mathrm{harm}} = c_r(\cA)\,m_0^{\lfloor r/2\rfloor-1}`, is introduced without proof or citation. In the files read, this factorization appears only in `thm:bv-bar-coderived`, its follow-up remark, and downstream restatements, so the theorem’s main engine is unproved.

- [CRITICAL] chapters/connections/bv_brst.tex:1945 — The proof treats `m_0\cdot x = d^2(x) \in \operatorname{Im}(d)` as enough to kill the obstruction in `D^{\mathrm{co}}`. But the appendix defines the coderived category as a Verdier quotient by coacyclic objects, not as “boundaries modulo `\operatorname{Im}(d)`” ([chapters/theory/coderived_models.tex:75]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:75), [chapters/theory/coderived_models.tex:545]( /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:545)). Worse, the manuscript itself says curved objects are *not* set to zero in the coderived category ([chapters/theory/bar_cobar_adjunction_inversion.tex:3355]( /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3355)). This is a direct logical failure in the coderived proof.

- [CRITICAL] chapters/connections/bv_brst.tex:1624 — The chapter says the higher-genus chain-level quasi-isomorphism remains open “even for free fields,” i.e. Heisenberg ([1636–1650]), but later upgrades class `G` to chain-level proved ([1821–1822]) and uses chain-level quasi-isomorphisms for `G/L/C` inside `thm:bv-bar-coderived` ([1938–1941]). The status surface is internally contradictory.

- [HIGH] chapters/connections/bv_brst.tex:1925 — For classes `G/L/C`, the theorem cites only `prop:chain-level-three-obstructions`. That proposition classifies obstructions; it does not construct the BV-to-bar chain map or prove a quasi-isomorphism. For `L` and `C`, its proof text only reaches genus `1` ([1741], [1759–1760]), while `thm:bv-bar-coderived` claims all `g\ge1`.

- [HIGH] chapters/connections/bv_brst.tex:1751 — The only support for class `C` is an untagged remark. Its Hodge argument says a quartic correction is a “5-form on a 2-manifold” ([1783–1788]), which uses the wrong domain for a quartic graph/configuration-space integral, and it then calls the “free `\beta\gamma` system” class `G` ([1799–1800]), contradicting the chapter’s own classification of `\beta\gamma` as class `C` ([1825–1826]). This does not support an unconditional proof.

- [HIGH] chapters/connections/bv_brst.tex:1677 — Obstruction (2) is only claimed resolved for theories whose partition function comes from a zeta-regularized determinant ([1682–1684]), but `thm:bv-bar-coderived` upgrades that to “resolved for all classes” ([1927–1929]) without importing any determinant hypothesis. That is scope inflation.

- [HIGH] chapters/connections/bv_brst.tex:1834 — The manuscript does not actually prove that class `M` is chain-level false. The only written reason is the heuristic nonholomorphic factor `\kappa/\mathrm{Im}(\tau)` not lying in the image of the holomorphic bar differential ([1834–1837], [1891–1894]). The same surface then rewrites the obstruction as `Q^{\mathrm{contact}}\cdot m_0` with `m_0=\kappa(\cA)\omega_g` ([1840], [1975–1977]) without proving a bridge between these different objects. So “false” is asserted, not established.

- [MEDIUM] chapters/connections/concordance.tex:7611 — The unsupported claims have propagated: concordance repeats “class `M` chain-level false,” “classes `G/L/C` chain-level proved,” and “every `\delta_r` is coderived-exact” ([7611], [10085–10124]); `en_koszul_duality.tex` reuses the same coderived-exactness mechanism ([3395–3397], [3445–3453]). The overclaim is not local to one theorem.

- [LOW] compute/lib/theorem_bv_sewing_engine.py:12 — The cited compute layer is not independent evidence. It hardcodes theorem-status assumptions, upgrades Heisenberg to a chain-level quasi-isomorphism absent from `thm:heisenberg-bv-bar-all-genera` ([41–45]), and gives a different `C/M` status split from the chapter.

**Status split from the files actually read**
- Analytic proved: `thm:general-hs-sewing` proves convergence under growth conditions; `thm:heisenberg-sewing` gives the explicit Heisenberg sewing/Fredholm model.
- Genus-0 algebraic proved: `thm:brst-bar-genus0`, packaged in `thm:algebraic-string-dictionary`.
- Higher-genus scalar proved: `thm:heisenberg-bv-bar-all-genera` proves only the scalar/free-energy identity, and explicitly says this is weaker than a chain-level quasi-isomorphism.
- Coderived lane: advertised as proved by `thm:bv-bar-coderived`, but the written proof fails.
- Class `M` chain-level false: not proved in the manuscript as read; only asserted heuristically.

## Summary
Instances checked: 28 | Violations found: 9 | Verdict: FAIL
tokens used
190,067
