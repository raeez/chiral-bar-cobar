# D02_slop_v1_examples (372s)



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
session id: 019d8813-a1db-7670-908b-6b2c42f63978
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


Same slop removal for chapters/examples/*.tex.
mcp startup: no servers

thinking
**Auditing for banned vocabulary**

I need to clarify what "Same slop removal" means, as it likely pertains to some banned vocabulary. I should audit all files in the chapters/examples directory for any banned tokens and issues with em-dashes or markdown. I aim to edit only the assigned files with minimum necessary edits. My strategy involves identifying problems and fixing them all at once, noting the issue's location and the exact change made in the final report. I’ll inspect all relevant files.
codex
I’m treating this as a scoped prose audit on `chapters/examples/*.tex`: read the repo’s required constitutional files first, then scan every example chapter for banned slop patterns and apply only minimal fixes inside that directory.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
codex
I’ve loaded the constitutional files and the examples scope is a known hot zone. Next I’m reading the relevant skill workflow and then scanning `chapters/examples/*.tex` for the banned prose patterns before touching anything.
exec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/beilinson-rectify/SKILL.md
printf '\\n---SPLIT---\\n'
sed -n '1,240p' .agents/skills/build-surface/SKILL.md
printf '\\n---SPLIT---\\n'
rg --files chapters/examples -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

codex
I’m using the `beilinson-rectify` workflow for the prose cleanup and `build-surface` for verification. The next pass is a literal grep against the banned-token surface in `chapters/examples/*.tex`, then I’ll inspect each hit in context before editing.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '"'`|'"\\*\\*' chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i --glob '*.tex' 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|arguably|perhaps|seems to|appears to|---|—' chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:85:The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
chapters/examples/deformation_quantization.tex:923:``short loops'' (an edge from $z_i$ to itself is inadmissible),
chapters/examples/deformation_quantization.tex:1170:of collisions. When the ``algebra'' is replaced by a \emph{map germ}
chapters/examples/deformation_quantization.tex:1224:$\JacF{F}{p}$ is the bar-type coalgebra of the ``algebra'' whose only
chapters/examples/deformation_quantization.tex:1487:in degree~$0$ (``coordinate functions''), and
chapters/examples/deformation_quantization.tex:1490:(``equation generators'').
chapters/examples/deformation_quantization.tex:1690:\begin{remark}[Why ``boundary-linear'']
chapters/examples/deformation_quantization.tex:1693:\emph{linear} in the $y$-variables (the ``boundary'' or
chapters/examples/deformation_quantization.tex:1694:``auxiliary'' directions). This linearity is the reason the
chapters/examples/deformation_quantization.tex:2059:``tail'' than the node's.
chapters/examples/w_algebras_deep.tex:83:where the right side is the ``thick'' flag variety with formal neighborhood structure.
chapters/examples/w_algebras_deep.tex:341:$\partial^2\phi_2$ (the ``background charge'') controlled by the level.
chapters/examples/w_algebras_deep.tex:1096:The point: the ``residue-side'' OPE coefficients
chapters/examples/w_algebras_deep.tex:1099:``DS-side'' coefficients $\mathsf{C}^{\mathrm{DS}}$ (the DS
chapters/examples/w_algebras_deep.tex:1404:The ``extraction problem'' on the $\mathcal{W}_\infty$ side of
chapters/examples/w_algebras_deep.tex:1455:\item Commutativity says: the bar complex ``knows'' that DS
chapters/examples/w_algebras_deep.tex:3247:Since $\lambda \mapsto \lambda^t$ exchanges ``distinct parts'' with
chapters/examples/w_algebras_deep.tex:3248:``consecutive differences $\leq 1$,'' the abelianity condition on
chapters/examples/w_algebras_deep.tex:3524:(the ``super'' analogue of the bosonic $c_{\mathrm{slab}} = 26$).
chapters/examples/w_algebras_deep.tex:4153:OPE is ``even'' in $W^{(s)}$). This forces
 succeeded in 51ms:
chapters/examples/w3_composite_fields.tex:36:In the $W$--$W$ OPE, $\Lambda$ appears together with the stress tensor conformal block
codex
The raw grep is noisy because the scope contains many quoted mathematical labels. I’m rerunning with token-by-token matching so only actual banned prose hits survive, then I’ll patch only those lines.
exec
/bin/zsh -lc "echo '== em-dash ==' ; rg -n --glob '*.tex' '[—]' chapters/examples || true ; echo '== triple-hyphen ==' ; rg -n --glob '*.tex' '---' chapters/examples || true ; echo '== markdown backticks or bold ==' ; rg -n --glob '*.tex' '"'`|'"\\*\\*' chapters/examples || true" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
== em-dash ==
== triple-hyphen ==
rg: unrecognized flag ---
== markdown backticks or bold ==
chapters/examples/deformation_quantization.tex:85:The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
chapters/examples/deformation_quantization.tex:923:``short loops'' (an edge from $z_i$ to itself is inadmissible),
chapters/examples/deformation_quantization.tex:1170:of collisions. When the ``algebra'' is replaced by a \emph{map germ}
chapters/examples/deformation_quantization.tex:1224:$\JacF{F}{p}$ is the bar-type coalgebra of the ``algebra'' whose only
chapters/examples/deformation_quantization.tex:1487:in degree~$0$ (``coordinate functions''), and
chapters/examples/deformation_quantization.tex:1490:(``equation generators'').
chapters/examples/deformation_quantization.tex:1690:\begin{remark}[Why ``boundary-linear'']
chapters/examples/deformation_quantization.tex:1693:\emph{linear} in the $y$-variables (the ``boundary'' or
chapters/examples/deformation_quantization.tex:1694:``auxiliary'' directions). This linearity is the reason the
chapters/examples/deformation_quantization.tex:2059:``tail'' than the node's.
chapters/examples/w_algebras_deep.tex:83:where the right side is the ``thick'' flag variety with formal neighborhood structure.
chapters/examples/w_algebras_deep.tex:341:$\partial^2\phi_2$ (the ``background charge'') controlled by the level.
chapters/examples/w_algebras_deep.tex:1096:The point: the ``residue-side'' OPE coefficients
chapters/examples/w_algebras_deep.tex:1099:``DS-side'' coefficients $\mathsf{C}^{\mathrm{DS}}$ (the DS
chapters/examples/w_algebras_deep.tex:1404:The ``extraction problem'' on the $\mathcal{W}_\infty$ side of
chapters/examples/w_algebras_deep.tex:1455:\item Commutativity says: the bar complex ``knows'' that DS
exec
/bin/zsh -lc "for pat in 'moreover' 'additionally' 'notably' 'crucially' 'remarkably' 'interestingly' 'furthermore' 'we now' 'it is worth noting' 'worth mentioning' 'it should be noted' 'it is important to note' 'delve' 'leverage' 'tapestry' 'cornerstone' 'journey' 'navigate' 'arguably' 'perhaps' 'seems to' 'appears to'; do echo \"== "'$pat =="; rg -n -i --glob '"'*.tex' -F \""'$pat" chapters/examples || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 95ms:
== navigate ==
== arguably ==
== perhaps ==
== seems to ==
== appears to ==
chapters/examples/w3_composite_fields.tex:36:In the $W$--$W$ OPE, $\Lambda$ appears together with the stress tensor conformal block

thinking
**Inspecting context lines**

I'm trying to figure out if "appears together" can also mean "appears to" when there's a double space. Though it feels irrelevant, I should check the context of the line. It might be better to use word boundaries and possibly skip certain parts. I think I need to closely analyze the suspicious line with `sed` to clarify what's going on. Let's see what insights that yields!
exec
/bin/zsh -lc "sed -n '30,42p' chapters/examples/w3_composite_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\Lambda = :TT: - \tfrac{3}{10}\,\partial^2 T
\end{equation}
where $:TT:$ is the normally ordered square of the stress tensor.
The coefficient $-3/10$ is the unique value making $\Lambda$ quasi-primary
(Proposition~\ref{prop:lambda-modes}).

In the $W$--$W$ OPE, $\Lambda$ appears together with the stress tensor conformal block
(Theorem~\ref{thm:lambda-coefficients-derivation}). The full $(z-w)^{-2}$ coefficient is:
\begin{equation}
W(z)W(w) \sim \cdots + \frac{\tfrac{3}{10}\,\partial^2 T(w) + \tfrac{16}{22+5c}\,\Lambda(w)}{(z-w)^2}
+ \frac{\tfrac{1}{15}\,\partial^3 T(w) + \tfrac{8}{22+5c}\,\partial\Lambda(w)}{z-w} + \cdots
\end{equation}
where the $\partial^2 T$ and $\partial^3 T$ terms arise from Taylor-expanding the stress tensor conformal block $c/3 \cdot T(w)/(z-w)^4$.



thinking
**Evaluating token patterns**

I've noticed a potential bug with the patterns "appears to" and "appears together," but I think I'll ignore that for now and look for a more systematic approach. Maybe I should search for banned connective words using word boundaries. The user mentioned “Same slop removal,” which suggests there could be slop phrases not in the explicit ban list. It seems like I'll need to audit examples for general AI slop too, focusing on removing narrative fluff and casual rhetoric. I need to find and fix these issues.
thinking
**Inspecting for AI slop**

I need to check files for any obvious AI slop language, even if it’s not on the blacklist. I might look for patterns like em dashes, markdown, and banned tokens. However, I’m not seeing any clear examples, except maybe with em dashes or triple hyphens. I suspect there are stylistic issues, like rhetorical phrases. The user mentioned "same slop removal," which could refer to criteria I'm not aware of. I'll audit files for known slop patterns and focus on those at higher risk.
thinking
**Searching for rhetorical phrases**

I need to look for common rhetorical phrases like "The point:", "A natural temptation," and some others. It's essential to minimize edits and not go overboard, but we also need evidence to support any changes. I could scan for colloquial phrases or marketing language in examples and determine how many we find. It might be helpful to set a threshold for what counts as problematic. Maybe using language model inspection would help clarify what needs to be addressed.
exec
/bin/zsh -lc "for pat in 'The point:' 'A natural temptation' 'This is not a coincidence' 'earns the name' 'naive ' 'fake' 'special point' 'top-down' 'bottom-up' 'wrong' 'slogan' 'The word ' 'the word ' 'use up' 'linearizes' 'horizontal' 'vertical' 'strongly coupled' 'half-string'; do echo \"== "'$pat =="; rg -n --glob '"'*.tex' -F \""'$pat" chapters/examples || true; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "for pat in 'natural temptation' 'not a coincidence' 'The first term corresponds' 'The upper half-plane' 'worldsheet' 'past,' 'A naive' 'scope of' 'unconditional' 'holographic atom' 'picture-changed' 'harmonic modes'; do echo \"== "'$pat =="; rg -n --glob '"'*.tex' -F \""'$pat" chapters/examples || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
== natural temptation ==
chapters/examples/beta_gamma.tex:245:A natural temptation is to write ``$\beta\gamma$ has shadow depth
== not a coincidence ==
chapters/examples/genus_expansions.tex:659:is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
chapters/examples/genus_expansions.tex:1904:substitution $x \mapsto ix$. This is not a coincidence: the family
== The first term corresponds ==
chapters/examples/deformation_quantization_examples.tex:171:The first term corresponds to the ``double Poisson'' Kontsevich graph (both internal vertices connecting directly to the two external vertices); the second involves $\partial\pi$ and vanishes for constant Poisson structures.
== The upper half-plane ==
chapters/examples/deformation_quantization.tex:85:The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
== worldsheet ==
chapters/examples/deformation_quantization.tex:85:The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
chapters/examples/free_fields.tex:4591:that Polyakov introduces for gauge-fixing the worldsheet
chapters/examples/free_fields.tex:4617:of the worldsheet theory. The degree-$2$ shadow
chapters/examples/free_fields.tex:5203:The genus-$1$ bar complex transforms covariantly under $\mathrm{SL}_2(\mathbb{Z})$ with weight $c/24$ (Theorem~\ref{thm:modular-invariance}). Modular invariance of the full partition function requires the left-right central charge difference $c - \tilde{c} = 0 \bmod 24$ (for single-valuedness of the phase $e^{2\pi i (c-\tilde{c})/24}$). For the bosonic string ($c = \tilde{c} = 26$) and the superstring ($c = \tilde{c} = 15$), conformal anomaly cancellation arises from Weyl invariance on the worldsheet, not from $c \bmod 24$ alone. This is the Belavin--Knizhnik theorem \cite{BK86}; see also Polchinski \cite[Ch.~5]{Pol98} for the standard textbook treatment.
chapters/examples/kac_moody.tex:158:worldsheet orientation. The same involution governs modular
== past, ==
chapters/examples/deformation_quantization.tex:85:The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
== A naive ==
chapters/examples/yangians_drinfeld_kohno.tex:8697:A naive ``shift-invariance'' statement at mixed-root level is
== scope of ==
 succeeded in 100ms:
chapters/examples/bershadsky_polyakov.tex:459:and principal reductions: together they ``use up'' the full
== linearizes ==
chapters/examples/landscape_census.tex:871: Proposition~\ref{prop:winfty-ds-stage-growth-packet} linearizes the
chapters/examples/free_fields.tex:2054:``linearizes'' Heisenberg representation theory via Koszul duality.
== horizontal ==
chapters/examples/w_algebras_deep.tex:1444:\item The upper horizontal arrow is the chain-level DS--KD
chapters/examples/w_algebras_deep.tex:1451:\item The lower horizontal arrow is the Hamiltonian reduction on
chapters/examples/free_fields.tex:2424:The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
chapters/examples/landscape_census.tex:29:Koszul chiral algebra treated in Part~\ref{part:physics-bridges}. Read horizontally, each row
chapters/examples/w_algebras.tex:811:encodes this: the upper horizontal arrow is the algebraic DS functor,
chapters/examples/w_algebras.tex:812:the lower horizontal arrow is the geometric localization, and the
chapters/examples/yangians_drinfeld_kohno.tex:394:horizontal subalgebra $U_{q^{-1}}(\mathfrak{g}) \hookrightarrow
chapters/examples/yangians_drinfeld_kohno.tex:7532:on $\overline{\mathcal{M}}_{0,n}$ whose horizontal sections are
chapters/examples/yangians_drinfeld_kohno.tex:8187:& \text{bar-horizontal connection}
chapters/examples/yangians_drinfeld_kohno.tex:8196:%% Bar-horizontal strictification and the KZ connection
chapters/examples/yangians_drinfeld_kohno.tex:8198:\subsubsection{Bar-horizontal strictification}
chapters/examples/yangians_drinfeld_kohno.tex:8207:\begin{definition}[Bar-horizontal strictification]
chapters/examples/yangians_drinfeld_kohno.tex:8208:\label{def:bar-horizontal-strictification}
chapters/examples/yangians_drinfeld_kohno.tex:8209:\index{bar-horizontal strictification|textbf}
chapters/examples/yangians_drinfeld_kohno.tex:8213:A \emph{bar-horizontal strictification} of $Y$ is a complete


thinking
**Considering text adjustments**

I need to scan the content with keywords like "naive," focusing on maintaining technical language rather than casual phrasing. It seems only some sections might need fixing. The user has asked for a similar cleanup for chapters/examples/*.tex, which suggests they want to focus on removing casual prose while keeping the technical terms, like "naive," intact. So, I’ll need to be careful about what I alter to preserve the intended meaning!
thinking
**Inspecting context and updating plans**

I need to inspect the context of candidate lines, which sounds a bit complex already. It’s probably a good idea to use parallel sed around them. Maybe I should search specific files for this. I’m beginning to think I’ll need to develop a longer plan since the task seems substantial. After that, I can update the plan tool as I go. I guess I’ll do this after I handle the initial context.
codex
I have the candidate surface narrowed. Most blacklist hits were false positives or technical uses; the remaining work is a line-by-line pass on the genuinely rhetorical prose, then a final grep to prove the cleanup stayed local to `chapters/examples/*.tex`.

```
plan:
1. Inspect each candidate context in `chapters/examples/*.tex` and separate real prose slop from technical terminology. in_progress
2. Apply minimum truthful edits only in the affected example files.
3. Re-run the banned-token grep plus a diff on `chapters/examples/*.tex` to verify the surface is clean and scoped.
```
Plan update
The examples directory is large; I’ve reduced the audit to candidate rhetorical phrases and am checking them in context before editing.
  → Inspect each candidate context in `chapters/examples/*.tex` and separate real prose slop from technical terminology.
  • Apply minimum truthful edits only in the affected example files.
  • Re-run the banned-token grep plus a diff on `chapters/examples/*.tex` to verify the surface is clean and scoped.
exec
/bin/zsh -lc "sed -n '76,92p' chapters/examples/deformation_quantization.tex
printf '\\n---\\n'
sed -n '1088,1110p' chapters/examples/w_algebras_deep.tex
printf '\\n---\\n'
sed -n '238,254p' chapters/examples/beta_gamma.tex
printf '\\n---\\n'
sed -n '1868,1988p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '286,300p' chapters/examples/w3_holographic_datum.tex
printf '\\n---\\n'
sed -n '2416,2432p' chapters/examples/free_fields.tex
printf '\\n---\\n'
sed -n '698,712p' chapters/examples/deformation_quantization_examples.tex
printf '\\n---\\n'
sed -n '44,60p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '652,670p' chapters/examples/genus_expansions.tex
printf '\\n---\\n'
sed -n '1896,1912p' chapters/examples/genus_expansions.tex
printf '\\n---\\n'
sed -n '3498,3526p' chapters/examples/lattice_foundations.tex
printf '\\n---\\n'
sed -n '452,468p' chapters/examples/bershadsky_polyakov.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The Kontsevich weight is:
\[w_\Gamma = \frac{1}{(2\pi)^2}\int_{\mathbb{H}} d\phi_{1f} \wedge d\phi_{1g} = \frac{1}{2}\]
where $\phi_{1f} = \arg(f - z_1)$ and $\phi_{1g} = \arg(g - z_1)$ are the angles from the internal vertex $z_1 \in \mathbb{H}$ to the boundary points. The bidifferential operator is $B_\Gamma(f,g) = \pi^{ij}\partial_i f \cdot \partial_j g = \{f, g\}$, giving:
\[f \star g = fg + \frac{\hbar}{2}\{f,g\} + O(\hbar^2)\]
\end{example}

\subsection{Role of the upper half-plane}

The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.

The key geometric fact: the Kontsevich configuration spaces $C_{n,m}(\mathbb{H})$ (of $n$ interior and $m$ boundary points, modulo $\operatorname{Aff}(\mathbb{R})$) have FM-type compactifications $\overline{C}_{n,m}(\mathbb{H})$ whose boundary strata are governed by the operad structure of the Stasheff associahedra $K_\bullet$ and the little 2-disks operad $E_2$. In particular, the boundary stratification encodes the same combinatorics as the real moduli spaces $\overline{\mathcal{M}}_{0,m}(\mathbb{R})$.

\section{Chiral algebras as quantum observables}

\subsection{From Poisson to chiral}


---
\eta_{12}$ in the $\widehat{\mathfrak{sl}}_3$ bar complex. The
 succeeded in 51ms:
$K_N = 0$, which excludes every $\Walg$-algebra.
\end{remark}

\begin{remark}[Self-dual point versus critical string point;
 guard]
\label{rem:w3hol-self-dual-vs-critical}
There are two distinguished central charges for $\Walg_3$. Both are
sometimes called ``the special point''; they must \emph{never} be
conflated.

\begin{itemize}
 \item \textbf{Self-dual point}\quad $c^* = 50$. This is the fixed
 point of the Feigin--Frenkel involution $c \mapsto 100 - c$, the
 unique central charge at which $\cA \simeq \cA^!$ as chiral
 algebras. At this point the asymmetry

---
$t = -1$ gives $\eta(\tau)^d$, consistent with the Euler
characteristic of the Ext algebra being the ratio of Heisenberg
to dual characters.
 succeeded in 51ms:
For the principal $\mathcal{W}_3$ algebra (where $c + c' = 100$), the analogous computation gives the Virasoro-lineage $W$-algebra sum $\kappa_{\mathcal{W}_3} + \kappa_{\mathcal{W}_3}' = 250/3$ \end{remark}

\begin{remark}[Bosonic string anomaly splitting]\label{rem:bosonic-string-anomaly-splitting}
The complementarity sum $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$ equals the bosonic string curvature $\kappa$ at $d = 26$ divided by~$2$. The combined genus-$g$ free energy
\[
F_g(\mathrm{Vir}_c) + F_g(\mathrm{Vir}_{26-c}) = 13 \cdot \lambda_g^{\mathrm{FP}}
\]
is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
\end{remark}

\begin{remark}[Verlinde bundle and the limits of the scalar genus tower]%
\label{rem:verlinde-vs-kappa}%
\index{Verlinde formula!vs scalar genus tower}%
The free energy $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ \textup{(}UNIFORM-WEIGHT\textup{)} is the
\emph{Euler characteristic} of a much richer object. For
$\widehat{\mathfrak{sl}}_{2,k}$ at integrable level, the
factorization homology $\int_{\Sigma_g}\!\widehat{\mathfrak{sl}}_{2,k}$
is a vector bundle over $\mathcal{M}_g$, the \emph{Verlinde bundle}
(or bundle of conformal blocks), whose rank is given by the


thinking
**Analyzing properties for context**

I'm looking at an excerpt from 1868 that mentions specific properties related to a modular holography concept. I think there might be some unclear parts labeled as "slop" that need refining. To understand better, I should read a larger context around the years 1858-1885 and also 1968-1985. Gathering this extra context should help clarify things and enable me to apply these ideas correctly.
codex
Several hits are genuinely rhetorical rather than technical. I’m reading the surrounding blocks before editing so the fixes stay minimal and don’t accidentally alter named technical notions.
exec
/bin/zsh -lc "sed -n '1858,1886p' chapters/examples/beta_gamma.tex
printf '\\n---\\n'
sed -n '1968,1988p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8688,8708p' chapters/examples/yangians_drinfeld_kohno.tex
printf '\\n---\\n'
sed -n '6064,6080p' chapters/examples/free_fields.tex
printf '\\n---\\n'
sed -n '236,252p' chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '864,878p' chapters/examples/lattice_foundations.tex
printf '\\n---\\n'
sed -n '388,414p' chapters/examples/deformation_quantization_examples.tex
printf '\\n---\\n'
sed -n '628,738p' chapters/examples/minimal_model_examples.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 global all-genera content is encoded by the variation of
 $\mathcal{D}^{\beta\gamma}_{g,\lambda}(L)$ over the moduli of curves
 and auxiliary bundles.
\end{enumerate}
\end{conjecture}

\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
\label{rem:betagamma-cleanest-test}
The $\beta\gamma$ system is optimal for testing the modular envelope because:
(1)~the OPE is free (single simple pole, no higher singularities);
(2)~all higher $A_\infty$ operations vanish ($m_k = 0$ for $k \ge 3$);
(3)~genus dependence enters entirely through determinant-line geometry on curves.
These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
\end{remark}


%% ================================================================
\begin{remark}[The $\beta\gamma$ system as holographic atom]
\label{rem:betagamma-holographic-atom}
\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
 succeeded in 51ms:
$\frac{1}{4}[[X,Y],Z] + \frac{1}{12}[X,[Y,Z]]
+ \frac{1}{12}[Y,[X,Z]]$.
When $[X,Z] = 0$, Jacobi gives $[[X,Y],Z] = [X,[Y,Z]]$ and
the sum reduces to $\frac{1}{3}[X,[Y,Z]]$.
\end{proof}

\begin{remark}[Shift transport, not shift invariance]
\label{rem:spectral-shift-transport}
\index{shift transport!spectral}
A naive ``shift-invariance'' statement at mixed-root level is
false if interpreted coefficientwise. The shift changes local
coefficients by explicit ratios of shift characters at different
spectral arguments. What is invariant is the
\emph{obstruction class} after transport by the shift cocycle.
In particular, the shifted triangle transport coefficients
are uniquely determined by
\[
 \kappa_{ij}^{L,\mu}(w,z)
 =
 \frac{\chi_i^\mu(w)\,\chi_j^\mu(w+z)}{\chi_{ij}^\mu(w)}
 succeeded in 51ms:
$\AffKM{so}_8$ current algebra at level~1.
\end{proposition}

\begin{proof}
The $D_4$ root lattice has 24 roots, all of the form $\pm e_i \pm e_j$ ($i \neq j$). These form a single orbit under the Weyl group $W(D_4)$. The outer automorphism group $\operatorname{Out}(D_4) \cong S_3$ acts as graph automorphisms of the $D_4$ Dynkin diagram, permuting the three ``legs'' and hence permuting the three nontrivial cosets of $D_4^*/D_4 \cong (\mathbb{Z}/2\mathbb{Z})^2$ (vector, spinor, and conjugate spinor representations). Note: the spinor and conjugate spinor vectors lie in $D_4^* \setminus D_4$, not in the root lattice itself.

