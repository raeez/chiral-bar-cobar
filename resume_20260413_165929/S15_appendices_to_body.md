# S15_appendices_to_body (1013s)

- [CRITICAL] appendices/homotopy_transfer.tex:457 — PROBLEM: Theorem `thm:chiral-htt` states an SDR of the “underlying D-module” with `H = H^{\mathrm{ch}}_*(\cA)` (lines 457-460), but its proof switches to an SDR of `\Bbar(\cA) \to H^*(\Bbar(\cA))` (line 482). The theorem surface is conflating the transfer target. FIX: rewrite the theorem to one object only. Minimal repair: replace lines 457-460 by “suppose `(C,H,p,\iota,h)` is an SDR of a chosen dg model `C` for `\cA`,” delete `H = H^{\mathrm{ch}}_*(\cA)`, and move the Koszul-line vanishing claim into a separate proposition explicitly about the bar complex `\Bbar(\cA) \to H^*(\Bbar(\cA))`.

- [HIGH] chapters/theory/higher_genus_foundations.tex:1582 — PROBLEM: Theorem `thm:chain-vs-homology` says HTT gives a minimal `A_\infty` structure on `H^*(\mathcal A)` (lines 1582-1588), but the proof actually constructs the SDR on `\barBgeom(\mathcal A)` and transfers to `H^*(\barBgeom(\mathcal A))` (lines 1600-1638). Statement and proof are about different objects. FIX: change lines 1582-1593 to say the transfer lands on the chosen SDR target, here `H^*(\barBgeom(\mathcal A))`; if the intended target really is `H^*(\mathcal A)`, then rewrite the proof to construct that SDR instead of the bar-complex SDR.

- [HIGH] appendices/homotopy_transfer.tex:531 — PROBLEM: Theorem `thm:bar-cobar-htt` is cited as proved input, but its SDR data `\iota_{\mathrm{counit}}` and `h_{\mathrm{Hodge}}` are introduced only here (lines 535-540) and are not constructed anywhere in the audited seam. FIX: either add a preceding proposition that constructs a filtered SDR `(\Omega(\Bbar(\cA)), \cA, \psi, \iota, h)` with those maps, or weaken the theorem to an implication: “Assume such a filtered SDR exists; then HTT identifies `\psi` as the canonical `A_\infty` quasi-isomorphism.”

- [HIGH] chapters/theory/quantum_corrections.tex:359 — PROBLEM: The homotopy-transfer citation is not what the appendix proves. `\eta_{123}^{\mathrm{FM}}` is nowhere defined in the seam, and the appendix gives the tree formula `\tilde m_3` as a sum of HTT terms/boundary-stratum integrals (appendices/homotopy_transfer.tex:193-195, 624-652), not a single integral over `\overline{C}_3(X)`. Line 361 also drops `p`, `\iota`, the sign, and treats `h` as multiplication. FIX: replace lines 359-361 by the actual HTT formula
  `m_3(a,b,c)=p\,m_3(\iota a,\iota b,\iota c)+p\,m_2(h\,m_2(\iota a,\iota b),\iota c)+(-1)^{|a|}p\,m_2(\iota a,h\,m_2(\iota b,\iota c))`,
  or cite Proposition `prop:trees-boundary-strata` and write the sum over the two FM boundary strata instead of introducing `\eta_{123}^{\mathrm{FM}}`.

- [HIGH] chapters/theory/nilpotent_completion.tex:1176 — PROBLEM: “The passage from modes to states is the HTT” is not supported by Theorem `thm:chiral-htt`, which never mentions a mode/state comparison. FIX: replace lines 1176-1178 by “After passing to the positive-energy state-space model, HTT is applied weightwise to the resulting SDR,” or insert a separate proposition constructing the mode-to-state comparison before invoking HTT.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32053,32292; chapters/theory/chiral_koszul_pairs.tex:3328,3449; chapters/theory/higher_genus_complementarity.tex:6085 — PROBLEM: These passages cite Theorem `thm:nms-archetype-trichotomy` as though it classifies the mixed class `M` / “Virasoro, `\mathcal W_N`”. But the cited theorem in appendices/nonlinear_modular_shadows.tex:1209-1224 proves only the three quartic-order cases `G/L/C` (Heisenberg, affine `\widehat{\mathfrak{sl}}_2`, `\beta\gamma`). Virasoro nontermination is separate in `thm:nms-finite-termination` (appendices/nonlinear_modular_shadows.tex:2190-2199), and principal `\mathcal W_N` mixed cubic/quartic behavior is only `cor:nms-principal-wn-mixed` (appendices/nonlinear_modular_shadows.tex:1637-1645). FIX: split the citation. Use `thm:nms-archetype-trichotomy` only for `G/L/C`; cite `thm:nms-finite-termination` for Virasoro; cite `cor:nms-principal-wn-mixed` only for principal `\mathcal W_N` through quartic order; if no theorem in scope proves infinite depth for all `\mathcal W_N`, replace “Virasoro, `\mathcal W_N`” by “Virasoro” or mark the `\mathcal W_N` extension conjectural.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:1582; chapters/theory/chiral_modules.tex:2657; chapters/theory/chiral_hochschild_koszul.tex:2900,2932; chapters/theory/quantum_corrections.tex:360,525 — PROBLEM: These lines call `app:homotopy-transfer` an appendix, but `main.tex:998-1000` explicitly promotes `appendices/homotopy_transfer.tex` into Part I before `\appendix` (`main.tex:1526`). FIX: replace each `Appendix~\ref{app:homotopy-transfer}` with `Chapter~\ref{app:homotopy-transfer}` or `Ch.~\ref{app:homotopy-transfer}` consistently.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:4843 — PROBLEM: This file repeatedly refers to `app:nonlinear-modular-shadows` as an appendix (also 10133, 12271, 12310, 13201, 15442, 15456, 29654, 30996), but `main.tex:1093` inputs `appendices/nonlinear_modular_shadows.tex` before `\appendix`. FIX: replace every `Appendix~\ref{app:nonlinear-modular-shadows}` in this file with `Chapter~\ref{app:nonlinear-modular-shadows}` or `Ch.~...`.

- [MEDIUM] chapters/theory/introduction.tex:1956; chapters/theory/chiral_hochschild_koszul.tex:5745,5777 — PROBLEM: These lines call `app:branch-line-reductions` an appendix, but `main.tex:1097` inputs `appendices/branch_line_reductions.tex` before `\appendix`. FIX: replace those occurrences with `Chapter~\ref{app:branch-line-reductions}` or `Ch.~...`.

- [LOW] appendices/general_relations.tex:100; chapters/theory/higher_genus_foundations.tex:1146 — PROBLEM: The cited appendix surface is curved, but the body definition is uncurved. The appendix writes `(\mathcal A,\{m_k\}_{k\ge0},\mu_0)` and uses `\mu_0` in the formulas, while the body at line 1146 defines an uncurved `A_\infty` algebra with `k\ge1` and sends the reader straight to that curved appendix. FIX: in `appendices/general_relations.tex`, replace `\mu_0` by `m_0` consistently in lines 100-113; in `higher_genus_foundations.tex:1146`, change the parenthetical to “for the curved extension with `m_0`, see Appendix~\ref{app:curved-ainfty-formulas}.”

## Summary
Checked: 25 | Findings: 10 | Verdict: FAIL


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
session id: 019d875a-d422-77b1-8980-2a888cda9cac
--------
user
<task>
You are a MAXIMALLY HARSH adversarial auditor of a 4,500-page mathematical manuscript.
Tear apart every weakness. Accept NOTHING at face value.
For EVERY finding, you MUST provide the EXACT FIX — not just the diagnosis.
Format: [SEVERITY] file:line — PROBLEM: ... FIX: ...
</task>

<grounding_rules>
Ground every claim in file contents you actually read. No guesses. No inferences presented as facts.
</grounding_rules>

<completeness_contract>
Exhaust the audit surface. After the first finding, dig deeper for second-order failures.
After the obvious issues, hunt for the SUBTLE ones that survive surface-level review.
</completeness_contract>

<verification_loop>
Re-verify each finding against actual file contents. Remove false positives.
</verification_loop>

<structured_output_contract>
Return findings as:
- [CRITICAL] file:line — PROBLEM: ... FIX: ...
- [HIGH] file:line — PROBLEM: ... FIX: ...
- [MEDIUM] file:line — PROBLEM: ... FIX: ...
- [LOW] file:line — PROBLEM: ... FIX: ...

End with:
## Summary
Checked: N | Findings: N | Verdict: PASS/FAIL
</structured_output_contract>


MISSION: SEAM AUDIT between appendices/ and chapters/theory/.

Appendices→Theory. Check: (a) appendix results cited correctly in body, (b) no circular dependencies, (c) notation consistent

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers
codex
Using `deep-beilinson-audit` for a seam audit between `appendices/` and `chapters/theory/`. I’m starting by locating every appendix/theory cross-reference, then I’ll read the cited source and destination contexts side by side to check citation correctness, dependency direction, and notation drift.
exec
/bin/zsh -lc "pwd && rg -n --glob '*.tex' '(appendix|appendices|app:|sec:app|thm:app|lem:app|prop:app|cor:app|Appendix|Part~|Chapter~|chapters/theory|theory)' appendices chapters/theory CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1468

/Users/raeez/chiral-bar-cobar
CLAUDE.md:21:**Architecture (2026-04-12):** E_n chiral algebra theory stays in Vol I (pure algebra/operads). ALL physics moves to Vol II. Vol III provides the geometric source (CY categories → chiral algebras via the E_n circle).
CLAUDE.md:339:- B33. `Part~IV`, `Chapter~12` hardcoded. CORRECT: `\ref{part:...}`. V2-AP26/FM10.
CLAUDE.md:437:**FM10. Hardcoded part number drift (`Part~IV` vs `\ref{part:...}`).** Cross-volume references as hardcoded roman numerals break silently on reorganisation. Counter: after any Edit, grep `Part~[IVX]+|Chapter~[0-9]+` in the file and replace with `\ref{part:...}`.
CLAUDE.md:479:(6) WRONG: "The Steinberg analogy: B(A) presents SC as the Steinberg variety presents the Hecke algebra." TRUTH: Retired. The Steinberg variety is a geometric object in the representation theory of reductive groups. The bar complex is a coalgebra computing the derived center. These are unrelated constructions at different categorical levels.
CLAUDE.md:869:AP124: Duplicate \label{} across chapters. Before creating ANY \label{foo}, grep the entire manuscript. Parallel agents independently create labels with the same natural name. LaTeX silently uses the last definition, misdirecting cross-refs. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates.
CLAUDE.md:934:AP176: CONSTITUTIONAL — "arity" is BANNED. The word "arity" does NOT appear anywhere in the manuscript. "Degree" is the universal term for: bar complex grading, operadic input count, tree vertex valence, Stasheff identity level, SC mixed sector parameters, cooperad/operad component indices, endomorphism operad components, brace insertion count, and all other contexts where Loday-Vallette would use "arity." This is a deliberate, permanent terminological decision. NEVER reintroduce "arity." NEVER suggest reverting "degree" to "arity." NEVER flag the use of "degree" in operadic contexts as an error. If an agent proposes restoring "arity" anywhere, the proposal is WRONG. The ~25 instances of "an degree" (article mismatch) should be corrected to "a degree." Grep check after every .tex edit: `grep -rn '\\barity\\b' chapters/ appendices/ standalone/` must return ZERO hits.
CLAUDE.md:983:AAP18: Confabulating operadic theory -> compute or cite (Loday-Vallette, Vallette, Livernet). NEVER analogize.
CLAUDE.md:1107:| Compl K | Fiber-center + Theorem D | Index theory / Euler characteristic (H12) |
appendices/general_relations.tex:2:\label{app:geometric-dictionary}
appendices/general_relations.tex:4:Each entry represents a precise mathematical correspondence, not merely an analogy, between three languages: the physical (conformal field theory and operator products), the algebraic (operads and homological algebra), and the geometric (configuration spaces and residues).
appendices/general_relations.tex:34:\label{app:sign-conventions-general}
appendices/general_relations.tex:48:\label{app:ope-tables}
appendices/general_relations.tex:68:\label{app:arnold-relations-small-n}
appendices/general_relations.tex:98:\label{app:curved-ainfty-formulas}
chapters/theory/three_invariants.tex:211:Part~(i) is the $\mathrm{d}\log$ absorption of
chapters/theory/three_invariants.tex:217:Part~(ii) is verified by the explicit computations for each standard
chapters/theory/three_invariants.tex:226:Part~(iii) is the shadow-depth classification. Class~$G$ is

thinking
**Exploring search details**

I need to check if the search output is too large and possibly not very relevant. It seems like I should use an explorer agent to pinpoint seams and read the skill file, maybe focusing on multiple skills like deep-beilinson-audit. Claim-surface-sync might not be necessary, though. I also think I need to read CLAUDE and concordance for instructions, but perhaps that isn't essential. Since this task is significant and the user wants an exhaustive audit, I should provide a plan after I gather enough context.
codex
I’ve mapped the broad surface and found that the seam is larger than a few explicit cross-refs: some theory chapters cite appendices by label, others rely on appendix conventions implicitly. Next I’m narrowing to exact appendix→theory transition points and checking each cited result against the source statement line by line.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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



thinking
**Gathering cross references**

I need to create a comprehensive list of cross-references between appendices and chapters in the theory section. I can script to identify these references using specific patterns like '\\ref{app:' for chapters and '\\ref{chap:' for appendices. It's also important to check if theorem labels in appendices are cited by the main body. I'll derive all labels in the appendices and look for references to them in the theory. Using shell commands makes the analysis simpler, as advised by the developer.
thinking
**Extracting cross-references**

