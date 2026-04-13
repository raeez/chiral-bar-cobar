# E10_missing_examples_thms (498s)

**Findings**
1. PROBLEM at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5475): `chapters/examples/` did not contain a worked Theorem H example; the Heisenberg five-theorem table only said “Degree-preserving sub-MC / polynomial,” which was a summary, not an explicit verification. EXACT edit applied: I replaced the H row with `\ChirHoch^{>2}(\cH_k)=0` and `P_{\cH_k}(t)=1+t+t^2`, then added the explicit Heisenberg computation at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5481) giving `\ChirHoch^0=\mathbb{C}`, `\ChirHoch^1=\mathbb{C}\cdot[D]`, `\ChirHoch^2=\mathbb{C}\cdot[\partial_k]`, and `\ChirHoch^n=0` for `n\ge 3`, with the bar-resolution argument and the tie-back to Theorem H.

2. PROBLEM at [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:67): the Theorem H row pointed to `thm:kac-moody-ainfty`, which is an `A_\infty` theorem, not the Hochschild theorem. EXACT edit applied: I changed the reference to `Thms~\ref{thm:main-koszul-hoch}, \ref{thm:hochschild-polynomial-growth}; Prop.~\ref{prop:chirhoch1-affine-km}` at [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:69).

3. PROBLEM at [level1_bridge.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/level1_bridge.tex:56): the level-1 five-theorem table had the same wrong Theorem H reference to `thm:kac-moody-ainfty`. EXACT edit applied: I changed it to `Thms~\ref{thm:main-koszul-hoch}, \ref{thm:hochschild-polynomial-growth}` at [level1_bridge.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/level1_bridge.tex:59).

**Worked-example coverage after the patch**
- A, B, C already had explicit family verification in [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:3937) for `\widehat{\mathfrak{sl}}_{2,k}` at genus 1.
- D already had an explicit Heisenberg lane in [heisenberg_eisenstein.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:58) and [heisenberg_eisenstein.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:2362).
- H now has an explicit Heisenberg worked example in [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5481).

Verification was a narrow grep and line inspection on the edited example files. I did not run a full TeX build.


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
session id: 019d87b5-0594-7123-8a5f-a7f51ec5bbde
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


For Theorems A-D, H: find worked examples.
Search chapters/examples/ for explicit verification of each theorem for a specific family.
If a theorem lacks a worked example: write one for Heisenberg (simplest).
mcp startup: no servers
codex
Using `deep-beilinson-audit` and likely `build-surface` after fixes. I’m first reading the repo constitution and locating the Theorem A-D, H example surface in `chapters/examples/`, then I’ll patch missing worked examples with the smallest truthful edits.
exec
/bin/zsh -lc "printf '--- CLAUDE.md ---\\n'; sed -n '1,220p' CLAUDE.md; printf '\\n--- concordance ---\\n'; sed -n '1,260p' chapters/connections/concordance.tex; printf '\\n--- theorem_registry ---\\n'; sed -n '1,260p' metadata/theorem_registry.md; printf '\\n--- red_team_summary ---\\n'; if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi; printf '\\n--- git status ---\\n'; git status --short" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
--- CLAUDE.md ---
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

thinking
**Considering tool usage**

I’m thinking about using the parallel spawn feature. Actually, I can use multi_tool_use.parallel to run multiple developer tools at the same time, like spawn_agent calls and exec_command, but only for developer tools. I wonder if I should just spawn one or two tools. It might be more efficient if I do two explorers in parallel. I think that could work well!
codex
I’ve read the constitution and the worktree is dirty, so I’ll keep edits confined to the example surface. Next I’m mapping which of A, B, C, D, H already have explicit worked examples and which gaps need a Heisenberg repair.
collab spawn_agent(call_Ez2klfeggrbuQGAVA4by6Wqu, prompt="<task>Audit chapters/examples/ for explicit worked examples of Theorems A, B, C, D, H in Volume I. Identify exact files/…")
mcp startup: no servers
spawn_agent(call_Ez2klfeggrbuQGAVA4by6Wqu, prompt="<task>Audit chapters/examples/ for explicit worked examples of Theorems A, B, C, D, H in Volume I. Identify exact files/…") pending init:
  agent: 019d87b5-7b0b-7283-b0e4-faaea3529774
collab spawn_agent(call_7DFrDRsTWMG044TfG4J5F81m, prompt="<task>Within chapters/examples/, find the best Heisenberg-focused file(s) to host missing worked examples for Theorems A…")
spawn_agent(call_7DFrDRsTWMG044TfG4J5F81m, prompt="<task>Within chapters/examples/, find the best Heisenberg-focused file(s) to host missing worked examples for Theorems A…") pending init:
  agent: 019d87b5-7b10-7951-a0de-cbe7799ee5ec
mcp startup: no servers
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
Plan update
  → Inventory chapters/examples directory to find files referencing Theorems A-D,H
  • Inspect identified files for worked examples, note families and references
  • Summarize findings in table and gap list

exec
/bin/zsh -lc 'ls chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
bar_complex_tables.tex
bershadsky_polyakov.tex
beta_gamma.aux
beta_gamma.tex
deformation_quantization.aux
deformation_quantization.tex
deformation_quantization_examples.tex
free_fields.aux
free_fields.tex
genus_expansions.tex
heisenberg_eisenstein.tex
kac_moody.aux
kac_moody.tex
landscape_census.tex
lattice_foundations.aux
lattice_foundations.tex
level1_bridge.aux
level1_bridge.tex
logarithmic_w_algebras.tex
minimal_model_examples.tex
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && ls chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bar_complex_tables.tex
bershadsky_polyakov.tex
beta_gamma.aux
beta_gamma.tex
deformation_quantization.aux
deformation_quantization.tex
deformation_quantization_examples.tex
free_fields.aux
free_fields.tex
genus_expansions.tex
heisenberg_eisenstein.tex
kac_moody.aux
kac_moody.tex
landscape_census.tex
lattice_foundations.aux
lattice_foundations.tex
level1_bridge.aux
level1_bridge.tex
logarithmic_w_algebras.tex
minimal_model_examples.tex
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem [ABCDH]" chapters/examples' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '1,160p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

% Regime I: quadratic (Convention~\ref{conv:regime-tags}).

\section{The algebra and shadow archetype}
\label{sec:heisenberg-archetype}

The Heisenberg algebra~$\cH_\kappa$ is the Gaussian archetype
(class~G, shadow depth $r_{\max} = 2$). It is the simplest modular
Koszul algebra: the shadow obstruction tower terminates at degree~$2$,
the complementarity potential is exactly quadratic, and the full open/closed
MC element reduces to the scalar modular characteristic~$\kappa$.
All five main theorems (A through~D and~H) are immediate. The genus
expansion is controlled entirely by~$\kappa$ and assembles into the
$\hat{A}$-genus.

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{ll}
\textbf{Algebra} & Heisenberg~$\cH_\kappa$, rank~$1$,
OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ \\
thinking
**Revising the plan**

