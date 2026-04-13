# F14_hidden_imports_hg_found (580s)

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:357` — PROBLEM: the proved-here Gauss--Manin proposition is not well-typed. It defines `\nabla^{GM}` on `R^q\pi_*(\cA^{\boxtimes n}\otimes\Omega^*_{\log})` using fiber holomorphic differentials `\omega_k` as if they were base 1-forms, and uses `t_k=\oint_{A_k}\omega_k` as coordinates even though the chapter later normalizes `\oint_{A_l}\omega_k=\delta_{kl}`, so these `t_k` are constants. The proof then switches to the different local system `R^q\pi_*\C` and never returns to the stated bar-complex object. FIX: downgrade `prop:gauss-manin-uncurving-chain` to a local analytic remark on the symplectic-frame cover of Teichmuller space, replace `\omega_k\otimes\partial_{t_k}` by genuine local base coordinates `du_\mu\otimes\nabla_\mu`, and explicitly state that only the relative de Rham/Gauss--Manin package is proved here unless a bar-complex lift is constructed.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:404` — PROBLEM: part (iii) of the same proposition overclaims a derived/coderived comparison “in general,” but the cited support `thm:cobar-resolution-scoped` is explicitly Koszul-locus-only and does not supply a comparison functor `D^{co}\to D^b`. FIX: add the Koszul-locus hypothesis everywhere this comparison is used, or replace the sentence by “no general comparison is proved here; only the Koszul-locus bar-cobar counit is available.”

- [HIGH] `chapters/theory/higher_genus_foundations.tex:465` — PROBLEM: `\kappa(\cA):=\sum_a\langle e_a,e^a\rangle` is declared for an arbitrary cyclic chiral algebra with no trace-class/finite-weight hypothesis, so the displayed sum need not define a scalar on the stated input class. FIX: either add a finiteness hypothesis such as positive energy with finite-dimensional graded pieces and absolute convergence, or make `\Theta_\cA^{\le 2}` the primary definition and present the basis-sum only as a finite-type formula under that extra hypothesis.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:668` — PROBLEM: the chain-level curvature proposition jumps from `c_1(\mathbb E,h_{Ar})=\pi_*[\omega_g^{Ar}]` to `\kappa(\cA)\lambda_g=\kappa(\cA)c_g(\mathbb E)`. A single pushed-forward `(1,1)`-form gives a first Chern class, not the top Chern class `c_g` for `g>1`; the displayed “two-step Chern--Weil projection” does not prove the claimed `\lambda_g` statement. FIX: rewrite part (ii) to conclude only the `c_1(\mathbb E)` statement, and move the `\kappa(\cA)\lambda_g` identification to a forward reference to `thm:genus-universality`/`thm:family-index` rather than deriving it here.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:776` — PROBLEM: `D^{(g)}_\cA := d_0+\kappa(\cA)\omega_g` adds a degree-2 form to a degree-1 differential and then calls the result a differential. The follow-up sentence “at `g=1`, the correction `\kappa\omega_1` is the Fay trisecant identity” also confuses a curvature term with an identity. FIX: replace the proposition by the curvature equation `d_{fib}^2=\kappa(\cA)\omega_g` or by the already-used strict differential `\Dg{g}` with genuine degree-1 correction operators; do not write `d_0+\kappa\omega_g` as a differential.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:807` — PROBLEM: the “five-level hierarchy” theorem contradicts itself. It opens with “each level is strictly contained in the next,” but later says only `(iv)\subsetneq(iii)\subsetneq(ii)\subsetneq(i)` and explicitly says level `(v)` is not comparable with `(iii)`. FIX: rewrite the theorem statement to match the proof: “Levels (i)-(iv) form a strict descending chain of increasingly restrictive conditions; level (v) implies (iv), (ii), and (i), but is not comparable with (iii).”

- [HIGH] `chapters/theory/higher_genus_foundations.tex:863` — PROBLEM: level (v) attributes genus-`g` finite-dimensional conformal blocks and a modular functor to `Zhu96`, but the file provides no higher-genus source and no local proof. This is an unsupported status upgrade inside a proved-here theorem. FIX: either restrict level (v) to the genus-1 Zhu-algebra/modular-character statement, or replace the citation with the actual higher-genus modular-functor theorem and state its precise hypotheses.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:1061` — PROBLEM: the family-index preface asserts that the genus-`g` bar family defines a virtual `K`-class and immediately applies GRR to `\bar B(\cA)|_{fiber}` without proving perfectness, finite rank, or any base-change package for this family. FIX: recast this paragraph as a roadmap: “On the proved uniform-weight scalar lane, Theorem `thm:family-index` later replaces the full bar family by the scalar `K`-class `\mathcal D_\cA^{(g)}=\kappa(\cA)\mathbb E` and applies GRR there.”

- [HIGH] `chapters/theory/higher_genus_foundations.tex:1944` — PROBLEM: `thm:convergence-filtered` invents a “unique closed element in the `gr`-harmonic complement” and then claims the filtered spectral sequence also collapses at `E_2` merely because the associated-graded one does. Neither statement is proved. FIX: delete item (2) or replace it by a noncanonical splitting statement, and weaken Step 4 to a pure convergence/comparison claim unless you add an independent degree argument forcing higher differentials to vanish on the filtered complex itself.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:2004` — PROBLEM: the same theorem flatly identifies the Koszul dual algebra with the continuous dual of the bar coalgebra, `\cA^!:=\bar B(\cA)^\vee`. That is the barred object’s linear dual, not the Koszul dual defined in this programme. FIX: replace Step 5 by the four-object template: first define `\cA^i:=H^*(\bar B(\cA))`, then `\cA^!:=(\cA^i)^\vee`; if you need `\bar B(\cA)^\vee`, name it explicitly as the continuous dual of the bar coalgebra and stop calling it the Koszul dual.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:3746` — PROBLEM: `thm:concrete-quantum-differential` is still a placeholder disguised as a theorem. The operator `\delta_{\gamma^*}` is undefined, “virtual puncture” is undefined, and the proof cites “associativity of the Leray filtration” and “exactness of the total complex” instead of an actual construction. FIX: either define `d^{(1)}` and every `d^{(k)}` as concrete endomorphisms with domains/codomains and filtration behavior, or downgrade the whole theorem to a heuristic remark and keep only the already proved statements `\dfib^2=\kappa\omega_g` and `\Dg{g}^2=0`.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:4379` — PROBLEM: the genus spectral sequence is not built from a defined filtered complex. `F^k\bar B(\cA)=\bigoplus_{g\ge k}\bar B^{(g)}(\cA)` is only a direct sum of separate genus complexes; the section never constructs a single total complex with a differential preserving this filtration, and the proof later introduces a different “genus expansion” differential after the fact. FIX: first define a total genus-completed complex, e.g. `\bar B^{tot}(\cA)=\prod_{g\ge0}\hbar^{2g-2}\bar B^{(g)}(\cA)`, specify its differential, prove filtration preservation, and only then define the spectral sequence; otherwise delete the whole section.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:4449` — PROBLEM: the explicit `E_2`-page formula is mathematically unprepared: `\mathcal M_k` is undefined, `H^p(\mathcal M_1,\mathcal M_k\otimes H^q)=\bigoplus_k\mathcal M_k\otimes H^q` is asserted without any sheaf/local-system definition, and the subsequent identification of `d_2` with Kodaira--Spencer is simply announced. FIX: replace the displayed genus-1 formula by the abstract Leray expression `H^p(\mathcal M_g,\underline H^q)`, define the relevant local system if modular forms are really intended, and move the Kodaira--Spencer identification to a separate proposition with an actual proof.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:6089` — PROBLEM: `prop:bar-tautological-filtration` stacks three unsupported upgrades: it places `E_2` classes in the tautological ring merely from a VHS input, it calls `d_2` the Kodaira--Spencer map without constructing that identification, and it says `\psi_1\in H^1(\overline{\mathcal M}_{g,1})`, which is wrong even on the chapter’s own grading conventions. FIX: change the proposition to a cautious remark; replace `H^1` by `H^2` where `\psi_1` appears; and remove the tautological-ring and `d_3`/Massey-product claims unless you add separate proofs.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:6563` — PROBLEM: the loop-order filtration is descending, but `prop:loop-filtration-compatible` proves only `d_{FT}(F^\ell)\subset F^{\ell-1}`, not `d_{FT}(F^\ell)\subset F^\ell`. So the differential does not preserve the filtration, and `thm:loop-order-spectral-sequence` has no spectral sequence to talk about. FIX: reverse the filtration convention to an ascending filtration `F_\ell:=\bigoplus_{b_1(\Gamma)\le \ell}`, rewrite the associated graded and bidegrees accordingly, and then rederive `d_0`/`d_1` with the corrected indexing.

- [MEDIUM] `chapters/theory/higher_genus_foundations.tex:288` — PROBLEM: the chapter says `(\bar B^{(g)}(\cA),\dfib)` is a curved dg coalgebra in the coderived category, but later at `729-736` it says `\dfib` is not a coderivation of the deconcatenation coproduct. Those two claims are incompatible in the ordinary CDG-coalgebra sense. FIX: standardize the language: either prove coderivation, or replace every “curved dg coalgebra” claim here by the weaker terminology used in `chapters/theory/coderived_models.tex:193-210` (“filtered curved factorization model”).

- [LOW] `chapters/theory/higher_genus_foundations.tex:293` — PROBLEM: the chapter consistently cites `Appendix~\ref{app:coderived-models}`, but the actual live label in the coderived appendix is `sec:coderived-models` (`chapters/theory/coderived_models.tex:180`); `app:coderived-models` is only a phantom label in `main.tex`. FIX: replace `app:coderived-models` by `sec:coderived-models` at lines `293`, `407`, and `829`, or rename the appendix label once and use it consistently.

## Summary
Checked: 24 | Findings: 16 | Verdict: FAIL


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
session id: 019d83e2-811a-7021-a128-67789356abea
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


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_foundations.tex

Same: hidden imports. Especially for the genus-g fiber bar, spectral sequences, and base-change arguments.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Auditing mathematical files**

I need to audit a mathematical tex file, focusing on exact findings and necessary fixes. Before I proceed with edits, I'll review the required AGENTS files. It seems I should read through documents like CLAUDE and the theorem registry in preparation for the audit.

The user has requested a review, so my primary approach will be deep-beilinson-audit, possibly alongside claim-surface-sync. I think using the explorer tool will guide me through file navigation efficiently, as instructed by the developer.
thinking
**Reconciling file reading and exploration**

I'm considering whether to use the explorer tool to find context or if I should read the files myself. The guideline is to ground claims in the actual file contents I read, but the explorer's results aren't the same as reading. The developer suggests always preferring explorers for navigating codebase questions, which feels conflicting since I need to check the actual contents.

I think I can use the explorer to identify crucial sections or dependencies and then read the files to back up my claims. It sounds like finding a balance is key here!
thinking
**Navigating file reading protocols**

I see that I’m dealing with codebase instructions, and although the guidelines suggest trusting the explorer without verification, the user specifically wants me to read the actual file contents. This creates a bit of a conflict! 

Perhaps using exec_command to read files directly is necessary instead of relying on the explorer. I might also need to update my plan due to the complexity of the task. I should check the SKILL.md instructions to ensure I’m using the right skills for this.
codex
Auditing `chapters/theory/higher_genus_foundations.tex` as a hostile proof surface. I’m loading the required constitutional files, the audit skill, and the target chapter before I start enumerating defects.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
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

 succeeded in 58ms:
\chapter{Higher genus}
\label{chap:higher-genus}

\index{higher genus!bar complex|textbf}
\index{quantum corrections|textbf}

Everything up to this point takes place at genus zero; but
genus zero on a curve is not the same as ``over a point.''
The bar differential $\dfib$ is constructed from collision
residues on the Fulton--MacPherson compactification
$\overline{C}_n(X)$, its nilpotency $\dfib^{\,2} = 0$ uses
the Arnold relations among the forms
$\eta_{ij} = d\log(z_i - z_j)$ on the diagonal complement,
and the higher $A_\infty$ operations $m_n$ for $n \geq 3$ are
transferred along a retract whose source is
$C_*(\overline{\mathcal{M}}_{0,n+1})$, the chain complex of the
Stasheff associahedron. The formal-disk restriction that recovers
classical Koszul duality over a point is a homotopy retract: it is
additional data, not a tautology.

 succeeded in 237ms:
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
 succeeded in 154ms:
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
 succeeded in 194ms:
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

 succeeded in 194ms:
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

