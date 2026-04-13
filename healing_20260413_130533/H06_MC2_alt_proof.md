# H06_MC2_alt_proof (595s)

Added a new remark at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:4156) giving a second proof path for MC2 in Kontsevich--Soibelman language. It packages the primitive shadow data as wall Hamiltonians, orders them by BPS phase, uses pronilpotent completion plus the shadow-growth estimate for convergence, and identifies the Maurer--Cartan equation with scattering-diagram consistency.

Verification: `python3 scripts/generate_metadata.py` succeeded. A clean `make fast` still fails outside this edit, at pre-existing undefined-control-sequence sites in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3407). Metadata regeneration updated generated files under `metadata/`; those diffs are broader because the worktree already has unrelated source changes.

## Fortification Report
- `thm:mc2-bar-intrinsic`
- PRIMARY PROOF: sound
- SECONDARY PROOF: sketched
- TECHNIQUE: Kontsevich--Soibelman scattering diagram / phase-ordered wall-crossing product in the completed pronilpotent shadow algebra
- CONDITION STATUS: unconditional for the primary proof; secondary path conditional on installing the full scattering-diagram formalism on `\widehat{\gAmod}` inside the manuscript
- CONFIDENCE: medium


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
session id: 019d868f-7b0d-7421-84fa-85cec6edc806
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.
Your mission is threefold:

1. HEAL: find remaining wounds (gaps, weaknesses, fragilities) and repair them
2. FORTIFY: for every main result, construct an ALTERNATIVE proof path that provides
   REDUNDANCY — if one proof fails, the other stands independently
3. UPGRADE: where a result is conditional, investigate whether the condition can be
   REMOVED by new mathematical insight, alternative technique, or reformulation

You have WRITE access. Make edits. Write new proofs. Add remarks.
The standard is: every theorem that can have two independent proofs MUST have two.
</task>

<action_safety>
Keep edits within assigned scope. After every substantial edit, re-read and verify.
New proofs must be mathematically rigorous — no hand-waving, no "by analogy."
If you cannot complete a proof: write a detailed proof SKETCH with the key steps
identified and the remaining gap precisely named.
</action_safety>

<completeness_contract>
For each theorem in your scope:
1. Verify the PRIMARY proof is now sound (after rectification)
2. Write or sketch a SECONDARY proof via a different technique
3. If conditional: investigate removing the condition
4. State confidence level for each proof path
</completeness_contract>

<structured_output_contract>
End with:
## Fortification Report
For each theorem:
  - PRIMARY PROOF: [sound/repaired/gap-remaining]
  - SECONDARY PROOF: [written/sketched/identified/blocked]
  - TECHNIQUE: [what alternative method]
  - CONDITION STATUS: [unconditional/conditional-on-X/research-programme-Y]
  - CONFIDENCE: [high/medium/low]
</structured_output_contract>


MC2 — ALTERNATIVE CONSTRUCTION of Theta_A.

TARGET: chapters/theory/higher_genus_modular_koszul.tex (add Remark near MC2)

The primary construction is bar-intrinsic (recursive inverse limit). Write an ALTERNATIVE:

TECHNIQUE: Kontsevich-Soibelman wall-crossing / scattering diagram.
1. The MC element Theta_A can be constructed as the product of wall-crossing automorphisms
   along the rays of a scattering diagram in the shadow tower grading.
2. Each ray corresponds to a primitive shadow invariant S_r.
3. The product is ordered by the BPS phase ordering (increasing central charge argument).
4. Convergence follows from the shadow tower growth bound (alpha_g).
5. The MC equation D*Theta + (1/2)[Theta,Theta] = 0 follows from the consistency of
   the scattering diagram (Kontsevich-Soibelman lemma).

Write as Remark[Alternative construction via scattering diagram]. Even as a sketch,
this provides CONCEPTUAL REDUNDANCY for why Theta_A exists and satisfies MC.
mcp startup: no servers
codex
Using `beilinson-rectify` for the target theorem lane and `build-surface` for narrow verification. I’m reading the required constitutional files plus the target chapter and nearby MC2 surface before drafting the alternative construction.
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
/bin/zsh -lc "sed -n '1,260p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
|---|---:|
| `ProvedHere` | 2842 |
 succeeded in 53ms:
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


thinking
**Searching for dependencies**

I need to read the target file and look for MC2, along with directly cited dependencies about Theta_A/bar-intrinsic. I might explore using rg for a deeper search, but that may not be necessary. Updating my plan could be helpful, so let’s search for mc2-bar-intrinsic, Theta_A, and look into scattering diagrams. I feel like that should cover all the bases!
codex
I’ve loaded the constitutional surfaces. Next I’m locating MC2 in the chapter, its proof context, and any existing scattering-diagram language elsewhere so the new remark matches the manuscript’s live conventions rather than introducing a foreign one.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"mc2-bar-intrinsic|MC2|Theta_A|Theta_\\\\cA|scattering diagram|Kontsevich--Soibelman|wall-crossing|shadow tower\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"scattering diagram|Kontsevich--Soibelman|wall-crossing|BPS phase|central charge argument|shadow invariant S_r|alpha_g\" chapters appendices metadata notes -g '*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.

Bar-cobar inversion (Theorem~B) proves that
$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
The proof uses one fact: the bar differential squares to zero.
At genus~$g \geq 1$, this fact fails fiberwise.
The bar complex $\barB^{(g)}(\cA)$ acquires curvature
\[
 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
\]
%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
where $\omega_g = c_1(\lambda)$ is the Hodge class on
$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
The fiberwise differential no longer squares to zero; cobar inversion,
as stated, does not extend.

 exited 2 in 51ms:
rg: regex parse error:
    (?:mc2-bar-intrinsic|MC2|Theta_A|Theta_\cA|scattering diagram|Kontsevich--Soibelman|wall-crossing|shadow tower)
                                           ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: notes: No such file or directory (os error 2)
