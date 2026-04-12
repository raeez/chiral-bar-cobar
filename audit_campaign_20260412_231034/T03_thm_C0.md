# T03_thm_C0 (570s, gpt-5.4)

- [CRITICAL] [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:238); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:258); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:350) — C0 and its prerequisite `lem:perfectness-criterion` are built on the fiber bar object with the curved differential `\dfib`, but then take ordinary `H^q`, `R^q\pi_*`, spectral-sequence cohomology, and EGA base change of that object. The repo’s own convention says `\dfib^2=\kappa(\cA)\omega_g` and that this lives in the coderived category; only `\Dg{g}` is a strict differential. On the stated `curved-central` surface, Steps 2–4 are therefore not well-typed unless one adds a flat-side comparison / replaces `\dfib` / restricts to a flat case such as `\kappa=0` (inference from the cited convention).

- [CRITICAL] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:411); [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:873); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:575); [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2645) — Step 3’s key identification does not follow from the cited source. `cor:bar-cohomology-koszul-dual` computes genus-0 bar cohomology/Koszul-dual data under PBW hypotheses; it does not identify that object with the center local system. But D4 defines `\mathcal Z_\cA` separately as the sheaf whose fiber is `Z(\cA|_\Sigma)`, and the introduction explicitly separates bar coalgebra/Koszul dual from center-type objects. The proof’s jump from “surviving bar cohomology/Koszul dual” to “center local system” is the main logical gap.

- [HIGH] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:357); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:385); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:283); [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:697) — Hidden hypothesis/regime inflation: C0 is tagged only `curved-central`, but the proof imports the `filtered-complete` PBW lane (`gr_F\cA`, “classical Koszul/Ext complex”, PBW bar-cohomology corollary, PBW filterability). Those hypotheses appear in the PBW criterion and in `lem:perfectness-criterion`, but they are not stated in the theorem surface itself.

- [HIGH] [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:99); [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1186) — Cross-volume propagation is live: Volume II already uses C0 to rewrite the ambient complex and to identify the `E_\infty` page with `\mathcal Z(\cA)`. Since C0’s proof is unsound, these downstream arguments inherit an unsupported premise.

- [MEDIUM] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:43); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:698); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:740); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1548); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1598) — “Unconditional on the Koszul locus” is not “all families” in the live manuscript surface. MK1–MK3 are only verified here for Heisenberg at nonzero level, free fermion/`βγ`-`bc`, generic affine Kac–Moody, generic Virasoro, and generic principal finite-type `\mathcal W`. Boundary/non-generic cases are outside the proved input surface.

## Summary
Instances checked: 10 | Violations found: 5 | Verdict: FAIL


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
session id: 019d8388-33ab-7ae1-9956-f4bcd575c2e2
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


MISSION: FALSIFY the proof of Theorem C0: fiber-center identification (unconditional). Check: (a) what exactly is identified? (b) is it really unconditional or are there hidden hypotheses? (c) does it work for ALL families or only specific ones?

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
Using `deep-beilinson-audit` for the adversarial proof audit and `multi-path-verify` for stepwise falsification checks. I’m starting by locating Theorem C0 and its dependency surface across `chapters/`, then I’ll read the full statement, proof, and cited results before assessing whether the “unconditional” claim survives scrutiny.

thinking
**Reading skill documentation**

I need to dive into the relevant skill docs and consider using the commentary tool to execute a command, maybe "cat". Since I'm in the commentary channel, it could be helpful to read multiple files in parallel using that multi_tool_use.parallel function. I might also think about updating my plan based on what I find, although it’s not strictly necessary. I'll focus on sections like CLAUDE, concordance, and relevant summaries to locate the theorem.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Theorem C0|thm:.*C0|fiber-center|center identification|fiber center" chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

 succeeded in 52ms:
chapters/connections/thqg_open_closed_realization.tex:524:\item \emph{Derived center identification.}
chapters/connections/ym_instanton_screening.tex:410:facewise to the visible tangent-to-center identification of Theorem~\ref{thm:screened-tangent-center}.
chapters/connections/thqg_symplectic_polarization.tex:105:(Theorem~\ref{thm:fiber-center-identification}) gives
chapters/connections/thqg_symplectic_polarization.tex:1122:sequence. By the fiber--center identification
chapters/connections/thqg_symplectic_polarization.tex:1123:(Theorem~\ref{thm:fiber-center-identification}), the
chapters/theory/chiral_koszul_pairs.tex:5918: (Theorem~\ref{thm:fiber-center-identification}).
chapters/theory/higher_genus_complementarity.tex:43:\item \emph{Fiber--center identification
chapters/theory/higher_genus_complementarity.tex:49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
chapters/theory/higher_genus_complementarity.tex:93:The fiber--center identification~(C0) and the
chapters/theory/higher_genus_complementarity.tex:350:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:351:\label{thm:fiber-center-identification}
chapters/theory/higher_genus_complementarity.tex:352:\index{fiber--center identification|textbf}
chapters/theory/higher_genus_complementarity.tex:364:\begin{equation}\label{eq:fiber-center}
chapters/theory/higher_genus_complementarity.tex:433:Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center


thinking
**Planning file and theorem analysis**

I need to read the required files and target file related to the theorem, along with possibly checking the theorem registry and concordance entry. I wonder if I should use the explorer or proceed with the exec. The developer mentions using explorer for codebase questions, so I’ll stick with that. I should ask explorers first, especially since we’ve already used exec to locate the theorem. I might also use multiple explorers to analyze dependencies and manage requests efficiently. Let's spawn them!
thinking
**Deciding on explorer usage**

It’s clear that the skill guidance suggests using the explorer for codebase questions. The developer emphasized this point, so I should definitely stick to using one explorer. It seems like parallel usage isn’t necessary or allowed unless there’s an explicit request for it. Therefore, I’ll move forward with just one explorer for now. This way, I can keep things straightforward and avoid any unnecessary complexity.
codex
I’ve located the theorem surface in `chapters/theory/higher_genus_complementarity.tex`. Next I’m loading the repo’s status/concordance sources and extracting the proof’s dependency chain so I can test each imported step against its actual hypotheses.
collab spawn_agent(call_4ylmR5ZdIbFqhn0ToEMwiLoN, prompt="<task>Audit theorem C0 in this repo. Find the exact statement and proof of Theorem~\ref{thm:fiber-center-identification}…")
spawn_agent(call_4ylmR5ZdIbFqhn0ToEMwiLoN, prompt="<task>Audit theorem C0 in this repo. Find the exact statement and proof of Theorem~\ref{thm:fiber-center-identification}…") pending init:
  agent: 019d8388-a411-7811-a31b-c12e30d7af4a
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar

exec
/bin/zsh -lc 'ls .agents/skills' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
beilinson-rectify
build-surface
chriss-ginzburg-rectify
claim-surface-sync
compute-engine-scaffold
cross-volume-propagation
deep-beilinson-audit
frontier-research
multi-path-verify
thinking
**Planning updates**

I’m thinking about how to read the required files and theorems, and it seems like using parallel execution could speed things up. I wonder if I should plan an update? It might make sense to set an update plan; that could help keep everything organized and ensure I'm on track. I’ll consider the best way to implement this plan. It feels like I'm getting closer to what I need to do!
Plan update
Running an adversarial audit of Theorem C0 by fixing the exact theorem surface, reading its proof and dependency sources, then checking scope/status propagation and boundary cases before reporting only verified findings.
  → Load constitutional/status sources and the theorem surface
  • Trace each proof step to cited dependencies and test hypotheses/scope
  • Check cross-file and cross-volume propagation for status or scope drift
  • Re-verify surviving findings and prepare severity-ordered report
exec
/bin/zsh -lc 'cat .agents/skills/deep-beilinson-audit/SKILL.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc 'cat CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 977

# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '320,470p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "fiber-center|C0|higher_genus_complementarity|thm:fiber-center-identification" chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md 2>/dev/null' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
$H^q(\operatorname{gr}_F\bar{B}^{(g)}(\cA)\big|_\Sigma) = 0$
for $q \neq 0$ at every point of the base.

\emph{Step~2: Transfer to the filtered complex.}
The bar-degree filtration spectral sequence
$E_1^{p,q} =
H^q(\operatorname{gr}_p\bar{B}^{(g)}(\cA)\big|_\Sigma)$
has $E_1^{p,q} = 0$ for $q \neq 0$ by Step~1. All higher
differentials $d_r$ ($r \geq 2$) therefore vanish (they map into
or out of the zero row), and the spectral sequence collapses at
$E_2$ with $E_\infty^{p,0} = E_2^{p,0}$. In particular, the
full fiber complex $\bar{B}^{(g)}(\cA)\big|_\Sigma$ has
cohomology concentrated in degree~$0$ for every~$\Sigma$.
The uniform vanishing range $q \neq 0$ is independent
of~$[\Sigma]$.

\emph{Step~3: Cohomology and base change.}
The family
$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$
is a proper morphism of finite type. By Steps~1--2, the fiber
 exited 2 in 51ms:
metadata/theorem_registry.md:61:| `chapters/theory/higher_genus_complementarity.tex` | 79 |
metadata/theorem_registry.md:701:#### `chapters/theory/higher_genus_complementarity.tex` (79)
metadata/theorem_registry.md:707:| `thm:fiber-center-identification` | `theorem` | 330 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
exec
/bin/zsh -lc 'rg -n "thm:fiber-center-identification" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
351:\label{thm:fiber-center-identification}
exec
/bin/zsh -lc "sed -n '300,420p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
Then the derived pushforward
$R\pi_{g*}\bar{B}^{(g)}(\cA)$ is a perfect complex on
$\overline{\mathcal{M}}_g$.
\end{lemma}

\begin{proof}
The argument has three steps.

\emph{Step~1: Uniform cohomological bound from the associated graded.}
The PBW filtration~$F_\bullet$ is flat over the base
$\overline{\mathcal{M}}_g$ (it is a bar-degree filtration,
hence defined fiber-by-fiber by the combinatorial bar grading).
At the associated graded level the fiberwise
curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes
(it sits in positive filtration degree), so
$\operatorname{gr}_F$ carries only the genus-$0$
differential~$\dzero$. By Koszul acyclicity~(i), the
cohomology of $\operatorname{gr}_F$ is concentrated in total
degree~$0$, giving a uniform vanishing range
exec
/bin/zsh -lc "sed -n '420,520p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$.
The fiber-level concentration from Step~3 gives
$R^q\pi_{g*}\bar{B}^{(g)}(\cA) = 0$ for $q \neq 0$.
Perfectness of $R\pi_{g*}\bar{B}^{(g)}(\cA)$
(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
uniformly over $\overline{\mathcal{M}}_g$.
The surviving $R^0\pi_{g*}$ is identified with
$\mathcal{Z}_{\cA}$ by the fiber-level identification
from Step~3, which holds uniformly over the base.
\end{proof}

\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
\index{Theorem C!decomposition}
Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
identification, this theorem) produces the ambient complex;
$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
gives the Verdier eigenspace decomposition and its Lagrangian
splitting; $\mathrm{C}_2$
(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
conditional bar-side BV / shifted-symplectic upgrade.
exec
/bin/zsh -lc 'rg -n "fiber-center" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md:488:| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
metadata/dependency_graph.dot:2748:  thm_fiber_center_identification [label="thm:fiber-center-identification\ntheorem [Pr]\nFiber--center identification \textup{(Th...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:707:| `thm:fiber-center-identification` | `theorem` | 330 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
metadata/label_index.json:11986:  "eq:fiber-center": {
metadata/label_index.json:46974:  "thm:fiber-center-identification": {
metadata/claims.jsonl:2643:{"label": "thm:fiber-center-identification", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 330, "title": "Fiber--center identification \\textup{(Theorem~\\texorpdfstring{$\\mathrm{C}_0$}{C0})}", "labels_in_block": ["thm:fiber-center-identification", "eq:fiber-center"], "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral", "lem:perfectness-criterion"]}
scripts/adversarial_campaign.py:128:    ("T03_thm_C0", "Theorem C0: fiber-center identification (unconditional). Check: (a) what exactly is identified? (b) is it really unconditional or are there hidden hypotheses? (c) does it work for ALL families or only specific ones?"),
AGENTS.md:549:| C | PROVED | C0 (fiber-center) unconditional, C1 (Lagrangian) unconditional, C2 (BV) conditional |
chapters/connections/thqg_symplectic_polarization.tex:105:(Theorem~\ref{thm:fiber-center-identification}) gives
chapters/connections/thqg_symplectic_polarization.tex:1123:(Theorem~\ref{thm:fiber-center-identification}), the
audit_campaign_20260412_230832/T03_thm_C0.md:52:MISSION: FALSIFY the proof of Theorem C0: fiber-center identification (unconditional). Check: (a) what exactly is identified? (b) is it really unconditional or are there hidden hypotheses? (c) does it work for ALL families or only specific ones?
chapters/theory/chiral_koszul_pairs.tex:5918: (Theorem~\ref{thm:fiber-center-identification}).
chapters/theory/higher_genus_complementarity.tex:49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
chapters/theory/higher_genus_complementarity.tex:351:\label{thm:fiber-center-identification}
chapters/theory/higher_genus_complementarity.tex:364:\begin{equation}\label{eq:fiber-center}
chapters/theory/higher_genus_complementarity.tex:433:Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
compute/audit/algebraic_integration/derived_global_sections.md:33:### 1.2 The fiber-center identification
compute/audit/algebraic_integration/derived_global_sections.md:35:**Theorem C_0** (thm:fiber-center-identification, higher_genus_complementarity.tex line 324):
compute/audit/algebraic_integration/derived_global_sections.md:283:**Answer**: The center local system Z_A, whose fiber over [Sigma_g] is Z(A|_{Sigma_g}) = the commutant of A in itself. This is proved by the fiber-center identification (thm:fiber-center-identification): R^0 pi_{g*} B-bar^{(g)}(A) = Z_A, with higher R^q vanishing (Koszulness concentration).
codex
The statement/proof is now fixed. The next pass is dependency attack: I’m tracing `MK1`, `lem:perfectness-criterion`, `cor:bar-cohomology-koszul-dual`, the definition of `\mathcal Z_\mathcal A`, and the exact meaning of the fiber complex to see whether Step 2–4 actually justify an unconditional identification.
exec
/bin/zsh -lc "sed -n '250,360p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5860,5965p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"lem:perfectness-criterion|cor:bar-cohomology-koszul-dual|def:modular-koszul-chiral|conv:regime-tags|MK1|center local system|Z_\\\\cA|\\\\mathcal\\{Z\\}_\\\\cA|C\\"'^'"\\{\\(g\\)\\}_X|\\\\mathbf\\{C\\}_g\\(\\\\cA\\)|fiber complex\" chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/algebraic_foundations.tex chapters/connections/concordance.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:lem:perfectness-criterion|cor:bar-cohomology-koszul-dual|def:modular-koszul-chiral|conv:regime-tags|MK1|center local system|Z_\cA|\mathcal\{Z\}_\cA|C\^\{\(g\)\}_X|\mathbf\{C\}_g\(\cA\)|fiber complex)
                                                                                                                                     ^^
error: unrecognized escape sequence
 succeeded in 51ms:
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
\emph{genus-$g$ fiber bar complex}
$C^{(g)}_X(\cA)\!\mid_\Sigma$, i.e.\ the bar complex of~$\cA$
 succeeded in 51ms:

% ================================================================
% SECTION 8.8: COMPUTATIONAL METHODS
% ================================================================

\section{Computational methods and verification}

\subsection{Algorithm for checking Koszul pairs}

\begin{construction}[Verification of Koszul pairs]\label{con:verify-koszul-pair}
Given chiral algebras $\mathcal{A}_1, \mathcal{A}_2$, one verifies whether they form a Koszul pair as follows.
In the quadratic case, extract generators and relations, check that the residue pairing is perfect, and verify orthogonality $R_1 \perp R_2$.
In the non-quadratic case, compute $\bar{B}^{\leq 3}(\mathcal{A}_i)$ geometrically, form the Koszul complexes $K_*(\mathcal{A}_i, \mathcal{A}_j)$, and check acyclicity in degrees $1,2,3$.
In both cases, verify bar-cobar quasi-isomorphisms to degree~$3$.
\end{construction}

\subsection{Complexity analysis}

For $n$ generators, $m$ relations, verification to degree $k$:
\begin{itemize}


thinking
**Gathering cross-volume references**

I'm compiling a list of all occurrences of 'fiber-center identification' and its theorem label across different volumes and directories, focusing on files both within this repo and in adjacent volume folders to identify any potential scope or status drift. I'll highlight each file and line number where these mentions appear to map dependencies and cross-volume connections clearly.
exec
/bin/zsh -lc 'rg -n "fiber-center identification" -n ../chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "thm:fiber-center-identification" ../chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
../chiral-bar-cobar-vol2/main.tex:936:\phantomsection\label{V1-thm:fiber-center-identification}%
../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:101:(Theorem~\ref{V1-thm:fiber-center-identification}) gives
../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1187:(Theorem~\ref{V1-thm:fiber-center-identification}), the
thinking
**Searching for definitions**

I’m thinking I need to look into the A1 theorem bar concentration and find a definition for modular pre-Koszul datum. Maybe it’s a good idea to simplify things a bit with rg. I wonder how these terms relate to one another and what I can uncover. Let’s see what’s out there and clarify some of these concepts!
exec
/bin/zsh -lc "sed -n '1,180p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'def:modular-koszul-chiral|MK1|MK2|MK3|modular pre-Koszul datum' chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_koszul_pairs.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'cor:bar-cohomology-koszul-dual|bar cohomology|Koszul dual coalgebra|center local system|def:center-local-system|Z_A|mathcal\\{Z\\}_\\{?\\\\cA\\}?|derived center' chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_koszul_pairs.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:45: For every chiral algebra~$\cA$ carrying a modular pre-Koszul datum
chapters/theory/higher_genus_complementarity.tex:281:curve~$X$, carrying a modular pre-Koszul datum
chapters/theory/higher_genus_complementarity.tex:282:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_complementarity.tex:290: Koszul-acyclic \textup{(}axioms \textup{MK1} and
chapters/theory/higher_genus_complementarity.tex:291: \textup{MK3} of
chapters/theory/higher_genus_complementarity.tex:292: Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_complementarity.tex:357:Assume $\cA$ carries a modular pre-Koszul datum
chapters/theory/higher_genus_complementarity.tex:358:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
chapters/theory/higher_genus_complementarity.tex:390:By genus-$0$ Koszulity (axiom~MK1), the associated graded is
chapters/theory/higher_genus_complementarity.tex:4024:(Definition~\ref{def:modular-koszul-chiral}), the PBW spectral
chapters/theory/higher_genus_complementarity.tex:4111:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
chapters/theory/higher_genus_complementarity.tex:4112:axioms \textup{MK1--MK3)}.
chapters/theory/higher_genus_complementarity.tex:4260:Theorem~B requires Koszulity (MK1). For simple admissible affine
chapters/examples/landscape_census.tex:2894:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})},
chapters/connections/thqg_holographic_reconstruction.tex:66:(Definition~\ref{def:modular-koszul-chiral}) with
chapters/connections/editorial_constitution.tex:214:the universal semisimple statement extends MK3 beyond those families
chapters/connections/editorial_constitution.tex:2487: Definition~\ref{def:modular-koszul-chiral} provides the dg bar
chapters/connections/editorial_constitution.tex:2523:Definition~\ref{def:modular-koszul-chiral}, and its three
chapters/theory/algebraic_foundations.tex:252:of Definition~\ref{def:modular-koszul-chiral}:
chapters/theory/algebraic_foundations.tex:268:The full dg model with axioms~(MK1)--(MK3) and data~(D1)--(D6)
 succeeded in 51ms:
Total output lines: 695

chapters/theory/higher_genus_complementarity.tex:48: with $R^0\pi_{g*}\bar{B}^{(g)}(\cA) \cong \mathcal{Z}_{\cA}$
chapters/theory/higher_genus_complementarity.tex:106:(finite-dimensional bar cohomology at each weight). In particular, hypothesis~(P2) (nondegeneracy) implies
chapters/theory/higher_genus_complementarity.tex:191:where $\mathcal{Z}(\cA)$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:369:\;\cong\; \mathcal{Z}_{\cA}
chapters/theory/higher_genus_complementarity.tex:372:where $\mathcal{Z}_{\cA}$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:413:which is identified with the Koszul dual coalgebra and
chapters/theory/higher_genus_complementarity.tex:414:hence with the center $\mathcal{Z}_{\cA}\!\mid_\Sigma$
chapters/theory/higher_genus_complementarity.tex:416:(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/theory/higher_genus_complementarity.tex:427:$\mathcal{Z}_{\cA}$ by the fiber-level identification
chapters/theory/higher_genus_complementarity.tex:871:piece captures the part of bar cohomology coming from genus~$g$,
chapters/theory/higher_genus_complementarity.tex:1790:\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
chapters/theory/higher_genus_complementarity.tex:1812:The center local system $\mathcal{Z}(\cA)$ on
chapters/theory/higher_genus_complementarity.tex:2622:\item Bar complex: $\bar{B}(\mathcal{F}) = \Lambda^{*,c}(\psi^*, \partial\psi^*, \ldots)$ (exterior coalgebra, the Koszul dual coalgebra).
chapters/theory/higher_genus_complementarity.tex:4219:by~$r$ steps, and the Koszul concentration (all bar cohomology
chapters/theory/higher_genus_complementarity.tex:4222:Corollary~\ref{cor:bar-cohomology-koszul-dual}, Step~4, applied
chapters/theory/higher_genus_complementarity.tex:5818:by the bar cohomology $H^*(\barB(\cA))$, which depends polynomially
chapters/theory/chiral_koszul_pairs.tex:13:when bar cohomology is concentrated in degree one, and the
chapters/theory/chiral_koszul_pairs.tex:82:Koszulness is the condition that bar cohomology is concentrated
exec
/bin/zsh -lc 'rg -n "fiber-center" -n ../calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Researching definitions**

I need to look up the definition of "modular pre-Koszul datum" within the context of "higher_genus_modular_koszul." Also, I should check "cor:bar-cohomology-koszul-dual." It seems like I need to search for exact lines, so I’ll use a command like `sed` to help with that. Let's dive into that information and see what I can find!
exec
/bin/zsh -lc "sed -n '1760,1845p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '850,930p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '535,665p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(the Virasoro generators modulo vacuum), which is
free of finite rank in each conformal weight.

\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
$\operatorname{gr}_F \mathrm{Vir}_c
\cong \operatorname{Sym}(V)$
is a polynomial algebra (the OPE reduces to a commutative
product on the associated graded: the non-linear terms
$T_{(0)}T = \partial T$, $T_{(1)}T = 2T$ are lower-order in the
PBW filtration, and the quartic pole $T_{(3)}T = c/2$ is a
scalar that contributes to the curvature, not the
associated graded bracket).
By Priddy's theorem, $\operatorname{Sym}(V)$ is Koszul.

\emph{Hypothesis~\ref{item:pbw-bounded}.}
Same argument as the Kac--Moody case: the number of
partitions of weight~$h$ into at most $n$ parts (each $\geq 2$)
is finite.

By Theorem~\ref{thm:pbw-koszulness-criterion},
 succeeded in 52ms:
(Lemma~\ref{lem:verdier-involution-moduli}).
\emph{Second}, Lemma~\ref{lem:involution-splitting}(a) gives
the cochain-level splitting: the projectors
$p^\pm = \tfrac{1}{2}(\mathrm{id} \pm \sigma)$ are cochain maps
whose images provide a quasi-isomorphic direct sum decomposition
$\mathbf{C}_g \simeq \operatorname{im}(p^+) \oplus \operatorname{im}(p^-)$.
\emph{Third}, model independence
(Proposition~\ref{prop:model-independence}) ensures the
decomposition depends only on the Koszul pair $(\cA, \cA^!)$,
not on auxiliary choices.
\end{remark}

\begin{remark}[Geometric substrate (Volume~II)]
\label{rem:theorem-c-lagrangian}
\index{Lagrangian self-intersection!Theorem C}
Volume~II interprets the complementary decomposition as two
Lagrangians $\mathcal{L}$ and $\mathcal{L}^!$ inside a
$(-2)$-shifted symplectic stack $\mathcal{M}$, whose derived
intersection $\mathcal{L} \times_{\mathcal{M}} \mathcal{L}^!$
carries the $(-1)$-shifted symplectic structure that governs the
 succeeded in 52ms:
 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
Let $X$ be a smooth projective curve over $\mathbb{C}$.
A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
the following data and satisfying the following axioms.

\smallskip\noindent\textbf{Data.}
\begin{enumerate}[label=\textup{(D\arabic*)}]
\item\label{D:bar}
A reduced bar construction
$\bar{B}_X(\cA) \in \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$
(Definition~\ref{def:bar-differential-complete},
Theorem~\ref{thm:bar-nilpotency-complete}).

\item\label{D:dual}
A candidate Koszul dual chiral algebra $\cA^!$ on~$X$ with
universal twisting morphism
$\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
$\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
\emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
exec
/bin/zsh -lc 'rg -n "lem:perfectness-criterion" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
73: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
89:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
113:base change (Lemma~\ref{lem:perfectness-criterion}).
277:\label{lem:perfectness-criterion}
362:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
424:(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
exec
/bin/zsh -lc "sed -n '240,340p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
\end{lemma}

\begin{proof}
The projectors $p^\pm := \tfrac{1}{2}(\mathrm{id} \pm \sigma)$
are cochain maps with $p^+ + p^- = \mathrm{id}$,
$(p^\pm)^2 = p^\pm$, and $p^+ \circ p^- = 0$.
Part~(a): the inclusion $\operatorname{im}(p^+) \oplus \operatorname{im}(p^-)
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
exec
/bin/zsh -lc "sed -n '180,220p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '570,610p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,715p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

#### `chapters/theory/higher_genus_complementarity.tex` (79)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:involution-splitting` | `lemma` | 201 | Involution splitting in characteristic~\texorpdfstring{$0$}{0} |
| `lem:perfectness-criterion` | `lemma` | 256 | Perfectness criterion for the relative bar family |
| `thm:fiber-center-identification` | `theorem` | 330 | Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})} |
| `thm:quantum-complementarity-main` | `theorem` | 435 | Quantum complementarity as Lagrangian polarization |
| `lem:genus-filtration` | `lemma` | 620 | Genus filtration |
| `thm:ss-quantum` | `theorem` | 675 | Spectral sequence for quantum corrections |
| `lem:quantum-ss-convergence` | `lemma` | 760 | Convergence of the quantum spectral sequence |
| `lem:quantum-from-ss` | `lemma` | 823 | Quantum corrections as spectral sequence limit |
| `lem:fiber-cohomology-center` | `lemma` | 875 | Fiber cohomology and center |
| `thm:verdier-duality-config-complete` | `theorem` | 1023 | Verdier duality for compactified configuration spaces |
| `cor:duality-bar-complexes-complete` | `corollary` | 1096 | Duality for bar complexes |
 succeeded in 51ms:

\subsection{Statement of the theorem}

\begin{definition}[Deformation-obstruction complexes: H-level]
\label{def:complementarity-complexes}
\index{deformation-obstruction complexes|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$.
The \emph{ambient complex} at genus~$g$ is
\[
\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
\]
where $\mathcal{Z}(\cA)$ is the center local system.
The Verdier involution $\sigma$ acts on $\mathbf{C}_g(\cA)$ as a
cochain-level endomorphism with $\sigma^2 = \mathrm{id}$
(Theorem~\ref{thm:verdier-bar-cobar}).
Define the \emph{deformation-obstruction complexes} as homotopy eigenspaces:
\begin{equation}\label{eq:complementarity-fiber}
\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}\colon
\mathbf{C}_g \to \mathbf{C}_g), \qquad
\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \mathrm{id}\colon
 succeeded in 51ms:
 (Theorem~\ref{thm:mc2-bar-intrinsic}).
 The BRST resolution is complete.

 More precisely, there is a spectral sequence with $E_1$ page
 $E_1^{p,q} = H^q(\barB^p_X(\cA))$ converging to $H^{p+q}(\Omega_X \barB_X(\cA))$.
 On the Koszul locus, $E_1^{p,q} = 0$ for $p \neq 1$, so
 $E_2 = E_\infty$, and the comparison map
 $\varepsilon \colon \Omega_X \barB_X(\cA) \to \cA$
 induces an isomorphism on cohomology. This is the categorical
 exponential: $\exp \circ \log = \operatorname{id}$.

\item \emph{Theorem~C} (Deformation-obstruction complementarity,
 Theorem~\ref{thm:quantum-complementarity-main}).
 The \emph{center local system} $\mathcal{Z}_\cA$ is the
 local system on $\overline{\cM}_g$ whose fibre over a
 smooth curve $[\Sigma_g]$ is the center
 $Z(\cA|_{\Sigma_g})$ (the commutant of~$\cA$ acting on
 itself via the chiral bracket).
 The \emph{ambient complex}
 $\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g,