codex
I have the chapter header and first structural block. Next I’m reading the full file plus directly cited dependencies, then I’ll attack hidden imports around the genus‑`g` fiber bar, spectral sequences, and base-change claims.
exec
/bin/zsh -lc "sed -n '261,520p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '521,780p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '781,1040p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1041,1300p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 557ms:
 \[
 \Dg{g} = \dzero + \sum_{k=1}^{g} t_k\, d_k,
 \]
 where $t_k = \oint_{A_k}\omega_k$ are $A$-period parameters from
 $H^1(\Sigma_g,\C)$ \textup{(}not $H^1(\mathcal{M}_g)$, which
 vanishes for $g\ge 2$ by Harer\textup{)}. This differential is
 \emph{strict}:
 \[
 \Dg{g}^{\,2} = 0
 \]
 \textup{(}Theorem~\textup{\ref{thm:quantum-diff-squares-zero})}.

\item[\textup{(iii)}] \textbf{Genus-$0$ collision differential} $\dzero$.
 The chiral bar differential from collision residues on configuration
 spaces of~$X$ (or the fiberwise collision component $d^{(0)}$ in
 the Leray decomposition). At genus~$0$, this involves the
 Fulton--MacPherson compactifications $\overline{C}_n(\bP^1)$ and
 the Arnold relations for the logarithmic forms $\eta_{ij}$; it is
 \emph{not} the classical bar differential over a point, which
 retains no configuration-space geometry. Satisfies $\dzero^2 = 0$
 succeeded in 341ms:
\]
where $D^{(g)}_\cA := d_0 + \kappa(\cA)\,\omega_g$ is the corrected
differential incorporating the genus-$g$ curvature. At $g = 0$,
this is the tree-level MC equation. At $g = 1$, the correction
$\kappa\,\omega_1$ is the Fay trisecant identity.
\end{proposition}

\begin{proof}
The bar-intrinsic construction
(Theorem~\ref{thm:mc2-bar-intrinsic}) defines
$\Theta_\cA := D_\cA - d_0 \in \mathrm{MC}(\gAmod)$,
satisfying $D_\cA\Theta_\cA +
\tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ because $D_\cA^2 = 0$.
The genus decomposition $\gAmod = \prod_{g \geq 0}
\mathfrak{g}^{(g)}_\cA$ projects this single equation to genus~$g$,
with the curvature $\kappa(\cA)\cdot\omega_g$ entering
through the corrected differential $D^{(g)}_\cA$
(Proposition~\ref{prop:genus-g-curvature-package}\textup{(ii)}).
\end{proof}

 succeeded in 565ms:
\textup{(}$\oint_{A_l}\omega_k = \delta_{kl}$\textup{)},
$\Omega = (\tau_{kl})$ the period matrix, and
$E(z,w)$ the prime form
\textup{(}a section of
$K^{-1/2}\boxtimes K^{-1/2}$ on $\Sigma_g \times \Sigma_g$,
not $K^{+1/2}$\textup{)}.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Propagator formula.}\;
 The single-valued \textup{(}Arakelov-normalized\textup{)}
 genus-$g$ propagator is
 \begin{equation}\label{eq:propagator-package}
 \eta_{ij}^{(g)}
 \;=\;
 \biggl[\partial_{z_i}\!\log E(z_i,z_j)
 + \pi \sum_{\alpha,\beta=1}^{g}
 \omega_\alpha(z_i)\,
 (\operatorname{Im}\Omega)^{-1}_{\alpha\beta}\,
 \operatorname{Im}\!\Bigl(\int_{z_0}^{z_j}\!\omega_\beta\Bigr)
 \biggr](dz_i - dz_j).
 \end{equation}
 succeeded in 571ms:
\index{Kodaira--Spencer map|textbf}

The infinitesimal version of~\eqref{eq:bar-family} is
\begin{equation}\label{eq:ks-intro-hg}
\mathrm{KS} \colon T_{[\Sigma_g]}\overline{\mathcal{M}}_g
\;\xrightarrow{\;\sim\;}
H^1(\Sigma_g, T\Sigma_g)
\;\longrightarrow\;
\mathrm{HH}^2_{\mathrm{ch}}(\cA),
\end{equation}
sending an infinitesimal deformation of the curve to a deformation of
the bar complex
(Theorem~\ref{thm:kodaira-spencer-chiral-complete}). The obstruction
to extending a first-order deformation lies in
$\mathrm{HH}^3_{\mathrm{ch}}(\cA)$.

\subsection{The family index}
\label{subsec:why-ahat}
\index{A-hat genus@$\hat{A}$-genus!geometric derivation}

codex
The file has already exposed several likely high-severity surfaces: proved-here statements importing uncited machinery, categorical claims with no established comparison, and a late section that looks structurally inconsistent with the chapter’s own conventions. I’m finishing the remaining lines and then checking every cited dependency the chapter leans on.
exec
/bin/zsh -lc "sed -n '2081,2340p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1821,2080p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1561,1820p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1301,1560p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item $m_3 = $ homotopy for the failure of $m_2$ to be associative
\item Higher $m_k$ encode coherent homotopies (generally non-trivial)
\item Non-trivial $A_\infty$ structure (contrast with Com)
\end{itemize}
\end{theorem}

\begin{proof}[Via configuration spaces]
For Com: All points can collide simultaneously without constraint
\[\overline{C}_n^{\text{Com}}(X) = X \times \overline{M}_{0,n}\]

For Lie: Points must collide in a specific tree pattern
\[\overline{C}_n^{\text{Lie}}(X) = \text{Blow-up along all diagonals}\]

The difference in these compactifications determines the $A_\infty$ structure.
\end{proof}

% ================================================================
% SECTION 4.6: CURVED AND FILTERED EXTENSIONS
% ================================================================

 succeeded in 53ms:
\xrightarrow{\sim} \mathcal{F}$.
The Koszul dual \emph{algebra} is obtained by dualizing the bar
coalgebra:
$\mathcal{F}^! = \bar{B}^{\mathrm{ch}}(\mathcal{F})^\vee
\cong \beta\gamma$
(Theorem~\ref{thm:fermion-boson-koszul};
cf.\ the explicit computation in Chapter~\ref{ch:heisenberg-frame}).
This is Koszul duality (Lie--Com), not bosonization.
\end{example}

% ================================================================
% SECTION 4.8: MAURER-CARTAN ELEMENTS AND DEFORMATIONS
% ================================================================

\subsection{Maurer--Cartan elements and deformation theory}

\subsubsection{The moduli space of deformations}

\begin{theorem}[Maurer--Cartan = deformations {\cite{Kon03,Ger63}}; \ClaimStatusProvedElsewhere]\label{thm:genus-graded-mc}
Maurer--Cartan elements in $\bar{B}^1(\mathcal{A})[[t]]$ satisfying
 succeeded in 52ms:
 $m_1^H = 0$. The product $m_2^H$ descends to homology
 (it is strictly associative if $\mathcal{A}$ is formal).
 However, the transferred higher operations
 $m_k^H$ for $k \geq 3$ are in general \emph{non-trivial}:
 they are the Massey products, encoding obstructions to formality.
\item \emph{What is lost.}
 The explicit chain-level homotopies $\{h_n\}$ (the contracting
 data) are lost in the passage to homology. For a Koszul algebra,
 formality ensures $m_k^H = 0$ for $k \geq 3$; for a non-Koszul
 algebra, the $m_k^H$ carry essential information that cannot be
 recovered from $m_2^H$ alone.
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{Step~1: Construction of the SDR.}
The bar complex $\barBgeom(\mathcal{A})$ is a chain complex of
$\mathcal{D}_X$-modules, graded by bar degree~$n$ and conformal
weight~$h$. Since we work over a field
(Convention~\ref{subsec:ambient-category}), the splitting lemma
 succeeded in 785ms:
For the Virasoro algebra with stress tensor $T(z)$:
\[T(z_1)T(z_2) = \frac{c/2}{(z_1-z_2)^4} + \frac{2T(z_2)}{(z_1-z_2)^2} + 
\frac{\partial T(z_2)}{z_1-z_2} + \text{reg}\]

The $m_3$ operation computes:
\[m_3(T \otimes T \otimes T) = 
\int_{\partial \overline{M}_{0,4}} \text{Res}[\text{triple OPE}]\]

This involves a primary pole $\propto c^2$ from $(T \cdot T) \cdot T$ vs.\ $T \cdot (T \cdot T)$, Schwarzian derivative terms from the conformal anomaly, and descendant contributions from $\partial T$. The result is non-zero ($m_3 \neq 0$: the Virasoro algebra is $A_\infty$-non-formal, shadow depth~$\infty$), encoding the conformal anomaly
and central charge. This $m_3$ operation is the obstruction to
a strictly associative product on the bar construction, but it does \emph{not} obstruct chiral Koszulness (Theorem~\ref{thm:virasoro-chiral-koszul}).
\end{example}

