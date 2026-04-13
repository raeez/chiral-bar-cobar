# OA8_mc5_harmonic (352s)

**Findings**
- `CRITICAL` PROBLEM at [bv_brst.tex:2101](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2101), [bv_brst.tex:2103](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2103), [bv_brst.tex:2285](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2285): the recent change inserted a second copy of `prop:harmonic-factorization` inside the first proof, duplicated the label `prop:harmonic-factorization`, and left the first proof sentence broken at [bv_brst.tex:2098](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2098). FIX: delete one copy, restore a single continuous proof, and keep exactly one `\label{prop:harmonic-factorization}`.

- `CRITICAL` PROBLEM at [bv_brst.tex:1929](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1929), [bv_brst.tex:1998](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1998), [bv_brst.tex:2023](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2023), against [bv_brst.tex:2495](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2495) and [bv_brst.tex:2517](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2517): the proof uses a Hodge decomposition of the fiber complex `V_g = im(d_fib) ⊕ H_g ⊕ im(d_fib^*)` and `H_g ⊂ ker(d_fib)` while the same file later treats the positive-genus differential as curved with `d^2 = m_0·id`. The file supports a Hodge decomposition of the propagator, not of this curved complex. FIX: define the square-zero analytic differential whose Hodge splitting is being used and prove how it controls the curved bar model, or weaken the proposition to a statement only about the propagator correction.

- `SERIOUS` PROBLEM at [bv_brst.tex:2007](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2007), [bv_brst.tex:2021](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2021), [bv_brst.tex:2032](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2032): part (i) is not proved. The leg-pairing argument gives, at best, a heuristic degree bound; it does not show the exact exponent `⌊r/2⌋-1`, and the claim that `m_0` is the unique central degree-2 endomorphism of `H_g` is asserted without proof. FIX: add a separate lemma identifying the central harmonic endomorphism algebra and the exact curvature-counting mechanism, or weaken (i) to `m_0`-divisibility for `r ≥ 4`.

- `SERIOUS` PROBLEM at [bv_brst.tex:2048](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2048), [bv_brst.tex:2058](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2058), [bv_brst.tex:2075](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2075): the low-degree evaluations are unsupported. Step 1 does not imply `c_2=0`; the affine KM argument uses a single contraction `f^{abc} I_harm f^{cde}`, but Jacobi kills a cyclic sum, not that tensor; and `c_4(\cA)=S_4(\cA)` is a normalization statement with no comparison map. FIX: either supply explicit `r=2,3,4` computations/citations, or restrict the proposition to the supported `r ≥ 4` curvature-divisibility statement and remove the exact `c_2,c_3,c_4` identifications.

- `SERIOUS` PROBLEM at [bv_brst.tex:1961](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1961), [bv_brst.tex:2094](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2094), supported only by [w_algebras.tex:5273](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:5273): part (iii) overclaims that class `\mathsf M` has `c_r` generically nonzero for every `r ≥ 4` and that the factorization is sharp. The cited nontermination corollary proves the shadow tower is infinite, not that these harmonic coefficients are all nonzero or identified with the shadow coefficients. FIX: weaken to an existence statement about higher obstructions on the Virasoro/`\mathcal W_N` lines, or prove a bridge from `c_r` to the shadow tower.

Environment/status is locally matched (`proposition` + `\ClaimStatusProvedHere` + proof), but label uniqueness fails: `prop:harmonic-factorization` appears twice in this file and nowhere else in Vols I–III. On the audited block I found no AP126, AP132, AP165, AP113, or AP29 hits; the failures are structural and proof-theoretic.


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
session id: 019d889b-ab5b-7780-be4b-dd2c23512b99
--------
user
<task>
You are a Beilinson rectification auditor. Read the RECENT changes to the assigned file.
These changes were written by automated mathematical research agents. Your job:
(1) Verify mathematical correctness of every new proposition and proof
(2) Check all labels are unique, environments match status tags
(3) Check no AP violations introduced (AP126, AP132, AP29, AP165, AP113)
(4) Flag any gaps, incorrect steps, or unjustified claims
For each finding: PROBLEM at file:line + FIX.
</task>
<grounding_rules>Ground every claim in the file contents you read.</grounding_rules>
<completeness_contract>Audit EVERY new proposition and proof in the file.</completeness_contract>


Audit prop:harmonic-factorization in chapters/connections/bv_brst.tex. Verify: Hodge decomposition, centrality of m_0, degree counting (floor(r/2)-1), low-degree evaluations (c_2=0, c_3=0 for G/L, c_4=S_4), class-by-class vanishing.
mcp startup: no servers


thinking
**Planning code review findings**

I need to produce findings for a problem indicated at a specific file and line, aiming for a code review style. I want to ground my claims in the content of the file, since the user asked for an audit of changes. It seems like I may not need to edit unless requested. To inspect changes, I might run git diff on the file and consider recent changes. I could also use an explorer agent to check the codebase—they're generally faster and more reliable for this sort of task.
thinking
**Using explorer for code review**