exec
/bin/zsh -lc 'rg -n "def:modular-koszul-chiral" -n -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/label_index.json:7158:  "def:modular-koszul-chiral": {
metadata/claims.jsonl:300:{"label": "thm:volume-one-concrete-modular-datum", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/editorial_constitution.tex", "line": 2470, "title": "Volume~I concrete modular datum", "refs_in_block": ["def:modular-koszul-homotopy", "thm:bar-cobar-isomorphism-main", "thm:quantum-complementarity-main", "thm:mc2-bar-intrinsic", "def:modular-koszul-chiral", "thm:bar-nilpotency-complete", "thm:genus-universality", "thm:quantum-diff-squares-zero", "def:full-modular-package", "thm:modular-characteristic", "thm:discriminant-spectral", "rem:periodicity-triple"]}
metadata/claims.jsonl:1368:{"label": "prop:discriminant-characteristic", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/examples/landscape_census.tex", "line": 2879, "title": "Discriminant as first characteristic invariant", "refs_in_block": ["def:modular-koszul-chiral", "thm:ds-bar-gf-discriminant"]}
metadata/claims.jsonl:2138:{"label": "thm:bar-cobar-inversion-qi", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 1604, "title": "Bar-cobar inversion is quasi-isomorphism", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "def:koszul-chiral-algebra", "sec:i-adic-completion", "MK:modular", "def:modular-koszul-chiral", "thm:pbw-allgenera-km", "thm:pbw-allgenera-principal-w", "rem:qi-vs-homology-iso", "thm:spectral-sequence-collapse", "rem:sl2-admissible", "rem:virasoro-module-koszul-minimal", "cor:bar-cobar-inverse"]}
metadata/claims.jsonl:2642:{"label": "lem:perfectness-criterion", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 256, "title": "Perfectness criterion for the relative bar family", "refs_in_block": ["def:modular-koszul-chiral"]}
metadata/claims.jsonl:2643:{"label": "thm:fiber-center-identification", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 330, "title": "Fiber--center identification \\textup{(Theorem~\\texorpdfstring{$\\mathrm{C}_0$}{C0})}", "labels_in_block": ["thm:fiber-center-identification", "eq:fiber-center"], "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral", "lem:perfectness-criterion"]}
metadata/claims.jsonl:2702:{"label": "thm:higher-genus-inversion", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 4082, "title": "Higher genus inversion", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "thm:modular-characteristic", "thm:multi-weight-genus-expansion", "def:modular-koszul-chiral", "def:shadow-postnikov-tower", "eq:universal-MC", "def:provisional-coderived", "prop:coderived-adequacy"]}
metadata/claims.jsonl:2805:{"label": "thm:loop-order-collapse", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_foundations.tex", "line": 6852, "title": "Loop order collapse", "labels_in_block": ["thm:loop-order-collapse", "eq:loop-collapse"], "refs_in_block": ["def:modular-koszul-chiral", "thm:loop-order-spectral-sequence"]}
metadata/claims.jsonl:2816:{"label": "prop:standard-examples-modular-koszul", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 601, "title": "Free-field examples are modular pre-Koszul", "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral", "thm:higher-genus-inversion", "thm:quantum-complementarity-main", "conv:heisenberg-kappa-notation"]}
metadata/claims.jsonl:2818:{"label": "thm:pbw-allgenera-principal-w", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 685, "title": "PBW concentration at all genera for principal finite-type \\texorpdfstring{$\\mathcal{W}$}{W}-algebras", "refs_in_block": ["conv:regime-tags", "thm:pbw-universal-semisimple", "def:modular-koszul-chiral"]}
metadata/claims.jsonl:2819:{"label": "thm:pbw-genus1-km", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 821, "title": "PBW degeneration at genus~\\texorpdfstring{$1$}{1} for Kac--Moody", "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral"]}
metadata/claims.jsonl:2821:{"label": "thm:pbw-allgenera-km", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 1111, "title": "PBW degeneration at all genera for Kac--Moody", "refs_in_block": ["conv:regime-tags", "thm:pbw-universal-semisimple", "def:modular-koszul-chiral"]}
metadata/claims.jsonl:2822:{"label": "cor:unconditional-allgenera-km", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 1308, "title": "Unconditional modular Koszulity for Kac--Moody", "refs_in_block": ["def:modular-koszul-chiral", "thm:higher-genus-inversion", "thm:quantum-complementarity-main", "prop:conditional-modular-koszul"]}
metadata/claims.jsonl:2823:{"label": "thm:pbw-allgenera-virasoro", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 1360, "title": "PBW degeneration at all genera for Virasoro", "refs_in_block": ["conv:regime-tags", "thm:pbw-universal-semisimple", "def:modular-koszul-chiral"]}
metadata/claims.jsonl:2824:{"label": "cor:unconditional-allgenera-virasoro", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 1460, "title": "Unconditional modular Koszulity for Virasoro", "refs_in_block": ["def:modular-koszul-chiral", "thm:higher-genus-inversion", "thm:quantum-complementarity-main", "prop:conditional-modular-koszul"]}
metadata/claims.jsonl:2825:{"label": "cor:unconditional-allgenera-principal-w", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 1510, "title": "Unconditional modular Koszulity for principal finite-type \\texorpdfstring{$\\mathcal{W}$}{W}-algebras", "refs_in_block": ["def:modular-koszul-chiral", "thm:higher-genus-inversion", "thm:quantum-complementarity-main", "prop:conditional-modular-koszul"]}
metadata/claims.jsonl:2828:{"label": "thm:pbw-propagation", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 1787, "title": "PBW propagation: MK1 implies MK3", "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral", "thm:pbw-universal-semisimple"]}
metadata/claims.jsonl:2833:{"label": "thm:modular-characteristic", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 2543, "title": "Modular characteristic", "labels_in_block": ["thm:modular-characteristic", "eq:modular-char-gf"], "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral", "def:scalar-modular-package", "thm:multi-generator-universality"]}
metadata/claims.jsonl:2835:{"label": "conj:kappa-holographic-central-charge", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 2748, "title": "$\\kappa$ as holographic central charge", "labels_in_block": ["conj:kappa-holographic-central-charge", "eq:kappa-holographic-identity"], "refs_in_block": ["def:modular-koszul-chiral", "eq:modular-char-gf", "thm:modular-characteristic", "cor:free-energy-ahat-genus"], "cites_in_block": ["CDG2023", "DNP25", "BH86"]}
metadata/claims.jsonl:2843:{"label": "prop:mc2-functoriality", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 3855, "title": "Functoriality of the bar-intrinsic MC element", "labels_in_block": ["prop:mc2-functoriality", "eq:mc2-functoriality"], "refs_in_block": ["def:modular-koszul-chiral"]}

exec
/bin/zsh -lc "sed -n '500,760p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\boldsymbol{\Omega}_X \mathbf{B}_X(\cA) \simeq \cA$
on the Koszul locus in
$\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))$.

\item\label{MK:complementarity-htpy}
\emph{(Lagrangian complementarity; Theorem~\textup{\ref{thm:quantum-complementarity-main}}.)}
The complementarity complex
$\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})$
decomposes as
$\mathbf{C}_g \simeq \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$,
where $\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}
\colon \mathbf{C}_g \to \mathbf{C}_g)$ and
$\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \mathrm{id})$
are homotopy eigenspaces of the Verdier involution~$\sigma$, each
Lagrangian for the shifted symplectic pairing
\textup{(}Proposition~\textup{\ref{prop:ptvv-lagrangian}},
Theorem~\textup{\ref{thm:ambient-complementarity-fmp})}.
\end{enumerate}
The cohomological shadows
$Q_g(\cA) := H^*(\mathbf{Q}_g(\cA))$ and
thinking
**Searching for theorem information**