I think I need to update my plan once I have enough context. In the meantime, I can manually search for the exact files I need. It might be a good idea to use the update_plan tool since it's significant to the task, but only after I've gathered that context. I should also search for examples and perhaps read the skill file. I'm considering using the build-surface skill too, along with the deep-beilinson-audit skill.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~\\\\ref\\{|Theorems~A|Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|thm:(bar-cobar-isomorphism-main|higher-genus-inversion|bar-cobar-inversion-qi|fiber-center-identification|quantum-complementarity-main|shifted-symplectic-complementarity|modular-characteristic|multi-weight-genus-expansion|main-koszul-hoch|hochschild-polynomial-growth|chirhoch1-affine-km)\" chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

 succeeded in 51ms:
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
chapters/examples/deformation_quantization.tex:803:The chiral Kontsevich formula realizes Theorem~A
chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
chapters/examples/deformation_quantization.tex:816:Theorems~B and~C (Theorems~\ref{thm:higher-genus-inversion}
chapters/examples/deformation_quantization.tex:817:and~\ref{thm:quantum-complementarity-main}) address the
chapters/examples/deformation_quantization.tex:820:whether the genus-$g$ bar-cobar inversion of Theorem~B
chapters/examples/w_algebras_deep.tex:356:(Theorem~\ref{thm:quantum-complementarity-main}; this is nonzero, since the full MC elements do \emph{not} sum to zero for $\mathcal{W}$-algebras). The Miura embedding
chapters/examples/w_algebras_deep.tex:1243:($\operatorname{Ran}_1(X) \cong X$) follows from Theorem~A +
chapters/examples/w_algebras_deep.tex:1250:is a quasi-isomorphism by the diagonal case (Theorem~B);
chapters/examples/w_algebras_deep.tex:1259:Theorems~A/B and factorization cosheaf structure, not the
chapters/examples/w_algebras_deep.tex:1974:(Theorem~\ref{thm:multi-weight-genus-expansion}).
chapters/examples/w_algebras_deep.tex:2346: Koszul conductor (Theorem~\textup{\ref{thm:quantum-complementarity-main}}).
chapters/examples/w_algebras_deep.tex:3283: by Theorem~\textup{\ref{thm:quantum-complementarity-main}}.
chapters/examples/w_algebras_deep.tex:3583:Theorem~D) or Kac--Moody-type ($\kappa + \kappa' = 0$).
chapters/examples/w_algebras_deep.tex:5193:under cosets (Theorem~D):
chapters/examples/symmetric_orbifolds.tex:194:status: Theorem~D is proved (Proposition~\ref{prop:symn-kappa}),
chapters/examples/symmetric_orbifolds.tex:230:Theorem~\ref{thm:hochschild-polynomial-growth}, with degree
chapters/examples/lattice_foundations.tex:230:for single-generator algebras of uniform conformal weight (Theorem~D, Remark~\ref{rem:propagator-weight-universality}).
chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/examples/lattice_foundations.tex:1950:\item \emph{Theorem~B} (Theorem~\ref{thm:higher-genus-inversion}).
chapters/examples/lattice_foundations.tex:1957:\item \emph{Theorem~C}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem A" chapters/examples' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "Heisenberg" -n chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 574

chapters/examples/deformation_quantization.tex:53:The configuration spaces here are the same ones that defined the Heisenberg bar differential (\S\ref{sec:frame-bar-deg2}), now with marked boundary points replacing interior points.
chapters/examples/deformation_quantization.tex:442:\subsection{Example 1: Heisenberg algebra}
chapters/examples/deformation_quantization.tex:1046:\subsection{Chiral star product: explicit Heisenberg computation}
chapters/examples/deformation_quantization.tex:1048:\begin{computation}[Heisenberg chiral star product through \texorpdfstring{$\hbar^3$}{3}]
chapters/examples/deformation_quantization.tex:1050:\index{Heisenberg algebra!star product}
chapters/examples/deformation_quantization.tex:1051:\index{deformation quantization!Heisenberg}
chapters/examples/deformation_quantization.tex:1053:For the Heisenberg algebra $\mathcal{H}_\kappa$ with Coisson
chapters/examples/deformation_quantization.tex:1081:For $a = a_{-1}|0\rangle$ (the basic Heisenberg mode):
chapters/examples/deformation_quantization.tex:1083:$\lambda$-bracket vanishes on generators because the Heisenberg
chapters/examples/deformation_quantization.tex:1087:All terms vanish for the same reason: the Heisenberg Poisson
chapters/examples/w_algebras_deep.tex:291:Heisenberg algebra $\mathcal{H}^{\otimes 2}$ (two free bosons $\phi_1, \phi_2$
chapters/examples/w_algebras_deep.tex:359:through the rank-$2$ Heisenberg curvature.
chapters/examples/w_algebras_deep.tex:3766:\item \emph{Gaussian} (Heisenberg, lattice VOA, free fermion):
chapters/examples/w_algebras_deep.tex:5132:Heisenberg current and a $c = 0$ stress tensor, both
chapters/examples/w_algebras_deep.tex:5202:$\kappa(\widehat{U(1)}) = k/2 + 1$ (Heisenberg at the
chapters/examples/w_algebras_deep.tex:5300:$J$-line \textup{(Heisenberg)} & $c/3$ & $0$ & $0$ & $0$ & G \\
chapters/examples/w_algebras_deep.tex:5306:a free Heisenberg channel \textup{(}class~G, shadow depth~$2$\textup{)}: the
chapters/examples/w_algebras_deep.tex:5404:$c = 9$, while the Heisenberg channels remain Gaussian.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:[ABCDH]" chapters/examples' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "Theorem [ABCDH]" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1575

chapters/examples/deformation_quantization.tex:27: Theorem~\ref{thm:hochschild-bar-cobar}.
chapters/examples/deformation_quantization.tex:144:\begin{proof}[Proof of Theorem~\ref{thm:chiral-quantization}]
chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/examples/deformation_quantization.tex:147:For coisson algebras, the classical Kontsevich formality theorem ensures the vanishing of all higher obstructions at the operadic level: the $E_2$-operad (governing Poisson structures) is formal, so the deformation problem is unobstructed. Theorem~\ref{thm:geometric-equals-operadic-bar} lifts this to the curve $X$: the same object as the operadic bar construction is computed via the geometric bar complex, so formality propagates from the classical to the chiral setting. Gauge equivalence follows from the standard deformation-theoretic argument: different choices of Maurer--Cartan element in the same gauge orbit give isomorphic deformations.
chapters/examples/deformation_quantization.tex:207:By Theorem~\ref{thm:chiral-formality}
chapters/examples/deformation_quantization.tex:232:FM spaces (Theorem~\ref{thm:FM-operad}; \cite{FM94}):
chapters/examples/deformation_quantization.tex:242:of Kontsevich's argument (\cite{Kon03}, Theorem~6.4).
chapters/examples/deformation_quantization.tex:260:Theorem~\ref{thm:chiral-formality} (\ClaimStatusProvedElsewhere,
chapters/examples/deformation_quantization.tex:427:Given an MC element $\alpha = \sum_{n \geq 1} \hbar^n \alpha_n$ with $\alpha_n \in \bar{B}^1(\mathcal{A}_{\mathrm{cl}})$, define $a \star_\alpha b = m_2(a,b) + \sum_{n \geq 1} \hbar^n \langle \alpha_n, a \otimes b \rangle$. The MC equation $d\alpha + \frac{1}{2}[\alpha,\alpha] = 0$ unfolds order by order in $\hbar$: at order $\hbar^n$, the condition $d\alpha_n + \frac{1}{2}\sum_{i+j=n}[\alpha_i,\alpha_j] = 0$ is equivalent to the associativity of $\star_\alpha$ at order $\hbar^n$, since the bar differential $d$ encodes the failure of associativity and the bracket $[\alpha_i,\alpha_j]$ encodes the composition of deformations (this is the standard deformation-theoretic correspondence, see \cite{Kon03}, \S4, or \cite{LV12}, Theorem~10.1.1). Conversely, any associative star product defines an MC element by reversing the correspondence.
chapters/examples/deformation_quantization.tex:543:By the modular operad decomposition (Theorem~\ref{thm:prism-higher-genus}), the bar complex of the quantized chiral algebra decomposes by genus: $\B(\cA_\hbar) = \bigoplus_{g \geq 0} \B^{(g)}(\cA_\hbar)$. The star product $a \star b$ is computed by the bar-cobar formalism applied to two insertions, and the genus-$g$ contribution is $\star^{(g)}(a,b) = \int_{\overline{\mathcal{M}}_{g,2}} \mathrm{ev}^*(\B^{(g)}_2(a \otimes b))$. The power $\hbar^g$ arises because the genus-$g$ contribution involves $g$ additional propagator insertions (each carrying a factor of~$\hbar$) beyond the tree-level term. At genus~0, $\star^{(0)}$ is the Kontsevich star product; for $g \geq 1$, $\star^{(g)}$ involves the genus-$g$ propagator and produces corrections controlled by modular forms of $\mathrm{Sp}(2g, \mathbb{Z})$.
chapters/examples/deformation_quantization.tex:635:theorem (Theorem~\ref{thm:chiral-formality}, \ClaimStatusProvedElsewhere,
chapters/examples/deformation_quantization.tex:637:$L_\infty$ quasi-isomorphism of Theorem~\ref{thm:chiral-formality}
chapters/examples/deformation_quantization.tex:641:(Theorem~\ref{thm:geometric-equals-operadic-bar}) provides the
chapters/examples/deformation_quantization.tex:725:(Theorem~\ref{thm:operadic-center-hochschild}).
chapters/examples/deformation_quantization.tex:803:The chiral Kontsevich formula realizes Theorem~A
chapters/examples/deformation_quantization.tex:804:(Theorem~\ref{thm:bar-cobar-isomorphism-main})
chapters/examples/deformation_quantization.tex:808:bar-cobar composite (Theorem~\ref{thm:chiral-kontsevich}).
chapters/examples/deformation_quantization.tex:811:(Theorem~\ref{thm:geometric-equals-operadic-bar}).
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~[ABCDH]" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/deformation_quantization.tex:803:The chiral Kontsevich formula realizes Theorem~A
chapters/examples/deformation_quantization.tex:820:whether the genus-$g$ bar-cobar inversion of Theorem~B
chapters/examples/w_algebras_deep.tex:1243:($\operatorname{Ran}_1(X) \cong X$) follows from Theorem~A +
chapters/examples/w_algebras_deep.tex:1250:is a quasi-isomorphism by the diagonal case (Theorem~B);
chapters/examples/w_algebras_deep.tex:3583:Theorem~D) or Kac--Moody-type ($\kappa + \kappa' = 0$).
chapters/examples/w_algebras_deep.tex:5193:under cosets (Theorem~D):
chapters/examples/symmetric_orbifolds.tex:194:status: Theorem~D is proved (Proposition~\ref{prop:symn-kappa}),
chapters/examples/lattice_foundations.tex:230:for single-generator algebras of uniform conformal weight (Theorem~D, Remark~\ref{rem:propagator-weight-universality}).
chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/examples/lattice_foundations.tex:1950:\item \emph{Theorem~B} (Theorem~\ref{thm:higher-genus-inversion}).
chapters/examples/lattice_foundations.tex:1957:\item \emph{Theorem~C}
chapters/examples/lattice_foundations.tex:5124:(Theorem~D). The higher-degree corrections at genus~$1$ involve
chapters/examples/y_algebras.tex:415:sums (Theorem~D, additivity) gives the channel-by-channel
chapters/examples/heisenberg_eisenstein.tex:58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
chapters/examples/heisenberg_eisenstein.tex:2362:= F_g(\cH_\kappa)$ which is the genus tower of Theorem~D.
chapters/examples/free_fields.tex:504:Theorem~C \textup{(}Theorem~\ref{thm:quantum-complementarity-main}\textup{)}:
chapters/examples/free_fields.tex:1767:Theorem~A$_2$).
chapters/examples/free_fields.tex:1854:The residue pairing matrix of Step~3 is rank 3 (matching the 3 generators $\psi^{(-1)}, \psi^{(0)}, \psi^{(1)}$ paired against the 4 generators $\beta, \gamma, b, c$ of the derived $\beta\gamma$-$bc$ system). The pairing $\langle \psi^{(i)}, - \rangle: \mathcal{B}^{\bullet} \to \mathbb{C}$ identifies $\mathcal{F}^{\bullet}$ with the linear dual of the cogenerators of $\bar{B}(\mathcal{B}^{\bullet})$: the bar complex of the derived $\beta\gamma$-$bc$ system has cogenerators in bar degree 1 dual to $\psi^{(0)}, \psi^{(\pm 1)}$, with the bar differential $d_{\bar{B}}$ encoding the BRST differential $Q$ of Step~4. The $A_\infty$ structure on $\mathcal{F}^{\bullet}$ is then recovered as the Verdier dual $D_{\mathrm{Ran}}(\bar{B}(\mathcal{B}^{\bullet})) \simeq \bar{B}((\mathcal{B}^{\bullet})^!)$ (Theorem~\ref{thm:quantum-complementarity-main}), identifying $\mathcal{F}^{\bullet}$ as the homotopy Koszul dual $(\mathcal{B}^{\bullet})^!_\infty$. Note: the cobar functor $\Omega(\bar{B}(\mathcal{B}^{\bullet})) \simeq \mathcal{B}^{\bullet}$ (bar-cobar inversion, Theorem~B) recovers $\mathcal{B}^{\bullet}$ itself, not its Koszul dual.
chapters/examples/yangians_foundations.tex:877:\emph{Theorem~A (Geometric Bar-Cobar Duality).}
chapters/examples/yangians_foundations.tex:895:\emph{Theorem~B (Bar-Cobar Inversion).}
exec
/bin/zsh -lc 'rg -n "Theorem~A" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2948

chapters/examples/deformation_quantization.tex:803:The chiral Kontsevich formula realizes Theorem~A
healing_20260413_132214/H05_thm_H_alt_proof.md:658:   668	$\cA^! = \mathbb{D}_X(\cA^i)$, and Theorem~A identifies the resulting
healing_20260413_132214/H05_thm_H_alt_proof.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 176848)
healing_20260413_132214/H01_thm_A_alt_proof.md:263:45:The bar-cobar adjunction of Theorem~A
healing_20260413_132214/H01_thm_A_alt_proof.md:272:142:locus (Theorem~A) are proved. The Verdier intertwining that
healing_20260413_132214/H01_thm_A_alt_proof.md:318:chapters/theory/chiral_koszul_pairs.tex:142:locus (Theorem~A) are proved. The Verdier intertwining that
healing_20260413_132214/H01_thm_A_alt_proof.md:640: (Theorem~A, Convention~\ref{conv:bar-coalgebra-identity}):
healing_20260413_132214/H01_thm_A_alt_proof.md:1723:  3857	\subsection{Geometric bar-cobar duality (Theorem~A)}
healing_20260413_132214/H01_thm_A_alt_proof.md:1729:  3863	Theorem~A identifies the conditions under which $\cA^!_\infty$ is
chapters/examples/w_algebras_deep.tex:1243:($\operatorname{Ran}_1(X) \cong X$) follows from Theorem~A +
healing_20260413_132214/H19_remove_genus0_koszul_vii.md:669:/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
fix_wave_D_20260413_182434/D04_slop_v2.md:469:of Theorem~A (with $h^\vee = 2$ the dual Coxeter number of
healing_20260413_132214/H02_thm_B_alt_proof.md:323:records the information lost in the round trip. Theorem~A
chapters/examples/lattice_foundations.tex:1940:\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
healing_20260413_132214/H14_remove_koszul_locus.md:206:records the information lost in the round trip. Theorem~A
healing_20260413_132214/H14_remove_koszul_locus.md:361:records the information lost in the round trip. Theorem~A
rectification_20260412_233715/R13_introduction.md:278:Theorem~A constructs the bar-cobar adjunction and its Verdier intertwining
chapters/examples/free_fields.tex:1767:Theorem~A$_2$).
codex
The initial grep shows D has a Heisenberg surface already, while A/B/C/H are scattered across other example files and may not be worked through in a single Heisenberg lane. I’m reading the Heisenberg and free-field example files now to check which theorem verifications are explicit versus only name-dropped.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "(Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:bar-cobar-inversion-qi|thm:quantum-complementarity-main|thm:modular-characteristic|thm:main-koszul-hoch|thm:hochschild-polynomial-growth)" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "(Theorem~H|thm:main-koszul-hoch|thm:hochschild-polynomial-growth|prop:chirhoch1-affine-km|ChirHoch|Hochschild)" chapters/examples/heisenberg_eisenstein.tex chapters/examples/free_fields.tex chapters/examples/lattice_foundations.tex chapters/examples/genus_expansions.tex chapters/examples/kac_moody.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

% Regime I: quadratic (Convention~\ref{conv:regime-tags}).

\section{The algebra and shadow archetype}
\label{sec:heisenberg-archetype}

The Heisenberg algebra~$\cH_\kappa$ is the Gaussian archetype
(class~G, shadow depth $r_{\max} = 2$). It is the simplest modular
Koszul algebra: the shadow obstruction tower terminates at degree~$2$,
the complementarity potential is exactly quadratic, and the full open/closed
MC element reduces to the scalar modular characteristic~$\kappa$.
All five main theorems (A through~D and~H) are immediate. The genus
expansion is controlled entirely by~$\kappa$ and assembles into the
$\hat{A}$-genus.

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{ll}
\textbf{Algebra} & Heisenberg~$\cH_\kappa$, rank~$1$,
OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ \\
 succeeded in 50ms:
58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
308:the free-field pairing $\kappa_{\mathrm{Heis}} + \kappa_{\mathrm{Heis}}' = 0$ This is the abelian case of Theorem~\ref{thm:modular-characteristic}(iv).
1103:Theorem~\ref{thm:modular-characteristic}(iii).
2362:= F_g(\cH_\kappa)$ which is the genus tower of Theorem~D.
 succeeded in 51ms:
chapters/examples/heisenberg_eisenstein.tex:2348:where the Hochschild homology of the semisimple category
chapters/examples/lattice_foundations.tex:1480:% Section 8: Chiral Hochschild Cohomology
chapters/examples/lattice_foundations.tex:1483:\section{Chiral Hochschild cohomology of lattice algebras}
chapters/examples/lattice_foundations.tex:1486:\begin{theorem}[Lattice Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:lattice:hochschild}
chapters/examples/lattice_foundations.tex:1489:\ChirHoch^n(\Vlat_\Lambda, \Vlat_\Lambda)
chapters/examples/lattice_foundations.tex:1491:\ChirHoch^n(\Vlat_\Lambda, \Vlat_\Lambda^\alpha)
chapters/examples/lattice_foundations.tex:1495:\ChirHoch^n(\Vlat_\Lambda, \Vlat_\Lambda^0)
chapters/examples/lattice_foundations.tex:1511:The chiral Hochschild complex respects this grading:
chapters/examples/lattice_foundations.tex:1522:\ChirHoch^*(\Vlat_\Lambda, \Vlat_\Lambda)
chapters/examples/lattice_foundations.tex:1524:\ChirHoch^*(\Vlat_\Lambda, \Vlat_\Lambda^\alpha).
chapters/examples/lattice_foundations.tex:1533:Hochschild cohomology reduces to:
chapters/examples/lattice_foundations.tex:1535:\ChirHoch^n(\Vlat_\Lambda, \Vlat_\Lambda)
chapters/examples/lattice_foundations.tex:1542:When $\Lambda$ is unimodular, $D(\Lambda) = \Lambda^*/\Lambda = 0$, so the discriminant contributions vanish and the chiral Hochschild complex reduces to the group cohomology complex $C^*(\Lambda, \mathbb{C})$ by the preceding theorem.
chapters/examples/lattice_foundations.tex:1545:\begin{example}[\texorpdfstring{$A_1$}{A1} Hochschild cohomology]\label{ex:lattice:hochschild-A1}
chapters/examples/lattice_foundations.tex:1555:Hence $\ChirHoch^n(\Vlat_{A_1}, \Vlat_{A_1})$ is concentrated
chapters/examples/lattice_foundations.tex:4881:\subsection{$\Eone$ Hochschild cohomology for quantum lattice VOAs}
chapters/examples/lattice_foundations.tex:4884:The $\Einf$ Hochschild cohomology of lattice VOAs decomposes by lattice
chapters/examples/lattice_foundations.tex:4891:\begin{conjecture}[$\Eone$ lattice Hochschild cohomology;
chapters/examples/lattice_foundations.tex:4893:\index{Hochschild cohomology!E1-chiral lattice@$\Eone$-chiral lattice}
chapters/examples/lattice_foundations.tex:4896:\item The $\Eone$-chiral Hochschild cohomology decomposes by lattice sector:
exec
/bin/zsh -lc "sed -n '5420,5485p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
non-binary correction data measured by the Li/PBW filtration.
\end{proof}



\section{Comparison and filtered structures}\label{sec:comparison-filtered}

This final section collects comparison results: the holographic Witten-diagram shadow, the interaction between filtrations and bar complexes, and a summary of the main theorems verified by free-field examples.

\subsection{Comparison of free-field examples}

Geometric complexity correlates inversely with algebraic simplicity: the free fermion (one generator) vanishes above degree~$1$; the $\beta\gamma$ system grows as $2 \cdot 3^{n-1}$; the Heisenberg gains a central charge class; the Virasoro connects to $\overline{\mathcal{M}}_{0,n}$; W-algebras link to flag varieties.

\begin{remark}[Five projections of $\Theta_\cA$: free-field archetypes]
\label{rem:free-field-five-theorems}
\index{main theorems!free field verification}
\index{Chriss--Ginzburg structure principle!free fields}
Each free-field archetype verifies all five main theorems as projections
of the universal MC element
$\Theta_\cA \in \MC(\gAmod)$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3900,3965p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{partition function!genus-1!Kac--Moody}
The genus-1 partition function of $\widehat{\mathfrak{sl}}_{2,k}$ decomposes as:
\begin{equation}\label{eq:sl2-genus1-partition}
Z_1(\widehat{\mathfrak{sl}}_{2,k}|\tau) = \frac{\chi(\mathfrak{sl}_2)}{\eta(\tau)^3} \cdot \bigl(1 + (k+2) \cdot E_2(\tau) + O(E_4)\bigr)
\end{equation}
where $\chi(\mathfrak{sl}_2)$ is the $\mathfrak{sl}_2$ character, $\eta(\tau)$ is the Dedekind eta function, and $E_2(\tau)$ is the (quasi-modular) Eisenstein series of weight~$2$.

The appearance of $E_2$ (rather than the modular $E_4$ or $E_6$) is forced by the quasi-periodicity~\eqref{eq:B-cycle-quasi-periodicity}: the same $B$-cycle monodromy that produces the curvature $(k+2) \cdot \omega_1$ also produces the $E_2$ coefficient in the partition function.
\end{proposition}

\begin{proof}
The genus-1 contribution to the partition function is computed by the supertrace over the bar complex:
\begin{equation}
Z_1 = \operatorname{Str}_{\barB^{(1)}} q^{L_0 - c/24}
\end{equation}
where $c = 3k/(k+2)$ is the central charge of $\widehat{\mathfrak{sl}}_{2,k}$ and $q = e^{2\pi i \tau}$.

The leading contribution comes from the three free currents $e, f, h$, each of conformal weight~$1$, giving the denominator $\eta(\tau)^{-3}$ (three bosonic oscillators). The first correction involves one propagator insertion and arises from the genus-1 Feynman diagram with a single loop (Theorem~\ref{thm:km-higher-genus-corrections}):
\begin{equation}
\delta Z_1 = (k+h^\vee) \cdot \sum_{a} \oint_{E_\tau} K^{(1)}(z,z|\tau) \cdot J^a(z) J_a(z)\, dz
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~H" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/yangians_foundations.tex:1012:ring (Theorem~H). Their $\Eone$ formulations require the following
exec
/bin/zsh -lc 'rg -n "bar complex|bar-cobar|cobar|complementarity|Hochschild|bulk|derived center|center|dual|Koszul dual|Theorem~D|Theorem~H|Theorem~C|Theorem~B|Theorem~A" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\section|\\\\subsection|\\\\begin\\{theorem\\}|\\\\begin\\{proposition\\}|\\\\begin\\{example\\}|\\\\begin\\{corollary\\}\" chapters/examples/heisenberg_eisenstein.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
10:the complementarity potential is exactly quadratic, and the full open/closed
16:\begin{center}
24:\textbf{Koszul dual} & $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$,
30:\end{center}
43:The Koszul dual $\cH_\kappa^! =
45:chiral algebra on the dual space (not isomorphic to~$\cH_\kappa$
49:The Heisenberg bar complex at genus~$0$
58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
63:bar complex, shadow obstruction tower, and modular characteristic}
143:(ii)~the Heisenberg Lie algebra with bar complex
235:\section{Extract projections: \texorpdfstring{$r$}{r}-matrix, complementarity,
236:genus expansion, bulk, lines}
270:\begin{remark}[Pole absorption and the pre-dualisation distinction]
281:The collision residue $r(z) = \kappa/z$ is a post-extraction object: it is the $r$-matrix of the bar complex after $d\log$~absorption. The pre-extraction (``pre-dualisation'') singular OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ has one higher pole order and is not to be confused with $r(z)$.
285:\label{subsec:heisenberg-complementarity}
286:\index{Heisenberg algebra!complementarity}
288:\begin{proposition}[Heisenberg complementarity; \ClaimStatusProvedHere]
289:\label{prop:heisenberg-complementarity}
290:The Heisenberg algebra and its Koszul dual satisfy exact
291:complementarity:
 succeeded in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '850,940p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
$R$-matrix on $V(a) \otimes V(b)$ is:
\[
R(u) = \frac{u - \hbar P}{u}
= \begin{pmatrix}
1 - \frac{\hbar}{u} & 0 & 0 & 0 \\
0 & 1 & \frac{-\hbar}{u} & 0 \\
0 & \frac{-\hbar}{u} & 1 & 0 \\
0 & 0 & 0 & 1 - \frac{\hbar}{u}
\end{pmatrix}
\quad\text{at } u = a-b,
\]
The tensor product $V(a) \otimes V(b)$ decomposes as
$\mathrm{Sym}^2(V) \oplus \bigwedge^2(V)$ when $a \neq b$
(generic), and is indecomposable when $a = b$ (the $R$-matrix
has a pole). Under Koszul duality,
$V(a) \otimes V(b) \mapsto V(-a) \otimes V(-b)$ with the
$R$-matrix $R(u) \mapsto R^{-1}(u)$: the $R$-matrix eigenvalues
on $\mathrm{Sym}^2(V)$ and $\bigwedge^2(V)$ are inverted.
\end{example}

exec
/bin/zsh -lc 'rg -n "Theorem~[ABCDH]" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
2362:= F_g(\cH_\kappa)$ which is the genus tower of Theorem~D.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '650,780p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

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
The free energy $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ is the
\emph{Euler characteristic} of a much richer object. For
$\widehat{\mathfrak{sl}}_{2,k}$ at integrable level, the
factorization homology $\int_{\Sigma_g}\!\widehat{\mathfrak{sl}}_{2,k}$
is a vector bundle over $\mathcal{M}_g$, the \emph{Verlinde bundle}
(or bundle of conformal blocks), whose rank is given by the
exec
/bin/zsh -lc "sed -n '2320,2395p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where $\{|\mu\rangle\}$ is an orthonormal basis of Fock states.

At the one-particle level, the self-loop sewing operator is
$\sewop_q$ on a single copy of $A^2(D)$, and the trace is
$\operatorname{Tr}_{\mathrm{Sym}}(\secquant(\sewop_q)^\kappa)
= \det(1 - \sewop_q)^{-\kappa}$. At genus~$1$
(one pair of pants with a self-loop), this gives
$Z_1 = \det(1 - \sewop_q)^{-\kappa}
= \prod_{n=1}^\infty (1 - q^n)^{-\kappa}
= (q^{-1/24}\,\eta(q))^{-\kappa}$,
reproducing the Heisenberg partition function
(Theorem~\ref{thm:heisenberg-one-particle-sewing}).

This is the categorical trace $\operatorname{Tr}_{\Cop}$ on the
dualizable category $\Cop(\cH_\kappa)$
(Proposition~\ref{prop:heisenberg-open-sector}(iii)): the
non-separating degeneration creates a handle by identifying two
boundary circles, which is precisely the categorical trace
operation $\operatorname{Tr}\colon \operatorname{End}(\cF_\lambda)
\to \operatorname{End}(\cF_\lambda)$. Agreement with the annulus
codex
I found a natural Heisenberg host: `chapters/examples/heisenberg_eisenstein.tex` already carries D and C-adjacent material, but A/B/H are not explicit there. I’m checking whether `free_fields.tex` already counts as a worked Heisenberg verification or whether the Heisenberg chapter needs its own compact theorem-by-theorem section.
exec
/bin/zsh -lc "rg -n \"\\\\section|\\\\subsection|\\\\begin\\{theorem\\}|\\\\begin\\{proposition\\}|\\\\begin\\{example\\}|\\\\begin\\{corollary\\}\" chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '284,360p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2320,2385p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
\subsection{Complementarity}
\label{subsec:heisenberg-complementarity}
\index{Heisenberg algebra!complementarity}

\begin{proposition}[Heisenberg complementarity; \ClaimStatusProvedHere]
\label{prop:heisenberg-complementarity}
The Heisenberg algebra and its Koszul dual satisfy exact
complementarity:
\begin{equation}\label{eq:heisenberg-complementarity}
\text{(free-field type~I):}\qquad \kappa_{\mathrm{Heis}}(\cH_\kappa) + \kappa_{\mathrm{Heis}}(\cH_\kappa^!) \;=\; 0 \qquad \text{(not the Virasoro $13$).}
\end{equation}
The dual algebra $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$
is the symmetric chiral algebra on the dual space, with
curvature $m_0 = -\kappa \cdot \omega_1$. At level
$\kappa = 0$ the bar complex is uncurved; at $\kappa \neq 0$ both
$\cH_\kappa$ and $\cH_\kappa^!$ are curved, with opposite
curvatures.
\end{proposition}

\begin{proof}
 succeeded in 52ms:
where $\{|\mu\rangle\}$ is an orthonormal basis of Fock states.

At the one-particle level, the self-loop sewing operator is
$\sewop_q$ on a single copy of $A^2(D)$, and the trace is
$\operatorname{Tr}_{\mathrm{Sym}}(\secquant(\sewop_q)^\kappa)
= \det(1 - \sewop_q)^{-\kappa}$. At genus~$1$
(one pair of pants with a self-loop), this gives
$Z_1 = \det(1 - \sewop_q)^{-\kappa}
= \prod_{n=1}^\infty (1 - q^n)^{-\kappa}
= (q^{-1/24}\,\eta(q))^{-\kappa}$,
reproducing the Heisenberg partition function
(Theorem~\ref{thm:heisenberg-one-particle-sewing}).

This is the categorical trace $\operatorname{Tr}_{\Cop}$ on the
dualizable category $\Cop(\cH_\kappa)$
(Proposition~\ref{prop:heisenberg-open-sector}(iii)): the
non-separating degeneration creates a handle by identifying two
boundary circles, which is precisely the categorical trace
operation $\operatorname{Tr}\colon \operatorname{End}(\cF_\lambda)
\to \operatorname{End}(\cF_\lambda)$. Agreement with the annulus
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem H" chapters/examples' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "Theorem~H" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '5445,5495p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5735,5775p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5496,5535p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\subsubsection{Heisenberg: five-theorem verification}

\begin{computation}[Five projections of $\Theta_{\cH_k}$;
\ClaimStatusProvedHere]
\label{comp:heisenberg-five-theorems}
\index{Heisenberg algebra!five-theorem verification}
Shadow archetype: G (Gaussian, $r_{\max} = 2$).
$\kappa(\cH_k) = k$.
Central charge $c = 1$.
\begin{center}
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
\toprule
\emph{Theorem} & \emph{Projection of $\Theta_{\cH_k}$}
 & \emph{Content} \\
\midrule
A (bar-cobar) &
 $\Theta_{\cH_k}\big|_{\hbar=0} = \tau$ &
 succeeded in 51ms:
$\kappa(\mathcal{F}) = 1/4$.
Central charge $c = 1/2$.
\begin{center}
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lll}
\toprule
\emph{Theorem} & \emph{Projection of $\Theta_{\mathcal{F}}$}
 & \emph{Content} \\
\midrule
A (bar-cobar) &
 $\Theta_\mathcal{F}\big|_{\hbar=0} = \tau$ &
 $\mathcal{F}^! = \mathrm{Sym}^{\mathrm{ch}}(\gamma)$ (Thm~\ref{thm:single-fermion-boson-duality}) \\
B (inversion) &
 $\Omega(\barBgeom(\mathcal{F})) \simeq \mathcal{F}$ &
 Bar collapses (Thm~\ref{thm:fermion-bar-complex-genus-0}) \\
C (complementarity) &
 $\kappa(\mathcal{F}) + \kappa(\mathcal{F}^!) = 0$ &
 Fermionic/bosonic complementarity \\
D (modular char.) &
 succeeded in 51ms:
The isomorphism $\text{Gr}\barBgeom(\mathcal{A}) \cong \barBgeom(\text{Gr}\mathcal{A})$ follows from:
\[\text{Gr}_p(F_{i_0}\mathcal{A} \otimes \cdots \otimes F_{i_n}\mathcal{A}) = \bigoplus_{j_0 + \cdots + j_n = p} \text{Gr}_{j_0}\mathcal{A} \otimes \cdots \otimes \text{Gr}_{j_n}\mathcal{A}\]
\end{proof}

\begin{definition}[Curved filtered algebra]
A \emph{curved filtered chiral algebra} is $(F_\bullet\mathcal{A}, d, m_0)$ where:
\begin{itemize}
\item $d: F_p\mathcal{A} \to F_p\mathcal{A}[1]$ (preserves filtration)
\item $m_0 \in F_0\mathcal{A}[2]$ (curvature in filtration degree 0)
\item $d^2 = [m_0, \cdot]$ (curved differential equation)
\end{itemize}
\end{definition}

\begin{theorem}[Curved Koszul duality \cite{Positselski11}; \ClaimStatusProvedElsewhere]
\label{thm:curved-koszul-duality}
For curved filtered chiral algebras:
\begin{enumerate}
\item The bar complex is a curved coalgebra with curvature $\kappa_C = \bar{m}_0$
\item The cobar of a curved coalgebra is a curved algebra
\item If $\text{Gr}\mathcal{A}$ is Koszul, then:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\(Theorem~H\" chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/yangians_foundations.tex:1012:ring (Theorem~H). Their $\Eone$ formulations require the following
exec
/bin/zsh -lc 'rg -n "bar-cobar" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1010,1050p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
of Theorem~C (complementarity on bordered moduli). Two theorems remain:
the modular characteristic (Theorem~D) and the Hochschild coefficient
ring (Theorem~H). Their $\Eone$ formulations require the following
structural replacements.

\begin{conjecture}[$\Eone$ modular characteristic;
\ClaimStatusConjectured]\label{conj:e1-theorem-D}
\index{modular characteristic!E1-chiral@$\Eone$-chiral}
For an $\Eone$-chiral algebra $\cA$ on an oriented interval, the
genus-$g$ obstruction
$\mathrm{obs}_g^{\Eone}(\cA) \in
H^*(\mathcal{M}_{g,1}^{\partial})$
of Conjecture~\textup{\ref{conj:e1-genus-theory}(iii)} is
controlled by a single invariant $\kappa^{\Eone}(\cA)$ analogous to
the $\Einf$ modular characteristic $\kappa(\cA)$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Universality.}
 $\kappa^{\Eone}(\cA)$ is determined by the leading OPE
 singularity: for the Yangian, the $R$-matrix
 residue $\Res_{u=0}\,R(u) = -\hbar P$.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Hochschild coefficient" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/yangians_foundations.tex:1011:the modular characteristic (Theorem~D) and the Hochschild coefficient
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Hochschild" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:26: $H^2(\Defcyc(\cA))$, the chiral Hochschild cohomology of
chapters/examples/deformation_quantization.tex:141:The higher-genus extension is conjectural (\ClaimStatusConjectured): it requires controlling the global obstructions in $H^2$ of the chiral Hochschild complex on $\overline{\mathcal{M}}_{g,n}$. This remains open.
chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/examples/deformation_quantization.tex:403:More precisely (via the Hochschild deformation complex):
chapters/examples/deformation_quantization.tex:583:\item Right side: Chiral Hochschild cochains (quantum)
chapters/examples/deformation_quantization.tex:585:This follows from the formality of the $E_2$-operad (Kontsevich, Tamarkin \cite{Tamarkin00}) via the factorization algebra formalism of Francis--Gaitsgory. See also Dolgushev--Tamarkin--Tsygan \cite{DTT09} for a systematic treatment of formality for Hochschild complexes.
chapters/examples/deformation_quantization.tex:608:The chiral Hochschild cohomology of the classical chiral algebra controls quantization:
chapters/examples/deformation_quantization.tex:1629:of the Hochschild--Kostant--Rosenberg theorem for dg algebras.
chapters/examples/deformation_quantization.tex:1827:\index{Hochschild--Kostant--Rosenberg!for dg algebras}
chapters/examples/deformation_quantization.tex:1841:$\HH^\bullet$ denotes Hochschild cohomology,
chapters/examples/deformation_quantization.tex:1867:over~$k$). Therefore, the derived Hochschild cohomology equals the
chapters/examples/deformation_quantization.tex:1868:strict Hochschild cohomology:
chapters/examples/deformation_quantization.tex:1874:The Hochschild--Kostant--Rosenberg theorem for dg algebras
chapters/examples/deformation_quantization.tex:1940:The Hochschild cohomology of $k$ is $\HH^\bullet(k) = k$
chapters/examples/deformation_quantization.tex:2118:theory of the singularity $Z_F$. The Hochschild cohomology
chapters/examples/deformation_quantization.tex:2130:(chiral) Hochschild cohomology of the boundary algebra, which
chapters/examples/symmetric_orbifolds.tex:56:H (Hochschild) &
chapters/examples/symmetric_orbifolds.tex:226:\begin{conjecture}[Chiral Hochschild growth;
chapters/examples/symmetric_orbifolds.tex:231:bounded by a function of~$N$ and the Hochschild degree of~$X$.
chapters/examples/lattice_foundations.tex:1480:% Section 8: Chiral Hochschild Cohomology
exec
/bin/zsh -lc 'rg -n "inversion" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

collab wait(call_6nyq9STjOp3iTp4RyOvJRq8e)
  receivers: 019d87b5-7b0b-7283-b0e4-faaea3529774, 019d87b5-7b10-7951-a0de-cbe7799ee5ec
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "coefficient ring" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/heisenberg_eisenstein.tex:719:For general $g$: The structure of the Siegel modular forms ring $M_*(\mathrm{Sp}_{2g}(\mathbb{Z}))$ is finitely presented for $g \leq 3$ by classical results \cite{Freitag83}, and the generators of the ring are known explicitly in those cases. The concrete expansion claimed in this theorem is therefore \emph{complete and rigorous for $g \leq 3$}. For $g \geq 4$, the ring of Siegel modular forms is not fully described, and the assertion about the coefficient ring means that the expansion coefficients lie in the finitely generated subalgebra of $M_*(\mathrm{Sp}_{2g}(\mathbb{Z}))$ determined by the modular weight constraints of Step~3.
exec
/bin/zsh -lc 'rg -n "ChirHoch" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1920,1975p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
19 & $6D_4$ & 144 & 6 & $33984/691$ \\
20 & $6A_4$ & 120 & 5 & $17400/691$ \\
21 & $8A_3$ & 96 & 4 & $816/691$ \\
22 & $12A_2$ & 72 & 3 & $-15768/691$ \\
23 & $24A_1$ & 48 & 2 & $-32352/691$ \\
24 & Leech & 0 & --- & $-65520/691$ \\
\bottomrule
\end{tabular}
\end{table}

\subsection{The three theorems for lattice algebras}

\begin{remark}[Main theorems for lattice VOAs]
\label{rem:lattice-three-theorems}
\index{main theorems!lattice VOA verification}
The computations of this chapter provide an abelian verification of the
main theorems of Part~\ref{part:bar-complex}. Each verification reveals structure invisible
in the abstract theory:

\begin{enumerate}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '40,120p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\operatorname{Sym}^{\mathrm{ch}}(V^*),\;\;
r(z) = \kappa/z\,\bigr).
\end{equation}
The Koszul dual $\cH_\kappa^! =
\operatorname{Sym}^{\mathrm{ch}}(V^*)$ is the curved symmetric
chiral algebra on the dual space (not isomorphic to~$\cH_\kappa$
itself), and the $r$-matrix has a single simple pole
(the $d\log$-absorbed residue of the double-pole OPE).

The Heisenberg bar complex at genus~$0$
(Chapter~\ref{ch:heisenberg-frame}) is controlled by the logarithmic
propagator $d\log(z-w)$. At higher genus, the propagator acquires
corrections from the period matrix: near the diagonal,
the Green's function on a genus-$g$ surface decomposes as
$G(z,w) = \log(z-w) + \sum_{k \geq 1} c_k(\Omega)\,(z-w)^{2k}$,
with Taylor coefficients $c_k(\Omega)$ equal to the
Eisenstein series $G_{2k}$. These enter the bar
differential as genus corrections. The Heisenberg is the simplest
nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
$\hat{A}$-genus shape, verifiable term by
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '30,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    30	\end{center}
    31	
    32	\noindent
    33	The modular Koszul triple
    34	(Definition~\ref{def:modular-koszul-triple}) of the Heisenberg
    35	algebra is
    36	\begin{equation}\label{eq:heisenberg-triple}
    37	\mathfrak{T}_{\cH}
    38	\;=\;
    39	\bigl(\,\cH_\kappa,\;\;
    40	\operatorname{Sym}^{\mathrm{ch}}(V^*),\;\;
    41	r(z) = \kappa/z\,\bigr).
    42	\end{equation}
    43	The Koszul dual $\cH_\kappa^! =
    44	\operatorname{Sym}^{\mathrm{ch}}(V^*)$ is the curved symmetric
    45	chiral algebra on the dual space (not isomorphic to~$\cH_\kappa$
    46	itself), and the $r$-matrix has a single simple pole
    47	(the $d\log$-absorbed residue of the double-pole OPE).
    48	
    49	The Heisenberg bar complex at genus~$0$
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5410,5480p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5410	\end{theorem}
  5411	
  5412	\begin{proof}
  5413	The existence of the higher operations $m_k$ is
  5414	Theorem~\ref{thm:w-algebra-ainfty}. The classical binary
  5415	Drinfeld--Sokolov integrable structure is the content of
  5416	Theorem~\ref{thm:w-classical-integrability}. Passing from the
  5417	classical Poisson algebra to the quantum $\mathcal{W}$-algebra
  5418	introduces the higher multilinear operations supplied by the
  5419	bar-side $A_\infty$ structure; these higher terms are exactly the
  5420	non-binary correction data measured by the Li/PBW filtration.
  5421	\end{proof}
  5422	
  5423	
  5424	
  5425	\section{Comparison and filtered structures}\label{sec:comparison-filtered}
  5426	
  5427	This final section collects comparison results: the holographic Witten-diagram shadow, the interaction between filtrations and bar complexes, and a summary of the main theorems verified by free-field examples.
  5428	
  5429	\subsection{Comparison of free-field examples}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '180,230p' chapters/examples/symmetric_orbifolds.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\sigma_h \cdot \sigma_{(gh)^{-1}} \rangle$ on the torus
factorizes through the untwisted OPE at leading order, and
the twist-field contribution to the three-point obstruction
class vanishes by $\mathfrak{sl}_2$-charge conservation in
the covering space. At degree~$4$, the four-point twist-field
correlator on the genus-$1$ surface has a nontrivial connected
component controlled by the Lunin--Mathur covering-space
technology \cite{LuninMathur2001}: the $N$-sheeted branched
cover introduces contact terms proportional to
$c(X) \cdot N$ that contribute to the quartic resonance
class~$Q$.
\end{remark}

The five main theorems for $\operatorname{Sym}^N(X)$ have mixed
status: Theorem~D is proved (Proposition~\ref{prop:symn-kappa}),
while A, B, C, H remain conjectural in full generality.

\begin{conjecture}[Orbifold Koszul duality;
\ClaimStatusConjectured]\label{conj:symn-koszul-dual}
\index{symmetric orbifold!Koszul dual}
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5480,5540p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5480	\end{center}
  5481	The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
  5482	= \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
  5483	for all $r \geq 2$. No cubic, quartic, or higher shadows.
  5484	All higher $L_\infty$ brackets vanish:
  5485	$\ell_k^{\mathrm{tr}} = 0$ for $k \geq 3$.
  5486	The modular convolution algebra $\gAmod$ is strictly formal.
  5487	\end{computation}
  5488	
  5489	\subsubsection{Free fermion: five-theorem verification}
  5490	
  5491	\begin{computation}[Five projections of $\Theta_{\mathcal{F}}$;
  5492	\ClaimStatusProvedHere]
  5493	\label{comp:fermion-five-theorems}
  5494	\index{free fermion!five-theorem verification}
  5495	Shadow archetype: G (Gaussian, $r_{\max} = 2$).
  5496	$\kappa(\mathcal{F}) = 1/4$.
  5497	Central charge $c = 1/2$.
  5498	\begin{center}
  5499	\small
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~H"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 4034

healing_20260413_132214/H05_thm_H_alt_proof.md:313:Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
healing_20260413_132214/H05_thm_H_alt_proof.md:407:   801	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
healing_20260413_132214/H05_thm_H_alt_proof.md:665:   675	which is the comparison used in Theorem~H.
healing_20260413_132214/H05_thm_H_alt_proof.md:902:   839	 \textup{(}Theorem~H\textup{)}.
healing_20260413_132214/H05_thm_H_alt_proof.md:921:  2365	 \textbf{Theorem~H}: $\ChirHoch^*(\cA)$ polynomial of amplitude
healing_20260413_132214/H05_thm_H_alt_proof.md:977:  2690	This is Theorem~\ref{thm:main-koszul-hoch} (Theorem~H), proved
healing_20260413_132214/H05_thm_H_alt_proof.md:1045:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1083:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1133:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1175:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1225:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1267:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1329:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1371:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1443:+for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1485:-Theorem~H says that the chiral deformation problem on a curve is a
healing_20260413_132214/H05_thm_H_alt_proof.md:1522:-for the connected examples of Theorem~H this is the scalar identity
healing_20260413_132214/H05_thm_H_alt_proof.md:1526:+center; for the connected examples of Theorem~H this is the scalar
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Vol~I Theorem~H" chapters/examples' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Hochschild" chapters/examples | head' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/deformation_quantization.tex:26: $H^2(\Defcyc(\cA))$, the chiral Hochschild cohomology of
chapters/examples/deformation_quantization.tex:141:The higher-genus extension is conjectural (\ClaimStatusConjectured): it requires controlling the global obstructions in $H^2$ of the chiral Hochschild complex on $\overline{\mathcal{M}}_{g,n}$. This remains open.
chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/examples/deformation_quantization.tex:403:More precisely (via the Hochschild deformation complex):
chapters/examples/deformation_quantization.tex:583:\item Right side: Chiral Hochschild cochains (quantum)
chapters/examples/deformation_quantization.tex:585:This follows from the formality of the $E_2$-operad (Kontsevich, Tamarkin \cite{Tamarkin00}) via the factorization algebra formalism of Francis--Gaitsgory. See also Dolgushev--Tamarkin--Tsygan \cite{DTT09} for a systematic treatment of formality for Hochschild complexes.
chapters/examples/deformation_quantization.tex:608:The chiral Hochschild cohomology of the classical chiral algebra controls quantization:
chapters/examples/deformation_quantization.tex:1629:of the Hochschild--Kostant--Rosenberg theorem for dg algebras.
chapters/examples/deformation_quantization.tex:1827:\index{Hochschild--Kostant--Rosenberg!for dg algebras}
chapters/examples/deformation_quantization.tex:1841:$\HH^\bullet$ denotes Hochschild cohomology,
exec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	
     2	% Regime I: quadratic (Convention~\ref{conv:regime-tags}).
     3	
     4	\section{The algebra and shadow archetype}
     5	\label{sec:heisenberg-archetype}
     6	
     7	The Heisenberg algebra~$\cH_\kappa$ is the Gaussian archetype
     8	(class~G, shadow depth $r_{\max} = 2$). It is the simplest modular
     9	Koszul algebra: the shadow obstruction tower terminates at degree~$2$,
    10	the complementarity potential is exactly quadratic, and the full open/closed
    11	MC element reduces to the scalar modular characteristic~$\kappa$.
    12	All five main theorems (A through~D and~H) are immediate. The genus
    13	expansion is controlled entirely by~$\kappa$ and assembles into the
    14	$\hat{A}$-genus.
    15	
    16	\begin{center}
    17	\renewcommand{\arraystretch}{1.3}
    18	\begin{tabular}{ll}
    19	\textbf{Algebra} & Heisenberg~$\cH_\kappa$, rank~$1$,
    20	OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ \\
wait(call_6nyq9STjOp3iTp4RyOvJRq8e) timed out:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~H" -n chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/yangians_foundations.tex:1012:ring (Theorem~H). Their $\Eone$ formulations require the following

thinking
**Reflecting on lattice foundations**

I think I might need to conduct a poll later, but for now, I should manually inspect some examples related to lattice_foundations. Maybe I should create an explicit list with A, B, and C, but why not include H? I guess it’s just not fitting. So, I’ll take a closer look around line 1930 to see what’s going on there. Let’s figure this out and see what insights I can gather!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/kac_moody.tex | sed -n '3860,3960p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3860	\begin{equation}
  3861	Q_1(\widehat{\mathfrak{sl}}_{2,k}) = \mathbb{C} \cdot (k+2) \subset H^0(\overline{\mathcal{M}}_{1,1})
  3862	\end{equation}
  3863	
  3864	\emph{Step~2: Identify $Q_1(\widehat{\mathfrak{sl}}_{2,-k-4})$.}
  3865	The Koszul dual $(\widehat{\mathfrak{sl}}_{2,k})^! = \widehat{\mathfrak{sl}}_{2,-k-4}$ (Theorem~\ref{thm:sl2-koszul-dual}) has shifted level $k^* = -k-4$. Repeating the curvature computation with $k$ replaced by $k^*$:
  3866	\begin{equation}
  3867	(d^{(1)}_!)^2 = (k^* + 2) \cdot \omega_1 \cdot \operatorname{id} = (-k-2) \cdot \omega_1 \cdot \operatorname{id}
  3868	\end{equation}
  3869	This is again non-zero for $k \neq -2$, confirming that the dual algebra also has a one-dimensional genus-1 obstruction:
  3870	\begin{equation}
  3871	Q_1(\widehat{\mathfrak{sl}}_{2,-k-4}) = \mathbb{C} \cdot (-k-2) \subset H^0(\overline{\mathcal{M}}_{1,1})
  3872	\end{equation}
  3873	
  3874	\emph{Step~3: Complementarity via the Kodaira--Spencer map.}
  3875	By the Kodaira--Spencer construction (Theorem~\ref{thm:kodaira-spencer-chiral-complete}), the Verdier involution $\sigma$ on $H^*(\overline{\mathcal{M}}_{1,1}, Z(\cA))$ exchanges the degree-0 and degree-2 components. Explicitly, $\sigma$ is defined via the Verdier duality pairing on $\overline{\mathcal{M}}_{1,1}$:
  3876	\begin{equation}
  3877	\sigma: H^0(\overline{\mathcal{M}}_{1,1}) \xrightarrow{\;\sim\;} H^2(\overline{\mathcal{M}}_{1,1}), \quad 1 \mapsto \lambda
  3878	\end{equation}
  3879	
codex
I found an existing Heisenberg five-theorem summary table in `free_fields.tex`, but it is mostly a projection ledger, not a worked derivation. I’m checking whether the chapter set already contains theorem-by-theorem worked proofs somewhere else; if not, I’ll add a compact Heisenberg worked-example subsection rather than duplicating full proofs.
exec
/bin/zsh -lc "sed -n '1928,1975p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,470p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1480,1565p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{table}

\subsection{The three theorems for lattice algebras}

\begin{remark}[Main theorems for lattice VOAs]
\label{rem:lattice-three-theorems}
\index{main theorems!lattice VOA verification}
The computations of this chapter provide an abelian verification of the
main theorems of Part~\ref{part:bar-complex}. Each verification reveals structure invisible
in the abstract theory:

\begin{enumerate}
\item \emph{Theorem~A} (Theorem~\ref{thm:bar-cobar-isomorphism-main}).
 Applied to $\Vlat_\Lambda$, the bar-cobar adjunction shows
 that the lattice bar complex concentrates in
 conformal-weight-graded degrees, with the concentration pattern
 governed by the root system of $\Lambda$
 (Theorem~\ref{thm:lattice:bar-structure}). The Koszul dual is
 identified as the lattice algebra with inverse cocycle
 (Theorem~\ref{thm:lattice:koszul-dual}), so the duality is
 succeeded in 51ms:
Recall from the Master Table (Table~\ref{tab:master-invariants}) the Koszul duality data for $\widehat{\mathfrak{sl}}_2$:
\begin{center}
\renewcommand{\arraystretch}{1.4}
\begin{tabular}{lllll}
\toprule
Algebra & Koszul Dual & $c(\cA)$ & $c + c'$ & $\kappa(\cA)$ \\
\midrule
$\widehat{\mathfrak{sl}}_{2,k}$ & $\widehat{\mathfrak{sl}}_{2,-k-4}$ & $\dfrac{3k}{k+2}$ & $6$ & $\dfrac{3(k+2)}{4}$ \\[6pt]
\bottomrule
\end{tabular}
\end{center}
The Feigin--Frenkel involution $k \mapsto k' = -k - 2h^\vee = -k-4$ acts on the central charge as $c \mapsto c' = 6 - c$, and on the obstruction coefficient as $\kappa \mapsto -\kappa$.

\begin{itemize}
\item \emph{Theorem~A} (Geometric Bar-Cobar Duality, Theorem~\ref{thm:bar-cobar-isomorphism-main}; this is Theorem~$\mathrm{A}_2$ in the $\mathrm{A}_0/\mathrm{A}_1/\mathrm{A}_2$ decomposition of Remark~\ref{rem:theorem-A-decomposition}):
$(\widehat{\mathfrak{sl}}_{2,k})^! \simeq
\widehat{\mathfrak{sl}}_{2,-k-4}$ via bar construction and Verdier
duality on configuration space integrals. The bar coalgebra
$\bar{B}(\widehat{\mathfrak{sl}}_{2,k})$ is a factorization
coalgebra on~$\mathrm{Ran}(X)$; Verdier duality
 succeeded in 51ms:
% Section 8: Chiral Hochschild Cohomology
% ======================================================================

\section{Chiral Hochschild cohomology of lattice algebras}
\label{sec:lattice:hochschild}

\begin{theorem}[Lattice Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:lattice:hochschild}
For an even integral lattice $\Lambda$:
\begin{equation}\label{eq:lattice:hochschild}
\ChirHoch^n(\Vlat_\Lambda, \Vlat_\Lambda)
\;=\; \bigoplus_{\alpha \in \Lambda}
\ChirHoch^n(\Vlat_\Lambda, \Vlat_\Lambda^\alpha)
\end{equation}
and the degree-zero component ($\alpha = 0$) is:
\[
\ChirHoch^n(\Vlat_\Lambda, \Vlat_\Lambda^0)
\;\cong\; H^n(\Lambda, \Vlat_\Lambda^{\Lambda})
\]
where $\Vlat_\Lambda^\Lambda = \Vlat_\Lambda^0 = \cH$ denotes the
$\Lambda$-invariants (the degree-zero sector under the lattice grading)

thinking
**Inspecting theorems and results**

I'm thinking I need to check the theorem registry lines, but maybe that's enough already. I should take a closer look at the explorer results as well. Hmm, I might need to wait a bit longer to see if it's still running. There’s a lot to consider, and I want to make sure I'm thorough in gathering the right information!
collab wait(call_OcwW769RgHsazHQQ2r6NntTb)
  receivers: 019d87b5-7b0b-7283-b0e4-faaea3529774, 019d87b5-7b10-7951-a0de-cbe7799ee5ec


thinking
**Summarizing recommended files and anchors**

I'll provide a clear, structured summary listing the best files to add worked examples for Theorems A, B, C, D, H, including precise insertion anchors with line numbers and labels from `heisenberg_eisenstein.tex` and `free_fields.tex`. I'll also outline local conventions like preserving `\ClaimStatusProvedHere`, maintaining `\index` entries, and respecting existing styles, so the user has a full guide without editing instructions.
thinking
**Summarizing theorem verification references**

I’m gathering line references and evidence sentences to build a clear table of which theorems have verifying examples in the repo. I’ll list Theorems A, B, C as verified by the Kac-Moody remark at lines 3932-3939, and Theorem D verified by the Heisenberg example around lines 33-60. For Theorem H, I confirm there’s no explicit example, so I’ll note that gap too. The goal is a straightforward plain-text table capturing theorem, example presence, family, file with line range, labels, and short evidence sentences, followed by a brief gap list.
Plan update
  ✓ Inventory chapters/examples directory to find files referencing Theorems A-D,H
  ✓ Inspect identified files for worked examples, note families and references
  → Summarize findings in table and gap list
codex
1) **Recommended Files**  
- `chapters/examples/heisenberg_eisenstein.tex` — entire chapter is Heisenberg-centric, already links the modular triple (eq.~\ref{eq:heisenberg-triple}) to the bar complex, complementarity, genus tower, and the open/closed MC, so it’s the canonical place to flesh out worked instances of Theorems A, B, C, D, and H while keeping the narrative self-contained.  
- `chapters/examples/free_fields.tex` — the subsection “Heisenberg: five-theorem verification” (`\label{comp:heisenberg-five-theorems}`) explicitly lists the projections for A–H and is already structured as a computation, making it ideal for concrete, tabulated worked examples that expand on each theorem in a uniform format.

2) **Insertion Anchors**  
- **Theorem A (bar-cobar adjunction)**: add a short worked example just after the modular Koszul triple paragraph in `chapters/examples/heisenberg_eisenstein.tex:4-46` (Section “The algebra and shadow archetype”, right after `\label{eq:heisenberg-triple}`) to show `\Theta|_{\hbar=0}=\tau` and identify the curved dual `\Sym^{\mathrm{ch}}(V^*)`.  
- **Theorem B (inversion)**: expand the discussion in `chapters/examples/heisenberg_eisenstein.tex:62-116` (Section `\label{sec:heisenberg-theta-oc}` and Proposition `\ref{prop:heisenberg-gaussian-termination}`) with a numerical bar/cobar inversion check (e.g., `\Omega(\barBgeom(\cH_\kappa))\simeq\cH_\kappa` at genus 0) to illustrate the quasi‑isomorphism of Theorem B.  
- **Theorem C (complementarity)**: insert a worked outline in `chapters/examples/heisenberg_eisenstein.tex:19-30` where complementarity is first mentioned, showing the explicit `\kappa + \kappa^! = 0` cancellation and how the shadow weight 2 tower collapses.  
- **Theorem D (genus tower)**: weave a detailed example into the same section (lines 58-60) and again around the “Compute \Theta^{\mathrm{oc}}” segment (lines 2320-2385) where `\Theta|_g = \kappa\cdot\lambda_g^{\mathrm{FP}}`, linking the Eisenstein coefficients to the universal generating function that Theorem D guarantees.  
- **Theorem H (Hochschild)**: around `chapters/examples/heisenberg_eisenstein.tex:2320-2400` (the “closed-sector compatibility” and `\eqref{eq:heisenberg-annulus-trace-agreement}` discussion), add an explicit computation showing how `HH_*(\Cop(\cH_\kappa))` collapses to the polynomial ChirHoch complex predicted by Theorem H.  
- **Aggregate location**: the `\subsubsection{Heisenberg: five-theorem verification}` block in `chapters/examples/free_fields.tex:5446-5487` is the ready-made locus for worked examples for all five theorems; after the table (lines 5463-5477) add per-theorem paragraphs or mini-computations that reference the same table entries and cite the relevant main-theorem numbers.