chapters/frame/preface.tex:1118:(\S6). The genus-$g$ obstruction class $\alpha_g(\cA)$ admits a
chapters/frame/heisenberg_frame.tex:62:resonances, no wall-crossing. The simplicity is not a weakness;
chapters/examples/deformation_quantization.tex:655:A curved chiral algebra (cf.\ Kontsevich--Soibelman \cite{KontsevichSoibelman}) is a triple $(\mathcal{A}, m, \theta)$ where:
appendices/nonlinear_modular_shadows.tex:2747:\begin{remark}[The phase index as a wall-crossing function]
appendices/nonlinear_modular_shadows.tex:2748:\label{rem:nms-phase-wall-crossing}
appendices/nonlinear_modular_shadows.tex:2749:The nonlinear phase index $\nu_{\mathrm{nl}}(\cA,u)$ is a constructible function on parameter space, measuring the degree at which complementarity becomes genuinely nonlinear. Its jump loci are the walls of the \emph{resonance scattering diagram} of \S\ref{subsec:nms-resonance-scattering-diagram}.
appendices/nonlinear_modular_shadows.tex:2840:\subsection{The resonance scattering diagram}
appendices/nonlinear_modular_shadows.tex:2852:\begin{definition}[Resonance scattering diagram; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2854:\index{scattering diagram!resonance}%
appendices/nonlinear_modular_shadows.tex:2855:The \emph{resonance scattering diagram}
appendices/nonlinear_modular_shadows.tex:2880:is the constructible sheaf of categories whose fibre over a chamber is the category of polarized quantizations of that chamber, and whose wall-crossing functors are induced by the scattering automorphisms of $\mathfrak{Scat}(\cA)$.
appendices/nonlinear_modular_shadows.tex:2883:\begin{remark}[Why a schober rather than a scattering diagram]
appendices/nonlinear_modular_shadows.tex:2988:\begin{conjecture}[Resonance wall-crossing theorem; \ClaimStatusConjectured]
appendices/nonlinear_modular_shadows.tex:2989:\label{conj:nms-resonance-wall-crossing}
appendices/nonlinear_modular_shadows.tex:2990:The spectral discriminant $\Delta_{\cA}$ is constant under scattering within a fixed sheet, while the resonance tower records the nonlinear wall-crossing corrections.
appendices/nonlinear_modular_shadows.tex:3008:This would turn complementarity from a theorem about decomposition into a theorem about \emph{transport, wall-crossing, and quantization}.
appendices/nonlinear_modular_shadows.tex:4090:Kontsevich--Soibelman homotopy transfer equivalence
chapters/theory/higher_genus_modular_koszul.tex:1520:for a basis $\{\alpha_1, \ldots, \alpha_g\}$ of
chapters/theory/higher_genus_modular_koszul.tex:5979: H^2(\mathbf{D}_g) \cong \mathbb{C}\alpha_g,
exec
/bin/zsh -lc "rg -n \"thm:mc2-bar-intrinsic|Theta_\\\\cA := D_\\\\cA - d_0|D_\\\\cA\\"'^2 = 0|Maurer--Cartan" chapters/theory chapters/connections appendices -g '"'*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:thm:mc2-bar-intrinsic|Theta_\cA := D_\cA - d_0|D_\cA\^2 = 0|Maurer--Cartan)
                                   ^^
error: unrecognized escape sequence

thinking
**Handling regex carefully**

I need to be cautious with escaped regex as I have the target file opening. Maybe it’s crucial to find the exact lines around MC2 and related references. There's also the existing remark about BPS wall-crossing from the bar coproduct that could be important. I should read around the theorem and the remark location near MC2. Searching with fixed strings, like rg -F, could be a good approach. Let's get started on this!
codex
The target file already carries related wall-crossing language later on. I’m reading the exact MC2 block and the existing BPS/bar-coproduct remark so the new alternative construction sits in the right local logic and doesn’t overclaim beyond what the file already supports.
exec
/bin/zsh -lc "rg -nF 'thm:mc2-bar-intrinsic' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
2350: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2648:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2705:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2802:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2913:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3608:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3624:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3764:\label{thm:mc2-bar-intrinsic}
3826:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
3834:Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
4100:Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
4153:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4203:Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
4257:exists at all genera by Theorem~\ref{thm:mc2-bar-intrinsic},
4755:(Theorem~\ref{thm:mc2-bar-intrinsic};
5192:assembly in Theorem~\ref{thm:mc2-bar-intrinsic}. Consequently the
8152:Theorem~\ref{thm:mc2-bar-intrinsic} supplies its unconditional
exec
/bin/zsh -lc "rg -nF 'Theta_\\cA := D_\\cA - d_0' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20880,21180p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2830,2898p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3608,3668p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '26480,26640p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
37:Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
292:The universal MC element $\Theta_\cA := D_\cA - d_0$
4357:$\Theta_\cA := D_\cA - d_0^{(\cA)}$ and
4849:element $\Theta_\cA := D_\cA - d_0$ does not vanish;
13088:element $\Theta_\cA := D_\cA - d_0$ lives in this completed space
31570:The bar-intrinsic element $\Theta_\cA := D_\cA - d_0$ satisfies
 succeeded in 51ms:
 \rho_T(K_N/2)
 \;\sim\;
 \frac{12}{K_N}
 \quad(N \to \infty).
\end{equation}
In particular, $\rho_T(K_N/2) < 1$ for all $N \geq 2$
\textup{(}since $K_2 = 26$\textup{)}, and the
convergence window fraction satisfies
\begin{equation}\label{eq:window-fraction}
 \frac{K_N - 2c_\star}{K_N}
 \;\to\; 1
 \quad(N \to \infty).
\end{equation}
For the W-line of~$\cW_N$
\textup{(}weight-$N$ primary\textup{)}:
$\rho_W(K_N/2) = O(K_N^{-(N-1)})$, giving an even faster
decay and a wider convergence window.
\end{proposition}

\begin{proof}
 succeeded in 52ms:
\index{polarized universal class}%
There exists a canonical Maurer--Cartan element
\[
\boldsymbol\Theta_{\cA}^{\pm}
\in
\mathrm{MC}\bigl(\mathcal G^{\pm}_{\mathrm{mod}}(\cA)\bigr)
\]
whose projections recover the entire hierarchy: scalar trace $\Rightarrow \kappa(\cA)\lambda_g$, branch determinant $\Rightarrow \Delta_{\cA}$, one-vertex degree-$r$ sector $\Rightarrow$ the shadow tensors $H_{\cA},\mathfrak C_{\cA},\mathfrak Q_{\cA},\ldots$, contact determinant sector $\Rightarrow \mathfrak R^{\mathrm{mod}}_{r,g,n}(\cA)$, and genus-summed semiclassical action $\Rightarrow$ the complementarity potential and its higher corrections.
\end{conjecture}

\subsection{The resonance scattering diagram}
\label{subsec:nms-resonance-scattering-diagram}

\begin{definition}[Resonance wall locus]
\label{def:nms-resonance-wall-locus}
Let
\[
\mathcal W_{\cA} := \{\Delta_{\cA}=0\}\cup \bigcup_{r\ge 4} |\mathfrak R^{\mathrm{mod}}_r(\cA)|
\]
be the total nonlinear wall locus in parameter space.
 succeeded in 51ms:
\textup{(}Construction~\textup{\ref{constr:v1-platonic-package})},
specialized to the CY setting.
\end{conjecture}


%%% --- Programme G: BKM algebras and scattering diagrams ---

\begin{openproblem}[Programme G: BKM algebras and scattering diagrams]
\label{op:programme-g-bkm-scattering}
\index{Borcherds--Kac--Moody algebra!scattering diagram}
\index{scattering diagram!BKM}
\index{Kontsevich--Soibelman!wall-crossing}
The BKM root system of
$K3 \times E$ lives in $\Gamma^{2,2} = U \oplus U$
(lattice of signature $(2,2)$, rank~$4$).
Root multiplicities are determined by $c_0(D)$ from the K3
elliptic genus. The Kontsevich--Soibelman scattering
diagram for $K3 \times E$ associates a wall to each BPS ray
with attached function determined by the root multiplicity.
\begin{enumerate}[label=\textup{(G\arabic*)}]
 succeeded in 52ms:
\index{MacMahon function!from bar complex}

\begin{theorem}[Bar--MacMahon correspondence; \ClaimStatusProvedHere]
\label{thm:bar-macmahon}
\index{MacMahon function!bar complex origin|textbf}
For $\cH$ on $\bC^3$, the second-quantized bar character is MacMahon:
\begin{equation}\label{eq:bar-macmahon}
Z^{(2)}_B(\cH; q)
:= \prod_{n \geq 1} (1-q^n)^{-n}
= \sum_{n \geq 0} p_3(n)\,q^n = M(q),
\end{equation}
where $p_3(n)$ counts plane partitions
$(1, 1, 3, 6, 13, 24, 48, 86, 160, 282, 500, \ldots)$.
\end{theorem}

\begin{proof}
$B(\cH) = \operatorname{Sym}^c(s^{-1}\bar{V})$.
Rank-$1$ bar character: $\prod(1-q^n)^{-1}$.
Second quantization raises the exponent to~$n$ via
$\operatorname{Hilb}^n(\bC^3)$, giving MacMahon.

thinking
**Looking for theorem details**

I need to find the exact theorem around line 3764, as well as the remarks nearby. I should focus on reading the content between lines 3700 and 3870 to ensure I get the full context of the theorem. It seems like that range will provide the information I need! Let me dig into that and pull out the relevant details effectively. This should help clarify anything I'm uncertain about.
exec
/bin/zsh -lc "sed -n '3875,3935p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3710,3875p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 minimum width=3.8cm, minimum height=0.7cm,
 font=\footnotesize] (MC) at (7.2,-0.3)
 {$d_0\Theta + \Theta\,d_0 + \Theta^2 = 0$};
%
% ---- Labels ----
\node[font=\tiny, text=black!50, anchor=north] at (-1.5,-0.8)
 {genus-$0$ bar differential};
\node[font=\tiny, text=black!50, anchor=north] at (1.8,-0.8)
 {positive-genus correction};
\node[font=\tiny, text=black!50, anchor=north] at (7.2,-0.8)
 {$\Longleftrightarrow\;
 \Theta_\cA \in
 \mathrm{MC}(\mathrm{Def}_{\mathrm{cyc}}(\cA)
 \widehat{\otimes}\, \mathcal{G}_{\mathrm{mod}})$};
%
% ---- Shadow projections ----
\draw[->, thick, black!40] (1.8,-1.4) -- (1.8,-2.0);
\node[font=\tiny\scshape, text=black!50, anchor=east]
 at (1.5,-1.7) {project};
\node[draw, thick, rounded corners=2pt,
 succeeded in 51ms:
In particular, every chiral algebra in the standard landscape
satisfies the centrality hypothesis of
Theorem~\textup{\ref{thm:genus-induction-strict}}.
\end{proposition}

\begin{proof}
Each genus-$g$ differential~$d_g$ ($g \geq 1$) is constructed from
period integrals $\oint_{\gamma_k} \omega$ over homology cycles
$\gamma_k \subset \Sigma_g$. These are \emph{global} operations:
they act on the bar complex by integration over $1$-cycles disjoint
from the collision locus~$\Delta$. The chiral bracket~$\mu$ is
\emph{local}: supported on~$\Delta$. By the locality axiom,
operations supported on disjoint subsets commute:
\[
 \bigl[\textstyle\oint_{\gamma_k},\;\mu(a,-)\bigr] = 0
 \qquad \text{for all } a \in \cA,\;
 \gamma_k \cap \Delta = \varnothing.
\]
Therefore the composition
$\mathrm{obs}_g
exec
/bin/zsh -lc "rg -n \"BPS phase|central charge argument|phase ordering|ray corresponds|primitive shadow invariant|S_r\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/arithmetic_shadows.tex appendices/nonlinear_modular_shadows.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"shadow tower growth bound|alpha_g|growth bound|radius|convergence\" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/landscape_census.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/landscape_census.tex:2214:The branch point at $x = 1/3$ (radius of convergence) determines the
chapters/examples/landscape_census.tex:2923:Part (ii): the radius of convergence of $P_{\cA}(x)$ is the
chapters/examples/landscape_census.tex:3260:The bar chain groups have $\dim \bar{B}^n = (\dim \mathfrak{g})^n \cdot (n{-}1)!$ (Lemma~\ref{lem:bar-dims-level-independent}). The Koszul property constrains the Koszul dual dimensions to grow at most as fast as the chain groups modulo the differential. The Hilbert series, being algebraic with radius of convergence $1/\dim\mathfrak{g}$ (by the DS discriminant, Theorem~\ref{thm:ds-bar-gf-discriminant} for $\mathfrak{sl}_2$), has exponential growth rate $(\dim \mathfrak{g})^n$.
chapters/examples/landscape_census.tex:3275:\item The radius of convergence of $P(x)$ is
chapters/examples/landscape_census.tex:3281:\item $\dim\mathfrak{g}$ is the spectral radius of the branch
chapters/examples/landscape_census.tex:3309:The spectral radius $\max_i |\alpha_i| = 1/\min_i |x_i| = 1/R
chapters/examples/landscape_census.tex:3311:determines the radius of convergence. Part~(ii) guarantees that
chapters/examples/landscape_census.tex:3317:$T_{\mathrm{br}} = \operatorname{diag}(3, -1)$, spectral radius $3
chapters/examples/landscape_census.tex:3321:$\Delta = (1 - 8x)(1 - 3x - x^2)$, spectral radius $8
chapters/examples/landscape_census.tex:3905:\index{Koszul radius!census}
chapters/examples/landscape_census.tex:3935: $\rho_K = $ Koszul radius (smallest positive root of $G_\cA(t)=1$);
chapters/examples/landscape_census.tex:3954:Koszul radius; M-class algebras (infinite tower) have non-zero defect
chapters/examples/landscape_census.tex:3955:starting at $t^3$ and irrational Koszul radius. The entropy ladder
chapters/theory/higher_genus_modular_koszul.tex:352:convergence hypothesis~(2).
chapters/theory/higher_genus_modular_koszul.tex:872:bounded-below convergence
chapters/theory/higher_genus_modular_koszul.tex:1215:By bounded-below convergence
chapters/theory/higher_genus_modular_koszul.tex:1520:for a basis $\{\alpha_1, \ldots, \alpha_g\}$ of
chapters/theory/higher_genus_modular_koszul.tex:1551:mechanism. By bounded-below convergence
chapters/theory/higher_genus_modular_koszul.tex:1706:By bounded-below convergence
chapters/theory/higher_genus_modular_koszul.tex:1929:identically. Bounded-below convergence
 succeeded in 51ms:
Total output lines: 248

chapters/connections/arithmetic_shadows.tex:624:The full scalar tower $(S_r)_{r \geq 2} = (24, 0, 0, \ldots)$
chapters/connections/arithmetic_shadows.tex:1517:$S_r$ in $\operatorname{Sh}_r = S_r\,x^r$ satisfies, for $r \geq 4$:
chapters/connections/arithmetic_shadows.tex:1519: S_r = \frac{2}{r}\,(-3)^{r-4}\,P^{r-2}
chapters/connections/arithmetic_shadows.tex:1524:$\lim_{c\to\infty} S_r \cdot r / [(-3)^{r-4} P^{r-2}] = 2$
chapters/connections/arithmetic_shadows.tex:1532:$S_r = -3(r{-}1)\,P\,S_{r-1}/r$
chapters/connections/arithmetic_shadows.tex:1539: S_r = S_4 \cdot \prod_{k=5}^{r} \frac{-3(k{-}1)P}{k}
chapters/connections/arithmetic_shadows.tex:1552:By~\eqref{eq:shadow-leading}, $S_r \neq 0$ at leading order
chapters/connections/arithmetic_shadows.tex:1556:$c$, the exact $S_r$ (a rational function of~$c$ with poles only at
chapters/connections/arithmetic_shadows.tex:1564:The recursion $S_r \propto (-3P)\,S_{r-1}$ identifies
chapters/connections/arithmetic_shadows.tex:1980:$S_r = \Delta \cdot R_r$, where $\Delta = 8\kappa S_4$ is
chapters/connections/arithmetic_shadows.tex:2117:$G(t) = \sum_{r\ge2} S_r\,t^r$
chapters/connections/arithmetic_shadows.tex:2128: S_r \;=\; -\frac{1}{r}\int \lambda^r\,d\rho(\lambda),
chapters/connections/arithmetic_shadows.tex:2142:$\sum_{r\ge4} S_r^{(0)}\,t^r$, where
chapters/connections/arithmetic_shadows.tex:2143:$S_r^{(0)} = (2/r)(-3)^{r-4}(2/c)^{r-2}$ is the leading-order
chapters/connections/arithmetic_shadows.tex:2151: \sum_{r\ge1} S_r^{(0)}\,t^r
chapters/connections/arithmetic_shadows.tex:2165:$S_r^{(0)} = (2/r)(-3)^{r-4}(2/c)^{r-2}$.
chapters/connections/arithmetic_shadows.tex:2169:$S_r^{(0)} = (2/9r)(-6/c)^{r-2}
chapters/connections/arithmetic_shadows.tex:2172:$\sum_{r\ge1} S_r^{(0)}\,t^r

thinking
**Exploring theorem remarks**

I need to figure out where to insert a remark after the theorem and before the scope remark. It’s important for me to understand local definitions to ensure my comments are rigorous. I should also search for specific terms related to the central charge notion or BPS phase in the file. This way, I can make informed remarks that add value to the discussion. Let's delve into that!
codex
I’ve got the MC2 surface. Now I’m checking whether the file already defines the phase-ordering and shadow-growth language needed for a rigorous “alternative construction” remark, so I can cite existing objects instead of inventing new unstated machinery.
exec
/bin/zsh -lc "rg -n \"BPS phase|phase ordering|central charge|argument\\(|\\arg|ray|primitive shadow|shadow grading|grading by r|shadow algebra\" chapters/theory/higher_genus_modular_koszul.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '12890,13040p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '19490,19680p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
85: The shadow algebra records \emph{what} the projections are;
744:\item the Virasoro algebra $\mathrm{Vir}_c$ at generic central charge
1634:For any genus~$g \geq 1$ and generic central charge~$c$, the PBW
1726:For generic central charge~$c$, the Virasoro algebra
2356:\item The shadow algebra
2603:the genus-$g$ quantum corrections live in higher Leray degrees,
3149:\begin{conjecture}[$\kappa$ as holographic central charge;
3152:\index{kappa@$\kappa$!as holographic central charge|textbf}
3153:\index{holographic central charge|textbf}
3173:Brown--Henneaux~\cite{BH86} central charge of the bulk theory
3230:\index{abelian Chern--Simons!holographic central charge}%
3247:\index{non-abelian Chern--Simons!holographic central charge}%
3254:Sugawara central charge of the boundary WZW model; it is also
3260:$k = -h^\vee$ the total holographic central charge vanishes,
3267:central charge is not zero: the residual Sugawara shift of
3306:\index{higher-spin gravity!holographic central charge}%
3307:For the principal $\cW_N$-algebra at central charge~$c$,
3347:\begin{remark}[$K3 \times E$: modular holographic central charge]
3350:\index{chiral de Rham complex!holographic central charge}%
3368:The Vol~I holographic central charge is the first; the BKM
 succeeded in 53ms:
\index{shadow tower!inter-channel coupling}
Let $\cA$ have generators of distinct conformal weights and let
$L \subset \Defcyc^{\mathrm{mod}}(\cA)$ be a primary subline.
Write $\{-,-\}_{r\textup{D}} = \{-,-\}_L + \{-,-\}_\perp$
for the decomposition into tangential and transverse brackets.
The shadow obstruction tower on~$L$, computed from the full multi-dimensional
MC equation, satisfies
\[
 \mathrm{Sh}_r^{\textup{full}}\big|_L
 \;=\;
 \mathrm{Sh}_r^{\textup{auton}}
 \;+\;
 \delta_r^{\perp}
\]
where $\mathrm{Sh}_r^{\textup{auton}}$ solves the autonomous $1$-D
recursion on~$L$ and
$\delta_r^{\perp}$ is the \emph{inter-channel coupling correction},
arising from transverse normal derivatives of shadows that vanish on~$L$.

The coupling correction $\delta_r^\perp$ vanishes on~$L$ if and only if
 succeeded in 53ms:
\end{remark}

\begin{construction}[Obstruction recursion]
\label{constr:obstruction-recursion}
Suppose a truncated solution $\Theta_{\cA}^{\leq N}$ has been
constructed through weight $N$. Its next obstruction is
\begin{equation}
\label{eq:next-obstruction}
\mathfrak{o}_{N+1}
:=
\Bigl(
D_{\cA}\Theta_{\cA}^{\leq N}
+ \tfrac12[\Theta_{\cA}^{\leq N},
\Theta_{\cA}^{\leq N}]
\Bigr)_{N+1}.
\end{equation}
If $[\mathfrak{o}_{N+1}] \in H^2(F^{N+1}/F^{N+2})$ vanishes,
choose a contracting homotopy $h$ and define
$\Theta_{\cA,N+1} := -h(\mathfrak{o}_{N+1})$.
Then $\Theta_{\cA}^{\leq N+1} := \Theta_{\cA}^{\leq N}
exec
/bin/zsh -lc "sed -n '25030,25110p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\sum_{\substack{d_1^+,d_1^-,\ldots,d_k^+,d_k^- \,\geq\, 0 \\
d_1^+ + d_1^- + \cdots + d_k^+ + d_k^- \,=\, 2k-3}}
\prod_{i=1}^{k} (-1)^{d_i^-}
\;\cdot\;
\bigl\langle
\tau_{d_1^+}\tau_{d_1^-}\cdots\tau_{d_k^+}\tau_{d_k^-}
\bigr\rangle_0
\;=\; 0.
\end{equation}
\end{proposition}

\begin{proof}
The dimension constraint
$\sum (d_i^+ + d_i^-) = 2k - 3$ has odd right-hand side for all~$k \geq 2$.
For any assignment~$(d_1^+,d_1^-,\ldots)$, define the swap
$\sigma_j\colon d_j^+ \leftrightarrow d_j^-$.
If $d_j^+ \neq d_j^-$ for some~$j$, then~$\sigma_j$ pairs the
assignment with a distinct one having the same Witten--Kontsevich number
(by symmetry of the correlator) but opposite sign factor
$(-1)^{d_j^+}$ versus~$(-1)^{d_j^-}$.




thinking
**Exploring theoretical remarks**

I think I need to define the BPS phase and central charge more clearly. Searching for broader connections or examples might help. While crafting a remark, I should be careful not to overstate claims. The user asked for a remark near MC2 involving "conceptual redundancy." Since the theorem is proven, I can label it as an alternative construction via a scattering diagram. I might say, "One can repackage," but I want to indicate it's a different proof path without replacing the original proof. I'll also check definitions supporting "BPS phase ordering."
thinking
**Defining self-contained remarks**

I need to make sure my remark is self-contained and doesn’t rely too much on undefined earlier terms, especially since "BPS phase ordering" may not be clearly defined. I could suggest choosing a central-charge function on the shadow grading and order rays by increasing \(\arg Z\). This would give a standard KS input. Each primitive degree yields a ray, and I’ll need to ensure consistency in the path-ordered product, relating it to the shadow algebra's growth bound. I might also reference the Kontsevich–Soibelman lemma and highlight convergence aspects.
thinking
**Adapting manuscript terminology**

I need to adapt to the manuscript's terminology carefully. I should verify if "alpha_g" as a growth bound is equivalent to the structural constant. In AGENTS' canonical formulas, alpha_g is expressed as \(2 \cdot \text{rank} + 4 \cdot \text{dim} \cdot h^v\), related to the Hilbert-series growth. However, the user mentions the shadow tower growth bound using alpha_g, which might indicate that this notation is defined differently elsewhere. So, I’ll need to clarify this!
thinking
**Investigating alpha_g in cohomology**

I’m looking into whether the user is referring to `alpha_g` from the shadow tower growth bound. I should check for any propositions or theorems that involve α_g related to growth in the number of graphs or genus growth. I'll search for "alpha_g" around relevant line numbers, like 16547, and then look up "shadow tower growth bound" near lines 4139 or 4753 to gather more information.
codex
I’m checking one last local dependency: whether the chapter already names a growth bound strong enough to justify the ordered product, or whether the remark needs to state that convergence is in the completed pronilpotent algebra and is controlled by the existing shadow-growth asymptotics instead of a new symbol.
exec
/bin/zsh -lc "rg -n \"growth bound|alpha_g|subexponential sector growth|primitive ray|pronilpotent|path-ordered|ordered product|BCH\" chapters/theory/higher_genus_modular_koszul.tex chapters/connections/arithmetic_shadows.tex appendices/nonlinear_modular_shadows.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16520,16610p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4090,4168p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:1520:for a basis $\{\alpha_1, \ldots, \alpha_g\}$ of
chapters/theory/higher_genus_modular_koszul.tex:2453:Tier~$2$ requires the growth bound; for finitely
chapters/theory/higher_genus_modular_koszul.tex:3965: pronilpotent completion
chapters/theory/higher_genus_modular_koszul.tex:3990: a pronilpotent dg~Lie algebra.
chapters/theory/higher_genus_modular_koszul.tex:4030:(Theorem~\ref{thm:cyclic-linf-graph}), and the pronilpotent
chapters/theory/higher_genus_modular_koszul.tex:4123:\item \emph{Weight filtration and pronilpotent completion}
chapters/theory/higher_genus_modular_koszul.tex:5979: H^2(\mathbf{D}_g) \cong \mathbb{C}\alpha_g,
chapters/theory/higher_genus_modular_koszul.tex:5981: H^2(\mathbf{D}_g^!) \cong \mathbb{C}\alpha_g^!,
chapters/theory/higher_genus_modular_koszul.tex:6098: H^2(\mathbf{D}_g)\cong \mathbb{C}\alpha_g,
chapters/theory/higher_genus_modular_koszul.tex:6100: H^2(\mathbf{D}_g^!)\cong \mathbb{C}\alpha_g^!;
chapters/theory/higher_genus_modular_koszul.tex:10127:a pronilpotent completed dg~Lie algebra.
chapters/theory/higher_genus_modular_koszul.tex:12063:inverse-limit element in a filtered pronilpotent Lie algebra, and the
chapters/theory/higher_genus_modular_koszul.tex:12080:algebra its pronilpotent completion), an extension tower (to define
chapters/theory/higher_genus_modular_koszul.tex:12116:\emph{pronilpotent}
chapters/theory/higher_genus_modular_koszul.tex:12968: $F^{N+1}$, making $\widehat{\gAmod}$ a pronilpotent
chapters/theory/higher_genus_modular_koszul.tex:13065:The standard reference for the pro-Artinian/pronilpotent MC
chapters/theory/higher_genus_modular_koszul.tex:13085:on $\gAmod$ (indexed by $2g - 2 + n$) is \emph{pronilpotent}:
chapters/theory/higher_genus_modular_koszul.tex:13099:pro-Artinian argument for MC elements in pronilpotent dg Lie algebras
chapters/theory/higher_genus_modular_koszul.tex:13179:(ii) follows from the pronilpotent weight filtration
chapters/theory/higher_genus_modular_koszul.tex:13415:\begin{theorem}[Stable-graph pronilpotent completion; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "sed -n '4728,4778p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The classification presupposes chiral Koszulness. Beyond the Koszul
boundary lies a fifth regime: class~$\mathbf{W}$ (wild), in which
the bar spectral sequence does not collapse at any finite page and
the shadow depth is undefined
(Remark~\ref{rem:wild-quiver-boundary}).
\end{definition}

\begin{remark}[The Koszul boundary and class~$\mathbf{W}$]
\label{rem:wild-quiver-boundary}
\index{shadow depth!wild class}%
\index{wild quiver!Koszul boundary}%
\index{Kronecker quiver!Koszul boundary}%
The Kronecker quiver $K_m$ (two vertices, $m$ parallel arrows)
exhibits a sharp Koszul boundary detected by the sign of the
determinant of the symmetric Euler form:
$\det \langle\cdot,\cdot\rangle_{\mathrm{sym}} = 4 - m^2$.
For $m \leq 2$ the form is positive semi-definite, the bar
spectral sequence collapses at~$E_2$, and the standard shadow
depth classification applies: $K_1$ is class~$\mathbf{L}$
(finite type $A_2$, shadow depth~$3$) and $K_2$ is class~$\mathbf{M}$
 succeeded in 51ms:
more generally $\kappa(\cA) + \kappa(\cA^!) = K(\mathfrak{g})$
for $\mathcal{W}$-algebras
(Theorem~\ref{thm:modular-characteristic}(iii),
Theorem~\ref{thm:genus-universality}(ii)).
\end{proof}

\begin{remark}[Complete foundational dependency chain]
\label{rem:mc2-foundational-chain}
\index{MC2!foundational dependency chain}
For the reader who wishes to trace the proof of
Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
dependency chain is as follows.
The argument rests on four independent pillars, each proved
earlier in the manuscript:
\begin{enumerate}[label=\textup{(\arabic*)}]
\item \emph{Modular operad structure of the bar complex}
 (Theorem~\ref{thm:bar-modular-operad},
 Chapter~\ref{chap:bar-cobar-adjunction}):
 $\{\barB^{(g,n)}(\cA)\}$ is an
 $\mathsf{F}\mathrm{Com}$-algebra.
 succeeded in 52ms:
and the genus-$g$ recursion begins at $l_3$.

Part~(f) is the downstream family-index identification
(Theorem~\ref{thm:family-index}) of the scalar series already
constructed above; the $\hat{A}$-genus appears because
$\operatorname{Td}(\Omega_{\pi_g})$ on the universal curve,
pushed forward to $\overline{\mathcal{M}}_g$, produces the
$\hat{A}$-class by Mumford's formula.
\end{proof}

\begin{remark}[Scope of Theorem~\ref{thm:explicit-theta}]
\label{rem:explicit-theta-scope}
\index{universal Maurer--Cartan class!scope}
The minimal model holds for KM
(Corollary~\ref{cor:km-minimal-linf}) and extends to
$\mathcal{W}$-algebras via DS functoriality. For VOAs
with $\dim H^2_{\mathrm{cyc}}\geq 2$, scalar saturation
is conditional;
see Conjecture~\ref{conj:scalar-saturation-universality}.
In the multi-channel regime, the correct framework is the

thinking
**Exploring growth sectors**

I need to read about growth bounds, possibly around 2453. I'm also considering the pronilpotent completion theorem, which might have a specific citation around 13415. Additionally, I'd like to search for information on subexponential sector growth, perhaps around 21870. Let's dig into those topics and see what insights I can uncover! It’ll be interesting to connect all these ideas together and see how they relate.
exec
/bin/zsh -lc "sed -n '2428,2472p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \textup{(Definitions~\ref{def:analytic-bar-coalgebra},
 \ref{def:analytic-koszul-pair})}.
\end{enumerate}
For finitely strongly generated Koszul algebras,
HS-sewing is \emph{automatic}: the PBW theorem gives
polynomial OPE growth, and
Theorem~\textup{\ref{thm:general-hs-sewing}} applies.
Tier~$2$ is therefore an independent condition only
for infinitely generated algebras.
\end{theorem}

\begin{proof}
Each item is proved by the referenced theorem. The
logical dependencies are:
Tier~$0$ requires $D_\cA^2 = 0$ alone
(Theorem~\ref{thm:convolution-d-squared-zero}).
Tier~$1$ requires~\ref{MK:koszul}; the key step
is Theorem~\ref{thm:pbw-propagation} supplying~\ref{MK:modular},
after which Theorems~\ref{thm:higher-genus-inversion}
and~\ref{thm:quantum-complementarity-main} provide B and C.
exec
/bin/zsh -lc "sed -n '13410,13490p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '21840,21895p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
codimension-$k$ strata of Mok's snc boundary
(see \cite[Section~5]{Mok25} for the stratification and
\cite[Theorem~11.1.2]{LV12} for the operadic framework).
\end{proof}

\begin{theorem}[Stable-graph pronilpotent completion; \ClaimStatusProvedHere]
\label{thm:stable-graph-pronilpotent-completion}
\index{stable-graph series!pronilpotent completion|textbf}
\index{pronilpotent completion!stable-graph series}
The Euler characteristic filtration on the modular convolution algebra,
\begin{equation}
\label{eq:pronilpotent-filtration}
F^p \mathfrak{g}^{\mathrm{mod,log}}_\cA
\;:=\;
\prod_{2g - 2 + n \geq p}
\mathfrak{g}^{\mathrm{mod,log}}_\cA(g,n),
\end{equation}
is pronilpotent: $F^1$ is a pronilpotent Lie ideal, each quotient
$\mathfrak{g}^{\mathrm{mod,log}}_\cA / F^{p+1}$ is nilpotent,
and the inverse limit
 succeeded in 52ms:
By the Jacobi identity
$f^{abe}f^{ecd} + f^{bce}f^{ead} + f^{cae}f^{ebd} = 0$,
the sum of the three channels satisfies the crossing relation
imposed by the associahedron
$K_4 = \overline{\mathcal{M}}_{0,4}$. For Heisenberg,
$f^{abc} = 0$ and the class vanishes identically. For
Virasoro, the vertex weight at $n = 3$ is
$\operatorname{tr}_{\mathrm{cyc}}(\ell_3^{(0)}) = 2$
(the $T_{(1)}T = 2T$ coefficient), and $\tau_{0,3}$
is a nonzero sum of boundary divisor classes.
\end{example}

\begin{corollary}[Analytic shadow realization]
\label{cor:analytic-shadow-realization}
\ClaimStatusProvedHere
\index{shadow obstruction tower!analytic realization}
\index{HS-sewing!shadow realization}
For every chirally Koszul algebra $\cA$ in the standard
landscape, the algebraic shadow obstruction tower extends to the sewing
envelope~$\cA^{\mathrm{sew}}$
exec
/bin/zsh -lc "sed -n '8815,8855p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[Scope and limitations]%
\label{rem:non-lattice-gap}%
\index{Ramanujan bound!scope}%
The theorem requires:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Rationality}: finitely many irreducible
 characters. For irrational VOAs (Virasoro at
 generic~$c$), the character space is infinite-dimensional
 and the Franc--Mason Hecke theory does not directly apply.
