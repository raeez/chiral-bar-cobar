# T07_thm_H (618s, gpt-5.4)

- [CRITICAL] `chapters/theory/chiral_hochschild_koszul.tex:618` — The proof of `thm:main-koszul-hoch` conflates the bar-side coalgebra with the Koszul dual algebra: it identifies `\bar B^{\mathrm{ch}}(\mathcal A)^\vee` with `\mathcal A^!` and then replaces `\Omega^{\mathrm{ch}}(\bar B^{\mathrm{ch}}(\mathcal A))` by `\Omega^{\mathrm{ch}}(\mathcal A^!)`. That makes the key step `\eqref{eq:hh-via-hom}` invalid as written. This is load-bearing, because Theorem H part `(b)` uses `thm:main-koszul-hoch` for the `t^2` coefficient.

- [CRITICAL] `chapters/theory/chiral_hochschild_koszul.tex:740` — The proof of `thm:hochschild-polynomial-growth` treats `\ChirHoch^n(\mathcal A)` as if its Ext-computing complex were just a complex of `\mathcal D_X`-module morphisms on the base curve and then imports the curve-level amplitude bound `[0,2]`. But the manuscript’s own bigraded definition places Hochschild cochains on the varying configuration spaces `\overline C_{p+2}(X)` of dimension `p+2` (`chapters/theory/higher_genus_foundations.tex:2684`). The proof never justifies collapsing those configuration-space terms to ordinary `\mathcal D_X`-Ext on `X`, so concentration in `{0,1,2}` is claimed as proved, not computed, but the written argument does not establish it.

- [HIGH] `chapters/connections/concordance.tex:64` — The concordance records Theorem H as universally having Hilbert polynomial `P(t)=1+t^2`, but the actual theorem states the family-dependent formula `P_\mathcal A(t)=\dim Z(\mathcal A)+\dim \ChirHoch^1(\mathcal A)\,t+\dim Z(\mathcal A^!)\,t^2` (`chapters/theory/chiral_hochschild_koszul.tex:701`). This already conflicts inside Vol I with the Heisenberg computation `1+t+t^2` (`chapters/theory/hochschild_cohomology.tex:390`) and the generic affine formula `1+\dim(\mathfrak g)t+t^2` (`chapters/theory/koszul_pair_structure.tex:705`).

- [HIGH] `chapters/connections/concordance.tex:68` — The theorem-H citation bundle mixes incompatible scopes. It cites `thm:critical-level-cohomology` under Theorem H even though Vol I explicitly says Theorem H does not apply at critical level (`chapters/theory/hochschild_cohomology.tex:167`), and it does not warn that for non-principal `W`-orbits the concentration claim is only conjectural when Koszulness is open (`chapters/theory/hochschild_cohomology.tex:331`). So the answer to “all families?” is no: the proved statement is on the Koszul locus, with separate family-specific treatments and exclusions.

- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:737` — The theorem-H package cites `Prop.~\ref{prop:bar-resolution-chirhoch}` immediately after the theorem statement, but repo-wide search finds no such label. A named dependency used to source the `RHH_{\mathrm{ch}}(A)\simeq \mathrm{RHom}_{\mathsf{ChirAlg}}(A,A)` identification is missing.

- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:497` — The shift lemma says bar concentration leaves only the “diagonal `p=q`,” but the cited bar-concentration theorem gives vanishing for `q\neq0`, not `p\neq q` (`chapters/theory/chiral_koszul_pairs.tex:1073`). The same wrong explanation recurs in `chapters/theory/higher_genus_foundations.tex:2710`. This does not by itself kill the shift-`2` claim, but it shows the proof narrative is tracking the wrong surviving bigrading.

- [LOW] `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1290` — The wrong universal `P(t)=1+t^2` has already propagated into Vol II; related broadened paraphrases also appear in `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2744` and `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:223`. The drift is not local to one Vol I summary.

## Summary
Instances checked: 20 | Violations found: 7 | Verdict: FAIL

Concentration in `{0,1,2}` is presented as proved-here on the Koszul locus, not merely computed, but the written proof has a core gap. The Hilbert series is not universally `1+t^2`; the surviving Vol I formula is the quadratic family-dependent one in `chapters/theory/chiral_hochschild_koszul.tex:701`, with examples `1+t+t^2` (Heisenberg), `1+t^2` (generic Vir/W), `1+\dim(\mathfrak g)t+t^2` (generic affine), and unbounded critical-level affine outside Theorem H. AP134 check: no surviving theorem-H vdim conflation was found on the audited core surfaces; the manuscript explicitly distinguishes cohomological amplitude from virtual dimension in `chapters/theory/higher_genus_modular_koszul.tex:29691`.


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
session id: 019d8388-33aa-7d73-9a3e-39b5b5e66b68
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


MISSION: FALSIFY the proof of Theorem H: ChirHoch*(A) polynomial Hilbert series, concentrated in {0,1,2}. Check: (a) is this really for ALL families? (b) what is the Hilbert series? (c) is concentration in {0,1,2} proved or just computed? (d) is this amplitude or vdim (AP134)?

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
Using `deep-beilinson-audit` with `multi-path-verify`: I’m locating Theorem H, its full proof surface, and the cited dependency chain before I test scope, logic, and claim inflation.
exec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
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

codex
I’ve loaded the audit workflow. Next I’m pinning the exact theorem surface in `chapters/`, then I’ll read the concordance, registry, red-team notes, and every dependency cited by the proof chain.
exec
/bin/zsh -lc "rg -n \"Theorem H|thm:.*H|ChirHoch|Hilbert series|\\{0,1,2\\}|amplitude|vdim\" chapters metadata CLAUDE.md archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
Total output lines: 2929

rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
archive/raeeznotes/raeeznotes100/red_team_summary.md:100:- `thm:thqg-contact-termination` has statuses **ProvedElsewhere,ProvedHere** across instances: V1:ProvedHere:chapters/connections/thqg_gravitational_complexity.tex:549:Contact termination || V2:ProvedElsewhere:chapters/connections/thqg_gravitational_complexity.tex:551:Contact termination...
archive/raeeznotes/raeeznotes100/red_team_summary.md:105:- `thm:grand-synthesis-principle` has statuses **Conditional,ProvedHere** across instances: V1:ProvedHere:chapters/connections/ym_boundary_theory.tex:128:Grand synthesis principle || V2:Conditional:chapters/connections/ym_synthesis.tex:36:Grand synthesis principle; \ClaimStatusConditional || V2:Conditional:chapters/connections/ym_...
CLAUDE.md:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:19:**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.
CLAUDE.md:273:**C27. Chiral Hochschild of Vir.** `ChirHoch^*(Vir_c)` concentrated in degrees {0,1,2}; polynomial Hilbert series. This is AMPLITUDE (topological), NOT virtual dimension (arithmetic) (AP134). NOT C[Theta] (AP94). NOT Gelfand-Fuchs (GF infinite, AP95).
CLAUDE.md:360:- B45. `vdim ChirHoch^*(A) = 2`. CORRECT: amplitude [0,2], NOT vdim. AP134/FM17.
CLAUDE.md:432:**FM17. Amplitude/dimension conflation for ChirHoch.** Opus conflates "cohomological amplitude [0,2]" (topological) with "virtual dimension 2" (arithmetic). Counter: any sentence mentioning ChirHoch and a numerical invariant must choose explicitly.
CLAUDE.md:480:**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."
CLAUDE.md:490:| H | PROVED | ChirHoch*(A) polynomial Hilbert series, concentrated in cohomological degrees {0,1,2} |
CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:515:**fiber-base/depth** (AP130, AP131, AP134): AP130: Objects on the fiber (forms on Σ_g) are NOT objects on the base (classes on M̄_g). Verify: does this expression live on moduli or on the curve? AP131: Generating depth (degree at which higher ops are determined) != algebraic depth (whether tower terminates). Vir: d_gen finite, d_alg=∞. AP134: Cohomological amplitude [0,d] != virtual dimension d.
CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
CLAUDE.md:807:AP134: Cohomological amplitude != virtual dimension. Concentration of ChirHoch* in degrees {0,1,2} means cohomological amplitude [0,2]. This is NOT "virtual dimension 2". Virtual dimension depends on the specific algebra and is typically defined via an Euler characteristic or index. The amplitude is a topological invariant of the complex; the virtual dimension is an arithmetic one.
CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
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
 succeeded in 50ms:
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
**Searching for theorems and proofs**

I need to locate the exact theorem and proof concerning Hochschild cohomology. The search suggests that `chapters/theory/hochschild_cohomology.tex` likely has Theorem H, so I should read the full file for the theorem statement and proof. There might be something in `chiral_hochschild_koszul.tex` too, if it exists. I'll look for specific theorem labels in the registry and search more targeted to find both the full statement and its cited dependencies. Inspecting lines around the theorem H label will be important.
codex
The live surface is already inconsistent at the constitutional level: `concordance.tex` states Theorem H as `P(t)=1+t^2`, while the constitution says “polynomial Hilbert series, concentrated in {0,1,2}” with a separate affine KM degree-1 exception. I’m now reading the actual theorem/proof file to see whether the proof matches either formulation.
exec
/bin/zsh -lc "sed -n '1,420p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '420,760p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem H|thm:virasoro-hochschild|thm:w-algebra-hochschild|prop:chirhoch1-affine-km|thm:critical-level-cohomology|ClaimStatus.*H|Hilbert polynomial|Hilbert series|concentrated in .*\\{0, ?1, ?2\\}|amplitude|vdim\" chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/koszul_pair_structure.tex chapters examples metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{Chiral Hochschild cohomology and deformation theory}

\index{Hochschild cohomology!classical}
\index{cyclic homology!chiral}

The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ is the
tangent complex to the MC moduli at~$\Theta_\cA$: the cohomology
of the convolution $L_\infty$-algebra controlling deformations,
obstructions, and bulk-field couplings.

The chiral Hochschild complex carries a degree $-1$ Lie bracket
(the chiral Gerstenhaber bracket, Theorem~\ref{thm:gerstenhaber-structure}),
computed by OPE residues on FM configuration spaces.
In the classical limit (fiber at a point), it recovers
Gerstenhaber's bracket~\cite{Ger63} on associative Hochschild
cochains. The chiral bracket is the strict shadow of a full
$L_\infty$ bracket on the chiral Hochschild complex. In the strict model, $\mathrm{HH}^2$ classifies
first-order deformations and $\mathrm{HH}^3$ contains obstructions;
the $L_\infty$ extension records coherent homotopies governing
convergence of formal deformations and transfer of Koszul properties
 succeeded in 51ms:
The Hochschild complex of a chiral algebra $\mathcal{A}$ on a curve $X$ is:
\[\text{HC}_n^{\text{ch}}(\mathcal{A}) = \Gamma(C_n(X), 
 \mathcal{A}^{\boxtimes n} \otimes \det(\Omega^1_{C_n(X)/X}))\]

This has a natural $S^1$-action (cyclic rotation of points), giving:
\[\text{HC}_n^{\text{ch}}(\mathcal{A}) = 
 [\text{Maps}(S^1, LX) \otimes_{\mathcal{A}} \mathcal{A}^{\otimes n}]^{S^1}\]
where $LX = \text{Maps}(S^1, X)$ is the loop space.

The cyclic spectral sequence computes $H_*(LX, \mathcal{A})$ by first computing 
$H_*(\text{Maps}(S^1, X), \mathcal{A})$ and then taking $S^1$-invariants.

Hochschild homology computes the homology of the free loop space, and cyclic homology computes the $S^1$-equivariant loop space homology.
This identification is classical for associative algebras \cite{Loday98}; the chiral extension follows from the factorization structure of the loop space \cite[Chapter~5]{CG17}.
\end{construction}

\begin{computation}[Explicit second-page computation; \ClaimStatusProvedHere]
We compute the $E_2$ page explicitly for standard examples:

\emph{Heisenberg algebra.}
 exited 2 in 51ms:
Total output lines: 3856

