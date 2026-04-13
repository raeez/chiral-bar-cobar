# S05_foundations_to_complementarity (853s)

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:738` — PROBLEM: Step I builds the Leray spectral sequence from `\overline{C}_n(X) \times \overline{\mathcal{M}}_g -> \overline{\mathcal{M}}_g`, but the fibers are then treated as varying `\overline{C}_n(\Sigma_g)`. This contradicts the foundations-side universal-family setup in `higher_genus_foundations.tex:2797-2814` and `:3692-3696`. FIX: replace the product diagram by the relative FM family `\pi:\overline{\mathcal{C}}_{g,n}\to\overline{\mathcal{M}}_g`, and rewrite the proof to use the universal configuration space throughout.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:706` — PROBLEM: The theorem states `E_1^{p,q,g}=H^q(\bar B_g^p(\mathcal A),d_{\mathrm{fiber}})`, and the proof at `:761-762` plus Lemma `lem:fiber-cohomology-center` at `:929-965` computes ordinary cohomology of the fiber differential. But the foundations chapter defines the fiber differential as curved, with `\dfib^2=\kappa(\mathcal A)\omega_g` (`higher_genus_foundations.tex:2867`, `:3712-3713`, `:4603-4606`). FIX: rewrite Step I, `lem:fiber-cohomology-center`, `lem:perfectness-criterion`, and `thm:fiber-center-identification` to use the strict flat comparison complex `(\bar B_{\mathrm{flat}}^{(g)}(\mathcal A),\Dg{g})` from `higher_genus_foundations.tex:4569-4617`; if the curved fiber model is kept, only use it after passing to the associated graded, where the `E_1` differential is `d_0`, not `\dfib`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:414` — PROBLEM: C0 identifies the surviving fiber cohomology with `\bigoplus_p(\mathcal A^!)_p` and then with the center by citing `cor:bar-cohomology-koszul-dual`. But `chapters/theory/chiral_koszul_pairs.tex:924-949` only gives bar-cohomology/Koszul-dual-dimension comparison; it does not identify `H^0` with the center. This is an `A / B(A) / A^! / Z^{der}` conflation. FIX: replace Step 3 by the residue-kernel argument already given in `lem:fiber-cohomology-center:945-965`: identify `H^0` as `\ker(d:\bar B^0\to\bar B^1)=Z(\mathcal A|_\Sigma)`, then use that fiberwise identification in Step 4.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:195` — PROBLEM: `def:complementarity-complexes` asserts a cochain involution on `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))` from `thm:verdier-bar-cobar`, but that theorem is the genus-0 bar/cobar Verdier pairing in `chapters/theory/cobar_construction.tex:1312-1349`, not an involution on the ambient center complex. The later attempted repair via `lem:center-isomorphism` at `:1481-1506` also fails: `thm:e1-module-koszul-duality` in `chiral_koszul_pairs.tex:5174-5226` gives complete-module/bar-comodule equivalence, not an equivalence `\mathrm{Mod}_{\mathcal A}\simeq\mathrm{Mod}_{\mathcal A^!}` that would identify centers. FIX: do not define `\sigma` as a self-map on one ambient factor. Either move the definition after a valid center-comparison theorem, or redefine the ambient object as `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))\oplus R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A^!))` with exchange involution `(x,y)\mapsto(\mathbb D y,\mathbb D x)`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1335` — PROBLEM: Step 7 globalizes from the smooth-locus lemma `lem:fiber-cohomology-center` to `H^*(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))`, and Step 8 repeats the same move at `:1570-1585`. But that lemma only proves constancy on `\overline{\mathcal M}_g^{\mathrm{sm}}`; it does not justify the compactified global ambient complex used in C1. C0 is supposed to supply exactly this upgrade, but the proof does not use it. FIX: replace those citations by `thm:fiber-center-identification`, and insert the derived identification `R\pi_{g*}\bar B_{\mathrm{flat}}^{(g)}(\mathcal A)\simeq\mathcal Z_{\mathcal A}` concentrated in degree 0 on all of `\overline{\mathcal M}_g` before defining the KS action and the `q=0` spectral-sequence concentration.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2029` — PROBLEM: `prop:ptvv-lagrangian` claims a shifted-symplectic structure on the cochain complex `C_g:=R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))`, but its proof uses `prop:lagrangian-eigenspaces`, which only constructs a pairing on cohomology `V=H^*(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))` (`:1807-1827`). It then treats `Q_g(\mathcal A)` and `Q_g(\mathcal A^!)` as subcomplexes at `:2061-2080`, although they were defined as cohomology eigenspaces. This silently imports the chain-level perfectness/nondegeneracy hypotheses that the opening says are conditional, and it collides with the later conditional formal-moduli theorem at `:4671-4689`. FIX: either downgrade `prop:ptvv-lagrangian` to a conditional result with explicit hypotheses `C_g\simeq C_g^\vee[-(3g-3)]` and chain-level homotopy eigenspaces `\mathbf Q_g`, or weaken it to a cohomology-level Verdier-Lagrangian statement and stop presenting it as the proved ambient C2 upgrade.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:6179` — PROBLEM: `thm:obs-def-pairing-explicit` reproves complementarity by plain Serre/Poincaré duality, bypassing the Verdier involution, the center-comparison problem, and the perfectness/nondegeneracy boundary tracked in the complementarity chapter. Its example at `:6246-6247` concludes `\mathrm{def}_1=0`, which directly contradicts `higher_genus_complementarity.tex:154-161`, where `Q_1(\mathcal H_\kappa^!)=\mathbb C\cdot\lambda`. FIX: rewrite `thm:obs-def-pairing-explicit` as a corollary of `thm:quantum-complementarity-main` plus the Verdier-pairing result, and replace the genus-1 example by the explicit nonzero genus-1 split `Q_1(\mathcal H_\kappa)=\mathbb C\cdot\kappa`, `Q_1(\mathcal H_\kappa^!)=\mathbb C\cdot\lambda_1`.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:96` — PROBLEM: the prose says “C0 and C1 hold unconditionally on the Koszul locus,” but C0 as stated at `:360-365` additionally assumes finite-dimensional fiber cohomology, and C1 still depends on constructing a global Verdier/Koszul involution on the correct ambient object. FIX: rewrite this sentence to separate the actual hypothesis boundary, e.g. “C0 is proved on the Koszul locus under the finite-dimensional fiber-cohomology hypothesis of Theorem~\ref{thm:fiber-center-identification}; C1 then follows once the global Verdier/Koszul involution has been constructed; the shifted-symplectic upgrades require the extra perfectness/nondegeneracy hypotheses.”

- [LOW] `chapters/theory/higher_genus_complementarity.tex:1882` — PROBLEM: `thm:lagrangian-complementarity` does not exist; the same dead reference appears in `chapters/theory/higher_genus_foundations.tex:7215`. FIX: replace the reference with the intended live label. If the sentence means the proved PTVV ambient statement, use `\ref{prop:ptvv-lagrangian}`; if it means the conditional bar-side BV theorem, use `\ref{thm:shifted-symplectic-complementarity}`.

## Summary
Checked: 7 | Findings: 9 | Verdict: FAIL


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
session id: 019d83c7-8383-70c2-8333-9f59fba5e864
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


MISSION: SEAM AUDIT between higher_genus_foundations.tex and higher_genus_complementarity.tex.

Foundations→Complementarity. Check: (a) the fiber-center identification (C0) feeds correctly into C1/C2, (b) the duality involution is well-defined on the correct objects, (c) no hidden perfectness assumptions

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers


thinking
**Planning an audit process**

I need to act as a coding agent for an audit between two TeX files. First, I should read the AGENTS instructions and gather required files before making any substantial edits. The user is asking for an audit, which indicates I should consult documents like CLAUDE.md and others relevant to the task.

It seems I might need to use the explorer agent for codebase questions, which the developer suggests is preferred over manual reading. I should consider asking the explorer to locate relevant lines and files.
thinking
**Preparing for the audit**

I need to ensure that my claims are grounded in the actual contents of the files I read. While it might not count if an agent reads them, it's safer for me to do so directly via shell. I should still ask the explorer for a map. According to AGENTS, before any mathematical edits, I should read materials like CLAUDE and others relevant to the audit. I'll need to use the deep-beilinson-audit skill and announce it in my commentary while inspecting the repository for files. Let's send a quick update: I'm auditing the seam and loading the necessary protocol.
codex
Auditing the seam between `higher_genus_foundations.tex` and `higher_genus_complementarity.tex`. I’m loading the required audit context first, then I’ll read the transition surface line-by-line and only report findings grounded in the live source.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg --files | rg 'CLAUDE\\.md|concordance\\.tex|theorem_registry\\.md|red_team_summary\\.md|higher_genus_(foundations|complementarity)\\.tex|SKILL\\.md"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/master_concordance.tex
chapters/connections/concordance.tex
chapters/theory/higher_genus_foundations.tex
chapters/theory/higher_genus_complementarity.tex

thinking
**Identifying transition points**

I need to focus on identifying transition points and theorem labels, possibly looking for C0, C1, and C2 within files or a concordance. It’s important to keep track of these elements and label them correctly. I'll prepare an update that includes my commentary on what I've found. Keeping things organized is crucial, especially when discussing these transitions in my findings. Let's make sure everything is clear and precise before sending that commentary out!
codex
Using `deep-beilinson-audit` for this pass. I’ve confirmed the target files and am loading the required constitutional sources plus the exact `C0/C1/C2` surfaces before I start attacking the seam.
exec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else rg --files | rg 'red_team_summary\\.md"'$'"'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
I’ve loaded the constitutional sources. Next I’m locating the exact `C0/C1/C2` seam and every local dependency inside the two target chapters so the audit stays on the real transition surface instead of drifting into nearby theory.
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"C0|C1|C2|fiber|centre|center|Verdier|perfect|perfectness|nondegeneracy|dual|involution|Lagrangian|complementarity|partition function|Q_g|Z\\(|Z\\"'^|derived center|H'"\\"'^'"\\*\\(\\\\overline\\{\\\\mathcal\\{M\\}\\}_g\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    7355 chapters/theory/higher_genus_foundations.tex
    6105 chapters/theory/higher_genus_complementarity.tex
   13460 total
 exited 2 in 50ms:
rg: regex parse error:
    (?:C0|C1|C2|fiber|centre|center|Verdier|perfect|perfectness|nondegeneracy|dual|involution|Lagrangian|complementarity|partition function|Q_g|Z\(|Z\^|derived center|H\^\*\(\overline\{\mathcal\{M\}\}_g)
                                                                                                                                                                              ^^
error: unrecognized escape sequence

thinking
**Adjusting search parameters**

I need to rerun the search with simpler parameters. Maybe I can try using the `-F` option with multiple patterns separately. I’m thinking this approach could lead to clearer results. It feels like breaking it down into simpler parts might help me understand the data better. I hope this adjustment will make my search more effective!
exec
/bin/zsh -lc "rg -n -e 'C0' -e 'C1' -e 'C2' -e 'fiber' -e 'center' -e 'centre' -e 'Verdier' -e 'perfect' -e 'perfectness' -e 'nondegeneracy' -e 'dual' -e 'involution' -e 'Lagrangian' -e 'complementarity' -e 'partition function' -e 'Q_g' -e 'derived center' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:quantum-complementarity-main|thm:higher-genus-inversion|fiber-center|fibre-center|center-fiber|fibre-centre|C0|C1|C2" metadata/theorem_registry.md chapters/connections/concordance.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1207

chapters/theory/higher_genus_complementarity.tex:1:\section{The complementarity theorem}
chapters/theory/higher_genus_complementarity.tex:2:\label{sec:complementarity-theorem}
chapters/theory/higher_genus_complementarity.tex:4:Classical Koszul duality over a point is a discrete correspondence:
chapters/theory/higher_genus_complementarity.tex:14:tower terminates. At genus~$g \geq 1$, the fiberwise curvature
chapters/theory/higher_genus_complementarity.tex:18:decomposes into two complementary halves via Verdier duality:
chapters/theory/higher_genus_complementarity.tex:19:\begin{equation}\label{eq:complementarity-chapter-opening}
chapters/theory/higher_genus_complementarity.tex:22: Q_g(\cA) \;\oplus\; Q_g(\cA^!),
chapters/theory/higher_genus_complementarity.tex:26:it is forced by the Verdier involution on the gravitational
chapters/theory/higher_genus_complementarity.tex:27:complex, which splits the moduli contribution into two Lagrangian
chapters/theory/higher_genus_complementarity.tex:30:characteristics of dual algebras sum to a constant that depends on
chapters/theory/higher_genus_complementarity.tex:31:the duality class alone, independent of all continuous parameters.
chapters/theory/higher_genus_complementarity.tex:33:sense that every state in the gravitational sector has a dual, every
chapters/theory/higher_genus_complementarity.tex:35:The partition function of the closed universe is~$1$; the content of
chapters/theory/higher_genus_complementarity.tex:37:genus, into two halves exchanged by duality.
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:43:\item \emph{Fiber--center identification
chapters/theory/higher_genus_complementarity.tex:46: with finite-dimensional fiber cohomology, the relative bar family
chapters/theory/higher_genus_complementarity.tex:49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:844: \textup{(}Theorem~\textup{\ref{thm:higher-genus-inversion})}.
chapters/theory/higher_genus_foundations.tex:913:Theorem~\ref{thm:higher-genus-inversion}. On the Koszul locus,
chapters/theory/higher_genus_foundations.tex:4170:Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
chapters/theory/higher_genus_foundations.tex:4187:The complementarity column follows from Theorem~\ref{thm:quantum-complementarity-main}
chapters/theory/higher_genus_foundations.tex:4947:The sign reversal is consistent with Main~Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}; the Kodaira--Spencer construction of Theorem~\ref{thm:kodaira-spencer-chiral-complete} provides the geometric mechanism):
chapters/theory/higher_genus_foundations.tex:6997:\textup{(}Theorem~\textup{\ref{thm:higher-genus-inversion})}
chapters/theory/higher_genus_foundations.tex:7011:$\Omega(\barB(\cA))$, and Theorem~\ref{thm:higher-genus-inversion}
chapters/theory/higher_genus_foundations.tex:7213:(Theorem~\ref{thm:quantum-complementarity-main}), and the
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
chapters/theory/higher_genus_complementarity.tex:50: This produces the ambient complex on which~\textup{(C1)}
chapters/theory/higher_genus_complementarity.tex:51: and~\textup{(C2)} operate.
chapters/theory/higher_genus_complementarity.tex:70: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:90:The conditionality in~(C2) is substantive:
chapters/theory/higher_genus_complementarity.tex:96:The fiber--center identification~(C0) and the
chapters/theory/higher_genus_complementarity.tex:97:S-level decomposition~(C1) hold unconditionally on the
chapters/theory/higher_genus_complementarity.tex:98:Koszul locus; the H-level Lagrangian upgrade~(C2) is the
chapters/theory/higher_genus_complementarity.tex:114:$\overline{\mathcal{M}}_g$ required by~(C2) is a stronger
chapters/theory/higher_genus_complementarity.tex:119:the natural geometric setting for the~(C2) upgrade.
chapters/theory/higher_genus_complementarity.tex:178:The Lagrangian upgrade~(C2) is the statement that the two
codex
I’ve isolated the main seam: `C0` at `higher_genus_complementarity.tex:353`, `C1` at `:458`, and the opening claims that say `C0` supplies the ambient complex for both. I’m reading that block in full now together with the exact foundations-side definitions it imports.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1,560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "cor:bar-cohomology-koszul-dual|thm:chiral-koszul-duality|thm:verdier-duality-config-complete|def:complementarity-complexes|lem:perfectness-criterion|thm:fiber-center-identification|thm:quantum-complementarity-main|thm:shifted-symplectic-complementarity|bar cohomology|center local system|Verdier duality on configuration" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:1663:(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/theory/higher_genus_foundations.tex:1940:Theorem~\ref{thm:chiral-koszul-duality}. Then:
chapters/theory/higher_genus_foundations.tex:2027:This filtration satisfies the hypotheses of Theorem~\ref{thm:convergence-filtered}: it is complete and separated (conformal weight is bounded below), compatible with chiral operations ($\mu(F_i \otimes F_j) \subset F_{i+j}$), and has associated graded $\mathrm{gr}\,W_N \cong$ free field algebra (Koszul by Theorem~\ref{thm:chiral-koszul-duality}).
chapters/theory/higher_genus_foundations.tex:4170:Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
chapters/theory/higher_genus_foundations.tex:4187:The complementarity column follows from Theorem~\ref{thm:quantum-complementarity-main}
chapters/theory/higher_genus_foundations.tex:4358:$E_1$~page is the genus-stratified bar cohomology, whose
chapters/theory/higher_genus_foundations.tex:4629:with the chiral product. Their sheaf is the center local system
chapters/theory/higher_genus_foundations.tex:4947:The sign reversal is consistent with Main~Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}; the Kodaira--Spencer construction of Theorem~\ref{thm:kodaira-spencer-chiral-complete} provides the geometric mechanism):
chapters/theory/higher_genus_foundations.tex:5484: curve-independent bar cohomology:
chapters/theory/higher_genus_foundations.tex:6081:induces a \emph{tautological filtration} on the bar cohomology:
chapters/theory/higher_genus_foundations.tex:6679: i.e., tree-level compositions of lower-genus bar cohomology.
chapters/theory/higher_genus_foundations.tex:6940:\begin{corollary}[Loop order decomposition of bar cohomology;
chapters/theory/higher_genus_foundations.tex:6942:\index{bar cohomology!loop order decomposition}
chapters/theory/higher_genus_foundations.tex:6943:For a modular Koszul chiral algebra~$\cA$, the bar cohomology
chapters/theory/higher_genus_foundations.tex:7134:on the all-genus bar cohomology of~$\cA$.
chapters/theory/higher_genus_foundations.tex:7165:all-genus bar cohomology of any Koszul chiral algebra, producing
chapters/theory/higher_genus_foundations.tex:7169:is trivial on bar cohomology (the bar complex is too simple for
chapters/theory/higher_genus_foundations.tex:7207: all-genus bar cohomology through the graph complex weight
chapters/theory/higher_genus_foundations.tex:7213:(Theorem~\ref{thm:quantum-complementarity-main}), and the
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
 succeeded in 53ms:
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


thinking
**Exploring mathematical dependencies**

I need to check specific dependency lines in foundations related to cor:bar-cohomology-koszul-dual and possibly definitions of center local systems. There are relevant theorems like chiral-koszul-duality and verdier-bar-cobar that I should reference. I’ll be focusing on line numbers around 1600-1670, plus sections near 4629. I want to determine if the proof for C1 relies on C0, looking at later steps for hidden assumptions regarding theorem applications like shifted-symplectic-complementarity.
thinking
**Examining theorem dependencies**

I need to investigate whether theorem C1/H-level perfect duality for g≥1 implicitly relies on perfectness or non-degeneracy. The statement mentions "Verdier duality induces pairing," but without explicit conditions. I'll examine the proof around Steps II and III to see if this assertion is justified since the local system might not be perfect. Additionally, I want to locate theorem verdier-bar-cobar, possibly in the foundations or another file, to see how it interacts with bar cohomology and center local systems.
codex
The first serious question is already visible: `C0` is advertised as the ambient input for both `C1` and `C2`, but `Definition 1.1` defines the ambient complex directly from `RΓ(\overline M_g,\mathcal Z(\mathcal A))`, not from `Rπ_{g*}\bar B^{(g)}(\mathcal A)`. I’m now tracing the exact definitions and imported theorems that are supposed to bridge that gap.
exec
/bin/zsh -lc "rg -n \"label\\{cor:bar-cohomology-koszul-dual\\}|label\\{thm:chiral-koszul-duality\\}|label\\{thm:verdier-bar-cobar\\}|label\\{def:modular-koszul-chiral\\}|label\\{thm:kodaira-spencer-chiral-complete\\}|center local system|Z\\(\\\\cA\\)|\\\\mathcal\\{Z\\}_\\\\cA|\\\\mathcal\\{Z\\}\\(\\\\cA\\)\" chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1540,1705p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4580,4665p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:label\{cor:bar-cohomology-koszul-dual\}|label\{thm:chiral-koszul-duality\}|label\{thm:verdier-bar-cobar\}|label\{def:modular-koszul-chiral\}|label\{thm:kodaira-spencer-chiral-complete\}|center local system|Z\(\cA\)|\mathcal\{Z\}_\cA|\mathcal\{Z\}\(\cA\))
                                                                                                                                                                                                                        ^^
error: unrecognized escape sequence
 succeeded in 57ms:
  1540	
  1541	% ================================================================
  1542	% ================================================================
  1543	
  1544	\subsection{Bar-cobar exchange}
  1545	
  1546	\subsubsection{Chain/cochain level precision}
  1547	
  1548	\begin{theorem}[Chain-level vs.\ homology-level structure; \ClaimStatusProvedHere]
  1549	\label{thm:chain-vs-homology}
  1550	Let $(\mathcal{A}, \{m_k\})$ be an $A_\infty$ chiral algebra.
  1551	\begin{enumerate}[label=\textup{(\roman*)}]
  1552	\item \emph{Chain level.}
  1553	 The full $A_\infty$ structure $\{m_k\}_{k \geq 1}$ is preserved,
  1554	 all operations are computable via configuration space integrals,
  1555	 and homotopies have geometric meaning as forms on
  1556	 $\overline{C}_n(X)$.
  1557	\item \emph{Homology level.}
  1558	 The homotopy transfer theorem
  1559	 (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
 succeeded in 50ms:
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
  4590	\;\in\;
  4591	H^2(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathcal{A}))
  4592	\end{equation}
  4593	coming from the hypercohomology spectral sequence
  4594	\begin{equation}
  4595	E_2^{p,q}
  4596	\;=\;
  4597	H^p\!\bigl(\overline{\mathcal{M}}_g,
  4598	\mathcal{H}^q(\mathcal{E}^{\bullet}_{g,\mathrm{flat}}(\mathcal{A}))\bigr)
  4599	\Longrightarrow

thinking
**Rerouting search command**

It looks like the search command failed, so I'm planning to rerun it in a simpler way. I need to find definitions for the terms "center," "local system," and "theorem labels." I think I might need to use a fixed string search with multiple "-e" options to look for plain text. This way, I can refine my search and hopefully get the information I need!
exec
/bin/zsh -lc "rg -n -F -e '\\label{cor:bar-cohomology-koszul-dual}' -e '\\label{thm:chiral-koszul-duality}' -e '\\label{thm:verdier-bar-cobar}' -e '\\label{def:modular-koszul-chiral}' -e '\\label{thm:kodaira-spencer-chiral-complete}' -e 'center local system' -e '\\mathcal{Z}_{\\cA}' -e '\\mathcal{Z}(\\cA)' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1880,2055p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '760,970p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:504:R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}_{\cA})
chapters/theory/higher_genus_foundations.tex:4629:with the chiral product. Their sheaf is the center local system
chapters/theory/higher_genus_foundations.tex:4718:H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)).
chapters/theory/higher_genus_complementarity.tex:20: H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)
chapters/theory/higher_genus_complementarity.tex:48: with $R^0\pi_{g*}\bar{B}^{(g)}(\cA) \cong \mathcal{Z}_{\cA}$
chapters/theory/higher_genus_complementarity.tex:59: H^*(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA))
chapters/theory/higher_genus_complementarity.tex:68: $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$ and
chapters/theory/higher_genus_complementarity.tex:79: \mathcal{Z}(\cA))$ is non-degenerate, the complex
chapters/theory/higher_genus_complementarity.tex:174:$H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$ decomposes
chapters/theory/higher_genus_complementarity.tex:192:\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
chapters/theory/higher_genus_complementarity.tex:194:where $\mathcal{Z}(\cA)$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:208:= \ker(\sigma - \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))),\\
chapters/theory/higher_genus_complementarity.tex:210:= \ker(\sigma + \mathrm{id} \mid H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))).
chapters/theory/higher_genus_complementarity.tex:372:\;\cong\; \mathcal{Z}_{\cA}
chapters/theory/higher_genus_complementarity.tex:375:where $\mathcal{Z}_{\cA}$ is the center local system.
chapters/theory/higher_genus_complementarity.tex:417:hence with the center $\mathcal{Z}_{\cA}\!\mid_\Sigma$
chapters/theory/higher_genus_complementarity.tex:430:$\mathcal{Z}_{\cA}$ by the fiber-level identification
chapters/theory/higher_genus_complementarity.tex:506:\mathcal{Z}(\cA))$, Lemma~\textup{\ref{lem:involution-splitting}(b)}
chapters/theory/higher_genus_complementarity.tex:524:Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA)),
chapters/theory/higher_genus_complementarity.tex:572:on $C_g=R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$.
 succeeded in 52ms:
  1880	\end{enumerate}
  1881	This is the $\mathrm{Ch}_\infty$ avatar of the curved
  1882	$A_\infty$-structure of Definition~\textup{\ref{def:curved-ainfty-hg}}.
  1883	\end{theorem}
  1884	
  1885	\begin{proof}
  1886	The curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ is proved
  1887	in Theorem~\ref{thm:arnold-quantum} via the genus-$g$ Arnold defect.
  1888	The $\mathrm{Ch}_\infty$ structure follows by applying the
  1889	Malikov--Schechtman construction~\cite[Theorem~3.1]{MS24} to the
  1890	cosimplicial object $\barB^{(g,\bullet)}(\cA)$, with the curvature
  1891	correction arising from the period-matrix correction to the
  1892	genus-$0$ propagator. Parts~(ii) and~(iii) are the
  1893	$\mathrm{Ch}_\infty$-algebra restatement of the fact that the bar
  1894	differential squares to the curvature, not to zero.
  1895	\end{proof}
  1896	
  1897	\begin{example}[Heisenberg algebra: curved structure]
  1898	The Heisenberg algebra $\mathcal{H}_k$ has current $J$ with OPE:
  1899	\[J(z)J(w) = \frac{k}{(z-w)^2} + \text{regular}\]
 succeeded in 51ms:
   760	The gauge transformation
   761	$\exp(\kappa(\cA) \cdot \alpha)$ provides a quasi-isomorphism
   762	but not an isomorphism of curved coalgebras: the cobar
   763	functors applied to the two models produce
   764	quasi-isomorphic but potentially non-isomorphic
   765	$A_\infty$ algebras (the difference is an exact deformation,
   766	invisible in cohomology but present at chain level).
   767	\end{proof}
   768	
   769	\begin{proposition}[Genus-$g$ MC element; \ClaimStatusProvedHere]
   770	\label{prop:genus-g-mc-element}
   771	\index{Maurer--Cartan!genus-g component@genus-$g$ component}
   772	\index{master MC element!genus decomposition}
   773	
   774	For each $g \geq 0$, the genus-$g$ component of the master MC
   775	element satisfies:
   776	\[
   777	D^{(g)}_\cA \;\Theta_\cA^{(g)}
   778	+ \sum_{g_1+g_2=g}
   779	\tfrac{1}{2}[\Theta_\cA^{(g_1)}, \Theta_\cA^{(g_2)}]

thinking
**Searching for cohomology resources**

I need to locate the corollary regarding bar-cohomology and its Koszul dual in the foundations of the topic. To do that effectively, I'll need to conduct a search and track down the specific lines or references related to this concept. It feels a bit daunting, but I’ll make sure to find the right information! Let’s get started on that search and see what I can uncover.
exec
/bin/zsh -lc "rg -n -F '\\label{thm:verdier-bar-cobar}' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:chiral-koszul-duality}' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{cor:bar-cohomology-koszul-dual}' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'cor:bar-cohomology-koszul-dual|thm:chiral-koszul-duality|thm:verdier-bar-cobar' chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'bar cohomology.*Koszul dual|Chiral Koszul duality|Verdier.*bar.*cobar' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_foundations.tex:1663:(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/theory/higher_genus_foundations.tex:1940:Theorem~\ref{thm:chiral-koszul-duality}. Then:
chapters/theory/higher_genus_foundations.tex:2027:This filtration satisfies the hypotheses of Theorem~\ref{thm:convergence-filtered}: it is complete and separated (conformal weight is bounded below), compatible with chiral operations ($\mu(F_i \otimes F_j) \subset F_{i+j}$), and has associated graded $\mathrm{gr}\,W_N \cong$ free field algebra (Koszul by Theorem~\ref{thm:chiral-koszul-duality}).
chapters/theory/higher_genus_foundations.tex:2621:\textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar})}.
chapters/theory/bar_cobar_adjunction_inversion.tex:1794:Theorem~\ref{thm:chiral-koszul-duality};
chapters/theory/bar_cobar_adjunction_inversion.tex:2260:By Verdier duality (Theorem~\ref{thm:verdier-bar-cobar}), the counit $\epsilon_{\mathcal{C}} \colon \bar{B}^{\mathrm{ch}}(\Omega^{\mathrm{ch}}(\mathcal{C})) \to \mathcal{C}$ is the Verdier dual of the unit $\eta_{\mathcal{A}^!}$, which is a quasi-isomorphism by Theorem~\ref{thm:geom-unit}. Since Verdier duality on the Fulton--MacPherson compactifications preserves quasi-isomorphisms (Theorem~\ref{thm:verdier-bar-cobar}), the result follows.
chapters/theory/bar_cobar_adjunction_inversion.tex:3447:Theorem~\ref{thm:verdier-bar-cobar}). For Koszul pairs, the
chapters/theory/bar_cobar_adjunction_inversion.tex:3589:(Theorem~\ref{thm:verdier-bar-cobar}) and the general adjunction
chapters/theory/bar_cobar_adjunction_inversion.tex:3653:(Theorem~\ref{thm:verdier-bar-cobar}); the commutativity
chapters/theory/higher_genus_modular_koszul.tex:711:MK2 (Verdier) by Theorem~\ref{thm:verdier-bar-cobar};
chapters/theory/higher_genus_modular_koszul.tex:721:(Theorem~\ref{thm:verdier-bar-cobar}), (2)~the bar complex is an
chapters/theory/higher_genus_modular_koszul.tex:765:MK2 by Theorem~\ref{thm:verdier-bar-cobar}.
chapters/theory/higher_genus_modular_koszul.tex:1220:Theorem~\ref{thm:verdier-bar-cobar}.
chapters/theory/higher_genus_modular_koszul.tex:1464:Theorem~\ref{thm:verdier-bar-cobar}.
chapters/theory/higher_genus_modular_koszul.tex:1614:Theorem~\ref{thm:verdier-bar-cobar}.
chapters/theory/higher_genus_modular_koszul.tex:1674:Theorem~\ref{thm:verdier-bar-cobar}.
chapters/theory/higher_genus_modular_koszul.tex:2037:Theorem~\ref{thm:verdier-bar-cobar}).
chapters/theory/higher_genus_modular_koszul.tex:3796:verified via Theorem~\textup{\ref{thm:verdier-bar-cobar}}
chapters/theory/chiral_koszul_pairs.tex:668:is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
chapters/theory/chiral_koszul_pairs.tex:925:\label{cor:bar-cohomology-koszul-dual}
 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:3815:By the Verdier intertwining (Theorem~\ref{thm:bar-cobar-verdier}):
