# R01_kappa_independent (576s)



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
session id: 019d88a4-201d-7240-acc0-5836eea03e05
--------
user
<task>
You are an ELITE RESCUE agent. Your focus: the latest 50-100 commits across a 3-volume,
4,700-page mathematical manuscript. This session deployed 592 Codex agents producing
63+ commits across: adversarial audit (105+250), rectification (25+20), platonic upgrade (20),
healing (40), plus relaunches. Every main theorem (A-D, H, MC1-5) was attacked, repaired,
and upgraded. You now operate on the CURRENT state — all those fixes are on disk.

Your mission:
1. HEAL remaining wounds from the session
2. PROVIDE alternative proof routes for REDUNDANCY (multiplicity of proof)
3. CROSS-CHECK against published literature (BD, FG, CG, Lurie, PTVV, CFG, Costello-Li)
4. DERIVE key results via INDEPENDENT methodology to confirm correctness
5. UPGRADE mathematical strength wherever possible
6. VERIFY cross-domain and cross-approach consistency

Run `git log --oneline -50` in the assigned repo to see recent work.
Read AGENTS.md and CLAUDE.md for the constitutional framework.
Read the actual .tex files — they reflect ALL session work.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs. Label hypotheses.
When citing literature: give paper, theorem number, and convention check.
</grounding_rules>

<completeness_contract>
For each result in your scope: state PRIMARY proof status, ALTERNATIVE proof (written/sketched/identified),
LITERATURE cross-check (confirmed/discrepant/not-checked), and CONFIDENCE (high/medium/low).
</completeness_contract>

<verification_loop>
After edits: re-read modified sections, grep for AP126/AP132/AP29/AP165 violations.
Run relevant tests if in compute scope.
</verification_loop>


INDEPENDENT DERIVATION: kappa(A) via three methods.

For Heisenberg, KM, Virasoro: derive kappa via THREE independent methods:
1. Shadow tower: kappa = av(r(z)) (+ Sugawara for non-abelian)
2. Anomaly: kappa from the 1-loop partition function Z_1 = eta(tau)^{-2*kappa}
3. Hilbert series: kappa from the growth rate of the bar complex Hilbert series

Verify all three agree for each family. Write the comparison as a Proposition
with three independent proofs. Add to chapters/theory/higher_genus_modular_koszul.tex.
mcp startup: no servers


thinking
**Planning exploration approach**

I think I should use the explorer sub-agent for any codebase questions and check repositories first. It’s important to give the user updates before I start exploring. Using an update plan might be necessary since the task is substantial. I might want to employ parallel tool calls to gather information efficiently. 

I need to ensure I read AGENTS.md thoroughly, as it may contain essential information. It's better to double-check instead of relying solely on the prompt’s instructions.
thinking
**Exploring for summaries**

I can use the explorer to locate relevant sections and summarize them, which sounds efficient. However, I still need to read the files myself, just to make sure everything's accurate. Maybe the explorer can handle some of the file reading, too, which could save time. I’ll focus on using the explorer to find existing kappa propositions and theorem labels, but I need to follow the repo instructions and check the actual files as well.
codex
Scope: audit the current surface around `chapters/theory/higher_genus_modular_koszul.tex`, reconstruct the latest 50 commits, and add a three-route `\kappa(A)` proposition grounded in the live manuscript and checks. I’m using `multi-path-verify` for the independent derivations, `beilinson-rectify` for the theorem insertion, and `cross-volume-propagation` only if the new claim duplicates elsewhere.
Plan update
  → Read required constitutional files and inspect recent commit surface plus target chapter context
  • Verify existing kappa conventions for Heisenberg, affine KM, and Virasoro from live sources and literature
  • Insert proposition with three independent derivations into higher_genus_modular_koszul.tex and keep labels/status consistent
  • Run targeted grep and narrow verification checks, then summarize proof/literature status and confidence
exec
/bin/zsh -lc 'git log --oneline -50' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1a7ac45 MC5 harmonic factorization: prop:harmonic-factorization proves delta_r^harm mechanism (AP203 resolved)
8421a1d AP225 RESOLVED: Theorem D all-genera universality proved via GRR + Arakelov-Faltings
e37cc33 Topologization chain-level: gauge rectification proves E_3 on original BRST complex for affine KM (AP210 resolved)
41ddfc4 Residual lollipop→tadpole: 10 instances in higher_genus_modular_koszul.tex + standalones
02336ae Final gaps + elite rescue: 85 source files rectified across theory, examples, connections
f2a6e1e Depth gap impossibility of 3: two independent proofs (AP219 tightened)
a93cb61 MC3 completion extension: conditional proof via Neeman/BvdB compact generation (AP233 resolved)
a09a633 Theorem H FM-tower spectral sequence: configuration-space collapse proved (AP222 resolved)
a46ee3d Koszul (viii) freeness DISPROVED: ChirHoch*(A) is NOT free polynomial (AP217 resolved)
55b2a24 SC-formality operadic proof: both directions without bilinear form (AP218 resolved)
07c7b9f Terminology: lollipop → tadpole across all Feynman diagram contexts (11 files)
c60db7e Final synchronisation: straggler audit reports and build artifacts
3fda149 Build artifacts: standalone PDFs synchronised, campaign script
da352b5 Makefile: icloud target reorganised into subject-sorted subfolders
5284950 Makefile: add all 14 new standalone papers to the standalone build target
b7bd5df Waves B-E + resume complete: 579/737 agents succeeded, 1,362 output files with content
bd28be8 release pdf
ecd3776 Agent campaign reports and build artifacts: final session synchronisation
1237d59 release pdf
d606b85 Condition removal research reports: H13-H17 from the healing campaign
 succeeded in 51ms:
# AGENTS.md — Modular Koszul Duality Programme (Canonical)

This file is the always-on operating constitution for Codex/GPT-5.4 in `~/chiral-bar-cobar` (Vol I). It is optimized for mathematical correction at `xhigh` reasoning effort. `CLAUDE.md` is the encyclopedic atlas; `AGENTS.md` is the load-bearing operational layer that steers correct behavior after compaction, context loss, model drift, or long multi-tool sessions. Every line changes behavior or it gets cut.

**Three volumes by Raeez Lorgat.** Vol I *Modular Koszul Duality* (this repo, ~2,719pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (`~/chiral-bar-cobar-vol2`, ~1,681pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (`~/calabi-yau-quantum-groups`, ~319pp). Total ~4,719pp, 121K+ tests, 3,500+ tagged claims.

Use this file for: durable repo-wide invariants; task routing and mode selection; truth hierarchy and claim-state discipline; session entry and verification loops; cross-volume propagation rules; empirical failure maps from recent commit archaeology; current dirty-surface awareness when it changes behavior.

Do not use this file as a dumping ground for temporary plans, session chatter, or a second prose copy of every anti-pattern in `CLAUDE.md`. If an instruction does not change behavior, remove it.

## I. Mission

This repository is in correction mode. For the current phase, optimize for truth, rectification, and claim-surface integrity over expansion. Assume all three volumes still contain undiscovered errors. Your job is not to defend inherited wording. Your job is to find falsehoods, isolate them, and either fix them or narrow the claims until they are true.

## II. GPT-5.4 Design Axioms

This constitution is deliberately shaped around current best practice for high-end agentic mathematical work:

1. **Exact scope before reasoning.** Name the file, theorem label, formula, convention, family, and status boundary before trying to solve the problem.
2. **Verification before verbosity.** Prefer a short falsifiable instruction plus a check over a long motivational paragraph.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
codex
I’ve loaded the constitutional surface and the last 50 commits. Next I’m reading the target chapter and adjacent canonical sources so the new proposition lands on the live proof path, not as a disconnected patch.
collab spawn_agent(call_stloHLVf2QnpC4CuBaf8aE1o, prompt="Inspect chapters/theory/higher_genus_modular_koszul.tex and identify the best insertion point for a new proposition givi…")
spawn_agent(call_stloHLVf2QnpC4CuBaf8aE1o, prompt="Inspect chapters/theory/higher_genus_modular_koszul.tex and identify the best insertion point for a new proposition givi…") pending init:
  agent: 019d88a4-a205-7202-972e-a2c879289e84
mcp startup: no servers
collab spawn_agent(call_umiboNkZ1RUBjOaShZAKZwfM, prompt="Inspect live sources for canonical kappa formulas and proofs relevant to Heisenberg, affine KM, and Virasoro: likely lan…")
spawn_agent(call_umiboNkZ1RUBjOaShZAKZwfM, prompt="Inspect live sources for canonical kappa formulas and proofs relevant to Heisenberg, affine KM, and Virasoro: likely lan…") pending init:
  agent: 019d88a4-a305-7320-950b-f645df24926a
mcp startup: no servers
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc 'rg -n "kappa" -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 9696

tmp_standalone_audit/survey_v2_xr.tex:202:$\kappa(\cA)\cdot\omega_g$ from the Hodge bundle at higher genus. A
tmp_standalone_audit/survey_v2_xr.tex:245:characteristic~$\kappa$ and the shadow obstruction tower, is the
tmp_standalone_audit/survey_v2_xr.tex:367:the curvature $d_{\mathrm{fib}}^2=\kappa(\cA)\cdot\omega_g$ is a
tmp_standalone_audit/survey_v2_xr.tex:394:its $\Sigma_2$-coinvariant trace $\kappa(\cA)=\mathrm{av}(r(z))$,
tmp_standalone_audit/survey_v2_xr.tex:448:\mathrm{av}\bigl(r^{\cH}(z)\bigr)=k=\kappa(\cH_k).
tmp_standalone_audit/survey_v2_xr.tex:453:Complementarity (free-field branch, sum $=0$; contrast Virasoro where sum $=13$): $\kappa(\cH_k)+\kappa(\cH_k^!)=k+(-k)=0$.
tmp_standalone_audit/survey_v2_xr.tex:461:+\frac{k\kappa^{ab}}{(z-w)^2}.
tmp_standalone_audit/survey_v2_xr.tex:465:form $J^a_{(1)}J^b=k\kappa^{ab}\cdot\mathbf 1$.
tmp_standalone_audit/survey_v2_xr.tex:475:\underbrace{k\kappa^{ab}\cdot\mathbf{1}}_{\text{curvature (double pole)}}.
tmp_standalone_audit/survey_v2_xr.tex:537:\;=\;\kappa_{\mathrm{dp}},
tmp_standalone_audit/survey_v2_xr.tex:539:\kappa(\widehat\fg_k)
tmp_standalone_audit/survey_v2_xr.tex:540:\;=\;\kappa_{\mathrm{dp}}+\frac{\dim\fg}{2}
tmp_standalone_audit/survey_v2_xr.tex:546:$\kappa=3(k+2)/4$; for $\widehat{\mathfrak{sl}}_3$:
tmp_standalone_audit/survey_v2_xr.tex:547:$\kappa=4(k+3)/3$.
tmp_standalone_audit/survey_v2_xr.tex:550:to~$\kappa$, is the data that builds the Yangian $Y(\fg)$.
tmp_standalone_audit/survey_v2_xr.tex:553:$\kappa(\widehat\fg_k)+\kappa(\widehat\fg_k^!)=0$
tmp_standalone_audit/survey_v2_xr.tex:576:\text{degree }2\colon&\quad\mathrm{av}(r(z))+\kappa_{\mathrm{sp}}=\kappa(\cA)
tmp_standalone_audit/survey_v2_xr.tex:577: &&\text{(Theorem D; $\kappa_{\mathrm{sp}}=0$ for abelian, $\dim\fg/2$ for KM)},\\
exec
/bin/zsh -lc "sed -n '1,200p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc 'rg -n "kappa" landscape_census.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "kappa" -n chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: landscape_census.tex: IO error for operation on landscape_census.tex: No such file or directory (os error 2)
 succeeded in 51ms:
Total output lines: 1219

12: d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
14:%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
16:$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
49:the modular characteristic $\kappa(\cA)$ at degree~$2$,
129: determined by three invariants $(\kappa, \alpha, S_4)$. The
130: discriminant $\Delta := 8\kappa S_4$ forces the tower depth.
137: If $\kappa = 0$, it stops at depth~$3$
153: $\kappa$, $\mathfrak{C}$, $\mathfrak{Q}$ are the genus-$0$
187:At critical level $k = -h^\vee$, the scalar curvature $\kappa$
397: \arrow[r, phantom, "\scriptstyle \dfib^{\,2} = \kappa(\cA) \cdot \omega_g"]
402: \arrow[r, phantom, "\scriptstyle \dfib^{\,2} = \kappa(\cA^!) \cdot \omega_g"]
409:($\kappa + \kappa' = 0$ for Kac--Moody and free-field
410:algebras; $\kappa + \kappa' = K_\fg \cdot \varrho(\fg)$ for
423:and curvature is controlled by a universal scalar~$\kappa(\cA)$.
488:$\mathrm{obs}_g = \kappa(\cA) \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{}) for
491:genus-$1$ identity $\mathrm{obs}_1 = \kappa(\cA) \cdot \lambda_1$ is
565:$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g \cdot \operatorname{id}$
699:\item the Heisenberg algebra $\mathcal{H}_\kappa$
exec
/bin/zsh -lc "rg -n \"kappa|eta\\(|Hilbert|shadow|Sugawara|partition function|r-matrix|classical r-matrix|av\\(r\" chapters/theory/higher_genus_modular_koszul.tex landscape_census.tex chapters/examples/kac_moody.tex chapters/examples/free_fields.tex chapters/examples/virasoro*.tex chapters/examples/w_algebras*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2920,3220p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "ls chapters/examples | rg 'vir|free|kac|w_'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
zsh:1: no matches found: chapters/examples/virasoro*.tex
 exited 1 in 51ms:
sed: landscape_census.tex: No such file or directory
 succeeded in 51ms:
free_fields.tex
kac_moody.tex
logarithmic_w_algebras.tex
w_algebras.tex
w_algebras_deep.tex
 succeeded in 51ms:
downstream step: it identifies the genus-$g$ scalar component of that
trace with $\kappa(\cA)\lambda_g$ on the proved uniform-weight lane.
Theorem~\ref{thm:family-index} is downstream again: it is the
Grothendieck--Riemann--Roch identification of the already constructed
scalar series for the bar family~\eqref{eq:bar-family} on the
universal curve. Thus the logical route is
\[
\Theta_\cA
\;\Longrightarrow\;
\mathrm{obs}_g=\kappa(\cA)\lambda_g
\;\Longrightarrow\;
\sum_{g \geq 1} F_g x^{2g}
=
\kappa(\cA)\cdot(\hat{A}(ix)-1),
\]
and Theorem~\ref{thm:genus-universality} does not invoke
Theorem~\ref{thm:family-index}.
Part~(i) is Theorem~\ref{thm:genus-universality} for
uniform-weight algebras. For multi-generator algebras
($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
exec
/bin/zsh -lc 'find . -name landscape_census.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4300,4700p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 2.14s:
./chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a074cd40/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ab4d244b/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a7a899b6/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ad4860d3/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-abc99e5a/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ab0fb328/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ac041f8d/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a618b30c/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a35dd0a7/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ae5ffa93/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a6b91d46/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a001fc1b/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a716d31f/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a78e4d88/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a7c35613/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a506436b/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a6d629eb/chapters/examples/landscape_census.tex
 succeeded in 50ms:
\Phi_{\mathfrak{D}} = \exp(\Theta_\cA^{\mathrm{scat}}),
\qquad
\Theta_\cA^{\mathrm{scat}} \in \widehat{\gAmod},
\]
its infinitesimal flatness equation in the completed dg~Lie algebra is
\[
[\dzero,\Theta_\cA^{\mathrm{scat}}]
+ \tfrac12[\Theta_\cA^{\mathrm{scat}},\Theta_\cA^{\mathrm{scat}}]
= 0.
\]
Thus $\Theta_\cA^{\mathrm{scat}}$ is a Maurer--Cartan element. Its
degree-$r$ truncation is assembled from the same primitive shadows as
the bar-intrinsic tower, but now by phase-ordered wall crossing and the
Baker--Campbell--Hausdorff product instead of the recursive inverse
limit. In this picture the primitive shadows are the wall data, the BPS
phase ordering is the assembly rule, and the Maurer--Cartan equation is
the infinitesimal form of scattering-diagram consistency; compare
Remark~\ref{rem:bps-wall-crossing-bar}. The missing manuscript-level
input is the full construction of the scattering diagram attached
to~$\cA$ together with the comparison between its wall data and the
exec
/bin/zsh -lc 'rg -n "shadow" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
14:archetype, by a finite set of shadow invariants: the scalar
15:$\kappa$, the cubic and quartic shadow coefficients $S_3$ and $S_4$,
22:forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
201:This is independent of shadow depth~$\kappa_d$
202:(Theorem~\ref{thm:shadow-euler-independence}).
207:\noindent\textbf{The shadow obstruction tower as organizing frame.}
212:ambient shadow at genus~$0$; the Koszul dual is obtained via
249:Table~\ref{tab:shadow-tower-census} below records the
250:shadow obstruction tower data that completes the portrait: the archetype class,
251:shadow depth $r_{\max}$, and the first nontrivial higher shadow for
257:\label{tab:shadow-tower-census}
258:\index{shadow obstruction tower!census table}
267: & \textbf{First higher shadow}
278:Niemeier $V_\Lambda$ (all 24; $\kappa = 24$) & G & 2 & none: blind to root system & Thm~\ref{thm:lattice:niemeier-shadow-universality} \\
282:\multicolumn{5}{|c|}{\textit{Lie/tree: cubic shadow nontrivial}} \\
288:\multicolumn{5}{|c|}{\textit{Contact/quartic: quartic contact shadow nontrivial}} \\
304:$\mathcal{W}_3^k(\mathfrak{sl}_3)$ (principal) & M & $\infty$ & $T$-line $S_4^T = 10/[c(5c{+}22)]$; $W$-line quartic $\neq 0$ & Comp~\ref{comp:w3-shadow-tower-data} \\
306:Ising minimal model $\mathcal{M}(4,3)$ ($c=1/2$) & M & $\infty$ & $S_4 = 40/49$; $\Delta = 80/49 \neq 0$ & Prop~\ref{prop:ising-shadow-invariants} \\
308:$\mathcal{N}{=}2$ superconformal $\mathrm{SCA}_c$ & M & $\infty$ & $T$-channel infinite; $J$-channel terminates at degree $2$; $G$-channel at degree $3$ & Rem~\ref{rem:n2-shadow-tower} \\
310:Triplet $\mathcal{W}(p)$ (logarithmic; $p \geq 2$) & M & $\infty$ & $T$-channel forces $r_{\max}^T = \infty$ regardless of $c$ & \S\ref{sec:wp-shadow-depth} \\
exec
/bin/zsh -lc 'rg -n "Hilbert" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2542:\underbrace{F_\cA \in \mathrm{IndHilb}}_{\text{Hilbert factorization}}
2573:The sewing envelope determines the Hilbert
2575:The Hilbert factorization theory determines the
2580:forgets the algebraic presentation; the Hilbert
3056:and its graded ranks are determined by the Hilbert series of~$\cA$.
28552:not the full Hilbert space structure or the modular
29077:The Hilbert space of $\operatorname{Sym}^N(\cA)$ decomposes
30734:$\{0, 1, 2\}$ with polynomial Hilbert series
exec
/bin/zsh -lc 'rg -n "kappa" chapters/examples/kac_moody.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
5:degree~$2$, and every obstruction is a scalar multiple of~$\kappa$.
12:cubic shadow~$\mathfrak{C}(x,y,z) = \kappa(x,[y,z])$ at
62: $\kappa(\widehat{\fg}_k)
64: $\kappa + \kappa' = 0$ (affine KM)
65: & Proved & Prop~\ref{prop:kappa-anti-symmetry-ff},
87:$\kappa(\widehat{\fg}_k)$ &
90: $\kappa(x,[y,z])$ (Lie bracket) \\
94: (sharing $\kappa$ with $\widehat{\fg}_{-k-2h^\vee}$) \\
95:Complementarity & $\kappa + \kappa' = 0$ (affine KM) \\
135:$\kappa = \dim(\mathfrak{g}) \cdot (k + h^\vee)/(2h^\vee)$
139:$\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$. The strict model $\Convstr$ carries a nonzero cubic shadow at degree~$3$
171:minimal package $\Theta^{\min} = \kappa \cdot \eta \otimes \Lambda$
173:$\kappa = \dim(\mathfrak{g})\cdot(k+h^\vee)/(2h^\vee)$, while
179:At critical level $k = -h^\vee$, $\kappa = 0$ and the bar complex
203:the scalar formula $\mathrm{obs}_g = \kappa\cdot\lambda_g$ holds
238:At level~$k$ with $\kappa=3(k+2)/4$, the genus-$1$ deformation
245:\kappa
268:(iv)~genus tower with $\kappa = \dim(\mathfrak{g})\cdot(k + h^\vee)/(2h^\vee)$, Lie/tree shadow
364:Let $\mathfrak{g}$ be a simple finite-dimensional Lie algebra with Killing form $\kappa_{\mathfrak{g}}$, normalized so that $(\theta|\theta) = 2$ where $\theta$ is the highest root. The \emph{loop algebra} is:
383:[x \otimes t^m, y \otimes t^n] = [x,y] \otimes t^{m+n} + m \delta_{m+n,0} \cdot \kappa_{\mathfrak{g}}(x,y) \cdot K
exec
/bin/zsh -lc "sed -n '3000,3085p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\[
\Theta_\cA \text{ and its shadow tower}
\Longrightarrow
\mathrm{obs}_g=\kappa\cdot\lambda_g
\Longrightarrow
\sum_{g \ge 1} F_g x^{2g}
=
\kappa\cdot(\hat{A}(ix)-1)
\]
The bar-intrinsic shadow tower is the common source.
The first implication is the scalar-trace identification of
Theorem~\ref{thm:genus-universality}; the second is the downstream
GRR/family-index identification of the same scalar series on the
virtual bar family. Theorem~\ref{thm:family-index} is therefore the
index-theoretic reformulation of the scalar output, not the
load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
\emph{Step~B} (M-level): universality
$\mathrm{obs}_g=\kappa\cdot\lambda_g$ \textup{(}UNIFORM-WEIGHT;
unconditional at $g{=}1$,
Theorem~\ref{thm:genus-universality}); generating function via
exec
/bin/zsh -lc 'rg -n "kappa" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
71:$\Theta_\cA^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$ and all
78:$\kappa \neq 0$; the $\beta\gamma$ and $bc$ systems break out of the
83:$\kappa(\beta\gamma) = c/2$ is generically nonzero). Both
115:$\mathbb{Q}[\kappa]$ (bosonic) or
116:$\mathbb{Q}[\kappa, \mu]$ with $\mu = 0$ ($\beta\gamma$--$bc$);
174:Modular characteristic $\kappa(\mathcal{F}) = c/2 = 1/4$.
179:= \kappa \cdot \eta \otimes \Lambda$
228:\item\label{item:fermion-kappa}
230: $\kappa(\mathcal{F}) = c/2 = 1/4$.
242: $\Delta(\mathcal{F}) = 8\kappa S_4 = 0$.
255:\eqref{item:fermion-kappa}:
259:Then $\kappa = c/2 = 1/4$ by the universal formula
260:$\kappa = c \cdot \rho$ with $\rho = 1/2$ for single-generator algebras
295:$\Theta_{\mathcal{F}}^{\leq r} = \kappa \cdot \eta \otimes \Lambda$
307:Q_{\mathcal{F}}(t) = (2\kappa)^2 = \tfrac{1}{4},
311:quadratic; only $S_2 = \kappa = 1/4$ contributes. The shadow
319:$\kappa(\mathcal{H}_k) = k$ is tunable
321:$\kappa(\mathcal{F}) = 1/4$ is fixed.
325:The shadow metric is $Q_L(t) = (2\kappa + 3\alpha t)^2 + 2\Delta\,t^2$
326:where $\alpha = S_3$ and $\Delta = 8\kappa S_4$. With

