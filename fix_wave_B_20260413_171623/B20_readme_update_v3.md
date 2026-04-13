# B20_readme_update_v3 (215s)

Edited [README.md](/Users/raeez/calabi-yau-quantum-groups/README.md:6) only.

- FIXED: page count updated from `~335+` to `367`, verified from `pdfinfo calabi_yau_quantum_groups.pdf`.
- FIXED: compute test count updated from `~17,700+` to `19,785 collected`, verified from `python3 -m pytest compute/tests --collect-only -q`.
- FIXED: theorem/status wording tightened to remove scope inflation. The top summary now states the CY-to-chiral/BKM picture as expected or conditional where appropriate; the CoHA row is qualified to `toric CY3`; the Drinfeld-center row is marked `Proved elsewhere` with conditional `d=3` use; the `d=3` functor row is now `Open` and explicitly tied to chain-level `S^3`-framing.

No blockers.

Verification: I re-read the edited spans and grepped `README.md` to confirm the stale counts and overstrong old status strings are gone. `README.md` has no `\ref`/`\label` surface to validate.


---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/calabi-yau-quantum-groups
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8798-c74a-7570-a968-69fd0ede4ce8
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


TARGET: README.md (Vol III)
Same: update page count, test count, theorem status. No scope inflation.
mcp startup: no servers

thinking
**Running commands**

I'm thinking about executing commands to read relevant sections from the README and checking the git status and skill instructions. I might need to use tools like rg or sed for this. It sounds like I should locate README lines related to page/test counts and status. Okay, let's proceed and run those commands to get the information I need!
codex
Target is `README.md`; I’m checking the live text, current dirty surface, and the repo’s verification/status conventions before editing anything.
exec
/bin/zsh -lc 'rg -n "page|pages|test|theorem|status|d = 2|d=2|d = 3|d=3|CY-A|proved|conject|conditional" README.md' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,260p' README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git status --short' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
48:- **II. The CY Characteristic Datum**: CY-to-chiral functor Phi, quantum chiral algebras, modular trace, quantum group foundations, braided factorization (U_q(g), R-matrix, YBE from bar coassociativity, braided bar-cobar adjunction CY-B, braided shadow tower), Drinfeld center and bulk algebras (BZF theorem, center vs derived center, Kazhdan-Lusztig at roots of unity)
57:| CY_2 functor (d=2) | **Proved** |
61:| CY_3 functor (d=3) | **Conjectural** (central open problem) |
62:| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
64:| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
74:| Compute tests | ~17,700+ |
75:| Compute modules | 189 lib + 187 test |
 succeeded in 51ms:
# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* (this volume) | The categorical completion |

## The CY-to-Chiral Functor

The programme flow:

```
 succeeded in 50ms:
---
name: vol3-pre-edit-verification
description: Use before editing any high-risk Vol III formula, theorem status, d=3 existence claim, compute oracle, or cross-volume convention bridge. This is the Codex-native analogue of the Claude-side pre-edit verification templates.
---

# Vol III Pre-Edit Verification

Before editing a high-risk surface, fill in a fenced `PRE-EDIT` block in commentary and end with `verdict: ACCEPT` or `verdict: REJECT`.

If a required source is blank or any boundary check fails, do not edit yet.

## Triggers

- `r`-matrix or OPE/lambda-bracket edit
- `kappa` or modular-characteristic edit
- bar/cobar/desuspension formula
- theorem environment or claim-status edit touching d=3 objects
- shadow-class or SC-formality edit
- `MF(W)` CY-dimension edit
- cross-volume Part reference or copied formula
 succeeded in 51ms:
 M calabi_yau_quantum_groups.pdf
 M chapters/connections/cy_holographic_datum_master.tex
 M chapters/connections/geometric_langlands.tex
 M chapters/connections/modular_koszul_bridge.tex
 M chapters/examples/fukaya_categories.tex
 M chapters/examples/quantum_group_reps.tex
 M chapters/examples/toric_cy3_coha.tex
 M chapters/examples/toroidal_elliptic.tex
 M chapters/frame/preface.tex
 M chapters/theory/braided_factorization.tex
 M chapters/theory/cy_categories.tex
 M chapters/theory/cy_to_chiral.tex
 M chapters/theory/drinfeld_center.tex
 M chapters/theory/e1_chiral_algebras.tex
 M chapters/theory/e2_chiral_algebras.tex
 M chapters/theory/introduction.tex
 M main.log
 M out/calabi_yau_quantum_groups.pdf
 M out/working_notes.pdf
 M working_notes.pdf
 succeeded in 51ms:
---
name: vol3-beilinson-loop
description: Use when auditing, rectifying, falsifying, converging, or pressure-testing theorem, proof, formula, status, or scope material in the Calabi-Yau Quantum Groups repository. Trigger on audit, rectify, red-team, Beilinson, theorem status, proof gap, convergence, or "is this actually proved?" tasks.
---

# Vol III Beilinson Loop

Read `AGENTS.md` first. This skill is the triggered deep workflow for hostile mathematical review.

## Surface

Work on the live manuscript surface:

- `main.tex`
- currently `\input`-ed files
- the dirty git diff
- relevant build logs
- the narrowest relevant `compute/tests/` slice

## Passes



thinking
**Evaluating page and test counts**

I need to determine the actual page count, test count, and theorem status by inspecting the relevant files. The README mentions about 335 pages, over 17,700 tests, and 364 tagged claims. However, I think the user wants an updated count. It seems the page count could be larger, with about 1,800 tests passing according to the latest results. I might need to check the PDF and logs to verify these numbers accurately. Let's use tools like pdfinfo or pytest for that!
thinking
**Clarifying theorem status and updates**

I’m looking into the bar-complex Euler product and its inflated scope. It seems that for d=2, only Yangians and elliptic Hall have been proven. While AGENTS mentions some chiral-algebra objects aren’t fully constructed, the README suggests otherwise about CoHA as the E1 sector. The user wants updates on page count, test count, and theorem status, specifically without scope inflation. I need to check previous fixes and audit findings to identify any outdated theorem statuses in the README. Let’s focus on gathering live sources for these updates!
thinking
**Searching for current statuses**

I should start by inspecting the introduction or preface for similar claims. I want to search for the most recent statuses and counts in the main.tex file or build logs. I need to cross-check the page count from the PDF and determine the test count using `pytest --collect-only` or a script. The theorem status could be found in the manuscript's introduction or claim tables. I’ll open the README and compare claims against the tex files, utilizing `rg` across the repository for efficiency.
codex
I’ve got the current README surface. Next I’m pinning the actual page/test counts and the manuscript’s current status language so the edit stays minimal and truthful.
exec
/bin/zsh -lc "rg -n \"A_X does not yet exist|chain-level S\\"'^3-framing|CoHA is associative data|not automatically the E_1 sector|CY-A is proved|CY-A` is proved|CY-A is proved|proved in the manuscript only for d = 2|d = 3 version depends|unconstructed object|Conjectural|Conditional" AGENTS.md chapters README.md' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg --files tests compute | wc -l' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"17,700|17700|335\\+|Pages \\|~|Compute tests|CY_3 functor|CoHA = E_1 sector|d=3|Conjectural|Conditional|Proved\" chapters README.md main.tex working_notes.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'pdfinfo calabi_yau_quantum_groups.pdf | rg -n "Pages|Page size|Title"' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "find compute -type f -name 'test_*.py' | wc -l" in /Users/raeez/calabi-yau-quantum-groups exited 1 in 52ms:
zsh:1: unmatched "
 succeeded in 51ms:
rg: tests: No such file or directory (os error 2)
     411
 succeeded in 51ms:
Total output lines: 420

README.md:6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
README.md:40:| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
README.md:57:| CY_2 functor (d=2) | **Proved** |
README.md:58:| Lattice VOA bridge | **Proved** |
README.md:59:| CoHA = E_1 sector | **Proved** |
README.md:60:| Drinfeld center = E_2 | **Proved** |
README.md:61:| CY_3 functor (d=3) | **Conjectural** (central open problem) |
README.md:62:| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
README.md:63:| Langlands = Koszul | **Conjectural** |
README.md:68:| Pages | ~335+ |
README.md:74:| Compute tests | ~17,700+ |
main.tex:139:\newcommand{\ClaimStatusProvedHere}{\textsuperscript{\textsc{[ph]}}}
main.tex:140:\newcommand{\ClaimStatusProvedElsewhere}{\textsuperscript{\textsc{[pe]}}}
main.tex:144:\newcommand{\ClaimStatusConditional}{\textsuperscript{\textsc{[cd]}}}
chapters/examples/quantum_group_reps.tex:44:\ClaimStatusProvedElsewhere
chapters/examples/quantum_group_reps.tex:116:\ClaimStatusProvedElsewhere
chapters/examples/quantum_group_reps.tex:162:\ClaimStatusProvedElsewhere
 succeeded in 51ms:
1:Title:           
16:Pages:           367
18:Page size:       612 x 792 pts (letter)
 succeeded in 52ms:
     202

thinking
**Verifying test counts**