3) **Local Conventions to Preserve**  
- Continue using the existing `\begin{computation}`/`\\end{computation}` wrappers with `\ClaimStatusProvedHere` (or the appropriate status) whenever you add worked examples/listings, so the provenance macros stay consistent.  
- Keep `\index{…}` entries for any new mathematical objects or theorems introduced, matching the current indexing practice around the Heisenberg sections.  
- Respect the established notation (`\kappa`, `F_g`, `\Theta`, `\lambda_g^{\mathrm{FP}}`, etc.) and the current table formatting (`\renewcommand{\arraystretch}{1.3}`, `\toprule`/`\bottomrule`) when expanding the verification block.  
- Tie each worked example back to the exact main-theorem reference already in place (e.g., Theorem~\ref{thm:mc2-bar-intrinsic}, Theorem~\ref{thm:bar-cobar-inversion-qi}, Theorem~\ref{thm:thqg-annulus-trace}), so the new material stays grounded in the existing cross-references.
wait(call_OcwW769RgHsazHQQ2r6NntTb) 1 agents complete:
  019d87b5-7b10-7951-a0de-cbe7799ee5ec completed: "1) **Recommended Files**  
- `chapters/examples/heisenberg_eisenstein.tex` — entire chapter is Heisenberg-centric, alrea…"