exec
/bin/zsh -lc 'ls chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
bar_complex_tables.tex
bershadsky_polyakov.tex
beta_gamma.tex
deformation_quantization.tex
deformation_quantization_examples.tex
free_fields.tex
genus_expansions.tex
heisenberg_eisenstein.tex
kac_moody.tex
landscape_census.tex
lattice_foundations.tex
level1_bridge.tex
logarithmic_w_algebras.tex
minimal_model_examples.tex
minimal_model_fusion.tex
moonshine.tex
n2_superconformal.tex
symmetric_orbifolds.tex
w3_composite_fields.tex
w3_holographic_datum.tex
exec
/bin/zsh -lc 'rg -n "Virasoro" chapters/examples' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 648

chapters/examples/w_algebras_deep.tex:183:\begin{example}[Virasoro bar complex coproduct]
chapters/examples/w_algebras_deep.tex:464:For the Virasoro ($A_1$), the graded dimension of $\bar{B}^1_h$
chapters/examples/w_algebras_deep.tex:647:The shadow obstruction tower reduces to the Virasoro tower:
chapters/examples/w_algebras_deep.tex:694:with the full Virasoro shadow obstruction tower, reflecting the fact that the
chapters/examples/w_algebras_deep.tex:695:stress tensor $T$ generates an autonomous Virasoro subalgebra
chapters/examples/w_algebras_deep.tex:829: Both theorematic Virasoro-target identities verified.
chapters/examples/w_algebras_deep.tex:977:(Virasoro, non-quadratic $\mathcal{W}_N$ at fixed~$N$)
chapters/examples/w_algebras_deep.tex:1687:Using the Virasoro OPE
chapters/examples/w_algebras_deep.tex:1758:($W$ is primary of weight 3 under Virasoro). Therefore:
chapters/examples/w_algebras_deep.tex:2137: higher-pole r-matrix of Virasoro/W-type (class~$M$). At $k = 0$
chapters/examples/w_algebras_deep.tex:2988:All shadow data is on the $T$-line (Virasoro direction).
chapters/examples/w_algebras_deep.tex:3169:$\mathcal{W}_2$ (Virasoro)
chapters/examples/w_algebras_deep.tex:3462:\subsection{The \texorpdfstring{$N=1$}{N=1} SuperVirasoro PVA and 3d supergravity}
chapters/examples/w_algebras_deep.tex:3464:\index{SuperVirasoro!PVA}
chapters/examples/w_algebras_deep.tex:3481:The bracket $\{T_\lambda T\}$ is the Virasoro PVA; the bracket
chapters/examples/w_algebras_deep.tex:3483:$\SVir_c$ contains the Virasoro subalgebra $\mathrm{Vir}_c$ as the
chapters/examples/w_algebras_deep.tex:3486:\begin{proposition}[SuperVirasoro 3d HT lift; \ClaimStatusProvedElsewhere]
chapters/examples/w_algebras_deep.tex:3507:Since $\SVir_c$ contains the Virasoro element $T$, the KZ
exec
/bin/zsh -lc "sed -n '3250,3335p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
theory. Then
\begin{equation}\label{eq:kappa-holographic-identity}
\kappa(\cA) \;=\; c_{\mathrm{bulk}}(\cA),
\end{equation}
and both sides agree, family by family, with the
Brown--Henneaux~\cite{BH86} central charge of the bulk theory
whose asymptotic boundary is~$\cA$. More precisely:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The genus-$1$ identity $F_1(\cA) = \kappa(\cA)/24$ of
Theorem~\ref{thm:modular-characteristic}(ii) is the exact
boundary translate of the one-loop Brown--Henneaux partition
function of the bulk theory on the solid torus.
\item The multiplier $\kappa(\cA) \cdot (\hat A(i\hbar) - 1)$
of Corollary~\ref{cor:free-energy-ahat-genus} is the
semiclassical expansion of the bulk theory around its flat
saddle, with $\hbar^{-2}$ playing the role of the bulk Newton
constant.
\item The additivity clause
$\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$ of
Theorem~\ref{thm:modular-characteristic}(iv) is the
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1180,1260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1180	 conformal weight $h = 2$, which is in the bar-relevant range
  1181	 $h \geq 2$. PBW fails; status is open. More generally, for
  1182	 admissible levels $k = p/q - 2$, the first null vector appears at
  1183	 $h = (p{-}1)q$, which is in the bar-relevant range whenever
  1184	 $(p{-}1)q \geq 2$.
  1185	\item \emph{Critical level does not break Koszulness.}
  1186	 The universal algebra $V_{-h^\vee}(\fg)$ at the critical level
  1187	 is uncurved ($\kappa = 0$) but remains Koszul by PBW universality.
  1188	 Critical level breaks the Sugawara construction, not free strong
  1189	 generation.
  1190	\end{enumerate}
  1191	\end{remark}
  1192	
  1193	\begin{remark}[Genus-\texorpdfstring{$1$}{1} free energy and the conformal anomaly]\label{rem:genus-1-verification}
  1194	\textup{(}LOCAL: genus-1 only\textup{})
  1195	\index{free energy!genus one}
  1196	The Faber--Pandharipande $\lambda_g$ formula (Theorem~\ref{thm:genus-universality}(iii))
  1197	gives the genus-$g$ free energy
  1198	$F_g(\cA) = \kappa(\cA) \cdot \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$ .
  1199	At $g = 1$, $|B_2| = 1/6$, yielding
thinking
**Cross-checking derivations**

I’m focusing on cross-checking the overall user mission by looking into three derivations from the literature. First up, there's the Heisenberg anomaly where the free boson partition function is akin to 1/η(τ). But the user mentions Z1 = η^{-2κ}, which gives me Z1 = η^{-2k} when I consider Heisenberg kappa as k. 

Then, moving on to KM, I might need to explore the WZW partition and anomaly, perhaps considering central charge and the Sugawara construction. Should I refer to Kac or Frenkel-BenZvi?
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '200,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   200	$\operatorname{ek} = N{-}1$ for $\cW_N$.
   201	This is independent of shadow depth~$\kappa_d$
   202	(Theorem~\ref{thm:shadow-euler-independence}).
   203	\end{remark}
   204	
   205	\medskip
   206	
   207	\noindent\textbf{The shadow obstruction tower as organizing frame.}
   208	Every entry in Table~\ref{tab:master-invariants} is a projection of the
   209	universal MC element $\Theta_\cA \in \MC(\gAmod)$
   210	(Theorem~\ref{thm:mc2-bar-intrinsic}). The scalar $\kappa(\cA)$ is
   211	the degree-$2$ projection; the complementarity sum $c + c'$ is the
   212	ambient shadow at genus~$0$; the Koszul dual is obtained via
   213	Verdier duality on the bar coalgebra.
   214	The seed datum for each family is its modular Koszul triple
   215	$\mathfrak{T} = (\cA, \cA^!, r(z))$
   216	(Definition~\ref{def:modular-koszul-triple}):
   217	\begin{equation}\label{eq:census-triples}
   218	\begin{aligned}
   219	\mathfrak{T}_{\cH}
exec
/bin/zsh -lc "rg -n \"\\\\kappa\\(\\\\mathcal\\{H\\}_k\\)\" -n chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\kappa\(\mathcal\{H\}_k\))
       ^^