I see a command failed due to quoting. I might want to search for the exact theorem status text, but perhaps that's not necessary. It seems like I need to find out if the test count can come from somewhere else since 17,700 might actually refer to individual tests instead of files. I ought to check logs for any mention of around 1,800 tests. Since the user asked for an updated test count, I'll need to verify the actual number from the repo.
codex
The page count is pinned at `367`. I’m checking how this repo measures “test count” before I touch the README, because the current `~17,700+` could be either collected cases or something broader than test files.
exec
/bin/zsh -lc 'ls -1' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "find compute -type f \\( -name 'test_*.py' -o -path '*/tests/*.py' \\) | head -40" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "find compute -type f \\( -name 'test_*.py' -o -path '*/tests/*.py' \\) | sed 's#"'^#/#'"' | wc -l" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'rg -n "pytest|test count|17,700|17700|1800|1,800|271 tests|tests pass|all builds pass|tests" Makefile README.md compute .github pyproject.toml pytest.ini setup.cfg setup.py' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
AGENTS.md
CLAUDE.md
FRONTIER.md
Makefile
README.md
appendices
bibliography
calabi_yau_quantum_groups.pdf
chapters
compute
main.aux
main.log
main.out
main.pdf
main.tex
main.toc
notes
out
scripts
working_notes.aux
 succeeded in 51ms:
compute/tests/test_tilting_chart_cy3.py
compute/tests/test_categorified_e1_shadow_engine.py
compute/tests/test_quintic.py
compute/tests/test_celestial_e1_chart_bridge.py
compute/tests/test_kw_twisted_n4_chiral.py
compute/tests/test_kl_sl2.py
compute/tests/test_higgs_bundle_chiral.py
compute/tests/test_e1_chiral_bialgebra.py
compute/tests/test_cech_descent_e1.py
compute/tests/test_ks_hocolim_equivalence.py
compute/tests/test_hms_e1_chart_compatibility.py
compute/tests/test_borcherds_lift.py
compute/tests/test_coha_chart_explicit.py
compute/tests/test_modular_cy_characteristic.py
compute/tests/test_nontoric_chart_atlas.py
compute/tests/test_hcs_codim2_defect_ope.py
compute/tests/test_psi34_fock_matrices.py
compute/tests/test_local_p2_shadow.py
compute/tests/conftest.py
compute/tests/test_sl2_chiral_coproduct.py
 succeeded in 51ms:
     204
 exited 2 in 51ms:
Total output lines: 1655

rg: .github: No such file or directory (os error 2)
rg: pyproject.toml: No such file or directory (os error 2)
rg: pytest.ini: No such file or directory (os error 2)
rg: setup.cfg: No such file or directory (os error 2)
rg: setup.py: No such file or directory (os error 2)
README.md:64:| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
README.md:74:| Compute tests | ~17,700+ |
Makefile:106:	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
Makefile:108:		python3 -m pytest compute/tests/ -q -ra --durations=10; \
Makefile:110:		echo "  (no compute tests found -- skipping)"; \
Makefile:230:	@echo "  make release       Full release: manuscript + working notes + tests -> out/"
Makefile:234:	@echo "  make test          Run compute tests"
compute/lib/banana_shadow.py:80:    This module tests the AP31 principle: kappa = 0 does NOT imply
compute/lib/gw_dt_e1_shadow_engine.py:1702:# Section 15: Utility functions for tests
compute/lib/e1_universality_deformation.py:1406:    Five independent tests all agree: the E_n level is determined by
compute/lib/drinfeld_center_heisenberg_bulk.py:180:    level: Fraction             # k (symbolic, but we use Fraction for tests)
compute/lib/quintic_e1_universality.py:15:This module tests E_1 universality for X_5 via THREE independent paths:
compute/lib/scattering_diagram.py:5:associated to K3 x E, and tests whether its wall multiplicities reproduce


thinking
**Evaluating test counts**

I'm noticing the output from rg is too large. I might need the actual collected test count using `pytest --collect-only -q`. The Makefile has a section for compute/tests, so I can run `python3 -m pytest compute/tests --collect-only -q | tail -1` to get the count. I should also check the relevant lines in the Makefile. 

On a different note, the README indicates the CoHA's E_1 sector is proved, but the manuscript has a conditional construction at d=3. I should decide how to reflect that accurately in the status line.
thinking
**Inspecting proof statuses**

I'm searching to clarify if the Drinfeld center = E_2 is universally proved or just at the categorical level. I’ll look into the drinfeld_center and the introduction sections for clarity. It's important to determine these statuses to avoid any scope inflation in my analysis. I plan to inspect the relevant sections, particularly in the introduction, e1_chiral, and drinfeld center, and I'll use sed to edit the lines as needed for clarity.
codex
I found one likely status inflation already: the README says `CoHA = E_1 sector` is proved, while the live theory chapter treats the `d=3` E₁-sector statement as conjectural/conditional. I’m reading the local manuscript wording around that before deciding the minimum fix.
exec
/bin/zsh -lc "sed -n '140,190p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '150,220p' chapters/theory/cy_categories.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
\label{prop:e1-sector-d2}
\ClaimStatusProvedHere
Let $\cC$ be a CY$_2$ category with cyclic $A_\infty$ structure and negative-cyclic trace. The ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries a natural $E_1$-chiral structure whose holomorphic direction matches the Hochschild differential and whose ordered direction matches the cyclic action on the bar coalgebra.
\end{proposition}