\emph{Step~1.} Triality action on bar complex.
The triality automorphism $\sigma$ acts on the lattice as a graph automorphism of the $D_4$ Dynkin diagram, permuting the three ``legs.'' This extends to an automorphism of $\Vlat_{D_4}$ via $\sigma(e^\alpha) = e^{\sigma(\alpha)}$. Since the bar construction is functorial (any algebra automorphism induces a coalgebra automorphism of the bar complex), $\sigma$ acts on $\barBgeom(\Vlat_{D_4})$.

\emph{Step~2.} Action on homology.
In bar degree~1, the generators are $[e^\alpha]$ for each of the 24 roots $\alpha$. The triality permutes these roots (preserving inner products). In bar degree~2, the differential $d([e^{\alpha_1} \mid e^{\alpha_2}]) = \varepsilon(\alpha_1,\alpha_2)\,[e^{\alpha_1+\alpha_2}]$ (when $\langle\alpha_1,\alpha_2\rangle = -1$) intertwines with $\sigma$ since $\sigma$ preserves inner products and the cocycle is equivariant (the standard Frenkel--Lepowsky--Meurman cocycle for $D_4$ is triality-invariant up to coboundary).

\emph{Step~3.} Conclusion.
The $S_3$-action on $H_*(\barBgeom(\Vlat_{D_4}))$ is the representation-theoretic manifestation of the triality symmetry: the three fundamental representations of $\mathfrak{so}_8$ (vector, spinor, conjugate spinor) are permuted by outer automorphisms, and this permutation lifts to the bar complex level.
\end{proof}

---
\label{eq:w3-poisson-WW}
\end{align}
where $\Lambda = TT - \frac{3}{10}\partial^2 T$ is the


thinking
**Revising terminology**

I’m pondering if I could just rewrite "has large shadow radius" instead of using "strongly coupled." I should check if "strongly coupled" is a common technical term. There’s a line about CFTs being the most 'strongly coupled,' but I wonder if I could say something like "the smallest central-charge minimal models have the largest shadow growth rates." That might be clearer. 

I’ll look into local edits as well, and check the wording in several examples to clarify further.
thinking
**Inspecting terminology**

