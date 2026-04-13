# A05_concordance (687s)

Edited [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex).

`FIXED` 1. Added the AP147 routing note in `rem:family-index-scope`, making the dependency explicit: shadow tower `\to` genus universality `\to` family index. The concordance now states that `thm:family-index` is downstream of `thm:genus-universality`, not an input to it.

`FIXED` 2. Updated topologization status so the concordance now distinguishes:
cohomological `E_3^{\mathrm{top}}` on BRST cohomology, proved for affine KM at non-critical level; chain-level lift conjectural in general. I corrected both the scoped constitutional box and `FT-5`.

`FIXED` 3. Updated MC5 status wording to the requested split: analytic proved, coderived proved, chain-level conjectural. I corrected the stale “partially proved” anti-pattern wording and the programme ledger summary.

`FIXED` 4. Updated the Koszul equivalences surface so `(vii)` is explicitly the genus-0 factorization-homology criterion, `(viii)` is weakened to a proved consequence on the Koszul locus, and the stale counts now read `9` unconditional equivalences plus `1` proved consequence rather than `10` unconditional equivalences.

No `BLOCKED` items.

Verification: I re-read all edited spans, confirmed the referenced labels `thm:family-index`, `thm:genus-universality`, `thm:topologization`, and `conj:topologization-general` exist, and grep-checked the target file for the stale pre-fix phrases; those checks returned no hits. I did not run a TeX build.


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
session id: 019d862a-dab9-7620-bfd3-fbede362b0de
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


TARGET: chapters/connections/concordance.tex

This is the CONSTITUTION. Must reflect all rectification changes.

FIXES:
1. Search for thm:family-index and thm:genus-universality. Add routing remark (AP147)
   breaking the circular dependency. The non-circular path: shadow tower -> universality -> family index.

2. Search for 'topologization' or 'topologisation'. Update status to reflect the split:
   (a) cohomological E_3 = ProvedHere for affine KM at non-critical level
   (b) chain-level E_3 = Conjectured in general

3. Search for MC5. Update to reflect: analytic proved, coderived proved, chain-level conjectural.
   The coderived proof is now clean (bv_brst.tex fixed).

4. Search for Koszul equivalences. Note that (vii) is g=0 only, (viii) weakened.

Do NOT rewrite the concordance. Only update the specific status entries.
mcp startup: no servers
codex
I’m locking the scope to `chapters/connections/concordance.tex` and the four listed status/routing fixes. First I’m reading the required repo context and locating the exact concordance entries before I patch anything.
Plan update
  → Read required constitutional context and locate the exact concordance entries for the four findings
  • Apply the minimum scoped edits in chapters/connections/concordance.tex
  • Re-read the modified entries, grep the file for forbidden/stale patterns, and report FIXED/BLOCKED status for each finding

thinking
**Reading files in parallel**

I need to read files, and I'm considering using parallel execution with the exec_command. The multi_tool_use.parallel could help here to run developer tools simultaneously. I think I might use exec_command to search for relevant patterns and then sed to extract excerpts from the required files. It seems like rg could be handy for locating lines, so I'll focus on reading key sections from CLAUDE, theorem_registry, red_team_summary, and concordance in parallel.
codex
I’m gathering the live claim surface now: concordance entries, theorem registry references, and any recent red-team notes that bear on these statuses. After that I’ll patch only the specific lines that need to move.
exec
/bin/zsh -lc "rg -n \"thm:family-index|thm:genus-universality|topologiz|topologis|MC5|Koszul equivalences|\\(vii\\)|\\(viii\\)\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:family-index|thm:genus-universality|topologiz|topologis|MC5|Koszul equivalences|topologization|coderived|chain-level|affine KM|non-critical" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP147|topologiz|topologis|MC5|Koszul equivalences|coderived|family-index|genus-universality" CLAUDE.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
416:| `thm:koszulness-from-sklyanin` | `theorem` | 2989 | Koszulness from Sklyanin--Poisson rigidity; {} for affine KM |
527:#### `chapters/theory/coderived_models.tex` (6)
531:| `prop:coderived-adequacy` | `proposition` | 243 | Adequacy |
782:| `prop:non-critical-liouville` | `proposition` | 5904 | Non-critical complementarity and the Liouville sector |
791:| `prop:chain-level-curvature-operator` | `proposition` | 626 | Chain-level curvature operator |
827:| `thm:genus-universality` | `theorem` | 5243 | Genus universality |
932:| `cor:saturation-algebraic-families` | `corollary` | 8960 | Level-direction concentration at all non-critical levels for algebraic families |
2315:| `prop:chain-level-three-obstructions` | `proposition` | 1646 | Three chain-level obstructions |
2316:| `thm:bv-bar-coderived` | `theorem` | 1895 | BV$=$bar in the coderived category |
2369:| `thm:family-index` | `theorem` | 5769 | Family index theorem for genus expansions |
2765:| `prop:thqg-X-coderived-fredholm-G` | `proposition` | 2107 | Coderived = Fredholm for class~G |
2898:| `comp:thqg-V-affine-yangian` | `computation` | 2331 | Gravitational Yangian of affine KM |
 succeeded in 51ms:
62: \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
290: (Theorem~\ref{thm:genus-universality}).}
641: (Theorem~\ref{thm:genus-universality}), which extends the FF involution
1943:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
1981:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
2889: & analytic bar coalgebra (MC5) \\[2pt]
3285:MC5 & Genus tower & Five components:
4432: & MC5 sewing programme,
4661:genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
4712:Index & GRR: scalar genus series $= \kappa(\cA) \cdot (\hat{A}(ix) - 1)$; genus-$1$ unconditional & \textbf{Proved} & Thm~\ref{thm:family-index} \\[2pt]
5280:(Theorem~\ref{thm:genus-universality}).
5287:(Theorem~\ref{thm:genus-universality}). The clutching compatibility
5412:$\kappa(\cA) \cdot \lambda_g$ (proved, Theorem~\ref{thm:genus-universality}).
5928:\ClaimStatusProvedHere]\label{thm:family-index}
5992:\textup{(}Theorem~\textup{\ref{thm:genus-universality}(ii))}
6011:(Theorem~\ref{thm:genus-universality}) establishes for
6202:Theorem~\ref{thm:genus-universality}) and imported results
6227:Theorem~\ref{thm:family-index} synthesizes the preceding results:
6466:genus~$1$ (Theorem~\ref{thm:genus-universality}).
6687: sewing (MC5). The integer-$n$ construction is well-defined from the
 exited 2 in 51ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:379:- B58. "E_3-chiral" for the topologized derived center. FALSE. The conformal vector kills the chiral direction; the result is E_3-TOPOLOGICAL. AP168.
CLAUDE.md:380:- B59. "Topologization proved for all chiral algebras with conformal vector." FALSE. Proved only for affine KM V_k(g) at non-critical level. General case conjectural (conj:topologization-general). AP167.
CLAUDE.md:480:**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."
CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
CLAUDE.md:499:| Topologization | PROVED (affine KM); CONJECTURAL (general) | SC^{ch,top} + Sugawara = E_3 for V_k(g) at k != -h^v (thm:topologization). General chiral algebras with conformal vector: conj:topologization-general. Proof cohomological; class M chain-level open. |
CLAUDE.md:826:AP147: Circular proof routing. Theorem B and def:koszul-chiral-algebra appeared mutually circular until the routing was made explicit: twisted-tensor → cone identification → bar-cobar (commit 65262ee). When a proof chain involves multiple theorems that reference each other, insert a ROUTING REMARK citing the primitive non-circular anchor. If no such anchor exists, the proof is genuinely circular and must be restructured.
CLAUDE.md:834:AP154: Two distinct E_3 structures. (a) Algebraic E_3: from HDC on E_2 bar coalgebra, no conformal vector needed. (b) Topological E_3: from Sugawara topologisation, requires conformal vector at non-critical level. These are NOT the same; their identification as families over hbar*H^3(g)[[hbar]] is CONJECTURAL (conj:e3-identification). Topological E_3 (b): PROVED for affine KM at non-critical level (thm:topologization); CONJECTURAL for general chiral algebras with conformal vector (conj:topologization-general in Vol I, conj:E3-topological-climax in Vol II). Proof is cohomological; for class M, chain-level E_3 may fail. COUNTER: always specify which E_3 and whether the claim requires Sugawara.
CLAUDE.md:838:AP158: SC^{ch,top} != E_3. The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, T(z) = {Q,G(z)}) = E_3-TOPOLOGICAL (NOT E_3-chiral). The conformal vector KILLS the chiral direction at the cohomological level: C-translations become Q-exact, the complex structure on C becomes irrelevant in cohomology, the two SC colors collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct). At critical level k=-h^v: Sugawara undefined, topologization fails. NEVER write "E_3-chiral" for the topologized bulk; it is E_3-topological. Vol II MUST construct the E_3-topological structure on Z^{der}_{ch}(A) explicitly at chain level — define it, prove it, verify on examples, and characterize the obstruction when conformal vector is absent.
CLAUDE.md:842:AP162: E_3 requires conformal vector. NEVER claim E_3 structure without stating: (a) the conformal vector exists, (b) the level is non-critical, (c) T(z) is Q-exact in the bulk. At critical level k = -h^v: Sugawara undefined, topologization fails, stuck at SC^{ch,top}. Status: PROVED for affine KM (thm:topologization); CONJECTURAL for general (conj:topologization-general). The proof is cohomological; for class M algebras the chain-level E_3 structure is open.
CLAUDE.md:849:AP167: Topologization scope. thm:topologization is PROVED for affine KM V_k(g) at non-critical level k != -h^v (where Sugawara T = {Q,G} is explicit). For general chiral algebras with conformal vector: CONJECTURAL (conj:topologization-general). The proof is COHOMOLOGICAL (works on Q-cohomology, not on cochains). For class M (Virasoro), where chain-level BV/bar is false, the E_3 may exist only on cohomology. COUNTER: every topologization reference must carry scope qualifier "(proved for affine KM at non-critical level)."
archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
codex
This is a claim-surface sync edit, so I’m loading the local workflow for status/label/concordance changes before I touch the constitution file.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:


thinking
**Evaluating theorem context**

I'm considering whether I need to read the theorem registry for more context, maybe not in full. I could focus on snippets around specific hits. It might be helpful to check relevant AP147 and red-team information, though I’m unsure about archiving red-team lines. Since there are scattered entries, I might need to open specific file sections and run a search across all volumes for theorem labels. But I also need to ensure accuracy with source files and check for duplicates.
thinking
**Searching for exact terminology**

I might also want to search the source theorem files for terms like "topologization," "MC5," and "family-index" to pinpoint the correct wording. It seems necessary to read the exact files we interact with and consider dependencies, especially since I'm only addressing the concordance. Locating theorem labels in the repository could be useful, and I think using rg for searches is a good idea. For Koszul equivalences, I should find the exact text, maybe in a specific chapter, so searching across the repo makes sense.
exec
/bin/zsh -lc "sed -n '1928,1998p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3268,3338p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7140,7215p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5880,6065p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:family-index|thm:genus-universality|thm:topologization|conj:topologization-general|MC5|Koszul equivalences|\\(vii\\)|\\(viii\\)\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{tabular}
\end{center}
The zeros of $\Delta_\cA(x)$ are the \emph{branch points}
of the modular MC problem: values of the spectral parameter
where deformation directions merge. Poles are resonance
points where the tangent complex degenerates.

For $\widehat{\mathfrak{sl}}_2$: zeros at $x=1/k$ and
$x=1/(k{+}4)$ (Feigin--Frenkel dual levels); pole at $x=1/2$
(critical level $k=-2$, where the center acquires opers).

For $\mathcal W_3$: two zeros at $x_1=1/\kappa_c$ and
$x_2=(5c{+}22)/(\kappa_c(5c{+}22){+}48)$, reflecting the
two-dimensional deformation space $(T,W)$. At $c=50$:
$x_1\to\infty$, $x_2=3/2$.

For $\beta\gamma$: the unique standard family with
$\kappa<0$. Branch point at $x=-1/2$; the genus tower has
alternating signs.

 succeeded in 51ms:
 (Theorem~\ref{thm:categorical-cg-all-types}),
 and the generated-core DK comparison surface
 \textup{(}traditionally packaged as DK-2/3\textup{)}
 on the evaluation-generated core is proved separately
 (Corollary~\ref{cor:dk23-all-types}).
 Extension beyond evaluation modules is DK-4/5 (downstream, not part of MC3).
 Key input: multiplicity-free $q$-characters for fundamental reps
 \cite{ChariMoura06} replace the minuscule hypothesis.
 Type~$A$ identifies the remaining post-CG completion packet
 (Theorem~\ref{thm:mc3-type-a-resolution});
 no global all-types closure is claimed on this row \\
MC4 & Strong filtration & Completion is formal inverse limit: the strong
 filtration axiom $\mu_r(F^{i_1},\ldots,F^{i_r}) \subset
 F^{i_1+\cdots+i_r}$ gives degree cutoff
 (Lemma~\ref{lem:degree-cutoff}), making continuity
 and Mittag-Leffler automatic
 (Theorem~\ref{thm:completed-bar-cobar-strong}) \\
MC5 & Genus tower & Five components:
 (1)~\textbf{Analytic HS-sewing proved} at all genera: polynomial OPE growth $+$ subexponential sector growth implies convergence
 (Theorem~\ref{thm:general-hs-sewing});
 succeeded in 51ms:
 theorem) is proved unconditionally. What remains is
 \emph{example-specific verification}: for each new
 algebra family beyond the standard landscape, one must
 verify that its coefficient sequences stabilize on finite
 windows and identify the H-level target. This is a
 finite computation for each family, not a theoretical
 gap.
 \emph{Arithmetic connection}: the spectral curve of the shadow
 Higgs field
 (Theorem~\ref{thm:shadow-higgs-field}) has convergence
 radius $|c|/3$ in the degree variable;
 the MC4 completion radius is controlled by the same parameter
 $\lambda_{\mathrm{eff}} = -6/c$
 (Chapter~\ref{chap:arithmetic-shadows},
 Remark~\ref{rem:effective-coupling}).
\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
 Inductive genus
 determination, 2D convergence (no UV renormalization needed),
 analytic-algebraic comparison, and the general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
 succeeded in 51ms:
 & \S\ref{sec:en-koszul-duality} \\
\ref{conj:center-essential-surjectivity}
 & Center essential surjectivity:
 every $E_2$-chiral algebra arises as a derived center
 \textup{(}Conjecture\textup{)}
 & \S\ref{sec:en-koszul-duality} \\
\ref{constr:sugawara-antighost}
 & Sugawara antighost construction:
 conformal vector at non-critical level yields
 antighost field for topologization
 & \S\ref{sec:en-koszul-duality} \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: AP165 bar-complex operadic correction}} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{AP165 correction (constitutional).}
 The bar complex $\barB(\cA)$ is an $E_1$ coassociative
 coalgebra over $(\mathrm{ChirAss})^!$, the Koszul dual
 cooperad of the chiral associative operad.
 succeeded in 51ms:
Total output lines: 345

chapters/examples/w_algebras_deep.tex:2646:propagator (Theorem~\ref{thm:genus-universality}).
chapters/frame/preface_sections10_13_draft.tex:368:MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera; the genus-$0$ algebraic BRST/bar comparison is proved; BV=bar in the coderived category is proved for all four shadow classes (including class~M). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional.
chapters/frame/preface_sections10_13_draft.tex:417:\noindent\emph{MC5} (genus expansion).
chapters/examples/beta_gamma.tex:1225:(Theorem~\ref{thm:genus-universality}), the genus-$g$ curvature
chapters/examples/y_algebras.tex:349:(Theorem~\ref{thm:genus-universality}). The generators of
chapters/examples/y_algebras.tex:741:(Theorem~\ref{thm:genus-universality}),
chapters/frame/guide_to_main_results.tex:99:\textbf{MC5 (genus tower)} &
chapters/frame/guide_to_main_results.tex:131:MC1 through MC4 are proved. MC5 is partially proved: the analytic
chapters/connections/editorial_constitution.tex:149:MC5 & BV/BRST $=$ bar
chapters/connections/editorial_constitution.tex:179:MC5 is not fully proved. What is proved at all genera is the analytic
chapters/connections/editorial_constitution.tex:459:\begin{remark}[MC5 analytic resolution vs.\ BV/BRST identification]
chapters/connections/editorial_constitution.tex:461:The analytic convergence component of MC5 is fully resolved:
chapters/connections/editorial_constitution.tex:503:&\Longrightarrow \text{MC5 physics completion}.
chapters/connections/editorial_constitution.tex:529:(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
chapters/connections/editorial_constitution.tex:562:remaining MC3--MC5 dependency chain.
chapters/connections/editorial_constitution.tex:565:\begin{conjecture}[Standard-tower MC5 reduction after MC3 and realized
chapters/connections/editorial_constitution.tex:598:itself: the remaining MC5 content is exactly the genuswise comparison
chapters/connections/editorial_constitution.tex:611:\text{MC5 BV/BRST comparison}.
codex
I found the concordance anchors. Next I’m reading the live theorem statements around `thm:topologization`, `thm:genus-universality`, and the Koszul meta-theorem so the concordance status lines match the actual scoped claims instead of a stale summary.
exec
/bin/zsh -lc "sed -n '2948,3215p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2148,2208p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "routing remark|non-circular|shadow tower|universality -> family index|family index is downstream|AP147" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/connections/editorial_constitution.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
stratification, so fiberwise $E_2$-collapse assembles to global
$E_2$-collapse: all transferred differentials $d_r = 0$ for
$r \geq 2$. Hence the spectral sequence
on~$\barBgeom(\cA)$ also collapses at~$E_2$.

\medskip
\textsc{Factorization homology concentration}
\textup{(i)}$\Leftrightarrow$\textup{(vii)}
\textup{(}the genus-$0$ specialization; cf.\
Remark~\ref{rem:fh-vii-uniform-weight-scope}\textup{)}:

\smallskip\noindent
\textup{(i)}$\Rightarrow$\textup{(vii)}\textup{ at }$g = 0$:
The bar complex \emph{is} factorization homology
(Proposition~\ref{prop:bar-fh}):
$\barB_n(\cA) = (\int_X \cA)_n$. $E_2$-collapse gives
$H^k(\int_{\mathbb{P}^1} \cA) = 0$ for $k \neq 0$: the Goodwillie
filtration of $\int_{\mathbb{P}^1} \cA$ has associated graded
given by $\barB_n$ contributions, each concentrated in degree~$0$
by PBW collapse. At $g \geq 1$ the corresponding concentration
 succeeded in 50ms:
\index{conformal vector!inner}
Let $\cA$ be a chiral algebra and let $Q$ be a
BRST-type differential on the algebra of observables
of a holomorphic--topological theory~$T$ on
$\bC \times \bR$ whose boundary chiral algebra
is~$\cA$. An \emph{inner conformal vector} for
$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
central charge~$c$ that is $Q$-exact in the algebra
of bulk observables up to a $Q$-boundary: there exists
$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
Equivalently, $T(z) = [Q, G(z)]$ in BRST cohomology.
For affine Kac--Moody $V_k(\fg)$ at non-critical level,
the Sugawara element
$T_{\mathrm{Sug}} = \frac{1}{2(k + h^\vee)}
\sum_a {:}J^a J_a{:}$
provides the inner conformal vector. For the
Virasoro algebra, $T(z)$ is the stress tensor itself.
\end{definition}

\begin{theorem}[Cohomological topologization for affine Kac--Moody; {\cite{KhanZeng25}}]
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2040:Remark~\ref{rem:non-circular-logical-chain}, this gives
chapters/theory/higher_genus_modular_koszul.tex:2727:The dependency route is one-way: the bar-intrinsic shadow tower of
chapters/theory/higher_genus_modular_koszul.tex:2795:\Theta_\cA \text{ and its shadow tower}
chapters/theory/higher_genus_modular_koszul.tex:3152:\index{random matrix theory!shadow tower}
chapters/theory/higher_genus_modular_koszul.tex:3973:\label{rem:non-circular-logical-chain}
chapters/theory/higher_genus_modular_koszul.tex:3974:\index{logical foundation!non-circular chain}
chapters/theory/higher_genus_modular_koszul.tex:4028:The non-circular chain is:
chapters/theory/higher_genus_modular_koszul.tex:11956:\index{Brown--Henneaux!shadow tower reading}
chapters/theory/higher_genus_modular_koszul.tex:12637:\index{inverse limit!shadow tower}
chapters/theory/higher_genus_modular_koszul.tex:15015:\index{Linfty@$L_\infty$-formality!shadow tower identification}
chapters/theory/higher_genus_modular_koszul.tex:15085:\index{formality!shadow tower dictionary}
chapters/theory/higher_genus_modular_koszul.tex:15457:\index{Linfty@$L_\infty$-formality!shadow tower identification!higher degrees}
chapters/theory/higher_genus_modular_koszul.tex:15769:\emph{extinct}: it contributes nothing to the shadow tower
chapters/theory/higher_genus_modular_koszul.tex:15783:\emph{infinite} shadow tower is controlled by the critical
chapters/theory/higher_genus_modular_koszul.tex:15984:\index{shadow tower!sign alternation!mechanism}
chapters/theory/higher_genus_modular_koszul.tex:16064:\index{rationality!shadow tower}
chapters/theory/higher_genus_modular_koszul.tex:16297:only if the shadow tower terminates, if and only if the associated
chapters/theory/higher_genus_modular_koszul.tex:16308:\index{Maurer--Cartan space!shadow tower as Taylor expansion}%
chapters/theory/higher_genus_modular_koszul.tex:16329: The shadow tower is a single Gaussian integral.
chapters/theory/higher_genus_modular_koszul.tex:16374: particles. The shadow tower terminates because there are no
exec
/bin/zsh -lc "sed -n '3968,4048p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2718,2820p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
The MC element
$\Theta_\cA := D_\cA - \dzero \in
\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_\cA)$
exists at all genera by Theorem~\ref{thm:mc2-bar-intrinsic},
with no Koszulity hypothesis beyond the existence of the
genus-completed bar differential~$D_\cA$. The following are
projections of this single element and require no additional
input:
 succeeded in 51ms:
 $\kappa(\cA \otimes \cB) = \kappa(\cA) + \kappa(\cB)$.
 Combined with~(iii), the vanishing
 $\kappa_{\mathrm{tot}} = 0$ for a tensor product
 $\cA \otimes \cA^!_{\mathrm{ghost}}$ is the algebraic
 form of anomaly cancellation.
\end{enumerate}
\end{theorem}

\begin{proof}
The dependency route is one-way: the bar-intrinsic shadow tower of
Theorem~\ref{thm:mc2-bar-intrinsic} produces the scalar trace,
Theorem~\ref{thm:genus-universality} identifies that trace with
$\kappa(\cA)\lambda_g$, and Theorem~\ref{thm:family-index} is only the
subsequent GRR repackaging of the resulting genus series.
Part~(i) is Theorem~\ref{thm:genus-universality} for
uniform-weight algebras. For multi-generator algebras
($\mathcal{W}_N$, $N \geq 3$), only the genus-$1$ factorization
is unconditional; the higher-genus extension is conditional on the
strong scalar ansatz of
Theorem~\ref{thm:multi-generator-universality}.

thinking
**Locating concordance entries**

I need to find concordance entries related to topologization and Koszul equivalences. My focus is on theorem references like "thm:koszul-equivalences." I'll search within concordance entries using specific labels or mentions to streamline my findings. To accomplish this, I'll utilize tools like rg and sed for efficient searching and extraction. Let's see how that goes!
exec
/bin/zsh -lc "sed -n '11100,11255p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"thm:koszul-equivalences-meta|Koszul equivalences|\\(vii\\)|\\(viii\\)\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8780,8895p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1992:Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
2385:Theorem~\ref{thm:koszul-equivalences-meta} in
3156: & \texttt{thm:koszul-equivalences-meta}
9601: \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
9719: Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
10221: (item~(xii) of Theorem~\ref{thm:koszul-equivalences-meta}).
 succeeded in 51ms:
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 These are different objects produced by different
 functors.
 \emph{Violated anti-pattern}:
 (three functors, three outputs:
 bar~$\neq$ Verdier dual~$\neq$ cobar).

\item \textbf{``The boundary algebra is the
 primitive object.''}
 \emph{False.}
 The primitive object is the open-sector
 factorization dg-category
 $\mathcal{C}_{\mathrm{op}}$ on a tangential log
 curve $(X, D, \tau)$ with real-oriented blowup at
 each puncture, not on the ordinary curve~$X$.
 The boundary algebra
 $A_b = \mathrm{End}_{\mathcal{C}_{\mathrm{op}}}(b)$
 is an endomorphism algebra of a chosen
 boundary condition~$b$: a Morita-dependent chart,
 not the intrinsic datum.
 succeeded in 51ms:
\sqrt[N]{p/X}
\;\cong\;
\bigl[\operatorname{Spec}\bC[\![u]\!] \,/\, \mu_N\bigr]
\;\sqcup\;
(X \setminus \{p\}),
\end{equation}
where $u^N = t$ is the tautological $N$-th root
coordinate and $\mu_N$ acts by
$\zeta \cdot u = \zeta u$ for
$\zeta \in \mu_N = \langle e^{2\pi i/N}\rangle$.
The coarse moduli space of $X_{p,N}$ is~$X$ itself,
with the stacky structure concentrated at the single
point~$p$. The structure morphism
$\pi_N \colon X_{p,N} \to X$
is an isomorphism away from~$p$ and a
$\mu_N$-gerbe at~$p$. The orbifold line bundle
$\mathcal{L}_p^{1/N} := \pi_N^* \mathcal{O}_X(p)^{1/N}$
on~$X_{p,N}$ has the property that
$(\mathcal{L}_p^{1/N})^{\otimes N} \cong
\pi_N^* \mathcal{O}_X(p)$;
exec
/bin/zsh -lc "sed -n '3128,3188p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\toprule
\textbf{Item} & \textbf{Label} & \textbf{Location} \\
\midrule
PBW $E_2$-collapse
 & \texttt{thm:pbw-koszulness-criterion}
 & Ch.~\ref{chap:koszul-pairs} \\
Bar-cobar q.i.\
 & \texttt{thm:bar-cobar-inversion-qi}
 & Ch.~\ref{chap:bar-cobar-adjunction} \\
ChirHoch polynomial
 & \texttt{thm:main-koszul-hoch}
 & Ch.~\ref{chap:deformation-theory} \\
$A_\infty$ ($\Rightarrow$)
 & \texttt{prop:ainfty-formality-implies-koszul}
 & Ch.~\ref{chap:koszul-pairs} \\
$A_\infty$ ($\Leftarrow$)
 & \texttt{thm:ainfty-koszul-characterization}
 & Ch.~\ref{chap:koszul-pairs} \\
Ext diagonal
 & \texttt{thm:ext-diagonal-vanishing}
exec
/bin/zsh -lc "sed -n '9568,9738p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The following table classifies every major result
and programme by proof status.
\textsc{Green}: proved within this monograph
(local algebra, all hypotheses discharged).
\textsc{Amber}: externally supported or conditional
(physically motivated, with partial evidence,
but dependent on conjectural inputs or
physical interpretation).
\textsc{Red}: unproved global or modular descent
(genuine open problems with no current proof
strategy reducing to proved results).

\begin{center}
\renewcommand{\arraystretch}{1.25}
\small
\begin{tabular}{cp{10.5cm}}
\textbf{Status} & \textbf{Result} \\
\hline
\multicolumn{2}{l}{\textsc{Green}

thinking
**Exploring topologization needs**

I’m thinking it might be helpful to consider if I need status table lines around topologization. Maybe that would provide clarity in how everything is organized? I’ll also search within concordance to see if there are any specific references or insights I can find that relate to this. There’s definitely some value in exploring this further, especially if it can streamline the process. Let’s see what’s out there!
exec
/bin/zsh -lc 'rg -n "topologization|topologisation|thm:topologization|conj:topologization-general|conj:coderived-e3" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
7136:\ref{conj:coderived-e3}
7149: antighost field for topologization
7178: The topologization theorem
7179: (Theorem~\ref{thm:topologization}:
7183: topologization is conjectural
7184: (Conjecture~\ref{conj:coderived-e3} gives the
9533:SC self-duality retraction, topologization scoping, critical-level
9546:\item \textbf{FT-5} (topologization scope):
9748: \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\

thinking
**Clarifying label confusion**

I’m checking the concordance references to see why it still mentions conj:coderived-e3 instead of conj:topologization-general. Maybe there’s a label issue in the concordance that’s stale? I might just need to update statuses without changing the labels. However, the actual theorem file uses conj:topologization-general, so I should examine the context around 9533 to clarify any confusion. Let's figure this out!
exec
/bin/zsh -lc "sed -n '9738,9755p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9524,9568p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 complement of Koszul locus $=$ algebraic swampland
 \textup{(}Conjecture~\ref{conj:koszul-swampland}\textup{)} \\
& Shadow $s{=}1$ pole, quantum modularity,
 and volume growth
 \textup{(}Conjecture~\ref{conj:shadow-s1-quantum-volume}\textup{)} \\
& Page curve from Koszul complementarity
 \textup{(}Conjecture~\ref{conj:ent-page-curve}\textup{)} \\
& Ordered chiral center of the Yangian
 \textup{(}Conjecture~\ref{conj:yangian-ordered-center}\textup{)} \\
& Coderived $E_3$ without conformal vector
 \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
& Center essential surjectivity
 \textup{(}Conjecture~\ref{conj:center-essential-surjectivity}\textup{)}
\end{tabular}
\end{center}

% ----------------------------------------------------------------------
\subsection{The descent fan}
 succeeded in 52ms:
\textup{(}Remark~\textup{\ref{rem:shadow-radius-atlas}}).
Computational support from the engine
\texttt{modular\_shadow\_tower} (104~tests).
\end{remark}

% ----------------------------------------------------------------------
\paragraph{April 2026 session: falsification test results.}
Five additional falsification tests were evaluated against this
session's structural corrections (AP165 operadic scoping,
SC self-duality retraction, topologization scoping, critical-level
Theorem~H failure).
\begin{itemize}
\item \textbf{FT-2} (bar complex cooperad structure):
 \emph{passed}. The bar complex $\barB(\cA)$ is confirmed as an
 $E_1$ coassociative coalgebra over $(\mathrm{ChirAss})^!$,
 not an $\SCchtop$-coalgebra (AP165).
\item \textbf{FT-4} (Theorem~H generic-level requirement):
 \emph{passed}. At critical level $k = -h^\vee$,
 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
 (Feigin--Frenkel center); Theorem~H does not apply.
exec
/bin/zsh -lc "sed -n '2360,2405p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{proposition}


%% ====================================================================
%% INTRINSIC KOSZULNESS: THE CHARACTERIZATION PROGRAMME
%% ====================================================================
\section{Intrinsic Koszulness: the characterization programme}
\label{sec:concordance-koszulness-programme}
\index{Koszul property!characterization programme|textbf}
\index{chiral Koszulness!intrinsic characterization|textbf}

The PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion})
detects chiral Koszulness for every standard family but does
not characterize it intrinsically. This section is the
constitutional index for the intrinsic characterization
programme. Full statements and proofs live in the source
chapters cited below.

%% ------------------------------------------------------------------
\subsection{The meta-theorem: twelve characterizations}
exec
/bin/zsh -lc "sed -n '2405,2478p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Converse via Keller classicality.
 \hfill \checkmark
\item\label{item:kp-ext}
 Ext diagonal: $\operatorname{Ext}^{p,q}_\cA(\omega_X,\omega_X)=0$ for $p \neq q$
 (Theorem~\ref{thm:ext-diagonal-vanishing}).
 Off-diagonal $d_r$ contradicts concentration.
 \hfill \checkmark
\item\label{item:kp-barcobar}
 Bar-cobar counit $\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism
 (Theorem~\ref{thm:bar-cobar-inversion-qi}).
 \hfill \checkmark
\item\label{item:kp-barrbeck}
 Barr--Beck--Lurie comparison for $\barBch \dashv \Omegach$ is an equivalence
 (Theorem~\ref{thm:barr-beck-lurie-koszulness}).
 Conservativity + totalization on log-FM strata.
 \hfill \checkmark
\item\label{item:kp-facthom}
 Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
 (Theorem~\ref{thm:fh-concentration-koszulness}).
 Bar = FH; genus-$0$ concentration forces $E_2$-collapse.

thinking
**Updating equivalence conditions**

I need to update the conditional and partial text for items (vii) and (viii). The user noted that (vii) applies when g=0 only, while (viii) is a weakened version. Currently, the unconditional equivalences (i)-(x) include all smooth X for (vii) and polynomial vanishing outside of {0,1,2} for (viii). I need to make minimal edits to clarify both points. First, I should check the actual theorem file for the precise truth. I'll look into chiral_koszul_pairs.tex for specific definitions.
codex
I’ve got the stale surfaces: the concordance still treats `(vii)` and `(viii)` as unconditional, and the topologization block is using older generic wording. I’m reading the exact meta-theorem statement now so I can weaken only the affected clauses, not the surrounding programme summary.
exec
/bin/zsh -lc "sed -n '2078,2145p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2012,2078p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"weakened|Condition~\\textup\\{\\(viii\\)\\}|(viii) is a proved consequence|viii\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/introduction.tex chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Corollary~\ref{cor:minimal-orbit-koszul}.
\end{remark}

\begin{theorem}[Equivalences and consequences of chiral Koszulness; \ClaimStatusProvedHere]
\label{thm:koszul-equivalences-meta}
\index{Koszul property!equivalences of characterizations|textbf}

Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
with PBW filtration $F_\bullet$.
Conditions \textup{(i)--(vii)} and \textup{(ix)--(x)} below are
equivalent. Condition~\textup{(viii)} is a proved consequence of
them on the Koszul locus.
Under the additional perfectness and non-degeneracy hypotheses on the
ambient tangent complex, condition~\textup{(xi)} is also equivalent to
them. Condition~\textup{(xii)} implies condition~\textup{(x)}
(Remark~\ref{rem:d-module-purity-content}); the converse is open.

\smallskip
\noindent\textbf{Unconditional equivalences:}
\begin{enumerate}
 succeeded in 51ms:
 $\cM_{\cA^!}$ are transverse Lagrangians in the $(-1)$-shifted
 symplectic deformation space~$\cM_{\mathrm{comp}}$.
\item[\textup{(xii)}] $\mathcal{D}$-module purity: each
 $\barBgeom_n(\cA)$ is pure of weight~$n$ as a mixed Hodge module,
 with characteristic variety aligned to FM boundary strata.
\end{enumerate}
\end{theorem}

\begin{proof}
\textsc{The core circuit}
\textup{(i)}$\Leftrightarrow$\textup{(ii)}$\Leftrightarrow$%
\textup{(iii)}$\Leftrightarrow$\textup{(v)}:

\smallskip\noindent
\textup{(i)}$\Leftrightarrow$\textup{(ii)}:
Koszulness (Definition~\ref{def:chiral-koszul-morphism}) is
acyclicity of $\barBgeom(\cA) \otimes_\tau \cA$ in positive degrees.
Theorem~\ref{thm:pbw-koszulness-criterion} identifies this with
$E_2$-collapse; the converse is immediate.

 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:2022:equivalent. Condition~\textup{(viii)} is a proved consequence of
chapters/theory/chiral_koszul_pairs.tex:2064:\item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is concentrated in
chapters/theory/chiral_koszul_pairs.tex:2114:\textup{(v)}$\Rightarrow$\textup{(viii)}:
chapters/theory/chiral_koszul_pairs.tex:2123:\textup{(viii)} to the bar-cobar counit is proved here.
chapters/theory/chiral_koszul_pairs.tex:2849:consequence~\textup{(viii)} have been verified
chapters/theory/chiral_koszul_pairs.tex:3144:and the Hochschild consequence~\textup{(viii)} no longer follows.
chapters/frame/preface.tex:3395:\Leftrightarrow \textup{(viii)}$,
chapters/frame/preface.tex:3429:Item~(viii) of the meta-theorem asserts that chiral Hochschild

thinking
**Searching for references**

I think I should dive into the concordance and look for mentions of terms like "10 unconditional" and "1 conditional." I see there are some hits around line 1992, and I wonder if there might be even more references elsewhere. It's a good idea to explore this thoroughly to get a clearer understanding of the context. Let’s see if I can uncover additional details that could help clarify these concepts!
exec
/bin/zsh -lc "rg -n \"10 unconditional|1 conditional|one-directional|Koszulness programme|equivalences \\+|equivalence\\)|equivalences\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1564: (bar-cobar Quillen equivalence)
1991:(10 unconditional, 1 conditional, 1 one-directional;
1992:Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
2381:\index{Koszul property!equivalences|textbf}
2385:Theorem~\ref{thm:koszul-equivalences-meta} in
2392:\textbf{Unconditional equivalences} (i)--(x):
2461: \hfill (\emph{one-directional}; $(\ref{item:kp-fmbdy})\Rightarrow(\ref{item:kp-dmod})$ proved, converse open)
3156: & \texttt{thm:koszul-equivalences-meta}
3197:\emph{Status}: ten equivalences
3204:one-directional (forward direction proved, converse open).
8299:(Proposition~\ref{prop:hecke-defect-equivalences},
9598:& Koszulness programme: $10$ unconditional
9599: equivalences $+$ $1$ conditional (Lagrangian)
9600: $+$ $1$ one-directional (D-module purity)
9601: \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
9719: Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
10216:\subsection{Koszulness programme}
10221: (item~(xii) of Theorem~\ref{thm:koszul-equivalences-meta}).
exec
/bin/zsh -lc "sed -n '3188,3210p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10192,10235p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Graph-complex shadow
 & \texttt{conj:graph-complex-shadow}
 & Ch.~\ref{chap:deformation-theory}
 \emph{(Heuristic: map $\Phi$ not rigorously constructed)} \\
\bottomrule
\end{tabular}
\end{center}

\noindent
\emph{Status}: ten equivalences
(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
unconditional for the standard landscape
(Proposition~\ref{prop:lagrangian-perfectness} verifies
perfectness at non-critical, non-degenerate levels);
$\mathcal{D}$-module purity~(\ref{item:kp-dmod})
one-directional (forward direction proved, converse open).
Two further characterizations, tropical Koszulness
(Theorem~\ref{thm:tropical-koszulness}) and
bifunctor obstruction decomposition
 succeeded in 52ms:
 Proved for semisimple Frobenius data
 (Theorem~\ref{thm:planted-forest-structure}(vi))
 via the Givental--Teleman--PPZ chain. Open for non-semisimple
 data (logarithmic/admissible algebras).

 \smallskip\noindent
 \emph{Strategy from $\Theta^{\mathrm{oc}}$.}
 The open sector of $\Theta^{\mathrm{oc}}_\cA$
 provides boundary-marked tautological classes
 $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
 strictly richer than the closed-sector classes.
 The four-sector decomposition of the MC equation
 produces relations with both interior and boundary
 markings. These additional relations may generate
 the full Pixton ideal even when the
 closed-sector relations alone do not, because the
 open sector accesses descendant pairings (e.g.\
 $\int_{\overline{\mathcal{M}}_{2,1}}
 \delta_{\mathrm{pf}}\,\psi_1^2$) that reveal
 shadow coefficients invisible in the closed
exec
/bin/zsh -lc "sed -n '9708,9726p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
& Pixton ideal generation from class-M shadows
 \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)} \\
& Arithmetic Langlands bridge:
 arithmetic descent from function field to
 number field
 \textup{(}Remark~\ref{rem:langlands-gap-b}\textup{)} \\
& Modular periodicity for simple quotients at
 admissible levels
 \textup{(}Conjecture~\ref{conj:modular-periodicity-minimal}\textup{)} \\
& D-module purity: converse direction
 \textup{(}item~(xii) of
 Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
& Shadow principal class: whether $Q_L$ always
 represents the principal ideal class
 \textup{(}Conjecture~\ref{conj:shadow-principal-class}\textup{)} \\
& Non-lattice $L$-function descent:
 sewing lift $\to$ $L$-function content for
 non-lattice algebras
 \textup{(}\S\ref{subsec:concordance-descent-fan}\textup{)} \\
exec
/bin/zsh -lc "sed -n '5200,5315p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6208,6255p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
follows from the functoriality of $\kappa$ (determined by
genus-$1$ curvature) and $\mathbb{E}$ (determined by the
universal curve).

\emph{What remains.}
The theorem identifies $\mathcal{D}_{\cA}^{(g)}$ via its top Chern
class (the obstruction). A stronger result would construct
$\mathcal{D}_{\cA}^{(g)}$ as a \emph{sheaf} on
$\overline{\mathcal{M}}_g$ (rather than a $K$-theory class) and
identify its full Chern character with the genus expansion at all
intermediate degrees, not only the top. This would require the
coderived Ran-space formalism of
\S\ref{sec:modular-koszul-programme} and is the subject of
Theorem~\ref{thm:universal-MC}.
\end{remark}

\begin{remark}[The GRR theorem as synthesis]
\label{rem:grr-horizon}
\index{Grothendieck--Riemann--Roch!synthesis}
Theorem~\ref{thm:family-index} synthesizes the preceding results:
 succeeded in 52ms:
 every positive-definite even lattice admits a canonical sewing envelope
 with charge-refined Hilbert sectors. Proof: HS-sewing
 (Corollary~\ref{cor:hs-sewing-standard-landscape}),
 amplitude factorization as Heisenberg Fredholm determinant times
 Siegel theta function (classical convergence for
 $\operatorname{Im}\Omega > 0$), Bergman-space charge-sector completion.
\item \emph{Analytic realization criterion}
 (Conjecture~\ref{conj:analytic-realization}): a unitary full VOA
 satisfying conformal OS, polynomial spectral growth, and
 HS-sewing admits a sewing envelope, a conformally flat 2-disk
 algebra, and a higher-genus coderived shadow.
\item \emph{Boundary bar duality}
 (Conjecture~\ref{conj:boundary-bar-duality}): for an
 analytically Koszul~$\cA$, completed boundary modules at
 genus~$0$ are equivalent to analytic comodules over
 $\barB^{\mathrm{an}}(\cA)$; at curved genus, the correct
 objects are analytic contramodules over the curved dual.
\end{enumerate}

\noindent
exec
/bin/zsh -lc "rg -n \"label\\{thm:genus-universality\\}|Family index theorem|routing|circular|Theorem~\\\\ref\\{thm:family-index\\}|genus universality theorem\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
691: The genus universality theorem shows that these two perspectives
4871:\emph{Non-circular logical chain.}
4873:is free of circularity
4874:(Remark~\ref{rem:non-circular-logical-chain}).
4898:Remark~\ref{rem:non-circular-logical-chain}).
5927:\begin{theorem}[Family index theorem for genus expansions;
6010:The genus universality theorem
exec
/bin/zsh -lc "sed -n '4828,4908p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The bar-cobar adjunction is an equivalence of
$\infty$-categories, the categorical $\exp/\log$ correspondence
(Remark~\ref{rem:nilpotence-periodicity}):
\[
\bar{B}_X \colon
\operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
\;\rightleftarrows\;
\operatorname{CoAlg}_{\mathrm{conil}}(\operatorname{Fact}(X))
\,:\!\Omega_X,
\]
where $\operatorname{Fact}(X)$ denotes factorization algebras on
$\operatorname{Ran}(X)$ (cf.\ Appendix~\ref{app:existence-criteria}).

On the Koszul locus this is an equivalence: $\exp \circ \log = \mathrm{id}$
on the convergence domain. When curvature is present (that is,
when the categorical logarithm acquires non-trivial monodromy), the
theorem-level statement moves from ordinary derived categories to the
intrinsic coderived/contraderived bar-coalgebra framework of
Positselski~\cite{Positselski11}. The logarithm/analytic-continuation
language is heuristic motivation only; the proved categorical content
exec
/bin/zsh -lc "sed -n '668,704p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chiral algebras and factorization algebras on curves (BD, Chapter~3).
The precise comparison:
\begin{enumerate}[label=(\roman*)]
\item \emph{Factorization homology.}
 The CG factorization homology $\int_X \cA$ computes the same object
 as our chiral homology $H_*(\bar{B}^{\mathrm{ch}}(\cA))$. Our explicit
 realization via configuration space integrals provides chain-level
 formulas that the CG framework treats abstractly.
\item \emph{Koszul duality.}
 The CG framework includes Koszul duality for factorization algebras
 (CG, Vol.~2, Chapter~5), specialized to holomorphic factorization
 algebras on curves. Their Koszul duality, restricted to this setting,
 recovers our chiral Koszul duality. Our contribution is the explicit
 identification of the Koszul dual for all standard families
 (Kac--Moody, Virasoro, $\mathcal{W}_N$, etc.) via the bar-cobar
 adjunction on Fulton--MacPherson spaces.
\item \emph{Quantum corrections.}
 The CG perturbative quantization framework produces $A_\infty$
 structures from Feynman diagram expansions (CG, Vol.~2, Chapter~3).
 Our curved $A_\infty$ structure on the bar complex is the

thinking
**Searching for theorem information**

I'm considering whether to add a routing remark. The user seems to want a search for labels related to genus-universality theorems. I should locate the specific theorem statement but not directly search around 5243 because that's a bit uncertain. Instead, it might be more effective to open up around 5400 instead. Let's see what I can find and refine my search from there!
exec
/bin/zsh -lc "rg -n \"genus universality|label\\{thm:genus-universality\\}|genus-universality}\" chapters/connections/concordance.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
62: \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
290: (Theorem~\ref{thm:genus-universality}).}
641: (Theorem~\ref{thm:genus-universality}), which extends the FF involution
691: The genus universality theorem shows that these two perspectives
5280:(Theorem~\ref{thm:genus-universality}).
5287:(Theorem~\ref{thm:genus-universality}). The clutching compatibility
5412:$\kappa(\cA) \cdot \lambda_g$ (proved, Theorem~\ref{thm:genus-universality}).
5992:\textup{(}Theorem~\textup{\ref{thm:genus-universality}(ii))}
6010:The genus universality theorem
6011:(Theorem~\ref{thm:genus-universality}) establishes for
6201:in this monograph (genus universality,
6202:Theorem~\ref{thm:genus-universality}) and imported results
6466:genus~$1$ (Theorem~\ref{thm:genus-universality}).
9616: \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
11204: (Theorem~\ref{thm:genus-universality}).

thinking
**Evaluating the theorem connection**

I’m considering how to relate the theorem family-index, which seems to be linked to genus-universality and shadow tower. The user mentioned searching for both theorems and to add routing remarks to break the circular dependency. I’ll focus on the non-circular path that goes from shadow tower to universality and then to family index. It’s interesting how these concepts connect, and I'll need to ensure I represent this correctly for clarity.
exec
/bin/zsh -lc "sed -n '7118,7156p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \textup{(}Proposition~\ref{prop:ds-chirhoch-compatibility}\textup{)}
 & BRST complex $+$ HPL transfer \\
\ref{prop:ker-av-schur-weyl}
 & Kernel of averaging: $\dim\ker(\mathrm{av}_n) = n! - \binom{n+d-1}{n}$
 closed formula via Schur--Weyl
 \textup{(}Proposition~\ref{prop:ker-av-schur-weyl}\textup{)}
 & Schur--Weyl duality $+$ symmetric group characters \\
\ref{prop:e1-obstruction-categorical}
 & $E_1$-obstruction is categorical:
 $E_1 \not\to E_2$ promotion obstructed by
 non-trivial Drinfeld associator
 \textup{(}Proposition~\ref{prop:e1-obstruction-categorical}\textup{)}
 & associator $+$ monodromy \\
\ref{conj:yangian-ordered-center}
 & Ordered chiral center of the Yangian:
 derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
 as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
 & standalone paper, \S\ref{sec:e1-yangian} \\
\ref{conj:coderived-e3}
 & Coderived $E_3$: $D^{\mathrm{co}}$-level $E_3$ on



thinking
**Considering the mathematical conjecture**

I'm reflecting on the `conj:coderived-e3` which seems different from what I expected. It’s not a general topologization conjecture, and it looks like the outdated reference to block 7178 needs updating. I might need to shift to `conj:topologization-general`, but I'm unsure if the concordance includes this label.

I think I'll check the label's existence in the repository and update accordingly, though I wonder if it’s necessary to edit the summary tables. I'll search for more information around 7178 and FT-5.
thinking
**Deciding on updates**

I need to decide on several updates regarding specific blocks and lines, like 7178 and 9546 in FT-5. I'm wondering if I really need to mention "topologization" in the label table. Perhaps using "antighost field for topologization" is sufficient. 

I should also check early sections for cross-references, and I found five hits so far. I’m thinking about changing the phrase at line 7179 to ensure correctness, especially since AGENTS clarify that it's not E3-chiral. Then I’ll look for mentions of MC5 throughout the document to make sure summaries are accurate.
thinking
**Searching for MC5 summaries**

I think some information might be outdated, so I need to search within the concordance for any mentions of `MC5` and check the status summaries to ensure they're accurate. I'll look for around 20 hits, which should give me a good overview. Once I have those, I'll inspect the details to confirm they're all up-to-date and relevant. It's essential to ensure everything reflects the correct information for clarity!
exec
/bin/zsh -lc 'rg -n "MC5" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1943:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
1981:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
2889: & analytic bar coalgebra (MC5) \\[2pt]
3285:MC5 & Genus tower & Five components:
4432: & MC5 sewing programme,
4661:genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
6687: sewing (MC5). The integer-$n$ construction is well-defined from the
9593:& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
11128: MC1 through MC4 are proved. MC5 is only partially
exec
/bin/zsh -lc "sed -n '11096,11152p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9578,9605p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 = H^*(C^\bullet_{\mathrm{ch}}(\cA, \cA), \delta)$,
 which classifies bulk operators acting on the
 boundary
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 These are different objects produced by different
 functors.
 \emph{Violated anti-pattern}:
 (three functors, three outputs:
 bar~$\neq$ Verdier dual~$\neq$ cobar).

\item \textbf{``The boundary algebra is the
 primitive object.''}
 \emph{False.}
 The primitive object is the open-sector
 factorization dg-category
 $\mathcal{C}_{\mathrm{op}}$ on a tangential log
 curve $(X, D, \tau)$ with real-oriented blowup at
 each puncture, not on the ordinary curve~$X$.
 The boundary algebra
 succeeded in 51ms:
(genuine open problems with no current proof
strategy reducing to proved results).

\begin{center}
\renewcommand{\arraystretch}{1.25}
\small
\begin{tabular}{cp{10.5cm}}
\textbf{Status} & \textbf{Result} \\
\hline
\multicolumn{2}{l}{\textsc{Green}
 \textup{(proved local algebra)}} \\[2pt]
& Theorems A--H
 (bar-cobar adjunction, inversion,
 complementarity, modular characteristic,
 Hochschild) \\
& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
 strong completion towers, HS-sewing) \\
& MC3 proved for all simple types on the
 evaluation-generated core; DK-4/5
 (extension beyond evaluation modules) downstream \\


thinking
**Updating summaries for accuracy**

I need to update some stale summaries in our search results for clarity. So, I'm checking which hits are outdated. Line 1943 is already correct, and line 1981 is fine as it is. Line 3285's table is correct too, but I found line 11128 is outdated. Line 9593’s table is misleading since it suggests MC5 is fully proved. I think updating it to clarify what "proved lanes of MC5" actually means would help. I’ll likely need two or three edits overall.
thinking
**Considering routing edits**

I think it might be better to edit the existing remark instead of adding something new since the user requested a "routing remark." I can update the remark about "The GRR theorem as synthesis" to include a routing line that references `thm:family-index`. By adding a simple line, like `\emph{Routing.} The non-circular dependency route is ...`, I can avoid creating new labels and satisfy the user's request. However, I also need to consider the search for both labels.
exec
/bin/zsh -lc "sed -n '6188,6234p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(1 - \hbar^2/4n^2\pi^2)^{-1}$.
At genus~$1$, the same scalar formula holds for every modular Koszul
algebra. For uniform-weight algebras the genus-$2$ ratio
$F_2/F_1 = 7/240$ is universal;
the ratio $F_2/F_1^2 = 7/(10\kappa)$ is perturbative
in $1/\kappa$. Shadow corrections beyond the scalar
sector enter as multiplicative deformations governed by
the MC equation, not by the KdV hierarchy
(Remark~\ref{rem:shadow-multiplicative-deformation}).
\end{remark}

\begin{remark}[Scope]\label{rem:family-index-scope}
Steps~1--3 of the proof use only results established
in this monograph (genus universality,
Theorem~\ref{thm:genus-universality}) and imported results
(Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
\cite{FP03}). Step~4 is classical generating function analysis.
The identification $\mathcal{D}_{\cA}^{(g)} =
\kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
universality theorem; the functoriality of the construction


thinking
**Evaluating search methods**

I wonder if we've already run a manual search. Maybe it would have been better to use a tool instead. I could still think about spawning an explorer to verify any stale spots, but I'm not sure if that’s overdoing it. The instruction to always prefer explorer checks over manual searches is important to remember. I should ask the explorers directly and precisely instead of re-reading or re-searching the code they cover.
thinking
**Identifying stale data**

I’m thinking about asking the explorer to pinpoint the exact stale entries. I need to determine the minimal change boundaries as well. It seems like a practical approach to address any issues I'm facing with outdated information. By being precise about those boundaries, I hope to ensure that any updates are both effective and efficient. Alright, let's move forward with this plan!
codex
I’ve isolated the likely stale spots. Before patching, I’m doing one independent pass to confirm that I only touch the constitution entries that actually drifted.
collab spawn_agent(call_iMHVZ2eBYEwZ9mX2XOgkHLF1, prompt="<task>Audit only chapters/connections/concordance.tex for four requested surgical fixes: (1) routing remark for thm:fami…")
spawn_agent(call_iMHVZ2eBYEwZ9mX2XOgkHLF1, prompt="<task>Audit only chapters/connections/concordance.tex for four requested surgical fixes: (1) routing remark for thm:fami…") pending init:
  agent: 019d862f-2eff-7170-844b-71620159f877
mcp startup: no servers
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
exec
/bin/zsh -lc 'rg -n "thm:family-index|thm:genus-universality|topologization|MC5|Koszul" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
38: on the Koszul locus
56: for uniform-weight modular Koszul algebras
62: \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
66: $P(t)=1+t^2$, Koszul-functorial;
121: modular Koszul algebras (Theorem~H).
163:polynomial consequence of Koszul functoriality.
189: For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ partition
217:Classical Koszul duality (Priddy; Beilinson--Ginzburg--Soergel)
246:\textbf{Shadow depth classifies complexity within the Koszul world.}\enspace
247:Within the chirally Koszul standard examples treated in
252:Koszulness status:
269: for all Koszul chiral algebras at all genera. Inversion is
290: (Theorem~\ref{thm:genus-universality}).}
291: For a Koszul chiral algebra~$\cA$ with uniform-weight
323: For a Koszul pair $(\cA, \cA^!)$, the genus-$g$ obstructions
326: The Kodaira--Spencer map is constructed for all Koszul pairs
329:\item \emph{$\Eone$-chiral Koszul duality
337: Complete Koszul duality computations for all standard families:
348: Koszul despite nonvanishing $H^2_{\mathrm{CE}}$\textup{)},
393: Functorial under Koszul duality via the Connes
exec
/bin/zsh -lc 'rg -n "shadow tower" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
4337:\paragraph{Three-lens identification of the shadow tower.}
7875:\index{shadow tower!orthogonal to critical level|textbf}
7977:\index{isomonodromic deformation!shadow tower}%
7978:\index{shadow tower!isomonodromic deformation}%
7979:\index{Gaudin Hamiltonian!shadow tower}%
8109:\index{shadow tower!convergence}%
exec
/bin/zsh -lc "sed -n '4310,4370p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\ChirHoch^{\bullet}(\cA) \cong
(\mathbb{D}_{\Ran}\barB(\cA))_{\Sigma}$,
on the Koszul locus. This identification was implicit in
the original Theorem~H proof; the lemma makes it citable
as a primitive step (A2).