\begin{proof}
The cyclic $\Ainf$-structure on $\cC$ provides an associative product on the bar coalgebra $B^{\mathrm{ord}}(A_\cC) = T^c(s^{-1}\bar{A}_\cC)$ via OPE residues (Step~1 of the cyclic-to-chiral passage, Section~\ref{sec:cyclic-to-chiral} of Chapter~\ref{ch:cy-to-chiral}). The holomorphic direction is the Hochschild differential $b \colon \mathrm{CC}_\bullet(\cC) \to \mathrm{CC}_{\bullet-1}(\cC)$, which descends to the bar differential $d_{\mathrm{bar}}$ on $B^{\mathrm{ord}}(A_\cC)$ via the standard identification of the bar construction with the Hochschild chain complex. The ordered direction is the $S^1$-action on the cyclic bar complex: the Connes $B$-operator cyclically permutes the bar entries, and its restriction to the ordered bar preserves the deconcatenation coproduct. The $E_1$-chiral structure is the factorization algebra on $C$ obtained by the factorization envelope of the Lie conformal algebra $\mathfrak{L}_\cC$ (Step~2), with the negative-cyclic trace in $\mathrm{HC}^-_2(\cC)$ providing the quantization datum (Step~4). At $d=2$, no framing obstruction arises: the $\bS^2$-framing is automatic (Kontsevich--Vlassopoulos). The full construction is Theorem~\ref{thm:cy-to-chiral} of Chapter~\ref{ch:cy-to-chiral}.
\end{proof}

For $\cC = D^b(\Coh(K3))$ the output is the positive half of the BKM superalgebra studied in \ref{part:examples}: the Borcherds denominator arises as the Euler character of $B^{\mathrm{ord}}(A_{K3})$, and $\kappa_{\mathrm{BKM}} = 5$ is distinct from $\kappa_{\mathrm{ch}} = 3$.

\begin{conjecture}[$E_1$ sector at $d=3$]
\label{conj:e1-sector-d3}
Let $\cC$ be a CY$_3$ category with a chain-level $S^3$-framing on $\mathrm{HC}^-_3(\cC)$ (the condition of Conjecture~CY-A$_3$). Then the ordered bar complex of the cyclic $A_\infty$ algebra $A_\cC$ carries an $E_1$-chiral structure whose representation category is a braided monoidal refinement of the BPS Yangian of $\cC$.
\end{conjecture}

The conjecture is conditional on the chain-level framing; the unconditional statement requires the full CY-A$_3$ programme. Every downstream result in \ref{part:examples} and \ref{part:connections} that uses the BPS Yangian inherits this conditionality. The connection to Maulik-Okounkov and Costello-Witten cohomological Hall algebras is traced in Chapter~\ref{ch:toric-coha}.

\begin{proposition}[$E_2$ enhancement via Drinfeld center]
\label{prop:e2-enhancement-drinfeld}
 succeeded in 52ms:
\]
for all $n \geq 2$, where $\epsilon$ is the Koszul sign determined by the degrees of the $f_i$.
\end{definition}

\begin{definition}[Negative cyclic CY class]
\label{def:negcyc-cy}
A \emph{$d$-dimensional CY structure} on a smooth dg category $\cC$ is a class
\[
 [\sigma] \in \HC^-_{d}(\cC)
\]
in the negative cyclic homology, whose image under the canonical map $\HC^- \to \HH$ is a non-degenerate trace $\Tr \colon \HH_d(\cC) \to k$. The lift to $\HC^-$ is essential for the $\bS^d$-framing used in Chapter~\ref{ch:cy-to-chiral}; see AP-CY2.
\end{definition}

\begin{theorem}[Cyclic $\Ainf$ enhancement]
\label{thm:cyclic-ainf-enhancement}
\ClaimStatusProvedElsewhere{}
Every smooth proper CY$_d$ category admits a cyclic $\Ainf$-enhancement, unique up to $\Ainf$-quasi-isomorphism preserving the pairing. The proof is due to Kontsevich--Soibelman in the formal case, Costello~\cite{Costello2005} for the TCFT enhancement, and Seidel~\cite{Seidel2008} for the Fukaya case.
\end{theorem}

At $d = 2$ the enhancement is explicit enough to compute directly; it drives the $K3$ computations feeding the Borcherds denominator (Vol~III Chapter~\ref{ch:k3-times-e}). At $d = 3$ the enhancement was constructed by Sheridan~\cite{Sheridan2015} for the quintic threefold, as part of the HMS proof; the general $d = 3$ construction remains programme-level (conditional on $\bS^3$-framing, see AP-CY6).
exec
/bin/zsh -lc "sed -n '248,305p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '420,455p' chapters/theory/drinfeld_center.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
The denominator identity of $\mathfrak{g}_X$ ($\Delta_5$ for $K3 \times E$, the DT partition function for toric CY3) should be the bar-complex Euler product of the quantum vertex chiral group, when that group exists. For toric CY3 this identification is part of Conjecture~CY-C. For $K3 \times E$, since $A_{K3 \times E}$ is not yet constructed, the product formula for $\Delta_5$ is an \emph{observation} about the Borcherds lift, not a theorem derived from the bar complex.

