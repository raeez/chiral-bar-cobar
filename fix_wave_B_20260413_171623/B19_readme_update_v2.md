# B19_readme_update_v2 (201s)

Updated [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md) with a tight scoped patch.

- `FIXED`: page count updated from `~1,704` to `1,736`, matching the current built PDF.
- `FIXED`: test reporting corrected by clarifying `53 lib + 64 test files` and adding `3,571` collected tests.
- `FIXED`: replaced the scope-inflating theorem-status sentence with the current truthful status: `SC^{ch,top}` proved, `E_3`-topological proved for affine KM, Drinfeld-Sokolov/W, and freely-generated-PVA families, conjectural in general.
- `BLOCKED`: none.

Verification: re-read the edited block for coherence; confirmed `Pages: 1736` via `pdfinfo`; confirmed `3571 tests collected` via `python3 -m pytest compute/tests --collect-only -q`; greps for the stale patterns `~1,704`, `Zero conjectural algebraic inputs`, and the old `Compute modules` line returned no matches. `README.md` has no `\ref`/`\label` surface to validate.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar-vol2
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8798-c74a-7d62-acfe-dc674724bf97
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


TARGET: README.md (Vol II)
Same: update page count, test count, theorem status. No scope inflation.
mcp startup: no servers


thinking
**Evaluating README edits**

I need to act as a coding agent focused on editing the README.md to resolve audit findings. I might need to inspect the repository instructions, though this task seems straightforward since it's just a README update. The user mentioned reading audit findings, so I’ll check those for details, like updating page count, test count, and theorem status. I need to comply with AGENTs instructions for any necessary updates. It appears I need to be cautious to stay focused on the README.
thinking
**Updating exploration plans**

I need to update my plan for a substantial task, which seems necessary given its complexity. Before diving in, I should add commentary and frequently check for updates if it’s lengthy. I’ll run `git status`, review the README, and possibly inputs from main.tex to gather important metrics like page count, test count, and theorem status. It might be helpful to use the build surface to verify these aspects while remembering that the user has placed some restrictions on files. I'll check my skills to see what’s needed.
codex
Target is [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md); I’m using `vol2-build-surface` to verify page/test facts and `vol2-beilinson-rectification` to keep the edit minimal and truthful. I’ll read the README, check the live repo surface (`git status`, page count, test count, theorem-status claims), then patch only the incorrect lines.
exec
/bin/zsh -lc "sed -n '1,260p' README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol2-beilinson-rectification/SKILL.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
# A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT

**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* (this volume) | The 3D interpretation: what the engine computes |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Connection to Volume I

Every chapter depends on Vol I's five theorems:

| Vol I Theorem | What it supplies |
 succeeded in 51ms:
---
name: vol2-build-surface
description: Use when the task depends on LaTeX builds, build logs, warning classification, targeted pytest runs, or deciding whether a manuscript change is actually verified. Do not use for purely conceptual work with no executable verification surface.
---

# Vol II Build Surface

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
 M Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf
 M chapters/connections/conclusion.tex
 M chapters/connections/concordance.tex
 M chapters/connections/hochschild.tex
 M chapters/connections/line-operators.tex
 M chapters/connections/ordered_associative_chiral_kd.tex
 M chapters/connections/ordered_associative_chiral_kd_core.tex
 M chapters/connections/spectral-braiding-core.tex
 M chapters/examples/examples-worked.tex
 M chapters/examples/rosetta_stone.tex
 M chapters/frame/preface.tex
 M chapters/frame/preface_trimmed.tex
 M compute/audit/linear_read_notes.md
 D working_notes.pdf
 succeeded in 51ms:
---
name: vol2-beilinson-rectification
description: Use when the user asks to audit, rectify, fortify, fix, tighten, or converge a Vol II chapter, theorem, proof, introduction, appendix, or the live manuscript surface. Do not use for purely local copyedits with no mathematical or structural truth conditions.
---

# Vol II Beilinson Rectification

Run the full local rectification loop on the live surface.

## Inputs

- exact target file or theorem if given
- otherwise the smallest live surface implied by the user prompt

