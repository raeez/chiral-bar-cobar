# R21_standalone_e1_primacy (402s)

Patched [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:464) so the degree-2 averaging theorem no longer states the false universal identity for affine KM. The theorem now says:
Heisenberg/abelian: `\av(r(z)) = \kappa`;
non-abelian affine KM: `\av(r(z)) = \kappa_{\mathrm{dp}} = k\dim(\mathfrak g)/(2h^\vee)`, with full `\kappa = \kappa_{\mathrm{dp}} + \dim(\mathfrak g)/2`.
I also synchronized the local restatements in the abstract, introduction, Theorem `D^{E_1}`, the explanatory remark, the tier-(b) summary, and the conclusion at [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:94), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:160), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:672), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:699), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:779), and [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:959).

Verification: re-read the modified sections, `git diff --check` passed, and fixed-string greps confirmed the stale universal phrasings are gone. A standalone LaTeX build did not complete because of a pre-existing unrelated fatal `\BarchFG` undefined control sequence at [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:346), before the edited theorem is reached.

## Rectification Summary
- [FIXED] [CRITICAL F14] The theorem “Degree-2 averaging” now distinguishes the abelian Heisenberg case from non-abelian affine KM, introducing `\kappa_{\mathrm{dp}}` and stating the full affine KM characteristic as `\kappa=\kappa_{\mathrm{dp}}+\dim(\mathfrak g)/2`.
- [FIXED] Downstream prose in the same file that repeated the old false universal formula was synchronized to the corrected affine KM/Sugawara-shift statement.
- [BLOCKED] Full standalone compile verification could not be completed because the file already fails earlier on an unrelated pre-existing macro error `\BarchFG` at line 346.


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
session id: 019d83b7-6678-7551-8ffe-450856537807
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


TARGET: standalone/N3_e1_primacy.tex

FINDINGS TO FIX:

1. [CRITICAL F14] Line ~457: Theorem "Degree-2 averaging: av(r(z))=kappa" is false for
   affine KM. For non-abelian KM: av(r(z)) + dim(g)/2 = kappa (Sugawara shift, C13/FM11).
   FIX: Add the Sugawara shift qualification. State: av(r(z)) = kappa for abelian (Heisenberg).
   For non-abelian KM: av(r(z)) = kappa_dp = k*dim(g)/(2h^v), and full kappa includes
   Sugawara shift dim(g)/2.

Read the file, find the theorem, make the fix.
mcp startup: no servers

thinking
**Considering verification protocols**

I’m wondering if a verification loop is necessary, especially if there aren’t any new label changes. I might explore using grep, but I also need to respect the AGENTS: Pre-Edit Verification Protocol in sensitive areas. This fix impacts the kappa formula and the averaging theorem, so I’ll need to add commentary consistent with the relevant protocols, likely PE-2 and PE-8, since they involve shared formulas. However, I must focus on editing only the specific file for safety.
codex
Using `beilinson-rectify` for a local mathematical claim repair. I’ll read the required constitutional files plus the target surface, then patch the affine KM averaging theorem with the correct Sugawara-shift qualification.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 220

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

thinking
**Planning file review**

I'm thinking to start by reading the entire target file or at least the relevant sections. Since it might not be too large, I could focus on the theorem and the beginning, but the skill suggests reading the whole file. So, I'll go with that. I'll run `wc -l` to check the line count and consider using `sed` to manage chunks, possibly running them in parallel. Searching for the target theorem will be part of this process too!
codex
I’ve loaded the repo-wide constraints. Next I’m reading the full target file and locating the degree-2 averaging theorem so the fix lands on the exact claim surface, not just the flagged line.
Plan update
  → Read the full target file and isolate the flagged theorem plus its local dependencies
  • Patch the theorem text to distinguish Heisenberg averaging from affine KM with the Sugawara shift
  • Re-read the modified section and verify the finding is resolved without new status or reference drift
exec
/bin/zsh -lc 'wc -l standalone/N3_e1_primacy.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Degree-2 averaging|av\\(r\\(z\\)\\)|Sugawara|kappa_dp|FM11|C13|Heisenberg|affine KM\" standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     987 standalone/N3_e1_primacy.tex
 succeeded in 52ms:
360:\begin{example}[Heisenberg ordered bar]
362:Let $\cH_{k}$ be the Heisenberg chiral algebra at level $k$,
457:\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
476:\item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
673:$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
735:Heisenberg $\cH_{k}$ with $r(z) = k/z$, affine Kac--Moody
742:tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
920:Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.

thinking
**Evaluating file reading strategy**

I need to read the full file, but I might consider breaking it into chunks for easier handling. The instructions say to focus on the entire target file, which means I should likely read it in segments like 1-250, 251-500, 501-750, and 751-987. I’m also considering looking into any dependencies related to "landscape_census." This approach should help me accomplish the task more effectively!
exec
/bin/zsh -lc "sed -n '1,250p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '501,750p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '251,500p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '751,987p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{thm:av-degree-3}
Let $\Phi_{\mathrm{KZ}}(\cA) \in \End(V^{\otimes 3})$ be the
genus-$0$ degree-$3$ Maurer--Cartan component, which for affine
Kac--Moody $\widehat\fg_{k}$ is the Drinfeld--Kontsevich KZ
associator. Then
\begin{equation}
\label{eq:av-degree-3}
\av_{n=3}\bigl(\Phi_{\mathrm{KZ}}(\cA)\bigr)
\;=\;
\mathfrak{C}(\cA),
\end{equation}
where $\mathfrak{C}(\cA)$ is the cubic shadow of Volume I,
equivalently the $\Sigma_{3}$-coinvariant of the associator. The
antisymmetric component $[\Omega_{12},\Omega_{23}]$ lies entirely
in $\ker(\av)$: it is antisymmetric under the transposition
$(1 \leftrightarrow 3)$, so its $\Sigma_{3}$-average vanishes.
Only the symmetric products
$\Omega_{12}\Omega_{23} + \Omega_{23}\Omega_{12}$
contribute to $\mathfrak{C}(\cA)$.
\end{theorem}
 succeeded in 51ms:
\documentclass[11pt,reqno]{amsart}

% ================================================================
% Packages
% ================================================================
\usepackage{amsmath,amssymb,amsthm}
\usepackage{mathrsfs}
\usepackage{enumerate}
\usepackage[shortlabels]{enumitem}
\usepackage{booktabs}
\usepackage{array}
\usepackage{microtype}
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true,linkcolor=blue!60!black,citecolor=green!40!black,urlcolor=blue!60!black]{hyperref}

% ================================================================
% Theorem environments
% ================================================================
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
 succeeded in 52ms:
term counts are elementary.
\end{proof}

The three cooperads sit in a commutative square of natural
transformations whose top arrow is the symmetrization and whose
bottom arrow is the Harrison projection, but they are not
canonically isomorphic. Conflating coshuffle with deconcatenation
is a standard error in the chiral-algebra literature and produces
spurious identifications between factorization coproducts and
bar coproducts.

\begin{remark}[Where each structure appears]
\label{rem:where-three-appear}
The Harrison coLie cooperad $\Lie^{c}$ underlies the chiral Lie
bar complex used by Francis--Gaitsgory, where only the zeroth
product of the OPE is visible. The coshuffle cooperad $\Sym^{c}$
underlies the symmetric bar $\BarSig(\cA)$ on the Ran space,
where factorization is implemented by the topological
coproduct on unordered configuration space. The deconcatenation
cooperad $T^{c}$ underlies the ordered bar $\Barord(\cA)$, where
 succeeded in 52ms:
Etingof--Kazhdan quantum vertex algebras~\cite{EtingofKazhdan00}
obtained from quasi-triangular Lie bialgebras. In this tier the
degree-$2$ Maurer--Cartan element is the rational Yang--Baxter
$r$-matrix $r_{\mathrm{YB}}(z)$, and the associator is a full
Drinfeld associator. Existing vertex-algebra theory cannot
recognise these algebras, and the ordered bar complex is the
minimal framework that makes them visible.

\begin{remark}[$E_{1}$ is the atom of the nonlocal regime]
\label{rem:e1-atom-nonlocal}
The three tiers form a strict hierarchy. Every standard chiral
algebra is $E_{\infty}$ in the sense that its OPE is symmetric in
the operator ordering up to the signs from the Arnold form; it is
the interpretation as an $E_{1}$ algebra that is the refinement.
Tier (c) consists of genuinely nonlocal objects, in the precise
sense that the Maurer--Cartan element lies outside the image of
any $E_{\infty}$-to-$E_{1}$ promotion functor. The error of
calling $E_{\infty}$-chiral algebras ``local'' and $E_{1}$-chiral
algebras ``non-abelian'' is a recurring pitfall; the right
distinction is symmetric versus ordered, or closed versus open.



thinking
**Fixing theorem references**

I need to find the target theorem and its dependencies. I could search landscape_census or another file for the C13 formula. It might help to look for line references in the comments too. The text of the theorem needs fixing since it seems to be incorrect. I should ensure that any mentions of the theorem throughout the file are consistent. Updating the title could be necessary, possibly something like "Degree-2 averaging: Heisenberg exact, affine KM with Sugawara shift."
thinking
**Adjusting theorem statement**

I need to refine the theorem statement and related references, focusing on theorem D for the cleanest option, which is tier (b). I want to make the strongest technical choice, possibly by strengthening the proof or adding a lemma while narrowing the claim. The current theorem seems incorrect for affine KM, so I should clarify the cases. It looks like for Heisenberg, we can say av(r(z)) = kappa, while for affine KM, it might be av(r(z)) = kappa_dp = k dim(g)/(2h^v).
thinking
**Clarifying the theorem for Virasoro**

I think the theorem needs some adjustments related to the Virasoro case. The title and equation should definitely be qualified. The user requested a fix, suggesting I include the Sugawara shift qualification. I can state that av(r(z)) = kappa for abelian (Heisenberg) cases. For non-abelian KM, I should clarify that av(r(z)) = kappa_dp = k * dim(g)/(2h^v), and the full kappa also includes the Sugawara shift of dim(g)/2. It might be worthwhile to mention other unaffected families or provide context.
codex
The false equation is not isolated to the theorem header. I’m sweeping the nearby downstream prose in the same file so the theorem, remarks, and conclusion all use the same affine KM qualification instead of reintroducing the bad statement one page later.
exec
/bin/zsh -lc "rg -n \"av\\(r\\(z\\)\\) = \\\\kappa|coinvariant of the spectral \\\\"'$r'"\\\\"'$-matrix|scalar modular characteristic '"\\\\kappa is the degree-\\\\"'$2'"\\\\"'$|strict projection|kappa'"\\(\\\\cA\\)\\)\" standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"av\\(r\\(z\\)\\)|kappa_dp|Sugawara|dim\\(\\\\fg\\)/2|landscape_census|C13|FM11\" -S ." in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:av\(r\(z\)\) = \kappa|coinvariant of the spectral \\569Xmatrix|scalar modular characteristic \kappa is the degree-\\$|strict projection|kappa\(\cA\)\))
                      ^^
error: unrecognized escape sequence
 succeeded in 52ms:
Total output lines: 3795

./CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
./CLAUDE.md:39:source:               landscape_census.tex line [N] OR compute engine
./CLAUDE.md:84:Step 2: Open landscape_census.tex, copy the formula WITH citation comment
./CLAUDE.md:85:Step 3: Paste with comment: % AP1: formula from landscape_census.tex:LINE; k=0 -> VALUE verified
./CLAUDE.md:202:4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower).
./CLAUDE.md:219:Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).
./CLAUDE.md:225:**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).
./CLAUDE.md:237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
./CLAUDE.md:245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
./CLAUDE.md:289:- B1. `r(z) = \Omega/z` (bare, no level). CORRECT: trace-form `r(z) = k\Omega/z` or KZ `r(z) = \Omega/((k+h^\vee)z)`. AP126. Regex: `r\(z\)\s*=\s*\\Omega\s*/\s*z` (catches bare form without any level prefix or Sugawara denominator).
./CLAUDE.md:302:- B11. `av(r(z)) = \kappa` for non-abelian KM. CORRECT: `av(r(z)) + dim(g)/2 = kappa(V_k(g))`. FM11.
./CLAUDE.md:420:**FM11. Sugawara shift missing in av(r(z)) = kappa.** For abelian Heisenberg, `av(r) = kappa` holds cleanly. For non-abelian KM, `av(r) + dim(g)/2 = kappa(V_k(g))`. Opus writes the abelian form universally. Counter: before writing av(r)=kappa, state the family (abelian vs non-abelian).
./CLAUDE.md:480:**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."
./CLAUDE.md:499:| Topologization | PROVED (affine KM); CONJECTURAL (general) | SC^{ch,top} + Sugawara = E_3 for V_k(g) at k != -h^v (thm:topologization). General chiral algebras with conformal vector: conj:topologization-general. Proof cohomological; class M chain-level open. |
./CLAUDE.md:505:**kappa** (AP1, AP9, AP20, AP24, AP48, AP136): DISTINCT per family, NEVER copy. KM=dim(g)(k+h^v)/(2h^v), Vir=c/2, W_N=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j (AP136: NOT c*H_{N-1}), Heis=k. Always qualify: kappa^{KM}, kappa^{Vir}. Complementarity: kappa+kappa'=0 (KM/free), 13 (Vir), NOT universal. State WHICH algebra: intrinsic vs kappa_eff=kappa(matter)+kappa(ghost) vs kappa(B) where B=A^!. **AP1 operational mandate**: before writing ANY kappa formula, (a) read landscape_census.tex for that family, (b) evaluate at k=0 and k=-h^v, (c) cross-check compute/. Writing kappa from memory is FORBIDDEN.
./CLAUDE.md:521:**computation discipline** (AP3, AP10, AP61): Compute independently. NEVER pattern-match across occurrences. Cross-family consistency checks are real verification; single-family hardcoded tests insufficient. Verify against OPE table, landscape_census.tex, cross-engine comparison. **AP10 strengthened**: every hardcoded expected value MUST have a comment citing 2+ independent derivation paths. For combinatorial counts, cite generating function or recursion. Bare numbers with no derivation trail are future AP10 violations.
./CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
./CLAUDE.md:599:source:                    [landscape_census.tex:LINE / compute/module.py]

thinking
**Searching for formula details**