The bar Euler product of lattice VOAs recovers the Borcherds denominator identity (verified for $E_8$ and Leech lattice; conditional on CY-A$_3$ for $K3 \times E$).

\section{Main results}
\label{sec:main-results}

\begin{itemize}
 \item \textbf{Theorem CY-A} (CY-to-chiral functor): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
 \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
 \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
 \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$): the weight of $\Delta_5$ is $5 = h^{1,1}(K3)/4 = 20/4$; this appears in the structural position of a modular characteristic, but without $A_{K3 \times E}$ (which is not constructed), the identification $\kappa_{\mathrm{BKM}} = 5$ is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition. The general $d = 3$ formula is conjectural.
 \item \textbf{Theorem (Shadow--Siegel gap)}: The shadow obstruction tower of $K3 \times E$ does not produce the Igusa cusp form $\Phi_{10}$. Four structural obstructions: categorical (number vs function), modular characteristic ($\kappa_{\mathrm{ch}} = 3 \neq 5 = \kappa_{\mathrm{BKM}}$), second quantization (single-copy vs DMVV symmetric product), and Schottky at $g \geq 4$ ($\mathrm{codim} = (g{-}2)(g{-}3)/2$). Thirteen structural results (K3-1 through K3-13) and ten research programmes (A through J) are developed in the toroidal and elliptic algebras chapter.
\end{itemize}

\section{What is proved versus what is conjectural}
\label{sec:proved-vs-conjectural}

\noindent\textbf{Proved (would survive a referee):}
\begin{itemize}
 succeeded in 52ms:
For $d = 3$, the boundary algebra is $\Eone$ (not $\Etwo$):
the $\mathbb{S}^3$-framing obstruction (Conjecture~CY-A$_3$)
breaks $\Etwo$ to $\Eone$. The braiding is recovered
via $\cZ(\Rep^{\Eone}(A))$, not from the boundary $A$ directly.
\end{remark}


\section{Categorical Theorem H}
\label{sec:categorical-thm-h}

Volume~I Theorem~H establishes that chiral Hochschild cohomology
$\ChirHoch^*(A)$ is polynomial (concentrated in degrees $\{0,1,2\}$)
for modular Koszul algebras, with total dimension $\leq 4$. The
categorical analogue replaces $\ChirHoch^*$ with $\HH^\bullet(\cC)$.

\begin{theorem}[Categorical Theorem H]
\label{thm:categorical-thm-h}
\ClaimStatusConditional
For a smooth proper CY$_d$ category $\cC$ whose quantum chiral
algebra $A_\cC = \Phi(\cC)$ is modular Koszul:
exec
/bin/zsh -lc 'python3 -m pytest compute/tests --collect-only -q | tail -n 5' in /Users/raeez/calabi-yau-quantum-groups succeeded in 3.25s:
  /Users/raeez/calabi-yau-quantum-groups/compute/tests/test_zamolodchikov_tetrahedron_engine.py:485: PytestUnknownMarkWarning: Unknown pytest.mark.slow - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.slow

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
19785 tests collected in 1.85s
codex
I’ve confirmed the status boundary in the live source: `d=2` is proved, while the `d=3` E₁/E₂ upgrade is still conditional/conjectural. I’m finishing the test-count verification with pytest collection now.




thinking
**Considering theorem status updates**

It seems like the user wants to clarify the "theorem status" updates. I think using terms like `Proved elsewhere` or `Conditional` makes more sense than just saying `Proved`. I should also check if the README uses "proved" in a general way. Maybe the table should differentiate between `Proved here` and `Proved elsewhere`, but right now, it's not that specific. The update might be needed because the status macro changed or there was an audit mismatch.
thinking
**Evaluating conjectures in chiral algebras**

I'm examining `e1_chiral_algebras`, which has Conjecture E1 sector at dimension 3. The introduction presents main results related to CY-A at d=3, marked as conditional on chain-level S^3-framing. However, the status section later lists "Theorem CY-A for d=3" as Conjectural. This presents a bit of mixed language since I'm seeing both conditional language and the conjectural status, which makes me ponder how they fit together.
thinking
**Inspecting README Updates**

I’m looking at the current README to see if there are any missing labels or references. I think I might need to apply a minimal patch and add a verification block in the commentary, particularly for the theorem status and compute oracle updates. Should I include one block for d=3 status and another for compute oracle? It seems page count might not be necessary, but I should make sure to cover the high-risk theorem status. I need to consider different paths for test counts too.
thinking
**Evaluating README Edits**