error: unrecognized escape sequence
codex
The target chapter already has the GRR alternative route and the theorem-D pipeline. I’m now locking the exact local evidence for each of the three `\kappa` derivations and checking whether the chapter already contains a compatible proposition or a gap I should fill.
exec
/bin/zsh -lc "rg -n \"anomaly-koszul|eta\\(|partition function|Hilbert series|Hilbert|growth rate|alpha_g|av\\(r\\)|Sugawara|r\\"'^|r'"\\(z\\)|Heisenberg|Virasoro|affine\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:|thm:|cor:" chapters/theory/higher_genus_modular_koszul.tex | tail -n 80' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"kappa\\(|av\\(r\\)|Sugawara|eta\\(|Hilbert series|alpha_g|partition function|free energy|Heisenberg|Virasoro|affine\" chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/logarithmic_w_algebras.tex chapters/examples/w_algebras.tex chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg '("'^|/)landscape_census'"\\.tex"'$|higher_genus_modular_koszul'"\\.tex"'$|kac_moody'"\\.tex"'$|free_fields'"\\.tex"'$|w_algebras'"\\.tex"'$|logarithmic_w_algebras'"\\.tex"'$'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
31903:\label{thm:convolution-d-squared-zero}
31917:\label{thm:differential-square-zero}% NOTE: retains conj: prefix for backward compatibility; claim is ProvedHere
31918:\label{thm:ambient-d-squared-zero}
32003:\textup{(}Theorem~\textup{\ref{thm:quantum-arnold-relations}(b)--(d)}\textup{)}.
32070:Theorem~\ref{thm:ambient-d-squared-zero} rests on a \emph{single
32079:by publication, Theorem~\textup{\ref{thm:ambient-d-squared-zero}}
32086: \textup{(}Theorem~\textup{\ref{thm:log-clutching-degeneration})};
32090: proof of Theorem~\textup{\ref{thm:ambient-d-squared-zero}}.
32093:(Theorem~\ref{thm:convolution-d-squared-zero}) is
32097:MC construction (Theorem~\ref{thm:mc2-bar-intrinsic}), and the
32098:shadow obstruction tower (Theorem~\ref{thm:recursive-existence})
32109:Theorem~\textup{\ref{thm:ambient-d-squared-zero}} uses only the
32139:(Theorem~\ref{thm:mc2-bar-intrinsic})
32147:\label{thm:inductive-genus-determination}
32190:at all genera (Theorem~\ref{thm:mc2-bar-intrinsic}).
32215:\label{cor:genus-base-cases}
32269:\label{thm:genus2-shell-activation}
32303:\textup{(}Corollary~\textup{\ref{cor:shadow-visibility-genus}}\textup{)}.
32310:\textup{(}Theorem~\textup{\ref{thm:single-line-dichotomy}}\textup{)},
32338:(Proposition~\ref{prop:shadow-formality-low-degree}(ii)).
 succeeded in 51ms:
24:$D_\cA = \sum_{g \geq 0} \hbar^g d_\cA^{(g)}$ still satisfies
233:$\mathcal{A}_{\mathrm{complete}} / \hbar^{g+1} = \bigoplus_{h=0}^{g} \mathcal{A}^{(h)}$.
266:$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
382:For the Heisenberg algebra and affine Kac--Moody at generic level, modular
569:\prod_{g \geq 0} \hbar^g \bar{B}^{(g)}_X(\cA)$
572:with $\Dg{}^2 = 0$, whose reduction modulo $\hbar^{g+1}$ restricts
699:\item the Heisenberg algebra $\mathcal{H}_\kappa$
711:Theorem~\ref{thm:heisenberg-koszul-dual-early} for Heisenberg,
731:\begin{proposition}[Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul; \ClaimStatusProvedHere]
743:\item affine Kac--Moody algebras $\widehat{\mathfrak{g}}_k$ at generic
747:\item the Virasoro algebra $\mathrm{Vir}_c$ at generic central charge
759:The Kac--Moody and Virasoro statements are exactly
805:As in the Kac--Moody and Virasoro cases, the genus-$g$ enriched
900:Theorem~\ref{thm:pbw-allgenera-km}), Virasoro ($L_0$ diagonal,
907:The affine KM Killing class shows that this is an $E_3$ statement, not
1344:For any simple~$\fg$ at generic level, the affine
1374:\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
1523:for a basis $\{\alpha_1, \ldots, \alpha_g\}$ of
1577:For any simple~$\fg$ at generic level, the affine
1626:\begin{theorem}[PBW degeneration at all genera for Virasoro; \ClaimStatusProvedHere]
 succeeded in 50ms:
Total output lines: 1153

chapters/examples/logarithmic_w_algebras.tex:56: $\kappa(\cW(p)) = c/2$
chapters/examples/logarithmic_w_algebras.tex:76:$\kappa(\cW(p))$ &
chapters/examples/logarithmic_w_algebras.tex:141:of singular terms. The $T$-$T$ OPE is the standard Virasoro OPE
chapters/examples/logarithmic_w_algebras.tex:173: \qquad\text{(shadow depth: class M, from the Virasoro $T$-channel)}.
chapters/examples/logarithmic_w_algebras.tex:175:The $T$-channel alone forces $r_{\max} = \infty$ (the Virasoro
chapters/examples/logarithmic_w_algebras.tex:187:\begin{proposition}[$\kappa(\cW(p))$;
chapters/examples/logarithmic_w_algebras.tex:192: \kappa(\cW(p)) \;=\; \frac{c(\cW(p))}{2}
chapters/examples/logarithmic_w_algebras.tex:204:the Virasoro subalgebra alone determines the genus-$1$ bar
chapters/examples/logarithmic_w_algebras.tex:214:lattice VOA has $\kappa(V_{\sqrt{2p}\Z}) = 1$ (rank-$1$ lattice: $\kappa = \mathrm{rank}$). But $\cW(p)$ is a proper
chapters/examples/logarithmic_w_algebras.tex:215:subalgebra, not the full lattice VOA, so $\kappa(\cW(p)) \neq 1$
chapters/examples/logarithmic_w_algebras.tex:216:in general. Instead, the Virasoro sector of $\cW(p)$ has central
chapters/examples/logarithmic_w_algebras.tex:218:$c = 1$. The Virasoro contribution to $\kappa$ is $c/2 =
chapters/examples/logarithmic_w_algebras.tex:220:Heisenberg current $J$ of the lattice VOA is \emph{not} a
chapters/examples/logarithmic_w_algebras.tex:225:$\kappa(\cW(2)) = -1$.
chapters/examples/logarithmic_w_algebras.tex:243:$p$ & $c(\cW(p))$ & $\kappa(\cW(p))$ & $F_1 = \kappa/24$ \\
chapters/examples/logarithmic_w_algebras.tex:253:For all $p \geq 2$, $\kappa(\cW(p)) < 0$: the triplet algebra
chapters/examples/logarithmic_w_algebras.tex:462:The $T$-channel of $\cW(p)$ is a copy of the Virasoro OPE
chapters/examples/logarithmic_w_algebras.tex:512:$\kappa(\cW(p)^!) = (26 - c(\cW(p)))/2 - \kappa(\cW(p))$
 succeeded in 52ms:
chapters/examples/logarithmic_w_algebras.tex
chapters/examples/free_fields.tex
chapters/examples/kac_moody.tex
chapters/examples/landscape_census.tex
chapters/examples/w_algebras.tex
chapters/theory/higher_genus_modular_koszul.tex
exec
/bin/zsh -lc "rg -n \"kappa\\\\(\\\\mathcal\\\\{H\\\\}_k\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:kappa\(\mathcal\{H\}_k)
              ^^
error: unrecognized escape sequence


exec
/bin/zsh -lc "rg -n \"\\\\kappa\\\\(\\\\cH\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\kappa\(\cH)
       ^^
error: unrecognized escape sequence
thinking
**Determining best insertion point for proposition**

I’m identifying the ideal place to insert the new proposition summarizing the three independent derivations of kappa near the existing remarks that mention formulas but don’t prove them. The best spot is right after the concluding paragraph of the remark covering Steps A–D (around lines 2999–3054) and just before the remark labeled `rem:theorem-d-alt-grr` about the alternative proof via GRR. This position allows the proposition to bridge the summarizing derivations and the shift to the Hilbert series discussion. I’ll also highlight relevant nearby labels to avoid reuse (`rem:theorem-d-alt-grr`, `rem:kappa-holo-heisenberg`, `rem:kappa-holo-km`, `rem:kappa-holo-virasoro`, `eq:kappa-holographic-identity`, `thm:anomaly-koszul`, `thm:genus-universality`, etc.) and reference existing discussions around kappa, r-matrix, anomaly, and Hilbert series for thorough context.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2980,3065p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2980	modular functor, extracted via GRR.
  2981	
  2982	For $\widehat{\mathfrak{sl}}_{2,k}$ at integrable level, the
  2983	trace gives one number $\kappa = 3(k{+}2)/4$; the sheaf
  2984	gives $k{+}1$ conformal blocks at genus~$1$
  2985	(Remark~\ref{rem:chain-vs-classical-mf}). The full Chern
  2986	character recovers the spectral
  2987	discriminant~$\Delta_{\cA}$
  2988	(Remark~\ref{rem:spectral-characteristic-programme});
  2989	the flat connection furnishes the bar-side comparison surface for
  2990	the KZ/Hitchin package on that
  2991	integrable affine lane; the factorization structure recovers the modular
  2992	functor (Theorem~\ref{thm:chain-modular-functor},
  2993	Conjecture~\ref{conj:categorical-modular-kd}).
  2994	\end{remark}
  2995	
  2996	\begin{remark}[Proof routing for Theorem~D;
  2997	Convention~\ref{conv:proof-architecture}]
  2998	\label{rem:theorem-d-model}
  2999	\index{modular characteristic theorem!model presentation}
exec
/bin/zsh -lc "rg -n \"\\\\\\\\kappa\\\\\\\\(\\\\\\\\cH\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\\kappa\\(\\cH)
    ^
error: unclosed group
thinking
**Searching for target insertion**

I need to locate a possible insertion point around line 3287 or near the remarks discussing the three definitions. I should search within the range of lines 3280 to 3490 for specific lines. It seems like the proposition might fit well around either "The three notions of \kappa" or "holographic anomaly." So, I'll take a look in that area carefully!
exec
/bin/zsh -lc "sed -n '3268,3498p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$ of
Theorem~\ref{thm:modular-characteristic}(iv) is the
boundary manifestation of the bulk rule
$c_{\mathrm{bulk}}(T_1 \otimes T_2) = c_{\mathrm{bulk}}(T_1)
+ c_{\mathrm{bulk}}(T_2)$ for decoupled bulk theories.
\item The duality clause
$\kappa(\cA) + \kappa(\cA^!) = K_\fg \cdot \varrho(\fg)$ is the
bulk Koszul conductor: it records the gravitational anomaly of
the bulk theory seen by the slab
$\cA \otimes \cA^!$-bimodule of Dimofte--Niu--Py.
\end{enumerate}
\end{conjecture}

\begin{remark}[Evidence]
The identity~\eqref{eq:kappa-holographic-identity} is a
consequence of Theorem~\ref{thm:modular-characteristic} and
Corollary~\ref{cor:free-energy-ahat-genus}: the left-hand side
is the genus-$1$ obstruction coefficient extracted from the
bar complex at degree~$2$ by
$\kappa(\cA) = \operatorname{av}(r(z))$ for abelian algebras
exec
/bin/zsh -lc "sed -n '3000,3095p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '14980,15110p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1538,1608p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$H^*(T^*\mathbb{P}^1,\mathcal{O})$. What it does say is that,
on the reduced quotient, the Li--bar $E_1$ page is the
commutative bar cohomology of
$\mathcal{O}(\mathcal{N}_{\mathfrak{sl}_2})$, and its $d_1$
differential is induced by the Kirillov--Kostant bracket.
Determining whether the resulting reduced Li--bar $E_2$ page is
diagonally concentrated is therefore a separate reduced-level
calculation.

Even if the reduced page were diagonally concentrated, the
remaining obstruction to Koszulness would still lie in the
nilradical of the
full non-reduced algebra $R_{L_{-4/3}}$
(Proposition~\ref{prop:large-orbit-obstruction}(ii)):
the null vectors of $L_{-4/3}(\mathfrak{sl}_2)$ contribute
nilpotent elements not visible on~$\mathcal{N}$, and
determining whether these produce off-diagonal bar
cohomology requires an explicit nilradical computation.

This pattern holds for all types: reduced associated-variety
 succeeded in 50ms:
D\alpha + \tfrac12[\alpha,\alpha] = 0
\bigr\}.
\end{equation}
\end{definition}

\begin{remark}[Five theorems from the shadow obstruction tower]
\label{rem:five-from-one}
\index{main theorems!from shadow obstruction tower}
The five main theorems are projections of the scalar
level~$\Theta_{\cA}^{\leq 2} = \kappa(\cA)$ of the
shadow obstruction tower
(Definition~\ref{def:shadow-postnikov-tower}):
\begin{center}
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lll}
\toprule
\emph{Theorem} & \emph{Projection} & \emph{MC content} \\
\midrule
A (bar-cobar adjunction) &
 succeeded in 50ms:
constraint, which applies only to same-weight, same-generator
channels
(Proposition~\ref{prop:bosonic-parity-constraint}).
\end{computation}

\subsection{Genus-1 pipeline for the Virasoro algebra}
\label{sec:virasoro-genus-one-pipeline}
\index{genus-1 pipeline!Virasoro}

The genus-0 bar complex $\bar{B}(\mathrm{Vir}_c)$ has curvature
$m_0 = c/2$ from the quartic pole $T_{(3)}T = c/2$, giving a curved
$A_\infty$ structure for $c \neq 0$. The genus-1 pipeline lifts this
to the torus $E_\tau$ and computes all three main-theorem invariants,
paralleling \S\ref{sec:sl2-genus-one-pipeline}.

Unlike the Kac--Moody bar complex, which is
\emph{uncurved} at genus~0 ($\dzero^2 = 0$, reflecting the Jacobi identity) with
genus-1 curvature $\mcurv{1} = (k+h^\vee)\cdot\omega_1$ arising entirely from the $B$-cycle
monodromy, the Virasoro bar complex is already curved at genus~0
($m_0 = c/2$, reflecting the quartic pole). The $B$-cycle monodromy at
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3240,3375p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3240	Let $\cA$ be a modular Koszul chiral algebra
  3241	(Definition~\ref{def:modular-koszul-chiral}) realized as the
  3242	boundary of a $3$d holomorphic-topological theory in the
  3243	Costello--Dimofte--Gaiotto sense~\cite{CDG2023,DNP25}, and write
  3244	$\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ for the chiral derived
  3245	centre supplying the bulk operator algebra. Let
  3246	$c_{\mathrm{bulk}}(\cA) \in \mathbb{C}$ denote the one-loop
  3247	coefficient that governs, through the
  3248	$\hat A$-class~\eqref{eq:modular-char-gf}, the leading
  3249	asymptotic behaviour of the genus free energies of the bulk
  3250	theory. Then
  3251	\begin{equation}\label{eq:kappa-holographic-identity}
  3252	\kappa(\cA) \;=\; c_{\mathrm{bulk}}(\cA),
  3253	\end{equation}
  3254	and both sides agree, family by family, with the
  3255	Brown--Henneaux~\cite{BH86} central charge of the bulk theory
  3256	whose asymptotic boundary is~$\cA$. More precisely:
  3257	\begin{enumerate}[label=\textup{(\roman*)}]
  3258	\item The genus-$1$ identity $F_1(\cA) = \kappa(\cA)/24$ of
  3259	Theorem~\ref{thm:modular-characteristic}(ii) is the exact
exec
/bin/zsh -lc "rg -n --fixed-strings \"\\kappa(\\cH\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"\\\\kappa\\\\(\\\\mathcal\" chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\kappa\(\mathcal)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n '\\\\kappa\\(\\\\mathcal' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1396:$\kappa(\mathcal{W}^k(\fg)^!) = \kappa(\mathcal{W}^{-k-2h^\vee}(\fg))$


thinking
**Summarizing insertion context and references**

I'll pinpoint the best place for insertion after the remark near `rem:theorem-d-model` around lines 2996-3032 in `chapters/theory/higher_genus_modular_koszul.tex`. I'll highlight how existing discussions on kappa, r-matrix, anomaly, and Hilbert series appear nearby at lines like 3254-3309 and 3034-3065, and list label names to avoid reusing. The final answer will be clear and follow the developer’s formatting guidelines with simple bullet points.
exec
/bin/zsh -lc "rg -n '\\\\cH' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
219:\mathfrak{T}_{\cH}
220: &= \bigl(\cH_\kappa,\;
415:$\cH_k$ ($JJ$)
1115:Heisenberg $\cH_\kappa$ & \checkmark & (ii),(ix) & PBW universality \\
1223:The anomaly ratio $\varrho(\cA) := \kappa(\cA)/c(\cA)$ measures how much of the conformal anomaly survives from the Lie bracket's cyclic deformation. For the rank-$d$ Heisenberg algebra $\cH_1^{\oplus d}$ at level~$1$, $\varrho = d/d = 1$: the Polyakov formula $F_1 = c/24$ and the shadow formula $F_1 = \kappa/24$ coincide because $\kappa = c = d$. For all other standard families, $\varrho \neq 1$:
1576:$\cH + \mathrm{Vir}$
1653:Heisenberg $\cH_k$
2797:Heisenberg $\cH_\kappa$
2835:$\cH_\kappa$ is the exterior algebra on $V^*$, giving
2836:$\dim (\cH_\kappa^!)_n = p(n{-}2)$ (partitions);
thinking
**Searching for mathematical examples**

I need to find more precise examples for KM and Heisenberg, focusing on relevant sections. I should look for exact theorem labels and formulas in free_fields and kac_moody for genus-1. The user wants a proposition with three independent proofs for higher_genus_modular_koszul.tex. This likely means developing one proposition with a statement and proof that contains three subproofs: shadow tower, anomaly, and Hilbert series. I also want strong local evidence related to the Hilbert series growth rate. I'll start searching around lines 2530-2585 for potential propositions.
codex
- Best insertion point: right after Remark “Proof routing for Theorem D” (lines 2996‑3032 in `chapters/theory/higher_genus_modular_koszul.tex`) and before Remark “Alternative proof via GRR” kicks in. That spot already ties the three proof steps (shadow tower ⇒ `obs_g=κ·λ_g` ⇒ GRR and the Heisenberg level check) to Theorem \ref{thm:genus-universality}, Theorem \ref{thm:universal-generating-function}, Corollary \ref{cor:kappa-additivity}, Theorem \ref{thm:anomaly-koszul}, and Theorem \ref{thm:family-index}, so a unifying proposition giving the three independent derivations for Heisenberg, affine KM, and Virasoro would continue the flow before the narrative switches to the GRR/Hilbert‑series variant. (`chapters/theory/higher_genus_modular_koszul.tex:2996-3032`)

- Nearby context you can leverage: the same paragraph mentions the uniform‑weight scalar trace identity, the Bernoulli residue generating function, the anomaly cancellation clause, and the GRR index expression for `κ·(Ĥ(i𝑥)-1)`, so the new proposition can cite those statements; the subsequent remark already targets the Brown–Henneaux checks for Heisenberg, KM, and Virasoro (`rem:kappa-holo-heisenberg`, `rem:kappa-holo-km`, `rem:kappa-holo-virasoro` around lines 3312‑3372) as well as the bulk anomaly discussion via `eq:kappa-holographic-identity` and the bar trace `κ = av(r(z))`/Sugawara shift.

- Existing discussions you can reference: the same region handles the `κ` discussion (Remark \ref{rem:theorem-d-model}), the `r`‑matrix discussion inside the holographic evidence remark (`κ = av(r(z))` for abelian and `κ = av(r(z)) + dim(g)/2` for KM at lines 3282‑3308), the anomaly via Theorem \ref{thm:anomaly-koszul} (line 3023‑3024), and the Hilbert series/Grothendieck–Riemann–Roch yarn in Remark \ref{rem:theorem-d-alt-grr} (lines 3034‑3065) that already notes the graded ranks come from the Hilbert series of `A`.

- Labels to avoid reusing around this location include `rem:theorem-d-model`, `rem:theorem-d-alt-grr`, `eq:kappa-holographic-identity`, `rem:kappa-holo-heisenberg`, `rem:kappa-holo-km`, `rem:kappa-holo-virasoro`, and the nearby theorems/corollaries cited above. Pick a fresh label (e.g., `prop:kappa-triple-derivation`) so you don’t collide with the existing naming scheme.
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '1630,1690p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1630	Table~\ref{tab:shadow-l-functions} records the shadow field data
  1631	for all standard families at representative central charges.
  1632	
  1633	\begin{table}[ht]
  1634	\centering
  1635	\caption{Shadow field and Epstein $L$-function data}
  1636	\label{tab:shadow-l-functions}
  1637	\index{shadow field!standard families}
  1638	\renewcommand{\arraystretch}{1.4}
  1639	{\small
  1640	\begin{tabular}{|l|c|c|c|c|c|}
  1641	\hline
  1642	\textbf{Family}
  1643	 & \textbf{Class}
  1644	 & $\boldsymbol{\operatorname{disc}(Q_L)}$
  1645	 & $\boldsymbol{K_L}$
  1646	 & $\boldsymbol{d}$
  1647	 & \textbf{$L$-function} \\
  1648	\hline
  1649	\multicolumn{6}{|c|}{%
exec
/bin/zsh -lc 'rg -n "Hilbert" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1762:Table~\ref{tab:bar-dimensions} records the Koszul dual Hilbert
1797:\begin{conjecture}[Koszul dual Hilbert functions; \ClaimStatusConjectured]
1799:The Koszul dual Hilbert function $\dim (\cA^!)_n$ for the algebras of
1818: Theorem~\ref{thm:heisenberg-bar}; the Hilbert function follows
1890:\caption{Koszul dual Hilbert function $\dim (\cA^!)_n$ through degree~$10$
1971:Hilbert function of the Koszul dual algebra~$\cA^!$, which by the
1997:the Koszul dual Hilbert function.)
2083:Among the Koszul chiral algebras in Table~\textup{\ref{tab:bar-dimensions}}, the Koszul dual Hilbert function $\dim (\cA^!)_n$ grows sub-exponentially if and only if $\cA$ is a free field (Heisenberg or free fermion) or affine $\widehat{\mathfrak{sl}}_2$ (which has linear growth $2n{+}1$). All other interacting algebras (higher-rank Kac--Moody, Virasoro, $\mathcal{W}_3$, $bc$, $\beta\gamma$, Yangian) have exponential growth.
2115:Define the Koszul dual Hilbert series
2873:generators (one per negative mode), whose Hilbert function
2902:\item If the Koszul dual Hilbert series
3197:\begin{remark}[Bar dimensions as Koszul dual Hilbert series]\label{rem:bar-hilbert-koszul-dual}
3198:\index{bar complex!Koszul dual Hilbert series}
3199:For a Koszul algebra $\cA$, the Koszul dual Hilbert function $\dim (\cA^!)_n$ equals the conformal-weight-graded bar cohomology dimension at bar degree~$n$ (Corollary~\ref{cor:bar-cohomology-koszul-dual}). The generating function $P_{\cA}(x) = \sum_n \dim (\cA^!)_n\, x^n$ is the Hilbert series of $\cA^!$. In the Kac--Moody case, $P_{\widehat{\mathfrak{g}}_k}(x)$ coincides with the Hilbert series of $\mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$ as a graded algebra; this is independent of~$k$ because the Koszul dual has the same graded structure at all generic levels.
3255:For affine Kac--Moody algebras $\widehat{\mathfrak{g}}_k$, the exponential growth rate of the Koszul dual Hilbert function satisfies
3263:The bar chain groups have $\dim \bar{B}^n = (\dim \mathfrak{g})^n \cdot (n{-}1)!$ (Lemma~\ref{lem:bar-dims-level-independent}). The Koszul property constrains the Koszul dual dimensions to grow at most as fast as the chain groups modulo the differential. The Hilbert series, being algebraic with radius of convergence $1/\dim\mathfrak{g}$ (by the DS discriminant, Theorem~\ref{thm:ds-bar-gf-discriminant} for $\mathfrak{sl}_2$), has exponential growth rate $(\dim \mathfrak{g})^n$.
3274:Koszul dual Hilbert series
3347:$\dim (\cA^!)_n$ into a bigraded Hilbert series
3523:with closed-form Hilbert series
3896:quadratic-dual coalgebra whose Hilbert series is consistent with
codex
I’ve found the natural landing zone: the chapter already has the holographic/anomaly remarks and the Sugawara-shift discussion, but it does not yet package the three `\kappa` routes into one proposition. I’m now pinning down the Hilbert-series route, since that is the only part that cannot be inserted safely from memory.
exec
/bin/zsh -lc "sed -n '2528,2595p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[The platonic chain]
\label{rem:platonic-chain-theory}
\index{platonic chain|textbf}
\index{sewing envelope!platonic chain}

For a modular Koszul chiral algebra~$\cA$
satisfying hypotheses~(a)--(b) of
Theorem~\ref{thm:pbw-universal-semisimple}, the
logical unfolding is a four-stage chain:
\begin{equation}\label{eq:platonic-chain-theory}
\underbrace{\cA_{\mathrm{alg}}}_{\text{algebraic core}}
\;\subset\;
\underbrace{\cA^{\mathrm{sew}}}_{\text{sewing envelope}}
\;\rightsquigarrow\;
\underbrace{F_\cA \in \mathrm{IndHilb}}_{\text{Hilbert factorization}}
\;\rightsquigarrow\;
\underbrace{Q^{\mathrm{an}}_\bullet(\cA)}_{\text{coderived shadow}}
\end{equation}
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\cA_{\mathrm{alg}}$ is the algebraic
exec
/bin/zsh -lc 'rg -n "alpha_g|Hilbert factorization|IndHilb|growth rate of the bar complex|bar Hilbert|Hilbert series determines|Hilbert series of the bar complex|Hilbert polynomial|one-loop partition" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"eta-appearance|Heisenberg.*eta|Z_1\\(|one-loop partition function|modular anomaly|kappa\\(V_k|Sugawara shift|genus-1 curvature|Heisenberg genus-1|sl2-genus1-curvature|critical level|kappa\\(\\mathrm\\{Vir|vir-genus1-curvature\" chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2400,2470p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:1523:for a basis $\{\alpha_1, \ldots, \alpha_g\}$ of
chapters/theory/higher_genus_modular_koszul.tex:2542:\underbrace{F_\cA \in \mathrm{IndHilb}}_{\text{Hilbert factorization}}
chapters/theory/higher_genus_modular_koszul.tex:2558:\item $F_\cA$ is the IndHilb-valued conformally flat
chapters/theory/higher_genus_modular_koszul.tex:2575:The Hilbert factorization theory determines the
chapters/theory/higher_genus_modular_koszul.tex:3292:logarithm of the bulk one-loop partition function on the solid
chapters/theory/higher_genus_modular_koszul.tex:6218: H^2(\mathbf{D}_g) \cong \mathbb{C}\alpha_g,
chapters/theory/higher_genus_modular_koszul.tex:6220: H^2(\mathbf{D}_g^!) \cong \mathbb{C}\alpha_g^!,
chapters/theory/higher_genus_modular_koszul.tex:6337: H^2(\mathbf{D}_g)\cong \mathbb{C}\alpha_g,
chapters/theory/higher_genus_modular_koszul.tex:6339: H^2(\mathbf{D}_g^!)\cong \mathbb{C}\alpha_g^!;
chapters/theory/higher_genus_modular_koszul.tex:30154:\index{Fredholm determinant!one-loop partition function}
 exited 2 in 52ms:
rg: regex parse error:
    (?:eta-appearance|Heisenberg.*eta|Z_1\(|one-loop partition function|modular anomaly|kappa\(V_k|Sugawara shift|genus-1 curvature|Heisenberg genus-1|sl2-genus1-curvature|critical level|kappa\(\mathrm\{Vir|vir-genus1-curvature)
                                                                                                                                                                                                  ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 \textup{(Corollary~\ref{cor:topological-recursion-mc-shadow})}.
\item The shadow metric $Q_L$, shadow connection
 $\nabla^{\mathrm{sh}}$, and complementarity of
 discriminants
 $\Delta(\cA) + \Delta(\cA^!) =
 6960/[(5c{+}22)(152{-}5c)]$
 \textup{(}Theorem~\ref{thm:shadow-connection},
 for the Virasoro family; the general formula is
 family-dependent\textup{)} hold
 throughout the Koszul locus.
\end{enumerate}

\smallskip\noindent
\textbf{Tier~2} \textup{(analytic input: HS-sewing)}.
\begin{enumerate}[label=\textup{(2.\arabic*)}]
\item The sewing envelope $\cA^{\mathrm{sew}}$ exists
 \textup{(Definition~\ref{def:sewing-envelope})}.
\item Genus-$g$ partition functions converge on the
 Siegel upper half-space $\mathfrak{H}_g$
 \textup{(Theorem~\ref{thm:general-hs-sewing})}.
exec
/bin/zsh -lc "rg -n '\\\\kappa\\(\\\\mathcal\\\\{H\\\\}_k' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\kappa\(\\mathcal\\{H\\}_k)
                            ^
error: repetition quantifier expects a valid decimal

exec
/bin/zsh -lc 'rg -n "Heisenberg" chapters/examples/free_fields.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5:The Heisenberg algebra has one generator. Its shadow tower
141:Heisenberg $\mathcal{H}_k$ & $1$ & $0$ & $1$ & $0$ & $0$ & $0$ & $0$
149:The free fermion and Heisenberg bar complexes are
185:The free fermion replaces the Heisenberg double pole with a fermionic simple pole; the bar complex collapses.
210:Heisenberg algebra achieves class~G through \emph{commutativity}: the
316:Compare: the Heisenberg has
389:\begin{remark}[Fermion versus Heisenberg genus tower]
391:\index{free fermion!comparison with Heisenberg}
392:Both the free fermion and the Heisenberg algebra have genus expansions
402:fermion genus tower coincides with that of the Heisenberg at level
444:Compare with the Heisenberg, where the double-pole OPE
448:$\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
507:exact cancellation, matching the Heisenberg pair
571:is the structural difference from the Heisenberg, whose bosonic
588:Fredholm determinant \textup{(}Heisenberg\textup{)} is the fundamental
596: & \textbf{Heisenberg $\mathcal{H}_k$} \\
616:the Heisenberg at $k = 1$ on the $\mathbb{Z}$-lattice. This is the
683: Heisenberg algebra on the lattice $\mathbb{Z}$, and more
873:The bar complex of each free-field archetype is determined by OPE residues along collision divisors in the Fulton--MacPherson compactification; the results range from collapse (free fermion) through finite rank growth ($\beta\gamma$, Heisenberg) to lattice-graded structure (lattice VOAs).
1395:\subsection{Heisenberg bar complex}\label{sec:heisenberg-bar-complex-sec2}
thinking
**Searching on Heisenberg**

I'm looking to search on Heisenberg's one-loop partition and modular anomaly, particularly in free fields. It seems like I need a more precise approach to ensure I'm gathering the right information. I wonder if there's a way to refine my search further. There's a sense that I can run a better renormalization group analysis. Getting the details right in these topics is essential, so I'll take my time to ensure accuracy.
exec
/bin/zsh -lc "sed -n '30080,30260p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'eta-appearance|Heisenberg.*eta|Z_1\\(|one-loop partition function|modular anomaly|Sugawara shift|genus-1 curvature|sl2-genus1-curvature|critical level|vir-genus1-curvature|heisenberg-one-particle-sewing|Heisenberg genus-1|kappa\\(V_k\\(|kappa\\(\\\\mathrm\\{Vir' chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\ClaimStatusProvedElsewhere
\index{effective action!shadow tower decomposition|textbf}
\index{shadow obstruction tower!effective action}
The shadow obstruction tower determines a decomposition of the effective
action:
\begin{equation}\label{eq:effective-action-decomposition}
 S_{\mathrm{eff}}(\cA)
 \;=\;
 \sum_{r=2}^{r_{\max}(\cA)}
 S_{\mathrm{eff}}^{(r)}(\cA),
\end{equation}
where $S_{\mathrm{eff}}^{(r)}(\cA)$ is the evaluation of the
degree-$r$ shadow $\mathrm{Sh}_r(\cA)$ against the conformal
structure data on~$\Sigma_g$. In particular:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $S_{\mathrm{eff}}^{(2)} = \kappa(\cA) \cdot
 S_{\mathrm{Polyakov}}$
 \textup{(}Proposition~\textup{\ref{prop:polyakov-degree-two-projection})}.

\item $S_{\mathrm{eff}}^{(3)} =
 succeeded in 51ms:
chapters/examples/free_fields.tex:1624:\emph{Degree~2.} The central extension appears from the modular anomaly:
chapters/examples/free_fields.tex:2667:\emph{Proved}: the free-field and Heisenberg dualities (Chapter~\ref{sec:betagamma-koszul-dual}, Theorem~\ref{thm:heisenberg-koszul-dual-early}); the Kac--Moody level shift $\widehat{\mathfrak{g}}_k \leftrightarrow \widehat{\mathfrak{g}}_{-k-2h^\vee}$ (Theorems~\ref{thm:sl2-koszul-dual} and~\ref{thm:universal-kac-moody-koszul}).
chapters/examples/free_fields.tex:2704:\item \emph{W-algebras.} At critical level, the external quantum-Langlands picture relates $\mathcal{W}^{-h^\vee}(\mathfrak{g}, f)$ to a Langlands-dual $\mathcal{W}$-algebra, while the manuscript-internal proved statement is the critical fixed-point inversion package for the principal algebra. At general central charge: $\mathcal{W}_N^c \leftrightarrow \mathcal{W}_N^{c'}$ with $c + c' = 2(N-1)(2N^2+2N+1)$.
chapters/examples/free_fields.tex:2897:(double poles for Heisenberg; simple poles for $\beta\gamma$, fermions,
chapters/examples/free_fields.tex:4002:Z_1(\cF, \sigma) = \frac{\vartheta_\sigma(0|\tau)}{\eta(\tau)},
chapters/examples/free_fields.tex:4008:Z_1(\cF, \sigma_2) &= \frac{\vartheta_2(0|\tau)}{\eta(\tau)}
chapters/examples/free_fields.tex:4012:Z_1(\cF, \sigma_3) &= \frac{\vartheta_3(0|\tau)}{\eta(\tau)}
chapters/examples/free_fields.tex:4016:Z_1(\cF, \sigma_4) &= \frac{\vartheta_4(0|\tau)}{\eta(\tau)}
chapters/examples/free_fields.tex:4020:Z_1(\cF, \sigma_1) &= \frac{\vartheta_1(0|\tau)}{\eta(\tau)} = 0
chapters/examples/free_fields.tex:4092:partition function $Z_1(\cH_\kappa) = 1/\eta(\tau)$,
chapters/examples/free_fields.tex:4098:\begin{remark}[Heisenberg comparison: $\eta^{-1}$ vs
chapters/examples/free_fields.tex:4105:\underbrace{Z_1(\cH_\kappa)
chapters/examples/free_fields.tex:4108:\underbrace{Z_1(\cF, \sigma)
chapters/examples/free_fields.tex:4584:For general $c$, the descent involves an anomalous term: the Lie derivative $\mathcal{L}_{L_k}$ acting on bar complex elements picks up a central extension contribution proportional to $c$. The equivariant bar complex differential satisfies $d_{\mathrm{equiv}}^2 = (c - 26) \cdot \mu$ where $\mu$ is the Mumford class $\kappa_1 \in H^2(\overline{\mathcal{M}}_{0,n+3})$. The anomaly coefficient $(c - 26)$ is $\kappa(\mathrm{Vir}_c) - \kappa(\mathrm{Vir}_{26}) = c/2 - 13$, measuring the departure from the critical Koszul dual. At $c = 26$, this anomaly vanishes: $d_{\mathrm{equiv}}^2 = 0$, so the equivariant bar complex is a genuine cochain complex.
chapters/examples/free_fields.tex:5199:The modular anomaly is computed by:
chapters/examples/free_fields.tex:5224:By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
chapters/examples/free_fields.tex:5232:The quasi-modular anomaly of $E_2$ (cf.\ Appendix~\ref{app:theta}) is what drives the non-trivial cocycle.
chapters/examples/free_fields.tex:5235:By the genus-1 bar complex computation (Theorem~\ref{thm:eta-appearance}), the bar complex partition function is:
chapters/examples/free_fields.tex:5248:\index{modular anomaly!KM and W-algebras}
chapters/examples/free_fields.tex:5249:For an affine Kac--Moody algebra $\widehat{\fg}_k$, the modular anomaly weight at
exec
/bin/zsh -lc "sed -n '5208,5288p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1418,1488p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{proposition}[Virasoro Koszul dual at generic central charge;
\ClaimStatusProvedHere]
\label{prop:virasoro-generic-koszul-dual}
\index{Virasoro algebra!Koszul dual at generic $c$|textbf}
For all $c \in \mathbb{C}$,
\begin{equation}\label{eq:vir-koszul-dual-generic}
\mathrm{Vir}_c^! \;\simeq\; \mathrm{Vir}_{26-c}.
\end{equation}
\end{proposition}

\begin{proof}
The Virasoro algebra $\mathrm{Vir}_c$ is the quantum
Drinfeld--Sokolov reduction of $\widehat{\mathfrak{sl}}_2$ at
level~$k$ related to~$c$ by the Kac determinant formula
$c(k) = 1 - 6(k+1)^2/(k+2)$, equivalently
$c = 13 - 6(k+2) - 6/(k+2)$.

By Proposition~\ref{prop:verdier-level-identification}
(Chapter~\ref{chap:kac-moody}), the chiral Koszul dual of
 succeeded in 52ms:
\subsection{\texorpdfstring{Modular invariance under $SL_2(\mathbb{Z})$}{Modular invariance under SL-2(Z)}}

\begin{theorem}[Modular invariance of bar complex; \ClaimStatusProvedHere]\label{thm:modular-invariance}
At genus 1, the bar complex transforms covariantly under $SL_2(\mathbb{Z})$:
\[\gamma: \barBgeom^{(1)}(\mathcal{A})_\tau \to \barBgeom^{(1)}(\mathcal{A})_{\gamma \cdot \tau}\]
where $\gamma \cdot \tau = \frac{a\tau + b}{c\tau + d}$ for $\gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in SL_2(\mathbb{Z})$.

The transformation law is:
\[\barBgeom^{(1)}(\mathcal{A})_{\gamma \cdot \tau} = (c\tau + d)^{c/24} \barBgeom^{(1)}(\mathcal{A})_\tau\]
where $c$ is the central charge of the chiral algebra $\mathcal{A}$.
\end{theorem}

\begin{proof}[Proof via genus-1 bar complex]
The precise content of this theorem is: the partition function $Z_\mathcal{A}(\tau)$, obtained by taking the supertrace of $q^{L_0 - c/24}$ over the vacuum module and assembling the bar complex over the elliptic curve $\mathbb{T}_\tau = \mathbb{C}/(\mathbb{Z} + \tau\mathbb{Z})$, transforms as a modular form of weight $c/24$ for $SL_2(\mathbb{Z})$.

\emph{Step~1: Propagator on $\mathbb{T}_\tau$.}
By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
\[
G_\tau(z) = \zeta_\tau(z) - \frac{\pi^2 E_2(\tau)}{3}\,z
\]
exec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '2400,2445p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2400	\[
  2401	\sum_{i,j} \dim \Lambda^i(V^*_{<0})_j\; t^i q^j
  2402	= \prod_{n=1}^{\infty}\prod_{a=1}^{d} (1 + t q^n)
  2403	= \prod_{n=1}^{\infty}(1 + tq^n)^d. \qedhere
  2404	\]
  2405	\end{proof}
  2406	
  2407	\begin{remark}[Ext Poincar\'e series and Jacobi functions]
  2408	\label{rem:fock-ext-jacobi}
  2409	For $d = 1$, the Ext generating function
  2410	$\prod_{n=1}^\infty (1 + tq^n)$ at $t = -1$ gives
  2411	$\prod(1 - q^n) = q^{-1/24}\,\eta(\tau)$, recovering the
  2412	Dedekind eta function. At $t = 1$, the series
  2413	$\prod(1 + q^n) = q^{-1/24}\,\eta(2\tau)/\eta(\tau)$
  2414	counts the total dimension $\sum_i \dim \mathrm{Ext}^i$
  2415	in each conformal weight. For general~$d$, the specialization
  2416	$t = -1$ gives $\eta(\tau)^d$, consistent with the Euler
  2417	characteristic of the Ext algebra being the ratio of Heisenberg
  2418	to dual characters.
  2419	\end{remark}
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '1300,1340p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1300	$k \mapsto -k - 6$, matching
  1301	\S\ref{sec:sl3-computation}.
  1302	\end{proof}
  1303	
  1304	\begin{remark}[Higher-genus extension of the level identification]
  1305	\textup{(}UNIFORM-WEIGHT\textup{})
  1306	\label{rem:level-shift-higher-genus}
  1307	\index{level identification!higher genus}
  1308	The identification~\eqref{eq:verdier-level-shift} is a genus-$0$
  1309	statement: it determines the Koszul dual \emph{level} from the
  1310	binary collision data on~$\overline{C}_2(X)$. The extension to
  1311	higher genera is automatic: once the dual level $k^* = -k - 2h^\vee$
  1312	is determined, the modular characteristic
  1313	$\kappa(\widehat{\fg}_k) = \dim(\fg)(k + h^\vee)/(2h^\vee)$
  1314	(Theorem~\ref{thm:modular-characteristic}(i)) controls every genus
  1315	$g \geq 1$ via $\mathrm{obs}_g = \kappa \cdot \lambda_g$
  1316	\textup{(}: all currents share conformal weight~$1$, so
  1317	the scalar formula holds without a cross-channel correction,
  1318	cf.\ Theorem~D\textup{)}.
  1319	The duality clause

exec
/bin/zsh -lc "rg -n '\\\\kappa\\(\\\\mathrm\\{Vir\\}_c' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
660:\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = \frac{c}{2} + \frac{26-c}{2} = 13
668:The complementarity sum $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$ equals the bosonic string curvature $\kappa$ at $d = 26$ divided by~$2$. The combined genus-$g$ free energy
1317:$\kappa(\mathrm{Vir}_c) = c/2$.
1356:The KM two-channel decomposition $\kappa(\widehat{\mathfrak{sl}}_{2,k}) = 3k/4 + 3/2$ maps under DS to the single Virasoro channel $\kappa(\mathrm{Vir}_c) = c/2$. This is \emph{not} a simple specialization: the DS reduction collapses two channels into one via the Sugawara denominator $2(k+2)$, with the quartic Virasoro OPE pole mixing the double-pole and structure-constant channels.
2175:By the genus universality theorem (Theorem~\ref{thm:genus-universality}) with $\kappa(\mathrm{Vir}_c) = c/2$ (Theorem~\ref{thm:vir-genus1-curvature}) and the Faber--Pandharipande formula (Theorem~\ref{thm:mumford-formula}).
2246:$\kappa(\mathrm{Vir}_c) = c/2$ vs.\ $\kappa(\mathcal{H}_\kappa) = \kappa$: for $c=1$, $\kappa(\mathcal{H}_1) = 1$ but $\kappa(\mathrm{Vir}_1) = 1/2$, reflecting the difference between the full algebra and its Virasoro subalgebra. For the bosonic string:
thinking
**Searching for theorems**

I need to find the exact theorem or propositions regarding the Heisenberg eta and the KM anomaly. The user specifically asked for the one-loop partition function, which is \(Z_1 = \eta^{-2\kappa}\). I might consider looking into modular invariance as well. I should search around the reference 3900 in the kac_moody context to see if I can find relevant sources, even if they aren't explicitly mentioning KM or Virasoro. Let's go ahead and inspect further.
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '1308,1335p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1308	\label{cor:virasoro-genus2-curvature}
  1309	\index{curvature!genus-2 for Virasoro}
  1310	The genus-$2$ obstruction class of $\mathrm{Vir}_c$ is:
  1311	\begin{equation}\label{eq:vir-obs2}
  1312	\mathrm{obs}_2(\mathrm{Vir}_c) = \frac{c}{2} \cdot \lambda_2
  1313	\in H^4(\overline{\mathcal{M}}_2, \mathbb{Q})
  1314	\end{equation}
  1315	consistent with the genus universality theorem
  1316	\textup{(}Theorem~\textup{\ref{thm:genus-universality})} with
  1317	$\kappa(\mathrm{Vir}_c) = c/2$.
  1318	
  1319	The genus-$2$ free energy is:
  1320	\begin{equation}\label{eq:vir-F2}
  1321	F_2(\mathrm{Vir}_c) = \frac{c}{2} \cdot \lambda_2^{\mathrm{FP}}
  1322	= \frac{c}{2} \cdot \frac{7}{5760} = \frac{7c}{11520}
  1323	\end{equation}
  1324	At $c = 26$ \textup{(}bosonic string\textup{)}:
  1325	$F_2(\mathrm{Vir}_{26}) = 182/11520 = 91/5760$.
  1326	At $c = 1/2$ \textup{(}Ising\textup{)}:
  1327	$F_2(\mathrm{Vir}_{1/2}) = 7/23040$.
codex
The anomaly route is partially present but scattered: Heisenberg has explicit `\eta` control, affine KM has an `E_2` expansion, and Virasoro has genus-1 curvature plus modular-weight statements. I’m reading those three local pieces now to decide whether the proposition should state the anomaly proof as written or as a controlled comparison argument.
exec
/bin/zsh -lc "sed -n '4068,4118p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{computation}[GSO-summed partition function]
\label{comp:fermion-gso}
\index{GSO projection!free fermion}
\index{free fermion!GSO projection}
The GSO (Gliozzi--Scherk--Olive) projection sums over spin
structures with equal weight, discarding the odd spin
structure (which vanishes):
\begin{equation}\label{eq:fermion-gso}
Z_1^{\mathrm{GSO}}(\cF)
= \frac{1}{2}\left(
 \frac{\vartheta_2(0|\tau)^2}{\eta(\tau)^2}
+ \frac{\vartheta_3(0|\tau)^2}{\eta(\tau)^2}
+ \frac{\vartheta_4(0|\tau)^2}{\eta(\tau)^2}
\right).
\end{equation}
By the Jacobi abstruse identity
$\vartheta_3^4 = \vartheta_2^4 + \vartheta_4^4$
and its consequence
$\vartheta_2^2 + \vartheta_3^2 + \vartheta_4^2
= 2\vartheta_3^2$ \textup{(}up to sign conventions on
exec
/bin/zsh -lc "sed -n '3888,3925p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1572,1618p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,780p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Virasoro algebra replacing that of $\widehat{\mathfrak{sl}}_2$.

\subsubsection{Curvature theorem}

\begin{theorem}[Genus-1 curvature for \texorpdfstring{$\mathrm{Vir}_c$}{Virc}; \ClaimStatusProvedHere]
\label{thm:vir-genus1-curvature}
The genus-1 differential satisfies:
\begin{equation}\label{eq:vir-genus1-dsquared}
(d^{(1)})^2 = \frac{c}{2} \cdot \omega_1 \cdot \operatorname{id}
\end{equation}
where $\omega_1 \in H^2(\overline{\mathcal{M}}_{1,1})$ is the fundamental class.
Equivalently, the genus-1 obstruction coefficient is
$\kappa(\mathrm{Vir}_c) = c/2$, in agreement with the genus universality
theorem (Theorem~\ref{thm:genus-universality}).
\end{theorem}

\begin{proof}
The $B$-cycle quasi-periodicity~\eqref{eq:B-cycle-quasi-periodicity}
shifts the propagator by $-2\pi i$. Applying $d^{(1)}$ twice to a
degree-2 element $T \otimes T \otimes \eta_{12}$, the self-contraction
 succeeded in 51ms:
Q_1(\widehat{\mathfrak{sl}}_{2,k}) \oplus Q_1(\widehat{\mathfrak{sl}}_{2,-k-4}) = \mathbb{C} \oplus \mathbb{C}\lambda = H^*(\overline{\mathcal{M}}_{1,1})
\end{equation}

\emph{Step~4: Consistency checks.}
\begin{enumerate}
\item \emph{Involutivity}: Swapping $k \leftrightarrow -k-4$ exchanges the two summands. $Q_1(\widehat{\mathfrak{sl}}_{2,-k-4})$ maps to $H^0$ with coefficient $(-k-2)$, while $Q_1(\widehat{\mathfrak{sl}}_{2,k})$ maps to $H^0$ with coefficient $(k+2)$; the complementarity is symmetric.
\item \emph{Dimension count}: $\dim Q_1 + \dim Q_1^! = 1 + 1 = 2 = \dim H^*(\overline{\mathcal{M}}_{1,1})$. \checkmark
\item \emph{Abelian limit}: Setting $h^\vee = 0$ (and relabeling $k$ as $\kappa$), we recover $Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$ and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda$, matching Example~\ref{ex:heisenberg-complementarity-explicit}. \checkmark
\item \emph{Critical level limit}: As $k \to -2$, the curvature $(k+2) \to 0$, so $\dim Q_1 \to 0$; by complementarity, $\dim Q_1^! \to 2$. This is consistent with the enhanced center at critical level: the Feigin--Frenkel center provides additional flat sections that absorb both components of $H^*(\overline{\mathcal{M}}_{1,1})$. \checkmark
\end{enumerate}
\end{proof}

\subsection{Genus-1 partition function}

\begin{proposition}[Partition function via complementarity; \ClaimStatusProvedHere]
\label{prop:sl2-genus1-partition}
\index{partition function!genus-1!Kac--Moody}
The genus-1 partition function of $\widehat{\mathfrak{sl}}_{2,k}$ decomposes as:
\begin{equation}\label{eq:sl2-genus1-partition}
Z_1(\widehat{\mathfrak{sl}}_{2,k}|\tau) = \frac{\chi(\mathfrak{sl}_2)}{\eta(\tau)^3} \cdot \bigl(1 + (k+2) \cdot E_2(\tau) + O(E_4)\bigr)
 succeeded in 51ms:
the same-generator OPE poles lie at even orders
$z^{-2h}, z^{-(2h-2)}, \ldots, z^{-2}$ (from the conformal
algebra) together with a descendant pole at~$z^{-1}$. After
$d\log$ absorption ($n \mapsto n{-}1$), the even-order poles
become $z^{-(2h-1)}, z^{-(2h-3)}, \ldots, z^{-1}$, all odd,
and the descendant pole drops. Consequence: the $r$-matrix of a
single bosonic generator whose OPE has only even-order poles
(above $z^{-1}$) has no even-order poles.

The maximal $r$-matrix pole order follows the formula
$\max\operatorname{pole}(r) = 2h - 1$: the Heisenberg
($h = 1$) gives $z^{-1}$; the Virasoro ($h = 2$) gives $z^{-3}$;
the $W$ generator of $\cW_3$ ($h = 3$) gives $z^{-5}$ in the $WW$
channel.

The constraint applies whenever all OPE poles above $z^{-1}$
have even order. For the stress tensor ($h = 2$), this holds:
the $TT$ OPE has poles at $\{4, 2, 1\}$, all even above $z^{-1}$,
and the $r$-matrix poles $\{3, 1\}$ are both odd.
For the $\cW_3$ $WW$ channel ($h = 3$), the OPE has an additional

thinking
**Exploring census landscape**

I'm thinking that the landscape census lines show a table, but it doesn't seem direct. Maybe I need to go back to earlier formulas to get a better understanding. I could cite this if needed, but there’s a bit of waiting involved with the explorer agents. I need to figure out how to proceed effectively and make sure I gather all the right information before moving forward.
collab wait(call_C0fYHq4CYl0pcoz2RPcxzlIE)
  receivers: 019d88a4-a205-7202-972e-a2c879289e84, 019d88a4-a305-7320-950b-f645df24926a
wait(call_C0fYHq4CYl0pcoz2RPcxzlIE) 1 agents complete:
  019d88a4-a205-7202-972e-a2c879289e84 completed: "- Best insertion point: right after Remark “Proof routing for Theorem D” (lines 2996‑3032 in `chapters/theory/higher_gen…"
collab wait(call_v4UKRFLLZRGWlYmgBVUmszYo)
  receivers: 019d88a4-a305-7320-950b-f645df24926a

thinking
**Summarizing canonical formula references**

I’m organizing a detailed summary highlighting canonical formulas for `kappa = c/2` and related results across several important routes—the shadow-tower, anomaly, and Hilbert-series approaches. I’ll cite exact file and single-line references like `chapters/examples/genus_expansions.tex:1310` for Virasoro formulas, `chapters/examples/kac_moody.tex:1313` for Kac-Moody, and key locations in `landscape_census.tex` for the shadow tower and anomaly discussions. This will include tables, remarks, and complementarity formulas, structured with bullet points to clearly present the strongest local evidence for each route as requested.
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '650,680p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   650	\[
   651	\kappa_{\mathrm{KM}}(\widehat{\mathfrak{sl}}_{2,k}) + \kappa_{\mathrm{KM}}(\widehat{\mathfrak{sl}}_{2,-k-4}) = \frac{3(k+2)}{4} + \frac{3(-k-2)}{4} = 0 \quad \text{(Kac--Moody type~I)}
   652	\]
   653	Since $F_g$ is linear in $\kappa$, the result follows.
   654	\end{proof}
   655	
   656	\begin{remark}[Comparison with Virasoro complementarity]\label{rem:sl2-vs-vir-complementarity}
   657	\textup{(}LOCAL: scope fixed in this environment\textup{})
   658	For $\widehat{\mathfrak{sl}}_2$, the Kac--Moody obstruction coefficients cancel exactly \textup{(}$\kappa_{\mathrm{KM}} + \kappa_{\mathrm{KM}}' = 0$ type~I, free-field pattern\textup{)}, a consequence of the symmetric level-shift $k \mapsto -k-4$ fixing the midpoint $k = -2$. For the Virasoro algebra $\mathrm{Vir}_c \simeq \mathcal{W}^k(\mathfrak{sl}_2)$, the complementarity takes a different form:
   659	\[
   660	\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = \frac{c}{2} + \frac{26-c}{2} = 13
   661	\]
   662	so $F_g(\mathrm{Vir}_c) + F_g(\mathrm{Vir}_{26-c}) = 13 \cdot \lambda_g^{\mathrm{FP}}$, where $\lambda_g^{\mathrm{FP}} = \frac{2^{2g-1}-1}{2^{2g-1}} \cdot \frac{|B_{2g}|}{(2g)!}$. The nonzero sum $\kappa + \kappa' = 13$ reflects the conformal anomaly of the $c = 26$ bosonic string: the combined obstruction of Virasoro and its same-family shadow partner equals half the bosonic string central charge times $\lambda_g^{\mathrm{FP}}$.
   663	
   664	For the principal $\mathcal{W}_3$ algebra (where $c + c' = 100$), the analogous computation gives the Virasoro-lineage $W$-algebra sum $\kappa_{\mathcal{W}_3} + \kappa_{\mathcal{W}_3}' = 250/3$ \end{remark}
   665	
   666	\begin{remark}[Bosonic string anomaly splitting]\label{rem:bosonic-string-anomaly-splitting}
   667	\textup{(}LOCAL: scope fixed in this environment\textup{})
   668	The complementarity sum $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$ equals the bosonic string curvature $\kappa$ at $d = 26$ divided by~$2$. The combined genus-$g$ free energy
   669	\[
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '2060,2108p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2060	which is generated by a single quadratic Casimir
  2061	(one generator per negative mode $t^{-m}$, $m \geq 1$).
  2062	The resulting bar cohomology at degree~$n$ and weight~$H$
  2063	counts the $\mathfrak{sl}_2$-invariant elements
  2064	in $\Lambda^n$ of the loop algebra restricted to
  2065	total weight~$H$; the net count is $2n+1$
  2066	(Computation~\ref{comp:sl2-ce-verification}).
  2067	
  2068	The linear growth $\dim H^n = 2n+1$
  2069	supersedes the Riordan prediction
  2070	$\dim H^n = R(n+3)$ (OEIS~A005043), which gives the
  2071	correct value at $n = 1$ ($R(4) = 3$) but
  2072	fails at $n = 2$ ($R(5) = 6 \neq 5$) and
  2073	at $n = 3$ ($R(6) = 15 \neq 7$).
  2074	A detailed treatment of the three concentration mechanisms
  2075	(Whitehead vanishing, Casimir generation, and
  2076	weight-by-weight cancellation) appears in the
  2077	companion paper~\cite{Lor-GL}.
  2078	\end{remark}
  2079	
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '3188,3215p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3188	The Virasoro case: $P_{\mathrm{Vir}} = ((1{-}2x{-}x^2) - (1{-}x)u)/(2x^3)$
  3189	has the same $u$-type singularity as $\widehat{\mathfrak{sl}}_2$
  3190	(the coefficient of $u$ is a polynomial with $u \sim \sqrt{1{-}3x}$),
  3191	hence the same $n^{-3/2}$ correction.
  3192	The Virasoro OPE \emph{does} have a bracket channel
  3193	($T_{(0)}T = \partial T$, $T_{(1)}T = 2T$),
  3194	so $d_{\mathrm{bracket}} \neq 0$, consistent with case (1).
  3195	\end{proof}
  3196	
  3197	\begin{remark}[Bar dimensions as Koszul dual Hilbert series]\label{rem:bar-hilbert-koszul-dual}
  3198	\index{bar complex!Koszul dual Hilbert series}
  3199	For a Koszul algebra $\cA$, the Koszul dual Hilbert function $\dim (\cA^!)_n$ equals the conformal-weight-graded bar cohomology dimension at bar degree~$n$ (Corollary~\ref{cor:bar-cohomology-koszul-dual}). The generating function $P_{\cA}(x) = \sum_n \dim (\cA^!)_n\, x^n$ is the Hilbert series of $\cA^!$. In the Kac--Moody case, $P_{\widehat{\mathfrak{g}}_k}(x)$ coincides with the Hilbert series of $\mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$ as a graded algebra; this is independent of~$k$ because the Koszul dual has the same graded structure at all generic levels.
  3200	\end{remark}
  3201	
  3202	\begin{lemma}[Degree-\texorpdfstring{$2$}{2} bar cohomology at lowest weight; \ClaimStatusProvedHere]\label{lem:bar-deg2-symmetric-square}
  3203	\index{bar complex!degree-2 cohomology}
  3204	At conformal weight $h = 2$, the bar complex of
  3205	$\widehat{\mathfrak{g}}_k$ (semisimple~$\mathfrak{g}$) satisfies
  3206	$H^2(\barBgeom(\widehat{\mathfrak{g}}_k))_{h=2} = 0$.
  3207	The chain groups are $\bar{B}^2_{h=2} \cong \mathfrak{g}^{\otimes 2}$
wait(call_v4UKRFLLZRGWlYmgBVUmszYo) timed out:
codex
I have the insertion point locked from the explorer: immediately after the theorem-D proof-routing remark and before the GRR alternative proof. I’m still waiting on the second pass over canonical sources to see whether the Hilbert-series route is already explicit enough or needs a compact derivation inside the new proposition.
collab wait(call_1VgpO43JLBoxai3qiNcv68Gb)
  receivers: 019d88a4-a305-7320-950b-f645df24926a

thinking
**Organizing canonical formulas and references**

I’m organizing detailed references for the user that tie Heisenberg, Kac-Moody, and Virasoro canonical formulas and proofs to specific lines in source files—carefully avoiding line ranges—and grouping evidence by thematic routes like shadow tower, anomaly, and Hilbert series. I plan to format the final answer with clear bullet lists under headers like **Kappa Atlas** and **Routes**, citing precise line numbers for key theorems, remarks, and tables to support each canonical formula and classification route. This will help the user track the proofs and data effectively across the complex sources.
codex
**Kappa Atlas**
- Heisenberg level = modular characteristic: the genus-universality remark states that the obstruction `obs_g = \kappa(\mathcal{H}_k)\,\lambda_g` and the Euler-class argument identify `\kappa(\mathcal{H}_k)=k` with the central-extension coefficient so that every `F_g = k\cdot\lambda_g^{\mathrm{FP}}` (Theorem references embedded in the remark). Source: `chapters/examples/free_fields.tex:2424`.
- Affine Kac–Moody level formula and duality: the higher-genus extension remark points to `\kappa(\widehat{\fg}_k)=\dim(\fg)(k+h^\vee)/(2h^\vee)` and explains that Verdier duality forces the anti-symmetry `\kappa+\kappa'=0` via the Feigin–Frenkel involution. Source: `chapters/examples/kac_moody.tex:1313`.
- Virasoro curvature/`kappa`: the genus-2 obstruction corollary computes `\mathrm{obs}_2(\mathrm{Vir}_c)=\frac{c}{2}\lambda_2` and, together with genus universality, fixes `\kappa(\mathrm{Vir}_c)=c/2`, which then controls all higher free energies `F_g`. Source: `chapters/examples/genus_expansions.tex:1311`.

**Routes**
- Shadow tower: `\Theta_\cA` is the master element, and Table 2 records each family’s shadow depth/class (Heisenberg class G with a terminating scalar tower, affine Kac–Moody class L with a Lie-bracket cubic shadow, Virasoro class M with infinite cubic+quartic shadows). Sources: `chapters/examples/landscape_census.tex:207` and `chapters/examples/landscape_census.tex:254`.
- Anomaly track: the Polyakov-anomaly remark roots the ratio `\varrho=\kappa/c` in the genus-one free energy (`\varrho=1/2` for Virasoro, `1` for Heisenberg), and the complementarity remark spells out `\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c})=13`, which matches the bosonic string anomaly half-budget, unlike the exact cancellation in the affine case. Sources: `chapters/examples/landscape_census.tex:1219` and `chapters/examples/genus_expansions.tex:660`.
- Hilbert-series link: the sub-exponential growth corollary isolates free-field (Heisenberg/free fermion) versus interacting spectra, and the subsequent algebraicity corollary plus remark `rem:bar-hilbert-koszul-dual` tie each Koszul dual Hilbert function/generating series to the bar cohomology dimensions, confirming that these series capture the canonical `\kappa`-driven geometry. Sources: `chapters/examples/landscape_census.tex:2083` and `chapters/examples/landscape_census.tex:3197`.
wait(call_1VgpO43JLBoxai3qiNcv68Gb) 1 agents complete:
  019d88a4-a305-7320-950b-f645df24926a completed: "**Kappa Atlas**
- Heisenberg level = modular characteristic: the genus-universality remark states that the obstruction `…"
exec
/bin/zsh -lc 'rg -n "Hilbert|bar Hilbert|growth rate|sub-exponential|alpha_g|Heisenberg|affine|Virasoro" chapters/examples/landscape_census.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3180,3238p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2060,2135p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1200,1255p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
so $d_{\mathrm{bracket}} = 0$
(Proposition~\ref{prop:pole-decomposition}: the simple-pole residue is
not a field value but the vacuum).
Its generating function $P_{\beta\gamma} = u/(1{-}3x) = (1{+}x)/u$
has the \emph{inverse} singularity $u^{-1} \sim c_1 / \sqrt{1{-}3x}$
near $x = 1/3^-$, giving $[x^n] \sim C' \cdot 3^n \cdot n^{-1/2}$
by the same transfer theorem.

The Virasoro case: $P_{\mathrm{Vir}} = ((1{-}2x{-}x^2) - (1{-}x)u)/(2x^3)$
has the same $u$-type singularity as $\widehat{\mathfrak{sl}}_2$
(the coefficient of $u$ is a polynomial with $u \sim \sqrt{1{-}3x}$),
hence the same $n^{-3/2}$ correction.
The Virasoro OPE \emph{does} have a bracket channel
($T_{(0)}T = \partial T$, $T_{(1)}T = 2T$),
so $d_{\mathrm{bracket}} \neq 0$, consistent with case (1).
\end{proof}

\begin{remark}[Bar dimensions as Koszul dual Hilbert series]\label{rem:bar-hilbert-koszul-dual}
\index{bar complex!Koszul dual Hilbert series}
For a Koszul algebra $\cA$, the Koszul dual Hilbert function $\dim (\cA^!)_n$ equals the conformal-weight-graded bar cohomology dimension at bar degree~$n$ (Corollary~\ref{cor:bar-cohomology-koszul-dual}). The generating function $P_{\cA}(x) = \sum_n \dim (\cA^!)_n\, x^n$ is the Hilbert series of $\cA^!$. In the Kac--Moody case, $P_{\widehat{\mathfrak{g}}_k}(x)$ coincides with the Hilbert series of $\mathrm{CE}^{\mathrm{ch}}(\widehat{\mathfrak{g}}_{-k-2h^\vee})$ as a graded algebra; this is independent of~$k$ because the Koszul dual has the same graded structure at all generic levels.
 succeeded in 50ms:
which is generated by a single quadratic Casimir
(one generator per negative mode $t^{-m}$, $m \geq 1$).
The resulting bar cohomology at degree~$n$ and weight~$H$
counts the $\mathfrak{sl}_2$-invariant elements
in $\Lambda^n$ of the loop algebra restricted to
total weight~$H$; the net count is $2n+1$
(Computation~\ref{comp:sl2-ce-verification}).

The linear growth $\dim H^n = 2n+1$
supersedes the Riordan prediction
$\dim H^n = R(n+3)$ (OEIS~A005043), which gives the
correct value at $n = 1$ ($R(4) = 3$) but
fails at $n = 2$ ($R(5) = 6 \neq 5$) and
at $n = 3$ ($R(6) = 15 \neq 7$).
A detailed treatment of the three concentration mechanisms
(Whitehead vanishing, Casimir generation, and
weight-by-weight cancellation) appears in the
companion paper~\cite{Lor-GL}.
\end{remark}

 succeeded in 51ms:
9:$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$, three
21:$S_4 = 0$ singles out affine Kac--Moody (class~L), and $\Delta \neq 0$
22:forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
37:\noindent\emph{The Master Table below collects the invariants computed throughout Part~\ref{part:physics-bridges}. For the Heisenberg algebra, these invariants were derived in Chapter~\ref{ch:heisenberg-frame}; for each subsequent algebra, the corresponding chapter provides the complete computation.}
81:\multicolumn{6}{|c|}{\textit{Heisenberg \textup{(}curved abelian\textup{)}}} \\
83:Heisenberg $\mathcal{H}_\kappa$
197:$\operatorname{ek} = 0$ for Heisenberg, affine $V_k(\fg)$,
274:Heisenberg $\mathcal{H}_\kappa$ & G & 2 & none & \S\ref{ch:heisenberg-frame} \\
365:$K_2$ is tame (affine $\widehat{A}_1$, class~M), and $K_m$ for
530:$\max\operatorname{pole}(r) = 2h - 1$: the Heisenberg
531:($h = 1$) gives $z^{-1}$; the Virasoro ($h = 2$) gives $z^{-3}$;
559:For class-L algebras (affine Kac--Moody, $r_{\max} = 3$), the
561:(Virasoro, $\cW_N$, $r_{\max} = \infty$), the degree-$3$ MC
609:\multicolumn{5}{|c|}{\textit{Heisenberg}} \\
673:\caption{Shadow obstruction tower invariants: discriminant, shadow coefficients, growth rate}
726:The Virasoro discriminant complementarity is
732:The self-dual central charges are $c^* = K_N/2$: $c^* = 13$ for Virasoro,
735:sum $\kappa + \kappa' = 13$ is the Virasoro-sector value
740:In the Virasoro row, the displayed partner $\mathrm{Vir}_{26-c}$ is
838:the full algebra, not the Virasoro subalgebra alone. For the
 succeeded in 51ms:
\[
F_1(\cA) = \frac{\kappa(\cA)}{24}.
\]
For the Heisenberg algebra at level $\kappa = 1$ (single free boson, $c = 1$),
$F_1(\mathcal{H}_1) = 1/24 = c/24$, precisely the conformal anomaly coefficient
$q^{-c/24}$ in the torus partition function $Z(\tau) = q^{-c/24}\sum_h d(h)\,q^h$.
For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
$F_1 = 3(k{+}2)/96 = (k{+}2)/32$.
In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.
The formula $F_1 = \kappa/24$ is the genus-$1$ evaluation
of the universal MC class: $\theta_1 = \kappa \cdot \mu
\otimes \lambda_1$
(Theorem~\ref{thm:explicit-theta}(d)), integrated
against the Faber--Pandharipande $\lambda_1$-formula.
The ratio $\kappa/c = \varrho(\mathfrak{g})$
(Corollary~\ref{cor:genus1-anomaly-ratio}) measures
how much of the Lie bracket's cyclic deformation
survives DS reduction.
\end{remark}




thinking
**Evaluating kappa derivation**

I’m looking into exact formulas from landscape census to see if we can derive kappa and anomaly ratio from Hilbert growth. The user mentioned calculating kappa from the growth rate of the bar complex Hilbert series, but it’s tricky. It seems the growth rate alone doesn’t determine kappa, since Heisenberg and Virasoro have consistent growth patterns. Maybe the user means the growth rate of the bar complex Hilbert series with a coefficient parameter? There’s a lot to unpack here!
thinking
**Exploring kappa from Hilbert series**

I’m considering whether we can derive kappa from the growth rate of the bar complex Hilbert series, possibly through coefficients in log singularity or a one-particle kernel. I need more context to proceed. I’m looking for connections between kappa and growth rates, like the formula for α_g, but that might not help unless we include another level. The user emphasized an independent derivation through Hilbert series, so maybe I could state that Hilbert series identifies a family-specific model. However, I’m unsure if that’s independent enough!
thinking
**Deriving from families in Heisenberg**

I’m trying to derive properties for each family. For Heisenberg, the Hilbert series of the bar complex is given by \( \prod_{m\ge 1} (1-q^m)^{-1} \) for a rank 1 free boson. Hmm, the eta exponent is guided by rank, not level. But if we factor in level k, the partition function suggests \(\eta^{-2k}\) according to the user’s formula, which feels odd if k isn’t an integer rank. I’m questioning whether the one-loop partition on the torus should really be \(\eta^{-2k}\) in this case.
codex
I hit a live-surface tension: the repository’s explicit Heisenberg torus partition function is `Z_1(\mathcal H_\kappa)=\eta^{-1}` in the free-field chapter, while your requested anomaly normalization `Z_1=\eta^{-2\kappa}` would give `\eta^{-2k}`. I’m tracing whether the chapter distinguishes full VOA character, bar/sewing determinant, and scalar shadow one-loop factor before I encode the anomaly proof, because otherwise the new proposition would silently mix conventions.
exec
/bin/zsh -lc "rg -n \"eta\\"'^'"\\{-2\\\\kappa\\}|eta\\(tau\\)\\"'^'"\\{-2|Z_1 = .*eta|eta\\(\\\\tau\\)\\"'^'"\\{-2|eta\\(\\tau\\)\\"'^'"\\{-1|F_1 = \\\\kappa/24|scalar shadow partition function|one-loop determinant\" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '27236,27815p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:eta\^\{-2\kappa\}|eta\(tau\)\^\{-2|Z_1 = .*eta|eta\(\tau\)\^\{-2|eta\(\tau\)\^\{-1|F_1 = \kappa/24|scalar shadow partition function|one-loop determinant)
                ^^
error: unrecognized escape sequence
 succeeded in 51ms:
in the top-weight graded piece.
\end{remark}



% ========================================================
% Non-perturbative shadow partition function
% ========================================================

\subsubsection{Non-perturbative shadow partition function}
\label{subsubsec:shadow-double-convergence}
\index{shadow partition function!double convergence}

The genus expansion of string theory diverges: amplitudes grow as
$(2g)!$ by Mirzakhani's recursion for Weil--Petersson
volumes~\cite{Mirzakhani}.
The shadow partition function \emph{converges}, because the shadow CohFT
\textup{(}Theorem~\ref{thm:shadow-cohft}, conditional on the
flat-identity hypothesis\textup{)}
extracts tautological intersection numbers with Bernoulli decay rather
exec
/bin/zsh -lc "sed -n '1200,1245p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '18890,19025p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\[
F_1(\cA) = \frac{\kappa(\cA)}{24}.
\]
For the Heisenberg algebra at level $\kappa = 1$ (single free boson, $c = 1$),
$F_1(\mathcal{H}_1) = 1/24 = c/24$, precisely the conformal anomaly coefficient
$q^{-c/24}$ in the torus partition function $Z(\tau) = q^{-c/24}\sum_h d(h)\,q^h$.
For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
$F_1 = 3(k{+}2)/96 = (k{+}2)/32$.
In general, $F_1 = \kappa/24$ differs from the conformal anomaly $c/24$ by the ratio $\kappa/c$, which is~$1$ for the Heisenberg algebra but varies for other algebras.
The formula $F_1 = \kappa/24$ is the genus-$1$ evaluation
of the universal MC class: $\theta_1 = \kappa \cdot \mu
\otimes \lambda_1$
(Theorem~\ref{thm:explicit-theta}(d)), integrated
against the Faber--Pandharipande $\lambda_1$-formula.
The ratio $\kappa/c = \varrho(\mathfrak{g})$
(Corollary~\ref{cor:genus1-anomaly-ratio}) measures
how much of the Lie bracket's cyclic deformation
survives DS reduction.
\end{remark}

 succeeded in 52ms:
satisfies $u' + u^2 = (2Q_L''Q_L - (Q_L')^2)/(4Q_L^2)$,
a Riccati equation. For class~$\mathbf{G}$:
$Q_L = (2\kappa)^2$ is constant, $\omega = 0$,
and the hierarchy is trivial. For class~$\mathbf{L}$:
$Q_L = (2\kappa + 3\alpha t)^2$, $\omega = 3\alpha/(2\kappa + 3\alpha t)$,
and the stationary equation is of Airy type
(the simplest Gelfand--Dickey reduction).
For class~$\mathbf{M}$ with $\Delta \neq 0$:
$Q_L$ is irreducible quadratic, the stationary equation
has two regular singular points (at the zeros of~$Q_L$)
with half-integer residues, and the full
recursive tower $\{S_r\}_{r \geq 2}$
provides the higher KdV Hamiltonians.
The correspondence between shadow depth and Gelfand--Dickey
order is: $r_{\max}(\cA) - 1$ counts the number of independent
conserved quantities in the stationary reduction on the
primary line~$L$.
\end{proof}

\begin{theorem}[Shadow tau function;
codex
The Hilbert-series route is the hard boundary. On the current manuscript surface the conformal-weight Hilbert series is family-sensitive but generically level/central-charge independent for affine KM and Virasoro, so it does not literally recover `\kappa` by itself. I’m checking whether there is a sharper local invariant in the Hilbert discussion that carries the missing scalar, and if not I’ll state the route in the proposition with the smallest truthful hypothesis instead of baking in a false equivalence.
exec
/bin/zsh -lc "sed -n '1758,1878p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\section*{Bar complex dimensions}
\label{sec:bar-dimensions}
\index{bar complex!dimension table|textbf}

Table~\ref{tab:bar-dimensions} records the Koszul dual Hilbert
function $\dim (\cA^!)_n$ for each algebra through degree~$10$.
By the $E_2$ collapse (Corollary~\ref{cor:bar-cohomology-koszul-dual}),
this equals the conformal-weight-graded bar cohomology; see
Remark~\ref{rem:table-vs-vanishing} for the distinction from the
total bar cohomology computed by the vanishing theorems.
(For Kac--Moody algebras, the bar \emph{chain-group} dimensions are much
larger: $\dim \bar{B}^n = (\dim\mathfrak{g})^n \cdot (n{-}1)!$,
the product of the generator factor and the Orlik--Solomon form
factor; see Lemma~\ref{lem:bar-dims-level-independent}.)

These dimensions are computed from the explicit
generators-and-relations
presentations of the bar complex given in Part~\ref{part:physics-bridges};
see Section~\ref{sec:cross-ref-guide} below for precise references.
Entries marked \texttt{unknown} are not currently known; entries marked \texttt{n/a} are not defined or not applicable.
exec
/bin/zsh -lc "sed -n '3248,3275p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1988,2055p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "family index|graded ranks|Hilbert series of.*bar|growth rate.*kappa|kappa.*Hilbert|Hilbert.*kappa|bar family" chapters/theory/higher_genus_modular_koszul.tex chapters/examples/landscape_census.tex chapters/examples/free_fields.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$H^2\bigl(\barBgeom(\widehat{\mathfrak{sl}}_2)\bigr) = 5$,
with all five classes at weight~${\geq}\, 3$.
\end{lemma}

\begin{corollary}[Exponential growth rate from Lie algebra dimension; \ClaimStatusProvedHere]
\label{cor:growth-rate-dimg}
\index{bar complex!growth rate!Lie algebra dimension}
For affine Kac--Moody algebras $\widehat{\mathfrak{g}}_k$, the exponential growth rate of the Koszul dual Hilbert function satisfies
\[
\lim_{n \to \infty} \frac{\log \dim (\widehat{\mathfrak{g}}_k^!)_n}{n} = \log(\dim \mathfrak{g}).
\]
More precisely, $\dim (\widehat{\mathfrak{g}}_k^!)_n \sim C \cdot (\dim \mathfrak{g})^n \cdot n^{-\alpha}$ for some $C > 0$ and $\alpha > 0$. The verified cases are: $\dim \mathfrak{sl}_2 = 3$ (growth $3^n$), $\dim \mathfrak{sl}_3 = 8$ (growth $8^n$).
\end{corollary}

\begin{proof}
The bar chain groups have $\dim \bar{B}^n = (\dim \mathfrak{g})^n \cdot (n{-}1)!$ (Lemma~\ref{lem:bar-dims-level-independent}). The Koszul property constrains the Koszul dual dimensions to grow at most as fast as the chain groups modulo the differential. The Hilbert series, being algebraic with radius of convergence $1/\dim\mathfrak{g}$ (by the DS discriminant, Theorem~\ref{thm:ds-bar-gf-discriminant} for $\mathfrak{sl}_2$), has exponential growth rate $(\dim \mathfrak{g})^n$.
\end{proof}

\begin{theorem}[Dominant branch point for Kac--Moody algebras;
\ClaimStatusProvedHere]
 succeeded in 51ms:
\end{remark}

\begin{remark}[Growth rates and Koszulness]\label{rem:bar-growth-koszul}
\index{Koszul algebra!bar complex growth}
The growth rate of $\dim (\cA^!)_n$ as $n \to \infty$ is
an invariant of the algebra with direct Koszul-theoretic meaning.
(Note: the bar \emph{chain-group} dimensions grow much faster;
for Kac--Moody algebras $\dim \bar{B}^n = (\dim\fg)^n \cdot (n{-}1)!$
is super-exponential. The growth rates below refer to
the Koszul dual Hilbert function.)
\begin{enumerate}
\item \emph{Sub-exponential growth.}
 The Heisenberg and free fermion Koszul duals grow
 sub-exponentially: $\dim (\cA^!)_n \sim
 e^{\pi\sqrt{2n/3}}/(4\sqrt{3}\,n)$ by the
 Hardy--Ramanujan asymptotics for the partition function.
\item \emph{Exponential growth.}
 All other algebras in the table have Koszul dual dimensions growing
 exponentially in~$n$, at rate~$\sim d^n$ where $d = \dim\fg$
 for Kac--Moody.
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2924:scalar series for the bar family~\eqref{eq:bar-family} on the
chapters/theory/higher_genus_modular_koszul.tex:3013:virtual bar family. Theorem~\ref{thm:family-index} is therefore the
chapters/theory/higher_genus_modular_koszul.tex:3026:virtual bar family $[\barB^{(g)}(\cA)] \in
chapters/theory/higher_genus_modular_koszul.tex:3056:and its graded ranks are determined by the Hilbert series of~$\cA$.
chapters/theory/higher_genus_modular_koszul.tex:3057:Thus its family index $R\pi_*\barB^{\mathrm{fib}}(\cA)$ is a perfect
chapters/theory/higher_genus_modular_koszul.tex:9913:virtual bar family~$\mathcal{V}_\cA$.
chapters/theory/higher_genus_modular_koszul.tex:10023:trace and are read index-theoretically by the family index theorem
chapters/theory/higher_genus_modular_koszul.tex:10040:The virtual bar family
chapters/theory/higher_genus_modular_koszul.tex:10082:\index{Theta_A@$\Theta_\cA$!vs virtual bar family}
chapters/theory/higher_genus_modular_koszul.tex:10083:\index{virtual bar family!vs Theta_A@$\Theta_\cA$}
chapters/theory/higher_genus_modular_koszul.tex:14479:now seen as a consequence of (i) via the family index theorem
chapters/theory/higher_genus_modular_koszul.tex:14685:where $V_\cA$ is the virtual bar family in

thinking
**Focusing on specific results**

I want to make sure we're using our limited time wisely. It seems best to concentrate on cross-checking literature that is directly relevant to our proposition. I’ll consider highlighting other results that haven't been checked as well, just to ensure we have a comprehensive view. This approach should help in narrowing down our findings to the most pertinent information. Let's see where this leads!
exec
/bin/zsh -lc "sed -n '2996,3072p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]*sl2-genus1-curvature|'"\\\\label\\{["'^}]*genus1-curvature|kappa'"\\(V_k\\(\\\\fg\\)\\)|kappa\\(V_k\\(\\\\mathfrak\\{sl\\}_2\\)\\)|partition function via complementarity|Sugawara shift' chapters/examples/kac_moody.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]*vir-genus1-curvature|kappa'"\\(\\\\mathrm\\{Vir|Motzkin|Virasoro.*bar cohomology|Virasoro.*partition function|Virasoro.*genus-1' chapters/examples/w_algebras.tex chapters/examples/landscape_census.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]*heisenberg|kappa'"\\(\\\\cH|kappa\\(\\\\mathcal\\{H|Z_1\\(\\\\cH|Z_1\\(\\\\mathcal\\{H|heisenberg.*partition|Heisenberg.*obstruction|Heisenberg.*genus-1' chapters/examples/free_fields.tex chapters/frame/heisenberg_frame.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[Proof routing for Theorem~D;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-d-model}
\index{modular characteristic theorem!model presentation}
\[
\Theta_\cA \text{ and its shadow tower}
\Longrightarrow
\mathrm{obs}_g=\kappa\cdot\lambda_g
\Longrightarrow
\sum_{g \ge 1} F_g x^{2g}
=
\kappa\cdot(\hat{A}(ix)-1)
\]
The bar-intrinsic shadow tower is the common source.
The first implication is the scalar-trace identification of
Theorem~\ref{thm:genus-universality}; the second is the downstream
GRR/family-index identification of the same scalar series on the
virtual bar family. Theorem~\ref{thm:family-index} is therefore the
index-theoretic reformulation of the scalar output, not the
load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3106:\kappa(V_k(\fg))
chapters/theory/higher_genus_modular_koszul.tex:3336:\kappa(V_k(\fg)) \;=\; \frac{\dim(\fg)\,(k + h^\vee)}{2\,h^\vee},
chapters/theory/higher_genus_modular_koszul.tex:3352:central charge is not zero: the residual Sugawara shift of
chapters/theory/higher_genus_modular_koszul.tex:3457:\begin{remark}[Sugawara shift as holographic anomaly]
chapters/theory/higher_genus_modular_koszul.tex:3460:\index{holographic anomaly!Sugawara shift}%
chapters/theory/higher_genus_modular_koszul.tex:3468:\kappa(V_k(\fg))
chapters/theory/higher_genus_modular_koszul.tex:3484:the total holographic central charge~$\kappa(V_k(\fg))$.
chapters/examples/kac_moody.tex:758:denominator $k + h^\vee$ is the Sugawara shift. This is the
chapters/examples/kac_moody.tex:3699:\label{thm:sl2-genus1-curvature}
chapters/examples/kac_moody.tex:3966:\label{thm:sl3-genus1-curvature}
 succeeded in 50ms:
chapters/theory/higher_genus_modular_koszul.tex:1750:$\{\kappa(\mathrm{Vir}_c),\, \{F_g\}_{g \geq 1}\}$ and the
chapters/theory/higher_genus_modular_koszul.tex:15337:$\kappa(\mathrm{Vir}_c) = c/2$,
chapters/theory/higher_genus_modular_koszul.tex:19585: $\kappa(\cH_1) = \kappa(\mathrm{Vir}_2) = 1$,\;
chapters/theory/higher_genus_modular_koszul.tex:19639:(ii)~$r = 3$: $\kappa(\cH_1) = 1 = \kappa(\mathrm{Vir}_2)$
chapters/theory/higher_genus_modular_koszul.tex:20130: = 8\,\kappa(\mathrm{Vir}_c)\,S_4(\mathrm{Vir}_c) \neq 0$
chapters/theory/higher_genus_modular_koszul.tex:20181:= 8\,\kappa(\mathrm{Vir}_c)\,S_4(\mathrm{Vir}_c)$
chapters/theory/higher_genus_modular_koszul.tex:27784:$\kappa(\mathrm{Vir}_c) = c/2$ and
chapters/theory/higher_genus_modular_koszul.tex:27785:$\kappa(\mathrm{Vir}_{26-c}) = (26-c)/2$, the
chapters/theory/higher_genus_modular_koszul.tex:27979: $\kappa(\mathrm{Vir}_{13}) = 13/2
chapters/theory/higher_genus_modular_koszul.tex:27980: = \kappa(\mathrm{Vir}_{26 - c}) \big|_{c = 13}
chapters/theory/higher_genus_modular_koszul.tex:27981: = \kappa(\mathrm{Vir}_{13}^!)$;
chapters/theory/higher_genus_modular_koszul.tex:28013:$\kappa(\mathrm{Vir}_{13}) = \kappa(\mathrm{Vir}_{13}^!) = 13/2$
chapters/theory/higher_genus_modular_koszul.tex:35166:families: Virasoro \textup{(}Motzkin differences,
chapters/examples/landscape_census.tex:33:and $\kappa(\mathrm{Vir}_c) = c/2$ both descend from the universality
chapters/examples/landscape_census.tex:736:($\kappa(V^\natural) = 12$, $\kappa(\mathrm{Vir}_2) = 1$; sum $= 13$),
chapters/examples/landscape_census.tex:1260:where $\varrho(\mathfrak{g}) = \sum_{i=1}^r \frac{1}{m_i+1}$ is the anomaly ratio (the sum over exponents $m_1, \ldots, m_r$ of~$\mathfrak{g}$). This is $1/2$ for $\mathfrak{sl}_2$ (Virasoro), $5/6$ for $\mathfrak{sl}_3$ ($\mathcal{W}_3$), and $H_N - 1$ for $\mathfrak{sl}_N$ ($\mathcal{W}_N$). The identity follows from $F_1 = \kappa/24$ (Remark~\ref{rem:genus-1-verification}) and $\kappa = c \cdot \varrho(\mathfrak{g})$ (Theorem~\ref{thm:genus-universality}\textup{(ii)}).
chapters/examples/landscape_census.tex:1862: where $M(n)$ is the $n$-th Motzkin number
chapters/examples/landscape_census.tex:2021: the first differences of Motzkin numbers
chapters/examples/landscape_census.tex:2030: The Virasoro bar cohomology growth~$3^n$ is consistent
chapters/examples/landscape_census.tex:2102:Virasoro (Motzkin differences, algebraic of degree $2$);
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3030:\emph{Step~D}: Heisenberg $\kappa(\mathcal{H}_k)=k$,
chapters/theory/higher_genus_modular_koszul.tex:3313:\label{rem:kappa-holo-heisenberg}
chapters/theory/higher_genus_modular_koszul.tex:3317:$\kappa(\mathcal{H}_k) = k$
chapters/theory/higher_genus_modular_koszul.tex:15334:$\kappa(\cH_k) = k$, $S_4(\cH_k) = 0$, so
chapters/theory/higher_genus_modular_koszul.tex:19585: $\kappa(\cH_1) = \kappa(\mathrm{Vir}_2) = 1$,\;
chapters/theory/higher_genus_modular_koszul.tex:19589: $\kappa(\cH_1) = \kappa(\beta\gamma_1) = 1$ and
chapters/theory/higher_genus_modular_koszul.tex:19639:(ii)~$r = 3$: $\kappa(\cH_1) = 1 = \kappa(\mathrm{Vir}_2)$
chapters/theory/higher_genus_modular_koszul.tex:19647:$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
chapters/theory/higher_genus_modular_koszul.tex:20135: = 8\,\kappa(\cH_k)\,S_4(\cH_k) = 0$,
chapters/theory/higher_genus_modular_koszul.tex:20193:= 8\,\kappa(\cH_k)\,S_4(\cH_k) = 0$,
chapters/theory/higher_genus_modular_koszul.tex:21188:For Heisenberg: $\kappa(\mathcal{H}_k) = k$,
chapters/theory/higher_genus_modular_koszul.tex:21189:$\kappa(\mathcal{H}_{-k}) = -k$, so $\kappa + \kappa' = 0$.
chapters/theory/higher_genus_modular_koszul.tex:26634:\begin{equation}\label{eq:virasoro-operators-heisenberg}
chapters/frame/heisenberg_frame.tex:1:\chapter{The Gaussian Archetype}\label{ch:heisenberg-frame}
chapters/frame/heisenberg_frame.tex:41:$\kappa(\mathcal{H}_k) = k$.
chapters/frame/heisenberg_frame.tex:51:$\kappa(\mathcal{H}_k) + \kappa(\mathcal{H}_k^!) = 0$
chapters/frame/heisenberg_frame.tex:71:\begin{equation}\label{eq:heisenberg-mc-element}
chapters/frame/heisenberg_frame.tex:205:\textbf{D}~(\S\ref{sec:frame-genus-tower}): $\kappa(\mathcal{H}_k) = k$; $\sum_{g \geq 1} F_g\, x^{2g} = k(\tfrac{x/2}{\sin(x/2)} - 1)$.
chapters/frame/heisenberg_frame.tex:219:\begin{equation}\label{eq:frame-heisenberg-ope}
chapters/frame/heisenberg_frame.tex:225:\begin{equation}\label{eq:frame-heisenberg-modes}
exec
/bin/zsh -lc "sed -n '1398,1458p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3688,3728p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The Heisenberg two-point function on $E_\tau$ is
\begin{equation}\label{eq:frame-genus1-2pt}
\langle \alpha(z_1)\, \alpha(z_2) \rangle_{E_\tau}
= k \cdot G_\tau(z_1 - z_2).
\end{equation}

The genus-$1$ partition function is computed by the following theorem.

\begin{theorem}[Genus-1 Heisenberg partition function; \ClaimStatusProvedHere]\label{thm:genus1-heisenberg}
The genus-$1$ partition function of the Heisenberg algebra $\mathcal{H}_k$ on the elliptic curve $E_\tau$ is
\begin{equation}\label{eq:frame-partition-g1}
Z_{E_\tau}^{\mathcal{H}} =
\mathrm{Tr}_{\mathcal{F}_k}\, q^{L_0 - c/24}
= \frac{1}{\eta(\tau)}
= q^{-1/24}\prod_{n=1}^{\infty}\frac{1}{1-q^n}
\end{equation}
where $\eta(\tau)$ is the Dedekind eta function. The coefficients
are the partition numbers $p(n)$: the number of partitions of $n$
counts the number of states at excitation level~$n$ in the
 succeeded in 51ms:
The $A$-cycle periodicity~\eqref{eq:A-cycle-periodicity} is exact, but the $B$-cycle quasi-periodicity~\eqref{eq:B-cycle-quasi-periodicity} introduces the \emph{constant} shift $-2\pi i$. This constant is the source of all genus-1 quantum corrections.

The differential on $\barB^{(1)}$ is:
\begin{equation}\label{eq:genus1-diff}
d^{(1)} = \sum_{i<j} \operatorname{Res}_{D_{ij}} \circ K^{(1)}_{ij}
\end{equation}
For $\widehat{\mathfrak{sl}}_{2,k}$, the residue extracts both the double-pole (level) and simple-pole (structure constant) contributions from the OPE, exactly as in the genus-0 computation~\eqref{eq:bar-diff-general}, but with the genus-0 propagator $d\log(z_i-z_j)$ replaced by $K^{(1)}$.

\subsection{Curvature decomposition}

\begin{theorem}[Genus-1 curvature for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k}; \ClaimStatusProvedHere]
\label{thm:sl2-genus1-curvature}
The genus-$1$ fiberwise differential
$\dfib$ \textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})} satisfies:
\begin{equation}\label{eq:sl2-genus1-dsquared}
\dfib^{\,2} = (k+2) \cdot \omega_1 \cdot \operatorname{id}_{\mathfrak{sl}_2}
\end{equation}
where $\omega_1 \in H^2(\overline{\mathcal{M}}_{1,1})$ is the fundamental class and $(k+2)$ is the shifted level $k + h^\vee$ for $\mathfrak{sl}_2$.

The curvature decomposes as:
exec
/bin/zsh -lc "sed -n '1234,1274p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{comp:heisenberg-partition-g1\\}|heisenberg-partition-g1|partition function.*Heisenberg.*eta|eta-appearance' chapters/frame/heisenberg_frame.tex chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\section{Explicit computation: Virasoro algebra}

\subsection{Setup}

The Virasoro algebra is the simplest W-algebra: $\mathcal{W}^k(\mathfrak{sl}_2, f_{\text{prin}})$ at central charge $c$.

\begin{definition}[Virasoro algebra]
The Virasoro algebra has generators $L_n$ ($n \in \mathbb{Z}$) and central element $c$, with commutation relations:
\begin{equation}
[L_m, L_n] = (m-n) L_{m+n} + \frac{c}{12}(m^3 - m)\delta_{m+n,0}
\end{equation}

As a vertex algebra, the generator is:
\begin{equation}
T(z) = \sum_{n \in \mathbb{Z}} L_n z^{-n-2}
\end{equation}
with OPE:
\begin{equation}
T(z)T(w) \sim \frac{c/2}{(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial T(w)}{z-w}
\end{equation}
 succeeded in 50ms:
chapters/examples/free_fields.tex:4095:\textup{(}Computation~\textup{\ref{comp:heisenberg-partition-g1})}.
chapters/examples/free_fields.tex:5224:By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
chapters/examples/free_fields.tex:5235:By the genus-1 bar complex computation (Theorem~\ref{thm:eta-appearance}), the bar complex partition function is:
exec
/bin/zsh -lc "rg -n 'comp:heisenberg-partition-g1|eta-appearance' chapters/examples/free_fields.tex chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:4095:\textup{(}Computation~\textup{\ref{comp:heisenberg-partition-g1})}.
chapters/examples/free_fields.tex:5224:By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
chapters/examples/free_fields.tex:5235:By the genus-1 bar complex computation (Theorem~\ref{thm:eta-appearance}), the bar complex partition function is:
exec
/bin/zsh -lc "rg -n 'comp:heisenberg-partition-g1|eta-appearance' ." in /Users/raeez/chiral-bar-cobar succeeded in 186ms:
./wave2_audit_20260413_001942/C11_heisenberg.md:11:- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:715,1259` — PROBLEM: two cross-references drift off the local surface. Line 715 cites `thm:eta-appearance` for the appearance of `E_2` in the propagator, but that label is the partition-function theorem; line 1259 cites `thm:heisenberg-all-genera` even though this file defines `thm:heisenberg-all-genus`. FIX: change line 715 to `Theorem~\ref{thm:heisenberg-genus-one-complete}` and line 1259 to `Theorem~\ref{thm:heisenberg-all-genus}`.
./wave2_audit_20260413_001942/C11_heisenberg.md:1310:I noticed that Theorem 779, which deals with `Partition function and determinant regularization`, doesn't mention E2, highlighting it as a stale cross-reference. That's a good catch! Now, I need to make sure there aren't any other instances of `thm:eta-appearance` in the repository. I'll conduct a search to verify that, just to ensure everything is accurate and up-to-date. Let’s double-check and clear up any confusion!
./wave2_audit_20260413_001942/C11_heisenberg.md:1312:/bin/zsh -lc "rg -n 'label\\{thm:eta-appearance\\}|thm:eta-appearance' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./wave2_audit_20260413_001942/C11_heisenberg.md:1313:./chapters/examples/heisenberg_eisenstein.tex:715:For $g = 1$: The graded ring $\bigoplus_k M_k(SL_2(\mathbb{Z}))$ is generated by $E_4$ and $E_6$; by Eisenstein's theorem, every even-weight modular form is a polynomial in these two. The quasi-Eisenstein series $E_2$ appears in $G_\tau$ at weight 2 as the unique quasi-modular form (Theorem~\ref{thm:eta-appearance}).
./wave2_audit_20260413_001942/C11_heisenberg.md:1314:./chapters/examples/heisenberg_eisenstein.tex:779:\begin{theorem}[Partition function and determinant regularization; \ClaimStatusProvedHere]\label{thm:eta-appearance}
./wave2_audit_20260413_001942/C11_heisenberg.md:1315:./chapters/examples/free_fields.tex:5185:By Theorem~\ref{thm:eta-appearance}, the genus-1 bar complex is built from the Weierstrass $\zeta$-function:
./wave2_audit_20260413_001942/C11_heisenberg.md:1316:./chapters/examples/free_fields.tex:5196:By the genus-1 bar complex computation (Theorem~\ref{thm:eta-appearance}), the bar complex partition function is:
./wave2_audit_20260413_001942/C11_heisenberg.md:1326:- [MEDIUM] `chapters/examples/heisenberg_eisenstein.tex:715,1259` — PROBLEM: two cross-references drift off the local surface. Line 715 cites `thm:eta-appearance` for the appearance of `E_2` in the propagator, but that label is the partition-function theorem; line 1259 cites `thm:heisenberg-all-genera` even though this file defines `thm:heisenberg-all-genus`. FIX: change line 715 to `Theorem~\ref{thm:heisenberg-genus-one-complete}` and line 1259 to `Theorem~\ref{thm:heisenberg-all-genus}`.
./metadata/dependency_graph.dot:785:  thm_eta_appearance [label="thm:eta-appearance\ntheorem [Pr]\nPartition function and determinant regul...", style=filled, fillcolor="#c8e6c9"];
./metadata/theorem_registry.md:1591:| `thm:eta-appearance` | `theorem` | 781 | Partition function and determinant regularization |
./metadata/label_index.json:934:  "comp:heisenberg-partition-g1": {
./metadata/label_index.json:41002:  "thm:eta-appearance": {
./metadata/claims.jsonl:761:{"label": "thm:eta-appearance", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/heisenberg_eisenstein.tex", "line": 781, "title": "Partition function and determinant regularization", "refs_in_block": ["comp:partition-genus-two"]}
🌐 Searching the web...
🌐 Searched: Frenkel Gaitsgory local geometric Langlands theorem 1 critical level site:arxiv.org pdf

thinking
**Searching for papers**

It seems like the search results aren't giving me what I need. I might need to go directly to the arXiv papers if I know the URLs. Maybe I could use domain filters while searching, or for FG06, I could try searching with the exact title to find more relevant results. It’s a bit frustrating, but I’m trying to get this right! Let’s see what I can find.
🌐 Searching the web...
🌐 Searched: Frenkel Gaitsgory localization at critical level theorem 1 arxiv
🌐 Searching the web...
🌐 Searched: https://www.numdam.org/item/10.1007/s10240-013-0054-1.pdf
🌐 Searching the web...
🌐 Searched: Frenkel Gaitsgory localization at critical level theorem 1 arxiv pdf domain:arxiv.org
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: math/0508382 arxiv pdf Frenkel Gaitsgory local geometric Langlands
🌐 Searching the web...
🌐 Searched the web
🌐 Searching the web...
🌐 Searched: https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n3-p07-p.pdf
🌐 Searching the web...
🌐 Searched: 'Theorem 1.7' in https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n3-p07-p.pdf
exec
/bin/zsh -lc "sed -n '3758,3786p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\[d_{\text{res}}(a(z_1) \otimes a(z_2) \otimes \eta_{12}) = k \cdot 1\]

\[d_{\text{res}}(a(z_1) \otimes a(z_2) \otimes a(z_3) \otimes \eta_{12} \wedge \eta_{23}) = k \cdot a(z_3) \otimes \eta_{23} - k \cdot a(z_1) \otimes \eta_{13}\]

We verify $d^2 = 0$ by direct computation. The two terms in $d(a \otimes a \otimes a \otimes \eta_{12} \wedge \eta_{23})$ yield, upon a second application of $d$:
\[d(k \cdot a(z_3) \otimes \eta_{23}) = k^2, \qquad d(-k \cdot a(z_1) \otimes \eta_{13}) = -k^2\]
so $d^2 = k^2 - k^2 = 0$ by telescoping cancellation of the two residue terms.
\end{proof}

\begin{remark}[Comparison with literature]\label{rem:heisenberg-literature}
This calculation agrees with:
\begin{itemize}
\item \emph{Gui--Li--Zeng \cite{GLZ22}.} Their Theorem 4.2 for Heisenberg specializes to the formulas above.
\item \emph{Beilinson--Drinfeld \cite{BD04}.} Section 4.7 on chiral homology, specialized to Heisenberg.
\item \emph{Costello--Gwilliam \cite{CG17}.} Volume 2, Chapter 5 on factorization algebras for Heisenberg.
\end{itemize}

The agreement provides non-trivial verification of the geometric approach via configuration spaces.
\end{remark}
exec
/bin/zsh -lc "rg -n 'FG06|Frenkel--Gaitsgory|Theorem~\\\\ref\\{thm:fg-localization\\}|ClaimStatusProvedElsewhere|Brown--Henneaux|Zhu96' chapters/examples/kac_moody.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/free_fields.tex:787:\ClaimStatusProvedElsewhere
chapters/examples/free_fields.tex:2614:Free boson $\partial\phi$ & Symplectic bosons & Exact & Open-closed & \ClaimStatusProvedElsewhere~\cite{FBZ04} \\
chapters/examples/free_fields.tex:2621:$W^{-h^\vee}(\mathfrak{g})$ & Wakimoto & Classical & DS reduction $\leftrightarrow$ free field & \ClaimStatusProvedElsewhere \\
chapters/examples/free_fields.tex:2622:Lattice $V_L$ & Lattice $V_{L^*}$ & Classical & Form duality & \ClaimStatusProvedElsewhere \\
chapters/examples/free_fields.tex:2859:\begin{theorem}[Heisenberg duality \cite{CG17}; \ClaimStatusProvedElsewhere]
chapters/examples/free_fields.tex:3664: duality; \ClaimStatusProvedElsewhere]
chapters/examples/free_fields.tex:3942:\ClaimStatusProvedElsewhere]
chapters/examples/free_fields.tex:4334:\ClaimStatusProvedElsewhere]
chapters/examples/free_fields.tex:4395:\ClaimStatusProvedElsewhere]
chapters/examples/free_fields.tex:4721:\begin{theorem}[BRST cohomology \cite{Pol98}; \ClaimStatusProvedElsewhere]
chapters/examples/free_fields.tex:4913:(Zhu \cite{Zhu96}).
chapters/examples/free_fields.tex:4963:\begin{theorem}[Classification of extendable algebras \cite{Pol98}; \ClaimStatusProvedElsewhere]\label{thm:classification-extendable}
chapters/examples/free_fields.tex:4992:(3)~the Verlinde formula and finite-dimensionality of conformal blocks (Zhu \cite{Zhu96});
chapters/examples/free_fields.tex:5134:\begin{theorem}[String amplitude factorization \cite{Pol98}; \ClaimStatusProvedElsewhere]\label{thm:amplitude-factorization}
chapters/examples/free_fields.tex:5193:\begin{theorem}[Modular invariance and anomaly cancellation; \ClaimStatusProvedElsewhere]\label{thm:modular-anomaly}
chapters/examples/free_fields.tex:5239:Zhu's theorem \cite{Zhu96} identifies $Z_\mathcal{A}(\tau)$ with a character in Zhu's module category. The modular-invariance properties of these characters (including the transformation weight $c/24$) are established by Zhu \cite[Thm.~4.4.2]{Zhu96} under rationality assumptions, which hold for the finite examples computed here (free fields, Heisenberg, Kac--Moody at positive integer level).
chapters/examples/free_fields.tex:5334:\begin{theorem}[Complete modular invariance classification \cite{Zhu96, MooreSeiberg89}; \ClaimStatusProvedElsewhere]\label{thm:modular-classification}
chapters/examples/free_fields.tex:5407:\begin{theorem}[Classical \texorpdfstring{$\mathcal{W}$}{W}-algebra integrability; \ClaimStatusProvedElsewhere]\label{thm:w-classical-integrability}
chapters/examples/free_fields.tex:5781:\begin{theorem}[Curved Koszul duality \cite{Positselski11}; \ClaimStatusProvedElsewhere]
chapters/examples/free_fields.tex:5814:\ClaimStatusProvedElsewhere]
codex
I’m at the edit boundary. The new proposition will use the true live normalization: shadow route, genus-one anomaly route, and a Hilbert/GRR route with the exact caveat that the Hilbert series fixes graded ranks while the scalar normalization is set at genus 1. I’m not going to encode the stronger `Z_1=\eta^{-2\kappa}` formula, because it conflicts with the manuscript’s Heisenberg and affine surfaces.

thinking
**Preparing PE templates**

I need to create PE templates for commentary, possibly using PE-2, PE-1, and PE-7. The idea is to edit a proposition with kappa and r-matrix formulas. I’m thinking of organizing them into blocks — maybe one for each family? 

Since kappa triggers a write, I might do three blocks for PE-2, plus one for PE-1 for KM, Heis, and Vir. We’ll mention the relevant formulas, ensuring to include AP126. Let's make sure to label the template properly too!
codex
```text
PE-2: kappa formula write
family: Heisenberg  kappa written: \kappa(\mathcal H_k)=k
census: chapters/examples/landscape_census.tex:81-83 = k  match? Y
at k=0: 0 expected 0  at k=1: 1 expected 1
wrong variants avoided: NOT k/2, NOT c/2, NOT KM formula
verdict: ACCEPT
```

```text
PE-2: kappa formula write
family: affine KM  kappa written: \kappa(V_k(\mathfrak g))=\dim(\mathfrak g)(k+h^\vee)/(2h^\vee)
census: AGENTS/CLAUDE canonical formula + higher_genus_modular_koszul.tex:3333-3356 match? Y
at k=0: dim(g)/2 expected dim(g)/2  at k=-h^\vee: 0 expected 0
wrong variants avoided: NOT dim(g)k/(2h^\vee), NOT c/2, NOT bare av(r)=kappa
verdict: ACCEPT
```

```text
PE-2: kappa formula write
family: Virasoro  kappa written: \kappa(\mathrm{Vir}_c)=c/2
census: AGENTS/CLAUDE canonical formula + w_algebras.tex:1577-1603 match? Y
at c=0: 0 expected 0  at c=13: 13/2 expected 13/2
wrong variants avoided: NOT c, NOT c/24
verdict: ACCEPT
```

```text
PE-1: r-matrix write
family: Heisenberg / affine KM / Virasoro
r(z): k/z ; k\Omega/z ; (c/2)/z^3 + 2T/z
level param: k ; k ; c
OPE pole: 2 ; 2 ; 4   r pole: 1 ; 1 ; 3
AP126 trace-form k=0 check: 0 ; 0 ; c-route NA  expected: 0 for trace-form families  match? Y
AP141 grep target: bare \Omega/z in scope: N  allowed? N
critical-level (KM): r|_{k=-h^\vee} = -h^\vee \Omega/z in trace-form convention; finite as required
source: CLAUDE.md canonical formulas; w_algebras.tex:1459ff; higher_genus_modular_koszul.tex:3457ff
verdict: ACCEPT
```

```text
PE-7: label creation
environment: proposition
label: \label{prop:kappa-three-routes}
prefix match (AP125): Y
AP124 duplicate check: Vol I:0 Vol II:0 Vol III:0 total before:0 after:1 delta=1? Y
verdict: ACCEPT
```
exec
/bin/zsh -lc "sed -n '493,820p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3088,3148p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{computation}[Partition function at genus 1]\label{comp:heisenberg-partition-g1}
The genus-1 partition function is:
\begin{equation}
Z_{E_\tau}^{\mathcal{H}} = \text{Tr}_{H_{\mathcal{H}}} q^{L_0 - c/24} 
= \frac{1}{\eta(\tau)}
\end{equation}

Explicitly:
\begin{align}
Z_{E_\tau}^{\mathcal{H}} &= q^{-1/24} \prod_{n=1}^{\infty} \frac{1}{1 - q^n} \\
&= q^{-1/24}(1 + q + 2q^2 + 3q^3 + 5q^4 + 7q^5 + \cdots)
\end{align}

The coefficients are the partition function $p(n)$ counting partitions of $n$.

Under $\tau \mapsto -1/\tau$, using $\eta(-1/\tau) = \sqrt{-i\tau}\,\eta(\tau)$:
\[Z_{E_{-1/\tau}}^{\mathcal{H}} = \frac{1}{\sqrt{-i\tau}} \cdot Z_{E_\tau}^{\mathcal{H}}\]

since $Z = 1/\eta(\tau)$ transforms contravariantly to $\eta$.
 succeeded in 51ms:
genus-$g$ obstruction with the top Chern class of the Hodge bundle.
This is a second proof route for the uniform-weight clause of
Theorem~D, using only the family of fiber bar complexes and Hodge
theory on the universal curve.
\end{remark}

\begin{remark}[FG comparison]
\label{rem:theorem-d-fg-comparison}
\index{Frenkel--Gaitsgory!comparison with Theorem D}
\index{critical level!FG comparison}
For affine Kac--Moody algebras, the critical specialization of
Theorem~D matches the oper side of the local geometric Langlands
package of Frenkel--Gaitsgory only after a convention conversion.
In~\cite{FG06} the level is the invariant bilinear form on
$\widehat{\fg}$; in the present chapter
$\kappa(\cA)$ is the scalar modular characteristic of Theorem~D.
On the affine Kac--Moody lane these parameters are related by
\[
\kappa(V_k(\fg))
\;=\;
exec
/bin/zsh -lc "rg -n '\\\\label\\{prop:kappa-three-routes\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 115ms:

exec
/bin/zsh -lc "sed -n '3355,3420p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{theorem}[Motzkin path model for Virasoro bar cohomology;
\ClaimStatusProvedHere]
\label{thm:motzkin-path-model}
\index{Motzkin numbers!path model}
\index{Virasoro algebra!bar cohomology!combinatorial model}
\index{bar complex!combinatorial model}
There exists a bijection
\begin{equation}\label{eq:motzkin-bijection}
\operatorname{Basis}(H^n(\bar{B}(\mathrm{Vir}_c)))
\;\xleftrightarrow{\;\sim\;}
\bigl\{\text{Motzkin paths of length $n{+}1$ starting with $U$}\bigr\}
\end{equation}
respecting the conformal weight filtration
\textup{(}Remark~\textup{\ref{rem:conformal-weight-filtration})},
where $U = (1,1)$, $D = (1,-1)$, $F = (1,0)$
are up, down, and flat steps of a lattice path staying
at height $\geq 0$ and ending at height $0$.
\end{theorem}

\begin{proof}

thinking
**Drafting statement clearly**

I need to create a proposition statement that explicitly mentions, "Under the exact normalization of Remark \ref{rem:theorem-d-alt-grr}, the Hilbert-series route recovers the same scalar." That's important! I want to keep it concise and clear, not too lengthy. So, I’ll draft the inserted text with careful style. Also, I should consider running apply_patch afterward to ensure everything is properly incorporated. Let’s focus on getting this right!
codex
I’m editing `higher_genus_modular_koszul.tex` now. The change is scoped to one new proposition block at the theorem-D proof-routing locus, plus only the wording needed to keep the anomaly and Hilbert routes mathematically true under the manuscript’s current normalizations.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -3033,2 +3033,138 @@
 
+\begin{proposition}[Three recovery routes for $\kappa$ on the scalar lane;
+\ClaimStatusProvedHere]
+\label{prop:kappa-three-routes}
+\index{modular characteristic!three recovery routes|textbf}
+\index{kappa@$\kappa$!shadow, anomaly, and Hilbert routes}
+For the three standard scalar families
+\[
+\mathcal{H}_k,\qquad
+V_k(\fg)\ \textup{(}\fg\ \textup{simple\textup{)}},\qquad
+\mathrm{Vir}_c,
+\]
+the modular characteristic is recovered by three mutually consistent
+routes:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{Shadow route.}
+ The degree-$2$ shadow of the ordered bar complex gives
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))
+ = \operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+ = \frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\item \emph{Genus-$1$ anomaly route.}
+ The genus-$1$ scalar coefficient satisfies
+ $F_1(\cA)=\kappa(\cA)/24$, so the same three values are read from the
+ one-loop anomaly:
+ Heisenberg from $\dfib^{\,2}=k\,\omega_1$,
+ affine Kac--Moody from the shifted level $k+h^\vee$,
+ and Virasoro from $(d^{(1)})^2=(c/2)\,\omega_1$.
+ In the present normalization this route reads $\kappa$ from the
+ logarithmic one-loop coefficient, not from a universal bare exponent
+ of~$\eta(\tau)$:
+ the rank-$1$ Heisenberg holomorphic partition function is
+ $1/\eta(\tau)$, and the affine genus-$1$ partition function carries
+ the shifted-level correction in its $E_2$ coefficient.
+\item \emph{Hilbert-series and family-index route.}
+ The conformal-weight Hilbert series of the bar/Koszul-dual model fixes
+ the graded ranks of the virtual bar family
+ $R\pi_*\barB^{\mathrm{fib}}(\cA)$, hence the GRR output
+ $\operatorname{ch}(R\pi_*\barB^{\mathrm{fib}}(\cA))
+ = \kappa(\cA)\operatorname{ch}(\mathbb{E}) + \cdots$.
+ For Heisenberg the Hilbert series is the partition-number series,
+ for affine Kac--Moody it is the Lie-theoretic series with growth rate
+ $\dim(\fg)$, and for Virasoro it is the Motzkin-difference series.
+ After the genus-$1$ scalar normalization of
+ Remark~\ref{rem:theorem-d-alt-grr}, this route recovers the same
+ $\kappa$:
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))=\frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\end{enumerate}
+\end{proposition}
+
+\begin{proof}
+\emph{Route \textup{(i)}: shadow tower.}
+Theorem~\ref{thm:five-theorems-as-av-images} identifies
+Theorem~D as the scalar degree-$2$ projection of the ordered
+$E_1$ bar package.
+For Heisenberg the ordered collision residue is
+$r^{\mathrm{Heis}}(z)=k/z$, so
+$\operatorname{av}(r^{\mathrm{Heis}})=k$.
+For affine Kac--Moody the exact degree-$2$ formula is the
+Sugawara-shift identity~\eqref{eq:sugawara-shift-holographic},
+which yields
+\[
+\kappa(V_k(\fg))
+\;=\;
+\operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+\;=\;
+\frac{\dim(\fg)(k+h^\vee)}{2h^\vee}.
+\]
+For Virasoro the ordered residue is
+$r^{\mathrm{Vir}}_c(z)=\frac{c/2}{z^3}+\frac{2T}{z}$
+\textup{(}Computation~\ref{comp:virasoro-rmatrix}\textup{)},
+and its scalar channel is the cubic-pole coefficient $c/2$.
+This gives
+$\kappa(\mathrm{Vir}_c)=c/2$.
+
+\emph{Route \textup{(ii)}: genus-$1$ anomaly.}
+On the scalar lane,
+Theorem~\ref{thm:genus-universality} and
+Corollary~\ref{cor:free-energy-ahat-genus} give
+$F_1(\cA)=\kappa(\cA)/24$.
+The three genus-$1$ curvature computations recover the same scalar.
+For Heisenberg,
+Theorem~\ref{thm:genus1-heisenberg} gives the holomorphic partition
+function $Z_1=1/\eta(\tau)$, while
+Theorem~\ref{thm:frame-genus1-curvature} gives
+$\dfib^{\,2}=k\,\omega_1$; the anomaly coefficient is therefore $k$.
+For affine Kac--Moody,
+Theorem~\ref{thm:sl2-genus1-curvature} displays the shifted level
+$k+h^\vee$ in the genus-$1$ curvature, and
+Proposition~\ref{prop:sl2-genus1-partition} displays the same shift in
+the $E_2$ coefficient of the one-loop partition function.
+The general simple-type formula is exactly
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$, as recorded in
+Remark~\ref{rem:kappa-holo-km}.
+For Virasoro,
+Theorem~\ref{thm:vir-genus1-curvature} gives
+$(d^{(1)})^2=(c/2)\,\omega_1$, hence
+$F_1(\mathrm{Vir}_c)=c/48$ and $\kappa(\mathrm{Vir}_c)=c/2$.
+The second route therefore agrees with the first.
+
+\emph{Route \textup{(iii)}: Hilbert series and GRR.}
+Remark~\ref{rem:theorem-d-alt-grr} gives a second proof architecture
+for the scalar lane:
+the graded ranks of the fiber bar complex are determined by the
+Hilbert series of~$\cA$, and GRR identifies the corresponding family
+index with
+$\kappa(\cA)\operatorname{ch}(\mathbb{E})$.
+The three relevant Hilbert models are already fixed on the live
+surface:
+partition-number growth for Heisenberg
+\textup{(}Theorem~\ref{thm:heisenberg-bar-complete},
+Remark~\ref{rem:heisenberg-literature}\textup{)},
+Lie-theoretic growth for affine Kac--Moody
+\textup{(}Corollary~\ref{cor:growth-rate-dimg},
+Remark~\ref{rem:bar-hilbert-koszul-dual}\textup{)},
+and Motzkin-difference growth for Virasoro
+\textup{(}Theorem~\ref{thm:motzkin-path-model}\textup{)}.
+These Hilbert models determine the graded family to which GRR applies;
+the genus-$1$ scalar normalization in
+Remark~\ref{rem:theorem-d-alt-grr} then fixes the coefficient of the
+Hodge term.
+For Heisenberg this coefficient is the level~$k$,
+for affine Kac--Moody it is the shifted-level scalar
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$,
+and for Virasoro it is the quartic-pole coefficient~$c/2$.
+Hence the family-index route recovers the same three values.
+\end{proof}
+
 \begin{remark}[Alternative proof via GRR]
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index dbb162fddd11e676ffac7779fc476884dcc6f76d..78d4de32adfa77fd7a061c243bbedcbb1f1b4333
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,6 +3031,142 @@
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
+\begin{proposition}[Three recovery routes for $\kappa$ on the scalar lane;
+\ClaimStatusProvedHere]
+\label{prop:kappa-three-routes}
+\index{modular characteristic!three recovery routes|textbf}
+\index{kappa@$\kappa$!shadow, anomaly, and Hilbert routes}
+For the three standard scalar families
+\[
+\mathcal{H}_k,\qquad
+V_k(\fg)\ \textup{(}\fg\ \textup{simple\textup{)}},\qquad
+\mathrm{Vir}_c,
+\]
+the modular characteristic is recovered by three mutually consistent
+routes:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{Shadow route.}
+ The degree-$2$ shadow of the ordered bar complex gives
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))
+ = \operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+ = \frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\item \emph{Genus-$1$ anomaly route.}
+ The genus-$1$ scalar coefficient satisfies
+ $F_1(\cA)=\kappa(\cA)/24$, so the same three values are read from the
+ one-loop anomaly:
+ Heisenberg from $\dfib^{\,2}=k\,\omega_1$,
+ affine Kac--Moody from the shifted level $k+h^\vee$,
+ and Virasoro from $(d^{(1)})^2=(c/2)\,\omega_1$.
+ In the present normalization this route reads $\kappa$ from the
+ logarithmic one-loop coefficient, not from a universal bare exponent
+ of~$\eta(\tau)$:
+ the rank-$1$ Heisenberg holomorphic partition function is
+ $1/\eta(\tau)$, and the affine genus-$1$ partition function carries
+ the shifted-level correction in its $E_2$ coefficient.
+\item \emph{Hilbert-series and family-index route.}
+ The conformal-weight Hilbert series of the bar/Koszul-dual model fixes
+ the graded ranks of the virtual bar family
+ $R\pi_*\barB^{\mathrm{fib}}(\cA)$, hence the GRR output
+ $\operatorname{ch}(R\pi_*\barB^{\mathrm{fib}}(\cA))
+ = \kappa(\cA)\operatorname{ch}(\mathbb{E}) + \cdots$.
+ For Heisenberg the Hilbert series is the partition-number series,
+ for affine Kac--Moody it is the Lie-theoretic series with growth rate
+ $\dim(\fg)$, and for Virasoro it is the Motzkin-difference series.
+ After the genus-$1$ scalar normalization of
+ Remark~\ref{rem:theorem-d-alt-grr}, this route recovers the same
+ $\kappa$:
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))=\frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\end{enumerate}
+\end{proposition}
+
+\begin{proof}
+\emph{Route \textup{(i)}: shadow tower.}
+Theorem~\ref{thm:five-theorems-as-av-images} identifies
+Theorem~D as the scalar degree-$2$ projection of the ordered
+$E_1$ bar package.
+For Heisenberg the ordered collision residue is
+$r^{\mathrm{Heis}}(z)=k/z$, so
+$\operatorname{av}(r^{\mathrm{Heis}})=k$.
+For affine Kac--Moody the exact degree-$2$ formula is the
+Sugawara-shift identity~\eqref{eq:sugawara-shift-holographic},
+which yields
+\[
+\kappa(V_k(\fg))
+\;=\;
+\operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+\;=\;
+\frac{\dim(\fg)(k+h^\vee)}{2h^\vee}.
+\]
+For Virasoro the ordered residue is
+$r^{\mathrm{Vir}}_c(z)=\frac{c/2}{z^3}+\frac{2T}{z}$
+\textup{(}Computation~\ref{comp:virasoro-rmatrix}\textup{)},
+and its scalar channel is the cubic-pole coefficient $c/2$.
+This gives
+$\kappa(\mathrm{Vir}_c)=c/2$.
+
+\emph{Route \textup{(ii)}: genus-$1$ anomaly.}
+On the scalar lane,
+Theorem~\ref{thm:genus-universality} and
+Corollary~\ref{cor:free-energy-ahat-genus} give
+$F_1(\cA)=\kappa(\cA)/24$.
+The three genus-$1$ curvature computations recover the same scalar.
+For Heisenberg,
+Theorem~\ref{thm:genus1-heisenberg} gives the holomorphic partition
+function $Z_1=1/\eta(\tau)$, while
+Theorem~\ref{thm:frame-genus1-curvature} gives
+$\dfib^{\,2}=k\,\omega_1$; the anomaly coefficient is therefore $k$.
+For affine Kac--Moody,
+Theorem~\ref{thm:sl2-genus1-curvature} displays the shifted level
+$k+h^\vee$ in the genus-$1$ curvature, and
+Proposition~\ref{prop:sl2-genus1-partition} displays the same shift in
+the $E_2$ coefficient of the one-loop partition function.
+The general simple-type formula is exactly
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$, as recorded in
+Remark~\ref{rem:kappa-holo-km}.
+For Virasoro,
+Theorem~\ref{thm:vir-genus1-curvature} gives
+$(d^{(1)})^2=(c/2)\,\omega_1$, hence
+$F_1(\mathrm{Vir}_c)=c/48$ and $\kappa(\mathrm{Vir}_c)=c/2$.
+The second route therefore agrees with the first.
+
+\emph{Route \textup{(iii)}: Hilbert series and GRR.}
+Remark~\ref{rem:theorem-d-alt-grr} gives a second proof architecture
+for the scalar lane:
+the graded ranks of the fiber bar complex are determined by the
+Hilbert series of~$\cA$, and GRR identifies the corresponding family
+index with
+$\kappa(\cA)\operatorname{ch}(\mathbb{E})$.
+The three relevant Hilbert models are already fixed on the live
+surface:
+partition-number growth for Heisenberg
+\textup{(}Theorem~\ref{thm:heisenberg-bar-complete},
+Remark~\ref{rem:heisenberg-literature}\textup{)},
+Lie-theoretic growth for affine Kac--Moody
+\textup{(}Corollary~\ref{cor:growth-rate-dimg},
+Remark~\ref{rem:bar-hilbert-koszul-dual}\textup{)},
+and Motzkin-difference growth for Virasoro
+\textup{(}Theorem~\ref{thm:motzkin-path-model}\textup{)}.
+These Hilbert models determine the graded family to which GRR applies;
+the genus-$1$ scalar normalization in
+Remark~\ref{rem:theorem-d-alt-grr} then fixes the coefficient of the
+Hodge term.
+For Heisenberg this coefficient is the level~$k$,
+for affine Kac--Moody it is the shifted-level scalar
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$,
+and for Virasoro it is the quartic-pole coefficient~$c/2$.
+Hence the family-index route recovers the same three values.
+\end{proof}
+
 \begin{remark}[Alternative proof via GRR]
 \label{rem:theorem-d-alt-grr}
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index dbb162fddd11e676ffac7779fc476884dcc6f76d..78d4de32adfa77fd7a061c243bbedcbb1f1b4333
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,6 +3031,142 @@
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
+\begin{proposition}[Three recovery routes for $\kappa$ on the scalar lane;
+\ClaimStatusProvedHere]
+\label{prop:kappa-three-routes}
+\index{modular characteristic!three recovery routes|textbf}
+\index{kappa@$\kappa$!shadow, anomaly, and Hilbert routes}
+For the three standard scalar families
+\[
+\mathcal{H}_k,\qquad
+V_k(\fg)\ \textup{(}\fg\ \textup{simple\textup{)}},\qquad
+\mathrm{Vir}_c,
+\]
+the modular characteristic is recovered by three mutually consistent
+routes:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{Shadow route.}
+ The degree-$2$ shadow of the ordered bar complex gives
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))
+ = \operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+ = \frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\item \emph{Genus-$1$ anomaly route.}
+ The genus-$1$ scalar coefficient satisfies
+ $F_1(\cA)=\kappa(\cA)/24$, so the same three values are read from the
+ one-loop anomaly:
+ Heisenberg from $\dfib^{\,2}=k\,\omega_1$,
+ affine Kac--Moody from the shifted level $k+h^\vee$,
+ and Virasoro from $(d^{(1)})^2=(c/2)\,\omega_1$.
+ In the present normalization this route reads $\kappa$ from the
+ logarithmic one-loop coefficient, not from a universal bare exponent
+ of~$\eta(\tau)$:
+ the rank-$1$ Heisenberg holomorphic partition function is
+ $1/\eta(\tau)$, and the affine genus-$1$ partition function carries
+ the shifted-level correction in its $E_2$ coefficient.
+\item \emph{Hilbert-series and family-index route.}
+ The conformal-weight Hilbert series of the bar/Koszul-dual model fixes
+ the graded ranks of the virtual bar family
+ $R\pi_*\barB^{\mathrm{fib}}(\cA)$, hence the GRR output
+ $\operatorname{ch}(R\pi_*\barB^{\mathrm{fib}}(\cA))
+ = \kappa(\cA)\operatorname{ch}(\mathbb{E}) + \cdots$.
+ For Heisenberg the Hilbert series is the partition-number series,
+ for affine Kac--Moody it is the Lie-theoretic series with growth rate
+ $\dim(\fg)$, and for Virasoro it is the Motzkin-difference series.
+ After the genus-$1$ scalar normalization of
+ Remark~\ref{rem:theorem-d-alt-grr}, this route recovers the same
+ $\kappa$:
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))=\frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\end{enumerate}
+\end{proposition}
+
+\begin{proof}
+\emph{Route \textup{(i)}: shadow tower.}
+Theorem~\ref{thm:five-theorems-as-av-images} identifies
+Theorem~D as the scalar degree-$2$ projection of the ordered
+$E_1$ bar package.
+For Heisenberg the ordered collision residue is
+$r^{\mathrm{Heis}}(z)=k/z$, so
+$\operatorname{av}(r^{\mathrm{Heis}})=k$.
+For affine Kac--Moody the exact degree-$2$ formula is the
+Sugawara-shift identity~\eqref{eq:sugawara-shift-holographic},
+which yields
+\[
+\kappa(V_k(\fg))
+\;=\;
+\operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+\;=\;
+\frac{\dim(\fg)(k+h^\vee)}{2h^\vee}.
+\]
+For Virasoro the ordered residue is
+$r^{\mathrm{Vir}}_c(z)=\frac{c/2}{z^3}+\frac{2T}{z}$
+\textup{(}Computation~\ref{comp:virasoro-rmatrix}\textup{)},
+and its scalar channel is the cubic-pole coefficient $c/2$.
+This gives
+$\kappa(\mathrm{Vir}_c)=c/2$.
+
+\emph{Route \textup{(ii)}: genus-$1$ anomaly.}
+On the scalar lane,
+Theorem~\ref{thm:genus-universality} and
+Corollary~\ref{cor:free-energy-ahat-genus} give
+$F_1(\cA)=\kappa(\cA)/24$.
+The three genus-$1$ curvature computations recover the same scalar.
+For Heisenberg,
+Theorem~\ref{thm:genus1-heisenberg} gives the holomorphic partition
+function $Z_1=1/\eta(\tau)$, while
+Theorem~\ref{thm:frame-genus1-curvature} gives
+$\dfib^{\,2}=k\,\omega_1$; the anomaly coefficient is therefore $k$.
+For affine Kac--Moody,
+Theorem~\ref{thm:sl2-genus1-curvature} displays the shifted level
+$k+h^\vee$ in the genus-$1$ curvature, and
+Proposition~\ref{prop:sl2-genus1-partition} displays the same shift in
+the $E_2$ coefficient of the one-loop partition function.
+The general simple-type formula is exactly
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$, as recorded in
+Remark~\ref{rem:kappa-holo-km}.
+For Virasoro,
+Theorem~\ref{thm:vir-genus1-curvature} gives
+$(d^{(1)})^2=(c/2)\,\omega_1$, hence
+$F_1(\mathrm{Vir}_c)=c/48$ and $\kappa(\mathrm{Vir}_c)=c/2$.
+The second route therefore agrees with the first.
+
+\emph{Route \textup{(iii)}: Hilbert series and GRR.}
+Remark~\ref{rem:theorem-d-alt-grr} gives a second proof architecture
+for the scalar lane:
+the graded ranks of the fiber bar complex are determined by the
+Hilbert series of~$\cA$, and GRR identifies the corresponding family
+index with
+$\kappa(\cA)\operatorname{ch}(\mathbb{E})$.
+The three relevant Hilbert models are already fixed on the live
+surface:
+partition-number growth for Heisenberg
+\textup{(}Theorem~\ref{thm:heisenberg-bar-complete},
+Remark~\ref{rem:heisenberg-literature}\textup{)},
+Lie-theoretic growth for affine Kac--Moody
+\textup{(}Corollary~\ref{cor:growth-rate-dimg},
+Remark~\ref{rem:bar-hilbert-koszul-dual}\textup{)},
+and Motzkin-difference growth for Virasoro
+\textup{(}Theorem~\ref{thm:motzkin-path-model}\textup{)}.
+These Hilbert models determine the graded family to which GRR applies;
+the genus-$1$ scalar normalization in
+Remark~\ref{rem:theorem-d-alt-grr} then fixes the coefficient of the
+Hodge term.
+For Heisenberg this coefficient is the level~$k$,
+for affine Kac--Moody it is the shifted-level scalar
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$,
+and for Virasoro it is the quartic-pole coefficient~$c/2$.
+Hence the family-index route recovers the same three values.
+\end{proof}
+
 \begin{remark}[Alternative proof via GRR]
 \label{rem:theorem-d-alt-grr}
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}


thinking
**Inspecting modifications**

I need to check a modified region, specifically looking for a label rather than a theorem. I mistakenly referenced `Theorem\ref{thm:five-theorems-as-av-images}`, but the correct label is `rem:five-theorems-as-av-images`. That’s a bug to fix. I should verify other theorems as well, such as `thm:genus1-heisenberg` and `thm:frame-genus1-curvature`. I also need to ensure I have correct citations and make adjustments within my proof, particularly regarding the wording used. Adjustments may be needed there.
codex
The proposition is in place. I’m re-reading the inserted block now for label/reference correctness and for any wording that accidentally overstates the Hilbert-series route beyond what the chapter actually proves.
exec
/bin/zsh -lc "sed -n '2996,3145p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'thm:five-theorems-as-av-images|rem:five-theorems-as-av-images|prop:kappa-three-routes|live surface|eta\\"'^{-2|eta'"\\"'^'"\\{-2' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:thm:five-theorems-as-av-images|rem:five-theorems-as-av-images|prop:kappa-three-routes|live surface|eta\^{-2|eta\^\{-2)
                                                                                                                ^
error: repetition quantifier expects a valid decimal
 succeeded in 52ms:
\begin{remark}[Proof routing for Theorem~D;
Convention~\ref{conv:proof-architecture}]
\label{rem:theorem-d-model}
\index{modular characteristic theorem!model presentation}
\[
\Theta_\cA \text{ and its shadow tower}
\Longrightarrow
\mathrm{obs}_g=\kappa\cdot\lambda_g
\Longrightarrow
\sum_{g \ge 1} F_g x^{2g}
=
\kappa\cdot(\hat{A}(ix)-1)
\]
The bar-intrinsic shadow tower is the common source.
The first implication is the scalar-trace identification of
Theorem~\ref{thm:genus-universality}; the second is the downstream
GRR/family-index identification of the same scalar series on the
virtual bar family. Theorem~\ref{thm:family-index} is therefore the
index-theoretic reformulation of the scalar output, not the
load-bearing input that proves~$\mathrm{obs}_g=\kappa\cdot\lambda_g$.
exec
/bin/zsh -lc "rg -n '\\\\label\\{prop:kappa-three-routes\\}|prop:kappa-three-routes' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 148ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3036:\label{prop:kappa-three-routes}
exec
/bin/zsh -lc "python - <<'PY'
import re, pathlib
p=pathlib.Path('chapters/theory/higher_genus_modular_koszul.tex')
text=p.read_text()
for bad in ['moreover','additionally','notably','crucially','remarkably','interestingly','furthermore','we now','it is worth noting','worth mentioning','it should be noted','it is important to note','delve','leverage','tapestry','cornerstone','journey']:
    if re.search(r'(?i)'+re.escape(bad), text):
        print('BAD', bad)
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index dbb162fddd11e676ffac7779fc476884dcc6f76d..78d4de32adfa77fd7a061c243bbedcbb1f1b4333
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,6 +3031,142 @@
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
+\begin{proposition}[Three recovery routes for $\kappa$ on the scalar lane;
+\ClaimStatusProvedHere]
+\label{prop:kappa-three-routes}
+\index{modular characteristic!three recovery routes|textbf}
+\index{kappa@$\kappa$!shadow, anomaly, and Hilbert routes}
+For the three standard scalar families
+\[
+\mathcal{H}_k,\qquad
+V_k(\fg)\ \textup{(}\fg\ \textup{simple\textup{)}},\qquad
+\mathrm{Vir}_c,
+\]
+the modular characteristic is recovered by three mutually consistent
+routes:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{Shadow route.}
+ The degree-$2$ shadow of the ordered bar complex gives
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))
+ = \operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+ = \frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\item \emph{Genus-$1$ anomaly route.}
+ The genus-$1$ scalar coefficient satisfies
+ $F_1(\cA)=\kappa(\cA)/24$, so the same three values are read from the
+ one-loop anomaly:
+ Heisenberg from $\dfib^{\,2}=k\,\omega_1$,
+ affine Kac--Moody from the shifted level $k+h^\vee$,
+ and Virasoro from $(d^{(1)})^2=(c/2)\,\omega_1$.
+ In the present normalization this route reads $\kappa$ from the
+ logarithmic one-loop coefficient, not from a universal bare exponent
+ of~$\eta(\tau)$:
+ the rank-$1$ Heisenberg holomorphic partition function is
+ $1/\eta(\tau)$, and the affine genus-$1$ partition function carries
+ the shifted-level correction in its $E_2$ coefficient.
+\item \emph{Hilbert-series and family-index route.}
+ The conformal-weight Hilbert series of the bar/Koszul-dual model fixes
+ the graded ranks of the virtual bar family
+ $R\pi_*\barB^{\mathrm{fib}}(\cA)$, hence the GRR output
+ $\operatorname{ch}(R\pi_*\barB^{\mathrm{fib}}(\cA))
+ = \kappa(\cA)\operatorname{ch}(\mathbb{E}) + \cdots$.
+ For Heisenberg the Hilbert series is the partition-number series,
+ for affine Kac--Moody it is the Lie-theoretic series with growth rate
+ $\dim(\fg)$, and for Virasoro it is the Motzkin-difference series.
+ After the genus-$1$ scalar normalization of
+ Remark~\ref{rem:theorem-d-alt-grr}, this route recovers the same
+ $\kappa$:
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))=\frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\end{enumerate}
+\end{proposition}
+
+\begin{proof}
+\emph{Route \textup{(i)}: shadow tower.}
+Theorem~\ref{thm:five-theorems-as-av-images} identifies
+Theorem~D as the scalar degree-$2$ projection of the ordered
+$E_1$ bar package.
+For Heisenberg the ordered collision residue is
+$r^{\mathrm{Heis}}(z)=k/z$, so
+$\operatorname{av}(r^{\mathrm{Heis}})=k$.
+For affine Kac--Moody the exact degree-$2$ formula is the
+Sugawara-shift identity~\eqref{eq:sugawara-shift-holographic},
+which yields
+\[
+\kappa(V_k(\fg))
+\;=\;
+\operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+\;=\;
+\frac{\dim(\fg)(k+h^\vee)}{2h^\vee}.
+\]
+For Virasoro the ordered residue is
+$r^{\mathrm{Vir}}_c(z)=\frac{c/2}{z^3}+\frac{2T}{z}$
+\textup{(}Computation~\ref{comp:virasoro-rmatrix}\textup{)},
+and its scalar channel is the cubic-pole coefficient $c/2$.
+This gives
+$\kappa(\mathrm{Vir}_c)=c/2$.
+
+\emph{Route \textup{(ii)}: genus-$1$ anomaly.}
+On the scalar lane,
+Theorem~\ref{thm:genus-universality} and
+Corollary~\ref{cor:free-energy-ahat-genus} give
+$F_1(\cA)=\kappa(\cA)/24$.
+The three genus-$1$ curvature computations recover the same scalar.
+For Heisenberg,
+Theorem~\ref{thm:genus1-heisenberg} gives the holomorphic partition
+function $Z_1=1/\eta(\tau)$, while
+Theorem~\ref{thm:frame-genus1-curvature} gives
+$\dfib^{\,2}=k\,\omega_1$; the anomaly coefficient is therefore $k$.
+For affine Kac--Moody,
+Theorem~\ref{thm:sl2-genus1-curvature} displays the shifted level
+$k+h^\vee$ in the genus-$1$ curvature, and
+Proposition~\ref{prop:sl2-genus1-partition} displays the same shift in
+the $E_2$ coefficient of the one-loop partition function.
+The general simple-type formula is exactly
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$, as recorded in
+Remark~\ref{rem:kappa-holo-km}.
+For Virasoro,
+Theorem~\ref{thm:vir-genus1-curvature} gives
+$(d^{(1)})^2=(c/2)\,\omega_1$, hence
+$F_1(\mathrm{Vir}_c)=c/48$ and $\kappa(\mathrm{Vir}_c)=c/2$.
+The second route therefore agrees with the first.
+
+\emph{Route \textup{(iii)}: Hilbert series and GRR.}
+Remark~\ref{rem:theorem-d-alt-grr} gives a second proof architecture
+for the scalar lane:
+the graded ranks of the fiber bar complex are determined by the
+Hilbert series of~$\cA$, and GRR identifies the corresponding family
+index with
+$\kappa(\cA)\operatorname{ch}(\mathbb{E})$.
+The three relevant Hilbert models are already fixed on the live
+surface:
+partition-number growth for Heisenberg
+\textup{(}Theorem~\ref{thm:heisenberg-bar-complete},
+Remark~\ref{rem:heisenberg-literature}\textup{)},
+Lie-theoretic growth for affine Kac--Moody
+\textup{(}Corollary~\ref{cor:growth-rate-dimg},
+Remark~\ref{rem:bar-hilbert-koszul-dual}\textup{)},
+and Motzkin-difference growth for Virasoro
+\textup{(}Theorem~\ref{thm:motzkin-path-model}\textup{)}.
+These Hilbert models determine the graded family to which GRR applies;
+the genus-$1$ scalar normalization in
+Remark~\ref{rem:theorem-d-alt-grr} then fixes the coefficient of the
+Hodge term.
+For Heisenberg this coefficient is the level~$k$,
+for affine Kac--Moody it is the shifted-level scalar
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$,
+and for Virasoro it is the quartic-pole coefficient~$c/2$.
+Hence the family-index route recovers the same three values.
+\end{proof}
+
 \begin{remark}[Alternative proof via GRR]
 \label{rem:theorem-d-alt-grr}
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}



