# T06_thm_D (558s, gpt-5.4)

- [CRITICAL] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2695) — Theorem D is not proved end-to-end as written. Its proof imports `thm:genus-universality`, but the load-bearing step there, [higher_genus_foundations.tex:5326](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5326), invokes `thm:family-index` to identify `\mathrm{obs}_g` with `\lambda_g`; the proof of `thm:family-index` then starts from `thm:genus-universality` at [concordance.tex:6010](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6010). This is a direct circular dependency on the main all-genera step.

- [HIGH] [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:5943) — Even ignoring the circularity, `thm:family-index` is ill-formed as a GRR argument. It defines `\mathcal D_\cA^{(g)} := \kappa(\cA)\cdot \mathbb E` inside `K_0(\overline{\mathcal M}_g)\otimes \mathbb Q`, although `\kappa(\cA)` is introduced as a complex scalar, and then concludes `c_g(\mathcal D_\cA^{(g)})=\kappa(\cA)c_g(\mathbb E)` at [concordance.tex:6020](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6020). That is not a valid K-theoretic/Chern-class operation.

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2650) — The scope note for multi-weight families is stale and now false on its own terms. It says the higher-genus extension is "conditional on the strong scalar ansatz of Theorem~`thm:multi-generator-universality`", but that label now points to the proved negative theorem [higher_genus_modular_koszul.tex:21681](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21681), which asserts `F_g=\kappa\lambda_g^{FP}+\delta F_g^{cross}` and gives explicit nonzero `\delta F_2(\mathcal W_3)`. The same stale wording also survives at [higher_genus_foundations.tex:5257](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5257).

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14172) — `thm:shadow-channel-decomposition` expands the Maurer-Cartan equation incorrectly: the linear term is written with `\kappa_i^2` instead of `\kappa_i`. Worse, even the corrected expansion would not show that arbitrary `\kappa_i\Theta_{\eta_i}` are Maurer-Cartan unless extra vanishing is proved. Since `thm:multi-weight-genus-expansion` uses this theorem in its diagonal reduction at [higher_genus_modular_koszul.tex:21796](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21796), the general multi-channel proof is not sound as written.

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21821) — `thm:multi-weight-genus-expansion` claims its uniform-weight clause needs no argument because it is `thm:algebraic-family-rigidity`, but that cited theorem explicitly stops short of identifying `\Gamma_\cA` with `\kappa(\cA)\Lambda`; see [higher_genus_modular_koszul.tex:8980](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:8980). So the advertised reason for `\delta F_g^{cross}=0` on the uniform-weight side does not actually prove the stated conclusion.

- [LOW] [compute/lib/multichannel_universality.py](/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:31) — Downstream propagation is not fully synchronized. The compute bookkeeping and tests still describe `thm:multi-generator-universality` as a conditional strong-scalar-ansatz surface; see also [test_multi_generator_universality.py:21](/Users/raeez/chiral-bar-cobar/compute/tests/test_multi_generator_universality.py:21). That no longer matches the proved negative theorem in the chapters.

Independent of those failures, two narrower points do survive this audit. Multi-weight really does need a correction in at least one concrete case: [w_algebras.tex:5741](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:5741) computes `\delta F_2(\mathcal W_3)=(c+204)/(16c)\neq 0`, so the scalar formula cannot hold uniformly off the uniform-weight lane. And `F_1=\kappa/24` does survive as a sanity check, via the genus-1 Faber-Pandharipande value at [higher_genus_foundations.tex:4552](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4552) and the `x^2` coefficient in [genus_expansions.tex:1919](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1919); it is a consistency check, not a substitute for the missing all-genera proof.

## Summary
Instances checked: 24 | Violations found: 6 | Verdict: FAIL


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
session id: 019d8388-33a9-7270-beff-82a4fb4eab35
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


MISSION: FALSIFY the proof of Theorem D: obs_g = kappa*lambda_g at uniform weight. Check: (a) is the formula correct? (b) what is the scope (genus, weight)? (c) is the proof complete? (d) does multi-weight really need delta_F_g^cross? (e) is F_1=kappa/24 a sanity check?

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.
mcp startup: no servers



thinking
**Planning the audit process**

I need to perform an audit that involves reading without making any modifications. First, I'll follow the repository instructions and review relevant files like CLAUDE.md, the concordance, theorem registry, and the red team summary. The user mentioned searching the chapters for theorems, and it seems like this task aligns closely with the deep-beilinson-audit. I might need to use skills like multi-path-verify too. It's clear I should provide updates and commentary throughout the process without changing any files.
thinking
**Organizing the audit task**

I need to ensure I follow the developer's instructions for updates every 30 seconds. In this environment, it’s likely I can only send a few commentary updates since there's no wall clock. I'll inspect the files to find Theorem D and its proof in the manuscript chapters. Cross-referencing for duplicates across volumes is essential. I should read the relevant files and possibly use skills like multi-path-verify for formula checks. I'll also look into sections of CLAUDE.md related to Theorem D and may spawn explorer agents for finding citations and theorems.
thinking
**Deciding on using explorer agents**

Since the instructions recommend using explorers over manual searches, I should consider spawning one or more explorer agents. I’ll need to conduct a detailed audit with specific file and line references. The explorer can help search for Theorem D, its proof, and cited lemmas. However, it’s likely I still need to read the actual lines myself. While the explorer is reliable, the user wants grounding in the file contents I read. I can use the explorer for quick location, then read the details directly.
codex
Using `deep-beilinson-audit` and `multi-path-verify`. I’m locating Theorem D, reading the concordance and registry surfaces first, then I’ll audit the full proof line by line against its cited dependencies and boundary cases.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg -n \"Theorem D|thm:.*D|obs_g\\\\s*=\\\\s*kappa\\\\s*\\\\*\\\\s*lambda_g|uniform weight|delta_F_g\\\\"'^cross|F_1'"\\\\s*=\\\\s*kappa/24|F_1\\\\s*=\\\\s*\\\\\\\\kappa/24|lambda_g\" chapters metadata CLAUDE.md | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,240p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,240p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:67:Every formula of the form `F_g = ... lambda_g ...` or `obs_g = ...` MUST be followed within the same sentence by ONE of:
CLAUDE.md:107:Downgrade atomicity: when downgrading theorem -> conjecture, rename `thm:foo -> conj:foo` AND update every `\ref{thm:foo}` across three volumes in the SAME tool-call batch. No intermediate commit.
CLAUDE.md:202:4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower).
CLAUDE.md:267:**C24. Cauchy integral normalization.** `[z^{n-1}] f(z) = (1/(2*pi*i)) * contour_integral f(z) dz/z^n`. Wrong: 1/(2*pi) (missing i gives zero for real integrands, AP120). Sanity: F_1 = kappa/24.
CLAUDE.md:329:- B26. `obs_g = \kappa * \lambda_g` untagged. CORRECT: append (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta F_g^cross). AP32.
CLAUDE.md:414:**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).
CLAUDE.md:440:**FM21. Dimensional analysis reconstruction with wrong prefactor.** Opus gets powers right but numerical prefactors (1/2, 1/24, 1/(2*pi*i), 7/5760) wrong. Counter: for any numerical coefficient in {F_g, lambda_g, Bernoulli numbers, Faber-Pandharipande values}, Read the canonical source file in compute/lib/ before writing.
CLAUDE.md:464:**FM26. False operad self-duality claim.** Opus claimed "(SC^{ch,top})^! ~ SC^{ch,top}" (Koszul self-dual) in thm:SC-self-duality, misciting Livernet [Liv06] (which proves Koszulity, not self-duality). The manuscript's OWN compute engine (sc_koszul_dual_cooperad_engine.py) computes SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!, manifestly different from SC = (Com, Ass) with closed dim = 1. The error: confusing "the duality FUNCTOR is an involution on SC-algebras" with "the OPERAD is self-dual." These are different: (P^!)^! ~ P (tautological for Koszul operads) does NOT mean P^! ~ P. Counter: before claiming any operad is self-dual, verify dim P(n) = dim P^!(n) at all degrees.
CLAUDE.md:489:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
CLAUDE.md:507:**pole/weight** (AP19, AP21, AP27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.
CLAUDE.md:531:AP32: Genus-1 != all-genera. obs_1=kappa*lambda_1 unconditional. Multi-weight g>=2: scalar formula FAILS. **Every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Untagged = violation.**
CLAUDE.md:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
CLAUDE.md:702:Trigger: any theorem statement, any obs_g / F_g / lambda_g formula, any universal quantifier.
CLAUDE.md:789:AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
CLAUDE.md:796:AP125: Label prefix MUST match environment. \begin{conjecture} uses conj:, \begin{theorem} uses thm:, \begin{proposition} uses prop:. When upgrading/downgrading, rename label AND update all \ref instances atomically. Stale thm: prefix on a conjecture misleads agents who grep for conj: to find conjectures.
CLAUDE.md:849:AP167: Topologization scope. thm:topologization is PROVED for affine KM V_k(g) at non-critical level k != -h^v (where Sugawara T = {Q,G} is explicit). For general chiral algebras with conformal vector: CONJECTURAL (conj:topologization-general). The proof is COHOMOLOGICAL (works on Q-cohomology, not on cochains). For class M (Virasoro), where chain-level BV/bar is false, the E_3 may exist only on cohomology. COUNTER: every topologization reference must carry scope qualifier "(proved for affine KM at non-critical level)."
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

 succeeded in 50ms:
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
**Considering modular theorem updates**

I might need to think about the D E1 modular theorem here. I should be careful since user requests an audit rather than an edit. It seems like we don't need to make changes, but maybe it's a good idea to clearly state the scope lock and plan through an update. I'll probably proceed with the update_plan to ensure everything aligns properly. Commentary will be important in this context.
codex
I’ve confirmed the constitutional surfaces: concordance records Theorem D as proved and already narrows it to uniform weight, with genus 1 universal and multi-weight requiring an extra correction term. Next I’m reading the exact theorem/proof block in `chapters/theory/higher_genus_modular_koszul.tex` and then every cited dependency that the proof actually uses.
Plan update
Adversarial audit of Theorem D requires fixing the exact theorem surface, then validating each proof dependency and boundary case before checking downstream drift.
  → Locate Theorem D statement, labels, surrounding definitions, and full proof block
  • Read each cited dependency and verify hypotheses match the proof’s use
  • Stress-test formula and scope via boundary values, genus/weight cases, and multi-weight correction surfaces
  • Search for duplicate or conflicting theorem surfaces in chapters and across volumes
  • Re-verify surviving findings and prepare severity-ordered audit report
exec
/bin/zsh -lc "rg -n \"thm:genus-universality|def:scalar-lane|delta F_g\\\\"'^'"\\\\{\\\\mathrm\\\\{cross\\\\}\\\\}|delta_F_g\\\\"'^cross|UNIFORM-WEIGHT|ALL-WEIGHT|genus universality|Theorem D|F_1 = '"\\\\kappa/24|F_1\\\\s*=\\\\s*\\\\kappa/24|F_1\\\\s*=\\\\s*\\\\\\\\kappa/24|lambda_g\\\\"'^'"\\\\{\\\\mathrm\\\\{FP\\\\}\\\\}|obs_g\\(|\\\\\\mathrm\\{obs\\}_g\" chapters/theory/higher_genus_modular_koszul.tex chapters/frame/guide_to_main_results.tex chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1180,1425p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,360p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1425,1575p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:thm:genus-universality|def:scalar-lane|delta F_g\^\{\mathrm\{cross\}\}|delta_F_g\^cross|UNIFORM-WEIGHT|ALL-WEIGHT|genus universality|Theorem D|F_1 = \kappa/24|F_1\s*=\s*\kappa/24|F_1\s*=\s*\\kappa/24|lambda_g\^\{\mathrm\{FP\}\}|obs_g\(|\\mathrm\{obs\}_g)
                                                           ^^
error: unrecognized escape sequence
 succeeded in 51ms:
and \textup{MK5} \textup{(}complementarity\textup{)} hold
at genus~$1$ without any conditional hypothesis.
\end{corollary}

\begin{proof}
MK1 (genus-$0$ Koszulity):
Theorem~\ref{thm:km-chiral-koszul}.
MK2 (Verdier):
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
 succeeded in 51ms:
 evaluation-generated core are proved for all simple Lie types
 (Corollary~\ref{cor:mc3-all-types}).
\item \textbf{Completion towers}: strong completion-tower theorem
 (Theorem~\ref{thm:completed-bar-cobar-strong}).
 MC4 splits into MC4$^+$ (positive towers, solved) and
 MC4$^0$ (resonant towers, reduced to finite resonance).
\item \textbf{Sewing at all genera}: general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}).
\end{enumerate}

\subsection*{The shadow obstruction tower}

