# R11_thqg_symplectic_polarization (406s)

Edited [chapters/connections/thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex).

I strengthened the `\sigma` construction rather than just adding a warning: the file now has a proved local lemma `lem:thqg-III-ambient-biduality` establishing that `\mathbf{C}_g(\cA) \to \mathbf{C}_g(\cA)^{\vee\vee}` is a quasi-isomorphism from finite-dimensional total cohomology. The construction and the C1 theorem now cite that lemma explicitly, and the Verdier arrow is attributed to the ambient self-duality proved in this file rather than loosely to the earlier bar-complex corollary.

I also made the genus scope impossible to miss on the eigenspace surface: the subsection introduction now says the splitting holds for all `g \ge 0` but the perfect duality starts only at `g \ge 1`, and the theorem header now reads “Duality only for `g \ge 1`,” with the genus-0 boundary `Q_0(\cA)=Z(\cA), Q_0(\cA^!)=0` left explicit. I also removed the incorrect universal range `0 \le n \le 6g-6` from the ambient-complex finite-dimensionality statement and replaced it with the truthful boundedness statement needed for biduality.

Verification: I re-read the modified sections and checked the new label/reference usage locally. I also attempted `latexmk -pdf main.tex`, but the run failed before a clean chapter-level verification because `main.aux` is already in a broken state (`Runaway argument ... while scanning use of \@writefile`) with many unrelated undefined refs/citations outside this edit.

## Rectification Summary
- [FIXED] finding 1 — made the genus split explicit on the C1 surface: decomposition for all `g \ge 0`, duality only for `g \ge 1`, with the genus-0 exception `Q_0(\cA)=Z(\cA), Q_0(\cA^!)=0` foregrounded.
- [FIXED] finding 2 — added a proved ambient-biduality lemma so the use of `\mathbf{C}_g(\cA)^{\vee\vee}` now rests on explicit perfectness/bidualizability, not an implicit reflexivity assumption.
- [FIXED] local coherence issue discovered during re-read — replaced the false finite-dimensionality range bound with a bounded-cohomology statement compatible with genus 0 and the biduality argument.
- [BLOCKED] full build verification — `latexmk` failed on pre-existing auxiliary/reference corruption in `main.aux`, so I could not use the monograph build as final evidence for this local edit.


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
session id: 019d8674-30ab-7363-b50c-a38ebd6b265d
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


TARGET: chapters/connections/thqg_symplectic_polarization.tex

FINDINGS TO FIX:

1. [CRITICAL T04] Lines ~476,694: Q_g(A) ≅ Q_g(A^!)^v claimed for all g>=0, but
   Q_0(A)=Z(A) and Q_0(A^!)=0 proven in the same file. Contradiction at g=0.
   FIX: Add hypothesis g>=1, or fix the genus-0 identifications. Check if Q_0 should
   actually be nonzero for both A and A^!.

2. [CRITICAL T04] Lines ~197,220: The involution sigma uses ev: C_g(A)^{vv} -> C_g(A)
   without reflexivity hypothesis. The vv construction imports finite-dimensional fiber-cohomology.
   FIX: Add the reflexivity/perfectness hypothesis explicitly, or use a different construction.

Read the file, verify both findings, fix.
mcp startup: no servers
codex
I’m rectifying the two flagged theorem-surface issues in [chapters/connections/thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex). First I’m reading the required repo invariants, the skill instructions, and the exact local context around both findings so the fix matches the manuscript’s live conventions and proof status.
exec
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

exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

 succeeded in 51ms:
% Section file for Chapter: Twisted Holography and Quantum Gravity
% Result (G3): Complementarity as Shifted-Symplectic Polarization

% Local macros (providecommand only; never \newcommand in chapter files)
\providecommand{\MC}{\mathrm{MC}}
\providecommand{\Defcyc}{\mathrm{Def}_{\mathrm{cyc}}}
\providecommand{\Definfmod}{\mathrm{Def}^{\mathrm{mod}}_\infty}
\providecommand{\Sh}{\mathrm{Sh}}
\providecommand{\gr}{\operatorname{gr}}
\providecommand{\id}{\mathrm{id}}
\providecommand{\Tr}{\operatorname{Tr}}
\providecommand{\Sym}{\operatorname{Sym}}
\providecommand{\Hom}{\operatorname{Hom}}
\providecommand{\End}{\operatorname{End}}
\providecommand{\Spec}{\operatorname{Spec}}
\providecommand{\Res}{\operatorname{Res}}
\providecommand{\rank}{\operatorname{rank}}
\providecommand{\ad}{\operatorname{ad}}
\providecommand{\Fred}{\operatorname{Fred}}
\providecommand{\Map}{\operatorname{Map}}
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
Total output lines: 220

# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2842 |
| Total tagged claims | 3669 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |

thinking
**Gathering findings context**

I need to look at specific lines in the file, particularly around lines 197, 220, 476, and 694, while considering the surrounding context. It's essential to check the local context to understand the findings better. Using a command like 'rg' might be useful for this. I should gather exact information about these lines and the theorem labels mentioned to ensure I'm capturing all relevant details. This sounds straightforward, but I want to be thorough!
codex
I’ve loaded the rectification workflow and the repo’s live invariants. Now I’m isolating the exact theorem blocks around the two failures, checking whether the contradiction is local to this file or imported from cited genus-0 identifications, and then I’ll patch the minimum truthful scope/hypothesis.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '150,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Q_g|Q_0|sigma|reflex|perfect|bidual|vv|duality|genus-0|g >= 0|g\\\\ge 0|g\\\\geq 0|g \\ge 0|g \\geq 0\" chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '1080,1820p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '430,740p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   150	 $\overline{\mathcal{M}}_g$.
   151	
   152	\item \emph{Functoriality.}
   153	 The assignment $(\cA, \cA^!) \mapsto \mathbf{C}_g(\cA)$
   154	 is functorial in morphisms of Koszul pairs.
   155	\end{enumerate}
   156	\end{proposition}
   157	
   158	\begin{proof}
   159	\emph{Part (i).}
   160	The cohomological dimension of $\overline{\mathcal{M}}_g$ is
   161	$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
   162	by Artin vanishing for proper DM stacks
   163	\cite[\S4.1]{Olsson16}. The stalks of
   164	$\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
   165	(finite-dimensional flat fiber cohomology,
   166	Lemma~\ref{lem:perfectness-criterion}(ii)).
   167	By constructibility of $\mathcal{Z}(\cA)$
   168	(Lemma~\ref{lem:quantum-ss-convergence}, condition (2)),
   169	each cohomology sheaf $R^q\pi_{g*}\barB^{(g)}(\cA)$
 exited 2 in 51ms:
rg: regex parse error:
    (?:Q_g|Q_0|sigma|reflex|perfect|bidual|vv|duality|genus-0|g >= 0|g\ge 0|g\geq 0|g \ge 0|g \geq 0)
                                                                      ^^
error: unrecognized escape sequence
 succeeded in 51ms:
   430	\otimes
   431	C^{(3g-3)-p}(\overline{\mathcal{M}}_g, \mathbb{D}\mathcal{Z})
   432	\to
   433	C^{3g-3}(\overline{\mathcal{M}}_g, \omega_{\overline{\mathcal{M}}_g})
   434	\xrightarrow{\int}
   435	\mathbb{C}
   436	\]
   437	is nondegenerate by the duality theorem for constructible sheaves
   438	on smooth proper varieties
   439	(Grothendieck--Verdier duality, \cite[Theorem~3.1.10]{KS90}).
   440	\end{proof}
   441	
   442	\begin{proposition}[Degree shift at each genus;
   443	\ClaimStatusProvedHere]
   444	\label{prop:thqg-III-degree-shift}
   445	The holographic Verdier pairing has cohomological degree
   446	$-(3g - 3)$. In particular:
   447	\begin{enumerate}[label=\textup{(\alph*)}]
   448	\item At genus $0$: degree $+3$, pairing
   449	 $H^0 \otimes H^0 \to \mathbb{C}[3]$
 succeeded in 52ms:
Total output lines: 741

  1080	This restricted pairing is nondegenerate: suppose
  1081	$v \in \mathbf{Q}_g(\cA)$ satisfies
  1082	$\langle v, w \rangle_g = 0$ for all
  1083	$w \in \mathbf{Q}_g(\cA^!)$. Combined with isotropy
  1084	$\langle v, w' \rangle_g = 0$ for
  1085	$w' \in \mathbf{Q}_g(\cA)$, this gives
  1086	$\langle v, - \rangle_g = 0$ on all of $\mathbf{C}_g$.
  1087	By nondegeneracy of the full pairing, $v = 0$.
  1088	
  1089	Therefore the induced map is a quasi-isomorphism, verifying
  1090	PTVV nondegeneracy.
  1091	
  1092	\emph{Part (C2c): anti-symplectomorphism.}
  1093	By the anti-symmetry \eqref{eq:thqg-III-anti-symmetry}:
  1094	$\langle \sigma(v), \sigma(w) \rangle_g
  1095	= -\langle v, w \rangle_g$.
  1096	This is the statement that
  1097	$\sigma^* \omega_g = -\omega_g$, i.e., $\sigma$ is an

thinking
**Inspecting search issues**

