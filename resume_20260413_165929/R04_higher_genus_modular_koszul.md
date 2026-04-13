# R04_higher_genus_modular_koszul (780s)

I verified the seven requested surfaces in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2911). Most proof-level findings were already repaired on the current theorem surfaces; the live downstream contradiction was the class-`\mathbf{C}` witness in `thm:shadow-separation`, and I corrected that proof plus the local representative tables/figures so they now consistently use the full `\beta\gamma_\lambda` family. I did not run a full TeX build; verification was by re-reading the touched sections and grep-checking the referenced labels/phrases. The introduction MC2/E1 cross-reference was already correct in [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2059), so I did not edit outside the assigned file.

## Rectification Summary
- [FIXED] finding 1 — Theorem D already has the non-circular routing remark in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2911): `thm:mc2-bar-intrinsic` builds the shadow tower, `thm:genus-universality` extracts `\mathrm{obs}_g=\kappa\lambda_g`, and `thm:family-index` is explicitly downstream.
- [FIXED] finding 2 — The PBW/Whitehead gap is already closed in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:916) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:971): the weightwise enrichment is rewritten as finite-dimensional `\fg`-modules, and the mixed map is factored through `H^1(\fg,-)` instead of the truncated current algebra.
- [FIXED] finding 3 — MC2 scope is already explicit in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3830): `thm:mc2-bar-intrinsic` is only the coinvariant/symmetric statement, while the ordered `E_1` lift is `thm:e1-mc-element`. The flagged introduction citation was already corrected and needed no new edit.
- [FIXED] finding 4 — The genuswise-product vs completed-tensor identification is already made explicit in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3794) and used again in the proof at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3967), so `\Theta_\cA` is no longer used tacitly as an element of `\Defcyc(\cA)\widehat\otimes\Gmod`.
- [FIXED] finding 5 — The depth-gap proposition is already correctly split in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17609): `\kappa|_L\neq0` lines give `{0,1,\infty}`, and the boundary value `d_{\mathrm{alg}}=2` is isolated to the global `\beta\gamma_\lambda` family.
- [FIXED] finding 6 — I repaired the residual contradiction in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:19478): `thm:shadow-separation` no longer uses the obsolete weight-changing-line witness, and now compares `\cH_1` with `\beta\gamma_1` on the full conformal-weight family. I also propagated that correction through the nearby representative surfaces at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12360), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12433), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17012), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:19245), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:20355), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:26669), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:30710), and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:35313).
- [FIXED] finding 7 — The ambient `D^2=0` theorem already uses the correct universal-family carrier in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:31745): the proof now explicitly rejects fixed-curve log-FM as insufficient and works over the relative Fulton-MacPherson compactification of the universal stable family over `\overline{\cM}_{g,n}`.


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
session id: 019d87a6-51db-7660-a008-a6621cf1e212
--------
user
<task>
You are a RECTIFICATION agent for a research mathematics manuscript on operadic Koszul duality.
Your mission: fix the specific findings below with the STRONGEST technical choice.
Hierarchy: (1) strengthen proof > (2) add missing lemma > (3) narrow claim to match proof > (4) mark conditional.
NEVER weaken when you can strengthen. NEVER leave a gap unfixed.
</task>

<action_safety>
Only edit the specific file(s) assigned. Do not touch other files.
Make the MINIMUM truthful edit that resolves each finding.
After each edit, re-read surrounding context to verify coherence.
</action_safety>

<verification_loop>
After all edits, re-read the modified sections and verify:
1. Each finding is resolved
2. No new inconsistencies introduced
3. Theorem status tags match the actual proof status
4. All \ref and \label are valid
</verification_loop>

<completeness_contract>
Address EVERY finding listed. Do not stop at the first fix.
For each finding, state: FIXED (how) or CANNOT_FIX (why, what narrower claim survives).
</completeness_contract>

<structured_output_contract>
End with:
## Rectification Summary
- [FIXED] finding — what was done
- [NARROWED] finding — claim narrowed to X
- [CONDITIONAL] finding — marked conditional on Y
- [BLOCKED] finding — cannot fix because Z
</structured_output_contract>


TARGET: chapters/theory/higher_genus_modular_koszul.tex

This is the largest theory file. Multiple CRITICAL findings.

FINDINGS TO FIX:

1. [CRITICAL T06] Line ~2695: Theorem D circular dependency with thm:family-index.
   FIX: Add a routing remark (AP147) identifying the non-circular anchor.
   The proof chain should be: shadow tower construction (independent) → genus universality
   (from shadow tower) → family index identification (from universality). Make this explicit.

2. [CRITICAL T08] Lines ~994,1011: MC1 PBW — d_1^PBW maps enrichment classes to genus-0 sector
   without controlling mixed maps. Whitehead invoked for semisimple g but applied to truncated
   current algebra.
   FIX: Add the missing comparison between truncated current algebra and g. Whitehead applies
   to the finite-dimensional Lie algebra g acting on the weight graded pieces; make this precise.

3. [CRITICAL T09] Line ~3475: MC2 proved on g^mod only, not g^{E1}.
   Introduction.tex:368 wrongly attributes the E1 statement to thm:mc2-bar-intrinsic.
   FIX: Clarify that MC2 as stated here is on g^mod. The E1 version is in e1_modular_koszul.tex.
   Fix the introduction cross-reference.

4. [CRITICAL T09] Line ~3627: Theta_A placed in product of genuswise cyclic coderivations,
   then treated as element of Defcyc(A) ⊗ Gmod without identification.
   FIX: Add the explicit identification or restructure the proof to work in the genuswise product.

5. [CRITICAL T16] Line ~17115: Depth gap prop over-scoped. The kappa!=0 hypothesis excludes
   the d_alg=2 case (betagamma with kappa|_L=0).
   FIX: Split into kappa!=0 case ({0,1,inf}) and the kappa=0 boundary ({2}). Or remove the kappa!=0 hypothesis.

6. [CRITICAL T16] Line ~16414: Class-C witness contradicted. betagamma shadow tower vanishes
   on the weight-changing line. The claimed r_max=4 conflicts with proved mu_bg=0.
   FIX: Check which line/family actually realizes d_alg=2. If betagamma on the standard line,
   verify the shadow tower is nonzero there. Update the witness.

7. [CRITICAL T18] Lines ~30863,30882: D^2=0 proof uses wrong space. Log FM for fixed (X,D)
   has FM collisions and puncture collisions, not curve degenerations.
   FIX: The D^2=0 should work on the universal family over M-bar_{g,n}, not on log FM for fixed curve.
   Rewrite the space to be the correct one.

