# T02_thm_B (517s, gpt-5.4)

[CRITICAL] chapters/theory/higher_genus_complementarity.tex:4123 — Clause `(b)` of `thm:higher-genus-inversion` is stated as theorematic, but the proof at `4140-4172` only proves the Koszul/modular-locus quasi-isomorphism in `(a)`. Its cited support is circular: `chapters/theory/coderived_models.tex:247-270` proves `prop:coderived-adequacy(a)` by invoking `thm:higher-genus-inversion` itself, and its off-locus argument reuses the strict spectral sequence of `chapters/theory/bar_cobar_adjunction_inversion.tex:2024-2077`, which is formulated for complexes with `d^2=0`, not for the curved off-locus setting.

[CRITICAL] chapters/theory/higher_genus_complementarity.tex:4077 — The boundary induction step silently replaces a tensor product over the nodal fiber algebra by an ordinary tensor product over the ground field. But the actual gluing statements at `chapters/theory/higher_genus_complementarity.tex:3208-3253` are over `\mathcal A(p)`, not over `\mathbb C`. Without flatness or Tor-vanishing at the node, Künneth does not justify preservation of quasi-isomorphisms, so the proof of `lem:higher-genus-boundary-qi` does not follow.

[HIGH] chapters/theory/higher_genus_complementarity.tex:4120 — Part `(a)` of `thm:higher-genus-inversion` claims the spectral sequence collapses at `E_2`, but the proof at `4140-4172` establishes only the quasi-isomorphism of `\psi_g`. The `E_2`-collapse is only proved later in `lem:e2-collapse-higher-genus` at `4205-4218`, so the theorem statement outruns the proof attached to it.

[HIGH] chapters/theory/higher_genus_complementarity.tex:4018 — The open-stratum proof does not pin down which genus-`g` complex is being inverted. The manuscript distinguishes the curved fiberwise differential `\dfib` with `\dfib^2=\kappa(\cA)\omega_g` on a fixed curve and the strict corrected differential `\Dg{g}` with `\Dg{g}^2=0` (`chapters/theory/higher_genus_foundations.tex:229-270`, `chapters/theory/higher_genus_modular_koszul.tex:557-572`). Yet `lem:higher-genus-open-stratum-qi` passes from PBW concentration for `(\bar B^{(g)}(\cA),\dfib)` to the strict bar-cobar counit on a fixed curve via `thm:fundamental-twisting-morphisms` (`chapters/theory/chiral_koszul_pairs.tex:357-375`) without supplying the comparison between the curved and strict models.

[MEDIUM] chapters/theory/algebraic_foundations.tex:223 — The primary definition of the Koszul locus is conclusion-based: `\cA` is “Koszul” iff the genus-0 counit `\Omega_X(\bar B_X(\cA))\to\cA` is already a quasi-isomorphism. Consequently the genus-0 clause of `thm:bar-cobar-inversion-qi` (`chapters/theory/bar_cobar_adjunction_inversion.tex:1611-1623`) is tautological on the live definition rather than a recognition theorem from independent hypotheses. The antecedent, non-tautological notion only appears later via chiral Koszul data/pairs.

[MEDIUM] chapters/frame/guide_to_main_results.tex:37 — The public theorem summaries inflate scope. `guide_to_main_results.tex:37-40` and `preface.tex:1212-1215` advertise all-genera inversion “on the Koszul locus”, while the actual theorem assumes a modular pre-Koszul datum `(MK1–MK3)`. `heisenberg_frame.tex:4583-4585` and `4611-4615` further summarize the off-locus result as living in “the coderived category”, but the theorem only names the provisional coderived category.

## Summary
Instances checked: 17 | Violations found: 6 | Verdict: FAIL


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
session id: 019d8388-33a9-73b3-a21d-b9028610c1b2
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


MISSION: FALSIFY the proof of Theorem B: bar-cobar inversion Omega(B(A))→A qi on Koszul locus. Check: (a) is Koszul locus correctly defined? (b) does the qi actually induce iso on cohomology? (c) is the model structure correct? (d) what happens OFF the Koszul locus?

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
Auditing Theorem B as a falsification pass. I’m locating the live theorem/proof surface, then I’ll read the dependency chain and test each proof step against the cited sources and scope boundaries.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
Using `deep-beilinson-audit`. I’m reading the repo’s status/convention surfaces in parallel with locating the exact Theorem B statement and proof so the audit is tied to the live claim surface, not folklore.
exec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 50ms:
Total output lines: 260

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
 succeeded in 50ms:
Total output lines: 260

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
/bin/zsh -lc "rg -n \"Theorem B|thm:.*B|bar-cobar|Omega\\\\(B\\\\(A\\\\)\\\\)|Koszul locus|Theorem\\\\s*B\" chapters metadata -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 51ms:
Total output lines: 2759

metadata/verified_formulas.jsonl:30:{"id": "VF070", "domain": "anti-pattern", "correct": "Bar-cobar QI does NOT imply D^b(A-mod) ~ D^b(A!-mod). Need Positselski D^co/D^ctr.", "wrong": "D^b(A-mod) ~ D^b(A!-mod) from bar-cobar", "source": "Positselski", "violations": 2}
chapters/examples/deformation_quantization.tex:27: Theorem~\ref{thm:hochschild-bar-cobar}.
chapters/examples/deformation_quantization.tex:543:By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
chapters/examples/deformation_quantization.tex:605:\subsection{Relation to bar-cobar}
chapters/examples/deformation_quantization.tex:640:setting. The bar-cobar framework of this monograph
chapters/examples/deformation_quantization.tex:646:This explains why the bar-cobar construction controls quantization.
chapters/examples/deformation_quantization.tex:703:The bar-cobar duality admits a conjectural holographic interpretation:
chapters/examples/deformation_quantization.tex:778:Local-to-global principles & Explicit bar-cobar formulas \\
chapters/examples/deformation_quantization.tex:788:The paper on quadratic duality for chiral algebras \cite{GLZ22} focuses on Koszul duality for quadratic operads. The deformation quantization framework of this monograph generalizes from quadratic to arbitrary (non-quadratic via curvature), geometrizes the duality via bar-cobar configuration spaces, and provides explicit formulas for dualizing.
chapters/examples/deformation_quantization.tex:792:Ayala--Francis \cite{AF15} develop factorization homology. The bar-cobar perspective:
chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
chapters/examples/deformation_quantization.tex:808:bar-cobar composite (Theorem~\ref{thm:chiral-kontsevich}).
chapters/examples/deformation_quantization.tex:813:that the bar-cobar adjunction, restricted to the formal disk at genus~$0$, recovers classical Koszul duality, in agreement with the Francis--Gaitsgory formality
chapters/examples/deformation_quantization.tex:820:whether the genus-$g$ bar-cobar inversion of Theorem~B
chapters/examples/w_algebras_deep.tex:12:secondary Borcherds operation nonzero). The bar-cobar adjunction
chapters/examples/w_algebras_deep.tex:24:nilpotent currents) reduces, through the bar-cobar engine, to
chapters/examples/w_algebras_deep.tex:44:(Theorem~\ref{thm:completed-bar-cobar-strong}), is a
chapters/examples/w_algebras_deep.tex:880:bar-cobar template for the Gaberdiel--Gopakumar conjecture.
Plan update
Audit is scoped to Theorem B’s live statement, proof, and dependency chain. I’m reading the theorem surface first, then checking each cited dependency and the off-locus boundary claims before consolidating only findings that survive re-verification.
  ✓ Locate Theorem B statement(s), labels, and claimed status across core files
  → Read full theorem/proof surface for bar-cobar inversion and extract dependency chain
  • Audit cited lemmas/propositions for logical use, scope, and hidden assumptions
  • Check off-Koszul-locus claims, model-structure claims, and propagation across frames/concordance
  • Re-verify surviving findings and compile severity-ordered report

thinking
**Locating theorems**

I need to find the exact statements of the theorems. I’ll use the labels like thm:higher-genus-inversion and thm:bar-cobar-inversion-qi, and potentially reference theorem B. I want to gather full statements and proofs relevant to those topics. I'm also considering off-locus options, possibly related to higher_genus_modular_koszul. Let’s take a look and inspect everything carefully, and I’ll use parallel sed ranges to manage it all effectively.
codex
The concordance already exposes one pressure point: Theorem B is advertised as `ClaimStatusProvedHere`, but its scope is split between unconditional genus 0, conditional arbitrary genus, and a “standard landscape” carve-out. I’m reading the exact theorem statements and proofs now to see whether the proof surface really matches that advertised status.
exec
/bin/zsh -lc "sed -n '1560,2235p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:higher-genus-inversion|thm:bar-cobar-inversion-qi|Theorem B|bar-cobar inversion" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/higher_genus_modular_koszul.tex chapters/frame/guide_to_main_results.tex chapters/frame/preface.tex chapters/frame/heisenberg_frame.tex -S' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3060,3215p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '28,80p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:config-space-role}
The proof of the chiral comodule-contramodule correspondence
(Theorem~\ref{thm:chiral-co-contra-correspondence}) uses the
geometry of configuration spaces in three places:
\begin{enumerate}
\item \emph{Exactness of the chiral tensor product.}
 The tensor-hom adjunction for holonomic $\mathcal{D}_X$-modules
 on $\overline{C}_n(X)$ ensures that cofree comodules are injective
 and free contramodules are projective
 (Proposition~\ref{prop:chiral-inj-proj-resolutions}).
\item \emph{Conilpotency from conformal weight.}
 The conformal weight grading on $\bar{B}^{\mathrm{ch}}(\cA)$
 (inherited from $\cA$) ensures conilpotency
 (Theorem~\ref{thm:coalgebra-via-NAP}(4)), which is needed for
 the compact generation argument in Step~5 of the proof.
\item \emph{Finite-dimensionality from holonomicity.}
 The holonomicity of the bar complex on each configuration space
 stratum (Lemma~\ref{lem:bar-holonomicity}) ensures
 finite-dimensional graded pieces, which is
 needed for the duality between contramodules and complete modules
 succeeded in 51ms:
chapters/frame/guide_to_main_results.tex:37:\textbf{Theorem B} &
chapters/frame/guide_to_main_results.tex:41: Thm~\ref{thm:higher-genus-inversion} \\[4pt]
chapters/frame/preface.tex:99:Theorem~B proves bar-cobar inversion
chapters/frame/preface.tex:522:proves bar-cobar inversion; Volume~II would upgrade it to bulk
chapters/frame/preface.tex:1212:\noindent\textbf{Theorem~B} (bar-cobar inversion). On the Koszul
chapters/frame/preface.tex:3396:proved by PBW concentration $\to$ bar-cobar inversion $\to$
chapters/frame/preface.tex:3712:completion. Third, bar-cobar inversion produces the
chapters/frame/heisenberg_frame.tex:1155:(Theorem~\ref{thm:bar-cobar-inversion-qi}).
chapters/frame/heisenberg_frame.tex:1218:locus (Theorem~\ref{thm:bar-cobar-inversion-qi}). The general
chapters/frame/heisenberg_frame.tex:1233:The counit $\varepsilon_\tau$ is bar-cobar inversion
chapters/frame/heisenberg_frame.tex:1244:\section{Bar-cobar inversion: Theorem B in action}
chapters/frame/heisenberg_frame.tex:1338:(Theorem~\ref{thm:higher-genus-inversion})
chapters/frame/heisenberg_frame.tex:3410:bimodule, and the bar-cobar inversion
chapters/frame/heisenberg_frame.tex:4583:(Theorem~\ref{thm:higher-genus-inversion}):
chapters/frame/heisenberg_frame.tex:4770: & Arnold relation, bar-cobar inversion, genus tower,
chapters/theory/bar_cobar_adjunction_inversion.tex:6:%% proves that the adjunction inverts: Theorem B says
chapters/theory/bar_cobar_adjunction_inversion.tex:21:Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) gives the
chapters/theory/bar_cobar_adjunction_inversion.tex:50:admit bar-cobar inversion by increasingly refined completions; the
chapters/theory/bar_cobar_adjunction_inversion.tex:70:algebras admit direct bar-cobar inversion without completion; curved
chapters/theory/bar_cobar_adjunction_inversion.tex:141:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
 succeeded in 51ms:
\label{rem:kappa-holo-sugawara-shift}
\index{Sugawara construction!holographic shift}%
\index{holographic anomaly!Sugawara shift}%
For an affine Kac--Moody algebra at level~$k$, the bar-intrinsic
identity
\begin{equation}\label{eq:sugawara-shift-holographic}
\operatorname{av}(r(z))
\;+\;
\tfrac{1}{2}\dim(\fg)
\;=\;
\kappa(V_k(\fg))
\;=\;
\frac{\dim(\fg)\,(k + h^\vee)}{2\,h^\vee}
\end{equation}
splits the holographic central charge into two pieces with
distinct bulk interpretations. The first summand
$\operatorname{av}(r(z)) = \dim(\fg)\,k/(2 h^\vee)$ is the
\emph{bare} boundary coupling: it is the level-dependent piece
seen directly by the $r$-matrix, and at $k = 0$ it vanishes,
consistent with the AP\textup{126} mandate that a level-stripped
 succeeded in 52ms:
 $\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
 \rightleftarrows
 \operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))$,
 intertwined with Verdier duality:
 $\mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA)
 \simeq \cA^!_\infty$ (factorization \emph{algebra},
 not coalgebra). &
 Thm~\ref{thm:bar-cobar-isomorphism-main} \\[4pt]

\textbf{Theorem B} &
 Bar--cobar inversion: on the Koszul locus, the counit
 $\Omega_X \bar{B}_X(\cA) \xrightarrow{\sim} \cA$ is a
 quasi-isomorphism at all genera. &
 Thm~\ref{thm:higher-genus-inversion} \\[4pt]

\textbf{Theorem C} &
 Complementarity: $Q_g(\cA) \oplus Q_g(\cA^!)
 \cong H^*(\overline{\cM}_g, \cZ_\cA)$ for all $g \ge 1$.
 Upgraded to shifted-symplectic Lagrangian geometry. &
 Thm~\ref{thm:quantum-complementarity-main} \\[4pt]

thinking
**Checking theorem proof details**

I need to ensure I have the full statement and proof for the theorem on higher genus inversion. It seems like there are dependencies regarding lemmas on open, boundary, and extension cases. I'll focus on inspecting the document from around line 3050 onwards, checking for the theorem statement and proof. It might take a bit of searching, especially around line 3140, so I’ll read through those sections carefully. Let's see what I find!
codex
The genus-0 theorem already shows a structural concern: its proof delegates the actual quasi-isomorphism to earlier theorems, then imports higher genus from `thm:higher-genus-inversion`. I’m drilling into that theorem and the three lemmas it cites, because that is where scope inflation or circularity would surface.
exec
/bin/zsh -lc "sed -n '2800,3225p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|label\\{lem:higher-genus-open-stratum-qi\\}|label\\{lem:higher-genus-boundary-qi\\}|label\\{lem:extension-across-boundary-qi\\}|label\\{def:modular-koszul-chiral\\}|label\\{MK:modular\\}|label\\{thm:BD-extension-higher-genus\\}|label\\{thm:pbw-allgenera-km\\}|label\\{thm:pbw-allgenera-principal-w\\}|label\\{thm:fundamental-twisting-morphisms\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/lattice_foundations.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.

Bar-cobar inversion (Theorem~B) proves that
$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
The proof uses one fact: the bar differential squares to zero.
At genus~$g \geq 1$, this fact fails fiberwise.
The bar complex $\barB^{(g)}(\cA)$ acquires curvature
\[
 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
\]
%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
where $\omega_g = c_1(\lambda)$ is the Hodge class on
$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
The fiberwise differential no longer squares to zero; cobar inversion,
as stated, does not extend.

 succeeded in 50ms:
chapters/theory/chiral_koszul_pairs.tex:357:\label{thm:fundamental-twisting-morphisms}
chapters/theory/higher_genus_modular_koszul.tex:535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
chapters/theory/higher_genus_modular_koszul.tex:614:\item\label{MK:modular}
chapters/theory/higher_genus_modular_koszul.tex:771:\label{thm:pbw-allgenera-principal-w}
chapters/theory/higher_genus_modular_koszul.tex:1197:\label{thm:pbw-allgenera-km}
 succeeded in 52ms:
In particular:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Convergence.}
 The series~\eqref{eq:scalar-free-energy-ahat}
 converges for $|\hbar| < 2\pi$
 (the first zero of $\sin(\hbar/2)$).
\item \emph{Infinite product.}
 $\displaystyle
 \frac{\hbar/2}{\sin(\hbar/2)}
 \;=\;
 \prod_{n=1}^{\infty}
 \Bigl(1 - \frac{\hbar^2}{4n^2\pi^2}\Bigr)^{\!-1}$,
 the zeta-regularized determinant of the Laplacian
 on~$S^1$ with eigenvalues $\omega_n = 2n\pi$.
\item \emph{Low-genus values.}
 $\lambda_1^{\mathrm{FP}} = 1/24$, \;
 $\lambda_2^{\mathrm{FP}} = 7/5760$, \;
 $\lambda_3^{\mathrm{FP}} = 31/967680$.
 The universal genus-$2$-to-genus-$1$ ratio is
 $F_2/F_1 = 7/240$, independent of~$\cA$.

thinking
**Checking theorem notation**

