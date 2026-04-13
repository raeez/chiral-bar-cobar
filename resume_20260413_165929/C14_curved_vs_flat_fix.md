# C14_curved_vs_flat_fix (482s)

These files already had unrelated worktree edits; the items below are only my hunks.

- PROBLEM at [bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:438): the genus-`g\ge 1` paragraph spoke about “ordinary bar-complex cohomology” on the higher-genus bar-object surface without naming that ordinary cohomology belongs to the square-zero comparison differential, not the curved fiber operator. EXACT edit applied: replaced that sentence with `The square-zero total comparison differential $d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology ... whereas the raw higher-genus fiber operator satisfies $\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on the coderived bar-object surface.`

- PROBLEM at [coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:1004): the H1-closure remark still left the off-Koszul promotion target too implicit, so the reader could still read “ordinary cohomology” as if it applied directly to the curved statement. EXACT edit applied: changed the summary to `ordinary quasi-isomorphism on the square-zero Koszul lane ... and no silent promotion of the off-Koszul curved statement back to ordinary cohomology. The remaining issue is exactly the flat-side collapse input needed for that promotion.` Also, at [coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:1033), I rewrote the spectral-sequence evidence to say the `E_1` page abuts to ordinary cohomology only on the square-zero Koszul lane, while off the Koszul locus it controls `coderived coacyclicity of the curved cone rather than ordinary cohomology`.

- PROBLEM at [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3173): the curved `\dfib^{\,2}` discussion rejected ordinary cohomology, but it did not explicitly name the flat comparison differential or the curved complex being excluded. EXACT edit applied: changed the sentence to `Otherwise one must pass either to the strict flat comparison differential $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived framework; ordinary cohomology of the curved fiber complex $(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.` Also, at [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3430), I made the same flat-side comparison explicit by changing the corollary tail to `whose cohomological shadow appears only after passage to the flat comparison differential $\Dg{g}$ or the corresponding Chern--Weil class.`

Verification: I re-grepped `chapters/theory` for `ordinary cohomology`, curved/cohomology pairings, and spectral-sequence language. The remaining hits in `bar_cobar_adjunction_inversion.tex`, `chiral_hochschild_koszul.tex`, `higher_genus_foundations.tex`, and `higher_genus_complementarity.tex` already explicitly restrict ordinary cohomology to square-zero flat representatives or to coderived comparisons, so I left them unchanged. I did not run a TeX build.


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
session id: 019d8809-5b8c-78b1-859f-8158f8f6d256
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


Fix curved-vs-flat confusion (D08 findings).
Search Vol I theory chapters for 'd\^2' and 'spectral sequence' and 'cohomology'.
Where ordinary cohomology is applied to curved complexes (d^2=kappa*omega_g), add
explicit flat-side comparison or coderived qualifier. Fix each instance.
mcp startup: no servers

thinking
**Producing findings and edits**

I'm thinking about producing multiple findings with the necessary edits and including verification. It might be useful to reference "D08 findings" maybe in the red team summary. I should search for that specifically. I also need to make sure I read the required files thoroughly. So, let's get started with the commentary update! I'm curious how these pieces will fit together.
codex
Using `deep-beilinson-audit` and `beilinson-rectify` here. I’m first loading the required constitutional files and locating every Vol I theory-chapter hit for `d^2`, `spectral sequence`, and `cohomology` before I classify which ones actually apply flat cohomology language to the curved `d^2=\kappa\omega_g` side.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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

exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the full target file
- the directly cited dependencies

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


thinking
**Searching for target files**

I need to find specific files in the Vol I theory chapters that mention terms like 'd^2', 'spectral sequence', and 'cohomology'. Essentially, I'm looking for instances where ordinary cohomology is applied to curved complexes and planning to add explicit comparisons. It seems I should search through all theory chapters, maybe located in chapters/theory. I could possibly use a tool for searching like rg or explore to gather a list of candidate files. It might be best to use an explorer subagent to quickly find the relevant sections.
thinking
**Using explorer for codebase tasks**

It looks like I need to follow developer instructions by using an explorer for codebase questions, particularly for files in the repository. I should spawn an explorer agent to help identify candidate areas where ordinary cohomology is misused within the Vol I theory chapter. The explorer can search for specific patterns and flag any issues. Even though the developer suggests trusting explorer results without re-reading, I might still want to check the flagged files for correctness. So, I think using the explorer for broad mapping before inspecting files directly is compliant. Let's initiate the explorer!
codex
I’ve loaded the constitutional surface. Next I’m mapping every theory-chapter hit and narrowing to the ones where flat cohomology language leaks onto the curved `d^2=\kappa\omega_g` side; after that I’ll patch only those files with the minimum qualifier needed.
collab spawn_agent(call_pru0y2fKzKbasEKj3WJPXcb3, prompt="<task>Map the Vol I theory-chapter audit surface for curved-vs-flat confusion. Search under chapters/theory for hits on …")
spawn_agent(call_pru0y2fKzKbasEKj3WJPXcb3, prompt="<task>Map the Vol I theory-chapter audit surface for curved-vs-flat confusion. Search under chapters/theory for hits on …") pending init:
  agent: 019d8809-e056-7ea0-ba4d-c069ec72c988
