# A08_cobar_construction (432s)

**Status**
- `FIXED` the `thm:verdier-bar-cobar` surface in [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1348). The Verdier item now states
  `\mathbb{D}_{\operatorname{Ran}}(\bar B^{\mathrm{ch}}(\mathcal A)) \simeq (\mathcal A)^!_\infty`
  as a factorization algebra on `\operatorname{Ran}(X)`, and Step 4 was aligned to the same algebra-level identification at [1421](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1421).
- `FIXED` the later affine/Kac--Moody restatement in [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2221). The corollary now says
  `\mathbb{D}_{\operatorname{Ran}}(\bar B^{\mathrm{ch}}(\widehat{\mathfrak g}_k)) \simeq (\widehat{\mathfrak g}_k)^!_\infty \simeq \widehat{\mathfrak g}_{k'}`
  at [2227](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2227), and the proof now cites the same Theorem A convention at [2253](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2253).
- `FIXED` surrounding local prose so the file no longer contradicts itself: the opening “three functors” remark at [72](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:72) and the Poincare--Verdier restatement at [2038](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2038) now use the same `(\cA)^!_\infty` convention.

Verification: I re-read all patched spans, `git diff --check` is clean, and grep on the modified file returned no remaining hits for the old target patterns `\barB(\cA^!)`, `\bar{B}^{\mathrm{ch}}(\cA^!)`, `gives the bar of the Koszul dual`, `\Omega^{\text{ch}}(\mathcal A^!)`, or `\mathbb D(\bar B^{\text{ch}}(\mathcal A))`.

Pending scope note: repo grep surfaced potential same-convention collision surfaces outside the assigned file, notably [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1972), [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3266), and [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:11241). I did not edit those because this task was scoped to `chapters/theory/cobar_construction.tex`.


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
session id: 019d8635-c9a6-7d71-ab7f-0f5cc9237e96
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


TARGET: chapters/theory/cobar_construction.tex

FINDING: Lines ~1347-1348 and ~2207-2219: Verdier convention must be consistent with
Theorem A after the chiral_koszul_pairs.tex rectification. The Verdier identification
should be at the ALGEBRA level (post-D_Ran), not coalgebra.

FIX: Read the current statement of thm:verdier-bar-cobar. Verify it says
D_Ran(bar B(A)) = (A)^!_inf as factorization algebra. If it says coalgebra, fix it.
mcp startup: no servers
codex
Using `beilinson-rectify` for a tightly scoped theorem-surface repair in [chapters/theory/cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex). I’m reading the required constitutional files, the theorem surface, and the current Verdier/Koszul statements before patching the minimum necessary lines.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
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

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 88ms:
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
 succeeded in 148ms:
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


thinking
**Inspecting protocols**

Okay, I need to prepare for the pre-edit verification protocol, placing it in a commentary block because of the hot zone four-functor. I’m considering whether to provide a list of four objects first in the commentary. I should probably start by reviewing the source for accuracy. It’s important to carefully inspect the target and any dependencies involved in this process to ensure everything is clear and well-organized!
codex
I’ve loaded the governing surfaces and I’m now checking the exact theorem/proof lane around `thm:verdier-bar-cobar`, plus the nearby restatement later in the file and the current rectified wording in `chiral_koszul_pairs.tex`. After that I’ll patch only the object-level mismatch if it is still claiming a coalgebra after Verdier duality.
exec
/bin/zsh -lc 'rg -n "thm:verdier-bar-cobar|Verdier|D_Ran|factorization algebra|coalgebra|cobar" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1290,1385p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1:\chapter{The geometric cobar complex}
2:\label{chap:cobar-construction}
5:factorization coalgebra $\barB(\cA)$ from which no multiplication
6:is directly visible. The cobar complex $\Omega(\cC)$ is the
7:reconstruction machine that recovers~$\cA$ from this coalgebraic
17:$\eta_{ij} = d\log(z_i - z_j)$; cobar integrates distributional
20:$j_*$ versus $j_!$) is the Verdier exchange on
24:coalgebra~$\cC$ on~$X$ valued in holonomic $\cD$-modules, the
25:\emph{geometric cobar complex} is
30:(Definition~\ref{def:geom-cobar-intrinsic}), where
31:$\cC^\vee = \mathbb{D}_X(\cC)$ is the $\cD$-module Verdier dual
33:is the open inclusion. The cobar differential is the Verdier
35:$d_{\mathrm{cobar}} := \mathbb{D}(d_{\mathrm{bar}})$.
38:cobar kernel as the distributional partner of the logarithmic
41:Theorem~\ref{thm:schwartz-kernel-cobar} is the $j_!$-side of the
45:(Theorem~\ref{thm:bar-cobar-adjunction}).
50:(Chapter~\ref{chap:bar-cobar-adjunction}). The total bar differential
51:$d_{\mathrm{bar}}^2 = 0$ remains nilpotent. The cobar functor
52:applied to the bar coalgebra viewed as an FCom-algebra
55:(Proposition~\ref{prop:cobar-modular-shadow}).
 succeeded in 54ms:

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

\subsection{Verdier duality on bar and cobar}
exec
/bin/zsh -lc "sed -n '2170,2245p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:verdier-bar-cobar|D_Ran\\(|Verdier dual|factorization algebra|coalgebra\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
where the first term comes from the double-pole $k(J^a,J^b)/(z-w)^2$.
Applying $m_1$ twice and using the Jacobi identity gives
\[
m_1^2(J^a \boxtimes J^b \cdot \eta_{12}) = (k + h^\vee) \cdot (\text{adjoint Casimir}),
\]
since the Killing form contraction $\sum_{c,d} f^{ac}{}_d f^{bc}{}_d = 2h^\vee \cdot \delta^{ab}$ (with long roots normalized to length $2$). The factor $h^\vee$ is the eigenvalue of the adjoint Casimir; the total coefficient $k + h^\vee$ vanishes precisely at critical level.

For $\mathfrak{g} = \mathfrak{sl}_2$ with $h^\vee = 2$, the explicit computation:
$m_1(e \boxtimes f \cdot \eta_{12}) = k \cdot \mathbf{1} + h$ (from
$e_{(0)}f = h$ and $e_{(1)}f = k$). Applying $m_1$ again:
$m_1(h) = 0$ (since $h$ is primitive) and
$m_1(\mathbf{1}) = 0$, but the composite $m_1^2$ on degree-$2$
elements picks up the adjoint action:
$m_1^2(e \boxtimes f \cdot \eta_{12}) = [h, k \cdot \mathbf{1} + h]_{\mathrm{bar}}
= k \cdot (\text{ad-action of Casimir}) + 2h = (k+2) \cdot \partial h$.
\end{proof}

\begin{remark}[Feigin--Frenkel center at critical level]
\label{rem:feigin-frenkel-center}
\index{Feigin--Frenkel center}
 succeeded in 52ms:
11:algebras over a field: the bar complex is a tensor coalgebra on a
14:duality exchanges quadratic algebras with quadratic coalgebras.
51:Verdier duality on $\Ran(X)$, connecting $\barB_X(\cA)$ with the
52:homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
57:adjunction achieves (a) but not (b) or (c); Verdier duality alone
160:produces the coalgebra $\bar{B}(\mathcal{H}_k)
193:its bar coalgebra. The bridge between them is a \emph{twisting morphism},
207:\item a conilpotent complete factorization coalgebra
246:the coalgebra element, and $\tau$ evaluates $c_{(1)}$ against the
385:is a quasi-isomorphism of classical conilpotent coalgebras. By the
423: coalgebras.
474:For a conilpotent complete factorization coalgebra $\cC$
507:The second bijection sends $\tau$ to the coalgebra morphism
510:coalgebra ensures uniqueness of factorization.
553: dual pair, Verdier duality sends the bar coalgebra of one side
554: to the dual factorization algebra of the other.
557:$\mathrm{A}_1$ extracts the dual coalgebra;
568:coalgebra~$C$ and a twisting morphism $\tau \colon C \to \cA$.
570:there exists a unique coalgebra map
584:is the cofree conilpotent coalgebra on the desuspended
 succeeded in 51ms:
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

thinking
**Looking into chiral koszul pairs**

I'm focusing on the relevant part in chiral_koszul_pairs, especially near theorem A or the bar-coalgebra identity. I'll need to locate lines around 3638 or so. It seems that searching for the terms "conv:bar-coalgebra-identity" and "theorem" might help me pinpoint the information I need. I’ll make sure to gather all the details carefully to ensure I'm getting it right!
codex
The target surface is now isolated. I’ve confirmed the local theorem already says “as factorization algebras” at one spot, so I’m checking the restated Theorem A convention and the later corollary proof to see whether any remaining wording still identifies the Verdier image as a coalgebra instead of the post-`D_{\operatorname{Ran}}` algebra.
exec
/bin/zsh -lc "rg -n \"conv:bar-coalgebra-identity|bar-coalgebra-identity|A_\\"'^!_'"\\infty|factorization algebra|homotopy dual factorization algebra|D_\\\\operatorname\\{Ran\\}\\(\\\\bar\\{B\\}|D_\\\\operatorname\\{Ran\\}\\(\\\\barB|Verdier intertwining\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3600,3815p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:conv:bar-coalgebra-identity|bar-coalgebra-identity|A_\^!_\infty|factorization algebra|homotopy dual factorization algebra|D_\operatorname\{Ran\}\(\bar\{B\}|D_\operatorname\{Ran\}\(\barB|Verdier intertwining)
                                                                ^^
error: unrecognized escape sequence
 succeeded in 52ms:
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
/bin/zsh -lc "sed -n '666,710p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\simeq \Omega_X(\cC_2)
\]
is supplied by Theorem~\ref{thm:verdier-bar-cobar} together with
the counit quasi-isomorphism
$\Omega_X(\cC_2) \xrightarrow{\sim} \cA_2$ from
Theorem~\ref{thm:fundamental-twisting-morphisms}.
The Heisenberg pair
$(\mathcal{H}_k, \mathrm{Sym}^{\mathrm{ch}}(V^*))$ is the
prototype (\S\ref{sec:frame-koszul-dual}).

\smallskip\noindent
In particular, each algebra~$\cA_i$ in a chiral Koszul pair is a
Koszul chiral algebra in the sense of
Definition~\textup{\ref{def:koszul-chiral-algebra}}, and hence lies on
the Koszul locus~$\operatorname{Kosz}(X)$
(Definition~\textup{\ref{def:koszul-locus}}).
\end{definition}


\begin{example}[Heisenberg specialization]\label{ex:heisenberg-koszul-pair}

thinking
**Searching for coalgebra identification**

I should consider searching in the target file for terms like `\mathbb{D}_{\operatorname{Ran}}\bigl(` or `D_Ran`. This might help highlight any other coalgebra identifications in the file. I think using a simpler approach, like `rg`, could make this search easier. This way, I can quickly find what I'm looking for without complicating the process too much!
codex
I’ve found the actual mismatch: the theorem surface near `thm:verdier-bar-cobar` is already close to the corrected convention, but the later “level-shifting via Verdier duality” corollary still states `\mathbb{D}_{\operatorname{Ran}}(\bar B^{\mathrm{ch}}(\widehat{\mathfrak g}_k)) \simeq \bar B^{\mathrm{ch}}(\widehat{\mathfrak g}_{k'})`, which is exactly the pre-rectification coalgebra-level claim. I’m checking one more local dependency, then I’ll patch that corollary and align the theorem wording with `(\mathcal A)^!_\infty` explicitly.
exec
/bin/zsh -lc "rg -n \"D_\\{\\\\operatorname\\{Ran\\}\\}|D_\\\\operatorname\\{Ran\\}|\\\\mathbb\\{D\\}_\\{\\\\operatorname\\{Ran\\}\\}|\\\\mathbb\\{D\\}_\\\\operatorname\\{Ran\\}.*bar|bar coalgebra.*Verdier duality|Verdier duality.*bar coalgebra\" chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:D_\{\operatorname\{Ran\}\}|D_\operatorname\{Ran\}|\mathbb\{D\}_\{\operatorname\{Ran\}\}|\mathbb\{D\}_\operatorname\{Ran\}.*bar|bar coalgebra.*Verdier duality|Verdier duality.*bar coalgebra)
           ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "sed -n '1408,1435p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2234,2260p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
e^{-|u|^2} \\
&= \int \frac{du}{u} \wedge \frac{1}{\pi} e^{-|u|^2} \\
&= \frac{1}{2\pi i} \oint_{|u|=1} \frac{du}{u} \quad \text{(by residue theorem)} \\
&= 1
\end{align*}

The pairing between residues and delta functions is therefore exact.

\emph{Step 4: Verdier duality realization}

The pairing establishes an isomorphism:
\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]

where $\mathbb{D}$ is the Verdier dualizing functor.

\emph{Non-degeneracy.}
At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
$\langle \eta_{ij}, \delta(z_i - z_j) \rangle = 1$. For $n > 1$,
non-degeneracy follows by induction using the coalgebra structure: the
comultiplication on $\bar{B}^n$ decomposes an $n$-point integrand into
 succeeded in 51ms:
\end{corollary}

\begin{proof}
The Verdier intertwining
(Theorem~\ref{thm:bar-cobar-isomorphism-main},
Convention~\ref{conv:bar-coalgebra-identity}) identifies
$\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
$k' = -k - 2h^\vee$: Verdier duality on Ran negates the
curvature element, sending
$m_0 = (k+h^\vee)\Omega/(2h^\vee)$
(Proposition~\ref{prop:km-bar-curvature}) to
$m_0' = -(k+h^\vee)\Omega/(2h^\vee)
= (k'+h^\vee)\Omega/(2h^\vee)$ where $\Omega$ is the Casimir
element. Since the simple-pole data $f^{ab}{}_c$ (the Lie
bracket) is preserved by Verdier duality and the double-pole
coefficient is determined by the curvature, the dual algebra
has OPE

thinking
**Evaluating proof correction**

I’m noticing that the proof I’m reviewing seems to have an error. It identifies D_Ran(bar B(A)) as equivalent to bar B(A^!), but I wonder if it should actually be A^!_∞. That’s definitely a minimum fix needed. To get a clearer understanding, I think I should look up the convention for "conv:bar-coalgebra-identity" as the wording could be relevant here. I’ll dig into that to see if it offers any insight!
exec
/bin/zsh -lc 'rg -n "conv:bar-coalgebra-identity|bar-coalgebra-identity" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1132:% viewed as a graded coalgebra (Convention~\ref{conv:bar-coalgebra-identity}).
3801:Convention~\ref{conv:bar-coalgebra-identity}), with