I’m considering using tools like rg and maybe awk for the cross-reference extraction. I can use rg to list labels in the appendices and then find references in the theory that match those labels. Additionally, I'll look for references from the appendices that go back to theory labels. It might be a good idea to use multi-tool commands in parallel for efficiency, particularly when I'm limited to using developer tools for executing commands.
codex
The seam is bidirectional, so I’m checking both directions now: theory citing appendix labels, and appendices reaching back into theory chapters. That’s where circularity and stale notation usually hide.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '"'^'"\\\\label\\{' appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'appendix|appendices|Appendix' chapters/theory --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\(ref|Cref|autoref|eqref)\\{["'^}]*'"\\}' chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '\\\\(ref|Cref|autoref|eqref)\\{["'^}]*'"\\}' appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 797

appendices/general_relations.tex:2:\label{app:geometric-dictionary}
appendices/general_relations.tex:34:\label{app:sign-conventions-general}
appendices/general_relations.tex:48:\label{app:ope-tables}
appendices/general_relations.tex:68:\label{app:arnold-relations-small-n}
appendices/general_relations.tex:98:\label{app:curved-ainfty-formulas}
appendices/homotopy_transfer.tex:2:\label{app:homotopy-transfer}
appendices/homotopy_transfer.tex:15:\label{prop:htt-rectification}
appendices/homotopy_transfer.tex:61:\label{sec:ainfty-historical}
appendices/homotopy_transfer.tex:66:\label{sec:htt}
appendices/homotopy_transfer.tex:69:\label{thm:htt}
appendices/homotopy_transfer.tex:130:\label{def:sdr}
appendices/homotopy_transfer.tex:146:\label{lem:sdr-existence}
appendices/homotopy_transfer.tex:176:\label{sec:transfer-formulas}
appendices/homotopy_transfer.tex:179:\label{constr:transfer-ainf}
appendices/homotopy_transfer.tex:209:\label{thm:tree-formula}
appendices/homotopy_transfer.tex:230:\label{ex:trees-m4}
appendices/homotopy_transfer.tex:259:\label{prop:transfer-signs}
appendices/homotopy_transfer.tex:270:\label{sec:minimal-models}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:631:\textup{(}Appendix~\textup{\ref{sec:coderived-models})} off it.
chapters/theory/higher_genus_modular_koszul.tex:4310: Appendix~\textup{\ref{app:nonlinear-modular-shadows}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:4843:(Appendix~\ref{app:nonlinear-modular-shadows});
chapters/theory/higher_genus_modular_koszul.tex:10133:Appendix~\ref{app:nonlinear-modular-shadows} at each finite
chapters/theory/higher_genus_modular_koszul.tex:12271: (Appendix~\ref{app:nonlinear-modular-shadows}).
chapters/theory/higher_genus_modular_koszul.tex:12310: Appendix~\ref{app:nonlinear-modular-shadows}.
chapters/theory/higher_genus_modular_koszul.tex:13201:and Appendix~\ref{app:nonlinear-modular-shadows}
chapters/theory/higher_genus_modular_koszul.tex:15442:Appendix~\ref{app:nonlinear-modular-shadows}:
chapters/theory/higher_genus_modular_koszul.tex:15456:Appendix~\ref{app:nonlinear-modular-shadows} enumerates
chapters/theory/higher_genus_modular_koszul.tex:29654:(Appendix~\ref{app:nonlinear-modular-shadows}) is
chapters/theory/higher_genus_modular_koszul.tex:30996:and Appendix~\ref{app:nonlinear-modular-shadows}) is the
chapters/theory/quantum_corrections.tex:360:where $\eta_{123}^{\text{FM}}$ is the propagator form on the Fulton--MacPherson compactification $\overline{C}_3(X)$, defined via homotopy transfer (cf.\ Appendix~\ref{app:homotopy-transfer}). Concretely, $m_3$ sums over binary trees with 3 leaves, each tree contributing an iterated composition of $m_2$ with the contracting homotopy $h$:
chapters/theory/quantum_corrections.tex:525:full $L_\infty$ structures on both sides, so homotopy transfer (Appendix~\ref{app:homotopy-transfer})
chapters/theory/en_koszul_duality.tex:5588:(see~\cite{Lorgat26II}, Appendix~A, Proposition~A.5):
chapters/theory/en_koszul_duality.tex:5644:(see~\cite{Lorgat26II}, Appendix~A, Proposition~A.6)
chapters/theory/bar_cobar_adjunction_inversion.tex:70:(Appendix~\ref{app:nilpotent-completion}); and general algebras may
chapters/theory/bar_cobar_adjunction_inversion.tex:1809:this chapter and in the coderived appendix.
chapters/theory/bar_cobar_adjunction_curved.tex:1510:See Appendix~\ref{app:nilpotent-completion},
chapters/theory/bar_cobar_adjunction_curved.tex:5953:(Appendix~\ref{app:nilpotent-completion}) inherits strict nilpotence.
chapters/theory/introduction.tex:1956:(Appendix~\ref{app:branch-line-reductions}) extract exact
 succeeded in 51ms:
Total output lines: 7303

chapters/theory/higher_genus_modular_koszul.tex:17:characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
chapters/theory/higher_genus_modular_koszul.tex:26:(Theorem~\ref{thm:bar-modular-operad}).
chapters/theory/higher_genus_modular_koszul.tex:32:(Theorem~\ref{thm:higher-genus-inversion}).
chapters/theory/higher_genus_modular_koszul.tex:43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
chapters/theory/higher_genus_modular_koszul.tex:62:(\S\ref{subsec:two-level-convention}). The weight filtration on
chapters/theory/higher_genus_modular_koszul.tex:80: (Definition~\ref{def:shadow-algebra})
chapters/theory/higher_genus_modular_koszul.tex:87: (Definition~\ref{def:modular-bar-hamiltonian})
chapters/theory/higher_genus_modular_koszul.tex:101: (Definition~\ref{def:shadow-postnikov-tower}).
chapters/theory/higher_genus_modular_koszul.tex:106: (Proposition~\ref{prop:master-equation-from-mc}), the
chapters/theory/higher_genus_modular_koszul.tex:112: Theorem~\ref{thm:recursive-existence}:
chapters/theory/higher_genus_modular_koszul.tex:126: (Theorem~\ref{thm:riccati-algebraicity}). On any one-dimensional
chapters/theory/higher_genus_modular_koszul.tex:132: (Theorem~\ref{thm:single-line-dichotomy}):
chapters/theory/higher_genus_modular_koszul.tex:146: No other depths occur (Proposition~\ref{prop:depth-gap-trichotomy}):
chapters/theory/higher_genus_modular_koszul.tex:150: (Theorem~\ref{thm:shadow-formality-identification}). The
chapters/theory/higher_genus_modular_koszul.tex:161: (Theorem~\ref{thm:quantum-complementarity-main}). For a Koszul pair
chapters/theory/higher_genus_modular_koszul.tex:178:(Construction~\ref{constr:dk-shadow-projections};
chapters/theory/higher_genus_modular_koszul.tex:179:Proposition~\ref{prop:e1-shadow-r-matrix}) recovers the classical
chapters/theory/higher_genus_modular_koszul.tex:184:Theorem~\ref{thm:gz26-commuting-differentials}; the Gaudin
 succeeded in 51ms:
Total output lines: 791

appendices/general_relations.tex:28:Each entry represents a precise functor or natural transformation between categories. For instance, the correspondence ``Chiral multiplication $\leftrightarrow$ Residues at collision divisors'' is the content of Theorem~\ref{thm:residue-formula}, establishing that the multiplication map factors through the residue homomorphism. Similarly, ``Central extensions $\leftrightarrow$ Curved $A_\infty$ structures'' reflects Theorem~\ref{thm:heisenberg-bar}, showing how the failure of strict associativity due to central charges is precisely captured by the curvature term $m_0$.
appendices/general_relations.tex:127:That is, when the curvature element is central, $m_1$ is strictly nilpotent ($m_1^2 = 0$). This is exactly the algebraic condition ensuring $d_{\text{bar}}^2 = 0$ in the bar complex (see the nine-term proof in \S\ref{sec:bar-nilpotency}).
appendices/homotopy_transfer.tex:12:(Theorem~\ref{thm:bar-ainfty-complete}).
appendices/homotopy_transfer.tex:19:(Theorem~\ref{thm:rectification-meta}): given a deformation retract
appendices/homotopy_transfer.tex:40: (Theorem~\ref{thm:htt}) endows~$H$
appendices/homotopy_transfer.tex:63:$A_\infty$ algebras were introduced by Stasheff~\cite{Sta63} to encode the homotopy-coherent associativity of loop space multiplication. The operadic viewpoint identifies them as algebras over the homology of the little intervals operad. For the role of bar-cobar duality in the chiral setting, see Chapter~\ref{chap:higher-genus}.
appendices/homotopy_transfer.tex:134:$(V, W, p, \iota, h)$ satisfying the conditions of Theorem~\ref{thm:htt}. 
appendices/homotopy_transfer.tex:226:Only tree-level graphs contribute to homotopy transfer: the sum in Theorem~\ref{thm:tree-formula} runs over trees (acyclic connected graphs), never over graphs with loops. This is because the three side conditions $h^2 = 0$, $ph = 0$, and $h\iota = 0$ together ensure that any graph with a cycle vanishes: $h^2 = 0$ kills paths with consecutive homotopies, $ph = 0$ kills graphs where $h$ appears at the output edge, and $h\iota = 0$ kills graphs where $h$ appears at an input edge. In the chiral algebra setting, this means the transferred operations are algebraic (finite sums), not analytic, and no renormalization issues arise.
appendices/homotopy_transfer.tex:472:We apply the general homotopy transfer theorem (Theorem~\ref{thm:htt}) to the $\Eone$-chiral operad.
appendices/homotopy_transfer.tex:474:\emph{Step~1} (D-module compatibility). Since $\cA$ is a chiral algebra, it carries a $\cD_X$-module structure. The SDR maps $(p, \iota, h)$ must be morphisms of $\cD_X$-modules (i.e., commute with the action of $\cD_X$). This holds because chiral homology $H = H^{\mathrm{ch}}_*(\cA)$ is defined as a derived functor in the category of $\cD_X$-modules, so $p$ and $\iota$ are automatically $\cD_X$-linear, and $h$ can be chosen $\cD_X$-linearly by the splitting argument of Lemma~\ref{lem:sdr-existence}(i) applied within the $\cD_X$-module category (which is abelian with enough projectives over a smooth curve~$X$).
appendices/homotopy_transfer.tex:476:\emph{Step~2} (Transferred binary operation). The transferred product is $\tilde{m}_2 = p \circ \mu^{\mathrm{ch}} \circ (\iota \otimes \iota)$, exactly as in Construction~\ref{constr:transfer-ainf}. Since $\mu^{\mathrm{ch}}$ is a chiral product (defined via the $j_*j^*$ functor on $X \times X$), $\tilde{m}_2$ inherits $\cD_X$-linearity from Step~1.
appendices/homotopy_transfer.tex:478:\emph{Step~3} (Higher operations via trees). The transferred operations $\tilde{m}_n^{\mathrm{ch}}$ for $n \geq 3$ are sums over planar rooted trees with $n$ leaves (as in Construction~\ref{constr:transfer-ainf}), where each internal edge contributes a factor of $h$ and each internal vertex contributes the chiral product $\mu^{\mathrm{ch}}$. Since only tree-level graphs contribute (no loops; cf.\ Remark~\ref{rem:tree-level}), each $\tilde{m}_n^{\mathrm{ch}}$ is a finite sum.
appendices/homotopy_transfer.tex:482:\emph{Koszulness} (iii). If $\cA$ is Koszul, the bar spectral sequence degenerates at $E_2$ with $E_\infty$ concentrated on the Koszul line $q = 0$ (Proposition~\ref{prop:degen-koszul}). This means $\mathrm{Ext}^{p,q}_{\cA}(k,k) = 0$ for $q \neq 0$: the bar resolution is minimal. One may therefore choose the SDR for $\Bbar(\cA) \to H^*(\Bbar(\cA))$ compatible with the bigrading, so that the homotopy $h$ preserves bar degree and shifts internal degree. Every tree contributing to $\tilde{m}_n^{\mathrm{ch}}$ for $n \geq 3$ would produce an operation of bar-degree shift incompatible with the Koszul line concentration, forcing $\tilde{m}_n^{\mathrm{ch}} = 0$. Equivalently, for a minimal resolution all Massey products vanish.
appendices/homotopy_transfer.tex:507:The bar construction is functorial for $\Ainf$-morphisms \cite{LV12}: an $\Ainf$-quasi-isomorphism $f: A \xrightarrow{\sim} B$ induces a quasi-isomorphism $\Bbar(f): \Bbar(A) \xrightarrow{\sim} \Bbar(B)$ of bar complexes. (The functoriality of $\barB$ for $A_\infty$-morphisms is the bar-cobar adjunction as a quantum $L_\infty$ functor.) Since the SDR maps $(\iota, p)$ extend to $\Ainf$-quasi-isomorphisms by Theorem~\ref{thm:htt}, the bar complexes $\Bbar(\cA)$ and $\Bbar(H, \{\tilde{m}_n\})$ are quasi-isomorphic. The geometric realization is compatible because $\Bbar^{\mathrm{geom}}$ is computed as the factorization homology of $\Bbar$, and factorization homology preserves quasi-isomorphisms between factorization algebras on $X$.
appendices/homotopy_transfer.tex:531:of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} is the
appendices/homotopy_transfer.tex:533:transfer theorem (Theorem~\ref{thm:htt}), applied to the SDR
appendices/homotopy_transfer.tex:555:(Proposition~\ref{prop:degen-koszul}). The $E_1$-degeneration
appendices/homotopy_transfer.tex:563:Applying Theorem~\ref{thm:htt} to the strict $\Eone$-chiral algebra

thinking
**Searching for seam issues**

I think I should check the red_team_summary for any mentions of seam issues. My plan is to load the relevant sections and look specifically for appendices or any theoretical aspects that might shed light on this. It seems crucial to gather all the information to ensure I don't miss anything important related to the seam problems. Let’s search through that summary to find the right details!
codex
I’ve isolated the seam files the body actually leans on: `appendices/nonlinear_modular_shadows.tex`, `appendices/homotopy_transfer.tex`, `appendices/branch_line_reductions.tex`, `appendices/arnold_relations.tex`, and the signs appendix. I’m now reading those exact source statements against the theory-side invocation points to see whether the body is citing proofs, merely previewing them, or accidentally depending on them.
exec
/bin/zsh -lc "rg -n 'appendix|Appendix|app:' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'appendix|Appendix|app:' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'appendices/|Appendix~\\\\ref\\{app:|Appendix~\\\\ref\\{sec:' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
59:| `appendices/ordered_associative_chiral_kd.tex` | 89 |
63:| `appendices/nonlinear_modular_shadows.tex` | 69 |
3215:#### `appendices/_sl2_yangian_insert.tex` (8)
3228:#### `appendices/arnold_relations.tex` (6)
3239:#### `appendices/branch_line_reductions.tex` (21)
3265:#### `appendices/combinatorial_frontier.tex` (1)
3271:#### `appendices/dual_methodology.tex` (1)
3277:#### `appendices/homotopy_transfer.tex` (6)
3288:#### `appendices/koszul_reference.tex` (7)
3300:#### `appendices/nonlinear_modular_shadows.tex` (69)
3374:#### `appendices/ordered_associative_chiral_kd.tex` (89)
3468:#### `appendices/signs_and_shifts.tex` (4)
3477:#### `appendices/spectral_higher_genus.tex` (1)
 succeeded in 52ms:
1125:In Loday--Vallette \cite{LV12}, \S7.1--7.2, the Koszul dual includes the sign representation: $\Ass^! = \Ass \otimes \mathrm{sgn}$ and $\Com^! = \Lie\{1\}$ (with operadic suspension). In this manuscript, we absorb the sign twist into the bar desuspension: our bar construction uses the shifted generators $s^{-1}\mathcal{A}$ whose sign already accounts for the $\mathrm{sgn}$-twist. Concretely, our convention $\Ass^! \cong \Ass$ means that the dual cooperad is isomorphic to $\Ass$ as a \emph{graded} cooperad after this shift. All bar-cobar computations in the text use the desuspended convention consistently, so no sign errors propagate. See Appendix~\ref{app:signs} for the explicit translation between conventions.
2047: (Chapter~\ref{app:nonlinear-modular-shadows}) makes the
2063:\item The \emph{branch-line reductions} appendix
2064: (Appendix~\ref{app:branch-line-reductions}) extracts exact
2241:Three axes, each with its own appendix chain:
3217: & App.~\ref{app:nonlinear-modular-shadows} \\
3220: & App.~\ref{app:nonlinear-modular-shadows} \\
4938:$\operatorname{Ran}(X)$ (cf.\ Appendix~\ref{app:existence-criteria}).
5017:Appendix~\ref{app:existence-criteria} compares the strict,
5022:Appendix~\ref{app:coderived},
6597:(Appendix~\ref{app:nonlinear-modular-shadows}).
exec
/bin/zsh -lc 'ls archive/raeeznotes/raeeznotes100 red_team_summary.md raeeznotes/raeeznotes100 2>/dev/null' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
archive/raeeznotes/raeeznotes100:
informal_claim_harvest.csv
label_status_conflicts.csv
master_claim_ledger_filtered.csv
provisionally_dismissed_claims.csv
red_team_summary.md
suspicious_proved_claim_dependencies.csv

thinking
**Searching for summaries**

I think I need to read the red team summary sections that are relevant. It feels like this will help me gather the information I need, but I want to be sure I’m looking in the right place. I’ll check the fixed path to see if I can find those sections easily. It’s always good to be thorough and make sure I’m not missing anything important. Let’s see what I can discover there!
exec
/bin/zsh -lc "rg -n 'appendix|Appendix|appendices|theory|sign|homotopy transfer|nonlinear modular shadows|branch-line|Arnold' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
31:- **9 label-status conflicts** exist across files/volumes. This is claim drift: the same label is not stably assigned a single epistemic status.
53:- V1 `chapters/theory/koszul_pair_structure.tex`: **14** conjectural / conditional / heuristic / open claims
54:- V1 `chapters/theory/chiral_hochschild_koszul.tex`: **13** conjectural / conditional / heuristic / open claims
71:- V1 `chapters/theory/higher_genus_modular_koszul.tex`: **4** proved-here claims with suspicious dependencies
78:- V1 `chapters/connections/ym_boundary_theory.tex`: **1** proved-here claims with suspicious dependencies
83:- V1 `chapters/theory/bar_cobar_adjunction_inversion.tex`: **1** proved-here claims with suspicious dependencies
95:- `thm:ym-bar-bridge` (V1 `chapters/connections/ym_boundary_theory.tex:58`): proved here, but cites `thm:conditional-mass-gap-transfer:Conditional,Conjectured`.
105:- `thm:grand-synthesis-principle` has statuses **Conditional,ProvedHere** across instances: V1:ProvedHere:chapters/connections/ym_boundary_theory.tex:128:Grand synthesis principle || V2:Conditional:chapters/connections/ym_synthesis.tex:36:Grand synthesis principle; \ClaimStatusConditional || V2:Conditional:chapters/connections/ym_...
107:- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
108:- `conj:DS` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1309:Reduction commutes with associative chiral duality || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1457: || V2:ProvedHere:chapters/connections/ordered_...
109:- `lem:PVA2_proof` has statuses **ProvedHere,Unknown** across instances: V2:Unknown:chapters/theory/pva-descent.tex:149:Alternative derivation of PVA2 via vertex algebra modes || V2:ProvedHere:chapters/theory/pva-descent-repaired.tex:375:Chain-level exchange homotopies; \ClaimStatusProvedHere...
113:- Volume I core theory and the explicitly tagged examples are safer than the high-energy connection/frontier material, but still need local proof verification claim by claim.

thinking
**Investigating suspicious dependencies**

I'm considering the possibility of suspicious dependencies concerning higher_genus_modular_koszul. It seems important to examine the suspicious_claim_dependencies CSV for any issues related to appendices. I'll need to conduct a search to analyze this further and clarify any concerns that might arise. It's always good to be thorough when it comes to dependencies to ensure everything is functioning as expected! Let's see what I can find.
exec
/bin/zsh -lc "rg -n 'higher_genus_modular_koszul|appendices/nonlinear_modular_shadows|appendices/homotopy_transfer|branch_line_reductions|arnold_relations|signs_and_shifts' archive/raeeznotes/raeeznotes100/suspicious_proved_claim_dependencies.csv" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
34:V1,chapters/theory/higher_genus_modular_koszul.tex,3155,thm:explicit-theta,Explicit universal MC class,theorem,ProvedHere,conj:scalar-saturation-universality:Conjectured
35:V1,chapters/theory/higher_genus_modular_koszul.tex,6724,cor:scalar-saturation,Scalar saturation of the universal MC class,corollary,ProvedHere,conj:scalar-saturation-universality:Conjectured
36:V1,chapters/theory/higher_genus_modular_koszul.tex,7115,prop:saturation-equivalence,Saturation equivalence criterion,proposition,ProvedHere,conj:scalar-saturation-universality:Conjectured
37:V1,chapters/theory/higher_genus_modular_koszul.tex,15606,cor:topological-recursion-mc-shadow,Topological recursion as MC shadow,corollary,ProvedHere,conj:EO-recursion:Conjectured

thinking
**Parsing labels and references**

I’m considering how to handle labels not prefixed by the app, like those defined in appendices. To capture everything, I need to map those labels and locate references in the theory section. It seems like a straightforward shell command might work, but it’s actually complex. A Python one-liner seems more suitable here. I’ll create a read-only Python script to build a label-to-definition mapping and scan for cross-references in both the theory and the appendices. This way, I can gather unique cross-references!
codex
The reference graph is large enough that manual grep isn’t enough. I’m extracting a resolved appendix↔theory cross-reference map now so I can check only real seam edges rather than sampling blindly.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, json
root=pathlib.Path('/Users/raeez/chiral-bar-cobar')
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat=re.compile(r'\\\\(?:ref|Cref|autoref|eqref)\\{(["'^}]+)'"\\}')
labels={}
for base in ['appendices','chapters/theory']:
    for path in (root/base).rglob('*.tex'):
        for i,line in enumerate(path.read_text().splitlines(),1):
            for m in label_pat.finditer(line):
                labels.setdefault(m.group(1),[]).append((str(path.relative_to(root)),i))

cross=[]
for src_base, dst_base in [('chapters/theory','appendices'),('appendices','chapters/theory')]:
    for path in (root/src_base).rglob('*.tex'):
        for i,line in enumerate(path.read_text().splitlines(),1):
            for m in ref_pat.finditer(line):
                label=m.group(1)
                defs=labels.get(label,[])
                for dpath,dline in defs:
                    if dpath.startswith(dst_base):
                        cross.append((src_base,str(path.relative_to(root)),i,label,dpath,dline,line.strip()))
print(json.dumps(cross,indent=2))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 96ms:
[
  [
    "chapters/theory",
    "chapters/theory/higher_genus_complementarity.tex",
    96,
    "app:nonlinear-modular-shadows",
    "appendices/nonlinear_modular_shadows.tex",
    2,
    "\\textup{(}Appendix~\\textup{\\ref{app:nonlinear-modular-shadows})}."
  ],
  [
    "chapters/theory",
    "chapters/theory/higher_genus_complementarity.tex",
    1308,
    "app:signs",
    "appendices/signs_and_shifts.tex",
    2,
    "This sign is precisely the Koszul sign convention (see Appendix~\\ref{app:signs}, \\S\\ref{app:sign-conventions})."
  ],
  [


thinking
**Assessing cross-references**

I need to summarize counts per file and possibly detect any reciprocal references or cycles. The user mentioned exhaustively examining the seam surface, but maybe I should focus specifically on mission appendices and theories. Manually inspecting 7319 lines seems impractical, so I think narrowing down to relevant external appendices is key. I should also compare the duplicated files to find inconsistencies. The goal is to identify real problems, not just list all references. I might need algorithmic checks for efficiency.
thinking
**Identifying duplicate references**

I see there’s an appendix file and a chapter with the same labels, which could lead to duplicates or drift. I’m thinking of using `diff -u` and `rg` to find any duplicate labels between the appendices and the theory sections. This could highlight ambiguous cross-references, indicating a seam issue. I might need to rename one side or delete the duplicate file to resolve this. It's also crucial to check how these duplicates affect reference resolution in LaTeX, since it can be unpredictable. Let's compute those duplicates!
codex
One seam failure is already visible structurally: some labels exist on both sides of the seam, which makes citation resolution unstable before we even get to the mathematics. I’m enumerating those duplicate label collisions now and checking whether they are accidental copies or genuinely divergent statements.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, collections
root=pathlib.Path('/Users/raeez/chiral-bar-cobar')
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
locs=collections.defaultdict(list)
for base in ['appendices','chapters/theory']:
    for path in (root/base).rglob('*.tex'):
        for i,line in enumerate(path.read_text().splitlines(),1):
            for m in label_pat.finditer(line):
                locs[m.group(1)].append((str(path.relative_to(root)),i))
# duplicates across the two roots only
for label, defs in sorted(locs.items()):
    roots={d[0].split('/')[0] for d in defs}
    if len(defs)>1 and roots=={'appendices','chapters'}:
        print(label)
        for p,l in defs:
            print(f'  {p}:{l}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
D1
  appendices/ordered_associative_chiral_kd.tex:2805
  chapters/theory/ordered_associative_chiral_kd.tex:2491
D2
  appendices/ordered_associative_chiral_kd.tex:2807
  chapters/theory/ordered_associative_chiral_kd.tex:2493
D3
  appendices/ordered_associative_chiral_kd.tex:2810
  chapters/theory/ordered_associative_chiral_kd.tex:2496
D4
  appendices/ordered_associative_chiral_kd.tex:2812
  chapters/theory/ordered_associative_chiral_kd.tex:2498
D5
  appendices/ordered_associative_chiral_kd.tex:2814
  chapters/theory/ordered_associative_chiral_kd.tex:2500
D6
  appendices/ordered_associative_chiral_kd.tex:2818
  chapters/theory/ordered_associative_chiral_kd.tex:2504
ch:ordered-associative-chiral-kd
  appendices/ordered_associative_chiral_kd.tex:37

thinking
**Investigating duplicate labels**

I’m noticing huge duplicate labels, which seems significant. I need to check if both files are included in the build. If only one is in, those duplicates might be dormant. I’ll inspect the main tex for appended sections. I’ll search for any inclusions related to appendices or chapters to see if both are in the same build. It’s important to determine if these duplicate labels matter or if it’s just a theoretical overlap in the build process. I’ll use rg for this search.
exec
/bin/zsh -lc "rg -n 'ordered_associative_chiral_kd' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./main.tex:1140:\input{chapters/theory/ordered_associative_chiral_kd}
exec
/bin/zsh -lc "rg -n 'appendices/(ordered_associative_chiral_kd|nonlinear_modular_shadows|branch_line_reductions|homotopy_transfer|signs_and_shifts|arnold_relations)|chapters/theory/(ordered_associative_chiral_kd|higher_genus_modular_koszul|higher_genus_complementarity|higher_genus_foundations|bar_construction|chiral_hochschild_koszul|quantum_corrections)' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./main.tex:983:\include{chapters/theory/bar_construction}
./main.tex:1000:\input{appendices/homotopy_transfer}
./main.tex:1040:\include{chapters/theory/chiral_hochschild_koszul}
./main.tex:1048:\include{chapters/theory/quantum_corrections}
./main.tex:1093:\input{appendices/nonlinear_modular_shadows}
./main.tex:1097:\input{appendices/branch_line_reductions}
./main.tex:1140:\input{chapters/theory/ordered_associative_chiral_kd}
./main.tex:1529:\input{appendices/arnold_relations}
./main.tex:1530:\input{appendices/signs_and_shifts}
./chapters/theory/higher_genus.tex:4:\input{chapters/theory/higher_genus_foundations}
./chapters/theory/higher_genus.tex:5:\input{chapters/theory/higher_genus_complementarity}
./chapters/theory/higher_genus.tex:6:\input{chapters/theory/higher_genus_modular_koszul}
exec
/bin/zsh -lc "rg -n 'appendices/(general_relations|computational_tables|notation_index|koszul_reference|combinatorial_frontier|theta_functions)' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1351: \input{appendices/combinatorial_frontier}
1528:\input{appendices/general_relations}
1531:\input{appendices/theta_functions}
1533:\input{appendices/koszul_reference}
1537:\input{appendices/notation_index}
1539: \input{appendices/computational_tables}





thinking
**Identifying cycles in theory and appendices**

I need to figure out the mission seam between the appendices and the main theory. It’s crucial to address any actual issues. My approach involves using a cross-reference map and possibly automated checks for cycles. If an appendix and theory reference each other, that indicates a cycle. I’ll look for reciprocal edges and determine if any circularity is harmful. It’s important to inspect the content and statuses of these references carefully.
thinking
**Investigating potential circular references**

I have noticed some potential issues with quick outputs. In `higher_genus_complementarity.tex`, the body cites `thm:chiral-htt` and `thm:bar-cobar-htt` from `homotopy_transfer.tex`. I need to inspect these theorem statements and proofs since they might refer back to `quantum-complementarity-main`, which could create circularity. 

Additionally, in `quantum_corrections.tex`, the appendix cites `app:homotopy-transfer`, which might be acceptable. However, lines in `appendices/homotopy_transfer.tex` seem problematic with the claim about Massey products. Lastly, I need to verify the existence of labels like `thm:heisenberg-bar` in `appendices/general_relations.tex`.
thinking
**Clarifying appendix citations and consistency**

I see that `general_relations` is included as an appendix, but it might not be cited in the main theory. According to the mission, results from appendices should be correctly referenced in the body. I need to double-check whether `general_relations` is indeed cited. Additionally, I should verify that there are no circular dependencies and that the notation is consistent throughout. It’s important to ensure everything aligns properly to avoid any confusion later on.
thinking
**Investigating theorem references**

I’m trying to determine when a theorem statement or proof in the appendix references a theorem from the theory. It sounds like I’ll have to manually check a few appendix labels used in the body. I want to list the unique appendix labels referenced in the theory. Then, I’ll group and count them to get a clear picture. If there are duplicates from chapter copies, I need to exclude those for accuracy. This might clarify how the theorem references are working.
thinking
**Computing unique appendix labels**

I need to make sure to exclude any labels that are also defined in the theory because they might be counted as a seam due to duplicates in the appendix. However, in the build, they end up resolving to chapter-local definitions rather than appendix ones, so I won’t need to audit those for seams. I can focus on the unique labels defined only in the appendices. I’ll set up a script to compute these unique appendix labels referenced by the theory.
codex
I’ve ruled out one false seam: most of the enormous `ordered_associative_chiral_kd` cross-links are artifacts of a dormant appendix copy, while `main.tex` only includes the chapter version. I’m filtering those out so the audit stays on live references that actually affect the build.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, pathlib, collections
root=pathlib.Path('/Users/raeez/chiral-bar-cobar')
label_pat=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ref_pat=re.compile(r'\\\\(?:ref|Cref|autoref|eqref)\\{(["'^}]+)'"\\}')
labels=collections.defaultdict(list)
for base in ['appendices','chapters/theory']:
    for path in (root/base).rglob('*.tex'):
        for i,line in enumerate(path.read_text().splitlines(),1):
            for m in label_pat.finditer(line):
                labels[m.group(1)].append((str(path.relative_to(root)),i))