collab wait(call_Lxa9xrNwwtB5ENXKMbjkaTEH)
  receivers: 019d87b5-7b0b-7283-b0e4-faaea3529774
thinking
**Summarizing theorems with evidence table**

I'm preparing a concise table listing Theorems A, B, C, D, and H with columns for example presence, family, file path with line ranges, labels, and brief evidence sentences from relevant files. I'll note Theorem H lacks a worked example and add a gap list highlighting that. Afterward, I'll mark plan step 3 as completed.
Plan update
  ✓ Inventory chapters/examples directory to find files referencing Theorems A-D,H
  ✓ Inspect identified files for worked examples, note families and references
  ✓ Summarize findings in table and gap list
codex
Theorem | Example? | Family | File (lines) | Labels | Evidence
---|---|---|---|---|---
A | Y | affine $\widehat{\mathfrak{sl}}_{2,k}$ at genus 1 | `chapters/examples/kac_moody.tex:3932-3939` | `rem:sl2-three-theorems` | Remark states Theorem A is realized by the genus-1 bar complex on $E_\tau$ with the propagator $K^{(1)}=\theta_1'/\theta_1$, closing the loop on the bar-cobar duality for this family.
B | Y | affine $\widehat{\mathfrak{sl}}_{2,k}$ at genus 1 | `chapters/examples/kac_moody.tex:3932-3939` | `rem:sl2-three-theorems` | Same remark records that Theorem B holds by the $E_2$-spectral-sequence collapse at generic level, giving the bar-cobar inversion for $\widehat{\mathfrak{sl}}_{2,k}$.
C | Y | affine $\widehat{\mathfrak{sl}}_{2,k}$ at genus 1 | `chapters/examples/kac_moody.tex:3932-3939` | `rem:sl2-three-theorems` | The complementarity sum $Q_1(\widehat{\mathfrak{sl}}_{2,k})\oplus Q_1(\widehat{\mathfrak{sl}}_{2,-k-4})=H^*(\overline{\mathcal{M}}_{1,1})$ is listed, so Theorem C is verified via the Kodaira–Spencer pairing in the same remark.
D | Y | Heisenberg family $\cH_\kappa$ | `chapters/examples/heisenberg_eisenstein.tex:33-60` | — | The text explains that the Heisenberg bar complex’s genus corrections and Eisenstein expansion realize Theorem D: $\kappa$ controls the universal generating function (with $\hat A$ shape) term-by-term, so the scalar genus tower is explicit.
H | N | none found | (only cross-reference mention) `chapters/examples/yangians_foundations.tex:1003-1020` | — | The Yangian remark notes Theorem H (Hochschild coefficient ring) is still pending an $\Eone$ formulation, and I could not find any worked example in `chapters/examples/` that actually verifies Theorem H for a family.

