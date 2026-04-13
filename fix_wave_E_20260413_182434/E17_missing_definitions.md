# E17_missing_definitions (609s)

Findings and fixes:

- PROBLEM at [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:433): `\mathrm{or}_{p+1}^{(g)}` appeared in the preview definition before the object itself was explained. EXACT edit applied: changed `orientation bundle \mathrm{or}_{p+1}^{(g)}, is given in...` to `orientation bundle \mathrm{or}_{p+1}^{(g)}, the sign line that records orientations of the codimension-$p$ collision strata at genus~$g$, is given in...`.

- PROBLEM at [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:574): `\epsilon_{\mathrm{geom}}(D_{ij})` was used before its meaning was stated. EXACT edit applied: replaced `where \epsilon_{\text{geom}}(D_{ij}) = 0 or 1 depending on orientation convention` with `where \epsilon_{\text{geom}}(D_{ij}) \in \{0,1\} is the parity of the boundary orientation of the collision divisor~D_{ij}; the full sign package is fixed in Convention~\ref{conv:orientations-enhanced}.`

- PROBLEM at [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:1519): `conilpotent dg coalgebras` was invoked in the proof before the chapter explained the term. EXACT edit applied: inserted the inline gloss `(that is, dg coalgebras whose iterated reduced coproduct vanishes on every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})`.

- PROBLEM at [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:16): the opening overview used `\barB(\cA)`, “conilpotent chiral coalgebra”, and `\Omega^{\mathrm{ch}}(\cC)` before local definition. EXACT edit applied: inserted an opening paragraph at lines 4-14 beginning `\smallskip\noindent\textit{Opening notation.}` that defines those three objects informally and points to Definitions `\ref{def:factorization-coalgebra}`, `\ref{def:conilpotent-cobar}`, and `\ref{def:geom-cobar-intrinsic}`.

- PROBLEM at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:67): the overview invoked `(\cA,\cC,\tau,F_\bullet)`, `K_\tau^L`, `K_\tau^R`, `\Theta_\cA^{\le r}`, and “chiral Koszul pair” before local introduction. EXACT edit applied: inserted a standing-notation paragraph at lines 61-75 beginning `\smallskip\noindent\textit{Standing notation for the overview.}` that defines the twisting datum, the twisted tensor products, the truncations `\Theta_\cA^{\le r}`, and the informal meaning of a chiral Koszul pair before the overview uses them.

Verification: I re-ran a targeted forward-definition pass on the three assigned files. The remaining forward references are deliberate pointers to later formal definitions or comments, not surviving use-before-introduction violations. I did not run a full TeX build.


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
session id: 019d87db-bd9d-7823-86ec-dfcf320b96eb
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


Find objects used before definition in Vol I theory chapters.
Read chapters/theory/bar_construction.tex, cobar_construction.tex, chiral_koszul_pairs.tex.
For each \ macro or symbol: is it defined before first use? Flag define-before-use violations.
mcp startup: no servers
codex
I’m auditing define-before-use across the three assigned theory chapters and will repair only those files. First I’m loading the required repo-wide context plus the target chapters, then I’ll trace first uses against local definitions and patch the minimum truthful fixes.
collab spawn_agent(call_a5u7eytnwPF2EkiMwvcCcXm1, prompt="Read and summarize only the instructions that materially affect this task from these files: CLAUDE.md, chapters/connecti…")
mcp startup: no servers
spawn_agent(call_a5u7eytnwPF2EkiMwvcCcXm1, prompt="Read and summarize only the instructions that materially affect this task from these files: CLAUDE.md, chapters/connecti…") pending init:
  agent: 019d87dc-010c-7b53-b380-05cc56cb78cc
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar
Plan update
Starting with required context and a targeted audit of the three assigned theory chapters for define-before-use violations, then I’ll patch only those files and verify no new violations were introduced.
  → Load required repo context and audit target chapters for define-before-use violations
  • Patch only the assigned theory chapters with minimum truthful edits
  • Verify the repaired surfaces and summarize each finding with exact edit applied
Plan update
  → Inspect constitutional instructions (CLAUDE.md, concordance, theorem registry, red team summary) for items affecting task, and summarize key directives
  • Review chapters/theory/bar_construction.tex, cobar_construction.tex, chiral_koszul_pairs.tex for define-before-use issues and note occurrences
  • Compile findings and craft final response referencing specific sections and line numbers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

codex
I’ve started the audit. Next I’m reading the audit workflow and the required repo-wide sources, then I’ll walk each chapter in order to pin down first-use and local-definition boundaries before editing.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

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

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

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
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\newcommand\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\newcommand' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

codex
The global context is loaded. I’m on the target surface now, checking each chapter as a local theory text rather than trusting global macros, because the failure mode here is object introduction order inside the chapter itself.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,320p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{The geometric cobar complex}
\label{chap:cobar-construction}

The bar functor destroys the algebra: it encodes~$\cA$ as a
factorization coalgebra $\barB(\cA)$ from which no multiplication
is directly visible. The cobar complex $\Omega(\cC)$ is the
reconstruction machine that recovers~$\cA$ from this coalgebraic
residue, realizing the inversion
$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ (Theorem~B) and
proving that the MC element
$\Theta_\cA \in \MC(\gAmod)$ determines~$\cA$ up to
quasi-isomorphism on the Koszul locus. Both functors are
projections of a single universal twisting morphism
$\tau \in \MC\bigl(\operatorname{Conv}(\cC, \cA)\bigr)$
(Definition~\ref{def:twisting-morphism}): bar records collision
residues via the logarithmic propagator
$\eta_{ij} = d\log(z_i - z_j)$; cobar integrates distributional
duals over the open configuration space $C_n(X)$.
The duality between them (residues versus delta functions,
$j_*$ versus $j_!$) is the Verdier exchange on
 succeeded in 51ms:
\chapter{The geometric bar complex}
\label{chap:bar-cobar}
\label{chap:bar-construction}


\index{bar construction!as integral transform|textbf}
\index{non-abelian Fourier transform|textbf}

An augmented algebra has exactly one piece of canonical structure beyond
its multiplication: the augmentation ideal $\bar\cA = \ker(\varepsilon)$,
the part that the counit forgets.
Desuspend it to shift the grading, then form the cofree
nilpotent coalgebra $T^c(s^{-1}\bar\cA)$ with deconcatenation coproduct.
This object is not a choice; it is the \emph{universal} recipient
of coderivations built from the algebra structure maps, and the
bar differential is the unique coderivation that encodes them all.
The entire construction is forced: given $\cA$ and $\varepsilon$, the
coalgebra $B(\cA)$ exists, its differential squares to zero,
and every deformation-theoretic invariant of $\cA$ is a projection
from the resulting Maurer--Cartan element.
 succeeded in 51ms:
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
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{The geometric bar complex}
\label{chap:bar-cobar}
\label{chap:bar-construction}


\index{bar construction!as integral transform|textbf}
\index{non-abelian Fourier transform|textbf}

An augmented algebra has exactly one piece of canonical structure beyond
its multiplication: the augmentation ideal $\bar\cA = \ker(\varepsilon)$,
the part that the counit forgets.
Desuspend it to shift the grading, then form the cofree
nilpotent coalgebra $T^c(s^{-1}\bar\cA)$ with deconcatenation coproduct.
This object is not a choice; it is the \emph{universal} recipient
of coderivations built from the algebra structure maps, and the
bar differential is the unique coderivation that encodes them all.
The entire construction is forced: given $\cA$ and $\varepsilon$, the
coalgebra $B(\cA)$ exists, its differential squares to zero,
and every deformation-theoretic invariant of $\cA$ is a projection
from the resulting Maurer--Cartan element.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\newcommand' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'wc -l chapters/theory/bar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\def' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    2391 chapters/theory/bar_construction.tex
 succeeded in 51ms:
    6565 chapters/theory/chiral_koszul_pairs.tex
 succeeded in 52ms:
    3454 chapters/theory/cobar_construction.tex
collab wait(call_IkV1BjOEC2js6Hf96f7IS5ft)
  receivers: 019d87dc-010c-7b53-b380-05cc56cb78cc
 exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\dfib\" -n chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\gAmod\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\gAmod)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\gAmod' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
36:$\Theta_\cA \in \MC(\gAmod)$ governing the genus expansion,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\begin{definition}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\begin{definition})
               ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\begin\\{definition\\}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
311:\begin{definition}[Bar as factorization homology]\label{def:bar-fh}
424:\begin{definition}[Genus-graded geometric bar complex, preliminary form]
509:\begin{definition}[Bar differential]\label{def:bar-differential-complete}%
1408:\begin{definition}[Orientation line bundle]\label{def:orientation}
1715:\begin{definition}[Genus-graded geometric bar complex]\label{def:geom-bar}
1745:\begin{definition}[Internal differential]
1758:\begin{definition}[Factorization differential]\label{def:diff-fact}
1839:\begin{definition}[Configuration differential]
2259:\begin{definition}[Conilpotent chiral coalgebra]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '280,360p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{example}[OPE as residue: the Heisenberg current]\label{ex:ope-to-residue}
The Heisenberg current $J(z)$ with OPE $J(z)J(w) = k/(z-w)^2 + \text{reg.}$ gives the bar element $J(z_1) \otimes J(z_2) \otimes \eta_{12} \in \bar{B}^1(\mathcal{H})$, where $\eta_{12} = d\log(z_1 - z_2)$. The bar differential extracts the full chiral product~$\mu$ (Convention~\ref{conv:product-vs-bracket}): since $J_{(0)}J = 0$ (no simple pole) and $J_{(1)}J = k$ (double pole), the result is
\[
d_{\mathrm{res}}(J \otimes J \otimes \eta_{12}) = k \cdot \mathbf{1}.
\]
The entire bar differential comes from the curvature component $d_{\mathrm{curvature}}$ (Proposition~\ref{prop:pole-decomposition}). One must not multiply the OPE pole by the propagator~$\eta_{12}$ and take a combined residue; the logarithmic form accounts for the bar degree, not an additional pole (Computation~\ref{comp:deg1-general}).
\end{example}

\begin{remark}[Logarithmic forms are forced]\label{rem:why-log-forced}
Three requirements distinguish logarithmic forms $\eta_{ij} = d\log(z_i - z_j)$ among meromorphic 1-forms with poles along diagonals, and together determine them uniquely.

\emph{Conformal invariance.}
Under a conformal transformation $z \mapsto f(z)$, a direct computation gives
$d\log(f(z_i) - f(z_j)) = \frac{f'(z_i)dz_i - f'(z_j)dz_j}{f(z_i) - f(z_j)}$,
which near the diagonal $z_i \approx z_j$ reduces to $(dz_i - dz_j)/(z_i - z_j)$
by cancellation of $f'$. Thus $\eta_{ij}$ is conformally invariant up to regular terms.

\emph{Well-defined residues.}
The residue $\operatorname{Res}_{D_{ij}}$ requires a \emph{simple pole} along $D_{ij}$: forms with higher-order poles (e.g.\ $dz_i/(z_i - z_j)^2$) do not admit canonical residues. A logarithmic form $\omega = \frac{df}{f} \wedge \alpha + \beta$ with $f = z_i - z_j$ has $\operatorname{Res}_{D_{ij}}(\omega) = \alpha|_{D_{ij}}$, which is canonical.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\DeclareMathOperator' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

