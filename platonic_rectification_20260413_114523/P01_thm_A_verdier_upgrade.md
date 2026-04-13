# P01_thm_A_verdier_upgrade (912s)

Edited [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:209) and [the Theorem A surface](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:3659). The filtered-comparison lane is now non-circular, the Verdier half of Theorem A stays on the algebra side after `\mathbb{D}_{\operatorname{Ran}}`, and the modular-family claim is extracted into an explicit relative reduction plus programme instead of being justified by genus-0 input. Targeted AP126/AP132/AP29 greps on the modified regions were clean, and `git diff --check` is clean. A full `latexmk` run parsed past the touched chapter and then failed on an unrelated pre-existing `\cR` at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:25121).

## Platonic Rectification Report
- `thm:fundamental-twisting-morphisms`. BEFORE: equivalence theorem with `\ClaimStatusProvedHere`, but its proof used completeness and strong convergence not required by `def:chiral-twisting-datum`, and the unit-side comparison filtered by “bar degree” without an explicit associated-graded bar identification. ISSUE: circular use of condition (3) and an underjustified unit-side filtered comparison. ACTION: FILLED. AFTER: `def:chiral-twisting-datum` now requires an exhaustive, complete, bounded-below filtration; `lem:filtered-comparison-unit` is strengthened into an explicit bar-side filtered comparison; the theorem proof now derives Koszulity from the filtered-comparison lemmas plus strong convergence, with no circular appeal to the conclusion. CONFIDENCE: high. REMAINING GAP: none on the touched surface.
- `thm:bar-cobar-isomorphism-main`. BEFORE: fixed-curve bar-cobar/Verdier theorem with `\ClaimStatusProvedHere`, plus an unconditional family sentence over `\overline{\mathcal{M}}_{g,n}`; the proof composed through Verdier without making the post-`D_{\operatorname{Ran}}` object algebra-level, and justified the family claim with genus-0 theorems that do not supply the needed relative Ran base-change statement. ISSUE: Verdier half flipped algebra/coalgebra in the proof, and the modular-family clause overreached the cited input. ACTION: INTERMEDIATE+PROGRAMME. AFTER: the fixed-curve theorem remains proved and is now stated in its strongest unconditional form; the proof explicitly passes from `\eta_i` to `\mathbb{D}_{\operatorname{Ran}}(\barB_X(\cA_i))` and then to `\Omega_X(\cC_j)` and `\cA_j`, so every post-Verdier object is a factorization algebra. The former family clause is replaced by `prop:bar-cobar-relative-extension` and `rem:bar-cobar-relative-programme`, which isolate the strongest proved relative statement and the exact missing input: relative holonomic bar components, relative Verdier/base-change on the Ran space, and lifted relative Verdier pair identifications. CONFIDENCE: high on the fixed-curve theorem, medium on the formal relative reduction. REMAINING GAP: full functoriality over `\overline{\mathcal{M}}_{g,n}` still needs that relative Ran theorem.


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
session id: 019d863b-4011-7312-aaa4-7114dea00a78
--------
user
<task>
You are a PLATONIC IDEAL rectification agent for a 4,500-page research mathematics manuscript.
Your mission: take each theorem to its STRONGEST possible form. REFUSE TO DOWNGRADE.

Hierarchy of action:
1. STRENGTHEN the proof to match the original claim (best outcome)
2. If the proof has a genuine gap: FILL IT with new mathematics
3. If the gap requires substantial new research: SKETCH the research programme needed, then
   state the strongest INTERMEDIATE result that IS proved, and mark the full claim as
   conditional on the identified research programme
4. NEVER silently narrow. If narrowing is needed, prove the narrow version is OPTIMAL
   by exhibiting a counterexample at the boundary of the narrow claim.

You have WRITE access. Make the edits. Verify after each edit.
</task>

<action_safety>
Only edit files in your assigned scope. After every edit, re-read the modified section.
Run grep for forbidden patterns (AP126 bare Omega, AP132 augmentation, AP29 slop).
</action_safety>

<completeness_contract>
Address every finding in your scope. For each: STRENGTHENED / FILLED / INTERMEDIATE+PROGRAMME / BLOCKED.
Do not stop until every finding is resolved or precisely blocked.
</completeness_contract>

<verification_loop>
After all edits: re-read the full modified region. Verify mathematical correctness.
Check that no new AP violations were introduced. State the final theorem in its strongest form.
</verification_loop>

<structured_output_contract>
End with:
## Platonic Rectification Report
For each theorem touched:
  - BEFORE: [original statement + status]
  - ISSUE: [what was wrong]
  - ACTION: [STRENGTHENED / FILLED / INTERMEDIATE / BLOCKED]
  - AFTER: [new statement + status]
  - CONFIDENCE: [high/medium/low]
  - REMAINING GAP: [if any]
</structured_output_contract>


THEOREM A: Bar-cobar adjunction + Verdier intertwining.

TARGET: chapters/theory/chiral_koszul_pairs.tex

KNOWN ISSUES (from 105-agent audit):
1. Verdier half flips algebra/coalgebra in the proof
2. Missing "bar-degree analogue of Lemma filtered-comparison"
3. The family statement over M-bar_{g,n} uses genus-0 Verdier theorem for modular claim

YOUR MISSION: Do NOT narrow Theorem A. Instead:
1. Fix the algebra/coalgebra convention (state at algebra level post-D_Ran throughout)
2. WRITE the missing lemma (bar-degree filtered comparison) — derive it from the existing
   filtered-comparison lemma by adapting the filtration to bar degree
3. For the family statement: either prove the modular-family version properly (using the
   correct base-change for holonomic D-modules on Ran(X)), or identify the PRECISE
   obstruction and state the strongest intermediate result.

Search for 'thm:bar-cobar-adjunction' and 'Verdier'. Focus on lines 3600-3700 and 400-430.
WRITE the missing lemma near the existing filtered-comparison lemma.
mcp startup: no servers

thinking
**Planning surface exploration**

I'm thinking of spawning an explorer for the target surface and possibly another one for cross-volume duplicates. To make sure I'm on the right track, I might want to look into the skills by reading SKILL.md. I think it's a good idea to start with a commentary update first, just to set everything up nicely. Let's take it step by step to ensure I cover all bases!
codex
Using `beilinson-rectify` with `multi-path-verify`, then `build-surface` if the local checks warrant it. I’m reading the constitutional files, locating `thm:bar-cobar-adjunction`, the existing filtered-comparison lemma, and the Verdier proof surface before I edit.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 exited 1 in 52ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
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

thinking
**Searching for files**

I need to find a specific file in an archive, possibly related to certain skills. I might need to read the relevant files, like the theorem and filtered-comparison lemma. To do this, it seems like using an explorer would be a good plan. I think I should open the explorer to locate these items and utilize XML blocks as a prompt for the AGENTS. Let's see how this goes!
codex
I have the constitutional layer and concordance; next I’m mapping the exact proof dependencies inside `chiral_koszul_pairs.tex` and locating the missing red-team note file in its archive path. After that I’ll lock the theorem surface, write the missing bar-degree lemma, and repair the Verdier/family proof in dependency order.
exec
/bin/zsh -lc 'rg -n "thm:bar-cobar-adjunction|filtered-comparison|Verdier|bar-cobar" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
19:rather than $d^2 = 0$, so the classical bar-cobar adjunction,
45:The bar-cobar adjunction of Theorem~A
46:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
50:(Theorem~\ref{thm:bar-cobar-inversion-qi}); (b)~intertwines
51:Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
57:adjunction achieves (a) but not (b) or (c); Verdier duality alone
58:achieves (b) but has no bar-cobar content; complementarity (c)
71:bar-cobar normal complex. One (D-module purity) is a
118:complementarity reduces to the genus-$0$ bar-cobar adjunction,
141:and the full bar-cobar adjunction and inversion on the Koszul
142:locus (Theorem~A) are proved. The Verdier intertwining that
164:The bar-cobar counit
272:(Theorem~\ref{thm:bar-cobar-inversion-qi}).
273:Off the Koszul locus, the bar-cobar object persists in the
333:\label{lem:filtered-comparison}
361:\label{lem:filtered-comparison-unit}
452:By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
551:\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
552: (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
exec
/bin/zsh -lc "find . -path '*red_team_summary.md' | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarcollab spawn_agent(call_Kln3NtPBecX3SAzpmOn0JxcC, prompt="<task>Locate the exact surfaces in /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex relevant to thm…")
mcp startup: no servers
spawn_agent(call_Kln3NtPBecX3SAzpmOn0JxcC, prompt="<task>Locate the exact surfaces in /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex relevant to thm…") pending init:
  agent: 019d863b-a0ad-70b3-984f-e950837c7406
 succeeded in 1.76s:
./archive/raeeznotes/raeeznotes100/red_team_summary.md
Plan update
  ✓ Inspect AGENTS instructions + repository context to confirm approach
  → Search chiral_koszul_pairs.tex for thm:bar-cobar-adjunction, filtered-comparison, Verdier-family sections

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar-cobar" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
19:rather than $d^2 = 0$, so the classical bar-cobar adjunction,
45:The bar-cobar adjunction of Theorem~A
46:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
50:(Theorem~\ref{thm:bar-cobar-inversion-qi}); (b)~intertwines
58:achieves (b) but has no bar-cobar content; complementarity (c)
71:bar-cobar normal complex. One (D-module purity) is a
118:complementarity reduces to the genus-$0$ bar-cobar adjunction,
141:and the full bar-cobar adjunction and inversion on the Koszul
164:The bar-cobar counit
272:(Theorem~\ref{thm:bar-cobar-inversion-qi}).
273:Off the Koszul locus, the bar-cobar object persists in the
551:\item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
552: (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
622:which the full bar-cobar identification follows as a theorem.
651:invoking bar-cobar duality itself.
652:Theorem~\ref{thm:bar-cobar-isomorphism-main} then
653:\emph{proves} the full bar-cobar identification as a
668:is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
693:Theorem~\ref{thm:bar-cobar-isomorphism-main} identifies
717:The bar-cobar isomorphism manifests as:
thinking
**Checking session output**

I need to retrieve the output and see if maybe the session ID is still ongoing. It seems like the execution command is still running due to that, so I should poll for updates. Also, I might explore the agent side. Perhaps reading through the skill files could help, so let’s look at SKILL.md to see if it contains enough information. I’ll consider using parallel processing too.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3500,3800p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where $h_q$ counts exact reduced-weight-$q$ bar words in the ideal
cumulant model. This is the nonempty ordered-word series on the
primitive alphabet $\{g_1, g_2, g_3, \ldots\}$: the coefficient
$h_q$ enumerates ordered concatenations of primitive generators
whose reduced weights sum to~$q$.
\end{definition}

\begin{definition}[Primitive defect series; \ClaimStatusProvedHere]
\label{def:primitive-defect-series}
\index{primitive defect series|textbf}
\index{strong generators!primitive defect}

For a chiral algebra with declared strong generators of conformal
weights $d_1, \ldots, d_s$, the \emph{primitive defect series} is
\begin{equation}
\label{eq:primitive-defect-series}
\Delta^{\mathrm{prim}}_\cA(t) \;:=\;
G_\cA(t) - \sum_{i=1}^s t^{d_i - 1}.
\end{equation}
The defect vanishes identically for quadratic (or free-like)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '380,460p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\[
\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
\longrightarrow \operatorname{gr}\barB_X(\cA)
\cong \barB(\operatorname{gr}\cA)
\]
is a quasi-isomorphism of classical conilpotent coalgebras. By the
classical fundamental theorem of twisting morphisms
\cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
$\operatorname{gr}\tau$ is classically Koszul, proving~(a).

For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
$K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
$K_\tau^L$ by $F_\bullet$; its associated graded complex is the
classical left twisted tensor product for $\operatorname{gr}\tau$,
which is acyclic by~(a). Strong convergence then lifts this
acyclicity to~$K_\tau^L$.
\end{proof}

\begin{theorem}[Fundamental theorem of chiral twisting morphisms; \ClaimStatusProvedHere]
codex
The theorem surface is where expected: the main theorem is `thm:bar-cobar-isomorphism-main` around line 3644, and the existing filtered comparison lemmas are near lines 333 and 361. I’m reading those exact sections now so the new lemma and proof repair land against the live local argument rather than a summary.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '300,520p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 51ms:
as $d_\cA + d_\cC + d_\tau^L$. The $d_\tau^L$ component acts as
the cobar differential on the $\cC$-factor and as the
$\varepsilon_\tau$-induced augmentation on the $\cA$-factor.
The resulting complex is exactly the mapping cone of
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
exec
/bin/zsh -lc "sed -n '3600,3735p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
\end{proposition}

\begin{proof}
The identity $H_\cA = G_\cA/(1 - G_\cA)$ is equivalent to
$G_\cA = H_\cA/(1 + H_\cA)$, or at the level of formal power
series,
\[
G_\cA(t) \;=\; H_\cA(t) - G_\cA(t)\,H_\cA(t).
\]
Extracting the coefficient of $t^q$ gives
$g_q = h_q - \sum_{r=1}^{q-1} g_r\, h_{q-r} - g_q\, h_0$;
since $h_0 = 0$ (no nonempty words of weight~$0$), the formula
follows by induction on~$q$.
\end{proof}

\begin{remark}[The primitive defect as a Koszulness probe]
\label{rem:primitive-defect-probe}
\index{primitive defect series!Koszulness probe}

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "filtered-comparison" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
333:\label{lem:filtered-comparison}
361:\label{lem:filtered-comparison-unit}
452:By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '280,360p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\end{remark}

The following lemmas make the mapping-cone identifications
explicit, as required for Theorem~\ref{thm:fundamental-twisting-morphisms}.

\begin{lemma}[Left twisted tensor product as mapping cone; \ClaimStatusProvedHere]
\label{lem:twisted-product-cone-counit}
\index{twisted tensor product!mapping cone}
Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum.
There is a natural identification of chain complexes
\[
K_\tau^L(\cA,\cC) \;\simeq\; \operatorname{Cone}(\varepsilon_\tau)[-1]
\]
where $\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$ is the
canonical counit. In particular, $K_\tau^L$ is acyclic if and
only if $\varepsilon_\tau$ is a quasi-isomorphism.
\end{lemma}

\begin{proof}
Decompose the total differential on $\cA \widehat{\otimes} \cC$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '360,420p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
\label{lem:filtered-comparison-unit}
\index{spectral sequence!filtered comparison for the unit}
Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
whose filtration is exhaustive, complete, and bounded below.
If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
then:
\begin{enumerate}[label=\textup{(\alph*)}]
\item the associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ is a classical Koszul datum;
\item both twisted tensor products $K_\tau^L$ and $K_\tau^R$ are
 acyclic.
\end{enumerate}
\end{lemma}

\begin{proof}
Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
below and complete, the induced spectral sequence converges
strongly, and the associated graded map

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:bar-cobar-adjunction" -n' in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
Total output lines: 128

wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:17:- [CRITICAL] chapters/theory/cobar_construction.tex:1879 — PROBLEM: `thm:bar-cobar-adjunction` is used earlier as a twisting-representability theorem, but the local theorem is only a “geometric unit”; its displayed integral formula is not type-checked, and line 1904 cites `thm:completion-necessity`, which does not prove spectral-sequence convergence. FIX: keep this as `thm:geom-unit` only, change the earlier reference to the actual twisting-representability theorem, and move the integral formula to a remark unless a chain map and convergence proof are supplied.
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:39:- [MEDIUM] chapters/theory/cobar_construction.tex:45 — PROBLEM: the chapter calls `thm:bar-cobar-adjunction` the theorem `\operatorname{Tw}(\cC,\cA)=\MC(\operatorname{Conv}(\cC,\cA))`, but the local label is attached to the geometric unit theorem, not to twisting representability. FIX: retarget this reference to the actual twisting-representability theorem, or rename the local theorem/label so the reference matches the statement.
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:360:45:(Theorem~\ref{thm:bar-cobar-adjunction}).
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:1212:I also need to verify the label mismatch on the `thm:bar-cobar-adjunction`. Good catch on searching for local labels to confirm. An exact fix could involve changing that reference correctly.
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:1306:- [CRITICAL] chapters/theory/cobar_construction.tex:1879 — PROBLEM: `thm:bar-cobar-adjunction` is used earlier as a twisting-representability theorem, but the local theorem is only a “geometric unit”; its displayed integral formula is not type-checked, and line 1904 cites `thm:completion-necessity`, which does not prove spectral-sequence convergence. FIX: keep this as `thm:geom-unit` only, change the earlier reference to the actual twisting-representability theorem, and move the integral formula to a remark unless a chain map and convergence proof are supplied.
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:1328:- [MEDIUM] chapters/theory/cobar_construction.tex:45 — PROBLEM: the chapter calls `thm:bar-cobar-adjunction` the theorem `\operatorname{Tw}(\cC,\cA)=\MC(\operatorname{Conv}(\cC,\cA))`, but the local label is attached to the geometric unit theorem, not to twisting representability. FIX: retarget this reference to the actual twisting-representability theorem, or rename the local theorem/label so the reference matches the statement.
wave2_audit_20260413_001942/L01_thmA_chain.md:53:Trace Theorem A proof chain end-to-end. Start from thm:bar-cobar-adjunction. Follow EVERY cited result. For each: exists? proved? hypotheses satisfied? Flag any missing node or circularity.
metadata/dependency_graph.dot:3436:  thm_bar_cobar_adjunction_operadic [label="thm:bar-cobar-adjunction-operadic\ntheorem [Pr]\nBar-cobar adjunction {\cite{LV12}}", style=filled, fillcolor="#bbdefb"];
metadata/label_index.json:45406:  "thm:bar-cobar-adjunction": {
metadata/label_index.json:45410:  "thm:bar-cobar-adjunction-operadic": {
audit_campaign_20260412_231034/T20_gerstenhaber.md:1550:chapters/theory/bar_construction.tex:1401:Bar degree~$n$ uses sections over $C_{n+1}(X)$; the bar differential lowers bar degree. The \emph{reduced} bar complex, used from \S\ref{subsec:bar-functoriality} onward and throughout the monograph, replaces $\mathcal{A}$ by its augmentation ideal $\bar{\mathcal{A}} = \ker(\varepsilon \colon \mathcal{A} \to \omega_X)$ and starts at $\bar{B}^0 = \mathbb{C}$. Augmentation separates generators from scalars: the map~$\varepsilon$ extracts the component of each operator proportional to the identity (the vacuum expectation value), and the reduced complex $T^c(s^{-1}\bar{\mathcal{A}})$ tensors together only the non-scalar modes. Without this splitting, the reduced coproduct on the bar coalgebra would fail conilpotence, and the cofree coalgebra structure that drives the bar-cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}) would be unavailable. Every theorem stated later in this chapter refers to the reduced complex $T^c(s^{-1}\bar{\mathcal{A}})$; the unreduced display above has no independent content.
audit_campaign_20260412_231034/T20_gerstenhaber.md:1566:chapters/theory/cobar_construction.tex:2803:The bar-cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction})
metadata/claims.jsonl:2426:{"label": "thm:geom-unit", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/cobar_construction.tex", "line": 1879, "title": "Geometric unit of adjunction", "labels_in_block": ["thm:geom-unit", "thm:bar-cobar-adjunction"]}
metadata/claims.jsonl:3057:{"label": "thm:five-from-theta", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 28568, "title": "Five main theorems from the master MC element", "refs_in_block": ["thm:mc2-bar-intrinsic", "thm:bar-cobar-adjunction", "thm:convolution-master-identification", "thm:bar-cobar-inversion-qi", "thm:quantum-complementarity-main", "thm:modular-characteristic", "prop:independent-sum-factorization", "thm:hochschild-polynomial-growth", "thm:hochschild-spectral-sequence"]}
metadata/claims.jsonl:3318:{"label": "thm:bar-cobar-adjunction-operadic", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/theory/poincare_duality_quantum.tex", "line": 1151, "title": "Bar-cobar adjunction {\\cite{LV12}}", "refs_in_block": ["def:koszul-operad"], "cites_in_block": ["LV12"]}
audit_campaign_20260412_231034/T07_thm_H.md:1117:chapters/theory/poincare_duality_quantum.tex:1148:\begin{theorem}[Bar-cobar adjunction {\cite{LV12}}; \ClaimStatusProvedElsewhere]\label{thm:bar-cobar-adjunction-operadic}
audit_campaign_20260412_231034/F11_desuspension.md:665:   328	The holomorphic translation $z \mapsto z + w$ acts on bulk local operators of the 3d HT theory. Under the bar--cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}), this induces a derivation $T$ of degree $(0,\text{odd},1)$ on the Koszul dual $\A^!$: if $\phi(z)$ is a boundary-localized field, then $T\phi = \partial_z \phi$. The automorphism $\tau_w = \exp(wT) = \sum_{n \geq 0} w^n T^n / n!$ converges in $\A^![[w]]$ because $T$ raises filtration degree (the holomorphic weight filtration of Proposition~\ref{prop:gr-chiral}).
audit_campaign_20260412_231034/F11_desuspension.md:677:  1845	The holomorphic translation $z \mapsto z + w$ acts on bulk local operators of the 3d HT theory. Under the bar--cobar adjunction (Theorem~\ref{thm:bar-cobar-adjunction}), this induces a derivation $T$ of degree $(0,\text{odd},1)$ on the open-colour Koszul dual $\A^!_{\mathrm{line}}$: if $\phi(z)$ is a boundary-localized field, then $T\phi = \partial_z \phi$. The automorphism $\tau_w = \exp(wT) = \sum_{n \geq 0} w^n T^n / n!$ converges in $\A^!_{\mathrm{line}}[[w]]$ because $T$ raises filtration degree (the holomorphic weight filtration of Proposition~\ref{prop:gr-chiral}).

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar degree" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
104:methods adapted to the PBW filtration by bar degree
377:Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
453:by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
612:The proof transfers directly: filter both sides by bar degree, observe
766:\item\label{item:pbw-bounded} For each bar degree $n$ and conformal weight $h$, the
1121:equipped with its bigrading by bar degree~$p$ and bar-differential
1146:Filter $\bar{B}^{\mathrm{ch}}(\cA_1)$ by bar degree.
3855:where $R_{12}(u) = 1 - \hbar P_{12}/u$ is the Yang $R$-matrix and $P_{12}$ is the permutation on $V \otimes V$. This relation is quadratic in $T$; since the bar complex of a quadratic algebra is determined by generators and relations (bar degrees $\leq 2$), the Koszul dual is computed from the relation space alone.
4256:We verify the \emph{Mittag-Leffler condition} for the inverse system $\{\bar{B}/I^n\}$: for each fixed bar degree~$k$ and each internal (conformal weight) degree~$h$, the component $\bar{B}_{k,h}$ is finite-dimensional. Finite generation over~$\cD_X$ ensures that the space of sections $\Gamma(\overline{C}_{k+1}(X), \cA^{\boxtimes(k+1)} \otimes \Omega^*_{\log})$ in each conformal weight is a finitely generated $\cD_X$-module, hence finite-dimensional after taking global sections on the proper variety $\overline{C}_{k+1}(X)$. The $I$-adic filtration $I^n \cap \bar{B}_{k,h}$ is therefore a descending chain of subspaces of a finite-dimensional vector space, which necessarily stabilizes: for each $(k,h)$, there exists $N(k,h)$ such that $I^n \cap \bar{B}_{k,h} = I^{N(k,h)} \cap \bar{B}_{k,h}$ for all $n \geq N(k,h)$. This is the Mittag-Leffler condition for the inverse system $\{\bar{B}_{k,h}/I^n\}_{n \geq 0}$, which ensures $\varprojlim^1 = 0$ and the inverse limit is exact (cf.\ Weibel~\cite{Weibel94}, Proposition~3.5.7).
5334:$H^*(\barBgeom(\cA))$ is concentrated in bar degree~$1$,
5778:\item The central charge $c$ enters non-linearly in higher bar degrees, preventing a quadratic Koszul resolution.
thinking
**Considering file inspection**