I'm noticing that the sed command didn't include the theorem due to the labeling, which might be placed later or earlier. I need to find the exact line for "thm:higher-genus-inversion" with the rg tool. It seems our rg pattern didn't give any output, possibly because the line wasn't found due to quoting issues. So, I think I should specify rg to look specifically in that file.
exec
/bin/zsh -lc 'rg -n "thm:higher-genus-inversion|higher-genus inversion|open-stratum-qi|boundary-qi|extension-across-boundary-qi|BD-extension-higher-genus" chapters/theory/higher_genus_modular_koszul.tex -S' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
32:(Theorem~\ref{thm:higher-genus-inversion}).
205:For each $g \geq 0$, the bar-cobar inversion of Theorem~\ref{thm:higher-genus-inversion}
345:At each genus~$g$, the bar-cobar inversion of Theorem~\ref{thm:higher-genus-inversion}
373:(Theorem~\ref{thm:higher-genus-inversion}) shows this complex is exact,
407:(Theorem~\ref{thm:higher-genus-inversion}); the duality
499:\emph{(Bar-cobar inversion; Theorem~\textup{\ref{thm:higher-genus-inversion}}.)}
593:or complementarity. Theorems~\ref{thm:higher-genus-inversion}
626:\emph{(Bar-cobar inversion; Theorem~\textup{\ref{thm:higher-genus-inversion}}.)}
645:consequences proved (Theorems~\ref{thm:higher-genus-inversion} and
655:\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
694:Theorems~\textup{\ref{thm:higher-genus-inversion}}
736:Theorems~\textup{\ref{thm:higher-genus-inversion}}
1177:By Theorems~\textup{\ref{thm:higher-genus-inversion}}
1192:Theorems~\ref{thm:higher-genus-inversion}
1404:Theorems~\textup{\ref{thm:higher-genus-inversion}}
1436:Theorems~\ref{thm:higher-genus-inversion}
1555:Theorems~\textup{\ref{thm:higher-genus-inversion}}
1586:Theorems~\ref{thm:higher-genus-inversion}
1607:Theorems~\textup{\ref{thm:higher-genus-inversion}}
1646:Theorems~\ref{thm:higher-genus-inversion}
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|begin\\{theorem\\}.*higher-genus|Higher-genus inversion\" chapters -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:1605:\begin{theorem}[Higher genus Heisenberg; \ClaimStatusProvedHere]\label{thm:heisenberg-higher-genus}
chapters/examples/kac_moody.tex:1973:\begin{theorem}[Higher genus corrections to Koszul duality; \ClaimStatusProvedHere]\label{thm:km-higher-genus-corrections}
chapters/theory/higher_genus_complementarity.tex:3109:\begin{theorem}[Chevalley--Cousin acyclicity at higher genus; \ClaimStatusProvedHere]\label{thm:CC-acyclicity-higher-genus}
chapters/theory/higher_genus_complementarity.tex:4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
chapters/theory/poincare_duality_quantum.tex:644:\begin{theorem}[Prism principle: higher-genus extension;
chapters/theory/configuration_spaces.tex:289:\begin{theorem}[Boundary strata of \texorpdfstring{$\overline{\mathcal{M}}_{g,n}$}{M-bar(g,n)} {\cite{DeligneM69,Knudsen83}}; \ClaimStatusProvedElsewhere]\label{thm:boundary-higher-genus}
chapters/connections/genus_complete.tex:159:\begin{theorem}[Higher-genus bar differential; \ClaimStatusProvedElsewhere{} \cite{CG17,costello-renormalization}]\label{thm:higher-genus-diff}

thinking
**Exploring theorems and definitions**

I need to check out the theorem in higher_genus_complementarity.tex. It's important to read the statement, proof, and any cited lemmas. I’ll also look for the definition of modular-koszul-chiral in the higher_genus_modular_koszul file. It seems I need to inspect the theorem and its dependencies thoroughly to grasp it all fully. Let's dig into the details!
codex
The higher-genus theorem lives in `higher_genus_complementarity.tex`, not the modular-Koszul chapter that advertises it. I’m reading that proof chain next, including the open-stratum, boundary, and extension lemmas it cites, because any break there invalidates the all-genus claim surface.
exec
/bin/zsh -lc "sed -n '3950,4215p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3000,3185p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|label\\{lem:higher-genus-open-stratum-qi\\}|label\\{lem:higher-genus-boundary-qi\\}|label\\{lem:extension-across-boundary-qi\\}|label\\{thm:CC-acyclicity-higher-genus\\}|label\\{lem:boundary-kunneth\\}|label\\{lem:open-stratum-pbw\\}|label\\{lem:normal-crossing-mv\\}\" chapters/theory/higher_genus_complementarity.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3109:\begin{theorem}[Chevalley--Cousin acyclicity at higher genus; \ClaimStatusProvedHere]\label{thm:CC-acyclicity-higher-genus}
4010:\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
4059:\begin{lemma}[Boundary-stratum compatibility of \texorpdfstring{$\psi_g$}{psi-g}; \ClaimStatusProvedHere]\label{lem:higher-genus-boundary-qi}
4085:\begin{lemma}[Extension across boundary; \ClaimStatusProvedHere]\label{lem:extension-across-boundary-qi}
4101:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
 succeeded in 52ms:
\begin{lemma}[Algebra structure from Verdier dual; \ClaimStatusProvedHere]\label{lem:coalgebra-verdier-AF}
Under $\text{DR}$, the algebra structure on $\cA^!_\infty$ comes from
applying Verdier duality to the coalgebra
$\bar{B}(\mathcal{A})$: Verdier duality converts the
factorization coalgebra $\bar{B}(\cA)$ into the factorization
algebra $\cA^!_\infty$.
\end{lemma}

\begin{proof}[Proof of Lemma]
The multiplication $\mu: \mathcal{A} \otimes \mathcal{A} \to \mathcal{A}$ dualizes to:
\[\mathbb{D}(\mu): \mathbb{D}(\mathcal{A}) \to \mathbb{D}(\mathcal{A} \otimes \mathcal{A}) 
\simeq \mathbb{D}(\mathcal{A}) \otimes \mathbb{D}(\mathcal{A})\]

Applying $\text{DR}$:
\[\text{DR}(\mathbb{D}(\mu)): \text{DR}(\mathcal{A})^* \to \text{DR}(\mathcal{A})^* 
\otimes \text{DR}(\mathcal{A})^*\]

This is the coproduct structure on the coalgebra.

In factorization terms, this says:
 succeeded in 52ms:
\label{subsec:BD-genus-zero-review}

We review the Beilinson--Drinfeld construction at genus zero, identifying what generalizes.

\begin{theorem}[BD 3.4.12: genus zero acyclicity; \ClaimStatusProvedHere]\label{thm:BD-genus-zero}
\index{Beilinson--Drinfeld!higher genus}
For a smooth projective curve $X$ and chiral algebra $\mathcal{A}$, the Chevalley--Cousin complex $C(\mathcal{A})$ defined over the Ran space $R(X)$ is acyclic:
\[H^i(R(X), C(\mathcal{A})) = 
\begin{cases}
\mathcal{A} & i = 0 \\
0 & i \neq 0
\end{cases}\]
\end{theorem}

\begin{proof}[Key steps from BD §3.4]
\emph{Step 1 (BD 3.4.10):} Embed $M(X) \hookrightarrow M(X^S)$ using the diagonal embedding $\Delta^{(S)}_*$. This is fully faithful and pseudo-tensor.

\emph{Step 2 (BD 3.4.11):} Construct the Chevalley--Cousin complex:
\[C(\mathcal{A})_{X^I} = \bigoplus_{T \in Q(I)} \Delta^{(I/T)}_* j^{(I/T)}_* j^{(I/T)*} \omega_{X^T}[|T|]\]
where $j^{(I/T)}: X^T \to X^I$ removes the diagonals.
exec
/bin/zsh -lc "rg -n \"label\\{def:koszul-chiral-algebra\\}|label\\{rem:koszul-chiral\\}|label\\{thm:fundamental-twisting-morphisms\\}|label\\{thm:bar-nilpotency-complete\\}|label\\{thm:chiral-koszul-duality\\}|label\\{thm:bar-cobar-adjunction\\}|label\\{thm:bar-functorial\\}|label\\{def:provisional-coderived\\}|label\\{prop:coderived-adequacy\\}|label\\{thm:bar-modular-operad\\}|label\\{thm:ss-quantum\\}|label\\{prop:gluing-at-nodes\\}|label\\{lem:boundary-compatible\\}|label\\{thm:pbw-allgenera-virasoro\\}|label\\{thm:heisenberg-higher-genus\\}|label\\{thm:operadic-homotopy-convolution\\}\" chapters -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '300,520p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,700p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:1605:\begin{theorem}[Higher genus Heisenberg; \ClaimStatusProvedHere]\label{thm:heisenberg-higher-genus}
chapters/theory/bar_cobar_adjunction_curved.tex:6161: \ClaimStatusProvedHere]\label{thm:bar-modular-operad}%
chapters/theory/bar_construction.tex:773:\begin{theorem}[Nilpotency of bar differential; \ClaimStatusProvedHere]\label{thm:bar-nilpotency-complete}
chapters/theory/bar_construction.tex:1414:\label{thm:bar-functorial}
chapters/theory/higher_genus_modular_koszul.tex:1446:\label{thm:pbw-allgenera-virasoro}
chapters/theory/coderived_models.tex:234:\label{def:provisional-coderived}
chapters/theory/coderived_models.tex:243:\label{prop:coderived-adequacy}
chapters/theory/higher_genus_complementarity.tex:696:\label{thm:ss-quantum}
chapters/theory/higher_genus_complementarity.tex:3208:\begin{proposition}[Gluing formula at nodes; \ClaimStatusProvedHere]\label{prop:gluing-at-nodes}
chapters/theory/higher_genus_complementarity.tex:3236:\begin{lemma}[Boundary compatibility; \ClaimStatusProvedHere]\label{lem:boundary-compatible}
chapters/theory/cobar_construction.tex:1879:\label{thm:bar-cobar-adjunction}
chapters/theory/cobar_construction.tex:2950:\label{rem:koszul-chiral}
chapters/theory/algebraic_foundations.tex:223:\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
chapters/theory/algebraic_foundations.tex:882:\label{thm:operadic-homotopy-convolution}%
chapters/theory/chiral_koszul_pairs.tex:357:\label{thm:fundamental-twisting-morphisms}
chapters/theory/chiral_koszul_pairs.tex:4097:\label{thm:chiral-koszul-duality}
 succeeded in 51ms:
$\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$ shifted by~$[-1]$:
the rows of the double complex are
$\cA \leftarrow \cA \otimes \cC \leftarrow \cA \otimes \cC^{\otimes 2}
\leftarrow \cdots$, which is the bar-type resolution of the
augmentation map. This is the chiral analogue of
\cite[Lemma~2.2.5]{LV12}.
\end{proof}

\begin{lemma}[Right twisted tensor product as mapping cone; \ClaimStatusProvedHere]
\label{lem:twisted-product-cone-unit}
\index{twisted tensor product!mapping cone}
Under the same hypotheses, there is a natural identification
\[
K_\tau^R(\cC,\cA) \;\simeq\; \operatorname{Cone}(\eta_\tau)[-1]
\]
where $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is the canonical
unit. In particular, $K_\tau^R$ is acyclic if and only if
$\eta_\tau$ is a weak equivalence.
\end{lemma}

 succeeded in 51ms:
%% ===== Editorial bridge: the inversion half of the chapter =====
%%
%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
%% framework that supports it off the quadratic locus. This second half
%% proves that the adjunction inverts: Theorem B says
%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
%% Together, Theorems A and B close the algebraic engine of the monograph.

\bigskip
\noindent\textbf{From adjunction to inversion.}\enspace
An adjunction that is not an equivalence is a deficiency: it
records the information lost in the round trip. Theorem~A
gives the adjunction $\Omegach \dashv \barBch$; the question is
whether the counit $\psi \colon \Omegach(\barBch(\cA)) \to \cA$
is a quasi-isomorphism, so that no information is lost. This is
not a formal consequence of the adjunction; it requires the
geometry of the Fulton--MacPherson compactification and the
Koszulness of the underlying chiral operad.

 succeeded in 52ms:
$Q_g(\cA^!) := H^*(\mathbf{Q}_g(\cA^!))$ recover the
deformation and obstruction spaces of
Theorem~\ref{thm:quantum-complementarity-main}.
\end{definition}

\begin{remark}[Model independence]\label{rem:model-independence}
Any two admissible dg presentations of the same factorization
object are connected by a contractible space of quasi-isomorphisms,
so the homotopy axioms \ref{MK:koszul-htpy}--\ref{MK:modular-htpy}
are invariants of the factorization algebra, not of a
chosen model. Definition~\ref{def:modular-koszul-chiral} provides
the dg model used throughout.
\end{remark}

\begin{definition}[Modular pre-Koszul chiral algebra: dg model of
 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
Let $X$ be a smooth projective curve over $\mathbb{C}$.
A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
the following data and satisfying the following axioms.

thinking
**Evaluating mathematical concepts**

I need to inspect the base case for the theorem on chiral-Koszul duality, exploring its meanings and any hidden assumptions. Then there's the concept of bar-nilpotency-complete. I’ll also look into the model structure and provisional coderived category definitions. I think I'll check out the theorem related to bar-cobar adjunction from cobar construction, and the one on bar-functoriality too. I'll need to read and assess the relevant citations for this.
codex
I now have the theorem/proof surface. The higher-genus proof is a three-lemma induction over the Deligne–Mumford boundary, so the next pass is checking whether those lemmas actually justify the jump from fiberwise/PBW data to a global quasi-isomorphism, and whether the off-locus “coderived persistence” is backed by an actual model-category statement.
exec
/bin/zsh -lc "sed -n '1800,1945p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '740,860p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4060,4145p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '220,330p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the three sign sources defines a parity character on $\operatorname{Aut}(T)$:
Koszul signs come from permuting tensor factors, orientation signs
come from permuting configuration-space coordinates, and operadic
signs come from grafting odd inputs through the operad composition.

The key identity is checked on an adjacent transposition of two inputs
$\phi_i,\phi_j$. On the desuspension $s^{-1}\bar{\mathcal{A}}$, that
transposition contributes
\[
(-1)^{(|\phi_i|-1)(|\phi_j|-1)}
= (-1)^{|\phi_i||\phi_j|}
 (-1)^{|\phi_i|+|\phi_j|}
 (-1).
\]
The first factor is the Koszul sign, the second is the operadic sign,
and the last factor is the orientation sign from swapping the two
coordinates. Hence the combined action on
$s^{-1}\bar{\mathcal{A}}$ already contains all three sign sources.

Because every tree automorphism is generated by adjacent
 succeeded in 52ms:
\end{proposition}

\begin{proof}
The bar-intrinsic MC element $\Theta_\cA := D_\cA - d_0$ (Theorem~\ref{thm:mc2-bar-intrinsic}) lives in the modular convolution algebra $\gAmod$, and the cobar complex reconstructs $\cA$ from $\barB(\cA)$ by the bar-cobar adjunction (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
The degree-$r$ component of the $\mathrm{FCom}$-algebra structure on $\Omega(\barB(\cA))$ is the graph sum $\sum_{|\Gamma| = r} |\mathrm{Aut}(\Gamma)|^{-1} \ell_\Gamma$, which is precisely the degree-$r$ projection $\Theta_\cA^{\leq r}$ of the universal MC element (Corollary~\ref{cor:shadow-extraction}).
\end{proof}

\subsection{Čech-Alexander complex realization}

\begin{theorem}[Cobar as Čech complex; \ClaimStatusProvedHere]\label{thm:cobar-cech}
The geometric cobar complex is quasi-isomorphic to a Čech-type complex:
\[
\Omega^{\text{ch}}(\mathcal{C}) \simeq \check{C}^{\bullet}(\mathfrak{U}, \mathcal{F}_{\mathcal{C}})
\]
where $\mathfrak{U} = \{U_{\sigma}\}$ is the open cover of $\overline{C}_n(X)$ by coordinate charts and $\mathcal{F}_{\mathcal{C}}$ is the factorization algebra associated to $\mathcal{C}$.
\end{theorem}

\begin{proof}
The factorization algebra $\mathcal{F}_{\mathcal{C}}$ on $X$ is defined by the assignment $U \mapsto \mathcal{F}_{\mathcal{C}}(U) = \Omega(\mathcal{C}|_U)$, with factorization structure maps $\mathcal{F}_{\mathcal{C}}(U_1) \otimes \mathcal{F}_{\mathcal{C}}(U_2) \to \mathcal{F}_{\mathcal{C}}(U_1 \sqcup U_2)$ for disjoint opens, given by the cobar product. This is a cosheaf on the Ran space $\operatorname{Ran}(X)$, hence in particular a precosheaf on $X$.

 succeeded in 52ms:
 $\operatorname{gr}_{\mathcal{F}} f$ is a quasi-isomorphism of the
 strict complexes $(\operatorname{gr} M, \operatorname{gr}^0 d)
 \xrightarrow{\sim} (\operatorname{gr} N, \operatorname{gr}^0 d')$.
\item The induced map on coacyclic quotients
 $M/\operatorname{coacyc}(M) \to N/\operatorname{coacyc}(N)$ is an
 isomorphism, where $\operatorname{coacyc}(M)$ is the thick subcategory
 generated by totalizations of short exact sequences
 (Positselski~\cite{Positselski11}).
\end{enumerate}
The equivalence of (i) and (ii) holds for bounded-below filtrations
by~\cite[Proposition~3.5]{Positselski11}.
\end{definition}

\begin{definition}[Provisional coderived category]
\label{def:provisional-coderived}
\index{coderived category!provisional|textbf}
The \emph{provisional coderived category} $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$
is the localization of the category of filtered curved factorization
models (Definition~\ref{def:filtered-curved-model}) at the weak
equivalences of Definition~\ref{def:curved-weak-equiv}.
 succeeded in 52ms:
\end{align*}

Adding: $(d_! \boxtimes \mathrm{id} + \mathrm{id} \boxtimes d_!)(\Delta(\phi_i^*))$ gives terms 1 and 4 from the left side. The remaining terms (2 and 3) vanish because $d_!$ is \emph{defined} as the unique coderivation of the cofree coalgebra $T^c(V^*)$ extending its projection to cogenerators. The cofree universal property guarantees the coderivation identity on \emph{all} elements, not just cogenerators; the explicit computation above verifies compatibility on the cogenerator level, which determines $d_!$ uniquely.

\medskip
\noindent\emph{(4) Nilpotence $d_!^2 = 0$.}

This is equivalent to associativity of the chiral product in $\mathcal{A}_2$.

Compute:
\begin{align*}
d_!^2(\phi_i^*) &= d_!\left(-\sum_{j,k,m} C_{ij}^{k,m} \phi_j^* \boxtimes \phi_k^*\right) \\
&= -\sum_{j,k,m} C_{ij}^{k,m} [d_!(\phi_j^*) \boxtimes \phi_k^* + \phi_j^* \boxtimes d_!(\phi_k^*)] \\
&= -\sum_{j,k,m} C_{ij}^{k,m} \left[\left(-\sum_{\ell,p} C_{j\ell}^{p,n} \phi_\ell^* \boxtimes \phi_p^*\right) \boxtimes \phi_k^* + \phi_j^* \boxtimes \left(-\sum_{q,r} C_{kq}^{r,s} \phi_q^* \boxtimes \phi_r^*\right)\right] \\
&= \sum_{j,k,\ell,m,n,p} C_{ij}^{k,m} C_{j\ell}^{p,n} \,(\phi_\ell^* \boxtimes \phi_p^* \boxtimes \phi_k^*) + \sum_{j,k,q,m,r,s} C_{ij}^{k,m} C_{kq}^{r,s} \,(\phi_j^* \boxtimes \phi_q^* \boxtimes \phi_r^*)
\end{align*}

For this to vanish, the coefficient of each $\phi_\alpha^* \boxtimes \phi_\beta^* \boxtimes \phi_\gamma^*$ must be zero:
\[\sum_{j,m,n} C_{ij}^{\gamma,m} C_{j\alpha}^{\beta,n} + \sum_{k,m,s} C_{i\alpha}^{k,m} C_{k\beta}^{\gamma,s} = 0 \qquad \forall\, i, \alpha, \beta, \gamma\]


thinking
**Inspecting mathematical definitions**

I need to inspect theorem/reference `thm:bar-cobar-isomorphism-main`, especially since the base case or structural reason might be misnamed. My primary question here is about falsifying the proof of Theorem B, so I'll have to analyze it step by step. Additionally, I should look into the definition of the Koszul locus `def:koszul-locus` and see if it’s correctly used in the introduction and theorem. I'll do a search to gather more information.
exec
/bin/zsh -lc "rg -n \"label\\{def:koszul-locus\\}|Koszul locus\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/frame/preface.tex chapters/frame/heisenberg_frame.tex chapters/theory/algebraic_foundations.tex chapters/theory/chiral_koszul_pairs.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/preface.tex:100:$\Omega(\barB(\cA))\xrightarrow{\sim}\cA$ on the Koszul locus.
chapters/frame/preface.tex:457:inverting the bar on the Koszul locus:
chapters/frame/preface.tex:476:That its cohomology recovers~$\cA^!$ on the Koszul locus is the
chapters/frame/preface.tex:495:functor $\Omega$ form an adjoint pair. On the Koszul locus
chapters/frame/preface.tex:509:Off the Koszul locus the inversion fails, and the failure is
chapters/frame/preface.tex:1215:complete invariant on the Koszul locus; no information is lost
chapters/frame/preface.tex:1259:bar-cobar-invertible on the Koszul locus (B), decomposes the
chapters/frame/preface.tex:2148:On the Koszul locus, the tree-level complex carries a contracting
chapters/frame/preface.tex:3450:an unrelated invariant. On the Koszul locus,
chapters/frame/preface.tex:3628:on the Koszul locus; the remaining comparisons are open.
chapters/frame/heisenberg_frame.tex:1332:equivalence on the Koszul locus
chapters/frame/heisenberg_frame.tex:1344:\cA$ holding on the Koszul locus. The PBW spectral sequence
chapters/frame/heisenberg_frame.tex:4546:\item Bar-cobar inversion on the Koszul locus
chapters/frame/heisenberg_frame.tex:4584:on the Koszul locus the counit is a quasi-isomorphism; off
chapters/frame/heisenberg_frame.tex:4612: \emph{Inversion on the Koszul locus, coderived persistence off it.}
chapters/frame/heisenberg_frame.tex:4613: The bar-cobar quasi-isomorphism holds on the Koszul locus at
chapters/theory/algebraic_foundations.tex:57:On the Koszul locus, $H^*(\barB(A))$ is concentrated in bar
chapters/theory/algebraic_foundations.tex:73:The bar-cobar adjunction, its inversion on the Koszul locus,
chapters/theory/algebraic_foundations.tex:88:On the Koszul locus (a homological acyclicity condition on the bar
chapters/theory/algebraic_foundations.tex:236:\begin{definition}[Koszul locus]\label{def:koszul-locus}
exec
/bin/zsh -lc "sed -n '220,310p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '680,725p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1210,1265p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{enumerate}
\end{definition}

\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
\index{Koszul chiral algebra|textbf}
Let $X$ be a smooth projective curve over~$\CC$.
An augmented chiral algebra~$\cA$
(Definition~\ref{def:chiral-algebra}) is \emph{Koszul}
if the bar-cobar counit
\[
\varepsilon \colon
\Omega_X(\barB_X(\cA)) \;\xrightarrow{\;\sim\;}\; \cA
\]
is a quasi-isomorphism at genus~$0$.
\end{definition}

\begin{definition}[Koszul locus]\label{def:koszul-locus}
\index{Koszul locus|textbf}
The \emph{Koszul locus} is the full subcategory
\[
 succeeded in 51ms:

The chiral analogues of Positselski's coalgebra homological
algebra~\cite{Positselski11} replace the ground field~$k$ by
$\mathcal{D}_X$ and the tensor product by $\chirtensor$; all
exactness properties are inherited from configuration space geometry.

\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
\label{rem:coderived-status}%
\index{coderived category!status}%
The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
$\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
and ordinary derived categories coincide.

At genus $g \geq 1$, the situation changes: the curvature
$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$ is nonzero for every algebra
with $\kappa(\cA) \neq 0$. This curvature is \emph{not a failure of
Koszulness}: a Koszul algebra has uncurved genus-$0$ bar
 succeeded in 52ms:
\medskip

\noindent\textbf{Theorem~B} (bar-cobar inversion). On the Koszul
locus, the cobar of the bar recovers the original algebra:
$\Omega(\barB(\cA))\xrightarrow{\sim}\cA$. The bar complex is a
complete invariant on the Koszul locus; no information is lost
there.
\medskip

\noindent\textbf{Theorem~C} (complementarity). The genus-$g$
cohomology of the center local system decomposes into two
Lagrangian halves, one controlled by~$\cA$ and the other by the
Koszul dual~$\cA^!$:
$R\Gamma(\overline{\cM}_g,\mathcal Z_\cA)
\simeq\mathbf Q_g(\cA)\oplus\mathbf Q_g(\cA^!)$.
\medskip

\noindent\textbf{Theorem~D} (modular characteristic).
For uniform-weight algebras at all genera, and unconditionally at
genus~$1$, the obstruction class factors as
exec
/bin/zsh -lc "sed -n '4575,4625p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the bar construction $\bar{B}(\cA)$ is the Koszul dual
coalgebra, a dg factorization coalgebra on $\mathrm{Ran}(X)$
intertwined with Verdier duality; the Koszul dual algebra
$\cA^!$ is obtained by Verdier duality, and the cobar of the
bar recovers $\cA$ itself
($\Omega(\bar{B}(\cA)) \xrightarrow{\sim} \cA$ on the Koszul
locus, not $\cA^!$).
\textbf{Theorem~B}
(Theorem~\ref{thm:higher-genus-inversion}):
on the Koszul locus the counit is a quasi-isomorphism; off
it, a curved quasi-isomorphism in the coderived category.
\textbf{Theorem~C}
(Theorem~\ref{thm:quantum-complementarity-main}):
for any Koszul pair $(\cA, \cA^!)$, deformation and
obstruction spaces embed as complementary Lagrangians in a
shifted-symplectic ambient space on
$\overline{\mathcal{M}}_g$.

\subsection{The modular Koszul package}


thinking
**Inspecting assumptions and findings**

I'm thinking about using `nl -ba` for my final output, but I want to make sure I have line references ready. It could be helpful to wrap my relevant findings with `nl -ba | sed -n`. First, I need to identify what those findings are. I should also inspect boundary lemmas and check any open-stratum dependencies to ensure I’m not missing any hidden assumptions. There’s a lot to consider!
exec
/bin/zsh -lc "rg -n \"label\\{def:chiral-koszul-pair\\}|label\\{def:chiral-koszul-morphism\\}|label\\{thm:koszul-equivalences-meta\\}|label\\{thm:pbw-koszulness-criterion\\}\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/algebraic_foundations.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:248:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
chapters/theory/chiral_koszul_pairs.tex:584:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:697:\label{thm:pbw-koszulness-criterion}
chapters/theory/chiral_koszul_pairs.tex:1965:\label{thm:koszul-equivalences-meta}
exec
/bin/zsh -lc "sed -n '236,335p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '568,635p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
coproduct. The MC equation $d\tau + \tau \star \tau = 0$ is
\emph{equivalent} to $(d_\cA + d_\cC + d_\tau^L)^2 = 0$
\textup{(}cf.\ \cite[Lemma~2.1.4]{LV12}\textup{)}: the twisting
morphism condition is the nilpotence of the twisted differential.
In the chiral setting, $\tau(c_{(1)})$ is the OPE extraction:
the coproduct $\Delta(c) = \sum c_{(1)} \otimes c_{(2)}$ separates
the coalgebra element, and $\tau$ evaluates $c_{(1)}$ against the
propagator on~$\overline{C}_2(X)$ by residue at the collision
divisor
\textup{(}Proposition~\textup{\ref{prop:twisting-morphism-propagator})}.
\end{remark}

\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
\index{Koszul morphism!chiral|textbf}
A chiral twisting datum $(\cA, \cC, \tau, F_\bullet)$ is
\emph{Koszul} if:
\begin{enumerate}
\item both $K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ are acyclic;
\item the associated graded
 $(\operatorname{gr}\cA, \operatorname{gr}\cC, \operatorname{gr}\tau)$
 succeeded in 50ms:
$\cA \otimes_\beta C$.

This is the chiral analogue of \textup{\cite[Theorem~2.4.1]{LV12}}.
The proof transfers directly: filter both sides by bar degree, observe
that $\mathrm{gr}(f)$ is an isomorphism (since $f$ is a quasi-isomorphism
of coalgebras), and conclude by spectral sequence comparison.
\end{theorem}

\subsection{The concept of chiral Koszul pairs: precise formulation}

To handle non-quadratic examples, we extend the notion of Koszul pairs
beyond the quadratic setting. The defining property is a set of
\emph{recognition criteria} (checkable conditions on the pair) from
which the full bar-cobar identification follows as a theorem.
No quasi-isomorphism statement is built into the definition itself.

\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
\index{Koszul pair!chiral|textbf}
A \emph{chiral Koszul pair} on a smooth projective curve~$X$
is a pair of chiral Koszul data
exec
/bin/zsh -lc "sed -n '1965,2060p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '688,750p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{sec:koszulness-verification}
\index{Koszul property!verification}
\index{PBW filtration!Koszulness verification}

A systematic method reduces
chiral Koszulness to classical Koszulness of the PBW-associated
graded via a flat deformation argument.

\begin{theorem}[PBW criterion for chiral Koszulness; \ClaimStatusProvedHere]
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
 succeeded in 51ms:
\label{thm:koszul-equivalences-meta}
\index{Koszul property!equivalences of characterizations|textbf}

Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
with PBW filtration $F_\bullet$.
Conditions \textup{(i)--(x)} below are equivalent.
Under the additional perfectness and non-degeneracy hypotheses on the
ambient tangent complex, condition~\textup{(xi)} is also equivalent to
them. Condition~\textup{(xii)} implies condition~\textup{(x)}
(Remark~\ref{rem:d-module-purity-content}); the converse is open.

\smallskip
\noindent\textbf{Unconditional equivalences:}
\begin{enumerate}
\item[\textup{(i)}] $\cA$ is chirally Koszul
 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
\item[\textup{(ii)}] The PBW spectral sequence on
 $\barBgeom(\cA)$ collapses at $E_2$
 \textup{(}Theorem~\textup{\ref{thm:pbw-koszulness-criterion})}.
\item[\textup{(iii)}] The minimal $A_\infty$-model of
exec
/bin/zsh -lc "rg -n \"label\\{conv:higher-genus-differentials\\}|d_fib\\"'^2|fiberwise differential|omega_g" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/bar_cobar_adjunction_inversion.tex -S' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:47:quadratic (strict $d^2=0$), curved-central ($\dfib^2 = \kappa\cdot\omega_g$
chapters/theory/bar_cobar_adjunction_inversion.tex:697:$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$ is nonzero for every algebra
chapters/theory/bar_cobar_adjunction_inversion.tex:1642: \[\psi_g: \Omega_g(\bar{B}_g(\mathcal{A})) \longrightarrow \mathcal{A}_g\]
chapters/theory/bar_cobar_adjunction_inversion.tex:2119: \[\psi_g: \Omega_g(\bar{B}_g(\mathcal{A})) \to \mathcal{A}_g\]
chapters/theory/bar_cobar_adjunction_inversion.tex:3616:curvature~$\kappa(\cA) \cdot \omega_g$), and strict commutativity
chapters/theory/bar_cobar_adjunction_inversion.tex:3703:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ at genus~$g \geq 1$ \\[2pt]
chapters/theory/bar_cobar_adjunction_inversion.tex:3879:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ \\[2pt]
chapters/theory/bar_cobar_adjunction_inversion.tex:3904:\item The \emph{curvature} of the fiberwise differential
chapters/theory/bar_cobar_adjunction_inversion.tex:3905:$\dfib^{\,2} = \kappa \cdot \omega_g$ is the infinitesimal generator
chapters/theory/bar_cobar_adjunction_inversion.tex:4244:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ governs the genus
chapters/theory/bar_cobar_adjunction_inversion.tex:5555:genus-$g$ bar curvature $\kappa(\cA) \cdot \omega_g$. The
chapters/theory/higher_genus_complementarity.tex:15:$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
chapters/theory/higher_genus_complementarity.tex:314:curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes
chapters/theory/higher_genus_complementarity.tex:387:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ vanishes (it lies
chapters/theory/higher_genus_complementarity.tex:2737:that $\dfib^{\,2} = \kappa \cdot \omega_g \in Z(\mathcal{A}) \otimes H^2(\overline{\mathcal{M}}_g)$;
chapters/theory/higher_genus_complementarity.tex:3360: $\dfib^{\,2} = \kappa\cdot\omega_g$ &
chapters/theory/higher_genus_complementarity.tex:3371:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$.
chapters/theory/higher_genus_complementarity.tex:3433:fiberwise differential $\dfib$ lives in the curved gauge.
chapters/theory/higher_genus_complementarity.tex:3450:d\tau_g + \tau_g \star \tau_g = \kappa(\cA) \cdot \omega_g.
chapters/theory/higher_genus_complementarity.tex:3452:The curvature $\kappa(\cA) \cdot \omega_g$ is the Arakelov

thinking
**Inspecting fiber curvature**

I need to take a closer look at lines 314 and 387, which might help clarify whether the fixed fiber curvature disappears. It's interesting how details in those specific lines can provide insights into the situation. I'm hopeful that this inspection will shed some light on the matter and help me understand the concept more clearly. Let's see what understanding emerges from analyzing those lines closely!
exec
/bin/zsh -lc "sed -n '300,405p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3440,3475p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9548,9575p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
\index{twisting morphism!curved|textbf}
\index{Maurer--Cartan equation!curved}
At genus~$0$, the universal twisting morphism
$\tau\colon \bar{B}(\cA) \to \cA$ satisfies the flat
Maurer--Cartan equation $d\tau + \tau \star \tau = 0$
(Corollary~\ref{cor:three-bijections},
Remark~\ref{rem:MC-is-Stokes}).
At genus~$g \geq 1$, the propagator acquires monodromy and the
twisting morphism becomes \emph{curved}:
\begin{equation}\label{eq:curved-MC-higher-genus}
d\tau_g + \tau_g \star \tau_g = \kappa(\cA) \cdot \omega_g.
\end{equation}
The curvature $\kappa(\cA) \cdot \omega_g$ is the Arakelov
$(1,1)$-form weighted by the modular characteristic
(Theorem~\ref{thm:quantum-arnold-relations}): it measures
the failure of the single-valued propagator to satisfy the
Arnold relation at genus~$g$.

The three propagators in the table of Step~4 above correspond
to three twisting morphisms: $\tau_0$ (classical, flat MC),
 succeeded in 51ms:
 H^2(\Defcyc(\cA), l_1) \otimes W_g
\]
is the cohomological class of the $d^2$-residual at genus~$g$.
Under the one-channel identification
$H^2(\Defcyc(\cA), l_1) \cong \mathbb{C}$
(Corollary~\ref{cor:one-dim-obstruction}), $o_g$ becomes a single
element of~$W_g$.

\medskip\noindent
\emph{Step~2: application of genus universality.}
The class $o_g \in W_g$ is the image of the fiberwise curvature
$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \mathrm{id}$
(the bar-degree-$2$ component of $d_{\mathrm{bar}}^2$). The
propagator defect $\omega_g$ on $\Sigma_g$ arises from the
$B$-cycle periods of the normalized differentials, and its class
in~$W_g$ is the tautological generator~$\lambda_g$ (via the
Hodge bundle interpretation:
$\omega_g = \tfrac{i}{2}\,(\operatorname{Im}\Omega)^{-1}_{\alpha\beta}\,\omega_\alpha\wedge\bar\omega_\beta$
with $\Omega$ the period matrix, giving
$[\omega_g] = c_g(\mathbb{E})$ after pushforward to
exec
/bin/zsh -lc "sed -n '2231,2315p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Functoriality of bar-cobar inversion; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-functorial}
% NOTE: removed duplicate label thm:cobar-functorial which conflated
% functoriality of the inversion qi with functoriality of the cobar functor.
The quasi-isomorphism $\psi: \Omega(\bar{B}(\mathcal{A})) \xrightarrow{\sim} \mathcal{A}$ 
is \emph{functorial}: for any morphism $f: \mathcal{A} \to \mathcal{A}'$ of 
chiral algebras, the diagram commutes:

\begin{center}
\begin{tikzcd}
\Omega(\bar{B}(\mathcal{A})) \ar[r, "\psi"] \ar[d, "\Omega(\bar{B}(f))"] 
& \mathcal{A} \ar[d, "f"] \\
\Omega(\bar{B}(\mathcal{A}')) \ar[r, "\psi'"] 
& \mathcal{A}'
\end{tikzcd}
\end{center}
\end{theorem}

\begin{proof}
This follows from the functoriality of the bar construction (Theorem~\ref{thm:bar-functorial}) and the universal property of the bar-cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}).


thinking
**Investigating the functoriality theorem**

I'm considering the functoriality theorem, which involves generic morphisms of chiral algebras. It doesn't seem to mention gluing or nodes, but I wonder if it could apply with restriction morphisms. The boundary lemma points to Proposition gluing-at-nodes and mentions boundary compatibility. I think I'll need to look into these to see if they truly demonstrate factorization into tensor products, and possibly the Künneth theorem. I'll search around line 3208 for more insights.
exec
/bin/zsh -lc "sed -n '3275,3335p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3335,3395p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3200,3275p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\emph{Pole-order separation.} The full OPE contains higher-order poles $(z_i - z_j)^{-m}$ for $m \geq 2$, but these contribute to the correction operators $d_k$ with $k \geq 2$ in the expansion $\Dg{g} = \dzero + \sum_k t_k d_k$, not to $\dzero$ or $d_1$. The relation $\dzero d_k + d_k \dzero = 0$ established above involves only the residue operator $\dzero$ and the period integral $d_k$; the simple-pole analysis suffices because $\dzero$ extracts first-order residues by definition (Definition~\ref{def:bar-differential-complete}).

\emph{Step 4: Quantum terms vanish; the Fay trisecant identity
is the higher-genus Borcherds identity.}

Three propagators control the bar differential at genus~$g$,
producing three chain-level models with different algebraic types
(Convention~\ref{conv:higher-genus-differentials}):
\begin{center}
\small
\begin{tabular}{lllll}
\textbf{Model} & \textbf{Propagator} & \textbf{Arnold 3-form} & \textbf{Differential} & \textbf{Category} \\[2pt]
Classical &
 $(z_i - z_j)^{-1}\,dz_i$ &
 $\mathcal{A}_3^{(0)} = 0$ &
 $\dzero^2 = 0$ &
 derived \\[2pt]
Corrected hol.\ &
 $\partial_{z_i}\!\log E(z_i,z_j)$ &
 $\mathcal{A}_3^{\mathrm{hol}} = 0$ &
 succeeded in 51ms:

(Note: $H^1(\mathcal{M}_g, \mathbb{Q}) = 0$ for $g \geq 2$ by Harer's theorem. The
parameters $t_i$ below arise from $H^1(\Sigma_g, \mathbb{C})$, the cohomology of the
\emph{curve}, not of the \emph{moduli space}.)

These enter the total corrected differential
(Convention~\ref{conv:higher-genus-differentials}) as:
\[\Dg{g} = \dzero + \sum_{i=1}^g t_i \cdot d_i\]
where $t_i$ are the period parameters arising from $H^1(\Sigma_g)$ and $d_i$ are the
genus-$g$ correction terms coming from period integrals.

\begin{definition}[Quantum-corrected differential]\label{def:quantum-differential}
At genus $g$, the total corrected differential on the Chevalley--Cousin
complex (Convention~\ref{conv:higher-genus-differentials}) receives corrections:
\[\Dg{g} = \dzero + \sum_{k=1}^{g} t_k \cdot d_k\]
where:
\begin{itemize}
\item $\dzero$ is the genus-zero (classical) differential from BD
\item $t_k = \oint_{A_k} \omega_k$ are the $A$-period parameters arising from the Hodge decomposition of $H^1(\Sigma_g, \mathbb{C})$
\item $d_k$ are correction operators encoding quantum effects via integration over the $A$-cycle $\gamma_k$
 succeeded in 50ms:
Parametrizes curves that split into two components of genera $g_1, g_2$.

\item \emph{Non-separating nodes:} $D_{\text{irr}}$
\[D_{\text{irr}} \simeq \overline{\mathcal{M}}_{g-1, n+2}\]
Parametrizes curves with a self-node (attaching handle).
\end{enumerate}
\end{definition}

\begin{proposition}[Gluing formula at nodes; \ClaimStatusProvedHere]\label{prop:gluing-at-nodes}
For a stable curve $C$ with a node $p$ splitting it into $C_1 \cup_p C_2$:
\[\mathcal{A}(C) \simeq \mathcal{A}(C_1) \otimes_{\mathcal{A}(p)} \mathcal{A}(C_2)\]
where the tensor product is over the fiber algebra $\mathcal{A}(p)$ at the node.
\end{proposition}

\begin{proof}
\emph{Step 1: Formal neighborhood of node.}

Near a node $p$, we have local analytic coordinates $(u,v)$ with $uv = t$ where $t \to 0$ as we approach the boundary. The two branches are:
\begin{align*}
C_1^{\text{loc}} &= \{(u, v) : v = 0, u \neq 0\} \cup \{p\} \\
exec
/bin/zsh -lc "rg -n \"label\\{conv:higher-genus-differentials\\}\" -n chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "higher-genus-differentials|Quantum-corrected differential|Convention.*higher-genus" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex -S' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:272:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/higher_genus_complementarity.tex:2735:This differential satisfies $\Dg{g}^{\,2} = 0$ (Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/higher_genus_complementarity.tex:3128:where $\pi \colon \mathcal{C}_g \to \mathcal{M}_g$ is the universal curve and $Z(\mathcal{A})$ is the center. (The parameters arise from $H^1(\Sigma_g, \C)$, not from $H^1(\mathcal{M}_g)$, which vanishes for $g \geq 2$ by Harer's theorem; see Convention~\ref{conv:higher-genus-differentials}.)
chapters/theory/higher_genus_complementarity.tex:3281:(Convention~\ref{conv:higher-genus-differentials}) as:
chapters/theory/higher_genus_complementarity.tex:3286:\begin{definition}[Quantum-corrected differential]\label{def:quantum-differential}
chapters/theory/higher_genus_complementarity.tex:3288:complex (Convention~\ref{conv:higher-genus-differentials}) receives corrections:
chapters/theory/higher_genus_complementarity.tex:3309:The total corrected differential $\Dg{g}$ \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}(ii))} satisfies $\Dg{g}^{\,2} = 0$.
chapters/theory/higher_genus_complementarity.tex:3342:(Convention~\ref{conv:higher-genus-differentials}):
chapters/theory/higher_genus_modular_koszul.tex:565:(Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/higher_genus_modular_koszul.tex:2580:Convention~\ref{conv:higher-genus-differentials}. Part~\textup{(ii)} is
chapters/theory/higher_genus_modular_koszul.tex:11617:(Convention~\ref{conv:higher-genus-differentials}(i))
exec
/bin/zsh -lc "sed -n '240,290p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc 'rg -n "conv:higher-genus-differentials" chapters -S' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:4869:(Convention~\ref{conv:higher-genus-differentials})
chapters/examples/free_fields.tex:4974:(Convention~\textup{\ref{conv:higher-genus-differentials}})
chapters/examples/kac_moody.tex:3697:$\dfib$ \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})} satisfies:
chapters/examples/kac_moody.tex:3747:At $k = -h^\vee = -2$, the curvature $\dfib^{\,2} = 0$ vanishes (Convention~\ref{conv:higher-genus-differentials}), so the genus-1 bar complex becomes a genuine differential graded coalgebra. This is consistent with the enhanced algebraic structure at critical level (Theorem~\ref{thm:sl2-critical}): the Feigin--Frenkel center provides extra flat sections, and the bar differential is strictly nilpotent.
chapters/examples/kac_moody.tex:3927:The quasi-modularity of $E_2$ (it transforms as $E_2(-1/\tau) = \tau^2 E_2(\tau) + 12\tau/(2\pi i)$) reflects the holomorphic anomaly: the genus-1 partition function is \emph{not} modular, and the failure of modularity is controlled by $(k+2) = k + h^\vee$, i.e., by the same curvature $\mcurv{1}$ that obstructs $\dfib^{\,2} = 0$ (Convention~\ref{conv:higher-genus-differentials}).
chapters/examples/kac_moody.tex:3964:$\dfib$ \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})} satisfies:
chapters/examples/genus_expansions.tex:1103:level~$h$ (since $\Dg{g}^{\,2} = 0$ on the total corrected bar complex, Convention~\ref{conv:higher-genus-differentials}).
chapters/connections/thqg_critical_string_dichotomy.tex:25:(Convention~\ref{conv:higher-genus-differentials})
chapters/connections/thqg_critical_string_dichotomy.tex:265:(Convention~\ref{conv:higher-genus-differentials}) is a
chapters/connections/thqg_open_closed_realization.tex:316:(Convention~\ref{conv:higher-genus-differentials}), and the
chapters/connections/editorial_constitution.tex:1889:Convention~\ref{conv:higher-genus-differentials}): the total bar complex is
chapters/connections/editorial_constitution.tex:1965:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/chiral_hochschild_koszul.tex:126:Convention~\ref{conv:higher-genus-differentials}), so the bar complex
chapters/theory/chiral_hochschild_koszul.tex:2863:(Convention~\ref{conv:higher-genus-differentials}(ii)), which
chapters/theory/chiral_hochschild_koszul.tex:3189: \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}(ii))}.
chapters/theory/chiral_hochschild_koszul.tex:3238:of Convention~\ref{conv:higher-genus-differentials}(ii):
chapters/theory/bar_construction.tex:72:Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
chapters/theory/higher_genus_complementarity.tex:272:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/higher_genus_complementarity.tex:2735:This differential satisfies $\Dg{g}^{\,2} = 0$ (Convention~\ref{conv:higher-genus-differentials}).
chapters/theory/higher_genus_complementarity.tex:3128:where $\pi \colon \mathcal{C}_g \to \mathcal{M}_g$ is the universal curve and $Z(\mathcal{A})$ is the center. (The parameters arise from $H^1(\Sigma_g, \C)$, not from $H^1(\mathcal{M}_g)$, which vanishes for $g \geq 2$ by Harer's theorem; see Convention~\ref{conv:higher-genus-differentials}.)
exec
/bin/zsh -lc "sed -n '229,285p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
\index{bar differential!higher-genus notation|textbf}
The Feynman transform differential
$d_{\mathrm{FT}} = d_{\mathrm{tree}} + d_{\mathrm{loop}}$
\textup{(}Proposition~\textup{\ref{prop:loop-filtration-compatible})} is
the single canonical differential on the genus-$g$ bar complex. For
computational purposes, three projections of this differential are
used throughout the manuscript.
\begin{enumerate}
\item[\textup{(i)}] \textbf{Fiberwise curved differential} $\dfib$.
 On a fixed curve $\Sigma_g$, the collision-residue differential built
 from the genus-$g$ propagator. This differential is \emph{curved}:
 \[
 \dfib^{\,2} = \kappa(\cA)\cdot\omega_g\cdot\mathrm{id},
 \]
 where $\omega_g$ is the Arakelov $(1,1)$-form
 (Theorem~\ref{thm:quantum-arnold-relations}) and
 $\kappa(\cA)$ is the leading OPE anomaly coefficient.
 At chain level, this equation is an operator identity on
 $\barB^{(g)}(\cA)|_{[\Sigma_g]}$: the endomorphism $\dfib^{\,2}$

thinking
**Evaluating spectral sequences**

I'm thinking about the bar-cobar spectral sequence and its application for Ω(B(A)), which uses an uncurved differential from the bar-cobar filtration. I wonder if this approach applies beyond the uncurved cases, particularly to curved or off-locus scenarios. I feel like I need to double-check the definitions, especially for strict complexes, because there might be some hidden assumptions I haven't considered yet. That's definitely worth exploring more!
exec
/bin/zsh -lc "sed -n '2000,2075p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '140,235p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Positselski~\cite[Corollary~4.4]{Positselski11}. In this
monograph, the genus-$0$ bar complex
$\bar{B}^{(0)}(\cA)$ is a conilpotent DG-coalgebra, so
the coderived category reduces to the ordinary derived
category; this is the content of
Remark~\textup{\ref{rem:exotic-vs-ordinary}}.
\end{proof}

\begin{remark}[Connection to bar-cobar duality]
\label{rem:coderived-bar-cobar}
\index{bar-cobar adjunction!coderived formulation}
In the setting of this monograph, the bar complex
$\bar{B}^{(g)}(\cA)$ is a chiral CDG-coalgebra with curvature
$m_0^{(g)} = \kappa(\cA) \cdot \omega_g$
(Convention~\ref{conv:higher-genus-differentials}).
At genus~$0$, $m_0^{(0)} = 0$ and
Theorem~\ref{thm:conilpotent-reduction} applies: the coderived
category is the ordinary derived category, and bar-cobar
inversion (Theorem~\ref{thm:higher-genus-inversion})
is a statement in $D(\bar{B}^{(0)}\text{-}\mathrm{comod})$.
 succeeded in 51ms:
\begin{enumerate}
\item $F^0 \supseteq F^1 \supseteq F^2 \supseteq \cdots$
\item $\bigcap_{p=0}^\infty F^p = 0$ (completeness)
\item The differential respects filtration: $d(F^p) \subseteq F^p$
\item The natural map factors through the filtration
\end{enumerate}
\end{definition}

\begin{lemma}[Associated graded; \ClaimStatusProvedHere]\label{lem:bar-cobar-associated-graded}
The associated graded of the bar-cobar filtration is:
\[\text{Gr}^p\Omega(\bar{B}(\mathcal{A})) = \Omega^p(\bar{B}^p(\mathcal{A}))\]

The induced differential on $\text{Gr}^\bullet$ is the \emph{bar complex differential} $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ (i.e., the full differential on $\bar{B}(\mathcal{A})$, lifted to each cobar tensor factor).
\end{lemma}

\begin{proof}
By definition of associated graded:
\[\text{Gr}^p = F^p / F^{p+1} = \Omega^p(\bar{B}^p(\mathcal{A}))\]

The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).