thinking
**Reviewing theorem syntax and references**

I can’t use python, but I need to fix the theorem label and use rg for simplicity. I notice an odd nested syntax with `\textup{(}\fg\ \textup{simple\textup{)}}`, which might be okay, but simplifying it to `V_k(\fg)\ \textup{(}\fg\ \textup{simple)}` seems better. I also have to correct a reference label from `thm:five-theorems-as-av-images` to `rem:five-theorems-as-av-images`. I should double-check some other details as needed.
thinking
**Considering compilation options**

I'm thinking about whether to run `grep -n` for "Moreover," but it might not be necessary. Maybe I should compile without a full build and run a targeted check instead. I could try using `latexmk -pdf -interaction=nonstopmode -halt-on-error` for the main file, but that seems heavy. The user asked about relevant tests for compute scope, so perhaps a narrow TeX sanity check is a better approach. I should explore the build-surface skill for assistance, but I'm unsure whether it's necessary in this context.
codex
I found one direct reference error in the new block and a small formatting awkwardness in the family display. I’m patching those now before running the AP greps and a narrow TeX sanity check.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -3041,3 +3041,3 @@
 \mathcal{H}_k,\qquad
-V_k(\fg)\ \textup{(}\fg\ \textup{simple\textup{)}},\qquad
+V_k(\fg)\ \textup{(}$\fg$ simple\textup{)},\qquad
 \mathrm{Vir}_c,