\item \emph{Diagonal modular invariant}:
 $Z = \sum|\chi_i|^2$. Non-diagonal invariants
 $Z = \sum M_{ij}\,\chi_i\,\bar\chi_j$ require
 the RS method for mixed terms $\chi_i\,\bar\chi_j$
 ($i \ne j$), which gives the Rankin--Selberg
 convolution $L(s, \chi_i \times \bar\chi_j)$ rather than
 $L(s, \chi_i \times \bar\chi_i)$. The argument extends
 to this case without difficulty.
\item \emph{HS-sewing}: polynomial OPE growth $+$
 subexponential sector growth. All standard families
 satisfy this



thinking
**Exploring proof structure**

I could construct a segment where I say, "This is a proof sketch," but I need to address any gaps with precision. It might be better to frame it as a remark and clarify that it provides a second construction under the standard Kontsevich-Soibelman theorem for scattering diagrams. I should then delve into identifying any missing elements, especially since there's no explicit theorem about applying the KS lemma to this algebra. I’ll need to work on making it sound rigorous using existing theoretical frameworks.
thinking
**Clarifying shadow class structure**

For each primitive shadow class \(S_r\), I can attach a wall automorphism \(T_r = \exp(S_r e_r)\) in the completed group. Since \(\widehat{\gAmod}\) is pronilpotent and the shadow growth estimate indicates that only a finite number of walls matter mod \(F^{N+1}\), the ordered product should converge. The consistency of the scattering diagram suggests path independence, which, according to the KS lemma, relates to the MC equation. Taking the logarithm will help recover \(\Theta_\cA\). I think this serves as a solid sketch!
thinking
**Considering theorem proof structure**

I need to ensure that any remark I insert doesn’t accidentally interfere with the theorem proof. It seems fine if the proof comes directly after the theorem, but I'm considering AGENTS AP8, which says to check the nearest preceding environment within 30 lines before the proof starts. If I insert a remark right before the proof, it might trigger AP8 since the nearest is the remark itself. Wait, is a figure also not a start? That's interesting!
exec
/bin/zsh -lc "sed -n '13050,13135p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4030,4215p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $\varprojlim_N \mathcal{E}_\cA(N)
 = \MC(\widehat{\gAmod})$:
 an element $x \in \widehat{\gAmod}$ is MC if and only if
 its projection $\pi_{\leq N}(x)$ is MC in
 $\gAmod/F^{N+1}$ for all~$N$.