thinking
**Analyzing tensor properties**

I’m thinking about how if A(p) isn't flat or not a field, tensoring over A(p) might not preserve quasi-isomorphisms. This feels like a critical issue! I need to verify specific lines later, especially since it could affect my induction step for the boundary quasi-isomorphism proof, which incorrectly uses Künneth. I wonder if the gluing-at-nodes proposition is already questionable because A(C) for factorization algebra should factor over a point by tensoring over the ground field.
thinking
**Evaluating theorem dependencies**

I'm considering a potential issue with the proof of theorem `bar-cobar-inversion-qi`. It claims that the genus-0 base case is proved using theorem bar-nilpotency-complete and chiral-koszul-duality. However, I need to determine if chiral-koszul-duality actually provides a quasi-isomorphism that the proof relies on. The way it computes the dual coalgebra may not sufficiently imply the necessary components for the proof. I'm noticing that the connections could be more complex than stated, and there may even be a missing dependency.
thinking
**Assessing logical precision**

Hmm, I notice that the first sentence is not quite clear. The theorem `bar-cobar-inversion-qi` can still be valid even if the fundamental theorem is sufficient. I’m thinking this might be more of a medium or low-level issue, rather than a critical one. It seems important to clarify these aspects for accuracy, but it doesn't appear to undermine the theorem itself significantly. I'll keep that in mind as I refine my understanding.
exec
/bin/zsh -lc "sed -n '2925,2975p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{Step 1: Individual Nilpotency.} On any chiral algebra, the bar differential satisfies $d_{\text{bar}}^2 = 0$ by Theorem~\ref{thm:bar-nilpotency-complete}.