\paragraph{Closure properties of chiral Koszulness.}
Proposition~\ref{prop:koszul-closure-properties} consolidates
three previously scattered facts: the class of chirally Koszul
algebras is closed under chiral tensor product
($(\cA \boxtimes \cB)^! \simeq \cA^! \boxtimes \cB^!$),
Koszul dualization (involutivity: $(\cA^!)^! \simeq \cA$),
and base change along finite \'etale covers of curves.
Quotients (e.g.\ Drinfeld--Sokolov reduction) are
\emph{not} in the closure and require
Theorem~\ref{thm:w-algebra-koszul} (A6).

\paragraph{Kac--Moody $\cD$-module purity equivalence.}
Proposition~\ref{prop:d-module-purity-km-equivalence}
proves the full equivalence between chiral Koszulness and
exec
/bin/zsh -lc "sed -n '4670,4750p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
complex $\mathrm{Def}_{\mathrm{cyc}}^{\mathrm{mod}}(V)$,
and the genus-$1$ obstruction is the variational modular class
$\mathrm{Mod}(V) = [\Delta_{\mathrm{cyc}} P_\Pi]$.
For the $\mathcal{W}_3$ PVA, $\mathrm{Mod}(V) = 0$
(Volume~II, Theorem~N). The lift freedom is one-dimensional,
generated by the central-parameter direction: the unique
deformation that produces the quantized $\mathcal{W}_3$
at central charge $c = c(k)$. This connects Volume~II's
PVA descent (Theorem~G) with Volume~I's shadow obstruction tower
(the degree-$2$ projection $\Theta_\cA^{\leq 2}$ recovers
the modular characteristic $\kappa(\cA)$, which is the
quantized value of the classical variational class).
\end{remark}