rg: examples: No such file or directory (os error 2)
chapters/theory/koszul_pair_structure.tex:136:\ClaimStatusProvedHere
chapters/theory/koszul_pair_structure.tex:184:\begin{lemma}[Well-definedness of chiral enveloping algebra; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:229:\begin{theorem}[Exactness of chiral bar resolution; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:269:\begin{theorem}[Chiral Hochschild complex; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:288:\begin{theorem}[Geometric model of chiral Hochschild cohomology; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:345:\begin{proposition}[Properties of cup product; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:408:\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} structure on chiral Hochschild cohomology; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:468:\begin{theorem}[Periodicity for Virasoro; \ClaimStatusProvedHere]\label{thm:periodicity-virasoro}
chapters/theory/koszul_pair_structure.tex:573:Combining the degeneration at $E_2$ with the de~Rham amplitude
chapters/theory/koszul_pair_structure.tex:599:The proof assembles three ingredients: (i)~Kac determinant irreducibility at generic $c$ (\ClaimStatusProvedElsewhere); (ii)~Beilinson--Drinfeld chiral Hochschild comparison (\ClaimStatusProvedElsewhere, \cite{BD04}); (iii)~Gel'fand--Fuchs computation of $H^*(L_1; \mathbb{C})$ (\ClaimStatusProvedElsewhere, \cite{Fuks86}). The combination is new. For rank~$1$, $\mathrm{Period}(\mathrm{Vir}_c) = 2$ is complete; for higher rank, the periodicity profile $\Pi(\cA)$ (Remark~\ref{rem:periodicity-triple}) is the correct invariant.
chapters/theory/koszul_pair_structure.tex:604:\begin{theorem}[Chiral Hochschild cohomology at critical level; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:699:\begin{proposition}[Hochschild periodicity for same-type pairs; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:704:\item \emph{Virasoro:} $\ChirHoch^*(\mathrm{Vir}_c)$ and $\ChirHoch^*(\mathrm{Vir}_{26-c})$ are both concentrated in $\{0, 2\}$ with $P(t) = 1 + t^2$ \textup{(}Theorem~\textup{\ref{thm:virasoro-hochschild}}\textup{)}.
chapters/theory/koszul_pair_structure.tex:705:\item \emph{Kac--Moody:} $\ChirHoch^*(\widehat{\mathfrak{g}}_k)$ and $\ChirHoch^*(\widehat{\mathfrak{g}}_{k'})$ are both concentrated in $\{0, 1, 2\}$ with $P(t) = 1 + \dim(\mathfrak{g})\,t + t^2$ at generic level \textup{(}the Hilbert polynomial depends on~$\mathfrak{g}$, not on~$k$\textup{)}.
chapters/theory/koszul_pair_structure.tex:706:\item \emph{$\mathcal{W}_N$:} $\ChirHoch^*(\mathcal{W}_N^k)$ and $\ChirHoch^*(\mathcal{W}_N^{k'})$ are both concentrated in $\{0, 1, 2\}$ with the same Hilbert polynomial, since the conformal weights $2, 3, \ldots, N$ are level-independent.
chapters/theory/koszul_pair_structure.tex:714:\begin{corollary}[Hochschild ring isomorphism under Koszul duality; \ClaimStatusProvedHere]
chapters/theory/koszul_pair_structure.tex:802:and the geometric amplitude operator~$G_{\cA}$.

thinking
**Searching for theorems and proofs**

I need to find theorems and proofs in the `hochschild_cohomology.tex` file since the user is asking for specific details. They mentioned searching the chapters directory, which implies I'll need to check for other theorems as well, such as potentially `thm:hochschild-polynomial-growth` in `chiral_hochschild_koszul.tex`. I should inspect around line 577 to locate that theorem and its proof to ensure I gather the right information for the user.
codex
The local theorem statements in `hochschild_cohomology.tex` are not Theorem H itself; they invoke `thm:hochschild-polynomial-growth` as the engine. I’m reading that upstream theorem now, because any downstream “proof” that just cites H would otherwise be circular.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,820p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:hochschild-polynomial-growth|Hochschild.*polynomial|polynomial growth|Hilbert series|Hilbert polynomial|amplitude.*\\[0,2\\]|vdim|Theorem H\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/koszul_pair_structure.tex chapters/connections/concordance.tex chapters/frame/guide_to_main_results.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Chiral Hochschild cohomology and Koszul duality}
\label{chap:deformation-theory}

\index{deformation theory!chiral|textbf}
\index{Hochschild cohomology!chiral|textbf}

The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
Koszul duality, but how rigid is the moduli it lives in? Without
knowing the tangent complex to
$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
bulk-field coupling remains inaccessible. The chiral Hochschild
complex $\ChirHoch^*(\cA)$ is that tangent complex;
Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
Koszul locus, so the MC moduli has cohomological
amplitude~$[0,2]$, and the Koszul duality
$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
is Verdier duality on this tangent space.

The cyclic deformation complex $\Defcyc(\cA)$
(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic
 succeeded in 51ms:
by the shift~$[-p]$, so the combined grading contribution at
bar degree~$p$ is $(p+2) - p = 2$.

It remains to see that this uniform value persists after passing to
cohomology. By Theorem~\ref{thm:bar-concentration}, the bar
cohomology $H^{p,q}(\barB^{\mathrm{ch}}(\cA))$ vanishes for
$q \neq 0$; only the $q = 0$ diagonal contributes. On this
diagonal, bar degree~$p$ and cohomological degree~$q = 0$ give
total degree~$p + 0 = p$ in the source and $p + 2$ in the target
(after the Verdier shift). The difference $2$ is independent of~$p$,
confirming the uniform shift.

The $\omega_X$ factor: Serre duality on the one-dimensional base
curve~$X$ contributes $\omega_X = \Omega^1_X$ as the dualizing sheaf.
This twist is intrinsic to $\mathcal{D}$-module duality on~$X$ and
independent of the configuration-space geometry.
\end{proof}

\begin{lemma}[Chiral Hochschild descent; \ClaimStatusProvedHere]
\label{lem:chirhoch-descent}
 succeeded in 52ms:
chapters/frame/guide_to_main_results.tex:56:\textbf{Theorem H} &
chapters/frame/guide_to_main_results.tex:57: Chiral Hochschild: $\ChirHoch^*(\cA)$ has polynomial
chapters/frame/guide_to_main_results.tex:61: Thm~\ref{thm:hochschild-polynomial-growth} \\[4pt]
chapters/theory/hochschild_cohomology.tex:105:The Hilbert series is $P(t) = 1 + t^2$.
chapters/theory/hochschild_cohomology.tex:112:(Theorem~\ref{thm:hochschild-polynomial-growth}) gives concentration:
chapters/theory/hochschild_cohomology.tex:115:amplitude~$[0,2]$.
chapters/theory/hochschild_cohomology.tex:155:with $\deg P_i = 2m_i + 1$ and $\deg \Theta_i = 2(m_i+1)$, where $m_1,\ldots,m_r$ are the exponents of~$\mathfrak{g}$ (Fuks--Feigin--Tsygan~\cite{FT87}, via BD comparison~\cite{BD04}). For rank~$1$ ($\mathfrak{sl}_2$): $H^{n+4} \cong H^n$ (strict periodicity). For rank $r > 1$: polynomial growth $O(n^{r-1})$ without strict periodicity (Theorem~\ref{thm:affine-periodicity-critical}).
chapters/theory/hochschild_cohomology.tex:163:(Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/theory/hochschild_cohomology.tex:187:which is \emph{unbounded} with polynomial growth $O(n^{r-1})$
chapters/theory/hochschild_cohomology.tex:222:The Hilbert series is $P(t) = 1 + t^2$.
chapters/theory/hochschild_cohomology.tex:234:Koszulness. Theorem~H (Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/theory/hochschild_cohomology.tex:263:Ext on the curve~$X$, bounded by the de~Rham amplitude $[0,2]$. The
chapters/theory/hochschild_cohomology.tex:267:has Hilbert series $1/(1-t^2)$, but $\ChirHoch^*(\mathrm{Vir}_c)$ has
chapters/theory/hochschild_cohomology.tex:268:Hilbert series $1 + t^2$.
chapters/theory/hochschild_cohomology.tex:319:The Hilbert series is $P_{\Walg^k(\fg)}(t) = 1 + t^2$ at
chapters/theory/hochschild_cohomology.tex:325:The S-level Hilbert series is extracted from the M-level
chapters/theory/hochschild_cohomology.tex:327:(Theorem~H) determines the Hilbert polynomial as a
chapters/theory/hochschild_cohomology.tex:722:The polynomial $E_2$ page above should not be confused with the ordinary Hochschild cohomology $HH^*(\mathcal{H})$, which is computed in Example~\ref{ex:HH-heisenberg-complete}. The latter uses the Koszul resolution (length~$2$) and gives $HH^n(\mathcal{H}) = \mathbb{C}$ for $n = 0, 1, 2$ and $HH^n(\mathcal{H}) = 0$ for $n \geq 3$. The difference is that the $E_2$ page here is computed from Hochschild \emph{homology} $HH_*(\mathcal{H}) = \mathbb{C}[c] \otimes \Lambda(\sigma)$, which is polynomial and does not vanish in high degrees. Hochschild cohomology (the $\mathrm{Ext}$-computation) and Hochschild homology (the $\mathrm{Tor}$-computation) are distinct invariants; the former detects deformations, while the latter feeds the cyclic spectral sequence.
chapters/theory/hochschild_cohomology.tex:830:(Theorem~\ref{thm:hochschild-polynomial-growth}). The two invariants
chapters/theory/koszul_pair_structure.tex:574:bound on a curve (Theorem~\ref{thm:hochschild-polynomial-growth}):

thinking
**Checking relevant materials**

I think I should check any claims related to vdim. I’m considering looking through relevant snippets from the guide and the concordance sections concerning theorem H and higher genus. It seems essential to ensure that I have the correct information to understand this better. I’m curious about how these concepts interconnect and could impact my understanding. Let’s see what I can find!
codex
I have the proof core. Next I’m auditing the dependency chain it imports and the downstream theorem summaries that advertise it, because the current manuscript already shows incompatible versions of H (`1+t^2` vs general quadratic polynomial vs family-specific degree-1 terms).
exec
/bin/zsh -lc "sed -n '40,80p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '360,410p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '29660,29710p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '680,715p' chapters/theory/koszul_pair_structure.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 quasi-isomorphism at all genera. &
 Thm~\ref{thm:higher-genus-inversion} \\[4pt]

\textbf{Theorem C} &
 Complementarity: $Q_g(\cA) \oplus Q_g(\cA^!)
 \cong H^*(\overline{\cM}_g, \cZ_\cA)$ for all $g \ge 1$.
 Upgraded to shifted-symplectic Lagrangian geometry. &
 Thm~\ref{thm:quantum-complementarity-main} \\[4pt]

\textbf{Theorem D} &
 Modular characteristic: $\kappa(\cA)$ is universal,
 additive under direct sums, constrained by Koszul
 duality ($\kappa + \kappa' = 0$ for KM/free fields),
 and generates the genus tower via the $\hat{A}$-genus. &
 Thm~\ref{thm:modular-characteristic} \\[4pt]

\textbf{Theorem H} &
 Chiral Hochschild: $\ChirHoch^*(\cA)$ has polynomial
 growth, is Koszul-functorial, and admits an explicit
 Koszul resolution of length bounded by the number
 succeeded in 51ms:
 and its cohomology recovers the formal-disc oper
 differential-form package:
 $H^n(\barB(\widehat{\fg}_{-h^\vee}))
 \cong \Omega^n(\mathrm{Op}_{\fg^\vee}(D))$.
 The $H^0$ identification gives the Feigin--Frenkel
 center~\cite{Feigin-Frenkel}; the $H^1$ identification
 gives K\"ahler differentials of the oper space; and the
 full cohomological identification follows from the bar-Ext
 identification combined with the
 Frenkel--Teleman theorem~\cite{FT06}.
 This gives a vertex-algebraic chain model interfacing with the
 oper side of the geometric Langlands programme.

\item \emph{Chiral Hochschild cohomology
 (Theorems~\ref{thm:w-algebra-hochschild},
 \ref{thm:virasoro-hochschild},
 \ref{thm:critical-level-cohomology};
 Proposition~\ref{prop:chirhoch1-affine-km}).}
 For the principal $\Walg$-algebra $\Walg^k(\fg)$ at generic level:
 $\ChirHoch^n(\Walg^k(\fg)) = 0$ for $n > 2$, with Hilbert polynomial
 succeeded in 50ms:
\emph{(H).}
The Hochschild spectral sequence degenerates at~$E_2$ for
Koszul algebras by the shadow obstruction tower concentration at degree~$2$
(Proposition~\ref{prop:e2-formality-hochschild}).
Polynomial growth of~$\operatorname{ChirHoch}^*$ follows
from $E_2$-degeneration plus finite-dimensional
graded pieces. Koszul-functoriality is the homotopy
invariance of
$\cA^{\mathrm{sh}} = H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
(Theorem~\ref{thm:shadow-homotopy-invariance}).
\end{proof}

\begin{remark}[Theorem~H as holographic finite-dimensionality]
\label{rem:theorem-h-holographic-finite-dim}
\index{Theorem H!holographic finite-dimensionality}
\index{ChirHoch@$\operatorname{ChirHoch}^*$!bulk state count}
\index{holographic correction hierarchy!finite bulk states}
Part~(H) of the master theorem admits a holographic reading that
sharpens its physical content. The chiral Hochschild cohomology
$\operatorname{ChirHoch}^*(\cA)$ is concentrated in degrees
 succeeded in 51ms:

\emph{Rank~$r > 1$.}
The cohomology ring has $r$ distinct polynomial degrees $2(m_i + 1)$; when not all equal, strict periodicity fails. For $\hat{\mathfrak{sl}}_3$ at $k = -3$: $\deg\Theta_1 = 4$, $\deg\Theta_2 = 6$, and $\dim \ChirHoch^{12} = 3 \neq 1 = \dim \ChirHoch^6$, violating $6$-periodicity. The correct statement is polynomial growth $\dim \ChirHoch^n = O(n^{r-1})$.
\end{remark}

\begin{remark}[Provenance]\label{rem:periodicity-provenance}
The proof assembles three published results:
(i)~the Beilinson--Drinfeld comparison between chiral Hochschild
and continuous Lie algebra cohomology (\ClaimStatusProvedElsewhere,
\cite{BD04}, Thm.~4.5.2);
(ii)~the Gel'fand--Fuchs/Feigin--Tsygan computation of
$H^*_{\mathrm{cont}}(\mathfrak{g} \otimes t\bC[[t]]; \bC)$
(\ClaimStatusProvedElsewhere, \cite{FT87});
(iii)~the uncurved bar complex structure at critical level, which
follows from the critical-level fixed-point property
(Corollary~\ref{cor:level-shifting-part1}).
The synthesis for general simple~$\mathfrak{g}$ is new to this work.
\end{remark}

\begin{proposition}[Hochschild periodicity for same-type pairs; \ClaimStatusProvedHere]

thinking
**Researching theorems**

I need to dive into the Hochschild-Bar-Cobar theorem, so I’ll start by searching for it and reading up on it. I should also check out the Bar Concentration theorem and look into any relevant definitions. There seems to be a lot to unpack here, and it's important to understand these concepts thoroughly for my work. I’ll make sure to keep everything organized as I gather information!
exec
/bin/zsh -lc "sed -n '4520,4665p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '300,420p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1220,1295p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:hochschild-bar-cobar\\}|label\\{thm:bar-concentration\\}|label\\{thm:bar-cobar-isomorphism-main\\}|label\\{def:chiral-koszul-morphism\\}|holonomic|de Rham functor.*\\[0, ?2\\]|Ext\\"'^n_'"\\{\\\\mathcal\\{D\\}_X\\}\" chapters/theory chapters/examples chapters/frame" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:label\{thm:hochschild-bar-cobar\}|label\{thm:bar-concentration\}|label\{thm:bar-cobar-isomorphism-main\}|label\{def:chiral-koszul-morphism\}|holonomic|de Rham functor.*\[0, ?2\]|Ext\^n_\{\mathcal\{D\}_X\})
                                                                                                                                                                                                  ^^
error: unrecognized escape sequence
 succeeded in 52ms:
\begin{itemize}
\item $m_1$: BRST operator $Q$
\item $m_2$: String multiplication
\item $m_3$: Four-string vertex
\item Higher $m_n$: Contact terms
\end{itemize}
\end{theorem}

The action:
\[
S[\Psi] = \frac{1}{2}\langle \Psi, Q\Psi \rangle + \sum_{n \geq 3} \frac{1}{n!}\langle \Psi, m_n(\Psi,\ldots,\Psi)\rangle
\]

\subsection{Holographic duality}

\begin{conjecture}[Holographic Koszul duality; \ClaimStatusConjectured]
\label{conj:holographic-koszul-deformation}
A holographic Koszul template for AdS$_3$/CFT$_2$ should exchange:
\begin{itemize}
\item a suitable bulk gravity package $\leftrightarrow$ a boundary CFT package
 succeeded in 52ms:
(Proposition~\ref{prop:shadow-formality-low-degree}). On each fiber,
the HPL transfer is an ordinary $A_\infty$ transfer over a field, to
which Keller's classicality theorem applies. The PBW filtration is
defined fiberwise and compatible with the FM stratification, so
fiberwise $E_2$-collapse assembles to global $E_2$-collapse: all
transferred differentials $d_r = 0$ for $r \geq 2$ because
$m_n = 0$. Hence Koszulness.
\end{proof}

\begin{remark}[$A_\infty$ products as genus-$0$ shadows]
\label{rem:ainfty-genus0-shadow}

The sequence $(m_3, m_4, \ldots)$ is the genus-$0$ analogue of the
shadow obstruction tower $\Theta_\cA^{\leq 3}, \Theta_\cA^{\leq 4},
\ldots$ of Theorem~\ref{thm:mc2-bar-intrinsic}: the $m_n$ measure
nonlinearity of the bar differential at genus~$0$, while the shadows
$\Theta_\cA^{\leq r}$ measure it at all genera.
\end{remark}

\begin{example}[Truncated polynomials: the homotopy Koszul dual off the Koszul locus]
 succeeded in 52ms:
(Theorem~\ref{thm:arnold-relations}): every boundary
stratum of $\overline{C}_{n+2}$ where two points collide
contributes a residue (from $d_{\text{fact}}$) and a
boundary form (from $d_{\text{config}}$), and the
Arnold relations ensure these pair up with opposite signs.
\end{proof}

\subsection{Explicit formula for the differential}

For a cochain $\phi \in C^n_{\text{chiral}}$, the differential acts by:

\begin{align}
(d_{\text{int}}\phi)(&z_0,\ldots,z_{n+1}) = \sum_{i=0}^{n+1} (-1)^i d_{\mathcal{A}}(\phi(z_0,\ldots,\hat{z}_i,\ldots,z_{n+1})) \\
(d_{\text{fact}}\phi)(&z_0,\ldots,z_{n+1}) = \sum_{i=1}^n (-1)^i \text{Res}_{z_i = z_0} \phi(\mu(z_0,z_i),z_1,\ldots,\hat{z}_i,\ldots,z_{n+1}) \\
&+ \sum_{1 \leq i < j \leq n} (-1)^{i+j} \phi(z_0,\ldots,\mu(z_i,z_j),\ldots,\hat{z}_i,\ldots,\hat{z}_j,\ldots,z_{n+1}) \\
(d_{\text{config}}\phi)(&z_0,\ldots,z_{n+1}) = d_{\overline{C}_{n+2}}(\phi)
\end{align}

where $\hat{z}_i$ denotes omission and $\mu$ is the chiral multiplication.


thinking
**Exploring bar concentration theorem**

I’m thinking about the bar concentration theorem and how it might relate to chiral koszul pairs. It seems like I need to study these concepts a bit separately to understand them better. I wonder what specific aspects to focus on since the connections might not be instantly clear. Let's take a closer look and see what insights emerge! This could lead to some interesting findings or questions to explore further.
exec
/bin/zsh -lc "sed -n '1300,1395p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:bar-concentration\\}|label\\{def:chiral-koszul-morphism\\}|label\\{def:chiral-koszul-pair\\}|label\\{thm:bar-cobar-isomorphism-main\\}|holonomic|de~Rham functor on .*\\[0, ?2\\]|Ext\\"'^n_'"\\{\\\\mathcal\\{D\\}_X\\}\" chapters/theory chapters/examples chapters/frame" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2280,2365p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1910,1965p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:label\{thm:bar-concentration\}|label\{def:chiral-koszul-morphism\}|label\{def:chiral-koszul-pair\}|label\{thm:bar-cobar-isomorphism-main\}|holonomic|de~Rham functor on .*\[0, ?2\]|Ext\^n_\{\mathcal\{D\}_X\})
                                                                                                                                                                                                    ^^
error: unrecognized escape sequence
 succeeded in 51ms:
\end{theorem}

\begin{proof}
Forward: $E_2$-collapse concentrates $H^*(\barBgeom(\cA))$ on
the diagonal $p = q$; since the bar resolution computes Ext,
$\operatorname{Ext}^{p,q}(\omega_X, \omega_X) = 0$ for
$p \neq q$.
Converse: diagonal concentration forces all PBW differentials
$d_r$ ($r \geq 2$) to vanish, since a $d_r$-differential shifts
the bigrading by $(r, 1-r)$, producing off-diagonal classes
that contradict~$\operatorname{Ext}^{p,q} = 0$ for $p \neq q$.
Hence $E_2$-collapse, hence Koszulness.
\end{proof}

\begin{proposition}[PBW universality; \ClaimStatusProvedHere]
\label{prop:pbw-universality}
\index{Koszul property!PBW universality}
\index{vertex algebra!freely strongly generated}

A vertex algebra~$\cA$ is \emph{freely strongly generated} if it
 succeeded in 51ms:

\smallskip\noindent
\textup{(xi)}$\Rightarrow$\textup{(i)}:
If $\cM_\cA$ and $\cM_{\cA^!}$ are transverse Lagrangians,
their derived intersection
$\cM_\cA \times^h_{\cM_{\mathrm{comp}}} \cM_{\cA^!}$
is discrete (transverse Lagrangian intersection in a $(-1)$-shifted
symplectic space has expected dimension~$0$). This derived
intersection computes the twisted tensor product
$K_\tau(\cA, \cA^!)$; its acyclicity (i.e., discreteness of the
intersection) is Koszulness
(Definition~\ref{def:chiral-koszul-morphism}).
\end{proof}

\begin{remark}[Status of the Lagrangian and purity refinements]
Condition~\textup{(xi)} remains conditional on perfectness and
non-degeneracy of the ambient tangent complex. Condition~\textup{(xii)}
implies condition~\textup{(x)} (via Saito's theory of mixed Hodge
modules; see Remark~\textup{\ref{rem:d-module-purity-content}}).
The converse direction (Koszulness implies D-module purity) is
 succeeded in 51ms:
\]
whose leading terms $\ell_1^{(0)}(\Theta) + \tfrac{1}{2}\ell_2^{(0)}(\Theta,\Theta) = 0$ give
the classical dg~MC equation
$d\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$,
the strict shadow of the full $L_\infty$-MC equation
(Theorem~\ref{thm:modular-homotopy-convolution}).
Theorem~\ref{thm:universal-MC} establishes existence of~$\Theta_\cA$
for Kac--Moody at non-critical level,
Virasoro, and principal~$\mathcal{W}_N$ at generic level.
All modular invariants ($\kappa$, $\Delta$, shadows
$\operatorname{Sh}_r$) are projections of~$\Theta_\cA$ onto graded
components; the higher brackets $\ell_n^{(g)}$ encode
the Feynman-amplitude content beyond the leading dg~terms.
\end{remark}

\begin{proposition}[Hochschild as degree-$2$ shadow projection;
\ClaimStatusProvedHere]
\label{prop:hochschild-shadow-projection}
\index{chiral Hochschild cohomology!shadow projection}
\index{shadow algebra!degree-2 projection}

thinking
**Searching for theorem details**

I realize I still need more details on the bar-concentration theorem. It seems a bit complex, so I should probably search for simpler explanations or resources to help me understand it better. Maybe there are some introductory articles or videos that break it down. Let’s find something that makes the concepts clearer and more accessible. I'm curious about what resources I can find!
exec
/bin/zsh -lc "sed -n '1580,1670p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1760,1835p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1120,1195p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:bar-concentration|def:chiral-koszul-morphism|def:chiral-koszul-pair|thm:bar-cobar-isomorphism-main|holonomic|de Rham functor on .*\\[0, 2\\]|Ext\\"'^n_'"\\{\\\\mathcal\\{D\\}_X\\}\" chapters/theory chapters/examples chapters/frame" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
defining~$\tau$.
Acyclicity of $K_\tau^L$ and $K_\tau^R$ upgrades this map from a
graded comparison to a coalgebra isomorphism
(the chiral analogue of \cite[Theorem~2.3.1]{LV12}; the
identical argument applies because acyclicity of the Koszul
complexes is the only input beyond the MC equation, and both
hold in the chiral setting by
Lemma~\ref{lem:bar-holonomicity} and
Theorem~\ref{thm:fundamental-twisting-morphisms}).
\end{proof}

%%% ---------------------------------------------------------------
%%% INTRINSIC CHARACTERIZATIONS OF CHIRAL KOSZULNESS
%%% ---------------------------------------------------------------

\subsection{Intrinsic characterizations of chiral Koszulness}
\label{sec:intrinsic-characterizations-koszulness}
\index{Koszul property!intrinsic characterizations}
\index{MC element!genus-0 formality}

 succeeded in 52ms:
 (Remark~\ref{rem:chiral-contramodules}).
\end{enumerate}
These geometric inputs are specific to the chiral setting and have
no analogue in Positselski's ground-field framework.
\end{remark}

%================================================================
% SECTION: BAR-COBAR INVERSION - COMPLETE QUASI-ISOMORPHISM
%================================================================

\section{Bar-cobar inversion}
\label{sec:bar-cobar-inversion-quasi-iso}

The comodule-contramodule correspondence of the preceding section
provides the categorical framework in which bar-cobar inversion
lives: at genus~$0$ the coderived category reduces to the
ordinary derived category, and the inversion theorem is a
quasi-isomorphism in the classical sense; at genus~$g \geq 1$
the curvature forces passage to the coderived setting, and the
inversion theorem becomes a statement about coderived equivalences.
 succeeded in 51ms:
\end{proposition}

\begin{proof}
The quotient-system data package precisely the inputs of Definition~\ref{def:winfty-principal-stage-compatible}.
\end{proof}

\begin{proposition}[Factorization-envelope criterion for principal
stages; \ClaimStatusProvedHere]
\label{prop:winfty-factorization-envelope-criterion}
Let $\mathcal{F}_\infty$ be a separated complete factorization algebra
on a curve with quotient maps
$\mathcal{F}_\infty \twoheadrightarrow \mathcal{F}_{\le N}$
whose kernels define a descending separated complete conformal-weight
filtration. If each $\mathcal{F}_{\le N}$ admits a BD chiral envelope
quasi-isomorphic to $W_N$ and the quotient maps intertwine the
principal-stage tower, then the chiral envelope of
$\mathcal{F}_\infty$ is a principal-stage compatible $W_\infty$ target.
Bar-data compatibility further implies
Proposition~\ref{prop:winfty-quotient-system-criterion} and
Corollary~\ref{cor:winfty-hlevel-comparison-criterion}.
 exited 2 in 51ms:
rg: regex parse error:
    (?:thm:bar-concentration|def:chiral-koszul-morphism|def:chiral-koszul-pair|thm:bar-cobar-isomorphism-main|holonomic|de Rham functor on .*\[0, 2\]|Ext\^n_\{\mathcal\{D\}_X\})
                                                                                                                                                               ^^
error: unrecognized escape sequence

thinking
**Searching for theorem details**

I experienced an issue with my search, but I still gathered some important information along the way. Now I need to check out the specifics of the bar-concentration theorem. It might help to search for a simpler string to find those details more effectively. There’s a lot to unravel here, so I just want to make sure I'm on the right track! Let’s see what I can find.
exec
/bin/zsh -lc "sed -n '2320,2395p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '80,155p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "bar-concentration|chiral-koszul-pair|chiral-koszul-morphism" chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1650,1735p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Chiral tensor product.}
 If $\cA, \cB$ are chirally Koszul on the curve $X$, then
 $\cA \boxtimes \cB$ is chirally Koszul, and
 $(\cA \boxtimes \cB)^! \simeq \cA^! \boxtimes \cB^!$ as Koszul
 duals.
\item \emph{Koszul dualization} \textup{(}involutivity\textup{)}.
 If $\cA$ is chirally Koszul, then so is $\cA^!$, and
 $(\cA^!)^! \simeq \cA$ canonically.
\item \emph{Smooth base change.}
 If $f \colon Y \to X$ is a smooth morphism of curves and
 $\cA$ is chirally Koszul on $X$, then $f^*\cA$ is chirally
 Koszul on $Y$, and $(f^*\cA)^! \simeq f^*(\cA^!)$.
\end{enumerate}
\end{proposition}

\begin{proof}
\textup{(a)}: Tensor product closure is
Proposition~\ref{prop:koszul-dual-tensor-product}, which
constructs the quadratic-tensor witnessing datum and verifies
 succeeded in 50ms:
behaviour, not by the validity of the duality. Second,
Koszulness and SC formality are logically independent properties.
Koszulness is the condition that bar cohomology is concentrated
in degree one; SC formality is the condition
$m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ in the Swiss-cheese
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
 succeeded in 51ms:
chapters/theory/chiral_modules.tex:624:(Definition~\ref{def:chiral-koszul-pair}). A \emph{Koszul module pair}
chapters/theory/chiral_modules.tex:649:\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair}}\textup{)}
chapters/theory/chiral_hochschild_koszul.tex:329:\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})},
chapters/theory/chiral_hochschild_koszul.tex:498:\textup{(}Theorem~\textup{\ref{thm:bar-concentration})}
chapters/theory/chiral_hochschild_koszul.tex:524:cohomology. By Theorem~\ref{thm:bar-concentration}, the bar
chapters/theory/chiral_hochschild_koszul.tex:545:\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}
chapters/theory/chiral_hochschild_koszul.tex:564:degree. On the Koszul locus, Theorem~\ref{thm:bar-concentration}
chapters/theory/chiral_hochschild_koszul.tex:584:\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})} with
chapters/theory/chiral_hochschild_koszul.tex:600:\textup{(}Theorem~\textup{\ref{thm:bar-concentration})} forces
chapters/theory/chiral_hochschild_koszul.tex:744:(Theorem~\ref{thm:bar-concentration}) gives a
chapters/theory/chiral_hochschild_koszul.tex:863:(Theorem~\ref{thm:bar-concentration}) gives
chapters/theory/chiral_hochschild_koszul.tex:1028: (Theorem~\ref{thm:bar-concentration}).
chapters/theory/chiral_hochschild_koszul.tex:1163:(Theorem~\ref{thm:bar-concentration}),
chapters/theory/chiral_hochschild_koszul.tex:3995:\item $\cA$ admits a Koszul dual $\cA^!$ in the sense of Definition~\ref{def:chiral-koszul-pair}, with $\cA^!$ also rational.
chapters/theory/chiral_hochschild_koszul.tex:4579:\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})},
chapters/theory/chiral_koszul_pairs.tex:137:pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
chapters/theory/chiral_koszul_pairs.tex:248:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
chapters/theory/chiral_koszul_pairs.tex:371: \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
chapters/theory/chiral_koszul_pairs.tex:393:By definition (Definition~\ref{def:chiral-koszul-morphism},
chapters/theory/chiral_koszul_pairs.tex:413:hypothesis (Definition~\ref{def:chiral-koszul-morphism},
 succeeded in 50ms:
 $H^\bullet(\Omega(\bar{B}(\mathcal{A})))$
 with $E_1$-page given by the bar-cobar complex; it collapses at $E_2$
 by the Koszul property (Theorem~\ref{thm:spectral-sequence-collapse})
\end{enumerate}

\smallskip\noindent\emph{Scope.}
The Koszul hypothesis is essential: for simple admissible affine
quotients and minimal-model Virasoro/W-algebras the PBW/Shapovalov
argument is unavailable, the bar spectral sequence can carry extra
higher-differential data, and this chapter does \emph{not} claim that
the counit $\psi$ is a quasi-isomorphism there
\textup{(}see Remark~\ref{rem:sl2-admissible}
and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
with the completed or coderived bar-cobar correspondence
(Corollary~\ref{cor:bar-cobar-inverse},
\S\ref{sec:i-adic-completion}).
\end{theorem}


\begin{example}[Admissible-level failure of bar-cobar inversion]
exec
/bin/zsh -lc "sed -n '236,285p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '584,640p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1135,1188p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1058,1135p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 51ms:
\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
\index{Koszul pair!chiral|textbf}
A \emph{chiral Koszul pair} on a smooth projective curve~$X$
is a pair of chiral Koszul data
\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
Definition~\textup{\ref{def:chiral-koszul-morphism})}
\[
(\cA_1, \cC_1, \tau_1, F_\bullet), \qquad
(\cA_2, \cC_2, \tau_2, F_\bullet)
\]
equipped with Verdier-compatible identifications
\[
\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \cC_2, \qquad
\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \cC_1,
\]
compatible with the twisting morphisms and filtrations.
In this situation we write $\cA_2 \simeq \cA_1^!$ and
$\cA_1 \simeq \cA_2^!$.

\smallskip\noindent
 succeeded in 51ms:
\subsection{Intrinsic characterizations of chiral Koszulness}
\label{sec:intrinsic-characterizations-koszulness}
\index{Koszul property!intrinsic characterizations}
\index{MC element!genus-0 formality}

The MC element $\Theta_\cA \in \MC(\mathfrak{g}_\cA^{\mathrm{mod}})$
lives in a modular convolution algebra bigraded by degree and genus.
Chiral Koszulness is a \emph{genus-$0$ formality property}:
it says the genus-$0$ component $\Theta_\cA^{(0)}$ is
determined by its binary part; equivalently, all genus-$0$
obstruction classes $o_{r+1}^{(0)}(\cA) = 0$ vanish for $r \geq 2$.
The shadow obstruction tower probes all genera; Koszulness constrains only
genus~$0$. Twelve characterizations of chiral
Koszulness (ten proved unconditionally equivalent, one conditional on
perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
one-directional (D-module purity, forward direction established)), each
reading~$\Theta_\cA^{(0)}$ through a different invariant
of the convolution algebra.

\begin{remark}[One-loop exactness]
 succeeded in 51ms:
chiral primary.
\end{remark}

\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
\label{thm:bar-concentration}
\index{bar complex!concentration}
\textup{[Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $(\cA_1, \cA_2)$ be a chiral Koszul pair
\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})}.
Then the augmented bar complex $\bar{B}^{\mathrm{ch}}(\cA_1)$,
equipped with its bigrading by bar degree~$p$ and bar-differential
cohomological degree~$q$, satisfies:
\[
H^{p,q}(\bar{B}^{\mathrm{ch}}(\cA_1)) = 0
\quad\text{for } q \neq 0,
\qquad
H^{p,0}(\bar{B}^{\mathrm{ch}}(\cA_1)) \cong (\cA_2^!)_p.
\]

thinking
**Inspecting mathematical concepts**

I need to look into the corollary about bar cohomology and its Koszul dual, since there’s a proof referencing it in the bar concentration theorem. It seems important to investigate this. I’m also considering the PBW-Koszulness criterion, as it could be relevant too. I’m wondering if I’ll need to dive deeper into these concepts to ensure I have a thorough understanding. Let's see what I find!
exec
/bin/zsh -lc 'rg -n "cor:bar-cohomology-koszul-dual|thm:pbw-koszulness-criterion|lem:bar-holonomicity|thm:fundamental-twisting-morphisms" chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_modules.tex:682:(extending Lemma~\ref{lem:bar-holonomicity} to the pointed
chapters/theory/chiral_koszul_pairs.tex:102:(Theorem~\ref{thm:pbw-koszulness-criterion}).
chapters/theory/chiral_koszul_pairs.tex:179:quadratic-Koszul (Theorem~\ref{thm:pbw-koszulness-criterion}).
chapters/theory/chiral_koszul_pairs.tex:279:explicit, as required for Theorem~\ref{thm:fundamental-twisting-morphisms}.
chapters/theory/chiral_koszul_pairs.tex:357:\label{thm:fundamental-twisting-morphisms}
chapters/theory/chiral_koszul_pairs.tex:499:(Theorem~\ref{thm:fundamental-twisting-morphisms}) is
chapters/theory/chiral_koszul_pairs.tex:618:(Theorem~\ref{thm:pbw-koszulness-criterion}), acyclicity
chapters/theory/chiral_koszul_pairs.tex:653:(Theorem~\ref{thm:pbw-koszulness-criterion}) is trivial and the
chapters/theory/chiral_koszul_pairs.tex:697:\label{thm:pbw-koszulness-criterion}
chapters/theory/chiral_koszul_pairs.tex:789:Theorem~\ref{thm:pbw-koszulness-criterion}.
chapters/theory/chiral_koszul_pairs.tex:825:By Theorem~\ref{thm:pbw-koszulness-criterion},
chapters/theory/chiral_koszul_pairs.tex:869:By Theorem~\ref{thm:pbw-koszulness-criterion},
chapters/theory/chiral_koszul_pairs.tex:874:\label{cor:bar-cohomology-koszul-dual}
chapters/theory/chiral_koszul_pairs.tex:877:Theorem~\textup{\ref{thm:pbw-koszulness-criterion}},
chapters/theory/chiral_koszul_pairs.tex:1096:By the PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion}),
chapters/theory/chiral_koszul_pairs.tex:1100:Corollary~\ref{cor:bar-cohomology-koszul-dual} then gives
chapters/theory/chiral_koszul_pairs.tex:1127:Lemma~\ref{lem:bar-holonomicity} and
chapters/theory/chiral_koszul_pairs.tex:1128:Theorem~\ref{thm:fundamental-twisting-morphisms}).
chapters/theory/chiral_koszul_pairs.tex:1160:(Corollary~\ref{cor:bar-cohomology-koszul-dual}) admits a sharp
chapters/theory/chiral_koszul_pairs.tex:1203:Theorem~\ref{thm:pbw-koszulness-criterion}.
exec
/bin/zsh -lc "sed -n '904,980p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '460,525p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,590p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The first bijection sends $\tau \in \mathrm{Tw}(\cC, \cA)$
to the algebra morphism $g_\tau\colon \Omega_X(\cC) \to \cA$
defined on cogenerators by $g_\tau(s^{-1} c) = \tau(c)$; the
MC equation for $\tau$ is equivalent to $g_\tau$ commuting
with differentials
(the same proof as \cite[Theorem~2.2.7]{LV12}).
The second bijection sends $\tau$ to the coalgebra morphism
$f_\tau\colon \cC \to \bar{B}_X(\cA)$ defined dually.
The universal property of the bar construction as a cofree
coalgebra ensures uniqueness of factorization.
\end{proof}