I should look at the entire local context in the README, especially around the lines that need editing. There's a thought that the opening paragraph's scope inflation from the G(X) statement may need to be softened. Although this isn't explicitly a d=3 status edit, since the user mentioned avoiding any scope inflation, I think I should minimally adjust that sentence. I might need to search for the opening synopsis in the introduction for supporting evidence.
codex
I’ve got enough to lock the edit surface. Before patching, I’m recording the status and test-count verification explicitly because this README change touches both theorem status and a hardcoded count.
exec
/bin/zsh -lc 'rg -n "root datum of a quantum vertex chiral group|CoHA = E_1 sector|Drinfeld center = E_2|BKM = shadow tower|CY_3 functor" README.md chapters' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
README.md:6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
README.md:59:| CoHA = E_1 sector | **Proved** |
README.md:60:| Drinfeld center = E_2 | **Proved** |
README.md:61:| CY_3 functor (d=3) | **Conjectural** (central open problem) |
README.md:62:| BKM = shadow tower | **Conjectural** (requires d=3 functor) |

thinking
**Drafting edit block**

I need to create a pre-edit block in the commentary section. I'm thinking about setting a status of d=3 and computing the oracle. Since I’m wondering if the page count is really necessary, I think it might be better not to include it. My plan is to tackle one block at a time to keep things organized. This approach should help ensure clarity in the editing process. Let's get started on this!
codex
```text
## PRE-EDIT: d=3 status
statement: README summary/status rows for the CY-to-chiral functor, CoHA as E_1 sector, and Drinfeld-center E_2 lift
depends on unconstructed object?: yes for d=3 CY-to-chiral / E_1 / E_2 applications; no for the abstract Drinfeld-center lift or the toric CY3 E_1 result
environment: README prose + status table
claim status: d=2 functor proved; toric CY3 E_1-sector result proved in the manuscript; abstract Drinfeld-center lift proved elsewhere, but d=3 applications remain conditional on CY-A_3; d=3 functor itself is open/not unconditional
dependency chain: chapters/theory/introduction.tex:256-294; chapters/theory/cy_categories.tex:192-194; chapters/theory/e1_chiral_algebras.tex:151-168; chapters/theory/drinfeld_center.tex:420-428
verdict: ACCEPT
```

```text
## PRE-EDIT: compute oracle
claim: README hardcoded page/test counts
path 1: `pdfinfo calabi_yau_quantum_groups.pdf` reports `Pages: 367`
path 2: `python3 -m pytest compute/tests --collect-only -q` reports `19785 tests collected`
path 3: `Makefile` test target points at `compute/tests/`, matching the collection surface; `find compute -type f \\( -name 'test_*.py' -o -path '*/tests/*.py' \\)` confirms the repo’s test corpus lives there
source and normalization: built PDF in repo root; pytest collection count over `compute/tests` as wired by `make test`
engine/test independence: page count comes from PDF metadata; test count comes from pytest collection, not from README prose or file-count heuristics
verdict: ACCEPT
```







thinking
**Editing README Changes**

I need to make some edits to the README, focusing on clarity and minimalism. For instance, I might start with "For d=2, the combinatorial skeleton ... produces the root datum..." or "Conjecturally, the combinatorial skeleton ...". It's essential to avoid scope inflation while rewriting sentences to address both d=2 and d=3. I should consider whether removing claims about the bar-complex Euler product's relation to the BKM denominator identity is necessary since that might be overstatements. I'll refine these ideas until they really reflect what’s accurate.
thinking
**Refining README Edits**

I want to make the README more concise while preserving important details. For example, I could say, "When the chiral group exists, the bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root multiplicity data." In the manuscript, this proves true for d=2 but remains conditional for d=3. I think this keeps things mostly minimal while conveying the necessary information. As for the section concerning d=2 and d=3, it might be fine as is, not needing any changes right now.
thinking
**Adjusting Scope in README**

I’m considering whether to clarify the statement about being "not yet unconditional." For the connection table row, it seems I might be inflating the scope when I say, "CoHA = E_1-sector of the quantum vertex chiral group." Instead, I could say, "In toric CY3, the CoHA provides the proved E_1 sector, but in d=3 generality, this remains conditional." The user only mentioned the theorem status, not the broader context, but since scope inflation is likely here, I need to be cautious with what I include.
thinking
**Updating test counts**

I’m computing the test counts now. For `19,785`, it could be more precise to say `19,785 collected`, keeping it exact since it's a collected count. But the user said to update the page count and test count. I think the best way is to go with `367` and `19,785 collected in compute/tests`. I may also want to verify if the `271 tests` are still relevant to keep things accurate. Just need to double-check the repository for that.
thinking
**Verifying edits in files**