mcp startup: no servers
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc "rg -n \"d\\\\\\"'^2" chapters/theory' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc 'rg -n -F "d''^2" chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:14:%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
chapters/theory/higher_genus_modular_koszul.tex:10004:is the cohomological class of the $d^2$-residual at genus~$g$.
chapters/theory/higher_genus_modular_koszul.tex:10030:geometric class (the $d^2$-residual projected to the one-channel
chapters/theory/higher_genus_modular_koszul.tex:33892:rank~$d^2 = 4$\textup{)}:
chapters/theory/higher_genus_modular_koszul.tex:33904:  $r = d^2 = 4$:
chapters/theory/higher_genus_modular_koszul.tex:34044:$\Sigma_g \setminus \{0\}$ has rank $d^2$
chapters/theory/higher_genus_modular_koszul.tex:34050:  = d^2(1 - 2g).
chapters/theory/higher_genus_modular_koszul.tex:34052:Explicitly: $\chi = d^2 \cdot \chi_{\mathrm{top}}
chapters/theory/higher_genus_modular_koszul.tex:34065:has rank $r = d^2$ (the fibre is $V \otimes V$ with
chapters/theory/higher_genus_modular_koszul.tex:34067:$\chi = d^2(1 - 2g)$.
chapters/theory/higher_genus_modular_koszul.tex:34081:  = -3 \cdot 9 = -3d^2$.
chapters/theory/quantum_corrections.tex:9:ensures $d^2 = 0$; at genus~$g \geq 1$, it deforms by coherent
chapters/theory/quantum_corrections.tex:100:These relations are the integrability conditions for the geometric bar complex: $d^2 = 0$ is flatness of the Knizhnik--Zamolodchikov connection on the local system of conformal blocks \cite[Section~3.4]{BD04}.
chapters/theory/quantum_corrections.tex:105:with differential $d = d_{\text{internal}} + d_{\text{residue}} + d_{\text{deRham}}$. The condition $d^2 = 0$ says that the differential defines a flat connection on an infinite-dimensional bundle.
chapters/theory/quantum_corrections.tex:112:The flatness condition $d^2 = 0$ is equivalent to the Maurer--Cartan equation:
chapters/theory/quantum_corrections.tex:122:For $d^2 = 0$, we need:
chapters/theory/quantum_corrections.tex:1329:while the full Borcherds differential gives $d^2 = 0$ is \emph{precisely}
chapters/theory/quantum_corrections.tex:1332:$j'_{(p,q,r)}$ are the coherent homotopies that restore $d^2 = 0$ at
chapters/theory/fourier_seed.tex:27:\item \emph{Kernel.} The identity $d^2 = 0$ is a formal consequence
chapters/theory/poincare_duality_quantum.tex:1120:To verify $d^2 = 0$ for this sign convention, consider a tree with three vertices and two edges $e_1, e_2$. The two ways to contract both edges give:
Plan update
The task is an adversarial audit plus repair on the curved-vs-flat surface inside Vol I theory chapters. I’m first identifying all true positives, then patching only the files that actually misuse ordinary cohomology language on the curved side, then running narrow verification.
  → Map all `d^2`, `spectral sequence`, and `cohomology` hits in `chapters/theory` and classify true positives for curved-vs-flat confusion
  • Read the flagged passages in context, determine the minimum truthful qualifier or flat-side comparison needed, and prepare edits
  • Apply minimal fixes in the affected theory files only
  • Run targeted grep verification to confirm no unqualified curved-side ordinary cohomology language remains in scope
exec
/bin/zsh -lc 'rg -n "spectral sequence" chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 491

chapters/theory/higher_genus_modular_koszul.tex:617:At each genus $g \geq 1$, the PBW spectral sequence of
chapters/theory/higher_genus_modular_koszul.tex:776:\index{PBW spectral sequence!higher genus concentration}
chapters/theory/higher_genus_modular_koszul.tex:787:Then for every genus~$g \geq 1$, the PBW spectral sequence for the
chapters/theory/higher_genus_modular_koszul.tex:918:\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
chapters/theory/higher_genus_modular_koszul.tex:977:\index{PBW spectral sequence!mixed map factorization|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1025:\index{PBW spectral sequence!genus-1 degeneration|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1031:$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
chapters/theory/higher_genus_modular_koszul.tex:1221:spectral sequence converges in each bidegree, and
chapters/theory/higher_genus_modular_koszul.tex:1368:\index{PBW spectral sequence!all-genera degeneration|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1380:generic level $k \notin \Sigma(\fg)$, the PBW spectral sequence
chapters/theory/higher_genus_modular_koszul.tex:1552:killed at finite page of the PBW spectral sequence,
chapters/theory/higher_genus_modular_koszul.tex:1628:\index{PBW spectral sequence!all-genera degeneration for Virasoro|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1638:spectral sequence for the genus-$g$ bar complex
chapters/theory/higher_genus_modular_koszul.tex:1840:\index{PBW spectral sequence!unique-weight-2 criterion|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1841:\index{PBW spectral sequence!universal semisimple enrichment-killing|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1859:spectral sequence satisfies
chapters/theory/higher_genus_modular_koszul.tex:1908:spectral sequence different from the one where the
chapters/theory/higher_genus_modular_koszul.tex:2002:\index{PBW spectral sequence!hook-type W-algebras|textbf}

thinking
**Considering findings location**

I need to check if I can locate the D08 findings, possibly in the red team. Maybe I can use the explorer tool for that, but I'll hold off for now. It might also be good to read the AGENTS sections regarding the curved part. I feel like I have enough information for the moment, so waiting on using the explorer seems like a reasonable choice.
collab wait(call_WDjms6JyM8jEmaz1xbQwpHHt)
  receivers: 019d8809-e056-7ea0-ba4d-c069ec72c988
exec
/bin/zsh -lc 'rg -n -C 2 "cohomology" chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1005-the Koszul lane, coderived equivalence for all complete augmented
1006-chiral algebras with finite-dimensional bar complex, and no silent
1007:promotion of the off-Koszul statement back to ordinary cohomology.
1008-The remaining issue is exactly the collapse input needed for that
1009-promotion.
--
1036- has the same strict associated-graded $E_1$ page on and off the
1037- Koszul locus; the difference is whether that page controls ordinary
1038: cohomology or coderived coacyclicity.
1039-\item \emph{Completed Yangian case.}
1040- Corollary~\ref{cor:completed-bar-cobar-yangian}.
exec
/bin/zsh -lc "sed -n '990,1045p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\textup{(}Theorem~\ref{thm:stratified-conservative-restriction}\textup{)},
$K$ is coacyclic in the factorization sense.
Therefore $\varepsilon$ becomes an isomorphism in
$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$.
\end{proof}

\begin{remark}[Closure of structural gap~H1]
\label{rem:H1-closure}
\index{structural gaps!H1 closed}
Theorem~\ref{thm:off-koszul-ran-inversion} resolves
structural gap~H1 (Remark~\ref{rem:structural-gaps}):
the coderived Ran-space formalism is now established.
Combined with the strict Koszul-locus inversion of
Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
proved package on the present surface: ordinary quasi-isomorphism on
the Koszul lane, coderived equivalence for all complete augmented
chiral algebras with finite-dimensional bar complex, and no silent
promotion of the off-Koszul statement back to ordinary cohomology.
The remaining issue is exactly the collapse input needed for that
promotion.
exec
/bin/zsh -lc "sed -n '930,1010p' chapters/theory/e1_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\cF^{\mathrm{ord}}_n))$ collapses at $E_2$ in characteristic~$0$:
group cohomology of a symmetric group over~$\bQ$ is concentrated
in degree zero.

(ii) When $S(z) \neq \tau$, the monodromy of the KZ connection
on $U_n(X)$ is governed by the Drinfeld associator
$\Phi_{\mathrm{KZ}} \in \exp(\hat{\mathfrak{t}}_3)$,
and the $\Sigma_n$-coinvariant projection annihilates the
$\Sigma_n$-non-invariant Eulerian components. The resulting
kernel is a $\mathrm{GRT}_1$-torsor at each degree $n \ge 3$
(at degree $2$ the symmetric group is $\Sigma_2$ and the kernel
consists of the $R$-matrix data $r(z)$ modulo its scalar
$\Sigma_2$-coinvariant $\av(r(z))$).
\end{proof}

\begin{remark}[Ordered chiral homology and the bar complex]
\label{rem:ordered-ch-hom-bar}
\index{ordered chiral homology!bar complex relationship}
The algebraic bar complex $\barB^{\mathrm{ord}}(\cA)$ computes the
ordered chiral homology on the formal disk~$D$: the degree-$n$
exec
/bin/zsh -lc 'rg -n -C2 "kappa" chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
12-is the genus-$0$ binary component of the MC element
13-$\Theta_\cA \in \MC(\gAmod)$; the degree-$2$ projection of
14:$\Theta_\cA$ is the modular characteristic $\kappa(\cA)$.
15-Theorem~B (Theorem~\ref{thm:bar-cobar-inversion-qi}) says
16-that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
--
71-\item \emph{Curved-central} ($d_0^{\,2} \neq 0$,
72- $\mu_0 \in Z(A)$): completed bar-cobar, geometric curvature
73: $d_{\mathrm{fib}}^2 = \kappa \cdot \omega_g$ (affine algebras, Virasoro);
74-\item \emph{Filtered-complete} (non-quadratic OPE):
75- $I$-adic completion required, work in coderived category
--
94-(Chapter~\ref{chap:higher-genus}) amounts to deforming the
95-differential by curvature. The curved extension provides the
96:framework in which $\kappa(\cA) \cdot \omega_g$ and the shadow
97-obstruction tower $\Theta_\cA^{\leq r}$ operate.
98-
--
135- matrix-valued meromorphic function satisfying the classical
136- Yang--Baxter equation. Its $\Sigma_2$-coinvariant is the scalar
exec
/bin/zsh -lc 'rg -n -C 2 "cohomology" chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
16-that~$\tau_\cA$ is \emph{acyclic}: the twisted tensor
17-product $\cA \otimes_{\tau_\cA} \barBch(\cA)$ has trivial
18:cohomology, so the counit
19-$\psi \colon \Omegach(\barBch(\cA)) \xrightarrow{\;\sim\;} \cA$
20-is a quasi-isomorphism on the Koszul locus.
--
436-\emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
437-\textup{(}$h \neq 0$\textup{)}.}
438:Ordinary bar-complex cohomology collapses on the higher-genus
439-bar-object surface
440-\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
--
741-\mathrm{Vir}_c^! \cong \mathrm{Vir}_{26-c},
742-\end{equation}
743:since $c(k) + c(k') = 2\operatorname{rank}(\mathfrak{sl}_2) + 4h^\vee\dim\mathfrak{sl}_2 = 2 + 24 = 26$ by Theorem~\ref{thm:central-charge-complementarity}(b) (the $\mathcal{W}$-algebra central-charge sum; this is the Virasoro-family formula, not the affine KM formula $c + c' = 2\dim\mathfrak{g}$). Physically, matter--ghost duality pairs a matter system at central charge~$c$ with ghosts at $c_{\mathrm{ghost}} = 26 - c$. In particular, $\mathrm{Vir}_{26}^! \cong \mathrm{Vir}_0$, consistent with bosonic string BRST cohomology at ghost number zero.
744-
745-At the M/S level, the completed dual has infinitely many primitive cumulants ($\Delta_{\mathrm{Vir}}(t) = t^3 + 2t^5 + \cdots$; Definition~\ref{def:primitive-defect-series}). The MC4 structural framework is proved (Theorem~\ref{thm:completed-bar-cobar-strong}); the residual H-level target identification is the subject of Example~\ref{ex:winfty-completion-frontier}.
--
1235-Then:
1236-\begin{enumerate}
exec
/bin/zsh -lc 'rg -n -C2 "curved" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1-%% ===== Editorial bridge: the inversion half of the chapter =====
2-%%
3:%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
4:%% established the adjunction Omega^ch -| barB^ch and the curved A-infty
5-%% framework that supports it off the quadratic locus. This second half
6-%% proves that the adjunction inverts: Theorem B says
--
29-cohomology requires an extra collapse input. The strict proof uses
30-the square-zero bar-cobar spectral sequence only on the Koszul lane.
31:The curved proof uses the coderived bar-degree filtration: the
32-curvature term lies in positive filtration, so the
33-associated-graded $E_1$ page is strict, while coacyclicity of the
--
37-
38-\section{Non-quadratic chiral algebras}
39:\label{sec:filtered-vs-curved-comprehensive}
40-
41-\label{sec:bar-convergence-overview}% see thm:bar-convergence below for the canonical theorem
42-The four-regime hierarchy (Convention~\ref{conv:regime-tags})
43-classifies chiral algebras by their bar-complex behavior:
exec
/bin/zsh -lc "sed -n '2320,2395p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chiral version used here.
Because $\mathcal{A}^!$ is generated in weight~$1$ with quadratic
relations, the bar cohomology is concentrated on the diagonal in the
bigrading by cobar degree and internal degree.
Thus on the $E_1$ page, where the differential is
$d_0=d_{\bar B}$, one has $E_1^{p,q}=0$ for $q\neq 0$.
The $d_1$ differential comes from $d_{\text{cobar}}$, so the same
diagonal concentration persists to $E_2$.
For $r\ge 2$, the differential
$d_r\colon E_r^{p,q}\to E_r^{p+r,q-r+1}$ changes the second grading,
so with $E_2^{p,q}$ supported only at $q=0$, either its source or its
target vanishes.
Hence every $d_r$ for $r\ge 2$ is zero, and the spectral sequence
collapses at $E_2$.
\end{proof}

\begin{remark}[Square-zero boundary of the spectral-sequence proof]
\label{rem:spectral-sequence-square-zero-boundary}
Theorems~\ref{thm:bar-cobar-spectral-sequence}
and~\ref{thm:spectral-sequence-collapse} are statements about filtered

thinking
**Analyzing spectral sequence usage in curved contexts**

I’m digging into parts where spectral sequences or ordinary cohomology are applied to curved objects without proper coderived warnings, focusing on `coderived_models.tex`. I want to identify statements that might incorrectly apply these tools by searching for key terms like “spectral sequence,” “curved,” and “cohomology” to see if any caution is missing.
exec
/bin/zsh -lc 'rg -n "spectral sequence" chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
314:\begin{proposition}[Coderived bar-degree spectral sequence;
317:\index{coderived category!bar-degree spectral sequence|textbf}
380:bar-degree spectral sequence collapses.
771:bounded-below spectral sequence with acyclic associated graded
781:on each stratum implies the associated graded spectral sequence
1034: The coderived bar-degree spectral sequence
wait(call_WDjms6JyM8jEmaz1xbQwpHHt) timed out:
exec
/bin/zsh -lc "sed -n '300,360p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

For (b): the PBW filtration by conformal weight is exhaustive,
decreasing, preserved by all three components of the bar differential,
and satisfies $m_0^{(g)} \in F^1$ because the curvature involves at
least one OPE contraction. At associated graded level, the
differential reduces to $\dzero$, which is strict.

For (c): Verdier duality preserves the PBW filtration
(it exchanges weight~$n$ generators with weight~$n$ cogenerators in
the Koszul dual) and commutes with the bar differential. Hence it
descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ and the
eigenspace decomposition is well-defined.
\end{proof}

\begin{proposition}[Coderived bar-degree spectral sequence;
\ClaimStatusProvedHere]
\label{prop:coderived-bar-degree-spectral-sequence}
\index{coderived category!bar-degree spectral sequence|textbf}
\index{bar-cobar inversion!coderived filtration}
Let

thinking
**Waiting and searching strategies**

It seems like the explorer timed out, and I can poll again. While I’m waiting, maybe I should think about using exec_command to search myself, since I need some progress. However, the instructions say to check with explorers first. Since I’ve already asked, I could consider a manual search if the explorer is too slow. But, maybe it’s best to wait a bit longer and poll again.
codex
The audit surface is larger than a single-file patch, so I’ve split it into a precise pass: first classify true positives, then rewrite only those sentences where curved `d^2=\kappa\omega_g` is being treated with ordinary flat cohomology language.

Plan:
1. Map all theory-chapter hits for `d^2`, `spectral sequence`, and `cohomology`, and discard flat-only passages.
2. Read each remaining passage in local proof context and decide the minimum truthful repair: either an explicit flat-side comparison or a coderived/curved qualifier.
3. Patch only the affected theory files.
4. Re-grep the touched surface to confirm the ambiguity is gone and no new drift was introduced.
exec
/bin/zsh -lc "sed -n '30,110p' chapters/theory/derived_langlands.tex" in /Users/raeez/chiral-bar-cobarcollab wait(call_HkggvV8vJeV7sNtjFIVXeLpk)
  receivers: 019d8809-e056-7ea0-ba4d-c069ec72c988
 succeeded in 50ms:
%: formula from CLAUDE.md C3; k=0 -> dim(g)/2; k=-h^v -> 0 verified
At generic level, $\kappa(\widehat{\fg}_k) \neq 0$ and the bar complex is curved:
$d^2 \neq 0$, no cohomology, no geometry. At the critical level
$k = -h^\vee$, the numerator $k + h^\vee$ vanishes, $\kappa(\widehat{\fg}_{-h^\vee}) = 0$,
and the bar complex becomes an honest chain complex. The cohomology
that appears is the algebra of differential forms on opers:
\[
H^n\bigl(\barB(\widehat{\fg}_{-h^\vee})\bigr)
\;\cong\;
\Omega^n\bigl(\mathrm{Op}_{\fg^\vee}(D)\bigr)
\qquad\text{for all } n \ge 0.
\]
This is Theorem~\ref{thm:oper-bar-dl}. It does not prove the full
categorical localization; it identifies the chain-level mechanism from
which the oper side of the Frenkel--Gaitsgory programme emerges.

To see why no other construction yields this identification, observe
the dichotomy. At generic level, the curvature $\kappa(\widehat{\fg}_k) \neq 0$
obstructs the formation of cohomology: the bar complex is a curved
dg-coalgebra with $d^2 = \kappa(\widehat{\fg}_k) \cdot \omega_1 \neq 0$, and no
exec
/bin/zsh -lc "sed -n '4950,5050p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
with differential assembled from the coface maps $\delta_0,\ldots,\delta_n$.
For $M=C_\Delta$, this is precisely the
annular bar complex: the coface maps $\delta_1,\ldots,\delta_{n-1}$
produce $d_\Delta$ (non-wrapping boundary collisions), and the
coface maps $\delta_0$ and $\delta_n$ produce $d_{\mathrm{wrap}}$
(the wrap-around at the seam). The internal differential $d_{\mathrm{int}}$
and collision residue $d_{\mathrm{res}}$ are carried along as the
internal structure of each tensor factor.

The second equivalence is
Theorem~\ref{thm:HH-coHH-homology}, which identifies
$\coHoch^{\mathrm{ch}}_\bullet(C,C_\Delta)\simeq
\HH^{\mathrm{ch}}_\bullet(\cA)$ via the bimodule/bicomodule
equivalence of Theorem~\ref{thm:bimod-bicomod}.
\end{proof}

\subsection{Connection to the modular operad at genus~$1$}

\begin{remark}[The annular bar complex and the modular
$E_1$-chiral structure]

thinking
**Identifying potential curved-vs-flat confusions**

I'm gathering specific references where the theory chapter might cause confusion between curved and flat cases, especially where ordinary cohomology or spectral sequences are applied in contexts with curvature. I'll highlight key passages that mention these issues and consider searching broader chapter files for additional unclear segments. This way, I can map out surfaces where the user’s question about curved-versus-flat conceptual clarity is most relevant.
exec
/bin/zsh -lc "sed -n '3700,3755p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
decomposes as:
\begin{equation}
\Dg{g} = d^{(0)} + d^{(1)} + d^{(2)} + \cdots
\end{equation}
where, for a \emph{fixed} genus~$g$, the component $d^{(k)}$ shifts the Leray filtration
on $\bar{B}^{(g)}(\mathcal{A})$ by $k$ base degrees
(see Remark~\ref{rem:differential-notation} below).

The strict nilpotence condition $\Dg{g}^{\,2} = 0$ decomposes into:
\begin{align}
(d^{(0)})^2 &= 0 \quad \text{(genus 0 exactness)}\\
\{d^{(0)}, d^{(1)}\} &= 0 \quad \text{(genus 1 compatibility)}\\
\{d^{(0)}, d^{(2)}\} + (d^{(1)})^2 &= 0 \quad \text{(genus 2 relation)}\\
&\vdots
\end{align}
\end{theorem}

\begin{proof}[Proof via spectral sequence]
Consider the Leray spectral sequence for the universal configuration space fibration:
\begin{equation}
exec
/bin/zsh -lc 'rg -n "ordinary cohomology" chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1678: bar-degree spectral sequence degenerates to ordinary cohomology on
chapters/theory/bar_cobar_adjunction_inversion.tex:1983: is still detected by ordinary cohomology.
chapters/theory/bar_cobar_adjunction_inversion.tex:1987: coderived bar-degree filtration degenerates to ordinary cohomology.
chapters/theory/coderived_models.tex:1007:promotion of the off-Koszul statement back to ordinary cohomology.
chapters/theory/cobar_construction.tex:3182:ordinary cohomology of the curved fiber complex is not the correct
chapters/theory/chiral_hochschild_koszul.tex:3747:$\Dg{g}\big|_{[\Sigma_g]}$ computes the same ordinary cohomology as
chapters/theory/chiral_hochschild_koszul.tex:3750:coderived side rather than in ordinary cohomology.
exec
/bin/zsh -lc "sed -n '1660,1705p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 is coacyclic. Equivalently, $\psi_X$ is an isomorphism in
 $D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$, without any
 Koszulness hypothesis.

\item \emph{Coderived bar-degree filtration.}
 On the curved cone $K_\psi$, the bar-degree filtration yields the
 coderived spectral sequence of
 Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
 $E_1$ page is computed from the strict associated-graded differential
 $\operatorname{gr}^0 d$; the curvature relation
 $\dfib^{\,2} = \kappa(\mathcal{A}) \cdot \omega_g$ is absorbed into
 positive filtration and does not obstruct the $E_1$ page.
 On the square-zero Koszul lane this reduces to
 Theorems~\ref{thm:bar-cobar-spectral-sequence}
 and~\ref{thm:spectral-sequence-collapse}.

\item \emph{Promotion back to ordinary quasi-isomorphism.}
 If $\kappa(\mathcal{A}) = 0$, or more generally if the coderived
 bar-degree spectral sequence degenerates to ordinary cohomology on
 the relevant off-Koszul locus
exec
/bin/zsh -lc "sed -n '1960,2010p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\item \emph{Off-locus obstruction.}
 The first obstruction is the first bar class off the Koszul
 diagonal. Once $H^*(\barB_X(\cA))$ contains a class in bidegree
 $(p,q)$ with $q \neq 0$ after the standard reindexing, diagonal
 concentration is lost, the square-zero $E_2$-collapse proof breaks,
 and the genus-$0$ counit need not be a quasi-isomorphism. After
 homotopy transfer, the same obstruction appears as the first
 non-vanishing higher multiplication
 $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
 This is distinct from the higher-genus curvature
 $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
 even on the Koszul locus, while the off-diagonal bar class is what
 removes strict genus-$0$ inversion.

\item \emph{How far the quasi-isomorphism extends.}
 Off the locus, the strongest unconditional statement is already
 clause~\textup{(2)} of
 Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
 augmented input with finite-dimensional graded bar pieces, the cone
 of the factorization counit is coacyclic, hence the counit is an
exec
/bin/zsh -lc "sed -n '3150,3210p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{lemma}

\begin{proof}
In the CDG framework (Definition~\ref{def:chiral-CDG-coalgebra}), the genus-$g$
bar complex carries curvature $h = m_0^{(g)}$ satisfying $\dfib^{\,2} = h \ast (-)$.
Explicitly, $m_0^{(g)}$ is the genus-$g$ contribution to the bar curvature,
constructed as a fiber integral:
\[
m_0^{(g)} = \int_{\Sigma_g} \omega_g \in \bar{B}^0_g(\mathcal{A}),
\]
where $\omega_g$ is the volume form of the genus-$g$ propagator
(cf.\ Definition~\ref{def:genus-stratified-bar}).

\emph{Centrality.}
The element $m_0^{(g)}$ lies in the center $Z(\mathcal{A})$ by the
following chain-level argument. For any generator $a \in \mathcal{A}$,
the OPE $m_0^{(g)}{}_{(n)} a$ for $n \geq 0$ vanishes because $m_0^{(g)}$
has conformal weight~$0$ (it is a scalar on each conformal-weight space),
and the Borcherds identity forces the iterated residue
$[\mathrm{Res}_{D_{ij}}, \mathrm{Res}_{D_{kl}}]$ to act trivially on
exec
/bin/zsh -lc "sed -n '3725,3775p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \begin{equation}\label{eq:chiral-homology-tower}
 \bigoplus_{g \geq 0} \hbar^{g}\,
 H^{\mathrm{ch}}_*(\Sigma_g, \cA)
 \;\cong\;
 H^*\bigl(\barB^{\mathrm{tot}}_X(\cA),\, D_{\mathrm{tot}}\bigr),
 \end{equation}
 with the genus filtration corresponding to the $\hbar$-adic
 filtration on the completed bar.
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{Part~(i).}
On a fixed curve $\Sigma_g$, the chiral homology
$H^{\mathrm{ch}}_*(\Sigma_g, \cA)$ is by definition
\cite[3.4.4]{BD04} the derived pushforward of $\cA^{\boxtimes n}$
along the Ran space $\operatorname{Ran}(\Sigma_g)$. The bar
construction computes this pushforward
(Theorem~\ref{thm:geometric-equals-operadic-bar} for genus~$0$;
Theorem~\ref{thm:prism-higher-genus} for the extension to all
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '430,445p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   430	D(C\text{-}\mathrm{comod}^{\mathrm{ch}}).
   431	\]
   432	The coderived category reduces to the ordinary derived category.
   433	This is the regime of Theorem~B (bar-cobar inversion on the Koszul locus).
   434	
   435	\smallskip\noindent
   436	\emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
   437	\textup{(}$h \neq 0$\textup{)}.}
   438	Ordinary bar-complex cohomology collapses on the higher-genus
   439	bar-object surface
   440	\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
   441	but the
   442	coderived--contraderived equivalence
   443	(Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
   444	The Positselski equivalence
   445	$D^{\mathrm{co}}(\barB^{\mathrm{ch}}(\cA)\text{-}\mathrm{comod}) \simeq
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '998,1043p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   998	\index{structural gaps!H1 closed}
   999	Theorem~\ref{thm:off-koszul-ran-inversion} resolves
  1000	structural gap~H1 (Remark~\ref{rem:structural-gaps}):
  1001	the coderived Ran-space formalism is now established.
  1002	Combined with the strict Koszul-locus inversion of
  1003	Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
  1004	proved package on the present surface: ordinary quasi-isomorphism on
  1005	the Koszul lane, coderived equivalence for all complete augmented
  1006	chiral algebras with finite-dimensional bar complex, and no silent
  1007	promotion of the off-Koszul statement back to ordinary cohomology.
  1008	The remaining issue is exactly the collapse input needed for that
  1009	promotion.
  1010	
  1011	The three-step proof (stratum-by-stratum Positselski,
  1012	factorization compatibility, conservative assembly) is the
  1013	factorization incarnation of Positselski's abstract
  1014	programme. The only input beyond the abstract theory is
  1015	the CDG-factorization compatibility
  1016	(\S\ref{subsec:CDG-factorization}), which ensures the
  1017	curved structure and the Ran-space stratification are
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3168,3210p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3168	and the Borcherds identity forces the iterated residue
  3169	$[\mathrm{Res}_{D_{ij}}, \mathrm{Res}_{D_{kl}}]$ to act trivially on
  3170	generators when $D_{ij} \cap D_{kl} = \emptyset$ (factorization axiom),
  3171	while nested collisions contribute only scalar multiples (OPE associativity).
  3172	
  3173	\emph{Cocycle condition.}
  3174	The curved $A_\infty$ relation at $n=0$
  3175	(Definition~\ref{def:curved-ainfty}) gives
  3176	$\mu_1(m_0^{(g)}) = 0$, so $m_0^{(g)}$ is closed. Hence
  3177	$\dfib^{\,2} = m_0^{(g)} \ast (-)$ is the chain-level obstruction to
  3178	lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
  3179	to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
  3180	differential is already square-zero. Otherwise one must pass either to
  3181	the strict flat comparison differential or to the coderived framework;
  3182	ordinary cohomology of the curved fiber complex is not the correct
  3183	invariant.
  3184	\end{proof}
  3185	
  3186	\emph{Step 2: Moduli space interpretation.}
  3187	
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '3720,3760p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3720	\pi: \overline{\mathcal{C}}_{g,n} \to \overline{\mathcal{M}}_{g}
  3721	\end{equation}
  3722	where $\overline{\mathcal{C}}_{g,n}$ is the relative Fulton--MacPherson compactification of $n$ points on the universal curve over~$\overline{\mathcal{M}}_g$. The fiber over $[\Sigma_g] \in \overline{\mathcal{M}}_g$ is $\overline{C}_n(\Sigma_g)$.
  3723	
  3724	\emph{Step 1: Fiberwise differential.} On each fiber $\overline{C}_n(\Sigma_g)$, the differential $d^{(0)}$ is the genus-zero bar differential using residues at collision divisors. By Theorem~\ref{thm:bar-nilpotency-complete}, $(d^{(0)})^2 = 0$.
  3725	
  3726	\emph{Step 2: Base contributions.} The differential $d^{(1)}$ arises from the Gauss--Manin connection on the local system $R^q\pi_*(\mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log})$ over $\overline{\mathcal{M}}_g$. The compatibility $\{d^{(0)}, d^{(1)}\} = 0$ follows from flatness of the Gauss--Manin connection (Stokes' theorem applied fiberwise).
  3727	
  3728	\emph{Step 3: Higher corrections.} Terms $d^{(k)}$ for $k \geq 2$ arise from the Leray filtration: $d^{(k)}$ maps $F^p \to F^{p+k}$ in the filtration by base degree. The relations ensuring $\Dg{g}^{\,2} = 0$ (e.g., $\{d^{(0)}, d^{(2)}\} + (d^{(1)})^2 = 0$) follow from the associativity of the Leray filtration and the exactness of the total complex.
  3729	\end{proof}
  3730	
  3731	\begin{remark}[Leray decomposition and Convention~\ref{conv:higher-genus-differentials}]
  3732	\label{rem:differential-notation}
  3733	\index{bar differential!notation}
  3734	The superscript~$(k)$ in $\Dg{g}=d^{(0)}+d^{(1)}+\cdots$ denotes
  3735	Leray filtration degree, not genus: $d^{(0)}=\dzero$ (fiberwise
  3736	collisions), $d^{(1)}$ (Gauss--Manin), $d^{(k\geq 2)}$ (higher
  3737	corrections). The total $\Dg{g}^{\,2}=0$
  3738	(Theorem~\ref{thm:quantum-diff-squares-zero}), while the fiberwise
  3739	$\dfib$ is curved: $\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$.
codex
**Candidates**
- `chapters/theory/bar_cobar_adjunction_curved.tex:436` & `:438` – the higher-genus subsection still talks about “ordinary bar-complex cohomology” collapsing even though this is the curved regime with $d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_g$ (see Proposition \ref{prop:curved-bar-acyclicity}). That language is a direct curved–vs.–flat red flag: once the fiberwise differential is curved the ordinary cohomology is trivial, so this paragraph needs to explicitly compare to the flat (Koszul) locus or switch to the coderived/curved phrasing it announces a need for.
- `chapters/theory/coderived_models.tex:1004`–`1038` – Remark \ref{rem:H1-closure} and the ensuing spectral-comparison bullet continue to lean on “ordinary quasi-isomorphism on the Koszul lane” and on the PBW page controlling “ordinary cohomology” even off the Koszul locus where $\kappa\ne0$. Since $d^2=\kappa\omega_g$ everywhere outside the flat locus, the text should explicitly state that the collapse hypothesis is about coderived coacyclicity (the remark itself gestures that way) rather than suggesting an ordinary cohomology promotion is automatic.
- `chapters/theory/cobar_construction.tex:3176` – the cocycle-condition discussion stresses that $\dfib^2=m_0^{(g)}\ast(-)=\kappa\omega_g\ast(-)$ and therefore “one must pass either to the strict flat comparison differential or to the coderived framework; ordinary cohomology of the curved fiber complex is not the correct invariant.” That paragraph name‑checks ordinary cohomology despite the curved differential and should be a textured pointer for the survey you’re building: it is exactly where the curved side needs a coderived qualifier instead of treating the spectral data as if it converges to classical cohomology.

**Flat-only safe mention**
- `chapters/theory/higher_genus_foundations.tex:3724` – the Leray spectral‑sequence proof is built from the corrected total differential $\Dg{g}$, which satisfies $\Dg{g}^2=0$, and the subsequent remark names the fiberwise $\dfib^2=\kappa(\cA)\cdot\omega_g$ as the curved piece. Because the spectral sequence only operates after passing to that flat/quantum-corrected differential, this section already keeps the curved/flat dichotomy clean and therefore can be left untouched.
wait(call_HkggvV8vJeV7sNtjFIVXeLpk) 1 agents complete:
  019d8809-e056-7ea0-ba4d-c069ec72c988 completed: "**Candidates**
- `chapters/theory/bar_cobar_adjunction_curved.tex:436` & `:438` – the higher-genus subsection still talk…"
codex
The first pass isolated three actual theory files. I’m reading those local proof blocks now, because the fix has to preserve the intended invariant: ordinary cohomology on the flat comparison side, coderived or curved language on the `d^2=\kappa\omega_g` side.
exec
/bin/zsh -lc "sed -n '400,470p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '980,1055p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3148,3205p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
$\cA$ and~$C$ intertwine $\varepsilon_{U_1 \sqcup U_2}$
with $\varepsilon_{U_1} \otimes \varepsilon_{U_2}$.
Hence $\varepsilon$ is a morphism in the factorization
CDG-comodule category.

\emph{Step~3: Assembly via conservativity.}
The global cone~$K$ restricts to the coacyclic object
$K|_{\operatorname{Ran}_n(X)}$ on each stratum~$n$ by Step~1.
By the conservativity clause of the stratified conservative
restriction theorem
\textup{(}Theorem~\ref{thm:stratified-conservative-restriction}\textup{)},
$K$ is coacyclic in the factorization sense.
Therefore $\varepsilon$ becomes an isomorphism in
$D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})$.
\end{proof}

\begin{remark}[Closure of structural gap~H1]
\label{rem:H1-closure}
\index{structural gaps!H1 closed}
Theorem~\ref{thm:off-koszul-ran-inversion} resolves
 succeeded in 50ms:
\label{rem:derived-coderived-chiral-CDG}
\index{coderived category!derived reduction}
\index{Positselski!derived--coderived reduction}
The chiral bar complex $C = \bar{B}^{\mathrm{ch}}(\cA)$ is a CDG-coalgebra
with curvature $h = m_0^{(g)}$. Three hypotheses govern the relationship
between its coderived and ordinary derived categories:
\begin{enumerate}[label=\textup{(H\arabic*)}]
\item \emph{Conilpotency}: $C$ is conilpotent, i.e., the coaugmentation
 filtration is exhaustive. This holds by
 Theorem~\ref{thm:coalgebra-via-NAP}(4): the conformal weight grading
 on $\bar{B}^{\mathrm{ch}}(\cA)$ provides an exhaustive
 $\mathbb{N}$-filtration with $C = \bigcup_n F^n C$.
\item \emph{Finite-type weight spaces}: each graded piece of $C$ is
 finite-dimensional. This holds because $\cA$ is finitely generated
 with finite-dimensional conformal weight spaces (the positive-energy
 axiom), so $\bar{B}^n(\cA)$ in each weight is a finite-dimensional
 vector space.
\item \emph{Compact generation}: (H1) and (H2) together imply that the
 coderived category $D^{\mathrm{co}}(C\text{-}\mathrm{comod}^{\mathrm{ch}})$
 is compactly generated by finite-dimensional comodules.
 succeeded in 51ms:
with $m_0^{(g)} \in Z(\mathcal{A})$. It vanishes if and only if the
genus-$g$ fiberwise bar differential is square-zero on the nose.
\end{lemma}

\begin{proof}
In the CDG framework (Definition~\ref{def:chiral-CDG-coalgebra}), the genus-$g$
bar complex carries curvature $h = m_0^{(g)}$ satisfying $\dfib^{\,2} = h \ast (-)$.
Explicitly, $m_0^{(g)}$ is the genus-$g$ contribution to the bar curvature,
constructed as a fiber integral:
\[
m_0^{(g)} = \int_{\Sigma_g} \omega_g \in \bar{B}^0_g(\mathcal{A}),
\]
where $\omega_g$ is the volume form of the genus-$g$ propagator
(cf.\ Definition~\ref{def:genus-stratified-bar}).

\emph{Centrality.}
The element $m_0^{(g)}$ lies in the center $Z(\mathcal{A})$ by the
following chain-level argument. For any generator $a \in \mathcal{A}$,
the OPE $m_0^{(g)}{}_{(n)} a$ for $n \geq 0$ vanishes because $m_0^{(g)}$
has conformal weight~$0$ (it is a scalar on each conformal-weight space),
exec
/bin/zsh -lc "rg -n \"ordinary cohomology|cohomology|spectral sequence|d\\"'^2|'"\\\\dfib\\"'^'"\\{?\\\\,?2|\\\\dfib\\"'^2|'"\\\\Dg\\"'^2|'"\\\\mathrm\\{cohomology\\}\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"ordinary cohomology|cohomology|spectral sequence|d\\"'^2|'"\\\\dfib\\"'^'"\\{?\\\\,?2|\\\\dfib\\"'^2|'"\\\\Dg\\"'^2|'"\\\\mathrm\\{cohomology\\}\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:ordinary cohomology|cohomology|spectral sequence|d\^2|\dfib\^\{?\,?2|\dfib\^2|\Dg\^2|\mathrm\{cohomology\})
                                                                                            ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: regex parse error:
    (?:ordinary cohomology|cohomology|spectral sequence|d\^2|\dfib\^\{?\,?2|\dfib\^2|\Dg\^2|\mathrm\{cohomology\})
                                                                                            ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"ordinary cohomology|cohomology|spectral sequence|d\\"'^2|'"\\\\dfib\\"'^'"\\{?\\\\,?2|\\\\dfib\\"'^2|'"\\\\Dg\\"'^2|'"\\\\mathrm\\{cohomology\\}\" chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:ordinary cohomology|cohomology|spectral sequence|d\^2|\dfib\^\{?\,?2|\dfib\^2|\Dg\^2|\mathrm\{cohomology\})
                                                                                            ^^
error: unrecognized escape sequence

thinking
**Improving patterns**

I need to create a better pattern for my task. I'm thinking that a simpler run with fixed strings and maybe using multiple -e options could help streamline things. It seems like there might be a way to simplify the process while still achieving the desired output. I want to ensure that it's efficient and clear, so I'll explore different approaches to find the best solution. It's all about making things work more smoothly!
codex
I’ve confirmed the three live files. I’m doing a tighter local sweep inside each one now so the patch catches every nearby flat/cohomology leak in the same proof lane, not just the first sentence the grep found.
exec
/bin/zsh -lc "rg -n -F -e 'ordinary cohomology' -e 'cohomology' -e 'spectral sequence' -e 'd"'^2'"' -e '\\dfib"'^{'"\\,2}' -e '\\dfib"'^2'"' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F -e 'ordinary cohomology' -e 'cohomology' -e 'spectral sequence' -e 'd"'^2'"' -e '\\dfib"'^{'"\\,2}' -e '\\dfib"'^2'"' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F -e 'ordinary cohomology' -e 'cohomology' -e 'spectral sequence' -e 'd"'^2'"' -e '\\dfib"'^{'"\\,2}' -e '\\dfib"'^2'"' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
18:cohomology, so the counit
181:of $d^2=0$ is the algebraic trace of the
230:\begin{remark}[Curvature, backreaction, and \texorpdfstring{$d^2$}{d\textasciicircum 2}]\label{rem:curvature-backreaction-terminology}
378:$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ where $\mcurv{g} = \kappa(\mathcal{A}) \cdot \lambda_g \neq 0$
438:Ordinary bar-complex cohomology collapses on the higher-genus
548:$d^2=[\mu_0,-]$ is preserved under this dualization because all filtration
743:since $c(k) + c(k') = 2\operatorname{rank}(\mathfrak{sl}_2) + 4h^\vee\dim\mathfrak{sl}_2 = 2 + 24 = 26$ by Theorem~\ref{thm:central-charge-complementarity}(b) (the $\mathcal{W}$-algebra central-charge sum; this is the Virasoro-family formula, not the affine KM formula $c + c' = 2\dim\mathfrak{g}$). Physically, matter--ghost duality pairs a matter system at central charge~$c$ with ghosts at $c_{\mathrm{ghost}} = 26 - c$. In particular, $\mathrm{Vir}_{26}^! \cong \mathrm{Vir}_0$, consistent with bosonic string BRST cohomology at ghost number zero.
1237:\item the completed cohomology is computed by the limit of the
1273:cohomology. The continuity hypothesis ensures that the completed cobar
1292:\item the completed cohomology stabilizes at the finite stage,
1303:Thus eventual stabilization of the finite-stage bar cohomology is a
1339:cohomology tower.
1351:gives the completed cohomology comparison and the completed bar-cobar
1381:cohomology stabilize, and if the cohomology splits as a direct sum of
1394:cohomology groups are canonically isomorphic. Passing to successive
1396:If the cohomology splits by weight, the direct-summand description of
1990:\item for each~$q$, the bar spectral sequence of $\cA_{\le N}/F^{q+1}$
1994:Then the quotient bar cohomology stabilizes for each~$q$, and completed
2003:stabilized $E^\infty$ implies stabilized total cohomology of the quotient
5639:\item \emph{Geometric:}\; $\dfib^{\,2} = \kappa(\mathcal{A})\cdot\omega_g \neq 0$ whenever $\kappa(\mathcal{A}) \neq 0$
 succeeded in 52ms:
8:($d^2 \neq 0$), for which ordinary cohomological derived methods
32:d^2(a) = [h, a], \qquad d(h) = 0.
37:$d^2 = h \ast (-)$ and $h \circ d = 0$.
105:$d^2$ need not vanish on the chain level.
209: $d^2 = m_0 \in Z(M)$ for a central curvature element~$m_0$
210: (cf.\ the fiberwise differential $\dfib$ with $\dfib^{\,2} = \mcurv{g}$,
314:\begin{proposition}[Coderived bar-degree spectral sequence;
317:\index{coderived category!bar-degree spectral sequence|textbf}
380:bar-degree spectral sequence collapses.
486: $h \colon C \to k$ satisfying $d^2 = h \ast (-)$ and
531: $d^2 = \mcurv{g} \ast (-)$ is the curved $A_\infty$ relation
771:bounded-below spectral sequence with acyclic associated graded
781:on each stratum implies the associated graded spectral sequence
1007:promotion of the off-Koszul statement back to ordinary cohomology.
1034: The coderived bar-degree spectral sequence
1038: cohomology or coderived coacyclicity.
 succeeded in 52ms:
763:(Theorem~\ref{thm:arnold-three}). The condition $d^2 = 0$ is equivalent to this cancellation.
788:\emph{Rigorous alternative.} A clean proof avoiding distributional issues entirely is given in Corollary~\ref{cor:cobar-nilpotence-verdier} above, which deduces $d^2 = 0$ from Verdier duality on the Fulton--MacPherson compactification without reference to distributional products.
867:This completes the verification of $d^2 = 0$. All nine cross-terms vanish:
872:$d_{\text{internal}}$ & chain map & $d^2=0$ & commute \\
885:\begin{remark}[Duality with bar \texorpdfstring{$d^2=0$}{d\textasciicircum 2=0} proof]\label{rem:bar-cobar-d2-duality}
886:The structure of this proof \emph{mirrors exactly} the bar $d^2=0$ proof from 
944:$d^2 = 0$ proof.
967:This is the distributional analog of the Arnold relation. \emph{Caveat:} products of delta functions supported on intersecting submanifolds require wavefront set conditions for rigorous definition; the argument here is heuristic. The rigorous proof of $d^2 = 0$ for the cobar complex is provided by Verdier duality (Corollary~\ref{cor:cobar-nilpotence-verdier}).
1054:of products), the cohomology is:
1215:\item \emph{S-matrix elements:} The cohomology $H^*(\Omega^{\text{ch}}(\mathcal{C}))$ 
1238:cohomology $H^*(\Omega^{\text{ch}})$ should therefore be read as algebraic
1483: $\bar{B}^{\mathrm{ch}}(\mathcal{A})$ has cohomology concentrated in a
1496: $\Omega^{\mathrm{ch}}(\mathcal{C})$ has cohomology concentrated in a
1516:of tensor degree $\leq n$. The associated spectral sequence has
1522:Convergence of the spectral sequence is guaranteed by hypothesis~(A2):
1530:finite and the spectral sequence converges on each quotient. Passing
1537:and is a quasi-isomorphism by the spectral sequence argument.
1542:coKoszulity (C1) collapses the spectral sequence to a single column.
1545:is a quasi-isomorphism by the same spectral sequence argument, applied
1698:The Koszul hypothesis forces the bar coalgebra cohomology


thinking
**Evaluating scope for inspection**

I need to think about the scope of my search. I'll consider target terms across all theory chapters, focusing on only three file surfaces. I should inspect passages in the coderived_models theorem regarding the spectral sequence; it might hold proposition text that needs change too. 

Additionally, I'll check lines 1004-1038 that the explorer flagged, along with theorem 314 and lines around 300-390 and 760-785 to confirm there aren't additional true positives. I want to ensure clarity, patching only actual confusion, like the remark at 3188 regarding cohomology with the center.
thinking
**Considering cohomology language**

I should mention that the preceding paragraph states the ordinary cohomology of curved fiber complexes isn't correct. That's important! The user is looking for an explicit flat-side comparison or a coderived qualifier wherever ordinary cohomology applies to curved complexes. I think I should only fix where the ordinary cohomology language is misapplied. The three surfaced lines might be enough for now. I should possibly consult D08 to check for any established phrase changes and search for D08 in the repository.
exec
/bin/zsh -lc 'rg -n "D08|curved-vs-flat|ordinary cohomology of the curved|coderived qualifier|flat-side comparison" -S .' in /Users/raeez/chiral-bar-cobar succeeded in 64ms:
./resume_20260413_163457/S15_appendices_to_body.md:480:flat-side comparison locus together with the coderived treatment of
./rectification_20260412_233715/R03_higher_genus_foundations.md:12:- [FIXED] finding 1 — rewrote `thm:obstruction-quantum` on the strict flat-side complex `(\bar B^{(g)},\Dg{g})`, using hypercohomology of its endomorphism complex and identifying the center on the flat derived side instead of taking ordinary cohomology of the curved `\dfib` object.
./rectification_20260412_233715/R03_higher_genus_foundations.md:77:   (b) Add an explicit flat-side comparison lemma that relates the curved object to a flat resolution, OR
./rectification_20260412_233715/R03_higher_genus_foundations.md:443:/bin/zsh -lc 'rg -n -F "flat-side comparison" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobarexec
./rectification_20260412_233715/R03_higher_genus_foundations.md:451:295:flat-side comparison locus together with the coderived treatment of
./rectification_20260412_233715/R03_higher_genus_foundations.md:560:295:flat-side comparison locus together with the coderived treatment of
./rectification_20260412_233715/R03_higher_genus_foundations.md:632:It seems I'm trying to clarify a theorem that involves the ordinary cohomology of a bar complex sheaf but I'm not sure about the specifics of the differential. I need to decide on the strongest fix—perhaps using a strict differential or a flat-side comparison lemma might help. I wonder if I could strengthen the theorem by changing the bar complex sheaf or by marking the curved fiberwise statement. I'll have to inspect the surrounding context to fully understand its significance.
./rectification_20260412_233715/R03_higher_genus_foundations.md:873:I’ve isolated the first gap: `thm:obstruction-quantum` is using ordinary sheaf cohomology of a bar complex without distinguishing the strict differential from the curved fiberwise one. I’m now checking whether the file already has enough flat-side comparison material to replace that argument by the strict `\Dg{g}` complex rather than downgrading it.
./rectification_20260412_233715/R03_higher_genus_foundations.md:11143:- [FIXED] finding 1 — rewrote `thm:obstruction-quantum` on the strict flat-side complex `(\bar B^{(g)},\Dg{g})`, using hypercohomology of its endomorphism complex and identifying the center on the flat derived side instead of taking ordinary cohomology of the curved `\dfib` object.
./scripts/adversarial_wave2.py:302:    ("D08_curved_vs_flat", "Find EVERY instance of d^2 in the manuscript. For each: is it clear whether d^2=0 (flat/bar) or d^2=kappa*omega_g (curved/fiber)? Any place where ordinary cohomology is applied to a curved complex?"),
./scripts/adversarial_wave2.py:612:    ("L03_thmC_chain", "Trace Theorem C (C0/C1/C2) chain through higher_genus_complementarity.tex + higher_genus_foundations.tex. Map every dependency. Flag curved-vs-flat issues."),
./scripts/fix_campaign_100.py:463:agent("C", "C14_curved_vs_flat_fix", """Fix curved-vs-flat confusion (D08 findings).
./scripts/fix_campaign_100.py:466:explicit flat-side comparison or coderived qualifier. Fix each instance.""", preamble=AUDIT_PREAMBLE)
./scripts/fix_campaign_100.py:519:agent("D", "D08_em_dash_v3", """Same em dash removal for Vol III.""", cwd=VOL3, preamble=AUDIT_PREAMBLE)
./scripts/rectification_campaign.py:171:   (b) Add an explicit flat-side comparison lemma that relates the curved object to a flat resolution, OR
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:497:295:flat-side comparison locus together with the coderived treatment of
./wave2_audit_20260413_001942/F14_hidden_imports_hg_found.md:1424:   295	flat-side comparison locus together with the coderived treatment of
./relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:17:- [HIGH] [chapters/theory/higher_genus_complementarity.tex:986](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:986) — PROBLEM: `lem:fiber-cohomology-center` fixes one curve `\Sigma_g`, computes with the curved differential `d=d_{\mathrm{coll}}+d_{\mathrm{curv}}`, and then upgrades the result to a sheaf over moduli by saying the OPE is local; no family-over-moduli hypothesis is stated, and ordinary cohomology of the curved complex is again used at lines 1052-1097. FIX: Add the missing family hypothesis on `(\mathcal A,\mathcal A^!)` over the universal curve and rewrite the lemma for the strict flat family `R^0\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\mathcal A)`; if only a pointwise statement is available, downgrade the lemma to a fixed-curve result.
./relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:817:The next layer is worse than a missing label: Step I repeatedly takes ordinary cohomology of the curved fiber complex, even though the repo’s own higher-genus convention says that object only lives in the coderived category when `\kappa \neq 0`. I’m reading Steps II and III now to see whether the same derived/coderived slippage and circularity continue there.
./relaunch_20260413_111534/F15_hidden_imports_hg_comp.md:1363:- [HIGH] [chapters/theory/higher_genus_complementarity.tex:986](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:986) — PROBLEM: `lem:fiber-cohomology-center` fixes one curve `\Sigma_g`, computes with the curved differential `d=d_{\mathrm{coll}}+d_{\mathrm{curv}}`, and then upgrades the result to a sheaf over moduli by saying the OPE is local; no family-over-moduli hypothesis is stated, and ordinary cohomology of the curved complex is again used at lines 1052-1097. FIX: Add the missing family hypothesis on `(\mathcal A,\mathcal A^!)` over the universal curve and rewrite the lemma for the strict flat family `R^0\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\mathcal A)`; if only a pointwise statement is available, downgrade the lemma to a fixed-curve result.

thinking
**Inspecting D08 audit file**

I should check the D08 audit file to see if it has a comprehensive list of findings, especially since the user mentioned it. I'll look at wave2_audit within the D08 file to find anything directly related. It’s essential to know if there are more files available beyond the explorer as the D08 audit likely contains numerous findings throughout the repo. I might use rg to search for specific terms within the chapters or theory sections. Let's dive into the relevant parts!
exec
/bin/zsh -lc 'rg -n "chapters/theory/.*(bar_cobar_adjunction_curved|coderived_models|cobar_construction|higher_genus_foundations|higher_genus_complementarity)|ordinary cohomology|spectral sequence|coderived" wave2_audit_20260413_001942/D08_curved_vs_flat.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
9:- [CRITICAL] [chiral-bar-cobar/chapters/theory/cobar_construction.tex:3111](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3111) and [3395](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3395) — PROBLEM: `\dfib^{\,2}` is turned into an ordinary cohomology class of a curved complex, then rewritten as `[ \mu_0,-]`. FIX: replace the lemma/corollary by the chain-level statement `\dfib^{\,2}=\kappa(\cA)\cdot\omega_g\cdot\id` (or the appropriate central endomorphism); if a class is needed, take it only after passing to the flat total differential `D_g` or to coderived data, not as `H^2(\barB_g(\cA),Z(\cA))`.
10:- [CRITICAL] [chiral-bar-cobar/chapters/connections/concordance.tex:10268](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:10268) — PROBLEM: line 10273 asks for ordinary cohomology concentration on a curved bar complex. FIX: replace “the curved bar complex `\barBch(L_k)` has cohomology concentrated in bar degree 1 despite the curvature” by “the critical/flat specialization has bar cohomology concentrated in bar degree 1; off the flat locus the correct target is coderived or Maurer–Cartan data, not ordinary cohomology.”
13:- [HIGH] [chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5958](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:5958) — PROBLEM: the Virasoro complementarity proposition is phrased as `d_{\barB}^2=\kappa(\mathrm{Vir}_c)\cdot\omega_g`. FIX: replace that identity and the proof line 5983 by `\dfib^{\,2}=\kappa(\mathrm{Vir}_c)\cdot\omega_g`, keeping `d_{\barB}^2=0`.
80:Find EVERY instance of d^2 in the manuscript. For each: is it clear whether d^2=0 (flat/bar) or d^2=kappa*omega_g (curved/fiber)? Any place where ordinary cohomology is applied to a curved complex?
90:Auditing the `d^2` surface across all three volumes now. I’m loading the audit workflow, then I’ll enumerate every `d^2` occurrence in the chapter trees, read each in context, classify whether it is flat or curved, and check for any illegitimate ordinary cohomology on curved complexes.
285:  17 /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex
290:  13 /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
298:  10 /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex
306:/bin/zsh -lc "rg -n --pcre2 'd\\"'^2'"\\s*=\\s*\\[|d\\"'^2'"\\s*=\\s*\\\\kappa|d\\"'^2'"\\s*\\\\neq\\s*0|d\\"'^2'"\\s*\\sim|cohomolog|chain complex|honest chain complex|ordinary cohomology|no cohomology' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
350:I’ve isolated the first genuinely dangerous cluster: places that assign curvature directly to the bar differential or write `d^2 = [m_0,-]` on a bar complex. Those are constitution-level object-conflations, so I’m reading them in context first and then checking whether the same mistake is paired with ordinary cohomology language downstream.
354:/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '536,548p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
414:/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex | sed -n '28,45p;194,208p;438,448p'" in /Users/raeez/chiral-bar-cobarexec
594:The main error pattern is confirmed, not hypothetical: several files explicitly say “the bar differential/bar complex satisfies `d^2 = [m_0,-]`” or “curved bar `d^2 = \kappa\omega_g`.” I’m now checking whether those same sections then speak about honest complexes, ordinary derived categories, or ordinary cohomology, because that turns an object-conflation into a downstream mathematical misuse.
613:   882	substitute is the coderived category (Definition~\ref{def:chiral-coderived}).
670:  1604	\begin{remark}[Curvature forces coderived passage]%
671:  1605	\label{rem:curvature-coderived-analytic}%
672:  1606	\index{coderived category!analytic motivation}%
674:  1608	$\mcurv{g} \neq 0$, then ordinary cohomology fails because the
677:  1611	receptacle is the coderived/contraderived analytic category
678:  1612	(\S\ref{subsec:coderived-ran}), not an ordinary derived category.


thinking
**Searching for patterns**

I see that the explorer has covered some patterns, but the D08 file offers more targeted findings. To ensure I’m being exhaustive, I should look for curved patterns specifically in the chapters or theory. It might be best to use the D08 file instead of relying solely on code search. I'll run targeted searches using relevant terms and make sure I gather comprehensive data since the explorers only mapped a few candidate files.
thinking
**Searching theory files**

I’ll focus on targeted regex searches with patterns like "ordinary cohomology," especially around terms like "curved," "coderived," "dfib^{\,2}," and "spectral sequence." I think I’ll use the command to search within chapters and theory files. It seems safe and won’t violate explorer guidelines, which is good since I want to provide comprehensive results for the user. Let’s get started by searching for "ordinary cohomology" in those theory chapters!
codex
I found an older D08 audit artifact in the repo. I’m using it as a cross-check against the live tree now, because it points to at least one additional theory-chapter cluster beyond the first three files and I need the current state, not the archived findings.
exec
/bin/zsh -lc "rg -n -F 'ordinary cohomology' chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\dfib"'^{'"\\,2}' chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'spectral sequence' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1678: bar-degree spectral sequence degenerates to ordinary cohomology on
chapters/theory/bar_cobar_adjunction_inversion.tex:1983: is still detected by ordinary cohomology.
chapters/theory/bar_cobar_adjunction_inversion.tex:1987: coderived bar-degree filtration degenerates to ordinary cohomology.
chapters/theory/coderived_models.tex:1007:promotion of the off-Koszul statement back to ordinary cohomology.
chapters/theory/cobar_construction.tex:3182:ordinary cohomology of the curved fiber complex is not the correct
chapters/theory/chiral_hochschild_koszul.tex:3747:$\Dg{g}\big|_{[\Sigma_g]}$ computes the same ordinary cohomology as
chapters/theory/chiral_hochschild_koszul.tex:3750:coderived side rather than in ordinary cohomology.
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:397: \arrow[r, phantom, "\scriptstyle \dfib^{\,2} = \kappa(\cA) \cdot \omega_g"]
chapters/theory/higher_genus_modular_koszul.tex:402: \arrow[r, phantom, "\scriptstyle \dfib^{\,2} = \kappa(\cA^!) \cdot \omega_g"]
chapters/theory/higher_genus_modular_koszul.tex:565:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
chapters/theory/higher_genus_modular_koszul.tex:2567: $\dfib^{\,2} = \kappa(\cA)\,\omega_g$ forces
chapters/theory/higher_genus_modular_koszul.tex:2622: fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
chapters/theory/higher_genus_modular_koszul.tex:2754: $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g\cdot\operatorname{id}$ and the
chapters/theory/higher_genus_modular_koszul.tex:10013:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \mathrm{id}$
chapters/theory/higher_genus_modular_koszul.tex:12100:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \neq 0$, the flat
chapters/theory/higher_genus_modular_koszul.tex:22200:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$.
chapters/theory/higher_genus_modular_koszul.tex:31770:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, where
chapters/theory/higher_genus_modular_koszul.tex:31849:\dfib^{\,2}
chapters/theory/bar_construction.tex:385:$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, and the curvature
chapters/theory/bar_construction.tex:1740:oriented at each genus. It is the determinant line of $T_{C_{p+1}(\Sigma_g)}$ with genus-dependent corrections, ensuring consistent signs across all face maps. At genus~$0$, this guarantees $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}); at genus~$g \geq 1$, the fiberwise differential satisfies $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ and the total corrected differential $\Dg{g}^2 = 0$ is established in Chapter~\ref{chap:higher-genus}.
chapters/theory/fourier_seed.tex:416:$\dfib^{\,2} \neq 0$: the Arnold
chapters/theory/fourier_seed.tex:419:\dfib^{\,2}(\xi^{(1)}_{123}) = k \cdot \omega_1.
chapters/theory/fourier_seed.tex:443:&= \dfib^{\,2}
chapters/theory/higher_genus_foundations.tex:11:$\overline{C}_n(X)$, its nilpotency $\dfib^{\,2} = 0$ uses
chapters/theory/higher_genus_foundations.tex:23:The genus-$0$ proof of $\dfib^{\,2} = 0$ is combinatorial:
chapters/theory/higher_genus_foundations.tex:36:identity $\dfib^{\,2} = 0$ fails by a measurable amount.
chapters/theory/higher_genus_foundations.tex:98:$\dfib^{\,2}|_{g=1} = \kappa(\cA)\cdot\omega_1$ arises from
 succeeded in 52ms:
Total output lines: 491

chapters/theory/higher_genus_modular_koszul.tex:617:At each genus $g \geq 1$, the PBW spectral sequence of
chapters/theory/higher_genus_modular_koszul.tex:776:\index{PBW spectral sequence!higher genus concentration}
chapters/theory/higher_genus_modular_koszul.tex:787:Then for every genus~$g \geq 1$, the PBW spectral sequence for the
chapters/theory/higher_genus_modular_koszul.tex:918:\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
chapters/theory/higher_genus_modular_koszul.tex:977:\index{PBW spectral sequence!mixed map factorization|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1025:\index{PBW spectral sequence!genus-1 degeneration|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1031:$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
chapters/theory/higher_genus_modular_koszul.tex:1221:spectral sequence converges in each bidegree, and
chapters/theory/higher_genus_modular_koszul.tex:1368:\index{PBW spectral sequence!all-genera degeneration|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1380:generic level $k \notin \Sigma(\fg)$, the PBW spectral sequence
chapters/theory/higher_genus_modular_koszul.tex:1552:killed at finite page of the PBW spectral sequence,
chapters/theory/higher_genus_modular_koszul.tex:1628:\index{PBW spectral sequence!all-genera degeneration for Virasoro|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1638:spectral sequence for the genus-$g$ bar complex
chapters/theory/higher_genus_modular_koszul.tex:1840:\index{PBW spectral sequence!unique-weight-2 criterion|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1841:\index{PBW spectral sequence!universal semisimple enrichment-killing|textbf}
chapters/theory/higher_genus_modular_koszul.tex:1859:spectral sequence satisfies
chapters/theory/higher_genus_modular_koszul.tex:1908:spectral sequence different from the one where the
chapters/theory/higher_genus_modular_koszul.tex:2002:\index{PBW spectral sequence!hook-type W-algebras|textbf}

thinking
**Inspecting search results**

I need to focus on specific issues in the search results, particularly regarding the terms bar_cobar_adjunction_inversion and chiral_hochschild_koszul, which might already be clarified. The user asked me to look for 'd^2', 'spectral sequence', and 'cohomology' in Vol I theory chapters. I'm considering unresolved matters in those lines. I’ll check around lines 1660-1690 and others, and read the contexts in the files related to "ordinary cohomology" to classify them.
exec
/bin/zsh -lc "sed -n '1648,1695p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3735,3760p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1968,1995p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\item \emph{Coderived off-Koszul lane.}
 For arbitrary complete augmented $\mathcal{A}$ with
 finite-dimensional graded bar pieces, the factorization counit
 \[
 \psi_X \colon \Omega_X \barB_X(\mathcal{A}) \longrightarrow \mathcal{A}
 \]
 is a coacyclic-equivalence: its cone
 \[
 K_\psi :=
 \operatorname{cone}\!\bigl(\Omega_X \barB_X(\mathcal{A}) \to \mathcal{A}\bigr)
 \]
 is coacyclic. Equivalently, $\psi_X$ is an isomorphism in
 $D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$, without any
 Koszulness hypothesis.

\item \emph{Coderived bar-degree filtration.}
 On the curved cone $K_\psi$, the bar-degree filtration yields the
 coderived spectral sequence of
 Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
 succeeded in 52ms:
 $m_r$ on $\cA^i = H^*(\barB_X(\cA))$ with $r \geq 3$.
 This is distinct from the higher-genus curvature
 $m_0^{(g)} = \kappa(\cA)\omega_g$: curvature forces coderived methods
 even on the Koszul locus, while the off-diagonal bar class is what
 removes strict genus-$0$ inversion.

\item \emph{How far the quasi-isomorphism extends.}
 Off the locus, the strongest unconditional statement is already
 clause~\textup{(2)} of
 Theorem~\ref{thm:bar-cobar-inversion-qi}: for every complete
 augmented input with finite-dimensional graded bar pieces, the cone
 of the factorization counit is coacyclic, hence the counit is an
 isomorphism in the coderived category. The natural enlargement of
 $\operatorname{Kosz}(X)$ is therefore a \emph{conjectural derived
 Koszul locus}: the full derived substack on which this coacyclic cone
 is still detected by ordinary cohomology.
 Conjecture~\ref{conj:koszul-wall-associated-variety} formulates that
 derived wall. The proved promotion surface is narrower: clause~\textup{(4)}
 upgrades the coderived equivalence only on collapse loci where the
 coderived bar-degree filtration degenerates to ordinary cohomology.
 succeeded in 52ms:

\begin{proof}
\emph{Part~(i).}
On a fixed curve $\Sigma_g$, the chiral homology
$H^{\mathrm{ch}}_*(\Sigma_g, \cA)$ is by definition
\cite[3.4.4]{BD04} the derived pushforward of $\cA^{\boxtimes n}$
along the Ran space $\operatorname{Ran}(\Sigma_g)$. The bar
construction computes this pushforward
(Theorem~\ref{thm:geometric-equals-operadic-bar} for genus~$0$;
Theorem~\ref{thm:prism-higher-genus} for the extension to all
genera via the Feynman transform): the bar complex on
$\overline{C}_n(\Sigma_g)$ with the flat comparison differential
$\Dg{g}\big|_{[\Sigma_g]}$ computes the same ordinary cohomology as
the Ran-space pushforward. If $\kappa(\cA) \neq 0$, the raw fiberwise
operator $\dfib^{(\Sigma_g)}$ is curved and therefore belongs on the
coderived side rather than in ordinary cohomology.

\emph{Part~(ii).}
The assignment $[\Sigma_g] \mapsto
H^{\mathrm{ch}}_*(\Sigma_g, \cA)$ varies in a local system because
exec
/bin/zsh -lc "rg -n -F 'cohomology' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'spectral sequence' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'coderived' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
66: curve~$X$ and every genus $g \geq 0$, the cohomology of the ambient
102:flat fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
121:(finite-dimensional bar cohomology at each weight). In particular, hypothesis~(P2) (nondegeneracy) implies
248:\item On cohomology:
317:\item \emph{Finite-dimensional flat fiber cohomology.}
340:cohomology of $\operatorname{gr}_F$ is concentrated in total
354:cohomology concentrated in degree~$0$ for every~$\Sigma$.
362:cohomology sheaves
365:degree-$0$ cohomology sheaf has
367:cohomology and base change theorem
370:complex (bounded, with coherent cohomology sheaves) on
427:form, and its ordinary-cohomology manifestation holds on the flat
440:cohomology is not the invariant when $\kappa(\cA)\neq 0$.
461:$\operatorname{gr}_F \cA$, which has cohomology concentrated
477:for $q \neq 0$: the strict flat fiber complex has cohomology
486:Apply cohomology and base change to the family
643:Taking cohomology gives the S-level decomposition
701:$\mathbf{Q}_g(\cA)$ and $\mathbf{Q}_g(\cA^!)$, whose cohomology gives
723:& Construct spectral sequence relating bar complex to moduli space cohomology\\
725:& Compute $E_2$ page in terms of fiber cohomology\\
 succeeded in 52ms:
346:The bar-degree filtration spectral sequence
351:or out of the zero row), and the spectral sequence collapses at
464:The bar-degree filtration spectral sequence
617:filtration spectral sequence (standard), Poincar\'e--Verdier
723:& Construct spectral sequence relating bar complex to moduli space cohomology\\
730:& Show duality interchanges $\mathcal{A}$ and $\mathcal{A}^!$ spectral sequences\\
744:\item Leray spectral sequence for fibration $\overline{C}_n(X) \times \overline{
757:\subsection{Step I: spectral sequence construction}
816:\emph{Step 2: Associated spectral sequence.}
823:induces a spectral sequence:
851:For each genus~$g$, the Leray spectral sequence for the fibration
857:then assembles these into the stated spectral sequence
860:The Leray spectral sequence is applied to the fibration:
908:\begin{lemma}[Convergence of the quantum spectral sequence;
911:\index{spectral sequence!convergence}
912:The spectral sequence of
956:\emph{Convergence.} By (1)--(3), the spectral sequence
966:suffices: the genus spectral sequence stabilizes
972:\begin{lemma}[Quantum corrections as spectral sequence limit; \ClaimStatusProvedHere]
983:By definition of spectral sequences, $E_\infty$ is the associated graded of the 
 succeeded in 52ms:
46: \textup{(}unconditional in coderived form on the Koszul locus\textup{)}.}\;
49: $(\barB^{(g)}(\cA),\dfib)$ determines a well-defined coderived
107:coderived form on the Koszul locus, and its ordinary-derived
399: coderived object. Proposition~\textup{\ref{prop:gauss-manin-uncurving-chain}}
426:In particular, $\mathrm{C}_0$ holds unconditionally in coderived
837:The curved fiber operator~$\dfib$ remains only as a coderived
886:coderived side.
1014:fiber model one retains the corresponding coderived class whenever
1058:$\dfib$ is retained only in coderived form; if $\kappa(\mathcal{A})=0$,
2911:$\kappa(\mathcal{A})$ and is interpreted coderivedly before passing to
3615: coderived
4417:\begin{remark}[Off-locus coderived continuation kept separate]
4427:coderived category
4429:left to the separate coderived-model formalism
4430:\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
4433:Proposition~\ref{prop:coderived-adequacy}(a) remains.
4528:The replacement is the coderived factorization co-contra comparison on
4676:(iii)~the coderived category
exec
/bin/zsh -lc "sed -n '3390,3460p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{proof}

\emph{Step 6: Conclusion}

Combining Lemmas \ref{lem:obstruction-class}, \ref{lem:period-integral}, 
\ref{lem:deformation-space}, \ref{lem:obs-def-pairing}, and \ref{lem:center-cohomology}, 
we conclude:
\[Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!) \simeq H^*(\mathcal{M}_g, Z(\mathcal{A}))\]
as claimed.

\end{proof}

\begin{remark}[Explicit formulas for low genus]\label{rem:explicit-low-genus-curved}

\emph{Genus 0.} $\mathcal{M}_0 = \text{pt}$, so $H^*(\mathcal{M}_0, Z(\mathcal{A})) 
= Z(\mathcal{A})$. There are no quantum corrections.

\emph{Genus 1.} The moduli space $\mathcal{M}_1$ has $H^1(\mathcal{M}_1, \mathbb{Q}) = 0$ (as for all $\mathcal{M}_g$), but $\dim \mathcal{M}_1 = 1$. Quantum corrections enter through the \emph{partition function}, which depends on the modulus $\tau \in \mathfrak{h}/\mathrm{SL}_2(\mathbb{Z})$:
\[Q_1(\mathcal{H}_k) = \mathbb{C} \cdot k\]
where $k$ is the level of the Heisenberg algebra. Here $Q_1$ is computed from the center $Z(\mathcal{A})$ evaluated over $\mathcal{M}_1$, not from $H^1$.
exec
/bin/zsh -lc "rg -n --pcre2 'curved.{0,80}cohomology|cohomology.{0,80}curved|ordinary.{0,80}curved|curved.{0,80}spectral sequence|spectral sequence.{0,80}curved' chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 'd\\"'^2[''^'"\\n]{0,120}cohomology|cohomology["'^'"\\n]{0,120}d\\"'^2|'"\\\\dfib\\"'^'"\\{\\\\,2\\}["'^'"\\n]{0,120}cohomology|cohomology["'^'"\\n]{0,120}\\\\dfib\\"'^'"\\{\\\\,2\\}' chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 'ordinary cohomology|coderived side rather than in ordinary cohomology|flat comparison differential|flat representative|flat fiber cohomology' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/derived_langlands.tex:48:obstructs the formation of cohomology: the bar complex is a curved
chapters/theory/derived_langlands.tex:66:2) = 0$: uncurved bar complex, honest cohomology. The classical
chapters/theory/nilpotent_completion.tex:898:bar cohomology of the ``decurved'' Virasoro algebra (the
chapters/theory/chiral_koszul_pairs.tex:6342:spectral sequence degenerates at~$E_2$. A \emph{completed curved}
chapters/theory/chiral_koszul_pairs.tex:6370:One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
chapters/theory/cobar_construction.tex:3182:ordinary cohomology of the curved fiber complex is not the correct
 succeeded in 51ms:
chapters/theory/derived_langlands.tex:32:$d^2 \neq 0$, no cohomology, no geometry. At the critical level
 succeeded in 51ms:
chapters/theory/coderived_models.tex:1007:promotion of the off-Koszul statement back to ordinary cohomology.
chapters/theory/bar_cobar_adjunction_inversion.tex:1678: bar-degree spectral sequence degenerates to ordinary cohomology on
chapters/theory/bar_cobar_adjunction_inversion.tex:1983: is still detected by ordinary cohomology.
chapters/theory/bar_cobar_adjunction_inversion.tex:1987: coderived bar-degree filtration degenerates to ordinary cohomology.
chapters/theory/higher_genus_foundations.tex:456:curved object with this strict flat representative:
chapters/theory/cobar_construction.tex:3181:the strict flat comparison differential or to the coderived framework;
chapters/theory/cobar_construction.tex:3182:ordinary cohomology of the curved fiber complex is not the correct
chapters/theory/higher_genus_complementarity.tex:102:flat fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
chapters/theory/higher_genus_complementarity.tex:317:\item \emph{Finite-dimensional flat fiber cohomology.}
chapters/theory/higher_genus_complementarity.tex:445:calculation must be performed on the flat representative.
chapters/theory/higher_genus_complementarity.tex:447:\emph{Step~2: Filter the strict flat representative.}
chapters/theory/higher_genus_complementarity.tex:839:cohomology is taken after passage to the flat representative.
chapters/theory/higher_genus_complementarity.tex:1032:the flat fiber cohomology sheaf over the smooth
chapters/theory/higher_genus_complementarity.tex:1047:$\Dg{g}$ squares to zero, the higher flat fiber cohomology vanishes,
chapters/theory/higher_genus_complementarity.tex:1974:derived global sections to the perfect flat representative yields the
chapters/theory/chiral_hochschild_koszul.tex:3689: square-zero flat comparison differential at
chapters/theory/chiral_hochschild_koszul.tex:3746:$\overline{C}_n(\Sigma_g)$ with the flat comparison differential
chapters/theory/chiral_hochschild_koszul.tex:3747:$\Dg{g}\big|_{[\Sigma_g]}$ computes the same ordinary cohomology as
chapters/theory/chiral_hochschild_koszul.tex:3750:coderived side rather than in ordinary cohomology.

thinking
**Clarifying model distinctions**

I think I need to make the summary clearer about the differences between the flat associated graded and corrected holomorphic models, which are square-zero and compute ordinary cohomology. The curved geometric model, on the other hand, computes cohomology only in coderived terms. The summary already addresses this, but I may need to adjust the wording to emphasize these distinctions better. Let’s consider how to make that line more explicit.
exec
/bin/zsh -lc "sed -n '350,395p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
respect to the conformal-weight filtration to make sense of it.

In $\hat{\text{Vir}}$, the sum converges because the conformal-weight
grading ensures that at any given total weight, only finitely many
mode combinations contribute. Formally, the state space of
$\mathrm{Vir}_c$ is graded by conformal weight with finite-dimensional
weight spaces, so the completed bar differential is a well-defined
continuous map in the inverse-limit topology.
\end{proof}

\begin{remark}[Scope of the proof]\label{rem:completion-necessity-scope}
The Virasoro example above establishes necessity for condition~(1).
Condition~(2) is demonstrated by the $\beta\gamma$-system, whose bar complex is not conilpotent due to the infinite-rank coproduct on the symmetric coalgebra (see~\S\ref{subsec:betagamma-all-genera} in Chapter~\ref{ch:genus-expansions}).
Condition~(3) is illustrated by affine $\widehat{\mathfrak{sl}}_2$ at non-integral level, where the Serre-type relations involve infinitely many generators (see~\S\ref{sec:three-theorems-sl2} in Chapter~\ref{ch:genus-expansions}).
\end{remark}

\begin{proposition}[Acyclicity of curved bar complexes; \ClaimStatusProvedHere]
\label{prop:curved-bar-acyclicity}
\index{acyclicity!curved bar complex}
\index{Positselski!acyclicity}

thinking
**Clarifying cohomology concepts**

I'm exploring a proposition that suggests an underlying cochain complex where d_total may align with Dg. It sounds like there’s a connection since the curved bar complex has an acyclic underlying cochain complex with H^*(..., d_total)=0. If Dg^2=0, then the ordinary cohomology of the total corrected differential is also 0. I think it’s essential to distinguish between the ordinary bar-complex and total corrected differential while avoiding confusion between terms. Let's keep investigating!
exec
/bin/zsh -lc "sed -n '395,430p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
which is why Theorem~\ref{thm:positselski-chiral} requires the
coderived/contraderived setting.
\end{remark}

\begin{remark}[Derived--coderived reduction for chiral CDG-coalgebras]
\label{rem:derived-coderived-chiral-CDG}
\index{coderived category!derived reduction}
\index{Positselski!derived--coderived reduction}
The chiral bar complex $C = \bar{B}^{\mathrm{ch}}(\cA)$ is a CDG-coalgebra
with curvature $h = m_0^{(g)}$. Three hypotheses govern the relationship
between its coderived and ordinary derived categories:
\begin{enumerate}[label=\textup{(H\arabic*)}]
\item \emph{Conilpotency}: $C$ is conilpotent, i.e., the coaugmentation
 filtration is exhaustive. This holds by
 Theorem~\ref{thm:coalgebra-via-NAP}(4): the conformal weight grading
 on $\bar{B}^{\mathrm{ch}}(\cA)$ provides an exhaustive
 $\mathbb{N}$-filtration with $C = \bigcup_n F^n C$.
\item \emph{Finite-type weight spaces}: each graded piece of $C$ is
 finite-dimensional. This holds because $\cA$ is finitely generated
 with finite-dimensional conformal weight spaces (the positive-energy

thinking
**Searching cohomology mentions**

If a file has already been corrected, I might not need to revisit it. However, there could be nearby sentences referring to ordinary cohomology that I should check. I think I’ll search for mentions around lines 3100 to 3450, especially the corollary about cohomological shadow. It might also be worth looking for an earlier lemma discussing "center as obstruction-deformation space" that uses the cohomology of curved objects. Reading around line 3330 seems like a good approach.
exec
/bin/zsh -lc "sed -n '3328,3365p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
each eigenspace (since $\sigma(\beta) = \pm\beta$ and the
antisymmetry $\langle \alpha, \sigma\beta \rangle
= -\langle \sigma\alpha, \beta \rangle$ forces vanishing on
equal eigenvalues).

\emph{Step~3: Non-degeneracy.}
On the cross-terms $Q_g(\mathcal{A}) \otimes Q_g(\mathcal{A}^!)$,
the pairing reduces to Serre duality on $\overline{\mathcal{M}}_g$
with coefficients in $\mathcal{Z}(\mathcal{A})$. Serre duality is
non-degenerate on the compact orbifold $\overline{\mathcal{M}}_g$,
so the pairing is perfect.
\end{proof}

\emph{Step 5: Center Cohomology}

\begin{lemma}[Center as obstruction-deformation space; \ClaimStatusProvedHere]\label{lem:center-cohomology}
The direct sum $Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)$ naturally identifies with:
\[H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathcal{A}))\]
\end{lemma}

exec
/bin/zsh -lc "sed -n '3365,3408p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
comparison class lies in the $\sigma$-invariant part of
$H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathcal{A}))$, because
$\sigma(m_0^{(g)}) = m_0^{(g)}$ (the curvature is Verdier-self-dual:
it is constructed from the volume form $\omega_g$, which is a canonical
section of $K_{\Sigma_g}$, and Verdier duality acts as the identity on
canonical sections). The full $+1$-eigenspace is generated by such
obstruction classes as $g$ varies, giving
$Q_g(\mathcal{A}) = \ker(\sigma^* - \mathrm{id})$.

\emph{The $-1$-eigenspace is $Q_g(\mathcal{A}^!)$.}
By Lemma~\ref{lem:deformation-space},
$\mathrm{Def}_g(\mathcal{A}^!)$ embeds in
$H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\mathcal{A}))$.
Since Koszul duality negates the Verdier involution
($\sigma_{\mathcal{A}^!} = -\sigma_{\mathcal{A}}$
on centers, by Theorem~\ref{thm:verdier-bar-cobar}),
deformation classes lie in the $-1$-eigenspace:
\[
Q_g(\mathcal{A}^!) = \ker(\sigma^* + \mathrm{id}).
\]




thinking
**Analyzing mathematical terminology**

I'm reviewing search results that mention "bar-degree spectral sequence degenerating to ordinary cohomology on the relevant off-Koszul locus." It seems to indicate a certain safety since it involves a collapse locus. There's also a derived substack where a coacyclic cone is detected by ordinary cohomology. I’m considering if the mention of flat-side could be important, especially concerning the curved complex. However, I need to verify if the theorem is explicit enough based on the context search.
thinking
**Reviewing mathematical statements**

The statement mentions that if kappa=0 or the coderived bar-degree spectral sequence degenerates to ordinary cohomology on the relevant off-Koszul locus, then the coderived equivalence becomes a chain-level quasi-isomorphism. It notes that outside those specific collapse loci, the theorem doesn't assert ordinary quasi-isomorphism, which feels explicit enough. There's a similar observation about a derived substack where the coacyclic cone is detected by ordinary cohomology, only upgrading on collapse loci. Looks good, so no edits needed!
thinking
**Exploring cohomology details**

I'm considering making the flat side of a discussion more explicit, particularly about the ambiguous flat side in curved complex contexts. The user's request to search for cohomology and the d^2 aspect brought to light line 3181/3182, which deals with ordinary cohomology. While the current line isn’t wrong, I can enhance clarity by adding comparisons. I’m also pondering if there are relevant points in bar_cobar_adjunction_inversion or derived_langlands that could be considered, but I think no edits are necessary for now.
thinking
**Reviewing cohomology details**

I need to inspect higher_genus_foundations and ensure the current complementarity is safe without needing edits. I should also check lines in bar_cobar_adjunction_inversion related to "ordinary cohomology" to confirm they’re already explicit enough. It might be good to run a targeted search across theory chapters to identify safe occurrences and content, which seems manageable. Before editing, I’ll provide a brief verification note that summarizes key details and includes the scope and comparisons. This update should help clarify everything before applying patches.
codex
I’ve narrowed the live write surface to three theory files. The common fix is the same in each case: ordinary cohomology is allowed only after naming the square-zero flat comparison differential, while the raw `\dfib^{\,2}=\kappa(\cA)\omega_g` side stays coderived.

```text
scope: bar_cobar_adjunction_curved.tex; coderived_models.tex; cobar_construction.tex
curved side: (\barB^{(g)}(\cA), \dfib), with \dfib^{\,2} = \kappa(\cA)\omega_g
flat side: square-zero total/flat comparison differential (d_total or \Dg{g})
ordinary cohomology used only on flat side after patch? Y
coderived qualifier retained for curved side after patch? Y
verdict: ACCEPT
```
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
@@ -3180,5 +3180,6 @@
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
@@ -3431,3 +3432,4 @@
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
M /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex
@@ -1004,7 +1004,7 @@
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
@@ -1036,4 +1036,6 @@
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -437,6 +437,8 @@
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
apply_patch(auto_approved=true) exited 0 in 36ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}

codex
The edits are in. I’m re-grepping the theory tree now to make sure the remaining `ordinary cohomology` hits are all explicitly tied to a square-zero flat lane or otherwise fenced on the coderived side, and I’m checking the exact diff for the three touched files.
exec
/bin/zsh -lc "rg -n -F 'ordinary cohomology' chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/coderived_models.tex chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --pcre2 'curved.{0,80}cohomology|cohomology.{0,80}curved|ordinary.{0,80}curved|curved.{0,80}spectral sequence|spectral sequence.{0,80}curved' chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1678: bar-degree spectral sequence degenerates to ordinary cohomology on
chapters/theory/bar_cobar_adjunction_inversion.tex:1983: is still detected by ordinary cohomology.
chapters/theory/bar_cobar_adjunction_inversion.tex:1987: coderived bar-degree filtration degenerates to ordinary cohomology.
chapters/theory/bar_cobar_adjunction_curved.tex:439:$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
chapters/theory/cobar_construction.tex:3183:framework; ordinary cohomology of the curved fiber complex
chapters/theory/chiral_hochschild_koszul.tex:3747:$\Dg{g}\big|_{[\Sigma_g]}$ computes the same ordinary cohomology as
chapters/theory/chiral_hochschild_koszul.tex:3750:coderived side rather than in ordinary cohomology.
chapters/theory/coderived_models.tex:1038: ordinary cohomology, while off the Koszul locus it controls
 succeeded in 51ms:
chapters/theory/derived_langlands.tex:48:obstructs the formation of cohomology: the bar complex is a curved
chapters/theory/derived_langlands.tex:66:2) = 0$: uncurved bar complex, honest cohomology. The classical
chapters/theory/nilpotent_completion.tex:898:bar cohomology of the ``decurved'' Virasoro algebra (the
chapters/theory/cobar_construction.tex:3183:framework; ordinary cohomology of the curved fiber complex
chapters/theory/chiral_koszul_pairs.tex:6342:spectral sequence degenerates at~$E_2$. A \emph{completed curved}
chapters/theory/chiral_koszul_pairs.tex:6370:One needs the PBW spectral sequence approach (Theorem~\ref{thm:pbw-koszulness-criterion}), or equivalently, curved Koszul duality (Positselski) with nilpotent completion and a filtered/completed category.
 succeeded in 51ms:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 32b8005..7ad5428 100644
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -143,12 +143,16 @@ three layers of structure:
  $\Factord(\cA)$. The $R$-matrix provides the braiding.
  After coinvariants, only the symmetric monoidal shadow survives.
 \item \emph{The Swiss-cheese directionality.} The
- $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$~operad decomposes as
- $\Eone \times \Einf$ on $\R \times \C$: the bar differential is
- the closed/$\Einf$ colour on holomorphic configurations, and the
- deconcatenation coproduct is the open/$\Eone$ colour on the
- topological interval. The symmetric bar retains only the closed
- colour; the ordered bar retains both.
+ $\mathrm{SC}^{\mathrm{ch},\mathrm{top}}$~picture couples
+ holomorphic collision data on~$\FM_k(\C)$ with topological
+ interval splitting on~$\Conf_k(\R)$. On the ordered bar these
+ appear as the bar differential and the deconcatenation
+ coproduct, but they do \emph{not} make
+ $\barB^{\mathrm{ord}}(\cA)$ itself an
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}



thinking
**Addressing git diff issues**

I'm noticing that the git diff output shows many unrelated changes in files I didn't edit. I need to be careful not to mention these as my changes. To get only the relevant edits, I might try `git diff -U0` for better context. The user wants to know the exact edits, so I need to focus on those. I suppose using `git blame` or `nl -ba` might help compare my changes accurately. I should ignore unrelated hunks and mention any existing changes cautiously.
thinking
**Clarifying git changes**

I'm seeing that the diff for `bar_cobar_adjunction_curved` and `coderived_models` includes unrelated modifications that might not be my changes. Since we edited the same file, I need to be careful not to claim those. I could mention that the worktree already had unrelated edits in those files and focus on my specific changes. It might be a good idea to check the status with `git diff -U0` and use `nl -ba` around my edits for accurate line numbers.
codex
The verification grep passed on the intended surface: the remaining `ordinary cohomology` hits in theory chapters are already fenced by a square-zero flat comparison or by an explicit coderived warning. I did notice the touched files already carry unrelated worktree diffs, so I’m isolating the exact line numbers of my own hunks before I close this out.
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '999,1042p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '432,447p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3172,3188p;3423,3432p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
   999	Theorem~\ref{thm:off-koszul-ran-inversion} resolves
  1000	structural gap~H1 (Remark~\ref{rem:structural-gaps}):
  1001	the coderived Ran-space formalism is now established.
  1002	Combined with the strict Koszul-locus inversion of
  1003	Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
  1004	proved package on the present surface: ordinary quasi-isomorphism on
  1005	the square-zero Koszul lane, coderived equivalence for all complete augmented
  1006	chiral algebras with finite-dimensional bar complex, and no silent
  1007	promotion of the off-Koszul curved statement back to ordinary
  1008	cohomology. The remaining issue is exactly the flat-side collapse
  1009	input needed for that promotion.
  1010	
  1011	The three-step proof (stratum-by-stratum Positselski,
  1012	factorization compatibility, conservative assembly) is the
  1013	factorization incarnation of Positselski's abstract
  1014	programme. The only input beyond the abstract theory is
  1015	the CDG-factorization compatibility
  1016	(\S\ref{subsec:CDG-factorization}), which ensures the
  1017	curved structure and the Ran-space stratification are
  1018	compatible.
 succeeded in 55ms:
   432	The coderived category reduces to the ordinary derived category.
   433	This is the regime of Theorem~B (bar-cobar inversion on the Koszul locus).
   434	
   435	\smallskip\noindent
   436	\emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
   437	\textup{(}$h \neq 0$\textup{)}.}
   438	The square-zero total comparison differential
   439	$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
   440	\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
   441	whereas the raw higher-genus fiber operator satisfies
   442	$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
   443	the coderived bar-object surface. The
   444	coderived--contraderived equivalence
   445	(Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
   446	The Positselski equivalence
   447	$D^{\mathrm{co}}(\barB^{\mathrm{ch}}(\cA)\text{-}\mathrm{comod}) \simeq
 succeeded in 51ms:
  3172	
  3173	\emph{Cocycle condition.}
  3174	The curved $A_\infty$ relation at $n=0$
  3175	(Definition~\ref{def:curved-ainfty}) gives
  3176	$\mu_1(m_0^{(g)}) = 0$, so $m_0^{(g)}$ is closed. Hence
  3177	$\dfib^{\,2} = m_0^{(g)} \ast (-)$ is the chain-level obstruction to
  3178	lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
  3179	to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
  3180	differential is already square-zero. Otherwise one must pass either to
  3181	the strict flat comparison differential $\Dg{g}$ of
  3182	Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
  3183	framework; ordinary cohomology of the curved fiber complex
  3184	$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
  3185	\end{proof}
  3186	
  3187	\emph{Step 2: Moduli space interpretation.}
  3188	
  3423	
  3424	\begin{corollary}[Curved differential formula; \ClaimStatusProvedHere]\label{cor:curved-differential}
  3425	For a curved chiral algebra $\mathcal{A}$ with curvature $\mu_0$, the fiberwise genus-$g$ bar
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}

exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3430,3435p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3430	Its square is the chain-level obstruction operator
  3431	\[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
  3432	whose cohomological shadow appears only after passage to the flat
  3433	comparison differential $\Dg{g}$ or the corresponding Chern--Weil
  3434	class.
  3435	\end{corollary}
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}

exec
/bin/zsh -lc "sed -n '36,72p' chapters/theory/derived_langlands.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '888,906p' chapters/theory/nilpotent_completion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6336,6376p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
H^n\bigl(\barB(\widehat{\fg}_{-h^\vee})\bigr)
\;\cong\;
\Omega^n\bigl(\mathrm{Op}_{\fg^\vee}(D)\bigr)
\qquad\text{for all } n \ge 0.
\]
This is Theorem~\ref{thm:oper-bar-dl}. It does not prove the full
categorical localization; it identifies the chain-level mechanism from
which the oper side of the Frenkel--Gaitsgory programme emerges.