# labels unique to appendices only
appendix_only={k:v[0] for k,v in labels.items() if len(v)==1 and v[0][0].startswith('appendices/')}
# theory refs to appendix-only labels
hits=collections.defaultdict(list)
for path in (root/'chapters/theory').rglob('*.tex'):
    for i,line in enumerate(path.read_text().splitlines(),1):
        for m in ref_pat.finditer(line):
            label=m.group(1)
            if label in appendix_only:
                hits[label].append((str(path.relative_to(root)),i,line.strip()))
for label,(dpath,dline) in sorted(appendix_only.items(), key=lambda kv:(kv[1][0],kv[1][1])):
    if label in hits:
        print(f'{label} <- {dpath}:{dline}')
        for p,l,t in hits[label]:
            print(f'  {p}:{l}: {t}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 79ms:
thm:sl2-koszul-dual <- appendices/_sl2_yangian_insert.tex:533
  chapters/theory/chiral_modules.tex:2874: (Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
  chapters/theory/chiral_modules.tex:2946: (Theorem~\ref{thm:sl2-koszul-dual}), the module Koszul duality
  chapters/theory/chiral_modules.tex:2967: Theorem~\ref{thm:sl2-koszul-dual},
app:arnold-relations <- appendices/arnold_relations.tex:1
  chapters/theory/bar_construction.tex:1225: By Arnol'd~\cite{Arnold69}, the 1-forms $\eta_{ij} = d\log(z_i - z_j)$ generate $H^*(C_n(\mathbb{C}); \mathbb{Q})$ and satisfy the Arnold relations $\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$. That these generate \emph{all} relations follows from Cohen's computation of $H^*(C_n(\mathbb{C}))$ as the cohomology of the Arnol'd--Brieskorn braid arrangement complement~\cite{Coh76}. See also Appendix~\ref{app:arnold-relations} for the three proofs of the Arnold relations used in this monograph.
cor:bar-d-squared-zero-arnold <- appendices/arnold_relations.tex:164
  chapters/theory/en_koszul_duality.tex:505: (Corollary~\ref{cor:bar-d-squared-zero-arnold}), with the Arnold
thm:arnold-iff-nilpotent <- appendices/arnold_relations.tex:180
  chapters/theory/configuration_spaces.tex:83: Theorem~\ref{thm:arnold-iff-nilpotent}; at genus~$0$ the
  chapters/theory/configuration_spaces.tex:3829: and Theorem~\ref{thm:arnold-iff-nilpotent} shows that the Arnold
app:branch-line-reductions <- appendices/branch_line_reductions.tex:2
  chapters/theory/chiral_hochschild_koszul.tex:5745: Appendix~\ref{app:branch-line-reductions} extracts exact
  chapters/theory/chiral_hochschild_koszul.tex:5777: (Appendix~\ref{app:branch-line-reductions}) are the spectral
  chapters/theory/introduction.tex:1956: (Appendix~\ref{app:branch-line-reductions}) extract exact
app:combinatorial-frontier <- appendices/combinatorial_frontier.tex:2
  chapters/theory/introduction.tex:2253: Computations + combinatorial frontier (Chs.~\ref{chap:detailed-computations}--\ref{app:combinatorial-frontier}) &
  chapters/theory/chiral_koszul_pairs.tex:1099: Bar cohomology of a non-abelian chiral Koszul algebra is the CE cohomology of $\fg \otimes t^{-1}\bC[t^{-1}]$, not the exterior algebra $\Lambda^n(V^*)$. For $\widehat{\mathfrak{sl}}_2$: $E_1$ totals $= \prod_{m \geq 1}(1+q^m)^3$, but $E_\infty = E_2 \neq E_1$ because the $d_1$ differential is nonzero for non-abelian $\fg$. In particular, $\dim H^2 = 5$ (not $R(5) = 6$; Appendix~\ref{app:combinatorial-frontier}).
conj:w3-bar-gf <- appendices/combinatorial_frontier.tex:469
  chapters/theory/higher_genus_modular_koszul.tex:34822: and~\ref{conj:w3-bar-gf}) is the first example where the
codex
The homotopy-transfer appendix is one of the main load-bearing seam files, so I’m reading its actual theorem statements and proof dependencies next. I’m checking whether the body cites those results as proved inputs when the appendix itself leans back on later theory theorems or changes convention midstream.
exec
/bin/zsh -lc "sed -n '1120,1185p' chapters/theory/nilpotent_completion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,560p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1560,1675p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4760,4810p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
This is the required topological nilpotence. The perturbation
argument used in the proof of
Theorem~\ref{thm:resonance-filtered-bar-cobar} depends only on
that nilpotence, so it applies here with the decreasing
filtration
\[
\mathcal F^p
:=
\{\text{bar chains of positive conformal weight } \le p\}.
\]
Combining this with Step~1 gives
\[
\widehat{\bar B}(\cA)
\simeq
\widehat{\bar B}^{\mathrm{st}}(\cA^+_\cA)
\;\widehat{\otimes}\;
\bar B(R_\cA),
\]
and the completed cobar recovers~$\cA$.

 succeeded in 51ms:
\end{construction}

\begin{example}[Transfer for symmetric coalgebra]
\label{ex:transfer-sym-coalg}
Let $C = S^c(V)$ be the symmetric coalgebra on a chain complex $(V, d_V)$. 
The coproduct is deconcatenation:
\[
\Delta(v_1 \cdots v_n) = \sum_{I \sqcup J = [n]} v_I \otimes v_J
\]
where $v_I = \prod_{i \in I} v_i$ (in order).

If $V \xrightarrow{p} H_*(V) =: W$ is a deformation retract:
\begin{enumerate}[label=(\roman*)]
\item $\tilde{\Delta}_2$ on $S^c(W)$ is the standard deconcatenation (symmetric coalgebra).
\item $\tilde{\Delta}_3$ involves Massey products: corrections arise when $d_V$ is nontrivial.
\item If $V$ is formal (quasi-isomorphic to $H_*(V)$ with zero differential), then $\tilde{\Delta}_n = 0$ for $n \geq 3$.
\end{enumerate}
\end{example}


 succeeded in 51ms:
\[K_n(z_1, \ldots, z_n; w) = \sum_{i_1, \ldots, i_n} \frac{c_{i_1\ldots i_n}}{(z_1 - w)^{i_1} \cdots (z_n - w)^{i_n}}\]
encoding how fields behave near insertion points in CFT.
\end{example}

% ================================================================
% ================================================================

\subsection{Bar-cobar exchange}

\subsubsection{Chain/cochain level precision}

\begin{theorem}[Chain-level vs.\ homology-level structure; \ClaimStatusProvedHere]
\label{thm:chain-vs-homology}
Let $(\mathcal{A}, \{m_k\})$ be an $A_\infty$ chiral algebra.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Chain level.}
 The full $A_\infty$ structure $\{m_k\}_{k \geq 1}$ is preserved,
 all operations are computable via configuration space integrals,
 and homotopies have geometric meaning as forms on
 $\overline{C}_n(X)$.
 succeeded in 51ms:
the off-Koszul regime has no chain-level analogue.
\end{remark}

\begin{proposition}[\texorpdfstring{$E_2$}{E2}-collapse as formality;
\ClaimStatusProvedHere]
\label{prop:e2-collapse-formality}
\index{formality!spectral sequence collapse}
On the Koszul locus, the following conditions on a chiral algebra
$\cA$ are equivalent:
\begin{enumerate}[label=(\roman*)]
\item The bar spectral sequence
$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g\Bbar_g(\cA))$
collapses at~$E_2$ for all $g \geq 0$.
\item The filtered $\Ainf$-algebra $\Omega_g(\Bbar_g(\cA))$ is
\emph{formal}: quasi-isomorphic to its cohomology with the
transferred $\Ainf$-structure
(Theorem~\textup{\ref{thm:chiral-htt}}).
\item The transferred higher operations satisfy
$\tilde{m}_n^{(g)} = 0$ for $n \geq 3$ and all~$g$
(Koszulness at all genera).
exec
/bin/zsh -lc "sed -n '560,640p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$h\iota = 0$ follow from the bigrading.

\emph{Step~2} (HTT produces the same map).
Applying Theorem~\ref{thm:htt} to the strict $\Eone$-chiral algebra
structure on $\Omega(\Bbar(\cA))$ and the SDR from Step~1 produces
transferred operations $\{\tilde{m}_n\}_{n \geq 2}$ on $\cA$
and an $\Ainf$-quasi-isomorphism $f_\infty \colon \cA \to
\Omega(\Bbar(\cA))$. The component $f_1 = \iota$ and the
binary product $\tilde{m}_2 = \psi \circ \mu \circ
(\iota \otimes \iota) = \mu_{\cA}$ (the original product on $\cA$,
since $\psi\iota = \mathrm{id}$).

\emph{Step~3} (Koszulness forces vanishing).
For $n \geq 3$, each tree $T$ contributing to $\tilde{m}_n$
(Construction~\ref{constr:transfer-ainf}) inserts at least one
homotopy~$h$ on an internal edge. Since $h$ lowers the filtration
degree by~$1$ and the Koszul-line concentration forces all
non-trivial cohomology to live on $q = 0$, the composition
$\psi \circ (\text{tree})\circ \iota^{\otimes n}$ vanishes: the
output lives in $q < 0$, which is empty. Therefore
exec
/bin/zsh -lc "sed -n '1830,1905p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3970,4065p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'label\\{thm:bar-cobar-isomorphism-main\\}|thm:bar-cobar-isomorphism-main|thm:bar-cobar-htt|thm:chiral-htt|prop:e2-collapse-formality' chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_foundations.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
$\psi_X$ as coacyclic by stratified Positselski inversion and the
Verdier-quotient criterion for
$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.

\item \emph{Coderived bar-degree filtration.}
On the strict square-zero surface, existence and collapse are exactly
Theorems~\ref{thm:bar-cobar-spectral-sequence}
and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
replaces ordinary abutment by coacyclicity of the cone: the
associated-graded $E_1$ page is strict because the curvature term lies
in positive filtration.

\item \emph{Promotion lane.}
If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
coderived and ordinary derived categories and the coderived
equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
any class~$G/L$ collapse input for the coderived bar-degree spectral
 succeeded in 50ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:340:The cobar-bar adjunction $\Omega \dashv B$ restricts to an equivalence on pro-nilpotent objects by the filtered analogue of Theorem~\ref{thm:bar-cobar-isomorphism-main}; the completion $\widehat{\bar{B}}(\mathcal{A})$ is pro-nilpotent by construction, so $\Omega(\widehat{\bar{B}}(\mathcal{A})) \simeq \widehat{\mathcal{A}}$. See Positselski~\cite{Positselski11} for the general framework of curved Koszul duality with completions.