I encountered a problem with my search command due to a regex issue, so I think I might need to simplify my search approach. I also want to find the exact lines in the landscape census formula that relate to kappa and averaging, which might be helpful. I'll look into the chapters or examples in the landscape_census.tex file to locate those specific lines.
codex
I’ve confirmed the repo-wide canonical rule in `CLAUDE.md`: for non-abelian affine KM, `av(r(z))` is only the double-pole piece `\kappa_{\mathrm{dp}}`, and the full `\kappa` adds `\dim(\mathfrak g)/2`. I’m now anchoring the edit to the local census language so the theorem statement and proof match the manuscript’s own convention surface.
exec
/bin/zsh -lc "rg -n \"kappa\\(V_k\\(g\\)\\)|av\\(r\\(z\\)\\)|kappa_dp|Sugawara shift|double-pole channel\" chapters/examples/landscape_census.tex chapters/examples/kac_moody.tex chapters/frame/introduction.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\av\\(r\\(z\\)\\) = \\\\kappa|Theorem D displays|degree-\\"'$2'"\\"'$ coinvariant|scalar modular characteristic '"\\\\kappa is the degree-\\"'$2'"\\"'$|tier '"\\(b\\).*av\\(r\\(z\\)\\)\" standalone/N3_e1_primacy.tex -F" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: chapters/frame/introduction.tex: No such file or directory (os error 2)
chapters/examples/kac_moody.tex:755:denominator $k + h^\vee$ is the Sugawara shift. This is the
chapters/examples/kac_moody.tex:1510:Equivalently: the double-pole channel contributes
chapters/examples/kac_moody.tex:1547:level~$k$, only the double-pole channel contributes:
chapters/examples/kac_moody.tex:1604:For the double-pole channel:
chapters/theory/higher_genus_modular_koszul.tex:3005:central charge is not zero: the residual Sugawara shift of
chapters/theory/higher_genus_modular_koszul.tex:3110:\begin{remark}[Sugawara shift as holographic anomaly]
chapters/theory/higher_genus_modular_koszul.tex:3113:\index{holographic anomaly!Sugawara shift}%
chapters/theory/higher_genus_modular_koszul.tex:4685: gives $\kappa = 3k/4$ (double-pole channel) $+ 3/2$
 exited 1 in 50ms:


thinking
**Searching for a target file**

I need to perform a proper search for the target file using regex or maybe a straightforward string. I want to get specific line references from the file around where those occurrences happen. So, I'm thinking of using the `rg -n` command with a simple string for an exact match. This should help me pinpoint exactly what I need. Let's see how that works out!
codex
Before editing, I’m running the required hot-zone checks on the exact formula surface I’m about to touch. This theorem hits both the `\kappa`-formula and cross-convention zones, so the edit needs a family-qualified statement, not a cosmetic caveat.
exec
/bin/zsh -lc "sed -n '1498,1615p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
of~$m_0$:
\begin{align}
\kappa
&= \operatorname{tr}(m_0)
= \frac{k + h^\vee}{2h^\vee}
 \cdot \operatorname{tr}(\mathsf{C})
= \frac{k + h^\vee}{2h^\vee}
 \cdot \sum_a (J^a, J_a)
\notag \\
&= \frac{k + h^\vee}{2h^\vee}\cdot\dim(\fg).
\label{eq:km-dfib-squared-trace}
\end{align}
Equivalently: the double-pole channel contributes
$\kappa_{\mathrm{dp}} = k\cdot\dim(\fg)/(2h^\vee)$
and the simple-pole channel contributes
$\kappa_{\mathrm{sp}} = \dim(\fg)/2$
(the self-contraction trace
$h^\vee\cdot\dim(\fg)/(2h^\vee) = \dim(\fg)/2$),
recovering~\eqref{eq:kappa-dp-sp}. Therefore:
\begin{equation}\label{eq:km-kappa-derivation}
codex
```text
family: affine KM / Heisenberg  kappa written: Heisenberg av(r)=kappa; affine KM av(r)=kappa_dp, kappa=kappa_dp+dim(g)/2
census: CLAUDE.md C13 / chapters/examples/kac_moody.tex:1510-1517 = av(r)=k*dim(g)/(2h^v), kappa=(k+h^v)dim(g)/(2h^v)  match? Y
at k=0: affine av(r)=0 expected 0; affine kappa=dim(g)/2 expected dim(g)/2
at k=-h^v (KM): affine av(r)=-dim(g)/2 expected -dim(g)/2; affine kappa=0 expected 0
at c=13 (Vir): unchanged, kappa=13/2 expected 13/2
AP136 (W_N N=2): not touched
wrong variants avoided: NOT av(r)=kappa for non-abelian KM, NOT kappa=k*dim(g)/(2h^v), NOT k/2, NOT c/(2h^v)
verdict: ACCEPT
```

```text
formula: degree-2 averaging in standalone/N3_e1_primacy.tex
Vol I: canonical rule present in CLAUDE.md C13 and chapters/examples/kac_moody.tex:1510-1517
Vol II: not edited per file-scope restriction; no propagation in this session
Vol III: not edited per file-scope restriction; no propagation in this session
consistent target for this edit? Y
convention conversion: trace-form convention r(z)=k*Omega/z, Sugawara shift applied? Y
verdict: ACCEPT
```

thinking
**Determining minimal edits**

I need to edit the file and pinpoint the exact minimal changes. I should search for occurrences related to the theorem and related phrases. Using a command like `rg` with exact strings could help here. I want to identify the lines that mention everything relevant. Maybe I should use a simpler approach like `rg -n "av\\(r\\(z\\)\\)|degree-\$2\$ coinvariant|strict projection" standalone/N3_e1_primacy.tex` to simplify the searching process. Let's get started!
exec
/bin/zsh -lc "rg -n 'av\\(r\\(z\\)\\)|degree-\\"'$2'"\\"'$ coinvariant|strict projection|scalar modular characteristic '"\\\\kappa|Theorem D displays this most visibly|tier \\(b\\)' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
95:is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
457:\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
673:$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
674:of a function. This is a strict projection; the full function
742:tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
849:the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
850:the passage from $r(z)$ to $\kappa$ is a strict projection with
920:Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
exec
/bin/zsh -lc "rg -n 'Sigma_\\{2\\}|\\"'$'"\\\\Sigma_\\{2\\}\\"'$-average|average of'"' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
161:$\Sigma_{2}$-average. The third is physical: the line-operator
490:in the pre-dualisation convention. Averaging over $\Sigma_{2}$
673:$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
exec
/bin/zsh -lc "sed -n '148,166p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
physical: the spectral $r$-matrix, the KZ connection, the
Drinfeld associator, and the full braiding of tensor categories
of modules all live on the ordered side.

Three principles motivate the inversion. The first is operadic:
Stasheff's associahedra $K_{n}$ (cf.~\cite{Stasheff63}) carry
more information than the symmetric groups $\Sigma_{n}$, and the
Getzler--Jones~\cite{GetzlerJones94} theory of $E_{n}$-operads
makes $E_{1}$ the lowest rung of a ladder whose every step is
non-commutative. The second is representation-theoretic: the
classical $r$-matrix of an affine Kac--Moody algebra at level $k$
is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
on the ordered side, and the scalar curvature $\kappa$ is its
$\Sigma_{2}$-average. The third is physical: the line-operator
sector of a chiral conformal theory is naturally open and
ordered, while the closed (bulk) sector is symmetric; the
averaging map is the operadic image of the open-to-closed
functor.


thinking
**Updating mathematical notes**

I need to update the notes about the Heisenberg exact, specifically detailing that the affine KM average has a double-pole contribution. Since the user is focusing on a specific theorem line, I should ensure consistency by modifying the introduction and other remarks as well. There might be around 6-7 edits needed across the theorem, proof, remarks, and conclusion sections to patch any repeated false universal statements. I'll examine the contexts around lines 830-853 and 915 for precise adjustments.
exec
/bin/zsh -lc "sed -n '734,752p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '664,688p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '842,853p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '914,924p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
All standard families of conformal field theory live here:
Heisenberg $\cH_{k}$ with $r(z) = k/z$, affine Kac--Moody
$\widehat\fg_{k}$ with $r(z) = k\Omega_{\fg}/z$, Virasoro $\Vir_{c}$ with $r(z) = (c/2)/z^{3}
+ 2T/z$ (cubic and simple poles, no quartic), $\beta\gamma$,
$bc$, $W$-algebras, Bershadsky--Polyakov. In each case $r(z)$ is
fully determined by the underlying $E_{\infty}$ vertex algebra
structure; the $E_{1}$ refinement adds no new data at degree $2$
beyond what is already visible in the OPE. The averaging map on
tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
nontrivial but reconstructible from $\cA$.