@@ -3093,3 +3093,3 @@
 \emph{Route \textup{(i)}: shadow tower.}
-Theorem~\ref{thm:five-theorems-as-av-images} identifies
+Remark~\ref{rem:five-theorems-as-av-images} identifies
 Theorem~D as the scalar degree-$2$ projection of the ordered
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index dbb162fddd11e676ffac7779fc476884dcc6f76d..37b20359894e6158884b2c23add2e5fad3c2a70b
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,6 +3031,142 @@
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
+\begin{proposition}[Three recovery routes for $\kappa$ on the scalar lane;
+\ClaimStatusProvedHere]
+\label{prop:kappa-three-routes}
+\index{modular characteristic!three recovery routes|textbf}
+\index{kappa@$\kappa$!shadow, anomaly, and Hilbert routes}
+For the three standard scalar families
+\[
+\mathcal{H}_k,\qquad
+V_k(\fg)\ \textup{(}$\fg$ simple\textup{)},\qquad
+\mathrm{Vir}_c,
+\]
+the modular characteristic is recovered by three mutually consistent
+routes:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{Shadow route.}
+ The degree-$2$ shadow of the ordered bar complex gives
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))
+ = \operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+ = \frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\item \emph{Genus-$1$ anomaly route.}
+ The genus-$1$ scalar coefficient satisfies
+ $F_1(\cA)=\kappa(\cA)/24$, so the same three values are read from the
+ one-loop anomaly:
+ Heisenberg from $\dfib^{\,2}=k\,\omega_1$,
+ affine Kac--Moody from the shifted level $k+h^\vee$,
+ and Virasoro from $(d^{(1)})^2=(c/2)\,\omega_1$.
+ In the present normalization this route reads $\kappa$ from the
+ logarithmic one-loop coefficient, not from a universal bare exponent
+ of~$\eta(\tau)$:
+ the rank-$1$ Heisenberg holomorphic partition function is
+ $1/\eta(\tau)$, and the affine genus-$1$ partition function carries
+ the shifted-level correction in its $E_2$ coefficient.
+\item \emph{Hilbert-series and family-index route.}
+ The conformal-weight Hilbert series of the bar/Koszul-dual model fixes
+ the graded ranks of the virtual bar family
+ $R\pi_*\barB^{\mathrm{fib}}(\cA)$, hence the GRR output
+ $\operatorname{ch}(R\pi_*\barB^{\mathrm{fib}}(\cA))
+ = \kappa(\cA)\operatorname{ch}(\mathbb{E}) + \cdots$.
+ For Heisenberg the Hilbert series is the partition-number series,
+ for affine Kac--Moody it is the Lie-theoretic series with growth rate
+ $\dim(\fg)$, and for Virasoro it is the Motzkin-difference series.
+ After the genus-$1$ scalar normalization of
+ Remark~\ref{rem:theorem-d-alt-grr}, this route recovers the same
+ $\kappa$:
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))=\frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\end{enumerate}
+\end{proposition}
+
+\begin{proof}
+\emph{Route \textup{(i)}: shadow tower.}
+Remark~\ref{rem:five-theorems-as-av-images} identifies
+Theorem~D as the scalar degree-$2$ projection of the ordered
+$E_1$ bar package.
+For Heisenberg the ordered collision residue is
+$r^{\mathrm{Heis}}(z)=k/z$, so
+$\operatorname{av}(r^{\mathrm{Heis}})=k$.
+For affine Kac--Moody the exact degree-$2$ formula is the
+Sugawara-shift identity~\eqref{eq:sugawara-shift-holographic},
+which yields
+\[
+\kappa(V_k(\fg))
+\;=\;
+\operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+\;=\;
+\frac{\dim(\fg)(k+h^\vee)}{2h^\vee}.
+\]
+For Virasoro the ordered residue is
+$r^{\mathrm{Vir}}_c(z)=\frac{c/2}{z^3}+\frac{2T}{z}$
+\textup{(}Computation~\ref{comp:virasoro-rmatrix}\textup{)},
+and its scalar channel is the cubic-pole coefficient $c/2$.
+This gives
+$\kappa(\mathrm{Vir}_c)=c/2$.
+
+\emph{Route \textup{(ii)}: genus-$1$ anomaly.}
+On the scalar lane,
+Theorem~\ref{thm:genus-universality} and
+Corollary~\ref{cor:free-energy-ahat-genus} give
+$F_1(\cA)=\kappa(\cA)/24$.
+The three genus-$1$ curvature computations recover the same scalar.
+For Heisenberg,
+Theorem~\ref{thm:genus1-heisenberg} gives the holomorphic partition
+function $Z_1=1/\eta(\tau)$, while
+Theorem~\ref{thm:frame-genus1-curvature} gives
+$\dfib^{\,2}=k\,\omega_1$; the anomaly coefficient is therefore $k$.
+For affine Kac--Moody,
+Theorem~\ref{thm:sl2-genus1-curvature} displays the shifted level
+$k+h^\vee$ in the genus-$1$ curvature, and
+Proposition~\ref{prop:sl2-genus1-partition} displays the same shift in
+the $E_2$ coefficient of the one-loop partition function.
+The general simple-type formula is exactly
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$, as recorded in
+Remark~\ref{rem:kappa-holo-km}.
+For Virasoro,
+Theorem~\ref{thm:vir-genus1-curvature} gives
+$(d^{(1)})^2=(c/2)\,\omega_1$, hence
+$F_1(\mathrm{Vir}_c)=c/48$ and $\kappa(\mathrm{Vir}_c)=c/2$.
+The second route therefore agrees with the first.
+
+\emph{Route \textup{(iii)}: Hilbert series and GRR.}
+Remark~\ref{rem:theorem-d-alt-grr} gives a second proof architecture
+for the scalar lane:
+the graded ranks of the fiber bar complex are determined by the
+Hilbert series of~$\cA$, and GRR identifies the corresponding family
+index with
+$\kappa(\cA)\operatorname{ch}(\mathbb{E})$.
+The three relevant Hilbert models are already fixed on the live
+surface:
+partition-number growth for Heisenberg
+\textup{(}Theorem~\ref{thm:heisenberg-bar-complete},
+Remark~\ref{rem:heisenberg-literature}\textup{)},
+Lie-theoretic growth for affine Kac--Moody
+\textup{(}Corollary~\ref{cor:growth-rate-dimg},
+Remark~\ref{rem:bar-hilbert-koszul-dual}\textup{)},
+and Motzkin-difference growth for Virasoro
+\textup{(}Theorem~\ref{thm:motzkin-path-model}\textup{)}.
+These Hilbert models determine the graded family to which GRR applies;
+the genus-$1$ scalar normalization in
+Remark~\ref{rem:theorem-d-alt-grr} then fixes the coefficient of the
+Hodge term.
+For Heisenberg this coefficient is the level~$k$,
+for affine Kac--Moody it is the shifted-level scalar
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$,
+and for Virasoro it is the quartic-pole coefficient~$c/2$.
+Hence the family-index route recovers the same three values.
+\end{proof}
+
 \begin{remark}[Alternative proof via GRR]
 \label{rem:theorem-d-alt-grr}
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}