chapters/theory/bar_cobar_adjunction_inversion.tex:3563:Theorem~\ref{thm:bar-cobar-isomorphism-main}: the Verdier dual of the
chapters/theory/bar_cobar_adjunction_inversion.tex:3650:(Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/theory/higher_genus_foundations.tex:1253:Proposition~\ref{prop:e2-collapse-formality}).
chapters/theory/higher_genus_foundations.tex:2556:(a consequence of $E_2$ collapse on the Koszul locus; see Proposition~\ref{prop:e2-collapse-formality}).
chapters/theory/higher_genus_foundations.tex:2567:\begin{remark}[Summary of Theorem~A; see Theorem~\ref{thm:bar-cobar-isomorphism-main}]
chapters/theory/higher_genus_foundations.tex:2570:(Theorem~\ref{thm:bar-cobar-isomorphism-main},
chapters/theory/higher_genus_foundations.tex:2586:\label{thm:bar-cobar-isomorphism-main-equations}
chapters/theory/higher_genus_foundations.tex:2650:See Theorem~\ref{thm:bar-cobar-isomorphism-main}
chapters/theory/higher_genus_foundations.tex:5497: Theorem~\ref{thm:bar-cobar-isomorphism-main-equations}
chapters/theory/higher_genus_complementarity.tex:4765:\label{prop:e2-collapse-formality}
chapters/theory/higher_genus_complementarity.tex:4776:(Theorem~\textup{\ref{thm:chiral-htt}}).
chapters/theory/higher_genus_complementarity.tex:4792:of Theorem~\ref{thm:bar-cobar-htt}, and the transferred structure
chapters/theory/higher_genus_complementarity.tex:5574:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) and higher-genus
chapters/theory/chiral_koszul_pairs.tex:46:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
chapters/theory/chiral_koszul_pairs.tex:568: (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
chapters/theory/chiral_koszul_pairs.tex:668:Theorem~\ref{thm:bar-cobar-isomorphism-main} then
chapters/theory/chiral_koszul_pairs.tex:714:Applying Theorem~\ref{thm:bar-cobar-isomorphism-main} to this bar
chapters/theory/chiral_koszul_pairs.tex:4014:\label{thm:bar-cobar-isomorphism-main}
chapters/theory/chiral_koszul_pairs.tex:4100:Theorem~\ref{thm:bar-cobar-isomorphism-main} at the H-level of


thinking
**Evaluating theorem dependencies**

I need to find out if the theorem bar-cobar-isomorphism-main relies on HTT. From the proof excerpt, it seems it might not. For instance, the theorem bar-cobar-htt uses the bar-cobar theorem, but that shouldn’t be circular unless bar-cobar-htt is referenced in proving something independent. In the higher genus complementarity property, e2-collapse-formality does reference bar-cobar-htt and chiral-htt, so I have to check if it supports earlier concepts. If it appears later, it could still be fine, but I need to be cautious about mis-citations.
thinking
**Inspecting dependencies and citations**

I’m checking the main include order for homotopy_transfer, which is at line 1000, probably before higher_genus_complementarity. However, the logical dependencies might not match the compile order, so I need to identify any circular dependencies. Each seam label in the theory could reference back to the same proposition in the appendix, and there could be cycles. For example, e2-collapse-formality may not be a seam label, but there’s a remark at line 593 referencing homotopy-native-b. More importantly, theorem bar-cobar-htt does use bar-cobar-isomorphism-main, but it won't be circular if the body avoids using bar-cobar-htt to prove it. I need to check for any mis-citations or notation mismatches as well.
exec
/bin/zsh -lc "nl -ba chapters/theory/quantum_corrections.tex | sed -n '340,385p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '610,700p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'eta_\\{123\\}|eta123|propagator|Fulton--MacPherson|binary trees with 3 leaves|m_3' appendices/homotopy_transfer.tex chapters/theory/quantum_corrections.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   610	
   611	\subsection{Trees and boundary strata: the geometric HTT}
   612	
   613	The tree formula of Theorem~\ref{thm:tree-formula} has a direct
   614	geometric realization via the Fulton--MacPherson compactification.
   615	
   616	\begin{proposition}[Trees as boundary strata;
   617	\ClaimStatusProvedHere]
   618	\label{prop:trees-boundary-strata}
   619	\index{Fulton--MacPherson compactification!boundary strata}
   620	\index{homotopy transfer theorem!geometric realization}
   621	Let $T$ be a planar rooted tree with $n$ leaves contributing to the
   622	transferred operation $\tilde{m}_n$
   623	(Construction~\ref{constr:transfer-ainf}). The corresponding
   624	term in the tree formula equals the integral
   625	\[
   626	\tilde{m}_n^T(a_1, \ldots, a_n) \;=\;
   627	\int_{\partial_T \overline{C}_n(X)}
   628	\mathrm{ev}^*(\bar{a}_1 \otimes \cdots \otimes \bar{a}_n)
   629	\;\wedge\;
 succeeded in 51ms:
   340	at genus~$2$ appears in~\S\ref{sec:koszul-across-genera}.
   341	
   342	\section{\texorpdfstring{The $A_\infty$ structure}{The A-infinity structure}}
   343	
   344	The $A_\infty$ structure (Stasheff~\cite{Sta63}) encodes the higher coherences for consistency across genera.
   345	
   346	\subsection{\texorpdfstring{The complete $A_\infty$ structure}{The complete A-infinity structure}}
   347	
   348	An $A_\infty$ algebra consists of operations $m_n: A^{\otimes n} \to A[2-n]$ for $n \geq 1$, satisfying:
   349	\[\sum_{\substack{r+s+t=n \\ r,t \geq 0,\; s \geq 1}} (-1)^{rs+t}\, m_{r+1+t}(\mathrm{id}^{\otimes r} \otimes m_s \otimes \mathrm{id}^{\otimes t}) = 0\]
   350	
   351	\subsubsection{For the bar complex}
   352	
   353	The bar complex of a chiral algebra carries a natural $A_\infty$ structure:
   354	
   355	\[m_1 = d_{\text{bar}}\]
   356	
   357	\[m_2(a \otimes b) = \text{Res}_{z_1=z_2}\left[\frac{a(z_1)b(z_2)}{z_1-z_2}\right]\]
   358	
   359	\[m_3(a \otimes b \otimes c) = \int_{\overline{C}_3(X)} a(z_1)\, b(z_2)\, c(z_3)\, \eta_{123}^{\text{FM}}\]
 succeeded in 50ms:
appendices/homotopy_transfer.tex:98:\tilde{m}_3 &= p \, m_3 \, \iota^{\otimes 3} + p \, m_2 (h m_2 \otimes \id) \, \iota^{\otimes 3}
appendices/homotopy_transfer.tex:193:\tilde{m}_3(a, b, c) &= p \, m_3(\iota(a), \iota(b), \iota(c)) \\
appendices/homotopy_transfer.tex:249:p \, m_3(h \, m_2 \otimes \id \otimes \id) \, \iota^{\otimes 4}, \quad
appendices/homotopy_transfer.tex:250:p \, m_2(h \, m_3 \otimes \id) \, \iota^{\otimes 4}, \quad \ldots
appendices/homotopy_transfer.tex:291:\item The resulting $(M, 0, m_2, m_3, \ldots)$ is the minimal model.
appendices/homotopy_transfer.tex:614:geometric realization via the Fulton--MacPherson compactification.
appendices/homotopy_transfer.tex:619:\index{Fulton--MacPherson compactification!boundary strata}
appendices/homotopy_transfer.tex:636:Fulton--MacPherson compactification indexed by~$T$: the locus
appendices/homotopy_transfer.tex:639:propagator on the internal edge~$e$ with source $s(e)$ and
appendices/homotopy_transfer.tex:656:The Fulton--MacPherson compactification
appendices/homotopy_transfer.tex:678:\prod_e h \circ \iota^{\otimes n}$ places propagators $\omega_e$
appendices/homotopy_transfer.tex:682:product of logarithmic propagators.
appendices/homotopy_transfer.tex:756:Eisenstein propagator on the elliptic curve, and $m_3$
chapters/theory/quantum_corrections.tex:61:Strict genus-$0$ nilpotence breaks once the propagator remembers the
chapters/theory/quantum_corrections.tex:266:propagator and produces the Arakelov $(1,1)$-form
chapters/theory/quantum_corrections.tex:359:\[m_3(a \otimes b \otimes c) = \int_{\overline{C}_3(X)} a(z_1)\, b(z_2)\, c(z_3)\, \eta_{123}^{\text{FM}}\]
chapters/theory/quantum_corrections.tex:360:where $\eta_{123}^{\text{FM}}$ is the propagator form on the Fulton--MacPherson compactification $\overline{C}_3(X)$, defined via homotopy transfer (cf.\ Appendix~\ref{app:homotopy-transfer}). Concretely, $m_3$ sums over binary trees with 3 leaves, each tree contributing an iterated composition of $m_2$ with the contracting homotopy $h$:
chapters/theory/quantum_corrections.tex:361:\[m_3(a, b, c) = m_2(m_2(a, b) \cdot h,\, c) + m_2(a,\, h \cdot m_2(b, c))\]
chapters/theory/quantum_corrections.tex:371:With background charge $Q$: $m_0$ is the degree-$2$ curvature element determined by $Q$ and $c_{\beta\gamma}$; $m_1$ is the BRST differential (satisfying the curved relation $m_1^2(a) = [m_0, a]$); $m_2$ is the standard OPE product; and $m_3$ is the transferred ternary operation from homotopy transfer on $\overline{C}_3(\mathbb{C})$, whose coefficient depends on the OPE structure constants of the $\beta\gamma$ system.
chapters/theory/quantum_corrections.tex:373:\subsubsection{\texorpdfstring{Explicit computation of $m_3$ for $\beta\gamma$}{Explicit computation of m 3 for beta-gamma}}
exec
/bin/zsh -lc "rg -n 'eta_\\{123\\}\\"'^'"\\{\\\\text\\{FM\\}\\}|eta_\\{123\\}|FM\\}' chapters/theory/quantum_corrections.tex appendices/homotopy_transfer.tex chapters/theory -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/quantum_corrections.tex:359:\[m_3(a \otimes b \otimes c) = \int_{\overline{C}_3(X)} a(z_1)\, b(z_2)\, c(z_3)\, \eta_{123}^{\text{FM}}\]
chapters/theory/quantum_corrections.tex:360:where $\eta_{123}^{\text{FM}}$ is the propagator form on the Fulton--MacPherson compactification $\overline{C}_3(X)$, defined via homotopy transfer (cf.\ Appendix~\ref{app:homotopy-transfer}). Concretely, $m_3$ sums over binary trees with 3 leaves, each tree contributing an iterated composition of $m_2$ with the contracting homotopy $h$:
chapters/theory/quantum_corrections.tex:980:$\overline{\mathrm{FM}}_3(\mathbb{C})$: it is the homotopy-transfer
chapters/theory/quantum_corrections.tex:993: $\overline{\mathrm{FM}}_3(\mathbb{C})$ on the bar side
chapters/theory/quantum_corrections.tex:1035: Associahedra $K_n \subset \overline{\mathrm{FM}}_n(\mathbb{C})$ \\
chapters/theory/higher_genus_modular_koszul.tex:8178: Proposition~\textup{\ref{prop:stokes-regularity-FM}}\textup{)}.
chapters/theory/higher_genus_modular_koszul.tex:8201:(Proposition~\ref{prop:stokes-regularity-FM}) and the Fay
chapters/theory/higher_genus_modular_koszul.tex:10900: $C_*(\operatorname{FM}^{\mathrm{log}}_n)$
chapters/theory/higher_genus_modular_koszul.tex:11313:\cC^{\log\mathrm{FM}}_{X \mathbin{|} D}(n)
chapters/theory/higher_genus_modular_koszul.tex:11315:C_\bullet\!\bigl(\operatorname{FM}_n(X \mathbin{|} D)\bigr),
chapters/theory/higher_genus_modular_koszul.tex:11317:\cC^{\log\mathrm{FM}}_{W/B}(n)
chapters/theory/higher_genus_modular_koszul.tex:11319:C_\bullet\!\bigl(\operatorname{FM}_n(W/B)\bigr).
chapters/theory/higher_genus_modular_koszul.tex:11324:of $\operatorname{FM}_n(X \mathbin{|} D)$ by planted forests and
chapters/theory/higher_genus_modular_koszul.tex:11335:\operatorname{FM}_n(W/B)(\rho)
chapters/theory/higher_genus_modular_koszul.tex:11338:\operatorname{FM}_{I_v}(Y_v \mathbin{|} D_v),
chapters/theory/higher_genus_modular_koszul.tex:11353:$D^{\log}_{\Gamma}\subset \operatorname{FM}^{\log}_n(X\mathbin{|}D)$
chapters/theory/higher_genus_modular_koszul.tex:11360:\operatorname{FM}_{I_v}(Y_v\mathbin{|}D_v)
chapters/theory/higher_genus_modular_koszul.tex:11370:\cC^{\log\mathrm{FM}}_{\mathrm{mod}}(g,n)
chapters/theory/higher_genus_modular_koszul.tex:11373:\cC^{\log\mathrm{FM}}_{\mathrm{mod}}\!\bigl(g(v),\,I_v\sqcup H(v)\bigr)
chapters/theory/higher_genus_modular_koszul.tex:11419:\cC^{\log\mathrm{FM}}_{\mathrm{mod}},\,

thinking
**Investigating findings**

I need to gather more findings and take a closer look at the appendices, specifically the theory references related to `arnold_relations`. I wonder if there could be any circularity issues. The theorem `thm:arnold-iff-nilpotent` might be applicable to body configuration spaces, so I'll need to inspect that theorem and its context as well. It's a matter of searching for relevant references to clarify these ideas.
exec
/bin/zsh -lc "nl -ba appendices/arnold_relations.tex | sed -n '150,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   150	\[\frac{1}{(z_1-z_2)(z_2-z_3)} + \frac{1}{(z_2-z_3)(z_3-z_1)} + \frac{1}{(z_3-z_1)(z_1-z_2)} = 0\]
   151	
   152	This identity holds because multiplying through by $(z_1-z_2)(z_2-z_3)(z_3-z_1)$ gives
   153	the telescoping sum $(z_3-z_1) + (z_1-z_2) + (z_2-z_3) = 0$.
   154	
   155	\begin{remark}[Systematic verification]\label{rem:nine-term-detailed-arnold}
   156	The Arnold relations can be verified systematically for each triple $\{i,j,k\} \subset \{1,\ldots,n\}$:
   157	\begin{itemize}
   158	\item $n=3$: $\binom{3}{3} = 1$ relation (verified above)
   159	\item $n=4$: $\binom{4}{3} = 4$ relations (all follow from the $n=3$ case by restriction)
   160	\item $n=5$: $\binom{5}{3} = 10$ relations (similarly)
   161	\end{itemize}
   162	\end{remark}
   163	
   164	\begin{corollary}[Bar differential squares to zero; \ClaimStatusProvedHere]\label{cor:bar-d-squared-zero-arnold}
   165	The Arnold relations ensure $d^2 = 0$ for the geometric bar differential:
   166	\[d^2 = \sum_{\text{cycles}} [\operatorname{Res}_{D_i}, \operatorname{Res}_{D_j}] = 0\]
   167	because the residue commutators sum to zero by Arnold relations.
   168	\begin{proof}
   169	This is the content of Theorem~\ref{thm:bar-nilpotency-complete}, where the nine pairwise compositions of the three bar differential components are shown to cancel. The Arnold relations enter in the $d_{\mathrm{res}} \circ d_{\mathrm{res}}$ component.
exec
/bin/zsh -lc "nl -ba chapters/theory/configuration_spaces.tex | sed -n '60,95p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/configuration_spaces.tex | sed -n '3810,3845p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '485,515p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    60	genus-$0$ tangent-space screen. For nested collisions
    61	($S_1 \subset S_2 \subset \cdots$), this iterates to produce
    62	screens within screens, each genus~$0$, giving the full boundary
    63	stratification by stable trees. Second, the logarithmic
    64	$1$-forms $\eta_{ij} = d\log(z_i - z_j)$ extend across the
    65	boundary as sections of
    66	$\Omega^1_{\overline{C}_n(X)}(\log D)$ and satisfy the
    67	\emph{Arnold relation}
    68	(Theorem~\ref{thm:arnold-relations}):
    69	\begin{equation}\tag{$\star$}
    70	\eta_{ij} \wedge \eta_{jk}
    71	+ \eta_{jk} \wedge \eta_{ki}
    72	+ \eta_{ki} \wedge \eta_{ij} = 0
    73	\qquad (i,j,k \text{ distinct}).
    74	\end{equation}
    75	Third, this relation forces $d_{\mathrm{residue}}^2 = 0$
    76	(Theorem~\ref{thm:bar-nilpotency-complete}): the
    77	bar differential at degree~$2$ is a sum of double residues
    78	at pairs of collision divisors $D_{ij} \cap D_{jk}$, and
    79	the Arnold relation is the precise cancellation identity
 succeeded in 50ms:
   485	 boundary stratum $\partial_S$ of
   486	 $\overline{\Conf}_k(\bR^2)$
   487	 \textup{(}Proposition~\textup{\ref{prop:linking-sphere-residue})},
   488	\item $\mu_S\colon \bar{A}^{\otimes |S|} \to \bar{A}$ is the
   489	 $\Etwo$-multiplication indexed by the FM operad element
   490	 corresponding to the stratum~$\partial_S$.
   491	\end{itemize}
   492	\end{definition}
   493	
   494	\begin{theorem}[\texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations;
   495	\ClaimStatusProvedHere]
   496	\label{thm:e2-d-squared}
   497	\index{Totaro relations!and $d^2 = 0$}
   498	The differential $d_{\Etwo}$ of
   499	Definition~\textup{\ref{def:e2-bar-complex}} satisfies
   500	$d_{\Etwo}^2 = 0$.
   501	\end{theorem}
   502	
   503	\begin{proof}
   504	The proof follows the same structure as the chiral case
 succeeded in 50ms:
  3810	
  3811	 
  3812	\begin{proposition}[Residue evaluation complexity; \ClaimStatusProvedHere]
  3813	\label{prop:residue-evaluation-complexity}
  3814	The procedure of Construction~\ref{con:residue-evaluation} computes residues with complexity $O(n^2 \cdot T_{\mathrm{OPE}})$, where $T_{\mathrm{OPE}}$ is the time to look up an OPE coefficient.
  3815	\end{proposition}
  3816	
  3817	\begin{proof}
  3818	Correctness follows from the residue formula in Theorem~\ref{thm:residue-operations}: nonzero contributions arise only when the weight condition is satisfied, corresponding to simple poles. The procedure checks all $\binom{n}{2}$ pairs, each in time $T_{\mathrm{OPE}}$.
  3819	\end{proof}
  3820	
  3821	\section{Arnold relations: explicit computations and physical interpretation}
  3822	\label{sec:arnold-three-proofs-comprehensive}
  3823	\label{sec:arnold-chiral}
  3824	
  3825	The Arnold relation (Theorem~\ref{thm:arnold-relations}) was proved
  3826	by two independent methods in \S\ref{sec:FM-compactification}: the
  3827	partial-fraction argument and the coordinate-reduction argument. Both
  3828	establish the relation in $\Omega^2(C_n(X))$ for every $n \geq 3$,
  3829	and Theorem~\ref{thm:arnold-iff-nilpotent} shows that the Arnold


thinking
**Inspecting theorem references**

I’m identifying a potential issue in the configuration spaces, specifically looking at lines 68 and 82, which reference Theorem arnold-relations and Theorem arnold-iff-nilpotent. I need to check if the theorem label thm:arnold-relations is in the same chapter or appendix. It seems there are dependencies between proofs, particularly in the appendix, and I want to clarify if corollary references are independent or sloppy. Additionally, line 68 cites a theorem that might not be correctly noted. There's a potential notation issue too, but I’ll verify that.
thinking
**Inspecting potential dependencies**

I don’t have a seam problem, which is good! Now I need to look at the nonlinear_modular_shadows appendix. It has many body citations that could potentially hide circular dependencies. I suspect that the body section on higher_genus_modular_koszul may cite the appendix theorem thm:nms-archetype-trichotomy, while the appendix proof could be relying on body theorem thm:shadow-archetype-classification from the same file. I should search the excerpt around line 1208 to clarify that.
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1180,1228p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '2180,2215p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32040,32310p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '5428,5450p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1180	weight-changing subspace is linear), so
  1181	$m_3(\eta,\eta,\eta) = 0$ by the $A_\infty$ relation
  1182	$m_3 = m_2 \circ (h \otimes \mathrm{id}) \circ m_2 + \cdots$
  1183	applied to the vanishing binary input.
  1184	(2)~Rank-one abelian rigidity (Theorem~\ref{thm:nms-rank-one-rigidity}):
  1185	the weight-changing line is a one-dimensional cyclic subspace with
  1186	vanishing higher brackets.
  1187	Computational verification: \texttt{compute/lib/betagamma\_quartic\_contact.py}.
  1188	\end{proof}
  1189	
  1190	\begin{corollary}[Pure contact boundary law; \ClaimStatusProvedHere]
  1191	\label{cor:nms-betagamma-boundary-law}
  1192	On the weight/contact slice of $\beta\gamma$ one has
  1193	\[
  1194	\xi^*\mathfrak Q_{\beta\gamma}
  1195	=
  1196	H_{\beta\gamma}\star_{P_{\beta\gamma}}\mathfrak Q_{\beta\gamma}
  1197	+
  1198	\mathfrak Q_{\beta\gamma}\star_{P_{\beta\gamma}}H_{\beta\gamma}.
  1199	\]
 succeeded in 52ms:
  5428	$\ell_3^{\mathrm{tr}} \neq 0$ (Virasoro, $\mathcal{W}_N$).
  5429	\end{itemize}
  5430	The shadow obstruction tower is the homotopy structure made visible.
  5431	\end{remark}
  5432	
  5433	\begin{remark}[The three archetypes from the Lagrangian perspective]
  5434	\label{rem:three-archetypes-lagrangian}
  5435	The fake-complementarity criterion reframes the archetype trichotomy
  5436	(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
  5437	The Heisenberg is exactly fake: $S_{\mathcal{H}}$ is quadratic.
  5438	Affine $\widehat{\mathfrak{sl}}_2$ is cubic at leading order:
  5439	$S_{\mathrm{aff}} = \tfrac12 H + \tfrac16\kappa(a,[a,a])$,
  5440	so the dual Lagrangian bends cubically. The $\beta\gamma$ system is
  5441	quartic on the weight/contact slice. Virasoro is the first family
  5442	where the dual Lagrangian has both cubic and quartic bending,
  5443	and the complementarity potential is genuinely non-polynomial; its
  5444	shadow obstruction tower is infinite (Theorem~\ref{thm:nms-finite-termination}).
  5445	\end{remark}
  5446	
  5447	\begin{remark}[Shadow obstruction tower as period correction]
 succeeded in 52ms:
  2180	\qquad
  2181	\text{for generic $c$}.
  2182	\end{equation}
  2183	Consequently $\mathrm{Sh}_5(\mathrm{Vir})\neq 0$ generically: the Virasoro shadow obstruction tower does not terminate at quartic order.
  2184	\end{theorem}
  2185	
  2186	\begin{proof}
  2187	The gravitational cubic is $\mathfrak C_{\mathrm{Vir}}=2x^3$ and the contact quartic is $\mathfrak Q^{\mathrm{contact}}_{\mathrm{Vir}}=Q_0\,x^4$ with $Q_0=10/[c(5c+22)]\neq 0$ for generic~$c$. Their single-edge sewing contraction on the one-generator primary line with propagator $P=2/c$ produces a nonzero rank-$5$ tensor proportional to $Q_0/c$.\qedhere
  2188	\end{proof}
  2189	
  2190	\begin{theorem}[Finite termination for primitive archetypes; \ClaimStatusProvedHere]
  2191	\label{thm:nms-finite-termination}
  2192	For the three frame families, the shadow obstruction tower terminates at finite degree.
  2193	\begin{enumerate}[label=\textup{(\roman*)}]
  2194	\item \textbf{Heisenberg:} $\mathrm{Sh}_r(\mathcal H)=0$ for all $r\ge 3$. The tower is exactly Gaussian.
  2195	\item \textbf{Affine $\widehat{\mathfrak{sl}}_2$ \textup{(strict sector, minimal gauge):}} $\mathrm{Sh}_r(\mathrm{aff})=0$ for $r\ge 4$.
  2196	\item \textbf{$\beta\gamma$ \textup{(weight-changing line):}} $\mathrm{Sh}_r(\beta\gamma)|_L=0$ for $r\ge 3$ by rank-one abelian rigidity.
  2197	\end{enumerate}
  2198	In contrast, Virasoro has $\mathrm{Sh}_5\neq 0$ (Theorem~\ref{thm:nms-virasoro-quintic-forced}), and by induction on the all-degree master equation, the tower is generically infinite.
  2199	\end{theorem}
 succeeded in 52ms:
 32040	-\tfrac{1}{2}[\Theta^{(1)}, \Theta^{(1)}]$
 32041	is nonzero for every algebra with $\kappa \neq 0$
 32042	(the genus-$1$ BV operator $\Theta^{(1)} \neq 0$
 32043	on the Koszul locus), so it is always activated.
 32044	
 32045	The separating-clutching shell
 32046	$\Theta^{(2)}_{\mathrm{sep}\circ\mathrm{loop}} =
 32047	-\Delta(\Theta^{(1)}) - d_{\mathrm{sew}}^{(2)}$
 32048	is nonzero iff $\Theta^{(1)}$ has nontrivial
 32049	separating-node data, which occurs iff the cubic
 32050	shadow $\mathfrak{C}(\cA) \neq 0$, i.e.,
 32051	$\ell_3^{(0),\mathrm{tr}}|_{H^*} \neq 0$
 32052	(Proposition~\ref{prop:shadow-formality-low-degree}(ii)).
 32053	By the archetype classification
 32054	(Theorem~\ref{thm:nms-archetype-trichotomy}):
 32055	$\mathfrak{C} = 0$ for classes $G$ and $C$ (Heisenberg
 32056	and $\beta\gamma$); $\mathfrak{C} \neq 0$ for classes
 32057	$L$ and $M$ (affine and Virasoro).
 32058	
 32059	The planted-forest shell
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1228,1260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1228	\begin{proof}
  1229	The three cases follow from the explicit shadow computations:
  1230	Heisenberg shadow Gaussianity (Theorem~\ref{thm:nms-heisenberg-exact-linearity}),
  1231	affine cubic normal form (Theorem~\ref{thm:nms-affine-cubic-normal-form}),
  1232	and $\beta\gamma$ quartic birth (Theorem~\ref{thm:nms-betagamma-quartic-birth}).
  1233	\end{proof}
  1234	
  1235	\begin{theorem}[Rank-one abelian rigidity; \ClaimStatusProvedHere]
  1236	\label{thm:nms-rank-one-rigidity}
  1237	Let $L \subset V_{\cA}$ be a one-dimensional cyclic subspace on which all transferred higher brackets vanish:
  1238	\[
  1239	\ell_n^{\mathrm{tr}}\big|_L = 0 \qquad (n \ge 2).
  1240	\]
  1241	Then the restriction of the complementarity potential to $L$ is exactly quadratic. In particular, complementarity on $L$ is formally fake.
  1242	\end{theorem}
  1243	
  1244	\begin{proof}
  1245	On such a line the cyclic action expansion collapses to its quadratic Hessian part: every higher jet $\mathrm{Sh}_r(\Theta_{\cA})|_L$ for $r \ge 3$ involves at least one factor of some $\ell_n^{\mathrm{tr}}$ with $n \ge 2$, and all vanish.\qedhere
  1246	\end{proof}
  1247	
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3318,3460p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16932,16960p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12320,12345p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3318	Proposition~\ref{prop:pbw-universality};
  3319	MC4 compl.\ =
  3320	Theorem~\ref{thm:completed-bar-cobar-strong};
  3321	lattice filt.\ =
  3322	Theorem~\ref{thm:lattice:koszul-morphism};
  3323	null vect.\ = Kac--Shapovalov obstruction
  3324	(Theorem~\ref{thm:kac-shapovalov-koszulness});
  3325	Cartan~$H^2$ = abelian Cartan subalgebra classes
  3326	surviving in $H^2(\barB)$
  3327	(Remark~\ref{rem:admissible-koszul-status}).
  3328	\textit{Shadow}: archetype class $G$/$L$/$C$/$M$
  3329	(Theorem~\ref{thm:nms-archetype-trichotomy})
  3330	and shadow depth $r_{\max}$;
  3331	all four classes contain Koszul algebras
  3332	(shadow depth $\neq$ Koszulness).
  3333	
  3334	\smallskip\noindent
  3335	${}^{\dagger}$\,The symplectic fermion
  3336	($\beta\gamma$ at $\lambda = \tfrac{1}{2}$,
  3337	$c = -1$) \emph{is} chirally Koszul:
 succeeded in 50ms:
 12320	not assumed before them. This reading does not change the
 12321	theorem statements; it names a physical content the combinatorial
 12322	definition already carries.
 12323	\end{remark}
 12324	
 12325	\begin{remark}[Depth classification as holographic truncation]
 12326	\label{rem:depth-classification-holographic-truncation}
 12327	\index{depth classification!holographic truncation}
 12328	\index{shadow depth class!G/L/C/M}
 12329	\index{Brown--Henneaux!shadow tower reading}
 12330	Under the holographic reading of
 12331	Remark~\textup{\ref{rem:shadow-tower-holographic-interpretation}},
 12332	the four shadow depth classes $\mathbf{G}$, $\mathbf{L}$,
 12333	$\mathbf{C}$, $\mathbf{M}$
 12334	\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}
 12335	and Theorem~\textup{\ref{thm:nms-finite-termination}}\textup{)}
 12336	are truncation classes for the holographic correction series.
 12337	\begin{center}
 12338	\small
 12339	\renewcommand{\arraystretch}{1.2}
 succeeded in 52ms:
 16932	arising from independent cusp forms in $M_{r/2}$
 16933	\textup{(}\S\textup{\ref{sec:higher-depths})}. This does not create
 16934	new algebraic-shadow archetypes: for lattices one has
 16935	$d_{\mathrm{alg}} = 0$, so the extra depth is purely arithmetic.
 16936	\end{theorem}
 16937	
 16938	\begin{proof}
 16939	Each case follows from the established vanishing theorems:
 16940	
 16941	(i)~For Heisenberg and lattice VOAs, the bar complex is strictly
 16942	coassociative ($m_k = 0$ for $k \geq 3$ in the transferred
 16943	$A_\infty$-structure), so all obstruction sources vanish
 16944	(Theorem~\ref{thm:nms-heisenberg-exact-linearity}).
 16945	
 16946	(ii)~For affine algebras, the cubic shadow is the Lie bracket
 16947	transported through the bar complex
 16948	(Theorem~\ref{thm:nms-affine-cubic-normal-form}). The quartic
 16949	obstruction $o_4 = \tfrac{1}{2}\{\mathfrak{C},\mathfrak{C}\}_H$
 16950	vanishes by the Jacobi identity: the cyclic double Lie bracket
 16951	$\kappa([x,[y,z]],w)$ summed over cyclic permutations is zero.