I think I need to look for something called a theorem_registry, possibly related to a concordance entry. I might search for the theorem title in the concordance to find what I'm looking for. This seems like a straightforward task, but I want to ensure I'm referring to the right sources to get accurate information. Let's see what I can dig up!
exec
/bin/zsh -lc "rg -n 'fiber-center|C0|Theorem~\\\\ref\\{thm:fiber-center-identification\\}|thm:fiber-center-identification' chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_symplectic_polarization.tex:105:(Theorem~\ref{thm:fiber-center-identification}) gives
chapters/connections/thqg_symplectic_polarization.tex:1123:(Theorem~\ref{thm:fiber-center-identification}), the
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '640,720p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '520,620p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc 'rg -n "cor:bar-cohomology-koszul-dual" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/dependency_graph.dot:2393:  cor_bar_cohomology_koszul_dual [label="cor:bar-cohomology-koszul-dual\ncorollary [Pr]\nBar cohomology computes Koszul dual", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:398:| `cor:bar-cohomology-koszul-dual` | `corollary` | 859 | Bar cohomology computes Koszul dual |
metadata/label_index.json:3794:  "cor:bar-cohomology-koszul-dual": {
metadata/claims.jsonl:1026:{"label": "comp:sl2-ce-verification", "env_type": "computation", "status": "ProvedHere", "file": "chapters/examples/bar_complex_tables.tex", "line": 1915, "title": "CE cohomology of\n  \\texorpdfstring{$\\mathfrak{sl}_2 \\otimes t^{-1}\\mathbb{C}{[t^{-1}", "refs_in_block": ["cor:bar-cohomology-koszul-dual"]}
metadata/claims.jsonl:2296:{"label": "cor:bar-cohomology-koszul-dual", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 859, "title": "Bar cohomology computes Koszul dual", "refs_in_block": ["thm:pbw-koszulness-criterion", "thm:universal-kac-moody-koszul"]}
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
thinking
**Investigating theorem findings**

I’m not seeing any hits for the concordance and wondering if the theorem isn’t included. Maybe I should read the introduction to get more context, particularly around line 583 about the center local system. I need to examine the proof dependencies carefully and check the logical validity, especially around Step 2. It seems like I might have overstated Step 3, as the corollary only addresses dimension equality rather than identifying the center local system. I should look for the phrase “genus-0 center-bar identification” to dig deeper.
exec
/bin/zsh -lc "sed -n '840,920p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The PBW filtration on $\mathrm{Vir}_c$ is defined by the
number of Virasoro mode applications:
\[
F_p = \operatorname{span}\{L_{-n_1} \cdots L_{-n_r}
|0\rangle : r \leq p,\; n_i \geq 2\}.
\]

\emph{Hypothesis~\ref{item:pbw-flat}.}
Each $F_p/F_{p-1} \cong S^p(V)$ where
$V = \bigoplus_{n \geq 2} \bC \cdot L_{-n}$
(the Virasoro generators modulo vacuum), which is
free of finite rank in each conformal weight.

\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
$\operatorname{gr}_F \mathrm{Vir}_c
\cong \operatorname{Sym}(V)$
is a polynomial algebra (the OPE reduces to a commutative
product on the associated graded: the non-linear terms
$T_{(0)}T = \partial T$, $T_{(1)}T = 2T$ are lower-order in the
PBW filtration, and the quartic pole $T_{(3)}T = c/2$ is a
codex
I’m now checking whether the proof’s only substantive identification step is actually licensed by the cited result. The vulnerable point is Step 3, where bar cohomology is promoted to the center local system; I’m tracing whether any theorem really proves that, or only proves a weaker genus-0 Koszul-dual statement.
exec
/bin/zsh -lc "sed -n '1088,1135p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '860,930p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'center-bar identification|fiber cohomology and center|identified with the center|center local system|Koszul dual coalgebra and hence with the center|Z\\(\\\\cA\\)|mathcal\\{Z\\}_\\\\cA|derived center|center.*bar cohomology|bar cohomology.*center' chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/introduction.tex chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\emph{Perfect pairing}: By Poincaré duality for compact oriented manifolds:
\begin{equation}
H^k(\overline{C}_n(X)) \times H^{2n-k}(\overline{C}_n(X)) \xrightarrow{\wedge} 
H^{2n}(\overline{C}_n(X)) \xrightarrow{\int} \mathbb{C}
\end{equation}
is a perfect pairing. This is the geometric incarnation of Verdier duality.

\emph{Logarithmic forms}: When we include logarithmic forms $\Omega^*_{\log}(
\overline{C}_n(X))$ (forms with logarithmic poles along $\partial \overline{C}_n(X)$), 
the duality becomes:
\begin{equation}
\Omega^k_{\log}(\overline{C}_n(X)) \times \Omega^{2n-k}_{\log}(\overline{C}_n(X)) 
\to \mathbb{C}
\end{equation}
given by:
\begin{equation}
\langle \eta, \xi \rangle = \text{Res}_{\partial \overline{C}_n(X)} (\eta \wedge \xi)
\end{equation}
where $\text{Res}$ denotes the Poincaré residue map.

 succeeded in 50ms:

The genus-$g$ quantum corrections are precisely those cohomology classes that arise 
from genus-$g$ contributions but not from lower genus. Thus:
\begin{equation}
Q_g(\mathcal{A}) := \text{gr}^g H^*(\bar{B}(\mathcal{A})) = E_\infty^{*,*,g}
\end{equation}
We use the same notation $Q_g(\mathcal{A})$ for this graded piece,
anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
which identifies it with the $+1$-eigenspace of the Verdier involution
(Definition~\ref{def:complementarity-complexes}).
The two characterizations coincide: the filtration graded
piece captures the part of bar cohomology coming from genus~$g$,
while the eigenspace captures the $\mathcal{A}$-sector under
Verdier involution.
The identification is proved in
Lemma~\ref{lem:eigenspace-decomposition-complete}: the Verdier
involution sorts contributions according to whether they arise
from $j_*$-extended bar cochains of~$\mathcal{A}$ (eigenvalue~$+1$) or
from $j_!$-extended bar cochains of~$\mathcal{A}^!$ (eigenvalue~$-1$),
and the genus filtration separates precisely these two sources
 succeeded in 51ms:
chapters/theory/introduction.tex:138:$Q_g(\cA) \oplus Q_g(\cA^!) \simeq H^*(\overline{\mathcal{M}}_g, Z(\cA))$:
chapters/theory/introduction.tex:399:(the chiral derived center
chapters/theory/introduction.tex:583: The \emph{center local system} $\mathcal{Z}_\cA$ is the
chapters/theory/introduction.tex:590: \mathcal{Z}_\cA)$
chapters/theory/introduction.tex:601: H^*(\overline{\mathcal{M}}_g, \mathcal{Z}_\cA).
chapters/theory/introduction.tex:606: The shifted-symplectic structure is a $(-(3g{-}3))$-shifted symplectic form on the derived moduli of genus-$g$ bar families, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The complementary Lagrangians~$Q_g(\cA)$ and~$Q_g(\cA^!)$ are the $\pm 1$ eigenspaces of the Verdier involution~$\sigma = \mathbb{D}_{\operatorname{Ran}}$ acting on~$\mathbf{C}_g(\cA)$. Their intersection is the center~$Z(\cA)$; the ambient complex is the direct sum.
chapters/theory/introduction.tex:749: = H^*(\overline{\cM}_g,\, Z(\cA))$.
chapters/theory/introduction.tex:1477:open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
chapters/theory/introduction.tex:1481:derived center, not on the bar complex. The closed sector of any
chapters/theory/introduction.tex:1559: $(\mathrm{ChirAss})^!$; the SC structure emerges on the derived center.
chapters/theory/introduction.tex:2253: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
chapters/theory/introduction.tex:2477: $\SCchtop$ on the derived center pair; curved at
chapters/theory/en_koszul_duality.tex:1246:$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
chapters/theory/en_koszul_duality.tex:1248:\index{Swiss-cheese operad!on derived center, NOT on bar}
chapters/theory/en_koszul_duality.tex:1265:The derived center is the algebra of bulk observables of
chapters/theory/en_koszul_duality.tex:1281:The passage from bar complex to derived center is
chapters/theory/en_koszul_duality.tex:1284:computational engine; the derived center is the
chapters/theory/en_koszul_duality.tex:5546:(where $\barB^{\Sigma}(\cA)$ exists), the \emph{derived center}
chapters/theory/en_koszul_duality.tex:5560:\index{Higher Deligne Conjecture!E3 structure on derived center@$\mathsf{E}_3$ structure on derived center}
chapters/theory/en_koszul_duality.tex:5597:\item \textup{($\mathsf{E}_3$ on the derived center.)}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '320,420p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   320	$H^q(\operatorname{gr}_F\bar{B}^{(g)}(\cA)\big|_\Sigma) = 0$
   321	for $q \neq 0$ at every point of the base.
   322	
   323	\emph{Step~2: Transfer to the filtered complex.}
   324	The bar-degree filtration spectral sequence
   325	$E_1^{p,q} =
   326	H^q(\operatorname{gr}_p\bar{B}^{(g)}(\cA)\big|_\Sigma)$
   327	has $E_1^{p,q} = 0$ for $q \neq 0$ by Step~1. All higher
   328	differentials $d_r$ ($r \geq 2$) therefore vanish (they map into
   329	or out of the zero row), and the spectral sequence collapses at
   330	$E_2$ with $E_\infty^{p,0} = E_2^{p,0}$. In particular, the
   331	full fiber complex $\bar{B}^{(g)}(\cA)\big|_\Sigma$ has
   332	cohomology concentrated in degree~$0$ for every~$\Sigma$.
   333	The uniform vanishing range $q \neq 0$ is independent
   334	of~$[\Sigma]$.
   335	
   336	\emph{Step~3: Cohomology and base change.}
   337	The family
   338	$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$
   339	is a proper morphism of finite type. By Steps~1--2, the fiber

thinking
**Exploring mathematical references**

I'm noticing something intriguing about the lemma on fiber-cohomology-center at line 875. However, there’s an oversight because theorem C0 at line 350 doesn’t mention this lemma. Could the lemma actually be intended as support for the theorem? I think I should delve into the full lemmas to see if it offers a more straightforward proof, especially since the earlier theorem might have some inconsistencies. It’s probably worth examining more closely.
exec
/bin/zsh -lc "sed -n '875,980p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Lemma~\ref{lem:eigenspace-decomposition-complete}: the Verdier
involution sorts contributions according to whether they arise
from $j_*$-extended bar cochains of~$\mathcal{A}$ (eigenvalue~$+1$) or
from $j_!$-extended bar cochains of~$\mathcal{A}^!$ (eigenvalue~$-1$),
and the genus filtration separates precisely these two sources
(Lemma~\ref{lem:eigenspace-decomposition-complete}).

\emph{Explicit description.} An element of $Q_g(\mathcal{A})$ is represented by a closed form $\omega \in \bar{B}^{(g)}(\mathcal{A})$ (i.e., $d\omega = 0$) that is not exact modulo lower genus contributions.

\emph{Example.} For the Heisenberg algebra at $g=1$:
\begin{equation}
Q_1(\mathcal{H}_\kappa) = \text{span}\{\kappa \cdot \lambda_1\} \cong \mathbb{C}
\end{equation}
Here $\kappa$ is the level parameter and $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class;
the obstruction class $\kappa \cdot \lambda_1$ is a genus-$1$ quantum correction
that does not appear at genus~$0$.
\end{proof}

\emph{Step 4: Identify fiber cohomology with center.}

exec
/bin/zsh -lc "sed -n '680,720p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
| `thm:bar-convergence-fc` | `theorem` | 178 | Convergence criterion in the filtered/curved regimes |

#### `chapters/theory/fourier_seed.tex` (14)

| Label | Env | Line | Title |
|---|---|---:|---|
| `prop:fourier-propagator-properties` | `proposition` | 58 | Three properties of the propagator |
| `prop:fourier-genus1-propagator` | `proposition` | 115 | Genus-\texorpdfstring{$1$}{1} propagator |
| `prop:fourier-com-lie-duality` | `proposition` | 224 | — |
| `comp:fourier-heisenberg-n2` | `computation` | 270 | \texorpdfstring{$n = 2$}{n = 2} |
| `comp:fourier-heisenberg-n3` | `computation` | 319 | \texorpdfstring{$n = 3$}{n = 3} |
| `thm:fourier-heisenberg-bar` | `theorem` | 348 | — |
| `comp:fourier-heisenberg-elliptic` | `computation` | 408 | Heisenberg on \texorpdfstring{$E_\tau$}{E-tau} |
| `prop:fourier-total-diff-nilpotent` | `proposition` | 435 | — |
| `prop:fourier-propagator-degeneration` | `proposition` | 492 | Degeneration of the propagator |
| `prop:fourier-poincare-degeneration` | `proposition` | 550 | Degeneration of the Poincar\'e line bundle |
| `thm:fourier-recovery` | `theorem` | 630 | Recovery of the Fourier transform |
| `comp:fourier-km-bar` | `computation` | 800 | Kac--Moody bar |
| `thm:fourier-km-bar` | `theorem` | 821 | — |
| `thm:fourier-specialization` | `theorem` | 863 | Specialization |
exec
/bin/zsh -lc "sed -n '980,1060p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Filter the fiber bar complex~\eqref{eq:fiber-bar-complex} by bar
degree:
\[
F_p := \bigoplus_{j \leq p}
\Gamma\bigl(\overline{C}_j(\Sigma_g),\,
\mathcal{A}^{\boxtimes j} \otimes \Omega^*_{\log}\bigr).
\]
This is an exhaustive, bounded-below ($F_{-1}=0$) filtration, so the
associated spectral sequence converges to
$H^*(\bar{B}^*_{\Sigma_g}(\mathcal{A}))$.

On the associated graded $\operatorname{gr}^p_F$, the curvature
corrections~$d_{\mathrm{curv}}$ vanish because they raise bar degree
(hence filtration level). The surviving differential~$d_0$ is the
genus-$0$ collision differential alone. By
Theorem~\ref{thm:geometric-equals-operadic-bar}, the complex
$(\operatorname{gr}^p_F, d_0)$ is identified with the operadic bar
complex of~$\operatorname{gr}\mathcal{A}$.

Since $\mathcal{A}$ is Koszul
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
/bin/zsh -lc "sed -n '60,140p' ../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
review of PTVV geometry.
\S\ref{V1-subsec:thqg-III-complementarity-potential} constructs the
complementarity potential and identifies it with the shadow jet
expansion.
\S\ref{V1-subsec:thqg-III-holographic-entanglement} gives the
holographic interpretation at genus~$1$ and the BTZ connection.
\S\ref{V1-subsec:thqg-III-standard-landscape} verifies all structures
across the standard landscape.

% ======================================================================
%
% 1. THE AMBIENT COMPLEX AND VERDIER INVOLUTION
%
% ======================================================================

\subsection{The ambient complex and Verdier involution}
% label removed: subsec:thqg-III-ambient-complex
\index{ambient complex|textbf}
\index{Verdier involution!on ambient complex}

exec
/bin/zsh -lc "sed -n '1160,1215p' ../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\textup{(}Theorem~\textup{\ref{thm:thqg-III-lagrangian-polarization})}
are compatible in the following sense:

The bar-complex spectral sequence
\textup{(}Theorem~\textup{\ref{V1-thm:ss-quantum})} induces a
filtered quasi-isomorphism from the BV complex to the Verdier
complex, under which the BV $(-1)$-shifted symplectic form
maps to a degenerate form on $\mathbf{C}_g$ whose
non-degenerate quotient is the $(-(3g-3))$-shifted Verdier
form. Concretely:
\begin{equation}% label removed: eq:thqg-III-compatibility-diagram
\begin{tikzcd}
\MC(L_g) \arrow[r, "{(-1)\text{-shifted}}"] \arrow[d] &
\text{BV antibracket} \arrow[d] \\
\mathbf{C}_g(\cA)
\arrow[r, "{-(3g{-}3)\text{-shifted}}"]
& \text{Verdier pairing}
\end{tikzcd}
\end{equation}
where the vertical maps are the Leray spectral sequence
exec
/bin/zsh -lc "sed -n '900,950p' ../chiral-bar-cobar-vol2/main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\phantomsection\label{V1-sec:thqg-open-closed-realization}%
\phantomsection\label{V1-sec:thqg-perturbative-finiteness}%
\phantomsection\label{V1-setup:thqg-I-brown-henneaux}%
\phantomsection\label{V1-subsec:collision-filtration-recovery}%
\phantomsection\label{V1-subsec:genus2-complementarity-verification}%
\phantomsection\label{V1-subsec:thqg-I-convergence-grav}%
\phantomsection\label{V1-subsec:thqg-I-heisenberg-prototype}%
\phantomsection\label{V1-subsec:thqg-I-hs-sewing-framework}%
\phantomsection\label{V1-subsec:thqg-I-shadow-free-energies}%
\phantomsection\label{V1-subsec:thqg-I-standard-landscape}%
\phantomsection\label{V1-subsec:thqg-III-ambient-complex}%
\phantomsection\label{V1-subsec:thqg-III-complementarity-potential}%
\phantomsection\label{V1-subsec:thqg-III-eigenspace-decomposition}%
\phantomsection\label{V1-subsec:thqg-III-holographic-entanglement}%
\phantomsection\label{V1-subsec:thqg-III-shifted-symplectic}%
\phantomsection\label{V1-subsec:thqg-III-standard-landscape}%
\phantomsection\label{V1-subsec:thqg-V-binary-collision}%
\phantomsection\label{V1-subsec:thqg-V-collision-filtration}%
\phantomsection\label{V1-subsec:thqg-V-line-operators-mc3}%
\phantomsection\label{V1-subsec:thqg-V-modular-yangian}%

exec
/bin/zsh -lc 'rg -n "fiber-center" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '5880,5935p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item Quadratic case: $O(n^2 + m^2)$ for orthogonality
\item General case: $O(n^k)$ for bar complex dimension
\item Configuration integrals: $O(k! \cdot n^k)$ worst case
\end{itemize}

% ================================================================
% SECTION 8.9: SUMMARY AND OUTLOOK
% ================================================================

\section{Summary}

The PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion})
reduces chiral Koszulness to a classical spectral sequence
degeneration, applicable uniformly to all freely strongly generated
vertex algebras (Proposition~\ref{prop:pbw-universality}). The
twelve characterizations of
Theorem~\ref{thm:koszul-equivalences-meta} read the same
genus-$0$ formality condition through distinct invariants: bar
concentration, Ext diagonal vanishing, factorization homology,
Kac--Shapovalov determinants, FM boundary acyclicity. Two



exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '250,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   250	via the standard cone identification.
   251	Part~(b) follows by applying $H^*$ to~(a).
   252	Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
   253	so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
   254	= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
   255	Maximality is immediate from the direct-sum decomposition.
   256	\end{proof}
   257	
   258	\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
   259	\index{bar complex!relative fiber|textbf}
   260	Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
   261	\[
   262	\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
   263	\overline{\mathcal{M}}_g
   264	\]
   265	be the family of genus-$g$ compactified configuration spaces
   266	carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
   267	Its stalk at $[\Sigma] \in \overline{\mathcal{M}}_g$ is the
   268	\emph{genus-$g$ fiber bar complex}
   269	$C^{(g)}_X(\cA)\!\mid_\Sigma$, i.e.\ the bar complex of~$\cA$
thinking
**Rethinking theorem assumptions**

I’m considering the theorem statement, which assumes that A carries a modular pre-Koszul datum with finite-dimensional fiber cohomology, leading to a perfect relative bar family. That seems like a solid foundation. However, Step 1 mentions filtering the full fiber bar complex by bar degree, but I haven’t yet proven that this corresponds to the PBW filtration from MK3. There’s definitely more to unpack and clarify here!
thinking
**Verifying theorem proofs**

I need to inspect the proof related to the perfectness criterion. It might already demonstrate that fiber cohomology is concentrated in degree 0. If that's true, theorem C0 duplicates a previous vanishing result from a lemma. I wonder if I should have cited that lemma earlier. Additionally, I’m concerned about whether theorem C0 is circular, as it involves a center local system. It's puzzling how the definitions may intertwine with the input data in a modular pre-Koszul framework.
thinking
**Inspecting theorem validity**

I'm realizing that the theorem doesn't prove existence, as it's part of the data itself. Since D4 serves as this data, the theorem can link R^0 pushforward to a predefined sheaf. That wouldn't be circular unless D4 is explicitly used in the proof. Step 3 employs a corollary for genus-0 center-bar identification, but I’m not sure if D4 is utilized here. I need to check if theorem C0 claims to be "unconditional on the Koszul locus" and whether it's family-specific.
thinking
**Examining family restrictions**

I'm looking to clarify whether the task works for all families or just specific ones. I need to check standard examples related to this proposition. The search seems to suggest that theorem C0 is considered unconditional for every chiral algebra carrying a modular pre-Koszul datum, but this may only be validated for certain families. It's important for me to identify if there are any hidden restrictions concerning families and to explore the standard examples related to modular Koszul.
exec
/bin/zsh -lc "sed -n '1170,1660p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'standard-examples-modular-koszul|axioms MK1--MK3 hold unconditionally|hold unconditionally at all genera|simple admissible affine|Virasoro algebra satisfies axiom MK3|Heisenberg|beta|principal finite-type W|family by family' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '685,780p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
\label{cor:unconditional-genus1-km}
\index{modular Koszul chiral algebra!unconditional genus-1}
For any simple~$\fg$ at generic level, the affine
Kac--Moody vertex algebra $\widehat{\fg}_k$ satisfies
axioms \textup{MK1--MK3} unconditionally at genus~$1$.
By Theorems~\textup{\ref{thm:higher-genus-inversion}}
and~\textup{\ref{thm:quantum-complementarity-main}},
the consequences \textup{MK4} \textup{(}inversion\textup{)}
and \textup{MK5} \textup{(}complementarity\textup{)} hold
at genus~$1$ without any conditional hypothesis.
\end{corollary}

\begin{proof}
MK1 (genus-$0$ Koszulity):
Theorem~\ref{thm:km-chiral-koszul}.
MK2 (Verdier):
Theorem~\ref{thm:verdier-bar-cobar}.
MK3 (modular Koszulity at $g = 1$):
 succeeded in 51ms:
Total output lines: 384