\emph{Step 2: BRST Coupling.} The total BRST differential $d_{\text{BRST}} = d_{\text{matter}} + d_{\text{ghost}} + d_{\text{coupling}}$ includes a coupling term from the matter-ghost interaction. The cross-terms yield:
\[d_{\text{BRST}}^2 = \frac{c_{\text{matter}} + c_{\text{ghost}}}{24} \cdot \chi(\overline{C}_n(X))\]
where $\chi$ is the Euler characteristic.

\emph{Step 3: Cancellation.} The anomaly vanishes precisely when $c_{\text{matter}} + c_{\text{ghost}} = 0$. Since $c_{\text{ghost}} = -26$ (bosonic) or $c_{\text{ghost}} = -15$ (superstring), this forces $c_{\text{matter}} = 26$ or $c_{\text{matter}} = 15$ respectively.
\end{remark}

\begin{remark}
The geometric bar complex connects BRST cohomology (string theory), OPEs as residues on configuration spaces (conformal field theory), geometric constraints on the central charge (anomaly cancellation), and compatibility with genus-one geometry (modular invariance).
\end{remark}

\section{Relationship between bar-cobar and Koszul duality}

For a chiral Koszul pair $(\cA_1, \cA_2)$, the bar of one is the
Koszul dual coalgebra of the other, and Verdier duality on
$\operatorname{Ran}(X)$ provides the equivalence. The Koszul
property (diagonal Ext vanishing in the (bar degree, weight)
bigrading) is the condition under which this equivalence descends
codex
I’ve isolated one substantive logical seam already: the boundary induction is routing through a node-gluing formula over `\mathcal A(p)` but then uses ordinary Künneth as if the tensor were over the ground field. I’m checking the family-specific PBW theorems now to see whether the theorem statement’s “standard landscape” language respects their actual boundary exclusions.
exec
/bin/zsh -lc "sed -n '1588,1665p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1188,1238p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1438,1495p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '740,800p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The differential includes the elliptic propagator:
\[
d^{(1)}\alpha = \text{Res}_{D_{12}}\left[\frac{\theta_1'(0)}{\theta_1(z_{12})} \cdot f \cdot \eta_{12}^{(1)}\right]
\]

The theta function zeros contribute additional cohomology classes corresponding to the $2^{2g}$ spin structures.

\emph{Degree~2.} The central extension appears from the modular anomaly:
\[
\hat{c} = \frac{c - \tilde{c}}{24}\omega_{\mathcal{M}_1}
\]
where $\omega_{\mathcal{M}_1}$ is the Kähler form on the moduli space of elliptic curves.
\end{proof}

\subsubsection{Heisenberg algebra on higher genus}

\begin{theorem}[Higher genus Heisenberg; \ClaimStatusProvedHere]\label{thm:heisenberg-higher-genus}
For $\mathcal{H}_k$ on $\Sigma_g$ ($g \geq 1$), the geometric bar complex cohomology is:
\[
 succeeded in 51ms:
Theorem~\ref{thm:verdier-bar-cobar}.
MK3 (modular Koszulity at $g = 1$):
Theorem~\ref{thm:pbw-genus1-km}.
MK4 and MK5 follow from MK1--MK3 by
Theorems~\ref{thm:higher-genus-inversion}
and~\ref{thm:quantum-complementarity-main}.
\end{proof}

\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
\label{thm:pbw-allgenera-km}
\index{PBW spectral sequence!all-genera degeneration|textbf}
\index{modular Koszul chiral algebra!unconditional all genera}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

This theorem does not use Theorem~\ref{thm:pbw-universal-semisimple}
\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
mechanism, and the absence of later differentials/extensions is supplied by the
family-specific argument below.
 succeeded in 51ms:
Item~(i) is MK4 applied to~$\widehat{\fg}_k$;
item~(ii) is MK5;
item~(iii) follows from~(i) and the
scalar characteristic
(Theorem~\ref{thm:modular-characteristic}).
\end{proof}

\begin{theorem}[PBW degeneration at all genera for Virasoro; \ClaimStatusProvedHere]
\label{thm:pbw-allgenera-virasoro}
\index{PBW spectral sequence!all-genera degeneration for Virasoro|textbf}
\index{Virasoro algebra!modular Koszulity|textbf}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

This theorem uses Theorem~\ref{thm:pbw-universal-semisimple} only to eliminate
the explicit genus-enrichment block. The absence of later differentials/extensions
is supplied by the family-specific argument below.

For any genus~$g \geq 1$ and generic central charge~$c$, the PBW
spectral sequence for the genus-$g$ bar complex
 succeeded in 51ms:
\item affine Kac--Moody algebras $\widehat{\mathfrak{g}}_k$ at generic
 level \textup{(}$k \notin \mathbb{Q}_{< 0}$ minus finitely many
 points\textup{)}, \emph{now unconditional by
 Theorem~\textup{\ref{thm:pbw-allgenera-km}};}
\item the Virasoro algebra $\mathrm{Vir}_c$ at generic central charge
 $c$, \emph{now unconditional by
 Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}};}
\item principal finite-type $\mathcal{W}$-algebras
 $\mathcal{W}^k(\mathfrak{g}, f_{\mathrm{prin}})$ at generic level,
 in particular higher $\mathcal{W}_N$
 , \emph{now unconditional by
 Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}.}
