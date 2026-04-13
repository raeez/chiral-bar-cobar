# G19_hg_modular_PBW_whitehead (201s)

FIXED. No edit was needed: the AP198 repair is already present on disk, and it is correct.

The reduction from the truncated current algebra to `\fg` is explicit in the current file:
- [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:917) proves the weightwise decomposition `\mathcal E_g^{*,h} \cong \bigoplus_\nu C^*_{\mathrm{CE}}(\fg,M_{h,\nu}) \otimes H^1(\Sigma_g,\bC)`, with `\fg \otimes V_h` used only for mode bookkeeping.
- [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:976) proves the mixed map factors through `H^1(\fg,N_h^{n-1})`.
- [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1326) states the scope cleanly: Whitehead is applied only to finite-dimensional `\fg`-modules, never to the non-semisimple Lie algebra `\fg \otimes V_h`.

I also checked the downstream PBW proofs at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1138) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1455); both use the repaired reduction correctly. This is the P08 repair, and it survives verification against the current source and the P08 rectification note. A hostile grep found no remaining AP198-style claim in this chapter applying Whitehead directly to `\fg \otimes V_h`.


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
session id: 019d88a1-3982-75b0-be27-fd0e78dd7693
--------
user
<task>
You are a FINAL GAPS agent. This is the LAST PASS. Every remaining gap must be closed.
832 agents have already run. You fix what they couldn't finish.
Read files on disk — they reflect ALL prior work. Be surgical. Be complete.
</task>
<action_safety>Keep changes scoped. After edits, re-read and verify. Grep for AP violations.</action_safety>
<completeness_contract>Fix EVERY issue in your scope. Report: FIXED or BLOCKED (with reason).</completeness_contract>
<verification_loop>After all edits, verify no new violations introduced.</verification_loop>


Verify MC1 PBW Whitehead reduction in higher_genus_modular_koszul.tex (AP198).

NARROW SCOPE. Search for 'Whitehead' near lines 1011-1030 and 1290-1300.
Verify: the reduction from truncated current algebra to g is explicit.
If the platonic agent P08 wrote it, verify it's correct.
If not written yet: add a remark explaining the reduction.
mcp startup: no servers
codex
Using `multi-path-verify` for this pass because the task is a narrow claim verification with a possible local repair. I’m reading the required repo-wide context files first, then the exact `Whitehead` surface in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/higher_genus_modular_koszul.tex).
collab spawn_agent(call_AkgMfCizb4mgO9qyiGHr3Xiq, prompt="Inspect the narrow AP198 surface in /Users/raeez/chiral-bar-cobar/higher_genus_modular_koszul.tex around Whitehead near …")
mcp startup: no servers
spawn_agent(call_AkgMfCizb4mgO9qyiGHr3Xiq, prompt="Inspect the narrow AP198 surface in /Users/raeez/chiral-bar-cobar/higher_genus_modular_koszul.tex around Whitehead near …") pending init:
  agent: 019d88a1-72d8-7191-845e-280d6781c1fa
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1000,1050p' higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:
sed: higher_genus_modular_koszul.tex: No such file or directory
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N3_e1_primacy.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
audit_campaign_20260413_163450
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg --files | grep higher_genus_modular_koszul' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/C08_higher_genus_modular_koszul.md
wave2_audit_20260413_001942/G07_higher_genus_modular_koszul.md
rectification_20260412_233715/R04_higher_genus_modular_koszul.md
relaunch_20260413_111534/R04_higher_genus_modular_koszul.md
resume_20260413_192632/R04_higher_genus_modular_koszul.md
resume_20260413_165929/R04_higher_genus_modular_koszul.md
chapters/theory/higher_genus_modular_koszul.tex
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1000,1050p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the non-semisimple truncated current algebra $\fg \otimes V_h$.
\end{lemma}

\begin{proof}
Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
enrichment class as a sum of tensors
$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
pattern. For each such tensor, isolate the $\fg$-label attached to the
slot carrying the regular form and collect the remaining bar data into
the coefficient module~$N_h^{n-1}$. This gives the map
$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.

The mixed residue brackets the distinguished $\fg$-label with one of
the remaining labels and then forgets the regular genus form. The
Jacobi identity for the residue bracket is exactly the cocycle
condition on $\iota_{g,h,n}(\xi)$ when
$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
depends only on the image of $\iota_{g,h,n}(\xi)$ in
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1260,1310p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $[\,,\,]\colon \Lambda^2(\mathfrak{sl}_2)
 \to \mathfrak{sl}_2$ is an isomorphism,
 so $d_1$ annihilates the target completely.
\item $V_5 = \mathrm{Sym}^2_0(\mathfrak{sl}_2)$
 (traceless symmetric tensors):
 Whitehead's theorem gives
 $H^q(\mathfrak{sl}_2, V_5) = 0$ for all~$q$, so $V_5$
 cannot contribute to $E_\infty$.
\item $V_1$: the invariant line, spanned by the
 Killing-form element
 $\kappa = e \otimes f + f \otimes e
 + \tfrac{1}{2}\,h \otimes h$.
 This element lies in $\ker(d_1)$ (symmetric tensors
 vanish under the antisymmetric bracket), but is killed
 at $E_3$ by $d_2^{\mathrm{PBW}}$: the $(1)$-product
 contraction maps $\kappa$ to the scalar
 $\kappa^{ab}\kappa_{ab} = 1 + 1 + \tfrac{1}{2} \cdot 2
 = 3 = \dim(\mathfrak{sl}_2)$,
 which is nonzero at generic level~$k$.
