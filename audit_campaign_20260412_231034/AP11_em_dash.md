# AP11_em_dash (235s, gpt-5.4)

[HIGH] `chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:891` — structural comment header uses a Unicode em dash: `% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS`

[HIGH] `chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex:1897` — structural comment banner uses decorative `---`: `%% ---- Complete genus-g formality: convergence + boundary cancellation ----`

[MEDIUM] `chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:115` — prose em dash: `The discrepancy---the fiber of the forgetful functor`

[MEDIUM] `chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:116` — same sentence continues with prose em dash: `$E_2\text{-}\mathsf{Alg}\to E_1\text{-}\mathsf{Alg}$---is`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:391` — prose em dash: `predictions---bigraded dimension, braiding reversal,`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:392` — same sentence continues with prose em dash: `$\kappa_{\mathrm{ch}}$-complementarity---on which the general conjecture`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:588` — prose em dash: `surface phenomenon---the relevant topology is $3$-dimensional---and`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:726` — prose em dash: `\emph{inverted}---its poles on the Humbert surfaces`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:452` — prose em dash, with the same “foundational predictions---…---” pattern recurring in a second Vol III theorem-scope remark: `predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.`

[MEDIUM] `calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1445` — prose em dash: `The interesting structure---distinguishing the Mukai lattice`

[MEDIUM] `calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1446` — same sentence continues with prose em dash: `$U^3 \oplus E_8(-1)^2$ from the Leech lattice $\Lambda_{24}$---emerges`

False positives excluded after context read: table `---` placeholders, pure ruler comments, and the functor-slot notation `(\text{---})`.

## Summary
Instances checked: 90 | Violations found: 11 | Verdict: FAIL


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
session id: 019d83aa-a8b6-7233-a561-0019234da46c
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


MISSION: Sweep for B41: em dashes across all three volumes.

Run: grep -rn '---\|—' chapters/ | head -30

Expected: FORBIDDEN: use colon/semicolon/separate sentence

For EACH hit:
1. Read surrounding context to determine if it's a genuine violation
2. Distinguish false positives from real violations
3. Report file:line and the exact violating text
4. Assess severity (CRITICAL if mathematical, HIGH if structural, MEDIUM if prose)
mcp startup: no servers

thinking
**Evaluating search command options**

I need to run `grep -rn '---\|—' chapters/ | head -30` in each of the three volumes as the user mentioned. However, the command references `chapters/`, which might point to just the current repo. Since the task spans all volumes, I think I’ll need to search in multiple directories: `/chiral-bar-cobar/chapters`, `/chiral-bar-cobar-vol2/chapters`, and `/calabi-yau-quantum-groups/chapters`. I might use `grep -rn -- '---\|—'` to check each volume's chapters separately. I need to ensure I read surrounding context to correctly identify violations.
codex
Using `deep-beilinson-audit` for an adversarial read-only sweep. I’m collecting the em-dash hits across the three `chapters/` trees first, then I’ll read context around each hit and drop any false positives before reporting.
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

codex
I have the audit protocol loaded. Next I’m narrowing the constitutional surface for `B41` specifically, then I’ll sweep the three `chapters/` trees and inspect every returned line in context before assigning severity.
exec
/bin/zsh -lc 'rg -n "B41|em-dash|emdash" chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "B41|em-dash|emdash|AI slop|Wrong Formulas Blacklist" CLAUDE.md' in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
170:### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances over 3 zero-tolerance commits
283:## Wrong Formulas Blacklist
353:- B41. Em-dash (`---` or Unicode U+2014). CORRECT: colon, semicolon, separate sentences.
354:- B42. AI slop vocabulary: `notably, crucially, remarkably, interestingly, furthermore, moreover, delve, leverage, tapestry, cornerstone`.
555:**Prose laws**: (1) No AI slop (notably/crucially/remarkably/interestingly/furthermore/moreover/delve/leverage/tapestry/cornerstone). (2) No hedging where math is clear. (3) No em dashes; use colons, semicolons, or separate sentences. (4) No passive voice hedging. (5) Every paragraph forces the next. (6) State once, prove once. (7) Scope always explicit. (8) Comparison with prior work: one sentence per paper.
exec
/bin/zsh -lc "printf 'VOL1\\n'; grep -rn -- '---\\|—' chapters/ | head -30; printf '\\nVOL2\\n'; grep -rn -- '---\\|—' /Users/raeez/chiral-bar-cobar-vol2/chapters/ | head -30; printf '\\nVOL3\\n'; grep -rn -- '---\\|—' /Users/raeez/calabi-yau-quantum-groups/chapters/ | head -30" in /Users/raeez/chiral-bar-cobar exited 1 in 61ms:

 succeeded in 253ms:
chapters/theory/higher_genus_complementarity.tex:1390:Let $\sigma = \mathbb{D} \circ ((\text{---})^!)^{-1}$ be the Verdier--Koszul involution
chapters/theory/higher_genus_complementarity.tex:2916: & $k$ & $-k$ & $0$ & --- & $k = 0$ \\
chapters/theory/higher_genus_complementarity.tex:2918: & $1/4$ & $-1/4$ & $0$ & --- & --- \\
chapters/theory/higher_genus_complementarity.tex:2920: & $r$ & $-r$ & $0$ & $2r$ & --- \\
chapters/theory/higher_genus_complementarity.tex:2924: & $0$ & --- & --- \\[4pt]
chapters/theory/higher_genus_complementarity.tex:2929: & $3(k{+}2)/4$ & $-3(k{+}2)/4$ & $0$ & $6$ & --- \\
chapters/theory/higher_genus_complementarity.tex:2931: & $4(k{+}3)/3$ & $-4(k{+}3)/3$ & $0$ & $16$ & --- \\
chapters/theory/higher_genus_complementarity.tex:2933: & $7(k{+}4)/4$ & $-7(k{+}4)/4$ & $0$ & $28$ & --- \\
chapters/theory/higher_genus_complementarity.tex:2935: & $62(k{+}30)/15$ & $-62(k{+}30)/15$ & $0$ & $496$ & --- \\[4pt]
chapters/theory/ordered_associative_chiral_kd.tex:8432:% ----------------------------------------------------------------
chapters/theory/ordered_associative_chiral_kd.tex:8807:% ----------------------------------------------------------------
chapters/theory/configuration_spaces.tex:4654:Interior $C_n(X)$ & 0 & $(z_1, \ldots, z_n)$ & --- \\
chapters/theory/coderived_models.tex:175:%%% ---------------------------------------------------------------
chapters/theory/coderived_models.tex:177:%%% ---------------------------------------------------------------
chapters/theory/coderived_models.tex:357:%%% ---------------------------------------------------------------
chapters/theory/coderived_models.tex:359:%%% ---------------------------------------------------------------
chapters/theory/introduction.tex:2153:$V_\Lambda$ (lattice) & $\mathrm{rk}(\Lambda)$ & $\mathrm{rk}(\Lambda)$ & $2\mathrm{rk}$ & --- & braided \\[2pt]
chapters/theory/introduction.tex:2154:$Y(\mathfrak{sl}_2)$ & --- & --- & --- & --- & $\Eone$, $R$-matrix
chapters/theory/chiral_koszul_pairs.tex:1131:%%% ---------------------------------------------------------------
chapters/theory/chiral_koszul_pairs.tex:1133:%%% ---------------------------------------------------------------



thinking
**Inspecting context for hits**

I need to closely examine the context surrounding each hit I find. There are numerous occurrences related to comments and table placeholders, so I must distinguish any false positives. As mentioned, B41 forbids em dashes in prose, and the `---` in tables might just be placeholders. The user wants me to sweep for em dashes across all three volumes, focusing on the first 30 hits from each volume to determine genuine violations.
thinking
**Clarifying hit inspection**

Each `head -30` command returns up to 30 hits per volume, so we might have a total of 59 hits collectively—29 from volume 1 and 30 from volume 2. The user wants me to inspect each hit specifically. Since the command limits hits to 30 per volume, I need to classify and check each one. I might implement a script to print out surrounding lines for context, especially since many hits involve comment separators. The user emphasized the importance of reading the actual context around each hit.
thinking
**Counting and parsing hits**

I need to count the exact hits, possibly by parsing the output from earlier or by rerunning the command and saving it to a variable. The command output might cut off due to token limits, so I think a targeted approach would be better. I could use `awk` to parse the results and show the context for each hit. Since the user wants to avoid modifying any files, I could just pipe the results using a `while read` loop instead of writing to a temporary file.
codex
The first pass shows mostly separator comments and table placeholders, plus a smaller set of prose uses with literal em-dash punctuation. I’m reading all returned hits in local context now so the final report only keeps genuine `B41` violations.
exec
/bin/zsh -lc 'for root in /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters; do
  echo "=== ROOT: $root ==="
  grep -rn -- '"'---\\|—' \""'$root" | head -30 | while IFS=: read -r file line rest; do
    start=$((line>2 ? line-2 : 1))
    end=$((line+2))
    echo "FILE:$file:$line"
    sed -n "${start},${end}p" "$file"
    echo "-----"
  done
  echo
 done' in /Users/raeez/chiral-bar-cobar succeeded in 755ms:
-----
FILE:/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2921
 & $1/4$ & $-1/4$ & $0$ & --- & --- \\
$V_\Lambda$ (rank $r$)
 & $r$ & $-r$ & $0$ & $2r$ & --- \\
$\beta\gamma_\lambda$
 & $6\lambda^2{-}6\lambda{+}1$
-----
FILE:/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2925
 & $6\lambda^2{-}6\lambda{+}1$
 & $-(6\lambda^2{-}6\lambda{+}1)$
 & $0$ & --- & --- \\[4pt]
\midrule
\multicolumn{6}{@{}l}{\textit{Affine Kac--Moody:
-----
FILE:/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2930
 $\kappa + \kappa^! = 0$, $K = 2\dim(\fg)$}} \\[2pt]
$\widehat{\mathfrak{sl}}_2$
 & $3(k{+}2)/4$ & $-3(k{+}2)/4$ & $0$ & $6$ & --- \\
$\widehat{\mathfrak{sl}}_3$





thinking
**Clarifying notation rules**

I’m thinking about the notation I’ve come across. It looks like there’s some confusion around using triple hyphens as placeholders in math notation versus prose. While B41 mentions em dashes in prose, it doesn't seem to apply here, making it a false positive. I’ll note that instances of false positives don’t need reporting since they aren’t genuine violations. For example, comments with multiple hyphens in the header are likely not relevant to B41’s prose rules.
thinking
**Evaluating comment formatting**

I’m considering how to address false positives in comments versus prose. In line 891 of pva-descent, there's a Unicode em dash used in a comment header. Since this is part of comment text, it might not apply to prose rules, likely making it a false positive. I need to clarify that if comments contain em dashes, they don’t show in the final document. However, the user still might expect the standard guidance on punctuation in user-facing content.
thinking
**Analyzing comments for violations**

The user wants me to analyze surrounding context for each hit to determine genuine violations and distinguish false positives from real ones. This involves checking if comments genuinely violate policies. While comments don’t affect output, they might still violate source hygiene with low severity. The user is focused on critical or high severity incidents. It seems likely that many comments will be false positives, but clear violations, like specific prose violations, should be addressed with medium severity.
thinking
**Assessing severity of violations**

The user specifies severity levels based on context: CRITICAL for mathematical violations, HIGH for structural, and MEDIUM for prose issues. In reviewing several sections, I see instances like placeholders and clear prose violations, most of which seem to fit into a medium category. For example, the explanations in the "braided_factorization" section are primarily prose with minor style violations. Similarly, other clear prose violations suggest a medium severity. I’ll have to make sure I’m following the user’s guidelines tightly.
thinking
**Considering severity reporting**

The user mentions that prose violations should be rated as medium, but the output contract also includes LOW as a category. I think I can possibly omit LOW for false positives unless there are genuine issues that need reporting. To make sure I'm thorough, I’ll need to inspect all the exact violating texts and their line numbers. That way, I can classify everything accurately and ensure no genuine violations are skipped.
codex
The candidate set has narrowed to a handful of true prose sentences; the rest are table `N/A` placeholders, functor-slot notation, or comment rulers. I’m re-reading just the surviving candidates with numbered lines now so the final citations and quoted text are exact.
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex | sed -n '387,395p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex | sed -n '111,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex | sed -n '448,454p'; printf '\\n'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex | sed -n '1442,1448p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex | sed -n '584,591p'; printf '\\n'; nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex | sed -n '722,729p'" in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
   111	\item \textbf{$E_1$-compatibility, $E_2$-incompatibility.}
   112	  The map~$\rho$ is an $E_1$-algebra map but \emph{not}
   113	  an $E_2$-algebra map: the target carries only an
   114	  $E_1$-structure.
   115	  The discrepancy---the fiber of the forgetful functor
   116	  $E_2\text{-}\mathsf{Alg}\to E_1\text{-}\mathsf{Alg}$---is
   117	  the holomorphic datum that homology discards.
   118	  The higher $E_2$-operations encode the braiding
   119	  (monodromy of two points in $D^\times$ around each
   120	  other), while the $E_1$-structure retains only the
 succeeded in 58ms:
   387	differentials are nonzero and the formality argument does not apply.
   388	For $V_k(\fsl_2)$, the Gerstenhaber bracket is nonzero and $d_Y \neq 0$,
   389	yielding a genuinely two-dimensional bar complex with nontrivial braiding.
   390	Nevertheless, the Heisenberg case confirms the foundational
   391	predictions---bigraded dimension, braiding reversal,
   392	$\kappa_{\mathrm{ch}}$-complementarity---on which the general conjecture
   393	rests.
   394	\end{remark}
   395	
 succeeded in 51ms:
   448	\end{proof}
   449	
   450	\begin{remark}[Scope of the theorem]
   451	\label{rem:e3-koszul-heisenberg-scope}
   452	Theorem~\ref{thm:e3-koszul-heisenberg} proves Conjecture~\ref{conj:e3-koszul-duality} for a single algebra: the Heisenberg $H_k$ (class~$G$). The proof exploits the free-field property ($d_i = 0$), which is specific to $H_k$. For the affine Yangian $Y(\widehat{\fgl}_1)$ at general parameters (class~$L$ or higher), the differentials are nonzero and the formality argument does not apply. The Conjecture remains open for class~$L$, $C$, and~$M$ algebras, where the $E_3$ bar complex has genuinely nontrivial cohomology. Nevertheless, the Heisenberg case confirms the foundational predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.
   453	\end{remark}
   454	

  1442	This agreement is a consequence of rank universality: the
  1443	energy-graded bar Euler product of any rank-$r$ lattice VOA or
  1444	Heisenberg algebra equals $\eta(q)^r/q^{r/24}$.
  1445	The interesting structure---distinguishing the Mukai lattice
  1446	$U^3 \oplus E_8(-1)^2$ from the Leech lattice $\Lambda_{24}$---emerges
  1447	in the \emph{full root-lattice-graded} bar Euler product,
  1448	which records root multiplicities at each lattice vector.
 succeeded in 51ms:
   584	$S_{ij} = \tr_i(\cR_{ij})$ arises by taking the trace over one factor:
   585	it is a \emph{number} (the Hopf link invariant), and when
   586	$\Rep^{E_2}(\cA)$ is a modular tensor category, $S$ governs the
   587	$\SL_2(\Z)$ action on conformal blocks. At $E_3$, the braiding is a
   588	surface phenomenon---the relevant topology is $3$-dimensional---and
   589	the analogue of the $S$-matrix is a \emph{categorical $2$-morphism},
   590	not a scalar. This section formulates the $E_3$ categorical $S$-matrix
   591	and connects it to Siegel modular forms.

   722	  \Phi_{10}(\tau_1, z, \tau_2)^{-1}
   723	  \;\cdot\; (\text{Eisenstein factor}),
   724	 \]
   725	 where $\Phi_{10}^{-1}$ is the Borcherds product
   726	 \emph{inverted}---its poles on the Humbert surfaces
   727	 $\{4n m - \ell^2 = 0\}$ are the \emph{resonances} of the
   728	 categorical scattering matrix, corresponding to BPS bound
   729	 states becoming massless. The Eisenstein factor is a
exec
/bin/zsh -lc 'c1=$(grep -rn -- '"'---\\|—' /Users/raeez/chiral-bar-cobar/chapters | head -30 | wc -l | tr -d ' ')
c2="'$(grep -rn -- '"'---\\|—' /Users/raeez/chiral-bar-cobar-vol2/chapters | head -30 | wc -l | tr -d ' ')
c3="'$(grep -rn -- '"'---\\|—' /Users/raeez/calabi-yau-quantum-groups/chapters | head -30 | wc -l | tr -d ' ')
printf 'vol1=%s\\nvol2=%s\\nvol3=%s\\ntotal=%s\\n' \""'$c1" "$c2" "$c3" "$((c1+c2+c3))"' in /Users/raeez/chiral-bar-cobar succeeded in 204ms:
vol1=30
vol2=30
vol3=30
total=90







thinking
**Clarifying grep hits**

I see that grep hits are line-based, and the user is asking for each hit individually. For example, there are two hits in the same sentence on lines 115 and 116 due to triple-hyphen groups. I could format that output as two separate bullet points, showing the specific text on each line. There are also similar instances in other lines, such as lines 391 and 392 in `e2_chiral_algebras` where there are two hits. I’ll clarify this in the output.
thinking
**Counting grep hits**

I’m trying to tally the total genuine hits reported by grep. It seems I have one hit each from lines 115 and 116 (from "raviolo"), one from lines 391 and 392 (from "e2"), one from line 588 (from "braided"), one from line 726, one from line 452 (from "en"), and two from lines 1445 and 1446 (from "k3"). Totaling these gives me nine lines or hits. I wonder if that count is accurate!
thinking
**Clarifying punctuation guidelines**

I'm considering whether using em dashes across all three volumes is acceptable based on the prompt. It's clear that the expected format forbids using colons, semicolons, or separate sentences. I need to figure out how to ensure I'm following the guidelines while also keeping things clear. So I might need to adjust my approach if em dashes aren’t allowed. I’ll be careful with punctuation to adhere to the requirements!
thinking
**Evaluating findings and false positives**

I’m considering organizing 9 findings into a bullet list along with a summary, which seems manageable. I should verify the count of false positives, possibly totaling 81. If I find that there are 9 genuine lines among those false positives, it might be useful to categorize them by type, but it may not be necessary. I want to ensure there are no false positives among the first 30 in each volume, so I’ll categorize all 90 systematically.
thinking
**Evaluating severity classifications**

I'm considering whether to classify the severity of issues in volume 2 of raviolo as HIGH structural. There's a distinction between the structural differences described and the punctuation violations noted. The user mentioned that severity depends on whether it's mathematical, structural, or prose-related. Since these are prose sentences rather than theorems, I think medium severity fits best. I'd also want to mention false positives and clarify findings before listing bullet points.
thinking
**Identifying false positives**

I'm analyzing the finding that 81 out of 90 returned lines are false positives, which could include things like comment rulers or headers, table placeholders, and functor-slot notation. I’m thinking I might place this information before the summary, while ensuring it doesn’t violate any output contract. The user asked me to check for downstream duplicates in specific lines, suggesting searching exact phrases across volumes. I should also focus on sweeping for B41 as instructed with the command provided.
thinking
**Clarifying audit scope**

I'm noting that the user didn't request a deduplication search beyond what we have done. The completeness contract requires checking for second-order failures and downstream propagation, which I think means clarifying the audit scope. It’s sufficient to mention that we’re focusing on a bounded sweep of the first 30 hits per volume, rather than the entire repository. In the summary, I’m planning to mention that "Checked 90 returned hits (30 per volume)" and consider any relevant downstream propagation concerning duplicated prose strings across multiple files.
codex
I’ve removed the obvious non-violations. One last pass is checking whether the surviving prose uses are duplicated elsewhere, so the report can call out any propagation pattern instead of treating them as isolated typos.
exec
/bin/zsh -lc "rg -n \"\\(\\\\text\\{---\\}\\)|& --- &|"'^%+ .*---|''^%+ .*—" /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | head -80' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "The discrepancy---|The discrepancy—|predictions---|predictions—|surface phenomenon---|surface phenomenon—|inverted---|inverted—|interesting structure---|interesting structure—" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:56:% Regime IV --- Programmatic (Vol~I, Convention~\ref{conv:regime-tags}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1458:%% ---------------------------------------------------------------
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1460:%% ---------------------------------------------------------------
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2648:%% ---------------------------------------------------------------
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2650:%% ---------------------------------------------------------------
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2961:%% ---------------------------------------------------------------
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2963:%% ---------------------------------------------------------------
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3136: & --- & $5$ & M \\
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3338:%% ---------------------------------------------------------------
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3353:%%% --- Programme A: Constructive CY gluing ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3412:%%% --- Programme B: kappa as universal moonshine multiplier ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3475:%%% --- Programme C: Second-quantization bridge ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3548:%%% --- Programme D: Schottky shadow programme ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3632:%%% --- Programme E: Mock modularity and the bar complex ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3722:%%% --- Programme F: Modular factorization envelope ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3780:%%% --- Programme G: BKM algebras and scattering diagrams ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3844:%%% --- Descent foundations ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3899:%%% --- Programme H: Descent theorem programme ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3938:%%% --- Programme I: Higher-dimensional shadows ---
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:3995:%%% --- Programme J: Convergence vs divergence ---
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1445:The interesting structure---distinguishing the Mukai lattice
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:452:Theorem~\ref{thm:e3-koszul-heisenberg} proves Conjecture~\ref{conj:e3-koszul-duality} for a single algebra: the Heisenberg $H_k$ (class~$G$). The proof exploits the free-field property ($d_i = 0$), which is specific to $H_k$. For the affine Yangian $Y(\widehat{\fgl}_1)$ at general parameters (class~$L$ or higher), the differentials are nonzero and the formality argument does not apply. The Conjecture remains open for class~$L$, $C$, and~$M$ algebras, where the $E_3$ bar complex has genuinely nontrivial cohomology. Nevertheless, the Heisenberg case confirms the foundational predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:588:surface phenomenon---the relevant topology is $3$-dimensional---and
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:391:predictions---bigraded dimension, braiding reversal,
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F18_complementarity.md:262:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:452:Theorem~\ref{thm:e3-koszul-heisenberg} proves Conjecture~\ref{conj:e3-koszul-duality} for a single algebra: the Heisenberg $H_k$ (class~$G$). The proof exploits the free-field property ($d_i = 0$), which is specific to $H_k$. For the affine Yangian $Y(\widehat{\fgl}_1)$ at general parameters (class~$L$ or higher), the differentials are nonzero and the formality argument does not apply. The Conjecture remains open for class~$L$, $C$, and~$M$ algebras, where the $E_3$ bar complex has genuinely nontrivial cohomology. Nevertheless, the Heisenberg case confirms the foundational predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F03_kappa_Heis.md:356:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:452:Theorem~\ref{thm:e3-koszul-heisenberg} proves Conjecture~\ref{conj:e3-koszul-duality} for a single algebra: the Heisenberg $H_k$ (class~$G$). The proof exploits the free-field property ($d_i = 0$), which is specific to $H_k$. For the affine Yangian $Y(\widehat{\fgl}_1)$ at general parameters (class~$L$ or higher), the differentials are nonzero and the formality argument does not apply. The Conjecture remains open for class~$L$, $C$, and~$M$ algebras, where the $E_3$ bar complex has genuinely nontrivial cohomology. Nevertheless, the Heisenberg case confirms the foundational predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:115:  The discrepancy---the fiber of the forgetful functor


thinking
**Evaluating false positives**

I’m identifying what those false positives are — they seem to be just a line of dashes, like `% --- Programme... ---`. This isn’t structural in the current context, except for volume 2, 1897, and PVA 891. I’m wondering about the volume 3 comment section headings, like `%% 7.1: Banana manifold`, which are sandwiched by ruler lines and might not count either. There’s no em dash appearing in the text. So, that’s where I stand on this.
thinking
**Verifying placeholder usage**

I'm considering whether placeholders should be marked as `none` or `n/a`, but that's not specified, so I'm thinking we should be cautious. It seems best to report only genuine violations where `---` or `—` is acting as an em dash in the text or headings. This leaves us with 11 instances. I'll also mention any false positives, like `---` in tables or comments. I should verify specific lines 1897 and 891 next.
codex
Two borderline cases remain in source comments rather than compiled prose. I’m checking them explicitly so I can either classify them as structural `B41` violations or exclude them cleanly as separator noise.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex | sed -n '1894,1900p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex | sed -n '888,894p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1894	The resulting formality holds at fixed genus~$g$
  1895	over any field of characteristic zero.
  1896	
  1897	%% ---- Complete genus-g formality: convergence + boundary cancellation ----
  1898	
  1899	\providecommand{\FMg}[1]{\FM_{#1}(\Sigma_g)}
  1900	\providecommand{\omhol}{\omega^{(g)}}
 succeeded in 52ms:
   888	\end{remark}
   889	
   890	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   891	% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS
   892	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


thinking
**Evaluating table formatting**

I see that there's a table cell with `---` listed under the divisor equation for the interior stratum. I wonder if it might make more sense to use `none` instead, since the compiled table shows an em dash. But the user expected a colon or semicolon, which doesn't quite fit. I suspect this might be a false positive for B41 specifically, but it could also be an issue related to the table style itself.
thinking
**Organizing content structure**

I'm thinking about the "source-banner form," which isn't exactly compiled prose. I notice the B41 construction recurs in Volume III in specific sections, mentioning that it might be worthwhile to note that recurrence. For the summary, I might say, "one pattern propagates across two theorem-scope remarks." I'm also noting if 11 violations are found, we should say the verdict is a FAIL. Out of 90 instances checked, it looks like 81 were false positives due to placeholders and comments. I'll make sure to clarify that in the report.
codex
[HIGH] `chiral-bar-cobar-vol2/chapters/theory/pva-descent.tex:891` — structural comment header uses a Unicode em dash: `% SECTION 5 — RAVIOLO RESTRICTION, ČECH/THOM–SULLIVAN MODEL, COINVARIANTS`

[HIGH] `chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex:1897` — structural comment banner uses decorative `---`: `%% ---- Complete genus-g formality: convergence + boundary cancellation ----`

[MEDIUM] `chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:115` — prose em dash: `The discrepancy---the fiber of the forgetful functor`

[MEDIUM] `chiral-bar-cobar-vol2/chapters/theory/raviolo-restriction.tex:116` — same sentence continues with prose em dash: `$E_2\text{-}\mathsf{Alg}\to E_1\text{-}\mathsf{Alg}$---is`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:391` — prose em dash: `predictions---bigraded dimension, braiding reversal,`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:392` — same sentence continues with prose em dash: `$\kappa_{\mathrm{ch}}$-complementarity---on which the general conjecture`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:588` — prose em dash: `surface phenomenon---the relevant topology is $3$-dimensional---and`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:726` — prose em dash: `\emph{inverted}---its poles on the Humbert surfaces`

[MEDIUM] `calabi-yau-quantum-groups/chapters/theory/en_factorization.tex:452` — prose em dash, with the same “foundational predictions---…---” pattern recurring in a second Vol III theorem-scope remark: `predictions---parameter inversion, $\kappa_{\mathrm{ch}}$-complementarity, trigraded structure---on which the general conjecture rests.`

[MEDIUM] `calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1445` — prose em dash: `The interesting structure---distinguishing the Mukai lattice`

[MEDIUM] `calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1446` — same sentence continues with prose em dash: `$U^3 \oplus E_8(-1)^2$ from the Leech lattice $\Lambda_{24}$---emerges`

False positives excluded after context read: table `---` placeholders, pure ruler comments, and the functor-slot notation `(\text{---})`.

## Summary
Instances checked: 90 | Violations found: 11 | Verdict: FAIL
tokens used
34,851