\end{enumerate}
\end{proposition}

\begin{proof}
The Kac--Moody and Virasoro statements are exactly
Theorems~\ref{thm:pbw-allgenera-km}
and~\ref{thm:pbw-allgenera-virasoro}.






thinking
**Evaluating Heisenberg's theorem**

I’m thinking about the Heisenberg higher genus theorem, which feels a bit complex. It doesn't directly relate to Theorem B, though there's some mention of it in open-stratum lemma. I wonder if the standard landscape covered by PBW all genera includes Heisenberg. Theorem B aims to generalize Heisenberg inversion for all Koszul chiral algebras, primarily focusing on genus zero. I think I need to further inspect if `thm:heisenberg-higher-genus` proves MK3, considering its implications on the cohomology.
thinking
**Analyzing the cohomology focus**

I’m considering whether explicit cohomology can demonstrate concentration. It seems that H^1 has a dimension of 2g, while H^2 presents as C⊕C⋅c_k^g, which might not be concentrated on the diagonal. I’m unsure about the meaning of the E∞ page. It looks like Heisenberg isn’t necessarily included in the higher genus inversion assumption, as the modular pre-Koszul includes MK1. I ought to inspect Theorem B and its claims against actual conditions, especially regarding the Koszul locus and missing modular hypotheses.
thinking
**Exploring mathematical concepts**