I need to check the `yangians_foundations` section, particularly the phrase, "The word Yangian carries three distinct meanings..." I feel like it's close but could be more precise. Maybe I should say, "In this chapter, 'Yangian' refers to three levels." It might not be necessary, but it's worth considering. I should also look at the `w_algebras_deep` document around line 234 to see if there's any relevant slogan or phrasing that might need adjustment. Let's take a closer look!
exec
/bin/zsh -lc "sed -n '228,240p' chapters/examples/w_algebras_deep.tex
printf '\\n---\\n'
sed -n '6062,6076p' chapters/examples/free_fields.tex
printf '\\n---\\n'
sed -n '196,208p' chapters/examples/deformation_quantization_examples.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
This section has three layers. Principal finite-type W-algebras remain
part of the proved core; the $\mathfrak{sl}_3$ minimal/subregular
computations and the hook-type family results provide the first
non-principal theorematic seeds; the global non-principal transport
statement remains Conjecture~\ref{conj:w-orbit-duality}. The purpose of
the section is to isolate the mechanism that a future theorem must
globalize, not to blur that boundary into a single slogan. Concretely,
the remaining non-principal work is threefold: determine the dual-orbit
input, determine the orbit-indexed level shift, and globalize the
paired DS seed transport beyond the present hook/subregular theorematic
seeds.
\end{remark}


---
not the algebra. For a two-element cover $\mathcal{U} =
\{U_0, U_\infty\}$ of $\mathbb{P}^1$, the Moore complex
$M\check{C}^\bullet$ is concentrated in degrees $0$ and $1$, and
$\check{C}^p = 0$ for $p \geq 2$ leaves no room for a
Jacobiator (Proposition~\textup{\ref{prop:two-element-strict}}).

thinking
**Refining language and search terms**

I’m considering changing "wrong level" to something like "non-integral" or "unquantized level" for better accuracy. I’ll scan for phrases like "the point," "natural temptation," "not coincidence," "slogan," "holographic atom," "top-down," and "bottom-up." I think it’s worthwhile to look at "cleanest modular test" and "optimal for testing" too. However, "hydrogen atom of modular holography" definitely needs changing. I should search for "hydrogen atom," "cleanest modular test," and "optimal."
exec
/bin/zsh -lc "for pat in 'hydrogen atom' 'cleanest modular test' 'optimal for testing' 'The key geometric fact:' 'The purpose of' 'The correct slogan is:' 'The point:' 'This is the expected output' 'earns the name' 'half-string' 'top-down' 'bottom-up' 'use up' 'wrong''; do echo \"== "'$pat =="; rg -n --glob '"'*.tex' -F \""'$pat" chapters/examples || true; done' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: unmatched '
exec
/bin/zsh -lc "for pat in 'The simplest object' 'simplest object in which' 'pure probe' 'uncontaminated by' 'A natural temptation is' 'This is the chiral-algebraic analogue' 'special point' 'cleanest' 'holographic atom principle'; do echo \"== "'$pat =="; rg -n --glob '"'*.tex' -F \""'$pat" chapters/examples || true; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
== The simplest object ==
== simplest object in which ==
chapters/examples/beta_gamma.tex:1882:simplest object in which the boundary algebra, the Koszul-dual defect
== pure probe ==
chapters/examples/beta_gamma.tex:1980:$Z_{\beta\gamma}(\hbar)$ as a pure probe of the global geometry of
== uncontaminated by ==
chapters/examples/beta_gamma.tex:1986:uncontaminated by local nonlinearity. Any failure of the modular
== A natural temptation is ==
chapters/examples/beta_gamma.tex:245:A natural temptation is to write ``$\beta\gamma$ has shadow depth
== This is the chiral-algebraic analogue ==
chapters/examples/minimal_model_examples.tex:630:This is the chiral-algebraic analogue of a well-known phenomenon
== special point ==
chapters/examples/w3_holographic_datum.tex:293:sometimes called ``the special point''; they must \emph{never} be
== cleanest ==
chapters/examples/w_algebras_deep.tex:266:problem is cleanest in this case. The current manuscript proves the
chapters/examples/beta_gamma.tex:1864:\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
chapters/examples/beta_gamma.tex:1865:\label{rem:betagamma-cleanest-test}
chapters/examples/yangians_drinfeld_kohno.tex:2784:This is the single cleanest CG benchmark for the Bridge Theorem
chapters/examples/n2_superconformal.tex:318:The $\mathcal{N}=2$ SCA provides the cleanest demonstration
== holographic atom principle ==
exec
/bin/zsh -lc "sed -n '258,270p' chapters/examples/w_algebras_deep.tex
printf '\\n---\\n'
sed -n '624,636p' chapters/examples/minimal_model_examples.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$T$ (spin 2) + $W$ (spin 3)
\end{tabular}
\end{center}

The minimal nilpotent $f_{\min} = F_1$ (a single simple root lowering
operator) gives the \emph{Bershadsky--Polyakov algebra}
$\mathcal{W}^k(\mathfrak{sl}_3, f_{\min})$.
The minimal orbit is self-transpose, so the orbit-identification
problem is cleanest in this case. The current manuscript proves the
explicit bar/OPE package and strictness for the BP algebra, but keeps
the level-shifted duality statement itself conjectural
(Conjecture~\ref{conj:bp-duality}).


---
genus; what diverges is the degree summation at fixed genus for
$g \ge 2$. The physical partition function is recovered by
Borel resummation of the degree series
(the generating function is algebraic of degree~$2$, hence
Gevrey-$0$ with no Stokes phenomenon).


thinking
**Considering clarity in titles**

I think "minimal orbit" isn’t too bad, but I could rewrite "is easiest in this case." The user wants slop removal, so maybe "cleanest" is okay to keep. However, it might help to rephrase the remark for clarity. I could also look for words like "optimal" or "pure probe" instead. The titles may need cleaning, too, since they could still feel clunky. I’m wondering if I should consider changing certain title phrases for improved clarity.
thinking
**Evaluating title references**

I need to be cautious about impacting references when changing titles in the prose. The titles are inline, so I can retitle without disrupting references, but I should consider if any index terms include "holographic atom." If that concept appears in other discussions or examples, I might need to keep it. It could be worth removing loaded phrases from the titles for clarity. I should search the repository to confirm if "holographic atom" is in use elsewhere. Perhaps I could simply retitle to "minimal holographic test case."
codex
The strongest slop cluster is in `beta_gamma.tex`; those remarks are structurally sound but phrased like slogans. I’m checking whether those phrases are local names or repeated terms before I rename them.
exec
/bin/zsh -lc "rg -n 'holographic atom|hydrogen atom of modular holography|cleanest modular test|holographic atom principle' chapters/examples/beta_gamma.tex chapters/examples" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'holographic atom|hydrogen atom of modular holography|cleanest modular test|holographic atom principle' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/beta_gamma.tex:1864:\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
chapters/examples/beta_gamma.tex:1870:These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
chapters/examples/beta_gamma.tex:1875:\begin{remark}[The $\beta\gamma$ system as holographic atom]
chapters/examples/beta_gamma.tex:1877:\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
chapters/examples/beta_gamma.tex:1973:\begin{remark}[The holographic atom principle]
chapters/examples/beta_gamma.tex:1975:\index{holographic atom!principle}
chapters/examples/beta_gamma.tex:1976:The $\beta\gamma$ system earns the name ``holographic atom'' for
chapters/examples/beta_gamma.tex:1864:\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
chapters/examples/beta_gamma.tex:1870:These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
chapters/examples/beta_gamma.tex:1875:\begin{remark}[The $\beta\gamma$ system as holographic atom]
chapters/examples/beta_gamma.tex:1877:\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
chapters/examples/beta_gamma.tex:1973:\begin{remark}[The holographic atom principle]
chapters/examples/beta_gamma.tex:1975:\index{holographic atom!principle}
chapters/examples/beta_gamma.tex:1976:The $\beta\gamma$ system earns the name ``holographic atom'' for
 succeeded in 52ms:
./chapters/examples/beta_gamma.tex:1864:\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
./chapters/examples/beta_gamma.tex:1870:These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
./chapters/examples/beta_gamma.tex:1875:\begin{remark}[The $\beta\gamma$ system as holographic atom]
./chapters/examples/beta_gamma.tex:1877:\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
./chapters/examples/beta_gamma.tex:1973:\begin{remark}[The holographic atom principle]
./chapters/examples/beta_gamma.tex:1975:\index{holographic atom!principle}
./chapters/examples/beta_gamma.tex:1976:The $\beta\gamma$ system earns the name ``holographic atom'' for
./wave2_audit_20260413_001942/D09_five_objects_discipline.md:531:\begin{remark}[The $\beta\gamma$ system as holographic atom]
./wave2_audit_20260413_001942/D09_five_objects_discipline.md:533:\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
./compute/audit/linear_read_notes.md:693:| F463 | 2026-04-02 10:40:36 SAST | **SERIOUS** | Beilinson | The next pass found a theorem-level status conflation in `thqg_celestial_holography_extensions.tex`. The theorem `Shadow depth classification of holographic atoms` was collapsing three very different surfaces into one proved classification: a genuinely proved $\beta\gamma$ class~C row, a Kodaira--Spencer large-$N$ defect package whose source chapter only supplies an open-closed benchmark packet while the separate HT/BBL theorematic datum is Gaussian/Gauss--Manin, and a $\mathcal W_3$ row built from an explicitly conjectural modular envelope. I rewrote the whole theorem/proof/complexity-hierarchy packet as an honest status split: $\beta\gamma$ remains the proved class~C theorematic example, Kodaira--Spencer is a benchmark Gauss--Manin/open-closed packet here, and $\mathcal W_3$ is an expected mixed/infinite higher-spin envelope rather than a proved shadow-depth classification on this celestial surface. | **FIXED** |

thinking
**Rephrasing mathematically**

I'm thinking about rephrasing my statement to give it a more mathematical tone. I’d say something like: "This aligns with a standard phenomenon in Quantum Field Theory (QFT): a theory that is well-defined non-perturbatively can possess a divergent perturbation series, where the Borel transform holds additional information." I wonder if this captures the essence of what I'm trying to convey while keeping it clear and precise!
exec
/bin/zsh -lc "sed -n '700,710p' chapters/examples/deformation_quantization_examples.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
sequence of $\bar{B}(\mathcal{A}^!)$: on the $E_1$ page, the generators
contributed by $m_k$ vanish for $k \geq d$, so the spectral sequence has
nonzero differentials only up to page $E_{d-1}$. For $d = 2$ it
collapses at $E_1$ (acyclicity); for $d = 3$ at $E_2$ (the classical
derived category); and for $d \geq 4$ the pages $E_3, \ldots, E_{d-1}$
carry genuinely $A_\infty$ information invisible to classical algebraic
geometry. This hierarchy gives a concrete filtration-theoretic meaning
to the slogan ``the degree of $W$ controls the homotopy depth of $\dCrit(W)$.''
\end{remark}

\begin{remark}[Three-pillar interpretation: deformation quantization]
codex
This touches HZ-10 directly, so I’m doing the prose-hygiene pre-edit check before patching. After that I’ll edit the small set of genuinely rhetorical lines I’ve confirmed in context.
exec
/bin/zsh -lc "rg -n 'PE-12|prose hygiene' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
350:**prose hygiene**
649:Fill-in-the-blank templates mandatory BEFORE writing the listed formula classes. Filling out a template IS the verification; the blank forces the computation; the computation catches the error. Source: pre_edit_verification_protocol_wave12.md (PE-1 through PE-12 full entries).
653:Eight highest-priority templates follow. Remaining four (PE-3 complementarity, PE-6 exceptional dimensions, PE-9 summation boundary, PE-12 prose hygiene) are in the source draft.
818:Remaining templates PE-3 (complementarity), PE-6 (exceptional dimensions), PE-9 (summation boundary), PE-12 (prose hygiene) in `compute/audit/pre_edit_verification_protocol_wave12.md`.
1043:1. Read this file. 2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. 3. Tests: `make test`. 4. `git log --oneline -10`. 5. Read .tex source before any edit (never from memory). 6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5). 7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1). 8. Apply convergent writing loop to all prose. 9. Session end: build all three volumes, run tests, summarize errors by class. 10. Before first Edit, read the HOT ZONE section (HZ-1 through HZ-10) and run the Pre-Edit Verification Protocol mental check: is the pending edit touching an r-matrix, kappa, bar complex, label, Vol III kappa, cross-volume formula, scope quantifier, or differential form? If yes, fill the corresponding PE-1..PE-12 template as a fenced block in the reply BEFORE invoking Edit, ending with `verdict: ACCEPT`.
exec
/bin/zsh -lc "nl -ba chapters/examples/deformation_quantization.tex | sed -n '82,90p'
nl -ba chapters/examples/w_algebras_deep.tex | sed -n '1092,1104p'
nl -ba chapters/examples/beta_gamma.tex | sed -n '242,252p'
nl -ba chapters/examples/beta_gamma.tex | sed -n '1862,1884p'
nl -ba chapters/examples/beta_gamma.tex | sed -n '1972,1988p'
nl -ba chapters/examples/genus_expansions.tex | sed -n '656,666p'
nl -ba chapters/examples/genus_expansions.tex | sed -n '1900,1908p'
nl -ba chapters/examples/lattice_foundations.tex | sed -n '3502,3524p'
nl -ba chapters/examples/bershadsky_polyakov.tex | sed -n '456,462p'
nl -ba chapters/examples/free_fields.tex | sed -n '2420,2428p'
nl -ba chapters/examples/free_fields.tex | sed -n '6068,6076p'
nl -ba chapters/examples/deformation_quantization_examples.tex | sed -n '200,206p'
nl -ba chapters/examples/deformation_quantization_examples.tex | sed -n '704,710p'
nl -ba chapters/examples/minimal_model_examples.tex | sed -n '628,636p'
nl -ba chapters/examples/minimal_model_examples.tex | sed -n '720,732p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    82	
    83	\subsection{Role of the upper half-plane}
    84	
    85	The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
    86	
    87	The key geometric fact: the Kontsevich configuration spaces $C_{n,m}(\mathbb{H})$ (of $n$ interior and $m$ boundary points, modulo $\operatorname{Aff}(\mathbb{R})$) have FM-type compactifications $\overline{C}_{n,m}(\mathbb{H})$ whose boundary strata are governed by the operad structure of the Stasheff associahedra $K_\bullet$ and the little 2-disks operad $E_2$. In particular, the boundary stratification encodes the same combinatorics as the real moduli spaces $\overline{\mathcal{M}}_{0,m}(\mathbb{R})$.
    88	
    89	\section{Chiral algebras as quantum observables}
    90	
  1092	(Computation~\ref{comp:ds-bar-sl3-w3}, Step~3). The curvature
  1093	compatibility: the KM curvature $(k+3)\kappa/6$ projects under DS
  1094	to $c/2$ (Step~4 of the same computation).
  1095	
  1096	The point: the ``residue-side'' OPE coefficients
  1097	$\mathsf{C}^{\mathrm{res}}$ (extracted from the
  1098	$\mathcal{W}_3$ OPE on $\overline{C}_n(X)$) and the
  1099	``DS-side'' coefficients $\mathsf{C}^{\mathrm{DS}}$ (the DS
  1100	projection of the KM bar complex) are \emph{entries of the same
  1101	chain complex}, identified by the proved intertwining theorem.
  1102	They match by the intertwining theorem.