Read the file carefully (it's very large), verify each finding, fix in dependency order.
mcp startup: no servers



thinking
**Clarifying document edits**

I need to modify a specific file: chapters/theory/higher_genus_modular_koszul.tex. There’s also a mention of fixing the introduction cross-reference, but the action safety says to only edit the assigned file. The target lists only this file, but finding three explicitly requests the introduction fix. I’m contemplating whether I can address both at once or if I should only focus on the target file while adding notes. It’s a tricky situation, so I might need to seek clarification.
thinking
**Reconciling edits and instructions**

There's a conflict if the introduction states that the theorem proves the E1 statement. I can note "not E1" in the target file, but the introduction would still be incorrect. I might need to ask the user, but interpreting "specific file(s) assigned" could mean addressing both the target and the introduction. Since I need to balance system instructions with the user's requests, I should mention using skills like `beilinson-rectify` and `claim-surface-sync` for theorem repairs and status cleanups. An update for the user before significant edits is essential.
thinking
**Updating the plan**

I should consider updating the plan since this task is quite substantial. I’ll do a commentary update first, then explore necessary skills and required reads potentially using a parallel approach. Given the file is large, I might need tools like `rg` or `sed` with line numbers to inspect context lines effectively. Reading the required constitutional files might be enough, but using an explorer agent could be beneficial since developers recommend explorers for codebase inquiries.
codex
Using `beilinson-rectify` first, then `claim-surface-sync` if the theorem/status surface needs cleanup. I’m reading the required repo invariants and the exact theorem neighborhoods in `higher_genus_modular_koszul.tex` before touching any proof text.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
 succeeded in 51ms:
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

 succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

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
 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |

thinking
**Assessing file inspection needs**

I’m thinking about whether I need to inspect the entire target file or just relevant sections around specific line numbers. It could be enough to focus on critical files like introduction.tex and e1_modular_koszul.tex. I'll use rg to find theorem labels and their contexts. Since the mathematical edits are substantive, it might be best to read relevant sections rather than the whole file, especially to gather context for my edits. Let’s also locate those labels!
codex
I have the governing constraints loaded. Next I’m locating each theorem/proof surface and its upstream labels so the repairs can be made in dependency order instead of patching isolated lines.
exec
/bin/zsh -lc "rg -n \"thm:family-index|modular-characteristic|mc2-bar-intrinsic|Theta_A|Theta_\\\\cA|depth-gap|betagamma|r_max|D\\"'^2|log FM|universal family|FM|Whitehead|PBW|d_1'"\\"'^'"\\\\mathrm\\{PBW\\}|truncated current algebra|current algebra|mixed maps|genus universality|shadow tower|family index\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '900,1085p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2620,2755p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3440,3665p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17060,17180p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16340,16510p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30870,30940p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30810,30920p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '340,395p' chapters/frame/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:thm:family-index|modular-characteristic|mc2-bar-intrinsic|Theta_A|Theta_\cA|depth-gap|betagamma|r_max|D\^2|log FM|universal family|FM|Whitehead|PBW|d_1\^\mathrm\{PBW\}|truncated current algebra|current algebra|mixed maps|genus universality|shadow tower|family index)
                                                                               ^^
error: unrecognized escape sequence
 succeeded in 51ms:
Theorem~\ref{thm:pbw-allgenera-principal-w}).
For semisimple weightwise symmetry, the genus enrichment splits into
non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
invariant pieces killed by the family-specific $d_2$ transgression.
The affine KM Killing class shows that this is an $E_3$ statement, not
an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
radical cohomology of the weightwise Lie action.
Open: non-principal families; the $\mathcal{W}_\infty$
inverse-limit package
(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
\end{remark}

\begin{lemma}[Weightwise reduction of the genus enrichment to
 \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
\label{lem:pbw-weightwise-g-module}
\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
\index{truncated current algebra!mode bookkeeping only}
Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
\[
V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
 succeeded in 51ms:
 (Theorem~\ref{thm:genus-universality}).
\item The \emph{genus tower} $\{F_g(\cA)\}_{g \geq 1}$, the sequence
 of free energies determined by the bar complex at genus~$g$
 (Theorem~\ref{thm:universal-generating-function}).
\end{enumerate}
Both components are established. The Heisenberg specialization
appears in Chapter~\ref{ch:heisenberg-frame},
Definition~\ref{def:frame-modular-package}.

\smallskip
\emph{The spectral discriminant}
$\Delta_{\cA}(x) = \prod_i (1 - \lambda_i x)$
encodes bar cohomology dimensions
(Theorem~\ref{thm:ds-bar-gf-discriminant}).
It is a separate non-scalar invariant depending on
the full quadratic OPE data, not
on~$\kappa(\cA)$ alone.
\end{definition}

\begin{definition}[Full modular characteristic package]
 succeeded in 50ms:
Gaussian answer at every genus.
The four shadow-depth classes correspond to matrix-model
criticality: class~G is the Gaussian model (no potential
beyond quadratic), class~L is the cubic potential at
criticality, class~C is the quartic potential at criticality,
and class~M is the infinite potential off criticality
(complex conjugate branch points of~$Q_L$).
\end{proposition}

\begin{proof}
The scalar free energy $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$
is linear in~$\kappa$ by
Theorem~\ref{thm:genus-universality}. The GUE free energy
at matrix size~$N$ satisfies
$F_g^{\mathrm{GUE}} = N^2\cdot\lambda_g^{\mathrm{FP}}$ by the
Harer--Zagier recursion. The identification
$N^2 = \kappa(\cA)$ matches the two term by term.
The decomposition~\eqref{eq:ceo-plus-pf} is proved by
comparing the Eynard--Orantin residue formula on~$\Sigma_L$
(which captures the codimension-$1$ boundary strata
 succeeded in 51ms:
\node[font=\tiny, text=black!50] at (3,-0.2) {\textsf{infinite}};
%
% ---- Horizontal rule below headers ----
\draw[black!25] (-0.5,4.3) -- (3.5,4.3);
%
% ---- Complexity arrow ----
\draw[maparrow, black!40] (-0.45,-0.5) -- (3.45,-0.5);
\node[font=\tiny\scshape, text=black!50, anchor=north] at (1.5,-0.55)
 {increasing shadow complexity};
\end{tikzpicture}
\caption{The four shadow archetypes.
Each column shows the non-vanishing shadows at each degree
for the primitive representative of the class.
Class~$\mathbf{G}$ is purely scalar ($\kappa$ only);
class~$\mathbf{L}$ adds the Lie cubic shadow;
class~$\mathbf{C}$ has a quartic contact invariant
but no cubic;
class~$\mathbf{M}$ has all obstructions non-vanishing,
giving an infinite shadow obstruction tower.
All four classes are chirally Koszul; shadow depth
 succeeded in 51ms:
Classes $\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$: the
shadow obstruction tower terminates at degree $2$, $3$, $4$ respectively
(Theorem~\ref{thm:shadow-archetype-classification}), so
$S_r = 0$ for $r \geq r_{\max} + 1$, and the
shadow-formality identification gives
$\ell_r^{(0),\mathrm{tr}} = 0$ for
$r \geq r_{\max} + 1$. In particular,
$\ell_5^{(0),\mathrm{tr}} = \ell_6^{(0),\mathrm{tr}} = 0$
for all three classes.

For class $\mathbf{M}$:
$\Delta = 8\kappa S_4 = 40/(5c{+}22) > 0$ for $c > 0$,
so $Q_L$ is irreducible over $\mathbb{Q}(c)$ and the
convolution recursion produces $a_n \neq 0$ for all
$n \geq 1$
(Theorem~\ref{thm:single-line-dichotomy}). Hence
$S_5 \neq 0$ and $S_6 \neq 0$.

\emph{Part~(iv).}
At the scalar level, the scalar MC equation closes with the
 succeeded in 51ms:
$\Pi_X(L) = (\Fact_X(L),\, \barB_X(L),\,
\Theta_L,\, \cL_L,\,
(V^{\mathrm{br}}_L, T^{\mathrm{br}}_L),\,
\mathfrak{R}_4^{\mathrm{mod}}(L))$
\textup{(}Construction~\textup{\ref{constr:v1-platonic-package}}\textup{)}
is canonically recovered from the MC element $\Theta_\cA$
as follows:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\Fact_X(L)$: the factorization algebra is
 $U^{\mathrm{mod}}_X(L)$ itself, the domain of $\Theta_\cA$.
\item $\barB_X(L)$: the bar coalgebra is the coaugmented
 coalgebra on which $D_\cA = \dzero + \Theta_\cA$ acts.
\item $\Theta_L = \eta_{L,*}^{-1}(\Theta_\cA|_{\operatorname{Prim}})$:
 the universal MC class restricted to primitive currents
 \textup{(}Corollary~\textup{\ref{cor:envelope-universal-mc}}\textup{)}.
\item $\cL_L$: the Lagrangian datum from
 the complementarity polarization
 $\Defcyc(\cA) = L^+_\cA \oplus L^-_\cA$ restricted
 to $\Defcyc(L) \hookrightarrow \Defcyc(\cA)$.
\item $(V^{\mathrm{br}}_L, T^{\mathrm{br}}_L) =
 succeeded in 50ms:
 $\Convinf(\cA)$: their MC moduli coincide
 \textup{(}\S\textup{\ref{subsec:two-level-convention}}\textup{)}.
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{(i).}
This is exactly
Theorem~\ref{thm:convolution-formality-one-channel}.

\smallskip\noindent
\emph{(ii).}
The bar construction is defined for $Ch_\infty$-algebras
(Theorem~\ref{thm:cech-hca}); the resulting coalgebra
is strictly coassociative. The cobar construction
$\Omega$ produces a strict chiral algebra.
Bar-cobar inversion
(Theorem~\ref{thm:bar-cobar-inversion-qi}) gives
the quasi-isomorphism.

 exited 1 in 50ms:
sed: chapters/frame/introduction.tex: No such file or directory


thinking
**Searching for file path**

I need to locate the introduction file path. At first, I think using "rg --files" is a good approach. Maybe I should also try searching with a simpler escaped pattern to make it easier. It feels like keeping things straightforward might help me find what I’m looking for more efficiently. Let's see how this plays out!
thinking
**Considering the tools to use**

I might think about using the explorer, but it seems like that may not be necessary after all. I could also use exec_command instead. I need to inspect labels and maybe check the e1 file along with the family index. Let's simplify the search and look for other files with rg as well. It sounds like I should also locate the introduction file. Let's get on that!
codex
I’ve isolated the first proof lane. The PBW repair already has partial supporting lemmas in place, so I’m now checking whether they actually close the mixed-map gap and then tracing the remaining labels for Theorem D, MC2 scope, depth-gap, and the universal-family argument.
exec
/bin/zsh -lc "rg -n 'thm:family-index|thm:genus-universality|thm:modular-characteristic|thm:mc2-bar-intrinsic|thm:e1-mc-element|thm:master-theta|thm:depth-gap|depth gap|d_alg|betagamma|r_max|mu_bg|D\\\\"'^2|universal family|log FM|fixed curve|overline'"\\\\{\\\\mathcal\\\\{M\\\\}_\\{g,n\\\\}|Theta_\\\\cA|Defcyc|cyclic coderiv' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17100,17155p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2660,2715p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16390,16470p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3455,3645p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg 'introduction\\\\.tex"'$|guide_to_main_results'"\\\\.tex"'$|frame.*introduction|introduction'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30840,30905p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:thm:family-index|thm:genus-universality|thm:modular-characteristic|thm:mc2-bar-intrinsic|thm:e1-mc-element|thm:master-theta|thm:depth-gap|depth gap|d_alg|betagamma|r_max|mu_bg|D\\^2|universal family|log FM|fixed curve|overline\\{\\mathcal\\{M\\}_\{g,n\\}|Theta_\\cA|Defcyc|cyclic coderiv)
                                                                                                                                                                                                                                            ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
is an automorphism of~$\gAmod$ respecting the weight
filtration, it bijects the obstruction classes:
$o_r(\cA) = 0$ if and only if $o_r(\cA^!) = 0$.
Hence $r_{\max}(\cA) = r_{\max}(\cA^!)$.
\end{proof}

\begin{remark}[Shadow depth refines GKW formality]
\label{rem:shadow-depth-gkw-refinement}
\index{GKW formality!shadow depth refinement}
\index{Gaiotto--Kulp--Wu|see{GKW formality}}
\index{shadow depth!GKW refinement}
The $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
is a strict four-class refinement of the binary formal/non-formal
dichotomy of Gaiotto--Kulp--Wu~\cite{GKW2025}.
In their framework, a theory with topological direction
$d' \geq 2$ is formal (all higher operations vanish),
while $d' = 1$ theories are generically non-formal.
The shadow depth resolves the $d' = 1$ non-formal class
into three distinct strata:
\begin{enumerate}[label=\textup{(\roman*)}]
 succeeded in 51ms:
 \[
 \Theta_{\cA} \in
 \operatorname{MC}\!\bigl(
 \Defcyc(\cA) \;\widehat{\otimes}\;
 R\Gamma(\overline{\mathcal{M}}_{g,\bullet},\, \mathbb{Q})
 \bigr);
 \]
\item $\kappa(\cA) \in \mathbb{C}$ is the
 \emph{scalar modular characteristic}
 (Definition~\ref{def:scalar-modular-package}),
 the first characteristic number of~$\Theta_{\cA}$
 under the trace map
 $\Defcyc(\cA) \to \mathbb{C}$;
\item $\Delta_{\cA}(x) = \prod_{i}(1 - \lambda_i x)$ is the
 \emph{spectral discriminant}
 (Theorem~\ref{thm:ds-bar-gf-discriminant});
\item $\Pi_{\cA} = (M_{\cA}, Q_{\cA}, G_{\cA})$ is the
 \emph{periodicity profile}
 (Remark~\ref{rem:periodicity-triple});
\item $\mathcal{H}_{\cA} := \{C_g(\cA)\}_{g \geq 0}$ is the
 succeeded in 51ms:
introduction_full_survey.pdf
wave2_audit_20260413_001942/H20_introduction.md
wave2_audit_20260413_001942/G30_introduction.md
wave2_audit_20260413_001942/I06_introduction.md
wave2_audit_20260413_001942/C02_introduction.md
elite_rescue_20260413_141402/H09_heal_introduction_preface.md
chapters/connections/thqg_introduction_supplement_body.tex
chapters/connections/thqg_introduction_supplement.tex
rectification_20260412_233715/R13_introduction.md
chapters/theory/introduction.tex
relaunch_20260413_111534/R13_introduction.md
fix_wave_A_20260413_112727/A04_introduction.md
standalone/introduction_full_survey.pdf
standalone/introduction_full_survey.tex
platonic_rectification_20260413_114523/P18_introduction_upgrade.md
mega_rescue_20260413_141327/M54_v3_introduction.md
compute/audit/preface_introduction_plan.md
 succeeded in 51ms:
\[
 t_\pm
 \;=\;
 \frac{-6\kappa\alpha
 \pm 2\kappa\,i\sqrt{2\Delta}}
 {9\alpha^2 + 2\Delta}
\]
are a \emph{complex conjugate pair} (they are real only
when $\Delta \leq 0$, which forces class~$\mathbf{G}$
or~$\mathbf{L}$). The branch points of $\sqrt{Q_L}$
at $t = t_\pm$ control the Taylor coefficients via the
standard formula
\begin{equation}\label{eq:branch-point-asymptotics}
 a_n
 \;\sim\;
 A \cdot |t_0|^{-n} \cdot n^{-3/2}
 \cos(n\,\theta + \varphi),
 \qquad n \to \infty,
\end{equation}
where $t_0 = t_+$ is the branch point, $|t_0|$ is its
 succeeded in 51ms:
\emph{(iv).}
The two-level convention
(\S\ref{subsec:two-level-convention}) establishes that
$\Convstr(\cA)$ is a strict model:
the inclusion $\Convstr \hookrightarrow \Convinf$ is a
quasi-isomorphism of $L_\infty$-algebras, hence
induces a bijection on MC moduli.
Representability by $\Defcyc^{\mathrm{mod}}(\cA)$
is the definition of the modular convolution algebra
(Definition~\ref{def:modular-convolution-dg-lie}).
\end{proof}

%%-------------------------------------------------------------
%% 6. The modular Koszul datum as universal structure
%%-------------------------------------------------------------

\subsubsection{The modular Koszul datum and the modular envelope}

\begin{theorem}[Recovery of the modular Koszul datum from
$\Theta_\cA$]
 succeeded in 51ms:
Harer--Zagier recursion. The identification
$N^2 = \kappa(\cA)$ matches the two term by term.
The decomposition~\eqref{eq:ceo-plus-pf} is proved by
comparing the Eynard--Orantin residue formula on~$\Sigma_L$
(which captures the codimension-$1$ boundary strata
of~$\overline{\mathcal{M}}_g$) with the full bar-complex
graph sum (which includes the planted-forest strata
at codimension~$\geq 2$). At genus~$2$, the four
codimension-$1$ graphs contribute~$F_2^{\mathrm{CEO}}$ and
the three planted-forest graphs contribute~$\delta_{\mathrm{pf}}^{(2,0)}
= S_3(10S_3-\kappa)/48$; the sum equals
$\kappa\cdot 7/5760$.
\end{proof}

\begin{remark}[Two projections of the universal MC element]
\label{rem:two-projections-theta}
\index{Maurer--Cartan element!two projections}
The genus-$g$ free energy~$F_g$ and the degree-$r$ shadow
coefficient~$S_r$ are two projections of the single MC
element~$\Theta_\cA \in \MC(\gAmod)$:
exec
/bin/zsh -lc "rg -n 'mc2-bar-intrinsic|e1-mc-element' ." in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
./compute/lib/nishinaka_envelope.py:46:    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/nishinaka_envelope.py:320:    The bar-intrinsic construction (thm:mc2-bar-intrinsic):
./compute/lib/nishinaka_envelope.py:331:    at all levels (thm:mc2-bar-intrinsic).
./compute/lib/theorem_dg_shifted_yangian_bridge_engine.py:565:    MK MC equation (thm:mc2-bar-intrinsic):
./compute/lib/shifted_symplectic_dag_engine.py:251:    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/shadow_obstruction_atlas.py:7:of the bar-intrinsic MC element Theta_A := D_A - d_0 (thm:mc2-bar-intrinsic).
./compute/lib/shadow_obstruction_atlas.py:43:    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/theorem_virasoro_constraints_mc_engine.py:8:in the modular convolution algebra g^mod_A (thm:mc2-bar-intrinsic),
./compute/lib/theorem_virasoro_constraints_mc_engine.py:88:    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/chern_simons_barcobar.py:58:- thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/string_field_theory_engine.py:64:  - thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/theorem_costello_genus3_amplitudes_engine.py:97:    higher_genus_modular_koszul.tex: thm:mc2-bar-intrinsic, thm:theorem-d.
./compute/lib/genus2_siegel_shadow.py:596:    where Theta_A is the universal MC element (thm:mc2-bar-intrinsic).
./compute/lib/theorem_bootstrap_koszul_engine.py:55:    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/theorem_bootstrap_koszul_engine.py:1331:    (b) follows from the MC recursion (thm:mc2-bar-intrinsic):
./compute/lib/theorem_bootstrap_koszul_engine.py:1351:                'proof': 'thm:mc2-bar-intrinsic: Theta := D_A - d_0 is MC',
./compute/lib/theorem_bootstrap_koszul_engine.py:1352:                'manuscript_ref': 'thm:mc2-bar-intrinsic',
./compute/lib/shadow_gv_integrality_engine.py:68:    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/bc_nc_motives_shadow_engine.py:67:  thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)
./compute/lib/shadow_hierarchy_engine.py:108:    thm:mc2-bar-intrinsic (higher_genus_modular_koszul.tex)


thinking
**Inspecting and refining outputs**

I need to target my searches better since the output is huge. I'll use simpler regular expressions with fixed strings to find specifics in the target file. I see the introduction looks like it has been edited already, so I’ll check line 368 to confirm that. If the introduction is fixed, I won't make changes there. I also need to locate specific theorem labels and verify their contexts to ensure everything is accurate. It seems I’ll need to be careful with the edits I make.
thinking
**Refining the inspection process**

I need to dig deeper than line 1085 and maybe check the theorem around line 1011 for more context. It’s important to look at the line numbers to see if the current file includes any of these fixes, even if partially. I also need to identify any remaining gaps in the work. Gathering precise theorem labels will be crucial too, so I'll use fixed strings with rg to help me locate everything accurately.
exec
/bin/zsh -lc "rg -n -F 'thm:family-index' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2917:Theorem~\ref{thm:family-index} is downstream again: it is the
2931:Theorem~\ref{thm:family-index}.
3008:virtual bar family. Theorem~\ref{thm:family-index} is therefore the
3024:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
4774: \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
4822:(Theorem~\ref{thm:family-index}) of the scalar series already
9873:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
14322:(Theorem~\ref{thm:family-index}).
exec
/bin/zsh -lc "rg -n -F 'thm:modular-characteristic' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:genus-universality' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'd_alg' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'beta\\gamma' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:mc2-bar-intrinsic' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'D"'^2=0'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'log Fulton' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'mu_{\\beta\\gamma}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2620: (Theorem~\ref{thm:genus-universality}).
2727:(Theorem~\ref{thm:genus-universality}).
2914:scalar trace. Theorem~\ref{thm:genus-universality} is the first
2930:and Theorem~\ref{thm:genus-universality} does not invoke
2932:Part~(i) is Theorem~\ref{thm:genus-universality} for
2940:Theorem~\ref{thm:genus-universality}(ii).
3006:Theorem~\ref{thm:genus-universality}; the second is the downstream
3014:Theorem~\ref{thm:genus-universality}); generating function via
3035:Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
3452:Theorem~\ref{thm:genus-universality}. The GUE free energy
3616:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
4047:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
4099:Theorem~\ref{thm:genus-universality}(ii)).
4772: Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
5751:(Theorem~\ref{thm:genus-universality},
8152:(Theorem~\ref{thm:genus-universality}).
8308:Theorem~\ref{thm:genus-universality} identifies the scalar trace
8456:Theorem~\ref{thm:genus-universality} identifies
8880:by Theorem~\ref{thm:genus-universality}\textup{(iii)}.
 exited 1 in 52ms:

 succeeded in 51ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
2350: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2648:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2705:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2802:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2913:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3614:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3630:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3770:\label{thm:mc2-bar-intrinsic}
3832:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
3840:Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
4106:Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
4161:Theorem~\ref{thm:mc2-bar-intrinsic}.
4244:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4294:Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
4348:exists at all genera by Theorem~\ref{thm:mc2-bar-intrinsic},
4846:(Theorem~\ref{thm:mc2-bar-intrinsic};
5283:assembly in Theorem~\ref{thm:mc2-bar-intrinsic}. Consequently the
 succeeded in 52ms:
411:$\cW$-algebras, Theorem~\ref{thm:modular-characteristic}(iii))
1620:(Theorem~\ref{thm:modular-characteristic}).
1770:(Theorem~\ref{thm:modular-characteristic}).
1831:(Theorem~\ref{thm:modular-characteristic}).
2813:(1)~scalar: $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic}),
2844:\label{thm:modular-characteristic}
3183:Theorem~\ref{thm:modular-characteristic}(ii) is the exact
3193:Theorem~\ref{thm:modular-characteristic}(iv) is the
3207:consequence of Theorem~\ref{thm:modular-characteristic} and
3216:term-by-term from Theorem~\ref{thm:modular-characteristic}.
3290:(Theorem~\ref{thm:modular-characteristic}, applied to the
3325:Theorem~\ref{thm:modular-characteristic}(iii). At $N = 2$
3362:Theorem~\ref{thm:modular-characteristic}(iv), applied to the
4098:(Theorem~\ref{thm:modular-characteristic}(iii),
4927:(Theorem~\ref{thm:modular-characteristic}(iii)) for KM, and from
5000:(i)~the scalar shadow $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic});
5509:(\textup{Theorem~\ref{thm:modular-characteristic}}).
8158:(Theorem~\ref{thm:modular-characteristic}(iii);
10116:(Theorem~\ref{thm:modular-characteristic}): a single number
21026:(Theorem~\ref{thm:modular-characteristic}(iv)) gives the result.
 succeeded in 51ms:
701:\item the free fermion algebra $\mathcal{F}$ and the $\beta\gamma$-$bc$
2207:The $\beta\gamma$-$bc$ system at non-integer spin
2210:$\beta\gamma$ ghost with $\lambda = 0$ or $1$\textup{)},
2480:\textup{(}the entire standard landscape except integer-spin $\beta\gamma$, where hypothesis~\textup{(a)} fails\textup{)},
2723:($\mathcal{W}_N$ for $N \geq 3$, $\beta\gamma$) do not.
3225:$\beta\gamma$/$bc$, and $K3 \times E$). The universality
3331:\begin{remark}[$\beta\gamma$ and $bc$: ghost slabs]
3333:\index{beta-gamma system@$\beta\gamma$ system!Brown--Henneaux}%
3335:For the $\beta\gamma$ system of conformal weight~$\lambda$,
3336:$\kappa(\beta\gamma) = c_{\beta\gamma}/2
3340:$\kappa_{\mathrm{tot}}(\beta\gamma\,{\otimes}\,bc) = 0$
3346:$\beta\gamma$-$bc$ slab is Koszul self-dual with
3567:The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
4276:at~$3$, $\beta\gamma$ at~$4$; Virasoro at~$\infty$),
12363:$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
12436: {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
12753:($\beta\gamma$); the Virasoro tower is infinite.
13839:$\beta\gamma$ & $\checkmark$ & gauge-trivial & $\checkmark$ (quartic) \\
13844:For the $\beta\gamma$ system, the cubic contribution is gauge-trivial
13849:$\mu_{\beta\gamma} = 0$
 succeeded in 51ms:
11568:$d_{\mathrm{pf}}$. The identity $D^2=0$ is the cancellation of
11758:Expand $D^2=0$ by weight using $D=D_{\mathrm{loc}}+\Theta_\cA$.
 succeeded in 51ms:
31880:external package}: Mok's relative log Fulton--MacPherson
 succeeded in 51ms:
13849:$\mu_{\beta\gamma} = 0$
16969:$\mu_{\beta\gamma} = 0$ by rank-one abelian rigidity
17719:all shadows vanish and $\mu_{\beta\gamma} = 0$ by rank-one abelian

thinking
**Inspecting neighborhood theorems**

I need to take a closer look at specific neighborhoods surrounding theorems D and MC2, particularly focusing on locations like 3770 and 2844. Additionally, I’ll evaluate the depth gap statements around 16950 and 17700, as well as the D^2 proof around 31880. It seems like I have a clear direction for my investigation, so let’s dive into these targeted contexts! I want to make sure I don’t miss anything important.
codex
The theorem labels are pinned down now. I’m reading the exact statements at `thm:modular-characteristic`, `thm:mc2-bar-intrinsic`, the depth-gap lane, and the `D^2=0` argument so I can decide whether to strengthen, split, or narrow each claim without collateral edits.
exec
/bin/zsh -lc "sed -n '358,382p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '31840,31935p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17690,17755p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16890,17020p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1075,1145p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '980,1075p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2828,3048p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3760,3855p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
on the standard CFT-type landscape except integer-spin $\beta\gamma$.
Once both sides are present, Theorem~C forces the Verdier decomposition
$\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$ of the ambient complex;
the Lagrangian splitting is proved, while the ambient
shifted-symplectic upgrade remains conditional on perfectness and
nondegeneracy. Tracing the same object yields Theorem~D: on the
uniform-weight modular Koszul lane,
$\mathrm{obs}_g(\cA) = \kappa(\cA)\lambda_g$ at all genera and the free
energies are the $\hat A$-series; at genus~$1$ this scalar statement is
unconditional for every family, while at genus $g \ge 2$ multi-weight
algebras acquire the explicit cross-channel term
$\delta F_g^{\mathrm{cross}}$. Theorem~H identifies the coefficient
ring of the same universal class: on the Koszul locus,
$\ChirHoch^n(\cA) = 0$ for $n \notin \{0,1,2\}$ and
\[
P_\cA(t)
=
\dim Z(\cA)
+ \dim \ChirHoch^1(\cA)\, t
+ \dim Z(\cA^!)\, t^2.
 succeeded in 51ms:
so the finite-depth locus at degree~$4$ is exactly the cancellation
$S_4 = 0$. This is the Jacobi locus of the affine class. Once that
cancellation fails, the next recursion step forces a tail. Indeed,
the master equation~\eqref{eq:single-line-inversion} at $r = 5$
gives
\[
 S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
 = -(6/5)\,P\,\alpha\,S_4.
\]
For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
$S_5 = 0$ but the next step gives
\[
 S_6
 \;=\;
 -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
 \;=\;
 -\frac{2\,S_4^2}{3\kappa},
\]
which is again nonzero. Thus there is no second finite
 succeeded in 50ms:
\emph{regular} at every collision divisor~$D_{ij}$
(they arise from the non-trivial $H^1$ of the elliptic curve,
not from OPE poles). Since $d_0^{\mathrm{PBW}}$ acts by
Poincar\'{e} residue at collision divisors, and the
Poincar\'{e} residue of a regular form is zero, every
such enrichment cochain is automatically $d_0^{\mathrm{PBW}}$-closed.
The enrichment cochains are not
$d_0^{\mathrm{PBW}}$-exact (they cannot be in the image
of the commutative bar differential from higher bar degree,
since the enrichment at higher degree is likewise
regular and $d_0^{\mathrm{PBW}}$-closed).

Hence the $E_1$ page decomposes:
\begin{equation}\label{eq:e1-decomposition-genus1}
E_1^{p,q}(g{=}1) \;=\; E_1^{p,q}(g{=}0)
 \;\oplus\; \mathcal{E}^{p,q}_1
\end{equation}
where $E_1(g{=}0)$ is the concentrated genus-$0$
part (Theorem~\ref{thm:km-chiral-koszul}) and
$\mathcal{E}^{p,q}_1$ is the enrichment from
 succeeded in 50ms:
$\{\overline{\mathcal{M}}_{g,n}\}_{g,n}$, the genus tower
assembles into a chain-level modular functor
(Theorem~\ref{thm:chain-modular-functor}): to each surface~$\Sigma_{g,n}$ a
cochain complex $V_{g,n} = \barB^{(g)}_n(\cA)$, to each boundary
degeneration a chain map, to each consistency relation a chain
homotopy. Passing to cohomology recovers the classical
modular-functor package; for $\widehat{\fg}_k$ at integrable level, $H^0(V_{g,n})$ is the
Tsuchiya--Ueno--Yamada space of conformal blocks
(Remark~\ref{rem:chain-vs-classical-mf}). The degree-$2$ projection
of $\Theta_\cA$ is the scalar $\kappa(\cA)$ that controls the
entire genus tower (the spectral discriminant~$\Delta_\cA$,
periodicity profile~$\Pi_\cA$, and full MC
class~$\Theta_\cA$ require data beyond~$\kappa$;
see Definition~\ref{def:full-modular-package}).

\begin{theorem}[Modular characteristic; \ClaimStatusProvedHere]
\label{thm:modular-characteristic}
\index{modular characteristic theorem|textbf}
\index{kappa@$\kappa$!as first characteristic number|textbf}
\textup{[}Regime: curved-central
 succeeded in 51ms:
$d_{\mathrm{alg}} = 1$, $r_{\max} = 3$\textup{)}:}
 Affine Kac--Moody $V_k(\fg)$ at generic level.
 The cubic shadow $\mathfrak{C}_{\mathrm{aff}}(x,y,z) =
 \kappa(x,[y,z])$ is the unique non-vanishing higher shadow; the
 quartic obstruction $o_4 = 0$ by the Jacobi identity.

\item \emph{Contact \textup{(}$\mathbf{C}$,
$d_{\mathrm{alg}} = 2$, $r_{\max} = 4$\textup{)}:}
 the conformal-weight family $\beta\gamma_\lambda$
 \textup{(}and its $bc$ dual\textup{)}.
 The class-$\mathbf{C}$ witness is not the weight-changing line and
 not the $T$-line: on the full family one has
 \[
  S_2 = 6\lambda^2 - 6\lambda + 1,\qquad
  S_3 = 0,\qquad
  S_4 = -5/12,\qquad
  S_r = 0 \quad (r \geq 5).
 \]
 Thus the charged quartic contact class is nonzero and is the last
 non-vanishing shadow component; the quintic obstruction vanishes by
 succeeded in 50ms:
$\fg$-equivariant maps
\[
\mathcal{E}_g^{n,h}
\xrightarrow{\ \iota_{g,h,n}\ }
C^1(\fg, N_h^{n-1})
\xrightarrow{\ q\ }
H^1(\fg, N_h^{n-1})
\xrightarrow{\ \beta_{g,h,n}\ }
E_2^{n-1,h}(g{=}0)
\]
with the following property: if
$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
the non-semisimple truncated current algebra $\fg \otimes V_h$.
\end{lemma}

 succeeded in 51ms:
+ \partial_{\mathrm{deg}}^{\,2}.
\]
Step~2 identifies the first term with the unconditional equality
$d_B^{\,2}=0$. Step~3 identifies the degeneration square with the
Hodge-class curvature $\kappa(\cA)\cdot\omega_g$. The mixed term is
the codimension-$2$ locus where a collision stratum meets a
curve-degeneration stratum; after transport through the Hom functor
it is exactly the ambient cross-term correction that absorbs this
fiberwise curvature when one passes from the curved operator
$\dfib$ to the strict total differential $D_{\cA}$. In particular,
\[
 [d_{\mathrm{sew}}, d_{\mathrm{pf}}]
 + [d_{\mathrm{int}}, \hbar\Delta]
 + [[\tau_{\cA},-], d_{\mathrm{sew}} + d_{\mathrm{pf}}]
 = 0
\]
is the algebraic form of that mixed codimension-$2$ cancellation.
Combining the three pieces yields $D_{\cA}^2 = 0$ on the ambient
algebra.

 succeeded in 51ms:
$\Theta_\cA$: the modular characteristic $\kappa$ at degree~$2$,
the cubic shadow $\mathfrak{C}$ at degree~$3$, the quartic
resonance $\mathfrak{Q}$ at degree~$4$, and all higher
obstructions in the Postnikov tower of
Definition~\ref{def:shadow-postnikov-tower}.
There is no separate construction for each invariant; there is
$\Theta_\cA$, and the invariants are what remain after
forgetting all but finitely many degrees.

\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
\label{thm:mc2-bar-intrinsic}
\index{universal Maurer--Cartan class!bar-intrinsic construction}
\index{MC2!bar-intrinsic proof}
\index{MC2!full generality}
Let $\cA$ be a modular Koszul chiral algebra on a smooth
projective curve~$X$ with non-degenerate invariant form.
Write
$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
for the genus-completed bar differential
\textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},

thinking
**Inspecting further steps**

I think I need to continue from 1145 for a bit, but step 2 is still ongoing. I wonder if I should delve deeper into the theorem that likely uses mixed-factorization. It might enrich my understanding. I'll check this out carefully, breaking down the various components to see how they fit in together. That could help illuminate some of the complexities I'm dealing with!
exec
/bin/zsh -lc "sed -n '1145,1205p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\qquad
M_h := \bigoplus_\nu M_{h,\nu}.
\]
The mixed component is the degree-one part of the same diagonal
$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
is carried out weight by weight on honest $\fg$-modules, not on the
non-semisimple Lie algebra $\fg \otimes V_h$. The relevant
comparison is therefore representation-theoretic rather than
Lie-algebraic: once the mode pattern is fixed, the residue action is
the diagonal adjoint $\fg$-action with multiplicity spaces coming
from the modes.

\medskip
\emph{Step~3: Acyclicity of the enrichment complex.}

We show $H^*(\mathcal{E}_1^{*,h},\, d_1^{\mathrm{PBW}}) = 0$
in each conformal weight~$h$, by a representation-theoretic
argument for~$\fg$ semisimple.
exec
/bin/zsh -lc "sed -n '1205,1255p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\otimes \alpha$ for
$\alpha \in H^1(E_\tau)$. The $d_2^{\mathrm{PBW}}$
differential maps the bar-degree-$3$ element
$J^c_{-1} \otimes \kappa^{ab} J^a_{-1} \otimes J^b_{-1}$
(with appropriate form data) to
$k \cdot \dim(\fg) \cdot J^c_{-1} \otimes \alpha$ via the
$(1)$-product contraction. At generic $k \neq 0$,
this is non-zero, so the invariant class is killed
at~$E_3$.

By bounded-below convergence
(\ref{item:pbw-bounded} of
Theorem~\ref{thm:pbw-koszulness-criterion}), the
spectral sequence converges in each bidegree, and
all enrichment classes are killed by $d_r$ for
some finite~$r$. In each fixed conformal weight~$h$,
only finitely many pages are non-trivial (since the
chain groups are finite-dimensional), so the spectral
sequence stabilizes.




thinking
**Evaluating repair findings**

It seems the PBW repair might already be fixed, but I need to verify if it mentions lines 994 and 1011. The inserted lemmas and proof seem to address the issue, so perhaps no edits are necessary there. However, I might still want to mention "Whitehead's theorem not on truncated current algebra." The user requested fixes for each finding, so I should check if they were already corrected and determine if a final summary should note they are already fixed.
thinking
**Reviewing routing remarks**

It looks like T06 already has a routing remark, and T09's MC2 scope includes a remark with a theorem statement that clarifies things. T16’s class-C witness also seems fixed, suggesting some findings may be pre-fixed. However, if the user requests fixes and the file already contains some, I need to verify if no action is required. There might still be subtle issues, so I’ll check if any lines remain problematic, like the introduction cross-reference which could be verified. I'll inspect more lines.
thinking
**Inspecting current state**

I think I need to take a closer look at the introduction to see what the current state is. Maybe I've already addressed the issues, but it wouldn't hurt to read through it a bit more to be sure. I want to catch anything that might be overlooked and make sure I'm on the right track. Let’s see what I discover as I review this section further!
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '364,380p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   364	uniform-weight modular Koszul lane,
   365	$\mathrm{obs}_g(\cA) = \kappa(\cA)\lambda_g$ at all genera and the free
   366	energies are the $\hat A$-series; at genus~$1$ this scalar statement is
   367	unconditional for every family, while at genus $g \ge 2$ multi-weight
   368	algebras acquire the explicit cross-channel term
   369	$\delta F_g^{\mathrm{cross}}$. Theorem~H identifies the coefficient
   370	ring of the same universal class: on the Koszul locus,
   371	$\ChirHoch^n(\cA) = 0$ for $n \notin \{0,1,2\}$ and
   372	\[
   373	P_\cA(t)
   374	=
   375	\dim Z(\cA)
   376	+ \dim \ChirHoch^1(\cA)\, t
   377	+ \dim Z(\cA^!)\, t^2.
   378	\]
   379	For Heisenberg this gives $P(t) = 1+t+t^2$; for generic Virasoro and
   380	principal $\mathcal{W}$-algebras it gives $P(t) = 1+t^2$; for generic