To see why no other construction yields this identification, observe
the dichotomy. At generic level, the curvature $\kappa(\widehat{\fg}_k) \neq 0$
obstructs the formation of cohomology: the bar complex is a curved
dg-coalgebra with $d^2 = \kappa(\widehat{\fg}_k) \cdot \omega_1 \neq 0$, and no
functor from curved coalgebras to graded algebras recovers opers.
At critical level, $\kappa(\widehat{\fg}_{-h^\vee}) = 0$ is the \emph{unique} value at which
the bar differential squares to zero. The cobar construction
$\Omega(\barB(\widehat{\fg}_{-h^\vee}))$ then inverts to recover the
vertex algebra (Theorem~B), and the bar cohomology computes the oper
package. Any approach that avoids the bar complex must independently
 succeeded in 51ms:
\end{itemize}
In particular, $\mathrm{Vir}_{26-c}$ is reinterpreted as the
first page of the resonance spectral sequence, not the final dual.
\end{corollary}

\begin{proof}
Since $R_{\mathrm{Vir}} = \bk \cdot m_0$ with trivial
differential, $H^*(\barB(R)) = \bk$. The $E_1$ page is
therefore $H^*(\barB(\mathrm{Vir}_c^{>0})) \otimes \bk
= H^*(\barB(\mathrm{Vir}_c^{>0}))$. This is the
bar cohomology of the ``decurved'' Virasoro algebra (the
algebra with central charge set to zero in the bar complex),
which computes the same-family Koszul dual
$\mathrm{Vir}_{26-c}$ at the M/S-level. The higher pages
$d_r$ compute corrections from the curvature coupling $m_0$,
producing the full H-level Koszul dual.
\end{proof}