chapters/theory/higher_genus_complementarity.tex:91:family by family
chapters/theory/higher_genus_complementarity.tex:92:(Proposition~\ref{prop:standard-examples-modular-koszul}).
chapters/theory/higher_genus_complementarity.tex:151:\begin{remark}[Computational perspective: Heisenberg at genus~$1$]
chapters/theory/higher_genus_complementarity.tex:451:The Heisenberg complementarity
chapters/theory/higher_genus_complementarity.tex:567:For the Heisenberg at genus~$1$: $Q_1=H^0$, $Q_1^!=H^2$.
chapters/theory/higher_genus_complementarity.tex:884:\emph{Example.} For the Heisenberg algebra at $g=1$:
chapters/theory/higher_genus_complementarity.tex:968:\emph{Verification for Heisenberg.}
chapters/theory/higher_genus_complementarity.tex:1084:\langle \alpha, \beta \rangle = \int_{\overline{C}_n(X)} \alpha \wedge \beta
chapters/theory/higher_genus_complementarity.tex:1086:for $\alpha \in H^k(\overline{C}_n(X))$ and $\beta \in H^{2n-k}(\overline{C}_n(X))$.
chapters/theory/higher_genus_complementarity.tex:1406:\emph{Verification for Heisenberg.} For $\mathcal{H}_\kappa$ with center
chapters/theory/higher_genus_complementarity.tex:1575:\eqref{eq:verdier-ks-anticommute}: for $\beta$ arising from
chapters/theory/higher_genus_complementarity.tex:1578:\sigma(\beta)
chapters/theory/higher_genus_complementarity.tex:1581:= -\beta
chapters/theory/higher_genus_complementarity.tex:1707:For the Heisenberg algebra: $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$
chapters/theory/higher_genus_complementarity.tex:2149: Example: The level $\kappa$ in Heisenberg $\mathcal{H}_\kappa$ appears as central
chapters/theory/higher_genus_complementarity.tex:2178:The first two bullet points are proved for specific examples (Heisenberg at genus~1
chapters/theory/higher_genus_complementarity.tex:2288:For $bc$--$\beta\gamma$: opposite obstructions cancel in the
chapters/theory/higher_genus_complementarity.tex:2434:\begin{example}[Heisenberg algebra: complete genus-1 computation]
 succeeded in 51ms:

\begin{proposition}[Free-field examples are modular pre-Koszul; \ClaimStatusProvedHere]
\label{prop:standard-examples-modular-koszul}
\index{modular Koszul chiral algebra!examples}
\textup{[Regime: quadratic
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

The following chiral algebras satisfy the antecedent axioms
\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
Theorems~\textup{\ref{thm:higher-genus-inversion}}
and~\textup{\ref{thm:quantum-complementarity-main}} then supply
\textup{MK4--MK5}, so they are modular Koszul:
\begin{enumerate}[label=\textup{(\alph*)}]
\item the Heisenberg algebra $\mathcal{H}_\kappa$
 (Convention~\textup{\ref{conv:heisenberg-kappa-notation}}) at any
 nonzero level $\kappa \neq 0$\textup{;}
\item the free fermion algebra $\mathcal{F}$ and the $\beta\gamma$-$bc$
 ghost systems.
\end{enumerate}
\end{proposition}
exec
/bin/zsh -lc "rg -n 'thm:pbw-koszulness-criterion|PBW Koszulness criterion' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
102:(Theorem~\ref{thm:pbw-koszulness-criterion}).
179:quadratic-Koszul (Theorem~\ref{thm:pbw-koszulness-criterion}).
618:(Theorem~\ref{thm:pbw-koszulness-criterion}), acyclicity
653:(Theorem~\ref{thm:pbw-koszulness-criterion}) is trivial and the
697:\label{thm:pbw-koszulness-criterion}
789:Theorem~\ref{thm:pbw-koszulness-criterion}.
825:By Theorem~\ref{thm:pbw-koszulness-criterion},
869:By Theorem~\ref{thm:pbw-koszulness-criterion},
877:Theorem~\textup{\ref{thm:pbw-koszulness-criterion}},
1096:By the PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion}),
1203:Theorem~\ref{thm:pbw-koszulness-criterion}.
1331:The three hypotheses of Theorem~\ref{thm:pbw-koszulness-criterion}
1378:Theorem~\textup{\ref{thm:pbw-koszulness-criterion}}
1767:Theorem~\ref{thm:pbw-koszulness-criterion}, this is
1983: \textup{(}Theorem~\textup{\ref{thm:pbw-koszulness-criterion})}.
2039:Theorem~\ref{thm:pbw-koszulness-criterion} identifies this with
2135:by Theorem~\ref{thm:pbw-koszulness-criterion} is Koszulness.
2163:(Theorem~\ref{thm:pbw-koszulness-criterion}) gives acyclicity:
5734:One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
5768:\item Not all vertex algebras are \emph{quadratic} Koszul, but the PBW framework (Theorem~\ref{thm:pbw-koszulness-criterion}) recovers Koszulness for a much wider class
exec
/bin/zsh -lc "sed -n '697,840p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{thm:pbw-koszulness-criterion}
\index{Koszul property!PBW criterion|textbf}
\textup{[Regime: filtered-complete
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a chiral algebra with PBW filtration
$F_0 \subset F_1 \subset \cdots \subset \cA$
such that the associated graded
$\operatorname{gr}_F \cA$ is a commutative chiral algebra
(equivalently, a vertex Poisson algebra).
Suppose:
\begin{enumerate}
\item\label{item:pbw-flat} The filtration is \emph{flat}: each $F_p/F_{p-1}$ is a free
 $\cO_X$-module of finite rank in each conformal weight.
\item\label{item:pbw-classical-koszul} The associated graded $\operatorname{gr}_F \cA$
 is classically Koszul: the Koszul complex
 $\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA$
 is acyclic in positive degrees.
\item\label{item:pbw-bounded} For each bar degree $n$ and conformal weight $h$, the
 chain group $\barBgeom^n_h(\cA)$ is finite-dimensional.
codex
A concrete mismatch has appeared: the proof of C0 invokes genus-0 bar/Koszul results from a `filtered-complete` PBW lane, but the theorem itself is only tagged `curved-central` and does not state those PBW hypotheses. I’m checking whether that hidden regime assumption is patched elsewhere or whether the theorem is overstated as written.
exec
/bin/zsh -lc "rg -n 'thm:higher-genus-inversion|quantum-complementarity-main|fiber-center-identification|C0' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:fiber-center-identification|fiber-center identification|Fiber--center identification' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups 2>/dev/null" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '340,430p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
39: \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
49: \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)};
188: (Theorem~\ref{thm:quantum-complementarity-main}).
264: and~\ref{thm:higher-genus-inversion}).}
322: (Theorem~\ref{thm:quantum-complementarity-main}).}
4502: (Theorem~\ref{thm:quantum-complementarity-main}).
4708:$B_{\mathrm{mod}}$ & Inversion on Koszul locus; coderived & Proved on Koszul locus; & Thm~\ref{thm:higher-genus-inversion}, \\
4710:$C_{\mathrm{mod}}$ & Shifted symplectic complementarity & \textbf{Proved} & Thms~\ref{thm:quantum-complementarity-main}, \\
4869:\textup{(}Theorem~\ref{thm:higher-genus-inversion}\textup{)}.
4884:Given these antecedents, Theorem~\ref{thm:higher-genus-inversion}
4921:provides the adjunction; Theorem~\ref{thm:higher-genus-inversion}
4954:Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}) establishes
5443: \textup{(}Theorem~\textup{\ref{thm:higher-genus-inversion})}.
7709:(Theorem~\ref{thm:quantum-complementarity-main},
9780: and~\textup{\ref{thm:higher-genus-inversion}}).
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:936:\phantomsection\label{V1-thm:fiber-center-identification}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:101:(Theorem~\ref{V1-thm:fiber-center-identification}) gives
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1187:(Theorem~\ref{V1-thm:fiber-center-identification}), the
 succeeded in 50ms:
   340	cohomology sheaves $R^q\pi_{g*}\bar{B}^{(g)}(\cA)$ vanish for
   341	$q \neq 0$ uniformly over the base, and the surviving $R^0$ has
   342	finite-dimensional fibers by hypothesis~(ii). The standard
   343	cohomology and base change theorem
   344	(EGA~III, Th\'eor\`eme~7.7.5)
   345	then gives that $R\pi_{g*}\bar{B}^{(g)}(\cA)$ is a perfect
   346	complex (bounded, with coherent cohomology sheaves) on
   347	$\overline{\mathcal{M}}_g$.
   348	\end{proof}
   349	
   350	\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
   351	\label{thm:fiber-center-identification}
   352	\index{fiber--center identification|textbf}
   353	\textup{[}Regime: curved-central
   354	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   355	
   356	\smallskip\noindent
   357	Assume $\cA$ carries a modular pre-Koszul datum
   358	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
   359	with finite-dimensional fiber cohomology, so that the relative bar
exec
/bin/zsh -lc "nl -ba ../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex | sed -n '80,140p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    80	The starting point is the datum of a chiral Koszul pair
    81	$(\cA, \cA^!)$ on a smooth projective curve $X$ over $\mathbb{C}$.
    82	The five main theorems (A--D+H) of Volume~I supply the following
    83	chain of identifications.
    84	
    85	\begin{definition}[Holographic ambient complex]
    86	% label removed: def:thqg-III-holographic-ambient
    87	\index{holographic ambient complex|textbf}
    88	Let $(\cA, \cA^!)$ be a chiral Koszul pair and let $g \ge 0$.
    89	The \emph{holographic ambient complex} at genus~$g$ is the cochain
    90	complex
    91	\begin{equation}% label removed: eq:thqg-III-holographic-ambient
    92	\mathbf{C}_g(\cA)
    93	:= \RGamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
    94	\end{equation}
    95	where $\mathcal{Z}(\cA)$ is the center local system on the
    96	Deligne--Mumford--Knudsen compactification
    97	$\overline{\mathcal{M}}_g$. When $g \ge 2$ and the relative bar
    98	family is perfect
    99	(Lemma~\ref{V1-lem:perfectness-criterion}), the fiber--center
exec
/bin/zsh -lc "nl -ba ../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex | sed -n '1160,1215p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1160	\textup{(}Theorem~\textup{\ref{thm:thqg-III-lagrangian-polarization})}
  1161	are compatible in the following sense:
  1162	
  1163	The bar-complex spectral sequence
  1164	\textup{(}Theorem~\textup{\ref{V1-thm:ss-quantum})} induces a
  1165	filtered quasi-isomorphism from the BV complex to the Verdier
  1166	complex, under which the BV $(-1)$-shifted symplectic form
  1167	maps to a degenerate form on $\mathbf{C}_g$ whose
  1168	non-degenerate quotient is the $(-(3g-3))$-shifted Verdier
  1169	form. Concretely:
  1170	\begin{equation}% label removed: eq:thqg-III-compatibility-diagram
  1171	\begin{tikzcd}
  1172	\MC(L_g) \arrow[r, "{(-1)\text{-shifted}}"] \arrow[d] &
  1173	\text{BV antibracket} \arrow[d] \\
  1174	\mathbf{C}_g(\cA)
  1175	\arrow[r, "{-(3g{-}3)\text{-shifted}}"]
  1176	& \text{Verdier pairing}
  1177	\end{tikzcd}
  1178	\end{equation}
  1179	where the vertical maps are the Leray spectral sequence

thinking
**Exploring cohomology concepts**

I'm thinking about the standard cohomology and the base change theorem, which indicates that Rπ_* is perfect. However, I notice a complexity in moving from fiber vanishing to the vanishing of sheaves. It seems like this transition isn’t straightforward unless there's proper base change and coherence involved. I’m curious about how these concepts connect and what implications they might hold for understanding the overall framework of cohomology. It's a fascinating topic!

thinking
**Organizing detailed cross-volume reference summary**

I'm preparing a structured bullet list summarizing statement lines, proof steps with line citations, the dependency map, and cross-volume mentions that include precise file and line references, making sure to highlight all relevant evidence without speculating beyond what's in the files.
exec
/bin/zsh -lc "rg -n '\\\\pi_g\\\\colon \\\\mathcal\\{C\\}_g\\(\\\\cA\\) \\\\to \\\\overline\\{\\\\mathcal\\{M\\}\\}_g|proper morphism of finite type|relative bar family|family of genus-\\"'$g'"\\"'$ compactified configuration spaces'"' chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:46: with finite-dimensional fiber cohomology, the relative bar family
chapters/theory/higher_genus_complementarity.tex:71: When the relative bar family
chapters/theory/higher_genus_complementarity.tex:265:be the family of genus-$g$ compactified configuration spaces
chapters/theory/higher_genus_complementarity.tex:275:\begin{lemma}[Perfectness criterion for the relative bar family;
chapters/theory/higher_genus_complementarity.tex:338:$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$
chapters/theory/higher_genus_complementarity.tex:339:is a proper morphism of finite type. By Steps~1--2, the fiber
chapters/theory/higher_genus_complementarity.tex:420:$\pi_g\colon \mathcal{C}_g(\cA) \to \overline{\mathcal{M}}_g$.
codex
- Statement lines: `chapters/theory/higher_genus_complementarity.tex:350`–`372` states that any modular pre-Koszul chiral algebra on a smooth projective curve whose fiber bar family is perfect (via Lemma \ref{lem:perfectness-criterion}) has vanishing higher direct images of the genus‑$g$ bar and identifies the surviving $R^0\pi_{g*}\bar{B}^{(g)}(\cA)$ with the center local system $\mathcal{Z}_\cA` on $\overline{\mathcal{M}}_g$.

- Proof steps with cited dependencies:
  - Step 1: filter the genus‑$g$ fiber complex by bar degree so that the associated graded sees only $\dzero$ (lines 378‑384).
  - Step 2: MK1 (genus‑0 Koszulity from Definition~\ref{def:modular-koszul-chiral}, `chapters/theory/higher_genus_modular_koszul.tex:597`) forces the graded complex to be the Koszul/Ext model with cohomology concentrated in degree 0 (`chapters/theory/higher_genus_complementarity.tex:385‑393`).
  - Step 3: the spectral sequence collapses, the surviving $H^0$ is $\bigoplus_p (\cA^!)_p$, and Corollary \ref{cor:bar-cohomology-koszul-dual} (`chapters/theory/chiral_koszul_pairs.tex:874`) identifies that graded coalgebra with the center local system on each fiber (`chapters/theory/higher_genus_complementarity.tex:395‑416`).
  - Step 4: base change (EGA III, Thm. 7.7.5 cited at `chapters/theory/higher_genus_complementarity.tex:343`) plus Lemma \ref{lem:perfectness-criterion} (`chapters/theory/higher_genus_complementarity.tex:275`) upgrades the vanishing to the perfect complex $R\pi_{g*}\bar{B}^{(g)}(\cA)$ and spreads the $R^0$ identification uniformly over $\overline{\mathcal{M}}_g$ (`chapters/theory/higher_genus_complementarity.tex:418‑424`).

- Dependency map:
  - `Definition def:modular-koszul-chiral` (`chapters/theory/higher_genus_modular_koszul.tex:534`) supplies the modular pre-Koszul datum hypothesis and MK1–MK3 axioms used throughout the proof.
  - `Axiom MK1 (genus-0 Koszulity)` (`chapters/theory/higher_genus_modular_koszul.tex:597`) ensures the associated graded fiber sees only a Koszul complex with cohomology in degree 0 (Step 2).
  - `Lemma lem:perfectness-criterion` (`chapters/theory/higher_genus_complementarity.tex:275`) guarantees $R\pi_{g*}\barB^{(g)}(\cA)$ is perfect when the PBW filtrations obey MK1/MK3 and fibers are finite dimensional, letting base change run in Step 4.
  - `Corollary cor:bar-cohomology-koszul-dual` (`chapters/theory/chiral_koszul_pairs.tex:874`) identifies the collapsed bar cohomology with the Koszul dual coalgebra/center in Step 3.
  - Standard cohomology-and-base-change (EGA III, Thm. 7.7.5) is invoked at `chapters/theory/higher_genus_complementarity.tex:343` to conclude from fiberwise concentration to perfectness and sheafy constancy.

- Cross-volume mention list:
  - `../chiral-bar-cobar-vol2/main.tex:936` defines `\label{V1-thm:fiber-center-identification}` so the volume‑II build pulls in Volume I references under the `V1-` prefix; watch for synchronized status tags.
  - `../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:99` uses the fiber‑center identification to replace the center local system by the $R^0\pi_{g*}$ bar family whenever the relative family is perfect (`Lemma~\ref{V1-lem:perfectness-criterion}`) in the holographic ambient complex.
  - `../chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1186` cites the identification again to concentrate the bar spectral sequence at $E_\infty$, so the BV pairing descends to the Verdier pairing in the shifted symplectic compatibility proof; any drift in hypothesis or status would ripple through these cross-volume uses.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '255,345p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   255	Maximality is immediate from the direct-sum decomposition.
   256	\end{proof}
   257	
   258	\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
   259	\index{bar complex!relative fiber|textbf}
   260	Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
   261	\[
   262	\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
   263	\overline{\mathcal{M}}_g
   264	\]
   265	be the family of genus-$g$ compactified configuration spaces
   266	carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
   267	Its stalk at $[\Sigma] \in \overline{\mathcal{M}}_g$ is the
   268	\emph{genus-$g$ fiber bar complex}
   269	$C^{(g)}_X(\cA)\!\mid_\Sigma$, i.e.\ the bar complex of~$\cA$
   270	on the fixed curve~$\Sigma$ with the fiberwise curved
   271	differential~$\dfib$
   272	\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
   273	\end{definition}
   274	
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '870,910p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '697,740p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '575,625p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   870	$\mathrm{Vir}_c$ is chiral Koszul.
   871	\end{proof}
   872	
   873	\begin{corollary}[Bar cohomology computes Koszul dual; \ClaimStatusProvedHere]
   874	\label{cor:bar-cohomology-koszul-dual}
   875	\index{bar complex!Koszul dual computation}
   876	For a chiral Koszul algebra $\cA$ satisfying the hypotheses of
   877	Theorem~\textup{\ref{thm:pbw-koszulness-criterion}},
   878	the PBW spectral sequence on $\barBgeom(\cA)$ collapses
   879	at $E_2$, and the bar cohomology dimensions equal the
   880	dimensions of the Koszul dual:
   881	\[
   882	\dim H^n(\barBgeom(\cA)) = \dim (\cA^!)_n
   883	\qquad\textup{(identifying $(\cA^!)_n = H^n(\barBgeom(\cA))^\vee$)}.
   884	\]
   885	In particular:
   886	\begin{enumerate}
   887	\item For $\widehat{\fg}_k$ at generic level:
   888	 $\dim H^n(\barBgeom(\widehat{\fg}_k)) = \dim (\widehat{\fg}_k^!)_n$
   889	 \textup{(}Theorem~\textup{\ref{thm:universal-kac-moody-koszul})}.
 succeeded in 51ms:
   697	\label{thm:pbw-koszulness-criterion}
   698	\index{Koszul property!PBW criterion|textbf}
   699	\textup{[Regime: filtered-complete
   700	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   701	
   702	Let $\cA$ be a chiral algebra with PBW filtration
   703	$F_0 \subset F_1 \subset \cdots \subset \cA$
   704	such that the associated graded
   705	$\operatorname{gr}_F \cA$ is a commutative chiral algebra
   706	(equivalently, a vertex Poisson algebra).
   707	Suppose:
   708	\begin{enumerate}
   709	\item\label{item:pbw-flat} The filtration is \emph{flat}: each $F_p/F_{p-1}$ is a free
   710	 $\cO_X$-module of finite rank in each conformal weight.
   711	\item\label{item:pbw-classical-koszul} The associated graded $\operatorname{gr}_F \cA$
   712	 is classically Koszul: the Koszul complex
   713	 $\barBgeom(\operatorname{gr}_F \cA) \otimes_\tau \operatorname{gr}_F \cA$
   714	 is acyclic in positive degrees.
   715	\item\label{item:pbw-bounded} For each bar degree $n$ and conformal weight $h$, the
   716	 chain group $\barBgeom^n_h(\cA)$ is finite-dimensional.
 succeeded in 51ms:
   575	A center local system $\mathcal{Z}_{\cA}$ on
   576	$\overline{\mathcal{M}}_{g,\bullet}$ whose fiber at a smooth
   577	curve~$\Sigma$ is the center $Z(\cA|_\Sigma)$.
   578	
   579	\item\label{D:discriminant-dg}
   580	A spectral discriminant
   581	$\Delta_{\cA}(x) = \det(1 - x\, T_{\mathrm{rec}})$
   582	(Theorem~\ref{thm:discriminant-spectral}).
   583	
   584	\item\label{D:periodicity-dg}
   585	A periodicity profile
   586	$\Pi(\cA) = (M_{\cA},\, Q_{\cA},\, G_{\cA})$
   587	(Remark~\ref{rem:periodicity-triple}).
   588	\end{enumerate}
   589	
   590	\smallskip\noindent\textbf{Axioms.}
   591	The axioms below are \emph{antecedent hypotheses}:
   592	they can be verified without invoking bar-cobar inversion
   593	or complementarity. Theorems~\ref{thm:higher-genus-inversion}
   594	and~\ref{thm:quantum-complementarity-main} then \emph{prove}


thinking
**Evaluating chiral Koszul pairs**

I need to clarify what a chiral Koszul pair is, although it might not be strictly necessary. I'm pondering if there's an issue with Step 2 regarding fiberwise curvature, since curvature typically relates to the square of the differential. The associated graded of a filtered complex can compute from the differential, but the conditions around d_fib's associated graded square aren’t clear unless it decomposes specifically. I should check if d_fib preserves filtration since it seems important, especially for the spectral sequence.
thinking
**Analyzing bar complex structure**

I’m considering the bar complex structure and its implications. The lemma's perfectness criterion mentions the bar-degree filtration spectral sequence, which uses a flat PBW filtration over the base. However, the proof lacks discussion on exhaustiveness or compatibility, leaving Step 1 feeling underexplained. It’s unclear if the theorem depends on genus 0 center-bar identification, since the actual corollary only relates bar cohomology to the Koszul dual. I might need to look for a deeper theorem linking them, perhaps through the MK2 Verdier or derived center.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1470,1490p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'derived center.*bar complex|bar complex.*derived center|SC.*derived center|center local system.*fiber at a smooth curve' chapters/theory/introduction.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'A\\"'^!.*center|center.*A'"\\"'^!|Koszul dual coalgebra.*center|center.*Koszul dual|Z'"\\(\\\\cA\\).*A\\"'^!|mathcal'"\\{Z\\}_\\\\cA.*A\\"'^!|center-bar identification'"' chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/introduction.tex chapters/theory/poincare_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1470	categories are obtained from braided ones by the
  1471	$\Sigma_n$-coinvariant procedure on the braid groupoid; this is
  1472	exactly the categorical analogue of the averaging
  1473	map~\eqref{eq:intro-averaging}.
  1474	
  1475	\textsc{Operadic primacy of Swiss-cheese.} The Swiss-cheese
  1476	operad $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$ governs the
  1477	open/closed derived center pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$
  1478	(Theorem~\ref{thm:thqg-swiss-cheese}); the bar complex itself
  1479	is a single-coloured $\Eone$-chiral coassociative coalgebra
  1480	over $(\mathrm{ChirAss})^!$. The SC structure emerges on the
  1481	derived center, not on the bar complex. The closed sector of any
  1482	Swiss-cheese algebra is recovered from the open sector by passing
  1483	to $\Sigma_n$-coinvariants along the open-to-closed boundary
  1484	operator. The closed sector is intrinsically a quotient of the
  1485	open sector, never an enrichment of it.
  1486	
  1487	\paragraph{Historical context.}
  1488	The manuscript developed from the Beilinson--Drinfeld theory of
  1489	factorization algebras on the Ran space~\cite{BD04}, which is
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:1246:$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
chapters/theory/en_koszul_duality.tex:1281:The passage from bar complex to derived center is
chapters/theory/introduction.tex:1481:derived center, not on the bar complex. The closed sector of any
chapters/theory/introduction.tex:1559: $(\mathrm{ChirAss})^!$; the SC structure emerges on the derived center.
chapters/theory/introduction.tex:2253: $\Eone$-chiral bar on $\FM_k(\C)\times\operatorname{Conf}_k(\R)$; $\SCchtop$ on derived center; curved at $g\ge 1$; recognition; homotopy-Koszulity of $\mathrm{SC}^{\mathrm{ch,top}}$; bulk/boundary/line triangle \\
chapters/theory/introduction.tex:2477: $\SCchtop$ on the derived center pair; curved at
 succeeded in 51ms:
chapters/theory/introduction.tex:606: The shifted-symplectic structure is a $(-(3g{-}3))$-shifted symplectic form on the derived moduli of genus-$g$ bar families, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The complementary Lagrangians~$Q_g(\cA)$ and~$Q_g(\cA^!)$ are the $\pm 1$ eigenspaces of the Verdier involution~$\sigma = \mathbb{D}_{\operatorname{Ran}}$ acting on~$\mathbf{C}_g(\cA)$. Their intersection is the center~$Z(\cA)$; the ambient complex is the direct sum.
chapters/theory/higher_genus_complementarity.tex:415:by the genus-$0$ center-bar identification
chapters/theory/higher_genus_complementarity.tex:1718:$\cA$ with trivial center, $\dim Q_2(\cA) + \dim Q_2(\cA^!) = 8$.
chapters/theory/higher_genus_modular_koszul.tex:29681:$P_\cA(t) = \dim Z(\cA) + \dim\operatorname{ChirHoch}^1(\cA)\cdot t + \dim Z(\cA^!)\cdot t^2$
codex
The core logical break is sharper now: Step 3 does not just use a theorem outside its stated regime, it also appears to conflate three different objects the repo elsewhere treats as distinct: fiber bar cohomology, the Koszul dual coalgebra, and the center local system. I’m pulling the local definitions/examples that make that conflation explicit before I finalize the finding.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '438,446p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '583,591p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2643,2646p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   438	$\cH_k^! \neq \cH_{-k}$
   439	(\S\ref{sec:frame-koszul-dual}).
   440	
   441	\smallskip
   442	\noindent\textbf{Theorem~B (bar-cobar inversion).}\enspace
   443	The bar cohomology is $H^{-1}(\barB(\cH_k)) = \C\cdot s^{-1}J$
   444	(concentrated in bar degree~$1$), so the Koszul dual coalgebra is
   445	$\cH_k^{\mathrm{i}} = \C\cdot s^{-1}J$. The Koszul dual algebra
   446	is $\cH_k^! = (\cH_k^{\mathrm{i}})^\vee$: the symmetric chiral
 succeeded in 51ms:
   583	 The \emph{center local system} $\mathcal{Z}_\cA$ is the
   584	 local system on $\overline{\cM}_g$ whose fibre over a
   585	 smooth curve $[\Sigma_g]$ is the center
   586	 $Z(\cA|_{\Sigma_g})$ (the commutant of~$\cA$ acting on
   587	 itself via the chiral bracket).
   588	 The \emph{ambient complex}
   589	 $\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g,
   590	 \mathcal{Z}_\cA)$
   591	 (derived global sections of this local system)
 succeeded in 51ms:
  2643	
  2644	\smallskip\noindent\textbf{Four objects.}
  2645	$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !`}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.
  2646	

thinking
**Evaluating theorem and proof**

I need to find out if the theorem statement itself is false or if just the proof is invalid, since the user is asking to falsify the proof. If the proof is flawed but the theorem might still be true, it’s crucial to determine whether the theorem is supported by this invalid proof. I should focus on identifying defects in the proof with ordered severity. 

There's something concerning about Step 2 regarding the curvature term. It mentions dfib^2 vanishing in the associated graded, but I think I need to verify how dfib is treated in this context.
exec
/bin/zsh -lc "rg -n 'conv:higher-genus-differentials|d_\\{\\mathrm\\{fib\\}\\}|dfib|curvature terms raise bar degree|genus-0 collision differential' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:conv:higher-genus-differentials|d_\{\mathrm\{fib\}\}|dfib|curvature terms raise bar degree|genus-0 collision differential)
                                           ^^
error: unrecognized escape sequence

thinking
**Simplifying search processes**

I want to make searches more straightforward and efficient. This could mean refining the search terms I'm using or streamlining the way I'm gathering information. It's important to focus on clarity and relevance so that the user gets exactly what they're looking for without any unnecessary confusion. I’ll keep my approach flexible, adapting as I go to ensure optimal search results. Let’s work on simplifying this together!
exec
/bin/zsh -lc "sed -n '400,480p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'conv:higher-genus-differentials|dfib|fiberwise curved differential|genus-0 collision differential' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Rather, $\nabla^{\mathrm{GM}}$ is an independent geometric datum
 (the connection on the base $\overline{\cM}_g$), and the
 uncurving identity~\eqref{eq:chain-uncurving} expresses the
 interplay between fiber curvature and base flatness.
 The resulting flat complex $(\barB^{(g)}(\cA), \Dg{g})$ lives in
 the derived category; the curved complex
 $(\barB^{(g)}(\cA), \dfib)$ lives in the coderived category
 $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
 These categories are \emph{inequivalent} in general: the
 coderived category has strictly more objects (the coacyclic
 complexes are invisible to the derived category).
\end{enumerate}
\end{proposition}

\begin{proof}
(i)~The Gauss--Manin connection on the cohomology local system
$R^q\pi_*\C$ is constructed from the Leray filtration of
$\Omega^*_{\overline{\cC}_g/\overline{\cM}_g}$.
The identification of the connection 1-forms with the
holomorphic differentials $\omega_k$ follows from the
 succeeded in 50ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:47:quadratic (strict $d^2=0$), curved-central ($\dfib^2 = \kappa\cdot\omega_g$
chapters/theory/bar_cobar_adjunction_inversion.tex:675:($\dfib^{\,2} = \mcurv{g} \neq 0$; Convention~\ref{conv:higher-genus-differentials}). In the curved case, ordinary
chapters/theory/bar_cobar_adjunction_inversion.tex:3349:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \mathrm{id}$ rather than $\dfib^{\,2} = 0$
chapters/theory/bar_cobar_adjunction_inversion.tex:3350:(see Convention~\ref{conv:higher-genus-differentials} for the notation).
chapters/theory/bar_cobar_adjunction_inversion.tex:3353:$\dfib^{\,2} \neq 0$'' and ``acyclic because of genuine exactness.''
chapters/theory/bar_cobar_adjunction_inversion.tex:3703:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ at genus~$g \geq 1$ \\[2pt]
chapters/theory/bar_cobar_adjunction_inversion.tex:3879:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ \\[2pt]
chapters/theory/bar_cobar_adjunction_inversion.tex:3905:$\dfib^{\,2} = \kappa \cdot \omega_g$ is the infinitesimal generator
chapters/theory/bar_cobar_adjunction_inversion.tex:3911:The three differentials $\dzero$, $\dfib$, $\Dg{g}$
chapters/theory/bar_cobar_adjunction_inversion.tex:3912:(Convention~\ref{conv:higher-genus-differentials}) are three levels of
chapters/theory/bar_cobar_adjunction_inversion.tex:3914:multi-valued lift ($\dfib$, curvature $= $ residue), and the
chapters/theory/bar_cobar_adjunction_inversion.tex:4213:($\dfib^{\,2} \neq 0$) and demands the full Maurer--Cartan package
chapters/theory/bar_cobar_adjunction_inversion.tex:4244:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
chapters/theory/higher_genus_complementarity.tex:271:differential~$\dfib$
chapters/theory/higher_genus_complementarity.tex:272:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/higher_genus_complementarity.tex:314:curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes
chapters/theory/higher_genus_complementarity.tex:387:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes (it lies
chapters/theory/higher_genus_complementarity.tex:2735:This differential satisfies $\Dg{g}^{\,2} = 0$ (Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/higher_genus_complementarity.tex:2736:\item Compute the fiberwise collision differential $\dfib$ and verify
chapters/theory/higher_genus_complementarity.tex:2737:that $\dfib^{\,2} = \kappa \cdot \omega_g \in Z(\mathcal{A}) \otimes H^2(\overline{\mathcal{M}}_g)$;
exec
/bin/zsh -lc "sed -n '500,560p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
H^1(\Sigma_g, \C)
\;\xrightarrow{\;\text{MC}\;}
Z^1(\operatorname{Def}_{\mathrm{cyc}}(\cA)_{\mathrm{model}})
\;\xrightarrow{\;\text{global}\;}
R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})
\;\xrightarrow{\;\mathrm{tr}\;}
R\Gamma(\overline{\mathcal{M}}_g, \mathbb{Q}).
\]
Fiber-period parameters live in $H^1(\Sigma_g,\C)$, not on moduli
($H^1(\mathcal{M}_g,\mathbb{Q})=0$ for $g\geq 2$ by Harer).
They become moduli classes via the Kodaira--Spencer map
(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
\end{remark}

\begin{proposition}[The genus-$g$ curvature package; \ClaimStatusProvedHere]
\label{prop:genus-g-curvature-package}
\index{curvature package!genus-g@genus-$g$|textbf}
Let $\cA$ be a cyclic chiral algebra on a smooth projective
curve~$X$ of genus~$g \geq 1$, and let
$\{\omega_1,\ldots,\omega_g\}$ be the normalized abelian
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '229,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
**Investigating differential equations**

I need to find out if another file discusses the "fiberwise differential dfib" and its curvature, especially regarding quantum corrections. It seems like there’s a strict differential Dg involved and I might need to use that in the theorem. I'm questioning if this creates a contradiction within the same chapter. I think I should search around chapter 3425 to see if there are any remarks acknowledging this difference. Let's delve deeper!
codex
A stronger defect has surfaced. By the repo’s own higher-genus convention, the fiberwise differential `\dfib` is curved (`\dfib^2=\kappa\omega_g`) and the resulting object lives in the coderived category, not as an honest complex. But C0 and its prerequisite lemma take ordinary cohomology, higher direct images, and base change of that curved fiber object. I’m pinning the exact internal contradiction now.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3420,3445p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '258,346p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '238,297p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3420	integrals of the Cauchy kernel to the symplectic
  3421	intersection pairing, and restricting to a Lagrangian
  3422	subspace forces all anticommutators to vanish.
  3423	
  3424	\emph{(Note: The two vanishings $\Dg{g}^{\,2} = 0$ and
  3425	$\dfib^{\,2} \neq 0$ are not in tension; they are the two
  3426	faces of the chiral Riemann--Hilbert correspondence
  3427	(Remark~\textup{\ref{rem:curvature-riemann-hilbert}}).
  3428	The holomorphic propagator defines a flat connection on
  3429	the universal cover of $\Sigma_g$. The Arakelov
  3430	propagator defines the single-valued but curved
  3431	projection to $\Sigma_g$ itself. The total corrected
  3432	differential $\Dg{g}$ lives in the flat gauge; the
  3433	fiberwise differential $\dfib$ lives in the curved gauge.
  3434	The passage $\dfib \leadsto \Dg{g}$ is the chiral
  3435	exponential map.)} \qedhere
  3436	\end{proof}
  3437	
  3438	\begin{remark}[Curved twisting morphisms at higher genus]
  3439	\label{rem:curved-twisting-higher-genus}
 succeeded in 52ms:
   258	\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
   259	\index{bar complex!relative fiber|textbf}
   260	Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
   261	\[
   262	\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
   263	\overline{\mathcal{M}}_g
   264	\]
   265	be the family of genus-$g$ compactified configuration spaces
   266	carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
   267	Its stalk at $[\Sigma] \in \overline{\mathcal{M}}_g$ is the
   268	\emph{genus-$g$ fiber bar complex}
   269	$C^{(g)}_X(\cA)\!\mid_\Sigma$, i.e.\ the bar complex of~$\cA$
   270	on the fixed curve~$\Sigma$ with the fiberwise curved
   271	differential~$\dfib$
   272	\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
   273	\end{definition}
   274	
   275	\begin{lemma}[Perfectness criterion for the relative bar family;
   276	\ClaimStatusProvedHere]
   277	\label{lem:perfectness-criterion}
 succeeded in 51ms:
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
   249	 acts as $\kappa(\cA)$ times the Arakelov $(1,1)$-form $\omega_g$
   250	 (a specific smooth chain on~$\Sigma_g$, not merely a cohomology class).
   251	 On the uniform-weight scalar lane, the cohomological curvature
   252	 element
   253	 $\mcurv{g} = \kappa(\cA)\cdot\lambda_g \in H^{2g}(\overline{\cM}_g)$ is the Chern--Weil image of this chain-level operator
   254	 under integration over the fibers of
   255	 $\pi\colon\overline{\cC}_g\to\overline{\cM}_g$
   256	 (Proposition~\ref{prop:chain-level-curvature-operator}).
   257	

thinking
**Assessing theorem implications**

There's a clear contradiction here; Theorem C0 uses a curved gauge but has derived pushforward, which is critical. I need to check if this theorem is referenced in Volume II under the V1 label. It may not be relevant to proof issues apart from propagation. I should read certain lines to assess drift and consider if the theorem is used as input for symplectic polarization. Since the theorem is flawed, its downstream consequences may be impacted.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex | sed -n '96,110p;1182,1192p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    96	Deligne--Mumford--Knudsen compactification
    97	$\overline{\mathcal{M}}_g$. When $g \ge 2$ and the relative bar
    98	family is perfect
    99	(Lemma~\ref{V1-lem:perfectness-criterion}), the fiber--center
   100	identification
   101	(Theorem~\ref{V1-thm:fiber-center-identification}) gives
   102	\begin{equation}% label removed: eq:thqg-III-bar-center
   103	\mathbf{C}_g(\cA)
   104	\simeq
   105	\RGamma(\overline{\mathcal{M}}_g,
   106	R^0\pi_{g*}\barB^{(g)}(\cA)).
   107	\end{equation}
   108	\end{definition}
   109	
   110	\begin{remark}[H/M/S layers]% label removed: rem:thqg-III-hms
  1182	
  1183	\begin{proof}
  1184	The BV pairing on $L_g = \barB^{(g)}(\cA)[1]$ descends to
  1185	a pairing on the $E_\infty$ page of the bar-degree spectral
  1186	sequence. By the fiber--center identification

thinking
**Considering theorem proof impact**

I’m thinking about the downstream impact here. It might not be strictly necessary to state it, but I could mention the high severity of downstream propagation. If the proof is invalid, I should refer to volume 2 and the invalid theorem at specific lines. This could be an important consequence to summarize. The user is focused on the findings from the theorem proof, so I’ll also consider including a cross-volume mention of propagation. I need to wait for the explorer results.
collab wait(call_P3vFs7uO8d8ZiihyyCBmjeAf)
  receivers: 019d8388-a411-7811-a31b-c12e30d7af4a
wait(call_P3vFs7uO8d8ZiihyyCBmjeAf) 1 agents complete:
  019d8388-a411-7811-a31b-c12e30d7af4a completed: "- Statement lines: `chapters/theory/higher_genus_complementarity.tex:350`–`372` states that any modular pre-Koszul chira…"



thinking
**Evaluating theorem implications**

I’m thinking about the explorer summary and whether I need to check the proof's circularity in Step 3. It claims to connect collapsed bar cohomology with the Koszul dual coalgebra, but that doesn't seem quite right. I must rely on our file readings for clarity. There’s an issue around Step 3's spectral sequence collapse too, particularly with curved differentials. While the theorem mentions local systems on moduli, it's tricky given the boundary structures. The definition might need more precision.
thinking
**Investigating boundary values**

I'm considering whether there could be boundary values that serve as counterexamples at kappa ≠ 0. Since dfib is curved, the theorem might not hold unless I use strict Dg or coderived frameworks. I should look for explicit counterexamples in our repository, particularly regarding the Heisenberg at a non-zero k. The theorem's commentary on Heisenberg at genus 1 hints at some fiber-center identification. The curved differential complicates the proof's validity, so I’ll need to assess if replacing dfib with Dg could still keep the theorem intact.
thinking
**Searching for relevant theorems**

I’m thinking about searching for terms like "flat-side comparison locus" or "cobar-resolution-scoped." The theorem statement didn't specify these, but it might still hold true at κ=0 or if we transition to Dg. The task mentions hidden hypotheses, and I wonder if the flat-side comparison locus could be one, particularly concerning κ=0 or a corrected differential. I should look for relevant theorems that might clarify this and see if they address my questions.
exec
/bin/zsh -lc "rg -n 'flat-side comparison locus|cobar-resolution-scoped|derived/coderived comparison|coderived' chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '294,297p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem~\\\\ref\\{thm:cobar-resolution-scoped\\}|flat-side|comparison locus' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:3361: coderived
chapters/theory/higher_genus_complementarity.tex:4132:faithfully in the provisional coderived category
chapters/theory/higher_genus_complementarity.tex:4134:\textup{(}Definition~\textup{\ref{def:provisional-coderived},}
chapters/theory/higher_genus_complementarity.tex:4135:Proposition~\textup{\ref{prop:coderived-adequacy}(a))},
chapters/theory/higher_genus_complementarity.tex:4266:The replacement is the coderived factorization co-contra comparison on
chapters/theory/higher_genus_complementarity.tex:4414:(iii)~the coderived category
chapters/theory/bar_cobar_adjunction_inversion.tex:33:coderived categories
chapters/theory/bar_cobar_adjunction_inversion.tex:662:The bar complex $\bar{B}^{\mathrm{ch}}(\cA)$ is a chiral coalgebra; when the curvature is nonzero, it is a \emph{curved} coalgebra requiring Positselski's coderived categories for its homological algebra.
chapters/theory/bar_cobar_adjunction_inversion.tex:686:\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
chapters/theory/bar_cobar_adjunction_inversion.tex:687:\label{rem:coderived-status}%
chapters/theory/bar_cobar_adjunction_inversion.tex:688:\index{coderived category!status}%
chapters/theory/bar_cobar_adjunction_inversion.tex:693:(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
chapters/theory/bar_cobar_adjunction_inversion.tex:701:($d^2 = [m_0^{(g)}, -]$ on $\barB^{(g)}$). The coderived category
chapters/theory/bar_cobar_adjunction_inversion.tex:708:these classes \emph{control} the coderived category at each genus requires
chapters/theory/bar_cobar_adjunction_inversion.tex:709:the curved bar-cobar adjunction to extend to a coderived Quillen equivalence.
chapters/theory/bar_cobar_adjunction_inversion.tex:717:\item Construct the coderived model structure on curved chiral
chapters/theory/bar_cobar_adjunction_inversion.tex:721:\item Identify the coderived shadow invariants with the proved
chapters/theory/bar_cobar_adjunction_inversion.tex:875:substitute is the coderived category (Definition~\ref{def:chiral-coderived}).
chapters/theory/bar_cobar_adjunction_inversion.tex:969:\label{subsec:chiral-coderived-contraderived}
chapters/theory/bar_cobar_adjunction_inversion.tex:972:\label{def:chiral-coderived}
 succeeded in 51ms:
   294	The derived/coderived comparison, established on the manuscript's
   295	flat-side comparison locus together with the coderived treatment of
   296	the curved model, ensures that the flat model carries the ordinary
   297	derived package while the curved model is its coderived counterpart.
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:295:flat-side comparison locus together with the coderived treatment of
chapters/theory/higher_genus_foundations.tex:457:(Theorem~\ref{thm:cobar-resolution-scoped}).
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2048,2075p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2048	\label{thm:cobar-resolution-scoped}
  2049	For any augmented chiral algebra $\mathcal{A}$, the bar construction
  2050	$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ and cobar construction
  2051	$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A}))$ exist as objects.
  2052	When the canonical twisting morphism is Koszul
  2053	\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})},
  2054	the cobar of the bar provides a free resolution:
  2055	\begin{multline*}
  2056	\cdots \to \Omega^2_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
  2057	\to \Omega^1_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))\\
  2058	\to \Omega^0_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
  2059	\xrightarrow{\epsilon} \cA \to 0
  2060	\end{multline*}
  2061	Off the Koszul locus, the bar-cobar object persists only in the
  2062	completed coderived category
  2063	\textup{(}Appendix~\textup{\ref{sec:coderived-models})}.
  2064	
  2065	The augmentation is given geometrically by:
  2066	\[\epsilon(K) = \lim_{\varepsilon \to 0} \int_{|z_i - z_j| > \varepsilon} K(z_1, \ldots, z_n) \prod_{i<j} |z_i - z_j|^{2h_{ij}}\]
  2067	\end{theorem}