exec
/bin/zsh -lc "sed -n '150,240p' compute/audit/pre_edit_verification_protocol_wave12.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  dual Coxeter h^v:        E_8=30, E_7=18, E_6=12, F_4=9, G_2=4, sl_n=n, so_{2n}=2n-2, so_{2n+1}=2n-1, sp_{2n}=n+1
written value in set?      [Y/N]   # must be Y
source for value:          [landscape_census.tex line _____ / Bourbaki ch. _____ / Atlas / computed]
AP10 derivation paths (>=2):
  path 1:                  [_____]
  path 2:                  [_____]
```

**Reject condition**: value not in canonical set, or fewer than 2 derivation paths, or missing source.

---

## Template 7 -- Label creation (AP124, AP125)

**Trigger**: Any `\label{...}` write, any new theorem/proposition/conjecture/definition/remark/lemma.

```
## PRE-EDIT: label
environment:               [theorem / proposition / conjecture / definition / remark / lemma / corollary / section]
label written:             \label{[_____]:[_____]}
exec
/bin/zsh -lc "sed -n '240,340p' compute/audit/pre_edit_verification_protocol_wave12.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
**Trigger**: Any theorem statement, any formula for obs_g / F_g / lambda_g / m_k, any universal quantifier.

```
## PRE-EDIT: scope quantifier
statement:                 [_______________________________]
genus specified?           [g = 0 / g = 1 / g >= 2 / all g / unspecified -- REJECT]
arity specified?           [n = _____ / all n / unspecified -- REJECT]
level (convolution vs ambient)? [convolution M-bar_{g,n} / ambient Mok25 log FM / both / N/A]
AP32 uniform-weight tag:   (if obs_g / F_g / lambda_g present)
  tag:                     [(UNIFORM-WEIGHT) / (ALL-WEIGHT with delta F_g^cross) / N/A]
  tagged in statement?     [Y/N]   # must be Y for any g >= 2 claim
AP139 free-variable audit:
  variables on LHS:        {_____}
  variables on RHS:        {_____}
  LHS \supseteq RHS?       [Y/N]   # if N, bind the free variable or reject
AP7 universal quantifier: does "for all" hide a hypothesis?  [Y/N]
  hidden hypotheses:       [_____]
AP36 implies vs iff:       [implies / iff]
  if iff, converse proved in same theorem?  [Y/N]
```






thinking
**Rethinking title and index terms**

I'm considering renaming it to remove any sloppiness. If the index term exists, I wonder if I should preserve the concept. Perhaps I can keep the title as "The $\beta\gamma$ system as a minimal holographic test case," while updating the index terms to just "minimal holographic test case." But then again, I worry that it might be too much. It's a bit of a balancing act, deciding on clarity versus simplicity.
thinking
**Summarizing the paragraph**

I need to rewrite the entire paragraph into 2-3 sentences. It’s about identifying the Virasoro complementarity sum alongside the bosonic-string curvature contribution that includes 13 free bosons. The goal is to condense this information while keeping the key concepts intact for clarity. Let’s keep it straightforward and ensure that the essence of the original text is preserved in my new version!
thinking
**Editing technical content**

I’m working through some technical details regarding the bosonic string anomaly and affine complementarity. There's a factor of 1/2 in the equation, which I should double-check. I need to fix punctuation before mentioning that affine complementarity is exact and might want to add a semicolon. Also, I want to rephrase a line to reflect the family index theorem. 

For the rewrite, I’ll clarify some sections to describe methods producing \Eone-chiral algebras. I’m questioning the importance of some descriptors, like abelian/non-abelian, in this context.
thinking
**Refining technical statements**

I’m reviewing specific lines for clarity and precision. For the passage about complementary roles, I see it reflects how minimal and principal reductions account for the full anomaly of the parent algebra, which is good. 

Next, I want to rewrite the final sentence in free_fields to maybe split it for better readability. Also, I need to clarify that non-strictness results from FM compactification, not from \v{C}ech descent. Lastly, for the chiral WZW model, I’ll ensure it’s clear that “wrong level” indicates a failure to satisfy quantization.
thinking
**Considering language clarity**

I’m noticing that while there are many examples to consider, not all might need the same treatment. The user mentioned wanting a consistent approach to slop removal for all examples. I'm thinking about perhaps removing rhetorical adjectives for clarity, but the scope of that could be quite large. It feels a bit overwhelming, and I'd want to ensure I’m not over-complicating things. Let's aim for consistency while keeping it manageable!
thinking
**Inspecting concepts**

I'm thinking about concepts like coincidence, top-down vs. bottom-up approaches, and hydrogen atoms. There's mention of holographic atoms and strong coupling, but it feels like I might be considering the wrong level of detail. After this thought process, I might conclude that I have enough to analyze. So, I’ll take a closer look at `yangians_drinfeld_kohno` and see what’s the cleanest, and also check into `n2_superconformal`.
codex
I’ve isolated a second tier of rhetorical adjectives (`cleanest`, similar superlatives) that weren’t in the blacklist but are still prose noise. I’m checking those remaining hits now so I can decide whether they need the same treatment or are carrying actual mathematical distinctions.
exec
/bin/zsh -lc "for pat in 'cleanest' 'optimal' 'simplest example of a worldsheet' 'hydrogen atom' 'holographic atom' 'The point:' 'This is not a coincidence' 'top-down' 'bottom-up' 'The correct slogan is:' 'earns the name' 'pure probe' 'uncontaminated by' 'strongly coupled' 'wrong''; do echo \"== "'$pat =="; rg -n --glob '"'*.tex' -F \""'$pat" chapters/examples || true; done' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '2778,2788p'
nl -ba chapters/examples/n2_superconformal.tex | sed -n '314,322p'
nl -ba chapters/examples/w_algebras_deep.tex | sed -n '262,268p'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: unmatched '
 succeeded in 50ms:
  2778	In the language of the shadow obstruction tower
  2779	(\S\ref{sec:nms-shadow-calculus}), $r(z)$ is the
  2780	same-genus, degree-$2$ slice of~$\Theta_\cA$: the scalar
  2781	shadow~$\kappa(\cA)$ is the trace of this slice, and $r(z)$ is
  2782	the full tensorial content.
  2783	
  2784	This is the single cleanest CG benchmark for the Bridge Theorem
  2785	package: compute $\tau|_{\deg 2}$ explicitly in each benchmark
  2786	family and verify it matches the known $r$-matrix.
  2787	\end{remark}
  2788	
   314	
   315	\begin{remark}[The CE/chiral bar gap]
   316	\label{rem:n2-ce-chiral-gap}
   317	\index{N=2 superconformal algebra!CE vs chiral bar}
   318	The $\mathcal{N}=2$ SCA provides the cleanest demonstration
   319	in the standard landscape that CE Koszulness (vanishing of
   320	$H^2_{\mathrm{CE}}(\mathfrak{g}_-)$) and chiral Koszulness
   321	(vanishing of $H^2(\barB(A))$) are genuinely distinct properties.
   322	For single-generator algebras (Heisenberg, Virasoro), the two

thinking
**Considering command options**

I’m thinking about using Python, but I realize that simple shell commands might work better. I can use `rg -n --glob '*.tex' -e 'cleanest' -e 'optimal' ...`, but then I remember that using apostrophes in the pattern won't work. I need to make sure I'm using the right syntax to get the results I want. Let’s give this command a shot and see how it goes!
exec
/bin/zsh -lc "rg -n --glob '*.tex' -e 'cleanest' -e 'optimal' -e 'simplest object' -e 'simplest example' -e 'pure probe' -e 'uncontaminated' -e 'hydrogen atom' -e 'holographic atom' -e 'slogan' -e 'temptation' -e 'not a coincidence' -e 'top-down' -e 'bottom-up' -e 'use up' -e 'strongly coupled' -e 'The point:' chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:85:The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
chapters/examples/w_algebras_deep.tex:234:globalize, not to blur that boundary into a single slogan. Concretely,
chapters/examples/w_algebras_deep.tex:266:problem is cleanest in this case. The current manuscript proves the
chapters/examples/w_algebras_deep.tex:1096:The point: the ``residue-side'' OPE coefficients
chapters/examples/y_algebras.tex:368:$Y_{1,1,1}$ algebra is the simplest example in the standard
chapters/examples/w3_holographic_datum.tex:40:the temptation to set this to zero by analogy with the affine
chapters/examples/minimal_model_examples.tex:635:is ``strongly coupled'' in the shadow obstruction tower sense, even though it
chapters/examples/minimal_model_examples.tex:726:most exactly solvable CFTs are the most ``strongly coupled'' in the
chapters/examples/n2_superconformal.tex:318:The $\mathcal{N}=2$ SCA provides the cleanest demonstration
chapters/examples/deformation_quantization_examples.tex:707:to the slogan ``the degree of $W$ controls the homotopy depth of $\dCrit(W)$.''
chapters/examples/genus_expansions.tex:659:is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
chapters/examples/genus_expansions.tex:1904:substitution $x \mapsto ix$. This is not a coincidence: the family
chapters/examples/bershadsky_polyakov.tex:459:and principal reductions: together they ``use up'' the full
chapters/examples/yangians_drinfeld_kohno.tex:2784:This is the single cleanest CG benchmark for the Bridge Theorem
chapters/examples/beta_gamma.tex:245:A natural temptation is to write ``$\beta\gamma$ has shadow depth
chapters/examples/beta_gamma.tex:1864:\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
chapters/examples/beta_gamma.tex:1865:\label{rem:betagamma-cleanest-test}
chapters/examples/beta_gamma.tex:1866:The $\beta\gamma$ system is optimal for testing the modular envelope because:
chapters/examples/beta_gamma.tex:1870:These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
chapters/examples/beta_gamma.tex:1875:\begin{remark}[The $\beta\gamma$ system as holographic atom]

thinking
**Evaluating potential edits**

I need to decide whether to edit several elements like y_algebras and w3_holographic_datum temptation. Some might be okay, but if I search after the edit, there could still be remaining references like "single slogan." I wonder if the user expects all issues to be addressed. It seems like I should strive to fix genuinely sloppy phrases based on search outputs. I'll inspect the remaining contexts for examples and see if they're just prose noise that can be improved.
codex
I’m expanding the patch slightly. A few remaining hits aren’t in the blacklist but are the same kind of rhetorical filler, so I’m reading those before I commit the edit set.
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras_deep.tex | sed -n '228,236p'
nl -ba chapters/examples/y_algebras.tex | sed -n '364,372p'
nl -ba chapters/examples/w3_holographic_datum.tex | sed -n '36,44p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '3878,3888p'
nl -ba chapters/examples/deformation_quantization.tex | sed -n '84,88p'
nl -ba chapters/examples/beta_gamma.tex | sed -n '1874,1884p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   228	This section has three layers. Principal finite-type W-algebras remain
   229	part of the proved core; the $\mathfrak{sl}_3$ minimal/subregular
   230	computations and the hook-type family results provide the first
   231	non-principal theorematic seeds; the global non-principal transport
   232	statement remains Conjecture~\ref{conj:w-orbit-duality}. The purpose of
   233	the section is to isolate the mechanism that a future theorem must
   234	globalize, not to blur that boundary into a single slogan. Concretely,
   235	the remaining non-principal work is threefold: determine the dual-orbit
   236	input, determine the orbit-indexed level shift, and globalize the
   364	\begin{remark}[$\kappa \neq c/2$ for $Y_{1,1,1}$]%
   365	\label{rem:y111-kappa-not-c-over-2}
   366	\index{kappa@$\kappa$!not c/2@$\neq c/2$}
   367	Since $c = 0$ but $\kappa = \Psi \neq 0$ generically, the
   368	$Y_{1,1,1}$ algebra is the simplest example in the standard
   369	landscape where $\kappa \neq c/2$. The
   370	formula $\kappa = c/2$ requires the Virasoro sector to be the
   371	\emph{sole} contributor to the genus-$1$ bar obstruction
   372	. For $Y_{1,1,1}$, the Heisenberg channel dominates
    36	$c$-dependent coefficient $\alpha(c) = 16/(22+5c)$;
    37	(iii)~Koszul duality is the nontrivial involution $c \mapsto 100 - c$,
 succeeded in 52ms:
  3878	\section{Free fermion genus expansion and spin structures}
  3879	\label{sec:free-fermion-genus-expansion}
  3880	\index{free fermion!genus expansion|textbf}
  3881	\index{spin structure!genus expansion}
  3882	
  3883	The free fermion $\cF$ ($c = 1/2$, $\kappa = 1/4$) is
  3884	the simplest example where spin structures enter the genus
  3885	expansion. The Heisenberg genus expansion
  3886	(Chapter~\ref{ch:heisenberg-frame}) involves determinants of
  3887	the $\bar\partial$ operator on the trivial line bundle; the free
  3888	fermion replaces determinants with Pfaffians and theta functions
    84	
    85	The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
    86	
    87	The key geometric fact: the Kontsevich configuration spaces $C_{n,m}(\mathbb{H})$ (of $n$ interior and $m$ boundary points, modulo $\operatorname{Aff}(\mathbb{R})$) have FM-type compactifications $\overline{C}_{n,m}(\mathbb{H})$ whose boundary strata are governed by the operad structure of the Stasheff associahedra $K_\bullet$ and the little 2-disks operad $E_2$. In particular, the boundary stratification encodes the same combinatorics as the real moduli spaces $\overline{\mathcal{M}}_{0,m}(\mathbb{R})$.
    88	
  1874	%% ================================================================
  1875	\begin{remark}[The $\beta\gamma$ system as holographic atom]
  1876	\label{rem:betagamma-holographic-atom}
  1877	\index{beta-gamma system@$\beta\gamma$ system!holographic atom}