\begin{remark}[Feynman diagram interpretation]
\label{rem:ainfty-feynman-preview}
The operation~$m_k$ corresponds to the tree-level Feynman diagrams
determined by the boundary stratification
of~$\overline{M}_{0,k+1}$: $m_2$ extracts the binary collision
residue, $m_3$ is the tree-level associator homotopy, and
higher~$m_k$ encode higher tree-level coherences (Stasheff

thinking
**Checking file lengths**

I’m wondering if I need more files after line 2340. I see I’ve set it up to go up to 2340, but I’m not sure if the file is shorter than that. I need to check the total number of lines in the file to figure this out. It’s important to have everything I might need, so let's confirm what the total lines are first!
exec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    7355 chapters/theory/higher_genus_foundations.tex
codex
I’ve finished the opening third and confirmed the file is 7,355 lines. I’m narrowing to the load-bearing foundation surfaces the request names: genus‑`g` fiber bar, spectral sequences, and base/base‑change claims, plus every proved-here theorem those sections depend on.
Plan update
Targeting the explicit foundation surfaces the user named, then drilling into their imported dependencies and status boundaries.
  → Map the chapter’s foundation claims around genus-g fiber bar, spectral sequences, and base/base-change arguments
  • Read each directly cited theorem/definition dependency and test whether hypotheses actually match the use
  • Assemble only re-verified findings with exact file:line references and concrete fixes

thinking
**Exploring theorem keywords**

I’m considering using a tool to find relevant keywords and theorems. I think I might want to use a multi-tool approach for topics like spectral theory, base-change, and other specific terms like proper base change or bar family. It feels like I might also need to check my local files for any missing information related to theorem labels. Maybe using a script could help for organizing this better.
exec
/bin/zsh -lc "rg -n \"spectral sequence|Leray|Boardman|base-change|base change|proper base|flat base|fiberwise|genus-\\"'$g'"\\"'$|genus-g|'"\\bGauss--Manin\\b|Kodaira--Spencer|bar complex as a family|family index|curvature package|convergence|filtered\" chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\begin\\{(theorem|proposition|lemma|corollary)\\}|\\\\ClaimStatus(ProvedHere|ProvedElsewhere|Conditional|Conjectured)|\\\\label\\{\" chapters/theory/higher_genus_foundations.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "proper base change|flat base change|coherent sheaf|coherence|Hodge bundle|Grothendieck--Riemann--Roch|Gauss--Manin|Griffiths transversality|Fay trisecant|Arakelov|Faltings|prime form|period matrix|Harer|coderived|derived category|Positselski|homotopy transfer|weight-by-weight SDR|HS-sewing" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
34:global. The fiberwise bar differential $\dfib$ inherits a
129:Three objects govern the genus tower: the curved fiberwise
184:complex forms a family of curved cochain complexes. The fiberwise
196:The fiberwise curvature $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ is the
275: spaces of~$X$ (or the fiberwise collision component $d^{(0)}$ in
276: the Leray decomposition). At genus~$0$, this involves the
301:The fiberwise differential $\dfib$ is curved; the quantum
315:The obstruction class $\mathrm{obs}_g$ (Definition~\ref{def:genus-g-obstruction})
344:\begin{proposition}[Gauss--Manin uncurving at chain level; \ClaimStatusProvedHere]
346:\index{Gauss--Manin connection!chain-level uncurving|textbf}
347:\index{uncurving!Gauss--Manin|textbf}
351:by the Gauss--Manin connection on the Hodge bundle.
353:\item \emph{Chain-level Gauss--Manin connection.}\;
357: over $\overline{\cM}_g$ carries the Gauss--Manin connection
389: \textup{(}fiberwise curvature\textup{)},
415:(i)~The Gauss--Manin connection on the cohomology local system
416:$R^q\pi_*\C$ is constructed from the Leray filtration of
422:Flatness $(\nabla^{\mathrm{GM}})^2 = 0$ is the Gauss--Manin
426:computes the obstruction to commutativity of the fiberwise bar
448:But the Gauss--Manin connection changes the
 succeeded in 51ms:
rg: regex parse error:
    (?:\begin\{(theorem|proposition|lemma|corollary)\}|\ClaimStatus(ProvedHere|ProvedElsewhere|Conditional|Conjectured)|\label\{)
                                                       ^^
error: unrecognized escape sequence
 succeeded in 50ms:
39:is forced. Here $\omega_g$ denotes the Arakelov $(1,1)$-form on
132:via the Fay trisecant identity, and the modular convolution dg~Lie
159:The single-valued (Arakelov-normalized) propagator is
167:where $\Omega$ is the period matrix, $\omega_1,\ldots,\omega_g$ the
168:normalized abelian differentials, and $E(z,w)$ the prime form
173:Arakelov $(1,1)$-form
180:by the Fay trisecant identity, so the nine-term verification
189:the top Chern class of the Hodge bundle; at genus~$1$ the same
221:Coderived category & Off-shell (curved background) \\
244: where $\omega_g$ is the Arakelov $(1,1)$-form
249: acts as $\kappa(\cA)$ times the Arakelov $(1,1)$-form $\omega_g$
266: vanishes for $g\ge 2$ by Harer\textup{)}. This differential is
288:the \emph{derived category}. The curved differential $\dfib$
291:lives in the \emph{coderived category}
292:$D^{\mathrm{co}}$~(Positselski;
293:see Appendix~\ref{app:coderived-models}).
294:The derived/coderived comparison, established on the manuscript's
295:flat-side comparison locus together with the coderived treatment of
297:derived package while the curved model is its coderived counterpart.
328:acquires monodromy $2\pi i$ around $B$-cycles; the Arakelov



thinking
**Auditing specific sections**

I need to audit targeted sections and find relevant theorem blocks around lines like 3600, 4350, 6077, and 6620. There could be many issues, so I'll need the exact lines and might use `nl -ba` with ranges. It's important to read around suspicious lines and any directly cited dependencies like Theorem quantum-diff-squares-zero or quantum-arnold-relations. The user is focusing on a specific file, but I may need to reference issues stemming from dependencies in other files. My output format will be file:line for clarity.
thinking
**Auditing references**

I’m thinking about using `grep` or `rg` to find labels and references, specifically any that are undefined. Since the user is asking for an audit, it doesn't require compiling everything, but some build surface skills might be useful. It could help to run a targeted `latexmk`, but that might be too much. I can also use a script to check for `\ref` labels in the file and verify their existence, potentially using `awk`, `sed`, or `perl`, since those could be simpler options. Running commands like these will help streamline the process.
thinking
**Identifying label mismatches**

I need to identify suspicious status mismatches for labels used in proofs, possibly utilizing the `theorem_registry`. It may be necessary to check the statuses of referenced labels from metadata in the `theorem_registry` or source files. The target file might cite theorems that are conditional or conjectured, which I need to detect. A script could help map references from the target file to their statuses. Overall, the best approach seems to be auditing the sections specified by the user, particularly focusing on terms like "spectral sequence" and "base-change" in the relevant lines.
codex
The first pass shows the main risk pattern: the chapter repeatedly upgrades slogans into proved-here claims, then imports heavy machinery by name only. I’m drilling into the exact theorem blocks around lines `344`, `514`, `770`, `800`, `1935`, `2167`, `3691`, `4355`, `6077`, and `6620`, because those are where hidden hypotheses and spectral/base-change drift concentrate.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2150,2215p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '514,770p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '4355,4495p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1935,2005p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6077,6145p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '340,470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '799,960p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2150	characteristic (Theorem~\textup{\ref{thm:modular-characteristic}}).
  2151	\end{convention}
  2152	
  2153	\begin{proposition}[Deforming Heisenberg; \ClaimStatusProvedHere]
  2154	\label{prop:deforming-heisenberg}
  2155	The Heisenberg algebra $\mathcal{H}_\kappa$ on a smooth curve~$X$ of
  2156	genus~$g$ admits deformations parametrized by
  2157	$H^1(\bar{B}(\mathcal{H}_\kappa)) \cong H^1(X, \mathbb{C}) \oplus
  2158	\mathbb{C} \cdot \partial\kappa$.
  2159	\end{proposition}
  2160	
  2161	\begin{proof}
  2162	The bar complex of $\mathcal{H}_\kappa$ is the symmetric coalgebra
  2163	$\bar{B}(\mathcal{H}_\kappa) = \mathrm{Sym}^c(s^{-1}\overline{\mathcal{H}})$
  2164	(Theorem~\ref{thm:heisenberg-koszul-dual-early}). The degree-$1$
  2165	component is $\bar{B}^1 = s^{-1}\overline{\mathcal{H}}_1 = s^{-1}
  2166	\mathbb{C} \cdot J$, so $H^1$ of the bar complex on~$X$ is computed
  2167	by the Leray spectral sequence for $\bar{B}$ viewed as a sheaf
  2168	on~$X$ (convergent: $X$ has finite cohomological dimension and
  2169	$\mathcal{H}^q(\bar{B}^\bullet)$ is a coherent sheaf for each~$q$):
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3668,3725p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6618,6668p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4355	\index{spectral sequence!genus|textbf}
  4356	
  4357	The genus-by-genus bar complexes assemble into a single spectral sequence whose
  4358	$E_1$~page is the genus-stratified bar cohomology, whose
  4359	differentials are the clutching maps along boundary divisors of
  4360	$\overline{\mathcal{M}}_g$, and whose $E_\infty$~page computes
  4361	the full chiral homology. The collapse page depends on the
  4362	family: $E_1$ for Kac--Moody (by CE acyclicity of the
  4363	associated graded); $E_2$ for Virasoro and $\mathcal{W}$-algebras
  4364	(the DS reduction of the $E_1$-collapsed KM spectral sequence
  4365	introduces one additional differential from the BRST operator
  4366	$Q_{\mathrm{DS}}$, shifting the collapse by one page;
  4367	see Theorem~\ref{thm:ds-koszul-intertwine}).
  4368	
  4369	\subsection{Spectral sequence = genus expansion}
  4370	
  4371	\begin{remark}[Spectral sequence as loop expansion]
  4372	\label{rem:ss-genus}
  4373	The spectral sequence $E_r^{p,q} \Rightarrow H^{p+q}(\bar{B}(\mathcal{A}))$ organizes contributions by genus: $E_1$ is tree-level (genus~$0$), $E_2$ is one-loop (genus~$1$), and $E_r$ is $(r{-}1)$-loop.
  4374	\end{remark}
 succeeded in 52ms:
  6077	\ClaimStatusProvedHere]\label{prop:bar-tautological-filtration}
  6078	\index{tautological ring!bar spectral sequence filtration}
  6079	The bar spectral sequence
  6080	$E_r^{p,q} \Rightarrow H^{p+q}(\bar{B}^{(g)}(\mathcal{A}))$
  6081	induces a \emph{tautological filtration} on the bar cohomology:
  6082	\begin{equation}\label{eq:tauto-filtration}
  6083	0 = F^{3g-2} \subset F^{3g-3} \subset \cdots \subset F^0 =
  6084	H^*(\bar{B}^{(g)}(\mathcal{A}))
  6085	\end{equation}
  6086	where $F^p / F^{p+1} = E_\infty^{p,*}$. The associated graded
  6087	pieces satisfy:
  6088	\begin{enumerate}[label=\textup{(\roman*)}]
  6089	\item $E_2^{p,q}$ involves classes in
  6090	 $H^p(\overline{\mathcal{M}}_g, \mathcal{H}^q(\bar{B}^{(g)}_\bullet))$,
  6091	 which lie in the tautological ring $R^*(\overline{\mathcal{M}}_g)$
  6092	 for Koszul algebras;
  6093	\item The differential $d_2\colon E_2^{p,q} \to E_2^{p+2,q-1}$
  6094	 is the Kodaira--Spencer map, which produces $\psi$-classes and
  6095	 boundary classes from $\lambda$-classes;
  6096	\item The differential $d_3$ involves triple Massey products,
 succeeded in 52ms:
  1935	\begin{theorem}[Convergence for filtered algebras; \ClaimStatusProvedHere]
  1936	\label{thm:convergence-filtered}
  1937	Let $\mathcal{A}$ be a complete filtered chiral algebra (i.e.,
  1938	$\mathcal{A} = \varprojlim \mathcal{A}/F_k\mathcal{A}$) whose associated
  1939	graded $\mathrm{gr}\,\mathcal{A}$ is a Koszul chiral algebra in the sense of
  1940	Theorem~\ref{thm:chiral-koszul-duality}. Then:
  1941	\begin{enumerate}
  1942	\item The bar complex $\bar{B}(\mathcal{A})$ converges without completion:
  1943	each $\bar{B}^n(\mathcal{A})$ is complete in the induced filtration
  1944	\item Each cohomology class in $H^*(\bar{B}(\mathcal{A}))$ has a canonical
  1945	representative given by the unique closed element in the $\mathrm{gr}$-harmonic
  1946	complement
  1947	\item The cobar-bar adjunction
  1948	$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A})) \xrightarrow{\sim}
  1949	\mathcal{A}$ is a filtered quasi-isomorphism
  1950	\item Koszul duality extends: the Koszul dual $\mathcal{A}^!$ inherits a
  1951	complete filtration with $\mathrm{gr}\,\mathcal{A}^! \cong
  1952	(\mathrm{gr}\,\mathcal{A})^!$
  1953	\end{enumerate}
  1954	\end{theorem}
 succeeded in 51ms:
   340	comparison of the three chain-level models and their relationship
   341	to the modular bar complex.
   342	\end{remark}
   343	
   344	\begin{proposition}[Gauss--Manin uncurving at chain level; \ClaimStatusProvedHere]
   345	\label{prop:gauss-manin-uncurving-chain}
   346	\index{Gauss--Manin connection!chain-level uncurving|textbf}
   347	\index{uncurving!Gauss--Manin|textbf}
   348	Let $\cA$ be a cyclic chiral algebra on $\Sigma_g$ with
   349	$g \geq 1$. The passage from the curved differential $\dfib$
   350	to the flat differential $\Dg{g}$ is realized at chain level
   351	by the Gauss--Manin connection on the Hodge bundle.
   352	\begin{enumerate}[label=\textup{(\roman*)}]
   353	\item \emph{Chain-level Gauss--Manin connection.}\;
   354	 The local system
   355	 $\mathcal{R}^q = R^q\pi_*(\cA^{\boxtimes n}
   356	 \otimes \Omega^*_{\log})$
   357	 over $\overline{\cM}_g$ carries the Gauss--Manin connection
   358	 \begin{equation}\label{eq:gauss-manin-chain}
   359	 \nabla^{\mathrm{GM}}
 succeeded in 76ms:
   514	\begin{proposition}[The genus-$g$ curvature package; \ClaimStatusProvedHere]
   515	\label{prop:genus-g-curvature-package}
   516	\index{curvature package!genus-g@genus-$g$|textbf}
   517	Let $\cA$ be a cyclic chiral algebra on a smooth projective
   518	curve~$X$ of genus~$g \geq 1$, and let
   519	$\{\omega_1,\ldots,\omega_g\}$ be the normalized abelian
   520	differentials on~$\Sigma_g$
   521	\textup{(}$\oint_{A_l}\omega_k = \delta_{kl}$\textup{)},
   522	$\Omega = (\tau_{kl})$ the period matrix, and
   523	$E(z,w)$ the prime form
   524	\textup{(}a section of
   525	$K^{-1/2}\boxtimes K^{-1/2}$ on $\Sigma_g \times \Sigma_g$,
   526	not $K^{+1/2}$\textup{)}.
   527	\begin{enumerate}[label=\textup{(\roman*)}]
   528	\item \emph{Propagator formula.}\;
   529	 The single-valued \textup{(}Arakelov-normalized\textup{)}
   530	 genus-$g$ propagator is
   531	 \begin{equation}\label{eq:propagator-package}
   532	 \eta_{ij}^{(g)}
   533	 \;=\;
 succeeded in 58ms:
   799	\end{proof}
   800	
   801	\begin{theorem}[Genus extension hierarchy; \ClaimStatusProvedHere]
   802	\label{thm:genus-extension-hierarchy}
   803	\index{genus extension hierarchy|textbf}
   804	\index{bar complex!genus extension levels}
   805	\index{Koszul locus!genus extension}
   806	\index{modular functor!genus extension level}
   807	The genus extension of the bar complex admits a five-level
   808	hierarchy of successively stronger structural conditions.
   809	Each level is strictly contained in the next, and the standard
   810	landscape satisfies all five.
   811	\begin{enumerate}[label=\textup{(\roman*)}]
   812	\item \emph{Algebraic \textup{(}bar $D^2=0$ at all genera\textup{)}.}\;
   813	 For \emph{any} chiral algebra $\cA$, the bar differential satisfies
   814	 $D_\cA^2 = 0$ at all genera, and the universal MC element
   815	 $\Theta_\cA := D_\cA - d_0 \in \MC(\gAmod)$ exists
   816	 unconditionally
   817	 \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
   818	 No finiteness or Koszulness condition is required: $D^2 = 0$
 succeeded in 53ms:
  6618	\begin{theorem}[Loop order spectral sequence;
  6619	\ClaimStatusProvedHere]\label{thm:loop-order-spectral-sequence}
  6620	\index{spectral sequence!loop order|textbf}
  6621	The loop order filtration on $\barB^{(g)}(\cA)$ induces a
  6622	convergent spectral sequence
  6623	\begin{equation}\label{eq:loop-ss}
  6624	E_0^{\ell,q}
  6625	\;=\;
  6626	\bigl(F^\ell / F^{\ell+1}\bigr)^q
  6627	\;\Longrightarrow\;
  6628	H^{\ell+q}\!\bigl(\barB^{(g)}(\cA)\bigr),
  6629	\end{equation}
  6630	with:
  6631	\begin{enumerate}[label=\textup{(\roman*)}]
  6632	\item $E_0^{\ell,q}$: the space of Feynman transform elements
  6633	 supported on stable graphs with $b_1(\Gamma) = \ell$ exactly;
  6634	
  6635	\item $d_0 = d_{\mathrm{tree}}$: the differential on~$E_0$ contracts
  6636	 only non-loop edges \textup{(}separating-type gluings\textup{)};
  6637	
 succeeded in 53ms:
  3668	
  3669	\subsection{The differential}
  3670	
  3671	\begin{theorem}[Genus-dependent differential; \ClaimStatusProvedHere]
  3672	\label{thm:genus-differential}
  3673	On a fixed genus-$g$ bar complex, the total corrected differential
  3674	decomposes as:
  3675	\begin{equation}
  3676	\Dg{g} = d^{(0)} + d^{(1)} + d^{(2)} + \cdots
  3677	\end{equation}
  3678	where, for a \emph{fixed} genus~$g$, the component $d^{(k)}$ shifts the Leray filtration
  3679	on $\bar{B}^{(g)}(\mathcal{A})$ by $k$ base degrees
  3680	(see Remark~\ref{rem:differential-notation} below).
  3681	
  3682	The strict nilpotence condition $\Dg{g}^{\,2} = 0$ decomposes into:
  3683	\begin{align}
  3684	(d^{(0)})^2 &= 0 \quad \text{(genus 0 exactness)}\\
  3685	\{d^{(0)}, d^{(1)}\} &= 0 \quad \text{(genus 1 compatibility)}\\
  3686	\{d^{(0)}, d^{(2)}\} + (d^{(1)})^2 &= 0 \quad \text{(genus 2 relation)}\\
  3687	&\vdots
