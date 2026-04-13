# R17_free_fields (265s)

Edited [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:705), [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1152), and [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1180) to make the slice/global distinction explicit. The weight-changing line now clearly means the pure one-dimensional slice, and the global `r_{\max}=4` witness is stated to live on the mixed charged stratum rather than on either one-dimensional line. I re-read the modified section and checked the referenced labels by grep; I did not run a full TeX build.

## Rectification Summary
- [FIXED] T16 vanishing-line contradiction — the weight-changing-line proposition now says `pure weight-changing line` and explicitly excludes both the Virasoro T-line and the mixed charged stratum from its scope.
- [FIXED] T16 depth-gap witness ambiguity — the global-depth theorem now states that `r_{\max}=4` is realized by the quartic contact class on the mixed charged stratum; it also says the pure weight-changing slice vanishes while the T-line is class `M`.
- [FIXED] T16 theorem/proof coherence — the proof now states that the class~C witness is mixed, and the quartic class is identified as the last nontrivial global shadow component rather than something visible on an isolated line.
- [FIXED] Local overview consistency — the earlier beta-gamma archetype remark was aligned with the theorem: weight-changing slice vanishes, T-line remains infinite, mixed charged stratum realizes the class~C witness.


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
session id: 019d8685-0f96-7a83-8600-13e0786436b1
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


TARGET: chapters/examples/free_fields.tex

FINDINGS TO FIX:

1. [CRITICAL T16] Line ~1148-1166: A proved proposition says the entire betagamma shadow tower
   vanishes on some line. This contradicts the depth-gap theorem's claim that betagamma has
   d_alg=2 (realized r_max=4).
   FIX: Read the proposition carefully. Determine WHICH line the shadow tower vanishes on
   vs which line d_alg=2 is claimed on. They may be different lines (weight-changing vs standard).
   If they're the same line: the depth gap witness is wrong and needs replacement.
   If they're different: add clarification about which line realizes d_alg=2.

Also check line ~1171 for the betagamma global-depth theorem contradiction with T-line.

Read the file, verify, resolve the contradiction.
mcp startup: no servers
codex
Using `beilinson-rectify` for a local theorem-surface repair in [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex). I’m reading the required constitutional files plus the target section to lock the exact contradiction before editing.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 52ms:
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
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1080,1225p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 52ms:
\item \emph{The stress tensor line}
 (T-line): the one-dimensional slice corresponding to
 the Virasoro subalgebra at central charge
 $c = c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$.
 On this line the shadow data coincides with that of
 $\mathrm{Vir}_{c}$.
\item \emph{The weight-changing line}: the deformation that shifts the
 conformal weight $\lambda \mapsto \lambda + \epsilon$. On this line
 all transferred higher brackets vanish
 ($\ell_n^{\mathrm{tr}}|_{L} = 0$ for $n \geq 2$),
 so the shadow obstruction tower is purely quadratic by rank-one abelian rigidity
 (Theorem~\textup{\ref{thm:betagamma-rank-one-rigidity}}).
\end{enumerate}
The $\beta\gamma$ system is \emph{not} a scalar-lane algebra:
the two directions carry independent shadow data, and the
global tower depends on their interaction.
\end{proposition}

\begin{proof}
Direction~(i): the stress tensor $T(z)$ of the $\beta\gamma$ system
codex
The local split is already visible: the file distinguishes a `T`-line from a weight-changing line, and the vanishing proposition is written for the weight-changing slice only. I’m reading the surrounding beta-gamma lane to check whether the later global-depth theorem still misstates the relation between the slice computations and the global `r_max=4` witness.
exec
/bin/zsh -lc 'rg -n "betagamma-(rank-one-rigidity|quartic-birth|global-depth|T-line-shadows|weight-line-shadows|shadow|depth)" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1000,1188p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
703:\label{rem:betagamma-shadow-archetype-free}
717:Theorem~\ref{thm:betagamma-rank-one-rigidity});
718:see \S\ref{sec:betagamma-shadow-tower-free} for the full tower.
814:(Theorem~\ref{thm:betagamma-rank-one-rigidity}) applies verbatim once
1060:\label{sec:betagamma-shadow-tower-free}
1091: (Theorem~\textup{\ref{thm:betagamma-rank-one-rigidity}}).
1110:Theorem~\ref{thm:betagamma-rank-one-rigidity}.\qedhere
1117:\label{prop:betagamma-T-line-shadows}
1152:\label{prop:betagamma-weight-line-shadows}
1161:Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
1167:rigidity (Theorem~\ref{thm:betagamma-rank-one-rigidity}): all
1178:\label{thm:betagamma-global-depth}
1195:(Proposition~\ref{prop:betagamma-T-line-shadows}). Generically nonzero.
1200:(Theorem~\ref{thm:betagamma-quartic-birth}).
1209:Theorem~\ref{thm:betagamma-quartic-birth}).
1253:\label{prop:betagamma-shadow-metric}
1289:\label{comp:betagamma-shadow-weights}
5560:(Theorem~\ref{thm:betagamma-global-depth}):
5563:(Theorem~\ref{thm:betagamma-rank-one-rigidity}).
5568:\S\ref{sec:betagamma-shadow-tower-free}.
 succeeded in 51ms:
\begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank; \ClaimStatusProvedHere]\label{thm:betagamma-bar-dim}
For all $n \geq 1$, $\operatorname{rank}(\bar{B}^n_{\mathrm{geom}}(\beta\gamma)) = 2 \cdot 3^{n-1}$,
where the rank counts the number of independent generator-type sectors in the
geometric bar complex.
\end{theorem}

\begin{proof}
We prove by induction on~$n$.

\emph{Base cases.} The cases $n = 1, 2, 3$ are verified explicitly in the
complete bar complex computation (Theorem~\ref{thm:betagamma-bar-cohomology},
Chapter~\ref{chap:beta-gamma}):
$\operatorname{rank}(\bar{B}^1) = 2$ ($\beta$- and $\gamma$-sectors),
$\operatorname{rank}(\bar{B}^2) = 6$ ($2^2 = 4$ pure tensor types $+$ $2$
derivative types $V_{\partial\beta}, V_{\partial\gamma}$),
$\operatorname{rank}(\bar{B}^3) = 18$ ($2^3 = 8$ pure tensor $+$ $10$ derivative).

\emph{Type decomposition.} The geometric bar complex at bar degree~$n$
decomposes by \emph{type assignment}: at each position
$i \in \{1, \ldots, n\}$, assign a type $t_i$ from the alphabet
exec
/bin/zsh -lc "sed -n '1265,1345p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1188,1265p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The proof proceeds degree by degree on the full deformation complex.
The T-line computations cited below are one-dimensional slice
computations, not literal restrictions of the global higher shadows.

\emph{Degree~$2$.}
$S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
(Proposition~\ref{prop:betagamma-T-line-shadows}). Generically nonzero.

\emph{Degree~$3$.}
The cubic shadow $\mathfrak{C}_{\beta\gamma}$ vanishes on the
weight-changing line because the Maurer--Cartan equation is linear there
(Theorem~\ref{thm:betagamma-quartic-birth}).
On the T-line, $S_3 = 2 \neq 0$; the cubic is supported only on the
stress tensor direction.

\emph{Degree~$4$.}
The quartic contact shadow $Q^{\mathrm{contact}}_{\beta\gamma}$
is nontrivial on the charged stratum that mixes the T-line and
weight-changing directions
 succeeded in 52ms:
 = 8\kappa\, S_4
 = \frac{40}{5c + 22}
 = \frac{40}{60\lambda^2 - 60\lambda + 32}.
\end{equation}
The discriminant $\Delta \neq 0$ for all real~$\lambda$, confirming
that $Q_L$ is irreducible quadratic and the T-line slice is
class~M.
\end{proposition}

\begin{proof}
Substituting $\alpha = 2$ and $S_4 = 10/(c(5c+22))$ into the shadow
metric formula $Q_L(t) = (2\kappa + 3\alpha t)^2 + 2\Delta t^2$
(Theorem~\ref{thm:riccati-algebraicity}) gives
$(2\kappa + 6t)^2 + 2\Delta t^2$ with
$\Delta = 8\kappa \cdot 10/(c(5c+22)) = 80\kappa/(c(5c+22)) = 40/(5c+22)$
(using $\kappa = c/2$). The denominator $5c + 22 = 60\lambda^2 - 60\lambda + 32$
has discriminant $3600 - 4 \cdot 60 \cdot 32 = -4080 < 0$, so it has
no real roots.\qedhere
\end{proof}


thinking
**Investigating theorem contradictions**

I need to check for contradictions around line 1171 related to the T-line. There might be a need to clarify that the global depth isn't realized on the T-line, which is infinite, while the wc-line vanishes. I should determine if any contradictions persist. It also makes sense to inspect the theorem `thm:betagamma-quartic-birth` to see if it addresses quartic birth on a charged stratum. I’ll search the file around that theorem for further insights.
codex
The actual gap is not a logical contradiction inside the local propositions; it is a missing routing sentence. One slice is zero, the other is infinite, and the global `r_max=4` witness sits on the mixed charged stratum, but the theorem does not currently say that cleanly enough. I’m locating the quartic-birth theorem and then I’ll patch the minimum wording needed to make the witness locus explicit.
exec
/bin/zsh -lc "sed -n '640,860p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:betagamma-quartic-birth\\}|quartic birth|charged stratum|mixed charged\" chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Shadow metric $Q(t)$ & $1/4$ \textup{(constant)} \\
Critical discriminant $\Delta$ & $0$ \\
$r$-matrix $r(z)$ & $0$ \textup{(regular)} \\
Koszul dual $\mathcal{F}^!$ & $\mathrm{Sym}^{\mathrm{ch}}(\gamma)$,
 $h_\gamma = 1/2$ \\
$\kappa(\mathcal{F}^!)$ & $-1/4$ \\
Complementarity sum & $0$ \\
Genus tower & $F_g = (1/4)\,\lambda_g^{\mathrm{FP}}$ \\
$F_1$ & $1/96$ \\
Genus partition function & $\mathrm{Pf}(\bar\partial_{K^{1/2}_\sigma})$ \\
Spin structures & $2^{2g}$ choices per genus \\
\bottomrule
\end{tabular}
\end{center}
All entries are projections of the single MC element
$\Theta_{\mathcal{F}} = (1/4) \cdot \eta \otimes \Lambda
\in \MC(\gAmod[\mathcal{F}])$
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)}.
\end{proposition}

 succeeded in 51ms:
80:contact shadow nontrivial on the charged stratum), even though
713:level is the quartic contact term on the charged stratum:
757:The quartic contact shadow lives on the charged stratum mixing the
1161:Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
1206:is nontrivial on the charged stratum that mixes the T-line and
1220:The quartic contact class lives on the charged stratum, while the cubic
1225:The quartic contact class lives on a charged stratum whose
1240:T-direction, the quartic contact lives on the charged stratum, and
5561:the quartic contact class lives on a charged stratum whose
exec
/bin/zsh -lc "sed -n '5528,5578p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
\toprule
\emph{Theorem} & \emph{Projection of $\Theta_{\beta\gamma}$}
 & \emph{Content} \\
\midrule
A (bar-cobar) &
 $\Theta_{\beta\gamma}\big|_{\hbar=0} = \tau$ &
 $(\beta\gamma)^! = bc$ (Thm~\ref{thm:betagamma-bc-koszul}) \\
B (inversion) &
 $\Omega(\barBgeom(\beta\gamma)) \simeq \beta\gamma$ &
 Genus-$0$ qi; rank $2 \cdot 3^{n-1}$ (Thm~\ref{thm:betagamma-bar-dim}) \\
C (complementarity) &
 $\kappa(\beta\gamma) + \kappa(bc) = 0$ &
 $Q_g + Q_g^! = H^*(\overline{\mathcal{M}}_g, Z(\beta\gamma))$ \\
D (modular char.) &
 $\Theta_{\beta\gamma}\big|_{g=1,n=0}
 = \kappa \cdot \lambda_1$ &
 $\kappa = 6\lambda^2{-}6\lambda{+}1$;\; $= 1$ at $\lambda=0,1$;\; $= -\tfrac{1}{2}$ at $\lambda=\tfrac{1}{2}$ \\



thinking
**Editing specific files**

I think I only need to edit a specific file, but I should consider consulting the theorem on `thm:betagamma-quartic-birth` to see if it’s in the same file or maybe another one. I’ll search for mentions of the label in different files. Reading the local reference around line 80 or 713 might help, especially since the remark at line 703 clarifies that the first nontrivial global shadow is a quartic contact term. However, the theorem on global depth could be confusing due to its mention of the T-line S5 being nonzero, which might also need fixing.
thinking
**Determining technical choices**

I need to decide on the strongest technical choice to enhance the theorem statement. It would be beneficial to identify the witness locus clearly and add a remark or proof to clarify that no 1D line realizes class C. I also think the proposition title could better say "weight-changing line; vanishing only on the pure weight-changing slice," but I want to keep edits minimal. I should check around line 1171, which might be part of the proof. It seems there’s no contradiction with the T-line, but the summary at line 5560 might be confusing. Since the user wants specific findings, focusing on one local section should suffice.
thinking
**Ensuring coherence in edits**

I need to search for phrases like "all one-dimensional shadows vanish" or "quartic contact" in the file to ensure that the summary around line 5560 remains consistent. Since my focus is only on editing the assigned file, I can adjust the summary if necessary. The user asked for specific findings near lines 1148-1166 and about the contradiction of the global-depth theorem with the T-line. I'll check the coherence of all modified sections, potentially editing the remark at line 703 or the computation summary at line 5550. After making edits, it’s crucial to reread the surrounding context to confirm everything fits well.
Plan update
Locked the contradiction surface in the beta-gamma shadow section. The current text distinguishes the vanishing weight-changing slice from the infinite T-line, but the global depth theorem needs an explicit witness-locus clarification so the class C claim cannot be misread as living on either one-dimensional slice.
  ✓ Diagnose the beta-gamma shadow section and identify the exact locus realizing global depth 4
  → Patch the local propositions/theorem in chapters/examples/free_fields.tex with the minimum truthful clarification
  • Re-read the modified section and verify finding resolution, status coherence, and local refs

thinking
**Analyzing mathematical consistency**