\begin{remark}[The Virasoro resonance model (resolved)]
 succeeded in 51ms:
\begin{remark}[Virasoro Koszulness requires the PBW framework]
The Virasoro algebra with central charge $c$ does \emph{not} admit a
Koszul dual in the standard \emph{quadratic} (uncurved) sense, because
its OPE involves a quartic pole. However, it \emph{is} chiral Koszul in
the PBW sense of Theorem~\ref{thm:virasoro-chiral-koszul}: the PBW
filtration yields a classical Koszul associated graded, and the
spectral sequence degenerates at~$E_2$. A \emph{completed curved}
same-family shadow can be constructed using the techniques of
\S\ref{sec:i-adic-completion}; the stronger H-level infinite-generator
dual object is delegated to the exact $W_\infty$ MC4 package of
filtered H-level targets, residue identities, and finite detection on
$\mathcal{I}_N$, whose first live higher-spin stages are already
reduced on the theorem surface to the stage-$3$ fifteen-coefficient
packet and the stage-$4$ six-coefficient packet organized as three
local OPE blocks, with the genuinely mixed stage-$4$ remaining problem reduced
to the single mixed $(3,4)$ triple.

\emph{Why the quadratic framework fails.}
\begin{enumerate}
\item The OPE involves a quartic pole:
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}


