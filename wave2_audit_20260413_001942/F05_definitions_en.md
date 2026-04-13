# F05_definitions_en (748s)

- [CRITICAL] chapters/theory/en_koszul_duality.tex:5432 — PROBLEM: The chapter summary resurrects the exact false claim the file already retracts: it says `\barB^{\mathrm{ord}}(\cA)` is a dg coalgebra over `\mathsf{SC}^{\mathrm{ch,top}}`, with the differential as the closed color and deconcatenation as the open color. That contradicts the corrected principle at lines 1247-1291 and Theorem `thm:bar-e1-coalgebra` at lines 1293-1353, which say the bar complex is single-colored `\Eone`-chiral and not Swiss-cheese. FIX: Replace lines 5430-5444 by: “`\barB^{\mathrm{ord}}(\cA)=T^c(s^{-1}\bar\cA)` is a single-colored `\Eone`-chiral coassociative dg coalgebra over `(\operatorname{Ass}^{\mathrm{ch}})^!`; the `\mathsf{SC}^{\mathrm{ch,top}}` structure appears only on the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`, not on the bar complex itself.`”

- [CRITICAL] chapters/theory/en_koszul_duality.tex:2142 — PROBLEM: `thm:center-geometric-inevitability` is tagged `\ClaimStatusProvedHere`, but its statement is explicitly conditional on the recognition theorem from Volume II at lines 2151-2154, and it also falsely says the needed `\mathsf{SC}^{\mathrm{ch,top}}` structure comes from `thm:bar-swiss-cheese` at lines 2148-2150 even though that theorem now says the bar complex is not Swiss-cheese. FIX: Downgrade this environment to `\begin{remark}[Conditional geometric realization]` or `\begin{proposition}...\ClaimStatusConditional`, rewrite the input as the pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)` from `thm:operadic-center-hochschild`, and state the Volume II recognition theorem as an explicit hypothesis.

- [CRITICAL] chapters/theory/en_koszul_duality.tex:2985 — PROBLEM: `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))` is used without any defined BRST differential on `Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)`. The only `Q` introduced in the section is attached to bulk observables of a 3d HT theory in Definition 2949-2957, while lines 2271-2299 say the identification of the derived center with that bulk theory is expected, not proved here. As written, the theorem’s object is undefined. FIX: Either restate Theorem `thm:topologization` on `H_Q^\bullet(\Obs_{\mathrm{bulk}}(T_{\mathrm{CS}}))`, or insert a proved proposition before line 2967 giving a quasi-isomorphism `Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)) \simeq \Obs_{\mathrm{bulk}}(T_{\mathrm{CS}})` and define `Q` by transport across that map; if neither is added, downgrade the theorem to conditional.

- [HIGH] chapters/theory/en_koszul_duality.tex:1223 — PROBLEM: Definition `def:SC` is not a full operad definition. It gives slogan-level arity spaces, but no `\Sigma_k\times\Sigma_m` actions, no unit conventions, no explicit pure-open arities, no separate closed/open/mixed insertion maps, and no codimension-1 boundary relations. The user asked whether `\mathsf{SC}^{\mathrm{ch,top}}` is properly defined by generators/relations; in this file it is not. FIX: Expand Definition `def:SC` to specify all arities for `k,m\ge0`, units `\FM_1(\C)=E_1(1)=\mathrm{pt}` and the `k=0` convention, the symmetric-group actions, and the three compositions; then add a proposition immediately after it recording the codimension-1 boundary/generators-and-relations presentation used later.

- [HIGH] chapters/theory/en_koszul_duality.tex:2918 — PROBLEM: “Topologization” is never formally defined before it is used as a theorem and conjecture label. The file never states whether topologization means a chain-level `\Ethree` structure, a cohomological `\Ethree` structure, or collapse of the two-color SC datum to one color. FIX: Insert `\begin{definition}[Cohomological topologization / chain-level topologization]` before Definition `def:inner-conformal-vector`, define both notions explicitly, and then state Theorem `thm:topologization` as the cohomological case and Conjecture `conj:topologization-general` as the chain-level lift.

- [HIGH] chapters/theory/en_koszul_duality.tex:2946 — PROBLEM: Definition `def:inner-conformal-vector` hides essential undefined inputs: “conformal vector,” “BRST-type differential,” “bulk observables,” and the boundary-to-bulk comparison map are not defined in the chapter. The last sentence is also misleading: “For the Virasoro algebra, `T(z)` is the stress tensor itself” gives an example of a conformal vector, not of an inner conformal vector, and later lines 3085-3093 say Virasoro innerness is conjectural. FIX: Split this into two definitions: first define a conformal vector in the boundary chiral algebra; then define innerness relative to a specified bulk complex `(\Obs_{\mathrm{bulk}}(T),Q)` and boundary map `\iota:\cA\to\Obs_{\mathrm{bulk}}(T)`. Replace the Virasoro sentence by: “For Virasoro, `T(z)` is the boundary conformal vector; whether it is inner is conjectural and depends on the 3d gravity BRST complex.”

- [HIGH] chapters/theory/en_koszul_duality.tex:2990 — PROBLEM: The proof jumps from `\partial_z=[Q,[G,-]]` to “the factorization algebra on `\C` becomes locally constant” and then invokes Lurie. No argument is given that both real translation generators become `Q`-exact, and no local-constancy criterion is cited or proved. This is the load-bearing step. FIX: Insert a lemma between lines 3009 and 3016 proving that `\partial_x` and `\partial_y` are `Q`-exact on BRST cohomology (using the holomorphic/Dolbeault direction plus Sugawara), then cite the precise recognition theorem for locally constant factorization algebras before concluding `\Etwo^{\mathrm{top}}`.

- [HIGH] chapters/theory/en_koszul_duality.tex:3204 — PROBLEM: Construction `constr:sugawara-antighost` claims to “verify” `[Q,G]=T_{\mathrm{Sug}}`, but the two correction terms are waved away as “Q-exact up to equations of motion” at lines 3308-3312 and 3318-3323 with no explicit homotopy and no cited BV lemma. That is not a verification. FIX: Either add the missing BV computation by exhibiting an operator `H(z)` with `[Q,H(z)]` equal to the correction terms modulo the BV differential/EOM ideal, or demote the construction to a heuristic remark and cite a precise external proof.

- [HIGH] chapters/theory/en_koszul_duality.tex:1417 — PROBLEM: Construction `constr:promotion-functor` overclaims. It says every chiral algebra canonically promotes to an `\mathsf{SC}^{\mathrm{ch,top}}`-algebra via self-action because every commutative algebra acts on itself as a module, but Remark `rem:center-scope-e-inf` at lines 2055-2069 later says the center theorem only works for logarithmic `E_\infty`-chiral input and fails for genuine `E_1`-chiral input. FIX: Rewrite the construction to start with “For logarithmic `E_\infty`-chiral input…” and add the sentence “For genuine `E_1`-chiral input there is no canonical promotion; the correct replacement is the ordered Hochschild complex.”

- [HIGH] chapters/theory/en_koszul_duality.tex:1796 — PROBLEM: Theorem `thm:operadic-center-hochschild` omits its real hypotheses. The statement says only “logarithmic chiral algebra,” but line 2055 later says it requires `E_\infty`-chiral input; the statement also treats the closed sector as the space-valued operad `\{\FM_k(\C)\}`, while the proof uses the dg model `\Omega^*(\FM_k(\C),\log D)` at lines 1883-1890. FIX: Change the theorem statement to: “Let `\cA` be a logarithmic `E_\infty`-chiral algebra equipped with an action of the dg operad `\Omega^\bullet(\FM_\bullet(\C),\log D)`, and let `A` be the open-color algebra in its promoted `\mathsf{SC}^{\mathrm{ch,top}}`-pair.” Then keep the identification only under those hypotheses.

- [MEDIUM] chapters/theory/en_koszul_duality.tex:1196 — PROBLEM: The chapter never actually lists the five presentations of `\mathsf{SC}^{\mathrm{ch,top}}`. In the Swiss-cheese lane I read one space-level definition, one abstract vanishing-operad reformulation, one Koszul-dual description, one Boardman–Vogt mention, and one imported local-pair model, but no explicit “five presentations” proposition or roadmap. FIX: Add a proposition immediately after Definition `def:SC` enumerating the five presentations with labels and cross-references: configuration-space operad, abstract two-colored operad with vanishing open-to-closed operations, local chiral Swiss-cheese pair, Koszul-dual three-sector cooperad, and Boardman–Vogt/HT prefactorization presentation.

- [MEDIUM] chapters/theory/en_koszul_duality.tex:2588 — PROBLEM: The “four assertions” summary silently changes scope. Item (1) is for every `E_1`-algebra `A`, while item (2) uses the chiral identification theorem that only applies to logarithmic `E_\infty`-chiral lifts `\cA`. As written, the paragraph reads as if one theorem handles both settings uniformly. FIX: Rewrite items (1)-(2) to separate the scopes: “For every `E_1` open algebra `A`, `Z_{\mathsf{SC}}(A)` exists. If `A` arises from a logarithmic `E_\infty`-chiral algebra `\cA`, then `Z_{\mathsf{SC}}(A)\simeq C^\bullet_{\mathrm{ch}}(\cA,\cA)`.”

- [MEDIUM] chapters/theory/en_koszul_duality.tex:5203 — PROBLEM: The subsection still uses the forbidden terminology “chiral `\Ethree`-algebra,” even though Theorem `thm:topologization` only proves a cohomological `\Ethree^{\mathrm{top}}` structure on BRST cohomology. This reintroduces the `SC^{\mathrm{ch,top}}\neq E_3` conflation the constitution explicitly warns against. FIX: Rename the subsection and its local terminology to “cohomological `\Ethree^{\mathrm{top}}` enhancement,” and replace each occurrence of “chiral `\Ethree`-algebra” in this subsection by either “holomorphic `\Etwo^{\mathrm{hol}}\otimes\Eone^{\mathrm{top}}` structure” before enhancement or “cohomological `\Ethree^{\mathrm{top}}` structure” after enhancement.

## Summary
Checked: 8 | Findings: 12 | Verdict: FAIL


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
session id: 019d83e2-7e17-7c01-9bf0-3af8a43ea844
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


MISSION: FOUNDATION AUDIT of chapters/theory/en_koszul_duality.tex

Check: is SC^{ch,top} properly defined (generators, relations)? Is topologization defined? Is 'inner conformal vector' defined? Are the five presentations of SC listed?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers


thinking
**Considering audit methods**

I might need to use the explorer sub-agent for codebase questions, as the instructions say to prefer it over manual searches or file readings. This is related to a codebase audit, so I think using the explorer can help me gather relevant sections. However, I realize that for mathematical accuracy, I might also need to read files manually. The explorer can help locate definitions, but I need to ensure I access the actual file contents properly. I might also consider using build-surface for a comprehensive audit of certain concepts.
thinking
**Inspecting references and tools**

I'm considering inspecting raw references. I could run rg for labels, which sounds promising! Compiling a targeted approach might not even be necessary, but since the user wants maximal accuracy, I’ll need to find unresolved references through grep, regex, or by compiling the LaTeX. I’ll need to do some focused checks. It's important to read the required files before making any substantial mathematical edits, as safety is a priority. I'll provide updates and plan my next steps accordingly, maybe using multi_tool for reading commands.
codex
Auditing `chapters/theory/en_koszul_duality.tex` as a hostile proof reader. I’m first loading the constitutional surfaces and the audit skill, then I’ll read the target file and its directly referenced definitions before I start issuing findings.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && printf '\\n--- AGENTS ok ---\\n' && sed -n '1,260p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
/Users/raeez/chiral-bar-cobar

--- AGENTS ok ---
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
 succeeded in 266ms:
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
 succeeded in 374ms:
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
**Planning an audit**

I need to conduct an audit on a target file, probably using commentary updates and a solid plan. I should read through this file completely and search for relevant terms using line numbers for reference. It’s important to identify specific concepts like the SC^{ch,top} definition and its related topics. The user is looking for hidden imports and unresolved references, so I must check whether these concepts are defined in the target file or depend on unstated results. Let’s start by inspecting the file structure and relevant hits.
codex
The audit surface is now fixed: `chapters/theory/en_koszul_duality.tex`, specifically the SC/the-topologization lane. I’m mapping every occurrence of `SC^{ch,top}`, `topolog`, `conformal`, `Swiss`, and the claimed “five presentations” so I can distinguish what is actually defined from what is only advertised.
exec
/bin/zsh -lc "rg -n \"SC\\"'^'"\\{ch,top\\}|SC\\\\"'^'"\\{ch,top\\}|Swiss|swiss|topolog|conformal|five presentations|five presentation|presentation\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"topologization|inner conformal vector|SC\\"'^'"\\{ch,top\\}|Swiss-cheese|Swiss cheese|five notions of E_1-chiral algebra|five presentations\" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md chapters/theory/*.tex chapters/examples/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 192ms:
23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
26:conformal vector.
27:The topologization proof is made constructive by an explicit
59:topological ladder is instead
81: presentation
82: \textup{(}Theorem~\ref{thm:totaro-presentation}\textup{)}.
83: At $n = 2$, this specializes to the Arnold presentation on
91: \emph{not} the topological $\En$ bar-cobar at $n = 1$
94: $n = 2$ with the commutativity constraint dropped. The topological
131:$\Eone$-algebra in the topological sense (which would be an
163:In this chapter, bare $\En$ always denotes little-disks/topological
167:topological ladder at $n = 2$, while the $n = 1$ case is the
190:generators-and-relations presentation due to Arnold ($n = 2$, i.e., $\bR^n = \bC$) and
194:\begin{theorem}[Arnold presentation {\cite{Arnold69}}; \texorpdfstring{$\bC \cong \bR^2$}{C = R2};
196:\label{thm:arnold-presentation}
197:\index{Arnold relations!presentation}
211:\begin{theorem}[Totaro presentation, general \texorpdfstring{$n$}{n} {\cite{Totaro96, Coh76}};
213:\label{thm:totaro-presentation}
312:with the structure of a topological operad, the
 succeeded in 477ms:
chapters/theory/algebraic_foundations.tex:2132:Swiss-cheese structure of Volume~II combines both.
chapters/theory/algebraic_foundations.tex:2358:\item \emph{Swiss-cheese factorisation algebra on
chapters/theory/algebraic_foundations.tex:2380:and~\textup{(ii)} via the Swiss-cheese mechanism;
chapters/theory/configuration_spaces.tex:2082:\emph{Voronov Swiss-cheese} space
chapters/theory/configuration_spaces.tex:2241:has three types, matching the Swiss-cheese operad structure
chapters/theory/configuration_spaces.tex:2698:Type~III faces (mixed bubbling): the Swiss-cheese fiber
chapters/theory/introduction.tex:88:Swiss-cheese formality ($m_k^{\mathrm{SC}} = 0$ for
chapters/theory/introduction.tex:1475:\textsc{Operadic primacy of Swiss-cheese.} The Swiss-cheese
chapters/theory/introduction.tex:1482:Swiss-cheese algebra is recovered from the open sector by passing
chapters/theory/introduction.tex:1590: \xrightarrow[\text{topologization}]{\;\;(4)\;\;}
chapters/theory/introduction.tex:1597:tensor structure. Arrow~(4) is the topologization
chapters/theory/introduction.tex:1598:(Theorem~\ref{thm:topologization} for affine Kac--Moody;
chapters/theory/introduction.tex:1599:Conjecture~\ref{conj:topologization-general} in general):
chapters/theory/introduction.tex:1606:\S\ref{sec:topologization}).
chapters/theory/introduction.tex:1728:\label{rem:topologization-intro}
chapters/theory/introduction.tex:1729:\index{topologization theorem!introduction}%
chapters/theory/introduction.tex:1739:Theorem~\ref{thm:topologization}
chapters/theory/introduction.tex:1740:(\S\ref{sec:topologization}) establishes this for affine
chapters/theory/introduction.tex:1742:Sugawara element provides the inner conformal vector
chapters/theory/introduction.tex:1749:(Conjecture~\ref{conj:topologization-general}). At critical
 succeeded in 801ms:
     1	\chapter{\texorpdfstring{$\En$ Koszul duality and higher-dimensional bar complexes}{En Koszul duality and higher-dimensional bar complexes}}
     2	\label{ch:en-koszul-duality}
     3	
     4	\index{En algebra@$\En$ algebra!Koszul duality|textbf}
     5	\index{bar complex!higher-dimensional|textbf}
     6	
     7	For $\En$ algebras, the bar-cobar adjunction replaces the logarithmic
     8	propagator $d\log(z-w)$ with a closed $(n{-}1)$-form, the Arnold
     9	relations with the Totaro relations, and chiral Koszul duality with
    10	$\En$ Koszul duality. The underlying construction is the same:
    11	duality is mediated by a convolution algebra on a compactified
    12	configuration space. The passage from $n = 1$
    13	(associative/$A_\infty$) through $n = 2$ (the holomorphic refinement
    14	recovering the chiral bar complex) to $n = 3$ (Chern--Simons,
    15	Vassiliev invariants) and beyond exhibits bar-cobar duality as a
    16	single construction parametrised by manifold dimension, with the
    17	formality phenomena of Kontsevich and Tamarkin as shadows of the
    18	Koszul property in each dimension.
    19	
    20	The chapter culminates in the chiral center theorem


thinking
**Investigating target file definitions**

I think I need to review sections related to Swiss-cheese and topologization in the target file, and also check the chiral center theorem for definitions. The user is looking for an audit of the foundations, so I should likely examine the cited dependencies in the relevant areas. Concepts probably rely on the chiral center theorem, so I'm inspecting specific lines in the en_koszul_duality.tex file and searching for mentions of "five presentations" to clarify their relevance. Let's see what I find!
thinking
**Reviewing specific sections**

I plan to read specific chunks from the target file, focusing on lines 1196-1605, 2918-3210, 5200-5265, 5400-5460, and 5710-5830. I'll also check the theorem registry entry for thm:bar-swiss-cheese, since it's crucial to understand its label status. It sounds like a good idea to ensure I have all the details, and I might need to use natural language to summarize my findings. Let’s get to it!
codex
I’ve located the live fault lines. Next I’m reading the actual Swiss-cheese and topologization sections in context, then I’ll chase every imported label they depend on to separate real definitions from deferred promises.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1190,1615p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5716,5835p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5200,5270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2918,3215p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5408,5460p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1190	%================================================================
  1191	
  1192	%================================================================
  1193	% SECTION: THE SWISS-CHEESE CASE (2,1)
  1194	%================================================================
  1195	
  1196	\section{The Swiss-cheese case: holomorphic--topological
  1197	factorization}
  1198	\label{sec:swiss-cheese}
  1199	\index{Swiss-cheese operad|textbf}
  1200	\index{bar complex!$\Eone$-chiral coassociative coalgebra|textbf}
  1201	\index{holomorphic--topological!factorization|textbf}
  1202	
  1203	The dimensional ladder has so far been one-dimensional: $n = 1$
  1204	(associative), $n = 2$ (chiral), $n = 3$ (Chern--Simons). But the
  1205	ordered bar complex $\barB^{\mathrm{ord}}(\cA)$ of this monograph
  1206	already carries a \emph{mixed}
  1207	structure that does not fit on this line. The differential
  1208	$d_{\barB}$ lives on $\FM_k(\bC)$ (the $n = 2$ slot); the
  1209	coassociative coproduct~$\Delta$ lives on $\Conf_k(\bR)$ (the
 succeeded in 53ms:
  5716	carries $\mathsf{E}_3$ structure by the Higher Deligne Conjecture,
  5717	a distinct object from $\barB^{\Sigma}(\cA)$ itself.
  5718	For genuinely $\Eone$-chiral algebras, $\barB^{\Sigma}$ does not
  5719	exist without an $R$-matrix, and the $\mathsf{E}_3$ claim requires
  5720	a 3d holomorphic-topological theory as independent input.
  5721	
  5722	\begin{proposition}[$\Etwo$ structure on the bar complex and the $\mathsf{E}_3$ obstruction;
  5723	\ClaimStatusProvedHere]
  5724	\label{prop:e3-bar-structure}
  5725	\index{bar complex!E3 obstruction@$\mathsf{E}_3$ obstruction|textbf}
  5726	\index{Gerstenhaber bracket!on bar complex}
  5727	\index{Higher Deligne Conjecture!E3 structure on derived center@$\mathsf{E}_3$ structure on derived center}
  5728	Let $\cA$ be a chiral algebra on a smooth algebraic curve~$X$.
  5729	\begin{enumerate}[label=\textup{(\roman*)}]
  5730	\item \textup{($\Etwo$ on $\barB^{\Sigma}(\cA)$.)}
  5731	 The symmetric bar $\barB^{\Sigma}(\cA)$ carries a natural
  5732	 $\Etwo$-coalgebra
  5733	 structure from the operad $\mathsf{FM}_2 \simeq \Etwo$ acting on
  5734	 $\Conf_k(\bC) \cong \Conf_k(\bR^2)$. The corresponding cohomological
  5735	 structure on $H^*(\barB^{\Sigma}(\cA))$ is a \emph{Gerstenhaber algebra}: an
 succeeded in 52ms:
  5200	\subsection{The Khan--Zeng topological enhancement}
  5201	\label{subsec:khan-zeng-enhancement}
  5202	
  5203	The chiral $\Ethree$-algebra is holomorphic: it depends on the
  5204	complex structure of $X$ through the KZ connection. At
  5205	non-critical level $k \neq -h^\vee$, the Sugawara Virasoro
  5206	element provides a homotopy between the holomorphic and
  5207	topological directions, upgrading the $\Ethree$ structure
  5208	from holomorphic to topological. At the critical level,
  5209	the Sugawara element is undefined and the enhancement fails.
  5210	
  5211	\begin{proposition}[Topological enhancement via Sugawara]
  5212	\label{prop:khan-zeng-topological}
  5213	\ClaimStatusProvedHere
  5214	At generic non-critical level $k \neq -h^\vee$, the affine
  5215	Kac--Moody vertex algebra $V_k(\fg)$ possesses a Sugawara
  5216	Virasoro element
  5217	\begin{equation}\label{eq:sugawara-element}
  5218	  T_{\mathrm{Sug}} \;=\;
  5219	  \frac{1}{2(k + h^\vee)}
 succeeded in 51ms:
  2918	\label{sec:topologization}
  2919	\index{topologization theorem|textbf}
  2920	\index{Sugawara construction!topologization}
  2921	\index{E3 algebra@$\Ethree$-algebra!from Swiss-cheese + conformal vector}
  2922	
  2923	The chiral center theorem
  2924	(Theorem~\ref{thm:operadic-center-hochschild}) establishes
  2925	that the operadic center of an
  2926	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra is an $\Etwo$-algebra,
  2927	with the $\Etwo$ structure coming from the closed sector
  2928	$\FM_k(\bC)$. The dimensional ladder of
  2929	\S\ref{sec:n3-chern-simons} identifies $\Ethree$ with
  2930	perturbative Chern--Simons on~$\bR^3$. The gap: how does the
  2931	$\Etwo$ center of an $\mathsf{SC}^{\mathrm{ch,top}}$-algebra
  2932	upgrade to~$\Ethree$?
  2933	
  2934	The answer requires extra structure. The
  2935	$\Etwo$ center carries $\Etwo$ operations from
  2936	$\FM_k(\bC)$: these are \emph{holomorphic}, not topological.
  2937	A topological $\Etwo$-algebra has operations from
 succeeded in 51ms:
  5408	\label{sec:examples}
  5409	%================================================================
  5410	
  5411	\section{The dimensional ladder}
  5412	\label{sec:en-summary}
  5413	
  5414	The chapter establishes eight results. The Totaro presentation
  5415	of $H^*(\Conf_k(\bR^n))$ generalizes Arnold's presentation from
  5416	$n = 2$ to all~$n$ (Theorem~\ref{thm:totaro-presentation}).
  5417	The $\Etwo$ bar complex satisfies $d^2 = 0$ via the Totaro
  5418	relations (Theorem~\ref{thm:e2-d-squared}).
  5419	The chiral bar-cobar duality of Main Theorem~A is recovered
  5420	as the $n = 2$ case of $\En$ Koszul duality
  5421	(Corollary~\ref{cor:n2-recovery}), and our construction is the
  5422	chain-level refinement of Ayala--Francis Poincar\'e--Koszul duality
  5423	at $n = 2$ (Proposition~\ref{prop:refines-af}).
  5424	The abstract $\En$ Koszul duality, $\En$ formality, and higher
  5425	enveloping algebras are established in the literature for all~$n$
  5426	(Theorem~\ref{thm:en-koszul-duality},
  5427	Theorem~\ref{thm:knudsen-higher-enveloping},

thinking
**Inspecting theorem proof**

I think I need to read the continuation after 3215 to fully understand the explicit construction of G. The proof depends on this, and it seems like the user is curious about specific issues that might involve some hidden imports. I should also check if the proof constructs G or mentions any external results. Maybe exploring from 3198 to 3335 will provide enough context for the topologization and any references like KhanZeng.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3398,3470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1100,1235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1235,1375p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "operadic-center-hochschild|brace-dg-algebra|gerstenhaber-sl2-bracket|constr:sugawara-antighost|khan-zeng-topological|topologization-general|bar-swiss-cheese|princ:sc-two-incarnations" chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3210,3398p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3398	 Conjecture~\textup{\ref{conj:topologization-general}}.
  3399	\end{enumerate}
  3400	\end{remark}
  3401	
  3402	\begin{conjecture}[Coderived $\Ethree$ for class~M; \ClaimStatusConjectured]
  3403	\label{conj:coderived-e3}%
  3404	\index{coderived category!E3 structure@$\Ethree$ structure|textbf}%
  3405	\index{topologization theorem!coderived refinement}%
  3406	\index{E3 algebra@$\Ethree$ algebra!coderived}%
  3407	Let $\cA$ be a chirally Koszul algebra with inner conformal vector
  3408	at non-critical level.
  3409	\begin{enumerate}[label=\textup{(\roman*)}]
  3410	\item \textup{(Coderived local constancy.)}
  3411	  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  3412	  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
  3413	  is locally constant. Precisely: the
  3414	  $m_0$-curvature obstruction to local constancy at
  3415	  step~\textup{(iv)} of
  3416	  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
  3417	  lies in $\operatorname{Im}(d)$ in $D^{\mathrm{co}}$, by the
 succeeded in 52ms:
  1100	one cannot choose $r > p$ distinct insertion positions.
  1101	\end{proof}
  1102	
  1103	%% ===========================================================
  1104	%% 5. LOCAL CHIRAL SWISS-CHEESE PAIR
  1105	%% ===========================================================
  1106	
  1107	\subsection{Local chiral Swiss-cheese pairs}
  1108	\label{subsec:local-swiss-cheese}
  1109	
  1110	\begin{definition}[Local chiral Swiss-cheese pair]
  1111	\label{def:local-swiss-cheese-pair}
  1112	\index{Swiss-cheese pair!local chiral}
  1113	A \emph{local chiral Swiss-cheese pair} over an
  1114	$\Ainf$-chiral algebra $(A, \{m_k\})$ is a triple
  1115	$(B, A, \{\mu_{p;q}\})$ where:
  1116	\begin{enumerate}[label=\textup{(\roman*)}]
  1117	\item $B = (B, \delta_B, \{-\}\{-, \ldots, -\})$
  1118	 is a brace dg algebra (satisfying (B1)--(B4)
  1119	 of Theorem~\ref{thm:brace-dg-algebra}).
 succeeded in 51ms:
  1235	\begin{enumerate}[label=\textup{(\roman*)}]
  1236	\item \emph{Brace algebra:}
  1237	 $B := C^\bullet_{\mathrm{ch}}(A, A)$ with the
  1238	 brace structure of
  1239	 Theorem~\ref{thm:brace-dg-algebra} and
  1240	 differential $\delta = [m, -]$.
  1241	
  1242	\item \emph{$\Ainf$-chiral algebra:} $A$ with its
  1243	 given structure $\{m_k\}$.
  1244	
  1245	\item \emph{Mixed operations:}
  1246	 For $f_1, \ldots, f_p \in C^\bullet_{\mathrm{ch}}(A, A)$
  1247	 of degrees $k_1, \ldots, k_p$ and
  1248	 $a_1, \ldots, a_q \in A$, the universal mixed
  1249	 operation is the \emph{iterated evaluation}:
  1250	 \begin{equation}\label{eq:universal-mixed}
  1251	 \boxed{
  1252	 \begin{aligned}
  1253	 &\mu^{\mathrm{univ}}_{p;q}
  1254	 (f_1, \ldots, f_p;\, a_1, \ldots, a_q;\,
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:37:Theorem~\ref{thm:brace-dg-algebra}).
chapters/theory/chiral_center_theorem.tex:558:\label{subsec:brace-dg-algebra}
chapters/theory/chiral_center_theorem.tex:592:Theorem~\textup{\ref{thm:brace-dg-algebra}} below:
chapters/theory/chiral_center_theorem.tex:610:\label{thm:brace-dg-algebra}
chapters/theory/chiral_center_theorem.tex:1119: of Theorem~\ref{thm:brace-dg-algebra}).
chapters/theory/chiral_center_theorem.tex:1239: Theorem~\ref{thm:brace-dg-algebra} and
chapters/theory/chiral_center_theorem.tex:2095:\label{prop:gerstenhaber-sl2-bracket}
chapters/theory/chiral_center_theorem.tex:2201:Proposition~\ref{prop:gerstenhaber-sl2-bracket} is the first
chapters/theory/en_koszul_duality.tex:31:(Construction~\ref{constr:sugawara-antighost}). For class~M
chapters/theory/en_koszul_duality.tex:1249:\label{princ:sc-two-incarnations}
chapters/theory/en_koszul_duality.tex:1272:  Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
chapters/theory/en_koszul_duality.tex:1295:\label{thm:bar-swiss-cheese}% label retained for backward compatibility
chapters/theory/en_koszul_duality.tex:1331:\textup{(}Principle~\textup{\ref{princ:sc-two-incarnations}}\textup{)}.
chapters/theory/en_koszul_duality.tex:1336:\textup{(}Theorem~\textup{\ref{thm:operadic-center-hochschild}}\textup{)}.
chapters/theory/en_koszul_duality.tex:1437:Theorem~\textup{\ref{thm:bar-swiss-cheese}} is the statement that
chapters/theory/en_koszul_duality.tex:1794:\label{thm:operadic-center-hochschild}
chapters/theory/en_koszul_duality.tex:2055:Theorem~\ref{thm:operadic-center-hochschild} requires the chiral
chapters/theory/en_koszul_duality.tex:2150:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
chapters/theory/en_koszul_duality.tex:2176:(Theorem~\ref{thm:bar-swiss-cheese}) with the recognition theorem.
chapters/theory/en_koszul_duality.tex:2254:Theorems~\ref{thm:operadic-center-hochschild}
 succeeded in 52ms:
  3210	Let $\fg$ be a finite-dimensional simple Lie algebra with basis
  3211	$\{t_a\}_{a=1}^{\dim\fg}$, structure constants
  3212	$f^a{}_{bc}$ ($[t_b, t_c] = f^a{}_{bc}\,t_a$), Killing form
  3213	$\kappa_{ab} = \operatorname{tr}(t_a t_b)$, and dual Coxeter number
  3214	$h^\vee$. Fix a non-critical level $k \ne -h^\vee$.
  3215	
  3216	\textsc{BV field space.}
  3217	The $3$d holomorphic Chern--Simons theory on
  3218	$\bR_t \times \bC_z$ with gauge algebra~$\fg$ at level~$k$
  3219	has BV field space
  3220	\begin{equation}\label{eq:bv-field-space-hol-cs}
  3221	\cE \;=\; \Omega^\bullet(\bR_t)
  3222	 \;\widehat{\otimes}\;
  3223	 \Omega^{0,\bullet}(\bC_z) \;\otimes\; \fg[1],
  3224	\end{equation}
  3225	with differential $Q_0 = d_t + \dbar$ and cubic interaction from
  3226	the Chern--Simons vertex. In the HT gauge, the physical components
  3227	are\textup:
  3228	\begin{center}
  3229	\renewcommand{\arraystretch}{1.15}

thinking
**Searching for presentations of SC**

The user is looking for a proper definition of SC with generators and relations. I see that the definition provides spaces, but it doesn't specify those generators or relations, which is a key part. So, I think I should search for "five presentations of SC" to see if there's any information available. It seems like a logical step to clarify the user’s question. I'll also keep in mind to use rg for a focused search.
codex
I’ve confirmed the file has a concrete Swiss-cheese section and a topologization section. I’m now checking whether the claimed structures are actually defined at the level the chapter pretends: operad data, relations, recognition inputs, and the advertised variants/presentations.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1768,1848p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"five.*Swiss|five.*SC|five.*presentation|presentations of SC|presentations? of the Swiss|presentations? of \\\\mathsf\\{SC|seven faces|faces of SC|incarnation|presentation\" chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/introduction.tex chapters/theory/*.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
  1768	
  1769	\begin{proof}
  1770	This is a standard construction in the theory of colored operads.
  1771	The product
  1772	$\prod_m \operatorname{Hom}_{\Sigma_m}(\cO(\mathsf{c},
  1773	\mathsf{o}^m; \mathsf{o}), \operatorname{Hom}(A_\mathsf{o}^{\otimes m}, A_\mathsf{o}))$
  1774	assembles all possible action maps with one closed input.
  1775	Equivariance with respect to $\cO^{\mathsf{c}}$-composition
  1776	(inserting further closed inputs) and $\cO^{\mathsf{o}}$-composition
  1777	(inserting open inputs into the open arguments) is imposed by the
  1778	two arrows. The equalizer exists because chain complexes are complete.
  1779	In the derived setting, one replaces $\cO$ by a cofibrant resolution
  1780	$\cO_\infty \xrightarrow{\sim} \cO$ and takes the homotopy equalizer
  1781	in the model-categorical sense; the resulting object is well-defined
  1782	up to quasi-isomorphism.
  1783	\end{proof}
  1784	
  1785	
  1786	\subsection{Step 2: Chain-level realization for
  1787	\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC-ch,top}}
 exited 2 in 50ms:
rg: regex parse error:
    (?:five.*Swiss|five.*SC|five.*presentation|presentations of SC|presentations? of the Swiss|presentations? of \mathsf\{SC|seven faces|faces of SC|incarnation|presentation)
                                                                                                                 ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"KhanZeng25|Lurie~\\\\cite\\{HA\\}|Dunn88|inner conformal vector|locally constant factorization algebras|Q-exact\" chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/theory/chiral_center_theorem.tex chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1848,1925p'" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:KhanZeng25|Lurie~\cite\{HA\}|Dunn88|inner conformal vector|locally constant factorization algebras|Q-exact)
                        ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  1848	Z_{\mathsf{SC}}(A)
  1849	\;\hookrightarrow\;
  1850	\prod_{m \geq 0}
  1851	\operatorname{Hom}_{\Sigma_m}
  1852	\!\bigl(
  1853	\mathsf{SC}((\mathsf{c}, \mathsf{o}^m);\, \mathsf{o}),\,
  1854	\operatorname{Hom}(A^{\otimes m}, A)
  1855	\bigr)
  1856	\;\rightrightarrows\;
  1857	(\cdots),
  1858	\]
  1859	where the two arrows impose closed-sector equivariance (composing
  1860	further closed inputs) and open-sector bimodule equivariance
  1861	(composing open inputs via~$E_1$). Substituting
  1862	$\mathsf{SC}((\mathsf{c}, \mathsf{o}^m); \mathsf{o})
  1863	= \FM_1(\bC) \times E_1(m) \cong \mathrm{pt} \times E_1(m)$
  1864	at $k = 1$, the product over~$m$ assembles into
  1865	$\prod_m \operatorname{Hom}_{\Sigma_m}(E_1(m),
  1866	\operatorname{Hom}(A^{\otimes m}, A))
  1867	\cong \operatorname{End}^{E_1}_{A}$,

thinking
**Rethinking the search process**

I need to consider rerunning a simpler regex. I want to search for five presentations that contain fixed strings. I think simplifying the search will help me focus on getting better results. It's important to clarify what I mean by "fixed strings" so I can effectively narrow down the presentations I’m after. I want to make sure I get this right and end up with relevant information that really meets the user’s needs!
exec
/bin/zsh -lc 'rg -n -F "KhanZeng25" chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/examples/kac_moody.tex chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "inner conformal vector" chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/connections/concordance.tex CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "five presentations" chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/introduction.tex chapters/theory chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"presentation\" chapters/theory/en_koszul_duality.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:2285:is given by Khan--Zeng~\cite{KhanZeng25}, who
chapters/theory/en_koszul_duality.tex:2289:$\lambda$-Jacobi identity is satisfied~\cite[\S\,2.2]{KhanZeng25}.
chapters/theory/en_koszul_duality.tex:2290:They show~\cite[\S\,4.3]{KhanZeng25} that
chapters/theory/en_koszul_duality.tex:2967:\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
chapters/theory/en_koszul_duality.tex:5226:By Khan--Zeng~\cite{KhanZeng25}, the Virasoro element
chapters/theory/en_koszul_duality.tex:5281:Khan--Zeng~\cite{KhanZeng25} prove the following at the
chapters/theory/en_koszul_duality.tex:5314:argument~\cite{KhanZeng25} then applies verbatim: BRST-exactness
 exited 1 in 51ms:

 succeeded in 53ms:
chapters/connections/concordance.tex:7180: $\SCchtop + \text{inner conformal vector} = E_3$)
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:838:AP158: SC^{ch,top} != E_3. The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, T(z) = {Q,G(z)}) = E_3-TOPOLOGICAL (NOT E_3-chiral). The conformal vector KILLS the chiral direction at the cohomological level: C-translations become Q-exact, the complex structure on C becomes irrelevant in cohomology, the two SC colors collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct). At critical level k=-h^v: Sugawara undefined, topologization fails. NEVER write "E_3-chiral" for the topologized bulk; it is E_3-topological. Vol II MUST construct the E_3-topological structure on Z^{der}_{ch}(A) explicitly at chain level — define it, prove it, verify on examples, and characterize the obstruction when conformal vector is absent.
chapters/theory/introduction.tex:1742:Sugawara element provides the inner conformal vector
chapters/theory/en_koszul_duality.tex:1273:\item With an inner conformal vector at non-critical level,
chapters/theory/en_koszul_duality.tex:2953:is~$\cA$. An \emph{inner conformal vector} for
chapters/theory/en_koszul_duality.tex:2963:provides the inner conformal vector. For the
chapters/theory/en_koszul_duality.tex:2976:provides an inner conformal vector
chapters/theory/en_koszul_duality.tex:2990:Here the inner conformal vector makes holomorphic
chapters/theory/en_koszul_duality.tex:3004:The inner conformal vector identifies
chapters/theory/en_koszul_duality.tex:3076:an explicit inner conformal vector and the $3$d
chapters/theory/en_koszul_duality.tex:3122:inner conformal vector in BRST cohomology, and (ii)~the
chapters/theory/en_koszul_duality.tex:3206:existence of $G(z)$ witnessing the inner conformal vector in BRST
chapters/theory/en_koszul_duality.tex:3407:Let $\cA$ be a chirally Koszul algebra with inner conformal vector
chapters/theory/en_koszul_duality.tex:3456:\item Topologization via inner conformal vector is proved on
 succeeded in 52ms:
81: presentation
82: \textup{(}Theorem~\ref{thm:totaro-presentation}\textup{)}.
83: At $n = 2$, this specializes to the Arnold presentation on
190:generators-and-relations presentation due to Arnold ($n = 2$, i.e., $\bR^n = \bC$) and
194:\begin{theorem}[Arnold presentation {\cite{Arnold69}}; \texorpdfstring{$\bC \cong \bR^2$}{C = R2};
196:\label{thm:arnold-presentation}
197:\index{Arnold relations!presentation}
211:\begin{theorem}[Totaro presentation, general \texorpdfstring{$n$}{n} {\cite{Totaro96, Coh76}};
213:\label{thm:totaro-presentation}
3954:on the adjoint representation valued in the trivial
3955:representation.
3982:representation to the trivial representation. Since the
4016:representation provides no equivariant maps to or from the
4017:trivial representation. This is specific to the
4052:representation valued in $\CC$. The space of such forms is
4255:$\mathfrak{sl}_2$-equivariant maps between representations.
4298:bilinear form on the adjoint representation:
4316:form on the adjoint representation:
4946:\item The monodromy representation of~$\nabla^{\mathrm{ch}}$
4959:The presentation here identifies this connection as the



thinking
**Considering presentation listings**

It looks like the file does not list the "five presentations of SC," even though the user asked about it. I wonder if I should search the repo to confirm their absence. The likely answer is no, as they’re probably not included. My exact fix needs to involve either adding a proposition that lists the five presentations or cross-referencing them. I could mention the phrase doesn't appear, and pinpoint the exact line, perhaps adding a proposition after Definition 1220.
thinking
**Investigating structural fixes**

I want to explore structural fixes based on other files if the presentations exist. I should look for what presentations are actually present in the repository, particularly the Swiss-cheese pair sections or mentions of Boardman-Vogt and the Koszul dual cooperad. I’m thinking about whether I can find enough information to offer an exact fix, like cross-referencing different formulations of SC in the target file. I’ll inspect sections around prop 1595 onwards for a possible solution.
thinking
**Checking definitions and weaknesses**

I need to verify if E1(m) is defined, and I’m guessing it probably is. If it is, that’s not particularly noteworthy, but I should pinpoint actual weaknesses in the definitions instead. From what I'm reading, it seems that Definition 1220 lacks a precise explanation of symmetric group actions and composition maps. It mentions componentwise actions but doesn’t clarify how mixed symmetric groups operate on FM_k(C) × E1(m) or how mixed color permutations are handled.
exec
/bin/zsh -lc 'rg -n -F "codimension-1" chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Boardman--Vogt" chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "local chiral Swiss-cheese pair" chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "def:chiral-hochschild" chapters/theory/en_koszul_duality.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/en_koszul_duality.tex:1951:because both are determined by the codimension-1 boundary
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:45:is the terminal local chiral Swiss-cheese pair over~$\cA$.
chapters/theory/chiral_center_theorem.tex:1113:A \emph{local chiral Swiss-cheese pair} over an
chapters/theory/chiral_center_theorem.tex:1197:A \emph{morphism of local chiral Swiss-cheese pairs}
chapters/theory/chiral_center_theorem.tex:1209:A local chiral Swiss-cheese pair in the sense above is
chapters/theory/chiral_center_theorem.tex:1231:define the \emph{universal local chiral Swiss-cheese pair}
chapters/theory/chiral_center_theorem.tex:1304:The universal local chiral Swiss-cheese pair
chapters/theory/chiral_center_theorem.tex:1311:of local chiral Swiss-cheese pairs over~$A$.
chapters/theory/chiral_center_theorem.tex:1313:More precisely: for any local chiral Swiss-cheese pair
chapters/theory/chiral_center_theorem.tex:1315:\emph{unique} morphism of local chiral Swiss-cheese pairs
chapters/theory/chiral_center_theorem.tex:1599:morphism of local chiral Swiss-cheese pairs over~$A$. We
 succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:1404:$W(\mathsf{SC}^{\mathrm{ch,top}})$ (the Boardman--Vogt resolution),
 succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:1811:\textup{(}Definition~\textup{\ref{def:chiral-hochschild})},
chapters/theory/en_koszul_duality.tex:1898:(Definition~\ref{def:chiral-hochschild},
chapters/theory/chiral_center_theorem.tex:36:(Definition~\ref{def:chiral-hochschild-cochain-brace},
chapters/theory/chiral_center_theorem.tex:299:\label{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:349:Definition~\ref{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:1923: complex of Definition~\ref{def:chiral-hochschild-cochain-brace}.
chapters/theory/chiral_hochschild_koszul.tex:4896:Definition~\ref{def:chiral-hochschild-cochain-brace}. In that

thinking
**Inspecting codimension boundaries**

I need to look into the codimension-1 boundaries around 1951 and see how they relate to the broader context. It seems important to gather insights from the period of 1930 to 1960 as well. I’m curious about how these elements interconnect, and I want to ensure I'm thorough in my examination. There’s likely valuable information to uncover there that could enhance my understanding. Let’s explore this further!
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1930,1965p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1930	\FM_{k+\ell-1}(\bC)$
  1931	inserts a degree-$\ell$ closed element into the $i$-th slot
  1932	of a degree-$k$ element. At the chain level, for a center
  1933	element $\phi \in Z_{\mathsf{SC}}(A)_k$, this composition acts
  1934	by restricting~$\phi$ to the boundary stratum
  1935	$\partial_{ij}\FM_k(\bC)$ where $z_i \to z_j$ and extracting the
  1936	residue of the chiral product~$\mu$:
  1937	\[
  1938	(d_{\mathrm{fact}}\phi)(z_1, \ldots, z_{k-1})
  1939	= \sum_{1 \leq i < j \leq k}
  1940	(-1)^{\epsilon(i,j)}\,
  1941	\operatorname{Res}_{z_i = z_j}
  1942	\bigl[\phi(\ldots, z_i, \ldots, z_j, \ldots)
  1943	\cdot \mu(a_i, a_j)\bigr],
  1944	\]
  1945	where $\epsilon(i,j)$ is the Koszul sign from permuting $a_i$ past
  1946	$a_{i+1}, \ldots, a_{j-1}$. This is the factorization component
  1947	$d_{\mathrm{fact}}$ from
  1948	Theorem~\ref{thm:chiral-hochschild-differential}: the
  1949	residue extraction at collision divisors $D_{ij} \subset

thinking
**Investigating theorem proof**

I need to look further into the continuation of the theorem proof to find any supporting elements. This could help me spot any gaps that might exist. I want to ensure everything is well-founded and coherent, so checking for those details is important. It might clarify my understanding and strengthen the overall argument. Let's see what I can uncover!
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1964,2015p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1964	\emph{(c.4) Verification that $d^2 = 0$ is preserved.}
  1965	The identity $d_{\mathrm{Hoch}}^2 = 0$ is proved in
  1966	Theorem~\ref{thm:chiral-hochschild-differential} by checking
  1967	three pure squares and three anticommutators. Under the
  1968	identification of Steps~2b--2c, each cancellation in the center
  1969	differential maps to the corresponding cancellation in the
  1970	Hochschild differential: $d_{\mathrm{int}}^2 = 0$ from
  1971	$d_\cA^2 = 0$;
  1972	$d_{\mathrm{config}}^2 = 0$ from
  1973	$d_{\mathrm{dR}}^2 = 0$;
  1974	$d_{\mathrm{fact}}^2 = 0$ from the Borcherds identity
  1975	(iterated residues at overlapping collision divisors);
  1976	$\{d_{\mathrm{int}}, d_{\mathrm{fact}}\} = 0$
  1977	because $\mu$ is a $\cD_X$-module map;
  1978	$\{d_{\mathrm{int}}, d_{\mathrm{config}}\} = 0$
  1979	because $d_\cA$ and $d_{\mathrm{dR}}$ act on independent tensor
  1980	factors;
  1981	$\{d_{\mathrm{fact}}, d_{\mathrm{config}}\} = 0$
  1982	by the Arnold--Orlik--Solomon relations on $\FM_k(\bC)$.
  1983	Hence the identification of Step~2b is an isomorphism of



thinking
**Investigating references and issues**

I need to check for lines with unsupported equalities or object conflation carefully. The user likely wants exact fixes for each finding, so I should probably present a review of findings ordered by severity. I’ll want to avoid false positives but still be thorough. Running a LaTeX check might help identify any undefined references or labels. I might consider using `rg` to look for labels or compiling the target chapter, but it’s important to choose wisely since it could get complicated.
thinking
**Verifying unresolved references**

I need to confirm the actual unresolved references in the project. I’m considering using a shell command with tools like Perl or Awk to extract references. While the instructions suggest avoiding Python for this task, I can use `rg` to extract `\ref{}` and grep for labels. I might check only within relevant line regions, but it could be beneficial to analyze the full file. The user specifically wants to address unresolved references, so I’ll focus on finding those and ensuring all labels are correctly defined.
thinking
**Executing shell command with rg**

Alright, I’m planning to use a shell command with `rg -o`. This should help me extract the necessary information efficiently. I think using `rg` is a good choice for this task since it’s powerful for searching within files. I’ll have to ensure I specify the correct parameters to get accurate results. It’s simple enough but crucial that I get it right the first time, so I’ll double-check everything before running it.
codex
I have enough local context to start adversarial verification. I’m now checking the referenced labels and imported definitions mechanically, because a polished theorem paragraph is worthless if its support surface is missing or downgraded elsewhere.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:topologization}' metadata/theorem_registry.md chapters/connections/concordance.tex chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:bar-swiss-cheese}' metadata/theorem_registry.md chapters/connections/concordance.tex chapters/theory/en_koszul_duality.tex CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'refs=$(sed -n '"'1196,3470p' chapters/theory/en_koszul_duality.tex | rg -o '\\\\(?:ref|eqref|textup\\{\\\\ref)\\{["'^}]+'"' -r '"'$0'"' | sed -E 's/.*\\{//' | sort -u); for r in "'$refs; do count=$(rg -n -F "'"\\\\label{"'$r}" chapters appendices metadata 2>/dev/null | wc -l | tr -d '"' '); if [ \""'$count" = "0" ]; then echo "MISSING $r"; fi; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'refs=$(sed -n '"'1196,3470p' chapters/theory/en_koszul_duality.tex | rg -o '\\\\cite(?:\\[["'^]]*'"\\])?\\{["'^}]+'"' | sed -E 's/.*\\{//' | tr ',' '\\n' | sed 's/"'^ *//;s/ *$//'"' | sort -u); for c in "'$refs; do count=$(rg -n -F "$c" bibliography.bib references.bib *.bib chapters appendices 2>/dev/null | wc -l | tr -d '"' '); if [ \""'$count" = "0" ]; then echo "MISSING_CITE $c"; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:2968:\label{thm:topologization}
 succeeded in 53ms:
chapters/theory/en_koszul_duality.tex:1295:\label{thm:bar-swiss-cheese}% label retained for backward compatibility
 succeeded in 52ms:
MISSING chap:config-spaces
chap:higher-genus
conj:center-essential-surjectivity
conj:topologization-general
constr:sugawara-antighost
conv:bar-coalgebra-identity
cor:center-functor
def:SC
def:chiral-braces
def:chiral-hochschild
def:inner-conformal-vector
def:operadic-center
def:two-colored-operad-vanishing
eq:TQG-result
eq:antighost-contraction-G
eq:bar-product-space
eq:center-action-maps
eq:center-as-derived-hom
eq:center-equalizer
eq:chiral-brace
 succeeded in 52ms:
zsh:1: no matches found: *.bib
MISSING_CITE Francis2013
HA
KS00
Keller06
KhanZeng25
Kon03
Tamarkin03
Voronov99

thinking
**Evaluating extraction command**

I think the extraction command I used was incorrect, possibly due to shell interpretation issues. It mentioned missing several labels, even those in the file, which might stem from how I executed the search. I’ll need to test a simpler approach, especially since it seems like my command only went through chapters and appendices. By searching directly for the string `\label{def:SC}` in my file, I should confirm if that works. Let's give it a try!
exec
/bin/zsh -lc "rg -n -F '\\label{def:SC}' chapters/theory/en_koszul_duality.tex && rg -n -F '\\label{thm:topologization}' chapters/theory/en_koszul_duality.tex && rg -n -F '\\label{conj:topologization-general}' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1221:\label{def:SC}
2968:\label{thm:topologization}
3108:\label{conj:topologization-general}

thinking
**Troubleshooting command variables**

I’m thinking that the command variable splitting might be acting strange. It seems like I got extra lines that aren’t useful, so I can probably ignore them. I should focus on manually checking for the existence of targeted labels using something simpler like `rg`. It could help to inspect just the main ones. I’m also considering if I should use the LaTeX build or search bibliography files. I need to locate `.bib` files with `rg --files -g '*.bib'`.
exec
/bin/zsh -lc "rg -n -F '\\label{def:operadic-center}' chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{prop:operadic-center-existence}' chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{prop:fm-boundary-strata}' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files -g '*.bib'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:1669:\label{def:operadic-center}
chapters/theory/en_koszul_duality.tex:1669:\label{def:operadic-center}
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:1741:\label{prop:operadic-center-existence}
chapters/theory/en_koszul_duality.tex:1741:\label{prop:operadic-center-existence}
 succeeded in 51ms:
standalone/references.bib
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:298:\label{prop:fm-boundary-strata}
chapters/theory/en_koszul_duality.tex:298:\label{prop:fm-boundary-strata}

thinking
**Inspecting definitions and theorems**

I should check the definition of `operadic-center` and the theorem `prop:operadic-center-existence` to see if the center definition applies correctly to a single open algebra. It probably makes sense to read around the sections from 1650 to 1767, just to see if there are any issues or inconsistencies. I mean, it’s essential to ensure everything lines up properly, right? Let’s dive into that!
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1650,1767p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '2088,2125p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '560,680p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{def:chiral-hochschild-cochain-brace}' chapters/theory/chiral_center_theorem.tex && rg -n -F '\\label{thm:chiral-hochschild-differential}' chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1650	\]
  1651	where
  1652	$\mathfrak{g}_\cA^{\mathrm{mod}}
  1653	= \operatorname{Conv}(\operatorname{Lie}^c, \operatorname{End}_\cA)$
  1654	controls the closed direction
  1655	(shadows $\kappa$, $\mathfrak{C}$, $\mathfrak{Q}$)
  1656	and
  1657	$\mathfrak{g}_\cA^{\mathbb{R}}
  1658	= \operatorname{Conv}(\operatorname{Ass}^c, \operatorname{End}_\cA)$
  1659	controls the open direction
  1660	($r$-matrix, KZ associator, Yangian deformation).
  1661	The two factors commute. The mixed sector
  1662	\textup{(}Proposition~\textup{\ref{prop:sc-koszul-dual-three-sectors}(iii)}\textup{)}
  1663	governs their interaction: bulk operators acting on boundary
  1664	states via iterated brace evaluation
  1665	\textup{(}Proposition~\textup{\ref{prop:mixed-sector-bulk-boundary}}\textup{)}.
  1666	\end{corollary}
  1667	
  1668	\begin{definition}[Operadic center]
  1669	\label{def:operadic-center}
 succeeded in 52ms:
  2088	on the total dimension. The dimension of $\ChirHoch^1$ grows with
  2089	$\dim(\fg)$: it is $8$ for $\mathfrak{sl}_3$, $15$ for
  2090	$\mathfrak{sl}_4$, $248$ for type $E_8$.
  2091	\end{remark}
  2092	
  2093	\begin{proposition}[Gerstenhaber bracket on
  2094	$\ChirHoch^1(V_k(\mathfrak{sl}_2))$; \ClaimStatusProvedHere]
  2095	\label{prop:gerstenhaber-sl2-bracket}
  2096	\index{Gerstenhaber bracket!affine sl2@affine $\mathfrak{sl}_2$|textbf}
  2097	Let $V_k(\mathfrak{sl}_2)$ be the affine vertex algebra at generic
  2098	level~$k$ \textup{(}$k \neq -2$\textup{)}.
  2099	The Gerstenhaber bracket of degree~$-1$ on
  2100	$\ChirHoch^*(V_k(\mathfrak{sl}_2))$
  2101	restricts on $\ChirHoch^1 \times \ChirHoch^1 \to \ChirHoch^1$ to
  2102	the $\mathfrak{sl}_2$ Lie bracket:
  2103	\begin{align}
  2104	[D_e,\, D_f] &= D_h, \label{eq:gerst-ef}\\
  2105	[D_h,\, D_e] &= 2\,D_e, \label{eq:gerst-he}\\
  2106	[D_h,\, D_f] &= -2\,D_f, \label{eq:gerst-hf}
  2107	\end{align}
 succeeded in 52ms:
   560	\begin{proposition}[Pre-Lie relation for the single brace; \ClaimStatusProvedHere]
   561	\label{prop:pre-lie-chiral}
   562	\index{pre-Lie!chiral braces}
   563	The single-brace operation on $C^\bullet_{\mathrm{ch}}(A, A)$
   564	satisfies the pre-Lie identity: for all $a, b, c$,
   565	\[
   566	a\{b\}\{c\} - a\{b\{c\}\}
   567	= (-1)^{\|b\| \cdot \|c\|}
   568	\bigl(a\{c\}\{b\} - a\{c\{b\}\}\bigr).
   569	\]
   570	\end{proposition}
   571	
   572	\begin{proof}
   573	Both sides are double insertions into~$a$. On the
   574	left, $a\{b\}\{c\}$ inserts $b$ first (at position~$i$)
   575	then $c$ (at position~$j$), while $a\{b\{c\}\}$
   576	inserts $c$ into~$b$ first and then the composite
   577	into~$a$. The non-nested terms ($i \ne j$ and $c$ not
   578	inside~$b$) on the left are paired with the corresponding
   579	non-nested terms on the right (with~$b$ and $c$ exchanged)
 succeeded in 52ms:
299:\label{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_hochschild_koszul.tex:173:\label{thm:chiral-hochschild-differential}
chapters/theory/chiral_hochschild_koszul.tex:173:\label{thm:chiral-hochschild-differential}

thinking
**Considering code issues**

I’m thinking about whether to search for build warnings or compile issues in the target file. It might not be necessary, but checking for duplicate labels could help since the user asked about unresolved references. I could ensure labels are unique in the target file across the repository. For instance, `thm:bar-swiss-cheese` seems to be unique, and `thm:topologization` might also be the only one. I also need to check if citations exist in the bibliography by searching within `standalone/references.bib`.
exec
/bin/zsh -lc "rg -n '\\\\(?:ref|eqref)\\{chap:config-spaces\\}|\\\\(?:ref|eqref)\\{chap:higher-genus\\}|\\\\(?:ref|eqref)\\{warn:multiple-e1-chiral\\}' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{chap:config-spaces}' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex && rg -n -F '\\label{chap:higher-genus}' chapters/theory/*.tex chapters/*.tex && rg -n -F '\\label{warn:multiple-e1-chiral}' chapters/theory/*.tex chapters/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{conj:center-essential-surjectivity}' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex && rg -n -F '\\label{subsec:center-essential-surjectivity}' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex && rg -n -F '\\label{cor:center-functor}' chapters/theory/*.tex && rg -n -F '\\label{rem:center-surjectivity-failure}' chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for c in Francis2013 HA KS00 Keller06 KhanZeng25 Kon03 Tamarkin03 Voronov99 Arnold69 Totaro96 Coh76 Dunn88 Getzler94 GJ; do if rg -n -F "@" standalone/references.bib | rg -n -F "$c" >/dev/null; then echo "FOUND $c"; else rg -n -F "$c" standalone/references.bib || echo "MISSING $c"; fi; done' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
chapters/theory/configuration_spaces.tex:2:\label{chap:config-spaces}
zsh:1: no matches found: chapters/*.tex
 succeeded in 52ms:
2077:See Warning~\ref{warn:multiple-e1-chiral}.
2123:of Chapter~\ref{chap:config-spaces}. Difficulties~(b)
2125:(Chapter~\ref{chap:higher-genus}). At genus~$0$, difficulties
 succeeded in 53ms:
chapters/theory/en_koszul_duality.tex:2725:\label{conj:center-essential-surjectivity}
chapters/theory/en_koszul_duality.tex:2725:\label{conj:center-essential-surjectivity}
chapters/theory/en_koszul_duality.tex:2652:\label{subsec:center-essential-surjectivity}
chapters/theory/en_koszul_duality.tex:2652:\label{subsec:center-essential-surjectivity}
chapters/theory/en_koszul_duality.tex:2551:\label{cor:center-functor}
chapters/theory/en_koszul_duality.tex:2783:\label{rem:center-surjectivity-failure}
 succeeded in 352ms:
MISSING Keller06
FOUND KhanZeng25
MISSING Kon03
MISSING Tamarkin03
MISSING Voronov99
FOUND Arnold69
MISSING Totaro96
MISSING Coh76
MISSING Dunn88
MISSING Getzler94
MISSING GJ

thinking
**Evaluating the citation check**

I’m realizing that the citation check command might be incorrect because grepping for `@` and then using `rg -F` on the output doesn't seem right. I should consider if references.bib is actually the main bibliography file. I think it makes sense to inspect the entries closely. It looks like using `rg` directly may be a better approach to clarify the situation. I’ll keep that in mind as I move forward!
exec
/bin/zsh -lc "rg -n -F '\\label{chap:higher-genus}' chapters/theory chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for c in Francis2013 HA KS00 Keller06 KhanZeng25 Kon03 Tamarkin03 Voronov99 Totaro96 Coh76 Dunn88 Getzler94 GJ; do rg -n -F "$c" standalone/references.bib || echo "MISSING $c"; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{warn:multiple-e1-chiral}' chapters/theory chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:2:\label{chap:higher-genus}
chapters/theory/higher_genus_foundations.tex:2:\label{chap:higher-genus}
exec
/bin/zsh -lc "rg -n -F '\\label{def:chiral-hochschild}' chapters/theory chapters appendices && rg -n -F '\\label{def:chiral-braces}' chapters/theory chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/algebraic_foundations.tex:2278:\label{warn:multiple-e1-chiral}
chapters/theory/algebraic_foundations.tex:2278:\label{warn:multiple-e1-chiral}
 succeeded in 53ms:
chapters/theory/hochschild_cohomology.tex:470:\label{def:chiral-hochschild}
chapters/theory/hochschild_cohomology.tex:470:\label{def:chiral-hochschild}
chapters/theory/en_koszul_duality.tex:2312:\label{def:chiral-braces}
chapters/theory/en_koszul_duality.tex:2312:\label{def:chiral-braces}
 succeeded in 129ms:
MISSING Tamarkin03
MISSING Voronov99
MISSING Totaro96
MISSING Coh76
MISSING Dunn88
MISSING Getzler94
MISSING GJ
exec
/bin/zsh -lc "nl -ba standalone/references.bib | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for c in Francis2013 HA KS00 Keller06 Kon03 Tamarkin03 Voronov99 Totaro96 Coh76 Dunn88 Getzler94 GJ; do echo "-- $c"; rg -n -F "$c" .; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	% Shared bibliography for standalone papers
     2	% Modular Koszul Duality programme — R. Lorgat
     3	
     4	% ============================================================
     5	%  A
     6	% ============================================================
     7	
     8	@article{AbouzaidGeneration,
     9	  author  = {Abouzaid, Mohammed},
    10	  title   = {A geometric criterion for generating the Fukaya category},
    11	  note    = {Preprint and related published versions},
    12	}
    13	
    14	@article{ADKMV,
    15	  author  = {Aganagic, Mina and Dijkgraaf, Robbert and Klemm, Albrecht
    16	             and Mari\~no, Marcos and Vafa, Cumrun},
    17	  title   = {Topological strings and integrable hierarchies},
    18	  journal = {Comm. Math. Phys.},
    19	  volume  = {261},
    20	  year    = {2006},
 succeeded in 598ms:
./CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
./CLAUDE.md:818:(c) A^1 ALREADY HAS ARNOLD RELATIONS. Configuration spaces Conf_n(A^1) carry the Arnol'd algebra: the forms omega_ij = d log(z_i - z_j) satisfy the Arnold relation omega_ij ^ omega_jk + cyc = 0. These are present on A^1, NOT only on P^1. The passage point -> A^1 introduces configuration-space topology, FM compactifications, and the ordered-vs-unordered bar distinction. The passage A^1 -> P^1 adds compactness and different global topology (compact FM compactifications, different homotopy type of Conf_n(P^1) vs Conf_n(A^1)).
./CLAUDE.md:819:CONSEQUENCES: (i) genus-0 chiral Koszul duality is NOT "just" classical Koszul duality—the passage from a point to A^1 already introduces Arnold relations, FM compactifications, and the E_1/E_inf bar distinction; (ii) claims that "everything new happens at g >= 1" are overstated—curvature/anomaly phenomena are new at g >= 1, but configuration-space geometry is new already at g = 0 on A^1; (iii) the fiber of modular Koszul duality over each step of the chain point <- D -> A^1 -> P^1 -> general X has not been systematically studied in this programme and should not be claimed to be trivial; (iv) even at the first step (formal disk vs point), the comparison requires the retraction data and it is an open question whether modular Koszul duality sees the thickening. BEFORE writing any claim comparing Koszul duality "over a point" with "over a curve": specify WHICH space (point / formal disk D / A^1 / P^1 / general X), specify the COMPARISON DATA (retraction, localization, formal thickening), state WHETHER the identification is on-the-nose or requires extra structure, and acknowledge WHAT geometric content is present in each step.
./CLAUDE.md:848:AP166: SC^{ch,top} is NOT Koszul self-dual. SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!. SC = (Com, Ass, product-mixed) with closed dim = 1. MANIFESTLY DIFFERENT. What IS true: the bar-cobar duality functor on SC-algebras is an involution ((A^!)^! ~ A). Koszul duality EXCHANGES Com (closed) with Lie (closed); Ass (open) is self-dual. The Livernet [Liv06] citation proves Koszulity, NOT self-duality. FORBIDDEN: "(SC^{ch,top})^! ~ SC^{ch,top}" or "SC is Koszul self-dual." CORRECT: "SC Koszul duality exchanges Com <-> Lie while preserving Ass; the duality functor is an involution."
./CLAUDE.md:853:AP171: Associator dependence dichotomy. The chiral QG equivalence (R-matrix <-> A_inf <-> coproduct) holds "up to choice of Drinfeld associator Phi." COHOMOLOGICAL derived center = ASSOCIATOR-INDEPENDENT (proved for sl_2: GRT_1 shifts P_3 by coboundaries). COCHAIN-LEVEL derived center = ASSOCIATOR-DEPENDENT (the cochain-level E_3 carries the quantum group structure). Bar-side invariants (kappa, shadow tower) are associator-FREE. Cobar-side and coproduct-side depend on Phi. Analogous to deformation quantization: gauge-equivalent star products.
./wave2_audit_20260413_001942/S09_examples_mutual.md:34:You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
./wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:31:You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
./AGENTS.md:553:| MC5 | ANALYTIC+CODERIVED PROVED, CHAIN CONJECTURAL | |
./wave2_audit_20260413_001942/S20_readme_to_manuscript.md:40:You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
./wave2_audit_20260413_001942/S20_readme_to_manuscript.md:767:    17	_SLOW_SUITE_LOCK_HANDLE = None
./wave2_audit_20260413_001942/F02_definitions_koszul.md:48:You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
./wave2_audit_20260413_001942/F02_definitions_koszul.md:595:  1183	%%% INTRINSIC CHARACTERIZATIONS OF CHIRAL KOSZULNESS
./wave2_audit_20260413_001942/F02_definitions_koszul.md:1273:  2550	Lurie's $\infty$-categorical Barr--Beck theorem~\cite[Theorem~4.7.3.5]{HA}
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:15:- [HIGH] `../calabi-yau-quantum-groups/README.md:41` — PROBLEM: the bridge table and status table conflate associative CoHA data with chiral data: line 41 says `CoHA = E_1-sector of quantum vertex chiral group`, line 42 uses bare `kappa(A)`, and line 59 marks `CoHA = E_1 sector` as proved. This directly violates Vol III AP-CY7 in `../calabi-yau-quantum-groups/CLAUDE.md:89-99`. FIX: split the table into distinct rows: `CoHA / associative Hall algebra data` and `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{BKM}}`; replace `kappa(A)` with the correct subscripted invariant; change the status row to “CoHA/Yangian identification on the associative side: proved” and remove any claim that CoHA is already an `E_1`-chiral sector of `G(X)`.
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:17:- [HIGH] `../calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:67` — PROBLEM: this chapter says the toric fan is the root datum of a quantum vertex chiral group `G(X)` and then states `The CoHA = the positive half of G(X) = the E_1-chiral sector`. That is exactly the AP-CY7 forbidden conflation in `CLAUDE.md:91-99`. FIX: rewrite lines 67-80 so they only claim the associative part: “the toric fan determines the quiver, the CoHA, and the affine super Yangian data; a global chiral group `G(X)` is conjectural, and CoHA is evidence for the ordered associative side, not an identified `E_1`-chiral sector.”
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:46:You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:423:     8	At $d = 2$, the functor is unconditional: the $\bS^2$-framing of Kontsevich--Vlassopoulos enhances $\Fact_X(\mathfrak{L}_\cC)$ to an $\Etwo$-chiral algebra, and $\Phi$ is constructed end-to-end. At $d = 3$, a fundamental obstruction intervenes. The native $E_3$-structure on $\HH_\bullet(\cC)$ restricts to \emph{symmetric} braiding under Dunn additivity; the nonsymmetric quantum group braiding that physics demands can only be recovered through the Drinfeld center of the $\Eone$-monoidal representation category. This chapter verifies the $d = 3$ chain end-to-end for $\C^3$, where both sides are independently known (CoHA$(\C^3) \simeq Y^+(\widehat{\fgl}_1)$ on the CY side, $\cW_{1+\infty}$ at $c=1$ on the chiral side), and sets up the quiver-chart gluing that assembles global $\Eone$-chiral algebras from local CoHA charts.
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:450:**Verifying CoHA claims**
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:452:In Vol III, I'm noting that CLAUDE says CoHA is associative and connects to chiral via the functor Phi, but it’s not a direct identification. The README line 41 mentions a role in Vol III, but the status table states that `CoHA = E_1 sector | Proved`, which might violate the AP-CY7 principle. I'll need to check if the source files make a direct claim, especially against `CLAUDE.md`, which clarifies that while CoHA is associative, it isn’t the same as E1-chiral algebra. Therefore, README lines 41 and 59 may be inaccurate.
./wave2_audit_20260413_001942/S17_v1_to_v3_bridge.md:511:  1081	 \item \emph{Character preservation} (necessary, not sufficient). The graded characters of $\CoHA(Q_\alpha, W_\alpha)$ and $\CoHA(Q_\beta, W_\beta)$ coincide: the Donaldson--Thomas partition function is wall-crossing invariant (Kontsevich--Soibelman). Equal characters do not imply algebra isomorphism, but character \emph{mismatch} would refute it.

thinking
**Investigating bibliography entries**

I found that some bibliography entries are located in bibliography/references.tex but not in standalone/references.bib. This could mean unresolved citations won't appear correctly if main.tex includes references from the .tex file instead of using BibTeX. 

I’m wondering if I need to check main.tex for any bibliography inclusion. It seems the citations probably resolve through references.tex. I might consider running a local build and searching for `\input{bibliography/references.tex}` in main.tex, but only if I find unresolved citations. I should also check if the target file uses `\cite{Keller06}` without a corresponding bibitem. I'll search across the repo for clarity.
exec
/bin/zsh -lc 'for c in Francis2013 HA KS00 Keller06 KhanZeng25 Kon03 Tamarkin03 Voronov99 Totaro96 Coh76 Dunn88 Getzler94 GJ; do echo "-- $c"; rg -n -F "'"\\\\bibitem{"'$c}" bibliography/references.tex standalone/ordered_chiral_homology.tex standalone/N6_shadow_formality.tex 2>/dev/null || echo "NO_BIBITEM $c"; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\cite{Keller06}' chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\cite{KS00}' chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Keller06' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:2767: Keller~\cite{Keller06} shows that for derived-simple algebras
chapters/theory/hochschild_cohomology.tex:972:The result is standard: see Keller~\cite{Keller06},
chapters/theory/hochschild_cohomology.tex:1121:\mathrm{HH}^\bullet(A)$ is implicit in Keller~\cite{Keller06} and
chapters/theory/en_koszul_duality.tex:2767: Keller~\cite{Keller06} shows that for derived-simple algebras
 succeeded in 50ms:
chapters/theory/chiral_center_theorem.tex:1360:Kontsevich--Soibelman~\cite{KS00}.
chapters/theory/en_koszul_duality.tex:2087:(Kontsevich--Soibelman~\cite{KS00},
chapters/theory/en_koszul_duality.tex:2412:by Kontsevich--Soibelman~\cite{KS00} and extending to the chiral
chapters/theory/en_koszul_duality.tex:2087:(Kontsevich--Soibelman~\cite{KS00},
chapters/theory/en_koszul_duality.tex:2412:by Kontsevich--Soibelman~\cite{KS00} and extending to the chiral
chapters/theory/higher_genus_modular_koszul.tex:15171:Kontsevich--Soibelman~\cite{KS00},
chapters/theory/chiral_center_theorem.tex:1360:Kontsevich--Soibelman~\cite{KS00}.
 succeeded in 52ms:
./wave2_audit_20260413_001942/F02_definitions_koszul.md:1515:./bibliography/references.tex:799:\bibitem{Keller06}
./wave2_audit_20260413_001942/F02_definitions_koszul.md:1517:./chapters/connections/thqg_open_closed_realization.tex:854:(\cite[Theorem~1.2]{Keller06}).
./wave2_audit_20260413_001942/F02_definitions_koszul.md:1521:./chapters/theory/en_koszul_duality.tex:2767: Keller~\cite{Keller06} shows that for derived-simple algebras
./wave2_audit_20260413_001942/F02_definitions_koszul.md:1528:./chapters/theory/hochschild_cohomology.tex:929:\begin{proposition}[Morita equivalence {\cite{Keller06,Toen07}}; \ClaimStatusProvedElsewhere]
./wave2_audit_20260413_001942/F02_definitions_koszul.md:1529:./chapters/theory/hochschild_cohomology.tex:972:The result is standard: see Keller~\cite{Keller06},
./wave2_audit_20260413_001942/F02_definitions_koszul.md:1530:./chapters/theory/hochschild_cohomology.tex:1121:\mathrm{HH}^\bullet(A)$ is implicit in Keller~\cite{Keller06} and
./metadata/dependency_graph.dot:3227:  prop_morita_equivalence_compact_gen [label="prop:morita-equivalence-compact-gen\nproposition [Pr]\nMorita equivalence {\cite{Keller06,Toen0...", style=filled, fillcolor="#bbdefb"];
./chapters/connections/thqg_open_closed_realization.tex:854:(\cite[Theorem~1.2]{Keller06}).
./metadata/claims.jsonl:3109:{"label": "prop:morita-equivalence-compact-gen", "env_type": "proposition", "status": "ProvedElsewhere", "file": "chapters/theory/hochschild_cohomology.tex", "line": 908, "title": "Morita equivalence {\\cite{Keller06,Toen07}}", "cites_in_block": ["Keller06", "Toen07"]}
./chapters/theory/en_koszul_duality.tex:2767: Keller~\cite{Keller06} shows that for derived-simple algebras
./chapters/theory/hochschild_cohomology.tex:929:\begin{proposition}[Morita equivalence {\cite{Keller06,Toen07}}; \ClaimStatusProvedElsewhere]
./chapters/theory/hochschild_cohomology.tex:972:The result is standard: see Keller~\cite{Keller06},
./chapters/theory/hochschild_cohomology.tex:1121:\mathrm{HH}^\bullet(A)$ is implicit in Keller~\cite{Keller06} and
./bibliography/references.tex:799:\bibitem{Keller06}
 succeeded in 186ms:
bibliography/references.tex:799:\bibitem{Keller06}
-- KhanZeng25
bibliography/references.tex:811:\bibitem{KhanZeng25}
standalone/ordered_chiral_homology.tex:10785:\bibitem{KhanZeng25}
-- Kon03
bibliography/references.tex:840:\bibitem{Kon03}
-- Tamarkin03
standalone/N6_shadow_formality.tex:697:\bibitem{Tamarkin03}
standalone/ordered_chiral_homology.tex:10670:\bibitem{Tamarkin03}
bibliography/references.tex:1548:\bibitem{Tamarkin03}
-- Voronov99
bibliography/references.tex:1196:\bibitem{Voronov99}
-- Totaro96
bibliography/references.tex:1184:\bibitem{Totaro96}
-- Coh76
bibliography/references.tex:278:\bibitem{Coh76}
-- Dunn88
bibliography/references.tex:1456:\bibitem{Dunn88}
-- Getzler94
bibliography/references.tex:1465:\bibitem{Getzler94}

thinking
**Comparing target files**

I think it would be helpful to compare the target file with the concordance related to topologization or SC. I should check for any drift between them, as that could reveal discrepancies or areas that need attention. It might involve searching for relevant lines that highlight those differences. This process will ensure that I have a clear understanding of how the files align or misalign with one another.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '9528,9554p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7168,7192p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:bar-swiss-cheese' metadata/claims.jsonl chapters/connections/concordance.tex chapters/theory/introduction.tex CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:topologization' metadata/claims.jsonl chapters/connections/concordance.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  9528	
  9529	% ----------------------------------------------------------------------
  9530	\paragraph{April 2026 session: falsification test results.}
  9531	Five additional falsification tests were evaluated against this
  9532	session's structural corrections (AP165 operadic scoping,
  9533	SC self-duality retraction, topologization scoping, critical-level
  9534	Theorem~H failure).
  9535	\begin{itemize}
  9536	\item \textbf{FT-2} (bar complex cooperad structure):
  9537	 \emph{passed}. The bar complex $\barB(\cA)$ is confirmed as an
  9538	 $E_1$ coassociative coalgebra over $(\mathrm{ChirAss})^!$,
  9539	 not an $\SCchtop$-coalgebra (AP165).
  9540	\item \textbf{FT-4} (Theorem~H generic-level requirement):
  9541	 \emph{passed}. At critical level $k = -h^\vee$,
  9542	 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
  9543	 (Feigin--Frenkel center); Theorem~H does not apply.
  9544	 For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  9545	 $4$-periodic and unbounded.
  9546	\item \textbf{FT-5} (topologization scope):
  9547	 \emph{passed}. Topologization
 succeeded in 52ms:
  7168	 \textbf{SC self-duality retracted.}
  7169	 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
  7170	 \text{shuffle-mixed})$: the closed dimensions are
  7171	 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not}
  7172	 Koszul self-dual. The duality \emph{functor} is an
  7173	 involution; the \emph{operad} is not self-dual.
  7174	 See AP166/B57.} \\
  7175	\hline
  7176	\multicolumn{3}{p{13cm}}{%
  7177	 \textbf{Topologization scoped.}
  7178	 The topologization theorem
  7179	 (Theorem~\ref{thm:topologization}:
  7180	 $\SCchtop + \text{inner conformal vector} = E_3$)
  7181	 is proved for affine Kac--Moody at non-critical level.
  7182	 For general chiral algebras with conformal vector,
  7183	 topologization is conjectural
  7184	 (Conjecture~\ref{conj:coderived-e3} gives the
  7185	 $D^{\mathrm{co}}$-level upgrade).} \\
  7186	\hline
  7187	\multicolumn{3}{p{13cm}}{%
 succeeded in 51ms:
chapters/theory/introduction.tex:1598:(Theorem~\ref{thm:topologization} for affine Kac--Moody;
chapters/theory/introduction.tex:1739:Theorem~\ref{thm:topologization}
chapters/theory/introduction.tex:2204: Higher-dimensional bar complexes; Totaro relations; Ayala--Francis; topologization $\mathsf{SC}^{\mathrm{ch,top}} + T_{\mathrm{Sug}} \Rightarrow \Ethree$ (Thm~\ref{thm:topologization}, proved for affine KM; Conj~\ref{conj:topologization-general}, general) \\[6pt]
chapters/connections/concordance.tex:7179: (Theorem~\ref{thm:topologization}:
 succeeded in 51ms:
CLAUDE.md:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
metadata/claims.jsonl:482:{"label": "prop:ht-bar-genus-zero", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/holomorphic_topological.tex", "line": 118, "title": "Bar complex and genus-zero HT data", "refs_in_block": ["thm:bar-swiss-cheese", "thm:bar-cobar-isomorphism-main", "conv:bar-coalgebra-identity", "thm:bar-modular-operad"]}
metadata/claims.jsonl:2604:{"label": "thm:bar-swiss-cheese", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 1232, "title": "Bar complex as Swiss-cheese coalgebra", "refs_in_block": ["eq:bar-product-space"]}
metadata/claims.jsonl:2608:{"label": "thm:center-geometric-inevitability", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 2037, "title": "Geometric inevitability of the chiral center", "refs_in_block": ["thm:bar-swiss-cheese"]}
exec
/bin/zsh -lc "rg -n 'FM_0|\\\\FM_k\\(\\\\bC\\)|Fulton--MacPherson compactification|FM_k\\(' chapters/theory/en_koszul_duality.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '260,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
270:\subsection{\texorpdfstring{Fulton--MacPherson compactification in dimension $n$}{Fulton--MacPherson compactification in dimension n}}
272:\index{Fulton--MacPherson compactification!higher-dimensional}
276:The \emph{Fulton--MacPherson compactification}
1208:$d_{\barB}$ lives on $\FM_k(\bC)$ (the $n = 2$ slot); the
1213:\FM_k(\bC) \times \Conf_k(\bR),
1230: := \FM_k(\bC)$.
1235: := \FM_k(\bC) \times E_1(m)$.
1271:  $\FM_k(\bC)$ (the operadic center theorem,
1319: & $\FM_k(\bC)$: collision at boundary strata \\[2pt]
1366:divisors $D_S \subset \partial\FM_k(\bC)$
1379:structure: at genus~$0$ the spaces $\FM_k(\bC)$ and $\Conf_k(\bR)$
1407:$\FM_k(\bC) \times \Conf_k(\bR)$, the same spaces that
1798:$(\mathsf{SC}^{\mathrm{ch,top}})^{\mathsf{c}} = \{\FM_k(\bC)\}$
1824:= \FM_k(\bC) \times E_1(m)$.
1828:\FM_k(\bC) \times E_1(m)
1832:equivariant for the $\Sigma_k$-action on $\FM_k(\bC)$ and the
1836:\phi_{k,0}\colon \FM_k(\bC) \;\longrightarrow\; A,
1872:$\FM_k(\bC)$ of such $E_1$-endomorphisms. The open-sector bimodule
1883:\bigl[\Omega^*(\FM_k(\bC), \log D)
1889:logarithmic forms $\Omega^*(\FM_k(\bC), \log D)$ arise from the
exec
/bin/zsh -lc "rg -n -F 'FM_0(\\bC)' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'E_1(0)' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   260	$n = 2$ & surface/curve & chiral bar (this monograph) \\
   261	$n = 3$ & $3$-manifold & Chern--Simons bar \\
   262	general $n$ & $n$-manifold & $\En$ bar
   263	\end{tabular}
   264	\end{center}
   265	Main Theorems~A, B, C are the holomorphic refinement of the
   266	$n = 2$ chapter of $\En$ Koszul duality.
   267	\end{remark}
   268	
   269	
   270	\subsection{\texorpdfstring{Fulton--MacPherson compactification in dimension $n$}{Fulton--MacPherson compactification in dimension n}}
   271	\label{subsec:fm-general-n}
   272	\index{Fulton--MacPherson compactification!higher-dimensional}
   273	
   274	\begin{definition}[FM compactification of \texorpdfstring{$\Conf_k(\bR^n)$}{Conf-k(R-n)}]
   275	\label{def:fm-rn}
   276	The \emph{Fulton--MacPherson compactification}
   277	$\overline{\Conf}_k(\bR^n)$ is the real oriented blowup of $(\bR^n)^k$
   278	along all partial diagonals, ordered by reverse inclusion.
   279	Equivalently (Axelrod--Singer, Kontsevich), it is the closure of
 exited 1 in 51ms:

 succeeded in 50ms:
chapters/theory/en_koszul_duality.tex:1834:Setting $m = 0$ and noting that $E_1(0) = \mathrm{pt}$:
chapters/theory/en_koszul_duality.tex:1834:Setting $m = 0$ and noting that $E_1(0) = \mathrm{pt}$:



thinking
**Evaluating theorem claims**

I need to be concise in my phrasing here. The theorem topologization 2967 claims it's proven, but it cites KhanZeng25 in the title. In the proof, it only covers BRST cohomology using a construction and Lurie. I'm wondering whether it’s self-contained or if it depends on an external unpublished preprint. If the proof holds on its own, maybe the "proved here" statement is still valid.
thinking
**Evaluating Dunn additivity**

Earlier, I noticed that Dunn additivity doesn't apply to colored operads, according to both the previous file and CLAUDE. It suggests that after applying an inner conformal vector, the holomorphic translations become Q-exact. Then they equate that to E3^top, stating that this is Dunn additivity.  I’m wondering if that conclusion makes sense, or if there's something I’m missing here. It's a bit tricky!
thinking
**Looking into theorems and propositions**

I'm examining principle 1267-1268, but it seems to be prose rather than a theorem. I might need a proper theorem or an explicit map. There’s a proposition related to 5200, possibly involving the Khan-Zeng topological enhancement. I should search through lines 2285 and inspect the area around lines 2270-2292 to see if there’s an external theorem from Khan-Zeng that proves 3D theory. Time to read through that.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2268,2305p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2268	\end{equation}
  2269	The left arrow is Theorem~\ref{thm:operadic-center-hochschild}
  2270	(proved here).
  2271	The right arrow is the recognition theorem identifying
  2272	$W(\mathsf{SC}^{\mathrm{ch,top}})$-algebras with
  2273	holomorphic-topological prefactorization algebras on
  2274	$D \times \bR$ (Volume~II, items F4--F5; not proved
  2275	in this volume).
  2276	
  2277	This is the mechanism by which a $2$-dimensional chiral
  2278	algebra on a curve~$X$ produces a $3$-dimensional
  2279	holomorphic-topological bulk/boundary system on $X \times \bR$.
  2280	The extra dimension is the
  2281	universal normal-collar direction of a codimension-one boundary
  2282	condition, forced by the center construction.
  2283	
  2284	An independent physical construction corroborating this picture
  2285	is given by Khan--Zeng~\cite{KhanZeng25}, who
  2286	build a mixed holomorphic-topological gauge theory on
  2287	$\bR \times \bC$ from a freely generated Poisson vertex algebra

thinking
**Verifying mathematical concepts**

I'm looking closely at lines 2285 to 2299. It seems like Khan-Zeng built their theory from a freely generated Poisson vertex algebra rather than a universal affine vertex algebra. Wait, could it be that the PVA approximates a classical limit? The theorem relies on the universal affine vertex algebra, so I need to double-check whether Khan-Zeng applies. Just based on what's in this file, I see that the theorem's claim about topologization for affine KM might not be justified here.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5278,5338p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5278	algebraic encoding of this factorisation structure.
  5279	
  5280	Part (ii).
  5281	Khan--Zeng~\cite{KhanZeng25} prove the following at the
  5282	classical level: an inner Virasoro element in a Poisson
  5283	vertex algebra with non-degenerate central charge provides
  5284	a homotopy between the holomorphic and topological
  5285	directions, upgrading the HT theory to a fully topological
  5286	theory. We extend this to the quantum vertex algebra
  5287	$V_k(\fg)$. The Sugawara construction
  5288	(Frenkel--Ben-Zvi~\cite{FBZ04}, Chapter~15) produces
  5289	$T_{\mathrm{Sug}} \in V_k(\fg)$ satisfying the exact
  5290	Virasoro OPE
  5291	\[
  5292	  T_{\mathrm{Sug}}(z)\,T_{\mathrm{Sug}}(w) \;\sim\;
  5293	  \frac{c/2}{(z-w)^4}
  5294	  + \frac{2\,T_{\mathrm{Sug}}(w)}{(z-w)^2}
  5295	  + \frac{\partial T_{\mathrm{Sug}}(w)}{z-w}
  5296	\]
  5297	at central charge $c = k\,\dim(\fg)/(k+h^\vee)$, and the
exec
/bin/zsh -lc "rg -n -F 'chiral \\Ethree' chapters/theory/en_koszul_duality.tex && rg -n -F 'chiral "'$'"\\Ethree"'$'"' chapters/theory/en_koszul_duality.tex && rg -n -F 'E_3-chiral' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Searching for specific lines**

I’m aiming to find lines around 5203, although the phrasing might not be exact. I’ll try using a search command with regex — something like `rg -n 'Ethree.*holomorphic|holomorphic.*Ethree|chiral .*Ethree'`. This should help me track down what I need by looking for specific patterns associated with "Ethree" and "holomorphic." Let's see if this method gets me the results I'm hoping for!
exec
/bin/zsh -lc "rg -n 'holomorphic.*\\\\Ethree|\\\\Ethree.*holomorphic|chiral .*\\\\Ethree|\\\\Ethree.*chiral|E_3-chiral' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3062:$\Eone$-chiral and $\Ethree$; the conformal vector is
4267:The $\Ethree$-algebra structure on the derived chiral
4477:\subsection{The filtered $\Ethree$-chiral algebra}
4482:a filtered $\Ethree$-chiral algebra
4487:\begin{definition}[The filtered $\Ethree$-chiral algebra]
4489:The \emph{chiral $\Ethree$-algebra}
4511:\begin{theorem}[Structure of the chiral $\Ethree$-algebra]
4515:The chiral $\Ethree$-algebra
4535:  a filtered $\Ethree$-chiral algebra:
4547:  commutative structure to a filtered $\Ethree$-chiral
4554:  The $\Ethree$-chiral algebra
4909:The chiral $\Ethree$-algebra
4920:The chiral $\Ethree$-algebra
4995:The chiral $\Ethree$-algebra
5013:from the global sections of the chiral $\Ethree$-algebra
5103:restriction of the chiral $\Ethree$-algebra to~$D$ is an
5203:The chiral $\Ethree$-algebra is holomorphic: it depends on the
5230:chiral $\Ethree$-algebra, this means:
5233:  The chiral $\Ethree$-algebra
5277:dependence on $\RR$; the chiral $\Ethree$-algebra is the

thinking
**Considering volume and proof redundancy**

I’m thinking about how the volume needs to treat SC^{ch,top} as a first-class object. It seems significant to also include generators-and-relations and multiple presentations. Plus, there’s the aspect of many-fold proof redundancy. It feels quite complex, and I need to ensure I'm approaching this clearly. Let’s explore these ideas and their implications to fully understand how they work together.
exec
/bin/zsh -lc "rg -n 'thm:bar-swiss-cheese|thm:topologization|thm:operadic-center-hochschild' metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'local constancy' chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{thm:bar-swiss-cheese\\}|Bar complex as Swiss-cheese coalgebra|E_1-coassociative' chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/theory/en_koszul_duality.tex CLAUDE.md metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
482:{"label": "prop:ht-bar-genus-zero", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/holomorphic_topological.tex", "line": 118, "title": "Bar complex and genus-zero HT data", "refs_in_block": ["thm:bar-swiss-cheese", "thm:bar-cobar-isomorphism-main", "conv:bar-coalgebra-identity", "thm:bar-modular-operad"]}
2604:{"label": "thm:bar-swiss-cheese", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 1232, "title": "Bar complex as Swiss-cheese coalgebra", "refs_in_block": ["eq:bar-product-space"]}
2607:{"label": "thm:operadic-center-hochschild", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 1715, "title": "The operadic center of\n$\\mathsf{SC}^{\\mathrm{ch,top}}$ is the chiral Hochschild complex", "labels_in_block": ["thm:operadic-center-hochschild", "eq:center-hochschild-qi"], "refs_in_block": ["def:chiral-hochschild"]}
2608:{"label": "thm:center-geometric-inevitability", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 2037, "title": "Geometric inevitability of the chiral center", "refs_in_block": ["thm:bar-swiss-cheese"]}
exec
/bin/zsh -lc "rg -n 'SC\\"'^'"\\{ch,top\\}.*pair|\\(C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch\\}\\}\\(\\\\cA,\\\\cA\\),.*\\\\cA\\)|derived center.*pair|operadic center.*pair' chapters/theory/en_koszul_duality.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:3040:that converts local constancy of the factorization algebra
chapters/theory/en_koszul_duality.tex:3045:by local constancy is equivalent to the one governed by
chapters/theory/en_koszul_duality.tex:3178:  \textup{(}local constancy of the factorization algebra\textup{)} is proved on
chapters/theory/en_koszul_duality.tex:3410:\item \textup{(Coderived local constancy.)}
chapters/theory/en_koszul_duality.tex:3414:  $m_0$-curvature obstruction to local constancy at
chapters/theory/en_koszul_duality.tex:3465:across all four shadow classes: the obstruction to local constancy
 succeeded in 53ms:
chapters/theory/en_koszul_duality.tex:1295:\label{thm:bar-swiss-cheese}% label retained for backward compatibility
metadata/claims.jsonl:2604:{"label": "thm:bar-swiss-cheese", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/en_koszul_duality.tex", "line": 1232, "title": "Bar complex as Swiss-cheese coalgebra", "refs_in_block": ["eq:bar-product-space"]}
CLAUDE.md:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
CLAUDE.md:452:(2) WRONG: "The deconcatenation coproduct is the open/topological color of SC." TRUTH: Deconcatenation is the cofree tensor coalgebra structure on T^c(V). It is coassociative. This makes B(A) an E_1-coassociative coalgebra. It is NOT a separate "color" of a two-colored operad.
 succeeded in 53ms:
chapters/theory/en_koszul_duality.tex:3165:  $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\;\cA)$ is \emph{chain-level}

thinking
**Inspecting topologization and definitions**

I'm searching for the term "pair" in line 3165, and it looks like the theorem on topologization doesn't explicitly keep the pair. That's an interesting finding. I need to check if the definition of a two-colored operad with vanishing constraints is sufficient. It feels abstract, though. I noticed that the definition still lacks operations. Maybe the proposition at line 1595 offers some insights about the Koszul dual. I'll also look into a potential proposition for the mixed sector boundary.
exec
/bin/zsh -lc "rg -n -F '\\label{prop:mixed-sector-bulk-boundary}' chapters/theory/en_koszul_duality.tex && nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1620,1668p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'recognition theorem' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'holomorphic-topological prefactorization algebras on' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'not proved in this volume' chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:2273:holomorphic-topological prefactorization algebras on
 succeeded in 51ms:
chapters/connections/concordance.tex:426: Two independent proofs: (i)~operadic, via the recognition theorem
chapters/connections/concordance.tex:3904:$\SCchtop$, and the recognition theorem (Volume~II, items F4--F5)
chapters/connections/concordance.tex:11283: recognition theorem
chapters/theory/en_koszul_duality.tex:2134:\index{recognition theorem!and the center}
chapters/theory/en_koszul_duality.tex:2137:transparent once the recognition theorem (proved in Volume~II) is
chapters/theory/en_koszul_duality.tex:2151:Under the recognition theorem identifying
chapters/theory/en_koszul_duality.tex:2176:(Theorem~\ref{thm:bar-swiss-cheese}) with the recognition theorem.
chapters/theory/en_koszul_duality.tex:2184:recognition theorem identifies this sector with~$\cA$.
chapters/theory/en_koszul_duality.tex:2271:The right arrow is the recognition theorem identifying
chapters/theory/en_koszul_duality.tex:2609:recognition theorem. The chiral setting enriches each with
 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'mixed-sector-bulk-boundary|mixed sector' chapters/theory/en_koszul_duality.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1630:The mixed sector is computed by the K\"unneth
1661:The two factors commute. The mixed sector
1665:\textup{(}Proposition~\textup{\ref{prop:mixed-sector-bulk-boundary}}\textup{)}.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1595,1666p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1595	\begin{proposition}[Koszul dual cooperad of
  1596	\texorpdfstring{$\mathsf{SC}^{\mathrm{ch,top}}$}{SC}: three sectors;
  1597	\ClaimStatusProvedHere]
  1598	\label{prop:sc-koszul-dual-three-sectors}
  1599	\index{Swiss-cheese operad!Koszul dual cooperad|textbf}
  1600	\index{Koszul dual cooperad!Swiss-cheese three sectors}
  1601	The Koszul dual cooperad
  1602	$\mathsf{SC}^{\mathrm{ch,top},!}$ has three sectors:
  1603	\begin{enumerate}[label=\textup{(\roman*)}]
  1604	\item \emph{Closed} ($\mathsf{c}^n \to \mathsf{c}$):
  1605	 $\dim = (n{-}1)!$ \textup{(}Lie cooperad,
  1606	 since $\operatorname{Com}^! = \operatorname{Lie}$\textup{)}.
  1607	\item \emph{Open} ($\mathsf{o}^m \to \mathsf{o}$):
  1608	 $\dim = m!$ \textup{(}Ass cooperad,
  1609	 self-Koszul-dual\textup{)}.
  1610	\item \emph{Mixed} ($\mathsf{c}^k,\,\mathsf{o}^m \to \mathsf{o}$,
  1611	 $k \geq 1$):
  1612	 $\dim = (k{-}1)!\,\binom{k+m}{m}$.
  1613	 This differs from the plain tensor product
  1614	 $(k{-}1)!\cdot m!$ by the factor $\binom{k+m}{m}/m!$,

thinking
**Searching for references**

I'm trying to figure out where the prop:mixed-sector-bulk-boundary is. It seems like there might be a missing label or unresolved reference. I'll search across the entire repository to find any references to it. It's a bit tricky when things aren't clearly labeled, but I want to make sure I cover all my bases to locate it. Let's see what I can uncover!
exec
/bin/zsh -lc "rg -n -F '\\label{prop:mixed-sector-bulk-boundary}' chapters appendices bibliography standalone ." in /Users/raeez/chiral-bar-cobar succeeded in 207ms:
chapters/connections/thqg_open_closed_realization.tex:465:\label{prop:mixed-sector-bulk-boundary}
./chapters/connections/thqg_open_closed_realization.tex:465:\label{prop:mixed-sector-bulk-boundary}

thinking
**Checking theorem connections**

I'm delving into a label that exists in connections rather than in theory, so it doesn't seem unresolved. However, there’s a corollary related to a chapter on connections. I might have a potential issue with corollary 1639 regarding its \ClaimStatus. I should check if the theorem statuses in the target file are correctly marked, like theorem 2967 and theorem 1293 being proved. Also, I'll need to inspect if `thm:topologization` is in the theorem registry or concordance since it wasn't found in the excerpt.
exec
/bin/zsh -lc "rg -n 'thm:topologization|conj:topologization-general|conj:coderived-e3' metadata/claims.jsonl chapters/connections/concordance.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/introduction.tex:1598:(Theorem~\ref{thm:topologization} for affine Kac--Moody;
chapters/theory/introduction.tex:1599:Conjecture~\ref{conj:topologization-general} in general):
chapters/theory/introduction.tex:1739:Theorem~\ref{thm:topologization}
chapters/theory/introduction.tex:1749:(Conjecture~\ref{conj:topologization-general}). At critical
chapters/theory/introduction.tex:2204: Higher-dimensional bar complexes; Totaro relations; Ayala--Francis; topologization $\mathsf{SC}^{\mathrm{ch,top}} + T_{\mathrm{Sug}} \Rightarrow \Ethree$ (Thm~\ref{thm:topologization}, proved for affine KM; Conj~\ref{conj:topologization-general}, general) \\[6pt]
chapters/connections/concordance.tex:7136:\ref{conj:coderived-e3}
chapters/connections/concordance.tex:7179: (Theorem~\ref{thm:topologization}:
chapters/connections/concordance.tex:7184: (Conjecture~\ref{conj:coderived-e3} gives the
chapters/connections/concordance.tex:9748: \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\

thinking
**Checking metadata issues**

It seems like the metadata search didn't return results because the claims.jsonl file might not include the theorem. I should explore searching directly in the claims, as this might lead to better findings. It's interesting how data organization can sometimes lead to unexpected hiccups in searches like this. I wonder if there's a more efficient way to handle this or if I'm missing a step. Let’s see what the claims reveal!
exec
/bin/zsh -lc "rg -n 'topologization' metadata/claims.jsonl | sed -n '1,30p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:






thinking
**Analyzing metadata issues**

I'm noticing that the claims.jsonl file is missing a key element related to the topologization theorem. It seems the claims extractor might not have parsed it correctly, possibly due to the theorem's title being special. That could indicate a bug in the metadata sync process. However, the user has requested the file without hidden imports, which makes me wonder if the absence of this theorem is something I really need to address. 

I should check if the theorem lacks a ClaimStatus in the registry, given that it’s only tracking ProvedHere blocks. If it wasn’t generated after changes, that could be significant. This indicates a sync issue, and I'd need to regenerate the metadata after correcting any parse issues. Nonetheless, I’m not quite sure how relevant this is to the audit.
thinking
**Inspecting file audit issues**

The user asked for a file audit, so I’m considering if I should include cross-file metadata drift as a secondary point. I really need to figure out why claims.jsonl is missing some information. It may relate to the theorem title being cited on the same line, or possibly issues with the label line. 

It’s odd that these are missing. I should also look into the topologization theorem's context for references and fixes. There’s a problem with Definition 2946 regarding the inner conformal vector. It states that for the Virasoro algebra, T(z) is the stress tensor, but that doesn’t clarify whether it's inner relative to Q. Being merely the stress tensor doesn’t say anything about innerness, which feels misleading.
thinking
**Clarifying the definition**

The current wording implies that the Virasoro algebra serves as an example of an inner conformal vector, which contradicts the conjectural status I noted earlier. To fix this, I need to rewrite the sentence. It should say something like, "For Virasoro, the boundary conformal vector is the stress tensor itself; however, whether it is inner in that sense depends on a 3D bulk BRST complex and remains conjectural." This would align better with the nuances I’m trying to convey.
thinking
**Evaluating mathematical definitions**

I’m considering a remark that might not be relevant, but there could be an issue with line 1220, which defines a "Holomorphic-topological Swiss-cheese operad" without relating to the local chiral Swiss-cheese pair. The user wants a proper definition with generators and relations, and it seems the current definition lacks formal rigor, especially regarding codimension-1 relations. I think I should check the proof around line 1951 and search for "codimension-1 boundary" to find any relevant propositions.
thinking
**Analyzing definitions and theorems**

I’m looking at lines 1196-1245 and 1558-1568, where proof steps list five steps, but that's not what the user is asking for. There seems to be a potential issue in definition 1223 and theorem 1791 with using \(\FM_k(\C)\). The operadic center theorem assumes a "logarithmic chiral algebra," but a chiral algebra on a curve isn’t literally an algebra over the topological operad \(\{\FM_k(\C)\}\). It’s more like factorization/d-module data, and I need to clarify how the theorem relates to chain models. This aspect feels pretty subtle and possibly crucial.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2048,2074p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2588,2662p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1412,1442p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2048	of an $E_1$-algebra as an $E_{n+1}$-algebra at the
  2049	$\infty$-categorical level, specialized to $n = 1$).
  2050	\end{proof}
  2051	
  2052	\begin{remark}[Scope: $E_\infty$-chiral input]
  2053	\label{rem:center-scope-e-inf}
  2054	\index{operadic center!scope restriction}
  2055	Theorem~\ref{thm:operadic-center-hochschild} requires the chiral
  2056	algebra~$\cA$ to be $E_\infty$-chiral (logarithmic): the
  2057	operations extend to the log compactification of
  2058	$\Conf_k(\bC)$, equivalently, the factorization $\cD$-module
  2059	descends to the symmetric powers $X^{(n)}$ via the
  2060	$\Sigma_n$-equivariance built into the $\FM_k(\bC)$-action.
  2061	For genuinely $E_1$-chiral input (Yangians, Etingof--Kazhdan
  2062	quantum vertex algebras), the factorization $\cD$-module does
  2063	\emph{not} descend to $X^{(n)}$, the symmetric bar
  2064	$\barB^{\Sigma}(\cA)$ does not exist, and
  2065	$C^\bullet_{\mathrm{ch}}(\cA, \cA)$ as defined above is
  2066	ill-formed. In the $E_1$ setting, the correct replacement is
  2067	the \emph{ordered} Hochschild complex
 succeeded in 53ms:
  2588	\index{center theorem!summary}
  2589	Assembling Steps~1--5, the chiral center theorem is the conjunction
  2590	of four assertions:
  2591	\begin{enumerate}[label=\textup{(\arabic*)}]
  2592	\item \emph{Existence}: The operadic center
  2593	 $Z_{\mathsf{SC}}(A)$ exists for every $E_1$-algebra~$A$
  2594	 (Proposition~\ref{prop:operadic-center-existence}).
  2595	\item \emph{Identification}: $Z_{\mathsf{SC}}(A) \simeq
  2596	 C^{\bullet}_{\mathrm{ch}}(\cA, \cA)$ as $\Etwo$-algebras
  2597	 (Theorem~\ref{thm:operadic-center-hochschild}).
  2598	\item \emph{Geometric realization}: The center computes
  2599	 interior bulk observables in the half-space
  2600	 $X \times \bR_{\geq 0}$
  2601	 (Theorem~\ref{thm:center-geometric-inevitability}).
  2602	\item \emph{Universality}: $(Z_{\mathsf{SC}}(A), A)$ is
  2603	 terminal among $\mathsf{SC}$-pairs with fixed open
  2604	 component (Theorem~\ref{thm:center-terminality}).
  2605	\end{enumerate}
  2606	In the topological setting, these four assertions are respectively:
  2607	existence of the Hochschild complex, the Deligne conjecture,
 succeeded in 52ms:
  1412	\begin{construction}[Promotion functor: from chiral algebra to
  1413	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra]
  1414	\label{constr:promotion-functor}
  1415	\index{promotion functor|textbf}
  1416	\index{Swiss-cheese operad!promotion from chiral algebra}
  1417	A chiral algebra~$\cA$ is one-coloured (an algebra over the
  1418	closed colour of~$\mathsf{SC}^{\mathrm{ch,top}}$). The operadic
  1419	bar relative to the full two-coloured operad requires a
  1420	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra
  1421	$(\cA_{\mathrm{cl}},\, \cA_{\mathrm{op}})$ as input
  1422	(a closed-colour algebra and an open-colour algebra with
  1423	mixed operations). The \emph{promotion functor}
  1424	$\cA \mapsto (\cA, \cA)$ uses self-action: every
  1425	commutative algebra acts on itself as a module, supplying
  1426	the open-colour and mixed data canonically. The operadic bar
  1427	$B_{\mathsf{SC}}(\cA, \cA)$ decomposes:
  1428	\begin{itemize}
  1429	\item Closed sector: $B_{\operatorname{Com}}(\cA)
  1430	 = \operatorname{Lie}^c \circ s^{-1}\bar{\cA}$ (Harrison).
  1431	\item Open sector: $B_{\operatorname{Ass}}(\cA)
exec
/bin/zsh -lc "rg -n -F '\\label{rem:center-scope-e-inf}' chapters/theory/en_koszul_duality.tex && rg -n -F '\\label{thm:center-geometric-inevitability}' chapters/theory/en_koszul_duality.tex && rg -n -F '\\label{thm:center-terminality}' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
2053:\label{rem:center-scope-e-inf}
2144:\label{thm:center-geometric-inevitability}
2462:\label{thm:center-terminality}
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2134,2190p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2134	\index{recognition theorem!and the center}
  2135	
  2136	The geometric content of the chiral center theorem becomes
  2137	transparent once the recognition theorem (proved in Volume~II) is
  2138	invoked. The argument below shows that the theorem is
  2139	\emph{forced} by the geometry of the half-space
  2140	$\bC \times \bR_{\geq 0}$.
  2141	
  2142	\begin{theorem}[Geometric inevitability of the chiral center;
  2143	\ClaimStatusProvedHere]
  2144	\label{thm:center-geometric-inevitability}
  2145	\index{center theorem!geometric inevitability|textbf}
  2146	Let $\cA$ be a chiral algebra on a curve~$X$, and let
  2147	$\cF_\cA$ denote the corresponding prefactorization algebra on
  2148	$X \times \bR$ obtained from the
  2149	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra structure
  2150	\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
  2151	Under the recognition theorem identifying
  2152	$\mathsf{SC}^{\mathrm{ch,top}}$-algebras with prefactorization
  2153	algebras on $D \times \bR$




thinking
**Evaluating theorem recognition**

I'm considering the theorem's status; it's proved under the recognition theorem from Volume II. Since this theorem's implications relate to a status violation if the recognition theorem isn't proved, I must reflect on that. The user's focus is the foundation audit related to the en_koszul_duality.tex and its topologization lane, but since the theorem's integrity relies on the recognition theorem and thm:bar-swiss-cheese, it’s critical. I should suggest downgrading the theorem and adjusting its conditions appropriately.
thinking
**Analyzing theorem dependencies**

I’m looking at theorem 2142, which claims the "Geometric inevitability of chiral center; ProvedHere," but it's dependent on the recognition theorem from Volume II, specifically items F4-F5. A code review would definitely flag this. The topologization theorem seems to rely on this too. The user wants to identify every possible issue, and this qualifies. I might need to check if theorem 2174 misuses thm:bar-swiss-cheese, which seems likely, but the core concern is the unproved recognition theorem.
thinking
**Investigating notation and terminology**

I think I need to check if "five presentations of SC" means something different than I initially thought. I should also explore the introduction about Swiss-cheese primacy to see if there's a connection to "seven faces," though it's not mandatory. There’s a potential issue with def 1674 regarding "terminal object in category of O-algebra pairs," since it uses inverse limit notation, which isn't standard and doesn’t always exist. However, prop 1741 confirms its existence, so I might be able to overlook it.
thinking
**Identifying algebra issues**

I'm noticing a potential issue in line 3070, talking about algebras without a conformal vector. It seems like for Heisenberg at k=0, there's a degenerate situation. I need to be careful about mathematical judgments based on the file content. Also, there's a note about Virasoro and W-algebras that suggests the importance of chain-level data and that the E3 upgrade may only exist on Q-cohomology. Additionally, there are concerns in the Chern-Simons construction about omitted components.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '4476,4520p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4476	% ----------------------------------------------------------------
  4477	\subsection{The filtered $\Ethree$-chiral algebra}
  4478	\label{subsec:filtered-e3-chiral}
  4479	
  4480	The chiral $\Pthree$ bracket and the chiral
  4481	Chevalley--Eilenberg complex assemble into a single object:
  4482	a filtered $\Ethree$-chiral algebra
  4483	$\CE^{\mathrm{ch}}_k(\fg)$, a factorisation $\cD$-module
  4484	on $\Ran(X)$ whose global sections on the formal disk
  4485	recover the CFG $\Ethree$-algebra.
  4486	
  4487	\begin{definition}[The filtered $\Ethree$-chiral algebra]
  4488	\label{def:filtered-e3-chiral}
  4489	The \emph{chiral $\Ethree$-algebra}
  4490	\begin{equation}\label{eq:chiral-e3-algebra}
  4491	  \CE^{\mathrm{ch}}_k(\fg)
  4492	  \;:=\;
  4493	  \bigl(\CE^{\mathrm{ch}}(\fg_k),\;
  4494	  \{-,-\}^{\mathrm{ch}},\;
  4495	  \cD\textrm{-module structure}\bigr)

thinking
**Verifying claims in the file**

I'm considering how to ensure my claims are solidly grounded in the file content as the user requested. The smart move is to focus on the actual content I’ve read. I might want to avoid mentioning any specific commands like "rg" and just state that "the section never lists them." Also, it’s worth checking if there’s a definition for “conformal vector” earlier in the same file — that could help clarify things too!
exec
/bin/zsh -lc "rg -n -F '\\begin{definition}[Conformal vector' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex && rg -n 'conformal vector' chapters/theory/en_koszul_duality.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "rg -n 'conformal vector' chapters/theory/en_koszul_duality.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\begin{definition}[Conformal vector' chapters/theory/en_koszul_duality.tex chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'BRST-type differential|bulk observables|holomorphic--topological theory' chapters/theory/en_koszul_duality.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
26:conformal vector.
1273:\item With an inner conformal vector at non-critical level,
1277:\item Without a conformal vector,
2921:\index{E3 algebra@$\Ethree$-algebra!from Swiss-cheese + conformal vector}
2946:\begin{definition}[Inner conformal vector]
2948:\index{conformal vector!inner}
2953:is~$\cA$. An \emph{inner conformal vector} for
2954:$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
2963:provides the inner conformal vector. For the
2976:provides an inner conformal vector
2990:Here the inner conformal vector makes holomorphic
3004:The inner conformal vector identifies
3036:conformal vector hypothesis.
3051:\begin{remark}[The conformal vector is necessary, not
3054:\index{conformal vector!necessity for $\Ethree$}
3055:Without a conformal vector, an
3062:$\Eone$-chiral and $\Ethree$; the conformal vector is
3076:an explicit inner conformal vector and the $3$d
3082:For general chiral algebras with conformal vector, the
3096:the conformal vector. Topologization is expected at generic
 exited 1 in 51ms:

 succeeded in 53ms:
1267:The derived center is the algebra of bulk observables of
2157:\item \emph{Closed color $=$ bulk observables.} The closed-sector
2167:\item \emph{Center $=$ interior bulk observables.} The
2599: interior bulk observables in the half-space
2950:BRST-type differential on the algebra of observables
2951:of a holomorphic--topological theory~$T$ on
2956:of bulk observables up to a $Q$-boundary: there exists
3077:holomorphic--topological theory is Chern--Simons.
3086:stress tensor $T(z)$. The holomorphic--topological theory

thinking
**Investigating definitions**

I'm looking for the conformal vector definition, which I can't find in the chapter. It seems like a hidden import might be a good lead. I should check if `thm:operadic-center-hochschild` references `Definition ref def:chiral-hochschild`, but I noticed that `def:chiral-hochschild` is located in `hochschild_cohomology.tex`. It might be worthwhile to run a search for "topologization" definitions to gather more information. Let's see where that leads!
exec
/bin/zsh -lc "rg -n '\\\\begin\\{definition\\}\\[.*topolog' chapters/theory/en_koszul_duality.tex chapters/theory/*.tex chapters/examples/*.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/en_koszul_duality.tex:1220:\begin{definition}[Holomorphic--topological Swiss-cheese operad]
chapters/theory/bar_cobar_adjunction_curved.tex:286:\begin{definition}[I-adic topology]
chapters/theory/en_koszul_duality.tex:1220:\begin{definition}[Holomorphic--topological Swiss-cheese operad]

thinking
**Searching for definitions**

I need to find the definition of "conformal vector" since it seems like it isn't available in the target file. The user is asking about this specific file, so I should note that the definition might exist elsewhere in the repository but isn't directly cited.

I could mention the absence of a definition in the target file and lack of cross-references. To find it, I’ll do a search in the repository. Let me check with a broader query as well.
exec
/bin/zsh -lc "rg -n 'definition\\]\\[.*conformal vector|\\\\label\\{def:.*conformal' chapters appendices standalone bibliography" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/beta_gamma.tex:1325:\label{def:conformal-weight-filtration}
chapters/theory/en_koszul_duality.tex:2947:\label{def:inner-conformal-vector}
chapters/theory/chiral_modules.tex:518:\label{def:conformal-blocks}
chapters/theory/chiral_modules.tex:767:\label{def:bundle-conformal-blocks}

thinking
**Searching for definitions**

I’m trying to find a general conformal vector definition, but I’m not seeing any. It seems like I couldn't locate a "def:" label in the repository. My search was good, though! I’m also considering whether I should look for a definition of "BRST-type differential," but that might not be necessary. It’s okay to think through these options carefully! Searching again might help clarify what I need.
exec
/bin/zsh -lc "rg -n 'BRST-type differential|\\bBRST\\b.*definition|\\\\label\\{def:.*BRST' chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:1760:where each arrow represents a BRST-type differential that shifts ghost number and conformal weight.
chapters/examples/y_algebras.tex:242: formula uses the full BRST definition: from
chapters/examples/y_algebras.tex:447:The BRST definition~\eqref{eq:y-brst-definition} realizes
chapters/theory/chiral_modules.tex:4373:$n$-th products by the BRST definition), the two differentials
chapters/theory/en_koszul_duality.tex:2950:BRST-type differential on the algebra of observables

thinking
**Considering search options**

I realize I don't have a formal definition on hand. Maybe I should search for the local constancy criterion or the notation `\partial_{\bar z}` from the theorem. Hm, searching might not be necessary, but it seems like it could clarify things. I think checking those options could help clarify my understanding of the concepts involved here, so perhaps I'll proceed that way if needed.
exec
/bin/zsh -lc "rg -n '\\\\partial_\\{\\\\bar z\\}|\\\\partial_\\\\bar z|\\\\bar\\\\partial|local constancy of the factorization algebra' chapters/theory/en_koszul_duality.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
3040:that converts local constancy of the factorization algebra
3178:  \textup{(}local constancy of the factorization algebra\textup{)} is proved on








thinking
**Evaluating proposition clarity**

I’m considering whether there’s an issue with proposition 5211 regarding the central charge line 5224: the equation \(c = k \dim(g)/(k+h^\vee)\) seems correct. I need to look closer at the section regarding the chiral center theorem and the chiral Hochschild cochain complex as the operadic center. Later, there's a restriction to E∞-chiral. I'll check if line 5430 retains the correct summary of theorem 1293 and if there’s any misstatement around line 31 in the introduction.
thinking
**Considering build options**

I’m thinking about whether I should perform a build or check for unresolved references. I could search for specific labels in audited findings, but that might not be essential. Running the command `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` is an option, but it might be too resource-intensive. I wonder if it's worth searching previous logs since the user didn’t ask for it, yet it could help verify unresolved references in our project. But if the build takes too long, maybe I should go with a more targeted approach.
thinking
**Reviewing audit findings**

I’m considering whether we need to compile since we already have strong findings without it. It might be enough as is. I wonder if I should update the plan, but it could be unnecessary. The developer mentioned that after providing sufficient context, a longer plan might be useful. We’ve been giving short updates, so maybe that’s fine. I need to re-verify findings against the actual files and gather specific lines, like 2053 and 1796, for citation purposes. I'll check for a "topologization" definition too.
thinking
**Checking for presentations**

I need to search for "five presentations" in the file, but it looks like there are no hits. I ran the command `rg -n -F "five presentations" chapters/theory/en_koszul_duality.tex`, and got exit 1 with no output, which seems conclusive. So, I can mention that the file never enumerates those presentations based on my reading. Now, I think I should search for "presentation of SC" as well, since that might also be absent.
thinking
**Revising verdict criteria**

I see that the verdict has failed. I should focus on keeping line references precise and maybe include secondary lines related to the problem. Formatting it into bullets could help. I'll ensure to use severity labels from the contract: CRITICAL, HIGH, MEDIUM, and LOW. Maybe I should aim for around 10 bullets to get clear points across. I want to keep it minimal but with enough detail. It's important to mention exact fixes too!
thinking
**Considering theorem details**

I notice there's a hidden dependency that’s revealing itself. That’s good! I should probably mention that line 1796's theorem statement is missing the E∞ hypothesis, referring to it as a "subtle second-order." Also, it might be valuable to link the 1417 promotion overclaim with the 1796 theorem statement together in one spot labeled [HIGH]. This connection could add clarity, don’t you think? I'm just trying to ensure everything is covered.
thinking
**Organizing findings for report**

I need to keep my report concise, aiming for about 50-70 lines total. The user expects detailed findings and solutions, so I might stretch to about 10 bullets with a summary. Each bullet can be quite detailed, as long as I maintain clarity. I should note the checks as “Checked: 8” since I audited 8 target surfaces plus 7 dependencies. I'll format the findings appropriately, starting directly with the bullets and ending with the summary.
thinking
**Drafting final report format**

I need to mention file paths in the report without making them clickable, even though the final instructions prefer clickable markdown links for local files. While I could construct clickable links with line numbers, I'll stick to the requested format, using the structure `file:line` as plain text, like `chapters/theory/en_koszul_duality.tex:5432`. It’s important to ensure each problem reflects the content of the file I’ve read. I should state facts clearly, like “the file never lists them.” I’ll aim for 10 findings and summarize with “Checked: 8 | Findings: 10 | Verdict: FAIL.”
codex
- [CRITICAL] chapters/theory/en_koszul_duality.tex:5432 — PROBLEM: The chapter summary resurrects the exact false claim the file already retracts: it says `\barB^{\mathrm{ord}}(\cA)` is a dg coalgebra over `\mathsf{SC}^{\mathrm{ch,top}}`, with the differential as the closed color and deconcatenation as the open color. That contradicts the corrected principle at lines 1247-1291 and Theorem `thm:bar-e1-coalgebra` at lines 1293-1353, which say the bar complex is single-colored `\Eone`-chiral and not Swiss-cheese. FIX: Replace lines 5430-5444 by: “`\barB^{\mathrm{ord}}(\cA)=T^c(s^{-1}\bar\cA)` is a single-colored `\Eone`-chiral coassociative dg coalgebra over `(\operatorname{Ass}^{\mathrm{ch}})^!`; the `\mathsf{SC}^{\mathrm{ch,top}}` structure appears only on the derived-center pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)`, not on the bar complex itself.`”

- [CRITICAL] chapters/theory/en_koszul_duality.tex:2142 — PROBLEM: `thm:center-geometric-inevitability` is tagged `\ClaimStatusProvedHere`, but its statement is explicitly conditional on the recognition theorem from Volume II at lines 2151-2154, and it also falsely says the needed `\mathsf{SC}^{\mathrm{ch,top}}` structure comes from `thm:bar-swiss-cheese` at lines 2148-2150 even though that theorem now says the bar complex is not Swiss-cheese. FIX: Downgrade this environment to `\begin{remark}[Conditional geometric realization]` or `\begin{proposition}...\ClaimStatusConditional`, rewrite the input as the pair `(C^\bullet_{\mathrm{ch}}(\cA,\cA),\cA)` from `thm:operadic-center-hochschild`, and state the Volume II recognition theorem as an explicit hypothesis.

- [CRITICAL] chapters/theory/en_koszul_duality.tex:2985 — PROBLEM: `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))` is used without any defined BRST differential on `Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)`. The only `Q` introduced in the section is attached to bulk observables of a 3d HT theory in Definition 2949-2957, while lines 2271-2299 say the identification of the derived center with that bulk theory is expected, not proved here. As written, the theorem’s object is undefined. FIX: Either restate Theorem `thm:topologization` on `H_Q^\bullet(\Obs_{\mathrm{bulk}}(T_{\mathrm{CS}}))`, or insert a proved proposition before line 2967 giving a quasi-isomorphism `Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)) \simeq \Obs_{\mathrm{bulk}}(T_{\mathrm{CS}})` and define `Q` by transport across that map; if neither is added, downgrade the theorem to conditional.

- [HIGH] chapters/theory/en_koszul_duality.tex:1223 — PROBLEM: Definition `def:SC` is not a full operad definition. It gives slogan-level arity spaces, but no `\Sigma_k\times\Sigma_m` actions, no unit conventions, no explicit pure-open arities, no separate closed/open/mixed insertion maps, and no codimension-1 boundary relations. The user asked whether `\mathsf{SC}^{\mathrm{ch,top}}` is properly defined by generators/relations; in this file it is not. FIX: Expand Definition `def:SC` to specify all arities for `k,m\ge0`, units `\FM_1(\C)=E_1(1)=\mathrm{pt}` and the `k=0` convention, the symmetric-group actions, and the three compositions; then add a proposition immediately after it recording the codimension-1 boundary/generators-and-relations presentation used later.

- [HIGH] chapters/theory/en_koszul_duality.tex:2918 — PROBLEM: “Topologization” is never formally defined before it is used as a theorem and conjecture label. The file never states whether topologization means a chain-level `\Ethree` structure, a cohomological `\Ethree` structure, or collapse of the two-color SC datum to one color. FIX: Insert `\begin{definition}[Cohomological topologization / chain-level topologization]` before Definition `def:inner-conformal-vector`, define both notions explicitly, and then state Theorem `thm:topologization` as the cohomological case and Conjecture `conj:topologization-general` as the chain-level lift.

- [HIGH] chapters/theory/en_koszul_duality.tex:2946 — PROBLEM: Definition `def:inner-conformal-vector` hides essential undefined inputs: “conformal vector,” “BRST-type differential,” “bulk observables,” and the boundary-to-bulk comparison map are not defined in the chapter. The last sentence is also misleading: “For the Virasoro algebra, `T(z)` is the stress tensor itself” gives an example of a conformal vector, not of an inner conformal vector, and later lines 3085-3093 say Virasoro innerness is conjectural. FIX: Split this into two definitions: first define a conformal vector in the boundary chiral algebra; then define innerness relative to a specified bulk complex `(\Obs_{\mathrm{bulk}}(T),Q)` and boundary map `\iota:\cA\to\Obs_{\mathrm{bulk}}(T)`. Replace the Virasoro sentence by: “For Virasoro, `T(z)` is the boundary conformal vector; whether it is inner is conjectural and depends on the 3d gravity BRST complex.”

- [HIGH] chapters/theory/en_koszul_duality.tex:2990 — PROBLEM: The proof jumps from `\partial_z=[Q,[G,-]]` to “the factorization algebra on `\C` becomes locally constant” and then invokes Lurie. No argument is given that both real translation generators become `Q`-exact, and no local-constancy criterion is cited or proved. This is the load-bearing step. FIX: Insert a lemma between lines 3009 and 3016 proving that `\partial_x` and `\partial_y` are `Q`-exact on BRST cohomology (using the holomorphic/Dolbeault direction plus Sugawara), then cite the precise recognition theorem for locally constant factorization algebras before concluding `\Etwo^{\mathrm{top}}`.

- [HIGH] chapters/theory/en_koszul_duality.tex:3204 — PROBLEM: Construction `constr:sugawara-antighost` claims to “verify” `[Q,G]=T_{\mathrm{Sug}}`, but the two correction terms are waved away as “Q-exact up to equations of motion” at lines 3308-3312 and 3318-3323 with no explicit homotopy and no cited BV lemma. That is not a verification. FIX: Either add the missing BV computation by exhibiting an operator `H(z)` with `[Q,H(z)]` equal to the correction terms modulo the BV differential/EOM ideal, or demote the construction to a heuristic remark and cite a precise external proof.

- [HIGH] chapters/theory/en_koszul_duality.tex:1417 — PROBLEM: Construction `constr:promotion-functor` overclaims. It says every chiral algebra canonically promotes to an `\mathsf{SC}^{\mathrm{ch,top}}`-algebra via self-action because every commutative algebra acts on itself as a module, but Remark `rem:center-scope-e-inf` at lines 2055-2069 later says the center theorem only works for logarithmic `E_\infty`-chiral input and fails for genuine `E_1`-chiral input. FIX: Rewrite the construction to start with “For logarithmic `E_\infty`-chiral input…” and add the sentence “For genuine `E_1`-chiral input there is no canonical promotion; the correct replacement is the ordered Hochschild complex.”

- [HIGH] chapters/theory/en_koszul_duality.tex:1796 — PROBLEM: Theorem `thm:operadic-center-hochschild` omits its real hypotheses. The statement says only “logarithmic chiral algebra,” but line 2055 later says it requires `E_\infty`-chiral input; the statement also treats the closed sector as the space-valued operad `\{\FM_k(\C)\}`, while the proof uses the dg model `\Omega^*(\FM_k(\C),\log D)` at lines 1883-1890. FIX: Change the theorem statement to: “Let `\cA` be a logarithmic `E_\infty`-chiral algebra equipped with an action of the dg operad `\Omega^\bullet(\FM_\bullet(\C),\log D)`, and let `A` be the open-color algebra in its promoted `\mathsf{SC}^{\mathrm{ch,top}}`-pair.” Then keep the identification only under those hypotheses.

- [MEDIUM] chapters/theory/en_koszul_duality.tex:1196 — PROBLEM: The chapter never actually lists the five presentations of `\mathsf{SC}^{\mathrm{ch,top}}`. In the Swiss-cheese lane I read one space-level definition, one abstract vanishing-operad reformulation, one Koszul-dual description, one Boardman–Vogt mention, and one imported local-pair model, but no explicit “five presentations” proposition or roadmap. FIX: Add a proposition immediately after Definition `def:SC` enumerating the five presentations with labels and cross-references: configuration-space operad, abstract two-colored operad with vanishing open-to-closed operations, local chiral Swiss-cheese pair, Koszul-dual three-sector cooperad, and Boardman–Vogt/HT prefactorization presentation.

- [MEDIUM] chapters/theory/en_koszul_duality.tex:2588 — PROBLEM: The “four assertions” summary silently changes scope. Item (1) is for every `E_1`-algebra `A`, while item (2) uses the chiral identification theorem that only applies to logarithmic `E_\infty`-chiral lifts `\cA`. As written, the paragraph reads as if one theorem handles both settings uniformly. FIX: Rewrite items (1)-(2) to separate the scopes: “For every `E_1` open algebra `A`, `Z_{\mathsf{SC}}(A)` exists. If `A` arises from a logarithmic `E_\infty`-chiral algebra `\cA`, then `Z_{\mathsf{SC}}(A)\simeq C^\bullet_{\mathrm{ch}}(\cA,\cA)`.”

- [MEDIUM] chapters/theory/en_koszul_duality.tex:5203 — PROBLEM: The subsection still uses the forbidden terminology “chiral `\Ethree`-algebra,” even though Theorem `thm:topologization` only proves a cohomological `\Ethree^{\mathrm{top}}` structure on BRST cohomology. This reintroduces the `SC^{\mathrm{ch,top}}\neq E_3` conflation the constitution explicitly warns against. FIX: Rename the subsection and its local terminology to “cohomological `\Ethree^{\mathrm{top}}` enhancement,” and replace each occurrence of “chiral `\Ethree`-algebra” in this subsection by either “holomorphic `\Etwo^{\mathrm{hol}}\otimes\Eone^{\mathrm{top}}` structure” before enhancement or “cohomological `\Ethree^{\mathrm{top}}` structure” after enhancement.

## Summary
Checked: 8 | Findings: 12 | Verdict: FAIL
tokens used
177,315