thinking
**Evaluating theorem steps**

I'm analyzing a step that doesn't strictly follow from MK1. I need to consider the assumption that the associated graded of the genus-g complex is related to the classical Koszul complex or the genus zero bar complex of gr_F A. The proof claims this because the curvature is in a positive filtration degree, but that aspect covers only the differential, not the identification of configuration-space forms. However, there's a stronger point in Step 2 that states this association clearly.
thinking
**Assessing geometry and terminology**

I'm thinking about the classical bar over a point and how it's emphasized that configuration-space geometry over a curve has no equivalent over a point. It seems like calling the associated graded "classical Koszul/Ext complex" might be questionable. I need to check if the genus-0 collision differential is indeed the classical bar differential over a point, since the convention suggests otherwise. Also, it feels like Step 2 might contradict itself and could be blending different geometrical ideas. I'll dig deeper into that.
thinking
**Reviewing differential conventions**

I need to look closely at lines 390-392 and cross-reference them with lines 273-280 in higher_genus_foundations, which states it's not the classical bar differential over a point. This could indicate object conflation. I already have lines 273-280, but I also want to check lines 4-10 from the chapter opening. It seems that Step 2's reference to the "classical Koszul/Ext complex of gr_F A" is unsupported and contradicts the convention. I should also check if the theorem proof applies the EGA base change theorem correctly, especially regarding stacks.
thinking
**Examining cohomology terms**

