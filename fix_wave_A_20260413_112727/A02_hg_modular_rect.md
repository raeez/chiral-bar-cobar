# A02_hg_modular_rect (372s)

Edited [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1021) only.

- `FIXED` MC1 PBW / Whitehead justification at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1021), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1208), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1326), and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1834). I made the reduction explicit: `\fg \otimes V_h` only records finitely many mode patterns, each weight block is rewritten as a finite direct sum of `C^*(\fg, M_{h,\nu})`, and Whitehead is applied only to the finite-dimensional semisimple Lie algebra `\fg` acting on those modules. I also added a short local remark freezing that point.
- `FIXED` Theorem D routing at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2751). I added an explicit routing remark: the independent anchor is the bar-intrinsic shadow tower, then `thm:genus-universality`, then `thm:family-index`, with no reverse dependence.

Verification: I re-read the touched regions for coherence, did not change any `\label` or `\ref`, and ran a targeted forbidden-pattern grep on the edited blocks with no hits. A full-file grep still shows pre-existing `---` comment/table separators elsewhere in the chapter, outside these edits. I did not run a TeX build.


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
session id: 019d862a-d95c-7b70-8650-c77e192e86ed
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: chapters/theory/higher_genus_modular_koszul.tex

Previous rectification agent timed out. Focus on TWO critical fixes:

1. MC1 PBW: Whitehead lemma applied to truncated current algebra without justification.
   At lines ~1011, 1027, 1294, 1776. FIX: Add explicit reduction: the truncated current
   algebra has the finite-dimensional semisimple g acting on weight-graded pieces;
   Whitehead applies to g, not to the full current algebra. Add a remark.

2. Theorem D circular dependency routing: thm:genus-universality <-> thm:family-index.
   FIX: Add routing remark (AP147) at the Theorem D proof identifying the non-circular
   anchor: shadow tower construction (independent) -> genus universality -> family index.
   Search for 'thm:genus-universality' and add the routing remark nearby.

Read only the relevant sections. Do not try to process the whole file.
mcp startup: no servers

thinking
**Considering tool usage**