\begin{remark}[Why the MC equation is Stokes' theorem]
\label{rem:MC-is-Stokes}
\index{Maurer--Cartan equation!geometric origin}
The Maurer--Cartan equation $d\tau + \tau \star \tau = 0$ is
not an imposed axiom. It is forced by the geometry of
$\overline{C}_2(X)$. The convolution
$(\tau \star \tau)(x) = \mu \circ (\tau \otimes \tau)
 succeeded in 52ms:
\[
F_p \barBgeom^n(\cA) = \bigl\{
a_1 \otimes \cdots \otimes a_{n+1} \otimes \omega
\;\big|\; a_i \in F_{p_i}\cA,\;
\textstyle\sum p_i \leq p\bigr\}
\]
where $\omega \in \Omega^n_{\log}(\overline{C}_{n+1}(X))$.
This filtration is exhaustive (every bar element lies in
some $F_p$ by finiteness of conformal weight) and
compatible with the differential (the bar differential
respects conformal weight since the OPE does).

\emph{Step~2: The associated graded.}
The filtration $F_p$ is placed on the algebra factor $\cA$ in the bar construction $T^c(s^{-1}\bar{\cA})$
underlying $\barBgeom(\cA)$; the configuration-space form factor
$\Omega^\bullet_{\log}(\overline{C}_\bullet(X))$ carries PBW degree~$0$.
Since $T^c$ is graded cofree and Hypothesis~\ref{item:pbw-flat} makes each
$\operatorname{gr}_F^p\cA$ a free graded $\cO_X$-module in each conformal weight,
tensor-product flatness gives
$\operatorname{gr}_F T^c(s^{-1}\bar{\cA}) \cong T^c(s^{-1}\operatorname{gr}_F\bar{\cA})$.
 succeeded in 51ms:
\begin{proposition}[Universal property of bar construction {\cite{LV12}}; \ClaimStatusProvedElsewhere]
\label{prop:bar-universal-property}
\index{bar construction!universal property}
For any augmented chiral algebra~$\cA$, the bar construction
$\barB_X(\cA)$ together with its canonical twisting morphism
$\tau_{\mathrm{can}} \colon \barB_X(\cA) \to \cA$
is initial among pairs $(C, \tau)$ consisting of a conilpotent chiral
coalgebra~$C$ and a twisting morphism $\tau \colon C \to \cA$.
Concretely: for any twisting morphism $\alpha \colon C \to \cA$,
there exists a unique coalgebra map
$f_\alpha \colon C \to \barB_X(\cA)$
such that $\tau_{\mathrm{can}} \circ f_\alpha = \alpha$.
Dually, the cobar construction $\Omega_X(C)$ together with
$\iota_{\mathrm{can}} \colon C \to \Omega_X(C)$ is terminal among
pairs $(A, \iota)$ consisting of an augmented chiral algebra~$A$
and a twisting morphism $\iota \colon C \to A$.
\end{proposition}

\begin{proof}
This is the chiral analogue of

thinking
**Evaluating proof completeness**

I’m thinking about the theorem proof and its criteria. I need to check if it’s truncated or if I have enough information for now. It might be important to consider Step 4 after the E2 collapse. I want to inspect the beginning of my notes around line 697. I just want to make sure I'm thorough and not missing any critical parts of the proof!
codex
I’m tracing H’s proof back to the PBW/Koszul concentration theorem it actually uses. The key question now is whether that theorem gives a genuine Ext bound on `\ChirHoch`, or only a bar-cohomology statement that is being overpromoted downstream.
exec
/bin/zsh -lc "sed -n '770,890p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '690,770p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '350,430p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,505p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The PBW criterion reduces chiral Koszulness to the classical statement that $\operatorname{gr}_F \cA$ is Koszul.
For Kac--Moody and Virasoro algebras, $\operatorname{gr}_F \cA$ is a polynomial algebra (Koszul by Priddy's theorem); semisimplicity of $\mathfrak{g}$ is not required.
\end{remark}

\begin{theorem}[Affine Kac--Moody algebras are chiral Koszul; \ClaimStatusProvedHere]
\label{thm:km-chiral-koszul}
\index{Kac--Moody algebra!chiral Koszulness|textbf}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For any simple Lie algebra $\fg$ and generic level
$k \notin \Sigma(\fg)$ (the finite exceptional set of
Theorem~\textup{\ref{thm:bar-cohomology-level-independence}}),
the affine Kac--Moody vertex algebra
$\widehat{\fg}_k$ is chiral Koszul.
\end{theorem}

\begin{proof}
We verify the three hypotheses of
Theorem~\ref{thm:pbw-koszulness-criterion}.
 succeeded in 51ms:
\begin{corollary}[Three bijections for chiral twisting morphisms;
\ClaimStatusProvedHere]
\label{cor:three-bijections}
\index{twisting morphism!three bijections|textbf}
For a conilpotent complete factorization coalgebra $\cC$
and an augmented chiral algebra $\cA$ on a smooth curve~$X$,
there are natural bijections
\begin{align}\label{eq:three-bijections}
\mathrm{Tw}(\cC, \cA)
&\;\cong\;
\operatorname{Hom}_{\mathrm{alg}}(\Omega_X(\cC), \cA)
\notag\\
&\;\cong\;
\operatorname{Hom}_{\mathrm{coalg}}(\cC, \bar{B}_X(\cA))
\end{align}
where\/ $\mathrm{Tw}(\cC, \cA)$ is the set of degree~$+1$
morphisms $\tau\colon \cC \to \cA$ satisfying the
Maurer--Cartan equation $d\tau + \tau \star \tau = 0$.

The \emph{universal twisting morphism}
 succeeded in 51ms:
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
\begin{enumerate}
\item\label{item:pbw-flat} The filtration is \emph{flat}: each $F_p/F_{p-1}$ is a free
 succeeded in 51ms:
morphism. Classical Koszulity gives acyclicity of the
associated graded twisted tensor products. Strong convergence
then lifts this to acyclicity of $K_\tau^L$ and $K_\tau^R$
themselves.
\end{proof}

\begin{theorem}[Fundamental theorem of chiral twisting morphisms; \ClaimStatusProvedHere]
\label{thm:fundamental-twisting-morphisms}
\index{twisting morphism!fundamental theorem|textbf}
\textup{[Regime: quadratic
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

\smallskip\noindent
This is the chiral analogue of \cite[Theorem~2.3.1]{LV12}.
For a chiral twisting datum
$(\cA, \cC, \tau, F_\bullet)$
\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum})},
the following are equivalent:
\begin{enumerate}[label=\textup{(\roman*)}]
\item\label{ftm:koszul}
exec
/bin/zsh -lc "rg -n \"label\\{thm:bar-cobar-isomorphism-main\\}|Bar-cobar adjunction|Verdier intertwining|Theorem A\" chapters/theory chapters/frame chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '880,980p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '980,1080p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1080,1145p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/guide_to_main_results.tex:26:\textbf{Theorem A} &
chapters/frame/preface_section1_v2.tex:515:The adjunction and Verdier intertwining (Theorem~A), the bar-cobar
chapters/frame/preface_section1_draft.tex:390:locus is the content of Theorem~A (the Verdier intertwining
chapters/theory/hochschild_cohomology.tex:1709:The theoretical arc of Part~\ref{part:bar-complex} is now complete. Algebraic foundations (\S\ref{ch:algebraic-foundations}) supplied the operadic language; configuration spaces (\S\ref{chap:config-spaces}) gave it geometric content; the bar-cobar adjunction (Theorem~A) and the Verdier intertwining $D_{\mathrm{Ran}}(B(\cA)) \simeq B(\cA^!)$ established duality on the Ran space; and the higher-genus theory assembled the proved scalar package~$\kappa(\cA)$, the proved spectral package~$(\Delta_{\cA},\Pi_{\cA})$, and the bar-intrinsic Maurer--Cartan element~$\Theta_{\cA}$. The three main theorems (adjunction~(A), inversion on the Koszul locus~(B), and Lagrangian complementarity~(C)) are projections of a single structure: the modular Koszul object associated to a factorization algebra on curves. Chiral Hochschild cohomology, developed in this chapter, is the infinitesimal invariant of that structure: concentrated in degrees $\{0,1,2\}$ for Koszul algebras (Theorem~H), it classifies deformations, detects obstructions, and exchanges under Koszul duality via the Connes operator.
chapters/theory/higher_genus_modular_koszul.tex:478:\emph{(Verdier intertwining.)}
chapters/theory/higher_genus_modular_koszul.tex:2581:the Verdier intertwining axiom~\textup{\ref{MK:verdier-htpy}}, realized
chapters/theory/higher_genus_modular_koszul.tex:12854: Additivity, Verdier intertwining
chapters/theory/fourier_seed.tex:959:(A) & Verdier intertwining
chapters/theory/koszul_pair_structure.tex:1844:Verdier intertwining (Theorem~A) is the statement that the
chapters/theory/poincare_duality_quantum.tex:1148:\begin{theorem}[Bar-cobar adjunction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:bar-cobar-adjunction-operadic}
chapters/connections/thqg_introduction_supplement_body.tex:125:Theorem~A (the Verdier intertwining). The triangle is not built from
chapters/connections/thqg_introduction_supplement_body.tex:1633: Verdier intertwining (Theorem~A,
chapters/connections/thqg_introduction_supplement_body.tex:1830:Koszul dual $\cA^!$ & Theorem~A (Verdier intertwining) \\[2pt]
chapters/theory/chiral_modules.tex:28:Verdier intertwining (Theorem~\ref{thm:module-bar-verdier}) exchanges
chapters/theory/chiral_modules.tex:594:The Verdier intertwining
chapters/theory/chiral_modules.tex:603:one needs the \emph{module-level} Verdier intertwining: the functor
chapters/theory/chiral_modules.tex:617:full module-level Verdier intertwining is
chapters/theory/chiral_modules.tex:644:\begin{theorem}[Module-level Verdier intertwining; \ClaimStatusProvedHere]
chapters/theory/chiral_modules.tex:647:\index{conformal blocks!Verdier intertwining}
chapters/theory/chiral_modules.tex:4485:\begin{corollary}[\texorpdfstring{$\mathcal{W}$}{W}-algebra bar at dual level via DS and Verdier intertwining; \ClaimStatusProvedHere]\label{cor:ds-bar-level-shift}
 succeeded in 52ms:
The MC4 completion problem asks: \emph{when do these finite-stage
MC elements assemble to an MC element
$\widehat\tau \in
\MC\bigl(\widehat{\operatorname{Conv}}(\widehat{\bar B}^{\mathrm{ch}}(\cA),
\cA)\bigr)$
in the completed convolution algebra?}
The answer is that a single axiom on the filtration (that
the $A_\infty$~operations respect the additive weight) makes
the MC equation $\partial(\widehat\tau) + \widehat\tau \star
\widehat\tau = 0$ converge in the inverse limit. Each component
of this equation involves only finitely many terms
(Lemma~\ref{lem:degree-cutoff}), so the passage to the completion
is automatic.

\begin{definition}[Strong completion tower]
\label{def:strong-completion-tower}
\index{strong completion tower|textbf}
\index{completion closure!strong completion tower}
An augmented curved chiral $\Ainf$-algebra $\cA$ on a curve $X$ is a
\emph{strong completion tower} if it carries a descending filtration
 succeeded in 50ms:
\]
The right term vanishes because each $\epsilon_N$ is a quasi-isomorphism.
The left term vanishes because the surjective quotient tower is
Mittag--Leffler. Hence $\widehat\epsilon$ is a quasi-isomorphism.

\emph{Step~4: unit on the coalgebra side.}
By the same quotientwise argument: the quotient of $\widehat\eta$ modulo
$F^{N+1}$ is the finite-stage unit, which is a quasi-isomorphism.
Lemma~\ref{lem:complete-filtered-comparison} applies identically.
\end{proof}

\begin{proposition}[Strong filtration for the standard landscape;
\ClaimStatusProvedHere]
\label{prop:standard-strong-filtration}
\index{strong completion tower!standard families|textbf}
The following chiral algebras are strong completion towers
\textup{(}Definition~\textup{\ref{def:strong-completion-tower})}
with respect to the conformal weight \textup{(}$L_0$-eigenvalue\textup{)}
filtration $F^N\cA := \bigoplus_{h \geq N} \cA_h$:
\begin{enumerate}[label=\textup{(\alph*)}]
 succeeded in 50ms:
 \[
 \widehat\epsilon \colon
 \widehat\Omega^{\mathrm{ch}}\bigl(
 \widehat{\bar B}^{\mathrm{ch}}(\cA)\bigr)
 \longrightarrow \cA
 \]
 is a quasi-isomorphism. At each quotient this is the
 finite-stage acyclicity of~$\tau_N$; the passage to the
 limit uses the Milnor exact sequence with the
 Mittag--Leffler condition guaranteed by the strong
 filtration axiom.
\item \emph{Dual acyclicity.}
 If $C = \varprojlim_N C_{\le N}$ is a separated complete
 pronilpotent curved dg chiral coalgebra with every finite
 quotient in the theorematic regime, then the completed unit
 $\widehat\eta \colon C \to
 \widehat{\bar B}^{\mathrm{ch}}\bigl(
 \widehat\Omega^{\mathrm{ch}}(C)\bigr)$
 is a quasi-isomorphism.
\item \emph{Completed Koszul duality.}
exec
/bin/zsh -lc "rg -n \"def:bigraded-hochschild|ChirHoch\\"'^'"\\*\\(|RHH_ch|RHom|Ext\\"'^n_'"\\{\\\\mathrm\\{ChirAlg\\}\\}|Definition~\\\\ref\\{def:bigraded-hochschild\\}|def:chiral-hochschild-cochain-brace|prop:bar-resolution-chirhoch\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/koszul_pair_structure.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '120,220p' chapters/theory/koszul_pair_structure.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '450,540p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4560,4625p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:def:bigraded-hochschild|ChirHoch\^\*\(|RHH_ch|RHom|Ext\^n_\{\mathrm\{ChirAlg\}\}|Definition~\ref\{def:bigraded-hochschild\}|def:chiral-hochschild-cochain-brace|prop:bar-resolution-chirhoch)
                                                                   ^^
error: unrecognized escape sequence
 succeeded in 51ms:
\subsection{The universal twisting morphism}

The universal twisting morphism
$\pi\colon \barB_X(\cA) \to \cA$
(Proposition~\ref{prop:universal-twisting-adjunction}) controls
all bar-cobar identifications in this chapter. Twisting morphisms
are MC elements in the convolution algebra $\mathrm{Hom}(C, A)$
(Definition~\ref{def:twisting-morphism}). The natural bijection
$\mathrm{Tw}(C, A) \cong \mathrm{Hom}(C, B(A)) \cong
\mathrm{Hom}(\Omega(C), A)$
mediates the bar-cobar adjunction
(Proposition~\ref{prop:universal-twisting-adjunction}(iii)); for the
geometric realization as a propagator integral, see
Remark~\ref{rem:twisting-as-propagator}.

\begin{example}[Twisting for fermion-boson duality]
\label{ex:fermion-boson-twisting}
For the Koszul pair (free fermions $\mathcal{F}$, $\beta\gamma$
system), the universal twisting morphism
$\pi\colon \barB^{\mathrm{ch}}(\mathcal{F}) \to \mathcal{F}$
 succeeded in 51ms:

\section{Computing Hochschild cohomology via bar-cobar resolution}
\label{sec:hochschild-via-bar-cobar-complete}

\subsection{The bar-cobar resolution strategy}

The bar-cobar approach computes Hochschild cohomology via the quasi-isomorphism
$\ChirHoch^n(\mathcal{A}) = H^n\bigl(\mathrm{Hom}_{\mathsf{Alg}}(\Omega(\bar{B}(\mathcal{A})),
\mathcal{A})\bigr)$,
using the cofree coalgebra resolution $\bar{B}(\mathcal{A})$ and the free algebra resolution $\Omega(\bar{B}(\mathcal{A}))$.

\subsection{The fundamental quasi-isomorphism}

\begin{theorem}[Bar-cobar resolution; \ClaimStatusProvedHere]\label{thm:bar-cobar-resolution}
\textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For any chiral Koszul algebra $\mathcal{A}$ on a curve $X$
\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})},
 succeeded in 51ms:
 $\dfib^2 = \kappa \cdot \omega_g$. Main results: Theorems~B--D.