exec
/bin/zsh -lc "sed -n '3855,3945p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 font=\footnotesize] (DA) at (0,2)
 {$D_\cA = \displaystyle\sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$};
%
% ---- Decomposition ----
\draw[maparrow, very thick] (0,1.2) -- (0,0.5);
\node[font=\scriptsize, anchor=west] at (0.15,0.85) {$=$};
%
% ---- d_0 + Theta ----
\node[draw, thick, rounded corners=3pt,
 minimum width=1.8cm, minimum height=0.7cm,
 font=\footnotesize] (d0) at (-1.5,-0.3)
 {$d_0 = d_\cA^{(0)}$};
\node[font=\normalsize] at (0,-0.3) {$+$};
\node[draw, very thick, rounded corners=3pt,
 minimum width=2.5cm, minimum height=0.7cm,
 fill=black!5, font=\footnotesize] (Theta) at (1.8,-0.3)
 {$\Theta_\cA = \displaystyle\sum_{g \geq 1}
 \hbar^g d_\cA^{(g)}$};
%
% ---- Implication arrow ----
exec
/bin/zsh -lc "sed -n '3945,4050p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 type~$(g,n)$ given by iterated edge contraction against
 the propagator~$P_\cA$.
\item \emph{$D_\cA^2 = 0$.}
 This is Theorem~\ref{thm:bar-modular-operad}(iii), itself
 proved via Theorem~\ref{thm:prism-higher-genus}:
 the bar differential satisfies $d_{\mathrm{full}}^2 = 0$
 because each codimension-$2$ boundary stratum of
 $\overline{\cM}_{g,n}$ appears with opposite signs from
 the two codimension-$1$ strata containing it
 (Lemma~\ref{lem:stable-graph-d-squared}).
 At the convolution-algebra level, this translates to
 $D^2 = 0$ on $\gAmod$
 (Theorem~\ref{thm:convolution-d-squared-zero}).
\item \emph{Brackets well-defined.}
 The graded commutator $[-,-]$ in the coderivation algebra
 is the convolution Lie bracket of
 Construction~\ref{const:explicit-convolution-bracket},
 which is well-defined on the completed modular convolution
 algebra $\gAmod$
 (Definition~\ref{def:modular-convolution-dg-lie}).

thinking
**Reviewing identification issues**

I'm focusing on how the proof handles identification. It seems good, but I need to inspect line 17115, possibly regarding the proposition label and statement. I should search around line 17080 for the term "depth gap trichotomy" as well. There might be a chance that the claim is still overscoped, so I’m considering using regular expressions to find the right label. Let's dive in and clarify these details!
exec
/bin/zsh -lc "rg -n -F 'prop:depth-gap-trichotomy' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
146: No other depths occur (Proposition~\ref{prop:depth-gap-trichotomy}):
17609:\label{prop:depth-gap-trichotomy}
17806:Proposition~\ref{prop:depth-gap-trichotomy} detects the same
exec
/bin/zsh -lc "sed -n '17585,17695p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
characteristic equation is~$\Sigma_L$.
\end{corollary}

\begin{proof}
$(2\kappa + 3\alpha t)^2 = 4\kappa^2 + 12\kappa\alpha\,t
+ 9\alpha^2 t^2$. Adding $2\Delta\,t^2 = 16\kappa S_4\,t^2$
gives $Q_L(t)$.
\end{proof}

The Gaussian decomposition reduces the entire shadow tower to a
single algebraic question: is $Q_L(t)$ a perfect square in
$k(c)[t]$? Because $Q_L$ is quadratic in~$t$, the answer is
governed by a classical dichotomy. A quadratic polynomial is a
perfect square if and only if its discriminant vanishes; when it
does, $\sqrt{Q_L}$ is linear and the tower terminates after
finitely many terms; when it does not, $\sqrt{Q_L}$ is
irrational over the polynomial ring and the binomial series for
$(1+u)^{1/2}$ produces infinitely many nonzero shadow
coefficients. There is no third possibility. The depth of the
shadow tower is not a free parameter: it is \emph{read off} from
exec
/bin/zsh -lc "sed -n '16250,16455p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $C_5 = 42$ binary trees with $6$ leaves
 \textup{(}Feynman transform route\textup{)}, or via
 $(2 \cdot 6 - 5)!! = 105$ trivalent trees with $6$
 legs \textup{(}stable-graph route\textup{)}.

\item \emph{Sextic bracket and obstruction class.}
 Similarly,
 \begin{equation}\label{eq:ell6-explicit}
 \ell_6^{(0),\mathrm{tr}}
 (\Theta^{\leq 5}, \dotsc, \Theta^{\leq 5})
 \;=\; S_6 \cdot e_6,
 \end{equation}
 where the MC equation at degree~$6$ absorbs $S_6$
 into the obstruction class $o_6(\cA)$. The three
 routes count $C_5 = 42$ planar trees with $6$ leaves,
 $C_6 = 132$ binary trees with $7$ leaves, and
 $(2 \cdot 7 - 5)!! = 945$ trivalent trees with $7$
 legs, respectively.

\item \emph{Vanishing and non-vanishing.}

thinking
**Inspecting proof details**

It looks like I need to inspect the D^2 proof around the lines 30863 and 30882. I'll search for the label, maybe "thm ambient-d-squared-zero." It’s likely I’ll need to read through the whole proof just to be sure—could be wrong. Checking the target lines around 30840 might also help clarify things. Let’s see how this all connects together.
exec
/bin/zsh -lc "sed -n '30770,31895p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Assume the full universal Maurer--Cartan element is scalar:
 \[
 \Theta_\cA
 \;=\;
 \kappa(\cA)\cdot \eta \otimes \Lambda.
 \]
 Then the distinguished scalar Maurer--Cartan orbit in
 $\Convinf(\cA)$ is formal: the higher transferred brackets
 vanish on the scalar line
 $\mathbb{C}\!\cdot\!\eta\otimes\Lambda$, and the MC equation
 restricts there to the scalar genus identities.
 No converse is proved here. In particular, one-channel
 minimal-model concentration
 $\Theta_\cA^{\min}=\eta\otimes\Gamma_\cA$ does not by itself
 imply scalar saturation, nor does it identify the full MC moduli
 with an affine line.
\item \emph{Homotopy chiral rectification.}
 A homotopy chiral algebra $\cA^{Ch_\infty}$
 rectifies to a strict chiral algebra~$\cA$
 via bar-cobar:



thinking
**Verifying file edits**

I’m checking to see if the introduction cross-reference is already fixed, and it looks like it is! Since the user only asked for edits to a specific file, I might not need to change anything if all remaining issues are fixed. However, it seems there could still be subtle edits needed. I’ll look into whether remarks about theorem D are present. If this file already includes previous changes, I should still verify for any lingering references or statements that need fixing.
thinking
**Inspecting unresolved findings**

I think some findings might still need adjustments. First, I’ll look into finding 2, which involves PBW mixed maps, and it seems alright. I need to check if theorem 1011 is still using "Whitehead on semisimple g" as applied to the truncated current algebra, but it now states otherwise, which is great. As for finding 1, the circular reference for Theorem D shows a good routing remark and proof. I'll check finding 3 about the introduction cross-reference too. If everything’s already addressed, I’ll verify that the user asked for fixes specific to this file.
thinking
**Verifying findings and edits**

Finding 6 about the class-C witness has been contradicted and fixed. Finding 7 regarding the D² proof's space issue is also corrected. It seems like the file may already have all necessary fixes from past work. Since the user asked now, I should verify and see if modifications are needed. The instructions mention to re-read after each edit and provide a summary, so I can mention verified findings without needing new edits. However, I need to check for any stale references that might still cause contradictions.
codex
I’m at the contradiction sweep now. Most flagged theorem surfaces already contain partial repairs, so I’m grep-checking the same file for stale statements that would quietly reintroduce the old errors elsewhere in the chapter.
exec
/bin/zsh -lc "rg -n 'mc2-bar-intrinsic.*E_1|E_1.*mc2-bar-intrinsic|ordered .*mc2-bar-intrinsic|mc2-bar-intrinsic.*ordered|g\\\\"'^'"\\{E1\\}|g\\\\"'^'"\\{mod\\}|coinvariant/symmetric MC2|Scope of MC2' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'family-index|genus-universality|Theorem~\\\\ref\\{thm:family-index\\}.*proof|family index.*universal|universal.*family index' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2620: (Theorem~\ref{thm:genus-universality}).
2727:(Theorem~\ref{thm:genus-universality}).
2914:scalar trace. Theorem~\ref{thm:genus-universality} is the first
2917:Theorem~\ref{thm:family-index} is downstream again: it is the
2930:and Theorem~\ref{thm:genus-universality} does not invoke
2931:Theorem~\ref{thm:family-index}.
2932:Part~(i) is Theorem~\ref{thm:genus-universality} for
2940:Theorem~\ref{thm:genus-universality}(ii).
3006:Theorem~\ref{thm:genus-universality}; the second is the downstream
3007:GRR/family-index identification of the same scalar series on the
3008:virtual bar family. Theorem~\ref{thm:family-index} is therefore the
3014:Theorem~\ref{thm:genus-universality}); generating function via
3024:\textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
3035:Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
3452:Theorem~\ref{thm:genus-universality}. The GUE free energy
3616:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
4047:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
4099:Theorem~\ref{thm:genus-universality}(ii)).
4772: Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
 succeeded in 51ms:
3596:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3830:\begin{remark}[Scope of MC2 in this chapter]
3840:Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
exec
/bin/zsh -lc "rg -n 'fixed pointed curve|fixed \\(X,D\\)|logarithmic Fulton--MacPherson space of a fixed|relative Fulton--MacPherson compactification|curve-degeneration boundary|universal stable curve' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'd_\\{\\mathrm\\{alg\\}\\} = 2|d_\\{\\mathrm\\{alg\\}\\}.*3|beta\\\\gamma_\\\\lambda|weight-changing line|mu_\\{\\\\beta\\\\gamma\\}|r_\\{\\\\max\\} = 4|class-\\\\mathbf\\{C\\} witness' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theta_\\\\cA := D_\\\\cA - \\\\dzero|genuswise-completion identification|G\\"'^1'"\\(\\\\Defcyc\\(\\\\cA\\)\\\\widehat\\\\otimes\\\\Gmod\\)|product expression in~\\\\eqref\\{eq:theta-bar-intrinsic\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Whitehead|truncated current algebra|H\\"'^1'"\\(\\\\fg|mixed genus-\\"'$0'"\\"'$/genus-'"\\"'$1'"\\"'$|mode pattern|finite-dimensional '"\\\\fg-module' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
22182:log-FM space of a fixed pointed curve.
31735:universal stable curve, and for every relative configuration space
31741:curve-degeneration boundary of the universal family.
31746:logarithmic Fulton--MacPherson space of a fixed pointed curve.
31750:curve-degeneration boundary of moduli. The correct carrier is the
31751:relative Fulton--MacPherson compactification of the universal stable
31823:curve-degeneration boundary of the universal family.
31869:collision strata and the curve-degeneration boundary. On that
 exited 2 in 50ms:
rg: regex parse error:
    (?:d_\{\mathrm\{alg\}\} = 2|d_\{\mathrm\{alg\}\}.*3|beta\\gamma_\\lambda|weight-changing line|mu_\{\\beta\\gamma\}|r_\{\\max\} = 4|class-\\mathbf\{C\} witness)
           ^^
error: unrecognized escape sequence
 succeeded in 50ms:
2348: $\Theta_\cA := D_\cA - \dzero
3609:Define $\Theta_\cA := D_\cA - \dzero$. Since
3749:The element $\Theta_\cA := D_\cA - \dzero$ is the positive-genus
3794:Via the genuswise-completion identification of
4346:$\Theta_\cA := D_\cA - \dzero \in
13231:$\Theta_\cA := D_\cA - \dzero$
 succeeded in 50ms:
896:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
902:non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
916:\index{truncated current algebra!mode bookkeeping only}
931:where $\nu$ runs over the finitely many mode patterns of total
935:In particular the truncated current algebra $\fg \otimes V_h$
936:records the mode cutoff only: the Whitehead step is carried out on
938:fixing a mode pattern~$\nu$, the residue action of the truncated
947:total weight is fixed, only finitely many mode patterns~$\nu$ occur.
954:mode pattern~$\nu$, this is exactly the
957:set of mode patterns gives the stated decomposition. More explicitly,
965:with coefficients $c_i(\nu)$ depending only on the mode pattern.
972: \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
975:\index{Whitehead lemma!mixed genus-0/genus-g factorization}
986:H^1(\fg, N_h^{n-1})
996:$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
997:the non-semisimple truncated current algebra $\fg \otimes V_h$.
1017:$H^1(\fg, N_h^{n-1})$.
1034:by Whitehead; the Killing-form invariant
1045:enrichment factorization, Whitehead acyclicity, and the
1137:mode patterns~$\nu$ of total weight~$h$. After separating mode data

thinking
**Inspecting curve details**

I need to search around line 22182 to check the fixed pointed curve. Maybe it's stale or outdated, and I should inspect it closely. I'm wondering what exactly I might find or if there's anything specific I should focus on during this inspection. I'll make sure not to overlook any details that could impact the analysis. Let's see if I can figure out what's going on!
exec
/bin/zsh -lc "sed -n '22155,22215p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 \otimes
 \Omega_{g_2,|S^c|+1}^{\cA}(v_{S^c}, e^\alpha),
 \]
 where $\{e_\alpha\}$, $\{e^\alpha\}$ are dual bases for~$\eta$.

\item \emph{Non-separating boundary.}
 For the gluing map
 $\xi_{\mathrm{nsep}} \colon
 \overline{\mathcal{M}}_{g-1,n+2} \to
 \overline{\mathcal{M}}_{g,n}$:
 \[
 \xi_{\mathrm{nsep}}^*\,\Omega_{g,n}^{\cA}(v_1, \ldots, v_n)
 \;=\;
 \sum_\alpha
 \Omega_{g-1,n+2}^{\cA}(v_1, \ldots, v_n, e_\alpha, e^\alpha).
 \]
\end{enumerate}
\end{theorem}

\begin{proof}



thinking
**Evaluating file status**

I’m working on checking for any uncommitted changes related to the theorem fixes, particularly around the "fixed pointed curve." The user expects changes to be made, so I need to make sure to review the git status. I think running `git diff -- chapters/theory/higher_genus_modular_koszul.tex` will help me identify any uncommitted changes. If everything is already verified, I’ll let the user know the file is rectified. But I need to ensure nothing is missed before confirming!
thinking
**Searching for inconsistencies**

To satisfy the requirement of "after each edit," it seems I should make minimal edits if I spot any micro inconsistencies. I need to search for residual contradictory phrasing that isn't directly part of the findings. For example, the proof regarding theorem `thm:universal-theta` might contain phrases that need clarifying. Additionally, I should look for any references to family-index being used improperly outside its proof context. I'll dig deeper into specific lines, like 2648, to ensure everything aligns well.
thinking
**Inspecting specific lines**

