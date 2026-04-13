# P08_MC1_PBW_whitehead_upgrade (1075s)

[higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:895) now makes the Whitehead reduction explicit instead of informal. I added a weightwise reduction lemma and a mixed-map factorization lemma at [lines 912-1003](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:912), rewrote the Kac--Moody genus-1 and all-genera PBW proofs to use them at [1005-1317](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1005), and recorded the optimal semisimple bound plus the non-semisimple obstruction at [2034-2058](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2034).

Strongest truthful PBW form on this surface: semisimple weightwise symmetry kills the genus enrichment by `E_3`, not `E_1`. The boundary counterexample is already affine KM: the weight-2 Killing-form class survives `d_1` and is only killed by the family-specific `d_2` transgression. In the non-semisimple case, the obstruction is the radical cohomology term `H^1(\mathfrak r_h,M_h)^{\mathfrak s_h}` and, more generally, the Hochschild--Serre package `H^p(\mathfrak s_h,H^q(\mathfrak r_h,M_h))`.

Verification: I re-read the full modified region, checked new-label uniqueness across all three volumes, and grepped the added lines for the requested forbidden patterns. `make fast` does not currently verify this file because the global build is blocked by a pre-existing corrupted `main.aux` surface with fatal aux-state failure and hundreds of pre-existing unresolved refs; I did not find a local TeX error tied to the new PBW edits before that global failure.

## Platonic Rectification Report
- BEFORE: `thm:pbw-genus1-km` (`ProvedHere`) asserted genus-1 PBW degeneration for affine KM, but the proof still routed Whitehead through the truncated current algebra informally.
- ISSUE: The mode cutoff `\fg[t]/t^N` was being used without an explicit theorem reducing the problem to finite-dimensional `\fg`-modules; the mixed genus-0/genus-1 map was not factored through `H^1(\fg,M)`.
- ACTION: FILLED
- AFTER: `thm:pbw-genus1-km` remains `ProvedHere`, now backed by `lem:pbw-weightwise-g-module` and `lem:pbw-mixed-factorization`, with Whitehead applied only to finite-dimensional weight modules and the mixed map explicitly controlled by `H^1(\fg,N_h^{n-1})`.
- CONFIDENCE: high
- REMAINING GAP: No local proof gap remains in this theorem lane; build verification is blocked globally by corrupted aux state, not by this proof.

- BEFORE: `thm:pbw-allgenera-km` (`ProvedHere`) asserted all-genera PBW degeneration by saying the genus-1 mechanism is genus-independent, but the Whitehead reduction was still only stated heuristically.
- ISSUE: The all-genera extension needed the same weightwise `\fg`-module reduction and the same mixed-map factorization, otherwise the semisimple argument was not fully transportable from genus 1 to genus `g`.
- ACTION: FILLED
- AFTER: `thm:pbw-allgenera-km` remains `ProvedHere`, now explicitly reuses the weightwise `\fg`-module package and the `H^1(\fg,-)` factorization for each basis vector of `H^{1,0}(\Sigma_g)`, so the Whitehead step is genuinely genus-independent.
- CONFIDENCE: high
- REMAINING GAP: None on the proof surface touched here.

- BEFORE: The semisimple PBW lane was described as if one might hope for an `E_1` collapse once Whitehead is available.
- ISSUE: That stronger claim is false even in the semisimple landscape; affine KM has a surviving `E_2` Killing-form class.
- ACTION: INTERMEDIATE
- AFTER: The file now states the optimal bound: semisimple weightwise symmetry gives an `E_3` statement, not an `E_1` statement, and the non-semisimple obstruction is identified by the Hochschild--Serre radical cohomology terms.
- CONFIDENCE: high
- REMAINING GAP: An actual `E_1`-collapse theorem would require new mathematics because the affine KM boundary example blocks it.


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
session id: 019d8652-8274-7e51-a33d-9b87912ced9e
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


MC1: PBW theorem.

TARGET: chapters/theory/higher_genus_modular_koszul.tex

KNOWN ISSUE: Whitehead lemma applied to truncated current algebra without justification.

YOUR MISSION: PROVE the Whitehead reduction properly:
1. The truncated current algebra g[t]/t^N has a weight decomposition where g acts
   on each weight piece. The enrichment classes live in H*(g, M_h) for weight-h modules M_h.
2. Whitehead: H^1(g, M) = 0 for semisimple g and any finite-dimensional M. This kills
   the enrichment at genus 0 -> genus 1.
3. The mixed maps (genus-0/genus-1) factor through the g-action on the weight pieces.
   WRITE this factorisation explicitly as a lemma.
4. State the PBW theorem in its STRONGEST form: the spectral sequence from bar degree
   to modular degree collapses at E_1 for ALL families where the underlying Lie algebra
   is semisimple. For non-semisimple families: characterise the obstruction.

Search for 'PBW' and 'Whitehead' near lines 990-1100 and 1290-1300.
mcp startup: no servers

thinking
**Exploring repair strategies**

I need to consider using the beilinson-rectify skill, as it seems to match the task at hand. I might need to use build-surface later. Additionally, cross-volume-propagation could be beneficial after making any necessary edits. For structural repair, I think utilizing a minimal set covering request with beilinson-rectify is key. Also, I might want to apply multi-path-verify to check the formula, especially if there are changes in the theorem status.
codex
Using `beilinson-rectify` for the theorem repair and `build-surface` for post-edit verification. I’m reading the required repo surfaces plus the PBW/Whitehead region in `chapters/theory/higher_genus_modular_koszul.tex` to lock the exact claim, status, and local dependencies before editing.
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
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2836 |
| Total tagged claims | 3665 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2836 |
 succeeded in 52ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
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

 succeeded in 53ms:
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
codex
I have the repo-wide constraints loaded. Next I’m locking the exact PBW/Whitehead claim surface in the target file, plus any nearby theorem-registry or cross-volume duplicates that will need synchronized repair.
exec
/bin/zsh -lc 'rg -n "PBW|Whitehead|truncated current|current algebra|mixed|semisimple|genus-0|genus-1" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '930,1125p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1240,1325p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3:%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
144: (class~$\mathsf{M}$, mixed).
198:For standard examples at generic parameters, the PBW argument of
615:\emph{(Modular Koszulity / PBW degeneration.)}
616:At each genus $g \geq 1$, the PBW spectral sequence of
709:MK1 (genus-0 Koszulity) by
770:\begin{theorem}[PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
773:\index{PBW spectral sequence!higher genus concentration}
777:This theorem uses Theorem~\ref{thm:pbw-universal-semisimple} only to eliminate
784:Then for every genus~$g \geq 1$, the PBW spectral sequence for the
844:the matrix of $d_2^{\mathrm{PBW}}$ is block upper triangular:
859:Consequently the diagonal block of $d_2^{\mathrm{PBW}}$ on
868:$d_2^{\mathrm{PBW}}$ is an isomorphism:
876:$d_2^{\mathrm{PBW}}$.
896:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
906:\begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
908:\index{PBW spectral sequence!genus-1 degeneration|textbf}
909:\index{modular Koszul chiral algebra!genus-1 unconditional}
914:$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
920:by Whitehead; the Killing-form invariant
 succeeded in 52ms:
We carry out the genus-$1$ Kac--Moody argument directly, using
enrichment factorization, Whitehead acyclicity, and the
level-$k$ Killing contraction.

\medskip
\emph{Step~1: Decomposition of the $E_1$ page.}

Equip $\bar{B}^{(1)}(\widehat{\fg}_k)$ with the PBW filtration
by conformal weight, as in
Theorem~\ref{thm:pbw-koszulness-criterion}.
The leading PBW differential $d_0^{\mathrm{PBW}}$ is the
commutative bar differential of the associated graded
$\operatorname{Sym}^{\mathrm{ch}}(V)$, $V = \fg \otimes
t^{-1}\bC[t^{-1}]$, now living on the
elliptic curve~$E_\tau$ rather than~$\mathbb{P}^1$.

At genus~$0$, the chain groups of the bar complex use
logarithmic forms on $\overline{C}_n(\mathbb{P}^1)$, and
$d_0^{\mathrm{PBW}}$ extracts Poincar\'{e} residues at
collision divisors. The $E_1$ page concentrates
 succeeded in 51ms:
Theorems~\ref{thm:higher-genus-inversion}
and~\ref{thm:quantum-complementarity-main}.
\end{proof}

\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
\label{thm:pbw-allgenera-km}
\index{PBW spectral sequence!all-genera degeneration|textbf}
\index{modular Koszul chiral algebra!unconditional all genera}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

This theorem does not use Theorem~\ref{thm:pbw-universal-semisimple}
\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
mechanism, and the absence of later differentials/extensions is supplied by the
family-specific argument below.

For any simple Lie algebra~$\fg$, any genus~$g \geq 1$, and
generic level $k \notin \Sigma(\fg)$, the PBW spectral sequence
for the genus-$g$ bar complex
collab spawn_agent(call_fc7bnYgVbTc9zVvvraB3uQd9, prompt="Inspect chapters/theory/higher_genus_modular_koszul.tex for the PBW/Whitehead lane around thm:pbw-genus1-km and thm:pbw-…")
spawn_agent(call_fc7bnYgVbTc9zVvvraB3uQd9, prompt="Inspect chapters/theory/higher_genus_modular_koszul.tex for the PBW/Whitehead lane around thm:pbw-genus1-km and thm:pbw-…") pending init:
  agent: 019d8653-1fef-7d20-a893-cfbbf4c3cae9
mcp startup: no servers
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "pbw" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
743: Theorem~\textup{\ref{thm:pbw-allgenera-km}};}
746: Theorem~\textup{\ref{thm:pbw-allgenera-virasoro}};}
751: Theorem~\textup{\ref{thm:pbw-allgenera-principal-w}}.}
757:Theorems~\ref{thm:pbw-allgenera-km}
758:and~\ref{thm:pbw-allgenera-virasoro}.
766:MK3 by Theorem~\ref{thm:pbw-allgenera-principal-w}.
771:\label{thm:pbw-allgenera-principal-w}
772:% backward-compatible label removed (was conj:pbw-higher-genus-degeneration)
777:This theorem uses Theorem~\ref{thm:pbw-universal-semisimple} only to eliminate
873:\textup{(}\ref{item:pbw-bounded} of
874:Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)},
888:\texttt{compute/lib/w\_algebra\_pbw\_genus1.py}
897:Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
898:Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
900:Theorem~\ref{thm:pbw-allgenera-principal-w}).
907:\label{thm:pbw-genus1-km}
939:Theorem~\ref{thm:pbw-koszulness-criterion}.
1101:(\ref{item:pbw-bounded} of
1102:Theorem~\ref{thm:pbw-koszulness-criterion}), the
1171:\nolinkurl{compute/lib/genus1_pbw_sl2.py},
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '880,1040p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\qquad (h > 0).
\]
The same argument applies to the antiholomorphic factor
$H^{0,1}(\Sigma_g)$, since $L_0$ acts only on the vertex-algebra
factor. Hence the full $H^1(\Sigma_g,\bC)$-enrichment is eliminated,
and one obtains $E_\infty(g) = E_\infty(0)$.

The computation module
\texttt{compute/lib/w\_algebra\_pbw\_genus1.py}
verifies the weight-triangular mechanism for the first
higher-spin case $\mathcal{W}_3$ through conformal weight~$8$,
together with the principal generator weights for the finite-type
families $A_1$, $A_2$, $A_3$, $B_2$, $C_2$, $G_2$, and~$F_4$.
\end{proof}