It looks like my search has failed due to a regex problem. I need to focus on proposition genus-0 and examine any theorem references around line 220, as well as lines starting at 733. I should also check for any duality for all g used elsewhere. Plus, there's the theorem labeled as thm:thqg-III-lagrangian-polarization that may need references. I should only edit the specific file, but there might be more occurrences of incorrect all g that I need to find. Maybe I should read through the entire file using simpler regex patterns.
codex
The contradiction is local and explicit: the theorem already states the genus-0 boundary correctly, but a downstream corollary/prose lane still treats the exchange as genus-uniform. I’m now scanning the remainder of this file for every place where `Q_g` duality or the `\sigma` construction is reused, so the patch closes the whole local surface instead of only one sentence.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '733,820p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Q_0|Q_g\\(|Q_g\\(|Q_g\\)|Q_1\\(|Q_2\\(|Q_g\\\\|sigma|bidual|perfect ambient complex|finite-dimensional fiber-cohomology|canonical biduality|g \\\\ge 0|g \\\\geq 0|g >= 0|g \\ge 0|g \\geq 0|genus-0 boundary|genus~\\\\"'$0'"\\\\"'$|genus~0|g = 0'"' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   733	\begin{proposition}[Genus-$0$ complementarity;
   734	\ClaimStatusProvedHere]
   735	\label{prop:thqg-III-genus-0}
   736	\index{complementarity!genus 0}
   737	At genus~$0$, $\overline{\mathcal{M}}_0 = \mathrm{pt}$ and
   738	$\mathcal{H}_0(\cA) = Z(\cA)$.
   739	The Verdier involution $\sigma$ acts as $+\id$ on $Z(\cA)$,
   740	giving:
   741	\[
   742	Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
   743	\]
   744	If $Z(\cA)\neq 0$, no duality
   745	$Q_0(\cA) \cong Q_0(\cA^!)^{\vee}$ can hold.
   746	\end{proposition}
   747	
   748	\begin{proof}
   749	Since $\overline{\mathcal{M}}_0$ is a point, the center
   750	local system has a single stalk, so
   751	\[
   752	\mathbf{C}_0(\cA)
 exited 2 in 51ms:
rg: regex parse error:
    (?:Q_0|Q_g\(|Q_g\(|Q_g\)|Q_1\(|Q_2\(|Q_g\\|sigma|bidual|perfect ambient complex|finite-dimensional fiber-cohomology|canonical biduality|g \\ge 0|g \\geq 0|g >= 0|g \ge 0|g \geq 0|genus-0 boundary|genus~\\$0\\$|genus~0|g = 0)
                                                                                                                                                                        ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '260,430p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   260	 \mathbf{C}_g(\cA) \otimes \mathbf{C}_g(\cA) \to
   261	 \mathbb{C}[{-(3g{-}3)}]$
   262	 satisfies the anti-symmetry
   263	 \begin{equation}\label{eq:thqg-III-anti-symmetry}
   264	 \langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}}
   265	 = -\langle v, w \rangle_{\mathbb{D}}
   266	 \end{equation}
   267	 for all $v, w \in \mathbf{C}_g(\cA)$.
   268	\end{enumerate}
   269	\end{proposition}
   270	
   271	\begin{proof}
   272	\emph{Part (a).}
   273	Write
   274	$\mathrm{can}_{\mathbf{C}_g}\colon
   275	\mathbf{C}_g(\cA) \xrightarrow{\sim}
   276	\mathbf{C}_g(\cA)^{\vee\vee}$
   277	for the canonical biduality map of
   278	Construction~\ref{constr:thqg-III-verdier-involution}.
   279	Koszul involutivity
exec
/bin/zsh -lc "rg -n 'Q_0|Q_g\\(|Q_g\\b|Q_1|Q_2|sigma|bidual|perfectness-criterion|finite-dimensional fiber-cohomology|dualit(y|ies) for \\"'$g '"\\\\ge 1\\"'$|genus-'"\\"'$0'"\\"'$ boundary'"' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'cor:quantum-dual-complete|lem:perfectness-criterion|thm:fiber-center-identification|lem:center-isomorphism|cor:duality-bar-complexes-complete|lem:eigenspace-decomposition-complete|lem:quantum-from-ss' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
103:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
166:Lemma~\ref{lem:perfectness-criterion}(ii)).
205:canonical biduality of the perfect ambient complex, combine to produce
207:\begin{equation}\label{eq:thqg-III-sigma-def}
208:\sigma
213:\begin{equation}\label{eq:thqg-III-sigma-composition}
232:$\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
236:Lemma~\ref{lem:perfectness-criterion} with
253:The endomorphism $\sigma$ of
257:\item $\sigma^2 = \id$ \textup{(}involutivity\textup{)}.
264: \langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}}
277:for the canonical biduality map of
285:smooth proper DM stacks, and biduality is natural for perfect
287:returns the canonical biduality morphism
292:Since $\sigma$ is defined by composing this once-iterated
295:the first and $\sigma^2 = \id$.
301:\langle \sigma(v), \sigma(w) \rangle_{\mathbb{D}}
325:The Verdier involution $\sigma$ intertwines the shadow projections
328:\sigma \circ \pi_g^*(\Theta_\cA)
343:\sigma(\Theta_\cA)
 succeeded in 51ms:
103:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
105:(Theorem~\ref{thm:fiber-center-identification}) gives
141: (Lemma~\ref{lem:center-isomorphism}) induce a
166:Lemma~\ref{lem:perfectness-criterion}(ii)).
178:(Corollary~\ref{cor:duality-bar-complexes-complete} and
179:Lemma~\ref{lem:center-isomorphism}).
228:Corollary~\ref{cor:duality-bar-complexes-complete},
231:via Lemma~\ref{lem:center-isomorphism}, and
236:Lemma~\ref{lem:perfectness-criterion} with
237:Theorem~\ref{thm:fiber-center-identification}: on the modular
414:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})},
505:Lemma~\ref{lem:perfectness-criterion}(ii), so that
642:(Lemma~\ref{lem:eigenspace-decomposition-complete}).
646:(Lemma~\ref{lem:quantum-from-ss}).
664:Corollary~\ref{cor:quantum-dual-complete}.
681:Corollary~\ref{cor:quantum-dual-complete}.
757:Corollary~\ref{cor:quantum-dual-complete} identifies the
992: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
1106:cohomology (Lemma~\ref{lem:perfectness-criterion}).
1176:(Theorem~\ref{thm:fiber-center-identification}), the

thinking
**Investigating references**

I think I need to take a closer look at references around 2134 and possibly summarize the theorem. It might also be important to keep an eye on things starting from around 2100 onwards. There's a lot to consider! I'll want to ensure I'm covering the relevant information. Let's see how this unfolds as I gather more details and organize my findings. I'll take my time with it for clarity!
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '2100,2165p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2100	\begin{proof}
  2101	\emph{Part (i).}
  2102	At genus $0$, the ambient complex
  2103	$\mathbf{C}_0(\cA) = Z(\cA)$ is independent of $X$
  2104	(the center is an intrinsic invariant of $\cA$,
  2105	independent of the curve).
  2106	
  2107	\emph{Part (ii).}
  2108	Bar-cobar inversion
  2109	$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ on the Koszul
  2110	locus gives a quasi-isomorphism of chiral algebras, hence
  2111	an isomorphism on centers and ambient complexes.
  2112	
  2113	\emph{Part (iii).}
  2114	Corollary~\ref{cor:modular-properties}: the complementarity
  2115	decomposition commutes with the $\operatorname{Sp}(2g, \mathbb{Z})$
  2116	action.
  2117	
  2118	The Koszul invariance of the shadow depth class follows because
  2119	$r_{\max}$ is determined by the vanishing pattern of the shadow
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '820,950p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '930,1015p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   820	extending its genus-$0$ structure to genus~$1$ (the
   821	central extension $\kappa$), the Koszul dual
   822	$\mathcal{H}_\kappa^!$ sees as a deformation (the Hodge
   823	class $\lambda_1$ parametrizing the curvature of the
   824	genus-$1$ structure).
   825	\end{remark}
   826	
   827	% ======================================================================
   828	%
   829	% 3. SHIFTED-SYMPLECTIC STRUCTURE (C2)
   830	%
   831	% ======================================================================
   832	
   833	\subsection{The shifted-symplectic structure}
   834	\label{subsec:thqg-III-shifted-symplectic}
   835	\index{shifted symplectic!structure!holographic|textbf}
   836	\index{PTVV!holographic application}
   837	
   838	The unconditional decomposition~(C1) is an eigenspace statement.
   839	The conditional upgrade~(C2) endows the ambient complex with a
 succeeded in 51ms:
   930	\end{proposition}
   931	
   932	\begin{remark}[Two shifted structures in complementarity]
   933	\label{rem:thqg-III-two-structures}
   934	\index{shifted symplectic!two structures}
   935	Complementarity carries two shifted symplectic structures:
   936	\begin{enumerate}[label=\textup{(\roman*)}]
   937	\item The \emph{BV structure}: the antibracket on
   938	 $\barB^{\mathrm{ch}}(\cA)$ gives a $(-1)$-shifted symplectic
   939	 structure on $\MC(\barB^{(g)}(\cA)[1])$, universal in $g$.
   940	\item The \emph{Verdier structure}: the holographic pairing on
   941	 $\mathbf{C}_g(\cA)$ gives a $(-(3g-3))$-shifted symplectic
   942	 structure, depending on $g$.
   943	\end{enumerate}
   944	Both make $Q_g(\cA)$ and $Q_g(\cA^!)$ complementary Lagrangians;
   945	the two are compatible via the bar-complex spectral sequence.
   946	\end{remark}
   947	
   948	\subsubsection{The BV shifted-symplectic structure}
   949	\label{subsubsec:thqg-III-bv-shifted}






thinking
**Exploring search queries**

I’m looking to search for the mathematical expression `\cong Q_g(\cA^!)^{\vee}` and maybe focus on specific lines like 541 and 1012. Additionally, I want to check into "half dimension" and any related genus 0 problems. It seems there’s a lot to consider in these areas, and I want to make sure I'm thorough in my search to find relevant information and insights! Let's see what we can uncover!
thinking
**Considering theorem adjustments**