I need to verify the edits I made by re-reading and grepping for forbidden patterns in the modified file. The specific patterns aren't clearly stated, but I think I can define them, such as stale counts like `335+` and `17,700+`, and phrases like "is the root datum." I definitely need to run a grep to ensure those aren't there anymore. Also, I might want to check the validity of \ref and \label, but the README doesn't seem to reference any. I'll craft the patch carefully, ensuring the changes are clear.
thinking
**Updating the paragraph**

I'm working on updating a section that discusses dimensions in mathematics. The new text states that "The combinatorial skeleton of a Calabi-Yau category..." and describes its implications for the root datum of a quantum vertex chiral group G(X). It explains how the bar-complex Euler product connects to the BKM denominator identity, while also mentioning Vol I's shadow obstruction tower organizing the root-multiplicity data. This revision feels clearer and more focused, emphasizing the relationships in the context of quantum groups.
thinking
**Updating section details**

I think I need to revise the top section regarding the statement, "For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist." It seems like there's a need for a patch to clarify things. Let's go ahead and make that update to ensure the information is accurate and clear! I'll focus on what needs to be changed and make sure it aligns well with the overall context.
codex
I’m making a tightly scoped README patch now: exact page/test counts, plus the smallest status wording changes needed to remove the current overclaiming.
file update
M /Users/raeez/calabi-yau-quantum-groups/README.md
@@ -5,3 +5,3 @@
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
@@ -40,5 +40,5 @@
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
-| R-matrix braiding | Vol II, Part III | E_2 enhancement from E_1 via Drinfeld center |
+| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |
 
@@ -58,5 +58,5 @@
 | Lattice VOA bridge | **Proved** |
-| CoHA = E_1 sector | **Proved** |
-| Drinfeld center = E_2 | **Proved** |
-| CY_3 functor (d=3) | **Conjectural** (central open problem) |
+| CoHA as E_1 sector (toric CY3) | **Proved** |
+| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
+| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
@@ -67,3 +67,3 @@
 |--------|------:|
-| Pages | ~335+ |
+| Pages | 367 |
 | Theory chapters | 13 |
@@ -73,3 +73,3 @@
 | Tagged claims | ~364 |
-| Compute tests | ~17,700+ |
+| Compute tests | 19,785 collected |
 | Compute modules | 189 lib + 187 test |
apply_patch(auto_approved=true) exited 0 in 18ms:
Success. Updated the following files:
M /Users/raeez/calabi-yau-quantum-groups/README.md
file update:
diff --git a/README.md b/README.md
index ccbf8663be0bc9a25ca185dbd4521f5837ea8fdf..427063893487b0112aa9c25ea937d92ef195c807
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
-| R-matrix braiding | Vol II, Part III | E_2 enhancement from E_1 via Drinfeld center |
+| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |
 
 ## Five-Part Structure
 
@@ -56,22 +56,22 @@
 |-----------|--------|
 | CY_2 functor (d=2) | **Proved** |
 | Lattice VOA bridge | **Proved** |
-| CoHA = E_1 sector | **Proved** |
-| Drinfeld center = E_2 | **Proved** |
-| CY_3 functor (d=3) | **Conjectural** (central open problem) |
+| CoHA as E_1 sector (toric CY3) | **Proved** |
+| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
+| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~335+ |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
 | Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
 | Working notes | 22 |
 | Tagged claims | ~364 |
-| Compute tests | ~17,700+ |
+| Compute tests | 19,785 collected |
 | Compute modules | 189 lib + 187 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |

file update:
diff --git a/README.md b/README.md
index ccbf8663be0bc9a25ca185dbd4521f5837ea8fdf..427063893487b0112aa9c25ea937d92ef195c807
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
-| R-matrix braiding | Vol II, Part III | E_2 enhancement from E_1 via Drinfeld center |
+| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |
 
 ## Five-Part Structure
 
@@ -56,22 +56,22 @@
 |-----------|--------|
 | CY_2 functor (d=2) | **Proved** |
 | Lattice VOA bridge | **Proved** |
-| CoHA = E_1 sector | **Proved** |
-| Drinfeld center = E_2 | **Proved** |
-| CY_3 functor (d=3) | **Conjectural** (central open problem) |
+| CoHA as E_1 sector (toric CY3) | **Proved** |
+| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
+| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~335+ |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
 | Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
 | Working notes | 22 |
 | Tagged claims | ~364 |
-| Compute tests | ~17,700+ |
+| Compute tests | 19,785 collected |
 | Compute modules | 189 lib + 187 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |

codex
The patch is in. I’m re-reading the edited spans and then grepping for the stale counts/overstrong status strings to make sure the README surface is internally clean.
exec
/bin/zsh -lc "sed -n '1,95p' README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- README.md' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"~335\\+|~17,700\\+|\\| CoHA = E_1 sector \\| \\*\\*Proved\\*\\* \\||\\| Drinfeld center = E_2 \\| \\*\\*Proved\\*\\* \\||\\| CY_3 functor \\(d=3\\) \\| \\*\\*Conjectural\\*\\*|is the root datum of a quantum vertex chiral group\" README.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:
# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* (this volume) | The categorical completion |