codex
I’m now cross-checking the chapter’s imports against the live repository: cited theorem labels, claim statuses, and bibliography entries. Several of these proved-here arguments look like they may be leaning on labels that either don’t exist, don’t say what this file uses them for, or only establish a weaker statement.
exec
/bin/zsh -lc "rg -n \"ClaimStatus(ProvedHere|ProvedElsewhere|Conditional|Conjectured)\" chapters/theory/higher_genus_foundations.tex | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
344:\begin{proposition}[Gauss--Manin uncurving at chain level; \ClaimStatusProvedHere]
514:\begin{proposition}[The genus-$g$ curvature package; \ClaimStatusProvedHere]
636:\begin{proposition}[Chain-level curvature operator; \ClaimStatusProvedHere]
769:\begin{proposition}[Genus-$g$ MC element; \ClaimStatusProvedHere]
801:\begin{theorem}[Genus extension hierarchy; \ClaimStatusProvedHere]
1134:\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex; \ClaimStatusProvedHere]\label{thm:bar-ainfty-complete}
1234:\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} operations via moduli spaces; \ClaimStatusProvedHere]\label{thm:ainfty-moduli}
1329:\begin{theorem}[Pentagon identity; \ClaimStatusProvedHere]\label{thm:pentagon-identity}
1367:\begin{theorem}[Higher associahedron identity for \texorpdfstring{$m_5$}{m5} {\cite{Sta63}}; \ClaimStatusProvedElsewhere]\label{thm:higher-associahedron-m5}
1379:\begin{theorem}[Catalan identity at higher levels {\cite{Sta97}}; \ClaimStatusProvedElsewhere]\label{thm:catalan-parenthesization}
1402:\begin{theorem}[Verdier duality = NAP duality {\cite{AF15,KS90}}; \ClaimStatusProvedElsewhere]\label{thm:verdier-NAP}
1442:\begin{theorem}[Cobar \texorpdfstring{$A_\infty$}{A-infinity} structure; \ClaimStatusProvedHere]\label{thm:cobar-ainfty-complete}
1548:\begin{theorem}[Chain-level vs.\ homology-level structure; \ClaimStatusProvedHere]
1696:\begin{theorem}[Verdier duality of operations; \ClaimStatusProvedHere]\label{thm:verdier-duality-operations}
1767:\begin{theorem}[Geometric enhancement of Com-Lie; \ClaimStatusProvedElsewhere]\label{thm:geometric-com-lie-enhancement}
1805:\begin{theorem}[Maximal vs.\ trivial \texorpdfstring{$A_\infty$}{A-infinity}; \ClaimStatusProvedElsewhere]\label{thm:ainfty-com-lie-interchange}
1857:$\mathrm{Ch}_\infty$-algebra; \ClaimStatusProvedHere]
1935:\begin{theorem}[Convergence for filtered algebras; \ClaimStatusProvedHere]
2038:\begin{theorem}[Cobar resolution on the Koszul locus {\cite{LV12}}; \ClaimStatusProvedElsewhere]
2099:\begin{theorem}[Maurer--Cartan = deformations {\cite{Kon03,Ger63}}; \ClaimStatusProvedElsewhere]\label{thm:genus-graded-mc}
exec
/bin/zsh -lc 'for lbl in thm:quantum-diff-squares-zero thm:quantum-arnold-relations thm:family-index thm:genus-universality thm:higher-genus-inversion thm:bar-cobar-inversion-qi thm:chiral-koszul-duality thm:bar-nilpotency-complete thm:concrete-quantum-differential thm:general-hs-sewing prop:loop-filtration-compatible thm:multi-generator-universality thm:koszul-equivalences-meta thm:mc2-bar-intrinsic thm:cobar-resolution-scoped rem:admissible-koszul-status; do echo "LABEL $lbl"; rg -n "'"\\\\label\\{"'$lbl'"\\}|"'$lbl" chapters appendices metadata -g '"'*.tex' -g '*.md'; echo; done" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for cite in Boardman-conditional Griffiths68 Ara74 Fal84 Zhu96 Cliff19 MS24 Fay73 LV12 Kon03 Ger63 Drinfeld85; do echo "CITE $cite"; rg -n "${cite}" . -g '"'*.bib' -g '*.tex'; echo; done" in /Users/raeez/chiral-bar-cobar succeeded in 163ms:
rg: regex parse error:
    (?:\label\{thm:concrete-quantum-differential\}|thm:concrete-quantum-differential)
       ^^
error: unrecognized escape sequence

LABEL thm:general-hs-sewing
rg: regex parse error:
    (?:\label\{thm:general-hs-sewing\}|thm:general-hs-sewing)
       ^^
error: unrecognized escape sequence

LABEL prop:loop-filtration-compatible
rg: regex parse error:
    (?:\label\{prop:loop-filtration-compatible\}|prop:loop-filtration-compatible)
       ^^
error: unrecognized escape sequence

LABEL thm:multi-generator-universality
rg: regex parse error:
    (?:\label\{thm:multi-generator-universality\}|thm:multi-generator-universality)
 succeeded in 213ms:
./bibliography/references.tex:281:\bibitem{Cliff19}
./chapters/theory/algebraic_foundations.tex:1320:Cliff~\cite{Cliff19}, meaning that it extends to a
./chapters/theory/algebraic_foundations.tex:1328:In dimension~$1$, Cliff~\cite[Proposition~8.1]{Cliff19}
./chapters/theory/higher_genus_modular_koszul.tex:28908:Cliff~\cite{Cliff19} defines a \emph{universal
./chapters/theory/higher_genus_modular_koszul.tex:28921:(Cliff~\cite[Proposition~8.1]{Cliff19}).
./chapters/theory/higher_genus_foundations.tex:905:(Cliff~\cite[Proposition~8.1]{Cliff19})
./chapters/theory/higher_genus_foundations.tex:5466: (Cliff~\cite[Proposition~8.1]{Cliff19};

CITE MS24
./bibliography/references.tex:948:\bibitem{MS24}
./chapters/examples/y_algebras.tex:813:\item \emph{Pillar~A (homotopy chiral, MS24):}
./standalone/programme_summary_section1.tex:668:\bibitem{MS24}
./standalone/references.bib:588:@article{MS24,
./standalone/programme_summary.tex:1161:algebras~\cite{MS24}. The modular characteristic~$\kappa$, the cubic
./standalone/programme_summary.tex:2717:\bibitem{MS24}
./standalone/programme_summary_sections9_14.tex:707:\bibitem{MS24}
./standalone/introduction_full_survey.tex:3391:\item \emph{Malikov--Schechtman~\cite{MS24}}: the primitive local object is a \emph{homotopy chiral algebra} ($\mathrm{Ch}_\infty$), not strict. The strict chiral algebra appears after rectification.
./standalone/introduction_full_survey.tex:4271:\subsection{Pillar A: homotopy chiral algebras (MS24)}
./standalone/introduction_full_survey.tex:4276:in the sense of Malikov--Schechtman~\cite{MS24}.
./standalone/introduction_full_survey.tex:4337:\item $F_n = o_n$: the secondary Borcherds operations of~\cite{MS24} at degree $n \geq 3$ coincide with the shadow obstruction tower obstruction classes (Proposition~\ref{prop:borcherds-shadow-identification}).

thinking
**Improving search for labels**

I'm thinking that I might need to fix the search for labels using `rg -F`. It feels like a straightforward plan, but I want to ensure it's done properly. My goal is to make the search process more efficient, and I think making adjustments here will help achieve that. I want to explore how I can improve the functionality and get it right this time! So, let’s dive deeper into that.
exec
/bin/zsh -lc 'for lbl in thm:quantum-diff-squares-zero thm:quantum-arnold-relations thm:family-index thm:genus-universality thm:higher-genus-inversion thm:bar-cobar-inversion-qi thm:chiral-koszul-duality thm:bar-nilpotency-complete thm:concrete-quantum-differential thm:general-hs-sewing prop:loop-filtration-compatible thm:multi-generator-universality thm:koszul-equivalences-meta thm:mc2-bar-intrinsic thm:cobar-resolution-scoped rem:admissible-koszul-status; do echo "LABEL $lbl"; rg -n -F "'"\\\\label{"'$lbl}" chapters appendices metadata -g '"'*.tex' -g '*.md'; echo; done" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'for lbl in thm:quantum-diff-squares-zero thm:quantum-arnold-relations thm:family-index thm:genus-universality thm:higher-genus-inversion thm:bar-cobar-inversion-qi thm:chiral-koszul-duality thm:bar-nilpotency-complete thm:concrete-quantum-differential thm:general-hs-sewing prop:loop-filtration-compatible thm:multi-generator-universality thm:koszul-equivalences-meta thm:mc2-bar-intrinsic thm:cobar-resolution-scoped rem:admissible-koszul-status; do echo "REG $lbl"; rg -n -F "$lbl" metadata/theorem_registry.md chapters/connections/concordance.tex; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 198ms:

REG thm:bar-nilpotency-complete
metadata/theorem_registry.md:303:| `thm:bar-nilpotency-complete` | `theorem` | 758 | Nilpotency of bar differential |

REG thm:concrete-quantum-differential
metadata/theorem_registry.md:812:| `thm:concrete-quantum-differential` | `theorem` | 3731 | Concrete quantum differential |

REG thm:general-hs-sewing
metadata/theorem_registry.md:2541:| `thm:general-hs-sewing` | `theorem` | 1398 | General HS-sewing criterion |
chapters/connections/concordance.tex:1947: (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
chapters/connections/concordance.tex:3287: (Theorem~\ref{thm:general-hs-sewing});
chapters/connections/concordance.tex:4389:(Theorem~\ref{thm:general-hs-sewing}).
chapters/connections/concordance.tex:6963:criterion (Theorem~\ref{thm:general-hs-sewing}) together
chapters/connections/concordance.tex:7722:(Theorem~\ref{thm:general-hs-sewing}) proves convergence for
chapters/connections/concordance.tex:9626: \textup{(}Theorem~\ref{thm:general-hs-sewing}\textup{)} \\
chapters/connections/concordance.tex:11130: at all genera (Theorem~\ref{thm:general-hs-sewing}); the

REG prop:loop-filtration-compatible
metadata/theorem_registry.md:842:| `prop:loop-filtration-compatible` | `proposition` | 6526 | Filtration compatibility |

 succeeded in 235ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1611:\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}

LABEL thm:chiral-koszul-duality
chapters/theory/chiral_koszul_pairs.tex:4138:\label{thm:chiral-koszul-duality}

LABEL thm:bar-nilpotency-complete
chapters/theory/bar_construction.tex:788:\begin{theorem}[Nilpotency of bar differential; \ClaimStatusProvedHere]\label{thm:bar-nilpotency-complete}

LABEL thm:concrete-quantum-differential
chapters/theory/higher_genus_foundations.tex:3732:\label{thm:concrete-quantum-differential}

LABEL thm:general-hs-sewing
chapters/connections/genus_complete.tex:1386:\label{thm:general-hs-sewing}%

LABEL prop:loop-filtration-compatible
chapters/theory/higher_genus_foundations.tex:6581:\ClaimStatusProvedHere]\label{prop:loop-filtration-compatible}

LABEL thm:multi-generator-universality
chapters/theory/higher_genus_modular_koszul.tex:21786:\label{thm:multi-generator-universality}

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '4128,4175p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
  4140	filtered-complete with completion
  4141	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  4142	
  4143	Let $(\mathcal{A}_1, \mathcal{A}_2)$ be a chiral Koszul pair. Then there exists a natural quasi-isomorphism of chiral coalgebras:
  4144	\[\Phi: \widehat{\bar{B}^{\text{ch}}(\mathcal{A}_1)} \xrightarrow{\sim} \mathcal{A}_2^!\]
  4145	where $\widehat{\bar{B}^{\text{ch}}(\mathcal{A}_1)}$ denotes the \emph{I-adic completion} of the geometric bar complex.
  4146	
  4147	The map $\Phi$ satisfies:
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21776,21835p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5288,5338p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 21776	without unit in the sense of
 21777	Pandharipande--Pixton--Zvonkine. The unit axiom
 21778	$\Omega_{0,3}(\mathbf{1}, v, w) = \eta(v,w)$ holds when the
 21779	vacuum vector of~$\cA$ lies in~$V$ and $\ell_2^{(0)}$
 21780	restricts to a unital multiplication on~$V$ (satisfied for
 21781	all standard families).
 21782	\end{proof}
 21783	
 21784	\begin{theorem}[Multi-weight genus expansion; \ClaimStatusProvedHere]
 21785	\label{thm:multi-weight-genus-expansion}
 21786	\label{thm:multi-generator-universality}
 21787	\index{multi-generator obstruction!genus expansion|textbf}%
 21788	\index{multi-weight genus expansion|textbf}%
 21789	\index{cross-channel correction|textbf}%
 21790	\index{Faber--Pandharipande formula!multi-weight decomposition}%
 21791	\index{genus expansion!multi-channel graph sum}%
 21792	Let\/ $\cA$ be a modular Koszul chiral algebra with
 21793	strong generators $\varphi_1, \ldots, \varphi_r$ of conformal
 21794	weights $h_1, \ldots, h_r$, per-channel modular characteristics
 21795	$\kappa_1, \ldots, \kappa_r$
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5918,5950p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  5288	\hline
  5289	$W_3(c)$ & $\frac{5c}{6} \lambda_g$\rlap{${}^*$} & Conformal anomaly \\
  5290	\hline
  5291	Virasoro $(c)$ & $\frac{c}{2} \lambda_g$ & Conformal anomaly \\
  5292	\hline
  5293	\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
  5294	\hline
  5295	\end{tabular}
  5296	\end{table}
  5297	
  5298	\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
  5299	\index{genus universality theorem|textbf}
  5300	\textup{[Regime: curved-central on the Koszul locus; all genera
  5301	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  5302	
  5303	Let $\cA$ be a modular Koszul chiral algebra whose strong generators
  5304	all have the \emph{same} conformal weight. There exists a
  5305	genus-independent scalar $\kappa(\cA)$, determined by the genus-$1$
  5306	curvature, such that \begin{equation}\label{eq:genus-universality}
  5307	\mathrm{obs}_g(\cA) \;=\; \kappa(\cA) \cdot \lambda_g
 succeeded in 52ms:
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
  5930	\index{Grothendieck--Riemann--Roch!genus expansion|textbf}
  5931	Let $\cA$ be a Koszul chiral algebra with obstruction coefficient
  5932	$\kappa(\cA)$, let $\pi \colon \overline{\mathcal{C}}_g \to
  5933	\overline{\mathcal{M}}_g$ be the universal curve with relative
  5934	dualizing sheaf~$\omega_\pi$, and let
  5935	$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle.
  5936	The following holds for uniform-weight modular Koszul algebras
  5937	at all genera; the genus-$1$ statements are unconditional for




thinking
**Evaluating coderivation terms**

I'm reflecting on proposition 636, which indicates that dfib does not imply coderivation when κ≠0. That's really significant! If it's true that differential fails coderivation, then my earlier use of "curved dg coalgebra" could actually be incorrect. It's interesting to consider how curvature might play a role here, and I'm curious about the implications that arise from this. There's a lot to untangle in how these concepts relate to each other!
thinking
**Addressing internal inconsistencies**

I'm noticing a major internal inconsistency with the phrasing "each level is strictly contained in the next" compared to later stating that "relation to iii is not one of containment." This seems problematic! I’ll take a closer look at the chain listed as `iv⊊iii⊊ii⊊i` because the reversed direction might actually cause confusion regarding the strength and weakness of the containment idea. It definitely needs a precise fix!
thinking
**Evaluating mathematical findings**

I think this is a significant finding. The theorem assumption indicates a complete filtered chiral algebra and related concepts like the associated graded Koszul. It seems to imply a filtered quasi-isomorphism `\Omega(B(A))→A`. However, I might need to ensure that I fully consider the complete filtration and Boardman hypotheses. I should also compare this with existing theorems in the repository to see if it's salvageable. Alright, let's move forward with that!
thinking
**Evaluating mathematical definitions**

I need to check the definition of `d^{(0)}` in `thm:concrete-quantum-differential`, maybe around page 3732, but it seems likely to be okay. Theorem 4438 E2 suggests that `d_2` is the Kodaira-Spencer map in a Leray spectral sequence, which is mapped from fiber cohomology. Identifying it is tricky and might be incorrect in this context. Also, there's an issue with undefined terms like `M_k`, so I should consider revising the formula or treating it as conjectural instead.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3731,3810p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6900,6950p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2038,2070p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6510,6595p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3731	\begin{theorem}[Concrete quantum differential; \ClaimStatusProvedHere]
  3732	\label{thm:concrete-quantum-differential}
  3733	For $\alpha \in \bar{B}^{(g)}_n(\mathcal{A})$ represented by:
  3734	\begin{equation}
  3735	\alpha = \int_{\overline{C}_n(\Sigma_g)} \phi_1(p_1) \cdots \phi_n(p_n) \cdot f(p_1, \ldots, p_n; \Omega) \cdot \prod_{i<j} \eta_{ij}^{(g)}
  3736	\end{equation}
  3737	
  3738	The total corrected differential decomposes by Leray degree
  3739	\textup{(}Remark~\textup{\ref{rem:differential-notation})}:
  3740	\[
  3741	\Dg{g} = d^{(0)} + d^{(1)} + \cdots
  3742	\]
  3743	and acts by:
  3744	\begin{align}
  3745	d^{(0)}\alpha &= \sum_{i<j} \mathrm{Res}_{D_{ij}} [\mu_{ij}(\phi_i \otimes \phi_j) \otimes \mathrm{remaining}]\\
  3746	d^{(1)}\alpha &= \sum_{\gamma \in H_1(\Sigma_g)} \oint_\gamma \omega_\gamma \cdot \delta_{\gamma^*}[\alpha]\\
  3747	d^{(k)}\alpha &= \sum_{\mathrm{strata}\; \Delta} \int_\Delta \mathrm{(boundary\; contribution)}, \qquad k \ge 2
  3748	\end{align}
  3749	where:
  3750	\begin{itemize}
 succeeded in 53ms:
  6900	\end{remark}
  6901	
  6902	\subsection{Collapse on the Koszul locus}
  6903	\label{subsec:loop-order-collapse}
  6904	\index{spectral sequence!loop order collapse}
  6905	
  6906	\begin{theorem}[Loop order collapse;
  6907	\ClaimStatusProvedHere]\label{thm:loop-order-collapse}
  6908	Let $\cA$ be a modular Koszul chiral algebra
  6909	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
  6910	The loop order spectral sequence
  6911	\textup{(}Theorem~\textup{\ref{thm:loop-order-spectral-sequence})}
  6912	collapses at $E_1$:
  6913	\begin{equation}\label{eq:loop-collapse}
  6914	E_1^{\ell,q} \;=\; E_\infty^{\ell,q}
  6915	\qquad\text{for all } \ell, q.
  6916	\end{equation}
  6917	\end{theorem}
  6918	
  6919	\begin{proof}
 succeeded in 51ms:
  2038	\begin{theorem}[Cobar resolution on the Koszul locus {\cite{LV12}}; \ClaimStatusProvedElsewhere]
  2039	\label{thm:cobar-resolution-scoped}
  2040	For any augmented chiral algebra $\mathcal{A}$, the bar construction
  2041	$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ and cobar construction
  2042	$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A}))$ exist as objects.
  2043	When the canonical twisting morphism is Koszul
  2044	\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})},
  2045	the cobar of the bar provides a free resolution:
  2046	\begin{multline*}
  2047	\cdots \to \Omega^2_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
  2048	\to \Omega^1_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))\\
  2049	\to \Omega^0_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
  2050	\xrightarrow{\epsilon} \cA \to 0
  2051	\end{multline*}
  2052	Off the Koszul locus, the bar-cobar object persists only in the
  2053	completed coderived category
  2054	\textup{(}Appendix~\textup{\ref{sec:coderived-models})}.
  2055	
  2056	The augmentation is given geometrically by:
  2057	\[\epsilon(K) = \lim_{\varepsilon \to 0} \int_{|z_i - z_j| > \varepsilon} K(z_1, \ldots, z_n) \prod_{i<j} |z_i - z_j|^{2h_{ij}}\]
 succeeded in 51ms:
  6510	\;=\;
  6511	\sum_{e \in E(\Gamma)}
  6512	(-1)^{\sigma(e,\Gamma)}\,\Gamma / e,
  6513	\end{equation}
  6514	where $\sigma(e,\Gamma)$ is the position of~$e$ in the chosen
  6515	ordering of $E(\Gamma)$.
  6516	\end{definition}
  6517	
  6518	\begin{lemma}[$\partial_{\mathcal{G}}^2 = 0$;
  6519	\ClaimStatusProvedHere]\label{lem:stable-graph-d-squared}
  6520	The stable graph differential satisfies $\partial_{\mathcal{G}}^2 = 0$.
  6521	\end{lemma}
  6522	
  6523	\begin{proof}
  6524	Each term in $\partial_{\mathcal{G}}^2$ contracts two edges
  6525	$e, e'$ in some order. If $e$ and $e'$ share no vertex, the
  6526	contractions commute. If they share a vertex, the two orders
  6527	produce the same graph $\Gamma / \{e, e'\}$ with opposite signs
  6528	(from the antisymmetry of the determinant ordering in
  6529	$\det(E(\Gamma))$). In both cases, the terms cancel in pairs.

thinking
**Exploring filtration compatibility**

I need to gather more information around the prop about loop-filtration compatibility, especially regarding theorem 6618, which seems to use decreasing filtration while dropping one degree. I’m also wondering if d_0 should actually be d_loop instead of d_tree, depending on the descending filtration. So, my next step is to inspect the lines starting from 6583 to clarify these points. Let’s see what I can find!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6580,6625p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  6580	\begin{proposition}[Filtration compatibility;
  6581	\ClaimStatusProvedHere]\label{prop:loop-filtration-compatible}
  6582	\index{loop order!filtration compatibility}
  6583	The Feynman transform differential respects the loop order
  6584	filtration:
  6585	\begin{equation}\label{eq:loop-filtration-d}
  6586	d_{\mathrm{FT}} \colon
  6587	F^\ell\!\barB^{(g)} \to F^{\ell-1}\!\barB^{(g)}.
  6588	\end{equation}
  6589	Precisely, $d_{\mathrm{FT}}$ decomposes as
  6590	\begin{equation}\label{eq:d-tree-loop}
  6591	d_{\mathrm{FT}}
  6592	\;=\; d_{\mathrm{tree}} + d_{\mathrm{loop}},
  6593	\end{equation}
  6594	where:
  6595	\begin{enumerate}[label=\textup{(\alph*)}]
  6596	\item $d_{\mathrm{tree}}$ contracts non-loop edges
  6597	 \textup{(}edges connecting distinct vertices\textup{)};
  6598	 this preserves loop order:
  6599	 $d_{\mathrm{tree}}\colon F^\ell \to F^\ell$.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '6068,6135p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  6068	$\overline{\mathcal{M}}_{g,n}$, which a priori lie in a larger part of
  6069	$R^*(\overline{\mathcal{M}}_g)$. On the proved scalar lane, collapse
  6070	at $E_2$ (Theorem~\ref{thm:spectral-sequence-collapse}) reduces the
  6071	scalar contribution to the single class $\kappa \cdot \lambda_g$ so
  6072	no additional scalar tautological classes emerge from the bar complex
  6073	at the level of cohomology.
  6074	\end{remark}
  6075	
  6076	\begin{proposition}[Bar spectral sequence and tautological filtration;
  6077	\ClaimStatusProvedHere]\label{prop:bar-tautological-filtration}
  6078	\index{tautological ring!bar spectral sequence filtration}
  6079	The bar spectral sequence
  6080	$E_r^{p,q} \Rightarrow H^{p+q}(\bar{B}^{(g)}(\mathcal{A}))$
  6081	induces a \emph{tautological filtration} on the bar cohomology:
  6082	\begin{equation}\label{eq:tauto-filtration}
  6083	0 = F^{3g-2} \subset F^{3g-3} \subset \cdots \subset F^0 =
  6084	H^*(\bar{B}^{(g)}(\mathcal{A}))
  6085	\end{equation}
  6086	where $F^p / F^{p+1} = E_\infty^{p,*}$. The associated graded
  6087	pieces satisfy:

thinking
**Finding missing references**

I need to compile any missing references—there might be unresolved labels. I'm considering using a quick script to detect which references in the target file are not defined. I could rely on a simple shell command with Perl and `rg` to help with this. The plan is to extract `\ref{...}` and search for the fixed label across the repository. I should gather the actual file contents next and run the shell loops.
codex
I’ve got several structural failures already. I’m doing one more pass for hard mechanical defects in the chapter itself: undefined labels, dead citations, and reference targets that don’t exist or are status-unstable.
exec
/bin/zsh -lc 'refs=$(perl -ne '"'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_foundations.tex | sort -u); for r in "'$refs; do if ! rg -q -F "'"\\\\label{"'$r}" chapters appendices; then echo "MISSING_LABEL $r"; fi; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'cites=$(perl -ne '"'while(/\\\\cite(?:\\[["'^]]*'"\\])?\\{(["'^}]+)'"\\}/g){for "'$k (split(/,/, $1)){ $k =~ s/''^'"\\s+|\\s+"'$//g; print "$k'"\\n\" if length "'$k;}}'"' chapters/theory/higher_genus_foundations.tex | sort -u); for c in "'$cites; do if ! rg -q -F "'"\\\\bibitem{"'$c}" bibliography/references.tex standalone/*.tex standalone/*.bib; then echo "MISSING_CITE $c"; fi; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'refs=$(perl -ne '"'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_foundations.tex | sort -u); for r in "'$refs; do hits=$(rg -n -F "$r" metadata/theorem_registry.md | wc -l | tr -d '"' '); if [ \""'$hits" = "0" ]; then printf "UNTRACKED %s'"\\n\" \""'$r"; fi; done | sed -n '"'1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
MISSING_LABEL app:coderived-models
app:curved-ainfty-formulas
app:homotopy-transfer
app:signs
ch:feynman
ch:heisenberg-frame
chap:deformation-theory
chap:koszul-pairs
comp:virasoro-m4
comp:w3-genus2-multichannel
conj:c2-cofiniteness-koszul-interaction
constr:explicit-convolution-linfty
constr:obstruction-recursion
constr:transfer-ainf
conv:higher-genus-differentials
conv:regime-tags
 succeeded in 52ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
MISSING_CITE AF15
Ara74
Boardman-conditional
Cliff19
DeligneM69
Drinfeld85
FBZ04
FP00
FP03
Fal84
Fay73
GeK98
Ger63
Griffiths68
HA
HZ86
 succeeded in 52ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
UNTRACKED app:coderived-models
app:curved-ainfty-formulas
app:homotopy-transfer
app:signs
ch:feynman
ch:heisenberg-frame
chap:deformation-theory
chap:koszul-pairs
comp:virasoro-m4
comp:w3-genus2-multichannel
conj:c2-cofiniteness-koszul-interaction
constr:explicit-convolution-linfty
constr:obstruction-recursion
constr:transfer-ainf
conv:higher-genus-differentials
conv:regime-tags

thinking
**Considering extraction methods**

I'm thinking about using `perl` to extract refs first, then applying `grep -R -F "\\label{$r}" chapters appendices` to see if I get a result. I’ll redirect any output to `/dev/null`, but if there's a match, I want to make sure to echo anything useful back. I’m curious about the earlier error with `rg`; it seemed odd. Maybe switching to `grep` will work better for this task.
exec
/bin/zsh -lc "perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/higher_genus_foundations.tex | sort -u | while IFS= read -r r; do grep -R -F \"\\\\label{"'$r}" chapters appendices >/dev/null || echo "$r"; done | sed -n '"'1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -R -n -F '\\label{app:coderived-models}' chapters appendices ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -R -n -F '\\label{chap:koszul-pairs}' chapters appendices ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -R -n -F '\\label{sec:coderived-models}' chapters appendices ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -R -n -F '\\label{sec:genus-spectral-complete}' chapters appendices ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{sec:coderived-models}' chapters appendices ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{app:coderived-models}' chapters appendices ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{chap:koszul-pairs}' chapters appendices ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{sec:genus-spectral-complete}' chapters appendices ." in /Users/raeez/chiral-bar-cobar succeeded in 88ms:
./chapters/theory/higher_genus_foundations.tex:4354:\label{sec:genus-spectral-complete}
chapters/theory/higher_genus_foundations.tex:4354:\label{sec:genus-spectral-complete}
 succeeded in 102ms:
./wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:983:./main.tex:1601: \phantomsection\label{app:coderived-models}% % planned appendix
./main.tex:1601: \phantomsection\label{app:coderived-models}% % planned appendix
 succeeded in 106ms:
./wave2_audit_20260413_001942/S02_bar_to_higher_genus.md:975:chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./audit_campaign_20260412_231034/T02_thm_B.md:1358:   180	\label{sec:coderived-models}
./main.tex:1807: \phantomsection\label{sec:coderived-models}%
./chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
 succeeded in 98ms:
./wave2_audit_20260413_001942/S13_concordance_to_body.md:275:     2	\label{chap:koszul-pairs}
./wave2_audit_20260413_001942/F04_definitions_complementarity.md:1210:     2	\label{chap:koszul-pairs}
./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:209:     2	\label{chap:koszul-pairs}
./wave2_audit_20260413_001942/F02_definitions_koszul.md:240:\label{chap:koszul-pairs}
./wave2_audit_20260413_001942/F02_definitions_koszul.md:290:     2	\label{chap:koszul-pairs}
./wave2_audit_20260413_001942/F02_definitions_koszul.md:455:2:\label{chap:koszul-pairs}
./audit_campaign_20260412_231034/T13_koszul_equivs.md:257:\label{chap:koszul-pairs}
./chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./audit_campaign_20260412_231034/T01_thm_A.md:379:\label{chap:koszul-pairs}
./audit_campaign_20260412_231034/T01_thm_A.md:1657:     2	\label{chap:koszul-pairs}
 succeeded in 35.25s:
app:coderived-models
part:bar-complex
part:characteristic-datum
part:physics-bridges
rem:feynman_genus_g
sec:conventions
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '3320,3388p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3320	\begin{itemize}
  3321	\item $\dzero$ is the genus-zero (classical) differential from BD
  3322	\item $t_k = \oint_{A_k} \omega_k$ are the $A$-period parameters arising from the Hodge decomposition of $H^1(\Sigma_g, \mathbb{C})$
  3323	\item $d_k$ are correction operators encoding quantum effects via integration over the $A$-cycle $\gamma_k$
  3324	\end{itemize}
  3325	
  3326	\emph{Explicit form.} For genus $g=1$ (elliptic case), there is one $A$-period $t_1 = \tau$, and:
  3327	\[\Dg{1} = \dzero + \tau \cdot d_{\text{elliptic}}\]
  3328	where $\tau$ is the modulus of the torus and $d_{\text{elliptic}}$ involves elliptic functions.
  3329	\end{definition}
  3330	
  3331	\begin{theorem}[Key property: \texorpdfstring{$\Dg{g}^{\,2} = 0$}{D(g) squared = 0}; \ClaimStatusProvedHere]\label{thm:quantum-diff-squares-zero}
  3332	\textup{[Regime: curved-central
  3333	\textup{(}i.e., curvature $\kappa$ is a central scalar;
  3334	the theorem proves that $\Dg{g}$ is \emph{flat}\/\textup{)};
  3335	all genera
  3336	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  3337	
  3338	The total corrected differential $\Dg{g}$ \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials}(ii))} satisfies $\Dg{g}^{\,2} = 0$.
  3339	\end{theorem}
exec
/bin/zsh -lc "rg -n -F 'app:coderived-models' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
293:see Appendix~\ref{app:coderived-models}).
407: $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
829: \textup{(}Appendix~\textup{\ref{app:coderived-models})}.

thinking
**Checking appendix labels**

I think I need to verify if the correct appendix label is actually "sec:coderived-models." It seems like I'm not having much luck finding that. I'll also check the `app:homotopy-transfer` at line 1558 to see if there’s anything there. Let's search for more information on these topics so I can clarify what I need! I'm curious about how everything connects.
exec
/bin/zsh -lc "rg -n -F 'app:homotopy-transfer' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'app:signs' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1167:(Appendix~\ref{app:signs}, \S\ref{sec:sign-dictionary-complete}).
 succeeded in 53ms:
1559: (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
exec
/bin/zsh -lc "rg -n -F '\\label{app:homotopy-transfer}' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{app:signs}' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./appendices/homotopy_transfer.tex:2:\label{app:homotopy-transfer}
 succeeded in 53ms:
./appendices/signs_and_shifts.tex:2:\label{app:signs}
exec
/bin/zsh -lc 'rg -n "base-change|base change|proper base|flat base|proper-base|basechange" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Reevaluating definitions**

I’m noticing something inconsistent with the definition of t_k. However, I remember that our audit surface relates to the target file, so I need to keep that connection in mind. I wonder if I need to adjust my understanding of t_k in this context. It’s essential to clarify these definitions so there’s no confusion moving forward, especially if they impact how I analyze the target file. Let's explore this further and ensure everything aligns!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '460,510p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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

thinking
**Inspecting theorem references**

I think theorem 801, specifically line 827, might reference appendix `app:coderived-models`. I should check that appendix to see if it confirms the equivalence mentioned. This feels like a necessary step to clarify things. I'll search for details in that appendix to verify what the theorem claims. Let’s ensure I have all the information right here! I want to make sure I'm thorough before jumping to conclusions.
exec
/bin/zsh -lc 'rg -n "equivalence|bar-cobar adjunction|coderived category|positive-energy|weight-by-weight SDR|SDR" chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/genus_complete.tex | sed -n '1380,1425p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Zhu|genus-\\"'$g'"\\"'$ conformal blocks|modular functor|finite-dimensional for all g|Huang" chapters/theory/higher_genus_foundations.tex chapters/theory/chiral_modules.tex chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4:\index{coderived category|textbf}
7:The bar-cobar adjunction at higher genus produces curved complexes
77:\index{coderived category!abstract definition|textbf}
79:The \emph{coderived category} and \emph{contraderived category}
105:Let $(C, d, h)$ be a CDG-coalgebra. There is an equivalence of
107:\begin{equation}\label{eq:co-contra-equivalence}
112:The equivalence is implemented by the functors
130:CDG-comodule is coacyclic, so the coderived category coincides
143:the coderived category reduces to the ordinary derived
150:\index{bar-cobar adjunction!coderived formulation}
165:coderived category
167:The Koszul duality equivalence
172:\eqref{eq:co-contra-equivalence}.
181:\index{coderived category!relative models|textbf}
188:a curved equivalence rather than a quasi-isomorphism) require
213:\begin{definition}[Weak equivalence of curved models]
216:is a \emph{weak equivalence} if it satisfies either of the following
229:The equivalence of (i) and (ii) holds for bounded-below filtrations
233:\begin{definition}[Provisional coderived category]
235:\index{coderived category!provisional|textbf}
 succeeded in 52ms:
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
 succeeded in 53ms:
  1380	pairs of pants; each sewing circle contributes one pair-of-pants
  1381	composition. Composition of two Hilbert--Schmidt operators is
  1382	trace class.
  1383	\end{proof}
  1384	
  1385	\begin{theorem}[General HS-sewing criterion; \ClaimStatusProvedHere]%
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
 succeeded in 53ms:
chapters/examples/free_fields.tex:2227:identifies $J_0$ with $\alpha_0$ at the Zhu algebra level
chapters/examples/free_fields.tex:2531:$J_0 \mapsto J_0 + k\lambda$. Under the Zhu algebra
chapters/examples/free_fields.tex:4875:(Zhu \cite{Zhu96}).
chapters/examples/free_fields.tex:4941:\emph{(3) Rationality:} Conformal blocks $\mathcal{V}(\Sigma_g, \vec{V})$ must be finite-dimensional, guaranteed by rationality (Zhu's theorem). The Verlinde formula ensures consistency with the OPE.
chapters/examples/free_fields.tex:4953:(3)~the Verlinde formula and finite-dimensionality of conformal blocks (Zhu \cite{Zhu96});
chapters/examples/free_fields.tex:5200:Zhu's theorem \cite{Zhu96} identifies $Z_\mathcal{A}(\tau)$ with a character in Zhu's module category. The modular-invariance properties of these characters (including the transformation weight $c/24$) are established by Zhu \cite[Thm.~4.4.2]{Zhu96} under rationality assumptions, which hold for the finite examples computed here (free fields, Heisenberg, Kac--Moody at positive integer level).
chapters/examples/free_fields.tex:5295:\begin{theorem}[Complete modular invariance classification \cite{Zhu96, MooreSeiberg89}; \ClaimStatusProvedElsewhere]\label{thm:modular-classification}
chapters/theory/higher_genus_foundations.tex:806:\index{modular functor!genus extension level}
chapters/theory/higher_genus_foundations.tex:864: Zhu~\cite{Zhu96}, then the spaces of conformal blocks
chapters/theory/higher_genus_foundations.tex:867: characters, and $\cA$ defines a modular functor.
chapters/theory/higher_genus_foundations.tex:930:Level~(v): $C_2$-cofiniteness implies, by Zhu's
chapters/theory/higher_genus_foundations.tex:931:theorem~\cite{Zhu96}, that the space of genus-$g$ conformal
chapters/theory/higher_genus_foundations.tex:5451:\index{modular functor!universality hierarchy}
chapters/theory/higher_genus_foundations.tex:5513: $\{V_{g,n}(\cA)\}$ assemble into a modular functor
chapters/theory/chiral_modules.tex:175:For a rational vertex algebra~$V$, the module category $\mathrm{Mod}_V$ carries a braided tensor structure via the fusion product (Huang--Lepowsky--Zhang~\cite{HLZ}), with braiding from the monodromy of conformal blocks on~$\mathbb{P}^1$. For $\widehat{\mathfrak{g}}_k$ at positive integer level, this is identified with the quantum group tensor product on $\mathcal{C}(U_q(\mathfrak{g}))$ via the KL equivalence (Theorem~\ref{thm:km-quantum-groups}).
chapters/theory/chiral_modules.tex:1531:by Huang--Lepowsky--Zhang~\cite{HLZ} using intertwining
chapters/theory/chiral_modules.tex:1841:\subsection{Zhu's algebra and module classification}
chapters/theory/chiral_modules.tex:1843:\begin{definition}[Zhu's algebra]\label{def:zhu-algebra}
chapters/theory/chiral_modules.tex:1844:\index{Zhu's algebra|textbf}
chapters/theory/chiral_modules.tex:1845:Zhu's algebra captures the genus-$0$ representation theory of a vertex algebra; for the Heisenberg algebra, $A(\mathcal{H}_k) \cong \mathbb{C}[x]$ is the polynomial algebra, reflecting the fact that Fock modules are parametrized by a single charge.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1040,1075p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1040	\label{subsec:ks-deformation-functor}
  1041	\index{Kodaira--Spencer map|textbf}
  1042	
  1043	The infinitesimal version of~\eqref{eq:bar-family} is
  1044	\begin{equation}\label{eq:ks-intro-hg}
  1045	\mathrm{KS} \colon T_{[\Sigma_g]}\overline{\mathcal{M}}_g
  1046	\;\xrightarrow{\;\sim\;}
  1047	H^1(\Sigma_g, T\Sigma_g)
  1048	\;\longrightarrow\;
  1049	\mathrm{HH}^2_{\mathrm{ch}}(\cA),
  1050	\end{equation}
  1051	sending an infinitesimal deformation of the curve to a deformation of
  1052	the bar complex
  1053	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}). The obstruction
  1054	to extending a first-order deformation lies in
  1055	$\mathrm{HH}^3_{\mathrm{ch}}(\cA)$.
  1056	
  1057	\subsection{The family index}
  1058	\label{subsec:why-ahat}
  1059	\index{A-hat genus@$\hat{A}$-genus!geometric derivation}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2000,2022p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2000	\emph{Step 5: Filtered Koszul dual.}
  2001	The bar coalgebra $\bar{B}(\cA)$ carries a filtration-compatible
  2002	coassociative coproduct $\Delta$ (from Step~1: the tensor-product
  2003	filtration is compatible with the deconcatenation coproduct). The
  2004	Koszul dual algebra is the continuous linear dual
  2005	$\cA^! := \bar{B}(\cA)^\vee$ with the dual filtration
  2006	$F_p(\cA^!) = (F_p\bar{B}(\cA))^\perp$; the chiral algebra structure
  2007	on~$\cA^!$ is the dual of the coalgebra structure: the product
  2008	$\mu^! = \Delta^\vee$ and the higher operations
  2009	$(m_k^!)^\vee = \Delta_k$ are obtained by dualizing the
  2010	bar coproduct and its iterated versions. This is a chiral algebra
  2011	(not merely a graded vector space) because the coalgebra axioms
  2012	dualize: coassociativity of~$\Delta$ gives associativity of~$\mu^!$,
  2013	and $d^2 = 0$ on $\bar{B}(\cA)$ gives $d^2 = 0$
  2014	on~$\cA^!$. By Step~2,
  2015	$\mathrm{gr}\,\cA^! = \mathrm{gr}\,\bar{B}(\cA)^\vee
  2016	= \bar{B}(\mathrm{gr}\,\cA)^\vee
  2017	= (\mathrm{gr}\,\cA)^!$.
  2018	Completeness of $\cA^!$ follows from completeness of
  2019	$\bar{B}(\cA)$ (Positselski~\cite[\S A.1]{Positselski11}).

thinking
**Evaluating theoretical statements**

I’m thinking about inspecting the file `chapters/theory/coderived_models.tex`, particularly around lines 242-251, to confirm some strong statements. I’ve read enough for now and identified a potential finding at line 408, where it mentions that "these categories are inequivalent in general; coderived category has strictly more objects." The appendix lines 92-98 clarify that when h≠0, derived no longer captures the curved theory, making the claim about inequivalence for this specific bar complex seem overclaimed. Good to note!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '284,299p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   284	\noindent
   285	\textbf{Categorical homes.}
   286	The strict differentials $\dzero$ and $\Dg{g}$ produce honest
   287	chain complexes; the bar complex equipped with either lives in
   288	the \emph{derived category}. The curved differential $\dfib$
   289	produces a curved dg coalgebra with $\dfib^{\,2} \neq 0$
   290	(for $\kappa \neq 0$); the bar complex equipped with $\dfib$
   291	lives in the \emph{coderived category}
   292	$D^{\mathrm{co}}$~(Positselski;
   293	see Appendix~\ref{app:coderived-models}).
   294	The derived/coderived comparison, established on the manuscript's
   295	flat-side comparison locus together with the coderived treatment of
   296	the curved model, ensures that the flat model carries the ordinary
   297	derived package while the curved model is its coderived counterpart.
   298	
   299	\noindent


 succeeded in 3m 08s:
chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./audit_campaign_20260412_231034/T01_thm_A.md:379:\label{chap:koszul-pairs}
./audit_campaign_20260412_231034/T01_thm_A.md:1657:     2	\label{chap:koszul-pairs}
./audit_campaign_20260412_231034/T13_koszul_equivs.md:257:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a074cd40/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-ab4d244b/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a7a899b6/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-ad4860d3/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-abc99e5a/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-ab0fb328/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a618b30c/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a35dd0a7/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-ae5ffa93/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a6b91d46/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a001fc1b/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a716d31f/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
./.claude/worktrees/agent-a78e4d88/chapters/theory/chiral_koszul_pairs.tex:2:\label{chap:koszul-pairs}
 succeeded in 3m 12s:
chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./main.tex:1807: \phantomsection\label{sec:coderived-models}%
./audit_campaign_20260412_231034/T02_thm_B.md:1358:   180	\label{sec:coderived-models}
./.claude/worktrees/agent-a074cd40/chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-a074cd40/main.tex:1722:  \phantomsection\label{sec:coderived-models}%
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/main.tex:1542:  \phantomsection\label{sec:coderived-models}%
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/appendices/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/main.tex:1542:  \phantomsection\label{sec:coderived-models}%
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/appendices/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-ab4d244b/chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-ab4d244b/main.tex:1722:  \phantomsection\label{sec:coderived-models}%
./.claude/worktrees/agent-a7a899b6/chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-a7a899b6/main.tex:1590:  \phantomsection\label{sec:coderived-models}%
./.claude/worktrees/agent-ad4860d3/chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-ad4860d3/main.tex:1722:  \phantomsection\label{sec:coderived-models}%
./.claude/worktrees/agent-abc99e5a/chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-abc99e5a/main.tex:1590:  \phantomsection\label{sec:coderived-models}%
./.claude/worktrees/agent-ab0fb328/chapters/theory/coderived_models.tex:180:\label{sec:coderived-models}
./.claude/worktrees/agent-ab0fb328/main.tex:1590:  \phantomsection\label{sec:coderived-models}%
 succeeded in 3m 12s:
./main.tex:1601: \phantomsection\label{app:coderived-models}% % planned appendix
./.claude/worktrees/agent-a074cd40/main.tex:1533:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/main.tex:1377:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/main.tex:1377:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-ab4d244b/main.tex:1533:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a7a899b6/main.tex:1401:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-ad4860d3/main.tex:1533:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-abc99e5a/main.tex:1401:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-ab0fb328/main.tex:1401:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a618b30c/main.tex:1401:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a35dd0a7/main.tex:1401:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-ae5ffa93/main.tex:1533:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a6b91d46/main.tex:1533:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a001fc1b/main.tex:1401:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a716d31f/main.tex:1533:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a78e4d88/main.tex:1377:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a7c35613/main.tex:1533:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a506436b/main.tex:1377:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a6d629eb/main.tex:1377:  \phantomsection\label{app:coderived-models}%             % planned appendix
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/main.tex:1377:  \phantomsection\label{app:coderived-models}%             % planned appendix
 succeeded in 3m 12s:
chapters/theory/higher_genus_foundations.tex:4354:\label{sec:genus-spectral-complete}
./chapters/theory/higher_genus_foundations.tex:4354:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a074cd40/chapters/theory/higher_genus_foundations.tex:4283:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/chapters/theory/higher_genus_foundations.tex:4140:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-ab4d244b/chapters/theory/higher_genus_foundations.tex:4283:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a7a899b6/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-ad4860d3/chapters/theory/higher_genus_foundations.tex:4283:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-abc99e5a/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-ab0fb328/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a618b30c/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a35dd0a7/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-ae5ffa93/chapters/theory/higher_genus_foundations.tex:4283:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a6b91d46/chapters/theory/higher_genus_foundations.tex:4283:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a001fc1b/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a716d31f/chapters/theory/higher_genus_foundations.tex:4283:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a78e4d88/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a7c35613/chapters/theory/higher_genus_foundations.tex:4283:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a506436b/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a6d629eb/chapters/theory/higher_genus_foundations.tex:4139:\label{sec:genus-spectral-complete}

thinking
**Organizing audit findings**

I’m thinking about how to organize my audit surface. While `Checked: 15` might seem small, I could justify using `Checked: 21` if we've reviewed 21 claim clusters. I need to count the exact local blocks audited. I have a list of blocks that amounts to 24. My plan includes stating: Checked: 24 | Findings: 13 | Verdict: FAIL. I want to ensure all claims are grounded and that each finding is concise, ideally with a clear fix.
thinking
**Clarifying formatting for links**

I realize we're not creating markdown links, but rather using plain text references like `chapters/theory/higher_genus_foundations.tex:344`. For multiline issues, I think mentioning just one line number could be sufficient—maybe the first offending line is a good idea. I’m considering using single line numbers to represent issues, for example, a representation like `...:357`. This helps keep things clear and concise in the documentation!
thinking
**Analyzing containment levels**

I’m thinking about inspecting lines 801 to 809 where it says “Each level is strictly contained in the next.” However, the chain I see, `iv ⊊ iii ⊊ ii ⊊ i`, seems to suggest the opposite direction. It's interesting how these two ideas might conflict! I really want to clarify this and understand how these connections work. I should take a closer look to resolve this inconsistency.
codex
The dependency pass is complete. The surviving findings are all grounded in lines I read; I’m collapsing them into the final audit list now, with exact fixes rather than generic objections.
Plan update
  ✓ Map the chapter’s foundation claims around genus-g fiber bar, spectral sequences, and base/base-change arguments
  ✓ Read each directly cited theorem/definition dependency and test whether hypotheses actually match the use
  → Assemble only re-verified findings with exact file:line references and concrete fixes

thinking
**Exploring spectral sequences**

I'm considering the genus spectral sequence at line 4379, where \( F^k = ⊕_{g≥k} \bar B^{(g)} \) uses separate genus complexes. It feels like there’s a layer of complexity here around how to interpret those components. I’ll need to think about how these genus complexes interact and what meanings they bring to the broader picture. It's essential to get these details right to ensure clarity in my understanding and explanations!
codex
- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:357` — PROBLEM: the proved-here Gauss--Manin proposition is not well-typed. It defines `\nabla^{GM}` on `R^q\pi_*(\cA^{\boxtimes n}\otimes\Omega^*_{\log})` using fiber holomorphic differentials `\omega_k` as if they were base 1-forms, and uses `t_k=\oint_{A_k}\omega_k` as coordinates even though the chapter later normalizes `\oint_{A_l}\omega_k=\delta_{kl}`, so these `t_k` are constants. The proof then switches to the different local system `R^q\pi_*\C` and never returns to the stated bar-complex object. FIX: downgrade `prop:gauss-manin-uncurving-chain` to a local analytic remark on the symplectic-frame cover of Teichmuller space, replace `\omega_k\otimes\partial_{t_k}` by genuine local base coordinates `du_\mu\otimes\nabla_\mu`, and explicitly state that only the relative de Rham/Gauss--Manin package is proved here unless a bar-complex lift is constructed.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:404` — PROBLEM: part (iii) of the same proposition overclaims a derived/coderived comparison “in general,” but the cited support `thm:cobar-resolution-scoped` is explicitly Koszul-locus-only and does not supply a comparison functor `D^{co}\to D^b`. FIX: add the Koszul-locus hypothesis everywhere this comparison is used, or replace the sentence by “no general comparison is proved here; only the Koszul-locus bar-cobar counit is available.”

- [HIGH] `chapters/theory/higher_genus_foundations.tex:465` — PROBLEM: `\kappa(\cA):=\sum_a\langle e_a,e^a\rangle` is declared for an arbitrary cyclic chiral algebra with no trace-class/finite-weight hypothesis, so the displayed sum need not define a scalar on the stated input class. FIX: either add a finiteness hypothesis such as positive energy with finite-dimensional graded pieces and absolute convergence, or make `\Theta_\cA^{\le 2}` the primary definition and present the basis-sum only as a finite-type formula under that extra hypothesis.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:668` — PROBLEM: the chain-level curvature proposition jumps from `c_1(\mathbb E,h_{Ar})=\pi_*[\omega_g^{Ar}]` to `\kappa(\cA)\lambda_g=\kappa(\cA)c_g(\mathbb E)`. A single pushed-forward `(1,1)`-form gives a first Chern class, not the top Chern class `c_g` for `g>1`; the displayed “two-step Chern--Weil projection” does not prove the claimed `\lambda_g` statement. FIX: rewrite part (ii) to conclude only the `c_1(\mathbb E)` statement, and move the `\kappa(\cA)\lambda_g` identification to a forward reference to `thm:genus-universality`/`thm:family-index` rather than deriving it here.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:776` — PROBLEM: `D^{(g)}_\cA := d_0+\kappa(\cA)\omega_g` adds a degree-2 form to a degree-1 differential and then calls the result a differential. The follow-up sentence “at `g=1`, the correction `\kappa\omega_1` is the Fay trisecant identity” also confuses a curvature term with an identity. FIX: replace the proposition by the curvature equation `d_{fib}^2=\kappa(\cA)\omega_g` or by the already-used strict differential `\Dg{g}` with genuine degree-1 correction operators; do not write `d_0+\kappa\omega_g` as a differential.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:807` — PROBLEM: the “five-level hierarchy” theorem contradicts itself. It opens with “each level is strictly contained in the next,” but later says only `(iv)\subsetneq(iii)\subsetneq(ii)\subsetneq(i)` and explicitly says level `(v)` is not comparable with `(iii)`. FIX: rewrite the theorem statement to match the proof: “Levels (i)-(iv) form a strict descending chain of increasingly restrictive conditions; level (v) implies (iv), (ii), and (i), but is not comparable with (iii).”

- [HIGH] `chapters/theory/higher_genus_foundations.tex:863` — PROBLEM: level (v) attributes genus-`g` finite-dimensional conformal blocks and a modular functor to `Zhu96`, but the file provides no higher-genus source and no local proof. This is an unsupported status upgrade inside a proved-here theorem. FIX: either restrict level (v) to the genus-1 Zhu-algebra/modular-character statement, or replace the citation with the actual higher-genus modular-functor theorem and state its precise hypotheses.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:1061` — PROBLEM: the family-index preface asserts that the genus-`g` bar family defines a virtual `K`-class and immediately applies GRR to `\bar B(\cA)|_{fiber}` without proving perfectness, finite rank, or any base-change package for this family. FIX: recast this paragraph as a roadmap: “On the proved uniform-weight scalar lane, Theorem `thm:family-index` later replaces the full bar family by the scalar `K`-class `\mathcal D_\cA^{(g)}=\kappa(\cA)\mathbb E` and applies GRR there.”

- [HIGH] `chapters/theory/higher_genus_foundations.tex:1944` — PROBLEM: `thm:convergence-filtered` invents a “unique closed element in the `gr`-harmonic complement” and then claims the filtered spectral sequence also collapses at `E_2` merely because the associated-graded one does. Neither statement is proved. FIX: delete item (2) or replace it by a noncanonical splitting statement, and weaken Step 4 to a pure convergence/comparison claim unless you add an independent degree argument forcing higher differentials to vanish on the filtered complex itself.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:2004` — PROBLEM: the same theorem flatly identifies the Koszul dual algebra with the continuous dual of the bar coalgebra, `\cA^!:=\bar B(\cA)^\vee`. That is the barred object’s linear dual, not the Koszul dual defined in this programme. FIX: replace Step 5 by the four-object template: first define `\cA^i:=H^*(\bar B(\cA))`, then `\cA^!:=(\cA^i)^\vee`; if you need `\bar B(\cA)^\vee`, name it explicitly as the continuous dual of the bar coalgebra and stop calling it the Koszul dual.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:3746` — PROBLEM: `thm:concrete-quantum-differential` is still a placeholder disguised as a theorem. The operator `\delta_{\gamma^*}` is undefined, “virtual puncture” is undefined, and the proof cites “associativity of the Leray filtration” and “exactness of the total complex” instead of an actual construction. FIX: either define `d^{(1)}` and every `d^{(k)}` as concrete endomorphisms with domains/codomains and filtration behavior, or downgrade the whole theorem to a heuristic remark and keep only the already proved statements `\dfib^2=\kappa\omega_g` and `\Dg{g}^2=0`.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:4379` — PROBLEM: the genus spectral sequence is not built from a defined filtered complex. `F^k\bar B(\cA)=\bigoplus_{g\ge k}\bar B^{(g)}(\cA)` is only a direct sum of separate genus complexes; the section never constructs a single total complex with a differential preserving this filtration, and the proof later introduces a different “genus expansion” differential after the fact. FIX: first define a total genus-completed complex, e.g. `\bar B^{tot}(\cA)=\prod_{g\ge0}\hbar^{2g-2}\bar B^{(g)}(\cA)`, specify its differential, prove filtration preservation, and only then define the spectral sequence; otherwise delete the whole section.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:4449` — PROBLEM: the explicit `E_2`-page formula is mathematically unprepared: `\mathcal M_k` is undefined, `H^p(\mathcal M_1,\mathcal M_k\otimes H^q)=\bigoplus_k\mathcal M_k\otimes H^q` is asserted without any sheaf/local-system definition, and the subsequent identification of `d_2` with Kodaira--Spencer is simply announced. FIX: replace the displayed genus-1 formula by the abstract Leray expression `H^p(\mathcal M_g,\underline H^q)`, define the relevant local system if modular forms are really intended, and move the Kodaira--Spencer identification to a separate proposition with an actual proof.

- [HIGH] `chapters/theory/higher_genus_foundations.tex:6089` — PROBLEM: `prop:bar-tautological-filtration` stacks three unsupported upgrades: it places `E_2` classes in the tautological ring merely from a VHS input, it calls `d_2` the Kodaira--Spencer map without constructing that identification, and it says `\psi_1\in H^1(\overline{\mathcal M}_{g,1})`, which is wrong even on the chapter’s own grading conventions. FIX: change the proposition to a cautious remark; replace `H^1` by `H^2` where `\psi_1` appears; and remove the tautological-ring and `d_3`/Massey-product claims unless you add separate proofs.

- [CRITICAL] `chapters/theory/higher_genus_foundations.tex:6563` — PROBLEM: the loop-order filtration is descending, but `prop:loop-filtration-compatible` proves only `d_{FT}(F^\ell)\subset F^{\ell-1}`, not `d_{FT}(F^\ell)\subset F^\ell`. So the differential does not preserve the filtration, and `thm:loop-order-spectral-sequence` has no spectral sequence to talk about. FIX: reverse the filtration convention to an ascending filtration `F_\ell:=\bigoplus_{b_1(\Gamma)\le \ell}`, rewrite the associated graded and bidegrees accordingly, and then rederive `d_0`/`d_1` with the corrected indexing.

- [MEDIUM] `chapters/theory/higher_genus_foundations.tex:288` — PROBLEM: the chapter says `(\bar B^{(g)}(\cA),\dfib)` is a curved dg coalgebra in the coderived category, but later at `729-736` it says `\dfib` is not a coderivation of the deconcatenation coproduct. Those two claims are incompatible in the ordinary CDG-coalgebra sense. FIX: standardize the language: either prove coderivation, or replace every “curved dg coalgebra” claim here by the weaker terminology used in `chapters/theory/coderived_models.tex:193-210` (“filtered curved factorization model”).

- [LOW] `chapters/theory/higher_genus_foundations.tex:293` — PROBLEM: the chapter consistently cites `Appendix~\ref{app:coderived-models}`, but the actual live label in the coderived appendix is `sec:coderived-models` (`chapters/theory/coderived_models.tex:180`); `app:coderived-models` is only a phantom label in `main.tex`. FIX: replace `app:coderived-models` by `sec:coderived-models` at lines `293`, `407`, and `829`, or rename the appendix label once and use it consistently.

## Summary
Checked: 24 | Findings: 16 | Verdict: FAIL
tokens used
189,488