The universal MC element $\Theta_\cA$ has finite-order
projections $\Theta_\cA^{\le r}$, each a graph sum through
degree~$r$ with obstruction class
$\mathfrak{o}_{r+1}(\cA) \in \mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(\cA)$.
The named shadows are:
\[
\underbrace{\kappa}_{\text{degree 2}}
\;\to\;
 succeeded in 51ms:
unconditional.
\end{corollary}

\begin{proof}
MK1 (genus-$0$ Koszulity):
Theorem~\ref{thm:km-chiral-koszul}.
MK2 (Verdier):
Theorem~\ref{thm:verdier-bar-cobar}.
MK3 (PBW degeneration at all genera):
Theorem~\ref{thm:pbw-allgenera-km}.
MK4 and MK5 follow from MK1--MK3 by
Theorems~\ref{thm:higher-genus-inversion}
and~\ref{thm:quantum-complementarity-main}.
Item~(i) is MK4 applied to~$\widehat{\fg}_k$;
item~(ii) is MK5;
item~(iii) follows from~(i) and the
scalar characteristic
(Theorem~\ref{thm:modular-characteristic}).
\end{proof}


thinking
**Searching for theorem details**

I'm trying to locate the theorem label, probably related to the modular characteristic or possibly referred to as Theorem D. I'll search within the higher genus modular Koszul file. Running a simpler command might help. I noticed that the registry has the reference for Theorem E1 at line 1276, but the modular characteristic theorem could be located elsewhere. I need to find this theorem and any associated dependencies, so I'll search a bit more thoroughly.
codex
The target surface is splitting into two theorem lanes in the theory chapter: `thm:e1-theorem-D-modular` and `thm:modular-characteristic`. I’m locating both, because the guide and concordance point to the scalar theorem, but the registry also exposes an ordered `E_1` version that may be feeding the final proof.
exec
/bin/zsh -lc "rg -n \"thm:modular-characteristic|thm:e1-theorem-D-modular|def:scalar-lane|thm:mumford-formula|thm:primitive-flat-descent|thm:theta-direct-derivation|delta F_g|delta_F_g|cross-channel|uniform-weight|scalar lane|obs_g|F_1 =|F_1=|\\\\lambda_g\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1230,1365p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13880,14280p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14280,14780p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:thm:modular-characteristic|thm:e1-theorem-D-modular|def:scalar-lane|thm:mumford-formula|thm:primitive-flat-descent|thm:theta-direct-derivation|delta F_g|delta_F_g|cross-channel|uniform-weight|scalar lane|obs_g|F_1 =|F_1=|\lambda_g)
                                                                                                                                                                                                                                    ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  1230	(Theorem~\ref{thm:pbw-genus1-km}) establishes a
  1231	three-step mechanism (PBW decomposition, Whitehead
  1232	acyclicity, Killing-form contraction) that is
  1233	genus-independent. We verify that each step
  1234	extends without modification to $g \geq 2$.
  1235	
  1236	\medskip
  1237	\emph{Step~1: $E_1$ decomposition at genus~$g$.}
  1238	
  1239	At genus~$g$, the chain groups of the bar complex use
  1240	forms on $\overline{C}_n(\Sigma_g)$, the
  1241	Fulton--MacPherson compactification of configuration
  1242	space on a smooth projective curve~$\Sigma_g$ of
  1243	genus~$g$. The curve contributes regular forms
  1244	from $H^{1,0}(\Sigma_g) \cong \bC^g$ (holomorphic
  1245	$1$-forms). These are regular at every collision
  1246	divisor~$D_{ij}$: they arise from the global geometry
  1247	of~$\Sigma_g$, not from OPE poles.
  1248	
  1249	Since $d_0^{\mathrm{PBW}}$ acts by Poincar\'{e} residue at
 succeeded in 50ms:
 13880	$d\mathfrak{K}_\cA + \mathfrak{K}_\cA \star
 13881	\mathfrak{K}_\cA = 0$
 13882	is the perturbative quantization of the chiral OPE
 13883	in the genus parameter~$\hbar$.
 13884	\begin{enumerate}[label=\textup{(\roman*)}]
 13885	\item \emph{Classical field theory.}
 13886	 The genus-zero restriction
 13887	 $\mathfrak{K}_\cA^{(0)} := \sum_{n \geq 3} K_{0,n}^\cA$
 13888	 satisfies the classical master equation
 13889	 $d\mathfrak{K}_\cA^{(0)}
 13890	 + \mathfrak{K}_\cA^{(0)} \star_0
 13891	 \mathfrak{K}_\cA^{(0)} = 0$:
 13892	 the $A_\infty$-structure equation for the transferred
 13893	 chiral operations. This is the complete tree-level content
 13894	 of $\cA$.
 13895	\item \emph{One-loop corrections.}
 13896	 At genus~$1$, degree~$0$: the non-separating self-sewing
 13897	 $\Delta_{\mathrm{ns}}(K_{0,2}^\cA)$ closes both legs of
 13898	 the binary corolla, producing the modular characteristic
 13899	 \begin{equation}
 succeeded in 50ms:
 14280	\]
 14281	\end{proposition}
 14282	
 14283	\begin{proof}
 14284	A cyclic Maurer--Cartan element defines a Hamiltonian whose
 14285	Euler--Lagrange equation is the Maurer--Cartan equation. The
 14286	derived intersection of the two Lagrangians is identified with the
 14287	corresponding shifted critical locus.
 14288	\end{proof}
 14289	
 14290	\begin{remark}[The unifying principle]
 14291	\label{rem:unifying-principle}
 14292	\index{unifying principle|textbf}
 14293	\index{shadow obstruction tower!as primary object}
 14294	The \emph{shadow obstruction tower}
 14295	$\Theta_\cA^{\leq 2},\, \Theta_\cA^{\leq 3},\,
 14296	\Theta_\cA^{\leq 4},\, \ldots$
 14297	in the modular convolution algebra
 14298	$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is the
 14299	organizing structure from which all five main theorems, the

thinking
**Searching for the theorem**

I’m trying to find the actual theorem, specifically thm:modular-characteristic, but I haven’t come across it in my snippets around 14135 yet. Maybe I can look for it in simpler ways, possibly using fixed-strings. I might want to use `rg -F` with multiple queries. What I need is a full proof of the theorem, so looking into executing commands could be my next step. Let's see how this unfolds!
exec
/bin/zsh -lc "rg -n -F 'thm:genus-universality' chapters/theory/higher_genus_modular_koszul.tex chapters chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:modular-characteristic' chapters/theory/higher_genus_modular_koszul.tex chapters chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'def:scalar-lane' chapters/theory/higher_genus_modular_koszul.tex chapters chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:e1-theorem-D-modular' chapters/theory/higher_genus_modular_koszul.tex chapters chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
chapters/theory/higher_genus_modular_koszul.tex:5064:(\textup{Theorem~\ref{thm:modular-characteristic}}).
chapters/theory/higher_genus_modular_koszul.tex:7713:(Theorem~\ref{thm:modular-characteristic}(iii);
chapters/theory/higher_genus_modular_koszul.tex:9670:(Theorem~\ref{thm:modular-characteristic}): a single number
chapters/theory/higher_genus_modular_koszul.tex:20421:(Theorem~\ref{thm:modular-characteristic}(iv)) gives the result.
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
chapters/theory/higher_genus_modular_koszul.tex:2404: (Theorem~\ref{thm:genus-universality}).
chapters/theory/higher_genus_modular_koszul.tex:2511:(Theorem~\ref{thm:genus-universality}).
chapters/theory/higher_genus_modular_koszul.tex:2695:Part~(i) is Theorem~\ref{thm:genus-universality} for
chapters/theory/higher_genus_modular_koszul.tex:2703:Theorem~\ref{thm:genus-universality}(ii).
chapters/theory/higher_genus_modular_koszul.tex:2760:Theorem~\ref{thm:genus-universality}); generating function via
chapters/theory/higher_genus_modular_koszul.tex:3133:Theorem~\ref{thm:genus-universality}. The GUE free energy
chapters/theory/higher_genus_modular_koszul.tex:3294:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
chapters/theory/higher_genus_modular_koszul.tex:3688:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
chapters/theory/higher_genus_modular_koszul.tex:3740:Theorem~\ref{thm:genus-universality}(ii)).
chapters/theory/higher_genus_modular_koszul.tex:5306:(Theorem~\ref{thm:genus-universality},
chapters/theory/higher_genus_modular_koszul.tex:7707:(Theorem~\ref{thm:genus-universality}).
chapters/theory/higher_genus_modular_koszul.tex:7863:Theorem~\ref{thm:genus-universality} identifies the scalar trace
chapters/theory/higher_genus_modular_koszul.tex:8011:Theorem~\ref{thm:genus-universality} identifies
chapters/theory/higher_genus_modular_koszul.tex:8435:by Theorem~\ref{thm:genus-universality}\textup{(iii)}.
chapters/theory/higher_genus_modular_koszul.tex:9515:Theorem~\textup{\ref{thm:genus-universality}}, then the full
chapters/theory/higher_genus_modular_koszul.tex:9570:By Theorem~\ref{thm:genus-universality},
chapters/theory/higher_genus_modular_koszul.tex:11623:theorem (Theorem~\ref{thm:genus-universality}).
chapters/theory/higher_genus_modular_koszul.tex:14452:Theorem~\ref{thm:genus-universality} identifies the scalar trace with
chapters/theory/higher_genus_modular_koszul.tex:21797:(Theorem~\ref{thm:genus-universality} at $g=1$, the
 succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:2495:\label{def:scalar-lane}
chapters/frame/heisenberg_frame.tex:1866:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}). The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1815:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
chapters/connections/thqg_preface_supplement.tex:551:(Definition~\ref{def:scalar-lane}), the scalar-level genus expansion of
chapters/connections/casimir_divisor_core_transport.tex:1320:uniform-weight lane (Definition~\ref{def:scalar-lane}),
chapters/connections/genus_complete.tex:884:(Definition~\ref{def:scalar-lane}) is determined by a single numerical invariant: the obstruction coefficient $\kappa(\mathcal{A})$, which depends on the genus-$1$ curvature alone. In practice, $\kappa(\cA)$ is computed from the central charge and the structure of the OPE: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$, $\kappa(\mathrm{Vir}_c) = c/2$, $\kappa(\mathcal{H}_k) = k$. On that lane, the scalar genus expansion $F_g(\mathcal{A}) = \kappa(\mathcal{A}) \cdot \lambda_g^{\mathrm{FP}}$ is given by Bernoulli numbers. For arbitrary modular Koszul algebras, only the genus-$1$ scalar term is unconditional. The separately proved spectral invariants, and the full Maurer--Cartan completion on the simple-Lie-symmetry locus of Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}, are \emph{not} determined by~$\kappa(\cA)$ alone; see Theorem~\ref{thm:spectral-characteristic} and Definition~\ref{def:full-modular-package}.
chapters/connections/thqg_modular_bootstrap.tex:2779: (Definition~\ref{def:scalar-lane}) this further gives a scalar
chapters/connections/frontier_modular_holography_platonic.tex:26: \textup{(}Definition~\textup{\ref{def:scalar-lane}}\textup{)},
chapters/connections/concordance.tex:57: \textup{(}Definition~\ref{def:scalar-lane}\textup{)}
chapters/connections/thqg_fredholm_partition_functions.tex:66:\textup{(}Definition~\ref{def:scalar-lane}\textup{)},
chapters/connections/thqg_preface_supplement.tex:551:(Definition~\ref{def:scalar-lane}), the scalar-level genus expansion of
chapters/connections/casimir_divisor_core_transport.tex:1320:uniform-weight lane (Definition~\ref{def:scalar-lane}),
chapters/connections/master_concordance.tex:522: (Definition~\ref{def:scalar-lane}).
chapters/connections/arithmetic_shadows.tex:10847: (Definition~\ref{def:scalar-lane}).
chapters/connections/genus_complete.tex:884:(Definition~\ref{def:scalar-lane}) is determined by a single numerical invariant: the obstruction coefficient $\kappa(\mathcal{A})$, which depends on the genus-$1$ curvature alone. In practice, $\kappa(\cA)$ is computed from the central charge and the structure of the OPE: $\kappa(\widehat{\mathfrak{g}}_k) = (k+h^\vee)\dim\mathfrak{g}/(2h^\vee)$, $\kappa(\mathrm{Vir}_c) = c/2$, $\kappa(\mathcal{H}_k) = k$. On that lane, the scalar genus expansion $F_g(\mathcal{A}) = \kappa(\mathcal{A}) \cdot \lambda_g^{\mathrm{FP}}$ is given by Bernoulli numbers. For arbitrary modular Koszul algebras, only the genus-$1$ scalar term is unconditional. The separately proved spectral invariants, and the full Maurer--Cartan completion on the simple-Lie-symmetry locus of Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}, are \emph{not} determined by~$\kappa(\cA)$ alone; see Theorem~\ref{thm:spectral-characteristic} and Definition~\ref{def:full-modular-package}.
chapters/connections/thqg_gravitational_complexity.tex:456:(Definition~\ref{def:scalar-lane};
chapters/connections/arithmetic_shadows.tex:10847: (Definition~\ref{def:scalar-lane}).
chapters/connections/master_concordance.tex:522: (Definition~\ref{def:scalar-lane}).
chapters/connections/thqg_fredholm_partition_functions.tex:66:\textup{(}Definition~\ref{def:scalar-lane}\textup{)},
chapters/connections/thqg_modular_bootstrap.tex:2779: (Definition~\ref{def:scalar-lane}) this further gives a scalar
 succeeded in 51ms:
chapters/connections/concordance.tex:3623: \ref{thm:e1-theorem-D-modular} \\
chapters/connections/concordance.tex:3623: \ref{thm:e1-theorem-D-modular} \\
chapters/theory/e1_modular_koszul.tex:2018:\label{thm:e1-theorem-D-modular}

thinking
**Clarifying theorem references**

I’m looking into the theorem on genus-universality in higher_genus_foundations.tex, as well as the likely summary in higher_genus_modular_koszul. I need to read the theorem statement and proof at line 2628 in the latter and also check the genus universality theorem at line 5241 in the former. I’m trying to figure out which theorem the user is referring to by Theorem D. I’ll need to explore the proofs thoroughly and determine if there’s a reference to modular-characteristic. I’ll do a detailed audit by checking lines from 2495 to 2890 in higher_genus_modular_koszul and the relevant parts in higher_genus_foundations.tex.
codex
The scalar theorem itself sits in `higher_genus_modular_koszul.tex`, but its proof imports the actual genus-universality theorem from `higher_genus_foundations.tex`. I’m reading both surfaces together so I can separate “proved here” from “repackaged here.”
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5405,5485p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5200,5405p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2470,2895p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '1970,2075p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5405	\item[\textup{Level~2.}] \emph{Koszul} (curve-independent
  5406	 invariants). Chirally Koszul algebras
  5407	 (Definition~\ref{def:koszul-chiral-algebra}) have
  5408	 curve-independent bar cohomology:
  5409	 Proposition~\ref{prop:genus0-curve-independence} at
  5410	 genus~$0$,
  5411	 Theorem~\ref{thm:open-stratum-curve-independence} at
  5412	 higher genus on the open stratum. The shadow invariants
  5413	 $\kappa$, $S_r$, and the modular characteristic
  5414	 $\mathrm{obs}_g = \kappa \cdot \lambda_g$ for
  5415	 uniform-weight algebras at all genera, and
  5416	 $\mathrm{obs}_1 = \kappa \cdot \lambda_1$
  5417	 \textup{(g=1 only; all-weight at g=1 is unconditional)}
  5418	 unconditionally
  5419	 (Theorem~\ref{thm:genus-universality}), are consequences
  5420	 of Koszulness combined with universality:
  5421	 the \'etale descent datum from Level~0 ensures
  5422	 that the shadow obstruction tower is extracted from
  5423	 curve-independent data
  5424	 (Remark~\ref{rem:cliff-universality}).
 succeeded in 52ms:
  5200	\begin{example}[Heisenberg case]\label{ex:heisenberg-obs-squares}
  5201	For the Heisenberg algebra with
  5202	$\operatorname{obs}_g = \kappa \cdot \lambda_g$ Theorem~\ref{thm:obstruction-nilpotent-all-genera} gives
  5203	$(\operatorname{obs}_g)^2 = \kappa^2 \cdot \lambda_g^2 = 0$
  5204	for \emph{all} $g \geq 1$, by Mumford's relation.
  5205	\end{example}
  5206	
  5207	\subsection{Summary table: obstruction classes for key examples}
  5208	\label{subsec:obstruction-summary-table}
  5209	
  5210	\begin{table}[ht]
  5211	\centering
  5212	\caption{Genus-$g$ obstruction classes For single-generator families, $\mathrm{obs}_g = \kappa \cdot \lambda_g$
  5213	 holds unconditionally at all genera. For multi-weight families
  5214	 \textup{(}$W_3$\textup{)}, the formula is unconditional at $g = 1$;
  5215	 at $g \geq 2$, a cross-channel correction
  5216	 $\delta F_g^{\mathrm{cross}} \neq 0$
  5217	 \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)} is present
  5218	 \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.}
  5219	\label{tab:obstruction-summary}
 succeeded in 50ms:
  2470	The package~$\mathcal{C}_{\cA}$ has four structural properties:
  2471	\begin{enumerate}[label=\textup{(\alph*)}]
  2472	\item \emph{Functorial}: $\mathcal{C}$ is natural in morphisms
  2473	 of modular Koszul objects;
  2474	\item \emph{Dualizable}: the duality $\cA \leftrightarrow \cA^!$
  2475	 acts on each component
  2476	 ($\kappa + \kappa' = K$, $\Delta_{\cA^!}$ determined by
  2477	 $\Delta_{\cA}$, etc.);
  2478	\item \emph{Modular}: compatible with clutching and
  2479	 boundary degeneration on~$\overline{\mathcal{M}}_{g,n}$;
  2480	\item \emph{Non-scalar}: $\kappa(\cA)$ is only the first shadow;
  2481	 the full package contains strictly more information
  2482	 (cf.\ the spectral data of level~(2) in
  2483	 Remark~\ref{rem:characteristic-hierarchy}).
  2484	\end{enumerate}
  2485	
  2486	\smallskip\noindent
  2487	The cyclic $L_\infty$-algebra $\Defcyc(\cA)$ is constructed
  2488	by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
  2489	is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
 succeeded in 52ms:
  1970	and this perturbation preserves the PBW filtration (the curvature is
  1971	in the center of the algebra). The inversion theorem for perturbed
  1972	complexes (the filtered quasi-isomorphism criterion of
  1973	Theorem~\ref{thm:bar-cobar-inversion-qi}) then gives the
  1974	result at each genus.
  1975	\end{proof}
  1976	
  1977	\begin{theorem}[Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity; \ClaimStatusProvedHere]
  1978	\label{thm:e1-theorem-C-modular}
  1979	\label{thm:e1-theorem-C}
  1980	\index{five main theorems!E1@$E_1$ (ordered)!Theorem C (modular)}
  1981	At genus~$g$ and each degree~$n$ with $2g - 2 + n > 0$, the ordered
  1982	complementarity takes the form
  1983	\begin{equation}
  1984	\label{eq:e1-complementarity-modular}
  1985	Q_{g,n}^{E_1}(\cA) + Q_{g,n}^{E_1}(\cA^{!,E_1})
  1986	\;=\;
  1987	H^*\!\bigl(\overline{\cM}_{g,n}^{\,\mathrm{rib}},\,
  1988	Z^{E_1}(\cA)\bigr),
  1989	\end{equation}
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '2075,2125p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2075	{\Barch}^{\mathrm{ord}}(\cA_2)$
  2076	(ordered shuffle theorem), and the monodromy of a product
  2077	connection is additive.
  2078	
  2079	(iii)~Anti-symmetry: opposite-duality gives
  2080	${\Barch}^{\mathrm{ord}}(\cA^{\op}) \cong
  2081	{\Barch}^{\mathrm{ord}}(\cA)^{\cop}$,
  2082	and the monodromy of the co-opposite is the inverse.
  2083	
  2084	(iv)~Coinvariant: by
  2085	Theorem~\ref{thm:e1-coinvariant-shadow} at degree~$2$.
  2086	\end{proof}
  2087	
  2088	\begin{theorem}[Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered Hochschild at genus~$g$; \ClaimStatusProvedHere]
  2089	\label{thm:e1-theorem-H-modular}
  2090	\label{thm:e1-theorem-H}
  2091	\index{five main theorems!E1@$E_1$ (ordered)!Theorem H (modular)}
  2092	For every genus~$g$ and complete $\cA$-bimodule~$M$, the
  2093	genus-$g$ ordered Hochschild homology is computed
  2094	coalgebraically\textup{:}