thinking
**Considering patching strategy**

I'm thinking about whether to search for "cleanest" after a patch, which might still be relevant in n2. We can patch that. Searching for "simplest" might work in other contexts but isn't necessary for slop removal, which is our main focus. I need to carefully consider patching beta_gamma titles and indices. There's a risk in editing those titles and indices that could require updating references, but it seems titles and index terms can stay as they are. Everything should be okay!
codex
```text
## PRE-EDIT: prose hygiene
text block (first 20 words): The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents
AI-slop scan (forbidden): notably, crucially, remarkably, interestingly, furthermore, moreover,
                          delve, leverage, tapestry, cornerstone, importantly, in essence
  any hits?                N
em-dash scan:              any `--` or `---` or unicode em-dash?  N
markdown leak (AP121):     any backtick numerals `29`?  N
                           any **bold** or _italic_?    N
AAP1 injection check:      any `antml` or `</invoke>` in file?  N
passive-voice hedge scan:  "it can be shown that", "we may note that", "it is worth noting"  N
scope explicitly stated?   Y
state-once-prove-once?     Y
verdict: ACCEPT
```

I’m patching the confirmed rhetorical lines now. The edit set is limited to the affected files under `chapters/examples`.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization.tex
@@ -84,3 +84,3 @@
 
-The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
+The upper half-plane $\mathbb{H}$ is the basic bordered surface in Kontsevich's construction: boundary insertions lie on $\mathbb{R} \subset \partial\mathbb{H}$, internal vertices lie in $\mathbb{H}$, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
 
M /Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex
@@ -201,3 +201,3 @@
 \begin{enumerate}[label=(\roman*)]
-\item Chiral WZW model with ``wrong'' level has $\mathrm{Obs} \neq 0$.
+\item Chiral WZW model at nonintegral level has $\mathrm{Obs} \neq 0$.
 \item The obstruction is the \emph{level quantization condition}: the
@@ -705,4 +705,4 @@
 carry genuinely $A_\infty$ information invisible to classical algebraic
-geometry. This hierarchy gives a concrete filtration-theoretic meaning
-to the slogan ``the degree of $W$ controls the homotopy depth of $\dCrit(W)$.''
+geometry. This hierarchy makes precise the statement that the degree
+of $W$ controls the homotopy depth of $\dCrit(W)$.
 \end{remark}
M /Users/raeez/chiral-bar-cobar/chapters/examples/bershadsky_polyakov.tex
@@ -458,3 +458,3 @@
 1/6 + 5/6 = 1$ reflects the complementary roles of the minimal
-and principal reductions: together they ``use up'' the full
+and principal reductions: together they account for the full
 anomaly of the parent algebra.
M /Users/raeez/chiral-bar-cobar/chapters/examples/minimal_model_examples.tex
@@ -629,9 +629,7 @@
 
-This is the chiral-algebraic analogue of a well-known phenomenon
-in quantum field theory: the perturbation series of a
-non-perturbatively well-defined theory can diverge, with the
-divergence encoding non-perturbative information through its
-Borel transform. Here $\rho \gg 1$ signals that the Ising model
-is ``strongly coupled'' in the shadow obstruction tower sense, even though it
-is free (in the sense of admitting a free-fermion realization).
+This matches a standard phenomenon in quantum field theory: the
+perturbation series of a non-perturbatively well-defined theory can
+diverge, with the Borel transform encoding additional information.
+Here $\rho \gg 1$ means that the Ising model has rapid shadow-tower
+growth even though it admits a free-fermion realization.
 \end{remark}
@@ -724,5 +722,4 @@
 has $\rho' < 1$ (convergent). The minimal models thus illustrate
-the shadow complementarity principle at its sharpest: the simplest,
-most exactly solvable CFTs are the most ``strongly coupled'' in the
-shadow obstruction tower sense.
+the shadow complementarity principle sharply: on the unitary minimal
+line, smaller central charge corresponds to larger shadow growth.
 \end{remark}
M /Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex
@@ -244,4 +244,4 @@
 \label{warn:bg-ap59}
-A natural temptation is to write ``$\beta\gamma$ has shadow depth
-$1$'' because the generator OPE has a simple pole. This is wrong on
+The statement ``$\beta\gamma$ has shadow depth
+$1$'' is wrong on
 three counts. \textup{(}a\textup{)}~The shadow depth $r_{\max}$ is
@@ -1863,5 +1863,5 @@
 
-\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
+\begin{remark}[The $\beta\gamma$ system as a minimal modular test case]
 \label{rem:betagamma-cleanest-test}
-The $\beta\gamma$ system is optimal for testing the modular envelope because:
+The $\beta\gamma$ system is a minimal test case for the modular envelope because:
 (1)~the OPE is free (single simple pole, no higher singularities);
@@ -1869,3 +1869,3 @@
 (3)~genus dependence enters entirely through determinant-line geometry on curves.
-These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
+These three properties isolate the global modular contribution from local higher-operation corrections.
 \end{remark}
@@ -1874,10 +1874,10 @@
 %% ================================================================
-\begin{remark}[The $\beta\gamma$ system as holographic atom]
+\begin{remark}[A minimal holographic test case]
 \label{rem:betagamma-holographic-atom}
-\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
-\index{holomorphic-topological!beta-gamma atom@$\beta\gamma$ atom}
+\index{beta-gamma system@$\beta\gamma$ system!minimal holographic test case}
+\index{holomorphic-topological!beta-gamma test case@$\beta\gamma$ test case}
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
-controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which the boundary algebra, the Koszul-dual defect
+controls the genus expansion. The $\beta\gamma$ system is therefore a
+minimal example in which the boundary algebra, the Koszul-dual defect
 sector, and the derived-center bulk are all explicitly computable.
@@ -1972,10 +1972,9 @@
 
-\begin{remark}[The holographic atom principle]
+\begin{remark}[Determinantal genus expansion for $\beta\gamma$]
 \label{rem:betagamma-holographic-atom-principle}