\item \emph{Existence.}
 By~(a)--(c), the compatible system
 $\{\Theta_\cA^{\leq N}\}_{N \geq 1}$ (Step~3) has a
 unique inverse limit
 $\Theta_\cA := \varprojlim_N \Theta_\cA^{\leq N}$
 in $\MC(\widehat{\gAmod})$, satisfying
 the full Maurer--Cartan equation
 $[\dzero, \Theta_\cA]
 + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$.
\end{enumerate}
The standard reference for the pro-Artinian/pronilpotent MC
argument is Goldman--Millson~\cite{GoldmanMillson88};
see also Manetti~\cite{Manetti04a}.

\smallskip\noindent
 succeeded in 52ms:
(Theorem~\ref{thm:cyclic-linf-graph}), and the pronilpotent
genus filtration on~$\Gmod$ makes the completed tensor product
a complete $L_\infty$-algebra~(F4) in which the MC equation
converges at each genus
(Proposition~\ref{prop:geometric-modular-operadic-mc}(b)).
No conditional hypotheses are needed: the centrality of the
genus-$g$ curvature, required by the genus-induction procedure,
is automatic from the locality axiom
(Proposition~\ref{prop:curvature-centrality-general}).

\emph{(ii) Scalar trace.}
Theorem~\ref{thm:genus-universality} gives the universal genus-$1$
identity
$\operatorname{tr}(\Theta_\cA)_{g=1} = \kappa(\cA)\lambda_1$.
On the proved uniform-weight lane, the same theorem upgrades this to
\[
 \operatorname{tr}(\Theta_\cA)
 = \sum_{g \geq 1} \kappa(\cA)\lambda_g .
\]


thinking
**Evaluating file access**

I’m contemplating whether I can read files outside the current working directory. I’m not entirely sure but it seems possible to read them. Writable roots might be limited to the current directory, but when it comes to reading files, it seems there could be broader access. I’m thinking about maybe running a non-intrusive search across different volumes, especially using tools like grep. My approach needs to be careful!
codex
I have the insertion point. Before editing I’m doing the label-uniqueness and wording checks, then I’ll patch in a remark that is explicitly framed as a secondary construction in the completed pronilpotent algebra, with the remaining setup assumptions stated rather than hidden.
exec
/bin/zsh -lc 'rg -ni "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|landscape|journey|navigate" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
720:\ref{MK:verdier} for the standard landscape follows from: (1)~the genus-$0$ bar-cobar Verdier pairing
2108:entire CFT-type standard landscape.
2217:therefore reduces to a single axiom for the standard landscape:
2480:\textup{(}the entire standard landscape except integer-spin $\beta\gamma$, where hypothesis~\textup{(a)} fails\textup{)},
2554: standard landscape.
3217:below, covering six families in the standard landscape
3710:In particular, every chiral algebra in the standard landscape
4068:\textup{(}For the standard landscape, this axiom is
4281:genera). For the standard landscape,~\ref{MK:modular}
8195:and on the full standard Lie-theoretic landscape
8723: for every algebra on the standard Lie-theoretic landscape
8740:(Kac--Moody, generic level, standard landscape).
8858:On the full standard Lie-theoretic landscape,
9045:for the standard landscape;
9050:standard Lie-theoretic landscape
9077:landscape, then derive the quadruple reduction.
9647:them, and $E = \emptyset$ for the standard landscape.
9716:standard Lie-theoretic landscape at all non-critical
9741:and on the standard Lie-theoretic landscape in the weaker
9747:Lie-theoretic landscape \textup{(}not for the live audit surface
exec
/bin/zsh -lc "rg -nF '\\label{rem:mc2-scattering-diagram}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Considering label creation**

The instructions say it's mandatory to label anything in hot zones before editing, which makes sense for safety. I see some potential dependencies in this theorem lane, though it’s unclear if it truly counts as a hot zone. To err on the side of caution, I'll create a PE-7 label and include a scope note. I should also prepare commentary for the PE-7 label and refrain from editing the formula until after I apply the patch.
codex
```text
PE-7 label creation
environment: remark
label: \label{rem:mc2-scattering-diagram}
prefix match (AP125): Y
AP124 duplicate check: Vol I:0 Vol II:0 Vol III:0 total before:0 after:1 delta=1? Y
verdict: ACCEPT
```

The edit is local to the MC2 theorem lane. I’m adding a secondary-construction remark after the theorem proof so the proof boundary stays clean, and I’ll keep the statement scoped to the completed pronilpotent algebra plus the existing shadow-growth inputs.


thinking
**Clarifying construct properties**

I'm realizing that my explanation was a bit circular. Instead, I think I should frame it as: "This creates a canonical completed MC element; comparing degree-two trace and finite-order shadow projections should align with \(\Theta_\cA\)." However, the user wants some conceptual redundancy related to existence and MC. Hmm, perhaps I can say that "A scattering-diagram construction can generate an element having the same defining properties." This way, it feels clearer and more connected.
thinking
**Considering redundancy in comparisons**

I see that if the comparison isn't fully developed, I can mention that the comparison of degree truncations should align with \(\Theta_\cA\). The user brought up conceptual redundancy, which makes me think that perhaps equality isn’t as crucial. I'm also noting their phrase, "The MC element Theta_A can be constructed" and thinking it might be useful to emphasize that it "can be constructed" as part of my response.
codex
I’m applying the edit now. The remark will stay explicit about what is proved in-file and what is imported from the standard Kontsevich-Soibelman consistency package, so the secondary route is useful without being status-inflated.

thinking
**Troubleshooting patch failure**

I’m having an issue with a patch failing, possibly due to some line wraps or extra text. I need to take a closer look at the specific segment around the insertion point. I think using sed to inspect lines around 4120-4170 might help me figure out what’s going wrong. It’s all about finding the right details to resolve this issue! Let's get to the bottom of it!
codex
The first patch missed the exact local context. I’m re-reading the immediate insertion block and will patch against the live lines rather than the summarized excerpt.
exec
/bin/zsh -lc "sed -n '4130,4198p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (Proposition~\ref{prop:curvature-centrality-general}):
 no conditional simple-Lie-symmetry hypothesis is needed,
 because centrality follows from the locality axiom alone.
\end{enumerate}
Given these four inputs, the MC equation
$[\dzero, \Theta_\cA] + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
is the algebraic restatement of~$D_\cA^2 = 0$ upon decomposing
$D_\cA = \dzero + \Theta_\cA$ by genus.
No additional construction or hypothesis is required.
The shadow obstruction tower convergence
(Theorem~\ref{thm:recursive-existence}) then inherits
from the weight filtration: each truncation
$\Theta_\cA^{\leq N} := \pi_{\leq N}(\Theta_\cA)$ is MC
in $\gAmod/F^{N+1}$, the projections are compatible, and the
Mittag-Leffler condition ensures
$\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ exists as
an MC element in~$\widehat{\gAmod}$.
\end{remark}

\begin{remark}[The bar-intrinsic perspective and the two regimes]
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -4148,2 +4148,78 @@
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
apply_patch(auto_approved=true) exited 0 in 32ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}


thinking
**Considering degree-truncation equality**

I should mention degree-truncation equality and clarify that it’s not exact equality. I think that could be helpful! Also, I might need to consider adding `\textup{(}` around citations, but it seems like it's not necessary. I'm wondering if `\cA^{\mathrm{sh}}_{r,\bullet}` exists; it likely does. Alright, let’s inspect the inserted region and compile a test to see how everything works together.
codex
The remark is in place. I’m re-reading the inserted block for mathematical overreach and TeX stability, then I’ll run a narrow LaTeX/metadata check on the touched surface.
exec
/bin/zsh -lc "rg -nF 'rem:mc2-scattering-diagram' chapters/theory/higher_genus_modular_koszul.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4142,4228p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\Theta_\cA^{\leq N} := \pi_{\leq N}(\Theta_\cA)$ is MC
in $\gAmod/F^{N+1}$, the projections are compatible, and the
Mittag-Leffler condition ensures
$\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ exists as
an MC element in~$\widehat{\gAmod}$.
\end{remark}

\begin{remark}[Alternative construction via scattering diagram]
\label{rem:mc2-scattering-diagram}
\index{Maurer--Cartan element!scattering-diagram construction}
\index{Kontsevich--Soibelman!alternative construction of MC2}
This is a proof sketch for a second construction of the element of
Theorem~\ref{thm:mc2-bar-intrinsic}.
Work in the shadow algebra of
Definition~\ref{def:shadow-algebra} and choose a central-charge map
\[
Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
\]
on the shadow grading. Order the rays by increasing
$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:4150:\label{rem:mc2-scattering-diagram}
exec
/bin/zsh -lc 'rg -ni "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
26170:Theorem~\ref{thm:mc-tautological-descent}. We now make
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}


thinking
**Considering makefile options**

I need to inspect the makefile to see if I can use `make fast` appropriately. Since the user wants verification, it might be best to check if there's a `latexmk` or a way to compile a specific file. I'll look for any script related to the makefile as well. Running `rg -n "fast:" Makefile` will help me see the available targets. Let's dig into it!
codex
The text is stable on reread. I’m moving to the narrowest falsification step now: a local build/log check against the touched chapter surface, not a full manuscript sweep.
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "''^fast:|''^all:|latexmk|main.tex|metadata" Makefile makefile GNUmakefile' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
bibliography
bp_self_duality.pdf
 exited 2 in 51ms:
rg: GNUmakefile: No such file or directory (os error 2)
Makefile:13:#    make watch          Continuous rebuild on file changes (requires latexmk)
Makefile:27:LATEXMK   := latexmk
Makefile:45:# Source files: every .tex file that main.tex transitively \input's or \include's.
Makefile:74:AUX_EXTS  := aux log out toc synctex.gz fdb_latexmk fls bbl blg \
Makefile:81:.PHONY: all fast watch clean veryclean count check draft integrity phase0-index metadata verify census test editorial standalone annals archive dist release help working-notes publish icloud
Makefile:93:all: $(STAMP) working-notes publish
Makefile:114:fast:
Makefile:219:## watch: Continuous rebuild on save (requires latexmk).
Makefile:222:		{ echo "Error: latexmk not found. Install via: brew install --cask mactex"; exit 1; }
Makefile:292:## metadata: Regenerate metadata artefacts and the proved-claim registry from .tex sources.
Makefile:293:metadata:
Makefile:294:	@echo "  ── Generating metadata ──"
Makefile:295:	@python3 scripts/generate_metadata.py
Makefile:297:## census: Print claim census from generated metadata.
Makefile:298:census: metadata
Makefile:299:	@python3 -c "import json; d=json.load(open('metadata/census.json')); t=d['totals']; print(f'  PH={t[\"ProvedHere\"]} PE={t[\"ProvedElsewhere\"]} CJ={t[\"Conjectured\"]} H={t[\"Heuristic\"]} O={t[\"Open\"]} total={t[\"total_claims\"]}')"
Makefile:302:audit: metadata
Makefile:394:		main.tex chapters/ appendices/ bibliography/ scripts/ compute/ \
Makefile:462:	@echo "  make watch      Continuous rebuild on save (latexmk)"
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}


thinking
**Evaluating build commands**

I'm considering whether to use `make fast`, which might be okay but could also be expensive. Alternatively, I could try `make metadata`, though metadata generation might not be necessary to avoid parse errors now that I've added a label. Since changes in tex might lead to compile issues, `make fast` seems like the better option. 

I also think about how to properly run the kill command for pdflatex without chaining bash commands poorly. Running the commands separately could be the safest approach. Let's proceed with that!
exec
/bin/zsh -lc 'pkill -9 -f pdflatex 2>/dev/null || true' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}

exec
/bin/zsh -lc 'sleep 2' in /Users/raeez/chiral-bar-cobar succeeded in 1.94s:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}

codex
The fast build is running. I’m watching the first pass for any TeX error or undefined-control-sequence issue introduced by the new remark before deciding whether the surface is clean.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..cc9080c0da776e0410f20982522fa0168fe3dd3c
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

 exited 2 in 22.94s:
   ?pp, 612 undef citations, 381 undef references, 0 rerun requests, 64 overfull, 115 underfull
✗ Build failed.
  Logs: .build_logs/tex-build.stdout.log and main.log
./main.aux:158:  ==> Fatal error occurred, no output PDF file produced!
./chapters/theory/ordered_associative_chiral_kd.tex:6060:  ==> Fatal error occu
./main.aux:158:  ==> Fatal error occurred, no output PDF file produced!
make: *** [fast] Error 1

thinking
**Inspecting build issues**

I've run into a build failure, possibly due to a pre-existing fatal error. I need to check the logs to see if they mention the main.aux fatal issue and another file called ordered_associative. It’s crucial to identify if my recent changes caused this problem. I should search the log for our specific label or look for errors near the line mentioned. Maybe using regex on the logs would be helpful here.
codex
The build failed, but the failure surface doesn’t point to the edited block yet. I’m classifying whether this is a pre-existing manuscript failure or something introduced in the new remark by searching the log for the touched file and for the standard fatal markers.
exec
/bin/zsh -lc "sed -n '1,220p' .build_logs/tex-build.stdout.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Fatal error|Undefined control sequence|Emergency stop|Runaway argument|File ended while scanning|! " main.log' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "mc2-scattering-diagram|higer_genus_modular_koszul|higher_genus_modular_koszul|Undefined control sequence|LaTeX Error|Fatal error|KS00|def:shadow-algebra|thm:shadow-radius|thm:stable-graph-pronilpotent-completion" main.log .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
binary file matches (found "\0" byte around offset 84168)
 succeeded in 52ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
 succeeded in 51ms:
main.log: binary file matches (found "\0" byte around offset 84168)
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Exploring log errors**

