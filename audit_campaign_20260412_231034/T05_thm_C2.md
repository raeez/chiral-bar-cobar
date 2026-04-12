# T05_thm_C2 (740s, gpt-5.4)

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1940](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1940) — Part (i) of `thm:shifted-symplectic-complementarity` proves nondegeneracy by switching from `\mathbb D(\bar B(\cA))` to `\Omega(\cA^!)`. That is not what the cited input says. `thm:bv-functor` identifies the Verdier dual with a factorization algebra whose underlying complex is equivalent to `\bar B(\cA^!)`, not `\Omega(\cA^!)` ([bv_brst.tex:1367](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1367)); `thm:verdier-bar-cobar` gives only a pairing with `\Omega(\cA^!)` ([cobar_construction.tex:1321](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1321)); and the theorem statement itself had used `\bar B(\cA^!)` ([higher_genus_complementarity.tex:1901](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1901)). The proof changes the dual object mid-argument, so nondegeneracy is not established.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1970](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1970) — Part (iii) asserts a Verdier involution on the bar-side dg Lie algebra `L_g = \bar B^{(g)}(\cA)[1]` and then cites `prop:lagrangian-eigenspaces` to conclude `L_g^\pm` are Lagrangian. But that proposition is about `V = H^*(\overline{\mathcal M}_g,\mathcal Z(\cA))` and the center-side eigenspaces `Q_g(\cA), Q_g(\cA^!)`, not about `L_g` ([higher_genus_complementarity.tex:1787](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1787)). I found no local lift from the center-level polarization to the bar-side BV Lie algebra. This is a second object conflation in the live C2 proof.

- [CRITICAL] [chapters/theory/higher_genus_foundations.tex:5326](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5326) — `thm:genus-universality` derives `\mathrm{obs}_g=\kappa(\cA)\lambda_g` by citing `thm:family-index`, but the proof of `thm:family-index` starts from `thm:genus-universality` itself ([concordance.tex:6009](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6009)). On the live theorem graph, the scalar genus theorem is circular.

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex:21722](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21722) — The claimed implication “equal conformal weights `=>` `\delta F_g^{cross}=0`” is not proved by the cited source. `thm:multi-weight-genus-expansion` outsources Part (iv) to `thm:algebraic-family-rigidity`, but that theorem explicitly stops at one-dimensionality of the minimal MC direction and says the identification `\Gamma_{\cA}=\kappa(\cA)\Lambda` is “not settled here” ([higher_genus_modular_koszul.tex:8980](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:8980)). The manuscript’s own later diagnosis says the obstruction at higher genus comes from mixed-channel vertex data while edges stay universal ([higher_genus_foundations.tex:5469](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5469), [higher_genus_modular_koszul.tex:22076](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22076)). So uniform-weight sufficiency is not justified.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:2500](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2500) — `def:scalar-lane` asserts that “all strong generators have the same conformal weight” is equivalent to “a single primary line” and hence a one-variable problem. But the live multi-channel formalism indexes channels by `1,\dots,r` and defines mixed assignments independently of weight equality ([higher_genus_modular_koszul.tex:22066](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22066)). I found no proof of that equivalence. Hidden assumption: equal weights collapse channel labels.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:5257](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5257) — Downstream status propagation is stale. This theorem, and likewise [higher_genus_modular_koszul.tex:2651](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2651), still says higher genus is “conditional on the strong scalar ansatz of `thm:multi-generator-universality`.” But that label now names the proved decomposition theorem with `\delta F_1^{cross}=0` and higher-genus cross-channel corrections ([higher_genus_modular_koszul.tex:21681](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21681)). The correction term is properly scoped there; these downstream surfaces are not.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:433](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:433) — The live manuscript no longer defines C2 as a scalar BV pairing. It defines C2 as the conditional bar-side BV / shifted-symplectic upgrade and explicitly says the scalar complementarity formulas are consequences of C1 plus Theorem D, “not a separate C2 label” ([higher_genus_complementarity.tex:441](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:441)). So the requested “Theorem C2: scalar BV pairing (conditional on uniform-weight)” is already off the current theorem surface.

Part-by-part: Part (i) fails by bar/cobar object switching. Part (ii) has no separate local contradiction I could verify, but it depends on Part (i)’s broken nondegeneracy input. Part (iii) is unsupported by a center-side/bar-side conflation. For the scalar lane, the live manuscript does not justify that uniform-weight alone kills `\delta F_g^{cross}`; what is properly scoped is the later corrected formula `F_g=\kappa\lambda_g^{FP}+\delta F_g^{cross}`, with `g=1` zero and higher-genus mixed-channel corrections possible.

## Summary
Instances checked: 16 | Violations found: 7 | Verdict: FAIL


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
session id: 019d8388-33aa-75e1-bea2-81e1ca8b7fd8
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


MISSION: FALSIFY the proof of Theorem C2: scalar BV pairing (conditional on uniform-weight). Check: (a) what is the condition? (b) does uniform-weight actually suffice? (c) what fails at multi-weight? (d) is the delta_F_g^cross correction properly scoped?

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
Using `deep-beilinson-audit` for this turn because the task is an adversarial proof audit, not a local formula check. I’ll lock the theorem surface first by locating Theorem C2 and reading the constitutional files that govern status, scope, and known drift before I inspect the statement and proof.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg -n \"Theorem C2|thm:C2|scalar BV pairing|uniform-weight|delta_F_g\\"'^cross|delta_F_g|BV pairing" chapters metadata CLAUDE.md /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex /Users/raeez/chiral-bar-cobar/raeeznotes/raeeznotes100/red_team_summary.md /Users/raeez/chiral-bar-cobar/archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 exited 2 in 51ms:
/Users/raeez/chiral-bar-cobar
rg: /Users/raeez/chiral-bar-cobar/raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
CLAUDE.md:65:### HZ-3. AP32 (uniform-weight tag on F_g) -- 4 waves, 30+ instances
CLAUDE.md:414:**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).
CLAUDE.md:488:| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
CLAUDE.md:489:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
CLAUDE.md:507:**pole/weight** (AP19, AP21, AP27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.
CLAUDE.md:543:**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:56: for uniform-weight modular Koszul algebras
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:291: For a Koszul chiral algebra~$\cA$ with uniform-weight
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:405: For uniform-weight algebras, the scalar genus tower
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:640: for uniform-weight algebras
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:907:Part~(iii) is the Heisenberg scalar formula (uniform-weight,
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:3022:\item \emph{Scalar-orbit convolution formality}: for uniform-weight algebras, the distinguished scalar Maurer--Cartan orbit in $\mathfrak{g}_\cA^{\mathrm{mod}}$ is formal; converse and one-channel generalizations remain open.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4000:For uniform-weight algebras, the shadow obstruction tower free energy
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4380:uniform-weight hypothesis at $g \geq 2$.
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:4754:$\mathrm{obs}_g = \kappa \cdot \lambda_g$ is, for uniform-weight
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:5257: $\kappa(\cA)\lambda_1$; on the proved uniform-weight lane,
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:5279:$\kappa\lambda_g$ only on the proved uniform-weight lane
/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:5285:$\kappa(\cA) \cdot \lambda_1$, and on the proved uniform-weight lane
codex
The target is not the rank-two `thm:C2-ordered-bar`; I’m narrowing to the complementarity theorem lane where “scalar BV pairing” appears, then I’ll read the theorem block with its proof and every cited dependency in context.
exec
/bin/zsh -lc "rg -n \"scalar BV pairing|scalar.*BV pairing|BV pairing.*scalar|Theorem C2|C2\\b|uniform-weight.*BV|delta F_g\\"'^'"\\{\\\\mathrm\\{cross\\}\\}|delta F_g\\"'^cross|cross-channel correction|multi-weight-genus-expansion|genus-universality|quantum-complementarity-main|minimal scalar package" chapters/theory chapters/connections chapters/frame' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:mc2-bar-intrinsic|thm:genus-universality|thm:multi-weight-genus-expansion|def:scalar-lane|def:uniform-weight-lane|Verdier/BV pairing|cross Verdier/BV pairing|scalar shadow|minimal scalar" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/introduction.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:scalar BV pairing|scalar.*BV pairing|BV pairing.*scalar|Theorem C2|C2\b|uniform-weight.*BV|delta F_g\^\{\mathrm\{cross\}\}|delta F_g\^cross|cross-channel correction|multi-weight-genus-expansion|genus-universality|quantum-complementarity-main|minimal scalar package)
                                                                                                               ^^
error: unrecognized escape sequence
 succeeded in 50ms:
chapters/theory/introduction.tex:108:(Theorem~\ref{thm:mc2-bar-intrinsic}).
chapters/theory/introduction.tex:374:(Theorem~\ref{thm:mc2-bar-intrinsic}); since
chapters/theory/introduction.tex:570: (Theorem~\ref{thm:mc2-bar-intrinsic}).
chapters/theory/introduction.tex:611: coefficient (Theorem~\ref{thm:genus-universality}), determines the
chapters/theory/introduction.tex:631: (Theorem~\ref{thm:multi-weight-genus-expansion},
chapters/theory/introduction.tex:724:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}.
chapters/theory/introduction.tex:885:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}
chapters/theory/introduction.tex:1793: (Theorem~\ref{thm:genus-universality}). The natural home is
chapters/theory/introduction.tex:1801: proved intrinsically by Theorem~\ref{thm:mc2-bar-intrinsic})
chapters/theory/introduction.tex:1856:is the scalar shadow of the top arrow;
chapters/theory/introduction.tex:1997:(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
chapters/theory/introduction.tex:2073:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & bar-intrinsic (Thm~\ref{thm:mc2-bar-intrinsic}) \\[2pt]
chapters/theory/introduction.tex:2082:\noindent\textbf{MC2} (Universal MC class): $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ exists for every modular Koszul chiral algebra by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of its finite-order projections. When $\dim H^2_{\mathrm{cyc}} = 1$, the MC element collapses to $\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Corollary~\ref{cor:scalar-saturation}).
chapters/theory/introduction.tex:2264:in Theorem~\ref{thm:mc2-bar-intrinsic}. Every chapter either
chapters/theory/higher_genus_complementarity.tex:547:(Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}).
chapters/theory/higher_genus_complementarity.tex:2854:(Theorem~\ref{thm:genus-universality}(ii)).
chapters/theory/higher_genus_complementarity.tex:3478: (Theorem~\ref{thm:mc2-bar-intrinsic};
chapters/theory/higher_genus_complementarity.tex:3484:\item \emph{S-level.} The scalar shadow is
chapters/theory/higher_genus_complementarity.tex:3486: (Theorem~\ref{thm:genus-universality}; ):
chapters/theory/higher_genus_complementarity.tex:3491: (Theorem~\ref{thm:multi-weight-genus-expansion}).

thinking
**Searching for scalar pairing theorem**

I’m looking for more information about the scalar BV pairing theorem. I think I should search specifically for “scalar pairing” in contexts like higher genus modular Koszul sections. Maybe I can simplify my approach and focus on relevant parts to get clearer answers. I want to make sure I find the most effective resources, so I’ll look for research papers or articles that detail this topic further.
codex
I have the global theorem lane. Next I’m isolating the exact theorem block for the scalar BV pairing and the local dependency chain around it, because the failure modes here are likely scope leakage and unsupported upgrade from chain-level pairing to scalar collapse.
exec
/bin/zsh -lc 'rg -n "scalar[''^'"\\n]{0,80}pairing|pairing["'^'"\\n]{0,80}scalar|BV pairing|Verdier/BV pairing|cross Verdier/BV pairing|minimal scalar package|scalar shadow\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5600,6265p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11280,11460p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:1952:axioms are inherited from the BV algebra axioms. The BV pairing on
chapters/theory/higher_genus_complementarity.tex:3484:\item \emph{S-level.} The scalar shadow is
chapters/theory/higher_genus_complementarity.tex:6007:lifting the uniform-weight scalar shadow $\kappa(\cA)\sum_{g \geq 1}\lambda_g$,
chapters/theory/higher_genus_modular_koszul.tex:487:of~$\mathbf{B}_X(\cA)$, whose scalar shadow is
chapters/theory/higher_genus_modular_koszul.tex:4555:(i)~the scalar shadow $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic});
chapters/theory/higher_genus_modular_koszul.tex:5640:\item the cross Verdier/BV pairing induces a quasi-isomorphism
chapters/theory/higher_genus_modular_koszul.tex:5763:\item the seed-level Verdier/BV pairing extends to a chain map
chapters/theory/higher_genus_modular_koszul.tex:5887: the cross Verdier/BV pairing on
chapters/theory/higher_genus_modular_koszul.tex:6046: the cross Verdier/BV pairing on
chapters/theory/higher_genus_modular_koszul.tex:6205:\item the cross Verdier/BV pairing on
chapters/theory/higher_genus_modular_koszul.tex:9409:\emph{determines the minimal scalar package} of~$\Theta_{\cA}$.
chapters/theory/higher_genus_modular_koszul.tex:9684:uniform-weight lane; the non-scalar shadow obstruction tower
chapters/theory/higher_genus_modular_koszul.tex:11389: internal edges via the cyclic Verdier/BV pairing;
chapters/theory/higher_genus_modular_koszul.tex:14432:about the minimal scalar package; the chain-level
chapters/theory/higher_genus_modular_koszul.tex:25475:\S\ref{subsec:recursion} is the scalar shadow of
chapters/theory/higher_genus_modular_koszul.tex:26349:The scalar shadow partition function
chapters/theory/higher_genus_modular_koszul.tex:26927: This is the scalar shadow of the full involution and is the
chapters/theory/higher_genus_modular_koszul.tex:27377:the scalar shadow free energies
chapters/theory/higher_genus_modular_koszul.tex:27391:the scalar shadow partition function is the
chapters/theory/higher_genus_modular_koszul.tex:33232:with $\kappa(\Theta)$ the scalar shadow of
 succeeded in 51ms:
  5600	coefficient complex with
  5601	\[
  5602	H^*(\mathbf{T}_g^\bullet) \;=\; \mathbb{C}\tau_g
  5603	\]
  5604	for a distinguished generator $\tau_g$.
  5605	Suppose there exist perfect subcomplexes
  5606	\[
  5607	\mathbf{D}_g \subset \Defcyc(\cA),
  5608	\qquad
  5609	\mathbf{D}_g^! \subset \Defcyc(\cA^!)
  5610	\]
  5611	and projector-compatible chain embeddings
  5612	\[
  5613	\iota_g^+ \colon
  5614	\mathbf{D}_g \,\widehat{\otimes}\, \mathbf{T}_g^\bullet
  5615	\hookrightarrow C_g^+,
  5616	\qquad
  5617	\iota_g^- \colon
  5618	\mathbf{D}_g^! \,\widehat{\otimes}\, \mathbf{T}_g^\bullet
  5619	\hookrightarrow C_g^-,
 succeeded in 52ms:
 11280	[\delta_t]\otimes\Phi_t
 11281	+
 11282	[\delta_u]\otimes\Phi_u,
 11283	\qquad
 11284	\Theta_\cA^{[1]}\big|_{(1,1)}
 11285	=
 11286	[\delta_{\mathrm{irr}}]\otimes\Delta .
 11287	\end{equation}
 11288	The combination $\Phi_s+\Phi_t+\Phi_u$ is the
 11289	Malikov--Schechtman secondary Borcherds Jacobiator
 11290	homotopy~$F_3$~\cite[\S3.2]{MS24}.
 11291	\item Weight~$2$ contains the planted-forest
 11292	corrections~\eqref{eq:dpf-logfm}:
 11293	\begin{equation}
 11294	\label{eq:weight-two-log-term}
 11295	\Theta_\cA^{[2]}
 11296	\supset
 11297	\sum_{\rho\in \mathsf{PF}^{\mathrm{rig}}_{g,n}}
 11298	\epsilon_\rho\,
 11299	(\kappa_\rho)_*\,\operatorname{pr}_\rho^{\,*}\otimes\mu_\rho .

thinking
**Searching for theorems**

I’m realizing that the search results aren't sufficient. I need to look more specifically for "C2," possibly related to enumerating subtheorems. There might be a theorem called "thm:mc2-full-resolution" in an editorial constitution. My main focus is on the proof of Theorem C2 regarding scalar BV pairing, assuming uniform weight. I should search for references to "C2:" or "scalar BV pairing" and delve deeper into the relevant files and metadata.
exec
/bin/zsh -lc 'rg -n "scalar BV pairing|scalar BV|Verdier/BV pairing|BV pairing" metadata/claims.jsonl metadata/theorem_registry.md metadata/label_index.json' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "C2[''^A-Za-z]|Theorem~C2|Theorem C2|scalar BV|BV pair|uniform-weight[''^'"\\n]{0,40}conditional|conditional on uniform-weight|minimal scalar package|cross-channel correction\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex chapters/frame/guide_to_main_results.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:596: a cross-channel correction $\delta F_g^{\mathrm{cross}}$
chapters/theory/higher_genus_foundations.tex:4950:cross-channel correction
chapters/theory/higher_genus_foundations.tex:4979:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:4982:class that deviates from~$\lambda_g$ by a cross-channel correction
chapters/theory/higher_genus_foundations.tex:5215: at $g \geq 2$, a cross-channel correction
chapters/theory/higher_genus_foundations.tex:5217: \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)} is present
chapters/theory/higher_genus_foundations.tex:5236:\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
chapters/theory/higher_genus_foundations.tex:5475:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:5478:nonvanishing cross-channel correction
chapters/theory/higher_genus_foundations.tex:5480:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:5495:\index{cross-channel correction!resolution of universality|textbf}%
chapters/theory/higher_genus_foundations.tex:5500:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:5502:\emph{cross-channel correction} at $g \geq 2$.
chapters/theory/higher_genus_foundations.tex:5504:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:5578:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:5602:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:5648:a cross-channel correction
chapters/theory/higher_genus_foundations.tex:5672:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
chapters/theory/higher_genus_foundations.tex:5675:a cross-channel correction $\delta F_g^{\mathrm{cross}} \neq 0$
chapters/theory/higher_genus_foundations.tex:5697:\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}

thinking
**Investigating theorem structure**