\subsection*{Tier (c): genuinely $E_{1}$}

The third tier is populated by algebras in which $r(z)$ is
independent input: the Maurer--Cartan element cannot be recovered
from any underlying $E_{\infty}$ structure. The paradigmatic
examples are the Yangians $Y_{\hbar}(\fg)$ and the
Etingof--Kazhdan quantum vertex algebras~\cite{EtingofKazhdan00}
obtained from quasi-triangular Lie bialgebras. In this tier the
 succeeded in 52ms:
coproduct, is the natural primitive object of modular Koszul
duality, and that the symmetric bar $\BarSig(\cA)$ is its
$\Sigma_{n}$-coinvariant shadow under an averaging map $\av$ of
dg Lie algebras. The five foundational theorems A, B, C, D, H of
modular Koszul duality admit ordered $E_{1}$ counterparts whose
symmetric images are the classical theorems. Theorem D is the
cleanest example: the scalar modular characteristic $\kappa$ is
the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
the passage from $r(z)$ to $\kappa$ is a strict projection with
nontrivial kernel.

Several problems remain open.
 succeeded in 52ms:
\end{theorem}

\begin{remark}[Theorem D is the cleanest example]
\label{rem:theorem-d-cleanest}
Among the five, Theorem D makes the $E_{1}$ primacy thesis most
concrete. The scalar modular characteristic $\kappa$ is a single
number per family$ are distinct per family, never to be
copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
variable, the collision coordinate $z$. The statement
$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
of a function. This is a strict projection; the full function
$r(z)$ carries information about the braiding, the quantum group,
and the line-operator algebra that no scalar invariant can see.
The universality property of $\kappa$ in Volume I Theorem D
lifts (with the same proof, interpreted one level higher) to a
universality property of $r(z)$ on the ordered side.
\end{remark}

\begin{remark}[What averaging forgets]
\label{rem:what-av-forgets}
 succeeded in 51ms:

We close by reiterating the thesis in one sentence: in modular
Koszul duality, the ordered bar complex $\Barord(\cA) =
T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
A, B, C, D, H are the invariants that survive the averaging, and
Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.

% ================================================================
\begin{thebibliography}{99}

exec
/bin/zsh -lc "sed -n '88,98p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
For a cyclic chiral algebra $\cA$, the ordered bar complex
$\Barord(\cA) = T^{c}(s^{-1}\bar\cA)$ with deconcatenation coproduct
is the natural primitive object of the theory. The symmetric bar
$\BarSig(\cA)$, which underlies the classical Francis--Gaitsgory
factorization picture, is its $\Sigma_{n}$-coinvariant image under
an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
lives natively on the ordered side. The Drinfeld associator is the
degree-$3$ coinvariant of the KZ connection. The five foundational
theorems A--D and H of modular Koszul duality admit ordered

thinking
**Considering theorem adjustments**

The user is asking for a specific fix in their findings. I realize I need to change the exact theorem and also address the downstream restatements. Since both the theorem D package and the introduction repeat the same incorrect statement, leaving them as is will make the theorem fix inconsistent. I don't think I need new labels or references; I should just use apply_patch for the edits without changing the labels.
codex
I’m patching the theorem together with the local restatements that depended on it: abstract, introduction, the theorem/proof pair, the theorem-D packaging line, the tier-(b) summary, and the closing summary sentence. The goal is one coherent convention surface inside `standalone/N3_e1_primacy.tex`, not a corrected theorem surrounded by stale false prose.

thinking
**Inspecting theorem D**

I need to construct the patch really carefully. It’s important to take a good look at theorem D, especially around the 610 area. I want to make sure I'm thorough in my inspection, considering all the underlying details and implications. Being methodical will help me catch any potential flaws before finalizing everything. Let's focus on getting this right!
exec
/bin/zsh -lc "sed -n '612,645p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Theorem~$\mathrm{C}^{E_{1}}$: ordered complementarity]
\label{thm:e1-theorem-c}
At each genus $g$ and degree $n$ with $2g-2+n > 0$, the ordered
complementarity takes the form
\begin{equation}
\label{eq:e1-complementarity}
Q_{g,n}^{E_{1}}(\cA) + Q_{g,n}^{E_{1}}(\cA^{!,E_{1}})
\;=\;
H^{*}\!\bigl(\overline{\cM}_{g,n}^{\,\mathrm{rib}},
Z^{E_{1}}(\cA)\bigr),
\end{equation}
where $Z^{E_{1}}(\cA)$ is the $E_{1}$ centre, the space of
$R$-matrix-equivariant elements. The scalar identity
$\kappa + \kappa^{!} = 0$ for Kac--Moody and free-field families
(and $\kappa + \kappa^{!} = 13$ for Virasoro) is the
$\Sigma_{n}$-coinvariant image.
\end{theorem}

\begin{theorem}[Theorem~$\mathrm{D}^{E_{1}}$: degree-$2$ package]
\label{thm:e1-theorem-d}
exec
/bin/zsh -lc "sed -n '645,660p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
line-side modular $R$-matrix interpretation requires additional
Yangian input and is not proved in this paper.
\end{theorem}

\begin{theorem}[Theorem~$\mathrm{H}^{E_{1}}$: ordered Hochschild]
\label{thm:e1-theorem-h}
For every genus $g$ and complete $\cA$-bimodule $M$, the
genus-$g$ ordered chiral Hochschild homology is computed
coalgebraically by the genus-$g$ ordered coHochschild complex of
the ordered bar coalgebra $C = \Barord(\cA)$, with twisted
differential involving the curvature term $\kappa(\cA)\cdot
\lambda_{g}$ in the uniform-weight case. At genus $g\geq 2$ with
multi-weight field content the scalar formula receives a
cross-channel correction $\delta F_{g}^{\mathrm{cross}}$, so the
statement above is strict only in the uniform-weight regime; the




thinking
**Reviewing mathematical notation**

I need to work on a patch for Theorem D. It’s important to keep things simple in the abstract and introduction. Maybe I should avoid introducing new notation like `\kappa_{\mathrm{dp}}` unless it’s defined somewhere else in the document. Using inline notation in the theorem and in remarks could be better. I'm also thinking about changing the theorem title to clarify the formula. The equation could define cases for different types of algebras, addressing potential confusion regarding the Vir example within the theorem statement.
thinking
**Clarifying scalar equations**

I’m thinking about adding explanations after the equation. For Virasoro and the scalar families mentioned, the scalar already equals `\kappa(\cA)`, but caution is necessary with canonical formulas. Keeping it simple might help: I could state, “At degree 2, averaging projects to the scalar channel.” For Heisenberg, this scalar is `\kappa`, while for non-abelian affine KM, it's the double-pole contribution `\kappa_dp`. I need to decide on the equation’s universality and whether to keep the label for clarity.
thinking
**Searching for occurrences**

I need to search for exact occurrences after applying the patch. I'm considering how to approach this effectively. Should I use specific keywords or the context surrounding the patch? I'm also wondering if there are any patterns or trends I should look for in these occurrences. It's a bit overwhelming to think about, but I want to ensure I'm thorough. Alright, let's dive in and see what I can find!
thinking
**Crafting a patch carefully**

I'm thinking about how to approach crafting a patch while considering the Heisenberg case, though I'm not entirely sure what the connection might be. I want to be careful and make sure I preserve the line widths. It seems important to patch sections thoughtfully so everything works well together. I should also look into searching after applying the patch to confirm everything is functioning as it should. Let's make sure to get this right!
exec
/bin/zsh -lc "sed -n '452,520p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Feynman transforms~\cite{GetzlerKapranov98}. Compatibility with
the Lie bracket follows because symmetrisation commutes with
the convolution bracket on cooperadic Homs.
\end{proof}