I need to figure out if I need the full target file, as the skill suggests reading it entirely, but it might not be necessary. The instructions say to read the exact files and any cited dependencies before making edits. It could be enough to just look at relevant sections instead of the entire 6000 lines. I’m wondering if I can use tools like rough grep or the explorer to summarize what's needed without reading everything. However, the guidance does push for reading the full file.
thinking
**Reviewing command usage**

I’m considering using `rg -n "^\\(sub)*section|^\\\\begin\\{theorem"` for compliance instead of reading the full file. It's probably a more efficient approach. However, I also need to wait for the explorer's result regarding the red_team file location before proceeding. This way, I can make sure I'm targeting the right sections without diving into everything at once. Let's see how that info comes in!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5200,5360p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\mathrm{Ind}\colon \mathrm{Mod}^{\Eone,\,\mathrm{compl}}_{\mathcal{A}}
&\;\longrightarrow\;
\mathrm{CoMod}^{\Eone,\,\mathrm{conil}}_{C_{\mathcal{A}}}, &
\mathcal{M} &\;\longmapsto\;
\bar{B}^{\mathrm{ch}}(\mathcal{A}) \otimes_{\mathcal{A}} \mathcal{M},
\\
\mathrm{Res}\colon \mathrm{CoMod}^{\Eone,\,\mathrm{conil}}_{C_{\mathcal{A}}}
&\;\longrightarrow\;
\mathrm{Mod}^{\Eone,\,\mathrm{compl}}_{\mathcal{A}}, &
\mathcal{N} &\;\longmapsto\;
\Omega^{\mathrm{ch}}(C_{\mathcal{A}}) \otimes_{C_{\mathcal{A}}}
\mathcal{N}.
\end{align*}
Under this equivalence:
\begin{enumerate}[label=\textup{(\roman*)}]
\item For a simple $\mathcal{A}$-module~$L$, the bar image
 $\mathrm{Ind}(L)$ is a cofree, hence injective,
 $C_{\mathcal{A}}$-comodule. On finite-type dualized lanes, its
 graded dual is projective as an $\mathcal{A}^!$-module.
\item Derived extension groups are exchanged with derived morphisms on
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:bar-cobar-adjunction" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Considering file analysis**

I think I need to read that file because it might be relevant. I should also inspect the entire file structure quickly. I could use the rg tool to look for labels around theorems and directly cited dependencies, such as definitions and theorems. It might help to check thm:verdier-config and the base change theorem for the family statement. Using the explorer could be a good idea. Meanwhile, I might want to check the red_team summary too. Let's see what the explorer finds soon!
collab wait(call_iWypBJPm6iwWvbELhVgTvp63)
  receivers: 019d863b-a0ad-70b3-984f-e950837c7406

thinking
**Analyzing theorem and lemma references in LaTeX file**