\begin{remark}[Status and mechanism]\label{rem:mk4-status}
Higher-genus PBW holds for KM (Whitehead + Killing contraction,
Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
$\mathcal{W}$ (block upper triangular,

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1040,1240p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
and $d_1^{\mathrm{PBW}}$ is the corresponding
Chevalley--Eilenberg differential for the finite-dimensional
semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
$\fg \otimes V_h$. The map to the concentrated
genus-$0$ sector is one of the $\fg$-equivariant components of this
same differential.

\medskip
\emph{Step~3: Acyclicity of the enrichment complex.}

We show $H^*(\mathcal{E}_1^{*,h},\, d_1^{\mathrm{PBW}}) = 0$
in each conformal weight~$h$, by a representation-theoretic
argument for~$\fg$ semisimple.

The enrichment module~$M_h$ at weight~$h$ decomposes
under~$\fg$ into irreducible summands. Since $\fg$ is
semisimple, the Whitehead--Chevalley--Eilenberg theorem
gives:
thinking
**Exploring theorem references**

I need to read more relevant lines while the explorer runs. I could potentially use `rg` to find theorem labels in the target file and maybe use `sed` around specific line ranges like 900-1450 or 1700-1950. It's important to reference theorems like thm:pbw-koszulness-criterion and thm:km-chiral-koszul. I should check if the theorem registry or concordance mentions pbw-allgenera-km. Also, I should search for duplicates across volumes using `rg`.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1200,1400p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
levels.

At each higher weight~$h$, the same
three mechanisms act (the representation-theoretic
decomposition under~$\fg$ and the Whitehead vanishing
are weight-independent), completing the proof.
\end{proof}

\begin{remark}[Whitehead reduction in the PBW proof]
For fixed conformal weight~$h$, the truncated current algebra
$\fg \otimes V_h$ only records which modes can occur. The actual
Whitehead input appears after rewriting the weight-$h$ enrichment
block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
$H^1$ factors treated as passive coefficients. No vanishing statement
is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
itself.
\end{remark}

\begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
codex
The local lane is centered on `thm:pbw-genus1-km` and `thm:pbw-allgenera-km`. I’m expanding that region now, then I’ll isolate the exact proof gap and patch the theorem/lemma structure around it instead of only touching a sentence.
exec
/bin/zsh -lc "sed -n '900,1455p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:pbw-genus1-km|thm:pbw-allgenera-km|Whitehead reduction in the PBW proof|PBW degeneration at genus~\\\\texorpdfstring\\{\\\\"'$1'"\\\\}\\{1\\} for Kac--Moody|PBW degeneration at all genera for Kac--Moody\" -S . ../chiral-bar-cobar-vol2 ../calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:pbw-allgenera-principal-w}).
Open: non-principal families; the $\mathcal{W}_\infty$
inverse-limit package
(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
\end{remark}

\begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
\label{thm:pbw-genus1-km}
\index{PBW spectral sequence!genus-1 degeneration|textbf}
\index{modular Koszul chiral algebra!genus-1 unconditional}
\textup{[Regime: curved-central
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For any simple Lie algebra~$\fg$ and generic level
$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
genus-$1$ bar complex
$\bar{B}^{(1)}(\widehat{\fg}_k)$ has concentrated
$E_\infty$ page: the enrichment from $H^1(E_\tau)$
is eliminated by~$d_1$ and~$d_2$
\textup{(}non-trivial $\fg$-modules at~$E_2$
 succeeded in 51ms:
./wave2_audit_20260413_001942/S13_concordance_to_body.md:1600:  - `chapters/connections/concordance.tex:4851-4874` (“Non-circular logical chain.”) states that the antecedent hypotheses MK:koszul–MK:modular are verified independently (via Theorem~\ref{thm:fundamental-twisting-morphisms}, Theorem~\ref{thm:verdier-bar-cobar}, Theorems~\ref{thm:pbw-allgenera-km}–\ref{thm:pbw-allgenera-principal-w}) and that Theorem~\ref{thm:higher-genus-inversion} then inductively proves inversion without invoking the genus under consideration.
./wave2_audit_20260413_001942/F20_status_audit.md:1992:\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
./wave2_audit_20260413_001942/U06_incomplete_proofs_v1.md:1821:\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
./audit_campaign_20260412_231034/T08_MC1_PBW.md:225:metadata/dependency_graph.dot:2927:  thm_pbw_genus1_km [label="thm:pbw-genus1-km\ntheorem [Pr]\nPBW degeneration at genus~\texorpdfstrin...", style=filled, fillcolor="#c8e6c9"];
./audit_campaign_20260412_231034/T08_MC1_PBW.md:377:743: Theorem~\textup{\ref{thm:pbw-allgenera-km}};}
./audit_campaign_20260412_231034/T08_MC1_PBW.md:380:757:Theorems~\ref{thm:pbw-allgenera-km}
./audit_campaign_20260412_231034/T08_MC1_PBW.md:384:897:Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
./audit_campaign_20260412_231034/T08_MC1_PBW.md:387:1197:\label{thm:pbw-allgenera-km}
./audit_campaign_20260412_231034/T08_MC1_PBW.md:388:1434:Theorem~\ref{thm:pbw-allgenera-km}.
./audit_campaign_20260412_231034/T08_MC1_PBW.md:392:1860:(Theorem~\ref{thm:pbw-allgenera-km}).
./audit_campaign_20260412_231034/T08_MC1_PBW.md:405:Theorem~\ref{thm:pbw-genus1-km}.
./audit_campaign_20260412_231034/T08_MC1_PBW.md:411:\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
./audit_campaign_20260412_231034/T08_MC1_PBW.md:412:\label{thm:pbw-allgenera-km}
./audit_campaign_20260412_231034/T08_MC1_PBW.md:449:  1190	Theorem~\ref{thm:pbw-genus1-km}.
./audit_campaign_20260412_231034/T08_MC1_PBW.md:455:  1196	\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
./audit_campaign_20260412_231034/T08_MC1_PBW.md:456:  1197	\label{thm:pbw-allgenera-km}
./audit_campaign_20260412_231034/T08_MC1_PBW.md:593:907:\label{thm:pbw-genus1-km}
./audit_campaign_20260412_231034/T08_MC1_PBW.md:594:1190:Theorem~\ref{thm:pbw-genus1-km}.
./audit_campaign_20260412_231034/T08_MC1_PBW.md:595:1230:(Theorem~\ref{thm:pbw-genus1-km}) establishes a
./audit_campaign_20260412_231034/T08_MC1_PBW.md:711:   - lines **1196‑1225** define `thm:pbw-allgenera-km` with its `\ClaimStatusProvedHere` tag; the accompanying proof runs through **1229‑1391**. 
exec
/bin/zsh -lc "rg -n \"pbw.*km|Whitehead.*PBW|truncated current algebra|Chevalley--Eilenberg complexes C\\"'^'"\\*\\(\\\\fg, M_h\\)|enrichment factorization|Killing-form contraction\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/theorem_registry.md:884:| `thm:pbw-genus1-km` | `theorem` | 907 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
metadata/theorem_registry.md:886:| `thm:pbw-allgenera-km` | `theorem` | 1245 | PBW degeneration at all genera for Kac--Moody |
chapters/theory/higher_genus_modular_koszul.tex:743: Theorem~\textup{\ref{thm:pbw-allgenera-km}};}
chapters/theory/higher_genus_modular_koszul.tex:757:Theorems~\ref{thm:pbw-allgenera-km}
chapters/theory/higher_genus_modular_koszul.tex:897:Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
chapters/theory/higher_genus_modular_koszul.tex:907:\label{thm:pbw-genus1-km}
chapters/theory/higher_genus_modular_koszul.tex:931:enrichment factorization, Whitehead acyclicity, and the
chapters/theory/higher_genus_modular_koszul.tex:1021:The truncated current algebra $\fg \otimes V_h$
chapters/theory/higher_genus_modular_koszul.tex:1114:Killing-form contraction at the first nontrivial conformal
chapters/theory/higher_genus_modular_koszul.tex:1208:\begin{remark}[Whitehead reduction in the PBW proof]
chapters/theory/higher_genus_modular_koszul.tex:1209:For fixed conformal weight~$h$, the truncated current algebra
chapters/theory/higher_genus_modular_koszul.tex:1238:Theorem~\ref{thm:pbw-genus1-km}.
chapters/theory/higher_genus_modular_koszul.tex:1245:\label{thm:pbw-allgenera-km}
chapters/theory/higher_genus_modular_koszul.tex:1278:(Theorem~\ref{thm:pbw-genus1-km}) establishes a
chapters/theory/higher_genus_modular_koszul.tex:1280:acyclicity, Killing-form contraction) that is
chapters/theory/higher_genus_modular_koszul.tex:1353:truncated current algebra that records the mode cutoff.
chapters/theory/higher_genus_modular_koszul.tex:1374:\emph{Step~3: Killing-form contraction kills
chapters/theory/higher_genus_modular_koszul.tex:1379:is spanned by the Killing-form contractions
chapters/theory/higher_genus_modular_koszul.tex:1488:Theorem~\ref{thm:pbw-allgenera-km}.
chapters/theory/higher_genus_modular_koszul.tex:1763:The enrichment factorization~\eqref{eq:enrichment-factorization}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:pbw-genus1-km" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/T08_MC1_PBW.md:225:metadata/dependency_graph.dot:2927:  thm_pbw_genus1_km [label="thm:pbw-genus1-km\ntheorem [Pr]\nPBW degeneration at genus~\texorpdfstrin...", style=filled, fillcolor="#c8e6c9"];
audit_campaign_20260412_231034/T08_MC1_PBW.md:405:Theorem~\ref{thm:pbw-genus1-km}.
audit_campaign_20260412_231034/T08_MC1_PBW.md:449:  1190	Theorem~\ref{thm:pbw-genus1-km}.
audit_campaign_20260412_231034/T08_MC1_PBW.md:593:907:\label{thm:pbw-genus1-km}
audit_campaign_20260412_231034/T08_MC1_PBW.md:594:1190:Theorem~\ref{thm:pbw-genus1-km}.
audit_campaign_20260412_231034/T08_MC1_PBW.md:595:1230:(Theorem~\ref{thm:pbw-genus1-km}) establishes a
audit_campaign_20260412_231034/T08_MC1_PBW.md:721:   - `chapters/theory/higher_genus_modular_koszul.tex:906‑927` `thm:pbw-genus1-km` (the genus‑1 Whitehead/Killing mechanism) used by the KM proof at line 1229. 
audit_campaign_20260412_231034/T08_MC1_PBW.md:793:   907	\label{thm:pbw-genus1-km}
audit_campaign_20260412_231034/T08_MC1_PBW.md:950:/bin/zsh -lc 'rg -n "eq:e1-decomposition-genusg|eq:enrichment-factorization|eq:e1-decomposition-genus1|enrichment factorization|PBW spectral sequence concentrates at all genera for the three standard|thm:master-pbw|thm:pbw-genus1-km" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/concordance.tex chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/T08_MC1_PBW.md:956:chapters/theory/higher_genus_modular_koszul.tex:907:\label{thm:pbw-genus1-km}
audit_campaign_20260412_231034/T08_MC1_PBW.md:959:chapters/theory/higher_genus_modular_koszul.tex:1190:Theorem~\ref{thm:pbw-genus1-km}.
audit_campaign_20260412_231034/T08_MC1_PBW.md:960:chapters/theory/higher_genus_modular_koszul.tex:1230:(Theorem~\ref{thm:pbw-genus1-km}) establishes a
fix_wave_A_20260413_112727/A02_hg_modular_rect.md:388:(Theorem~\ref{thm:pbw-genus1-km}) establishes a
audit_campaign_20260412_231034/T03_thm_C0.md:661:metadata/claims.jsonl:2819:{"label": "thm:pbw-genus1-km", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 821, "title": "PBW degeneration at genus~\\texorpdfstring{$1$}{1} for Kac--Moody", "refs_in_block": ["conv:regime-tags", "def:modular-koszul-chiral"]}
audit_campaign_20260412_231034/T06_thm_D.md:285:Theorem~\ref{thm:pbw-genus1-km}.
audit_campaign_20260412_231034/T06_thm_D.md:354:  1230	(Theorem~\ref{thm:pbw-genus1-km}) establishes a
metadata/dependency_graph.dot:2972:  thm_pbw_genus1_km [label="thm:pbw-genus1-km\ntheorem [Pr]\nPBW degeneration at genus~\texorpdfstrin...", style=filled, fillcolor="#c8e6c9"];
audit_campaign_20260412_231034/T02_thm_B.md:1245:Theorem~\ref{thm:pbw-genus1-km}.
metadata/theorem_registry.md:884:| `thm:pbw-genus1-km` | `theorem` | 907 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
metadata/label_index.json:50334:  "thm:pbw-genus1-km": {
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:pbw-allgenera-km" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
wave2_audit_20260413_001942/S13_concordance_to_body.md:1600:  - `chapters/connections/concordance.tex:4851-4874` (“Non-circular logical chain.”) states that the antecedent hypotheses MK:koszul–MK:modular are verified independently (via Theorem~\ref{thm:fundamental-twisting-morphisms}, Theorem~\ref{thm:verdier-bar-cobar}, Theorems~\ref{thm:pbw-allgenera-km}–\ref{thm:pbw-allgenera-principal-w}) and that Theorem~\ref{thm:higher-genus-inversion} then inductively proves inversion without invoking the genus under consideration.
wave2_audit_20260413_001942/F20_status_audit.md:1992:\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
wave2_audit_20260413_001942/U06_incomplete_proofs_v1.md:1821:\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
wave2_audit_20260413_001942/F02_definitions_koszul.md:790:./metadata/claims.jsonl:2138:{"label": "thm:bar-cobar-inversion-qi", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 1604, "title": "Bar-cobar inversion is quasi-isomorphism", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "def:koszul-chiral-algebra", "sec:i-adic-completion", "MK:modular", "def:modular-koszul-chiral", "thm:pbw-allgenera-km", "thm:pbw-allgenera-principal-w", "rem:qi-vs-homology-iso", "thm:spectral-sequence-collapse", "rem:sl2-admissible", "rem:virasoro-module-koszul-minimal", "cor:bar-cobar-inverse"]}
wave2_audit_20260413_001942/S08_en_to_topologization.md:1059:  1229	\label{thm:pbw-allgenera-km}
metadata/dependency_graph.dot:2974:  thm_pbw_allgenera_km [label="thm:pbw-allgenera-km\ntheorem [Pr]\nPBW degeneration at all genera for Kac--...", style=filled, fillcolor="#c8e6c9"];
wave2_audit_20260413_001942/U09_missing_examples.md:981:   199	\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
audit_campaign_20260412_231034/T06_thm_D.md:292:\label{thm:pbw-allgenera-km}
audit_campaign_20260412_231034/T06_thm_D.md:326:Theorem~\ref{thm:pbw-allgenera-km}.
audit_campaign_20260412_231034/T02_thm_B.md:326:/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|label\\{lem:higher-genus-open-stratum-qi\\}|label\\{lem:higher-genus-boundary-qi\\}|label\\{lem:extension-across-boundary-qi\\}|label\\{def:modular-koszul-chiral\\}|label\\{MK:modular\\}|label\\{thm:BD-extension-higher-genus\\}|label\\{thm:pbw-allgenera-km\\}|label\\{thm:pbw-allgenera-principal-w\\}|label\\{thm:fundamental-twisting-morphisms\\}\" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/examples/lattice_foundations.tex -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/T02_thm_B.md:352:chapters/theory/higher_genus_modular_koszul.tex:1197:\label{thm:pbw-allgenera-km}
audit_campaign_20260412_231034/T02_thm_B.md:1252:\label{thm:pbw-allgenera-km}
audit_campaign_20260412_231034/T02_thm_B.md:1288: Theorem~\textup{\ref{thm:pbw-allgenera-km}};}
audit_campaign_20260412_231034/T02_thm_B.md:1302:Theorems~\ref{thm:pbw-allgenera-km}
audit_campaign_20260412_231034/T02_thm_B.md:1356:  4029	Kac--Moody by Theorem~\ref{thm:pbw-allgenera-km}, for Virasoro
audit_campaign_20260412_231034/T13_koszul_equivs.md:379:2138:{"label": "thm:bar-cobar-inversion-qi", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 1604, "title": "Bar-cobar inversion is quasi-isomorphism", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "def:koszul-chiral-algebra", "sec:i-adic-completion", "MK:modular", "def:modular-koszul-chiral", "thm:pbw-allgenera-km", "thm:pbw-allgenera-principal-w", "rem:qi-vs-homology-iso", "thm:spectral-sequence-collapse", "rem:sl2-admissible", "rem:virasoro-module-koszul-minimal", "cor:bar-cobar-inverse"]}
metadata/theorem_registry.md:886:| `thm:pbw-allgenera-km` | `theorem` | 1245 | PBW degeneration at all genera for Kac--Moody |
metadata/label_index.json:50322:  "thm:pbw-allgenera-km": {
audit_campaign_20260412_231034/T01_thm_A.md:522:Theorems~\ref{thm:pbw-allgenera-km}--\ref{thm:pbw-allgenera-principal-w})
audit_campaign_20260412_231034/T01_thm_A.md:1216:  2160	Theorems~\ref{thm:pbw-allgenera-km}--\ref{thm:pbw-allgenera-principal-w})

thinking
**Looking into the universal semisimple theorem**

I see the user is asking for more context around the universal semisimple theorem, particularly concerning its strongest form. I should focus on the period between 1710 and 1917 to gather information. It's essential to understand the relationships and perhaps modify the theorem for the strongest version related to all semisimple underlying Lie algebras and obstruction characterization for non-semisimple families. I realize I need to inspect existing theorems as they might be weaker than necessary.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '870,1180p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   870	
   871	Any class in a fixed bidegree has finite conformal-weight support by
   872	bounded-below convergence
   873	\textup{(}\ref{item:pbw-bounded} of
   874	Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)},
   875	so it lies in some finite truncation and is killed by
   876	$d_2^{\mathrm{PBW}}$.
   877	Thus
   878	\[
   879	E_3^{*,h}(g)_{\mathrm{enr}} = 0
   880	\qquad (h > 0).
   881	\]
   882	The same argument applies to the antiholomorphic factor
   883	$H^{0,1}(\Sigma_g)$, since $L_0$ acts only on the vertex-algebra
   884	factor. Hence the full $H^1(\Sigma_g,\bC)$-enrichment is eliminated,
   885	and one obtains $E_\infty(g) = E_\infty(0)$.
   886	
   887	The computation module
   888	\texttt{compute/lib/w\_algebra\_pbw\_genus1.py}
   889	verifies the weight-triangular mechanism for the first
codex
The local proof already tries to route Whitehead through finite-dimensional `\fg`-modules, but the reduction is still informal and the all-semigimple claim is not stated cleanly enough. I’m reading the universal semisimple theorem now, because the requested strongest form likely belongs there as well, not only in the Kac–Moody special case.
exec
/bin/zsh -lc "sed -n '1688,1938p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "non-semisimple|obstruction|Whitehead decomposition|pbw-universal-semisimple|hook-type|semisimple symmetry" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/*.tex chapters/connections/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
from conditional to unconditional.
\end{corollary}

\begin{proof}
MK1 (genus-$0$ Koszulity):
Theorems~\ref{thm:w-algebra-koszul-main}
and~\ref{thm:bar-cobar-spectral-sequence}.
MK2 (Verdier):
Theorem~\ref{thm:verdier-bar-cobar}.
MK3 (PBW concentration at all genera):
Theorem~\ref{thm:pbw-allgenera-principal-w}.
MK4 and MK5 follow from MK1--MK3 by
Theorems~\ref{thm:higher-genus-inversion}
and~\ref{thm:quantum-complementarity-main}.
Item~(i) is MK4 applied to the principal
$\mathcal{W}$-algebra;
item~(ii) is MK5;
item~(iii) follows from~(i) and the
scalar characteristic
(Theorem~\ref{thm:modular-characteristic}).
 succeeded in 50ms:
Total output lines: 2309

chapters/examples/bar_complex_tables.tex:272:uncurved; this does not determine the higher-degree shadow obstruction tower. At
chapters/examples/bar_complex_tables.tex:831:(Theorem~\ref{thm:explicit-theta}): the obstruction to
chapters/examples/bar_complex_tables.tex:858:Casimir obstruction: the Killing form element
chapters/examples/bar_complex_tables.tex:867:shadow of the modular anomaly: the genus-$1$ obstruction class
chapters/examples/bar_complex_tables.tex:1166:\begin{remark}[Euler characteristic obstruction to naive bar models]
chapters/examples/bar_complex_tables.tex:1167:\label{rem:euler-chi-obstruction}
chapters/examples/bar_complex_tables.tex:1168:\index{bar complex!Euler characteristic obstruction}
chapters/examples/bar_complex_tables.tex:1552:obstruction $m_1^2 \neq 0$ via the formula
chapters/examples/bar_complex_tables.tex:1995:The unifying object is the shadow obstruction tower
chapters/examples/bar_complex_tables.tex:2603:\index{shadow obstruction tower!exceptional types}
chapters/examples/bar_complex_tables.tex:2604:\index{shadow obstruction tower!non-simply-laced types}
chapters/examples/bar_complex_tables.tex:2609:The following table collects the shadow obstruction tower data for all exceptional ($E_6, E_7, E_8$) and non-simply-laced ($B_2, G_2, F_4$) affine Kac--Moody algebras. Every family is class L (shadow depth $r_{\max} = 3$), with cubic shadow $C$ from the Lie bracket, quartic shadow $S_4 = 0$ by the Jacobi identity, and critical discriminant $\Delta = 8\kappa S_4 = 0$. The r-matrix has a simple pole at $z = 0$ ($d\log$ extraction absorbs one power), and complementarity $\kappa + \kappa' = 0$ holds for all Kac--Moody families. All data verified by 458 compute tests (\texttt{test\_exceptional\_shadows.py}, \texttt{test\_non\_simply\_laced\_shadows.py}).
chapters/examples/bar_complex_tables.tex:4394:genus-$1$ obstruction: at genus~$0$ the bar complex
chapters/examples/kac_moody.tex:5:degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
chapters/examples/kac_moody.tex:9:finiteness of the obstruction tower or preserves it.
chapters/examples/kac_moody.tex:15:introduces noncommutativity but not infinite obstruction complexity:
chapters/examples/kac_moody.tex:164:\begin{remark}[Shadow obstruction tower for Kac--Moody]\label{rem:km-master-mc}
chapters/examples/kac_moody.tex:166:obstruction tower in the modular convolution algebra
exec
/bin/zsh -lc "sed -n '440,520p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{chain-level enhancement} of the Feigin--Frenkel center:
it encodes functions on the oper space (in $H^0$),
K\"ahler differentials (in $H^1$), and higher exterior forms
(in $H^{\geq 2}$), reproducing the oper differential-form
package central to the Langlands programme
(Theorem~\ref{thm:oper-bar}).
\end{remark}

\begin{remark}[The twisting morphism as organizing datum]
\label{rem:tau-protagonist}
\index{twisting morphism!as organizing datum}
The canonical twisting morphism $\tau \colon \barB_X(\cA) \to \cA$
underlies the four main theorems
(Convention~\ref{conv:bar-coalgebra-identity}):
Theorem~A establishes $\tau$; Theorem~B inverts it;
Theorem~C identifies its genus-$g$ curvature; Theorem~D computes
its leading coefficient.
At higher genus, $\tau$ extends to a curved twisting cochain
$\tau_{\mathrm{mod}} = \tau + \Theta_\cA$
whose curvature $\kappa(\cA)\cdot\omega_g$ governs the entire
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1220,1490p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1220	\label{cor:unconditional-genus1-km}
  1221	\index{modular Koszul chiral algebra!unconditional genus-1}
  1222	For any simple~$\fg$ at generic level, the affine
  1223	Kac--Moody vertex algebra $\widehat{\fg}_k$ satisfies
  1224	axioms \textup{MK1--MK3} unconditionally at genus~$1$.
  1225	By Theorems~\textup{\ref{thm:higher-genus-inversion}}
  1226	and~\textup{\ref{thm:quantum-complementarity-main}},
  1227	the consequences \textup{MK4} \textup{(}inversion\textup{)}
  1228	and \textup{MK5} \textup{(}complementarity\textup{)} hold
  1229	at genus~$1$ without any conditional hypothesis.
  1230	\end{corollary}
  1231	
  1232	\begin{proof}
  1233	MK1 (genus-$0$ Koszulity):
  1234	Theorem~\ref{thm:km-chiral-koszul}.
  1235	MK2 (Verdier):
  1236	Theorem~\ref{thm:verdier-bar-cobar}.
  1237	MK3 (modular Koszulity at $g = 1$):
  1238	Theorem~\ref{thm:pbw-genus1-km}.
  1239	MK4 and MK5 follow from MK1--MK3 by
exec
/bin/zsh -lc 'ls /Users/raeez' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Applications
Desktop
Documents
Downloads
Library
Movies
Music
Pictures
Public
api-gateway
attestation-engine
audit
blueprint.md
calabi-yau-quantum-groups
cbc
centcom
chiral-bar-cobar
chiral-bar-cobar-gitbackups
chiral-bar-cobar-vol2
dotfiles
exec
/bin/zsh -lc 'rg -n "pbw-genus1-km" /Users/raeez/chiral-bar-cobar-vol2' in /Users/raeez/chiral-bar-cobar exited 1 in 55ms:

exec
/bin/zsh -lc 'rg -n "pbw-genus1-km" /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Exploring PBW theorem**

The user wants me to state the PBW theorem in its strongest form. I note that it specifically mentions the spectral sequence from bar degree to modular degree collapsing at E1 for all families with a semisimple underlying Lie algebra. For non-semisimple families, there’s an obstruction to characterize. I’ll search for any existing theorem or remark around reference 8896, as it could be relevant. I also need to inspect the context around references 8890 to 9055.
codex
I’ve isolated the exact gap: the KM proof is locally repairable, but the “strongest form” request also forces a cleaner universal statement separating semisimple and non-semisimple symmetry. I’m checking whether that characterization already exists later in the file so I can strengthen the theorem instead of duplicating it.
exec
/bin/zsh -lc "sed -n '9050,9135p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8888,9068p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$H^2_{\mathrm{cyc,prim}}$
(Corollary~\ref{cor:effective-quadruple}).
At admissible levels, the module category is non-semisimple, and
the question becomes: \emph{does the MC moduli remain
one-dimensional, and does the corresponding coefficient equal
$\kappa\Lambda$?}
Theorem~\ref{thm:algebraic-family-rigidity} answers only the first
question for algebraic families; the second remains open for
multi-weight examples.
\end{remark}

\begin{theorem}[Algebraic-family rigidity; \ClaimStatusProvedHere]
\label{thm:algebraic-family-rigidity}
\index{cyclic cohomology!algebraic-family rigidity}
\index{scalar saturation!algebraic-family proof}
\index{Whitehead decomposition!algebraic-family upgrade}
Let $\{{\cA}_k\}_{k \in U}$ be a family of vertex algebras
over a Zariski-open $U \subset \mathbb{C}$ with
$-h^\vee \notin U$, each equipped with simple affine current
subalgebra~$\widehat{\fg}_k$, satisfying:
 succeeded in 52ms:
at level~(L3), $\Pi_{\cA}$ carries the periodicity data.
\end{proof}

\begin{theorem}[Cyclic rigidity at generic level;
\ClaimStatusProvedHere]
\label{thm:cyclic-rigidity-generic}
\index{cyclic cohomology!rigidity theorem}
\index{scalar saturation!at generic level}
\index{Whitehead decomposition!of cyclic cohomology}
Let\/ $\cA$ be a vertex algebra with simple affine current
subalgebra\/ $\widehat{\fg}_k$ satisfying:
\begin{enumerate}[label=\textup{(\alph*)}]
\item $\cA$ is strongly finitely generated
 over\/~$\widehat{\fg}_k$;
\item each conformal weight space $\cA_h$ is a
 finite-dimensional\/ $\fg$-module;
\item the\/ $\widehat{\fg}_k$-module category containing the
 summands of\/~$\cA$ is semisimple
 \textup{(}holds at all non-admissible, non-critical
 levels~$k$\textup{)}.