\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
\label{thm:av-degree-2}
Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
component of the $E_{1}$ Maurer--Cartan element, in the
pre-dualisation convention of
Volume~I (the shadow-archetype column of
\cite[Example]{Lorgat26I}, equivalently the collision residue
computed in $\cA\otimes\cA$ before applying the Koszul pairing).
Then
\begin{equation}
\label{eq:av-degree-2}
\av_{n=2}\bigl(r(z)\bigr)
\;=\;
\kappa(\cA),

thinking
**Considering patching approach**

I’m thinking I need to focus on smaller patches. It seems more manageable to tackle things chunk by chunk rather than taking on a massive project all at once. This way, I can maintain better control and efficiency. I wonder if breaking it down will lead to cleaner outcomes. Let's see how this goes as I start patching, keeping an eye on each piece I work on!
file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -94,4 +94,7 @@
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
apply_patch(auto_approved=true) exited 0 in 46ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..f3f14fc52e1026c21a59b6bccde4971e44f8a7cb
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..f3f14fc52e1026c21a59b6bccde4971e44f8a7cb
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the

file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -162,4 +162,8 @@
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
apply_patch(auto_approved=true) exited 0 in 57ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..cb96737ba01199d7a28c43b46e404362d2a7ef92
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..cb96737ba01199d7a28c43b46e404362d2a7ef92
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed

file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -463,3 +463,3 @@
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
@@ -477,5 +477,19 @@
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
@@ -485,3 +499,5 @@
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
@@ -497,9 +513,16 @@
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
apply_patch(auto_approved=true) exited 0 in 40ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..4756b07a39f566e8a81bc2cedc640b50378c0d26
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..4756b07a39f566e8a81bc2cedc640b50378c0d26
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]

file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -672,3 +672,6 @@
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
apply_patch(auto_approved=true) exited 0 in 40ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..9c141fe163bab2e59103b8875bd34e5c93406844
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..9c141fe163bab2e59103b8875bd34e5c93406844
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional

file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -705,4 +705,8 @@
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
apply_patch(auto_approved=true) exited 0 in 32ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..e500ffdbad212db481c076393d7490e109087dbb
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -670,8 +703,12 @@
 number per family$ are distinct per family, never to be
 copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..e500ffdbad212db481c076393d7490e109087dbb
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -670,8 +703,12 @@
 number per family$ are distinct per family, never to be
 copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D


thinking
**Considering sentence clarity**

I’m noticing a strangely worded sentence: "number per family$ are distinct per family..." It seems a bit odd, and I’m thinking we might not need to fix it—maybe it’s best left alone since our patch didn't make it any worse. However, I wonder if a re-read could help clarify things, but then again, maybe it’s not worth the trouble. It might be safest to keep the edits minimal and move on.
file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -778,3 +778,6 @@
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
apply_patch(auto_approved=true) exited 0 in 61ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..3bca5f83393c332382312276494d6eeca40a91ec
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -670,8 +703,12 @@
 number per family$ are distinct per family, never to be
 copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +776,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..3bca5f83393c332382312276494d6eeca40a91ec
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -670,8 +703,12 @@
 number per family$ are distinct per family, never to be
 copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +776,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}

file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -887,5 +887,8 @@
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
@@ -959,3 +962,6 @@
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
apply_patch(auto_approved=true) exited 0 in 65ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..28099b1d1e3c955a8c3fa97d4258a5ba82bc64a8
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -670,8 +703,12 @@
 number per family$ are distinct per family, never to be
 copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +776,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +885,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +960,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..28099b1d1e3c955a8c3fa97d4258a5ba82bc64a8
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -670,8 +703,12 @@
 number per family$ are distinct per family, never to be
 copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +776,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +885,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +960,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}


thinking
**Searching bad phrases**

I need to search for the remaining problematic phrases, like `av(r(z)) = \kappa` and degree-2 coinvariant expressions. It might also be worthwhile to check the title line of the theorem. Overall, it seems necessary to dig deeper into these specific terms to ensure everything is accurate and clear. I want to make sure I have all the right information before proceeding! So, I'll get started on that search.
codex
The patch is in. I’m now re-reading the modified surface and grepping for stale copies of the old false formula inside the same file, especially the theorem-D restatements and closing summary.
exec
/bin/zsh -lc "sed -n '628,930p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '452,520p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '88,170p' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'av\\(r\\(z\\)\\) = \\\\kappa|degree-\\"'$2'"\\"'$ coinvariant|scalar degree-'"\\"'$2'"\\"'$ shadow|Sugawara shift|kappa_'"\\{\\\\mathrm\\{dp\\}\\}' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\Sigma_{n}$-invariant homomorphism from $\cM_{\Com}(g,n)$ lifts,
via any section of the ribbon-forgetting quotient, to a
homomorphism from $\cM_{\Ass}(g,n)$. Compatibility with the
differential follows because the ribbon edge-contraction
differential descends to the symmetric edge-contraction
differential under external $\Sigma_{n}$-coinvariants; this is
the Getzler--Kapranov comparison between ribbon and commutative
Feynman transforms~\cite{GetzlerKapranov98}. Compatibility with
the Lie bracket follows because symmetrisation commutes with
the convolution bracket on cooperadic Homs.
\end{proof}

\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
\label{thm:av-degree-2}
Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
component of the $E_{1}$ Maurer--Cartan element, in the
pre-dualisation convention of
Volume~I (the shadow-archetype column of
\cite[Example]{Lorgat26I}, equivalently the collision residue
 succeeded in 52ms:
\[
\Cobar^{(g)}\!\bigl(\Barord(\cA)(g,\bullet)\bigr)
\;\xrightarrow{\;\sim\;}\; \cA
\]
is a quasi-isomorphism (the inversion $\Cobar \circ \Barord
\simeq \id$ on the Koszul locus, not a Koszul-duality statement),
and the $E_{1}$ linear Koszul dual $\cA^{!,E_{1}}$ obtained by
linear duality on a finite-dimensional model of $\Barord(\cA)$ is
an $E_{1}$-chiral algebra at each such genus. The scope of ``all
genera'' here is contingent on the PBW-completeness hypothesis
being propagated genus by genus via the MC perturbation lemma of
\cite[Chapter~9]{Lorgat26I}.
\end{theorem}

\begin{theorem}[Theorem~$\mathrm{C}^{E_{1}}$: ordered complementarity]
\label{thm:e1-theorem-c}
At each genus $g$ and degree $n$ with $2g-2+n > 0$, the ordered
complementarity takes the form
\begin{equation}
\label{eq:e1-complementarity}
 succeeded in 52ms:
For a cyclic chiral algebra $\cA$, the ordered bar complex
$\Barord(\cA) = T^{c}(s^{-1}\bar\cA)$ with deconcatenation coproduct
is the natural primitive object of the theory. The symmetric bar
$\BarSig(\cA)$, which underlies the classical Francis--Gaitsgory
factorization picture, is its $\Sigma_{n}$-coinvariant image under
an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
lives natively on the ordered side: for abelian families the average
is $\kappa$, while for non-abelian affine Kac--Moody it is the
double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
degree-$3$ coinvariant of the KZ connection. The five foundational
theorems A--D and H of modular Koszul duality admit ordered
counterparts whose $\Sigma_{n}$-shadows are exactly the
commutative theorems; information lost under $\av$ includes the
full braiding, the Grothendieck--Teichm\"uller torsor of
splittings, and the cross-degree leakage that obstructs a dg Lie
section. Three distinct coalgebra structures feature and must not
be conflated: the Harrison coLie structure with $n!/n$ terms at
 succeeded in 51ms:
98:double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
99:adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
166:$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
167:$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
464:\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
480:\kappa_{\mathrm{dp}}(\widehat\fg_{k})
489:\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
501: $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
519:$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
522:$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
675:$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
676:$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
706:$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
708:$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
779:tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
780:$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
781:Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
782:$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
888:cleanest example: the scalar degree-$2$ shadow is recovered from
890:for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..28099b1d1e3c955a8c3fa97d4258a5ba82bc64a8
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -670,8 +703,12 @@
 number per family$ are distinct per family, never to be
 copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +776,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +885,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +960,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}