thinking
**Checking for issues**

I’m feeling relieved everything is safe and good! I should probably check to see if any of my edits unintentionally introduced any banned words. But so far, it looks good! I think I also need to update my plan to mark everything as complete. This is always a nice feeling, knowing I'm wrapping things up properly! Let's keep everything organized!
Plan update
I classified the live theory-chapter hits, patched the three passages that still blurred curved `\dfib^{\,2}=\kappa\omega_g` data with ordinary cohomology, and re-grepped the theory tree to confirm the remaining hits are already fenced by a square-zero flat comparison or coderived warning.
  ✓ Map all `d^2`, `spectral sequence`, and `cohomology` hits in `chapters/theory` and classify true positives for curved-vs-flat confusion
  ✓ Read the flagged passages in context, determine the minimum truthful qualifier or flat-side comparison needed, and prepare edits
  ✓ Apply minimal fixes in the affected theory files only
  ✓ Run targeted grep verification to confirm no unqualified curved-side ordinary cohomology language remains in scope
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}







thinking
**Considering git diff clarifications**

I need to address potential unintended differences caused by unrelated changes. The user should know that some files already had existing edits, and I'm only focusing on the specific lines I changed. It might be important to mention these pre-existing diffs, but I don't want to overdo it. I think I should present findings clearly in a requested format, including problem descriptions and exact edits made, along with verification lines for clarity. I’ll make sure everything refers to current line numbers and use clickable markdown links.
thinking
**Formulating edit presentation**

