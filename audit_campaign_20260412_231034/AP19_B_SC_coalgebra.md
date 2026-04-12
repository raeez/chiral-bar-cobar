# AP19_B_SC_coalgebra (410s, gpt-5.4)

[CRITICAL] Vol II `chapters/connections/3d_gravity.tex:5146` — Direct AP165/B54 violation: `$\SCchtop$ bar coalgebra.` In context, this sentence says `The half-plane bar complex ... is the $\SCchtop$ bar coalgebra`, which assigns Swiss-cheese coalgebra structure to the bar complex itself rather than to the derived-center pair.

[HIGH] Vol I `chapters/theory/en_koszul_duality.tex:1295` — Structural drift persists at the canonical source: `\label{thm:bar-swiss-cheese}% label retained for backward compatibility`. The theorem text is corrected to `E_1` coassociative coalgebra, but the live theorem label still encodes the retired Swiss-cheese reading and propagates through cross-volume references.

[HIGH] Vol II `chapters/theory/factorization_swiss_cheese.tex:1792` — Structural contradiction in a core theory chapter title: `The half-plane model as $\SCchtop$-coalgebra datum`. The same file opens by stating `The bar complex is not an $\SC^{\ch,\top}$-coalgebra` at lines 20-28, so this title reintroduces the forbidden object-level framing.

[MEDIUM] Vol II `chapters/connections/log_ht_monodromy_frontier.tex:744` — Prose conflation: `the connection arises from the Swiss-cheese bar complex`. This attributes Swiss-cheese structure to the bar complex instead of reserving it for the derived-center/bulk-boundary datum.

[MEDIUM] Vol II `chapters/connections/spectral-braiding-core.tex:601` — Prose conflation: `constructs via the Swiss-cheese bar complex and derived center.` The phrasing treats the bar complex itself as Swiss-cheese-flavoured rather than `E_1` with Swiss-cheese emerging only at the derived center.

[MEDIUM] Vol II `chapters/connections/anomaly_completed_topological_holography.tex:1840` — Prose conflation: `Swiss-cheese algebra is presented by the bar complex.` This collapses the bar complex / derived-center distinction on the audited surface.

All contextualized Volume III hits I checked were corrective, not violating; likewise several Vol I/II hits were false positives where the surrounding text explicitly says the bar complex is only `E_1`-coassociative.

## Summary
Instances checked: 29 | Violations found: 6 | Verdict: FAIL


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
session id: 019d83aa-a883-7451-9d01-229a43fb4411
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: Sweep for AP165/B54: B(A) is SC-coalgebra claim across all three volumes.

Run: grep -rni 'bar.*SC\|B(A).*SC\|coalgebra.*SC\|SC.*coalgebra' chapters/ | head -20

Expected: B(A) is E_1 coalgebra, NOT SC

For EACH hit:
1. Read surrounding context to determine if it's a genuine violation
2. Distinguish false positives from real violations
3. Report file:line and the exact violating text
4. Assess severity (CRITICAL if mathematical, HIGH if structural, MEDIUM if prose)
mcp startup: no servers

thinking
**Evaluating command options**

I’m considering using a tool to sweep through all volumes, but the final answer really needs to rely on actual tool outputs. The user specifically requested to run a grep command, so that’s likely the best route. I could use exec_command for that. Though I wonder if I need to use explorer first, since it's a codebase question. But since direct shell might be acceptable, I think I should stick with the developer's advice to prefer using rg for text or files.
codex
Using `deep-beilinson-audit` for a cross-volume falsification sweep of AP165/B54. I’ll read the constitutional surfaces that affect this claim, run the requested search in repo terms, then inspect each hit in context and classify only genuine violations.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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


thinking
**Analyzing search requirements**

I need to run checks on each volume, especially if it's over 20, to inspect all relevant aspects. I should use rg rather than grep for this, as the user's request is for a thorough sweep. Initially, I could run a quick check with head -20 and then follow up with a full search to ensure I don't miss anything. It's essential to keep the operation as read and report only, avoiding modifications. It seems that noting the current claimed status is also important.
thinking
**Running searches across volumes**