I’m considering whether genus-0 Koszulity from a chiral Koszul pair, along with the fundamental theorem on a fixed curve, could work if the chiral twisting datum is filtered-complete. It’s interesting because the theorem's regime tag indicates quadratic relations, but the text doesn’t explicitly limit it to just those. Maybe I can still accept a broader application. There are definitely some nuances to explore in this theorem!
thinking
**Clarifying theorems**

I'm thinking about the higher-genus theorem and its implications. In part (b), there's a specific clause I need to address. A potential issue arises with part (a) of the higher-genus-inversion theorem, which states that the spectral sequence collapses at E2. I need to unpack what that means and how it affects the overall understanding of this theorem. It’s essential to ensure I accurately interpret these aspects for a clear explanation.
thinking
**Inspecting the theorem and proposition**

I need to take a closer look at part (b) of the higher-genus-inversion theorem and the proposition regarding coderived adequacy, especially considering any potential circularity involved. It's important to ensure these concepts are thoroughly understood and that I’m not missing any critical aspects. Diving into the details could help clarify how these elements interact and avoid any misconceptions surrounding them. Let's uncover what exactly needs to be scrutinized here!
codex
I have enough surface to pin exact discrepancies. I’m re-reading the suspect blocks with line numbers now so the final report keeps only findings that survive direct textual verification.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4010,4155p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '180,275p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '229,270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '357,400p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4010	\begin{lemma}[Open-stratum quasi-isomorphism; \ClaimStatusProvedHere]\label{lem:higher-genus-open-stratum-qi}
  4011	Let $U_g \subset \overline{\mathcal{M}}_g$ be the open stratum of smooth genus-$g$
  4012	curves. The restriction
  4013	\[j_g^*\psi_g: j_g^*\Omega_g(\bar{B}_g(\mathcal{A})) \longrightarrow j_g^*\mathcal{A}_g\]
  4014	is a quasi-isomorphism.
  4015	\end{lemma}
  4016	
  4017	\begin{proof}
  4018	Fix a geometric point $s \in U_g$, corresponding to a smooth
  4019	genus-$g$ curve~$X_s$. The fiber of $j_g^*\psi_g$ at~$s$ is
  4020	the bar-cobar counit
  4021	$\psi_s\colon \Omega(\bar{B}(\cA|_{X_s})) \to \cA|_{X_s}$
  4022	on the \emph{fixed} curve~$X_s$.
  4023	By axiom~\ref{MK:modular}
  4024	(Definition~\ref{def:modular-koszul-chiral}), the PBW spectral
  4025	sequence of $(\bar{B}^{(g)}(\cA), \dfib)$ has concentrated
  4026	$E_\infty$ page at genus~$g$. This concentration is verified
  4027	independently of bar-cobar inversion: for Heisenberg by
  4028	Theorem~\ref{thm:heisenberg-higher-genus}, for affine
  4029	Kac--Moody by Theorem~\ref{thm:pbw-allgenera-km}, for Virasoro
 succeeded in 50ms:
   180	\label{sec:coderived-models}
   181	\index{coderived category!relative models|textbf}
   182	
   183	The full theory of coderived categories of factorization algebras
   184	on $\operatorname{Ran}(X)$ is not yet available in the literature;
   185	its development is part of the Stratum~II programme
   186	(Remark~\ref{rem:two-strata}). Nevertheless, the off-Koszul
   187	statements in this monograph (where the bar-cobar counit is
   188	a curved equivalence rather than a quasi-isomorphism) require
   189	a precise ambient homotopy category. This subsection defines the
   190	\emph{minimal} relative homotopy theory needed to make those
   191	statements mathematically honest.
   192	
   193	\begin{definition}[Filtered curved factorization model]
   194	\label{def:filtered-curved-model}
   195	A \emph{filtered curved factorization model} is a triple
   196	$(M, d, \mathcal{F})$ where:
   197	\begin{enumerate}[label=\textup{(\roman*)}]
   198	\item $M$ is a conilpotent factorization coalgebra on $\operatorname{Ran}(X)$
   199	 (or a dg module over such);
 succeeded in 51ms:
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
 succeeded in 51ms:
   357	\label{thm:fundamental-twisting-morphisms}
   358	\index{twisting morphism!fundamental theorem|textbf}
   359	\textup{[Regime: quadratic
   360	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   361	
   362	\smallskip\noindent
   363	This is the chiral analogue of \cite[Theorem~2.3.1]{LV12}.
   364	For a chiral twisting datum
   365	$(\cA, \cC, \tau, F_\bullet)$
   366	\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum})},
   367	the following are equivalent:
   368	\begin{enumerate}[label=\textup{(\roman*)}]
   369	\item\label{ftm:koszul}
   370	 $\tau$ is a chiral Koszul morphism
   371	 \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
   372	\item\label{ftm:counit}
   373	 The canonical counit
   374	 $\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$
   375	 is a quasi-isomorphism.
   376	\item\label{ftm:unit}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3208,3258p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1960,2085p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/algebraic_foundations.tex | sed -n '223,275p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3208	\begin{proposition}[Gluing formula at nodes; \ClaimStatusProvedHere]\label{prop:gluing-at-nodes}
  3209	For a stable curve $C$ with a node $p$ splitting it into $C_1 \cup_p C_2$:
  3210	\[\mathcal{A}(C) \simeq \mathcal{A}(C_1) \otimes_{\mathcal{A}(p)} \mathcal{A}(C_2)\]
  3211	where the tensor product is over the fiber algebra $\mathcal{A}(p)$ at the node.
  3212	\end{proposition}
  3213	
  3214	\begin{proof}
  3215	\emph{Step 1: Formal neighborhood of node.}
  3216	
  3217	Near a node $p$, we have local analytic coordinates $(u,v)$ with $uv = t$ where $t \to 0$ as we approach the boundary. The two branches are:
  3218	\begin{align*}
  3219	C_1^{\text{loc}} &= \{(u, v) : v = 0, u \neq 0\} \cup \{p\} \\
  3220	C_2^{\text{loc}} &= \{(u, v) : u = 0, v \neq 0\} \cup \{p\}
  3221	\end{align*}
  3222	
  3223	\emph{Step 2: Chiral algebra factorizes.}
  3224	
  3225	For disjoint opens $U_1 \subset C_1$, $U_2 \subset C_2$ with $U_1 \cap U_2 = \emptyset$:
  3226	\[\mathcal{A}(U_1 \sqcup U_2) = \mathcal{A}(U_1) \otimes \mathcal{A}(U_2)\]
  3227	by the factorization axiom.
exec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '34,44p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1960	\index{derived Morita equivalence!bar coalgebra characterization}
  1961	\index{Koszul conductor!Morita obstruction}
  1962	Theorem~\ref{thm:bar-cobar-inversion-qi} converts the bar coalgebra
  1963	into a complete derived invariant: two Koszul chiral algebras
  1964	$\cA$, $\cB$ are derived Morita equivalent (quasi-isomorphic as
  1965	objects of the bar-cobar localization) if and only if their bar
  1966	coalgebras $\bar{B}^{\mathrm{ch}}(\cA)$ and
  1967	$\bar{B}^{\mathrm{ch}}(\cB)$ are quasi-isomorphic as dg~coalgebras.
  1968	The Koszul conductor $K(\cA) = \kappa(\cA) + \kappa(\cA^!)$
  1969	(\S\ref{sec:complementarity}) controls the rigidity of this
  1970	identification.
  1971	
  1972	When $K = 0$ (affine Kac--Moody at non-critical level, Heisenberg,
  1973	free fields), the complementarity $\kappa(\cA^!) = -\kappa(\cA)$
  1974	permits non-trivial bar-coalgebra identifications
  1975	$\bar{B}^{\mathrm{ch}}(\cA) \simeq \bar{B}^{\mathrm{ch}}(\cB)$
  1976	with $\cA \not\simeq \cB$ as chiral algebras; level-rank duality
  1977	provides the prototype.
  1978	When $K \neq 0$ (Virasoro with $K = 13$, Bershadsky--Polyakov with
  1979	$K = 196$), a quasi-isomorphism of bar coalgebras forces
 succeeded in 52ms:
   223	\begin{definition}[Koszul chiral algebra]\label{def:koszul-chiral-algebra}
   224	\index{Koszul chiral algebra|textbf}
   225	Let $X$ be a smooth projective curve over~$\CC$.
   226	An augmented chiral algebra~$\cA$
   227	(Definition~\ref{def:chiral-algebra}) is \emph{Koszul}
   228	if the bar-cobar counit
   229	\[
   230	\varepsilon \colon
   231	\Omega_X(\barB_X(\cA)) \;\xrightarrow{\;\sim\;}\; \cA
   232	\]
   233	is a quasi-isomorphism at genus~$0$.
   234	\end{definition}
   235	
   236	\begin{definition}[Koszul locus]\label{def:koszul-locus}
   237	\index{Koszul locus|textbf}
   238	The \emph{Koszul locus} is the full subcategory
   239	\[
   240	\operatorname{Kosz}(X)
   241	\;\subset\;
   242	\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
 succeeded in 51ms:
    34	 not coalgebra). &
    35	 Thm~\ref{thm:bar-cobar-isomorphism-main} \\[4pt]
    36	
    37	\textbf{Theorem B} &
    38	 Bar--cobar inversion: on the Koszul locus, the counit
    39	 $\Omega_X \bar{B}_X(\cA) \xrightarrow{\sim} \cA$ is a
    40	 quasi-isomorphism at all genera. &
    41	 Thm~\ref{thm:higher-genus-inversion} \\[4pt]
    42	
    43	\textbf{Theorem C} &
    44	 Complementarity: $Q_g(\cA) \oplus Q_g(\cA^!)
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1210,1218p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '4580,4615p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '535,660p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  4580	($\Omega(\bar{B}(\cA)) \xrightarrow{\sim} \cA$ on the Koszul
  4581	locus, not $\cA^!$).
  4582	\textbf{Theorem~B}
  4583	(Theorem~\ref{thm:higher-genus-inversion}):
  4584	on the Koszul locus the counit is a quasi-isomorphism; off
  4585	it, a curved quasi-isomorphism in the coderived category.
  4586	\textbf{Theorem~C}
  4587	(Theorem~\ref{thm:quantum-complementarity-main}):
  4588	for any Koszul pair $(\cA, \cA^!)$, deformation and
  4589	obstruction spaces embed as complementary Lagrangians in a
  4590	shifted-symplectic ambient space on
  4591	$\overline{\mathcal{M}}_g$.
  4592	
  4593	\subsection{The modular Koszul package}
  4594	
  4595	The Heisenberg already contains the modular story: curvature at
  4596	genus~$1$, the $\hat{A}$-genus generating function, and
  4597	complementarity are all visible by direct calculation. The general
  4598	theorems do not \emph{add} modular structure to the genus-$0$ engine;
  4599	they \emph{unfold} what was already present in the bar complex's
 succeeded in 51ms:
  1210	\medskip
  1211	
  1212	\noindent\textbf{Theorem~B} (bar-cobar inversion). On the Koszul
  1213	locus, the cobar of the bar recovers the original algebra:
  1214	$\Omega(\barB(\cA))\xrightarrow{\sim}\cA$. The bar complex is a
  1215	complete invariant on the Koszul locus; no information is lost
  1216	there.
  1217	\medskip
  1218	
 succeeded in 52ms:
   535	 Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
   536	Let $X$ be a smooth projective curve over $\mathbb{C}$.
   537	A \emph{modular pre-Koszul chiral algebra} on $X$ is an augmented chiral
   538	algebra $(\cA, \varepsilon\colon \cA \to \mathcal{O}_X)$ equipped with
   539	the following data and satisfying the following axioms.
   540	
   541	\smallskip\noindent\textbf{Data.}
   542	\begin{enumerate}[label=\textup{(D\arabic*)}]
   543	\item\label{D:bar}
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
   554	\emph{consequence} of Theorem~\ref{thm:bar-cobar-isomorphism-main},