thinking
**Fixing broken text**

The broken text is now noticeable, and I think we can make some minimal fixes since a part of it was touched upon. I could rewrite the first sentence of the remark to create a more coherent version. Perhaps I can say something like: "Among the five, Theorem D makes the $E_{1}$ primacy thesis the most concrete." This should clarify the meaning and improve readability.
codex
The formula surface is now consistent. One local sentence in the same remark is still visibly corrupted text from earlier drafting, so I’m cleaning that line as part of the same touched chunk to keep the section readable and mathematically coherent.
file update
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
@@ -702,4 +702,5 @@
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
apply_patch(auto_approved=true) exited 0 in 53ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}



thinking
**Considering LaTeX compilation**

I need to check the file syntax and see if it's still functional. Running `latexmk -pdf -interaction=nonstopmode -halt-on-error standalone/N3_e1_primacy.tex` could be heavy, but it might provide the strongest local verification. The user didn't mention any specific skill, but it could be relevant here. Since local verification is critical after editing, I should likely compile the standalone file to ensure correctness, even if it’s not explicitly required for this task.
thinking
**Deciding on skill usage**

I see that the skill trigger applies only if the task matches its description, but the user didn't specifically ask for a build. Still, verifying changes in the standalone TeX file could benefit from using the build-surface skill. Just to be safe, I think I should apply the build-surface skill if I decide to compile. I just need to read enough to ensure everything works. Alright, let’s move forward with this approach.
codex
I have the textual fix done. For verification I’m using the strongest local check available on this surface: a standalone TeX build plus a final grep/re-read, so we know the theorem and its restatements are both coherent and syntactically valid.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error standalone/N3_e1_primacy.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 exited 12 in 941ms:
Rc files read:
  NONE
Latexmk: This is Latexmk, John Collins, 27 Dec. 2024. Version 4.86a.
No existing .aux file, so I'll make a simple one, and require run of *latex.
Latexmk: applying rule 'pdflatex'...
Rule 'pdflatex':  Reasons for rerun
Category 'other':
  Rerun of 'pdflatex' forced or previously required:
    Reason or flag: 'Initial setup'

------------
Run number 1 of rule 'pdflatex'
------------
------------
Running 'pdflatex  -interaction=nonstopmode -halt-on-error -recorder  "standalone/N3_e1_primacy.tex"'
------------
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./standalone/N3_e1_primacy.tex
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}


thinking
**Considering file checks**

I think I might need to use `git diff` specifically for the file `standalone/N3_e1_primacy.tex` to check for changes. This way, I can focus only on the necessary modifications. I should read the modified sections with line numbers, and perhaps confirm the absence of stale formula strings using `rg -n`. Also, checking whitespace issues with `git diff --check` might be useful. I wonder if I should involve `sed` for line numbers, but maybe `texfot` isn't necessary.
codex
The standalone build is blocked by a pre-existing fatal `\BarchFG` undefined-control-sequence earlier in the file, before the edited theorem is even parsed. I’m doing the remaining verification by diff/re-read on the touched region and checking that no stale universal `av(r)=\kappa` claim remains on the repaired surface.
exec
/bin/zsh -lc 'git diff --check -- standalone/N3_e1_primacy.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- standalone/N3_e1_primacy.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Degree-\\"'$2'"\\"'$ averaging: '"\\\\av\\(r\\(z\\)\\) = \\\\kappa|the scalar modular characteristic \\\\kappa is the degree-\\"'$2'"\\"'$ coinvariant|Theorem D displays this most visibly as '"\\\\av\\(r\\(z\\)\\) = \\\\kappa\\(\\\\cA\\\\)' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 51ms:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec..ca0e595 100644
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@ $\BarSig(\cA)$, which underlies the classical Francis--Gaitsgory
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@ makes $E_{1}$ the lowest rung of a ladder whose every step is
 non-commutative. The second is representation-theoretic: the
 exited 2 in 51ms:
rg: regex parse error:
    (?:Degree-\$2\$ averaging: \\av\(r\(z\)\) = \\kappa|the scalar modular characteristic \\kappa is the degree-\$2\$ coinvariant|Theorem D displays this most visibly as \\av\(r\(z\)\) = \\kappa\(\\cA\\))
                                                                                                                                                                                                           ^
error: unopened group
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}

codex
The diff is clean and `git diff --check` is clean. I’m running one last fixed-string sweep for the exact stale phrasings I replaced, since the earlier regex search was just a shell quoting miss.
exec
/bin/zsh -lc "rg -n -F 'Degree-"'$2$ averaging: $'"\\av(r(z)) = \\kappa"'$'"' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Theorem D displays this most visibly as "'$'"\\av(r(z)) = \\kappa(\\cA)"'$.'"' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'the scalar modular characteristic "'$'"\\kappa"'$ is the degree-$2$ coinvariant'"' standalone/N3_e1_primacy.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}

Plan update
The theorem and its downstream restatements in the target file now distinguish the Heisenberg case from non-abelian affine KM, with the Sugawara shift stated explicitly. Verification was completed by re-reading, diff/grep checks, and an attempted standalone build that failed earlier in the file on a pre-existing unrelated macro error.
  ✓ Read the full target file and isolate the flagged theorem plus its local dependencies
  ✓ Patch the theorem text to distinguish Heisenberg averaging from affine KM with the Sugawara shift
  ✓ Re-read the modified section and verify the finding is resolved without new status or reference drift
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}


thinking
**Fetching line numbers**