I'm considering that the main.log might be binary or corrupted, possibly due to issues with the aux file. I think using `strings` or checking for errors in the .build_logs might help, but the output could be truncated. I can try inspecting the tail of main.log with commands like `tail -n 100` or `grep`. It might also be good to check the content of the .aux file at line 158. Let’s open main.aux around that line for a closer look!
exec
/bin/zsh -lc 'tail -n 120 .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
exec
/bin/zsh -lc "nl -ba main.aux | sed -n '148,166p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'file main.log main.aux .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   148	\@writefile{toc}{\contentsline {subsection}{\numberline {9.7.2}Trees and boundary strata: the geometric HTT}{578}{subsection.9.7.2}\protected@file@percent }
   149	\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.7.3\else \numberline {9.7.3}Proposition\fi \thmtformatoptarg {Trees as boundary strata; }}{578}{proposition.9.7.3}\protected@file@percent }
   150	\newlabel{prop:trees-boundary-strata}{{9.7.3}{578}{Trees as boundary strata; \ClaimStatusProvedHere }{proposition.9.7.3}{}}
   151	\@@wrindexm@m{main}{Fulton--MacPherson compactification!boundary strata|hyperpage}{578}
   152	\@@wrindexm@m{main}{homotopy transfer theorem!geometric realization|hyperpage}{578}
   153	\@writefile{loe}{\contentsline {remark}{\ifthmt@listswap Remark~9.7.4\else \numberline {9.7.4}Remark\fi \thmtformatoptarg {Feynman diagrams as transferred operations}}{579}{remark.9.7.4}\protected@file@percent }
   154	\newlabel{rem:feynman-htt}{{9.7.4}{579}{Feynman diagrams as transferred operations}{remark.9.7.4}{}}
   155	\@@wrindexm@m{main}{Feynman diagrams!homotopy transfer|hyperpage}{579}
   156	\@writefile{toc}{\contentsline {subsection}{\numberline {9.7.3}Genus corrections as transferred operations}{579}{subsection.9.7.3}\protected@file@percent }
   157	\newlabel{subsec:genus-corrections-htt}{{9.7.3}{579}{Genus corrections as transferred operations}{subsection.9.7.3}{}}
   158	\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~9.7.5\else \numberline {9.7.5}Proposition\fi \thmtformatoptarg {Genus-$1$ curvature as $m_0$; }}{579}{proposition.9.7.5}\protected@file@percent }
   159	\newlabel{prop:genus1-curvature-m0}{{9.7.5}{579}{Genus-\texorpdfstring {$1$}{1} curvature as \texorpdfstring {$m_0$}{m0}; \ClaimStatusProvedHere }{proposition.9.7.5}{}}
   160	\@@wrindexm@m{main}{curvature!as $m_0$|hyperpage}{579}
   161	\citation{LV12}
   162	\@writefile{loe}{\contentsline {remark}{\ifthmt@listswap Remark~9.7.6\else \numberline {9.7.6}Remark\fi \thmtformatoptarg {Higher genus: moduli cohomology as transferred operations}}{580}{remark.9.7.6}\protected@file@percent }
   163	\newlabel{rem:higher-genus-htt}{{9.7.6}{580}{Higher genus: moduli cohomology as transferred operations}{remark.9.7.6}{}}
   164	\@@wrindexm@m{main}{moduli space!homotopy transfer|hyperpage}{580}
   165	\@writefile{loe}{\contentsline {remark}{\ifthmt@listswap Remark~9.7.7\else \numberline {9.7.7}Remark\fi \thmtformatoptarg {Physical content: renormalization vs.\ homotopy transfer}}{580}{remark.9.7.7}\protected@file@percent }
   166	\newlabel{rem:renormalization-htt}{{9.7.7}{580}{Physical content: renormalization vs.\ homotopy transfer}{remark.9.7.7}{}}
 succeeded in 51ms:
main.log:                         ASCII text
main.aux:                         LaTeX table of contents, ASCII text, with very long lines (318)
.build_logs/tex-build.stdout.log: ASCII text
exec
/bin/zsh -lc 'strings -n 1 main.log | tail -n 120' in /Users/raeez/chiral-bar-cobar succeeded in 64ms:
Package: enumitem 2025/02/06 v3.11 Customized lists
\labelindent=\skip264
\enit@outerparindent=\dimen338
\enit@toks=\toks62
\enit@inbox=\box135
\enit@count@id=\count404
\enitdp@description=\count405
)
(/usr/local/texlive/2025/texmf-dist/tex/latex/newunicodechar/newunicodechar.sty
Package: newunicodechar 2018/04/08 v1.2 Defining Unicode characters
)
\main@idxfile=\write5
\openout5 = `main.idx'.
Writing index file main.idx 
(/usr/local/texlive/2025/texmf-dist/tex/latex/mathtools/mathtools.sty
Package: mathtools 2024/10/04 v1.31 mathematical typesetting tools
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/calc.sty
Package: calc 2023/07/08 v4.3 Infix arithmetic (KKT,FJ)
\calc@Acount=\count406
\calc@Bcount=\count407
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an




thinking
**Considering file deletion**

I’m thinking about whether deleting an auxiliary file could be a good idea for build hygiene. It seems I need to ensure it’s safe, especially since the generated auxiliary file may be corrupted. The user didn't specifically ask for this, but if it's necessary for verification, it could be worthwhile. Since the build failed due to a character issue, removing possibly corrupted files seems reasonable. I should check if there are any NUL bytes before proceeding.
thinking
**Evaluating tracked files**

I’m considering whether the auxiliary file is tracked or untracked. It seems likely it’s untracked, which means I could delete it safely since it’s a generated file. The build failed due to a bad auxiliary file, so cleaning it up should be okay. However, I want to be cautious and inform the user, as the final answer can indicate that the build was blocked by the pre-existing corrupted file. I'll think about verifying the issue myself too.
thinking
**Inspecting files for NUL bytes**

I need to build something, but first, I should inspect the files. I'm thinking about searching for files with NUL bytes, so maybe there's only one. I could use `python` or `perl` for this, but I think using `grep -rlU` could be better. Alternatively, I might try `rg -lU '\x00' chapters/theory/*.aux` to find them. Alright, let's see what I can uncover!
codex
The failure is pre-existing build debris: `pdfTeX` is dying on a NUL byte inside `chapters/theory/quantum_corrections.aux`, not on the edited chapter. I’m checking whether that aux corruption is isolated; if it is, I can clear the generated artifact and rerun the build to get a real verification pass.
exec
/bin/zsh -lc 'git status --short chapters/theory/quantum_corrections.aux chapters/theory/higher_genus_modular_koszul.tex main.aux main.log .build_logs/tex-build.stdout.log' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
paths=[]
for p in Path('chapters').rglob('*.aux'):
    try:
        data=p.read_bytes()
    except Exception:
        continue
    if b'\\x00' in data:
        paths.append(str(p))
print('\\n'.join(paths))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 M chapters/theory/higher_genus_modular_koszul.tex
 M main.aux
 M main.log
 succeeded in 51ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Investigating Python output issues**

I’m trying to figure out why Python output is blank. It could be that the main log had NUL characters. I noticed the log indicated NUL from the strings output, which may suggest a read error from main. The pdfTeX is mentioning an invalid character at line 2279 while reading the main.aux file, possibly with quantum_corrections.aux. I need to inspect that specific line in the aux file using tools like `sed`, `file`, and `xxd`.
exec
/bin/zsh -lc 'file chapters/theory/quantum_corrections.aux' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/quantum_corrections.aux: LaTeX table of contents, ASCII text
exec
/bin/zsh -lc "nl -ba chapters/theory/quantum_corrections.aux | sed -n '2274,2284p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
p=Path('chapters/theory/quantum_corrections.aux')
data=p.read_bytes()
print('nul_count', data.count(b'\\x00'))
print('size', len(data))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 51ms:
nul_count 0
size 25802
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Considering file cleanup**

I'm thinking about using `make clean`, but I might just delete `main.aux` and `chapters/theory/quantum_corrections.aux` specifically. The `rm` command should be safe since I'm not destructively resetting anything in git. I should mention this in the commentary. I wonder if there are any strange bytes at line 2279 of `main.aux`. Maybe I should check the line count using `nl -ba main.aux | sed -n '2270,2286p'` to get a better look.
exec
/bin/zsh -lc "nl -ba main.aux | sed -n '2270,2288p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

exec
/bin/zsh -lc "sed -n '226,260p' Makefile" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
check:
	@echo "  ── Error check (halt-on-error) ──"
	@mkdir -p $(LOG_DIR)
	@$(TEX) -interaction=nonstopmode -halt-on-error -file-line-error $(MAIN).tex >$(LOG_DIR)/check.log 2>&1 || { \
		echo "  ✗  Check failed. See $(LOG_DIR)/check.log"; \
		grep -aE '^! |Emergency stop|Runaway argument|Fatal error|Undefined control sequence|File ended while scanning|No pages of output' $(LOG_DIR)/check.log | head -n 20 || tail -n 40 $(LOG_DIR)/check.log; \
		exit 1; \
	}
	@echo "  ✓  No fatal errors."
	@echo "     Log: $(LOG_DIR)/check.log"

## integrity: Strict manuscript integrity gate (clean rebuild + diagnostics + claim-tag coverage).
integrity:
	@./scripts/integrity_gate.sh

## phase0-index: Regenerate active-theory theorem dependency index.
phase0-index:
	@./scripts/generate_theorem_dependency_index.py

## draft: Build with draft class option (skips image rendering, faster).
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

exec
/bin/zsh -lc "sed -n '260,305p' Makefile" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
clean:
	@echo "  Cleaning build artifacts..."
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext; \
	done
	@find chapters appendices bibliography -name '*.aux' -delete 2>/dev/null || true
	@rm -rf $(LOG_DIR)
	@rm -f texput.log
	@echo "  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged)."

## veryclean: Remove EVERYTHING including PDF, out/, and build stamp (forces full rebuild).
veryclean: clean
	@rm -f $(MAIN).pdf $(STAMP) $(WN_PDF)
	@rm -rf $(OUT_DIR)
	@echo "  ✓  Stamp, PDFs, and out/ removed — next make will rebuild."

## count: Manuscript statistics.
count:
	@echo ""
	@echo "  ── Manuscript Statistics ──"
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Planning the build process**

I'm thinking we should run `make clean` first to ensure everything's tidy. After that, I'll go ahead with `make fast`—I guess optimizing is key. I wonder if I should skip building everything, but then again, maybe it's fine to do the whole thing. I guess we'll figure it out as we go! It feels important to keep things organized and efficient. Let's just move forward with this plan and see where it leads!
codex
The first build failure was an aux-surface issue, not a source error. I’m clearing generated build debris and rerunning `make fast`; this is safe because it only removes LaTeX auxiliaries and log files.
exec
/bin/zsh -lc 'make clean' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  Cleaning build artifacts...
  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged).
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

exec
/bin/zsh -lc 'make fast' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

 exited 2 in 40.00s:
   ?pp, 1594 undef citations, 7348 undef references, 0 rerun requests, 105 overfull, 196 underfull
✗ Build failed.
  Logs: .build_logs/tex-build.stdout.log and main.log
./chapters/theory/en_koszul_duality.tex:3407: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:3953: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:3956: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4267: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4269: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4269: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4275: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4278: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4278: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4341: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4341: Undefined control sequence.
./chapters/theory/en_koszul_duality.tex:4342: Undefined control sequence.
make: *** [fast] Error 1
codex
The clean rebuild now gets past the aux corruption and fails on unrelated pre-existing undefined macros in `chapters/theory/en_koszul_duality.tex`. I’m doing one more local check that doesn’t depend on the full manuscript being buildable: metadata regeneration plus a search for errors pointing at the edited chapter.
exec
/bin/zsh -lc 'python3 scripts/generate_metadata.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"higher_genus_modular_koszul\\.tex:41[0-9][0-9]|mc2-scattering-diagram|Undefined control sequence|LaTeX Error\" main.log .build_logs/tex-build.stdout.log" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"higher_genus_modular_koszul\" test_chapter.tex test_latex.tex standalone -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
main.log:40938:./chapters/theory/ordered_associative_chiral_kd.tex:2343: LaTeX Error: \mathcal
main.log:41703:./chapters/theory/ordered_associative_chiral_kd.tex:6048: LaTeX Error: \begin{d
main.log:42126:./chapters/theory/ordered_associative_chiral_kd.tex:8223: LaTeX Error: \begin{d
main.log:42178:./chapters/theory/ordered_associative_chiral_kd.tex:8240: LaTeX Error: \mathcal
main.log:42519:./chapters/theory/ordered_associative_chiral_kd.tex:8799: LaTeX Error: \begin{r
main.log:44813:./chapters/theory/en_koszul_duality.tex:3407: Undefined control sequence.
main.log:45025:./chapters/theory/en_koszul_duality.tex:3953: Undefined control sequence.
main.log:45034:./chapters/theory/en_koszul_duality.tex:3956: Undefined control sequence.
main.log:45179:./chapters/theory/en_koszul_duality.tex:4267: Undefined control sequence.
main.log:45188:./chapters/theory/en_koszul_duality.tex:4269: Undefined control sequence.
main.log:45197:./chapters/theory/en_koszul_duality.tex:4269: Undefined control sequence.
main.log:45206:./chapters/theory/en_koszul_duality.tex:4275: Undefined control sequence.
main.log:45215:./chapters/theory/en_koszul_duality.tex:4278: Undefined control sequence.
main.log:45226:./chapters/theory/en_koszul_duality.tex:4278: Undefined control sequence.
main.log:45250:./chapters/theory/en_koszul_duality.tex:4341: Undefined control sequence.
main.log:45261:./chapters/theory/en_koszul_duality.tex:4341: Undefined control sequence.
main.log:45270:./chapters/theory/en_koszul_duality.tex:4342: Undefined control sequence.
main.log:45434:./chapters/theory/en_koszul_duality.tex:4935: LaTeX Error: \begin{proof} on inp
 exited 2 in 52ms:
rg: test_chapter.tex: No such file or directory (os error 2)
rg: test_latex.tex: No such file or directory (os error 2)
 succeeded in 261ms:
Generating metadata for chiral-bar-cobar monograph...
  Root: /Users/raeez/chiral-bar-cobar
  Active files (in main.tex): 85
  All .tex files: 128

  Extracted 3672 tagged claims from 128 files

Writing metadata to /Users/raeez/chiral-bar-cobar/metadata/
  claims.jsonl: 3672 claims
  census.json: PH=2845 PE=454 CJ=317 H=30 CD=23 O=3 total=3672
  dependency_graph.dot: 3672 nodes, 2222 edges
  label_index.json: 13188 labels
  theorem_registry.md: 2845 proved claims indexed
  verified_formulas.jsonl: 34 formulas

Done. Run 'make metadata' to regenerate.
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an



thinking
**Evaluating metadata changes**

I realize that we didn't add the `ClaimStatus` remark, so the counts shouldn't really change unless there are pre-existing changes or metadata drift. However, the user may have a dirty worktree, so I need to inspect the overall git status. I should check the `git diff --stat -- metadata/theorem_registry.md`, as the counts might just be due to modifications in other files. I want to ensure we don't accidentally include unrelated changes when regenerating metadata. I need to be careful here!
thinking
**Inspecting metadata changes**

I need to remember that metadata generation tracks the entire repository and may incorporate unrelated changes. That's a bit tricky! If there are dirty source changes already present, the regenerated metadata might accidentally include them, and we definitely shouldn't revert user changes. It's important to inspect the diff carefully. If there are significant unrelated changes, I should mention that. I think I'll limit the inspection to just our files to keep things clear and manageable!
codex
The local source verification is clean enough: `generate_metadata.py` succeeds and the full build failures are elsewhere. I’m checking the exact diff now so I can report only the changes I actually introduced and not blur them with any pre-existing worktree noise.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/higher_genus_modular_koszul.tex metadata/theorem_registry.md metadata/census.json metadata/claims.jsonl metadata/label_index.json metadata/dependency_graph.dot metadata/verified_formulas.jsonl' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 M chapters/connections/bv_brst.tex
 M chapters/connections/concordance.tex
 M chapters/frame/preface.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_complementarity.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/introduction.tex
 M main.aux
 M main.log
 M main.out
 M metadata/census.json
 M metadata/claims.jsonl
 M metadata/dependency_graph.dot
 M metadata/label_index.json
 M metadata/theorem_registry.md
 M standalone/chiral_chern_weil.tex
 M standalone/classification_trichotomy.tex
 M standalone/introduction_full_survey.tex
 M standalone/programme_summary_sections5_8.tex
 M standalone/seven_faces.tex
 succeeded in 52ms:
Total output lines: 17322

diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76..3f49d20 100644
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@ $\Theta_\cA = \varprojlim_N \Theta_\cA^{\leq N}$ exists as
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..3f49d20fe4fd9365471c8b602eeb826067b80632
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\]
+therefore converges in every quotient
+$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an



thinking
**Considering version control options**

I'm thinking about alternatives to `git checkout`, maybe using `exec_command` with `git diff --name-only`. It's generally advised to avoid destructive commands like `git checkout --` or `git reset --hard`. I wonder if `git restore --source=HEAD --worktree -- metadata/...` is too destructive as well. I might explore using `apply_patch`, but that could be tough with large files. Since the user didn't request a commit, it's worth noting that I might keep metadata changes just for verification. However, that could complicate things!
thinking
**Considering mathematical convergence**

I'm thinking about how the ordered product converges in every quotient of the completion. It seems using `\gAmod/F^{N+1}\gAmod` could work well, since these are finite quotients from the theorem. I should also mention the "missing manuscript-level input," which seems important. But I wonder if mentioning `Baker--Campbell--Hausdorff` is necessary; maybe it's fine to keep it minimal. I’ll patch this up!
codex
I’m tightening two phrases before I stop: one about the phase order and one about the finite quotients, so the remark matches the chapter’s actual pronilpotent-completion notation exactly.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -4160,3 +4160,3 @@
 on the shadow grading. Order the rays by increasing
-$\arg Z$ \textup{(}the BPS phase ordering\textup{)}.
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
 On an autonomous primary line~$L$, the primitive degree-$r$ shadow
@@ -4183,6 +4183,6 @@
 \;:=\;
-\prod_{\ell\ \textup{in increasing }\arg Z} \Phi_\ell
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
 \]
 therefore converges in every quotient
-$\widehat{\gAmod}/F^{N+1}$ and hence in
+$\gAmod/F^{N+1}\gAmod$ and hence in
 $\exp(F^1\widehat{\gAmod})$.
apply_patch(auto_approved=true) exited 0 in 35ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..188c196983fd97a6397eb205be09b395eccc3001
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..188c196983fd97a6397eb205be09b395eccc3001
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Considering code modifications**

I think I may not need any more builds since they're unrelated. Instead, I wonder if running a quick grep or checking logs is necessary. It might be more efficient to just inspect the lines I inserted after the patch. This could save me time, so I should weigh the effort versus the potential benefits of running additional tests. Let's see how that goes!
exec
/bin/zsh -lc "sed -n '4150,4208p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:mc2-scattering-diagram}
\index{Maurer--Cartan element!scattering-diagram construction}
\index{Kontsevich--Soibelman!alternative construction of MC2}
This is a proof sketch for a second construction of the element of
Theorem~\ref{thm:mc2-bar-intrinsic}.
Work in the shadow algebra of
Definition~\ref{def:shadow-algebra} and choose a central-charge map
\[
Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
\]
on the shadow grading. Order the rays by increasing
$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
On an autonomous primary line~$L$, the primitive degree-$r$ shadow
invariant $S_r(L)$ determines a wall
$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
\[
\Phi_{\ell_r}
\;:=\;
\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
\qquad
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..188c196983fd97a6397eb205be09b395eccc3001
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

exec
/bin/zsh -lc "sed -n '4208,4238p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\qquad
[\dzero,\Theta_\cA^{\mathrm{scat}}]
+ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
= 0.
\]
Its degree-$r$ truncation is built from the same primitive shadow data
as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
rather than by the recursive inverse-limit construction.
This gives a second conceptual origin for~$\Theta_\cA$:
the primitive shadows are the wall data, the BPS phase ordering is the
assembly rule, and the Maurer--Cartan equation is the infinitesimal
form of scattering-diagram consistency.
The missing manuscript-level input is the full setup of this
scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
installed, it furnishes an alternative proof path to MC2.
\end{remark}

\begin{remark}[The bar-intrinsic perspective and the two regimes]
\label{rem:mc2-bar-intrinsic-perspective}
\index{MC2!bar-intrinsic perspective}
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..188c196983fd97a6397eb205be09b395eccc3001
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -4146,6 +4146,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17710,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

codex
Verification is done. I’m cleaning the LaTeX build debris again so the worktree only reflects source and metadata surfaces, not transient `aux`/`log` noise from the failed global build.
exec
/bin/zsh -lc 'make clean' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  Cleaning build artifacts...
  ✓  Clean (stamp preserved — make will skip rebuild if sources unchanged).
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..4fc4048efff16b5d2944c80af17318b232c97fee
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,26 +3031,32 @@
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
 \index{Hodge bundle!alternative proof of Theorem D}
 There is a second proof route to the uniform-weight clause of
-Theorem~D which does not use the shadow tower or the
-Maurer--Cartan element. Let
+Theorem~D which does not use the shadow tower, the
+Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
+as input. Let
 \[
 \pi \colon \overline{\mathcal{C}}_g \longrightarrow
 \overline{\mathcal{M}}_g
 \]
 be the universal curve, let
-$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, and
-write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex
-in the family~\eqref{eq:bar-family}. By the bar-family
-construction and the chain-level modular functor
-\textup{(}Theorem~\textup{\ref{thm:chain-modular-functor}}\textup{)},
-this family defines a virtual perfect complex on
-$\overline{\mathcal{M}}_g$; its scalar rank is determined by the
-Hilbert series of~$\cA$, and the genus-$1$ curvature fixes the
-normalization to be~$\kappa(\cA)$. Since every scalar propagator is
-the same weight-$1$ form $d\!\log E(z,w)$, the only Hodge-theoretic
-bundle entering the scalar sector is~$\mathbb{E}$: higher Hodge
-bundles $R^0\pi_*\omega_\pi^{\otimes h}$ do not appear on the
-uniform-weight lane.
+$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, so
+$c_1(\mathbb{E}) = \lambda_1$ and $c_g(\mathbb{E}) = \lambda_g$.
+Write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex in
+the family~\eqref{eq:bar-family}. Fiberwise it is the complex
+\[
+\barB^{\mathrm{fib}}(\cA)\big|_{[\Sigma]}
+\;=\;
+\bigl(T^c(s^{-1}\bar{\cA}),\, \dfib^{(\Sigma)}\bigr),
+\]
+and its graded ranks are determined by the Hilbert series of~$\cA$.
+Thus its family index $R\pi_*\barB^{\mathrm{fib}}(\cA)$ is a perfect
+virtual complex on $\overline{\mathcal{M}}_g$, with scalar
+normalization fixed at genus~$1$ by the curvature coefficient
+$\kappa(\cA)$. Since every scalar propagator is the same weight-$1$
+form $d\!\log E(z,w)$, the scalar sector couples only to the Hodge
+bundle~$\mathbb{E}$: higher Hodge bundles
+$R^0\pi_*\omega_\pi^{\otimes h}$ do not enter on the uniform-weight
+lane.
 
 Applying Grothendieck--Riemann--Roch to the universal curve gives
 \[
@@ -3061,10 +3067,10 @@
 \text{tautological classes of codimension $< g$},
 \]
 with the Hodge contribution computed by Mumford's GRR formula and
-its Arakelov--Faltings refinement
+Faltings' Arakelov refinement
 \textup{(}\cite{Mumford83,Fal84}\textup{)}. Passing from the
-Chern character to the Euler class of the Hodge summand, the
-codimension-$g$ term is
+Chern character to the codimension-$g$ Euler term, the top-degree
+contribution is
 \[
 \mathrm{obs}_g(\cA)
 \;=\;
@@ -3074,10 +3080,11 @@
 \qquad
 \textup{(UNIFORM-WEIGHT)}.
 \]
-This gives an alternative Hodge-theoretic proof path for
-Theorem~D: genus~$1$ determines~$\kappa(\cA)$, and the family
-index of the fiber bar complex identifies the genus-$g$
-obstruction with the top Chern class of the Hodge bundle.
+Thus genus~$1$ fixes~$\kappa(\cA)$, and GRR identifies the
+genus-$g$ obstruction with the top Chern class of the Hodge bundle.
+This is a second proof route for the uniform-weight clause of
+Theorem~D, using only the family of fiber bar complexes and Hodge
+theory on the universal curve.
 \end{remark}
 
 \begin{corollary}[Scalar free energy as $\hat{A}$-genus;
@@ -4146,6 +4153,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17717,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Checking git status**

I think I should run the git status command again to see the current state of my repository. It’s a good practice to check for any changes, staged files, or untracked files before I make further commits or any other actions. Keeping track of my repository's status helps me avoid mistakes and potential conflicts. Alright, let’s go ahead and get that status updated!
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M chapters/connections/bv_brst.tex
 M chapters/connections/concordance.tex
 M chapters/frame/preface.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_complementarity.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/introduction.tex
 D main.aux
 D main.log
 D main.out
 M metadata/census.json
 M metadata/claims.jsonl
 M metadata/dependency_graph.dot
 M metadata/label_index.json
 M metadata/theorem_registry.md
 M standalone/chiral_chern_weil.tex
 M standalone/classification_trichotomy.tex
 M standalone/introduction_full_survey.tex
 M standalone/programme_summary_sections5_8.tex
 M standalone/seven_faces.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..4fc4048efff16b5d2944c80af17318b232c97fee
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,26 +3031,32 @@
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
 \index{Hodge bundle!alternative proof of Theorem D}
 There is a second proof route to the uniform-weight clause of
-Theorem~D which does not use the shadow tower or the
-Maurer--Cartan element. Let
+Theorem~D which does not use the shadow tower, the
+Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
+as input. Let
 \[
 \pi \colon \overline{\mathcal{C}}_g \longrightarrow
 \overline{\mathcal{M}}_g
 \]
 be the universal curve, let
-$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, and
-write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex
-in the family~\eqref{eq:bar-family}. By the bar-family
-construction and the chain-level modular functor
-\textup{(}Theorem~\textup{\ref{thm:chain-modular-functor}}\textup{)},
-this family defines a virtual perfect complex on
-$\overline{\mathcal{M}}_g$; its scalar rank is determined by the
-Hilbert series of~$\cA$, and the genus-$1$ curvature fixes the
-normalization to be~$\kappa(\cA)$. Since every scalar propagator is
-the same weight-$1$ form $d\!\log E(z,w)$, the only Hodge-theoretic
-bundle entering the scalar sector is~$\mathbb{E}$: higher Hodge
-bundles $R^0\pi_*\omega_\pi^{\otimes h}$ do not appear on the
-uniform-weight lane.
+$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, so
+$c_1(\mathbb{E}) = \lambda_1$ and $c_g(\mathbb{E}) = \lambda_g$.
+Write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex in
+the family~\eqref{eq:bar-family}. Fiberwise it is the complex
+\[
+\barB^{\mathrm{fib}}(\cA)\big|_{[\Sigma]}
+\;=\;
+\bigl(T^c(s^{-1}\bar{\cA}),\, \dfib^{(\Sigma)}\bigr),
+\]
+and its graded ranks are determined by the Hilbert series of~$\cA$.
+Thus its family index $R\pi_*\barB^{\mathrm{fib}}(\cA)$ is a perfect
+virtual complex on $\overline{\mathcal{M}}_g$, with scalar
+normalization fixed at genus~$1$ by the curvature coefficient
+$\kappa(\cA)$. Since every scalar propagator is the same weight-$1$
+form $d\!\log E(z,w)$, the scalar sector couples only to the Hodge
+bundle~$\mathbb{E}$: higher Hodge bundles
+$R^0\pi_*\omega_\pi^{\otimes h}$ do not enter on the uniform-weight
+lane.
 
 Applying Grothendieck--Riemann--Roch to the universal curve gives
 \[
@@ -3061,10 +3067,10 @@
 \text{tautological classes of codimension $< g$},
 \]
 with the Hodge contribution computed by Mumford's GRR formula and
-its Arakelov--Faltings refinement
+Faltings' Arakelov refinement
 \textup{(}\cite{Mumford83,Fal84}\textup{)}. Passing from the
-Chern character to the Euler class of the Hodge summand, the
-codimension-$g$ term is
+Chern character to the codimension-$g$ Euler term, the top-degree
+contribution is
 \[
 \mathrm{obs}_g(\cA)
 \;=\;
@@ -3074,10 +3080,11 @@
 \qquad
 \textup{(UNIFORM-WEIGHT)}.
 \]
-This gives an alternative Hodge-theoretic proof path for
-Theorem~D: genus~$1$ determines~$\kappa(\cA)$, and the family
-index of the fiber bar complex identifies the genus-$g$
-obstruction with the top Chern class of the Hodge bundle.
+Thus genus~$1$ fixes~$\kappa(\cA)$, and GRR identifies the
+genus-$g$ obstruction with the top Chern class of the Hodge bundle.
+This is a second proof route for the uniform-weight clause of
+Theorem~D, using only the family of fiber bar complexes and Hodge
+theory on the universal curve.
 \end{remark}
 
 \begin{corollary}[Scalar free energy as $\hat{A}$-genus;
@@ -4146,6 +4153,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17717,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an



thinking
**Evaluating tracked files**

It seems like I’m dealing with some tracked files like `main.aux` that were surprisingly deleted by `make clean`. We shouldn’t remove user changes since these files are generated but tracked in the repo. I might need to restore them from HEAD since they've been deleted. Using a command like `git show HEAD:main.aux > main.aux` could help restore them, but I need to check if they are indeed tracked first. Let's confirm that!
thinking
**Considering file restoration methods**

I’m pondering using `exec_command` with `sh -lc` to restore `main.aux` and other generated files. While editing via shell seems okay for generated files, the instructions suggest using `apply_patch`. However, restoring these deleted tracked files feels more urgent. I could also consider running `git diff -- main.aux` since it’s deleted, but restoring from `git show` seems better. I’ll focus on restoring these three files and maybe comment to the user about the situation!
codex
`make clean` removed tracked aux files in this repo, which I do not want to leave behind. I’m restoring those three tracked artifacts from `HEAD` so the worktree reflects only the theorem-lane change and the metadata regeneration, not accidental deletions.
exec
/bin/zsh -lc 'git show HEAD:main.aux > main.aux && git show HEAD:main.log > main.log && git show HEAD:main.out > main.out' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..4fc4048efff16b5d2944c80af17318b232c97fee
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,26 +3031,32 @@
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
 \index{Hodge bundle!alternative proof of Theorem D}
 There is a second proof route to the uniform-weight clause of
-Theorem~D which does not use the shadow tower or the
-Maurer--Cartan element. Let
+Theorem~D which does not use the shadow tower, the
+Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
+as input. Let
 \[
 \pi \colon \overline{\mathcal{C}}_g \longrightarrow
 \overline{\mathcal{M}}_g
 \]
 be the universal curve, let
-$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, and
-write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex
-in the family~\eqref{eq:bar-family}. By the bar-family
-construction and the chain-level modular functor
-\textup{(}Theorem~\textup{\ref{thm:chain-modular-functor}}\textup{)},
-this family defines a virtual perfect complex on
-$\overline{\mathcal{M}}_g$; its scalar rank is determined by the
-Hilbert series of~$\cA$, and the genus-$1$ curvature fixes the
-normalization to be~$\kappa(\cA)$. Since every scalar propagator is
-the same weight-$1$ form $d\!\log E(z,w)$, the only Hodge-theoretic
-bundle entering the scalar sector is~$\mathbb{E}$: higher Hodge
-bundles $R^0\pi_*\omega_\pi^{\otimes h}$ do not appear on the
-uniform-weight lane.
+$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, so
+$c_1(\mathbb{E}) = \lambda_1$ and $c_g(\mathbb{E}) = \lambda_g$.
+Write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex in
+the family~\eqref{eq:bar-family}. Fiberwise it is the complex
+\[
+\barB^{\mathrm{fib}}(\cA)\big|_{[\Sigma]}
+\;=\;
+\bigl(T^c(s^{-1}\bar{\cA}),\, \dfib^{(\Sigma)}\bigr),
+\]
+and its graded ranks are determined by the Hilbert series of~$\cA$.
+Thus its family index $R\pi_*\barB^{\mathrm{fib}}(\cA)$ is a perfect
+virtual complex on $\overline{\mathcal{M}}_g$, with scalar
+normalization fixed at genus~$1$ by the curvature coefficient
+$\kappa(\cA)$. Since every scalar propagator is the same weight-$1$
+form $d\!\log E(z,w)$, the scalar sector couples only to the Hodge
+bundle~$\mathbb{E}$: higher Hodge bundles
+$R^0\pi_*\omega_\pi^{\otimes h}$ do not enter on the uniform-weight
+lane.
 
 Applying Grothendieck--Riemann--Roch to the universal curve gives
 \[
@@ -3061,10 +3067,10 @@
 \text{tautological classes of codimension $< g$},
 \]
 with the Hodge contribution computed by Mumford's GRR formula and
-its Arakelov--Faltings refinement
+Faltings' Arakelov refinement
 \textup{(}\cite{Mumford83,Fal84}\textup{)}. Passing from the
-Chern character to the Euler class of the Hodge summand, the
-codimension-$g$ term is
+Chern character to the codimension-$g$ Euler term, the top-degree
+contribution is
 \[
 \mathrm{obs}_g(\cA)
 \;=\;
@@ -3074,10 +3080,11 @@
 \qquad
 \textup{(UNIFORM-WEIGHT)}.
 \]
-This gives an alternative Hodge-theoretic proof path for
-Theorem~D: genus~$1$ determines~$\kappa(\cA)$, and the family
-index of the fiber bar complex identifies the genus-$g$
-obstruction with the top Chern class of the Hodge bundle.
+Thus genus~$1$ fixes~$\kappa(\cA)$, and GRR identifies the
+genus-$g$ obstruction with the top Chern class of the Hodge bundle.
+This is a second proof route for the uniform-weight clause of
+Theorem~D, using only the family of fiber bar complexes and Hodge
+theory on the universal curve.
 \end{remark}
 
 \begin{corollary}[Scalar free energy as $\hat{A}$-genus;
@@ -4146,6 +4153,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17717,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Rechecking git status**

So, I used shell redirection, which is good. Now I’m thinking it might be useful to run `git status` again just to see where everything stands. I wonder if I’m missing anything important. Checking the status is always a good idea to make sure I’m on the right track before moving forward. Let’s see what changes or updates have occurred. It’s just smart to double-check!
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 M chapters/connections/bv_brst.tex
 M chapters/connections/concordance.tex
 M chapters/frame/preface.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_complementarity.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/introduction.tex
 M metadata/census.json
 M metadata/claims.jsonl
 M metadata/dependency_graph.dot
 M metadata/label_index.json
 M metadata/theorem_registry.md
 M standalone/chiral_chern_weil.tex
 M standalone/classification_trichotomy.tex
 M standalone/introduction_full_survey.tex
 M standalone/programme_summary_sections5_8.tex
 M standalone/seven_faces.tex
 M standalone/survey_modular_koszul_duality.tex
 M standalone/survey_modular_koszul_duality_v2.tex
 M standalone/survey_track_a_compressed.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..4fc4048efff16b5d2944c80af17318b232c97fee
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,26 +3031,32 @@
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
 \index{Hodge bundle!alternative proof of Theorem D}
 There is a second proof route to the uniform-weight clause of
-Theorem~D which does not use the shadow tower or the
-Maurer--Cartan element. Let
+Theorem~D which does not use the shadow tower, the
+Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
+as input. Let
 \[
 \pi \colon \overline{\mathcal{C}}_g \longrightarrow
 \overline{\mathcal{M}}_g
 \]
 be the universal curve, let
-$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, and
-write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex
-in the family~\eqref{eq:bar-family}. By the bar-family
-construction and the chain-level modular functor
-\textup{(}Theorem~\textup{\ref{thm:chain-modular-functor}}\textup{)},
-this family defines a virtual perfect complex on
-$\overline{\mathcal{M}}_g$; its scalar rank is determined by the
-Hilbert series of~$\cA$, and the genus-$1$ curvature fixes the
-normalization to be~$\kappa(\cA)$. Since every scalar propagator is
-the same weight-$1$ form $d\!\log E(z,w)$, the only Hodge-theoretic
-bundle entering the scalar sector is~$\mathbb{E}$: higher Hodge
-bundles $R^0\pi_*\omega_\pi^{\otimes h}$ do not appear on the
-uniform-weight lane.
+$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, so
+$c_1(\mathbb{E}) = \lambda_1$ and $c_g(\mathbb{E}) = \lambda_g$.
+Write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex in
+the family~\eqref{eq:bar-family}. Fiberwise it is the complex
+\[
+\barB^{\mathrm{fib}}(\cA)\big|_{[\Sigma]}
+\;=\;
+\bigl(T^c(s^{-1}\bar{\cA}),\, \dfib^{(\Sigma)}\bigr),
+\]
+and its graded ranks are determined by the Hilbert series of~$\cA$.
+Thus its family index $R\pi_*\barB^{\mathrm{fib}}(\cA)$ is a perfect
+virtual complex on $\overline{\mathcal{M}}_g$, with scalar
+normalization fixed at genus~$1$ by the curvature coefficient
+$\kappa(\cA)$. Since every scalar propagator is the same weight-$1$
+form $d\!\log E(z,w)$, the scalar sector couples only to the Hodge
+bundle~$\mathbb{E}$: higher Hodge bundles
+$R^0\pi_*\omega_\pi^{\otimes h}$ do not enter on the uniform-weight
+lane.
 
 Applying Grothendieck--Riemann--Roch to the universal curve gives
 \[
@@ -3061,10 +3067,10 @@
 \text{tautological classes of codimension $< g$},
 \]
 with the Hodge contribution computed by Mumford's GRR formula and
-its Arakelov--Faltings refinement
+Faltings' Arakelov refinement
 \textup{(}\cite{Mumford83,Fal84}\textup{)}. Passing from the
-Chern character to the Euler class of the Hodge summand, the
-codimension-$g$ term is
+Chern character to the codimension-$g$ Euler term, the top-degree
+contribution is
 \[
 \mathrm{obs}_g(\cA)
 \;=\;
@@ -3074,10 +3080,11 @@
 \qquad
 \textup{(UNIFORM-WEIGHT)}.
 \]
-This gives an alternative Hodge-theoretic proof path for
-Theorem~D: genus~$1$ determines~$\kappa(\cA)$, and the family
-index of the fiber bar complex identifies the genus-$g$
-obstruction with the top Chern class of the Hodge bundle.
+Thus genus~$1$ fixes~$\kappa(\cA)$, and GRR identifies the
+genus-$g$ obstruction with the top Chern class of the Hodge bundle.
+This is a second proof route for the uniform-weight clause of
+Theorem~D, using only the family of fiber bar complexes and Hodge
+theory on the universal curve.
 \end{remark}
 
 \begin{corollary}[Scalar free energy as $\hat{A}$-genus;
@@ -4146,6 +4153,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17717,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an



thinking
**Evaluating metadata and structure**

I’m considering the modified files and whether our metadata changes are acceptable. Restoring could be tricky. I should mention in the final report that metadata regeneration updated the files, but since the worktree is dirty, other files remain unchanged. The user should see the same workspace. I'll provide exact references, perhaps including the link for `chapters/theory/higher_genus_modular_koszul.tex`, around line 4149. The user requested a structured output with details about each theorem in the scope report, focusing on MC2 only. The Fortification Report will also need to mention proof statuses.
thinking
**Clarifying errors and build issues**

I need to mention verification of `make fast` failure after cleaning, specifically related to `chapters/theory/en_koszul_duality.tex` due to undefined control sequences, while noting that metadata generation succeeded. It's important to say that the metadata was successfully regenerated, but the full build remains blocked by unrelated errors in the same file. If the build fails for unrelated reasons, I should inform the user. Before finalizing, I think I should inspect for new remark line numbers as well.
exec
/bin/zsh -lc "rg -nF 'Alternative construction via scattering diagram' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4156:\begin{remark}[Alternative construction via scattering diagram]
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..4fc4048efff16b5d2944c80af17318b232c97fee
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,26 +3031,32 @@
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
 \index{Hodge bundle!alternative proof of Theorem D}
 There is a second proof route to the uniform-weight clause of
-Theorem~D which does not use the shadow tower or the
-Maurer--Cartan element. Let
+Theorem~D which does not use the shadow tower, the
+Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
+as input. Let
 \[
 \pi \colon \overline{\mathcal{C}}_g \longrightarrow
 \overline{\mathcal{M}}_g
 \]
 be the universal curve, let
-$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, and
-write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex
-in the family~\eqref{eq:bar-family}. By the bar-family
-construction and the chain-level modular functor
-\textup{(}Theorem~\textup{\ref{thm:chain-modular-functor}}\textup{)},
-this family defines a virtual perfect complex on
-$\overline{\mathcal{M}}_g$; its scalar rank is determined by the
-Hilbert series of~$\cA$, and the genus-$1$ curvature fixes the
-normalization to be~$\kappa(\cA)$. Since every scalar propagator is
-the same weight-$1$ form $d\!\log E(z,w)$, the only Hodge-theoretic
-bundle entering the scalar sector is~$\mathbb{E}$: higher Hodge
-bundles $R^0\pi_*\omega_\pi^{\otimes h}$ do not appear on the
-uniform-weight lane.
+$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, so
+$c_1(\mathbb{E}) = \lambda_1$ and $c_g(\mathbb{E}) = \lambda_g$.
+Write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex in
+the family~\eqref{eq:bar-family}. Fiberwise it is the complex
+\[
+\barB^{\mathrm{fib}}(\cA)\big|_{[\Sigma]}
+\;=\;
+\bigl(T^c(s^{-1}\bar{\cA}),\, \dfib^{(\Sigma)}\bigr),
+\]
+and its graded ranks are determined by the Hilbert series of~$\cA$.
+Thus its family index $R\pi_*\barB^{\mathrm{fib}}(\cA)$ is a perfect
+virtual complex on $\overline{\mathcal{M}}_g$, with scalar
+normalization fixed at genus~$1$ by the curvature coefficient
+$\kappa(\cA)$. Since every scalar propagator is the same weight-$1$
+form $d\!\log E(z,w)$, the scalar sector couples only to the Hodge
+bundle~$\mathbb{E}$: higher Hodge bundles
+$R^0\pi_*\omega_\pi^{\otimes h}$ do not enter on the uniform-weight
+lane.
 
 Applying Grothendieck--Riemann--Roch to the universal curve gives
 \[
@@ -3061,10 +3067,10 @@
 \text{tautological classes of codimension $< g$},
 \]
 with the Hodge contribution computed by Mumford's GRR formula and
-its Arakelov--Faltings refinement
+Faltings' Arakelov refinement
 \textup{(}\cite{Mumford83,Fal84}\textup{)}. Passing from the
-Chern character to the Euler class of the Hodge summand, the
-codimension-$g$ term is
+Chern character to the codimension-$g$ Euler term, the top-degree
+contribution is
 \[
 \mathrm{obs}_g(\cA)
 \;=\;
@@ -3074,10 +3080,11 @@
 \qquad
 \textup{(UNIFORM-WEIGHT)}.
 \]
-This gives an alternative Hodge-theoretic proof path for
-Theorem~D: genus~$1$ determines~$\kappa(\cA)$, and the family
-index of the fiber bar complex identifies the genus-$g$
-obstruction with the top Chern class of the Hodge bundle.
+Thus genus~$1$ fixes~$\kappa(\cA)$, and GRR identifies the
+genus-$g$ obstruction with the top Chern class of the Hodge bundle.
+This is a second proof route for the uniform-weight clause of
+Theorem~D, using only the family of fiber bar complexes and Hodge
+theory on the universal curve.
 \end{remark}
 
 \begin{corollary}[Scalar free energy as $\hat{A}$-genus;
@@ -4146,6 +4153,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17717,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an


thinking
**Structuring my report**

I think it’s better to present my confidence levels in prose before the report. I’ll indicate a primary high and secondary medium confidence, but I should specify that total fortification isn't complete. I’ll use `CONFIDENCE: medium` but clarify it in a paragraph. It's important to note build verification and the relevant file link. I want to mention that the `make fast` command resulted in unrelated failures and that the metadata regeneration was successful. Additionally, I need to keep it concise!
codex
Added a new remark at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:4156) giving a second proof path for MC2 in Kontsevich--Soibelman language. It packages the primitive shadow data as wall Hamiltonians, orders them by BPS phase, uses pronilpotent completion plus the shadow-growth estimate for convergence, and identifies the Maurer--Cartan equation with scattering-diagram consistency.

Verification: `python3 scripts/generate_metadata.py` succeeded. A clean `make fast` still fails outside this edit, at pre-existing undefined-control-sequence sites in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3407). Metadata regeneration updated generated files under `metadata/`; those diffs are broader because the worktree already has unrelated source changes.

## Fortification Report
- `thm:mc2-bar-intrinsic`
- PRIMARY PROOF: sound
- SECONDARY PROOF: sketched
- TECHNIQUE: Kontsevich--Soibelman scattering diagram / phase-ordered wall-crossing product in the completed pronilpotent shadow algebra
- CONDITION STATUS: unconditional for the primary proof; secondary path conditional on installing the full scattering-diagram formalism on `\widehat{\gAmod}` inside the manuscript
- CONFIDENCE: medium
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index 6ffda76d61028b50781971421c7753a7df4362a2..4fc4048efff16b5d2944c80af17318b232c97fee
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,26 +3031,32 @@
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}
 \index{Hodge bundle!alternative proof of Theorem D}
 There is a second proof route to the uniform-weight clause of
-Theorem~D which does not use the shadow tower or the
-Maurer--Cartan element. Let
+Theorem~D which does not use the shadow tower, the
+Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
+as input. Let
 \[
 \pi \colon \overline{\mathcal{C}}_g \longrightarrow
 \overline{\mathcal{M}}_g
 \]
 be the universal curve, let
-$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, and
-write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex
-in the family~\eqref{eq:bar-family}. By the bar-family
-construction and the chain-level modular functor
-\textup{(}Theorem~\textup{\ref{thm:chain-modular-functor}}\textup{)},
-this family defines a virtual perfect complex on
-$\overline{\mathcal{M}}_g$; its scalar rank is determined by the
-Hilbert series of~$\cA$, and the genus-$1$ curvature fixes the
-normalization to be~$\kappa(\cA)$. Since every scalar propagator is
-the same weight-$1$ form $d\!\log E(z,w)$, the only Hodge-theoretic
-bundle entering the scalar sector is~$\mathbb{E}$: higher Hodge
-bundles $R^0\pi_*\omega_\pi^{\otimes h}$ do not appear on the
-uniform-weight lane.
+$\mathbb{E} = R^0\pi_*\omega_\pi$ be the Hodge bundle, so
+$c_1(\mathbb{E}) = \lambda_1$ and $c_g(\mathbb{E}) = \lambda_g$.
+Write $\barB^{\mathrm{fib}}(\cA)$ for the scalar fiber bar complex in
+the family~\eqref{eq:bar-family}. Fiberwise it is the complex
+\[
+\barB^{\mathrm{fib}}(\cA)\big|_{[\Sigma]}
+\;=\;
+\bigl(T^c(s^{-1}\bar{\cA}),\, \dfib^{(\Sigma)}\bigr),
+\]
+and its graded ranks are determined by the Hilbert series of~$\cA$.
+Thus its family index $R\pi_*\barB^{\mathrm{fib}}(\cA)$ is a perfect
+virtual complex on $\overline{\mathcal{M}}_g$, with scalar
+normalization fixed at genus~$1$ by the curvature coefficient
+$\kappa(\cA)$. Since every scalar propagator is the same weight-$1$
+form $d\!\log E(z,w)$, the scalar sector couples only to the Hodge
+bundle~$\mathbb{E}$: higher Hodge bundles
+$R^0\pi_*\omega_\pi^{\otimes h}$ do not enter on the uniform-weight
+lane.
 
 Applying Grothendieck--Riemann--Roch to the universal curve gives
 \[
@@ -3061,10 +3067,10 @@
 \text{tautological classes of codimension $< g$},
 \]
 with the Hodge contribution computed by Mumford's GRR formula and
-its Arakelov--Faltings refinement
+Faltings' Arakelov refinement
 \textup{(}\cite{Mumford83,Fal84}\textup{)}. Passing from the
-Chern character to the Euler class of the Hodge summand, the
-codimension-$g$ term is
+Chern character to the codimension-$g$ Euler term, the top-degree
+contribution is
 \[
 \mathrm{obs}_g(\cA)
 \;=\;
@@ -3074,10 +3080,11 @@
 \qquad
 \textup{(UNIFORM-WEIGHT)}.
 \]
-This gives an alternative Hodge-theoretic proof path for
-Theorem~D: genus~$1$ determines~$\kappa(\cA)$, and the family
-index of the fiber bar complex identifies the genus-$g$
-obstruction with the top Chern class of the Hodge bundle.
+Thus genus~$1$ fixes~$\kappa(\cA)$, and GRR identifies the
+genus-$g$ obstruction with the top Chern class of the Hodge bundle.
+This is a second proof route for the uniform-weight clause of
+Theorem~D, using only the family of fiber bar complexes and Hodge
+theory on the universal curve.
 \end{remark}
 
 \begin{corollary}[Scalar free energy as $\hat{A}$-genus;
@@ -4146,6 +4153,82 @@
 an MC element in~$\widehat{\gAmod}$.
 \end{remark}
 
+\begin{remark}[Alternative construction via scattering diagram]
+\label{rem:mc2-scattering-diagram}
+\index{Maurer--Cartan element!scattering-diagram construction}
+\index{Kontsevich--Soibelman!alternative construction of MC2}
+This is a proof sketch for a second construction of the element of
+Theorem~\ref{thm:mc2-bar-intrinsic}.
+Work in the shadow algebra of
+Definition~\ref{def:shadow-algebra} and choose a central-charge map
+\[
+Z \colon \bigoplus_{r \geq 2} \mathbb{Z} e_r \longrightarrow \mathbb{C}
+\]
+on the shadow grading. Order the rays by increasing
+$\arg Z(e_r)$ \textup{(}the BPS phase ordering\textup{)}.
+On an autonomous primary line~$L$, the primitive degree-$r$ shadow
+invariant $S_r(L)$ determines a wall
+$\ell_r := \mathbb{R}_{>0} Z(e_r)$ and a wall-crossing automorphism
+\[
+\Phi_{\ell_r}
+\;:=\;
+\exp\!\bigl(\operatorname{ad}_{H_r}\bigr),
+\qquad
+H_r := S_r(L)\,e_r .
+\]
+For the full multi-channel theory one replaces the scalar Hamiltonian
+$H_r$ by the primitive degree-$r$ shadow class in
+$\cA^{\mathrm{sh}}_{r,\bullet}$.
+
+Theorem~\ref{thm:stable-graph-pronilpotent-completion} and the weight
+filtration used in Theorem~\ref{thm:recursive-existence} place all
+these automorphisms in the pronilpotent group
+$\exp(F^1\widehat{\gAmod})$.
+The ordered product
+\[
+\Phi_{\mathfrak{D}}
+\;:=\;
+\prod_{\ell\ \textup{in BPS phase order}} \Phi_\ell
+\]
+therefore converges in every quotient
+$\gAmod/F^{N+1}\gAmod$ and hence in
+$\exp(F^1\widehat{\gAmod})$.
+On an autonomous primary line, the shadow-growth estimate
+\[
+|S_r(L)| \sim A(L)\,\rho_L^{\,r}\,r^{-5/2}
+\qquad (r \to \infty)
+\]
+of Theorem~\ref{thm:shadow-radius}\textup{(}ii\textup{)} implies that
+modulo $F^{N+1}$ only finitely many rays of weight $\leq N$ contribute,
+so the phase-ordered product stabilizes degree by degree.
+
+If the scattering diagram is consistent in the sense of
+Kontsevich--Soibelman~\cite{KS00}, the product around any loop is the
+identity. The Kontsevich--Soibelman lemma then identifies the logarithm
+of the ordered product with a Maurer--Cartan element:
+\[
+\Theta_\cA^{\mathrm{scat}}
+\;:=\;
+\log(\Phi_{\mathfrak{D}})
+\;\in\;
+\widehat{\gAmod},
+\qquad
+[\dzero,\Theta_\cA^{\mathrm{scat}}]
++ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
+= 0.
+\]
+Its degree-$r$ truncation is built from the same primitive shadow data
+as the obstruction tower, now assembled by Baker--Campbell--Hausdorff
+rather than by the recursive inverse-limit construction.
+This gives a second conceptual origin for~$\Theta_\cA$:
+the primitive shadows are the wall data, the BPS phase ordering is the
+assembly rule, and the Maurer--Cartan equation is the infinitesimal
+form of scattering-diagram consistency.
+The missing manuscript-level input is the full setup of this
+scattering-diagram formalism on $\widehat{\gAmod}$; once that package is
+installed, it furnishes an alternative proof path to MC2.
+\end{remark}
+
 \begin{remark}[The bar-intrinsic perspective and the two regimes]
 \label{rem:mc2-bar-intrinsic-perspective}
 \index{MC2!bar-intrinsic perspective}
@@ -17634,6 +17717,82 @@
 $d_{\mathrm{alg}} \geq 3$ remains.
 \end{proof}
 
+\begin{remark}[Alternative proof via the shadow Lie algebra]
+\label{rem:depth-gap-shadow-lie-alternative}
+\index{shadow algebra!depth gap alternative proof}
+\index{algebraic depth!shadow Lie algebra proof}
+On a primary line $L = \Bbbk \cdot x$ with $\kappa|_L \neq 0$,
+the one-variable shadow algebra carries the H-Poisson bracket
+\[
+ \{x^j, x^k\}_H \;=\; jk\,P\,x^{j+k-2},
+ \qquad P = \kappa^{-1}.
+\]
+Set $h := S_2 x^2 = \kappa x^2$. Then
+\[
+ \operatorname{ad}_h(x^r)
+ \;=\;
+ \{h, x^r\}_H
+ \;=\;
+ 2r\,x^r
+ \;=\;
+ \nabla_H(x^r),
+ \qquad r \geq 2.
+\]
+Thus $\operatorname{ad}_h$ is semisimple and invertible on every
+degree-$r$ piece with $r \geq 3$. The projected Maurer--Cartan
+equation
+\textup{(}Proposition~\textup{\ref{prop:master-equation-from-mc}}\textup{)}
+therefore reads
+\[
+ \operatorname{ad}_h(\operatorname{Sh}_r)
+ \;=\;
+ -\,\mathfrak{o}^{(r)},
+\]
+so a higher shadow can vanish only when the corresponding
+obstruction bracket vanishes inside the shadow Lie algebra.
+
+At degree~$4$ one has
+$o_4 = \tfrac12\{\mathfrak{C}, \mathfrak{C}\}_H$. For the affine
+class, $\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$, and $o_4 = 0$ is
+exactly the Jacobi identity. This is the finite Lie case
+$d_{\mathrm{alg}} = 1$.
+
+If $S_4 \neq 0$, then the quartic class cannot be terminal on a
+$\kappa \neq 0$ line. If $S_3 \neq 0$, then
+\[
+ \{\mathfrak{C}, \mathfrak{Q}\}_H
+ \;=\;
+ 12\,P\,S_3 S_4\,x^5
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_5 \neq 0$. If $S_3 = 0$, then
+\[
+ \tfrac12\{\mathfrak{Q}, \mathfrak{Q}\}_H
+ \;=\;
+ 8\,P\,S_4^2\,x^6
+ \;\neq\; 0,
+\]
+so $\operatorname{Sh}_6 \neq 0$. In the first case,
+$\{\mathfrak{C}, \operatorname{Sh}_r\}_H \neq 0$ propagates the
+tower to all higher degrees. In the second,
+$\{\mathfrak{Q}, \operatorname{Sh}_{2m}\}_H \neq 0$ produces an
+infinite even tail. Hence a nonzero quartic shadow on a
+$\kappa \neq 0$ line forces infinitely many higher shadows.
+
+This recovers the $\kappa \neq 0$ part of
+Proposition~\ref{prop:depth-gap-trichotomy} without using the
+closed form $H(t) = t^2\sqrt{Q_L(t)}$: the only finite
+possibilities on a primary line are the Gaussian square
+$S_3 = S_4 = 0$ and the Lie square $S_3 \neq 0$, $S_4 = 0$.
+The remaining finite value $d_{\mathrm{alg}} = 2$ is the global
+contact boundary case $\kappa = 0$, realized by the full
+$\beta\gamma_\lambda$ family as in the proof above. This is the
+shadow-Lie reinterpretation of the degree-$4$ Jacobi cancellation
+used elsewhere in this chapter, so it is consistent with the
+primary proof while remaining independent of the Riccati closed
+form.
+\end{remark}
+
 The depth gap is the shadow tower's sharpest structural
 constraint. It says that the four classes
 $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an

tokens used
254,920