## Mandatory loop

1. Start with a short progress update naming the target and first verification step.
2. Register a nontrivial task in `update_plan`.
3. Read before editing:
   - target file


thinking
**Updating audit plan**

I need to update the plan since it’s pretty complex. The user wants me to look into specifics like page count, test count, and theorem status without any scope inflation. I should verify the actual page count from the PDF and consider counting files for the test count. I really want to ensure I'm checking main.tex for any relevant details and inspect the README for claims about theorem statuses to see if they’re outdated. I'll also need to compute actual numbers for those modules.
thinking
**Searching for theorem status**

I need to look up "Zero conjectural algebraic inputs" or find the theorem status table in the manuscript. I'll probably need to check the audit ledger as well for any relevant findings or current notes. It's crucial to gather all this information to ensure I fully understand the context and address any issues that are present. I’m eager to get this right so that I can provide the most helpful insights for the user!
codex
I’ve confirmed the README contains the likely stale claims: page count, compute/test counts, and a broad theorem-status sentence. Next I’m checking the live evidence surface for exact replacements so the patch only touches the incorrect facts.
Plan update
Verify the current README facts against the live build/manuscript surface, then make the smallest scoped README edit and re-check it.
  ✓ Read the assigned README and identify the stale factual claims to correct
  → Verify current page count, compute/test counts, and theorem-status scope from the live repo surface
  • Patch README.md minimally and re-read for coherence
  • Run targeted grep checks for forbidden/outdated patterns in README.md
exec
/bin/zsh -lc "pdfinfo Ainfinity_Chiral_Algebras_and_Chiral_Hochschild_Cohomology.pdf | rg '"'^Pages:'"'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'find compute/tests -type f | wc -l' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'find compute/lib -type f | wc -l' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "Zero conjectural algebraic inputs|conjectural algebraic|theorem status|Status" main.tex chapters appendices compute/audit/linear_read_notes.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
Pages:           1736
 succeeded in 50ms:
     129
 succeeded in 50ms:
     123
 succeeded in 51ms:
Total output lines: 4084

main.tex:102:\newcommand{\ClaimStatusProvedHere}{\textnormal{[proved here]}}
main.tex:103:\newcommand{\ClaimStatusProvedElsewhere}{\textnormal{[proved elsewhere]}}
main.tex:104:\newcommand{\ClaimStatusOpen}{\textnormal{[open]}}
main.tex:105:\newcommand{\ClaimStatusConjectured}{\textnormal{[conjectured]}}
main.tex:106:\newcommand{\ClaimStatusHeuristic}{\textnormal{[physical heuristic]}}
main.tex:208:\newcommand{\ClaimStatusConditional}{\textnormal{[conditional]}}
main.tex:209:\newcommand{\ClaimStatusNeedsVerification}{\textnormal{[needs verification]}}
main.tex:1164:\begin{remark}[Status of results]
compute/audit/linear_read_notes.md:6:- Status: COMPLETE
compute/audit/linear_read_notes.md:16:   Status: `FIXED`
compute/audit/linear_read_notes.md:26:- Status: IN PROGRESS
compute/audit/linear_read_notes.md:36:   Status: `PENDING`
compute/audit/linear_read_notes.md:44:   Status: `PENDING`
compute/audit/linear_read_notes.md:52:   Status: `PENDING`
compute/audit/linear_read_notes.md:60:   Status: `PENDING`
compute/audit/linear_read_notes.md:68:   Status: `PENDING`
compute/audit/linear_read_notes.md:73:- Status: COMPLETE
compute/audit/linear_read_notes.md:83:   Status: `FIXED`
exec
/bin/zsh -lc 'find compute -type f | wc -l' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"PROVED|CONJECTURAL|OPEN|Status \\(updated|E3-topological|global triangle|modular operad|pentagon\" chapters/frame chapters/connections chapters/examples README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
    5245
 succeeded in 51ms:
Total output lines: 290