codex
I’ve reached the proof-bearing surface. The high-risk part is not the repackaged `thm:modular-characteristic` proof, which is only a routing proof, but the underlying `thm:genus-universality` argument in `higher_genus_foundations.tex`, especially the jump from fiberwise curvature to the global `\lambda_g` class and the multi-weight carve-out.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:quantum-arnold-relations}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:family-index}' chapters/theory chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:2872:\label{thm:quantum-arnold-relations}
 succeeded in 50ms:
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/concordance.tex:5928:\ClaimStatusProvedHere]\label{thm:family-index}
exec
/bin/zsh -lc "rg -n -F '\\label{thm:mumford-formula}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:multi-generator-universality}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{prop:multi-generator-obstruction}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:heisenberg-obs}' chapters/theory chapters/examples chapters/frame" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:kac-moody-obs}' chapters/theory chapters/examples chapters/frame" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:multi-weight-genus-expansion}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:vir-genus1-curvature}' chapters/theory chapters/examples chapters/frame" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:wn-obstruction}' chapters/theory chapters/examples chapters/frame" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:universal-generating-function}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{rem:propagator-weight-universality}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:anomaly-koszul}' chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:4548:\label{thm:mumford-formula}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:21683:\label{thm:multi-generator-universality}
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:5655:\label{prop:multi-generator-obstruction}
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:4813:\begin{theorem}[Kac--Moody obstruction at genus \texorpdfstring{$g$}{g}; \ClaimStatusProvedHere]\label{thm:kac-moody-obs}
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:4734:\begin{theorem}[Heisenberg obstruction at genus \texorpdfstring{$g$}{g}; \ClaimStatusProvedHere]\label{thm:heisenberg-obs}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:21682:\label{thm:multi-weight-genus-expansion}
 succeeded in 50ms:
chapters/examples/w_algebras.tex:1577:\label{thm:vir-genus1-curvature}
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:5610:\label{rem:propagator-weight-universality}%
 succeeded in 51ms:
chapters/examples/genus_expansions.tex:1913:\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
 succeeded in 51ms:
chapters/examples/w_algebras.tex:2173:\label{thm:wn-obstruction}
 succeeded in 51ms:
chapters/connections/editorial_constitution.tex:1864:\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
chapters/connections/outlook.tex:667:\phantomsection\label{thm:anomaly-koszul}
codex
A likely circularity surface has appeared: `thm:genus-universality` cites `thm:family-index`, but the only live `thm:family-index` label I’ve found so far is in the concordance chapter, not a theory proof file. I’m checking whether that theorem is actually proved independently or merely restates Theorem D.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2840,2915p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4525,4588p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1560,1618p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4728,4868p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1910,1945p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2150,2218p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '1848,1888p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5590,5695p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5910,5968p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2840	\emph{Genus 0 (Rational Curve).}
  2841	\begin{equation}
  2842	\eta_{ij}^{(0)} = d\log(z_i - z_j) = \frac{dz_i - dz_j}{z_i - z_j}
  2843	\end{equation}
  2844	No global obstructions.
  2845	
  2846	\emph{Genus 1 (Elliptic Curve $E_\tau = \mathbb{C}/(\mathbb{Z} + \tau\mathbb{Z})$):}
  2847	\begin{equation}
  2848	\eta_{ij}^{(1)} = \frac{\theta_1'(z_i - z_j \mid \tau)}{\theta_1(z_i - z_j \mid \tau)}(dz_i - dz_j)
  2849	\end{equation}
  2850	where $\theta_1(z|\tau)$ is the odd Jacobi theta function and $\theta_1' = \partial_z \theta_1$. This form is quasi-periodic: $\eta_{ij}^{(1)}(z_i + \tau, z_j) = \eta_{ij}^{(1)}(z_i, z_j) - 2\pi i\,(dz_i - dz_j)$.
  2851	
  2852	\emph{Genus $g \geq 2$ (Hyperbolic Case).}
  2853	\begin{equation}
  2854	\eta_{ij}^{(g)} = \partial_{p_i}\log E(p_i, p_j) + \pi\sum_{\alpha, \beta = 1}^g \omega_\alpha(p_i) \,(\operatorname{Im}\Omega)_{\alpha\beta}^{-1}\, \operatorname{Im}\!\left(\int_{p_0}^{p_j}\omega_\beta\right)
  2855	\end{equation}
  2856	where $\partial_{p_i}$ differentiates in the first variable (giving a $(1,0)$-form in $p_i$, scalar in $p_j$) and:
  2857	\begin{itemize}
  2858	\item $E(p, q)$ is the prime form (a $(-\frac{1}{2}, -\frac{1}{2})$-differential with a simple zero along the diagonal)
  2859	\item $\omega_1, \ldots, \omega_g$ are the normalized holomorphic 1-forms ($\oint_{A_\alpha}\omega_\beta = \delta_{\alpha\beta}$)
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21655,21755p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4525	This theorem is imported and treated as \ClaimStatusProvedElsewhere. Standard
  4526	descriptions of tautological generators and low-genus cohomology structure for
  4527	$\overline{\mathcal{M}}_{g,n}$ are classical in the moduli-space literature;
  4528	see~\cite{Mumford83}.
  4529	\end{remark}
  4530	
  4531	\begin{definition}[Hodge bundle]
  4532	\label{def:hodge-bundle}
  4533	\index{Hodge bundle|textbf}
  4534	The \emph{Hodge bundle} $\mathbb{E} \to \overline{\mathcal{M}}_{g,n}$ is the rank-$g$ vector bundle whose fiber over $[(\Sigma_g; p_1, \ldots, p_n)]$ is:
  4535	\begin{equation}
  4536	\mathbb{E}_{[\Sigma_g]} = H^0(\Sigma_g, \Omega^1_{\Sigma_g})
  4537	\end{equation}
  4538	the space of holomorphic differentials.
  4539	
  4540	The Chern classes:
  4541	\begin{equation}
  4542	\lambda_i = c_i(\mathbb{E}) \in H^{2i}(\overline{\mathcal{M}}_{g,n}, \mathbb{Q})
  4543	\end{equation}
  4544	are the \emph{$\lambda$-classes}. (The \emph{Mumford--Morita--Miller classes} $\kappa_i = \pi_*(\psi_{n+1}^{i+1}) \in H^{2i}(\overline{\mathcal{M}}_{g,n})$ are related but distinct: they are pushforwards of powers of the universal cotangent class.)
 succeeded in 52ms:
  1560	
  1561	\subsubsection{Genus-1 bar complex}
  1562	
  1563	The genus-1 bar complex is:
  1564	\begin{equation}\label{eq:vir-genus1-bar}
  1565	\barB^{(1),n}(\mathrm{Vir}_c) = \Gamma\bigl(\overline{C}_n(E_\tau),\;
  1566	 \omega_{E_\tau}^{\otimes 2n} \otimes \Omega^n_{\log}\bigr)
  1567	\end{equation}
  1568	where the exponent $2n$ reflects the conformal weight $h_T = 2$ of the
  1569	generator (each copy of $T$ contributes weight~$2$ to the tensor product).
  1570	The genus-1 propagator is~\eqref{eq:genus1-propagator}
  1571	and the differential is~\eqref{eq:genus1-diff}, with the OPE data of the
  1572	Virasoro algebra replacing that of $\widehat{\mathfrak{sl}}_2$.
  1573	
  1574	\subsubsection{Curvature theorem}
  1575	
  1576	\begin{theorem}[Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc}; \ClaimStatusProvedHere]
  1577	\label{thm:vir-genus1-curvature}
  1578	The genus-1 differential satisfies:
  1579	\begin{equation}\label{eq:vir-genus1-dsquared}
 succeeded in 51ms:
  4728	Combining with Step 2 gives the stated formula.
  4729	\end{proof}
  4730	
  4731	\subsection{Example 1: Heisenberg algebra, level shift obstruction}
  4732	\label{subsec:heisenberg-obstruction}
  4733	
  4734	\begin{theorem}[Heisenberg obstruction at genus \texorpdfstring{$g$}{g}; \ClaimStatusProvedHere]\label{thm:heisenberg-obs}
  4735	For the Heisenberg vertex algebra $\mathcal{H}_\kappa$ at level $\kappa$, the 
  4736	genus-$g$ obstruction is :
  4737	\begin{equation}
  4738	\text{obs}_g^{\mathcal{H}} = \kappa \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g, \mathbb{C})
  4739	\qquad \end{equation}
  4740	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle \textup{(LOCAL)}.
  4741	
  4742	Explicitly:
  4743	\begin{itemize}
  4744	\item $g=1$: $\text{obs}_1 = \kappa \cdot \lambda_1$ \textup{(g=1 only; all-weight at g=1 is unconditional)} where $\lambda_1 = c_1(\mathbb{E}) \in H^2(\overline{\mathcal{M}}_{1,1})$
  4745	\item $g=2$: $\text{obs}_2 = \kappa \cdot \lambda_2 = \kappa \cdot c_2(\mathbb{E})$ \item $g \geq 3$: $\text{obs}_g = \kappa \cdot \lambda_g$ \end{itemize}
  4746	\end{theorem}
  4747	
 succeeded in 52ms:
  1910	theorem on $\overline{\mathcal{M}}_g$.
  1911	\end{remark}
  1912	
  1913	\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
  1914	\index{genus expansion!universal generating function}
  1915	\index{obstruction coefficient!generating function}
  1916	For any Koszul chiral algebra $\mathcal{A}$ with uniform conformal
  1917	weight and obstruction coefficient $\kappa = \kappa(\mathcal{A})$:
  1918	\begin{equation}\label{eq:universal-generating-function}
  1919	\sum_{g=1}^{\infty} F_g(\mathcal{A})\, x^{2g} \;=\; \kappa \left(\frac{x/2}{\sin(x/2)} - 1\right)
  1920	\end{equation}
  1921	with radius of convergence $|x| = 2\pi$, independent of $\mathcal{A}$.
  1922	For arbitrary modular Koszul algebras, the genus-$1$ coefficient
  1923	still satisfies $F_1(\mathcal{A}) = \kappa(\mathcal{A})/24$.
  1924	\end{theorem}
  1925	
  1926	\begin{proof}
  1927	By Theorem~\ref{thm:genus-universality}(iii), $F_g(\mathcal{A}) = \kappa \cdot \lambda_g^{\mathrm{FP}}$ where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The proof of Proposition~\ref{prop:complementarity-genus-series} shows that $\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g} = (x/2)/\sin(x/2) - 1$. Multiplying by $\kappa$ gives~\eqref{eq:universal-generating-function}. The radius is $2\pi$ (the first zero of $\sin(x/2)$). The genus-$1$ clause is the $x^2$ coefficient.
  1928	\end{proof}
  1929	
 succeeded in 52ms:
  2150	\end{tabular}
  2151	\end{center}
  2152	For KM, $\kappa$ is linear in~$k$ (sum vanishes); for $\mathcal{W}$-algebras, $\kappa$ is nonlinear (via DS), producing a nonzero sum.
  2153	\end{remark}
  2154	
  2155	\begin{remark}[Convention: \texorpdfstring{$\kappa$}{kappa} vs.\ \texorpdfstring{$\kappa_g$}{kappa\_g}]\label{rem:kappa-convention-disambiguation}
  2156	Throughout this chapter, $\kappa$ (without subscript) denotes the \emph{obstruction coefficient} of the genus-1 bar complex: the scalar in the formula $\mathrm{obs}_1 = \kappa \cdot \lambda_1$, where $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class. This is a number depending on the chiral algebra (e.g., $\kappa = c/2$ for Virasoro, $\kappa = 5c/6$ for $\mathcal{W}_3$).
  2157	
  2158	This should not be confused with the \emph{Mumford--Miller--Morita kappa class} $\kappa_g = \pi_*(\psi^{g+1}) \in H^{2g}(\overline{\mathcal{M}}_g)$, which is a tautological class on the moduli space of curves (cf.\ Chapter~\ref{chap:higher-genus}). The level of the affine algebra is denoted~$k$, not~$\kappa$.
  2159	\end{remark}
  2160	
  2161	\subsection{\texorpdfstring{General $\mathcal{W}_N$: obstruction coefficient formula}{General WN: obstruction coefficient formula}}
  2162	\label{sec:wn-obstruction}
  2163	\index{obstruction coefficient!general W_N@general $\mathcal{W}_N$}
  2164	
  2165	The Virasoro ($N = 2$) and $\mathcal{W}_3$ ($N = 3$) genus-1 pipelines
  2166	reveal a pattern in the obstruction coefficients: $\kappa = c/2$ and
  2167	$\kappa = c/2 + c/3 = 5c/6$ respectively, with each generator
  2168	contributing its own vacuum leakage. The general formula
  2169	for all $N$ validates the Master Table entry
 succeeded in 51ms:
  1848	analytic continuation argument from holomorphic to topological
  1849	Feynman transforms.
  1850	The correct bridge between holomorphic and topological frameworks is Chern--Simons gauge equivalence, not merely restriction from complex curves to $S^1$: Cattaneo--Mnev~\cite{CattaneoMnev10} establish that configuration space integrals on $3$-manifolds produce Vassiliev invariants via BV integration, and the comparison map involves the CS partition function (not a pointwise restriction of propagators).
  1851	
  1852	\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
  1853	The conjecture asserts that the dg Lie algebras controlling
  1854	holomorphic (chiral bar) and topological (Kontsevich integral)
  1855	deformation problems are quasi-isomorphic.
  1856	(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
  1857	\end{remark}
  1858	
  1859	\subsection{Anomaly cancellation and Koszul structure}
  1860	\label{subsec:anomaly-koszul}
  1861	\index{anomaly!Koszul-theoretic}
  1862	
  1863	\begin{theorem}[Anomaly cancellation as Koszul constraint;
  1864	\ClaimStatusProvedHere]\label{thm:anomaly-koszul}
  1865	\index{anomaly cancellation!Koszul constraint}
  1866	For the matter-ghost system
  1867	$\cA_{\mathrm{tot}} = \cA_{\mathrm{matter}} \otimes \cA_{\mathrm{ghost}}$:
 succeeded in 51ms:
  5590	$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
  5591	\textup{(LOCAL)}.
  5592	
  5593	\textup{(c)} \textbf{Resolved negatively.}
  5594	The bar propagator $d\log E(z,w)$ is weight-$1$
  5595	(Remark~\ref{rem:propagator-weight-universality}),
  5596	which controls the \emph{edges} of the graph sum.
  5597	The \emph{vertices} carry cross-channel OPE data, and the
  5598	mixed-channel amplitudes do \emph{not} cancel:
  5599	Theorem~\ref{thm:multi-weight-genus-expansion} proves
  5600	$F_g(\cA) = \kappa\cdot\lambda_g^{\mathrm{FP}}
  5601	+ \delta F_g^{\mathrm{cross}}(\cA)$
  5602	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5603	with $\delta F_2(\cW_3) = (c{+}204)/(16c) \neq 0$.
  5604	The identification
  5605	$\Gamma_{\cA} = \kappa(\cA)\Lambda$ fails for multi-weight
  5606	algebras.
  5607	\end{remark}
  5608	
  5609	\begin{remark}[Propagator weight universality]%
 succeeded in 50ms:
  5910	$\operatorname{rank}(\Delta_\cA)
  5911	=\deg\Delta_\cA
  5912	=\dim H^1_{\mathrm{cyc,prim}}(\cA)$: the number of independent
  5913	genus-$1$ deformation directions. Rank~$1$ for algebras with
  5914	one-dimensional deformation space (Heisenberg, Virasoro,
  5915	$\beta\gamma$); rank~$2$ for $\widehat{\mathfrak{sl}}_2$ and
  5916	$\mathcal W_3$.
  5917	\end{computation}
  5918	
  5919	\subsection{The index theorem for genus expansions}
  5920	
  5921	The appearance of the $\hat{A}$-genus in the Heisenberg genus
  5922	expansion (Theorem~\ref{thm:universal-generating-function})
  5923	and the Bernoulli asymptotics of $F_g(\cA)$ are not coincidental:
  5924	they are the output of a Grothendieck--Riemann--Roch computation
  5925	on the universal curve.
  5926	
  5927	\begin{theorem}[Family index theorem for genus expansions;
  5928	\ClaimStatusProvedHere]\label{thm:family-index}
  5929	\index{index theorem!modular deformation|textbf}
 succeeded in 52ms:
 21655	
 21656	\smallskip\noindent
 21657	(iii)~\emph{Non-separating boundary.}
 21658	The component $\hbar\Delta$ of $D$ acts by contracting two
 21659	external half-edges of a graph into an internal self-loop via the
 21660	pairing $\eta$. On the graph sum, removing the non-separating
 21661	edge~$e$ from $\Gamma$ produces a graph $\Gamma'$ of type
 21662	$(g{-}1, n{+}2)$: the genus drops by~$1$ and two new legs appear.
 21663	The amplitude is
 21664	$\sum_\alpha W_{\Gamma'}(v_1, \ldots, v_n, e_\alpha, e^\alpha)
 21665	\cdot P_e(\psi)$.
 21666	Collecting all such graphs gives the restriction to the
 21667	non-separating divisor
 21668	$\delta_{\mathrm{irr}} =
 21669	\xi_{\mathrm{nsep}}(\overline{\cM}_{g-1,n+2})$,
 21670	yielding axiom~(iii).
 21671	
 21672	Axioms~(i)--(iii) make $(\Omega^\cA, V, \eta)$ a CohFT
 21673	without unit in the sense of
 21674	Pandharipande--Pixton--Zvonkine. The unit axiom
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5968,6038p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5968	$\operatorname{ch}_g(\mathbb{E})$ against $\psi^{2g-2}$ on
  5969	$\overline{\mathcal{M}}_{g,1}$.
  5970	
  5971	\item \emph{$\hat{A}$-genus identification.}
  5972	On the same uniform-weight locus, the total generating function is
  5973	\begin{equation}\label{eq:family-index-generating}
  5974	\sum_{g \geq 1} F_g(\cA)\, x^{2g}
  5975	\;=\;
  5976	\kappa(\cA) \cdot \bigl(\hat{A}(ix) - 1\bigr)
  5977	\;=\;
  5978	\kappa(\cA) \cdot
  5979	\left(\frac{x/2}{\sin(x/2)} - 1\right),
  5980	\end{equation}
  5981	where the function $(x/2)/\sin(x/2)$ arises from
  5982	$\operatorname{Td}(T_\pi) = c_1(\omega_\pi)/(1 - e^{-c_1(\omega_\pi)})$
  5983	in the GRR formula, Wick-rotated by the positivity of
  5984	tautological intersection numbers on
  5985	$\overline{\mathcal{M}}_g$.
  5986	
  5987	\item \emph{Verdier compatibility.}
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6038,6098p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6038	and the relative dualizing sheaf~$\omega_\pi$:
  6039	\begin{equation}\label{eq:mumford-grr}
  6040	\operatorname{ch}(\mathbb{E})
  6041	\;=\;
  6042	\operatorname{ch}(R^0\pi_*\omega_\pi)
  6043	\;=\;
  6044	1 + \pi_*\!\left(
  6045	 \operatorname{ch}(\omega_\pi) \cdot
  6046	 \operatorname{Td}(T_\pi)
  6047	\right),
  6048	\end{equation}
  6049	
  6050	Serre duality on the fibers gives
  6051	$R^1\pi_*\omega_\pi \cong (R^0\pi_*\mathcal{O})^\vee \cong \mathcal{O}$,
  6052	so $\operatorname{ch}(R\pi_*\omega_\pi) = \operatorname{ch}(\mathbb{E}) - 1$.
  6053	
  6054	Write $K = c_1(\omega_\pi)$ for the relative canonical class. Since
  6055	$c_1(T_\pi) = -K$, the Todd class of the relative tangent bundle is
  6056	$\operatorname{Td}(T_\pi) = (-K)/(1 - e^K) = K/(e^K - 1)$, and the
  6057	pushforward becomes
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '6098,6148p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6098	Faber--Pandharipande~\cite{FP03}.
  6099	
  6100	\emph{Step~4: Generating function from the Todd class.}
  6101	The Bernoulli numbers $B_{2g}$ are the Taylor coefficients of
  6102	the Todd generating function
  6103	$x/(1 - e^{-x}) = 1 + x/2 + \sum_{g \geq 1}
  6104	\frac{B_{2g}}{(2g)!}\, x^{2g}$.
  6105	In Step~2, the Todd class $\operatorname{Td}(\omega_\pi)$
  6106	produced these Bernoulli numbers as the Chern character
  6107	$\operatorname{ch}_g(\mathbb{E})$, i.e., the genus expansion
  6108	\emph{is} the GRR pushforward.
  6109	Concretely:
  6110	\begin{align}
  6111	\sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\, x^{2g}
  6112	&\;=\;
  6113	\sum_{g \geq 1}
  6114	\frac{2^{2g-1}-1}{2^{2g-1}} \cdot
  6115	\frac{|B_{2g}|}{(2g)!}\, x^{2g}
  6116	\notag \\
  6117	&\;=\;

thinking
**Evaluating theorem dependencies**

I'm considering that the family-index theorem definitely depends on genus-universality, which raises a potential circularity issue. I need to verify whether the proof of genus-universality cites family-index at 5329, which seems critical. I should also check if the family-index theorem is in the concordance or see if there's another theorem with an independent proof. It looks circular, so cross-checking those references will be essential. I need to re-verify that there are no other family-index theorems. Time to read more of the Kac-Moody proof.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4868,4908p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4868	\text{obs}_g &= \dim(\mathfrak{g}) \cdot m_0 \cdot \lambda_g \\
  4869	&= \dim(\mathfrak{g}) \cdot \frac{k+h^\vee}{2h^\vee} \cdot \lambda_g \\
  4870	&= \frac{(k+h^\vee)\dim(\mathfrak{g})}{2h^\vee} \cdot \lambda_g
  4871	\qquad \end{align}
  4872	
  4873	\emph{Step 4: Consistency checks.}
  4874	
  4875	\emph{Critical level}: At $k = -h^\vee$, $\text{obs}_g = 0$ for all $g$ This is consistent
  4876	with $d^2 = 0$ on the bar complex at critical level (Proposition~\ref{prop:km-bar-curvature}(i)),
  4877	which reflects the enlarged center of $V_{-h^\vee}(\mathfrak{g})$.
  4878	
  4879	\emph{Heisenberg limit}: Taking $\mathfrak{g}$ abelian (so $h^\vee = 0$ requires care),
  4880	we instead note that for the Heisenberg algebra the structure constants vanish ($f^{abc} = 0$),
  4881	so the Casimir correction is absent. The obstruction reduces to
  4882	$\text{obs}_g = k \cdot \lambda_g$ in agreement with Theorem~\ref{thm:heisenberg-obs}.
  4883	
  4884	\emph{Koszul duality}: Under the Feigin--Frenkel involution $k \mapsto -k-2h^\vee$, the
  4885	obstruction transforms as:
  4886	\[\text{obs}_g^{\widehat{\mathfrak{g}}_{-k-2h^\vee}} =
  4887	\frac{(-k-2h^\vee+h^\vee)\dim(\mathfrak{g})}{2h^\vee} \cdot \lambda_g
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '1618,1638p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1618	$\mathrm{obs}_1(\mathrm{Vir}_c) = \kappa \cdot \lambda_1$ with
  1619	$\kappa = c/2$. The computation gives exactly $\kappa = c/2$.
  1620	In particular, $\kappa = 0 \iff c = 0$: the bar complex is uncurved at
  1621	genus~1 precisely when it is uncurved at genus~0
  1622	(Theorem~\ref{thm:virasoro-self-duality}).
  1623	\end{proof}
  1624	
  1625	\subsubsection{Spectral sequence collapse}
  1626	
  1627	\begin{theorem}[Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc}; \ClaimStatusProvedHere]
  1628	\label{thm:vir-genus1-inversion}
  1629	For generic central charge $c$ (specifically, $c \neq c_{r,s}$ for all
  1630	$r, s \geq 1$, where $c_{r,s}$ are the minimal model central charges),
  1631	the genus-1 bar-cobar adjunction:
  1632	\begin{equation}
  1633	\Omega\bigl(\barB^{(1)}(\mathrm{Vir}_c)\bigr) \xrightarrow{\;\sim\;} \mathrm{Vir}_c
  1634	\end{equation}
  1635	is a quasi-isomorphism. The spectral sequence collapses at $E_2$.
  1636	\end{theorem}
  1637	
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '2218,2268p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2218	weight-zero term from the OPE, which corresponds to
  2219	$W^{(s)}_{(s+t-1)} W^{(t)}$. This coefficient equals the
  2220	two-point function normalization up to a universal factor, and vanishes
  2221	by orthogonality:
  2222	\begin{equation}
  2223	W^{(s)}_{(s+t-1)} W^{(t)} = 0 \quad \text{for } s \neq t
  2224	\end{equation}
  2225	(For $s = 2$: $T_{(t+1)} W^{(t)} = 0$ since the $TW^{(t)}$ OPE has
  2226	at most a double pole when $W^{(t)}$ is primary.
  2227	For $s, t \geq 3$: the vanishing is a consequence of the orthogonality
  2228	and the associativity constraints of the $\mathcal{W}_N$
  2229	OPE~\cite{Bouwknegt-Schoutens}.)
  2230	
  2231	\emph{Step~3: Summation and B-cycle promotion.}
  2232	By Steps 1--2, the genus-0 curvature endomorphism is diagonal in the
  2233	generator basis, with eigenvalue $c/s$ on $W^{(s)}$. The total
  2234	genus-0 vacuum leakage is:
  2235	\begin{equation}
  2236	m_0^{\mathrm{total}} = \sum_{s=2}^{N} \frac{c}{s}
  2237	= c \cdot (H_N - 1)
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21755,21885p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 21755	 \delta F_2(\cW_3) \;=\; \frac{3}{c} + \frac{9}{2c}
 21756	 + \frac{1}{16} + \frac{21}{4c}
 21757	 \;=\; \frac{c + 204}{16c},
 21758	 \end{equation}
 21759	 the first closed-form cross-channel correction at
 21760	 genus\/~$\geq 2$
 21761	 \textup{(}Computation~\textup{\ref{comp:w3-genus2-multichannel}}).
 21762	\end{enumerate}
 21763	In particular, the scalar formula
 21764	$F_g(\cA) = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$
 21765	holds at all genera if and only if\/~$\cA$ is uniform-weight or
 21766	$\delta F_g^{\mathrm{cross}}(\cA) = 0$ at each genus
 21767	individually. For $\cW_3$ the scalar formula
 21768	\emph{fails} at $g = 2$: the cross-channel correction
 21769	$\delta F_2 = (c{+}204)/(16c) \neq 0$ for all finite central
 21770	charge. This resolves Open
 21771	Problem~\textup{\ref{op:multi-generator-universality}} in
 21772	the negative.
 21773	\end{theorem}
 21774	


thinking
**Exploring the theorem**

I'm thinking about a theorem mentioned in line 2876, which relates to the origin of fiberwise curvature. I note that it states "dfib^2 = ...", but I realize the theorem focuses on forms rather than algebra-specific coefficients. That said, maybe it would be sufficient if I combine this information with the Operator Product Expansion (OPE). I wonder how the two could complement each other, and I should explore this further to clarify.
thinking
**Inspecting quantum theorem proof**

I need to read relevant portions surrounding the theorem about quantum Arnold relations and see if it can indeed generalize to all g. I should check the lines after 2905 to focus on the proof, especially since it might only address the genus 1 case. There’s a lot to inspect here, so careful examination will help clarify whether it supports line 5318. Let’s dive in and find the information we need!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2905,2998p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2905	\begin{proof}[Genus $1$ case]
  2906	Consider the elliptic curve $E_\tau$ with $\tau \in \mathbb{H}$ (upper half-plane). Use the Weierstrass $\zeta$-function:
  2907	\begin{equation}
  2908	\zeta(z|\tau) = \frac{1}{z} + \sum_{(m,n) \neq (0,0)} \left[\frac{1}{z - \omega_{mn}} + \frac{1}{\omega_{mn}} + \frac{z}{\omega_{mn}^2}\right]
  2909	\end{equation}
  2910	where $\omega_{mn} = m + n\tau$.
  2911	
  2912	The quasi-periodicity is:
  2913	\begin{align}
  2914	\zeta(z + 1|\tau) &= \zeta(z|\tau) + 2\eta_1(\tau)\\
  2915	\zeta(z + \tau|\tau) &= \zeta(z|\tau) + 2\eta_\tau(\tau)
  2916	\end{align}
  2917	with the Legendre relation:
  2918	\begin{equation}
  2919	\tau \eta_1 - \eta_\tau = \pi i
  2920	\end{equation}
  2921	
  2922	The holomorphic form $\zeta(z_{ij}|\tau)\,dz_i$ is quasi-periodic and therefore not globally defined on~$E_\tau$. The single-valued propagator on the elliptic curve is \textup{(}g=1 only, so the period matrix is the $1\times 1$ matrix $\Omega = (\tau)$\textup{)}:
  2923	\begin{equation}\label{eq:genus-1-propagator-full}
  2924	\eta_{ij}^{(1)} = \left[\zeta(z_{ij}|\tau) + \frac{\pi}{\mathrm{Im}(\tau)}\,\mathrm{Im}(z_{ij})\right](dz_i - dz_j)
exec
/bin/zsh -lc "rg -n -F '\\label{constr:cross-channel-graph-sum}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{comp:w3-genus2-multichannel}' chapters/theory/higher_genus_modular_koszul.tex chapters/examples chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:algebraic-family-rigidity}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21495,21655p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21885,22025p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:22055:\label{constr:cross-channel-graph-sum}
chapters/theory/higher_genus_modular_koszul.tex:22055:\label{constr:cross-channel-graph-sum}
 succeeded in 51ms:
chapters/examples/w_algebras.tex:5698:\label{comp:w3-genus2-multichannel}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:8953:\label{thm:algebraic-family-rigidity}
chapters/theory/higher_genus_modular_koszul.tex:8953:\label{thm:algebraic-family-rigidity}
 succeeded in 52ms:
 21495	via $\eta^{-1} \in \cA \otimes \cA$;
 21496	leave the $n$~external outputs as multilinear functionals on~$\cA$.
 21497	The scalar trace
 21498	$\operatorname{tr}_{\mathrm{cyc}} \colon
 21499	(\cA^*)^{\otimes n}_{\mathrm{cyc}} \to \mathbb{C}$
 21500	recovers the shadow tautological classes:
 21501	\begin{equation}\label{eq:phi-trace-recovery}
 21502	\tau_{g,n}(\cA)
 21503	\;=\;
 21504	\operatorname{tr}_{\mathrm{cyc}}
 21505	\bigl(\Phi_{\cA}^{(g,n)}(\Theta_\cA)\bigr)
 21506	\;\in\; R^*(\overline{\mathcal{M}}_{g,n+1}).
 21507	\end{equation}
 21508	\end{construction}
 21509	
 21510	\begin{theorem}[Shadow cohomological field theory]
 21511	\label{thm:shadow-cohft}
 21512	\ClaimStatusProvedHere
 21513	\index{cohomological field theory!shadow CohFT|textbf}
 21514	\index{Chriss--Ginzburg principle!CohFT structure}
 succeeded in 52ms:
 21885	(factorization structure, metric orthogonality, ghost-number
 21886	conservation) converge on the identical conclusion is the
 21887	signature of a structural inevitability. The vanishing of
 21888	$\delta F_g^{\mathrm{cross}}$ for free fields is not an
 21889	algebraic accident but a consequence of the factorization
 21890	geometry of the free-field OPE: the quadratic vertex has no room
 21891	to couple distinct weight sectors, regardless of which language
 21892	one uses to express this constraint.
 21893	
 21894	\smallskip\noindent
 21895	\emph{Mechanism~\textup{1}: class~$\mathsf{G}$ factorization
 21896	\textup{(}shadow-tower collapse\textup{)}.}
 21897	For free fields of class~$\mathsf{G}$ (Heisenberg, lattice),
 21898	the shadow tower terminates at degree~$2$
 21899	\textup{(}Theorem~\textup{\ref{thm:shadow-archetype-classification}(i)}\textup{)}.
 21900	Because $m_k = 0$ for $k \geq 3$, every genus-$0$ vertex in the
 21901	stable-graph expansion is binary: the bar differential is
 21902	purely deconcatenation, so the only surviving graphs are
 21903	trees-of-loops with no higher-valence vertices. Each edge
 21904	contributes on its own quadratic block, and the graph weight

thinking
**Evaluating theorem stability**

I need to check the theorem multi-weight-genus-expansion proof, specifically looking at shadow-channel-decomposition, which might have issues. I should verify if it’s in the same file and possibly incorrect. There’s a claim about independent components that seems to imply instability. However, the user wants a proof for Theorem D, so I might just need enough information to decide if a complete audit is necessary. I can also investigate the computation related to W3 for more context.
codex
The multi-weight correction is not just a caveat in prose anymore: there is a dedicated theorem with an explicit `\mathcal W_3` genus-2 correction. I’m reading that computation now to see whether it genuinely establishes nonzero `\delta F_2^{\mathrm{cross}}` or merely assumes the channel decomposition it cites.
exec
/bin/zsh -lc "rg -n -F 'cor:scalar-saturation' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14136,14214p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5668,5738p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '8928,9008p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'prop:saturation-equivalence' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:5949:(Corollary~\ref{cor:scalar-saturation}).
chapters/theory/higher_genus_modular_koszul.tex:3317:(Corollary~\ref{cor:scalar-saturation}).
chapters/theory/higher_genus_modular_koszul.tex:3810:(Corollary~\ref{cor:scalar-saturation}),
chapters/theory/higher_genus_modular_koszul.tex:7815:\label{cor:scalar-saturation}
chapters/theory/higher_genus_modular_koszul.tex:7953:Corollary~\ref{cor:scalar-saturation} gives only the one-channel
chapters/theory/higher_genus_modular_koszul.tex:7977:Corollary~\textup{\ref{cor:scalar-saturation}} extends at the level
chapters/theory/higher_genus_modular_koszul.tex:8005:The same argument as Corollary~\ref{cor:scalar-saturation} then
chapters/theory/higher_genus_modular_koszul.tex:8280:(i)~KM with simple~$\mathfrak{g}$ (Corollary~\ref{cor:scalar-saturation});
chapters/theory/higher_genus_modular_koszul.tex:14441:Corollary~\ref{cor:scalar-saturation} therefore places the minimal
chapters/theory/higher_genus_modular_koszul.tex:14454:Corollary~\ref{cor:scalar-saturation} then forces
 succeeded in 50ms:
 14136	\begin{theorem}[Shadow channel decomposition; \ClaimStatusProvedHere]
 14137	\label{thm:shadow-channel-decomposition}
 14138	\index{shadow obstruction tower!channel decomposition|textbf}
 14139	\index{shadow algebra!multi-channel decomposition}
 14140	Let $\cA$ be a modular Koszul chiral algebra with
 14141	$\dim H^2_{\mathrm{cyc}}(\cA, \cA) = r$ and basis
 14142	$\eta_1, \ldots, \eta_r \in H^2_{\mathrm{cyc}}$.
 14143	The shadow obstruction tower decomposes into $r$ independent
 14144	one-channel components:
 14145	\begin{equation}\label{eq:shadow-channel-decomposition}
 14146	\Theta_{\cA}
 14147	\;=\; \sum_{i=1}^r \kappa_i \cdot \Theta_{\eta_i}
 14148	\end{equation}
 14149	where each $\Theta_{\eta_i}$ is an independent MC element in
 14150	$\Defcyc(\cA) \widehat\otimes \Gmod$, solving its own MC equation
 14151	\begin{equation}\label{eq:per-channel-mc}
 14152	[\dzero, \Theta_{\eta_i}]
 14153	+ \tfrac{1}{2}[\Theta_{\eta_i}, \Theta_{\eta_i}]
 14154	\;=\; 0
 14155	\end{equation}
 succeeded in 50ms:
  5668	\end{equation}
  5669	The general term is
  5670	\begin{equation}\label{eq:w3-wline-general-term}
  5671	S_{2n}^W
  5672	\;=\;
  5673	\frac{a_n}{c^{2n-3}\,(5c{+}22)^{3(n-1)}}
  5674	\end{equation}
  5675	where $a_n = (-12)^n \binom{3/2}{n}/54$ are integers satisfying
  5676	$|a_n| = 1, 2, 9, 54, 378, 2916, 24057, \dots$
  5677	\textup{(}$n = 2, 3, \dots$\textup{)}.
  5678	\end{proposition}
  5679	
  5680	\begin{proof}
  5681	The $W$-line has $\alpha = 0$ (cubic vanishes by $\mathbb{Z}_2$~parity)
  5682	and $S_4^W = 2560/[c(5c{+}22)^3]$. The shadow metric on this
  5683	line is $Q_W(t) = (2\kappa_W)^2 + 2\Delta_W\,t^2$ with
  5684	$\Delta_W = 20480/[3(5c{+}22)^3]$, and the MC recursion
  5685	$f^2 = Q_W$ produces $S_{2n}^W$ as a polynomial in $S_4^W/c$
  5686	because all odd-degree terms vanish. The ring
  5687	relation~\eqref{eq:w3-wline-ring} follows from the explicit
 succeeded in 51ms:
  8928	decomposes this tangent space into the \emph{level direction}
  8929	$\mathbb{C}\cdot\eta$ (the one-dimensional orbit of the current
  8930	subalgebra, parameterized by~$\kappa$) and the \emph{primitive
  8931	directions} $H^2_{\mathrm{cyc,prim}}$. The strong scalar formula
  8932	$\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ is
  8933	strictly stronger than vanishing of the primitive tangent space.
  8934	What Theorem~\ref{thm:algebraic-family-rigidity} proves for
  8935	algebraic families is only that the MC moduli is
  8936	\emph{infinitesimally} a line in the cyclic direction: the
  8937	primitive tangent space vanishes and
  8938	$\Theta_{\cA}^{\min} = \eta \otimes \Gamma_{\cA}$ for some
  8939	tautological coefficient~$\Gamma_{\cA}$.
  8940	At generic level, Kazhdan--Lusztig semisimplicity kills
  8941	$H^2_{\mathrm{cyc,prim}}$
  8942	(Corollary~\ref{cor:effective-quadruple}).
  8943	At admissible levels, the module category is non-semisimple, and
  8944	the question becomes: \emph{does the MC moduli remain
  8945	one-dimensional, and does the corresponding coefficient equal
  8946	$\kappa\Lambda$?}
  8947	Theorem~\ref{thm:algebraic-family-rigidity} answers only the first
 succeeded in 50ms:
chapters/theory/higher_genus_foundations.tex:5694:parity (Proposition~\ref{prop:saturation-equivalence}), so the
chapters/theory/higher_genus_modular_koszul.tex:8270:Proposition~\ref{prop:saturation-equivalence}
chapters/theory/higher_genus_modular_koszul.tex:8335:\label{prop:saturation-equivalence}
chapters/theory/higher_genus_modular_koszul.tex:8518:Proposition~\ref{prop:saturation-equivalence} is exactly the
chapters/theory/higher_genus_modular_koszul.tex:8599:Proposition~\ref{prop:saturation-equivalence}(ii)$\Rightarrow$(i)
chapters/theory/higher_genus_modular_koszul.tex:8727:criterion of Proposition~\ref{prop:saturation-equivalence}\,(ii),
chapters/theory/higher_genus_modular_koszul.tex:8754:By Proposition~\ref{prop:saturation-equivalence}(ii)$\Rightarrow$(i),
chapters/theory/higher_genus_modular_koszul.tex:8915:Proposition~\ref{prop:saturation-equivalence}(ii)$\Rightarrow$(i).
chapters/theory/higher_genus_modular_koszul.tex:9058:Proposition~\ref{prop:saturation-equivalence}(ii)$\Rightarrow$(i)
chapters/theory/higher_genus_modular_koszul.tex:9371:\textup{(}Proposition~\textup{\ref{prop:saturation-equivalence}}\textup{)}:
chapters/theory/higher_genus_modular_koszul.tex:9401:(Proposition~\ref{prop:saturation-equivalence}).







thinking
**Evaluating theorem implications**

I need to consider if the theorem regarding modular characteristic suggests that κ=0 indicates A is at a critical level, particularly without any family restriction. It seems like a crucial point, but I’m not quite sure if I’m interpreting this right. I’ll have to weigh the implications carefully, and I want to ensure my reasoning is sound, so I'm pondering possible interpretations and their consequences.
thinking
**Identifying discrepancies in terminology**

I’m realizing that calling it "strong scalar ansatz" seems to be outdated terminology. There’s a genuine discrepancy here that I need to clarify. I also see that the theorem regarding modular characteristics at lines 2652-2654 references multi-generator higher-genus, and it’s conditional on that strong scalar ansatz. I’m thinking it’s important to ensure clarity around this term in future discussions!
thinking
**Evaluating theorem accuracy**

This is serious. I need to classify the issue, possibly as high, because the theorem’s statement misrepresents its scope and status. I should check if there’s another theorem with the same label. It seems the genus-universality and modular-characteristic theorem cites outdated wording linking to a now-negative theorem as if it's a positive statement. That’s a significant finding. This misalignment means the theorem’s statement isn’t in sync with the current theorem, which could lead to misunderstandings about its scope.
thinking
**Reviewing theorem definitions**

I should note that lines 2508-2516 accurately define the scalar lane, referencing the multi-weight-genus-expansion theorem, which provides cross-correction and free-field exceptions. However, the genus-universality theorem's statement seems inconsistent with this definition. I need to check the completeness of the modular-characteristic proof, as it routes back to genus-universality. 

There's also a concern with part (ii), because it labels the generating function as UNIFORM-WEIGHT, but part (i) incorrectly states conditions that could lead to circularity in the proof. This needs careful attention due to potential issues in its arguments.
thinking
**Analyzing fiber pushforward**

For genus g≥2, when considering the pushforward of a (1,1)-form on the fiber along the universal curve, it results in a degree 0 class on the base instead of λ_g. I need to think through this carefully. The proof mentions that "Its B-cycle quasi-periodicity produces the fiberwise Arakelov curvature ω_g, whose pushforward gives c1(E) on moduli" at lines 5316-5317. I want to ensure I'm understanding the implications of this correctly for the overall proof.
thinking
**Evaluating theorem definitions**

I need to check if the theorem about family-index in Step 1 uses genus-universality to define D_A and derive family-index, which seems circular. There’s a potential issue with the theorem's mod characteristic part concerning duality for W-algebras, relying on genus-universality(ii) from higher_genus_foundations that cites genus-1 only wn-obstruction. I should verify the W_N formula at N=2 and N=3; it looks correct. There's also a concern with theorem genus-universality, proof lines about multi-generator algebras, which might not substantively prove the conditional claim.
thinking
**Inspecting theorem details**

I need to check if the `thm:modular-characteristic` part (i) relates to `obs_g` classes or `F_g` numerical free energies. It mentions a cohomological `obs_g` formula and generating function `F_g`, which seems fine. However, there might be a potential issue with Theorem D, where the formula `obs_g = κ λ_g` applies uniformly across weights. I should clarify these points to ensure everything aligns properly with the intended definitions and implications.
codex
I’ve confirmed one hard defect already: the proof of `thm:genus-universality` invokes `thm:family-index`, and `thm:family-index` in turn starts from `thm:genus-universality`. That is a direct circular dependency on the load-bearing step from fiberwise curvature to the global `\lambda_g` formula.
exec
/bin/zsh -lc "rg -n -F 'thm:genus-universality' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'obs}_g(\\cA) = \\kappa(\\cA)\\cdot\\lambda_g' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'delta F_g"'^{'"\\mathrm{cross}}' /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:33:\phantomsection\label{thm:genus-universality}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4168: (Theorem~\ref{thm:genus-universality}),
/Users/raeez/chiral-bar-cobar-vol2/main.tex:624:\phantomsection\label{V1-thm:genus-universality}%
/Users/raeez/chiral-bar-cobar-vol2/main.tex:712:\phantomsection\label{thm:genus-universality}%
/Users/raeez/calabi-yau-quantum-groups/notes/physics_anomaly_cancellation.tex:7:% thm:anomaly-koszul, cor:kappa-additivity, thm:genus-universality,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1304:(Theorem~\ref*{V1-thm:genus-universality},
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1710:\textup{(}Volume~I, Theorem~\textup{\ref*{V1-thm:genus-universality}}\textup{)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2541:(Theorem~\ref*{V1-thm:genus-universality}):
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:164:\textup{(}Theorem~\textup{\ref{thm:genus-universality}};
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1114: & \checkmark\;Thm~\ref{thm:genus-universality} \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1249:(uniform-weight), Theorem~\ref{thm:genus-universality}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/holomorphic_topological.tex:1410: (Theorem~\ref{thm:genus-universality};
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1686:Theorem~\ref{V1-thm:genus-universality} gives
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:2185:(Theorem~\ref{V1-thm:genus-universality}). The factor $1/2^g$ accounts
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:478:Theorem~\ref{V1-thm:genus-universality}) with the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:810:Theorem~\ref{V1-thm:genus-universality}\textup{(iii)}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:1816:Part~(ii) is Theorem~\ref{V1-thm:genus-universality}\textup{(iii)} on the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex:272:(Theorem~\ref{V1-thm:genus-universality}).
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/working_notes.tex:3124: $\delta F_g^{\mathrm{cross}} = 0$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2206: genera \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$; Vol~I)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2644:at each genus \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2798:receives cross-channel corrections $\delta F_g^{\mathrm{cross}}$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2812:$\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ \textup{(all-weight; Vol~I)}.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3590: $F_g = \kappa_{\mathrm{ch}}\,\lambda_g^{\mathrm{FP}}$ \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4359:\quad \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$)},
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:4678:$F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$, all-weight with cross-channel correction $\delta F_g^{\mathrm{cross}}$) and what it
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5217: \item At genus~$g \geq 2$: $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}} = 2 \cdot \lambda_g^{\mathrm{FP}}$ (all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$) captures the tautological class contribution, while the full genus-$g$ GW invariant receives additional contributions from higher BPS states $n_h^g$ with $g \leq h$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:8:This chapter replaces the wrong identification by the right one. The CY trace, properly refined to negative cyclic homology $\HC^-_d(\cC)$, determines $\kappa_{\mathrm{ch}}(A_\cC)$ through the CY-to-chiral functor $\Phi$. The resulting equality $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is a statement about the CY Euler characteristic of the category, which in general differs from the topological Euler characteristic of the underlying manifold. The genus-$g$ obstruction tower $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ then encodes the higher-genus CY invariants on the uniform-weight lane, with the multi-weight cross-channel correction $\delta F_g^{\mathrm{cross}}$ from Vol~I appearing at $g \geq 2$ for families with fields of distinct conformal weights.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:28: \item The genus-$g$ obstruction satisfies $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ on the uniform-weight lane; unconditionally at genus~$1$ for all families (Vol~I, Theorem~D); at genus $g \geq 2$ for multi-weight algebras, the scalar formula receives a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$ (Vol~I, op:multi-generator-universality, resolved negatively; $\delta F_2(\mathcal{W}_3) = (c{+}204)/(16c) > 0$);
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:85:at genus $g \geq 2$ for multi-weight algebras the scalar formula receives a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$ (ALL-WEIGHT, with cross-channel correction $\delta F_g^{\mathrm{cross}}$).
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:109:where $K$ is the Koszul conductor and $\rho$ the anomaly ratio; this holds only on the \emph{uniform-weight lane} (all generators of $A$ of equal conformal weight), and at $g \geq 2$ multi-weight algebras incur a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$. This section transports both statements to CY categories via the functor $\Phi$.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:178:Three independent obstructions block upgrading Conjecture~\ref{conj:cy-complementarity-d3} to a theorem: (a) AP-CY6, the chiral algebra $A_X$ is not constructed at $d = 3$; (b) the uniform-weight hypothesis fails for compact CY$_3$ (chiral de Rham is multi-weight, so gives $\delta F_g^{\mathrm{cross}} \neq 0$ at $g \geq 2$); (c) the BKM automorphic correction at $d = 3$ generates infinitely many imaginary root generators (\S\ref{sec:cy-shadow-cohft} below), so even stating the Koszul conductor $K_X$ requires resolving the degree-$r$ shadow identification of theory\_automorphic\_shadow.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:342:For the full $\cN = 4$ algebra (multi-weight, generators at conformal weights $\{1/2, 1, 3/2, 2\}$), the scalar formula acquires a correction $\delta F_g^{\mathrm{cross}} \neq 0$ at $g \geq 2$ (ALL-WEIGHT, with cross-channel correction).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:196:the cross-channel correction $\delta F_g^{\mathrm{cross}}$ of Vol~I,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1415:where $\lambda_g^{\mathrm{FP}}$ is the Faber--Pandharipande tautological intersection number on $\overline{\mathcal{M}}_g$. At $g \geq 2$ with multi-weight input, the scalar formula fails and requires the cross-channel correction $\delta F_g^{\mathrm{cross}}$ of Vol~I.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1443:\item \emph{Uniform-weight vs.\ multi-weight.} At genus $g \geq 2$, the scalar formula $F_g = \kappa_{\mathrm{ch}} \cdot \lambda_g^{\mathrm{FP}}$ holds on the uniform-weight lane (Vol~I, Theorem~D). For CY$_3$ chiral algebras with generators of multiple conformal weights, the cross-channel correction $\delta F_g^{\mathrm{cross}} \neq 0$ modifies the higher-genus free energies. The full DT free energies require these corrections.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:909:$\delta F_g^{\mathrm{cross}} \ne 0$
 exited 1 in 53ms:

exec
/bin/zsh -lc "rg -n -F 'strong scalar ansatz' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5259:extension is conditional on the strong scalar ansatz of
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2653: strong scalar ansatz
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2699:strong scalar ansatz of
/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:1:r"""Conditional bookkeeping for the strong scalar ansatz.
/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:24:  3. Conditional free-energy formulas under the strong scalar ansatz
/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:104:    r"""Per-channel genus-g free energy under the strong scalar ansatz.
/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:117:    Under the strong scalar ansatz:
/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:191:    # under the strong scalar ansatz.
/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:319:    arithmetic consequences of assuming the strong scalar ansatz.
/Users/raeez/chiral-bar-cobar/compute/tests/test_multichannel_universality.py:1:r"""Conditional test suite for the strong scalar ansatz.
/Users/raeez/chiral-bar-cobar/compute/tests/test_multi_generator_universality.py:21:conditional on the strong scalar ansatz.
exec
/bin/zsh -lc "rg -n -F '\\label{def:higher-genus-log-forms}' chapters/theory/higher_genus_foundations.tex && nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2808,2858p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2829:\label{def:higher-genus-log-forms}
  2808	There exists a universal curve:
  2809	\begin{equation}
  2810	\pi: \overline{\mathcal{C}}_{g,n+1} \to \overline{\mathcal{M}}_{g,n}
  2811	\end{equation}
  2812	such that:
  2813	\begin{itemize}
  2814	\item The fiber over $[(\Sigma_g; p_1, \ldots, p_n)]$ is $\Sigma_g$ with $n$ marked points removed
  2815	\item Sections $\sigma_i: \overline{\mathcal{M}}_{g,n} \to \overline{\mathcal{C}}_{g,n+1}$ give the marked points
  2816	\item The relative dualizing sheaf $\omega_\pi = \omega_{\overline{\mathcal{C}}_{g,n+1}/\overline{\mathcal{M}}_{g,n}}$ is relatively ample
  2817	\end{itemize}
  2818	
  2819	The configuration space sits in this fibration:
  2820	\begin{equation}
  2821	\overline{C}_n(\Sigma_g) \subset \overline{\mathcal{C}}_{g,n+1}^{(n)} \to \overline{\mathcal{M}}_{g,n}
  2822	\end{equation}
  2823	where the superscript $(n)$ denotes the $n$-fold fiber product over $\overline{\mathcal{M}}_{g,n}$.
  2824	\end{theorem}
  2825	
  2826	\subsection{Logarithmic forms at higher genus}







thinking
**Navigating mathematical proofs**

I'm noticing that the inconsistency here impacts the "same Hodge bundle on every edge" argument. If the propagator weight structure gets confused, that weakens the proof's weight-uniformity step, which is concerning. I need to carefully ground this in my files and consider inspecting certain theorems to check for circularity. The Kac-Moody proof and Vir theorem seem interlinked, but it looks like the generality might not apply to all cases. Maybe I could even read the `obstruction-general` theorem for clarity.
thinking
**Exploring critical issues**

I’m spotting a potential critical issue with `thm:family-index` being in the concordance chapter. According to the chapter's introduction, if there’s a disagreement among chapters, this one takes precedence. That raises questions about how this discord affects the overall argument or framework being established. I should explore this further to clarify how this may impact my current understanding or application of the theorems at hand. It's essential to get this right!
thinking
**Evaluating theorem proofs**

I’m thinking about how the use of certain theorems in proving others feels a bit strange, especially when it leads to circular proofs. For the theorem about universal-generating-functions, it relies on complementarity-genus-series, but I need to check if this proposition stands alone or ties back to the genus-universality theorem. The F1 sanity check focusing on the x² coefficient seems fine, but I wonder about modular-characteristic proof requirements. I might need to verify the independence of `cor:kappa-additivity` in V1, but perhaps that’s not really necessary.
thinking
**Analyzing theorem details**

I see there might be a potential issue with the modular-characteristic theorem, specifically part (iii), which mentions the W algebra duality constant `K_fg` being linked to the Feigin-Frenkel central-charge sum. I'm considering that the genus-universality theorem indicates `kappa = 0` at critical levels, possibly hinting that `c=0` is relevant for W-algebras. Furthermore, the proof’s reference to multi-generator algebras suggests consistency in contributions, while cross-channel corrections are noted later, which don't seem contradictory. I need to remember that the strong scalar ansatz is outdated in this context.
thinking
**Reviewing theorem remarks**

I see that the definition of scalar lane is already updated, but I might need to mention this as a downstream drift. It feels necessary to check whether the genus-universality or modular-characteristic theorems around lines 5257-5260 and 2650-2654 conflict with remarks made nearby in lines 5463-5485 and the statement of theorem 21681. This could clarify any inconsistencies, so I’ll want to search and compare those sections carefully to ensure everything aligns correctly.
thinking
**Inspecting theorems and definitions**

I need to look more closely at whether the theorem modular-characteristic part (i) or the scalar lane definition uses "obs_g" versus free energy. The genus-universality theorem uses the `obs_g` class formula, which seems fine. I’m noticing a potential issue with line 5323 of the genus-universality proof regarding uniform-weight assumptions. If every edge uses the standard Hodge bundle, then that’s not distinguishing. I’m also thinking about the potential problems with the `shadow-channel-decomposition` proof and the role of non-abelian OPE. It might be worth checking if the `conformal-bootstrap-rigidity` theorem states that.
thinking
**Evaluating multi-weight dependencies**

The user is asking whether multi-weight truly needs the delta_F cross. I think we can argue that there’s an independent W3 computation, which could serve as extra evidence. If this computation doesn’t heavily rely on decomposition, it might come from stable graphs with T/W assignments, suggesting it could be independent enough. I need to inspect the W3 genus-2 continuation and look for explicit nonzero values, which could support the necessity of the delta. I’ll continue from line 5738 onward.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5738,5798p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5738	The remaining three graphs (smooth, figure-eight, dumbbell) have
  5739	at most one edge or have vanishing mixed amplitudes.
  5740	The total cross-channel correction is
  5741	\begin{equation}\label{eq:w3-cross-channel-genus2}
  5742	\delta F_2(\mathcal{W}_3)
  5743	= \frac{c + 204}{16c}.
  5744	\end{equation}
  5745	This decomposes as
  5746	$\delta F_2 = 1/16 + 51/(4c)$:
  5747	the constant $1/16$ from the lollipop (c-independent, from a
  5748	genus-$1$ vertex times a genus-$0$ vertex), the rational
  5749	$15/(2c)$ from the banana and theta graphs, and
  5750	$21/(4c)$ from the barbell. At large~$c$,
  5751	$\delta F_2 \to 1/16$; the cross-channel correction is a
  5752	$O(1)$ perturbation of the scalar $F_2 \sim 7c/6912$, hence
  5753	$\delta F_2/F_2 \sim 432(c{+}204)/(7c^2) \to 0$.
  5754	
  5755	\smallskip\noindent\emph{Banana universality.}
  5756	The genus-$0$ quartic vertex $V_{0,4}(i,i,j,j) = 2c$ for all
  5757	channel assignments $(i,j) \in \{T,W\}^2$, because











thinking
**Identifying algebraic gaps**

I realize that I've made an error: the algebraic-family-rigidity theorem doesn’t identify Γ or eliminate delta. That’s definitely a significant gap. I’m also starting to think that the multi-weight-genus-expansion theorem, part (iv), might not even be necessary to establish a nonzero delta for W3 or in the case of genus1 unconditional. It's interesting to see how these components connect!
thinking
**Considering theorem issue**

I'm noticing a potential issue with the theorem related to shadow-channel decomposition that says on line 14165 that conformal bootstrap rigidity forces r to equal 1 for non-abelian operator product expansions (OPE). I wonder if there's a deeper implication or if I might be misunderstanding the context here. I think I should review the relevant literature to clarify this point and ensure I fully grasp its significance in the field.
thinking
**Considering mathematical examples**

I see that for the Virasoro, it's c/2, which sounds good. For W_N at g=1, I have κ = c(H_N - 1), and when N=2, it also gives c/2. That's great! But wait, I'm wondering if there could be a counterexample at those boundary values? It’s something to think about. I’ll need to explore that further to make sure I’m not missing anything important.
thinking
**Evaluating findings step by step**

I think I need to evaluate my findings part by part. Instead of narrating each step, I could order the findings by severity while considering whether to include open questions. Including a summary might be helpful, and I should count instances checked, potentially around 15. I'll continue inspecting the theorem on line 5241 regarding genus-universality. I've already identified some issues, such as circular references and possible inconsistencies. I'll also consider looking into some specific theories, but I’m unsure if it's necessary.
thinking
**Identifying potential issues**

I see a potential issue with the theorem regarding the modular characteristic. It mentions that `obs_g` factors into `H^{2g}(\overline{M}_g)` for all g≥1, which is uniform-weight and unconditional at g=1. However, I notice that λ_g is defined only for g≥1 on \overline{M}_g. This is interesting, especially since the genus-universality statement on line 5255 uses a local tag (LOCAL). While it's odd, I wonder if this is really a violation or just a quirk.
thinking
**Exploring K-theory nuances**

I'm thinking about how multiplying a K-theory class by a complex scalar leads to results that don’t fall within K_0 ⊗ Q. This raises questions about the implications of this operation and how it interacts with the structures involved. I wonder what this means for further analysis. It's definitely a concept that seems intricate and invites deeper thought into the relationships between K-theory classes and scalar multiplication.
thinking
**Examining mathematical inconsistencies**

I’m noticing a potential inconsistency here involving the theorem related to κ(A). They mentioned the modular deformation complex, and there might be issues if κ is not rational. I wonder if expanding coefficients to C could help, even though they specified Q. There's also a notable discrepancy regarding the family-index theorem, which could impact its proof and possibly relate to the coefficient-ring mismatch. It’s a genuine concern I should address in the response!
thinking
**Assessing mathematical proofs**

I’m spotting some circularity in Step 1, and the coefficient ring mismatch seems significant. There's a potential conflict with the genus-universality theorem, particularly regarding the propagator's formula—it's not aligning with previous definitions. I should consider if I need to gather four findings. I'm also checking if the quantum-arnold-relations state gives a consistent formula for curvature and how that relates to the first Chern. It seems plausible, but I need to clarify the overall scope regarding genus and weight!
thinking
**Clarifying Theorem D**

I’m thinking about Theorem D, which applies uniform weight for all genera, but only provides unconditional results for g=1. For g≥2, it needs cross-correction instead of a straightforward scalar formula, particularly for free fields. However, I notice that the theorem's wording is somewhat stale, leading to internal inconsistencies regarding its scope. This is definitely something that needs to be addressed for clarity's sake. Let's ensure everything aligns properly!
thinking
**Examining theoretical notation**

I’m considering whether the statement in `chapters/theory/higher_genus_modular_koszul.tex` around line 2637, which mentions the "scalar modular characteristic package (Definition def:scalar-modular-package)," needs an existing label. It’s a bit of a technical point and I’m wondering if it’s necessary to label it or if it can stand on its own. Let's see if clarity would improve by adding a label, but I think it's an optional step.
thinking
**Evaluating computation aspects**

I’m considering whether I need to inspect the `compute/tests` or compute modules. The user mentioned they only want to read/report on the chapters directory, but there might be a connection to second-order notes regarding the old scalar ansatz surfaces in the compute layer. Since they asked about downstream propagation, this issue seems relevant, especially with files like `compute/lib/multichannel_universality.py`. I’m thinking I should quickly check the top lines in those compute files to see if there’s stale data.
codex
I’ve finished the proof surface and I’m checking propagation. There is internal theorem drift in the text already; now I’m confirming whether the same stale “strong scalar ansatz” language is still present in dependent compute surfaces.
exec
/bin/zsh -lc "nl -ba compute/lib/multichannel_universality.py | sed -n '1,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_multi_generator_universality.py | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_multichannel_universality.py | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	r"""Conditional bookkeeping for the strong scalar ansatz.
     2	
     3	What is proved in the manuscript after rectification:
     4	  - genus-1 universality: obs_1(A) = κ(A) · λ_1 for every modular
     5	    Koszul algebra
     6	  - uniform-weight all-genera scalar package
     7	  - algebraic-family rigidity only gives the weaker statement
     8	        Θ_A^{min} = η ⊗ Γ_A
     9	    with the cyclic direction fixed but the tautological coefficient
    10	    Γ_A still undetermined in general multi-weight families.
    11	
    12	This module keeps the exact arithmetic consequences of the stronger
    13	ansatz
    14	
    15	    Θ_A^{min} = κ(A) · η ⊗ Λ,   Λ = Σ_{g≥1} λ_g
    16	
    17	for W_N-style families.  Those consequences are useful as bookkeeping
    18	and for conditional comparisons, but they are NOT a proof that
    19	obs_g = κ(A) · λ_g holds for all multi-generator algebras.
    20	
 succeeded in 52ms:
     1	r"""Test suite for multi-generator genus universality.
     2	
     3	MATHEMATICAL CONTEXT:
     4	For multi-generator chiral algebras like W_3 (generators T of weight 2, W of weight 3),
     5	the genus-1 obstruction is obs_1 = kappa * lambda_1 with
     6	kappa = sum_i kappa_{h_i}, using the STANDARD Hodge bundle
     7	E_1 = R^0 pi_* omega for ALL channels.
     8	
     9	WHAT THIS FILE ACTUALLY ESTABLISHES:
    10	The bar complex propagator is d log E(z,w), where E(z,w) is the prime form.
    11	The prime form is a section of K^{-1/2} boxtimes K^{-1/2}, so d log E = dE/E
    12	has weight 1 in both variables, REGARDLESS of the conformal weight of the
    13	field being sewed (rem:propagator-weight-universality).
    14	
    15	The former obstruction decomposition obs_g = sum_j kappa_j * lambda_g^{(j)}
    16	was based on the incorrect assignment of weight-h generators to E_h.
    17	Since the propagator is weight 1, all channels use E_1.  This kills the
    18	false higher-weight Hodge-bundle story, but it does NOT by itself prove
    19	the stronger higher-genus identity F_g = kappa * lambda_g^FP for general
    20	multi-weight families.  The all-genera formulas tested below are therefore
 succeeded in 51ms:
     1	r"""Conditional test suite for the strong scalar ansatz.
     2	
     3	After rectification, the manuscript proves:
     4	  - genus-1 universality for every modular Koszul algebra
     5	  - the all-genera scalar package on the uniform-weight lane
     6	  - only level-direction concentration Θ^{min} = η⊗Γ_A in general
     7	    multi-weight families.
     8	
     9	These tests keep the exact arithmetic consequences of the stronger
    10	ansatz Θ^{min} = κ·η⊗Λ for W_N-style families.  They are useful as
    11	bookkeeping checks, but they do NOT resolve
    12	op:multi-generator-universality.
    13	
    14	COMPUTE TESTS:
    15	  - κ formulas for W_N (N = 2..8)
    16	  - Per-channel decomposition: Σ κ_s = κ
    17	  - Free energy universality: F_g = κ · λ_g^FP (g = 1..5)
    18	  - Idempotent trace condition for W_3
    19	  - Scalar saturation: minimal model has S_n = 0 for n ≥ 3
    20	  - Â-genus generating function agreement