exec
/bin/zsh -lc "rg -n '(Chapter|Ch\\.)~\\\\ref\\{app:' chapters/theory appendices --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/introduction.tex:1954:(Chapter~\ref{app:nonlinear-modular-shadows}).
chapters/theory/introduction.tex:2226:Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
chapters/theory/introduction.tex:2379: (Ch.~\ref{app:nonlinear-modular-shadows}).
chapters/theory/chiral_hochschild_koszul.tex:5733:in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
exec
/bin/zsh -lc "nl -ba appendices/general_relations.tex | sed -n '88,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    88	 
    89	\emph{General $n$.} The cohomology ring $H^*(C_n(\mathbb{C}))$ is the quotient of the
    90	exterior algebra $\bigwedge^* \mathbb{C}^{\binom{n}{2}}$ (generated by classes $\eta_{ij}$ in degree~1)
    91	by the ideal generated by $\binom{n}{3}$ quadratic Arnold relations (one for each triple $i < j < k$).
    92	The Poincar\'{e} polynomial is $\prod_{i=0}^{n-1}(1 + it)$, so
    93	$\dim H^k(C_n(\mathbb{C})) = |s(n, n-k)|$ (unsigned Stirling numbers of the first kind)
    94	and the total Betti number is $n!$.
    95	
    96	
    97	\chapter{\texorpdfstring{Curved $A_\infty$ relations: complete formulas}{Curved A infty relations: complete formulas}}
    98	\label{app:curved-ainfty-formulas}
    99	
   100	For reference, we collect the complete curved $A_\infty$ relations. An $A_\infty$ algebra 
   101	$(\mathcal{A}, \{m_k\}_{k \geq 0}, \mu_0)$ satisfies:
   102	
   103	\emph{$n = 0$.} (Curvature is a cycle.)
   104	\[m_1(\mu_0) = 0\]
   105	
   106	\emph{$n = 1$.} (Failure of strict nilpotence.)
   107	\[m_1^2 = m_2(\mu_0 \otimes \text{id}) - m_2(\text{id} \otimes \mu_0)\]

thinking
**Investigating appendix formatting**