\end{itemize}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Whitehead" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
899:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
905:non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
939:records the mode cutoff only: the Whitehead step is carried out on
978:\index{Whitehead lemma!mixed genus-0/genus-g factorization}
1037:by Whitehead; the Killing-form invariant
1048:enrichment factorization, Whitehead acyclicity, and the
1154:finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
1177:Whitehead's first lemma for semisimple~$\fg$
1184:semisimple extension of Whitehead then gives:
1231:We exhibit the interplay of Whitehead vanishing and
1265: Whitehead's theorem gives
1282:three by the bracket isomorphism, five by Whitehead, one by the
1316:summands killed by Whitehead, invariant summands passed to
1322:decomposition under~$\fg$ and the Whitehead vanishing
1326:\begin{remark}[Whitehead reduction in the PBW proof]
1329:Whitehead input appears after rewriting the weight-$h$ enrichment
1375:Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
1401:three-step mechanism (PBW decomposition, Whitehead
1455:\emph{Step~2: Whitehead acyclicity of the enrichment.}
1477:$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "truncated" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
919:\index{truncated current algebra!mode bookkeeping only}
938:In particular the truncated current algebra $\fg \otimes V_h$
941:fixing a mode pattern~$\nu$, the residue action of the truncated
1000:the non-semisimple truncated current algebra $\fg \otimes V_h$.
1138:By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
1327:For fixed conformal weight~$h$, the truncated current algebra
1448:truncated at weight~$h$, which is genus-independent. Equivalently,
1480:truncated current algebra that records the mode cutoff.
4180:$\mathfrak{Q}$ are its degree-truncated projections
5296: The same completed surrogate computes truncated MC residuals
5302: genus-truncated completed MC solver branch: fixing $a_0=1$ in
5312: (both truncated and recursive):
12324:shadows at degrees~$\leq r$: whether the tower can be truncated at
12340:obstruction tower itself (the sequence of truncated MC elements
12608:element in the degree-truncated modular convolution algebra
12627:of truncated MC elements. Each truncation $\Theta_\cA^{\leq r}$
12774: truncated MC element
13153:Suppose a truncated solution $\Theta_{\cA}^{\leq N}$ has been
13248:$\gAmod / F^{N+1}\gAmod$ gives the truncated MC equation
13346:limit of its weight-truncated quotients. The bar-intrinsic MC
codex
I’ve loaded the mandatory constitutional context and the verification skill. Next I’m checking the exact `Whitehead` surface in the chapter and comparing the proof text against the explicit algebra map that should reduce the truncated current algebra to `\fg`.
exec
/bin/zsh -lc 'rg -n "Whitehead" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '980,1045p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg 'higher_genus_modular_koszul\\.tex"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
899:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
905:non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
939:records the mode cutoff only: the Whitehead step is carried out on
978:\index{Whitehead lemma!mixed genus-0/genus-g factorization}
1037:by Whitehead; the Killing-form invariant
1048:enrichment factorization, Whitehead acyclicity, and the
1154:finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
1177:Whitehead's first lemma for semisimple~$\fg$
1184:semisimple extension of Whitehead then gives:
1231:We exhibit the interplay of Whitehead vanishing and
1265: Whitehead's theorem gives
1282:three by the bracket isomorphism, five by Whitehead, one by the
1316:summands killed by Whitehead, invariant summands passed to
1322:decomposition under~$\fg$ and the Whitehead vanishing
1326:\begin{remark}[Whitehead reduction in the PBW proof]
1329:Whitehead input appears after rewriting the weight-$h$ enrichment
1375:Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
1401:three-step mechanism (PBW decomposition, Whitehead
1455:\emph{Step~2: Whitehead acyclicity of the enrichment.}
1477:$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 succeeded in 50ms:
After choosing a basis of $H^1(\Sigma_g,\bC)$ and using
Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
finite-dimensional $\fg$-module $N_h^{n-1}$ and
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
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex
exec
/bin/zsh -lc "sed -n '1270,1315p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '910,960p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\kappa = e \otimes f + f \otimes e
 + \tfrac{1}{2}\,h \otimes h$.
 This element lies in $\ker(d_1)$ (symmetric tensors
 vanish under the antisymmetric bracket), but is killed
 at $E_3$ by $d_2^{\mathrm{PBW}}$: the $(1)$-product
 contraction maps $\kappa$ to the scalar
 $\kappa^{ab}\kappa_{ab} = 1 + 1 + \tfrac{1}{2} \cdot 2
 = 3 = \dim(\mathfrak{sl}_2)$,
 which is nonzero at generic level~$k$.
\end{itemize}

Thus all nine enrichment classes at $h = 2$ are eliminated:
three by the bracket isomorphism, five by Whitehead, one by the
Killing contraction.
The decomposition $E_\infty^{*,2}(g{=}1) =
E_\infty^{*,2}(g{=}0)$ follows.

A symbolic check of the same mechanism at the next tensor
powers, implemented in
\nolinkurl{compute/lib/genus1_pbw_sl2.py},
 succeeded in 51ms:
Open: non-principal families; the $\mathcal{W}_\infty$
inverse-limit package
(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
\end{remark}

\begin{lemma}[Weightwise reduction of the genus enrichment to
 \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
\label{lem:pbw-weightwise-g-module}
\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
\index{truncated current algebra!mode bookkeeping only}
Fix a genus $g \geq 1$ and a conformal weight $h \geq 1$. Write
\[
V_h := t^{-1}\bC[t^{-1}] / t^{-h-1}\bC[t^{-1}].
\]
Then the weight-$h$ genus-enrichment block of
$\bar{B}^{(g)}(\widehat{\fg}_k)$ admits a finite decomposition
\[
\mathcal{E}_g^{*,h}
\;\cong\;
\bigoplus_\nu

thinking
**Inspecting theorem context**

I realize we need to gather more context around the theorem and remark mentioned at 1322. It might be a good idea to inspect the broader sections that cover both the theorem proof and the remark to get a clearer understanding. By looking at these surrounding details, I can ensure that I'm fully grasping the necessary concepts and how they connect. I'll focus on pulling that information together for clarity.
exec
/bin/zsh -lc "sed -n '1030,1215p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1215,1365p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
For any simple Lie algebra~$\fg$ and generic level
$k \notin \Sigma(\fg)$, the PBW spectral sequence for the
genus-$1$ bar complex
$\bar{B}^{(1)}(\widehat{\fg}_k)$ has concentrated
$E_\infty$ page: the enrichment from $H^1(E_\tau)$
is eliminated by~$d_1$ and~$d_2$
\textup{(}non-trivial $\fg$-modules at~$E_2$
by Whitehead; the Killing-form invariant
at~$E_3$ by the level-$k$ contraction\textup{)}.
In particular, the interacting Kac--Moody algebras satisfy
axiom~\textup{MK3}
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
unconditionally at genus~$1$:
they are modular pre-Koszul at~$g = 1$.
\end{theorem}

\begin{proof}
We carry out the genus-$1$ Kac--Moody argument directly, using
enrichment factorization, Whitehead acyclicity, and the
level-$k$ Killing contraction.
 succeeded in 52ms:
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

\medskip
\emph{Step~4: The mechanism in action ($\fg = \mathfrak{sl}_2$, $h = 2$).}

We exhibit the interplay of Whitehead vanishing and
Killing-form contraction at the first nontrivial conformal
weight.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '996,1015p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
equals $\beta_{g,h,n}\bigl(q(\iota_{g,h,n}(\xi))\bigr)$.
Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
the non-semisimple truncated current algebra $\fg \otimes V_h$.
\end{lemma}

\begin{proof}
Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
enrichment class as a sum of tensors
$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
pattern. For each such tensor, isolate the $\fg$-label attached to the
slot carrying the regular form and collect the remaining bar data into
the coefficient module~$N_h^{n-1}$. This gives the map
$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.

The mixed residue brackets the distinguished $\fg$-label with one of
the remaining labels and then forgets the regular genus form. The
Jacobi identity for the residue bracket is exactly the cocycle
condition on $\iota_{g,h,n}(\xi)$ when
codex
The chapter already contains a local `Whitehead reduction` remark. I’m now checking the two cited lemmas to see whether the reduction is genuinely explicit or whether the remark still hides the key map behind shorthand.
exec
/bin/zsh -lc 'rg -n "lem:pbw-weightwise-g-module|lem:pbw-mixed-factorization" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '900,990p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
917:\label{lem:pbw-weightwise-g-module}
976:\label{lem:pbw-mixed-factorization}
981:Lemma~\ref{lem:pbw-weightwise-g-module}, there is a
1138:By Lemma~\ref{lem:pbw-weightwise-g-module}, the truncated
1152:$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
1172:By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
1331:\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
1334:\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
1452:\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.
1474:Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
 succeeded in 52ms:
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
(Conjecture~\ref{conj:master-infinite-generator}; MC4 structural framework proved, Theorem~\ref{thm:completed-bar-cobar-strong}; H-level identification remaining).
\end{remark}

\begin{lemma}[Weightwise reduction of the genus enrichment to
 \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
\label{lem:pbw-weightwise-g-module}
\index{PBW spectral sequence!weightwise \texorpdfstring{$\fg$}{g}-module reduction|textbf}
\index{truncated current algebra!mode bookkeeping only}
exec
/bin/zsh -lc "sed -n '990,1045p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

\begin{proof}
Choose a basis $\{\alpha_r\}$ of $H^1(\Sigma_g,\bC)$ and write every
enrichment class as a sum of tensors
$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
pattern. For each such tensor, isolate the $\fg$-label attached to the
slot carrying the regular form and collect the remaining bar data into
the coefficient module~$N_h^{n-1}$. This gives the map
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "AP198" -n' in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
scripts/final_gaps_campaign.py:249:agent("G19_hg_modular_PBW_whitehead", """Verify MC1 PBW Whitehead reduction in higher_genus_modular_koszul.tex (AP198).
resume_20260413_163457/S15_appendices_to_body.md:172:CLAUDE.md:1079:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
scripts/mega_rescue_100.py:98:    ("M07_higher_genus_modular", "chapters/theory/higher_genus_modular_koszul.tex", "Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g."),
CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
mega_rescue_20260413_141327/M07_higher_genus_modular.md:54:Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g.
final_gaps_20260413_213946/G05_curved_flat_xvol.md:117:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
final_gaps_20260413_213946/G05_curved_flat_xvol.md:122:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
resume_20260413_192632/F13_hidden_imports_curved.md:166:CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
resume_20260413_192632/M07_higher_genus_modular.md:54:Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g.
final_gaps_20260413_213946/G07_uniform_weight_rest.md:1978:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
resume_20260413_165929/B14_stale_cross_vol_refs_v2.md:407:/Users/raeez/chiral-bar-cobar/CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
resume_20260413_165929/C15_five_objects_fix.md:677:./CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
compute/audit/new_antipatterns_wave12_campaign.md:104:### AP198: Whitehead lemma scope error.
resume_20260413_165929/B11_orphaned_chapters.md:101:CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
resume_20260413_165929/B11_orphaned_chapters.md:102:resume_20260413_163457/S15_appendices_to_body.md:172:CLAUDE.md:1079:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
resume_20260413_165929/M07_higher_genus_modular.md:54:Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g.
elite_rescue_20260413_221642/L07_KS_comparison.md:1809:scripts/final_gaps_campaign.py:249:agent("G19_hg_modular_PBW_whitehead", """Verify MC1 PBW Whitehead reduction in higher_genus_modular_koszul.tex (AP198).
elite_rescue_20260413_221642/L07_KS_comparison.md:1813:scripts/mega_rescue_100.py:98:    ("M07_higher_genus_modular", "chapters/theory/higher_genus_modular_koszul.tex", "Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g."),
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '90,150p' compute/audit/new_antipatterns_wave12_campaign.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
**Rule**: In addition to checking formulas (AP25), audit PROSE around bar/cobar/Koszul/center discussions. Before any sentence mentioning two or more of {bar, cobar, Koszul dual, derived center, bulk}: write the four-object template and verify the sentence correctly distinguishes them.
Evidence: D09 (15C, 26H), XV14_five_objects_xvol (20 findings).

### AP196: SC^{ch,top} misattribution in non-formula contexts.
39 findings from D11_SC_discipline (9C, 23H). The existing AP165 covers B(A)-is-not-SC, but the campaign found subtler misattributions: SC structure described without specifying it lives on the PAIR (C^bullet_ch(A,A), A); topologization described without conformal vector hypothesis; SC^! described without the (Lie, Ass) structure.
**Rule**: Every sentence mentioning SC^{ch,top} must specify: (a) which object it's attributed to (the derived center PAIR, not B(A)), (b) whether topologization is claimed (requires conformal vector), (c) that SC^! = (Lie, Ass, shuffle-mixed), not self-dual.
Evidence: D11 (9C, 23H), AP17 (17 findings), AP18 (6 findings), AP19 (16 findings).

### AP197: Three Hochschild theories conflated in bare "Hochschild" usage.
89 findings from D12_hochschild_disambiguation (1C, 53H, 35M). The existing AP160 defines the three theories but the campaign found 89 instances of bare "Hochschild" without chiral/topological/categorical qualifier.
**Rule**: In mathematical contexts, NEVER write bare "Hochschild" without qualifier. The three theories give different answers: (i) topological HH: E_1→E_2, (ii) chiral ChirHoch: E_inf-chiral→{0,1,2}, (iii) categorical HH: dg cat→E_2+CY. The geometry determines which. Add qualifier at every occurrence.
**Grep**: `grep -rn 'Hochschild' FILE | grep -v 'chiral\|topological\|categorical\|ChirHoch'`
Evidence: D12 (1C, 53H, 35M).

### AP198: Whitehead lemma scope error.
From T08_MC1_PBW (5C). Whitehead's lemma for Lie algebra cohomology applies to finite-dimensional SEMISIMPLE Lie algebras g, not to truncated current algebras, loop algebras, or their modules without additional justification.
**Rule**: Before invoking Whitehead's lemma: verify the Lie algebra in question is (a) finite-dimensional, (b) semisimple. If the argument involves a current algebra g[[t]] or g[t]/t^N: the reduction to g must be made explicit (typically via a weight-graded decomposition where g acts on each graded piece).
Evidence: T08 (lines ~1011, 1027, 1294, 1776 of higher_genus_modular_koszul.tex).

### AP199: Strong filtration inequality direction.
exec
/bin/zsh -lc 'rg -n "AP198|Whitehead reduction" -S .' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 79

./resume_20260413_163457/S15_appendices_to_body.md:172:CLAUDE.md:1079:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
./tmp_standalone_audit/survey_v2_xr.tex:3287:\noindent\textbf{Step~1: Whitehead reduction.}\enspace
./CLAUDE.md:540:| MC1-4 | PROVED | PBW (Whitehead reduction for current algebras explicit), MC element (g^mod carrier; E1 version in e1_modular_koszul.tex), thick gen (MC3 conditional on Baxter constraint b=a-1/2 for type A; genuine mathematical restriction), completion tower (filtration by pole order corrected; resonance lane conditional on transfer comparison). MC2 ALT: KS scattering diagram (H06). |
./CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
./relaunch_20260413_111534/F10_prerequisites_MC1_5.md:679:Whitehead reduction to a finite-dimensional linear system
./mega_rescue_20260413_141327/M07_higher_genus_modular.md:54:Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g.
./relaunch_20260413_111534/R04_higher_genus_modular_koszul.md:14758:1323:\begin{remark}[Whitehead reduction in the PBW proof]
./elite_rescue_20260413_221642/L07_KS_comparison.md:391:./CLAUDE.md:540:| MC1-4 | PROVED | PBW (Whitehead reduction for current algebras explicit), MC element (g^mod carrier; E1 version in e1_modular_koszul.tex), thick gen (MC3 conditional on Baxter constraint b=a-1/2 for type A; genuine mathematical restriction), completion tower (filtration by pole order corrected; resonance lane conditional on transfer comparison). MC2 ALT: KS scattering diagram (H06). |
./elite_rescue_20260413_221642/L07_KS_comparison.md:1809:scripts/final_gaps_campaign.py:249:agent("G19_hg_modular_PBW_whitehead", """Verify MC1 PBW Whitehead reduction in higher_genus_modular_koszul.tex (AP198).
./elite_rescue_20260413_221642/L07_KS_comparison.md:1813:scripts/mega_rescue_100.py:98:    ("M07_higher_genus_modular", "chapters/theory/higher_genus_modular_koszul.tex", "Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g."),
./scripts/final_gaps_campaign.py:249:agent("G19_hg_modular_PBW_whitehead", """Verify MC1 PBW Whitehead reduction in higher_genus_modular_koszul.tex (AP198).
./scripts/mega_rescue_100.py:98:    ("M07_higher_genus_modular", "chapters/theory/higher_genus_modular_koszul.tex", "Theorems D + MC1-MC2 + shadow tower. Verify non-circularity (AP191). MC1 Whitehead (AP198). Depth gap (AP219). D^2=0 space (AP220). Cross-check with Faber-Pandharipande for F_g."),
./scripts/platonic_rectification_20.py:247:YOUR MISSION: PROVE the Whitehead reduction properly:
./resume_20260413_165929/B11_orphaned_chapters.md:101:CLAUDE.md:1081:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
./resume_20260413_165929/B11_orphaned_chapters.md:102:resume_20260413_163457/S15_appendices_to_body.md:172:CLAUDE.md:1079:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
./resume_20260413_165929/M07_higher_genus_modula…2888 tokens truncated…d lemma scope error.
./platonic_rectification_20260413_114523/P08_MC1_PBW_whitehead_upgrade.md:3:[higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:895) now makes the Whitehead reduction explicit instead of informal. I added a weightwise reduction lemma and a mixed-map factorization lemma at [lines 912-1003](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:912), rewrote the Kac--Moody genus-1 and all-genera PBW proofs to use them at [1005-1317](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1005), and recorded the optimal semisimple bound plus the non-semisimple obstruction at [2034-2058](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2034).
./platonic_rectification_20260413_114523/P08_MC1_PBW_whitehead_upgrade.md:17:- BEFORE: `thm:pbw-allgenera-km` (`ProvedHere`) asserted all-genera PBW degeneration by saying the genus-1 mechanism is genus-independent, but the Whitehead reduction was still only stated heuristically.
 succeeded in 52ms:
 M appendices/ordered_associative_chiral_kd.tex
 M bibliography/references.tex
 M chapters/theory/chiral_koszul_pairs.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_complementarity.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/ordered_associative_chiral_kd.tex
 M standalone/ordered_chiral_homology.tex
 M standalone/references.bib
?? elite_rescue_20260413_221642/L07_KS_comparison.md
?? elite_rescue_20260413_221642/L08_Livernet_comparison.md
?? elite_rescue_20260413_221642/L09_CFG_E3_comparison.md
?? elite_rescue_20260413_221642/L10_GR_comparison.md
?? final_gaps_20260413_213946/G11_provedhere_theory_2.md
?? final_gaps_20260413_213946/G12_provedhere_rest.md
?? final_gaps_20260413_213946/G13_vol2_thm_status_propagate.md
?? final_gaps_20260413_213946/G14_vol3_thm_status_propagate.md
?? final_gaps_20260413_213946/G15_vol2_3d_gravity_topol_scope.md
?? opus_audit_20260413_224154/
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1285,1345p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
E_\infty^{*,2}(g{=}0)$ follows.

A symbolic check of the same mechanism at the next tensor
powers, implemented in
\nolinkurl{compute/lib/genus1_pbw_sl2.py},
confirms that no new representation-theoretic obstruction
appears. The diagonal Casimir eigenspace dimensions are:
\[
\begin{aligned}
\mathfrak{sl}_2^{\otimes 3}&:\ \{24{:}7,\;12{:}10,\;4{:}9,\;0{:}1\},\\
\mathfrak{sl}_2^{\otimes 4}&:\ \{40{:}9,\;24{:}21,\;12{:}30,\;4{:}18,\;0{:}3\},\\
\mathfrak{sl}_2^{\otimes 5}&:\ \{60{:}11,\;40{:}36,\;24{:}70,\;12{:}75,\;4{:}45,\;0{:}6\},\\
\mathfrak{sl}_2^{\otimes 6}&:\ \{84{:}13,\;60{:}55,\;40{:}135,\;24{:}203,\;12{:}200,\;4{:}108,\;0{:}15\},\\
\mathfrak{sl}_2^{\otimes 7}&:\ \{112{:}15,\;84{:}78,\;60{:}231,\;40{:}441,\\
&\qquad 24{:}588,\;12{:}525,\;4{:}273,\;0{:}36\}
\quad\textup{(sparse/modular extraction).}
\end{aligned}
\]
These match the expected irreducible decompositions.


thinking
**Checking file modifications**

I need to be careful about any existing modifications in the target file, as there may be changes made by the user or other agents. It sounds like inspecting the git diff for the relevant file could help me understand the baseline. I should check for uncommitted changes in this file to avoid overwriting anything unrelated. I might use `git diff -- chapters/theory/higher_genus_modular_koszul.tex` around the relevant lines to see any pending changes, keeping it noninteractive.
codex
`higher_genus_modular_koszul.tex` is already dirty in the worktree, so I’m checking the local diff before editing anything. I need to preserve unrelated in-flight changes and only touch the exact Whitehead surface if the current wording still leaves AP198 exposed.
exec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index b0aa08e..12a3043 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3910,105 +3910,6 @@ argument. The universal MC element on the coinvariant modular
 convolution algebra is therefore proved in full generality.
 \end{theorem}
 
-\begin{remark}[Scope of MC2 in this chapter]
-\index{MC2!coinvariant scope}
-Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
-statement: its target dg~Lie algebra is
-$\gAmod \cong \Defcyc(\cA)\widehat{\otimes}\Gmod$.
-The ordered lift
-$\Theta_\cA^{E_1} = D_\cA^{E_1} - \dzero \in
-\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
-Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
-$\Theta_\cA^{E_1}$ to~$\Theta_\cA$. Any external citation of
-Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
-therefore incorrect; the ordered theorem is
collab wait(call_23fYI4B5Eqgvw6hIYeScgxBe)
  receivers: 019d88a1-72d8-7191-845e-280d6781c1fa

thinking
**Confirming AP198 reduction correctness**

I'll verify that the reduction from the truncated current algebra to the semisimple algebra g is explicitly stated and mathematically sound. Key references include `chapters/theory/higher_genus_modular_koszul.tex:919` for the lemma ensuring the truncated algebra records only mode patterns and factors through g, `:1001` for supporting statements on cohomology, and `:1326` for the remark emphasizing Whitehead reduction. All labels and statuses are consistent with no fix needed for AP198’s requirements.
codex
**AP198 Surface**

- `Lemma \ref{lem:pbw-weightwise-g-module}` (lines near `chapters/theory/higher_genus_modular_koszul.tex:919`) explicitly states that the weight‑$h$ enrichment block decomposes as a finite direct sum of `C^*(\fg, M_{h,\nu})` factors, with the truncated current algebra `\fg⊗V_h` supplying only the passive mode pattern data and the actual Whitehead input happening on the finite‑dimensional $\fg$-modules. The same passage notes that, after fixing a mode pattern, the residue action factors through the diagonal adjoint action of the semisimple $\fg`; there is therefore no need to invoke Whitehead on the non‑semisimple truncated algebra itself, so the reduction is both explicit and mathematically correct for AP198.
- The remark “Whitehead reduction in the PBW proof” (`chapters/theory/higher_genus_modular_koszul.tex:1326`) restates the same reduction for emphasis: after rewriting the weight block as `C^*(\fg, M_{h,\nu})`, all cohomology computations live on $\fg$ and the truncated algebra contributes only multiplicities, so no vanishing is claimed for `\fg⊗V_h`. The nearby text around line `1000` also clarifies that the mixed genus interaction is controlled by $H^1(\fg, N_h^{n-1})$ rather than a cohomology theory for the truncated current algebra.
- Labels/statuses are in order: the lemma carries `\ClaimStatusProvedHere`, and the remark is appropriately titled; no missing labels or status issues crop up in the requested neighborhood.

No surgical fix is needed—the reduction is already explicit, correct, and properly annotated for AP198.
wait(call_23fYI4B5Eqgvw6hIYeScgxBe) 1 agents complete:
  019d88a1-72d8-7191-845e-280d6781c1fa completed: "**AP198 Surface**

- `Lemma \ref{lem:pbw-weightwise-g-module}` (lines near `chapters/theory/higher_genus_modular_koszul.…"
codex
The explicit reduction is already present in the local lemmas, but I’m checking the later all-genera PBW lane too so AP198 is closed on the whole MC1 surface rather than only in the genus-1 proof.
exec
/bin/zsh -lc "sed -n '1,220p' platonic_rectification_20260413_114523/P08_MC1_PBW_whitehead_upgrade.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2055,2095p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1935,2055p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 50ms:

\begin{remark}[Optimal semisimple page bound and the non-semisimple
 obstruction]
\index{PBW spectral sequence!optimal semisimple page bound|textbf}
\index{PBW spectral sequence!non-semisimple obstruction|textbf}
The semisimple PBW conclusion is an $E_3$ statement, not an
$E_1$ statement. The affine KM proof gives the boundary example:
at weight~$2$ the Killing-form class is $d_1$-closed and nonzero on
$E_2$, and only the family-specific $d_2$ contraction kills it.
Hence one cannot strengthen the semisimple theorem to an
$E_1$-collapse claim without adding a false statement.

For a general weightwise Lie symmetry algebra
$\mathfrak{l}_h = \mathfrak{s}_h \ltimes \mathfrak{r}_h$
\textup{(}Levi decomposition\textup{)}, the enrichment is governed by
the Hochschild--Serre spectral sequence
\[
E_2^{p,q}(h)
\;=\;
H^p\!\bigl(\mathfrak{s}_h,\,
 succeeded in 51ms:
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
(Lie bracket residue from the $(0)$-products of the generators)
acts on the enrichment through the $\fg$-module
factor~$M_h^{\mathrm{non\text{-}triv}}$, leaving the
$H^{1,0}(\Sigma_g)$ factor unchanged. The enrichment complex

thinking
**Considering file edits**

I'm thinking about the decomposition, but since the file is dirty, caution is required. If the current wording is correct, maybe no edit is necessary. However, I wonder if it would be a good idea to search specific lines, like 1011-1030 and 1290-1300 in the current file. Using `nl` to check line numbers could help clarify things. Let's see how that goes!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1005,1035p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1324,1338p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1290,1310p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1290	confirms that no new representation-theoretic obstruction
  1291	appears. The diagonal Casimir eigenspace dimensions are:
  1292	\[
  1293	\begin{aligned}
  1294	\mathfrak{sl}_2^{\otimes 3}&:\ \{24{:}7,\;12{:}10,\;4{:}9,\;0{:}1\},\\
  1295	\mathfrak{sl}_2^{\otimes 4}&:\ \{40{:}9,\;24{:}21,\;12{:}30,\;4{:}18,\;0{:}3\},\\
  1296	\mathfrak{sl}_2^{\otimes 5}&:\ \{60{:}11,\;40{:}36,\;24{:}70,\;12{:}75,\;4{:}45,\;0{:}6\},\\
  1297	\mathfrak{sl}_2^{\otimes 6}&:\ \{84{:}13,\;60{:}55,\;40{:}135,\;24{:}203,\;12{:}200,\;4{:}108,\;0{:}15\},\\
  1298	\mathfrak{sl}_2^{\otimes 7}&:\ \{112{:}15,\;84{:}78,\;60{:}231,\;40{:}441,\\
  1299	&\qquad 24{:}588,\;12{:}525,\;4{:}273,\;0{:}36\}
  1300	\quad\textup{(sparse/modular extraction).}
  1301	\end{aligned}
  1302	\]
  1303	These match the expected irreducible decompositions.
  1304	
  1305	The bracket differential has ranks
  1306	$\operatorname{rank}(d_1)=8$ at $n=3$ and
  1307	$\operatorname{rank}(d_1)=27$ at $n=4$ and
  1308	$\operatorname{rank}(d_1)=80$ at $n=5$ and
  1309	$\operatorname{rank}(d_1)=243$ at $n=6$ and
 succeeded in 51ms:
  1005	enrichment class as a sum of tensors
  1006	$(a_1 \otimes \cdots \otimes a_n) \otimes \alpha_r$ with fixed mode
  1007	pattern. For each such tensor, isolate the $\fg$-label attached to the
  1008	slot carrying the regular form and collect the remaining bar data into
  1009	the coefficient module~$N_h^{n-1}$. This gives the map
  1010	$\iota_{g,h,n}$ to degree-one Chevalley--Eilenberg cochains.
  1011	
  1012	The mixed residue brackets the distinguished $\fg$-label with one of
  1013	the remaining labels and then forgets the regular genus form. The
  1014	Jacobi identity for the residue bracket is exactly the cocycle
  1015	condition on $\iota_{g,h,n}(\xi)$ when
  1016	$d_{1,\mathrm{enr}}(\xi) = 0$. Changing $\xi$ by a
  1017	$d_{1,\mathrm{enr}}$-boundary changes $\iota_{g,h,n}(\xi)$ by a
  1018	Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
  1019	depends only on the image of $\iota_{g,h,n}(\xi)$ in
  1020	$H^1(\fg, N_h^{n-1})$.
  1021	\end{proof}
  1022	
  1023	\begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
  1024	\label{thm:pbw-genus1-km}
 succeeded in 50ms:
  1324	\end{proof}
  1325	
  1326	\begin{remark}[Whitehead reduction in the PBW proof]
  1327	For fixed conformal weight~$h$, the truncated current algebra
  1328	$\fg \otimes V_h$ only records which modes can occur. The actual
  1329	Whitehead input appears after rewriting the weight-$h$ enrichment
  1330	block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
  1331	\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)},
  1332	and the mixed genus-$0$/genus-$1$ map factors through
  1333	$H^1(\fg, N_h^{n-1})$
  1334	\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
  1335	The Lie algebra~$\fg$ acts diagonally on the $\fg$-labels; the
  1336	mode and $H^1$ factors are passive coefficients. No vanishing
  1337	statement is invoked for the non-semisimple Lie algebra
  1338	$\fg \otimes V_h$ itself.
codex
I’m not editing yet because the local proof lane already looks repaired. I’m doing one last hostile grep for AP198-style regressions in this chapter: any place that still applies Whitehead to `\fg \otimes V_h` itself, or blurs the reduction back into the truncated algebra.
exec
/bin/zsh -lc "rg -n \"Whitehead\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"H\\"'^1'"\\(\\\\fg \\\\otimes V_h|Whitehead.*\\\\fg \\\\otimes V_h|non-semisimple Lie algebra \\\\fg \\\\otimes V_h|factors through the diagonal adjoint action of the finite-dimensional semisimple Lie algebra \\\\fg|C\\"'^'"\\*\\(\\\\fg, M_\\{h,\\\\nu\\}\\)|H\\"'^1'"\\(\\\\fg, N_h\\"'^'"\\{n-1\\}\\)\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:H\^1\(\fg \otimes V_h|Whitehead.*\fg \otimes V_h|non-semisimple Lie algebra \fg \otimes V_h|factors through the diagonal adjoint action of the finite-dimensional semisimple Lie algebra \fg|C\^\*\(\fg, M_\{h,\nu\}\)|H\^1\(\fg, N_h\^\{n-1\}\))
                 ^^
error: unrecognized escape sequence
 succeeded in 52ms:
899:Higher-genus PBW holds for KM (Whitehead + Killing contraction,
905:non-trivial isotypic pieces killed by Whitehead on the $d_1$ page and
939:records the mode cutoff only: the Whitehead step is carried out on
978:\index{Whitehead lemma!mixed genus-0/genus-g factorization}
1037:by Whitehead; the Killing-form invariant
1048:enrichment factorization, Whitehead acyclicity, and the
1154:finite-dimensional $\fg$-module~$N_h^{n-1}$. Thus the Whitehead step
1177:Whitehead's first lemma for semisimple~$\fg$
1184:semisimple extension of Whitehead then gives:
1231:We exhibit the interplay of Whitehead vanishing and
1265: Whitehead's theorem gives
1282:three by the bracket isomorphism, five by Whitehead, one by the
1316:summands killed by Whitehead, invariant summands passed to
1322:decomposition under~$\fg$ and the Whitehead vanishing
1326:\begin{remark}[Whitehead reduction in the PBW proof]
1329:Whitehead input appears after rewriting the weight-$h$ enrichment
1375:Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
1401:three-step mechanism (PBW decomposition, Whitehead
1455:\emph{Step~2: Whitehead acyclicity of the enrichment.}
1477:$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead

thinking
**Revising grep usage**

I need to rerun my grep command, but with fixed quoting this time. I’m thinking about using fgrep or perhaps rg with the -F option for fixed-string searching. It’s interesting to ponder how these changes might improve my command's accuracy. I want to ensure that I capture exactly what I need without missing anything. Let’s see how those adjustments work out when I run it again!
exec
/bin/zsh -lc "rg -n -F 'H"'^1('"\\fg \\otimes V_h' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -F 'C"'^*('"\\fg, M_{h,\\nu})' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'H"'^1('"\\fg, N_h"'^{n-1})'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'non-semisimple Lie algebra \\fg \\otimes V_h' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1143:$C^*(\fg, M_{h,\nu})$, or equivalently
1330:block as a finite direct sum of complexes $C^*(\fg, M_{h,\nu})$
1450:Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
 succeeded in 51ms:
989:H^1(\fg, N_h^{n-1})
999:$H^1(\fg, N_h^{n-1})$ and does not require any cohomology theory for
1020:$H^1(\fg, N_h^{n-1})$.
1153:mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
1175:$H^1(\fg, N_h^{n-1}) = 0$
1333:$H^1(\fg, N_h^{n-1})$
1477:$H^1(\fg, N_h^{n-1})$ as in genus~$1$. Thus the Whitehead
 exited 1 in 51ms:


thinking
**Inspecting patterns**

I don't see any direct bad patterns at the moment, which is a relief! But I think it would be wise to inspect the all-genera proof around 1450 just to be extra cautious. I need to focus on searching through lines 1435 to 1490 to ensure that nothing slips through the cracks. It feels good to be thorough, so I’m on it! I'm glad I’m being diligent about this.
exec
/bin/zsh -lc "sed -n '1438,1492p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where $M_h$ is the \emph{same} finite-dimensional
$\fg$-module as at genus~$1$.
This factorization holds because the
$H^{1,0}(\Sigma_g)$ forms enter as global
multiplicative factors that do not interact with the
OPE data: the collision divisors (where OPE poles live)
are codimension-$1$ loci in $\overline{C}_n(\Sigma_g)$,
and the regular forms from $H^{1,0}(\Sigma_g)$ are
smooth across these divisors. The module~$M_h$ is
determined solely by the OPE structure of~$\widehat{\fg}_k$
truncated at weight~$h$, which is genus-independent. Equivalently,
the weight-$h$ enrichment block is the same finite direct sum of
Chevalley--Eilenberg complexes $C^*(\fg, M_{h,\nu})$ as in
genus~$1$, indexed by the finitely many mode patterns
\textup{(}Lemma~\textup{\ref{lem:pbw-weightwise-g-module}}\textup{)}.

\medskip
\emph{Step~2: Whitehead acyclicity of the enrichment.}

The $d_1^{\mathrm{PBW}}$ differential (Lie bracket residue)
codex
The AP198 gap is closed on disk already. The weightwise reduction lemma, the mixed-map factorization lemma, the genus-1 proof, the all-genera proof, and the local remark all agree that Whitehead is applied only to finite-dimensional `\fg`-modules, never to the non-semisimple truncated current algebra itself.
codex
FIXED. No edit was needed: the AP198 repair is already present on disk, and it is correct.

The reduction from the truncated current algebra to `\fg` is explicit in the current file:
- [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:917) proves the weightwise decomposition `\mathcal E_g^{*,h} \cong \bigoplus_\nu C^*_{\mathrm{CE}}(\fg,M_{h,\nu}) \otimes H^1(\Sigma_g,\bC)`, with `\fg \otimes V_h` used only for mode bookkeeping.
- [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:976) proves the mixed map factors through `H^1(\fg,N_h^{n-1})`.
- [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1326) states the scope cleanly: Whitehead is applied only to finite-dimensional `\fg`-modules, never to the non-semisimple Lie algebra `\fg \otimes V_h`.

I also checked the downstream PBW proofs at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1138) and [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1455); both use the repaired reduction correctly. This is the P08 repair, and it survives verification against the current source and the P08 rectification note. A hostile grep found no remaining AP198-style claim in this chapter applying Whitehead directly to `\fg \otimes V_h`.
tokens used
145,541