chapters/theory/higher_genus_complementarity.tex:4030:With Verdier duality and Ayala--Francis compatibility established, the bar-cobar adjunction at higher genus can be inverted on the Koszul locus.
chapters/theory/higher_genus_foundations.tex:1419:While the bar complex uses differential forms on compactified configuration spaces, the cobar complex uses distributions on open configuration spaces. This duality is the distributional manifestation of the intrinsic Verdier-dual definition (Definition~\ref{def:geom-cobar-intrinsic}); see Theorem~\ref{thm:cobar-distributional-model} for the precise identification.
chapters/theory/higher_genus_foundations.tex:1516:The Verdier pairing $\langle m_k^{\mathrm{bar}}, n_k^{\mathrm{cobar}} \rangle$ evaluates to~$1$ by construction: the bar operations~$m_k$ (residue extraction of logarithmic forms) and the cobar operations~$n_k$ (delta-function insertion) are dual under the residue-distribution pairing on $\overline{C}_k(X)$, as established in Theorem~\ref{thm:verdier-duality-operations}.
codex
I’ve confirmed the main imported labels live outside the two seam chapters, so I’m reading them too where they control correctness. On the complementarity side I’m now checking the actual construction of the involution, the pairing, and the shifted-symplectic upgrade instead of trusting the theorem header.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1250,1765p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1770,2035p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1000,1265p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1770	\emph{First}, the Verdier involution~$\sigma$ is a
  1771	\emph{cochain-level} involution on
  1772	$\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$:
  1773	it is induced by the composition of Verdier duality~$\mathbb{D}$
  1774	(an exact functor on $D^b_{\mathrm{hol}}(\mathcal{D})$) with the
  1775	Koszul identification
  1776	$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$
  1777	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}, Step~7).
  1778	Since~$\sigma$ is induced by exact functors, it commutes with
  1779	differentials at every page of the spectral sequence
  1780	(Lemma~\ref{lem:verdier-involution-moduli}).
  1781	\emph{Second}, Lemma~\ref{lem:involution-splitting}(a) gives
  1782	the cochain-level splitting: the projectors
  1783	$p^\pm = \tfrac{1}{2}(\mathrm{id} \pm \sigma)$ are cochain maps
  1784	whose images provide a quasi-isomorphic direct sum decomposition
  1785	$\mathbf{C}_g \simeq \operatorname{im}(p^+) \oplus \operatorname{im}(p^-)$.
  1786	\emph{Third}, model independence
  1787	(Proposition~\ref{prop:model-independence}) ensures the
  1788	decomposition depends only on the Koszul pair $(\cA, \cA^!)$,
  1789	not on auxiliary choices.
 succeeded in 53ms:
  1250	
  1251	\subsection{Step III: decomposition and complementarity}
  1252	
  1253	\begin{proof}[Step III: Steps 7-10]
  1254	
  1255	\emph{Step 7: Center action on moduli space cohomology.}
  1256	
  1257	\begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
  1258	\label{thm:kodaira-spencer-chiral-complete}
  1259	\index{Kodaira--Spencer map|textbf}
  1260	\textup{[Regime: curved-central on the Koszul locus; positive genus
  1261	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1262	
  1263	Let $(\mathcal{A}, \mathcal{A}^!)$ be a chiral Koszul pair with
  1264	$g \geq 1$, and let $\pi: \mathcal{C}_g
  1265	\to \overline{\mathcal{M}}_g$ be the universal curve. There is a natural action:
  1266	\begin{equation}
  1267	\rho: Z(\mathcal{A}) \to \mathrm{End}\bigl(H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))\bigr)
  1268	\end{equation}
  1269	constructed from the Gauss--Manin connection on the chiral homology sheaf.
 succeeded in 52ms:
  1000	$H^*(\bar{B}^*_{\Sigma_g}(\mathcal{A}))$.
  1001	
  1002	On the associated graded $\operatorname{gr}^p_F$, the curvature
  1003	corrections~$d_{\mathrm{curv}}$ vanish because they raise bar degree
  1004	(hence filtration level). The surviving differential~$d_0$ is the
  1005	genus-$0$ collision differential alone. By
  1006	Theorem~\ref{thm:geometric-equals-operadic-bar}, the complex
  1007	$(\operatorname{gr}^p_F, d_0)$ is identified with the operadic bar
  1008	complex of~$\operatorname{gr}\mathcal{A}$.
  1009	
  1010	Since $\mathcal{A}$ is Koszul
  1011	(Definition~\ref{def:chiral-koszul-pair}), the bar concentration
  1012	theorem (Theorem~\ref{thm:bar-concentration}) gives
  1013	\[
  1014	E_1^{p,q}
  1015	= H^q\bigl(\operatorname{gr}^p_F
  1016	 \bar{B}^*_{\Sigma_g}(\mathcal{A}),\, d_0\bigr)
  1017	= 0
  1018	\qquad\text{for } q \neq 0.
  1019	\]

thinking
**Inspecting theorems**