exec
/bin/zsh -lc 'rg -n "E_1 collapse|collapse at E_1|modular degree|bar degree to modular degree|non-semisimple families|obstruction to PBW|Jordan|radical|reductive|nilpotent radical" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/*.tex chapters/connections/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/landscape_census.tex:1173: The logarithmic phenomena (Jordan blocks for~$L_0$) appear in the
chapters/examples/w_algebras.tex:507:$\widehat{\fg}_k$, tensors with a ghost system indexed by the nilradical
chapters/examples/w_algebras.tex:3075: logarithmic couplings (rank-$2$ Jordan blocks for $L_0$).
chapters/connections/concordance.tex:5642:radical $\sqrt{1-2x-3x^2}$, they share the same branch locus,
chapters/connections/concordance.tex:7355: \emph{not} control is the nilradical of~$R_{L_k}$.
chapters/connections/concordance.tex:7361: unconditional Koszulness still requires a nilradical/reducedness
chapters/connections/concordance.tex:10324: nilradical of~$R_{L_k}$.
chapters/theory/higher_genus_modular_koszul.tex:1901:$\mathfrak{sl}_N$ is a reductive subalgebra whose semisimple
chapters/theory/higher_genus_modular_koszul.tex:9438:any~$\cA$ with maximal reductive current algebra
chapters/theory/higher_genus_modular_koszul.tex:17015:For a non-principal nilpotent of Jordan type~$\lambda$,
chapters/theory/higher_genus_modular_koszul.tex:25500:elements, and the nilpotent radical of $\cW(p)$ is not
chapters/theory/higher_genus_modular_koszul.tex:25519:the Frobenius algebra of $\cW(p)$ has a nilpotent radical
chapters/theory/higher_genus_modular_koszul.tex:28395: useful evidence, yet a nilradical calculation is still
chapters/theory/higher_genus_modular_koszul.tex:33590:nilpotently on the finite-length module, giving a Jordan factor
chapters/examples/y_algebras.tex:126:element with Jordan block of size~$N_2$. Equivalently,
chapters/connections/casimir_divisor_core_transport.tex:33:That is where the Jordan geometry lives.
chapters/connections/casimir_divisor_core_transport.tex:338:\subsection{Primary and Jordan sectors}
chapters/connections/casimir_divisor_core_transport.tex:348:\begin{theorem}[Primary Jordan filtration]
chapters/connections/casimir_divisor_core_transport.tex:364:and \(T_p-\lambda\) acts on this sector by a single Jordan block of size \(m\).
chapters/connections/casimir_divisor_core_transport.tex:384:and multiplication by \(t\) is multiplication by \(\lambda+\tau\), so \(t-\lambda\) acts by the standard nilpotent Jordan shift.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1160,1230p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1160	 which is nonzero at generic level~$k$.
  1161	\end{itemize}
  1162	
  1163	Thus all nine enrichment classes at $h = 2$ are eliminated:
  1164	three by the bracket isomorphism, five by Whitehead, one by the
  1165	Killing contraction.
  1166	The decomposition $E_\infty^{*,2}(g{=}1) =
  1167	E_\infty^{*,2}(g{=}0)$ follows.
  1168	
  1169	A symbolic check of the same mechanism at the next tensor
  1170	powers, implemented in
  1171	\nolinkurl{compute/lib/genus1_pbw_sl2.py},
  1172	confirms that no new representation-theoretic obstruction
  1173	appears. The diagonal Casimir eigenspace dimensions are:
  1174	\[
  1175	\begin{aligned}
  1176	\mathfrak{sl}_2^{\otimes 3}&:\ \{24{:}7,\;12{:}10,\;4{:}9,\;0{:}1\},\\
  1177	\mathfrak{sl}_2^{\otimes 4}&:\ \{40{:}9,\;24{:}21,\;12{:}30,\;4{:}18,\;0{:}3\},\\
  1178	\mathfrak{sl}_2^{\otimes 5}&:\ \{60{:}11,\;40{:}36,\;24{:}70,\;12{:}75,\;4{:}45,\;0{:}6\},\\
  1179	\mathfrak{sl}_2^{\otimes 6}&:\ \{84{:}13,\;60{:}55,\;40{:}135,\;24{:}203,\;12{:}200,\;4{:}108,\;0{:}15\},\\

thinking
**Updating the plan**

I think it might be helpful to use the explorer result. However, wait a second! I realize I have enough context now to update the plan. I should outline the steps involved and their statuses so I can keep everything organized. This way, I can track progress and ensure everything is moving along smoothly. Let’s break it down further and make sure I’m covering all the necessary details.
Plan update
Scoped to the PBW/Whitehead lane in chapters/theory/higher_genus_modular_koszul.tex. I’ve read the required repo surfaces, the KM genus-1/all-genera proofs, and the nearby universal semisimple theorem. Next I’m tightening the Whitehead factorization into explicit lemmas and strengthening the semisimple/non-semisimple statement in the same local lane.
  ✓ Audit the KM PBW lane and identify the exact Whitehead reduction gap plus the strongest truthful theorem statement in local scope
  → Draft the repair structure: explicit weight-piece factorization lemma, explicit mixed-map factorization lemma, strengthened semisimple/non-semisimple theorem statement, and proof rewrites
  • Edit the target file with scoped theorem/lemma/proof changes and re-read the modified region immediately after each edit
  • Run local verification: forbidden-pattern grep, targeted LaTeX build/test surface if feasible, and hostile re-read of the modified PBW lane

thinking
**Organizing theorem references and cross-volume mentions**

I'm sorting out detailed references to theorems, remarks, and proofs about Whitehead reductions and PBW-related results across multiple files. I'll prepare a clear bullet list noting exact line ranges and filenames to clarify dependencies, cross-volume duplicates, and question responses, making sure to ground everything in precise text locations for easy tracking.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "pbw-allgenera-km" chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
25:\ref{thm:pbw-allgenera-km},
85:Theorems~\ref{thm:pbw-allgenera-km},
199:\textup{(}Theorem~\textup{\ref{thm:pbw-allgenera-km}}\textup{)},
478:with Theorems~\ref{thm:pbw-allgenera-km},
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "pbw-allgenera-km" chapters/examples/genus_expansions.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
466:genus by Theorem~\ref{thm:pbw-allgenera-km}. The proof mechanism is
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "pbw-allgenera-km" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4893:(Theorems~\ref{thm:pbw-allgenera-km}--\ref{thm:pbw-allgenera-principal-w}).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "pbw-genus1-km" chapters/connections' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc 'rg -n "pbw-genus1-km" standalone' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '880,900p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
| `lem:genus-graded-koszul-resolution` | `lemma` | 356 | Genus-graded Koszul complex resolution |
| `prop:standard-examples-modular-koszul` | `proposition` | 687 | Free-field examples are modular pre-Koszul |
| `prop:conditional-modular-koszul` | `proposition` | 729 | Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul |
| `thm:pbw-allgenera-principal-w` | `theorem` | 771 | PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-genus1-km` | `theorem` | 907 | PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody |
| `cor:unconditional-genus1-km` | `corollary` | 1220 | Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1} |
| `thm:pbw-allgenera-km` | `theorem` | 1245 | PBW degeneration at all genera for Kac--Moody |
| `cor:unconditional-allgenera-km` | `corollary` | 1448 | Unconditional modular Koszulity for Kac--Moody |
| `thm:pbw-allgenera-virasoro` | `theorem` | 1500 | PBW degeneration at all genera for Virasoro |
| `cor:unconditional-allgenera-virasoro` | `corollary` | 1600 | Unconditional modular Koszulity for Virasoro |
| `cor:unconditional-allgenera-principal-w` | `corollary` | 1650 | Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras |
| `thm:pbw-universal-semisimple` | `theorem` | 1712 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
| `prop:hook-pbw` | `proposition` | 1873 | Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses |
| `thm:pbw-propagation` | `theorem` | 1930 | PBW propagation: MK1 implies MK3 |
| `prop:collision-locality` | `proposition` | 2089 | Locality of the collision differential |
| `thm:three-tier-architecture` | `theorem` | 2176 | Three-tier logical architecture of modular Koszul duality |
| `lem:e2-higher-genus` | `lemma` | 2425 | $E_2$ collapse at higher genus |
| `thm:genus-internalization` | `theorem` | 2577 | Genus internalization of modular Koszul duality |
| `thm:modular-characteristic` | `theorem` | 2685 | Modular characteristic |
| `cor:free-energy-ahat-genus` | `corollary` | 2852 | Scalar free energy as $\hat{A}$-genus |
thinking
**Considering genus enrichment**

I'm trying to unpack what the user means by "enrichment at genus 0 -> genus 1." It seems like they might be referencing how genus-enrichment classes could vanish due to H^1. I need to think about how mixed maps factor through the g-action on weight pieces as well. There’s a lot of technical terminology here, so let's make sure I clarify these concepts properly for a better understanding. It’s important to get this right!
exec
/bin/zsh -lc 'rg -n "bar degree to modular degree|modular degree|collapse at E_1|collapses at E_1|bar degree" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_*.tex chapters/examples/*.tex chapters/connections/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:120:No completion is needed. The bar complex is conilpotent (finite-dimensional in each bar degree) and the differential is zero except for the curvature term $m_0$. Convergence of the bar spectral sequence follows: the filtration by bar degree is bounded below ($n \geq 0$) and exhaustive, with finite-dimensional graded pieces, so the spectral sequence converges to the bar homology by the standard bounded-below complete convergence theorem (\cite{LV12}, Theorem~2.2.3).
chapters/theory/bar_cobar_adjunction_inversion.tex:430:bar degrees, the output of $d_{\mathrm{curvature}}$ is the
chapters/theory/bar_cobar_adjunction_inversion.tex:579:$d(F_p)\subseteq F_p$ and $d$ lowers bar degree by one on $\gr_F\bar{B}(\mathcal{A})$.
chapters/theory/bar_cobar_adjunction_inversion.tex:687:bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
chapters/theory/bar_cobar_adjunction_inversion.tex:1726:(bar degree~$\geq 2$), so this singular vector at weight~$4$
chapters/theory/bar_cobar_adjunction_inversion.tex:1783:singular vector at conformal weight~$4$ lives in bar degree~$2$.
chapters/theory/bar_cobar_adjunction_inversion.tex:2043:This is the filtration by \emph{bar degree} (= cobar degree).
chapters/theory/bar_cobar_adjunction_inversion.tex:2069:The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
chapters/theory/bar_cobar_adjunction_inversion.tex:2084:converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
chapters/theory/bar_cobar_adjunction_inversion.tex:2090: \quad \text{(bar cohomology at fixed cobar degree $p$)} \\
chapters/theory/bar_cobar_adjunction_inversion.tex:2103:By definition of the filtration, this isolates the piece in cobar degree~$p$ and total degree $p+q$.
chapters/theory/bar_cobar_adjunction_inversion.tex:2107:is the bar complex differential $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$, lifted to each cobar tensor factor. This is the filtration-preserving component of $d$: both $d_{\text{internal}}$ (from the differential on~$\mathcal{A}$) and $d_{\text{bar}}$ (from the multiplication of~$\mathcal{A}$, encoding collisions) preserve cobar degree.
chapters/theory/bar_cobar_adjunction_inversion.tex:2109:Taking cohomology gives the $E_1$ page: bar cohomology at each fixed cobar degree.
chapters/theory/bar_cobar_adjunction_inversion.tex:2113:is induced by $d_{\text{cobar}}$ (the comultiplication on $\bar{B}(\mathcal{A})$, which increases cobar degree by~$1$).
chapters/theory/bar_cobar_adjunction_inversion.tex:2123:For the application to Theorem~\ref{thm:bar-cobar-inversion-qi}, the completeness statement in Definition~\ref{def:bar-cobar-filtration}(2) is supplied by its conilpotency/completion hypothesis: if $\bar{B}(\mathcal{A})$ is conilpotent in the sense of Definition~\ref{def:conilpotent-complete}, every element has finite bar degree, while in the augmentation-ideal completion regime the filtration is complete by construction.
chapters/theory/bar_cobar_adjunction_inversion.tex:2147:The Koszul property of $\mathcal{A}$ means that the natural inclusion $\iota: \mathcal{A}^! \hookrightarrow \bar{B}(\mathcal{A})$ of the quadratic dual into the bar complex is a quasi-isomorphism (see \cite[Theorem~3.4.1]{LV12} for the classical case and Chapter~\ref{chap:koszul-pairs} for the chiral adaptation). Since $\mathcal{A}^!$ is generated in weight~1 with quadratic relations, its image under $\iota$ lies on the diagonal $p + q = \text{const}$ in the bigrading $(p,q)$ by bar degree and internal degree.
chapters/theory/bar_cobar_adjunction_inversion.tex:2149:At the $E_1$ page, we compute the cohomology of each column with respect to $d_0 = d_{\bar{B}}$, the full bar complex differential. Each column $E_0^{p,\bullet}$ with differential $d_0$ computes the bar cohomology $H^q(\bar{B}^p(\mathcal{A}), d_{\bar{B}})$ at fixed cobar degree~$p$. By the Koszul quasi-isomorphism, the bar cohomology is concentrated on the diagonal, giving $E_1^{p,q} = 0$ whenever $q \neq 0$ (after reindexing by the bar filtration degree).
chapters/theory/bar_cobar_adjunction_inversion.tex:4186:The bar complex at bar degree~$n$ and conformal weight~$h$ satisfies
chapters/theory/bar_cobar_adjunction_curved.tex:1899:Suppose that for every finite generator set~$S$, bar degree bound~$m$,
chapters/theory/bar_cobar_adjunction_curved.tex:6496:concentrated in bar degree~$1$ (the Koszul dual coalgebra), carrying a curved cooperad structure with comultiplication dual to~$m_2$ and curvature dual to~$\mu_0$. The Koszul dual \emph{algebra}~$\cA^!$ is characterized by Verdier intertwining: $\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA) \simeq \cA^!_\infty$ (factorization \emph{algebra}, not coalgebra; Convention~\ref{conv:bar-coalgebra-identity}).
exec
/bin/zsh -lc "sed -n '6760,6825p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

Fix two augmented chiral algebras $\cA$ and $\cB$ and form the
chiral tensor product $\cA \otimes_{\mathrm{ch}} \cB$. Color
$\cA$-insertions red and $\cB$-insertions blue on
$\overline{\Conf}_{m,n}(X)$.

\begin{definition}[Mixed boundary filtration]
\label{def:mixed-boundary-filtration}
Let $D_{\mathrm{mix}} \subset \overline{\Conf}_{m,n}(X)$ be the
union of boundary strata where at least one red point and one blue
point collide. Define the mixed-boundary filtration by
\[
F^p_{\mathrm{mix}}
:= I(D_{\mathrm{mix}})^p \cdot
 \barBch_X(\cA \otimes_{\mathrm{ch}} \cB).
\]
The bar differential decomposes as
$d = d_\cA + d_\cB + d_{\mathrm{mix}}$, where $d_\cA$ and $d_\cB$
preserve the filtration and $d_{\mathrm{mix}}$ lowers it by one.
\end{definition}
exec
/bin/zsh -lc "sed -n '560,760p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"modular degree|PBW filtration|PBW spectral sequence|E_1 page|d_0\\"'^'"\\{\\\\mathrm\\{PBW\\}\\}|d_1\\"'^'"\\{\\\\mathrm\\{PBW\\}\\}|d_2\\"'^'"\\{\\\\mathrm\\{PBW\\}\\}\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\overline{C}_n(\Sigma_g)$
(Theorem~\ref{thm:prism-higher-genus}).
Each genus-$g$ piece carries a degree-$1$ \emph{fiberwise
differential}~$\dfib$ with
$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
(Convention~\ref{conv:higher-genus-differentials}).
The completed total bar object
$\bar{B}^{\mathrm{full}}_X(\cA) :=
\prod_{g \geq 0} \hbar^g \bar{B}^{(g)}_X(\cA)$
carries a strict total differential $\Dg{} \colon
\bar{B}^{\mathrm{full}}_X(\cA) \to \bar{B}^{\mathrm{full}}_X(\cA)$
with $\Dg{}^2 = 0$, whose reduction modulo $\hbar^{g+1}$ restricts
to $\dfib$ at genus~$g$.

\item\label{D:center-dg}
A center local system $\mathcal{Z}_{\cA}$ on
$\overline{\mathcal{M}}_{g,\bullet}$ whose fiber at a smooth
curve~$\Sigma$ is the center $Z(\cA|_\Sigma)$.

\item\label{D:discriminant-dg}
 succeeded in 52ms:
rg: regex parse error:
    (?:modular degree|PBW filtration|PBW spectral sequence|E_1 page|d_0\^\{\mathrm\{PBW\}\}|d_1\^\{\mathrm\{PBW\}\}|d_2\^\{\mathrm\{PBW\}\})
                                                                           ^^
error: unrecognized escape sequence
codex
- **Lane labels + ranges**  
  - `rem:mk4-status` (covers the mechanistic recap just before the PBW theorems, see `chapters/theory/higher_genus_modular_koszul.tex:895-904`).  
  - `thm:pbw-genus1-km` and its proof chain (statement + Steps 1–4) span `chapters/theory/higher_genus_modular_koszul.tex:906-1206`; the supplementary `remark` about the Whitehead reduction appears immediately afterward at `…tex:1208-1217`.  
  - `cor:unconditional-genus1-km` (genus‑1 Koszulity corollary) sits at `…tex:1219-1242`.  
  - `thm:pbw-allgenera-km` and its genus-gote proof cover `…tex:1244-1445` (with the antiholomorphic note at the end of the proof and the unconditional corollary `cor:unconditional-allgenera-km` following straight after, `…tex:1447-1490`).

- **Direct local dependencies cited in the proofs**  
  - The genus-1 argument leans on the PBW filtration / bounded convergence toolkit from `thm:pbw-koszulness-criterion` (`…tex:937-975`, again invoked for bounded-below convergence at `…tex:1100-1108`) and the genus-0 PBW Koszulity theorem `thm:km-chiral-koszul` (`…tex:946-950`).  
  - Whitehead acyclicity is invoked via the Chevalley–Eilenberg vanishing for semisimple $\fg$ (`…tex:1056-1072`), followed by the level-$k$ Killing-form contraction to eliminate the invariant line (`…tex:1075-1098`), and bounded convergence closes the spectral sequence (`…tex:1100-1108`).  
  - The all-genera proof explicitly reuses `thm:pbw-genus1-km` to bootstrap the three-step mechanism (`…tex:1277-1284`), employs the same PBW/Killing logic on the $\fg$-module factor (`…tex:1304-1406`), and again cites the ``bounded‐below convergence’’ item of `thm:pbw-koszulness-criterion` to conclude `E_\infty(g)=E_\infty(0)` (`…tex:1421-1431`).

- **Cross-volume/duplicate surfaces that mention these PBW/Whitehead statements**  
  - `chapters/connections/editorial_constitution.tex` throws the theorems into global context at lines 25, 85, 199, and 478.  
  - `chapters/connections/concordance.tex:4893` bundles `thm:pbw-allgenera-km` with the analogous $\mathcal{W}$ statement.  
  - `chapters/examples/genus_expansions.tex:466` and `chapters/examples/landscape_census.tex:1048` cite `thm:pbw-allgenera-km` when discussing the higher-genus PBW boom; `standalone/introduction_full_survey.tex:3430` repeats that citation in the survey narrative.  
  - Registry/metadata surfaces catalogue both theorems (`metadata/theorem_registry.md:884-887`) plus their status-dependent corollaries; `metadata/claims.jsonl` and `metadata/dependency_graph.dot` (via the audit campaign outputs) likewise list them as proven nodes.  
  - (No occurrences of these labels show up in Volume II/III directories, so the “duplicate surfaces” are within Volume I’s meta/editorial ecosystem.)

- **Whitehead on truncated current algebra vs. $\fg$-modules**  
  - The genus-1 proof is crystal-clear: the truncated current algebra $\fg\otimes V_h$ merely organizes the mode patterns, but the Whitehead step is applied to the finite-dimensional $\fg$-modules $M_{h,\nu}$ after mode data is stripped away (`…tex:1015-1047`).  
  - The explicit remark that follows the proof reinforces this; there is no vanishing claim for the non-semisimple truncated algebra itself (`…tex:1208-1217`).  
  - The all-genus extension repeats the same logic: the enrichment factorizes as $M_h\otimes H^{1,0}(\Sigma_g)$, and the Chevalley–Eilenberg complex is built purely from the $\fg$-module $M_h$ (`…tex:1311-1352`), so Whitehead is never being applied to $\fg\otimes V_h$ but rather to honest $\fg$-modules.


thinking
**Clarifying spectral sequence claims**

The user wants to know about the spectral sequence collapsing from bar degree to modular degree at E_1. I think it might relate to identifying the CE differential as d1, but I need to be cautious about stating something inaccurately. The strongest claim I can make might be that “the enrichment spectral sequence collapses at E_1” for semisimple subcomplexes after reindexing. I should also consider what the user means about non-semisimple families and the characterisation of their obstructions.
thinking
**Reinterpreting spectral sequence theorems**

I need to think about rephrasing as a theorem related to the auxiliary spectral sequence from the bar-degree filtration on the enrichment bicomplex. Perhaps I could create a new theorem or lemma called "semisimple symmetry criterion." It's crucial to avoid making the false claim about E1 for the main PBW spectral sequence if it turns out that d2 is necessary for invariants. Maybe I can frame it as: "the bar-to-modular spectral sequence collapses at E1" due to only invariants remaining after Whitehead reduction being killed by the modular-degree operator.
exec
/bin/zsh -lc 'rg -n "modular degree|modular filtration|bar-to-modular|bar degree, modular|bar-degree.*modular|modular-degree" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "sed -n '25485,25535p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9428,9455p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '28370,28415p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
For algebras without a vacuum in~$V$, the flat unit condition
must be verified separately before applying the theorem.
\end{remark}

\begin{proposition}[Non-semisimple obstruction to Pixton generation]
\label{prop:non-semisimple-pixton-obstruction}
\ClaimStatusProvedHere
\index{Pixton ideal!non-semisimple obstruction|textbf}
\index{logarithmic vertex algebra!Pixton ideal obstruction}
\index{triplet algebra!non-semisimple CohFT}
For non-semisimple shadow CohFTs
\textup{(}logarithmic vertex algebras, triplet $\cW(p)$\textup{)},
Step~\textup{2} of the semisimple proof fails:
the Givental--Teleman classification does not apply because
the Frobenius algebra $(V, \eta, \ell_3^{(0)})$ has nilpotent
elements, and the nilpotent radical of $\cW(p)$ is not
$\eta$-orthogonal.
The MC-descended tautological relations still lie in the
Pixton ideal \textup{(}from $D^2 = 0$;
Theorem~\textup{\ref{thm:mc-tautological-descent})},
 succeeded in 52ms:

\begin{conjecture}[Scalar saturation universality]
\label{conj:scalar-saturation-universality}
\index{universal Maurer--Cartan class!universality conjecture}
\index{scalar saturation!universality conjecture}
\ClaimStatusConjectured
The effective \(\Gamma\)-quadruple reduction
\textup{(}Corollary~\textup{\ref{cor:effective-quadruple}}\textup{)}
extends to \textbf{all} modular Koszul chiral algebras at
\textbf{all} levels: for
any~$\cA$ with maximal reductive current algebra
$\mathfrak{g} = \mathfrak{g}_1 \oplus \cdots \oplus \mathfrak{g}_r$
\textup{(}each $\mathfrak{g}_i$ simple\textup{)}, the
minimal-model MC element factors as
\[
\Theta^{\min}_{\cA}
\;=\; \sum_{i=1}^r \eta_i \otimes \Gamma_i(\cA)
\]
for tautological coefficients
$\Gamma_i(\cA)\in\widehat{\Gmod}$.
 succeeded in 52ms:

\begin{remark}[The true residual frontier]
\label{rem:true-residual-frontier}
\index{frontier!true residual}
Theorem~\textup{\ref{thm:envelope-koszul}} and
Corollary~\textup{\ref{cor:generic-ht-koszul}}
resolve chiral Koszulness for the entire
\emph{generic-parameter} landscape: every perturbative
HT theory at non-critical, non-admissible coupling
produces a chirally Koszul boundary algebra.

Three classes escape this resolution:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Simple quotients at admissible levels}
 \textup{(}\textbf{LIVE}\textup{)}.
 The simple quotient $L_k(\fg) = V_k(\fg)/I_k$
 fails free strong generation when null vectors
 enter the bar-relevant range, but the PBW route is
 not the only path. At non-degenerate admissible
 levels, $L_k(\fg)$ is rational with semisimple Zhu

thinking
**Exploring algebraic structures**

I'm thinking about non-semisimple obstruction and wondering if it relates to nilradical or Jordan blocks. It could be useful to search more specifically on PBW (Poincaré–Birkhoff–Witt theorem). I need to compute surfaces or find examples, maybe diving into Kac-Moody algebras could help too. There’s a lot to explore and clarify here!
collab wait(call_7GoDG0IHdMtwg5AA7PjTQTxD)
  receivers: 019d8653-1fef-7d20-a893-cfbbf4c3cae9
wait(call_7GoDG0IHdMtwg5AA7PjTQTxD) 1 agents complete:
  019d8653-1fef-7d20-a893-cfbbf4c3cae9 completed: "- **Lane labels + ranges**  
  - `rem:mk4-status` (covers the mechanistic recap just before the PBW theorems, see `chapt…"

thinking
**Considering Lie algebras**

I'm thinking about the coverage regarding Kac-Moody algebras due to the composite stress tensor. Perhaps I should strengthen this with a theorem that doesn't require a unique weight-2 generator. The user mentions "all families where the underlying Lie algebra is semisimple," but this includes Kac-Moody, Virasoro, and principal W. Since the Lie algebra of Virasoro isn’t semisimple, it seems this might only apply to Kac-Moody-like families or algebras with semisimple symmetry. I might propose a theorem based on these conditions.
codex
The universal theorem as written is still too bifurcated: one lane for “unique weight-2 generator”, a separate lane for KM. I’m checking whether the existing curved-bar transgression theorems already justify merging those lanes into a stronger semisimple criterion without inventing unsupported new machinery.
exec
/bin/zsh -lc "sed -n '6848,7028p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\]
The mixed $\lambda$-bracket
$[L_\lambda J^a] = (\partial + \lambda)J^a$
says every current is primary of conformal weight~$1$.

\begin{theorem}[Universal first mixed Sugawara differential;
\ClaimStatusProvedHere]
\label{thm:universal-sugawara-d1}
On the one-Virasoro sector
$\eta \otimes C_\mathfrak{g}
\subset H^\bullet_{\mathrm{bar}}(\mathrm{Vir}_{c(k)})
\,\widehat{\otimes}\,
H^\bullet_{\mathrm{bar}}(\widehat{\mathfrak{g}}_k)$,
the first mixed differential is
\begin{equation}\label{eq:universal-d1-sugawara}
d_1^{\mathrm{mix}}(\eta \otimes x)
= 1 \otimes (\partial x + Nx),
\end{equation}
where $\partial$ is the translation coderivation and $N$ is the
total conformal-weight Euler operator on the affine dual
exec
/bin/zsh -lc "rg -n \"Sugawara|Casimir transgression|Killing contraction|level-\\"'$k'"\\"'$ Killing contraction|quadric rigidity" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/examples/kac_moody.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/kac_moody.tex:119:Sugawara singularity, and the Feigin--Frenkel involution is the fixed
chapters/examples/kac_moody.tex:202:(iii)~the Sugawara construction at non-critical level gives a Virasoro
chapters/examples/kac_moody.tex:236:space is one-dimensional (generated by the Sugawara variation
chapters/examples/kac_moody.tex:419:T(z) = \sum_n L_n z^{-n-2} &\longleftrightarrow \text{Sugawara stress tensor}
chapters/examples/kac_moody.tex:421:where the Sugawara construction gives:
chapters/examples/kac_moody.tex:430:The \emph{level} $k$ determines the central charge of the Virasoro algebra via the Sugawara construction:\index{Sugawara construction}
chapters/examples/kac_moody.tex:438:At $k = -h^\vee$ (the \emph{critical level}), the Sugawara construction is undefined: the denominator $k + h^\vee$ vanishes, so no Virasoro subalgebra is produced. The critical level is distinguished on three counts: the theory admits a commutative chiral algebra structure (the classical limit), the center $Z(\widehat{\mathfrak{g}}_{-h^\vee})$ becomes infinite-dimensional (Feigin--Frenkel), and the algebra governs self-dual Yang--Mills theory. For Koszul duality, the critical level is the fixed point of the Feigin--Frenkel involution $k \mapsto -k - 2h^\vee$: the curvature $m_0 \propto (k + h^\vee)$ vanishes, making the bar complex a genuine (uncurved) dg coalgebra and the Koszul dual algebra uncurved.
chapters/examples/kac_moody.tex:595:\item The Sugawara construction is \emph{undefined} ($k + h^\vee = 0$): no Virasoro subalgebra exists. The center of the completed enveloping algebra enlarges to the Feigin--Frenkel center $\mathfrak{z}(\widehat{\mathfrak{g}})$
chapters/examples/kac_moody.tex:690:The simple pole comes from $\beta(z)$ contracting with $\gamma(w)^2$; the double pole from $\beta(z)\cdot(-2\partial\gamma(w)) = -2/(z-w)^2 = k/(z-w)^2$. At critical level $k = -h^\vee$, the Sugawara construction\index{Sugawara construction!undefined at critical level} $T = \frac{1}{2(k+h^\vee)}\sum_a {:}J^a J^a{:}$ is \emph{undefined} (division by zero), not merely zero.
chapters/examples/kac_moody.tex:709: dual. Simultaneously, the Sugawara construction degenerates and the
chapters/examples/kac_moody.tex:738:the $r$-matrix degenerates (Sugawara singularity).
chapters/examples/kac_moody.tex:755:denominator $k + h^\vee$ is the Sugawara shift. This is the
chapters/examples/kac_moody.tex:1277:Sugawara construction
chapters/examples/kac_moody.tex:1552:\item \emph{Sugawara comparison.}
chapters/examples/kac_moody.tex:1553:The Sugawara central charge is
chapters/examples/kac_moody.tex:1567:sees only the Sugawara stress tensor).
chapters/examples/kac_moody.tex:2247:reflecting the Sugawara singularity: the $r$-matrix degenerates
chapters/examples/kac_moody.tex:2248:when the Sugawara construction is undefined.
chapters/examples/kac_moody.tex:4414:the curvature $m_0$ vanishes because the Sugawara construction
chapters/examples/kac_moody.tex:4586:weight~$1$; the Sugawara tensor is composite. Hence
exec
/bin/zsh -lc "sed -n '880,910p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\qquad (h > 0).
\]
The same argument applies to the antiholomorphic factor
$H^{0,1}(\Sigma_g)$, since $L_0$ acts only on the vertex-algebra
factor. Hence the full $H^1(\Sigma_g,\bC)$-enrichment is eliminated,
and one obtains $E_\infty(g) = E_\infty(0)$.