I’m considering how to format the findings for the user. It might be best to use a structure like "PROBLEM at [bar_cobar_adjunction_curved.tex](/Users/...:438): ..." for clarity. I should include the exact edit applied, perhaps with a direct quote or a paraphrase. The user specifically asked for the exact change, so I’ll provide the precise inserted text rather than a full old vs. new comparison. Keeping it straightforward could be key!
thinking
**Organizing findings**

I’m thinking about the user’s request for line references regarding the current issue with cobar_construction. There are certainly two edits, but I wonder if it’s better to present them as separate findings or combine them since they're in the same file and relate to the same issue cluster. 

The user wants clarity, which makes me consider presenting it as one finding per passage. Okay, I'll list the findings based on files and indicate the exact edits applied.
thinking
**Structuring findings**

I’m considering using three bullet points to clearly present the findings. For both coderived_models and cobar_construction, I'll include two exact edits each, which seems like an acceptable way to format the information. This approach should help keep everything organized and easy to understand for the user, ensuring they have clear visibility on each edit. It's nice to have a clear structure that makes it simpler for them to follow along!
thinking
**Structuring verification findings**

I think I need to note verification maybe as short, flat bullets after my findings. My proposed structure includes mentioning unrelated worktree edits. For example, I’ll list the problems found in specific files, detailing the exact edits applied. I should also state that I didn't run a TeX build since we only grepped. It’s important to ensure there are no nested bullets, and I should conclude by mentioning I edited only three files.
thinking
**Clarifying edits for problems**