\end{enumerate}
Each level introduces new phenomena invisible to the previous one:
the chiral level brings integration kernels, OPE poles, and the
configuration-space geometry of $\FM_n(X)$ (Arnold relations,
logarithmic propagator); the modular level brings curvature,
central extensions, and anomalies. The classical and chiral levels
are \emph{not} identified by specializing to genus~$0$ on~$\bP^1$:
the chiral bar on~$\bP^1$ retains the full FM compactification
geometry, and the passage to the classical bar over a point requires
formal-disk restriction plus homotopy-transfer data (see the
discussion following Definition~\ref{def:chiral-koszul-pair}).
\end{remark}

\begin{proposition}[Three levels as MC at successive completions]
\label{prop:three-levels-mc-completion}
\ClaimStatusProvedHere
The three levels of Koszul structure (classical, chiral, and modular) correspond to the MC equation in successive completions of the convolution algebra:
\begin{enumerate}[label=\textup{(\roman*)}]
\item Classical: $\Theta_\cA^{(0,2)} \in \mathrm{MC}(\mathfrak{g}^{(0,\leq 2)}_\cA)$ (genus~$0$, degree~$2$).





thinking
**Considering complex resolutions**

I'm analyzing potential issues in moving from Ext in the ChirAlg framework to D_X-module morphisms on X, which seems unsupported. The resolution involves configuration spaces, which adds complexity since the Hom complex might be based on those spaces, not just the curve X. The de Rham amplitude is used to bound Ext, but previous theorems only show a quasi-isomorphism without confirming the Hom as a D_X-module complex of cohomological dimension 2. I need to check if any theorems clarify this further.
thinking
**Examining amplitude bounds**

I'm feeling a bit suspicious about the amplitude bound from curve X because the configuration spaces with n+2 points have a complex dimension of n+2. This means naively applying de Rham cohomology might yield high degrees. The proof collapses using bar concentration to q=0 diagonal, but to get n in {0,1,2}, they rely on D_X Ext and not on the configuration space dimension. I need to test if the logic is consistent here.

Theorem\ref{thm:bar-concentration} states that bar complex cohomology H^{p,q}(B) vanishes for q≠0, allowing p to be arbitrarily large. So, bar concentration alone doesn't guarantee Hochschild concentration in dimensions n≤2. The `main-koszul-hoch` theorem suggests that ChirHoch^n(A) could enforce vanishing for n>2, but it seems the theorem H proof doesn't leverage this effectively.
thinking
**Gathering line references**

I'm thinking that I need to note that the proof step uses `A^!` as input to cobar, which conflicts with the established object identity. I realize I need to find the exact lines — probably around line 575, so gathering line numbers is essential. I'll use `nl -ba` or `rg -n` to get precise references for final output. It’s important to produce exact line numbers for all relevant candidate findings!
thinking
**Clarifying theorem relevance**

It seems there are two levels to consider: the proof of the theorem itself versus how it's advertised. The user asked if Theorem H applies to all families, and I need to clarify. It specifically pertains to "chiral Koszul algebras on a smooth projective curve," not universally across all families. Additionally, some interpretations might misrepresent the theorem. I also notice a potential issue of circular reasoning in the proofs regarding Hochschild computations, but it might not be circular after all.
thinking
**Exploring Theorem H**

I'm noticing that Theorem H is coming up. The user is specifically asking about part (d). I think I should search through the chapters to see if there are any false mentions of `vdim`. Maybe using a regular expression around Theorem H could help clarify things. I'll focus on ensuring I'm thorough in my search and checking the context to address the user's question properly.
codex
I’m checking the AP134 question separately now: whether any theorem-H surface turns the `[0,2]` bound into a virtual-dimension claim rather than a cohomological amplitude claim.
exec
/bin/zsh -lc "rg -n \"vdim|virtual dimension|cohomological amplitude|amplitude \\[0,2\\]|Theorem H\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '29684,29698p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/guide_to_main_results.tex:56:\textbf{Theorem H} &
chapters/theory/chiral_hochschild_koszul.tex:755:cohomological amplitude~$[0, 2]$ (the de~Rham complex
chapters/theory/chiral_hochschild_koszul.tex:780:\index{Lagrangian self-intersection!Theorem H}
chapters/theory/higher_genus_modular_koszul.tex:29674:\index{Theorem H!holographic finite-dimensionality}
chapters/theory/higher_genus_modular_koszul.tex:29691:\item The amplitude $[0, 2]$ is a cohomological amplitude, not a
chapters/theory/higher_genus_modular_koszul.tex:29692: virtual dimension: it bounds the graded support of
 succeeded in 51ms:
(Theorem~\ref{thm:holo-comp-bulk-reconstruction}),
$\operatorname{ChirHoch}^*(\cA)$ is the bulk state space: its
nonzero classes are the bulk fields that the boundary algebra
supports. The Theorem~H bound therefore reads: the bulk built
from a modular Koszul chiral algebra carries finitely many states,
concentrated in three cohomological degrees.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The amplitude $[0, 2]$ is a cohomological amplitude, not a
 virtual dimension: it bounds the graded support of
 $\operatorname{ChirHoch}^*$, not the Euler characteristic.
\item The bound is a \emph{holographic finite-dimensionality}
 statement: the bulk state space is finite, with cardinality
 independent of the genus expansion of~$\cA$, and the
 holographic correction hierarchy
 \textup{(}Remark~\textup{\ref{rem:shadow-tower-holographic-interpretation}}\textup{)}
exec
/bin/zsh -lc "sed -n '8,22p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '108,118p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Koszul duality, but how rigid is the moduli it lives in? Without
knowing the tangent complex to
$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
bulk-field coupling remains inaccessible. The chiral Hochschild
complex $\ChirHoch^*(\cA)$ is that tangent complex;
Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
Koszul locus, so the MC moduli has cohomological
amplitude~$[0,2]$, and the Koszul duality
$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
is Verdier duality on this tangent space.

The cyclic deformation complex $\Defcyc(\cA)$
(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic
refinement of $\ChirHoch^*(\cA)$.
The complementarity
 succeeded in 52ms:
\begin{proof}
The Virasoro algebra is chirally Koszul
(Corollary~\ref{cor:universal-koszul}: freely strongly generated
implies bar concentration). Theorem~H
(Theorem~\ref{thm:hochschild-polynomial-growth}) gives concentration:
$\ChirHoch^n(\mathrm{Vir}_c) = 0$ for $n \notin \{0, 1, 2\}$,
since the de~Rham functor on a curve has cohomological
amplitude~$[0,2]$.

For the individual degrees:
$\ChirHoch^0(\mathrm{Vir}_c) = Z(\mathrm{Vir}_c) = \mathbb{C}$




thinking
**Reviewing theorem findings**

I’m not finding any misuse of vdim in theorem H surfaces, only some explicit corrections. The answer might lean toward amplitude rather than vdim. I might mention that there are no AP134 violations found on the core theorem surfaces, but since the user seems to want specific findings, I’ll focus on any actual discrepancies in the summary. I need to inspect the references in detail for both theorem H proof and the main-koszul-hoch. I could also check the potential weaknesses in the claims related to `thm:hochschild-bar-cobar`.
thinking
**Analyzing theorem proof steps**

This proof has three steps: citing the bar gives cofree resolution, the cobar gives free resolution, and then we have the definition of Ext. It might be a skeletal proof, and I'm unsure whether I can call it flawed unless there's a substantial lack of justification. Since part (a) of theorem H relies on it, any gaps become important. I wonder if Step 1's cofree resolution proves out as stated. If not, there's a risk considering theorem B or bar-cobar resolution. I need to check if all cited lemmas are actually proven.
thinking
**Clarifying theorem reliance**

I should note that the proof of theorem H depends on `thm:hochschild-bar-cobar`, which establishes only a bar-cobar model for `ChirHoch` through Hom in `ChirAlg`. However, it doesn’t seem to derive the de Rham amplitude bound that theorem H requires. That’s an important point to clarify. It might be better to emphasize this limitation to show how these elements are interconnected. So, I’ll make sure to highlight that distinction in my summary.
thinking
**Evaluating theorem H citations**

If `cor:universal-koszul` is cited in other contexts (like Vir proofs), it could exaggerate Kac-Moody at different levels. However, theorem H itself doesn’t reference this universal theorem. I noticed that theorem H is promoted alongside the critical level theorem included in discussions. It's interesting because theorem H notably excludes critical by Koszulness, and critical is addressed separately through BD comparison. Therefore, the universal theorem doesn’t encompass every family or level, and I should highlight that.
codex
The family scope is narrower than the concordance summary. I’m checking the affine KM `\ChirHoch^1` proposition now, because the main-table statement folds it into H even though critical level is already treated separately as non-Koszul.
exec
/bin/zsh -lc "sed -n '930,1010p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '840,930p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"prop:chirhoch1-affine-km|Generic affine first chiral Hochschild group|ChirHoch\\"'^1'"\\(V_k\" chapters/theory/chiral_hochschild_koszul.tex metadata/theorem_registry.md chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
metadata/theorem_registry.md:337:| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
chapters/connections/concordance.tex:67: $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
chapters/connections/concordance.tex:71: Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
chapters/connections/concordance.tex:377: Proposition~\ref{prop:chirhoch1-affine-km}).}
chapters/connections/concordance.tex:387: $\ChirHoch^1(V_k(\fg)) \cong \fg$
chapters/connections/concordance.tex:388: (Proposition~\ref{prop:chirhoch1-affine-km}).
chapters/connections/concordance.tex:7084:\ref{prop:chirhoch1-affine-km}
chapters/connections/concordance.tex:7085: & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
chapters/connections/concordance.tex:7086: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)}
chapters/connections/concordance.tex:9652:& $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
chapters/connections/concordance.tex:9653: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)} \\
 succeeded in 52ms:
\item All higher $\Etwo$-operations \textup{(}braces of
 degree~$\geq 3$, Massey products, $A_\infty$ corrections\textup{)}
 are cohomologically trivial.
\end{enumerate}
\end{proposition}

\begin{proof}
By Theorem~\ref{thm:hochschild-polynomial-growth},
$\ChirHoch^n(\cA) = 0$ for $n \notin \{0,1,2\}$.
The $\Etwo$-operations of degree~$k$ on $H^*(\ChirHoch(\cA))$
are maps
$H^{n_1} \otimes \cdots \otimes H^{n_k} \to H^{n_1 + \cdots + n_k - k + 1}$.
For $k \geq 3$, the source lives in total degree
$n_1 + \cdots + n_k \geq 0$ and the target in degree
$\leq n_1 + \cdots + n_k - 2$. Since each $n_i \in \{0,1,2\}$,
the target degree is at most $2k - 2$; but for the target to be
nonzero it must lie in $\{0,1,2\}$, which forces $2k - 2 \geq 0$
(automatic) and $n_1 + \cdots + n_k - k + 1 \leq 2$, i.e.\
$n_1 + \cdots + n_k \leq k + 1$. With each $n_i \geq 0$ and
$k \geq 3$ inputs, the inputs are almost all in degree~$0$.
 succeeded in 52ms:
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
Assume the full universal Maurer--Cartan element is scalar:
\begin{equation}\label{eq:one-channel-formality}
\Theta_{\cA}
\;=\;
\kappa(\cA) \cdot \eta \otimes \Lambda.
\end{equation}
Then the quantum $L_\infty$-structure is formal along the
distinguished scalar Maurer--Cartan orbit of\/~$\Theta_{\cA}$:
the higher transferred brackets vanish on the one-dimensional
scalar line $\mathbb{C}\!\cdot\!\eta \otimes \Lambda$, and the MC
equation restricts there to the scalar genus identities.
No converse is proved here. In particular, one-channel
minimal-model concentration
$\Theta_{\cA}^{\min} = \eta \otimes \Gamma_{\cA}$ does
\emph{not} by itself imply the scalar identity
\eqref{eq:one-channel-formality}.
\end{theorem}

\begin{proof}

thinking
**Searching for theorems**

Oops, it looks like I missed something around the proposition from 1924; I need to do a better search or check the theorem registry for that time. I'm considering exploring the area around 1900 in the chiral Hochschild-Koszul context, so I can get a clearer picture. I'll make sure to approach this systematically to not overlook any important details!
exec
/bin/zsh -lc "sed -n '1888,1955p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1955,2015p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Theorem~\ref{thm:modular-quantum-linfty} promotes it to a
\emph{quantum $L_\infty$-algebra} with operations
$\{\ell_n^{(g)}\}_{n \geq 1,\, g \geq 0}$: here
$\ell_1^{(0)} = D$, $\ell_2^{(0)} = [-,-]$,
$\ell_n^{(0)}$ for $n \geq 3$ are the higher operadic brackets from
homotopy transfer through $C_*(\overline{\mathcal{M}}_{0,n+1})$
(Loday--Vallette~\cite[Thm~10.3.8]{LV12}), and
$\ell_n^{(g)}$ for $g \geq 1$ are the higher-genus Feynman
amplitudes from stable-graph sums of type~$(g,n)$
(Getzler--Kapranov~\cite[\S5]{GeK98},
Chuang--Lazarev~\cite{CL10}).

The modular MC problem: find
$\Theta_\cA \in \MC(\Defcyc^{\mathrm{mod}}(\cA))$ satisfying the
quantum $L_\infty$ Maurer--Cartan equation
\[
\sum_{n \geq 1} \frac{1}{n!}\,\ell_n^{(0)}
 (\Theta_\cA,\dots,\Theta_\cA)
\;+\;
\sum_{g \geq 1} \hbar^{g}\,
 succeeded in 52ms:
\begin{theorem}[MC2-1 for Kac--Moody algebras;
\ClaimStatusProvedHere]\label{thm:mc2-1-km}
\index{MC2!Kac--Moody resolution}
For $\widehat{\mathfrak{g}}_k$ at non-critical level ($k \neq -h^\vee$)
with $\mathfrak{g}$ simple, Hypothesis~\textup{\ref{mc2-hyp:cyclic}}
is satisfied:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Cyclic $L_\infty$ structure.}
 The bar-intrinsic cyclic deformation complex
 \[
 \Defcyc(\widehat{\mathfrak{g}}_k)
 := \operatorname{CoDer}^{\mathrm{cyc}}(\widehat{\barB}_X
 (\widehat{\mathfrak{g}}_k))[1]
 \]
 is a well-defined complete cyclic $L_\infty$-algebra
 \textup{(}a fortiori: a cyclic dg~Lie algebra\textup{)}.

\item \emph{CE identification.}
 The coderivation differential $l_1 = [d_{\barB},-]$ is canonically
 identified with the cyclic Chevalley--Eilenberg differential:
exec
/bin/zsh -lc "rg -n \"label\\{prop:chirhoch1-affine-km\\}|prop:chirhoch1-affine-km\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4380,4475p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4475,4535p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_center_theorem.tex:2003:\label{prop:chirhoch1-affine-km}
chapters/theory/chiral_center_theorem.tex:2104:\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
chapters/theory/chiral_center_theorem.tex:2232:\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
chapters/theory/chiral_center_theorem.tex:2310:(Proposition~\ref{prop:chirhoch1-affine-km}), the
chapters/theory/introduction.tex:685: (Proposition~\ref{prop:chirhoch1-affine-km}).
chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
 succeeded in 50ms:
 tautological classes on $\mathcal{M}_g$ (\emph{nilpotent}, proved).
\end{itemize}

\emph{Step~3: Combined structure.}
The genuine period of $\mathcal{A}$ is governed by the periodic
operators only:
$\mathrm{Period}(\mathcal{A}) \mid \mathrm{lcm}(N_{\mathrm{mod}},
N_{\mathrm{quant}})$. The geometric contribution controls
the \emph{stabilization threshold}: bar cohomology dimensions
become $\mathrm{Period}(\mathcal{A})$-periodic in conformal weight
once the weight exceeds a threshold determined by the tautological
depth. On $\overline{\mathcal{M}}_g$ the depth is at most $3g-2$
(Theorem~\ref{thm:geometric-periodicity-weak}); on $\mathcal{M}_g$
the sharp bound is $g-1$
(Theorem~\ref{thm:geometric-depth-smooth}).
\end{evidence}

\begin{remark}[Scope]\label{rem:periodicity-classification-scope}
Conjectured because the modular bound
(Conjecture~\ref{conj:modular-periodicity}) is open. Quantum
 succeeded in 50ms:
$q \mapsto q^{-1}$. Since $[n]_{q^{-1}} = [n]_q$ for all $n$, the
Type~II quantum input is preserved under duality whenever that regime
applies.
\end{proof}