Since this is a repo question, I might want to use the explorer to quickly locate recent changes and theorem surfaces. However, a math audit might require direct reading. The developer suggests preferring explorers over manual searches or file reading. I could spawn an explorer for file and diff context, along with another for relevant documentation. I won't need to re-read what the explorer covers, but I'll rely on its summaries and might need direct line references to ground my claims.
codex
Using `deep-beilinson-audit` for a theorem-level adversarial check and recent-diff review. I’m pulling the live surface first: recent diff for [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex), then the proposition/proof context and the required constitutional references.
exec
/bin/zsh -lc "rg -n \"prop:harmonic-factorization|harmonic factorization|begin\\{proposition\\}|begin\\{proof\\}|status|claim\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 52ms:
199:\begin{proof}[Geometric construction supporting \textup{Theorem~\ref{thm:bv-bar-geometric}}]
408:\begin{proof}
507:\begin{proof}
661:\begin{proof}
683:\begin{proposition}[Koszul duality preserves BRST anomaly cancellation; \ClaimStatusProvedHere]
720:\begin{proof}
941:\begin{proof}
1095:\begin{proof}
1156:\begin{proof}
1188:\begin{proof}
1239:\begin{proof}
1324:\begin{proof}
1379:\begin{proof}
1430:\begin{proof}
1658:\begin{proposition}[Three chain-level obstructions and harmonic factorization;
1732:\begin{proof}
1869:\begin{remark}[BV sewing at the chain level: class-by-class status;
1919:\begin{proposition}[Harmonic factorization of higher bar differentials;
1921:\label{prop:harmonic-factorization}%
1922:\index{harmonic factorization|textbf}%
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
 succeeded in 51ms:
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
**Reviewing file changes**

I need to review a specific file difference and theorem, but my first command, `git diff`, returned no output. That might mean there are no uncommitted changes. I should then check recent commits to the file using `git log -p -n 3` or `git show HEAD1`. I want to focus on recent changes, and I’ve noticed there are duplicate proposition labels at lines 1921 and 2103, so it’s important to inspect those areas. I might also look at the context from lines 1860-2160 for clarity.
codex
I have the constitutional surface. Next I’m isolating the proposition block and the file’s recent history, because the initial grep already shows a duplicate `prop:harmonic-factorization` label in the same file, which may indicate a duplicated insertion rather than a single clean edit.
exec
/bin/zsh -lc "sed -n '1880,2188p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
non-separating boundary divisor
$\delta^{\mathrm{ns}}\colon
\overline{\mathcal{M}}_{g,n+2} \to
\overline{\mathcal{M}}_{g+1,n}$.
Four complementary descriptions of this comparison
\textup{(}operator definition, spectral sequence, Heisenberg
extraction, modular operad\textup{)} lead to the following
class-by-class obstruction profile on the current written record.
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{lcl}
\toprule
Class & Status on current record & Comment \\
\midrule
$\mathsf{G}$ \textup{(}Heisenberg\textup{)}
 & chain-level curved equivalence & no interaction vertices \\
$\mathsf{L}$ \textup{(}affine KM\textup{)}
 & chain-level curved equivalence & Jacobi kills the cubic harmonic term \\
$\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git blame -L 1919,2188 -- chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git log --oneline --decorate -n 8 -- chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1919) \begin{proposition}[Harmonic factorization of higher bar differentials;
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1920) \ClaimStatusProvedHere]%
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1921) \label{prop:harmonic-factorization}%
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1922) \index{harmonic factorization|textbf}%
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1923) \index{bar complex!harmonic projection}%
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1924) \index{curvature!harmonic factorization through}%
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1925) Let~$\cA$ be a chirally Koszul algebra with curvature
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1926) $m_0 = \kappa(\cA)\cdot\omega_g$ at genus $g \geq 1$
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1927) \textup{(}cohomological degree~$+2$, central\textup{)}.
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1928) Let $d_{\mathrm{fib}}$ denote the fiber bar differential,
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1929) $H_g \subset \ker(d_{\mathrm{fib}})$ the harmonic subspace
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1930) of the Hodge decomposition, and
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1931) $P_{\mathrm{harm}} \colon V_g \twoheadrightarrow H_g$
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1932) the harmonic projector. For each $r \geq 2$, let
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1933) $\delta_r$ denote the degree-$r$ component of the discrepancy
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1934) between the BV differential and the bar differential, arising
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1935) from insertion of the harmonic propagator at
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1936) $r$-valent interaction vertices. Then:
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1937) \begin{enumerate}[label=\textup{(\roman*)}]
41ddfc45 (Raeez Lorgat 2026-04-13 22:34:22 +0200 1938) \item The harmonic projection
 succeeded in 52ms:
1a7ac45 (HEAD -> main, origin/main) MC5 harmonic factorization: prop:harmonic-factorization proves delta_r^harm mechanism (AP203 resolved)
41ddfc4 Residual lollipop→tadpole: 10 instances in higher_genus_modular_koszul.tex + standalones
02336ae Final gaps + elite rescue: 85 source files rectified across theory, examples, connections
eb521e0 Build artifacts, compute engines, audit reports, and standalone PDFs synchronised
56cd1ab Final sync: late-arriving frontier agent results
96e9a16 Session terminus: the 133-commit chiral quantum group programme
1d59361 Fix 3 test failures (198/198 pass): AP128 engine bug in averaging kernel + 2 test bugs
fd56627 Coderived E_3 obstruction analysis: Steps 1-2 proved, Step 3 (categorical infrastructure) open. conj:coderived-e3 stays conjectural.