thinking
**Evaluating critical findings**

I’m realizing that “κ c_g(E)” isn't a valid K-theoretic operation, which could strengthen my critical findings. I need to verify specific lines in the text, maybe mentioning circularity and invalid K-theory scaling together as a separate item. I should also check if the theorem's modular-characteristic proof is complete since it seems tiny but potentially important. It's a bit complicated, and I'll need to weigh the severity of different issues like critical false theorems and circular proofs.
thinking
**Identifying critical findings**

I’m considering issues like wrong formulas, scopes, and unstable dependencies—those seem high priority. I also see medium concerns with misleading prose and incomplete verifications. A critical finding relates to the theorem's genus-universality proof, which appears circular. It uses family-index assumptions inappropriately, which weakens the argument. I'll need to pinpoint file lines for both genus-universality and the family-index. For the user, I could provide references like "higher_genus_foundations.tex:5326" and "concordance.tex:6010" in a way that aligns with their request.
thinking
**Considering theorem details**

I might also want to point out that the theorem on modular-characteristic inherits from previous findings in lines 2695-2701. It could be helpful to make this a separate item or include it in my description for clarity. The proof for theorem D specifically relies on genus-universality, so I should ensure that connection is clear too. I want to make sure I'm presenting everything accurately for the user!
thinking
**Drafting findings summary**