\begin{remark}[Modular period exchange]\label{rem:periodicity-exchange-harmonic}
% backward-compatible label removed (was conj:periodicity-exchange-harmonic)
Proposition~\ref{prop:periodicity-exchange-koszul} establishes
unconditionally that the geometric tautological depth is preserved and
that the dual modular phase bound is determined by the dual central
charge. In the admissible-level KL/DS regime it also preserves the
Type~II quantum input. The sum of reciprocal modular periods is given by
Conjecture~\ref{conj:reflected-modular-periodicity}: writing $c = p/q$
and $c' = p'/q'$,
\[
\frac{1}{N_{\text{mod}}} + \frac{1}{N'_{\text{mod}}}
= \frac{\gcd(p,24) + \gcd(p',24)}{24q}.
\]
This equals $\frac{1}{12}$ precisely when $\gcd(p,24) + \gcd(p',24) = 2q$; for $q = 1$ and $c + c' = 26$, this requires both $p$ and $26 - p$ coprime to~$24$ (e.g.\ $c = 1$, $c' = 25$ or $c = 7$, $c' = 19$, but \emph{not} $c = 5$, $c' = 21$ since $\gcd(21, 24) = 3$).
\end{remark}

thinking
**Inspecting theorem references**

It seems I couldn't find the proposition due to a wrong file. The relevant information might be in chiral_center_theorem.tex, although it may not directly relate to theorem H proof. Concordance does cite it, so I should mention that the KM generic linear term comes from a proposition in another file. It might be enough to note this, but I definitely need to check the chiral_center_theorem proposition to confirm its relevance to the theorem surface.
exec
/bin/zsh -lc "sed -n '1990,2035p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2035,2075p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
essential phenomenon: the first chiral Hochschild group
$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
This is not a coincidence special to rank one. For any simple Lie
algebra, the affine vertex algebra $V_k(\fg)$ at generic level is
chirally Koszul with generating space $V = \fg$; the Koszul resolution
is a three-term complex whose degree-$1$ piece is $\fg$ itself.
Degree-$1$ Hochschild cochains are infinitesimal deformations of the
current algebra: maps $J^a \mapsto J^a + \epsilon\,\phi^a$ preserving
the OPE to first order. The space of such deformations is determined
by the generating space alone, and the generating space is~$\fg$.
The deformation space of $V_k(\fg)$ \emph{is}~$\fg$.

\begin{proposition}[Generic affine first chiral Hochschild group; \ClaimStatusProvedHere]
\label{prop:chirhoch1-affine-km}
Let $\fg$ be a simple Lie algebra and let $V_k(\fg)$ be the affine
vertex algebra at generic level~$k$ \textup{(}$k \neq -h^\vee$\textup{)}.
Then
\[
\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
\]
 succeeded in 52ms:
0 \longrightarrow
\cA \otimes \fg^* \otimes \cA \longrightarrow
\cA \otimes \fg \otimes \cA \longrightarrow
\cA \otimes \cA \longrightarrow
\cA \longrightarrow 0,
\]
a three-term complex with generating space $V = \fg$. A degree-$1$
Hochschild cochain is a $\fg$-equivariant map from the generating
currents to the algebra:
\[
\phi \;\in\; \ChirHoch^1(V_k(\fg))
\quad\Longleftrightarrow\quad
J^a \;\longmapsto\; J^a + \epsilon\,\phi^a,
\qquad
\phi^a \in V_k(\fg).
\]
At generic level ($k \neq -h^\vee$), the Sugawara construction is
nondegenerate: the Segal--Sugawara vector is a well-defined conformal
vector, and the Kac--Shapovalov determinant is nonvanishing.
No singular vectors enter the generating filtration, and the



thinking
**Evaluating proof inconsistencies**

I'm noticing that this proof cites cor:universal-koszul, which raises some questions about critical-level inconsistency. I wonder if I really need to check the references to theorem H in the introduction or other chapters, especially regarding the claim about "explicit resolution length bounded by the number of generators." The user's focus seems to be on theorem H and its proof scope, particularly the Hilbert series, so I might want to keep the discussion centered there. I need to look more into theorem H.
thinking
**Clarifying spectral sequence**

I'm examining the statement about the Hochschild spectral sequence degenerating at E2 for Koszul algebras, noting that it involves some polynomial growth from this degeneration and finite-dimensional graded pieces. It feels distinct from the proof related to theorem H. I should check a specific line about family-specific Poincare polynomials, particularly for the Heisenberg case. The user seems to want to know about the Hilbert series, and I can clarify that theorem H only confirms the degree ≤2 polynomial while relating it to certain algebraic structures.
thinking
**Analyzing family-specific values**

I’m compiling some family-specific values for various algebraic cases. For the Heisenberg family, it's represented as 1+t+t^2, while both the Virasoro and principal W generic families show 1+t^2. The affine KM generic case includes terms like 1+dim(g)t+t^2, which I found through a proposition. However, for critical level affine algebras, the scenario is different, as they don't fit theorem H. I might want to check a specific line regarding Heisenberg again for accuracy.
codex
I have enough of the dependency chain to pin concrete failures. I’m collecting exact line references now so the final report only includes re-checked discrepancies, not speculative concerns.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '540,620p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '688,770p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1060,1132p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '58,72p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   540	\index{chiral Hochschild!descent from bar}
   541	The chiral Hochschild complex $\ChirHoch^{\bullet}(\cA)$ arises as
   542	the $\Sigma$-coinvariant descent of the bar complex
   543	$\bar{B}^{\mathrm{ch}}(\cA)$ along the Verdier intertwining
   544	$\mathbb{D}_{\Ran}$. Concretely, on the Koszul locus
   545	\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}
   546	there is a natural identification of chain complexes
   547	\begin{equation}
   548	\label{eq:chirhoch-descent}
   549	\ChirHoch^{\bullet}(\cA)
   550	\;\cong\;
   551	\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma},
   552	\end{equation}
   553	where $(-)_{\Sigma}$ denotes totalized $\Sigma_n$-coinvariants in
   554	bar degree~$n$.
   555	\end{lemma}
   556	
   557	\begin{proof}
   558	By the Verdier intertwining of Theorem~\ref{thm:bar-cobar-isomorphism-main}
   559	(Theorem~A), the Verdier dual
 succeeded in 51ms:
   688	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
   689	\label{thm:hochschild-polynomial-growth}
   690	\index{Hochschild cohomology!polynomial growth|textbf}
   691	\textup{[Regime: quadratic on the Koszul locus
   692	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   693	
   694	Let $\cA$ be a chiral Koszul algebra on a smooth projective curve~$X$,
   695	and let $\cA^!$ denote its Koszul dual. Then:
   696	\begin{enumerate}[label=\textup{(\alph*)}]
   697	\item \emph{Concentration.}\;
   698	 $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
   699	 The nonvanishing range is $0 \leq n \leq 2$.
   700	
   701	\item \emph{Polynomial growth.}\;
   702	 The Hochschild--Hilbert series
   703	 \[
   704	 P_{\cA}(t)
   705	 \;:=\;
   706	 \sum_{n \geq 0} \dim \ChirHoch^n(\cA)\,t^n
   707	 \]
 succeeded in 52ms:
  1060	
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
 succeeded in 51ms:
    58	 at all genera;
    59	 genus~$1$ universal for all families;
    60	 additivity and duality constraints;
    61	 Faber--Pandharipande free-energy formula
    62	 \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
    63	 & \ClaimStatusProvedHere \\
    64	\textbf{H} & Chiral Hochschild
    65	 & $\ChirHoch^*(\cA)$ polynomial with Hilbert polynomial
    66	 $P(t)=1+t^2$, Koszul-functorial;
    67	 $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
    68	 \textup{(}Thms~\ref{thm:w-algebra-hochschild},
    69	 \ref{thm:virasoro-hochschild},
    70	 \ref{thm:critical-level-cohomology};
    71	 Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
    72	 & \ClaimStatusProvedHere
exec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '52,62p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '96,132p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29678,29696p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    52	 duality ($\kappa + \kappa' = 0$ for KM/free fields),
    53	 and generates the genus tower via the $\hat{A}$-genus. &
    54	 Thm~\ref{thm:modular-characteristic} \\[4pt]
    55	
    56	\textbf{Theorem H} &
    57	 Chiral Hochschild: $\ChirHoch^*(\cA)$ has polynomial
    58	 growth, is Koszul-functorial, and admits an explicit
    59	 Koszul resolution of length bounded by the number
    60	 of generators. &
    61	 Thm~\ref{thm:hochschild-polynomial-growth} \\[4pt]
    62	
 succeeded in 51ms:
    96	\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
    97	For the Virasoro algebra at generic central charge $c$ (avoiding
    98	$c_{p,q} = 1 - 6(p-q)^2/(pq)$ and $c = 1$):
    99	\[\ChirHoch^n(\mathrm{Vir}_c) = \begin{cases}
   100	\mathbb{C} & n = 0 \text{ (center: scalars)}, \\
   101	0 & n = 1 \text{ (no outer derivations at generic $c$)}, \\
   102	\mathbb{C} & n = 2 \text{ (central charge deformation)}, \\
   103	0 & n \geq 3.
   104	\end{cases}\]
   105	The Hilbert series is $P(t) = 1 + t^2$.
   106	\end{theorem}
   107	
   108	\begin{proof}
   109	The Virasoro algebra is chirally Koszul
   110	(Corollary~\ref{cor:universal-koszul}: freely strongly generated
   111	implies bar concentration). Theorem~H
   112	(Theorem~\ref{thm:hochschild-polynomial-growth}) gives concentration:
   113	$\ChirHoch^n(\mathrm{Vir}_c) = 0$ for $n \notin \{0, 1, 2\}$,
   114	since the de~Rham functor on a curve has cohomological
   115	amplitude~$[0,2]$.
 succeeded in 51ms:
 29678	sharpens its physical content. The chiral Hochschild cohomology
 29679	$\operatorname{ChirHoch}^*(\cA)$ is concentrated in degrees
 29680	$\{0, 1, 2\}$ with polynomial Hilbert series
 29681	$P_\cA(t) = \dim Z(\cA) + \dim\operatorname{ChirHoch}^1(\cA)\cdot t + \dim Z(\cA^!)\cdot t^2$
 29682	(Theorem~\ref{thm:hochschild-polynomial-growth}). Under the
 29683	boundary-bulk reconstruction $\cA \mapsto Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$
 29684	(Theorem~\ref{thm:holo-comp-bulk-reconstruction}),
 29685	$\operatorname{ChirHoch}^*(\cA)$ is the bulk state space: its
 29686	nonzero classes are the bulk fields that the boundary algebra
 29687	supports. The Theorem~H bound therefore reads: the bulk built
 29688	from a modular Koszul chiral algebra carries finitely many states,
 29689	concentrated in three cohomological degrees.
 29690	\begin{enumerate}[label=\textup{(\roman*)}]
 29691	\item The amplitude $[0, 2]$ is a cohomological amplitude, not a
 29692	 virtual dimension: it bounds the graded support of
 29693	 $\operatorname{ChirHoch}^*$, not the Euler characteristic.
 29694	\item The bound is a \emph{holographic finite-dimensionality}
 29695	 statement: the bulk state space is finite, with cardinality
 29696	 independent of the genus expansion of~$\cA$, and the
exec
/bin/zsh -lc "nl -ba chapters/theory/koszul_pair_structure.tex | sed -n '700,708p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   700	\label{prop:periodicity-same-type}
   701	\index{periodicity!preservation under Koszul duality}
   702	For a Koszul pair $(\mathcal{A}, \mathcal{A}^!)$ where both algebras have the same type \textup{(}both Kac--Moody, both Virasoro, or both $\mathcal{W}_N$\textup{)}, the chiral Hochschild cohomology rings $\ChirHoch^*(\mathcal{A})$ and $\ChirHoch^*(\mathcal{A}^!)$ have the same growth type:
   703	\begin{enumerate}[label=\textup{(\roman*)}]
   704	\item \emph{Virasoro:} $\ChirHoch^*(\mathrm{Vir}_c)$ and $\ChirHoch^*(\mathrm{Vir}_{26-c})$ are both concentrated in $\{0, 2\}$ with $P(t) = 1 + t^2$ \textup{(}Theorem~\textup{\ref{thm:virasoro-hochschild}}\textup{)}.
   705	\item \emph{Kac--Moody:} $\ChirHoch^*(\widehat{\mathfrak{g}}_k)$ and $\ChirHoch^*(\widehat{\mathfrak{g}}_{k'})$ are both concentrated in $\{0, 1, 2\}$ with $P(t) = 1 + \dim(\mathfrak{g})\,t + t^2$ at generic level \textup{(}the Hilbert polynomial depends on~$\mathfrak{g}$, not on~$k$\textup{)}.
   706	\item \emph{$\mathcal{W}_N$:} $\ChirHoch^*(\mathcal{W}_N^k)$ and $\ChirHoch^*(\mathcal{W}_N^{k'})$ are both concentrated in $\{0, 1, 2\}$ with the same Hilbert polynomial, since the conformal weights $2, 3, \ldots, N$ are level-independent.
   707	\end{enumerate}
   708	\end{proposition}
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '618,641p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '741,760p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   618	Since $(\mathcal{A}, \mathcal{A}^!)$ is a Koszul pair, the bar coalgebra
   619	computes the Koszul dual coalgebra:
   620	$\bar{B}^{\mathrm{ch}}(\mathcal{A})^{\vee} \simeq \mathcal{A}^!$
   621	(Theorem~\ref{thm:e1-chiral-koszul-duality}). Therefore:
   622	\begin{align}
   623	\ChirHoch^n(\mathcal{A})
   624	&= \mathrm{Ext}^n_{\mathrm{ChirAlg}}(\mathcal{A}, \mathcal{A}) \notag \\
   625	&\cong H^n\bigl(\mathrm{Hom}(\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A})), \mathcal{A})\bigr) \notag \\
   626	&\cong H^n\bigl(\mathrm{Hom}(\Omega^{\mathrm{ch}}(\mathcal{A}^!), \mathcal{A})\bigr). \label{eq:hh-via-hom}
   627	\end{align}
   628	
   629	The chiral Hochschild complex in bar degree~$n$ lives on
   630	$\overline{C}_{n+2}(X)$, a smooth proper variety of complex dimension~$n+2$
   631	(since $\dim_{\mathbb{C}} X = 1$ and FM compactification preserves smoothness).
   632	Serre--Verdier duality for $\mathcal{D}$-modules on a smooth proper variety
   633	$Y$ of dimension~$d$ gives:
   634	\[
   635	H^j(Y, \mathcal{M}) \cong H^{d-j}(Y, \mathbb{D}\mathcal{M})^{\vee}
   636	\]
   637	where $\mathbb{D} = R\mathcal{H}\!\mathit{om}_{\mathcal{D}}({-}, \mathcal{D} \otimes \omega_Y^{-1})[\dim Y]$
 succeeded in 52ms:
   741	$\ChirHoch^n(\cA)
   742	= \mathrm{Ext}^n_{\mathrm{ChirAlg}(X)}(\cA, \cA)$.
   743	On the Koszul locus, bar concentration
   744	(Theorem~\ref{thm:bar-concentration}) gives a
   745	quasi-isomorphism $\barB^{\mathrm{ch}}(\cA) \simeq \cA^{!,\vee}$
   746	of graded chiral coalgebras. The bar-cobar resolution
   747	$\Omega^{\mathrm{ch}}(\barB^{\mathrm{ch}}(\cA))
   748	\xrightarrow{\sim} \cA$
   749	(Theorem~\ref{thm:bar-cobar-isomorphism-main})
   750	then provides a resolution of $\cA$ by free chiral algebras
   751	generated from the graded pieces of~$\cA^!$. The resulting
   752	Hom complex computing the Ext groups is a complex of
   753	$\mathcal{D}_X$-module morphisms on the curve~$X$. Since
   754	$\dim_{\mathbb{C}} X = 1$, the de~Rham functor on $X$ has
   755	cohomological amplitude~$[0, 2]$ (the de~Rham complex
   756	$\mathcal{O}_X \to \Omega^1_X$ has length~$2$, so
   757	$\mathrm{Ext}^n_{\mathcal{D}_X}(\cM, \cN) = 0$ for $n > 2$
   758	for holonomic $\mathcal{D}_X$-modules). The chiral algebra
   759	Ext inherits this bound: $\ChirHoch^n(\cA) = 0$ for
   760	$n \notin \{0, 1, 2\}$.\footnote{This is the chiral analogue
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '248,259p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '2003,2031p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   248	\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
   249	\index{Koszul morphism!chiral|textbf}
   250	A chiral twisting datum $(\cA, \cC, \tau, F_\bullet)$ is
   251	\emph{Koszul} if:
   252	\begin{enumerate}
   253	\item both $K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ are acyclic;
   254	\item the associated graded
   255	 $(\operatorname{gr}\cA, \operatorname{gr}\cC, \operatorname{gr}\tau)$
   256	 is quadratic/Koszul in the ordinary operadic sense;
   257	\item the filtration converges strongly on $\bar{B}_X(\cA)$ and
   258	 $\Omega_X(\cC)$.
   259	\end{enumerate}
 succeeded in 51ms:
  2003	\label{prop:chirhoch1-affine-km}
  2004	Let $\fg$ be a simple Lie algebra and let $V_k(\fg)$ be the affine
  2005	vertex algebra at generic level~$k$ \textup{(}$k \neq -h^\vee$\textup{)}.
  2006	Then
  2007	\[
  2008	\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
  2009	\]
  2010	as $\fg$-modules. In particular,
  2011	\[
  2012	\dim \ChirHoch^1(V_k(\fg)) = \dim(\fg),
  2013	\qquad
  2014	\dim \ChirHoch^1(V_k(\mathfrak{sl}_N)) = N^2 - 1.
  2015	\]
  2016	\end{proposition}
  2017	
  2018	\begin{proof}
  2019	The affine vertex algebra $V_k(\fg)$ is generated by weight-$1$
  2020	currents $\{J^a\}_{a=1}^{\dim(\fg)}$ with quadratic OPE
  2021	\[
  2022	J^a(z)\,J^b(w) \;\sim\;
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1338,1392p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1392,1422p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '165,196p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1338	
  1339	\begin{corollary}[Universal vertex algebras are chirally Koszul;
  1340	\ClaimStatusProvedHere]
  1341	\label{cor:universal-koszul}
  1342	\index{Koszul property!universal algebras}
  1343	
  1344	The following are chirally Koszul:
  1345	\begin{enumerate}
  1346	\item $V_k(\fg)$ at all levels~$k$ \textup{(}including $k = -h^\vee$\textup{)},
  1347	 since its vacuum module is Verma with no null vectors.
  1348	\item $\mathrm{Vir}_c$ as the universal vertex algebra at all~$c$,
  1349	 since the vacuum Verma module is freely strongly generated.
  1350	\item $\mathcal{W}^k(\fg)$ obtained by Drinfeld--Sokolov reduction,
  1351	 by the Feigin--Frenkel theorem \textup{(}the Miura images freely
  1352	 generate\textup{)}.
  1353	\end{enumerate}
  1354	
  1355	\noindent\textbf{The universal vs.\ simple distinction.}
  1356	The universal algebra $V_k(\fg)$ is always chirally Koszul.
  1357	The simple quotient $L_k(\fg) = V_k(\fg)/I_k$ may fail Koszulness
 succeeded in 51ms:
  1392	the full Koszulness
  1393	\textup{(}diagonal Ext concentration\textup{)}
  1394	holds at generic~$k$
  1395	but fails at $k = -h^\vee$.
  1396	Theorem~H
  1397	\textup{(Theorem~\ref{thm:hochschild-polynomial-growth})}
  1398	requires the diagonal criterion, so it does not apply at
  1399	critical level.
  1400	See Remark~\textup{\ref{rem:critical-level-lie-vs-chirhoch}}
  1401	for the Beilinson--Drinfeld comparison that replaces
  1402	Theorem~H at critical level.
  1403	\end{remark}
  1404	
  1405	\begin{theorem}[Kac--Shapovalov criterion for simple quotients;
  1406	\ClaimStatusProvedHere]
  1407	\label{thm:kac-shapovalov-koszulness}
  1408	\index{Koszul property!Kac--Shapovalov criterion}
  1409	\index{Kac determinant!Koszulness criterion}
  1410	\index{Shapovalov form!Koszulness criterion}
  1411	
 succeeded in 52ms:
   165	cohomology extends into arbitrarily high degrees.
   166	
   167	At \emph{critical} level ($k = -h^\vee$), chiral Koszulness
   168	fails: PBW degeneration (Proposition~\ref{prop:pbw-universality})
   169	still holds, but the Ext algebra $\mathrm{Ext}^{p,q}$ is not
   170	diagonally concentrated (the Feigin--Frenkel center
   171	$\mathrm{Fun}(\mathrm{Op})$ lives at bar degree $p = 0$ with
   172	conformal weight $q > 0$). Since Theorem~H requires diagonal
   173	Ext concentration (via bar concentration,
   174	Theorem~\ref{thm:bar-concentration}), Theorem~H does not apply
   175	at critical level.
   176	
   177	Instead, the Beilinson--Drinfeld comparison theorem
   178	(\cite{BD04}, Theorem~4.5.2) identifies the chiral Hochschild
   179	cohomology with the continuous Lie algebra cohomology:
   180	\[
   181	\ChirHoch^*(\widehat{\fg}_{-h^\vee})
   182	\;\cong\;
   183	H^*_{\mathrm{Lie,cont}}(\fg \otimes t\bC[[t]];\, \bC)
   184	\;\cong\;
exec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '328,336p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '205,252p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '694,731p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   328	degree-$2$ polynomial in~$t$.
   329	\end{remark}
   330	
   331	\begin{remark}[Non-principal nilpotent orbits]
   332	For general $\Walg^k(\mathfrak{g}, f)$ with $f$ not necessarily principal, the conformal weights of the generators are determined by the Kazhdan grading associated to the $\mathfrak{sl}_2$-triple $(e, h, f)$. The concentration $\ChirHoch^n = 0$ for $n > 2$ holds whenever the algebra is chirally Koszul (Theorem~H); the individual dimensions $\dim \ChirHoch^0$, $\dim \ChirHoch^1$, $\dim \ChirHoch^2$ depend on the center, derivations, and Koszul dual center for the specific orbit. For special orbits where Koszulness is open, the concentration bound remains conjectural.
   333	\end{remark}
   334	
   335	\section{Deformation theory}
   336	
 succeeded in 51ms:
   205	\begin{theorem}[W-algebra Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:w-algebra-hochschild}
   206	For the principal W-algebra $\Walg^k(\mathfrak{g}) = \Walg^k(\mathfrak{g}, f_{\mathrm{prin}})$ at generic level $k$
   207	(away from admissible and critical levels), the chiral Hochschild cohomology
   208	is concentrated in degrees $\{0, 1, 2\}$:
   209	\[\ChirHoch^n(\Walg^k(\mathfrak{g})) = 0 \quad \text{for } n \notin \{0, 1, 2\}.\]
   210	The nonvanishing degrees are:
   211	\begin{enumerate}[label=\textup{(\roman*)}]
   212	\item $\ChirHoch^0(\Walg^k(\mathfrak{g})) = Z(\Walg^k(\mathfrak{g})) = \mathbb{C}$
   213	 \textup{(}the center at generic~$k$ is one-dimensional\textup{)};
   214	\item $\ChirHoch^1(\Walg^k(\mathfrak{g})) = 0$ at generic~$k$
   215	 \textup{(}the Shapovalov form is non-degenerate, all derivations are
   216	 inner\textup{)};
   217	\item $\ChirHoch^2(\Walg^k(\mathfrak{g})) = \mathbb{C}$
   218	 \textup{(}the level deformation; equivalently,
   219	 $\dim Z((\Walg^k(\mathfrak{g}))^!) = 1$ by
   220	 Theorem~\textup{\ref{thm:main-koszul-hoch})}.
   221	\end{enumerate}
   222	The Hilbert series is $P(t) = 1 + t^2$.
   223	\end{theorem}
   224	
 succeeded in 51ms:
   694	Let $\cA$ be a chiral Koszul algebra on a smooth projective curve~$X$,
   695	and let $\cA^!$ denote its Koszul dual. Then:
   696	\begin{enumerate}[label=\textup{(\alph*)}]
   697	\item \emph{Concentration.}\;
   698	 $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
   699	 The nonvanishing range is $0 \leq n \leq 2$.
   700	
   701	\item \emph{Polynomial growth.}\;
   702	 The Hochschild--Hilbert series
   703	 \[
   704	 P_{\cA}(t)
   705	 \;:=\;
   706	 \sum_{n \geq 0} \dim \ChirHoch^n(\cA)\,t^n
   707	 \]
   708	 is a polynomial of degree at most~$2$. More precisely,
   709	 \begin{equation}\label{eq:hoch-hilbert-polynomial}
   710	 P_{\cA}(t)
   711	 \;=\;
   712	 \dim Z(\cA)
   713	 + \dim \ChirHoch^1(\cA)\,t


thinking
**Inspecting theorems and proofs**

I need to gather information about the bar-cobar resolution lines around 324 since the H proof cites it. It might be worth checking if unsupported inheritance from D_X is relevant, although it could be unnecessary. There seems to be a potential logical error in `lem:hochschild-shift-computation`: it suggests that Theorembar-concentration forces p=q on the surviving diagonal, while it actually states that q=0. That doesn't seem to add up, so let’s inspect this more closely.
thinking
**Verifying theorem statements**

In the lemma proof at line 529, it suggests that by theorem bar-concentration, it’s true that contributions only come from the diagonal for q=0. So the statement at line 600 claiming "p=q" seems wrong, but it might not matter if variable shifts are computed correctly. Still, the theorem itself uses p=q on the surviving diagonal, which contradicts the cited theorem. I need to check bigrading conventions and the statements in `lem:hochschild-shift-computation` for clarity.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '468,506p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   468	system), the universal twisting morphism
   469	$\pi\colon \barB^{\mathrm{ch}}(\mathcal{F}) \to \mathcal{F}$
   470	takes the explicit form
   471	$\pi(\psi^*)(z) = \operatorname{Res}_{w=z}\, \psi(w) \cdot \frac{dw}{z-w}$,
   472	implementing the fermion-boson correspondence at the MC level
   473	(Remark~\ref{rem:twisting-as-propagator}).
   474	\end{example}
   475	
   476	\subsection{Main duality theorem}\label{subsec:hochschild-duality}
   477	
   478	\begin{lemma}[Hochschild duality shift; \ClaimStatusProvedHere]
   479	\label{lem:hochschild-shift-computation}
   480	\index{Hochschild cohomology!duality shift computation}
   481	For a chiral Koszul pair $(\cA, \cA^!)$ on a smooth projective
   482	curve~$X$ of genus~$g$, the Verdier duality shift in the bigraded
   483	chiral Hochschild complex
   484	\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})}
   485	collapses to a uniform constant. More precisely, at bar degree~$p$
   486	the three grading contributions are:
   487	\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '506,538p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   506	
   507	\begin{proof}
   508	At bar degree~$p$, the Hochschild complex lives on the smooth proper
   509	variety $Y_p := \overline{C}_{p+2}(X)$ of complex dimension
   510	$d_p = p + 2$. Serre--Verdier duality for holonomic
   511	$\mathcal{D}$-modules on~$Y_p$ gives
   512	\[
   513	H^j(Y_p, \mathcal{M})
   514	\;\cong\;
   515	H^{d_p - j}(Y_p, \mathbb{D}\mathcal{M})^\vee,
   516	\]
   517	so the duality on the $p$-th bar summand carries a shift of~$[d_p] = [p+2]$.
   518	
   519	In the total complex, the $p$-th summand is placed in degree~$p$
   520	by the shift~$[-p]$, so the combined grading contribution at
   521	bar degree~$p$ is $(p+2) - p = 2$.
   522	
   523	It remains to see that this uniform value persists after passing to
   524	cohomology. By Theorem~\ref{thm:bar-concentration}, the bar
   525	cohomology $H^{p,q}(\barB^{\mathrm{ch}}(\cA))$ vanishes for
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '872,930p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '930,988p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
   890	 The Koszul dual $\widehat{\fg}_k^!$ has the same modular characteristic
   891	 as $\widehat{\fg}_{-k-2h^\vee}$, but the two are distinct
 succeeded in 50ms:
   930	\barBgeom(\operatorname{gr}_F \cA)
   931	\;=\; \barBgeom(\operatorname{Sym}^{\mathrm{ch}}(V))
   932	\end{equation}
   933	where $V$ is the generating $\mathcal{D}_X$-module.
   934	This identification holds because the bar differential on the
   935	associated graded sees only the leading-order OPE terms.
   936	For $\widehat{\fg}_k$: the singular OPE
   937	$J^a(z) J^b(w) \sim f^{ab}_c J^c(w)/(z-w)
   938	+ k\kappa^{ab}/(z-w)^2$
   939	reduces on $\operatorname{gr}_F$ to the commutative product
   940	(the bracket $f^{ab}_c J^c$ and level term $k\kappa^{ab}$ are
   941	lower-order in the PBW filtration).
   942	For $\mathrm{Vir}_c$: similarly, the Virasoro OPE reduces to a
   943	commutative product on the associated graded.
   944	
   945	\emph{Step~3: Computation of the $E_1$ page.}
   946	The $E_0$ page is
   947	$E_0^{p,q} = \operatorname{gr}^p_F \barBgeom^{p+q}(\cA)$,
   948	with $d_0$ the associated-graded bar differential.
   949	By~\eqref{eq:pbw-associated-graded-bar}, the $E_1$ page
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '988,1026p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   988	\[
   989	H^n(\barBgeom(\cA)) \cong E_\infty^{n,0}
   990	= E_2^{n,0}
   991	= H^n_{\mathrm{CE}}\!\bigl(\fg \otimes t^{-1}\bC[t^{-1}],\, \bC\bigr)
   992	= (\cA^!)_n.
   993	\]
   994	For commutative chiral algebras (e.g.\ the Heisenberg algebra),
   995	the Lie bracket of $\fg$ vanishes, $d_1 = 0$,
   996	$E_\infty = E_2 = E_1 = \Lambda(V^*)$, and the bar cohomology
   997	reduces to the exterior algebra. For non-abelian algebras
   998	(Kac--Moody, Virasoro), $d_1 \neq 0$ and the bar
   999	cohomology is computed by the CE cohomology, a proper
  1000	subquotient of $\Lambda(V^*)$.
  1001	
  1002	\emph{Step~5: Verification for $\widehat{\mathfrak{sl}}_2$.}
  1003	$V = \bC^3 \otimes t^{-1}\bC[t^{-1}]$
  1004	(three generators $J^+, J^0, J^-$, each with modes
  1005	$J^a_{-n}$ for $n \geq 1$).
  1006	The $E_1$ page has
  1007	$\dim {E_1}^{n,0}_h = \dim \Lambda^n(\bC^3 \otimes t\bC[t])_h$.
exec
/bin/zsh -lc "rg -n \"label\\{def:bigraded-hochschild\\}|bigraded chiral Hochschild complex\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "def:bigraded-hochschild|bigraded chiral Hochschild complex" chapters/theory chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:2682:\label{def:bigraded-hochschild}
chapters/theory/higher_genus_foundations.tex:2684:The \emph{bigraded chiral Hochschild complex} of a chiral
chapters/theory/higher_genus_foundations.tex:2707:Definition~\ref{def:bigraded-hochschild}.
chapters/theory/chiral_hochschild_koszul.tex:484:\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})}
chapters/theory/chiral_hochschild_koszul.tex:587:\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})} satisfies
chapters/theory/chiral_hochschild_koszul.tex:484:\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})}
chapters/theory/chiral_hochschild_koszul.tex:587:\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})} satisfies
chapters/theory/higher_genus_foundations.tex:2682:\label{def:bigraded-hochschild}
chapters/theory/higher_genus_foundations.tex:2684:The \emph{bigraded chiral Hochschild complex} of a chiral
chapters/theory/higher_genus_foundations.tex:2707:Definition~\ref{def:bigraded-hochschild}.