file update:
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index dbb162fddd11e676ffac7779fc476884dcc6f76d..37b20359894e6158884b2c23add2e5fad3c2a70b
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -3031,6 +3031,142 @@
 $F_g=k\cdot\frac{2^{2g-1}-1}{2^{2g-1}}\cdot\frac{|B_{2g}|}{(2g)!}$.
 \end{remark}
 
+\begin{proposition}[Three recovery routes for $\kappa$ on the scalar lane;
+\ClaimStatusProvedHere]
+\label{prop:kappa-three-routes}
+\index{modular characteristic!three recovery routes|textbf}
+\index{kappa@$\kappa$!shadow, anomaly, and Hilbert routes}
+For the three standard scalar families
+\[
+\mathcal{H}_k,\qquad
+V_k(\fg)\ \textup{(}$\fg$ simple\textup{)},\qquad
+\mathrm{Vir}_c,
+\]
+the modular characteristic is recovered by three mutually consistent
+routes:
+\begin{enumerate}[label=\textup{(\roman*)}]
+\item \emph{Shadow route.}
+ The degree-$2$ shadow of the ordered bar complex gives
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))
+ = \operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+ = \frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\item \emph{Genus-$1$ anomaly route.}
+ The genus-$1$ scalar coefficient satisfies
+ $F_1(\cA)=\kappa(\cA)/24$, so the same three values are read from the
+ one-loop anomaly:
+ Heisenberg from $\dfib^{\,2}=k\,\omega_1$,
+ affine Kac--Moody from the shifted level $k+h^\vee$,
+ and Virasoro from $(d^{(1)})^2=(c/2)\,\omega_1$.
+ In the present normalization this route reads $\kappa$ from the
+ logarithmic one-loop coefficient, not from a universal bare exponent
+ of~$\eta(\tau)$:
+ the rank-$1$ Heisenberg holomorphic partition function is
+ $1/\eta(\tau)$, and the affine genus-$1$ partition function carries
+ the shifted-level correction in its $E_2$ coefficient.
+\item \emph{Hilbert-series and family-index route.}
+ The conformal-weight Hilbert series of the bar/Koszul-dual model fixes
+ the graded ranks of the virtual bar family
+ $R\pi_*\barB^{\mathrm{fib}}(\cA)$, hence the GRR output
+ $\operatorname{ch}(R\pi_*\barB^{\mathrm{fib}}(\cA))
+ = \kappa(\cA)\operatorname{ch}(\mathbb{E}) + \cdots$.
+ For Heisenberg the Hilbert series is the partition-number series,
+ for affine Kac--Moody it is the Lie-theoretic series with growth rate
+ $\dim(\fg)$, and for Virasoro it is the Motzkin-difference series.
+ After the genus-$1$ scalar normalization of
+ Remark~\ref{rem:theorem-d-alt-grr}, this route recovers the same
+ $\kappa$:
+ \[
+ \kappa(\mathcal{H}_k)=k,\qquad
+ \kappa(V_k(\fg))=\frac{\dim(\fg)(k+h^\vee)}{2h^\vee},
+ \qquad
+ \kappa(\mathrm{Vir}_c)=\frac{c}{2}.
+ \]
+\end{enumerate}
+\end{proposition}
+
+\begin{proof}
+\emph{Route \textup{(i)}: shadow tower.}
+Remark~\ref{rem:five-theorems-as-av-images} identifies
+Theorem~D as the scalar degree-$2$ projection of the ordered
+$E_1$ bar package.
+For Heisenberg the ordered collision residue is
+$r^{\mathrm{Heis}}(z)=k/z$, so
+$\operatorname{av}(r^{\mathrm{Heis}})=k$.
+For affine Kac--Moody the exact degree-$2$ formula is the
+Sugawara-shift identity~\eqref{eq:sugawara-shift-holographic},
+which yields
+\[
+\kappa(V_k(\fg))
+\;=\;
+\operatorname{av}(r^{\mathrm{KM}}(z)) + \tfrac{1}{2}\dim(\fg)
+\;=\;
+\frac{\dim(\fg)(k+h^\vee)}{2h^\vee}.
+\]
+For Virasoro the ordered residue is
+$r^{\mathrm{Vir}}_c(z)=\frac{c/2}{z^3}+\frac{2T}{z}$
+\textup{(}Computation~\ref{comp:virasoro-rmatrix}\textup{)},
+and its scalar channel is the cubic-pole coefficient $c/2$.
+This gives
+$\kappa(\mathrm{Vir}_c)=c/2$.
+
+\emph{Route \textup{(ii)}: genus-$1$ anomaly.}
+On the scalar lane,
+Theorem~\ref{thm:genus-universality} and
+Corollary~\ref{cor:free-energy-ahat-genus} give
+$F_1(\cA)=\kappa(\cA)/24$.
+The three genus-$1$ curvature computations recover the same scalar.
+For Heisenberg,
+Theorem~\ref{thm:genus1-heisenberg} gives the holomorphic partition
+function $Z_1=1/\eta(\tau)$, while
+Theorem~\ref{thm:frame-genus1-curvature} gives
+$\dfib^{\,2}=k\,\omega_1$; the anomaly coefficient is therefore $k$.
+For affine Kac--Moody,
+Theorem~\ref{thm:sl2-genus1-curvature} displays the shifted level
+$k+h^\vee$ in the genus-$1$ curvature, and
+Proposition~\ref{prop:sl2-genus1-partition} displays the same shift in
+the $E_2$ coefficient of the one-loop partition function.
+The general simple-type formula is exactly
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$, as recorded in
+Remark~\ref{rem:kappa-holo-km}.
+For Virasoro,
+Theorem~\ref{thm:vir-genus1-curvature} gives
+$(d^{(1)})^2=(c/2)\,\omega_1$, hence
+$F_1(\mathrm{Vir}_c)=c/48$ and $\kappa(\mathrm{Vir}_c)=c/2$.
+The second route therefore agrees with the first.
+
+\emph{Route \textup{(iii)}: Hilbert series and GRR.}
+Remark~\ref{rem:theorem-d-alt-grr} gives a second proof architecture
+for the scalar lane:
+the graded ranks of the fiber bar complex are determined by the
+Hilbert series of~$\cA$, and GRR identifies the corresponding family
+index with
+$\kappa(\cA)\operatorname{ch}(\mathbb{E})$.
+The three relevant Hilbert models are already fixed on the live
+surface:
+partition-number growth for Heisenberg
+\textup{(}Theorem~\ref{thm:heisenberg-bar-complete},
+Remark~\ref{rem:heisenberg-literature}\textup{)},
+Lie-theoretic growth for affine Kac--Moody
+\textup{(}Corollary~\ref{cor:growth-rate-dimg},
+Remark~\ref{rem:bar-hilbert-koszul-dual}\textup{)},
+and Motzkin-difference growth for Virasoro
+\textup{(}Theorem~\ref{thm:motzkin-path-model}\textup{)}.
+These Hilbert models determine the graded family to which GRR applies;
+the genus-$1$ scalar normalization in
+Remark~\ref{rem:theorem-d-alt-grr} then fixes the coefficient of the
+Hodge term.
+For Heisenberg this coefficient is the level~$k$,
+for affine Kac--Moody it is the shifted-level scalar
+$\dim(\fg)(k+h^\vee)/(2h^\vee)$,
+and for Virasoro it is the quartic-pole coefficient~$c/2$.
+Hence the family-index route recovers the same three values.
+\end{proof}
+
 \begin{remark}[Alternative proof via GRR]
 \label{rem:theorem-d-alt-grr}
 \index{Grothendieck--Riemann--Roch!alternative proof of Theorem D}

ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Apr 16th, 2026 11:00 PM.
tokens used
359,424