I should consider including the exact edits applied in quotes but keep them concise. For each bullet point after a problem line, I can format it to have "EXACT edit applied: ..." to clarify what was changed. Long inline edits might get messy, so using a second sentence could help. I’m thinking of using fenced code for clarity and avoiding nested bullets. Each bullet could effectively contain two sentences to maintain organization and readability.
codex
These files already had unrelated worktree edits; the items below are only my hunks.

- PROBLEM at [bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:438): the genus-`g\ge 1` paragraph spoke about “ordinary bar-complex cohomology” on the higher-genus bar-object surface without naming that ordinary cohomology belongs to the square-zero comparison differential, not the curved fiber operator. EXACT edit applied: replaced that sentence with `The square-zero total comparison differential $d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology ... whereas the raw higher-genus fiber operator satisfies $\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on the coderived bar-object surface.`

- PROBLEM at [coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:1004): the H1-closure remark still left the off-Koszul promotion target too implicit, so the reader could still read “ordinary cohomology” as if it applied directly to the curved statement. EXACT edit applied: changed the summary to `ordinary quasi-isomorphism on the square-zero Koszul lane ... and no silent promotion of the off-Koszul curved statement back to ordinary cohomology. The remaining issue is exactly the flat-side collapse input needed for that promotion.` Also, at [coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex:1033), I rewrote the spectral-sequence evidence to say the `E_1` page abuts to ordinary cohomology only on the square-zero Koszul lane, while off the Koszul locus it controls `coderived coacyclicity of the curved cone rather than ordinary cohomology`.