I think I need to get line numbers for the final references. It seems like using "nl -ba" around relevant sections could help me with that. I’ll fetch line numbers specifically for the theorem and its restatements. It should make everything clearer and more organized for whoever's looking at this. Let's make sure to keep everything precise and tidy while I'm at it!
exec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '92,170p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '668,785p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '460,525p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/N3_e1_primacy.tex | sed -n '886,968p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    92	factorization picture, is its $\Sigma_{n}$-coinvariant image under
    93	an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
    94	of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
    95	is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
    96	lives natively on the ordered side: for abelian families the average
    97	is $\kappa$, while for non-abelian affine Kac--Moody it is the
    98	double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
    99	adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
   100	degree-$3$ coinvariant of the KZ connection. The five foundational
   101	theorems A--D and H of modular Koszul duality admit ordered
   102	counterparts whose $\Sigma_{n}$-shadows are exactly the
   103	commutative theorems; information lost under $\av$ includes the
   104	full braiding, the Grothendieck--Teichm\"uller torsor of
   105	splittings, and the cross-degree leakage that obstructs a dg Lie
   106	section. Three distinct coalgebra structures feature and must not
   107	be conflated: the Harrison coLie structure with $n!/n$ terms at
   108	degree $n$, the coshuffle structure with $2^{n}$ terms, and the
   109	deconcatenation structure with $n+1$ terms. Only deconcatenation
   110	equips the ordered bar. We record three tiers of $r$-matrix
   111	input: the pole-free tier where $R = \tau$ is Koszul-signed,
 succeeded in 52ms:
   668	\end{equation}
   669	obtained from the genus-refined degree-$2$ projection of the
   670	$E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
   671	characteristic package of $\cA$. It is universal, additive,
   672	antisymmetric under opposite-duality, and satisfies
   673	$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
   674	non-abelian affine Kac--Moody one has
   675	$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
   676	$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
   677	The coinvariant recovery of the scalar curvature from $r(z)$ is
   678	the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
   679	line-side modular $R$-matrix interpretation requires additional
   680	Yangian input and is not proved in this paper.
   681	\end{theorem}
   682	
   683	\begin{theorem}[Theorem~$\mathrm{H}^{E_{1}}$: ordered Hochschild]
   684	\label{thm:e1-theorem-h}
   685	For every genus $g$ and complete $\cA$-bimodule $M$, the
   686	genus-$g$ ordered chiral Hochschild homology is computed
   687	coalgebraically by the genus-$g$ ordered coHochschild complex of
 succeeded in 52ms:
   460	the Lie bracket follows because symmetrisation commutes with
   461	the convolution bracket on cooperadic Homs.
   462	\end{proof}
   463	
   464	\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
   465	\label{thm:av-degree-2}
   466	Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
   467	genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
   468	component of the $E_{1}$ Maurer--Cartan element, in the
   469	pre-dualisation convention of
   470	Volume~I (the shadow-archetype column of
   471	\cite[Example]{Lorgat26I}, equivalently the collision residue
   472	computed in $\cA\otimes\cA$ before applying the Koszul pairing).
   473	Then
   474	\begin{equation}
   475	\label{eq:av-degree-2}
   476	\av_{n=2}\bigl(r(z)\bigr)
   477	\;=\;
   478	\begin{cases}
   479	\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
 succeeded in 53ms:
   886	dg Lie algebras. The five foundational theorems A, B, C, D, H of
   887	modular Koszul duality admit ordered $E_{1}$ counterparts whose
   888	symmetric images are the classical theorems. Theorem D is the
   889	cleanest example: the scalar degree-$2$ shadow is recovered from
   890	the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
   891	for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
   892	affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
   893	added; the passage from $r(z)$ to the scalar shadow is a strict
   894	projection with
   895	nontrivial kernel.
   896	
   897	Several problems remain open.
   898	
   899	\subsection*{The full $E_{1}$ Koszul duality theorem}
   900	
   901	An unconditional $E_{1}$ Koszul duality theorem, asserting that
   902	the bar and cobar functors exchange the categories of
   903	$E_{1}$-chiral algebras and cocomplete $F\Ass$-coalgebras on the
   904	Koszul locus, is not available in the present paper. What is
   905	proved (Theorems~\ref{thm:e1-theorem-a} and~\ref{thm:e1-theorem-b})
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}


thinking
**Considering summary format**

I need to include a summary with a bullet, something like "- [FIXED] [CRITICAL F14] ...". Maybe it makes sense to mention the build blocker separately since that could be important. However, the summary contract only specifies certain categories. So, I must be careful not to stray too far from what's required. It looks like I need to balance the need for clarity with the contract's requirements. I'll figure out how to best combine those elements.
codex
Patched [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:464) so the degree-2 averaging theorem no longer states the false universal identity for affine KM. The theorem now says:
Heisenberg/abelian: `\av(r(z)) = \kappa`;
non-abelian affine KM: `\av(r(z)) = \kappa_{\mathrm{dp}} = k\dim(\mathfrak g)/(2h^\vee)`, with full `\kappa = \kappa_{\mathrm{dp}} + \dim(\mathfrak g)/2`.
I also synchronized the local restatements in the abstract, introduction, Theorem `D^{E_1}`, the explanatory remark, the tier-(b) summary, and the conclusion at [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:94), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:160), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:672), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:699), [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:779), and [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:959).

Verification: re-read the modified sections, `git diff --check` passed, and fixed-string greps confirmed the stale universal phrasings are gone. A standalone LaTeX build did not complete because of a pre-existing unrelated fatal `\BarchFG` undefined control sequence at [standalone/N3_e1_primacy.tex](/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:346), before the edited theorem is reached.

## Rectification Summary
- [FIXED] [CRITICAL F14] The theorem “Degree-2 averaging” now distinguishes the abelian Heisenberg case from non-abelian affine KM, introducing `\kappa_{\mathrm{dp}}` and stating the full affine KM characteristic as `\kappa=\kappa_{\mathrm{dp}}+\dim(\mathfrak g)/2`.
- [FIXED] Downstream prose in the same file that repeated the old false universal formula was synchronized to the corrected affine KM/Sugawara-shift statement.
- [BLOCKED] Full standalone compile verification could not be completed because the file already fails earlier on an unrelated pre-existing macro error `\BarchFG` at line 346.
file update:
diff --git a/standalone/N3_e1_primacy.tex b/standalone/N3_e1_primacy.tex
index 858b4ec9765391aa0194bb9af2c51c57a07f835b..ca0e59533a58dfb87ec1108eec7e9984707a5e8e
--- a/standalone/N3_e1_primacy.tex
+++ b/standalone/N3_e1_primacy.tex
@@ -92,8 +92,11 @@
 factorization picture, is its $\Sigma_{n}$-coinvariant image under
 an averaging map $\av \colon \gEone \twoheadrightarrow \gmod$
 of dg Lie algebras. The scalar modular characteristic $\kappa(\cA)$
-is the degree-$2$ coinvariant of a meromorphic $r$-matrix $r(z)$ that
-lives natively on the ordered side. The Drinfeld associator is the
+is recovered at degree $2$ from a meromorphic $r$-matrix $r(z)$ that
+lives natively on the ordered side: for abelian families the average
+is $\kappa$, while for non-abelian affine Kac--Moody it is the
+double-pole term $\kappa_{\mathrm{dp}}$, and the full $\kappa$
+adds the Sugawara shift $\dim(\fg)/2$. The Drinfeld associator is the
 degree-$3$ coinvariant of the KZ connection. The five foundational
 theorems A--D and H of modular Koszul duality admit ordered
 counterparts whose $\Sigma_{n}$-shadows are exactly the
@@ -157,8 +160,12 @@
 non-commutative. The second is representation-theoretic: the
 classical $r$-matrix of an affine Kac--Moody algebra at level $k$
 is the content of the degree-$2$ genus-$0$ Maurer--Cartan element
-on the ordered side, and the scalar curvature $\kappa$ is its
-$\Sigma_{2}$-average. The third is physical: the line-operator
+on the ordered side, and its $\Sigma_{2}$-average recovers the
+degree-$2$ scalar shadow: for Heisenberg this is $\kappa$, while
+for non-abelian affine Kac--Moody it is
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$, with the full
+$\kappa$ obtained after adding the Sugawara shift $\dim(\fg)/2$.
+The third is physical: the line-operator
 sector of a chiral conformal theory is naturally open and
 ordered, while the closed (bulk) sector is symmetric; the
 averaging map is the operadic image of the open-to-closed
@@ -454,7 +461,7 @@
 the convolution bracket on cooperadic Homs.
 \end{proof}
 
-\begin{theorem}[Degree-$2$ averaging: $\av(r(z)) = \kappa$]
+\begin{theorem}[Degree-$2$ averaging: Heisenberg exact, affine KM with Sugawara shift]
 \label{thm:av-degree-2}
 Let $r(z) \in \End(V \otimes V) \otimes \cO(*\Delta)$ be the
 genus-$0$ degree-$2$ $E_{1}$ shadow of $\cA$: the degree-$2$
@@ -468,15 +475,31 @@
 \label{eq:av-degree-2}
 \av_{n=2}\bigl(r(z)\bigr)
 \;=\;