I’m positively addressing the question but need some qualifications. I’ll count instances that were checked as 24 with 6 potential violations. If there's a low compute drift, we could consider it either 5 or 6 findings. So, I’ll go ahead with 6 findings. For the summary, I’m aiming to keep it under 50-70 lines, with 6 bullet points and 2 short paragraphs. I’ll format the file paths clearly, perhaps like `[CRITICAL] chapters/theory/higher_genus_modular_koszul.tex:2695 — ...`. That keeps it concise!
thinking
**Choosing file reference format**

The developer prefers clickable links for local files. I could use markdown links, like `[chapters/theory/higher_genus_modular_koszul.tex](/Users/.../higher_genus_modular_koszul.tex:2695)`. However, the contract specifies a format like `- [CRITICAL] file:line — description`. So, I might format it as `- [CRITICAL] [higher_genus_modular_koszul.tex](/Users/.../higher_genus_modular_koszul.tex:2695) — description`. For secondary references, I’ll keep them in plain relative lines, avoiding nested bullets. I also need to remember: no em dashes are allowed; I’ll use hyphens or semicolons instead!
thinking
**Finalizing report details**

I think it’s good to mention that there are “Violations found: 6.” I need to note that there were no false positives after re-verification; that will add clarity. So, I'll craft the final report with those 6 items and include short notes for each. Keeping it clear and concise is important here to ensure everything is understood properly. Let’s make sure the final document looks polished!
codex
- [CRITICAL] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2695) — Theorem D is not proved end-to-end as written. Its proof imports `thm:genus-universality`, but the load-bearing step there, [higher_genus_foundations.tex:5326](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5326), invokes `thm:family-index` to identify `\mathrm{obs}_g` with `\lambda_g`; the proof of `thm:family-index` then starts from `thm:genus-universality` at [concordance.tex:6010](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6010). This is a direct circular dependency on the main all-genera step.