I’m thinking about whether finding 1 has already been partially fixed by someone else, but the user wants a correction now. The proof states something about duality and seems consistent. I wonder if the user’s references are outdated, but I need to verify that. It looks like we might only need minimal edits, such as adding explicit terms like g ≥ 1. It could be that no edits are needed for finding 1, yet they want all findings addressed. I think I might need to clarify the corollary about the Complementarity exchange principle, too. Maybe I should explore the file for more thoroughness?
thinking
**Inspecting references for finding 2**

I think it might be fine, but I really need to look into the exact references for finding 2. The construction mentions something about the "canonical biduality of the perfect ambient complex" and notes that there's no need for a bounded finite-dimensional model. That suggests it could already be fixed. But then, I see that the finding states involution sigma uses a specific mapping without the reflexivity hypothesis, which might complicate things. I should clarify this.
thinking
**Rethinking curves of genus 0**

I'm considering whether stable curves of genus 0 without marks can exist. It seems they might mean one-point compactification, but I notice their local conventions suggest that \overline{M_0} = pt, indicating cohomology in degree 0. So, I'm realizing that part (i) should specify nonzero only for 0≤n≤max(0,6g−6) or potentially separate cases for g=0, g=1, and g≥2. It's a bit intricate, but I think I'm getting there!
thinking
**Reviewing file details**

It seems like the current file already has some of the user’s findings addressed, so I might just need to clarify a few things to ensure everything's fully resolved. I should check the dependencies cited in finding 2 to see if they connect well. Maybe opening the lemma on perfectness-criteria or the theorem on fiber-center-identification could help, but it might not be necessary. AGENTS mentioned going through the exact files and directly cited dependencies.
thinking
**Investigating perfection criteria**

I'm opening up the relevant dependency concerning the perfection criterion, particularly looking at the corollary related to quantum-dual completeness since the theorem utilizes them. I might need to verify if finite-dimensional fiber-cohomology is enough for perfection. The source of the lemma states an assumption about this hypothesis, so I’ll check by reading through it. I might consider using an explorer tool to find these theorem labels and summarize whether the assumptions indicate perfection or reflexivity.
codex
I’ve hit one more local fragility tied to finding 2: the construction currently leans on “finite-dimensional fiber cohomology” and then upgrades to biduality via perfection, so I’m checking the cited source labels directly to make sure the hypothesis I write is exactly what the repository already proves, not a new invention.
collab spawn_agent(call_TZhi5MdVBHIpc3KrsbcrTnt5, prompt="Locate and summarize the exact hypotheses/results for these labels, with file+line references only from this repo: lem:p…")
mcp startup: no servers
spawn_agent(call_TZhi5MdVBHIpc3KrsbcrTnt5, prompt="Locate and summarize the exact hypotheses/results for these labels, with file+line references only from this repo: lem:p…") pending init:
  agent: 019d8675-d21a-7a83-9f8d-ea5035455f43
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "lem:perfectness-criterion" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 757

metadata/dependency_graph.dot:2792:  lem_perfectness_criterion [label="lem:perfectness-criterion\nlemma [Pr]\nPerfectness criterion for the strict fla...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:726:| `lem:perfectness-criterion` | `lemma` | 290 | Perfectness criterion for the strict flat relative bar family |
metadata/label_index.json:24802:  "lem:perfectness-criterion": {
metadata/claims.jsonl:912:{"label": "lem:thqg-III-nondegeneracy", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 411, "title": "Nondegeneracy of the holographic pairing", "refs_in_block": ["lem:perfectness-criterion", "eq:thqg-III-holographic-pairing-def"]}
metadata/claims.jsonl:914:{"label": "thm:thqg-III-eigenspace-decomposition", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 500, "title": "Holographic eigenspace decomposition (C1)", "labels_in_block": ["thm:thqg-III-eigenspace-decomposition", "eq:thqg-III-C1-homotopy", "eq:thqg-III-C1-shadow", "eq:thqg-III-C1-duality"], "refs_in_block": ["lem:perfectness-criterion", "constr:thqg-III-verdier-involution"]}
metadata/claims.jsonl:921:{"label": "thm:thqg-III-lagrangian-polarization", "env_type": "theorem", "status": "Conditional", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 985, "title": "Verdier Lagrangian polarization (C2)", "labels_in_block": ["thm:thqg-III-lagrangian-polarization", "eq:thqg-III-lagrangian-decomp"], "refs_in_block": ["lem:perfectness-criterion", "lem:thqg-III-nondegeneracy", "def:thqg-III-shifted-symplectic"]}
metadata/claims.jsonl:2685:{"label": "lem:perfectness-criterion", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 290, "title": "Perfectness criterion for the strict flat relative bar family", "refs_in_block": ["def:modular-koszul-chiral", "conv:higher-genus-differentials"]}
metadata/claims.jsonl:2686:{"label": "thm:fiber-center-identification", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 373, "title": "Fiber--center identification \\textup{(Theorem~\\texorpdfstring{$\\mathrm{C}_0$}{C0})}", "labels_in_block": ["thm:fiber-center-identification", "eq:fiber-center"], "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral", "prop:gauss-manin-uncurving-chain", "lem:perfectness-criterion"]}
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:395: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:708:chapters/theory/higher_genus_complementarity.tex:76: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:710:chapters/theory/higher_genus_complementarity.tex:92:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:712:chapters/theory/higher_genus_complementarity.tex:116:base change (Lemma~\ref{lem:perfectness-criterion}).
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:722:chapters/theory/higher_genus_complementarity.tex:365:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
fix_wave_A_20260413_112727/A11_fix_broken_refs_v1_theory.md:724:chapters/theory/higher_genus_complementarity.tex:427:(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
rectification_20260412_233715/R11_thqg_symplectic_polarization.md:241:103:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
rectification_20260412_233715/R11_thqg_symplectic_polarization.md:245:166:Lemma~\ref{lem:perfectness-criterion}(ii)).
rectification_20260412_233715/R11_thqg_symplectic_polarization.md:271:Lemma~\ref{lem:perfectness-criterion}(ii)).
rectification_20260412_233715/R11_thqg_symplectic_polarization.md:412:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center

thinking
**Updating the plan**

I’m considering whether I should conduct a search using tools like rg and sed while the agent is running. It seems like a good idea, but I’m contemplating if I need to update my plan to make it more effective. Maybe a revised approach could be really useful since there’s a substantial amount to cover. Let’s see how this plays out and adjust as necessary!
Plan update
Rectifying the two flagged theorem-surface issues in the assigned file only.
  ✓ Read live repo invariants, target file, and cited dependencies for the two findings
  → Verify the exact contradiction and the biduality/perfectness hypothesis gap on the local theorem surface
  • Patch the file with the minimum truthful scope/hypothesis changes
  • Re-read modified sections and run targeted checks for labels, refs, and coherence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '250,360p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \textup{(}anti-symmetric under $\sigma$\textup{)}, then $V^+$ and
 $V^-$ are isotropic for $\langle -,- \rangle$; if the pairing is
 non-degenerate, they are Lagrangian.
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '360,460p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
cohomology sheaves
$\mathcal{H}^q(R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA))$ vanish for
$q \neq 0$ uniformly over the base, and the surviving
degree-$0$ cohomology sheaf has
finite-dimensional fibers by hypothesis~(ii). The standard
cohomology and base change theorem
(EGA~III, Th\'eor\`eme~7.7.5)
then gives that $R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA)$ is a perfect
complex (bounded, with coherent cohomology sheaves) on
$\overline{\mathcal{M}}_g$.
\end{proof}

\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
\label{thm:fiber-center-identification}
\index{fiber--center identification|textbf}
\textup{[}Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})].}

\smallskip\noindent
Assume $\cA$ carries a modular pre-Koszul datum
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "cor:quantum-dual-complete" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
1288:\label{cor:quantum-dual-complete}
1301:\begin{proof}[Proof of Corollary~\ref{cor:quantum-dual-complete}]
1339:\mathcal{A}^!))^\vee$ be the Verdier isomorphism of Corollary~\ref{cor:quantum-dual-complete}.
2455:By Verdier duality (Corollary~\ref{cor:quantum-dual-complete}):
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1240,1380p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
for all $r \geq 1$, where $d = \dim_{\mathbb{R}} \overline{C}_n(X) = 2n$.
\end{lemma}

\begin{proof}[Proof of Lemma~\ref{lem:ss-duality-complete}]
\emph{$E_1$ page}: By definition,
\begin{align}
(E_1^{p,q,g})_{\mathcal{A}} &= H^q(\bar{B}^p_g(\mathcal{A}), d_{\text{fiber}})\\
(E_1^{p,d-q,g})_{\mathcal{A}^!} &= H^{d-q}(\bar{B}^p_g(\mathcal{A}^!), d_{\text{fiber}})
\end{align}

By Corollary~\ref{cor:duality-bar-complexes-complete}, the pairing:
\begin{equation}
\langle -, - \rangle: H^q(\bar{B}^p_g(\mathcal{A})) \otimes H^{d-q}(\bar{B}^p_g(
\mathcal{A}^!)) \to \mathbb{C}
\end{equation}
is perfect. Thus $(E_1^{p,q,g})_{\mathcal{A}} \cong ((E_1^{p,d-q,g})_{\mathcal{A}^!})^\vee$.

\emph{Differential $d_1$}: The differential $d_1: E_1^{p,q,g} \to E_1^{p+1,q,g}$ is 
induced by the moduli space differential. Under Verdier duality:
\begin{equation}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "cor:duality-bar-complexes-complete" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 271