I’m considering the importance of the theorem prop:ptvv-lagrangian, especially since it might hold proof for C2. This could conflict with Theorem thm:shifted-symplectic-complementarity. It's interesting to think that there could be a disagreement between these theorems! I need to delve into the details from line 2029 onwards for more clarity. It sounds like a critical examination is in order! Let’s see what I find there.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2029,2155p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2155,2265p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2029	\begin{proposition}[PTVV Lagrangian embedding; \ClaimStatusProvedHere]
  2030	\label{prop:ptvv-lagrangian}
  2031	\index{PTVV!Lagrangian embedding|textbf}
  2032	\index{Lagrangian!PTVV sense|textbf}
  2033	For a chiral Koszul pair $(\cA, \cA^!)$ and $g \geq 2$, the cochain
  2034	complex
  2035	$C_g := R\Gamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$
  2036	carries a $(-(3g{-}3))$-shifted symplectic structure in the sense of
  2037	Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}, and
  2038	$Q_g(\cA)$, $Q_g(\cA^!)$ embed as complementary Lagrangians in the
  2039	PTVV sense.
  2040	\end{proposition}
  2041	
  2042	\begin{proof}
  2043	\emph{Shifted symplectic structure.}
  2044	For a cochain complex $V$ with a non-degenerate symmetric pairing
  2045	$\langle -,- \rangle \colon V \otimes V \to \mathbb{C}[n]$,
  2046	the associated linear derived affine scheme
  2047	$\mathbf{V} := \operatorname{Spec}(\operatorname{Sym}(V^*))$
  2048	carries an $n$-shifted symplectic structure: the pairing defines a
 succeeded in 50ms:
  2155	$\mathcal{F} = \sum_{g \geq 0} \hbar^{2g-2} \mathcal{F}_g$ is
  2156	recovered from the spectral sequence: the $d_r$ differential shifts
  2157	genus by~$r$ in the genus filtration, and the $E_\infty$~page
  2158	captures the genus-graded partition function. The physical
  2159	identification of $d_r$ with literal integration over
  2160	$\overline{\mathcal{M}}_r$ is heuristic; the actual $d_r$ is a
  2161	derived-functor differential, not a pushforward integral.
  2162	Convergence is controlled by the finite cohomological dimension
  2163	of $\overline{\mathcal{M}}_g$
  2164	(Lemma~\ref{lem:quantum-ss-convergence}; compare
  2165	Costello--Gwilliam~\cite{CG17}, Volume~2, Chapter~5).
  2166	\end{remark}
  2167	
  2168	\subsection{Corollaries and physical interpretation}
  2169	
  2170	\begin{conjecture}[Physical interpretation; \ClaimStatusConjectured]
  2171	\label{conj:physical-complementarity}
  2172	In conformal field theory language, the Complementarity Theorem states:
  2173	\begin{itemize}
  2174	\item \emph{Central charges in one theory $\leftrightarrow$ Curved algebra structure 

thinking
**Inspecting foundations**

I need to check the foundations starting around line 500 and maybe consider mentioning the ambient complexity, as the search pointed me to line 504. I'll open the document around that area to see what information I can gather. It seems like a good spot to start my inspection and find relevant details. Let's see what I can uncover there!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '460,535p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4660,4745p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6168,6245p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4660	\begin{equation}
  4661	H^*(\overline{\mathcal{M}}_{1,1}) = \mathbb{Q}[\lambda] / (\lambda^2) \cong \mathbb{Q} \oplus \mathbb{Q}\lambda
  4662	\end{equation}
  4663	
  4664	For the Heisenberg algebra $\mathcal{H}_\kappa$, the obstruction to genus-1 extension defines a class in $H^2$
  4665	\textup{(g=1 only; all-weight at g=1 is unconditional)}:
  4666	\begin{equation}
  4667	\mathrm{obs}_1 = \kappa \cdot \lambda_1 \in H^2(\overline{\mathcal{M}}_{1,1}, \mathbb{C}) \cong \mathbb{C}
  4668	\end{equation}
  4669	(Note: $H^1(\overline{\mathcal{M}}_{1,1}) = 0$ since the Poincar\'e polynomial $1 + t^2$ has no odd-degree terms.)
  4670	
  4671	The \emph{central charge} is the numerical invariant
  4672	\textup{(g=1 only; all-weight at g=1 is unconditional)}:
  4673	\begin{equation}
  4674	\int_{\overline{\mathcal{M}}_{1,1}} \mathrm{obs}_1 = \kappa \int_{\overline{\mathcal{M}}_{1,1}} \lambda_1 = \frac{\kappa}{24}
  4675	\end{equation}
  4676	\end{example}
  4677	
  4678	\begin{example}[Genus 2 obstruction]
  4679	\label{ex:genus-2-obstruction}
 succeeded in 52ms:
   460	\begin{definition}[Modular curvature: the direct definition]
   461	\label{def:modular-curvature-direct}
   462	\label{def:scalar-curvature-shadow}
   463	\index{curvature coefficient!direct definition|textbf}
   464	\index{self-contraction trace|textbf}
   465	The \emph{modular curvature coefficient} of a cyclic chiral
   466	algebra~$\cA$ with invariant bilinear form
   467	$\langle -, - \rangle_\cA$ is
   468	\begin{equation}\label{eq:kappa-direct}
   469	\kappa(\cA)
   470	\;:=\;
   471	\mathrm{Tr}_\cA
   472	\;:=\;
   473	\sum_a \langle e_a, e^a \rangle_\cA,
   474	\end{equation}
   475	where $\{e_a\}$ is a homogeneous basis and $\{e^a\}$ the dual
   476	basis. Equivalently, $\kappa(\cA) = \Theta_{\cA}^{\leq 2}$ is the
   477	weight-$2$ level of the shadow obstruction tower
   478	\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
   479	The self-contraction trace is the value of the unique
 succeeded in 51ms:
  6168	\index{uncurved quotient category}
  6169	The \emph{uncurved quotient} of the category $\mathrm{KCA}$ is the localization
  6170	\[
  6171	\mathrm{KCA}^{\mathrm{unc}} := \mathrm{KCA}[\kappa^{-1}(0)]
  6172	\]
  6173	at the full subcategory of algebras with $\kappa = 0$. Objects of $\mathrm{KCA}^{\mathrm{unc}}$ are equivalence classes of Koszul chiral algebras modulo critical-level algebras: $\cA \sim \mathcal{B}$ if $\cA \otimes \mathcal{C} \simeq \mathcal{B} \otimes \mathcal{C}'$ for some $\mathcal{C}, \mathcal{C}'$ with $\kappa = 0$. By Theorem~\ref{thm:koszul-k0}, the obstruction coefficient $\kappa$ is a complete invariant on $K_0(\mathrm{KCA}^{\mathrm{unc}})$.
  6174	\end{definition}
  6175	
  6176	\subsection{Connection to deformation-obstruction complementarity}
  6177	\label{subsec:obstruction-deformation-connection}
  6178	
  6179	\begin{theorem}[Obstruction-deformation pairing; \ClaimStatusProvedHere]\label{thm:obs-def-pairing-explicit}
  6180	\textup{[Regime: curved-central on the Koszul locus; all genera
  6181	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  6182	
  6183	\leavevmode\\
  6184	The obstruction class
  6185	$\text{obs}_g \in H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathcal{A}))$
  6186	pairs with the deformation space $Q_g(\mathcal{A}^!)$ via
  6187	\begin{equation}

thinking
**Examining theorems and gaps**

I think there's a risk with the theorem on obs-def-pairing in the foundations, as it might state complementarity without conditions. The user is asking about a seam audit related to this. I should inspect the complementarity theorem and see how it's referenced, as there may be a mismatch in theorem labeling. I’ll need to check if `thm:deformation-obstruction` is outdated or possibly unrelated, and evaluate if pairing uses Serre duality without conditions, especially if the complementarity chapter has specific conditions.
codex
The foundations chapter also has an independent “obstruction-deformation pairing” theorem that already states the complementarity decomposition using plain Serre/Poincaré duality. I’m checking whether that earlier surface is stronger than the complementarity chapter actually proves, because that would be a seam-level status leak.
exec
/bin/zsh -lc "rg -n 'thm:deformation-obstruction|obstruction-deformation pairing|quantum-complementarity-main|perfectness|nondegenerate|Serre duality on .*moduli' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:70: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:73: \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
chapters/theory/higher_genus_complementarity.tex:76: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
chapters/theory/higher_genus_complementarity.tex:91:perfectness requires PBW filterability and finite-dimensional
chapters/theory/higher_genus_complementarity.tex:92:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
chapters/theory/higher_genus_complementarity.tex:101:\begin{remark}[Calabi--Yau exchange and the perfectness hypothesis]
chapters/theory/higher_genus_complementarity.tex:107:(a nondegenerate invariant bilinear form), then
chapters/theory/higher_genus_complementarity.tex:110:fiber-level perfectness of the bar complex, and makes
chapters/theory/higher_genus_complementarity.tex:113:intertwining. The family-level perfectness over
chapters/theory/higher_genus_complementarity.tex:116:base change (Lemma~\ref{lem:perfectness-criterion}).
chapters/theory/higher_genus_complementarity.tex:280:\label{lem:perfectness-criterion}
chapters/theory/higher_genus_complementarity.tex:281:\index{perfectness criterion|textbf}
chapters/theory/higher_genus_complementarity.tex:282:\index{bar complex!relative perfectness|textbf}
chapters/theory/higher_genus_complementarity.tex:365:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
chapters/theory/higher_genus_complementarity.tex:427:(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
chapters/theory/higher_genus_complementarity.tex:438:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
chapters/theory/higher_genus_complementarity.tex:459:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:878:anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
chapters/theory/higher_genus_complementarity.tex:1122:\cong H^*(C_n(X))$; the perfectness then follows from
exec
/bin/zsh -lc "rg -n 'lem:fiber-cohomology-center|thm:ss-quantum|lem:quantum-from-ss|lem:verdier-extension-exchange|thm:e1-module-koszul-duality|prop:model-independence' chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_modules.tex:22:(Theorem~\ref{thm:e1-module-koszul-duality}): complete
chapters/theory/chiral_modules.tex:38:A module over a factorization algebra is itself a factorization algebra on a pointed space: the marked point carries the module data, the remaining points carry algebra data (Voronov~\cite{Voronov99}, Costello--Gwilliam~\cite{CG17}, Ayala--Francis~\cite{AF15}). The bar complex $\bar{B}(\cA, M)$ lives on such pointed configuration spaces, and its Verdier dual is a comodule over $\bar{B}(\cA)$. On the proved quadratic genus-$0$ $\Eone$ surface, this leads to the complete/conilpotent module comparison of Theorem~\ref{thm:e1-module-koszul-duality}. More generally, the module bar construction provides the intrinsic coalgebra-side object, while broader representation-category equivalences require additional hypotheses and are treated only on the specific lanes where they are established.
chapters/theory/chiral_modules.tex:287:Theorem~\ref{thm:e1-module-koszul-duality}. Then $\Phi$ is the module
chapters/theory/chiral_modules.tex:306:Theorem~\ref{thm:e1-module-koszul-duality}, rewritten in the notation
chapters/theory/chiral_modules.tex:338:Theorem~\ref{thm:e1-module-koszul-duality}, its completed module
chapters/theory/chiral_modules.tex:466:Theorem~\ref{thm:e1-module-koszul-duality}. For complete
chapters/theory/chiral_modules.tex:485:Theorem~\ref{thm:e1-module-koszul-duality}(ii), rewritten in the
chapters/theory/chiral_modules.tex:1248: (Theorem~\ref{thm:ss-quantum}).
chapters/theory/chiral_modules.tex:1586:The contragredient $(-)^\vee$ on $\mathcal{O}_k$ operates \emph{within} a fixed level; Koszul duality sends complete $\widehat{\mathfrak{g}}_k$-modules to conilpotent bar-comodules on the dual-side genus-$0$ lane \textup{(}Theorem~\ref{thm:e1-module-koszul-duality}\textup{)}. Thus it compares structures at \emph{different} levels $k' = -k - 2h^\vee$, while the contragredient remains internal to level~$k$. Both preserve highest weight labels but act on different structures.
chapters/theory/chiral_modules.tex:1931:\textup{(}Theorem~\textup{\ref{thm:e1-module-koszul-duality})}.
chapters/theory/chiral_modules.tex:3382:Theorem~\ref{thm:e1-module-koszul-duality}, the module bar functor
chapters/theory/chiral_modules.tex:3403:finite-type/quadratic lane where Theorem~\ref{thm:e1-module-koszul-duality}
chapters/theory/chiral_modules.tex:3419:(Theorem~\ref{thm:e1-module-koszul-duality}).
chapters/theory/chiral_modules.tex:3546:Theorem~\ref{thm:e1-module-koszul-duality}, the module bar functor
chapters/theory/chiral_modules.tex:4687:\textup{(}Theorem~\textup{\ref{thm:e1-module-koszul-duality})},
chapters/theory/chiral_modules.tex:4700:Combine Theorem~\ref{thm:e1-module-koszul-duality} (the module bar
chapters/theory/chiral_koszul_pairs.tex:3785:(Proposition~\ref{prop:model-independence}). The M-level
chapters/theory/chiral_koszul_pairs.tex:5164:Theorem~\ref{thm:e1-module-koszul-duality}, restricted to the
chapters/theory/chiral_koszul_pairs.tex:5176:\label{thm:e1-module-koszul-duality}
chapters/theory/chiral_koszul_pairs.tex:5324:(used in the proof of Theorem~\ref{thm:e1-module-koszul-duality}(iii)

thinking
**Reviewing quantum theorems**

I need to read theorems like ss-quantum, lem quantum-from-ss, and lem fiber-cohomology-center to understand complementarity better. This is important because the main proof likely relies on them. The fiber-cohomology-center has already been partially included. I should review sections around pages 700-940 to clarify if `Q_g` is defined as E∞ from a spectral sequence or through eigenspaces. I also wonder if the lemma for fiber-cohomology-center duplicates C0 in the restricted smooth locus, which I need to inspect.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '680,940p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4120,4205p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '900,980p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   680	\begin{equation}
   681	\bar{B}^{(h)}(\mathcal{A}) = R\Gamma(\overline{\mathcal{M}}_h, \mathcal{H}^*(\mathcal{
   682	C}_n, \mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log}))
   683	\end{equation}
   684	
   685	The genus filtration $F^{\leq g}$ consists of contributions from curves of genus 
   686	$\leq g$. This is well-defined because:
   687	\begin{enumerate}
   688	\item The differential $d = \sum_{D} \text{Res}_D$ respects the genus filtration 
   689	(residues at divisors do not change genus)
   690	\item The comultiplication $\Delta$ respects the genus filtration (splitting points 
   691	does not change total genus)
   692	\end{enumerate}
   693	\end{proof}
   694	
   695	\begin{remark}[Physical interpretation]
   696	In quantum field theory, the genus expansion is the \emph{loop expansion}:
   697	\begin{equation}
   698	Z = Z^{(0)} + \hbar Z^{(1)} + \hbar^2 Z^{(2)} + \cdots
   699	\end{equation}
 succeeded in 51ms:
  4120	
  4121	But this is \emph{precisely the associativity constraint} for the chiral product in $\mathcal{A}_2$: the second sum encodes $(\phi_i \cdot \phi_\alpha) \cdot \phi_\beta$ evaluated at $\phi_\gamma$, while the first sum encodes the rearrangement through $\phi_i \cdot (\phi_\alpha \cdot \phi_\beta)$.
  4122	
  4123	Geometrically: $d_!^2 = 0$ encodes $\partial^2 = 0$ in configuration space; boundaries of boundaries vanish (Arnold--Orlik--Solomon relations).
  4124	\end{proof}
  4125	
  4126	\begin{remark}
  4127	Theorem~\ref{thm:coalgebra-axioms-verified} exhibits the characteristic feature of Koszul duality: associativity of the algebra $\mathcal{A}_2$ is equivalent to nilpotence of the coalgebra differential $d_!$. Algebraic structure on one side translates to cohomological structure on the dual side.
  4128	\end{remark}
  4129	
  4130	%----------------------------------------------------------------
  4131	% STAGE 3: BAR COMPUTES THE DUAL
  4132	%----------------------------------------------------------------
  4133	
  4134	\subsection{\texorpdfstring{Stage 3: bar construction computes $\mathcal{A}_2^!$}{Stage 3: bar construction computes A-2!}}
  4135	
  4136	\begin{theorem}[Bar computes Koszul dual, complete statement; \ClaimStatusProvedHere]
  4137	\label{thm:bar-computes-koszul-dual-complete}
  4138	\label{thm:chiral-koszul-duality}
  4139	\textup{[Regime: quadratic on the Koszul locus;
 succeeded in 51ms:
   900	$V = \bigoplus_{n \geq 2} \bC \cdot L_{-n}$
   901	(the Virasoro generators modulo vacuum), which is
   902	free of finite rank in each conformal weight.
   903	
   904	\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
   905	$\operatorname{gr}_F \mathrm{Vir}_c
   906	\cong \operatorname{Sym}(V)$
   907	is a polynomial algebra (the OPE reduces to a commutative
   908	product on the associated graded: the non-linear terms
   909	$T_{(0)}T = \partial T$, $T_{(1)}T = 2T$ are lower-order in the
   910	PBW filtration, and the quartic pole $T_{(3)}T = c/2$ is a
   911	scalar that contributes to the curvature, not the
   912	associated graded bracket).
   913	By Priddy's theorem, $\operatorname{Sym}(V)$ is Koszul.
   914	
   915	\emph{Hypothesis~\ref{item:pbw-bounded}.}
   916	Same argument as the Kac--Moody case: the number of
   917	partitions of weight~$h$ into at most $n$ parts (each $\geq 2$)
   918	is finite.
   919	
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5168,5248p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '350,430p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1290,1375p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5168	require extra hypotheses and a module-level comparison theorem beyond
  5169	what is currently established here.
  5170	\end{remark}
  5171	
  5172	\subsection{\texorpdfstring{$\Eone$-chiral module category Koszul duality}{E1-chiral module category Koszul duality}}
  5173	
  5174	\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-module category Koszul duality;
  5175	\ClaimStatusProvedHere]
  5176	\label{thm:e1-module-koszul-duality}
  5177	\index{module Koszul duality|textbf}
  5178	Let $\mathcal{A}$ be a Koszul $\Eone$-chiral algebra with Koszul
  5179	dual bar coalgebra
  5180	$C_{\mathcal{A}} := \bar{B}^{\mathrm{ch}}(\mathcal{A})$
  5181	\textup{(}Theorem~\ref{thm:e1-chiral-koszul-duality},
  5182	Corollary~\ref{cor:e1-self-duality}\textup{)}. When the finite-type
  5183	graded dual exists, we write $\mathcal{A}^! := C_{\mathcal{A}}^\vee$
  5184	for the corresponding dual algebra. Then the bar-cobar adjunction
  5185	restricts to an equivalence of derived categories between
  5186	\emph{complete} (pro-nilpotent) $\mathcal{A}$-modules and
  5187	\emph{conilpotent} $C_{\mathcal{A}}$-comodules:
 succeeded in 51ms:
   350	\end{proof}
   351	
   352	\begin{lemma}[Verdier duality exchanges extensions; \ClaimStatusProvedHere]%
   353	\label{lem:verdier-extension-exchange}
   354	Let $Y$ be a smooth variety, $U \xhookrightarrow{j} Y$ an open inclusion
   355	with complement a normal crossings divisor, and $\mathcal{M}$ a holonomic
   356	$\mathcal{D}_U$-module. Then there is a canonical isomorphism in the
   357	derived category of holonomic $\mathcal{D}_Y$-modules:
   358	\[
   359	\mathbb{D}_Y(j_*\mathcal{M}) \;\cong\; j_!\,\mathbb{D}_U(\mathcal{M}).
   360	\]
   361	\end{lemma}
   362	
   363	\begin{proof}
   364	This is a standard consequence of the theory of holonomic
   365	$\mathcal{D}$-modules; we recall the argument. By
   366	adjunction, $j_*$ is right adjoint to $j^*$ and $j_!$ is left adjoint to
   367	$j^!$. For $j$ an open inclusion we have $j^! = j^*$, so:
   368	\[
   369	j_! \dashv j^* \dashv j_*.
 succeeded in 51ms:
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

thinking
**Searching for modular concepts**

I think I need to read the definition of modular pre-Koszul datum. Maybe I should look into higher_genus_modular_koszul or foundational concepts related to it? There's likely some interesting information out there. I'll just do a quick search to gather more details and see what I can find. It's always good to understand these concepts better, and I'm curious about what I might discover!
exec
/bin/zsh -lc "rg -n '\\\\label\\{def:modular-koszul-chiral\\}|modular pre-Koszul datum|MK1|MK3' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '60,145p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:45: For every chiral algebra~$\cA$ carrying a modular pre-Koszul datum
chapters/theory/higher_genus_complementarity.tex:284:curve~$X$, carrying a modular pre-Koszul datum
chapters/theory/higher_genus_complementarity.tex:293: Koszul-acyclic \textup{(}axioms \textup{MK1} and
chapters/theory/higher_genus_complementarity.tex:294: \textup{MK3} of
chapters/theory/higher_genus_complementarity.tex:360:Assume $\cA$ carries a modular pre-Koszul datum
chapters/theory/higher_genus_complementarity.tex:393:By genus-$0$ Koszulity (axiom~MK1), the associated graded is
chapters/theory/higher_genus_complementarity.tex:4140:axioms \textup{MK1--MK3)}.
chapters/theory/higher_genus_complementarity.tex:4294:Theorem~B requires Koszulity (MK1). For simple admissible affine
chapters/theory/higher_genus_foundations.tex:837: If $\cA$ satisfies MK1 \textup{(}genus-$0$
chapters/theory/higher_genus_foundations.tex:911:Level~(iii): MK1 (PBW collapse at $E_2$) implies diagonal Ext
chapters/theory/higher_genus_foundations.tex:6920:By the PBW filterability hypothesis (axiom~MK1 of
chapters/theory/higher_genus_modular_koszul.tex:535: Definition~\ref{def:modular-koszul-homotopy}]\label{def:modular-koszul-chiral}
chapters/theory/higher_genus_modular_koszul.tex:644:Only MK1--MK3 are axioms; MK4 and MK5 are
chapters/theory/higher_genus_modular_koszul.tex:654:The definition separates \emph{hypotheses} (MK1--MK3) from
chapters/theory/higher_genus_modular_koszul.tex:655:\emph{consequences} (MK4--MK5). The hypotheses are checkable; the consequences are theorems: MK4 (inversion) is proved by Theorem~\ref{thm:higher-genus-inversion} and MK5 (complementarity) by Theorem~\ref{thm:quantum-complementarity-main}, both from MK1--MK3.
chapters/theory/higher_genus_modular_koszul.tex:656:There is no circularity. The dg axioms MK1--MK3 present the homotopy axioms
chapters/theory/higher_genus_modular_koszul.tex:693:\textup{MK1--MK3} of Definition~\textup{\ref{def:modular-koszul-chiral}}.
chapters/theory/higher_genus_modular_koszul.tex:709:MK1 (genus-0 Koszulity) by
chapters/theory/higher_genus_modular_koszul.tex:712:MK3 (modular Koszulity) by explicit genus-$g$ computation: for~(a)
chapters/theory/higher_genus_modular_koszul.tex:735:\textup{MK1--MK3}.
 succeeded in 51ms:
    60	dg~Lie algebra~$\gAmod$, a strict model of the homotopy-invariant
    61	$L_\infty$-algebra $\Definfmod(\cA)$
    62	(\S\ref{subsec:two-level-convention}). The weight filtration on
    63	$\gAmod$ controls the extension tower: each finite truncation
    64	$\Theta_\cA^{\leq r}$ is a graph sum through degree~$r$, with vertex
    65	labels from the transferred cyclic minimal model and edge contractions
    66	by the complementarity propagator $P_\cA = H_\cA^{-1}$.
    67	
    68	%% FORCED LOGICAL CHAIN: five constructions, each demanded by the preceding.
    69	
    70	Five constructions govern $\Theta_\cA$.
    71	Each arises because the preceding one creates a problem that
    72	only the next one resolves.
    73	\begin{enumerate}[label=\textup{(\arabic*)}]
    74	\item \emph{Shadow algebra.}
    75	 The MC element $\Theta_\cA$ lives in an infinite-dimensional
    76	 dg~Lie algebra. To extract finite-dimensional invariants,
    77	 pass to cohomology:
    78	 $\cA^{\mathrm{sh}} := H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
    79	 is the bigraded Lie algebra
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '145,255p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   145	
   146	 No other depths occur (Proposition~\ref{prop:depth-gap-trichotomy}):
   147	 $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$, with a gap at~$3$.
   148	
   149	\item \emph{Formality}
   150	 (Theorem~\ref{thm:shadow-formality-identification}). The
   151	 genus-$0$ shadow obstruction tower coincides with the
   152	 $L_\infty$~formality obstruction tower:
   153	 $\kappa$, $\mathfrak{C}$, $\mathfrak{Q}$ are the genus-$0$
   154	 obstructions at degrees $2$, $3$, $4$, and the four-class
   155	 partition $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is the
   156	 formality classification of the transferred
   157	 $L_\infty$-structure.
   158	 Positive-genus corrections are carried by the quantum layer.
   159	
   160	\item \emph{Complementarity}
   161	 (Theorem~\ref{thm:quantum-complementarity-main}). For a Koszul pair
   162	 $(\cA, \cA^!)$, the quantum corrections decompose as
   163	 $Q_g(\cA) \oplus Q_g(\cA^!) \cong
   164	 H^*(\overline{\mathcal{M}}_g, Z(\cA))$:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '520,665p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4120,4225p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4120	
  4121	\begin{proof}
  4122	Let $C=\operatorname{Cone}(f)$. It suffices to prove $C$ is acyclic.
  4123	From $j^*f$ and $i^*f$ quasi-isomorphisms, $j^*C$ and $i^*C$ are acyclic.
  4124	Apply the localization triangle
  4125	\[j_!j^*C \longrightarrow C \longrightarrow i_*i^*C \xrightarrow{+1}.\]
  4126	Both outer terms are acyclic, hence $C$ is acyclic. Therefore $f$ is a
  4127	quasi-isomorphism.
  4128	\end{proof}
  4129	
  4130	\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
  4131	\index{bar-cobar inversion!higher genus}
  4132	\textup{[}Regime: curved-central on the Koszul locus
  4133	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
  4134	
  4135	\smallskip\noindent
  4136	The genus-$0$ inversion of~\S\ref{sec:frame-inversion} extends to all genera; at the scalar level, quantum corrections are controlled by $\kappa(\cA) \cdot \lambda_g$ for uniform-weight algebras \textup{(}Theorem~\textup{\ref{thm:modular-characteristic})}; for multi-weight algebras at $g \geq 2$, the scalar formula receives a cross-channel correction \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}, op:multi-generator-universality resolved negatively\textup{)}.
  4137	
  4138	Let $\cA$ be a modular pre-Koszul chiral algebra
  4139	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral}},
codex
A second seam break is showing up: the file itself disagrees about what `C2` is. The chapter opening says `C2` is the conditional ambient shifted-symplectic upgrade on `RΓ(\overline M_g,\mathcal Z(\mathcal A))`, but the later “C2” theorem is a different conditional bar-side BV statement, while the ambient PTVV statement is already marked `ProvedHere` in a proposition. I’m pinning down the exact conflict surface now.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '40,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'prop:lagrangian-perfectness|perfectness for the standard landscape|lagrangian-perfectness|PTVV Lagrangian embedding|shifted-symplectic-complementarity|conditional on perfectness and nondegeneracy|C2' chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '188,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    40	 genus~$0$ unconditional; for arbitrary~$\cA$,
    41	 $g \geq 1$ is conditional on
    42	 axiom~\ref{MK:modular}; unconditional on the
    43	 CFT-type standard landscape except integer-spin
    44	 $\beta\gamma$ by Theorem~\ref{thm:pbw-propagation}
    45	 and Remark~\ref{rem:pbw-propagation-scope}
    46	 & \ClaimStatusProvedHere \\
    47	\textbf{C} & Complementarity
    48	 & $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\mathcal{M}}_g, Z(\cA))$
    49	 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)};
    50	 Verdier-side Lagrangian splitting unconditional;
    51	 ambient shifted-symplectic upgrade conditional on
    52	 perfectness/nondegeneracy
    53	 & \ClaimStatusProvedHere \\
    54	\textbf{D} & Modular characteristic
    55	 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
    56	 for uniform-weight modular Koszul algebras
    57	 \textup{(}Definition~\ref{def:scalar-lane}\textup{)}
    58	 at all genera;
    59	 genus~$1$ universal for all families;
 succeeded in 52ms:
chapters/theory/chiral_modules.tex:2072:\index{C2-cofiniteness@$C_2$-cofiniteness}
chapters/theory/chiral_koszul_pairs.tex:2312:Proposition~\textup{\ref{prop:lagrangian-perfectness}}; conditional
chapters/theory/higher_genus_complementarity.tex:51: and~\textup{(C2)} operate.
chapters/theory/higher_genus_complementarity.tex:73: \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
chapters/theory/higher_genus_complementarity.tex:90:The conditionality in~(C2) is substantive:
chapters/theory/higher_genus_complementarity.tex:98:Koszul locus; the H-level Lagrangian upgrade~(C2) is the
chapters/theory/higher_genus_complementarity.tex:114:$\overline{\mathcal{M}}_g$ required by~(C2) is a stronger
chapters/theory/higher_genus_complementarity.tex:119:the natural geometric setting for the~(C2) upgrade.
chapters/theory/higher_genus_complementarity.tex:178:The Lagrangian upgrade~(C2) is the statement that the two
chapters/theory/higher_genus_complementarity.tex:441:(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
chapters/theory/higher_genus_complementarity.tex:1886:\label{sec:shifted-symplectic-complementarity}
chapters/theory/higher_genus_complementarity.tex:1899:\label{thm:shifted-symplectic-complementarity}
chapters/theory/higher_genus_complementarity.tex:2017:Theorem~\ref{thm:shifted-symplectic-complementarity} is a genus-$g$
chapters/theory/higher_genus_complementarity.tex:2029:\begin{proposition}[PTVV Lagrangian embedding; \ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:2095:Conditional on Theorem~\ref{thm:shifted-symplectic-complementarity},
chapters/theory/poincare_duality_quantum.tex:840:(Part of the MC2 theorem package; Theorem~\ref{thm:mc2-full-resolution}.)
chapters/theory/chiral_hochschild_koszul.tex:1827:(Part of the MC2 theorem package; Theorem~\ref{thm:mc2-full-resolution}.)
chapters/theory/chiral_hochschild_koszul.tex:1992:\begin{theorem}[MC2-1 for Kac--Moody algebras;
chapters/theory/chiral_hochschild_koszul.tex:1994:\index{MC2!Kac--Moody resolution}
chapters/theory/chiral_hochschild_koszul.tex:2184:$\widehat{\mathfrak{g}}_k$ at non-critical levels; all three MC2
 succeeded in 51ms:
   188	 (Theorem~\ref{thm:quantum-complementarity-main}).
   189	 For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ partition
   190	 functions decompose as
   191	 $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\mathcal{M}}_g, Z(\cA))$.
   192	 The Verdier involution sends $\Theta_\cA$ to $\Theta_{\cA^!}$,
   193	 and the two summands are complementary Lagrangians for the
   194	 Verdier-side shifted pairing; the ambient formal-moduli
   195	 upgrade is conditional on perfectness and nondegeneracy.
   196	\end{itemize}
   197	
   198	\noindent
   199	The organizing invariant is the \emph{critical discriminant}
   200	\begin{equation}\label{eq:concordance-discriminant}

thinking
**Considering Lagrangian perfectness**

I think I might need to read about prop:lagrangian-perfectness since it’s referenced by concordance, but maybe it's not strictly necessary. However, to assess the conflict between prop:ptvv-lagrangian and conditional opening, using prop:lagrangian-perfectness as a verifying standard could be helpful. It might indicate that a shifted-symplectic upgrade is generally conditional. I should inspect the proposition name more closely to understand its implications.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2890,2965p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2890	computation (Remark~\ref{rem:lagrangian-ptvv}) once the three
  2891	sub-hypotheses are verified. Global Lagrangian at the tangent level and
  2892	globally Lagrangian are equivalent when the derived intersection is
  2893	discrete.
  2894	
  2895	\emph{Verification for the standard landscape.}
  2896	Proposition~\ref{prop:lagrangian-perfectness} verifies
  2897	perfectness for the standard landscape at non-critical,
  2898	non-degenerate levels. The proof proceeds in four steps:
  2899	(1)~finite-dimensionality of the deformation complex at
  2900	each weight level (from~(P1));
  2901	(2)~chain-level nondegeneracy of the cyclic pairing
  2902	(the pairing on $\fg = \Defcyc^{\mathrm{mod}}(\cA)$ is
  2903	block-diagonal in the $(g,r)$-decomposition, and each block
  2904	is a convolution of nondegenerate pairings on finite-dimensional
  2905	spaces (the invariant form~(P2) and the cyclic
  2906	trace on the modular cooperad));
  2907	(3)~skew-adjointness of the differential with respect to the
  2908	pairing (a defining property of invariant pairings on dg~Lie
  2909	algebras);

thinking
**Identifying the center in cohomology**

I'm thinking about which theorem or definition should identify the center. In the foundations, line 4629 refers to the center local system as `H^0(End flat bar complex)` instead of `H^0(bar complex)`. There’s also a lemma about fiber-cohomology-center in the same file, proving that degree-0 fiber cohomology is the center. I believe Step 417-419 needs rephrasing to accurately describe surviving degree-0 fiber cohomology as it relates to the center, highlighting an important distinction. I need to pinpoint exact lines for corrections.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '920,1005p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   920	\begin{proof}[Proof of Lemma~\ref{lem:fiber-cohomology-center}]
   921	Fix a smooth curve $\Sigma_g$ of genus~$g$. The fiber of the bar
   922	complex at the moduli point $[\Sigma_g] \in \mathcal{M}_g$ is
   923	\begin{equation}\label{eq:fiber-bar-complex}
   924	\bar{B}^*_{\Sigma_g}(\mathcal{A})
   925	= \bigoplus_{n \geq 0}
   926	 \Gamma\bigl(\overline{C}_n(\Sigma_g),\,
   927	 \mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log}\bigr),
   928	\end{equation}
   929	with differential $d = d_{\mathrm{coll}} + d_{\mathrm{curv}}$
   930	(collision residues plus curvature corrections).
   931	
   932	The proof proceeds in four steps: identify degree-$0$ cocycles with
   933	the center (Steps~1--2), verify constancy over moduli (Step~3), then
   934	show vanishing of all higher fiber cohomology (Step~4).
   935	
   936	\emph{Step 1: Degree-$0$ identification.}
   937	The bar-degree-$0$ component is
   938	$\bar{B}^0_{\Sigma_g}(\mathcal{A}) = \mathcal{A}$
   939	(the algebra on $\Sigma_g$ with no configuration space insertions).



thinking
**Considering complementarity theorem nuances**

I'm looking into the complementarity theorem and lemmas involving linear algebra on a vector space V. It seems finite dimensionality isn't strictly necessary for decomposition, especially in infinite-dimensional spaces. However, the details around Lagrangian maximal isotropic setups are more intricate. The user mentioned hidden perfectness assumptions, possibly regarding hidden finite dimensionality. I notice that dimension statements in the theorems might need clarity about whether they require weight-wise finite dimensionality. Removing "finite-dimensional vector space" from the statement could simplify this. It's a subtle distinction!
thinking
**Examining Verdier duality implications**