Gap list:
- Theorem H currently lacks any explicit worked example in `chapters/examples/`; the only mention is that Yangian geometry needs an $\Eone$ substitute for the Hochschild coefficient ring.
wait(call_Lxa9xrNwwtB5ENXKMbjkaTEH) 1 agents complete:
  019d87b5-7b0b-7283-b0e4-faaea3529774 completed: "Theorem | Example? | Family | File (lines) | Labels | Evidence
---|---|---|---|---|---
A | Y | affine $\widehat{\mathfra…"


thinking
**Analyzing worked examples**

I'm thinking that "H gap" might still refer to Heisenberg, and I need to check if theorems A-D have worked examples. It seems A, B, and C might be in the free_fields table, but maybe they're lacking a derivation. The user could be asking for a worked example for Heisenberg if no specific examples exist in the chapters. I'll need to clarify which theorems have examples and ensure Heisenberg gets one if it’s missing. Additionally, the user mentioned fixing issues in one pass.
thinking
**Identifying gaps and issues**

I need to document each finding by specifying the problem with details like the file and line number, followed by the exact edit applied. My focus will be on identifying any gaps or issues in the existing scope and then fixing them. For example, I might address the H gap by including a worked example for Heisenberg. Additionally, I should check if the free_fields Heisenberg summary table properly cites theorem H labels or uses vague language like "Degree-preserving sub-MC." An audit within the assigned scope is necessary to catch any further issues in this area.
exec
/bin/zsh -lc "sed -n '5188,5245p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3928,3943p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,95p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{proof}

\subsection{The three theorems for affine Kac--Moody algebras}

\begin{remark}[Verification for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k} at genus 1]
\label{rem:sl2-three-theorems}
\index{main theorems!genus-1 verification}
The three main theorems are verified at genus~$1$ for $\widehat{\mathfrak{sl}}_{2,k}$: Theorem~A via the bar complex on $E_\tau$ with propagator $K^{(1)} = \theta_1'/\theta_1$ (Theorem~\ref{thm:km-higher-genus-corrections}); Theorem~B via $E_2$-collapse for generic $k$ (Theorem~\ref{thm:sl2-genus1-inversion}); and Theorem~C via
\[
Q_1(\widehat{\mathfrak{sl}}_{2,k}) \oplus Q_1(\widehat{\mathfrak{sl}}_{2,-k-4}) = H^*(\overline{\mathcal{M}}_{1,1})
\]
(Theorem~\ref{thm:sl2-genus1-complementarity}). All four genus-1 invariants are controlled by $k + h^\vee = k + 2$, manifesting the prism principle (Corollary~\ref{cor:prism-principle}).
\end{remark}