wave2_audit_20260413_001942/F04_definitions_complementarity.md:744:/bin/zsh -lc 'rg -n -F "cor:duality-bar-complexes-complete" chapters/theory/cobar_construction.tex chapters/theory/higher_genus_complementarity.tex chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wave2_audit_20260413_001942/F04_definitions_complementarity.md:799:chapters/theory/higher_genus_complementarity.tex:1128:\label{cor:duality-bar-complexes-complete}
wave2_audit_20260413_001942/F04_definitions_complementarity.md:800:chapters/theory/higher_genus_complementarity.tex:1137:\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
wave2_audit_20260413_001942/F04_definitions_complementarity.md:801:chapters/theory/higher_genus_complementarity.tex:1184:By Corollary~\ref{cor:duality-bar-complexes-complete}, the pairing:
wave2_audit_20260413_001942/F04_definitions_complementarity.md:802:chapters/theory/higher_genus_complementarity.tex:1378:(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
wave2_audit_20260413_001942/F04_definitions_complementarity.md:803:chapters/theory/higher_genus_complementarity.tex:1460:By Corollary~\ref{cor:duality-bar-complexes-complete}, the Verdier-Koszul pairing
wave2_audit_20260413_001942/F04_definitions_complementarity.md:804:chapters/theory/higher_genus_complementarity.tex:1967:configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
wave2_audit_20260413_001942/F04_definitions_complementarity.md:805:chapters/theory/higher_genus_complementarity.tex:1128:\label{cor:duality-bar-complexes-complete}
wave2_audit_20260413_001942/F04_definitions_complementarity.md:806:chapters/theory/higher_genus_complementarity.tex:1137:\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
wave2_audit_20260413_001942/F04_definitions_complementarity.md:807:chapters/theory/higher_genus_complementarity.tex:1184:By Corollary~\ref{cor:duality-bar-complexes-complete}, the pairing:
wave2_audit_20260413_001942/F04_definitions_complementarity.md:808:chapters/theory/higher_genus_complementarity.tex:1378:(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
wave2_audit_20260413_001942/F04_definitions_complementarity.md:809:chapters/theory/higher_genus_complementarity.tex:1460:By Corollary~\ref{cor:duality-bar-complexes-complete}, the Verdier-Koszul pairing
wave2_audit_20260413_001942/F04_definitions_complementarity.md:810:chapters/theory/higher_genus_complementarity.tex:1967:configuration-space residue pairing. Corollary~\ref{cor:duality-bar-complexes-complete}
audit_campaign_20260412_231034/T04_thm_C1.md:475:(Corollary~\ref{cor:duality-bar-complexes-complete}) with the
audit_campaign_20260412_231034/T04_thm_C1.md:843:   227	Corollary~\ref{cor:duality-bar-complexes-complete},
audit_campaign_20260412_231034/T04_thm_C1.md:946:/bin/zsh -lc 'rg -n "thm:verdier-duality-config-complete|cor:duality-bar-complexes-complete|lem:center-isomorphism|thm:kodaira-spencer-chiral-complete|lem:verdier-extension-exchange|lem:ss-duality-complete" chapters/theory/higher_genus_complementarity.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
audit_campaign_20260412_231034/T04_thm_C1.md:977:chapters/theory/higher_genus_complementarity.tex:1117:\label{cor:duality-bar-complexes-complete}
audit_campaign_20260412_231034/T04_thm_C1.md:978:chapters/theory/higher_genus_complementarity.tex:1126:\begin{proof}[Proof of Corollary~\ref{cor:duality-bar-complexes-complete}]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1180,1260p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\mathbf\\{C\\}_g\\(\\\\cA\\)\\"'^'"\\{\\\\vee\\\\vee\\}|can_\\{\\\\mathbf\\{C\\}_g\\}|biduality|perfect ambient complex|finite-dimensional total cohomology' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{lem:perfectness-criterion\\}|\\\\label\\{thm:fiber-center-identification\\}|\\\\label\\{cor:quantum-dual-complete\\}|\\\\label\\{cor:duality-bar-complexes-complete\\}|\\\\label\\{lem:center-isomorphism\\}' chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{equation}
\langle \eta, \xi \rangle = \text{Res}_{\partial \overline{C}_n(X)} (\eta \wedge \xi)
\end{equation}
where $\text{Res}$ denotes the Poincaré residue map.

This pairing is also perfect, by the logarithmic Poincar\'e lemma
(Deligne~\cite{Deligne71}, Hodge~II, Proposition~3.1.8), which
identifies $H^*(\Omega^*_{\log}(\overline{C}_n(X) \setminus D))
\cong H^*(C_n(X))$; the perfectness then follows from
Poincar\'e--Lefschetz duality for the smooth quasi-projective
variety~$C_n(X)$.
\end{proof}

\begin{corollary}[Duality for bar complexes; \ClaimStatusProvedHere]
\label{cor:duality-bar-complexes-complete}
The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
\begin{equation}
\langle -, - \rangle: \bar{B}^n(\mathcal{A}) \otimes \bar{B}^n(\mathcal{A}^!) \to 
\mathbb{C}
\end{equation}
 succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:290:\label{lem:perfectness-criterion}
chapters/theory/higher_genus_complementarity.tex:373:\label{thm:fiber-center-identification}
chapters/theory/higher_genus_complementarity.tex:1194:\label{cor:duality-bar-complexes-complete}
chapters/theory/higher_genus_complementarity.tex:1288:\label{cor:quantum-dual-complete}
chapters/theory/higher_genus_complementarity.tex:1548:\label{lem:center-isomorphism}
 succeeded in 52ms:
205:canonical biduality of the perfect ambient complex, combine to produce
221:\mathbf{C}_g(\cA)^{\vee\vee}[{-(3g{-}3)}][{3g{-}3}]
232:$\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
234:$\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
242:$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
276:\mathbf{C}_g(\cA)^{\vee\vee}$
277:for the canonical biduality map of
285:smooth proper DM stacks, and biduality is natural for perfect
287:returns the canonical biduality morphism
507:using the canonical biduality quasi-isomorphism of
678:biduality of the perfect ambient complex.
exec
/bin/zsh -lc "rg -n 'Q_g\\(\\\\cA\\) \\\\cong Q_g\\(\\\\cA\\"'^!'"\\)\\"'^'"\\{\\\\vee\\}|Q_0\\(\\\\cA\\)|Q_0\\(\\\\cA\\"'^!'"\\)|duality statement above cannot extend to genus~\\"'$0'"\\"'$|g '"\\\\ge 1' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
538:\textbf{Duality for $g \ge 1$.}\;
548:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
550:Hence the duality statement above cannot extend to genus~$0$
661:For $g \ge 1$, the duality
662:$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ is exactly the
668:$Q_0(\cA) = Z(\cA)$ and $Q_0(\cA^!) = 0$.
671:$Q_0(\cA) \cong Q_0(\cA^!)^{\vee}$ would force
680:statement in Stage~4 for $g \ge 1$ is taken directly from
721:$g \ge 1$, the total dimension
742:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
745:$Q_0(\cA) \cong Q_0(\cA^!)^{\vee}$ can hold.
759:$Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,\mathcal{Z}(\cA))$
760:and $Q_0(\cA^!)=0$.
764:If $Z(\cA)\neq 0$, then $Q_0(\cA)$ is nonzero while
765:$Q_0(\cA^!)=0$, so any putative duality
766:$Q_0(\cA) \cong Q_0(\cA^!)^{\vee}$ would force
958:Let $(\cA, \cA^!)$ be a chiral Koszul pair and $g \ge 1$.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "lem:center-isomorphism" -n chapters/theory/higher_genus_complementarity.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1440:Sublemma~\ref{lem:center-isomorphism} identifies
1548:\label{lem:center-isomorphism}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1500,1585p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
where $\lambda_1 = c_1(\mathbb{E})$ is the first Chern class of the Hodge bundle.
This is computed via the Gauss--Manin connection: the central charge $\kappa$ pairs with
the KS class $\partial/\partial\tau$ to give $\lambda_1$ (Mumford isomorphism).
\end{proof}

\emph{Step 8: Verdier involution and eigenspace decomposition.}

The anti-commutativity~\eqref{eq:verdier-ks-anticommute} is the key to the
eigenspace decomposition. We construct a canonical involution on $H^*(\overline{
\mathcal{M}}_g, Z(\mathcal{A}))$ whose $\pm 1$ eigenspaces give $Q_g(\mathcal{A})$
and $Q_g(\mathcal{A}^!)$.

\begin{lemma}[Verdier involution on moduli cohomology; \ClaimStatusProvedHere]
\label{lem:verdier-involution-moduli}
For a chiral Koszul pair $(\mathcal{A}, \mathcal{A}^!)$, Verdier duality on
$\overline{C}_n(X)$ together with the Koszul pairing $\mathcal{A} \otimes
\mathcal{A}^! \to \mathcal{O}_X$ induces an involution:
\begin{equation}
\sigma: H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) \xrightarrow{\sim}
H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '290,420p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1180,1325p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   290	\label{lem:perfectness-criterion}
   291	\index{perfectness criterion|textbf}
   292	\index{bar complex!relative perfectness|textbf}
   293	Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
   294	curve~$X$, carrying a modular pre-Koszul datum
   295	\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
   296	Write
   297	\[
   298	\barB^{(g)}_{\mathrm{flat}}(\cA)
   299	\;:=\;
   300	\bigl(\barB^{(g)}(\cA), \Dg{g}\bigr)
   301	\]
   302	for the strict flat comparison family of
   303	Convention~\textup{\ref{conv:higher-genus-differentials}}.
   304	Suppose the following two conditions hold:
   305	\begin{enumerate}[label=\textup{(\roman*)}]
   306	\item \emph{PBW filterability.}
   307	 The genus-$g$ bar complex $\bar{B}^{(g)}(\cA)$ admits an
   308	 exhaustive multiplicative filtration~$F_\bullet$ such that the
   309	 associated graded $\operatorname{gr}_F \bar{B}^{(g)}(\cA)$
 succeeded in 51ms:
  1180	\begin{equation}
  1181	\langle \eta, \xi \rangle = \text{Res}_{\partial \overline{C}_n(X)} (\eta \wedge \xi)
  1182	\end{equation}
  1183	where $\text{Res}$ denotes the Poincaré residue map.
  1184	
  1185	This pairing is also perfect, by the logarithmic Poincar\'e lemma
  1186	(Deligne~\cite{Deligne71}, Hodge~II, Proposition~3.1.8), which
  1187	identifies $H^*(\Omega^*_{\log}(\overline{C}_n(X) \setminus D))
  1188	\cong H^*(C_n(X))$; the perfectness then follows from
  1189	Poincar\'e--Lefschetz duality for the smooth quasi-projective
  1190	variety~$C_n(X)$.
  1191	\end{proof}
  1192	
  1193	\begin{corollary}[Duality for bar complexes; \ClaimStatusProvedHere]
  1194	\label{cor:duality-bar-complexes-complete}
  1195	The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
  1196	\begin{equation}
  1197	\langle -, - \rangle: \bar{B}^n(\mathcal{A}) \otimes \bar{B}^n(\mathcal{A}^!) \to 
  1198	\mathbb{C}
  1199	\end{equation}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1535,1585p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1535	\mathbb{D}': H^*(\bar{B}^{(g)}(\mathcal{A}^!)) \xrightarrow{\sim}
  1536	H^*(\bar{B}^{(g)}(\mathcal{A}))^\vee
  1537	\end{equation}
  1538	The composition $(\mathbb{D}')^\vee \circ \mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A}))
  1539	\to H^*(\bar{B}^{(g)}(\mathcal{A}))$ is the identity (by involutivity of Verdier
  1540	duality on compact smooth varieties, see Theorem~\ref{thm:verdier-duality-config-complete}).
  1541	
  1542	Now, the $E_2$ page of the Leray spectral sequence
  1543	(Theorem~\ref{thm:ss-quantum}) identifies both $Q_g(\mathcal{A})$ and
  1544	$Q_g(\mathcal{A}^!)$ as subquotients of $H^*(\overline{\mathcal{M}}_g,
  1545	Z(\mathcal{A}))$, using the following canonical identification of centers.
  1546	
  1547	\begin{lemma}[Center isomorphism via module Koszul duality; \ClaimStatusProvedHere]
  1548	\label{lem:center-isomorphism}
  1549	For a Koszul chiral pair $(\mathcal{A}, \mathcal{A}^!)$, there is a canonical
  1550	isomorphism $Z(\mathcal{A}) \cong Z(\mathcal{A}^!)$.
  1551	\end{lemma}
  1552	
  1553	\begin{proof}[Proof of Sublemma]
  1554	Since every $E_\infty$-chiral algebra is in particular an $E_1$-chiral algebra, and the Koszul property at the $E_\infty$ level implies Koszulity at the $E_1$ level (the forgetful functor is exact on bar complexes), we may apply the module Koszul duality equivalence
thinking
**Referencing lemma and corollary with line numbers**

I'm gathering exact line numbers for the lemma on perfectness and the corollaries about quantum duality, genus exceptions, and pairing, so I can reference them precisely in the user's summary following their formatting instructions. I'll use line numbering tools to pinpoint these in the source files.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '260,340p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   260	Part~(a): the inclusion $\operatorname{im}(p^+) \oplus \operatorname{im}(p^-)
   261	\hookrightarrow V$ is a quasi-isomorphism by direct-sum decomposition,
   262	and $\operatorname{im}(p^\pm) \simeq \operatorname{fib}(\sigma \mp \mathrm{id})$
   263	via the standard cone identification.
   264	Part~(b) follows by applying $H^*$ to~(a).
   265	Part~(c): for $x, y \in V^+$ we have $\sigma x = x$, $\sigma y = y$,
   266	so $\langle x, y \rangle = \langle \sigma x, \sigma y \rangle
   267	= -\langle x, y \rangle$, hence $\langle x, y \rangle = 0$.
   268	Maximality is immediate from the direct-sum decomposition.
   269	\end{proof}
   270	
   271	\begin{definition}[Relative bar fiber complex]\label{def:relative-bar-fiber}
   272	\index{bar complex!relative fiber|textbf}
   273	Let $(\cA, \cA^!)$ be a chiral Koszul pair on~$X$, and let
   274	\[
   275	\pi_g\colon \mathcal{C}_g(\cA) \longrightarrow
   276	\overline{\mathcal{M}}_g
   277	\]
   278	be the family of genus-$g$ compactified configuration spaces
   279	carrying the relative bar complex $\bar{B}^{(g)}(\cA)$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1180,1250p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1180	\begin{equation}
  1181	\langle \eta, \xi \rangle = \text{Res}_{\partial \overline{C}_n(X)} (\eta \wedge \xi)
  1182	\end{equation}
  1183	where $\text{Res}$ denotes the Poincaré residue map.
  1184	
  1185	This pairing is also perfect, by the logarithmic Poincar\'e lemma
  1186	(Deligne~\cite{Deligne71}, Hodge~II, Proposition~3.1.8), which
  1187	identifies $H^*(\Omega^*_{\log}(\overline{C}_n(X) \setminus D))
  1188	\cong H^*(C_n(X))$; the perfectness then follows from
  1189	Poincar\'e--Lefschetz duality for the smooth quasi-projective
  1190	variety~$C_n(X)$.
  1191	\end{proof}
  1192	
  1193	\begin{corollary}[Duality for bar complexes; \ClaimStatusProvedHere]
  1194	\label{cor:duality-bar-complexes-complete}
  1195	The Verdier duality on $\overline{C}_n(X)$ induces a perfect pairing:
  1196	\begin{equation}
  1197	\langle -, - \rangle: \bar{B}^n(\mathcal{A}) \otimes \bar{B}^n(\mathcal{A}^!) \to 
  1198	\mathbb{C}
  1199	\end{equation}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1270,1365p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1270	\begin{equation}
  1271	(E_{r+1})_{\mathcal{A}} = H(E_r, d_r)_{\mathcal{A}} \cong (H(E_r, d_r)_{\mathcal{A}^!})^\vee 
  1272	= ((E_{r+1})_{\mathcal{A}^!})^\vee
  1273	\end{equation}
  1274	
  1275	\emph{$E_\infty$ page}: Taking the limit $r \to \infty$:
  1276	\begin{equation}
  1277	(E_\infty^{p,q,g})_{\mathcal{A}} \cong ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee
  1278	\end{equation}
  1279	
  1280	But $E_\infty^{*,*,g} = \text{gr}^g H^*$ by definition, so:
  1281	\begin{equation}
  1282	\text{gr}^g H^{p+q}(\bar{B}(\mathcal{A})) \cong (\text{gr}^g H^{p+d-q}(\bar{B}(
  1283	\mathcal{A}^!)))^\vee
  1284	\end{equation}
  1285	\end{proof}
  1286	
  1287	\begin{corollary}[Quantum corrections are dual; \ClaimStatusProvedHere]
  1288	\label{cor:quantum-dual-complete}
  1289	For each genus $g \geq 1$ and every Koszul dual chiral pair
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1520,1595p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1520	\end{equation}
  1521	satisfying $\sigma^2 = \mathrm{id}$.
  1522	\end{lemma}
  1523	
  1524	\begin{proof}[Proof of Lemma~\ref{lem:verdier-involution-moduli}]
  1525	\emph{Construction.}
  1526	By Corollary~\ref{cor:duality-bar-complexes-complete}, the Verdier-Koszul pairing
  1527	identifies:
  1528	\begin{equation}
  1529	\mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A})) \xrightarrow{\sim}
  1530	H^*(\bar{B}^{(g)}(\mathcal{A}^!))^\vee
  1531	\end{equation}
  1532	Since $(\mathcal{A}^!)^! \simeq \mathcal{A}$ (Koszul involutivity,
  1533	Theorem~\ref{thm:chiral-koszul-duality}), we also have:
  1534	\begin{equation}
  1535	\mathbb{D}': H^*(\bar{B}^{(g)}(\mathcal{A}^!)) \xrightarrow{\sim}
  1536	H^*(\bar{B}^{(g)}(\mathcal{A}))^\vee
  1537	\end{equation}
  1538	The composition $(\mathbb{D}')^\vee \circ \mathbb{D}: H^*(\bar{B}^{(g)}(\mathcal{A}))
  1539	\to H^*(\bar{B}^{(g)}(\mathcal{A}))$ is the identity (by involutivity of Verdier



exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '360,430p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   360	cohomology sheaves
   361	$\mathcal{H}^q(R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA))$ vanish for
   362	$q \neq 0$ uniformly over the base, and the surviving
   363	degree-$0$ cohomology sheaf has
   364	finite-dimensional fibers by hypothesis~(ii). The standard
   365	cohomology and base change theorem
   366	(EGA~III, Th\'eor\`eme~7.7.5)
   367	then gives that $R\pi_{g*}\bar{B}^{(g)}_{\mathrm{flat}}(\cA)$ is a perfect
   368	complex (bounded, with coherent cohomology sheaves) on
   369	$\overline{\mathcal{M}}_g$.
   370	\end{proof}
   371	
   372	\begin{theorem}[Fiber--center identification \textup{(Theorem~\texorpdfstring{$\mathrm{C}_0$}{C0})}; \ClaimStatusProvedHere]
   373	\label{thm:fiber-center-identification}
   374	\index{fiber--center identification|textbf}
   375	\textup{[}Regime: curved-central
   376	\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
   377	
   378	\smallskip\noindent
   379	Assume $\cA$ carries a modular pre-Koszul datum


thinking
**Summarizing key hypotheses and references for perfectness and bidualizability**

I’m organizing a clear bullet list referencing the relevant lemmas, theorems, and corollaries from `chapters/theory/higher_genus_complementarity.tex` with exact line numbers. This will address the user’s question about what hypotheses ensure the ambient complex is perfect or bidualizable, tying in PBW filterability, finite-dimensional fibers, and the canonical isomorphisms involved. I’m also including details on the quantum duality for genus ≥1 and the genus 0 exception, making sure to link each point with the precise file and line references. The goal is a concise, well-structured, plain-text summary that directly answers the question with supporting citations.
codex
- **Perfectness hypothesis.** `lem:perfectness-criterion` (chapters/theory/higher_genus_complementarity.tex:293-324) says that a modular pre-Koszul chiral pair whose genus‑$g$ bar admits the PBW filtration satisfying MK1+MK3 (so the graded piece is Koszul-acyclic) and whose strict flat fiber bar has finite-dimensional cohomology at every closed point yields a perfect derived pushforward $R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA)$ on $\overline{\mathcal{M}}_g$ (the uniform vanishing range plus base change give bounded coherent cohomology, see lines 360-369). 
- **Ordinary realization / ambient biduality.** `thm:fiber-center-identification` (chapters/theory/higher_genus_complementarity.tex:372-427) then upgrades the coderived curved model to an ordinary perfect complex on the flat locus: whenever that perfectness holds (by the lemma above) the higher cohomology of $R\pi_{g*}\barB^{(g)}_{\mathrm{flat}}(\cA)$ vanishes and the surviving $H^0$ is identified with the center local system $\mathcal{Z}_\cA$, recovering the original fiber model when $\kappa(\cA)=0$. Together with `cor:duality-bar-complexes-complete` (chapters/theory/higher_genus_complementarity.tex:1193-1219) and `lem:center-isomorphism` (chapters/theory/higher_genus_complementarity.tex:1547-1571), this means the ambient bar complex carries the perfect Verdier pairing and a canonical Koszul-induced isomorphism $Z(\cA)\cong Z(\cA^!)$, so the ambient object is reflexive/bidualizable once the PBW+finite-dimensional hypotheses hold. 
- **Q_g duality and genus‑0 exception.** `cor:quantum-dual-complete` (chapters/theory/higher_genus_complementarity.tex:1287-1314) asserts $Q_g(\cA)\cong Q_g(\cA^!)^\vee$ for every genus $g\geq 1$ using the Verdier-perfect pairing, while recording that at genus zero the “cohomological shadow” eigenspaces are instead $Q_0(\cA)=H^0(\overline{\mathcal{M}}_0,Z(\cA))$ and $Q_0(\cA^!)=0$ (theorem C1 records that separately), so no duality between nonzero $Q_0$’s is claimed.


thinking
**Clarifying theorems and constructions**

I need to identify if Theorem 1 has been fixed by the quantum-dual-complete dependency. If the user's findings come from an outdated file, I should check for contradictions in the local statement. It might help to clarify with a condition like g≥1 in the title or proof, though that might be unnecessary. Regarding Finding 2, it appears that the construction’s use of finite-dimensional total cohomology holds up, but I should ensure the assumptions about the sigma construction are clear.
thinking
**Examining theorem assumptions**

The construction suggests I combine the Lemma perfectness criterion with the Theorem fiber-center identification. It states that on the modular Koszul locus, C_g(A) acts as derived global sections of a perfect complex on Mbar_g, which means it's a perfect complex over C. However, I’m wondering if just assuming finite-dimensional fiber-cohomology is enough for the construction. The Lemma perfectness criterion requires PBW filterability as well. But perhaps Proposition ambient properties provides finite-dimensional total cohomology independently, making the assumption sufficient after all.
thinking
**Clarifying construction details**

I need to clearly state that canonical biduality is justified by finite total cohomology, not by fiber-center perfection. It might also be a good idea to revise the wording in the construction to make it more straightforward. Additionally, I should explore whether the part (i) of the proposition ambient properties only provides finite-dimensionality. And I need to check if this part relies solely on the Lemma perfectness-criterion (ii). Let’s ensure everything aligns logically!
thinking
**Evaluating corollary proof**

I’m considering whether we can still make a corollary proof without implying genus-0 duality. To be cautious, I might need to adjust the corollary title or add a note stating that no genus-0 duality is asserted. Hmm, I should also inspect if there are any uses of `Q_g(A) ≅ Q_g(A^!)^∨` for all g elsewhere in the file to ensure everything aligns properly. It's all a bit intricate, but I’m on it!
thinking
**Clarifying decomposition and duality**

I’m thinking about line 694 and the corollary exchange principle. It seems like this line should clarify that at genus0, it’s just a decomposition statement, not a duality statement. But wait, the corollary doesn't mention duality. Maybe line 694 is referencing a proof or a later comment about symmetry in a more generic way. I should check around line 694 again. It looks like the corollary focuses on decomposition symmetry, which is fine. Line 476 might correspond to theorem statement line 538, but it’s hard to know for sure.
thinking
**Evaluating theorem structure**

I think a simple, explicit sentence in the theorem and subsection intro might be sufficient. I may need to use the pre-edit verification protocol PE-10 because of the theorem's scope quantifier. Additionally, I should fill the commentary block before any editing takes place. There's also a possibility that no label creation will be necessary. But hmm, I think I’ll just wait for the explorer's insights before making any final decisions.
collab wait(call_3vw6XGyT3bqFaF8yyLUUQaf1)
  receivers: 019d8675-d21a-7a83-9f8d-ea5035455f43
wait(call_3vw6XGyT3bqFaF8yyLUUQaf1) 1 agents complete:
  019d8675-d21a-7a83-9f8d-ea5035455f43 completed: "- **Perfectness hypothesis.** `lem:perfectness-criterion` (chapters/theory/higher_genus_complementarity.tex:293-324) say…"


thinking
**Deciding on edits**

I need to determine the edits now. I’m thinking of adding a lemma and possibly fixing finding 1 with an explicit sentence in a subsection or theorem. I’ll be using apply_patch only and will provide commentary before making edits. It might be wise to show PE-10 since the scope quantifier is involved. For finding 2, which isn’t in the templates, I can still mention the justification. I should also check for label uniqueness across volumes before proceeding with any edits.
thinking
**Considering actions for edits**

I need to follow action safety, which says I can only edit a specific file, while reading other volumes is fine. Regarding label uniqueness, I’m thinking I could avoid creating a new label by folding a lemma into an existing proposition. Still, adding a new labeled lemma might be the strongest option. I wonder if I could make the lemma unlabeled, but then the theorem might need it. It seems better to have a label after checking its uniqueness across volumes.
codex
I’ve verified the dependency chain. The strongest clean fix is to formalize the biduality step instead of merely asserting it: I’m adding a short local lemma that proves `\mathbf{C}_g(\cA) \to \mathbf{C}_g(\cA)^{\vee\vee}` is a quasi-isomorphism from finite-dimensional total cohomology, and I’m tightening the eigenspace subsection so the genus-0 exception is stated before any reader can misread the duality as genus-uniform.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '120,250p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   120	is the S-level (shadow) object; and the bar complex
   121	$(\barB^{(g)}(\cA), \Dg{g})$ is the M-level (model) object.
   122	\end{remark}
   123	
   124	\begin{proposition}[Properties of the holographic ambient complex;
   125	\ClaimStatusProvedHere]
   126	\label{prop:thqg-III-ambient-properties}
   127	\index{holographic ambient complex!properties}
   128	The holographic ambient complex
   129	$\mathbf{C}_g(\cA)$ satisfies:
   130	\begin{enumerate}[label=\textup{(\roman*)}]
   131	\item \emph{Finite-dimensionality.}
   132	 For each $n \in \mathbb{Z}$,
   133	 $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
   134	 $\mathbb{C}$, and is nonzero only for
   135	 $0 \le n \le 6g - 6$.
   136	
   137	\item \emph{Verdier self-duality.}
   138	 The Koszul pairing
   139	 $\cA \otimes \cA^! \to \omega_X$ and the center isomorphism
exec
/bin/zsh -lc "rg -n 'label\\{lem:thqg-III-ambient-biduality\\}|label\\{lem:thqg-III-biduality\\}|label\\{lem:ambient-biduality\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 131ms:

exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '488,560p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   488	\label{subsec:thqg-III-eigenspace-decomposition}
   489	\index{eigenspace decomposition!holographic|textbf}
   490	\index{complementarity!C1 decomposition}
   491	
   492	Under the finite-dimensional fiber-cohomology hypothesis needed
   493	for Construction~\ref{constr:thqg-III-verdier-involution}, the
   494	eigenspace decomposition~(C1) holds on the Koszul locus without
   495	any additional nondegeneracy hypothesis.
   496	We give a self-contained proof in the holographic setting.
   497	
   498	\begin{theorem}[Holographic eigenspace decomposition (C1);
   499	\ClaimStatusProvedHere]
   500	\label{thm:thqg-III-eigenspace-decomposition}
   501	\index{Lagrangian!eigenspace decomposition!holographic}
   502	Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
   503	curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
   504	Assume the finite-dimensional fiber-cohomology hypothesis of
   505	Lemma~\ref{lem:perfectness-criterion}(ii), so that
   506	Construction~\ref{constr:thqg-III-verdier-involution} is defined
   507	using the canonical biduality quasi-isomorphism of



thinking
**Evaluating cohomology properties**

I'm considering that Proposition ambient properties(i) indicates finite-dimensional total cohomology. When dealing with a field, a complex with this trait is quasi-isomorphic to a bounded complex of finite-dimensional vector spaces, and thus is perfect. However, the invalid bound line isn't critical. I'm wondering if the finite-dimensional total cohomology part of the proposition could still be acceptable, even if it doesn’t provide an exact upper bound? There seems to be a lot to unpack here!
thinking
**Evaluating section intro**

I’m considering whether I should add subsection intro lines 492-496. It seems that the splitting is genus-uniform, but the duality between summands only begins at genus 1, with genus 0 being the key exception. I think this offers a minimal yet strong clarification that might be really helpful in understanding the context. I want to make sure I clearly convey this distinction in the writing.
thinking
**Considering heading changes**

I'm thinking about altering the heading from "Duality for g ≥ 1" to "Duality begins at g ≥ 1" to clarify the meaning. I could also consider adding the word "only" to emphasize exclusivity. This might help users grasp the concept better, but I want to ensure it still communicates the intended message clearly. It’s all about making it as clear as possible, right? Let's see if changing the wording improves the readability!
codex
```
PE-10
genus: all, split as [all for decomposition] + [g>=1 for duality] + [g=0 boundary]
degree: NA
AP32 weight tag: NA
AP139 free-var audit: LHS vars {g,\cA} RHS vars {g,\cA} LHS⊇RHS? Y
AP36: implies/iff = implies only
verdict: ACCEPT
```

```
PE-7
environment: lemma
label: \label{lem:thqg-III-ambient-biduality}
prefix match (AP125): Y
AP124 duplicate check: Vol I:0 Vol II:0 Vol III:0 total before:0 after:1 delta=1? Y
verdict: ACCEPT
```

I’m applying a scoped patch now: one formal biduality lemma plus explicit genus scoping language where the eigenspace theorem is introduced and invoked.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex
@@ -133,4 +133,3 @@
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
@@ -159,6 +158,5 @@
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
@@ -172,3 +170,6 @@
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
@@ -196,2 +197,28 @@
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
@@ -204,3 +231,4 @@
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
@@ -234,3 +262,3 @@
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
@@ -240,6 +268,6 @@
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
@@ -494,3 +522,5 @@
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
@@ -504,6 +534,8 @@
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
@@ -537,3 +569,3 @@
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
apply_patch(auto_approved=true) exited 0 in 31ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..0f016e4e880422688aa0e595bce11f08df00164f
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -232,16 +260,16 @@
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +520,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +532,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +567,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..0f016e4e880422688aa0e595bce11f08df00164f
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -232,16 +260,16 @@
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +520,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +532,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +567,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

codex
The patch is in. I’m re-reading the touched theorem surface now, checking the new biduality lemma against the construction/proof that uses it and making sure the genus-0 exception is visible before any downstream duality language.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '488,690p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '124,285p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'lem:thqg-III-ambient-biduality|Duality only for \\"'$g '"\\\\ge 1\\"'$|genus~'"\\"'$0'"\\"'$ is the sharp center-valued boundary case|canonical biduality quasi-isomorphism of '"\\\\mathbf\\{C\\}_g\\(\\\\cA\\)' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
200:\label{lem:thqg-III-ambient-biduality}
233:Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
263:One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
525:only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
537:Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
570:\textbf{Duality only for $g \ge 1$.}\;
 succeeded in 52ms:
   488	
   489	\begin{proof}
   490	The degree is $-(3g - 3) = -\dim_{\mathbb{C}}
   491	\overline{\mathcal{M}}_g$, which is the Verdier shift for
   492	Serre duality on a smooth variety of dimension $3g - 3$.
   493	The three cases follow by substituting $g = 0, 1, \ge 2$.
   494	\end{proof}
   495	
   496	\begin{remark}[Genus $1$ distinguished]
   497	\label{rem:thqg-III-genus-1-special}
   498	\index{genus 1!holographic pairing}
   499	At genus~$1$, $\dim \overline{\mathcal{M}}_{1,1} = 1$
   500	but $\dim \overline{\mathcal{M}}_1 = 0$ (a point for the
   501	coarse moduli). The relevant moduli space for marked curves
   502	is $\overline{\mathcal{M}}_{1,1}$, where the pairing has
   503	degree~$0$. This is the reason genus~$1$ complementarity
   504	has the simplest form:
   505	$Q_1(\cA) \oplus Q_1(\cA^!) \cong H^*(\overline{\mathcal{M}}_{1,1},
   506	\mathcal{Z}(\cA))$ with a classical (unshifted) pairing.
   507	\end{remark}
 succeeded in 52ms:
   124	\begin{proposition}[Properties of the holographic ambient complex;
   125	\ClaimStatusProvedHere]
   126	\label{prop:thqg-III-ambient-properties}
   127	\index{holographic ambient complex!properties}
   128	The holographic ambient complex
   129	$\mathbf{C}_g(\cA)$ satisfies:
   130	\begin{enumerate}[label=\textup{(\roman*)}]
   131	\item \emph{Finite-dimensionality.}
   132	 For each $n \in \mathbb{Z}$,
   133	 $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
   134	 $\mathbb{C}$, and only finitely many cohomological degrees occur.
   135	
   136	\item \emph{Verdier self-duality.}
   137	 The Koszul pairing
   138	 $\cA \otimes \cA^! \to \omega_X$ and the center isomorphism
   139	 $Z(\cA) \cong Z(\cA^!)$
   140	 (Lemma~\ref{lem:center-isomorphism}) induce a
   141	 quasi-isomorphism of constructible sheaves on
   142	 $\overline{\mathcal{M}}_g$:
   143	 \begin{equation}\label{eq:thqg-III-verdier-self-duality}
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..0f016e4e880422688aa0e595bce11f08df00164f
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -232,16 +260,16 @@
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +520,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +532,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +567,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.






thinking
**Evaluating LaTeX options**

For LaTeX, I think a good approach might be `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, but perhaps it's a bit too heavy. A simpler option could be `python scripts/verify_labels.py` if it exists. Since the user hasn't asked for anything extensive, I might just run a local command to check for specific references. I should consider if a new lemma proof introduces any assumptions, but it seems like it does. Good to verify that!
thinking
**Clarifying mathematical notation**

I’m realizing there’s some confusion about the `\mathbb{D}` arrow, which goes from the ambient complex to the dual of the ambient complex of A^!. The current line references cor:duality-bar-complexes-complete, but I think it should state Proposition ambient properties(ii) instead for better accuracy. It's essential to clarify this in the construction because the self-duality and Koszul involutivity are key concepts. Should I fix this to improve accuracy? It seems important to address this.
thinking
**Improving mathematical clarity**

I think I need to change the line to clarify that "Here, \mathbb{D} is the map induced on derived global sections by the Verdier self-duality quasi-isomorphism." This seems to originate from Corollary cor:duality-bar-complexes-complete after the fiber-center identification. It should help strengthen the proof and eliminate inconsistencies, especially considering the user's request for the strongest technical choice. Additionally, I should mention "via Proposition ambient properties(ii)" in the construction description. It looks like I may also need to patch some other parts, including the theorem proof.
thinking
**Noting theorem assumptions**

I'm recognizing a potential concern with the new lemma that states, "Under the finite-dimensionality statement of Proposition...". The problem is that the theorem assumption only addresses finite-dimensional fiber-cohomology and doesn't explicitly mention the proposition. This distinction seems important, so I should clarify the wording to avoid any misunderstandings. It’s good I caught this issue before finalizing things. Keeping things accurate is key, and I want to make sure everything aligns properly!
thinking
**Adjusting complex definitions**

I'm figuring out that the concept of "complex" is defined as the RGamma of the center local system, not derived from the pushforward bar complex. Alright, that’s clear. I think I might need to patch lines 255-256. Also, I want to adjust the wording around "One route to Lemma... is to combine Lemma perfectness criterion with Theorem fiber-center identification." It seems like a good idea to make that small patch too! Let's get to it.
codex
I found one remaining local mismatch in the construction prose: the `\mathbb{D}` arrow there should be attributed first to the ambient Verdier self-duality already proved in this file, not directly to the earlier bar-complex corollary. I’m tightening that reference now so the construction’s evidence chain is exact end-to-end.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex
@@ -254,4 +254,6 @@
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
apply_patch(auto_approved=true) exited 0 in 35ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..4ead75cfed851c2849362c4207ca18eac84cef0c
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -224,24 +252,26 @@
 \mathbf{C}_g(\cA)
 \end{tikzcd}
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +522,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +534,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +569,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..4ead75cfed851c2849362c4207ca18eac84cef0c
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -224,24 +252,26 @@
 \mathbf{C}_g(\cA)
 \end{tikzcd}
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +522,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +534,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +569,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

codex
The text-level re-read is coherent. I’m doing one build-oriented verification pass now; if the monograph compile fails for unrelated reasons I’ll separate that from the local rectification, but I want to catch any immediate LaTeX breakage from the new lemma/reference surface.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..4ead75cfed851c2849362c4207ca18eac84cef0c
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -224,24 +252,26 @@
 \mathbf{C}_g(\cA)
 \end{tikzcd}
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +522,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +534,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +569,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

 exited 12 in 1.40s:
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
  chapters/theory/chiral_koszul_pairs.tex
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..4ead75cfed851c2849362c4207ca18eac84cef0c
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -224,24 +252,26 @@
 \mathbf{C}_g(\cA)
 \end{tikzcd}
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +522,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +534,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +569,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

codex
The compile check did not reach this chapter cleanly: `latexmk` failed while reading the pre-existing `main.aux`, with a runaway `\@writefile` and many unrelated undefined references before the document body finished. I’m doing one final source-only diff/readback on the edited file, then I’ll close with exactly what changed and what the build check did not verify.
exec
/bin/zsh -lc "rg -n '\\\\ref\\{lem:thqg-III-ambient-biduality\\}|\\\\label\\{lem:thqg-III-ambient-biduality\\}|Q_0\\(\\\\cA\\) = Z\\(\\\\cA\\), \\\\qquad Q_0\\(\\\\cA\\"'^!'"\\) = 0|Duality only for \\"'$g '"\\\\ge 1\\"'$'"' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/connections/thqg_symplectic_polarization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
200:\label{lem:thqg-III-ambient-biduality}
233:Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
265:One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
539:Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
572:\textbf{Duality only for $g \ge 1$.}\;
582:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
776:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
 succeeded in 52ms:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa..4ead75c 100644
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@ $\mathbf{C}_g(\cA)$ satisfies:
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@ $\mathbf{C}_g(\cA)$ satisfies:
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..4ead75cfed851c2849362c4207ca18eac84cef0c
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -224,24 +252,26 @@
 \mathbf{C}_g(\cA)
 \end{tikzcd}
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +522,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +534,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +569,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

Plan update
The target file has been patched and re-read; local label/reference checks passed. A full monograph compile was attempted but failed in pre-existing auxiliary/reference state outside the edited surface.
  ✓ Read live repo invariants, target file, and cited dependencies for the two findings
  ✓ Verify the exact contradiction and the biduality/perfectness hypothesis gap on the local theorem surface
  ✓ Patch the file with the minimum truthful scope/hypothesis changes
  ✓ Re-read modified sections and run targeted checks for labels, refs, and coherence
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..4ead75cfed851c2849362c4207ca18eac84cef0c
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -224,24 +252,26 @@
 \mathbf{C}_g(\cA)
 \end{tikzcd}
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +522,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +534,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +569,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.


thinking
**Organizing the output summary**

I need to produce a final concise summary that includes a mention of a build failure, which is unrelated to the main issue. I tried to compile, but it failed due to a runaway in main.aux and undefined references. I want a structured output that ends with `## Rectification Summary`, including bullet points with statuses. I might also mention any files that were changed, along with findings resolved, and keep it concise with two short sections. No nested bullets!
codex
Edited [chapters/connections/thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex).

I strengthened the `\sigma` construction rather than just adding a warning: the file now has a proved local lemma `lem:thqg-III-ambient-biduality` establishing that `\mathbf{C}_g(\cA) \to \mathbf{C}_g(\cA)^{\vee\vee}` is a quasi-isomorphism from finite-dimensional total cohomology. The construction and the C1 theorem now cite that lemma explicitly, and the Verdier arrow is attributed to the ambient self-duality proved in this file rather than loosely to the earlier bar-complex corollary.

I also made the genus scope impossible to miss on the eigenspace surface: the subsection introduction now says the splitting holds for all `g \ge 0` but the perfect duality starts only at `g \ge 1`, and the theorem header now reads “Duality only for `g \ge 1`,” with the genus-0 boundary `Q_0(\cA)=Z(\cA), Q_0(\cA^!)=0` left explicit. I also removed the incorrect universal range `0 \le n \le 6g-6` from the ambient-complex finite-dimensionality statement and replaced it with the truthful boundedness statement needed for biduality.

Verification: I re-read the modified sections and checked the new label/reference usage locally. I also attempted `latexmk -pdf main.tex`, but the run failed before a clean chapter-level verification because `main.aux` is already in a broken state (`Runaway argument ... while scanning use of \@writefile`) with many unrelated undefined refs/citations outside this edit.

## Rectification Summary
- [FIXED] finding 1 — made the genus split explicit on the C1 surface: decomposition for all `g \ge 0`, duality only for `g \ge 1`, with the genus-0 exception `Q_0(\cA)=Z(\cA), Q_0(\cA^!)=0` foregrounded.
- [FIXED] finding 2 — added a proved ambient-biduality lemma so the use of `\mathbf{C}_g(\cA)^{\vee\vee}` now rests on explicit perfectness/bidualizability, not an implicit reflexivity assumption.
- [FIXED] local coherence issue discovered during re-read — replaced the false finite-dimensionality range bound with a bounded-cohomology statement compatible with genus 0 and the biduality argument.
- [BLOCKED] full build verification — `latexmk` failed on pre-existing auxiliary/reference corruption in `main.aux`, so I could not use the monograph build as final evidence for this local edit.
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 43412aa12dab5afb95b138e78b927ea76d087a8c..4ead75cfed851c2849362c4207ca18eac84cef0c
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -131,8 +131,7 @@
 \item \emph{Finite-dimensionality.}
  For each $n \in \mathbb{Z}$,
  $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
- $\mathbb{C}$, and is nonzero only for
- $0 \le n \le 6g - 6$.
+ $\mathbb{C}$, and only finitely many cohomological degrees occur.
 
 \item \emph{Verdier self-duality.}
  The Koszul pairing
@@ -157,10 +156,9 @@
 
 \begin{proof}
 \emph{Part (i).}
-The cohomological dimension of $\overline{\mathcal{M}}_g$ is
-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
-by Artin vanishing for proper DM stacks
-\cite[\S4.1]{Olsson16}. The stalks of
+$\mathbf{C}_g(\cA)$ is the derived global sections of a
+constructible complex on the proper Noetherian DM stack
+$\overline{\mathcal{M}}_g$. The stalks of
 $\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
 (finite-dimensional flat fiber cohomology,
 Lemma~\ref{lem:perfectness-criterion}(ii)).
@@ -170,7 +168,10 @@
 is a constructible sheaf on the Noetherian stack
 $\overline{\mathcal{M}}_g$. Cohomology of a constructible
 sheaf on a Noetherian DM stack is finite-dimensional
-\cite[Theorem~18.1.1]{SAG}.
+\cite[Theorem~18.1.1]{SAG}, and proper DM stacks have finite
+cohomological dimension \cite[\S4.1]{Olsson16}. Hence
+$H^*(\mathbf{C}_g(\cA))$ is finite-dimensional in each degree and
+vanishes outside a finite range.
 
 \emph{Part (ii).}
 The Koszul pairing restricts to a perfect pairing on centers
@@ -194,6 +195,32 @@
 functoriality.
 \end{proof}
 
+\begin{lemma}[Canonical biduality for the ambient complex;
+\ClaimStatusProvedHere]
+\label{lem:thqg-III-ambient-biduality}
+\index{ambient complex!canonical biduality}
+Under the finite-dimensionality statement of
+Proposition~\ref{prop:thqg-III-ambient-properties}(i), the canonical
+evaluation morphism
+\[
+\mathrm{can}_{\mathbf{C}_g}\colon
+\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)^{\vee\vee}
+\]
+is a quasi-isomorphism.
+\end{lemma}
+
+\begin{proof}
+Over the field~$\mathbb{C}$, a complex is perfect if and only if it
+is quasi-isomorphic to a bounded complex of finite-dimensional vector
+spaces. Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology for $\mathbf{C}_g(\cA)$, so
+$\mathbf{C}_g(\cA)$ is perfect in $D(\mathbb{C})$. For a bounded
+finite-dimensional complex, evaluation into the double dual is an
+isomorphism termwise, hence a quasi-isomorphism. Transporting this
+along any perfect representative gives the canonical biduality
+quasi-isomorphism above.
+\end{proof}
+
 \begin{construction}[Verdier involution on the ambient complex]
 \label{constr:thqg-III-verdier-involution}
 \index{Verdier involution!construction|textbf}
@@ -202,7 +229,8 @@
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
 (Theorem~\ref{thm:chiral-koszul-duality}), together with the
-canonical biduality of the perfect ambient complex, combine to produce
+canonical biduality quasi-isomorphism of
+Lemma~\ref{lem:thqg-III-ambient-biduality}, combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -224,24 +252,26 @@
 \mathbf{C}_g(\cA)
 \end{tikzcd}
 \end{equation}
-Here $\mathbb{D}$ is the Verdier duality map from
-Corollary~\ref{cor:duality-bar-complexes-complete},
+Here $\mathbb{D}$ is the map on derived global sections induced by the
+Verdier self-duality
+\eqref{eq:thqg-III-verdier-self-duality} of
+Proposition~\ref{prop:thqg-III-ambient-properties}(ii),
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and
 $\mathrm{can}_{\mathbf{C}_g}$ denotes the canonical biduality
 quasi-isomorphism
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA)^{\vee\vee}$.
-One way to see this canonically is to combine
+One route to Lemma~\ref{lem:thqg-III-ambient-biduality} is to combine
 Lemma~\ref{lem:perfectness-criterion} with
 Theorem~\ref{thm:fiber-center-identification}: on the modular
 Koszul locus, $\mathbf{C}_g(\cA)$ is the derived global sections of
 a perfect complex on $\overline{\mathcal{M}}_g$, hence is itself a
 perfect complex over~$\mathbb{C}$. Equivalently,