I see a potential issue with Proposition 1803, specifically around lines 1810-1820, which states that Verdier duality on a central local system induces a non-degenerate bilinear pairing on \( V \otimes V \). I need to think critically about the implications of this claim and whether it holds under the stated conditions. It’s important for me to ensure that the reasoning behind this assertion is sound and accurately reflects the intended mathematical principles.
thinking
**Evaluating foundational statements**

I’m considering if there are statements in the foundations that summarize the concepts of complementarity, especially distinguishing between unconditional and conditional aspects. I think it would be helpful to read around sections 4150-4190 to gather insights on this. It seems like that could provide a clearer understanding. Let's explore those sections together to see what they reveal about these concepts. It’s always interesting to dive deeper!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4148,4195p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4148	\[
  4149	F_1(\cA) = \kappa(\cA)\cdot\lambda_1^{FP} = \frac{\kappa(\cA)}{24},
  4150	\]
  4151	satisfies $\Dg{1}^{\,2} = 0$ by the same cancellation mechanism as in
  4152	Theorem~\textup{\ref{thm:genus1-d-squared}}.
  4153	
  4154	Explicit values for the standard landscape:
  4155	\begin{center}
  4156	\begin{tabular}{lcccc}
  4157	\toprule
  4158	$\cA$ & $\kappa(\cA)$ & $\kappa(\cA^!)$ & $\kappa + \kappa^!$ & $F_1(\cA)$ \textup{(g=1 only; all-weight at g=1 is unconditional)} \\
  4159	\midrule
  4160	$\mathcal{H}_\kappa$ & $\kappa$ & $-\kappa$ & $0$ & $\kappa/24$ \\
  4161	$\widehat{\mathfrak{sl}}_2$ level $k$ & $\tfrac{3(k+2)}{4}$ & $-\tfrac{3(k+2)}{4}$ & $0$ & $\tfrac{k+2}{32}$ \\
  4162	$\mathrm{Vir}_c$ & $c/2$ & $(26-c)/2$ & $13$ & $c/48$ \\
  4163	$\mathcal{W}_3$ charge $c$ & $5c/6$ & $5(100-c)/6$ & $250/3$ & $5c/144$ \\
  4164	$bc_\lambda$ & $c_{bc}/2$ & --- & --- & $c_{bc}/48$ \\
  4165	\bottomrule
  4166	\end{tabular}
  4167	\end{center}
exec
/bin/zsh -lc "rg -n 'label\\{thm:deformation-obstruction\\}|thm:deformation-obstruction' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_curved.tex:6433:(Theorem~\ref{thm:deformation-obstruction}); homotopy nilpotence
chapters/theory/higher_genus_foundations.tex:6195:as stated in Theorem~\ref{thm:deformation-obstruction}.
chapters/theory/higher_genus_foundations.tex:6195:as stated in Theorem~\ref{thm:deformation-obstruction}.
chapters/theory/cobar_construction.tex:3058:\begin{theorem}[Quantum deformation-obstruction complementarity; \ClaimStatusProvedElsewhere]\label{thm:deformation-obstruction}

thinking
**Inspecting theorem relationships**

I need to read that theorem to check for consistency, but maybe it’s not necessary. I’m considering if it’s related to the deformation-obstruction theorem or the cobar construction. Since the user is asking about the seam between foundations and complementarity, if there’s a local theorem within foundations that's stronger than the main complementarity one, that might still create a seam issue. I really need to inspect the cobar construction theorem for clarity.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3040,3088p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3040	 distinction of Remark~\ref{rem:cobar-three-functors}.
  3041	\item Vertical double arrow: Koszul duality as an operation on
  3042	 algebras (exists only for Koszul pairs).
  3043	\item Diagonal arrow $\Omega$: cobar reconstruction; the inversion
  3044	 $\Omega(\bar{B}(\mathcal{A}_i)) \simeq \mathcal{A}_i$
  3045	 (Corollary~\ref{cor:bar-cobar-inverse}). This is the round-trip,
  3046	 not a map to $\mathcal{A}_{3-i}^!$.
  3047	\end{itemize}
  3048	
  3049	\subsection{Examples illustrating the distinction}
  3050	
  3051	\begin{example}[Heisenberg: level shift required]\label{ex:heisenberg-koszul-vs-barcobar}
  3052	Bar-cobar inversion gives $\Omega(\bar{B}(\mathcal{H}_k)) \simeq \mathcal{H}_k$ automatically, while Koszul duality yields $\mathcal{H}_k^! \simeq \mathrm{Sym}^{\mathrm{ch}}(V^*)$ with curvature $m_0 = -k\,\omega$ (cf.\ \S\ref{sec:heisenberg-koszul}). These are distinct statements: bar-cobar inverts $\mathcal{H}_k$, but the Koszul dual is a different type of algebra (commutative vs.\ Lie). See Part~\ref{part:characteristic-datum}.
  3053	\end{example}
  3054	
  3055	\section{Curved Koszul duality and quantum obstructions}
  3056	\label{sec:curved-koszul-quantum}
  3057	
  3058	\begin{theorem}[Quantum deformation-obstruction complementarity; \ClaimStatusProvedElsewhere]\label{thm:deformation-obstruction}
  3059	\textup{[Regime: curved-central on the Koszul locus; all genera


thinking
**Considering audit reporting**

I need to make sure that for audit findings, I’m including both the source and supporting dependencies, formatted correctly according to the user’s instructions. The format specifies `[SEVERITY] file:line — PROBLEM: ... FIX: ...`, and I should list the exact line numbers especially if there’s an issue with citations. If needed, I could use `sed` to provide precise context, ensuring rigorous verification. There's a potential issue with the theorem's proof that I need to address.
thinking
**Inspecting theorem foundations**

I'm thinking I need to inspect the foundations theorem around 6179 related to observation-definitive pairing, and maybe also check the theorem around 500. I wonder if there's a stale theorem label or a mismatch with complementarity. The theorem states it relates back to Theorem 1 on deformation obstruction, not the main complementarity. It seems that the foundations still might contain an independent proof via Serre duality, which could bypass certain conditions. I should verify if the theorem label or status appears in the theorem registry as proved. So, I’ll search for that.
exec
/bin/zsh -lc "rg -n 'obs-def-pairing-explicit|Theorem~\\\\ref\\{thm:deformation-obstruction\\}|Obstruction-deformation pairing' metadata/theorem_registry.md chapters/theory/higher_genus_foundations.tex chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/cobar_construction.tex:3261:\begin{lemma}[Obstruction-deformation pairing; \ClaimStatusProvedHere]\label{lem:obs-def-pairing}
chapters/theory/higher_genus_foundations.tex:6179:\begin{theorem}[Obstruction-deformation pairing; \ClaimStatusProvedHere]\label{thm:obs-def-pairing-explicit}
chapters/theory/higher_genus_foundations.tex:6195:as stated in Theorem~\ref{thm:deformation-obstruction}.
chapters/theory/higher_genus_foundations.tex:6272:\textup{(}Theorem~\ref{thm:obs-def-pairing-explicit}\textup{)} to have
metadata/theorem_registry.md:523:| `lem:obs-def-pairing` | `lemma` | 3262 | Obstruction-deformation pairing |
metadata/theorem_registry.md:838:| `thm:obs-def-pairing-explicit` | `theorem` | 6112 | Obstruction-deformation pairing |
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3250,3290p'" in /Users/raeez/chiral-bar-cobar succeeded in 63ms:
  3250	= H^1(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathcal{A}^!))
  3251	\hookrightarrow H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathcal{A})).
  3252	\]
  3253	\emph{(Note: One must use the local system $\mathcal{Z}(\mathcal{A})$,
  3254	not the trivial local system. By Harer's theorem,
  3255	$H^1(\mathcal{M}_g, \mathbb{Q}) = 0$ for $g \geq 2$, so the
  3256	deformation space would be trivially zero with trivial coefficients.)}
  3257	\end{proof}
  3258	
  3259	\emph{Step 4: Perfect Pairing}
  3260	
  3261	\begin{lemma}[Obstruction-deformation pairing; \ClaimStatusProvedHere]\label{lem:obs-def-pairing}
  3262	There is a perfect pairing:
  3263	\[\langle -, - \rangle: Q_g(\mathcal{A}) \otimes Q_g(\mathcal{A}^!) \to
  3264	H^{3g-3}(\overline{\mathcal{M}}_g, \mathbb{C})\]
  3265	given by the trace:
  3266	\[\langle \mathrm{Obs}, \mathrm{Def} \rangle = \mathrm{Tr}(\mathrm{Obs} \circ \mathrm{Def}).\]
  3267	\end{lemma}
  3268	
  3269	\begin{proof}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6245,6280p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6245	\emph{Note:} The deformation degree is $4g - 6$.
  6246	At $g = 1$, $4g - 6 = -2 < 0$, so $\text{def}_1 = 0$:
  6247	the genus-$1$ obstruction is uncompensated.
  6248	At $g = 2$, $\text{def}_2 \in H^2(\overline{\mathcal{M}}_2)$
  6249	(a $3$-dimensional space).
  6250	At $g = 3$, $\text{def}_3 \in H^6(\overline{\mathcal{M}}_3) = H^{\mathrm{top}} \cong \mathbb{C}$, so the deformation is a scalar.
  6251	For $g \geq 2$, the Poincar\'e duality pairing couples
  6252	$\text{obs}_g$ with $\text{def}_g$:
  6253	\begin{align}
  6254	\langle \text{obs}_g, \text{def}_g \rangle &= \int_{\mathcal{M}_g} (\kappa \cdot \lambda_g)
  6255	\qquad \cup (\kappa^{-1} \cdot \lambda_{g-3}^*) \\
  6256	&= \int_{\mathcal{M}_g} \lambda_g \cup \lambda_{g-3}^* \quad (g \geq 4)
  6257	\end{align}
  6258	\end{example}
  6259	
  6260	\begin{remark}[Hodge filtration compatibility]\label{rem:hodge-filtration}
  6261	\index{Hodge filtration!bar complex}
  6262	On the proved scalar lane, the factorization
  6263	$\mathrm{obs}_g = \kappa \cdot \lambda_g$ \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} is
  6264	compatible with the Hodge filtration on