thinking
**Exploring theorem proof**

I need to look into the theorem related to higher-genus inversion, particularly focusing on the proof beyond line 4155 to ensure it includes the entirety of section, excluding part b. It's essential to gather the relevant lines to understand everything thoroughly. Let’s explore this together and ensure I capture all necessary details for clarity and completeness!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4150,4218p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4150	Fix $g>0$ and assume the claim for all genera $<g$. Set
  4151	$X=\overline{\mathcal{M}}_g$, with $j:U_g\hookrightarrow X$ and
  4152	$i:\partial X\hookrightarrow X$.
  4153	\begin{enumerate}[label=(\arabic*)]
  4154	\item By Lemma~\ref{lem:higher-genus-open-stratum-qi}, $j^*\psi_g$ is a
  4155	quasi-isomorphism.
  4156	\item By Lemma~\ref{lem:higher-genus-boundary-qi} and the induction hypothesis
  4157	on the lower-genus vertices of each stable graph $\Gamma$ indexing a boundary
  4158	stratum $D_\Gamma$, $\psi_g|_{D_\Gamma}$ is a quasi-isomorphism for every
  4159	$D_\Gamma$. The passage from ``quasi-isomorphism on each~$D_\Gamma$''
  4160	to ``quasi-isomorphism on all of~$\partial\overline{\mathcal{M}}_g$''
  4161	follows by a Mayer--Vietoris argument on the normal crossing boundary:
  4162	the boundary strata form a simple normal crossing divisor, so the
  4163	cone of~$i^*\psi_g$ is computed by iterated extensions along the
  4164	pairwise intersections $D_\Gamma \cap D_{\Gamma'}$, each of which
  4165	is a deeper boundary stratum where the same inductive hypothesis
  4166	applies. Hence $i^*\psi_g$ is a quasi-isomorphism.
  4167	\item Apply Lemma~\ref{lem:extension-across-boundary-qi} to
  4168	$X=U_g\sqcup\partial X$ and $f=\psi_g$. Since $j^*f$ and $i^*f$ are
  4169	quasi-isomorphisms by (1)--(2), $f$ is a quasi-isomorphism.

thinking
**Considering theorem details**

I think I need to reference the standard landscape in the bar_cobar_adjunction_inversion theorem statement, but I'm not sure if it's really necessary. Maybe it's sufficient without it? Additionally, I should look for line numbers related to the theorem statement around 1604 and the D2 proof. Getting those line numbers might help clarify things and provide better context for the theorem. Let's see if I can track those down!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1604,1665p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1778,1890p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1604	\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
  1605	\textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
  1606	on the Koszul locus; filtered-complete off it
  1607	\textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
  1608	
  1609	The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
  1610	
  1611	Let $\mathcal{A}$ be a \emph{Koszul} chiral algebra on a Riemann surface $X$
  1612	(Definition~\ref{def:koszul-chiral-algebra};
  1613	equivalently, $\cA \in \operatorname{Kosz}(X)$;
  1614	this excludes simple admissible-level quotients and minimal-model
  1615	central charges; see Scope below), with
  1616	$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ conilpotent or $\mathcal{A}$ complete
  1617	with respect to its augmentation ideal
  1618	\textup{(}\S\ref{sec:i-adic-completion}\textup{)}. Then the genus-$0$
  1619	counit
  1620	\[
  1621	\psi_0: \Omega_0(\bar{B}_0(\mathcal{A})) \longrightarrow \mathcal{A}
  1622	\]
  1623	is a quasi-isomorphism of chiral algebras.
 succeeded in 51ms:
  1778	(Theorem~\ref{thm:bar-functorial}; functoriality of cobar is the formal dual).
  1779	
  1780	\item \emph{Genuswise quasi-isomorphism.}
  1781	The genus-$0$ base case is proved independently by
  1782	Theorem~\ref{thm:bar-nilpotency-complete} and
  1783	Theorem~\ref{thm:chiral-koszul-duality};
  1784	equivalently, it is the implication
  1785	\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
  1786	the fundamental theorem of chiral twisting morphisms
  1787	(Theorem~\ref{thm:fundamental-twisting-morphisms}).
  1788	Under axiom~\ref{MK:modular}, the genus-$g$ components $\psi_g$ for
  1789	$g \geq 1$ are quasi-isomorphisms by induction on genus via
  1790	Theorem~\ref{thm:genus-graded-convergence}, item~(2), together with the
  1791	higher-genus inversion package (Theorem~\ref{thm:higher-genus-inversion}).
  1792	
  1793	\item \emph{Full genus-graded convergence and quasi-isomorphism.}
  1794	Under the same higher-genus hypothesis, this is
  1795	Theorem~\ref{thm:genus-graded-convergence}, item~(3), which identifies
  1796	the completed genus series $\psi=\sum_{g\ge 0}\hbar^{2g-2}\psi_g$ and
  1797	proves convergence.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '689,730p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
   708	these classes \emph{control} the coderived category at each genus requires









thinking
**Inspecting prop adequacy**

I’m thinking about how the circular reference might be sufficient. I need to check if `heisenberg_frame` and `guide_to_main_results` utilize a coderived category rather than something provisional. That could be significant to mention! It's important to clarify these aspects before moving forward, just to ensure I'm on the right path. I'll have to look into this further and gather more insights. Let's see what I find!
thinking
**Considering the theorem details**

I’m pondering over the fundamental theorem related to twisting morphisms and their application to a "chiral twisting datum" with filtration. It seems to suggest that filtered-complete structures can be covered by this. The regime tag notes quadratic relationships, but the theorem's text doesn’t strictly require them. It states that for a chiral twisting datum, there are four equivalent conditions to consider. This line of reasoning is quite intriguing!
thinking
**Exploring Koszul morphism**

I'm delving into Koszul morphism and its relationships with associated graded quadratic/Koszul forms and strong filtration convergence. I see that there's an existing filtered theorem, suggesting applicability beyond strictly quadratic contexts. The theorem includes a notion of chiral twisting, which might imply broader use cases. I should closely examine the definition of chiral Koszul morphism and the context of the theorem, especially regarding its association with W-algebras and quadratic regimes. This definitely warrants more inspection!
thinking
**Analyzing chiral Koszul morphism**

I’m reviewing the definition of chiral Koszul morphism, which involves associated graded quadratic/Koszul forms and strong convergence. I wonder if the "quadratic" tag is misleading or possibly points to a quadratic locus. However, it could still encompass filtered data. I need to closely inspect how the fundamental theorem of twisting morphisms applies to chiral twisting data and whether it adequately addresses filtered contexts. The application to W-algebras seems plausible, but I should ensure my interpretations align with the theorem’s statements.
thinking
**Clarifying PBW Concentration**

To apply the PBW concentration, it seems like I need more than just concentration at genus-g; I might need twisting datum plus convergence. The modular pre-Koszul concept, along with a fixed curve, could help, but there might be a hidden assumption involved. This isn't as straightforward as I initially thought, so I should be careful not to frame it as a regime mismatch but rather as a differential comparison issue. I can focus on the differences between "\dfib" and strict counit to clarify my findings.
thinking
**Examining theorem components**

I'll focus on the theorem statement for part (a), which is specifically about the counit qi. It seems like inspecting `guide_to_main_results` might give us what we need without including the preface or the heisenberg_frame. If we mention the supporting references, that could be enough. It’s worth noting that we have the required lines, so it could simplify things. I'm keen to clarify this and ensure everything is properly referenced!
thinking
**Evaluating theorem details**

I'm looking at the theorem regarding off-locus persistence. It mentions the provisional coderived category, but I'm wondering if the first critical includes too much detail. It's okay if it does, but I need to make sure the proof at 4140-4172 doesn't treat part b. Should I provide an overall answer to the user’s subquestions after my findings? Maybe a summary line in prose would work, but the structured contract calls for an ending summary, so no extras there.
thinking
**Clarifying theorem aspects**

I’m delving into various descriptions that need addressing. For the Koszul locus definition, it’s not very clean and seems conclusion-based. The proof for qi is incomplete due to boundary induction issues. Regarding the model structure, it’s only provisional and has some circular reasoning. The off locus clause is mentioned but not proved, and I should note a "verdict FAIL" since I found 6 violations out of 17 instances. I need to keep everything straightforward, without nested bullets, and pay attention to the user’s severity categories for structured contracts.
thinking
**Formatting theorem references**

I can write raw file and line numbers within the description, and it’s fine to use markdown code in a plain format. I need to ensure that the first critical line, 4123, correctly introduces clause b. I'll also mention supporting lines 263-270 from coderived_models and 2024-2077 as well. There's a potential false positive regarding theorem part (a) with E2 collapse, and the theorem's proof misses a crucial point, which creates a discrepancy. The definition of the Koszul locus seems conclusion-based, so I might answer “No” to whether it’s correctly defined.
codex
[CRITICAL] chapters/theory/higher_genus_complementarity.tex:4123 — Clause `(b)` of `thm:higher-genus-inversion` is stated as theorematic, but the proof at `4140-4172` only proves the Koszul/modular-locus quasi-isomorphism in `(a)`. Its cited support is circular: `chapters/theory/coderived_models.tex:247-270` proves `prop:coderived-adequacy(a)` by invoking `thm:higher-genus-inversion` itself, and its off-locus argument reuses the strict spectral sequence of `chapters/theory/bar_cobar_adjunction_inversion.tex:2024-2077`, which is formulated for complexes with `d^2=0`, not for the curved off-locus setting.

[CRITICAL] chapters/theory/higher_genus_complementarity.tex:4077 — The boundary induction step silently replaces a tensor product over the nodal fiber algebra by an ordinary tensor product over the ground field. But the actual gluing statements at `chapters/theory/higher_genus_complementarity.tex:3208-3253` are over `\mathcal A(p)`, not over `\mathbb C`. Without flatness or Tor-vanishing at the node, Künneth does not justify preservation of quasi-isomorphisms, so the proof of `lem:higher-genus-boundary-qi` does not follow.

[HIGH] chapters/theory/higher_genus_complementarity.tex:4120 — Part `(a)` of `thm:higher-genus-inversion` claims the spectral sequence collapses at `E_2`, but the proof at `4140-4172` establishes only the quasi-isomorphism of `\psi_g`. The `E_2`-collapse is only proved later in `lem:e2-collapse-higher-genus` at `4205-4218`, so the theorem statement outruns the proof attached to it.

[HIGH] chapters/theory/higher_genus_complementarity.tex:4018 — The open-stratum proof does not pin down which genus-`g` complex is being inverted. The manuscript distinguishes the curved fiberwise differential `\dfib` with `\dfib^2=\kappa(\cA)\omega_g` on a fixed curve and the strict corrected differential `\Dg{g}` with `\Dg{g}^2=0` (`chapters/theory/higher_genus_foundations.tex:229-270`, `chapters/theory/higher_genus_modular_koszul.tex:557-572`). Yet `lem:higher-genus-open-stratum-qi` passes from PBW concentration for `(\bar B^{(g)}(\cA),\dfib)` to the strict bar-cobar counit on a fixed curve via `thm:fundamental-twisting-morphisms` (`chapters/theory/chiral_koszul_pairs.tex:357-375`) without supplying the comparison between the curved and strict models.

[MEDIUM] chapters/theory/algebraic_foundations.tex:223 — The primary definition of the Koszul locus is conclusion-based: `\cA` is “Koszul” iff the genus-0 counit `\Omega_X(\bar B_X(\cA))\to\cA` is already a quasi-isomorphism. Consequently the genus-0 clause of `thm:bar-cobar-inversion-qi` (`chapters/theory/bar_cobar_adjunction_inversion.tex:1611-1623`) is tautological on the live definition rather than a recognition theorem from independent hypotheses. The antecedent, non-tautological notion only appears later via chiral Koszul data/pairs.

[MEDIUM] chapters/frame/guide_to_main_results.tex:37 — The public theorem summaries inflate scope. `guide_to_main_results.tex:37-40` and `preface.tex:1212-1215` advertise all-genera inversion “on the Koszul locus”, while the actual theorem assumes a modular pre-Koszul datum `(MK1–MK3)`. `heisenberg_frame.tex:4583-4585` and `4611-4615` further summarize the off-locus result as living in “the coderived category”, but the theorem only names the provisional coderived category.

## Summary
Instances checked: 17 | Violations found: 6 | Verdict: FAIL
tokens used
173,058