-\index{holographic atom!principle}
-The $\beta\gamma$ system earns the name ``holographic atom'' for
-precisely this reason: local algebraic triviality ($m_k = 0$ for
+\index{beta-gamma system@$\beta\gamma$ system!determinantal genus expansion}
+Local algebraic triviality ($m_k = 0$ for
 $k \geq 3$) strips away all combinatorial complexity of curved
 $A_\infty$ corrections, leaving the genus expansion
-$Z_{\beta\gamma}(\hbar)$ as a pure probe of the global geometry of
+$Z_{\beta\gamma}(\hbar)$ governed by the global geometry of
 moduli. Every term $\chi_{\mathrm{gr}}(H_g^{\beta\gamma})$ is, by
@@ -1985,3 +1984,3 @@
 factorization homology interacts with stable-curve compactification,
-uncontaminated by local nonlinearity. Any failure of the modular
+with no local nonlinear correction terms. Any failure of the modular
 package at the $\beta\gamma$ level is therefore a failure of the
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex
@@ -2783,3 +2783,3 @@
 
-This is the single cleanest CG benchmark for the Bridge Theorem
+This is a concrete CG benchmark for the Bridge Theorem
 package: compute $\tau|_{\deg 2}$ explicitly in each benchmark
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -2423,3 +2423,3 @@
 \index{genus universality!Ext algebra}
-The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
+The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. Thus the same invariant $\kappa(\mathcal{H}_k)$ controls both the module Ext Euler characteristic and the genus expansion.
 \end{remark}
@@ -3883,3 +3883,3 @@
 The free fermion $\cF$ ($c = 1/2$, $\kappa = 1/4$) is
-the simplest example where spin structures enter the genus
+an example where spin structures enter the genus
 expansion. The Heisenberg genus expansion
@@ -6069,3 +6069,3 @@
 nonzero and a genuine homotopy $F_3$ would be needed; strictness
-would then depend on the algebra. The correct slogan is:
+would then depend on the algebra. Equivalently,
 \emph{non-strictness is a bar-side phenomenon on $\mathbb{P}^1$,
M /Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex
@@ -233,3 +233,3 @@
 the section is to isolate the mechanism that a future theorem must
-globalize, not to blur that boundary into a single slogan. Concretely,
+globalize without obscuring that status boundary. Concretely,
 the remaining non-principal work is threefold: determine the dual-orbit
@@ -265,3 +265,3 @@
 The minimal orbit is self-transpose, so the orbit-identification
-problem is cleanest in this case. The current manuscript proves the
+problem reduces most directly in this case. The current manuscript proves the
 explicit bar/OPE package and strictness for the BP algebra, but keeps
@@ -1095,3 +1095,3 @@
 
-The point: the ``residue-side'' OPE coefficients
+The ``residue-side'' OPE coefficients
 $\mathsf{C}^{\mathrm{res}}$ (extracted from the
@@ -1101,3 +1101,2 @@
 chain complex}, identified by the proved intertwining theorem.
-They match by the intertwining theorem.
 
M /Users/raeez/chiral-bar-cobar/chapters/examples/y_algebras.tex
@@ -367,3 +367,3 @@
 Since $c = 0$ but $\kappa = \Psi \neq 0$ generically, the
-$Y_{1,1,1}$ algebra is the simplest example in the standard
+$Y_{1,1,1}$ algebra is an explicit example in the standard
 landscape where $\kappa \neq c/2$. The
M /Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex
@@ -3505,4 +3505,4 @@
  (this section): start with an $\Einf$-chiral lattice VOA and
- deform the cocycle to break symmetry. This is a ``top-down''
- method: the state space is fixed, and the OPE acquires phases.
+ deform the cocycle to break symmetry. The state space is fixed,
+ and the OPE acquires phases.
  The deformation is controlled by a finite parameter ($N$, $q$).
@@ -3511,4 +3511,4 @@
  build the $\Eone$-chiral algebra from generators and relations.
- This is a ``bottom-up'' method: the algebra is presented by
- generators with an $R$-matrix-valued OPE.
+ The algebra is presented by generators with an
+ $R$-matrix-valued OPE.
 \end{enumerate}
@@ -3519,5 +3519,4 @@
 The bridge between the two constructions is the Frenkel--Kac--Segal
-theorem: method~(a) produces $\Eone$-chiral algebras from lattices
-(the ``abelian'' source), while method~(b) produces them from
-quantum groups (the ``non-abelian'' source). At level~1 with
+theorem: method~(a) produces $\Eone$-chiral algebras from lattice
+VOAs, while method~(b) produces them from quantum groups. At level~1 with
 symmetric cocycle, FKS identifies the two; the deformed FKS
M /Users/raeez/chiral-bar-cobar/chapters/examples/w3_holographic_datum.tex
@@ -38,4 +38,4 @@
 producing a complementarity sum that takes the manifestly nonzero
-constant value $250/3$ ( guards against
-the temptation to set this to zero by analogy with the affine
+constant value $250/3$ (this rules out
+the affine-style conclusion that the sum should vanish
 case);
M /Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex
@@ -659,2 +659,3 @@
 is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
+is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This reflects the Koszul-dual form of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The factor $1/2$ comes from $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ accounts for half of the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$; the affine complementarity is \emph{exact}, with no residual anomaly.
 \end{remark}
@@ -1903,3 +1904,3 @@
 $\hat{A}$-genus: $\hat{A}(x) = (x/2)/\sinh(x/2)$, related by the
-substitution $x \mapsto ix$. This is not a coincidence: the family
+substitution $x \mapsto ix$. This reflects the family
 index theorem (Theorem~\ref{thm:family-index}) shows that
M /Users/raeez/chiral-bar-cobar/chapters/examples/n2_superconformal.tex
@@ -317,3 +317,3 @@
 \index{N=2 superconformal algebra!CE vs chiral bar}
-The $\mathcal{N}=2$ SCA provides the cleanest demonstration
+The $\mathcal{N}=2$ SCA provides a direct demonstration
 in the standard landscape that CE Koszulness (vanishing of
apply_patch(auto_approved=true) exited 0 in 112ms:
Success. Updated the following files:
M chapters/examples/deformation_quantization.tex
M chapters/examples/w_algebras_deep.tex
M chapters/examples/beta_gamma.tex
M chapters/examples/genus_expansions.tex
M chapters/examples/lattice_foundations.tex
M chapters/examples/bershadsky_polyakov.tex
M chapters/examples/free_fields.tex
M chapters/examples/deformation_quantization_examples.tex
M chapters/examples/minimal_model_examples.tex
M chapters/examples/yangians_drinfeld_kohno.tex
M chapters/examples/n2_superconformal.tex
M chapters/examples/y_algebras.tex
M chapters/examples/w3_holographic_datum.tex
file update:
diff --git a/chapters/examples/bershadsky_polyakov.tex b/chapters/examples/bershadsky_polyakov.tex
index 2ad638fef7b5e29d8ec1346b6adb2748625ce3f3..05f1c366202f6a50049685ad6a76174e355bb884
--- a/chapters/examples/bershadsky_polyakov.tex
+++ b/chapters/examples/bershadsky_polyakov.tex
@@ -456,7 +456,7 @@
 
 The pattern $\varrho(\mathcal{B}^k) + \varrho(\mathcal{W}_3) =
 1/6 + 5/6 = 1$ reflects the complementary roles of the minimal
-and principal reductions: together they ``use up'' the full
+and principal reductions: together they account for the full
 anomaly of the parent algebra.
 
 \begin{remark}[Relation to the $\mathcal{N}=2$ SCA]
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 32f68d6b6583630d06ac1ccb670a3436706c04df..f5196ca9d0dd2419f293707e8ccc20268dc43534
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -242,8 +242,8 @@
 
 \begin{warning}[never conflate $p_{\max}$, $k_{\max}$, $r_{\max}$]
 \label{warn:bg-ap59}
-A natural temptation is to write ``$\beta\gamma$ has shadow depth
-$1$'' because the generator OPE has a simple pole. This is wrong on
+The statement ``$\beta\gamma$ has shadow depth
+$1$'' is wrong on
 three counts. \textup{(}a\textup{)}~The shadow depth $r_{\max}$ is
 not the OPE pole order. \textup{(}b\textup{)}~By $d\log$ absorption
 the collision residue has pole order $p_{\max} - 1 = 0$, not~$1$.
@@ -1861,25 +1861,25 @@
 \end{enumerate}
 \end{conjecture}
 
-\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
+\begin{remark}[The $\beta\gamma$ system as a minimal modular test case]
 \label{rem:betagamma-cleanest-test}
-The $\beta\gamma$ system is optimal for testing the modular envelope because:
+The $\beta\gamma$ system is a minimal test case for the modular envelope because:
 (1)~the OPE is free (single simple pole, no higher singularities);
 (2)~all higher $A_\infty$ operations vanish ($m_k = 0$ for $k \ge 3$);
 (3)~genus dependence enters entirely through determinant-line geometry on curves.
-These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
+These three properties isolate the global modular contribution from local higher-operation corrections.
 \end{remark}
 
 
 %% ================================================================
-\begin{remark}[The $\beta\gamma$ system as holographic atom]
+\begin{remark}[A minimal holographic test case]
 \label{rem:betagamma-holographic-atom}
-\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
-\index{holomorphic-topological!beta-gamma atom@$\beta\gamma$ atom}
+\index{beta-gamma system@$\beta\gamma$ system!minimal holographic test case}
+\index{holomorphic-topological!beta-gamma test case@$\beta\gamma$ test case}
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
-controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which the boundary algebra, the Koszul-dual defect
+controls the genus expansion. The $\beta\gamma$ system is therefore a
+minimal example in which the boundary algebra, the Koszul-dual defect
 sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
@@ -1970,20 +1970,19 @@
 where $\chi_{\mathrm{gr}}$ denotes the graded Euler characteristic.
 \end{definition}
 
-\begin{remark}[The holographic atom principle]
+\begin{remark}[Determinantal genus expansion for $\beta\gamma$]
 \label{rem:betagamma-holographic-atom-principle}
-\index{holographic atom!principle}
-The $\beta\gamma$ system earns the name ``holographic atom'' for
-precisely this reason: local algebraic triviality ($m_k = 0$ for
+\index{beta-gamma system@$\beta\gamma$ system!determinantal genus expansion}
+Local algebraic triviality ($m_k = 0$ for
 $k \geq 3$) strips away all combinatorial complexity of curved
 $A_\infty$ corrections, leaving the genus expansion
-$Z_{\beta\gamma}(\hbar)$ as a pure probe of the global geometry of
+$Z_{\beta\gamma}(\hbar)$ governed by the global geometry of
 moduli. Every term $\chi_{\mathrm{gr}}(H_g^{\beta\gamma})$ is, by
 Conjecture~\ref{conj:betagamma-determinant-control}, a determinant-line
 invariant on $\mathcal{M}_g$, so the generating function
 \eqref{eq:betagamma-partition-function} records how
 factorization homology interacts with stable-curve compactification,
-uncontaminated by local nonlinearity. Any failure of the modular
+with no local nonlinear correction terms. Any failure of the modular
 package at the $\beta\gamma$ level is therefore a failure of the
 global gluing axioms, not of local algebra.
 
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index d3c313626eef51ed5297969981f9dec7e46681e4..627a77efbd20dc3a33e2196a96706b82d81646ae
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -82,7 +82,7 @@
 
 \subsection{Role of the upper half-plane}
 
-The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
+The upper half-plane $\mathbb{H}$ is the basic bordered surface in Kontsevich's construction: boundary insertions lie on $\mathbb{R} \subset \partial\mathbb{H}$, internal vertices lie in $\mathbb{H}$, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
 
 The key geometric fact: the Kontsevich configuration spaces $C_{n,m}(\mathbb{H})$ (of $n$ interior and $m$ boundary points, modulo $\operatorname{Aff}(\mathbb{R})$) have FM-type compactifications $\overline{C}_{n,m}(\mathbb{H})$ whose boundary strata are governed by the operad structure of the Stasheff associahedra $K_\bullet$ and the little 2-disks operad $E_2$. In particular, the boundary stratification encodes the same combinatorics as the real moduli spaces $\overline{\mathcal{M}}_{0,m}(\mathbb{R})$.
 
diff --git a/chapters/examples/deformation_quantization_examples.tex b/chapters/examples/deformation_quantization_examples.tex
index a4f5ccf2fe43661b3a1a49736abf5677b42bbb9f..7964bf6c71c487f016699ff42102478ce3800126
--- a/chapters/examples/deformation_quantization_examples.tex
+++ b/chapters/examples/deformation_quantization_examples.tex
@@ -199,7 +199,7 @@
 \begin{example}[Obstruction: anomalous theories]\label{ex:anomaly}
 Certain physical theories have obstructions:
 \begin{enumerate}[label=(\roman*)]
-\item Chiral WZW model with ``wrong'' level has $\mathrm{Obs} \neq 0$.
+\item Chiral WZW model at nonintegral level has $\mathrm{Obs} \neq 0$.
 \item The obstruction is the \emph{level quantization condition}: the
  Wess--Zumino class $[H] \in H^3(G, \mathbb{Z})$ requires $k \in \mathbb{Z}$
  for the path integral to be well-defined (arising from $\pi_3(G) \cong \mathbb{Z}$).
@@ -703,8 +703,8 @@
 collapses at $E_1$ (acyclicity); for $d = 3$ at $E_2$ (the classical
 derived category); and for $d \geq 4$ the pages $E_3, \ldots, E_{d-1}$
 carry genuinely $A_\infty$ information invisible to classical algebraic
-geometry. This hierarchy gives a concrete filtration-theoretic meaning
-to the slogan ``the degree of $W$ controls the homotopy depth of $\dCrit(W)$.''
+geometry. This hierarchy makes precise the statement that the degree
+of $W$ controls the homotopy depth of $\dCrit(W)$.
 \end{remark}
 
 \begin{remark}[Three-pillar interpretation: deformation quantization]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index a4d4d1d9f2650b81b850aad00e336484a4b101c6..daf9be2b2efbe2f0b0c98381dc849c46bb35bc2d
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2421,7 +2421,7 @@
 \begin{remark}[Ext algebra and the genus universality invariant]
 \label{rem:ext-genus-universality}
 \index{genus universality!Ext algebra}
-The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
+The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. Thus the same invariant $\kappa(\mathcal{H}_k)$ controls both the module Ext Euler characteristic and the genus expansion.
 \end{remark}
 
 
@@ -3881,7 +3881,7 @@
 \index{spin structure!genus expansion}
 
 The free fermion $\cF$ ($c = 1/2$, $\kappa = 1/4$) is
-the simplest example where spin structures enter the genus
+an example where spin structures enter the genus
 expansion. The Heisenberg genus expansion
 (Chapter~\ref{ch:heisenberg-frame}) involves determinants of
 the $\bar\partial$ operator on the trivial line bundle; the free
@@ -6067,7 +6067,7 @@
 Every chiral algebra on this cover has strict \v{C}ech HCA. On a
 finer cover with triple intersections, the Jacobiator could be
 nonzero and a genuine homotopy $F_3$ would be needed; strictness
-would then depend on the algebra. The correct slogan is:
+would then depend on the algebra. Equivalently,
 \emph{non-strictness is a bar-side phenomenon on $\mathbb{P}^1$,
 arising from FM compactification, not from \v{C}ech descent}.
 \end{remark}
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 4986edf083007b283e4a25a8f531b0d52a989afb..35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -657,6 +657,7 @@
 F_g(\mathrm{Vir}_c) + F_g(\mathrm{Vir}_{26-c}) = 13 \cdot \lambda_g^{\mathrm{FP}}
 \]
 is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
+is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This reflects the Koszul-dual form of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The factor $1/2$ comes from $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ accounts for half of the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$; the affine complementarity is \emph{exact}, with no residual anomaly.
 \end{remark}
 
 \begin{remark}[Verlinde bundle and the limits of the scalar genus tower]%
@@ -1901,7 +1902,7 @@
 \index{A-hat genus@$\hat{A}$-genus}
 The generating function $(x/2)/\sin(x/2)$ is the Wick rotation of the
 $\hat{A}$-genus: $\hat{A}(x) = (x/2)/\sinh(x/2)$, related by the
-substitution $x \mapsto ix$. This is not a coincidence: the family
+substitution $x \mapsto ix$. This reflects the family
 index theorem (Theorem~\ref{thm:family-index}) shows that
 the genus expansion is the Gro\-then\-dieck--Rie\-mann--Roch pushforward of
 the Todd class of the universal curve, and $(x/2)/\sin(x/2)$ is the
diff --git a/chapters/examples/lattice_foundations.tex b/chapters/examples/lattice_foundations.tex
index a6117193c8eae9845a5ce9ec5a5026897caab4c3..a0b774570ac7b4a5cf1b87be47e90b8f4bc767c5
--- a/chapters/examples/lattice_foundations.tex
+++ b/chapters/examples/lattice_foundations.tex
@@ -3503,23 +3503,22 @@
 \begin{enumerate}[label=\textup{(\alph*)}]
 \item \emph{Lattice cocycle deformation}
  (this section): start with an $\Einf$-chiral lattice VOA and
- deform the cocycle to break symmetry. This is a ``top-down''
- method: the state space is fixed, and the OPE acquires phases.
+ deform the cocycle to break symmetry. The state space is fixed,
+ and the OPE acquires phases.
  The deformation is controlled by a finite parameter ($N$, $q$).
 \item \emph{RTT/R-matrix presentation}
  (Chapter~\ref{chap:yangians}): start with the RTT relations and
  build the $\Eone$-chiral algebra from generators and relations.
- This is a ``bottom-up'' method: the algebra is presented by
- generators with an $R$-matrix-valued OPE.
+ The algebra is presented by generators with an
+ $R$-matrix-valued OPE.
 \end{enumerate}
 The two methods are unified by the $\Eone$ inversion principle
 (Theorem~\ref{thm:e1-inversion-principle}): in both cases, Koszul
 duality inverts the non-commutativity datum.
 
 The bridge between the two constructions is the Frenkel--Kac--Segal
-theorem: method~(a) produces $\Eone$-chiral algebras from lattices
-(the ``abelian'' source), while method~(b) produces them from
-quantum groups (the ``non-abelian'' source). At level~1 with
+theorem: method~(a) produces $\Eone$-chiral algebras from lattice
+VOAs, while method~(b) produces them from quantum groups. At level~1 with
 symmetric cocycle, FKS identifies the two; the deformed FKS
 construction (Remark~\ref{rem:lattice:deformed-fks}) extends this
 identification to the $\Eone$ world, connecting lattice cocycle
diff --git a/chapters/examples/minimal_model_examples.tex b/chapters/examples/minimal_model_examples.tex
index 87b38b0bec695cb70fa492f686dcd54c789303bc..700e3ebde84cb3507a1e941fa75f557ed10edede
--- a/chapters/examples/minimal_model_examples.tex
+++ b/chapters/examples/minimal_model_examples.tex
@@ -627,13 +627,11 @@
 (the generating function is algebraic of degree~$2$, hence
 Gevrey-$0$ with no Stokes phenomenon).
 
-This is the chiral-algebraic analogue of a well-known phenomenon
-in quantum field theory: the perturbation series of a
-non-perturbatively well-defined theory can diverge, with the
-divergence encoding non-perturbative information through its
-Borel transform. Here $\rho \gg 1$ signals that the Ising model
-is ``strongly coupled'' in the shadow obstruction tower sense, even though it
-is free (in the sense of admitting a free-fermion realization).
+This matches a standard phenomenon in quantum field theory: the
+perturbation series of a non-perturbatively well-defined theory can
+diverge, with the Borel transform encoding additional information.
+Here $\rho \gg 1$ means that the Ising model has rapid shadow-tower
+growth even though it admits a free-fermion realization.
 \end{remark}
 
 \begin{proposition}[Koszul dual complementarity; \ClaimStatusProvedHere]%
@@ -722,7 +720,6 @@
 $\rho \approx 8.94$; for the three-state Potts model at $c = 4/5$,
 $\rho \approx 7.81$. In each case the Koszul dual at $c' = 26 - c$
 has $\rho' < 1$ (convergent). The minimal models thus illustrate
-the shadow complementarity principle at its sharpest: the simplest,
-most exactly solvable CFTs are the most ``strongly coupled'' in the
-shadow obstruction tower sense.
+the shadow complementarity principle sharply: on the unitary minimal
+line, smaller central charge corresponds to larger shadow growth.
 \end{remark}
diff --git a/chapters/examples/n2_superconformal.tex b/chapters/examples/n2_superconformal.tex
index 0e31ea2ac4fba08ce24e17b8783b4310ebad2781..332de43747c8a919f9253f9d6cb31b629c957558
--- a/chapters/examples/n2_superconformal.tex
+++ b/chapters/examples/n2_superconformal.tex
@@ -315,7 +315,7 @@
 \begin{remark}[The CE/chiral bar gap]
 \label{rem:n2-ce-chiral-gap}
 \index{N=2 superconformal algebra!CE vs chiral bar}
-The $\mathcal{N}=2$ SCA provides the cleanest demonstration
+The $\mathcal{N}=2$ SCA provides a direct demonstration
 in the standard landscape that CE Koszulness (vanishing of
 $H^2_{\mathrm{CE}}(\mathfrak{g}_-)$) and chiral Koszulness
 (vanishing of $H^2(\barB(A))$) are genuinely distinct properties.
diff --git a/chapters/examples/w3_holographic_datum.tex b/chapters/examples/w3_holographic_datum.tex
index e15015e477bff412439d92ec0634d820d943ca58..d93dfa6e0a3228fbbb906e6dd7a77a1574540f3f
--- a/chapters/examples/w3_holographic_datum.tex
+++ b/chapters/examples/w3_holographic_datum.tex
@@ -36,8 +36,8 @@
 $c$-dependent coefficient $\alpha(c) = 16/(22+5c)$;
 (iii)~Koszul duality is the nontrivial involution $c \mapsto 100 - c$,
 producing a complementarity sum that takes the manifestly nonzero
-constant value $250/3$ ( guards against
-the temptation to set this to zero by analogy with the affine
+constant value $250/3$ (this rules out
+the affine-style conclusion that the sum should vanish
 case);
 (iv)~the genus-2 cross-channel correction
 $\delta F_2(\Walg_3) = (c+204)/(16c)$ is the smallest manuscript
diff --git a/chapters/examples/w_algebras_deep.tex b/chapters/examples/w_algebras_deep.tex
index 24b08fd91f6d094ca7f9b90b0008130cd4c6455d..3a30edabee7528e1be8a891c8a4fd254be0753c6
--- a/chapters/examples/w_algebras_deep.tex
+++ b/chapters/examples/w_algebras_deep.tex
@@ -231,7 +231,7 @@
 non-principal theorematic seeds; the global non-principal transport
 statement remains Conjecture~\ref{conj:w-orbit-duality}. The purpose of
 the section is to isolate the mechanism that a future theorem must
-globalize, not to blur that boundary into a single slogan. Concretely,
+globalize without obscuring that status boundary. Concretely,
 the remaining non-principal work is threefold: determine the dual-orbit
 input, determine the orbit-indexed level shift, and globalize the
 paired DS seed transport beyond the present hook/subregular theorematic
@@ -263,7 +263,7 @@
 operator) gives the \emph{Bershadsky--Polyakov algebra}
 $\mathcal{W}^k(\mathfrak{sl}_3, f_{\min})$.
 The minimal orbit is self-transpose, so the orbit-identification
-problem is cleanest in this case. The current manuscript proves the
+problem reduces most directly in this case. The current manuscript proves the
 explicit bar/OPE package and strictness for the BP algebra, but keeps
 the level-shifted duality statement itself conjectural
 (Conjecture~\ref{conj:bp-duality}).
@@ -1093,13 +1093,12 @@
 compatibility: the KM curvature $(k+3)\kappa/6$ projects under DS
 to $c/2$ (Step~4 of the same computation).
 
-The point: the ``residue-side'' OPE coefficients
+The ``residue-side'' OPE coefficients
 $\mathsf{C}^{\mathrm{res}}$ (extracted from the
 $\mathcal{W}_3$ OPE on $\overline{C}_n(X)$) and the
 ``DS-side'' coefficients $\mathsf{C}^{\mathrm{DS}}$ (the DS
 projection of the KM bar complex) are \emph{entries of the same
 chain complex}, identified by the proved intertwining theorem.
-They match by the intertwining theorem.
 
 \subsubsection*{The pattern at rank $4$}
 
diff --git a/chapters/examples/y_algebras.tex b/chapters/examples/y_algebras.tex
index 6c30d4a690add673a9722be30362b2a505bf86de..c941b44517ecbca85e99966e3d00eb119a49accc
--- a/chapters/examples/y_algebras.tex
+++ b/chapters/examples/y_algebras.tex
@@ -365,7 +365,7 @@
 \label{rem:y111-kappa-not-c-over-2}
 \index{kappa@$\kappa$!not c/2@$\neq c/2$}
 Since $c = 0$ but $\kappa = \Psi \neq 0$ generically, the
-$Y_{1,1,1}$ algebra is the simplest example in the standard
+$Y_{1,1,1}$ algebra is an explicit example in the standard
 landscape where $\kappa \neq c/2$. The
 formula $\kappa = c/2$ requires the Virasoro sector to be the
 \emph{sole} contributor to the genus-$1$ bar obstruction
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index b24beea67702424a36b518421a0c6238e301e1d8..b0437410c861242d5f69b8490c67f108d3d0c864
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -2781,7 +2781,7 @@
 shadow~$\kappa(\cA)$ is the trace of this slice, and $r(z)$ is
 the full tensorial content.
 
-This is the single cleanest CG benchmark for the Bridge Theorem
+This is a concrete CG benchmark for the Bridge Theorem
 package: compute $\tau|_{\deg 2}$ explicitly in each benchmark
 family and verify it matches the known $r$-matrix.
 \end{remark}

file update:
diff --git a/chapters/examples/bershadsky_polyakov.tex b/chapters/examples/bershadsky_polyakov.tex
index 2ad638fef7b5e29d8ec1346b6adb2748625ce3f3..05f1c366202f6a50049685ad6a76174e355bb884
--- a/chapters/examples/bershadsky_polyakov.tex
+++ b/chapters/examples/bershadsky_polyakov.tex
@@ -456,7 +456,7 @@
 
 The pattern $\varrho(\mathcal{B}^k) + \varrho(\mathcal{W}_3) =
 1/6 + 5/6 = 1$ reflects the complementary roles of the minimal
-and principal reductions: together they ``use up'' the full
+and principal reductions: together they account for the full
 anomaly of the parent algebra.
 
 \begin{remark}[Relation to the $\mathcal{N}=2$ SCA]
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index 32f68d6b6583630d06ac1ccb670a3436706c04df..f5196ca9d0dd2419f293707e8ccc20268dc43534
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -242,8 +242,8 @@
 
 \begin{warning}[never conflate $p_{\max}$, $k_{\max}$, $r_{\max}$]
 \label{warn:bg-ap59}
-A natural temptation is to write ``$\beta\gamma$ has shadow depth
-$1$'' because the generator OPE has a simple pole. This is wrong on
+The statement ``$\beta\gamma$ has shadow depth
+$1$'' is wrong on
 three counts. \textup{(}a\textup{)}~The shadow depth $r_{\max}$ is
 not the OPE pole order. \textup{(}b\textup{)}~By $d\log$ absorption
 the collision residue has pole order $p_{\max} - 1 = 0$, not~$1$.
@@ -1861,25 +1861,25 @@
 \end{enumerate}
 \end{conjecture}
 
-\begin{remark}[The $\beta\gamma$ system as the cleanest modular test]
+\begin{remark}[The $\beta\gamma$ system as a minimal modular test case]
 \label{rem:betagamma-cleanest-test}
-The $\beta\gamma$ system is optimal for testing the modular envelope because:
+The $\beta\gamma$ system is a minimal test case for the modular envelope because:
 (1)~the OPE is free (single simple pole, no higher singularities);
 (2)~all higher $A_\infty$ operations vanish ($m_k = 0$ for $k \ge 3$);
 (3)~genus dependence enters entirely through determinant-line geometry on curves.
-These three properties make $\beta\gamma$ the hydrogen atom of modular holography.
+These three properties isolate the global modular contribution from local higher-operation corrections.
 \end{remark}
 
 
 %% ================================================================
-\begin{remark}[The $\beta\gamma$ system as holographic atom]
+\begin{remark}[A minimal holographic test case]
 \label{rem:betagamma-holographic-atom}
-\index{beta-gamma system@$\beta\gamma$ system!holographic atom}
-\index{holomorphic-topological!beta-gamma atom@$\beta\gamma$ atom}
+\index{beta-gamma system@$\beta\gamma$ system!minimal holographic test case}
+\index{holomorphic-topological!beta-gamma test case@$\beta\gamma$ test case}
 Local triviality ($m_k = 0$ for $k \ge 3$) forces all modular content
 into the global geometry of curves, so factorization homology alone
-controls the genus expansion. The $\beta\gamma$ system is therefore the
-simplest object in which the boundary algebra, the Koszul-dual defect
+controls the genus expansion. The $\beta\gamma$ system is therefore a
+minimal example in which the boundary algebra, the Koszul-dual defect
 sector, and the derived-center bulk are all explicitly computable.
 \end{remark}
 
@@ -1970,20 +1970,19 @@
 where $\chi_{\mathrm{gr}}$ denotes the graded Euler characteristic.
 \end{definition}
 
-\begin{remark}[The holographic atom principle]
+\begin{remark}[Determinantal genus expansion for $\beta\gamma$]
 \label{rem:betagamma-holographic-atom-principle}
-\index{holographic atom!principle}
-The $\beta\gamma$ system earns the name ``holographic atom'' for
-precisely this reason: local algebraic triviality ($m_k = 0$ for
+\index{beta-gamma system@$\beta\gamma$ system!determinantal genus expansion}
+Local algebraic triviality ($m_k = 0$ for
 $k \geq 3$) strips away all combinatorial complexity of curved
 $A_\infty$ corrections, leaving the genus expansion
-$Z_{\beta\gamma}(\hbar)$ as a pure probe of the global geometry of
+$Z_{\beta\gamma}(\hbar)$ governed by the global geometry of
 moduli. Every term $\chi_{\mathrm{gr}}(H_g^{\beta\gamma})$ is, by
 Conjecture~\ref{conj:betagamma-determinant-control}, a determinant-line
 invariant on $\mathcal{M}_g$, so the generating function
 \eqref{eq:betagamma-partition-function} records how
 factorization homology interacts with stable-curve compactification,
-uncontaminated by local nonlinearity. Any failure of the modular
+with no local nonlinear correction terms. Any failure of the modular
 package at the $\beta\gamma$ level is therefore a failure of the
 global gluing axioms, not of local algebra.
 
diff --git a/chapters/examples/deformation_quantization.tex b/chapters/examples/deformation_quantization.tex
index d3c313626eef51ed5297969981f9dec7e46681e4..627a77efbd20dc3a33e2196a96706b82d81646ae
--- a/chapters/examples/deformation_quantization.tex
+++ b/chapters/examples/deformation_quantization.tex
@@ -82,7 +82,7 @@
 
 \subsection{Role of the upper half-plane}
 
-The upper half-plane $\mathbb{H}$ is the simplest example of a worldsheet: its boundary $\mathbb{R} \subset \partial\mathbb{H}$ represents the ``past,'' quantum fluctuations occur in its interior, points escaping to infinity represent physical states, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
+The upper half-plane $\mathbb{H}$ is the basic bordered surface in Kontsevich's construction: boundary insertions lie on $\mathbb{R} \subset \partial\mathbb{H}$, internal vertices lie in $\mathbb{H}$, and $\text{PSL}(2,\mathbb{R})$ acts by M\"obius transformations.
 
 The key geometric fact: the Kontsevich configuration spaces $C_{n,m}(\mathbb{H})$ (of $n$ interior and $m$ boundary points, modulo $\operatorname{Aff}(\mathbb{R})$) have FM-type compactifications $\overline{C}_{n,m}(\mathbb{H})$ whose boundary strata are governed by the operad structure of the Stasheff associahedra $K_\bullet$ and the little 2-disks operad $E_2$. In particular, the boundary stratification encodes the same combinatorics as the real moduli spaces $\overline{\mathcal{M}}_{0,m}(\mathbb{R})$.
 
diff --git a/chapters/examples/deformation_quantization_examples.tex b/chapters/examples/deformation_quantization_examples.tex
index a4f5ccf2fe43661b3a1a49736abf5677b42bbb9f..7964bf6c71c487f016699ff42102478ce3800126
--- a/chapters/examples/deformation_quantization_examples.tex
+++ b/chapters/examples/deformation_quantization_examples.tex
@@ -199,7 +199,7 @@
 \begin{example}[Obstruction: anomalous theories]\label{ex:anomaly}
 Certain physical theories have obstructions:
 \begin{enumerate}[label=(\roman*)]
-\item Chiral WZW model with ``wrong'' level has $\mathrm{Obs} \neq 0$.
+\item Chiral WZW model at nonintegral level has $\mathrm{Obs} \neq 0$.
 \item The obstruction is the \emph{level quantization condition}: the
  Wess--Zumino class $[H] \in H^3(G, \mathbb{Z})$ requires $k \in \mathbb{Z}$
  for the path integral to be well-defined (arising from $\pi_3(G) \cong \mathbb{Z}$).
@@ -703,8 +703,8 @@
 collapses at $E_1$ (acyclicity); for $d = 3$ at $E_2$ (the classical
 derived category); and for $d \geq 4$ the pages $E_3, \ldots, E_{d-1}$
 carry genuinely $A_\infty$ information invisible to classical algebraic
-geometry. This hierarchy gives a concrete filtration-theoretic meaning
-to the slogan ``the degree of $W$ controls the homotopy depth of $\dCrit(W)$.''
+geometry. This hierarchy makes precise the statement that the degree
+of $W$ controls the homotopy depth of $\dCrit(W)$.
 \end{remark}
 
 \begin{remark}[Three-pillar interpretation: deformation quantization]
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index a4d4d1d9f2650b81b850aad00e336484a4b101c6..daf9be2b2efbe2f0b0c98381dc849c46bb35bc2d
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -2421,7 +2421,7 @@
 \begin{remark}[Ext algebra and the genus universality invariant]
 \label{rem:ext-genus-universality}
 \index{genus universality!Ext algebra}
-The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. This is the ``horizontal'' (module Ext) manifestation of the ``vertical'' (genus) invariant~$\kappa(\mathcal{H}_k)$.
+The Euler characteristic $\chi(\mathrm{Ext}^*) = \prod(1 - q^n)^d = q^{-d/24}\,\eta(\tau)^d$ satisfies $\chi(\mathrm{Ext}^*) \cdot Z(\mathcal{H}_k) = 1$, where $Z = q^{d/24}/\eta(\tau)^d$ is the Heisenberg partition function. The conformal anomaly $q^{d/24}$ reflects $c = d$; the genus universality invariant $\kappa(\mathcal{H}_k) = k$ (Theorem~\ref{thm:genus-universality}) governs the genus-$g$ obstruction $\mathrm{obs}_g = k \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}), with genus-$1$ value $F_1 = k/24 = c/24$. Thus the same invariant $\kappa(\mathcal{H}_k)$ controls both the module Ext Euler characteristic and the genus expansion.
 \end{remark}
 
 
@@ -3881,7 +3881,7 @@
 \index{spin structure!genus expansion}
 
 The free fermion $\cF$ ($c = 1/2$, $\kappa = 1/4$) is
-the simplest example where spin structures enter the genus
+an example where spin structures enter the genus
 expansion. The Heisenberg genus expansion
 (Chapter~\ref{ch:heisenberg-frame}) involves determinants of
 the $\bar\partial$ operator on the trivial line bundle; the free
@@ -6067,7 +6067,7 @@
 Every chiral algebra on this cover has strict \v{C}ech HCA. On a
 finer cover with triple intersections, the Jacobiator could be
 nonzero and a genuine homotopy $F_3$ would be needed; strictness
-would then depend on the algebra. The correct slogan is:
+would then depend on the algebra. Equivalently,
 \emph{non-strictness is a bar-side phenomenon on $\mathbb{P}^1$,
 arising from FM compactification, not from \v{C}ech descent}.
 \end{remark}
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index 4986edf083007b283e4a25a8f531b0d52a989afb..35f8f7d8a7a8a58c5dd29ef53a3400b99aebb26d
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -657,6 +657,7 @@
 F_g(\mathrm{Vir}_c) + F_g(\mathrm{Vir}_{26-c}) = 13 \cdot \lambda_g^{\mathrm{FP}}
 \]
 is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This is not a coincidence: it is the Koszul-dual manifestation of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The ``half-string'' factor arises because $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ saturates half the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$ the affine complementarity is \emph{exact}, with no residual anomaly.
+is the bosonic string free energy of $26/2 = 13$ free bosons (each contributing $\kappa = 1$). This reflects the Koszul-dual form of Polyakov's anomaly cancellation $c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 26 - 26 = 0$. The factor $1/2$ comes from $\kappa = c/2$ for the Virasoro algebra (the anomaly ratio $\varrho = 1/2$), so the combined $\kappa_{\mathrm{Vir}} + \kappa_{\mathrm{Vir}}' = c/2 + (26-c)/2$ accounts for half of the bosonic string anomaly. By contrast, for the affine Kac--Moody algebra $\widehat{\mathfrak{sl}}_{2,k}$ the Feigin--Frenkel dual is at level $k' = -k-4$, giving $\kappa_{\mathrm{KM}}(k) + \kappa_{\mathrm{KM}}(k') = 3(k{+}2)/4 + 3(-k{-}2)/4 = 0$; the affine complementarity is \emph{exact}, with no residual anomaly.
 \end{remark}
 
 \begin{remark}[Verlinde bundle and the limits of the scalar genus tower]%
@@ -1901,7 +1902,7 @@
 \index{A-hat genus@$\hat{A}$-genus}
 The generating function $(x/2)/\sin(x/2)$ is the Wick rotation of the
 $\hat{A}$-genus: $\hat{A}(x) = (x/2)/\sinh(x/2)$, related by the
-substitution $x \mapsto ix$. This is not a coincidence: the family
+substitution $x \mapsto ix$. This reflects the family
 index theorem (Theorem~\ref{thm:family-index}) shows that
 the genus expansion is the Gro\-then\-dieck--Rie\-mann--Roch pushforward of
 the Todd class of the universal curve, and $(x/2)/\sin(x/2)$ is the
diff --git a/chapters/examples/lattice_foundations.tex b/chapters/examples/lattice_foundations.tex
index a6117193c8eae9845a5ce9ec5a5026897caab4c3..a0b774570ac7b4a5cf1b87be47e90b8f4bc767c5
--- a/chapters/examples/lattice_foundations.tex
+++ b/chapters/examples/lattice_foundations.tex
@@ -3503,23 +3503,22 @@
 \begin{enumerate}[label=\textup{(\alph*)}]
 \item \emph{Lattice cocycle deformation}
  (this section): start with an $\Einf$-chiral lattice VOA and
- deform the cocycle to break symmetry. This is a ``top-down''
- method: the state space is fixed, and the OPE acquires phases.
+ deform the cocycle to break symmetry. The state space is fixed,
+ and the OPE acquires phases.
  The deformation is controlled by a finite parameter ($N$, $q$).
 \item \emph{RTT/R-matrix presentation}
  (Chapter~\ref{chap:yangians}): start with the RTT relations and
  build the $\Eone$-chiral algebra from generators and relations.
- This is a ``bottom-up'' method: the algebra is presented by
- generators with an $R$-matrix-valued OPE.
+ The algebra is presented by generators with an
+ $R$-matrix-valued OPE.
 \end{enumerate}
 The two methods are unified by the $\Eone$ inversion principle
 (Theorem~\ref{thm:e1-inversion-principle}): in both cases, Koszul
 duality inverts the non-commutativity datum.
 
 The bridge between the two constructions is the Frenkel--Kac--Segal
-theorem: method~(a) produces $\Eone$-chiral algebras from lattices
-(the ``abelian'' source), while method~(b) produces them from
-quantum groups (the ``non-abelian'' source). At level~1 with
+theorem: method~(a) produces $\Eone$-chiral algebras from lattice
+VOAs, while method~(b) produces them from quantum groups. At level~1 with
 symmetric cocycle, FKS identifies the two; the deformed FKS
 construction (Remark~\ref{rem:lattice:deformed-fks}) extends this
 identification to the $\Eone$ world, connecting lattice cocycle
diff --git a/chapters/examples/minimal_model_examples.tex b/chapters/examples/minimal_model_examples.tex
index 87b38b0bec695cb70fa492f686dcd54c789303bc..700e3ebde84cb3507a1e941fa75f557ed10edede
--- a/chapters/examples/minimal_model_examples.tex
+++ b/chapters/examples/minimal_model_examples.tex
@@ -627,13 +627,11 @@
 (the generating function is algebraic of degree~$2$, hence
 Gevrey-$0$ with no Stokes phenomenon).
 
-This is the chiral-algebraic analogue of a well-known phenomenon
-in quantum field theory: the perturbation series of a
-non-perturbatively well-defined theory can diverge, with the
-divergence encoding non-perturbative information through its
-Borel transform. Here $\rho \gg 1$ signals that the Ising model
-is ``strongly coupled'' in the shadow obstruction tower sense, even though it
-is free (in the sense of admitting a free-fermion realization).
+This matches a standard phenomenon in quantum field theory: the
+perturbation series of a non-perturbatively well-defined theory can
+diverge, with the Borel transform encoding additional information.
+Here $\rho \gg 1$ means that the Ising model has rapid shadow-tower
+growth even though it admits a free-fermion realization.
 \end{remark}
 
 \begin{proposition}[Koszul dual complementarity; \ClaimStatusProvedHere]%
@@ -722,7 +720,6 @@
 $\rho \approx 8.94$; for the three-state Potts model at $c = 4/5$,
 $\rho \approx 7.81$. In each case the Koszul dual at $c' = 26 - c$
 has $\rho' < 1$ (convergent). The minimal models thus illustrate
-the shadow complementarity principle at its sharpest: the simplest,
-most exactly solvable CFTs are the most ``strongly coupled'' in the
-shadow obstruction tower sense.
+the shadow complementarity principle sharply: on the unitary minimal
+line, smaller central charge corresponds to larger shadow growth.
 \end{remark}
diff --git a/chapters/examples/n2_superconformal.tex b/chapters/examples/n2_superconformal.tex
index 0e31ea2ac4fba08ce24e17b8783b4310ebad2781..332de43747c8a919f9253f9d6cb31b629c957558
--- a/chapters/examples/n2_superconformal.tex
+++ b/chapters/examples/n2_superconformal.tex
@@ -315,7 +315,7 @@
 \begin{remark}[The CE/chiral bar gap]
 \label{rem:n2-ce-chiral-gap}
 \index{N=2 superconformal algebra!CE vs chiral bar}
-The $\mathcal{N}=2$ SCA provides the cleanest demonstration
+The $\mathcal{N}=2$ SCA provides a direct demonstration
 in the standard landscape that CE Koszulness (vanishing of
 $H^2_{\mathrm{CE}}(\mathfrak{g}_-)$) and chiral Koszulness
 (vanishing of $H^2(\barB(A))$) are genuinely distinct properties.
diff --git a/chapters/examples/w3_holographic_datum.tex b/chapters/examples/w3_holographic_datum.tex
index e15015e477bff412439d92ec0634d820d943ca58..d93dfa6e0a3228fbbb906e6dd7a77a1574540f3f
--- a/chapters/examples/w3_holographic_datum.tex
+++ b/chapters/examples/w3_holographic_datum.tex
@@ -36,8 +36,8 @@
 $c$-dependent coefficient $\alpha(c) = 16/(22+5c)$;
 (iii)~Koszul duality is the nontrivial involution $c \mapsto 100 - c$,
 producing a complementarity sum that takes the manifestly nonzero
-constant value $250/3$ ( guards against
-the temptation to set this to zero by analogy with the affine
+constant value $250/3$ (this rules out
+the affine-style conclusion that the sum should vanish
 case);
 (iv)~the genus-2 cross-channel correction
 $\delta F_2(\Walg_3) = (c+204)/(16c)$ is the smallest manuscript
diff --git a/chapters/examples/w_algebras_deep.tex b/chapters/examples/w_algebras_deep.tex
index 24b08fd91f6d094ca7f9b90b0008130cd4c6455d..3a30edabee7528e1be8a891c8a4fd254be0753c6
--- a/chapters/examples/w_algebras_deep.tex
+++ b/chapters/examples/w_algebras_deep.tex
@@ -231,7 +231,7 @@
 non-principal theorematic seeds; the global non-principal transport
 statement remains Conjecture~\ref{conj:w-orbit-duality}. The purpose of
 the section is to isolate the mechanism that a future theorem must
-globalize, not to blur that boundary into a single slogan. Concretely,
+globalize without obscuring that status boundary. Concretely,
 the remaining non-principal work is threefold: determine the dual-orbit
 input, determine the orbit-indexed level shift, and globalize the
 paired DS seed transport beyond the present hook/subregular theorematic
@@ -263,7 +263,7 @@
 operator) gives the \emph{Bershadsky--Polyakov algebra}
 $\mathcal{W}^k(\mathfrak{sl}_3, f_{\min})$.
 The minimal orbit is self-transpose, so the orbit-identification
-problem is cleanest in this case. The current manuscript proves the
+problem reduces most directly in this case. The current manuscript proves the
 explicit bar/OPE package and strictness for the BP algebra, but keeps
 the level-shifted duality statement itself conjectural
 (Conjecture~\ref{conj:bp-duality}).
@@ -1093,13 +1093,12 @@
 compatibility: the KM curvature $(k+3)\kappa/6$ projects under DS
 to $c/2$ (Step~4 of the same computation).
 
-The point: the ``residue-side'' OPE coefficients
+The ``residue-side'' OPE coefficients
 $\mathsf{C}^{\mathrm{res}}$ (extracted from the
 $\mathcal{W}_3$ OPE on $\overline{C}_n(X)$) and the
 ``DS-side'' coefficients $\mathsf{C}^{\mathrm{DS}}$ (the DS
 projection of the KM bar complex) are \emph{entries of the same
 chain complex}, identified by the proved intertwining theorem.
-They match by the intertwining theorem.
 
 \subsubsection*{The pattern at rank $4$}
 
diff --git a/chapters/examples/y_algebras.tex b/chapters/examples/y_algebras.tex
index 6c30d4a690add673a9722be30362b2a505bf86de..c941b44517ecbca85e99966e3d00eb119a49accc
--- a/chapters/examples/y_algebras.tex
+++ b/chapters/examples/y_algebras.tex
@@ -365,7 +365,7 @@
 \label{rem:y111-kappa-not-c-over-2}
 \index{kappa@$\kappa$!not c/2@$\neq c/2$}
 Since $c = 0$ but $\kappa = \Psi \neq 0$ generically, the
-$Y_{1,1,1}$ algebra is the simplest example in the standard
+$Y_{1,1,1}$ algebra is an explicit example in the standard
 landscape where $\kappa \neq c/2$. The
 formula $\kappa = c/2$ requires the Virasoro sector to be the
 \emph{sole} contributor to the genus-$1$ bar obstruction
diff --git a/chapters/examples/yangians_drinfeld_kohno.tex b/chapters/examples/yangians_drinfeld_kohno.tex
index b24beea67702424a36b518421a0c6238e301e1d8..b0437410c861242d5f69b8490c67f108d3d0c864
--- a/chapters/examples/yangians_drinfeld_kohno.tex
+++ b/chapters/examples/yangians_drinfeld_kohno.tex
@@ -2781,7 +2781,7 @@
 shadow~$\kappa(\cA)$ is the trace of this slice, and $r(z)$ is
 the full tensorial content.
 
-This is the single cleanest CG benchmark for the Bridge Theorem
+This is a concrete CG benchmark for the Bridge Theorem
 package: compute $\tau|_{\deg 2}$ explicitly in each benchmark
 family and verify it matches the known $r$-matrix.
 \end{remark}

ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 9:35 PM.
tokens used
163,202