\section[Towards modular homotopy theory]{Towards modular homotopy theory for factorization algebras on curves}
\label{sec:modular-koszul-programme}
\index{modular Koszul duality!project}

The modular characteristic theorem (Theorem~D,
exec
/bin/zsh -lc "sed -n '5900,6005p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc 'rg -n "genus-universality" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
62: \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
290: (Theorem~\ref{thm:genus-universality}).}
641: (Theorem~\ref{thm:genus-universality}), which extends the FF involution
5280:(Theorem~\ref{thm:genus-universality}).
5287:(Theorem~\ref{thm:genus-universality}). The clutching compatibility
5412:$\kappa(\cA) \cdot \lambda_g$ (proved, Theorem~\ref{thm:genus-universality}).
5992:\textup{(}Theorem~\textup{\ref{thm:genus-universality}(ii))}
6011:(Theorem~\ref{thm:genus-universality}) establishes for
6202:Theorem~\ref{thm:genus-universality}) and imported results
6466:genus~$1$ (Theorem~\ref{thm:genus-universality}).
9616: \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
11204: (Theorem~\ref{thm:genus-universality}).
exec
/bin/zsh -lc "sed -n '5980,6040p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
where the function $(x/2)/\sin(x/2)$ arises from
$\operatorname{Td}(T_\pi) = c_1(\omega_\pi)/(1 - e^{-c_1(\omega_\pi)})$
in the GRR formula, Wick-rotated by the positivity of
tautological intersection numbers on
$\overline{\mathcal{M}}_g$.