I’m examining whether global depth rmax = 4 is acceptable since the last nontrivial is quartic. There's a remark that suggests the first nontrivial beyond scalar should be quartic, which contradicts the inclusion of cubic. The user's focus is on the vanishing proposition and depth-gap theorem, highlighting inconsistencies. It seems to pertain to the weight-changing line. I need to clarify if cubic global vanishes or exists based on surrounding files or theorems; searching for cubic/quartic birth theorem could help illuminate this.
codex
I found a second local pressure point in the same lane: an earlier remark says the first nontrivial global shadow beyond the scalar level is quartic, while the later proof says a cubic survives on the T-direction. I’m checking that before editing so the patch doesn’t harden one contradiction while leaving another in place.
exec
/bin/zsh -lc 'rg -n "first nontrivial global shadow|cubic shadow|supported only on the stress tensor direction|quartic contact term" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '690,730p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
212:a simple pole kills the cubic shadow. The free fermion achieves class~G
238: \textup{(}Consequence of $S_3 = 0$: no quartic contact term survives in the
264:The cubic shadow $S_3$ is the degree-$3$ projection of
712:shadows vanish. The first nontrivial global shadow beyond the scalar
713:level is the quartic contact term on the charged stratum:
1103:of~$c$, with $S_3 = 2$ (the universal Virasoro cubic shadow) and
1198:The cubic shadow $\mathfrak{C}_{\beta\gamma}$ vanishes on the
1239:of the deformation complex. The cubic shadow is supported on the
1261:where $\kappa = 6\lambda^2 - 6\lambda + 1$, the cubic shadow
5661:$e^\alpha$ for $\alpha \in \Lambda$ contribute cubic shadow
 succeeded in 52ms:
 charge $c_{\mathrm{Vir}}$ yields the $N = 1$ superconformal algebra
 at $c = c_{\mathrm{Vir}} + 1/2$. The fermion sector contributes
 $\kappa_{\mathrm{ferm}} = 1/4$ to the total $\kappa$, and the
 shadow class of the combined system is determined by the Virasoro
 factor \textup{(}class~M, $r_{\max} = \infty$\textup{)}: the
 fermionic contribution does not increase shadow depth.
\end{enumerate}
\end{remark}

\subsection{\texorpdfstring{The $\beta\gamma$ system}{The beta-gamma system}}
\index{beta-gamma system|textbf}

\begin{remark}[Shadow archetype: contact/quartic]
\label{rem:betagamma-shadow-archetype-free}
\index{beta-gamma system@$\beta\gamma$ system!shadow archetype}
Shadow depth $r_{\max} = 4$ (class~C).
Modular characteristic $\kappa(\beta\gamma) = c/2 = 6\lambda^2 - 6\lambda + 1$,
where $\lambda$ is the conformal weight of $\gamma$.
Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$



thinking
**Addressing inconsistencies**

I’m thinking about the task and how to approach it carefully. Since I need to make sure my edits are honest and don’t create new inconsistencies, I might need to patch up some remarks to align with earlier findings.

It may be wise to adjust the remark at line 703, as the user didn’t restrict edits there. The goal is to make a minimal change, perhaps clarifying that "all one-dimensional shadows vanish" to better match the overall theorem.
thinking
**Clarifying computations**

I need to check if the computation summary already mentions the one-dimensional weight-changing line vanishing while noting that the full two-channel has a nonzero quartic contact invariant. It doesn't mention the infinite T-line, but I wonder if I should address that to prevent contradictions with the global theorem. 

It might be wise to patch the summary since it states that "on the one-dimensional weight-changing line all shadows vanish" without mentioning the T-line. The user asked me to check line 1171, so I’ll keep that in mind!
thinking
**Searching for theorem definitions**

I’m considering whether line 5560 in the summary requires a change. I should probably search for the theorem `thm:betagamma-rank-one-rigidity` and the local definitions for `thm:betagamma-quartic-birth`. It might be useful to look around line 760 to see if the full proof of quartic birth is there. This could help clarify if any adjustments are necessary in the summary!
exec
/bin/zsh -lc "sed -n '760,840p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:betagamma-rank-one-rigidity\\}|label\\{thm:betagamma-quartic-birth\\}|rank-one rigidity|quartic birth\" chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
716:stratum separation (rank-one rigidity,
1226:self-bracket exits the complex by rank-one rigidity; no further
5562:self-bracket exits the complex by rank-one rigidity
 succeeded in 50ms:

This should not be confused with the single-generator free fermion
$\mathcal{F}$ (class~G, $r_{\max} = 2$), where fermionic
antisymmetry on a single generator kills all higher bar cohomology.
The $bc$ system has two generators, so the antisymmetry argument
does not apply.

Modular characteristic $\kappa(bc) = c_{bc}/2 = -(6\lambda^2 - 6\lambda + 1)$.
At the physical point $(h_b, h_c) = (2, -1)$ (i.e.\ $\lambda = 2$):
$c_{bc} = -26$, $\kappa(bc) = -13$.
Complementarity:
$\kappa(\beta\gamma) + \kappa(bc) = 0$ (exact cancellation,
free-field family).
Shadow depth is preserved by Koszul duality for this pair: both
$\beta\gamma$ and $bc$ are class~C with $r_{\max} = 4$.
\end{remark}

\begin{definition}[\texorpdfstring{$bc$}{bc} ghost system]
Generated by $b(z)$ of weight $h_b = 2$ and $c(z)$ of weight $h_c = -1$,
with OPE $b(z)c(w) = \frac{1}{z-w}$ and Clifford relation $R_{bc} = b \otimes c + c \otimes b$.

thinking
**Evaluating mathematical terms**

I think I need to clarify the distinctions between "the pure weight-changing line" that has no tower and "the T-line" which is class M with infinite slice depth. It seems I should mention the difference between global towers and slice towers. Also, I want to address that while the quintic shadow S_5=0 globally, the recomputed T-line tower shows S_5 ≠0. I might change "separately recomputed" to emphasize that it's not about restriction.
codex
```text
scope: chapters/examples/free_fields.tex
surface: rem:betagamma-shadow-archetype-free; prop:betagamma-weight-line-shadows; thm:betagamma-global-depth
one-dimensional slices:
- T-line: Virasoro slice, infinite recomputed slice tower
- pure weight-changing line: vanishing tower
global witness:
- mixed charged stratum coupling the two directions; quartic contact class realizes r_max = 4
status check:
- proposition/theorem remain \ClaimStatusProvedHere; no downgrade justified
edit rule:
- strengthen by making the witness locus explicit and separating slice towers from the global tower
verdict: ACCEPT
```
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -710,5 +710,7 @@
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
@@ -1153,3 +1155,3 @@
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
@@ -1159,5 +1161,6 @@
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
@@ -1183,4 +1186,10 @@
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+has $S_r \neq 0$ for all $r \geq 2$.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
@@ -1191,2 +1200,4 @@
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
@@ -1213,4 +1224,6 @@
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
apply_patch(auto_approved=true) exited 0 in 24ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..17e05dc40f94427655034ea6717274a1ce365360
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+has $S_r \neq 0$ for all $r \geq 2$.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..17e05dc40f94427655034ea6717274a1ce365360
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+has $S_r \neq 0$ for all $r \geq 2$.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket





thinking
**Reviewing modifications**

I need to reread the modified sections about changes and ensure everything is correctly line-wrapped. There might be an awkward phrasing around "the recomputed one-dimensional tower is the Virasoro tower and has infinite depth." I should verify that my earlier remarks are consistent, especially noting the change that "all one-dimensional shadows vanish." 

I'll check for any theorem status drift and make sure the labels are valid. It might be a good idea to run some tools for cross-referencing as I confirm consistency in the propositions related to T-lines.
thinking
**Clarifying theorems**

At λ=(3 ±√3)/6, both c and kappa equal zero. This leads to S2 = 0, and S4's formula diverges, which seems problematic since the proposition states S_r ≠ 0 for all r ≥ 2. This creates confusion, especially because the theorem claims that the T-line slice has S_r ≠ 0 globally, yet at c = 0, S2 = 0. I should be careful with phrasing and perhaps say the T-line slice is class M, ensuring to specify S_5 ≠ 0 and avoid stating all r.
thinking
**Adjusting claims**

I need to adjust my statements to avoid overclaiming. The line about "T-line infinite depth" is fine, but the theorem may need a tweak. It might be clearer if I say the separately recomputed one-dimensional T-line tower is class M and specifically has S_5 ≠ 0. This way, I'm patching any ambiguity and accurately representing its properties without making overly broad claims. I'll make these adjustments to ensure precision in the language.
thinking
**Exploring mathematical properties**

I need to check the earlier proposition that suggests the T-line is infinite for all real λ, but that's not my focus right now. I should probably search for “all one-dimensional shadows vanish” to see if I can find relevant information, but I’m not getting any hits. That’s okay, though. I might need to read through the section and pay attention to specific line numbers while I do.
codex
The first pass is in. I changed only the beta-gamma shadow lane, and I’m re-reading it now for two things: that the witness locus is explicit in the theorem itself, and that I haven’t accidentally overclaimed the T-line beyond what the local proof actually uses.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '1148,1235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '700,725p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   700	\index{beta-gamma system|textbf}
   701	
   702	\begin{remark}[Shadow archetype: contact/quartic]
   703	\label{rem:betagamma-shadow-archetype-free}
   704	\index{beta-gamma system@$\beta\gamma$ system!shadow archetype}
   705	Shadow depth $r_{\max} = 4$ (class~C).
   706	Modular characteristic $\kappa(\beta\gamma) = c/2 = 6\lambda^2 - 6\lambda + 1$,
   707	where $\lambda$ is the conformal weight of $\gamma$.
   708	Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
   709	The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
   710	is nonzero at generic $\lambda$, but on the weight-changing line
   711	$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
   712	weight-changing slice tower vanishes. On the T-line, by contrast, the
   713	recomputed one-dimensional tower is the Virasoro tower and has infinite
   714	depth. The class~C witness on the full deformation space is the quartic
   715	contact term on the mixed charged stratum:
   716	$Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
   717	Tower terminates at exactly $r = 4$ by
   718	stratum separation (rank-one rigidity,
   719	Theorem~\ref{thm:betagamma-rank-one-rigidity});
 succeeded in 52ms:
  1148	discriminant $-4080 < 0$), so the T-line tower does not terminate
  1149	(Theorem~\ref{thm:single-line-dichotomy}).\qedhere
  1150	\end{proof}
  1151	
  1152	\begin{proposition}[$\beta\gamma$ shadow obstruction tower: weight-changing line;
  1153	\ClaimStatusProvedHere]
  1154	\label{prop:betagamma-weight-line-shadows}
  1155	\index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
  1156	On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
  1157	\[
  1158	 S_r\big|_{\mathrm{wc}} = 0
  1159	 \qquad (r \geq 2).
  1160	\]
  1161	This statement concerns only the one-dimensional slice generated by the
  1162	weight-changing class. It does not describe either the Virasoro T-line
  1163	of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
  1164	stratum that realizes the global depth-$4$ witness in
  1165	Theorem~\ref{thm:betagamma-global-depth}.
  1166	\end{proposition}
  1167	
exec
/bin/zsh -lc 'rg -n "all one-dimensional shadows vanish|S_r != 0|S_r '"\\\\neq 0|mixed charged stratum|class~C by itself\" chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: the literal "\n" is not allowed in a regex

Consider enabling multiline mode with the --multiline flag (or -U for short).
When multiline mode is enabled, new line characters can be matched.
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..17e05dc40f94427655034ea6717274a1ce365360
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+has $S_r \neq 0$ for all $r \geq 2$.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket

codex
I found one sentence that was stronger than needed: I had echoed the T-line proposition as `S_r \neq 0` for every `r`, which is more than this repair needs. I’m tightening that back to the exact point the finding requires: the T-line is the infinite slice, but the class-C witness is mixed and global.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -1191,3 +1191,3 @@
 $r \geq 2$, while the separately recomputed one-dimensional T-line tower
-has $S_r \neq 0$ for all $r \geq 2$.
+is class~M.
 The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
apply_patch(auto_approved=true) exited 0 in 26ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..4f6ed9e8e99e110e0779f5f22ded573da7a28cfc
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+is class~M.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..4f6ed9e8e99e110e0779f5f22ded573da7a28cfc
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+is class~M.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket

exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '1152,1238p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '705,724p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   705	Shadow depth $r_{\max} = 4$ (class~C).
   706	Modular characteristic $\kappa(\beta\gamma) = c/2 = 6\lambda^2 - 6\lambda + 1$,
   707	where $\lambda$ is the conformal weight of $\gamma$.
   708	Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
   709	The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
   710	is nonzero at generic $\lambda$, but on the weight-changing line
   711	$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
   712	weight-changing slice tower vanishes. On the T-line, by contrast, the
   713	recomputed one-dimensional tower is the Virasoro tower and has infinite
   714	depth. The class~C witness on the full deformation space is the quartic
   715	contact term on the mixed charged stratum:
   716	$Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
   717	Tower terminates at exactly $r = 4$ by
   718	stratum separation (rank-one rigidity,
   719	Theorem~\ref{thm:betagamma-rank-one-rigidity});
   720	see \S\ref{sec:betagamma-shadow-tower-free} for the full tower.
   721	Koszul dual: $(\beta\gamma)^! = bc$
   722	(Theorem~\ref{thm:betagamma-bc-koszul}).
   723	See Chapter~\ref{chap:beta-gamma} for the full quartic
   724	birth analysis.
 succeeded in 51ms:
  1152	\begin{proposition}[$\beta\gamma$ shadow obstruction tower: weight-changing line;
  1153	\ClaimStatusProvedHere]
  1154	\label{prop:betagamma-weight-line-shadows}
  1155	\index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
  1156	On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
  1157	\[
  1158	 S_r\big|_{\mathrm{wc}} = 0
  1159	 \qquad (r \geq 2).
  1160	\]
  1161	This statement concerns only the one-dimensional slice generated by the
  1162	weight-changing class. It does not describe either the Virasoro T-line
  1163	of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
  1164	stratum that realizes the global depth-$4$ witness in
  1165	Theorem~\ref{thm:betagamma-global-depth}.
  1166	\end{proposition}
  1167	
  1168	\begin{proof}
  1169	The weight-changing line satisfies the hypothesis of rank-one abelian
  1170	rigidity (Theorem~\ref{thm:betagamma-rank-one-rigidity}): all
  1171	transferred higher brackets $\ell_n^{\mathrm{tr}}|_L = 0$ for
exec
/bin/zsh -lc "rg -n '\\\\label\\{(prop:betagamma-T-line-shadows|prop:betagamma-weight-line-shadows|thm:betagamma-global-depth|thm:betagamma-rank-one-rigidity|thm:betagamma-bc-koszul|thm:betagamma-quartic-birth|cor:nms-betagamma-mu-vanishing|chap:beta-gamma)\\}' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'all one-dimensional shadows vanish|first nontrivial global shadow beyond the scalar|class~C by itself|T-line slice has \\\\"'$S_5 '"\\\\neq 0\\\\"'$'"' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1189:one-dimensional slice realizes class~C by itself.
 succeeded in 51ms:
./appendices/nonlinear_modular_shadows.tex:1167:\label{cor:nms-betagamma-mu-vanishing}
./audit_campaign_20260412_231034/F15_S2.md:713:\label{prop:betagamma-T-line-shadows}
./audit_campaign_20260412_231034/T16_depth_gap.md:820:/bin/zsh -lc "rg -n -F '\\label{cor:nms-betagamma-mu-vanishing}' appendices/nonlinear_modular_shadows.tex chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./audit_campaign_20260412_231034/T16_depth_gap.md:863:appendices/nonlinear_modular_shadows.tex:1167:\label{cor:nms-betagamma-mu-vanishing}
./audit_campaign_20260412_231034/T16_depth_gap.md:1228:  2096	\label{thm:betagamma-quartic-birth}
./audit_campaign_20260412_231034/T16_depth_gap.md:1261:/bin/zsh -lc "rg -n -F '\\label{thm:betagamma-rank-one-rigidity}' chapters/examples/beta_gamma.tex chapters/examples/free_fields.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./audit_campaign_20260412_231034/T16_depth_gap.md:1306:chapters/examples/beta_gamma.tex:2560:\label{thm:betagamma-rank-one-rigidity}
./audit_campaign_20260412_231034/T16_depth_gap.md:1307:chapters/examples/beta_gamma.tex:2560:\label{thm:betagamma-rank-one-rigidity}
./audit_campaign_20260412_231034/T16_depth_gap.md:1310:  2560	\label{thm:betagamma-rank-one-rigidity}
./fix_wave_A_20260413_112727/A07_free_fields.md:130:\label{prop:betagamma-T-line-shadows}
./fix_wave_A_20260413_112727/A07_free_fields.md:283:\label{thm:betagamma-quartic-birth}
./fix_wave_A_20260413_112727/A07_free_fields.md:329:\label{thm:betagamma-rank-one-rigidity}
./fix_wave_A_20260413_112727/A07_free_fields.md:444: \label{thm:betagamma-global-depth}
./fix_wave_A_20260413_112727/A07_free_fields.md:511: \label{thm:betagamma-global-depth}
./fix_wave_A_20260413_112727/A07_free_fields.md:570:\label{prop:betagamma-weight-line-shadows}
./fix_wave_A_20260413_112727/A07_free_fields.md:605: \label{thm:betagamma-global-depth}
./fix_wave_A_20260413_112727/A07_free_fields.md:699: \label{thm:betagamma-global-depth}
./fix_wave_A_20260413_112727/A07_free_fields.md:773: \label{thm:betagamma-global-depth}
./fix_wave_A_20260413_112727/A07_free_fields.md:859: \label{thm:betagamma-global-depth}
./fix_wave_A_20260413_112727/A07_free_fields.md:924:/bin/zsh -lc "rg -n -F -e '\\label{prop:betagamma-T-line-shadows}' -e '\\label{prop:betagamma-weight-line-shadows}' -e '\\label{thm:betagamma-global-depth}' -e '\\ref{prop:betagamma-T-line-shadows}' -e '\\ref{prop:betagamma-weight-line-shadows}' -e '\\ref{thm:betagamma-global-depth}' -e '\\ref{thm:betagamma-rank-one-rigidity}' -e '\\ref{thm:betagamma-quartic-birth}' -e '\\ref{cor:nms-betagamma-mu-vanishing}' chapters/examples/free_fields.tex chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..4f6ed9e8e99e110e0779f5f22ded573da7a28cfc
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+is class~M.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket


thinking
**Updating plan for progress review**

I need to update step 3 as it’s in progress and I’ll mark it completed when done. Before finalizing, I should run `git diff -- chapters/examples/free_fields.tex` to check for any unintended changes. It’s a good idea to review the exact modifications made. So, running that command will help me ensure everything looks as it should before moving forward. Let’s do that now!
codex
The modified surface now reads consistently: the vanishing proposition is explicitly only the pure weight-changing slice, and the theorem now states that the class-C witness is mixed rather than one-dimensional. I’m doing one last diff read to make sure the patch stayed minimal and didn’t spill into unrelated claims.
exec
/bin/zsh -lc 'git diff -- chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\ref{prop:betagamma-T-line-shadows}' chapters/examples/free_fields.tex && rg -n -F '\\ref{thm:betagamma-global-depth}' chapters/examples/free_fields.tex && rg -n -F '\\ref{thm:betagamma-rank-one-rigidity}' chapters/examples/free_fields.tex && rg -n -F '\\ref{thm:betagamma-quartic-birth}' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6..4f6ed9e 100644
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@ where $\lambda$ is the conformal weight of $\gamma$.
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@ discriminant $-4080 < 0$), so the T-line tower does not terminate
 succeeded in 51ms:
1163:of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
1206:(Proposition~\ref{prop:betagamma-T-line-shadows}). Generically nonzero.
1165:Theorem~\ref{thm:betagamma-global-depth}.
5573:(Theorem~\ref{thm:betagamma-global-depth}):
719:Theorem~\ref{thm:betagamma-rank-one-rigidity});
816:(Theorem~\ref{thm:betagamma-rank-one-rigidity}) applies verbatim once
1093: (Theorem~\textup{\ref{thm:betagamma-rank-one-rigidity}}).
1112:Theorem~\ref{thm:betagamma-rank-one-rigidity}.\qedhere
1170:rigidity (Theorem~\ref{thm:betagamma-rank-one-rigidity}): all
5576:(Theorem~\ref{thm:betagamma-rank-one-rigidity}).
1211:(Theorem~\ref{thm:betagamma-quartic-birth}).
1220:Theorem~\ref{thm:betagamma-quartic-birth}).
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..4f6ed9e8e99e110e0779f5f22ded573da7a28cfc
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+is class~M.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket



thinking
**Evaluating summary consistency**

I'm considering if a summary around line 5573 could work. I think I should check the content around line 5568 to see if it aligns with the theorem reference. It’s all about making sure everything is consistent, right? I wonder if the details connect well and if I should adjust anything to enhance clarity. Let’s inspect it closely and see what improvements might be needed!
thinking
**Considering inspection benefits**