I think I should examine lines around 4760 and 4810 to look for any inconsistencies or areas that might need clarification. Checking these lines could help ensure everything aligns with the overall proof and findings, and I want to make sure that I’m thorough in my review. I’ll take a close look at the context to confirm that it all makes sense and meets the user's expectations. Let's see what I find!
exec
/bin/zsh -lc "sed -n '4758,4835p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \textup{(}up to gauge\textup{)} satisfies
 $[\theta_g] = \kappa(\cA) \cdot [\mu] \otimes \lambda_g$.

\item \emph{Generating function.}
 The scalar trace of $\Theta_{\cA}$ recovers the $\hat{A}$-genus:
 \begin{equation}\label{eq:theta-generating-function}
 \operatorname{tr}(\Theta_{\cA})
 \;=\;
 \kappa(\cA) \cdot \sum_{g \geq 1} \lambda_g
 \;=\;
 \kappa(\cA) \cdot
 \Bigl(\hat{A}(ix) - 1\Bigr)
 \end{equation}
 where the first equality is the scalar trace already identified by
 Theorem~\textup{\ref{thm:genus-universality}}, and the second is its
 downstream GRR/family-index reformulation
 \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
\end{enumerate}
\end{theorem}


thinking
**Reviewing equations and edits**

I'm considering the impact of the proof for `μ_{βγ}=0` in relation to the weight-changing line. There might be a need for minimal adjustments to incorporate `β\gamma_\lambda` in the key tables and figure captions. I should take a close look at the relevant tables around 12350 and 20357 to ensure everything aligns correctly. This is key to maintaining clarity and accuracy in the presentation. Let's see what we find!
exec
/bin/zsh -lc "sed -n '12340,12450p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17695,17815p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20340,20375p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '34945,34980p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '35300,35335p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{rem:depth-classification-holographic-truncation}
\index{depth classification!holographic truncation}
\index{shadow depth class!G/L/C/M}
\index{Brown--Henneaux!shadow tower reading}
Under the holographic reading of
Remark~\textup{\ref{rem:shadow-tower-holographic-interpretation}},
the four shadow depth classes $\mathbf{G}$, $\mathbf{L}$,
$\mathbf{C}$, $\mathbf{M}$
\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}
and Theorem~\textup{\ref{thm:nms-finite-termination}}\textup{)}
are truncation classes for the holographic correction series.
\begin{center}
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{@{}lllll@{}}
\toprule
\textbf{Class} & $r_{\max}$ & \textbf{Surviving corrections} &
 \textbf{Archetype} & \textbf{Holographic reading} \\
\midrule
$\mathbf{G}$ & $2$ & $S_2$ only & Heisenberg &
 succeeded in 51ms:
\[
 S_5 = -(P/10)(3 \cdot 4 \cdot S_3 S_4)
 = -(6/5)\,P\,\alpha\,S_4.
\]
For $\kappa \neq 0$ (so $P = 1/\kappa \neq 0$), $\alpha \neq 0$,
and $S_4 \neq 0$, this is nonzero. If $\alpha = 0$, then
$S_5 = 0$ but the next step gives
\[
 S_6
 \;=\;
 -\frac{P}{12}\cdot \frac12 \cdot 4 \cdot 4\,S_4^2
 \;=\;
 -\frac{2\,S_4^2}{3\kappa},
\]
which is again nonzero. Thus there is no second finite
cancellation beyond the affine one: away from $S_4 = 0$ the
single-line tower does not terminate. By induction,
$S_4 \neq 0$ propagates to infinitely many nonzero $S_r$: the closed form
$H(t) = t^2\sqrt{Q_L(t)}$ makes this manifest.

 succeeded in 51ms:
\label{rem:shadow-radius-atlas}
\index{shadow radius!atlas|textbf}
\index{shadow depth!classification}
The shadow growth rate refines the
$\mathbf{G}$/$\mathbf{L}$/$\mathbf{C}$/$\mathbf{M}$
classification into a \emph{continuous invariant} on
class~$\mathbf{M}$:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{llcccc}
\toprule
\textbf{Family} & \textbf{Class} & $r_{\max}$ &
 $\boldsymbol{\rho}$ & \textbf{Conv?} & \textbf{$\arg(t_0)/\pi$} \\
\midrule
Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
$\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
 $12.53$ & no & $0.907$ \\
 succeeded in 50ms:
\ClaimStatusConjectured
\index{bar complex!growth rate!rank-$1$ universality|textbf}
\index{bar cohomology!exponential growth rate}
For every rank-$1$ chirally Koszul algebra~$\cA$ with
interacting OPE \textup{(}i.e., excluding free fields\textup{)},
the bar cohomology generating function
$P_{\cA^!}(x) = \sum_{n \geq 1} \dim(\cA^!)_n\, x^n$
has dominant singularity at $x = 1/3$, giving exponential
growth rate
\begin{equation}\label{eq:bar-growth-rate-3}
 \gamma(\cA)
 \;:=\;
 \limsup_{n \to \infty}
 \bigl(\dim(\cA^!)_n\bigr)^{1/n}
 \;=\; 3.
\end{equation}
The value $\gamma = 3$ is \emph{universal} across rank-$1$
families: Virasoro \textup{(}Motzkin differences,
$P(x) = (1 - x - \sqrt{1{-}2x{-}3x^2})/(2x)$,
degree-$2$ algebraic\textup{)},
 succeeded in 50ms:
this flag variety: $\kappa$ is the scalar coordinate (degree~$2$),
the cubic class $\mathfrak{C}$ opens the first higher direction,
and the quartic class $\mathfrak{Q}$ opens the second.

Under this reading, the
$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
(Theorem~\ref{thm:single-line-dichotomy}) describes the
topology of the period image:
\begin{itemize}
\item Class~$\mathbf{G}$ (Heisenberg, depth $r=2$): the period
 image is a single point; $\kappa$ is the only nonvanishing
 coordinate and the shadow tower terminates at degree~$2$.
\item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
 image traces a curve in the flag variety, parametrized by the
 cubic direction $\mathfrak{C}$; no quartic thickening.
\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
 is a surface, with the quartic coordinate $\mathfrak{Q}$
 providing the second independent direction; higher transport
 is blocked by stratum separation.
\item Class~$\mathbf{M}$ (Virasoro and $\mathcal{W}_N$, depth


thinking
**Adjusting tables for clarity**

I’m considering some adjustments with the βγ shorthand in my tables. To avoid contradictions, it might help to tweak one or two key tables or captions, particularly around line 12363, which is a classification table. I should think about replacing ambiguous `βγ` with `βγ_\lambda` in a few representative class tables. Since I'm only editing the target file, I’ll focus on minimal edits in directly relevant areas to clarify without changing unrelated elements.
thinking
**Inspecting classification tables**

I need to identify surfaces related to finding 6, particularly around line 16414, which might be tied to the propositions on obstruction 5/6 and related figures. I noticed that around line 16250, there's a class C row labeled just `βγ`. It seems logical to update that table row and possibly the figure beneath it. I should focus on editing only core classification surfaces near 16414 and 17014. I’ll check the exact line with the command `nl -ba` to confirm.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16390,16430p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 16390	\[
 16391	 t_\pm
 16392	 \;=\;
 16393	 \frac{-6\kappa\alpha
 16394	 \pm 2\kappa\,i\sqrt{2\Delta}}
 16395	 {9\alpha^2 + 2\Delta}
 16396	\]
 16397	are a \emph{complex conjugate pair} (they are real only
 16398	when $\Delta \leq 0$, which forces class~$\mathbf{G}$
 16399	or~$\mathbf{L}$). The branch points of $\sqrt{Q_L}$
 16400	at $t = t_\pm$ control the Taylor coefficients via the
 16401	standard formula
 16402	\begin{equation}\label{eq:branch-point-asymptotics}
 16403	 a_n
 16404	 \;\sim\;
 16405	 A \cdot |t_0|^{-n} \cdot n^{-3/2}
 16406	 \cos(n\,\theta + \varphi),
 16407	 \qquad n \to \infty,
 16408	\end{equation}
 16409	where $t_0 = t_+$ is the branch point, $|t_0|$ is its

thinking
**Inspecting line discrepancies**