- [HIGH] [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:5943) — Even ignoring the circularity, `thm:family-index` is ill-formed as a GRR argument. It defines `\mathcal D_\cA^{(g)} := \kappa(\cA)\cdot \mathbb E` inside `K_0(\overline{\mathcal M}_g)\otimes \mathbb Q`, although `\kappa(\cA)` is introduced as a complex scalar, and then concludes `c_g(\mathcal D_\cA^{(g)})=\kappa(\cA)c_g(\mathbb E)` at [concordance.tex:6020](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6020). That is not a valid K-theoretic/Chern-class operation.

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2650) — The scope note for multi-weight families is stale and now false on its own terms. It says the higher-genus extension is "conditional on the strong scalar ansatz of Theorem~`thm:multi-generator-universality`", but that label now points to the proved negative theorem [higher_genus_modular_koszul.tex:21681](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21681), which asserts `F_g=\kappa\lambda_g^{FP}+\delta F_g^{cross}` and gives explicit nonzero `\delta F_2(\mathcal W_3)`. The same stale wording also survives at [higher_genus_foundations.tex:5257](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5257).

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14172) — `thm:shadow-channel-decomposition` expands the Maurer-Cartan equation incorrectly: the linear term is written with `\kappa_i^2` instead of `\kappa_i`. Worse, even the corrected expansion would not show that arbitrary `\kappa_i\Theta_{\eta_i}` are Maurer-Cartan unless extra vanishing is proved. Since `thm:multi-weight-genus-expansion` uses this theorem in its diagonal reduction at [higher_genus_modular_koszul.tex:21796](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21796), the general multi-channel proof is not sound as written.

- [HIGH] [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21821) — `thm:multi-weight-genus-expansion` claims its uniform-weight clause needs no argument because it is `thm:algebraic-family-rigidity`, but that cited theorem explicitly stops short of identifying `\Gamma_\cA` with `\kappa(\cA)\Lambda`; see [higher_genus_modular_koszul.tex:8980](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:8980). So the advertised reason for `\delta F_g^{cross}=0` on the uniform-weight side does not actually prove the stated conclusion.

- [LOW] [compute/lib/multichannel_universality.py](/Users/raeez/chiral-bar-cobar/compute/lib/multichannel_universality.py:31) — Downstream propagation is not fully synchronized. The compute bookkeeping and tests still describe `thm:multi-generator-universality` as a conditional strong-scalar-ansatz surface; see also [test_multi_generator_universality.py:21](/Users/raeez/chiral-bar-cobar/compute/tests/test_multi_generator_universality.py:21). That no longer matches the proved negative theorem in the chapters.

Independent of those failures, two narrower points do survive this audit. Multi-weight really does need a correction in at least one concrete case: [w_algebras.tex:5741](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:5741) computes `\delta F_2(\mathcal W_3)=(c+204)/(16c)\neq 0`, so the scalar formula cannot hold uniformly off the uniform-weight lane. And `F_1=\kappa/24` does survive as a sanity check, via the genus-1 Faber-Pandharipande value at [higher_genus_foundations.tex:4552](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4552) and the `x^2` coefficient in [genus_expansions.tex:1919](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:1919); it is a consistency check, not a substitute for the missing all-genera proof.

## Summary
Instances checked: 24 | Violations found: 6 | Verdict: FAIL
tokens used
198,297