I’m thinking there might not be a need, but it could be beneficial to inspect it. Especially since I have a reference to the global depth theorem. It feels like looking deeper could clarify things. I wonder if there are specific aspects worth investigating further. So, I should weigh the potential advantages of this inspection against whether it might genuinely help with the understanding. Overall, it seems like it's worth taking a closer look!
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5566,5579p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5566	\end{center}
  5567	Shadow obstruction tower: on the one-dimensional weight-changing line all
  5568	shadows vanish, but on the full two-channel deformation space one has
  5569	$\Theta^{\leq 4} \neq 0$ because the quartic contact invariant
  5570	$Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$
  5571	\textup{(}Chapter~\ref{chap:beta-gamma}\textup{)}. The quintic
  5572	obstruction still satisfies $o_5 = 0$ by stratum separation
  5573	(Theorem~\ref{thm:betagamma-global-depth}):
  5574	the quartic contact class lives on a charged stratum whose
  5575	self-bracket exits the complex by rank-one rigidity
  5576	(Theorem~\ref{thm:betagamma-rank-one-rigidity}).
  5577	Tower terminates at exactly $r = 4$.
  5578	The full shadow obstruction tower data (multi-channel structure,
  5579	special weight table, shadow metric, weight symmetry,
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..4f6ed9e8e99e110e0779f5f22ded573da7a28cfc
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+is class~M.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket

Plan update
Patched the beta-gamma shadow lane so the slice/global distinction is explicit in the proposition, theorem, and overview remark. Re-read the modified surface, checked the relevant labels/refs, and confirmed the theorem status remains ProvedHere.
  ✓ Diagnose the beta-gamma shadow section and identify the exact locus realizing global depth 4
  ✓ Patch the local propositions/theorem in chapters/examples/free_fields.tex with the minimum truthful clarification
  ✓ Re-read the modified section and verify finding resolution, status coherence, and local refs
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..4f6ed9e8e99e110e0779f5f22ded573da7a28cfc
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+is class~M.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket

codex
Edited [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:705), [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1152), and [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1180) to make the slice/global distinction explicit. The weight-changing line now clearly means the pure one-dimensional slice, and the global `r_{\max}=4` witness is stated to live on the mixed charged stratum rather than on either one-dimensional line. I re-read the modified section and checked the referenced labels by grep; I did not run a full TeX build.

## Rectification Summary
- [FIXED] T16 vanishing-line contradiction — the weight-changing-line proposition now says `pure weight-changing line` and explicitly excludes both the Virasoro T-line and the mixed charged stratum from its scope.
- [FIXED] T16 depth-gap witness ambiguity — the global-depth theorem now states that `r_{\max}=4` is realized by the quartic contact class on the mixed charged stratum; it also says the pure weight-changing slice vanishes while the T-line is class `M`.
- [FIXED] T16 theorem/proof coherence — the proof now states that the class~C witness is mixed, and the quartic class is identified as the last nontrivial global shadow component rather than something visible on an isolated line.
- [FIXED] Local overview consistency — the earlier beta-gamma archetype remark was aligned with the theorem: weight-changing slice vanishes, T-line remains infinite, mixed charged stratum realizes the class~C witness.
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 5741cb6f3fb10f16b122079d6840fd5ddcdd8e9b..4f6ed9e8e99e110e0779f5f22ded573da7a28cfc
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -708,9 +708,11 @@
 Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.
 The scalar shadow $\Theta^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 is nonzero at generic $\lambda$, but on the weight-changing line
-$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and all one-dimensional
-shadows vanish. The first nontrivial global shadow beyond the scalar
-level is the quartic contact term on the charged stratum:
+$\Theta^{\leq 2}\big|_{\mathrm{w.c.}} = 0$ and the entire
+weight-changing slice tower vanishes. On the T-line, by contrast, the
+recomputed one-dimensional tower is the Virasoro tower and has infinite
+depth. The class~C witness on the full deformation space is the quartic
+contact term on the mixed charged stratum:
 $Q^{\mathrm{contact}}_{\beta\gamma} \neq 0$.
 Tower terminates at exactly $r = 4$ by
 stratum separation (rank-one rigidity,
@@ -1151,15 +1153,16 @@
 \ClaimStatusProvedHere]
 \label{prop:betagamma-weight-line-shadows}
 \index{beta-gamma system@$\beta\gamma$ system!weight-changing line}
-On the weight-changing line, the shadow obstruction tower vanishes at all degrees:
+On the pure weight-changing line, the shadow obstruction tower vanishes at all degrees:
 \[
  S_r\big|_{\mathrm{wc}} = 0
  \qquad (r \geq 2).
 \]
 This statement concerns only the one-dimensional slice generated by the
-weight-changing class; the quartic contact shadow in
-Theorem~\ref{thm:betagamma-global-depth} lives on the mixed charged
-stratum and is not detected on this line.
+weight-changing class. It does not describe either the Virasoro T-line
+of Proposition~\ref{prop:betagamma-T-line-shadows} or the mixed charged
+stratum that realizes the global depth-$4$ witness in
+Theorem~\ref{thm:betagamma-global-depth}.
 \end{proposition}
 
 \begin{proof}
@@ -1181,14 +1184,22 @@
 On the full two-channel deformation space, the $\beta\gamma$ system has
 global shadow depth $r_{\max} = 4$
 \textup{(}class~C, the contact/quartic archetype\textup{)}.
-The quintic shadow $S_5 = 0$ globally, even though the separately
-computed one-dimensional T-line tower has $S_5 \neq 0$.
+The depth-$4$ witness is the quartic contact class on the mixed charged
+stratum coupling the T-line to the weight-changing direction; neither
+one-dimensional slice realizes class~C by itself.
+The pure weight-changing line has $S_r|_{\mathrm{wc}} = 0$ for all
+$r \geq 2$, while the separately recomputed one-dimensional T-line tower
+is class~M.
+The quintic shadow $S_5 = 0$ globally, even though the T-line slice has
+$S_5 \neq 0$.
 \end{theorem}
 
 \begin{proof}
 The proof proceeds degree by degree on the full deformation complex.
 The T-line computations cited below are one-dimensional slice
 computations, not literal restrictions of the global higher shadows.
+Thus the class~C witness must be mixed: it is not the vanishing pure
+weight-changing slice, and it is not the infinite T-line slice.
 
 \emph{Degree~$2$.}
 $S_2 = \kappa = 6\lambda^2 - 6\lambda + 1$
@@ -1211,8 +1222,10 @@
 $\mu_{\beta\gamma} := \langle \eta, m_3(\eta,\eta,\eta)\rangle = 0$
 vanishes by rank-one abelian rigidity
 (Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
-The quartic contact class is the \emph{last} nontrivial shadow
-component.
+Hence the nonzero quartic class is genuinely mixed: it is invisible on
+both isolated one-dimensional slices and appears only on the charged
+stratum. The quartic contact class is the \emph{last} nontrivial global
+shadow component.
 
 \emph{Degree~$5$.}
 The quintic obstruction is the Lie bracket

tokens used
169,241