-\kappa(\cA),
+\begin{cases}
+\kappa(\cA), & \text{for abelian Heisenberg families},\\[4pt]
+\kappa_{\mathrm{dp}}(\widehat\fg_{k})
+:= \dfrac{k\,\dim(\fg)}{2h^{\vee}}, &
+\text{for non-abelian affine Kac--Moody in the trace-form convention.}
+\end{cases}
 \end{equation}
-the scalar modular characteristic of $\cA$. Concretely, for the
+In the affine Kac--Moody case the full modular characteristic is
+\[
+\kappa(\widehat\fg_{k})
+\;=\;
+\kappa_{\mathrm{dp}}(\widehat\fg_{k}) + \frac{\dim(\fg)}{2}
+\;=\;
+\frac{\dim(\fg)(k+h^{\vee})}{2h^{\vee}},
+\]
+so the extra $\dim(\fg)/2$ is the Sugawara simple-pole shift.
+Concretely, for the
 principal examples:
 \begin{itemize}
 \item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
 \item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
  (the level $k$ survives; at $k=0$ the $r$-matrix vanishes
- identically), and
+ identically),
+ $\av(r(z)) = \kappa_{\mathrm{dp}}(\widehat\fg_k)
+ = k\dim(\fg)/(2h^{\vee})$, and
  $\kappa(\widehat\fg_{k}) = \dim(\fg)(k+h^{\vee})/(2h^{\vee})$.
 \item Virasoro $\Vir_{c}$: $r(z) = (c/2)/z^{3} + 2T/z$ (cubic
  plus simple pole, no quartic), and $\kappa(\Vir_{c}) = c/2$.
@@ -488,13 +511,20 @@
 degree-$2$ $E_{1}$ shadow
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$
 in the pre-dualisation convention. Averaging over $\Sigma_{2}$
-projects onto the trivial isotypic component, which coincides
-with the scalar modular characteristic by the genus-$1$ curvature
-identification of Volume~I~Theorem~D. The example computations
-are recorded in \cite[Chapter~5]{Lorgat26I}; each formula is
-verified by the three independent paths of pole-order analysis,
-limiting case (at $k=0$, where $r$ vanishes), and
-cross-family consistency against the landscape census.
+projects onto the trivial isotypic component. For abelian
+Heisenberg families this scalar coincides with the full modular
+characteristic. For non-abelian affine Kac--Moody in the
+trace-form convention $r(z)=k\Omega_{\fg}/z$, the averaging sees
+only the double-pole channel and yields
+$\kappa_{\mathrm{dp}} = k\dim(\fg)/(2h^{\vee})$; the simple-pole
+self-contraction contributes the additional Sugawara term
+$\dim(\fg)/2$, so
+$\kappa = \kappa_{\mathrm{dp}} + \dim(\fg)/2$. The example
+computations are recorded in \cite[Chapter~5]{Lorgat26I}; each
+formula is verified by the three independent paths of pole-order
+analysis, the limiting case at $k=0$ for the trace-form
+$r$-matrix, and cross-family consistency against the landscape
+census.
 \end{proof}
 
 \begin{theorem}[Degree-$3$ averaging: associator to cubic shadow]
@@ -640,7 +670,10 @@
 $E_{1}$ Maurer--Cartan element is the $E_{1}$ degree-$2$
 characteristic package of $\cA$. It is universal, additive,
 antisymmetric under opposite-duality, and satisfies
-$\av(R^{E_{1},\mathrm{bin}}(z;\hbar)) = \kappa(\cA) + O(\hbar^{2})$.
+$\av(r_{0}(z)) = \kappa(\cA)$ on abelian families, while for
+non-abelian affine Kac--Moody one has
+$\av(r_{0}(z)) = \kappa_{\mathrm{dp}}(\cA)$ and
+$\kappa(\cA) = \kappa_{\mathrm{dp}}(\cA) + \dim(\fg)/2$.
 The coinvariant recovery of the scalar curvature from $r(z)$ is
 the content of Theorem~\ref{thm:av-degree-2}. A full higher-genus
 line-side modular $R$-matrix interpretation requires additional
@@ -667,11 +700,16 @@
 \label{rem:theorem-d-cleanest}
 Among the five, Theorem D makes the $E_{1}$ primacy thesis most
 concrete. The scalar modular characteristic $\kappa$ is a single
-number per family$ are distinct per family, never to be
-copied; the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$). Its degree-$2$ lift is a meromorphic function of a single
+number per family, and the family formulas are distinct: for
+$W_{N}$ the harmonic number is $H_{N} = \sum_{j=1}^{N} 1/j$ and
+must not be copied from a different family. Its degree-$2$ lift is a meromorphic function of a single
 variable, the collision coordinate $z$. The statement
-$\av(r(z)) = \kappa$ says: the scalar is the $\Sigma_{2}$-average
-of a function. This is a strict projection; the full function
+$\av(r(z)) = \kappa$ says this exactly for Heisenberg, while for
+non-abelian affine Kac--Moody the same averaging recovers only
+$\kappa_{\mathrm{dp}}$ and the full $\kappa$ adds the Sugawara
+shift $\dim(\fg)/2$. The scalar shadow is still the
+$\Sigma_{2}$-average of a function. This is a strict projection;
+the full function
 $r(z)$ carries information about the braiding, the quantum group,
 and the line-operator algebra that no scalar invariant can see.
 The universality property of $\kappa$ in Volume I Theorem D
@@ -739,7 +777,10 @@
 fully determined by the underlying $E_{\infty}$ vertex algebra
 structure; the $E_{1}$ refinement adds no new data at degree $2$
 beyond what is already visible in the OPE. The averaging map on
-tier (b) satisfies $\av(r(z)) = \kappa(\cA)$, and the kernel is
+tier (b) recovers the scalar degree-$2$ shadow: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$; the kernel is
 nontrivial but reconstructible from $\cA$.
 
 \subsection*{Tier (c): genuinely $E_{1}$}
@@ -845,9 +886,12 @@
 dg Lie algebras. The five foundational theorems A, B, C, D, H of
 modular Koszul duality admit ordered $E_{1}$ counterparts whose
 symmetric images are the classical theorems. Theorem D is the
-cleanest example: the scalar modular characteristic $\kappa$ is
-the degree-$2$ coinvariant of the spectral $r$-matrix $r(z)$, and
-the passage from $r(z)$ to $\kappa$ is a strict projection with
+cleanest example: the scalar degree-$2$ shadow is recovered from
+the spectral $r$-matrix $r(z)$ by averaging, giving $\kappa$
+for abelian families and $\kappa_{\mathrm{dp}}$ for non-abelian
+affine Kac--Moody before the Sugawara shift $\dim(\fg)/2$ is
+added; the passage from $r(z)$ to the scalar shadow is a strict
+projection with
 nontrivial kernel.
 
 Several problems remain open.
@@ -917,7 +961,10 @@
 T^{c}(s^{-1}\bar\cA)$ is the primitive object and the symmetric
 bar is its $\Sigma_{n}$-coinvariant shadow; the five theorems
 A, B, C, D, H are the invariants that survive the averaging, and
-Theorem D displays this most visibly as $\av(r(z)) = \kappa(\cA)$.
+Theorem D displays this most visibly at degree $2$: for Heisenberg
+$\av(r(z)) = \kappa(\cA)$, while for non-abelian affine
+Kac--Moody $\av(r(z)) = \kappa_{\mathrm{dp}}(\cA)$ and the full
+$\kappa(\cA)$ adds the Sugawara shift $\dim(\fg)/2$.
 
 % ================================================================
 \begin{thebibliography}{99}

tokens used
84,996