I'm wondering if there's an issue with saying that the "full fiber complex, including curvature terms, has cohomology concentrated in bar-differential degree 0." It seems that the curved complex isn't defined here. I need to inspect whether the theorem statement is misnamed "fiber-center identification (unconditional)." The chapter opening lines 43-51 mention being unconditional on the Koszul locus, which might bring up some inconsistencies. I should definitely look into that further to clarify its implications.
thinking
**Exploring quantum concepts**

I could mention cross-volume use in Volume II and the main theorem related to quantum complementarity, which might depend on C0. I’m considering checking the proof, particularly Step 7 to see if it references C0, but I'm unsure if that's necessary. The user asked about downstream propagation, so I could also bring up the theorem used in Volume II with respect to symplectic polarization, possibly linking it to theorem C decomposition. I’ll search for relevant lines around that content.
exec
/bin/zsh -lc "rg -n 'fiber-center-identification|C0|center local system|R\\"'^0'"\\\\pi_\\{g\\*\\}\\\\bar\\{B\\}' chapters/theory/higher_genus_complementarity.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
48: with $R^0\pi_{g*}\bar{B}^{(g)}(\cA) \cong \mathcal{Z}_{\cA}$
49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
93:The fiber--center identification~(C0) and the
191:where $\mathcal{Z}(\cA)$ is the center local system.
350:\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
351:\label{thm:fiber-center-identification}
368:R^0\pi_{g*}\bar{B}^{(g)}(\cA)
372:where $\mathcal{Z}_{\cA}$ is the center local system.
1790:\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
1812:The center local system $\mathcal{Z}(\cA)$ on
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '38,52p;88,95p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
    38	This is Theorem~C
    39	(Theorem~\ref{thm:quantum-complementarity-main}).
    40	Theorem~C decomposes into three layers
    41	with distinct logical statuses.
    42	\begin{enumerate}[label=\textup{(C\arabic*)},start=0]
    43	\item \emph{Fiber--center identification
    44	 \textup{(}unconditional on the Koszul locus\textup{)}.}\;
    45	 For every chiral algebra~$\cA$ carrying a modular pre-Koszul datum
    46	 with finite-dimensional fiber cohomology, the relative bar family
    47	 satisfies $R^q\pi_{g*}\bar{B}^{(g)}(\cA) = 0$ for $q \neq 0$,
    48	 with $R^0\pi_{g*}\bar{B}^{(g)}(\cA) \cong \mathcal{Z}_{\cA}$
    49	 \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
    50	 This produces the ambient complex on which~\textup{(C1)}
    51	 and~\textup{(C2)} operate.
    52	
    88	perfectness requires PBW filterability and finite-dimensional
    89	fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
    90	nondegeneracy of the Verdier pairing is a hypothesis verified
    91	family by family
    92	(Proposition~\ref{prop:standard-examples-modular-koszul}).