exec
/bin/zsh -lc "rg -n 'Q_g\\(\\\\mathcal\\{A\\}\\"'^!'"\\)|Q_g\\(\\\\cA\\"'^!'"\\)|Q_1\\(|deformation space|obstruction-deformation pairing|complementarity' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
130:differential~$\dfib$ (Section~\ref{sec:complementarity-theorem}), the
4168:In every case, complementarity $\kappa(\cA) + \kappa(\cA^!) = \mathrm{const}$
4170:Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
4187:The complementarity column follows from Theorem~\ref{thm:quantum-complementarity-main}
4947:The sign reversal is consistent with Main~Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}; the Kodaira--Spencer construction of Theorem~\ref{thm:kodaira-spencer-chiral-complete} provides the geometric mechanism):
4949:sees as the negative obstruction, confirming deformation-obstruction complementarity.
5329:$K = c(\mathcal{A}) + c(\mathcal{A}^!)$ is the complementarity constant
5330:(Remark~\ref{rem:vir-vs-km-complementarity}) and
5356:curvature $m_0 = -\kappa$. The complementarity constant $c + c'$ is not defined
5900:\begin{corollary}[Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)}; \ClaimStatusProvedHere]
5902:\index{obstruction coefficient!W-algebra complementarity}
5903:For the principal $\mathcal{W}$-algebra $\mathcal{W}_N = \mathcal{W}^k(\mathfrak{sl}_N)$, the obstruction complementarity sum is
6176:\subsection{Connection to deformation-obstruction complementarity}
6186:pairs with the deformation space $Q_g(\mathcal{A}^!)$ via
6193:\[Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g, 
6271:constrains the deformation space $Q_g(\cA^!)$
7212:(Theorem~\ref{thm:genus-universality}), complementarity
7213:(Theorem~\ref{thm:quantum-complementarity-main}), and the
7215:(Theorem~\ref{thm:lagrangian-complementarity}),

thinking
**Inspecting theorem references**

I think I need to check the section starting around line 121, especially since it references the complementarity theorem. The search only returned a few results, which seems odd. There might be a potential issue at line 7215 where it mentions Theorem\ref{thm:lagrangian-complementarity}—maybe that label doesn't exist? I should check the introduction as well to see if I can find any clues. Let's dig into that!
exec
/bin/zsh -lc "rg -n 'label\\{thm:lagrangian-complementarity\\}|thm:lagrangian-complementarity' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:1882:sense (Theorem~\ref{thm:lagrangian-complementarity}).
chapters/theory/higher_genus_foundations.tex:7215:(Theorem~\ref{thm:lagrangian-complementarity}),
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '7208,7218p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7208	 system, connecting quantum chiral homology to arithmetic
  7209	 geometry.
  7210	\end{enumerate}
  7211	Together with genus universality
  7212	(Theorem~\ref{thm:genus-universality}), complementarity
  7213	(Theorem~\ref{thm:quantum-complementarity-main}), and the
  7214	Lagrangian polarization
  7215	(Theorem~\ref{thm:lagrangian-complementarity}),
  7216	these pillars form the complete structural theory of quantum chiral
  7217	homology at all genera.
  7218	\end{remark}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1874,1884p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1874	
  1875	\begin{remark}[Lagrangian interpretation of complementarity]\label{rem:lagrangian-complementarity}
  1876	\index{Lagrangian!complementarity}
  1877	The decomposition of
  1878	Theorem~\ref{thm:quantum-complementarity-main} is a Lagrangian
  1879	polarization: $Q_g(\cA)$ and $Q_g(\cA^!)$ are complementary
  1880	Lagrangians for the Verdier pairing.
  1881	This extends to a $(-1)$-shifted symplectic structure in the PTVV
  1882	sense (Theorem~\ref{thm:lagrangian-complementarity}).
  1883	\end{remark}
  1884	

thinking
**Exploring C0 in C2 Considerations**

I'm pondering whether there's a potential gap in the direct application of C0 within the C2 ambient shifted symplectic proposition for 2029. This proposition looks to define \(C_g=RΓ(...)\) explicitly. It creates an interesting space for investigation, making me want to dive deeper into the implications and explore how these concepts connect. There’s certainly a lot to unpack here, and it'd be worthwhile to examine how these elements interplay!
codex
A more structural seam mismatch is emerging in Step I of complementarity: the spectral-sequence proof switches from the universal configuration family used in `higher_genus_foundations.tex` to a fake product `\overline C_n(X)\times \overline M_g`. I’m checking whether that shortcut is just expositional or actually breaks the argument.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2748,2818p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3688,3715p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '731,788p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2748	
  2749	\begin{remark}[Dimension count]
  2750	\label{rem:dimension-higher-genus}
  2751	The configuration space has complex dimension:
  2752	\begin{equation}
  2753	\dim_{\mathbb{C}} C_n(\Sigma_g) = n \cdot \dim \Sigma_g = n
  2754	\end{equation}
  2755	However, we must account for the moduli:
  2756	\begin{equation}
  2757	\dim_{\mathbb{C}} \overline{\mathcal{M}}_{g,n} = 3g - 3 + n
  2758	\end{equation}
  2759	The universal family over $\overline{\mathcal{M}}_g$ with fiber $\overline{C}_n(\Sigma_g)$ has total dimension $(3g-3) + n$, which equals $\dim \overline{\mathcal{M}}_{g,n}$. Indeed, $\overline{\mathcal{M}}_{g,n}$ can be identified with this universal configuration space.
  2760	\end{remark}
  2761	
  2762	\subsection{\texorpdfstring{The moduli space $\overline{\mathcal{M}}_{g,n}$}{The moduli space M-g,n}}
  2763	
  2764	\begin{definition}[Deligne--Mumford compactification]
  2765	\label{def:deligne-mumford-compactification}
  2766	\index{Deligne--Mumford compactification|textbf}
  2767	\index{moduli space!of curves|textbf}
 succeeded in 51ms:
   731	For each genus~$g$, the Leray spectral sequence for the fibration
   732	below converges to $H^{p+q}(\bar{B}^{(g)}(\mathcal{A}))$;
   733	the genus filtration on the total bar complex
   734	$\bar{B}(\mathcal{A}) = \bigoplus_g \bar{B}^{(g)}(\mathcal{A})$
   735	then assembles these into the stated spectral sequence
   736	with target~$H^{p+q}(\bar{B}(\mathcal{A}), d_{\mathrm{total}})$.
   737	
   738	The Leray spectral sequence is applied to the fibration:
   739	\begin{equation}
   740	\begin{tikzcd}
   741	\overline{C}_n(X) \times \overline{\mathcal{M}}_g \arrow[d, "\pi"] \\
   742	\overline{\mathcal{M}}_g
   743	\end{tikzcd}
   744	\end{equation}
   745	
   746	\emph{$E_1$~page.}
   747	By definition, $E_1^{p,q,g}$ is the cohomology
   748	of the fiber complex.
   749	The fiber over
   750	$[(\Sigma_g;\allowbreak p_1, \ldots, p_n)]$ is:
 succeeded in 52ms:
  3688	\end{align}
  3689	\end{theorem}
  3690	
  3691	\begin{proof}[Proof via spectral sequence]
  3692	Consider the Leray spectral sequence for the universal configuration space fibration:
  3693	\begin{equation}
  3694	\pi: \overline{\mathcal{C}}_{g,n} \to \overline{\mathcal{M}}_{g}
  3695	\end{equation}
  3696	where $\overline{\mathcal{C}}_{g,n}$ is the relative Fulton--MacPherson compactification of $n$ points on the universal curve over~$\overline{\mathcal{M}}_g$. The fiber over $[\Sigma_g] \in \overline{\mathcal{M}}_g$ is $\overline{C}_n(\Sigma_g)$.
  3697	
  3698	\emph{Step 1: Fiberwise differential.} On each fiber $\overline{C}_n(\Sigma_g)$, the differential $d^{(0)}$ is the genus-zero bar differential using residues at collision divisors. By Theorem~\ref{thm:bar-nilpotency-complete}, $(d^{(0)})^2 = 0$.
  3699	
  3700	\emph{Step 2: Base contributions.} The differential $d^{(1)}$ arises from the Gauss--Manin connection on the local system $R^q\pi_*(\mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log})$ over $\overline{\mathcal{M}}_g$. The compatibility $\{d^{(0)}, d^{(1)}\} = 0$ follows from flatness of the Gauss--Manin connection (Stokes' theorem applied fiberwise).
  3701	
  3702	\emph{Step 3: Higher corrections.} Terms $d^{(k)}$ for $k \geq 2$ arise from the Leray filtration: $d^{(k)}$ maps $F^p \to F^{p+k}$ in the filtration by base degree. The relations ensuring $\Dg{g}^{\,2} = 0$ (e.g., $\{d^{(0)}, d^{(2)}\} + (d^{(1)})^2 = 0$) follow from the associativity of the Leray filtration and the exactness of the total complex.
  3703	\end{proof}
  3704	
  3705	\begin{remark}[Leray decomposition and Convention~\ref{conv:higher-genus-differentials}]
  3706	\label{rem:differential-notation}
  3707	\index{bar differential!notation}


thinking
**Analyzing the differential issue**

Line 929 involves a fiber bar complex with a differential represented as `d = d_coll + d_curv`. If `d_curv` induces curvature, then \(d^2 \neq 0\), which makes the statements in lines 961-965 about \(H^0 = \ker d / im d\) invalid. It seems the lemma proof filters by bar degree while using associated graded, which raises concerns. I'll need to check line 929 and context within higher genus foundations because the fiberwise differential appears to be curved. This could cause foundational issues with the theorem and lemma.
thinking
**Exploring uncurving chain concepts**

I'm considering how to label the topic of uncurved comparison complex, especially around proposition 4613. It might help to explicitly state, "We work on the uncurved comparison complex whose differential squares to zero." I also need to identify the curvature term after recognizing the obstruction class. I'll search for the proposition label related to uncurving chain, possibly looking into foundations or complementarity. A search like `gauss-manin-uncurving-chain` could be beneficial.
codex
This is the sharpest seam failure so far: the complementarity chapter computes fiber cohomology with `d_fiber` as if it were a genuine differential, but the foundations chapter defines the genus-`g` fiber differential to be curved, with `d_fib^2 = κ(A)·ω_g`. I’m tracing whether the chapter ever switches to the strict flat comparison model; if not, the whole Step I/C0 setup is stated on the wrong complex.
exec
/bin/zsh -lc "rg -n 'gauss-manin-uncurving-chain|uncurving|Dg\\{|\\\\Dg\\{g\\}|fiberwise curved differential|d_\\{\\mathrm\\{fib\\}\\}\\"'^'"\\{\\\\,2\\\\}|d_\\{\\mathrm\\{fiber\\}\\}\\"'^2|curved differential|flat model'"' chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4540,4650p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '904,968p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  4540	\index{Faber--Pandharipande formula}
  4541	The top $\lambda$-class, paired with the appropriate $\psi$-class, evaluates to \textup{(LOCAL)}:
  4542	\begin{equation}\label{eq:faber-pandharipande}
  4543	\int_{\overline{\mathcal{M}}_{g,1}} \psi_1^{2g-2}\,\lambda_g = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}
  4544	\end{equation}
  4545	where $B_{2g}$ are Bernoulli numbers~\cite{FP03}. The integrand has degree $(2g-2)+g = 3g-2 = \dim\overline{\mathcal{M}}_{g,1}$. At $g = 1$: $\frac{1}{2} \cdot \frac{1/6}{2} = \frac{1}{24}$; at $g = 2$: $\frac{7}{8} \cdot \frac{1/30}{24} = \frac{7}{5760}$ \textup{(LOCAL)}.
  4546	\end{theorem}
  4547	
  4548	\begin{remark}[Imported-proof dependency tags]
  4549	\emph{Dependency tags.}
  4550	\begin{enumerate}[label=(D\arabic*)]
  4551	\item The class-theoretic setup is provided by
  4552	Theorem~\ref{thm:mmm-classes} and Definition~\ref{def:hodge-bundle}.
  4553	\item The closed-form Bernoulli expression is imported from the external
  4554	tautological-ring literature (see~\cite{Mumford83}).
  4555	\item In this manuscript, the formula is used as input to obstruction and
  4556	quantum-correction bookkeeping (e.g. Theorem~\ref{thm:obstruction-general}).
  4557	\end{enumerate}
  4558	\emph{Provenance note.}
  4559	This claim is used in this manuscript as an external theorem, proved in
 exited 2 in 52ms:
rg: regex parse error:
    (?:gauss-manin-uncurving-chain|uncurving|Dg\{|\\Dg\{g\}|fiberwise curved differential|d_\{\mathrm\{fib\}\}\^\{\\,2\\}|d_\{\mathrm\{fiber\}\}\^2|curved differential|flat model)
                                                                                              ^^
error: unrecognized escape sequence
 succeeded in 55ms:
   904	\emph{Step 4: Identify fiber cohomology with center.}
   905	
   906	\begin{lemma}[Fiber cohomology and center; \ClaimStatusProvedHere]
   907	\label{lem:fiber-cohomology-center}
   908	For a Koszul chiral algebra~$\mathcal{A}$
   909	\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})},
   910	the fiber cohomology sheaf over the smooth
   911	locus~$\overline{\mathcal{M}}_g^{\mathrm{sm}}$ satisfies:
   912	\begin{equation}
   913	\mathcal{H}^*_{\mathrm{fiber}}(\mathcal{A})
   914	\big|_{\overline{\mathcal{M}}_g^{\mathrm{sm}}}
   915	\cong Z(\mathcal{A}) \otimes \underline{\mathbb{C}}
   916	\end{equation}
   917	where $\underline{\mathbb{C}}$ is the constant sheaf.
   918	\end{lemma}
   919	
   920	\begin{proof}[Proof of Lemma~\ref{lem:fiber-cohomology-center}]
   921	Fix a smooth curve $\Sigma_g$ of genus~$g$. The fiber of the bar
   922	complex at the moduli point $[\Sigma_g] \in \mathcal{M}_g$ is
   923	\begin{equation}\label{eq:fiber-bar-complex}


thinking
**Evaluating findings and definitions**

I’m noticing multiple findings related to the same issue, possibly at lines 706 and 929. It might make sense to combine them but keep both file:line references. For instance, I could label one as [CRITICAL] higher_genus_complementarity.tex:706 and describe the 929 reference. There’s a potential issue with the foundations theorem 4565, which defines the center local system as H^0 of the endomorphism sheaf of a complex, while the complementarity chapter just references it directly.
thinking
**Evaluating structural findings**

I’m contemplating whether to separate findings due to distinct structural errors or combine them. It seems better to keep them separate, with one finding for wrong fiberation and another for the wrong differential. There’s a potential issue because line 761 uses Theorem `arnold-three` to justify that d_fiber^2=0, while line 2867 says the genus1 Arnold relation needs a correction, leading to a direct contradiction. I should inspect the specific details in line 2867.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2862,2872p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2862	\begin{theorem}[Quantum-corrected Arnold relations; \ClaimStatusProvedHere]
  2863	\label{thm:quantum-arnold-relations}
  2864	\label{thm:arnold-higher-genus}
  2865	\label{thm:arnold-quantum}
  2866	\index{Arnold relations!higher genus}
  2867	At genus~$0$, the Arnold relation $\mathcal{A}_3^{(0)} = 0$ was the mechanism ensuring $\dzero^2 = 0$ in the Heisenberg bar complex (\S\ref{sec:frame-bar-deg2}). At genus~$1$, the Arnold $3$-form acquires a correction proportional to the volume form; this is the geometric origin of the fiberwise curvature $\dfib^{\,2} = \kappa \cdot \omega_1$ that we computed in~\S\ref{sec:frame-genus1}.
  2868	
  2869	Define the Arnold 3-form:
  2870	\begin{equation}
  2871	\mathcal{A}_3^{(g)} = \eta_{12}^{(g)} \wedge \eta_{23}^{(g)} + \eta_{23}^{(g)} \wedge \eta_{31}^{(g)} + \eta_{31}^{(g)} \wedge \eta_{12}^{(g)}
  2872	\end{equation}


thinking
**Investigating mathematical definitions**

I'm thinking about whether the complementarity file defines `\bar B^{(g)}(\A)` as strict or flat. I want to search for higher-genus-differentials, but I’m not sure if they'll be in the file. Sections 261-276 seem to define relative bar fiber complex with a fiberwise curved differential, which points to something. However, there's a potential issue because theorem 1257 in the KS map theorem discusses `R^q \pi_*^{ch} A` with a GM connection, which isn't obviously the same as the center local system. This might lead to wrong identification.
thinking
**Analyzing mathematical structures**