thinking
**Reading definitions and supporting theorems**

I need to check the definition that could potentially support theorem H. Understanding foundational concepts is usually key for grasping more complex ideas. I want to make sure I’m clear about how they connect to each other. If there’s a specific aspect of theorem H that stands out, I should highlight that too, as it might clarify why this definition is important. Let's take a moment to dive deeper into both!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2682,2714p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2714,2740p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2682	\label{def:bigraded-hochschild}
  2683	\index{Hochschild cohomology!bigraded|textbf}
  2684	The \emph{bigraded chiral Hochschild complex} of a chiral
  2685	algebra~$\cA$ on a smooth curve~$X$ is the double complex
  2686	\[
  2687	CH^{p,\bullet}_{\mathrm{ch}}(\cA) :=
  2688	R\mathrm{Hom}_{\mathcal{D}_{\overline{C}_{p+2}(X)}}
  2689	\bigl(\cA^{\boxtimes(p+2)}, \omega_{\overline{C}_{p+2}(X)}\bigr)
  2690	\]
  2691	at bar degree~$p$, with the total object
  2692	\[
  2693	RHH_{\mathrm{ch}}(\cA) :=
  2694	\operatorname{Tot}\!\left(
  2695	\bigoplus_{p \geq 0} CH^{p,\bullet}_{\mathrm{ch}}(\cA)[-p]
  2696	\right).
  2697	\]
  2698	At bar degree~$p$, the configuration space
  2699	$\overline{C}_{p+2}(X)$ has complex dimension~$p + 2$
  2700	\textup{(}since $\dim_\C X = 1$\textup{)}, and Verdier duality
  2701	contributes a shift of~$p+2$.
 succeeded in 50ms:
  2714	The formal degree accounting is carried out in
  2715	Lemma~\ref{lem:hochschild-shift-computation}
  2716	(Chapter~\ref{chap:deformation-theory}).
  2717	\end{remark}
  2718	
  2719	% ================================================================
  2720	% SECTION 4.10: HIGHER GENUS CONFIGURATION SPACES - COMPLETE THEORY
  2721	% ================================================================
  2722	
  2723	\section{Higher-genus configuration spaces}
  2724	\label{sec:higher-genus-config-complete}
  2725	
  2726	\subsection{The genus stratification philosophy}
  2727	
  2728	\begin{remark}[Genus as quantum number]
  2729	\label{rem:genus-quantum}
  2730	The genus $g$ organizes corrections: at genus~$0$ the bar differential satisfies~$d^{(0)2} = 0$ exactly (the Arnold relation ensures nilpotency on the curve; on the formal disk this recovers the classical statement), genus~$1$ produces central extensions, and genus $g \geq 2$ introduces modular structures.
  2731	
  2732	This parallels the loop expansion in quantum field theory:
  2733	\begin{equation}
codex
I’ve confirmed the core Vol I discrepancies. I’m doing one quick cross-volume grep for Theorem H’s advertised shape so the report can say whether the drift is local or already propagated into Vol II/III.
exec
/bin/zsh -lc "rg -n \"Theorem H|hochschild-polynomial-growth|\\{0, ?1, ?2\\}|P\\(t\\)=1\\+t\\"'^2|dim Z'"\\(.*\\)\\+.*t\\+.*t\\"'^2|virtual dimension|cohomological amplitude" /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem H|hochschild-polynomial-growth|P\\(t\\)=1\\+t\\"'^2|ChirHoch'"\\"'^1'"\\(V_k\\(\\\\fg\\\\)\\)\" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2467:The virtual dimension of all moduli problems on $K3 \times E$
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:223: \item[Theorem H (Hochschild).] $\ChirHoch^*(A_\cC)$ is polynomial in degrees $\{0, 1, 2\}$, and the CY Hochschild calculus of $\cC$ (HKR decomposition, Connes operator, categorical Hodge structure) is faithfully reflected in $\ChirHoch^*(A_\cC)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:312:\section{Categorical Theorem H}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:320:\begin{theorem}[Categorical Theorem H]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:1349:scheme $X$ of virtual dimension zero is the Euler class of the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/concordance.tex:139:Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:2798:$k \geq 2$: despite bounded cohomological amplitude, the algebraic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:345:of the virtual dimension $\mathrm{vdim} = 1 - n^2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:389:$(-1)^{n-1}$ comes from the virtual dimension
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_frontier.tex:392:weight structure, not the virtual dimension directly).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1288:\index{five main theorems!E1@$E_1$ variant!Theorem H}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1290:The Hilbert series is $P(t)=1+t^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3073:The cohomological amplitude of $Z(U_\cA)$ is $[0,2]$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:3158:states constrained by Theorem~H's cohomological amplitude
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:5864:states; Theorem~H's concentration bound (cohomological amplitude $[0,2]$) constrains the bulk
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2744:\item \textbf{Theorem H} (Hochschild, at generic level): the chiral Hochschild
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1346:\index{five main theorems!E1@$E_1$ variant!Theorem H}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2268:$P(t)=1+t^2$.
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:109:**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input -> E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input -> E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input -> E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X -> chiral, R -> topological, CY category -> categorical.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:309:| Hochschild | BV-BRST origin of Thm H | Theorem H | Proved |
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:109:(i) Topological HH: E_1-algebra input -> E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input -> concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input -> E_2 with CY shifted Poisson. The geometry determines which Hochschild: curve X -> chiral, R -> topological, CY category -> categorical. NEVER conflate. Bare "Hochschild" MUST carry qualifier (chiral/topological/categorical) in non-historical contexts.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_drinfeld_double_wave11.md:32:### F-CRIT-1: Internal contradiction between comp:tamarkin-e2-heisenberg and Theorem H (amplitude bound)
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_drinfeld_double_wave11.md:34:At hochschild.tex:294-302, comp:tamarkin-e2-heisenberg computes `V_T = C^*(H_k, H_k) ≅ k[[κ]]` as a formal power series ring: INFINITE-dimensional as a graded vector space. At hochschild.tex:1691-1695, Part (c) invokes this exact computation then writes "truncated to the amplitude bound of Theorem H, the surviving piece is k<1,κ> with total dimension two." But Vol I Theorem H is a **theorem**, not a filter: it says `total_dim(ChirHoch*(A)) ≤ 4`, so if comp:tamarkin-e2-heisenberg is correct it already contradicts Theorem H, and the Drinfeld-center-equals-bulk base case (comp:drinfeld-center-heisenberg at 1685-1697) depends on this "truncation" to reach `Z(U_{H_k}) ≅ k<1, κ>` with dim 2. CLAUDE.md AP94-AP98 and the audit notes at compute/audit/complete_frontier_status_2026_04_08.md:290 already flag this exact inconsistency as a known issue ("polynomial" was corrected to "polynomial growth of Betti numbers, not a polynomial algebra"), but comp:tamarkin-e2-heisenberg was not updated in the sweep. Part (c) inherits the stale computation and papers over the contradiction by calling Theorem H a "truncation." Either comp:tamarkin-e2-heisenberg is wrong (it should be a finite complex of total dim ≤ 4), or Theorem H does not apply to H_k (class G), or the two objects are different. All three resolutions demand explicit statement; the current text contains a logical cycle.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_drinfeld_double_wave11.md:129:- Z(U(A)) ≃ ChirHoch*(A), bounded to dim ≤ 4 by Theorem H (Part c)
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_drinfeld_double_wave11.md:221:1. **F-CRIT-1:** `comp:tamarkin-e2-heisenberg` says `V_T ≅ k[[κ]]` (infinite-dim) but Theorem H says total dim ≤ 4. Part (c) "truncates" to dim 2; Theorem H is not a truncation but a theorem. Internal Vol II contradiction that the Drinfeld-center-equals-bulk Heisenberg base case depends on.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_drinfeld_double_wave11.md:266:5. **Part (c) comp:drinfeld-center-heisenberg**: demote from `\ClaimStatusProvedHere` to `\ClaimStatusHeuristic` pending resolution of F-CRIT-1 (the contradiction between V_T = k[[κ]] and Theorem H amplitude bound).
/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_hochschild_bulk_bridge.py:11:  Vol I: chiral_hochschild_koszul.tex (Theorem H), concordance.tex
/Users/raeez/chiral-bar-cobar-vol2/compute/tests/test_hochschild_bulk_bridge.py:33:    This is Theorem H of Vol I.
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/universal_modular_deformation_theorem.md:51:(E) Hochschild: ChirHoch*(A) is the Theta-twisted cohomology of the genus-0 convolution algebra (thm:hochschild-polynomial-growth).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:19:  Vol I: chiral_hochschild_koszul.tex (Theorem H), concordance.tex
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:25:  This follows from the PBW filtration and Koszulness (Theorem H).
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:290:    For Koszul chiral algebras (Theorem H), ChirHoch*(A) is a polynomial
/Users/raeez/chiral-bar-cobar-vol2/compute/lib/hochschild_bulk_bridge.py:297:    This is the content of Theorem H: the Poincare polynomial of
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:223: \item[Theorem H (Hochschild).] $\ChirHoch^*(A_\cC)$ is polynomial in degrees $\{0, 1, 2\}$, and the CY Hochschild calculus of $\cC$ (HKR decomposition, Connes operator, categorical Hodge structure) is faithfully reflected in $\ChirHoch^*(A_\cC)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:312:\section{Categorical Theorem H}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:320:\begin{theorem}[Categorical Theorem H]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1290:The Hilbert series is $P(t)=1+t^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:1288:\index{five main theorems!E1@$E_1$ variant!Theorem H}

thinking
**Inspecting cross-volume details**

I'm looking at the cross-volume grep results showing propagation. I think I should examine specific lines in volumes 2 and 3 to confirm the details. The search output provided those lines, which could be useful. It might be good to mention the cross-volume drift at the connections in vol2 or in vol3. I should definitely inspect those relevant lines to ground my understanding. Let's check them out!
exec
/bin/zsh -lc "sed -n '2742,2748p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '220,226p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1284,1294p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
conformal weight is inner, so $H^1=0$. The map
$\partial_c\colon T\otimes T \mapsto \partial_c\{T_\lambda T\}$
is a $2$-cochain (it differentiates the binary operation, not
a single element), and is not a coboundary
(it shifts the central term without being generated by
any inner $1$-cochain), so $H^2=\Bbbk\langle\Theta_c\rangle$.
The Hilbert series is $P(t)=1+t^2$.
\end{computation}

\begin{computation}[Bulk algebra for $\mathcal W_3$;
\ClaimStatusProvedHere]
 succeeded in 52ms:
\item \textbf{Theorem D} (modular characteristic): the first
 cumulant is $\kappa(\cA)$.
\item \textbf{Theorem H} (Hochschild, at generic level): the chiral Hochschild
 cohomology is polynomial in the cumulants. The critical level $k = -h^\vee$
 is excluded because $\dim \ChirHoch^0$ can be infinite there
 (see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
\end{enumerate}
 succeeded in 52ms:

 \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).

 \item[Theorem H (Hochschild).] $\ChirHoch^*(A_\cC)$ is polynomial in degrees $\{0, 1, 2\}$, and the CY Hochschild calculus of $\cC$ (HKR decomposition, Connes operator, categorical Hodge structure) is faithfully reflected in $\ChirHoch^*(A_\cC)$.
\end{description}
\end{theorem*}

exec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '389,406p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   389	
   390	For the Heisenberg algebra:
   391	\[\ChirHoch^n(\text{Heis}_k) = \begin{cases}
   392	\mathbb{C} & n = 0 \text{ (center: only scalars commute with all of } \text{Heis}_k) \\
   393	\mathbb{C} & n = 1 \text{ (outer derivation } D(\alpha)=\mathbf{1}\text{; zero mode is central)} \\
   394	\mathbb{C} & n = 2 \text{ (central extension: the level deformation)} \\
   395	0 & n \geq 3
   396	\end{cases}\]
   397	
   398	For free fermions (with OPE $\psi(z)\psi^*(w) \sim (z-w)^{-1}$):
   399	\[\ChirHoch^n(\text{Fermions}) = \begin{cases}
   400	\mathbb{C} & n = 0 \text{ (center: only scalars)} \\
   401	0 & n = 1 \text{ (all derivations of the Clifford algebra are inner)} \\
   402	\mathbb{C} & n = 2 \text{ (one-dimensional deformation space)}
   403	\end{cases}\]
   404	(The computation follows from the Clifford algebra structure: $HH^0$ is the center $\mathbb{C}$; $HH^1 = 0$ by the standard result that all derivations of a Clifford algebra are inner \cite[Ch.~9]{Weibel94}; $HH^2 \cong \mathbb{C}$ represents the unique deformation parametrized by the level.)
   405	\section{Hochschild-cyclic spectral sequence for chiral algebras}
   406	\label{sec:hochschild-cyclic-spectral}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29694,29706p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 29694	\item The bound is a \emph{holographic finite-dimensionality}
 29695	 statement: the bulk state space is finite, with cardinality
 29696	 independent of the genus expansion of~$\cA$, and the
 29697	 holographic correction hierarchy
 29698	 \textup{(}Remark~\textup{\ref{rem:shadow-tower-holographic-interpretation}}\textup{)}
 29699	 corrects at most four bulk fields. Every degree-$r$ shadow
 29700	 $S_r(\cA)$ is a coefficient of an effective vertex acting on a
 29701	 four-or-fewer-dimensional bulk space.
 29702	\item The bound is tight in the sense that each of the four
 29703	 depth classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$,
 29704	 $\mathbf{M}$ realizes a distinct bulk state count: class
 29705	 $\mathbf{G}$ with one state, class $\mathbf{L}$ with two, and
 29706	 class $\mathbf{C}$ with three, and class $\mathbf{M}$ saturating
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29706,29710p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 29706	 class $\mathbf{C}$ with three, and class $\mathbf{M}$ saturating
 29707	 at four
 29708	 \textup{(}cross-reference to the bar cohomology dimensions
 29709	 tabulated in \S\ref{subsec:shadow-postnikov-tower}\textup{)}.
 29710	\end{enumerate}