I'm thinking about whether to use exec_command in parallel with spawn_agent, but maybe it's not necessary. I could explore using the explorer agent alongside exec_command for more efficiency. It's possible that functions.spawn_agent and functions.exec_command could be simpler options. I also need to check the relevant instructions in the prompt, especially regarding AGENTS and specific files like CLAUDE.md and theorem_registry.md before making any significant edits. Let's outline this plan!
codex
I’m locking scope to [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex) and only the two audit findings you listed. First I’m reading the required repo context plus the exact local theorem/proof regions around the cited lines and `thm:genus-universality` so the edits stay minimal and non-circular.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Whitehead|truncated current algebra|thm:genus-universality|thm:family-index|Theorem D|family index|genus universality" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 51ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
896:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
920:by Whitehead; the Killing-form invariant
931:enrichment factorization, Whitehead acyclicity, and the
1021:The truncated current algebra $\fg \otimes V_h$
1022:records which modes can occur at weight~$h$; Whitehead is
1053:semisimple, the Whitehead--Chevalley--Eilenberg theorem
1108:We exhibit the interplay of Whitehead vanishing and
1142: Whitehead's theorem gives
1159:three by the bracket isomorphism, five by Whitehead, one by the
1193:summands killed by Whitehead, invariant summands passed to
1199:decomposition under~$\fg$ and the Whitehead vanishing
1237:Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
1263:three-step mechanism (PBW decomposition, Whitehead
1313:\emph{Step~2: Whitehead acyclicity of the enrichment.}
1334:Whitehead--Chevalley--Eilenberg theorem gives
1404:by the genus-independent Whitehead + Killing contraction
1420:and Whitehead + Killing contraction applies without
1812:By the Whitehead--Chevalley--Eilenberg vanishing theorem,
1834:$\fg$-non-trivial summand (killed by Whitehead at~$E_2$)
codex
I’m using the `beilinson-rectify` skill for a tightly scoped proof-surface repair. Next I’m reading only the Whitehead/PBW block and the Theorem D routing block so the patch lands exactly where the audit findings fire.
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

collab spawn_agent(call_hi8cODkFHoYp0JksytS8OXfQ, prompt="Read only the relevant sections of chapters/theory/higher_genus_modular_koszul.tex for two audit fixes. Identify the exa…")
spawn_agent(call_hi8cODkFHoYp0JksytS8OXfQ, prompt="Read only the relevant sections of chapters/theory/higher_genus_modular_koszul.tex for two audit fixes. Identify the exa…") pending init:
  agent: 019d862b-7c8a-7370-a0d9-9ef2fae19bb8
mcp startup: no servers
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Whitehead" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
896:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
920:by Whitehead; the Killing-form invariant
931:enrichment factorization, Whitehead acyclicity, and the
1022:records which modes can occur at weight~$h$; Whitehead is
1053:semisimple, the Whitehead--Chevalley--Eilenberg theorem
1108:We exhibit the interplay of Whitehead vanishing and
1142: Whitehead's theorem gives
1159:three by the bracket isomorphism, five by Whitehead, one by the
1193:summands killed by Whitehead, invariant summands passed to
1199:decomposition under~$\fg$ and the Whitehead vanishing
1237:Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
1263:three-step mechanism (PBW decomposition, Whitehead
1313:\emph{Step~2: Whitehead acyclicity of the enrichment.}
1334:Whitehead--Chevalley--Eilenberg theorem gives
1404:by the genus-independent Whitehead + Killing contraction
1420:and Whitehead + Killing contraction applies without
1812:By the Whitehead--Chevalley--Eilenberg vanishing theorem,
1834:$\fg$-non-trivial summand (killed by Whitehead at~$E_2$)
1881:Whitehead vanishing argument of
1891:KM uses the independent Whitehead--Casimir--Killing mechanism
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:genus-universality" -n chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2436: (Theorem~\ref{thm:genus-universality}).
2543:(Theorem~\ref{thm:genus-universality}).
2729:Theorem~\ref{thm:genus-universality} identifies that trace with
2732:Part~(i) is Theorem~\ref{thm:genus-universality} for
2740:Theorem~\ref{thm:genus-universality}(ii).
2804:Theorem~\ref{thm:genus-universality}; the second arrow is the
2811:Theorem~\ref{thm:genus-universality}); generating function via
3184:Theorem~\ref{thm:genus-universality}. The GUE free energy
3345:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3768:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3820:Theorem~\ref{thm:genus-universality}(ii)).
5386:(Theorem~\ref{thm:genus-universality},
7787:(Theorem~\ref{thm:genus-universality}).
7943:Theorem~\ref{thm:genus-universality} identifies the scalar trace
8091:Theorem~\ref{thm:genus-universality} identifies
8515:by Theorem~\ref{thm:genus-universality}\textup{(iii)}.
9595:Theorem~\textup{\ref{thm:genus-universality}}, then the full
9650:By Theorem~\ref{thm:genus-universality},
11703:theorem (Theorem~\ref{thm:genus-universality}).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~D" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2179:\item Theorem~D \textup{(}modular characteristic
2790:\begin{remark}[Proof routing for Theorem~D;
2807:Theorem~D and is not an input to its proof.
3935: \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
3989:\item \emph{Theorem~D} (modular characteristic~$\kappa$):
5143:of Theorem~D$_{\mathrm{scal}}$
9486:Theorem~D establishes that $\kappa$ exists as a universal
9506:Properties~(i)--(iv) of Theorem~D are shadows of the family index
9749:Theorem~D$_{\mathrm{scal}}$
9756:Theorem~D$_\Delta$
9797:Theorem~D extracts the scalar level~$\kappa(\cA)$, while the
11893: \quad(the modular characteristic, Theorem~D);
12148: \quad(the modular characteristic, Theorem~D);
13923:Theorem~D
14484:Theorem~D extracts the scalar $\kappa = \operatorname{av}(r(z))$
14604:modular characteristic (Theorem~D).
15023: Theorem~D\textup{)}.
15044:curvature $\kappa(\cA)$ by definition (Theorem~D).
25304:The shadow obstruction tower free energy (Theorem~D) is the
26204:$\int_{\overline{\cM}_g}\lambda_g\cdot\kappa$ by Theorem~D.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '980,1060p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathcal{E}^{p,q}_1$ is the enrichment from
$H^1(E_\tau)$.

\medskip
\emph{Step~2: The $d_1^{\mathrm{PBW}}$ differential on
the enrichment.}

The next PBW differential $d_1^{\mathrm{PBW}}$ comes
from the $\fg$-bracket, the $(0)$-product component
of the OPE, which lowers PBW degree by~$1$. It acts
on the enrichment $\mathcal{E}^{*,*}_1$ by extracting
the Lie bracket residue. It splits according to whether the
$H^1(E_\tau)$ factor survives the residue or is absorbed into a
concentrated genus-$0$ class:
\[
d_1^{\mathrm{PBW}}
=
d_{1,\mathrm{mix}} \oplus d_{1,\mathrm{enr}}\colon
\mathcal{E}_1^{n, h}
\;\longrightarrow\; E_1^{n-1,h}(g{=}0)
thinking
**Checking context for reading**

I'm planning to read specific line ranges from a document, particularly around 960-1360, 1750-1845, and 2700-2820. I might also check Theorem D proof lines. To do this efficiently, I'm considering using the `sed` command. This should help me extract the sections I need for a closer look without getting lost in too much text. Let's see how that works out!
exec
/bin/zsh -lc "sed -n '980,1360p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1740,1865p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2680,2825p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The enrichment factorization~\eqref{eq:enrichment-factorization}
holds for any chiral algebra defined by local OPE relations:
at each conformal weight~$h$,
\[
\mathcal{E}_g^{*,h}
\;\cong\; M_h \otimes_{\bC} H^{1,0}(\Sigma_g),
\]
because the $H^{1,0}(\Sigma_g)$ forms are smooth across
collision divisors and enter as passive multiplicative factors.

The $d_2^{\mathrm{PBW}}$ differential on the enrichment is
induced by the $(1)$-products of the generators. A generator
of conformal weight~$s$ has $(1)$-product shifting conformal
weight by $s - 2$. By hypothesis~(b), the stress tensor~$T$
is the \emph{unique} generator with $s = 2$, so it is the
unique generator whose $(1)$-product preserves conformal weight.
Every other generator has $s \neq 2$ and therefore shifts the
weight-grading: its contribution appears on a page of the PBW
spectral sequence different from the one where the
 succeeded in 52ms:
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
 \;=\; \kappa(\cA) \cdot
 \left(\frac{x/2}{\sin(x/2)} - 1\right),
 \end{equation}
 recovering the $\hat{A}$-genus as topological generating function
 \textup{(UNIFORM-WEIGHT)}.
 At genus~$1$ this holds unconditionally for all families;
 at genus $g \geq 2$ with multi-weight algebras, the scalar
 formula fails and a cross-channel correction
 succeeded in 52ms:
$\mathcal{E}^{p,q}_1$ is the enrichment from
$H^1(E_\tau)$.

\medskip
\emph{Step~2: The $d_1^{\mathrm{PBW}}$ differential on
the enrichment.}

The next PBW differential $d_1^{\mathrm{PBW}}$ comes
from the $\fg$-bracket, the $(0)$-product component
of the OPE, which lowers PBW degree by~$1$. It acts
on the enrichment $\mathcal{E}^{*,*}_1$ by extracting
the Lie bracket residue. It splits according to whether the
$H^1(E_\tau)$ factor survives the residue or is absorbed into a
concentrated genus-$0$ class:
\[
d_1^{\mathrm{PBW}}
=
d_{1,\mathrm{mix}} \oplus d_{1,\mathrm{enr}}\colon
\mathcal{E}_1^{n, h}
\;\longrightarrow\; E_1^{n-1,h}(g{=}0)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1060,1135p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
non-trivial irreducible summands. Thus only the
$\fg$-invariant part $M_h^{\fg}$ can contribute
to cohomology.
Because the mixed component
$d_{1,\mathrm{mix}}\colon \mathcal{E}_1^{*,h} \to E_1^{*,h}(g{=}0)$
is also $\fg$-equivariant, the same conclusion applies to the
genus-$0$ target: no non-trivial $\fg$-isotypic summand survives the
$E_2$-page through the mixed map. Any possible survivor must lie on the
$\fg$-invariant line.

For the $\fg$-invariant part: the invariants in the
enrichment arise from the Killing form
$\kappa^{ab} \in (\fg \otimes \fg)^{\fg}$ paired
with $H^1(E_\tau)$ data. These invariant enrichment classes
are exact under $d_2^{\mathrm{PBW}}$
(the $(1)$-product differential, which lowers PBW
degree by~$2$ and involves the level~$k$): the
$d_2^{\mathrm{PBW}}$ image of the bar-degree-$(n{+}1)$
invariant at weight~$h$ covers the bar-degree-$n$
invariant, provided $k \neq 0$ (non-degeneracy of the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1260,1335p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The genus-$1$ proof
(Theorem~\ref{thm:pbw-genus1-km}) establishes a
three-step mechanism (PBW decomposition, Whitehead
acyclicity, Killing-form contraction) that is
genus-independent. We verify that each step
extends without modification to $g \geq 2$.

\medskip
\emph{Step~1: $E_1$ decomposition at genus~$g$.}

At genus~$g$, the chain groups of the bar complex use
forms on $\overline{C}_n(\Sigma_g)$, the
Fulton--MacPherson compactification of configuration
space on a smooth projective curve~$\Sigma_g$ of
genus~$g$. The curve contributes regular forms
from $H^{1,0}(\Sigma_g) \cong \bC^g$ (holomorphic
$1$-forms). These are regular at every collision
divisor~$D_{ij}$: they arise from the global geometry
of~$\Sigma_g$, not from OPE poles.

thinking
**Searching for theorem definitions**

I'm looking into theorem definitions related to Theorem D and considering aspects like genus-universality and family-index. I want to find more precise local lines and relevant context around these concepts. I'll make sure to explore various sources to gather accurate information, ensuring my understanding is solid and comprehensive. It's important to get the details right, as these theorems can be quite intricate! Let's see what I can find.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1335,1415p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$H^q(\fg, N) = 0$ for all $q \geq 0$ and any
finite-dimensional $\fg$-module~$N$ with no trivial
summand. Decompose $M_h = M_h^{\fg} \oplus
M_h^{\mathrm{non\text{-}triv}}$ under~$\fg$. Then:
\[
H^*\!\bigl(C^*(\fg, M_h^{\mathrm{non\text{-}triv}})\bigr)
\;\otimes\; H^{1,0}(\Sigma_g) \;=\; 0.
\]
This vanishing is \emph{independent of~$g$}: the
$H^{1,0}(\Sigma_g)$ tensor factor is a
finite-dimensional vector space (of dimension~$g$),
and tensoring a zero module with any vector space
gives zero. Only the $\fg$-invariant
summand~$M_h^{\fg}$ can contribute cohomology, exactly
as at genus~$1$.

\medskip
\emph{Step~3: Killing-form contraction kills
invariants.}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1740,1820p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proof}
The enrichment factorization~\eqref{eq:enrichment-factorization}
holds for any chiral algebra defined by local OPE relations:
at each conformal weight~$h$,
\[
\mathcal{E}_g^{*,h}
\;\cong\; M_h \otimes_{\bC} H^{1,0}(\Sigma_g),
\]
because the $H^{1,0}(\Sigma_g)$ forms are smooth across
collision divisors and enter as passive multiplicative factors.

The $d_2^{\mathrm{PBW}}$ differential on the enrichment is
induced by the $(1)$-products of the generators. A generator
of conformal weight~$s$ has $(1)$-product shifting conformal
weight by $s - 2$. By hypothesis~(b), the stress tensor~$T$
is the \emph{unique} generator with $s = 2$, so it is the
unique generator whose $(1)$-product preserves conformal weight.
Every other generator has $s \neq 2$ and therefore shifts the
weight-grading: its contribution appears on a page of the PBW
spectral sequence different from the one where the
codex
The local surfaces are clear now. The PBW blocks already partly isolate `\fg` from the truncated current algebra, but they do not state that reduction uniformly where the audit flagged it; I’m pulling the exact theorem/proof snippets around those line anchors and the nearby routing prose before editing.
exec
/bin/zsh -lc "sed -n '880,1075p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1280,1355p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2708,2758p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1768,1845p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 succeeded in 51ms:

Since $d_0^{\mathrm{PBW}}$ acts by Poincar\'{e} residue at
collision divisors, and the Poincar\'{e} residue of a
regular form is zero, the $H^{1,0}(\Sigma_g)$-enrichment
cochains are $d_0^{\mathrm{PBW}}$-closed. They are not
$d_0^{\mathrm{PBW}}$-exact by the same degree argument
as in genus~$1$. Thus
\begin{equation}\label{eq:e1-decomposition-genusg}
E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0)
 \;\oplus\; \mathcal{E}^{p,q}_g
\end{equation}
where $\mathcal{E}^{p,q}_g$ is the enrichment from
$H^{1,0}(\Sigma_g)$.

The enrichment
\emph{factors}: at each conformal weight~$h$,
\begin{equation}\label{eq:enrichment-factorization}
\mathcal{E}_g^{*,h}
\;\cong\; M_h \otimes_{\bC} H^{1,0}(\Sigma_g)
\end{equation}
 succeeded in 52ms:
by~$T_{(1)} = L_0$:
\[
d_2^{\mathrm{PBW}}\big|_{\mathcal{E}_g^{*,h}}
\;=\;
h \cdot \mathrm{id}_{M_h}
\otimes
\mathrm{id}_{H^{1,0}(\Sigma_g)}.
\]
Since $h \geq h_{\min} > 0$, this map is an isomorphism,
killing the entire genus-$g$ enrichment on the $E_3$ page.
The weight-lowering contributions from generators with $s < 2$
now act on zero (the enrichment is already dead) and cannot
create new classes.

The antiholomorphic factor $H^{0,1}(\Sigma_g)$ is handled
identically. Bounded-below convergence
\textup{(}\ref{item:pbw-bounded} of
Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}
then shows that once later differentials and extension classes are
ruled out by family-specific input, the genus-$g$ and genus-$0$
 succeeded in 52ms:
 K_\fg \cdot \varrho(\fg)$
 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
 $m_1, \ldots, m_r$ the exponents;
 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
\item \emph{Additivity.}
 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
 Combined with~(iii), the vanishing
 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
 $\cA \otimes \cA^!_{\mathrm{ghost}}$ is the algebraic
 form of anomaly cancellation.
\end{enumerate}
\end{theorem}

\begin{proof}
The dependency route is one-way: the bar-intrinsic shadow tower of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1820,1925p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\emph{Invariant summands.}
The surviving $\fg$-invariant enrichment classes live in
$M_h^{\fg} \otimes H^{1,0}(\Sigma_g)$. On these, the
$d_2^{\mathrm{PBW}}$ differential acts through $T_{(1)} = L_0$
as proved above: the conformal vector is the unique weight-$2$
generator, and its $(1)$-product gives
$L_0|_{M_h^{\fg}} = h \cdot \mathrm{id}$. Since
$h \geq h_{\min} > 0$, this is an isomorphism, and the
$\fg$-invariant enrichment is killed at the $E_3$ page.

\emph{No later differentials or extension ambiguity.}
The two mechanisms are complementary and exhaustive:
every enrichment class belongs to either the
$\fg$-non-trivial summand (killed by Whitehead at~$E_2$)
or the $\fg$-invariant summand (killed by $L_0$ invertibility
at~$E_3$). No residual classes survive to later pages,
and there are no extension ambiguities because the enrichment
is zero on the $E_3$ page. By bounded-below convergence
\textup{(}\ref{item:pbw-bounded} of
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:family-index" -n chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2730:$\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
2806:series. In particular, Theorem~\ref{thm:family-index} is downstream of
2816:to $\kappa\cdot(\hat{A}(ix)-1)$ (Theorem~\ref{thm:family-index}).
4407: \textup{(}Theorem~\textup{\ref{thm:family-index}}\textup{)}.
4457:(Theorem~\ref{thm:family-index}); the $\hat{A}$-genus appears
9507:theorem (Theorem~\ref{thm:family-index}).
13934:(Theorem~\ref{thm:family-index}).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2700,2835p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\delta F_g^{\mathrm{cross}}$ is required
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
\item \emph{Duality.}
 Under Koszul duality, $\kappa$ satisfies a duality constraint:
 $\kappa(\cA) + \kappa(\cA^!) = 0$ for affine Kac--Moody and
 free-field algebras. For the principal $\mathcal{W}$-algebra
 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
 K_\fg \cdot \varrho(\fg)$
 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
 $m_1, \ldots, m_r$ the exponents;
 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
\item \emph{Additivity.}
 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
 Combined with~(iii), the vanishing
Plan update
Scoped to one file and two audit findings. I have the exact local proof blocks and am about to make the smallest edits that tighten the Whitehead reduction and the Theorem D dependency routing without changing theorem statements.
  ✓ Inspect the Whitehead/PBW blocks and Theorem D routing blocks in the target file plus required repo context
  → Patch the Whitehead/PBW passages with an explicit reduction to finite-dimensional fg-modules and add a local clarifying remark
  • Patch the Theorem D proof with a one-way routing remark from shadow tower to genus universality to family index
  • Re-read touched regions and grep the modified file for forbidden or stale patterns
collab wait(call_yrF5tlGOIq1B7jKVJMSsg9rk)
  receivers: 019d862b-7c8a-7370-a0d9-9ef2fae19bb8
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3960,4045p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{proof}
Each projection is the restriction of
$\Theta_\cA = D_\cA - \dzero$ to the relevant bigraded
component of $\cA^{\mathrm{sh}} =
H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$
(Definition~\ref{def:shadow-algebra}):
(i) is the $(r{=}2, g{=}\bullet)$ scalar trace,
(ii) is the $(r{=}2, g{=}\bullet)$ matrix-valued component,
(iii) is $(r{=}4, g{=}0)$,
(iv) is $(r, g{=}\bullet)$ in general.
\end{proof}

\begin{remark}[Non-circular logical foundation]
\label{rem:non-circular-logical-chain}
\index{logical foundation!non-circular chain}
The bar-intrinsic construction partitions the five main
theorems into two tiers by logical prerequisites.

\smallskip\noindent
\emph{Tier~1: unconditional consequences of~$D_\cA^2 = 0$.}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "modular characteristic" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
49:the modular characteristic $\kappa(\cA)$ at degree~$2$,
2179:\item Theorem~D \textup{(}modular characteristic
2425:\begin{definition}[Scalar modular characteristic package]
2428:\index{modular characteristic package!scalar|textbf}
2431:\emph{scalar modular characteristic package} of~$\cA$ consists of:
2455:\begin{definition}[Full modular characteristic package]
2457:\index{modular characteristic package!full|textbf}
2465:\emph{full modular characteristic package} is the quintuple
2484: \emph{scalar modular characteristic}
2623:\begin{remark}[The modular characteristic hierarchy]
2626:\index{modular characteristic!hierarchy|textbf}
2661:\index{modular characteristic theorem|textbf}
2761:\index{modular characteristic theorem!as integrability condition}%
2793:\index{modular characteristic theorem!model presentation}
3489:$\Theta_\cA$: the modular characteristic $\kappa$ at degree~$2$,
3989:\item \emph{Theorem~D} (modular characteristic~$\kappa$):
4558:(level equals modular characteristic). For rank-$d$ lattice VOAs,
4602:\index{modular characteristic!W3 channel decomposition@$\cW_3$ channel decomposition}
4604:$W$ \textup{(}weight~$3$\textup{)}, the modular characteristic
8121:The non-scalar modular characteristic package
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2160,2245p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\textbf{Tier~0} \textup{(topological input:
$D_\cA^2 = 0$)}.
\begin{enumerate}[label=\textup{(0.\arabic*)}]
\item The universal MC element
 $\Theta_\cA := D_\cA - \dzero
 \in \MC(\gAmod)$ exists at all genera
 \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
\item The shadow obstruction tower
 $\Theta_\cA^{\leq r}$ exists at all finite degrees,
 with $\Theta_\cA = \varprojlim_r
 \Theta_\cA^{\leq r}$
 \textup{(Theorem~\ref{thm:recursive-existence})}.
\item The shadow algebra
 $\cA^{\mathrm{sh}} =
 H_\bullet(\Defcyc^{\mathrm{mod}}(\cA))$ carries
 a graded Lie bracket with
 projections $\kappa$, $\Delta$,
 $\mathfrak{C}$, $\mathfrak{Q}$
 \textup{(Corollary~\ref{cor:shadow-extraction})}.
\item Theorem~D \textup{(}modular characteristic
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\begin{theorem}\\[Theorem~D\" -n chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\begin{theorem}\[Theorem~D)
              ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\begin\\{theorem\\}\\[Theorem~D\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"Theorem~\\\\textup\\{D\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "modular characteristic" -n chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
49:the modular characteristic $\kappa(\cA)$ at degree~$2$,
2179:\item Theorem~D \textup{(}modular characteristic
2425:\begin{definition}[Scalar modular characteristic package]
2428:\index{modular characteristic package!scalar|textbf}
2431:\emph{scalar modular characteristic package} of~$\cA$ consists of:
2455:\begin{definition}[Full modular characteristic package]
2457:\index{modular characteristic package!full|textbf}
2465:\emph{full modular characteristic package} is the quintuple
2484: \emph{scalar modular characteristic}
2623:\begin{remark}[The modular characteristic hierarchy]
2626:\index{modular characteristic!hierarchy|textbf}
2661:\index{modular characteristic theorem|textbf}
2761:\index{modular characteristic theorem!as integrability condition}%
2793:\index{modular characteristic theorem!model presentation}
3489:$\Theta_\cA$: the modular characteristic $\kappa$ at degree~$2$,
3989:\item \emph{Theorem~D} (modular characteristic~$\kappa$):
4558:(level equals modular characteristic). For rank-$d$ lattice VOAs,
4602:\index{modular characteristic!W3 channel decomposition@$\cW_3$ channel decomposition}
4604:$W$ \textup{(}weight~$3$\textup{)}, the modular characteristic
8121:The non-scalar modular characteristic package
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2405,2495p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
degenerates at~$E_2$.
\end{lemma}

\begin{proof}
The PBW filtration is a filtration by chiral algebras, and the
Koszulness hypothesis ensures that the associated graded is a
Koszul complex in the classical sense. The $d_r$ differential
for $r \geq 2$ maps between PBW-graded components separated
by~$r$ steps, and the Koszul concentration (all bar cohomology
is in bar-degree~$0$ on the associated graded) forces these maps
to have zero source or zero target.

On each geometric fiber (a fixed smooth or stable curve), the
collision differential is genus-$0$ type (with $d_0^2 = 0$), and
the genus-$g$ quantum corrections live in higher Leray degrees,
contributing only to $d_r$ for $r \geq 2$. Since $E_2$ is
already concentrated on the diagonal by Koszul concentration,
these higher differentials vanish.
\end{proof}

wait(call_yrF5tlGOIq1B7jKVJMSsg9rk) timed out:

thinking
**Inspecting code issues**

I noticed the process timed out, so I can either ignore it or keep going. Maybe the explorer is still running; I'll look at that later. For now, I can continue manually. I should check the exact line numbers, possibly using `nl`. I might also utilize `rg` or `nl -ba` to identify areas that need patching. Let’s focus on getting those line numbers for local context.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:genus-universality\" -n chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "genus-universality" -g"*"' in /Users/raeez/chiral-bar-cobarcodex
I’ve isolated the exact sentences that need surgical changes. The Whitehead fix only needs a couple of local clarifications plus one remark; the theorem-routing fix is a short AP147-style sentence at the Theorem D proof surface, not a theorem rewrite.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1010,1068p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1298,1350p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1802,1842p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2722,2750p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1010	$d_{1,\mathrm{mix}}$ and $d_{1,\mathrm{enr}}$ are
  1011	$\fg$-equivariant for the diagonal adjoint action on the
  1012	$\fg$-labels $a_i$: the mode labels and the $H^1(E_\tau)$ factor are
  1013	spectators.
  1014	
  1015	In each conformal
  1016	weight~$h$, the enrichment
  1017	$\mathcal{E}_1^{*,h}$ is a finite-dimensional complex
  1018	with only finitely many mode labels.
  1019	Write
  1020	$V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
  1021	The truncated current algebra $\fg \otimes V_h$
  1022	records which modes can occur at weight~$h$; Whitehead is
  1023	not applied to this non-semisimple Lie algebra.
  1024	After separating the mode data from the $\fg$-labels,
  1025	the weight-$h$ enrichment block is a finite direct sum of
  1026	Chevalley--Eilenberg complexes
  1027	$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
  1028	mode patterns~$\nu$ of total weight~$h$. Each
  1029	$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
 succeeded in 51ms:
  1298	\;\cong\; M_h \otimes_{\bC} H^{1,0}(\Sigma_g)
  1299	\end{equation}
  1300	where $M_h$ is the \emph{same} finite-dimensional
  1301	$\fg$-module as at genus~$1$.
  1302	This factorization holds because the
  1303	$H^{1,0}(\Sigma_g)$ forms enter as global
  1304	multiplicative factors that do not interact with the
  1305	OPE data: the collision divisors (where OPE poles live)
  1306	are codimension-$1$ loci in $\overline{C}_n(\Sigma_g)$,
  1307	and the regular forms from $H^{1,0}(\Sigma_g)$ are
  1308	smooth across these divisors. The module~$M_h$ is
  1309	determined solely by the OPE structure of~$\widehat{\fg}_k$
  1310	truncated at weight~$h$, which is genus-independent.
  1311	
  1312	\medskip
  1313	\emph{Step~2: Whitehead acyclicity of the enrichment.}
  1314	
  1315	The $d_1^{\mathrm{PBW}}$ differential (Lie bracket residue)
  1316	acts on the enrichment through the $\fg$-module factor~$M_h$,
  1317	leaving the $H^{1,0}(\Sigma_g)$ factor unchanged:
 succeeded in 50ms:
  1802	(Lie bracket residue from the $(0)$-products of the generators)
  1803	acts on the enrichment through the $\fg$-module
  1804	factor~$M_h^{\mathrm{non\text{-}triv}}$, leaving the
  1805	$H^{1,0}(\Sigma_g)$ factor unchanged. The enrichment complex
  1806	at weight~$h$ restricted to the non-trivial summand is
  1807	\[
  1808	\bigl(C^*(\fg,\, M_h^{\mathrm{non\text{-}triv}}),\, d_{\mathrm{CE}}\bigr)
  1809	\;\otimes_{\bC}\;
  1810	H^{1,0}(\Sigma_g).
  1811	\]
  1812	By the Whitehead--Chevalley--Eilenberg vanishing theorem,
  1813	$H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
  1814	finite-dimensional $\fg$-module~$N$ with no trivial summand,
  1815	since $\fg$ is semisimple. Therefore the non-trivial
  1816	enrichment is acyclic already at the $E_2$ page:
  1817	\[
  1818	E_2^{*,h}(g)_{\mathrm{enr,\, non\text{-}triv}} = 0.
  1819	\]
  1820	
  1821	\emph{Invariant summands.}
 succeeded in 51ms:
  2722	 form of anomaly cancellation.
  2723	\end{enumerate}
  2724	\end{theorem}
  2725	
  2726	\begin{proof}
  2727	The dependency route is one-way: the bar-intrinsic shadow tower of
  2728	Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
  2729	Theorem~\ref{thm:genus-universality} identifies that trace with
  2730	$\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
  2731	subsequent GRR repackaging of the resulting genus series.
  2732	Part~(i) is Theorem~\ref{thm:genus-universality} for
  2733	uniform-weight algebras. For multi-generator algebras
  2734	($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
  2735	is unconditional; the higher-genus extension is conditional on the
  2736	strong scalar ansatz of
  2737	Theorem~\ref{thm:multi-generator-universality}.
  2738	Part~(ii) is Theorem~\ref{thm:universal-generating-function}.
  2739	Part~(iii) is the duality clause of
  2740	Theorem~\ref{thm:genus-universality}(ii).
  2741	Part~(iv) is Theorem~\ref{thm:anomaly-koszul}.
 succeeded in 3.74s:
.claude/worktrees/agent-a074cd40/compute/audit/scalar_saturation_assessment.md:48:| Uniform-weight algebras, all genera | YES | YES | thm:genus-universality |
.claude/worktrees/agent-a074cd40/compute/audit/linear_read_notes.md:311:| F72 | — | **CRITICAL** | Beilinson | `higher_genus_foundations.tex` Theorem `thm:genus-universality` still stated the Faber--Pandharipande free-energy formula without the multi-weight fence, even though its own proof and `rem:multi-generator-obs` show the higher-genus multi-weight factorization is open. Narrowed item (iii) to the uniform-weight lane and genus~1 unconditionality. | **FIXED** |
.claude/worktrees/agent-a074cd40/compute/audit/linear_read_notes.md:563:| F334 | 2026-04-02 00:22:00 SAST | **MODERATE** | Beilinson | The next pass found a theorem-surface wording leak in `higher_genus_foundations.tex`. `prop:grr-bridge` was still titled and stated on the broad “scalar lane,” even though its proof runs through the repaired all-genera uniform-weight genus-universality theorem together with a separate unconditional genus-$1$ fallback. I narrowed the proposition title and statement to the proved uniform-weight scalar lane and aligned the nearby family-index remark to the same scope. | **FIXED** |
.claude/worktrees/agent-a074cd40/compute/audit/linear_read_notes.md:564:| F335 | 2026-04-02 00:39:00 SAST | **SERIOUS** | Beilinson | The next pass found a theorem-chain overclaim in `higher_genus_modular_koszul.tex`. `thm:conformal-block-reconstruction` was still stated for arbitrary modular Koszul algebras even though parts (i)--(ii) of its proof import the repaired all-genera scalar formula from the uniform-weight genus-universality theorem. I narrowed the theorem and its immediate export remark so the genus-$g$ free-energy and $\hat A$ reconstruction package now live only on the proved uniform-weight scalar lane, with the genus-$1$ scalar specialization kept separate for arbitrary modular Koszul algebras. | **FIXED** |
.claude/worktrees/agent-a7a899b6/compute/lib/rectangular_w_algebra_engine.py:48:  rho is proved ONLY for principal W-algebras (Theorem genus-universality).
.claude/worktrees/agent-a7a899b6/compute/lib/rectangular_w_algebra_engine.py:59:    thm:genus-universality (higher_genus_foundations.tex)
.claude/worktrees/agent-a7a899b6/compute/lib/rectangular_w_algebra_engine.py:361:    principal W-algebras (Theorem genus-universality).
.claude/worktrees/agent-a074cd40/compute/audit/multi_generator_universality_2026_04_05.md:16:- Uniform-weight algebras: PROVED at all genera (thm:genus-universality)
.claude/worktrees/agent-a074cd40/compute/audit/multi_generator_universality_2026_04_05.md:200:- `chapters/theory/higher_genus_foundations.tex` (op:multi-generator-universality at line 5122, thm:genus-universality at line 4991, prop:multi-generator-obstruction at line 5248)
.claude/worktrees/agent-ab4d244b/compute/audit/scalar_saturation_assessment.md:48:| Uniform-weight algebras, all genera | YES | YES | thm:genus-universality |
.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/compute/lib/rectangular_w_algebra_engine.py:48:  rho is proved ONLY for principal W-algebras (Theorem genus-universality).
.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/compute/lib/rectangular_w_algebra_engine.py:59:    thm:genus-universality (higher_genus_foundations.tex)
.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/compute/lib/rectangular_w_algebra_engine.py:361:    principal W-algebras (Theorem genus-universality).
.claude/worktrees/agent-ab4d244b/compute/audit/linear_read_notes.md:311:| F72 | — | **CRITICAL** | Beilinson | `higher_genus_foundations.tex` Theorem `thm:genus-universality` still stated the Faber--Pandharipande free-energy formula without the multi-weight fence, even though its own proof and `rem:multi-generator-obs` show the higher-genus multi-weight factorization is open. Narrowed item (iii) to the uniform-weight lane and genus~1 unconditionality. | **FIXED** |
.claude/worktrees/agent-ab4d244b/compute/audit/linear_read_notes.md:563:| F334 | 2026-04-02 00:22:00 SAST | **MODERATE** | Beilinson | The next pass found a theorem-surface wording leak in `higher_genus_foundations.tex`. `prop:grr-bridge` was still titled and stated on the broad “scalar lane,” even though its proof runs through the repaired all-genera uniform-weight genus-universality theorem together with a separate unconditional genus-$1$ fallback. I narrowed the proposition title and statement to the proved uniform-weight scalar lane and aligned the nearby family-index remark to the same scope. | **FIXED** |
.claude/worktrees/agent-ab4d244b/compute/audit/linear_read_notes.md:564:| F335 | 2026-04-02 00:39:00 SAST | **SERIOUS** | Beilinson | The next pass found a theorem-chain overclaim in `higher_genus_modular_koszul.tex`. `thm:conformal-block-reconstruction` was still stated for arbitrary modular Koszul algebras even though parts (i)--(ii) of its proof import the repaired all-genera scalar formula from the uniform-weight genus-universality theorem. I narrowed the theorem and its immediate export remark so the genus-$g$ free-energy and $\hat A$ reconstruction package now live only on the proved uniform-weight scalar lane, with the genus-$1$ scalar specialization kept separate for arbitrary modular Koszul algebras. | **FIXED** |
.claude/worktrees/agent-ab4d244b/compute/audit/multi_generator_universality_2026_04_05.md:16:- Uniform-weight algebras: PROVED at all genera (thm:genus-universality)
.claude/worktrees/agent-ab4d244b/compute/audit/multi_generator_universality_2026_04_05.md:200:- `chapters/theory/higher_genus_foundations.tex` (op:multi-generator-universality at line 5122, thm:genus-universality at line 4991, prop:multi-generator-obstruction at line 5248)
.claude/worktrees/agent-a277b925/compute/lib/rectangular_w_algebra_engine.py:48:  rho is proved ONLY for principal W-algebras (Theorem genus-universality).
.claude/worktrees/agent-a277b925/compute/lib/rectangular_w_algebra_engine.py:59:    thm:genus-universality (higher_genus_foundations.tex)
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "1011" -n .' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Total output lines: 59

./wave2_audit_20260413_001942/S03_koszul_to_shadow.md:697:chapters/theory/chiral_koszul_pairs.tex:1011:E_1^{p,q} = H^{p+q}(\barBgeom^p(\operatorname{Sym}^{\mathrm{ch}}(V)))
./wave2_audit_20260413_001942/C17_concordance.md:1069: 11011	
./wave2_audit_20260413_001942/D13_genus_1_vs_all.md:582:'/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex':[44,260,896,1011],
./wave2_audit_20260413_001942/C10_en_koszul_duality.md:531:  1011	$\mathrm{GC}_2$.
./wave2_audit_20260413_001942/C10_en_koszul_duality.md:1155:chapters/examples/deformation_quantization.tex:1011:Arnold relation on $\overline{C}_n(\bC)$ \\
./wave2_audit_20260413_001942/B04_thm_D_bridge.md:1443:  1011	$\ell_k^{(g),\mathrm{tr}}$ also vanish for $k \geq 3$.
./wave2_audit_20260413_001942/U13_dead_labels.md:1363:- [MEDIUM] chapters/connections/arithmetic_shadows.tex:227 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:lattice-specificity` (227), `prop:divisor-sum-decomposition` (311), `prop:sewing-trace-formula` (349), `thm:narain-universality` (444), `rem:discrimination-hierarchy` (756), `prop:shadow-arithmetic-factorization` (779), `rem:genus2-theta-niemeier` (832), `rem:mc-complete-niemeier` (882), `rem:shadow-spectral-CG` (984), `prop:hecke-all-orders` (1021), `prop:period-shadow-dictionary` (1072), `rem:depth-non-unimodular` (1137), `comp:period-shadow-vz` (1155), `comp:period-shadow-ve8` (1173), `comp:period-shadow-leech` (1195), `comp:period-shadow-rank24-comparison` (1247), `comp:period-shadow-rank2` (1266), `thm:spectral-decomposition-principle` (1290), `rem:homotopy-becomes-arithmetic` (1330), `def:cusp-growth-rate` (1366), `prop:growth-rate-dictionary` (1377), `thm:bg-vir-coincidence` (1403), `cor:rigorous-infinite-depth` (1546), `prop:bg-primary-counting` (1580), `rem:ising-arithmetic-paradox` (1651), `rem:non-unimodular` (1719), `def:arithmetic-depth-filtration` (1757), `rem:depth-decomposition-universality` (1880), `rem:vnatural-class-m` (1938), `thm:shadow-sullivan` (1973), `rem:shadow-metric-gram` (2103), `rem:stieltjes-discriminant` (2197), `rem:transcendence-asymmetry` (2329), `rem:mc-motivic-identity` (2346), `rem:shadow-tower-dm-z` (2386), `prop:resurgent-orthogonality` (2491), `prop:gevrey-zero-degree` (2564), `rem:resurgent-anomaly-cancellation` (2599), `prop:padic-convergence` (2622), `rem:kummer-kubota-leopoldt` (2648), `rem:ferrero-washington-failure` (2693), `thm:drinfeld-associator-bar-transport` (2833), `rem:zagier-dimension-shadow` (2904), `rem:shadow-mzv-observational` (2927), `thm:partition-modular-classification` (3018), `rem:l-functions-koszul-pairs` (3121), `prop:hecke-eigenvalue-extraction` (3152), `prop:moment-matrix-negativity` (3242), `rem:shadow-p-adic-locality` (3264), `prop:calogero-shadow-dictionary` (3298), `rem:tau-shadow-kw` (3379), `rem:shadow-eisenstein-numerical-check` (3631), `rem:langlands-gl2-eisenstein` (3694), `rem:shadow-s1-quantum-volume-evidence` (3749), `rem:cs-bernoulli` (3889), `thm:nonabelian-hodge` (3920), `rem:depth-hodge` (4095), `rem:nahc-upgrade` (4140), `rem:ode-im-shadow-identification` (4273), `rem:wn-galois-evidence` (4590), `rem:eisenstein-deformation` (4611), `rem:bps-self-referential` (4699), `thm:general-bps` (4719), `rem:dt-pt-wall-crossing` (4760), `ex:heisenberg-intertwining` (4910), `rem:specialised-shadow-field-invariants` (5390), `prop:koszul-field-criterion` (5441), `ex:koszul-field-1-25` (5500), `ex:koszul-field-13` (5507), `prop:two-fixed-points` (5516), `rem:koszul-epstein-constraints` (5638), `prop:heisenberg-koszul-epstein` (5683), `comp:virasoro-c1-koszul-epstein` (5735), `rem:davenport-heilbronn-koszul-epstein` (5799), `rem:virasoro-character-vector` (5898), `rem:vvmf-rankin-selberg` (5899), `def:potential-side-transform` (5934), `def:gram-side-transform` (5952), `def:genuine-residue-moment-matrix` (6150), `def:compatibility-ratios` (6174), `rem:li-numerical-values-arith` (6497), `rem:sewing-lift-two-line` (6589), `rem:euler-product-from-independent-sum` (6629), `rem:propagator-variance-euler` (6711), `rem:virasoro-first-miura-defect` (6838), `def:residue-divisor` (6990), `rem:clutching-defect-meaning` (7032), `rem:clutching-vs-quartic-closure` (7087), `def:local-compatibility-discrepancy` (7114), `def:beilinson-functional` (7139), `rem:beilinson-closure-hierarchy` (7168), `rem:zeta-proxy-failure` (7204), `rem:decisive-computation` (7264), `rem:quartic-meeting-point` (7334), `rem:arithmetic-end-state` (7367), `rem:mc-rigidity-diagnosis` (7704), `rem:operadic-transfer` (7729), `def:shadow-bracket-form` (7758), `thm:petersson-identification` (7778), `rem:route-c-finite-atoms` (7936), `conj:modular-spectral-rigidity-sharp` (7952), `prop:lattice-ramanujan-rigidity` (7999), `ex:leech-rigidity` (8023), `rem:naive-prime-locality-obstruction` (8259), `prop:shadow-arithmetic-trichotomy` (8292), `rem:mgf-relation` (8613), `rem:universal-ramanujan` (8962), `rem:prime-locality-known` (9046), `prop:mc-constraint-counting` (9249), `rem:route-c-hypotheses` (9390), `rem:theta-bridge-resolution` (9631), `rem:two-chiralities` (9838), `rem:kronecker-limit` (9855), `rem:algebra-representation-gap` (9970), `rem:holomorphic-arithmetic-blindness` (10113), `rem:three-new-gaps` (10319), `rem:honest-comparison` (10362), `def:scattering-coupling` (10468), `rem:factorization-scope` (10547), `rem:hecke-defect-leading` (10769), `rem:hecke-defect-two-levels` (10908), `conj:conditional-ramanujan` (11005), `rem:langlands-interface` (11152), `def:arithmetic-packet-module` (11194), `rem:packet-reformulation` (11415), `rem:arithmetic-comparison-sharpening` (11488), `ex:packet-heisenberg` (11686), `ex:packet-rank1-lattice` (11749), `ex:packet-virasoro` (11783), `ex:packet-w3` (11857), `rem:genus2-definitive-scope` (12261), `rem:leech-all-sk` (12316), `prop:prime-locality-proved-cases` (12553), `thm:prime-locality-obstructions` (12594), `rem:route-c-success` (12702), `rem:route-c-gap` (12726), `thm:riccati-determinacy-assessment` (12796), `prop:shadow-not-selberg` (12839), `rem:shadow-riemann-independence` (12900), `rem:prime-locality-definitive` (12937). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
./wave2_audit_20260413_001942/U13_dead_labels.md:1383:12:- [MEDIUM] chapters/connections/arithmetic_shadows.tex:227 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:lattice-specificity` (227), `prop:divisor-sum-decomposition` (311), `prop:sewing-trace-formula` (349), `thm:narain-universality` (444), `rem:discrimination-hierarchy` (756), `prop:shadow-arithmetic-factorization` (779), `rem:genus2-theta-niemeier` (832), `rem:mc-complete-niemeier` (882), `rem:shadow-spectral-CG` (984), `prop:hecke-all-orders` (1021), `prop:period-shadow-dictionary` (1072), `rem:depth-non-unimodular` (1137), `comp:period-shadow-vz` (1155), `comp:period-shadow-ve8` (1173), `comp:period-shadow-leech` (1195), `comp:period-shadow-rank24-comparison` (1247), `comp:period-shadow-rank2` (1266), `thm:spectral-decomposition-principle` (1290), `rem:homotopy-becomes-arithmetic` (1330), `def:cusp-growth-rate` (1366), `prop:growth-rate-dictionary` (1377), `thm:bg-vir-coincidence` (1403), `cor:rigorous-infinite-depth` (1546), `prop:bg-primary-counting` (1580), `rem:ising-arithmetic-paradox` (1651), `rem:non-unimodular` (1719), `def:arithmetic-depth-filtration` (1757), `rem:depth-decomposition-universality` (1880), `rem:vnatural-class-m` (1938), `thm:shadow-sullivan` (1973), `rem:shadow-metric-gram` (2103), `rem:stieltjes-discriminant` (2197), `rem:transcendence-asymmetry` (2329), `rem:mc-motivic-identity` (2346), `rem:shadow-tower-dm-z` (2386), `prop:resurgent-orthogonality` (2491), `prop:gevrey-zero-degree` (2564), `rem:resurgent-anomaly-cancellation` (2599), `prop:padic-convergence` (2622), `rem:kummer-kubota-leopoldt` (2648), `rem:ferrero-washington-failure` (2693), `thm:drinfeld-associator-bar-transport` (2833), `rem:zagier-dimension-shadow` (2904), `rem:shadow-mzv-observational` (2927), `thm:partition-modular-classification` (3018), `rem:l-functions-koszul-pairs` (3121), `prop:hecke-eigenvalue-extraction` (3152), `prop:moment-matrix-negativity` (3242), `rem:shadow-p-adic-locality` (3264), `prop:calogero-shadow-dictionary` (3298), `rem:tau-shadow-kw` (3379), `rem:shadow-eisenstein-numerical-check` (3631), `rem:langlands-gl2-eisenstein` (3694), `rem:shadow-s1-quantum-volume-evidence` (3749), `rem:cs-bernoulli` (3889), `thm:nonabelian-hodge` (3920), `rem:depth-hodge` (4095), `rem:nahc-upgrade` (4140), `rem:ode-im-shadow-identification` (4273), `rem:wn-galois-evidence` (4590), `rem:eisenstein-deformation` (4611), `rem:bps-self-referential` (4699), `thm:general-bps` (4719), `rem:dt-pt-wall-crossing` (4760), `ex:heisenberg-intertwining` (4910), `rem:specialised-shadow-field-invariants` (5390), `prop:koszul-field-criterion` (5441), `ex:koszul-field-1-25` (5500), `ex:koszul-field-13` (5507), `prop:two-fixed-points` (5516), `rem:koszul-epstein-constraints` (5638), `prop:heisenberg-koszul-epstein` (5683), `comp:virasoro-c1-koszul-epstein` (5735), `rem:davenport-heilbronn-koszul-epstein` (5799), `rem:virasoro-character-vector` (5898), `rem:vvmf-rankin-selberg` (5899), `def:potential-side-transform` (5934), `def:gram-side-transform` (5952), `def:genuine-residue-moment-matrix` (6150), `def:compatibility-ratios` (6174), `rem:li-numerical-values-arith` (6497), `rem:sewing-lift-two-line` (6589), `rem:euler-product-from-independent-sum` (6629), `rem:propagator-variance-euler` (6711), `rem:virasoro-first-miura-defect` (6838), `def:residue-divisor` (6990), `rem:clutching-defect-meaning` (7032), `rem:clutching-vs-quartic-closure` (7087), `def:local-compatibility-discrepancy` (7114), `def:beilinson-functional` (7139), `rem:beilinson-closure-hierarchy` (7168), `rem:zeta-proxy-failure` (7204), `rem:decisive-computation` (7264), `rem:quartic-meeting-point` (7334), `rem:arithmetic-end-state` (7367), `rem:mc-rigidity-diagnosis` (7704), `rem:operadic-transfer` (7729), `def:shadow-bracket-form` (7758), `thm:petersson-identification` (7778), `rem:route-c-finite-atoms` (7936), `conj:modular-spectral-rigidity-sharp` (7952), `prop:lattice-ramanujan-rigidity` (7999), `ex:leech-rigidity` (8023), `rem:naive-prime-locality-obstruction` (8259), `prop:shadow-arithmetic-trichotomy` (8292), `rem:mgf-relation` (8613), `rem:universal-ramanujan` (8962), `rem:prime-locality-known` (9046), `prop:mc-constraint-counting` (9249), `rem:route-c-hypotheses` (9390), `rem:theta-bridge-resolution` (9631), `rem:two-chiralities` (9838), `rem:kronecker-limit` (9855), `rem:algebra-representation-gap` (9970), `rem:holomorphic-arithmetic-blindness` (10113), `rem:three-new-gaps` (10319), `rem:honest-comparison` (10362), `def:scattering-coupling` (10468), `rem:factorization-scope` (10547), `rem:hecke-defect-leading` (10769), `rem:hecke-defect-two-levels` (10908), `conj:conditional-ramanujan` (11005), `rem:langlands-interface` (11152), `def:arithmetic-packet-module` (11194), `rem:packet-reformulation` (11415), `rem:arithmetic-comparison-sharpening` (11488), `ex:packet-heisenberg` (11686), `ex:packet-rank1-lattice` (11749), `ex:packet-virasoro` (11783), `ex:packet-w3` (11857), `rem:genus2-definitive-scope` (12261), `rem:leech-all-sk` (12316), `prop:prime-locality-proved-cases` (12553), `thm:prime-locality-obstructions` (12594), `rem:route-c-success` (12702), `rem:route-c-gap` (12726), `thm:riccati-determinacy-assessment` (12796), `prop:shadow-not-selberg` (12839), `rem:shadow-riemann-independence` (12900), `rem:prime-locality-definitive` (12937). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
./wave2_audit_20260413_001942/U13_dead_labels.md:1748:- [MEDIUM] appendices/nonlinear_modular_shadows.tex:35 — PROBLEM: dead labels on claim-like environments (theorem/proposition/definition/remark/example/convention/etc.) with zero incoming refs: `rem:shadow-period-correction` (35), `rem:nms-prefundamental-cg` (74), `rem:shadow-termination-novelty` (289), `prop:nms-five-component` (335), `thm:nms-shadow-tower-mc` (395), `cor:nms-all-families-universal` (435), `rem:nms-chriss-ginzburg` (448), `def:nms-ambient-datum` (480), `def:nms-ambient-tangent-complex` (513), `thm:nms-ambient-complementarity-tangent` (528), `thm:nms-ambient-complementarity-fmp` (552), `rem:nms-stronger-than-additive` (566), `def:nms-degree-shadows` (693), `rem:nms-hcq-as-degree-shadows` (706), `def:nms-shadow-graph-complex` (849), `rem:nms-tree-vs-obstruction` (882), `def:nms-primary-composite-envelope` (903), `prop:nms-quartic-closure-envelope` (924), `cor:nms-heisenberg-gaussian-boundary` (974), `rem:nms-class-g-not-over-a-point` (986), `rem:nms-heisenberg-derived-center` (1011), `def:nms-affine-sector` (1029), `cor:nms-affine-boundary-tree` (1062), `conj:nms-critical-mc` (1103), `rem:nms-critical-purely-nonlinear` (1116), `rem:nms-affine-derived-center` (1121), `def:nms-betagamma-slice` (1138), `cor:nms-betagamma-boundary-law` (1191), `rem:nms-uniform-linearity` (1249), `rem:nms-betagamma-derived-center` (1254), `def:nms-virasoro-envelope` (1304), `rem:quartic-theta-significance` (1394), `rem:nms-virasoro-derived-center` (1431), `def:nms-w3-envelope` (1460), `thm:nms-w3-mixed-shadow-normal-form` (1472), `def:nms-w3-primary-resonance` (1502), `rem:nms-visible-vs-full-resonance` (1526), `def:nms-principal-wn-envelope` (1590), `def:nms-generic-parameter-locus` (1661), `def:nms-contact-quartic-bundle` (1666), `rem:nms-tautological-lines` (1685), `prop:nms-basis-independence-specialization` (1747), `rem:nms-why-characteristic-class` (1760), `def:nms-cubic-tree-bundle` (1768), `rem:nms-tree-class-interpretation` (1794), `rem:nms-log-fm-clutching` (1863), `cor:nms-family-boundary-behavior` (1910), `rem:nms-why-quartic-resonance-is-new` (1942), `def:nms-nonlinear-characteristic-package` (1950), `prop:nms-functoriality-duality-quartic` (1979), `rem:nms-characteristic-hierarchy` (1988), `rem:nms-frontier-reset` (2047), `thm:nms-quintic-frame-families` (2153), `rem:nms-virasoro-infinite-tower` (2208), `cor:nms-quintic-separating-boundary` (2232), `prop:nms-genus-loop-properties` (2278), `rem:nms-beyond-ahat` (2335), `rem:nms-modular-invariant-ratio` (2396), `def:nms-full-modular-shadow-characteristic` (2406), `rem:nms-invariant-hierarchy-summary` (2432), `thm:nms-unified-summary` (2452), `rem:nms-what-remains` (2494), `def:nms-modular-feynman-transform` (2507), `rem:nms-feynman-three-requirements` (2538), `def:nms-complementarity-legendrian` (2568), `rem:nms-legendrian-three-virtues` (2580), `rem:nms-phase-wall-crossing` (2748), `def:nms-nonlinear-branch-stack` (2756), `rem:nms-conceptual-outcome` (2772), `def:nms-polarized-modular-graph-algebra` (2795), `thm:nms-bipartite-complementarity` (2821), `conj:nms-polarized-universal-class` (2829), `def:nms-resonance-wall-locus` (2844), `def:nms-resonance-scattering-diagram` (2853), `def:nms-complementarity-schober` (2874), `rem:nms-schober-vs-scattering` (2884), `def:nms-modular-wavefunction` (2892), `rem:nms-wavefunction-normal-forms` (2909), `conj:nms-quartic-lift` (2948), `rem:quartic-lift-evidence` (2953), `conj:nms-resonance-wall-crossing` (2989), `conj:nms-quantization-theorem` (2994), `rem:nms-implementation-path` (2999), `rem:nms-bridge-consumption` (3079), `rem:nms-extended-hierarchy` (3135), `rem:nms-factorization-envelope-programme` (3154), `rem:nms-mc4-finite-linear-algebra` (3465), `def:nms-kappa-matrix` (3513), `ex:nms-w3-multivariable-shadow` (3584), `rem:propagator-variance-mixing` (3632), `rem:nms-w4-two-propagator` (3724), `rem:ds-depth-monotonicity-failure` (3805), `rem:ds-ghost-shadow-consistency` (3891), `rem:ope-closedness-necessary` (4019), `rem:nms-discriminant-instability` (4179), `def:nms-mc-moduli-curve` (4213), `thm:nms-mc-moduli-curve-structure` (4236), `thm:nms-hadamard-mc-potential` (4299), `cor:nms-mc-solution-counting` (4346), `rem:nms-trivial-isomonodromy` (4363). FIX: Keep the surrounding mathematical content, but delete the listed `\label{...}` commands. If one of these surfaces is supposed to be cited, add a real inbound reference instead of carrying a dead anchor.
./wave2_audit_20260413_001942/F08_prerequisites_thm_D.md:897:  1011	$\tau_{kl} = \oint_{B_l} \omega_k \in \mathfrak{H}_g$ determines
./audit_campaign_20260412_231034/AP23_pi3_BU.md:404:/Users/raeez/calabi-yau-quantum-groups/compute/lib/e1_descent_theory.py:1011:      But for CY3, the S^3-framing is TOPOLOGICALLY trivial (pi_3(BU) = 0),
./wave2_audit_20260413_001942/B05_thm_H_bridge.md:1297:  1011	trivial topological direction ($\R = \mathrm{pt}$), the chiral
./wave2_audit_20260413_001942/D15_hardcoded_parts.md:1643:  1011	statements; the present chapter is the algebraic engine that makes the
./rectification_20260412_233715/R07_yangians_computations.md:1378:index 08039b9b4c1f9f675510c6eb17725f65180f795b..570967eda1c5428101121a282cad98ce4f0ca4f0
./rectification_20260412_233715/R07_yangians_computations.md:1517:index 08039b9b4c1f9f675510c6eb17725f65180f795b..570967eda1c5428101121a282cad98ce4f0ca4f0
./rectification_20260412_233715/R07_yangians_computations.md:1767:index 08039b9b4c1f9f675510c6eb17725f65180f795b..570967eda1c5428101121a282cad98ce4f0ca4f0
./rectification_20260412_233715/R07_yangians_computations.md:1929:index 08039b9b4c1f9f675510c6eb17725f65180f795b..570967eda1c5428101121a282cad98ce4f0ca4f0
./rectification_20260412_233715/R07_yangians_computations.md:2086:index 08039b9b4c1f9f675510c6eb17725f65180f795b..570967eda1c5428101121a282cad98ce4f0ca4f0
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,200p' audit_campaign_20260412_231034/T08_MC1_PBW.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# T08_MC1_PBW (622s, gpt-5.4)

- [CRITICAL] [higher_genus_modular_koszul.tex:994](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:994) — The genus-1 Kac--Moody proof explicitly allows `d_1^{PBW}` of enrichment classes to land in the concentrated genus-0 sector (`E_1(g=0) \oplus \mathcal E_1`). The later proofs at [1292](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1292), [1472](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1472), [801](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:801), and [1709](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1709) then kill the enrichment and conclude `E_\infty(g)=E_\infty(0)` without controlling those mixed maps. That comparison is not proved.

- [CRITICAL] [higher_genus_modular_koszul.tex:1011](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1011) — The proof says `d_1^{PBW}` is built from the bracket of the truncated loop algebra, then immediately reidentifies the enrichment as `C^*(\fg,M_h)` and invokes Whitehead for semisimple `\fg` at [1027](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1027). That reduction is not justified by the text. The same unsupported move reappears at [1294](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1294) and [1776](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1776). Whitehead applies to `\fg`, not automatically to the truncated current algebra that the proof itself names.

- [HIGH] [higher_genus_modular_koszul.tex:1050](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1050) — The displayed `d_2` computation does not hit the invariant class it claims to kill. The surviving class is `\kappa^{ab}(J^a_{-1}\otimes J^b_{-1})\otimes\alpha`, but the computed image is `k\dim(\fg)\,J^c_{-1}\otimes\alpha`, a different target. The all-genera repetition at [1346](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1346) has the same defect. This step also requires `k\neq0`, while the theorem statement [1210](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1210) includes generic `k\notin\Sigma(\fg)`, and the cited genericity theorem [kac_moody.tex:983](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:983) excludes special values via `\lambda=k+h^\vee`, not by removing `k=0`.

- [HIGH] [higher_genus_modular_koszul.tex:1264](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1264) — Inference: the factorization `\mathcal E_g^{*,h}\cong M_h\otimes H^{1,0}(\Sigma_g)` is asserted but not proved, and it is hard to reconcile with the chain groups written at [955](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:955), which use `\Omega^{n-1}_{\log}` in bar degree `n`. For `n>2`, the regular contribution should depend on bar degree and allow multiple global 1-forms, not a single `H^{1,0}` factor. This unsupported factorization is then reused in the Virasoro, principal-`\mathcal W`, and universal proofs.

- [HIGH] [concordance.tex:1842](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1842) — Downstream propagation is overstated. Concordance packages `prop:pbw-universality` as an MC1 citation for universal `V_k(\fg)`, `\mathrm{Vir}_c`, and `\mathcal W^k(\fg)`, but [chiral_koszul_pairs.tex:1314](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1314) only proves genus-0 chiral Koszulness of freely strongly generated vertex algebras. It does not prove the all-genera PBW concentration used elsewhere for MC1, including [editorial_constitution.tex:193](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:193).

- [MEDIUM] [higher_genus_modular_koszul.tex:1486](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1486) — The Virasoro proof misquotes its own cited input. It says `\dim M_h=p(h-2)` by `comp:virasoro-vacuum`, but [bar_complex_tables.tex:278](/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:278) gives `\dim \bar V_h=p_{\ge2}(h)=p(h)-p(h-1)`; at `h=5` the table gives `2`, while `p(3)=3`. This is not fatal by itself, but the cited step is false as written.

- [LOW] [higher_genus_modular_koszul.tex:1380](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1380) — The repeated appeal to `H^{0,1}(\Sigma_g)` “antiholomorphic forms” sits outside the algebraic bar-complex surface actually written, which uses logarithmic forms [higher_genus_modular_koszul.tex:955](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:955) on a smooth projective curve [higher_genus_modular_koszul.tex:534](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:534). This is a scope/convention leak even if the core theorem were repairable.

## Summary
Instances checked: 15 | Violations found: 7 | Verdict: FAIL



thinking
**Analyzing audit fixes in T08_MC1_PBW**

I’m carefully examining the user’s request to identify two minimal but truthful corrections in the T08_MC1_PBW file—first, clarifying the justification for transitioning from the truncated current algebra to the Chevalley-Eilenberg complex, and second, finding issues related to Theorem D and genus universality by searching the file for relevant references to audit them. This will help ensure a clear, accurate bridge in the proofs around those line numbers.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" audit_campaign_20260412_231034/T08_MC1_PBW.md' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem D" audit_campaign_20260412_231034/*.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/BC06_genus_0.md:7:[CRITICAL] chapters/connections/concordance.tex:54 — The concordance table states Theorem D as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera.” The governing theorem itself only states that formula for `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)). Since the concordance is the repo’s status constitution, this is a top-level scope misstatement at the genus-0 boundary.
audit_campaign_20260412_231034/BC06_genus_0.md:2001:[CRITICAL] chapters/connections/concordance.tex:54 — The concordance table states Theorem D as `\mathrm{obs}_g=\kappa\lambda_g` “at all genera.” The governing theorem itself only states that formula for `g\ge 1` ([chapters/theory/higher_genus_foundations.tex:5303](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:5303)). Since the concordance is the repo’s status constitution, this is a top-level scope misstatement at the genus-0 boundary.
audit_campaign_20260412_231034/AP12_markdown_latex.md:342:/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:221: \item[Theorem D (modular characteristic).] The genus-$g$ obstruction is $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g^{\mathrm{FP}}$ on the uniform-weight lane, where $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is the CY modular characteristic. For rigid compact CICYs with $h^{1,0} = 0$, the BCOV prediction gives $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}} / 24$; for K3-fibered CY$_3$, this fails (Theorem~\ref{thm:chi-neq-kappa}).
audit_campaign_20260412_231034/CE06_bar_cohom.md:166:CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
audit_campaign_20260412_231034/CE03_koszul_conductor.md:439:     6	At the scalar level (Theorem D):
audit_campaign_20260412_231034/CE03_koszul_conductor.md:499:     3	Theorem C (complementarity) at the scalar level (Theorem D):
audit_campaign_20260412_231034/CE05_E8_dims.md:139:CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
audit_campaign_20260412_231034/F01_kappa_KM.md:593:standalone/N3_e1_primacy.tex:920:Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
audit_campaign_20260412_231034/F01_kappa_KM.md:1113:   668	Among the five, Theorem D makes the $E_{1}$ primacy thesis most
audit_campaign_20260412_231034/CE09_cy3_engines.md:155:/Users/raeez/chiral-bar-cobar/CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
audit_campaign_20260412_231034/T05_thm_C2.md:15:- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:433](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:433) — The live manuscript no longer defines C2 as a scalar BV pairing. It defines C2 as the conditional bar-side BV / shifted-symplectic upgrade and explicitly says the scalar complementarity formulas are consequences of C1 plus Theorem D, “not a separate C2 label” ([higher_genus_complementarity.tex:441](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:441)). So the requested “Theorem C2: scalar BV pairing (conditional on uniform-weight)” is already off the current theorem surface.
audit_campaign_20260412_231034/T05_thm_C2.md:177:CLAUDE.md:414:**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).
audit_campaign_20260412_231034/T05_thm_C2.md:2663:- [MEDIUM] [chapters/theory/higher_genus_complementarity.tex:433](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:433) — The live manuscript no longer defines C2 as a scalar BV pairing. It defines C2 as the conditional bar-side BV / shifted-symplectic upgrade and explicitly says the scalar complementarity formulas are consequences of C1 plus Theorem D, “not a separate C2 label” ([higher_genus_complementarity.tex:441](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:441)). So the requested “Theorem C2: scalar BV pairing (conditional on uniform-weight)” is already off the current theorem surface.
audit_campaign_20260412_231034/F18_complementarity.md:782:/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:530:% For W-algebras: kappa + kappa' = rho*K (Theorem D).
audit_campaign_20260412_231034/F18_complementarity.md:1697:I’m noticing a potential conflict in the naming conventions within the documents. The `complementarity constant` for the shift `α_N` in one part contrasts with `K_N` in another, which isn't in line with the canonical scalar naming `K(Vir)=13`. Is this an actual discrepancy, or are these just two separate quantities? I should focus on how the formulas align with the canonical forms since the user highlighted that they match. I may also want to check for any wrong references related to Theorem D.
audit_campaign_20260412_231034/F14_averaging.md:892:   668	Among the five, Theorem D makes the $E_{1}$ primacy thesis most
audit_campaign_20260412_231034/F14_averaging.md:1420:  1269	\index{five main theorems!E1@$E_1$ variant!Theorem D}
audit_campaign_20260412_231034/T04_thm_C1.md:124:CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
audit_campaign_20260412_231034/T04_thm_C1.md:228:CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
audit_campaign_20260412_231034/XV08_thm_status_xvol.md:311:/bin/zsh -lc "rg -n --glob 'README*' --glob '*.tex' --glob '*.md' 'thm:genus-universality|Modular characteristic|Theorem D|obs_g\\(\\\\cA\\)=\\\\kappa\\(\\\\cA\\)\\\\lambda_g' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5280,5355p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\hline
Heisenberg $\mathcal{H}_\kappa$ & $\kappa \cdot \lambda_g$ & Level shift / central charge \\
\hline
$\widehat{\mathfrak{sl}}_2(k)$ & $\frac{3(k+2)}{4} \lambda_g$ & Affine level shift \\
\hline
$\widehat{\mathfrak{sl}}_3(k)$ & $\frac{4(k+3)}{3} \lambda_g$ & Affine level shift \\
\hline
$\widehat{E_8}(k)$ & $\frac{62(k+30)}{15} \lambda_g$ & Affine level shift \\
\hline
$W_3(c)$ & $\frac{5c}{6} \lambda_g$\rlap{${}^*$} & Conformal anomaly \\
\hline
Virasoro $(c)$ & $\frac{c}{2} \lambda_g$ & Conformal anomaly \\
\hline
\multicolumn{3}{|l|}{\small ${}^*$Unconditional at $g=1$; $g \geq 2$ receives cross-channel correction.}\\
\hline
\end{tabular}
\end{table}

\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
\index{genus universality theorem|textbf}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "family-index" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
194:(Theorem~\ref{thm:family-index}).
599: The generating function on the uniform-weight lane is \begin{equation}\label{eq:family-index-package}
631:\eqref{eq:family-index-package} is its
633:(Theorem~\ref{thm:family-index}).
1074:(Theorem~\ref{thm:family-index}). The scalar $\kappa(\cA)$ is the
5405:does not invoke Theorem~\ref{thm:family-index}.
6386:\begin{remark}[Family index theorem]\label{rem:towards-family-index}
6388:The family index theorem (Theorem~\ref{thm:family-index}) assembles
6789: \textup{(}Theorem~\textup{\ref{thm:family-index})}: the
6827:(Theorem~\ref{thm:family-index}) gives
6897:the third in Theorem~\ref{thm:family-index}.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1768,1818p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1768	by~$T_{(1)} = L_0$:
  1769	\[
  1770	d_2^{\mathrm{PBW}}\big|_{\mathcal{E}_g^{*,h}}
  1771	\;=\;
  1772	h \cdot \mathrm{id}_{M_h}
  1773	\otimes
  1774	\mathrm{id}_{H^{1,0}(\Sigma_g)}.
  1775	\]
  1776	Since $h \geq h_{\min} > 0$, this map is an isomorphism,
  1777	killing the entire genus-$g$ enrichment on the $E_3$ page.
  1778	The weight-lowering contributions from generators with $s < 2$
  1779	now act on zero (the enrichment is already dead) and cannot
  1780	create new classes.
  1781	
  1782	The antiholomorphic factor $H^{0,1}(\Sigma_g)$ is handled
  1783	identically. Bounded-below convergence
  1784	\textup{(}\ref{item:pbw-bounded} of
  1785	Theorem~\ref{thm:pbw-koszulness-criterion}\textup{)}
  1786	then shows that once later differentials and extension classes are
  1787	ruled out by family-specific input, the genus-$g$ and genus-$0$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '580,660p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $H^0(\Sigma_g,\Omega^1)$ of rank~$g$. As
 $[\Sigma_g]$ varies, the scalar trace of the
 curvature endomorphism defines an obstruction class.
 For uniform-weight algebras and at
 genus~$1$ for arbitrary families
 \textup{(g=1 only; all-weight at g=1 is unconditional)}:
 \begin{equation}\label{eq:obstruction-hodge}
 \mathrm{obs}_g(\cA)
 \;=\;
 \kappa(\cA)\cdot\lambda_g
 \;\in\;
 H^{2g}(\overline{\mathcal{M}}_g,\mathbb{Q}),
 \end{equation}
 where $\lambda_g = c_g(\mathbb{E})$ is the top Chern
 class \textup{(LOCAL)}.
 For multi-weight algebras at $g \geq 2$,
 a cross-channel correction $\delta F_g^{\mathrm{cross}}$
 is present
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
 The generating function on the uniform-weight lane is \begin{equation}\label{eq:family-index-package}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:family-index\" -n chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{thm:family-index\" -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/concordance.tex:5928:\ClaimStatusProvedHere]\label{thm:family-index}
exec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|Theorem~\\\\ref\\{thm:family-index\\}|genus-universality\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
2436: (Theorem~\ref{thm:genus-universality}).
2543:(Theorem~\ref{thm:genus-universality}).
2729:Theorem~\ref{thm:genus-universality} identifies that trace with
2732:Part~(i) is Theorem~\ref{thm:genus-universality} for
2740:Theorem~\ref{thm:genus-universality}(ii).
2804:Theorem~\ref{thm:genus-universality}; the second arrow is the
2811:Theorem~\ref{thm:genus-universality}); generating function via
3184:Theorem~\ref{thm:genus-universality}. The GUE free energy
3345:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3768:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
3820:Theorem~\ref{thm:genus-universality}(ii)).
5386:(Theorem~\ref{thm:genus-universality},
7786:proved genus-universality formula
7787:(Theorem~\ref{thm:genus-universality}).
7943:Theorem~\ref{thm:genus-universality} identifies the scalar trace
8091:Theorem~\ref{thm:genus-universality} identifies
8515:by Theorem~\ref{thm:genus-universality}\textup{(iii)}.
9595:Theorem~\textup{\ref{thm:genus-universality}}, then the full
9650:By Theorem~\ref{thm:genus-universality},
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5900,5965p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{Duality.}
$\Delta_{\cA^!}(x)=\Delta_\cA(x)$ for all Koszul pairs:
the spectral discriminant is self-dual. For
$\widehat{\mathfrak{sl}}_2$: the zero at $1/k$ corresponds
to level~$k$; the zero at $1/(k{+}4)$ corresponds to the
dual level $-k-4$. The product of the two zeros is
$1/(k(k{+}4))$; their sum is $(2k{+}4)/(k(k{+}4))=2/k+2/(k{+}4)
\to 0$ as $k\to\infty$.

\emph{Rank.}
$\operatorname{rank}(\Delta_\cA)
=\deg\Delta_\cA
=\dim H^1_{\mathrm{cyc,prim}}(\cA)$: the number of independent
genus-$1$ deformation directions. Rank~$1$ for algebras with
one-dimensional deformation space (Heisenberg, Virasoro,
$\beta\gamma$); rank~$2$ for $\widehat{\mathfrak{sl}}_2$ and
$\mathcal W_3$.
\end{computation}

\subsection{The index theorem for genus expansions}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5965,6035p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\right]_g^{\mathrm{eval}},
\end{equation}
where $[\cdot]_g^{\mathrm{eval}}$ denotes evaluation of the degree-$g$ Chern character
$\operatorname{ch}_g(\mathbb{E})$ against $\psi^{2g-2}$ on
$\overline{\mathcal{M}}_{g,1}$.

\item \emph{$\hat{A}$-genus identification.}
On the same uniform-weight locus, the total generating function is
\begin{equation}\label{eq:family-index-generating}
\sum_{g \geq 1} F_g(\cA)\, x^{2g}
\;=\;
\kappa(\cA) \cdot \bigl(\hat{A}(ix) - 1\bigr)
\;=\;
\kappa(\cA) \cdot
\left(\frac{x/2}{\sin(x/2)} - 1\right),
\end{equation}
where the function $(x/2)/\sin(x/2)$ arises from
$\operatorname{Td}(T_\pi) = c_1(\omega_\pi)/(1 - e^{-c_1(\omega_\pi)})$
in the GRR formula, Wick-rotated by the positivity of
tautological intersection numbers on
exec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|begin\\{theorem\\}.*family index|Family index theorem|family index theorem\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4406: by the family index theorem
4456:Part~(f) is the family index theorem
13933:now seen as a consequence of (i) via the family index theorem
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6035,6125p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{Step~2: Mumford's GRR computation.}
By Grothendieck--Riemann--Roch applied to the universal curve
$\pi \colon \overline{\mathcal{C}}_g \to \overline{\mathcal{M}}_g$
and the relative dualizing sheaf~$\omega_\pi$:
\begin{equation}\label{eq:mumford-grr}
\operatorname{ch}(\mathbb{E})
\;=\;
\operatorname{ch}(R^0\pi_*\omega_\pi)
\;=\;
1 + \pi_*\!\left(
 \operatorname{ch}(\omega_\pi) \cdot
 \operatorname{Td}(T_\pi)
\right),
\end{equation}

Serre duality on the fibers gives
$R^1\pi_*\omega_\pi \cong (R^0\pi_*\mathcal{O})^\vee \cong \mathcal{O}$,
so $\operatorname{ch}(R\pi_*\omega_\pi) = \operatorname{ch}(\mathbb{E}) - 1$.

Write $K = c_1(\omega_\pi)$ for the relative canonical class. Since
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n -C 20 "thm:genus-universality" chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1098

172-$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$, where $\omega_g$ is the
173-Arakelov $(1,1)$-form
174-(Theorem~\ref{thm:quantum-arnold-relations}).
175-The total corrected differential $\Dg{g}$, built from the
176-\emph{holomorphic} part $\partial_z\!\log E$ alone, satisfies
177-$\Dg{g}^{\,2} = 0$
178-(Theorem~\ref{thm:quantum-diff-squares-zero}):
179-the holomorphic propagator obeys the exact Arnold relation
180-by the Fay trisecant identity, so the nine-term verification
181-of nilpotence goes through verbatim from genus~$0$.
182-
183-As $[\Sigma_g]$ varies over $\overline{\mathcal{M}}_g$, the bar
184-complex forms a family of curved cochain complexes. The fiberwise
185-curvature defines a characteristic class
186-$\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g \in
187-H^*(\overline{\mathcal{M}}_g)$ for
188-uniform-weight algebras, where $\lambda_g = c_g(\mathbb{E})$ is
189-the top Chern class of the Hodge bundle; at genus~$1$ the same
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5300,5340p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

\begin{enumerate}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5340,5405p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\kappa + \kappa' = 13$ for the Virasoro algebra
($\varrho = 1/2$, $K = 26$),
and $\kappa + \kappa' = 250/3$ for $\mathcal{W}_3$
($\varrho = 5/6$, $K = 100$).
The obstruction coefficient $\kappa = 0$ if and only if $\mathcal{A}$ is at critical level;
for Kac--Moody the dual is then also critical, but for $\mathcal{W}$-algebras
$\kappa(\mathcal{A}^!) = \varrho(\mathfrak{g})\, K \neq 0$.

\emph{Abelian case.}
The Heisenberg algebra $\mathcal{H}_\kappa$ is the abelian Kac--Moody algebra
($\mathfrak{g}$ abelian, $h^\vee = 0$). The general formula
$\kappa = (k + h^\vee)\dim\mathfrak{g}/(2h^\vee)$ has a removable singularity
at $h^\vee = 0$; one defines $\kappa(\mathcal{H}_\kappa) = \kappa$ directly
from the genus-$1$ curvature (Theorem~\ref{thm:heisenberg-obs}).
The duality $\kappa + \kappa' = 0$ still holds: $\kappa(\mathcal{H}_\kappa^!) = -\kappa$,
consistent with the Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ being curved with
curvature $m_0 = -\kappa$. The complementarity constant $c + c'$ is not defined
in the usual sense because the dual is a curved (non-conformal) chiral algebra.
\item[\textup{(iii)}] \emph{Faber--Pandharipande formula.}
On the scalar lane (Definition~\ref{def:scalar-lane}), the genus-$g$ free energy is $F_g = \kappa \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$,



thinking
**Considering theorem validation**

I need to ensure I have both the Whitehead theorem and the general theorem about cohomology of semisimple Lie algebras. This relates to completely reducible modules vanishing if there are no invariants, also known as the Whitehead–Chevalley–Eilenberg theorem. I'm thinking about mentioning the full name to be clear. I'll also check for any flagged patterns in the document and verify the validity of my references and labels, running a grep search for any specifics.
thinking
**Checking for forbidden patterns**

I might need to check for B41, but I'm not entirely sure. Running an "rg" search for banned tokens on any modified lines could be useful too, but that feels like overkill. I don't think I need the specific command for the unneeded tokens right now. I should focus on grepping for “Whitehead” and “thm:family-index” since the user wants to verify the forbidden patterns in the modified files after all the edits.
collab wait(call_Fwg9gleCTEuMnctkGoOoJ4bb)
  receivers: 019d862b-7c8a-7370-a0d9-9ef2fae19bb8
thinking
**Summarizing minimal edits for circularity concerns**

I'm gathering that to resolve the reported circular dependency, the main fixes involve adding clarifying bridging text around lines 1011, 1027, 1294, and 1776 about applying Whitehead's lemma to a truncated algebra; and in the proof of Theorem D (around line 2695) explicitly stating that while the generating function references the family index theorem, that theorem itself depends on genus universality—so no true cycle arises. These minimal textual additions should clear up audit concerns without broad rewrites.
codex
- **Whitehead justification near the PBW spectral sequence (lines ~1010‑1035, 1290‑1350, 1768‑1840 in `chapters/theory/higher_genus_modular_koszul.tex`).**  The current text jumps from “$d_1^{\mathrm{PBW}}$ comes from the bracket of the truncated current algebra $\fg\otimes V_h$” straight to “$\mathcal{E}_1^{*,h}\cong C^*(\fg,M_h)$ and we invoke Whitehead,” so the reader has no bridge explaining why the non‑semisimple mode part can be ignored.  Insert a short paragraph saying that the mode algebra is abelian (the bracket acts only on the $\fg$ factors), that $d_1^{\mathrm{PBW}}$ therefore factors through the diagonal $\fg$ bracket, and that $M_h$ absorbs the $V_h$ multiplicities.  Once this is explicit the subsequent appeal to Whitehead on $\fg$ is justified; no new labels are needed, but keep the paragraph in the same neighborhood (the three occurrences around 1011/1027, 1294, and 1776) so the reader sees the same reduction whenever the enrichment is killed.

- **Theorem D / `thm:genus-universality` / `thm:family-index` dependency (proof of Theorem D around lines 2680‑2775 in `chapters/theory/higher_genus_modular_koszul.tex`, with the `constituent` arguments in `higher_genus_foundations.tex:5290‑5405` and `concordance.tex:5990‑6035`).**  The proof already cites `thm:genus-universality` for $\mathrm{obs}_g=\kappa\lambda_g$ and `thm:family-index` for the $\hat{A}$‑genus generating function, but the surrounding narrative makes it look like the two theorems depend on one another.  Add a one‑sentence clarifier immediately after the roadmap (around the paragraph that lists the dependency chain in the proof of Theorem D) explicitly stating “Theorem~\ref{thm:genus-universality} is proved by the scalar shadow recursion alone (see `higher_genus_foundations.tex:5380‑5445`), and `thm:family-index` is merely a GRR refinement of that already established scalar identity; there is no reverse dependence.”  This keeps the reference graph acyclic and warns readers that `family-index` relies on `genus-universality` (not vice versa).  No labels need to change, but make sure the sentence links the line numbers mentioned in the proof to `higher_genus_foundations.tex`/`concordance.tex` so the logical order is transparent.
wait(call_Fwg9gleCTEuMnctkGoOoJ4bb) 1 agents complete:
  019d862b-7c8a-7370-a0d9-9ef2fae19bb8 completed: "- **Whitehead justification near the PBW spectral sequence (lines ~1010‑1035, 1290‑1350, 1768‑1840 in `chapters/theory/h…"
codex
I’m applying the patch now. The edits are limited to the three Whitehead/PBW proof surfaces plus the Theorem D proof opening, with one short local remark added to freeze the reduction and one routing sentence to make the dependency graph explicit.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -1022,3 +1022,5 @@
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
@@ -1039,3 +1041,6 @@
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
@@ -1202,2 +1207,13 @@
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
@@ -1309,3 +1325,6 @@
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
@@ -1330,3 +1349,6 @@
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
@@ -1811,2 +1833,5 @@
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
@@ -2726,3 +2751,5 @@
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
@@ -2730,3 +2757,5 @@
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

codex
The patch is in. I’m re-reading only the touched blocks now to make sure the new sentences actually fit the proof flow and that the new remark doesn’t create any reference or logic drift.
exec
/bin/zsh -lc "sed -n '1015,1065p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1300,1350p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1188,1218p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1798,1822p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2726,2745p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
In each conformal
weight~$h$, the enrichment
$\mathcal{E}_1^{*,h}$ is a finite-dimensional complex
with only finitely many mode labels.
Write
$V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
The truncated current algebra $\fg \otimes V_h$
records which modes can occur at weight~$h$; Whitehead is
not applied to this non-semisimple Lie algebra. Its role is
only to enumerate the finitely many mode patterns~$\nu$
that occur in weight~$h$.
After separating the mode data from the $\fg$-labels,
the weight-$h$ enrichment block is a finite direct sum of
Chevalley--Eilenberg complexes
$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
mode patterns~$\nu$ of total weight~$h$. Each
$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
diagonal adjoint action on the $\fg$-labels and trivial
action on the mode and $H^1(E_\tau)$ factors. Equivalently,
\[
 succeeded in 51ms:
cochains are $d_0^{\mathrm{PBW}}$-closed. They are not
$d_0^{\mathrm{PBW}}$-exact by the same degree argument
as in genus~$1$. Thus
\begin{equation}\label{eq:e1-decomposition-genusg}
E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0)
 \;\oplus\; \mathcal{E}^{p,q}_g
\end{equation}
where $\mathcal{E}^{p,q}_g$ is the enrichment from
$H^{1,0}(\Sigma_g)$.

The enrichment
\emph{factors}: at each conformal weight~$h$,
\begin{equation}\label{eq:enrichment-factorization}
\mathcal{E}_g^{*,h}
\;\cong\; M_h \otimes_{\bC} H^{1,0}(\Sigma_g)
\end{equation}
where $M_h$ is the \emph{same} finite-dimensional
$\fg$-module as at genus~$1$.
This factorization holds because the
$H^{1,0}(\Sigma_g)$ forms enter as global
 succeeded in 50ms:
$\operatorname{rank}(d_1)=8$ at $n=3$ and
$\operatorname{rank}(d_1)=27$ at $n=4$ and
$\operatorname{rank}(d_1)=80$ at $n=5$ and
$\operatorname{rank}(d_1)=243$ at $n=6$ and
$\operatorname{rank}(d_1)=728$ at $n=7$; the commutators
$[\operatorname{ad}(x), d_1]$ ($x \in \mathfrak{sl}_2$) and
$[C_2, d_1]$ vanish identically in the full checks at
$n=3,4,5,6$ and remain zero in the staged $n=7$ extended run.

This verifies that the elimination pattern (nontrivial
summands killed by Whitehead, invariant summands passed to
higher $d_r$) is already stable at the first higher tensor
levels.

At each higher weight~$h$, the same
three mechanisms act (the representation-theoretic
decomposition under~$\fg$ and the Whitehead vanishing
are weight-independent), completing the proof.
\end{proof}

 succeeded in 51ms:
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
\item \emph{Duality.}
 Under Koszul duality, $\kappa$ satisfies a duality constraint:
 $\kappa(\cA) + \kappa(\cA^!) = 0$ for affine Kac--Moody and
 free-field algebras. For the principal $\mathcal{W}$-algebra
 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
 K_\fg \cdot \varrho(\fg)$
 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
 $m_1, \ldots, m_r$ the exponents;
 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
\item \emph{Additivity.}
 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
 Combined with~(iii), the vanishing
 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
 succeeded in 52ms:
Since $h \geq h_{\min} > 0$, this map is an isomorphism,
killing the entire genus-$g$ enrichment on the $E_3$ page.
The weight-lowering contributions from generators with $s < 2$
now act on zero (the enrichment is already dead) and cannot
create new classes.

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
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

exec
/bin/zsh -lc "sed -n '2724,2743p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 formula fails and a cross-channel correction
 $\delta F_g^{\mathrm{cross}}$ is required
 \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
\item \emph{Duality.}
 Under Koszul duality, $\kappa$ satisfies a duality constraint:
 $\kappa(\cA) + \kappa(\cA^!) = 0$ for affine Kac--Moody and
 free-field algebras. For the principal $\mathcal{W}$-algebra
 $\mathcal{W}^k(\mathfrak{g})$ under Drinfeld--Sokolov reduction,
 $\kappa(\mathcal{W}^k) + \kappa(\mathcal{W}^{k'}) =
 K_\fg \cdot \varrho(\fg)$
 where $K_\fg$ is the Feigin--Frenkel dual central-charge sum
 \textup{(}$K_{\mathfrak{sl}_2} = 26$,
 $K_{\mathfrak{sl}_3} = 100$\textup{)} and
 $\varrho(\fg) = \sum_{i=1}^{r} 1/(m_i + 1)$ is the anomaly
 ratio \textup{(}$r = \operatorname{rank}(\fg)$,
 $m_1, \ldots, m_r$ the exponents;
 $\varrho(\mathfrak{sl}_N) = H_N - 1$\textup{)}.
 In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
\item \emph{Additivity.}
 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

exec
/bin/zsh -lc "sed -n '2743,2762p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
 Combined with~(iii), the vanishing
 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
 $\cA \otimes \cA^!_{\mathrm{ghost}}$ is the algebraic
 form of anomaly cancellation.
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{Routing remark.}
The dependency route is one-way and has an independent anchor:
the bar-intrinsic shadow tower of
Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
Theorem~\ref{thm:genus-universality} identifies that trace with
$\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
subsequent GRR repackaging of the resulting genus series. There is no
reverse dependence from Theorem~\ref{thm:family-index} back to
Theorem~\ref{thm:genus-universality}.
Part~(i) is Theorem~\ref{thm:genus-universality} for
uniform-weight algebras. For multi-generator algebras
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization


thinking
**Reviewing sentence structure**

I'm thinking that line 1300 might need to be read again to check if it's a continuation or if it feels truncated. I want to ensure that the sentence flows well and doesn't sound weird in its current form. Let's dig a bit further into it to make sure everything reads smoothly. Yes, clarity is key here!
exec
/bin/zsh -lc "sed -n '1324,1344p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
smooth across these divisors. The module~$M_h$ is
determined solely by the OPE structure of~$\widehat{\fg}_k$
truncated at weight~$h$, which is genus-independent. Equivalently,
the weight-$h$ enrichment block is the same finite direct sum of
Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
genus~$1$, indexed by the finitely many mode patterns.

\medskip
\emph{Step~2: Whitehead acyclicity of the enrichment.}

The $d_1^{\mathrm{PBW}}$ differential (Lie bracket residue)
acts on the enrichment through the $\fg$-module factor~$M_h$,
leaving the $H^{1,0}(\Sigma_g)$ factor unchanged:
\[
d_1^{\mathrm{PBW}}\colon
M_h \otimes H^{1,0}(\Sigma_g)
\;\longrightarrow\;
M_{h} \otimes H^{1,0}(\Sigma_g).
\]
Thus the enrichment complex at weight~$h$ is
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

exec
/bin/zsh -lc "sed -n '1344,1360p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
\bigl(C^*(\fg,\, M_h),\, d_{\mathrm{CE}}\bigr)
\;\otimes_{\bC}\;
H^{1,0}(\Sigma_g)
\]
where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
argument is again applied to the finite-dimensional semisimple
Lie algebra~$\fg$ on each weight-graded piece, not to the
truncated current algebra that records the mode cutoff.

Since $\fg$ is semisimple, the
Whitehead--Chevalley--Eilenberg theorem gives
$H^q(\fg, N) = 0$ for all $q \geq 0$ and any
finite-dimensional $\fg$-module~$N$ with no trivial
summand. Decompose $M_h = M_h^{\fg} \oplus
M_h^{\mathrm{non\text{-}triv}}$ under~$\fg$. Then:
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

exec
/bin/zsh -lc "sed -n '1804,1819p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

exec
/bin/zsh -lc "sed -n '1819,1836p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Decompose $M_h = M_h^{\fg} \oplus M_h^{\mathrm{non\text{-}triv}}$
into $\fg$-invariant and non-trivial summands.

\emph{Non-trivial summands.}
The $d_1^{\mathrm{PBW}}$ differential
(Lie bracket residue from the $(0)$-products of the generators)
acts on the enrichment through the $\fg$-module
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
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

exec
/bin/zsh -lc "sed -n '1836,1844p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

codex
The local reread is clean. I’m running a final grep on the modified file for common forbidden prose patterns and em dashes, then I’ll close with a fixed/blocked accounting.
exec
/bin/zsh -lc "rg -n \"—|---|\\b(moreover|additionally|notably|remarkably|interesting(?:ly)?|furthermore|delve|leverage|tapestry)\\b\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Whitehead reduction in the PBW proof|truncated current algebra|Routing remark|thm:genus-universality|thm:family-index" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
490:\textup{(}Theorem~\textup{\ref{thm:genus-universality})}; the
1021:The truncated current algebra $\fg \otimes V_h$
1208:\begin{remark}[Whitehead reduction in the PBW proof]
1209:For fixed conformal weight~$h$, the truncated current algebra
1353:truncated current algebra that records the mode cutoff.
2461: (Theorem~\ref{thm:genus-universality}).
2568:(Theorem~\ref{thm:genus-universality}).
2752:\emph{Routing remark.}
2756:Theorem~\ref{thm:genus-universality} identifies that trace with
2757:$\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
2759:reverse dependence from Theorem~\ref{thm:family-index} back to
2760:Theorem~\ref{thm:genus-universality}.
2761:Part~(i) is Theorem~\ref{thm:genus-universality} for
2769:Theorem~\ref{thm:genus-universality}(ii).
2833:Theorem~\ref{thm:genus-universality}; the second arrow is the
2835:series. In particular, Theorem~\ref{thm:family-index} is downstream of
2840:Theorem~\ref{thm:genus-universality}); generating function via
2845:to $\kappa\cdot(\hat{A}(ix)-1)$ (Theorem~\ref{thm:family-index}).
3213:Theorem~\ref{thm:genus-universality}. The GUE free energy
3374:Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
 succeeded in 52ms:
3595:% ----------------------------------------------------------------
3597:% ----------------------------------------------------------------
3602:% ---- D_A box ----
3608:% ---- Decomposition ----
3612:% ---- d_0 + Theta ----
3624:% ---- Implication arrow ----
3629:% ---- MC equation ----
3635:% ---- Labels ----
3646:% ---- Shadow projections ----
9962:% ----------------------------------------------------------------
9964:% ----------------------------------------------------------------
11647: & $\checkmark$ & --- & --- \\
11649: & $\checkmark$ & $\checkmark$ & --- \\
11783: precisely what makes the genus expansion interesting.
12027:% ----------------------------------------------------------------
12029:% ----------------------------------------------------------------
12033:% ---- Extension tower (left column) ----
12052:% ---- Vertical arrows ----
12058:% ---- Obstruction labels (left) ----
12069:% ---- Shadow depth classes (right column) ----
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization


thinking
**Running targeted checks**

I found that the grep for forbidden patterns revealed many existing comment separators and table entries marked as `---`, which are not from my patch. It's not an ideal situation, since it means there are pre-existing `---` in other parts of the file that are unrelated to my edits. I could run a more targeted grep to confirm that there are no new problems near the edits. So, let's verify by focusing only on the areas I touched!
codex
The full-file grep exposed pre-existing `---` table/comment separators elsewhere in this chapter, outside the edited regions. I’m doing one narrow pass on the touched blocks only so the close-out can distinguish local verification from unrelated legacy noise.
exec
/bin/zsh -lc "sed -n '1015,1065p;1204,1215p;1324,1355p;1819,1840p;2750,2762p' chapters/theory/higher_genus_modular_koszul.tex | rg -n \"—|---|\\b(moreover|additionally|notably|remarkably|interesting(?:ly)?|furthermore|delve|leverage|tapestry)\\b\"" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1018,1045p;1204,1216p;1324,1352p;1820,1838p;2750,2762p'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 50ms:
  1018	with only finitely many mode labels.
  1019	Write
  1020	$V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
  1021	The truncated current algebra $\fg \otimes V_h$
  1022	records which modes can occur at weight~$h$; Whitehead is
  1023	not applied to this non-semisimple Lie algebra. Its role is
  1024	only to enumerate the finitely many mode patterns~$\nu$
  1025	that occur in weight~$h$.
  1026	After separating the mode data from the $\fg$-labels,
  1027	the weight-$h$ enrichment block is a finite direct sum of
  1028	Chevalley--Eilenberg complexes
  1029	$C^*(\fg, M_{h,\nu})$, indexed by the finitely many
  1030	mode patterns~$\nu$ of total weight~$h$. Each
  1031	$M_{h,\nu}$ is a finite-dimensional $\fg$-module with
  1032	diagonal adjoint action on the $\fg$-labels and trivial
  1033	action on the mode and $H^1(E_\tau)$ factors. Equivalently,
  1034	\[
  1035	\mathcal{E}_1^{*,h}
  1036	\;\cong\;
  1037	C^*(\fg, M_h),
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization


thinking
**Updating plan after grep**

Okay, so the targeted grep didn't return any output, which is actually a good sign since it means it didn’t find what I was looking for. Now, I need to think about updating my approach or plan moving forward. It's always a good idea to be flexible and adjust as new information comes in. Let’s consider the next steps I should take based on this outcome.
Plan update
The local patch is in, the touched proof surfaces reread coherently, and the narrow forbidden-pattern grep on the edited blocks returned no matches. The only full-file grep hits were pre-existing `---` comment/table separators elsewhere in the chapter.
  ✓ Inspect the Whitehead/PBW blocks and Theorem D routing blocks in the target file plus required repo context
  ✓ Patch the Whitehead/PBW passages with an explicit reduction to finite-dimensional fg-modules and add a local clarifying remark
  ✓ Patch the Theorem D proof with a one-way routing remark from shadow tower to genus universality to family index
  ✓ Re-read touched regions and grep the modified file for forbidden or stale patterns
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

exec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516..9c83fc1 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@ Write
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@ C^*(\fg, M_h),
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

collab close_agent(call_dErxViOCjnglhp7IzfoATJoh)
  receiver: 019d862b-7c8a-7370-a0d9-9ef2fae19bb8
close_agent(call_dErxViOCjnglhp7IzfoATJoh) completed: "- **Whitehead justification near the PBW spectral sequence (lines ~1010‑1035, 1290‑1350, 1768‑1840 in `chapters/theory/h…":
  receiver: 019d862b-7c8a-7370-a0d9-9ef2fae19bb8
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

codex
Edited [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1021) only.

- `FIXED` MC1 PBW / Whitehead justification at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1021), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1208), [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1326), and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1834). I made the reduction explicit: `\fg \otimes V_h` only records finitely many mode patterns, each weight block is rewritten as a finite direct sum of `C^*(\fg, M_{h,\nu})`, and Whitehead is applied only to the finite-dimensional semisimple Lie algebra `\fg` acting on those modules. I also added a short local remark freezing that point.
- `FIXED` Theorem D routing at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2751). I added an explicit routing remark: the independent anchor is the bar-intrinsic shadow tower, then `thm:genus-universality`, then `thm:family-index`, with no reverse dependence.

Verification: I re-read the touched regions for coherence, did not change any `\label` or `\ref`, and ran a targeted forbidden-pattern grep on the edited blocks with no hits. A full-file grep still shows pre-existing `---` comment/table separators elsewhere in the chapter, outside these edits. I did not run a TeX build.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 1b11516b7389bfd1e550b617bfbaf71af94cc294..9c83fc1a70024df136dd323e19d7da00a4a7933f
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -1020,7 +1020,9 @@
 $V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}]$.
 The truncated current algebra $\fg \otimes V_h$
 records which modes can occur at weight~$h$; Whitehead is
-not applied to this non-semisimple Lie algebra.
+not applied to this non-semisimple Lie algebra. Its role is
+only to enumerate the finitely many mode patterns~$\nu$
+that occur in weight~$h$.
 After separating the mode data from the $\fg$-labels,
 the weight-$h$ enrichment block is a finite direct sum of
 Chevalley--Eilenberg complexes
@@ -1037,7 +1039,10 @@
 M_h := \bigoplus_\nu M_{h,\nu},
 \]
 and $d_1^{\mathrm{PBW}}$ is the corresponding
-Chevalley--Eilenberg differential. The map to the concentrated
+Chevalley--Eilenberg differential for the finite-dimensional
+semisimple Lie algebra~$\fg$. Thus the Whitehead step is carried
+out weight by weight on the $\fg$-modules~$M_{h,\nu}$, not on
+$\fg \otimes V_h$. The map to the concentrated
 genus-$0$ sector is one of the $\fg$-equivariant components of this
 same differential.
 
@@ -1200,6 +1205,17 @@
 are weight-independent), completing the proof.
 \end{proof}
 
+\begin{remark}[Whitehead reduction in the PBW proof]
+For fixed conformal weight~$h$, the truncated current algebra
+$\fg \otimes V_h$ only records which modes can occur. The actual
+Whitehead input appears after rewriting the weight-$h$ enrichment
+block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$,
+with~$\fg$ acting diagonally on the $\fg$-labels and the mode and
+$H^1$ factors treated as passive coefficients. No vanishing statement
+is invoked for the non-semisimple Lie algebra $\fg \otimes V_h$
+itself.
+\end{remark}
+
 \begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
 \label{cor:unconditional-genus1-km}
 \index{modular Koszul chiral algebra!unconditional genus-1}
@@ -1307,7 +1323,10 @@
 and the regular forms from $H^{1,0}(\Sigma_g)$ are
 smooth across these divisors. The module~$M_h$ is
 determined solely by the OPE structure of~$\widehat{\fg}_k$
-truncated at weight~$h$, which is genus-independent.
+truncated at weight~$h$, which is genus-independent. Equivalently,
+the weight-$h$ enrichment block is the same finite direct sum of
+Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
+genus~$1$, indexed by the finitely many mode patterns.
 
 \medskip
 \emph{Step~2: Whitehead acyclicity of the enrichment.}
@@ -1328,7 +1347,10 @@
 H^{1,0}(\Sigma_g)
 \]
 where $C^*(\fg, M_h)$ is the Chevalley--Eilenberg
-complex of~$\fg$ with coefficients in~$M_h$.
+complex of~$\fg$ with coefficients in~$M_h$. Thus the Whitehead
+argument is again applied to the finite-dimensional semisimple
+Lie algebra~$\fg$ on each weight-graded piece, not to the
+truncated current algebra that records the mode cutoff.
 
 Since $\fg$ is semisimple, the
 Whitehead--Chevalley--Eilenberg theorem gives
@@ -1809,6 +1831,9 @@
 \;\otimes_{\bC}\;
 H^{1,0}(\Sigma_g).
 \]
+Here the mode truncation has already been absorbed into the
+finite-dimensional coefficient module~$M_h^{\mathrm{non\text{-}triv}}$,
+so Whitehead is applied only to the semisimple Lie algebra~$\fg$.
 By the Whitehead--Chevalley--Eilenberg vanishing theorem,
 $H^q(\fg,\, N) = 0$ for all $q \geq 0$ and any
 finite-dimensional $\fg$-module~$N$ with no trivial summand,
@@ -2724,11 +2749,15 @@
 \end{theorem}
 
 \begin{proof}
-The dependency route is one-way: the bar-intrinsic shadow tower of
+\emph{Routing remark.}
+The dependency route is one-way and has an independent anchor:
+the bar-intrinsic shadow tower of
 Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
 Theorem~\ref{thm:genus-universality} identifies that trace with
 $\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
-subsequent GRR repackaging of the resulting genus series.
+subsequent GRR repackaging of the resulting genus series. There is no
+reverse dependence from Theorem~\ref{thm:family-index} back to
+Theorem~\ref{thm:genus-universality}.
 Part~(i) is Theorem~\ref{thm:genus-universality} for
 uniform-weight algebras. For multi-generator algebras
 ($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization

tokens used
102,111