\item \emph{Verdier compatibility.}
Under Koszul duality $\cA \leftrightarrow \cA^!$,
$\mathcal{D}_{\cA^!}^{(g)} = \kappa(\cA^!) \cdot \mathbb{E}$,
and the complementarity
$\kappa(\cA) + \kappa(\cA^!) = \kappa_{\mathrm{total}}$
\textup{(}Theorem~\textup{\ref{thm:genus-universality}(ii))}
gives
\[
F_g(\cA) + F_g(\cA^!)
\;=\;
\kappa_{\mathrm{total}} \cdot \lambda_g^{\mathrm{FP}},
\]
the ``index-theoretic complementarity'': the total genus expansion
exec
/bin/zsh -lc "sed -n '7140,7205p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 & \S\ref{sec:en-koszul-duality} \\
\ref{conj:center-essential-surjectivity}
 & Center essential surjectivity:
 every $E_2$-chiral algebra arises as a derived center
 \textup{(}Conjecture\textup{)}
 & \S\ref{sec:en-koszul-duality} \\
\ref{constr:sugawara-antighost}
 & Sugawara antighost construction:
 conformal vector at non-critical level yields
 antighost field for topologization
 & \S\ref{sec:en-koszul-duality} \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: AP165 bar-complex operadic correction}} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{AP165 correction (constitutional).}
 The bar complex $\barB(\cA)$ is an $E_1$ coassociative
 coalgebra over $(\mathrm{ChirAss})^!$, the Koszul dual
 cooperad of the chiral associative operad.
codex
I’ve narrowed the patch to a handful of concordance summaries plus the family-index scope remark. I’m checking the count drift around the Koszul meta-theorem before I edit, because weakening `(viii)` forces the headline counts to change anywhere this file still says “10 unconditional”.
collab wait(call_VnRhzOiI8RIdS00QDVgKbdo6)
  receivers: 019d862f-2eff-7170-844b-71620159f877
exec
/bin/zsh -lc 'rg -n "MC5" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1943:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
1981:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
2889: & analytic bar coalgebra (MC5) \\[2pt]
3285:MC5 & Genus tower & Five components:
4432: & MC5 sewing programme,
4661:genus (MC5, Conjecture~\ref{conj:master-bv-brst}).
6687: sewing (MC5). The integer-$n$ construction is well-defined from the
9593:& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
11128: MC1 through MC4 are proved. MC5 is only partially
exec
/bin/zsh -lc "sed -n '1930,2100p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 algebra family beyond the standard landscape, one must
 verify that its coefficient sequences stabilize on finite
 windows and identify the H-level target. This is a
 finite computation for each family, not a theoretical
 gap.
 \emph{Arithmetic connection}: the spectral curve of the shadow
 Higgs field
 (Theorem~\ref{thm:shadow-higgs-field}) has convergence
 radius $|c|/3$ in the degree variable;
 the MC4 completion radius is controlled by the same parameter
 $\lambda_{\mathrm{eff}} = -6/c$
 (Chapter~\ref{chap:arithmetic-shadows},
 Remark~\ref{rem:effective-coupling}).
\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
 Inductive genus
 determination, 2D convergence (no UV renormalization needed),
 analytic-algebraic comparison, and the general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
 plus subexponential sector growth implies convergence at all genera).
 Heisenberg sewing proved (Theorem~\ref{thm:heisenberg-sewing}:
exec
/bin/zsh -lc "sed -n '11090,11170p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \emph{twisting morphisms}:
 algebraic maps $\tau \colon \barB(\cA) \to \cA$
 controlling the coupling between~$\cA$ and its
 Koszul dual~$\cA^!$.
 The bulk algebra is the
 \emph{chiral derived center}
 $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 = H^*(C^\bullet_{\mathrm{ch}}(\cA, \cA), \delta)$,
 which classifies bulk operators acting on the
 boundary
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 These are different objects produced by different
 functors.
 \emph{Violated anti-pattern}:
 (three functors, three outputs:
 bar~$\neq$ Verdier dual~$\neq$ cobar).

\item \textbf{``The boundary algebra is the
 primitive object.''}
 \emph{False.}
exec
/bin/zsh -lc 'rg -n "Koszul equivalences" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '3030,3095p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{Robert-Nicoud--Wierstra!bifunctor obstruction}
\index{Koszul property!bifunctor obstruction}

The RNW no-bifunctor obstruction \cite{RNW19}
(\S\ref{sec:concordance-three-pillars}, identification
theorem~7) is structural: $\operatorname{hom}_\alpha(
\mathcal{C},\mathcal{A})$ extends to $\infty$-morphisms in
either slot separately but not both. Koszulness does not kill
it; Koszulness makes it irrelevant by factoring all
constructions one slot at a time
(Theorem~\ref{thm:quillen-equivalence-chiral}). This is why
the MC3 strategy
(Theorem~\ref{thm:mc3-type-a-resolution}) succeeds.
\label{rem:concordance-bifunctor-koszul}


%% ------------------------------------------------------------------
\subsection{Computational diagnostics}
\label{subsec:concordance-computational-diagnostics}
\index{Koszul property!computational diagnostics}
exec
/bin/zsh -lc "rg -n \"\\(vii\\)\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '10200,10340p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 provides boundary-marked tautological classes
 $\operatorname{taut}_{g,n}^{\mathrm{oc}}$, which are
 strictly richer than the closed-sector classes.
 The four-sector decomposition of the MC equation
 produces relations with both interior and boundary
 markings. These additional relations may generate
 the full Pixton ideal even when the
 closed-sector relations alone do not, because the
 open sector accesses descendant pairings (e.g.\
 $\int_{\overline{\mathcal{M}}_{2,1}}
 \delta_{\mathrm{pf}}\,\psi_1^2$) that reveal
 shadow coefficients invisible in the closed
 $(g,0)$ projection.

\end{enumerate}

\subsection{Koszulness programme}

\begin{enumerate}[resume, label=\textup{(\arabic*)}]

exec
/bin/zsh -lc "rg -n \"\\\\begin\\{enumerate\\}\\[resume\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "rg -n \"item~\\(vii\" -n chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "koszul-equivalences" -i chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1992:Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
2385:Theorem~\ref{thm:koszul-equivalences-meta} in
3156: & \texttt{thm:koszul-equivalences-meta}
9601: \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
9719: Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
10221: (item~(xii) of Theorem~\ref{thm:koszul-equivalences-meta}).
exec
/bin/zsh -lc "sed -n '2350,2415p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The shadow obstruction tower
$\Theta_\cA^{\leq r}$ consists of finite-order truncations; the
obstruction classes~$o_{r+1}(\cA)$ classify shadow depth into the
four archetypes
$\mathsf{G}$/$\mathsf{L}$/$\mathsf{C}$/$\mathsf{M}$
(Theorem~\ref{thm:shadow-archetype-classification}).
The full MC element
$\Theta_\cA = \varprojlim \Theta_\cA^{\leq r}$ is proved by the
bar-intrinsic construction
(Theorem~\ref{thm:mc2-bar-intrinsic}).
\end{proposition}


%% ====================================================================
%% INTRINSIC KOSZULNESS: THE CHARACTERIZATION PROGRAMME
%% ====================================================================
\section{Intrinsic Koszulness: the characterization programme}
\label{sec:concordance-koszulness-programme}
\index{Koszul property!characterization programme|textbf}
\index{chiral Koszulness!intrinsic characterization|textbf}
wait(call_VnRhzOiI8RIdS00QDVgKbdo6) timed out:
exec
/bin/zsh -lc "sed -n '2415,2525p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \hfill \checkmark
\item\label{item:kp-barrbeck}
 Barr--Beck--Lurie comparison for $\barBch \dashv \Omegach$ is an equivalence
 (Theorem~\ref{thm:barr-beck-lurie-koszulness}).
 Conservativity + totalization on log-FM strata.
 \hfill \checkmark
\item\label{item:kp-facthom}
 Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
 (Theorem~\ref{thm:fh-concentration-koszulness}).
 Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
 \hfill \checkmark
\item\label{item:kp-hochschild}
 $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
 (Theorem~\ref{thm:main-koszul-hoch}).
 For single-generator algebras with no simple pole in the OPE,
 $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
 the zero mode is central); for algebras with simple poles,
 $\ChirHoch^1 = 0$ (all derivations inner).
 \hfill \checkmark
\item\label{item:kp-nullvec}

thinking
**Considering action steps**

It seems like the explorer timed out, which isn't ideal. I might need to poll again later, but for now, I should probably focus on the next steps. Should I consider using update_plan? Hmm, maybe not yet. I also want to remember to include a pre-edit verification block in the commentary before proceeding. Let's make sure I’m crafting my response well!
exec
/bin/zsh -lc "sed -n '2525,2685p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\neq 0$), and $f_\infty$ is the $L_\infty$-formality level
(largest $n$ with $\ell_n^{(0),\mathrm{tr}} \neq 0$ on
$\mathfrak{g}_\cA^{\mathrm{mod}}$).
\end{theorem}

\begin{proof}
The equality $r_{\max} = f_\infty$ is
Theorem~\ref{thm:shadow-formality-identification}:
the degree-$r$ shadow $\operatorname{Sh}_r(\cA)$ equals
$\ell_r^{(0),\mathrm{tr}}$ evaluated on the truncated
MC element at every degree, so $\operatorname{Sh}_r = 0$
iff $\ell_r^{(0),\mathrm{tr}} = 0$ on $H^*$.

For $f_\infty = d_\infty$: the cyclic deformation complex
$\Defcyc(\cA)$ carries both an $A_\infty$ structure
(from the bar differential) and an $L_\infty$ structure
(from the convolution bracket). On the genus-$0$ part,
the Lie bracket $[-,-]^{(0)}$ is the antisymmetrization
of the associative composition, so the transferred
brackets satisfy
codex
```text
scope: chapters/connections/concordance.tex only
routing: shadow tower -> Theorem~\ref{thm:genus-universality} -> Theorem~\ref{thm:family-index}; family index downstream only [Y]
topologization: cohomological E_3^{top} on BRST cohomology proved for affine KM at k != -h^\vee; chain-level E_3^{top} remains conjectural in general [Y]
MC5: analytic lane proved; coderived BV=bar proved; genuswise chain-level BV/BRST/bar conjectural [Y]
koszul meta: (vii) is the genus-0 factorization-homology criterion; (viii) is a proved consequence on the Koszul locus, not an unconditional equivalence [Y]
labels introduced: none
verdict: ACCEPT
```
exec
/bin/zsh -lc 'rg -n "g=0 only" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "sed -n '9540,9620p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \textbf{FT-4} (Theorem~H generic-level requirement):
 \emph{passed}. At critical level $k = -h^\vee$,
 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
 (Feigin--Frenkel center); Theorem~H does not apply.
 For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
 $4$-periodic and unbounded.
\item \textbf{FT-5} (topologization scope):
 \emph{passed}. Topologization
 ($\SCchtop + \text{conformal vector} = E_3$) is proved for
 affine KM at non-critical level; conjectural in general.
\item \textbf{FT-9} (SC duality):
 \emph{partial pass}. SC self-duality is retracted:
 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
 \text{shuffle-mixed}) \not\cong \SCchtop$.
 The duality functor is an involution (passed);
 self-duality of the operad is false (corrected).
\item \textbf{FT-10} (kernel of averaging):
 \emph{passed}. Closed formula
 $\dim\ker(\mathrm{av}_n) = n! - \binom{n+d-1}{n}$
 verified via Schur--Weyl
exec
/bin/zsh -lc "sed -n '9600,9690p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $+$ $1$ one-directional (D-module purity)
 \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
& Shadow obstruction tower algebraicity:
 $H(t)^2 = t^4 Q_L(t)$, tower determined by
 $(\kappa, \alpha, S_4)$
 \textup{(}Theorem~\ref{thm:riccati-algebraicity}\textup{)};
 cubic coefficient $\alpha = S_3/\kappa$ universal per family:
 $\alpha = 0$ \textup{(}Heis\textup{)},
 $\alpha = 2$ \textup{(}Vir\textup{)},
 family-specific for $\Walg_N$ and affine KM \\
& $\kappa$ formula universality: $\kappa(\cH_k) = k$,
 $\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$,
 $\kappa(\mathrm{Vir}_c) = c/2$,
 $\kappa(\Walg_N) = c(H_N{-}1)$ \\
& $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ for
 uniform-weight modular Koszul algebras at all genera
 \textup{(}Theorem~\ref{thm:genus-universality}\textup{)} \\
& Swiss-cheese theorem
 \textup{(}Theorem~\ref{thm:thqg-swiss-cheese}\textup{)} \\
& Chiral derived center as universal bulk \\
exec
/bin/zsh -lc "sed -n '3120,3185p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

%% ------------------------------------------------------------------
\subsection{Cross-reference table}
\label{subsec:concordance-koszulness-xref}

\begin{center}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{@{}p{3.6cm}lp{4.5cm}@{}}
\toprule
\textbf{Item} & \textbf{Label} & \textbf{Location} \\
\midrule
PBW $E_2$-collapse
 & \texttt{thm:pbw-koszulness-criterion}
 & Ch.~\ref{chap:koszul-pairs} \\
Bar-cobar q.i.\
 & \texttt{thm:bar-cobar-inversion-qi}
 & Ch.~\ref{chap:bar-cobar-adjunction} \\
ChirHoch polynomial
 & \texttt{thm:main-koszul-hoch}
 & Ch.~\ref{chap:deformation-theory} \\
exec
/bin/zsh -lc 'rg -o "item:kp-[''^}]*" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2388:item:kp-def
2388:item:kp-dmod
2395:item:kp-def
2398:item:kp-pbw
2402:item:kp-ainfty
2407:item:kp-ext
2412:item:kp-barcobar
2416:item:kp-barrbeck
2421:item:kp-facthom
2426:item:kp-hochschild
2434:item:kp-nullvec
2439:item:kp-fmbdy
2450:item:kp-lagrangian
2458:item:kp-dmod
2460:item:kp-fmbdy
2461:item:kp-fmbdy
2461:item:kp-dmod
3198:item:kp-def
3198:item:kp-fmbdy
3199:item:kp-lagrangian

exec
/bin/zsh -lc "sed -n '3170,3245p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathcal{N}{=}2$ SCA Koszulness
 & \texttt{prop:n2-koszulness}
 & Ch.~\ref{chap:n2-sca} \\