wait(call_IkV1BjOEC2js6Hf96f7IS5ft) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\NewDocumentCommand' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\providecommand' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '380,460p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
on~$C_2(\mathbb{P}^1)$, the bar differential is nilpotent
($\dzero^2 = 0$), and the monodromy is trivial. At
genus~$g \geq 1$, the logarithm $d\log E(z_i,z_j)$ acquires
monodromy around the $B$-cycles of~$\Sigma_g$, the fiberwise bar
differential fails nilpotence by
$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, and the curvature
$\kappa(\cA)$ is the \emph{infinitesimal generator} of this
monodromy: the residue at the branch point of the logarithm.
This is the chiral Riemann--Hilbert correspondence: the nilpotent
datum~$\kappa$ determines the periodic datum (the monodromy of the
bar family over~$\overline{\mathcal{M}}_g$) via exponentiation.

The four theorems are four aspects of this correspondence:
Theorem~A asserts that the categorical logarithm and exponential
exist; Theorem~B that they are mutually inverse on the
convergence domain (the Koszul locus); Theorem~C that the failure
off the convergence domain decomposes into complementary
Lagrangians (the branch structure of the logarithm); and
Theorem~D that the leading coefficient~$\kappa(\cA)$ of the
logarithm determines the genus expansion
codex
The three target chapters are large enough that a manual skim will miss first-use errors. I’m switching to a structured pass: locate local introduction points (`define`, `write`, `denote`, definitions/conventions) and compare them to earlier occurrences of the same symbols before I patch.
collab wait(call_Aac4VKwHB7wgPuTgn3FNWb0R)
  receivers: 019d87dc-010c-7b53-b380-05cc56cb78cc
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\bar\\{B\\}\\"'^{'"\\\\text\\{geom\\}}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\bar\{B\}\^{\\text\{geom\}})
                    ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\bar\\{B\\}\\"'^'"\\{\\\\text\\{geom\\}\\}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