\section{\texorpdfstring{Genus-1 pipeline for $\widehat{\mathfrak{sl}}_3$: rank-2 verification}{Genus-1 pipeline for sl-3: rank-2 verification}}
\label{sec:sl3-genus-one-pipeline}
 succeeded in 52ms:
Differentiate the critical-level cubic action:
$dS(a) = \tfrac{1}{2}[a,a] + O(a^3)$. The cubic truncation of
$\mathrm{Crit}(S)$ is therefore $\{a : [a,a] = 0\}$, the
Maurer--Cartan locus. Any relation to critical opers is indirect
and mediated by the separate bar-cohomological theorem
Theorem~\ref{thm:oper-bar-h0}; the present conjecture does not
identify the Maurer--Cartan locus with the oper space.
\end{remark}

\begin{conjecture}[SC deformation complex at critical level;
\ClaimStatusConjectured]\label{conj:sc-deformation-critical}
\index{critical level!SC deformation complex}
\index{Swiss-cheese!critical level deformation}
At the critical level $k = -h^\vee$ for $\fg$ simple of rank~$r$
with exponents $m_1 \le \cdots \le m_r$, the SC deformation complex
governing the chiral Swiss-cheese pair
$\bigl(\ChirHoch^*(\widehat{\fg}_{-h^\vee}),\, \widehat{\fg}_{-h^\vee}\bigr)$
exhibits the following structure:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Degree-$0$ jump)}\quad
 succeeded in 52ms:
\chapter{Affine Kac--Moody algebras}\label{chap:kac-moody-koszul}
\label{chap:kac-moody}

The Heisenberg algebra is abelian: its shadow tower terminates at
degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
The first nonabelian chiral algebra is
$\widehat{\mathfrak{g}}_k$, and the question that
governs this chapter is whether the Lie bracket destroys the
finiteness of the obstruction tower or preserves it.
%
It preserves it. The Lie bracket of~$\fg$ appears as the
cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
degree~$3$; the Jacobi identity forces the quartic shadow to vanish;
the tower terminates (class~$L$, $r_{\max} = 3$). Gauge symmetry
introduces noncommutativity but not infinite obstruction complexity:
the structure constants of~$\fg$ produce exactly one new shadow
beyond the Gaussian, and the Jacobi identity is the mechanism that
kills the rest. This is the content of the assertion that gauge
theory is simpler than gravity; for the Virasoro algebra
(Chapter~\ref{chap:w-algebras}), where no Jacobi relation governs the
exec
/bin/zsh -lc "rg -n \"thm:kac-moody-ainfty|kac-moody-ainfty|ChirHoch\\"'^'"\\*\\(\\\\widehat\\{\\\\fg\\}_k\\)|polynomial\" chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
68: ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
69: & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
534:generated by a $\beta$-$\gamma$ system $(\beta_\alpha, \gamma_\alpha)$ of conformal weights $(1, 0)$ for each positive root $\alpha \in \Delta_+$, together with $r = \mathrm{rank}(\mathfrak{g})$ free bosons $\phi_i$ for the Cartan generators. The currents $J^a = f^a(\beta, \gamma, \phi, \partial\phi)$ are explicit differential polynomials determined by the Wakimoto construction.
805:e_{-\alpha_i}(z) &= \text{differential polynomial in } \beta_{\alpha_i}, \gamma_{\alpha_i}, \phi_i, \partial\phi_i \\
874:than the chain-group dimensions and exhibit polynomial growth
933:This is a polynomial identity in the variable
988:polynomial family \textup{(}linear in~$\lambda$\textup{)},
1006:For a matrix $A(\lambda)$ depending polynomially on a
1820:The double-pole term is proportional to $k + h^\vee = 0$ at critical level (the level-$(-h^\vee)$ curvature element $m_0$ vanishes; cf.\ Theorem~\ref{thm:kac-moody-ainfty}). Thus only the simple-pole term contributes to $d_{\bar{B}}$:
1934:\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody; \ClaimStatusProvedHere]\label{thm:kac-moody-ainfty}
4002:At $k = -h^\vee = -3$, the curvature vanishes. The Feigin--Frenkel center $\mathfrak{z}(\widehat{\mathfrak{sl}}_{3,-3})$ is a polynomial algebra in $2$ generators (corresponding to the $2$ fundamental invariants of $\mathfrak{sl}_3$, of degrees $2$ and $3$), consistent with the Wakimoto realization (Theorem~\ref{thm:w3-wakimoto-sl3}).
4196: polynomials:
4201: recovering Remark~\textup{\ref{rem:bar-complex-kl-polynomials}}.
4231:\emph{Proved here}: level-shifting duality (Theorem~\ref{thm:universal-kac-moody-koszul}), module-level bar-cobar (Theorem~\ref{thm:e1-module-koszul-duality}), bar resolution with KL multiplicities (Remark~\ref{rem:bar-complex-kl-polynomials}), $2\mathsf{h}$-periodicity for type $A_1$ (Proposition~\ref{prop:periodicity-same-type}), affine Hecke Koszul duality (Proposition~\ref{prop:affine-hecke-kd}), tensor structure (Theorem~\ref{thm:fusion-bar-cobar}), and weightwise finiteness at non-degenerate admissible level (Corollary~\ref{cor:bar-admissible-finiteness}).
5231: This is \emph{unbounded}, with polynomial growth $O(n^{r-1})$.
exec
/bin/zsh -lc "sed -n '1934,2015p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody; \ClaimStatusProvedHere]\label{thm:kac-moody-ainfty}
\index{$A_\infty$-structure!Kac--Moody}
The chiral algebra $\widehat{\mathfrak{g}}_k$ carries a canonical curved $A_\infty$ structure $(m_0, m_1, m_2, m_3, \ldots)$:
\begin{align}
m_0 &\in \widehat{\mathfrak{g}}_k \quad \text{(curvature, vanishes iff } k = -h^\vee\text{)} \\
m_2 &: \widehat{\mathfrak{g}}_k \otimes \widehat{\mathfrak{g}}_k \to \widehat{\mathfrak{g}}_k \quad \text{(chiral multiplication)} \\
m_n &: \widehat{\mathfrak{g}}_k^{\otimes n} \to \widehat{\mathfrak{g}}_k \quad \text{(higher coherences, } n \geq 3\text{)}
\end{align}

These are computed geometrically by:
\begin{equation}
m_n(\omega_1, \ldots, \omega_n) = \int_{\overline{C}_n(X)} \omega_1 \wedge \cdots \wedge \omega_n \cdot \Phi_n
\end{equation}
where $\Phi_n$ is the propagator form (fundamental chain) on $\overline{C}_n(X)$.
\end{theorem}

\begin{proof}
The $A_\infty$ structure is obtained by homotopy transfer from the bar-cobar adjunction. By the general theory (Theorem~\ref{thm:bar-cobar-inversion-qi} and the Homotopy Transfer Theorem, Appendix~\ref{app:homotopy-transfer}), for a chiral Koszul algebra $\cA$ with bar complex $\bar{B}(\cA)$, the cobar construction $\Omega(\bar{B}(\cA))$ carries a canonical dg algebra structure, and the quasi-isomorphism $\Omega(\bar{B}(\cA)) \xrightarrow{\sim} \cA$ (Theorem~\ref{thm:bar-cobar-isomorphism-main}) transfers an $A_\infty$ structure to~$\cA$.

For $\cA = \widehat{\mathfrak{g}}_k$, the geometric realization of the bar complex on $\overline{C}_{n+1}(X)$ (Theorem~\ref{thm:geometric-equals-operadic-bar}) identifies the transferred operations with configuration space integrals: $m_n$ is computed by integrating the product of input forms against the propagator $\Phi_n$ over the compactified configuration space. The $A_\infty$ relations $\sum_{r+s+t=n}(-1)^{rs+t} m_{r+1+t}(\mathrm{id}^{\otimes r} \otimes m_s \otimes \mathrm{id}^{\otimes t}) = 0$ follow from the Stokes theorem on $\overline{C}_n(X)$: the boundary strata of the FM compactification encode exactly the compositions of lower operations.
codex
I found a real audit defect inside the example surface: the affine Kac–Moody five-theorem table points Theorem H to an `A_\infty` theorem, not a Hochschild theorem. I’m now checking the other example-summary tables for the same drift, then I’ll patch the minimal set of files.
exec
/bin/zsh -lc "rg -n \"five-theorem verification|five-theorems|Theorem} &|H \\(Hochschild\\)\" chapters/examples/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"H \\(Hochschild\\)|ChirHoch\\"'$'"\\{\\}\\"'^'"\\*|ChirHoch\\"'^'"\\*|hochschild-polynomial-growth|main-koszul-hoch|prop:chirhoch1-affine-km|kac-moody-ainfty\" chapters/examples/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/bershadsky_polyakov.tex:43:H (Hochschild) &
chapters/examples/bershadsky_polyakov.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/logarithmic_w_algebras.tex:58:H (Hochschild) &
chapters/examples/lattice_foundations.tex:1522:\ChirHoch^*(\Vlat_\Lambda, \Vlat_\Lambda)
chapters/examples/lattice_foundations.tex:1524:\ChirHoch^*(\Vlat_\Lambda, \Vlat_\Lambda^\alpha).
chapters/examples/beta_gamma.tex:63:H (Hochschild) &
chapters/examples/beta_gamma.tex:65: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/beta_gamma.tex:2970:H (Hochschild) &
chapters/examples/kac_moody.tex:67:H (Hochschild) &
chapters/examples/kac_moody.tex:69: & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
chapters/examples/kac_moody.tex:1820:The double-pole term is proportional to $k + h^\vee = 0$ at critical level (the level-$(-h^\vee)$ curvature element $m_0$ vanishes; cf.\ Theorem~\ref{thm:kac-moody-ainfty}). Thus only the simple-pole term contributes to $d_{\bar{B}}$:
chapters/examples/kac_moody.tex:1934:\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody; \ClaimStatusProvedHere]\label{thm:kac-moody-ainfty}
chapters/examples/kac_moody.tex:5204:$\bigl(\ChirHoch^*(\widehat{\fg}_{-h^\vee}),\, \widehat{\fg}_{-h^\vee}\bigr)$
chapters/examples/kac_moody.tex:5216: \textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km}}\textup{)};
chapters/examples/kac_moody.tex:5225: \ChirHoch^*(\widehat{\fg}_{-h^\vee})
chapters/examples/level1_bridge.tex:56:H (Hochschild) &
chapters/examples/level1_bridge.tex:59: & Thm~\ref{thm:kac-moody-ainfty} \\
chapters/examples/y_algebras.tex:64:H (Hochschild) &
chapters/examples/y_algebras.tex:66: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/n2_superconformal.tex:52:H (Hochschild) &
 succeeded in 52ms:
chapters/examples/bershadsky_polyakov.tex:20:$k \neq -3$.}\label{tab:bp-five-theorems}
chapters/examples/bershadsky_polyakov.tex:23:\textbf{Theorem} & \textbf{Statement for $\mathcal{B}^k$}
chapters/examples/bershadsky_polyakov.tex:43:H (Hochschild) &
chapters/examples/level1_bridge.tex:27:\label{tab:level1-five-theorems}
chapters/examples/level1_bridge.tex:30:\textbf{Theorem} & \textbf{Statement}
chapters/examples/level1_bridge.tex:56:H (Hochschild) &
chapters/examples/beta_gamma.tex:43:$\lambda$.}\label{tab:betagamma-five-theorems}
chapters/examples/beta_gamma.tex:46:\textbf{Theorem} & \textbf{Statement for $\beta\gamma$}
chapters/examples/beta_gamma.tex:63:H (Hochschild) &
chapters/examples/beta_gamma.tex:2954:\emph{Theorem} & \emph{Projection of $\Theta_{\beta\gamma}$}
chapters/examples/beta_gamma.tex:2970:H (Hochschild) &
chapters/examples/y_algebras.tex:41:\label{tab:y-five-theorems}
chapters/examples/y_algebras.tex:44:\textbf{Theorem} & \textbf{Statement for $Y_{N_1,N_2,N_3}[\Psi]$}
chapters/examples/y_algebras.tex:64:H (Hochschild) &
chapters/examples/logarithmic_w_algebras.tex:39:$\cW(p)$.}\label{tab:wp-five-theorems}
chapters/examples/logarithmic_w_algebras.tex:42:\textbf{Theorem} & \textbf{Statement for $\cW(p)$}
chapters/examples/logarithmic_w_algebras.tex:58:H (Hochschild) &
chapters/examples/moonshine.tex:17:module~$V^\natural$.}\label{tab:moonshine-five-theorems}
chapters/examples/moonshine.tex:20:\textbf{Theorem} & \textbf{Statement for $V^\natural$}
chapters/examples/moonshine.tex:42:H (Hochschild) &