thinking
**Verifying theorem reasoning**

I need to confirm whether the proof of theorem H involves circular reasoning. It seems like the special family of theorems could rely on theorem H instead of the other way around. If that's true, I wouldn't find any circularity there. I'll have to double-check to make sure my understanding is accurate, as sorting this out might be crucial for aligning my thoughts correctly on the overall argument structure.
thinking
**Evaluating Hilbert series and reports**

I’m considering the user’s request to read and report rather than using a search compute script. It seems important to independently verify the Hilbert series through tests, as that could be useful. I remember that there might be tests related to this in volume 2 of the compute reference. However, I also note that theorem H's claims may not have robust computational backing. Still, we have enough direct evidence in the repository to support our assertions.
thinking
**Summarizing findings clearly**

I’m thinking about putting a summary after my findings or maybe a bit lower. The final summary can indicate that the amplitude/virtual dimension distinction is handled correctly in the theorem-H discussion, and no AP134 violation was found in the inspected surfaces. Since the user is asking for specific insights, I want to keep my summary concise but structured. Maybe just mention, "AP134 check: no violation found; core surfaces state amplitude, not virtual dimension," for clarity. I’ll avoid listing non-violations in the findings.
thinking
**Verifying reasoning and findings**

I should probably mention that no circular reasoning was found, but I also see that the theorem H proof, while not circular, is defective. The user asked specifically about circular reasoning, so that’s important to clarify. The object-conflation and scope issues are significant enough to include. I also need to verify if cross-volume volumes are accessible. If I include that finding, I’ll need to provide exact line numbers using the `nl -ba` command. I’ll gather those details next.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex | sed -n '1288,1292p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex | sed -n '2743,2747p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex | sed -n '222,224p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1288	(it shifts the central term without being generated by
  1289	any inner $1$-cochain), so $H^2=\Bbbk\langle\Theta_c\rangle$.
  1290	The Hilbert series is $P(t)=1+t^2$.
  1291	\end{computation}
  1292	
 succeeded in 51ms:
  2743	 cumulant is $\kappa(\cA)$.
  2744	\item \textbf{Theorem H} (Hochschild, at generic level): the chiral Hochschild
  2745	 cohomology is polynomial in the cumulants. The critical level $k = -h^\vee$
  2746	 is excluded because $\dim \ChirHoch^0$ can be infinite there
  2747	 (see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
 succeeded in 51ms:
   222	
   223	 \item[Theorem H (Hochschild).] $\ChirHoch^*(A_\cC)$ is polynomial in degrees $\{0, 1, 2\}$, and the CY Hochschild calculus of $\cC$ (HKR decomposition, Connes operator, categorical Hodge structure) is faithfully reflected in $\ChirHoch^*(A_\cC)$.
   224	\end{description}

thinking
**Inspecting mathematical proofs**

I want to be careful not to make claims unsupported by the entire repository, especially regarding the proposition bar-resolution-chirhoch. I realize I haven't read it yet. The user asked for each step of the proof and its direct dependencies. Maybe I should inspect `prop:bar-resolution-chirhoch` closely. I need to search and see if it discusses the actual complex `C^*_ch(A,A)` computed by bar resolution across degrees 0 to 2. It's better to be thorough to avoid any false positives.
codex
One dependency remains unchecked: the bar-resolution proposition cited immediately after the theorem statement. I’m reading that now to make sure the Ext-to-cochain identification doesn’t already repair the degree bound.
exec
/bin/zsh -lc "sed -n '1840,1908p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:bar-resolution-chirhoch|bar resolution.*chirhoch|chiral-hochschild-cochain-brace" chapters/theory/chiral_center_theorem.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1908,1968p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{derived center!affine Kac--Moody|textbf}
\index{derived center!Virasoro|textbf}
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Heisenberg $\mathfrak{H}_k$.)}
 The chiral Hochschild cohomology is
 \[
 \ChirHoch^n(\mathfrak{H}_k, \mathfrak{H}_k)
 \;=\;
 \begin{cases}
 \bC & n = 0, \\
 \bC & n = 1, \\
 \bC & n = 2, \\
 0 & n \geq 3.
 \end{cases}
 \]
 The generators are:
 $1 \in \ChirHoch^0$ \textup{(}the vacuum, center of~$\mathfrak{H}_k$\textup{)},
 $\xi_k \in \ChirHoch^1$ \textup{(}the level deformation
 $k \mapsto k + \epsilon$\textup{)}, and
 $\eta \in \ChirHoch^2$ \textup{(}the dual vacuum, the obstruction
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:36:(Definition~\ref{def:chiral-hochschild-cochain-brace},
chapters/theory/chiral_center_theorem.tex:299:\label{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:349:Definition~\ref{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:1917: complex of Definition~\ref{def:chiral-hochschild-cochain-brace}.
chapters/theory/chiral_hochschild_koszul.tex:737:The derived chiral Hochschild complex $\mathrm{RHH}_{\mathrm{ch}}(A)$ is computed by the algebraic cochain complex $C^*_{\mathrm{ch}}(A, A)$ of Definition~\ref{def:chiral-hochschild-cochain-brace} (\texttt{chiral\_center\_theorem.tex}), which in turn is identified with $\mathrm{RHom}_{\mathsf{ChirAlg}}(A, A)$ via the bar resolution (Proposition~\ref{prop:bar-resolution-chirhoch}).
chapters/theory/chiral_center_theorem.tex:36:(Definition~\ref{def:chiral-hochschild-cochain-brace},
chapters/theory/chiral_center_theorem.tex:299:\label{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:349:Definition~\ref{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:1917: complex of Definition~\ref{def:chiral-hochschild-cochain-brace}.
 succeeded in 50ms:
 Note that the continuous Lie algebra cohomology
 $H^*_{\mathrm{cont}}(\mathrm{Vect}(S^1);\,\bC)$
 (Gel'fand--Fuchs cohomology) is infinite-dimensional; it is a
 \emph{different object} from $\ChirHoch^*(\mathrm{Vir}_c)$,
 which is bounded in degrees $\{0, 2\}$ with total dimension~$2$.
 The former is computed from the topological Lie algebra of
 smooth vector fields on~$S^1$ (no central charge, no chiral
 structure); the latter is computed from the vertex algebra
 $\mathrm{Vir}_c$ on a formal disc via the chiral Hochschild
 complex of Definition~\ref{def:chiral-hochschild-cochain-brace}.
\end{enumerate}
\end{proposition}

\begin{proof}
\textbf{Part~(i).}
The Heisenberg algebra $\mathfrak{H}_k$ is generated by a single
weight-$1$ field $a(z)$ with OPE $a(z)\, a(w) \sim k/(z-w)^2$.
Since $\mathfrak{H}_k$ is quadratic (only binary OPE), it is
chirally Koszul
(Corollary~\ref{cor:universal-koszul}), and the bar cohomology is

thinking
**Searching for theorem proof**

I see that this isn't directly repairing the theorem H proof. I’m thinking I should check `prop:bar-resolution-chirhoch`, which I can't find. Maybe the relevant file continues after 1908 or the proposition comes after that? I need to search for the exact label, but I'm not entirely sure I'd still find it. So, I'll go ahead and do another search to see if I can locate the right information.
exec
/bin/zsh -lc 'rg -n "bar-resolution-chirhoch" chapters/theory/chiral_center_theorem.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:737:The derived chiral Hochschild complex $\mathrm{RHH}_{\mathrm{ch}}(A)$ is computed by the algebraic cochain complex $C^*_{\mathrm{ch}}(A, A)$ of Definition~\ref{def:chiral-hochschild-cochain-brace} (\texttt{chiral\_center\_theorem.tex}), which in turn is identified with $\mathrm{RHom}_{\mathsf{ChirAlg}}(A, A)$ via the bar resolution (Proposition~\ref{prop:bar-resolution-chirhoch}).
exec
/bin/zsh -lc "rg -n \"e1-chiral-koszul-duality|label\\{thm:e1-chiral-koszul-duality\\}\" chapters/theory chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex:2140:construction of Theorem~\ref{thm:e1-chiral-koszul-duality}, indexed by
chapters/examples/lattice_foundations.tex:3168:(Theorem~\ref{thm:e1-chiral-koszul-duality}).
chapters/examples/lattice_foundations.tex:3217:(Theorem~\ref{thm:e1-chiral-koszul-duality}) and the self-duality of
chapters/examples/lattice_foundations.tex:3944:Theorem~\ref{thm:e1-chiral-koszul-duality}). The Verdier
chapters/examples/yangians_foundations.tex:697:Theorem~\ref{thm:e1-chiral-koszul-duality} then applies:
chapters/examples/yangians_foundations.tex:891:equivalence by Theorem~\ref{thm:e1-chiral-koszul-duality}, and the
chapters/examples/toroidal_elliptic.tex:243:(Theorem~\ref{thm:e1-chiral-koszul-duality}) applies to the
chapters/examples/toroidal_elliptic.tex:266:\item \emph{RTT presentation.} By $\Eone$-chiral Koszul duality (Theorem~\ref{thm:e1-chiral-koszul-duality}), the dual has $R$-matrix $R(u;q,t)^{-1} = R(u;q^{-1},t^{-1})$ (Ding--Iohara inversion; cf.\ Theorem~\ref{thm:yangian-koszul-dual}).
chapters/examples/landscape_census.tex:1059: \textup{(}Theorems~\ref{thm:e1-chiral-koszul-duality},
chapters/examples/landscape_census.tex:1460:Theorem~\ref{thm:e1-chiral-koszul-duality});
chapters/theory/algebraic_foundations.tex:313:Theorem~\ref{thm:e1-chiral-koszul-duality}.
chapters/examples/yangians_drinfeld_kohno.tex:664:\textbf{DK-0/1}: chain-level braided bar-cobar (Theorems~\ref{thm:e1-chiral-koszul-duality}--\ref{thm:derived-dk-yangian}) and evaluation-locus factorization DK (Theorem~\ref{thm:factorization-dk-eval}), proved. \textbf{DK-2/3}: the type-$A$ thick-generation input is proved, but the promotion beyond generators is only conditional on the ambient extension/comparison package of Theorem~\ref{conj:dk-fd-typeA}; a separate sectorwise-convergence route exists at the H-level for all types (Corollary~\ref{cor:dk23-all-types}). Category-$\mathcal{O}$ extension remains conjectural (Conjecture~\ref{conj:full-derived-dk}; see Corollary~\ref{cor:dk-partial-conj}). \textbf{DK-4}: structural framework proved (MC4 closed, Theorem~\ref{thm:completed-bar-cobar-strong}); algebraic identification $\varprojlim \mathfrak{g}_N \cong Y^{\mathrm{dg}}_\cA$ remains open (Conjecture~\ref{conj:dk4-inverse-limit}). \textbf{DK-5}: conjectural (Conjecture~\ref{conj:full-dk-bridge}; see Remark~\ref{rem:yangian-dk23-inputs} for exact inputs). \ifannalsedition\else
chapters/examples/yangians_drinfeld_kohno.tex:903:Theorem~\ref{thm:e1-chiral-koszul-duality} gives the
chapters/examples/w_algebras.tex:397:For $k \neq -h^\vee$, the W-algebra has non-trivial curvature $m_0 \neq 0$ (Theorem~\ref{thm:w-bar-curvature}). The bar-cobar adjunction of Theorem~\ref{thm:e1-chiral-koszul-duality} gives a curved $A_\infty$ quasi-isomorphism:
chapters/theory/chiral_koszul_pairs.tex:4793:\label{thm:e1-chiral-koszul-duality}
chapters/theory/chiral_koszul_pairs.tex:4990:Theorem~\ref{thm:e1-chiral-koszul-duality} simplifies dramatically:
chapters/theory/chiral_koszul_pairs.tex:5049:Theorem~\ref{thm:e1-chiral-koszul-duality} is the \emph{associative}
chapters/theory/chiral_koszul_pairs.tex:5140:\textup{(}Theorem~\ref{thm:e1-chiral-koszul-duality},
chapters/theory/chiral_koszul_pairs.tex:5206:(Theorem~\ref{thm:e1-chiral-koszul-duality}, equation
chapters/theory/chiral_koszul_pairs.tex:5903:theorem (Theorem~\ref{thm:e1-chiral-koszul-duality}) extends the



thinking
**Verifying references in the repository**

I notice that the search output isn't sourced from a file, which is an issue since the final format doesn’t allow that. I've come across a citation reference that doesn't exist in the repository—specifically, at a certain line in the document. It feels important to highlight this, especially since the user asked about cited lemmas. Verifying this will help ensure the accuracy of references, so I’m considering how to clarify that the proposition is indeed missing.
thinking
**Summarizing findings on proofs and concepts**

I’m organizing my findings into a final list, which includes several varying levels of importance. There's a critical issue with conflating objects and another regarding the validity of a proof. Additionally, I’ve identified some misstatements and nonexistent citations that need addressing. Perhaps combining the missing proposition with cross-volume propagation could be beneficial, as cross-volume drift may hold more value. I’ll ensure the final output is concise, aiming for six findings with brief summaries for clarity.
thinking
**Assessing critical severity**

I’m determining the severity of an issue in a specific document. The core duality proof at a certain line conflates the Koszul dual algebra with the bar-side coalgebra, which leads to invalid deductions. This confusion arises when it identifies one component with another and makes a crucial replacement. I want to categorize this as critical severity because it fundamentally undermines the integrity of the proof. It's important to clearly articulate this to highlight the potential impact of the mistake.
codex
- [CRITICAL] `chapters/theory/chiral_hochschild_koszul.tex:618` — The proof of `thm:main-koszul-hoch` conflates the bar-side coalgebra with the Koszul dual algebra: it identifies `\bar B^{\mathrm{ch}}(\mathcal A)^\vee` with `\mathcal A^!` and then replaces `\Omega^{\mathrm{ch}}(\bar B^{\mathrm{ch}}(\mathcal A))` by `\Omega^{\mathrm{ch}}(\mathcal A^!)`. That makes the key step `\eqref{eq:hh-via-hom}` invalid as written. This is load-bearing, because Theorem H part `(b)` uses `thm:main-koszul-hoch` for the `t^2` coefficient.

- [CRITICAL] `chapters/theory/chiral_hochschild_koszul.tex:740` — The proof of `thm:hochschild-polynomial-growth` treats `\ChirHoch^n(\mathcal A)` as if its Ext-computing complex were just a complex of `\mathcal D_X`-module morphisms on the base curve and then imports the curve-level amplitude bound `[0,2]`. But the manuscript’s own bigraded definition places Hochschild cochains on the varying configuration spaces `\overline C_{p+2}(X)` of dimension `p+2` (`chapters/theory/higher_genus_foundations.tex:2684`). The proof never justifies collapsing those configuration-space terms to ordinary `\mathcal D_X`-Ext on `X`, so concentration in `{0,1,2}` is claimed as proved, not computed, but the written argument does not establish it.

- [HIGH] `chapters/connections/concordance.tex:64` — The concordance records Theorem H as universally having Hilbert polynomial `P(t)=1+t^2`, but the actual theorem states the family-dependent formula `P_\mathcal A(t)=\dim Z(\mathcal A)+\dim \ChirHoch^1(\mathcal A)\,t+\dim Z(\mathcal A^!)\,t^2` (`chapters/theory/chiral_hochschild_koszul.tex:701`). This already conflicts inside Vol I with the Heisenberg computation `1+t+t^2` (`chapters/theory/hochschild_cohomology.tex:390`) and the generic affine formula `1+\dim(\mathfrak g)t+t^2` (`chapters/theory/koszul_pair_structure.tex:705`).

- [HIGH] `chapters/connections/concordance.tex:68` — The theorem-H citation bundle mixes incompatible scopes. It cites `thm:critical-level-cohomology` under Theorem H even though Vol I explicitly says Theorem H does not apply at critical level (`chapters/theory/hochschild_cohomology.tex:167`), and it does not warn that for non-principal `W`-orbits the concentration claim is only conjectural when Koszulness is open (`chapters/theory/hochschild_cohomology.tex:331`). So the answer to “all families?” is no: the proved statement is on the Koszul locus, with separate family-specific treatments and exclusions.

- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:737` — The theorem-H package cites `Prop.~\ref{prop:bar-resolution-chirhoch}` immediately after the theorem statement, but repo-wide search finds no such label. A named dependency used to source the `RHH_{\mathrm{ch}}(A)\simeq \mathrm{RHom}_{\mathsf{ChirAlg}}(A,A)` identification is missing.

- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:497` — The shift lemma says bar concentration leaves only the “diagonal `p=q`,” but the cited bar-concentration theorem gives vanishing for `q\neq0`, not `p\neq q` (`chapters/theory/chiral_koszul_pairs.tex:1073`). The same wrong explanation recurs in `chapters/theory/higher_genus_foundations.tex:2710`. This does not by itself kill the shift-`2` claim, but it shows the proof narrative is tracking the wrong surviving bigrading.

- [LOW] `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1290` — The wrong universal `P(t)=1+t^2` has already propagated into Vol II; related broadened paraphrases also appear in `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2744` and `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:223`. The drift is not local to one Vol I summary.

## Summary
Instances checked: 20 | Violations found: 7 | Verdict: FAIL

Concentration in `{0,1,2}` is presented as proved-here on the Koszul locus, not merely computed, but the written proof has a core gap. The Hilbert series is not universally `1+t^2`; the surviving Vol I formula is the quadratic family-dependent one in `chapters/theory/chiral_hochschild_koszul.tex:701`, with examples `1+t+t^2` (Heisenberg), `1+t^2` (generic Vir/W), `1+\dim(\mathfrak g)t+t^2` (generic affine), and unbounded critical-level affine outside Theorem H. AP134 check: no surviving theorem-H vdim conflation was found on the audited core surfaces; the manuscript explicitly distinguishes cohomological amplitude from virtual dimension in `chapters/theory/higher_genus_modular_koszul.tex:29691`.
tokens used
223,738