315:\[\bar{B}^{\text{geom}}_n(\mathcal{A}) = \int_{\overline{C}_{n+1}(X)/X} \mathcal{A}\]
345:\[H_*(\bar{B}^{\text{geom}}(\mathcal{A})) \cong \int_{C_*(X)} \mathcal{A}\]
349:The coalgebra structure on $\bar{B}^{\text{geom}}(\mathcal{A})$ arises from the coproduct in factorization homology:
1450:\[\bar{B}^{\text{geom}}: \mathsf{ChirAlg}_X^{\mathrm{aug}} \to \mathsf{dgCoalg}_X\]
1453:\item \emph{Well-defined on objects:} For each augmented chiral algebra $\mathcal{A}$, $\bar{B}^{\text{geom}}(\mathcal{A})$ is a differential graded coalgebra
1454:\item \emph{Well-defined on morphisms:} For each morphism $f: \mathcal{A} \to \mathcal{B}$ of augmented chiral algebras, there is an induced coalgebra morphism $\bar{B}^{\text{geom}}(f): \bar{B}^{\text{geom}}(\mathcal{A}) \to \bar{B}^{\text{geom}}(\mathcal{B})$
1455:\item \emph{Preserves identities:} $\bar{B}^{\text{geom}}(\text{id}_\mathcal{A}) = \text{id}_{\bar{B}^{\text{geom}}(\mathcal{A})}$
1456:\item \emph{Preserves composition:} $\bar{B}^{\text{geom}}(g \circ f) = \bar{B}^{\text{geom}}(g) \circ \bar{B}^{\text{geom}}(f)$
1535:\[\Delta: \bar{B}^{\text{geom}}(\mathcal{A}) \to \bar{B}^{\text{geom}}(\mathcal{A}) \otimes \bar{B}^{\text{geom}}(\mathcal{A})\]
1676:The bar complex $\bar{B}^{\text{geom}}(\mathcal{A})$ with:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\bar\\{B\\}\\"'^'"\\{\\(g\\)' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
428:\[\bar{B}^{(g),n}(\mathcal{A}) = \Gamma\left(\overline{C}_{n+1}^{(g)}(\Sigma_g), j_*j^*\mathcal{A}^{\boxtimes(n+1)} \otimes \Omega^n(\log D^{(g)})\right)\]
430:$\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
455:A global section $\alpha \in \bar{B}^{(g),n}(\mathcal{A})$ is a ``correlation function'':
1718:\bar{B}^{(g)}_{p,q}(\mathcal{A}) = \Gamma\left(\overline{C}_{p+1}(\Sigma_g), j_*j^*\mathcal{A}^{\boxtimes(p+1)} \otimes \Omega^q_{\overline{C}_{p+1}(\Sigma_g)}(\log D^{(g)}) \otimes \text{or}_{p+1}^{(g)}\right)
1730:\[\bar{B}(\mathcal{A}) = \bigoplus_{g=0}^{\infty} \bar{B}^{(g)}(\mathcal{A})\]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '500,580p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\emph{Dimension.} 
\[\dim \bar{B}^{(0),2}(\mathcal{A}) = N^3 \cdot 2\]

This grows rapidly with $n$.
\end{example}

\subsubsection{The bar differential}

\begin{definition}[Bar differential]\label{def:bar-differential-complete}%
\label{def:geometric-bar}\label{def:geometric-bar-definition}\label{def:bar-geometric}%
\label{def:bar-diff-detailed}\label{def:diff-total}%
\index{bar complex!differential|textbf}
The bar complex carries a bigrading
$\barB_{p,q}(\cA)$ by \emph{bar degree}~$p$ (number of
desuspended tensor factors minus one) and
\emph{form degree}~$q$. The \emph{cohomological
degree} of a homogeneous element
$s^{-1}\phi_0 \otimes \cdots \otimes s^{-1}\phi_p
\otimes \omega \in \barB_{p,q}$ is
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\barB' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
33:The factorization coalgebra $\barB(\cA) = \mathrm{Sym}^c(s^{-1}\bar\cA)$
43:$\Omega \circ \barB \xrightarrow{\sim} \mathrm{id}$
84:The bar construction $\barB_X(\cA)$ of an augmented chiral
86:$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the bar coalgebra
90:\cA^i \;:=\; H^*(\barB_X(\cA)).
92:Thus $\barB_X(\cA)$, $\cA^i$, and $\cA^!$ are distinct objects.
108:\mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
113:$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
124:its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
129:the symmetric bar $\barB_X(\cA)$) and $\cA^!_{\mathrm{line}}$ (the line
135:$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
142:$\tau \colon \barB_X(\cA) \to \cA$,
145:$\mathfrak{g}_\tau := \Hom(\barB_X(\cA),\, \cA)$ carries a
148:\Delta_{\barB}$ and whose differential is
149:$\partial f = d_\cA \circ f - (-1)^{|f|} f \circ d_{\barB}$.
181:$\barB_X(\cA)$ & factorization coalgebra
183:$\cA^i = H^*(\barB_X(\cA))$ & factorization coalgebra
188:$\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)$
191:$\Omega_X(\barB_X(\cA))$ & chiral algebra
514:$\barB_{p,q}(\cA)$ by \emph{bar degree}~$p$ (number of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\newcommand' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -F \"\\newcommand\" chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{The geometric cobar complex}
\label{chap:cobar-construction}

The bar functor destroys the algebra: it encodes~$\cA$ as a
factorization coalgebra $\barB(\cA)$ from which no multiplication
is directly visible. The cobar complex $\Omega(\cC)$ is the
reconstruction machine that recovers~$\cA$ from this coalgebraic
residue, realizing the inversion
$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ (Theorem~B) and
proving that the MC element
$\Theta_\cA \in \MC(\gAmod)$ determines~$\cA$ up to
quasi-isomorphism on the Koszul locus. Both functors are
projections of a single universal twisting morphism
$\tau \in \MC\bigl(\operatorname{Conv}(\cC, \cA)\bigr)$
(Definition~\ref{def:twisting-morphism}): bar records collision
residues via the logarithmic propagator
$\eta_{ij} = d\log(z_i - z_j)$; cobar integrates distributional
duals over the open configuration space $C_n(X)$.
The duality between them (residues versus delta functions,
$j_*$ versus $j_!$) is the Verdier exchange on
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'geom-cobar-intrinsic' -n chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
30:(Definition~\ref{def:geom-cobar-intrinsic}), where
250:\begin{definition}[Intrinsic geometric cobar complex]\label{def:geom-cobar-intrinsic}
393:(Definition~\ref{def:geom-cobar-intrinsic}) admits a canonical isomorphism:
486:definition (Definition~\ref{def:geom-cobar-intrinsic}) dissolves this
Plan update
Gathered the mandatory instructions from CLAUDE.md, concordance, theorem registry, and red-team summary; will now analyze the three theory files for define-before-use issues.
  ✓ Inspect constitutional instructions (CLAUDE.md, concordance, theorem registry, red team summary) for items affecting task, and summarize key directives
  → Review chapters/theory/bar_construction.tex, cobar_construction.tex, chiral_koszul_pairs.tex for define-before-use issues and note occurrences
  • Compile findings and craft final response referencing specific sections and line numbers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'or_{p+1}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:or_{p+1})
           ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'or_\\{p\\+1\\}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1380,1435p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
\[
\dim H^2(B^{\mathrm{ord}}(\cA))
= \text{number of independent scattering channels},
\]
where the second count records the independent quadratic relations.
For the standard families:
\begin{itemize}
\item Heisenberg: $\dim H^1 = 1$, corresponding to one boson, and
 $\dim H^2 = 0$, reflecting the absence of quadratic interaction
 channels in the free theory.
\item $\widehat{\mathfrak{sl}}_{2,k}$: $\dim H^1 = 3 = \dim \mathfrak{sl}_2$
 and $\dim H^2 = 5$. The degree-$2$ count is $5$, not $6$.
\item $\widehat{\mathfrak{sl}}_{3,k}$: $\dim H^1 = 8 = \dim \mathfrak{sl}_3$
 and $\dim H^2 = 36$. This is the chiral bar value; the
 Chevalley--Eilenberg count gives $20$ and does not include the
 extra chiral Orlik--Solomon contribution.
\end{itemize}
\end{remark}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'conilpotent' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1518:on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
1905: the cofree conilpotent coLie coalgebra on
1915: the cofree cocommutative coassociative conilpotent
1928: the cofree conilpotent coassociative
2255:It defines a functor from chiral algebras to filtered conilpotent chiral coalgebras, with essential image the coalgebras having logarithmic coderivations supported on collision divisors.
2260:A chiral coalgebra $C$ is \emph{filtered conilpotent} if the iterated comultiplication 
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'd_\\{\\\\text\\{config\\}\\}' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1841: \[d_{\text{config}} = d_{\text{config}}^{\text{dR}} + d_{\text{config}}^{\text{Lie*}}\]
1842: where the de~Rham component $d_{\text{config}}^{\text{dR}} = \text{id}_{\mathcal{A}^{\boxtimes(n+1)}} \otimes d_{\text{dR}} \otimes \text{id}_{\text{or}}$ acts on the differential forms, and the Lie$^*$ component $d_{\text{config}}^{\text{Lie*}} = \sum_{I \subset [n+1]} (-1)^{\epsilon(I)} d_{\text{Lie}}^{(I)} \otimes \text{id}_{\Omega^*}$ acts via the Lie$^*$ algebra structure (when present).
1844: For general chiral algebras without Lie* structure, $d_{\text{config}}^{\text{Lie*}} = 0$.
2341:\[d_F(r) = d_{\text{fact}}(r) + d_{\text{config}}(r) + d_{\text{int}}(r)\]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\begin\\{definition\\}' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
149:\begin{definition}[Test function space]\label{def:test-functions}
156:\begin{definition}[Distribution space]\label{def:distributions}
197:\begin{definition}[Conilpotent coalgebra]\label{def:conilpotent-cobar}
223:\begin{definition}[Factorization coalgebra]\label{def:factorization-coalgebra}
250:\begin{definition}[Intrinsic geometric cobar complex]\label{def:geom-cobar-intrinsic}
504:\begin{definition}[Geometric cobar complex]\label{def:geom-cobar}
1858:\begin{definition}[Cobar integration kernel]\label{def:cobar-kernel}
1933:\begin{definition}[Categorical logarithm and exponential]
1979:\begin{definition}[Distribution space]
2138:\begin{definition}[Curved cobar]\label{def:curved-cobar}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'factorization coalgebra' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5:factorization coalgebra $\barB(\cA)$ from which no multiplication
107: coshuffle coproduct ($2^n$ terms; the factorization coalgebra of
116:factorization coalgebra~$\cC$ on~$X$, $\Omegach(\cC)$ is the free
224:\index{factorization coalgebra|textbf}
225:A \emph{factorization coalgebra} on a smooth
245:coalgebra) is a factorization coalgebra, and conversely
389:Let $\mathcal{C}$ be a factorization coalgebra that is conilpotent
3060: factorization coalgebra.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'conilpotent' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
23:Concretely, given a conilpotent chiral
197:\begin{definition}[Conilpotent coalgebra]\label{def:conilpotent-cobar}
198:\index{conilpotent!coalgebra}
201:\emph{conilpotent} if for each element $c \in \cC$,
219:See also Definition~\ref{def:conilpotent-complete} for the
252:Let $\mathcal{C}$ be a conilpotent chiral coalgebra on a smooth algebraic
389:Let $\mathcal{C}$ be a factorization coalgebra that is conilpotent
390:(Definition~\ref{def:conilpotent-complete}) or complete with respect to
507:For a conilpotent chiral coalgebra $\mathcal{C}$ on $X$ with coaugmentation
1480: $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ is conilpotent, or $\mathcal{A}$
1492:\item $\mathcal{C}$ is conilpotent
1493: (Definition~\ref{def:conilpotent-cobar}),
2776:consists precisely of those conilpotent chiral coalgebras $\mathcal{C}$ satisfying:
2832:any conilpotent coalgebra. On the Koszul locus
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'cobar integration kernel' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'chiral Koszul pair' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
103:property of a chiral Koszul pair, is checked by spectral sequence
634:\subsection{The concept of chiral Koszul pairs: precise formulation}
644:A \emph{chiral Koszul pair} on a smooth projective curve~$X$
696:In particular, each algebra~$\cA_i$ in a chiral Koszul pair is a
731:Consider the chiral Koszul pair $(\mathcal{BC}, \mathcal{BG})$ where:
1138:Let $(\cA_1, \cA_2)$ be a chiral Koszul pair
4074:$(\cA_2, \cC_2, \tau_2, F_\bullet)$ be a chiral Koszul pair in
4228:whose geometric fibers are chiral Koszul pairs in the sense of
4722:Let $(\mathcal{A}_1, \mathcal{A}_2)$ be a chiral Koszul pair. Then there exists a natural quasi-isomorphism of chiral coalgebras:
5730:\subsection{The fundamental theorem for chiral Koszul pairs}
5735:chiral Koszul pair $(\cA_1,\cA_2)$
5746:Any extension of that package to arbitrary chiral Koszul pairs would
6051:resolution is minimal. The chiral Koszul pair
6065:quadratic data alone. The chiral Koszul pair
6432:Let $(\cA_1, \cA_1^!)$ and $(\cA_2, \cA_2^!)$ be \emph{quadratic} chiral Koszul pairs
6529:\index{chiral Koszul pairs!dependency map}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'chiral twisting' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
98:On a curve~$X$, the chiral twisting morphism
138:Heisenberg example the general notion of chiral twisting data
202:A \emph{chiral twisting datum} on a smooth curve $X$ is a quadruple
254:A chiral twisting datum $(\cA, \cC, \tau, F_\bullet)$ is
288:Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum.
335:Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
363:Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
411:\begin{theorem}[Fundamental theorem of chiral twisting morphisms; \ClaimStatusProvedHere]
419:For a chiral twisting datum
486:\begin{corollary}[Three bijections for chiral twisting morphisms;
554:The fundamental theorem of chiral twisting morphisms
615:Let $\alpha, \beta \colon C \to \cA$ be two chiral twisting morphisms
2175:The fundamental theorem of chiral twisting morphisms
4107:Part~(1) is the fundamental theorem of chiral twisting morphisms
6532:\item $\mathrm{A}_0$: Fundamental theorem of chiral twisting morphisms
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\begin\\{definition\\}' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
200:\begin{definition}[Chiral twisting datum]\label{def:chiral-twisting-datum}
252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
642:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
3855:\begin{definition}[Primitive cumulant quotient; \ClaimStatusProvedHere]
3877:\begin{definition}[Primitive generating series; \ClaimStatusProvedHere]
3899:\begin{definition}[Completion Hilbert series; \ClaimStatusProvedHere]
3919:\begin{definition}[Primitive defect series; \ClaimStatusProvedHere]
3939:\begin{definition}[Koszul radius and completion entropy;
4541:\begin{definition}[Koszul dual chiral coalgebra: intrinsic construction]\label{def:koszul-dual-coalgebra}
5366:\begin{definition}[Augmented \texorpdfstring{$\Eone$}{E1}-chiral algebra]
5375:\begin{definition}[Pro-nilpotent and conilpotent]
6172:\begin{definition}[Filtered chiral algebra]
6178:\begin{definition}[Curved \texorpdfstring{$A_\infty$}{A-infinity}]\label{def:curved-ainfty-kp}
6248:\begin{definition}[Derived chiral algebra]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'Chiral Koszul morphism' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'primitive cumulant' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3839:\subsection{Completion kinematics: the primitive cumulant spectrum}
3841:\index{primitive cumulant spectrum|textbf}
3849:of~$\cA$. The central objects (the primitive cumulant quotients,
3857:\index{primitive cumulant quotient|textbf}
3867:The \emph{primitive cumulant quotient} at weight~$h$ is
3935:which nonquadratic OPEs force new primitive cumulants beyond the
3987:primitive cumulants, with $g_r = p(r+1) - p(r)$ growing
4002:\index{primitive cumulant spectrum!recovery from windows}
wait(call_Aac4VKwHB7wgPuTgn3FNWb0R) timed out:
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{definition\\}|\\\\begin\\{convention\\}|\\\\begin\\{notation\\}|define|denote|write|let |Throughout this chapter|we write|is the .*?object|:=|\\\\coloneqq\" chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\begin\{definition\}|\begin\{convention\}|\begin\{notation\}|define|denote|write|let |Throughout this chapter|we write|is the .*?object|:=|\coloneqq)
                                                                                                                                                  ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'Koszul dual chiral coalgebra' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4541:\begin{definition}[Koszul dual chiral coalgebra: intrinsic construction]\label{def:koszul-dual-coalgebra}
4554:Define the \emph{Koszul dual chiral coalgebra} $\mathcal{A}_2^!$ by the following stages:

thinking
**Addressing regex issue**

I'm facing a regex issue related to escapes while using rg. I could simplify multiple instances of -e with fixed strings, so I should probably rerun that. Also, it seems like the explorer isn’t showing any results, but maybe it’s still processing? I wonder if we can just resume or close it for now. In any case, I should focus on using rg with the right patterns for better analysis.
exec
/bin/zsh -lc "rg -n -e '\\\\begin\\{definition\\}' -e '\\\\begin\\{convention\\}' -e '\\\\begin\\{notation\\}' -e 'define' -e 'denote' -e 'we write' -e 'Throughout this chapter' -e ':=' -e '\\\\coloneqq' chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:140:pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
chapters/theory/chiral_koszul_pairs.tex:200:\begin{definition}[Chiral twisting datum]\label{def:chiral-twisting-datum}
chapters/theory/chiral_koszul_pairs.tex:218:K_\tau^L(\cA,\cC) := (\cA \otimes \cC,\; d_\cA + d_\cC + d_\tau^L),
chapters/theory/chiral_koszul_pairs.tex:220:K_\tau^R(\cC,\cA) := (\cC \otimes \cA,\; d_\cC + d_\cA + d_\tau^R).
chapters/theory/chiral_koszul_pairs.tex:252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
chapters/theory/chiral_koszul_pairs.tex:519:defined on cogenerators by $g_\tau(s^{-1} c) = \tau(c)$; the
chapters/theory/chiral_koszul_pairs.tex:524:$f_\tau\colon \cC \to \bar{B}_X(\cA)$ defined dually.
chapters/theory/chiral_koszul_pairs.tex:642:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:660:In this situation we write $\cA_2 \simeq \cA_1^!$ and
chapters/theory/chiral_koszul_pairs.tex:801:both respect $F$ since they are defined by the OPE, which respects
chapters/theory/chiral_koszul_pairs.tex:863:The PBW filtration on $\widehat{\fg}_k$ is defined by
chapters/theory/chiral_koszul_pairs.tex:911:The PBW filtration on $\mathrm{Vir}_c$ is defined by the
chapters/theory/chiral_koszul_pairs.tex:1183:are well-defined chain complexes (twisted differentials square to
chapters/theory/chiral_koszul_pairs.tex:1251:$(m_2, m_3, m_4, \ldots)$ denote the transferred
chapters/theory/chiral_koszul_pairs.tex:1295:defined fiberwise and compatible with the FM stratification, so
chapters/theory/chiral_koszul_pairs.tex:1732:graded~$R_V := \operatorname{gr}^F V$, which is a commutative
chapters/theory/chiral_koszul_pairs.tex:2227:filtration is defined fiberwise and compatible with the FM
chapters/theory/chiral_koszul_pairs.tex:2985:same transferred genus-$0$ tree that defines the mixed degree-$r$
chapters/theory/chiral_koszul_pairs.tex:3016:\textup{Proved:} the PBW filtration is defined by order of OPE
chapters/theory/chiral_koszul_pairs.tex:3472:$r_{\max} := \min\{r : o_{s+1}(\cA) = 0 \text{ for all } s > r\}$.
exec
/bin/zsh -lc "rg -n -e '\\\\tau' -e '\\\\Theta_\\\\cA' -e '\\\\gAmod' -e '\\\\dzero' -e '\\\\dfib' -e '\\\\Dg\\{g\\}' -e '\\\\barB_X' -e '\\\\barB\\(' -e 'B\\"'^'"\\{\\\\mathrm\\{ord\\}\\}' chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_construction.tex:30:$B^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar\cA)$: the cofree
chapters/theory/bar_construction.tex:33:The factorization coalgebra $\barB(\cA) = \mathrm{Sym}^c(s^{-1}\bar\cA)$
chapters/theory/bar_construction.tex:36:$\Theta_\cA \in \MC(\gAmod)$ governing the genus expansion,
chapters/theory/bar_construction.tex:38:tower $\Theta_\cA^{\leq r}$.
chapters/theory/bar_construction.tex:65:components into the full genus-$0$ differential $\dzero$
chapters/theory/bar_construction.tex:66:and proves $\dzero^2 = 0$; the key input is the Arnold relation
chapters/theory/bar_construction.tex:72:Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
chapters/theory/bar_construction.tex:84:The bar construction $\barB_X(\cA)$ of an augmented chiral
chapters/theory/bar_construction.tex:86:$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the bar coalgebra
chapters/theory/bar_construction.tex:90:\cA^i \;:=\; H^*(\barB_X(\cA)).
chapters/theory/bar_construction.tex:92:Thus $\barB_X(\cA)$, $\cA^i$, and $\cA^!$ are distinct objects.
chapters/theory/bar_construction.tex:108:\mathbb{D}_{\operatorname{Ran}}\, \barB_X(\cA)
chapters/theory/bar_construction.tex:113:$\barB_X(\cA)$ on unordered $\operatorname{Ran}(X)$.
chapters/theory/bar_construction.tex:115:$B^{\mathrm{ord}}_X(\cA)$.
chapters/theory/bar_construction.tex:118:the expression $\mathbb{D}_{\operatorname{Ran}}\, B^{\mathrm{ord}}_X(\cA)$
chapters/theory/bar_construction.tex:124:its $\Sigma_n$-coinvariant quotient $\barB_X(\cA)$.
chapters/theory/bar_construction.tex:129:the symmetric bar $\barB_X(\cA)$) and $\cA^!_{\mathrm{line}}$ (the line
chapters/theory/bar_construction.tex:131:bar $B^{\mathrm{ord}}_X(\cA)$). Throughout Volume~I, bare~$\cA^!$
chapters/theory/bar_construction.tex:135:$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
chapters/theory/bar_construction.tex:142:$\tau \colon \barB_X(\cA) \to \cA$,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/bar_construction.tex | sed -n '410,450p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   410	eigenvalues $\lambda = \exp(2\pi i(h - c/24))$ are the
   411	\emph{exponentials} of conformal weights shifted by the central
   412	charge; the modular period~$N$ is the smallest positive integer for
   413	which $\exp(2\pi i N c/24) = 1$. At the geometric level, the
   414	nilpotency $\kappa(\lambda)^{g-1} = 0$
   415	(Theorem~\ref{thm:geometric-depth-smooth}) makes the operator
   416	$\exp(\kappa(\lambda))$ \emph{unipotent}, not periodic: geometry
   417	provides a stabilization threshold, not a period. True periodicity
   418	arises from modular and quantum sources whose nilpotent generators
   419	have finite-order exponentials.
   420	\end{remark}
   421	
   422	\subsection{Precise construction of the bar complex}
   423	
   424	\begin{definition}[Genus-graded geometric bar complex, preliminary form]
   425	\label{def:geom-bar-preview}
   426	The bar complex at genus $g$ and bar degree~$n$ is, in first
   427	approximation:
   428	\[\bar{B}^{(g),n}(\mathcal{A}) = \Gamma\left(\overline{C}_{n+1}^{(g)}(\Sigma_g), j_*j^*\mathcal{A}^{\boxtimes(n+1)} \otimes \Omega^n(\log D^{(g)})\right)\]
   429	The total bar complex is
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/bar_construction.tex | sed -n '1500,1555p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1500	\begin{proposition}[Model independence; \ClaimStatusProvedHere]
  1501	\label{prop:model-independence}
  1502	\index{model independence}
  1503	Let $\cA$ be a chiral algebra on~$X$.
  1504	Any two admissible\footnote{An admissible presentation is a
  1505	dg factorization coalgebra computing $\bar{B}_X(\cA)$ in the homotopy
  1506	category: it is built from sections of $\cA^{\boxtimes(n+1)}$ over
  1507	open substacks of $\operatorname{Ran}(X)$ and its differential restricts
  1508	to the collision-residue map on each boundary stratum.}
  1509	dg presentations of the bar object
  1510	$\mathcal{B}_X(\cA)$ are connected by a contractible space of
  1511	quasi-isomorphisms. In particular, any two such models give
  1512	canonically isomorphic cohomology, spectral sequences, and generating
  1513	functions.
  1514	\end{proposition}
  1515	
  1516	\begin{proof}
  1517	Both presentations are cofibrant-fibrant objects in the model structure
  1518	on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
  1519	(Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/cobar_construction.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	\chapter{The geometric cobar complex}
     2	\label{chap:cobar-construction}
     3	
     4	The bar functor destroys the algebra: it encodes~$\cA$ as a
     5	factorization coalgebra $\barB(\cA)$ from which no multiplication
     6	is directly visible. The cobar complex $\Omega(\cC)$ is the
     7	reconstruction machine that recovers~$\cA$ from this coalgebraic
     8	residue, realizing the inversion
     9	$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ (Theorem~B) and
    10	proving that the MC element
    11	$\Theta_\cA \in \MC(\gAmod)$ determines~$\cA$ up to
    12	quasi-isomorphism on the Koszul locus. Both functors are
    13	projections of a single universal twisting morphism
    14	$\tau \in \MC\bigl(\operatorname{Conv}(\cC, \cA)\bigr)$
    15	(Definition~\ref{def:twisting-morphism}): bar records collision
    16	residues via the logarithmic propagator
    17	$\eta_{ij} = d\log(z_i - z_j)$; cobar integrates distributional
    18	duals over the open configuration space $C_n(X)$.
    19	The duality between them (residues versus delta functions,
    20	$j_*$ versus $j_!$) is the Verdier exchange on



thinking
**Summarizing define-before-use issues and relevant instructions**

I’m noting specific lines where terms are used before being defined in `cobar_construction` and `chiral_koszul_pairs`, highlighting where the first use occurs and where definitions actually are. I’m also gathering and condensing key instructions from CLAUDE, concordance, theorem_registry, and red_team_summary that directly affect how I verify define-before-use—emphasizing principles like treating claims as false until verified and relying on concordance as the authority. Finally, I plan to update the step statuses in the plan to reflect progress after this analysis.
Plan update
Documented the define-before-use findings in the three theory files; ready to consolidate observations and craft the final response.
  ✓ Inspect constitutional instructions (CLAUDE.md, concordance, theorem registry, red team summary) for items affecting task, and summarize key directives
  ✓ Review chapters/theory/bar_construction.tex, cobar_construction.tex, chiral_koszul_pairs.tex for define-before-use issues and note occurrences
  → Compile findings and craft final response referencing specific sections and line numbers

thinking
**Improving definitions clarity**

I’m thinking about how to fix issues with definitions in documents. It seems like adding brief inline definitions before using terms is a minimum edit. We should identify cases in assigned files where symbols or objects are referenced before they’re defined, especially in intro sections. Oh, and I noticed that we could target early paragraphs for definitions. We might need a systematic method since bigger files could have many instances of this happening.
thinking
**Identifying definition issues**

I’m considering focusing on local labels and symbols that have later definitions. It seems using a script to detect any forward references could help. For each macro or symbol, just checking the first reference after the definition might work as a way to define before use. I could also parse labels in definition environments and look for those forward references. Although the user is asking about macros or symbols specifically, not theorem references, which is an interesting point to consider!
thinking
**Analyzing symbol identification**

I think we should use a script to identify candidate symbols only found before specific definitions, like `:=`, `\coloneqq`, or `define`. However, the large symbol space might make it noisy. Focusing on major symbols in introductions could work since definitions often come later. I want to ensure being exhaustive, so I’ll use heuristics to find all relevant environments and local label definitions. I'll write a quick Python script to parse and gather necessary line numbers for further review.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
files = [
    'chapters/theory/bar_construction.tex',
    'chapters/theory/cobar_construction.tex',
    'chapters/theory/chiral_koszul_pairs.tex',
]
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\(?:ref|eqref|autoref|Cref|cref)\\{(["'^}]+)'"\\}')
for path in files:
    text = pathlib.Path(path).read_text()
    lines = text.splitlines()
    labels = {}
    env = None
    title = None
    env_re = re.compile(r'\\\\begin\\{(definition|convention|notation|remark|theorem|lemma|proposition|corollary|example)\\}(?:\\[(["'^'"\\]]*)\\])?')
    for i,l in enumerate(lines, start=1):
        m = env_re.search(l)
        if m:
            env = m.group(1)
            title = m.group(2) or ''
        for lm in label_re.finditer(l):
            labels[lm.group(1)] = (i, env, title)
        if '\\\\end{' in l:
            env = None
            title = None
    refs=[]
    for i,l in enumerate(lines, start=1):
        for rm in ref_re.finditer(l):
            key=rm.group(1)
            if key in labels and labels[key][0] > i:
                refs.append((i,key,labels[key]))
    print('\\nFILE', path)
    for r in refs[:200]:
        print(r)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

FILE chapters/theory/bar_construction.tex
(64, 'thm:bar-nilpotency-complete', (796, 'theorem', 'Nilpotency of bar differential; \\ClaimStatusProvedHere'))
(67, 'thm:arnold-three', (1208, 'theorem', 'Arnold relations; \\ClaimStatusProvedHere'))
(68, 'rem:costello-gwilliam-factorization', (262, 'remark', 'Holomorphic factorization on $\\FM_k(X)$'))
(72, 'thm:bar-nilpotency-complete', (796, 'theorem', 'Nilpotency of bar differential; \\ClaimStatusProvedHere'))
(209, 'prop:pole-decomposition', (978, 'proposition', 'Pole decomposition of the bar differential; \\ClaimStatusProvedHere'))
(286, 'prop:pole-decomposition', (978, 'proposition', 'Pole decomposition of the bar differential; \\ClaimStatusProvedHere'))
(286, 'comp:deg1-general', (1269, None, None))
(434, 'def:geom-bar', (1715, 'definition', 'Genus-graded geometric bar complex'))
(563, 'sec:residue-calculus', (1851, None, None))
(574, 'conv:orientations-enhanced', (644, 'convention', 'Enhanced sign system'))
(627, 'prop:pole-decomposition', (978, 'proposition', 'Pole decomposition of the bar differential; \\ClaimStatusProvedHere'))
(637, 'prop:pole-decomposition', (978, 'proposition', 'Pole decomposition of the bar differential; \\ClaimStatusProvedHere'))
(640, 'def:orientation', (1408, 'definition', 'Orientation line bundle'))
(667, 'lem:orientation', (1785, 'lemma', 'Orientation convention; \\ClaimStatusProvedHere'))
(738, 'lem:orientation', (1785, 'lemma', 'Orientation convention; \\ClaimStatusProvedHere'))
(898, 'lem:orientation', (1785, 'lemma', 'Orientation convention; \\ClaimStatusProvedHere'))
(1055, 'thm:bar-functorial-complete', (1447, 'theorem', 'Bar construction is functorial; \\ClaimStatusProvedHere'))
(1123, 'lem:orientation', (1785, 'lemma', 'Orientation convention; \\ClaimStatusProvedHere'))

thinking
**Summarizing instructions and define-before-use issues**

I'm preparing a final response that covers the key instructions from four main files and details define-before-use problems found in specific source files, including precise file paths and line numbers. For each issue, I'll provide local context and suggest fixes like moving definitions earlier or adding forward references to clarify the ordering. I’ll also summarize instructions referencing CLAUDE.md and related files, noting important principles and guidelines with approximate line numbers for orientation.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'Beilinson Principle' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
189:## The Beilinson Principle
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'constitution' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
6:This chapter is the constitution of the monograph. When chapters
1226:architecture} is a constitutional amendment.
2410:constitutional index for the intrinsic characterization
2563:constitution.
7292: \textbf{AP165 correction (constitutional).}
codex
I’ve isolated the objective forward-reference surface and I’m now separating true notation failures from benign theorem cross-references. The fixes will stay minimal: early standing-notation sentences, not chapter reordering.
collab wait(call_s9p9GoN66jTM7l4sFZjl62oJ)
  receivers: 019d87dc-010c-7b53-b380-05cc56cb78cc

thinking
**Outlining detailed final response**

I’m putting together a comprehensive plan for the final message that summarizes key instructions by file and line numbers, outlines define-before-use issues with context and fix suggestions, and acknowledges that no edits were made per the user’s guidance. I’m focusing on clear bullet lists without nested bullets and including references to instructions from several files like CLAUDE.md, Concordance, and Theorem Registry. This will help create a well-structured, informative summary for the user.
codex
**Instruction Digest**
- `CLAUDE.md` (lines 1‑80, 189‑230) reminds us that this repo is in correction mode: treat every claim as provisional, honour the E₁-first/projection-heavy architecture, and obey the Beilinson principle (false until independently verified) plus the hot-zone templates before touching formulas; that also means respecting the no-bold/AI-slop vocab and following the label/status conventions before adding content.
- `chapters/connections/concordance.tex` (lines 1‑30) is “the constitution”: anything that disagrees with its recorded status must be treated as an error, every claim needs a status tag, and the geometry determines which Hochschild theory applies, so don’t invent or reuse statements that aren’t registered there.
- `metadata/theorem_registry.md` (lines 1‑30) makes the auto‑generated registry the ground truth for `\ClaimStatusProvedHere` claims and tracks proved counts per file, so avoid drifting statuses that would break the registry’s synchronization requirements.
- `archive/raeeznotes/raeeznotes100/red_team_summary.md` (lines 1‑70) flags heuristics/conjectures/open claims as untrusted, highlights status conflicts and dependencies as red flags, and points to the high‑risk clusters where rigorous verification should focus before accepting or quoting any claim.

**Define-before-use Issues**
- `chapters/theory/bar_construction.tex`: the preliminary definition of the genus‑graded bar complex (lines 424‑434) already invokes the orientation bundle `\mathrm{or}_{p+1}^{(g)}` before its definition at line 1408, so the reader meets the symbol only by reference; either move Definition 6.1 (orientation line bundle) ahead of the preview or replace the reference with a brief inline description and a pointer to the later definition.  
- `chapters/theory/bar_construction.tex`: Proposition 5.1 (line 1518) uses “conilpotent dg coalgebras” before the filtered conilpotent chiral coalgebra definition at line 2259, which makes the term feel undefined; bring the definition forward or insert a clear forward reference next to the first mention so the technical audience knows what “conilpotent” means before it is needed.
- `chapters/theory/cobar_construction.tex`: the opening paragraph (lines 4‑33) refers to the factorization coalgebra $\barB(\cA)$, conilpotent chiral coalgebras, and the geometric cobar complex $\Omega^{\mathrm{ch}}_n(\cC)$ before Definitions 4.4, 4.2, and 4.5 introduce them at lines 223, 197, and 250 respectively; consider flipping the order (or at least inserting short “Definition coming below” bridges) so the terms are defined prior to their first use.
- `chapters/theory/chiral_koszul_pairs.tex`: the narrative around lines 98‑105 already talks about “the chiral twisting morphism/datum” and “properties of a chiral Koszul pair” but the precise Definition 7.1 of a chiral twisting datum (line 200) and Definition 7.3 of a chiral Koszul pair (line 642) come much later; pulling those definitions earlier or explicitly flagging the forward references will prevent readers from parsing the non‑technical high‑level discussion before the objects are formally introduced.

No edits were made; this is a purely observational pass. Let me know if you’d like me to reorder any of these definitions or to draft wording that clarifies the dependency order.
wait(call_s9p9GoN66jTM7l4sFZjl62oJ) 1 agents complete:
  019d87dc-010c-7b53-b380-05cc56cb78cc completed: "**Instruction Digest**
- `CLAUDE.md` (lines 1‑80, 189‑230) reminds us that this repo is in correction mode: treat every …"

thinking
**Inspecting identified issues**

Great, the explorer has identified four issues that I need to verify and possibly find more of. It’s essential to be exhaustive within the scope. I’ll manually confirm the exact lines and make minimal fixes. But I wonder if there could be additional similar issues? I might need to inspect specific line numbers and their context, and I could potentially detect more from forward references or uses. Combining this with my review, I’ll read around the relevant lines for better local context. Let’s take a close look!
exec
/bin/zsh -lc "sed -n '410,455p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '88,115p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,70p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1498,1535p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
eigenvalues $\lambda = \exp(2\pi i(h - c/24))$ are the
\emph{exponentials} of conformal weights shifted by the central
charge; the modular period~$N$ is the smallest positive integer for
which $\exp(2\pi i N c/24) = 1$. At the geometric level, the
nilpotency $\kappa(\lambda)^{g-1} = 0$
(Theorem~\ref{thm:geometric-depth-smooth}) makes the operator
$\exp(\kappa(\lambda))$ \emph{unipotent}, not periodic: geometry
provides a stabilization threshold, not a period. True periodicity
arises from modular and quantum sources whose nilpotent generators
have finite-order exponentials.
\end{remark}

\subsection{Precise construction of the bar complex}

\begin{definition}[Genus-graded geometric bar complex, preliminary form]
\label{def:geom-bar-preview}
The bar complex at genus $g$ and bar degree~$n$ is, in first
approximation:
\[\bar{B}^{(g),n}(\mathcal{A}) = \Gamma\left(\overline{C}_{n+1}^{(g)}(\Sigma_g), j_*j^*\mathcal{A}^{\boxtimes(n+1)} \otimes \Omega^n(\log D^{(g)})\right)\]
The total bar complex is
 succeeded in 51ms:
bar complex. All standard families are Koszul; only class~$G$
(Heisenberg and its relatives) is SC-formal
(Proposition~\ref{prop:sc-formal-iff-class-g}).
Confusing the two misidentifies what the shadow tower measures.

On a point, the bar complex
$\barB(A) = T^c(s^{-1}\bar{A})$ is built from tensor powers of
the augmentation ideal; a classical twisting morphism
$\tau \colon \barB(A) \to A^!$ is a degree-$+1$ element in the
convolution dg~Lie algebra satisfying $d\tau + \tau \star \tau = 0$.
On a curve~$X$, the chiral twisting morphism
(Definition~\ref{def:chiral-twisting-datum}) lives in the chiral
convolution algebra, where the star product is mediated by the
integration kernel on $X^2 \setminus \Delta$. The acyclicity of
the twisted tensor product $K_\tau^L(\cA, \cC)$, the defining
property of a chiral Koszul pair, is checked by spectral sequence
methods adapted to the PBW filtration by bar degree
(Theorem~\ref{thm:pbw-koszulness-criterion}).

Three phenomena distinguish the chiral setting from its
 succeeded in 51ms:
\end{proof}

\begin{proposition}[Model independence; \ClaimStatusProvedHere]
\label{prop:model-independence}
\index{model independence}
Let $\cA$ be a chiral algebra on~$X$.
Any two admissible\footnote{An admissible presentation is a
dg factorization coalgebra computing $\bar{B}_X(\cA)$ in the homotopy
category: it is built from sections of $\cA^{\boxtimes(n+1)}$ over
open substacks of $\operatorname{Ran}(X)$ and its differential restricts
to the collision-residue map on each boundary stratum.}
dg presentations of the bar object
$\mathcal{B}_X(\cA)$ are connected by a contractible space of
quasi-isomorphisms. In particular, any two such models give
canonically isomorphic cohomology, spectral sequences, and generating
functions.
\end{proposition}

\begin{proof}
Both presentations are cofibrant-fibrant objects in the model structure
 succeeded in 51ms:
\chapter{The geometric cobar complex}
\label{chap:cobar-construction}

The bar functor destroys the algebra: it encodes~$\cA$ as a
factorization coalgebra $\barB(\cA)$ from which no multiplication
is directly visible. The cobar complex $\Omega(\cC)$ is the
reconstruction machine that recovers~$\cA$ from this coalgebraic
residue, realizing the inversion
$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ (Theorem~B) and
proving that the MC element
$\Theta_\cA \in \MC(\gAmod)$ determines~$\cA$ up to
quasi-isomorphism on the Koszul locus. Both functors are
projections of a single universal twisting morphism
$\tau \in \MC\bigl(\operatorname{Conv}(\cC, \cA)\bigr)$
(Definition~\ref{def:twisting-morphism}): bar records collision
residues via the logarithmic propagator
$\eta_{ij} = d\log(z_i - z_j)$; cobar integrates distributional
duals over the open configuration space $C_n(X)$.
The duality between them (residues versus delta functions,
$j_*$ versus $j_!$) is the Verdier exchange on

thinking
**Identifying issues in code**

The user is asking me to "find issues AND fix them in one pass," but they might not be expecting a full computer parsing. I need to look for any obvious forward references, like in "chiral_koszul_pairs," which isn't an object.

Then there's "bar_construction," where it mentions \dzero defined in another chapter. I see a note indicating what it denotes. So, I should clarify that in my response.
exec
/bin/zsh -lc "sed -n '1,95p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

thinking
**Checking construction issues**

I think I need to check whether bar_construction has other local issues, particularly looking at conilpotent dg coalgebras in the proof. I wonder if line 1518 is before definition 2259, and it seems good to fix that inline. It might also be helpful to add an early local convention for the orientation bundle, but I don't want to overdo it. I'll also need to inspect the title and details around definition 2259.
codex
I’ve reduced the audit to four real local notation failures. I’m patching them by introducing the missing objects exactly where they first appear, not by moving later theory blocks.


thinking
**Inspecting patch failure**

It looks like the patch partially failed, likely due to some mismatched context around spaces. I want to check the exact snippet around that position, but actually, it seems unnecessary to patch there. I should start fresh! I need to understand if the patch failed entirely or just partially. Usually, it’s the case that none applied. I’ll have to re-run it carefully and consider using smaller, separate patches instead.
thinking
**Inspecting update context**

I need to consider whether I should mention any updates before proceeding to edit. It seems like I already have, though. So now, I’m thinking about inspecting specific contexts to make the necessary patches. I guess I could use a command like `sed` to pinpoint the exact lines around where I want to insert the changes. I like the idea of being precise! Let’s see how that goes.
exec
/bin/zsh -lc "sed -n '1,25p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,442p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '54,70p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1514,1524p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{The geometric cobar complex}
\label{chap:cobar-construction}

The bar functor destroys the algebra: it encodes~$\cA$ as a
factorization coalgebra $\barB(\cA)$ from which no multiplication
is directly visible. The cobar complex $\Omega(\cC)$ is the
reconstruction machine that recovers~$\cA$ from this coalgebraic
residue, realizing the inversion
$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ (Theorem~B) and
proving that the MC element
$\Theta_\cA \in \MC(\gAmod)$ determines~$\cA$ up to
quasi-isomorphism on the Koszul locus. Both functors are
projections of a single universal twisting morphism
$\tau \in \MC\bigl(\operatorname{Conv}(\cC, \cA)\bigr)$
(Definition~\ref{def:twisting-morphism}): bar records collision
residues via the logarithmic propagator
$\eta_{ij} = d\log(z_i - z_j)$; cobar integrates distributional
duals over the open configuration space $C_n(X)$.
The duality between them (residues versus delta functions,
$j_*$ versus $j_!$) is the Verdier exchange on
 succeeded in 52ms:
$\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
The complete definition, incorporating the bigrading by bar
degree~$p$ and form degree~$q$ together with the genus-graded
orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
Definition~\ref{def:geom-bar} below.
\end{definition}

\begin{convention}[Global sections vs.\ derived global sections]\label{conv:gamma-vs-rgamma}
\index{global sections!underived vs.\ derived}
Throughout this chapter, $\Gamma(-)$ denotes \emph{underived} global sections:
for a sheaf $\mathcal{F}$ on a variety $Y$, the symbol $\Gamma(Y, \mathcal{F})$
is the vector space $H^0(Y, \mathcal{F})$. When derived global sections are
needed (e.g., over moduli stacks or in derived $\mathcal{D}$-module arguments),
 succeeded in 51ms:
\end{proposition}

\begin{proof}
Both presentations are cofibrant-fibrant objects in the model structure
on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
(Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
replacements in this model structure are unique up to a contractible
space of weak equivalences: the mapping space
$\operatorname{Map}(B_1, B_2)$ between two such replacements is
contractible whenever both compute the same homotopy object.
The configuration-space model $\bar{B}_X(\cA)$ is cofibrant by
 succeeded in 51ms:
H^*(\overline{\mathcal{M}}_g, Z(\cA))$
(Theorem~\ref{thm:quantum-complementarity-main}).
No other functorial construction achieves all three: the operadic
adjunction achieves (a) but not (b) or (c); Verdier duality alone
achieves (b) but has no bar-cobar content; complementarity (c)
requires both (a) and (b) as input.

Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
tests and consequences around chiral Koszulness. Nine are
unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
vanishing of transferred $A_\infty$ operations $m_k$ for
$k \geq 3$, acyclicity of the twisted tensor product
$K_\tau^L(\cA, \cC)$, truncation of the shadow tower
$\Theta_\cA^{\leq r}$, and five others. One (Hochschild
duality and concentration in degrees $\{0,1,2\}$) is a proved
consequence on the Koszul locus. One (the Lagrangian
eigenspace decomposition) is conditional on perfectness of the
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
@@ -432,3 +432,4 @@
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
apply_patch(auto_approved=true) exited 0 in 18ms:
Success. Updated the following files:
M chapters/theory/bar_construction.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..a08536fa794ad1727e45e3f192940415586ff023
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..a08536fa794ad1727e45e3f192940415586ff023
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
@@ -1519,2 +1519,4 @@
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
apply_patch(auto_approved=true) exited 0 in 18ms:
Success. Updated the following files:
M chapters/theory/bar_construction.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
@@ -3,2 +3,14 @@
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
apply_patch(auto_approved=true) exited 0 in 26ms:
Success. Updated the following files:
M chapters/theory/cobar_construction.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -60,2 +60,18 @@
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
apply_patch(auto_approved=true) exited 0 in 42ms:
Success. Updated the following files:
M chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the


thinking
**Inspecting bar construction issues**

I think there might be more issues in the bar_construction introduction that haven't been fixed yet. Maybe it's worth adding another point in the opening section of bar_construction. I’ll need to inspect the first 80 lines to see if there are any glaring problems that catch my eye. It's essential to make sure everything is as clear and polished as possible before moving on! Let's take a closer look at it.
codex
The first pass is patched. I’m re-reading the modified openings against the earlier failure list to check whether anything still appears before its local introduction.
exec
/bin/zsh -lc "sed -n '1,95p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,45p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '46,90p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{The geometric bar complex}
\label{chap:bar-cobar}
\label{chap:bar-construction}


\index{bar construction!as integral transform|textbf}
\index{non-abelian Fourier transform|textbf}

An augmented algebra has exactly one piece of canonical structure beyond
its multiplication: the augmentation ideal $\bar\cA = \ker(\varepsilon)$,
the part that the counit forgets.
Desuspend it to shift the grading, then form the cofree
nilpotent coalgebra $T^c(s^{-1}\bar\cA)$ with deconcatenation coproduct.
This object is not a choice; it is the \emph{universal} recipient
of coderivations built from the algebra structure maps, and the
bar differential is the unique coderivation that encodes them all.
The entire construction is forced: given $\cA$ and $\varepsilon$, the
coalgebra $B(\cA)$ exists, its differential squares to zero,
and every deformation-theoretic invariant of $\cA$ is a projection
from the resulting Maurer--Cartan element.
 succeeded in 52ms:
(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
functorial pair that resolves all three obstructions. It is the
unique adjunction that (a)~inverts on the Koszul locus, producing
$\Omega_X(\barB_X(\cA)) \xrightarrow{\sim} \cA$
(Theorem~\ref{thm:bar-cobar-inversion-qi}); (b)~intertwines
Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
$Q_g(\cA) \oplus Q_g(\cA^!) \simeq
H^*(\overline{\mathcal{M}}_g, Z(\cA))$
(Theorem~\ref{thm:quantum-complementarity-main}).
No other functorial construction achieves all three: the operadic
adjunction achieves (a) but not (b) or (c); Verdier duality alone
achieves (b) but has no bar-cobar content; complementarity (c)
requires both (a) and (b) as input.

\smallskip\noindent\textit{Standing notation for the overview.}
A chiral twisting datum means a quadruple
$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
a conilpotent complete factorization coalgebra, a degree-$+1$
twisting morphism $\tau\colon \cC\to \cA$ satisfying the
 succeeded in 52ms:
\chapter{The geometric cobar complex}
\label{chap:cobar-construction}

\smallskip\noindent\textit{Opening notation.}
In the overview below, $\barB(\cA)$ denotes the symmetric factorization
bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
factorization coalgebra whose iterated reduced coproduct vanishes on
every local section; and
$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
denotes the geometric cobar complex obtained by Verdier duality on
configuration spaces. Definitions~\ref{def:factorization-coalgebra},
\ref{def:conilpotent-cobar}, and
\ref{def:geom-cobar-intrinsic} give the formal versions used in the
rest of the chapter.

The bar functor destroys the algebra: it encodes~$\cA$ as a
factorization coalgebra $\barB(\cA)$ from which no multiplication
is directly visible. The cobar complex $\Omega(\cC)$ is the
reconstruction machine that recovers~$\cA$ from this coalgebraic
residue, realizing the inversion
exec
/bin/zsh -lc 'git diff -- chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 4380d79..b3e2e39 100644
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -79,23 +79,28 @@ Throughout this chapter: collision divisors are $D_{ij}$ with $i < j$ (indices i
 
 \begin{convention}[Bar coalgebra and Koszul dual algebra]
 \label{conv:bar-coalgebra-identity}
-\index{bar construction!as Koszul dual coalgebra|textbf}
+\index{bar construction!as bar coalgebra|textbf}
 \index{Koszul dual!coalgebra vs.\ algebra|textbf}
 The bar construction $\barB_X(\cA)$ of an augmented chiral
 algebra~$\cA$ is a dg factorization \emph{coalgebra} on
-$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
-of~$\cA$: the bar complex is not a tool for computing the dual,
-it \emph{is} the dual.
+$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the bar coalgebra
+of~$\cA$: the bar complex computes the dual
+coalgebra
+\[
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the



thinking
**Checking modifications carefully**

Oh no, I see that `git diff` is showing a lot of unrelated existing changes. I need to be careful not to mention them or accidentally revert them. Our modifications are mixed in with many user changes, so I should focus only on our exact edits. Maybe I should use `git diff` with line numbers to inspect our insertions? Using tools like `rg` might be simpler. I need to make sure to check for any remaining issues or symbols flagged as undefined.
thinking
**Verifying definitions in code**

I should probably run some narrow verification, maybe using `grep` or a `TeX` tool since it's just prose, which suggests compiling might not be necessary. Instead, I could target `latexmk`, but that could be a bit costly. Maybe using `python` or just `grep` would be simpler. The user asked about defined-before-use, so I could search to ensure that my inserted definitions come before their first occurrence. I’ll run checks on specific tokens to verify their positions and get their line numbers.
codex
The edits are in place. I’m doing one narrow verification pass now: line-check the repaired first-use sites so I can report each problem and the exact local fix without guessing line numbers.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1516,1524p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '424,438p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1,18p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '58,76p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1516	
  1517	\begin{proof}
  1518	Both presentations are cofibrant-fibrant objects in the model structure
  1519	on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
  1520	(that is, dg coalgebras whose iterated reduced coproduct vanishes on
  1521	every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
  1522	(Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
  1523	replacements in this model structure are unique up to a contractible
  1524	space of weak equivalences: the mapping space
 succeeded in 52ms:
   424	\begin{definition}[Genus-graded geometric bar complex, preliminary form]
   425	\label{def:geom-bar-preview}
   426	The bar complex at genus $g$ and bar degree~$n$ is, in first
   427	approximation:
   428	\[\bar{B}^{(g),n}(\mathcal{A}) = \Gamma\left(\overline{C}_{n+1}^{(g)}(\Sigma_g), j_*j^*\mathcal{A}^{\boxtimes(n+1)} \otimes \Omega^n(\log D^{(g)})\right)\]
   429	The total bar complex is
   430	$\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
   431	The complete definition, incorporating the bigrading by bar
   432	degree~$p$ and form degree~$q$ together with the genus-graded
   433	orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
   434	orientations of the codimension-$p$ collision strata at genus~$g$, is given in
   435	Definition~\ref{def:geom-bar} below.
   436	\end{definition}
   437	
   438	\begin{convention}[Global sections vs.\ derived global sections]\label{conv:gamma-vs-rgamma}
 succeeded in 51ms:
     1	\chapter{The geometric cobar complex}
     2	\label{chap:cobar-construction}
     3	
     4	\smallskip\noindent\textit{Opening notation.}
     5	In the overview below, $\barB(\cA)$ denotes the symmetric factorization
     6	bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
     7	factorization coalgebra whose iterated reduced coproduct vanishes on
     8	every local section; and
     9	$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
    10	denotes the geometric cobar complex obtained by Verdier duality on
    11	configuration spaces. Definitions~\ref{def:factorization-coalgebra},
    12	\ref{def:conilpotent-cobar}, and
    13	\ref{def:geom-cobar-intrinsic} give the formal versions used in the
    14	rest of the chapter.
    15	
    16	The bar functor destroys the algebra: it encodes~$\cA$ as a
    17	factorization coalgebra $\barB(\cA)$ from which no multiplication
    18	is directly visible. The cobar complex $\Omega(\cC)$ is the
 succeeded in 51ms:
    58	achieves (b) but has no bar-cobar content; complementarity (c)
    59	requires both (a) and (b) as input.
    60	
    61	\smallskip\noindent\textit{Standing notation for the overview.}
    62	A chiral twisting datum means a quadruple
    63	$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
    64	a conilpotent complete factorization coalgebra, a degree-$+1$
    65	twisting morphism $\tau\colon \cC\to \cA$ satisfying the
    66	Maurer--Cartan equation, and a compatible filtration. We write
    67	$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
    68	twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
    69	truncation of the universal Maurer--Cartan element of the modular
    70	convolution algebra. A chiral Koszul pair is such a datum on the
    71	Koszul locus, so the twisted tensor products are acyclic and the
    72	associated graded datum is classically Koszul.
    73	Definitions~\ref{def:chiral-twisting-datum},
    74	\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
    75	record the precise versions used below.
    76	
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the


thinking
**Investigating code references**

I’m noticing that there might be other uses of `def:orientation` before its definition at line 640. I’ll need to take a closer look at the script, particularly between lines 630 and 645. It feels like there could be another issue lurking around there. Let's check it out to confirm what’s going on! It always helps to inspect these details before jumping to conclusions.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '632,646p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   632	\end{remark}
   633	
   634	\begin{example}[Heisenberg degree-\texorpdfstring{$1$}{1} bar differential]\label{ex:heisenberg-d-deg1}
   635	\label{ex:free-boson-d-deg1}
   636	The Heisenberg algebra $\mathcal{H}_k$ with OPE $J(z)J(w) = k/(z-w)^2 + \text{regular}$ has bar differential
   637	$d_{\mathrm{res}}(J \otimes J \otimes \eta_{12}) = J_{(1)}J = k \cdot \mathbf{1}$
   638	at degree~$1$: the full chiral product extracts the double-pole mode $J_{(1)}J = k$. Since $J_{(0)}J = 0$ (no simple pole), only the curvature component $d_{\mathrm{curvature}}$ contributes (Proposition~\ref{prop:pole-decomposition}). The level~$k$ is visible at genus~$0$ through the bar differential; at genus~$g \geq 1$, it acquires a topological partner $\kappa(\cH_k)\cdot\omega_g$ from the Hodge bundle (Chapter~\ref{chap:higher-genus}). See Chapter~\ref{ch:heisenberg-frame}, \S\ref{sec:frame-bar-deg1} for the full computation.
   639	\end{example}
   640	
   641	% Orientation bundle: see Definition~\ref{def:orientation} below.
   642	
   643	\subsection{Sign conventions}\label{sec:sign-conventions}
   644	
   645	\begin{convention}[Enhanced sign system]\label{conv:orientations-enhanced}
   646	The bar complex requires three types of sign conventions:
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '566,578p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   566	 \begin{enumerate}
   567	 \item Position of $i,j$ in the tensor product (Koszul sign)
   568	 \item Orientation of $D_{ij}$ as boundary (geometric sign)
   569	 \item Grading of fields $\phi_i, \phi_j$ (super sign)
   570	 \end{enumerate}
   571	\end{itemize}
   572	
   573	The explicit formula for the sign is:
   574	\[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
   575	where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
   576	
   577	\emph{Component 3: Form differential $d_{\text{form}}$.}
   578	
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
files = [
    'chapters/theory/bar_construction.tex',
    'chapters/theory/cobar_construction.tex',
    'chapters/theory/chiral_koszul_pairs.tex',
]
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\(?:ref|eqref|autoref|Cref|cref)\\{(["'^}]+)'"\\}')
env_re = re.compile(r'\\\\begin\\{(definition|convention|notation)\\}(?:\\[(["'^'"\\]]*)\\])?')
for path in files:
    text = pathlib.Path(path).read_text()
    lines = text.splitlines()
    labels = {}
    env = None; title = None
    for i,l in enumerate(lines, start=1):
        m = env_re.search(l)
        if m:
            env = m.group(1); title = m.group(2) or ''
        for lm in label_re.finditer(l):
            if env:
                labels[lm.group(1)] = (i, env, title)
        if re.search(r'\\\\end\\{(definition|convention|notation)\\}', l):
            env = None; title = None
    print('\\nFILE', path)
    for i,l in enumerate(lines, start=1):
        for rm in ref_re.finditer(l):
            key = rm.group(1)
            if key in labels and labels[key][0] > i:
                print(f'{i}: ref {key} -> {labels[key][0]} ({labels[key][1]} {labels[key][2]}) :: {l.strip()}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

FILE chapters/theory/bar_construction.tex
435: ref def:geom-bar -> 1718 (definition Genus-graded geometric bar complex) :: Definition~\ref{def:geom-bar} below.
575: ref conv:orientations-enhanced -> 645 (convention Enhanced sign system) :: where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
641: ref def:orientation -> 1409 (definition Orientation line bundle) :: % Orientation bundle: see Definition~\ref{def:orientation} below.

FILE chapters/theory/cobar_construction.tex
11: ref def:factorization-coalgebra -> 235 (definition Factorization coalgebra) :: configuration spaces. Definitions~\ref{def:factorization-coalgebra},
12: ref def:conilpotent-cobar -> 209 (definition Conilpotent coalgebra) :: \ref{def:conilpotent-cobar}, and
13: ref def:geom-cobar-intrinsic -> 262 (definition Intrinsic geometric cobar complex) :: \ref{def:geom-cobar-intrinsic} give the formal versions used in the
42: ref def:geom-cobar-intrinsic -> 262 (definition Intrinsic geometric cobar complex) :: (Definition~\ref{def:geom-cobar-intrinsic}), where
120: ref def:factorization-coalgebra -> 235 (definition Factorization coalgebra) :: Definition~\ref{def:factorization-coalgebra});

FILE chapters/theory/chiral_koszul_pairs.tex
73: ref def:chiral-twisting-datum -> 216 (definition Chiral twisting datum) :: Definitions~\ref{def:chiral-twisting-datum},
74: ref def:chiral-koszul-morphism -> 268 (definition Chiral Koszul morphism) :: \ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
74: ref def:chiral-koszul-pair -> 658 (definition Chiral Koszul pair) :: \ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
115: ref def:chiral-twisting-datum -> 216 (definition Chiral twisting datum) :: (Definition~\ref{def:chiral-twisting-datum}) lives in the chiral
156: ref def:chiral-koszul-pair -> 658 (definition Chiral Koszul pair) :: pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..b3e2e395162ee60de7bf699a1e415abb12318789
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -1516,6 +1517,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the


thinking
**Fixing code references**

I think there's just one additional fix needed in bar_construction at line 575. The other references are pretty clear because they connect informal definitions to formal ones. Line 42 in cobar and lines 115/156 seem alright too, as they also reference later definitions. However, I should patch line 575 to define epsilon_geom inline instead of being purely conventional. Removing comment line 641 might be useful since it isn’t visible to readers, but ultimately, let’s focus on fixing line 575 first.
codex
One remaining local notation gap is still visible in `bar_construction.tex`: the orientation sign `\epsilon_{\mathrm{geom}}(D_{ij})` is named before it is explained. I’m fixing that inline rather than sending the reader ahead to the later sign convention.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex
@@ -574,3 +574,5 @@
 \[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
-where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
+where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
+boundary orientation of the collision divisor~$D_{ij}$; the full sign
+package is fixed in Convention~\ref{conv:orientations-enhanced}.
 
apply_patch(auto_approved=true) exited 0 in 31ms:
Success. Updated the following files:
M chapters/theory/bar_construction.tex
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..98e375b855169cfe3ce98ca5a787221d548f2e93
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -571,7 +572,9 @@
 
 The explicit formula for the sign is:
 \[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
-where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
+where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
+boundary orientation of the collision divisor~$D_{ij}$; the full sign
+package is fixed in Convention~\ref{conv:orientations-enhanced}.
 
 \emph{Component 3: Form differential $d_{\text{form}}$.}
 
@@ -1516,6 +1519,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..98e375b855169cfe3ce98ca5a787221d548f2e93
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -571,7 +572,9 @@
 
 The explicit formula for the sign is:
 \[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
-where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
+where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
+boundary orientation of the collision divisor~$D_{ij}$; the full sign
+package is fixed in Convention~\ref{conv:orientations-enhanced}.
 
 \emph{Component 3: Form differential $d_{\text{form}}$.}
 
@@ -1516,6 +1519,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the


thinking
**Evaluating bar construction**

I'm thinking about whether I need to address any other local symbol gaps. In the `bar_construction` script, I'm focusing on the `def:geom-bar`, which seems okay since the orientation is already described. Maybe I should accept this as is? I could quickly re-run the forward references list to check for any potential issues. Just trying to ensure everything is aligned properly!
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib
files = [
    'chapters/theory/bar_construction.tex',
    'chapters/theory/cobar_construction.tex',
    'chapters/theory/chiral_koszul_pairs.tex',
]
label_re = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_re = re.compile(r'\\\\(?:ref|eqref|autoref|Cref|cref)\\{(["'^}]+)'"\\}')
env_re = re.compile(r'\\\\begin\\{(definition|convention|notation)\\}(?:\\[(["'^'"\\]]*)\\])?')
for path in files:
    text = pathlib.Path(path).read_text()
    lines = text.splitlines()
    labels = {}
    env = None; title = None
    for i,l in enumerate(lines, start=1):
        m = env_re.search(l)
        if m:
            env = m.group(1); title = m.group(2) or ''
        for lm in label_re.finditer(l):
            if env:
                labels[lm.group(1)] = (i, env, title)
        if re.search(r'\\\\end\\{(definition|convention|notation)\\}', l):
            env = None; title = None
    print('\\nFILE', path)
    for i,l in enumerate(lines, start=1):
        for rm in ref_re.finditer(l):
            key = rm.group(1)
            if key in labels and labels[key][0] > i:
                print(f'{i}: ref {key} -> {labels[key][0]} ({labels[key][1]} {labels[key][2]}) :: {l.strip()}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

FILE chapters/theory/bar_construction.tex
435: ref def:geom-bar -> 1720 (definition Genus-graded geometric bar complex) :: Definition~\ref{def:geom-bar} below.
577: ref conv:orientations-enhanced -> 647 (convention Enhanced sign system) :: package is fixed in Convention~\ref{conv:orientations-enhanced}.
643: ref def:orientation -> 1411 (definition Orientation line bundle) :: % Orientation bundle: see Definition~\ref{def:orientation} below.

FILE chapters/theory/cobar_construction.tex
11: ref def:factorization-coalgebra -> 235 (definition Factorization coalgebra) :: configuration spaces. Definitions~\ref{def:factorization-coalgebra},
12: ref def:conilpotent-cobar -> 209 (definition Conilpotent coalgebra) :: \ref{def:conilpotent-cobar}, and
13: ref def:geom-cobar-intrinsic -> 262 (definition Intrinsic geometric cobar complex) :: \ref{def:geom-cobar-intrinsic} give the formal versions used in the
42: ref def:geom-cobar-intrinsic -> 262 (definition Intrinsic geometric cobar complex) :: (Definition~\ref{def:geom-cobar-intrinsic}), where
120: ref def:factorization-coalgebra -> 235 (definition Factorization coalgebra) :: Definition~\ref{def:factorization-coalgebra});

FILE chapters/theory/chiral_koszul_pairs.tex
73: ref def:chiral-twisting-datum -> 216 (definition Chiral twisting datum) :: Definitions~\ref{def:chiral-twisting-datum},
74: ref def:chiral-koszul-morphism -> 268 (definition Chiral Koszul morphism) :: \ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
74: ref def:chiral-koszul-pair -> 658 (definition Chiral Koszul pair) :: \ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
115: ref def:chiral-twisting-datum -> 216 (definition Chiral twisting datum) :: (Definition~\ref{def:chiral-twisting-datum}) lives in the chiral
156: ref def:chiral-koszul-pair -> 658 (definition Chiral Koszul pair) :: pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..98e375b855169cfe3ce98ca5a787221d548f2e93
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -571,7 +572,9 @@
 
 The explicit formula for the sign is:
 \[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
-where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
+where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
+boundary orientation of the collision divisor~$D_{ij}$; the full sign
+package is fixed in Convention~\ref{conv:orientations-enhanced}.
 
 \emph{Component 3: Form differential $d_{\text{form}}$.}
 
@@ -1516,6 +1519,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the




thinking
**Calculating findings and fixes**

I need to compute the exact line numbers for all findings and fixes after the final patch. I have several findings within the `bar_construction`, `cobar_construction`, and `chiral_koszul_pairs` files. That's at least five total, and it seems I've found an extra one beyond what was initially explored. I should mention these findings, ensuring that there are no define-before-use issues in the rest of the assigned scope after my audit. For instance, I need to specify the problematic line numbers, especially line 4 for `cobar_construction`.
thinking
**Finalizing bar functor report**

The bar functor paragraph starts at line 16 after our recent insertion. There was originally a problem at line 4, possibly before the patch. I need to ensure the final report cites the current line number where the issue was, specifically in `chapters/theory/cobar_construction.tex` at line 16. However, the task specifies to mention the "PROBLEM at file:line" along with the exact edit that was applied, especially since we've made changes to the lines.
thinking
**Ensuring final clarity**

I want to keep the final version concise, so I might consider using a bullet list to summarize my findings. It’s also important to mention verification; I can say, "Verification: I re-audited the three files for forward definition references, and only deliberate forward pointers remain, with informal definitions before the first symbol use." I didn’t run a full TeX build, but that seems good. Now, I’d like to get the line numbers for `epsilon_geom`, around 573-579.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '572,579p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Opening notation|Standing notation for the overview|sign line that records|iterated reduced coproduct vanishes on|boundary orientation of the collision divisor" chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   572	
   573	The explicit formula for the sign is:
   574	\[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
   575	where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
   576	boundary orientation of the collision divisor~$D_{ij}$; the full sign
   577	package is fixed in Convention~\ref{conv:orientations-enhanced}.
   578	
   579	\emph{Component 3: Form differential $d_{\text{form}}$.}
 succeeded in 51ms:
chapters/theory/bar_construction.tex:433:orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
chapters/theory/bar_construction.tex:576:boundary orientation of the collision divisor~$D_{ij}$; the full sign
chapters/theory/bar_construction.tex:1522:(that is, dg coalgebras whose iterated reduced coproduct vanishes on
chapters/theory/cobar_construction.tex:4:\smallskip\noindent\textit{Opening notation.}
chapters/theory/cobar_construction.tex:7:factorization coalgebra whose iterated reduced coproduct vanishes on
chapters/theory/chiral_koszul_pairs.tex:61:\smallskip\noindent\textit{Standing notation for the overview.}
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..98e375b855169cfe3ce98ca5a787221d548f2e93
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -571,7 +572,9 @@
 
 The explicit formula for the sign is:
 \[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
-where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
+where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
+boundary orientation of the collision divisor~$D_{ij}$; the full sign
+package is fixed in Convention~\ref{conv:orientations-enhanced}.
 
 \emph{Component 3: Form differential $d_{\text{form}}$.}
 
@@ -1516,6 +1519,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the


thinking
**Updating the plan**

I've completed step 1, step 2, and step 3. Now, it seems like it's a good time to update the plan to reflect our progress. It feels satisfying to see the steps checked off! I want to make sure we're on track, so let’s get this updated and move on to the next phase. Keeping everything organized will help us stay focused and effective!
Plan update
Completed the targeted define-before-use audit of the three assigned theory chapters, applied only local notation repairs, and re-checked the repaired first-use sites. Only deliberate forward pointers to later formal definitions remain.
  ✓ Load required repo context and audit target chapters for define-before-use violations
  ✓ Patch only the assigned theory chapters with minimum truthful edits
  ✓ Verify the repaired surfaces and summarize each finding with exact edit applied
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..98e375b855169cfe3ce98ca5a787221d548f2e93
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -571,7 +572,9 @@
 
 The explicit formula for the sign is:
 \[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
-where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
+where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
+boundary orientation of the collision divisor~$D_{ij}$; the full sign
+package is fixed in Convention~\ref{conv:orientations-enhanced}.
 
 \emph{Component 3: Form differential $d_{\text{form}}$.}
 
@@ -1516,6 +1519,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

codex
Findings and fixes:

- PROBLEM at [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:433): `\mathrm{or}_{p+1}^{(g)}` appeared in the preview definition before the object itself was explained. EXACT edit applied: changed `orientation bundle \mathrm{or}_{p+1}^{(g)}, is given in...` to `orientation bundle \mathrm{or}_{p+1}^{(g)}, the sign line that records orientations of the codimension-$p$ collision strata at genus~$g$, is given in...`.

- PROBLEM at [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:574): `\epsilon_{\mathrm{geom}}(D_{ij})` was used before its meaning was stated. EXACT edit applied: replaced `where \epsilon_{\text{geom}}(D_{ij}) = 0 or 1 depending on orientation convention` with `where \epsilon_{\text{geom}}(D_{ij}) \in \{0,1\} is the parity of the boundary orientation of the collision divisor~D_{ij}; the full sign package is fixed in Convention~\ref{conv:orientations-enhanced}.`

- PROBLEM at [bar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex:1519): `conilpotent dg coalgebras` was invoked in the proof before the chapter explained the term. EXACT edit applied: inserted the inline gloss `(that is, dg coalgebras whose iterated reduced coproduct vanishes on every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})`.

- PROBLEM at [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:16): the opening overview used `\barB(\cA)`, “conilpotent chiral coalgebra”, and `\Omega^{\mathrm{ch}}(\cC)` before local definition. EXACT edit applied: inserted an opening paragraph at lines 4-14 beginning `\smallskip\noindent\textit{Opening notation.}` that defines those three objects informally and points to Definitions `\ref{def:factorization-coalgebra}`, `\ref{def:conilpotent-cobar}`, and `\ref{def:geom-cobar-intrinsic}`.

- PROBLEM at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:67): the overview invoked `(\cA,\cC,\tau,F_\bullet)`, `K_\tau^L`, `K_\tau^R`, `\Theta_\cA^{\le r}`, and “chiral Koszul pair” before local introduction. EXACT edit applied: inserted a standing-notation paragraph at lines 61-75 beginning `\smallskip\noindent\textit{Standing notation for the overview.}` that defines the twisting datum, the twisted tensor products, the truncations `\Theta_\cA^{\le r}`, and the informal meaning of a chiral Koszul pair before the overview uses them.

Verification: I re-ran a targeted forward-definition pass on the three assigned files. The remaining forward references are deliberate pointers to later formal definitions or comments, not surviving use-before-introduction violations. I did not run a full TeX build.
file update:
diff --git a/chapters/theory/bar_construction.tex b/chapters/theory/bar_construction.tex
index 99acb94d113898b6cd79da04f2cebc0957c7c2e1..98e375b855169cfe3ce98ca5a787221d548f2e93
--- a/chapters/theory/bar_construction.tex
+++ b/chapters/theory/bar_construction.tex
@@ -430,7 +430,8 @@
 $\bar{B}(\mathcal{A}) = \bigoplus_{g \geq 0} \bar{B}^{(g)}(\mathcal{A})$.
 The complete definition, incorporating the bigrading by bar
 degree~$p$ and form degree~$q$ together with the genus-graded
-orientation bundle $\mathrm{or}_{p+1}^{(g)}$, is given in
+orientation bundle $\mathrm{or}_{p+1}^{(g)}$, the sign line that records
+orientations of the codimension-$p$ collision strata at genus~$g$, is given in
 Definition~\ref{def:geom-bar} below.
 \end{definition}
 
@@ -571,7 +572,9 @@
 
 The explicit formula for the sign is:
 \[\sigma_{ij} = \left(\sum_{k=0}^{i-1} |\phi_k|\right) + \left(\sum_{k=i+1}^{j-1} |\phi_k|\right) + |\phi_i| + \epsilon_{\text{geom}}(D_{ij})\]
-where $\epsilon_{\text{geom}}(D_{ij}) = 0$ or $1$ depending on orientation convention (see Convention \ref{conv:orientations-enhanced}).
+where $\epsilon_{\text{geom}}(D_{ij}) \in \{0,1\}$ is the parity of the
+boundary orientation of the collision divisor~$D_{ij}$; the full sign
+package is fixed in Convention~\ref{conv:orientations-enhanced}.
 
 \emph{Component 3: Form differential $d_{\text{form}}$.}
 
@@ -1516,6 +1519,8 @@
 \begin{proof}
 Both presentations are cofibrant-fibrant objects in the model structure
 on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
+(that is, dg coalgebras whose iterated reduced coproduct vanishes on
+every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
 (Positselski~\cite{Positselski11}, Theorem~8.1). Cofibrant-fibrant
 replacements in this model structure are unique up to a contractible
 space of weak equivalences: the mapping space
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 62a0bff7974bdbb3e60c7e3e246fa27a2ea0c685..33da923da80bfdc3b56e8067b404e53712aa3a1e
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -58,6 +58,22 @@
 achieves (b) but has no bar-cobar content; complementarity (c)
 requires both (a) and (b) as input.
 
+\smallskip\noindent\textit{Standing notation for the overview.}
+A chiral twisting datum means a quadruple
+$(\cA,\cC,\tau,F_\bullet)$ consisting of an augmented chiral algebra,
+a conilpotent complete factorization coalgebra, a degree-$+1$
+twisting morphism $\tau\colon \cC\to \cA$ satisfying the
+Maurer--Cartan equation, and a compatible filtration. We write
+$K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ for the corresponding
+twisted tensor products, and $\Theta_\cA^{\leq r}$ for the degree-$r$
+truncation of the universal Maurer--Cartan element of the modular
+convolution algebra. A chiral Koszul pair is such a datum on the
+Koszul locus, so the twisted tensor products are acyclic and the
+associated graded datum is classically Koszul.
+Definitions~\ref{def:chiral-twisting-datum},
+\ref{def:chiral-koszul-morphism}, and \ref{def:chiral-koszul-pair}
+record the precise versions used below.
+
 Theorem~\ref{thm:koszul-equivalences-meta} assembles twelve
 tests and consequences around chiral Koszulness. Nine are
 unconditional equivalences: $E_2$-collapse of the bar spectral sequence,
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 10f06dec9f30ec59d13bca273a7efdec2fe5c26a..e913d18a61d60818bb5d356d3cd777b14c2a82e4
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -1,6 +1,18 @@
 \chapter{The geometric cobar complex}
 \label{chap:cobar-construction}
 
+\smallskip\noindent\textit{Opening notation.}
+In the overview below, $\barB(\cA)$ denotes the symmetric factorization
+bar coalgebra of~$\cA$; a conilpotent chiral coalgebra means a
+factorization coalgebra whose iterated reduced coproduct vanishes on
+every local section; and
+$\Omega^{\mathrm{ch}}(\cC)=\bigoplus_{n\geq 0}\Omega^{\mathrm{ch}}_n(\cC)$
+denotes the geometric cobar complex obtained by Verdier duality on
+configuration spaces. Definitions~\ref{def:factorization-coalgebra},
+\ref{def:conilpotent-cobar}, and
+\ref{def:geom-cobar-intrinsic} give the formal versions used in the
+rest of the chapter.
+
 The bar functor destroys the algebra: it encodes~$\cA$ as a
 factorization coalgebra $\barB(\cA)$ from which no multiplication
 is directly visible. The cobar complex $\Omega(\cC)$ is the

tokens used
119,294