chapters/frame/preface_trimmed.tex:615:is the Feynman transform of the modular operad
chapters/frame/preface_trimmed.tex:720: modular operad (Theorems~\ref{thm:modular-bar}
chapters/examples/w-algebras-w3.tex:791:\item \textbf{$m_5$:} Involves 5-point tree and 1-loop diagrams. The tree part has pentagonal symmetry; the loop part involves "ladder" and "star" topologies.
chapters/examples/w-algebras-w3.tex:912: (Definition~\ref{def:E3-topological-algebra}):
chapters/examples/w-algebras-w3.tex:919: Theorem~\ref{thm:E3-topological-DS}.
chapters/frame/preface.tex:155:the partially modular operad $\SCchtop_{\mathrm{mod}}$ with
chapters/frame/preface.tex:193:general chiral algebras is a modular operad governing
chapters/frame/preface.tex:202:(Theorem~\ref{thm:E3-topological-km}).  For $W$-algebras via Drinfeld--Sokolov reduction---principal or
chapters/frame/preface.tex:205:(Theorems~\ref{thm:E3-topological-DS}
chapters/frame/preface.tex:206:and~\ref{thm:E3-topological-DS-general}): the BRST identity
chapters/frame/preface.tex:228:factorisation, BV/BRST, and convolution---and a pentagon of
chapters/frame/preface.tex:230:(\S\ref{sec:SC-pentagon}).
chapters/frame/preface.tex:426:The global triangle (boundary determines bulk determines
chapters/frame/preface.tex:899:At $n = 4$: the Stasheff pentagon, five boundary faces, $m_4$
chapters/frame/preface.tex:1036:is the Feynman transform of the modular operad
chapters/frame/preface.tex:1288:(iv)~\emph{The global triangle}: boundary determines bulk
chapters/frame/preface.tex:1291:(v)~\emph{The Stokes regularity gap}: modular operad composition
chapters/examples/examples-worked.tex:4306:  (Definition~\ref{def:E3-topological-algebra}): \textbf{proved}
codex
The live counts have moved substantially: the built PDF is 1,736 pages, and the `compute` tree now has far more files than the README advertises. I’m narrowing the test-count definition now so the replacement matches the repository’s own conventions, and I’m reading the manuscript’s current status summary to replace the scope-inflating theorem-status sentence with something accurate.
exec
/bin/zsh -lc "sed -n '1035,1085p' chapters/connections/conclusion.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '180,240p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/tests -type f -name '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/lib -type f -name '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/lib -type f | sed 's#"'^#/#'"' | head -40" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/tests -type f | sed 's#"'^#/#'"' | head -40" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
\end{enumerate}

\subsection{Major open conjectures}
\label{subsec:major-open-conjectures}

The following list records the principal open problems and conjectures
of the programme, with their current status and the specific gap
that remains in each case.

\begin{center}
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{@{}p{4.8cm}lp{5.2cm}@{}}
\textbf{Conjecture / Problem} & \textbf{Status} & \textbf{Gap} \\
\hline
$\Ethree$-topological for affine KM
 (Thm~\ref{thm:E3-topological-km})
 & Proved
 & --- \\
$\Ethree$-topological via principal DS reduction
 succeeded in 51ms:
and the derived centre (Stages~3--4),
Part~\ref{part:examples} is the characteristic datum and
modularity (Stages~6--7), Part~\ref{part:holography} is the
standard HT landscape (Stage~5), Part~\ref{part:gravity} is 3d
quantum gravity (Stages~8--9), and Part~\ref{part:frontier} is the
frontier.

Stages~0--8 are proved.  Stage~9 is proved for the affine,
Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
conjectural beyond those families: the passage from
$\SCchtop$ to $E_3$-topological requires both a 3d
holomorphic-topological theory whose boundary is $\cA$ \emph{and} a
conformal vector at non-critical level.  The missing ingredient for
general chiral algebras is a modular operad governing
$\Ainf$-algebras in $\Eone$-chiral algebras
(whose genus-zero part is constructed in
Definition~\ref{def:modular-operad-ainf-chiral} and
Proposition~\ref{prop:genus0-product-decomposition}; the full
modular extension to genus $\geq 1$ remains open)---the operad
whose algebras are the 3d bulk theories.  For affine Kac--Moody at
 succeeded in 51ms:
      61
 succeeded in 51ms:
      64
 succeeded in 51ms:
/compute/lib/ainfty.py
/compute/lib/celestial_ope_from_shadow.py
/compute/lib/genus2_graph_sum.py
/compute/lib/exact_wkb_stokes.py
/compute/lib/modular_pva_quantization.py
/compute/lib/lg_ainfty_chain_level.py
/compute/lib/ordered_chiral_kd_engine.py
/compute/lib/factorization_modular_engine.py
/compute/lib/koszul_epstein_steps_bc.py
/compute/lib/hochschild_bulk_bridge.py
/compute/lib/genus2_obstruction_engine.py
/compute/lib/affine_half_space_bv_engine.py
/compute/lib/pva_descent_chain_level.py
/compute/lib/gravity_3d_engine.py
/compute/lib/modular_obstruction_engine.py
/compute/lib/pva_descent_coefficients_engine.py
/compute/lib/anomaly_completed_engine.py
/compute/lib/km_c4_root_mult.py
/compute/lib/bulk_boundary_duality_engine.py
/compute/lib/__init__.py
 succeeded in 51ms:
/compute/tests/test_cross_engine_consistency.py
/compute/tests/test_planted_forest_obstruction.py
/compute/tests/test_pva_axioms.py
/compute/tests/test_swiss_cheese_verification.py
/compute/tests/test_affine_kac_moody_pva.py
/compute/tests/test_holographic_ht_engine.py
/compute/tests/test_session_results.py
/compute/tests/test_line_operators_engine.py
/compute/tests/test_affine_half_space_bv_engine.py
/compute/tests/test_genus1_kappa_verification.py
/compute/tests/test_genus1_intersection.py
/compute/tests/test_d4_triality_bar.py
/compute/tests/test_pva_descent_chain_level.py
/compute/tests/test_collision_residue_rmatrix.py
/compute/tests/test_genus_one_bridge.py
/compute/tests/test_koszul_epstein_steps_bc.py
/compute/tests/test_borcherds_c4_structure.py
/compute/tests/test_pva_descent_coefficients_engine.py
/compute/tests/test_non_simply_laced_rmatrix.py
/compute/tests/test_swiss_cheese_virasoro_wheels.py


thinking
**Verifying page counts**

I'm considering how to create a summary that accurately reflects the page count in the README. I might need to check the actual number of `.py` files in the compute/tests directory and confirm if I should include `__init__.py` files. The README mentions "Compute modules | 53 lib + 64 test," but I need to verify if the 53 count is outdated. The user has specifically asked to update the test count, so that's important to clarify. This feels a bit complicated!
thinking
**Checking update requirements**

I'm thinking that the audit findings might have mentioned the same updates for page count, test count, and theorem status. The README possibly reflects a test count source of 61 for lib files and 64 for tests. Since the user mentioned "same," it's likely referring to updates from another repository. I need to verify if there's a change needed in the test count. I'll look at the top-level test files in `compute/tests`, excluding `__init__.py`, to confirm how many there are. Let's check if it's 63!
exec
/bin/zsh -lc "find compute/lib -maxdepth 1 -type f -name '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/tests -maxdepth 1 -type f -name 'test_*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"53 lib \\+ 64 test|Compute modules|Zero conjectural algebraic inputs|~1,704\" README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute -type f -name 'test_*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
      63
 succeeded in 52ms:
      53
 succeeded in 50ms:
42:| Pages | ~1,704 |
45:| Compute modules | 53 lib + 64 test |
51:Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
78:  compute/                  53 lib + 64 test files
 succeeded in 52ms:
     884


thinking
**Evaluating file counts**

I’m looking into the results of my command to find Python files. It shows 53 top-level files in the `compute` library, plus 64 test files, including `__init__.py`. The README might not be outdated, but the user mentioned updating the test count. I think they might be referring to a different metric, such as the actual count of test cases from `pytest`. I’ll need to check if there are more nested tests or consider what the user specifically wants regarding the count.
thinking
**Investigating test file counts**

I'm searching for line or test counts across different sources, possibly in other READMEs or summaries. The user mentioned they want an updated test count, maybe exceeding 64 due to subdirectories. I checked the tests in `compute/tests` and found a surprising 884. This seems high—perhaps it includes backups or autogenerated files. I’ll need to examine if this count is accurate, considering possible nested directories or shells affecting my commands. I might not need to inspect the heads, but something feels off.
codex
The README’s old `53 lib + 64 test` line is only “true” if you count top-level Python files in `compute/lib` and include `compute/tests/__init__.py` as a test file. I’m checking whether the audit intended file counts or actual pytest tests, because that determines the smallest truthful edit.
exec
/bin/zsh -lc "find compute/tests -type f -name 'test_*.py' | head -20" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "find compute/tests -type f -name '*.py' | wc -l" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "Zero conjectural algebraic inputs|Stage~9|Conjectural|Partially proved|proved for the affine|freely-generated-PVA" chapters/frame/preface.tex chapters/connections/conclusion.tex chapters/connections/3d_gravity.tex chapters/connections/hochschild.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
compute/tests/test_cross_engine_consistency.py
compute/tests/test_planted_forest_obstruction.py
compute/tests/test_pva_axioms.py
compute/tests/test_swiss_cheese_verification.py
compute/tests/test_affine_kac_moody_pva.py
compute/tests/test_holographic_ht_engine.py
compute/tests/test_session_results.py
compute/tests/test_line_operators_engine.py
compute/tests/test_affine_half_space_bv_engine.py
compute/tests/test_genus1_kappa_verification.py
compute/tests/test_genus1_intersection.py
compute/tests/test_d4_triality_bar.py
compute/tests/test_pva_descent_chain_level.py
compute/tests/test_collision_residue_rmatrix.py
compute/tests/test_genus_one_bridge.py
compute/tests/test_koszul_epstein_steps_bc.py
compute/tests/test_borcherds_c4_structure.py
compute/tests/test_pva_descent_coefficients_engine.py
compute/tests/test_non_simply_laced_rmatrix.py
compute/tests/test_swiss_cheese_virasoro_wheels.py
 succeeded in 51ms:
      64
 succeeded in 51ms:
chapters/frame/preface.tex:160:Stage~9 is topologization: given a 3d holomorphic-topological
chapters/frame/preface.tex:174:Deligne conjecture.  The $E_3$ layer (Stage~9) is
chapters/frame/preface.tex:187:Stages~0--8 are proved.  Stage~9 is proved for the affine,
chapters/frame/preface.tex:188:Drinfeld--Sokolov/$W$, and freely-generated-PVA lanes, and
chapters/frame/preface.tex:201:(Costello--Li), and Stage~9 is proved
chapters/frame/preface.tex:204:theorem, and Stage~9 is proved
chapters/frame/preface.tex:217:$E_3$-topological (Stage~9) is a \emph{special case}, requiring a
chapters/frame/preface.tex:244:The critical level is the boundary of Stage~9: all stages through~8
chapters/frame/preface.tex:665:Drinfeld--Sokolov/$W$ and freely-generated-PVA lanes; beyond
chapters/frame/preface.tex:1283:proved affine, Drinfeld--Sokolov/$W$, and freely-generated-PVA
chapters/connections/conclusion.tex:1064: & Conjectural
chapters/connections/conclusion.tex:1070: & Conjectural
chapters/connections/conclusion.tex:1084: & Partially proved
chapters/connections/conclusion.tex:1100: & Partially proved
chapters/connections/3d_gravity.tex:2183:\begin{remark}[Conjectural Virasoro realization of lines; \ClaimStatusConjectured]
exec
/bin/zsh -lc 'python3 -m pytest compute/tests --collect-only -q' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 781ms:
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_even_vanishing_k12[12]
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_even_vanishing_k14_TRUNCATION_BUG
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_polynomial_match_k13[13]
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_T_coefficient_k13[13]
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_roots_k13[13]
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_functional_equation_extended[12]
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_functional_equation_extended[14]
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_catalan_numbers_extended
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_profile_polynomial_r5
compute/tests/test_adversarial_verification.py::TestCatalanFactorisationExtended::test_max_deriv_boundary_detection
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_B2_casimir_symmetry
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_G2_casimir_symmetry
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_G2_jacobi
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_G2_antisymmetry
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_G2_killing_invariance
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_G2_dimension
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_G2_dual_coxeter_number
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_B2_cybe_algebraic
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_G2_cybe
compute/tests/test_adversarial_verification.py::TestNonSimplyLacedAdversarial::test_B2_casimir_trace




thinking
**Evaluating theorem status clarity**

I’m realizing that my current sentence is too inflated with scope. It’s important to summarize the status of the theorem in a concise way. I might rephrase it to be clearer, like: “Stages 0–8 are proved; Stage 9 is proved for certain families, but conjectural beyond that.” This wording could capture the theorem status effectively without adding unnecessary details. I'll check for any other claims in the README that might affect this.
thinking
**Reviewing theorem status updates**

I’m thinking about updating the sentences concerning the PVA descent and spectral Drinfeld strictification. Those phrases seem acceptable, especially since they clarify status without inflation. There’s a broader sentence that might need to be revised, though. I should consider whether the counts for anti-patterns are current, but the user didn’t request this. I’ll focus on what's listed and relevant, leaving the anti-pattern row untouched unless it becomes critical for accuracy. Keeping changes scoped tightly is key!
thinking
**Updating page count**

I’m considering whether to use an approximate page count of `1,736` or the exact count of `1,736`. Since the README uses approximations, it might be nice to stick with that style, but the user seems to want an update. The current row shows `1,704`, which I could change to `1,736` for accuracy, especially since that reflects the built PDF. However, I need to ensure the page count is reliable, as there may be uncommitted changes in the repo.
thinking
**Verifying page counts and tests**

I think the page count should reflect the current PDF in the working tree, and it might be good to note whether that count corresponds to the current version, especially after edits. I should probably verify if `pytest --collect-only` succeeded, which would show evidence for the 3571 tests. Now that I’ve checked, it did succeed! 

Next, I need to inspect the README for the status section and provide commentary before making any edits. Let's update the plan for step 2 as well!
codex
I’ve pinned the live facts: `pdfinfo` reports 1,736 pages, `pytest --collect-only -q compute/tests` collects 3,571 tests, and the manuscript status surface says Stage 9 is proved only for affine KM, DS/W, and freely-generated-PVA lanes, with the general case still conjectural. I’m patching just those README lines, and I’ll keep the existing structure intact.
Plan update
  ✓ Read the assigned README and identify the stale factual claims to correct
  ✓ Verify current page count, compute/test counts, and theorem-status scope from the live repo surface
  → Patch README.md minimally and re-read for coherence
  • Run targeted grep checks for forbidden/outdated patterns in README.md



thinking
**Revising layout decisions**

I see that the layout line still shows the file count instead of the test count. Keeping it as the file count might be best. I can add a row for `Collected tests | 3,571` after the compute modules. The status section should include both modules and the actual test count. The user wants a status table correction, so maybe updating `Compute modules` to `Compute files` would work better. I think I’ll go for that adjustment!
thinking
**Clarifying the repository layout**

Okay, that clarifies things! The repository layout already mentions `files`, which is good. I need to create a theorem-status sentence that captures the current nuance. I’m thinking of something like: "Stages 0–8 are proved; Stage 9 (`E_3`-topological) is proved for affine Kac–Moody, Drinfeld–Sokolov/$W$, and freely-generated PVA families, but remains conjectural in general." This fits with the preface. I wonder if I should mention the modular operad; I'm not quite sure.
thinking
**Considering open problems**

I’m thinking about open problems like modular operad genus ≥1 and global triangle class M. It seems saying “the SC package is proved” or “E3 upgrade proved for...” is fine because they don’t claim everything else. That’s great. I may need to add a `Collected tests` row from pytest collect to enhance clarity. Let’s go ahead and patch that up! Keeping track of these details is key.
file update
M /Users/raeez/chiral-bar-cobar-vol2/README.md
@@ -41,6 +41,7 @@
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
@@ -50,3 +51,3 @@
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The $\SC^{\mathrm{ch},\mathrm{top}}$ package is proved; the $E_3$-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/$W$, and freely-generated-PVA families, and remains conjectural in general.
 
apply_patch(auto_approved=true) exited 0 in 18ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/README.md
file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..bf6fecf50f93ecb379f197219c5caf04f1a3c0b2
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The $\SC^{\mathrm{ch},\mathrm{top}}$ package is proved; the $E_3$-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/$W$, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 

file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..bf6fecf50f93ecb379f197219c5caf04f1a3c0b2
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The $\SC^{\mathrm{ch},\mathrm{top}}$ package is proved; the $E_3$-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/$W$, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 

codex
The patch is in. I’m re-reading the edited block now and running focused greps for the stale phrases the audit was targeting, so I can confirm the README no longer advertises the old counts or the overbroad theorem-status claim.
exec
/bin/zsh -lc "sed -n '34,90p' README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"~1,704|Zero conjectural algebraic inputs|\\| Compute modules \\| 53 lib \\+ 64 test \\|\" README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'git diff -- README.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
- **V. The Standard HT Landscape**: YM boundary, celestial holography, anomaly-completed Koszul duality, holographic reconstruction
- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26
- **VII. The Frontier**: All conditional and conjectural material; no earlier part depends on this

## Status

| Metric | Value |
|--------|------:|
| Pages | 1,736 |
| Tagged claims | ~2,650+ |
| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
| Compute files | 53 lib + 64 test files |
| Collected tests | 3,571 |
| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
| Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
| Cross-volume bridges | 15 (including 3D gravity climax row) |
| Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |

The $\SC^{\mathrm{ch},\mathrm{top}}$ package is proved; the $E_3$-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/$W$, and freely-generated-PVA families, and remains conjectural in general.

 exited 1 in 51ms:

 succeeded in 50ms:
diff --git a/README.md b/README.md
index 0027e39..bf6fecf 100644
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@ Every chapter depends on Vol I's five theorems:
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..bf6fecf50f93ecb379f197219c5caf04f1a3c0b2
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The $\SC^{\mathrm{ch},\mathrm{top}}$ package is proved; the $E_3$-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/$W$, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 



thinking
**Checking README for LaTeX compatibility**

I need to check if there’s an outdated anti-pattern row that isn’t assigned, and maybe mention any residual risks. I’ll run another grep for theorem status using the pattern “in general.” I could also search for overbroad phrases like “Zero conjectural.” 

Now, I’m considering if the README Markdown using LaTeX math is okay, and I see it already includes `SC^{ch,top}` in plain text. GitHub supports inline math now, but adding LaTeX commands with `$...$` might not render properly.
thinking
**Refining README format**

To ensure safety and consistency, I think it’s best to avoid TeX markup and just use plain text. For instance, I could phrase it like: “The SC^{ch,top} package is proved; the E_3-topological upgrade...” without any `$` or `--`. 

It would be good to stick to the existing style. I might need to patch the document to remove math delimiters for that consistency, and I believe making this minimal refinement is the way to go!
codex
The README block is coherent, and the stale patterns are gone. One small consistency cleanup remains: the replacement sentence should match the README’s existing plain-text math style rather than switch to inline TeX delimiters.
file update
M /Users/raeez/chiral-bar-cobar-vol2/README.md
@@ -51,3 +51,3 @@
 
-The $\SC^{\mathrm{ch},\mathrm{top}}$ package is proved; the $E_3$-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/$W$, and freely-generated-PVA families, and remains conjectural in general.
+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
 
apply_patch(auto_approved=true) exited 0 in 18ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar-vol2/README.md
file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..987249a5400811dbe3e52c6535b5ce070e124937
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 

file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..987249a5400811dbe3e52c6535b5ce070e124937
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 

exec
/bin/zsh -lc "sed -n '39,56p' README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"~1,704|Zero conjectural algebraic inputs|\\"'$SC|'"\\"'$E_3|'"\\| Compute modules \\|\" README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

| Metric | Value |
|--------|------:|
| Pages | 1,736 |
| Tagged claims | ~2,650+ |
| Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
| Compute files | 53 lib + 64 test files |
| Collected tests | 3,571 |
| Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
| Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
| Cross-volume bridges | 15 (including 3D gravity climax row) |
| Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |

The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.

## Build

```bash
 exited 1 in 52ms:

file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..987249a5400811dbe3e52c6535b5ce070e124937
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 


thinking
**Updating plans**

I think I need to finalize the update to my plan. It’s important to make sure everything is completed accurately before moving forward. I wonder what specific aspects might need my attention or if I should check for any loose ends. Making sure I don't overlook anything will really help streamline the process. Okay, let's review what I've got and adjust anything necessary to ensure it's all set!
Plan update
  ✓ Read the assigned README and identify the stale factual claims to correct
  ✓ Verify current page count, compute/test counts, and theorem-status scope from the live repo surface
  ✓ Patch README.md minimally and re-read for coherence
  ✓ Run targeted grep checks for forbidden/outdated patterns in README.md
file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..987249a5400811dbe3e52c6535b5ce070e124937
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 



thinking
**Structuring findings**

I need to create a concise final answer that states "FIXED" or "BLOCKED" for each finding and highlight verification. Also, I might mention that there are no references or labels touched in the README. 

Simple bullet points could help organize this list. I’ll note that I verified using `pdfinfo`, `pytest --collect-only -q`, and manuscript status lines, and include mentions of grep. The README was the only document modified, and I could summarize that there are no blockers.
thinking
**Finalizing README updates**

I could note in the README that I've made several updates. For instance, I've fixed the page count to 1,736 and clarified that there are 53 library files and 64 test files, with a total of 3,571 collected tests. I replaced an overly broad theorem status claim with a more scoped statement, confirming certain topological proofs. I also found no blockers during verification, and the README shows no `\ref` or `\label` issues. I should ensure my summary stays under 50 lines.
codex
Updated [README.md](/Users/raeez/chiral-bar-cobar-vol2/README.md) with a tight scoped patch.

- `FIXED`: page count updated from `~1,704` to `1,736`, matching the current built PDF.
- `FIXED`: test reporting corrected by clarifying `53 lib + 64 test files` and adding `3,571` collected tests.
- `FIXED`: replaced the scope-inflating theorem-status sentence with the current truthful status: `SC^{ch,top}` proved, `E_3`-topological proved for affine KM, Drinfeld-Sokolov/W, and freely-generated-PVA families, conjectural in general.
- `BLOCKED`: none.

Verification: re-read the edited block for coherence; confirmed `Pages: 1736` via `pdfinfo`; confirmed `3571 tests collected` via `python3 -m pytest compute/tests --collect-only -q`; greps for the stale patterns `~1,704`, `Zero conjectural algebraic inputs`, and the old `Compute modules` line returned no matches. `README.md` has no `\ref`/`\label` surface to validate.
file update:
diff --git a/README.md b/README.md
index 0027e390d734f80295cd52b77f00a902f11fc158..987249a5400811dbe3e52c6535b5ce070e124937
--- a/README.md
+++ b/README.md
@@ -39,16 +39,17 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~1,704 |
+| Pages | 1,736 |
 | Tagged claims | ~2,650+ |
 | Source files | 19 theory + 13 examples + 72 connections = 104 chapter .tex + 2 appendices |
-| Compute modules | 53 lib + 64 test |
+| Compute files | 53 lib + 64 test files |
+| Collected tests | 3,571 |
 | Anti-patterns | V2-AP1 through V2-AP39 + AP150-AP175 + FM24-FM57 |
 | Seven-faces master | Per-face status tags (F1-F7 with individual scope qualifiers) |
 | Cross-volume bridges | 15 (including 3D gravity climax row) |
 | Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
 
-Zero conjectural algebraic inputs beyond the standing physical axioms, which have been made explicit as derived consequences.
+The SC^{ch,top} package is proved; the E_3-topological upgrade is proved for affine Kac--Moody, Drinfeld--Sokolov/W, and freely-generated-PVA families, and remains conjectural in general.
 
 ## Build
 

tokens used
116,135