thinking
**Exploring theorem tables**

I see there are many five-theorem tables to consider. I’m wondering if I should only find those within the assigned scope. The user asked me to search chapters or examples for explicit verification related to a specific family, which makes sense. Should I audit all tables? That could get exhausting, but maybe it's necessary. I might need to scan all H entries to check for wrong references, particularly around level1_bridge.
exec
/bin/zsh -lc "sed -n '1,80p' chapters/examples/level1_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' chapters/examples/logarithmic_w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,90p' chapters/examples/symmetric_orbifolds.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
% ======================================================================
% Chapter: The Level-1 KM/Lattice Bridge
% ======================================================================

\chapter{The level-1 bridge}\label{chap:level1-bridge}

At level~$1$, two independently constructed bar complexes produce
identical cohomology by the Frenkel--Kac--Segal theorem
(Theorem~\ref{thm:lattice:frenkel-kac}). The affine Kac--Moody algebra
$\widehat{\fg}_1$ at level~$1$ and the lattice vertex algebra
$\Vlat_{\Lambda_\fg}$ on the root lattice of a simply-laced~$\fg$
are the same algebra in two presentations: the current presentation
(with $\dim\fg$ generating fields $J^a(z)$) and the lattice
presentation (with $\operatorname{rank}(\fg)$ Heisenberg fields
and vertex operators $E_\alpha(z) = Y(e^\alpha, z)$).
The bar constructions built from these two descriptions must
agree, and the comparison reveals a structural phenomenon:
the modular characteristic $\kappa$ undergoes a
\emph{level-$1$ reduction} from the generic-level Kac--Moody
value to the lattice rank.
 succeeded in 51ms:
% ======================================================================
% Chapter: Logarithmic W-algebras: the triplet family W(p)
% ======================================================================

\chapter{\texorpdfstring{Logarithmic $\cW$-algebras: the triplet
$\cW(p)$}{Logarithmic W-algebras: the triplet W(p)}}
\label{chap:logarithmic-w-algebras}

Every algebra treated so far has a semisimple module category:
the representation theory decomposes into a direct sum of irreducibles,
and the bar complex detects this decomposition through concentrated
cohomology. The triplet algebra $\cW(p)$ breaks this pattern at the
most fundamental level. Its module category is non-semisimple:
the operator $L_0$ acts with Jordan blocks, yet
Zhu's $C_2$-cofiniteness condition holds, the algebra has finitely
many simple modules, and modular invariance of characters persists in
a generalized form involving pseudo-trace functions
(Miyamoto~\cite{Miyamoto04}). The question is whether the bar
complex, which was built for the rational world, can accommodate
this non-semisimple structure; and if so, what modular Koszul
 succeeded in 50ms:
% ======================================================================
% Chapter: Symmetric Orbifolds
% ======================================================================

\chapter{\texorpdfstring{The symmetric orbifold $\operatorname{Sym}^N(X)$}{The symmetric orbifold Sym\^{}N(X)}}\label{chap:symmetric-orbifold}
% Regime III: non-perturbative (Convention~\ref{conv:regime-tags}).

The symmetric orbifold $\operatorname{Sym}^N(X) = X^{\otimes N}/S_N$
is the only standard family whose modular characteristic grows
linearly with a discrete parameter~$N$. This linearity is not a
coincidence: $\kappa(\operatorname{Sym}^N(X)) = N \cdot \kappa(X)$
follows from additivity of $\kappa$ for tensor products
(Corollary~\ref{cor:kappa-additivity}) and the fact that twisted
sectors, having positive conformal weight, do not contribute to the
genus-$1$ obstruction class. The result is a family in which
large-$N$ asymptotics become visible within the shadow obstruction
tower itself, and the DMVV infinite-product formula
\cite{DMVV97} provides a complete genus-$1$ partition function
against which every computation can be checked.



thinking
**Identifying issues with references**

I see that the level1 bridge might have incorrect links. I should think about fixing tables if they’re in scope, and I need to check if there are other issues. I also need to search for the reference "thm:kac-moody-ainfty." There could be missing worked examples, especially for Heisenberg. Since the user asked for those, I might consider adding a specific paragraph after a table to provide an explicit worked example. The free_fields file could be the right choice since it already has relevant details.
thinking
**Exploring Heisenberg verification**

I’m considering adding a remark in the free_fields document after the Heisenberg table. This remark would verify H by computing the bar differential being zero and possibly relating Hochschild to Sym(u, ε). I need to ensure everything is accurate and check existing sources for reference. I should clarify the exact statement of theorem H and look into the Heisenberg family results. Additionally, I’ll need to inspect any theory or proofs available for Heisenberg or Lattice to inform this process, and I'll search for Heisenberg Hochschild in the repository.
exec
/bin/zsh -lc "rg -n \"Heisenberg.*Hochschild|Hochschild.*Heisenberg|ChirHoch\\"'^'"\\*\\(\\\\cH|ChirHoch\\"'^'"\\*\\(H|ChirHoch\\"'^'"\\*\\(\\\\mathcal\\{H|derived center.*Heisenberg|Heisenberg.*derived center|bulk.*Heisenberg\" chapters/examples chapters/theory chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:main-koszul-hoch|thm:hochschild-polynomial-growth|prop:chirhoch1-affine-km" chapters/theory chapters/examples' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:Heisenberg.*Hochschild|Hochschild.*Heisenberg|ChirHoch\^\*\(\cH|ChirHoch\^\*\(H|ChirHoch\^\*\(\mathcal\{H|derived center.*Heisenberg|Heisenberg.*derived center|bulk.*Heisenberg)
                                                                   ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/examples/symmetric_orbifolds.tex:230:Theorem~\ref{thm:hochschild-polynomial-growth}, with degree
chapters/examples/beta_gamma.tex:65: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/theory/higher_genus_modular_koszul.tex:2388: Theorem~\textup{\ref{thm:main-koszul-hoch}}\textup{)}:
chapters/theory/higher_genus_modular_koszul.tex:4390: (Theorem~\ref{thm:main-koszul-hoch}), using Theorem~A
chapters/theory/higher_genus_modular_koszul.tex:30461: \textup{(}Theorem~\textup{\ref{thm:hochschild-polynomial-growth}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:30546:(Theorem~\ref{thm:hochschild-polynomial-growth}). Under the
chapters/examples/y_algebras.tex:66: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/theory/fourier_seed.tex:975:Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/examples/bershadsky_polyakov.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/moonshine.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/kac_moody.tex:5216: \textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km}}\textup{)};
chapters/theory/koszul_pair_structure.tex:574:bound on a curve (Theorem~\ref{thm:hochschild-polynomial-growth}):
chapters/theory/chiral_center_theorem.tex:62:(Theorem~\ref{thm:hochschild-polynomial-growth}).
chapters/theory/chiral_center_theorem.tex:1901: By Theorem~\textup{\ref{thm:hochschild-polynomial-growth}},
chapters/theory/chiral_center_theorem.tex:1977:By Theorem~\ref{thm:hochschild-polynomial-growth}, the chiral
chapters/theory/chiral_center_theorem.tex:2009:\label{prop:chirhoch1-affine-km}
chapters/theory/chiral_center_theorem.tex:2110:\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
chapters/theory/chiral_center_theorem.tex:2238:\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
chapters/theory/chiral_center_theorem.tex:2316:(Proposition~\ref{prop:chirhoch1-affine-km}), the
chapters/theory/introduction.tex:664: Theorem~\ref{thm:hochschild-polynomial-growth}).
exec
/bin/zsh -lc "sed -n '4945,5008p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

This imposes:
\[d\phi = 0\]
(cohomological condition)

\emph{Trivial cocycles.} If $\phi = d\psi$ for some $\psi$, the deformation is trivial
(comes from a redefinition of $\alpha$).

\emph{Nontrivial deformations.} The only independent deformation is changing the level $k$:
\[\alpha(z_1)\alpha(z_2) \sim \frac{k + t}{(z_1-z_2)^2}\]

This gives a 1-dimensional space:
\[\ChirHoch^2(\mathcal{B}) = \mathbb{C} \cdot [k].\]

Here $[k]$ is the cohomology class of the level.

\subsubsection{\texorpdfstring{Higher degrees: $\ChirHoch^n(\mathcal{B})$ for $n \geq 3$}{Higher degrees: HH n(B) for n >= 3}}

For the Heisenberg algebra (free boson), all higher Hochschild cohomology vanishes:
\[\ChirHoch^n(\mathcal{B}) = 0 \quad \text{for } n \geq 3\]

thinking
**Reviewing polynomial statements**

I'm considering the idea that calling "polynomial" related to group cohomology of \(\Z^r\) might not be accurate. The theorem indicates a degree limit of ≤2 for the Hilbert polynomial in modular Koszul algebras. Lattice structures, like `ChirHoch`, might not correspond directly to polynomial rings, so my earlier statements may need refinement.

I should closely examine the level1_bridge context and possibly clarify the results instead of using the vague term "polynomial." It seems the current description may lack support.
exec
/bin/zsh -lc "rg -n \"level1.*Hochschild|H (Hochschild)|ChirHoch\\"'$'"\\{\\}\\"'^'"\\*\\(\\\\widehat\\{\\\\fg\\}_1\\)|ChirHoch\\"'^'"\\*\\(\\\\widehat\\{\\\\fg\\}_1\\)|thm:lattice:hochschild|cor:lattice:hochschild-unimodular\" chapters/examples/level1_bridge.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n \"H \\(Hochschild\\)|thm:lattice:hochschild|cor:lattice:hochschild-unimodular|Hochschild\" chapters/examples/level1_bridge.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
56:H (Hochschild) &
codex
I have the minimal patch set now: one true gap and two reference drifts in the example tables. Before editing, I’m reading the precise Theorem H statement so the new Heisenberg worked example matches the actual theorem surface rather than an informal summary.
exec
/bin/zsh -lc "sed -n '5438,5490p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '680,845p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '56,74p'; printf '\\n'; nl -ba chapters/examples/level1_bridge.tex | sed -n '48,64p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
of the universal MC element
$\Theta_\cA \in \MC(\gAmod)$
(Theorem~\ref{thm:mc2-bar-intrinsic}). The verification tables below
organize the proved data per family; the shadow archetype column
refers to the classification of
Table~\ref{tab:shadow-tower-census}.
\end{remark}

\subsubsection{Heisenberg: five-theorem verification}

\begin{computation}[Five projections of $\Theta_{\cH_k}$;
\ClaimStatusProvedHere]
\label{comp:heisenberg-five-theorems}
\index{Heisenberg algebra!five-theorem verification}
Shadow archetype: G (Gaussian, $r_{\max} = 2$).
$\kappa(\cH_k) = k$.
Central charge $c = 1$.
\begin{center}
\small
\renewcommand{\arraystretch}{1.3}
 succeeded in 51ms:
    56	 $Q_g(\widehat{\fg}_k) \oplus
    57	 Q_g(\widehat{\fg}_{-k-2h^\vee})
    58	 = H^*(\overline{\cM}_g, Z)$
    59	 & Proved & Thm~\ref{thm:sl2-genus1-complementarity},
    60	 \ref{thm:sl3-genus1-complementarity} \\
    61	D (modular char.) &
    62	 $\kappa(\widehat{\fg}_k)
    63	 = \frac{\dim\fg\,(k{+}h^\vee)}{2h^\vee}$;\quad
    64	 $\kappa + \kappa' = 0$ (affine KM)
    65	 & Proved & Prop~\ref{prop:kappa-anti-symmetry-ff},
    66	 Rem~\ref{rem:sl3-universality} \\
    67	H (Hochschild) &
    68	 ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
    69	 & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	\begin{table}[ht]

 succeeded in 52ms:
\ChirHoch^\bullet(\cA)
\simeq
R\mathrm{Hom}_{\mathrm{ChirAlg}}
\bigl(\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA)),\cA\bigr),
\]
and the bar-cobar counit from
Theorem~\ref{thm:bar-cobar-isomorphism-main}(1) identifies this
with the $\Sigma$-coinvariant descent of $(\cA)^!_\infty$.
This gives~\eqref{eq:chirhoch-descent}.
\end{proof}

\begin{theorem}[Koszul duality for Hochschild cohomology
\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
\label{thm:main-koszul-hoch}
\index{Hochschild cohomology!Koszul duality|textbf}
\textup{[Regime: quadratic on the Koszul locus
\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}

For every chiral Koszul datum~$\cA$
\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})} with


thinking
**Working on theorem verification**

I’m considering deformation \(k\mapsto k+\varepsilon\) and thinking it might suffice. I should tie this to theorem H by name since that feels minimal enough. The paragraph could reference "This is the Heisenberg specialization of Theorem\ref{thm:hochschild-polynomial-growth}" to ground it better. The user wants explicit verification with examples, so I should add one for Heisenberg. Also, I'll make sure to check if the statement about "ChirHoch*(ĝ_1) polynomial" is correct for level 1.
thinking
**Finalizing example updates**

I’m considering that if there’s no local worked example, that might not be a fix. Yet, the table doesn’t necessarily need one. Maybe it’s better to add a note stating that A/B/C/D already have worked examples while H lacked one in the `chapters/examples/`, which I added in `free_fields.tex`. I also need to correct two tables that mislabeled an `A_\infty` theorem as the H reference. I should find exact line numbers after these changes, maybe using targeted grep or `rg`. I’ll think about running a narrow check with `make fast`, but I’m mindful of making it too heavy.
Plan update
Audit narrowed to the example surface for Theorems A-D, H. I found one real coverage gap for Theorem H and two incorrect H references in summary tables.
  ✓ Map existing A-D, H worked examples across chapters/examples and isolate gaps/drift
  → Patch the missing Theorem H worked example in the Heisenberg verification surface
  • Correct mispointed Theorem H references in example summary tables
  • Run narrow verification grep on the edited example files
codex
I’m editing three example files only: `free_fields.tex` to add the missing Heisenberg worked example for Theorem H, and `kac_moody.tex` plus `level1_bridge.tex` to repair two H references that currently point to the wrong theorem.

thinking
**Fixing patch issues**