thinking
**Clarifying theorem statements**

I’m discovering that "unconditional on Koszul locus" might be a bit misleading, since the proof relies on a filtered-complete PBW criterion and specifically considers families with verified MK antecedents. I wonder if the theorem statement requires a modular pre-Koszul datum, which would define the Koszul locus. The question asks if this is valid for all families or just specific ones. Summarizing, the theorem suggests an axiomatic all-family statement, but the proof uses specific machinery not applicable to every family.
thinking
**Considering boundary values in propositions**

I’m thinking about how standard examples in propositions exclude Heisenberg at k=0, while the Kac-Moody generic framework leaves out an exceptional set. The Virasoro case might have all central charges in genus 0 but is generic at all genera. I wonder if the theorem might exclude k=0 based on unverified antecedents. The key question is whether counterexamples could arise at these boundary values. I should definitely mention that the theorem doesn't address boundaries effectively, particularly for Heisenberg at k=0 and other critical cases.
thinking
**Examining the theorem's implications**

The theorem’s opening, stating “for every chiral algebra carrying modular pre-Koszul datum,” doesn’t assure that k=0 holds this datum. This raises a concern since boundary values aren't included in verified family surfaces. I should note that k=0 and non-generic levels are not accounted for, and it's essential to use precise citations from the propositions. Maybe it carries a medium severity in implications. I’ll also need to delve into the conflation of direct objects. Perhaps Step 3 indicates that H^0 is a graded coalgebra?
thinking
**Exploring algebraic relationships**

I’m thinking that D2 in the modular pre-Koszul context might explicitly state that \bar B^\vee ≅ A^! as factorization algebras. It’s interesting to note that \bar B itself is the Koszul dual coalgebra. I should consider citing the higher_genus_modular_koszul content from lines 548-552 to support this. Capturing this with line numbers could help clarify my points while presenting these relationships effectively. I'll need to gather more context to solidify my understanding.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '544,553p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   544	A reduced bar construction
   545	$\bar{B}_X(\cA) \in \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$
   546	(Definition~\ref{def:bar-differential-complete},
   547	Theorem~\ref{thm:bar-nilpotency-complete}).
   548	
   549	\item\label{D:dual}
   550	A candidate Koszul dual chiral algebra $\cA^!$ on~$X$ with
   551	universal twisting morphism
   552	$\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
   553	$\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '552,556p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   552	$\tau\colon \bar{B}_X(\cA) \to \cA^!$. The identification
   553	$\bar{B}_X(\cA)^\vee \simeq \cA^!$ as factorization algebras is a
   554	\emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},
   555	not an input; $\bar{B}_X(\cA)$ itself is the Koszul dual \emph{coalgebra}.
   556	




thinking
**Analyzing contradictions**

I see there's a contradiction in Step 3 regarding the identification with the Koszul dual coalgebra and earlier objects. Good to note that there might be missing proof for the cited lemmas and check their perfection. While it seems like the cited results are likely proved, I wonder if the corollary supports what's needed. Also, searching for the "center-bar identification" reveals it may not actually correspond to a theorem. There may be a hidden conflation here too, especially around the spectral sequence's degree.
thinking
**Exploring cohomological degrees**

I’m noticing that because E_1 is concentrated at q=0, the differential d_r could lead the target to be zero if page indices are only for q≥0, but do we truly know q is nonnegative? If the cohomological degree allows for negatives due to desuspension, that could complicate things. Earlier theorems utilize H^q, suggesting q may also be negative. Since the introduction mentions bar cohomology can indeed be negative, it conflicts with previous assertions about zero rows in the spectral sequence. This needs more clarification!
thinking
**Clarifying bar cohomology**

I’m realizing that the Heisenberg genus-0 bar cohomology actually appears in H^{-1}, not H^0, which is quite interesting! But then, the theorem in Step 2 indicates that the associated graded cohomology is focused on total degree 0. Meanwhile, the introduction states that the bar cohomology is concentrated in degree -1. Is there possibly an indexing shift happening here? It feels like I may need to work through this apparent contradiction a bit more!
thinking
**Inspecting theorem bar concentration**

I’m thinking about inspecting theorem bar concentration. There seems to be a need to search for lines around the label. I want to clarify what specific aspects or details I'd be looking for in this search. Maybe I'll gather some context about the theorem and its relevance to the concentration aspect. This could lead to a more informed understanding and help me clarify what I’m trying to achieve in terms of results.
exec
/bin/zsh -lc "rg -n 'thm:bar-concentration|Bar concentration' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
508: (Theorem~\ref{thm:bar-concentration}): for a Koszul morphism,
1061:\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
1062:\label{thm:bar-concentration}
2045:(Theorem~\ref{thm:bar-concentration}), which is the input for
5915:\item $\mathrm{A}_1$: Bar concentration
5916: (Theorem~\ref{thm:bar-concentration}), used by
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1061,1115p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1061	\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
  1062	\label{thm:bar-concentration}
  1063	\index{bar complex!concentration}
  1064	\textup{[Regime: quadratic on the Koszul locus
  1065	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1066	
  1067	Let $(\cA_1, \cA_2)$ be a chiral Koszul pair
  1068	\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})}.
  1069	Then the augmented bar complex $\bar{B}^{\mathrm{ch}}(\cA_1)$,
  1070	equipped with its bigrading by bar degree~$p$ and bar-differential
  1071	cohomological degree~$q$, satisfies:
  1072	\[
  1073	H^{p,q}(\bar{B}^{\mathrm{ch}}(\cA_1)) = 0
  1074	\quad\text{for } q \neq 0,
  1075	\qquad
  1076	H^{p,0}(\bar{B}^{\mathrm{ch}}(\cA_1)) \cong (\cA_2^!)_p.
  1077	\]
  1078	% Resolved RECTIFICATION-FLAG (2026-04-07): The notation $\cA_2^!$ when
  1079	% $\cA_2 = \cA_1^!$ creates a notational double-dual. The intended meaning
  1080	% is the bar cohomology of $\cA_1$, i.e.\ $\cA_1^i = H^*(\barBch(\cA_1))$

thinking
**Evaluating mathematical citations**

I'm working through some complex theorems in cohomology and noticing that theorem bar concentration could support the identification in Step 3 regarding H^{p,0} and dual coalgebra. However, the citation in C0 focuses on a corollary instead of theorem bar concentration. That might be a mistake in citation rather than in the identification with A^i. Yet, it's clear that Step 3's claim about the center is unsupported. I wonder if theorem bar concentration could provide a better result, specifically citing its connection to genus 0.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '687,769p;1396,1605p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   687	\label{prop:standard-examples-modular-koszul}
   688	\index{modular Koszul chiral algebra!examples}
   689	\textup{[Regime: quadratic
   690	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   691	
   692	The following chiral algebras satisfy the antecedent axioms
   693	\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
   694	Theorems~\textup{\ref{thm:higher-genus-inversion}}
   695	and~\textup{\ref{thm:quantum-complementarity-main}} then supply
   696	\textup{MK4--MK5}, so they are modular Koszul:
   697	\begin{enumerate}[label=\textup{(\alph*)}]
   698	\item the Heisenberg algebra $\mathcal{H}_\kappa$
   699	 (Convention~\textup{\ref{conv:heisenberg-kappa-notation}}) at any
   700	 nonzero level $\kappa \neq 0$\textup{;}
   701	\item the free fermion algebra $\mathcal{F}$ and the $\beta\gamma$-$bc$
   702	 ghost systems.
   703	\end{enumerate}
   704	\end{proposition}
   705	
   706	\begin{proof}



thinking
**Evaluating critical issues**

I'm identifying two critical concerns here. The lemma's perfectness criterion might be invalid due to ordinary cohomology and base change of curved differentials. It seems that theorem C0 could inherit this flaw. The second concern relates to critical step 3, where there's potential conflation of objects. I think it would be useful to report both issues. I should also consider how severe each concern is, so I can prioritize addressing them.
thinking
**Considering fiber-cohomology issues**

I’m wondering if there’s a potential issue with the lemma related to fiber-cohomology, particularly concerning its proof on the smooth locus. It seems that this lemma relies on ordinary cohomology of curved differentials, but I'm not sure if that's solid. There's a lot going on here, so I'll need to take a closer look. Maybe I should consider how the concepts interact to clarify my understanding!
thinking
**Confirming theorem requirements**

I’m thinking it might not be necessary to dig too deeply right now. I want to check a specific point around 4260 just to make sure I get the details right. It’s mentioned later that theorem B needs coderived comparisons, and not just general ones. So, it seems prudent to confirm that detail to ensure I have everything accurate before moving forward!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4258,4270p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4258	\index{admissible level!scope boundary}
  4259	\index{bar-cobar inversion!failure at admissible levels}
  4260	Theorem~B requires Koszulity (MK1). For simple admissible affine
  4261	quotients $L_k(\fg)$ at levels $k=-h^\vee+p/q$, that hypothesis is
  4262	not currently verified: null vectors obstruct the PBW/Shapovalov
  4263	route, and the bar-cobar counit is therefore not promoted here as a
  4264	derived equivalence. The obstruction is expected to be carried by
  4265	the nontrivial higher bar data encoded in $\Theta_\cA$.
  4266	The replacement is the coderived factorization co-contra comparison on
  4267	the bar-coalgebra surface
  4268	\textup{(}Theorem~\ref{thm:factorization-positselski}\textup{)},
  4269	which is available without Koszulness.
  4270	\end{remark}
Plan update
  ✓ Load constitutional/status sources and the theorem surface
  ✓ Trace each proof step to cited dependencies and test hypotheses/scope
  ✓ Check cross-file and cross-volume propagation for status or scope drift
  → Re-verify surviving findings and prepare severity-ordered report



thinking
**Verifying findings on the theorem**

I need to ensure all findings are re-verified, especially with evidence and line numbers in mind. It might be necessary to double-check the C0 theorem's use of the center local system fiber at the smooth curve definition. I wonder if there could be any false positives regarding the corollary not identifying the center. Perhaps we should reopen the theorem bar concentration comment. I also need to classify the findings based on their importance, with some being critical.
thinking
**Deciding on final findings**

I might want to include just four findings in total. Here’s a potential concise summary. The first finding, labeled as critical, discusses how the fiber object in C0 is defined with a curved differential. The proof and prerequisite lemma involve various concepts like cohomology and spectral sequence convergence, but as it stands, Steps 2-4 might not be valid under the mentioned regime. The second critical finding notes that the main identification step doesn't align with the cited result regarding genus-0 bar cohomology.
thinking
**Refining reporting structure**

I should probably include a line like "Instances checked: 10," which covers the statement, steps, dependencies, and propagation. It looks like 10 is okay. Then, I'll state "Violations found: 5," and the overall result is a FAIL. I want to mention that findings are "ordered by severity." After the summary, it feels like I shouldn't add extra sentences. I also need to avoid nested bullets and start directly with the list. I'll focus on being concise yet clear.
codex
- [CRITICAL] [higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:238); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:258); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:350) — C0 and its prerequisite `lem:perfectness-criterion` are built on the fiber bar object with the curved differential `\dfib`, but then take ordinary `H^q`, `R^q\pi_*`, spectral-sequence cohomology, and EGA base change of that object. The repo’s own convention says `\dfib^2=\kappa(\cA)\omega_g` and that this lives in the coderived category; only `\Dg{g}` is a strict differential. On the stated `curved-central` surface, Steps 2–4 are therefore not well-typed unless one adds a flat-side comparison / replaces `\dfib` / restricts to a flat case such as `\kappa=0` (inference from the cited convention).

- [CRITICAL] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:411); [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:873); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:575); [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2645) — Step 3’s key identification does not follow from the cited source. `cor:bar-cohomology-koszul-dual` computes genus-0 bar cohomology/Koszul-dual data under PBW hypotheses; it does not identify that object with the center local system. But D4 defines `\mathcal Z_\cA` separately as the sheaf whose fiber is `Z(\cA|_\Sigma)`, and the introduction explicitly separates bar coalgebra/Koszul dual from center-type objects. The proof’s jump from “surviving bar cohomology/Koszul dual” to “center local system” is the main logical gap.

- [HIGH] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:357); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:385); [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:283); [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:697) — Hidden hypothesis/regime inflation: C0 is tagged only `curved-central`, but the proof imports the `filtered-complete` PBW lane (`gr_F\cA`, “classical Koszul/Ext complex”, PBW bar-cohomology corollary, PBW filterability). Those hypotheses appear in the PBW criterion and in `lem:perfectness-criterion`, but they are not stated in the theorem surface itself.

- [HIGH] [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:99); [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:1186) — Cross-volume propagation is live: Volume II already uses C0 to rewrite the ambient complex and to identify the `E_\infty` page with `\mathcal Z(\cA)`. Since C0’s proof is unsound, these downstream arguments inherit an unsupported premise.

- [MEDIUM] [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:43); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:698); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:740); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1548); [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1598) — “Unconditional on the Koszul locus” is not “all families” in the live manuscript surface. MK1–MK3 are only verified here for Heisenberg at nonzero level, free fermion/`βγ`-`bc`, generic affine Kac–Moody, generic Virasoro, and generic principal finite-type `\mathcal W`. Boundary/non-generic cases are outside the proved input surface.

## Summary
Instances checked: 10 | Violations found: 5 | Verdict: FAIL
tokens used
140,832