I need to use rg across different volumes since the network is restricted. It seems like a multi-tool approach would be helpful here, as I could run searches in parallel for efficiency. Including file lines in the results might be beneficial. I’ll start with a search that utilizes specific patterns like 'bar.*SC' or 'coalgebra.*SC' within the chapters. Using options like -g '*.tex' could also narrow down the results effectively. Let's proceed with that plan!
codex
The audit surface is now locked: AP165/B54, namely any claim that `B(A)` or “the bar complex” carries Swiss-cheese coalgebra structure rather than only `E_1` coalgebra structure. I’m sweeping all three `chapters/` trees first, then I’ll read every hit in context and discard false positives aggressively.
exec
/bin/zsh -lc "rg -n -i 'bar.*SC|B\\(A\\).*SC|coalgebra.*SC|SC.*coalgebra' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -i 'bar.*SC|B\\(A\\).*SC|coalgebra.*SC|SC.*coalgebra' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w-algebras-stable.tex:4:W-algebras are the decisive test cases for the $A_\infty$ chiral framework in the $d' = 1$ regime. The reason is structural: the pre-reduction affine vertex algebra $V_k(\mathfrak{g})$ is Koszul (Theorem~\ref{thm:one-loop-koszul}), so the transferred $A_\infty$ operations on bar cohomology vanish ($m_k = 0$ for $k \ge 3$), though the Swiss-cheese operations on $V_k(\mathfrak{g})$ itself have $m_3^{\mathrm{SC}} \neq 0$ (class~$\mathbf{L}$, depth~$3$). Drinfeld--Sokolov reduction changes this. The BRST functor manufactures the higher operations $m_k$ for $k \ge 3$ that break Swiss-cheese formality (Theorem~\ref{thm:ds-koszul-obstruction}): the quartic OPE pole of the Virasoro generator, the quintic pole of $W_3$, and the higher poles of $W_N$ are all artefacts of the reduction, absent in the affine input. The resulting $\mathcal{W}$-algebra remains chirally Koszul (the bar complex is well-behaved), but the $A_\infty$ structure is genuinely infinite. This section computes the $A_\infty$ operations, spectral $r$-matrices, and deformation data for Virasoro and $W_3$ via the Khan--Zeng 3D holomorphic-topological Poisson sigma model \cite{KZ25}.
chapters/frame/preface_trimmed.tex:189:makes $B(\cA)$ into a coassociative coalgebra over $\mathrm{Ass}^{\scriptstyle\text{\rm !`}}$.
chapters/examples/examples-complete-proved.tex:851: \Hom(\barB^{(0,2)}(\SCop), \End_{V_k(\fg)})$
chapters/examples/examples-worked.tex:16:bar complex; the \emph{extended landscape}
chapters/examples/examples-worked.tex:1764:\begin{conjecture}[M2--M5 bar-cobar duality; \ClaimStatusConjectured]
chapters/examples/rosetta_stone.tex:967:\begin{proposition}[Bar cohomology and Hochschild cohomology;
chapters/examples/rosetta_stone.tex:969:\label{prop:rosetta-bar-hochschild}
chapters/examples/rosetta_stone.tex:1644: & $e^{k\hbar/z}$ (scalar, abelian) \\[2pt]
chapters/examples/rosetta_stone.tex:1877:$\S$\ref{sec:shadow-tower-atlas}--\ref{subsec:e1-ordered-bar-landscape}
chapters/examples/rosetta_stone.tex:2813:p.~\pageref{comp:e1-ordered-bar-landscape}, we record
chapters/examples/rosetta_stone.tex:3919:bar cogenerators appear. For $d = 2$ with scalar residues,
chapters/examples/rosetta_stone.tex:4181:(Proposition~\ref{prop:rosetta-bar-hochschild})
chapters/examples/rosetta_stone.tex:5539:\subsection{The complete E$_1$ ordered bar landscape}%
chapters/examples/rosetta_stone.tex:5540:\label{subsec:e1-ordered-bar-landscape}%
chapters/examples/rosetta_stone.tex:5541:\index{ordered bar complex!landscape table|textbf}%
chapters/examples/rosetta_stone.tex:5549:complete ordered bar landscape: all invariants of the
chapters/examples/rosetta_stone.tex:5553:\begin{computation}[Complete $\Eone$ ordered bar landscape;
chapters/examples/rosetta_stone.tex:5555:\label{comp:e1-ordered-bar-landscape}%
chapters/examples/rosetta_stone.tex:5556:\index{ordered bar complex!landscape!master table}%
chapters/examples/rosetta_stone.tex:5804:(Computation~\ref{comp:e1-ordered-bar-landscape})
 succeeded in 52ms:
Total output lines: 342

chapters/frame/preface_sections10_13_draft.tex:75:and the bar-cobar adjunction on $\SCchtop$-algebras is a Quillen
chapters/frame/preface_sections10_13_draft.tex:78:$\SCchtop$-algebras is equivalent to that of coalgebras over the Koszul
chapters/examples/deformation_quantization.tex:145:The quantization problem for coisson algebras reduces to the existence of a Maurer--Cartan element in the chiral deformation complex. By Theorem~\ref{thm:curved-mc-cobar}, solutions to the curved Maurer--Cartan equation $d\alpha + \frac{1}{2}[\alpha,\alpha] + m_0 = 0$ parametrize deformations. The obstruction to existence lies in $H^2$ of the chiral Hochschild complex (classical deformation theory enhances to the chiral setting via Theorem~\ref{thm:geometric-equals-operadic-bar}).
chapters/examples/deformation_quantization.tex:515:The quantization of $W_3$ involves the central charge $c$ (from $\hbar^1$), structure constants $\lambda, \mu$ (from $\hbar^2, \hbar^3$), and screening charges (non-perturbative corrections).
chapters/examples/deformation_quantization.tex:525:\[W_3^{-22/5} \text{ bar complex} = \text{Free theory} \oplus \text{Screening operators}\]
chapters/examples/deformation_quantization.tex:715:The mathematical content (that the genus expansion $\sum_g \hbar^{2g-2} F_g$ is computed via configuration space integrals on the modular convolution algebra) is established in the preceding sections. The interpretation as a bulk-boundary holographic duality in $\mathrm{AdS}_3/\mathrm{CFT}_2$ requires physical input (Chern--Simons/WZW correspondence, bulk reconstruction) beyond the scope of this monograph.
chapters/connections/typeA_baxter_rees_theta.tex:320:$f(u)=-\hbar u^{-1}$. Passing to the reduced quotient removes the scalar
chapters/examples/w_algebras_deep.tex:21:bar coalgebra structure, screening operators, and Toda field theory.
chapters/examples/w_algebras_deep.tex:515:The bar-complex dimensions across the simple types (Table~\ref{comp:w-bar-dims}) display a uniform pattern: at each bar degree the chain spaces are infinite-dimensional but graded-finite under the conformal weight grading, and the growth rates are governed by a single discriminant $\Delta(x)$ that is invariant under both DS reduction and Koszul duality. This uniformity persists in the large-$N$ limit, made precise below.
chapters/examples/w_algebras_deep.tex:1528:\begin{remark}[Barbasch--Vogan duality as Springer duality of Slodowy slices]
chapters/examples/w_algebras_deep.tex:1530:\index{Barbasch--Vogan duality!Springer geometry}
chapters/examples/w_algebras_deep.tex:1537:Barbasch--Vogan dual $f^D$ has Slodowy slice $S_{f^D}$. The
chapters/examples/w_algebras_deep.tex:2094:The Barbasch--Vogan duality
chapters/examples/w_algebras_deep.tex:2710:bar-intrinsic MC element descends:
chapters/examples/bar_complex_tables.tex:492:This is the most complex bar differential in the manuscript: it produces components
chapters/examples/bar_complex_tables.tex:533:See Theorem~\ref{thm:w-bar-curvature} for the full discussion.
chapters/examples/bar_complex_tables.tex:1989:Parts~\ref{part:bar-complex}--\ref{part:standard-landscape} (configuration space integrals, FM
chapters/examples/bar_complex_tables.tex:4198:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
exec
/bin/zsh -lc "rg -n -i 'bar.*SC|B\\(A\\).*SC|coalgebra.*SC|SC.*coalgebra' chapters/" in /Users/raeez/calabi-yau-quantum-groups succeeded in 53ms:
chapters/examples/toroidal_elliptic.tex:1862:\subsection{Bar complex of the $\cN = 4$ SCA}
chapters/examples/toroidal_elliptic.tex:1866:\label{prop:bar-n4-sca}
chapters/examples/toroidal_elliptic.tex:1867:\index{bar complex!N=4 SCA}
chapters/examples/toroidal_elliptic.tex:1868:The bar complex $B(\cA_{K3})$ of the small $\cN = 4$ SCA at
chapters/examples/toroidal_elliptic.tex:1949:\texttt{cy\_bar\_n4sca\_engine.py}.
chapters/examples/toroidal_elliptic.tex:4123:\label{rem:bar-descent}
chapters/examples/toroidal_elliptic.tex:4124:\index{bar complex!descent}
chapters/examples/toroidal_elliptic.tex:4125:Proposition~\ref{prop:bar-hocolim} gives a descent theorem for
chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
chapters/connections/modular_koszul_bridge.tex:276: \item \emph{Categorical Hochschild.} The cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ with Hochschild differential $b$ and Connes operator $B$. This is the topological invariant of $\cC$ as a dg category: it carries the Gerstenhaber bracket and the $(2-d)$-shifted Poisson structure from the Serre pairing (Chapter~\ref{ch:hochschild-calculus}).
chapters/connections/modular_koszul_bridge.tex:297:Part (i) is Proposition~\ref{prop:bar-dictionary}. For (ii): the Gerstenhaber bracket on $\HH^\bullet(\cC)$ is a Lie bracket of degree $-1$. Under $\Phi$, this bracket becomes the convolution bracket of Vol~I by functoriality of the bar construction: the deconcatenation coproduct on $B(A_\cC)$ and the binary product of $A_\cC$ assemble into a bracket on $\Hom_{\Ran}(B(A_\cC), A_\cC)$, which restricts to $\ChirHoch^*(A_\cC)$ on the cohomology. The Connes operator $B$ on $\mathrm{CC}_\bullet(\cC)$ corresponds, under the bar dictionary, to the degree-preserving component of the bar differential (Proposition~\ref{prop:bar-dictionary}(ii)), which is the modular differential on the chiral side. For (iii): the categorical Hochschild cochains $\mathrm{CC}^\bullet(\cC, \cC)$ map to $\RHom(\Omega B(A_\cC), A_\cC)$ by applying $\Phi$ to each hom-space and using the bar-cobar quasi-isomorphism $\Omega B(A_\cC) \simeq A_\cC$ (Vol~I Theorem~B on the Koszul locus).
chapters/connections/bar_cobar_bridge.tex:37: \item The Hodge filtration on $\HH_*(\cC)$ corresponds to the degree filtration on $B(A)$: the degree-$r$ piece $B^{(r)}(A)$ captures Hochschild chains of tensor length $\leq r$.
chapters/connections/bar_cobar_bridge.tex:262:The banana manifold is the prototypical example : $\kappa_{\mathrm{ch}} = 0$ does \emph{not} imply $\Theta_A = 0$. The vanishing of $\kappa_{\mathrm{ch}}$ means the bar complex is uncurved ($d^2 = 0$ at the leading scalar level), but the higher-degree components of $\Theta_A$ (the quartic shadow $Q$ and beyond) are nonvanishing, sourced by the instanton contributions (genus-$0$ GV invariants of the banana curves).
chapters/theory/en_factorization.tex:351:\emph{Important scope restriction} (AP153): For $\Eone$ input (e.g.\ the CoHA or an ordered bar algebra), the Deligne conjecture gives only $\Etwo$ on Hochschild cochains. The $E_3$ claim requires the input to be at least $\Etwo$.
chapters/theory/en_factorization.tex:726:Dunn additivity $\En \simeq \Eone^{\otimes n}$ suggests that $\En$ Koszul duality should decompose as $n$ iterated $\Eone$ Koszul dualities. This is too optimistic. The Koszul dual $A^!$ is determined by the \emph{joint} $\En$-coalgebra structure on $B_{\En}(A)$, not by the $n$ separate $\Eone$-coalgebra structures independently. The Miki automorphism (Conjecture~\ref{conj:miki-from-e3}) is the obstruction to such a decomposition: it permutes the three $\Eone$-factors cyclically, and the $E_3$ Koszul duality must respect this $S_3$-symmetry. A decomposition into three independent $\Eone$ Koszul dualities would break $S_3$ to the identity, losing the Miki symmetry. The cascade is a \emph{tower}, not a product.
chapters/theory/drinfeld_center.tex:479: \item \emph{Bar-cobar/Hochschild compatibility.}
chapters/theory/braided_factorization.tex:260:\label{rem:e2-bar-not-sc}
chapters/theory/braided_factorization.tex:262:a Swiss-cheese ($\SC^{\mathrm{ch,top}}$) coalgebra. The SC structure of
chapters/theory/e1_chiral_algebras.tex:142:Let $\cC$ be a CY$_2$ category with cyclic $A_\infty$ structure and negative-cyclic trace. The ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries a natural $E_1$-chiral structure whose holomorphic direction matches the Hochschild differential and whose ordered direction matches the cyclic action on the bar coalgebra.
chapters/theory/e1_chiral_algebras.tex:217:\item \textbf{Symmetric bar $B^{\Sigma}$}: the $S_n$-coinvariant quotient of $B^{\mathrm{ord}}$ with the coshuffle coproduct descended from the shuffle product on $T^c$. Natural $E_\infty$-object. Source of the modular characteristic $\kappa_{\mathrm{ch}}$.



thinking
**Refining search queries**

I see that the search results are quite extensive and often truncated, which makes it important to isolate the relevant hits precisely. I’ll need to focus only on entries matching AP165/B54. The current broad regex query is causing a lot of false positives. Since the user wants each hit from the grep, it seems important to look into potential violations specifically within the chapters of the repository. I plan to audit fully across all three volumes while identifying genuine matches related to the “bar complex is SC coalgebra” claims, narrowing down the search to avoid incidental mentions.
thinking
**Identifying potential violations**

I’m pinpointing potential hits related to possible violations in the documents. For instance, the V1 frame/heisenberg_frame theorem registry references the “sl2 bar complex as Swiss-cheese coalgebra,” which could be a genuine violation. V2 has various lines that warn about the “swiss cheese” and may also mention the bar coalgebra. There are instances like comments on the transition from SC-algebra to A∞ data, and specific mentions like “bar element parameterized by FM_k(C).” It’s important to clarify these references for accuracy.
thinking
**Inspecting transverse bar complex**

I'm looking into the transverse bar complex, which might indicate a potential violation. In V2, the document bar-cobar-review.tex references "Theorem\ref{thm:bar-swiss-cheese}," discussing the E1 dg coalgebra structure of Bbar, so it needs closer inspection to verify if the theorem is now corrected or stale. Meanwhile, V3 has a line stating it's not a Swiss-cheese coalgebra, which seems likely corrected. I should run targeted queries across volumes to find exact phrases related to “swiss-cheese coalgebra” and others, and compile a list of candidate files.
codex
The first pass over the broad regex is noisy. I’m tightening to the actual AP165/B54 surface now: direct claims that the bar complex itself is an `SC` or Swiss-cheese coalgebra, plus stale theorem labels that still advertise that claim.
exec
/bin/zsh -lc "rg -n -i 'SC-?coalgebra|Swiss-?cheese coalgebra|bar-swiss-cheese|bar complex.*Swiss|bar complex.*SC|B\\(A\\).*SC|SC.*B\\(A\\)|SCchtop.*coalgebra|coalgebra.*SCchtop' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -i 'SC-?coalgebra|Swiss-?cheese coalgebra|bar-swiss-cheese|bar complex.*Swiss|bar complex.*SC|B\\(A\\).*SC|SC.*B\\(A\\)|SCchtop.*coalgebra|coalgebra.*SCchtop' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -i 'SC-?coalgebra|Swiss-?cheese coalgebra|bar-swiss-cheese|bar complex.*Swiss|bar complex.*SC|B\\(A\\).*SC|SC.*B\\(A\\)|SCchtop.*coalgebra|coalgebra.*SCchtop' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:1862:\subsection{Bar complex of the $\cN = 4$ SCA}
chapters/examples/toroidal_elliptic.tex:1867:\index{bar complex!N=4 SCA}
chapters/examples/toroidal_elliptic.tex:1868:The bar complex $B(\cA_{K3})$ of the small $\cN = 4$ SCA at
chapters/examples/toroidal_elliptic.tex:4124:\index{bar complex!descent}
chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
chapters/connections/modular_koszul_bridge.tex:276: \item \emph{Categorical Hochschild.} The cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ with Hochschild differential $b$ and Connes operator $B$. This is the topological invariant of $\cC$ as a dg category: it carries the Gerstenhaber bracket and the $(2-d)$-shifted Poisson structure from the Serre pairing (Chapter~\ref{ch:hochschild-calculus}).
chapters/theory/introduction.tex:13:A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
chapters/theory/introduction.tex:15:That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
chapters/theory/hochschild_calculus.tex:23:This chapter develops the Hochschild calculus underlying the CY-to-chiral functor of Chapter~\ref{ch:cy-to-chiral}. The shifted Poisson structure on $\HH^\bullet(\cC)$ is the categorical precursor of the convolution Lie bracket on the modular deformation complex of Volume~I: the Gerstenhaber bracket becomes the bar-cobar convolution bracket, the Connes $B$-operator becomes the modular differential, and the Serre pairing becomes the cyclic duality that controls the $\bS^d$-framing. The cyclic bar complex of Chapter~\ref{ch:cyclic-ainf} is the single-object specialization of the Hochschild complex constructed here.
chapters/theory/braided_factorization.tex:259:\begin{remark}[$B_{E_2}(\cA)$ is not a Swiss-cheese coalgebra]
chapters/connections/bar_cobar_bridge.tex:37: \item The Hodge filtration on $\HH_*(\cC)$ corresponds to the degree filtration on $B(A)$: the degree-$r$ piece $B^{(r)}(A)$ captures Hochschild chains of tensor length $\leq r$.
chapters/connections/bar_cobar_bridge.tex:262:The banana manifold is the prototypical example : $\kappa_{\mathrm{ch}} = 0$ does \emph{not} imply $\Theta_A = 0$. The vanishing of $\kappa_{\mathrm{ch}}$ means the bar complex is uncurved ($d^2 = 0$ at the leading scalar level), but the higher-degree components of $\Theta_A$ (the quartic shadow $Q$ and beyond) are nonvanishing, sourced by the instanton contributions (genus-$0$ GV invariants of the banana curves).
chapters/theory/cy_to_chiral.tex:170:These five objects are distinct: $B(A)$ is a coalgebra, $A^!$ is an algebra, and the cobar recovery $\Omega(B(A)) \simeq A$ is \emph{inversion}, not Koszul duality. The derived center $\Zder(A)$ arises from Hochschild cochains, not from bar-cobar.
chapters/theory/cy_to_chiral.tex:1430:The conjecture does NOT claim that the naive numerical DT invariants (e.g., the Fourier coefficients of $\Delta_5$ for $K3 \times E$) are recovered by the scalar shadow $\kappa_{\mathrm{ch}}$ alone. The higher Fourier coefficients encode information from the full bar complex (all degrees), not merely the leading shadow coefficient. The scalar shadow captures the leading asymptotics; the refined shadow (bar cohomology at all degrees) captures the full DT data.
chapters/theory/cy_to_chiral.tex:1828:% AP165: SC^{ch,top} lives on the derived center pair, NOT on B(A).
chapters/theory/cy_to_chiral.tex:1829:The bar complex $B(A)$ is an $\Eone$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$; the $\SC^{\mathrm{ch,top}}$ two-colour structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on the bar complex itself. Three bar constructions reflect three levels of operadic symmetry:
chapters/connections/geometric_langlands.tex:36:Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
chapters/theory/quantum_chiral_algebras.tex:264: \item The \emph{chiral CE cochains} are the chiral Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(A, A) = \RHom(\Omega B(A), A)$, the chiral derived center $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ of Vol~I Theorem~H. This is the analogue of $C^\bullet(\frakg, \frakg) = \Hom(\bigwedge^\bullet \frakg, \frakg)$, the Chevalley--Eilenberg cochains with adjoint coefficients.
chapters/theory/quantum_chiral_algebras.tex:476:At $n = 2$: affine Yangian $\to$ bar complex $\to$ dual Yangian $\to$ quantum group braiding (PARTIALLY ESTABLISHED, via Schiffmann--Vasserot / Maulik--Okounkov).
chapters/theory/e1_chiral_algebras.tex:142:Let $\cC$ be a CY$_2$ category with cyclic $A_\infty$ structure and negative-cyclic trace. The ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries a natural $E_1$-chiral structure whose holomorphic direction matches the Hochschild differential and whose ordered direction matches the cyclic action on the bar coalgebra.
 succeeded in 52ms:
chapters/examples/examples-worked.tex:16:bar complex; the \emph{extended landscape}
chapters/connections/ht_bulk_boundary_line_frontier.tex:126:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}.
chapters/connections/ht_bulk_boundary_line_frontier.tex:229:Statement~(ii) is Theorem~\ref{thm:bar-swiss-cheese} (the
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:210:scalar class vanishes and the bar complex is uncurved on the scalar
chapters/connections/spectral-braiding-core.tex:13:The $E_1$ bar construction resolves all three deficiencies at once. The ordered bar coalgebra $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with its deconcatenation coproduct \emph{is} the Yangian's coproduct: the spectral parameter is the coordinate on $\C$ (the holomorphic direction), the coproduct arises from the $E_1$-factorization along the topological half-line $\R_{\ge 0}$, and the Yang--Baxter equation is Stokes' theorem on the Fulton--MacPherson compactification $\FM_3(\C)$. The $\SCchtop$ structure emerges not on $B(A)$ itself but on the chiral derived center: the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ of chiral Hochschild cochains and boundary algebra is the $\SCchtop$ datum. The symmetric bar $B^\Sigma$ is the $\Sigma_n$-coinvariant shadow; $R$-matrix descent relates $B^{\mathrm{ord}}$ to $B^\Sigma$.
chapters/connections/spectral-braiding-core.tex:555:A \emph{meromorphic braided tensor category} is a category $\cC$ equipped with a tensor product $\Theta_z\colon \cC \otimes \cC \to \cC[\![z]\!]$ depending meromorphically on a complex parameter $z$, together with a braiding $R(z)\colon \Theta_z \to \Theta_z^{\mathrm{op}}$ that is meromorphic in $z$ and satisfies the hexagon axioms up to meromorphic correction along the diagonal. In the Vol~II framework, the ordered bar coalgebra $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ (with $\bar A = \ker \varepsilon$ the augmentation ideal,) \emph{classifies} meromorphic braided tensor categories via its spectral braiding $R(z)$ of Definition~\ref{def:spectral-braiding}: the holomorphic colour $\C_z$ of $\SCchtop$ supplies the spectral parameter, while the topological colour $\R_{\geq 0}$ supplies the strict associativity and the ordering that generates the braid group action. This is the categorical reading of Dimofte's slab-and-fibre functor picture~\cite{Dimofte25} (PIRSA 25110067).
chapters/connections/spectral-braiding-core.tex:2382:A pure $E_1$ bar complex would discard this data and produce a
chapters/connections/spectral-braiding-core.tex:3472:$(\SCchtop)^!$-coalgebras via the operadic bar-cobar
chapters/connections/ym_instanton_screening.tex:764:Polyakov~\cite{Pol87} argues that confinement in compact QED arises from monopole condensation: magnetic monopoles condense, squeezing electric flux into strings between charges (the dual Meissner effect). In bar-cobar language, the instanton-completed bar complex $B^\Lambda(\cA)$ (Theorem~\ref{thm:novikov-completion-theorem}) carries the non-perturbative data. The screening formalism on the dual side, the visible center $Z_{\mathrm{vis}}$ of Definition~\ref{def:visible-center-and-couplings}, is the algebraic confinement criterion: the vanishing $Z_{\mathrm{vis}} = 0$ translates monopole condensation into the statement that no center-symmetric deformations survive instanton-generated screening.
chapters/connections/spectral-braiding-frontier.tex:379:\,d\lambda$ produces the infinitesimal braiding, and the full quantum $R(z)$ produces the finite braiding. For the affine lineage, this is proved unconditionally: one-loop exactness collapses the $A_\infty$ tower, on the reduced evaluation comparison surface the reduced HT monodromy identifies with the KZ monodromy, and the affine Drinfeld--Kohno theorem compares that monodromy with the corresponding braided tensor-product representation of $\mathrm{Rep}_q(\fg)$ there (Theorem~\ref{thm:affine-monodromy-identification}). On the $\mathfrak{sl}_2$ weight system, the bar complex integrals over $\FM_n(\C) \times \Conf_n(\R)$ compute the colored Jones polynomial (Corollary~\ref{cor:jones-polynomial}), recovering the Reshetikhin--Turaev invariant directly from the Swiss-cheese structure. The all-types categorical Clebsch--Gordan and
chapters/connections/spectral-braiding-frontier.tex:2320:coalgebra; the $\SCchtop$~structure emerges not from $B(A)$ itself
chapters/examples/rosetta_stone.tex:5541:\index{ordered bar complex!landscape table|textbf}%
chapters/examples/rosetta_stone.tex:5556:\index{ordered bar complex!landscape!master table}%
chapters/connections/thqg_ht_bbl_extensions.tex:2316:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}.
chapters/connections/ordered_associative_chiral_kd_core.tex:2419:ordered bar complex. The descended local system is the
chapters/connections/ordered_associative_chiral_kd_core.tex:4596:close the two-sided cobar complex into the coHochschild
chapters/connections/log_ht_monodromy_core.tex:2046:The bar complex of $V^k(\mathfrak{sl}_2)$, viewed as a logarithmic $\SCchtop$-algebra, produces a flat connection on configuration spaces by Theorem~\ref{thm:synthesis}. By Theorem~\ref{thm:affine-monodromy-identification}(i)--(ii), on the reduced evaluation comparison surface the monodromy of this connection identifies with the KZ monodromy, and the affine Drinfeld--Kohno theorem compares it with the corresponding braided tensor-product representation of $\mathrm{Rep}_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$. In particular, the bar complex computes the braid-group representation
chapters/connections/ym_synthesis_core.tex:289:For the affine lineage (generic-level affine Kac--Moody and principal $\cW$-algebras obtained by Drinfeld--Sokolov reduction), the Koszul property (Theorem~\ref{thm:one-loop-koszul}) ensures that the chiral bar complex $\barBch(\cA_{\cB})$ is a resolution of $\cA_{\cB}^!$. Chiral Hochschild cohomology is then computed by the bar resolution:
chapters/connections/relative_feynman_transform.tex:1322:bar coalgebra of~$\SCchtop$. The differential $D_0|_{\gr^0}$
chapters/connections/relative_feynman_transform.tex:1324:conilpotent dg coalgebra over $B(\SCchtop)$. Since $\SCchtop$
 succeeded in 51ms:
chapters/examples/deformation_quantization.tex:525:\[W_3^{-22/5} \text{ bar complex} = \text{Free theory} \oplus \text{Screening operators}\]
chapters/examples/lattice_foundations.tex:4917:cycles in the bar complex (which control Hochschild via bar-cobar)
chapters/examples/beta_gamma.tex:358:Unlike the Heisenberg bar complex (\S\ref{sec:frame-bar-all}), where $d_{\mathrm{bracket}} = 0$ because the abelian OPE has no simple pole, $\beta\gamma$ has a nontrivial bar differential: the mixed OPE $\beta(z)\gamma(w) \sim 1/(z-w)$ kills every element containing both $\beta$ and $\gamma$ factors (via $\operatorname{Res}[\beta\gamma \cdot \eta_{ij}] = 1$), while pure $\beta^{\otimes n}$ and $\gamma^{\otimes n}$ tensors are cocycles. This is the chain-level mechanism behind $3^n$ growth: the differential acts on mixed pairs but not on pure types or their conformal descendants.
chapters/examples/w3_composite_fields.tex:845:bar complex at weight $h + \ell$, which records the descendants)
chapters/examples/free_fields.tex:723:The $\beta\gamma$ system combines a bosonic weight-$1$ field $\beta$ and a bosonic weight-$0$ field $\gamma$. Its bar complex shares the discriminant $\Delta(x) = (1-3x)(1+x)$ with $\widehat{\mathfrak{sl}}_2$ and the Virasoro algebra. The Koszul dual is the $bc$ ghost system (\S\ref{sec:fermion-boson-koszul}).
chapters/examples/free_fields.tex:4508:\subsubsection{Bar complex and critical descent}\label{sec:virasoro-bar-moduli-main}
chapters/examples/free_fields.tex:4526:Hence at $c = 26$ the equivariant bar complex descends to a genuine
chapters/examples/free_fields.tex:4543:The bar complex $\bar{B}^n_{\mathrm{geom}}(\mathrm{Vir}_c)$ consists of logarithmic forms on $\overline{C}_{n+1}(\mathbb{P}^1)$ with coefficients in $\mathrm{Vir}_c^{\boxtimes(n+1)}$. The Virasoro Ward identities (annihilation by $L_{-1}, L_0, L_1$) precisely implement the $\mathrm{PSL}_2$-equivariance condition: a form $\omega \in \bar{B}^n$ satisfying $\iota_{L_k}\omega = 0$ for $k = -1, 0, 1$ descends to $\overline{\mathcal{M}}_{0,n+3}$.
chapters/examples/free_fields.tex:5342:The Wakimoto bar complex admits a description via decorated graphs in which vertices carry Wakimoto generators, edges carry log-form propagators $\eta_{ij} = d\log(z_i - z_j)$, and the differential implements Wick contraction (Feynman rule interpretation). See Chapter~\ref{chap:w-algebras} for the complete graphical calculus.
chapters/examples/kac_moody.tex:1800:At critical level $k = -h^\vee$, the bar complex differential is determined by the screening charges:
chapters/examples/kac_moody.tex:4093:The supertrace over the bar complex gives a denominator $\eta(\tau)^{-8}$ from the $\dim(\mathfrak{sl}_3) = 8$ bosonic oscillators (cf.\ Proposition~\ref{prop:sl2-genus1-partition} for $\mathfrak{sl}_2$). The first correction involves the regularized self-energy:
chapters/examples/toroidal_elliptic.tex:1810:\subsection{Bar complex of the $\cN = 4$ SCA}
chapters/examples/toroidal_elliptic.tex:1815:\index{bar complex!N=4 SCA}
chapters/examples/toroidal_elliptic.tex:1816:The bar complex $B(\cA_{K3})$ of the small $\cN = 4$ SCA at
chapters/examples/toroidal_elliptic.tex:3901:\index{bar complex!descent}
chapters/examples/deformation_quantization_examples.tex:616:For $\mathrm{Vir}_c$ via DS reduction of $\widehat{\mathfrak{sl}}_2$ at level $k$: the Koszul dual is $\mathrm{Vir}_{26-c}$ (Theorem~\ref{thm:w-algebra-koszul-main}), with curvatures $\kappa(c)=c/2$, $\kappa(c')=(26-c)/2$, summing to $13$ independently of $c$. At $c=0$ the bar complex is uncurved while the dual is maximally curved; at $c=26$ the roles reverse, giving the algebraic uncurved-shadow configuration that appears in the no-ghost discussion.
chapters/connections/thqg_introduction_supplement_body.tex:67:(Theorem~\ref{thm:bar-swiss-cheese}).
chapters/examples/landscape_census.tex:2107:\index{bar complex!generating function!shared discriminant}
chapters/examples/landscape_census.tex:2645:\index{bar complex!discriminant families}
chapters/connections/feynman_connection.tex:137:\begin{conjecture}[Bar complex = path integral for the free boson; \ClaimStatusConjectured]\label{conj:bar-cobar-path-integral-heisenberg}





thinking
**Inspecting candidate files**

I need to look carefully at the candidate files and lines. The user wants to check each hit found by grep, focusing on their surrounding context to see if they are genuine violations. There are quite a few hits, but I can manage by filtering for direct violations. I should also conduct additional searches for specific theorem labels and exact statements. My goal is to create a final report that only includes genuine discrepancies, while removing any false positives. I'll focus on the necessary context from the candidate lines.
thinking
**Reviewing theorem labels and contexts**

I need to dive into specific chapters to see if any theorem labels have been retained for backward compatibility. For instance, in chapters/theory/en_koszul_duality.tex, I should inspect lines 1251-1305 and 1437. If the theorem statement has been corrected, the label `thm:bar-swiss-cheese` might no longer be violating anything. However, I need to check references around line 1437 to confirm its accuracy.

In chapters/connections/holomorphic_topological.tex, I’ll look for potential mischaracterizations regarding SC structure. Also, for chapters/frame/preface_sections10_13_draft.tex, some lines about the bar-cobar adjunction may need clarification.
thinking
**Inspecting theorem references**

I think I need to use the exact label `thm:bar-swiss-cheese` across all volumes to check the contexts. There could be many mischaracterizations of the theorem. I should also inspect each reference where the text mentions what the theorem says. It's possible the user asked for a report on exact violating text. Structural issues could arise if stale theorem titles or descriptions misstate the theorem's content. I should gather a candidate list from my search first and then inspect each one carefully.
thinking
**Enumerating candidates for inspection**

I'm considering a list of likely candidates for inspection. First, there’s Vol I, specifically `chapters/frame/heisenberg_frame.tex` around lines 2690-2765. Then, `en_koszul_duality.tex` at lines 1240-1310 and 1428-1445. Also, there's `holomorphic_topological.tex` with a range from 20-40, 115-150, and 1228-1242. I should check `thqg_introduction_supplement_body.tex` between 55-75 too. Moving to Vol II, I want to look at `bar-cobar-review.tex`, `factorization_swiss_cheese.tex`, and a few more chapters. I’ll need to assess these ranges closely.
thinking
**Searching for contexts**

I’m thinking about searching for "Swiss-cheese" in specific chapters, particularly in the Heisenberg frame context. This might be a broad approach, but I need to consider if "thm:Obs-is-SC" in the Volume II introduction could work, although it might not be complex enough. I’ll definitely want to inspect that candidate and examine the contexts around it. I think using a parallel approach could really help clarify things.
codex
I’ve narrowed the surface to the files that actually look dangerous rather than incidental `SC` mentions. Next I’m reading the local theorem statements and nearby prose to separate real mathematical violations from corrected text and stale labels.
exec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '2705,2795p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1430,1450p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement_body.tex | sed -n '55,75p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holomorphic_topological.tex | sed -n '1228,1242p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1245,1315p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holomorphic_topological.tex | sed -n '20,150p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2705	bar differential.
  2706	
  2707	\begin{remark}[The two components have different geometric origins]
  2708	\label{rem:rosetta-two-components}
  2709	The bracket component $d_{\mathrm{bracket}}$ extracts
  2710	$\Res_{z_1 = z_2}[c_1(z_2)/(z_1 - z_2)]$, the coefficient of
  2711	the simple pole in the OPE. The curvature component
  2712	$d_{\mathrm{curvature}}$ extracts
  2713	$\Res_{z_1 = z_2}[c_2/(z_1 - z_2)^2]$, the coefficient of the
  2714	double pole. On the Fulton--MacPherson compactification
  2715	$\FM_2(\mathbb{C})$, these correspond to the first and second
  2716	boundary jet of the logarithmic form $\eta_{12}$ along the diagonal
  2717	$D_{12}$. The simple pole contributes to $\partial\FM_2$ at
  2718	first order; the double pole requires the exceptional fiber
  2719	direction of the blowup.
  2720	\end{remark}
  2721	
  2722	The degree-$2$ analysis of
  2723	\S\ref{subsec:frame-sl2-bar-low-degree} shows that
  2724	$d_{\mathrm{bracket}}^2 \neq 0$ on the element
 succeeded in 52ms:
  1430	 = \operatorname{Lie}^c \circ s^{-1}\bar{\cA}$ (Harrison).
  1431	\item Open sector: $B_{\operatorname{Ass}}(\cA)
  1432	 = T^c(s^{-1}\bar{\cA})$ (tensor).
  1433	\item Mixed sector: dimension $(k{-}1)!\,\binom{k+m}{m}$
  1434	 at bi-degree $(k,m)$
  1435	 (Proposition~\textup{\ref{prop:sc-koszul-dual-three-sectors}}).
  1436	\end{itemize}
  1437	Theorem~\textup{\ref{thm:bar-swiss-cheese}} is the statement that
  1438	the bar of a chiral algebra, promoted to an
  1439	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra via self-action,
  1440	naturally carries the $\Eone$-chiral coassociative dg coalgebra structure.
  1441	\end{construction}
  1442	
  1443	\begin{remark}[Ordered Verdier duality does not exist]
  1444	\label{rem:ordered-verdier-nonexistence}
  1445	\index{Verdier duality!ordered bar obstruction}
  1446	The Verdier intertwining
  1447	$\mathbb{D}_{\mathrm{Ran}}\barB^{\Sigma}(\cA) \simeq \barB^{\Sigma}(\cA^!)$
  1448	(Theorem~A, Convention~\textup{\ref{conv:bar-coalgebra-identity}})
  1449	is a statement about the \emph{symmetric} bar~$\barB^{\Sigma}$
 succeeded in 52ms:
  1245	\end{definition}
  1246	
  1247	\begin{principle}[The bar complex is $\Eone$-chiral coassociative;
  1248	$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
  1249	\label{princ:sc-two-incarnations}
  1250	\index{Swiss-cheese operad!on derived center, NOT on bar}
  1251	\index{bar complex!is E1 coassociative, NOT SC}
  1252	The ordered bar complex
  1253	$\barB^{\mathrm{ord}}(\cA) = T^c(s^{-1}\bar{\cA})$
  1254	is an $\Eone$-chiral coassociative coalgebra: a coalgebra
  1255	over the Koszul dual cooperad
  1256	$(\operatorname{Ass}^{\mathrm{ch}})^{\scriptstyle !}$.
  1257	It has a differential (from OPE collision residues) and a
  1258	coassociative deconcatenation coproduct. These are the two
  1259	structures of a dg coalgebra. The bar complex does \emph{not}
  1260	carry $\mathsf{SC}^{\mathrm{ch,top}}$ structure.
  1261	
  1262	The $\mathsf{SC}^{\mathrm{ch,top}}$ structure emerges on
  1263	the \emph{derived chiral center}
  1264	$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 succeeded in 52ms:
  1228	The body of work by Gaiotto and
  1229	collaborators~\cite{gaiotto-rapchak,CostelloGaiotto2020,GKW2025}
  1230	develops HT field theory from the gauge-theoretic side. The
  1231	relationship with this monograph has three layers.
  1232	
  1233	\emph{Structural identification.}
  1234	The $\Eone$-chiral coassociative structure on the bar complex
  1235	$B(\cA_T)$
  1236	(Theorem~\ref{thm:bar-swiss-cheese}: deconcatenation coproduct
  1237	in the $\bR$-direction, factorization product in
  1238	the $\bC$-direction) is the algebraic skeleton of the HT
  1239	twist on $\bC \times \bR$. The $\bC$-direction encodes the
  1240	chiral algebra; the $\bR$-direction encodes the topological
  1241	coproduct. The $\mathrm{SC}^{\mathrm{ch,top}}$ structure emerges on the
  1242	derived center pair $(C^\bullet_{\mathrm{ch}}(\cA_T,\cA_T),\,\cA_T)$;
 succeeded in 52ms:
    55	The first equation is the bar nilpotence of~$\cA$ on~$X$. The second
    56	is the coassociativity of the bar coproduct. The third is the
    57	compatibility of the OPE with the ordered product.
    58	
    59	\begin{definition}[$\Eone$-chiral coassociative structure on the bar complex]
    60	\label{def:thqg-intro-swiss-cheese-structure}
    61	\index{bar complex!$\Eone$ coassociative coalgebra}
    62	The \emph{$\Eone$-chiral coassociative structure} on $\barB_X(\cA)$ is the
    63	pair $(d_C, d_R)$ satisfying~\eqref{eq:thqg-intro-swiss-cheese-squares}.
    64	The differential $d_C$ is $\Einf$-chiral (factorization on~$X$);
    65	the coproduct $d_R$ is $\Eone$-topological (deconcatenation on
    66	ordered configurations of~$\mathbb{R}$)
    67	(Theorem~\ref{thm:bar-swiss-cheese}).
    68	The $\mathrm{SC}^{\mathrm{ch,top}}$ two-colour datum emerges not on
    69	$\barB_X(\cA)$ itself but on the derived center pair
    70	$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$; see Volume~II\@.
    71	\end{definition}
    72	
    73	The two-component decomposition is the geometric origin of the
    74	bulk-boundary-line triangle. The holomorphic direction produces the bulk:
 succeeded in 51ms:
    20	$C^\bullet_{\mathrm{ch}}(\cA,\cA)$ computes the universal
    21	bulk; bar-cobar inversion $\Omega(B(\cA)) \simeq \cA$
    22	recovers the boundary algebra itself. The modular
    23	convolution algebra~$\gAmod$
    24	(Definition~\ref{def:modular-convolution-dg-lie}) organizes the full boundary-to-bulk correspondence
    25	at all genera. The $\mathrm{SC}^{\mathrm{ch,top}}$ operad, descent
    26	calculus, and recognition theorem are developed in Volume~II\@. The bar complex of
    27	this volume, equipped with its $\Eone$-chiral coassociative coproduct
    28	(Theorem~\ref{thm:bar-swiss-cheese}), provides the algebraic input.
    29	
    30	\section{The HT twist and shadow data}
    31	\label{sec:ht-shadow-data}
    32	\index{holomorphic-topological theory!shadow data}
    33	
    34	\begin{construction}[Shadow data from the holomorphic-topological twist]
    35	\label{constr:ht-shadow-data}
    36	\index{shadow data!holomorphic-topological}
    37	The holomorphic-topological twist of a $4$d $\mathcal{N} \geq 1$
    38	theory~$T$ produces a chiral algebra~$\cA_T$ on~$\mathbb{C}$ with:
    39	\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "nl -ba chapters/connections/bar-cobar-review.tex | sed -n '1320,1345p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/bar-cobar-review.tex | sed -n '1908,1922p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/bar-cobar-review.tex | sed -n '4088,4098p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '1,35p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/foundations.tex | sed -n '1878,1900p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '1788,1803p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
  1320	\end{remark}
  1321	
  1322	\subsection{The $E_1$ coalgebra structure on the bar complex}
  1323	\label{subsec:bar-swiss-cheese}
  1324	
  1325	The chiral bar complex $\barB_{\mathrm{ch}}(\cA)$ carries two structures: the bar differential $d_{\barB}$ (from the holomorphic direction) and the deconcatenation coproduct $\Delta$ (from the topological direction). Together they make $\barB(\cA)$ an $E_1$ dg coassociative coalgebra: the differential is a coderivation of the coproduct. The $\SCchtop$ structure does not live on $\barB(\cA)$ itself; it emerges in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, where the bulk $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ acts on the boundary~$\cA$ (Section~\ref{sec:derived-center}).
  1326	
  1327	\begin{theorem}[$E_1$ dg coalgebra structure on the bar complex;
  1328	\ClaimStatusProvedHere]
  1329	\label{thm:bar-swiss-cheese}
  1330	Let $\cA$ be a chiral algebra on a smooth algebraic curve~$X$.
  1331	The geometric bar complex $\barB_X(\cA)$ of Volume~I, equipped
  1332	with:
  1333	\begin{enumerate}[label=\textup{(\roman*)}]
  1334	\item the bar differential $d_{\barB}$ (residues along collision
  1335	 divisors in $\FM_k(X)$), encoding the $A_\infty$ chiral
  1336	 structure;
  1337	\item the deconcatenation coproduct
  1338	 $\Delta[a_1|\cdots|a_n]
  1339	 = \sum_{i=0}^{n}
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '24,40p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '262,275p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/holomorphic_topological.tex | sed -n '108,140p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  1908	 holomorphic and topological directions of $\C_z \times \R_t$.
  1909	\end{enumerate}
  1910	\end{theorem}
  1911	
  1912	\begin{proof}
  1913	Part~(i) combines Theorem~\ref{thm:bar-swiss-cheese} (the bar complex
  1914	is an $E_1$ dg coassociative coalgebra) with the Quillen equivalence of
  1915	Theorem~\ref{thm:bar-cobar-adjunction}, unconditional by
  1916	homotopy-Koszulity (Theorem~\ref{thm:homotopy-Koszul}).
  1917	
  1918	Part~(ii): since $\barB(\cA)$ is an $E_1$ dg coassociative coalgebra
  1919	(Theorem~\ref{thm:bar-swiss-cheese}), the Quillen equivalence gives
  1920	$\barB(\cA)\text{-}\mathbf{comod}^{E_1}
  1921	\simeq \cA\text{-}\mathbf{mod}^{\mathrm{open}}$,
  1922	where the right-hand side is the open-colour module category of $\cA$
exec
/bin/zsh -lc "nl -ba chapters/theory/raviolo.tex | sed -n '356,366p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '223,235p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ht_bulk_boundary_line.tex | sed -n '1382,1395p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2126,2136p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '5140,5152p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  4088	Scalar trace $\pi_{\mathrm{sc}}$ & D (Modular char.) & $\kappa(\cA)$ universal, additive, $\hat{A}$-genus \\
  4089	Hochschild $\pi_{\mathrm{HH}}$ & H (Hochschild, generic level) & $\mathrm{ChirHoch}^*(\cA)$ polynomial \\
  4090	\bottomrule
  4091	\end{tabular}
  4092	\end{center}
  4093	The $E_1$ dg coalgebra structure of $\barB(\cA)$ (Theorem~\ref{thm:bar-swiss-cheese}) encodes both directions: the deconcatenation coproduct encodes the $\mathbb{R}$-direction (topological factorization), while the bar differential encodes the $\mathbb{C}$-direction (holomorphic collisions). The $\SCchtop$ structure emerges in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$ (Part~\ref{part:swiss-cheese} of this volume).
  4094	\end{construction}
  4095	
  4096	\begin{remark}[Transition to line operators]
  4097	\label{rem:transition-to-line-operators}
  4098	Line operators are modules for the open-colour Koszul dual. The mechanism:
 succeeded in 51ms:
     1	%% Factorization Swiss-Cheese: the primary treatment
     2	%% Layers 0--5 of the six-layer hierarchy
     3	
     4	%% Macro safety: providecommand only
     5	\providecommand{\fSet}{\mathsf{fSet}}
     6	\providecommand{\IndCoh}{\operatorname{IndCoh}}
     7	\providecommand{\QCoh}{\operatorname{QCoh}}
     8	\providecommand{\Dmod}{D\text{-}\mathsf{mod}}
     9	\providecommand{\Mbar}{\overline{\cM}}
    10	\providecommand{\colim}{\operatorname{colim}}
    11	\providecommand{\varprojlim}{\underleftarrow{\lim}}
    12	\providecommand{\Obs}{\mathsf{Obs}}
    13	\providecommand{\id}{\mathrm{id}}
    14	\providecommand{\cG}{\mathcal{G}}
    15	\providecommand{\cB}{\mathcal{B}}
    16	
    17	\chapter{Factorization Swiss-Cheese Algebras}
    18	\label{ch:factorization-swiss-cheese}
    19	
    20	\begin{remark}[Structural warning: the bar complex is not an $\SC^{\ch,\top}$-coalgebra]
 succeeded in 50ms:
  1788	restrict to the boundary strata of $\Conf_m^<(\R)$ and
  1789	$\FM_k(\C)$ respectively.
  1790	\end{proof}
  1791	
  1792	\begin{remark}[The half-plane model as $\SCchtop$-coalgebra
  1793	datum]
  1794	\label{rem:half-plane-sc-datum}
  1795	\index{Swiss-cheese!half-plane bar chain model}%
  1796	The half-plane bar complex $\barB^{\mathbb{H}}(\cA)$ is a genus-$0$
  1797	object: the configuration space $\FM_k(\C)$ is
  1798	on~$\C \simeq \mathbb{P}^1 \setminus \{\infty\}$, not
  1799	on a higher-genus surface, and the differential uses the
  1800	rational propagator $K^{(0)} = dz/(z-w)$.
  1801	Genus dependence enters via the closed-sector curvature
  1802	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$
  1803	(Construction~\ref{constr:bar-fact-coalgebra}(iv)), which
 succeeded in 50ms:
  1878	desuspension $s^{-1}$.
  1879	\end{remark}
  1880	
  1881	The central claim of this volume: \emph{the bar complex of
  1882	Volume~I, equipped with its coproduct, is an $E_1$ chiral
  1883	coassociative coalgebra; the $\SCchtop$ structure emerges in the
  1884	chiral derived center pair
  1885	$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$.} The bar differential is holomorphic
  1886	factorization; the bar coproduct is topological factorization; the
  1887	no-open-to-closed rule is the physical directionality that bulk
  1888	interactions restrict to boundaries but not conversely. By operadic Koszul self-duality
  1889	(\S\ref{subsec:dg-yangian-operadic}), on the chirally Koszul locus
  1890	the open-colour Koszul dual $\cA^!_{\mathrm{line}}$ inherits an
  1891	${\SCchtop}^{!}$-algebra structure (closed $=$ Lie, open $=$ Ass)
  1892	\textup{(}Theorem~\textup{\ref{thm:dual-sc-algebra}}\textup{)}
  1893	and hence a dg-shifted Yangian package
  1894	\textup{(}Theorem~\textup{\ref{thm:yangian-recognition}}\textup{)}.
  1895	
  1896	A deeper fact (Volume~I,
  1897	Theorem~\ref*{thm:bar-swiss-cheese} of
 succeeded in 51ms:
   262	an $E_1$ chiral coassociative coalgebra
   263	(Theorem~\ref{thm:rosetta-swiss-cheese} for the Heisenberg;
   264	Section~\ref{sec:foundations} in general).
   265	The two-coloured configuration spaces
   266	$\FM_k(\C) \times \Conf_k^<(\R)$ parametrise the bar element at
   267	degree~$k$: the differential sees~$\FM_k(\C)$, the coproduct
   268	sees~$\Conf_k^<(\R)$. The resulting dg coalgebra $\barB(\cA)$ is
   269	an $E_1$ chiral coassociative coalgebra; the $\SCchtop$ structure
   270	lives not on~$\barB(\cA)$ itself but on the chiral derived center
   271	pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, where chiral
   272	Hochschild cochains (defined via~$\End^{\mathrm{ch}}_\cA$) act on
   273	the boundary algebra via brace operations. The bar-cobar Quillen
   274	equivalence
   275	$\Omega^{\mathrm{ch}}(\barB(\cA)) \xrightarrow{\sim} \cA$
 succeeded in 52ms:
    24	tower classifies the nonlinear complexity of the gravitational
    25	dynamics, and whose five structural properties are the five main
    26	theorems. This volume identifies the architecture of that
    27	construction: the primitive object is an open factorization
    28	dg-category on the gravitational boundary; bulk observables are its
    29	chiral derived center; line operators are modules over the Koszul
    30	dual; modularity is trace plus clutching on the boundary category.
    31	Replacing Virasoro by~$\mathcal{W}_N$ gives higher-spin gravity;
    32	replacing it by affine Kac--Moody gives gauge theory. The
    33	MC element, bar complex, and Swiss-cheese structure exist
    34	uniformly for all families.
    35	
    36	The mechanism is the holomorphic-topological decomposition of
    37	spacetime itself. A three-dimensional theory on
    38	$\C_z \times \R_t$ presents two factorization structures:
    39	holomorphic collisions in the $\C$-plane produce the bar
    40	differential; topological splittings along $\R$ produce the
 succeeded in 52ms:
   108	
   109	\begin{proposition}[Bar complex and genus-zero HT data; \ClaimStatusProvedHere]
   110	\label{prop:ht-bar-genus-zero}
   111	Let $T$ be a $4$d $\mathcal{N}=2$ theory with HT boundary chiral
   112	algebra~$\cA_T$. The bar complex $B(\cA_T)$ carries:
   113	\begin{enumerate}[label=\textup{(\roman*)}]
   114	\item a coassociative coproduct
   115	 \textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}
   116	 encoding the topological-direction factorization;
   117	\item a differential $d_B$ whose cohomology is the Koszul dual
   118	 coalgebra; the Verdier dual
   119	 $\mathbb{D}_{\Ran}\,B(\cA_T) \simeq B(\cA_T^!)$
   120	 recovers the homotopy Koszul dual algebra $(\cA_T^!)_\infty$
   121	 \textup{(}Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}},
   122	 Convention~\textup{\ref{conv:bar-coalgebra-identity}}\textup{)};
   123	\item a modular operad algebra structure over the Feynman transform of
   124	 the commutative modular operad~$\mathrm{FCom}$
   125	 \textup{(}Theorem~\textup{\ref{thm:bar-modular-operad}}\textup{)},
   126	 with $\partial^2 = 0$ at all genera a formal consequence.
   127	\end{enumerate}
 succeeded in 50ms:
  1382	 and the shadow obstruction tower
  1383	 \textup{(}Proposition~\textup{\ref{prop:alpha-projections}(v)}\textup{)}.
  1384	\end{enumerate}
  1385	\end{theorem}
  1386	
  1387	\begin{proof}
  1388	The theorem assembles five proved results into a single package.
  1389	Statement~(i) is Theorem~\ref{thm:bar-swiss-cheese} (the bar
  1390	complex is an $E_1$ dg coassociative coalgebra) together with
  1391	Theorem~\ref{thm:homotopy-Koszul} (homotopy-Koszulity ensures
  1392	the bar-cobar resolution recovers the operad).
  1393	Statement~(ii) combines
  1394	Proposition~\ref{prop:alpha-projections}(ii) (the open projection
  1395	gives the line-sector operations) with
 succeeded in 50ms:
   223	\begin{proof}
   224	The theorem assembles six proved results into a single package.
   225	Statement~(i) is Theorem~A (the bar-cobar adjunction), which
   226	gives $\barB(\cA)$ the structure of an $E_1$ dg coassociative
   227	coalgebra with differential $d_{\barB}$ and deconcatenation
   228	coproduct~$\Delta$.
   229	Statement~(ii) is Theorem~\ref{thm:bar-swiss-cheese} (the
   230	$\SCchop$-datum on the pair
   231	$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$) together with
   232	Theorem~\ref{thm:homotopy-Koszul} (homotopy transfer from the
   233	MC element).
   234	Statement~(iii) combines
   235	Proposition~\ref{prop:alpha-projections}(ii) (the open projection
 succeeded in 51ms:
   356	The bulk–to–boundary map (Section~\ref{sec:bulk-boundary}) intertwines the bulk PVA with the boundary VOA.
   357	
   358	\subsection{The essential principle}
   359	\label{sec:bridge-principle}
   360	
   361	The bar complex $\barB^{\mathrm{ch}}(\cA) = T^c(s^{-1}\bar\cA)$ carries a differential $d_{\barB}$ from OPE residues on $\FM_k(\C)$ and a coproduct~$\Delta$ from deconcatenation on $\Conf_k(\R)$. A bar element of degree~$k$ is parametrised by $\FM_k(\C) \times \Conf_k(\R)$, the operation spaces of~$\SCchtop$ (Definition~\ref{def:SC-colors}).
   362	
   363	\begin{definition}[Logarithmic $\SCchtop$-algebra]
   364	\label{def:log-SC-algebra}
   365	A \emph{logarithmic $\SCchtop$-algebra} is a $C_\ast(W(\SCchtop))$-algebra $(\cA_{\mathrm{ch}}, \cA_{\mathrm{top}})$ whose closed-colour $A_\infty$ operations $\{m_k\}_{k \ge 1}$ are defined by weight forms
   366	\[
 succeeded in 50ms:
  2126	$\Ainf$ relations are Stokes' theorem on boundary strata of
  2127	$\FM_k(\C)$, with explicit formulas for~$m_2$ and~$m_3$
  2128	(Propositions~\ref{prop:m2_formula} and~\ref{prop:m3_formula}).
  2129	The BV-BRST construction
  2130	(Section~\ref{sec:BV_construction}) shows that BV quantisation of
  2131	a 3d HT field theory on $\C \times \R$ produces exactly these
  2132	bar complexes (Theorem~\ref{thm:Obs-is-SC}).
  2133	Two descent mechanisms then extract invariants from the bar complex.
  2134	Cohomological descent produces the $(-1)$-shifted PVA on
  2135	cohomology (Theorem~\ref{thm:cohomology_PVA}), with the
  2136	regular/singular decomposition of~$m_2$ yielding the product and
 succeeded in 50ms:
  5140	$\Eone$-chiral algebras, as required by
  5141	Conjecture~\ref{conj:modular-operad-ainf-chiral}(i).
  5142	
  5143	The half-plane bar complex
  5144	$\barB^{\mathbb{H}}(\cA)$
  5145	(Construction~\ref{constr:half-plane-bar}) is the
  5146	$\SCchtop$ bar coalgebra. The transverse bar complex is
  5147	the standard $\Eone$-bar of $\barB^{\mathbb{H}}(\cA)$,
  5148	taken in the transverse direction: at the cochain level
  5149	it produces the Hochschild complex of the boundary, and
  5150	$\Zder^{\mathrm{ch}}(\cA)$ inherits the $\Ethree$-chiral
  5151	structure of Definition~\ref{def:E3-chiral-algebra}.
  5152	\end{remark}



thinking
**Evaluating potential violations**

I'm finding that line 5146 in 3d_gravity might have a direct violation. It mentions "The half-plane bar complex..." and I need to analyze whether it should refer to the "bar coalgebra of the SC operad" or the operadic bar of SC. There seems to be a discrepancy regarding the half-plane bar complex, suggesting it could be a significant issue. I should look further into lines 5130-5152 for context, especially if it’s part of a remark. Depending on its implications, I might classify it as CRITICAL.
thinking
**Analyzing parameterization of bar elements**

The text mentions bar elements being parametrized by the operation spaces of SCchtop, but it doesn't directly state that the bar complex is the SC coalgebra. The operation spaces are a product of FM_k(C) × Conf_k(R), which raises some conceptual issues. While AP165 clarifies that the SC structure isn't on the bar complex itself, it could still be misleading, possibly classifying this as a low concern. I should check further context to assess the surrounding definitions, hinting at potential inaccuracies. I’ll inspect the relevant files for corrections.
thinking
**Reviewing the lines for accuracy**

I’m checking the lines and finding that `ht_bulk_boundary_line_frontier` on line 229 references Theoremref{thm:bar-swiss-cheese} correctly, so that’s good—it has no violation. Also, it looks like `ht_bulk_boundary_line` on line 1389 has been corrected as well. So overall, this seems to be a false positive. I can confidently say that everything checks out here. Nice to see things falling into place!
exec
/bin/zsh -lc "nl -ba chapters/theory/braided_factorization.tex | sed -n '255,266p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/modular_koszul_bridge.tex | sed -n '1,12p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '10,18p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/cy_to_chiral.tex | sed -n '1824,1834p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
  1824	
  1825	\subsection{$\Eone$-chiral coalgebra and the derived center}
  1826	\label{subsec:cross-vol-sc}
  1827	
  1828	% AP165: SC^{ch,top} lives on the derived center pair, NOT on B(A).
  1829	The bar complex $B(A)$ is an $\Eone$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$; the $\SC^{\mathrm{ch,top}}$ two-colour structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on the bar complex itself. Three bar constructions reflect three levels of operadic symmetry:
  1830	\begin{itemize}
  1831	 \item $B_{\Eone}(A)$: ordered tensors, deconcatenation coproduct ($\Eone$ coalgebra).
  1832	 \item $B_{\Etwo}(A)$: braided tensors, with $R$-matrix data ($\Etwo$ coalgebra via Drinfeld center).
  1833	 \item $B_{\Einf}(A)$: symmetric tensors, Vol~I shadow tower ($\Einf$ coalgebra).
  1834	\end{itemize}
 succeeded in 52ms:
    10	\]
    11	on its Hochschild homology, encoding the CY condition as a $d$-dimensional Frobenius structure at the chain level. The cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ is the primary invariant; it carries an $\Sd$-action from the $d$-sphere framing of the trace, and its $\Sd$-equivariant structure governs higher-genus amplitudes.
    12	
    13	A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
    14	
    15	That these two structures admit a common description is not a coincidence but the central fact of the theory. Both the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ and the chiral bar complex $B(A)$ are instances of the same homotopical object: a cyclic $\Ainf$-coalgebra equipped with a compatible trace. The cyclic $\Ainf$-condition on the CY side (the non-degenerate pairing $\Tr$ satisfying the higher homotopy Frobenius relations) and the Maurer--Cartan equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ on the chiral side are two presentations of one structure. Homological algebra supplies the universal language in which CY geometry and chiral algebra are the same sentence written in different alphabets; the functor $\Phi$ is the translation. Its existence is forced: any construction that respects the cyclic $\Ainf$-structure on both sides must factor through it.
    16	
    17	This work constructs a bridge:
    18	\begin{center}
 succeeded in 52ms:
     1	\chapter{Modular Koszul Duality and CY Geometry}
     2	\label{ch:modular-koszul-bridge}
     3	
     4	A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
     5	
     6	
     7	%% ===================================================================
     8	%% SECTION 1: CY modular convolution algebra
     9	%% ===================================================================
    10	
    11	\section{The modular convolution algebra for CY categories}
    12	\label{sec:modular-conv-cy}
 succeeded in 52ms:
   255	differential satisfies $d_{\mathrm{fib}}^2 = \kappa_{\mathrm{cat}} \cdot \omega_g$
   256	(Hodge curvature; see Theorem~\ref{thm:e2-bar-cobar}(iii)).
   257	\end{definition}
   258	
   259	\begin{remark}[$B_{E_2}(\cA)$ is not a Swiss-cheese coalgebra]
   260	\label{rem:e2-bar-not-sc}
   261	The $\Etwo$-bar complex $B_{E_2}(\cA)$ is an $\Etwo$-coalgebra, \emph{not}
   262	a Swiss-cheese ($\SC^{\mathrm{ch,top}}$) coalgebra. The SC structure of
   263	Vol~II is two-coloured (holomorphic + topological) and emerges on the
   264	\emph{derived center} $\Zder(\cA) = C^\bullet_{\mathrm{ch}}(\cA, \cA)$
   265	(the bulk algebra), not on the bar complex of $\cA$ itself. The bar
   266	complex encodes the boundary; the SC structure governs the bulk-boundary
codex
Volume III is clean on this surface so far: the visible hits explicitly negate the forbidden claim. I’m doing one more targeted pass in Volume I and II for stale positive phrasings like `is the SC... bar coalgebra` or theorem titles that still encode the old claim.
exec
/bin/zsh -lc "rg -n -i 'Swiss-cheese coalgebra|SC["'^'"\\n]{0,40}bar coalgebra|bar coalgebra["'^'"\\n]{0,40}SC|is an? \\\\SC|is the \\\\SC|bar complex as Swiss|bar complex.*not an \\\\SC' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -i 'Swiss-cheese coalgebra|SC["'^'"\\n]{0,40}bar coalgebra|bar coalgebra["'^'"\\n]{0,40}SC|is an? \\\\SC|is the \\\\SC|bar complex as Swiss|bar complex.*not an \\\\SC' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -i 'Swiss-cheese coalgebra|SC["'^'"\\n]{0,40}bar coalgebra|bar coalgebra["'^'"\\n]{0,40}SC|is an? \\\\SC|is the \\\\SC|bar complex as Swiss|bar complex.*not an \\\\SC' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/braided_factorization.tex:259:\begin{remark}[$B_{E_2}(\cA)$ is not a Swiss-cheese coalgebra]
 succeeded in 52ms:
chapters/theory/axioms.tex:1125:$\Omega$ recovers the SC-algebra from the bar coalgebra, and the
chapters/connections/3d_gravity.tex:5146:$\SCchtop$ bar coalgebra. The transverse bar complex is
chapters/connections/relative_feynman_transform.tex:1322:bar coalgebra of~$\SCchtop$. The differential $D_0|_{\gr^0}$
chapters/connections/relative_feynman_transform.tex:3292:\item \textbf{Local} \textup{(}Operadic, Chapter~\textup{\ref{ch:modular-sc-operad})}: the modular bar coalgebra $\barB_{\mathrm{op}}(\cA) = \Bmod(\cA)$ with flat bicomplex $(D_0, D_1)$ and $D^2 = 0$.
 succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:21:bar coalgebra structure, screening operators, and Toda field theory.
chapters/theory/introduction.tex:2645:$\cA$ is the algebra. $\barB(\cA)$ is the bar coalgebra. $\cA^{\scriptstyle \text{\normalfont !`}} = H^*(\barB(\cA))$ is the Koszul dual coalgebra. $\cA^! = (\cA^{\scriptstyle \text{\normalfont !`}})^\vee$ is the Koszul dual algebra. The cobar $\Omega(\barB(\cA))$ recovers~$\cA$ (bar-cobar \emph{inversion}, not duality); $\cA^!$ is obtained by Verdier/linear duality, not cobar.

thinking
**Inspecting algebra axioms**

I need to look into Volume II axioms 1124-1125. They might explain how the SC-algebra is recovered from bar coalgebra, which could relate to operadic concepts. I also think relative Feynman transforms may use the operadic bar coalgebra of the SC operad. It's important to double-check the 3D gravity candidate too, as there could be a structural issue at play. I'll need to inspect those axioms carefully to classify everything correctly.
exec
/bin/zsh -lc "nl -ba chapters/theory/axioms.tex | sed -n '1118,1128p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/relative_feynman_transform.tex | sed -n '1318,1326p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/relative_feynman_transform.tex | sed -n '3288,3295p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  1118	complex $\barB$ passes to the self-intersection groupoid
  1119	$\mathfrak{S}_b = \mathcal{L}\times_{\mathcal{M}}^h\mathcal{L}$;
  1120	and the cobar functor $\Omega$ recovers the
  1121	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra from the groupoid. The
  1122	Quillen equivalence states that the $A_\infty$ axioms and the
  1123	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra structure determine each
  1124	other: $\barB$ passes from the SC-algebra to the $A_\infty$ data,
  1125	$\Omega$ recovers the SC-algebra from the bar coalgebra, and the
  1126	two operations are inverse on the homotopy category. In the
  1127	Lagrangian interpretation, this is the skeleton theorem: the
  1128	self-intersection data (groupoid) determines the correspondence
 succeeded in 51ms:
  1318	\smallskip\noindent
  1319	\emph{Step 2: the open-color structure.}
  1320	At genus~$0$, $\gr_F^0 \Bmod(C) = \Bch(C)$
  1321	(Theorem~\ref{thm:genus-completion}(i)), which is the tree-level
  1322	bar coalgebra of~$\SCchtop$. The differential $D_0|_{\gr^0}$
  1323	is the tree-level bar differential, making $\Bch(C)$ a
  1324	conilpotent dg coalgebra over $B(\SCchtop)$. Since $\SCchtop$
  1325	is homotopy-Koszul (Theorem~\ref{thm:homotopy-Koszul}), the
  1326	inclusion ${\SCchtop}^{!} \hookrightarrow
 succeeded in 51ms:
  3288	\label{thm:three-routes-equivalence}
  3289	Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra with modular characteristic~$\kappa(\cA)$. The global/factorization and local/operadic constructions produce bar-complex models that are connected by the relative Feynman transform; the local flat model carries ordinary derived invariants, and the global curved model is its coderived counterpart at every genus~$g \ge 0$:
  3290	\begin{enumerate}[label=\textup{(\roman*)}]
  3291	\item \textbf{Global} \textup{(}Factorization, Chapter~\textup{\ref{ch:factorization-swiss-cheese})}: the factorization coalgebra $\barB_{\mathrm{fact}}(\cA)$ on $\operatorname{Ran}(\Sigma_g) \times \operatorname{Ran}(\R)$, with fiberwise differential~$\dfib$ satisfying $\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$.
  3292	\item \textbf{Local} \textup{(}Operadic, Chapter~\textup{\ref{ch:modular-sc-operad})}: the modular bar coalgebra $\barB_{\mathrm{op}}(\cA) = \Bmod(\cA)$ with flat bicomplex $(D_0, D_1)$ and $D^2 = 0$.
  3293	\end{enumerate}
  3294	The relative Feynman transform $\FTrel$ \textup{(}this chapter\textup{)} provides the algebraic skeleton that mediates between them: $\barB_{\mathrm{op}}(\cA) \cong \FTrel(\cA)$ as bigraded complexes.
  3295	
exec
/bin/zsh -lc "rg -n -i 'bar complex["'^.]{0,120}(carries|is|as)[''^.]{0,80}SC|B'"\\(A\\)["'^.]{0,120}(carries|is|as)[''^.]{0,80}SC|bar complex[''^.]{0,120}Swiss-cheese|B'"\\(A\\)["'^.]{0,120}Swiss-cheese'"' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -i 'bar complex["'^.]{0,120}(carries|is|as)[''^.]{0,80}SC|B'"\\(A\\)["'^.]{0,120}(carries|is|as)[''^.]{0,80}SC|bar complex[''^.]{0,120}Swiss-cheese|B'"\\(A\\)["'^.]{0,120}Swiss-cheese'"' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -i 'bar complex["'^.]{0,120}(carries|is|as)[''^.]{0,80}SC|B'"\\(A\\)["'^.]{0,120}(carries|is|as)[''^.]{0,80}SC|bar complex[''^.]{0,120}Swiss-cheese|B'"\\(A\\)["'^.]{0,120}Swiss-cheese'"' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bar_cobar_bridge.tex:262:The banana manifold is the prototypical example : $\kappa_{\mathrm{ch}} = 0$ does \emph{not} imply $\Theta_A = 0$. The vanishing of $\kappa_{\mathrm{ch}}$ means the bar complex is uncurved ($d^2 = 0$ at the leading scalar level), but the higher-degree components of $\Theta_A$ (the quartic shadow $Q$ and beyond) are nonvanishing, sourced by the instanton contributions (genus-$0$ GV invariants of the banana curves).
chapters/theory/hochschild_calculus.tex:23:This chapter develops the Hochschild calculus underlying the CY-to-chiral functor of Chapter~\ref{ch:cy-to-chiral}. The shifted Poisson structure on $\HH^\bullet(\cC)$ is the categorical precursor of the convolution Lie bracket on the modular deformation complex of Volume~I: the Gerstenhaber bracket becomes the bar-cobar convolution bracket, the Connes $B$-operator becomes the modular differential, and the Serre pairing becomes the cyclic duality that controls the $\bS^d$-framing. The cyclic bar complex of Chapter~\ref{ch:cyclic-ainf} is the single-object specialization of the Hochschild complex constructed here.
chapters/theory/e1_chiral_algebras.tex:142:Let $\cC$ be a CY$_2$ category with cyclic $A_\infty$ structure and negative-cyclic trace. The ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries a natural $E_1$-chiral structure whose holomorphic direction matches the Hochschild differential and whose ordered direction matches the cyclic action on the bar coalgebra.
chapters/theory/quantum_chiral_algebras.tex:476:At $n = 2$: affine Yangian $\to$ bar complex $\to$ dual Yangian $\to$ quantum group braiding (PARTIALLY ESTABLISHED, via Schiffmann--Vasserot / Maulik--Okounkov).
chapters/theory/cy_to_chiral.tex:1829:The bar complex $B(A)$ is an $\Eone$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$; the $\SC^{\mathrm{ch,top}}$ two-colour structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on the bar complex itself. Three bar constructions reflect three levels of operadic symmetry:
 succeeded in 51ms:
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:210:scalar class vanishes and the bar complex is uncurved on the scalar
chapters/connections/log_ht_monodromy_core.tex:2046:The bar complex of $V^k(\mathfrak{sl}_2)$, viewed as a logarithmic $\SCchtop$-algebra, produces a flat connection on configuration spaces by Theorem~\ref{thm:synthesis}. By Theorem~\ref{thm:affine-monodromy-identification}(i)--(ii), on the reduced evaluation comparison surface the monodromy of this connection identifies with the KZ monodromy, and the affine Drinfeld--Kohno theorem compares it with the corresponding braided tensor-product representation of $\mathrm{Rep}_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$. In particular, the bar complex computes the braid-group representation
chapters/theory/foundations.tex:200:\index{three bar complexes!Swiss-cheese decomposition}
chapters/theory/foundations.tex:1350:\index{three bar complexes!Swiss-cheese provenance}%
chapters/theory/introduction.tex:33:MC element, bar complex, and Swiss-cheese structure exist
chapters/theory/introduction.tex:2132:bar complexes (Theorem~\ref{thm:Obs-is-SC}).
chapters/theory/factorization_swiss_cheese.tex:20:\begin{remark}[Structural warning: the bar complex is not an $\SC^{\ch,\top}$-coalgebra]
chapters/theory/factorization_swiss_cheese.tex:1024:\index{ordered bar complex!Swiss-cheese provenance}
 succeeded in 51ms:
chapters/examples/kac_moody.tex:1800:At critical level $k = -h^\vee$, the bar complex differential is determined by the screening charges:
chapters/frame/preface.tex:3741:bar complex is fed into the Hochschild construction.
chapters/theory/chiral_hochschild_koszul.tex:1983:cyclic coderivations of the bar complex, which is the Hochschild
chapters/theory/introduction.tex:26:is always a dg algebra morphism. When it is a quasi-isomorphism, $A$ is \emph{Koszul}: the bar cohomology concentrates in degree~$1$, the Koszul dual coalgebra is $A^{\scriptstyle \text{\normalfont !`}} = H^1(B(A))$, and the Koszul dual algebra is $A^! = (A^{\scriptstyle \text{\normalfont !`}})^\vee = T(V^*)/R^\perp$. The derived categories of $A$-modules and $A^!$-modules become equivalent (Priddy~\cite{Priddy70}, Beilinson--Ginzburg--Soergel~\cite{BGS96}, Loday--Vallette~\cite{LV12}). The theory is complete: $\Omega(B(A)) \simeq A$ is bar-cobar \emph{inversion}, and nothing beyond this equivalence remains.
chapters/theory/introduction.tex:2204: Higher-dimensional bar complexes; Totaro relations; Ayala--Francis; topologization $\mathsf{SC}^{\mathrm{ch,top}} + T_{\mathrm{Sug}} \Rightarrow \Ethree$ (Thm~\ref{thm:topologization}, proved for affine KM; Conj~\ref{conj:topologization-general}, general) \\[6pt]
chapters/theory/configuration_spaces.tex:3020:The FM compactification $\overline{C}_n(\mathbb{P}^1)$ (without the $\mathrm{PSL}_2$ quotient) is a higher-dimensional space: $\dim_{\mathbb{C}} C_n(\mathbb{P}^1) = n$, and $\dim_{\mathbb{C}} \overline{M}_{0,n+1} = n - 2$. The bar complex uses the automorphism-free configuration space $C_n(X)$ for curves $X$ of genus~$g \geq 1$, where $\mathrm{Aut}(X)$ is discrete.
chapters/theory/ordered_associative_chiral_kd.tex:517:Then the unordered bar complex is the $R$-twisted $\Sigma_n$-descent:
chapters/theory/nilpotent_completion.tex:55:The bar complex $\bar{B}(\mathcal{A})$ carries the $I$-adic (descending) filtration:
chapters/theory/en_koszul_duality.tex:1251:\index{bar complex!is E1 coassociative, NOT SC}

thinking
**Inspecting structure and context**

I'm looking into the search results, but I don't see other positives surface. It seems like there could be just one clear violation combined with a structural label. I might need to check the introduction in Volume II, particularly line 33, to see if it fits a medium or something else. Let me look for additional context and consider examining the Swiss-cheese structure separately to understand better.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '28,36p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
    28	dg-category on the gravitational boundary; bulk observables are its
    29	chiral derived center; line operators are modules over the Koszul
    30	dual; modularity is trace plus clutching on the boundary category.
    31	Replacing Virasoro by~$\mathcal{W}_N$ gives higher-spin gravity;
    32	replacing it by affine Kac--Moody gives gauge theory. The
    33	MC element, bar complex, and Swiss-cheese structure exist
    34	uniformly for all families.
    35	
    36	The mechanism is the holomorphic-topological decomposition of

thinking
**Evaluating structural concerns**

I'm noticing this is a separate issue rather than a related one. It might be fine if a Swiss-cheese structure exists uniformly on the derived center pair. There's no specific relation to the bar complex, so maybe I should skip that for now. I need to examine the 3D gravity context more closely to fully grasp the remark's severity and how it ties into the previous sentences.
exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '5128,5154p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  5128	 $C_\ast(\FM_k(\C) \times \Eone(m) \times \Eone(p))
  5129	 \otimes A_{\mathsf{ch}}^{\otimes k} \otimes
  5130	 A_{\mathsf{bdy}}^{\otimes m} \otimes
  5131	 A_{\mathsf{tr}}^{\otimes p} \to A_{\mathsf{tr}}$:
  5132	 the transverse operations, combining holomorphic, boundary,
  5133	 and transverse data.
  5134	\end{enumerate}
  5135	By the product decomposition~\eqref{eq:genus0-product},
  5136	this is equivalent to an $\Ainf$-algebra
  5137	$(A_{\mathsf{tr}},\, \{m_p^{\mathsf{tr}}\}_{p \ge 1})$
  5138	whose underlying object carries an $\SCchtop$-algebra
  5139	structure---that is, an $\Ainf$-algebra in
  5140	$\Eone$-chiral algebras, as required by
  5141	Conjecture~\ref{conj:modular-operad-ainf-chiral}(i).
  5142	
  5143	The half-plane bar complex
  5144	$\barB^{\mathbb{H}}(\cA)$
  5145	(Construction~\ref{constr:half-plane-bar}) is the
  5146	$\SCchtop$ bar coalgebra. The transverse bar complex is
  5147	the standard $\Eone$-bar of $\barB^{\mathbb{H}}(\cA)$,
exec
/bin/zsh -lc "nl -ba chapters/theory/factorization_swiss_cheese.tex | sed -n '1792,1812p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  1792	\begin{remark}[The half-plane model as $\SCchtop$-coalgebra
  1793	datum]
  1794	\label{rem:half-plane-sc-datum}
  1795	\index{Swiss-cheese!half-plane bar chain model}%
  1796	The half-plane bar complex $\barB^{\mathbb{H}}(\cA)$ is a genus-$0$
  1797	object: the configuration space $\FM_k(\C)$ is
  1798	on~$\C \simeq \mathbb{P}^1 \setminus \{\infty\}$, not
  1799	on a higher-genus surface, and the differential uses the
  1800	rational propagator $K^{(0)} = dz/(z-w)$.
  1801	Genus dependence enters via the closed-sector curvature
  1802	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$
  1803	(Construction~\ref{constr:bar-fact-coalgebra}(iv)), which
  1804	deforms only $d_{\mathrm{bb}}$ and leaves $d_{\partial\partial}$
  1805	and $d_{\mathrm{mix}}$ unchanged
  1806	(Proposition~\ref{prop:mixed-sector-genus-independence}).
  1807	\end{remark}
  1808	
  1809	\begin{construction}[The factorizable $D$-module from a chiral algebra]
  1810	\label{constr:fact-dmod-from-chiral}
  1811	\index{factorizable D-module@factorizable $D$-module!from chiral algebra}


thinking
**Evaluating structural issues**

The title mentioning "half-plane model as SC coalgebra datum" doesn't match the text since it doesn't confirm the bar complex as SC-coalgebra. This feels like a structural or prose problem. The title suggests SC coalgebra, while the text discusses genus-0 and curvature without explicitly negating SC. It might be a high-severity structural drift rather than a mathematical violation, but the user wants specific references. I need to decide if this warrants a report since it can cause confusion.
thinking
**Analyzing structural discrepancies**

I see a few instances that highlight potential discrepancies. In Vol II, the title "The half-plane model as SC coalgebra datum" appears misleading since it only discusses the half-plane bar complex. There's a direct math claim in another section, and in Vol I, a label kept for backward compatibility may not be viewed by users. Additionally, there's a subsec label that doesn't match the text. I should inspect more indexes related to "Swiss-cheese" and bar complexes for further clarity. I'll need to search thoroughly for associated titles.
exec
/bin/zsh -lc "rg -n 'Swiss-cheese.*bar|bar.*Swiss-cheese|bar-swiss-cheese|bar complex"'!Swiss-cheese|Swiss-cheese provenance|Swiss-cheese decomposition|SCchtop-?coalgebra datum|SC'"\\"'^'"\\{\\\\ch,\\\\top\\}-coalgebra|SCchtop bar coalgebra' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'Swiss-cheese.*bar|bar.*Swiss-cheese|bar-swiss-cheese|bar complex"'!Swiss-cheese|Swiss-cheese provenance|Swiss-cheese decomposition|SCchtop-?coalgebra datum|SC'"\\"'^'"\\{\\\\ch,\\\\top\\}-coalgebra|SCchtop bar coalgebra' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Swiss-cheese.*bar|bar.*Swiss-cheese|bar-swiss-cheese|bar complex"'!Swiss-cheese|Swiss-cheese provenance|Swiss-cheese decomposition|SCchtop-?coalgebra datum|SC'"\\"'^'"\\{\\\\ch,\\\\top\\}-coalgebra|SCchtop bar coalgebra' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_celestial_holography_extensions.tex:480:\begin{remark}[Swiss-cheese non-formality versus bar concentration]
chapters/examples/w-algebras-stable.tex:4:W-algebras are the decisive test cases for the $A_\infty$ chiral framework in the $d' = 1$ regime. The reason is structural: the pre-reduction affine vertex algebra $V_k(\mathfrak{g})$ is Koszul (Theorem~\ref{thm:one-loop-koszul}), so the transferred $A_\infty$ operations on bar cohomology vanish ($m_k = 0$ for $k \ge 3$), though the Swiss-cheese operations on $V_k(\mathfrak{g})$ itself have $m_3^{\mathrm{SC}} \neq 0$ (class~$\mathbf{L}$, depth~$3$). Drinfeld--Sokolov reduction changes this. The BRST functor manufactures the higher operations $m_k$ for $k \ge 3$ that break Swiss-cheese formality (Theorem~\ref{thm:ds-koszul-obstruction}): the quartic OPE pole of the Virasoro generator, the quintic pole of $W_3$, and the higher poles of $W_N$ are all artefacts of the reduction, absent in the affine input. The resulting $\mathcal{W}$-algebra remains chirally Koszul (the bar complex is well-behaved), but the $A_\infty$ structure is genuinely infinite. This section computes the $A_\infty$ operations, spectral $r$-matrices, and deformation data for Virasoro and $W_3$ via the Khan--Zeng 3D holomorphic-topological Poisson sigma model \cite{KZ25}.
chapters/connections/holomorphic_topological.tex:28:(Theorem~\ref{thm:bar-swiss-cheese}), provides the algebraic input.
chapters/connections/holomorphic_topological.tex:115: \textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}
chapters/connections/holomorphic_topological.tex:135:Theorem~\ref{thm:bar-swiss-cheese}. The Koszul dual identification
chapters/connections/holomorphic_topological.tex:1286:(Theorem~\ref{thm:bar-swiss-cheese}: coassociative coproduct
chapters/connections/dnp_identification_master.tex:58:\section{Face 1: Swiss-cheese bar-cobar twisting}
chapters/connections/spectral-braiding-core.tex:601:constructs via the Swiss-cheese bar complex and derived center.
chapters/connections/thqg_fm_calculus_extensions.tex:1935:% label removed: cor:bar-swiss-cheese
chapters/connections/spectral-braiding-frontier.tex:379:\,d\lambda$ produces the infinitesimal braiding, and the full quantum $R(z)$ produces the finite braiding. For the affine lineage, this is proved unconditionally: one-loop exactness collapses the $A_\infty$ tower, on the reduced evaluation comparison surface the reduced HT monodromy identifies with the KZ monodromy, and the affine Drinfeld--Kohno theorem compares that monodromy with the corresponding braided tensor-product representation of $\mathrm{Rep}_q(\fg)$ there (Theorem~\ref{thm:affine-monodromy-identification}). On the $\mathfrak{sl}_2$ weight system, the bar complex integrals over $\FM_n(\C) \times \Conf_n(\R)$ compute the colored Jones polynomial (Corollary~\ref{cor:jones-polynomial}), recovering the Reshetikhin--Turaev invariant directly from the Swiss-cheese structure. The all-types categorical Clebsch--Gordan and
chapters/connections/ht_bulk_boundary_line_frontier.tex:126:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}.
chapters/connections/ht_bulk_boundary_line_frontier.tex:229:Statement~(ii) is Theorem~\ref{thm:bar-swiss-cheese} (the
chapters/connections/celestial_holography_core.tex:1014:\begin{theorem}[Helicity splitting via the Swiss-cheese decomposition; part~\textup{(i)} \ClaimStatusProvedHere, parts~\textup{(ii)--(v)} \ClaimStatusHeuristic]
chapters/connections/ym_instanton_screening.tex:774:Polyakov's Wilson loop $\langle W(C) \rangle$ should admit a sum-over-surfaces representation with the loop~$C$ as boundary. In the Swiss-cheese bar-cobar of Volume~II, this is the open-string channel: the boundary of the worldsheet is a module over the boundary chiral algebra~$\cA_{\partial}$. Line operators in the holomorphic-topological theory carry the shadow obstruction tower's boundary data.
chapters/connections/line-operators.tex:1683:Swiss-cheese bar-cobar adjunction. The open-colour Koszul dual
chapters/connections/relative_feynman_transform.tex:50:The Maurer--Cartan equation $D\Theta^{\mathrm{oc}} + \tfrac{1}{2}[\Theta^{\mathrm{oc}}, \Theta^{\mathrm{oc}}] = 0$ is the MC equation for the relative Feynman transform of the modular Swiss-cheese operad~$\SCmod$. The bicomplex structure $D_0^2 = 0$, $D_1^2 = 0$, $D_0 D_1 + D_1 D_0 = 0$ on the modular bar complex~$\Bmod(C)$, together with the genus spectral sequence, are formal consequences of the algebra-over-relative-Feynman-transform structure.
chapters/connections/thqg_ht_bbl_extensions.tex:2316:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}.
chapters/connections/concordance.tex:184:(Theorem~\ref{thm:bar-swiss-cheese}).
chapters/connections/conclusion.tex:9:$\barB^{\mathrm{ch}}(\cA)$ of Volume~I and the Swiss-cheese operad
chapters/connections/conclusion.tex:272:helicity splitting is Swiss-cheese decomposition,
 succeeded in 52ms:
chapters/theory/e1_chiral_algebras.tex:179:Volume~II resolves the ordered side of the programme. Its seven parts develop the Swiss-cheese operad, the ordered bar complex, the classical $r(z)$-matrix at level $k$, the seven faces of $r(z)$, and the derived center of an $E_1$-chiral algebra. Vol~III uses that machinery through the CY interface fixed here.
chapters/theory/e1_chiral_algebras.tex:611:Four facts control the later parts of Vol~III. First, factorization algebras on a complex curve are $E_2$ topologically but specialize to $E_1$ when holomorphy fixes an ordering, and the Swiss-cheese splitting $E_1(C) \times E_2(\mathrm{top})$ makes that specialization precise. Second, the ordered bar complex $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with deconcatenation coproduct is the natural $E_1$ primitive, and averaging to the symmetric bar $B^{\Sigma}(A)$ is lossy because it kills the ordered $R$-matrix data. Third, the CY-to-chiral functor $\Phi$ at $d=2$ produces an ordered bar whose Euler character is the Borcherds denominator and whose first shadow invariant is $\kappa_{\mathrm{ch}}$, distinct from $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, and $\kappa_{\mathrm{fiber}}$. Fourth, the $E_2$ enhancement requires the Drinfeld center construction, the categorified averaging map $E_1\text{-Cat} \to E_2\text{-Cat}$; at $d=3$ the enhancement is conditional on the CY-A$_3$ programme.
chapters/theory/cy_to_chiral.tex:1800:The results of this chapter connect the CY$_3$ programme to the algebraic engine of Vol~I (Theorems~A--D, the bar-intrinsic MC element $\Theta_A := D_A - d_0$) and the holomorphic-topological QFT framework of Vol~II (Swiss-cheese structure, PVA descent).
 succeeded in 51ms:
chapters/theory/en_koszul_duality.tex:1250:\index{Swiss-cheese operad!on derived center, NOT on bar}
chapters/theory/en_koszul_duality.tex:1295:\label{thm:bar-swiss-cheese}% label retained for backward compatibility
chapters/theory/en_koszul_duality.tex:1437:Theorem~\textup{\ref{thm:bar-swiss-cheese}} is the statement that
chapters/theory/en_koszul_duality.tex:2150:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
chapters/theory/en_koszul_duality.tex:2176:(Theorem~\ref{thm:bar-swiss-cheese}) with the recognition theorem.
chapters/theory/en_koszul_duality.tex:5292:(Theorem~\ref{thm:bar-swiss-cheese}); the symmetric bar
chapters/theory/chiral_koszul_pairs.tex:2459:This ordering refines the Koszulness programme: all four classes are chirally Koszul (bar $E_2$-collapse), but they differ in Swiss-cheese formality depth.
chapters/connections/holomorphic_topological.tex:28:(Theorem~\ref{thm:bar-swiss-cheese}), provides the algebraic input.
chapters/connections/holomorphic_topological.tex:123: \textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}
chapters/connections/holomorphic_topological.tex:143:Theorem~\ref{thm:bar-swiss-cheese}. The Koszul dual identification
chapters/connections/holomorphic_topological.tex:1236:(Theorem~\ref{thm:bar-swiss-cheese}: deconcatenation coproduct
chapters/connections/thqg_preface_supplement.tex:1892:The Swiss-cheese extension of the modular bar construction
chapters/frame/heisenberg_frame.tex:2732:\subsection{Swiss-cheese decomposition}
chapters/frame/heisenberg_frame.tex:2739:directions (Theorem~\ref{thm:bar-swiss-cheese}). The
chapters/frame/heisenberg_frame.tex:2775:The proof is the same as Theorem~\ref{thm:bar-swiss-cheese},
chapters/connections/thqg_introduction_supplement_body.tex:67:(Theorem~\ref{thm:bar-swiss-cheese}).

thinking
**Inspecting potential anomaly**

I'm noticing a potential issue with the file `anomaly_completed_topological_holography.tex`. It mentions that "Swiss-cheese algebra is presented by the bar complex." I need to check if this aligns with AP165 since there might be some confusion there. It seems like it could be an error, so I'll inspect it more closely to get clarity. Let's just make sure everything is in order!
exec
/bin/zsh -lc "nl -ba chapters/connections/anomaly_completed_topological_holography.tex | sed -n '1834,1844p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  1834	 genus-Clifford, and localization package.
  1835	\end{enumerate}
  1836	The boundary fixes the formal-local bulk model at all genera.
  1837	Identifying that strict model with the physical bulk package
  1838	remains the H-level bridge problem: the proposed holographic
  1839	dictionary is presented by the transgression algebra, as the
  1840	Swiss-cheese algebra is presented by the bar complex.
  1841	\end{remark}
  1842	
  1843	\begin{remark}[Repository integration]
  1844	% label removed: rem:tholog-repository-integration
exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '596,604p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   596	perturbative invariants: the associated graded of the
   597	holomorphic weight filtration recovers the formal power
   598	series in~$\hbar$ that underlie the CFG construction. In
   599	this sense, the CFG $E_3$-algebra is the perturbative shadow
   600	of the $E_3$-topological structure that the present volume
   601	constructs via the Swiss-cheese bar complex and derived center.
   602	
   603	The key structural comparison is between traces:
   604	CFG compute link invariants as factorisation homology of their

thinking
**Searching Swiss-cheese bar complex**

I'm thinking that the phrase "Swiss-cheese bar complex" could be a bit messy because it pairs two terms together. It feels like it might be MEDIUM prose, but I'm really not sure without more context. It’s possible there could be multiple instances of that phrase, which makes me want to search for the exact wording to see how it's used. I need to dig into that to clarify my understanding!
exec
/bin/zsh -lc "rg -n 'Swiss-cheese bar complex|SCchtop bar complex|bar complex and derived center|bar complex.*derived center|Swiss-cheese algebra.*bar complex|half-plane model as \\\\SCchtop-?coalgebra datum|bar-swiss-cheese' chapters/" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/examples-worked.tex:2613:(the bar complex classifies twisting morphisms, not bulk observables). It is the chiral derived center
chapters/connections/spectral-braiding-core.tex:601:constructs via the Swiss-cheese bar complex and derived center.
chapters/theory/foundations.tex:211:programme (Volume~I, Theorem~\textup{\ref*{thm:bar-swiss-cheese}}).
chapters/theory/foundations.tex:1897:Theorem~\ref*{thm:bar-swiss-cheese} of
chapters/connections/concordance.tex:184:(Theorem~\ref{thm:bar-swiss-cheese}).
chapters/connections/bar-cobar-review.tex:1323:\label{subsec:bar-swiss-cheese}
chapters/connections/bar-cobar-review.tex:1325:The chiral bar complex $\barB_{\mathrm{ch}}(\cA)$ carries two structures: the bar differential $d_{\barB}$ (from the holomorphic direction) and the deconcatenation coproduct $\Delta$ (from the topological direction). Together they make $\barB(\cA)$ an $E_1$ dg coassociative coalgebra: the differential is a coderivation of the coproduct. The $\SCchtop$ structure does not live on $\barB(\cA)$ itself; it emerges in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$, where the bulk $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ acts on the boundary~$\cA$ (Section~\ref{sec:derived-center}).
chapters/connections/bar-cobar-review.tex:1329:\label{thm:bar-swiss-cheese}
chapters/connections/bar-cobar-review.tex:1567:\label{rem:bar-swiss-cheese-strategy}
chapters/connections/bar-cobar-review.tex:1571:Theorem~\ref{thm:bar-swiss-cheese} identifies $\Delta$ as the
chapters/connections/bar-cobar-review.tex:1604:Theorem~\ref{thm:bar-swiss-cheese} produces the ordered bar complex
chapters/connections/bar-cobar-review.tex:1630: coalgebra of Theorem~\ref{thm:bar-swiss-cheese}. Linear duality
chapters/connections/bar-cobar-review.tex:1807:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
chapters/connections/bar-cobar-review.tex:1913:Part~(i) combines Theorem~\ref{thm:bar-swiss-cheese} (the bar complex
chapters/connections/bar-cobar-review.tex:1919:(Theorem~\ref{thm:bar-swiss-cheese}), the Quillen equivalence gives
chapters/connections/bar-cobar-review.tex:3709:(Theorem~\ref{thm:bar-swiss-cheese}): the $A_\infty$ operations
chapters/connections/bar-cobar-review.tex:3970:coderivation (Theorem~\ref{thm:bar-swiss-cheese}, Step~2), now
chapters/connections/bar-cobar-review.tex:4093:The $E_1$ dg coalgebra structure of $\barB(\cA)$ (Theorem~\ref{thm:bar-swiss-cheese}) encodes both directions: the deconcatenation coproduct encodes the $\mathbb{R}$-direction (topological factorization), while the bar differential encodes the $\mathbb{C}$-direction (holomorphic collisions). The $\SCchtop$ structure emerges in the chiral derived center pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\, \cA)$ (Part~\ref{part:swiss-cheese} of this volume).
chapters/connections/log_ht_monodromy_frontier.tex:744:\item the \emph{factorization origin}: the connection arises from the Swiss-cheese bar complex, not from the Sugawara construction alone;
chapters/connections/thqg_fm_calculus_extensions.tex:1935:% label removed: cor:bar-swiss-cheese
exec
/bin/zsh -lc "rg -n 'Swiss-cheese bar complex|SCchtop bar complex|bar complex and derived center|bar complex.*derived center|Swiss-cheese algebra.*bar complex|half-plane model as \\\\SCchtop-?coalgebra datum|bar-swiss-cheese' chapters/" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n 'Swiss-cheese bar complex|SCchtop bar complex|bar complex and derived center|bar complex.*derived center|Swiss-cheese algebra.*bar complex|half-plane model as \\\\SCchtop-?coalgebra datum|bar-swiss-cheese' chapters/" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/modular_koszul_bridge.tex:4:A CY category $\cC$ produces, via the CY-to-chiral functor $\Phi$ of Chapter~\ref{ch:cy-to-chiral}, a chiral algebra $A_\cC$; the bar complex $B(A_\cC) = T^c(s^{-1}\overline{A_\cC})$, built on the augmentation ideal $\overline{A_\cC} = \ker(\varepsilon)$, is a factorization coalgebra on $\Ran(C)$. Three Volume~I structures act on $B(A_\cC)$. The Verdier intertwining $D_{\Ran}(B(A)) \simeq B(A^!)$ of Theorem~A is a functor of factorization coalgebras on $\Ran(C)$; it is the Koszul duality, not bar-cobar inversion, and not the chiral derived center. Complementarity (Theorem~C) splits the genus-$g$ shadow complex into Verdier eigenspaces and, on the uniform-weight lane, equates the scalar sum of Koszul-dual modular characteristics to a family-dependent Koszul conductor. The genus tower (Theorem~D) identifies $\mathrm{obs}_g$ with $\kappa_{\mathrm{ch}} \cdot \lambda_g$ on the uniform-weight lane at genus $1$ unconditionally, with a cross-channel correction $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$ for multi-weight algebras. Vol~III inherits three deficiencies. First, the convolution dg Lie algebra living on $\overline{\cM}_{g,n}$ has no existing CY-side habitat. Second, the Vol~I scalar complementarity (Vol~I Theorem~C$_2$, with its family-dependent Koszul conductor; see Remark~\ref{rem:cy-complementarity-kappa-zero} below) has no CY translation stating which Koszul conductor $K_X$ applies at $d \in \{2, 3\}$. Third, the Vol~I CohFT promotion (Theorem~D$+$H) has no CY restatement tracking the flat identity axiom through $\Phi$. Five sections address these deficiencies and their consequences: \S\ref{sec:modular-conv-cy} builds the CY modular convolution algebra; \S\ref{sec:cy-complementarity-bridge} transports complementarity with explicit (C1) versus (C2) scoping and explicit $d = 2$ versus $d = 3$ conditionality; \S\ref{sec:cy-shadow-cohft} upgrades the shadow tower to a CohFT on $\overline{\cM}_{g,n}$ and records how the Borcherds lift converts the $K3 \times E$ tower into the genus-$2$ Igusa cusp form $\Phi_{10}$; \S\ref{sec:hochschild-bridge} establishes the bridge between the three Hochschild theories (categorical, chiral, derived-center) through $\Phi$; and \S\ref{sec:cy-bridge-examples} collects the principal examples with their $\kappa_\bullet$-spectra.
chapters/connections/bar_cobar_bridge.tex:50:These are not the same operation, and the CY cyclic bar complex $\mathrm{CC}_\bullet(\cC)$ corresponds to $B(A)$ itself, not to the derived center and not to the cobar.
chapters/theory/introduction.tex:13:A chiral algebra $A$ on a curve $X$ carries a bar complex $B(A)$, a factorization coalgebra on $\Ran(X)$ whose differential encodes holomorphic OPE residues and whose coproduct encodes topological interval-cutting. At genus $g \geq 1$, the bar complex acquires curvature $\kappa_{\mathrm{ch}}(A) \cdot \omega_g$ from the Hodge bundle, and the full modular structure is controlled by the universal Maurer--Cartan element $\Theta_A := D_A - d_0$ (Volume~I). Together with the $\SC^{\mathrm{ch,top}}$ structure on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ (Volume~II), these data form the complete modular invariant.
chapters/connections/geometric_langlands.tex:4:The functor $\Phi$ of \ref{part:bridge} sends a Calabi--Yau category to an $\Etwo$-chiral algebra; the bar complex of the output (Volume~I, Theorem~A) is the factorization invariant on which geometric Langlands is ultimately a statement. This chapter traces the thread. At the critical level the Feigin--Frenkel theorem identifies the chiral center with the algebra of $G^L$-opers; the Verdier intertwining of Volume~I Theorem~A then relates local geometric Langlands to the four-functor picture (bar, cobar, Verdier, derived center). For Calabi--Yau input, the analogue is conjectural: a Langlands dual of a CY $d$-category should realize the mirror of its $\Phi$-image. The chapter is entirely FRONTIER material. Every formal statement uses \texttt{\textbackslash{}begin\{conjecture\}} unless it is a literal citation of Feigin--Frenkel (1992) or Frenkel--Gaitsgory (2006), in which case it is tagged \ClaimStatusProvedElsewhere.
chapters/theory/cy_to_chiral.tex:1829:The bar complex $B(A)$ is an $\Eone$ chiral coassociative coalgebra over $(\mathrm{ChirAss})^!$; the $\SC^{\mathrm{ch,top}}$ two-colour structure emerges on the derived center pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$, not on the bar complex itself. Three bar constructions reflect three levels of operadic symmetry:
chapters/theory/e1_chiral_algebras.tex:179:Volume~II resolves the ordered side of the programme. Its seven parts develop the Swiss-cheese operad, the ordered bar complex, the classical $r(z)$-matrix at level $k$, the seven faces of $r(z)$, and the derived center of an $E_1$-chiral algebra. Vol~III uses that machinery through the CY interface fixed here.
 succeeded in 51ms:
chapters/frame/heisenberg_frame.tex:2739:directions (Theorem~\ref{thm:bar-swiss-cheese}). The
chapters/frame/heisenberg_frame.tex:2775:The proof is the same as Theorem~\ref{thm:bar-swiss-cheese},
chapters/connections/holomorphic_topological.tex:28:(Theorem~\ref{thm:bar-swiss-cheese}), provides the algebraic input.
chapters/connections/holomorphic_topological.tex:123: \textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}
chapters/connections/holomorphic_topological.tex:143:Theorem~\ref{thm:bar-swiss-cheese}. The Koszul dual identification
chapters/connections/holomorphic_topological.tex:1236:(Theorem~\ref{thm:bar-swiss-cheese}: deconcatenation coproduct
chapters/connections/thqg_introduction_supplement_body.tex:67:(Theorem~\ref{thm:bar-swiss-cheese}).
chapters/theory/en_koszul_duality.tex:1283:The passage from bar complex to derived center is
chapters/theory/en_koszul_duality.tex:1295:\label{thm:bar-swiss-cheese}% label retained for backward compatibility
chapters/theory/en_koszul_duality.tex:1437:Theorem~\textup{\ref{thm:bar-swiss-cheese}} is the statement that
chapters/theory/en_koszul_duality.tex:2150:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
chapters/theory/en_koszul_duality.tex:2176:(Theorem~\ref{thm:bar-swiss-cheese}) with the recognition theorem.
chapters/theory/en_koszul_duality.tex:5292:(Theorem~\ref{thm:bar-swiss-cheese}); the symmetric bar

thinking
**Inspecting connection issue**

I'm noticing a potential issue with the log file referencing the Swiss-cheese bar complex. It seems to be an error at line 744 in `log_ht_monodromy_frontier.tex`. I want to inspect that closely to understand the root of this connection problem. I'll need to delve deeper into the details of the file and see if I can pinpoint what might be going wrong here. This could be key to resolving it!
exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy_frontier.tex | sed -n '738,748p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   738	\providecommand{\fS}{\mathfrak{S}}
   739	
   740	Theorem~\ref{thm:affine-monodromy-identification} identifies the monodromy of the reduced HT connection with the quantum group $R$-matrix on \emph{evaluation modules}: finite-dimensional $\fg$-modules pulled back to the dg-shifted Yangian $Y_\h(\fg)$ via the evaluation homomorphism. This section develops the derived Steinberg geometry that governs the extension beyond evaluation modules, working in detail for $\fg = \mathfrak{sl}_2$ at generic level $k$.
   741	
   742	The genuine new content beyond the classical Drinfeld--Kohno theorem is not the monodromy identification itself (which DK proves on category $\cO$ modules), but rather:
   743	\begin{enumerate}[label=\textup{(\alph*)}]
   744	\item the \emph{factorization origin}: the connection arises from the Swiss-cheese bar complex, not from the Sugawara construction alone;
   745	\item the \emph{derived enhancement}: the full $A_\infty$ superconnection on the bar coalgebra $\mathrm{B}(V^k(\fg))$ specializes, after one-loop collapse and passage to the reduced evaluation comparison surface, to the KZ connection, but carries strictly more information before reduction;
   746	\item the \emph{Steinberg geometric package}: the monodromy acts on the derived Steinberg object $\fS_b$, which carries a $(-1)$-shifted symplectic structure encoding both the convolution product and the line-category tensor structure;
   747	\item the \emph{convergence mechanism}: the exponential $\exp(2\pi i \cdot \Omega/(k+h^\vee))$ converges in the completed tensor product $\End(\cL_b^{\wot 2})$ by a spectral bound that uses the polynomial growth of the $\lambda$-bracket, not merely the finite-dimensionality of evaluation modules.
   748	\end{enumerate}

thinking
**Investigating report classifications**

I’m considering whether to report these findings as MEDIUM or HIGH, perhaps depending on their context within theorems or proofs. I'll take a closer look at specific lines, like spectral-braiding-core line 601 and anomaly line 1840. It seems these are more related to connection/frontier prose rather than theorem, so MEDIUM seems appropriate. I also need to search for the phrase "Swiss-cheese bar complex" in V2 to see the connections and results specific to this context.
exec
/bin/zsh -lc "rg -n 'Swiss-cheese bar complex|Swiss-cheese algebra is presented by the bar complex|SCchtop bar coalgebra|half-plane model as \\\\SCchtop-?coalgebra datum|Swiss-cheese structure exist|Swiss-cheese bar-cobar|bar-swiss-cheese' chapters/" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '598,603p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/anomaly_completed_topological_holography.tex | sed -n '1836,1841p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/connections/spectral-braiding-core.tex:601:constructs via the Swiss-cheese bar complex and derived center.
chapters/connections/holomorphic_topological.tex:28:(Theorem~\ref{thm:bar-swiss-cheese}), provides the algebraic input.
chapters/connections/holomorphic_topological.tex:115: \textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}
chapters/connections/holomorphic_topological.tex:135:Theorem~\ref{thm:bar-swiss-cheese}. The Koszul dual identification
chapters/connections/holomorphic_topological.tex:1286:(Theorem~\ref{thm:bar-swiss-cheese}: coassociative coproduct
chapters/connections/thqg_fm_calculus_extensions.tex:1935:% label removed: cor:bar-swiss-cheese
chapters/connections/dnp_identification_master.tex:58:\section{Face 1: Swiss-cheese bar-cobar twisting}
chapters/connections/ht_bulk_boundary_line.tex:1307:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}.
chapters/connections/ht_bulk_boundary_line.tex:1389:Statement~(i) is Theorem~\ref{thm:bar-swiss-cheese} (the bar
chapters/connections/ht_bulk_boundary_line_frontier.tex:126:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese}}\textup{)}.
chapters/connections/ht_bulk_boundary_line_frontier.tex:229:Statement~(ii) is Theorem~\ref{thm:bar-swiss-cheese} (the
chapters/connections/ym_instanton_screening.tex:774:Polyakov's Wilson loop $\langle W(C) \rangle$ should admit a sum-over-surfaces representation with the loop~$C$ as boundary. In the Swiss-cheese bar-cobar of Volume~II, this is the open-string channel: the boundary of the worldsheet is a module over the boundary chiral algebra~$\cA_{\partial}$. Line operators in the holomorphic-topological theory carry the shadow obstruction tower's boundary data.
chapters/connections/bar-cobar-review.tex:1323:\label{subsec:bar-swiss-cheese}
chapters/connections/bar-cobar-review.tex:1329:\label{thm:bar-swiss-cheese}
chapters/connections/bar-cobar-review.tex:1567:\label{rem:bar-swiss-cheese-strategy}
chapters/connections/bar-cobar-review.tex:1571:Theorem~\ref{thm:bar-swiss-cheese} identifies $\Delta$ as the
chapters/connections/bar-cobar-review.tex:1604:Theorem~\ref{thm:bar-swiss-cheese} produces the ordered bar complex
chapters/connections/bar-cobar-review.tex:1630: coalgebra of Theorem~\ref{thm:bar-swiss-cheese}. Linear duality
chapters/connections/bar-cobar-review.tex:1807:\textup{(}Theorem~\textup{\ref{thm:bar-swiss-cheese})}.
chapters/connections/bar-cobar-review.tex:1913:Part~(i) combines Theorem~\ref{thm:bar-swiss-cheese} (the bar complex
 succeeded in 52ms:
   598	series in~$\hbar$ that underlie the CFG construction. In
   599	this sense, the CFG $E_3$-algebra is the perturbative shadow
   600	of the $E_3$-topological structure that the present volume
   601	constructs via the Swiss-cheese bar complex and derived center.
   602	
   603	The key structural comparison is between traces:
 succeeded in 50ms:
  1836	The boundary fixes the formal-local bulk model at all genera.
  1837	Identifying that strict model with the physical bulk package
  1838	remains the H-level bridge problem: the proposed holographic
  1839	dictionary is presented by the transgression algebra, as the
  1840	Swiss-cheese algebra is presented by the bar complex.
  1841	\end{remark}







thinking
**Verifying findings**

I need to verify each finding against the actual file content to eliminate any false positives. One candidate is from Vol II, specifically chapters/connections/3d_gravity.tex, lines 5143-5147, which includes the phrase, "The half-plane bar complex ... is the $\SCchtop$ bar coalgebra." This seems critical, as it could imply forbidden object-level identification. Another is from Vol II, chapters/theory/factorization_swiss_cheese.tex, lines 1792-1793, which discusses the title, "The half-plane model as $\SCchtop$-coalgebra datum," labeled as high priority.
thinking
**Evaluating report structure**

I'm considering possibly including the high structural aspect at Vol I, since the comment points out that it’s a known stale surface and keeps the label for backward compatibility. I wonder if it’s wise not to duplicate with Vol II since the user requested the exact text from the report file:line. It might be helpful to mention downstream propagation, saying that the same stale label is re-exported in Vol II. However, I might face formatting issues with multiple file references.
thinking
**Evaluating SC-algebra context**

I noticed that it doesn't state that the bar complex is an SC-coalgebra. Instead, it mentions the bar of a chiral algebra being promoted to an SC-algebra through self-action. This seems a bit strange and might just be a leftover detail. I should consider inspecting the previous context, especially regarding the construction of self-action, but maybe it's fine to skip it since it's not directly relevant to AP165.
thinking
**Evaluating model title significance**

I think the title `half-plane model as SCchtop-coalgebra datum` might not carry as much weight as I initially thought. However, it is visible and explicit, so I wonder if I could denote both as separate HIGH and MEDIUM, but without overwhelming the content. 

I’m considering whether the term "datum" refers specifically to the bar complex plus action pair. The body doesn’t clarify this, which could lead to potential confusion. As for `Swiss-cheese bar complex`, it's clearly less effective. I might skip the title to prevent misrepresentation.
thinking
**Identifying structural elements**

I'm considering that another significant structural component could be the local theorem label from `bar-cobar-review.tex:1329` since it’s the same. However, if I mention the Vol I source along with its propagation in Vol II, that might be sufficient. 

It seems I also need to check Vol III to ensure there are no violations in the process. Keeping everything clear and accurate is essential.
thinking
**Considering structural issues**

I'm thinking about the final version of the document. The contract says to end with a summary, and I wonder if I should mention "No surviving violations in Vol III" after the list or before the summary. Following that, the phrase "Verdict: FAIL" might suffice. I also question if some references might count as structural issues, especially if they appear correct in context but are stale. Specifically, examining `bar-cobar-review.tex` could also be insightful, focusing on user-visible labels.
thinking
**Assessing structural findings**

I’m considering whether to label the internal issues or not, and it seems better to focus on the high structural finding, such as `chapters/connections/3d_gravity.tex:5146` as a direct violation. There are medium severity findings too, but only one is critical, and I'm not sure if I need to report on every category. The user asked for severity categories, so if there are structural issues, including the high stale label might be useful. I should double-check the line numbers and the exact text for clarity.
codex
I have one unambiguous mathematical violation and a small set of downstream prose/structural drifts. I’m re-reading just those lines now so the final list contains only text that actually survives adversarial scrutiny.
exec
/bin/zsh -lc "sed -n '599,601p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '742,745p' chapters/connections/log_ht_monodromy_frontier.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '5143,5147p' chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1838,1840p' chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1293,1296p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
The genuine new content beyond the classical Drinfeld--Kohno theorem is not the monodromy identification itself (which DK proves on category $\cO$ modules), but rather:
\begin{enumerate}[label=\textup{(\alph*)}]
\item the \emph{factorization origin}: the connection arises from the Swiss-cheese bar complex, not from the Sugawara construction alone;
\item the \emph{derived enhancement}: the full $A_\infty$ superconnection on the bar coalgebra $\mathrm{B}(V^k(\fg))$ specializes, after one-loop collapse and passage to the reduced evaluation comparison surface, to the KZ connection, but carries strictly more information before reduction;
 succeeded in 50ms:
this sense, the CFG $E_3$-algebra is the perturbative shadow
of the $E_3$-topological structure that the present volume
constructs via the Swiss-cheese bar complex and derived center.
 succeeded in 50ms:
remains the H-level bridge problem: the proposed holographic
dictionary is presented by the transgression algebra, as the
Swiss-cheese algebra is presented by the bar complex.
 succeeded in 51ms:
The half-plane bar complex
$\barB^{\mathbb{H}}(\cA)$
(Construction~\ref{constr:half-plane-bar}) is the
$\SCchtop$ bar coalgebra. The transverse bar complex is
the standard $\Eone$-bar of $\barB^{\mathbb{H}}(\cA)$,
 succeeded in 51ms:
\begin{theorem}[Bar complex as $\Eone$-chiral coassociative coalgebra;
\ClaimStatusProvedHere]
\label{thm:bar-swiss-cheese}% label retained for backward compatibility
\label{thm:bar-e1-coalgebra}



thinking
**Considering file paths**

I’m thinking about how to handle files for Vol II/III since the user seems to want access across all three volumes. It looks like I might need to use full paths or a path with a volume prefix. An absolute path could work, such as `/Users/raeez/chiral-bar-cobar-vol2/chapters/...:5146`, but that feels a bit lengthy. Maybe a relative path with some volume context would be clearer and more concise!
thinking
**Reviewing formatting issues**

I'm considering whether we might violate any formatting rules with nested bullets. It looks like we've found six violations, while perhaps only checking 29 instances—so, the verdict appears to be a FAIL. I think it's worthwhile to note that there are no surviving violations found in Volume III, which could be mentioned just before the summary. We want to be careful not to overstate anything. For instance, I can identify specific phrases for citations regarding prose conflation.
thinking
**Clarifying volume violations**

I need to mention that not all volumes have violations. It would be useful to state something like, "The hits checked in Volume III were corrective only," right after listing the findings. My goal is to craft a final answer that's concise yet detailed enough to convey the important information without overwhelming anyone. Balancing thoroughness with clarity is key here, so I’ll ensure to keep things straightforward and direct.
codex
[CRITICAL] Vol II `chapters/connections/3d_gravity.tex:5146` — Direct AP165/B54 violation: `$\SCchtop$ bar coalgebra.` In context, this sentence says `The half-plane bar complex ... is the $\SCchtop$ bar coalgebra`, which assigns Swiss-cheese coalgebra structure to the bar complex itself rather than to the derived-center pair.

[HIGH] Vol I `chapters/theory/en_koszul_duality.tex:1295` — Structural drift persists at the canonical source: `\label{thm:bar-swiss-cheese}% label retained for backward compatibility`. The theorem text is corrected to `E_1` coassociative coalgebra, but the live theorem label still encodes the retired Swiss-cheese reading and propagates through cross-volume references.

[HIGH] Vol II `chapters/theory/factorization_swiss_cheese.tex:1792` — Structural contradiction in a core theory chapter title: `The half-plane model as $\SCchtop$-coalgebra datum`. The same file opens by stating `The bar complex is not an $\SC^{\ch,\top}$-coalgebra` at lines 20-28, so this title reintroduces the forbidden object-level framing.

[MEDIUM] Vol II `chapters/connections/log_ht_monodromy_frontier.tex:744` — Prose conflation: `the connection arises from the Swiss-cheese bar complex`. This attributes Swiss-cheese structure to the bar complex instead of reserving it for the derived-center/bulk-boundary datum.

[MEDIUM] Vol II `chapters/connections/spectral-braiding-core.tex:601` — Prose conflation: `constructs via the Swiss-cheese bar complex and derived center.` The phrasing treats the bar complex itself as Swiss-cheese-flavoured rather than `E_1` with Swiss-cheese emerging only at the derived center.

[MEDIUM] Vol II `chapters/connections/anomaly_completed_topological_holography.tex:1840` — Prose conflation: `Swiss-cheese algebra is presented by the bar complex.` This collapses the bar complex / derived-center distinction on the audited surface.

All contextualized Volume III hits I checked were corrective, not violating; likewise several Vol I/II hits were false positives where the surrounding text explicitly says the bar complex is only `E_1`-coassociative.

## Summary
Instances checked: 29 | Violations found: 6 | Verdict: FAIL
tokens used
118,200