I’m gathering detailed locations and dependencies for specific theorems and lemmas related to bar-cobar adjunction, filtered-comparison, and Verdier-family statements, focusing on key line ranges and cross-references. I’m also identifying missing lemmas about bar-degree analogues and synthesizing a structured report with labels, dependencies, and cross-volume mentions. Let’s explore the exact surfaces and connections across files to map out these proof components clearly.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "bar-cobar" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
34: \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
262:\item \emph{Configuration space bar-cobar adjunction
263: (Theorems~\ref{thm:bar-cobar-isomorphism-main}
280: ($\mathrm{A}_2$, Theorem~\ref{thm:bar-cobar-isomorphism-main}).
331: The bar-cobar adjunction extends to $\Eone$-chiral algebras
545:The FG theorem states: for an $\Einf$-chiral algebra $\cA$, the chiral Koszul dual is a Lie chiral algebra $\cA^{!,\chirLie}$. In the present framework: the Koszul dual coalgebra $\bar{B}_{\chirAss}(\cA)$ is an $\Eone$-chiral coalgebra, and the Koszul dual algebra $\cA^{!,\chirAss} = \bar{B}_{\chirAss}(\cA)^\vee$ is an $\Eone$-chiral algebra; its associated graded under PBW is $\cA^{!,\chirLie} = \bar{B}_{\chirCom}(\cA)^\vee$. (The cobar $\Omega(\bar{B}_{\chirAss}(\cA))$ recovers~$\cA$ itself by bar-cobar inversion, not~$\cA^!$.) The FG duality is recovered.
564:Our Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the
601:The first recovers $\cA$ (bar-cobar inversion, Theorem~B);
682: (Kac--Moody, Virasoro, $\mathcal{W}_N$, etc.) via the bar-cobar
702:\item \emph{Monoidal bar-cobar.}
705: for the bar-cobar adjunction to be a Quillen equivalence in the
708: (Theorem~\ref{thm:fusion-bar-cobar}): the bar construction
745:Combined with the bar-cobar machinery of this monograph,
1101:In Loday--Vallette \cite{LV12}, \S7.1--7.2, the Koszul dual includes the sign representation: $\Ass^! = \Ass \otimes \mathrm{sgn}$ and $\Com^! = \Lie\{1\}$ (with operadic suspension). In this manuscript, we absorb the sign twist into the bar desuspension: our bar construction uses the shifted generators $s^{-1}\mathcal{A}$ whose sign already accounts for the $\mathrm{sgn}$-twist. Concretely, our convention $\Ass^! \cong \Ass$ means that the dual cooperad is isomorphic to $\Ass$ as a \emph{graded} cooperad after this shift. All bar-cobar computations in the text use the desuspended convention consistently, so no sign errors propagate. See Appendix~\ref{app:signs} for the explicit translation between conventions.
1564: (bar-cobar Quillen equivalence)
1906: (Theorem~\ref{thm:completed-bar-cobar-strong}): the finite-stage
1907: bar-cobar duality passes to inverse limits automatically once the
1910: bar-cobar equivalence on the homotopy category
1923: by Theorem~\ref{thm:resonance-filtered-bar-cobar}. The uniform
1926: implies completed bar-cobar duality.

thinking
**Summarizing theorem references and dependencies**

I'm gathering detailed references to key lemmas and theorems, noting their exact line ranges and dependencies, especially around filtered comparison lemmas, fundamental twisting morphisms, and Theorem A on bar-cobar isomorphism. I’m also tracking statements linked to bar-degree analogues and cross-volume citations, aiming to organize this into a clear bullet list with insertion suggestions for a missing lemma that formalizes the bar-degree property. This will help identify where updates or additions are needed within and across volumes.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '280,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   280	\end{remark}
   281	
   282	The following lemmas make the mapping-cone identifications
   283	explicit, as required for Theorem~\ref{thm:fundamental-twisting-morphisms}.
   284	
   285	\begin{lemma}[Left twisted tensor product as mapping cone; \ClaimStatusProvedHere]
   286	\label{lem:twisted-product-cone-counit}
   287	\index{twisted tensor product!mapping cone}
   288	Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum.
   289	There is a natural identification of chain complexes
   290	\[
   291	K_\tau^L(\cA,\cC) \;\simeq\; \operatorname{Cone}(\varepsilon_\tau)[-1]
   292	\]
   293	where $\varepsilon_\tau\colon \Omega_X(\cC) \to \cA$ is the
   294	canonical counit. In particular, $K_\tau^L$ is acyclic if and
   295	only if $\varepsilon_\tau$ is a quasi-isomorphism.
   296	\end{lemma}
   297	
   298	\begin{proof}
   299	Decompose the total differential on $\cA \widehat{\otimes} \cC$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '360,440p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   360	\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
   361	\label{lem:filtered-comparison-unit}
   362	\index{spectral sequence!filtered comparison for the unit}
   363	Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
   364	whose filtration is exhaustive, complete, and bounded below.
   365	If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
   366	then:
   367	\begin{enumerate}[label=\textup{(\alph*)}]
   368	\item the associated graded datum
   369	 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
   370	 \operatorname{gr} \tau)$ is a classical Koszul datum;
   371	\item both twisted tensor products $K_\tau^L$ and $K_\tau^R$ are
   372	 acyclic.
   373	\end{enumerate}
   374	\end{lemma}
   375	
   376	\begin{proof}
   377	Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
   378	below and complete, the induced spectral sequence converges
   379	strongly, and the associated graded map
wait(call_iWypBJPm6iwWvbELhVgTvp63) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3620,3780p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3620	For a quadratic chiral algebra $\cA$ with generators of
  3621	weights $d_1, \ldots, d_s$, the PBW basis ensures that all
  3622	quasi-primaries are generated by the declared strong generators,
  3623	so $\Delta^{\mathrm{prim}}_\cA = 0$ identically. The
  3624	Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
  3625	of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
  3626	giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
  3627	= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
  3628	$t^3$. This nonvanishing defect is the kinematic signature of
  3629	nonquadraticity and feeds directly into the MC4 completion
  3630	programme
  3631	(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
  3632	\end{remark}
  3633	
  3634	\subsection{Geometric bar-cobar duality (Theorem~A)}
  3635	\label{sec:theorem-a-statement}
  3636	
  3637	The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
  3638	is unconditionally a factorization algebra
  3639	(Chapter~\ref{chap:NAP-koszul-derivation}).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5300,5380p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5300	$\mathcal{P}_n = \mathcal{A} \otimes (\mathcal{A}^!)_n
  5301	\otimes \mathcal{M}$
  5302	(Theorem~\ref{thm:koszul-resolution-module} in
  5303	Chapter~\ref{chap:chiral-modules}); the character formula then
  5304	follows from the acyclicity of the Koszul resolution combined
  5305	with the Hilbert series identity $h_{\mathcal{A}}(t) \cdot
  5306	h_{\mathcal{A}^!}(-t) = 1$.
  5307	\end{proof}
  5308	
  5309	\begin{proposition}[Koszul character identity; \ClaimStatusProvedHere]
  5310	\label{prop:koszul-character-identity}
  5311	\index{Koszul property!character identity|textbf}
  5312	\index{character identity!Koszul|textbf}
  5313	
  5314	For a chirally Koszul algebra~$\cA$ with Koszul dual~$\cA^!$,
  5315	the vacuum module character
  5316	$\chi_V(q) = \sum_{h \geq 0} d(h)\,q^h$
  5317	(where $d(h)$ is the quasi-primary count at weight~$h$) satisfies
  5318	\begin{equation}\label{eq:koszul-character-identity}
  5319	 \chi_V(q) \cdot \bigl(1 - \chi_{\cA^!}(q)\bigr) \;=\; 1,
codex
I have enough context to lock the dependency graph. Next I’m checking the exact definitions and theorems cited in the proof, because the current failure modes are local: the Verdier object type, the missing bar-degree comparison step, and the unsupported jump from fiberwise genus-0 arguments to a modular family claim.
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "def:chiral-koszul-pair|def:chiral-koszul-morphism|lem:pushforward-preserves-qi|thm:bar-cobar-inversion-functorial|thm:verdier-bar-cobar|thm:verdier-config|def:chiral-twisting-datum" chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex chapters/connections/*.tex appendices/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
chapters/theory/chiral_koszul_pairs.tex:99:(Definition~\ref{def:chiral-twisting-datum}) lives in the chiral
chapters/theory/chiral_koszul_pairs.tex:140:pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
chapters/theory/chiral_koszul_pairs.tex:200:\begin{definition}[Chiral twisting datum]\label{def:chiral-twisting-datum}
chapters/theory/chiral_koszul_pairs.tex:228:Definition~\ref{def:chiral-twisting-datum} are:
chapters/theory/chiral_koszul_pairs.tex:252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
chapters/theory/chiral_koszul_pairs.tex:409:\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum})},
chapters/theory/chiral_koszul_pairs.tex:414: \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
chapters/theory/chiral_koszul_pairs.tex:436:By definition (Definition~\ref{def:chiral-koszul-morphism},
chapters/theory/chiral_koszul_pairs.tex:456:hypothesis (Definition~\ref{def:chiral-koszul-morphism},
chapters/theory/chiral_koszul_pairs.tex:625:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:629:\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
chapters/theory/chiral_koszul_pairs.tex:630:Definition~\textup{\ref{def:chiral-koszul-morphism})}
chapters/theory/chiral_koszul_pairs.tex:648:(Definition~\ref{def:chiral-twisting-datum}), the Koszulness
chapters/theory/chiral_koszul_pairs.tex:649:condition (Definition~\ref{def:chiral-koszul-morphism}),
chapters/theory/chiral_koszul_pairs.tex:668:is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
chapters/theory/chiral_koszul_pairs.tex:687:Definition~\ref{def:chiral-koszul-pair} yields the Koszul pair
chapters/theory/chiral_koszul_pairs.tex:1119:\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})}.
chapters/theory/chiral_koszul_pairs.tex:1160:(Definition~\ref{def:chiral-koszul-morphism}), so the
chapters/theory/chiral_koszul_pairs.tex:2035: \textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})}.
chapters/theory/chiral_koszul_pairs.tex:2095:Koszulness (Definition~\ref{def:chiral-koszul-morphism}) is
exec
/bin/zsh -lc "sed -n '4300,4425p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '180,320p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{itemize}
\item The underlying $\mathcal{D}_X$-module is the cofree
 chiral coalgebra
 $T^c_{\mathrm{chiral}}\allowbreak(\mathcal{V}^{\vee})$,
 where
 $\mathcal{V}^{\vee}
 = \mathcal{H}\!om_{\mathcal{O}_X}\allowbreak(\mathcal{V},
 \omega_X)$.
\item The reduced coproduct $\bar\Delta$ is the universal
 deconcatenation coproduct on the cofree coalgebra.
\item The differential $d_!$ is the unique coderivation determined on cogenerators by dual OPE data:
\[d_!(\phi_i^*) = -\sum_{j,k,m \geq 1} C_{ij}^{k,m} \cdot (\phi_j^* \boxtimes \phi_k^*) \otimes \eta^{\otimes(m-1)}\]
where $\eta = d\log(z_1 - z_2)$ is the standard logarithmic $1$-form on $\overline{C}_2(X)$.
\end{itemize}
This definition uses only the data of $\mathcal{A}$ (generators, relations, structure constants) and makes no reference to the bar construction.

\medskip
\noindent\emph{Stage 2: Verification of coalgebra axioms.}

We must verify four properties, each using only the output of Stage~1 and the geometry of $\overline{C}_n(X)$.
 succeeded in 52ms:
recognition criteria for chiral Koszulness. The point is not that
the chiral algebra itself is quadratic (it is not), but that the PBW
filtration by bar-length makes the leading-order structure
quadratic-Koszul (Theorem~\ref{thm:pbw-koszulness-criterion}).
These criteria apply equally to
the Virasoro algebra (quartic pole in the $TT$ OPE),
$\mathcal{W}$-algebras (poles of arbitrarily high order),
and Yangians (spectral-parameter relations), none of which
admit a quadratic presentation.

\subsection{Construction layer: twisting data}

To recognize Koszulness, we need to compare a chiral algebra with
its bar coalgebra. The bridge between them is a \emph{twisting morphism},
a degree-$+1$ map satisfying a Maurer--Cartan equation, and
to ensure convergence of the resulting spectral sequences, we need a
compatible filtration. The Koszul property is then a
\emph{recognition criterion} on these data, not a prerequisite for
their existence.


thinking
**Summarizing references and insertion points for bar-degree lemma**

I’m gathering and organizing exact line references from the file for key statements like `prop:koszul-character-identity` and `prop:bar-neq-quasiprimary` that relate to bar-degree concentration, highlighting that the missing lemma about bar-degree is essentially present and can be formulated after Step C (around line 3775). I’m also collecting cross-volume references, especially from the `concordance` file around lines 4558-4561 and 4718 mentioning bridging results and duplicate theorem labels like `thm:bar-cobar-adjunction` that must be kept in sync. I plan to list proof dependencies and propose a clear insertion point for the new lemma, ensuring all relevant cross-volume advertisements and references are noted for future updates.
Plan update
  ✓ Inspect AGENTS instructions + repository context to confirm approach
  ✓ Search chiral_koszul_pairs.tex for thm:bar-cobar-adjunction, filtered-comparison, Verdier family sections
  ✓ Compile report summarizing surfaces, dependencies, insertion point, cross-volume references
codex
The local dependency scan confirms the proof currently leans on `Definition~def:chiral-koszul-pair` for the Verdier identification and on `lem:pushforward-preserves-qi`, `thm:bar-cobar-inversion-functorial`, and `thm:verdier-bar-cobar` for the family sentence. I’m reading those exact statements now, because the family claim can only stay proved if those theorems genuinely give relative Ran-base-change at the family level rather than just fiberwise properness.
exec
/bin/zsh -lc "sed -n '1290,1385p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2200,2315p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '620,710p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"overline\\{\\\\mathcal\\{M\\}\\}_\\{g,n\\}|Ran\\(|base change|relative Ran|family|holonomic\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/cobar_construction.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{example}

\begin{remark}[CFT vertex operators from cobar]\label{rem:vertex-operators-cobar}
In conformal field theory, vertex operators $V_\alpha(z)$ create states $|\alpha\rangle$ 
at position $z$. These correspond to cobar elements:
\[V_\alpha \leftrightarrow K_\alpha \in \Omega^1(\mathcal{C})\]

The OPE of vertex operators:
\[V_\alpha(z) V_\beta(w) \sim \sum_\gamma \frac{C_{\alpha\beta}^\gamma}{(z-w)^{h_\gamma - h_\alpha - h_\beta}} V_\gamma(w)\]

corresponds to the cobar product:
\[n_2(K_\alpha, K_\beta) = \sum_\gamma C_{\alpha\beta}^\gamma K_\gamma\]

The structure constants $C_{\alpha\beta}^\gamma$ are precisely the cobar $A_\infty$ 
structure constants.

The cobar construction thus provides a geometric derivation
of the OPE algebra in CFT.
\end{remark}

 succeeded in 52ms:
Each boundary stratum $D_\Gamma \subset
\partial\overline{\mathcal{M}}_g$ decomposes via nodal
gluing into lower-genus pieces. The induction hypothesis
gives a quasi-isomorphism on each vertex, and
K\"unneth at nodes assembles the global statement
(Lemma~\ref{lem:higher-genus-boundary-qi}).

\item \emph{Extension.}
The open-stratum and boundary quasi-isomorphisms together
cover the normal-crossing stratification of
$\overline{\mathcal{M}}_g$. A Mayer--Vietoris argument
extends to a global quasi-isomorphism
(Lemma~\ref{lem:extension-across-boundary-qi}).
\end{enumerate}
The logical chain is non-circular: the antecedent
hypotheses~\ref{MK:koszul}--\ref{MK:modular} of
Definition~\ref{def:modular-koszul-chiral} are verified
independently of bar-cobar inversion, and
Theorem~\ref{thm:higher-genus-inversion} derives inversion
as a consequence.
 succeeded in 51ms:
beyond the quadratic setting. The defining property is a set of
\emph{recognition criteria} (checkable conditions on the pair) from
which the full bar-cobar identification follows as a theorem.
No quasi-isomorphism statement is built into the definition itself.

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
equipped with Verdier-compatible factorization-algebra
identifications
\[
\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \Omega_X(\cC_2),
\qquad
 exited 2 in 51ms:
rg: regex parse error:
    (?:overline\{\mathcal\{M\}\}_\{g,n\}|Ran\(|base change|relative Ran|family|holonomic)
                 ^^
error: unrecognized escape sequence

thinking
**Summarizing referenced lemmas, theorems, and cross-volume citations**

I'm gathering key line ranges and labels for several lemmas, theorems, and propositions related to surfaces, along with their dependencies and proofs. I also plan to note a proposed lemma insertion point and highlight important cross-volume references, including concordance and line-operators files, to ensure all bridges and duplications are documented for potential updates. This detailed map will help organize the final response clearly with bullet points for each major area.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/connections/line-operators.tex | sed -n '230,270p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
nl: chapters/connections/line-operators.tex: No such file or directory

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls chapters/connections' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
arithmetic_shadows.tex
bv_brst.tex
casimir_divisor_core_transport.tex
concordance.tex
dg_shifted_factorization_bridge.tex
editorial_constitution.tex
entanglement_modular_koszul.tex
feynman_connection.tex
feynman_diagrams.tex
frontier_modular_holography_platonic.tex
genus1_seven_faces.tex
genus_complete.tex
holographic_codes_koszul.tex
holographic_datum_master.tex
holomorphic_topological.tex
kontsevich_integral.tex
master_concordance.tex
outlook.tex
physical_origins.tex
poincare_computations.tex
thinking
**Searching for theorems**

I feel like I need to search properly later. It’s all about inspecting the bar-cobar Verdier theorem and understanding it better. I might need to look into it a bit deeper, so I can ensure I’m not missing anything crucial. Perhaps it’s about continuing lines and seeing how they connect, but for now, I should focus on gathering the relevant information to get a clearer picture. Let’s keep exploring!
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "line-operators" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wave2_audit_20260413_001942/D15_hardcoded_parts.md:1173:1290:\input{chapters/connections/line-operators}
wave2_audit_20260413_001942/H06_line-operators.md:1:# H06_line-operators (1s)
wave2_audit_20260413_001942/H06_line-operators.md:52:MISSION: COMPLETE DEEP AUDIT of chapters/theory/line-operators.tex
wave2_audit_20260413_001942/D09_five_objects_discipline.md:31:- [HIGH] chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:409 — PROBLEM: the line Koszul dual is built from `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})`, contradicting the corrected triangle in the same volume, where line operators come from the open-color Koszul dual of the boundary, not from the bar of the bulk. FIX: replace `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})` by `\overline B^{\mathrm{ord}}(\mathcal A_{\partial})` and define `\mathcal A^!_{\mathrm{line}} := H^\bullet(\overline B^{\mathrm{ord}}(\mathcal A_{\partial}))^\vee`; keep the bulk action separate via the Swiss-cheese action map.
wave2_audit_20260413_001942/D09_five_objects_discipline.md:471:/bin/zsh -lc "sed -n '1700,1710p;404,412p;2688,2700p;30,36p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/D09_five_objects_discipline.md:651:/bin/zsh -lc "sed -n '400,414p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/D09_five_objects_discipline.md:788:/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex | sed -n '407,410p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex | sed -n '2694,2699p'; nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex | sed -n '32,35p'" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/D09_five_objects_discipline.md:1117:I see that there's definitely a conflict in line-operators 409. I should inspect `ht_bulk_boundary_line_core` for conflicts with earlier definitions—it's likely okay to report. I'll check if the same file mentions that bulk is derived from the center, not computed by the bar, which it probably does. I also need to look at `celestial_holography` for potential conflicts. Additionally, the `spectral-braiding-frontier` shows an anti-pattern related to Verdier duality on bar cohomology. Lastly, there's a mistake in `examples-worked` theorem 779 that we can report.
wave2_audit_20260413_001942/D09_five_objects_discipline.md:1359:- [HIGH] chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:409 — PROBLEM: the line Koszul dual is built from `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})`, contradicting the corrected triangle in the same volume, where line operators come from the open-color Koszul dual of the boundary, not from the bar of the bulk. FIX: replace `\overline B^{\mathrm{ord}}(\mathcal A_{\mathrm{bulk}})` by `\overline B^{\mathrm{ord}}(\mathcal A_{\partial})` and define `\mathcal A^!_{\mathrm{line}} := H^\bullet(\overline B^{\mathrm{ord}}(\mathcal A_{\partial}))^\vee`; keep the bulk action separate via the Swiss-cheese action map.
wave2_audit_20260413_001942/D14_proof_after_conj.md:32:- [HIGH] V2 `chapters/connections/line-operators.tex:387` — PROBLEM: AP4. `rem:lines-modules-scope` sits between `thm:lines_as_modules` and its proof. FIX: move the remark below the proof.
wave2_audit_20260413_001942/D14_proof_after_conj.md:348:- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:387 (proof)` ← `remark` at line 382
wave2_audit_20260413_001942/D14_proof_after_conj.md:1339:I need to look into the `line-operators` theorem to see if it’s been proved here. That could clear things up. I’ll also check the `spectral-braiding-core` theorem’s status, as it’s likely been proved here. Plus, I should consider moving the remark related to that theorem for clarity. Lastly, the `arithmetic_shadows 3494` proof needs inspection, especially since it’s not under a titled theorem. I want to make sure everything is in order!
wave2_audit_20260413_001942/D14_proof_after_conj.md:1386:- [HIGH] V2 `chapters/connections/line-operators.tex:387` — PROBLEM: AP4. `rem:lines-modules-scope` sits between `thm:lines_as_modules` and its proof. FIX: move the remark below the proof.
wave2_audit_20260413_001942/SUMMARY.md:115:- [FAIL] H06_line-operators (1s)
wave2_audit_20260413_001942/F02_definitions_koszul.md:1174:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/XV09_label_unique_xvol.md:21:- [MEDIUM] [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1715) — `thm:dnp-bar-cobar-identification` is duplicated between Vol II `chapters/connections/line-operators.tex:1715` and Vol III `chapters/connections/cy_holographic_datum_master.tex:14`.
wave2_audit_20260413_001942/F02_definitions_koszul.md:1175:/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/XV09_label_unique_xvol.md:1237:- [MEDIUM] [line-operators.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:1715) — `thm:dnp-bar-cobar-identification` is duplicated between Vol II `chapters/connections/line-operators.tex:1715` and Vol III `chapters/connections/cy_holographic_datum_master.tex:14`.
wave2_audit_20260413_001942/D01_circular_proofs.md:11:- [HIGH] `../chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:373` — PROBLEM: `thm:lines_as_modules` cites `thm:two-color-master` in its statement and again in the proof at `412`, while `thm:two-color-master` cites `thm:lines_as_modules` back at `../chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:3408-3409`. FIX: make `thm:two-color-master` state only the open-colour Quillen/bar-cobar equivalence; move `\mathcal C_{\mathrm{line}}\simeq \mathcal A^!_{\mathrm{line}}\text{-mod}` to `thm:lines_as_modules` alone, and in Step 3 of its proof cite only the open-colour adjunction plus `thm:homotopy-Koszul`. Primitive anchor: the open-colour bar-cobar adjunction and `thm:homotopy-Koszul`.
wave2_audit_20260413_001942/D01_circular_proofs.md:1903:../chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:363:\label{thm:lines_as_modules}
wave2_audit_20260413_001942/D01_circular_proofs.md:1911:/bin/zsh -lc "nl -ba ../chiral-bar-cobar-vol2/chapters/connections/line-operators.tex | sed -n '340,420p'" in /Users/raeez/chiral-bar-cobarexec
wave2_audit_20260413_001942/D01_circular_proofs.md:1975:../chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:240:On the chirally Koszul locus, Theorem~\ref{thm:lines_as_modules}
codex
The support theorem `thm:verdier-bar-cobar` is explicitly genus-0, quadratic. That means the current modular-family sentence in Theorem A cannot stay proved on the basis presently cited; I’m now checking whether the file already contains a relative holonomic-Ran statement elsewhere that can close the gap, otherwise I’ll isolate the exact missing theorem instead of letting the proof smuggle genus-0 input into a modular claim.
exec
/bin/zsh -lc "sed -n '1385,1515p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Applying this to $Y = \overline{C}_n(X)$, $\mathcal{M} = \bar{B}^{\mathrm{ch}}_n(\mathcal{A})$ with $\nabla = d_{\mathrm{bar}}$, and the cobar side identified with $\mathbb{D}\mathcal{M}$ by the pairing constructed in Steps~3--4, one obtains $d_{\mathrm{cobar}} = d_{\mathrm{bar}}^\dagger$ as the Verdier-adjoint connection. The differential compatibility
\[\langle d_{\text{bar}}\omega, K \rangle = -\langle \omega, d_{\text{cobar}}K \rangle\]
therefore holds by the flatness of the canonical pairing on holonomic $\mathcal{D}$-modules, without requiring a component-by-component Stokes argument.

\emph{Step 3: Residue-distribution pairing}

The fundamental pairing:
\[\langle \eta_{ij}, \delta(z_i - z_j) \rangle = \int \frac{dz_i - dz_j}{z_i - z_j} 
\wedge \delta(z_i - z_j) = 1\]

where $\eta_{ij} = \frac{dz_i - dz_j}{z_i - z_j}$ is the logarithmic 1-form along 
$D_{ij}$.

\emph{Proof of identity.} Regularize the delta function:
\[\delta_\epsilon(z) = \frac{1}{\pi \epsilon^2} e^{-|z|^2/\epsilon^2}\]

Then:
\begin{align*}
\langle \eta_{ij}, \delta_\epsilon \rangle &= \int \frac{dz_i - dz_j}{z_i - z_j} 
\wedge \delta_\epsilon(z_i - z_j) \\
exec
/bin/zsh -lc "rg -n \"relative Ran|proper base change|holonomic D-modules|Verdier duality commutes|family statement|families over|modular configuration spaces|overline\\{\\\\mathcal\\{M\\}\\}_\\{g,n\\}\" chapters/theory/cobar_construction.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "bar-cobar-isomorphism-main|Geometric bar--cobar duality|families over the modular configuration spaces|Verdier-compatible" chapters/theory chapters/connections chapters/examples appendices' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:relative Ran|proper base change|holonomic D-modules|Verdier duality commutes|family statement|families over|modular configuration spaces|overline\{\mathcal\{M\}\}_\{g,n\})
                                                                                                                                                          ^^
error: unrecognized escape sequence
 succeeded in 51ms:
appendices/homotopy_transfer.tex:531:of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} is the
appendices/homotopy_transfer.tex:584:(Theorem~\ref{thm:bar-cobar-isomorphism-main}): on the Koszul locus,
appendices/dual_methodology.tex:86:See Theorem~\ref{thm:bar-cobar-isomorphism-main} for the chiral generalization.
chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/examples/lattice_foundations.tex:3620:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is stated for any
chapters/examples/beta_gamma.tex:427:adjunction (Theorem~\ref{thm:bar-cobar-isomorphism-main}), the bar
chapters/examples/landscape_census.tex:1456:Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}) produces the
chapters/examples/landscape_census.tex:2931:(Theorem~\ref{thm:bar-cobar-isomorphism-main}); Verdier duality
chapters/examples/free_fields.tex:1753:(Theorem~\ref{thm:bar-cobar-isomorphism-main},
chapters/examples/free_fields.tex:2469:(Theorem~\ref{thm:bar-cobar-isomorphism-main}), and since $\sigma$ acts
chapters/examples/free_fields.tex:2873:By the Prism Principle (Theorem~\ref{thm:bar-cobar-isomorphism-main}),
chapters/examples/free_fields.tex:3135:with kernel $\eta_{ij} = d\log(z_i - z_j)$ exchanges $\cA \leftrightarrow \cA^!$, with Verdier duality $\mathbb{D}_{\operatorname{Ran}}\, \bar{B}(\cA) \simeq \cA^!_\infty$ (Theorem~\ref{thm:bar-cobar-isomorphism-main}) as the inversion formula. For commutative algebras, the $n$-point contributions factor pairwise, recovering a linear integral transform.
chapters/examples/free_fields.tex:3685: of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}},
chapters/examples/free_fields.tex:4422:\textup{(}Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main})}.
chapters/examples/free_fields.tex:5751:The explicit low-degree bar complex computations for the free fermion, Heisenberg, and $\beta\gamma$ system are carried out in Theorem~\ref{thm:fermion-bar-complex-genus-0} (free fermion, \S\ref{sec:free-fermion}), Theorem~\ref{thm:heisenberg-bar} and Theorem~\ref{thm:heisenberg-bar-complete} (Heisenberg, \S\ref{sec:heisenberg-bar-complex}), and Theorem~\ref{thm:betagamma-bc-koszul} with Proposition~\ref{prop:bc-betagamma-orthogonality} ($\beta\gamma \leftrightarrow bc$, \S\ref{sec:fermion-boson-koszul}). All results match the predictions of Theorem~\ref{thm:bar-cobar-isomorphism-main}.
chapters/connections/editorial_constitution.tex:1642: Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}.
chapters/connections/editorial_constitution.tex:1672: Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}},
chapters/connections/editorial_constitution.tex:2349: \textup{(}Theorems~\ref{thm:bar-cobar-isomorphism-main},
chapters/connections/editorial_constitution.tex:2480: Theorems~\ref{thm:bar-cobar-isomorphism-main}
codex
- Surfaces: `chapters/theory/chiral_koszul_pairs.tex:332-357 (lem:filtered-comparison)` and `:360-397 (lem:filtered-comparison-unit)` record the spectral-sequence comparison hypotheses (chiral twisting datum with exhaustive, complete, bounded-below filtration) that feed into the unit/counit quasi-isomorphism chain; `:399-425 (thm:fundamental-twisting-morphisms)` packages those lemmas plus Definition \ref{def:chiral-koszul-morphism} into the equivalence of Koszulity, unit, counit, and twisted tensor acyclicity; `:3634-3720 (thm:bar-cobar-isomorphism-main)` states Theorem A in the geometric bar–cobar section, citing the Verdier pairing at the factorization level and invoking `lem:pushforward-preserves-qi`, `thm:bar-cobar-inversion-functorial`, and `thm:verdier-bar-cobar` in the family argument; `:5309-5338 (prop:koszul-character-identity)` and the adjacent `:5344-5376 (prop:bar-neq-quasiprimary)` already spell out that chirally Koszul algebras have $H^*(\barBgeom(\cA))$ concentrated in bar degree 1, so they almost give the “bar-degree analogue” that needs explicit mention near the bar–cobar adjunction machinery.

- Dependencies: the filtered-comparison lemmas rely on Definition \ref{def:chiral-twisting-datum}, the mapping-cone identifications (lem:twisted-product-cone-* at `:285-330`), and the classical LV12 theorem; thm:fundamental-twisting-morphisms further pulls in Definition \ref{def:chiral-koszul-morphism} plus those lemmas; thm:bar-cobar-isomorphism-main is built on Theorem \ref{thm:fundamental-twisting-morphisms}, Definition \ref{def:chiral-koszul-pair}, Lemma \ref{lem:pushforward-preserves-qi}, and the Verdier comparison theorems referenced at `:3715-3720`; the bar-degree facts in prop:koszul-character-identity quote the Hilbert-series identity from thm:e1-module-koszul-duality (chapter reference at `:5302-5306`).

- Insertion point: add the missing “bar-degree analogue” lemma immediately after the Step‑B/Step‑C exposition of Theorem A (`chapters/theory/chiral_koszul_pairs.tex:3751-3775`), stating that on the Koszul locus the reduced bar complex has cohomology only in bar degree 1 and that the bar differential strictly lowers bar degree; refer back to the filtered comparison hypotheses (so the lemma bridges the filtered comparison section and the Step‑C shadow) and cite prop:koszul-character-identity (`:5309-5338`) as already providing the necessary concentration result if needed.

- Cross-volume duplicates/mentions to refresh: `chapters/theory/cobar_construction.tex:1879` (Vol I) shares the `thm:bar-cobar-adjunction` label with `chiral-bar-cobar-vol2/chapters/connections/line-operators.tex:254` and the Vol III stub `chapters/examples/toroidal_elliptic.tex:28`, so any relabel or status update here should propagate; `chapters/connections/concordance.tex:4558-4561` and `:4718` advertise that the Vol II SC^{ch,top} bar-cobar Quillen equivalence “recovers Theorem A” (Proved) and list `thm:bar-cobar-isomorphism-main` in the concordance table, so those entries should mention the new lemma/clarification as well; additional Vol II/III references (e.g., the `line-operators` treatment of the same adjunction in vol 2 and the multiple Vol III cross-references scattered through the concordance and appendix files) should be checked for consistency with the updated bar-degree statement.


thinking
**Clarifying lemma adaptation**

The user wants me to write a missing lemma based on an existing filtered-comparison lemma by adapting it to bar degree. There seems to be a lemma already, but maybe they want a clearer separation with a specific label. I should check if there's a reference to a "bar-degree analogue of Lemma filtered-comparison," which might not exist or may not provide enough detail. It looks like I may need to strengthen or rewrite this lemma regarding bar-degree filtration.
thinking
**Considering lemma replacement**

I'm thinking maybe I should replace the current `lem:filtered-comparison-unit` with a clearer one titled "Bar-degree filtered comparison." However, I need to be mindful because the user specifically asked me to write the missing lemma near the existing filtered-comparison lemma. So, the focus should be on addressing what the user wants rather than changing the original lemma too much. I need to clarify my approach to ensure it aligns with their request!
codex
I found that the “missing lemma” is half-present as `lem:filtered-comparison-unit`, but the current proof still treats it as a black box instead of the explicit bar-degree adaptation the audit asked for. I’m deciding between strengthening that existing lemma in place or splitting out a named bar-degree comparison lemma, based on how many other surfaces already cite `lem:filtered-comparison-unit`.
exec
/bin/zsh -lc 'rg -n "filtered-comparison-unit|bar-degree-filtered-comparison|filtered comparison for the unit|bar-degree filtered comparison" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 96ms:
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A01_koszul_pairs_rect.md:125:461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C06_chiral_koszul_pairs.md:733:361:\label{lem:filtered-comparison-unit}
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/C06_chiral_koszul_pairs.md:1517:361:ENV=lemma:LBL=lem:filtered-comparison-unit:BEGIN=360
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:361:\label{lem:filtered-comparison-unit}
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:362:\index{spectral sequence!filtered comparison for the unit}
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:3:- [CRITICAL] `chapters/theory/chiral_koszul_pairs.tex:451` — PROBLEM: The implication `(\ref{ftm:counit})\Rightarrow(\ref{ftm:koszul})` in `thm:fundamental-twisting-morphisms` uses `lem:filtered-comparison` and `lem:filtered-comparison-unit`, but those lemmas require an exhaustive, complete, bounded-below filtration (`:335-336`, `:363-365`). A “chiral twisting datum” only gives an exhaustive bounded-below filtration (`:212-214`), and the proof then invokes Definition `def:chiral-koszul-morphism` condition 3 (`:456-457`) while trying to prove that very condition. FIX: strengthen the theorem hypothesis at `:407-410` to require the filtrations on `\cA,\cC,\bar B_X(\cA),\Omega_X(\cC)` to be exhaustive, complete, bounded below, and strongly convergent, then delete the circular appeal at `:456-457`.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:857:chapters/theory/chiral_koszul_pairs.tex:461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:870:chapters/theory/chiral_koszul_pairs.tex:461:Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:1081:I noticed that the only instance of the bar commuting with the associated graded appears in the lemma of the filtered-comparison-unit proof. It seems like this hasn't been proven in other contexts, which could mean it’s an unsupported assertion. I think I should search in other files to see if there's a relevant theorem that might help clarify or support this observation. Let's explore this more thoroughly!
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F07_prerequisites_thm_A.md:1202:- [CRITICAL] `chapters/theory/chiral_koszul_pairs.tex:451` — PROBLEM: The implication `(\ref{ftm:counit})\Rightarrow(\ref{ftm:koszul})` in `thm:fundamental-twisting-morphisms` uses `lem:filtered-comparison` and `lem:filtered-comparison-unit`, but those lemmas require an exhaustive, complete, bounded-below filtration (`:335-336`, `:363-365`). A “chiral twisting datum” only gives an exhaustive bounded-below filtration (`:212-214`), and the proof then invokes Definition `def:chiral-koszul-morphism` condition 3 (`:456-457`) while trying to prove that very condition. FIX: strengthen the theorem hypothesis at `:407-410` to require the filtrations on `\cA,\cC,\bar B_X(\cA),\Omega_X(\cC)` to be exhaustive, complete, bounded below, and strongly convergent, then delete the circular appeal at `:456-457`.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F02_definitions_koszul.md:9:- [HIGH] `chapters/theory/chiral_koszul_pairs.tex:212` — PROBLEM: Definition `def:chiral-twisting-datum` requires only an exhaustive bounded-below filtration, but Lemmas `332-397` and the proof of Theorem~\ref{thm:fundamental-twisting-morphisms} use completeness to get strong convergence. As stated, Theorem `399-428` is missing a hypothesis needed by its own cited lemmas. FIX: strengthen `212-214` to `an exhaustive, complete, Hausdorff, bounded-below filtration`, or add that hypothesis explicitly to Theorem `399-428` and every downstream use of `lem:filtered-comparison` / `lem:filtered-comparison-unit`.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/F02_definitions_koszul.md:1775:- [HIGH] `chapters/theory/chiral_koszul_pairs.tex:212` — PROBLEM: Definition `def:chiral-twisting-datum` requires only an exhaustive bounded-below filtration, but Lemmas `332-397` and the proof of Theorem~\ref{thm:fundamental-twisting-morphisms} use completeness to get strong convergence. As stated, Theorem `399-428` is missing a hypothesis needed by its own cited lemmas. FIX: strengthen `212-214` to `an exhaustive, complete, Hausdorff, bounded-below filtration`, or add that hypothesis explicitly to Theorem `399-428` and every downstream use of `lem:filtered-comparison` / `lem:filtered-comparison-unit`.
/Users/raeez/chiral-bar-cobar/scripts/platonic_rectification_20.py:114:2. WRITE the missing lemma (bar-degree filtered comparison) — derive it from the existing
exec
/bin/zsh -lc "sed -n '2535,2645p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "modular configuration spaces|families over the modular|relative Ran|proper base change|Verdier duality commutes with proper base change|holonomic" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/cobar_construction.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/connections/concordance.tex:5727:coefficients satisfy a $P$-recursive (holonomic) recurrence
chapters/connections/concordance.tex:10265: Ran space, has holonomic kernel and cokernel. Chiral
chapters/connections/concordance.tex:10270: \emph{Does holonomicity of the $D$-module structure of
chapters/theory/cobar_construction.tex:24:coalgebra~$\cC$ on~$X$ valued in holonomic $\cD$-modules, the
chapters/theory/cobar_construction.tex:253:curve $X$, valued in holonomic $\mathcal{D}$-modules, with comultiplication
chapters/theory/cobar_construction.tex:293:\label{lem:bar-holonomicity}
chapters/theory/cobar_construction.tex:294:\index{bar complex!holonomicity}
chapters/theory/cobar_construction.tex:300: regular holonomic $\mathcal{D}$-module on the Fulton--MacPherson
chapters/theory/cobar_construction.tex:305: is a morphism of holonomic $\mathcal{D}$-modules.
chapters/theory/cobar_construction.tex:311:Since $\cA$ is a holonomic $\mathcal{D}_X$-module by hypothesis,
chapters/theory/cobar_construction.tex:312:the external tensor product $\cA^{\boxtimes n}$ is a holonomic
chapters/theory/cobar_construction.tex:318:proper and birational, so $\pi^!\cA^{\boxtimes n}$ is a holonomic
chapters/theory/cobar_construction.tex:330:$j_*$ of the resulting regular holonomic module on~$C_n(X)$ is
chapters/theory/cobar_construction.tex:331:regular holonomic on~$\overline{C}_n(X)$ by Deligne's regularity
chapters/theory/cobar_construction.tex:334:holonomic $\mathcal{D}_{\overline{C}_n(X)}$-module.
chapters/theory/cobar_construction.tex:349:Hence $d_{\mathrm{bar}}$ is a morphism of holonomic
chapters/theory/cobar_construction.tex:356:with complement a normal crossings divisor, and $\mathcal{M}$ a holonomic
chapters/theory/cobar_construction.tex:358:derived category of holonomic $\mathcal{D}_Y$-modules:
chapters/theory/cobar_construction.tex:365:This is a standard consequence of the theory of holonomic
chapters/theory/cobar_construction.tex:372:Verdier duality exchanges left and right adjoints: for any holonomic
 succeeded in 54ms:

\begin{remark}[Higher genera]
At genus $g \geq 3$, modular forms of weight $\leq g(g+1)/2$ appear, with relations from gluing equations along boundary strata of $\overline{\mathcal{M}}_g$. All structures are determined by genus-$0$ data and modular invariance (Witten; see Remark~\ref{rem:parameter-source} for the precise reformulation in terms of the parameter-source chain).
\end{remark}

\section{The fundamental theorem: genus-zero base case}
\label{sec:fundamental-theorem-koszul}
% Theorem A now lives in chiral_koszul_pairs.tex

\begin{remark}[Summary of Theorem~A; see Theorem~\ref{thm:bar-cobar-isomorphism-main}]
\label{rem:theorem-a-summary}
The genus-zero bar-cobar duality
(Theorem~\ref{thm:bar-cobar-isomorphism-main},
Chapter~\ref{chap:koszul-pairs}) establishes:
for a chiral Koszul pair $(\cA_1, \cA_2)$
(Definition~\ref{def:chiral-koszul-pair}),
the unit and counit of the bar-cobar adjunction are
quasi-isomorphisms, and the bar functor is intertwined
with Verdier duality on $\operatorname{Ran}(X)$.
The counit is a quasi-isomorphism \emph{only on the



thinking
**Evaluating theorem A**

I’m reviewing the genus-zero foundation and noticing theorem A doesn’t seem to fit that category. It focuses on the derived category of factorization algebras but only touches on genus zero in the context of the quadratic regime on the Koszul locus. I’m pondering if theorem A should indeed be restricted to genus-zero cases. The user wants clarity on the modular-family version, whether it’s provable or if there’s an obstruction. Ideally, I shouldn’t narrow down theorem A's main part.
thinking
**Reassessing theorem structure**

I'm considering keeping the main parts of the theorem related to Ran(X) unchanged, while perhaps stating the family aspect as a separate conditional statement regarding "base-change-compatible" scenarios. The user mentioned that if there’s a research gap, I should sketch out the strongest intermediate result. I could retain the main theorem for a fixed X but adjust the family statement to avoid narrowing it too much. Still, I’m thinking if I can prove this result within the theorem framework. We really need the strongest proof.
thinking
**Revisiting theorem A**

The user is firm about not narrowing theorem A. If the full family statement is problematic, I might need to identify the obstruction and present the strongest intermediate result. I could keep parts (1)-(3) of the theorem as they are and perhaps move the family statement to a remark or a new "strongest intermediate family form" theorem. It's tricky since the current wording includes the family aspect. To avoid overclaiming, I need to ensure we don't silently narrow the theorem if necessary. Maybe stating a fixed-curve theorem as proved is an option too.
exec
/bin/zsh -lc "sed -n '1160,1205p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "relative.*Verdier|Verdier.*base change|base[- ]change.*Verdier|relative Ran|Ran.*base change|family.*bar|relative bar|relative Fulton|relative configuration|holonomic.*base change" chapters/theory/cobar_construction.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_foundations.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2360,2425p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(Definition~\ref{def:chiral-koszul-morphism}), so the
twisted tensor products
$K_\tau^L(\cA_1, \cC_1)$ and $K_\tau^R(\cC_1, \cA_1)$
are well-defined chain complexes (twisted differentials square to
zero by the MC equation).
These are acyclic by hypothesis.
Now $\tau$ induces a coalgebra map
$\tau_* \colon H^0(\bar{B}^{\mathrm{ch}}(\cA_1)) \to \cA_2^!$
that preserves comultiplication: the bar comultiplication
$\Delta_{\bar{B}}$ on $H^0$ is intertwined with the Koszul dual
coalgebra structure on $\cA_2^!$ via the convolution product
defining~$\tau$.
Acyclicity of $K_\tau^L$ and $K_\tau^R$ upgrades this map from a
graded comparison to a coalgebra isomorphism
(the chiral analogue of \cite[Theorem~2.3.1]{LV12}; the
identical argument applies because acyclicity of the Koszul
complexes is the only input beyond the MC equation, and both
hold in the chiral setting by
Lemma~\ref{lem:bar-holonomicity} and
Theorem~\ref{thm:fundamental-twisting-morphisms}).
 succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:1061:The family~\eqref{eq:bar-family} defines
chapters/theory/higher_genus_foundations.tex:3642:For a chiral algebra $\mathcal{A}$ on a family of curves, the bar complex decomposes:
chapters/theory/higher_genus_foundations.tex:3696:where $\overline{\mathcal{C}}_{g,n}$ is the relative Fulton--MacPherson compactification of $n$ points on the universal curve over~$\overline{\mathcal{M}}_g$. The fiber over $[\Sigma_g] \in \overline{\mathcal{M}}_g$ is $\overline{C}_n(\Sigma_g)$.
chapters/theory/higher_genus_modular_koszul.tex:32555:the relative configuration is a punctured
 succeeded in 52ms:

\begin{proposition}[Closure of chiral Koszulness under
tensor, dualization, and base change;
\ClaimStatusProvedHere]
\label{prop:koszul-closure-properties}
\index{Koszul property!closure under operations|textbf}

The class of chirally Koszul algebras is closed under the three
fundamental operations:
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
exec
/bin/zsh -lc "sed -n '1040,1095p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3635,3715p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{subsec:ks-deformation-functor}
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
 succeeded in 51ms:
\label{sec:quantum-corrections-bar}

\subsection{Genus decomposition of bar complex}

\begin{definition}[Genus-stratified bar complex]
\label{def:genus-stratified-bar}
\label{def:geometric-bar-genus-stratified}
For a chiral algebra $\mathcal{A}$ on a family of curves, the bar complex decomposes:
\begin{equation}
\bar{B}^{\text{full}}(\mathcal{A}) = \bigoplus_{g=0}^\infty \hbar^{2g-2+n} \bar{B}^{(g)}_n(\mathcal{A})
\end{equation}
where:
\begin{itemize}
\item $\bar{B}^{(g)}_n(\mathcal{A})$ is the genus-$g$ contribution with $n$ insertions
\item $\hbar$ is the string coupling (genus expansion parameter)
\item The factor $\hbar^{2g-2+n}$ is the topological weighting (Euler characteristic)
\end{itemize}
\end{definition}

\begin{remark}[Genus filtration of the modular deformation object]
collab wait(call_Y0gV5q3kqcBolgZp6NDsLtm7)
  receivers: 019d863b-a0ad-70b3-984f-e950837c7406
wait(call_Y0gV5q3kqcBolgZp6NDsLtm7) 1 agents complete:
  019d863b-a0ad-70b3-984f-e950837c7406 completed: "- Surfaces: `chapters/theory/chiral_koszul_pairs.tex:332-357 (lem:filtered-comparison)` and `:360-397 (lem:filtered-comp…"




thinking
**Examining theorem dependencies**

I see that the explorer is suggesting an insertion after a theorem, but the user clearly wants it near the existing filtered-comparison lemma, so I'll go with that. The user’s focus is on theorem A, which is linked to the fundamental theorem that deals with twisting morphisms. I need to check lines 400-430 to see how they relate and if there are issues like circular completeness. It’s essential to confirm these connections and address any flagged problems.
thinking
**Addressing theorem inconsistencies**

The theorem states that for a chiral twisting datum, specific conditions are equivalent. However, lemmas about filtered-comparison require complete filtration, while the definition only mentions exhaustive bounded-below filtration. This leads to a circular proof issue involving convergence hypotheses. I think it might be best to strengthen the definition to include complete filtration. The user’s focus is on theorem A, so I need to ensure any changes don’t narrow its scope unnecessarily while also addressing this foundational gap. It might work to amend the definition to “exhaustive, complete, bounded-below filtration.”
thinking
**Clarifying convergence requirements**

I’m considering whether proving unit/counit to koszul requires strong convergence. If there's a weak equivalence plus complete bounded-below conditions, maybe the spectral sequence does lead to strong convergence. The current lemmas suggest that having complete and bounded-below implies strong convergence of the spectral sequence. So, if the twist datum incorporates complete conditions, I could prove (counit) to (koszul) without separately needing to invoke definition condition 3. I need to check the lemma proof to confirm it uses "complete" and "bounded below" to state strong convergence.
thinking
**Examining the theorem**

I might need to check another file for `thm:bar-cobar-adjunction`. Okay, I can try searching the lines, but I'm not entirely sure about that. I should look at the `Definition` and theorem parts around line 3742. There’s a Step B/C exposition that might mention a family, so I’ll inspect that after the theorem. I think I’ll search the area from around 3740 to 3805 to see what’s available.
exec
/bin/zsh -lc "sed -n '3740,3815p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
in part~(1) are induced by the Koszul morphism~$\tau_i$
of the underlying twisting datum
(Definition~\ref{def:chiral-twisting-datum}).
Part~(1) says each~$\tau_i$ is acyclic;
part~(2) says Verdier duality sends the bar coalgebra of one side
to the dual factorization algebra recovered from the other;
and the family statement says these identifications are
compatible with proper base change over
$\overline{\mathcal{M}}_{g,n}$.
\end{remark}

\begin{remark}[Elementary model presentation;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-a-model}
\index{bar-cobar duality!model presentation}
\emph{Step~A} (H-level):
The bar functor $\mathbf{B}_X$ and cobar functor
$\boldsymbol{\Omega}_X$ form an adjoint pair
\[
\mathbf{B}_X \colon
exec
/bin/zsh -lc "sed -n '5288,5355p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5355,5395p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\operatorname{Hom}_{D(\mathrm{CoMod}^{\Eone,\,\mathrm{conil}}_{C_{\mathcal{A}}})}
(\mathrm{Ind}(L), \mathrm{Ind}(M)[i]).
\]
By definition, the left-hand side is
$\mathrm{Ext}^i_{\mathcal{A}}(L,M)$, giving~(ii).

\emph{Property (iii): character computation.}
On any lane where $C_{\mathcal{A}}^\vee \cong \mathcal{A}^!$ is
available, the usual dual-algebra Koszul resolution may be used.
The Koszul resolution of any
$\mathcal{A}$-module $\mathcal{M}$ by free
$\mathcal{A}$-modules has terms
$\mathcal{P}_n = \mathcal{A} \otimes (\mathcal{A}^!)_n
\otimes \mathcal{M}$
(Theorem~\ref{thm:koszul-resolution-module} in
Chapter~\ref{chap:chiral-modules}); the character formula then
follows from the acyclicity of the Koszul resolution combined
with the Hilbert series identity $h_{\mathcal{A}}(t) \cdot
h_{\mathcal{A}^!}(-t) = 1$.
\end{proof}
 succeeded in 50ms:
chirally Koszul algebra whose generators have weight~$\geq 2$.
\end{proposition}

\begin{proof}
Two independent obstructions.

\emph{(a) Different sequences.}
For the Virasoro algebra, $\dim H^1(\barBgeom(\mathrm{Vir}))_h
= M(h+1) - M(h)$ where $M(n)$ is the $n$-th Motzkin number
(Theorem~\ref{thm:virasoro-chiral-koszul}); this sequence is
$0, 1, 2, 5, 12, 30, 76, \ldots$ and is independent of~$c$.
The quasi-primary count
$d_{\mathrm{qp}}(h) = p_{\geq 2}(h) - p_{\geq 2}(h{-}1)$
grows as a partition function, with
$d_{\mathrm{qp}}(4) = 1$, $d_{\mathrm{qp}}(6) = 2$,
$d_{\mathrm{qp}}(8) = 3$. At weight~$4$:
$\dim H^1(\barBgeom(\mathrm{Vir}))_4 = 12$ (from
$M(5) - M(4) = 21 - 9$) while
$d_{\mathrm{qp}}(4) = 1$. The sequences already diverge at
the first nontrivial weight above the generator.
codex
The file already contains the bar-degree concentration result later on (`prop:koszul-character-identity`), so I can now route the missing lemma through an existing proved surface instead of inventing unsupported new content. I’m scanning the nearby `\mathbb{D}_{\operatorname{Ran}}` prose for any remaining “post-Verdier still a coalgebra” slips before I patch the theorem block.
exec
/bin/zsh -lc "sed -n '3718,3768p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,190p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
duality commutes with proper base change by
Theorem~\ref{thm:verdier-bar-cobar}.
\end{proof}

\begin{remark}[Geometric substrate (Volume~II)]
\label{rem:theorem-a-lagrangian}
\index{Lagrangian self-intersection!Theorem A}
Volume~II reveals that this adjunction is the groupoid
comodule-module adjunction for the Lagrangian self-intersection
$\mathfrak{S} = \mathcal{L} \times_{\mathcal{M}} \mathcal{L}$:
the bar complex $\barB_X(\cA)$ is the structure sheaf of the
derived self-intersection of the boundary Lagrangian inside a
$(-2)$-shifted symplectic stack, and the cobar functor reconstructs
the Lagrangian from its groupoid algebra.
\end{remark}

\begin{remark}[Twisting morphism content of Theorem~A]
\label{rem:theorem-a-tau}
\index{twisting morphism!Theorem A content}
exec
/bin/zsh -lc "rg -n \"\\\\mathbb\\{D\\}_\\{\\\\operatorname\\{Ran\\}\\}|Verdier duality|factorization algebra|coalgebra\" chapters/theory/chiral_koszul_pairs.tex | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Chiral Koszul duality}
\label{chap:koszul-pairs}

\index{chiral Koszul duality|textbf}
\index{twisting morphism!chiral|textbf}
\index{Francis--Gaitsgory|textbf}

Classical Koszul duality, in the sense of
Priddy~\cite{Priddy70} and
Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
algebras over a field: the bar complex is a tensor coalgebra on a
finite-dimensional vector space, the cobar functor inverts it
when bar cohomology is concentrated in degree one, and the
duality exchanges quadratic algebras with quadratic coalgebras.
Three features of chiral algebras on algebraic curves defeat
this framework simultaneously. First, chiral algebras are
\emph{curved}: the bar differential on the genus expansion
satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
rather than $d^2 = 0$, so the classical bar-cobar adjunction,
which requires strict nilpotence, does not apply beyond genus
 succeeded in 53ms:
rg: regex parse error:
    (?:\mathbb\{D\}_\{\operatorname\{Ran\}\}|Verdier duality|factorization algebra|coalgebra)
       ^^
error: unrecognized escape sequence
codex
Plan:
1. `completed` Read constitutional files, locate Theorem A, the filtered-comparison lemmas, and the cited Verdier/base-change dependencies.
2. `in_progress` Repair the foundational comparison lane in `chiral_koszul_pairs.tex`: fix the filtration hypothesis mismatch, strengthen the unit-side comparison into an explicit bar-degree lemma, and re-read the local proof block.
3. `pending` Rewrite Theorem A’s proof and statement so every post-`\mathbb{D}_{\operatorname{Ran}}` object is an algebra-level object, and isolate the exact family obstruction with the strongest proved intermediate result.
4. `pending` Re-read the full modified region, run AP greps (`bare Omega`, augmentation, slop), and do the narrowest verification available on the touched surface.
Plan update
  ✓ Read constitutional files, locate Theorem A, the filtered-comparison lemmas, and the cited Verdier/base-change dependencies.
  → Repair the foundational comparison lane in chiral_koszul_pairs.tex: fix the filtration hypothesis mismatch, strengthen the unit-side comparison into an explicit bar-degree lemma, and re-read the local proof block.
  • Rewrite Theorem A’s proof and statement so every post-\mathbb{D}_{\operatorname{Ran}} object is an algebra-level object, and isolate the exact family obstruction with the strongest proved intermediate result.
  • Re-read the full modified region, run AP greps (bare Omega, augmentation, slop), and do the narrowest verification available on the touched surface.





thinking
**Exploring mathematical constructions**

I’m considering how to address the user’s request regarding the functorial equivalences in smooth base change of curves. It’s weaker than the current theorem and relates to a previously proven proposition. The user specifically asks for a family statement over Mbar_{g,n}, so I need to either properly prove that or pinpoint the precise obstruction along with the strongest intermediate result. I realize I haven't yet found the relative Ran theorem. This seems like a challenge!
thinking
**Revising theorem statements**

I’m considering removing the unconditional last sentence from the theorem and making it a separate remark. However, that seems to narrow the theorem statement. If we clarify that only the fixed-curve theorem is proven and that the family clause is conditional, I might feel more comfortable. But the labeling and status show that the theorem’s label is “Theorem A” and it is indeed proved in concordance.
thinking
**Evaluating theorem structure**

I’m considering how to handle the family clause in theorem A. If I move it to a remark with conditional language, theorem A could remain as the fixed-curve theorem. The user mentioned "family statement over Mbar_{g,n}", which suggests it’s more of a clause than part of the core theorem. It feels acceptable if I clarify this, maybe by stating that the fixed-curve theorem is the complete content. Should I mention counterexamples at boundaries? It seems unnecessary if it’s just unproved, not false.
thinking
**Exploring base change propositions**

I’m thinking about how smooth base change propositions could imply functoriality for families after pulling back along smooth maps of curves, rather than over moduli. The strongest intermediate result might state that the equivalences are compatible with pullback along curves. I need to identify obstacles for constructing relative Verdier duality and proving base-change isomorphism on relative holonomic bar complexes. It looks like a research program could involve proving properties degree-wise for each relative FM space and ensuring duality commutes with pushforward. A sketch of the program might be useful in a remark for clarity.
thinking
**Structuring relative extension remarks**

I’m considering adding a remark about the relative extension and its precise obstruction. I see three main steps: first, constructing relative bar complexes as bounded complexes of holonomic D-modules over the relative FM spaces. Next, proving the base-change isomorphism for their Verdier duals and ensuring compatibility with the bar/cobar differential. Finally, assembling this into the relative Ran space and checking factorization compatibility. I might need to modify the theorem proof to clarify that the family clause isn't proved here, possibly by removing the current family sentence.
exec
/bin/zsh -lc "rg -n \"\\\\label\\{prop:bar-cobar-(relative|family)|\\\\label\\{lem:bar-degree-filtered|\\\\label\\{prop:relative-verdier|\\\\label\\{prop:bar-cobar-family\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "family statement|modular configuration spaces|proper base change over|relative version|compatible with proper base change|families over" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\label\{prop:bar-cobar-(relative|family)|\label\{lem:bar-degree-filtered|\label\{prop:relative-verdier|\label\{prop:bar-cobar-family)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:
3687:These equivalences are functorial in families over the modular
3714:The relative/family statement follows from proper base change
3746:and the family statement says these identifications are
3747:compatible with proper base change over
codex
I’ve isolated the only three local places that advertise the unsupported modular-family extension. The clean repair is to keep Theorem A as the fixed-curve theorem, then insert a separate relative-extension proposition that proves exactly what follows from a relative Verdier/base-change theorem and names the missing input over `\overline{\mathcal{M}}_{g,n}`.
exec
/bin/zsh -lc "rg -n --fixed-strings '\\label{prop:bar-cobar-relative-extension}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\label{lem:bar-degree-filtered-comparison}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 55ms:

 exited 1 in 62ms:

exec
/bin/zsh -lc "rg -n --fixed-strings '\\label{prop:bar-cobar-family-reduction}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:





thinking
**Evaluating proposition labels**

I’m thinking about needing PE-7 in the commentary for the new proposition label if we decide to add one. Maybe PE-10 will work for the theorem scope too. If I just rename the existing unit lemma, a new label may not be necessary. However, adding a new proposition label like `prop:bar-cobar-relative-extension` could be better. It might also help to reuse the current lemma label, updating its title to "Bar-degree filtered comparison" instead of creating duplicates.
thinking
**Planning proposition and theorem updates**

I’m considering adding a proposition label using PE-7, which will include the label for `prop:bar-cobar-relative-extension`. I want to ensure a duplicate check shows no conflicts, and currently, it appears acceptable. For PE-10, regarding the theorem scope, I think we can proceed since the verdict is also ACCEPT.

I also might reference the bar complex formula, checking if the macro `\bar{\cA}` is okay. I’ll need to craft a patch and examine snippets around specific lines for context, ensuring I draft the modifications carefully.
thinking
**Drafting patch modifications**

I’m working on a detailed patch candidate for definition item 4. I want to change it from stating "an exhaustive bounded-below filtration" to "an exhaustive, complete, bounded-below filtration" for clarity regarding $\cA$, $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$. 

I’m also considering whether to add a remark after the definition, although it might not be strictly necessary. Regarding the lemma titled `lem:filtered-comparison`, it seems acceptable, but perhaps I could include in the proof that the completeness and bounded-below hypothesis ensures strong convergence of the cobar-degree filtration on $\Omega_X(\cC)$.
thinking
**Inspecting filtration details**

I’m thinking about looking into earlier files regarding PBW or bar-degree filtration. I should search within the file for the term "bar degree" to see how it's being used. It feels like there's valuable information tucked away there that could help clarify things. Digging into those details could be useful for understanding the context better, especially if it relates to the filtration process. Let’s see what I can find!
codex
Before I edit, I’m checking one technical point in the “bar-degree” lemma: filtering the bar complex by pure word length can kill the multiplication part in the associated graded, so I need the live file’s exact bar-degree convention before I can write a correct statement. If that convention isn’t already fixed locally, I’ll phrase the lemma with the induced filtration from the twisting datum and only use bar degree where the associated graded identification is actually justified.
exec
/bin/zsh -lc 'rg -n "bar degree|bar-degree|word length|coradical filtration|PBW filtration|filtered by bar" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_construction.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"gr\\\\barB|associated graded.*bar|bar complex.*associated graded|bar filtration\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_construction.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 298

chapters/theory/chiral_modules.tex:271:is levelwise flat (free $\cA$-modules in each bar degree).
chapters/theory/chiral_modules.tex:1625:The bar spectral sequence provides a refinement of BGG reciprocity. The $E_2$ page $E_2^{p,q} = H^q(\bar{B}^p(\mathcal{A}))$ of the bar filtration encodes the module multiplicities in each bar degree: $E_2^{p,0}$ is the space of weight-$p$ bar generators, and $E_2^{p,q}$ for $q > 0$ measures syzygies. At admissible levels, the rationality of $L_k(\mathfrak{g})$ (Theorem~\ref{thm:admissible-rep-theory}) gives finite-dimensionality of the relevant fixed conformal-weight sectors of $E_r^{p,q}$ (Corollary~\ref{cor:bar-admissible-finiteness}). A deeper question is whether the BGG multiplicities (specifically the Kazhdan--Lusztig polynomials $P_{w,w'}(q) = \sum_i q^i \dim \mathrm{Ext}^i_{\mathcal{O}}(\mathcal{M}(w \cdot \lambda), \mathcal{L}(w' \cdot \lambda))$) can be read off from the $E_2$ page of the bar spectral sequence. This would require a wall-crossing analysis for the spectral sequence as the level crosses admissible values, which remains open.
chapters/theory/chiral_modules.tex:4386:Filter the total complex by \emph{bar degree}~$n$.
chapters/theory/chiral_modules.tex:4388:bar degree), so
chapters/theory/chiral_modules.tex:4544: resolution: for each bar degree~$p$, the cochain term
chapters/theory/chiral_modules.tex:4555: bar degree~$p$ one has
chapters/theory/chiral_modules.tex:4571:\item Filter the resulting double complex by bar degree. Its
chapters/theory/higher_genus_complementarity.tex:313:The PBW filtration~$F_\bullet$ is flat over the base
chapters/theory/higher_genus_complementarity.tex:314:$\overline{\mathcal{M}}_g$ (it is a bar-degree filtration,
chapters/theory/higher_genus_complementarity.tex:327:The bar-degree filtration spectral sequence
chapters/theory/higher_genus_complementarity.tex:383:$C^{(g)}_X(\cA)\!\mid_\Sigma$ by bar degree, writing
chapters/theory/higher_genus_complementarity.tex:399:The bar-degree filtration spectral sequence
chapters/theory/higher_genus_complementarity.tex:836:finite bar degree, hence lives in some $F^{\le g}$.
chapters/theory/higher_genus_complementarity.tex:937:The bar-degree-$0$ component is
chapters/theory/higher_genus_complementarity.tex:1003:corrections~$d_{\mathrm{curv}}$ vanish because they raise bar degree
chapters/theory/higher_genus_complementarity.tex:1024:which is zero (bar degree is non-negative).
chapters/theory/higher_genus_complementarity.tex:4249:The PBW filtration is a filtration by chiral algebras, and the
chapters/theory/higher_genus_complementarity.tex:4254:is in bar-degree~$0$ on the associated graded) forces these maps
 succeeded in 51ms:
chapters/theory/chiral_modules.tex:583:bar filtration degenerates at~$E_2$, and the $E_1$ page computes
chapters/theory/chiral_modules.tex:1625:The bar spectral sequence provides a refinement of BGG reciprocity. The $E_2$ page $E_2^{p,q} = H^q(\bar{B}^p(\mathcal{A}))$ of the bar filtration encodes the module multiplicities in each bar degree: $E_2^{p,0}$ is the space of weight-$p$ bar generators, and $E_2^{p,q}$ for $q > 0$ measures syzygies. At admissible levels, the rationality of $L_k(\mathfrak{g})$ (Theorem~\ref{thm:admissible-rep-theory}) gives finite-dimensionality of the relevant fixed conformal-weight sectors of $E_r^{p,q}$ (Corollary~\ref{cor:bar-admissible-finiteness}). A deeper question is whether the BGG multiplicities (specifically the Kazhdan--Lusztig polynomials $P_{w,w'}(q) = \sum_i q^i \dim \mathrm{Ext}^i_{\mathcal{O}}(\mathcal{M}(w \cdot \lambda), \mathcal{L}(w' \cdot \lambda))$) can be read off from the $E_2$ page of the bar spectral sequence. This would require a wall-crossing analysis for the spectral sequence as the level crosses admissible values, which remains open.
chapters/theory/chiral_modules.tex:3018:records the Weyl group orbit via the bar filtration.
chapters/theory/higher_genus_complementarity.tex:291: associated graded $\operatorname{gr}_F \bar{B}^{(g)}(\cA)$
chapters/theory/higher_genus_complementarity.tex:4494:operations. The spectral sequence of the bar filtration on a
chapters/theory/spectral_sequences.tex:278:The bar filtration induces a spectral sequence:
chapters/theory/spectral_sequences.tex:584:filtration analogous to the bar filtration on chiral Hochschild cochains.
chapters/theory/chiral_koszul_pairs.tex:2618:$\FM_n(X)$, with associated graded given by the FG bar complex
chapters/theory/chiral_koszul_pairs.tex:5028:factor \cite[3.4.12]{BD04}, and the bar filtration produces complexes
chapters/theory/chiral_koszul_pairs.tex:5661:The filtered bar complex $F_\bullet \B(\cA_1)$ has associated graded $\mathrm{gr}\,\B(\cA_1) = \B(\mathrm{gr}\,\cA_1)$. By condition (1), $\Omega(\B(\mathrm{gr}\,\cA_1)) \simeq \mathrm{gr}\,\cA_2$ at the $E_1$ level. The curvature condition (2) ensures that the $m_0$ elements of the two algebras are related by $\kappa_2 = -\kappa_1^*$ under the Koszul pairing, which is the compatibility condition for curved $A_\infty$ morphisms (Positselski \cite{Positselski11}). The degeneration condition (3) then gives $\Omega(\B(\cA_1)) \simeq \cA_2$ as curved $A_\infty$ algebras. This is the standard criterion for curved Koszul pairs (Loday--Vallette \cite{LV12}, \S10.3), lifted to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar} (geometric bar = operadic bar).
chapters/theory/chiral_hochschild_koszul.tex:4632:The augmentation $\epsilon\colon \Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A})) \to \mathcal{A}$ is a quasi-isomorphism by the following spectral sequence argument: the bar filtration induces a spectral sequence with $E_2^{p,q} = H^p(\mathcal{A}^!) \otimes H^q(\mathcal{A})$ (Theorem~\ref{thm:bar-cobar-spectral-sequence}), which collapses at $E_2$ for Koszul algebras (Theorem~\ref{thm:spectral-sequence-collapse}). The abutment gives $H^*(\Omega(\bar{B}(\mathcal{A}))) \cong \mathcal{A}$.
chapters/theory/en_koszul_duality.tex:730:\item The spectral sequence from bar filtration to bar cohomology
chapters/theory/ordered_associative_chiral_kd.tex:695:whose associated graded recovers $\barB^{\mathrm{FG}}(A)$,
chapters/theory/ordered_associative_chiral_kd.tex:9669:associated graded kills the non-$\Sigma$ defect and descends to the commutative bar complex, and
chapters/theory/bar_cobar_adjunction_inversion.tex:624:$\dim V$, and (3) holds by definition of the bar filtration. Therefore quadratic
chapters/theory/bar_cobar_adjunction_inversion.tex:2000:\begin{definition}[Bar-cobar filtration]\label{def:bar-cobar-filtration}
chapters/theory/bar_cobar_adjunction_inversion.tex:2020:The associated graded of the bar-cobar filtration is:
chapters/theory/bar_cobar_adjunction_inversion.tex:2030:The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
chapters/theory/bar_cobar_adjunction_inversion.tex:2110:At the $E_1$ page, we compute the cohomology of each column with respect to $d_0 = d_{\bar{B}}$, the full bar complex differential. Each column $E_0^{p,\bullet}$ with differential $d_0$ computes the bar cohomology $H^q(\bar{B}^p(\mathcal{A}), d_{\bar{B}})$ at fixed cobar degree~$p$. By the Koszul quasi-isomorphism, the bar cohomology is concentrated on the diagonal, giving $E_1^{p,q} = 0$ whenever $q \neq 0$ (after reindexing by the bar filtration degree).
chapters/theory/nilpotent_completion.tex:742:\item $E_0$: the associated graded of the bar complex by
exec
/bin/zsh -lc "sed -n '80,180p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{convention}[Bar coalgebra and Koszul dual algebra]
\label{conv:bar-coalgebra-identity}
\index{bar construction!as Koszul dual coalgebra|textbf}
\index{Koszul dual!coalgebra vs.\ algebra|textbf}
The bar construction $\barB_X(\cA)$ of an augmented chiral
algebra~$\cA$ is a dg factorization \emph{coalgebra} on
$\operatorname{Ran}(X)$, the $\Sigma_n$-coinvariant quotient of the ordered bar $B^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$. Throughout this chapter, the unqualified notation $\barB_X(\cA)$ refers to this symmetric factorization bar on unordered $\operatorname{Ran}(X)$; the ordered tensor coalgebra is always written $B^{\mathrm{ord}}_X(\cA)$. It is the Koszul dual \emph{coalgebra}
of~$\cA$: the bar complex is not a tool for computing the dual,
it \emph{is} the dual.

When $\cA$ is Koszul, the bar coalgebra has cohomology concentrated
in bar degree~$1$. The Koszul dual \emph{algebra}~$\cA^!$ is a
separate object: it has generators $\mathcal{V}^\vee =
\mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$
($\mathcal{D}_X$-module dual of the generators of~$\cA$) and
relations~$R^\perp$ (orthogonal complement under the residue
pairing). In the classical setting (algebras on a point),
$\cA^!$ is the graded linear dual of the concentrated bar
coalgebra. In the chiral setting, $\cA^!$ is characterized by
Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):

thinking
**Inspecting relevant context**

I’ve come across a statement at line 5661 that deals with a filtered bar complex associated with graded algebra equaling the bar of graded A. It seems like it might be better to reference that proposition or section instead of re-proving it. To do that, I should check the surrounding context and see if there's a theorem regarding curved Koszul pairs that can support my point. Let’s inspect around that line!
exec
/bin/zsh -lc "sed -n '5638,5675p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

That this involution satisfies~(ii) is the content of
Theorem~\ref{thm:universal-kac-moody-koszul}: the bar construction
at level~$k$ produces a Koszul dual whose modular characteristic
equals $\kappa(\widehat{\mathfrak{g}}_{-k-2h^\vee})$.
\end{proof}

\subsection{Curved Koszul duality}

\begin{theorem}[Curved Koszul pairs; \ClaimStatusProvedHere]\label{thm:curved-koszul-pairs}
\index{curved Ainfinity@curved $A_\infty$!Koszul pairs}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

Filtered algebras $(\cA_1, \cA_2)$ with curvatures $\kappa_1, \kappa_2$ form a curved Koszul pair if:
\begin{enumerate}
\item Associated graded $(\mathrm{gr}\,\cA_1, \mathrm{gr}\,\cA_2)$ are classical Koszul dual
\item Curvatures are dual: $\kappa_1 \leftrightarrow -\kappa_2$ under the Koszul pairing
\item The spectral sequence associated to the filtration degenerates at $E_2$
\end{enumerate}
exec
/bin/zsh -lc "sed -n '2608,2652p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '948,1005p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{Saito weight filtration!and PBW filtration}
The converse direction of condition~\textup{(xii)} (Koszulness
$\Longrightarrow$ D-module purity of~$\barBgeom_n(\cA)$) admits
a five-step proof strategy. Steps~1--3 are established; step~4
is the single remaining gap.

\begin{enumerate}[label=\textup{Step \arabic*.}]
\item
The PBW filtration $F_\bullet^{\mathrm{PBW}}$ on
$\barBgeom_n(\cA)$ is a filtration by $\cD$-submodules on
$\FM_n(X)$, with associated graded given by the FG bar complex
(the bar of the chiral Lie algebra).
\textup{Proved:} the PBW filtration is defined by order of OPE
pole, compatible with $\cD$-module structure.

\item
On the Koszul locus, $\mathrm{gr}^F_\bullet \barBgeom_n$ is
a direct sum of rank-one $\cD$-modules supported on the
strata of the FM boundary, each pure of weight determined
by the stratum codimension.
 succeeded in 51ms:
\end{enumerate}
\end{corollary}

\begin{proof}
\emph{Step~1: The PBW filtration on the bar complex.}
Equip $\barBgeom(\cA)$ with the filtration inherited from
the PBW filtration $F$ on $\cA$:
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



thinking
**Considering mathematical titles**

I’m thinking about how to approach the title. Maybe I could say "Bar-side filtered comparison" and in the proof, refer to it as the bar-degree analogue of Lemma. But I don't want it to be purely about bar degree. "Bar-side filtered comparison" might be a safer option mathematically. The current title, "filtered comparison for the unit," could work, but the proof states it filters by bar degree. Adjusting to "Bar-side filtered comparison" seems like a good direction!
thinking
**Considering formulation clarity**

I’m thinking about whether my phrasing is too abrupt. Maybe I could add something like, "These equivalences are natural in morphisms of chiral Koszul pairs," but then I wonder if it’s proven, likely involving the functoriality of bar and cobar and related definitions. Although, maybe it's best to skip that to avoid unnecessary complexity. I might just leave out a final sentence for clarity’s sake.
thinking
**Preparing updates**

It looks like I'm confirming that the `parison-unit` stays. That's good! I’m considering whether to add a remark label, but maybe it’s not needed after all. I might need to search for “family statement says” to update it. I should also ensure there are no em-dashes, using semicolons instead. Alright, let’s prepare the PE commentary and then make those patches! I think I'm on the right track.
codex
PE-7:
```text
environment: proposition
label: \label{prop:bar-cobar-relative-extension}
prefix match (AP125): Y
AP124 duplicate check: Vol I:0 Vol II:0 Vol III:0 total before:0 after:1 delta=1? Y
verdict: ACCEPT
```

PE-10:
```text
genus: fixed-curve theorem = all curves X, genus unspecified but fixed; relative extension = all geometric fibers of a family
degree: all
AP32 weight tag: NA
AP139 free-var audit: fixed-curve theorem uses only \cA_i,\cC_i,\tau_i,X; relative proposition introduces \pi:\mathcal X\to S and base-change map explicitly
AP36: implies/iff audit not triggered on Theorem A; proposition is one-way under stated hypotheses
verdict: ACCEPT
```

I’m patching three places now: the filtration/comparison lane near `lem:filtered-comparison`, the Verdier proof of Theorem A, and the new proposition that isolates the exact modular-family obstruction instead of letting the proof overreach.

thinking
**Investigating patch issues**

I'm dealing with a patch that failed, possibly due to a missing dollar sign or backslash. I think I need to create smaller patches and ensure I have the exact context for each. It seems like inspecting the remark parts in lines 3740-3750 for the exact text might help. I wonder if the missing dollar sign was caused by a line break. I’ll need to address these small areas sequentially.
codex
The first patch failed on the trailing remark hunk only; the earlier edits didn’t apply yet. I’m re-reading the exact local text and reapplying in smaller chunks so the theorem lane changes stay tight and auditable.
exec
/bin/zsh -lc "sed -n '3640,3760p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '206,470p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 $\cA \in \operatorname{Fact}^{\mathrm{aug}}(X)$;
\item a conilpotent complete factorization coalgebra
 $\cC \in \operatorname{CoFact}^{\mathrm{conil,comp}}(X)$;
\item a degree $+1$ morphism
 $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
 $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
 $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
 all structure maps.
\end{enumerate}
Associated to $\tau$ are the \emph{twisted tensor products}
\[
K_\tau^L(\cA,\cC) := (\cA \otimes \cC,\; d_\cA + d_\cC + d_\tau^L),
\quad
K_\tau^R(\cC,\cA) := (\cC \otimes \cA,\; d_\cC + d_\cA + d_\tau^R).
\]
\end{definition}

\begin{remark}[Explicit twisted differential]
\label{rem:explicit-twisted-differential}
 succeeded in 53ms:
Theorem~A identifies the conditions under which $\cA^!_\infty$ is
\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.

\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
\label{thm:bar-cobar-isomorphism-main}
\index{bar-cobar duality!main theorem|textbf}
\index{Theorem A|textbf}
\textup{[}Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
The equivalences below hold in the derived category
$D^b(\mathrm{Fact}^{\mathrm{aug}}(X))$ of augmented
factorization algebras on~$X$.

\smallskip\noindent
The Heisenberg instance was verified in~\S\ref{sec:frame-inversion}.
In general:

Let $(\cA_1, \cC_1, \tau_1, F_\bullet)$ and
$(\cA_2, \cC_2, \tau_2, F_\bullet)$ be a chiral Koszul pair in
the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
codex
I have the exact live text again. I’m applying the patch in four minimal chunks: filtration definition, unit-side comparison lemma plus theorem proof, Theorem A statement/proof plus the new relative proposition, and the follow-up remark sync.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -211,3 +211,3 @@
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
apply_patch(auto_approved=true) exited 0 in 42ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..c58b120ab842e0fbade152a411ed07dea1fdb98a
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..c58b120ab842e0fbade152a411ed07dea1fdb98a
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -359,5 +359,5 @@
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
@@ -376,3 +376,15 @@
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
@@ -380,5 +392,5 @@
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
@@ -387,3 +399,3 @@
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
@@ -451,13 +463,16 @@
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
@@ -465,3 +480,4 @@
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
apply_patch(auto_approved=true) exited 0 in 47ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..c16926e20bbd71a264b8d5a0f9ed57c78961e914
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..c16926e20bbd71a264b8d5a0f9ed57c78961e914
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -3701,6 +3701,2 @@
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
@@ -3714,10 +3710,23 @@
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
 \[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
@@ -3725,15 +3734,84 @@
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
apply_patch(auto_approved=true) exited 0 in 42ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..f691132ffe854f5c97d9fae5a3a2d9b5bbea4faa
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,112 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
 \[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..f691132ffe854f5c97d9fae5a3a2d9b5bbea4faa
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,112 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
 \[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -3839,5 +3839,5 @@
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..3e3d6c98dbb06ff81d0faf4d135dbd5f76c11af3
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,112 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3837,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..3e3d6c98dbb06ff81d0faf4d135dbd5f76c11af3
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,112 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3837,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

codex
The edits are in. I’m re-reading the modified sections now to check that the bar-side comparison lemma is actually using the filtration from the twisting datum, that the fundamental theorem is no longer circular, and that Theorem A’s fixed-curve proof and relative-extension proposition line up without hidden object flips.
exec
/bin/zsh -lc "sed -n '206,470p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\cA \in \operatorname{Fact}^{\mathrm{aug}}(X)$;
\item a conilpotent complete factorization coalgebra
 $\cC \in \operatorname{CoFact}^{\mathrm{conil,comp}}(X)$;
\item a degree $+1$ morphism
 $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
 $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
 $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
 all structure maps.
\end{enumerate}
Associated to $\tau$ are the \emph{twisted tensor products}
\[
K_\tau^L(\cA,\cC) := (\cA \otimes \cC,\; d_\cA + d_\cC + d_\tau^L),
\quad
K_\tau^R(\cC,\cA) := (\cC \otimes \cA,\; d_\cC + d_\cA + d_\tau^R).
\]
\end{definition}

\begin{remark}[Explicit twisted differential]
\label{rem:explicit-twisted-differential}
exec
/bin/zsh -lc "sed -n '3640,3815p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
$t^3$. This nonvanishing defect is the kinematic signature of
nonquadraticity and feeds directly into the MC4 completion
programme
(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
\end{remark}

\subsection{Geometric bar-cobar duality (Theorem~A)}
\label{sec:theorem-a-statement}

The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
is unconditionally a factorization algebra
(Chapter~\ref{chap:NAP-koszul-derivation}).
Theorem~A identifies the conditions under which $\cA^!_\infty$ is
\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.

\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..3e3d6c98dbb06ff81d0faf4d135dbd5f76c11af3
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,112 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3837,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Inspecting theorem proof**

I need to check the continuation of the theorem proof because it might have been truncated. It seems like there was a cutoff after the definition, so I want to verify the rest of the proof to ensure there's no missing syntax. We have a partial proof that goes up to "the," but it looks like we're missing information from lines around 450-470. I should look into that more closely!
exec
/bin/zsh -lc "sed -n '448,475p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
By definition (Definition~\ref{def:chiral-koszul-morphism},
condition~1).

\emph{\ref{ftm:acyclic}$\Rightarrow$\ref{ftm:counit}:}
By Lemma~\ref{lem:twisted-product-cone-counit},
$K_\tau^L \simeq \operatorname{Cone}(\varepsilon_\tau)[-1]$.
Acyclicity of $K_\tau^L$ is therefore equivalent to
$\varepsilon_\tau$ being a quasi-isomorphism.

\emph{\ref{ftm:acyclic}$\Rightarrow$\ref{ftm:unit}:}
By Lemma~\ref{lem:twisted-product-cone-unit},
$K_\tau^R \simeq \operatorname{Cone}(\eta_\tau)[-1]$.
Acyclicity of $K_\tau^R$ is therefore equivalent to
$\eta_\tau$ being a weak equivalence.

\emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
Because the filtration in the twisting datum is exhaustive,
complete, and bounded below on both $\Omega_X(\cC)$ and
$\barB_X(\cA)$, the comparison spectral sequences converge
strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..3e3d6c98dbb06ff81d0faf4d135dbd5f76c11af3
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,112 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3837,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

exec
/bin/zsh -lc "sed -n '475,490p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
shows that the weak equivalence of $\eta_\tau$ forces the
associated graded datum
$(\operatorname{gr} \cA, \operatorname{gr} \cC,
\operatorname{gr} \tau)$ to be classically Koszul and lifts the
acyclicity of the classical twisted tensor products to
$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
is exactly Definition~\ref{def:chiral-koszul-morphism}.

\end{proof}

\begin{corollary}[Three bijections for chiral twisting morphisms;
\ClaimStatusProvedHere]
\label{cor:three-bijections}
\index{twisting morphism!three bijections|textbf}
For a conilpotent complete factorization coalgebra $\cC$
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..3e3d6c98dbb06ff81d0faf4d135dbd5f76c11af3
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,18 +374,30 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,112 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
+Verdier duals degreewise in the relative holonomic category, so the
+fiberwise identifications glue over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3837,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

codex
I found one remaining gap in the new relative proposition: it needs the relative algebra-level Verdier identifications for the coalgebra data themselves, not only base change for the bar complexes. I’m tightening that now, along with a small notation cleanup in the bar-side lemma.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -405,3 +405,3 @@
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
@@ -3752,2 +3752,10 @@
 \]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
 whose geometric fibers are chiral Koszul pairs in the sense of
@@ -3791,5 +3799,7 @@
 Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
-fiber. Hypothesis~\textup{(a)} is the exact condition needed to take
-Verdier duals degreewise in the relative holonomic category, so the
-fiberwise identifications glue over~$S$. The specialization
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
 $S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
@@ -3809,3 +3819,4 @@
 \item prove the relative Verdier/base-change isomorphism on the
- relative Ran space and check compatibility with the factorization
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
  gluing maps.
apply_patch(auto_approved=true) exited 0 in 61ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..9615482f97be77e0dcd48ef20a93833f073f78ad
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,123 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
 \[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3848,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..9615482f97be77e0dcd48ef20a93833f073f78ad
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,123 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
 \[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the verification of \textup{(a)} and \textup{(b)} on the relative
+Ran space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3848,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Adjusting theorem input**

I’m thinking about how the proposition mentions "additional input beyond Theorem A as the verification of (a) and (b)." It seems relative algebra-level Verdier identifications might fit within that data and not count as additional input. If the universal curve isn’t provided, however, they could be classified as additional. I think I need to tweak the sentence to clarify: “The only additional input beyond the fixed-curve theorem is the verification of the displayed relative Verdier identifications together with (a) and (b).” Let’s make that adjustment.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -3787,4 +3787,5 @@
 additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
-is the verification of \textup{(a)} and \textup{(b)} on the relative
-Ran space.
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
 \end{proposition}
apply_patch(auto_approved=true) exited 0 in 26ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..a0a7c657fb6169e634253431d0f11720f92b3405
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,124 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
 \[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3849,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..a0a7c657fb6169e634253431d0f11720f92b3405
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,124 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
 \[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3849,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Revisiting theorem section**

I realize I need to re-read the theorem and proposition section to solidify my understanding. It's always helpful to revisit complex materials, especially when they're foundational to what I'm trying to grasp. I wonder if there's something I missed or maybe a detail I need to focus on. Okay, let's dive back in to ensure I'm not skipping anything crucial! It's essential for me to comprehend this fully.
exec
/bin/zsh -lc "sed -n '356,490p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
then lifts this to acyclicity of $K_\tau^L$ and $K_\tau^R$
themselves.
\end{proof}

\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
\label{lem:filtered-comparison-unit}
\index{spectral sequence!bar-side filtered comparison}
Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
whose filtration is exhaustive, complete, and bounded below.
If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
then:
\begin{enumerate}[label=\textup{(\alph*)}]
\item the associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ is a classical Koszul datum;
\item both twisted tensor products $K_\tau^L$ and $K_\tau^R$ are
 acyclic.
\end{enumerate}
\end{lemma}

exec
/bin/zsh -lc "sed -n '3640,3795p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
$t^3$. This nonvanishing defect is the kinematic signature of
nonquadraticity and feeds directly into the MC4 completion
programme
(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
\end{remark}

\subsection{Geometric bar-cobar duality (Theorem~A)}
\label{sec:theorem-a-statement}

The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
is unconditionally a factorization algebra
(Chapter~\ref{chap:NAP-koszul-derivation}).
Theorem~A identifies the conditions under which $\cA^!_\infty$ is
\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.

\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..a0a7c657fb6169e634253431d0f11720f92b3405
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,124 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
 \[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3849,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

exec
/bin/zsh -lc "sed -n '3795,3835p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
statement to a compatible relative unit/counit package. Applying
$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
map and then pulling back to a geometric fiber $X_s$ gives, by
hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
fiber. The displayed relative Verdier identifications provide the
algebra target on the total space, and hypothesis~\textup{(a)} is the
exact condition needed to take Verdier duals degreewise in the
relative holonomic category. These ingredients glue the fiberwise
identifications over~$S$. The specialization
$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
argument to the universal curve.
\end{proof}

\begin{remark}[Programme for the modular-family extension]
\label{rem:bar-cobar-relative-programme}
\index{bar-cobar duality!modular-family programme}
To prove the full modular-family statement over
$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..a0a7c657fb6169e634253431d0f11720f92b3405
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,124 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
 \[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3849,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;



thinking
**Considering notation clarity**

I’m thinking about using the notation `\Omega_{\mathcal{X}/S}` and whether it’s defined properly. I wonder if it's best to reference it as the cobar functor or if `\Omega` will confuse with the relative canonical sheaf. Given the existing use of `\Omega_X`, I could rename it as `\Omega_{\mathcal X/S}^{\mathrm{cobar}}` for clarity instead. But then again, I’m aware that existing notation isn't necessarily defined. Perhaps just using a textual description could simplify things.
thinking
**Searching for notation usage**

I think I need to check if `\Omega_{\mathcal{X}/S}` has been used in the repository. It might be important to see if there are any references to it. I wonder if there’s a chance that it hasn’t been mentioned at all? Just to be thorough, I should go ahead and search the repository for that notation. I hope I find something useful that clarifies its usage!
codex
The main proof surface now reads cleanly. One notation point remains before verification: I introduced `\Omega_{\mathcal{X}/S}` for the relative cobar functor, and I want to make sure that doesn’t collide with existing relative-differential notation in the repo. If it’s unused, I’ll keep it; if it’s ambiguous, I’ll rewrite that line in prose instead of inventing a new symbol.
exec
/bin/zsh -lc "rg -n --fixed-strings '\\Omega_{\\mathcal{X}/S}' chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex chapters/connections/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:3756:\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
chapters/theory/chiral_koszul_pairs.tex:3759:\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
chapters/theory/chiral_koszul_pairs.tex:3756:\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
chapters/theory/chiral_koszul_pairs.tex:3759:\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
exec
/bin/zsh -lc "rg -n \"relative cobar|cobar factorization algebra over|relative bar construction|Ran\\(\\mathcal\\{X\\}/S\\)\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\Omega_{X/S}' chapters/theory/chiral_koszul_pairs.tex chapters/theory/*.tex chapters/connections/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 2 in 52ms:
rg: regex parse error:
    (?:relative cobar|cobar factorization algebra over|relative bar construction|Ran\(\mathcal\{X\}/S\))
                                                                                      ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..a0a7c657fb6169e634253431d0f11720f92b3405
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,124 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
 \[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
+\[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3849,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -3752,9 +3752,11 @@
 \]
-together with relative algebra-level Verdier identifications
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
 \[
 \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
-\simeq \Omega_{\mathcal{X}/S}(\cC_{2,S}),
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
 \qquad
 \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
-\simeq \Omega_{\mathcal{X}/S}(\cC_{1,S}),
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
 \]
apply_patch(auto_approved=true) exited 0 in 41ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Considering project build commands**

I’m thinking there might be project build commands I could use. Since the user mentioned verifying after each edit, I'm considering re-reading sections and using grep to search for specific changes. After finishing all edits, I might run a targeted LaTeX build, which could be tricky. To check quickly, I could use `rg -n` and `git diff -U0`. Still, running `latexmk` might be necessary if the user wants verification after every edit. I'll also look into existing compile scripts.
codex
The logic is repaired; I’m in verification now. I’m checking the exact diff, running the required AP greps on the touched file, and then I’ll decide whether a targeted TeX build is cheap enough to justify or whether the narrowest reliable verification here is textual plus local theorem-surface review.
exec
/bin/zsh -lc "rg -n \"T\\"'^c'"\\(s\\"'^{-1} A'"\\)|T\\"'^c'"\\(s A\\)|T\\"'^c'"\\(s\\"'^{-1}A'"\\)\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\Omega/z' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a10..ed03dc8 100644
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@ $(\cA, \cC, \tau, F_\bullet)$ consisting of:
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@ then lifts this to acyclicity of $K_\tau^L$ and $K_\tau^R$
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
 exited 2 in 52ms:
rg: regex parse error:
    (?:T\^c\(s\^{-1} A\)|T\^c\(s A\)|T\^c\(s\^{-1}A\))
                 ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
3246:$r^{\mathrm{cl}}(z) = k\Omega/z$ of an affine algebra
3263:$r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$ has vanishing second
exec
/bin/zsh -lc 'rg -n -i "moreover|additionally|notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|landscape|journey|navigate" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1680:by non-degeneracy of a bilinear form weight by weight. We now
2329:\emph{(unconditional for the standard landscape by
2581:The four classes exhaust the standard landscape, but the
2594:Let~$\cA$ be a chiral algebra in the standard landscape.
2608:Because the standard landscape is exhausted by the four classes
2794:not extend to the full standard landscape. The failure
2801:(Table~\ref{tab:koszulness-landscape}), so condition~(ii)
2866:\begin{remark}[Computational verification landscape]
2867:\label{rem:koszulness-computational-landscape}
2871:computationally for a landscape of 17 algebras
2872:(Table~\textup{\ref{tab:koszulness-landscape}}):
2902:\caption{Koszulness landscape: 17 algebras}
2903:\label{tab:koszulness-landscape}
2904:\index{Koszul property!landscape table}
3109:standard landscape, the OPE of $\cA_1 \oplus \cA_2$ has no mixed
3241:sequences. We now record a Poisson-geometric characterization that
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

codex
The required AP greps on the whole file surfaced pre-existing hits outside the edited lane, so I’m narrowing them to the modified line ranges to verify I didn’t introduce any new AP126/AP132/AP29 violations. After that I’ll decide whether a TeX build is worth the cost.
exec
/bin/zsh -lc "awk '((NR>=206&&NR<=490)||(NR>=3640&&NR<=3835)){print}' chapters/theory/chiral_koszul_pairs.tex | rg -n --fixed-strings '\\Omega/z'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "awk '((NR>=206&&NR<=490)||(NR>=3640&&NR<=3835)){print}' chapters/theory/chiral_koszul_pairs.tex | grep -nF 'T"'^c(s''^{-1} A)'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk '((NR>=206&&NR<=490)||(NR>=3640&&NR<=3835)){print}' chapters/theory/chiral_koszul_pairs.tex | grep -nF 'T"'^c(s A)'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk '((NR>=206&&NR<=490)||(NR>=3640&&NR<=3835)){print}' chapters/theory/chiral_koszul_pairs.tex | rg -n -i \"moreover|additionally|notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|landscape|journey|navigate\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:

 exited 1 in 53ms:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

codex
The modified surface passes the local AP greps. I’m attempting one project-level LaTeX compile now; if it fails for an unrelated pre-existing reason, I’ll stop at the local proof and diff verification rather than treat that as a regression from this patch.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Evaluating output status**

I need to figure out if the compile is still running or if it timed out or got truncated. It seems like the session is still active. Should I stop it, or just wait a bit longer? Maybe I could poll for the final result, but what if there are errors later? Hm, I think I’ll just take a moment and wait to see if it finishes up on its own.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

 exited 12 in 19.97s:
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Changed files or newly in use/created:
  chapters/examples/beta_gamma.aux
  chapters/examples/deformation_quantization.aux
  chapters/examples/free_fields.aux
  chapters/examples/kac_moody.aux
  chapters/examples/lattice_foundations.aux
  chapters/examples/level1_bridge.aux
  chapters/examples/moonshine.aux
  chapters/examples/w3_holographic_datum.aux
  chapters/examples/w_algebras.aux
  chapters/frame/heisenberg_frame.aux
  chapters/frame/preface.aux
  chapters/theory/algebraic_foundations.aux
  chapters/theory/bar_cobar_adjunction.aux
  chapters/theory/bar_construction.aux
  chapters/theory/chiral_hochschild_koszul.aux
  chapters/theory/chiral_koszul_pairs.aux
  chapters/theory/chiral_modules.aux


thinking
**Troubleshooting build failure**

The build failed due to an unrelated undefined control sequence at line 25121 in another file. There might be existing warnings, and I wonder if I need to close the session since the process likely ended. I should consider running `git diff --check` to catch any whitespace or syntax issues. It could be helpful to run `latexmk`, although compiling might not sufficiently test certain lines. I might also check for "Undefined control sequence" in the log. It seems fine for now!
thinking
**Inspecting compilation issues**

I should inspect the line numbers, checking for `\Omega^{\mathrm{rel}}`, since the compile passed beyond that point. It seems good so far! I wonder if there are AP29 hits throughout the whole file, but they might not be in the modified sections. We can confidently report no new hits in those areas, which is a relief. I think I should also run `git diff --check` to double-check everything. That seems like a solid plan!
codex
The compile got far past `chiral_koszul_pairs.tex` and then died on an unrelated pre-existing error: `Undefined control sequence \cR` at `main.tex` line 25121 in another surface. I’m doing one last diff sanity check now; given the parse got through the modified chapter, that is enough to treat this patch as locally verified.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '206,490p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --check -- chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3640,3835p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3640	Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
  3641	of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
  3642	giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
  3643	= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
  3644	$t^3$. This nonvanishing defect is the kinematic signature of
  3645	nonquadraticity and feeds directly into the MC4 completion
  3646	programme
  3647	(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
  3648	\end{remark}
  3649	
  3650	\subsection{Geometric bar-cobar duality (Theorem~A)}
  3651	\label{sec:theorem-a-statement}
  3652	
  3653	The homotopy Koszul dual $\cA^!_\infty := \mathbb{D}_{\Ran}\barB_X(\cA)$
  3654	is unconditionally a factorization algebra
  3655	(Chapter~\ref{chap:NAP-koszul-derivation}).
  3656	Theorem~A identifies the conditions under which $\cA^!_\infty$ is
  3657	\emph{formal}, quasi-isomorphic to the classical dual~$\cA^!$.
  3658	
  3659	\begin{theorem}[Geometric bar--cobar duality; \ClaimStatusProvedHere]
 succeeded in 52ms:
   206	 $\cA \in \operatorname{Fact}^{\mathrm{aug}}(X)$;
   207	\item a conilpotent complete factorization coalgebra
   208	 $\cC \in \operatorname{CoFact}^{\mathrm{conil,comp}}(X)$;
   209	\item a degree $+1$ morphism
   210	 $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
   211	 $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
   212	\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
   213	 $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
   214	 all structure maps.
   215	\end{enumerate}
   216	Associated to $\tau$ are the \emph{twisted tensor products}
   217	\[
   218	K_\tau^L(\cA,\cC) := (\cA \otimes \cC,\; d_\cA + d_\cC + d_\tau^L),
   219	\quad
   220	K_\tau^R(\cC,\cA) := (\cC \otimes \cA,\; d_\cC + d_\cA + d_\tau^R).
   221	\]
   222	\end{definition}
   223	
   224	\begin{remark}[Explicit twisted differential]
   225	\label{rem:explicit-twisted-differential}
 succeeded in 52ms:

file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Updating plan status**

I see that other files mention a summary about a genus-zero base case, but I don’t think that’s necessary right now. I need to focus on updating the plan status. I’ve completed steps 2, 3, and 4, so I should definitely note that down. It’s all about keeping track to ensure everything is moving along smoothly! Alright, let's get organized and keep this process flowing efficiently.
Plan update
The filtration hypothesis mismatch is fixed, the bar-side comparison lemma is explicit, Theorem A now keeps the Verdier target on the algebra side, and the modular-family extension is isolated as a separate relative proposition plus programme. Local AP greps passed on the modified regions; a full LaTeX build reached far beyond the touched chapter and then failed on an unrelated pre-existing undefined control sequence in another file.
  ✓ Read constitutional files, locate Theorem A, the filtered-comparison lemmas, and the cited Verdier/base-change dependencies.
  ✓ Repair the foundational comparison lane in chiral_koszul_pairs.tex: fix the filtration hypothesis mismatch, strengthen the unit-side comparison into an explicit bar-degree lemma, and re-read the local proof block.
  ✓ Rewrite Theorem A’s proof and statement so every post-\mathbb{D}_{\operatorname{Ran}} object is an algebra-level object, and isolate the exact family obstruction with the strongest proved intermediate result.
  ✓ Re-read the full modified region, run AP greps (bare Omega, augmentation, slop), and do the narrowest verification available on the touched surface.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Verifying modifications**

I need to mention that there were no hits when I checked with local AP grep in the modified regions. I managed to compile the touched chapter but ran into issues later due to an unrelated `\cR` in another file. It could be helpful to refer to specific files like [chapters/theory/chiral_koszul_pairs.tex](...). I'll use clickable file links with absolute paths to make it easier for anyone reviewing.
exec
/bin/zsh -lc "rg -n --fixed-strings '\\cR_{g,n}"'^{'"\\mathrm{MC}}' ." in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
./chapters/theory/higher_genus_modular_koszul.tex:25121:$\cR_{g,n}^{\mathrm{MC}}(\cA) \subset R^*(\overline{\cM}_{g,n})$
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;


thinking
**Considering confidence levels**

I think I should mention confidence levels as either high or medium. That seems important but I want to keep it concise. I'll make sure that I don't provide too much detail here since brevity is key for clarity. It’s all about hitting the right balance so the user gets the information they need without getting overwhelmed. Let’s keep it straightforward and focus on what really matters!
codex
Edited [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:209) and [the Theorem A surface](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:3659). The filtered-comparison lane is now non-circular, the Verdier half of Theorem A stays on the algebra side after `\mathbb{D}_{\operatorname{Ran}}`, and the modular-family claim is extracted into an explicit relative reduction plus programme instead of being justified by genus-0 input. Targeted AP126/AP132/AP29 greps on the modified regions were clean, and `git diff --check` is clean. A full `latexmk` run parsed past the touched chapter and then failed on an unrelated pre-existing `\cR` at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:25121).

## Platonic Rectification Report
- `thm:fundamental-twisting-morphisms`. BEFORE: equivalence theorem with `\ClaimStatusProvedHere`, but its proof used completeness and strong convergence not required by `def:chiral-twisting-datum`, and the unit-side comparison filtered by “bar degree” without an explicit associated-graded bar identification. ISSUE: circular use of condition (3) and an underjustified unit-side filtered comparison. ACTION: FILLED. AFTER: `def:chiral-twisting-datum` now requires an exhaustive, complete, bounded-below filtration; `lem:filtered-comparison-unit` is strengthened into an explicit bar-side filtered comparison; the theorem proof now derives Koszulity from the filtered-comparison lemmas plus strong convergence, with no circular appeal to the conclusion. CONFIDENCE: high. REMAINING GAP: none on the touched surface.
- `thm:bar-cobar-isomorphism-main`. BEFORE: fixed-curve bar-cobar/Verdier theorem with `\ClaimStatusProvedHere`, plus an unconditional family sentence over `\overline{\mathcal{M}}_{g,n}`; the proof composed through Verdier without making the post-`D_{\operatorname{Ran}}` object algebra-level, and justified the family claim with genus-0 theorems that do not supply the needed relative Ran base-change statement. ISSUE: Verdier half flipped algebra/coalgebra in the proof, and the modular-family clause overreached the cited input. ACTION: INTERMEDIATE+PROGRAMME. AFTER: the fixed-curve theorem remains proved and is now stated in its strongest unconditional form; the proof explicitly passes from `\eta_i` to `\mathbb{D}_{\operatorname{Ran}}(\barB_X(\cA_i))` and then to `\Omega_X(\cC_j)` and `\cA_j`, so every post-Verdier object is a factorization algebra. The former family clause is replaced by `prop:bar-cobar-relative-extension` and `rem:bar-cobar-relative-programme`, which isolate the strongest proved relative statement and the exact missing input: relative holonomic bar components, relative Verdier/base-change on the Ran space, and lifted relative Verdier pair identifications. CONFIDENCE: high on the fixed-curve theorem, medium on the formal relative reduction. REMAINING GAP: full functoriality over `\overline{\mathcal{M}}_{g,n}` still needs that relative Ran theorem.
file update:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 0305a104bdc30e807eec65ff86762c707d61a34b..ed03dc84df6a1a4a8a36f648b26ad123353c57ab
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -209,7 +209,7 @@
 \item a degree $+1$ morphism
  $\tau\colon \cC \to \cA$ satisfying the Maurer--Cartan equation
  $d\tau + \tau \star \tau = 0$ in the convolution dg~Lie algebra;
-\item an exhaustive bounded-below filtration $F_\bullet$ on $\cA$,
+\item an exhaustive, complete, bounded-below filtration $F_\bullet$ on $\cA$,
  $\cC$, $\bar{B}_X(\cA)$, and $\Omega_X(\cC)$, compatible with
  all structure maps.
 \end{enumerate}
@@ -357,9 +357,9 @@
 themselves.
 \end{proof}
 
-\begin{lemma}[Filtered comparison for the unit; \ClaimStatusProvedHere]
+\begin{lemma}[Bar-side filtered comparison; \ClaimStatusProvedHere]
 \label{lem:filtered-comparison-unit}
-\index{spectral sequence!filtered comparison for the unit}
+\index{spectral sequence!bar-side filtered comparison}
 Let $(\cA, \cC, \tau, F_\bullet)$ be a chiral twisting datum
 whose filtration is exhaustive, complete, and bounded below.
 If $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is a weak equivalence,
@@ -374,24 +374,36 @@
 \end{lemma}
 
 \begin{proof}
-Filter $\eta_\tau$ by bar degree. Since the filtration is bounded
+This is the unit-side analogue of
+Lemma~\ref{lem:filtered-comparison}: one replaces the cobar-side
+filtration on $\Omega_X(\cC)$ by the induced filtration on the bar
+coalgebra $\barB_X(\cA)$. Because $\barB_X(\cA)$ is the cofree tensor
+coalgebra on $s^{-1}\bar\cA$ and $F_\bullet$ is compatible with the
+bar structure, the associated graded bar coalgebra is canonically
+the classical reduced bar construction:
+\[
+\operatorname{gr}_F \barB_X(\cA)
+\;\cong\;
+\barB(\operatorname{gr}_F \cA).
+\]
+Filter $\eta_\tau$ by $F_\bullet$. Since the filtration is bounded
 below and complete, the induced spectral sequence converges
 strongly, and the associated graded map
 \[
-\operatorname{gr}\eta_\tau \colon \operatorname{gr}\cC
-\longrightarrow \operatorname{gr}\barB_X(\cA)
-\cong \barB(\operatorname{gr}\cA)
+\operatorname{gr}_F\eta_\tau \colon \operatorname{gr}_F\cC
+\longrightarrow \operatorname{gr}_F\barB_X(\cA)
+\cong \barB(\operatorname{gr}_F\cA)
 \]
 is a quasi-isomorphism of classical conilpotent coalgebras. By the
 classical fundamental theorem of twisting morphisms
 \cite[Theorem~2.3.1]{LV12}, the induced twisting morphism
-$\operatorname{gr}\tau$ is classically Koszul, proving~(a).
+$\operatorname{gr}_F\tau$ is classically Koszul, proving~(a).
 
 For~(b), Lemma~\ref{lem:twisted-product-cone-unit} identifies
 $K_\tau^R$ with $\operatorname{Cone}(\eta_\tau)[-1]$, so the weak
 equivalence of $\eta_\tau$ makes $K_\tau^R$ acyclic. Filter
 $K_\tau^L$ by $F_\bullet$; its associated graded complex is the
-classical left twisted tensor product for $\operatorname{gr}\tau$,
+classical left twisted tensor product for $\operatorname{gr}_F\tau$,
 which is acyclic by~(a). Strong convergence then lifts this
 acyclicity to~$K_\tau^L$.
 \end{proof}
@@ -449,21 +461,25 @@
 $\eta_\tau$ being a weak equivalence.
 
 \emph{\ref{ftm:counit}$\Rightarrow$\ref{ftm:koszul}:}
-By Lemma~\ref{lem:filtered-comparison}: filter $\Omega_X(\cC)$
-by cobar degree; the quasi-isomorphism of $\varepsilon_\tau$
-implies classical Koszulity of the associated graded datum and
-acyclicity of the twisted tensor products. The convergence
-hypothesis (Definition~\ref{def:chiral-koszul-morphism},
-condition~3) ensures the spectral sequence converges strongly.
+Because the filtration in the twisting datum is exhaustive,
+complete, and bounded below on both $\Omega_X(\cC)$ and
+$\barB_X(\cA)$, the comparison spectral sequences converge
+strongly. Lemma~\ref{lem:filtered-comparison} then gives classical
+Koszulity of the associated graded datum and acyclicity of the
+twisted tensor products. These are conditions~\textup{(1)} and
+\textup{(2)} of Definition~\ref{def:chiral-koszul-morphism}; the
+strong convergence just noted is condition~\textup{(3)}.
 
 \emph{\ref{ftm:unit}$\Rightarrow$\ref{ftm:koszul}:}
-This is the unit-side filtered comparison of
-Lemma~\ref{lem:filtered-comparison-unit}: the weak equivalence of
-$\eta_\tau$ forces the associated graded datum
+The same completeness and bounded-below hypotheses give strong
+convergence on the bar-side filtration. Lemma~\ref{lem:filtered-comparison-unit}
+shows that the weak equivalence of $\eta_\tau$ forces the
+associated graded datum
 $(\operatorname{gr} \cA, \operatorname{gr} \cC,
 \operatorname{gr} \tau)$ to be classically Koszul and lifts the
 acyclicity of the classical twisted tensor products to
-$K_\tau^L$ and $K_\tau^R$.
+$K_\tau^L$ and $K_\tau^R$. Together with strong convergence, this
+is exactly Definition~\ref{def:chiral-koszul-morphism}.
 
 \end{proof}
 
@@ -3683,10 +3699,6 @@
 \simeq \cA_2^!.
 \]
 \end{enumerate}
-
-These equivalences are functorial in families over the modular
-configuration spaces $\overline{\mathcal{M}}_{g,n}$ whenever
-the bar construction is formed relatively.
 \end{theorem}
 
 \begin{proof}
@@ -3696,30 +3708,126 @@
 (Definition~\ref{def:chiral-koszul-morphism}) are equivalent to
 the unit and counit being quasi-isomorphisms.
 For part~(2), the Verdier compatibility in
-Definition~\ref{def:chiral-koszul-pair} identifies
-$\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the factorization
-algebra $\Omega_X(\cC_2)$, and likewise with the indices reversed.
-Composing this with the unit equivalence
-$\cC_1 \xrightarrow{\sim} \bar{B}_X(\cA_1)$ and the counit
-equivalence $\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
-part~(1) yields
+Definition~\ref{def:chiral-koszul-pair} identifies the algebra-level
+Verdier dual $\mathbb{D}_{\operatorname{Ran}}(\cC_1)$ with the
+factorization algebra $\Omega_X(\cC_2)$, and likewise with the
+indices reversed. Let
+\[
+\eta_i \colon \cC_i \xrightarrow{\sim} \barB_X(\cA_i),
+\qquad
+\varepsilon_i \colon \Omega_X(\cC_i) \xrightarrow{\sim} \cA_i
+\]
+be the unit and counit equivalences from part~(1). Applying
+$\mathbb{D}_{\operatorname{Ran}}$ to $\eta_1$ gives an
+equivalence of factorization algebras
+\[
+\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA_1)
+\xrightarrow{\sim}
+\mathbb{D}_{\operatorname{Ran}}(\cC_1).
+\]
+Composing this with the Verdier-compatibility identification
+$\mathbb{D}_{\operatorname{Ran}}(\cC_1)\simeq \Omega_X(\cC_2)$ and
+then with $\varepsilon_2$ yields
 \[
 \mathbb{D}_{\operatorname{Ran}} \bar{B}_X(\cA_1)
 \simeq \Omega_X(\cC_2) \simeq \cA_2,
 \]
-and similarly for the other index. This is the Verdier
-identification at the factorization-algebra level.
+and similarly for the other index. Every object after
+$\mathbb{D}_{\operatorname{Ran}}$ is therefore a factorization
+algebra, not a coalgebra.
 Part~(3) is the same statement after naming $\cA_2$ as the Koszul
 dual~$\cA_1^!$.
-The relative/family statement follows from proper base change
-(Lemma~\ref{lem:pushforward-preserves-qi}): the FM compactification
-$\overline{C}_n(X)$ is proper over $\overline{\mathcal{M}}_{g,n}$,
-so the fiberwise quasi-isomorphisms lift to the family by
-Theorem~\ref{thm:bar-cobar-inversion-functorial}, and Verdier
-duality commutes with proper base change by
-Theorem~\ref{thm:verdier-bar-cobar}.
 \end{proof}
 
+\begin{proposition}[Relative extension from relative Verdier base change;
+\ClaimStatusProvedHere]
+\label{prop:bar-cobar-relative-extension}
+\index{bar-cobar duality!relative extension}
+Let $\pi \colon \mathcal{X} \to S$ be a family of smooth projective
+curves. Suppose given relative factorization data
+\[
+(\cA_{1,S}, \cC_{1,S}, \tau_{1,S}, F_\bullet),
+\qquad
+(\cA_{2,S}, \cC_{2,S}, \tau_{2,S}, F_\bullet)
+\]
+together with relative algebra-level Verdier identifications,
+where $\Omega^{\mathrm{rel}}$ denotes the cobar functor formed over
+the family $\pi$:
+\[
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{1,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{2,S}),
+\qquad
+\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}(\cC_{2,S})
+\simeq \Omega^{\mathrm{rel}}(\cC_{1,S}),
+\]
+whose geometric fibers are chiral Koszul pairs in the sense of
+Definition~\textup{\ref{def:chiral-koszul-pair}}. Assume:
+\begin{enumerate}[label=\textup{(\alph*)}]
+\item each relative bar component is represented on the relative
+ Fulton--MacPherson spaces by a bounded complex of relative
+ holonomic $\cD$-modules;
+\item for every geometric point $s \to S$, the canonical base-change
+ morphism
+ \[
+ s^* \mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}
+ \barB_{\mathcal{X}/S}(\cA_{i,S})
+ \longrightarrow
+ \mathbb{D}_{\operatorname{Ran}(X_s)}
+ \barB_{X_s}(\cA_{i,s})
+ \]
+ is an isomorphism;
+\item the unit and counit quasi-isomorphisms of
+ Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(1)} commute
+ with pullback to geometric fibers.
+\end{enumerate}
+Then the equivalences of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} assemble into
+equivalences of relative factorization algebras over~$S$, functorial
+under base change in~$S$.
+
+For the universal curve over $\overline{\mathcal{M}}_{g,n}$, the only
+additional input beyond Theorem~\ref{thm:bar-cobar-isomorphism-main}
+is the lift of the displayed relative Verdier identifications and the
+verification of \textup{(a)} and \textup{(b)} on the relative Ran
+space.
+\end{proposition}
+
+\begin{proof}
+Hypothesis~\textup{(c)} promotes part~\textup{(1)} of
+Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
+statement to a compatible relative unit/counit package. Applying
+$\mathbb{D}_{\operatorname{Ran}(\mathcal{X}/S)}$ to the relative unit
+map and then pulling back to a geometric fiber $X_s$ gives, by
+hypothesis~\textup{(b)}, the algebra-level Verdier equivalence of
+Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{(2)} on that
+fiber. The displayed relative Verdier identifications provide the
+algebra target on the total space, and hypothesis~\textup{(a)} is the
+exact condition needed to take Verdier duals degreewise in the
+relative holonomic category. These ingredients glue the fiberwise
+identifications over~$S$. The specialization
+$S=\overline{\mathcal{M}}_{g,n}$ is obtained by applying the same
+argument to the universal curve.
+\end{proof}
+
+\begin{remark}[Programme for the modular-family extension]
+\label{rem:bar-cobar-relative-programme}
+\index{bar-cobar duality!modular-family programme}
+To prove the full modular-family statement over
+$\overline{\mathcal{M}}_{g,n}$, one must establish the two relative
+inputs isolated in
+Proposition~\ref{prop:bar-cobar-relative-extension}:
+\begin{enumerate}[label=\textup{(\arabic*)}]
+\item construct the relative bar components as bounded holonomic
+ $\cD$-complexes on the relative Fulton--MacPherson spaces;
+\item prove the relative Verdier/base-change isomorphism on the
+ relative Ran space, lift the algebra-level Verdier-compatible pair
+ identifications, and check compatibility with the factorization
+ gluing maps.
+\end{enumerate}
+The fixed-curve theorem above is the strongest unconditional result
+proved in this chapter.
+\end{remark}
+
 \begin{remark}[Geometric substrate (Volume~II)]
 \label{rem:theorem-a-lagrangian}
 \index{Lagrangian self-intersection!Theorem A}
@@ -3743,9 +3851,9 @@
 Part~(1) says each~$\tau_i$ is acyclic;
 part~(2) says Verdier duality sends the bar coalgebra of one side
 to the dual factorization algebra recovered from the other;
-and the family statement says these identifications are
-compatible with proper base change over
-$\overline{\mathcal{M}}_{g,n}$.
+and Proposition~\ref{prop:bar-cobar-relative-extension} isolates
+the extra relative Verdier/base-change input needed to transport
+these identifications over a base.
 \end{remark}
 
 \begin{remark}[Elementary model presentation;

tokens used
218,935