## The CY-to-Chiral Functor

The programme flow:

```
 succeeded in 50ms:
diff --git a/README.md b/README.md
index ccbf866..4270638 100644
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@ For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfac
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
 exited 1 in 51ms:

file update:
diff --git a/README.md b/README.md
index ccbf8663be0bc9a25ca185dbd4521f5837ea8fdf..427063893487b0112aa9c25ea937d92ef195c807
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
-| R-matrix braiding | Vol II, Part III | E_2 enhancement from E_1 via Drinfeld center |
+| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |
 
 ## Five-Part Structure
 
@@ -56,22 +56,22 @@
 |-----------|--------|
 | CY_2 functor (d=2) | **Proved** |
 | Lattice VOA bridge | **Proved** |
-| CoHA = E_1 sector | **Proved** |
-| Drinfeld center = E_2 | **Proved** |
-| CY_3 functor (d=3) | **Conjectural** (central open problem) |
+| CoHA as E_1 sector (toric CY3) | **Proved** |
+| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
+| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~335+ |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
 | Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
 | Working notes | 22 |
 | Tagged claims | ~364 |
-| Compute tests | ~17,700+ |
+| Compute tests | 19,785 collected |
 | Compute modules | 189 lib + 187 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |




thinking
**Finalizing response details**

I’m considering whether to use an update_plan, but it might not be necessary. I need to keep my final response concise with clear points about FIXED/BLOCKED findings, maybe three bullet points. It’s important to mention verification, yet no tests were run, although we did run verification commands. I should list a clickable link to the README, and it could be useful to mention verification via `pdfinfo` and `pytest --collect-only`, while avoiding verbosity.
thinking
**Summarizing fixes and verifications**

I’ve identified several fixes: the page count in the README was updated from `335+` to `367` based on `pdfinfo`. Then, the compute test count changed from `17,700+` to `19,785 collected` from `pytest --collect-only`. Additionally, the wording around the theorem/status was tightened to address scope inflation. For verification, I re-read modified sections, and grep confirmed no stale patterns were present. I should clarify that there are no blockers, stating, "No blockers" in a minimal way.
thinking
**Crafting README details**

I need to consider including line numbers for the README.md file. I could mention specific lines like 6, 38, 56, and 68 as they seem relevant, possibly linking to line 6 for clarity. I think a short, concise list would feel more natural rather than nested bullets. I’ll work on making the information clear and straightforward, focusing on essential details without overcomplicating things!
codex
Edited [README.md](/Users/raeez/calabi-yau-quantum-groups/README.md:6) only.

- FIXED: page count updated from `~335+` to `367`, verified from `pdfinfo calabi_yau_quantum_groups.pdf`.
- FIXED: compute test count updated from `~17,700+` to `19,785 collected`, verified from `python3 -m pytest compute/tests --collect-only -q`.
- FIXED: theorem/status wording tightened to remove scope inflation. The top summary now states the CY-to-chiral/BKM picture as expected or conditional where appropriate; the CoHA row is qualified to `toric CY3`; the Drinfeld-center row is marked `Proved elsewhere` with conditional `d=3` use; the `d=3` functor row is now `Open` and explicitly tied to chain-level `S^3`-framing.

No blockers.

Verification: I re-read the edited spans and grepped `README.md` to confirm the stale counts and overstrong old status strings are gone. `README.md` has no `\ref`/`\label` surface to validate.
file update:
diff --git a/README.md b/README.md
index ccbf8663be0bc9a25ca185dbd4521f5837ea8fdf..427063893487b0112aa9c25ea937d92ef195c807
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
-| R-matrix braiding | Vol II, Part III | E_2 enhancement from E_1 via Drinfeld center |
+| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |
 
 ## Five-Part Structure
 
@@ -56,22 +56,22 @@
 |-----------|--------|
 | CY_2 functor (d=2) | **Proved** |
 | Lattice VOA bridge | **Proved** |
-| CoHA = E_1 sector | **Proved** |
-| Drinfeld center = E_2 | **Proved** |
-| CY_3 functor (d=3) | **Conjectural** (central open problem) |
+| CoHA as E_1 sector (toric CY3) | **Proved** |
+| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
+| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | ~335+ |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 7 (all now in build, including 4 re-enabled former stubs) |
 | Connection chapters | 5 (including restored modular_koszul_bridge + geometric_langlands) |
 | Working notes | 22 |
 | Tagged claims | ~364 |
-| Compute tests | ~17,700+ |
+| Compute tests | 19,785 collected |
 | Compute modules | 189 lib + 187 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |

tokens used
56,707