thinking
**Considering conventions across the repo**

I’m wondering if the convention is defined somewhere else and not just in this file. It could be that searching across the entire repository might provide enough information. I think that could be a good step to take! I want to make sure I’m being thorough, so checking the broader context is key here. Let’s explore that idea further to find the right conventions!
exec
/bin/zsh -lc "rg -n \"conv:bar-coalgebra-identity|bar-coalgebra-identity\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:2117:Convention~\textup{\ref{conv:bar-coalgebra-identity}):}
chapters/connections/holomorphic_topological.tex:130: Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)};
chapters/connections/concordance.tex:453:(Convention~\ref{conv:bar-coalgebra-identity}):
chapters/theory/bar_construction.tex:81:\label{conv:bar-coalgebra-identity}
chapters/theory/bar_construction.tex:2274:(here $s^{-1}V$ is the desuspension $|s^{-1}v| = |v| - 1$ of Convention~\ref{conv:bar-coalgebra-identity}, matching the desuspension in $T^c(s^{-1}\bar{\mathcal{A}})$), and similarly for $G$, giving a canonical isomorphism $\eta_V\colon F(\text{Free}^{\text{ch}}(V)) \xrightarrow{\sim} G(\text{Free}^{\text{ch}}(V))$.
chapters/theory/algebraic_foundations.tex:1534: (Convention~\ref{conv:bar-coalgebra-identity}). This is a
chapters/theory/algebraic_foundations.tex:1980:(Convention~\ref{conv:bar-coalgebra-identity}): it lives on
chapters/theory/nilpotent_completion.tex:49:For these, the bar construction $\bar{B}(\cA)$ remains a perfectly well-defined dg coalgebra (it \emph{is} the Koszul dual coalgebra in the derived sense, Convention~\ref{conv:bar-coalgebra-identity}), but its cohomology does not concentrate in a single degree, so the classical Koszul dual algebra $\cA^!$ is not directly visible. $I$-adic completion resolves this: the completed bar coalgebra $\widehat{\bar{B}}(\cA)$ recovers $\cA^!$ as a graded piece of a filtered inverse limit.
chapters/theory/configuration_spaces.tex:108:Convention~\textup{\ref{conv:bar-coalgebra-identity}}): the Verdier
chapters/theory/cobar_construction.tex:73: (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
chapters/theory/cobar_construction.tex:1675:(Convention~\ref{conv:bar-coalgebra-identity}).
chapters/theory/cobar_construction.tex:2206:% invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
chapters/theory/cobar_construction.tex:2210:Convention~\ref{conv:bar-coalgebra-identity}) applied to the
chapters/theory/cobar_construction.tex:2239:Convention~\ref{conv:bar-coalgebra-identity}) identifies
chapters/theory/poincare_duality_quantum.tex:81:(Convention~\ref{conv:bar-coalgebra-identity}), not a tautology \emph{Caution}: the cobar construction $\Omega(\bar{B}(\mathcal{A}))$
chapters/theory/bar_cobar_adjunction_inversion.tex:143:Applying the \emph{cobar} functor to this coalgebra recovers the \emph{original} algebra: $\Omegach(\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)) \simeq \widehat{\mathfrak{g}}_k$ (bar-cobar inversion, Theorem~\ref{thm:bar-cobar-inversion-qi}). The \emph{Koszul dual algebra} $\widehat{\mathfrak{g}}_k^! \simeq \widehat{\mathfrak{g}}_{-k-2h^\vee}$ is obtained by the distinct route of Verdier duality: $\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k) \simeq (\widehat{\mathfrak{g}}_k^!)_\infty$ (Convention~\ref{conv:bar-coalgebra-identity}).
chapters/theory/bar_cobar_adjunction_inversion.tex:3268: \textup{(}Convention~\ref{conv:bar-coalgebra-identity}\textup{)}.
chapters/theory/chiral_modules.tex:639:of~$\cA$ (Convention~\ref{conv:bar-coalgebra-identity}),
chapters/theory/chiral_modules.tex:721:Convention~\ref{conv:bar-coalgebra-identity},
chapters/theory/en_koszul_duality.tex:1448:(Theorem~A, Convention~\textup{\ref{conv:bar-coalgebra-identity}})

thinking
**Looking into conventions**

I think I need to read the convention definition from bar_construction.tex to understand the precise language being used. It seems like gaining clarity about the conventions will help me better grasp the context and ensure I'm interpreting everything correctly. I'll focus on identifying any key terms or phrases that are critical for understanding the topic at hand. This way, I can be more accurate in my analysis or discussion.
exec
/bin/zsh -lc "sed -n '60,110p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{tabular}
\end{center}

\noindent
Theorem~\ref{thm:bar-nilpotency-complete} assembles these three
components into the full genus-$0$ differential $\dzero$
and proves $\dzero^2 = 0$; the key input is the Arnold relation
(Theorem~\ref{thm:arnold-three},
Remark~\ref{rem:costello-gwilliam-factorization}).

\smallskip
\noindent\textit{Notation.}
Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.

\medskip

\begin{convention}[Set notation and ordering]\label{conv:set-notation}
Throughout this chapter: collision divisors are $D_{ij}$ with $i < j$ (indices in increasing order); the hat notation $\widehat{ij}$ denotes \emph{omission} of both factors $\phi_i$ and $\phi_j$ after applying the OPE (we write $\widehat{ij}$ for the collision pattern itself, and $\widehat{\phi_i, \phi_j}$ when listing omitted terms in a tensor product).
\end{convention}

codex
Pre-edit verification for this hot-zone surface:

```text
% FOUR OBJECTS:
% 1. B(A) = bar coalgebra = T^c(s^{-1} A-bar) with deconcatenation + twist
% 2. A^i = H^*(B(A)) = dual coalgebra (Koszul cohomology of bar)
% 3. A^! = ((A^i)^v) = dual ALGEBRA (linear or Verdier dual)
% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk

claim surface: chapters/theory/cobar_construction.tex
labels: thm:verdier-bar-cobar, cor:level-shifting-part1
target convention: D_Ran(bar B(A)) identifies with (A)^!_infty as a factorization algebra; it is not a coalgebra-level identification
forbidden conflation check: "D_Ran(B(A)) is the cobar complex" avoided
forbidden conflation check: "D_Ran(B(A)) is a bar coalgebra" rejected on this surface
surrounding context check: bar-cobar inversion remains Omega(B(A)) ~ A and is distinct from Verdier/Koszul duality
verdict: ACCEPT
```

thinking
**Inspecting patch details**