thinking
**Evaluating propositions**

I'm considering auditing the propositions at 1919 and 2101. The first one might have an incomplete proof due to some duplication that was added before the end. As for the second, I wonder if it’s complete or also just a duplicate? It seems like I need to read more thoroughly to get a clearer understanding of both propositions and see how they differ or align.
codex
The last commit did not just add a new proposition; it spliced a second copy of the same proposition into the middle of the first proof. I’m reading the surrounding dependency chain now to separate structural breakage from the actual mathematical claims.
exec
/bin/zsh -lc "sed -n '2188,2288p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\label\\{prop:harmonic-factorization\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1628,1888p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"prop:chain-level-three-obstructions|thm:bv-bar-coderived|cor:virasoro-postnikov-nontermination|S_4\\(|quartic shadow|harmonic propagator|Hodge decomposition\" chapters/connections/bv_brst.tex chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{prop:harmonic-factorization\})
       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
= P_{\mathrm{harm}} \circ \delta_r |_{H_g}$
is a map from harmonics to harmonics. The $r$-valent
interaction vertex involves $r$ external legs from the fiber.
Insertion of the harmonic propagator contracts these legs
pairwise: each contraction through $P_{\mathrm{harm}}$
pairs two fiber directions and contributes cohomological
degree~$+2$. With $r$ legs, at most
$\lfloor r/2 \rfloor$ pairwise contractions are possible.
One contraction is already accounted for by the propagator
insertion that creates the discrepancy~$\delta_r$ itself.
The remaining $\lfloor r/2 \rfloor - 1$ contractions
contribute total cohomological degree
$2(\lfloor r/2 \rfloor - 1)$ to the harmonic-to-harmonic
map.

On~$H_g$, the curvature $m_0$ is the unique
\textup{(}up to scalar\textup{)} central endomorphism of
cohomological degree~$+2$: it is the restriction
of $d_{\mathrm{fib}}^2$ to $H_g$, and no other central
operator of that degree exists because the fiber model is
 succeeded in 52ms:
Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
consequence predicted by
Conjecture~\ref{conj:master-bv-brst} for the Heisenberg
family at all genera.
The Heisenberg succeeds because it is class~G:
a single Gaussian channel, no interaction vertices, and
all moduli dependence controlled by the Quillen anomaly.
For non-free theories, the scalar identification requires
the shadow obstruction tower machinery
\textup{(}Theorem~D for uniform-weight algebras;
the multi-weight genus expansion for $W_N$\textup{)}.

What remains open, even for
free fields, is:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item the chain-level quasi-isomorphism between the BV complex and
 the bar complex at genus $g \geq 1$;
\item the identification of the BV Laplacian with the sewing
 operator on the bar complex;
 succeeded in 51ms:
chapters/connections/bv_brst.tex:33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
chapters/connections/bv_brst.tex:1660:\label{prop:chain-level-three-obstructions}
chapters/connections/bv_brst.tex:1673: By Hodge decomposition, $P = d\log E + P_{\mathrm{ex}}
chapters/connections/bv_brst.tex:1690:\item \textbf{Higher-degree coupling through the harmonic propagator.}
chapters/connections/bv_brst.tex:1733:Obstruction~(1): the Hodge decomposition
chapters/connections/bv_brst.tex:1745:fiber model at genus~$g$. Hodge decomposition gives
chapters/connections/bv_brst.tex:1848:system at genus~$1$, despite the nonzero quartic shadow
chapters/connections/bv_brst.tex:1855:Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
chapters/connections/bv_brst.tex:1861:identity. Proposition~\ref{prop:chain-level-three-obstructions}
chapters/connections/bv_brst.tex:1863:curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
chapters/connections/bv_brst.tex:1909:in the ordinary chain complex. Proposition~\ref{prop:chain-level-three-obstructions}
chapters/connections/bv_brst.tex:1911:powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
chapters/connections/bv_brst.tex:1930:of the Hodge decomposition, and
chapters/connections/bv_brst.tex:1935:from insertion of the harmonic propagator at
chapters/connections/bv_brst.tex:1956:$c_4(\cA) = S_4(\cA)$, the quartic shadow invariant.
chapters/connections/bv_brst.tex:1968:The proof proceeds through Hodge decomposition, degree
chapters/connections/bv_brst.tex:1972:\emph{Step~1: Hodge decomposition isolates the harmonic
chapters/connections/bv_brst.tex:1974:At genus $g \geq 1$, the Hodge decomposition of the BV
chapters/connections/bv_brst.tex:2009:Insertion of the harmonic propagator contracts these legs
chapters/connections/bv_brst.tex:2033:\textup{(}the harmonic propagator is constructed from the
codex
I have enough context to start separating proof defects from theorem-state defects. I’m pulling exact line numbers and the last-commit patch now, then I’ll check whether the stated low-degree formulas and class-vanishing claims are actually supported elsewhere in the repo rather than only restated here.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1918,2292p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git show --stat --patch 1a7ac45 -- chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
commit 1a7ac45695ee6052704fad949e4e0ab1d07b81d2
Author: Raeez Lorgat <raeez@momentum.inc>
Date:   Mon Apr 13 22:41:04 2026 +0200

    MC5 harmonic factorization: prop:harmonic-factorization proves delta_r^harm mechanism (AP203 resolved)
    
    prop:harmonic-factorization (182 lines) proves that the harmonic projection of
    the degree-r BV/bar discrepancy factors through powers of the curvature m_0:
      delta_r^harm = c_r(A) * m_0^{floor(r/2)-1}
    
    Five-step proof:
      (1) Hodge decomposition isolates harmonic discrepancy; d_fib-exact commutator
          contributes only chain homotopy.
      (2) Centrality of m_0 = d_fib^2: degree +2, commutes with P_harm, restricts
          to central endomorphism of H_g.
      (3) Degree counting: r legs pairwise through P_harm yield floor(r/2) pairings;
          one absorbed by propagator; remaining floor(r/2)-1 contribute m_0 powers.
          m_0 is the unique central degree-+2 endomorphism of H_g.
      (4) Low-degree: c_2=0 (Hodge homotopy), c_3=0 for G/L (Jacobi), c_4=S_4(A)
          (quartic shadow; Vir: 10/[c(5c+22)] != 0 at generic c).
 succeeded in 117ms:
  1918	
  1919	\begin{proposition}[Harmonic factorization of higher bar differentials;
  1920	\ClaimStatusProvedHere]%
  1921	\label{prop:harmonic-factorization}%
  1922	\index{harmonic factorization|textbf}%
  1923	\index{bar complex!harmonic projection}%
  1924	\index{curvature!harmonic factorization through}%
  1925	Let~$\cA$ be a chirally Koszul algebra with curvature
  1926	$m_0 = \kappa(\cA)\cdot\omega_g$ at genus $g \geq 1$
  1927	\textup{(}cohomological degree~$+2$, central\textup{)}.
  1928	Let $d_{\mathrm{fib}}$ denote the fiber bar differential,
  1929	$H_g \subset \ker(d_{\mathrm{fib}})$ the harmonic subspace
  1930	of the Hodge decomposition, and
  1931	$P_{\mathrm{harm}} \colon V_g \twoheadrightarrow H_g$
  1932	the harmonic projector. For each $r \geq 2$, let
  1933	$\delta_r$ denote the degree-$r$ component of the discrepancy
  1934	between the BV differential and the bar differential, arising
  1935	from insertion of the harmonic propagator at
  1936	$r$-valent interaction vertices. Then:
  1937	\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "rg -n \"S_4\\(\\\\mathrm\\{Vir\\}_c\\)|10/\\[c\\(5c\\+22\\)\\]|quartic shadow invariant|shadow depth r_\\{max\\} = 3|Jacobi kills.*quartic|c_3\\(\\\\cA\\) = 0|c_4\\(\\\\cA\\) = S_4\" chapters/examples/w_algebras.tex chapters/examples/kac_moody.tex chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "label{prop:harmonic-factorization}" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:S_4\(\mathrm\{Vir\}_c\)|10/\[c\(5c\+22\)\]|quartic shadow invariant|shadow depth r_\{max\} = 3|Jacobi kills.*quartic|c_3\(\cA\) = 0|c_4\(\cA\) = S_4)
            ^^
error: unrecognized escape sequence
 succeeded in 228ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1921:\label{prop:harmonic-factorization}%
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2103:\label{prop:harmonic-factorization}%



thinking
**Evaluating pairings and m0**

I'm considering why the remaining pairings correspond to extra m0. It seems more heuristic than rigorous. Maybe I should approach it with a low-degree r=4; the formula suggests m0 raised to the first power. That aligns with having one extra pair, apart from the discrepancy propagator, but it's still a bit unclear. I need to reconsider the approach to ensure I'm on the right track.
thinking
**Reviewing shadow corrections**

I need to confirm if the quartic shadow indeed vanishes by Jacobi, rather than focusing on the cubic harmonic correction. Class L has a shadow depth of r_max=3, which indicates that the cubic shadow is nonzero while the quartic shadow is zero. The proposition claims that c_3 = 0, and that seems plausible because the harmonic correction differs from the cubic shadow. However, the proof via a single contraction expression seems invalid, so I should flag that for review.
thinking
**Evaluating quartic corrections**

The proof only demonstrates that the quartic correction is the first nontrivial term that is curvature-divisible, but it doesn’t show that the coefficient matches the existing quartic shadow normalization. They identify c_4 with S_4 from the Maurer-Cartan class without any computation, which seems likely unsupported. I should check the repository to see if the same formula appears and search with a fixed string to gather more information.
codex
The structural failure is clear. I’m checking the substance now: whether the proof’s two strongest steps, `c_3=0` for class `L` and `c_4=S_4`, are actually derived anywhere, because those are the parts most likely to overclaim beyond what the cited shadow machinery proves.
exec
/bin/zsh -lc "rg -n -F \"S_4(\\mathrm{Vir}_c) = 10/[c(5c+22)]\" chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"c_4(\\cA) = S_4(\\cA)\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex:2083:$S_4(\mathrm{Vir}_c) = 10/[c(5c+22)] \neq 0$
chapters/connections/bv_brst.tex:2265:$S_4(\mathrm{Vir}_c) = 10/[c(5c+22)] \neq 0$
chapters/connections/entanglement_modular_koszul.tex:948: $S_4(\mathrm{Vir}_c) = 10/[c(5c+22)]$ Substituted into the
 succeeded in 52ms:
chapters/connections/bv_brst.tex:1956:$c_4(\cA) = S_4(\cA)$, the quartic shadow invariant.
chapters/connections/bv_brst.tex:2076:invariant: $c_4(\cA) = S_4(\cA)$, the degree-$4$
chapters/connections/bv_brst.tex:2138:$c_4(\cA) = S_4(\cA)$, the quartic shadow invariant.
chapters/connections/bv_brst.tex:2258:invariant: $c_4(\cA) = S_4(\cA)$, the degree-$4$
exec
/bin/zsh -lc "rg -n -F \"m_0 = \\kappa(\\cA)\\cdot\\omega_g\" chapters/connections/bv_brst.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "f''^{abc}f''^{cde}" chapters/connections/bv_brst.tex chapters/examples/kac_moody.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/bar_complex_tables.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"shadow depth r_{\\max} = 3\" chapters/examples/kac_moody.tex chapters/examples/landscape_census.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "cor:virasoro-postnikov-nontermination" chapters/examples/w_algebras.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex:1755:curvature $m_0 = \kappa(\cA)\cdot\omega_g$ is central of
chapters/connections/bv_brst.tex:1926:$m_0 = \kappa(\cA)\cdot\omega_g$ at genus $g \geq 1$
chapters/connections/bv_brst.tex:2108:$m_0 = \kappa(\cA)\cdot\omega_g$ at genus $g \geq 1$
chapters/connections/bv_brst.tex:2399: $m_0 = \kappa(\cA)\cdot\omega_g$, so the full discrepancy is
 exited 1 in 51ms:

 succeeded in 51ms:
chapters/connections/bv_brst.tex:1779:$f^{abc}f^{cde} + \text{cyclic} = 0$ force this coefficient to
 succeeded in 51ms:
chapters/connections/bv_brst.tex:2095:terminate \textup{(}Corollary~\ref{cor:virasoro-postnikov-nontermination}\textup{)},
chapters/connections/bv_brst.tex:2277:terminate \textup{(}Corollary~\ref{cor:virasoro-postnikov-nontermination}\textup{)},
chapters/connections/bv_brst.tex:2562:Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
chapters/connections/bv_brst.tex:2594:Corollary~\ref{cor:virasoro-postnikov-nontermination} shows why
chapters/examples/w_algebras.tex:5275:\label{cor:virasoro-postnikov-nontermination}
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5260,5325p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '4436,4452p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  5260	$\beta\gamma$ & $4$ (contact) & rank-one rigidity &
  5261	quartic on weight line \\
  5262	Virasoro/$\mathcal{W}_N$ & $\infty$ & permanent cubic source &
  5263	non-polynomial \\
  5264	\bottomrule
  5265	\end{tabular}
  5266	\end{center}
  5267	For the infinite-tower families, $\Theta_\cA = \varprojlim_r
  5268	\Theta_\cA^{\leq r}$
  5269	(Theorem~\ref{thm:recursive-existence}) is genuinely
  5270	infinite-order: the complementarity potential is non-polynomial.
  5271	\end{remark}
  5272	
  5273	\begin{corollary}[Virasoro/$\mathcal{W}_N$ shadow obstruction tower:
  5274	infinite; \ClaimStatusProvedHere]
  5275	\label{cor:virasoro-postnikov-nontermination}
  5276	\index{shadow obstruction tower!Virasoro non-termination}
  5277	The shadow obstruction tower
  5278	\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}
  5279	of the Virasoro algebra \textup{(}and principal
 succeeded in 52ms:
  4436	 \textup{(}Lie bracket\textup{)},
  4437	 $S_3(\mathcal{W}_N^k) = 2$ \textup{(}stress-tensor $T_{(1)}T = 2T$\textup{)},
  4438	 and the ratio $S_3(\mathcal{W}_N)/S_3(V_k(\mathfrak{sl}_N)) = 2$
  4439	 is universal in $N$ and~$k$.
  4440	\item \emph{Quartic creation from zero.}
  4441	 $S_4(V_k(\mathfrak{sl}_N)) = 0$ \textup{(}Jacobi identity kills the
  4442	 quartic obstruction for affine algebras\textup{)},
  4443	 but $S_4(\mathcal{W}_N^k) \neq 0$ for generic~$k$.
  4444	 For Virasoro: $S_4(\mathrm{Vir}_c) = 10/[c(5c{+}22)]$.
  4445	\item \emph{Commutation failure.}
  4446	 The DS-shadow diagram does \emph{not} commute: $\kappa$ is not
  4447	 additive under DS \textup{(}the ghost constant
  4448	 $C(N,k) = \kappa(V_k(\mathfrak{sl}_N)) - \kappa(\mathcal{W}_N^k)$
  4449	 depends on~$k$\textup{)}, and $S_r$ disagrees at every degree
  4450	 $r \geq 2$. Central charge~$c$ is additive
  4451	 \textup{(}$c(V_k) = c(\mathcal{W}_N^k) + N(N{-}1)$\textup{)},
  4452	 but $\kappa$ is not.
exec
/bin/zsh -lc 'rg -n -F "LOCAL: scope fixed in this environment" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/entanglement_modular_koszul.tex | sed -n '940,954p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   940	\item \emph{Cardy one-loop at large $n$.}
   941	 Gaussian fluctuation around the saddle $\tau_* = i\sqrt{c/(24n)}$
   942	 produces a determinant $(\det K)^{-1/2}$ with three soft modes
   943	 \textup{(}two translations plus dilation\textup{)}, yielding
   944	 $-\tfrac{3}{2}\log S_0$ \cite{Carlip98,Cardy86}.
   945	\item \emph{Shadow tower identification.}
   946	 The quartic shadow projection $Q^{\mathrm{contact}}$ for
   947	 $\mathrm{Vir}_c$ gives
   948	 $S_4(\mathrm{Vir}_c) = 10/[c(5c+22)]$ Substituted into the
   949	 saddle-point expansion of the $\hat{A}$-genus generating
   950	 function, the quartic shadow contributes exactly
   951	 $-\tfrac{3}{2}\log S_0$ through the Hessian ratio
   952	 $\det(F''_0)/F''_0$.
   953	\item \emph{Hartle--Hawking inner product.}
   954	 Direct evaluation of
 exited 1 in 51ms:

codex
I’ve isolated the main mathematical overclaims. I’m doing a final pass for the requested APs on the audited block itself so the review cleanly separates structural defects, proof gaps, and any formula-policy violations.
exec
/bin/zsh -lc "sed -n '1919,2285p' chapters/connections/bv_brst.tex | rg -n -i \"moreover|additionally|notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate\"" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1919,2285p' chapters/connections/bv_brst.tex | rg -n -F \"\\Omega/z\"" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '1919,2285p' chapters/connections/bv_brst.tex | rg -n -F \"SC\"" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1919,2285p' chapters/connections/bv_brst.tex | rg -n -F \"T"'^c(s''^{-1} A)"' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:





thinking
**Evaluating theorem and issues**

I think I need to look into the use of the theorem or potential corollary and consider its relation to the proposition line. Although it's not necessary, it could be worth mentioning since the theorem cites the proposition and might inherit its problems. The user asked for an audit of the proposition, so I should focus on exact findings in terms of file and line numbers and any fixes needed. 

I'll also be sure to note structural issues related to duplicate insertions and highlight specific mathematical issues at certain lines.
thinking
**Analyzing duplicate labels and proofs**

I’m considering that the duplicate label might be AP125, although the user didn’t ask about that. It’s important to note that no requested AP formula violations were found, but the duplicate proposition causes label uniqueness issues. I need to verify if every new proposition and proof is included. It seems like a recent commit may have inadvertently inserted two copies due to a manual merge. 

I should also mention the structural problem with the proposition being nested improperly within an open proof. It could lead to a malformed environment, which is critical. I need to get the file lines and check the validity of the first proof as well, especially if the duplicate is removed. This could signify potential warnings or errors that should be compiled.
thinking
**Investigating theorem nesting issues**

I’m realizing that theorem environments can nest, and actually, amsthm allows theorems inside proofs. However, nesting could cause weird italicization and other formatting issues, so it’s definitely problematic. The user asked for an audit of recent changes, which gives me a clear direction. I need to identify the last commit that accidentally inserted the duplicate block. 

Using `git show`, I can see the differences that demonstrate this. I should also mention that `git show 1a7ac45` inserted the second copy at line 2100 within the open proof, which is crucial to highlight.
thinking
**Considering technical clarity**

I need to suggest a fix here. Maybe I can replace the phrase with something clearer, like, "for class L, only quartic and higher coefficients vanish from shadow depth; the cubic coefficient requires a separate explicit cyclic-symmetrized computation." Alternatively, I could recommend citing a precise affine KM proposition that includes the actual cyclic tensor since the user seems focused on addressing gaps. It's important, especially considering that claim part (ii) states c3=0 for class L, which might affect the proposition.
codex
There is one more structural point I need to check before I close: the proof treats `d_{\mathrm{fib}}` as if ordinary Hodge theory applies, but elsewhere the chapter also says the fiber model is curved at positive genus. I’m checking whether the file itself distinguishes a square-zero differential from the curved one, because that affects the validity of the whole Hodge-decomposition step.
exec
/bin/zsh -lc "rg -n -F \"d_{\\mathrm{fib}}\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Hodge decomposition" chapters/connections/bv_brst.tex chapters/theory/higher_genus_foundations.tex chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "d''^2 = m_0" chapters/connections/bv_brst.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2328,2410p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1749:d\log E + [d_{\mathrm{fib}}, h] + P_{\mathrm{harm}},
1928:Let $d_{\mathrm{fib}}$ denote the fiber bar differential,
1929:$H_g \subset \ker(d_{\mathrm{fib}})$ the harmonic subspace
1979:d\log E + [d_{\mathrm{fib}}, h] + P_{\mathrm{harm}},
1984:subspace~$H_g$. The commutator $[d_{\mathrm{fib}}, h]$
1985:is $d_{\mathrm{fib}}$-exact and therefore contributes
1998:$V_g = \operatorname{im}(d_{\mathrm{fib}})
1999:\oplus H_g \oplus \operatorname{im}(d_{\mathrm{fib}}^*)$.
2024:of $d_{\mathrm{fib}}^2$ to $H_g$, and no other central
2026:generated by $d_{\mathrm{fib}}$ and the chiral product,
2052:$[d_{\mathrm{fib}}, h]$ already absorbs this replacement
2110:Let $d_{\mathrm{fib}}$ denote the fiber bar differential,
2111:$H_g \subset \ker(d_{\mathrm{fib}})$ the harmonic subspace
2161:d\log E + [d_{\mathrm{fib}}, h] + P_{\mathrm{harm}},
2166:subspace~$H_g$. The commutator $[d_{\mathrm{fib}}, h]$
2167:is $d_{\mathrm{fib}}$-exact and therefore contributes
2180:$V_g = \operatorname{im}(d_{\mathrm{fib}})
2181:\oplus H_g \oplus \operatorname{im}(d_{\mathrm{fib}}^*)$.
2206:of $d_{\mathrm{fib}}^2$ to $H_g$, and no other central
2208:generated by $d_{\mathrm{fib}}$ and the chiral product,
 succeeded in 50ms:
chapters/connections/bv_brst.tex:2495:$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. Theorem~\ref{thm:bv-bar-coderived}
chapters/connections/bv_brst.tex:2517:$d^2 = m_0 \cdot \mathrm{id}$ is permitted. The bar complex
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:3296:By the Hodge decomposition, $\mathcal{H}^{1,1}(\Sigma_g)$
chapters/connections/bv_brst.tex:1673: By Hodge decomposition, $P = d\log E + P_{\mathrm{ex}}
chapters/connections/bv_brst.tex:1733:Obstruction~(1): the Hodge decomposition
chapters/connections/bv_brst.tex:1745:fiber model at genus~$g$. Hodge decomposition gives
chapters/connections/bv_brst.tex:1930:of the Hodge decomposition, and
chapters/connections/bv_brst.tex:1968:The proof proceeds through Hodge decomposition, degree
chapters/connections/bv_brst.tex:1972:\emph{Step~1: Hodge decomposition isolates the harmonic
chapters/connections/bv_brst.tex:1974:At genus $g \geq 1$, the Hodge decomposition of the BV
chapters/connections/bv_brst.tex:2112:of the Hodge decomposition, and
chapters/connections/bv_brst.tex:2150:The proof proceeds through Hodge decomposition, degree
chapters/connections/bv_brst.tex:2154:\emph{Step~1: Hodge decomposition isolates the harmonic
chapters/connections/bv_brst.tex:2156:At genus $g \geq 1$, the Hodge decomposition of the BV
chapters/connections/bv_brst.tex:2333:For $g \geq 1$, Hodge decomposition writes the BV propagator as
chapters/connections/bv_brst.tex:2393:\item Hodge decomposition on the fiber model isolates the harmonic
 succeeded in 50ms:
  2328	
  2329	\begin{proof}
  2330	At genus~$0$, the comparison is the chain-level quasi-isomorphism
  2331	of Theorem~\ref{thm:bv-bar-geometric}.
  2332	
  2333	For $g \geq 1$, Hodge decomposition writes the BV propagator as
  2334	\[
  2335	P_{\mathrm{BV}}
  2336	\;=\;
  2337	d\log E + [d_{\mathrm{fib}}, h] + P_{\mathrm{harm}}.
  2338	\]
  2339	The commutator term contributes only a chain homotopy, so the
  2340	failure of~$f_g$ to intertwine the two curved differentials is the
  2341	harmonic discrepancy
  2342	$\delta^{\mathrm{harm}} = \sum_{r \geq 4}\delta_r^{\mathrm{harm}}$.
  2343	Proposition~\ref{prop:harmonic-factorization} gives the
  2344	factorization
  2345	$\delta_r^{\mathrm{harm}} = c_r(\cA) \cdot
  2346	m_0^{\lfloor r/2 \rfloor - 1}$, and
  2347	Proposition~\ref{prop:chain-level-three-obstructions} gives the
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2488,2522p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2488	piece from $H^{0,1}(\Sigma_g)$. The BV formalism uses the
  2489	\emph{full} propagator; the bar complex uses only
  2490	$P_{\mathrm{bar}} = d\log E(z,w)$. The discrepancy at degree~$r$
  2491	is controlled by the harmonic piece. This shows why curvature
  2492	appears in higher genus: the harmonic sector is invisible to the
  2493	genus-$0$ bar differential but survives in the BV propagator.
  2494	Passing to the coderived setting is therefore natural once
  2495	$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. Theorem~\ref{thm:bv-bar-coderived}
  2496	supplies the missing step: curvature factorization forces the
  2497	comparison cone to be coacyclic.
  2498	
  2499	\emph{The spacetime viewpoint.}
  2500	In the Costello--Li framework of twisted supergravity, the bulk
  2501	theory on $\mathrm{AdS}_{d+1}$ is computed by Witten diagrams
  2502	using the bulk propagator, while the boundary theory is computed
  2503	by the bar complex using the boundary OPE. The mismatch between
  2504	bulk and boundary propagators at one loop ($g = 1$) is the
  2505	holographic anomaly: the Weyl anomaly coefficient
  2506	$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
  2507	correction to the BV/bar comparison. The coderived formalism


thinking
**Analyzing mathematical propositions**

I'm noticing a potential issue with the proposition from 1925 that includes curvature and relates it to genus g≥1, specifically the equation `m_0 = kappa(A)·ω_g`. For class G with k=0, it seems like m0 could be zero, which might not be a problem. However, part (iii) raises another concern regarding class L, stating `c_r=0 for all r`, but only arguments for r≥4 plus c3 are mentioned. I think c2 is necessary since it's universal.
thinking
**Crafting findings**

I'm thinking it might be useful to mention class G/L c3. Also, the AP29 grep didn't yield any results, which is important to note. I want to ensure the final style is clean and avoids a standard opener. I could just start directly with a header **Findings** and use bullets for clarity, but no nested bullets to keep things straightforward. Alright, let’s create it concisely while still including enough detail.
codex
**Findings**
- `CRITICAL` PROBLEM at [bv_brst.tex:2101](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2101), [bv_brst.tex:2103](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2103), [bv_brst.tex:2285](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2285): the recent change inserted a second copy of `prop:harmonic-factorization` inside the first proof, duplicated the label `prop:harmonic-factorization`, and left the first proof sentence broken at [bv_brst.tex:2098](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2098). FIX: delete one copy, restore a single continuous proof, and keep exactly one `\label{prop:harmonic-factorization}`.

- `CRITICAL` PROBLEM at [bv_brst.tex:1929](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1929), [bv_brst.tex:1998](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1998), [bv_brst.tex:2023](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2023), against [bv_brst.tex:2495](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2495) and [bv_brst.tex:2517](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2517): the proof uses a Hodge decomposition of the fiber complex `V_g = im(d_fib) ⊕ H_g ⊕ im(d_fib^*)` and `H_g ⊂ ker(d_fib)` while the same file later treats the positive-genus differential as curved with `d^2 = m_0·id`. The file supports a Hodge decomposition of the propagator, not of this curved complex. FIX: define the square-zero analytic differential whose Hodge splitting is being used and prove how it controls the curved bar model, or weaken the proposition to a statement only about the propagator correction.

- `SERIOUS` PROBLEM at [bv_brst.tex:2007](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2007), [bv_brst.tex:2021](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2021), [bv_brst.tex:2032](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2032): part (i) is not proved. The leg-pairing argument gives, at best, a heuristic degree bound; it does not show the exact exponent `⌊r/2⌋-1`, and the claim that `m_0` is the unique central degree-2 endomorphism of `H_g` is asserted without proof. FIX: add a separate lemma identifying the central harmonic endomorphism algebra and the exact curvature-counting mechanism, or weaken (i) to `m_0`-divisibility for `r ≥ 4`.

- `SERIOUS` PROBLEM at [bv_brst.tex:2048](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2048), [bv_brst.tex:2058](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2058), [bv_brst.tex:2075](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2075): the low-degree evaluations are unsupported. Step 1 does not imply `c_2=0`; the affine KM argument uses a single contraction `f^{abc} I_harm f^{cde}`, but Jacobi kills a cyclic sum, not that tensor; and `c_4(\cA)=S_4(\cA)` is a normalization statement with no comparison map. FIX: either supply explicit `r=2,3,4` computations/citations, or restrict the proposition to the supported `r ≥ 4` curvature-divisibility statement and remove the exact `c_2,c_3,c_4` identifications.

- `SERIOUS` PROBLEM at [bv_brst.tex:1961](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1961), [bv_brst.tex:2094](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2094), supported only by [w_algebras.tex:5273](/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:5273): part (iii) overclaims that class `\mathsf M` has `c_r` generically nonzero for every `r ≥ 4` and that the factorization is sharp. The cited nontermination corollary proves the shadow tower is infinite, not that these harmonic coefficients are all nonzero or identified with the shadow coefficients. FIX: weaken to an existence statement about higher obstructions on the Virasoro/`\mathcal W_N` lines, or prove a bridge from `c_r` to the shadow tower.

Environment/status is locally matched (`proposition` + `\ClaimStatusProvedHere` + proof), but label uniqueness fails: `prop:harmonic-factorization` appears twice in this file and nowhere else in Vols I–III. On the audited block I found no AP126, AP132, AP165, AP113, or AP29 hits; the failures are structural and proof-theoretic.
tokens used
187,072