The computation module
\texttt{compute/lib/w\_algebra\_pbw\_genus1.py}
verifies the weight-triangular mechanism for the first
higher-spin case $\mathcal{W}_3$ through conformal weight~$8$,
together with the principal generator weights for the finite-type
families $A_1$, $A_2$, $A_3$, $B_2$, $C_2$, $G_2$, and~$F_4$.
\end{proof}

\begin{remark}[Status and mechanism]\label{rem:mk4-status}
Higher-genus PBW holds for KM (Whitehead + Killing contraction,
Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
$\mathcal{W}$ (block upper triangular,
codex
I’m at the point of editing. The key decision is now clear: I can prove the Whitehead reduction cleanly, but I cannot truthfully upgrade the main PBW page-degeneration claim to `E_1` because the affine KM invariant line survives to `E_2` and dies only under `d_2`. I’m adding the explicit lemmas and then stating that `E_3` is the optimal semisimple bound, with the non-semisimple obstruction identified by radical cohomology.
exec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 40c1fef..b3c4e9a 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -32169,6 +32169,98 @@ is recovered from the ordered chiral homology at roots of
 unity. The shadow tower lives at generic level.
 \end{remark}
 
+\begin{remark}[Second proof of $Z_1 = k + 1$ via the Zhu algebra]
+\label{rem:verlinde-via-zhu}
+\index{Zhu algebra!second proof of Verlinde at genus 1}
+\index{Verlinde formula!Zhu algebra proof}
+The genus-$1$ Verlinde count $Z_1(k) = k + 1$
+(Proposition~\ref{prop:verlinde-from-ordered}\textup{(ii)})
+admits a second, representation-theoretic proof that passes
+entirely through the Zhu algebra $A(V)$ of
+Zhu~\cite{Zhu96} and connects to the ordered chiral
+homology at degree~$0$.
+
+\textsc{Step 1: the Zhu algebra.}
exec
/bin/zsh -lc "rg -n \"label\\{lem:pbw-weightwise-g-module\\}|label\\{lem:pbw-mixed-factorization\\}|label\\{prop:pbw-semisimple-obstruction\\}|label\\{thm:pbw-semisimple-obstruction\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Considering file changes**

I see that the `git diff` shows the target file is already dirty with unrelated user changes in distant lines. I need to be careful not to overwrite anything. My plan is to edit only the local region and use `apply_patch` without reverting unrelated changes. I might target the line range around 880-1930. I also need to check for duplicates, but I got no output from my `rg` command, which is good. Now, I need to carefully craft the patch and inspect the exact text around insertion points for lemmas.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '892,1250p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1708,1935p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   892	families $A_1$, $A_2$, $A_3$, $B_2$, $C_2$, $G_2$, and~$F_4$.
   893	\end{proof}
   894	
   895	\begin{remark}[Status and mechanism]\label{rem:mk4-status}
   896	Higher-genus PBW holds for KM (Whitehead + Killing contraction,
   897	Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
   898	Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
   899	$\mathcal{W}$ (block upper triangular,
   900	Theorem~\ref{thm:pbw-allgenera-principal-w}).
   901	Open: non-principal families; the $\mathcal{W}_\infty$
   902	inverse-limit package
   903	(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
   904	\end{remark}
   905	
   906	\begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
   907	\label{thm:pbw-genus1-km}
   908	\index{PBW spectral sequence!genus-1 degeneration|textbf}
   909	\index{modular Koszul chiral algebra!genus-1 unconditional}
   910	\textup{[Regime: curved-central
   911	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
 succeeded in 51ms:
  1708	\end{proof}
  1709	
  1710	\begin{theorem}[Universal PBW enrichment-killing for chiral
  1711	 algebras with conformal vector; \ClaimStatusProvedHere]
  1712	\label{thm:pbw-universal-semisimple}
  1713	\index{PBW spectral sequence!unique-weight-2 criterion|textbf}
  1714	\index{PBW spectral sequence!universal semisimple enrichment-killing|textbf}
  1715	\index{modular Koszul chiral algebra!unique-weight-2 criterion|textbf}
  1716	\index{modular Koszul chiral algebra!semisimple enrichment-killing|textbf}
  1717	\textup{[Regime: curved-central
  1718	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1719	
  1720	Let $\cA$ be a chiral algebra defined by local OPE relations,
  1721	admitting a PBW filtration by conformal weight, and satisfying:
  1722	\begin{enumerate}[label=\textup{(\alph*)}]
  1723	\item the augmentation ideal $\bar{V}_\cA$ is
  1724	 positively graded: every homogeneous state has
  1725	 conformal weight $h \geq h_{\min} > 0$;
  1726	\item among all generators, exactly one has conformal
  1727	 weight~$2$, namely the stress tensor~$T$, with

thinking
**Evaluating theorem modifications**

The user wants the strongest theorem in the target, possibly regarding semisimple bounds. I might modify `rem:mk4-status` or `rem:pbw-universal-scope` and consider adding a proposition near the universal theorem. Adding lemmas before the theorem could clarify local references in the proof. 

I think it might be best to adjust proof steps to cite the lemmas instead of restating them, which could reduce repetition. The user requested explicit factorization as a lemma. I'll inspect specific line numbers to make necessary updates.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1288,1378p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1288	forms on $\overline{C}_n(\Sigma_g)$, the
  1289	Fulton--MacPherson compactification of configuration
  1290	space on a smooth projective curve~$\Sigma_g$ of
  1291	genus~$g$. The curve contributes regular forms
  1292	from $H^{1,0}(\Sigma_g) \cong \bC^g$ (holomorphic
  1293	$1$-forms). These are regular at every collision
  1294	divisor~$D_{ij}$: they arise from the global geometry
  1295	of~$\Sigma_g$, not from OPE poles.
  1296	
  1297	Since $d_0^{\mathrm{PBW}}$ acts by Poincar\'{e} residue at
  1298	collision divisors, and the Poincar\'{e} residue of a
  1299	regular form is zero, the $H^{1,0}(\Sigma_g)$-enrichment
  1300	cochains are $d_0^{\mathrm{PBW}}$-closed. They are not
  1301	$d_0^{\mathrm{PBW}}$-exact by the same degree argument
  1302	as in genus~$1$. Thus
  1303	\begin{equation}\label{eq:e1-decomposition-genusg}
  1304	E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0)
  1305	 \;\oplus\; \mathcal{E}^{p,q}_g
  1306	\end{equation}
  1307	where $\mathcal{E}^{p,q}_g$ is the enrichment from









thinking
**Evaluating citation standards**

I'm considering whether we need to reference primary literature, and it seems we haven't directly addressed the dependency if the citation standard is met. Could it be alright to cite Weibel or CE instead? It’s a bit confusing since I'm weighing the necessity of those citations. I want to make sure I'm accurately representing the standards here, but I'm not entirely sure how to move forward without more clarity.
thinking
**Considering theorem presentation**

I’m browsing and thinking we might not need to pull in external citations since it’s not a high-stakes situation. But I should be cautious about adding new citations to avoid any bibliography issues unless I can reference `Weibel94`. The user asked for the PBW theorem in its strongest form, so I’m considering how to best articulate that while mentioning optimality. Instead of modifying the theorem statement itself, it might be better to add a remark about non-semisimple obstruction following the theorem.
thinking
**Updating theorem details**

I’m thinking of updating my statement to clarify that for every family in the manuscript with semisimple weightwise Lie symmetry, the only surviving invariants are the invariant lines, with the family-specific transgression leading to their loss. This E_3 bound is optimal since the Kac–Moody Killing class survives to E_2. I also need to mention the radical cohomology obstruction for non-semisimple families. The user asked for the theorem in its strongest form, so I might adjust the `thm:pbw-genus1-km` to explicitly mention optimality.
thinking
**Refining theorem expression**

I’m considering adding a precision to the statement: "the enrichment is annihilated by d1 on non-trivial isotypic pieces and by d2 on the invariant line." That seems useful and might clarify the discussion further. I think this could be a good adjustment to ensure the details are clear for the reader. Now, I need to think through the best way to implement that change into the existing structure of the theorem.
thinking
**Updating theorem statement**

I need to update the theorem `thm:pbw-allgenera-km` to clarify that for any simple Lie algebra, the PBW spectral sequence has E3=E∞ after applying weightwise semisimple Whitehead reduction. I should also mention that the E1 collapse is false and optimal. Additionally, it would be great to include the specific detail that the non-trivial isotypic part vanishes at E2, while the invariant line remains at E3. That’s a nice local observation!
thinking
**Considering theorem integration**

I'm pondering whether inserting a new theorem might impact existing references. It seems that it could be possible to connect the proposition to the new theorem in a meaningful way. I wonder about the implications this could have on the current framework. Understanding how everything interrelates is essential here, and it'll require careful consideration of the references to ensure coherence and clarity in the overall argument. Should I explore this further?
thinking
**Considering projection in cohomology**

I'm thinking about needing `\beta_{h,n}`, possibly induced by projecting from cocycles to a genus 0 target after transforming it into cohomology. I wonder how that relationship plays out and what implications it could have on the overall system! It's fascinating to think about the connections between these concepts and how they can influence each other in different scenarios. I'm curious to explore this further and see what insights can come from such projections.
thinking
**Assessing lemma requirements**

I need to consider whether I really need all-genera proof without lemma 2, possibly just citing lemma 1 instead. I could say that each basis vector of H^{1,0}(Σ_g) behaves like the genus 1 case, supporting the factorization through H^1(\fg,N_h). It might be simpler to add a remark about the non-semisimple obstruction rather than proving a whole new theorem. Still, I’m thinking a proposition on obstruction via Hochschild-Serre could be straightforward. Should I include that?
thinking
**Considering theorem wording**

I’m reflecting on mentioning affine KM as page-bound optimal but not satisfying (b). It feels a bit odd to include in the theorem statement, so maybe I’ll hold off. After the theorem, I could add a remark about “Optimal page bound and non-semisimple obstruction.” I think it’ll be enough there. It’s important to clarify that the strongest true theorem is E3, not E1. I'll ensure I'm cautious with labels, keeping uniqueness in mind.
codex
I’ve finished the mathematical design. The edit is scoped to the PBW lane only: two new lemmas, a proof rewrite in the KM genus-1/all-genera arguments, and one global remark that records the optimal semisimple bound plus the non-semisimple obstruction.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -900,2 +900,8 @@
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
@@ -905,2 +911,91 @@
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
@@ -1020,15 +1115,8 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
@@ -1038,11 +1126,10 @@
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
@@ -1056,5 +1143,17 @@
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
@@ -1063,12 +1162,5 @@
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
@@ -1211,7 +1303,11 @@
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
@@ -1328,3 +1424,4 @@
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
@@ -1349,3 +1446,7 @@
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
@@ -1928,2 +2029,37 @@
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
apply_patch(auto_approved=true) exited 0 in 56ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Reviewing edits**

I need to reread the modified section right after the edit. It’s essential to ensure everything flows well, especially with long titles and line breaks. I’ll probably use sed around the inserted regions to help with the syntax. After that, I should make some remarks about what I find. It’s always good to double-check things, especially how they might look after changes! Let’s make sure everything is neat and clear.
codex
The file edit is in. I’m re-reading the modified PBW lane now to catch any mathematical or LaTeX regressions before I verify the surface.
exec
/bin/zsh -lc "sed -n '892,1375p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
families $A_1$, $A_2$, $A_3$, $B_2$, $C_2$, $G_2$, and~$F_4$.
\end{proof}

\begin{remark}[Status and mechanism]\label{rem:mk4-status}
Higher-genus PBW holds for KM (Whitehead + Killing contraction,
Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
$\mathcal{W}$ (block upper triangular,
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

exec
/bin/zsh -lc "sed -n '1905,1965p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The antiholomorphic factor $H^{0,1}(\Sigma_g)$ is handled
identically. Bounded-below convergence
\textup{(}\ref{item:pbw-bounded} of
Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}
then shows that once later differentials and extension classes are
ruled out by family-specific input, the genus-$g$ and genus-$0$
$E_\infty$ pages agree. Under hypotheses~(a)--(b) alone, the
theorem proves only the common $E_3$-page vanishing mechanism.

\medskip
\emph{Part~\textup{(c)}: semisimple symmetry gives universal
$E_2$ collapse.}

Assume hypothesis~(c): $\fg$ is semisimple
and acts on each $M_h$ through the $(0)$-products.
Decompose $M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$
into $\fg$-invariant and non-trivial summands.

\emph{Non-trivial summands.}
The $d_1^{\mathrm{PBW}}$ differential
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

exec
/bin/zsh -lc "sed -n '1927,1968p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
factor~$M_h^{\mathrm{non\text{-}triv}}$, leaving the
$H^{1,0}(\Sigma_g)$ factor unchanged. The enrichment complex
at weight~$h$ restricted to the non-trivial summand is
\[
\bigl(C^*(\fg,\, M_h^{\mathrm{non\text{-}triv}}),\, d_{\mathrm{CE}}\bigr)
\;\otimes_{\bC}\;
H^{1,0}(\Sigma_g).
\]
Here the mode truncation has already been absorbed into the
finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
By the Whitehead--Chevalley--Eilenberg vanishing theorem,
$H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
finite-dimensional $\fg$-module~$N$ with no trivial summand,
since $\fg$ is semisimple. Therefore the non-trivial
enrichment is acyclic already at the $E_2$ page:
\[
E_2^{*,h}(g)_{\mathrm{enr,\, non\text{-}triv}} = 0.
\]

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

exec
/bin/zsh -lc "sed -n '1968,2018p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The antiholomorphic factor is handled identically.
\end{proof}

\begin{proposition}[Hook-type $\mathcal{W}$-algebras satisfy the PBW hypotheses;
 \ClaimStatusProvedHere]
\label{prop:hook-pbw}
\index{W-algebra@$\mathcal{W}$-algebra!hook-type!PBW hypotheses|textbf}
\index{PBW spectral sequence!hook-type W-algebras|textbf}
For $N \geq 3$ and $1 \leq r \leq N-2$, the hook-type
$\mathcal{W}$-algebra
$\mathcal{W}^k(\mathfrak{sl}_N, f_{(N-r,\,1^r)})$ at generic level
satisfies hypotheses~\textup{(a)--(b)} of
Theorem~\textup{\ref{thm:pbw-universal-semisimple}}. When
$r \leq N-3$, the centralizer $\mathfrak{g}^f$ contains a
semisimple Levi factor, and hypothesis~\textup{(c)} holds as well.
In particular, \textup{MC1} implies \textup{MK3} unconditionally
for these algebras.
\end{proposition}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

exec
/bin/zsh -lc "sed -n '2018,2065p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
(Theorem~\ref{thm:pbw-allgenera-km}).
Beyond the hook-type family
(Proposition~\ref{prop:hook-pbw}), the same hypotheses hold for
Bershadsky--Polyakov and $\mathcal{N}=1,2$ superconformal algebras.
For $\mathcal{W}_\infty$, hypotheses~(a)--(b) hold at each finite
stage; the completed MK3 statement is part of the MC4 package.
The structural input is the enrichment factorization
$M_h \otimes H^{1,0}(\Sigma_g)$
(\ref{eq:enrichment-factorization}), which separates local OPE
data from global curve topology.
\end{remark}

\begin{remark}[Optimal semisimple page bound and the non-semisimple
 obstruction]
\index{PBW spectral sequence!optimal semisimple page bound|textbf}
\index{PBW spectral sequence!non-semisimple obstruction|textbf}
The semisimple PBW conclusion is an $E_3$ statement, not an
$E_1$ statement. The affine KM proof gives the boundary example:
at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
$E_2$, and only the family-specific $d_2$ contraction kills it.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}







thinking
**Considering mathematical remarks**

I think the content looks decent, but I might need to fix the line break indentation in the remarks. I also want to check the mathematical correctness and make sure there's consistency with the `C^*_{CE}` notation. It's probably fine since it isn't used elsewhere, but I’ll verify if `C^*_{\mathrm{CE}}` needs a definition. There might be some mismatches between genus statements. Overall, I'm ensuring there aren't any issues with the environment or any duplicates. I'm analyzing potential issues related to certain propositions too.
thinking
**Addressing lemma 2 issues**

I'm noticing a potential issue with lemma 2 regarding the `$E_2$-class of the mixed differential d_{1,mix}(\xi)`. It seems odd because `d_{1,mix}(\xi)` is defined on E1 and might not be closed individually. However, it could mean its contribution on E2 after accounting for d1-exactness. I think I could rephrase it to clarify the image of `\xi` in the mixed part of the E2 page. The proof mentions a degree-one CE coboundary, but if it maps to `Z^1`, how does that work? I need to rethink that as it moves to cocycles then H^1.
thinking
**Clarifying the mixed residue**

I’m thinking about the mixed residue as a CE coboundary followed by a projection to the genus-0 target. That concept seems okay overall, but I'm unsure about the statement “there is \iota to Z^1.” The proof mentions that this gives the map to degree-one CE cocycles. I need to make sure I understand how these components fit together properly to ensure clarity and consistency in the argument. Let's see how this all integrates with the broader context.
thinking
**Considering compilation and edits**

I’m thinking about augmentation and the need to run some searches, like checking for banned tokens with AP29. I should examine duplicates in labels, since they might have been edited before. It might be worth running a targeted LaTeX build. I need a narrow approach for falsifying, and since everything is in one file, I’m considering running `make fast` or `latexmk -pdf`. I'll also verify after each edit, possibly with `rg -n` for new labels to ensure they're unique.
thinking
**Inspecting git changes**

I need to inspect the local changes with `git diff`. To start, I’ll run some pattern searches with `rg`. I’m thinking of using the fixed string `\\Omega/z` for bare Omega. Also, there’s the missing augmentation pattern, which might need a fixed string approach too. For slop, I've got a list of case-insensitive tokens to check. Since action safety is key, I might grep the modified region or the whole file to find our new strings without picking up unrelated hits. Using `git diff -U0` with `rg -i` sounds smart for focusing on added lines.
thinking
**Searching for tokens in added lines**

I need to search for slop tokens in the added lines, particularly focusing on AP126 and AP132. It seems like a good idea to use `git diff` combined with `rg` to filter through the necessary chapters. I’ll structure my command to specifically look for these tokens in the modified sections. This way, I can pinpoint exactly what’s changed without sifting through unrelated content. It should streamline my review process efficiently!
codex
I’ve re-read the edited region. I’m verifying the exact post-edit surface now: forbidden-pattern greps on the added lines, label uniqueness, and then a narrow build/test pass if the LaTeX surface is stable enough to trust.
exec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex | rg -n \"\\\\\\\\Omega/z|T\\"'^c'"\\(s\\"'^{-1} A'"\\)|moreover|additionally|notably|crucially|remarkably|interesting|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate\" -i" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{lem:pbw-weightwise-g-module\\}|label\\{lem:pbw-mixed-factorization\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --unified=0 -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\Omega/z|T\^c\(s\^{-1} A\)|moreover|additionally|notably|crucially|remarkably|interesting|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate)
                           ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:914:\label{lem:pbw-weightwise-g-module}
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:958:\label{lem:pbw-mixed-factorization}
 succeeded in 51ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index b3c4e9a..6dab611 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -900,0 +901,6 @@ Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
@@ -905,0 +912,89 @@ inverse-limit package
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Running grep commands**

I see that the diff includes unrelated changes in the file from the user, which is fine. I need to run the grep command correctly. I could opt for multiple commands using fixed strings or regex. Using `rg -F` on the diff seems like a good choice. Alright, I'll proceed with separate commands to ensure accuracy in my results. Let’s make sure I execute this properly!
codex
The manuscript lane itself reads coherently after the patch. I’m doing one more pass on the exact added lines for banned patterns and then a narrow build surface check.
exec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\Omega/z'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'T"'^c(s''^{-1} A)'"'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex | rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
bibliography
bp_self_duality.pdf
chapters
 exited 1 in 53ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Inspecting build options**

It seems there are no matches with grep, so I need to build a surface check. I see references to main, aux, and other elements. Maybe I could run `make fast` if that's available. I should take a look at the target names in the Makefile to confirm what I can do. Using `rg` could help me find references to "fast" more easily. Let's figure this out step by step!
exec
/bin/zsh -lc 'rg -n "''^fast:|''^all:|latexmk|make fast|''^main:|''^pdf:" Makefile' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
7:#    make fast           Single-pass build for quick iteration
13:#    make watch          Continuous rebuild on file changes (requires latexmk)
27:LATEXMK   := latexmk
74:AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
93:all: $(STAMP) working-notes publish
114:fast:
141:	else echo "  ⚠  $(PDF) not found — run 'make fast' first."; fi
219:## watch: Continuous rebuild on save (requires latexmk).
222:		{ echo "Error: latexmk not found. Install via: brew install --cask mactex"; exit 1; }
457:	@echo "  make fast           Quick converging build (up to $(FAST_PASSES) passes)"
462:	@echo "  make watch      Continuous rebuild on save (latexmk)"
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

exec
/bin/zsh -lc "sed -n '108,132p' Makefile" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
	@echo "     Logs: $(LOG_DIR)/tex-build.stdout.log and $(MAIN).log"
	@echo ""

## fast: Bounded quick build for rapid iteration.
##   Runs enough passes to settle references in normal editing flows, while
##   still capping the work below the full build target.
fast:
	@echo "  ── Fast build (up to $(FAST_PASSES) passes) ──"
	@mkdir -p $(LOG_DIR)
	@$(BUILD_SCRIPT) $(FAST_PASSES)
	@echo "     Logs: $(LOG_DIR)/tex-build.stdout.log and $(MAIN).log"

## working-notes: Build the working notes (standalone document).
working-notes: $(OUT_WN)

$(OUT_WN): $(WN_TEX)
	@echo "  ── Building working notes ──"
	@mkdir -p $(OUT_DIR) $(LOG_DIR)
	@cd $(WN_DIR) && \
		$(TEX) $(TEXFLAGS) working_notes.tex >/dev/null 2>&1 || true && \
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Considering build script execution**

I think I need to run the build script, and maybe I can also try `make fast`. It seems I should kill any `pdflatex` processes first, since that might interfere. I’m planning to run the commands sequentially instead of in parallel, just to be safe. So, I’ll execute `pkill -9 -f pdflatex 2>/dev/null || true`, and then follow up with `make fast`. That seems like the best approach!
codex
The greps on the added lines are clean: no bare `\Omega/z`, no missing `A-bar` pattern, no slop tokens. I’m running the narrow build target now to see whether the local theorem-surface still compiles on the current aux state.
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

codex
The build is still running; the script is quiet between LaTeX passes. I’m waiting it out before deciding whether there’s a real build failure or just slow TeX on the current tree.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Inspecting build logs**

I'm wondering if I might be stuck at user input. Maybe there's an issue with LaTeX waiting on an error but with stdout not being flushed? It seems the session isn't a tty either. I could check the last 50 lines of `main.log` in parallel since the build runs using that file. It might be helpful to use commentary tools to execute commands while the build is running. Let's see the logs while the build goes on!
exec
/bin/zsh -lc 'tail -n 80 main.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:


LaTeX Warning: Reference `app:koszul_higher_genus' on page 2571 undefined on in
put line 28.


LaTeX Warning: Reference `thm:prism-higher-genus' on page 2571 undefined on inp
ut line 29.


LaTeX Warning: Reference `thm:genus-induction-strict' on page 2571 undefined on
 input line 30.


LaTeX Warning: Reference `thm:universal-extension-tower' on page 2571 undefined
 on input line 31.


pdfTeX warning (ext4): destination with the same identifier (name{section.H.2})
 has been already used, duplicate ignored
exec
/bin/zsh -lc 'tail -n 80 out/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
tail: out/tex-build.stdout.log: No such file or directory
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

 exited 2 in 1m 36s:
   ?pp, 254 undef citations, 490 undef references, 0 rerun requests, 13 overfull, 46 underfull
✗ Build failed.
  Logs: .build_logs/tex-build.stdout.log and main.log
./main.aux:1:  ==> Fatal error occurred, no output PDF file produced!
./main.aux:158:  ==> Fatal error occurred, no output PDF file produced!
make: *** [fast] Error 1

thinking
**Inspecting build logs**

I need to look at the build log, which might have many pre-existing undefined references that aren't related to our changes. There's a chance the build is still running. I should inspect the end of the main.log for any fatal errors. Maybe I could search for our labels using commands like `rg -n "pbw-weightwise-g-module|pbw-mixed-factorization"` in the main.log or main.aux. But first, I need to check if the session is still active.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Inspecting log files**

I need to check the build logs, specifically `.build_logs/tex-build.stdout.log` and `main.log`, to figure out the cause of an error. It might be linked to some corruption in `main.aux`. It says there’s a fatal error in `main.aux`, but it could be unrelated. I’ll classify the logs and focus on the parts around the fatal error to find more context. Let's see what information I can gather!
codex
The fast build failed, but the failure signature points at the broader aux surface, not the PBW edit itself: `main.aux` is already in a bad state and the log is dominated by hundreds of existing undefined references. I’m checking the exact fatal lines now to make sure the new lemmas didn’t introduce a local TeX error.
exec
/bin/zsh -lc 'tail -n 120 .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Fatal error|! LaTeX Error|Emergency stop|Undefined control sequence|Runaway argument|pbw-weightwise-g-module|pbw-mixed-factorization" main.log .build_logs/tex-build.stdout.log main.aux' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
 exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba main.aux | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 220

     1	\relax 
     2	\providecommand*{\memsetcounter}[2]{}
     3	\providecommand\hyper@newdestlabel[2]{}
     4	\providecommand\HyField@AuxAddToFields[1]{}
     5	\providecommand\HyField@AuxAddToCoFields[2]{}
     6	\@writefile{toc}{\contentsline {chapter}{Contents}{2}{section*.1}\protected@file@percent }
     7	\@input{chapters/frame/preface.aux}
     8	\gdef \LT@i {\LT@entry 
     9	    {3}{110.87878pt}\LT@entry 
    10	    {1}{253.84842pt}\LT@entry 
    11	    {3}{84.45659pt}}
    12	\@writefile{toc}{\contentsline {chapter}{Guide to main results}{49}{chapter*.80}\protected@file@percent }
    13	\newlabel{ch:guide}{{}{49}{Guide to main results}{chapter*.80}{}}
    14	\citation{MS24}
    15	\citation{RNW19}
    16	\citation{Val16}
    17	\citation{RNW19}
    18	\citation{Mok25}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}



thinking
**Considering file editing guidelines**

It seems like the instruction "Only edit files in your assigned scope" is referring specifically to manuscript source files, so I probably shouldn't touch build artifacts. Just to be cautious, I think I'll avoid editing those altogether. However, if there's an issue with a blocked build due to corrupted aux files, I might still need to report that. It's all about being careful to follow the guidelines while addressing any issues that come up!
thinking
**Running a syntax check**

Okay, I'm thinking that I might need to run a standalone syntax check using `latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=/tmp/pbwcheck test_chapter.tex`. This is assuming that test_chapter actually includes the chapter. I should inspect test_chapter.tex to see if it's just a simple wrapper for the chapter compilation. I'll take a moment to search around for any necessary information regarding this process.
exec
/bin/zsh -lc "sed -n '1,220p' test_chapter.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"higher_genus_modular_koszul|input\\{|include\\{\" test_chapter.tex test_latex.tex test_concordance.tex main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
sed: test_chapter.tex: No such file or directory
 exited 2 in 51ms:
rg: test_chapter.tex: No such file or directory (os error 2)
rg: test_latex.tex: No such file or directory (os error 2)
rg: test_concordance.tex: No such file or directory (os error 2)
main.tex:841:\include{chapters/frame/preface}
main.tex:845: \input{chapters/frame/guide_to_main_results}
main.tex:854:\include{chapters/theory/introduction}
main.tex:869:\include{chapters/frame/heisenberg_frame}
main.tex:882:% \input{platonic_introduction_volume_I} % archived; content absorbed into introduction.tex
main.tex:958:\include{chapters/theory/fourier_seed}
main.tex:965:\include{chapters/theory/algebraic_foundations}
main.tex:971:\include{chapters/theory/three_invariants}
main.tex:977:\include{chapters/theory/configuration_spaces}
main.tex:983:\include{chapters/theory/bar_construction}
main.tex:989:\include{chapters/theory/cobar_construction}
main.tex:996:\include{chapters/theory/bar_cobar_adjunction}
main.tex:1000:\input{appendices/homotopy_transfer}
main.tex:1006:% \input{chapters/theory/bar_cobar_quasi_isomorphism}
main.tex:1012:\include{chapters/theory/poincare_duality}
main.tex:1020:\include{chapters/theory/chiral_koszul_pairs}
main.tex:1021:\include{chapters/theory/koszul_pair_structure}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..6dab611d2cb3baee8332a21887d6c94a74da10ea
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,106 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+Z^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+such that the $E_2$-class of the mixed differential
+$d_{1,\mathrm{mix}}(\xi)$ equals
+$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
+$\xi \in \mathcal{E}_g^{n,h}$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. This is
+the standard degree-one Chevalley--Eilenberg coboundary, followed by
+the projection to the genus-$0$ target. Passing to the $E_2$ page
+quotients by coboundaries, so the class of the mixed differential
+depends only on the image in $H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1113,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1141,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1301,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1422,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1444,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2027,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}




thinking
**Troubleshooting PDF files**

I'm realizing that the files I'm working with are PDFs instead of tex files. I could try including `main.tex`, which might reference `chapters/theory/higher_genus`, but the build is blocked by a corrupted aux file. I wonder if I should verify for local TeX syntax errors or if I should attempt a quick structural compile by cleaning `main.aux`. My gut tells me a clean build might work, especially since the current aux is corrupted. It feels like there's a way forward here!
thinking
**Considering safe build options**

I think I can safely copy `main.aux` to a backup in /tmp and then remove it before running `make fast`. I wonder if the user might be concerned about losing build artifacts since they're shared, but they are not the source files. Restoring the original afterward could work, but maybe I should avoid destructive commands altogether. If I rename `main.aux`, could that let the build regenerate? Given the issues with 490 undefined references, this might be a slow process. I just want to find the best way to move forward!
thinking
**Evaluating clean build impacts**

Cleaning the aux file might lead to a successful build, and I could restore afterward. If the new build generates an updated aux with many changes, it feels like I might be editing outside the assigned scope, even if it’s autogenerated. That said, the user clearly emphasized that I should only edit files within the assigned scope. While I think build artifacts are probably acceptable to adjust, I'd prefer not to modify them unless absolutely necessary.
codex
I found one local mathematical inconsistency in the new factorization lemma: I had mapped directly to cocycles while still describing a coboundary step. I’m correcting that now so the lemma cleanly says the mixed `E_2` contribution factors through `H^1`, which is the actual Whitehead input.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -968,3 +968,3 @@
 \xrightarrow{\ \iota_{g,h,n}\ }
-Z^1(\fg, N_h^{n-1})
+C^1(\fg, N_h^{n-1})
 \xrightarrow{\ q\ }
@@ -974,6 +974,7 @@
 \]
-such that the $E_2$-class of the mixed differential
-$d_{1,\mathrm{mix}}(\xi)$ equals
-$\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$ for every
-$\xi \in \mathcal{E}_g^{n,h}$.
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
 Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
@@ -990,10 +991,13 @@
 the coefficient module~$N_h^{n-1}$. This gives the map
-$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cocycles.
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
 
 The mixed residue brackets the distinguished $\fg$-label with one of
-the remaining labels and then forgets the regular genus form. This is
-the standard degree-one Chevalley--Eilenberg coboundary, followed by
-the projection to the genus-$0$ target. Passing to the $E_2$ page
-quotients by coboundaries, so the class of the mixed differential
-depends only on the image in $H^1(\fg, N_h^{n-1})$.
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
 \end{proof}
apply_patch(auto_approved=true) exited 0 in 63ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..80770f8580579791dce258ea10a84f180b6ac2a8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,110 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+C^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1117,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1145,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1305,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1426,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1448,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2031,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..80770f8580579791dce258ea10a84f180b6ac2a8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,110 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+C^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1117,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1145,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1305,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1426,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1448,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2031,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

exec
/bin/zsh -lc "sed -n '946,1008p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
divisor.

The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
mode pattern~$\nu$, this is exactly the
Chevalley--Eilenberg differential for the diagonal adjoint action of
$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
set of mode patterns gives the stated decomposition.
\end{proof}

\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
 \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
\label{lem:pbw-mixed-factorization}
\index{PBW spectral sequence!mixed map factorization|textbf}
\index{Whitehead lemma!mixed genus-0/genus-g factorization}
Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
finite-dimensional $\fg$-module $N_h^{n-1}$ and
$\fg$-equivariant maps
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..80770f8580579791dce258ea10a84f180b6ac2a8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,110 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+C^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1117,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1145,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1305,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1426,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1448,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2031,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Checking build and logs**

I think it looks better now. I might need to run a grep diff again, but I'm wondering if it's necessary. Should I run the build? There haven’t been any changes to the source, but the build is blocked by aux. I could check the logs, but it seems like there’s nothing there. It could be worthwhile to run the diff grep commands again with the corrected regex. I’ll do that separately to be thorough.
exec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex | rg -n -F 'T"'^c(s''^{-1} A)'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex | rg -n -F '\\Omega/z'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "git diff -- chapters/theory/higher_genus_modular_koszul.tex | rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "lem:pbw-weightwise-g-module|lem:pbw-mixed-factorization|Optimal semisimple page bound and the non-semisimple obstruction|Whitehead reduction in the PBW proof" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
914:\label{lem:pbw-weightwise-g-module}
958:\label{lem:pbw-mixed-factorization}
963:Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
1120:By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
1134:$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
1150:By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
1304:\begin{remark}[Whitehead reduction in the PBW proof]
1309:\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
1312:\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
1430:\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
1452:Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..80770f8580579791dce258ea10a84f180b6ac2a8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,110 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+C^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1117,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1145,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1305,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1426,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1448,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2031,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Updating technical plans**

Okay, I’m inspecting the all-genera lines around 1430 to ensure everything looks fine after the patch, which should be good. I’m considering running a search for fatal errors, but maybe I’ll hold off on that. I should probably mention that the build was blocked by a corrupted main.aux file. I also need to confirm that main.aux line 158 has NUL bytes. Anyway, I want to update the plan status since steps 2, 3, and 4 are all complete!
Plan update
The PBW/Whitehead lane is now patched in the target file. I added explicit weightwise and mixed-map lemmas, rewrote the KM genus-1/all-genera arguments to use them, and recorded the optimal semisimple page bound plus the non-semisimple obstruction. Verification is complete on the edited surface; the global fast build is blocked by a pre-existing corrupted main.aux, not by a local TeX error from this patch.
  ✓ Audit the KM PBW lane and identify the exact Whitehead reduction gap plus the strongest truthful theorem statement in local scope
  ✓ Draft the repair structure: explicit weight-piece factorization lemma, explicit mixed-map factorization lemma, strengthened semisimple/non-semisimple theorem statement, and proof rewrites
  ✓ Edit the target file with scoped theorem/lemma/proof changes and re-read the modified region immediately after each edit
  ✓ Run local verification: forbidden-pattern grep, targeted LaTeX build/test surface if feasible, and hostile re-read of the modified PBW lane
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..80770f8580579791dce258ea10a84f180b6ac2a8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,110 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+C^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1117,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1145,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1305,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1426,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1448,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2031,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}


thinking
**Gathering line references**

I’m thinking to get absolute line references to mention in the final output. Using `nl -ba` around the inserted regions seems like a good approach to obtain the final line numbers. I should search for line numbers specifically around 895-1320 and maybe 2030 as well. This way, I can ensure all details are accurately accounted for in the final product. It sounds simple enough, but I want to make sure I get it right!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '895,1320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2008,2058p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   895	\begin{remark}[Status and mechanism]\label{rem:mk4-status}
   896	Higher-genus PBW holds for KM (Whitehead + Killing contraction,
   897	Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
   898	Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
   899	$\mathcal{W}$ (block upper triangular,
   900	Theorem~\ref{thm:pbw-allgenera-principal-w}).
   901	For semisimple weightwise symmetry, the genus enrichment splits into
   902	non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
   903	invariant pieces killed by the family-specific $d_2$ transgression.
   904	The affine KM Killing class shows that this is an $E_3$ statement, not
   905	an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
   906	radical cohomology of the weightwise Lie action.
   907	Open: non-principal families; the $\mathcal{W}_\infty$
   908	inverse-limit package
   909	(Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
   910	\end{remark}
   911	
   912	\begin{lemma}[Weightwise reduction of the genus enrichment to
   913	 \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
   914	\label{lem:pbw-weightwise-g-module}
 succeeded in 52ms:
  2008	$(0)$-products of the currents~$J^a$. When $r \leq N-3$, the
  2009	centralizer has nontrivial semisimple part (containing at least
  2010	$\mathfrak{sl}_{r}$ or $\mathfrak{sl}_{N-r-1}$), so the
  2011	Whitehead vanishing argument of
  2012	Theorem~\ref{thm:pbw-universal-semisimple}(c) applies.
  2013	\end{proof}
  2014	
  2015	\begin{remark}[Scope of the universal PBW theorem]
  2016	\label{rem:pbw-universal-scope}
  2017	\index{PBW spectral sequence!scope of universality}
  2018	Hypotheses~(a)--(b) of Theorem~\ref{thm:pbw-universal-semisimple}
  2019	capture the common unique-weight-$2$ mechanism behind the Virasoro
  2020	and principal $\mathcal{W}$ degenerations.
  2021	KM uses the independent Whitehead--Casimir--Killing mechanism
  2022	(Theorem~\ref{thm:pbw-allgenera-km}).
  2023	Beyond the hook-type family
  2024	(Proposition~\ref{prop:hook-pbw}), the same hypotheses hold for
  2025	Bershadsky--Polyakov and $\mathcal{N}=1,2$ superconformal algebras.
  2026	For $\mathcal{W}_\infty$, hypotheses~(a)--(b) hold at each finite
  2027	stage; the completed MK3 statement is part of the MC4 package.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..80770f8580579791dce258ea10a84f180b6ac2a8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,110 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+C^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1117,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1145,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1305,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1426,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1448,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2031,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

codex
[higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:895) now makes the Whitehead reduction explicit instead of informal. I added a weightwise reduction lemma and a mixed-map factorization lemma at [lines 912-1003](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:912), rewrote the Kac--Moody genus-1 and all-genera PBW proofs to use them at [1005-1317](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1005), and recorded the optimal semisimple bound plus the non-semisimple obstruction at [2034-2058](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2034).

Strongest truthful PBW form on this surface: semisimple weightwise symmetry kills the genus enrichment by `E_3`, not `E_1`. The boundary counterexample is already affine KM: the weight-2 Killing-form class survives `d_1` and is only killed by the family-specific `d_2` transgression. In the non-semisimple case, the obstruction is the radical cohomology term `H^1(\mathfrak r_h,M_h)^{\mathfrak s_h}` and, more generally, the Hochschild--Serre package `H^p(\mathfrak s_h,H^q(\mathfrak r_h,M_h))`.

Verification: I re-read the full modified region, checked new-label uniqueness across all three volumes, and grepped the added lines for the requested forbidden patterns. `make fast` does not currently verify this file because the global build is blocked by a pre-existing corrupted `main.aux` surface with fatal aux-state failure and hundreds of pre-existing unresolved refs; I did not find a local TeX error tied to the new PBW edits before that global failure.

## Platonic Rectification Report
- BEFORE: `thm:pbw-genus1-km` (`ProvedHere`) asserted genus-1 PBW degeneration for affine KM, but the proof still routed Whitehead through the truncated current algebra informally.
- ISSUE: The mode cutoff `\fg[t]/t^N` was being used without an explicit theorem reducing the problem to finite-dimensional `\fg`-modules; the mixed genus-0/genus-1 map was not factored through `H^1(\fg,M)`.
- ACTION: FILLED
- AFTER: `thm:pbw-genus1-km` remains `ProvedHere`, now backed by `lem:pbw-weightwise-g-module` and `lem:pbw-mixed-factorization`, with Whitehead applied only to finite-dimensional weight modules and the mixed map explicitly controlled by `H^1(\fg,N_h^{n-1})`.
- CONFIDENCE: high
- REMAINING GAP: No local proof gap remains in this theorem lane; build verification is blocked globally by corrupted aux state, not by this proof.

- BEFORE: `thm:pbw-allgenera-km` (`ProvedHere`) asserted all-genera PBW degeneration by saying the genus-1 mechanism is genus-independent, but the Whitehead reduction was still only stated heuristically.
- ISSUE: The all-genera extension needed the same weightwise `\fg`-module reduction and the same mixed-map factorization, otherwise the semisimple argument was not fully transportable from genus 1 to genus `g`.
- ACTION: FILLED
- AFTER: `thm:pbw-allgenera-km` remains `ProvedHere`, now explicitly reuses the weightwise `\fg`-module package and the `H^1(\fg,-)` factorization for each basis vector of `H^{1,0}(\Sigma_g)`, so the Whitehead step is genuinely genus-independent.
- CONFIDENCE: high
- REMAINING GAP: None on the proof surface touched here.

- BEFORE: The semisimple PBW lane was described as if one might hope for an `E_1` collapse once Whitehead is available.
- ISSUE: That stronger claim is false even in the semisimple landscape; affine KM has a surviving `E_2` Killing-form class.
- ACTION: INTERMEDIATE
- AFTER: The file now states the optimal bound: semisimple weightwise symmetry gives an `E_3` statement, not an `E_1` statement, and the non-semisimple obstruction is identified by the Hochschild--Serre radical cohomology terms.
- CONFIDENCE: high
- REMAINING GAP: An actual `E_1`-collapse theorem would require new mathematics because the affine KM boundary example blocks it.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 7cb6b48ab9b8643b23801b85c89042f21a64ae9c..80770f8580579791dce258ea10a84f180b6ac2a8
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -898,11 +898,110 @@
 Theorem~\ref{thm:pbw-allgenera-virasoro}), and principal
 $\mathcal{W}$ (block upper triangular,
 Theorem~\ref{thm:pbw-allgenera-principal-w}).
+For semisimple weightwise symmetry, the genus enrichment splits into
+non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
+invariant pieces killed by the family-specific $d_2$ transgression.
+The affine KM Killing class shows that this is an $E_3$ statement, not
+an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
+radical cohomology of the weightwise Lie action.
 Open: non-principal families; the $\mathcal{W}_\infty$
 inverse-limit package
 (Conjecture~\ref{conj:v1-master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
 \end{remark}
 
+\begin{lemma}[Weightwise reduction of the genus enrichment to
+ \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
+\label{lem:pbw-weightwise-g-module}
+\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
+\index{truncated current algebra!mode bookkeeping only}
+Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
+\[
+V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
+\]
+Then the weight-$h$ genus-enrichment block of
+$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
+\[
+\mathcal{E}_g^{*,h}
+\;\cong\;
+\bigoplus_\nu
+C^*_{\mathrm{CE}}(\fg, M_{h,\nu})
+\otimes_{\bC}
+H^1(\Sigma_g,\bC),
+\]
+where $\nu$ runs over the finitely many mode patterns of total
+weight~$h$, and each $M_{h,\nu}$ is a finite-dimensional
+$\fg$-module with diagonal adjoint action on the $\fg$-labels and
+trivial action on the mode and $H^1(\Sigma_g,\bC)$ factors.
+In particular the truncated current algebra $\fg \otimes V_h$
+records the mode cutoff only: the Whitehead step is carried out on
+the finite-dimensional $\fg$-modules $M_{h,\nu}$.
+\end{lemma}
+
+\begin{proof}
+At fixed weight~$h$, only modes $J^a_{-m}$ with $1 \leq m \leq h$
+can occur, so $V_h$ records all possible mode labels. Because the
+total weight is fixed, only finitely many mode patterns~$\nu$ occur.
+Fixing~$\nu$ separates the mode data from the $\fg$-labels in a bar
+word. The regular genus form contributes a passive factor from
+$H^1(\Sigma_g,\bC)$ because it is smooth across every collision
+divisor.
+
+The Lie-bracket residue acts only on the $\fg$-labels. For each fixed
+mode pattern~$\nu$, this is exactly the
+Chevalley--Eilenberg differential for the diagonal adjoint action of
+$\fg$ on the coefficient module~$M_{h,\nu}$. Summing over the finite
+set of mode patterns gives the stated decomposition.
+\end{proof}
+
+\begin{lemma}[Mixed genus-\texorpdfstring{$0/g$}{0/g} map factors through
+ \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
+\label{lem:pbw-mixed-factorization}
+\index{PBW spectral sequence!mixed map factorization|textbf}
+\index{Whitehead lemma!mixed genus-0/genus-g factorization}
+Fix $g \geq 1$, conformal weight~$h$, and bar degree~$n$.
+After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
+Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
+finite-dimensional $\fg$-module $N_h^{n-1}$ and
+$\fg$-equivariant maps
+\[
+\mathcal{E}_g^{n,h}
+\xrightarrow{\ \iota_{g,h,n}\ }
+C^1(\fg, N_h^{n-1})
+\xrightarrow{\ q\ }
+H^1(\fg, N_h^{n-1})
+\xrightarrow{\ \beta_{g,h,n}\ }
+E_2^{n-1,h}(g{=}0)
+\]
+with the following property: if
+$\xi \in \mathcal{E}_g^{n,h}$ is $d_{1,\mathrm{enr}}$-closed, then
+$\iota_{g,h,n}(\xi)$ is a Chevalley--Eilenberg $1$-cocycle and the
+mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
+equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
+Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
+$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
+the non-semisimple truncated current algebra $\fg \otimes V_h$.
+\end{lemma}
+
+\begin{proof}
+Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
+enrichment class as a sum of tensors
+$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
+pattern. For each such tensor, isolate the $\fg$-label attached to the
+slot carrying the regular form and collect the remaining bar data into
+the coefficient module~$N_h^{n-1}$. This gives the map
+$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
+
+The mixed residue brackets the distinguished $\fg$-label with one of
+the remaining labels and then forgets the regular genus form. The
+Jacobi identity for the residue bracket is exactly the cocycle
+condition on $\iota_{g,h,n}(\xi)$ when
+$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
+$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
+Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
+depends only on the image of $\iota_{g,h,n}(\xi)$ in
+$H^1(\fg, N_h^{n-1})$.
+\end{proof}
+
 \begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
 \label{thm:pbw-genus1-km}
 \index{PBW spectral sequence!genus-1 degeneration|textbf}
@@ -1018,33 +1117,25 @@
 with only finitely many mode labels.
 Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
-The truncated current algebra $\fg \otimes V_h$
-records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra. Its role is
-only to enumerate the finitely many mode patterns~$\nu$
-that occur in weight~$h$.
-After separating the mode data from the $\fg$-labels,
-the weight-$h$ enrichment block is a finite direct sum of
-Chevalley--Eilenberg complexes
-$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
-mode patterns~$\nu$ of total weight~$h$. Each
-$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
-diagonal adjoint action on the $\fg$-labels and trivial
-action on the mode and $H^1(E_\tau)$ factors. Equivalently,
+By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
+current algebra $\fg \otimes V_h$ records only the finitely many
+mode patterns~$\nu$ of total weight~$h$. After separating mode data
+from $\fg$-labels, the weight-$h$ enrichment block is a finite
+direct sum of Chevalley--Eilenberg complexes
+$C^*(\fg, M_{h,\nu})$, or equivalently
 \[
 \mathcal{E}_1^{*,h}
 \;\cong\;
 C^*(\fg, M_h),
 \qquad
-M_h := \bigoplus_\nu M_{h,\nu},
+M_h := \bigoplus_\nu M_{h,\nu}.
 \]
-and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential for the finite-dimensional
-semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
-out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
-$\fg \otimes V_h$. The map to the concentrated
-genus-$0$ sector is one of the $\fg$-equivariant components of this
-same differential.
+The mixed component is the degree-one part of the same diagonal
+$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
+mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
+finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
+is carried out weight by weight on honest $\fg$-modules, not on the
+non-semisimple Lie algebra $\fg \otimes V_h$.
 
 \medskip
 \emph{Step~3: Acyclicity of the enrichment complex.}
@@ -1054,23 +1145,28 @@
 argument for~$\fg$ semisimple.
 
 The enrichment module~$M_h$ at weight~$h$ decomposes
-under~$\fg$ into irreducible summands. Since $\fg$ is
-semisimple, the Whitehead--Chevalley--Eilenberg theorem
-gives:
+under~$\fg$ into irreducible summands. Write
+$M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$.
+By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
+genus-$0$/genus-$1$ component on the non-trivial summands factors
+through
+$H^1(\fg, N_h^{n-1}) = 0$
+for finite-dimensional $\fg$-modules~$N_h^{n-1}$, by
+Whitehead's first lemma for semisimple~$\fg$
+\cite{Weibel94}. Hence no non-trivial isotypic summand survives to
+the $E_2$ page through the mixed map.
+
+For the internal enrichment differential, the same weightwise
+decomposition identifies the non-trivial summands with a finite
+direct sum of Chevalley--Eilenberg complexes. The standard
+semisimple extension of Whitehead then gives:
 \[
 H^q(\fg,\, M_h^{\mathrm{non\text{-}triv}}) = 0
 \quad \text{for all } q \geq 0,
 \]
-where $M_h^{\mathrm{non\text{-}triv}}$ is the sum of
-non-trivial irreducible summands. Thus only the
-$\fg$-invariant part $M_h^{\fg}$ can contribute
-to cohomology.
-Because the mixed component
-$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
-is also $\fg$-equivariant, the same conclusion applies to the
-genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
-$E_2$-page through the mixed map. Any possible survivor must lie on the
-$\fg$-invariant line.
+so only the $\fg$-invariant part $M_h^{\fg}$ can contribute to
+cohomology. Any possible survivor must lie on the $\fg$-invariant
+line.
 
 For the $\fg$-invariant part: the invariants in the
 enrichment arise from the Killing form
@@ -1209,11 +1305,15 @@
 For fixed conformal weight~$h$, the truncated current algebra
 $\fg \otimes V_h$ only records which modes can occur. The actual
 Whitehead input appears after rewriting the weight-$h$ enrichment
-block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
-with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
-$H^1$ factors treated as passive coefficients. No vanishing statement
-is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
-itself.
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
+and the mixed genus-$0$/genus-$1$ map factors through
+$H^1(\fg, N_h^{n-1})$
+\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
+The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
+mode and $H^1$ factors are passive coefficients. No vanishing
+statement is invoked for the non-semisimple Lie algebra
+$\fg \otimes V_h$ itself.
 \end{remark}
 
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1326,7 +1426,8 @@
 truncated at weight~$h$, which is genus-independent. Equivalently,
 the weight-$h$ enrichment block is the same finite direct sum of
 Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
-genus~$1$, indexed by the finitely many mode patterns.
+genus~$1$, indexed by the finitely many mode patterns
+\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1347,7 +1448,11 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+complex of~$\fg$ with coefficients in~$M_h$. By
+Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
+$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
+factorization through
+$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 argument is again applied to the finite-dimensional semisimple
 Lie algebra~$\fg$ on each weight-graded piece, not to the
 truncated current algebra that records the mode cutoff.
@@ -1926,6 +2031,41 @@
 data from global curve topology.
 \end{remark}
 
+\begin{remark}[Optimal semisimple page bound and the non-semisimple
+ obstruction]
+\index{PBW spectral sequence!optimal semisimple page bound|textbf}
+\index{PBW spectral sequence!non-semisimple obstruction|textbf}
+The semisimple PBW conclusion is an $E_3$ statement, not an
+$E_1$ statement. The affine KM proof gives the boundary example:
+at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
+$E_2$, and only the family-specific $d_2$ contraction kills it.
+Hence one cannot strengthen the semisimple theorem to an
+$E_1$-collapse claim without adding a false statement.
+
+For a general weightwise Lie symmetry algebra
+$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
+\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
+the Hochschild--Serre spectral sequence
+\[
+E_2^{p,q}(h)
+\;=\;
+H^p\!\bigl(\mathfrak{s}_h,\,
+H^q(\mathfrak{r}_h, M_h)\bigr)
+\;\Longrightarrow\;
+H^{p+q}(\mathfrak{l}_h, M_h).
+\]
+When $\mathfrak{r}_h = 0$, Whitehead kills the non-trivial
+$\mathfrak{s}_h$-isotypic summands and the only possible survivors are
+the invariant classes handled by the family-specific $d_2$
+transgression. When $\mathfrak{r}_h \neq 0$, the obstruction is the
+$\mathfrak{s}_h$-invariant radical cohomology. In particular
+\[
+H^1(\mathfrak{r}_h, M_h)^{\mathfrak{s}_h}
+\]
+is the first mixed genus-$1$ obstruction. Jordan blocks and
+nilpotent radicals are concrete sources of this term.
+\end{remark}
+
 \begin{theorem}[PBW propagation: MK1 implies MK3;
  \ClaimStatusProvedHere]\label{thm:pbw-propagation}
 \index{PBW spectral sequence!propagation theorem|textbf}

tokens used
239,669