I'm finding it interesting that there’s a `\chapter` mid-file. Is it possible this is an appendix chapter? I should check if it's included in the main body or the references as Appendixref{app:curved-ainfty-formulas}. Since the label is chapter, this might not be an issue. It could be good to search for appendix labels cited as chapters, especially since `app:nonlinear-modular-shadows` is at the top, so I want to inspect that further.
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\chapter[Ambient complementarity and nonlinear modular shadows]{Ambient complementarity, nonlinear modular shadows, and the quartic resonance class}
     2	\label{app:nonlinear-modular-shadows}
     3	
     4	The modular characteristic $\kappa(\cA)$ (Theorem~D) and the spectral
     5	discriminant~$\Delta_{\cA}$ are the linear face of a single ambient
     6	deformation problem. The ambient problem carries a $(-1)$-shifted
     7	symplectic form, and the two dual packages $\mathcal{Q}_g(\cA)$
     8	and~$\mathcal{Q}_g(\cA^{!})$ are complementary Lagrangians inside it.
     9	Their interaction produces an infinite nonlinear tower
    10	\[
    11	\kappa \;\longrightarrow\; \Delta \;\longrightarrow\;
    12	\mathfrak{C} \;\longrightarrow\; \mathfrak{Q}
    13	\;\longrightarrow\; \Theta,
    14	\]
    15	the \emph{shadow obstruction tower}: the sequence of finite-order
    16	projections $\Theta_\cA^{\leq r}$ of the universal MC element
    17	$\Theta_\cA \in \MC(\gAmod)$
    18	(Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
    19	is MC because $D_\cA^2 = 0$; all-degree convergence
    20	$\Theta_\cA = \varprojlim_r \Theta_\cA^{\leq r}$ by

thinking
**Analyzing appendix notation**

I'm looking at whether it's correct to call it a chapter even if it's in the appendices. So, labeling it `\chapter` may not be totally wrong, but it could also be a stylistic choice that confuses readers if it's supposed to be an appendix.

I’m considering if the prefix `app:` clarifies its purpose. It seems like it might impact cross-referencing in TeX, particularly if chasing mathematical detail reveals whether the theorem references are correctly aligned with appendix content. I should double-check that!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1572,1596p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1572	\label{thm:chain-vs-homology}
  1573	Let $(\mathcal{A}, \{m_k\})$ be an $A_\infty$ chiral algebra.
  1574	\begin{enumerate}[label=\textup{(\roman*)}]
  1575	\item \emph{Chain level.}
  1576	 The full $A_\infty$ structure $\{m_k\}_{k \geq 1}$ is preserved,
  1577	 all operations are computable via configuration space integrals,
  1578	 and homotopies have geometric meaning as forms on
  1579	 $\overline{C}_n(X)$.
  1580	\item \emph{Homology level.}
  1581	 The homotopy transfer theorem
  1582	 (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
  1583	 $A_\infty$ structure $\{m_k^H\}$ on $H^*(\mathcal{A})$ with
  1584	 $m_1^H = 0$. The product $m_2^H$ descends to homology
  1585	 (it is strictly associative if $\mathcal{A}$ is formal).
  1586	 However, the transferred higher operations
  1587	 $m_k^H$ for $k \geq 3$ are in general \emph{non-trivial}:
  1588	 they are the Massey products, encoding obstructions to formality.
  1589	\item \emph{What is lost.}
  1590	 The explicit chain-level homotopies $\{h_n\}$ (the contracting
  1591	 data) are lost in the passage to homology. For a Koszul algebra,
exec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '451,490p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   451	\label{sec:htt-chiral}
   452	
   453	
   454	\begin{theorem}[Chiral homotopy transfer; \ClaimStatusProvedHere]
   455	\label{thm:chiral-htt}
   456	\index{$A_\infty$-structure!transferred}
   457	Let $\cA$ be an $\Eone$-chiral algebra on a curve $X$ and suppose we have an 
   458	SDR of the underlying D-module:
   459	\[
   460	(\cA, H, p, \iota, h) \quad \text{with } H = H^{\mathrm{ch}}_*(\cA).
   461	\]
   462	Then:
   463	\begin{enumerate}[label=(\roman*)]
   464	\item $H$ inherits an $\Ainf$-chiral algebra structure.
   465	\item The higher operations $\{m_n^{\mathrm{ch}}\}_{n \geq 3}$ are ``Massey products'' 
   466	for the chiral structure.
   467	\item If $\cA$ is Koszul, then $m_n^{\mathrm{ch}} = 0$ for $n \geq 3$.
   468	\end{enumerate}
   469	\end{theorem}
   470	



thinking
**Analyzing theorem integrity**

I'm looking at potential issues with the theorem `thm:htt`. I need to check if `thm:chiral-htt` has been properly cited, especially in relation to higher_genus_complementarity and nilpotent_completion. Lines 1177 in nilpotent_completion might reference weight compatibility, but I'm unsure if it's necessary. I notice there's a potential problem with `prop:e2-collapse-formality`, which uses `thm:chiral-htt` incorrectly to assert that certain operations vanish. This raises questions about the reliance on these theorems.
thinking
**Examining theorem equivalence**

I’m considering whether I need to stray from the seam, especially if the appendix theorem was employed to assert a too-strong equivalence. I should check if this theorem actually supports that equivalence. In the proof of `prop:e2-collapse-formality`, the transition from (i) to (ii) claims collapse produces a standard decomposition related to `thm:bar-cobar-htt`, but the argument might rely on specific conditions. The step from (ii) to (iii) seems problematic due to assumptions about transferred operations, which may not vanish in all cases. If the appendix theorem is misused, it could indeed affect the conclusion.
thinking
**Identifying theorem issues**

I realize the problem lies within the body of the theorem itself. I should mention this, but it’s essential to ground each claim based on the files I’ve read. While I can bring this up, I might want to focus on the direct mismatches with the appendices. A specific concern is that the `quantum_corrections` in line 360 uses appendix homotopy transfer for defining the propagator form on full FM compactification, which doesn’t seem to be supported.
exec
/bin/zsh -lc "rg -n 'thm:nms-archetype-trichotomy' chapters/theory --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:32054:(Theorem~\ref{thm:nms-archetype-trichotomy}):
chapters/theory/higher_genus_modular_koszul.tex:32294:(Theorem~\ref{thm:nms-archetype-trichotomy})
chapters/theory/higher_genus_complementarity.tex:5436:(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
chapters/theory/higher_genus_complementarity.tex:6092:(Theorem~\ref{thm:nms-archetype-trichotomy}).
chapters/theory/chiral_koszul_pairs.tex:3329:(Theorem~\ref{thm:nms-archetype-trichotomy})
chapters/theory/chiral_koszul_pairs.tex:3450:(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32288,32310p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 32288	$\operatorname{Ob}_2$; $d_3\colon E_1^{0,*} \to E_1^{3,*}$
 32289	encodes the deepest obstruction at genus~$3$.
 32290	
 32291	\smallskip\noindent
 32292	\emph{Shadow depth filtration.}
 32293	The archetype classification
 32294	(Theorem~\ref{thm:nms-archetype-trichotomy})
 32295	controls which of the $42$ graphs carry nonscalar vertex weights:
 32296	\[
 32297	\renewcommand{\arraystretch}{1.2}
 32298	\begin{array}{c|c|c|l}
 32299	\text{class}
 32300	& r_{\max}
 32301	& \text{vertex constraint}
 32302	& \text{active/scalar} \\\hline
 32303	G\;\text{(Gaussian)}
 32304	 & 2 & \text{all vertices binary}
 32305	 & 42/42\text{ scalar (}\kappa\text{-only)} \\
 32306	L\;\text{(Lie/tree)}
 32307	 & 3 & \operatorname{val}(v) \geq 3\text{ activates cubic}
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '32310,32324p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 32310	 & 4 & \operatorname{val}(v) \geq 4\text{ activates quartic}
 32311	 & \text{quartic at 4-valent vertices; cubic absent} \\
 32312	M\;\text{(mixed)}
 32313	 & \infty & \text{all degrees active}
 32314	 & \text{all 42 graphs carry higher-degree corrections}
 32315	\end{array}
 32316	\]
 32317	For class~$G$ (Heisenberg), every graph contributes
 32318	$\kappa^{|E|}/|\operatorname{Aut}|$ and the sum recovers
 32319	$F_3 = \kappa\cdot 31/967680$.
 32320	For class~$L$ (affine), graphs with a vertex of valence~${\geq}\,3$
 32321	acquire cubic shadow corrections from $\mathfrak{C}(\cA)$.
 32322	For class~$C$ ($\beta\gamma$), the quartic contact invariant
 32323	$\mathfrak{Q}^{\mathrm{contact}}$ contributes at graphs with a
 32324	vertex of valence~${\geq}\,4$; the cubic shadow vanishes.

thinking
**Searching for theorems and corrections**

I'm noticing the appendix theorem on finite termination is broader than I thought. It indicates that the Virasoro case is generically infinite but doesn't specify that all 42 graphs have corrections or mention W_N. I need to limit row M to "Virasoro witness" or refer to a separate theorem if it exists. 
Next, I should search for a W_N theorem, possibly around 1604 and 1638, as there might be appendix theorems for principal W_N that could support this mixed-class generalization.
exec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '1584,1645p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1584	\end{proof}
  1585	
  1586	\subsection{Principal \texorpdfstring{$\mathcal W_N$}{WN}}
  1587	\label{subsec:nms-principal-wn}
  1588	
  1589	\begin{definition}[Principal quartic shadow envelope]
  1590	\label{def:nms-principal-wn-envelope}
  1591	For principal $\mathcal W_N$ with strong generators
  1592	\[
  1593	W^{(2)}=T,\;W^{(3)},\dots,W^{(N)},
  1594	\]
  1595	let $E_{W_N}^{[4]}$ be the primary--composite quartic shadow envelope generated by the strong generators together with all quasi-primary bilinears
  1596	\[
  1597	\Pi_{\mathrm{qp}}\bigl(:W^{(r)}W^{(s)}:\bigr)
  1598	\qquad (2\le r\le s\le N)
  1599	\]
  1600	that occur in pairwise OPEs.
  1601	\end{definition}
  1602	
  1603	\begin{theorem}[Diagonal Hessian and universal cubic sector for principal \texorpdfstring{$\mathcal W_N$}{WN}; \ClaimStatusProvedHere]

thinking
**Fixing references**

I need to ensure I'm accurately citing the correct theorem to prove that M is infinite. The user wants a precise fix, so I'll replace the citations and relevant text as needed. It might be helpful to check the body references in the branch line reductions appendix for any miscitations. I should also look for context around the introduction to chiral Hochschild-Koszul from 1956, especially regarding its relation to the mixed cubic-quartic.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1948,1965p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '5728,5785p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/branch_line_reductions.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1948	The scalar characteristic $\kappa(\cA)$ is proved. The spectral
  1949	discriminant $\Delta_\cA$ is proved. The cubic and quartic shadow
  1950	classes $[\mathfrak C_\cA]$ and $[\mathfrak Q_\cA]$ are the first
  1951	genuinely nonlinear modular invariants, computable on any family
  1952	where the cyclic deformation package is available through the
  1953	relevant order
  1954	(Chapter~\ref{app:nonlinear-modular-shadows}).
  1955	The branch-line reductions
  1956	(Appendix~\ref{app:branch-line-reductions}) extract exact
  1957	finite-dimensional quotients of this layer, including genus-$2$
  1958	transparency and the universal genus-$3$ constant~$7$ on the shared
  1959	$\widehat{\mathfrak{sl}}_2$/Virasoro/$\beta\gamma$ spectral sheet.
  1960	For class~$\mathbf{M}$ algebras the infinite tower has a computable
  1961	exponential growth rate $\rho(\cA)$ governed by the shadow metric
  1962	$Q_L$ (Proposition~\ref{prop:shadow-tower-growth-rate}); for the
  1963	Virasoro family this gives
  1964	$\rho(\mathrm{Vir}_c) =
  1965	\sqrt{(180c{+}872)/((5c{+}22)\,c^2)}$
 succeeded in 51ms:
     1	\chapter[Branch-line reductions and primitive modular characteristics]{Branch-line reductions, primitive modular characteristics, and the intrinsic invariant ladder}
     2	\label{app:branch-line-reductions}
     3	
     4	The full modular Maurer--Cartan element $\Theta_\cA$ lives in an
     5	infinite-dimensional convolution algebra. A \emph{branch-line
     6	reduction} restricts~$\Theta_\cA$ to a configuration of minimal
     7	complexity (two-point branch lines, rank-one spectral sectors,
     8	genus-$2$ transparency windows) and proves structural theorems
     9	inside the resulting finite-dimensional quotient.
    10	
    11	The \emph{primitive modular characteristics} are the irreducible
    12	components of~$\Theta_\cA$ under the clutching maps of
    13	$\overline{\mathcal{M}}_{g,n}$: they are to the shadow obstruction
    14	tower what primitive elements are to a Hopf algebra. The intrinsic
    15	invariant ladder
    16	\[
    17	\kappa(\cA)
    18	\rightsquigarrow
    19	\Delta_{\cA}(x)
    20	\rightsquigarrow
 succeeded in 51ms:
  5728	\end{remark}
  5729	
  5730	\begin{remark}[Nonlinear shadow calculus]
  5731	\label{rem:nonlinear-shadow-pointer}
  5732	The first nonlinear jets of~$S_\cA$ are developed systematically
  5733	in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
  5734	shadow cocycle
  5735	$\Theta_\cA^{\le 4} = H_\cA + \mathfrak C_\cA + \mathfrak Q_\cA$
  5736	is constructed, its master and clutching equations are proved,
  5737	and the three frame families are shown to realize the Gaussian,
  5738	Lie/tree, and contact/quartic archetypes respectively.
  5739	The modular quartic resonance class~$\mathfrak R_{4,g,n}^{\mathrm{mod}}(\cA)$
  5740	constructed there is the first Picard-valued nonlinear characteristic of the theory.
  5741	\end{remark}
  5742	
  5743	\begin{remark}[Branch-line reductions]
  5744	\label{rem:branch-line-pointer}
  5745	Appendix~\ref{app:branch-line-reductions} extracts exact
  5746	finite-dimensional quotients of the full modular deformation problem: the
  5747	scalar Maurer--Cartan skeleton, the spectral cumulant hierarchy, and


thinking
**Identifying dependencies clearly**

I'm diving into the need to find circular dependencies, as the user specifically asked to check for them. I see that the `thm:bar-cobar-htt` depends on `thm:bar-cobar-isomorphism-main`, and the `prop:e2-collapse-formality` relies on it too. However, that's not a direct cycle. 

Next, I’m checking if the corollary cor:bar-d-squared-zero-arnold involves `thm:bar-nilpotency-complete`. It probably doesn’t lead to any cycle either. So it looks like there are no circular dependencies here.
thinking
**Identifying seam inconsistencies**

I'm noticing a seam inconsistency here: the body references "cf appendix homotopy transfer," but the algebraic formula it provides is different from what's in the appendix. I should specify a precise fix: replace line 361 with the given formula. I might also refer to Construction\ref{constr:transfer-ainf}. I need to verify later whether the body actually presents the correct formula and check near lines 380 to double-check everything.
exec
/bin/zsh -lc "nl -ba chapters/theory/quantum_corrections.tex | sed -n '380,395p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   380	The transferred operation $m_3$ is computed by homotopy transfer from
   381	the Fulton--MacPherson compactification $\overline{C}_3(\mathbb{C})$:
   382	\begin{equation}
   383	m_3(a, b, c)
   384	= \sum_{T \in \mathrm{PBT}_3}
   385	 (\pm)\, p \circ \mu_T \circ i^{\otimes 3}(a, b, c),
   386	\end{equation}
   387	where $\mathrm{PBT}_3$ is the set of planar binary trees with $3$
   388	leaves (two trees), each internal edge carrying the contracting
   389	homotopy~$h$, and $p, i$ are the projection and inclusion of the
   390	homotopy retract. This is a genus-$0$ (tree-level) operation;
   391	genus $g \geq 1$ corrections enter through the propagator and the
   392	cohomology of $\overline{\mathcal{M}}_g$, not through the degree of the
   393	$A_\infty$ operations.
   394	
   395	\subsubsection{For $\mathcal{W}$-algebras}

thinking
**Considering labeling terminology**

I’m thinking about the difference between calling it an appendix versus a chapter. It seems like there might be some confusion regarding the terminology, but fine! It’s important for me to get the terminology right, so I’ll keep that in mind moving forward. It’s interesting how wording can impact understanding, and I want to make sure I'm clear on what to call things. Let's keep exploring this!
exec
/bin/zsh -lc "rg -n '_sl2_yangian_insert|sl2_yangian_insert' main.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Verifying references in documents**

I find it interesting that `_sl2_yangian_insert.tex` isn't included in the main document. Yet, `chiral_modules.tex` references `thm:sl2-koszul-dual`, which is uniquely defined there. If the main document doesn’t include that appendix, it creates an undefined reference when building. I should check to verify if this label is defined elsewhere too. Time to search for that!
codex
I found a potentially live seam break, not just a wording issue: `chapters/theory/chiral_modules.tex` cites `thm:sl2-koszul-dual`, but that label seems to live only in `appendices/_sl2_yangian_insert.tex`, which `main.tex` does not include. I’m verifying that there isn’t a second live definition before I count it as a broken citation.
exec
/bin/zsh -lc "rg -n 'label\\{thm:sl2-koszul-dual\\}|thm:sl2-koszul-dual' -g '*.tex' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/_sl2_yangian_insert.tex | sed -n '500,545p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '2866,2972p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '_sl2_yangian_insert' -g '*.tex' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./appendices/_sl2_yangian_insert.tex:533:\label{thm:sl2-koszul-dual}
./chapters/examples/landscape_census.tex:1388:for $\mathfrak{sl}_2$ (Theorem~\ref{thm:sl2-koszul-dual}),
./chapters/examples/landscape_census.tex:3994: (Theorem~\ref{thm:sl2-koszul-dual}),
./chapters/examples/bar_complex_tables.tex:1715:(Theorem~\ref{thm:sl2-koszul-dual}).
./chapters/examples/bar_complex_tables.tex:4415:(Theorem~\ref{thm:sl2-koszul-dual}):
./chapters/examples/kac_moody.tex:610:\begin{theorem}[Koszul dual of \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k}; \ClaimStatusProvedHere]\label{thm:sl2-koszul-dual}
./chapters/examples/kac_moody.tex:1176:The factor $h^\vee$ arises from the adjoint representation: by Lemma~\ref{lem:killing-structure-constants}, $\sum_{c,d} f^{ac}{}_d f^{bc}{}_d = 2h^\vee \cdot \delta^{ab}$, which gives $\sum_{c,d,e} f^{ac}{}_d f^{bc}{}_e (J^d, J^e) = 2h^\vee \cdot (J^a, J^b)$. (For $\mathfrak{sl}_2$ with $h^\vee = 2$, this was verified explicitly in Theorem~\ref{thm:sl2-koszul-dual}: $m_1^2(e \boxtimes f \cdot \eta_{12}) = (k+2) \cdot \partial h$.)
./chapters/examples/kac_moody.tex:1205:which is precisely the OPE of $\widehat{\mathfrak{g}}_{-k-2h^\vee}$. (For $\mathfrak{sl}_2$: $-k-2 \cdot 2 = -k-4$, matching Theorem~\ref{thm:sl2-koszul-dual}.)
./chapters/examples/kac_moody.tex:1218:\item \emph{Explicit verification}: For $\mathfrak{sl}_2$ (Theorem~\ref{thm:sl2-koszul-dual}) and $\mathfrak{sl}_3$ (\S\ref{sec:sl3-computation}), the low-degree bar complex computations confirm the predicted dual level. \checkmark
./chapters/examples/kac_moody.tex:1295:Theorem~\ref{thm:sl2-koszul-dual}.
./chapters/examples/kac_moody.tex:2135:(cf.\ Theorem~\ref{thm:sl2-koszul-dual}) is
./chapters/examples/kac_moody.tex:2210:(Theorem~\ref{thm:sl2-koszul-dual}), the dualised collision
./chapters/examples/kac_moody.tex:3663:The genus-0 level-shifting duality $(\widehat{\mathfrak{sl}}_{2,k})^! \simeq \widehat{\mathfrak{sl}}_{2,-k-4}$ (Theorem~\ref{thm:sl2-koszul-dual}) is the starting point. We carry out the genus-1 pipeline for $\widehat{\mathfrak{sl}}_2$ at generic level $k \neq -2$: the first non-abelian example of all three main theorems at genus~1.
./chapters/examples/kac_moody.tex:3865:The Koszul dual $(\widehat{\mathfrak{sl}}_{2,k})^! = \widehat{\mathfrak{sl}}_{2,-k-4}$ (Theorem~\ref{thm:sl2-koszul-dual}) has shifted level $k^* = -k-4$. Repeating the curvature computation with $k$ replaced by $k^*$:
./chapters/examples/free_fields.tex:2630:\textup{(}Theorem~\textup{\ref{thm:sl2-koszul-dual}} for
./chapters/examples/free_fields.tex:2663:\emph{Proved}: the free-field and Heisenberg dualities (Chapter~\ref{sec:betagamma-koszul-dual}, Theorem~\ref{thm:heisenberg-koszul-dual-early}); the Kac--Moody level shift $\widehat{\mathfrak{g}}_k \leftrightarrow \widehat{\mathfrak{g}}_{-k-2h^\vee}$ (Theorems~\ref{thm:sl2-koszul-dual} and~\ref{thm:universal-kac-moody-koszul}).
./chapters/theory/chiral_modules.tex:2874:(Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
./chapters/theory/chiral_modules.tex:2946:(Theorem~\ref{thm:sl2-koszul-dual}), the module Koszul duality
./chapters/theory/chiral_modules.tex:2967:Theorem~\ref{thm:sl2-koszul-dual},
 succeeded in 51ms:
   500	\begin{proposition}[Tensor products and Yang--Baxter;
   501	\ClaimStatusProvedHere]
   502	\label{prop:eval-tensor-sl2}
   503	The tensor product of evaluation modules $V_a\otimes V_b$ ($a\neq b$) is
   504	irreducible as a $Y_\hbar(\mathfrak{sl}_2)$-module. The
   505	$R$-matrix intertwining $V_a\otimes V_b\cong V_b\otimes V_a$ is
   506	\begin{equation}\label{eq:eval-r-sl2}
   507	\check R_{ab}\;=\;(a-b)\,I+\hbar\,P\;=\;R(a-b)
   508	\;\in\;\operatorname{End}(V_a\otimes V_b),
   509	\end{equation}
   510	recovering the Yang $R$-matrix of Theorem~\ref{thm:yang-r-matrix}. At
   511	$a=b$, the tensor product is reducible:
   512	$V_a\otimes V_a\cong \operatorname{Sym}^2 V\oplus\bigwedge^2 V$ decomposes
   513	as a direct sum of the $3$-dimensional irreducible and the trivial
   514	representation. The $R$-matrix $R(0)=\hbar P$ is the
   515	permutation, consistent with $R(0)$ having eigenvalue
   516	$+\hbar$ on $\operatorname{Sym}^2$ and $-\hbar$ on $\bigwedge^2$.
   517	\end{proposition}
   518	
   519	\begin{proof}
 succeeded in 51ms:
  2866	\label{comp:bgg-sl2-pipeline}
  2867	\index{BGG resolution!explicit pipeline}
  2868	\index{bar complex!BGG pipeline}
  2869	We trace the bar complex of $\widehat{\mathfrak{sl}}_{2,k}$ through
  2870	the BGG spectral sequence (Theorem~\ref{thm:bgg-from-bar}) step by
  2871	step, connecting the explicit bar differential matrix
  2872	(Computation~\ref{comp:sl2-bar-matrix}) to the classical BGG
  2873	resolution, and verifying compatibility with Koszul duality
  2874	(Theorem~\ref{thm:sl2-koszul-dual}) and screening operators
  2875	(Theorem~\ref{thm:screening-bar}). \emph{Step~1: Weight decomposition of the bar complex.}
  2876	The bar differential $d\colon \bar{B}^2 \to \bar{B}^1$
  2877	(eq.~\eqref{eq:sl2-bar-matrix}) decomposes under the adjoint
  2878	$\mathfrak{h}$-action into weight sectors:
  2879	\begin{center}
  2880	\renewcommand{\arraystretch}{1.2}
  2881	\begin{tabular}{cccc}
  2882	\textbf{Weight} & $\dim \bar{B}^2$ & $\dim \bar{B}^1$
  2883	 & $\operatorname{rank} d$ \\
  2884	\hline
  2885	$+4$ & $1$ & $0$ & $0$ \\
 exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1138,1165p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/general_relations.tex | sed -n '97,122p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1138	\[m_2(m_2 \otimes \text{id}) - m_2(\text{id} \otimes m_2) = d(h_3)\]
  1139	where $h_3$ is the homotopy between associations
  1140	\end{itemize}
  1141	\end{example}
  1142	
  1143	\subsubsection{\texorpdfstring{Complete $A_\infty$ structure from configuration spaces}{Complete A-infinity structure from configuration spaces}}
  1144	
  1145	\begin{definition}[\texorpdfstring{$A_\infty$}{A-infinity} algebra]\label{def:a-infinity-complete}
  1146	An $A_\infty$ algebra consists of a graded vector space $A$ with operations $m_k: A^{\otimes k} \to A[2-k]$ for $k \geq 1$ satisfying (cf.\ Appendix~\ref{app:curved-ainfty-formulas}):
  1147	\[\sum_{\substack{r+s+t=n \\ r,t \geq 0,\; s \geq 1}} (-1)^{rs+t}\, m_{r+1+t}(\mathrm{id}^{\otimes r} \otimes m_s \otimes \mathrm{id}^{\otimes t}) = 0\]
  1148	
  1149	Explicitly for small $k$:
  1150	\begin{align}
  1151	k=1: &\quad m_1 \circ m_1 = 0 \quad \text{($m_1$ is a differential)} \\
  1152	k=2: &\quad m_1(m_2) = m_2(m_1 \otimes 1) + m_2(1 \otimes m_1) \quad \text{(Leibniz rule)} \\
  1153	k=3: &\quad m_2(m_2 \otimes 1) - m_2(1 \otimes m_2) = m_1(m_3) + m_3(m_1 \otimes 1 \otimes 1) + \cdots
  1154	\end{align}
  1155	\end{definition}
  1156	
  1157	\begin{theorem}[\texorpdfstring{$A_\infty$}{A-infinity} structure from bar complex; \ClaimStatusProvedHere]\label{thm:bar-ainfty-complete}
 succeeded in 52ms:
    97	\chapter{\texorpdfstring{Curved $A_\infty$ relations: complete formulas}{Curved A infty relations: complete formulas}}
    98	\label{app:curved-ainfty-formulas}
    99	
   100	For reference, we collect the complete curved $A_\infty$ relations. An $A_\infty$ algebra 
   101	$(\mathcal{A}, \{m_k\}_{k \geq 0}, \mu_0)$ satisfies:
   102	
   103	\emph{$n = 0$.} (Curvature is a cycle.)
   104	\[m_1(\mu_0) = 0\]
   105	
   106	\emph{$n = 1$.} (Failure of strict nilpotence.)
   107	\[m_1^2 = m_2(\mu_0 \otimes \text{id}) - m_2(\text{id} \otimes \mu_0)\]
   108	
   109	\emph{$n = 2$.} (Associativity with curvature corrections.)
   110	\begin{multline}
   111	m_1 m_2 - m_2(m_1 \otimes \text{id}) - m_2(\text{id} \otimes m_1) + m_3(\mu_0 \otimes \text{id} 
   112	\otimes \text{id}) \\
   113	- m_3(\text{id} \otimes \mu_0 \otimes \text{id}) + m_3(\text{id} \otimes \text{id} \otimes \mu_0) = 0
   114	\end{multline}
   115	
   116	\emph{$n = 3$.} (Higher coherences.)


thinking
**Analyzing citation issues**

I'm noticing a notation mismatch regarding the uncurved A∞ algebra. The body defines it for k≥1, while it cites curved relations and uses m_0/μ_0 inconsistently in the appendix. It's possible the citation could just refer to a curved extension, but I should be careful. I think the severity isn't too high, but it’s worth mentioning. I'll suggest clarifying the citation to refer specifically to the extended appendix. This helps align the definition scope properly.
thinking
**Fixing citation issues**

I realize the appendix only covers curved formulas, so I need to update line 1146 to clarify that it refers to an uncurved A∞ algebra, while directing readers to the curved variant in the appendix. That sounds good! I’ll also check if the `higher_genus_foundations` theorem proof uses the appendix’s Lemma, which seems fine. However, there's a potential mixing of notation in line 101 of the appendix. I wonder if that's worth mentioning. Overall, I need to watch for any circular dependencies in the `nonlinear_modular_shadows` appendix, but it looks like it’s all good!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12728,12742p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 12728	\label{rem:shadow-algebra-structural-home}
 12729	\index{shadow algebra!structural role}
 12730	The shadow algebra governs the nonlinear modular characteristic.
 12731	The recursive obstruction construction
 12732	(Construction~\ref{constr:obstruction-recursion})
 12733	is the \emph{computational method} for extracting shadows; the
 12734	shadow algebra is the \emph{structural home}. Finite termination means
 12735	$\cA^{\mathrm{sh}}_{r,0} = 0$ for $r > r_{\max}(\cA)$.
 12736	Theorem~\ref{thm:nms-finite-termination} gives
 12737	explicit bounds: $r_{\max} = 2$
 12738	(Heisenberg), $3$ (affine), $4$
 12739	($\beta\gamma$); the Virasoro tower is infinite.
 12740	The shadow algebra depends only on the homotopy type of $\Defcyc^{\mathrm{mod}}(\cA)$, not on presentations, bases, or contracting homotopies.
 12741	\end{remark}
 12742	
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1160,1180p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/nonlinear_modular_shadows.tex | sed -n '2060,2140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12696,12715p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1160	hence $A_\infty$-depth $d_\infty(\cA) = 2$ and
  1161	$L_\infty$-formality level $f_\infty(\cA) = 2$.
  1162	The genus-$0$ transferred $L_\infty$ brackets therefore
  1163	satisfy $\ell_k^{(0),\mathrm{tr}} = 0$ for $k \geq 3$:
  1164	the genus-$0$ convolution algebra is formal.
  1165	
  1166	For the full scalar orbit, the shadow
  1167	obstruction tower terminates at degree~$2$:
  1168	$\Theta_{\cA}^{(\le r)} = \kappa \cdot \eta \otimes \Lambda$
  1169	for all~$r$. The obstruction classes
  1170	$o^{(r+1)}(\cA) \in H^2(F^{r+1}\gAmod / F^{r+2}\gAmod, d_2)$
  1171	vanish for all $r \geq 2$
  1172	(Theorem~\ref{thm:nms-all-degree-master-equation}).
  1173	Since the genus-$g$ quantum brackets $\ell_k^{(g)}$ for
  1174	$g \geq 1$ are induced by sewing on $\overline{\cM}_{g,n}$,
  1175	and sewing applied to the scalar element
  1176	$\kappa \cdot \eta \otimes \Lambda$ produces the scalar
  1177	genus-$g$ curvature $\kappa^g \cdot \eta_g \otimes \Lambda_g$
  1178	(which lies in the image of the differential, not in
  1179	independent cohomology), the transferred higher-genus brackets
 succeeded in 52ms:
  2060	
  2061	The quartic shadow calculus of \S\ref{sec:nms-shadow-calculus} stops at degree~$4$. But the master equation is a truncation of a universal recursive structure governing all degrees. We now prove the general degree-$r$ equations and draw structural consequences.
  2062	
  2063	\subsection{The all-degree master equation}
  2064	\label{subsec:nms-all-degree-master-equation}
  2065	
  2066	\begin{definition}[Degree-$r$ shadow jet]
  2067	\label{def:nms-degree-r-shadow-jet}
  2068	For $r\ge 2$, define the \emph{degree-$r$ shadow jet} on the cyclic slice $V_{\cA}$ by
  2069	\begin{equation}
  2070	\label{eq:nms-degree-r-shadow-jet}
  2071	\mathrm{Sh}_r(\cA)(x_1,\dots,x_r)
  2072	:=
  2073	\sum_{\mathrm{cyc}}\langle x_1,\ell_{r-1}^{\mathrm{tr}}(x_2,\dots,x_r)\rangle.
  2074	\end{equation}
  2075	Write $S_{\cA}^{\le r}:=\sum_{k=2}^r \frac{1}{k!}\mathrm{Sh}_k(\cA)$ for the truncated complementarity potential through degree~$r$.
  2076	\end{definition}
  2077	
  2078	\begin{definition}[Degree-$r$ obstruction]
  2079	\label{def:nms-degree-r-obstruction}
 succeeded in 52ms:
 12696	preserves quasi-isomorphisms, so
 12697	$f_*$ is a quasi-isomorphism of convolution algebras.
 12698	The descended map on cohomology is therefore an
 12699	isomorphism.
 12700	\end{proof}
 12701	
 12702	\begin{proposition}[All-degree master equation from MC]
 12703	\label{prop:master-equation-from-mc}
 12704	\ClaimStatusProvedHere
 12705	\index{all-degree master equation!from Maurer--Cartan}
 12706	The all-degree master equation
 12707	$\nabla_H(\operatorname{Sh}_r) + \mathfrak{o}^{(r)} = 0$
 12708	(Theorem~\ref{thm:nms-all-degree-master-equation}) is a structural
 12709	consequence of the Maurer--Cartan equation for
 12710	$\Theta_{\cA} \in \MC(\Defcyc^{\mathrm{mod}}(\cA))$: projecting
 12711	the MC equation $d\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ onto
 12712	the degree-$r$ component gives exactly
 12713	$\nabla_H(\operatorname{Sh}_r) + \mathfrak{o}^{(r)} = 0$.
 12714	\end{proposition}
 12715	
exec
/bin/zsh -lc "nl -ba chapters/theory/nilpotent_completion.tex | sed -n '1168,1184p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1168	chiral algebra (positive-energy grading on the VOA state space),
  1169	not the \emph{mode algebra} formulation (generators $L_n$ for
  1170	all~$n \in \mathbb{Z}$). In the mode algebra, the coproduct
  1171	of~$L_0$ involves infinitely many terms
  1172	$L_k \otimes L_{-k}$, and the raw mode bar construction has
  1173	infinite-dimensional weight-$0$ part. The positive-energy
  1174	state-space formulation avoids this: each weight space is
  1175	finite-dimensional by axiom, and the SDR is constructed weight by
  1176	weight. The passage from modes to states is the HTT
  1177	(Theorem~\ref{thm:chiral-htt}), and the weight compatibility
  1178	(Step~2 above) ensures that the resonance piece remains
  1179	finite-dimensional after transfer.
  1180	\end{remark}
  1181	
  1182	\begin{construction}[Completion towers as MC4 inverse limits]
  1183	\label{constr:completion-mc4}
  1184	The strong completion-tower theorem

thinking
**Evaluating theorem citation errors**

I'm noticing something seems off with the HTT theorem and its connection from mode algebra to state-space formulation. It appears that modes and states aren't interchangeable unless a specific SDR is built. The appendix theorem doesn't mention modes, which leads me to think there's a citation issue. A possible fix is to clarify that the transition from modes to states isn’t covered by Theorem\ref{thm:chiral-htt}. I should look for additional misuse examples in references.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1868,1888p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1868	\]
  1869	for the counit. After passing to the PBW-associated graded quadratic
  1870	model, one is working in the formal neighborhood governed by the
  1871	quadratic closure
  1872	\[
  1873	\cA^i = H^*(\barB(\cA)),
  1874	\]
  1875	and the homotopy transfer theorem
  1876	\textup{(}Theorem~\textup{\ref{thm:htt}}\textup{)} supplies maps
  1877	\[
  1878	\cA \;\underset{\psi}{\overset{i}{\rightleftarrows}}\;
  1879	\Omega(\barB(\cA))
  1880	\]
  1881	with $\psi i = \id$ and $i\psi \sim \id$ on the tangent complex of the
  1882	bar-cobar deformation problem. In Keller's deformation-theoretic
  1883	language, this identifies the formal moduli problem of
  1884	$\Omega(\barB(\cA))$ with the one controlled by the transferred
  1885	$A_\infty$-structure on~$\cA^i$; on the Koszul locus, PBW
  1886	concentration says that this tangent complex is already governed by the
  1887	quadratic closure.
exec
/bin/zsh -lc "nl -ba chapters/theory/quantum_corrections.tex | sed -n '518,532p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   518	evaluated on specific graph types: $d_{A_\infty}$ encodes tree graphs
   519	(genus~$0$), $d_{\mathrm{sew}}$ encodes self-gluing (separating nodes),
   520	$\hbar\Delta$ encodes non-separating clutching (genus-raising loops),
   521	and $d_r$ encodes spectral twisting (line-operator insertions).
   522	
   523	The bar-cobar adjunction (Theorem~A) preserves quasi-isomorphisms
   524	\emph{because} it is a quantum $L_\infty$ functor: it intertwines the
   525	full $L_\infty$ structures on both sides, so homotopy transfer (Appendix~\ref{app:homotopy-transfer})
   526	produces the correct $A_\infty$ operations: the transferred
   527	operations are the $L_\infty$-functorial image of the original ones,
   528	not an ad hoc perturbative approximation.
   529	\end{remark}
   530	
   531	\subsection{Tree-level operations: explicit \texorpdfstring{$A_\infty$}{A-infinity} and \texorpdfstring{$L_\infty$}{L-infinity} brackets}
   532	
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '948,960p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba appendices/signs_and_shifts.tex | sed -n '568,612p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/configuration_spaces.tex | sed -n '2884,2895p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   948	For $\{d_2, d_3\} = 0$: this follows from the residue exact sequence for logarithmic forms. On a normal crossing divisor $D = \bigcup D_{ij} \subset \overline{C}_{n+1}(X)$, the residue map fits into the exact sequence $0 \to \Omega^k \to \Omega^k(\log D) \xrightarrow{\text{Res}} \bigoplus_{D_{ij}} \Omega^{k-1}_{D_{ij}}(\log D') \to 0$, and the de Rham differential is compatible with the residue map: $\text{Res}_{D_{ij}} \circ d_{\text{dR}} = d_{\text{dR}}|_{D_{ij}} \circ \text{Res}_{D_{ij}}$. Since $d_2$ is a signed sum of residues and $d_3 = d_{\text{dR}}$, they anticommute (with signs from Convention~\ref{conv:orientations-enhanced}).
   949	\end{proof}
   950	
   951	\begin{remark}[Sign-level verification]\label{rem:sign-bridge}
   952	For a complete sign-by-sign verification of $d^2 = 0$ at low degrees
   953	(including the explicit computation for degree-3 elements $[a|b|c]$ in a
   954	graded associative algebra), see Verification~\ref{ver:d2-degree3} and
   955	Proposition~\ref{prop:master-sign} in Appendix~\ref{app:signs}.
   956	\end{remark}
   957	
   958	\begin{remark}[Synthesis]\label{rem:d-squared-synthesis}\label{rem:geometric-miracle}
   959	The three mechanisms entering the proof of $d^2 = 0$,
   960	the Borcherds identity (algebra), Stokes' theorem (topology), and
exec
/bin/zsh -lc "nl -ba appendices/signs_and_shifts.tex | sed -n '1378,1392p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   568	d_\Omega(s^{-1}c_1 \otimes s^{-1}c_2) &= -s^{-1}(dc_1) \otimes s^{-1}c_2 \\
   569	&\quad - \sum (-1)^{|c_1'|} s^{-1}c_1' \otimes s^{-1}c_1'' \otimes s^{-1}c_2 \\
   570	&\quad + (-1)^{|c_1|} s^{-1}c_1 \otimes s^{-1}(dc_2) \\
   571	&\quad + (-1)^{|c_1|} \sum (-1)^{|c_2'|} s^{-1}c_1 \otimes s^{-1}c_2' \otimes s^{-1}c_2''
   572	\end{align*}
   573	\end{computation}
   574	
   575	\begin{proposition}[Master sign formula {\cite{LV12}}; \ClaimStatusProvedElsewhere]
   576	\label{prop:master-sign}
   577	For the bar complex of an $\Ainf$-algebra $(A, \{m_n\})$, the full differential 
   578	on $[a_1|\cdots|a_n]$ is:
   579	\[
   580	d_{\mathrm{bar}}[a_1|\cdots|a_n] = \sum_{i=1}^{n} \sum_{k=1}^{n-i+1} 
   581	(-1)^{\epsilon_{i,k}} [a_1|\cdots|a_{i-1}|m_k(a_i, \ldots, a_{i+k-1})|a_{i+k}|\cdots|a_n]
   582	\]
   583	where the sign is:
   584	\[
   585	\epsilon_{i,k} = \sum_{j=1}^{i-1} (|a_j| - 1) + \sum_{j=i}^{i+k-2} |a_j|
   586	\]
   587	where the first sum is the \emph{coderivation sign} (from commuting past
 succeeded in 52ms:
  2884	\item $\{S, S\} = 2(d\,\Theta + \tfrac{1}{2}[\Theta, \Theta])$:
  2885	 the BV antibracket combines the chain differential and the
  2886	 convolution bracket.
  2887	\item $\hbar\,\Delta(S) = \hbar\,\Delta_{\mathrm{clutch}}(\Theta)$:
  2888	 the BV operator is the non-separating clutching.
  2889	\end{itemize}
  2890	The factor of $\frac{1}{2}$ in~\eqref{eq:modular-mc-clutching}
  2891	is the QME factor (cf.\ Appendix~\ref{app:signs}, equation~\eqref{eq:qme-cg}: the QME
  2892	has $\hbar\Delta S + \frac{1}{2}\{S, S\} = 0$,
  2893	not $\hbar\Delta S + \{S, S\} = 0$).
  2894	\end{remark}
  2895	
 succeeded in 52ms:
  1378	\subsection{Costello--Gwilliam $\leftrightarrow$ this manuscript: BV and genus}
  1379	\label{sec:cg-us-formulas}
  1380	
  1381	\subsubsection{Quantum master equation}
  1382	
  1383	CG's BV formalism (on a manifold $M$ of dimension $d$) uses the quantum
  1384	master equation (QME):
  1385	\begin{equation}\label{eq:qme-cg}
  1386	\hbar \Delta_{\BV} S + \tfrac{1}{2}\{S, S\}_{\BV} = 0
  1387	\end{equation}
  1388	where $\Delta_{\BV}$ is the BV Laplacian, $\{-,-\}_{\BV}$ is the BV antibracket,
  1389	and $S$ is the action functional.
  1390	
  1391	\emph{Our convention} (specialized to curves, $d=1$): the QME becomes the
  1392	Maurer--Cartan equation in the modular convolution algebra





thinking
**Checking appendix and theorem references**

I'm looking into the appendix and searching for a potential issue in the `general_relations` at line 127. It refers to `m1^2=0`, which is linked to the nine-term proof in a specific section. I need to verify if the label `sec:bar-nilpotency` is in the right place, likely in `bar_construction`. There's also a concern with `higher_genus_foundations` at line 1582 regarding the theorem in the appendix. Since the user asked for exact fixes, I can suggest both changes and reference them accordingly.
thinking
**Identifying potential issues in theorems**

I need to look closely at the appendix theorem `thm:bar-cobar-htt`. Step 1 mentions the Hodge decomposition of \(\Omega(B_{\text{bar}}(A))\) relative to the bar filtration, but I'm not sure if such a decomposition exists or if it has been proven. The body might use this concept, but I want to avoid guessing. Additionally, I see a possible inconsistency in the `homotopy_transfer` theorem regarding higher operations and the `higher_genus_foundations` theorem, although they seem to align. I should inspect it more closely.
thinking
**Proposing exact fixes for citations**

I think the exact fix here involves changing the citation wording or possibly adding a note like "for curved extension see Appendix...". If the goal is to define curved \(A_{\infty}\), then including \(m_0\) is crucial. Additionally, there’s a potential issue with the `quantum_corrections` at line 360, where the formula uses \(\eta_{123}^{FM}\) without a definition. It's important to address these concerns objectively.
thinking
**Considering style consistency**

I’m thinking that saying "Chapter" in prose might not be the best choice. It could represent a low-severity style inconsistency that I need to address. It’s interesting how even small details can impact the overall flow and clarity of writing! I want to ensure everything aligns well and contributes positively to the text. Maybe I should look for alternatives that fit better within the style I'm aiming for.
thinking
**Verifying report details**

I need to check if I can report low if more findings are necessary. I should verify the main entries in the appendix before examining these files. I'm thinking that I might find what I need around line 1080. So, I'll search for details around the main entries to confirm that everything aligns correctly before moving forward. Getting this right is important!
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '1078,1100p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1078	scalar is extracted from the collision residue $r(z)$ by a
  1079	$\Sigma_2$-coinvariant integral on the Fulton--MacPherson
  1080	compactification $\overline{C}_2(X)$, so the shadow tower is rooted
  1081	in curve geometry from the start.
  1082	Part~\ref{part:characteristic-datum} develops the full nonlinear
  1083	structure: the shadow obstruction tower
  1084	$\kappa \to \Delta \to \mathfrak{C} \to \mathfrak{Q} \to \cdots$,
  1085	each level a constructive finite-order invariant with obstruction
  1086	classes in the cyclic deformation complex; the branch-line reductions
  1087	that extract structural theorems from finite-dimensional quotients;
  1088	and the computational methods that verify every formula by at least
  1089	three independent paths. The all-degree limit is the universal
  1090	Maurer--Cartan element~$\Theta_\cA$, proved by the bar-intrinsic
  1091	construction (Theorem~\ref{thm:mc2-bar-intrinsic}).
  1092	
  1093	\input{appendices/nonlinear_modular_shadows}
  1094	
  1095	% Branch-line reductions: genus-2 transparency, universal genus-3 constant,
  1096	% spectral cumulant hierarchy. The computational heart of Ring 2.
  1097	\input{appendices/branch_line_reductions}
exec
/bin/zsh -lc "rg -n '\\\\appendix' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1526:\appendix
codex
The build order changes the seam materially: `appendices/homotopy_transfer.tex`, `appendices/nonlinear_modular_shadows.tex`, and `appendices/branch_line_reductions.tex` are included before `\\appendix`, so they compile as ordinary chapters, not appendices. I’m now checking the prose cross-references for places where the manuscript treats those files inconsistently as appendices in some chapters and chapters in others.
exec
/bin/zsh -lc "nl -ba main.tex | sed -n '992,1006p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '(Chapter|Ch\\.)~\\\\ref\\{app:(homotopy-transfer|nonlinear-modular-shadows|branch-line-reductions)\\}' chapters/theory appendices chapters/connections --glob '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '(Appendix|App\\.)~\\\\ref\\{app:(homotopy-transfer|nonlinear-modular-shadows|branch-line-reductions)\\}' chapters/theory appendices chapters/connections --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   992	% Chapter 7: Bar-Cobar Adjunction and Curved Koszul Duality
   993	% Curved structures, I-adic completion, coalgebra homological algebra,
   994	% bar-cobar inversion (Theorem A), Ran-space perspective, categorical logarithm.
   995	% --------------------------------------------------
   996	\include{chapters/theory/bar_cobar_adjunction}
   997	
   998	% Homotopy Transfer Theorem: the mechanical heart of A∞ structure production.
   999	% Promoted from Appendix to Part I: this is foundational, not supplementary.
  1000	\input{appendices/homotopy_transfer}
  1001	
  1002	% Bar-Cobar Inversion: the quasi-isomorphism theorem, spectral sequence
  1003	% construction, E_2 collapse, functoriality, derived equivalence.
  1004	% Phase 0 canonicalization: merged into bar_cobar_construction; preserved at
  1005	% archive/legacy/bar_cobar_quasi_isomorphism_legacy.tex.
  1006	% \input{chapters/theory/bar_cobar_quasi_isomorphism}
 succeeded in 51ms:
chapters/connections/thqg_introduction_supplement_body.tex:1653:Chapter~\ref{app:nonlinear-modular-shadows}) extends the scalar
chapters/theory/introduction.tex:1954:(Chapter~\ref{app:nonlinear-modular-shadows}).
chapters/theory/introduction.tex:2226:Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
chapters/theory/introduction.tex:2379: (Ch.~\ref{app:nonlinear-modular-shadows}).
chapters/theory/chiral_hochschild_koszul.tex:5733:in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
chapters/connections/concordance.tex:2047: (Chapter~\ref{app:nonlinear-modular-shadows}) makes the
 succeeded in 51ms:
chapters/connections/thqg_open_closed_realization.tex:1460:appendix (Appendix~\ref{app:nonlinear-modular-shadows}):
chapters/connections/thqg_open_closed_realization.tex:1522:Appendix~\ref{app:nonlinear-modular-shadows}),
chapters/connections/thqg_symplectic_polarization.tex:51:Appendix~\ref{app:nonlinear-modular-shadows}, and that at genus~$1$
chapters/connections/thqg_symplectic_polarization.tex:1330:Appendix~\ref{app:nonlinear-modular-shadows}.
chapters/theory/higher_genus_modular_koszul.tex:4843:(Appendix~\ref{app:nonlinear-modular-shadows});
chapters/theory/higher_genus_modular_koszul.tex:10133:Appendix~\ref{app:nonlinear-modular-shadows} at each finite
chapters/theory/higher_genus_modular_koszul.tex:12271: (Appendix~\ref{app:nonlinear-modular-shadows}).
chapters/theory/higher_genus_modular_koszul.tex:12310: Appendix~\ref{app:nonlinear-modular-shadows}.
chapters/theory/higher_genus_modular_koszul.tex:13201:and Appendix~\ref{app:nonlinear-modular-shadows}
chapters/theory/higher_genus_modular_koszul.tex:15442:Appendix~\ref{app:nonlinear-modular-shadows}:
chapters/theory/higher_genus_modular_koszul.tex:15456:Appendix~\ref{app:nonlinear-modular-shadows} enumerates
chapters/theory/higher_genus_modular_koszul.tex:29654:(Appendix~\ref{app:nonlinear-modular-shadows}) is
chapters/theory/higher_genus_modular_koszul.tex:30996:and Appendix~\ref{app:nonlinear-modular-shadows}) is the
chapters/theory/quantum_corrections.tex:360:where $\eta_{123}^{\text{FM}}$ is the propagator form on the Fulton--MacPherson compactification $\overline{C}_3(X)$, defined via homotopy transfer (cf.\ Appendix~\ref{app:homotopy-transfer}). Concretely, $m_3$ sums over binary trees with 3 leaves, each tree contributing an iterated composition of $m_2$ with the contracting homotopy $h$:
chapters/theory/quantum_corrections.tex:525:full $L_\infty$ structures on both sides, so homotopy transfer (Appendix~\ref{app:homotopy-transfer})
chapters/connections/thqg_fredholm_partition_functions.tex:1475:in Appendix~\ref{app:nonlinear-modular-shadows})
chapters/connections/feynman_diagrams.tex:798:(Appendix~\ref{app:homotopy-transfer}) gives:
chapters/connections/feynman_diagrams.tex:875:(Appendix~\ref{app:homotopy-transfer},
chapters/connections/concordance.tex:2064: (Appendix~\ref{app:branch-line-reductions}) extracts exact
chapters/connections/concordance.tex:3217: & App.~\ref{app:nonlinear-modular-shadows} \\

thinking
**Fixing references consistently**

I need to replace every instance of `Appendix\ref{app:nonlinear-modular-shadows}` in the file with either `Chapter\ref{app:nonlinear-modular-shadows}` or `Ch.\ref{app:nonlinear-modular-shadows}` for consistency. I noted the specific lines where this needs to happen. I'll address homotopy transfer appendix references in each file too. Mentioning the main comments could be useful as evidence. In the PROBLEM section, I can clarify that "main.tex inputs this file before \appendix." Additionally, I might look into the `chapters/connections` references, but the focus here is the audit between appendices and chapters.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '2894,2935p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4838,4848p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_modules.tex | sed -n '2652,2662p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2894	\label{const:modular-homotopy-deformation-object}
  2895	\index{modular deformation!homotopy object|textbf}
  2896	Filter $\operatorname{Def}^{\mathrm{mod}}(\cA)$ by genus and
  2897	bar length. Choose any complete filtered contraction of this
  2898	quantum $L_\infty$-algebra onto a smaller filtered complex.
  2899	By the homotopy transfer package of
  2900	Appendix~\ref{app:homotopy-transfer}, the transferred higher
  2901	brackets $\{\ell_n\}_{n\ge 1}$ endow the target with a cyclic
  2902	$L_\infty$-structure. Its filtered $L_\infty$ quasi-isomorphism class
  2903	is denoted
  2904	\[
  2905	\Definfmod(\cA).
  2906	\]
  2907	The formula in
  2908	Definition~\ref{def:modular-deformation-complex} is one explicit
  2909	strict chart for this invariant object.
  2910	\end{construction}
  2911	
  2912	\begin{proposition}[Strictification principle for modular deformation theory; \ClaimStatusProvedHere]
  2913	\label{prop:modular-strictification-principle}
 succeeded in 51ms:
  4838	In the multi-channel regime, the correct framework is the
  4839	shadow obstruction tower
  4840	$\Theta_\cA^{\leq 2}, \Theta_\cA^{\leq 3}, \Theta_\cA^{\leq 4},\ldots$
  4841	with obstruction classes
  4842	$o_{r+1}(\cA)$ at each level
  4843	(Appendix~\ref{app:nonlinear-modular-shadows});
  4844	the all-degree convergence of this tower is proved by the
  4845	bar-intrinsic construction
  4846	(Theorem~\ref{thm:mc2-bar-intrinsic};
  4847	Theorem~\ref{thm:recursive-existence}).
  4848	\end{remark}
 succeeded in 51ms:
  2652	\end{theorem}
  2653	
  2654	\begin{remark}
  2655	The $A_\infty$-module structure on the bar resolution is a special case
  2656	of the general homotopy transfer theorem
  2657	(Appendix~\ref{app:homotopy-transfer}; see
  2658	Keller~\cite{Keller01} and Merkulov~\cite{Merkulov99} for the
  2659	original constructions). In the chiral setting, the transfer
  2660	data come from the operad structure on configuration spaces
  2661	(Definition~\ref{def:chiral-operad}).
  2662	\end{remark}
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1952,1959p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1952	where the cyclic deformation package is available through the
  1953	relevant order
  1954	(Chapter~\ref{app:nonlinear-modular-shadows}).
  1955	The branch-line reductions
  1956	(Appendix~\ref{app:branch-line-reductions}) extract exact
  1957	finite-dimensional quotients of this layer, including genus-$2$
  1958	transparency and the universal genus-$3$ constant~$7$ on the shared
  1959	$\widehat{\mathfrak{sl}}_2$/Virasoro/$\beta\gamma$ spectral sheet.


thinking
**Refining error reporting**

I’m considering focusing on the exact lines where inconsistencies first appear for each build artifact type. The user requested every inconsistency, but since there are many similar issues, grouping them might be better. We could specify the lines all within a PROBLEM section. For example, I could format it like this: `[MEDIUM] chapters/theory/higher_genus_foundations.tex:1582; chapters/theory/chiral_modules.tex:2657; ... — PROBLEM: ... FIX: ...`. This keeps the final report concise while still providing the necessary detail.
thinking
**Reviewing file structure**

Since this section comes before the appendix, I need to decide whether the file should refer to itself as a chapter or an appendix. I'll check the first line for the chapter designation, and it looks okay. However, calling it an appendix seems wrong. 

Maybe using a label prefix for `nonlinear_modular_shadows` could help, but that might be inconsistent. I should also check if there are circular dependencies among the promoted chapters. Although something might need an update in terms of the plan, it’s not entirely necessary at this point.
codex
The live seam is now split into three concrete failure modes: type mismatches in what the appendix theorems actually say, theorem-scope overreach when theory cites nonlinear-shadow results, and build-order drift where files in `appendices/` are treated as appendices even though `main.tex` promotes them to ordinary chapters.

Plan:
1. Re-read the source theorem statements in `appendices/homotopy_transfer.tex` and `appendices/nonlinear_modular_shadows.tex` against the exact theory-side invocations.
2. Separate genuine mathematical miscitations from pure naming/build-order drift.
3. Verify each candidate by checking the cited theorem statement, the local theory sentence, and `main.tex` include order before I keep it as a finding.


thinking
**Inspecting potential issues**

I need to check the `higher_genus_foundations` around line 1253, especially regarding the reference to `prop:e2-collapse-formality`. Then, I might find an issue with `quantum_corrections` at line 525, where the homotopy transfer chapter is misnamed as an appendix. If there's a general drift in build-order for homotopy transfer citations throughout the theory files, that could include `quantum_corrections`. There’s also a formula issue at line 360 that might not need separate mention if it's grouped. There are additional concerns in the appendices regarding inconsistent notation at lines 100-101; this could be worth noting despite being low severity. I might need to outline about seven findings overall.
thinking
**Analyzing theorem mismatches**

I’m noticing there's not just a citation mismatch but also an internal mismatch between theorem statements and proofs within the theory. The appendix theorem is mis-specified, which causes the body theorem to be mismatched as well. I could report both: a critical type error in the appendix and a high severity issue with the body's theorem misidentifying output. The surface presents as critical due to its false nature. The body theorem also relies on this false assertion, so assessing its severity is tricky. I want to avoid too many critical issues, but it may be warranted here.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '6084,6098p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6084	 contact invariant $\mathfrak{Q}^{\mathrm{contact}}_{\beta\gamma}$.
  6085	\item \emph{Virasoro, $\mathcal{W}_N$.}\;
  6086	 The shadow obstruction tower is infinite. All trace-log terms
  6087	 $\operatorname{Tr}((C_1 B_2)^m)$ contribute, and the anomaly
  6088	 series does not truncate. The full metaplectic cocycle carries
  6089	 infinite-order modular data.
  6090	\end{itemize}
  6091	This is the holographic restatement of the archetype trichotomy
  6092	(Theorem~\ref{thm:nms-archetype-trichotomy}).
  6093	\end{remark}
  6094	
  6095	\begin{remark}[Shadow tower as $A_\infty$ coproduct corrections (Vol~III)]
  6096	\label{rem:shadow-ainfty-coproduct-vol3}
  6097	The shadow invariants $S_k$ have a second interpretation discovered in Vol~III: they are the coefficients of the $A_\infty$ corrections $\delta^{(k)}$ to the Yangian coproduct $\Delta_z$. The full $A_\infty$ coproduct is $\Delta_z^{A_\infty} = \Delta_z^{\mathrm{Yangian}} + \sum_{k \geq 3} \hbar^{k-1} \delta^{(k)}$, where $\delta^{(3)}$ has coefficient $\alpha = 2$ (from $m_3(T,T,T) = -2T$) and $\delta^{(4)}$ has coefficient $S_4 = 10/27$ (from $m_4(T,T,T,T) = (40/27)T$). For class~$G$: all $\delta^{(k)} = 0$ and the Yangian coproduct is exact. For class~$M$: the coproduct has infinite corrections whose coefficients are precisely the shadow tower $\{S_k\}$. The shadow tower is therefore not merely a classification invariant: it encodes the $A_\infty$ corrections to the chiral quantum group coproduct. See Vol~III, Remark~\texttt{rem:ainfty-coproduct-shadow}.
  6098	\end{remark}


thinking
**Evaluating theorems and files**

I’m thinking through how to address the user’s inquiry about each inconsistency. It seems I could reference multiple files: higher_genus_modular_koszul, chiral_koszul_pairs, and higher_genus_complementarity. I wonder if I should also look for any other relevant files that address the same theorem. I’ll need to inspect a specific line. While considering grouping these files, I still have to give the user exact file and line references.
thinking
**Grouping high findings**

I think it's best to present a grouped approach to specific findings. I want to link together passages from higher_genus_modular_koszul, chiral_koszul_pairs, and higher_genus_complementarity. The problem arises as each claims the nms-archetype-trichotomy theorem applies to the mixed class but only proves the G/L/C trichotomy. My fix would be to cite the correct sections for Virasoro and principal W_N specifically. I also need to confirm the existence of certain theorems, and it looks like they do exist!
exec
/bin/zsh -lc "rg -n 'h_\\{\\\\mathrm\\{Hodge\\}\\}|Hodge decomposition of \\\\Omega|relative to the bar filtration' appendices/homotopy_transfer.tex chapters/theory --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/homotopy_transfer.tex:536:h_{\mathrm{Hodge}}\bigr)
appendices/homotopy_transfer.tex:539:$h_{\mathrm{Hodge}}$ is the contracting homotopy from the

thinking
**Evaluating unsupported notation**

Hmm, this notation seems unsupported, which could indicate a seam issue. The body doesn’t cite the symbol, and the theorem statement relies on a nonexistent Hodge decomposition. However, it might be a general unsupported theorem. Since the user wants a seam audit and the theorem is cited in the body, I could report on it. But I need to establish something solid — there’s no prior definition or construction of `iota_counit` or `h_Hodge`. I'll look into `iota_{\mathrm{counit}}`.
exec
/bin/zsh -lc "rg -n 'iota_\\{\\\\mathrm\\{counit\\}\\}|h_\\{\\\\mathrm\\{Hodge\\}\\}|Hodge decomposition' appendices/homotopy_transfer.tex chapters/theory --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/homotopy_transfer.tex:535:\bigl(\Omega(\Bbar(\cA)),\; \cA,\; \psi,\; \iota_{\mathrm{counit}},\;
appendices/homotopy_transfer.tex:536:h_{\mathrm{Hodge}}\bigr)
appendices/homotopy_transfer.tex:538:where $\iota_{\mathrm{counit}}$ is the canonical inclusion and
appendices/homotopy_transfer.tex:539:$h_{\mathrm{Hodge}}$ is the contracting homotopy from the
appendices/homotopy_transfer.tex:540:Hodge decomposition of $\Omega(\Bbar(\cA))$ relative to the bar
chapters/theory/higher_genus_foundations.tex:3243:By the Hodge decomposition, $\mathcal{H}^{1,1}(\Sigma_g)$
chapters/theory/higher_genus_complementarity.tex:3632:\item $t_k = \oint_{A_k} \omega_k$ are the $A$-period parameters arising from the Hodge decomposition of $H^1(\Sigma_g, \mathbb{C})$

thinking
**Evaluating report details**

I’m thinking about how to report this as medium-high. The appendix provides information on HTT/quasi-isomorphism invariance of bar construction, but it doesn’t present the stronger statement that Theorem A preserves quasi-isomorphisms. This is important; the bar-cobar adjunction is a quantum L∞ functor, which I need to consider in my explanation. I want to ensure I'm accurately conveying the nuances of this topic without oversimplifying things.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '1597,1660p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1597	
  1598	\begin{proof}
  1599	\emph{Step~1: Construction of the SDR.}
  1600	The bar complex $\barBgeom(\mathcal{A})$ is a chain complex of
  1601	$\mathcal{D}_X$-modules, graded by bar degree~$n$ and conformal
  1602	weight~$h$. Since we work over a field
  1603	(Convention~\ref{subsec:ambient-category}), the splitting lemma
  1604	(Lemma~\ref{lem:sdr-existence}) furnishes a strong deformation
  1605	retract:
  1606	\[
  1607	\begin{tikzcd}[column sep=large]
  1608	(\barBgeom(\mathcal{A}), d_{\mathrm{bar}})
  1609	 \arrow[r, shift left, "p"] &
  1610	(H^*(\barBgeom(\mathcal{A})), 0)
  1611	 \arrow[l, shift left, "\iota"]
  1612	\end{tikzcd}
  1613	\quad h\colon \barBgeom^n \to \barBgeom^{n-1},
  1614	\quad \mathrm{id} - \iota p = d_{\mathrm{bar}}\, h + h\, d_{\mathrm{bar}}.
  1615	\]
  1616	The SDR is constructed by choosing, at each conformal weight~$h$,
exec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '186,198p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   186	\emph{$\tilde{m}_2$.} The induced product:
   187	\[
   188	\tilde{m}_2(a, b) = p \, m_2(\iota(a), \iota(b)).
   189	\]
   190	
   191	\emph{$\tilde{m}_3$.} The \emph{Massey product} or $\Ainf$-associator:
   192	\begin{align*}
   193	\tilde{m}_3(a, b, c) &= p \, m_3(\iota(a), \iota(b), \iota(c)) \\
   194	&\quad + p \, m_2(h \, m_2(\iota(a), \iota(b)), \iota(c)) \\
   195	&\quad + (-1)^{|a|}\, p \, m_2(\iota(a), h \, m_2(\iota(b), \iota(c))).
   196	\end{align*}
   197	The sign $(-1)^{|a|}$ arises from commuting the homotopy $h$ (degree $-1$) past $\iota(a)$ (degree $|a|$) via the Koszul sign rule.
   198	


thinking
**Reviewing potential inconsistencies**

I’m exploring if `highe_genus_modular_koszul` misnames nonlinear_modular_shadows. The introduction refers to chapters, which might lead to internal inconsistencies. I think it’s a good idea to gather line numbers for other repeated references in the Appendix related to higher_genus_modular_koszul. I also need to check line numbers for quantum corrections and formulas. There’s a specific line in `chiral_hochschild_koszul` that seems correct, so it seems like we don't need nonlinear naming in that file. However, I need to mention the appendix theorem related to `thm:chiral-htt` and the local circularity issue.
thinking
**Inspecting the theorem**

I'm considering the theorem in the appendix, `thm:bar-cobar-htt`, related to homotopy transfer. I need to examine it since there's something undefined with `h_Hodge`. Let's check the line numbers; we already have lines 524-540 noted, but I’ll need to gather more information for clarity, especially on the missing details regarding `nl`. I want to ensure I get this right!
exec
/bin/zsh -lc "nl -ba appendices/homotopy_transfer.tex | sed -n '524,542p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   524	\label{thm:bar-cobar-htt}
   525	\index{homotopy transfer theorem!bar-cobar inversion}
   526	Let $\cA$ be a chiral Koszul algebra on a smooth curve~$X$.
   527	The bar-cobar counit
   528	\[
   529	\psi \colon \Omega(\Bbar(\cA)) \to \cA
   530	\]
   531	of Theorem~\textup{\ref{thm:bar-cobar-isomorphism-main}} is the
   532	\emph{canonical} $\Ainf$-quasi-isomorphism produced by the homotopy
   533	transfer theorem (Theorem~\ref{thm:htt}), applied to the SDR
   534	\[
   535	\bigl(\Omega(\Bbar(\cA)),\; \cA,\; \psi,\; \iota_{\mathrm{counit}},\;
   536	h_{\mathrm{Hodge}}\bigr)
   537	\]
   538	where $\iota_{\mathrm{counit}}$ is the canonical inclusion and
   539	$h_{\mathrm{Hodge}}$ is the contracting homotopy from the
   540	Hodge decomposition of $\Omega(\Bbar(\cA))$ relative to the bar
   541	filtration.
   542	\end{theorem}
exec
/bin/zsh -lc "rg -n 'prop:e2-collapse-formality' chapters/theory --glob '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:1253:Proposition~\ref{prop:e2-collapse-formality}).
chapters/theory/higher_genus_foundations.tex:2556:(a consequence of $E_2$ collapse on the Koszul locus; see Proposition~\ref{prop:e2-collapse-formality}).
chapters/theory/higher_genus_complementarity.tex:4765:\label{prop:e2-collapse-formality}


thinking
**Inspecting notation issues**

I’m looking at `chiral_hochschild_koszul`, particularly line 2900 — it mentions using a "homotopy transfer package" to transfer a quantum L∞ algebra. There seems to be a section in the appendix about extended HTT. I also need to check line 1146 in `higher_genus_foundations` to confirm if it’s just a seam issue or a deliberate choice. Notably, the mismatch with notation, where "An A∞ algebra consists of..." directs a reader incorrectly. I'll check line 101 in `general_relations` for mixed notations too.
thinking
**Considering audit inconsistencies**

The user wants a thorough audit and exact fixes for inconsistencies. I think mentioning the body theorem, along with some remarks about nilpotent structures and quantum corrections, could help illustrate potential misuse. I wonder if we should check specific lines in the `higher_genus_foundations` to see if they align with the `prop:e2-collapse-formality`. Additionally, I'll consider if `Appendix\ref{app:nonlinear-modular-shadows}` has some inconsistencies, given where it's included. I might compile a list of findings, possibly eight key points.
codex
- [CRITICAL] appendices/homotopy_transfer.tex:457 — PROBLEM: Theorem `thm:chiral-htt` states an SDR of the “underlying D-module” with `H = H^{\mathrm{ch}}_*(\cA)` (lines 457-460), but its proof switches to an SDR of `\Bbar(\cA) \to H^*(\Bbar(\cA))` (line 482). The theorem surface is conflating the transfer target. FIX: rewrite the theorem to one object only. Minimal repair: replace lines 457-460 by “suppose `(C,H,p,\iota,h)` is an SDR of a chosen dg model `C` for `\cA`,” delete `H = H^{\mathrm{ch}}_*(\cA)`, and move the Koszul-line vanishing claim into a separate proposition explicitly about the bar complex `\Bbar(\cA) \to H^*(\Bbar(\cA))`.

- [HIGH] chapters/theory/higher_genus_foundations.tex:1582 — PROBLEM: Theorem `thm:chain-vs-homology` says HTT gives a minimal `A_\infty` structure on `H^*(\mathcal A)` (lines 1582-1588), but the proof actually constructs the SDR on `\barBgeom(\mathcal A)` and transfers to `H^*(\barBgeom(\mathcal A))` (lines 1600-1638). Statement and proof are about different objects. FIX: change lines 1582-1593 to say the transfer lands on the chosen SDR target, here `H^*(\barBgeom(\mathcal A))`; if the intended target really is `H^*(\mathcal A)`, then rewrite the proof to construct that SDR instead of the bar-complex SDR.

- [HIGH] appendices/homotopy_transfer.tex:531 — PROBLEM: Theorem `thm:bar-cobar-htt` is cited as proved input, but its SDR data `\iota_{\mathrm{counit}}` and `h_{\mathrm{Hodge}}` are introduced only here (lines 535-540) and are not constructed anywhere in the audited seam. FIX: either add a preceding proposition that constructs a filtered SDR `(\Omega(\Bbar(\cA)), \cA, \psi, \iota, h)` with those maps, or weaken the theorem to an implication: “Assume such a filtered SDR exists; then HTT identifies `\psi` as the canonical `A_\infty` quasi-isomorphism.”

- [HIGH] chapters/theory/quantum_corrections.tex:359 — PROBLEM: The homotopy-transfer citation is not what the appendix proves. `\eta_{123}^{\mathrm{FM}}` is nowhere defined in the seam, and the appendix gives the tree formula `\tilde m_3` as a sum of HTT terms/boundary-stratum integrals (appendices/homotopy_transfer.tex:193-195, 624-652), not a single integral over `\overline{C}_3(X)`. Line 361 also drops `p`, `\iota`, the sign, and treats `h` as multiplication. FIX: replace lines 359-361 by the actual HTT formula
  `m_3(a,b,c)=p\,m_3(\iota a,\iota b,\iota c)+p\,m_2(h\,m_2(\iota a,\iota b),\iota c)+(-1)^{|a|}p\,m_2(\iota a,h\,m_2(\iota b,\iota c))`,
  or cite Proposition `prop:trees-boundary-strata` and write the sum over the two FM boundary strata instead of introducing `\eta_{123}^{\mathrm{FM}}`.

- [HIGH] chapters/theory/nilpotent_completion.tex:1176 — PROBLEM: “The passage from modes to states is the HTT” is not supported by Theorem `thm:chiral-htt`, which never mentions a mode/state comparison. FIX: replace lines 1176-1178 by “After passing to the positive-energy state-space model, HTT is applied weightwise to the resulting SDR,” or insert a separate proposition constructing the mode-to-state comparison before invoking HTT.

- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:32053,32292; chapters/theory/chiral_koszul_pairs.tex:3328,3449; chapters/theory/higher_genus_complementarity.tex:6085 — PROBLEM: These passages cite Theorem `thm:nms-archetype-trichotomy` as though it classifies the mixed class `M` / “Virasoro, `\mathcal W_N`”. But the cited theorem in appendices/nonlinear_modular_shadows.tex:1209-1224 proves only the three quartic-order cases `G/L/C` (Heisenberg, affine `\widehat{\mathfrak{sl}}_2`, `\beta\gamma`). Virasoro nontermination is separate in `thm:nms-finite-termination` (appendices/nonlinear_modular_shadows.tex:2190-2199), and principal `\mathcal W_N` mixed cubic/quartic behavior is only `cor:nms-principal-wn-mixed` (appendices/nonlinear_modular_shadows.tex:1637-1645). FIX: split the citation. Use `thm:nms-archetype-trichotomy` only for `G/L/C`; cite `thm:nms-finite-termination` for Virasoro; cite `cor:nms-principal-wn-mixed` only for principal `\mathcal W_N` through quartic order; if no theorem in scope proves infinite depth for all `\mathcal W_N`, replace “Virasoro, `\mathcal W_N`” by “Virasoro” or mark the `\mathcal W_N` extension conjectural.

- [MEDIUM] chapters/theory/higher_genus_foundations.tex:1582; chapters/theory/chiral_modules.tex:2657; chapters/theory/chiral_hochschild_koszul.tex:2900,2932; chapters/theory/quantum_corrections.tex:360,525 — PROBLEM: These lines call `app:homotopy-transfer` an appendix, but `main.tex:998-1000` explicitly promotes `appendices/homotopy_transfer.tex` into Part I before `\appendix` (`main.tex:1526`). FIX: replace each `Appendix~\ref{app:homotopy-transfer}` with `Chapter~\ref{app:homotopy-transfer}` or `Ch.~\ref{app:homotopy-transfer}` consistently.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:4843 — PROBLEM: This file repeatedly refers to `app:nonlinear-modular-shadows` as an appendix (also 10133, 12271, 12310, 13201, 15442, 15456, 29654, 30996), but `main.tex:1093` inputs `appendices/nonlinear_modular_shadows.tex` before `\appendix`. FIX: replace every `Appendix~\ref{app:nonlinear-modular-shadows}` in this file with `Chapter~\ref{app:nonlinear-modular-shadows}` or `Ch.~...`.

- [MEDIUM] chapters/theory/introduction.tex:1956; chapters/theory/chiral_hochschild_koszul.tex:5745,5777 — PROBLEM: These lines call `app:branch-line-reductions` an appendix, but `main.tex:1097` inputs `appendices/branch_line_reductions.tex` before `\appendix`. FIX: replace those occurrences with `Chapter~\ref{app:branch-line-reductions}` or `Ch.~...`.

- [LOW] appendices/general_relations.tex:100; chapters/theory/higher_genus_foundations.tex:1146 — PROBLEM: The cited appendix surface is curved, but the body definition is uncurved. The appendix writes `(\mathcal A,\{m_k\}_{k\ge0},\mu_0)` and uses `\mu_0` in the formulas, while the body at line 1146 defines an uncurved `A_\infty` algebra with `k\ge1` and sends the reader straight to that curved appendix. FIX: in `appendices/general_relations.tex`, replace `\mu_0` by `m_0` consistently in lines 100-113; in `higher_genus_foundations.tex:1146`, change the parenthetical to “for the curved extension with `m_0`, see Appendix~\ref{app:curved-ainfty-formulas}.”

## Summary
Checked: 25 | Findings: 10 | Verdict: FAIL
tokens used
384,127