- PROBLEM at [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3173): the curved `\dfib^{\,2}` discussion rejected ordinary cohomology, but it did not explicitly name the flat comparison differential or the curved complex being excluded. EXACT edit applied: changed the sentence to `Otherwise one must pass either to the strict flat comparison differential $\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived framework; ordinary cohomology of the curved fiber complex $(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.` Also, at [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:3430), I made the same flat-side comparison explicit by changing the corollary tail to `whose cohomological shadow appears only after passage to the flat comparison differential $\Dg{g}$ or the corresponding Chern--Weil class.`

Verification: I re-grepped `chapters/theory` for `ordinary cohomology`, curved/cohomology pairings, and spectral-sequence language. The remaining hits in `bar_cobar_adjunction_inversion.tex`, `chiral_hochschild_koszul.tex`, `higher_genus_foundations.tex`, and `higher_genus_complementarity.tex` already explicitly restrict ordinary cohomology to square-zero flat representatives or to coderived comparisons, so I left them unchanged. I did not run a TeX build.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_curved.tex b/chapters/theory/bar_cobar_adjunction_curved.tex
index 2346a3d6e34ed57c0ec8a3a2b2dd67408d397d3a..7ad542841848d0c893143fb022ed911f30fdcb9f
--- a/chapters/theory/bar_cobar_adjunction_curved.tex
+++ b/chapters/theory/bar_cobar_adjunction_curved.tex
@@ -435,10 +435,12 @@
 \smallskip\noindent
 \emph{Genus $g \geq 1$ with $\kappa(\cA) \neq 0$
 \textup{(}$h \neq 0$\textup{)}.}
-Ordinary bar-complex cohomology collapses on the higher-genus
-bar-object surface
+The square-zero total comparison differential
+$d_{\mathrm{total}} = \Dg{g}$ has trivial ordinary cohomology
 \textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
-but the
+whereas the raw higher-genus fiber operator satisfies
+$\dfib^{\,2} = \mcurv{g} \cdot \mathrm{id}$ and therefore lives only on
+the coderived bar-object surface. The
 coderived--contraderived equivalence
 (Theorem~\ref{thm:positselski-chiral-proved}) is nontrivial.
 The Positselski equivalence
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index fa460200c00b3720aea8c2171bfebfa81a1f4ece..baf55cf992bb32c62f1a00820d1c6d08f73cebec
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -3178,9 +3178,10 @@
 lifting the genus-$0$ square-zero differential (where $m_0^{(0)} = 0$)
 to genus~$g$. It vanishes exactly when the fiberwise genus-$g$
 differential is already square-zero. Otherwise one must pass either to
-the strict flat comparison differential or to the coderived framework;
-ordinary cohomology of the curved fiber complex is not the correct
-invariant.
+the strict flat comparison differential $\Dg{g}$ of
+Theorem~\ref{thm:quantum-diff-squares-zero} or to the coderived
+framework; ordinary cohomology of the curved fiber complex
+$(\bar{B}^{(g)}(\mathcal{A}), \dfib)$ is not the correct invariant.
 \end{proof}
 
 \emph{Step 2: Moduli space interpretation.}
@@ -3429,7 +3430,8 @@
 Its square is the chain-level obstruction operator
 \[\dfib^{\,2} = [\mu_0, -] \otimes \omega_g^2,\]
 whose cohomological shadow appears only after passage to the flat
-comparison differential or the corresponding Chern--Weil class.
+comparison differential $\Dg{g}$ or the corresponding Chern--Weil
+class.
 \end{corollary}
 \begin{proof}
 The genus-$g$ bar differential receives quantum corrections from the
diff --git a/chapters/theory/coderived_models.tex b/chapters/theory/coderived_models.tex
index 8cb170f178aeb4572416293277f6a695ddd92c1a..b276bfba3beb4c254ecd976cd61066e9768e02c6
--- a/chapters/theory/coderived_models.tex
+++ b/chapters/theory/coderived_models.tex
@@ -1002,11 +1002,11 @@
 Combined with the strict Koszul-locus inversion of
 Theorem~\ref{thm:bar-cobar-inversion-qi}, this gives the strongest
 proved package on the present surface: ordinary quasi-isomorphism on
-the Koszul lane, coderived equivalence for all complete augmented
+the square-zero Koszul lane, coderived equivalence for all complete augmented
 chiral algebras with finite-dimensional bar complex, and no silent
-promotion of the off-Koszul statement back to ordinary cohomology.
-The remaining issue is exactly the collapse input needed for that
-promotion.
+promotion of the off-Koszul curved statement back to ordinary
+cohomology. The remaining issue is exactly the flat-side collapse
+input needed for that promotion.
 
 The three-step proof (stratum-by-stratum Positselski,
 factorization compatibility, conservative assembly) is the
@@ -1034,8 +1034,10 @@
  The coderived bar-degree spectral sequence
  \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
  has the same strict associated-graded $E_1$ page on and off the
- Koszul locus; the difference is whether that page controls ordinary
- cohomology or coderived coacyclicity.
+ Koszul locus; on the square-zero Koszul lane that page abuts to
+ ordinary cohomology, while off the Koszul locus it controls
+ coderived coacyclicity of the curved cone rather than ordinary
+ cohomology.
 \item \emph{Completed Yangian case.}
  Corollary~\ref{cor:completed-bar-cobar-yangian}.
 \end{enumerate}

tokens used
101,347