I want to confirm some details. On line 734, about genus filtration, using a direct sum might work if we're only considering finite genus contributions. However, the foundations define the full bar object as a product. Since spectral sequences differ between direct sums and products, especially with infinite genus contributions, there may be a hidden assumption about completion. This could be subtle. I realize we have many solid findings already, but the theorem on lines 481-483 is an interesting potential issue.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4706,4716p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  4706	$A_{\mathrm{mod}}$ & Bar-cobar intertwined with Verdier, & \textbf{Proved} & Thm~\ref{thm:bar-cobar-isomorphism-main} \\
  4707	 & functorial over $\overline{\mathcal{M}}_{g,n}$ & & \\[2pt]
  4708	$B_{\mathrm{mod}}$ & Inversion on Koszul locus; coderived & Proved on Koszul locus; & Thm~\ref{thm:higher-genus-inversion}, \\
  4709	 & persistence off it & coderived persistence conjectural & \S\ref{subsec:coderived-ran} \\[2pt]
  4710	$C_{\mathrm{mod}}$ & Shifted symplectic complementarity & \textbf{Proved} & Thms~\ref{thm:quantum-complementarity-main}, \\
  4711	 & (PTVV Lagrangian embedding) & & \ref{thm:ambient-complementarity-fmp} \\[2pt]
  4712	Index & GRR: scalar genus series $= \kappa(\cA) \cdot (\hat{A}(ix) - 1)$; genus-$1$ unconditional & \textbf{Proved} & Thm~\ref{thm:family-index} \\[2pt]
  4713	DK & DK-0/1/$1\frac{1}{2}$: chain-level, eval-locus, lattice; & DK-0/1/$1\frac{1}{2}$: proved (all types); & Thms~\ref{thm:derived-dk-affine}, \\
  4714	 & DK-2/3: generated-core DK comparison; & DK-2/3: \textbf{proved} (eval-gen.\ core, all types; $\mathcal{O}_{\mathrm{poly}}$ only on the separate type-$A$ thick-generation lane; & \ref{thm:derived-dk-yangian}, \ref{thm:factorization-dk-eval}, \\
  4715	 & DK-4/5: dg-shifted/triple bridge & uses Molev PBW \cite{molev-yangians}); DK-4: ML proved, alg.\ id.\ open; DK-5: \textbf{proved for $\mathfrak{sl}_2$} (FRT, Prop.~\ref{prop:dk5-sl2-frt}); general: conj. & \ref{conj:dk-fd-typeA}, \ref{cor:dk23-all-types}, \ref{thm:rtt-mittag-leffler}; Conj.~\ref{conj:full-dk-bridge} \\[2pt]
  4716	$H$ & Chiral Hochschild: $\ChirHoch^n = 0$ for $n > 2$, $P(t) = 1+t^2$; & \textbf{Proved} (generic level, & Thms~\ref{thm:w-algebra-hochschild}, \\

thinking
**Searching for label clarity**

I'm looking into a potential mismatch in the references. The concordance mentions "shifted symplectic complementarity" and cites `thm:ambient-complementarity-fmp`, but it doesn’t seem to align with either `prop:ptvv-lagrangian` or `thm:shifted-symplectic-complementarity`. It could be considered an outside seam, so I want to search specifically for the label `thm:ambient-complementarity-fmp` to clarify what's going on here and resolve any confusion.
exec
/bin/zsh -lc "rg -n 'label\\{thm:ambient-complementarity-fmp\\}|ambient-complementarity-fmp' chapters/theory/higher_genus_complementarity.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:2324:(Theorem~\ref{thm:ambient-complementarity-fmp})
chapters/theory/higher_genus_complementarity.tex:2094:Theorem~\ref{thm:ambient-complementarity-fmp}).
chapters/theory/higher_genus_complementarity.tex:4673:\label{thm:ambient-complementarity-fmp}
chapters/theory/bar_cobar_adjunction_inversion.tex:2819:Theorem~\ref{thm:ambient-complementarity-fmp}) equips the modular
chapters/theory/bar_cobar_adjunction_inversion.tex:2831:Theorem~\textup{\ref{thm:ambient-complementarity-fmp})}, and the
chapters/theory/bar_cobar_adjunction_inversion.tex:2851:(Theorem~\ref{thm:ambient-complementarity-fmp}) makes them
chapters/theory/bar_cobar_adjunction_inversion.tex:2887:(Theorem~\ref{thm:ambient-complementarity-fmp}) is proved
chapters/theory/higher_genus_complementarity.tex:2094:Theorem~\ref{thm:ambient-complementarity-fmp}).
chapters/theory/higher_genus_complementarity.tex:4673:\label{thm:ambient-complementarity-fmp}
chapters/theory/higher_genus_modular_koszul.tex:516:Theorem~\textup{\ref{thm:ambient-complementarity-fmp})}.
chapters/theory/higher_genus_modular_koszul.tex:30155:(Theorem~\ref{thm:ambient-complementarity-fmp})

thinking
**Exploring complementarity theorems**

I'm thinking that the prop:ptvv-lagrangian isn't the only ambient complementarity theorem out there. There's a later theorem 4673 that I might need to look into as well. I wonder what makes it different or relevant in the context of this conversation. Let me inspect around theorem 4673 to see if it adds any helpful insights or understanding to what I'm currently considering. It could be significant!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4658,4715p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4658	pairing reduces to the quadratic term in the differentiated
  4659	Maurer--Cartan equation for the universal kernel. That quadratic term
  4660	vanishes because the Maurer--Cartan equation is exactly the isotropy
  4661	condition for the graph of the one-sided variation. The same argument
  4662	applies to $T_{\cA^!}$.
  4663	
  4664	If the cyclic pairing is perfect and bar--cobar duality identifies the
  4665	normal complex to one side with the shifted dual tangent complex of the
  4666	other, maximal isotropicity follows. This is the derived form of the
  4667	slogan that the two sides are opposite polarizations of a single
  4668	symplectic deformation problem.
  4669	\end{proof}
  4670	
  4671	\begin{theorem}[Ambient complementarity as shifted symplectic formal
  4672	moduli problem]
  4673	\label{thm:ambient-complementarity-fmp}
  4674	\ClaimStatusProvedHere
  4675	Under the perfectness and nondegeneracy hypotheses of
  4676	Theorem~\textup{\ref{thm:ambient-complementarity-tangent}(iii)},
  4677	the tangent complex $T_{\mathrm{comp}}(\cA)$ integrates to a








thinking
**Evaluating technical findings**

I'm noticing a potential issue with the complementarity section, where it states that \(Q_g\) are Lagrangian subspaces of \(\mathbf{C}_g(\A)\), but they are actually cohomological shadows. I think it should be referred to as \(\mathbf{Q}_g\). Also, the theorem mentions Lagrangian subspaces, which is good. But I'm concerned about the details regarding the theorem's foundation and its use of filtered dg Lie algebra. I need to ensure I keep the findings concise, maybe around 8-10 key points for clarity.
thinking
**Evaluating summary details**

I’m trying to figure out the summary details. They want to know how many files were checked, and “Checked: N” seems ambiguous. It could mean the count of files or the seam surfaces. Maybe it’s clearer to say “Checked: 8,” suggesting we reviewed eight source files, but I need to ensure accuracy. I could say “Checked: 8 | Findings: 10 | Verdict: FAIL.” It’s essential to get this right!
thinking
**Grounding findings in evidence**

I need to ensure that every finding is backed by the content from the files I’ve read. We have line numbers from those files, and it might help to reference supporting lines in the dependency file. I should verify line numbers for findings D and H, especially since they might overlap. Combining them could clarify the critical issues about PTVV and the C2 naming. However, there may be merit in keeping them separate to highlight distinct mathematical overclaims and nomenclature mismatches.
thinking
**Deciding on separation of findings**

I believe it’s better to separate the findings for clarity. One can focus on the wrong family mentioned at line 738, while the other addresses the wrong differential noted at lines 761 and 929. This way, each issue is highlighted distinctly, making it easier for anyone reviewing the findings to understand the specific problems identified. I think clarity is key here!
thinking
**Refining findings summary**

I’m working with 10 findings summarized in one-liners, but I’m worried about making it too lengthy—maybe around 40 lines. I could incorporate extra points in descriptions to keep things concise. For instance, findings 7 and 9 might be combined since they address the 2029 prop and opening/concordance mismatch. However, I need to think about clarity versus detail. Perhaps simplifying to 9 findings by merging D/H into one critical point around 2029 and 441 could work.
thinking
**Considering improvements**

I'm thinking about using exchange involution on the direct sum, or maybe adding a valid separate center-comparison theorem. That might actually work better for what I'm trying to achieve. Including the 1488 detail could also serve as solid evidence. It’s a nice little boost for my reasoning! I'm glad I'm sorting through this. Let’s see how it all comes together.
thinking
**Fixing references and descriptions**

I’m working on finding entry 5 at 1335 and need to recheck the description, which also mentions entry 1571. Then there’s entry 6 at 2029; I need to look at the description again for specific lines 2054-2080 and 4671-4676 for the conditional theorem. It feels a bit chaotic, but I’m making a note to ensure everything is accurate. Let's get those references sorted out!
thinking
**Finalizing findings summary**

I need to clearly present the results, so I'll mention that I checked 7 files and found 9 findings, which led to a verdict of "FAIL." That should sum it up nicely! I think organizing this into 9 bullet points and around 45 lines will make the information clearer for the user. It feels good to have a structured approach to this! Let’s get to building that final summary.
codex
- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:738` — PROBLEM: Step I builds the Leray spectral sequence from `\overline{C}_n(X) \times \overline{\mathcal{M}}_g -> \overline{\mathcal{M}}_g`, but the fibers are then treated as varying `\overline{C}_n(\Sigma_g)`. This contradicts the foundations-side universal-family setup in `higher_genus_foundations.tex:2797-2814` and `:3692-3696`. FIX: replace the product diagram by the relative FM family `\pi:\overline{\mathcal{C}}_{g,n}\to\overline{\mathcal{M}}_g`, and rewrite the proof to use the universal configuration space throughout.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:706` — PROBLEM: The theorem states `E_1^{p,q,g}=H^q(\bar B_g^p(\mathcal A),d_{\mathrm{fiber}})`, and the proof at `:761-762` plus Lemma `lem:fiber-cohomology-center` at `:929-965` computes ordinary cohomology of the fiber differential. But the foundations chapter defines the fiber differential as curved, with `\dfib^2=\kappa(\mathcal A)\omega_g` (`higher_genus_foundations.tex:2867`, `:3712-3713`, `:4603-4606`). FIX: rewrite Step I, `lem:fiber-cohomology-center`, `lem:perfectness-criterion`, and `thm:fiber-center-identification` to use the strict flat comparison complex `(\bar B_{\mathrm{flat}}^{(g)}(\mathcal A),\Dg{g})` from `higher_genus_foundations.tex:4569-4617`; if the curved fiber model is kept, only use it after passing to the associated graded, where the `E_1` differential is `d_0`, not `\dfib`.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:414` — PROBLEM: C0 identifies the surviving fiber cohomology with `\bigoplus_p(\mathcal A^!)_p` and then with the center by citing `cor:bar-cohomology-koszul-dual`. But `chapters/theory/chiral_koszul_pairs.tex:924-949` only gives bar-cohomology/Koszul-dual-dimension comparison; it does not identify `H^0` with the center. This is an `A / B(A) / A^! / Z^{der}` conflation. FIX: replace Step 3 by the residue-kernel argument already given in `lem:fiber-cohomology-center:945-965`: identify `H^0` as `\ker(d:\bar B^0\to\bar B^1)=Z(\mathcal A|_\Sigma)`, then use that fiberwise identification in Step 4.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:195` — PROBLEM: `def:complementarity-complexes` asserts a cochain involution on `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))` from `thm:verdier-bar-cobar`, but that theorem is the genus-0 bar/cobar Verdier pairing in `chapters/theory/cobar_construction.tex:1312-1349`, not an involution on the ambient center complex. The later attempted repair via `lem:center-isomorphism` at `:1481-1506` also fails: `thm:e1-module-koszul-duality` in `chiral_koszul_pairs.tex:5174-5226` gives complete-module/bar-comodule equivalence, not an equivalence `\mathrm{Mod}_{\mathcal A}\simeq\mathrm{Mod}_{\mathcal A^!}` that would identify centers. FIX: do not define `\sigma` as a self-map on one ambient factor. Either move the definition after a valid center-comparison theorem, or redefine the ambient object as `R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))\oplus R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A^!))` with exchange involution `(x,y)\mapsto(\mathbb D y,\mathbb D x)`.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1335` — PROBLEM: Step 7 globalizes from the smooth-locus lemma `lem:fiber-cohomology-center` to `H^*(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))`, and Step 8 repeats the same move at `:1570-1585`. But that lemma only proves constancy on `\overline{\mathcal M}_g^{\mathrm{sm}}`; it does not justify the compactified global ambient complex used in C1. C0 is supposed to supply exactly this upgrade, but the proof does not use it. FIX: replace those citations by `thm:fiber-center-identification`, and insert the derived identification `R\pi_{g*}\bar B_{\mathrm{flat}}^{(g)}(\mathcal A)\simeq\mathcal Z_{\mathcal A}` concentrated in degree 0 on all of `\overline{\mathcal M}_g` before defining the KS action and the `q=0` spectral-sequence concentration.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:2029` — PROBLEM: `prop:ptvv-lagrangian` claims a shifted-symplectic structure on the cochain complex `C_g:=R\Gamma(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))`, but its proof uses `prop:lagrangian-eigenspaces`, which only constructs a pairing on cohomology `V=H^*(\overline{\mathcal M}_g,\mathcal Z(\mathcal A))` (`:1807-1827`). It then treats `Q_g(\mathcal A)` and `Q_g(\mathcal A^!)` as subcomplexes at `:2061-2080`, although they were defined as cohomology eigenspaces. This silently imports the chain-level perfectness/nondegeneracy hypotheses that the opening says are conditional, and it collides with the later conditional formal-moduli theorem at `:4671-4689`. FIX: either downgrade `prop:ptvv-lagrangian` to a conditional result with explicit hypotheses `C_g\simeq C_g^\vee[-(3g-3)]` and chain-level homotopy eigenspaces `\mathbf Q_g`, or weaken it to a cohomology-level Verdier-Lagrangian statement and stop presenting it as the proved ambient C2 upgrade.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:6179` — PROBLEM: `thm:obs-def-pairing-explicit` reproves complementarity by plain Serre/Poincaré duality, bypassing the Verdier involution, the center-comparison problem, and the perfectness/nondegeneracy boundary tracked in the complementarity chapter. Its example at `:6246-6247` concludes `\mathrm{def}_1=0`, which directly contradicts `higher_genus_complementarity.tex:154-161`, where `Q_1(\mathcal H_\kappa^!)=\mathbb C\cdot\lambda`. FIX: rewrite `thm:obs-def-pairing-explicit` as a corollary of `thm:quantum-complementarity-main` plus the Verdier-pairing result, and replace the genus-1 example by the explicit nonzero genus-1 split `Q_1(\mathcal H_\kappa)=\mathbb C\cdot\kappa`, `Q_1(\mathcal H_\kappa^!)=\mathbb C\cdot\lambda_1`.

- [MEDIUM] `chapters/theory/higher_genus_complementarity.tex:96` — PROBLEM: the prose says “C0 and C1 hold unconditionally on the Koszul locus,” but C0 as stated at `:360-365` additionally assumes finite-dimensional fiber cohomology, and C1 still depends on constructing a global Verdier/Koszul involution on the correct ambient object. FIX: rewrite this sentence to separate the actual hypothesis boundary, e.g. “C0 is proved on the Koszul locus under the finite-dimensional fiber-cohomology hypothesis of Theorem~\ref{thm:fiber-center-identification}; C1 then follows once the global Verdier/Koszul involution has been constructed; the shifted-symplectic upgrades require the extra perfectness/nondegeneracy hypotheses.”

- [LOW] `chapters/theory/higher_genus_complementarity.tex:1882` — PROBLEM: `thm:lagrangian-complementarity` does not exist; the same dead reference appears in `chapters/theory/higher_genus_foundations.tex:7215`. FIX: replace the reference with the intended live label. If the sentence means the proved PTVV ambient statement, use `\ref{prop:ptvv-lagrangian}`; if it means the conditional bar-side BV theorem, use `\ref{thm:shifted-symplectic-complementarity}`.

## Summary
Checked: 7 | Findings: 9 | Verdict: FAIL
tokens used
210,068
