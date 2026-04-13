# D03_slop_v1_connections (660s)

**Findings**
- `PROBLEM at chapters/connections/feynman_connection.tex:6`: rhetorical escalation. `EXACT edit applied`: `The similarity is striking enough to demand an answer` -> `The similarity raises a precise question`.
- `PROBLEM at chapters/connections/genus_complete.tex:261,750-751`: inflated prose (`categorically richer`, `natural holographic interpretation`). `EXACT edit applied`: `categorically richer object` -> `chain-level modular functor`; `carries a natural holographic interpretation` -> `admits a holographic interpretation`.
- `PROBLEM at chapters/connections/genus1_seven_faces.tex:642,1136`: loaded phrasing (`deeper identification`, `fundamentally genus-1`). `EXACT edit applied`: `deeper identification` -> `corresponding genus-$g \geq 2$ identification`; `fundamentally genus-$1$ phenomenon` -> `genus-$1$ phenomenon`.
- `PROBLEM at chapters/connections/semistrict_modular_higher_spin_w3.tex:8,10,31,69`: forbidden `---` comment separators and inflated chapter-opening prose. `EXACT edit applied`: `% ----------------------------------------------------------------------` -> `% ======================================================================` at lines 8 and 10; `nearest route`/`natural targets`/`recognizably gravitational` sentence -> a neutral `first route`/`target settings` formulation at line 31; `correct first test` -> `first one handled here because it admits proofs` at line 69.
- `PROBLEM at chapters/connections/holographic_datum_master.tex:24,1181`: promotional `centrepiece` language. `EXACT edit applied`: `the centrepiece of Part...` -> `the main theorem of Part...`; `The seven-face programme is the centrepiece...` -> `The seven-face programme is a core result...`.
- `PROBLEM at chapters/connections/arithmetic_shadows.tex:1228,1687,3718,3750,4164,4283,11033,11036,11039,11045,11048,11057,12667`: repeated style inflation and `---` placeholders. `EXACT edit applied`: `deepest arithmetic content` -> `arithmetic content at degree~$4$`; `A natural refinement` -> `A refinement`; `fundamentally different object` -> `separate object`; `deeper point` -> `structural point`; `deepest` -> `strongest`; `natural interpretation` -> `interpretation`; each table cell `& --- \\` -> `& n/a \\`; `deepest structural obstruction` -> `main structural obstruction`.
- `PROBLEM at chapters/connections/concordance.tex:335,971,3415,5910,6373,7656,8230,9319,10350`: rhetorical and inflated wording. `EXACT edit applied`: `categorically richer` -> `a chain-level categorical invariant`; `same mechanism organizes the nonlinear chiral landscape` -> `same construction for nonlinear chiral families`; `first natural audit surface` -> `initial audit surface`; `A natural first guess` -> `A first guess`; `richer geometric settings` -> `broader geometric settings`; `single deepest problem` -> `main unresolved problem`; `deepest open problem` -> `a major open problem`; `deepest layer` -> `last layer`; `strictly richer than the closed-sector classes` -> `contain more data than the closed-sector classes`.
- `PROBLEM at chapters/connections/outlook.tex:2,573,646`: em-dash comments and inflated comparison. `EXACT edit applied`: `OUTLOOK —` -> `OUTLOOK:`; `tower is richer than the KdV hierarchy` -> `tower extends beyond the KdV hierarchy`; `Additional stub labels —` -> `Additional stub labels:`.
- `PROBLEM at chapters/connections/editorial_constitution.tex:829,2691`: `---` table placeholder and inflated comparison. `EXACT edit applied`: `Ind. & --- &` -> `Ind. & n/a &`; `configuration-space topology on curves is richer than...` -> `has more structure than...`.
- `PROBLEM at chapters/connections/poincare_computations.tex:107`: inflated comparison (`deeper phenomenon`). `EXACT edit applied`: `a deeper phenomenon than NAP duality` -> `a different phenomenon from NAP duality`.
- `PROBLEM at chapters/connections/frontier_modular_holography_platonic.tex:1177,1204,2660`: inflated packaging language. `EXACT edit applied`: `same mechanism unifies` -> `same construction applies to`; `organizes a genuine bulk/boundary system` -> `defines a bulk/boundary system`; `strictly richer than for Virasoro` -> `carries more data than in the Virasoro case`.
- `PROBLEM at chapters/connections/thqg_entanglement_programme.tex:6,9,16-18`: comment-surface em-dashes. `EXACT edit applied`: replaced `—` with `;` or `:` in the audit notes and status legend.
- `PROBLEM at chapters/connections/entanglement_modular_koszul.tex:19,21`: forbidden `---` comment separators. `EXACT edit applied`: each `% ----------------------------------------------------------------------` -> `% ======================================================================`.
- `PROBLEM at chapters/connections/thqg_open_closed_realization.tex:40,44,357,361,519,523,625,630,944,948,1033,1037,1213,1218,1379,1383,1529,1533`: forbidden `---` comment separators. `EXACT edit applied`: each `% -------------------------------------------------------------------` -> `% ===================================================================`.

**Verification**
`rg` sweeps for the zero-tolerance slop list and for literal `---|—` now come back clean across `chapters/connections/*.tex`. The only remaining `deeper` hit is `chapters/connections/frontier_modular_holography_platonic.tex:1906`, where it refers to actual geometric strata, so I left it. I did not run a TeX build; verification here was grep-based because the edits were prose/comment-local.


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
session id: 019d87a8-b75a-72c0-96b7-63062d65402d
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