I need to apply a patch and inspect the exact lines that I might need to edit carefully. I'm thinking about patching the theorem property, proof in Step 4, corollary statement, and some comments. Maybe I should also look at intro remark lines 73-76? There’s a remark around line 72 that might mention Verdier duality and bar coalgebra. So, I'll be inspecting the lines between 60 and 90 for more context.
codex
I’ve finished the diagnosis. The patch is limited to the theorem item, its Step 4 restatement, and the later affine-level corollary so the file consistently treats `\mathbb D_{\Ran}(\bar B_X(\mathcal A))` as the homotopy dual factorization algebra, with bar-cobar inversion left untouched.
exec
/bin/zsh -lc "sed -n '60,95p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2198,2248p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[Three functors on the bar coalgebra: cobar is NOT the Koszul dual]
\label{rem:cobar-three-functors}
Before entering the construction, we fix a critical distinction that
pervades the chapter. Three functors act on the bar coalgebra
$\barB(\cA)$, producing three different objects; confusing any two
produces false statements.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Cobar / bar-cobar inversion}
 (Theorem~B, Corollary~\ref{cor:bar-cobar-inverse}):
 \[\Omegach(\barB(\cA)) \;\xrightarrow{\sim}\; \cA\qquad
 \text{(recovers $\cA$ itself: a round-trip, not a duality)}.\]