$\mathcal{N}{=}2$ CE/bar gap
 & \texttt{rem:n2-ce-chiral-gap}
 & Ch.~\ref{chap:n2-sca} \\
$V^\natural$ modular char.
 & \texttt{prop:moonshine-kappa}
 & Ch.~\ref{chap:moonshine} \\
Envelope-shadow
 & \texttt{def:envelope-shadow-functor}
 & \S\ref{sec:concordance-nishinaka-vicedo} \\
Finite-jet rigidity
 & \texttt{prop:finite-jet-rigidity}
 & \S\ref{sec:concordance-nishinaka-vicedo} \\
Gaussian collapse
 & \texttt{prop:gaussian-collapse-abelian}
 & \S\ref{sec:concordance-nishinaka-vicedo} \\
Graph-complex shadow
 & \texttt{conj:graph-complex-shadow}

exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '5960,6045p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5960	\left[
  5961	 \pi_*\!\left(
  5962	 \operatorname{ch}(\omega_\pi) \cdot
  5963	 \operatorname{Td}(T_\pi)
  5964	 \right)
  5965	\right]_g^{\mathrm{eval}},
  5966	\end{equation}
  5967	where $[\cdot]_g^{\mathrm{eval}}$ denotes evaluation of the degree-$g$ Chern character
  5968	$\operatorname{ch}_g(\mathbb{E})$ against $\psi^{2g-2}$ on
  5969	$\overline{\mathcal{M}}_{g,1}$.
  5970	
  5971	\item \emph{$\hat{A}$-genus identification.}
  5972	On the same uniform-weight locus, the total generating function is
  5973	\begin{equation}\label{eq:family-index-generating}
  5974	\sum_{g \geq 1} F_g(\cA)\, x^{2g}
  5975	\;=\;
  5976	\kappa(\cA) \cdot \bigl(\hat{A}(ix) - 1\bigr)
  5977	\;=\;
  5978	\kappa(\cA) \cdot
  5979	\left(\frac{x/2}{\sin(x/2)} - 1\right),
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7130,7195p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  7130	 & associator $+$ monodromy \\
  7131	\ref{conj:yangian-ordered-center}
  7132	 & Ordered chiral center of the Yangian:
  7133	 derived center of $Y_\hbar(\fg)^{\mathrm{ch}}$
  7134	 as $E_2$-chiral algebra \textup{(}Conjecture\textup{)}
  7135	 & standalone paper, \S\ref{sec:e1-yangian} \\
  7136	\ref{conj:coderived-e3}
  7137	 & Coderived $E_3$: $D^{\mathrm{co}}$-level $E_3$ on
  7138	 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$
  7139	 without conformal vector \textup{(}Conjecture\textup{)}
  7140	 & \S\ref{sec:en-koszul-duality} \\
  7141	\ref{conj:center-essential-surjectivity}
  7142	 & Center essential surjectivity:
  7143	 every $E_2$-chiral algebra arises as a derived center
  7144	 \textup{(}Conjecture\textup{)}
  7145	 & \S\ref{sec:en-koszul-duality} \\
  7146	\ref{constr:sugawara-antighost}
  7147	 & Sugawara antighost construction:
  7148	 conformal vector at non-critical level yields
  7149	 antighost field for topologization
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1920,1995p'" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
  1920	 completion to finite truncations. MC4$^0$ concerns algebras with
  1921	 finite resonance rank (Virasoro, non-quadratic
  1922	 $\mathcal{W}_N$) and is reduced to a finite-dimensional problem
  1923	 by Theorem~\ref{thm:resonance-filtered-bar-cobar}. The uniform
  1924	 PBW bridge (Theorem~\ref{thm:uniform-pbw-bridge}) connects MC1
  1925	 to MC4: uniform PBW degeneration plus quotient stabilization
  1926	 implies completed bar-cobar duality.
  1927	 The \emph{general theorem} (strong completion-tower
  1928	 theorem) is proved unconditionally. What remains is
  1929	 \emph{example-specific verification}: for each new
  1930	 algebra family beyond the standard landscape, one must
  1931	 verify that its coefficient sequences stabilize on finite
  1932	 windows and identify the H-level target. This is a
  1933	 finite computation for each family, not a theoretical
  1934	 gap.
  1935	 \emph{Arithmetic connection}: the spectral curve of the shadow
  1936	 Higgs field
  1937	 (Theorem~\ref{thm:shadow-higgs-field}) has convergence
  1938	 radius $|c|/3$ in the degree variable;
  1939	 the MC4 completion radius is controlled by the same parameter
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3170,3215p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3170	$\mathcal{N}{=}2$ SCA Koszulness
  3171	 & \texttt{prop:n2-koszulness}
  3172	 & Ch.~\ref{chap:n2-sca} \\
  3173	$\mathcal{N}{=}2$ CE/bar gap
  3174	 & \texttt{rem:n2-ce-chiral-gap}
  3175	 & Ch.~\ref{chap:n2-sca} \\
  3176	$V^\natural$ modular char.
  3177	 & \texttt{prop:moonshine-kappa}
  3178	 & Ch.~\ref{chap:moonshine} \\
  3179	Envelope-shadow
  3180	 & \texttt{def:envelope-shadow-functor}
  3181	 & \S\ref{sec:concordance-nishinaka-vicedo} \\
  3182	Finite-jet rigidity
  3183	 & \texttt{prop:finite-jet-rigidity}
  3184	 & \S\ref{sec:concordance-nishinaka-vicedo} \\
  3185	Gaussian collapse
  3186	 & \texttt{prop:gaussian-collapse-abelian}
  3187	 & \S\ref{sec:concordance-nishinaka-vicedo} \\
  3188	Graph-complex shadow
  3189	 & \texttt{conj:graph-complex-shadow}

thinking
**Identifying specific summary regions needing updates**

I’m pinpointing exact line regions in the document—around 3197-3204, near 1981-1993, and around 9600-9610—that include summaries of equivalences and statuses which likely need revising. These spots contain counts and references that must stay consistent with changes made to sections (vii) and (viii), so I’ll make sure to highlight them precisely for editing.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '9590,9645p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  9590	 (bar-cobar adjunction, inversion,
  9591	 complementarity, modular characteristic,
  9592	 Hochschild) \\
  9593	& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
  9594	 strong completion towers, HS-sewing) \\
  9595	& MC3 proved for all simple types on the
  9596	 evaluation-generated core; DK-4/5
  9597	 (extension beyond evaluation modules) downstream \\
  9598	& Koszulness programme: $10$ unconditional
  9599	 equivalences $+$ $1$ conditional (Lagrangian)
  9600	 $+$ $1$ one-directional (D-module purity)
  9601	 \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
  9602	& Shadow obstruction tower algebraicity:
  9603	 $H(t)^2 = t^4 Q_L(t)$, tower determined by
  9604	 $(\kappa, \alpha, S_4)$
  9605	 \textup{(}Theorem~\ref{thm:riccati-algebraicity}\textup{)};
  9606	 cubic coefficient $\alpha = S_3/\kappa$ universal per family:
  9607	 $\alpha = 0$ \textup{(}Heis\textup{)},
  9608	 $\alpha = 2$ \textup{(}Vir\textup{)},
  9609	 family-specific for $\Walg_N$ and affine KM \\

thinking
**Considering theorem adjustments**

I'm thinking about whether to delete certain elements from the theorem file since they aren't included. But I want to only do the minimal necessary changes. It seems important to weaken the claim from equivalence to consequence. However, the polynomial claim might still be true under the main theorem H. The user specifically asked for it to be “weakened,” which I need to keep in mind while making adjustments.
thinking
**Clarifying concise descriptions**

I need to make this concise because it’s part of a table. For the Koszulness program, I’ll summarize the details: "$9$ unconditional equivalences with factorization homology at $g=0$, $1$ proved consequence (Hochschild on the Koszul locus), $1$ conditional (Lagrangian), $1$ one-directional (D-module purity)." It’s lengthy, but I think wrapping it will work. I’ll look to similarly condense the line 1981 ring summary too. Then for the topologization block on line 7178, I need to format it effectively.
thinking
**Considering typographical conventions**

I’m looking at the file where the topologization theorem uses `\Ethree^{\mathrm{top}}`, but in another block, it shows `E_3`. I think I can use `$E_3^{\mathrm{top}}$` in the text, which should be safe. I also need to avoid unsupported macros in concordance if `\Ethree` has global definitions. I’m thinking of updating topologization search results beyond line 7178 after the patch. I’ll need to check other specific lines for any changes too, like 11128, 9593, and 1943.
codex
I’m patching the constitution now. The edits are limited to the stale status summaries, the Koszul meta-theorem summary block, and the family-index scope remark where the routing note belongs.

thinking
**Summarizing concordance updates**

I’m gathering exact file paths and line ranges for four key edits requested in concordance.tex. Each bullet will state the region, what to fix (like clarifying proofs, splitting statuses, or updating Koszul equivalences), and the reason for the change. I'll make sure to highlight any stale summary counts that should move alongside the Koszul equivalence updates.
codex
- `chapters/connections/concordance.tex:6005-6034` (Step 1 of the proof of Thm.~\ref{thm:family-index}): add a routing remark that the genus-universality input itself comes from the shadow-tower reconstruction before feeding into the index theorem, so the dependence chain is “shadow tower → genus universality → family index” and not a circular argument.  
- `chapters/connections/concordance.tex:7177-7185` (Topologization scoped box in the “program status” table): clarify that the proved topologization is the cohomological $E_3$ upgrade for affine Kac–Moody at non-critical level, while the full chain-level $E_3$ structure remains conjectural in the general conformal-vector case (Conj.~\ref{conj:coderived-e3}).  
- `chapters/connections/concordance.tex:1943-1959` and `1980-1984` (MC5 remark plus the Ring 1 summary table; see also the “Master conjectures resolved” anti-pattern around 11128): spell out the three separate MC5 lanes—analytic HS-sewing (proved), coderived BV=bar (proved), chain-level BV/BRST/bar (conjectural)—so the status split matches the new wording rather than bundling them together.  
- `chapters/connections/concordance.tex:2416-2444` (items (vii) and (viii) in the Koszul equivalences list) together with the summary counts at `3197-3204` and the ledger entry at `9598-9601`: restrict (vii) to the $g=0$ factorization-homology case and weaken (viii) appropriately, then adjust the “ten equivalences…” tally to reflect the downgraded/unconditional status so the counts in the summaries stay accurate.

thinking
**Troubleshooting patch issues**

It looks like the patch failed, possibly due to spacing or differing lines. I need to revisit the exact snippets in those areas to figure out what went wrong. I'll focus on doing targeted edits around those specific areas to correct the issue. It feels a bit tedious, but I want to ensure everything gets fixed properly! Let’s take it step by step and get that patch working again.
codex
The patch hit drift in the exact local text, so I’m re-reading the affected spans and patching them in smaller hunks. Scope is unchanged.
exec
/bin/zsh -lc "sed -n '2388,2474p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7170,7192p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1984,2000p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9588,9604p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9542,9552p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11124,11144p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3192,3208p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6200,6222p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 \textup{(proved local algebra)}} \\[2pt]
& Theorems A--H
 (bar-cobar adjunction, inversion,
 complementarity, modular characteristic,
 Hochschild) \\
& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
 strong completion towers, HS-sewing) \\
& MC3 proved for all simple types on the
 evaluation-generated core; DK-4/5
 (extension beyond evaluation modules) downstream \\
& Koszulness programme: $10$ unconditional
 equivalences $+$ $1$ conditional (Lagrangian)
 $+$ $1$ one-directional (D-module purity)
 \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
& Shadow obstruction tower algebraicity:
 $H(t)^2 = t^4 Q_L(t)$, tower determined by
 $(\kappa, \alpha, S_4)$
 succeeded in 54ms:
\textup{(\ref{item:kp-def})}--\textup{(\ref{item:kp-dmod})}
in the concordance and in the chapter are identical.

\medskip\noindent
\textbf{Unconditional equivalences} (i)--(x):

\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
\item\label{item:kp-def}
 Chirally Koszul (Definition~\ref{def:chiral-koszul-morphism}).
 \hfill \checkmark
\item\label{item:kp-pbw}
 PBW spectral sequence on $\barBgeom(\cA)$ collapses at~$E_2$
 (Theorem~\ref{thm:pbw-koszulness-criterion}).
 \hfill \checkmark
\item\label{item:kp-ainfty}
 Minimal $A_\infty$-model has $m_n = 0$ for $n \ge 3$
 (Theorem~\ref{thm:ainfty-koszul-characterization}).
 Converse via Keller classicality.
 \hfill \checkmark
\item\label{item:kp-ext}
 succeeded in 54ms:
 \text{shuffle-mixed})$: the closed dimensions are
 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not}
 Koszul self-dual. The duality \emph{functor} is an
 involution; the \emph{operad} is not self-dual.
 See AP166/B57.} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{Topologization scoped.}
 The topologization theorem
 (Theorem~\ref{thm:topologization}:
 $\SCchtop + \text{inner conformal vector} = E_3$)
 is proved for affine Kac--Moody at non-critical level.
 For general chiral algebras with conformal vector,
 topologization is conjectural
 (Conjecture~\ref{conj:coderived-e3} gives the
 $D^{\mathrm{co}}$-level upgrade).} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{Critical level: Theorem~H does NOT apply.}
 At the critical level $k = -h^\vee$ for affine KM,
 succeeded in 54ms:
chain-level BV/BRST/bar conjectural\textup{)},
MC3 \textup{(}three-layer split: MC3a evaluation core all types unconditional,
MC3b categorical thick generation all types unconditional,
MC3c full Cat~O type~A unconditional / other types conditional on
Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
and the Koszulness characterization programme
(10 unconditional, 1 conditional, 1 one-directional;
Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
appendices touches it except to cross-reference from it.

\subsection*{Ring~2: The nonlinear characteristic layer}
Before the extension appendices, the modular characteristic was
scalar: the single number~$\kappa(\cA)$ and its $\lambda_g$ tower,
plus the spectral discriminant~$\Delta_\cA(x)$. The full
hierarchy is:
\[
 succeeded in 52ms:
 the category).

\item \textbf{``All master conjectures resolved.''}
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is only partially
 proved: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}; the
 genuswise chain-level BV/BRST/bar identification remains
 conjectural (Conjecture~\ref{conj:master-bv-brst};
 class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types}):
 MC3a/b unconditional for all simple types;
 succeeded in 54ms:
 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
 (Feigin--Frenkel center); Theorem~H does not apply.
 For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
 $4$-periodic and unbounded.
\item \textbf{FT-5} (topologization scope):
 \emph{passed}. Topologization
 ($\SCchtop + \text{conformal vector} = E_3$) is proved for
 affine KM at non-critical level; conjectural in general.
\item \textbf{FT-9} (SC duality):
 \emph{partial pass}. SC self-duality is retracted:
 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
 succeeded in 52ms:
Steps~1--3 of the proof use only results established
in this monograph (genus universality,
Theorem~\ref{thm:genus-universality}) and imported results
(Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
\cite{FP03}). Step~4 is classical generating function analysis.
The identification $\mathcal{D}_{\cA}^{(g)} =
\kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
universality theorem; the functoriality of the construction
follows from the functoriality of $\kappa$ (determined by
genus-$1$ curvature) and $\mathbb{E}$ (determined by the
universal curve).

\emph{What remains.}
The theorem identifies $\mathcal{D}_{\cA}^{(g)}$ via its top Chern
class (the obstruction). A stronger result would construct
$\mathcal{D}_{\cA}^{(g)}$ as a \emph{sheaf} on
$\overline{\mathcal{M}}_g$ (rather than a $K$-theory class) and
identify its full Chern character with the genus expansion at all
intermediate degrees, not only the top. This would require the
coderived Ran-space formalism of
 succeeded in 54ms:
\bottomrule
\end{tabular}
\end{center}

\noindent
\emph{Status}: ten equivalences
(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
unconditional for the standard landscape
(Proposition~\ref{prop:lagrangian-perfectness} verifies
perfectness at non-critical, non-degenerate levels);
$\mathcal{D}$-module purity~(\ref{item:kp-dmod})
one-directional (forward direction proved, converse open).
Two further characterizations, tropical Koszulness
(Theorem~\ref{thm:tropical-koszulness}) and
bifunctor obstruction decomposition
(Theorem~\ref{thm:bifunctor-obstruction-decomposition}),
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -1990,3 +1990,5 @@
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
apply_patch(auto_approved=true) exited 0 in 35ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..49eb855222e46d4d1881e39ef5d35072533254f2
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..49eb855222e46d4d1881e39ef5d35072533254f2
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -2393,3 +2393,3 @@
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
@@ -2423,3 +2423,5 @@
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
@@ -2427,9 +2429,12 @@
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
apply_patch(auto_approved=true) exited 0 in 50ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..a2e5653bf31cc94c836254ac7e721c1639538c11
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..a2e5653bf31cc94c836254ac7e721c1639538c11
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -3203,4 +3203,9 @@
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
apply_patch(auto_approved=true) exited 0 in 36ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..919b612ffe2d70bf47233d291ddff77e0ad663d3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..919b612ffe2d70bf47233d291ddff77e0ad663d3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -7189,10 +7189,10 @@
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
apply_patch(auto_approved=true) exited 0 in 51ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..2a8ba068b1597cd3ffc4bc4f5126fc680c9357f5
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -7175,14 +7187,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..2a8ba068b1597cd3ffc4bc4f5126fc680c9357f5
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -7175,14 +7187,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -9604,4 +9604,5 @@
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
@@ -9609,4 +9610,7 @@
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
apply_patch(auto_approved=true) exited 0 in 46ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..206d3ad2776722fb8389be19102afec825eccdb8
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -7175,14 +7187,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9590,13 +9602,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..206d3ad2776722fb8389be19102afec825eccdb8
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -7175,14 +7187,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9590,13 +9602,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -6216,2 +6216,13 @@
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
apply_patch(auto_approved=true) exited 0 in 50ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..3900a907e01745741ff9834cabcd0306e4087a11
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9590,13 +9613,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..3900a907e01745741ff9834cabcd0306e4087a11
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9590,13 +9613,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -9569,5 +9569,7 @@
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
apply_patch(auto_approved=true) exited 0 in 40ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..49964978e5b2b6668593721fee19598c46438543
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..49964978e5b2b6668593721fee19598c46438543
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -11156,4 +11156,5 @@
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
apply_patch(auto_approved=true) exited 0 in 66ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar


thinking
**Evaluating technical changes**

I need to check if there are still "10 unconditional" stale counts after the patch. I should also look at topologization search results and identify if lines 1991 and 9598 need changes. It’s essential to see if the new structure compiles and to re-read relevant sections. I’ll search for references like "MC5 is only partially" and others. While waiting is an option, I might double-check with the explorer after making edits.
codex
The edits are in. I’m re-reading the modified spans now and then I’ll grep the file for the stale patterns the audit called out so I can confirm nothing contradictory remains in `concordance.tex`.
exec
/bin/zsh -lc "sed -n '2388,2478p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1984,2000p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9588,9606p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3192,3212p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7170,7192p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6200,6230p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11124,11144p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9542,9552p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Chapter~\ref{chap:koszul-pairs}.
Items are listed in the meta-theorem's numbering, so that
\textup{(\ref{item:kp-def})}--\textup{(\ref{item:kp-dmod})}
in the concordance and in the chapter are identical.

\medskip\noindent
\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):

\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
\item\label{item:kp-def}
 Chirally Koszul (Definition~\ref{def:chiral-koszul-morphism}).
 \hfill \checkmark
\item\label{item:kp-pbw}
 PBW spectral sequence on $\barBgeom(\cA)$ collapses at~$E_2$
 (Theorem~\ref{thm:pbw-koszulness-criterion}).
 \hfill \checkmark
\item\label{item:kp-ainfty}
 Minimal $A_\infty$-model has $m_n = 0$ for $n \ge 3$
 (Theorem~\ref{thm:ainfty-koszul-characterization}).
 Converse via Keller classicality.
 succeeded in 50ms:
chain-level BV/BRST/bar conjectural\textup{)},
MC3 \textup{(}three-layer split: MC3a evaluation core all types unconditional,
MC3b categorical thick generation all types unconditional,
MC3c full Cat~O type~A unconditional / other types conditional on
Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
and the Koszulness characterization programme
(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
factorization-homology criterion; 1 proved consequence,
1 conditional, 1 one-directional;
Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
appendices touches it except to cross-reference from it.

\subsection*{Ring~2: The nonlinear characteristic layer}
Before the extension appendices, the modular characteristic was
scalar: the single number~$\kappa(\cA)$ and its $\lambda_g$ tower,
plus the spectral discriminant~$\Delta_\cA(x)$. The full
 succeeded in 51ms:
% ======================================================================
\section{Programme status ledger}
\label{sec:concordance-programme-ledger}
\index{programme status!ledger}
% ======================================================================

The following table classifies every major result
and programme by proof status.
\textsc{Green}: proved within this monograph
(local algebra, all hypotheses discharged).
\textsc{Amber}: externally supported or conditional
(physically motivated, with partial evidence,
but dependent on conjectural inputs or
physical interpretation).
\textsc{Red}: unproved global or modular descent
(genuine open problems with no current proof
strategy reducing to proved results).

\begin{center}
 succeeded in 51ms:
Gaussian collapse
 & \texttt{prop:gaussian-collapse-abelian}
 & \S\ref{sec:concordance-nishinaka-vicedo} \\
Graph-complex shadow
 & \texttt{conj:graph-complex-shadow}
 & Ch.~\ref{chap:deformation-theory}
 \emph{(Heuristic: map $\Phi$ not rigorously constructed)} \\
\bottomrule
\end{tabular}
\end{center}

\noindent
\emph{Status}: nine equivalences
(\ref{item:kp-def})--(\ref{item:kp-facthom}),
(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
proved unconditionally, with
(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
consequence on the Koszul locus;
the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 succeeded in 51ms:
 & Sugawara antighost construction:
 conformal vector at non-critical level yields
 antighost field for topologization
 & \S\ref{sec:en-koszul-duality} \\
\hline
\multicolumn{3}{l}{\textit{%
 April 2026 session: AP165 bar-complex operadic correction}} \\
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{AP165 correction (constitutional).}
 The bar complex $\barB(\cA)$ is an $E_1$ coassociative
 coalgebra over $(\mathrm{ChirAss})^!$, the Koszul dual
 cooperad of the chiral associative operad.
 It is \emph{not} an $\SCchtop$-coalgebra.
 The $\SCchtop$ structure emerges on the derived chiral
 center pair
 $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\; \cA)$:
 bulk acts on boundary.
 See Vol~II CLAUDE.md, AP165/B54--B56.} \\
\hline
 succeeded in 50ms:
(1 - \hbar^2/4n^2\pi^2)^{-1}$.
At genus~$1$, the same scalar formula holds for every modular Koszul
algebra. For uniform-weight algebras the genus-$2$ ratio
$F_2/F_1 = 7/240$ is universal;
the ratio $F_2/F_1^2 = 7/(10\kappa)$ is perturbative
in $1/\kappa$. Shadow corrections beyond the scalar
sector enter as multiplicative deformations governed by
the MC equation, not by the KdV hierarchy
(Remark~\ref{rem:shadow-multiplicative-deformation}).
\end{remark}

\begin{remark}[Scope]\label{rem:family-index-scope}
Steps~1--3 of the proof use only results established
in this monograph (genus universality,
Theorem~\ref{thm:genus-universality}) and imported results
(Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
\cite{FP03}). Step~4 is classical generating function analysis.
\emph{Routing.} The non-circular proof route is
\[
\Theta_\cA \text{ and its shadow tower}
 succeeded in 54ms:
 \emph{chiral derived center}
 $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)
 = H^*(C^\bullet_{\mathrm{ch}}(\cA, \cA), \delta)$,
 which classifies bulk operators acting on the
 boundary
 (Theorem~\ref{thm:thqg-swiss-cheese}).
 These are different objects produced by different
 functors.
 \emph{Violated anti-pattern}:
 (three functors, three outputs:
 bar~$\neq$ Verdier dual~$\neq$ cobar).

\item \textbf{``The boundary algebra is the
 primitive object.''}
 \emph{False.}
 The primitive object is the open-sector
 factorization dg-category
 $\mathcal{C}_{\mathrm{op}}$ on a tangential log
 curve $(X, D, \tau)$ with real-oriented blowup at
 each puncture, not on the ordinary curve~$X$.
 succeeded in 50ms:
\textup{(}Theorem~\textup{\ref{thm:virasoro-quartic-resonance}})
satisfies the positivity constraint $Q^{\mathrm{ct}} > 0$
for all $c > 0$.
The shadow metric $Q_L > 0$ for all unitary theories
in the standard landscape
\textup{(}Remark~\textup{\ref{rem:shadow-radius-atlas}}).
Computational support from the engine
\texttt{modular\_shadow\_tower} (104~tests).
\end{remark}

% ----------------------------------------------------------------------
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

codex
I’m on the verification pass now. I’m grepping the modified file for the stale phrases the audit targeted: old topologization wording, old MC5 wording, and the old Koszul count.
exec
/bin/zsh -lc "sed -n '11132,11144p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"10 unconditional|MC5 is only partially|\\bpartial(ly)? proved\\b|coderived-e3|topologiz|topologis|FT-5|family-index-scope|genus-\\"'$0'"\\"'$ specialization|proved consequence on the Koszul locus|genus-'"\\"'$0'"\\"'$ factorization-homology criterion" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"All master conjectures resolved|Koszulness programme: \\"'$9'"\\"'$ unconditional|analytic/coderived lanes of MC5|Routing'"\\. The non-circular proof route|Theorem~\\\\ref\\{thm:family-index\\} is the downstream GRR\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9548,9605p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7178,7190p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \emph{Violated anti-pattern}:
 (three functors, three outputs:
 bar~$\neq$ Verdier dual~$\neq$ cobar).

\item \textbf{``The boundary algebra is the
 primitive object.''}
 \emph{False.}
 The primitive object is the open-sector
 factorization dg-category
 $\mathcal{C}_{\mathrm{op}}$ on a tangential log
 curve $(X, D, \tau)$ with real-oriented blowup at
 each puncture, not on the ordinary curve~$X$.
 The boundary algebra
 succeeded in 52ms:
6211:\begin{remark}[Scope]\label{rem:family-index-scope}
7159:\ref{conj:coderived-e3}
7172: antighost field for topologization
7201: The cohomological topologization theorem
7202: (Theorem~\ref{thm:topologization}:
7208: (Conjecture~\ref{conj:topologization-general}).} \\
9556:SC self-duality retraction, topologization scoping, critical-level
9569:\item \textbf{FT-5} (topologization scope):
9570: \emph{passed}. Cohomological topologization
9777: \textup{(}Conjecture~\ref{conj:coderived-e3}\textup{)} \\
 succeeded in 50ms:
9618:& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
11155:\item \textbf{``All master conjectures resolved.''}
 succeeded in 52ms:
Computational support from the engine
\texttt{modular\_shadow\_tower} (104~tests).
\end{remark}

% ----------------------------------------------------------------------
\paragraph{April 2026 session: falsification test results.}
Five additional falsification tests were evaluated against this
session's structural corrections (AP165 operadic scoping,
SC self-duality retraction, topologization scoping, critical-level
Theorem~H failure).
\begin{itemize}
\item \textbf{FT-2} (bar complex cooperad structure):
 \emph{passed}. The bar complex $\barB(\cA)$ is confirmed as an
 $E_1$ coassociative coalgebra over $(\mathrm{ChirAss})^!$,
 not an $\SCchtop$-coalgebra (AP165).
\item \textbf{FT-4} (Theorem~H generic-level requirement):
 \emph{passed}. At critical level $k = -h^\vee$,
 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
 (Feigin--Frenkel center); Theorem~H does not apply.
 For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
 succeeded in 50ms:
\multicolumn{3}{p{13cm}}{%
 \textbf{AP165 correction (constitutional).}
 The bar complex $\barB(\cA)$ is an $E_1$ coassociative
 coalgebra over $(\mathrm{ChirAss})^!$, the Koszul dual
 cooperad of the chiral associative operad.
 It is \emph{not} an $\SCchtop$-coalgebra.
 The $\SCchtop$ structure emerges on the derived chiral
 center pair
 $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\; \cA)$:
 bulk acts on boundary.
 See Vol~II CLAUDE.md, AP165/B54--B56.} \\