-Proposition~\ref{prop:thqg-III-ambient-properties}(i) shows that
-$\mathbf{C}_g(\cA)$ has finite-dimensional total cohomology, which
-is the same perfection statement over a field. Thus no choice of a
-bounded finite-dimensional model is needed.
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional total cohomology, which over a field is the same
+perfection statement. Thus no separate reflexivity hypothesis and no
+choice of a bounded finite-dimensional model are needed.
 The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
@@ -492,7 +522,9 @@
 Under the finite-dimensional fiber-cohomology hypothesis needed
 for Construction~\ref{constr:thqg-III-verdier-involution}, the
 eigenspace decomposition~(C1) holds on the Koszul locus without
-any additional nondegeneracy hypothesis.
+any additional nondegeneracy hypothesis. The splitting is valid for
+all $g \ge 0$, but the perfect duality between the two summands starts
+only at genus~$1$; genus~$0$ is the sharp center-valued boundary case.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -502,10 +534,12 @@
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 Assume the finite-dimensional fiber-cohomology hypothesis of
-Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Lemma~\ref{lem:perfectness-criterion}(ii). Then
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) and
+Lemma~\ref{lem:thqg-III-ambient-biduality} supply the canonical
+biduality quasi-isomorphism of $\mathbf{C}_g(\cA)$, so
 Construction~\ref{constr:thqg-III-verdier-involution} is defined
-using the canonical biduality quasi-isomorphism of
-$\mathbf{C}_g(\cA)$.
+for every such genus.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -535,7 +569,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality for $g \ge 1$.}\;
+\textbf{Duality only for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.

tokens used
201,328