I’m noticing line 16414 in the current file is not a class C witness, and the line numbers have shifted. So, I can't use the user-provided line references exactly as they correspond to an earlier version. I need to focus on local sections by label and inspect the current proposition around line 17115. I also want to check the actual line near 17609 for the depth-gap. Plus, looking into tables around 12363 and 20357 seems important! Let's also inspect the theorem regarding `shadow-archetype-classification` around 16800.
exec
/bin/zsh -lc "rg -n -F 'thm:shadow-archetype-classification' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4590:(Theorem~\ref{thm:shadow-archetype-classification}), so
16065:(Theorem~\ref{thm:shadow-archetype-classification}),
16342:(Theorem~\ref{thm:shadow-archetype-classification}), so
16866:\label{thm:shadow-archetype-classification}
18898:Theorem~\ref{thm:shadow-archetype-classification}).
19234:For affine Kac--Moody $\hat{\fg}_k$: the quartic obstruction $o_4 = \frac{1}{2}\{\mathfrak{C},\mathfrak{C}\}_H$ vanishes by the Jacobi identity (Theorem~\ref{thm:shadow-archetype-classification}(ii)), giving $S_4 = 0$ and $\Delta = 0$. The shadow metric $Q_L = (2\kappa + 3\alpha t)^2$ is a \emph{perfect square}: $\sqrt{Q_L}$ is polynomial and the tower terminates at $r_{\max} = 3$. The shadow connection is trivial ($\omega = Q'/(2Q) = 3\alpha/(2\kappa+3\alpha t)$, regular everywhere), consistent with the finite depth.
19485:Theorem~\ref{thm:shadow-archetype-classification}:
22512:\textup{(}Theorem~\textup{\ref{thm:shadow-archetype-classification}(i)}\textup{)}.
25330:(Theorem~\ref{thm:shadow-archetype-classification})
25824:(Theorem~\ref{thm:shadow-archetype-classification});
27827:(Theorem~\ref{thm:shadow-archetype-classification}),
exec
/bin/zsh -lc "sed -n '16850,17030p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \S\ref{sec:higher-depths} \\
Rank-$72$ &
 $\mathbf{G}$ & $6$ & $0$ & $0$ &
 \S\ref{sec:higher-depths} \\
\bottomrule
\multicolumn{6}{l}{\textsuperscript{$\ast$}%
 Stratum-separated global family:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
 The charged quartic lies off the $T$-line, so the single-line
 discriminant is not the class-$\mathbf{C}$ witness.}
\end{tabular}
\end{center}
\end{example}

\begin{theorem}[Shadow archetype classification]
\label{thm:shadow-archetype-classification}
\ClaimStatusProvedHere
\index{shadow depth!classification theorem|textbf}
\index{shadow archetype classification|textbf}









thinking
**Revising theorem details**

I've corrected the theorem, but the figure node still shows `βγ`. That seems okay, yet the line 20357 table might need a similar check. The task to find six is likely resolved by the theorem or proof, so maybe no edits are necessary. However, we could add a note to clarify any ambiguity about shorthand in the figure or table. I should also confirm that the remaining uses of “βγ” are not crucial. Lastly, I need to note that the introduction cross-reference has been fixed but user instructions only target the specific file. It might be worthwhile to mention that it’s fixed upstream in the final summary.
thinking
**Editing classification visuals**

I see that some findings are already fixed, so we might only need small edits to clarify the ambiguous class-C witness shorthand used in the visuals and related holographic table. The user asked to fix seven findings, and if everything is resolved but the shorthand, I can mention that I performed a minimal consistency update. However, we should check for any remaining contradictions, like the figure label at 16866 still using node `βγ`, which may imply a single algebra instead of the full family. Updating it to `β\gamma_\lambda` or “full $\beta\gamma_\lambda$” would help avoid confusion. I also need to consider other tables and whether editing multiple occurrences is necessary, especially since the user requested a specific file.
thinking
**Updating theorem references**

I can update the figure associated with the theorem and one local summary remark nearby. The footnote in the example might already help clarify the stratum-separated global family. Now, about finding five and the depth gap; I see that there's a split in the proposition. The line 146 at the top says "No other depths occur," which might be fine. I should search for any theorems or tables that reference `kappa ≠0` to see if they exclude beta gamma. There's also a potential unresolved issue with the statement at 3596, but the intro cross-reference seems okay. I should check earlier references in the target file to see if they misattribute E1 to the MC2 theorem.
thinking
**Evaluating proof adjustments**

I’m considering potential issues with the 7 D^2 proof that utilizes a universal family now, contrasting it with an earlier proposition proving cross-term cancellation. That part seems fine, but I need to remember an earlier remark about the ambient level geometry requiring log-FM normal-crossings. The user asked for specific edits, so I’ll aim to clarify where there’s ambiguity, like adjusting `βγ` to `βγ_\lambda`. I might also note that there's an alternative route in the theorem, but edits might not be necessary overall.
thinking
**Reviewing theorem edits**

I need to examine if there are any contradictory phrases in the alternative proof for Theorem D regarding the uniform-weight clause. The statement about having a second proof route without using certain concepts seems fine and not circular. I’m considering whether I should adjust lines 3596 or 3770, but the theorem already appears to be in good shape. The user expected fixes, yet if everything is already rectified, I might just state that no changes are needed while also verifying for pending edits via git. However, I could still add a small clarification to strengthen the ambiguity.
thinking
**Checking for contradictory tables**

I want to verify whether there are contradictory archetype tables that reference `βγ` at `r_max=4` without mentioning the full family, as these could be misleading. Specifically, I’m looking at the remark at 12363 regarding "Archetype βγ" and the shadow postnikov diagram node `\mathbf{C}: \beta\gamma, r_max=4`. Since the theorem proof clarifies the full family, it makes sense to update these references to `\beta\gamma_\lambda$ family. I’m also considering whether any figures or tables need adjustments, particularly in the depth classification area.
thinking
**Updating findings in theorem file**

I'm noticing that the task asks for careful reading and fixing specific issues in a large theory file. I think I need to update the visualization surfaces around the theorem and one major table. I’ll search for the exact pattern “$\beta\gamma$ &” with class C. 

I might change the Archetype from “$\beta\gamma$” to “full $\beta\gamma_\lambda$ family” in one area, and update labels in diagrams to reflect this family. Additionally, I could rephrase some captions and remarks for clarity. These seem like moderate but necessary edits.
thinking
**Considering technical edits**

The user requested the strongest technical choice, but it seems like these edits are more about cleanup than providing a proof. I'm wondering if that’s acceptable, especially if there are no proof issues remaining. 

I might need to use a Pre-Edit Verification Protocol since this task touches theorem statuses and potentially affects hot zones. Since we're editing class C witness and possibly theorem D, I’ll have to fill in the commentary template first. The instructions say that mandatory checks are needed before editing any surfaces in hot zones, so I need to be cautious.
thinking
**Preparing commentary and verification**

I need to provide commentary with the verification template, possibly using at least PE-10 or something relevant. It seems theorem D may not relate to proof routing or formulas. For the class C witness, it looks like there might not be a designated template. However, I can still include a short pre-edit verification block that touches on the scope quantifier or relevant details like PE-10. Regarding editing, if it's complex, maybe I won't go there. The theorem D routing could just focus on remarks instead of formulas.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '19236,19255p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 19236	
 19237	\begin{remark}[Stratum separation and the depth decomposition]
 19238	\label{rem:contact-stratum-separation}
 19239	\index{contact class!stratum separation}
 19240	\index{stratum separation|textbf}
 19241	\index{rank-one abelian rigidity!stratum separation}
 19242	The single-line dichotomy governs
 19243	$r_{\max}|_L \in \{2,3,\infty\}$. The value
 19244	$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
 19245	requires \emph{stratum separation}.
 19246	The cyclic deformation complex decomposes by charge:
 19247	$\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
 19248	For $\beta\gamma$, the quartic contact invariant
 19249	$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
 19250	lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 19251	The self-bracket
 19252	$\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
 19253	has $\dim \Defcyc^{(2q)} = 0$ for rank-one systems:
 19254	the quartic pump does not activate, so $r_{\max} = 4$.
 19255	This is rank-one rigidity
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '20350,20370p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 20350	\toprule
 20351	\textbf{Family} & \textbf{Class} & $r_{\max}$ &
 20352	 $\boldsymbol{\rho}$ & \textbf{Conv?} & \textbf{$\arg(t_0)/\pi$} \\
 20353	\midrule
 20354	Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 20355	Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 20356	Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
 20357	$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 20358	$\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
 20359	 $12.53$ & no & $0.907$ \\
 20360	$\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
 20361	 $6.24$ & no & $0.911$ \\
 20362	$\mathrm{Vir}_6$ & $\mathbf{M}$ & $\infty$ &
 20363	 $1.02$ & no & $0.935$ \\
 20364	$\mathrm{Vir}_{c_\star}$ ($\approx 6.125$) & $\mathbf{M}$ &
 20365	 $\infty$ & $1.00$ & marginal & $0.936$ \\
 20366	$\mathrm{Vir}_{13}$ (self-dual) & $\mathbf{M}$ & $\infty$ &
 20367	 $0.47$ & yes & $0.950$ \\
 20368	$\mathrm{Vir}_{25}$ & $\mathbf{M}$ & $\infty$ &
 20369	 $0.24$ & yes & $0.961$ \\
exec
/bin/zsh -lc "rg -n -F 'realized by "'$'"\\beta\\gamma"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
19244:$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)

thinking
**Searching for class interpretations**

I’m looking into class C and its shorthand interpretations, especially with beta gamma notation. I should consider how to search for something like `Class\mathbf{C} (\beta\gamma, depth...)` at 35315. I might need to update my search if it’s local. It seems that searching with a fixed string, like `Class$\\mathbf{C}$ ($\\beta\\gamma$`, could be a good idea too. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n -F 'Class~"'$'"\\mathbf{C}"'$ ($'"\\beta\\gamma"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
35315:\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
exec
/bin/zsh -lc "rg -n -F '"'$'"\\mathbf{C}"'$: $'"\\beta\\gamma"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12436: {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
exec
/bin/zsh -lc "rg -n -F '"'$'"\\beta\\gamma"'$ & $'"\\mathbf{C}"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
20357:$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
exec
/bin/zsh -lc "rg -n -F '& "'$'"\\beta\\gamma"'$ &'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
12363:$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
26671:$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
30712: & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
exec
/bin/zsh -lc "sed -n '26660,26680p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '35308,35322p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30704,30718p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
families of tautological relations:
\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{llll}
\textbf{Class} & \textbf{Family} & \textbf{Shadow data}
 & \textbf{Relations generated} \\
\hline
$\mathsf{G}$ & Heisenberg & $\kappa$ only
 & Mumford ($\lambda$-class identities) \\
$\mathsf{L}$ & Affine KM & $\kappa, S_3$
 & Mumford $+$ Faber--Zagier \\
$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
 & Mumford $+$ FZ $+$ quartic \\
$\mathsf{M}$ & Virasoro & all $S_r$
 & Full MC tower $\supseteq$ Pixton ideal\,?
\end{tabular}
\end{center}
Theorem~\ref{thm:pixton-from-shadows} proves that on the
semisimple locus, the MC tower from class-$\mathsf{M}$ algebras
generates the full Pixton ideal
 succeeded in 50ms:
 \toprule
 Class & $r_{\max}$ & Archetype & Examples \\
 \midrule
 $\mathsf{G}$ (Gaussian) & $2$
 & Heisenberg & free bosons, lattice VOAs \\
 $\mathsf{L}$ (Lie/tree) & $3$
 & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
 $\mathsf{C}$ (contact) & $4$
 & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
 $\mathsf{M}$ (mixed) & $\infty$
 & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
 \bottomrule
 \end{tabular}
 \end{center}
 Shadow depth classifies \emph{complexity}, not
 succeeded in 50ms:
\begin{itemize}
\item Class~$\mathbf{G}$ (Heisenberg, depth $r=2$): the period
 image is a single point; $\kappa$ is the only nonvanishing
 coordinate and the shadow tower terminates at degree~$2$.
\item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
 image traces a curve in the flag variety, parametrized by the
 cubic direction $\mathfrak{C}$; no quartic thickening.
\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
 is a surface, with the quartic coordinate $\mathfrak{Q}$
 providing the second independent direction; higher transport
 is blocked by stratum separation.
\item Class~$\mathbf{M}$ (Virasoro and $\mathcal{W}_N$, depth
 $r=\infty$): the image meets a dense open subset of the
 period domain; for every finite cutoff~$N$ the period map has
 maximal horizontal rank.


thinking
**Updating tables and examples**

I’m considering updating all 8 instances to the beta gamma family since they’re all from the same file and have a specific issue. It's a modest change! I think line 30712 should include symplectic fermions as examples, and I might change the archetype row for Family to `$\beta\gamma_\lambda$ family` as well. There are some other lines I could update similarly, like line 26671 to `$\beta\gamma_\lambda$`. I'll keep evaluating the fit of various components and labels!
thinking
**Considering updates for clarity**

I’m thinking about updating line 34965 to adjust the conjecture examples of rank-1 families because they might not relate specifically to class C witnesses. That's probably not necessary. For line 19248, I wonder if I should change it to say, “For the full $\beta\gamma_\lambda$ family, the quartic contact invariant...". I’d also like to clarify the remark around line 19244, but I need to read more of the context before making that decision.
exec
/bin/zsh -lc "sed -n '19237,19266p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[Stratum separation and the depth decomposition]
\label{rem:contact-stratum-separation}
\index{contact class!stratum separation}
\index{stratum separation|textbf}
\index{rank-one abelian rigidity!stratum separation}
The single-line dichotomy governs
$r_{\max}|_L \in \{2,3,\infty\}$. The value
$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
requires \emph{stratum separation}.
The cyclic deformation complex decomposes by charge:
$\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
For $\beta\gamma$, the quartic contact invariant
$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
lives in $\Defcyc^{(q)}$ with $q \neq 0$.
The self-bracket
$\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
has $\dim \Defcyc^{(2q)} = 0$ for rank-one systems:
the quartic pump does not activate, so $r_{\max} = 4$.
This is rank-one rigidity
(Theorem~\ref{thm:betagamma-rank-one-rigidity})

thinking
**Evaluating build feasibility**

I'm pondering whether the full `texlab` build is too heavy. The user didn’t really request a complete build, so maybe I could try something lighter, like running `latexmk -pdf -interaction=nonstopmode -f main.tex`, but that feels too big. 

Instead, I might consider not running the build at all and just mentioning that. However, a targeted grep to reread modified sections could work! This way, I can keep things updated before any edits.
codex
I’ve confirmed the proof-level findings are already repaired on the main theorem surfaces. The residual problem is propagation: several summary tables/figures in the same file still advertise class `\mathbf{C}` as plain `\beta\gamma`, which reintroduces the old witness ambiguity. I’m making a scoped consistency edit inside this file only.
exec
/bin/zsh -lc "printf '%s
' '"'```'"' 'formula: class-C witness' 'Vol I: higher_genus_modular_koszul.tex uses both full "'$'"\\beta\\gamma_\\lambda"'$ family and shorthand $'"\\beta\\gamma"'$ in class-C representative tables/figures'"' 'Vol II: not touched (out of scope for this task)' 'Vol III: NA' 'consistent? N' 'if not: canonical vol I theorem surface uses full conformal-weight family; summary surfaces in this file will be updated same session? Y' 'convention conversion: NA' 'verdict: ACCEPT' '"'```'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
```
formula: class-C witness
Vol I: higher_genus_modular_koszul.tex uses both full $\beta\gamma_\lambda$ family and shorthand $\beta\gamma$ in class-C representative tables/figures
Vol II: not touched (out of scope for this task)
Vol III: NA
consistent? N
if not: canonical vol I theorem surface uses full conformal-weight family; summary surfaces in this file will be updated same session? Y
convention conversion: NA
verdict: ACCEPT
```

thinking
**Evaluating notation usage**

I'm thinking that the invariant for contact might still rely on subscripts beta and gamma without using lambda. I wonder if I could switch to `\mathfrak{Q}_{\beta\gamma_\lambda}` instead. But I should check if this notation is used elsewhere before making any changes. Searching for existing references would be a smart move to ensure consistency. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n -F '\\mathfrak{Q}_{\\beta\\gamma' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
19249:$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
19424: = \mathfrak{Q}_{\beta\gamma_1}$.
19480:while $\mathfrak{Q}_{\beta\gamma} =
exec
/bin/zsh -lc "sed -n '19410,19490p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 At degrees $r = 3$ and $r = 4$, there exist chirally
 Koszul algebras $\cA$, $\cB$ with
 $[\Theta_\cA^{\leq r-1}] = [\Theta_\cB^{\leq r-1}]$
 but $[\Theta_\cA^{\leq r}] \neq [\Theta_\cB^{\leq r}]$.
 \begin{itemize}
 \item $r = 3$:
 $\kappa(\cH_1) = \kappa(\mathrm{Vir}_2) = 1$,\;
 $\mathfrak{C}_{\cH} = 0 \neq 2x^3 =
 \mathfrak{C}_{\mathrm{Vir}}$.
 \item $r = 4$:
 $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
 $\mathfrak{C}_{\cH_1} = \mathfrak{C}_{\beta\gamma_1} = 0$
 on the conformal-weight family line;\;
 $\mathfrak{Q}_{\cH_1} = 0 \neq -5/12
 = \mathfrak{Q}_{\beta\gamma_1}$.
 \end{itemize}

\item \emph{Shadow class detection.}
 The shadow class is detected by the vanishing pattern of
 the first three nonlinear shadow components:

thinking
**Identifying inconsistencies in proof**

I'm looking at the case where r=4, and it's comparing Heisenberg H_1 and beta gamma_1 on the conformal-weight family line. But then, the proof mentions a weight-changing line and H_0, which feels inconsistent! This is really important, and I need to address this. I’m thinking I should inspect the theorem label and gather full context, especially around 19380, to clarify things. Nice catch on this inconsistency!
codex
I found a real residual contradiction tied to the class-`C` witness: one later proof still uses the old weight-changing-line `\beta\gamma` comparison, even though the corrected theorem surface says the witness is the full `\beta\gamma_\lambda` family. I’m repairing that downstream proof and aligning the summary tables/figures to the corrected witness.
exec
/bin/zsh -lc "sed -n '19380,19495p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
recursively via the OPE relation $T \in T_{(1)} T$), while
$d_{\mathrm{alg}}(\mathrm{Vir}_c) = \infty$ (every $m_n$ is nonzero,
$m_n(\bar T, \ldots, \bar T) = S_n(c)\cdot\bar T$ with $S_n(c) \neq 0$,
Theorem~\ref{thm:depth-decomposition}). Saying ``Virasoro has depth
$3$'' without a subscript is therefore ambiguous and forbidden:
$d_{\mathrm{gen}}(\mathrm{Vir}_c) = 3$ is the generating-depth
statement; $d_{\mathrm{alg}}(\mathrm{Vir}_c) = \infty$ is the
algebraic-depth statement, and both must be qualified.:
every depth claim in this manuscript carries an explicit subscript;
bare $d(\cA)$ is forbidden.
\end{definition}

\begin{theorem}[Shadow separation and completeness]
\label{thm:shadow-separation}
\ClaimStatusProvedHere
\index{shadow obstruction tower!separation theorem|textbf}
\index{shadow separation theorem|textbf}
The shadow obstruction tower is a complete and strictly refined
invariant of the modular deformation type.
\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "rg -n -F 'Q_{\\beta\\gamma_1}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -- '-5/12|S_4 = -5/12|\\mathfrak\\{Q\\}_\\{\\beta\\\\gamma_1\\}|\\mathfrak\\{Q\\}_\\{\\beta\\\\gamma' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:-5/12|S_4 = -5/12|\mathfrak\{Q\}_\{\beta\\gamma_1\}|\mathfrak\{Q\}_\{\beta\\gamma)
                         ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'S_4 = -5/12' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{Q}_{\\beta\\gamma_1}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:betagamma-global-depth' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathfrak{Q}_{\\beta\\gamma}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
15060: & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
15079:$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
15124:$S_4 = -5/12$, and $S_r = 0$ for $r \geq 5$.
16858: $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
16905:  S_4 = -5/12,\qquad
16976:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
17630:  S_4 = -5/12,\qquad
17730:is the nonzero constant $S_4 = -5/12$.
 succeeded in 52ms:
19424: = \mathfrak{Q}_{\beta\gamma_1}$.
 succeeded in 52ms:
19249:$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
19480:while $\mathfrak{Q}_{\beta\gamma} =
 succeeded in 52ms:
15129:\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
16833: Thm~\ref{thm:betagamma-global-depth} \\[3pt]
16911: \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
16976:$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
17725:Theorem~\ref{thm:betagamma-global-depth} gives

thinking
**Inspecting theorem**

I need to take a closer look at the theorem related to 15050 to see if it provides exact shadow data. My goal is to understand what this theorem entails and how it can be applied. I may need to gather additional information or formulas to fully grasp the implications of this data. Once I have a clearer understanding, I'll be able to proceed more effectively. Let's dive into the details!
exec
/bin/zsh -lc "sed -n '15045,15135p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Heisenberg $\cH_c$
 & $\mathbf{G}$ & $2$
 & $c$
 & ---\;(tower trivial) \\
Lattice $V_\Lambda$
 & $\mathbf{G}$ & $2$
 & $\operatorname{rank}\Lambda$
 & --- \\[4pt]
Affine $\hat{\fg}_k$
 & $\mathbf{L}$ & $3$
 & $\dfrac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ \\[6pt]
$\beta\gamma_\lambda$\rlap{\textsuperscript{$\dagger$}}
 & $\mathbf{C}$ & $4$
 & $6\lambda^2 - 6\lambda + 1$
 & $S_3 = 0,\;\; S_4 = -5/12$ \\[4pt]
$\mathrm{Vir}_c$
 & $\mathbf{M}$ & $\infty$
 & $c/2$
 & $\mathfrak{C} = 2x^3$,\;
exec
/bin/zsh -lc "rg -n -F 'label{thm:depth-decomposition}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'Depth decomposition|termination mechanisms|Table~\\(A\\)|shadow depth classes' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
12346:the four shadow depth classes $\mathbf{G}$, $\mathbf{L}$,
15031:projections~(A) and the termination mechanisms~(B).
15035:\textbf{Table~(A).\enspace Shadow obstruction tower projections.}
15711:truncated MC element. The four shadow depth classes are:
16876:Equivalently, it belongs to exactly one of the shadow depth classes
17828:the coarse shadow depth classes as follows:
26660:The four shadow depth classes produce hierarchically richer
34971:algebraic structures and distinct shadow depth classes

thinking
**Inspecting theorem header**

I need to take a closer look at the theorem header before the table at 15031. It's important to ensure everything is correctly set up there. I'm curious about what specific details or adjustments need to be made to clarify the theorem. I'll focus on making sure the information is accurately represented before moving ahead with any related tasks. Let’s see how everything connects!
exec
/bin/zsh -lc "sed -n '14985,15040p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\noindent\textbf{Input}: a cyclic chiral algebra~$\cA$ with cyclic
deformation complex $\Defcyc(\cA)$, Hessian~$H_{\cA}$,
propagator~$P_{\cA}$.

\smallskip
\noindent\textbf{Step~1} (Degree~$2$).
Solve the Maurer--Cartan equation at weight~$2$.
The unique solution is $\Theta_{\cA}^{\leq 2} = \kappa(\cA)$, the
modular characteristic (Theorem~D).

\smallskip
\noindent\textbf{Step~2} (Degree~$3$).
Compute the obstruction $o_3(\cA) =
(D\Theta^{\leq 2} + \tfrac12[\Theta^{\leq 2},\Theta^{\leq 2}])_3$.
If $[o_3] = 0$ in $H^2(\cA^{\mathrm{sh}}_{3,0})$, the cubic shadow
$\mathfrak{C}(\cA) = 0$ (Gaussian archetype: Heisenberg).
If $[o_3] \neq 0$, define
$\Theta_{\cA}^{\leq 3} = \Theta_{\cA}^{\leq 2}
+ \mathfrak{C}(\cA)$ where $\mathfrak{C} = -h(o_3)$
(Lie archetype: affine).

thinking
**Updating construction step**

I'm noticing that construction step 3 still mentions contacting archetype βγ. I think it would be better to update it to reflect βγ_λ family instead. That's a positive move! I could look into searching for "contact archetype: βγ" to find any additional information or context if needed. This might help ensure I have the most relevant details. I'm curious to see what I can uncover with that search!
exec
/bin/zsh -lc "rg -n -F 'contact archetype: "'$'"\\beta\\gamma"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
15014:+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).



thinking
**Searching for archetype fixes**

I should consider searching for `"class-$\\mathbf{C}$ witness"` to see what changes we can make. I already fixed some things, so that's good! I also think searching for `βγ` in archetype contexts might help us systematically patch any issues. However, there could be too many occurrences to handle at once. Let’s identify all instances of "contact archetype" and "class C" while keeping the scope to the same section and summary tables. That should work!
thinking
**Addressing findings and contradictions**

I’m considering searching for `\beta\gamma$ & $4`, but it might not be necessary. The user is asking about multiple critical findings that need fixing with strong technical choices. It’s vital to address the proof-level contradiction in `thm:shadow-separation`, directly tied to T16, so that needs fixing. 

I’m also wondering if there's a stale contradiction in the `r=4` example. We should just patch the proof since the theorem statement already uses the correct terms. Let's focus on possible contradictions around "The class-$\mathbf{C}$ witness" and adjust accordingly.
thinking
**Planning necessary patches**

I’m thinking we can patch all representative tables plus the proof, which seems fine. I should estimate around 10 patch occurrences. I might need to use `apply_patch` with multiple hunks to address everything.

For example, at Step 3 construction on line 15014, I’ll change `$\beta\gamma$` to `$\beta\gamma_\lambda$`. I want to inspect line 12363 closely, and it might be okay to patch now. We’ve got a snippet already, so I'll patch necessary rows and figure nodes. I'll also check whether to change the notation in `\mathfrak{Q}_{\beta\gamma}` for consistency.
codex
I’m editing the class-`C` witness surfaces now: the downstream proof of `thm:shadow-separation` and the representative tables/figures will all point to the full `\beta\gamma_\lambda` family rather than the obsolete single-line shorthand.

thinking
**Investigating patch errors**

I'm looking into why the patch failed, thinking it might be due to spaces. I need to inspect the exact lines to see if there's any issue with tabs or indentation. Checking for unnecessary newlines might be useful, but I want to focus on gathering the specific snippets surrounding those occurrences. It's important to pinpoint the problem to fix it effectively!
exec
/bin/zsh -lc "sed -n '15006,15018p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12358,12367p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12432,12440p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '19242,19252p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '26668,26673p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '19474,19484p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17008,17017p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30708,30714p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20354,20358p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '35312,35318p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\smallskip
\noindent\textbf{Step~3} (Degree~$4$).
Compute $o_4(\cA) =
(D\Theta^{\leq 3} + \tfrac12[\Theta^{\leq 3},\Theta^{\leq 3}])_4$.
This contains the $H$-Poisson bracket
$\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
vertex from~$m_4$. If $[o_4] = 0$, define
$\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).

\smallskip
\noindent\textbf{Step~4} (Degree~$5{+}$).
Repeat. Termination at degree~$r_{\max}$ means
 succeeded in 51ms:
\midrule
$\mathbf{G}$ & $2$ & $S_2$ only & Heisenberg &
 classical reconstruction exact \\
$\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
 first quantum correction \\
$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
 quartic contact term \\
$\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
 $\cW_N$ & full correction tower \\
\bottomrule
 succeeded in 50ms:
\index{rank-one abelian rigidity!stratum separation}
The single-line dichotomy governs
$r_{\max}|_L \in \{2,3,\infty\}$. The value
$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
requires \emph{stratum separation}.
The cyclic deformation complex decomposes by charge:
$\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
For $\beta\gamma$, the quartic contact invariant
$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
lives in $\Defcyc^{(q)}$ with $q \neq 0$.
The self-bracket
 succeeded in 51ms:
 font=\scriptsize] (TL) at (3.5,1.2)
 {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
\node[shC, minimum width=1.8cm, minimum height=0.45cm,
 font=\scriptsize] (TC) at (3.5,2.4)
 {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
\node[shM, minimum width=1.8cm, minimum height=0.45cm,
 font=\scriptsize] (TM) at (3.5,5.2)
 {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
%
 succeeded in 50ms:
$\mathsf{G}$ & Heisenberg & $\kappa$ only
 & Mumford ($\lambda$-class identities) \\
$\mathsf{L}$ & Affine KM & $\kappa, S_3$
 & Mumford $+$ Faber--Zagier \\
$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
 & Mumford $+$ FZ $+$ quartic \\
 succeeded in 50ms:
 font=\footnotesize\scshape] at (2,5.5) {Contact ($\mathbf{C}$)};
\node[shM, minimum width=2.2cm, minimum height=0.5cm,
 font=\footnotesize\scshape] at (3,5.5) {Mixed ($\mathbf{M}$)};
%
% ---- Archetype representatives ----
\node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
\node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
\node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
%
 succeeded in 50ms:
$\mathfrak{C}_{\cH_1} = 0$
(class~$\mathbf{G}$, strict coassociativity) while
$\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
(class~$\mathbf{M}$).
$r = 4$: on the weight-changing line,
$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
while $\mathfrak{Q}_{\beta\gamma} =
\operatorname{cyc}(m_3) \neq 0$
(Theorem~\ref{thm:nms-betagamma-quartic-birth}).

 succeeded in 51ms:
 $\mathsf{G}$ (Gaussian) & $2$
 & Heisenberg & free bosons, lattice VOAs \\
 $\mathsf{L}$ (Lie/tree) & $3$
 & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
 $\mathsf{C}$ (contact) & $4$
 & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
 $\mathsf{M}$ (mixed) & $\infty$
 succeeded in 51ms:
\midrule
Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 succeeded in 51ms:
 coordinate and the shadow tower terminates at degree~$2$.
\item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
 image traces a curve in the flag variety, parametrized by the
 cubic direction $\mathfrak{C}$; no quartic thickening.
\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
 is a surface, with the quartic coordinate $\mathfrak{Q}$
 providing the second independent direction; higher transport
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -15013,3 +15013,3 @@
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
apply_patch(auto_approved=true) exited 0 in 29ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..7dda89e2f1cfb517b87df744c3e8ddb6c61add31
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..7dda89e2f1cfb517b87df744c3e8ddb6c61add31
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -12362,3 +12362,3 @@
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
@@ -12435,3 +12435,3 @@
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
apply_patch(auto_approved=true) exited 0 in 28ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..e1cde05a0e2a89611b41645c4e54839cdeb2544c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..e1cde05a0e2a89611b41645c4e54839cdeb2544c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -17014,3 +17014,3 @@
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
apply_patch(auto_approved=true) exited 0 in 31ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..42127cb78dc5c5b20812bb8b7128129dd9a988df
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..42127cb78dc5c5b20812bb8b7128129dd9a988df
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -19244,8 +19244,8 @@
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
apply_patch(auto_approved=true) exited 0 in 30ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..75a4c09771c1c0ba27783ee5a6d086cf4855c9f8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..75a4c09771c1c0ba27783ee5a6d086cf4855c9f8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -19477,8 +19477,8 @@
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
apply_patch(auto_approved=true) exited 0 in 29ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..efb2e051b701e9fcb973af7bae0294ea497d40f1
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..efb2e051b701e9fcb973af7bae0294ea497d40f1
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -20357,3 +20357,3 @@
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
@@ -26671,3 +26671,3 @@
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
@@ -30712,3 +30712,3 @@
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
@@ -35315,3 +35315,3 @@
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
apply_patch(auto_approved=true) exited 0 in 29ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.


thinking
**Verifying updates and coherence**

I need to update `\mathfrak{Q}_{\beta\gamma}` and remove another occurrence at 19480. I should look for family representation patterns and might add `\beta\gamma_\lambda` to the radius table, though I'm unsure. I must verify if `\mathfrak{Q}_{\beta\gamma_\lambda}` is causing any undefined notation. Also, could there be a more representative table occurrence at 34965? Maybe not, but I need to re-read the modified sections for coherence and apply `sed` around each.
codex
The proof-level repair is in. I’m re-reading the modified blocks now to make sure the new `\beta\gamma_\lambda` family witness is coherent in the theorem proof and that the local summary surfaces don’t drift back to the obsolete single-line interpretation.
exec
/bin/zsh -lc "sed -n '15006,15018p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\smallskip
\noindent\textbf{Step~3} (Degree~$4$).
Compute $o_4(\cA) =
(D\Theta^{\leq 3} + \tfrac12[\Theta^{\leq 3},\Theta^{\leq 3}])_4$.
This contains the $H$-Poisson bracket
$\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
vertex from~$m_4$. If $[o_4] = 0$, define
$\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).

\smallskip
\noindent\textbf{Step~4} (Degree~$5{+}$).
Repeat. Termination at degree~$r_{\max}$ means
exec
/bin/zsh -lc "sed -n '12358,12440p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '17008,17017p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '19242,19256p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\midrule
$\mathbf{G}$ & $2$ & $S_2$ only & Heisenberg &
 classical reconstruction exact \\
$\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
 first quantum correction \\
$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
 quartic contact term \\
$\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
 $\cW_N$ & full correction tower \\
\bottomrule
\end{tabular}
\end{center}
Class~$\mathbf{G}$ is the Brown--Henneaux regime: the leading
central charge $S_2 = \kappa(\cA)$ already captures the entire
boundary-bulk map, and no higher-degree vertices contribute.
Class~$\mathbf{L}$ admits a single quantum correction at degree~$3$,
killed at degree~$\geq 4$ by the Jacobi identity of the affine
bracket. Class~$\mathbf{C}$ admits a further quartic
contact vertex, after which stratum separation on
$\overline{\mathcal{M}}_{0,5}$ forces all higher shadows to
 succeeded in 52ms:
 font=\footnotesize\scshape] at (2,5.5) {Contact ($\mathbf{C}$)};
\node[shM, minimum width=2.2cm, minimum height=0.5cm,
 font=\footnotesize\scshape] at (3,5.5) {Mixed ($\mathbf{M}$)};
%
% ---- Archetype representatives ----
\node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
\node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
\node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
%
 succeeded in 52ms:
\index{rank-one abelian rigidity!stratum separation}
The single-line dichotomy governs
$r_{\max}|_L \in \{2,3,\infty\}$. The value
$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
The cyclic deformation complex decomposes by charge:
$\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
lives in $\Defcyc^{(q)}$ with $q \neq 0$.
The self-bracket
$\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
has $\dim \Defcyc^{(2q)} = 0$ for rank-one systems:
the quartic pump does not activate, so $r_{\max} = 4$.
This is rank-one rigidity
exec
/bin/zsh -lc "sed -n '19472,19484p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
by \S\ref{sec:heisenberg-shadow-gaussianity} and
\S\ref{sec:mixed-cubic-quartic-shadows}; but
$\mathfrak{C}_{\cH_1} = 0$
(class~$\mathbf{G}$, strict coassociativity) while
$\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
(class~$\mathbf{M}$).
$r = 4$: on the global conformal-weight family,
$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
while $\mathfrak{Q}_{\cH_1} = 0$ and
$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.

exec
/bin/zsh -lc "sed -n '26668,26673p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20354,20358p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '30708,30714p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'realized by "'$'"\\beta\\gamma"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '35312,35318p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '"'$'"\\mathbf{C}"'$: $'"\\beta\\gamma"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
$\mathsf{G}$ & Heisenberg & $\kappa$ only
 & Mumford ($\lambda$-class identities) \\
$\mathsf{L}$ & Affine KM & $\kappa, S_3$
 & Mumford $+$ Faber--Zagier \\
$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
 & Mumford $+$ FZ $+$ quartic \\
 succeeded in 50ms:
\midrule
Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 succeeded in 51ms:
 $\mathsf{G}$ (Gaussian) & $2$
 & Heisenberg & free bosons, lattice VOAs \\
 $\mathsf{L}$ (Lie/tree) & $3$
 & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
 $\mathsf{C}$ (contact) & $4$
 & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
 $\mathsf{M}$ (mixed) & $\infty$
exec
/bin/zsh -lc "rg -n -F '"'$'"\\beta\\gamma"'$ & $'"\\mathbf{C}"'$'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
 coordinate and the shadow tower terminates at degree~$2$.
\item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
 image traces a curve in the flag variety, parametrized by the
 cubic direction $\mathfrak{C}$; no quartic thickening.
\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
 is a surface, with the quartic coordinate $\mathfrak{Q}$
 providing the second independent direction; higher transport
 exited 1 in 52ms:

 exited 1 in 51ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.

exec
/bin/zsh -lc "rg -n -F '"'$'"\\beta\\gamma"'$ &'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
13839:$\beta\gamma$ & $\checkmark$ & gauge-trivial & $\checkmark$ (quartic) \\
15358:$\beta\gamma$ &
15907: $\beta\gamma$ & $0$ & $0$ & $0$ & $\mathbf{C}$ &
16832:$\beta\gamma$ &
19117:$\beta\gamma$ & --- & --- & --- & ---
28390: $\beta\gamma$ & $\mathsf{C}$ & $0$ & $\infty$ & Yes \\
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.


thinking
**Evaluating updates for tables**

I see there are many generic tables concerning beta and gamma, but it's unclear if I need to update them. Some might still be valid, especially if they reference family notation. But if a row in class C uses the terms ambiguously, I may need to consider updating specific examples. I'll search for contexts where `βγ` and `r_max=4` appear in connection with class C to determine if they're still relevant.
exec
/bin/zsh -lc "rg -n 'beta\\\\gamma.*r_\\{\\\\max\\}|r_\\{\\\\max\\}.*beta\\\\gamma|class.~\\\\mathbf\\{C\\}.*beta\\\\gamma|beta\\\\gamma.*class.~\\\\mathbf\\{C\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
12436: {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.






thinking
**Searching for theorem updates**

I'm thinking about searching for `d_alg = 2` and checking if `weight-changing line` in the shadow separation theorem has been resolved. It seems like there might be other unresolved issues that need attention. I wonder if the current introduction adequately references `thm:mc2-bar-intrinsic` and `thm:e1-mc-element`. It could be a good idea to mention that some findings have already been addressed in our current edits, but I also want to confirm anything that might still need attention.
thinking
**Reviewing theorem edits**

I’m considering noting a `[FIXED]` finding since the existing theorem surface already addresses the routing remark, and no additional edits are needed. The structured output requires a rectification summary, so I'll mention which items were verified as fixed. It could be worth running a targeted diff to inspect modifications and possibly add line numbers for references in my final answer. I should check for any compile issues too, but I'll try to keep things concise in my output.
thinking
**Checking syntax and references**

I’m considering running a targeted syntax check with `tectonic --keep-intermediates`, though that might not be available. At the very least, I could run `latexmk -pdf -silent -interaction=nonstopmode -halt-on-error main.tex`, even if it takes a while. Since the user asked, I need to verify that the references and labels are valid. I haven’t introduced any new ones, aside from those already in the theorem. It might be worth exploring a narrow LaTeX parse.
thinking
**Verifying theorem status and references**

I’m considering using `chktex`, but it might not be installed. I could run `latexmk -pdf` with specific options, even though the repo is large. The user asked about the status of theorem tags, references, and labels. I can check if the label `thm:betagamma-global-depth` exists, perhaps using `rg` for a quick search. I need to confirm that no new invalid macros have appeared. It seems necessary to keep things efficient.
thinking
**Checking for stale lines**

I’m considering whether I need to use `texfot`, but I don't think it's necessary. Instead, I want to verify that there are no remaining stale "weight-changing line" references in the shadow-separation proof. I could search for the line using `rg -n -F` to identify contexts. It looks like there are some correct instances, which is good. I might run a `git diff` command on the relevant file to check specifics in the first 220 lines.
codex
The file-local contradiction sweep is clean now: the repaired proof no longer falls back to the weight-changing line, and the class-`C` summary surfaces in this chapter consistently use the full `\beta\gamma_\lambda` family. I’m doing one last diff/readback pass before closing.
exec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index ccd33b0..29dbe3c 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -11814,6 +11814,20 @@ $\ell_3^{(0)}\neq0$, $\ell_4^{(0)}\neq0$ the mixed class
 (Virasoro, $\mathcal{W}_N$).
 \end{computation}
 
+\begin{proof}
+The formulas for $\ell_3^{(0)}$, $\ell_4^{(0)}$, and $\ell_1^{(1)}$
+are the specializations of the graphwise Taylor-coefficient definition
+\eqref{eq:graphwise-taylor-coefficients} to the stable graphs
+with $(g,k)=(0,3)$, $(0,4)$, and $(1,1)$.
+Equations~\eqref{eq:ell3-explicit}, \eqref{eq:ell4-explicit}, and
+\eqref{eq:ell1-genus1} record these three cases explicitly.
+The archetype classification is then read off from the first place
+where the Taylor coefficients fail to vanish:
+Heisenberg has trivial cubic term, affine
+$\widehat{\mathfrak{sl}}_2$ has a nonzero cubic term but no quartic
+obstruction, and the mixed families have both coefficients nonzero.
exec
/bin/zsh -lc "rg -n -F 'weight-changing line' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{thm:betagamma-global-depth}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'coinvariant/symmetric MC2 statement' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
15127:weight-changing line has zero shadow tower, so the
16901: The class-$\mathbf{C}$ witness is not the weight-changing line and
16968:(iii)~For $\beta\gamma_\lambda$, the weight-changing line alone is not
17719:one-dimensional internal slices. On the weight-changing line,
19135:${}^*$\,Stratum separation (Remark~\ref{rem:contact-stratum-separation}): $\kappa = 0$ on the weight-changing line; shadow metric not applicable.\\
 succeeded in 51ms:
3596:In this chapter, it is the coinvariant/symmetric MC2 statement; the
 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F 'finite-dimensional "'$'"\\fg"'$-module'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Theorem~\\ref{thm:family-index} is downstream again' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'genuswise-completion identification' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'relative Fulton--MacPherson compactification of the universal stable' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
31752:relative Fulton--MacPherson compactification of the universal stable
 succeeded in 51ms:
3794:Via the genuswise-completion identification of
 succeeded in 51ms:
2917:Theorem~\ref{thm:family-index} is downstream again: it is the
 succeeded in 51ms:
937:the finite-dimensional $\fg$-modules $M_{h,\nu}$. Equivalently, after
979:finite-dimensional $\fg$-module $N_h^{n-1}$ and
1151:finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
1173:for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
1482:finite-dimensional $\fg$-module~$N$ with no trivial
1963:finite-dimensional $\fg$-module~$N$ with no trivial summand,
9411: finite-dimensional $\fg$-module, with the same
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.


thinking
**Reviewing verification process**

I'm considering linking the target file with line numbers for clarity since the final version is concise. I want to mention that I didn't run a full TeX build; instead, I verified by rereading modified sections and using grep checks for stale class-C witness phrases. This was to ensure refs and labels were valid. There's also the matter of cross-referencing the introduction. I could check around line 374, but it seems that correction is already done in the workspace.
codex
I’ve finished the local verification loop. The remaining proof gap was the downstream `thm:shadow-separation` witness, and that is now aligned with the corrected `\beta\gamma_\lambda` family witness. I’m checking the one external intro reference once more, but not editing outside the assigned file unless it is still wrong.
exec
/bin/zsh -lc "rg -n -F 'thm:e1-mc-element' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '17605,17735p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2910,2945p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31735,31875p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3770,3850p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '19240,19485p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '916,1185p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
392:(Theorem~\ref{thm:e1-mc-element}); since
874:\textup{(}Theorem~\textup{\ref{thm:e1-mc-element}}\textup{)}
1258:(Theorem~\ref{thm:e1-mc-element}):
1361:(Theorem~\ref{thm:e1-mc-element}).
2059:MC2 & Universal MC class $\Theta_\cA$ & \textbf{proved} & coinvariant bar-intrinsic MC2 (Thm~\ref{thm:mc2-bar-intrinsic}); ordered lift (Thm~\ref{thm:e1-mc-element}) \\[2pt]
2076:\textup{(}Theorem~\ref{thm:e1-mc-element}\textup{)}, and averaging
 succeeded in 51ms:
 17605	shadow tower is not a free parameter: it is \emph{read off} from
 17606	the arithmetic of a single quadratic, and the only outcomes are
 17607	termination or infinite extent.
 17608	
 17609	\begin{proposition}[Algebraic depth gap: no $d_{\mathrm{alg}} = 3$]
 17610	\label{prop:depth-gap-trichotomy}
 17611	\ClaimStatusProvedHere
 17612	\index{algebraic depth!gap theorem|textbf}
 17613	\index{shadow depth!forbidden values}
 17614	\index{depth classification!algebraic depth gap}
 17615	Let $\cA$ be a chirally Koszul algebra in the standard landscape.
 17616	Then the algebraic depth satisfies
 17617	\begin{equation}\label{eq:depth-gap}
 17618	 d_{\mathrm{alg}}(\cA) \;\in\; \{0,\, 1,\, 2,\, \infty\}.
 17619	\end{equation}
 17620	More precisely:
 17621	\begin{enumerate}[label=\textup{(\roman*)}]
 17622	\item on any primary line~$L$ with $\kappa|_L \neq 0$, one has
 17623	 $d_{\mathrm{alg}}(L) \in \{0, 1, \infty\}$;
 17624	\item the boundary value $d_{\mathrm{alg}} = 2$ is realized by the
 succeeded in 51ms:
 31735	writing $\pi\colon \cC_{g,n}\to \overline{\cM}_{g,n}$ for the
 31736	universal stable curve, and for every relative configuration space
 31737	$\operatorname{FM}_k(\cC_{g,n}/\overline{\cM}_{g,n})$, the
 31738	fiberwise collision operator $d_B$ satisfies $d_B^{\,2}=0$
 31739	unconditionally, and the fiberwise genus-$g$ differential satisfies
 31740	$\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$, where
 31741	$\omega_g = c_1(\lambda)$ is the Hodge class contributed by the
 31742	curve-degeneration boundary of the universal family.
 31743	\end{theorem}
 31744	
 31745	\begin{proof}
 31746	The ambient differential $D_{\cA}$ is not built from the
 31747	logarithmic Fulton--MacPherson space of a fixed pointed curve.
 31748	For fixed $(X,D)$, the space
 31749	$\operatorname{FM}_n^{\mathrm{log}}(X \mathbin{|} D)$ sees only
 31750	configuration and puncture collisions, so it cannot produce the
 31751	curve-degeneration boundary of moduli. The correct carrier is the
 31752	relative Fulton--MacPherson compactification of the universal stable
 31753	family over $\overline{\cM}_{g,n}$.
 31754	
 succeeded in 51ms:
  2910	\begin{proof}
  2911	\emph{Routing remark.}
  2912	The non-circular anchor is the bar-intrinsic shadow tower.
  2913	Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
  2914	scalar trace. Theorem~\ref{thm:genus-universality} is the first
  2915	downstream step: it identifies the genus-$g$ scalar component of that
  2916	trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
  2917	Theorem~\ref{thm:family-index} is downstream again: it is the
  2918	Grothendieck--Riemann--Roch identification of the already constructed
  2919	scalar series for the bar family~\eqref{eq:bar-family} on the
  2920	universal curve. Thus the logical route is
  2921	\[
  2922	\Theta_\cA
  2923	\;\Longrightarrow\;
  2924	\mathrm{obs}_g=\kappa(\cA)\lambda_g
  2925	\;\Longrightarrow\;
  2926	\sum_{g \geq 1} F_g x^{2g}
  2927	=
  2928	\kappa(\cA)\cdot(\hat{A}(ix)-1),
  2929	\]
 succeeded in 52ms:
  3770	\label{thm:mc2-bar-intrinsic}
  3771	\index{universal Maurer--Cartan class!bar-intrinsic construction}
  3772	\index{MC2!bar-intrinsic proof}
  3773	\index{MC2!full generality}
  3774	Let $\cA$ be a modular Koszul chiral algebra on a smooth
  3775	projective curve~$X$ with non-degenerate invariant form.
  3776	Write
  3777	$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
  3778	for the genus-completed bar differential
  3779	\textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},
  3780	with $d_\cA^{(0)} = \dzero$ the genus-$0$ bar differential.
  3781	Define the \emph{positive-genus correction}
  3782	\begin{equation}\label{eq:theta-bar-intrinsic}
  3783	\Theta_\cA
  3784	\;:=\;
  3785	D_\cA - \dzero
  3786	\;=\;
  3787	\sum_{g \geq 1} \hbar^g\, d_\cA^{(g)}
  3788	\;\in\;
  3789	\prod_{g \geq 1}
 succeeded in 51ms:
 19240	\index{contact class!stratum separation}
 19241	\index{stratum separation|textbf}
 19242	\index{rank-one abelian rigidity!stratum separation}
 19243	The single-line dichotomy governs
 19244	$r_{\max}|_L \in \{2,3,\infty\}$. The value
 19245	$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
 19246	$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 19247	The cyclic deformation complex decomposes by charge:
 19248	$\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
 19249	For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
 19250	$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 19251	lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 19252	The self-bracket
 19253	$\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
 19254	has $\dim \Defcyc^{(2q)} = 0$ for rank-one systems:
 19255	the quartic pump does not activate, so $r_{\max} = 4$.
 19256	This is rank-one rigidity
 19257	(Theorem~\ref{thm:betagamma-rank-one-rigidity})
 19258	as stratum separation.
 19259	
 succeeded in 51ms:
   916	\index{truncated current algebra!mode bookkeeping only}
   917	Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
   918	\[
   919	V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
   920	\]
   921	Then the weight-$h$ genus-enrichment block of
   922	$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
   923	\[
   924	\mathcal{E}_g^{*,h}
   925	\;\cong\;
   926	\bigoplus_\nu
   927	C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
   928	\otimes_{\bC}
   929	H^1(\Sigma_g,\bC),
   930	\]
   931	where $\nu$ runs over the finitely many mode patterns of total
   932	weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
   933	$\fg$-module with diagonal adjoint action on the $\fg$-labels and
   934	trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
   935	In particular the truncated current algebra $\fg \otimes V_h$
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.

codex
I verified the seven requested surfaces in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2911). Most proof-level findings were already repaired on the current theorem surfaces; the live downstream contradiction was the class-`\mathbf{C}` witness in `thm:shadow-separation`, and I corrected that proof plus the local representative tables/figures so they now consistently use the full `\beta\gamma_\lambda` family. I did not run a full TeX build; verification was by re-reading the touched sections and grep-checking the referenced labels/phrases. The introduction MC2/E1 cross-reference was already correct in [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:2059), so I did not edit outside the assigned file.

## Rectification Summary
- [FIXED] finding 1 — Theorem D already has the non-circular routing remark in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2911): `thm:mc2-bar-intrinsic` builds the shadow tower, `thm:genus-universality` extracts `\mathrm{obs}_g=\kappa\lambda_g`, and `thm:family-index` is explicitly downstream.
- [FIXED] finding 2 — The PBW/Whitehead gap is already closed in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:916) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:971): the weightwise enrichment is rewritten as finite-dimensional `\fg`-modules, and the mixed map is factored through `H^1(\fg,-)` instead of the truncated current algebra.
- [FIXED] finding 3 — MC2 scope is already explicit in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3830): `thm:mc2-bar-intrinsic` is only the coinvariant/symmetric statement, while the ordered `E_1` lift is `thm:e1-mc-element`. The flagged introduction citation was already corrected and needed no new edit.
- [FIXED] finding 4 — The genuswise-product vs completed-tensor identification is already made explicit in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3794) and used again in the proof at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3967), so `\Theta_\cA` is no longer used tacitly as an element of `\Defcyc(\cA)\widehat\otimes\Gmod`.
- [FIXED] finding 5 — The depth-gap proposition is already correctly split in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17609): `\kappa|_L\neq0` lines give `{0,1,\infty}`, and the boundary value `d_{\mathrm{alg}}=2` is isolated to the global `\beta\gamma_\lambda` family.
- [FIXED] finding 6 — I repaired the residual contradiction in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:19478): `thm:shadow-separation` no longer uses the obsolete weight-changing-line witness, and now compares `\cH_1` with `\beta\gamma_1` on the full conformal-weight family. I also propagated that correction through the nearby representative surfaces at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12360), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12433), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:17012), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:19245), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:20355), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:26669), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:30710), and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:35313).
- [FIXED] finding 7 — The ambient `D^2=0` theorem already uses the correct universal-family carrier in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:31745): the proof now explicitly rejects fixed-curve log-FM as insufficient and works over the relative Fulton-MacPherson compactification of the universal stable family over `\overline{\cM}_{g,n}`.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.

tokens used
200,080