I see that the patch failed because the mixed files include Kac_Moody content, but the necessary file context isn't found in the free_fields. It seems I need to create separate files for this. Also, applying the patch can’t be done in parallel, and we complied with that. So, I’ll rerun the operation but with the sections split correctly to avoid this issue. Let's make it work!
codex
The first patch missed because I combined contexts from multiple files. I’m splitting the edits cleanly now: `free_fields.tex`, then the two table files.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -5475,4 +5475,4 @@
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
@@ -5480,2 +5480,22 @@
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.

file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex
@@ -68,3 +68,5 @@
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
M /Users/raeez/chiral-bar-cobar/chapters/examples/level1_bridge.tex
@@ -58,3 +58,4 @@
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M chapters/examples/kac_moody.tex
M chapters/examples/level1_bridge.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}

Reconnecting... 1/5 (stream disconnected before completion: Transport error: network error: error decoding response body)
codex
I’ve applied the three edits. Now I’m doing a narrow verification pass: line-level inspection of the modified blocks and a grep to make sure no Theorem H example table in `chapters/examples/` still points to the `A_\infty` theorem.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5466,5498p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '64,73p'; printf '\\n'; nl -ba chapters/examples/level1_bridge.tex | sed -n '54,62p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5466	B (inversion) &
  5467	 $\Omega(\barBgeom(\cH_k)) \simeq \cH_k$ &
  5468	 Genus-$0$ qi (Thm~\ref{thm:bar-cobar-inversion-qi}) \\
  5469	C (complementarity) &
  5470	 $\kappa(\cH_k) + \kappa(\cH_k^!) = 0$ &
  5471	 $Q_g + Q_g^! = H^*(\overline{\mathcal{M}}_g, Z(\cH_k))$ \\
  5472	D (modular char.) &
  5473	 $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  5474	 $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
  5475	H (Hochschild) &
  5476	 $\ChirHoch^{>2}(\cH_k)=0$ &
  5477	 $P_{\cH_k}(t)=1+t+t^2$ \\
  5478	\bottomrule
  5479	\end{tabular}
  5480	\end{center}
  5481	For Theorem~H the Heisenberg computation is explicit:
  5482	\[
  5483	\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
  5484	\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
  5485	\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
 succeeded in 52ms:
    64	 $\kappa + \kappa' = 0$ (affine KM)
    65	 & Proved & Prop~\ref{prop:kappa-anti-symmetry-ff},
    66	 Rem~\ref{rem:sl3-universality} \\
    67	H (Hochschild) &
    68	 ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
    69	 & Proved & Thms~\ref{thm:main-koszul-hoch},
    70	 \ref{thm:hochschild-polynomial-growth};
    71	 Prop.~\ref{prop:chirhoch1-affine-km} \\
    72	\bottomrule
    73	\end{tabular}

    54	 & Proved
    55	 & \S\ref{sec:level1-kappa} \\
    56	H (Hochschild) &
    57	 ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
    58	 & Proved
    59	 & Thms~\ref{thm:main-koszul-hoch},
    60	 \ref{thm:hochschild-polynomial-growth} \\
    61	\bottomrule
    62	\end{tabular}
exec
/bin/zsh -lc 'rg -n "thm:kac-moody-ainfty" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/kac_moody.tex:1822:The double-pole term is proportional to $k + h^\vee = 0$ at critical level (the level-$(-h^\vee)$ curvature element $m_0$ vanishes; cf.\ Theorem~\ref{thm:kac-moody-ainfty}). Thus only the simple-pole term contributes to $d_{\bar{B}}$:
chapters/examples/kac_moody.tex:1936:\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} operations on Kac--Moody; \ClaimStatusProvedHere]\label{thm:kac-moody-ainfty}
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}


thinking
**Inspecting code lines**

I noticed that grep shows only legitimate uses remaining, which is a positive sign. I think I need to check some continuation lines, specifically lines 5497 and around 5500, to see if the sentences there look okay. It might be a good idea to open a few more lines too. I want to ensure everything is clear and properly structured before moving forward! Let’s take a closer look.
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5497,5504p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5497	which is the Heisenberg specialization of
  5498	Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
  5499	degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
  5500	Theorem~\ref{thm:main-koszul-hoch}.
  5501	The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
  5502	= \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
  5503	for all $r \geq 2$. No cubic, quartic, or higher shadows.
  5504	All higher $L_\infty$ brackets vanish:
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}



thinking
**Evaluating compile options**

It looks okay, but I need to think about whether to run a complete compile or just a targeted LaTeX syntax check on snippets. The repository is quite large and messy, so I worry about stability. Running `latexmk` could work, but a full compile might be better since we made changes. There’s talk of running `rg` for line inspection, which could be sufficient. Still, any output is only valid if the repository is stable enough.
thinking
**Deciding on verification method**

I think I can use narrow verification with grep, since the edits are mostly label references and local prose. But maybe it’s worth running `git diff --` to inspect the changes. Using `git diff -- chapters/examples/...` could help me review what's been modified. Running a diff would allow me to get a clearer picture of the changes and ensure everything looks as expected before moving forward.
codex
I’ve verified the edited lines and confirmed the bad `thm:kac-moody-ainfty` H references are gone from the example tables. I’m doing one final diff read now to check that the fixes stay minimal and scoped.
exec
/bin/zsh -lc 'git diff -- chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/level1_bridge.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 4f6ed9e..78818ea 100644
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -1,6 +1,6 @@
 
 \chapter{Free field archetypes}\label{chap:free-fields}
-% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
+% Regime I: quadratic (Convention~\ref{conv:regime-tags}).
 
 The Heisenberg algebra has one generator. Its shadow tower
 terminates at degree~$2$, its $r$-matrix vanishes after $d\log$
@@ -5473,11 +5473,31 @@ D (modular char.) &
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
exec
/bin/zsh -lc 'git status --short chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/level1_bridge.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 M chapters/examples/free_fields.tex
 M chapters/examples/kac_moody.tex
 M chapters/examples/level1_bridge.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}

Plan update
Added the missing Heisenberg worked example for Theorem H and corrected the two summary-table H references that pointed to the unrelated A_infinity theorem. Verified the edited blocks by line inspection and grep.
  ✓ Map existing A-D, H worked examples across chapters/examples and isolate gaps/drift
  ✓ Patch the missing Theorem H worked example in the Heisenberg verification surface
  ✓ Correct mispointed Theorem H references in example summary tables
  ✓ Run narrow verification grep on the edited example files
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}


thinking
**Checking line numbers**

I'm considering whether to include optional line numbers in the target, possibly from grep results. I want to ensure they're accurate enough. I think it would be helpful to get line numbers for specific remarks. I might be able to use `rg -n` to fetch relevant lines. It would make things clearer for the user, but I want to make sure it adds value without complicating anything too much. Let's try to get those numbers quickly!
exec
/bin/zsh -lc 'rg -n "For Theorem~H the Heisenberg computation is explicit" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"The three main theorems are verified at genus~\\\\\\"'$1'"\\\\\\"'$" chapters/examples/kac_moody.tex; rg -n "nontrivial instance of Theorem~D|:= F_g'"\\(\\\\cH_\\\\kappa\\)\" chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5481:For Theorem~H the Heisenberg computation is explicit:
 exited 2 in 51ms:
3937:The three main theorems are verified at genus~$1$ for $\widehat{\mathfrak{sl}}_{2,k}$: Theorem~A via the bar complex on $E_\tau$ with propagator $K^{(1)} = \theta_1'/\theta_1$ (Theorem~\ref{thm:km-higher-genus-corrections}); Theorem~B via $E_2$-collapse for generic $k$ (Theorem~\ref{thm:sl2-genus1-inversion}); and Theorem~C via
rg: regex parse error:
    (?:nontrivial instance of Theorem~D|:= F_g\(\cH_\kappa\))
                                                ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}

exec
/bin/zsh -lc 'rg -n "nontrivial instance of Theorem~D|genus tower of Theorem~D" chapters/examples/heisenberg_eisenstein.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
58:nontrivial instance of Theorem~D: $\kappa$ determines a universal generating function with
2362:= F_g(\cH_\kappa)$ which is the genus tower of Theorem~D.
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}



thinking
**Clarifying revisions and checks**

I think I should mention the existing A/B/C in the remarks at line 3937. It's good to note there are other example surfaces like lattice_foundations, but not essential. If the user asks for completeness, I could say, "I did not find any other H table in chapters/examples pointing to the wrong theorem." I could also include that a grep check passed and verification on edited blocks indicates the correct theorem definition in `kac_moody.tex`. However, I might skip mentioning the dirty worktree unless it's relevant.
thinking
**Structuring findings and verification**

I could mention that `free_fields.tex` had unrelated pre-existing differences near line 1, which I left untouched, but the user might find that confusing since they don’t see command outputs. However, if the final version clearly states the exact edits at line 5475, that should help. I also need to ensure the final version is concise, ideally around 15-20 lines. I’m thinking of crafting two brief sections: findings and coverage/verification, using a numbered list for clarity, ensuring each item stands alone and includes absolute clickable file links with line numbers.
codex
**Findings**
1. PROBLEM at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5475): `chapters/examples/` did not contain a worked Theorem H example; the Heisenberg five-theorem table only said “Degree-preserving sub-MC / polynomial,” which was a summary, not an explicit verification. EXACT edit applied: I replaced the H row with `\ChirHoch^{>2}(\cH_k)=0` and `P_{\cH_k}(t)=1+t+t^2`, then added the explicit Heisenberg computation at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5481) giving `\ChirHoch^0=\mathbb{C}`, `\ChirHoch^1=\mathbb{C}\cdot[D]`, `\ChirHoch^2=\mathbb{C}\cdot[\partial_k]`, and `\ChirHoch^n=0` for `n\ge 3`, with the bar-resolution argument and the tie-back to Theorem H.

2. PROBLEM at [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:67): the Theorem H row pointed to `thm:kac-moody-ainfty`, which is an `A_\infty` theorem, not the Hochschild theorem. EXACT edit applied: I changed the reference to `Thms~\ref{thm:main-koszul-hoch}, \ref{thm:hochschild-polynomial-growth}; Prop.~\ref{prop:chirhoch1-affine-km}` at [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:69).

3. PROBLEM at [level1_bridge.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/level1_bridge.tex:56): the level-1 five-theorem table had the same wrong Theorem H reference to `thm:kac-moody-ainfty`. EXACT edit applied: I changed it to `Thms~\ref{thm:main-koszul-hoch}, \ref{thm:hochschild-polynomial-growth}` at [level1_bridge.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/level1_bridge.tex:59).

**Worked-example coverage after the patch**
- A, B, C already had explicit family verification in [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:3937) for `\widehat{\mathfrak{sl}}_{2,k}` at genus 1.
- D already had an explicit Heisenberg lane in [heisenberg_eisenstein.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:58) and [heisenberg_eisenstein.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:2362).
- H now has an explicit Heisenberg worked example in [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:5481).

Verification was a narrow grep and line inspection on the edited example files. I did not run a full TeX build.
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index fb2010881a933246229713eef9055d92044a191c..78818ea5fe1c0707bd17b31a0ddd9897dc6e7676
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -5473,11 +5473,31 @@
  $\Theta_{\cH_k}\big|_{g=1,n=0} = k \cdot \lambda_1$ &
  $\kappa(\cH_k) = k$;\; $F_g = k \cdot \lambda_g^{\mathrm{FP}}$ \\
 H (Hochschild) &
- Degree-preserving sub-MC &
- $\operatorname{ChirHoch}^*(\cH_k)$ polynomial \\
+ $\ChirHoch^{>2}(\cH_k)=0$ &
+ $P_{\cH_k}(t)=1+t+t^2$ \\
 \bottomrule
 \end{tabular}
 \end{center}
+For Theorem~H the Heisenberg computation is explicit:
+\[
+\ChirHoch^0(\cH_k)=\mathbb{C},\qquad
+\ChirHoch^1(\cH_k)=\mathbb{C}\cdot[D],\qquad
+\ChirHoch^2(\cH_k)=\mathbb{C}\cdot[\partial_k],\qquad
+\ChirHoch^n(\cH_k)=0 \textup{ for } n \ge 3,
+\]
+where $D(J)=\mathbf{1}$ is the outer derivation and $[\partial_k]$
+is the infinitesimal level deformation. The bar resolution has one
+cogenerator in bar degree~$1$ and its quadratic square in bar
+degree~$2$, so applying
+$\operatorname{Hom}_{\cH_k\textup{-}\cH_k}(-,\cH_k)$ produces a
+cochain complex concentrated in degrees $0,1,2$. Hence
+\[
+P_{\cH_k}(t)=\sum_{n \ge 0}\dim \ChirHoch^n(\cH_k)\,t^n = 1+t+t^2,
+\]
+which is the Heisenberg specialization of
+Theorem~\ref{thm:hochschild-polynomial-growth}; the one-dimensional
+degree-$0$ and degree-$2$ terms match the shift-$[2]$ symmetry of
+Theorem~\ref{thm:main-koszul-hoch}.
 The tower terminates at $r = 2$: $\Theta_{\cH_k}^{\leq r}
 = \Theta_{\cH_k}^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 for all $r \geq 2$. No cubic, quartic, or higher shadows.
diff --git a/chapters/examples/kac_moody.tex b/chapters/examples/kac_moody.tex
index 529baf623e1e30c6a5d201e8b41cc511c643daf5..70767be402470bfbfeb2fb4807b93477d50edf2d
--- a/chapters/examples/kac_moody.tex
+++ b/chapters/examples/kac_moody.tex
@@ -66,7 +66,9 @@
  Rem~\ref{rem:sl3-universality} \\
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_k)$ polynomial
- & Proved & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Proved & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth};
+ Prop.~\ref{prop:chirhoch1-affine-km} \\
 \bottomrule
 \end{tabular}
 \end{table}
diff --git a/chapters/examples/level1_bridge.tex b/chapters/examples/level1_bridge.tex
index 147d35e200456737acc9d4102c2544c90d1cda06..793a16b2b62c27e1795dedcb4106acc3361c43a9
--- a/chapters/examples/level1_bridge.tex
+++ b/chapters/examples/level1_bridge.tex
@@ -56,7 +56,8 @@
 H (Hochschild) &
  ChirHoch${}^*(\widehat{\fg}_1)$ polynomial
  & Proved
- & Thm~\ref{thm:kac-moody-ainfty} \\
+ & Thms~\ref{thm:main-koszul-hoch},
+ \ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 \end{tabular}
 \end{table}

tokens used
102,704