\item \emph{Verdier duality on $\operatorname{Ran}(X)$}
 (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
 \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
 \barB(\cA^!)\qquad
 \text{(gives the Koszul dual's bar coalgebra)}.\]
\item \emph{Chiral derived centre / Hochschild cochains}
 (Theorem~H):
 \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 succeeded in 51ms:
\label{cor:level-shifting-part1}
\index{Feigin--Frenkel duality}
\index{level!shifted}
% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
% duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
% inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
% Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
% invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
the Verdier intertwining
(Theorem~\ref{thm:bar-cobar-isomorphism-main},
Convention~\ref{conv:bar-coalgebra-identity}) applied to the
curved bar coalgebra of
Proposition~\ref{prop:km-bar-curvature} gives
\begin{equation}\label{eq:level-shifting-part1}
\mathbb{D}_{\operatorname{Ran}}\bigl(
 \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
\;\simeq\;
\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
codex
I found one more local sentence in the same file that still states the old rule in plain prose: the opening “three functors on the bar coalgebra” remark says Verdier duality “gives the bar of the Koszul dual.” That would leave the file self-contradictory after the theorem fix, so I’m correcting that sentence in the same patch.
exec
/bin/zsh -lc 'rg -n -F "gives the bar of the Koszul dual" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\\\barB(\\\\cA"'^!)" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
92:gives the bar of the Koszul dual.''
 succeeded in 52ms:
75: \barB(\cA^!)\qquad
exec
/bin/zsh -lc 'rg -n -F "factorization algebra" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\\\bar{B}"'^{'"\\\\mathrm{ch}}(\\\\cA"'^!)" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
1348: \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
1788:\begin{remark}[Costello--Gwilliam factorization algebras]\label{rem:CG-factorization-detailed}
1814:where $\mathfrak{U} = \{U_{\sigma}\}$ is the open cover of $\overline{C}_n(X)$ by coordinate charts and $\mathcal{F}_{\mathcal{C}}$ is the factorization algebra associated to $\mathcal{C}$.
1818:The factorization algebra $\mathcal{F}_{\mathcal{C}}$ on $X$ is defined by the assignment $U \mapsto \mathcal{F}_{\mathcal{C}}(U) = \Omega(\mathcal{C}|_U)$, with factorization structure maps $\mathcal{F}_{\mathcal{C}}(U_1) \otimes \mathcal{F}_{\mathcal{C}}(U_2) \to \mathcal{F}_{\mathcal{C}}(U_1 \sqcup U_2)$ for disjoint opens, given by the cobar product. This is a cosheaf on the Ran space $\operatorname{Ran}(X)$, hence in particular a precosheaf on $X$.
1824:On each chart $U_\sigma$, the factorization algebra $\mathcal{F}_{\mathcal{C}}|_{U_\sigma}$ is computed by the cobar complex with local coordinates. The cobar differential $d_\Omega$ on $U_\sigma$ uses the coproduct $\bar{\Delta}$ of $\mathcal{C}$ together with the local propagator $\eta_{ij} = d\log(z_i - z_j)$. On overlaps $U_\sigma \cap U_\tau$, the transition data is encoded by the change-of-coordinate forms, which are $\bar{\partial}$-exact on the holomorphic curve $X$.
 succeeded in 53ms:
2032:\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
2241:\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra

thinking
**Inspecting theorem details**

I need to take a closer look at theorem p.2027, which involves `\bar{B}^{\mathrm{ch}}(\cA^!)`. It sounds like there could be interesting information or concepts to explore in this theorem. I'll focus on understanding what it says and how it might relate to other topics or implications. This could require some careful reading and consideration on my part to make sure I grasp all the relevant details.
exec
/bin/zsh -lc "sed -n '2024,2040p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\subsection{Poincaré--Verdier duality realization}

\begin{theorem}[Bar-cobar Verdier pairing; \ClaimStatusProvedHere]\label{thm:poincare-verdier}
The bar and cobar constructions are related by the Verdier
intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
\[
\mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
\]
where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
\simeq \cA$ on the Koszul locus
\textup{(}Theorem~B\textup{)}.
The Verdier pairing between bar forms and cobar distributions


thinking
**Clarifying file editing rules**

I need to follow the user's instructions to edit only the assigned file. I can grep across volumes, but I shouldn't change anything else. If there are genuine duplicates, I must note them or leave an explicit pending note. I also need to think about how the network and filesystem access might restrict reading from other directories, though I can read some areas. Ultimately, since I'm focused on one target file, I might not need to grep other volumes for the same incorrect formula.
thinking
**Reviewing cross-volume editing rules**

AGENTS mentions that I should grep before and after editing to check for duplicates, updating them all in the same session, or leave a note for untouched areas. I've already corrected some terms like chiral_koszul_pairs and bar_cobar_adjunction_inversion, but there might be more duplicates to find. I can grep the repository for specific patterns, but since the user asked me to focus only on the assigned file, I'll make a note if I find anything outside of that. I'll gather more details later using a specific search across the repository.

thinking
**Fixing patch issues**

I see that my patch attempt failed, possibly due to a newline issue. It looks like I need to reopen the relevant segments to apply the patch accurately. I might consider using the sed command around the specified ranges: 65-95, 1340-1430, 2027-2038, and 2198-2250. I hope this works better! I'll make sure to double-check my approach this time.
codex
The first patch missed one exact proof hunk because of line wrapping. I’m re-reading the affected spans and applying the same scoped changes with the file’s exact line breaks.
exec
/bin/zsh -lc "sed -n '68,95p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1338,1432p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{itemize}

\emph{Properties of the pairing.}
\begin{enumerate}
\item \emph{Perfect pairing:} Non-degenerate in both arguments (by Lemma~\ref{lem:bar-holonomicity}: each graded piece is a holonomic $\mathcal{D}$-module on $\overline{C}_n(X)$, hence has finite-dimensional stalks, and Verdier duality for holonomic $\mathcal{D}$-modules is an involution~\cite{KS90})
\item \emph{Differential compatibility:} $\langle d_{\text{bar}}\omega, K \rangle 
= -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
\item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
\delta_D \rangle = 1$ for any divisor $D$
\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
 \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
\end{enumerate}
\end{theorem}

\begin{proof}
\emph{Step 1: Well-definedness of the pairing}

Logarithmic forms on $\overline{C}_n(X)$ restrict to distributional 
forms on $C_n(X)$. Explicitly, near a divisor $D = \{z_i = z_j\}$ with local 
coordinate $\epsilon = z_i - z_j$:
 succeeded in 52ms:
\item \emph{Cobar / bar-cobar inversion}
 (Theorem~B, Corollary~\ref{cor:bar-cobar-inverse}):
 \[\Omegach(\barB(\cA)) \;\xrightarrow{\sim}\; \cA\qquad
 \text{(recovers $\cA$ itself: a round-trip, not a duality)}.\]
\item \emph{Verdier duality on $\operatorname{Ran}(X)$}
 (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
 \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
 \barB(\cA^!)\qquad
 \text{(gives the Koszul dual's bar coalgebra)}.\]
\item \emph{Chiral derived centre / Hochschild cochains}
 (Theorem~H):
 \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 \;=\; C^\bullet_{\mathrm{ch}}(\cA, \cA)\qquad
 \text{(the universal bulk / closed-string observables)}.\]
\end{enumerate}
\emph{Cobar is the inverse, not the dual.} Throughout this
chapter $\Omegach$ denotes the bar-cobar inverse functor of
(i); it recovers the algebra from its bar coalgebra. The
Koszul dual $\cA^!$ is obtained by Verdier duality on
$\operatorname{Ran}(X)$, which is a \emph{different} operation on
exec
/bin/zsh -lc "sed -n '2199,2248p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2026,2039p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{Feigin--Frenkel duality}
\index{level!shifted}
% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
% duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
% inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
% Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
% invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
the Verdier intertwining
(Theorem~\ref{thm:bar-cobar-isomorphism-main},
Convention~\ref{conv:bar-coalgebra-identity}) applied to the
curved bar coalgebra of
Proposition~\ref{prop:km-bar-curvature} gives
\begin{equation}\label{eq:level-shifting-part1}
\mathbb{D}_{\operatorname{Ran}}\bigl(
 \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
\;\simeq\;
\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
\qquad k' = -k - 2h^\vee.
 succeeded in 52ms:

\begin{theorem}[Bar-cobar Verdier pairing; \ClaimStatusProvedHere]\label{thm:poincare-verdier}
The bar and cobar constructions are related by the Verdier
intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
\[
\mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
\]
where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
\simeq \cA$ on the Koszul locus
\textup{(}Theorem~B\textup{)}.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
@@ -74,4 +74,4 @@
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
@@ -85,5 +85,6 @@
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
@@ -91,3 +92,3 @@
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
@@ -1346,4 +1347,8 @@
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
@@ -1417,6 +1422,11 @@
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
@@ -2031,6 +2041,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
@@ -2204,3 +2217,4 @@
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
@@ -2216,3 +2230,5 @@
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
@@ -2240,4 +2256,5 @@
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
apply_patch(auto_approved=true) exited 0 in 83ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex
file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending

file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending

codex
The edit is in place. I’m re-reading the patched spans and then grepping the modified file for the old coalgebra-level Verdier formulas and nearby forbidden phrasing so I can confirm the surface is internally consistent.
exec
/bin/zsh -lc "sed -n '1338,1432p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '68,95p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2026,2039p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item The integration is well-defined because logarithmic forms pair with distributions
\end{itemize}

\emph{Properties of the pairing.}
\begin{enumerate}
\item \emph{Perfect pairing:} Non-degenerate in both arguments (by Lemma~\ref{lem:bar-holonomicity}: each graded piece is a holonomic $\mathcal{D}$-module on $\overline{C}_n(X)$, hence has finite-dimensional stalks, and Verdier duality for holonomic $\mathcal{D}$-modules is an involution~\cite{KS90})
\item \emph{Differential compatibility:} $\langle d_{\text{bar}}\omega, K \rangle 
= -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
\item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
\delta_D \rangle = 1$ for any divisor $D$
\item \emph{Verdier duality:} The perfect pairing realizes
\[
\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
\;\simeq\; (\mathcal{A})^!_\infty
\]
as factorization algebras on $\operatorname{Ran}(X)$
\end{enumerate}
\end{theorem}

\begin{proof}
 succeeded in 53ms:
\item \emph{Cobar / bar-cobar inversion}
 (Theorem~B, Corollary~\ref{cor:bar-cobar-inverse}):
 \[\Omegach(\barB(\cA)) \;\xrightarrow{\sim}\; \cA\qquad
 \text{(recovers $\cA$ itself: a round-trip, not a duality)}.\]
\item \emph{Verdier duality on $\operatorname{Ran}(X)$}
 (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
 \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
 (\cA)^!_\infty\qquad
 \text{(gives the homotopy Koszul dual factorization algebra)}.\]
\item \emph{Chiral derived centre / Hochschild cochains}
 (Theorem~H):
 \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 \;=\; C^\bullet_{\mathrm{ch}}(\cA, \cA)\qquad
 \text{(the universal bulk / closed-string observables)}.\]
\end{enumerate}
\emph{Cobar is the inverse, not the dual.} Throughout this
chapter $\Omegach$ denotes the bar-cobar inverse functor of
(i); it recovers the algebra from its bar coalgebra. The
homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
 succeeded in 52ms:

\emph{Physical interpretation.} In quantum field theory:
\begin{itemize}
\item Bar elements = algebraic shadow data for off-shell states with infrared cutoffs
\item Cobar elements = algebraic shadow data for on-shell propagators with UV regularization
\item The pairing = conjectural algebraic shadow of S-matrix elements
\end{itemize}
\end{example}

\subsection{Poincaré--Verdier duality realization}

\begin{theorem}[Bar-cobar Verdier pairing; \ClaimStatusProvedHere]\label{thm:poincare-verdier}
The bar and cobar constructions are related by the Verdier
intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
exec
/bin/zsh -lc "sed -n '2199,2248p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\\\barB(\\\\cA"'^!)" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "gives the bar of the Koszul dual" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\\\bar{B}"'^{'"\\\\mathrm{ch}}(\\\\cA"'^!)" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{thm:bar-cobar-isomorphism-main\\}|Convention~\\\\ref\\{conv:bar-coalgebra-identity\\}\" chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:

\begin{remark}[Feigin--Frenkel center at critical level]
\label{rem:feigin-frenkel-center}
\index{Feigin--Frenkel center}
At the critical level $k = -h^\vee$, Proposition~\ref{prop:km-bar-curvature}(i) gives $m_1^2 = 0$, so the bar complex is \emph{uncurved}. A foundational result of Feigin--Frenkel~\cite{Feigin-Frenkel} shows that the center of $\widehat{\mathfrak{g}}_{-h^\vee}$ is then isomorphic to the algebra of functions on $\mathfrak{g}^\vee$-opers:
\[
Z(\widehat{\mathfrak{g}}_{-h^\vee}) \cong \mathrm{Fun}(\mathrm{Op}_{\check{\mathfrak{g}}}(X)).
\]
The critical level is the fixed point of the level-shifting involution $k \mapsto -k - 2h^\vee$, and the uncurved bar complex recovers $\widehat{\mathfrak{g}}_{-h^\vee}$ via cobar. See Part~\ref{part:characteristic-datum} for the detailed treatment.
\end{remark}

\begin{corollary}[Level-shifting via Verdier duality; \ClaimStatusProvedHere]
\label{cor:level-shifting-part1}
\index{Feigin--Frenkel duality}
\index{level!shifted}
% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
% duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
% inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
% Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
 exited 1 in 51ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending


thinking
**Looking for theorem context**

I realize I need more context for the Poincaré theorem and its proof after the corollary because it seems my information got truncated. I should open up more details around those sections to get a clearer understanding. Let’s explore what got cut off so I can ensure I grasp the theorem correctly and make sense of the proof. I want to make sure I’m comprehending everything fully!
codex
The old fixed-string patterns are gone from the target file. I’m doing one last read of the theorem at `thm:poincare-verdier` and the level-shift proof block because those are the two places where a locally coherent sentence matters more than the grep alone.
exec
/bin/zsh -lc "sed -n '2026,2046p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2238,2262p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "notably|crucially|remarkably|furthermore|it is worth noting|it should be noted|worth mentioning|delve|leverage|tapestry|cornerstone|journey|navigate" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\emph{Physical interpretation.} In quantum field theory:
\begin{itemize}
\item Bar elements = algebraic shadow data for off-shell states with infrared cutoffs
\item Cobar elements = algebraic shadow data for on-shell propagators with UV regularization
\item The pairing = conjectural algebraic shadow of S-matrix elements
\end{itemize}
\end{example}

\subsection{Poincaré--Verdier duality realization}

\begin{theorem}[Bar-cobar Verdier pairing; \ClaimStatusProvedHere]\label{thm:poincare-verdier}
The bar and cobar constructions are related by the Verdier
intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
\[
\mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
\;\simeq\; (\cA)^!_\infty,
\]
where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
 succeeded in 50ms:
\simeq \widehat{\mathfrak{g}}_k$ on the Koszul locus
(Theorem~B). The level-shifted algebra
$\widehat{\mathfrak{g}}_{k'}$ is the
\emph{Koszul dual}, obtained by Verdier duality on
$\operatorname{Ran}(X)$, not by the cobar functor.

The dual level $k' = -k - 2h^\vee$ satisfies:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $k + k' = -2h^\vee$;
\item the central charges satisfy $c(\widehat{\mathfrak{g}}_k) + c(\widehat{\mathfrak{g}}_{k'}) = 2\dim\mathfrak{g}$ \textup{(}Theorem~\ref{thm:central-charge-complementarity}\textup{)};
\item the curvatures are opposite: $m_0(k') = -m_0(k)$.
\end{enumerate}
\end{corollary}

\begin{proof}
The Verdier intertwining
(Theorem~\ref{thm:bar-cobar-isomorphism-main},
Convention~\ref{conv:bar-coalgebra-identity}) identifies
$\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
 exited 1 in 50ms:

exec
/bin/zsh -lc "rg -n --fixed-strings '---' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: unrecognized flag ---
file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending


thinking
**Refining grep usage**

I’m considering using `rg -n --fixed-strings -- '---' file` to find em dashes. It seems like the banned tokens didn’t return anything useful, so I might need the full theorem lines, especially since they get cut off after "On the Koszul locus." I’m thinking opening up a bit more could help, and I also need to make sure I run the em dash grep correctly this time. Let’s see how this turns out!
exec
/bin/zsh -lc "sed -n '2026,2050p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\emph{Physical interpretation.} In quantum field theory:
\begin{itemize}
\item Bar elements = algebraic shadow data for off-shell states with infrared cutoffs
\item Cobar elements = algebraic shadow data for on-shell propagators with UV regularization
\item The pairing = conjectural algebraic shadow of S-matrix elements
\end{itemize}
\end{example}

\subsection{Poincaré--Verdier duality realization}

\begin{theorem}[Bar-cobar Verdier pairing; \ClaimStatusProvedHere]\label{thm:poincare-verdier}
The bar and cobar constructions are related by the Verdier
intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
\[
\mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
\;\simeq\; (\cA)^!_\infty,
\]
where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
exec
/bin/zsh -lc "rg -n --fixed-strings -- '---' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '(\\cA)"'^!_'"\\infty' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
75: (\cA)^!_\infty\qquad
2042:\;\simeq\; (\cA)^!_\infty,
2045:$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
2048:$(\cA)^!_\infty \simeq \cA^!$.
2257:\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
2258:Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
 succeeded in 51ms:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef2..e27fe65 100644
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@ produces false statements.
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@ produces false statements.
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending

exec
/bin/zsh -lc "sed -n '2038,2054p' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
The bar and cobar constructions are related by the Verdier
intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
\[
\mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
\;\simeq\; (\cA)^!_\infty,
\]
where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
dual factorization algebra. On the Koszul locus,
Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
$(\cA)^!_\infty \simeq \cA^!$.
The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
\simeq \cA$ on the Koszul locus
\textup{(}Theorem~B\textup{)}.
The Verdier pairing between bar forms and cobar distributions
is the configuration-space incarnation of this intertwining.
file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending


thinking
**Checking theorem references**

I want to make sure everything looks coherent and check references to the `bar-cobar-verdier` theorem, particularly `\mathbb D_{\operatorname{Ran}}`. I’m wondering if this can extend to factorization algebras on Ran(X) and if theorem pairings relate to a specific bar degree. I might need to run a grep search for the same old formula, especially since the user only needs information from a target file. It looks like I need to search the repo for specific strings too.
codex
The target file is clean now. I’m doing one cross-surface grep for the same outdated `\mathbb D_{\Ran}\bar B(\mathcal A) \simeq \bar B(\mathcal A^!)` pattern so I can either confirm there’s no remaining collision or leave an explicit pending note, without editing outside the assigned file.
exec
/bin/zsh -lc "rg -n -F '\\barB(\\cA"'^!)'"' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:2404:$(\cA^!)^! = \mathrm{cobar}(\barB(\cA^!)) =
chapters/theory/higher_genus_complementarity.tex:1972:$\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \simeq \barB(\cA^!)$.
chapters/theory/higher_genus_complementarity.tex:5823: corrections to $\barB(\cA^!)$ vanish because the obstruction
chapters/theory/bar_cobar_adjunction_inversion.tex:3266: $\mathbb{D}_{\mathrm{Ran}}(\widehat{\mathcal{C}}) \simeq \barB(\cA^!)$
chapters/theory/bar_cobar_adjunction_inversion.tex:3270: identification of $\cA^!_\infty$ with $\barB(\cA^!)$ is the content
chapters/connections/concordance.tex:11241: $\barB(\cA)$ to $\barB(\cA^!)$, not to
chapters/connections/frontier_modular_holography_platonic.tex:3306:$\barB(\cA^!)$ is uncurved if and only if
exec
/bin/zsh -lc "rg -n -F '\\bar{B}"'^{'"\\mathrm{ch}}(\\cA"'^!)'"' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:621:\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA^!)\bigr)_{\Sigma}.
chapters/theory/chiral_hochschild_koszul.tex:630:\bar{B}^{\mathrm{ch}}(\cA^!),
chapters/theory/chiral_hochschild_koszul.tex:632:\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA^!)
chapters/theory/chiral_hochschild_koszul.tex:654:\bigl(\mathbb{D}_{\Ran}^2\bar{B}^{\mathrm{ch}}(\cA^!)\bigr)_{\Sigma}
chapters/theory/chiral_hochschild_koszul.tex:656:\bigl(\bar{B}^{\mathrm{ch}}(\cA^!)\bigr)_{\Sigma}.
exec
/bin/zsh -lc "rg -n -F '(\\cA)"'^!_'"\\infty' chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'gives the bar of the Koszul dual' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:3771:(\cA)^!_\infty \simeq \cA^!$ on the Koszul locus. This is the
chapters/theory/cobar_construction.tex:75: (\cA)^!_\infty\qquad
chapters/theory/cobar_construction.tex:2042:\;\simeq\; (\cA)^!_\infty,
chapters/theory/cobar_construction.tex:2045:$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
chapters/theory/cobar_construction.tex:2048:$(\cA)^!_\infty \simeq \cA^!$.
chapters/theory/cobar_construction.tex:2257:\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
chapters/theory/cobar_construction.tex:2258:Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending


thinking
**Checking syntax and errors**

I want to make sure there are no whitespace errors or syntax issues. I’ll use a command like `git diff --check -- chapters/theory/cobar_construction.tex` to verify everything. Running that check will help ensure the code is in good shape. It seems like a straightforward step, but I know how easy it can be to overlook small details. So this check feels important to get right!
codex
I have the local truth fix and the target-file grep checks. I’m running one final diff sanity check on the edited file only, plus a targeted grep to confirm the old `\Omega^{\mathrm{ch}}(\mathcal A^!)`/bar-of-dual wording is absent from this file.
exec
/bin/zsh -lc 'git diff --check -- chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc "rg -n -F '\\Omega"'^{'"\\text{ch}}(\\mathcal{A}"'^!)'"' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathbb{D}(\\bar{B}"'^{'"\\text{ch}}(\\mathcal{A}))' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 51ms:

file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending


thinking
**Finding line numbers**

I think I need to include a clickable file link with line references. It also seems important to get exact line numbers, so I might use `nl -ba` to help with that. I should read the file with `nl` around the changed chunks to pull those line numbers accurately. Getting those details will surely make it easier for anyone to follow along with the edits!
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '72,94p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    72	\item \emph{Verdier duality on $\operatorname{Ran}(X)$}
    73	 (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
    74	 \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
    75	 (\cA)^!_\infty\qquad
    76	 \text{(gives the homotopy Koszul dual factorization algebra)}.\]
    77	\item \emph{Chiral derived centre / Hochschild cochains}
    78	 (Theorem~H):
    79	 \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
    80	 \;=\; C^\bullet_{\mathrm{ch}}(\cA, \cA)\qquad
    81	 \text{(the universal bulk / closed-string observables)}.\]
    82	\end{enumerate}
    83	\emph{Cobar is the inverse, not the dual.} Throughout this
    84	chapter $\Omegach$ denotes the bar-cobar inverse functor of
    85	(i); it recovers the algebra from its bar coalgebra. The
    86	homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
    87	Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
    88	Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
    89	\emph{different} operation on $\barB(\cA)$. A statement such as
    90	``the cobar of the bar gives the Koszul dual''
    91	is false; the correct statement is
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '1344,1430p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2038,2050p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '2214,2260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1344	\item \emph{Differential compatibility:} $\langle d_{\text{bar}}\omega, K \rangle 
  1345	= -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
  1346	\item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
  1347	\delta_D \rangle = 1$ for any divisor $D$
  1348	\item \emph{Verdier duality:} The perfect pairing realizes
  1349	\[
  1350	\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
  1351	\;\simeq\; (\mathcal{A})^!_\infty
  1352	\]
  1353	as factorization algebras on $\operatorname{Ran}(X)$
  1354	\end{enumerate}
  1355	\end{theorem}
  1356	
  1357	\begin{proof}
  1358	\emph{Step 1: Well-definedness of the pairing}
  1359	
  1360	Logarithmic forms on $\overline{C}_n(X)$ restrict to distributional 
  1361	forms on $C_n(X)$. Explicitly, near a divisor $D = \{z_i = z_j\}$ with local 
  1362	coordinate $\epsilon = z_i - z_j$:
  1363	
 succeeded in 50ms:
  2038	The bar and cobar constructions are related by the Verdier
  2039	intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
  2040	\[
  2041	\mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
  2042	\;\simeq\; (\cA)^!_\infty,
  2043	\]
  2044	where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
  2045	$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
  2046	dual factorization algebra. On the Koszul locus,
  2047	Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
  2048	$(\cA)^!_\infty \simeq \cA^!$.
  2049	The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
  2050	not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 succeeded in 51ms:
  2214	% Resolved RECTIFICATION-FLAG (2026-04-07): This result uses Verdier
  2215	% duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
  2216	% inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
  2217	% Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
  2218	% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
  2219	% k' = -k-2h^v. The proof below correctly
  2220	% invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
  2221	For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
  2222	the Verdier intertwining
  2223	(Theorem~\ref{thm:bar-cobar-isomorphism-main},
  2224	Convention~\ref{conv:bar-coalgebra-identity}) applied to the
  2225	curved bar coalgebra of
  2226	Proposition~\ref{prop:km-bar-curvature} gives
  2227	\begin{equation}\label{eq:level-shifting-part1}
  2228	\mathbb{D}_{\operatorname{Ran}}\bigl(
  2229	 \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
  2230	\;\simeq\;
  2231	\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
  2232	\;\simeq\;
  2233	\widehat{\mathfrak{g}}_{k'},
file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending

codex
**Status**
- `FIXED` the `thm:verdier-bar-cobar` surface in [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1348). The Verdier item now states
  `\mathbb{D}_{\operatorname{Ran}}(\bar B^{\mathrm{ch}}(\mathcal A)) \simeq (\mathcal A)^!_\infty`
  as a factorization algebra on `\operatorname{Ran}(X)`, and Step 4 was aligned to the same algebra-level identification at [1421](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:1421).
- `FIXED` the later affine/Kac--Moody restatement in [cobar_construction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2221). The corollary now says
  `\mathbb{D}_{\operatorname{Ran}}(\bar B^{\mathrm{ch}}(\widehat{\mathfrak g}_k)) \simeq (\widehat{\mathfrak g}_k)^!_\infty \simeq \widehat{\mathfrak g}_{k'}`
  at [2227](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2227), and the proof now cites the same Theorem A convention at [2253](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2253).
- `FIXED` surrounding local prose so the file no longer contradicts itself: the opening “three functors” remark at [72](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:72) and the Poincare--Verdier restatement at [2038](/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex:2038) now use the same `(\cA)^!_\infty` convention.

Verification: I re-read all patched spans, `git diff --check` is clean, and grep on the modified file returned no remaining hits for the old target patterns `\barB(\cA^!)`, `\bar{B}^{\mathrm{ch}}(\cA^!)`, `gives the bar of the Koszul dual`, `\Omega^{\text{ch}}(\mathcal A^!)`, or `\mathbb D(\bar B^{\text{ch}}(\mathcal A))`.

Pending scope note: repo grep surfaced potential same-convention collision surfaces outside the assigned file, notably [higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:1972), [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:3266), and [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:11241). I did not edit those because this task was scoped to `chapters/theory/cobar_construction.tex`.
file update:
diff --git a/chapters/theory/cobar_construction.tex b/chapters/theory/cobar_construction.tex
index 8715ef23c79733725fa19b750849f211086ca70d..e27fe65439cc4cfc3f7eaf94aa272527126481e6
--- a/chapters/theory/cobar_construction.tex
+++ b/chapters/theory/cobar_construction.tex
@@ -72,8 +72,8 @@
 \item \emph{Verdier duality on $\operatorname{Ran}(X)$}
  (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
  \[\mathbb{D}_{\operatorname{Ran}}(\barB(\cA)) \;\simeq\;
- \barB(\cA^!)\qquad
- \text{(gives the Koszul dual's bar coalgebra)}.\]
+ (\cA)^!_\infty\qquad
+ \text{(gives the homotopy Koszul dual factorization algebra)}.\]
 \item \emph{Chiral derived centre / Hochschild cochains}
  (Theorem~H):
  \[Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
@@ -83,13 +83,14 @@
 \emph{Cobar is the inverse, not the dual.} Throughout this
 chapter $\Omegach$ denotes the bar-cobar inverse functor of
 (i); it recovers the algebra from its bar coalgebra. The
-Koszul dual $\cA^!$ is obtained by Verdier duality on
-$\operatorname{Ran}(X)$, which is a \emph{different} operation on
-$\barB(\cA)$. A statement such as
+homotopy Koszul dual factorization algebra $\cA^!_\infty$ is obtained by
+Verdier duality on $\operatorname{Ran}(X)$, and on the Koszul locus
+Theorem~A identifies $\cA^!_\infty \simeq \cA^!$. This is a
+\emph{different} operation on $\barB(\cA)$. A statement such as
 ``the cobar of the bar gives the Koszul dual''
 is false; the correct statement is
 ``the cobar of the bar gives $\cA$, and Verdier duality of the bar
-gives the bar of the Koszul dual.''
+gives the homotopy Koszul dual factorization algebra.''
 \end{remark}
 
 \begin{remark}[Which bar complex does the cobar invert?]
@@ -1344,8 +1345,12 @@
 = -\langle \omega, d_{\text{cobar}}K \rangle$ (graded Leibniz rule)
 \item \emph{Residue-distribution duality:} $\langle \text{Res}_{D}[\omega], 
 \delta_D \rangle = 1$ for any divisor $D$
-\item \emph{Verdier duality:} The perfect pairing realizes $\Omega^{\text{ch}}(\mathcal{A}^!)
- \simeq \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))$ as factorization algebras
+\item \emph{Verdier duality:} The perfect pairing realizes
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\;\simeq\; (\mathcal{A})^!_\infty
+\]
+as factorization algebras on $\operatorname{Ran}(X)$
 \end{enumerate}
 \end{theorem}
 
@@ -1415,10 +1420,15 @@
 
 \emph{Step 4: Verdier duality realization}
 
-The pairing establishes an isomorphism:
-\[\Omega^{\text{ch}}(\mathcal{A}^!) \xrightarrow{\sim} \mathbb{D}(\bar{B}^{\text{ch}}(\mathcal{A}))\]
+The pairing establishes an isomorphism of factorization algebras on
+$\operatorname{Ran}(X)$:
+\[
+\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\text{ch}}(\mathcal{A}))
+\xrightarrow{\sim} (\mathcal{A})^!_\infty
+\]
 
-where $\mathbb{D}$ is the Verdier dualizing functor.
+where $(\mathcal{A})^!_\infty$ denotes the homotopy Koszul dual factorization
+algebra of Theorem~A.
 
 \emph{Non-degeneracy.}
 At bar degree~$n = 1$, Step~3 establishes the fundamental pairing
@@ -2029,10 +2039,13 @@
 intertwining of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}}:
 \[
 \mathbb{D}_{\operatorname{Ran}}\bigl(\bar{B}^{\mathrm{ch}}(\cA)\bigr)
-\;\simeq\; \bar{B}^{\mathrm{ch}}(\cA^!),
+\;\simeq\; (\cA)^!_\infty,
 \]
 where $\mathbb{D}_{\operatorname{Ran}}$ denotes Verdier duality on
-$\operatorname{Ran}(X)$ and $\cA^!$ is the Koszul dual algebra.
+$\operatorname{Ran}(X)$ and $(\cA)^!_\infty$ is the homotopy Koszul
+dual factorization algebra. On the Koszul locus,
+Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} identifies
+$(\cA)^!_\infty \simeq \cA^!$.
 The cobar construction $\Omega^{\mathrm{ch}}$ is the \emph{inverse},
 not the dual: $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
 \simeq \cA$ on the Koszul locus
@@ -2202,7 +2215,8 @@
 % duality D_Ran on the bar coalgebra (Theorem A intertwining), NOT bar-cobar
 % inversion (Theorem B). Bar-cobar inversion recovers the original algebra:
 % Omega(B(g_k)) ~ g_k. The level-shifted algebra arises from
-% D_Ran(B(g_k)) ~ B(g_{k'}) with k' = -k-2h^v. The proof below correctly
+% D_Ran(B(g_k)) ~ (g_k)^!_infty ~ g_{k'} as factorization algebras, with
+% k' = -k-2h^v. The proof below correctly
 % invokes Theorem A and Convention conv:bar-coalgebra-identity. Verified.
 For any simple Lie algebra $\mathfrak{g}$ and level $k \neq -h^\vee$,
 the Verdier intertwining
@@ -2214,7 +2228,9 @@
 \mathbb{D}_{\operatorname{Ran}}\bigl(
  \bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_k)\bigr)
 \;\simeq\;
-\bar{B}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{k'}),
+\bigl(\widehat{\mathfrak{g}}_k\bigr)^!_\infty
+\;\simeq\;
+\widehat{\mathfrak{g}}_{k'},
 \qquad k' = -k - 2h^\vee.
 \end{equation}
 Bar-cobar \emph{inversion} recovers the original algebra:
@@ -2238,8 +2254,9 @@
 (Theorem~\ref{thm:bar-cobar-isomorphism-main},
 Convention~\ref{conv:bar-coalgebra-identity}) identifies
 $\mathbb{D}_{\operatorname{Ran}}(\bar{B}^{\mathrm{ch}}(\cA))
-\simeq \bar{B}^{\mathrm{ch}}(\cA^!)$ for any chiral algebra
-$\cA$. For $\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
+\simeq (\cA)^!_\infty$ for any chiral algebra $\cA$, and on the
+Koszul locus $(\cA)^!_\infty \simeq \cA^!$. For
+$\cA = \widehat{\mathfrak{g}}_k$, the Koszul dual
 is $\cA^! = \widehat{\mathfrak{g}}_{k'}$ with
 $k' = -k - 2h^\vee$: Verdier duality on Ran negates the
 curvature element, sending

tokens used
107,105