I'm noticing interesting results in the higher genus complementarity section, particularly around C2. It seems essential to understand the beginning and the overall theorem structure. I should focus on lines 1 through 220 and maybe hone in on the theorem around line 150, as well as checking around line 1952. Let’s take some time to carefully inspect these lines to grasp what’s being conveyed!
codex
The complementarity chapter explicitly names `(C2)` near the opening, so I’m reading that theorem lane first to pin down what “scalar BV pairing” actually claims before I test whether the later modular-characteristic theorems can support it.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1880,2025p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3440,3515p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\section{The complementarity theorem}
     2	\label{sec:complementarity-theorem}
     3	
     4	Classical Koszul duality over a point is a discrete correspondence:
     5	$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
     6	Already at genus~$0$ on a curve, the Fulton--MacPherson
     7	compactifications $\overline{C}_n(X)$ and the Arnold forms
     8	$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
     9	that has no counterpart over a point: the collision residues that
    10	define the bar differential, the averaging map
    11	$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
    12	characteristic from the spectral $r$-matrix, and the higher
    13	operations $m_n$ for $n \geq 3$ that determine whether the shadow
    14	tower terminates. At genus~$g \geq 1$, the fiberwise curvature
    15	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
    16	algebras to interact through the moduli
    17	$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
    18	decomposes into two complementary halves via Verdier duality:
    19	\begin{equation}\label{eq:complementarity-chapter-opening}
    20	 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
 succeeded in 52ms:
  3440	\index{twisting morphism!curved|textbf}
  3441	\index{Maurer--Cartan equation!curved}
  3442	At genus~$0$, the universal twisting morphism
  3443	$\tau\colon \bar{B}(\cA) \to \cA$ satisfies the flat
  3444	Maurer--Cartan equation $d\tau + \tau \star \tau = 0$
  3445	(Corollary~\ref{cor:three-bijections},
  3446	Remark~\ref{rem:MC-is-Stokes}).
  3447	At genus~$g \geq 1$, the propagator acquires monodromy and the
  3448	twisting morphism becomes \emph{curved}:
  3449	\begin{equation}\label{eq:curved-MC-higher-genus}
  3450	d\tau_g + \tau_g \star \tau_g = \kappa(\cA) \cdot \omega_g.
  3451	\end{equation}
  3452	The curvature $\kappa(\cA) \cdot \omega_g$ is the Arakelov
  3453	$(1,1)$-form weighted by the modular characteristic
  3454	(Theorem~\ref{thm:quantum-arnold-relations}): it measures
  3455	the failure of the single-valued propagator to satisfy the
  3456	Arnold relation at genus~$g$.
  3457	
  3458	The three propagators in the table of Step~4 above correspond
  3459	to three twisting morphisms: $\tau_0$ (classical, flat MC),
 succeeded in 52ms:
  1880	\index{shifted symplectic!(-1)-shifted|textbf}
  1881	\index{Lagrangian!complementarity!shifted symplectic|textbf}
  1882	\textup{[Regime: curved-central on the Koszul locus; all genera
  1883	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1884	
  1885	Assume the conditional BV package of
  1886	Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
  1887	genus-$1$ complementarity
  1888	$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
  1889	\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
  1890	computed in~\S\ref{sec:frame-complementarity} admits the following
  1891	bar-side $(-1)$-shifted symplectic refinement.
  1892	\index{BV algebra!shifted symplectic structure}
  1893	Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
  1894	curve $X$.
  1895	\begin{enumerate}[label=\textup{(\roman*)}]
  1896	\item \emph{BV antibracket is $(-1)$-shifted Poisson.}
  1897	 The BV bracket $\{-,-\}_{\mathrm{BV}}$ on
  1898	 $\barB^{\mathrm{ch}}(\cA)$
  1899	 \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
🌐 Searching the web...
🌐 Searched the web

thinking
**Locating a theorem**

I think I mistakenly used the web when I should stick to local tools due to network restrictions. I mean, the web is available, but maybe I shouldn't be using it. I need to locate the exact theorem, possibly in the guide to main results. It might help to search for "scalar BV pairing" in the generated metadata. Maybe I'll try using "rg -i 'scalar.*pair'" to find it.
exec
/bin/zsh -lc 'rg -n "thm:.*scalar|prop:.*scalar|lem:.*scalar|classification of scalar|scalar lane|proved uniform-weight scalar lane|minimal scalar package" metadata/claims.jsonl chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -ni "scalar.{0,60}pair|pair.{0,60}scalar|scalar BV|BV scalar|uniform-weight.{0,60}pair|pairing.{0,60}uniform-weight" chapters metadata' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/dependency_graph.dot:4960:  prop_winfty_stage4_residue_pairing_reduction -> cor_winfty_stage4_single_scalar_equivalent;
chapters/examples/kac_moody.tex:3857:The quantum correction $Q_1(\cA)$ is the obstruction to strict nilpotence of $d^{(1)}$, living in $H^*(\overline{\mathcal{M}}_{1,1}, Z(\cA))$. For $\widehat{\mathfrak{sl}}_{2,k}$ at generic level, the center is $Z(\widehat{\mathfrak{sl}}_{2,k}) = \mathbb{C} \cdot \mathbf{1} \oplus \mathbb{C} \cdot k$ (the vacuum and the level). The curvature $(k+2) \cdot \omega_1$ is a non-zero element of $H^0(\overline{\mathcal{M}}_{1,1}) \otimes Z(\widehat{\mathfrak{sl}}_{2,k})$ (the factor $(k+2)$ is a scalar since $k$ is fixed, and $\omega_1$ pairs with $H^0$ via the intersection form).
chapters/connections/editorial_constitution.tex:996:weight-$4$ self-pairing normalization as the exact remaining scalar
chapters/connections/editorial_constitution.tex:1514:explicit pair of residues at $0$ and~$1$, equivalently the two scalar
chapters/examples/free_fields.tex:3384:The pairwise terms yield $1$-point elements (scalar times a single
chapters/connections/thqg_gravitational_s_duality.tex:2030:\item For uniform-weight Koszul pairs, for every $g \geq 1$:
chapters/theory/bar_construction.tex:1000:\emph{Property~(2).} Since $d_{\mathrm{curvature}}$ replaces a pair $(\phi_i, \phi_j)$ by a scalar multiple of the vacuum $|0\rangle$, the output of $d_{\mathrm{curvature}}$ at position $i$ is proportional to $|0\rangle$. A subsequent application of $d_{\mathrm{curvature}}$ (or $d_{\mathrm{bracket}}$) involving this vacuum position produces $|0\rangle_{(n)}\phi_k = 0$ for $n \geq 0$, hence $d_{\mathrm{curvature}}^2 = 0$.
chapters/theory/e1_modular_koszul.tex:1710: \textup{(}the Koszul pairing absorbs a scalar factor\textup{)}.
chapters/frame/heisenberg_frame.tex:417:collapses the pair to the scalar~$k$. The form
metadata/claims.jsonl:2048:{"label": "prop:winfty-stage4-residue-pairing-reduction", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_curved.tex", "line": 3644, "title": "Stage-\\texorpdfstring{$4$}{4} swap-even residue channel from a visible\ninvariant pairing", "refs_in_block": ["cor:winfty-stage4-single-scalar-equivalent"]}
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:377:collapses the pair to the scalar~$k$.  The form
chapters/theory/bar_cobar_adjunction_inversion.tex:4262:pairs. Scalar saturation is the vanishing of the primitive summand.
chapters/connections/thqg_modular_bootstrap.tex:1261:$\lambda_p = c_p(\mathbb{E})$, paired with the scalar modular
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:4108:The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
chapters/theory/higher_genus_foundations.tex:193:function of these classes on the uniform-weight scalar lane is $\kappa(\cA) \cdot (\hat{A}(i\hbar) - 1)$
chapters/theory/higher_genus_foundations.tex:251: On the uniform-weight scalar lane, the cohomological curvature
chapters/theory/higher_genus_foundations.tex:1083:(Theorem~\ref{thm:family-index}). The scalar $\kappa(\cA)$ is the
chapters/theory/higher_genus_foundations.tex:5302:On the scalar lane (Definition~\ref{def:scalar-lane}), the genus-$g$ free energy is $F_g = \kappa \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$,
chapters/theory/higher_genus_foundations.tex:5813:In particular, on the proved scalar lane,
chapters/theory/higher_genus_foundations.tex:5857:On the proved scalar lane, these equivalent conditions further imply
chapters/theory/higher_genus_foundations.tex:5878:on the proved scalar lane. The final assertion follows: with
chapters/theory/higher_genus_foundations.tex:5883:\begin{corollary}[Tautological class map on the scalar lane; universal genus-$1$ class; \ClaimStatusProvedHere]\label{cor:tautological-class-map}
chapters/theory/higher_genus_foundations.tex:5892:On the proved scalar lane, one also has
chapters/theory/higher_genus_foundations.tex:5916:is Theorem~\ref{thm:genus-universality}; on the proved scalar lane,
chapters/theory/higher_genus_foundations.tex:5939:on the proved scalar lane a one-parameter family of classes
chapters/theory/higher_genus_foundations.tex:5976:(Theorem~\ref{thm:genus-universality}). On the proved scalar lane,
chapters/theory/higher_genus_foundations.tex:5993:$R^*(\overline{\mathcal{M}}_g)$. On the proved scalar lane, collapse
chapters/theory/higher_genus_foundations.tex:6186:On the proved scalar lane, the factorization
chapters/theory/higher_genus_foundations.tex:6203:A modular Koszul chiral algebra $\cA$ on the proved scalar lane lifts
chapters/theory/higher_genus_foundations.tex:6212: genera on the proved scalar lane.
chapters/theory/higher_genus_foundations.tex:6221:On the proved scalar lane, Theorem~\ref{thm:genus-universality} gives
chapters/theory/higher_genus_foundations.tex:6225:$\mathrm{obs}_g = 0$ for all $g$ on that scalar lane. For arbitrary
chapters/theory/higher_genus_foundations.tex:6239:universal genus-$1$ scalar term and, on the proved scalar lane, all

thinking
**Searching for clarity**

I see that the search isn't quite exact. The user's question might involve a theorem related to some document summarizing C2, possibly in the context of gravitational duality. I think I need to focus on finding where the phrase "scalar BV pairing" is located since it may not be precisely stated. I'll zero in on line 2030 in the thqg_gravitational_s_duality document to check for any relevant information.
codex
There are two different “C2” surfaces in play: the complementarity chapter’s shifted-symplectic upgrade, and a scalar-lane shadow package elsewhere. The user’s mention of “scalar BV pairing” plus “uniform-weight” points to a scalar-lane theorem downstream of MC2, so I’m checking the S-duality/connections summaries to see which theorem label they are using for C2.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_s_duality.tex | sed -n '2000,2065p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '220,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "scalar BV|BV pairing|uniform-weight Koszul pairs|For uniform-weight Koszul pairs|C2" chapters/connections/thqg_gravitational_s_duality.tex chapters/connections/genus_complete.tex chapters/frame/guide_to_main_results.tex chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   220	\item \textbf{Deformation-control object} (Pillar~B). The universal
   221	 deformation machine is a \emph{filtered convolution $sL_\infty$-algebra}
   222	 $\operatorname{hom}_\alpha(\cC, \cA)$ relative to a twisting morphism
   223	 $\alpha$, in the sense of Robert-Nicoud--Wierstra~\cite{RNW19} and
   224	 Vallette~\cite{Val16}. The dg~Lie algebra $\gAmod$ of
   225	 Definition~\ref{def:modular-convolution-dg-lie} is the strict model.
   226	 \emph{Design constraint}:
   227	 $\operatorname{hom}_\alpha$ extends to $\infty$-morphisms in either
   228	 slot separately but not both simultaneously~\cite[Section~6]{RNW19}.
   229	
   230	\item \textbf{Global collision geometry} (Pillar~C). The natural
   231	 compactification for punctured curves and nodal degenerations
   232	 is \emph{logarithmic Fulton--MacPherson}
   233	 $\overline{\operatorname{FM}}_n(X|D)$ on simple normal crossings pairs
   234	 $(X, D)$, in the sense of Mok~\cite{Mok25}. Ordinary FM
   235	 compactification is the special case $D = \emptyset$.
   236	\end{enumerate}
   237	
   238	\subsection*{Family index theorem}
   239	
 succeeded in 51ms:
  2000	$H^*(\barB^{(g)}(\cA)) \oplus H^*(\barB^{(g)}(\cA^!))
  2001	\hookrightarrow H^*(\overline{\cM}_g, \cZ(\cA))$.
  2002	The Lagrangian decomposition follows from
  2003	Lemma~\ref{lem:involution-splitting}(c): the Verdier involution on
  2004	the ambient complex $\mathbf{C}_g(\cA)$ has eigenvalues $\pm 1$,
  2005	producing the splitting into $\mathbf{Q}_g(\cA)$ (eigenvalue $+1$)
  2006	and $\mathbf{Q}_g(\cA^!)$ (eigenvalue $-1$).
  2007	\end{proof}
  2008	
  2009	\begin{remark}[The single functor]
  2010	\label{rem:thqg-IV-single-functor}
  2011	The four facets are evaluations of~$\sigma$ at different
  2012	points of the modular graph expansion. Its restriction to genus~$0$
  2013	is classical Verdier duality; to genus~$1$, degree~$2$ is
  2014	Feigin--Frenkel; its all-genera shadow is shifted-symplectic
  2015	complementarity. The statements are projections of one identity.
  2016	\end{remark}
  2017	
  2018	\subsubsection{Free energy and the functional equation}
  2019	
 succeeded in 50ms:
chapters/frame/guide_to_main_results.tex:81:\textbf{MC2 ($\Theta_\cA$)} &
chapters/theory/introduction.tex:2073:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & bar-intrinsic (Thm~\ref{thm:mc2-bar-intrinsic}) \\[2pt]
chapters/theory/introduction.tex:2082:\noindent\textbf{MC2} (Universal MC class): $\Theta_\cA \in \MC(\Defcyc(\cA) \widehat{\otimes} \Gmod)$ exists for every modular Koszul chiral algebra by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$ is MC because $D_\cA^2 = 0$. The shadow obstruction tower $\Theta_\cA^{\leq r}$ consists of its finite-order projections. When $\dim H^2_{\mathrm{cyc}} = 1$, the MC element collapses to $\Theta_\cA = \kappa(\cA) \cdot \eta \otimes \Lambda$ (Corollary~\ref{cor:scalar-saturation}).
chapters/connections/thqg_gravitational_s_duality.tex:2030:\item For uniform-weight Koszul pairs, for every $g \geq 1$:
chapters/connections/genus_complete.tex:610:(Part of the MC2 theorem package; Theorem~\ref{thm:mc2-full-resolution}.)
codex
I still have not seen the exact phrase “scalar BV pairing” in source, which suggests the user is naming a theorem informally. I’m now reading the scalar-lane theorem blocks that actually use the chain-level Verdier/BV pairing to derive scalar data, because that is the only place the “uniform-weight” condition enters the BV story.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13760,14080p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14120,14520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2488,2675p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 13760	$\overline{\mathcal{M}}_{0,n}$ is the shadow connection
 13761	$\nabla^{\mathrm{sh}} = d - \operatorname{Sh}_{0,n}(\Theta_\cA)$.
 13762	For $\cA = \widehat{\mathfrak{g}}_k$, on the affine Kac--Moody
 13763	comparison surface this identifies with the KZ connection by
 13764	Theorem~\ref{thm:shadow-connection-kz}.
 13765	
 13766	(iv)~The monodromy of $\nabla_\cA$ around a boundary divisor
 13767	$\delta_i$ is computed by restricting $D_\Theta$
 13768	to a formal neighborhood of $\delta_i$. The restriction of
 13769	$\Theta_\cA$ to $\delta_i$ factorizes via the clutching
 13770	law (Construction~\ref{const:vol1-clutching-law-logfm}):
 13771	the leading contribution is the separating bracket
 13772	$[K_{g_1}, K_{g_2}]$ for $\delta_i^{\mathrm{sep}}$, the
 13773	non-separating loop $\Delta_{\mathrm{ns}}(K_{g-1})$ for
 13774	$\delta_i^{\mathrm{nsep}}$, and the rigid cutting terms
 13775	$R_\rho$ for the planted-forest strata. These are exactly
 13776	the genus-$g$ shell equation terms.
 13777	\end{proof}
 13778	
 13779	\begin{theorem}[Scalar free-energy and determinant reconstruction from the
 succeeded in 51ms:
  2488	by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
  2489	is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
  2490	(Theorems~\ref{thm:universal-MC}
  2491	and~\ref{thm:universal-theta}).
  2492	\end{definition}
  2493	
  2494	\begin{definition}[Uniform-weight lane (scalar lane)]
  2495	\label{def:scalar-lane}
  2496	\label{def:uniform-weight-lane}
  2497	\index{scalar lane|textbf}
  2498	\index{uniform-weight lane|see{scalar lane}}
  2499	A modular Koszul chiral algebra~$\cA$ lies on the
  2500	\emph{uniform-weight lane} (or \emph{scalar lane}) if every
  2501	strong generator of~$\cA$ has the same conformal weight.
  2502	Equivalently, $\cA$ has a single primary line in
  2503	$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
  2504	reduces to a one-variable problem.
  2505	Single-generator algebras (Heisenberg, free fermion, Virasoro)
  2506	lie on the scalar lane automatically; multi-generator algebras
  2507	($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.
 succeeded in 52ms:
 14120	the degree filtration $F_{\mathrm{ar}}^{\leq n}$ on $\Barch(\cA)$
 14121	is a strong filtration, and the bar-cobar
 14122	quasi-isomorphism at each finite degree level
 14123	$\operatorname{Ran}^{\leq n}$ (Theorem~\ref{thm:bar-cobar-inversion-qi})
 14124	gives a compatible inverse system. The degree cutoff lemma shows
 14125	that the quasi-isomorphism at level~$n$ depends only on the bar
 14126	complex data at degrees $\leq n$, so the inverse system satisfies
 14127	the Mittag--Leffler condition.
 14128	
 14129	(iii)~The $E_2$-collapse of the bar spectral sequence at
 14130	$\operatorname{Ran}^{\leq n}$ is a property of the degree-$\leq n$
 14131	components of the bar differential. Since the $E_2$-page on
 14132	$\operatorname{Ran}$ is the product of the $E_2$-pages at each
 14133	degree, collapse at each degree implies collapse of the product.
 14134	\end{proof}
 14135	
 14136	\begin{theorem}[Shadow channel decomposition; \ClaimStatusProvedHere]
 14137	\label{thm:shadow-channel-decomposition}
 14138	\index{shadow obstruction tower!channel decomposition|textbf}
 14139	\index{shadow algebra!multi-channel decomposition}

thinking
**Inspecting theorem proof**

I need to check the theorem proof, focusing on the names of theorems referenced. I should continue from line 2675 onward to see if the proof incorporates a multi-generator ansatz or other techniques. It's important for me to pay careful attention to these details to ensure I understand the proof fully. Alright, let’s dig into the proof and see what I can uncover!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2675,2768p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:multi-generator-universality|multi-generator universality|strong scalar ansatz|uniform-weight" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
  2685	\item \emph{Additivity.}
  2686	 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
  2687	 Combined with~(iii), the vanishing
  2688	 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
  2689	 $\cA \otimes \cA^!_{\mathrm{ghost}}$ is the algebraic
  2690	 form of anomaly cancellation.
  2691	\end{enumerate}
  2692	\end{theorem}
  2693	
  2694	\begin{proof}
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:188:uniform-weight algebras, where $\lambda_g = c_g(\mathbb{E})$ is
chapters/theory/higher_genus_foundations.tex:193:function of these classes on the uniform-weight scalar lane is $\kappa(\cA) \cdot (\hat{A}(i\hbar) - 1)$
chapters/theory/higher_genus_foundations.tex:251: On the uniform-weight scalar lane, the cohomological curvature
chapters/theory/higher_genus_foundations.tex:583: For uniform-weight algebras and at
chapters/theory/higher_genus_foundations.tex:598: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
chapters/theory/higher_genus_foundations.tex:599: The generating function on the uniform-weight lane is \begin{equation}\label{eq:family-index-package}
chapters/theory/higher_genus_foundations.tex:5124:For uniform-weight algebras, the same nilpotence holds at all genera;
chapters/theory/higher_genus_foundations.tex:5126:Theorem~\ref{thm:multi-generator-universality}.
chapters/theory/higher_genus_foundations.tex:5259:extension is conditional on the strong scalar ansatz of
chapters/theory/higher_genus_foundations.tex:5260:Theorem~\ref{thm:multi-generator-universality}.
chapters/theory/higher_genus_foundations.tex:5323:On the uniform-weight lane, every edge of the genus-$g$ graph sum
chapters/theory/higher_genus_foundations.tex:5415: uniform-weight algebras at all genera, and
chapters/theory/higher_genus_foundations.tex:6269:\begin{proposition}[Grothendieck--Riemann--Roch bridge on the proved uniform-weight scalar lane; \ClaimStatusProvedHere]
chapters/theory/higher_genus_foundations.tex:6273:On the proved uniform-weight scalar lane for a modular Koszul chiral algebra
chapters/theory/higher_genus_foundations.tex:6316:genus universality on that proved uniform-weight lane. Constructing
chapters/connections/concordance.tex:56: for uniform-weight modular Koszul algebras
chapters/connections/concordance.tex:291: For a Koszul chiral algebra~$\cA$ with uniform-weight
chapters/connections/concordance.tex:405: For uniform-weight algebras, the scalar genus tower
chapters/connections/concordance.tex:640: for uniform-weight algebras
chapters/connections/concordance.tex:907:Part~(iii) is the Heisenberg scalar formula (uniform-weight,

thinking
**Investigating pairing concepts**

I'm thinking about the concept of pairing, and maybe there's a theorem related to chain-level pairing that deals with internal edges. I wonder if there's something in `chapters/theory/higher_genus_foundations.tex` about genus universality, possibly involving graph weights and BV pairing. It sounds like I need to search for "pairing" in the context of theorem proofs. Time to inspect the theorem and the associated proof to get a clearer understanding!
codex
The user’s subquestions force me onto the scalar-theorem chain itself: `uniform-weight` and `δF_g^{cross}` are defined and proved in the genus-expansion theorems, not in the abstract complementarity statement. I’m reading those proofs in full now and then tracing whichever “BV pairing” step they actually use.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5240,5608p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"cor:scalar-saturation|scalar saturation|one-channel|minimal Maurer|eta \\otimes \\\\Lambda|theta-direct-derivation|primitive-to-global-reconstruction|primitive-flat-descent\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21680,22040p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:cor:scalar-saturation|scalar saturation|one-channel|minimal Maurer|eta \otimes \Lambda|theta-direct-derivation|primitive-to-global-reconstruction|primitive-flat-descent)
                                                                              ^^
error: unrecognized escape sequence
 succeeded in 52ms:
  5240	
  5241	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5242	\index{genus universality theorem|textbf}
  5243	\textup{[Regime: curved-central on the Koszul locus; all genera
  5244	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5245	
  5246	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5247	all have the \emph{same} conformal weight. There exists a
  5248	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5249	curvature, such that \begin{equation}\label{eq:genus-universality}
  5250	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5251	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5252	\quad \text{for all } g \geq 1,
  5253	\end{equation}
  5254	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  5255	\textup{(LOCAL)}
  5256	Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
  5257	For algebras with generators of \emph{several} conformal weights,
  5258	the genus-$1$ specialization is unconditional; the higher-genus
  5259	extension is conditional on the strong scalar ansatz of
 succeeded in 51ms:
 21680	
 21681	\begin{theorem}[Multi-weight genus expansion; \ClaimStatusProvedHere]
 21682	\label{thm:multi-weight-genus-expansion}
 21683	\label{thm:multi-generator-universality}
 21684	\index{multi-generator obstruction!genus expansion|textbf}%
 21685	\index{multi-weight genus expansion|textbf}%
 21686	\index{cross-channel correction|textbf}%
 21687	\index{Faber--Pandharipande formula!multi-weight decomposition}%
 21688	\index{genus expansion!multi-channel graph sum}%
 21689	Let\/ $\cA$ be a modular Koszul chiral algebra with
 21690	strong generators $\varphi_1, \ldots, \varphi_r$ of conformal
 21691	weights $h_1, \ldots, h_r$, per-channel modular characteristics
 21692	$\kappa_1, \ldots, \kappa_r$
 21693	\textup{(}Theorem~\textup{\ref{thm:shadow-channel-decomposition})},
 21694	and total modular characteristic\/
 21695	$\kappa(\cA) = \sum_{i=1}^r \kappa_i$.
 21696	\begin{enumerate}[label=\textup{(\roman*)}]
 21697	\item \emph{Per-channel universality.}
 21698	 The diagonal contribution to the genus-$g$ free energy satisfies
 21699	 \begin{equation}\label{eq:multi-weight-diagonal}
codex
I’ve now read the two theorems that actually govern the user’s subquestions: `thm:genus-universality` and `thm:multi-weight-genus-expansion`. The next step is to trace the hidden dependency chain the scalar-lane proofs rely on, especially `cor:scalar-saturation`, `thm:family-index`, and any theorem they cite under the outdated “strong scalar ansatz” wording.
exec
/bin/zsh -lc "rg -n \"cor:scalar-saturation|scalar saturation|eta\\\\otimes\\\\Lambda|theta-direct-derivation|family-index|mupford-formula|mymford-formula|thm:mumford-formula|prop:multi-generator-obstruction|rem:propagator-weight-universality|thm:algebraic-family-rigidity|primitive-to-global-reconstruction|primitive-flat-descent\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6160,6325p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '7800,7895p'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:cor:scalar-saturation|scalar saturation|eta\otimes\Lambda|theta-direct-derivation|family-index|mupford-formula|mymford-formula|thm:mumford-formula|prop:multi-generator-obstruction|rem:propagator-weight-universality|thm:algebraic-family-rigidity|primitive-to-global-reconstruction|primitive-flat-descent)
                                                  ^^
error: unrecognized escape sequence
 succeeded in 50ms:
  6160	For the Heisenberg algebra $\mathcal{H}_\kappa$:
  6161	\begin{align}
  6162	\text{obs}_g &= \kappa \cdot \lambda_g \in H^{2g}(\overline{\mathcal{M}}_g)
  6163	\qquad \\
  6164	\text{def}_g &\in H^{4g-6}(\overline{\mathcal{M}}_g)
  6165	\end{align}
  6166	
  6167	The degrees are complementary under Poincar\'e duality: $\dim_{\mathbb{R}}(\overline{\mathcal{M}}_g) = 6g - 6$, so $H^{2g}$ pairs with $H^{6g-6-2g} = H^{4g-6}$.
  6168	
  6169	\emph{Note:} The deformation degree is $4g - 6$.
  6170	At $g = 1$, $4g - 6 = -2 < 0$, so $\text{def}_1 = 0$:
  6171	the genus-$1$ obstruction is uncompensated.
  6172	At $g = 2$, $\text{def}_2 \in H^2(\overline{\mathcal{M}}_2)$
  6173	(a $3$-dimensional space).
  6174	At $g = 3$, $\text{def}_3 \in H^6(\overline{\mathcal{M}}_3) = H^{\mathrm{top}} \cong \mathbb{C}$, so the deformation is a scalar.
  6175	For $g \geq 2$, the Poincar\'e duality pairing couples
  6176	$\text{obs}_g$ with $\text{def}_g$:
  6177	\begin{align}
  6178	\langle \text{obs}_g, \text{def}_g \rangle &= \int_{\mathcal{M}_g} (\kappa \cdot \lambda_g)
  6179	\qquad \cup (\kappa^{-1} \cdot \lambda_{g-3}^*) \\
 succeeded in 52ms:
  7800	\end{proof}
  7801	
  7802	\begin{remark}[Relation to the universal class]
  7803	\label{rem:kappa-theta-relation}
  7804	The scalar $\kappa(\cA)$ is the first characteristic number of
  7805	$\Theta_{\cA}$ (Theorems~\ref{thm:universal-theta}
  7806	and~\ref{thm:mc2-bar-intrinsic}); the
  7807	spectral discriminant $\Delta_{\cA}$
  7808	(Theorem~\ref{thm:spectral-characteristic}) is a separately proved
  7809	non-scalar invariant.
  7810	\end{remark}
  7811	
  7812	\begin{corollary}[One-channel line concentration of the minimal MC
  7813	class;
  7814	\ClaimStatusProvedHere]
  7815	\label{cor:scalar-saturation}
  7816	\index{universal Maurer--Cartan class!scalar saturation}
  7817	\index{universal Maurer--Cartan class!scalar exactness}
  7818	For any Koszul chiral algebra~$\cA$ with simple Lie
  7819	symmetry~$\mathfrak{g}$ satisfying

thinking
**Identifying theorems**

I need to clarify which theorem the user is referring to. Maybe Theorem C2 relates to `thm:theta-direct-derivation`, but they're specifically asking about "scalar BV pairing." I also have a thought about `thm:obs-def-pairing-explicit`, which seems to involve obstruction-deformation pairing. It feels like I should search for more information to ensure I'm on the right track. Let’s dig deeper into these theorems to find the right connection!
codex
The scalar-lane proofs are already showing a serious ambiguity: some places say the higher-genus multi-weight case is “conditional on the strong scalar ansatz,” while later the manuscript claims it is resolved negatively by an explicit correction theorem. I’m now checking whether the target theorem still depends on that stale conditional wording or has been updated consistently.
exec
/bin/zsh -lc "rg -n \"uniform-weight scalar lane|scalar lane|one-channel cyclic deformation complex|minimal scalar package|Gamma_\\\\cA = \\\\kappa|Theta_\\\\cA\\"'^'"\\{\\\\min\\}|cross-channel correction\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5608,6208p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "strong scalar ansatz|resolved negatively|multi-generator universality|multi-weight genus expansion|conditional on the strong scalar ansatz|obs-def-pairing-explicit|pairing explicit|obstruction.*pairing|def.*pairing" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:uniform-weight scalar lane|scalar lane|one-channel cyclic deformation complex|minimal scalar package|Gamma_\cA = \kappa|Theta_\cA\^\{\min\}|cross-channel correction)
                                                                                                                  ^^
error: unrecognized escape sequence
 succeeded in 51ms:
  5608	
  5609	\begin{remark}[Propagator weight universality]%
  5610	\label{rem:propagator-weight-universality}%
  5611	\index{propagator weight universality|textbf}%
  5612	\index{bar complex!propagator weight}%
  5613	\index{prime form!weight of d log}%
  5614	The bar complex propagator is $d\log E(z,w)$, where $E(z,w)$
  5615	is the prime form on a Riemann surface. The prime form is a
  5616	section of $K^{-1/2} \boxtimes K^{-1/2}$
  5617	(cf.\ the critical pitfall in~\S\ref{sec:conventions}),
  5618	so $d\log E = dE/E$ has weight~$1$ in both variables,
  5619	\emph{regardless} of the conformal weight of the fields being sewed.
  5620	
  5621	This observation has two consequences:
  5622	\begin{enumerate}[label=\textup{(\roman*)}]
  5623	\item \emph{Genus-$1$ universality:}
  5624	At $g = 1$, $H^2(\overline{\cM}_{1,1}) \cong \mathbb{C}$ forces
  5625	every class to be proportional to~$\lambda_1$, so
  5626	$\mathrm{obs}_1(\cA) = \kappa \cdot \lambda_1$
  5627	\textup{(g=1 only; all-weight at g=1 is unconditional)} unconditionally.
 succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:1135:By Koszul duality (Definition~\ref{def:koszul-dual-chiral}), there is a natural pairing:
chapters/theory/higher_genus_complementarity.tex:4108:The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
chapters/theory/higher_genus_foundations.tex:4796:At genus~$g \geq 2$: $\lambda_g = c_g(\mathbb{E})$ has degree~$g < 3g{-}3 = \dim_{\mathbb{C}}\overline{\mathcal{M}}_g$, so the obstruction class $\mathrm{obs}_g = \kappa \cdot \lambda_g$ is a non-trivial class in $H^{2g}(\overline{\mathcal{M}}_g)$ but is \emph{not} a top-degree class. Its numerical evaluation requires pairing with a complementary tautological class of degree~$2g{-}3$; the relevant intersection numbers are computable from the Faber conjectures (proved by Faber--Pandharipande) involving Bernoulli numbers.
chapters/theory/higher_genus_foundations.tex:5259:extension is conditional on the strong scalar ansatz of
chapters/theory/higher_genus_foundations.tex:5677:resolved negatively;
chapters/theory/higher_genus_foundations.tex:5752:This has been resolved negatively:
chapters/theory/higher_genus_foundations.tex:6103:\begin{theorem}[Obstruction-deformation pairing; \ClaimStatusProvedHere]\label{thm:obs-def-pairing-explicit}
chapters/theory/higher_genus_foundations.tex:6196:\textup{(}Theorem~\ref{thm:obs-def-pairing-explicit}\textup{)} to have
chapters/connections/concordance.tex:6928: (\textbf{op:multi-generator-universality}, resolved negatively;
chapters/connections/concordance.tex:7628: Layer~2 (tautological purity) resolved negatively for multi-weight at $g \geq 2$.
chapters/connections/concordance.tex:9701: resolved negatively\textup{)} \\
chapters/connections/concordance.tex:10027: \textbf{resolved negatively}).
chapters/connections/concordance.tex:10999: \textbf{resolved negatively}\textup{)}.
chapters/connections/concordance.tex:11150: multi-generator universality at $g \geq 2$
chapters/connections/concordance.tex:11152: resolved negatively: cross-channel correction nonzero),
chapters/theory/higher_genus_modular_koszul.tex:2653: strong scalar ansatz
chapters/theory/higher_genus_modular_koszul.tex:2699:strong scalar ansatz of
chapters/theory/higher_genus_modular_koszul.tex:21685:\index{multi-weight genus expansion|textbf}%
chapters/theory/higher_genus_modular_koszul.tex:22003:\begin{remark}[Resolution of the multi-generator universality problem]%
chapters/theory/higher_genus_modular_koszul.tex:22050:multi-weight genus expansion to a single new object: the
codex
I found another likely collision surface: `thm:obs-def-pairing-explicit` in `higher_genus_foundations.tex` states a “perfect pairing” with a very thin proof, but it is not the same as the complementarity chapter’s conditional Lagrangian upgrade. I’m reading the main complementarity theorem and this foundations theorem side by side because a stale or over-strong reuse between them would explain the user’s “Theorem C2” naming.
exec
/bin/zsh -lc 'rg -n "thm:deformation-obstruction|deformation-obstruction|quantum-complementarity-main|shifted-symplectic-complementarity|perfectness-criterion|prop:lagrangian-eigenspaces|thm:fiber-center-identification|thm:verdier-bar-cobar|thm:bv-functor|thm:config-space-bv" chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex metadata/claims.jsonl' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '180,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '520,900p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:2630:\textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar})}.
chapters/theory/higher_genus_foundations.tex:4179:Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
chapters/theory/higher_genus_foundations.tex:4196:The complementarity column follows from Theorem~\ref{thm:quantum-complementarity-main}
chapters/theory/higher_genus_foundations.tex:4890:The sign reversal is consistent with Main~Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}; the Kodaira--Spencer construction of Theorem~\ref{thm:kodaira-spencer-chiral-complete} provides the geometric mechanism):
chapters/theory/higher_genus_foundations.tex:4892:sees as the negative obstruction, confirming deformation-obstruction complementarity.
chapters/theory/higher_genus_foundations.tex:6100:\subsection{Connection to deformation-obstruction complementarity}
chapters/theory/higher_genus_foundations.tex:6119:as stated in Theorem~\ref{thm:deformation-obstruction}.
chapters/theory/higher_genus_foundations.tex:7137:(Theorem~\ref{thm:quantum-complementarity-main}), and the
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
chapters/theory/higher_genus_complementarity.tex:67: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:73: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
chapters/theory/higher_genus_complementarity.tex:89:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
chapters/theory/higher_genus_complementarity.tex:113:base change (Lemma~\ref{lem:perfectness-criterion}).
chapters/theory/higher_genus_complementarity.tex:185:\index{deformation-obstruction complexes|textbf}
chapters/theory/higher_genus_complementarity.tex:194:(Theorem~\ref{thm:verdier-bar-cobar}).
chapters/theory/higher_genus_complementarity.tex:195:Define the \emph{deformation-obstruction complexes} as homotopy eigenspaces:
chapters/theory/higher_genus_complementarity.tex:277:\label{lem:perfectness-criterion}
chapters/theory/higher_genus_complementarity.tex:351:\label{thm:fiber-center-identification}
chapters/theory/higher_genus_complementarity.tex:362:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
 succeeded in 52ms:
   180	
   181	\subsection{Statement of the theorem}
   182	
   183	\begin{definition}[Deformation-obstruction complexes: H-level]
   184	\label{def:complementarity-complexes}
   185	\index{deformation-obstruction complexes|textbf}
   186	Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$.
   187	The \emph{ambient complex} at genus~$g$ is
   188	\[
   189	\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
   190	\]
   191	where $\mathcal{Z}(\cA)$ is the center local system.
   192	The Verdier involution $\sigma$ acts on $\mathbf{C}_g(\cA)$ as a
   193	cochain-level endomorphism with $\sigma^2 = \mathrm{id}$
   194	(Theorem~\ref{thm:verdier-bar-cobar}).
   195	Define the \emph{deformation-obstruction complexes} as homotopy eigenspaces:
   196	\begin{equation}\label{eq:complementarity-fiber}
   197	\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \mathrm{id}\colon
   198	\mathbf{C}_g \to \mathbf{C}_g), \qquad
   199	\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \mathrm{id}\colon
 succeeded in 52ms:
   520	What one algebra sees as deformation, its dual sees as obstruction.
   521	\end{remark}
   522	
   523	\begin{proof}
   524	The proof occupies the remainder of this chapter,
   525	organized as three steps:
   526	Step~I (\S\ref{lem:genus-filtration}ff.) constructs the spectral
   527	sequence from the genus filtration;
   528	Step~II (from Theorem~\ref{thm:verdier-duality-config-complete})
   529	establishes Verdier duality for the configuration space complexes;
   530	Step~III (from Theorem~\ref{thm:kodaira-spencer-chiral-complete})
   531	constructs the Kodaira--Spencer map and identifies the eigenspaces
   532	as Lagrangian complements.
   533	\end{proof}
   534	
   535	\begin{remark}[External dependency status]
   536	\label{rem:theorem-c-mok-independence}
   537	Theorem~C depends on three inputs: the genus
   538	filtration spectral sequence (standard), Poincar\'e--Verdier
   539	duality on FM compactifications (standard algebraic


thinking
**Considering theorem discrepancies**

I'm trying to confirm whether the user's request for a theorem description matches the manuscript. It seems there's a discrepancy that needs addressing, as the findings should focus on those differences. I’m not sure if this is related to a bug in the manuscript, but clarifying those discrepancies is critical to help resolve any confusion. It’s important to ensure we’re aligned on this topic!
thinking
**Searching for C2 connections**

I'm searching for "C2" in my notes or connections. I found a potential label: `thm:thqg-III-lagrangian-polarization`, titled "Verdier Lagrangian polarization (C2)" in my document. This theorem is a conditional one, not uniform-weight. It doesn't seem like I have a source for scalar BV pairing. Maybe the phrasing from the user is the issue, but I need to ensure findings are ordered by severity. I wonder if there's any drift in how C2 is referenced elsewhere. Let's search for it in additional files to clarify.
codex
I’ve confirmed the first structural issue: in the live source, `C2` is the conditional BV/shifted-symplectic upgrade of complementarity, not a uniform-weight scalar theorem. I’m doing one last pass for internal drift around that label and then I’ll write the audit findings against the actual theorem/proof surfaces rather than the user’s informal name.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '860,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\(C2\\)|C2\\)|Theorem C2|scalar BV pairing|bar-side BV upgrade|shifted-symplectic-complementarity|uniform-weight\" chapters/theory/higher_genus_complementarity.tex chapters/connections/thqg_symplectic_polarization.tex chapters/connections/concordance.tex chapters/frame/guide_to_main_results.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   860	
   861	\begin{proposition}[{Kontsevich--Pridham correspondence; \ClaimStatusProvedElsewhere;
   862	\cite{Pridham17}}]
   863	\label{prop:thqg-III-kontsevich-pridham}
   864	\index{Kontsevich--Pridham correspondence}
   865	Let $\mathfrak{g}$ be a dg Lie algebra with a nondegenerate
   866	invariant pairing of degree $n$:
   867	\[
   868	\langle -, - \rangle
   869	\colon \mathfrak{g} \otimes \mathfrak{g}
   870	\to \mathbb{C}[n],
   871	\qquad
   872	\langle [x,y], z \rangle
   873	= \langle x, [y,z] \rangle.
   874	\]
   875	Then the formal moduli problem
   876	$\MC(\mathfrak{g})$ carries an $n$-shifted symplectic structure.
   877	\end{proposition}
   878	
   879	\begin{remark}[Two shifted structures in complementarity]
 succeeded in 51ms:
chapters/frame/guide_to_main_results.tex:249:The following holds for uniform-weight modular Koszul algebras
chapters/frame/guide_to_main_results.tex:254:For uniform-weight algebras, the genus-$g$ free energy is the
chapters/frame/guide_to_main_results.tex:309:for uniform-weight algebras at all genera,
chapters/frame/guide_to_main_results.tex:329:non-uniform-weight, non-convergence, non-algebraic family)
chapters/connections/thqg_symplectic_polarization.tex:38:\textup{(}Theorem~\ref{thm:shifted-symplectic-complementarity}\textup{)},
chapters/connections/thqg_symplectic_polarization.tex:44:shifted-symplectic Lagrangian structure~(C2) becomes the natural
chapters/connections/thqg_symplectic_polarization.tex:63:shifted-symplectic structure~(C2), including a self-contained
chapters/connections/thqg_symplectic_polarization.tex:776:% 3. SHIFTED-SYMPLECTIC STRUCTURE (C2)
chapters/connections/thqg_symplectic_polarization.tex:786:The conditional upgrade~(C2) endows the ambient complex with a
chapters/connections/thqg_symplectic_polarization.tex:922:This is Theorem~\ref{thm:shifted-symplectic-complementarity} rewritten
chapters/connections/thqg_symplectic_polarization.tex:930:\begin{theorem}[Verdier Lagrangian polarization (C2);
chapters/connections/thqg_symplectic_polarization.tex:1048:\begin{remark}[Conditionality of (C2)]
chapters/connections/thqg_symplectic_polarization.tex:1873:Koszul locus), but the Lagrangian upgrade~(C2) breaks down:
chapters/connections/thqg_symplectic_polarization.tex:2029:polarization \textup{(C2)}, and the complementarity potential
chapters/theory/introduction.tex:361:function on the uniform-weight lane; the multi-weight
chapters/theory/introduction.tex:627: and $F_g = \kappa \cdot \hat{A}_g$, hold on the uniform-weight
chapters/theory/introduction.tex:639: On the uniform-weight lane, the generating function is the
chapters/theory/introduction.tex:754: On the uniform-weight lane, the degree-$2$ genus-$g$ component is
chapters/theory/introduction.tex:833: uniform-weight lane.
chapters/theory/introduction.tex:837: On the uniform-weight lane, the genus-$g$ obstruction
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1866,1985p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1866	\label{sec:shifted-symplectic-complementarity}
  1867	\index{shifted symplectic!complementarity|textbf}
  1868	
  1869	Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
  1870	Lagrangian polarization at the level of cohomology, and
  1871	Proposition~\ref{prop:ptvv-lagrangian} upgrades the Verdier side to a
  1872	proved shifted-symplectic statement on the ambient complex~$C_g$. The
  1873	direct bar-side realization of a $(-1)$-shifted symplectic chart on
  1874	$L_g = \barB^{(g)}(\cA)[1]$ would require the additional BV package of
  1875	Chapter~\ref{ch:bv-brst}. The following theorem records that bar-side
  1876	upgrade conditionally.
  1877	
  1878	\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
  1879	\label{thm:shifted-symplectic-complementarity}
  1880	\index{shifted symplectic!(-1)-shifted|textbf}
  1881	\index{Lagrangian!complementarity!shifted symplectic|textbf}
  1882	\textup{[Regime: curved-central on the Koszul locus; all genera
  1883	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1884	
  1885	Assume the conditional BV package of
codex
I’ve isolated the first genuine manuscript error: the “strong scalar ansatz” wording is stale and now points to a theorem that proves the opposite conclusion. I’m checking one more possible proof-level fault inside the actual C2 theorem, because its proof appears to toggle between `D(barB(A)) ≅ barB(A^!)` and `D(barB(A)) ≅ Ω(A^!)`, which would be an object-conflation if the cited theorem really says the latter.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1280,1388p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"D\\(\\\\barB|mathbb\\{D\\}.*barB|Omega\\(\\\\cA\\"'^!'"\\)|barB\\(\\\\cA\\"'^!'"\\)|bv-functor\" chapters/connections/bv_brst.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/cobar_construction.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1290,1338p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1280	$(A, \cdot)$ equipped with a degree-$+1$ operator
  1281	$\Delta\colon A \to A$ satisfying:
  1282	\begin{enumerate}[label=\textup{(\roman*)}]
  1283	\item \emph{Nilpotency}: $\Delta^2 = 0$.
  1284	\item \emph{Second-order}: $\Delta$ is a second-order operator, meaning the
  1285	 \emph{BV bracket}
  1286	 \[
  1287	 \{a, b\} := (-1)^{|a|}\bigl[\Delta(ab) - \Delta(a)\,b
  1288	 - (-1)^{|a|} a\,\Delta(b)\bigr]
  1289	 \]
  1290	 (the failure of $\Delta$ to be a graded derivation) satisfies the
  1291	 graded Leibniz rule in each slot:
  1292	 \begin{gather*}
  1293	 \{a, bc\} = \{a, b\}\,c + (-1)^{(|a|+1)|b|} b\,\{a, c\},\\
  1294	 \{a, b\} = -(-1)^{(|a|+1)(|b|+1)}\{b, a\}.
  1295	 \end{gather*}
  1296	\end{enumerate}
  1297	The bracket automatically satisfies the graded Jacobi identity.
  1298	\end{definition}
  1299	
 succeeded in 50ms:
  1290	
  1291	\begin{remark}[CFT vertex operators from cobar]\label{rem:vertex-operators-cobar}
  1292	In conformal field theory, vertex operators $V_\alpha(z)$ create states $|\alpha\rangle$ 
  1293	at position $z$. These correspond to cobar elements:
  1294	\[V_\alpha \leftrightarrow K_\alpha \in \Omega^1(\mathcal{C})\]
  1295	
  1296	The OPE of vertex operators:
  1297	\[V_\alpha(z) V_\beta(w) \sim \sum_\gamma \frac{C_{\alpha\beta}^\gamma}{(z-w)^{h_\gamma - h_\alpha - h_\beta}} V_\gamma(w)\]
  1298	
  1299	corresponds to the cobar product:
  1300	\[n_2(K_\alpha, K_\beta) = \sum_\gamma C_{\alpha\beta}^\gamma K_\gamma\]
  1301	
  1302	The structure constants $C_{\alpha\beta}^\gamma$ are precisely the cobar $A_\infty$ 
  1303	structure constants.
  1304	
  1305	The cobar construction thus provides a geometric derivation
  1306	of the OPE algebra in CFT.
  1307	\end{remark}
  1308	
  1309	\subsection{Verdier duality on bar and cobar}
 exited 2 in 51ms:
rg: regex parse error:
    (?:D\(\barB|mathbb\{D\}.*barB|Omega\(\cA\^!\)|barB\(\cA\^!\)|bv-functor)
                                         ^^
error: unrecognized escape sequence
codex
There is a real object-identity problem inside the actual C2 proof: the theorem statement uses `D_Ran(\barB(A)) ≅ \barB(A^!)`, but the proof switches to `D(\barB(A)) ≅ Ω(A^!)`. I’m checking the cited corollary to make sure this isn’t salvaged elsewhere before I mark it as a defect.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1748,1858p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "cor:duality-bar-complexes-complete|duality-bar-complexes-complete|Koszul duality pairing|perfect pairing" chapters/theory chapters/connections' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '4080,4165p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1748	S-level (cohomological) and H-level (homotopy) claims of
  1749	Theorem~\ref{thm:quantum-complementarity-main} via three steps.
  1750	\emph{First}, the Verdier involution~$\sigma$ is a
  1751	\emph{cochain-level} involution on
  1752	$\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$:
  1753	it is induced by the composition of Verdier duality~$\mathbb{D}$
  1754	(an exact functor on $D^b_{\mathrm{hol}}(\mathcal{D})$) with the
  1755	Koszul identification
  1756	$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$
  1757	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
  1758	Since~$\sigma$ is induced by exact functors, it commutes with
  1759	differentials at every page of the spectral sequence
  1760	(Lemma~\ref{lem:verdier-involution-moduli}).
  1761	\emph{Second}, Lemma~\ref{lem:involution-splitting}(a) gives
  1762	the cochain-level splitting: the projectors
  1763	$p^\pm = \tfrac{1}{2}(\mathrm{id} \pm \sigma)$ are cochain maps
  1764	whose images provide a quasi-isomorphic direct sum decomposition
  1765	$\mathbf{C}_g \simeq \operatorname{im}(p^+) \oplus \operatorname{im}(p^-)$.
  1766	\emph{Third}, model independence
  1767	(Proposition~\ref{prop:model-independence}) ensures the
 succeeded in 51ms:
chapters/connections/thqg_symplectic_polarization.tex:176:The Koszul pairing restricts to a perfect pairing on centers
chapters/connections/thqg_symplectic_polarization.tex:178:(Corollary~\ref{cor:duality-bar-complexes-complete} and
chapters/connections/thqg_symplectic_polarization.tex:227:Corollary~\ref{cor:duality-bar-complexes-complete},
chapters/connections/thqg_symplectic_polarization.tex:403:and Serre duality on the stack gives a perfect pairing on
chapters/theory/poincare_duality.tex:129:perfect pairing
chapters/theory/poincare_duality.tex:172:There exists a canonical perfect pairing:
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:227:\item perfect pairings
chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:231:\item induced perfect pairings on reduced bar slices
chapters/connections/thqg_fredholm_partition_functions.tex:2701:$\cZ(\cA)$ carries the perfect pairing from
chapters/theory/higher_genus_foundations.tex:1423:Applied to the sheaf $j_!\mathbb{C}_{C_n(X)}$ where $j: C_n(X) \hookrightarrow \overline{C}_n(X)$ is the open inclusion, this exchanges $j_!$ and $Rj_*$ (Theorem~\ref{thm:verdier-config}), identifying logarithmic forms on the compactification with distributional forms on the open configuration space. The perfect pairing $\langle \eta_{ij}, \delta(z_i - z_j) \rangle = 1$ realizes the NAP isomorphism at the level of differential forms, since residues (bar operations) and delta functions (cobar operations) are Verdier duals.
chapters/connections/thqg_gravitational_s_duality.tex:325:the perfect pairing
chapters/connections/holographic_codes_koszul.tex:193:is a perfect pairing
chapters/connections/holographic_codes_koszul.tex:252: $\cC \times \mathbf{Q}_g(\cA^!)$ is a perfect pairing
chapters/theory/higher_genus_complementarity.tex:608:& Establish perfect pairing between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$\\
chapters/theory/higher_genus_complementarity.tex:1093:is a perfect pairing. This is the geometric incarnation of Verdier duality.
chapters/theory/higher_genus_complementarity.tex:1117:\label{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:1118:The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
chapters/theory/higher_genus_complementarity.tex:1126:\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
chapters/theory/higher_genus_complementarity.tex:1173:By Corollary~\ref{cor:duality-bar-complexes-complete}, the pairing:
chapters/theory/higher_genus_complementarity.tex:1229:induces a duality of spectral sequences and a perfect pairing
 succeeded in 51ms:
  4080	$\barB^{p,q}(\cA)$ compatible with the conformal grading
  4081	\textup{(}i.e., the total conformal weight is bounded by a
  4082	function of the bigrading\textup{)},
  4083	the growth bound
  4084	\[
  4085	\dim E_1^{0,p} < c^p
  4086	\qquad\text{for every } c>1 \text{ and all sufficiently large } p
  4087	\]
  4088	holds automatically.
  4089	\end{proposition}
  4090	
  4091	\begin{proof}
  4092	The bar complex at bar degree~$n$ and conformal weight~$h$ satisfies
  4093	$\barB^{n}_{[h]} \subset (\bar{\cA})^{\otimes n}_{[h]}$, hence
  4094	\begin{equation}\label{eq:bar-dim-bound}
  4095	\dim \barB^{n}_{[h]}
  4096	\;\leq\;
  4097	\sum_{\substack{h_1 + \cdots + h_n = h \\ h_i \geq 1}}
  4098	\prod_{i=1}^n \dim \cA_{h_i}.
  4099	\end{equation}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1090,1145p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1090	H^k(\overline{C}_n(X)) \times H^{2n-k}(\overline{C}_n(X)) \xrightarrow{\wedge} 
  1091	H^{2n}(\overline{C}_n(X)) \xrightarrow{\int} \mathbb{C}
  1092	\end{equation}
  1093	is a perfect pairing. This is the geometric incarnation of Verdier duality.
  1094	
  1095	\emph{Logarithmic forms}: When we include logarithmic forms $\Omega^*_{\log}(
  1096	\overline{C}_n(X))$ (forms with logarithmic poles along $\partial \overline{C}_n(X)$), 
  1097	the duality becomes:
  1098	\begin{equation}
  1099	\Omega^k_{\log}(\overline{C}_n(X)) \times \Omega^{2n-k}_{\log}(\overline{C}_n(X)) 
  1100	\to \mathbb{C}
  1101	\end{equation}
  1102	given by:
  1103	\begin{equation}
  1104	\langle \eta, \xi \rangle = \text{Res}_{\partial \overline{C}_n(X)} (\eta \wedge \xi)
  1105	\end{equation}
  1106	where $\text{Res}$ denotes the Poincaré residue map.
  1107	
  1108	This pairing is also perfect, by the logarithmic Poincar\'e lemma
  1109	(Deligne~\cite{Deligne71}, Hodge~II, Proposition~3.1.8), which
codex
The C2 proof has a confirmed bar/cobar conflation. I’m doing the same circularity check on the scalar proof now, because `genus-universality` invokes `family-index`, and if `family-index` is itself derived from `genus-universality`, the uniform-weight step is only packaging, not proof.
exec
/bin/zsh -lc 'rg -n "thm:family-index|Family index theorem|family index theorem" chapters/theory/higher_genus_foundations.tex chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex metadata/claims.jsonl' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6600,6895p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '540,670p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/guide_to_main_results.tex:238:\subsection*{Family index theorem}
chapters/frame/guide_to_main_results.tex:240:\begin{theorem}[Family index theorem for genus expansions;
chapters/connections/concordance.tex:4712:Index & GRR: scalar genus series $= \kappa(\cA) \cdot (\hat{A}(ix) - 1)$; genus-$1$ unconditional & \textbf{Proved} & Thm~\ref{thm:family-index} \\[2pt]
chapters/connections/concordance.tex:5927:\begin{theorem}[Family index theorem for genus expansions;
chapters/connections/concordance.tex:5928:\ClaimStatusProvedHere]\label{thm:family-index}
chapters/connections/concordance.tex:6227:Theorem~\ref{thm:family-index} synthesizes the preceding results:
chapters/connections/concordance.tex:6238:and the family index theorem follows.
chapters/theory/higher_genus_foundations.tex:194:(Theorem~\ref{thm:family-index}).
chapters/theory/higher_genus_foundations.tex:635:(Theorem~\ref{thm:family-index}).
chapters/theory/higher_genus_foundations.tex:689: \textup{(}Theorem~\textup{\ref{thm:family-index})}:
chapters/theory/higher_genus_foundations.tex:755:is $\lambda_g$ (Theorem~\ref{thm:family-index}).
chapters/theory/higher_genus_foundations.tex:1083:(Theorem~\ref{thm:family-index}). The scalar $\kappa(\cA)$ is the
chapters/theory/higher_genus_foundations.tex:5329:= \kappa(\cA)\cdot\lambda_g$ (Theorem~\ref{thm:family-index}).
chapters/theory/higher_genus_foundations.tex:6310:\begin{remark}[Family index theorem]\label{rem:towards-family-index}
chapters/theory/higher_genus_foundations.tex:6312:The family index theorem (Theorem~\ref{thm:family-index}) assembles
chapters/theory/higher_genus_foundations.tex:6712: family index theorem
chapters/theory/higher_genus_foundations.tex:6713: \textup{(}Theorem~\textup{\ref{thm:family-index})}: the
chapters/theory/higher_genus_foundations.tex:6750:(iii)~The family index theorem
chapters/theory/higher_genus_foundations.tex:6751:(Theorem~\ref{thm:family-index}) gives
chapters/theory/higher_genus_foundations.tex:6821:the third in Theorem~\ref{thm:family-index}.
 succeeded in 52ms:
   540	 \end{equation}
   541	 The first term is holomorphic with monodromy; the second
   542	 is smooth and restores double periodicity.
   543	
   544	\item \emph{Curvature equation.}\;
   545	 The fiberwise bar differential satisfies
   546	 \begin{equation}\label{eq:curvature-package}
   547	 \dfib^{\,2}
   548	 \;=\;
   549	 \kappa(\cA) \cdot \omega_g \cdot \mathrm{id},
   550	 \qquad
   551	 \omega_g
   552	 \;=\;
   553	 \frac{i}{2}\sum_{\alpha,\beta=1}^{g}
   554	 (\operatorname{Im}\Omega)^{-1}_{\alpha\beta}\,
   555	 \omega_\alpha \wedge \overline{\omega}_\beta,
   556	 \end{equation}
   557	 where $\omega_g$ is the Arakelov $(1,1)$-form and
   558	 $\kappa(\cA) = \mathrm{Tr}_\cA = \sum_a\langle e_a,
   559	 e^a\rangle$ is the self-contraction trace.
 succeeded in 52ms:
  6600	 \bigotimes_{v \in V}
  6601	 H^*\!\bigl(\barB^{(g_v)}(\cA)\bigr)[\mathrm{val}(v)],
  6602	 \end{equation}
  6603	 i.e., tree-level compositions of lower-genus bar cohomology.
  6604	
  6605	\item \emph{Maximal loop order} \textup{(}$\ell = g$\textup{):}
  6606	 The summand $E_0^{g,*}$ consists of stable graphs with
  6607	 $b_1(\Gamma) = g$ \textup{(}all vertices genus~$0$\textup{)}.
  6608	 Its $d_0$-cohomology is:
  6609	 \begin{equation}\label{eq:max-loop-page}
  6610	 E_1^{g,*}
  6611	 \;\cong\;
  6612	 \bigoplus_{\substack{
  6613	 \Gamma \in \mathcal{G}_{g,n}^{\mathrm{st}}\\
  6614	 g_v = 0 \;\forall v}}
  6615	 \bigotimes_{v \in V(\Gamma)}
  6616	 H^*\!\bigl(\barB^{(0)}(\cA)\bigr)[\mathrm{val}(v)]
  6617	 \;\otimes\;
  6618	 \det(E(\Gamma)),
  6619	 \end{equation}

thinking
**Investigating theorem metadata**

I’m noticing that `thm:family-index` only appears in concordance, but not in the source for higher-genus foundations. I’m thinking it might be missing there. When I look at the references, especially around 5927, it seems strange that `thm:family-index` is cited in the genus-universality proof, yet it only exists in concordance. This could be generated metadata, so I need to check if there’s a theorem labeled `thm:family-index` in concordance. If it's there, it might change things a bit.
codex
The scalar proof has another potential structural problem: `thm:genus-universality` cites `thm:family-index`, but the only live theorem with that label appears to be in `concordance.tex`, where metadata already says it depends on `thm:genus-universality`. I’m checking that block directly to see whether this is a circular citation or just a summary theorem with a duplicate label.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5920,6018p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
  5930	\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
  5931	Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
  5932	$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
  5933	\overline{\mathcal{M}}_g$ be the universal curve with relative
  5934	dualizing sheaf~$\omega_\pi$, and let
  5935	$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
  5936	The following holds for uniform-weight modular Koszul algebras
  5937	at all genera; the genus-$1$ statements are unconditional for
  5938	all families, including multi-generator.
  5939	Define the \emph{modular deformation complex} of~$\cA$ at genus~$g$ by
exec
/bin/zsh -lc "rg -n \"\\\\label\\{thm:family-index\\}\" chapters metadata" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"family index theorem follows|Theorem~\\\\ref\\{thm:family-index\\} synthesizes|depends on thm:genus-universality|refs_in_block.*thm:genus-universality\" chapters/connections/concordance.tex metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\label\{thm:family-index\})
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/connections/concordance.tex:6238:and the family index theorem follows.
metadata/claims.jsonl:155:{"label": "rem:bv-bar-bridge", "env_type": "remark", "status": "Heuristic", "file": "chapters/connections/bv_brst.tex", "line": 61, "title": "BV/bar dictionary", "refs_in_block": ["thm:bv-bar-geometric", "thm:genus-universality", "comp:virasoro-curvature"]}
metadata/claims.jsonl:169:{"label": "cor:anomaly-duality-km", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1019, "title": "Anomaly duality for Kac--Moody pairs", "refs_in_block": ["thm:bar-cohomology-level-independence", "thm:genus-universality", "thm:quantum-complementarity-main", "thm:explicit-theta"]}
metadata/claims.jsonl:240:{"label": "thm:family-index", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5769, "title": "Family index theorem for genus expansions", "labels_in_block": ["thm:family-index", "eq:modular-deformation-complex-concordance", "eq:family-index-grr", "eq:family-index-generating"], "refs_in_block": ["thm:genus-universality"]}
metadata/claims.jsonl:300:{"label": "thm:volume-one-concrete-modular-datum", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/editorial_constitution.tex", "line": 2470, "title": "Volume~I concrete modular datum", "refs_in_block": ["def:modular-koszul-homotopy", "thm:bar-cobar-isomorphism-main", "thm:quantum-complementarity-main", "thm:mc2-bar-intrinsic", "def:modular-koszul-chiral", "thm:bar-nilpotency-complete", "thm:genus-universality", "thm:quantum-diff-squares-zero", "def:full-modular-package", "thm:modular-characteristic", "thm:discriminant-spectral", "rem:periodicity-triple"]}
metadata/claims.jsonl:419:{"label": "thm:extension-obstruction", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/connections/genus_complete.tex", "line": 133, "title": "Extension obstruction; {} \\cite{FBZ04,CG17}", "refs_in_block": ["thm:genus-universality"], "cites_in_block": ["FBZ04", "CG17"]}
metadata/claims.jsonl:483:{"label": "thm:ht-mc-all-genera", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/holomorphic_topological.tex", "line": 150, "title": "MC element and all-genus HT partition function", "labels_in_block": ["thm:ht-mc-all-genera", "eq:ht-theta"], "refs_in_block": ["thm:mc2-bar-intrinsic", "def:shadow-postnikov-tower", "thm:genus-universality", "thm:multi-weight-genus-expansion"]}
metadata/claims.jsonl:490:{"label": "rem:burns-f2-verification", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/holomorphic_topological.tex", "line": 1190, "title": "Burns space $F_2$ prediction", "refs_in_block": ["thm:genus-universality"], "cites_in_block": ["CPS2208", "CPS2306"]}
metadata/claims.jsonl:594:{"label": "cor:g9-partition-trace", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/thqg_critical_string_dichotomy.tex", "line": 2128, "title": "Genus-$g$ partition function via trace", "labels_in_block": ["cor:g9-partition-trace", "eq:g9-Fg-trace"], "refs_in_block": ["thm:genus-universality"]}
metadata/claims.jsonl:1165:{"label": "thm:fermion-F1-shadow", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/free_fields.tex", "line": 4097, "title": "Free fermion genus-1 free energy", "labels_in_block": ["thm:fermion-F1-shadow", "eq:fermion-F1-shadow-verification"], "refs_in_block": ["thm:genus-universality"]}
metadata/claims.jsonl:1173:{"label": "thm:algebraic-string-dictionary", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/free_fields.tex", "line": 4746, "title": "Algebraic bar/BRST genus dictionary", "refs_in_block": ["thm:bar-semi-infinite-km", "thm:brst-bar-genus0", "cor:anomaly-duality-km", "rem:w3-kappa-sums", "thm:genus-universality", "thm:genus-induction-strict"]}
metadata/claims.jsonl:1215:{"label": "prop:bivariate-gf", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/examples/genus_expansions.tex", "line": 770, "title": "Bivariate generating function", "labels_in_block": ["prop:bivariate-gf", "eq:bivariate-gf", "eq:bivariate-gf-general"], "refs_in_block": ["thm:modular-characteristic", "thm:genus-universality"]}
metadata/claims.jsonl:1221:{"label": "cor:virasoro-genus2-curvature", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/genus_expansions.tex", "line": 1294, "title": "Genus-2 Virasoro curvature", "labels_in_block": ["cor:virasoro-genus2-curvature", "eq:vir-obs2", "eq:vir-F2"], "refs_in_block": ["thm:genus-universality"]}
metadata/claims.jsonl:1246:{"label": "prop:loop-expansion-knots", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/examples/genus_expansions.tex", "line": 3663, "title": "Loop expansion interpretation", "refs_in_block": ["thm:genus-universality", "ch:kontsevich-integral"]}
metadata/claims.jsonl:1259:{"label": "thm:heisenberg-genus2-obstruction", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/heisenberg_eisenstein.tex", "line": 561, "title": "Genus-2 obstruction class for \\texorpdfstring{$\\mathcal{H}_\\kappa$}{H_kappa}", "labels_in_block": ["thm:heisenberg-genus2-obstruction", "eq:heisenberg-genus2-curvature"], "refs_in_block": ["thm:genus-universality", "def:genus-g-obstruction"]}
metadata/claims.jsonl:1355:{"label": "cor:genus1-anomaly-ratio", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/landscape_census.tex", "line": 1241, "title": "Genus-\\texorpdfstring{$1$}{1} free energy and anomaly ratio", "labels_in_block": ["cor:genus1-anomaly-ratio", "eq:F1-over-c"], "refs_in_block": ["rem:genus-1-verification", "thm:genus-universality"]}
metadata/claims.jsonl:1579:{"label": "thm:vir-genus1-curvature", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/w_algebras.tex", "line": 1577, "title": "Genus-1 curvature for \\texorpdfstring{$\\mathrm{Vir}_c$}{Virc}", "labels_in_block": ["thm:vir-genus1-curvature", "eq:vir-genus1-dsquared"], "refs_in_block": ["thm:genus-universality"]}
metadata/claims.jsonl:1585:{"label": "thm:w3-genus1-curvature", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/w_algebras.tex", "line": 1942, "title": "Genus-1 curvature for \\texorpdfstring{$\\mathcal{W}_3$}{W3}", "labels_in_block": ["thm:w3-genus1-curvature", "eq:w3-genus1-dsquared"], "refs_in_block": ["thm:genus-universality"]}
metadata/claims.jsonl:2892:{"label": "thm:tautological-line-support", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 9394, "title": "Tautological line support from genus universality", "refs_in_block": ["mc2-hyp:cyclic", "mc2-hyp:tautological", "thm:genus-universality"]}
metadata/claims.jsonl:3407:{"label": "prop:genus1-curvature-m0", "env_type": "proposition", "status": "ProvedHere", "file": "appendices/homotopy_transfer.tex", "line": 734, "title": "Genus-\\texorpdfstring{$1$}{1} curvature as \\texorpdfstring{$m_0$}{m0}", "refs_in_block": ["thm:genus-universality"]}
codex
The scalar proof is indeed circular through `thm:family-index`. I’m checking one last dependency: whether there is any separate theorem that actually kills the cross-channel terms on the uniform-weight locus, because `genus-universality` itself currently only argues from edge data and GRR, which would not be enough on its own.
exec
/bin/zsh -lc "rg -n \"thm:algebraic-family-rigidity|algebraic-family rigidity|uniform-weight universality|delta F_g\\"'^'"\\{\\\\mathrm\\{cross\\}\\} = 0|delta F_g\\"'^'"\\{cross\\} = 0|Theorem~\\\\ref\\{thm:algebraic-family-rigidity\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:thm:algebraic-family-rigidity|algebraic-family rigidity|uniform-weight universality|delta F_g\^\{\mathrm\{cross\}\} = 0|delta F_g\^\{cross\} = 0|Theorem~\ref\{thm:algebraic-family-rigidity\})
                                                                                                        ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21718,21730p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '20380,20540p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 21718	
 21719	\item \emph{Genus-$1$ universality.}
 21720	 $\delta F_1^{\mathrm{cross}} = 0$ for all\/~$\cA$.
 21721	
 21722	\item \emph{Uniform-weight universality.}
 21723	 If\/ $h_1 = h_2 = \cdots = h_r$, then\/
 21724	 $\delta F_g^{\mathrm{cross}} = 0$ for all\/ $g \geq 1$
 21725	 \textup{(}Theorem~\textup{\ref{thm:algebraic-family-rigidity})}.
 21726	
 21727	\item \emph{$R$-matrix independence.}
 21728	 The cross-channel correction $\delta F_g^{\mathrm{cross}}$
 21729	 is independent of the Givental $R$-matrix:
 21730	 genus-$0$ boundary vertices receive no $R$-contribution,
 succeeded in 52ms:
 20380	 every simple $\fg$, the $\kappa$-conductor is strictly positive
 20381	 for every $\cW$-algebra.
 20382	\item For the Virasoro algebra $(\fg = \mathfrak{sl}_2)$:
 20383	 $K_{\mathfrak{sl}_2} = 26$,
 20384	 $\varrho(\mathfrak{sl}_2) = H_2 - 1 = 1/2$, so
 20385	 \begin{equation}\label{eq:virasoro-conductor-thirteen}
 20386	 \kappa(\operatorname{Vir}_c) + \kappa(\operatorname{Vir}_{26-c})
 20387	 \;=\; 13
 20388	 \;=\; \tfrac{1}{2}\,K_{\mathfrak{sl}_2}.
 20389	 \end{equation}
 20390	 The value $K_{\mathfrak{sl}_2} = 26$ is the critical dimension
 20391	 of the bosonic string; the $\kappa$-conductor $13$ is half
 20392	 this value, reflecting the passage from central charges
 20393	 $c + c' = 26$ to their $\kappa$-projections
 20394	 $\kappa + \kappa' = (c + c')/2 = 13$.
 20395	\end{enumerate}
 20396	The $\kappa$-conductor $\kappa(\cA) + \kappa(\cA^!)$ measures the
 20397	obstruction to extending complementarity
 20398	\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}
 20399	from genus~$0$ to higher genus without correction: the

thinking
**Finding algebraic-family rigidity proof**

I need to locate the proof for the algebraic-family rigidity theorem. Searching might not be necessary if I'm only looking for the existence of the theorem. However, it could be relevant to determining if uniform-weight suffices. I'll need to audit whether the theorem indeed implies δF=0, so I should check the statement closely for clarity. It feels vital to ensure I'm on the right track with my reasoning!
exec
/bin/zsh -lc "rg -n \"label\\{thm:algebraic-family-rigidity\\}|algebraic-family-rigidity\" chapters/theory/higher_genus_modular_koszul.tex metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/claims.jsonl:246:{"label": "rem:four-test-interface", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 7345, "title": "The four-test interface", "refs_in_block": ["thm:bar-modular-operad", "thm:quantum-diff-squares-zero", "thm:mc2-bar-intrinsic", "thm:modular-characteristic", "thm:algebraic-family-rigidity", "thm:quantum-complementarity-main", "thm:ambient-complementarity-fmp", "thm:general-hs-sewing", "rem:thqg-I-admissible", "thm:heisenberg-sewing", "op:multi-generator-universality", "thm:multi-weight-genus-expansion", "thm:heisenberg-bv-bar-all-genera", "conj:master-bv-brst", "conj:analytic-realization"]}
metadata/claims.jsonl:2845:{"label": "thm:explicit-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 4082, "title": "Explicit universal MC class", "labels_in_block": ["thm:explicit-theta", "eq:theta-minimal", "eq:theta-chain", "eq:theta-genus1", "eq:l2-vanishes", "eq:genus-g-recursion", "eq:theta-generating-function"], "refs_in_block": ["thm:mc2-1-km", "thm:cyclic-rigidity-generic", "thm:algebraic-family-rigidity", "cor:km-minimal-linf", "prop:cyclic-ce-identification", "constr:linf-from-graphs", "thm:family-index"]}
metadata/claims.jsonl:2877:{"label": "cor:scalar-saturation", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 7710, "title": "One-channel line concentration of the minimal MC\nclass", "refs_in_block": ["thm:mc2-1-km", "thm:cyclic-rigidity-generic", "cor:effective-quadruple", "thm:algebraic-family-rigidity"]}
metadata/claims.jsonl:2883:{"label": "prop:saturation-equivalence", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 8230, "title": "Cyclic rigidity and level-direction concentration", "refs_in_block": ["thm:cyclic-rigidity-generic", "cor:effective-quadruple", "thm:algebraic-family-rigidity"]}
metadata/claims.jsonl:2887:{"label": "thm:algebraic-family-rigidity", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 8848, "title": "Algebraic-family rigidity"}
metadata/claims.jsonl:2888:{"label": "cor:saturation-algebraic-families", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 8960, "title": "Level-direction concentration at all non-critical levels for\nalgebraic families", "refs_in_block": ["thm:algebraic-family-rigidity", "prop:saturation-functorial"], "cites_in_block": ["FL88"]}
metadata/claims.jsonl:2890:{"label": "cor:one-channel-no-lie", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 9136, "title": "One-channel criterion without Lie symmetry", "refs_in_block": ["thm:conformal-bootstrap-rigidity", "thm:algebraic-family-rigidity"]}
metadata/claims.jsonl:2891:{"label": "conj:scalar-saturation-universality", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 9216, "title": "Scalar saturation universality", "labels_in_block": ["conj:scalar-saturation-universality", "eq:theta-multi-scalar", "eq:mc-decoupled"], "refs_in_block": ["cor:effective-quadruple", "thm:cyclic-rigidity-generic", "thm:algebraic-family-rigidity", "prop:saturation-equivalence"]}
metadata/claims.jsonl:2976:{"label": "thm:multi-weight-genus-expansion", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 20860, "title": "Multi-weight genus expansion", "labels_in_block": ["thm:multi-weight-genus-expansion", "thm:multi-generator-universality", "eq:multi-weight-diagonal", "eq:multi-weight-decomposition", "eq:multi-weight-genus2-explicit", "eq:w3-genus2-cross"], "refs_in_block": ["thm:shadow-channel-decomposition", "constr:cross-channel-graph-sum", "thm:algebraic-family-rigidity", "fig:genus2-stable-graphs", "comp:w3-genus2-multichannel", "op:multi-generator-universality"]}
metadata/claims.jsonl:3048:{"label": "cor:tropical-cohen-macaulay", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 27734, "title": "Tropical Koszulness as the Cohen--Macaulay property", "refs_in_block": ["thm:algebraic-family-rigidity", "thm:tropical-koszulness", "thm:mc2-bar-intrinsic"]}
chapters/theory/higher_genus_modular_koszul.tex:4198:Theorem~\textup{\ref{thm:algebraic-family-rigidity}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:7845:Theorem~\textup{\ref{thm:algebraic-family-rigidity}}.
chapters/theory/higher_genus_modular_koszul.tex:8313:Theorem~\ref{thm:algebraic-family-rigidity} settles only the
chapters/theory/higher_genus_modular_koszul.tex:8373: \textup{(}Theorem~\textup{\ref{thm:algebraic-family-rigidity}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:8509:Theorem~\ref{thm:algebraic-family-rigidity}
chapters/theory/higher_genus_modular_koszul.tex:8934:What Theorem~\ref{thm:algebraic-family-rigidity} proves for
chapters/theory/higher_genus_modular_koszul.tex:8947:Theorem~\ref{thm:algebraic-family-rigidity} answers only the first
chapters/theory/higher_genus_modular_koszul.tex:8953:\label{thm:algebraic-family-rigidity}
chapters/theory/higher_genus_modular_koszul.tex:9070:Theorem~\textup{\ref{thm:algebraic-family-rigidity}}\textup{)}
chapters/theory/higher_genus_modular_koszul.tex:9096: Theorem~\textup{\ref{thm:algebraic-family-rigidity}}.

thinking
**Looking into algebraic theorems**

I need to read up on the algebraic family rigidity theorem to see if it really implies uniform weight universality. It’s possible that it only proves one-dimensional H^2 and not δF=0. I should search around theorem lines, particularly number 8953, to gather more insight. Making sure I understand the implications will definitely help clarify things!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '8940,9078p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  8940	At generic level, Kazhdan--Lusztig semisimplicity kills
  8941	$H^2_{\mathrm{cyc,prim}}$
  8942	(Corollary~\ref{cor:effective-quadruple}).
  8943	At admissible levels, the module category is non-semisimple, and
  8944	the question becomes: \emph{does the MC moduli remain
  8945	one-dimensional, and does the corresponding coefficient equal
  8946	$\kappa\Lambda$?}
  8947	Theorem~\ref{thm:algebraic-family-rigidity} answers only the first
  8948	question for algebraic families; the second remains open for
  8949	multi-weight examples.
  8950	\end{remark}
  8951	
  8952	\begin{theorem}[Algebraic-family rigidity; \ClaimStatusProvedHere]
  8953	\label{thm:algebraic-family-rigidity}
  8954	\index{cyclic cohomology!algebraic-family rigidity}
  8955	\index{scalar saturation!algebraic-family proof}
  8956	\index{Whitehead decomposition!algebraic-family upgrade}
  8957	Let $\{{\cA}_k\}_{k \in U}$ be a family of vertex algebras
  8958	over a Zariski-open $U \subset \mathbb{C}$ with
  8959	$-h^\vee \notin U$, each equipped with simple affine current

thinking
**Examining channel construction**

I'm considering that this approach might make sense if channels are defined solely by weights and not by generator labels. However, the statement references generator index i, which complicates things a bit. I think I should delve into the construction of `cross-channel-graph-sum`. Maybe it's worth defining mixed-channel by different weights or distinct channels. I’ll need to search for more information on this to clarify.
codex
There is a stronger defect than stale wording: `thm:multi-weight-genus-expansion` claims uniform-weight forces `δF_g^{cross}=0` by citing `thm:algebraic-family-rigidity`, but that cited theorem explicitly says it only proves one-dimensional line concentration and does **not** prove the tautological-purity identification `Γ_A = κ(A)Λ`. I’m checking whether the graph-sum construction defines “cross-channel” by weight or by generator label, because if it is by label then equal weights do not even remove the mixed assignments combinatorially.
exec
/bin/zsh -lc 'rg -n "constr:cross-channel-graph-sum|cross-channel-graph-sum|mixed-channel|channel assignments|uniform-weight universality|generator label|same conformal weight" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21480,21680p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '22040,22190p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2501:strong generator of~$\cA$ has the same conformal weight.
21716: mixed-channel boundary graphs of\/ $\overline{\mathcal{M}}_{g,0}$
21717: \textup{(}Construction~\textup{\ref{constr:cross-channel-graph-sum}}).
21804:channel assignments $\sigma \colon E(\Gamma) \to \{1,\ldots,r\}$:
21816:A single edge has only $r$ channel assignments
21818:mixed-channel assignments on a single-edge graph, so
21876:formula holds at genus~$g$ if and only if every mixed-channel
21883:irrelevant because the other two still kill every mixed-channel
21924:sectors. A mixed-channel graph, by definition, assigns at least
21962:Mechanism~2 alone kills every mixed-channel graph for every
22025:Mixed-channel assignments in the graph sum for $F_g(\cA)$
22055:\label{constr:cross-channel-graph-sum}
22177:a common genus-$0$ vertex, so mixed-channel assignments produce
22333:The four channel assignments $(i,j) \in \{T,W\}^2$:
22368:The $2^3 = 8$ channel assignments.
22470:Its mixed-channel amplitude is nonzero because the two
22471:self-loops can carry different channel assignments.
22527:Construction~\ref{constr:cross-channel-graph-sum},
22586:Construction~\ref{constr:cross-channel-graph-sum} has zero
22772:with all\/ $2^{|E(\Gamma)|}$ channel assignments
 succeeded in 51ms:
 21480	\begin{equation}\label{eq:phi-composite}
 21481	\Phi_{\cA}^{(g,n)}(\alpha)
 21482	\;:=\;
 21483	\sum_{\Gamma \in \mathcal{G}_{g,n}}
 21484	\frac{1}{|\operatorname{Aut}(\Gamma)|}
 21485	\;\iota_{\Gamma,*}\!\Bigl(
 21486	\prod_{e \in E(\Gamma)}
 21487	 P_e(\psi_{e^+}, \psi_{e^-})
 21488	\Bigr)
 21489	\;\otimes\;
 21490	w_\Gamma^{\otimes}(\alpha),
 21491	\end{equation}
 21492	where $w_\Gamma^{\otimes}(\alpha)$ is the \emph{untraced vertex amplitude}:
 21493	at each vertex~$v$, apply the $(g(v),|v|)$-component
 21494	of~$\alpha$; at each internal edge, contract
 21495	via $\eta^{-1} \in \cA \otimes \cA$;
 21496	leave the $n$~external outputs as multilinear functionals on~$\cA$.
 21497	The scalar trace
 21498	$\operatorname{tr}_{\mathrm{cyc}} \colon
 21499	(\cA^*)^{\otimes n}_{\mathrm{cyc}} \to \mathbb{C}$
 succeeded in 51ms:
 22040	% ================================================================
 22041	% THE CROSS-CHANNEL GRAPH CALCULUS
 22042	% ================================================================
 22043	\subsection{The cross-channel graph calculus}
 22044	\label{subsec:cross-channel-graph-calculus}
 22045	\index{cross-channel graph calculus|textbf}
 22046	\index{genus expansion!multi-channel graph sum|textbf}
 22047	
 22048	The per-channel universality of
 22049	Theorem~\ref{thm:multi-weight-genus-expansion}(i) reduces the
 22050	multi-weight genus expansion to a single new object: the
 22051	cross-channel correction
 22052	$\delta F_g^{\mathrm{cross}}(\cA)$.
 22053	
 22054	\begin{construction}[Multi-channel graph sum]
 22055	\label{constr:cross-channel-graph-sum}
 22056	\index{multi-channel graph sum|textbf}
 22057	\index{channel assignment|textbf}
 22058	\index{graph amplitude!multi-channel}
 22059	Let $\cA$ be a modular Koszul chiral algebra of rank~$r$




thinking
**Exploring uniform weights**

I'm thinking about the scenario with uniform-weight generators and how having the same weight doesn’t mean all vertices are identical. The variation in vertices can still occur depending on the channel and the OPE coefficients. It’s interesting to see how these factors interplay even when the generators are uniform in weight. I wonder how significant that variation can be and what practical implications it might have. Let's keep digging into this!
thinking
**Examining generator weight equivalence**

I'm looking into the construction confirming that mixed assignments are based on edge labels. The proof about edge uniformity seems incomplete or invalid. It also suggests that if every strong generator has the same conformal weight, they might represent a single primary line. But I have to question this equivalence since having multiple generators with the same weight doesn't necessarily lead to just one primary line. So, I need to closely inspect definitions in lines 2499-2504 to clarify this.
thinking
**Investigating equal-weight generators**

I'm searching for examples of multiple generators that share the same weight. There might be families of equal-weight generators, but I'm not entirely certain. 

In theorem part (iv), it seems that channels correspond to strong generators, meaning that having equal weights doesn’t simplify the channels. This raises questions about the definition’s equivalence and the uniform-weight condition. If multiple generators with equal weights don’t mean a single channel, it makes the sufficiency argument weaker. I’ll need to ground my findings with the file contents to clarify this issue.
thinking
**Identifying proof gaps**

I need to note that while I didn't find an explicit counterexample in the repository, the logical gap stands out. The definition from lines 2500-2504 states an equivalence, but the construction in lines 22066-22106 defines channels without considering weights. Additionally, lines 21722-21725 mention equal weights to eliminate cross-channel correction. There’s a clear gap since the manuscript doesn’t address the multiplicity of generators. This suggests a hidden assumption: uniform-weight sufficiency likely requires not just equal weights, but effective single-channelity, which is highly relevant and could be critical!
codex
I found a deeper hidden assumption: the manuscript defines the “uniform-weight lane” as “all strong generators have the same conformal weight” and calls that equivalent to a single primary line, but the later cross-channel graph calculus labels channels by generator index, not by weight. I’m checking whether any theorem actually proves that equal weights collapse those multiple channels, because without that the scalar-lane condition is overstated.
exec
/bin/zsh -lc "rg -n \"thm:universal-theta|label\\{thm:universal-theta\\}|Universal MC element|Explicit universal MC class\" chapters/theory/higher_genus_modular_koszul.tex metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4038,4115p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2488,2510p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/claims.jsonl:2839:{"label": "thm:universal-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 3162, "title": "Universal modular Maurer--Cartan class", "refs_in_block": ["thm:master-theta"]}
metadata/claims.jsonl:2845:{"label": "thm:explicit-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 4082, "title": "Explicit universal MC class", "labels_in_block": ["thm:explicit-theta", "eq:theta-minimal", "eq:theta-chain", "eq:theta-genus1", "eq:l2-vanishes", "eq:genus-g-recursion", "eq:theta-generating-function"], "refs_in_block": ["thm:mc2-1-km", "thm:cyclic-rigidity-generic", "thm:algebraic-family-rigidity", "cor:km-minimal-linf", "prop:cyclic-ce-identification", "constr:linf-from-graphs", "thm:family-index"]}
metadata/claims.jsonl:2850:{"label": "prop:mc2-reduction-principle", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 4974, "title": "MC2 reduction principle", "refs_in_block": ["def:cyclic-deformation-bar", "thm:universal-theta"]}
metadata/claims.jsonl:2874:{"label": "thm:mc2-conditional-completion", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 7529, "title": "MC2 completion under explicit hypotheses", "labels_in_block": ["thm:mc2-conditional-completion", "mc2-hyp:cyclic", "mc2-hyp:completion", "mc2-hyp:tautological"], "refs_in_block": ["cor:one-dim-obstruction", "thm:cyclic-linf-graph", "prop:geometric-modular-operadic-mc", "mc2-hyp:cyclic", "thm:tautological-line-support", "thm:universal-theta"]}
metadata/claims.jsonl:2875:{"label": "thm:mc2-full-resolution", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 7614, "title": "MC2 comparison completion on the proved scalar lane", "refs_in_block": ["thm:mc2-conditional-completion", "thm:cyclic-linf-graph", "prop:fay-trisecant", "prop:stokes-regularity-FM", "prop:geometric-modular-operadic-mc", "thm:tautological-line-support", "thm:universal-theta"]}
metadata/claims.jsonl:2876:{"label": "lem:mk67-from-mc2", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 7667, "title": "Bar-intrinsic MC2 identifies MK6--MK7", "refs_in_block": ["rem:extended-axiom-schema", "prop:geometric-modular-operadic-mc", "thm:universal-theta"]}
metadata/claims.jsonl:2893:{"label": "cor:mc2-single-hypothesis", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 9506, "title": "MC2 comparison gauntlet collapses on the proved\nscalar lane", "refs_in_block": ["thm:universal-theta", "thm:mc2-conditional-completion", "mc2-hyp:cyclic", "prop:geometric-modular-operadic-mc", "thm:tautological-line-support"]}
metadata/claims.jsonl:3363:{"label": "prop:scalar-mc-skeleton", "env_type": "proposition", "status": "ProvedHere", "file": "appendices/branch_line_reductions.tex", "line": 175, "title": "The scalar shadow is an abelian MC element", "refs_in_block": ["eq:scalar-mc-skeleton", "thm:universal-theta"]}
chapters/theory/higher_genus_modular_koszul.tex:672:(Theorem~\ref{thm:universal-theta}).
chapters/theory/higher_genus_modular_koszul.tex:2430:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
chapters/theory/higher_genus_modular_koszul.tex:2443: (Theorem~\ref{thm:universal-theta}):
chapters/theory/higher_genus_modular_koszul.tex:2491:and~\ref{thm:universal-theta}).
chapters/theory/higher_genus_modular_koszul.tex:2585:Theorem~\ref{thm:universal-theta}, made unconditional by
chapters/theory/higher_genus_modular_koszul.tex:2604:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
chapters/theory/higher_genus_modular_koszul.tex:3252:\label{thm:universal-theta}
chapters/theory/higher_genus_modular_koszul.tex:3324:Theorem~\ref{thm:universal-theta} extends the canonical twisting
chapters/theory/higher_genus_modular_koszul.tex:4186:\begin{theorem}[Explicit universal MC class;
chapters/theory/higher_genus_modular_koszul.tex:4554:The proof of Theorem~\ref{thm:universal-theta} assembles:
chapters/theory/higher_genus_modular_koszul.tex:5088:Theorem~\ref{thm:universal-theta}. Then:
chapters/theory/higher_genus_modular_koszul.tex:7687:In particular, Theorem~\ref{thm:universal-theta}
 succeeded in 50ms:
  4038	\end{proof}
  4039	
  4040	\begin{remark}[Complementarity as bipartite gauge-fixing]
  4041	\label{rem:mc2-bipartite}
  4042	\index{bipartite gauge-fixing|textbf}
  4043	\index{complementarity!bipartite gauge-fixing}
  4044	The complementarity decomposition
  4045	$\Defcyc(\cA) = L^+_\cA \oplus L^-_\cA$
  4046	of Conjecture~\ref{conj:ambient-complementarity} imposes a
  4047	bipartite constraint on the graph-sum expansion of
  4048	Definition~\ref{def:modular-bar-hamiltonian}: the
  4049	complementarity propagator $P_\cA = H_\cA^{-1}$ is
  4050	off-diagonal in the Lagrangian polarization, so every internal
  4051	edge must run from $L^+$ to~$L^-$. The summation over stable
  4052	graphs automatically restricts to the bipartite subposet
  4053	$\Gamma^{\mathrm{st,bip}}_{g,n}
  4054	\subset \Gamma^{\mathrm{st}}_{g,n}$.
  4055	This bipartite restriction is the chain-level
  4056	expression of Theorem~C: the two dual sides
  4057	interact only through the opposite polarization, and
 succeeded in 50ms:
  2488	by Theorem~\ref{thm:cyclic-linf-graph}, and the MC equation
  2489	is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
  2490	(Theorems~\ref{thm:universal-MC}
  2491	and~\ref{thm:universal-theta}).
  2492	\end{definition}
  2493	
  2494	\begin{definition}[Uniform-weight lane (scalar lane)]
  2495	\label{def:scalar-lane}
  2496	\label{def:uniform-weight-lane}
  2497	\index{scalar lane|textbf}
  2498	\index{uniform-weight lane|see{scalar lane}}
  2499	A modular Koszul chiral algebra~$\cA$ lies on the
  2500	\emph{uniform-weight lane} (or \emph{scalar lane}) if every
  2501	strong generator of~$\cA$ has the same conformal weight.
  2502	Equivalently, $\cA$ has a single primary line in
  2503	$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
  2504	reduces to a one-variable problem.
  2505	Single-generator algebras (Heisenberg, free fermion, Virasoro)
  2506	lie on the scalar lane automatically; multi-generator algebras
  2507	($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.
context compacted

thinking
**Planning file inspection**

I'm dealing with some restrictions and thinking that using the explorer subagent might be good. I need to verify findings with actual file lines, and while a summary could help, my final answer shouldn’t include clickable links. It might be best to reference files in plain text while adding severity headings as bullet points.

I'll ensure I'm checking for genuine discrepancies since false positives could be an issue. So, I need to inspect the files closely for accuracy.
codex
I’ve isolated the theorem surface and its dependency chain. I’m re-checking the exact statement/proof lines and the cited dependencies now so the report only includes findings that survive a second pass.
exec
/bin/zsh -lc "sed -n '1358,1398p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1312,1348p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1878,1985p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '431,470p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
\index{Theorem C!decomposition}
Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
identification, this theorem) produces the ambient complex;
$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
gives the Verdier eigenspace decomposition and its Lagrangian
splitting; $\mathrm{C}_2$
(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
conditional bar-side BV / shifted-symplectic upgrade.
The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
$\sigma$ exchanging the two eigenspaces; at the scalar level
the complementarity formulas below are consequences of the
$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
separate $\mathrm{C}_2$ label:
$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
Table~\ref{tab:complementarity-landscape}).
\end{remark}

 succeeded in 52ms:
\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
\label{thm:verdier-bar-cobar}
\index{Verdier duality!bar-cobar|textbf}
\textup{[Regime: quadratic, genus-$0$
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\mathcal{A}$ be on the Koszul locus and write $\mathcal{A}^!$ for its
Koszul dual.

There is a perfect pairing:
\[\langle \cdot, \cdot \rangle: \bar{B}^{\text{ch}}_n(\mathcal{A}) \otimes 
\Omega^{\text{ch}}_n(\mathcal{A}^!) \to \mathbb{C}\]

given by:
\[\langle \omega_{\text{bar}}, K_{\text{cobar}} \rangle = \int_{\overline{C}_n(X)} 
\omega_{\text{bar}} \wedge \iota^* K_{\text{cobar}}\]

where:
\begin{itemize}
\item $\omega_{\text{bar}} \in \Gamma(\overline{C}_n(X), \mathcal{A}^{\boxtimes n} 
 succeeded in 52ms:
\begin{theorem}[Conditional bar-side BV upgrade of complementarity; \ClaimStatusConditional]
\label{thm:shifted-symplectic-complementarity}
\index{shifted symplectic!(-1)-shifted|textbf}
\index{Lagrangian!complementarity!shifted symplectic|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Assume the conditional BV package of
Theorems~\ref{thm:config-space-bv} and~\ref{thm:bv-functor}. Then the
genus-$1$ complementarity
$Q_1(\mathcal{H}_\kappa) \oplus Q_1(\mathcal{H}_\kappa^!)
\cong H^*(\overline{\mathcal{M}}_1, Z(\mathcal{H}_\kappa))$ that we
computed in~\S\ref{sec:frame-complementarity} admits the following
bar-side $(-1)$-shifted symplectic refinement.
\index{BV algebra!shifted symplectic structure}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
curve $X$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{BV antibracket is $(-1)$-shifted Poisson.}
 The BV bracket $\{-,-\}_{\mathrm{BV}}$ on
 succeeded in 52ms:
\begin{theorem}[Conditional BV functor package; \ClaimStatusConditional]
\label{thm:bv-functor}
\index{BV functor}
Assume the conditional BV package of
Theorem~\ref{thm:config-space-bv} and a Verdier-duality comparison
identifying the dual of the bar coalgebra with a factorization algebra
$\cA^!_\infty$ compatibly with the bracket, coproduct/product, and
differential. Then the assignment
\[\mathrm{BV}: \mathrm{ChirAlg}_X \longrightarrow \mathrm{BV\text{-}Alg}\]
is a lax monoidal functor, and the Verdier dual
$\mathbb{D}_{\operatorname{Ran}}(\bar{B}(\mathcal{A}))$ identifies
with a factorization algebra $\cA^!_\infty$ whose underlying complex
is equivalent to $\bar{B}(\mathcal{A}^!)$
\textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}.
On the Koszul locus, $\cA^!_\infty \simeq \cA^!$.
\end{theorem}

\begin{proof}
Functoriality of the underlying bar construction is standard. The
extra BV functoriality and lax monoidal statements are exactly the
codex
The C2 proof does contain a real bar/cobar switch, so I’m checking whether the later scalar-lane and multi-weight theorems actually justify the claimed “uniform-weight suffices” step or only state it.
exec
/bin/zsh -lc "sed -n '1116,1138p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2494,2524p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{corollary}[Duality for bar complexes; \ClaimStatusProvedHere]
\label{cor:duality-bar-complexes-complete}
The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
\begin{equation}
\langle -, - \rangle: \bar{B}^n(\mathcal{A}) \otimes \bar{B}^n(\mathcal{A}^!) \to 
\mathbb{C}
\end{equation}
where $\mathcal{A}^!$ is the Koszul dual of $\mathcal{A}$.
\end{corollary}

\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
Recall that:
\begin{align}
\bar{B}^n(\mathcal{A}) &= \Gamma(\overline{C}_n(X), \mathcal{A}^{\boxtimes n} \otimes 
\Omega^*_{\log})\\
\bar{B}^n(\mathcal{A}^!) &= \Gamma(\overline{C}_n(X), (\mathcal{A}^!)^{\boxtimes n} 
\otimes \Omega^*_{\log})
\end{align}

By Koszul duality (Definition~\ref{def:koszul-dual-chiral}), there is a natural pairing:
 succeeded in 51ms:
\begin{definition}[Uniform-weight lane (scalar lane)]
\label{def:scalar-lane}
\label{def:uniform-weight-lane}
\index{scalar lane|textbf}
\index{uniform-weight lane|see{scalar lane}}
A modular Koszul chiral algebra~$\cA$ lies on the
\emph{uniform-weight lane} (or \emph{scalar lane}) if every
strong generator of~$\cA$ has the same conformal weight.
Equivalently, $\cA$ has a single primary line in
$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
reduces to a one-variable problem.
Single-generator algebras (Heisenberg, free fermion, Virasoro)
lie on the scalar lane automatically; multi-generator algebras
($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.

On the scalar lane, $\mathrm{obs}_g = \kappa(\cA)\cdot\lambda_g$
is proved at all genera
(Theorem~\ref{thm:genus-universality}).
Off the scalar lane, this identity holds at genus~$1$
universally. For general multi-weight algebras at $g \geq 2$,
exec
/bin/zsh -lc "sed -n '8952,8996p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '22054,22118p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '21681,21852p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Algebraic-family rigidity; \ClaimStatusProvedHere]
\label{thm:algebraic-family-rigidity}
\index{cyclic cohomology!algebraic-family rigidity}
\index{scalar saturation!algebraic-family proof}
\index{Whitehead decomposition!algebraic-family upgrade}
Let $\{{\cA}_k\}_{k \in U}$ be a family of vertex algebras
over a Zariski-open $U \subset \mathbb{C}$ with
$-h^\vee \notin U$, each equipped with simple affine current
subalgebra~$\widehat{\fg}_k$, satisfying:
\begin{enumerate}[label=\textup{(\alph*)}]
\item ${\cA}_k$ is strongly finitely generated over~$\widehat{\fg}_k$
 with the same finite set of primary strong generators
 $\{\varphi_1, \ldots, \varphi_m\}$ for all~$k \in U$;
\item each conformal weight space $({\cA}_k)_h$ is a
 finite-dimensional $\fg$-module, with the same
 $\fg$-representation decomposition for all~$k$;
\item[\textup{(c$'$)}] the OPE structure constants
 $C^k_{ij}(n) := \langle \varphi_i{}_{(n)}\varphi_j \rangle$
 of the primary strong generators are rational functions
 of\/~$k$ on~$U$.
 succeeded in 52ms:
\begin{construction}[Multi-channel graph sum]
\label{constr:cross-channel-graph-sum}
\index{multi-channel graph sum|textbf}
\index{channel assignment|textbf}
\index{graph amplitude!multi-channel}
Let $\cA$ be a modular Koszul chiral algebra of rank~$r$
with diagonal Zamolodchikov metric
$\eta = \operatorname{diag}(\eta_1, \ldots, \eta_r)$.
Fix a genus~$g \geq 2$. For each stable graph
$\Gamma \in \mathcal{G}_{g,0}$ with edge set~$E(\Gamma)$
and vertex set~$V(\Gamma)$, define:

\emph{Channel assignment.}
A function $\sigma \colon E(\Gamma) \to \{1, \ldots, r\}$.
There are $r^{|E(\Gamma)|}$ such assignments.

\emph{Multi-channel amplitude.}
\begin{equation}\label{eq:multi-channel-amplitude}
A_\Gamma(\sigma, \cA)
\;:=\;
 succeeded in 51ms:
\begin{theorem}[Multi-weight genus expansion; \ClaimStatusProvedHere]
\label{thm:multi-weight-genus-expansion}
\label{thm:multi-generator-universality}
\index{multi-generator obstruction!genus expansion|textbf}%
\index{multi-weight genus expansion|textbf}%
\index{cross-channel correction|textbf}%
\index{Faber--Pandharipande formula!multi-weight decomposition}%
\index{genus expansion!multi-channel graph sum}%
Let\/ $\cA$ be a modular Koszul chiral algebra with
strong generators $\varphi_1, \ldots, \varphi_r$ of conformal
weights $h_1, \ldots, h_r$, per-channel modular characteristics
$\kappa_1, \ldots, \kappa_r$
\textup{(}Theorem~\textup{\ref{thm:shadow-channel-decomposition})},
and total modular characteristic\/
$\kappa(\cA) = \sum_{i=1}^r \kappa_i$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Per-channel universality.}
 The diagonal contribution to the genus-$g$ free energy satisfies
 \begin{equation}\label{eq:multi-weight-diagonal}
 F_g^{\mathrm{diag}}(\cA)

thinking
**Inspecting genera and claims**

I need to take a closer look at genus-universality and possibly check out family-index and claims as well. There seems to be a lot to consider here, and it might be useful to understand how they connect. I want to ensure I'm on the right path in exploring these concepts and how they might interact or contribute to whatever larger framework I'm working with. Alright, let's dive in deeper!
codex
I’ve confirmed the multi-weight theorem really outsources its uniform-weight clause to a theorem that explicitly says the needed identification is still open. I’m checking whether that leak propagates into Theorem C’s scalar consequences and whether there’s a genuine circular dependency in the “genus universality” proof.
exec
/bin/zsh -lc "sed -n '5241,5358p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5460,5488p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5998,6025p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
\index{genus universality theorem|textbf}
\textup{[Regime: curved-central on the Koszul locus; all genera
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Let $\cA$ be a modular Koszul chiral algebra whose strong generators
all have the \emph{same} conformal weight. There exists a
genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
curvature, such that \begin{equation}\label{eq:genus-universality}
\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
\quad \text{for all } g \geq 1,
\end{equation}
where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
\textup{(LOCAL)}
Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
For algebras with generators of \emph{several} conformal weights,
the genus-$1$ specialization is unconditional; the higher-genus
extension is conditional on the strong scalar ansatz of
Theorem~\ref{thm:multi-generator-universality}.
exec
/bin/zsh -lc "sed -n '2640,2705p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:family-index|Family index" chapters metadata -S' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
the ``index-theoretic complementarity'': the total genus expansion
of a Koszul pair is a fixed multiple of the
Faber--Pandharipande tautological integral.
\end{enumerate}
\end{theorem}

\begin{proof}
The proof assembles four ingredients, each established
independently.

\emph{Step~1: Construction of $\mathcal{D}_{\cA}^{(g)}$.}
The genus universality theorem
(Theorem~\ref{thm:genus-universality}) establishes for
uniform-weight algebras that the
genus-$g$ obstruction class factors as
$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ in
$H^{2g}(\overline{\mathcal{M}}_g)$, where
$\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
Hodge bundle. This factorization determines
 succeeded in 51ms:
interpretation.
\end{remark}

\begin{remark}[Multi-generator obstruction]\label{rem:multi-generator-obs}
For an algebra with generators of conformal weights $h_1, \ldots, h_r$:
at genus~$1$, $\mathrm{obs}_1 = \kappa \cdot \lambda_1$
\textup{(g=1 only; all-weight at g=1 is unconditional)} with
$\kappa = \sum_i \kappa_{h_i}$, unconditionally
(Theorem~\ref{thm:genus-universality}\textup{(iii)}).
At all genera the \emph{edges} of the genus-$g$ graph sum carry
the standard Hodge bundle $\mathbb{E} = R^0\pi_*\omega$, because
the propagator $\partial_z\log E(z,w)$ is weight~$1$
(Remark~\ref{rem:propagator-weight-universality},
Proposition~\ref{prop:multi-generator-obstruction}(b)).
The full identity $\mathrm{obs}_g = \kappa \cdot \lambda_g$
\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
\emph{fails} at $g \geq 2$ for multi-weight algebras
($\mathcal{W}_N$, $N \geq 3$): the free energy receives a
nonvanishing cross-channel correction
$\delta F_g^{\mathrm{cross}} \neq 0$
 succeeded in 51ms:

\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Universality.}
 \begin{enumerate}[label=\textup{(\alph*)}]
 \item \emph{Cohomological\textup{:}} The genus-$g$ obstruction class
 factors as
 $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$
 in $H^{2g}(\overline{\mathcal{M}}_g)$ for all $g \geq 1$
 \textup{(}uniform-weight; unconditional at $g = 1$\textup{)}.
 \end{enumerate}
 For multi-generator algebras \textup{(}$\mathcal{W}_N$ with
 $N \geq 3$\textup{)}, the genus-$1$ factorization is unconditional,
 while the higher-genus extension remains conditional on the
 strong scalar ansatz
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
\item \emph{Generating function.}
 The genus free energies
 assemble as
 \begin{equation}\label{eq:modular-char-gf}
 \sum_{g=1}^{\infty} F_g(\cA)\, x^{2g}
 succeeded in 50ms:
metadata/dependency_graph.dot:253:  thm_family_index [label="thm:family-index\ntheorem [Pr]\nFamily index theorem for genus expansion...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2010:  thm_guide_family_index [label="thm:guide-family-index\ntheorem [Pr]\nFamily index theorem for genus expansion...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:84:| `thm:guide-family-index` | `theorem` | 241 | Family index theorem for genus expansions |
metadata/theorem_registry.md:2369:| `thm:family-index` | `theorem` | 5769 | Family index theorem for genus expansions |
chapters/examples/heisenberg_eisenstein.tex:1738:confirming Theorem~\ref{thm:family-index} directly from the shadow
metadata/label_index.json:46878:  "thm:family-index": {
chapters/examples/genus_expansions.tex:169:This identification reflects the family index theorem (Theorem~\ref{thm:family-index}): $F_g$ is the GRR pushforward of the Todd class. For general $\kappa$: $\sum_g F_g x^{2g} = \kappa(\mathrm{Td}_{\mathrm{even}}(ix) - 1)$.
chapters/examples/genus_expansions.tex:1904:index theorem (Theorem~\ref{thm:family-index}) shows that
metadata/claims.jsonl:240:{"label": "thm:family-index", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5769, "title": "Family index theorem for genus expansions", "labels_in_block": ["thm:family-index", "eq:modular-deformation-complex-concordance", "eq:family-index-grr", "eq:family-index-generating"], "refs_in_block": ["thm:genus-universality"]}
metadata/claims.jsonl:625:{"label": "prop:thqg-X-free-energy-ahat", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/thqg_fredholm_partition_functions.tex", "line": 1425, "title": "Free energy: $\\hat{A}$-genus verification", "refs_in_block": ["thm:family-index"]}
metadata/claims.jsonl:1941:{"label": "thm:guide-family-index", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/frame/guide_to_main_results.tex", "line": 241, "title": "Family index theorem for genus expansions"}
metadata/claims.jsonl:2728:{"label": "prop:chain-level-curvature-operator", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/higher_genus_foundations.tex", "line": 626, "title": "Chain-level curvature operator", "labels_in_block": ["prop:chain-level-curvature-operator", "eq:chain-curvature-operator", "eq:chern-weil-step1", "eq:chern-weil-projection"], "refs_in_block": ["prop:genus-g-curvature-package", "eq:chain-curvature-operator", "thm:family-index"]}
metadata/claims.jsonl:2803:{"label": "thm:curvature-self-contraction", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_foundations.tex", "line": 6695, "title": "Curvature from loop contraction", "labels_in_block": ["thm:curvature-self-contraction", "eq:self-contraction-trace", "eq:kappa-self-contraction", "eq:qme-genus1"], "refs_in_block": ["thm:quantum-master-equation", "thm:family-index"]}
metadata/claims.jsonl:2845:{"label": "thm:explicit-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 4082, "title": "Explicit universal MC class", "labels_in_block": ["thm:explicit-theta", "eq:theta-minimal", "eq:theta-chain", "eq:theta-genus1", "eq:l2-vanishes", "eq:genus-g-recursion", "eq:theta-generating-function"], "refs_in_block": ["thm:mc2-1-km", "thm:cyclic-rigidity-generic", "thm:algebraic-family-rigidity", "cor:km-minimal-linf", "prop:cyclic-ce-identification", "constr:linf-from-graphs", "thm:family-index"]}
chapters/connections/thqg_fredholm_partition_functions.tex:1449:(Theorem~\textup{\ref{thm:family-index}}).
chapters/connections/editorial_constitution.tex:2579:(Theorem~\ref{thm:family-index}).
chapters/connections/editorial_constitution.tex:2668:5 & Index genus expansions & \textbf{Realized} (Thm~\ref{thm:family-index}) \\
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/bv_brst.tex:1500:\textup{(}Theorem~\ref{thm:family-index}\textup{)},
chapters/connections/concordance.tex:4712:Index & GRR: scalar genus series $= \kappa(\cA) \cdot (\hat{A}(ix) - 1)$; genus-$1$ unconditional & \textbf{Proved} & Thm~\ref{thm:family-index} \\[2pt]

thinking
**Questioning circular proof**

I'm considering the potential circularity between the theorem and concordance summary. I wonder if the family-index is only in the concordance. It might be necessary to inspect the theorem registry line and the actual theorem itself. The claim about the proof of genus-universality citing the family-index could be problematic if it relies on each other. I think I need to read more of the family-index theorem to confirm if it truly depends on genus universality.
codex
The dependency loop looks real rather than rhetorical: the proof of `thm:genus-universality` cites `thm:family-index`, and the proof of `thm:family-index` starts from `thm:genus-universality`. I’m reading the family-index theorem itself to distinguish a true circular proof from a concordance-only summary.
exec
/bin/zsh -lc "sed -n '240,275p' chapters/frame/guide_to_main_results.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5927,6008p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7812,7860p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1500,1530p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{theorem}[Family index theorem for genus expansions;
\ClaimStatusProvedHere]\label{thm:guide-family-index}
\index{index theorem!modular deformation|textbf}
\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
\overline{\mathcal{M}}_g$ be the universal curve with relative
dualizing sheaf~$\omega_\pi$, and let
$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
The following holds for uniform-weight modular Koszul algebras
at all genera; the genus-$1$ statements are unconditional for
all families.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{GRR formula.}
For uniform-weight algebras, the genus-$g$ free energy is the
GRR pushforward:
\[
F_g(\cA)
\;=\;
\kappa(\cA) \cdot
 succeeded in 51ms:
\begin{theorem}[Family index theorem for genus expansions;
\ClaimStatusProvedHere]\label{thm:family-index}
\index{index theorem!modular deformation|textbf}
\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
\overline{\mathcal{M}}_g$ be the universal curve with relative
dualizing sheaf~$\omega_\pi$, and let
$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
The following holds for uniform-weight modular Koszul algebras
at all genera; the genus-$1$ statements are unconditional for
all families, including multi-generator.
Define the \emph{modular deformation complex} of~$\cA$ at genus~$g$ by
\begin{equation}\label{eq:modular-deformation-complex-concordance}
\mathcal{D}_{\cA}^{(g)}
\;:=\;
\kappa(\cA) \cdot \mathbb{E}
\;\in\; K_0(\overline{\mathcal{M}}_g) \otimes_{\mathbb{Z}} \mathbb{Q},
\end{equation}
the $K$-theory class given by $\kappa(\cA)$ copies of the
 succeeded in 51ms:
\begin{corollary}[One-channel line concentration of the minimal MC
class;
\ClaimStatusProvedHere]
\label{cor:scalar-saturation}
\index{universal Maurer--Cartan class!scalar saturation}
\index{universal Maurer--Cartan class!scalar exactness}
For any Koszul chiral algebra~$\cA$ with simple Lie
symmetry~$\mathfrak{g}$ satisfying
$\dim H^2_{\mathrm{cyc}}(\cA,\cA) = 1$, the universal MC element
has minimal projection concentrated on a single cyclic line:
\[
\Theta_{\cA}^{\min} = \eta \otimes \Gamma_{\cA}
\qquad
\text{for a unique }\Gamma_{\cA}\in\widehat{\Gmod}.
\]
On the proved uniform-weight lane one further has
\[
\Gamma_{\cA} = \kappa(\cA)\Lambda,
\qquad
\Theta_{\cA}^{\min}
 succeeded in 51ms:
\textup{(}Theorem~\ref{thm:family-index}\textup{)},
where $\hat{A}(x) = (x/2)/\sinh(x/2)$.

\emph{Step~4} \textup{(}Faber--Pandharipande\textup{)}.
The intersection number
\[
\int_{\overline{\mathcal{M}}_{g,1}}
\psi^{2g-2}\,\lambda_g
= \lambda_g^{\mathrm{FP}}
= \frac{2^{2g-1}-1}{2^{2g-1}}
\cdot \frac{|B_{2g}|}{(2g)!}
\]
is the Faber--Pandharipande formula~\cite{FP00}.
Combining Steps~1--4:
$F_g^{\mathrm{BV}}(\cH_\kappa)
= \kappa \cdot \lambda_g^{\mathrm{FP}}
= F_g^{\mathrm{bar}}(\cH_\kappa)$.
\index{Quillen metric!BV/bar proof|)}

\medskip

thinking
**Exploring theorem justification**

I need to understand if the theorem about multi-weight genus expansion can be justified by something other than the algorithm family rigidity. Maybe considering the uniform-weight lane along with the genus universality theorem is a path to explore. However, the theorem specifically cites algorithm family rigidity, which makes me think the focus should be on mis-citation and any unproved steps. I should inspect the proof related to "proved uniform-weight lane" for further insights.
codex
I’m checking whether the repo proves the missing scalar identification somewhere else under a different label. If it does, the issue drops from “false theorem step” to “bad citation”; if it does not, the uniform-weight clause remains unsupported.
exec
/bin/zsh -lc "sed -n '7860,7925p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Gamma_\\\\{\\\\cA\\\\}|\\\\Gamma_\\\\{\\\\{\\\\cA\\\\}_k\\\\}|tautological-purity|kappa\\\\(\\\\cA\\\\)\\\\Lambda|strong scalar ansatz\" chapters/theory chapters/connections chapters/frame -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "uniform-weight lane|scalar lane|single primary line|one-variable problem" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex -S' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:Gamma_\{\cA\}|\Gamma_\{\{\cA\}_k\}|tautological-purity|kappa\(\cA\)\Lambda|strong scalar ansatz)
               ^^
error: unrecognized escape sequence
 succeeded in 52ms:
$l_1^{\mathrm{tr}} = 0$ by minimality.
This proves the one-line concentration statement.
On the proved uniform-weight lane,
Theorem~\ref{thm:genus-universality} identifies the scalar trace
with $\kappa(\cA)\Lambda$, forcing
$\Gamma_{\cA} = \kappa(\cA)\Lambda$ there.
\end{proof}

\begin{remark}[One-channel line concentration and the Casimir
spectrum]
\label{rem:scalar-saturation-casimirs}
\index{universal Maurer--Cartan class!Casimir spectrum}
\index{cubic Casimir!does not contribute to $\Theta$}
Higher Casimirs ($C_3, C_4, \ldots$) do not contribute to
the degree-$2$ minimal line $\eta\otimes\Gamma_{\cA}$:
they live in $H^{2k}_{\mathrm{cyc}}$ for
$k\geq 2$, which is the wrong degree for the MC equation.
Since $H^2_{\mathrm{cyc}}(\mathfrak{g},\mathfrak{g})\cong
H^3(\mathfrak{g})\cong\mathbb{C}$, the minimal degree-$2$
direction is one-dimensional.
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:193:function of these classes on the uniform-weight scalar lane is $\kappa(\cA) \cdot (\hat{A}(i\hbar) - 1)$
chapters/theory/higher_genus_foundations.tex:251: On the uniform-weight scalar lane, the cohomological curvature
chapters/theory/higher_genus_foundations.tex:599: The generating function on the uniform-weight lane is \begin{equation}\label{eq:family-index-package}
chapters/theory/higher_genus_foundations.tex:5302:On the scalar lane (Definition~\ref{def:scalar-lane}), the genus-$g$ free energy is $F_g = \kappa \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$,
chapters/theory/higher_genus_foundations.tex:5323:On the uniform-weight lane, every edge of the genus-$g$ graph sum
chapters/theory/higher_genus_foundations.tex:5813:In particular, on the proved scalar lane,
chapters/theory/higher_genus_foundations.tex:5857:On the proved scalar lane, these equivalent conditions further imply
chapters/theory/higher_genus_foundations.tex:5878:on the proved scalar lane. The final assertion follows: with
chapters/theory/higher_genus_foundations.tex:5883:\begin{corollary}[Tautological class map on the scalar lane; universal genus-$1$ class; \ClaimStatusProvedHere]\label{cor:tautological-class-map}
chapters/theory/higher_genus_foundations.tex:5892:On the proved scalar lane, one also has
chapters/theory/higher_genus_foundations.tex:5916:is Theorem~\ref{thm:genus-universality}; on the proved scalar lane,
chapters/theory/higher_genus_foundations.tex:5939:on the proved scalar lane a one-parameter family of classes
chapters/theory/higher_genus_foundations.tex:5976:(Theorem~\ref{thm:genus-universality}). On the proved scalar lane,
chapters/theory/higher_genus_foundations.tex:5993:$R^*(\overline{\mathcal{M}}_g)$. On the proved scalar lane, collapse
chapters/theory/higher_genus_foundations.tex:6186:On the proved scalar lane, the factorization
chapters/theory/higher_genus_foundations.tex:6203:A modular Koszul chiral algebra $\cA$ on the proved scalar lane lifts
chapters/theory/higher_genus_foundations.tex:6212: genera on the proved scalar lane.
chapters/theory/higher_genus_foundations.tex:6221:On the proved scalar lane, Theorem~\ref{thm:genus-universality} gives
chapters/theory/higher_genus_foundations.tex:6225:$\mathrm{obs}_g = 0$ for all $g$ on that scalar lane. For arbitrary
chapters/theory/higher_genus_foundations.tex:6239:universal genus-$1$ scalar term and, on the proved scalar lane, all

thinking
**Evaluating regex parse failure**

I’m considering the failed regex parse issue. It might not be absolutely necessary, but I could check around lines 9408 to see if there are any remarks regarding one-dimensionality or Gamma identification. I wonder if there’s an unresolved issue that I can find? Maybe I should search for the string “tautological purity” instead, as that might lead to a simpler understanding of the problem. It feels like there's more to uncover here!
codex
There is already language elsewhere in the chapter admitting a gap between “one-dimensional primitive direction” and “the coefficient is exactly `\kappa\Lambda`.” I’m locating that admission so the report cites the manuscript against itself, not just one theorem against another.
exec
/bin/zsh -lc "rg -n \"tautological-purity|tautological purity|kappa\\\\(\\\\cA\\\\)\\\\Lambda|strong scalar ansatz|scalar-saturated families|one-channelity alone|does not force the full universal MC class\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9388,9438p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '14414,14458p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '14032,14062p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:tautological-purity|tautological purity|kappa\(\cA\)\Lambda|strong scalar ansatz|scalar-saturated families|one-channelity alone|does not force the full universal MC class)
                                                      ^^
error: unrecognized escape sequence
 succeeded in 52ms:
\;\xrightarrow{\;d + [\Theta_\cA, -]\;}
\nabla_\cA
\;\xrightarrow{\;\text{integrable affine }H^0\;}
\text{conformal blocks}.
\]
The genus-zero OPE data $\mathfrak{K}_\cA^{(0)}$ and the
propagator $P_\cA$ determine all higher-genus corrections via
the primitive master equation.
On the proved uniform-weight scalar lane, the genus-$g$ free
energy is the Feynman amplitude sum
$F_g = \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$
(Theorem~\ref{thm:conformal-block-reconstruction}); for arbitrary
modular Koszul algebras, the unconditional scalar specialization is
the genus-$1$ identity $F_1 = \kappa(\cA)/24$.
\end{remark}

\begin{conjecture}[Determinant-line half-form]
\label{conj:conformal-block-half-form}
\ClaimStatusConjectured
\index{determinant line!half-form conjecture}
 succeeded in 52ms:
\begin{theorem}[Direct derivation on the proved scalar lane;
\ClaimStatusProvedHere]
\label{thm:theta-direct-derivation}
\index{Theta@$\Theta_\cA$!direct derivation}
For a modular Koszul chiral algebra~$\cA$ on the proved
uniform-weight lane with one-channel cyclic deformation complex
\textup{(}$\dim H^2(\Defcyc(\cA), l_1) = 1$ at each genus\textup{)},
the minimal Maurer--Cartan class is
\begin{equation}\label{eq:theta-explicit-direct}
\Theta_{\cA}^{\min}
\;=\;
\kappa(\cA) \cdot \eta \otimes \Lambda,
\qquad
\Lambda = \sum_{g \geq 1} \lambda_g,
\end{equation}
where $\eta$ is the unique degree-$1$ generator of the
one-dimensional obstruction space and $\lambda_g$ the
Faber--Pandharipande tautological class. This is a statement
about the minimal scalar package; the chain-level
element $D_\cA-\dzero$ may still retain nontrivial higher-degree
 succeeded in 52ms:
effective-\(\Gamma\)-quadruple form
(Corollary~\ref{cor:effective-quadruple}).
The algebraic-family theorem subsumes the generic-level result
and extends it to admissible parameter values only for the
already verified algebraic-family objects in the standard
Lie-theoretic landscape \textup{(}not for the live audit surface
of simple admissible quotients\textup{)}.
What remains open outside the proved uniform-weight scalar lane is
the tautological-purity step
$\Gamma_i(\cA)=\kappa_i(\cA)\Lambda$,
even when the cyclic direction is already known to be
one-dimensional.
The testable criterion is $\dim H^2_{\mathrm{cyc}} = 1$
(Proposition~\ref{prop:saturation-equivalence}).
The sharpest potential counterexample, 4D $\mathcal{N}=2$
quiver VOAs with multi-dimensional conformal manifolds,
has so far produced only single-parameter dependence in all
computed cases, and in every tested instance satisfies~(c$'$).
Theorem~D establishes that $\kappa$ exists as a universal
invariant; the quadruple reduction strengthens this to the

thinking
**Investigating regex failure**

I'm noticing a regex escaping failure, but other outputs seem enough for now. I’m wondering if I need to check if scalar-lane equivalence is truly contradicted by known multi-generator examples with the same weights. I think I might explore if beta-gamma weights need to be equal and whether equal weights plus multiple generators can coexist.

Theorem mentions things generally, but I realize that same weights don’t automatically mean a single primary line exists. I might need to look for proof of equivalence, so searching for "single primary line" references could help.
codex
I’ve verified the repo repeatedly uses the stronger statement “uniform weight implies scalar saturation,” but the local definitions of channels and graph assignments are indexed by generator/channel, not weight. I’m checking whether the manuscript ever proves that equivalence, or just asserts it.
exec
/bin/zsh -lc "sed -n '20952,20992p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17640,17732p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"single primary line|one-variable problem|uniform-weight.*equival|Equivalently, \\\\cA has a single primary line|proved scalar lane\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Neither the quantization nor the Schr\"odinger
equation is established here; the connection between the
genus spectral sequence
(Construction~\ref{const:vol1-genus-spectral-sequence}) and
the Hamilton--Jacobi structure remains a
structural analogy.
\end{remark}

\begin{remark}[Reduction to the Riccati equation]
\label{rem:hj-riccati-reduction}
\index{Hamilton--Jacobi equation!Riccati reduction}
\index{Riccati equation!Hamilton--Jacobi reduction}
On a single primary line $L_i$
\textup{(}$x_j = 0$ for $j \neq i$\textup{)},
the multi-channel Hamilton--Jacobi
equation~\eqref{eq:shadow-hamilton-jacobi}
reduces to the single-channel Riccati equation
of Theorem~\textup{\ref{thm:riccati-algebraicity}},
provided the transverse gradients vanish:
$(\partial U / \partial x_j)|_{x_j = 0} = 0$
 exited 2 in 52ms:
rg: regex parse error:
    (?:single primary line|one-variable problem|uniform-weight.*equival|Equivalently, \cA has a single primary line|proved scalar lane)
                                                                                      ^^
error: unrecognized escape sequence
 succeeded in 52ms:

The construction is sharpest for algebras at rational~$c$
where $h(D_0) = 1$: then the Epstein zeta factors completely
through a single Dedekind zeta function and produces an explicit
Dirichlet $L$-function $L(s, \chi_d)$.
For $h(D_0) > 1$, the Epstein zeta depends on the
\emph{specific ideal class} represented by $Q_L$, not merely on
the field~$K_L$. The sum over all $h(D_0)$ classes in the
discriminant gives $(2/w)\zeta_{K_L}(s)$, but the single form
$Q_L$ carries finer information.
Whether the shadow metric always selects the principal class
is recorded as
Conjecture~\textup{\ref{conj:shadow-principal-class}}
in Chapter~\textup{\ref{chap:arithmetic-shadows}}.
\end{remark}

% ====================================================================
\subsection{The clutching closure programme}
\label{subsec:clutching-closure-programme}
\index{clutching closure programme|textbf}

thinking
**Searching String Issues**

I'm noticing that the regex search failed due to the escape sequence issue. I could try searching for simple strings individually. However, it feels like we've already defined and constructed enough for our needs. Maybe we don't really need to work through theorem proving equivalence? Still, I should consider searching for something like “single primary line” in relation to simple strings. That could help clarify things!
exec
/bin/zsh -lc 'rg -n "single primary line" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "strong scalar ansatz" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "one-variable problem" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2653: strong scalar ansatz
chapters/theory/higher_genus_modular_koszul.tex:2699:strong scalar ansatz of
chapters/theory/higher_genus_foundations.tex:5259:extension is conditional on the strong scalar ansatz of
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:2502:Equivalently, $\cA$ has a single primary line in
chapters/theory/higher_genus_modular_koszul.tex:17665:invariant: it lives on a single primary line and sees only local OPE data.
chapters/theory/higher_genus_modular_koszul.tex:17719:single primary line: it strips the lower-degree (cubic)
chapters/theory/higher_genus_modular_koszul.tex:20964:On a single primary line $L_i$
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2504:reduces to a one-variable problem.



thinking
**Auditing theorem details**

I’m investigating the stale wording in the theorem status labels to ensure it's an actual bug and not just outdated phrasing. It suggests that the extension is contingent on a now-proved negative scalar ansatz, which seems misleading. I might need to update the label for "thm:multi-generator-universality" to reflect its current status clearly. I’ll also check for duplicates of "strong scalar ansatz," with three identified occurrences, and explore potential propagation issues that may provide useful insights.
thinking
**Analyzing proof steps**

I’m considering citing both the first and second parts since it might be enough. I should check if the proof of C2 correctly justifies the Verdier involution's anti-commutation with the Lie bracket based on the cited proposition about Lagrangian eigenspaces. I found at least one critical flaw in part i, so I need to evaluate parts ii and iii as well. It seems there might be issues with how part ii uses the Kontsevich--Pridham correspondence. I’ll inspect the sources and confirm the cited proposition has been proved, ensuring there are no false positives.
thinking
**Inspecting proposition citation**

Since the user requested every step, I need to take a closer look at the citation in part iii to confirm that the proposition actually exists. I’ll search the lines around the proposition to ensure it's valid. This way, I can make sure I’m providing accurate information and fully supporting my claims. Being thorough is important, especially since the user is looking for detailed verification at each step!
codex
I have enough to show the scalar condition is not cleanly supported, but I’m checking the remaining cited proposition in Part (iii) so I don’t overstate the case. If that step is sound, the report will isolate the failure to Part (i) and the scalar-lane prerequisites instead of flagging the whole theorem indiscriminately.
exec
/bin/zsh -lc "sed -n '1718,1768p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:lagrangian-eigenspaces|lagrangian eigenspaces" chapters/theory/higher_genus_complementarity.tex chapters -S' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:multi-generator-obstruction|multi-generator obstruction" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex -S' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\cA$ with trivial center, $\dim Q_2(\cA) + \dim Q_2(\cA^!) = 8$.
Detailed genus-$2$ complementarity dimensions are verified in
Part~\ref{part:characteristic-datum} (\S\ref{subsec:genus2-complementarity-verification}).
\end{proof}

This completes Step~III. Combining Steps~7--10, we have shown:
\begin{enumerate}
\item Kodaira--Spencer map via Gauss--Manin connection (Step 7), with anti-commutativity
$\mathbb{D} \circ \nabla_{\kappa(v)}^z = -\nabla_{\kappa(v)}^z \circ \mathbb{D}$
\item Verdier involution $\sigma$ with $\sigma^2 = \mathrm{id}$ (Step 8)
\item Direct sum: $Q_g(\mathcal{A}) \cap Q_g(\mathcal{A}^!) = 0$ as eigenspaces of
$\sigma$ (Step 9)
\item Exhaustion: $Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) = H^*(\overline{
\mathcal{M}}_g, Z(\mathcal{A}))$ because $\sigma^2 = \mathrm{id}$ (Step 10)
\end{enumerate}

Therefore:
\begin{equation}
Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g,
Z(\mathcal{A}))
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:5121:(Proposition~\ref{prop:multi-generator-obstruction}\textup{(a)}),
chapters/theory/higher_genus_foundations.tex:5341:(Proposition~\ref{prop:multi-generator-obstruction}).
chapters/theory/higher_genus_foundations.tex:5463:\begin{remark}[Multi-generator obstruction]\label{rem:multi-generator-obs}
chapters/theory/higher_genus_foundations.tex:5473:Proposition~\ref{prop:multi-generator-obstruction}(b)).
chapters/theory/higher_genus_foundations.tex:5494:\index{multi-generator obstruction!resolution|textbf}%
chapters/theory/higher_genus_foundations.tex:5570:\index{multi-generator obstruction!structural diagnosis}%
chapters/theory/higher_genus_foundations.tex:5655:\label{prop:multi-generator-obstruction}
chapters/theory/higher_genus_foundations.tex:5656:\index{multi-generator obstruction}
chapters/theory/higher_genus_foundations.tex:5704:\index{multi-generator obstruction!quartic dependence}%
chapters/theory/higher_genus_foundations.tex:5730:\index{multi-generator obstruction!multi-channel resolution}%
chapters/theory/higher_genus_modular_koszul.tex:21684:\index{multi-generator obstruction!genus expansion|textbf}%
chapters/theory/higher_genus_modular_koszul.tex:22005:\index{multi-generator obstruction!resolution}%
 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:1780:Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
chapters/theory/higher_genus_complementarity.tex:1783:\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:1784:\label{prop:lagrangian-eigenspaces}
chapters/theory/higher_genus_complementarity.tex:1869:Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
chapters/theory/higher_genus_complementarity.tex:1978:Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
chapters/theory/higher_genus_complementarity.tex:2027:(Proposition~\ref{prop:lagrangian-eigenspaces}(i)) is a
chapters/theory/higher_genus_complementarity.tex:2044: Proposition~\ref{prop:lagrangian-eigenspaces}(iii):
chapters/theory/higher_genus_modular_koszul.tex:5399:$\sigma$ as in Proposition~\ref{prop:lagrangian-eigenspaces}. Let
chapters/theory/higher_genus_modular_koszul.tex:5438:By Proposition~\ref{prop:lagrangian-eigenspaces}, both lines are
chapters/theory/higher_genus_modular_koszul.tex:5450:Again by Proposition~\ref{prop:lagrangian-eigenspaces}, the pairing
chapters/theory/higher_genus_modular_koszul.tex:5681:Proposition~\ref{prop:lagrangian-eigenspaces}. Condition~\textup{(iii)}
chapters/connections/holographic_codes_koszul.tex:130: \textup{(}Proposition~\textup{\ref{prop:lagrangian-eigenspaces}(iii)}\textup{)},
chapters/connections/holographic_codes_koszul.tex:175:Proposition~\ref{prop:lagrangian-eigenspaces}(ii)).
chapters/theory/higher_genus_complementarity.tex:1780:Verdier pairing of Proposition~\ref{prop:lagrangian-eigenspaces}.
chapters/theory/higher_genus_complementarity.tex:1783:\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:1784:\label{prop:lagrangian-eigenspaces}
chapters/theory/higher_genus_complementarity.tex:1869:Proposition~\ref{prop:lagrangian-eigenspaces} establishes the
chapters/theory/higher_genus_complementarity.tex:1978:Proposition~\ref{prop:lagrangian-eigenspaces}(iii), the
chapters/theory/higher_genus_complementarity.tex:2027:(Proposition~\ref{prop:lagrangian-eigenspaces}(i)) is a
chapters/theory/higher_genus_complementarity.tex:2044: Proposition~\ref{prop:lagrangian-eigenspaces}(iii):
exec
/bin/zsh -lc "sed -n '1783,1848p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
\label{prop:lagrangian-eigenspaces}
\index{Lagrangian!eigenspaces|textbf}
\index{Verdier duality!pairing on moduli}
Let $(\cA, \cA^!)$ be a chiral Koszul pair and let
$V = H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
 induces a non-degenerate bilinear pairing
 \[
 \langle -, - \rangle_{\mathbb{D}} \colon V \otimes V \to \mathbb{C}
 \]
 of cohomological degree $-(3g-3)$ \textup{(}the shift coming from
 $\dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 3g-3$\textup{)}.
\item The Verdier involution $\sigma$ is an \emph{anti-involution}
 for this pairing:
 $\langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}} = -\langle v, w \rangle_{\mathbb{D}}$
 for all $v, w \in V$.
\item Consequently, the eigenspaces
 $V^+ = Q_g(\cA)$ and $V^- = Q_g(\cA^!)$
exec
/bin/zsh -lc "sed -n '5655,5702p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{prop:multi-generator-obstruction}
\index{multi-generator obstruction}
Let $\cA$ be a modular Koszul chiral algebra with strong generators
of conformal weights $h_1, \ldots, h_r$.
\begin{enumerate}[label=\textup{(\alph*)}]
\item At genus~$1$,
$\mathrm{obs}_1(\cA) = \kappa(\cA) \cdot \lambda_1$
\textup{(g=1 only; all-weight at g=1 is unconditional)}
with $\kappa = \sum_i \kappa_{h_i}$.
\item Every edge of the genus-$g$ graph sum carries the standard
Hodge bundle $\mathbb{E} = R^0\pi_*\omega$
\textup{(}Remark~\textup{\ref{rem:propagator-weight-universality}}\textup{)}.
\item Scalar saturation fixes the $H^2_{\mathrm{cyc}}$ direction
to~$\eta$, but the Kuranishi map vanishes by parity, so the
MC equation does not determine which class in
$H^*(\overline{\mathcal{M}}_g)$ appears at genus~$g$.
The identity $\mathrm{obs}_g = \kappa \cdot \lambda_g$
\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
\emph{fails}
at $g \geq 2$ for multi-weight algebras: the free energy receives
codex
There is a second possible leak: Part (iii) of C2 cites a proposition about cohomology of the center on moduli, but C2 needs a statement about the bar-side dg Lie algebra `L_g`. I’m checking whether the manuscript actually lifts that involution/polarization to `L_g`, or only at the center-cohomology level.
exec
/bin/zsh -lc "rg -n \"induces an involution on L_g|L_g\\"'^'"\\+|L_g\\"'^'"\\-|bar-side eigenspaces|Verdier involution.*L_g|sigma.*L_g|Lagrangian subspaces\" chapters/theory/higher_genus_complementarity.tex chapters/connections/bv_brst.tex chapters/theory/higher_genus_modular_koszul.tex -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2020,2050p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "shifted symplectic.*Lagrangian|(-1)-shifted symplectic form|anti-commutes with the Lie bracket" chapters/theory/higher_genus_complementarity.tex chapters/connections/bv_brst.tex -S' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
carries an $n$-shifted symplectic structure: the pairing defines a
constant $2$-form of degree~$n$ on $\mathbf{V}$, and the closure
condition $d_{\mathrm{dR}}\omega = 0$ is automatic for a constant
form on a linear space~\cite[Example~1.4]{PTVV13}.
Non-degeneracy of the pairing translates to non-degeneracy of the
$2$-form.
The Verdier pairing on $C_g$
(Proposition~\ref{prop:lagrangian-eigenspaces}(i)) is a
non-degenerate symmetric pairing of degree $-(3g{-}3)$, so $C_g$
carries a $(-(3g{-}3))$-shifted symplectic structure.

\emph{PTVV Lagrangian conditions.}
A \emph{Lagrangian} in a linear $n$-shifted symplectic space
$(V, \omega)$ is a subcomplex $L \hookrightarrow V$
satisfying~\cite[Definition~2.8]{PTVV13}:
\begin{enumerate}[label=(\alph*)]
\item \emph{Isotropy:} $\omega|_L = 0$ (the pairing restricts to
 zero on $L$).
\item \emph{Non-degeneracy:} the induced map
 $L \to (V/L)^{\vee}[n]$ is a quasi-isomorphism.
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:80: $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
chapters/theory/higher_genus_complementarity.tex:1922: The Verdier involution induces an involution on~$L_g$, and the
chapters/theory/higher_genus_complementarity.tex:1923: eigenspace decomposition $L_g = L_g^+ \oplus L_g^-$ provides
chapters/theory/higher_genus_complementarity.tex:1924: complementary Lagrangian subspaces, with $L_g^+$ controlling
chapters/theory/higher_genus_complementarity.tex:1925: deformations of~$\cA$ and $L_g^-$ controlling deformations
chapters/theory/higher_genus_complementarity.tex:1970:The Verdier involution~$\sigma$ induces an involution on~$L_g$ that
chapters/theory/higher_genus_complementarity.tex:1979:$\sigma$-eigenspaces $L_g^+$ and $L_g^-$ are isotropic for the
chapters/theory/higher_genus_complementarity.tex:1981:Lagrangian) because $L_g = L_g^+ \oplus L_g^-$ over a field of
chapters/theory/higher_genus_complementarity.tex:5155:$\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces of this phase space,
 succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:1971:anti-commutes with the Lie bracket:


thinking
**Investigating theorem C2 proof**

I need to check if part (ii) of theorem C2 uses pairing from the bar-cobar construction for invariant pairing on L_g. It's a bit tricky since the invariance deduced comes from the BV Leibniz rule, and I’m not sure if it’s conditionally valid. I'll also verify if `Theorem\ref{thm:config-space-bv}` provides proof of bracket degree. I should look for a possible "scalar BV pairing" theorem elsewhere. It turns out that the requested theorem C2 might be conditional, which is important.
thinking
**Searching for theorem C2**

The user asked specifically about the theorem C2 scalar BV pairing, and it seems that the live manuscript actually refutes that premise, which is quite useful information. I’m wondering if there might be an actual theorem mentioned in the guide or framework regarding C2. So, I’ll search quickly for “C2” or “scalar BV pairing” to see what comes up. This could provide me with more clarity on the topic.
codex
I’ve verified a second object-level mismatch in Part (iii): the cited Lagrangian proposition is about the center cohomology `C_g`, not the bar-side dg Lie algebra `L_g`. I’m doing one last sweep for any theorem explicitly labeled as “C2 scalar BV pairing”; if none exists, the report will state that the live manuscript has already reassigned C2.
exec
/bin/zsh -lc "rg -n \"Theorem~C has three named pieces|scalar-level formulas below are consequences|not a separate \\\\mathrm\\{C\\}_2 label\" chapters/theory/higher_genus_complementarity.tex chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex -S" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "scalar BV pairing|Theorem C2|C_2|bar-side BV|uniform-weight.*BV|BV pairing" chapters metadata -S' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:Theorem~C has three named pieces|scalar-level formulas below are consequences|not a separate \mathrm\{C\}_2 label)
                                                                                                    ^^
error: unrecognized escape sequence
 succeeded in 51ms:
Total output lines: 243

chapters/examples/deformation_quantization.tex:289:\[w = \int_{C_2^{\text{ch}}(X)} d\arg(z_2 - z_1) = \frac{1}{2}\]
chapters/examples/deformation_quantization.tex:308:Weight: $w_{\Gamma_1} = \frac{1}{8}$ (computed via the Kontsevich configuration space integral on $C_2(\mathfrak{H})$)
chapters/examples/deformation_quantization.tex:849:\int_{C_2(\mathfrak{H})} d\phi(z_1,q_1) \wedge d\phi(z_1,q_1)
chapters/examples/deformation_quantization.tex:877:\int_{C_2(\mathfrak{H})}
metadata/dependency_graph.dot:1481:  prop_wp_c2_cofinite [label="prop:wp-c2-cofinite\nproposition [Pr]\n$C_2$-cofiniteness of $\cW(p)$", style=filled, fillcolor="#bbdefb"];
metadata/dependency_graph.dot:2767:  thm_shifted_symplectic_complementarity [label="thm:shifted-symplectic-complementarity\ntheorem [Co]\nConditional bar-side BV upgrade of compl...", style=filled, fillcolor="#e1bee7"];
metadata/dependency_graph.dot:3292:  conj_koszul_c2_duality [label="conj:koszul-c2-duality\nconjecture [Co]\nKoszul--$C_2$ duality", style=filled, fillcolor="#fff9c4"];
chapters/examples/lattice_foundations.tex:3385:$Q_i^2 = \oint_{C_2}\oint_{C_1}
chapters/examples/logarithmic_w_algebras.tex:15:Zhu's $C_2$-cofiniteness condition holds, the algebra has finitely
chapters/examples/logarithmic_w_algebras.tex:24:prototypical $C_2$-cofinite non-rational vertex algebra. It has four
chapters/examples/logarithmic_w_algebras.tex:260:% Section 3: C_2-cofiniteness and the bar complex
chapters/examples/logarithmic_w_algebras.tex:263:\section{$C_2$-cofiniteness and the bar complex}
chapters/examples/logarithmic_w_algebras.tex:266:The $C_2$-cofiniteness condition
chapters/examples/logarithmic_w_algebras.tex:267:$\dim(\cA / C_2(\cA)) < \infty$
chapters/examples/logarithmic_w_algebras.tex:271:$R_\cA = \cA / C_2(\cA)$ is Zhu's $C_2$-algebra.
chapters/examples/logarithmic_w_algebras.tex:272:For $C_2$-cofinite algebras, $X_\cA = \{0\}$: the associated
chapters/examples/logarithmic_w_algebras.tex:275:\begin{proposition}[$C_2$-cofiniteness of $\cW(p)$;
chapters/examples/logarithmic_w_algebras.tex:277:\index{triplet algebra!$C_2$-cofiniteness}
codex
I’ve narrowed the report to six genuine issues. I’m pulling exact numbered lines now so the final audit cites only the live locations that support each finding.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1318,1334p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1360,1378p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1116,1128p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1896,1983p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1783,1838p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1318	Let $\mathcal{A}$ be on the Koszul locus and write $\mathcal{A}^!$ for its
  1319	Koszul dual.
  1320	
  1321	There is a perfect pairing:
  1322	\[\langle \cdot, \cdot \rangle: \bar{B}^{\text{ch}}_n(\mathcal{A}) \otimes 
  1323	\Omega^{\text{ch}}_n(\mathcal{A}^!) \to \mathbb{C}\]
  1324	
  1325	given by:
  1326	\[\langle \omega_{\text{bar}}, K_{\text{cobar}} \rangle = \int_{\overline{C}_n(X)} 
  1327	\omega_{\text{bar}} \wedge \iota^* K_{\text{cobar}}\]
  1328	
  1329	where:
  1330	\begin{itemize}
  1331	\item $\omega_{\text{bar}} \in \Gamma(\overline{C}_n(X), \mathcal{A}^{\boxtimes n} 
  1332	\otimes \Omega^*_{\log})$ is a bar element (logarithmic form on compactified space)
  1333	\item $K_{\text{cobar}} \in \mathcal{D}'(C_n(X), (\mathcal{A}^!)^{\boxtimes n})$ is 
  1334		a cobar element (distribution on open space)
 succeeded in 52ms:
  1116	\begin{corollary}[Duality for bar complexes; \ClaimStatusProvedHere]
  1117	\label{cor:duality-bar-complexes-complete}
  1118	The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
  1119	\begin{equation}
  1120	\langle -, - \rangle: \bar{B}^n(\mathcal{A}) \otimes \bar{B}^n(\mathcal{A}^!) \to 
  1121	\mathbb{C}
  1122	\end{equation}
  1123	where $\mathcal{A}^!$ is the Koszul dual of $\mathcal{A}$.
  1124	\end{corollary}
  1125	
  1126	\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
  1127	Recall that:
  1128	\begin{align}
 succeeded in 52ms:
  1896	\item \emph{BV antibracket is $(-1)$-shifted Poisson.}
  1897	 The BV bracket $\{-,-\}_{\mathrm{BV}}$ on
  1898	 $\barB^{\mathrm{ch}}(\cA)$
  1899	 \textup{(}Theorem~\textup{\ref{thm:config-space-bv}}\textup{)}
  1900	 has degree~$+1$, hence defines a $(-1)$-shifted Poisson structure.
  1901	 Non-degeneracy is guaranteed by the Koszul duality pairing
  1902	 \textup{(}Corollary~\textup{\ref{cor:duality-bar-complexes-complete}}\textup{)}
  1903	 and the Verdier intertwining
  1904	 $\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \cong \barB(\cA^!)$
  1905	 \textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}};
  1906	 Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)}.
  1907	
  1908	\item \emph{Formal moduli is $(-1)$-shifted symplectic.}
  1909	 The dg Lie algebra $L_g := \barB^{(g)}(\cA)[1]$, with Lie bracket
  1910	 induced by the BV antibracket, carries a non-degenerate invariant
  1911	 pairing of degree~$-1$. By the Kontsevich--Pridham correspondence
  1912	 \cite{Pridham17}, the formal moduli problem
  1913	 $\mathrm{Def}_g(\cA) := \mathrm{MC}(L_g)$
  1914	 is $(-1)$-shifted symplectic.
  1915	
 succeeded in 52ms:
  1360	\index{BV functor}
  1361	Assume the conditional BV package of
  1362	Theorem~\ref{thm:config-space-bv} and a Verdier-duality comparison
  1363	identifying the dual of the bar coalgebra with a factorization algebra
  1364	$\cA^!_\infty$ compatibly with the bracket, coproduct/product, and
  1365	differential. Then the assignment
  1366	\[\mathrm{BV}: \mathrm{ChirAlg}_X \longrightarrow \mathrm{BV\text{-}Alg}\]
  1367	is a lax monoidal functor, and the Verdier dual
  1368	$\mathbb{D}_{\operatorname{Ran}}(\bar{B}(\mathcal{A}))$ identifies
  1369	with a factorization algebra $\cA^!_\infty$ whose underlying complex
  1370	is equivalent to $\bar{B}(\mathcal{A}^!)$
  1371	\textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}.
  1372	On the Koszul locus, $\cA^!_\infty \simeq \cA^!$.
  1373	\end{theorem}
  1374	
  1375	\begin{proof}
  1376	Functoriality of the underlying bar construction is standard. The
  1377	extra BV functoriality and lax monoidal statements are exactly the
  1378	assumed functorial and tensor-compatibility properties of the
 succeeded in 52ms:
  1783	\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
  1784	\label{prop:lagrangian-eigenspaces}
  1785	\index{Lagrangian!eigenspaces|textbf}
  1786	\index{Verdier duality!pairing on moduli}
  1787	Let $(\cA, \cA^!)$ be a chiral Koszul pair and let
  1788	$V = H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
  1789	\begin{enumerate}[label=\textup{(\roman*)}]
  1790	\item Verdier duality on the center local system $\mathcal{Z}(\cA)$
  1791	 induces a non-degenerate bilinear pairing
  1792	 \[
  1793	 \langle -, - \rangle_{\mathbb{D}} \colon V \otimes V \to \mathbb{C}
  1794	 \]
  1795	 of cohomological degree $-(3g-3)$ \textup{(}the shift coming from
  1796	 $\dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 3g-3$\textup{)}.
  1797	\item The Verdier involution $\sigma$ is an \emph{anti-involution}
  1798	 for this pairing:
  1799	 $\langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}} = -\langle v, w \rangle_{\mathbb{D}}$
  1800	 for all $v, w \in V$.
  1801	\item Consequently, the eigenspaces
  1802	 $V^+ = Q_g(\cA)$ and $V^- = Q_g(\cA^!)$
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2494,2508p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21681,21830p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '8952,8992p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '22054,22110p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2494	\begin{definition}[Uniform-weight lane (scalar lane)]
  2495	\label{def:scalar-lane}
  2496	\label{def:uniform-weight-lane}
  2497	\index{scalar lane|textbf}
  2498	\index{uniform-weight lane|see{scalar lane}}
  2499	A modular Koszul chiral algebra~$\cA$ lies on the
  2500	\emph{uniform-weight lane} (or \emph{scalar lane}) if every
  2501	strong generator of~$\cA$ has the same conformal weight.
  2502	Equivalently, $\cA$ has a single primary line in
  2503	$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
  2504	reduces to a one-variable problem.
  2505	Single-generator algebras (Heisenberg, free fermion, Virasoro)
  2506	lie on the scalar lane automatically; multi-generator algebras
  2507	($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.
  2508	
 succeeded in 52ms:
 21681	\begin{theorem}[Multi-weight genus expansion; \ClaimStatusProvedHere]
 21682	\label{thm:multi-weight-genus-expansion}
 21683	\label{thm:multi-generator-universality}
 21684	\index{multi-generator obstruction!genus expansion|textbf}%
 21685	\index{multi-weight genus expansion|textbf}%
 21686	\index{cross-channel correction|textbf}%
 21687	\index{Faber--Pandharipande formula!multi-weight decomposition}%
 21688	\index{genus expansion!multi-channel graph sum}%
 21689	Let\/ $\cA$ be a modular Koszul chiral algebra with
 21690	strong generators $\varphi_1, \ldots, \varphi_r$ of conformal
 21691	weights $h_1, \ldots, h_r$, per-channel modular characteristics
 21692	$\kappa_1, \ldots, \kappa_r$
 21693	\textup{(}Theorem~\textup{\ref{thm:shadow-channel-decomposition})},
 21694	and total modular characteristic\/
 21695	$\kappa(\cA) = \sum_{i=1}^r \kappa_i$.
 21696	\begin{enumerate}[label=\textup{(\roman*)}]
 21697	\item \emph{Per-channel universality.}
 21698	 The diagonal contribution to the genus-$g$ free energy satisfies
 21699	 \begin{equation}\label{eq:multi-weight-diagonal}
 21700	 F_g^{\mathrm{diag}}(\cA)
 succeeded in 51ms:
 22054	\begin{construction}[Multi-channel graph sum]
 22055	\label{constr:cross-channel-graph-sum}
 22056	\index{multi-channel graph sum|textbf}
 22057	\index{channel assignment|textbf}
 22058	\index{graph amplitude!multi-channel}
 22059	Let $\cA$ be a modular Koszul chiral algebra of rank~$r$
 22060	with diagonal Zamolodchikov metric
 22061	$\eta = \operatorname{diag}(\eta_1, \ldots, \eta_r)$.
 22062	Fix a genus~$g \geq 2$. For each stable graph
 22063	$\Gamma \in \mathcal{G}_{g,0}$ with edge set~$E(\Gamma)$
 22064	and vertex set~$V(\Gamma)$, define:
 22065	
 22066	\emph{Channel assignment.}
 22067	A function $\sigma \colon E(\Gamma) \to \{1, \ldots, r\}$.
 22068	There are $r^{|E(\Gamma)|}$ such assignments.
 22069	
 22070	\emph{Multi-channel amplitude.}
 22071	\begin{equation}\label{eq:multi-channel-amplitude}
 22072	A_\Gamma(\sigma, \cA)
 22073	\;:=\;
 succeeded in 51ms:
  8952	\begin{theorem}[Algebraic-family rigidity; \ClaimStatusProvedHere]
  8953	\label{thm:algebraic-family-rigidity}
  8954	\index{cyclic cohomology!algebraic-family rigidity}
  8955	\index{scalar saturation!algebraic-family proof}
  8956	\index{Whitehead decomposition!algebraic-family upgrade}
  8957	Let $\{{\cA}_k\}_{k \in U}$ be a family of vertex algebras
  8958	over a Zariski-open $U \subset \mathbb{C}$ with
  8959	$-h^\vee \notin U$, each equipped with simple affine current
  8960	subalgebra~$\widehat{\fg}_k$, satisfying:
  8961	\begin{enumerate}[label=\textup{(\alph*)}]
  8962	\item ${\cA}_k$ is strongly finitely generated over~$\widehat{\fg}_k$
  8963	 with the same finite set of primary strong generators
  8964	 $\{\varphi_1, \ldots, \varphi_m\}$ for all~$k \in U$;
  8965	\item each conformal weight space $({\cA}_k)_h$ is a
  8966	 finite-dimensional $\fg$-module, with the same
  8967	 $\fg$-representation decomposition for all~$k$;
  8968	\item[\textup{(c$'$)}] the OPE structure constants
  8969	 $C^k_{ij}(n) := \langle \varphi_i{}_{(n)}\varphi_j \rangle$
  8970	 of the primary strong generators are rational functions
  8971	 of\/~$k$ on~$U$.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5241,5334p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5927,6018p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5463,5485p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2648,2702p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '9388,9420p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5463	\begin{remark}[Multi-generator obstruction]\label{rem:multi-generator-obs}
  5464	For an algebra with generators of conformal weights $h_1, \ldots, h_r$:
  5465	at genus~$1$, $\mathrm{obs}_1 = \kappa \cdot \lambda_1$
  5466	\textup{(g=1 only; all-weight at g=1 is unconditional)} with
  5467	$\kappa = \sum_i \kappa_{h_i}$, unconditionally
  5468	(Theorem~\ref{thm:genus-universality}\textup{(iii)}).
  5469	At all genera the \emph{edges} of the genus-$g$ graph sum carry
  5470	the standard Hodge bundle $\mathbb{E} = R^0\pi_*\omega$, because
  5471	the propagator $\partial_z\log E(z,w)$ is weight~$1$
  5472	(Remark~\ref{rem:propagator-weight-universality},
  5473	Proposition~\ref{prop:multi-generator-obstruction}(b)).
  5474	The full identity $\mathrm{obs}_g = \kappa \cdot \lambda_g$
  5475	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5476	\emph{fails} at $g \geq 2$ for multi-weight algebras
  5477	($\mathcal{W}_N$, $N \geq 3$): the free energy receives a
  5478	nonvanishing cross-channel correction
  5479	$\delta F_g^{\mathrm{cross}} \neq 0$
  5480	\textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)}
  5481	(Open Problem~\ref{op:multi-generator-universality}, resolved
  5482	negatively; Theorem~\ref{thm:multi-weight-genus-expansion}).
 succeeded in 51ms:
  5927	\begin{theorem}[Family index theorem for genus expansions;
  5928	\ClaimStatusProvedHere]\label{thm:family-index}
  5929	\index{index theorem!modular deformation|textbf}
  5930	\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
  5931	Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
  5932	$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
  5933	\overline{\mathcal{M}}_g$ be the universal curve with relative
  5934	dualizing sheaf~$\omega_\pi$, and let
  5935	$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
  5936	The following holds for uniform-weight modular Koszul algebras
  5937	at all genera; the genus-$1$ statements are unconditional for
  5938	all families, including multi-generator.
  5939	Define the \emph{modular deformation complex} of~$\cA$ at genus~$g$ by
  5940	\begin{equation}\label{eq:modular-deformation-complex-concordance}
  5941	\mathcal{D}_{\cA}^{(g)}
  5942	\;:=\;
  5943	\kappa(\cA) \cdot \mathbb{E}
  5944	\;\in\; K_0(\overline{\mathcal{M}}_g) \otimes_{\mathbb{Z}} \mathbb{Q},
  5945	\end{equation}
  5946	the $K$-theory class given by $\kappa(\cA)$ copies of the
 succeeded in 51ms:
  5241	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5242	\index{genus universality theorem|textbf}
  5243	\textup{[Regime: curved-central on the Koszul locus; all genera
  5244	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5245	
  5246	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5247	all have the \emph{same} conformal weight. There exists a
  5248	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5249	curvature, such that \begin{equation}\label{eq:genus-universality}
  5250	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
  5251	\qquad \text{in } H^{2g}(\overline{\mathcal{M}}_g)
  5252	\quad \text{for all } g \geq 1,
  5253	\end{equation}
  5254	where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the
  5255	\textup{(LOCAL)}
  5256	Hodge bundle $\mathbb{E} = R^0\pi_*\omega$.
  5257	For algebras with generators of \emph{several} conformal weights,
  5258	the genus-$1$ specialization is unconditional; the higher-genus
  5259	extension is conditional on the strong scalar ansatz of
  5260	Theorem~\ref{thm:multi-generator-universality}.
 succeeded in 51ms:
  2648	 \textup{(}uniform-weight; unconditional at $g = 1$\textup{)}.
  2649	 \end{enumerate}
  2650	 For multi-generator algebras \textup{(}$\mathcal{W}_N$ with
  2651	 $N \geq 3$\textup{)}, the genus-$1$ factorization is unconditional,
  2652	 while the higher-genus extension remains conditional on the
  2653	 strong scalar ansatz
  2654	 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
  2655	\item \emph{Generating function.}
  2656	 The genus free energies
  2657	 assemble as
  2658	 \begin{equation}\label{eq:modular-char-gf}
  2659	 \sum_{g=1}^{\infty} F_g(\cA)\, x^{2g}
  2660	 \;=\; \kappa(\cA) \cdot
  2661	 \left(\frac{x/2}{\sin(x/2)} - 1\right),
  2662	 \end{equation}
  2663	 recovering the $\hat{A}$-genus as topological generating function
  2664	 \textup{(UNIFORM-WEIGHT)}.
  2665	 At genus~$1$ this holds unconditionally for all families;
  2666	 at genus $g \geq 2$ with multi-weight algebras, the scalar
  2667	 formula fails and a cross-channel correction
 succeeded in 50ms:
  9388	effective-\(\Gamma\)-quadruple form
  9389	(Corollary~\ref{cor:effective-quadruple}).
  9390	The algebraic-family theorem subsumes the generic-level result
  9391	and extends it to admissible parameter values only for the
  9392	already verified algebraic-family objects in the standard
  9393	Lie-theoretic landscape \textup{(}not for the live audit surface
  9394	of simple admissible quotients\textup{)}.
  9395	What remains open outside the proved uniform-weight scalar lane is
  9396	the tautological-purity step
  9397	$\Gamma_i(\cA)=\kappa_i(\cA)\Lambda$,
  9398	even when the cyclic direction is already known to be
  9399	one-dimensional.
  9400	The testable criterion is $\dim H^2_{\mathrm{cyc}} = 1$
  9401	(Proposition~\ref{prop:saturation-equivalence}).
  9402	The sharpest potential counterexample, 4D $\mathcal{N}=2$
  9403	quiver VOAs with multi-dimensional conformal manifolds,
  9404	has so far produced only single-parameter dependence in all
  9405	computed cases, and in every tested instance satisfies~(c$'$).
  9406	Theorem~D establishes that $\kappa$ exists as a universal
  9407	invariant; the quadruple reduction strengthens this to the

thinking
**Looking into theorem decomposition**

I need to focus on identifying the exact lines for the C decomposition theorem, particularly addressing the stale user premise. It seems like mentioning this around line 431 could clarify my point. I'll ensure that I keep my remarks concise and informative so they serve the user’s needs without confusion. It’s important to get this right to avoid any misunderstanding!
exec
/bin/zsh -lc "nl -ba metadata/claims.jsonl | sed -n '236,242p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '431,447p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   236	{"label": "conj:categorical-modular-kd", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/concordance.tex", "line": 5266, "title": "Categorical modular Koszul duality", "refs_in_block": ["subsec:coderived-ran", "thm:higher-genus-inversion", "rem:chain-vs-classical-mf", "rem:spectral-characteristic-programme"]}
   237	{"label": "thm:discriminant-spectral-verified", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5433, "title": "Discriminant as spectral determinant, verified cases"}
   238	{"label": "thm:discriminant-spectral", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5478, "title": "Spectral discriminant, general case", "labels_in_block": ["thm:discriminant-spectral", "eq:discriminant-spectral-rational", "eq:p-recursive-recurrence", "eq:discriminant-spectral-general"], "refs_in_block": ["thm:dominant-branch-point"]}
   239	{"label": "comp:spectral-discriminants-standard", "env_type": "computation", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5704, "title": "Spectral discriminants of standard families"}
   240	{"label": "thm:family-index", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 5769, "title": "Family index theorem for genus expansions", "labels_in_block": ["thm:family-index", "eq:modular-deformation-complex-concordance", "eq:family-index-grr", "eq:family-index-generating"], "refs_in_block": ["thm:genus-universality"]}
   241	{"label": "conj:derived-drinfeld-kohno", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/concordance.tex", "line": 6158, "title": "Factorization-categorical DK/KL bridge (DK-3)", "refs_in_block": ["thm:derived-dk-yangian"], "cites_in_block": ["Latyntsev23"]}
   242	{"label": "rem:c13-concordance-holographic", "env_type": "remark", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 6384, "title": "The self-dual central charge $c = 13$", "refs_in_block": ["prop:c13-full-self-duality", "thm:shadow-connection", "rem:koszul-nonperturbative", "subsubsec:shadow-borel-resurgence", "rem:c13-holographic-significance", "sec:shadow-metric"]}
 succeeded in 52ms:
   431	\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
   432	\index{Theorem C!decomposition}
   433	Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
   434	identification, this theorem) produces the ambient complex;
   435	$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
   436	gives the Verdier eigenspace decomposition and its Lagrangian
   437	splitting; $\mathrm{C}_2$
   438	(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
   439	conditional bar-side BV / shifted-symplectic upgrade.
   440	The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
   441	$\sigma$ exchanging the two eigenspaces; at the scalar level
   442	the complementarity formulas below are consequences of the
   443	$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
   444	separate $\mathrm{C}_2$ label:
   445	$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
   446	while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
   447	$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};






thinking
**Evaluating findings in parts**

I’m thinking I could mention that no independent flaw was found in part ii, aside from its reliance on the broken part i. A final answer might not be necessary here. However, I could note that "Part (ii) is not independently falsified locally but does rely on Part (i)'s nondegeneracy". I wonder if including this could be useful, but the structured output contract might not allow extra details, insisting on findings ordered by severity and a summary. Now, I’ll refine the severity and wording.
thinking
**Assessing theorem weaknesses**

I'm noticing some critical issues in the theorem proof. First, the conflation of 2 L_g and C_g undermines Part iii, which is pivotal. Then, I see a circular dependency between genus-universality and family-index, which is foundational for proving the scalar formula — definitely critical. The uniform-weight universality clause cites a theorem that doesn't provide the necessary identification, which also seems critical. Lastly, the assumption of equal weights in scalar-lane equivalence asserts a primary line without proof, creating hidden assumptions. That's quite a few critical issues!
thinking
**Considering theorem discrepancies**

I see this could provide some useful clarity since the user asked about the theorem C2 scalar BV pairing. It’s not a violation, but rather a discrepancy in identifying the theorem. This helps answer the question about the condition, which is related to the conditional BV package and not uniform-weight. To keep things tidy, I might label it as medium. Then, I’ll summarize by noting seven discrepancies, but I’m unsure if "live theorem surface differs from requested label" qualifies as a violation—maybe just a discrepancy.
thinking
**Clarifying theorem search**

I think the user is asking about searching for "C2 scalar BV pairing." I need to check if there's a misidentification of the theorem. Earlier search results were extensive, but I didn’t find an exact "Theorem C2." Maybe I should search within chapters or guides, specifically for "C_2." It might also be related to theorem decomposition. I should check `claims.jsonl` for information on lines related to this theorem and mention "delta_F_g^cross" in context.
thinking
**Evaluating higher genus assertions**

I see that in higher_genus_modular_koszul.tex and higher_genus_foundations.tex, there's stale information suggesting higher genus is still conditional on older theorems, even though we’ve proven the corrected all-weight formula. The correction is properly scoped, but the propagation isn’t. This answers part (d), and I might need to add something about multi-weight failure. It appears that equal weights don’t suppress mixed-channel vertex terms due to how they interact, and this could be included as a critical finding.
thinking
**Evaluating counterexamples**

The user asked if a counterexample could exist at boundary values. I think we can say yes because the current proof doesn't exclude equal-weight multi-generator algebras with mixed-channel vertex amplitudes. This needs to be labeled as an inference, stating a counterexample is not excluded. I should also consider that the proof about `thm:genus-universality` shows edge bundle universality, but the correction stems from vertex OPE data. This might tie back to findings four and five regarding circularity or sufficiency issues.
codex
- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1940](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1940) — Part (i) of `thm:shifted-symplectic-complementarity` proves nondegeneracy by switching from `\mathbb D(\bar B(\cA))` to `\Omega(\cA^!)`. That is not what the cited input says. `thm:bv-functor` identifies the Verdier dual with a factorization algebra whose underlying complex is equivalent to `\bar B(\cA^!)`, not `\Omega(\cA^!)` ([bv_brst.tex:1367](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1367)); `thm:verdier-bar-cobar` gives only a pairing with `\Omega(\cA^!)` ([cobar_construction.tex:1321](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1321)); and the theorem statement itself had used `\bar B(\cA^!)` ([higher_genus_complementarity.tex:1901](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1901)). The proof changes the dual object mid-argument, so nondegeneracy is not established.

- [CRITICAL] [chapters/theory/higher_genus_complementarity.tex:1970](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1970) — Part (iii) asserts a Verdier involution on the bar-side dg Lie algebra `L_g = \bar B^{(g)}(\cA)[1]` and then cites `prop:lagrangian-eigenspaces` to conclude `L_g^\pm` are Lagrangian. But that proposition is about `V = H^*(\overline{\mathcal M}_g,\mathcal Z(\cA))` and the center-side eigenspaces `Q_g(\cA), Q_g(\cA^!)`, not about `L_g` ([higher_genus_complementarity.tex:1787](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1787)). I found no local lift from the center-level polarization to the bar-side BV Lie algebra. This is a second object conflation in the live C2 proof.

- [CRITICAL] [chapters/theory/higher_genus_foundations.tex:5326](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5326) — `thm:genus-universality` derives `\mathrm{obs}_g=\kappa(\cA)\lambda_g` by citing `thm:family-index`, but the proof of `thm:family-index` starts from `thm:genus-universality` itself ([concordance.tex:6009](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:6009)). On the live theorem graph, the scalar genus theorem is circular.

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex:21722](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21722) — The claimed implication “equal conformal weights `=>` `\delta F_g^{cross}=0`” is not proved by the cited source. `thm:multi-weight-genus-expansion` outsources Part (iv) to `thm:algebraic-family-rigidity`, but that theorem explicitly stops at one-dimensionality of the minimal MC direction and says the identification `\Gamma_{\cA}=\kappa(\cA)\Lambda` is “not settled here” ([higher_genus_modular_koszul.tex:8980](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:8980)). The manuscript’s own later diagnosis says the obstruction at higher genus comes from mixed-channel vertex data while edges stay universal ([higher_genus_foundations.tex:5469](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5469), [higher_genus_modular_koszul.tex:22076](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22076)). So uniform-weight sufficiency is not justified.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex:2500](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2500) — `def:scalar-lane` asserts that “all strong generators have the same conformal weight” is equivalent to “a single primary line” and hence a one-variable problem. But the live multi-channel formalism indexes channels by `1,\dots,r` and defines mixed assignments independently of weight equality ([higher_genus_modular_koszul.tex:22066](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:22066)). I found no proof of that equivalence. Hidden assumption: equal weights collapse channel labels.

- [HIGH] [chapters/theory/higher_genus_foundations.tex:5257](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5257) — Downstream status propagation is stale. This theorem, and likewise [higher_genus_modular_koszul.tex:2651](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2651), still says higher genus is “conditional on the strong scalar ansatz of `thm:multi-generator-universality`.” But that label now names the proved decomposition theorem with `\delta F_1^{cross}=0` and higher-genus cross-channel corrections ([higher_genus_modular_koszul.tex:21681](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21681)). The correction term is properly scoped there; these downstream surfaces are not.

- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:433](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:433) — The live manuscript no longer defines C2 as a scalar BV pairing. It defines C2 as the conditional bar-side BV / shifted-symplectic upgrade and explicitly says the scalar complementarity formulas are consequences of C1 plus Theorem D, “not a separate C2 label” ([higher_genus_complementarity.tex:441](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:441)). So the requested “Theorem C2: scalar BV pairing (conditional on uniform-weight)” is already off the current theorem surface.

Part-by-part: Part (i) fails by bar/cobar object switching. Part (ii) has no separate local contradiction I could verify, but it depends on Part (i)’s broken nondegeneracy input. Part (iii) is unsupported by a center-side/bar-side conflation. For the scalar lane, the live manuscript does not justify that uniform-weight alone kills `\delta F_g^{cross}`; what is properly scoped is the later corrected formula `F_g=\kappa\lambda_g^{FP}+\delta F_g^{cross}`, with `g=1` zero and higher-genus mixed-channel corrections possible.

## Summary
Instances checked: 16 | Violations found: 7 | Verdict: FAIL
tokens used
330,186