Same slop removal for chapters/connections/*.tex.
mcp startup: no servers
codex
I’m treating this as an adversarial wording audit on `chapters/connections/*.tex`, with fixes applied immediately and kept minimal. First I’m loading the repo’s required constitutional surface and the audit skill, then I’ll scan the connection chapters for banned prose/slop patterns and repair only those files.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files chapters/connections -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/Users/raeez/chiral-bar-cobar
chapters/connections/thqg_open_closed_realization.tex
chapters/connections/editorial_constitution.tex
chapters/connections/feynman_connection.tex
chapters/connections/genus_complete.tex
chapters/connections/subregular_hook_frontier.tex
chapters/connections/genus1_seven_faces.tex
chapters/connections/thqg_introduction_supplement_body.tex
chapters/connections/holographic_datum_master.tex
chapters/connections/frontier_modular_holography_platonic.tex
chapters/connections/entanglement_modular_koszul.tex
chapters/connections/semistrict_modular_higher_spin_w3.tex
chapters/connections/master_concordance.tex
chapters/connections/bv_brst.tex
chapters/connections/thqg_introduction_supplement.tex
chapters/connections/poincare_computations.tex
chapters/connections/feynman_diagrams.tex
chapters/connections/concordance.tex
chapters/connections/holographic_codes_koszul.tex
chapters/connections/thqg_entanglement_programme.tex
 succeeded in 51ms:
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

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
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
**Inspecting files for slop removal**

I need to check the target files for slop, as the user mentioned applying slop removal for the specified `.tex` files in the `chapters/connections/` directory. 

I might run a case-insensitive search using `rg` to find and remove banned prose tokens. It’s essential to minutely inspect the context to ensure minimal edits without changing math. I’ll produce findings that detail each edit with the corresponding file and line number while keeping an exhaustive approach within scope. Let’s plan to use `rg -n -i` for the scan.
thinking
**Searching for banned tokens**

I’m planning to search for common banned tokens from sources like CLAUDE/AGENTS, which include words and phrases like "moreover," "notably," "it should be noted," and others. I also want to include metaphors, like "landscape" and "journey." 

I’ll check if there are many instances that need addressing. Automating this with a script could be useful. Using `rg` to gather all the hits seems like a solid plan. Let’s go ahead with the search!
codex
I’ve loaded the required repo surface and the audit workflow. Next I’m running a directory-wide grep for the banned prose patterns and em-dashes in `chapters/connections/*.tex`, then I’ll inspect each hit in context before editing.
exec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|arguably|perhaps|seems to|appears to)'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/connections/*.tex' '---|—'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/connections/*.tex' '\\\\label\\{|\\\\ClaimStatus|\\\\begin\\{(theorem|proposition|lemma|conjecture|remark|definition|corollary)\\}' chapters/connections | wc -l" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 2 in 50ms:
rg: unrecognized flag ---|—
 succeeded in 51ms:
    3358
codex
The first banned-token sweep came back clean for the standard zero-tolerance list, so I’m widening the scan to the remaining prose offenders: em-dashes and metaphorical stock terms like `landscape` and `navigate`, then I’ll read each hit in place before deciding whether it needs surgery.
exec
/bin/zsh -lc "rg -n --glob 'chapters/connections/*.tex' -- '---|—' chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(landscape|navigate|rich|deep|beautiful|powerful|fundamental|natural|elegant|striking|intricate|interplay|web of|unpack|underscores|showcases|paradigm|key idea|in many ways|in this sense)' chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_open_closed_realization.tex:40:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:44:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:357:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:361:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:519:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:523:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:625:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:630:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:944:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:948:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1033:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1037:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1213:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1218:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1379:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1383:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1529:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1533:% -------------------------------------------------------------------
chapters/connections/editorial_constitution.tex:829:Ind. & --- & ${\sim}8$ independent problems
chapters/connections/entanglement_modular_koszul.tex:19:% ----------------------------------------------------------------------
 succeeded in 51ms:
Total output lines: 449

chapters/connections/thqg_open_closed_realization.tex:807:naturally identified with the \emph{cyclic bar complex}
chapters/connections/editorial_constitution.tex:160:core. The all-types categorical prefundamental
chapters/connections/editorial_constitution.tex:165:proves shifted-prefundamental generation and pro-Weyl recovery
chapters/connections/editorial_constitution.tex:166:\textup{(}Theorems~\ref{thm:shifted-prefundamental-generation},
chapters/connections/editorial_constitution.tex:211:hypotheses~\textup{(a)--(c)}, the enrichment-killing is unconditional
chapters/connections/editorial_constitution.tex:256:ordinary-derived/completed/coderived enlargement carrying the natural
chapters/connections/editorial_constitution.tex:283:prefundamental Clebsch--Gordan $V_n \otimes L^- \cong
chapters/connections/editorial_constitution.tex:466:the entire standard landscape (universal algebras; for simple
chapters/connections/editorial_constitution.tex:488:hypothesis~(c), the enrichment-killing is unconditional.
chapters/connections/editorial_constitution.tex:515:prefundamental Clebsch--Gordan closure and evaluation-generated-core
chapters/connections/editorial_constitution.tex:519:shifted-prefundamental and pro-Weyl packets. The residual DK-4/5
chapters/connections/editorial_constitution.tex:557:(quintuple $\to$ effective $\Gamma$-quadruple, proved for standard landscape);
chapters/connections/editorial_constitution.tex:596: Corollary~\ref{thm:yangian-typea-realization-plus-fundamental-packet};
chapters/connections/editorial_constitution.tex:644:Corollary~\ref{thm:yangian-typea-realization-plus-fundamental-packet}
chapters/connections/editorial_constitution.tex:810: & All-types prefundamental CG and evaluation-generated-core DK.
chapters/connections/editorial_constitution.tex:811: Type-$A$ shifted-prefundamental generation and pro-Weyl recovery.
chapters/connections/editorial_constitution.tex:853:Type~$A$ proves shifted-prefundamental generation and
chapters/connections/editorial_constitution.tex:857:(1)~prefundamental Clebsch--Gordan closure


thinking
**Analyzing language use**

I'm considering how to remove loaded adjectives and adverbs that aren't mathematical. For example, phrases like "similarity is striking enough to demand an answer" seem rhetorical, while "the entire standard landscape" might be more straightforward and actually a classification. I need to identify which terms might add excess embellishment or bias without losing the meaning. The user requested to apply this "slop removal" approach across several files, so I'll need to review the current working tree and past edits for patterns.
thinking
**Planning rhetorical evaluation**

I need to create a plan to tackle removing rhetorical slop from my text. First, I'll scan for all zero-tolerance tokens, which appear to be none at the moment. Then, I’ll identify additional terms that may be overly rhetorical, like "landscape," "centerpiece," "deepest," "richer," "striking," and "natural." However, it seems "landscape" is an actual concept in the repo, and "natural" has a technical meaning, so I need to be cautious about which terms I decide to remove.
codex
The zero-tolerance list is almost clean already; what remains is mostly harder rhetorical stock language rather than the canned tokens. I’m isolating those stronger phrases now so I can patch only sentences that are actually carrying style inflation rather than technical meaning.
exec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(robust|beautiful|compelling|remarkable|interesting|elegant|intricate|rich|powerful|essentially|obviously|clearly|of course|central|cornerstone|showcase|showcases)' chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(striking|deeper|deepest|richer|centrepiece|centerpiece|correct first test|nearest route|demand an answer|first natural|precisely because|full spectrum|natural holographic|natural interpretation|natural refinement|natural first guess|fundamentally|same mechanism|organizes|survive intact)' chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/connections/editorial_constitution.tex:929:degeneration formula organizes their compatibility. The Costello
chapters/connections/editorial_constitution.tex:2691:multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
chapters/connections/editorial_constitution.tex:2695:(Remark~\ref{rem:characteristic-hierarchy}) organizes the
chapters/connections/feynman_connection.tex:6:The similarity is striking enough to demand an answer: is the bar
chapters/connections/genus_complete.tex:261:\emph{first Chern class} of a categorically richer object.
chapters/connections/genus_complete.tex:751:natural holographic interpretation: the bulk algebra is recovered as
chapters/connections/bv_brst.tex:2158:isomorphism precisely because its cone is coacyclic.
chapters/connections/outlook.tex:165: degeneration organizes these across genera).
chapters/connections/outlook.tex:222:organizes the resulting data into a single six-fold datum
chapters/connections/outlook.tex:573:tower is richer than the KdV hierarchy
chapters/connections/genus1_seven_faces.tex:642:genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
chapters/connections/genus1_seven_faces.tex:1136:The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
chapters/connections/poincare_computations.tex:107:The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
chapters/connections/frontier_modular_holography_platonic.tex:1177: the same mechanism unifies twisted and celestial holography.
chapters/connections/frontier_modular_holography_platonic.tex:1204: that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
chapters/connections/frontier_modular_holography_platonic.tex:1905:obtained by projecting $\Theta_\cA$ to successively deeper strata of
chapters/connections/frontier_modular_holography_platonic.tex:2659:The spectral sequence for $\mathcal W_3$ is strictly richer
chapters/connections/semistrict_modular_higher_spin_w3.tex:31:The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
chapters/connections/semistrict_modular_higher_spin_w3.tex:69:The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
chapters/connections/holographic_datum_master.tex:24:theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
 succeeded in 52ms:
chapters/connections/editorial_constitution.tex:211:hypotheses~\textup{(a)--(c)}, the enrichment-killing is unconditional
chapters/connections/editorial_constitution.tex:488:hypothesis~(c), the enrichment-killing is unconditional.
chapters/connections/editorial_constitution.tex:1178:The first structured route between them is a finite-window Dirichlet Schr\"odinger operator with sextic potential.
chapters/connections/editorial_constitution.tex:1925:central charge}:
chapters/connections/editorial_constitution.tex:2691:multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
chapters/connections/genus_complete.tex:136:\item \emph{Central charge:} $c \in \mathbb{R}$ (any rational CFT extends to genus one; in critical string theory the matter central charge is $c_{\mathrm{matter}} = 26$ (bosonic) or $c_{\mathrm{matter}} = 15$ (superstring), chosen so that the total anomaly $c_{\mathrm{matter}} + c_{\mathrm{ghosts}} = 0$ cancels)
chapters/connections/genus_complete.tex:261:\emph{first Chern class} of a categorically richer object.
chapters/connections/genus_complete.tex:636:where $E_2(\tau) = 1 - 24\sum_{n=1}^\infty \frac{nq^n}{1-q^n}$ is the second Eisenstein series. At $\lambda = 1/2$, the central charge is $c_{\beta\gamma} = -1$ and the coefficient is $-1/24$.
chapters/connections/genus_complete.tex:884:(Definition~\ref{def:scalar-lane}) is determined by a single numerical invariant: the obstruction coefficient $\kappa(\mathcal{A})$, which depends on the genus-$1$ curvature alone. In practice, $\kappa(\cA)$ is computed from the central charge and the structure of the OPE: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$, $\kappa(\mathrm{Vir}_c) = c/2$, $\kappa(\mathcal{H}_k) = k$. On that lane, the scalar genus expansion $F_g(\mathcal{A}) = \kappa(\mathcal{A}) \cdot \lambda_g^{\mathrm{FP}}$ is given by Bernoulli numbers. For arbitrary modular Koszul algebras, only the genus-$1$ scalar term is unconditional. The separately proved spectral invariants, and the full Maurer--Cartan completion on the simple-Lie-symmetry locus of Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}, are \emph{not} determined by~$\kappa(\cA)$ alone; see Theorem~\ref{thm:spectral-characteristic} and Definition~\ref{def:full-modular-package}.
chapters/connections/genus_complete.tex:1049:distinguishes the Virasoro from other algebras at the same central
chapters/connections/genus_complete.tex:1460:positive-semidefinite inner product on Dirichlet polynomials
chapters/connections/genus_complete.tex:1785:\subsection{The Dirichlet--sewing lift}%
chapters/connections/genus_complete.tex:1787:\label{subsec:dirichlet-sewing-lift}%
chapters/connections/genus_complete.tex:1788:\index{Dirichlet--sewing lift|textbf}%
chapters/connections/genus_complete.tex:1813:\begin{definition}[Dirichlet--sewing lift]%
chapters/connections/genus_complete.tex:1814:\label{def:dirichlet-sewing-lift}%
chapters/connections/genus_complete.tex:1815:\index{Dirichlet--sewing lift|textbf}%
chapters/connections/genus_complete.tex:1816:\index{Dirichlet series!sewing}%
chapters/connections/genus_complete.tex:1817:The \emph{Dirichlet--sewing lift} of~$\cA$ is
chapters/connections/genus_complete.tex:1818:\begin{equation}\label{eq:dirichlet-sewing-lift}


thinking
**Evaluating language clarity**

I’m considering how to inspect contexts around selected matches. I might focus on obvious slop phrases, aiming for an efficient process. I could target explicit hyperbolic or metaphorical phrases and define selection criteria.

User mentioned "same slop removal" for certain files, wanting to remove those phrases similarly to previous tasks. I’ll need a broader list but not too broad — maybe searching for terms like "deep" and "natural" to refine the prose. However, I might run into many occurrences, so identifying a finite set of problematic cases will be essential.
thinking
**Inspecting context for clarity**

I’m thinking about inspecting contexts around selected obvious hits. I might use a script to gather snippets from around each line. Using `sed -n` seems like a good approach for lines with suspect matches, focusing on about 20-30 instances. I want to ensure that any patches I make are minimal to preserve the overall integrity while clarifying the language. It’s all about finding that balance between correction and maintaining the original meaning!
codex
I’ve narrowed this to the genuinely inflated sentences rather than ordinary technical uses of words like `natural`. I’m reading those exact passages now so the edits stay local and don’t disturb theorem content.
exec
/bin/zsh -lc "nl -ba chapters/connections/feynman_connection.tex | sed -n '1,40p'
nl -ba chapters/connections/genus_complete.tex | sed -n '250,270p;744,758p'
nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '636,648p;1130,1142p'
nl -ba chapters/connections/semistrict_modular_higher_spin_w3.tex | sed -n '28,74p'
nl -ba chapters/connections/holographic_datum_master.tex | sed -n '18,30p;1172,1184p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '820,836p'
nl -ba chapters/connections/outlook.tex | sed -n '1,20p;640,650p'
nl -ba chapters/connections/thqg_entanglement_programme.tex | sed -n '1,22p'
nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '11028,11060p'
nl -ba chapters/connections/thqg_open_closed_realization.tex | sed -n '36,46p;353,364p'
nl -ba chapters/connections/entanglement_modular_koszul.tex | sed -n '15,24p'
nl -ba chapters/connections/semistrict_modular_higher_spin_w3.tex | sed -n '1,14p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '1224,1234p;1682,1692p;3712,3756p;4158,4168p;4278,4288p;12662,12672p'
nl -ba chapters/connections/concordance.tex | sed -n '330,340p;966,976p;3408,3420p;5904,5914p;6368,6376p;7648,7658p;8224,8232p;9312,9320p'
nl -ba chapters/connections/outlook.tex | sed -n '568,578p'
nl -ba chapters/connections/editorial_constitution.tex | sed -n '2686,2696p'
nl -ba chapters/connections/poincare_computations.tex | sed -n '102,112p'
nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1172,1208p;2654,2664p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	
     2	The bar complex looks like a Feynman expansion. The differential
     3	is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
     4	the degree counts vertices, and iterated residues on
     5	Fulton--MacPherson boundary strata play the role of UV divergences.
     6	The similarity is striking enough to demand an answer: is the bar
     7	complex a literal reformulation of perturbative QFT, or only a
     8	structural analogy?
     9	
    10	The honest answer distinguishes two regimes. For the Heisenberg
    11	algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
    12	reproduces the free-boson residue calculus exactly, and
    13	Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
    14	expected all-genera path-integral identification. For interacting
    15	theories, Volume~I proves only the
    16	genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
    17	the local binary/ternary reduction package; the general perturbative
    18	comparison remains conjectural
    19	\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
    20	The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 succeeded in 51ms:
   820	 & Strong completion-tower theorem
   821	 (Thm~\ref{thm:completed-bar-cobar-strong});
   822	 $\mathcal{W}_\infty$ unconditional at all stages;
   823	 Yangian eval-core verified ($249$~tests);
   824	 DK-$5$ categorical packet accessible in type~A. \\
   825	MC5 & \textbf{Analytic part proved}
   826	 & HS-sewing / convergence proved; BV/BRST-bar comparison,
   827	 Feynman, AGT, and holographic identifications remain downstream. \\
   828	\midrule
   829	Ind. & --- & ${\sim}8$ independent problems
   830	 (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
   831	\bottomrule
   832	\end{tabular}
   833	\end{center}
   834	\end{remark}
   835	
   836	\begin{remark}[Proof roadmaps]\label{rem:proof-roadmaps}
     1	% ======================================================================
     2	% OUTLOOK — Replaces concordance + editorial_constitution in the
     3	% monograph proper. Contains the mathematical architecture (three
 succeeded in 51ms:
  1224	\end{tabular}
  1225	\end{center}
  1226	The degree-$4$ shadow \emph{is} the cusp form period: the quartic
  1227	resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
  1228	from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
  1229	$\tau(n)$ is governed by the Ramanujan conjecture
  1230	$\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
  1231	which places the zeros of $L(s,\Delta_{12})$ on
  1232	$\mathrm{Re}(s) = 6$. The tower terminates at degree~$4$ because
  1233	$\dim S_{12} = 1$: a single cusp form exhausts the cuspidal
  1234	spectrum, and $o_5 = 0$.
  1682	$\cM_{1,1} = \mathrm{SL}(2,\bZ)\backslash\mathbb{H}$;
  1683	the fusion ring and VVMF arithmetic live in the
  1684	\emph{multi-component structure} of the character vector,
  1685	not in the scalar primary-counting function.
  1686	\end{enumerate}
  1687	A natural refinement:
  1688	a \emph{genus-dependent arithmetic depth}
  1689	$d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
  1690	independent Hecke eigenforms in the genus-$g$




thinking
**Assessing report clarity**

I believe the final report can address explicit style inflation, but I won’t cover every neutral technical verb. Since the user requested a similar slop removal approach, I think it’s likely acceptable to do so. It’s important that the report is clear and understandable, so I’ll focus on refining the language while ensuring it meets the user’s expectations for clarity. I’m on the right track thinking this way!
thinking
**Evaluating data and patching**

I’m thinking about how to refine my search for specific terms. I might need to check around line 1081 to see what “full spectrum” refers to—maybe it’s not a big deal. The term "centrepiece" definitely needs attention. I’ll also look into the arithmetic_shadows at line 5922, specifically about "tower organizes MC deformation data." It seems worth inspecting more closely. Overall, I’m ready to patch any identified occurrences in the output list.
thinking
**Identifying patchable phrases**

I'm considering patching only specific loaded adjectives and phrases. Some of them include "striking enough to demand an answer," "categorically richer object," and "natural holographic interpretation." I’m also looking at things like "deepest structural obstruction" and "tower's deepest arithmetic content." Phrases like "deeper phenomenon than NAP duality" and "six-tuple organizes a genuine bulk/boundary system" seem important too. I might also want to include "fundamentally genus-1 phenomenon" and "fundamentally different object" in the patch list. It's a lot to manage, but I want to get it right!
thinking
**Considering patch approach**

I’m thinking that "strictly richer" might be okay, but it's still pretty loaded. Maybe I could rewrite it to clarify the precise differences. I need to search for terms like "centrepiece," "deeper," "rich," and others after my edits to ensure nothing's left unresolved. I’m also considering a plan for pre-edit verification since there are certain hot zones that aren’t shown. It's suggested to include a commentary fenced block before making any edits in those zones. I want to keep everything clear and tidy!
codex
I’ve isolated the actual prose-inflation hits. The edit pass will do two things only: replace literal em-dash placeholders/comments, and flatten rhetorical phrases into neutral statements without changing mathematical scope or claim status.

```text
scope: chapters/connections/*.tex
issue class: AP29 prose hygiene + em-dash ban
banned-token sweep (standard list): clean
residual offenders found: rhetorical inflation ("striking", "deeper/deepest", "richer", "centrepiece", "natural first guess/interpretation/refinement"), literal --- / — in comments and table cells
status/labels/formulas touched: none
edit policy: sentence-local rewrites only; preserve theorem content, labels, and references
verdict: ACCEPT
```
Plan update
Auditing only prose-slop surfaces in chapters/connections/*.tex and applying sentence-local fixes.
  ✓ Enumerate slop/em-dash findings in chapters/connections/*.tex
  → Apply minimal wording fixes only in affected connection files
  • Re-run directory-wide grep to verify the cleaned surface






thinking
**Refining Terminology**

I'm exploring the best phrasing for statements about arithmetic content in a tower. Instead of saying "the tower's deepest arithmetic content," I'll use "the tower's degree-4 arithmetic content" or "the tower's arithmetic content at degree 4." 

For other phrases, I think "A natural refinement" could be simplified to just "A refinement." It's also better to clarify "and is a fundamentally different object" to "and is a separate object." 

Lastly, I need to consider simplifying "deepest, requiring naturality in A" to "least local, requiring naturality in A." That makes sense since I am considering enumerated conditions.
thinking
**Inspecting Conditions and Terminology**

I’m considering a list of conditions. For example, condition (i) is the most concrete, (ii) is checkable, and (iii) is the strongest, which requires a certain naturality in A. I think using "strongest" is appropriate since it implies the most demanding condition.

I’ll revise the phrase "admits a natural interpretation within the shadow obstruction tower" to simply "admits an interpretation within the shadow obstruction tower."

Also, I can rephrase "this is the deepest structural obstruction" to "this is the main structural obstruction." I still want to check on some additional phrases like "tower organizes MC deformation data" and "same mechanism as (ii)" to see if they fit well. Lastly, I’ll look into the concept of "deeply transcendental" and see if I can refine it based on earlier data.
thinking
**Considering "Deep" Patching**

I’m thinking it might be a good idea to patch the term "deep" as well since I haven't inspected it thoroughly. I could search through all occurrences of "deep," "deeper," and "deepest" in the chapters and connections. There could be quite a few sections that need handling.

It makes sense to run this search later after I've done the initial patch. I’ll consider patching all remaining "deep" occurrences too, as some might be legitimate usages.
thinking
**Refining terminology**

I'm thinking about how to improve the phrase "major open problem." Instead of "deepest layer," I should use "final layer" or "last layer." The phrase "last layer" sounds clearer and more concise, so I’ll go with that. It's all about ensuring I communicate effectively, and small adjustments can make a big difference. I wonder if there are other terms that might need a similar rethink!
thinking
**Exploring search options**

I'm considering whether to ignore the mention of a "structured route." It seems okay, but I might need to focus on "fundamentally" occurrences only found in genus1 and arithmetic. I wonder if it would help to search for more information later. There’s quite a bit to think about with this, and I just want to ensure I’m getting it right!
thinking
**Evaluating patch strategy**

I’m considering how to manage the patching process. If there are adjacent lines around a subsection, I might need to replace one hunk instead of both, especially since there are nine pairs to work through. It could take a while. I wonder if we need to patch comment separators in all files, but I’ll aim to patch everything just in case. It might be a considerable risk, but I think I can handle it.
codex
I’ve got the edit set. I’m patching only the flagged sentences and comment/table separators now; no theorem environments, formulas, labels, or status tags are being changed.
codex
One hunk missed exact context, so I’m splitting the patch into smaller verified chunks. I’ll re-read the mismatched spots and then apply the edits file by file to keep the patch deterministic.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '964,974p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/connections/feynman_connection.tex chapters/connections/genus_complete.tex chapters/connections/genus1_seven_faces.tex chapters/connections/semistrict_modular_higher_spin_w3.tex chapters/connections/holographic_datum_master.tex chapters/connections/arithmetic_shadows.tex chapters/connections/concordance.tex chapters/connections/outlook.tex chapters/connections/editorial_constitution.tex chapters/connections/poincare_computations.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/thqg_entanglement_programme.tex chapters/connections/entanglement_modular_koszul.tex chapters/connections/thqg_open_closed_realization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   964	\eqref{eq:factorization-envelope-pipeline} replaces \emph{ad hoc}
   965	constructions (free fields for Heisenberg, currents for
   966	Kac--Moody, the stress tensor for Virasoro) with a single
   967	functorial input: a Lie conformal algebra. The bar-intrinsic
   968	construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
   969	$\Thetaenv(R)$ from this input. The super
   970	extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
   971	same mechanism organizes the nonlinear chiral landscape.
   972	\end{remark}
   973	
   974	\begin{remark}[Conjectural frontier]
 succeeded in 51ms:
Total output lines: 485

diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debe..a8a1e9d 100644
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -63,7 +63,9 @@ Their proved core and conditional refinements are recorded explicitly below.
  Thm~\ref{thm:modular-characteristic}\textup{)};
  genus~$1$ is universal for all families;
  multi-weight $g \geq 2$ acquires the cross-channel term
- $\delta F_g^{\mathrm{cross}}$; the routing
+ $\delta F_g^{\mathrm{cross}}$
+ \textup{(}Thm~\ref{thm:multi-weight-genus-expansion}\textup{)};
+ the routing
  $\Theta_\cA \to \mathrm{obs}_g \to$ family index is non-circular
  & \ClaimStatusProvedHere \\
 \textbf{H} & Chiral Hochschild
@@ -715,14 +717,15 @@ The precise comparison:
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.



thinking
**Addressing patch issues**

I see that there are unrelated user changes in some files, and I need to be careful not to revert those. Since the previous patch didn't apply any of my changes, I should check if files like "feynman_connection" are still original. It's important that I carefully patch incrementally, considering the dirty worktree and preserving those unwanted changes in "concordance," "editorial_constitution," and "frontier_modular_holography_platonic." I’ll focus on patching selected files individually using exact current context lines.
thinking
**Considering patching strategy**

I might hold off on patching "frontier_modular_holography_platonic" since there are unrelated dirty changes, but I could patch just my specific lines. I need to look closely at line 1177 in "holographic_datum_master" because there’s a duplicated phrase that needs fixing, especially since my previous patch had that redundancy. I'll also think about using `perl` to change comment separators but will stick to apply_patch for now. I should focus on smaller patches across multiple files while avoiding the tricky repeated comments. It’s important to keep the dirty changes in mind!
thinking
**Gathering context for patching**

I’m looking to gather exact contexts for patching, and I already have some for "holographic_datum_master" at line 1177 for the comments. It’s important not to include repeated identical lines without proper context. I can still create patches with locally unique lines nearby. I'll also check current contexts for files we haven't inspected yet. For the "thqg_open_closed_realization" comments, I’ll get unique contexts around each subsection, and I need to closely inspect "outlook" lines 2 and 646, plus arithmetic tables at line 11033.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/feynman_connection.tex
@@ -5,3 +5,3 @@
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
apply_patch(auto_approved=true) exited 0 in 20ms:
Success. Updated the following files:
M chapters/connections/feynman_connection.tex
file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 

file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex
@@ -260,3 +260,3 @@
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
@@ -749,4 +749,4 @@
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M chapters/connections/genus_complete.tex
file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..5bad56c060dda4bab2670a93e8e0de3c6a22edfc
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual

file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..5bad56c060dda4bab2670a93e8e0de3c6a22edfc
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex
@@ -641,3 +641,3 @@
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
@@ -1135,3 +1135,3 @@
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
apply_patch(auto_approved=true) exited 0 in 31ms:
Success. Updated the following files:
M chapters/connections/genus1_seven_faces.tex
file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..5bad56c060dda4bab2670a93e8e0de3c6a22edfc
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual

file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..5bad56c060dda4bab2670a93e8e0de3c6a22edfc
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -30,3 +30,3 @@
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
@@ -68,3 +68,3 @@
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 36ms:
Success. Updated the following files:
M chapters/connections/semistrict_modular_higher_spin_w3.tex
file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..5bad56c060dda4bab2670a93e8e0de3c6a22edfc
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..66eb4913aa35b965794bdc7e73c9e67c54ddde79
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,7 +3,7 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..5bad56c060dda4bab2670a93e8e0de3c6a22edfc
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex
@@ -23,3 +23,3 @@
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
@@ -1176,3 +1176,3 @@
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
apply_patch(auto_approved=true) exited 0 in 43ms:
Success. Updated the following files:
M chapters/connections/holographic_datum_master.tex
file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update:
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex
@@ -1227,3 +1227,3 @@
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
@@ -1686,3 +1686,3 @@
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
@@ -3717,3 +3717,3 @@
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
@@ -3749,3 +3749,3 @@
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
@@ -4163,3 +4163,3 @@
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
@@ -4281,4 +4281,4 @@
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
@@ -12666,3 +12666,3 @@
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
apply_patch(auto_approved=true) exited 0 in 49ms:
Success. Updated the following files:
M chapters/connections/arithmetic_shadows.tex
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..86c550efc7429cc58762a73ff60a79447035ce78
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..86c550efc7429cc58762a73ff60a79447035ce78
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -334,3 +334,3 @@
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
@@ -970,3 +970,3 @@
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
@@ -3414,3 +3414,3 @@
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
@@ -5909,3 +5909,3 @@
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
@@ -6372,3 +6372,3 @@
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
@@ -7655,3 +7655,3 @@
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
@@ -8229,3 +8229,3 @@
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
@@ -9318,3 +9318,3 @@
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
apply_patch(auto_approved=true) exited 0 in 58ms:
Success. Updated the following files:
M chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..86c550efc7429cc58762a73ff60a79447035ce78
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..9e3ded0742ff7c59d9bd83af8f1b925e442009c6
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..86c550efc7429cc58762a73ff60a79447035ce78
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..9e3ded0742ff7c59d9bd83af8f1b925e442009c6
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}


thinking
**Inspecting lines in Outlook**

I'm focusing on patching Outlook and need to inspect specific lines closely. It looks like I'll be checking line wrapping, for instance, around line 568. I want to confirm everything is correct and ensure nothing is missed during the patching process. It's important to pay attention to these details to avoid issues later on! Let's dive in and see what adjustments need to be made!
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '826,832p;2688,2693p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1174,1205p;2656,2662p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/outlook.tex | sed -n '1,12p;568,576p;644,649p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	% ======================================================================
     2	% OUTLOOK — Replaces concordance + editorial_constitution in the
     3	% monograph proper. Contains the mathematical architecture (three
     4	% pillars, three rings, five main theorems) and key definitions
     5	% referenced from theory chapters. The full concordance with
     6	% literature comparisons, conjecture stratification, and research
     7	% programmes is available as a standalone companion document
     8	% (standalone/editorial.tex).
     9	% ======================================================================
    10	
    11	\chapter{Outlook}
    12	\label{chap:outlook}
   568	but \emph{not} the cross-channel correction. The cross-channel
   569	correction arises from the multi-channel Feynman rules of the stable
   570	graph sum, not from the spectral curve of the integrable hierarchy.
   571	This separation (integrable on the diagonal, non-integrable
   572	off-diagonal) instantiates the principle that the shadow obstruction
   573	tower is richer than the KdV hierarchy
   574	(Remark~\ref{rem:shadow-multiplicative-deformation}).
   575	
 succeeded in 52ms:
  1174	 to~$\cA$. With the correct large transversal boundary condition, the
  1175	 boundary chiral algebra of the KK-reduced HT theory identifies with the
  1176	 universal defect algebra of the parent theory~\cite{GZ26};
  1177	 the same mechanism unifies twisted and celestial holography.
  1178	\item \emph{Line-side algebraic model.}
  1179	 $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  1180	 meromorphic line-side model, with the meromorphic tensor/OPE package
  1181	 supplied on the compatible dg-shifted Yangian surface
  1182	 of~\cite{DNP25}. The tensor product is meromorphic, not genuinely
  1183	 braided.
  1184	\item \emph{Genus-zero binary shadow.}
  1185	 $r(z) \in \cA^! \,\widehat{\otimes}\, \cA^!\bigl[\![z^{-1},z]\!\bigr]$
  1186	 is the degree-one Maurer--Cartan element controlling the binary
  1187	 line-operator OPE. It satisfies the $A_\infty$ Yang--Baxter equation
  1188	 and identifies with the bar-cobar twisting morphism
  1189	 (Definition~\ref{def:dg-shifted-yangian};
  1190	 Remark~\ref{rem:yangian-twisting-morphism}).
  1191	\item \emph{Modular Maurer--Cartan class.}
  1192	 $\Theta_\cA \in
  1193	 \mathrm{MC}\!\bigl(\Defcyc(\cA) \,\widehat{\otimes}\,
 succeeded in 52ms:
   826	 & HS-sewing / convergence proved; BV/BRST-bar comparison,
   827	 Feynman, AGT, and holographic identifications remain downstream. \\
   828	\midrule
   829	Ind. & --- & ${\sim}8$ independent problems
   830	 (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
   831	\bottomrule
   832	\end{tabular}
  2688	\emph{nilpotence is the logarithm of periodicity}: the bar
  2689	construction is the categorical logarithm whose single-valued
  2690	regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
  2691	multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
  2692	curvature $\kappa(\cA)$ is the infinitesimal generator of the
  2693	monodromy; the coderived category is the analytic continuation; the
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..86c550efc7429cc58762a73ff60a79447035ce78
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..9e3ded0742ff7c59d9bd83af8f1b925e442009c6
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..e8178034bb756bd3a21eaf5746fa5d7ab46d2920
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -7,5 +7,5 @@
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
M /Users/raeez/chiral-bar-cobar/chapters/connections/outlook.tex
@@ -1,3 +1,3 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
@@ -572,3 +572,3 @@
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
@@ -645,3 +645,3 @@
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
M /Users/raeez/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex
@@ -18,5 +18,5 @@
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
M /Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex
@@ -828,3 +828,3 @@
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
@@ -2690,3 +2690,3 @@
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
M /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex
@@ -11032,9 +11032,9 @@
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
@@ -11044,6 +11044,6 @@
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
@@ -11056,3 +11056,3 @@
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1176,3 +1176,3 @@
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
@@ -1203,3 +1203,3 @@
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
@@ -2658,4 +2658,4 @@
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_entanglement_programme.tex
@@ -5,6 +5,6 @@
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
@@ -15,5 +15,5 @@
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
apply_patch(auto_approved=true) exited 0 in 89ms:
Success. Updated the following files:
M chapters/connections/outlook.tex
M chapters/connections/editorial_constitution.tex
M chapters/connections/frontier_modular_holography_platonic.tex
M chapters/connections/thqg_entanglement_programme.tex
M chapters/connections/arithmetic_shadows.tex
M chapters/connections/entanglement_modular_koszul.tex
M chapters/connections/semistrict_modular_higher_spin_w3.tex
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..9e3ded0742ff7c59d9bd83af8f1b925e442009c6
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..172decc65cfcd24297b345fbe1b81c1187753998
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -2656,8 +2656,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}

file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..9e3ded0742ff7c59d9bd83af8f1b925e442009c6
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..172decc65cfcd24297b345fbe1b81c1187753998
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -2656,8 +2656,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}

codex
The prose rewrites are in. I’m finishing the mechanical cleanup now: remaining literal `---` separators/placeholders and any leftover high-noise adjectives that still survive the grep.
exec
/bin/zsh -lc "rg -n --glob 'chapters/connections/*.tex' -- '---|—' chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_open_closed_realization.tex:40:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:44:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:357:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:361:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:519:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:523:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:625:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:630:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:944:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:948:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1033:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1037:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1213:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1218:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1379:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1383:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1529:% -------------------------------------------------------------------
chapters/connections/thqg_open_closed_realization.tex:1533:% -------------------------------------------------------------------
exec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(striking|deeper|deepest|richer|centrepiece|centerpiece|fundamentally|natural refinement|natural interpretation|natural first guess|first natural|nearest route|correct first test)' chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/poincare_computations.tex:107:The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
chapters/connections/frontier_modular_holography_platonic.tex:1905:obtained by projecting $\Theta_\cA$ to successively deeper strata of
chapters/connections/concordance.tex:10350: strictly richer than the closed-sector classes.
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..9e3ded0742ff7c59d9bd83af8f1b925e442009c6
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..172decc65cfcd24297b345fbe1b81c1187753998
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -2656,8 +2656,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}

exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '10344,10352p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_open_closed_realization.tex | sed -n '38,45p;355,362p;517,524p;623,631p;942,949p;1031,1038p;1211,1219p;1377,1384p;1527,1534p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 10344	
 10345	 \smallskip\noindent
 10346	 \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
 10347	 The open sector of $\Theta^{\mathrm{oc}}_\cA$
 10348	 provides boundary-marked tautological classes
 10349	 $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
 10350	 strictly richer than the closed-sector classes.
 10351	 The four-sector decomposition of the MC equation
 10352	 produces relations with both interior and boundary
 succeeded in 50ms:
    38	\end{remark}
    39	
    40	% -------------------------------------------------------------------
    41	\subsection{The chiral endomorphism operad and the algebraic derived center}
    42	\label{subsec:thqg-chiral-endomorphism-operad}
    43	\index{chiral endomorphism operad|textbf}
    44	% -------------------------------------------------------------------
    45	
   355	\end{definition}
   356	
   357	% -------------------------------------------------------------------
   358	\subsection{The universal open/closed pair}
   359	\label{subsec:thqg-universal-oc-pair}
   360	\index{universal open/closed pair|textbf}
   361	% -------------------------------------------------------------------
   362	
   517	\end{remark}
   518	
   519	% -------------------------------------------------------------------
   520	\subsection{Restriction from global to local: the bordered FM bridge}
exec
/bin/zsh -lc "nl -ba chapters/connections/poincare_computations.tex | sed -n '104,108p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   104	This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
   105	
   106	\emph{The geometric Langlands connection.}
   107	The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
   108	
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..9e3ded0742ff7c59d9bd83af8f1b925e442009c6
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..172decc65cfcd24297b345fbe1b81c1187753998
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -2656,8 +2656,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..fb0f7c635cdc157c282d29baa288983189520f0e
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -1174,7 +1174,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/poincare_computations.tex
@@ -106,3 +106,3 @@
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -10348,4 +10348,4 @@
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex
@@ -39,3 +39,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
@@ -43,3 +43,3 @@
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -356,3 +356,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
@@ -360,3 +360,3 @@
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -518,3 +518,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
@@ -522,3 +522,3 @@
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -624,3 +624,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
@@ -629,3 +629,3 @@
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -943,3 +943,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
@@ -947,3 +947,3 @@
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -1032,3 +1032,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
@@ -1036,3 +1036,3 @@
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -1212,3 +1212,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
@@ -1217,3 +1217,3 @@
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -1378,3 +1378,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
@@ -1382,3 +1382,3 @@
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
@@ -1528,3 +1528,3 @@
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
@@ -1532,3 +1532,3 @@
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
apply_patch(auto_approved=true) exited 0 in 96ms:
Success. Updated the following files:
M chapters/connections/poincare_computations.tex
M chapters/connections/concordance.tex
M chapters/connections/thqg_open_closed_realization.tex
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..172decc65cfcd24297b345fbe1b81c1187753998
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -2656,8 +2656,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}

file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..172decc65cfcd24297b345fbe1b81c1187753998
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -2656,8 +2656,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}

exec
/bin/zsh -lc "rg -n --glob 'chapters/connections/*.tex' -- '---|—' chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(striking|deeper|deepest|richer|centrepiece|centerpiece|fundamentally|natural refinement|natural interpretation|natural first guess|first natural|nearest route|correct first test)' chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/connections/feynman_connection.tex chapters/connections/genus_complete.tex chapters/connections/genus1_seven_faces.tex chapters/connections/semistrict_modular_higher_spin_w3.tex chapters/connections/holographic_datum_master.tex chapters/connections/arithmetic_shadows.tex chapters/connections/concordance.tex chapters/connections/outlook.tex chapters/connections/editorial_constitution.tex chapters/connections/poincare_computations.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/thqg_entanglement_programme.tex chapters/connections/entanglement_modular_koszul.tex chapters/connections/thqg_open_closed_realization.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
chapters/connections/frontier_modular_holography_platonic.tex:1906:obtained by projecting $\Theta_\cA$ to successively deeper strata of
 succeeded in 51ms:
Total output lines: 1256

diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279..1d4c7da 100644
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@ $4$ & Ramanujan $\Delta_{12}$
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@ the fusion ring and VVMF arithmetic live in the
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -2656,8 +2657,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}






thinking
**Refining search terms**

I see that the diff output includes some unrelated changes, and I want to ensure our edits don’t conflict. I should search for specific technical terms like "deeper strata" and maybe others like "centrepiece." I'll refine my search to include "centerpiece" and "natural interpretation." 

My aim is to catch any modifications, possibly including "frontier," to avoid missing anything due to case sensitivity. I'll check additional terms but remain cautious about any technical phrases that might not seem relevant.
thinking
**Finalizing findings format**

I might need to adjust the comment in the `outlook` line. First, I want to verify that my search for specific patterns returns only technical results, and it seems to be doing that.

Next, it looks like I should gather line numbers of our changes. The user seems to want a clear output listing problems at the format "PROBLEM at file:line" along with the exact edits applied. I could use tools like `rg` for matching old and new lines or `nl -ba` to help with gathering line numbers. Finally, it's important to present this in a concise manner.
thinking
**Clarifying findings output**

I’m thinking about how to present the findings, which should range from 20 to 30 lines but not exceed 70. Currently, I have about 26 findings to report. 

Should I compress them? The requirement states each finding must be clear. Maybe I could group similar comment replacements as one finding per file or by repeated patterns, but then I wonder if that fits the “PROBLEM at file:line” format, which seems singular. So, I need to strike a balance between clarity and conciseness.
thinking
**Evaluating code change tracking**

I'm considering how to handle multiple files and tracking specific changes. I could use `git diff --unified=0` to mention the approximate start lines from the hunk. But I'm also thinking about needing exact line numbers, possibly using `rg -n` on new phrases to map each change. While `git diff` can show unrelated changes, I should focus on our current line numbers without mentioning those unrelated ones. It’s all about keeping it clear and concise!
thinking
**Creating a change summary table**

I think it could be easiest to create a short table reflecting our planned changes and the associated line numbers from earlier commands like `nl` or the new `rg`. I could also use `rg -n` for identifying our new phrases. Writing a script to print file lines and their content based on the patterns we changed sounds like a solid plan. For repetitive replacements, I’ll want to use `rg` to find occurrences near specific comments. It's all about organization!
codex
The verification sweep is down to one technical `deeper strata` phrase in a geometric statement, which I’m leaving because it describes an actual filtration. I’m now extracting the final changed line numbers so I can report each finding with the exact edit, per your format.
exec
/bin/zsh -lc "rg -n '"'^'"\\s*& n/a \\\\\\\\"'$|''^% =+$'"' chapters/connections/arithmetic_shadows.tex chapters/connections/editorial_constitution.tex chapters/connections/entanglement_modular_koszul.tex chapters/connections/semistrict_modular_higher_spin_w3.tex chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'precise question|chain-level modular functor|holographic interpretation:|corresponding genus-|genus-\\"'$1'"\\"'$ phenomenon|first route from the proved modular Koszul core|parallel directions|main theorem of Part|core result of Part|arithmetic content at degree|''^A refinement:|separate object'"\\.|structural point is that|strongest, requiring naturality|interpretation within the shadow obstruction tower|main structural obstruction|chain-level categorical invariant|same construction for nonlinear chiral families|initial audit surface|"'^A first guess is|broader geometric settings|main unresolved problem|a major open problem|is the last layer|OUTLOOK:|extends beyond the KdV hierarchy|Additional stub labels:|has more structure than the classical picture|different phenomenon from NAP duality|same construction applies to twisted and celestial holography|defines a bulk/boundary|carries more data|Entanglement rank replaced;|Tomita-Takesaki downgraded;|''^% ProvedHere:|''^% Conjectured:|''^% Heuristic:'"' chapters/connections/feynman_connection.tex chapters/connections/genus_complete.tex chapters/connections/genus1_seven_faces.tex chapters/connections/semistrict_modular_higher_spin_w3.tex chapters/connections/holographic_datum_master.tex chapters/connections/arithmetic_shadows.tex chapters/connections/concordance.tex chapters/connections/outlook.tex chapters/connections/editorial_constitution.tex chapters/connections/poincare_computations.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/semistrict_modular_higher_spin_w3.tex:8:% ======================================================================
chapters/connections/semistrict_modular_higher_spin_w3.tex:10:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:19:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:21:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:91:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:95:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:223:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:227:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:340:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:344:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:471:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:475:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:556:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:560:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:692:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:696:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:967:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:971:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:1129:% ======================================================================
chapters/connections/entanglement_modular_koszul.tex:1133:% ======================================================================
 succeeded in 51ms:
chapters/connections/semistrict_modular_higher_spin_w3.tex:31:The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
chapters/connections/semistrict_modular_higher_spin_w3.tex:69:The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
chapters/connections/holographic_datum_master.tex:24:theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
chapters/connections/holographic_datum_master.tex:1181:The seven-face programme is a core result of Part~\ref{part:standard-landscape}
chapters/connections/feynman_connection.tex:6:The similarity raises a precise question: is the bar
chapters/connections/thqg_entanglement_programme.tex:6:% F1: Entanglement rank replaced; direct sum ≠ tensor product.
chapters/connections/thqg_entanglement_programme.tex:9:% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
chapters/connections/thqg_entanglement_programme.tex:16:% ProvedHere: follows from the existing proved core
chapters/connections/thqg_entanglement_programme.tex:17:% Conjectured: well-motivated, precise, falsifiable
chapters/connections/thqg_entanglement_programme.tex:18:% Heuristic: structural identification, not yet a theorem
chapters/connections/outlook.tex:2:% OUTLOOK: replaces concordance + editorial_constitution in the
chapters/connections/outlook.tex:573:tower extends beyond the KdV hierarchy
chapters/connections/outlook.tex:646:% Additional stub labels: these were defined in the full concordance
chapters/connections/frontier_modular_holography_platonic.tex:1177: the same construction applies to twisted and celestial holography.
chapters/connections/frontier_modular_holography_platonic.tex:1204: that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
chapters/connections/frontier_modular_holography_platonic.tex:2660:The spectral sequence for $\mathcal W_3$ carries more data
chapters/connections/poincare_computations.tex:107:The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
chapters/connections/genus_complete.tex:32:The result is a chain-level modular functor
chapters/connections/genus_complete.tex:261:\emph{first Chern class} of a chain-level modular functor.
chapters/connections/genus_complete.tex:265:chain-level modular functor (not the scalar genus tower) that
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -2656,8 +2657,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}

exec
/bin/zsh -lc "rg -n '"'^% ===================================================================$'"' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'broader|n/a|has more structure than the classical picture|"'^% =====================================================================$'"' chapters/connections/concordance.tex chapters/connections/editorial_constitution.tex chapters/connections/entanglement_modular_koszul.tex chapters/connections/semistrict_modular_higher_spin_w3.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
40:% ===================================================================
44:% ===================================================================
357:% ===================================================================
361:% ===================================================================
519:% ===================================================================
523:% ===================================================================
625:% ===================================================================
630:% ===================================================================
944:% ===================================================================
948:% ===================================================================
1033:% ===================================================================
1037:% ===================================================================
1213:% ===================================================================
1218:% ===================================================================
1379:% ===================================================================
1383:% ===================================================================
1529:% ===================================================================
1533:% ===================================================================
 succeeded in 51ms:
chapters/connections/editorial_constitution.tex:456:tree-level moduli-integration/amplitude pairing is only conditional
chapters/connections/editorial_constitution.tex:829:Ind. & n/a & ${\sim}8$ independent problems
chapters/connections/editorial_constitution.tex:914:moduli-integration/amplitude pairing is only conditional
chapters/connections/editorial_constitution.tex:2691:multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
chapters/connections/concordance.tex:3021: & \textup{n/a} \\
chapters/connections/concordance.tex:6373:The following extensions use the same master diagram in broader
chapters/connections/concordance.tex:6514: The broader HT boundary/line route, beginning with
chapters/connections/concordance.tex:11301: The broader programme contains open problems downstream
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -2656,8 +2657,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}

exec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|arguably|perhaps|seems to|appears to)' chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i --glob 'chapters/connections/*.tex' '(striking|deeper|deepest|richer|centrepiece|centerpiece|fundamentally|natural refinement|natural interpretation|natural first guess|first natural|nearest route|correct first test)' chapters/connections" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
chapters/connections/frontier_modular_holography_platonic.tex:1906:obtained by projecting $\Theta_\cA$ to successively deeper strata of
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -2656,8 +2657,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}


thinking
**Evaluating technical terms**

I’m considering whether the term "deeper strata" is appropriate in this context. It relates to geometric filtration, and I think it might work since it's about stratification depth rather than style. I'll note that it's residual, which should be acceptable. Okay, I definitely need to update the plan after this assessment, as it's important to ensure everything aligns correctly. Let's move forward!
Plan update
Applied the slop-cleanup edits across the assigned connection files and verified the surface with directory-wide grep. Only a technical geometric use of 'deeper strata' remains.
  ✓ Enumerate slop/em-dash findings in chapters/connections/*.tex
  ✓ Apply minimal wording fixes only in affected connection files
  ✓ Re-run directory-wide grep to verify the cleaned surface
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -2656,8 +2657,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}


thinking
**Structuring findings and verification**

I need to mention the semistructured comment separators on lines 8 and 10, but not line 1. I should craft the final output with headings like **Findings** and **Verification**, ensuring each bullet is clear and concise. I'll avoid nested bullets to keep it simple and straightforward. It’s important to focus on clarity while providing the necessary details. Let's write it in an organized manner to make it easy to read!
codex
**Findings**
- `PROBLEM at chapters/connections/feynman_connection.tex:6`: rhetorical escalation. `EXACT edit applied`: `The similarity is striking enough to demand an answer` -> `The similarity raises a precise question`.
- `PROBLEM at chapters/connections/genus_complete.tex:261,750-751`: inflated prose (`categorically richer`, `natural holographic interpretation`). `EXACT edit applied`: `categorically richer object` -> `chain-level modular functor`; `carries a natural holographic interpretation` -> `admits a holographic interpretation`.
- `PROBLEM at chapters/connections/genus1_seven_faces.tex:642,1136`: loaded phrasing (`deeper identification`, `fundamentally genus-1`). `EXACT edit applied`: `deeper identification` -> `corresponding genus-$g \geq 2$ identification`; `fundamentally genus-$1$ phenomenon` -> `genus-$1$ phenomenon`.
- `PROBLEM at chapters/connections/semistrict_modular_higher_spin_w3.tex:8,10,31,69`: forbidden `---` comment separators and inflated chapter-opening prose. `EXACT edit applied`: `% ----------------------------------------------------------------------` -> `% ======================================================================` at lines 8 and 10; `nearest route`/`natural targets`/`recognizably gravitational` sentence -> a neutral `first route`/`target settings` formulation at line 31; `correct first test` -> `first one handled here because it admits proofs` at line 69.
- `PROBLEM at chapters/connections/holographic_datum_master.tex:24,1181`: promotional `centrepiece` language. `EXACT edit applied`: `the centrepiece of Part...` -> `the main theorem of Part...`; `The seven-face programme is the centrepiece...` -> `The seven-face programme is a core result...`.
- `PROBLEM at chapters/connections/arithmetic_shadows.tex:1228,1687,3718,3750,4164,4283,11033,11036,11039,11045,11048,11057,12667`: repeated style inflation and `---` placeholders. `EXACT edit applied`: `deepest arithmetic content` -> `arithmetic content at degree~$4$`; `A natural refinement` -> `A refinement`; `fundamentally different object` -> `separate object`; `deeper point` -> `structural point`; `deepest` -> `strongest`; `natural interpretation` -> `interpretation`; each table cell `& --- \\` -> `& n/a \\`; `deepest structural obstruction` -> `main structural obstruction`.
- `PROBLEM at chapters/connections/concordance.tex:335,971,3415,5910,6373,7656,8230,9319,10350`: rhetorical and inflated wording. `EXACT edit applied`: `categorically richer` -> `a chain-level categorical invariant`; `same mechanism organizes the nonlinear chiral landscape` -> `same construction for nonlinear chiral families`; `first natural audit surface` -> `initial audit surface`; `A natural first guess` -> `A first guess`; `richer geometric settings` -> `broader geometric settings`; `single deepest problem` -> `main unresolved problem`; `deepest open problem` -> `a major open problem`; `deepest layer` -> `last layer`; `strictly richer than the closed-sector classes` -> `contain more data than the closed-sector classes`.
- `PROBLEM at chapters/connections/outlook.tex:2,573,646`: em-dash comments and inflated comparison. `EXACT edit applied`: `OUTLOOK —` -> `OUTLOOK:`; `tower is richer than the KdV hierarchy` -> `tower extends beyond the KdV hierarchy`; `Additional stub labels —` -> `Additional stub labels:`.
- `PROBLEM at chapters/connections/editorial_constitution.tex:829,2691`: `---` table placeholder and inflated comparison. `EXACT edit applied`: `Ind. & --- &` -> `Ind. & n/a &`; `configuration-space topology on curves is richer than...` -> `has more structure than...`.
- `PROBLEM at chapters/connections/poincare_computations.tex:107`: inflated comparison (`deeper phenomenon`). `EXACT edit applied`: `a deeper phenomenon than NAP duality` -> `a different phenomenon from NAP duality`.
- `PROBLEM at chapters/connections/frontier_modular_holography_platonic.tex:1177,1204,2660`: inflated packaging language. `EXACT edit applied`: `same mechanism unifies` -> `same construction applies to`; `organizes a genuine bulk/boundary system` -> `defines a bulk/boundary system`; `strictly richer than for Virasoro` -> `carries more data than in the Virasoro case`.
- `PROBLEM at chapters/connections/thqg_entanglement_programme.tex:6,9,16-18`: comment-surface em-dashes. `EXACT edit applied`: replaced `—` with `;` or `:` in the audit notes and status legend.
- `PROBLEM at chapters/connections/entanglement_modular_koszul.tex:19,21`: forbidden `---` comment separators. `EXACT edit applied`: each `% ----------------------------------------------------------------------` -> `% ======================================================================`.
- `PROBLEM at chapters/connections/thqg_open_closed_realization.tex:40,44,357,361,519,523,625,630,944,948,1033,1037,1213,1218,1379,1383,1529,1533`: forbidden `---` comment separators. `EXACT edit applied`: each `% -------------------------------------------------------------------` -> `% ===================================================================`.

**Verification**
`rg` sweeps for the zero-tolerance slop list and for literal `---|—` now come back clean across `chapters/connections/*.tex`. The only remaining `deeper` hit is `chapters/connections/frontier_modular_holography_platonic.tex:1906`, where it refers to actual geometric strata, so I left it. I did not run a TeX build; verification here was grep-based because the edits were prose/comment-local.
file update:
diff --git a/chapters/connections/arithmetic_shadows.tex b/chapters/connections/arithmetic_shadows.tex
index 5c7a279f6aa90b2a009c0c1059327bb770ea4787..1d4c7dab462e66fde1fd1337916b398bd9f6b02c
--- a/chapters/connections/arithmetic_shadows.tex
+++ b/chapters/connections/arithmetic_shadows.tex
@@ -1225,7 +1225,7 @@
 \end{center}
 The degree-$4$ shadow \emph{is} the cusp form period: the quartic
 resonance class $Q(V_{\mathrm{Leech}})$ extracts $L(s,\Delta_{12})$
-from the Epstein zeta function. This is the tower's deepest arithmetic content. The coefficient
+from the Epstein zeta function. This is the tower's arithmetic content at degree~$4$. The coefficient
 $\tau(n)$ is governed by the Ramanujan conjecture
 $\lvert\tau(p)\rvert \le 2p^{11/2}$ (Deligne's theorem),
 which places the zeros of $L(s,\Delta_{12})$ on
@@ -1684,7 +1684,7 @@
 \emph{multi-component structure} of the character vector,
 not in the scalar primary-counting function.
 \end{enumerate}
-A natural refinement:
+A refinement:
 a \emph{genus-dependent arithmetic depth}
 $d_{\mathrm{arith}}^{(g)}(\cA)$, defined as the number of
 independent Hecke eigenforms in the genus-$g$
@@ -3715,7 +3715,7 @@
 = \sum (\dim V)^{-s}$
 (Remark~\ref{rem:categorical-zeta-riemann}) carries
 rank-dependent information but has no Euler product for $N \geq 3$
-and is a fundamentally different object.
+and is a separate object.
 \end{remark}
 
 \begin{conjecture}[The $s=1$ shadow pole, quantum modularity,
@@ -3747,7 +3747,7 @@
 
 \begin{remark}[Evidence and structural interpretation]
 \label{rem:shadow-s1-quantum-volume-evidence}
-The evidence has three layers, but the deeper point is that
+The evidence has three layers, but the structural point is that
 the shadow $L$-function
 $D_2(\cA,s) = -24\kappa\,\zeta(s)\,\zeta(s{-}1)$
 is not merely an analytic device: it is the bridge between
@@ -4161,7 +4161,7 @@
  Shapovalov form.
 \end{enumerate}
 Condition~(i) is most concrete; (ii) is checkable; (iii) is the
-deepest, requiring naturality in~$\cA$.
+strongest, requiring naturality in~$\cA$.
 \end{remark}
 
 \begin{remark}[The shadow spectral triple and Connes axioms]
@@ -4279,8 +4279,8 @@
 \index{Bazhanov--Lukyanov--Zamolodchikov}%
 \index{Dorey--Tateo}%
 The ODE/IM correspondence of Dorey--Tateo~\cite{DT99} and
-Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits a
-natural interpretation within the shadow obstruction tower:
+Bazhanov--Lukyanov--Zamolodchikov~\cite{BLZ99} admits an
+interpretation within the shadow obstruction tower:
 the correspondence is a \emph{projection} of the universal
 MC element~$\Theta_{\cA}$
 (Theorem~\ref{thm:mc2-bar-intrinsic}) onto the
@@ -11030,22 +11030,22 @@
 \cmidrule{1-4}
 1 & CPS automorphy of $M_r(s)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 2 & Prime-locality (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 3 & Prime-locality (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 4 & Prime-locality (irrational)
  & \ClaimStatusConjectured
  & $[\delta_p] = 0$? \\
 5 & Ramanujan (lattice)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 6 & Ramanujan (rational)
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 7 & Ramanujan (irrational)
  & \ClaimStatusConjectured
  & Langlands $r \ge 5$ \\
@@ -11054,7 +11054,7 @@
 \cmidrule{1-4}
 8 & MC determines $\cE_\rho(\cA)$
  & \ClaimStatusProvedHere
- & --- \\
+ & n/a \\
 9 & RS holomorphic at $\rho/2$
  & \ClaimStatusProvedHere
  & Gap P2 \\
@@ -12664,7 +12664,7 @@
  At degrees $r \ge 3$, the shadow amplitudes involve products
  of $E_2^*$, and the Fourier coefficients of $(E_2^*)^k$ are
  \emph{not} multiplicative for $k \ge 2$.
- \textbf{Status:} this is the deepest structural obstruction.
+ \textbf{Status:} this is the main structural obstruction.
  Even if the shadow \emph{coefficients} $S_r$ are tau-independent
  \textup{(}hence trivially Hecke-equivariant\textup{)}, the
  shadow \emph{amplitudes} $\operatorname{Sh}_r^{(1)}(\tau)$
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index e800c2b4fd7faee955b23d22e1d923eecc44d221..de837b8eeb21c3132d237ede82e5c59b67dfd943
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -332,7 +332,7 @@
  first Chern class of the factorization homology bundle.
  The full genus-$g$ invariant, the cohomology
  $H^*(\barB^{(g)}(\cA), \Dg{g})$ and its variation over
- $\mathcal{M}_g$, is categorically richer
+ $\mathcal{M}_g$, is a chain-level categorical invariant
  (Theorem~\ref{thm:chain-modular-functor}).
 
 \item \emph{Deformation-obstruction complementarity
@@ -968,7 +968,7 @@
 construction (Theorem~\ref{thm:mc2-bar-intrinsic}) produces
 $\Thetaenv(R)$ from this input. The super
 extension (Neveu--Schwarz, $\mathcal{N}=2$) suggests the
-same mechanism organizes the nonlinear chiral landscape.
+same construction for nonlinear chiral families.
 \end{remark}
 
 \begin{remark}[Conjectural frontier]
@@ -3412,7 +3412,7 @@
 level is the possible failure of $E_1$-degeneration at
 rational~$k$ (admissible/critical levels), where vacuum null
 vectors can produce genuine higher differentials.
-The hook-type corridor is the first natural audit surface for this
+The hook-type corridor is the initial audit surface for this
 route, but the manuscript currently contains incompatible summaries
 of the type-$A$ abelian-$\mathfrak{n}_+$ locus, so the hook-wide
 extension is not used as unconditional input. Accordingly the
@@ -5907,7 +5907,7 @@
 function (Remark~\ref{rem:two-discriminant-families}).
 
 \emph{Why not the Kodaira--Spencer operator on $H^1$?}
-A natural first guess is
+A first guess is
 $\Delta(x) = \det(1 - x\, T_{\mathrm{KS}} \mid H^1)$
 where $T_{\mathrm{KS}}$ acts on
 $H^1(\bar{B}(\cA)) \cong \mathfrak{sl}_2$ ($3$-dimensional).
@@ -6370,7 +6370,7 @@
 and the family index theorem follows.
 
 \smallskip\noindent\emph{Open problems.}
-The following extensions use the same master diagram in richer
+The following extensions use the same master diagram in broader
 geometric settings:
 $C_{\mathrm{mod}}$ (shifted-symplectic complementarity),
 derived Drinfeld--Kohno, and the elliptic extension.
@@ -7653,7 +7653,7 @@
 bar concentration) constrains the spectral Drinfeld
 class relevant to~\textbf{P3}.
 \textbf{P3} does not feed back into the other two.
-P2~is the \emph{single deepest problem}: it is the
+P2~is the \emph{main unresolved problem}: it is the
 only one whose failure could invalidate the downstream
 conclusions.
 
@@ -8227,7 +8227,7 @@
 $\operatorname{Spec}(\mathcal{O}_F)$ and the
 factorization structure is replaced by adelic
 automorphic forms. The descent from function field to
-number field is the deepest open problem in the
+number field is a major open problem in the
 Langlands programme and has been open since
 Langlands's original letter to Weil (1967).
 
@@ -9316,7 +9316,7 @@
  conjectural (\ClaimStatusConjectured).
 \item The periodic CDG structure
  (Conjecture~\ref{conj:periodic-cdg})
- is the deepest layer: it asserts that the
+ is the last layer: it asserts that the
  cyclotomic grading of the boundary chart
  is reflected in the periodicity of the bar
  differential on the simple quotient.
@@ -10346,8 +10346,8 @@
  \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
  The open sector of $\Theta^{\mathrm{oc}}_\cA$
  provides boundary-marked tautological classes
- $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
- strictly richer than the closed-sector classes.
+ $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which contain
+ more data than the closed-sector classes.
  The four-sector decomposition of the MC equation
  produces relations with both interior and boundary
  markings. These additional relations may generate
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index 841d2d2085b43acf267f96b69ffee3a536a7b3df..28be34ce0ec049c6ac212afae3a1c1e2dce3577e
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -826,7 +826,7 @@
  & HS-sewing / convergence proved; BV/BRST-bar comparison,
  Feynman, AGT, and holographic identifications remain downstream. \\
 \midrule
-Ind. & --- & ${\sim}8$ independent problems
+Ind. & n/a & ${\sim}8$ independent problems
  (periodicity, derived $bc$-$\beta\gamma$, $\mathsf{E}_n$). \\
 \bottomrule
 \end{tabular}
@@ -2688,7 +2688,7 @@
 \emph{nilpotence is the logarithm of periodicity}: the bar
 construction is the categorical logarithm whose single-valued
 regime recovers, via formal-disk restriction, classical Koszul duality over a point (the degree-$2$ stratum) and whose
-multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves is richer than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
+multi-valued regime is the full chiral theory (already at genus~$0$, configuration-space topology on curves has more structure than the classical picture over a point; at genus~$g \geq 1$, Hodge curvature enters); the
 curvature $\kappa(\cA)$ is the infinitesimal generator of the
 monodromy; the coderived category is the analytic continuation; the
 characteristic hierarchy
diff --git a/chapters/connections/entanglement_modular_koszul.tex b/chapters/connections/entanglement_modular_koszul.tex
index 6881fb4dbef0d0c458953189646abc0cde157aed..de43afaca527e14dd7af3922d8b8dae850a4f371
--- a/chapters/connections/entanglement_modular_koszul.tex
+++ b/chapters/connections/entanglement_modular_koszul.tex
@@ -16,9 +16,9 @@
 \index{Ryu--Takayanagi formula!algebraic derivation|textbf}
 \index{quantum extremal surface!shadow connection|textbf}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\MC}{\mathrm{MC}}
 \providecommand{\Sh}{\mathrm{Sh}}
 \providecommand{\Tr}{\operatorname{Tr}}
diff --git a/chapters/connections/feynman_connection.tex b/chapters/connections/feynman_connection.tex
index 20c6759dc290b513a7dec937e875a2d2a768a072..9eab03a5bf282f1c12698fe6160bfd27c1c73d71
--- a/chapters/connections/feynman_connection.tex
+++ b/chapters/connections/feynman_connection.tex
@@ -3,20 +3,20 @@
 is a sum over trees weighted by propagators $\eta_{ij} = d\log(z_i - z_j)$,
 the degree counts vertices, and iterated residues on
 Fulton--MacPherson boundary strata play the role of UV divergences.
-The similarity is striking enough to demand an answer: is the bar
+The similarity raises a precise question: is the bar
 complex a literal reformulation of perturbative QFT, or only a
 structural analogy?
 
 The honest answer distinguishes two regimes. For the Heisenberg
 algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$, the bar complex
 reproduces the free-boson residue calculus exactly, and
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records the
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records the
 expected all-genera path-integral identification. For interacting
 theories, Volume~I proves only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package; the general perturbative
 comparison remains conjectural
-\textup{(}Conjecture~\ref{conj:bar-cobar-path-integral}\textup{)}.
+\textup{(}Conjecture~\ref{conj:v1-bar-cobar-path-integral}\textup{)}.
 The Feynman--bar mnemonic (Remark~\ref{rem:feynman-bar-bridge})
 identifies propagator $= \eta_{ij}$, vertex $=$ collision residue,
 and UV divergence $=$ FM boundary stratum; it does \emph{not}
@@ -134,7 +134,7 @@
 
 \section{Path integral = bar complex}
 
-\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}
+\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral-heisenberg}
 For the Heisenberg vertex algebra $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$
 \textup{(}free boson at nonzero Heisenberg level\textup{)} on a
 compact Riemann surface $\Sigma_g$ of genus~$g \geq 0$:
@@ -178,14 +178,14 @@
 cohomology~\cite{CG17}.
 \end{remark}
 
-\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral}
+\begin{conjecture}[Bar-cobar as worldsheet path integral: general case; \ClaimStatusConjectured]\label{conj:v1-bar-cobar-path-integral}
 For a general chiral algebra $\cA$ on $\Sigma_g$, the generating functional of correlation functions is classified by the bar complex:
 \begin{equation}
 \exp\left( \sum_{g,n} \frac{1}{n!} \int_{C_n(\Sigma_g)} \langle a(z_1) \cdots a(z_n) \rangle_g \right) = \det(\mathbf{1} + \bar{B}(\cA))
 \end{equation}
 where the right side is the Fredholm determinant of the bar complex.
 Evidence is strongest for $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera
-\textup{(}Conjecture~\textup{\ref{conj:bar-cobar-path-integral-heisenberg})};
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-cobar-path-integral-heisenberg})};
 conjectural for interacting $\cA$.
 Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.
 \end{conjecture}
@@ -201,11 +201,11 @@
 \end{remark}
 
 \begin{remark}[Scope of the bar-path-integral comparison]\label{rem:bar-path-integral-scope}
-Conjecture~\ref{conj:bar-cobar-path-integral-heisenberg} records
+Conjecture~\ref{conj:v1-bar-cobar-path-integral-heisenberg} records
 the expected bar-complex/path-integral identification for
 $\mathcal{H}_{\kappa^{\mathrm{Heis}}}$ at all genera. For interacting chiral algebras $\cA$, only the
 genus-$0$ algebraic BRST/bar comparison on the Kac--Moody locus and
 the local binary/ternary reduction package are proved in this volume
 (Theorem~\ref{thm:brst-bar-genus0}); the all-genera comparison is
-Conjecture~\ref{conj:bar-cobar-path-integral}.
+Conjecture~\ref{conj:v1-bar-cobar-path-integral}.
 \end{remark}
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 4a0f3d75135a7a1bb1b6c164f8ef2afa16ff7d8a..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1174,7 +1174,7 @@
  to~$\cA$. With the correct large transversal boundary condition, the
  boundary chiral algebra of the KK-reduced HT theory identifies with the
  universal defect algebra of the parent theory~\cite{GZ26};
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
 \item \emph{Line-side algebraic model.}
  $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$ is the algebraic
  meromorphic line-side model, with the meromorphic tensor/OPE package
@@ -1201,7 +1201,7 @@
  (Definition~\ref{def:shadow-postnikov-tower}).
  Note: $\Theta_\cA$ itself is proved; the conjectural content of
  this definition is the HT holographic packaging, the assertion
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
  system.
 \item \emph{Modular shadow connection.}
  $\nabla^{\mathrm{hol}}_{g,n}$ is the flat connection on derived
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -2656,8 +2657,8 @@
 propagates the quartic to the quintic, producing a class in
 $E_2^{3,*}$ controlled by the $WW$-OPE at sixth-order pole.
 
-The spectral sequence for $\mathcal W_3$ is strictly richer
-than for Virasoro: the deformation space is $2$-dimensional
+The spectral sequence for $\mathcal W_3$ carries more data
+than in the Virasoro case: the deformation space is $2$-dimensional
 ($T$ and $W$ directions), the genus-$1$ Hessian is a
 $2\times 2$ matrix
 (Computation~\ref{comp:w3-genus1-hessian}),
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/genus1_seven_faces.tex b/chapters/connections/genus1_seven_faces.tex
index 8b9ffead0e7be3e025c5a1a3bc828f749b5673f3..0bade4d1a868682328cd2263033a360c253ed41f
--- a/chapters/connections/genus1_seven_faces.tex
+++ b/chapters/connections/genus1_seven_faces.tex
@@ -639,7 +639,7 @@
 spectral curves, and the Hitchin Hamiltonians restrict to the
 elliptic Gaudin Hamiltonians on the trivial $G$-bundle. The
 identification of the collision residue with the Hitchin system at
-genus~$1$ is a shadow of the deeper identification at genus~$g \geq 2$,
+genus~$1$ is a shadow of the corresponding genus-$g \geq 2$ identification,
 where the collision residue on $\Sigma_g$ produces the Hitchin
 Hamiltonians on $\mathrm{Bun}_G(\Sigma_g)$. This genus~$\geq 2$
 extension is the content of the holographic modular Koszul datum
@@ -1133,7 +1133,7 @@
 
 \begin{remark}[The $B$-cycle as genus-$1$ Face~$0$]
 \label{rem:g1sf-b-cycle-face-0}
-The $B$-cycle monodromy is a fundamentally genus-$1$ phenomenon: it
+The $B$-cycle monodromy is a genus-$1$ phenomenon: it
 has no genus-$0$ counterpart. One may view it as a ``Face~$0$'' of
 the genus-$1$ collision residue: the quantum group parameter $q$ is
 an invariant of the elliptic curve that does not appear in any of the
diff --git a/chapters/connections/genus_complete.tex b/chapters/connections/genus_complete.tex
index 5755c0728b45feb9c1dd8bfa6a073295e6c42564..b3ee091cd816d01fc039146fb6e441e420ae84a2
--- a/chapters/connections/genus_complete.tex
+++ b/chapters/connections/genus_complete.tex
@@ -258,7 +258,7 @@
 
 The scalar genus tower
 $F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$ (Theorem~\ref{thm:modular-characteristic}) is the
-\emph{first Chern class} of a categorically richer object.
+\emph{first Chern class} of a chain-level modular functor.
 The bar complex refines the classical modular-functor
 formalism (Segal, Bakalov--Kirillov) to cochain complexes with
 $A_\infty$-morphisms as structure maps, and it is this
@@ -486,12 +486,12 @@
 \cite{Eyn04,CEO06,EO07}.
 
 \item[\textup{(b)}] \textup{[\ClaimStatusConditional{}, conditional on
-Conjecture~\textup{\ref{conj:bar-worldline}}; separated from the surrounding conjecture]}
+Conjecture~\textup{\ref{conj:v1-bar-worldline}}; separated from the surrounding conjecture]}
 \emph{Koszul chiral algebras.} For a Koszul chiral
 algebra~$\mathcal{A}$, the bar complex correlation functions
 satisfy the EO recursion (see proof below), conditional on the
 propagator--bidifferential correspondence
-\textup{(}Conjecture~\textup{\ref{conj:bar-worldline}},
+\textup{(}Conjecture~\textup{\ref{conj:v1-bar-worldline}},
 \ClaimStatusHeuristic\textup{)}.
 
 \item[\textup{(c)}] \textup{[\ClaimStatusConjectured]}
@@ -514,7 +514,7 @@
 $x\colon S \to \mathbb{P}^1$; the bidifferential
 $\omega_{0,2} = B$ is the Bergman kernel on~$S$, identified with
 the genus-$0$ propagator $G_0(z,w) = 1/(z-w)$ via
-Conjecture~\ref{conj:bar-worldline}. The Koszul property (quadratic
+Conjecture~\ref{conj:v1-bar-worldline}. The Koszul property (quadratic
 OPE relations) ensures that $S$ is a branched cover with finitely
 many ramification points.
 
@@ -597,7 +597,7 @@
 Theorem~\ref{thm:mk-general-structure} (Feynman transform = graph sum)
 with the abstract topological recursion framework.
 The spectral curve identification in Step~1 invokes
-Conjecture~\ref{conj:bar-worldline} (\ClaimStatusHeuristic) for the
+Conjecture~\ref{conj:v1-bar-worldline} (\ClaimStatusHeuristic) for the
 propagator--bidifferential correspondence; the remaining
 steps are unconditional.
 
@@ -747,8 +747,8 @@
 \label{subsec:holographic-dictionary}
 \index{holographic dictionary!chain-level}
 
-The chain-level modular functor of the preceding subsection carries a
-natural holographic interpretation: the bulk algebra is recovered as
+The chain-level modular functor of the preceding subsection admits a
+holographic interpretation: the bulk algebra is recovered as
 the derived center of the boundary, and factorization homology produces
 genus-graded state spaces equipped with a modular partition function.
 The complete packaging of these ingredients (bulk algebra, Koszul-dual
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index a1d74cab1a38583102e66a56a4081551558558bc..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -21,7 +21,7 @@
 convention, and a different proof of consistency. This chapter
 proves that all seven incarnations agree, on the nose, as elements
 of the same convolution dg~Lie algebra. The seven-face master
-theorem is the centrepiece of Part~\ref{part:standard-landscape}: it asserts that the
+theorem is the main theorem of Part~\ref{part:standard-landscape}: it asserts that the
 collision residue is a basis-independent invariant of the chiral
 algebra, computable from any one of the seven frameworks and equal in
 all of them. When two faces disagree, both are wrong.
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
@@ -1174,7 +1178,7 @@
 same object.
 \end{remark}
 
-The seven-face programme is the centrepiece of Part~\ref{part:standard-landscape} precisely
+The seven-face programme is a core result of Part~\ref{part:standard-landscape}
 because it converts the abstract claim ``the bar-intrinsic MC
 element is universal'' into a concrete checklist: seven frameworks,
 seven independent computations, one mathematical object. When the
diff --git a/chapters/connections/outlook.tex b/chapters/connections/outlook.tex
index 99013503ddd7427273398080bedb1a787993f810..a2923a93e36e9ba2d80817c3d9556d3219f782fd
--- a/chapters/connections/outlook.tex
+++ b/chapters/connections/outlook.tex
@@ -1,5 +1,5 @@
 % ======================================================================
-% OUTLOOK — Replaces concordance + editorial_constitution in the
+% OUTLOOK: replaces concordance + editorial_constitution in the
 % monograph proper. Contains the mathematical architecture (three
 % pillars, three rings, five main theorems) and key definitions
 % referenced from theory chapters. The full concordance with
@@ -570,7 +570,7 @@
 graph sum, not from the spectral curve of the integrable hierarchy.
 This separation (integrable on the diagonal, non-integrable
 off-diagonal) instantiates the principle that the shadow obstruction
-tower is richer than the KdV hierarchy
+tower extends beyond the KdV hierarchy
 (Remark~\ref{rem:shadow-multiplicative-deformation}).
 
 \subsection{D-module purity: the BPZ Hitchin connection}
@@ -643,7 +643,7 @@
 \label{sec:concordance-arithmetic-sewing}
 
 % ======================================================================
-% Additional stub labels — these were defined in the full concordance
+% Additional stub labels: these were defined in the full concordance
 % and editorial constitution, and are referenced from other chapters.
 % The full definitions appear in the editorial companion (make editorial).
 % ======================================================================
diff --git a/chapters/connections/poincare_computations.tex b/chapters/connections/poincare_computations.tex
index 6bd049a1e11f38d0f2ba79097beeafd8a75ddfe1..440eab53082e73af75b0a31cd934c6cff69e52ad
--- a/chapters/connections/poincare_computations.tex
+++ b/chapters/connections/poincare_computations.tex
@@ -104,7 +104,7 @@
 This is pure NAP duality: Verdier duality on the factorization algebra associated to the \emph{same} chiral algebra on the orientation-reversed curve. The Langlands dual $\mathfrak{g}^\vee$ enters separately, through the Feigin--Frenkel theorem:
 
 \emph{The geometric Langlands connection.}
-The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a deeper phenomenon than NAP duality.
+The Feigin--Frenkel theorem identifies $\mathcal{Z}(\widehat{\mathfrak{g}}_{-h^\vee})$ with ${}^L\mathfrak{g}$-opers, providing a bridge to the Langlands dual; $\widehat{\mathfrak{g}}_{-h^\vee}$ describes D-modules on $\text{Bun}_G(X)$; and the geometric Langlands correspondence (conjecturally) relates D-modules on $\text{Bun}_G(X)$ to those on $\text{Bun}_{G^\vee}(X)$, a different phenomenon from NAP duality.
 
 \begin{conjecture}[Critical-level affine \texorpdfstring{$\to$}{to} Yangian bridge;
 \ClaimStatusConjectured]\label{conj:critical-affine-yangian}
diff --git a/chapters/connections/semistrict_modular_higher_spin_w3.tex b/chapters/connections/semistrict_modular_higher_spin_w3.tex
index feeef06da441c900b91c3bd743abe3487ba64720..5c0120fcf5f84d772751f12705ec4d52887f2b5a
--- a/chapters/connections/semistrict_modular_higher_spin_w3.tex
+++ b/chapters/connections/semistrict_modular_higher_spin_w3.tex
@@ -5,9 +5,9 @@
 \chapter{Semistrict modular higher-spin geometry of the classical \texorpdfstring{$W_3$}{W3} sector}
 \label{chap:semistrict-modular-W3}
 
-% ----------------------------------------------------------------------
+% ======================================================================
 % Local macros: provided only if absent from the ambient manuscript.
-% ----------------------------------------------------------------------
+% ======================================================================
 \providecommand{\Bbbk}{\mathbb{k}}
 \providecommand{\MC}{\operatorname{MC}}
 \providecommand{\HS}{\operatorname{HS}}
@@ -28,7 +28,7 @@
 \section{Why this chapter exists}
 \label{sec:why-semistrict-modular-W3}
 
-The nearest route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures survive intact. Among the three natural targets (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first where the mathematics is simultaneously nonlinear, explicit, finite-valent, and recognizably gravitational.
+The first route from the proved modular Koszul core to quantum gravity passes through protected sectors where chiral, holomorphic-topological, and factorization structures remain available. Among the three target settings (twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4}, celestial holography, and \texorpdfstring{AdS$_3$}{AdS3} higher-spin gravity), the classical $W_3$ sector is the first one where the mathematics is nonlinear, explicit, and finite-valent.
 
 A boundary algebra determines a bulk deformation problem, and the complexity of the boundary nonlinearity controls the degree of the bulk homotopy algebra. For the classical $W_3$ Poisson vertex algebra, the nonlinearity is quadratic and the bulk is therefore semistrict. Once this is made precise, the higher-genus modular problem reduces from an unbounded infinity of coherence relations to a filtered cubic recursion around a canonical central Maurer--Cartan base point.
 
@@ -66,7 +66,7 @@
  \item The boundary-to-bulk dictionary is present in the holomorphic-topological literature: boundary chiral algebras, higher operations, and homotopy transfer are developed in~\cite{CDG20,Zeng23,GKW24}.
  \item The bulk retains enough gravity-like structure to deserve the name ``higher-spin gravitational sector,'' while remaining rigid enough to admit proofs.
 \end{enumerate}
-The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are natural companion directions, but the $W_3$ sector is the correct first test because one can prove theorems.
+The twisted \texorpdfstring{AdS$_5$/CFT$_4$}{AdS5/CFT4} and celestial targets are parallel directions, but the $W_3$ sector is the first one handled here because it admits proofs.
 \end{remark}
 
 \section{From boundary \texorpdfstring{$\lambda$}{lambda}-brackets to bulk semistrictity}
diff --git a/chapters/connections/thqg_entanglement_programme.tex b/chapters/connections/thqg_entanglement_programme.tex
index fd4ff0eab4296fd4f4efae3d8ce67d4f5342d31e..3e56affb93df47d3194f41ccf3a6bb9c96087260
--- a/chapters/connections/thqg_entanglement_programme.tex
+++ b/chapters/connections/thqg_entanglement_programme.tex
@@ -3,19 +3,19 @@
 % ===========================================================================
 %
 % Beilinson-audited rewrite (2026-03-30). Fixes from first draft:
-% F1: Entanglement rank replaced — direct sum ≠ tensor product.
+% F1: Entanglement rank replaced; direct sum ≠ tensor product.
 % Tensor product comes from SEWING (open/closed), not Lagrangian split.
 % F2: Replica genus formula corrected: ng (Riemann-Hurwitz), not n(g-1)+1.
-% F3: Tomita-Takesaki downgraded — anti-linearity needs unitarity structure.
+% F3: Tomita-Takesaki downgraded; anti-linearity needs unitarity structure.
 % F4: Page constraint stated purely in dimensional terms (proved),
 % not in terms of S_EE (heuristic).
 % F5: Error correction framed as structural analogy, not literal QECC.
 % F6: Citation key Engelhardt-Wall14 (not 15).
 %
 % Status hierarchy:
-% ProvedHere — follows from the existing proved core
-% Conjectured — well-motivated, precise, falsifiable
-% Heuristic — structural identification, not yet a theorem
+% ProvedHere: follows from the existing proved core
+% Conjectured: well-motivated, precise, falsifiable
+% Heuristic: structural identification, not yet a theorem
 
 \section{The entanglement programme: quantum information from the shadow obstruction tower}
 \label{sec:thqg-entanglement-programme}
diff --git a/chapters/connections/thqg_open_closed_realization.tex b/chapters/connections/thqg_open_closed_realization.tex
index df10e954356b8abf355f27e06cc07065d5039796..92d9688167055326e0edcc7ef65322fa3d9f63c8
--- a/chapters/connections/thqg_open_closed_realization.tex
+++ b/chapters/connections/thqg_open_closed_realization.tex
@@ -37,11 +37,11 @@
 the gravitational input (Definition~\ref{def:thqg-standing-hypotheses}).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The chiral endomorphism operad and the algebraic derived center}
 \label{subsec:thqg-chiral-endomorphism-operad}
 \index{chiral endomorphism operad|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The geometric chiral Hochschild complex of
 Definition~\ref{def:chiral-hochschild} lives on FM
@@ -354,11 +354,11 @@
 Definition~\ref{def:thqg-chiral-derived-center}.
 \end{definition}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The universal open/closed pair}
 \label{subsec:thqg-universal-oc-pair}
 \index{universal open/closed pair|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Local chiral open/closed pair]
 \label{def:thqg-local-oc-pair}
@@ -516,11 +516,11 @@
 (bulk-to-boundary $\mathsf{SC}$ operations).
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{Restriction from global to local: the bordered FM bridge}
 \label{subsec:thqg-bordered-fm-bridge}
 \index{bordered FM bridge|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The bordered FM compactification
 $\overline{C}{}^{\,\mathrm{oc}}_{k,\vec{m}}(X, D, \tau)$
@@ -622,12 +622,12 @@
 of~\eqref{eq:thqg-derived-center-three-term}.
 \end{corollary}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The annulus trace: first modular shadow of the open sector}
 \label{subsec:thqg-annulus-trace}
 \index{annulus trace|textbf}
 \index{Hochschild homology!as open trace|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Annulus trace theorem; \ClaimStatusProvedHere]
 \label{thm:thqg-annulus-trace}
@@ -941,11 +941,11 @@
 \lambda_1$, as claimed.
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed MC element}
 \label{subsec:thqg-oc-mc-element}
 \index{Maurer--Cartan element!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed MC element]
 \label{constr:thqg-oc-mc-element}
@@ -1030,11 +1030,11 @@
 (Type IV faces).
 \end{proof}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The open/closed projection principle}
 \label{subsec:thqg-oc-projection}
 \index{projection principle!open/closed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{theorem}[Open/closed projection principle; \ClaimStatusProvedHere]
 \label{thm:thqg-oc-projection}
@@ -1210,12 +1210,12 @@
 \end{enumerate}
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{CT-2: the modular cooperad conjecture for the open sector}
 \label{subsec:thqg-ct2-cooperad-conjecture}
 \index{CT-2 conjecture|textbf}
 \index{modular cooperad!open sector|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
 carries cocomposition maps read off from clutching on bordered
@@ -1376,11 +1376,11 @@
 obstructed by any geometric or chain-level computation.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The first nonlinear open/closed invariant}
 \label{subsec:thqg-nonlinear-oc-invariant}
 \index{open/closed invariant!nonlinear|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{construction}[Open/closed quartic resonance class]
 \label{constr:thqg-oc-quartic-resonance}
@@ -1526,11 +1526,11 @@
 where the boundary shadow obstruction tower degenerates.
 \end{remark}
 
-% -------------------------------------------------------------------
+% ===================================================================
 \subsection{The modular Koszul datum, completed}
 \label{subsec:thqg-platonic-completed}
 \index{platonic datum!completed|textbf}
-% -------------------------------------------------------------------
+% ===================================================================
 
 \begin{definition}[Completed modular Koszul datum]
 \label{def:thqg-completed-platonic-datum}

tokens used
146,485