\hline
\multicolumn{3}{p{13cm}}{%
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar


thinking
**Checking line numbers**

I see that the search results show the line numbers have shifted. This means I might need to open the topologization block properly to address the issue. I should check if the format is correct and make any necessary adjustments to ensure everything aligns as expected. It seems like a minor detail, but I want to get it right to avoid confusion later on!
exec
/bin/zsh -lc "sed -n '7198,7210p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\hline
\multicolumn{3}{p{13cm}}{%
 \textbf{Topologization scoped.}
 The cohomological topologization theorem
 (Theorem~\ref{thm:topologization}:
 $\SCchtop + \text{inner conformal vector}
 \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
 is proved for affine Kac--Moody at non-critical level.
 The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
 general
 (Conjecture~\ref{conj:topologization-general}).} \\
\hline
\multicolumn{3}{p{13cm}}{%
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

exec
/bin/zsh -lc 'rg -n "resolved analytically|chain level: the analytic HS-sewing" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
11159: chain level: the analytic HS-sewing package is proved
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

exec
/bin/zsh -lc "sed -n '11154,11168p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\item \textbf{``All master conjectures resolved.''}
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is resolved
 analytically and in the coderived category, but not at
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}; the
 genuswise chain-level BV/BRST/bar identification remains
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar


thinking
**Running audit findings search**

I’m contemplating running a broader search for blacklist terms, though it might not be necessary. The user specifically asks for audit findings, so I’ll need to look for stale phrases. I think I’ll also use a command to verify references exist in the chapters while focusing on certain terms. I’ll run this in parallel to save time and make sure I’m covering all necessary steps efficiently!
codex
I’ve cleared the stale phrases in the target file. I’m doing one last verification pass for reference existence and for the exact pre-fix strings the audit wanted removed.
exec
/bin/zsh -lc 'git diff -- chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"10 unconditional|MC5 is only partially|MC5 is partially proved|\\\\SCchtop \\+ \\\\text\\{inner conformal vector\\} = E_3|\\\\SCchtop \\+ \\\\text\\{conformal vector\\} = E_3|Factorization homology \\\\"'$'"\\\\textstyle\\\\int_X \\\\cA\\\\"'$ in degree~'"\\\\"'$0'"\\\\"'$ for all smooth|'"\\\\ChirHoch\\"'^'"\\*\\\\(\\\\cA\\\\) polynomial, vanishing outside \\\\{0,1,2\\\\}|topologization is conjectural \\(Conjecture~\\\\ref\\{conj:coderived-e3\\}\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:family-index\\}|label\\{thm:genus-universality\\}|label\\{thm:topologization\\}|label\\{conj:topologization-general\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 exited 2 in 52ms:
rg: regex parse error:
    (?:10 unconditional|MC5 is only partially|MC5 is partially proved|\SCchtop \+ \text\{inner conformal vector\} = E_3|\SCchtop \+ \text\{conformal vector\} = E_3|Factorization homology \$\textstyle\int_X \cA\$ in degree~\/bin/zsh\$ for all smooth|\ChirHoch\^\*\(\cA\) polynomial, vanishing outside \{0,1,2\}|topologization is conjectural \(Conjecture~\ref\{conj:coderived-e3\})
                                                                                                                                                                                                       ^^
error: unrecognized escape sequence
 succeeded in 54ms:
chapters/connections/outlook.tex:660:\phantomsection\label{thm:family-index}
chapters/connections/concordance.tex:5940:\ClaimStatusProvedHere]\label{thm:family-index}
chapters/theory/en_koszul_duality.tex:2968:\label{thm:topologization}
chapters/theory/en_koszul_duality.tex:3108:\label{conj:topologization-general}
chapters/theory/higher_genus_foundations.tex:5298:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

codex
I have label existence confirmed. The only verification miss was a bad grep regex, so I’m rerunning that check with fixed-string searches and then reviewing the final diff once before I close out.
exec
/bin/zsh -lc "rg -n -F -e '10 unconditional' -e 'MC5 is only partially' -e 'MC5 is partially proved' -e '\\SCchtop + \\text{inner conformal vector} = E_3' -e '\\SCchtop + \\text{conformal vector} = E_3' -e 'Factorization homology "'$'"\\textstyle\\int_X \\cA"'$ in degree~$0$ for all smooth~$X$'"' -e '\\ChirHoch"'^*('"\\cA)"'$ polynomial, vanishing outside $'"\\{0,1,2\\}"'$'"' -e 'topologization is conjectural' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --unified=3 -- chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:

collab wait(call_74xucTrh4N63Gk71vV3yrQMt)
  receivers: 019d862f-2eff-7170-844b-71620159f877
wait(call_74xucTrh4N63Gk71vV3yrQMt) 1 agents complete:
  019d862f-2eff-7170-844b-71620159f877 completed: "- `chapters/connections/concordance.tex:6005-6034` (Step 1 of the proof of Thm.~\ref{thm:family-index}): add a routing r…"
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

codex
The independent check matched the same edit regions. I’m doing one last diff read with paging disabled, then I’ll report each finding as `FIXED` or `BLOCKED`.
exec
/bin/zsh -lc 'GIT_PAGER=cat git diff --unified=3 -- chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar


thinking
**Checking git status**

I'm trying to understand why the file remains blank even after it's been modified. I wonder if maybe git diff sees the file as untracked or if it's in .gitignore. That feels a bit odd, though. It's possible I could use `git status --short` to check if the file is modified. I guess there's a chance it’s already modified but not tracked. I’ll run `git status --short -- chapters/connections/concordance.tex` to see what's happening.
exec
/bin/zsh -lc 'git status --short -- chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar




thinking
**Considering git issues**

I'm trying to figure out why Git sees no changes. It could be that the repository is in a clean state, or the file isn't under Git tracking. When I run `git status --short` and see a blank output, it suggests the file might not be tracked. But the repository should still show an error if it's not a Git repo. 

I wonder if there could be a weird state in the worktree or possibly an output suppression issue with the developer tool if the output is too large.
thinking
**Evaluating git and references**

I’m not sure why `git diff` isn't working. First, I should check if the references exist and search for any stale phrases. If I get a fixed-string search exit code 1 with no output, that indicates there are no stale strings, which is great! 

Next, I need to confirm if the `topologization-general` reference exists. The green table entry for `MC5` didn’t mention genus-0 algebraic BRST/bar, which is part of what the user asked about. Maybe I should update the green table to include this for clarity.
thinking
**Clarifying genus-0 status**

I need to clarify that genus-0 algebraic BRST/bar isn't classified as analytic or coderived; it belongs to the chain-level at genus 0. The user specifically asked for a status split: analytic proved, coderived proved, and chain-level conjectural. While the genus-0 is indeed proved, the "chain-level conjectural" might refer specifically to genus-wise chain-level rather than all chain levels. My edits in the MC5 detailed lines aim to preserve this important nuance.
Plan update
Patched only chapters/connections/concordance.tex, re-read each edited region, verified the referenced labels exist, and grep-checked the file for the stale phrases targeted by the audit.
  ✓ Read required constitutional context and locate the exact concordance entries for the four findings
  ✓ Apply the minimum scoped edits in chapters/connections/concordance.tex
  ✓ Re-read the modified entries, grep the file for forbidden/stale patterns, and report FIXED/BLOCKED status for each finding
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

collab close_agent(call_daop1Kk935eEtybcYFua7Tiy)
  receiver: 019d862f-2eff-7170-844b-71620159f877
close_agent(call_daop1Kk935eEtybcYFua7Tiy) completed: "- `chapters/connections/concordance.tex:6005-6034` (Step 1 of the proof of Thm.~\ref{thm:family-index}): add a routing r…":
  receiver: 019d862f-2eff-7170-844b-71620159f877
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

codex
Edited [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex).

`FIXED` 1. Added the AP147 routing note in `rem:family-index-scope`, making the dependency explicit: shadow tower `\to` genus universality `\to` family index. The concordance now states that `thm:family-index` is downstream of `thm:genus-universality`, not an input to it.

`FIXED` 2. Updated topologization status so the concordance now distinguishes:
cohomological `E_3^{\mathrm{top}}` on BRST cohomology, proved for affine KM at non-critical level; chain-level lift conjectural in general. I corrected both the scoped constitutional box and `FT-5`.

`FIXED` 3. Updated MC5 status wording to the requested split: analytic proved, coderived proved, chain-level conjectural. I corrected the stale “partially proved” anti-pattern wording and the programme ledger summary.

`FIXED` 4. Updated the Koszul equivalences surface so `(vii)` is explicitly the genus-0 factorization-homology criterion, `(viii)` is weakened to a proved consequence on the Koszul locus, and the stale counts now read `9` unconditional equivalences plus `1` proved consequence rather than `10` unconditional equivalences.

No `BLOCKED` items.

Verification: I re-read all edited spans, confirmed the referenced labels `thm:family-index`, `thm:genus-universality`, `thm:topologization`, and `conj:topologization-general` exist, and grep-checked the target file for the stale pre-fix phrases; those checks returned no hits. I did not run a TeX build.
file update:
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 28293eb0b4f5ca2bb0f76fbf195df11a939dbdc3..0f3df83f76da84879fa2fcc1f37ee2418eebc5b3
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -1988,7 +1988,9 @@
 Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
 DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
 and the Koszulness characterization programme
-(10 unconditional, 1 conditional, 1 one-directional;
+(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
+factorization-homology criterion; 1 proved consequence,
+1 conditional, 1 one-directional;
 Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
 appendices touches it except to cross-reference from it.
 
@@ -2389,7 +2391,7 @@
 in the concordance and in the chapter are identical.
 
 \medskip\noindent
-\textbf{Unconditional equivalences} (i)--(x):
+\textbf{Unconditional equivalences} (i)--(vii), (ix)--(x):
 
 \begin{enumerate}[label=\textup{(\roman*)},ref=\roman*]
 \item\label{item:kp-def}
@@ -2419,17 +2421,22 @@
  Conservativity + totalization on log-FM strata.
  \hfill \checkmark
 \item\label{item:kp-facthom}
- Factorization homology $\textstyle\int_X \cA$ in degree~$0$ for all smooth~$X$
+ Factorization homology $\textstyle\int_{\mathbb{P}^1} \cA$ in degree~$0$
+ (the genus-$0$ specialization; higher genus only on the
+ uniform-weight lane)
  (Theorem~\ref{thm:fh-concentration-koszulness}).
  Bar = FH; genus-$0$ concentration forces $E_2$-collapse.
  \hfill \checkmark
+\end{enumerate}
+
+\medskip\noindent
+\textbf{Proved consequence on the Koszul locus} (viii):
+
+\begin{enumerate}[label=\textup{(\roman*)},ref=\roman*,resume]
 \item\label{item:kp-hochschild}
- $\ChirHoch^*(\cA)$ polynomial, vanishing outside $\{0,1,2\}$
+ $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
+ $\{0,1,2\}$ and satisfies Koszul-dual duality on the Koszul locus
  (Theorem~\ref{thm:main-koszul-hoch}).
- For single-generator algebras with no simple pole in the OPE,
- $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
- the zero mode is central); for algebras with simple poles,
- $\ChirHoch^1 = 0$ (all derivations inner).
  \hfill \checkmark
 \item\label{item:kp-nullvec}
  Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
@@ -3194,8 +3201,13 @@
 \end{center}
 
 \noindent
-\emph{Status}: ten equivalences
-(\ref{item:kp-def})--(\ref{item:kp-fmbdy}) proved unconditionally;
+\emph{Status}: nine equivalences
+(\ref{item:kp-def})--(\ref{item:kp-facthom}),
+(\ref{item:kp-nullvec}), (\ref{item:kp-fmbdy})
+proved unconditionally, with
+(\ref{item:kp-facthom}) the genus-$0$ factorization-homology criterion;
+the Hochschild statement~(\ref{item:kp-hochschild}) is a proved
+consequence on the Koszul locus;
 the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
 unconditional for the standard landscape
 (Proposition~\ref{prop:lagrangian-perfectness} verifies
@@ -6202,6 +6214,17 @@
 Theorem~\ref{thm:genus-universality}) and imported results
 (Mumford's GRR formula \cite{Mumford83}; Faber--Pandharipande
 \cite{FP03}). Step~4 is classical generating function analysis.
+\emph{Routing.} The non-circular proof route is
+\[
+\Theta_\cA \text{ and its shadow tower}
+\Longrightarrow
+\text{Theorem~\ref{thm:genus-universality}}
+\Longrightarrow
+\text{Theorem~\ref{thm:family-index}}.
+\]
+Theorem~\ref{thm:family-index} is the downstream GRR
+repackaging of the scalar genus series; it is not an
+input to Theorem~\ref{thm:genus-universality}.
 The identification $\mathcal{D}_{\cA}^{(g)} =
 \kappa(\cA) \cdot \mathbb{E}$ is canonical given the genus
 universality theorem; the functoriality of the construction
@@ -7175,14 +7198,14 @@
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Topologization scoped.}
- The topologization theorem
+ The cohomological topologization theorem
  (Theorem~\ref{thm:topologization}:
- $\SCchtop + \text{inner conformal vector} = E_3$)
+ $\SCchtop + \text{inner conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
  is proved for affine Kac--Moody at non-critical level.
- For general chiral algebras with conformal vector,
- topologization is conjectural
- (Conjecture~\ref{conj:coderived-e3} gives the
- $D^{\mathrm{co}}$-level upgrade).} \\
+ The chain-level $E_3^{\mathrm{top}}$ lift is conjectural in
+ general
+ (Conjecture~\ref{conj:topologization-general}).} \\
 \hline
 \multicolumn{3}{p{13cm}}{%
  \textbf{Critical level: Theorem~H does NOT apply.}
@@ -9544,9 +9567,11 @@
  For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  $4$-periodic and unbounded.
 \item \textbf{FT-5} (topologization scope):
- \emph{passed}. Topologization
- ($\SCchtop + \text{conformal vector} = E_3$) is proved for
- affine KM at non-critical level; conjectural in general.
+ \emph{passed}. Cohomological topologization
+ ($\SCchtop + \text{conformal vector}
+ \Rightarrow E_3^{\mathrm{top}}$ on BRST cohomology)
+ is proved for affine KM at non-critical level; the
+ chain-level lift is conjectural in general.
 \item \textbf{FT-9} (SC duality):
  \emph{partial pass}. SC self-duality is retracted:
  $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
@@ -9590,13 +9615,17 @@
  (bar-cobar adjunction, inversion,
  complementarity, modular characteristic,
  Hochschild) \\
-& MC1, MC2, MC4, MC5 (PBW, bar-intrinsic MC,
- strong completion towers, HS-sewing) \\
+& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
+ (PBW, bar-intrinsic MC, strong completion towers,
+ HS-sewing, coderived BV$=$bar) \\
 & MC3 proved for all simple types on the
  evaluation-generated core; DK-4/5
  (extension beyond evaluation modules) downstream \\
-& Koszulness programme: $10$ unconditional
- equivalences $+$ $1$ conditional (Lagrangian)
+& Koszulness programme: $9$ unconditional
+ equivalences \textup{(}with factorization homology at
+ genus~$0$\textup{)} $+$ $1$ proved consequence
+ \textup{(}Hochschild on the Koszul locus\textup{)}
+ $+$ $1$ conditional (Lagrangian)
  $+$ $1$ one-directional (D-module purity)
  \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
 & Shadow obstruction tower algebraicity:
@@ -11125,8 +11154,9 @@
 
 \item \textbf{``All master conjectures resolved.''}
  \emph{Misleading.}
- MC1 through MC4 are proved. MC5 is only partially
- proved: the analytic HS-sewing package is proved
+ MC1 through MC4 are proved. MC5 is resolved
+ analytically and in the coderived category, but not at
+ chain level: the analytic HS-sewing package is proved
  at all genera (Theorem~\ref{thm:general-hs-sewing}); the
  genus-$0$ algebraic BRST/bar comparison is proved
  (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar

tokens used
179,103
