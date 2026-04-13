# D02_scope_inflation (645s)

- [CRITICAL] [chapters/connections/holographic_datum_master.tex:726](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:726) — PROBLEM: The theorem opens with “for every modular Koszul chiral algebra” all seven faces coincide, but [line 750](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:750) immediately restricts the seventh equality to `\widehat{\fg}_k`, and the proof only imports Face 7 through the affine theorem. FIX: Replace the opening claim by “For every modular Koszul chiral algebra, Faces (F1)–(F4) coincide in the genus-zero two-point sector; for `\cA=\widehat{\fg}_k`, Faces (F5)–(F7) are additionally defined and coincide with the first four.”

- [CRITICAL] [chapters/connections/arithmetic_shadows.tex:4003](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4003) — PROBLEM: `thm:general-nahc` claims a shadow triple for “every chirally Koszul algebra,” but the proof at [4029-4034](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4029) only cites the Virasoro generating-function theorem and then handwaves “analogous finiteness” for standard families. FIX: Rename it to “Standard-landscape shadow triple” and change line 4003 to “For every chirally Koszul algebra `\cA` in the standard landscape with `N` strong generators, ...”.

- [CRITICAL] [chapters/connections/arithmetic_shadows.tex:4735](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4735) — PROBLEM: `thm:general-bps` enlarges the scope to every finitely strongly generated vertex algebra with invariant form, but the proof at [4748-4756](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4748) only works out Virasoro and lattice examples and never proves the shadow tower exists in that larger class. FIX: Rewrite the theorem conditionally: “Assume (a)–(c). Then the shadow coefficients, when defined, determine a formal BPS spectrum...”; delete the sentences claiming this is established for every finitely strongly generated vertex algebra and for admissible/logarithmic/coset/orbifold theories.

- [CRITICAL] [chapters/connections/modular_koszul_bridge.tex:126](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:126) — PROBLEM: Item `(C2^{CY})` states a general CY\(_2\) scalar complementarity law, but [line 130](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130) already concedes the displayed K3 computation is “NOT universal across all CY\(_2\) categories,” and the proof at [137](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:137) only treats K3. FIX: Replace `(C2^{CY})` by a K3-only statement, e.g. “For `\cC=D^b(\Coh(K3))`, `\kappa_{\mathrm{ch}}(\cA_{K3})+\kappa_{\mathrm{ch}}(\cA_{K3}^!)=0`,” and move the general free-field/KM transport claim to a conjecture or remark.

- [HIGH] [chapters/theory/cy_to_chiral.tex:853](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:853) — PROBLEM: `thm:e1-universality-cy3` claims any toric CY\(_3\), but line 853 universalizes from the C\(^3\)-only theorem [thm:c3-hochschild](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:386); the later scope remark at [910-913](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:910) admits the pillars are geometry-specific. FIX: Change [line 837](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:837) to “For `X=\C^3` with `T^3`-equivariant `\Omega`-deformation, the chiral algebra `A_{\C^3}` is natively `\Eone`,” or prove a toric-general `HH^2`/braiding argument before retaining toric-general scope.

- [HIGH] [chapters/connections/arithmetic_shadows.tex:5102](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5102) — PROBLEM: `thm:universality-of-G` says `\log(1+6t/c)` is universal across all single-generator vertex algebras, but the proof at [5118-5123](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5118) proves it only for standard families. FIX: Replace lines 5102-5104 by “universal across the standard-landscape single-generator families treated here at leading order in `1/c`,” or add a proof for arbitrary single-generator vertex algebras.

- [HIGH] [chapters/examples/yangians_foundations.tex:303](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:303) — PROBLEM: `thm:rtt-all-classical-types` advertises a proved-here all-classical result, but the proof computes type \(A\) explicitly at [299-302](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:299) and disposes of types \(B,C,D\) with “the same strategy”; the theorem text itself falls back to low-rank numerics at [274-276](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:274). FIX: Split the theorem: keep type \(A\) as `\ClaimStatusProvedHere`; move \(B,C,D\) to `\ClaimStatusProvedElsewhere` with Molev citations, or insert the full rank-\(n\) YBE expansion for \(B,C,D\) before keeping the current claim.

## Summary
Checked: 18 | Findings: 7 | Verdict: FAIL


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
session id: 019d8418-b5fe-7a41-b445-25f1edbfbc0d
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


MISSION: DEEP ANTI-PATTERN SWEEP.

Find ALL theorems that claim 'for all g' or 'for all families' but whose proofs only cover specific cases. Grep for 'for all', 'every', 'any' in theorem environments. For each: verify the proof matches the scope.

Search ALL three volumes:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding: exact file:line, PROBLEM, and EXACT FIX.
mcp startup: no servers



thinking
**Planning the audit response**

I need to respond to the user asking for a deep audit across three volumes. First, I should follow the AGENTS instructions and use the commentary tool. I'll read the required documents like CLAUDE.md and the other relevant files before making any mathematical edits. However, the user may just want audit findings, not edits. I should check the skill documentation and possibly the explorer tool to help with searching across the volumes. It seems a thorough plan is necessary for this large task.
thinking
**Planning the command execution**

I need to use multi-tool parallel for commands and possibly search with rg since the approval process is restricted. It looks like I can only read files across different roots, especially those like chiral-bar-cobar-vol2 and calabi-yau-quantum-groups outside writable roots. I should ensure I'm within allowed parameters—generally, reading across the filesystem should be fine. I plan to maintain commentary updates every 30 seconds and start by using the deep-beilinson-audit skill to read required documents and grep theorem surfaces effectively. Let's get to inspecting!
thinking
**Initiating file reading**

I think I should open skill files using exec commands like cat, sed, or rg. To efficiently read multiple files, I need to use multi-tool parallel for this. This seems like a logical approach to streamline the process. Also, I plan to start the commentary updates simultaneously, which will help me keep track of everything as I work through the files. Let’s dive in and get this rolling!
codex
I’m treating this as a cross-volume adversarial scope audit. First step is to load the audit workflow and the repo’s live constitutional surfaces, then I’ll grep theorem environments for universal quantifiers and verify proof scope against the actual text.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

codex
I’ve loaded the audit constitution and the red-team baseline. Next I’m building a candidate set from theorem-like environments containing universal quantifiers, then I’ll inspect each proof block to see whether the argument actually covers the advertised scope or silently drops to special cases.
Plan update
Cross-volume universal-scope audit: identify theorem surfaces that advertise all-genera/all-family scope, then verify proof coverage against the live text and record only rechecked findings with exact narrowing fixes.
  → Collect candidate theorem/proposition/lemma/corollary/conjecture environments across all three volumes containing 'for all', 'every', or 'any' in statement text
  • Inspect each candidate in file context, including adjacent status tags and proof blocks, to test whether the proof covers the full advertised scope
  • Dig for second-order failures around each confirmed finding: reused labels, downstream prose, nearby corollaries, or scope tags that inherit the same overclaim
  • Re-verify findings against file contents and deliver severity-ranked audit report with exact file:line references and exact textual fixes

thinking
**Searching theorem environments**

It seems I need to focus on theorem environments that include propositions, lemmas, and corollaries. The user's request is to find all theorems that state "for all g" or "for all families," but only partly proven. I should grep for phrases like "for all," "every," and "any" in these environments. For each theorem, I'll verify that the proof corresponds to the correct scope. I plan to search through three volumes, extracting relevant blocks using Perl. Let's get started!
codex
I’m switching from broad grep to structured extraction so the audit surface is explicit instead of anecdotal. The candidate list will be theorem-like environments whose statement text itself contains universal quantifiers; only after that will I read the corresponding proof blocks.
exec
/bin/zsh -lc "perl -ne '
  BEGIN { @envs = qw(theorem proposition lemma corollary maintheorem conjecture); }
  if ("'!$in) {
    if (/'"\\\\begin\\{((?:theorem|proposition|lemma|corollary|maintheorem|conjecture))\\}/) {
      "'$in=1; $env=$1; $start=$.; $buf=$_; $hit = /'"\\b(?:for all|every|any)\\b/i;
    }
  } else {
    "'$buf .= $_; $hit ||= /'"\\b(?:for all|every|any)\\b/i;
    if (/\\\\end\\{"'$env'"\\}/) {
      if ("'$hit) {
        my ($title) = $buf =~ /'"\\\\begin\\{"'$env'"\\}(?:\\[["'^'"\\]]*\\])?/;
        "'$buf =~ s/'"\\n/ /g;
        "'$buf =~ s/'"\\s+/ /g;
        my "'$snippet = substr($buf,0,260);
        print "$ARGV:$start:$env:$snippet'"\\n\";
      }
      "'$in=0; $env=""; $buf=""; $hit=0;
    }
  }
'"' /Users/raeez/chiral-bar-cobar/chapters/**/*.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/**/*.tex /Users/raeez/calabi-yau-quantum-groups/chapters/**/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 81ms:
depth-definition-recall r_{\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:437962:theorem:\begin{theorem}[$r_{\max}(\mathcal{H}_k) = 2$; \ClaimStatusProvedHere] % label removed: thm:gaussian-rmax-two \index{shadow depth!Heisenberg} For the Heisenberg algebra $\mathcal{H}_k$ at any nonzero level $k \neq 0$, the shadow depth is $r_{\max} = 2$. Every 
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:438105:theorem:\begin{theorem}[$r_{\max}(\widehat{\mathfrak{g}}_k) = 3$; \ClaimStatusProvedHere] % label removed: thm:lie-rmax-three \index{shadow depth!affine Kac--Moody} For the affine Kac--Moody algebra $\widehat{\mathfrak{g}}_k$ at generic level $k$, the shadow depth is 
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:438313:theorem:\begin{theorem}[$r_{\max}(\beta\gamma) = 4$; \ClaimStatusProvedHere] % label removed: thm:contact-rmax-four \index{shadow depth!beta-gamma@$\beta\gamma$} For the $\beta\gamma$ system, the shadow depth is $r_{\max} = 4$. The obstruction classes satisfy: \begin{
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:438476:theorem:\begin{theorem}[$r_{\max}(\mathrm{Vir}_c) = \infty$; \ClaimStatusProvedHere] % label removed: thm:virasoro-rmax-infinity \index{shadow depth!Virasoro} For the Virasoro algebra $\mathrm{Vir}_c$ at generic central charge $c \neq 0, -22/5$, the shadow depth is $r
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:438833:theorem:\begin{theorem}[Polynomial growth of Virasoro jet spaces; \ClaimStatusProvedHere] % label removed: thm:jet-space-polynomial-growth \index{Virasoro algebra!jet space growth rate} For the Virasoro algebra at generic central charge, the extended jet space dimensi
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:439182:proposition:\begin{proposition}[$\Walg_N$ is class~\textbf{M} for $N \geq 2$; \ClaimStatusProvedHere] % label removed: prop:wn-class-m \index{shadow depth!$\Walg_N$} For the principal $\Walg_N$-algebra at generic level, $r_{\max}(\Walg_N) = \infty$ for all $N \geq 2$. The
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_holographic_reconstruction.tex:439244:proposition:\begin{proposition}[Structure of the Postnikov filtration; \ClaimStatusProvedHere] % label removed: prop:postnikov-filtration-structure \index{Postnikov filtration!structural properties} \begin{enumerate}[label=\textup{(\roman*)}] \item \emph{Uniqueness.} The 
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:440903:theorem:\begin{theorem}[$M2$ Koszul dual presentation; \ClaimStatusProvedHere] % label removed: thm:m2-koszul-dual-presentation \index{M2-brane!Koszul dual} The Koszul dual algebra $A^!_{M2} = H^\bullet(\barB(A_{M2,\infty}))^{\vee}$ is generated by dual generators \[ 
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:441101:theorem:\begin{theorem}[Components of $\Theta_{M2}$; \ClaimStatusProvedHere{} except genus-$1$ value, which is \ClaimStatusHeuristic] % label removed: thm:m2-theta-components The MC element $\Theta_{M2}$ decomposes by genus, degree, and planted-forest depth as \begin{
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:442203:proposition:\begin{proposition}[Holonomy obstruction; \ClaimStatusProvedHere] \label{prop:holonomy-obstruction} The locally constructed comparison map \[ \beta_{\der}:\Abulk\longrightarrow\Zder(\Bbound) \] globalizes to a global quasi-isomorphism if the defect holonomy is
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:442409:theorem:\begin{theorem}[Single MC theorem; \ClaimStatusProvedHere] % label removed: thm:single-mc \index{Swiss-cheese!single MC theorem} Let $T$ be an $\SCop$-algebra satisfying \textup{(H1)--(H4)}. The MC element $\alpha_T\in\mc(\gSC_T)$ determines: \begin{enumerate}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex:442722:corollary:\begin{corollary}[Mutual determination; \ClaimStatusProvedHere] % label removed: cor:mutual-determination The five structures \textup{(}boundary algebra, line operators, $R$-matrix, bulk algebra, genus tower\textup{)} are not independent. Any two of them, toge
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:443081:theorem:\begin{theorem}[dg-categorical equivalence; \ClaimStatusProvedHere] % label removed: thm:dg-categorical-equivalence \index{line operators!dg-categorical equivalence|textbf} Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra. The functor $\Phi\colon\cC_{\mathrm{
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:443485:proposition:\begin{proposition}[Virasoro module category; \ClaimStatusProvedHere] % label removed: prop:virasoro-module-category \index{Virasoro algebra!module category} The dg module category $\mathrm{Vir}_{26-c}\text{-}\mathbf{mod}^{\mathrm{dg}}$ has: \begin{itemize} \i
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:443789:proposition:\begin{proposition}[Evaluation modules and the affine/evaluation core; \ClaimStatusProvedHere] % label removed: prop:evaluation-modules-dense \index{evaluation modules!affine core} Let $M$ be an $A_\infty$-module over $\cA^!$. The \emph{evaluation module} $\ma
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:444250:proposition:\begin{proposition}[Prefundamental Clebsch--Gordan; \ClaimStatusProvedElsewhere] % label removed: prop:prefundamental-cg-line-ops \index{prefundamental representation!Clebsch--Gordan|textbf} \textup{(Vol~I, Proposition~\ref*{V1-prop:prefundamental-clebsch-gord
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:444280:corollary:\begin{corollary}[Universal character containment; \ClaimStatusProvedElsewhere] % label removed: cor:universal-character-containment-line-ops \index{Verma module!character containment} \textup{(Vol~I, Corollary~\ref*{V1-cor:universal-character-containment}.)} 
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:444291:corollary:\begin{corollary}[$K_0$-generation; \ClaimStatusProvedElsewhere] % label removed: cor:k0-generation-line-ops \index{K-theory@$K_0$!generation} \textup{(Vol~I, Corollary~\ref*{V1-cor:k0-generation-OY}.)} Every class $[M(\lambda)]\in K_0(\cO^{\mathrm{sh}})$ lies
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_line_operators_extensions.tex:444354:theorem:\begin{theorem}[All-types MC3 on the evaluation-generated core; \ClaimStatusProvedElsewhere] % label removed: conj:mc3-arbitrary-type-line-ops \index{MC3!all simple types|textbf} \textup{(Vol~I, Theorem~\ref*{V1-thm:categorical-cg-all-types}, plus the all-type


thinking
**Refining theorem extraction**

I’m noticing that the extraction output is quite large and may need to be narrowed down. Maybe I should save a better candidate list to a file in /tmp for further processing. The user specifically wants "all theorems that claim 'for all g' or 'for all families'," so it seems I should focus on theorems rather than propositions or corollaries. I’m considering generating a candidate list across all three volumes, focusing on theorem and maintheorem environments only.
thinking
**Clarifying extraction parameters**

I’m considering the directives like "for EVERY finding" and "MISSION: deep anti-pattern sweep." It seems I can include propositions if they're theorem-like, but the user specifically asked for all theorems. To avoid false positives, I should probably focus on theorem environments and only include corollaries if they directly overclaim. I need to extract theorem and maintheorem with quantifiers like "for all g," "every," and "any." I'll create a candidate list file in /tmp and possibly use ripgrep with line numbers for this.
exec
/bin/zsh -lc "perl -ne '
  if ("'!$in) {
    if (/'"\\\\begin\\{((?:theorem|maintheorem))\\}/) {
      "'$in=1; $env=$1; $start=$.; $buf=$_; $hit = /'"\\b(?:for all|every|any)\\b/i;
    }
  } else {
    "'$buf .= $_; $hit ||= /'"\\b(?:for all|every|any)\\b/i;
    if (/\\\\end\\{"'$env'"\\}/) {
      if ("'$hit) {
        (my $snippet = $buf) =~ s/'"\\n/ /g;
        "'$snippet =~ s/'"\\s+/ /g;
        "'$snippet = substr($snippet,0,320);
        print "$ARGV:$start:$env:$snippet'"\\n\";
      }
      "'$in=0; $env=""; $buf=""; $hit=0;
    }
  }
'"' /Users/raeez/chiral-bar-cobar/chapters/**/*.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/**/*.tex /Users/raeez/calabi-yau-quantum-groups/chapters/**/*.tex > /tmp/universal_theorem_candidates.txt
wc -l /tmp/universal_theorem_candidates.txt
sed -n '1,220p' /tmp/universal_theorem_candidates.txt" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 221

     627 /tmp/universal_theorem_candidates.txt
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:1513:theorem:\begin{theorem}[Shadow obstruction tower leading asymptotics] \label{thm:shadow-tower-asymptotics} \ClaimStatusProvedHere For the Virasoro algebra at central charge~$c$, the shadow coefficient $S_r$ in $\operatorname{Sh}_r = S_r\,x^r$ satisfies, for $r \geq 4$: \begin{equation}\label{eq:shadow-leading} S_r = \frac{2}{r
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:1971:theorem:\begin{theorem}[$A_\infty$ formality criterion] \label{thm:ainfty-formality-depth} \label{thm:shadow-sullivan} \ClaimStatusProvedHere On the single-generator primary line of~$\cA$, the bar cohomology $H^*(\barB(\cA))$ carries a transferred $A_\infty$ structure with operations $m_n$. The single-line dichotomy \textup{(}
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2028:theorem:\begin{theorem}[Interacting Gram positivity; \ClaimStatusProvedHere]% \label{thm:interacting-gram-positivity}% Let $\cA$ be chirally Koszul with shadow spectral measure $\rho = \sum_j c_j\,\delta(\lambda_j)$ \textup{(}Theorem~\textup{\ref{thm:shadow-spectral-measure}}\textup{)}. The \emph{interacting sewing weight} \be
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:2082:theorem:\begin{theorem}[\ClaimStatusProvedHere]% \label{thm:shadow-resonance-locus}% \index{shadow resonance locus|textbf}% The shadow resonance locus $\mathcal{R} := \{(c,\alpha) : \det\mathscr{M}^{\mathrm{int}} = 0\}$ is empty for $c > 0$ \textup{(}unitary\textup{)}. For non-unitary $c < 0$ with $|c| < 6$: $\lambda_{\mathrm{
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:3409:theorem:\begin{theorem}[The genus-$1$ amplitude Mellin transform is Eisenstein] \label{thm:shadow-eisenstein} \ClaimStatusProvedHere \index{shadow L-function@shadow $L$-function!Eisenstein decomposition|textbf} \index{Eisenstein series!shadow tower} \index{Rankin--Selberg unfolding!genus-$1$ amplitude} \index{genus-$1$ amplitu
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:3918:theorem:\begin{theorem}[Shadow Higgs field] \label{thm:shadow-higgs-field} \label{thm:nonabelian-hodge} \ClaimStatusProvedHere \index{Higgs field!shadow tower} \index{shadow triple!flat/Higgs/harmonic} \index{Shapovalov form!as harmonic metric} The Virasoro shadow tower carries a \emph{triple} of compatible structures on the d
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:3999:theorem:\begin{theorem}[General shadow triple] \label{thm:general-nahc} \ClaimStatusProvedHere \index{shadow triple!general} For \emph{every} chirally Koszul algebra~$\cA$ with $N$ strong generators, the shadow tower carries a triple of compatible structures $(\Theta_\cA,\, M_\cA,\, h_\cA)$: \textup{(A)}~the MC element $\Theta
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4718:theorem:\begin{theorem}[General BPS spectrum of the shadow obstruction tower] \label{thm:general-bps} \ClaimStatusProvedHere \index{BPS spectrum!general construction} Let $\cA$ be a finitely strongly generated vertex algebra with invariant bilinear form. The shadow tower defines a BPS spectrum $\Omega_r(\cA) := S_r(\cA)$ whose
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5073:theorem:\begin{theorem}[Universality of $G$]% \label{thm:universality-of-G}% \ClaimStatusProvedHere% \index{shadow generating function!universal structure} For any chirally Koszul algebra~$\cA$ with HS-sewing, the connected genus-$1$ free energy admits the factorization \begin{equation}\label{eq:universality-factorization} F_1
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5839:theorem:\begin{theorem}[Hecke-equivariant MC element] \label{thm:spectral-continuation-bridge} \ClaimStatusProvedHere Let $V_\Lambda$ be a lattice VOA of rank~$r$, and let $\Theta_\Lambda = E_{r/2} + \sum_{j=1}^m c_j f_j$ be the Hecke decomposition in $M_{r/2}(\mathrm{SL}(2,\bZ))$. \begin{enumerate}[label=\textup{(\roman*)}] \
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:8731:theorem:\begin{theorem}[Non-lattice Ramanujan bound]% \label{thm:non-lattice-ramanujan}% % backward-compat: removed (promoted to thm:) \ClaimStatusProvedHere% \index{Ramanujan bound!general VOA}% Let $\cA$ be a rational chirally Koszul algebra with HS-sewing and diagonal modular invariant partition function $Z(\tau,\bar\tau) =
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:9312:theorem:\begin{theorem}[Route~C: MC rigidity forces character-level prime-locality; \ClaimStatusProvedHere]% \label{thm:route-c-propagation}% \index{prime-locality!Route C theorem}% \index{MC rigidity!forces prime-locality} Let $\cA$ be a chirally Koszul algebra with HS-sewing and spectral measure~$\rho_\cA$ satisfying the Car
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:9475:theorem:\begin{theorem}[Verdier--Hecke commutation at genus~$1$]% \label{thm:hecke-verdier-commutation}% \ClaimStatusProvedHere% \index{Verdier duality!commutes with Hecke operators}% \index{Hecke operators!commute with Verdier duality}% On the genus-$1$ moduli space~$\cM_{1,1}$, the Verdier duality involution~$\sigma$ induced
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:10487:theorem:\begin{theorem}[Scattering coupling factorization; \ClaimStatusProvedHere]% \label{thm:scattering-coupling-factorization}% \index{scattering coupling!factorization}% The scattering coupling factors into a universal part and an algebra-dependent part: \begin{equation}\label{eq:scattering-factorization} \cE_\rho(\cA) \;=
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:10570:theorem:\begin{theorem}[Structural separation of algebraic and arithmetic content; \ClaimStatusProvedHere]% \label{thm:structural-separation}% \index{structural obstruction!refined form|textbf}% \index{algebraic--analytic divide!structural theorem}% Let $\cA$ range over the class of chirally Koszul algebras with HS-sewing. The
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:10943:theorem:\begin{theorem}[Rigidity inheritance; \ClaimStatusProvedHere]% \label{thm:rigidity-inheritance}% \index{prime-locality!from rigidity inheritance}% \index{Carleman condition!rigidity inheritance}% Let $\cA$ be a chirally Koszul algebra with HS-sewing. Assume: \begin{enumerate}[label=\textup{(\alph*)}] \item The \emph{Ca
/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:11244:theorem:\begin{theorem}[Flatness and divisor independence]% \label{thm:packet-connection-flatness}% \ClaimStatusProvedHere% \index{arithmetic packet connection!flatness}% \begin{enumerate}[label=\textup{(\roman*)}] \item $(\nabla_\cA^{\mathrm{arith}})^2 = 0$. \item The singular divisor is \begin{equation}\label{eq:arithmetic-s


thinking
**Exploring theorem proofs**

I’m thinking about using the theorem registry to address suspicious dependencies, particularly around proof scope mismatches for universality. I could search for candidate theorem statements using “every” or “any” and inspect their proofs. Focusing on high-risk files like connections and genus_complete seems prudent since many universal theorems might be hidden there. I should write a script to extract theorem statements and proofs, narrowing by phrases like "for every" and identifying mentions of family names.
thinking
**Searching universal theorems**

I need to search for universal-scope theorems with proofs mentioning words like "Heisenberg," "Virasoro," "Kac," and "W," since these seem to relate to specific cases. Automating candidate ranking could help streamline this, especially since the user is looking for an exact fix. I'll read contexts more closely, focusing on universal theorem statements and proof lines. Using a script to parse theorems and their corresponding proofs should help identify mentions of explicit families effectively.
codex
The raw quantifier sweep is too broad to be trustworthy by itself. I’m now ranking candidates by a sharper failure signature: universal theorem statements whose proof text collapses into named families or case-by-case citations, which is the exact anti-pattern you asked for.
exec
/bin/zsh -lc "perl -0ne '
  while (/\\\\begin\\{(theorem|maintheorem)\\}(.*?)\\\\end\\{\\1\\}/sg) {
    my "'$stmt=$&; my $pre=$`; my $post=$'"';
    next unless "'$stmt =~ /'"\\b(?:for all|for every|every|for any|any)\\b/i;
    my ("'$startline) = (() = $pre =~ /'"\\n/g); "'$startline++;
    my $proof="";
    if ($post =~ /'"\\A(.*?)\\\\begin\\{proof\\}(.*?)\\\\end\\{proof\\}/sg) {
      "'$proof=$2;
    } elsif ($post =~ /'"\\A(.*?)\\\\begin\\{remark\\}/sg) {
      "'$proof="";
    }
    my $score=0;
    $score += () = $proof =~ /'"\\b(?:Heisenberg|Virasoro|Kac|Moody|W_\\{?\\d|W\\\\_|W-algebra|Yangian|lattice|free field|beta\\\\gamma|affine)\\b/ig;
    next unless "'$score>0;
    (my $one=$stmt)=~s/'"\\n/ /g; "'$one =~ s/'"\\s+/ /g; "'$one=substr($one,0,240);
    (my $pt=$proof)=~s/'"\\n/ /g; "'$pt =~ s/'"\\s+/ /g; "'$pt=substr($pt,0,260);
    print "$ARGV:$startline:score=$score'"\\nSTATEMENT: "'$one'"\\nPROOF: "'$pt'"\\n---\\n\";
  }
' /Users/raeez/chiral-bar-cobar/chapters/**/*.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/**/*.tex /Users/raeez/calabi-yau-quantum-groups/chapters/**/*.tex > /tmp/universal_ranked.txt
wc -l /tmp/universal_ranked.txt
sed -n '1,260p' /tmp/universal_ranked.txt" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:5: parse error near `)'

thinking
**Fixing shell quoting**

I need to address the shell quoting issue, so I'll try using `cat <<'PERL'`. It seems I can utilize a Perl script file through a here-document within the command line. I'll consider whether `cat` is allowed in this context. It might make sense to use `exec_command` with the shell script. Okay, let's go ahead and make those adjustments!
exec
/bin/zsh -lc "cat > /tmp/rank_universal_theorems.pl <<'PERL'
while (<>) {
  "'$text .= $_;
}
while ($text =~ /'"\\\\begin\\{(theorem|maintheorem)\\}(.*?)\\\\end\\{\\1\\}/sg) {
  my "'$stmt = $&;
  my $pre = $`;
  my $post = $'"';
  next unless "'$stmt =~ /'"\\b(?:for all|for every|every|for any|any)\\b/i;
  my "'$startline = 1 + (() = $pre =~ /'"\\n/g);
  my "'$proof = "";
  if ($post =~ /'"\\A(.*?)\\\\begin\\{proof\\}(.*?)\\\\end\\{proof\\}/sg) {
    "'$proof = $2;
  }
  my $score = 0;
  $score += () = $proof =~ /'"\\b(?:Heisenberg|Virasoro|Kac|Moody|W_\\{?\\d|Yangian|lattice|free field|beta\\\\gamma|affine)\\b/ig;
  next unless "'$score > 0;
  (my $one = $stmt) =~ s/'"\\n/ /g;
  "'$one =~ s/'"\\s+/ /g;
  "'$one = substr($one, 0, 240);
  (my $pt = $proof) =~ s/'"\\n/ /g;
  "'$pt =~ s/'"\\s+/ /g;
  "'$pt = substr($pt, 0, 260);
  print "$ARGV:$startline:score=$score'"\\nSTATEMENT: "'$one'"\\nPROOF: "'$pt'"\\n---\\n\";
}
PERL
perl /tmp/rank_universal_theorems.pl /Users/raeez/chiral-bar-cobar/chapters/**/*.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/**/*.tex /Users/raeez/calabi-yau-quantum-groups/chapters/**/*.tex > /tmp/universal_ranked.txt
wc -l /tmp/universal_ranked.txt
sed -n '1,260p' /tmp/universal_ranked.txt" in /Users/raeez/chiral-bar-cobar succeeded in 11.06s:
     700 /tmp/universal_ranked.txt
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:2082:score=1
STATEMENT: \begin{theorem}[\ClaimStatusProvedHere]% \label{thm:shadow-resonance-locus}% \index{shadow resonance locus|textbf}% The shadow resonance locus $\mathcal{R} := \{(c,\alpha) : \det\mathscr{M}^{\mathrm{int}} = 0\}$ is empty for $c > 0$ \textup
PROOF:  $c > 0$: Corollary~\ref{cor:virasoro-interacting-gram}. $c < 0$: $\lambda = |6/c| > 0$. At $N = 1$: $w = a(1)(1 - |6/c|) < 0$ when $|c| < 6$. 
---
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:3999:score=3
STATEMENT: \begin{theorem}[General shadow triple] \label{thm:general-nahc} \ClaimStatusProvedHere \index{shadow triple!general} For \emph{every} chirally Koszul algebra~$\cA$ with $N$ strong generators, the shadow tower carries a triple of compatible 
PROOF:  (A)~is Theorem~\ref{thm:mc2-bar-intrinsic}. (B)~The recursion operator $\mathcal{R}\colon S_r \mapsto S_{r+1}$ has matrix entries built from the OPE structure constants (polynomial in the deformation parameters) and the propagator $P = h^{-1}$. The generating
---
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:4718:score=2
STATEMENT: \begin{theorem}[General BPS spectrum of the shadow obstruction tower] \label{thm:general-bps} \ClaimStatusProvedHere \index{BPS spectrum!general construction} Let $\cA$ be a finitely strongly generated vertex algebra with invariant bilinear
PROOF:  Conditions (a)--(c) hold for any vertex algebra with invariant form. The plethystic logarithm is the formal operation $\operatorname{PLog}(f) = \sum_{k\ge1}\mu(k)\,f(t^k)/k$. For the Virasoro leading-order series $f = -\log(1{+}6t/c)$: $\operatorname{PLog}(f)
---
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:5073:score=1
STATEMENT: \begin{theorem}[Universality of $G$]% \label{thm:universality-of-G}% \ClaimStatusProvedHere% \index{shadow generating function!universal structure} For any chirally Koszul algebra~$\cA$ with HS-sewing, the connected genus-$1$ free energy ad
PROOF:  The factorization~\eqref{eq:universality-factorization} is the composition of the sewing--shadow intertwining (Theorem~\ref{thm:sewing-shadow-intertwining}) and the Stieltjes representation (Theorem~\ref{thm:shadow-spectral-measure}). The separation of algebr
---
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:8731:score=1
STATEMENT: \begin{theorem}[Non-lattice Ramanujan bound]% \label{thm:non-lattice-ramanujan}% % backward-compat: removed (promoted to thm:) \ClaimStatusProvedHere% \index{Ramanujan bound!general VOA}% Let $\cA$ be a rational chirally Koszul algebra with
PROOF:  The proof adds four observations to the twelve-station argument. \smallskip \emph{Observation~$\mathrm{A}$ \textup{(}holomorphy of characters\textup{)}.} Each character $\chi_i(\tau) = q^{h_i-c/24}\sum_n d_n^{(i)}\,q^n$ is holomorphic in~$\tau$ (it is $\opera



thinking
**Analyzing file output issues**

I realize the output is wrong due to the ARGV variable bug, causing file paths to all be read from one file instead of multiple. I'm considering if we need to loop through each file instead, but I'm not entirely sure. We might inspect specific candidates manually to gather actual file references. I'll utilize rg/sed for candidate theorems and focus on identifying likely overclaims and mismatched proofs. Theorem `thm:hdm-seven-way-master` has a mismatch that needs precise corrections.
thinking
**Planning theorem audit strategy**

The user requested an exhaustive list, but I can only provide confirmed findings from my audit. I need to consider checking N universal theorem candidates in high-risk files, but the user wants all three volumes reviewed comprehensively. I might script the process to identify mismatches automatically, followed by manual verification. I plan to adopt a systematic method: first, I'll extract theorems with universal quantifiers like “every” and “any.” Then, I’ll inspect their proofs, focusing on specific phrases related to certain theorem families or genus 0 conditions.
thinking
**Identifying high-risk files**

I’m considering some high-risk files that may pose issues. The `holographic_datum_master.tex` has a master theorem with a universal claim, which only references proof for face 3 genus 0. The `yangians_foundations.tex` explores all types of Yangian structures, but it might be limited to type A vector representations, so inspection is necessary. For `genus_complete.tex`, I suspect its proofs may only apply to standard families. Additionally, `holographic_codes_koszul.tex` claims “every algebra in standard landscape is chirally Koszul,” which may not be proven for all families. Lastly, `w_algebras_deep.tex` could reference Gaiotto-Rapcak regarding general Y-algebras.
codex
I have the first likely overclaim already: the seven-way master theorem advertises every modular Koszul algebra, but its own proof admits Face 3 only at genus 0. I’m now reading the surrounding blocks for the other universal-scope theorems to separate real scope failures from harmless universal phrasing.
exec
/bin/zsh -lc "sed -n '45970,46030p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3990,4065p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '165770,166700p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4710,4775p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '155520,155620p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

exec
/bin/zsh -lc "sed -n '150230,150310p' chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

 succeeded in 50ms:

For \emph{lattice VOAs}: the plethystic logarithm has
$\dim M_{r/2}$ primitives (one per Hecke eigenform), giving
a \emph{multi-particle} BPS spectrum. The shadow depth
$d = 3 + \dim S_k$ counts the number of independent BPS
charges.
\end{remark}

\begin{theorem}[General BPS spectrum of the shadow obstruction tower]
\label{thm:general-bps}
\ClaimStatusProvedHere
\index{BPS spectrum!general construction}
Let $\cA$ be a finitely strongly generated vertex algebra with
invariant bilinear form. The shadow tower defines a BPS spectrum
$\Omega_r(\cA) := S_r(\cA)$ whose plethystic logarithm
$\operatorname{PLog}(\sum \Omega_r t^r) = \sum p_r(\cA)\,t^r$
identifies the primitive BPS states: $p_r \neq 0$ iff the shadow
tower has an independent primitive at charge~$r$. The
construction requires only:
\textup{(a)}~$\Theta_\cA$ exists
 succeeded in 50ms:
$S_r = (2/r)(-3P)^{r-4}\cdot S_4$, which are the Taylor
coefficients of $H(t) = t^2\sqrt{c^2 + 12ct + \alpha t^2}$,
the spectral data of~$M(t)$. The harmonic
metric~$h = P^{-1} = c/2$ converts each recursion step from the
flat ($\Theta$) to the Higgs ($M$) frame. The Koszulness condition
$h > 0$ (i.e., $c > 0$ for unitary theories) ensures the
propagator is well-defined.
\end{proof}

\begin{theorem}[General shadow triple]
\label{thm:general-nahc}
\ClaimStatusProvedHere
\index{shadow triple!general}
For \emph{every} chirally Koszul algebra~$\cA$ with $N$ strong
generators, the shadow tower carries a triple of compatible
structures $(\Theta_\cA,\, M_\cA,\, h_\cA)$:
\textup{(A)}~the MC element $\Theta_\cA$ with
$D_\Theta^2 = 0$ \textup{(}flat side\textup{)};
\textup{(B)}~the shadow Higgs field
$M_\cA(t_1,\dotsc,t_N)$, an $N \times N$ matrix whose spectral
 succeeded in 52ms:

 succeeded in 53ms:


thinking
**Adjusting content retrieval**

I found that running `sed -n '3990,4065p' arithmetic_shadows.tex` returned content, which is great—it means I have access to that earlier part of the file. However, for other files, I might not get any output because they could have fewer lines. I think I'll need to utilize `rg -n "label{thm:...}"` to get those exact lines for the labels. So, using `rg -n` on the target files sounds like the right approach!
codex
The first two arithmetic-shadows theorems are confirmed overclaims: their proofs explicitly fall back to Virasoro or to “all standard families,” while the theorem text says every algebra in a strictly larger class. I’m now resolving exact local line numbers and checking the next universal claims file by file instead of trusting the earlier cumulative offsets.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:general-nahc\\}|\\\\label\\{thm:general-bps\\}|\\\\label\\{thm:hdm-seven-way-master\\}|\\\\label\\{thm:rtt-all-classical-types\\}|\\\\label\\{thm:all-types-yangian-structure\\}|\\\\label\\{thm:mc3-arbitrary-type\\}|\\\\label\\{thm:y-algebra-koszulness\\}' chapters/connections/arithmetic_shadows.tex chapters/connections/holographic_datum_master.tex chapters/examples/yangians_foundations.tex chapters/examples/yangians_computations.tex chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:e1-universality-cy3\\}|\\\\label\\{thm:cy-modular-characteristic\\}|\\\\label\\{thm:face1-cy-bar-cobar\\}|\\\\label\\{thm:face7-cy3-gaudin\\}|\\\\label\\{thm:cy-complementarity-d2\\}' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/*.tex /Users/raeez/calabi-yau-quantum-groups/chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:PVA-descent-roadmap\\}|\\\\label\\{thm:genus-g-formality\\}|\\\\label\\{thm:universal-bulk\\}' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/holographic_datum_master.tex:723:\label{thm:hdm-seven-way-master}
chapters/examples/yangians_computations.tex:3875:\label{thm:mc3-arbitrary-type}% backward compat
chapters/examples/w_algebras_deep.tex:5000:\label{thm:y-algebra-koszulness}
chapters/examples/yangians_foundations.tex:209:\label{thm:rtt-all-classical-types}
chapters/examples/yangians_foundations.tex:1044:\label{thm:all-types-yangian-structure}
chapters/connections/arithmetic_shadows.tex:4000:\label{thm:general-nahc}
chapters/connections/arithmetic_shadows.tex:4719:\label{thm:general-bps}
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex:580:\label{thm:PVA-descent-roadmap}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex:1908:\label{thm:genus-g-formality}
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex:249:\label{thm:universal-bulk}
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:114:\label{thm:cy-complementarity-d2}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:122:\label{thm:face1-cy-bar-cobar}
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:739:\label{thm:face7-cy3-gaudin}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:835:\label{thm:e1-universality-cy3}
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex:17:\label{thm:cy-modular-characteristic}

thinking
**Inspecting candidate proofs**

I need to take a closer look at these candidate proofs. I'm considering using a red-team approach to identify any suspicious dependency clusters and potential scope mismatches. This might help in pinpointing any inconsistencies around the labels. It’s important to examine everything thoroughly to ensure accuracy and clarity. There’s a lot to assess here, so I’ll keep my focus on the details while analyzing the proofs and dependencies closely.
exec
/bin/zsh -lc "sed -n '1038,1115p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '716,770p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '200,270p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '570,650p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/raviolo.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3868,3955p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4992,5075p' chapters/examples/w_algebras_deep.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
 \ar@{<->}[u]^{\textrm{(F5--F7)}}
}
\end{equation}

\begin{theorem}[Seven-way master theorem; \ClaimStatusProvedHere]
\label{thm:hdm-seven-way-master}
\index{seven faces!master theorem|textbf}
\index{collision residue!seven-way master|textbf}
For every modular Koszul chiral algebra $\cA$, the seven faces
$(\mathrm{F}1)$--$(\mathrm{F}7)$ of $r_\cA(z)$ are equal as elements
of $\mathrm{End}_\cA(2)[\![z^{-1}]\!]$ after the standard
normalization. Concretely, the master equation
\begin{equation}\label{eq:hdm-master-equation}
\boxed{\;
r_\cA(z)
\;=\;
\pi_\cA
\;=\;
 succeeded in 52ms:
 general $\Eone$-chiral algebras the complementarity sum
 $\kappa(\cA) + \kappa(\cA^!)$ need not vanish.
\end{enumerate}
\end{conjecture}

\begin{theorem}[All-types Yangian structure; \ClaimStatusProvedHere]%
\label{thm:all-types-yangian-structure}
For every simple Lie algebra~$\fg$ with dual Coxeter number~$h^\vee$ and
fundamental representation~$V_{\omega_i}$:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Collision residue and the classical $r$-matrix.}
 The genus-$0$ binary collision residue of the bar-complex MC
 element~$\Theta_\cA$ for $\cA = \hat{\fg}_k$ produces the
 classical $r$-matrix
 \begin{equation}\label{eq:r-matrix-all-types}
 r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
 = \frac{\Omega}{(k + h^\vee)\,z}
 \;\in\; \fg \otimes \fg(z^{-1}),
 \end{equation}
 where $\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b$ is the
 succeeded in 51ms:
this presentation directly amenable to quadratic Koszul duality
(mechanism~(iii) of Remark~\ref{rem:three-koszul-mechanisms}).
The isomorphism with the Drinfeld presentation
(Definition~\ref{def:yangian}) is given by
$J_a^{(0)} = \sum_{i,j} \rho(e_a)_{ij}\, T_{ij}^{(0)}$
and higher modes from the coproduct structure.
\end{definition}

\begin{theorem}[RTT R-matrices for all classical types; \ClaimStatusProvedHere]
\label{thm:rtt-all-classical-types}
\index{Yangian!RTT!all classical types}
\index{R-matrix!all classical types}
The RTT presentation extends to all classical Lie types
$A_n, B_n, C_n, D_n$ via the collision residue
$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
of the bar-complex MC element. In each case, the $R$-matrix
acts on $V \otimes V$ where $V$ is the fundamental representation,
and the operators $P$, $Q$, $K$ satisfy the identities recorded below.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Type $A_n$ $(\mathfrak{sl}_{n+1}$, $V = \bC^{n+1})$.}
 succeeded in 51ms:
Let $(\cA_{\mathrm{ch}}, \cA_{\mathrm{top}})$ be a logarithmic $\SCchtop$-algebra. Then $\cA_{\mathrm{ch}}$, equipped with operations $m_k$ from integration of weight forms over $\Conf_k(\R) \times \FM_k(\C)$, is an $A_\infty$ chiral algebra. The $A_\infty$ relations follow from Stokes' theorem on $\FM_k(\C)$ with corner cancellation via Arnold--Orlik--Solomon (Theorem~\ref{thm:stokes_arnold}).
\end{theorem}

\begin{proof}
This is a direct consequence of Theorem~\ref{thm:stokes_arnold} (Section~\ref{sec:BV_construction}). That theorem proves that for any family of logarithmic weight forms $\{\omega_k\}$ on $\FM_k(\C)$ satisfying interior closedness, boundary factorisation, and Arnold corner cancellation (all of which hold for a logarithmic $\SCchtop$-algebra by Theorem~\ref{thm:FM-calculus}), the operations $m_k$ defined by integration satisfy the $A_\infty$ identities. The proof proceeds by Stokes' theorem on the FM compactification (Step~1), residue-to-composition identification at codimension-$1$ boundaries (Step~2), Koszul sign verification (Step~3), and codimension-$2$ corner cancellation via Arnold relations (Step~5).
\end{proof}

\subsubsection*{III. PVA descent (Section \ref{sec:PVA_descent})}

\begin{theorem}[PVA descent; \ClaimStatusProvedHere]
\label{thm:PVA-descent-roadmap}
For any logarithmic $\SCchtop$-algebra, $H^\bullet(\cA_{\mathrm{ch}},Q)$ is a $(-1)$-shifted Poisson vertex algebra: the $\lambda$-bracket descends from $m_2$, and $m_{k \geq 3}$ vanish on cohomology via homotopies $h_{k-1}$ from topological contraction of $\Conf_k^{<}(\R)$ (Theorem~\ref{thm:cohomology_PVA}).
\end{theorem}

\begin{proof}
This is Theorem~\ref{thm:cohomology_PVA} (Section~\ref{sec:PVA_descent}), proved in full there. The argument decomposes as: (i)~descent of $\mu$ and $\{-{}_\lambda-\}$ to cohomology via the regular/singular splitting of $m_2$; (ii)~verification of the PVA axioms (sesquilinearity, shifted skew-symmetry, Jacobi, Leibniz) for the descended operations, with the $(-1)$-shift arising from the desuspension in the bar complex; and (iii)~vanishing of $m_{k \ge 3}$ on cohomology (Proposition~\ref{prop:m3_vanish}), using the contractibility of $\Conf_k^{<}(\R)$ to construct explicit nullhomotopies.
\end{proof}

\subsubsection*{IV. Chiral Hochschild and bar--cobar duality (Sections \ref{sec:chiral_hochschild_expanded}--\ref{sec:bar_cobar})}

 succeeded in 51ms:
 No further independent type-$A$ obstruction remains on this
 surface.
\end{enumerate}
\end{proof}

\begin{theorem}[Categorical prefundamental CG decomposition, all types;
 \ClaimStatusProvedHere]
\label{thm:mc3-arbitrary-type}% backward compat
\label{thm:categorical-cg-all-types}%
\index{MC3!arbitrary type CG resolution|textbf}%
\index{prefundamental!categorical Clebsch--Gordan!all types|textbf}%
\index{q-character!multiplicity-free|textbf}%
For any simple Lie algebra~$\mathfrak{g}$ and any fundamental
weight~$\omega_i$, for generic spectral parameters~$a,b$:
\begin{equation}\label{eq:prefundamental-cg-general-type}
 V_{\omega_i}(a) \otimes L^-_{i}(b)
 \;\cong\;
 \bigoplus_{m \in \operatorname{ch}_q(V_{\omega_i}(a))}
 L^-_{i}(\mathrm{shift} = m)
\end{equation}
 succeeded in 51ms:
(of a super affine algebra), a truncation
(of $\mathcal{W}_{1+\infty}$), and a freely strongly
generated vertex algebra (at generic coupling). The
following theorem proves Koszulness by four independent
routes.

\begin{theorem}[Chiral Koszulness of $Y$-algebras;
\ClaimStatusProvedHere]
\label{thm:y-algebra-koszulness}
\index{Y-algebra@$Y$-algebra!Koszulness}
\index{Koszul property!Y-algebra@$Y$-algebra}

For every triple $(N_1, N_2, N_3) \in \bZ_{\geq 0}^3$ and
every $\Psi \in \bC \setminus \Sigma_{N_1,N_2,N_3}$,
the corner vertex algebra $Y_{N_1,N_2,N_3}[\Psi]$ is
chirally Koszul.

The \emph{non-generic locus}
$\Sigma_{N_1,N_2,N_3} \subset \bC$ is at most countable,
contained in the union of:
codex
The Yangian and Vol II surfaces I just checked are not automatic findings. `thm:PVA-descent-roadmap` cleanly defers to a later theorem with matching scope. I’m now checking whether the “general” shadow and Yangian results actually have general dependencies, or whether the proof leans on family-specific theorems masked as universal.
exec
/bin/zsh -lc "sed -n '180,330p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:kac-shapovalov-koszulness\\}|\\\\label\\{thm:virasoro-shadow-generating-function\\}|\\\\label\\{thm:shadow-archetype-classification\\}' chapters/connections/arithmetic_shadows.tex chapters/examples/kac_moody.tex chapters/examples/w_algebras.tex chapters/examples/free_fields.tex chapters/connections/genus_complete.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1115,1215p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3955,4035p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,910p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1888,1975p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(valued in $\mathrm{End}(V)$ for a fundamental representation~$V$,
not in~$\mathfrak{g}$), satisfying the \emph{RTT relation}:\index{RTT relation}
\begin{equation}\label{eq:rtt-relation}
R_{12}(u-v)\, T_1(u)\, T_2(v)
\;=\; T_2(v)\, T_1(u)\, R_{12}(u-v)
\end{equation}
where $R_{12}(u) = 1 - \hbar P_{12}/u + O(u^{-2})$ is the
Yang $R$-matrix, $P_{12}$ is the permutation, and the subscripts
$1, 2$ indicate the tensor factor in
$\mathrm{End}(V) \otimes \mathrm{End}(V) \otimes Y(\mathfrak{g})$.
Expanding in modes
$T_{ij}(u) = \delta_{ij} + \hbar \sum_{r \geq 0} T_{ij}^{(r)} u^{-r-1}$,
the RTT relation \eqref{eq:rtt-relation} is equivalent to:
\begin{equation}\label{eq:rtt-modes}
[T_{ij}^{(r+1)}, T_{kl}^{(s)}]
- [T_{ij}^{(r)}, T_{kl}^{(s+1)}]
\;=\; T_{kj}^{(r)} T_{il}^{(s)}
- T_{kj}^{(s)} T_{il}^{(r)}.
\end{equation}
The RTT relation is \emph{quadratic} in the entries of $T$, making
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:1458:\label{thm:kac-shapovalov-koszulness}
chapters/examples/w_algebras.tex:4951:\label{thm:virasoro-shadow-generating-function}
chapters/theory/higher_genus_modular_koszul.tex:16470:\label{thm:shadow-archetype-classification}
 succeeded in 51ms:
 to the $i$-th simple root.
 \item The evaluation-generated core
 $\mathcal{O}^{\mathrm{eval}}(\fg)$
 of the Yangian category~$\mathcal{O}$ is thick-generated
 by evaluation modules for all simple types. MC3 Layers~1
 and~2 are unconditional for all simple Lie types on the
 evaluation-generated core; Layer~3 (shifted prefundamental
 generation) is unconditional in type~$A$ and conditional on
 Conjecture~\textup{\ref{conj:rank-independence-step2}}
 for other types
 \textup{(}Corollary~\textup{\ref{cor:mc3-all-types}}\textup{)}.

 \end{enumerate}
\end{enumerate}
\end{theorem}

\begin{proof}
The proof assembles four ingredients.

\emph{Step~1: Classical $r$-matrix.}
 succeeded in 51ms:
At generic spectral parameters
\textup{(}avoiding a finite set of values of~$a - b$ where
$A$-factorizations occur\textup{)}, the $\dim(V_{\omega_i})$
highest $\ell$-weights are pairwise non-$A$-linked, hence lie in
pairwise distinct blocks.

\emph{Step~4 (Character accounting forces simplicity).}
The tensor product $V_{\omega_i}(a) \otimes L^-_i(b)$ lies in
$\mathcal{O}^{\mathrm{sh}}$
\textup{(}$V$ is finite-dimensional, $L^-_i$ is
in~$\mathcal{O}^{\mathrm{sh}}$ by~\cite{HJZ25}, and
tensoring with a finite-dimensional module preserves the
category\textup{)}. The block decomposition
in~$\mathcal{O}^{\mathrm{sh}}$ gives a direct sum
$V \otimes L^- = \bigoplus_B (V \otimes L^-)_B$.
By Step~3, the $\dim(V_{\omega_i})$ proposed summands lie in
pairwise distinct blocks $B(m_1), \dotsc, B(m_d)$.
The character identity (Step~1) gives
$\sum_B \operatorname{ch}((V \otimes L^-)_B)
= \sum_j \operatorname{ch}(L^-_i(\mathrm{shift} = m_j))$,
 succeeded in 51ms:
This ratio counts the higher-spin contributions.

\noindent\textit{Verification}: 87 tests in \texttt{c3\_envelope\_comparison.py}; 50 tests in \texttt{macmahon\_shadow\_decomposition.py}.
\end{remark}


% ============================================================
\section{$\Eone$ universality for CY$_3$ chiral algebras}
\label{sec:e1-universality}
% ============================================================

The preceding sections have established the $d = 3$ functor chain and the Drinfeld center passage from $\Eone$ to $\Etwo$. The following theorem shows that the $\Eone$ structure is \emph{universal}: every CY$_3$ chiral algebra with $\Omega$-deformation is natively $\Eone$, not $\Etwo$. The proof has four independent pillars.


\begin{theorem}[$\Eone$ universality for CY$_3$ chiral algebras]
\label{thm:e1-universality-cy3}
\ClaimStatusProvedHere{}
For any toric CY$_3$ category $\cC$ with $T^3$-equivariant $\Omega$-deformation ($\sigma_3 = h_1 h_2 h_3 \neq 0$, subject to $h_1 + h_2 + h_3 = 0$), the chiral algebra $A_\cC = \Phi(\cC)$ is natively $\Eone$. For compact CY$_3$ without a global torus action, the $\Eone$ nature is expected but requires a different argument; see Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.

Concretely: the $\bS^3$-framing obstruction vanishes topologically ($\pi_3(B\Sp(2m)) = 0$), but the chain-level BV trivialization via holomorphic CS is NOT $\Etwo$-equivariant. The $\Etwo$-braided structure is recovered \emph{only} through the Drinfeld center of the $\Eone$-monoidal representation category (Theorem~\textup{\ref{thm:c3-drinfeld-center}}).
 succeeded in 51ms:
is new: the Fay trisecant replaces the algebraic Arnold relation,
and the FM compactification $\FM_k(\Sigma_g)$ of
Sinha~\cite{Sinha2004} replaces $\FM_k(\C)$ of
Fulton--MacPherson~\cite{FM94}. The essential
mechanism (cancellation of boundary terms via the three-term
relation among propagator forms) is identical.
The resulting formality holds at fixed genus~$g$
over any field of characteristic zero.

%% ---- Complete genus-g formality: convergence + boundary cancellation ----

\providecommand{\FMg}[1]{\FM_{#1}(\Sigma_g)}
\providecommand{\omhol}{\omega^{(g)}}
\providecommand{\cU}{\mathcal{U}}
\providecommand{\cS}{\mathcal{S}}
\providecommand{\vol}{\mathrm{vol}}
\providecommand{\PP}{\mathbb{P}}

\begin{theorem}[Operadic formality of $C_\ast(\FMg{k})$;
\ClaimStatusProvedHere]


thinking
**Evaluating classical types proof**

I'm examining the `thm:rtt-all-classical-types` statement. The proof mentions type A explicitly, while types B, C, and D use the same strategy with additional operators Q and K without real computations. I'm questioning if this qualifies as proof for all n, or if it's merely a sketch. The user is looking for a rigorous audit, and I might flag this if it's only citing Molev's RTT presentation. I think I need more precise wording to clarify the proof's limitations.
thinking
**Analyzing Lie types theorem**

I'm considering the theorem that claims to cover all classical Lie types. The proof relies on explicit operator identities and numerical examples for low ranks, but I’m wondering if the operator identities in Step 1 could be general for all ranks. Step 2 doesn't seem fully fleshed out. Regarding `thm:mc3-arbitrary-type`, it states all simple Lie algebras and addresses the multiplicity-free property with various references. Step 4 includes character accounting, which might provide support but isn't entirely clear. I may skip this unless I find stronger evidence.
codex
Vol III already exposed another concrete anti-pattern: `thm:e1-universality-cy3` claims any toric CY3 category, but the theorem’s own follow-up remark says Pillar (a) is specific to `\C^3`. I’m checking whether the remaining pillars actually recover the full toric scope or whether the theorem needs to be narrowed to the explicitly analyzed examples.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:c3-hochschild\\}|\\\\label\\{thm:c3-abelian-bracket\\}|\\\\label\\{thm:c3-drinfeld-center\\}' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '740,835p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '910,980p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/modular_trace.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,320p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/foundations_recast_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '100,180p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
364:\label{thm:c3-abelian-bracket}
387:\label{thm:c3-hochschild}
679:\label{thm:c3-drinfeld-center}
 succeeded in 51ms:

\begin{proposition}[Bar-complex Euler product for $\C^3$]
\label{prop:c3-bar-euler}
\ClaimStatusProvedHere{}
The bar-complex Euler product for $\C^3$ is
\[
 \sum_{k \geq 0} (-1)^k \, \mathrm{ch}(B^k) \;=\; \frac{1}{M(q)} \;=\; \prod_{n \geq 1}(1-q^n)^n.
\]
The BPS invariants are $\Omega(n) = n$ (the multiplicity of the degree-$n$ BPS state equals~$n$). The first bar cohomology at degree~$n$ has $\dim H^1(B)_n = n$.

\noindent\textit{Verification}: 115 tests in \texttt{c3\_grand\_verification.py}; 59 tests in \texttt{bar\_comparison\_c3.py}.
\end{proposition}


\begin{proposition}[Crystal melting = $\Eone$ bar cohomology]
\label{prop:crystal-melting-bar-cohomology}
\ClaimStatusProvedHere{}
Three-dimensional partitions (crystal melting configurations for $\C^3$) are precisely the bar cohomology classes of $Y^+(\widehat{\fgl}_1)$. Explicitly:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item The MacMahon function $M(q) = \prod_{n \geq 1}(1-q^n)^{-n}$ is the bar Euler characteristic of the positive half of the affine Yangian: $M(q) = \sum_{k \geq 0} \mathrm{ch}(H^k(B(Y^+(\widehat{\fgl}_1))))$.
 succeeded in 52ms:
 \item Pillar~(a) \textup{(}abelian classical bracket\textup{)}: specific to $\C^3$. For compact CY$_3$, the global sections of the polyvector sheaf carry nontrivial brackets from the complex structure moduli. Does not categorify.
 \item Pillar~(b) \textup{(}one-dimensional deformation space\textup{)}: specific to toric CY$_3$. Compact CY$_3$ have $\dim \HH^2 = h^{2,1}$, which is multi-dimensional for generic threefolds ($h^{2,1} = 101$ for the quintic). Does not categorify.
 \item Pillar~(c) \textup{(}BV-to-$\Eone$ breaking\textup{)}: partially categorical. The topological vanishing $\pi_3(B\Sp) = 0$ is fully categorical \textup{(}this is Proposition~\textup{\ref{prop:e1-obstruction-categorical}(i)} above\textup{)}. The chain-level BV breaking via the holomorphic volume form $\Omega$ requires geometric input beyond the categorical CY$_3$ structure.
 \item Pillar~(d) \textup{(}$R$-matrix unitarity\textup{)}: specific to toric CY$_3$ with explicit equivariant parameters. The structure function $g(z)$ requires the torus action. Does not categorify in its current form.
\end{itemize}
The categorical content of the four pillars is precisely the $\Etwo$-obstruction of Proposition~\textup{\ref{prop:e1-obstruction-categorical}}: Serre duality forces antisymmetry of the Euler form, which obstructs the promotion. The \emph{construction} of the $\Eone$ structure for non-toric CY$_3$ remains the content of Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.
\end{remark}


% ============================================================
\section{The quiver-chart gluing construction}
\label{sec:quiver-chart-gluing}
% ============================================================

The preceding sections construct the CY$_3$ chiral algebra for $\C^3$ via the five-step chain (Section~\ref{sec:d3-functor-chain}) and establish $\Eone$ universality (Section~\ref{sec:e1-universality}). For a general CY$_3$ $X$, the geometry is not globally toric. The strategy is to cover $X$ by quiver charts (local presentations of the derived category as modules over a quiver with potential) and to glue the local $\Eone$-chiral algebras into a global object via homotopy colimits. Wall-crossing mutations provide the transition data, and the bar-hocolim commutation theorem guarantees that the modular characteristic $\kappa_{\mathrm{ch}}$ is an invariant of the global algebra, independent of the atlas.

\subsection{Quiver chart atlases}
\label{subsec:quiver-chart-atlas}

\begin{definition}[Quiver chart]
 succeeded in 52ms:
%% ===================================================================

\section{CY complementarity}
\label{sec:cy-complementarity-bridge}

Volume~I Theorem~C has two components. The eigenspace statement (C1) asserts that the genus-$g$ shadow complex of a Koszul pair $(A, A^!)$ splits into complementary eigenspaces for the Verdier involution; this holds unconditionally. The scalar statement (C2) asserts the sum
\[
 \kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!) \;=\; \rho \cdot K,
\]
where $K$ is the Koszul conductor and $\rho$ the anomaly ratio; this holds only on the \emph{uniform-weight lane} (all generators of $A$ of equal conformal weight), and at $g \geq 2$ multi-weight algebras incur a nonvanishing cross-channel correction $\delta F_g^{\mathrm{cross}}$. This section transports both statements to CY categories via the functor $\Phi$.

\subsection{The $d = 2$ theorem}

\begin{theorem}[CY complementarity at $d = 2$]
\label{thm:cy-complementarity-d2}
\ClaimStatusProvedHere
Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d = 2$ with Serre duality $\mathbb{S}_\cC \simeq [2]$, and let $A_\cC = \Phi(\cC)$ be its quantum chiral algebra (CY-A at $d = 2$, PROVED). Let $\cC^!$ denote the Koszul dual CY$_2$ category (for $\cC = D^b(\Coh(X))$ with $X$ a K3 surface, $\cC^! \simeq \Fuk(X)$ under homological mirror self-duality). Then:
\begin{enumerate}[label=\textup{(C1$^{\mathrm{CY}}$)}]
 \item \emph{Eigenspace complementarity.} For every genus $g \geq 1$ and every degree $n \geq 1$ with $2g - 2 + n > 0$, the genus-$g$ shadow complex satisfies
 \[
 succeeded in 52ms:
\]
with differential $\delta f := [m, f]$ using the Gerstenhaber
bracket from operadic braces. The brace operations
$f\{g_1, \ldots, g_r\}$ are defined by iterated operadic
insertion with Koszul signs.
\end{definition}

\begin{theorem}[The universal bulk;
 \ClaimStatusProvedHere]
\label{thm:universal-bulk}
\index{derived center!as universal bulk|textbf}
\index{Swiss-cheese theorem!chiral|textbf}
Let $(A, \{m_k\})$ be a curved $A_\infty$-chiral algebra.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Brace dg algebra.} The complex
 $(\cC^\bullet_{\mathrm{ch}}(A, A), \delta, \{-\}\{-,\ldots,-\})$
 is a brace dg algebra: $\delta^2 = 0$ from $[m,m] = 0$, the
 brace operations satisfy the higher pre-Lie identity, and the
 Gerstenhaber bracket $[f,g] = f\{g\} - (-1)^{\|f\|\|g\|} g\{f\}$
 descends to a Gerstenhaber algebra on cohomology.
 succeeded in 52ms:
\chapter{The Modular Trace}
\label{ch:modular-trace}

A chiral algebra carries a modular characteristic $\kappa_{\mathrm{ch}}$; a Calabi--Yau category carries a trace $\Tr \colon \HH_d(\cC) \to k$; a Calabi--Yau manifold carries a topological Euler characteristic $\chi_{\mathrm{top}}$. The tempting identification $\kappa_{\mathrm{ch}} = \chi_{\mathrm{top}}/24$ is \emph{wrong in every computed case}, and wrong in an instructive way.

For the elliptic curve, $\chi_{\mathrm{top}} = 0$ but $\kappa_{\mathrm{ch}}(H_1) = 1$. For $K3$, $\chi_{\mathrm{top}}/24 = 1$ but $\kappa_{\mathrm{ch}}(\cA_{K3}) = 2 = \dim_\C$. For $K3 \times E$, two different modular characteristics appear: $\kappa_{\mathrm{ch}} = 3$ from the chiral de Rham complex and $\kappa_{\mathrm{BKM}} = 5$ from the Borcherds lift weight. For the resolved conifold, $\chi_{\mathrm{top}}/24 = 1/12$ but $\kappa_{\mathrm{ch}} = 1$. The topological invariant is not what the chiral algebra sees.

This chapter replaces the wrong identification by the right one. The CY trace, properly refined to negative cyclic homology $\HC^-_d(\cC)$, determines $\kappa_{\mathrm{ch}}(A_\cC)$ through the CY-to-chiral functor $\Phi$. The resulting equality $\kappa_{\mathrm{ch}}(A_\cC) = \chi^{\CY}(\cC)$ is a statement about the CY Euler characteristic of the category, which in general differs from the topological Euler characteristic of the underlying manifold. The genus-$g$ obstruction tower $\mathrm{obs}_g(A_\cC) = \kappa_{\mathrm{ch}}(A_\cC) \cdot \lambda_g$ then encodes the higher-genus CY invariants on the uniform-weight lane, with the multi-weight cross-channel correction $\delta F_g^{\mathrm{cross}}$ from Vol~I appearing at $g \geq 2$ for families with fields of distinct conformal weights.

\section{CY trace as modular characteristic}
\label{sec:cy-trace-kappa}

%: kappa always subscripted in Vol III.
The CY trace $\Tr \colon \HH_d(\cC) \to k$ determines the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$.

\begin{theorem}[CY modular characteristic: Theorem CY-D]
\label{thm:cy-modular-characteristic}
\ClaimStatusProvedHere
For a CY category $\cC$ of dimension $d = 2$ with quantum chiral algebra $A_\cC = \Phi(\cC)$:
\begin{enumerate}[label=(\roman*)]
codex
I have a third strong scope failure in Vol III: the CY$_2$ complementarity theorem states a general categorical result, but its scalar proof collapses to the K3 example. I’m checking a few more “all families” census-style theorems now, because those are the next most likely places where a table or example list is standing in for an actual universal argument.
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:hc-census\\}|\\\\label\\{thm:ent-landscape-census\\}|\\\\label\\{thm:w-finite-termination\\}|\\\\label\\{thm:bar-cohomology-generating-function-classification\\}|\\\\label\\{thm:cy-complementarity-d2\\}' chapters/connections/holographic_codes_koszul.tex chapters/connections/entanglement_modular_koszul.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '32926,33005p' chapters/connections/entanglement_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '143245,143315p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '114,175p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '45170,45260p' chapters/connections/holographic_codes_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '120750,120830p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:114:\label{thm:cy-complementarity-d2}
chapters/connections/entanglement_modular_koszul.tex:568:\label{thm:ent-landscape-census}
chapters/connections/holographic_codes_koszul.tex:713:\label{thm:hc-census}
 succeeded in 53ms:

 succeeded in 51ms:

 succeeded in 53ms:

 succeeded in 52ms:

 succeeded in 53ms:
\label{thm:cy-complementarity-d2}
\ClaimStatusProvedHere
Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d = 2$ with Serre duality $\mathbb{S}_\cC \simeq [2]$, and let $A_\cC = \Phi(\cC)$ be its quantum chiral algebra (CY-A at $d = 2$, PROVED). Let $\cC^!$ denote the Koszul dual CY$_2$ category (for $\cC = D^b(\Coh(X))$ with $X$ a K3 surface, $\cC^! \simeq \Fuk(X)$ under homological mirror self-duality). Then:
\begin{enumerate}[label=\textup{(C1$^{\mathrm{CY}}$)}]
 \item \emph{Eigenspace complementarity.} For every genus $g \geq 1$ and every degree $n \geq 1$ with $2g - 2 + n > 0$, the genus-$g$ shadow complex satisfies
 \[
 Q_g^n(A_\cC) \;\oplus\; Q_g^n(A_{\cC^!})
 \;\simeq\; H^\bullet\!\bigl(\overline{\cM}_{g,n},\, \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)\bigr),
 \]
 as a direct sum of $\pm 1$ eigenspaces for the Verdier involution induced by Serre duality on $D^b(\Coh(\cC))$. This is unconditional in the CY$_2$ case.
\end{enumerate}
\begin{enumerate}[label=\textup{(C2$^{\mathrm{CY}}$)}]
 \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes),
 \[
 \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}.
 \]
 Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
\end{enumerate}
\end{theorem}


thinking
**Inspecting line numbers**

It looks like the sed commands I used earlier on line 45170 didn’t work because the line numbers were wrong. I need to get the correct lines from the output of rg, specifically around 713 and 568. I'll take a closer look at those local lines to ensure I'm using the right information. This meticulous checking should help me resolve the issue accurately!
exec
/bin/zsh -lc "sed -n '556,620p' chapters/connections/entanglement_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,760p' chapters/connections/holographic_codes_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

% ======================================================================
%
% 5. STANDARD LANDSCAPE CODE CENSUS
%
% ======================================================================

\section{Code census for the standard landscape}
\label{sec:hc-census}
\index{standard landscape!code census|textbf}

\begin{theorem}[Standard landscape code census;
\ClaimStatusProvedHere]
\label{thm:hc-census}
Every algebra in the standard landscape is chirally Koszul, and
therefore admits exact holographic reconstruction. The
code parameters are:

\begin{center}
\renewcommand{\arraystretch}{1.3}
 succeeded in 52ms:
% ======================================================================
%
% 5. ENTANGLEMENT DATA FOR THE STANDARD LANDSCAPE
%
% ======================================================================

\section{Entanglement census for the standard landscape}
\label{sec:ent-standard-landscape}
\index{standard landscape!entanglement census|textbf}

\begin{theorem}[Standard landscape entanglement census;
\ClaimStatusProvedHere]
\label{thm:ent-landscape-census}
\index{entanglement entropy!standard landscape}
For each standard family, the scalar entanglement entropy
coefficient $S_{\EE}^{\mathrm{sc}} / \log(L/\varepsilon)$,
the shadow depth class, and the convergence status are:

\begin{center}
\renewcommand{\arraystretch}{1.3}
exec
/bin/zsh -lc "sed -n '620,680p' chapters/connections/entanglement_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
(Theorem~\ref{thm:shadow-radius}):
all class~G and~L algebras have finite shadow obstruction towers
(automatically convergent); class~M convergence depends
on~$\rho(\cA) < 1$.
The Virasoro sum~\eqref{eq:ent-virasoro-census} is
$c/3 + (26-c)/3 = 26/3$, verified for all~$c$.
Computational verification: 72~tests in
\texttt{compute/tests/test\_entanglement\_shadow\_engine.py}.
\end{proof}

\begin{remark}[Additivity under independent sums]
\label{rem:ent-additivity}
\index{entanglement entropy!additivity}
For independent chiral algebras $\cA = \cA_1 \oplus \cA_2$
with vanishing mixed OPE
(Proposition~\ref{prop:independent-sum-factorization}),
$\kappa(\cA) = \kappa(\cA_1) + \kappa(\cA_2)$
and therefore
$S_{\EE}(\cA) = S_{\EE}(\cA_1) + S_{\EE}(\cA_2)$
at the scalar level. The shadow corrections also

thinking
**Examining theorem classifications**

I'm digging into the `thm:ent-landscape-census`, which references the theorem of modular characteristic and archetype classification, but it doesn't seem to have an obvious mismatch. `Thm:hc-census` also refers to family chapters, which might be acceptable. I need to look more closely at the `quantum_groups_foundations` theorem classification because the line numbers are huge, and there may be scope issues. For instance, the `thm:bar-cohomology generating function classification` seems to state classification while the proof suggests some entries are conjectural. I need to search for the exact theorem and proof.
exec
/bin/zsh -lc "rg -n 'Bar cohomology generating function classification|\\\\label\\{thm:bar-gf-classification\\}|\\\\label\\{thm:bar-cohomology-generating-function-classification\\}' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/*.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

exec
/bin/zsh -lc "rg -n 'Bar cohomology generating function classification|classification framework and all unmarked|Table~\\\\ref\\{tab:bar-gf-classification\\}' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/examples" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:


thinking
**Verifying file paths**

I might be having trouble with the file `quantum_groups_foundations.tex`. I wonder if it doesn't exist or if the earlier output was incorrect due to cumulative errors. Wait, the path I got from the weird output, `chapters/theory/quantum_groups_foundations.tex`, might not even exist. I should probably check and list the files in that directory to verify what's going on. Let’s take a closer look!
exec
/bin/zsh -lc 'ls /Users/raeez/calabi-yau-quantum-groups/chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
braided_factorization.tex
cy_categories.tex
cy_to_chiral.tex
cyclic_ainf.tex
drinfeld_center.tex
e1_chiral_algebras.tex
e2_chiral_algebras.tex
en_factorization.tex
hochschild_calculus.tex
introduction.tex
modular_trace.tex
quantum_chiral_algebras.tex
quantum_groups_foundations.tex
exec
/bin/zsh -lc "rg -n 'Bar cohomology generating function classification|classification framework and all unmarked|bar-gf' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:





thinking
**Exploring proof claims**

I’m considering whether to ignore or systematically check for phrases like "for every," "for any," and "for all" using some search method. We have a few confirmed examples, but I might need at least five or six more. I should search within volumes I and III for explicit proof texts about specific cases. Using patterns might help, especially for theorems related to "for K3" or "for Virasoro." I’m thinking of combining scripted searches or manual targeting to check around known suspicious files, like `arithmetic_shadows.tex`, which has various theorems.
thinking
**Inspecting theorem proofs**

I need to inspect some theorems, like `thm:packet-connection-flatness`, which seems fine. However, `thm:cy-modular-characteristic` at modular_trace has no proof, which is more severe than a scope mismatch. The user specifically requested the theorem/proof scope, and the absence of proof could be considered critical, even if it doesn't apply to specific cases. I also need to check `thm:e1-universality-cy3`; the proof seems partly general but specific for certain pillars. I must clarify whether the toric aspects are intended in the theorem.
thinking
**Evaluating proof examples**

I notice that the proof only checks examples like `C^3`, resolved conifold, local P^2, and quintic in the verification note. However, wait a minute—the quintic isn't actually toric. That's important! I need to consider how this affects the validity of the proof. It seems like the examples should align with the toric context while evaluating their relevance. I'm curious about how this might influence overall conclusions, as it feels like there's more to unpack here.
thinking
**Investigating the proof**

I'm looking into the assertion that "the equivariant deformation space is one-dimensional," which hasn't been proven yet. I need to search for the theorem `c3-hochschild` to understand its relation to C^3. Since pillar b cites it and aims to universalize, I think this proof uses `thm:c3-hochschild`, indicating it's specific to C^3. I should inspect the statement of the theorem for more clarity on this.
exec
/bin/zsh -lc "sed -n '380,420p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\end{proof}


\subsection{Hochschild cohomology and the unique deformation}
\label{subsec:hochschild-unique-deformation}

\begin{theorem}[Hochschild cohomology and unique deformation]
\label{thm:c3-hochschild}
\ClaimStatusProvedHere{}
For $\C^3$:
\begin{enumerate}[label=\textup{(\roman*)}]
 \item $\HH^2(\mathrm{PV}^*(\C^3)) = 1$: the deformation space is one-dimensional, spanned by the $\sigma_3$ direction. The unique deformation is the $\Omega$-deformation.
 \item $\HH^3(\mathrm{PV}^*(\C^3)) = 0$: the Bogomolov--Tian--Todorov theorem guarantees unobstructedness.
 \item The quantized algebra is $\cW_{1+\infty}$ at $c = 1$.
\end{enumerate}

\noindent\textit{Verification}: 71 tests in \texttt{cy3\_hochschild.py}.
\end{theorem}

\begin{proof}


thinking
**Evaluating chiral algebra fixes**

I'm considering the safest fix, stating that for \C^3 with T^3-equivariant Ω-deformation, the chiral algebra A_{\C^3} = \Phi(\C^3) is natively E1. That really narrows things down. I might need to refine the theorem's introductory sentence and specify the toric case. There's potential ambiguity in other findings, like that universal-bulk theorem—could be an overclaim? I need to check the proof section, even though it might be too much.
thinking
**Considering proof scope**

I'm reflecting on whether this could be a finding related to environment mismatch instead of scope. However, the user specifically asks for a proof of the universal claim, focusing only on specific cases. I'm thinking maybe that distinction is important. It seems like understanding the context of the question matters here, but I might need to clarify those claims further to ensure I'm guiding the user correctly.
codex
The Vol III toric theorem is now clearly compromised by a C\^3-only input: `thm:c3-hochschild` proves the one-dimensional deformation space only for `\C^3`, but `thm:e1-universality-cy3` promotes it to every toric CY\_3. I’m verifying the remaining dependencies on the shadow-side theorem so the fix can be scoped precisely rather than hand-wavy.
exec
/bin/zsh -lc "sed -n '1440,1485p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16390,16490p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{thm:shadow-archetype-classification\\}|\\\\label\\{thm:modular-characteristic\\}' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters/connections/entanglement_modular_koszul.tex chapters/connections/holographic_codes_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
item~(1) of
Corollary~\textup{\ref{cor:universal-koszul}}
should be understood as: PBW degeneration holds at all~$k$;
the full Koszulness
\textup{(}diagonal Ext concentration\textup{)}
holds at generic~$k$
but fails at $k = -h^\vee$.
Theorem~H
\textup{(Theorem~\ref{thm:hochschild-polynomial-growth})}
requires the diagonal criterion, so it does not apply at
critical level.
See Remark~\textup{\ref{rem:critical-level-lie-vs-chirhoch}}
for the Beilinson--Drinfeld comparison that replaces
Theorem~H at critical level.
\end{remark}

\begin{theorem}[Kac--Shapovalov criterion for simple quotients;
\ClaimStatusProvedHere]
\label{thm:kac-shapovalov-koszulness}
\index{Koszul property!Kac--Shapovalov criterion}
 succeeded in 51ms:
\label{rem:shadow-depth-k-matrix}
\index{shadow depth!K-matrix}%
\index{Costello--Dimofte!K-matrix}%
In the Costello--Dimofte--Gaiotto framework for $3$d HT
theories~\cite{CDG2024}, line operators carry a modified
coproduct $\Delta_K = K \circ \Delta$, where the K-matrix~$K$
measures the failure of the naive coproduct to intertwine the
$R$-matrix action. The shadow depth~$r_{\max}$ controls the
complexity of~$K$: for class~$\mathbf{G}$ ($r_{\max} = 2$),
$K = \mathrm{id}$ and the coproduct is primitive; for
class~$\mathbf{L}$ ($r_{\max} = 3$), $K$ is a single Lie-bracket
correction; for class~$\mathbf{M}$ ($r_{\max} = \infty$), $K$
receives corrections at every order in the $A_\infty$
tower. The shadow obstruction tower
$\Theta_\cA^{\leq r}$ is the generating function for the
K-matrix corrections at each degree: the quartic resonance
class~$\mathfrak{Q}$ at $r = 4$ is the first correction
to the Yangian coproduct that cannot be removed by gauge
transformation.
\end{remark}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2660:\label{thm:modular-characteristic}
chapters/theory/higher_genus_modular_koszul.tex:16470:\label{thm:shadow-archetype-classification}
exec
/bin/zsh -lc "sed -n '730,790p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20,80p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
seven-face master is the Gaudin model arising from a chiral algebra
with primitive generator (Vol~I,
Theorem~\ref{thm:gaudin-yangian-identification}). In the CY setting, the
Gaudin model arises from CY$_3$ collision residues, with Gaudin
Hamiltonians constructed directly from the toric or elliptic $r$-matrix
of face~5 or face~6, and with the Bethe ansatz interpreted in terms of
DT/PT counts.

\begin{theorem}[Face 7 for $\C^3$: Gaudin from the Jordan-quiver residue]
\label{thm:face7-cy3-gaudin}
\ClaimStatusProvedHere
Let $X = \C^3$. Fix $n$ marked points $z_1, \ldots, z_n$ on the chiral
curve and Fock representations $V_1, \ldots, V_n$ of
$Y(\widehat{\fgl}_1)$. Define
\[
 H_i^{\C^3} \;:=\; \sum_{j \neq i} \frac{k\,\Omega_{ij}^{Y(\widehat{\fgl}_1)}}{z_i - z_j},
\]
acting on $V_1 \otimes \cdots \otimes V_n$, where
$\Omega_{ij}^{Y(\widehat{\fgl}_1)}$ is the Casimir tensor
$\Res_{z=0}\bigl[r_{CY}^{\C^3}(z)\bigr]$ acting on the $i$-th and
 succeeded in 53ms:
\phantomsection\label{def:k-max}%
\phantomsection\label{def:r-max}%

\chapter{The seven faces of $r_{CY}(z)$ for Calabi--Yau chiral algebras}
\label{ch:cy-holographic-datum-master}

\begin{quote}\itshape
For a Calabi--Yau chiral algebra arising from the CY-to-chiral functor,
the binary collision residue
$r_{CY}(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{CY})$
has seven equivalent realizations specific to the CY setting: as the CY
bar-cobar twisting morphism, as a CoHA / perverse-coherent-sheaves shadow,
as the classical CY Poisson coisson, as the Maulik--Okounkov $R$-matrix
(for $K3 \times E$), as the affine super Yangian $Y(\widehat{\fgl}_1)$
$r$-matrix (for toric CY$_3$), as the elliptic Sklyanin bracket
(for toroidal CY), and as a Gaudin model arising from CY$_3$ collision
residues. This chapter establishes the seven-face identification in
the CY setting and shows how Vol~I's general theorems specialize to the
CY$_3$ cases.
\end{quote}

thinking
**Exploring theorems and conjectures**

I'm thinking about the `face7` theorem, which only applies to C^3, and how there's a conjecture for the general case. That's interesting! Then I wonder if there might be a theorem in `cy_holographic_datum_master` related to a general face1. It feels like the theorem statement could be general, but the conjecture might extend to d=3. I should take a closer look and inspect this further!
exec
/bin/zsh -lc "sed -n '110,165p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

\section{Face 1: the CY bar-cobar twisting morphism}
\label{sec:face1-bar-cobar}

The first face is the home framework of this volume. The CY-to-chiral
functor sends a Calabi--Yau category $\cC$ to a chiral algebra $A_\cC$,
and the bar construction sends $A_\cC$ to a factorization coalgebra
$\barB(A_\cC)$ on $\Ran(X)$. The collision residue is the binary
component of the universal twisting morphism between $\barB(A_\cC)$ and
$A_\cC$.

\begin{theorem}[Face 1: CY bar-cobar realization, $d = 2$]
\label{thm:face1-cy-bar-cobar}
\ClaimStatusProvedHere
Let $A_\cC$ be the chiral algebra of a CY$_2$ category $\cC$ produced by
the CY-to-chiral functor $\Phi$ (Theorem~CY-A$_2$). Then:
\begin{enumerate}[label=(\roman*)]
\item The convolution dg Lie algebra $\fg^{\mathrm{mod}}_{A_\cC}$
identifies with the homotopy Lie algebra of twisting morphisms
$\mathrm{hom}_\alpha(\barB(A_\cC), A_\cC)$ between bar coalgebra and


thinking
**Searching for theorems**

I need to find more findings on the universal theorem where proof mentions standard families. I can use a search command to locate relevant theorem proofs. So far, I’ve found four strong candidates: hdm-seven-way-master, general-nahc, general-bps, and cy-complementarity-d2, along with e1-universality-cy3. However, there's a potential finding in Vol III regarding a theorem that lacks a proof. The user specified they want a "deep anti-pattern sweep," so I have to be precise about missing proofs and only include what's relevant to their request.
thinking
**Exploring findings in theorems**

I'm looking into potential findings in various theorem drafts. One possible statement in `foundations_recast_draft.tex` regarding `thm:universal-bulk` discusses local open/closed pairs, but there's no proof yet. I should search for the direct phrase "every ... standard family" and see which references are made. Another interesting potential is in `quantum_groups_foundations.tex`, where `thm:w-finite-termination` matches the specific family statement. I also found mentions in `arithmetic_shadows.tex` with theorems like `thm:general-nahc` and `thm:general-bps`. I'm gathering all this information carefully!
codex
I have enough confirmed scope failures to avoid guessing. I’m doing one last pass over the most likely remaining pattern: universal genus/category statements in Vol III whose proofs reduce to K3, `\C^3`, or another named example. Anything that survives that pass gets dropped rather than padded with speculation.
exec
/bin/zsh -lc "rg -n 'For every genus|for every genus|For every .*category|For any toric CY\\"'$_3'"\\"'$|For every CY|For any CY'"' /Users/raeez/calabi-yau-quantum-groups/chapters/theory /Users/raeez/calabi-yau-quantum-groups/chapters/connections" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:80:Consequently, for every genus $g \geq 1$ and on the uniform-weight lane,
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:118: \item \emph{Eigenspace complementarity.} For every genus $g \geq 1$ and every degree $n \geq 1$ with $2g - 2 + n > 0$, the genus-$g$ shadow complex satisfies
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:138:For every CY category $\cC$ of dimension $d = 2$, the quantum geometric Langlands parameter of the Frenkel--Gaitsgory equivalence applied to $\Phi(\cC)$ coincides, up to the dimensional normalization $\dim(\frakg)/(2 h^\vee)$ in the Kac--Moody case, with the Vol~I chiral shadow parameter $\kappa_{\mathrm{ch}}(\Phi(\cC))$ of the CY $2$-category. Equivalently, the Frenkel--Gaitsgory QGL deformation is the shadow obstruction tower of Vol~I (Volume~I, Theorem~D) evaluated along the critical-level family.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:837:For any toric CY$_3$ category $\cC$ with $T^3$-equivariant $\Omega$-deformation ($\sigma_3 = h_1 h_2 h_3 \neq 0$, subject to $h_1 + h_2 + h_3 = 0$), the chiral algebra $A_\cC = \Phi(\cC)$ is natively $\Eone$. For compact CY$_3$ without a global torus action, the $\Eone$ nature is expected but requires a different argument; see Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.
exec
/bin/zsh -lc "cat > /tmp/find_scope_mismatches.pl <<'PERL'
use strict;
use warnings;
my @files = @ARGV;
for my "'$file (@files) {
  open my $fh, '"'<', "'$file or next;
  my @lines = <$fh>;
  close $fh;
  my $n = @lines;
  my $i = 0;
  while ($i < $n) {
    if ($lines[$i] =~ /'"\\\\begin\\{(theorem|maintheorem)\\}/) {
      my "'$env = $1;
      my $start = $i + 1;
      my $stmt = $lines[$i];
      $i++;
      while ($i < $n && $lines[$i] !~ /'"\\\\end\\{"'$env'"\\}/) {
        "'$stmt .= $lines[$i];
        $i++;
      }
      $stmt .= $lines[$i] if $i < $n;
      my $end_stmt = $i + 1;
      my $norm = $stmt; $norm =~ s/'"\\s+/ /g;
      if ("'$norm =~ /'"\\b(?:for every|for any|every|any|all genera|all families|for all)\\b/i) {
        my "'$j = $i + 1;
        while ($j < $n && $lines[$j] =~ /''^'"\\s*%/) { "'$j++; }
        while ($j < $n && $lines[$j] =~ /''^'"\\s*"'$/) { $j++; }
        my $proof = '"'';
        my "'$proof_start = 0;
        if ($j < $n && $lines[$j] =~ /'"\\\\begin\\{proof/) {
          "'$proof_start = $j + 1;
          $proof .= $lines[$j];
          $j++;
          while ($j < $n && $lines[$j] !~ /'"\\\\end\\{proof\\}/) {
            "'$proof .= $lines[$j];
            $j++;
          }
          $proof .= $lines[$j] if $j < $n;
        }
        my $pn = $proof; $pn =~ s/'"\\s+/ /g;
        if ("'$pn =~ /(genus~'"\\"'$0'"\\"'$ only|standard families|For K3|for K3|For the Virasoro|for the Virasoro|For Virasoro|for Virasoro|for lattice VOAs|For lattice VOAs|For '"\\"'$X = '"\\\\C\\"'^3|For '"\\"'$X = '"\\\\C\\"'^3|type~'"\\"'$A'"\\"'$|type-'"\\"'$A'"\\"'$|type A|conditional on Conjecture|only in type~'"\\"'$A'"\\"'$|this argument applies universally|all standard families|not universal across all|specific to '"\\\\C\\"'^3|specific to toric)/i) {
          print "$file:$start'"\\n\";
          print \"STMT: "'$norm'"\\n\";
          print \"PROOF: "'$pn'"\\n---\\n\";
        }
      }
    }
    "'$i++;
  }
}
PERL
perl /tmp/find_scope_mismatches.pl $(rg --files /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | tr '"'\\n' ' ') > /tmp/scope_candidates.txt
wc -l /tmp/scope_candidates.txt
sed -n '1,260p' /tmp/scope_candidates.txt" in /Users/raeez/chiral-bar-cobar succeeded in 149ms:
     132 /tmp/scope_candidates.txt
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:113
STMT: \begin{theorem}[CY complementarity at $d = 2$] \label{thm:cy-complementarity-d2} \ClaimStatusProvedHere Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d = 2$ with Serre duality $\mathbb{S}_\cC \simeq [2]$, and let $A_\cC = \Phi(\cC)$ be its quantum chiral algebra (CY-A at $d = 2$, PROVED). Let $\cC^!$ denote the Koszul dual CY$_2$ category (for $\cC = D^b(\Coh(X))$ with $X$ a K3 surface, $\cC^! \simeq \Fuk(X)$ under homological mirror self-duality). Then: \begin{enumerate}[label=\textup{(C1$^{\mathrm{CY}}$)}] \item \emph{Eigenspace complementarity.} For every genus $g \geq 1$ and every degree $n \geq 1$ with $2g - 2 + n > 0$, the genus-$g$ shadow complex satisfies \[ Q_g^n(A_\cC) \;\oplus\; Q_g^n(A_{\cC^!}) \;\simeq\; H^\bullet\!\bigl(\overline{\cM}_{g,n},\, \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)\bigr), \] as a direct sum of $\pm 1$ eigenspaces for the Verdier involution induced by Serre duality on $D^b(\Coh(\cC))$. This is unconditional in the CY$_2$ case. \end{enumerate} \begin{enumerate}[label=\textup{(C2$^{\mathrm{CY}}$)}] \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes), \[ \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}. \] Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories). \end{enumerate} \end{theorem} 
PROOF: \begin{proof}[Sketch] (C1$^{\mathrm{CY}}$): the eigenspace decomposition is the $\Phi$-image of Vol~I Theorem~C1. The functor $\Phi$ is compatible with the Verdier involution (Chapter~\ref{ch:cy-to-chiral}, Proposition on Serre-functor intertwining), so the direct sum decomposition of Vol~I pulls back to a decomposition of $Q_g^n(A_\cC) \oplus Q_g^n(A_{\cC^!})$ indexed by Serre eigenvalues. (C2$^{\mathrm{CY}}$): under uniform weight, Vol~I Theorem~C2 gives $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for the Heisenberg/free-field classes. For K3, $\cA_{K3}$ is the $\cN = 4$ superconformal algebra with $c = 6$, and all generators sit at conformal weights $\{1/2, 1, 3/2, 2\}$; the uniform-weight lane of interest is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$, where $\kappa_{\mathrm{ch}} = 2$ is attained. The Verdier involution under the $K3$ Mukai lattice self-duality $\Lambda_{K3} \simeq \Lambda_{K3}^\vee$ acts by a sign on odd-degree Hochschild classes, giving $\kappa_{\mathrm{ch}}' = -2$. The sum vanishes. \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:998
STMT: \begin{theorem}[\texorpdfstring{$\beta\gamma$}{beta-gamma} bar complex rank; \ClaimStatusProvedHere]\label{thm:betagamma-bar-dim} For all $n \geq 1$, $\operatorname{rank}(\bar{B}^n_{\mathrm{geom}}(\beta\gamma)) = 2 \cdot 3^{n-1}$, where the rank counts the number of independent generator-type sectors in the geometric bar complex. \end{theorem} 
PROOF: \begin{proof} We prove by induction on~$n$. \emph{Base cases.} The cases $n = 1, 2, 3$ are verified explicitly in the complete bar complex computation (Theorem~\ref{thm:betagamma-bar-cohomology}, Chapter~\ref{chap:beta-gamma}): $\operatorname{rank}(\bar{B}^1) = 2$ ($\beta$- and $\gamma$-sectors), $\operatorname{rank}(\bar{B}^2) = 6$ ($2^2 = 4$ pure tensor types $+$ $2$ derivative types $V_{\partial\beta}, V_{\partial\gamma}$), $\operatorname{rank}(\bar{B}^3) = 18$ ($2^3 = 8$ pure tensor $+$ $10$ derivative). \emph{Type decomposition.} The geometric bar complex at bar degree~$n$ decomposes by \emph{type assignment}: at each position $i \in \{1, \ldots, n\}$, assign a type $t_i$ from the alphabet $\{\beta, \gamma, \partial\}$, subject to the constraint $t_1 \in \{\beta, \gamma\}$ (no descendant at the root). Here $\partial$ denotes the conformal descendant sector arising from the simple-pole OPE $\beta(z)\gamma(w) \sim 1/(z{-}w)$: the first-order pole contributes exactly one new generator type per non-root position (the residue along each collision divisor $D_{ij}$ in the NBC spanning tree). \emph{Independence.} The type sectors carry distinct quantum numbers under the bigrading by generator parity and leading conformal weight: $\beta$-type has parity~$\beta$ and leading weight~$h_\beta = 1$; $\gamma$-type has parity~$\gamma$ and leading weight~$h_\gamma = 0$; $\partial$-type has parity~$\gamma$ and leading weight~$h_\gamma + 1 = 1 \neq 0$. Since the $\beta$- and $\gamma$-parities are orthogonal, and $\partial$-type is distinguished from $\gamma$-type by weight, the sectors are linearly independent. \emph{Exhaustion.} Every element of $\bar{B}^n_{\mathrm{geom}}$ belongs to a unique type sector, since the PBW basis of the $\beta\gamma$ vertex algebra provides a weight-graded decomposition of $(s^{-1}\bar{A})^{\otimes n}$, and each PBW basis element tensored with an NBC form belongs to a unique type assignment via its parity and weight at each position. \emph{Count.} $|t_1| = 2$ and $|t_i| = 3$ for $i > 1$ gives $\operatorname{rank}(\bar{B}^n) = 2 \cdot 3^{n-1}$. \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:208
STMT: \begin{theorem}[RTT R-matrices for all classical types; \ClaimStatusProvedHere] \label{thm:rtt-all-classical-types} \index{Yangian!RTT!all classical types} \index{R-matrix!all classical types} The RTT presentation extends to all classical Lie types $A_n, B_n, C_n, D_n$ via the collision residue $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ of the bar-complex MC element. In each case, the $R$-matrix acts on $V \otimes V$ where $V$ is the fundamental representation, and the operators $P$, $Q$, $K$ satisfy the identities recorded below. \begin{enumerate}[label=\textup{(\roman*)}] \item \emph{Type $A_n$ $(\mathfrak{sl}_{n+1}$, $V = \bC^{n+1})$.} The Yang $R$-matrix is \begin{equation}\label{eq:rmatrix-type-a} R(u) = u\, \mathbb{1} + P, \end{equation} where $P$ is the permutation operator on $V \otimes V$. The corresponding Casimir is $\Omega = P - \mathbb{1}/N$ with $N = n+1$, so in the KZ normalisation the classical $r$-matrix at affine level $k$ reads $r(z) = \Omega/\bigl((k + h^\vee)\,z\bigr) = (P - \mathbb{1}/N)/\bigl((k + n + 1)\,z\bigr)$ (Remark~\ref{rem:km-collision-residue-rmatrix}). At the critical level $k = -h^\vee$ the denominator vanishes, tracking the Sugawara singularity. \item \emph{Type $B_n$ $(\mathfrak{so}_{2n+1}$, $V = \bC^{2n+1})$.} The $R$-matrix is% \footnote{The pole position of the $R$-matrix in types $B$, $C$, $D$ is denoted~$\varkappa$ (following Molev~\cite{molev-yangians}) to avoid conflation with the modular characteristic~$\kappa(\cA)$ of Theorem~\textup{\ref{thm:modular-characteristic}}; these are unrelated quantities.} \begin{equation}\label{eq:rmatrix-type-b} R(u) = \mathbb{1} - \frac{P}{u} + \frac{Q}{u - \varkappa}, \qquad \varkappa = n - \tfrac{1}{2}, \end{equation} where $Q_{(ij),(kl)} = \delta_{ij}\delta_{kl}$ is the trace projection operator satisfying $Q^2 = (2n{+}1) Q$ and $PQ = QP = Q$. \item \emph{Type $C_n$ $(\mathfrak{sp}_{2n}$, $V = \bC^{2n})$.} The $R$-matrix is \begin{equation}\label{eq:rmatrix-type-c} R(u) = \mathbb{1} - \frac{P}{u} - \frac{K}{u - \varkappa}, \qquad \varkappa = n + 1, \end{equation} where $K_{(ab),(cd)} = -J_{ab}J_{cd}$ is the symplectic contraction, $J = \bigl[\begin{smallmatrix} 0 & I_n \\ -I_n & 0 \end{smallmatrix}\bigr]$ is the symplectic form, and $K$ satisfies $K^2 = -2n\,K$ and $PK = KP = -K$. The minus sign before $K/(u - \varkappa)$ is the symplectic-type sign, distinguishing type~$C$ from types~$B$ and~$D$. \item \emph{Type $D_n$ $(\mathfrak{so}_{2n}$, $V = \bC^{2n}$, $n \geq 3)$.} The $R$-matrix is \begin{equation}\label{eq:rmatrix-type-d} R(u) = \mathbb{1} - \frac{P}{u} + \frac{Q}{u - \varkappa}, \qquad \varkappa = n - 1, \end{equation} with the same trace projection~$Q$ as type~$B$ (now on $\bC^{2n}$), satisfying $Q^2 = 2n\, Q$ and $PQ = QP = Q$. \end{enumerate} In all four cases, the Yang--Baxter equation \begin{equation}\label{eq:ybe-all-types} R_{12}(u{-}v)\, R_{13}(u)\, R_{23}(v) = R_{23}(v)\, R_{13}(u)\, R_{12}(u{-}v) \end{equation} holds, verified numerically in the fundamental representation for $A_1$--$A_4$, $B_2$--$B_4$, $C_2$--$C_4$, $D_3$--$D_5$ at $10^3$ random spectral parameters per type \textup{(}\texttt{yangian\_rtt\_all\_types.py}\textup{)}. The RTT relation~\eqref{eq:rtt-relation} with the type-specific $R$-matrix defines $Y(\fg)$ for all classical~$\fg$. \end{theorem} 
PROOF: \begin{proof} The proof proceeds in three steps. \emph{Step 1: Operator identities.} For types $B$ and $D$, the trace projection $Q$ satisfies $Q^2 = NQ$ (where $N = \dim V$), $PQ = QP = Q$: these follow from $Q_{(ij),(kl)} = \delta_{ij}\delta_{kl}$, giving $(Q^2)_{(ij),(kl)} = \sum_{m,n} \delta_{ij}\delta_{mn}\delta_{mn}\delta_{kl} = N\,\delta_{ij}\delta_{kl}$. For type $C$, the symplectic contraction $K$ satisfies $K^2 = -NK$ and $PK = KP = -K$: the sign difference from the orthogonal case arises because $J$ is skew-symmetric ($J^T = -J$), so $PK = -K$ rather than $PK = Q$. \emph{Step 2: YBE verification.} The Yang--Baxter equation is verified by expanding $R_{12}(u{-}v) R_{13}(u) R_{23}(v)$ using the operator identities from Step~1. For type~$A$, this is the classical computation of Yang~\cite{Yang67}: both sides reduce to $u(u{-}v)\,\mathbb{1} + u\,P_{23} + (u{-}v)P_{13} + v\,P_{12} + P_{12}P_{23} + P_{23}P_{13}$. For types $B$, $C$, $D$, the verification uses the same strategy with the additional operator $Q$ or $K$; the identities $Q^2 = NQ$, $PQ = Q$ (resp.\ $K^2 = -NK$, $PK = -K$) close the calculation. \emph{Step 3: RTT presentation.} The RTT relation $R_{12}(u{-}v) T_1(u) T_2(v) = T_2(v) T_1(u) R_{12}(u{-}v)$ with the type-specific $R$-matrix generates $Y(\fg)$ by Molev~\cite[Theorems 3.2.1, 4.2.1, 4.3.1, 4.4.1]{molev-yangians}. \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1043
STMT: \begin{theorem}[All-types Yangian structure; \ClaimStatusProvedHere]% \label{thm:all-types-yangian-structure} For every simple Lie algebra~$\fg$ with dual Coxeter number~$h^\vee$ and fundamental representation~$V_{\omega_i}$: \begin{enumerate}[label=\textup{(\roman*)}] \item \emph{Collision residue and the classical $r$-matrix.} The genus-$0$ binary collision residue of the bar-complex MC element~$\Theta_\cA$ for $\cA = \hat{\fg}_k$ produces the classical $r$-matrix \begin{equation}\label{eq:r-matrix-all-types} r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \frac{\Omega}{(k + h^\vee)\,z} \;\in\; \fg \otimes \fg(z^{-1}), \end{equation} where $\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b$ is the quadratic Casimir tensor (inverse Killing form) and the Sugawara denominator $k + h^\vee$ arises from dualizing the zeroth product via the level-shifted Killing form (Computation~\ref{comp:sl2-collision-residue-kz}). %: this is a section on C_2(X), not a formula over a point. Equivalently, in the trace-form normalization where $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads $r(z) = \Omega_{\mathrm{tr}}/z$. This $r$-matrix satisfies the classical Yang--Baxter equation in spectral-parameter form \textup{(}equivalently, the infinitesimal braid relations for $\Omega$\textup{)}, for all simple~$\fg$ \textup{(}\texttt{quantum\_rmatrix\_barcomplex.py}, verified for $A_1$--$A_3$, $B_2$--$B_3$, $C_1$--$C_3$, $D_3$--$D_4$\textup{)}. \item \emph{Quantization and RTT.} The $\hbar$-deformation $R(u) = 1 + \hbar\, r(u) + O(\hbar^2)$ satisfies the quantum Yang--Baxter equation \[ R_{12}(u{-}v)\, R_{13}(u)\, R_{23}(v) = R_{23}(v)\, R_{13}(u)\, R_{12}(u{-}v), \] and the RTT relation $R_{12}(u{-}v)\, T_1(u)\, T_2(v) = T_2(v)\, T_1(u)\, R_{12}(u{-}v)$ defines $Y(\fg)$ for all simple~$\fg$. For the classical types, the explicit $R$-matrices are those of Theorem~\textup{\ref{thm:rtt-all-classical-types}}. \item \emph{Multiplicity-free $\ell$-weights.} For any simple~$\fg$ and any fundamental weight~$\omega_i$, the evaluation module $V_{\omega_i}(a) = \mathrm{ev}_a^*(V_{\omega_i})$ of $Y(\fg)$ has the property that its $q$-character $\chi_q(V_{\omega_i}(a))$ is a sum of distinct $\ell$-weight monomials: no $\ell$-weight has multiplicity $> 1$. This is the fundamental result of Chari--Moura~\cite{ChariMoura06}. The multiplicity-free property ensures that the tensor product $V_{\omega_i}(a) \otimes V_{\omega_j}(b)$ has a composition series whose successive quotients are $\ell$-weight-separated at generic spectral parameters, enabling the categorical Clebsch--Gordan decomposition \textup{(}Theorem~\textup{\ref{thm:categorical-cg-all-types}}\textup{)}. \item \emph{MC3 categorical closure.} The multiplicity-free $\ell$-weight property, combined with the Francis--Gaitsgory pro-nilpotent completion and the DK comparison on compacts, yields: \begin{enumerate}[label=\textup{(\alph*)}] \item Prefundamental representations $L_i^\pm(a)$ exist as limits of evaluation modules in the Borel subalgebra $Y_q^+(\fg)$ for all simple~$\fg$ \textup{(}Hernandez--Jimbo~\cite{HJ12}\textup{)}. \item The Baxter TQ relation $t(u)\, Q_i(u) = a_i(u)\, Q_i(u - 1) + d_i(u)\, Q_i(u + 1)$ holds for the transfer-matrix eigenvalues, where $Q_i(u)$ is the eigenvalue of the $Q$-operator associated to the $i$-th simple root. \item The evaluation-generated core $\mathcal{O}^{\mathrm{eval}}(\fg)$ of the Yangian category~$\mathcal{O}$ is thick-generated by evaluation modules for all simple types. MC3 Layers~1 and~2 are unconditional for all simple Lie types on the evaluation-generated core; Layer~3 (shifted prefundamental generation) is unconditional in type~$A$ and conditional on Conjecture~\textup{\ref{conj:rank-independence-step2}} for other types \textup{(}Corollary~\textup{\ref{cor:mc3-all-types}}\textup{)}. \end{enumerate} \end{enumerate} \end{theorem} 
PROOF: \begin{proof} The proof assembles four ingredients. \emph{Step~1: Classical $r$-matrix.} The bar-complex propagator $\eta_{12} = d\log(z_1 - z_2)$ absorbs one pole order from the OPE. For $\hat{\fg}_k$, the OPE $J^a(z)J^b(w) \sim k\,g^{ab}/(z{-}w)^2 + f^{ab}{}_c J^c(w)/(z{-}w)$ yields, after $d\log$ absorption, the classical $r$-matrix $r(z) = k\Omega/z$ (the double pole $k\,g^{ab}/(z{-}w)^2$ shifts to $k\,g^{ab}/(z{-}w)$; the simple pole becomes regular and drops). The classical Yang--Baxter equation for $r(z) = k\Omega/z$ reduces to the infinitesimal braid relations $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$, which hold because $\Omega$ is constructed from a basis of $\fg$ and its dual. \emph{Step~2: Quantization.} The QYBE for $R(u)$ at leading $\hbar$-order reduces to the CYBE for $r(u) = k\Omega/u$. The full QYBE is verified for all classical types by the operator algebra of $P$, $Q$, $K$ (Theorem~\ref{thm:rtt-all-classical-types}). For the exceptional types $E_6$--$E_8$, $F_4$, $G_2$, the quantum $R$-matrix in the fundamental representation is constructed via the universal $R$-matrix of $U_q(\fg)$~\cite{Drinfeld85,Jimbo85}, which satisfies QYBE universally; the fundamental representation is obtained by evaluating on $V_{\omega_1} \otimes V_{\omega_1}$. \emph{Step~3: Multiplicity-free $\ell$-weights.} By Chari--Moura~\cite[Theorem~1.1]{ChariMoura06}, for any simple $\fg$ and any fundamental weight $\omega_i$, the $q$-character of the fundamental evaluation module $V_{\omega_i}(a)$ of the quantum affine algebra $U_q(\hat{\fg})$ has multiplicity-free $\ell$-weights. The key property is that the monomials in $\chi_q(V_{\omega_i}(a))$ are in bijection with the weight spaces of $V_{\omega_i}$ as a $\fg$-module, and the $\ell$-weight refinement separates degenerate classical weight spaces by the spectral parameter. This replaces the earlier minuscule hypothesis (which guaranteed multiplicity-free \emph{classical} weights but restricted to a single fundamental weight per type). \emph{Step~4: MC3 categorical closure.} Given multiplicity-free $\ell$-weights, the categorical Clebsch--Gordan decomposition of Theorem~\ref{thm:categorical-cg-all-types} follows by the standard argument: the tensor product $V_{\omega_i}(a) \otimes V_{\omega_j}(b)$ admits a composition series with factors indexed by the dominant monomials in $\chi_q(V_{\omega_i}(a)) \cdot \chi_q(V_{\omega_j}(b))$, and the multiplicity-free property ensures that no two factors share an $\ell$-weight. The thick generation of $\mathcal{O}^{\mathrm{eval}}$ follows from the fact that every finite-dimensional $U_q(\hat{\fg})$-module has a Jordan--H\"older series whose factors are evaluation modules (or tensor products thereof). In type~$A$, the Francis--Gaitsgory pro-nilpotent completion~\cite{FG12} extends the comparison to the full category~$\mathcal{O}$; for other simple types, this extension is conditional on Conjecture~\ref{conj:rank-independence-step2}. The DK comparison on compact objects (Corollary~\ref{cor:dk23-all-types}) then upgrades the $K_0$-level Clebsch--Gordan identity to an exact equivalence on the evaluation-generated core. \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:5023
STMT: \begin{theorem}[Standard type-\texorpdfstring{$A$}{A} Yangian DK-4/DK-5 closure: seven variant hypotheses; \ClaimStatusProvedHere] \label{thm:yangian-dk45-closure-variants}% \label{thm:yangian-typea-realization-plus-compacts}% \label{thm:yangian-typea-realization-plus-fundamental-packet}% \label{thm:yangian-typea-realization-plus-core-realization}% \label{thm:yangian-formal-moduli-plus-core-realization}% \label{thm:yangian-typea-realization-plus-dg-packet}% \label{thm:yangian-canonical-realization-plus-one-seed}% \label{thm:yangian-canonical-realization-plus-vector-line}% Under any one of the following seven sets of hypotheses, the standard type-$A$ Yangian DK-4/DK-5 packet closes. \begin{enumerate}[label=\textup{(\roman*)}] \item\emph{Realization $+$ compact core.} Assume the hypotheses of Proposition~\ref{prop:yangian-typea-realization-criterion}. Assume further that the compact cores of \(\operatorname{Mod}^{\mathrm{comp}}(\Ydg_{\cA})\) and \(\operatorname{Rep}^{\mathrm{spec}}(\QGspec(R_{\cA}))^{\mathrm{op}}\) are presentable, stable, compactly generated, and exactly equivalent in a way compatible with DK-3 on the completed fundamental packet. \item\emph{Realization $+$ completed fundamental packet.} Assume the hypotheses of Proposition~\ref{prop:yangian-typea-realization-criterion}. Assume further that the completed dg-shifted and spectral categories are presentable, stable, and compactly generated; that their compact objects are the smallest full stable idempotent-complete braided monoidal subcategories containing the completed fundamental evaluation packets; and that there exist exact braided monoidal functors between those compact cores whose restrictions to the completed fundamental evaluation packets recover the DK-3 transport and whose composites are the identity on that packet. \item\emph{Realization $+$ core realization.} Assume the hypotheses of Proposition~\ref{prop:yangian-typea-realization-criterion}. Assume further that the completed dg-shifted and spectral categories are presentable, stable, and compactly generated, with compact objects exactly $\mathcal{C}_Y^\omega$ and $\mathcal{C}_q^\omega$; and that those compact cores are exact braided monoidal realizations of the chosen finite-dimensional factorization DK pair in the sense of Proposition~\ref{prop:yangian-dk5-core-realization}. \item\emph{Canonical formal-moduli target $+$ core realization.} Let $\cA=\mathcal{Y}(\mathfrak{sl}_M)$, $\mathfrak{g}_{\cA}:=T_*\mathfrak{F}_{\cA}$ be the canonical H-level dg target of Proposition~\ref{prop:yangian-canonical-hlevel-target}, and let $U^{\mathrm{comp}}(\mathfrak{g}_{\cA})$ be the canonical associative dg model of Proposition~\ref{prop:yangian-canonical-envelope}. Assume that the hypotheses of Proposition~\ref{prop:yangian-typea-realization-criterion} hold for $U^{\mathrm{comp}}(\mathfrak{g}_{\cA})$. Assume further that the completed dg-shifted and spectral categories are presentable, stable, and compactly generated, with compact objects exactly $\mathcal{C}_{\mathfrak g}^\omega$ and $\mathcal{C}_q^\omega$; and that those compact cores are exact braided monoidal realizations of a chosen finite-dimensional factorization DK pair in the sense of Proposition~\ref{prop:yangian-dk5-core-realization}. \item\emph{Realization $+$ spectral vector-line realization.} Assume the hypotheses of Proposition~\ref{prop:yangian-typea-realization-criterion}. Assume further that the spectral compact core admits an exact braided monoidal functor $J_q^\omega$ whose restriction to the vector evaluation line is an equivalence onto the completed vector spectral line, as in Proposition~\ref{prop:yangian-dk5-spectral-vector-line}. \item\emph{Canonical target $+$ one canonical spectral seed (equivariant multiplicative locus).} As in~\textup{(iv)}, let $\cA=\mathcal{Y}(\mathfrak{sl}_M)$ with canonical target $U^{\mathrm{comp}}(\mathfrak{g}_{\cA})$ satisfying the hypotheses of Proposition~\ref{prop:yangian-typea-realization-criterion}. Assume further the equivariant multiplicative spectral realization hypotheses of Corollary~\ref{cor:yangian-canonical-realization-to-spectral-seed}, so that the shift family is intrinsic and the single canonical spectral seed $V^\omega(0):=J_q^\omega(V(0))$ is defined. \item\emph{Canonical target $+$ spectral vector-line realization.} As in~\textup{(iv)}, let $\cA=\mathcal{Y}(\mathfrak{sl}_M)$ with canonical target $U^{\mathrm{comp}}(\mathfrak{g}_{\cA})$ satisfying the hypotheses of Proposition~\ref{prop:yangian-typea-realization-criterion}. Assume further that the spectral compact core admits an exact braided monoidal functor \(J_q^\omega\colon \operatorname{Fact}_{\Eone}^{\mathrm{fd}}(U_q(\mathfrak{sl}_M))^{\mathrm{op}} \longrightarrow \mathcal C_q^\omega\) whose restriction to the vector evaluation line is an equivalence onto the completed vector spectral line, as in Proposition~\ref{prop:yangian-dk5-spectral-vector-line}. \end{enumerate} \end{theorem} 
PROOF: \begin{proof} In each variant, Proposition~\ref{prop:yangian-typea-realization-criterion} (applied directly or via its canonical specialization) closes the local DK-4 packet on the standard type-$A$ tower. \textup{(i)} The compact-core equivalence is the input of Corollary~\ref{cor:yangian-dk5-compact-core}, which closes DK-5. \textup{(ii)} The three additional hypotheses are the input of Corollary~\ref{cor:yangian-dk5-fundamental-packet}, which closes DK-5. \textup{(iii)} The compact-core realization is the input of Corollary~\ref{cor:yangian-dk5-core-realization}, which closes DK-5. \textup{(iv)} Proposition~\ref{prop:yangian-canonical-envelope} identifies the dg model with the canonical formal-moduli target. The compact-core hypotheses reduce to variant~\textup{(iii)} with $\mathcal{C}_Y^\omega$ realized inside $\operatorname{Mod}^{\mathrm{comp}}(\mathfrak{g}_{\cA})$ as $\mathcal{C}_{\mathfrak g}^\omega$. \textup{(v)} Propositions~\ref{prop:yangian-dk5-dg-extension-existence}, \ref{prop:yangian-dk5-dg-realization-formal}, and Corollary~\ref{cor:yangian-dk5-dg-packet-ind} close the dg side. On the spectral side, the vector-line hypothesis, together with the seed-and-shift construction (Propositions~\ref{prop:yangian-dk5-spectral-seed-shift-construction} and~\ref{prop:yangian-dk5-spectral-core-shifts}, Corollary~\ref{cor:yangian-dk5-spectral-seed-realization}), satisfies the input of Corollary~\ref{cor:yangian-dk5-core-realization}, so DK-5 closes. \textup{(vi)} Corollary~\ref{cor:yangian-canonical-realization-to-spectral-seed} makes the hypotheses of Corollary~\ref{cor:yangian-dk5-spectral-one-seed} automatic. The completed vector line, fundamental packet, spectral compact core, and ambient spectral category are all formal, so variant~\textup{(vii)} is satisfied. \textup{(vii)} The vector-line hypothesis is the remaining spectral input of variant~\textup{(v)} specialized to the canonical target. \end{proof} 





thinking
**Considering theorem implications**

I think I should avoid diving too deep into the boundary-holographic complexity classification theorem right now. The proof cites Brown-Henneaux for the Virasoro case and seems to make general claims. It could be applicable across various cases, but I wonder if there are limitations in specificity. It feels like a lot is at stake, and careful consideration is key before deciding how to approach this topic. Let’s take a step back for now!
thinking
**Exploring theorem details**

I’m looking at the statement about dividing general class G versus L/C/M and the specific parts iii and iv. The proof seems fine, using the theorem and specific Virasoro/affine methods, but I feel we need more robust findings. I'll consider searching for other relevant results, like `thm:rtt-all-classical-types` and `thm:e1-universality-cy3`, which might not have been addressed due to prior remarks. I also wonder if item (iii) cites the Chari-Moura theorem, but I can't assert its validity without further confirmation, especially since the user wants certainty based solely on the file contents.
thinking
**Analyzing theorem grounding**

I’m considering the potential for `thm:rtt-all-classical-types`, which seems grounded since the proof fully computes type A, while stating that B, C, and D use the same strategy, though the theorem claims universality. It appears the proof is schematic and based on low-rank numerics, which is solid. 

Next, I’ll look at the remarks in `holographic_datum_master` after the theorem. I also want to examine findings from Volume III's `e1-universality-cy3` theorem, which links to other relevant pillars, even though their specifications impact the toric aspect of the theorem.
thinking
**Clarifying proof scope**

The remark doesn’t claim that part b is proven for all toric structures; it only specifies that it’s particular to toric CY3. So, that’s not a contradiction! However, the line in the proof that states, “By Theorem c3-hochschild... This argument applies universally: for any toric CY3...” seems like an unproven leap. It looks like there’s a scope failure moving from the C^3 proof to the more general toric CY3, which is worth noting.
thinking
**Searching for deformation space**

I’m exploring if there's a search result for “one-dimensional deformation space” or “sigma_3.” If it turns out there isn't any, that could be a strong result in itself. I want to ensure I'm using the right search terms, so I'll keep that in mind as I go along. It's interesting to see what pops up when I dig deeper into these concepts. Let’s see what I can find!
exec
/bin/zsh -lc "rg -n 'one-dimensional deformation space|unique deformation|sigma_3|equivariant deformation space is one-dimensional|toric CY\\"'$_3'"\\"'$'"' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
322:& $\big\downarrow$ \quad $\Omega$-deformation in the $\sigma_3$ direction \\[3pt]
333:The input at Step~1 is $\mathrm{PV}^*(\C^3) = \bigoplus_{p=0}^{3} \Gamma(\C^3, \bigwedge^p T_{\C^3})$, the algebra of polyvector fields with the Schouten--Nijenhuis bracket. The $\mathrm{GL}(3)$-invariant sector carries the deformation-theoretic data needed for the CY-to-chiral functor. The $\Omega$-deformation at Step~2 is parametrized by $\sigma_3 = h_1 h_2 h_3$ (with $h_1 + h_2 + h_3 = 0$), the unique direction in $\HH^2(\mathrm{PV}^*(\C^3))$. At the self-dual level ($\sigma_3 \to 0$, giving $h_1 = 1, h_2 = 0, h_3 = -1$), the output at Step~3 is $\cW_{1+\infty}$ at $c = 1$, which \emph{is} the Heisenberg VOA $H_1$.
344: \item \emph{Step~2}: $\HH^2(\mathrm{PV}^*(\C^3)) = 1$, so the deformation is unique, spanned by $\sigma_3$ (Theorem~\textup{\ref{thm:c3-hochschild}}). $\HH^3 = 0$ by Bogomolov--Tian--Todorov, so the deformation is unobstructed.
383:\subsection{Hochschild cohomology and the unique deformation}
386:\begin{theorem}[Hochschild cohomology and unique deformation]
391: \item $\HH^2(\mathrm{PV}^*(\C^3)) = 1$: the deformation space is one-dimensional, spanned by the $\sigma_3$ direction. The unique deformation is the $\Omega$-deformation.
402:The equivariant parameters $h_1, h_2, h_3$ with $h_1 + h_2 + h_3 = 0$ span a two-dimensional space. The unique $T^3$-equivariant deformation class in $\HH^2$ is $\sigma_3 = h_1 h_2 h_3$, the elementary symmetric polynomial of degree $3$. The class $\sigma_2 = h_1 h_2 + h_2 h_3 + h_3 h_1 = -(h_1^2+h_2^2+h_3^2)/2$ on the constraint locus is generically nonzero, but it generates a trivial deformation equivalent to rescaling: the $\sigma_2$-deformation acts as a conformal weight shift that can be absorbed by redefining the grading. The nontrivial deformation class is $\sigma_3 = h_1 h_2 h_3$, which cannot be removed by regrading.
404:The vanishing $\HH^3 = 0$ is the Bogomolov--Tian--Todorov unobstructedness theorem for the CY$_3$ moduli problem: the Kodaira--Spencer dga of $\C^3$ is formal, and the Maurer--Cartan moduli space is smooth. This guarantees that the $\Omega$-deformation determined by $\sigma_3$ extends to all orders.
420:When $\sigma_3 = 0$ (equivalently, one of $h_1, h_2, h_3$ vanishes), the factorization envelope of the abelian Lie conformal algebra is the free Heisenberg vertex algebra $H_1$. The representation category $\Rep(H_1)$ is symmetric monoidal: the braiding on Fock modules is the identity (all monodromy is trivial for a free boson at level~$1$). In particular, $\cZ(\Rep^{\Eone}(H_1)) = \Rep(H_1)$ itself (the Drinfeld center of a symmetric monoidal category is the category itself), so no $\Etwo$-enhancement occurs.
422:When $\sigma_3 \neq 0$, the $\Omega$-deformation introduces the nonlinear OPE terms of $\cW_{1+\infty}$. These terms break the $\Einf$ symmetry to $\Etwo$, and the Drinfeld center produces a nontrivially braided category with the Yang $R$-matrix (Theorem~\ref{thm:c3-drinfeld-center}).
424:For a \emph{compact} CY$_3$ such as the quintic, the global sections of the polyvector sheaf have nontrivial bracket (the complex structure moduli introduce genuine noncommutativity), and the $\Omega$-deformation is not needed. The role of $\sigma_3$ for $\C^3$ is to \emph{replace} the global geometric data that is absent for a noncompact variety.
492:Assuming Conjecture~\textup{\ref{conj:cy-to-chiral-d3}} is formulated with symplectic structure group (i.e., the $d = 3$ CY-to-chiral functor targets a CY$_3$ chiral algebra whose obstruction theory sits in $\pi_3(B\Sp(2m))$), the topological component of that obstruction vanishes. The remaining chain-level construction of the trivialization of $\kappa_{\mathrm{ch}} \cdot [\Omega_3]$ is known to exist by holomorphic Chern--Simons, but its compatibility with the full $\Ainf$-structure is part of CY-A$_3$ itself and remains conjectural. For the toric CY$_3$ verified in compute ($\C^3$, conifold, local $\bP^2$, local $\bP^1 \times \bP^1$, $K3 \times E$), the $\Eone \to \Etwo$ enhancement obstruction vanishes at the level of the explicit CoHA construction.
837:For any toric CY$_3$ category $\cC$ with $T^3$-equivariant $\Omega$-deformation ($\sigma_3 = h_1 h_2 h_3 \neq 0$, subject to $h_1 + h_2 + h_3 = 0$), the chiral algebra $A_\cC = \Phi(\cC)$ is natively $\Eone$. For compact CY$_3$ without a global torus action, the $\Eone$ nature is expected but requires a different argument; see Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.
851:By Theorem~\ref{thm:c3-hochschild}, $\HH^2(\PV^*(\C^3)) = 1$: the deformation space is one-dimensional, spanned by $\sigma_3 = h_1 h_2 h_3$. An $\Eone$-algebra (associative) has a one-parameter deformation theory (the associator is a single scalar). An $\Etwo$-algebra would have a \emph{two}-dimensional deformation space, since Dunn additivity $\Etwo \simeq \Eone \otimes_{E_0} \Eone$ contributes one parameter per $\Eone$-factor. The fact that $\dim \HH^2 = 1$ is therefore diagnostic of $\Eone$, not $\Etwo$.
853:This argument applies universally: for any toric CY$_3$ with $T^3$-equivariant $\Omega$-deformation, the equivariant deformation space is one-dimensional (spanned by $\sigma_3$), and the conclusion is $\Eone$.
878:At the self-dual point $\sigma_3 = 0$, the $\Omega$-deformation is trivial and the chiral algebra degenerates to the free Heisenberg $H_1$. The representation category is then symmetric monoidal ($\Einf$): the Drinfeld center adds no new braiding. The $\Eone$ universality theorem applies only when $\sigma_3 \neq 0$.
911: \item Pillar~(b) \textup{(}one-dimensional deformation space\textup{)}: specific to toric CY$_3$. Compact CY$_3$ have $\dim \HH^2 = h^{2,1}$, which is multi-dimensional for generic threefolds ($h^{2,1} = 101$ for the quintic). Does not categorify.
913: \item Pillar~(d) \textup{(}$R$-matrix unitarity\textup{)}: specific to toric CY$_3$ with explicit equivariant parameters. The structure function $g(z)$ requires the torus action. Does not categorify in its current form.
915:The categorical content of the four pillars is precisely the $\Etwo$-obstruction of Proposition~\textup{\ref{prop:e1-obstruction-categorical}}: Serre duality forces antisymmetry of the Euler form, which obstructs the promotion. The \emph{construction} of the $\Eone$ structure for non-toric CY$_3$ remains the content of Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.
959:For toric CY$_3$ varieties $X_\Sigma$, the atlas is explicitly constructible: $|I| = |\Sigma(3)|$ (the number of maximal cones in the fan), each chart $(Q_\alpha, W_\alpha)$ is the McKay quiver of the corresponding toric patch, and the mutations are the flop transitions.


thinking
**Exploring toric variety theorems**

I’m investigating the theorem `toric-chart-gluing`, which proves all smooth toric Calabi-Yau 3 varieties. There's something about the e1-universality theorem being verified for various cases, although quintics aren't toric. This repository might be messy, but I think we might find proof related to `toric-chart-gluing`.

I'm considering focusing on theorems since the user asked for those specifically, perhaps even inspecting `thm:toric-chart-gluing`, and maybe the proof could relate to all smooth toric varieties through McKay atlas and BKR.
thinking
**Examining proofs and theorems**

I'm analyzing the proof that cites Brown-Henneaux for the Virasoro algebra and Costello-Gwilliam's general case. I see potential findings in `yangians_foundations`, particularly `thm:all-types-yangian-structure`. Step 4 discusses thick generation of evaluation cores from finite-dimensional U_q modules, which sounds broad but unsupported.

There's a specific issue with the KZ-normalized condition in item (i) versus the derived trace-form in Step 1; it's a convention mismatch. The user is focused on whether the proof covers specific cases, and there's an additional concern regarding item iv about thick generation being conditional.
exec
/bin/zsh -lc "rg -n '\\\\begin\\{theorem\\}|For any toric CY\\"'$_3'"\\"'$|For every smooth toric CY'"\\"'$_3'"\\"'$|For all smooth toric CY'"\\"'$_3'"\\"'$|For every toric CY'"\\"'$_3'"\\"'$'"' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
32:\begin{theorem}[CY-to-chiral functor: Theorem CY-A$_2$, $d = 2$]
338:\begin{theorem}[The $d = 3$ functor chain is verified for $\C^3$]
363:\begin{theorem}[Abelianity of the classical bracket]
386:\begin{theorem}[Hochschild cohomology and unique deformation]
455:\begin{theorem}[Vanishing of the $\bS^3$-framing obstruction for CY$_3$ categories]
507:\begin{theorem}[\v{C}ech contracting homotopy for compact CY$_3$;
678:\begin{theorem}[Drinfeld center identification for $\C^3$]
790:\begin{theorem}[Modular characteristic of $\C^3$: five-path verification]
834:\begin{theorem}[$\Eone$ universality for CY$_3$ chiral algebras]
837:For any toric CY$_3$ category $\cC$ with $T^3$-equivariant $\Omega$-deformation ($\sigma_3 = h_1 h_2 h_3 \neq 0$, subject to $h_1 + h_2 + h_3 = 0$), the chiral algebra $A_\cC = \Phi(\cC)$ is natively $\Eone$. For compact CY$_3$ without a global torus action, the $\Eone$ nature is expected but requires a different argument; see Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.
1025:\begin{theorem}[Quiver-chart gluing for toric CY$_3$]
1107:\begin{theorem}[KS wall-crossing $=$ homotopy colimit $=$ MC gauge equivalence]
1146:\begin{theorem}[Scattering diagrams as $\Eone$ Maurer--Cartan data]
1242:\begin{theorem}[$\Eone$ descent degeneration]
1452:\begin{theorem}[Bar-hocolim commutation]
1858:\begin{theorem}[$\chi_{\mathrm{top}}/24 \neq \kappa_{\mathrm{ch}}$ in general]
1978:\begin{theorem}[HAE $=$ MC genus spectral sequence, structural identification]
2038:\begin{theorem}[Curved chiral algebra from non-CY local surfaces]
2055:\begin{theorem}[Hitchin modular characteristic]

thinking
**Exploring mathematical findings**

I’m contemplating the theorem or proof regarding `quiver-chart gluing for toric CY3` to see if it utilizes finite maximal cones in general. It seems possible, but the proof might only be focusing on pairwise adjacency and triple overlaps as a "formal consequence of fan relations." That makes me think it’s not specific enough for what I need. I might want to look into findings from Volume 1 in `arithmetic_shadows`, particularly concerning `general-nahc` and `general-bps`, along with `thm:universality-of-G`.
exec
/bin/zsh -lc "sed -n '5068,5118p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The universality of~$G$ is a direct consequence of the
Stieltjes representation of the MC element: the spectral
measure~$\rho$ encodes the MC data of~$\Theta_\cA$, and $G$
is its moment generating function.

\begin{theorem}[Universality of $G$]%
\label{thm:universality-of-G}%
\ClaimStatusProvedHere%
\index{shadow generating function!universal structure}
For any chirally Koszul algebra~$\cA$ with HS-sewing, the
connected genus-$1$ free energy admits the factorization
\begin{equation}\label{eq:universality-factorization}
 F_1^{\mathrm{conn}}(q;\,\cA)
 \;=\;
 G_\cA\!\bigl(t(q)\bigr),
 \qquad
 G_\cA(t)
 \;=\;
 \int\!\log(1 - \lambda\,t)\,d\rho_\cA(\lambda),
\end{equation}
exec
/bin/zsh -lc "sed -n '5118,5158p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The leading-order universality~\eqref{eq:G-leading-order}:
for all standard families, the spectral measure at
leading $1/c$ is a single atom at
$\lambda_{\mathrm{eff}} = -6/c$
(Remark~\ref{rem:effective-coupling}), giving
$G = \log(1 + 6t/c)$. The first correction at subleading
order involves the quartic contact coupling
$Q^{\mathrm{ct}}_\cA$
(Proposition~\ref{prop:virasoro-quartic-determinant}),
which splits the single atom into a pair whose
separation is controlled by~$Q^{\mathrm{ct}}$.
\end{proof}

\subsection{The MC recursion in spectral coordinates}%
\label{sec:mc-newton-identities}%
\index{Newton's identity!from MC equation|textbf}

Rewriting the MC recursion in spectral coordinates (power sums
and elementary symmetric polynomials via the Newton relations)
reveals that the self-interaction encoded by
exec
/bin/zsh -lc "rg -n 'for all standard families|For all standard families|all standard families|not universal across all|specific to' chapters/connections/arithmetic_shadows.tex chapters/connections/holographic_datum_master.tex /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:796:This is \emph{not} $c/2 = 1/2$. At $c = 1$, the $\cW_{1+\infty}$ algebra \emph{is} the Heisenberg VOA $H_1$, whose modular characteristic is $\kappa_{\mathrm{ch}}(H_k) = k$, giving $\kappa_{\mathrm{ch}} = 1$. The formula $\kappa_{\mathrm{ch}} = c/2$ is specific to the Virasoro algebra; for the Heisenberg VOA, $\kappa_{\mathrm{ch}} = k$ (the level), not $c/2$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:910: \item Pillar~(a) \textup{(}abelian classical bracket\textup{)}: specific to $\C^3$. For compact CY$_3$, the global sections of the polyvector sheaf carry nontrivial brackets from the complex structure moduli. Does not categorify.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:911: \item Pillar~(b) \textup{(}one-dimensional deformation space\textup{)}: specific to toric CY$_3$. Compact CY$_3$ have $\dim \HH^2 = h^{2,1}$, which is multi-dimensional for generic threefolds ($h^{2,1} = 101$ for the quintic). Does not categorify.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:913: \item Pillar~(d) \textup{(}$R$-matrix unitarity\textup{)}: specific to toric CY$_3$ with explicit equivariant parameters. The structure function $g(z)$ requires the torus action. Does not categorify in its current form.
chapters/connections/arithmetic_shadows.tex:2682:holds for all standard families. This is the
chapters/connections/arithmetic_shadows.tex:2712: verified for all standard families at primes
chapters/connections/arithmetic_shadows.tex:4031:Virasoro; the analogous finiteness holds for all standard families).
chapters/connections/arithmetic_shadows.tex:5119:for all standard families, the spectral measure at

thinking
**Exploring arithmetic shadows**

I'm considering inspecting arithmetic shadows around the numbers 2660 and 2712. Hmm, this might connect to some broader universal theorem as well! I wonder what insights I could uncover by diving into these numbers. There's still a bit of uncertainty, so I'll take my time and carefully analyze what I find. Let’s see what patterns or connections may arise from this exploration!
exec
/bin/zsh -lc "sed -n '2655,2725p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the Kubota--Leopoldt $p$-adic $L$-function
$L_p(s, \omega^a)$ for Dirichlet characters.
The shadow tower inherits this structure: the degree-$r$
coefficients $S_r(\cA)$, when reduced modulo~$p$,
satisfy congruences determined by the $p$-adic residue
class of~$r$. For Heisenberg ($S_r = 0$ for $r \geq 3$),
all congruences are trivially satisfied. For Virasoro
($S_r = (-1)^{r+1}(6/c)^{r-2}/r$ at leading order), the
congruences reduce to $p$-adic properties of the geometric
series in~$6/c$, which are controlled by $v_p(6/c)$.
The convergence radius $p^{-1/(p-1)}$ is the shadow-tower
manifestation of the $p$-adic exponential radius, linking
the tower to the Iwasawa-theoretic framework.
\end{remark}

\begin{remark}[Hilbert symbol detection of shadow-spectral zero-crossings]
\label{rem:hilbert-symbol-detection}
\index{Hilbert symbol!shadow-spectral detection|textbf}
\index{shadow invariants!$p$-adic zero-crossings}
The $p$-adic Hilbert symbols $(\kappa, \Delta)_p$ detect
exec
/bin/zsh -lc "awk '/"'^'"\\//{print "'$1}'"' /tmp/scope_candidates.txt | sort | uniq -c | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   1 /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:113
   1 /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:834
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:9200
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1377
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:3245
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:210
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:768
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex:1282
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_complexity.tex:1406
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_soft_graviton_theorems.tex:924
   1 /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:450
   1 /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:3999
   1 /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4718
   1 /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5073
   1 /Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:9475
   1 /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:722
   1 /Users/raeez/chiral-bar-cobar/chapters/connections/subregular_hook_frontier.tex:228
   1 /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_soft_graviton_theorems.tex:911
   1 /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:998
   1 /Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:1627
exec
/bin/zsh -lc "for p in 'chapters/theory/bar_cobar_adjunction_inversion.tex:572' 'chapters/theory/higher_genus_foundations.tex:801' 'chapters/theory/koszul_pair_structure.tex:468' 'chapters/theory/nilpotent_completion.tex:947' 'chapters/theory/higher_genus_modular_koszul.tex:21613' 'chapters/examples/w_algebras.tex:1627' 'chapters/examples/yangians_computations.tex:3039'; do echo \"=== "'$p"; rg -n -A2 -B0 "''^$p$" /tmp/scope_candidates.txt; done' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:
=== chapters/theory/bar_cobar_adjunction_inversion.tex:572
=== chapters/theory/higher_genus_foundations.tex:801
=== chapters/theory/koszul_pair_structure.tex:468
=== chapters/theory/nilpotent_completion.tex:947
=== chapters/theory/higher_genus_modular_koszul.tex:21613
=== chapters/examples/w_algebras.tex:1627
=== chapters/examples/yangians_computations.tex:3039

thinking
**Finding absolute paths**

I’m thinking about paths in /tmp that may be absolute. It feels essential to have the exact full paths, so I want to ensure I get them right. Maybe I can use a grep pattern by basename to help filter out the necessary information. I wonder if this approach will yield the precise results I’m looking for, but I’m feeling curious about how effective it’ll be. Let’s see if this method works!
exec
/bin/zsh -lc "rg -n 'bar_cobar_adjunction_inversion\\.tex:572|higher_genus_foundations\\.tex:801|koszul_pair_structure\\.tex:468|nilpotent_completion\\.tex:947|higher_genus_modular_koszul\\.tex:21613|w_algebras\\.tex:1627|yangians_computations\\.tex:3039' /tmp/scope_candidates.txt" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
21:/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:1627
29:/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3039
73:/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:21613
77:/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:572
81:/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:801
85:/Users/raeez/chiral-bar-cobar/chapters/theory/nilpotent_completion.tex:947
89:/Users/raeez/chiral-bar-cobar/chapters/theory/koszul_pair_structure.tex:468
exec
/bin/zsh -lc "sed -n '21,96p' /tmp/scope_candidates.txt" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 76

/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:1627
STMT: \begin{theorem}[Genus-1 bar-cobar inversion for \texorpdfstring{$\mathrm{Vir}_c$}{Virc}; \ClaimStatusProvedHere] \label{thm:vir-genus1-inversion} For generic central charge $c$ (specifically, $c \neq c_{r,s}$ for all $r, s \geq 1$, where $c_{r,s}$ are the minimal model central charges), the genus-1 bar-cobar adjunction: \begin{equation} \Omega\bigl(\barB^{(1)}(\mathrm{Vir}_c)\bigr) \xrightarrow{\;\sim\;} \mathrm{Vir}_c \end{equation} is a quasi-isomorphism. The spectral sequence collapses at $E_2$. \end{theorem} 
PROOF: \begin{proof} \emph{Step~1: Weight filtration.} The generator $T$ has conformal weight~$2$, so the weight filtration $F^p\barB^{(1)} = \bigoplus_{w \geq p} \barB^{(1)}_w$ is bounded below (with $w \geq 2n$ on $\barB^{(1),n}$) and exhaustive. The $E_1$ differential agrees with the genus-0 bar differential at leading order, since $K^{(1)}(z,w|\tau) = 1/(z-w) + O(1)$. \emph{Step~2: Kac determinant non-degeneracy.} For generic $c$ (avoiding the discrete set of minimal model values $c_{r,s} = 1 - 6(r-s)^2/(rs)$), the Verma module $M(c,0)$ is irreducible and the Kac determinant is nonzero at every weight. Irreducibility implies that all extensions of $V_c$ by itself split (by the same argument as Shapovalov non-degeneracy for Kac--Moody, Theorem~\ref{thm:sl2-genus1-inversion}, Step~3), giving the Ext vanishing: \begin{equation} \operatorname{Ext}^p_{\mathrm{Vir}_c}(V_c, V_c) = 0 \quad \text{for } p \geq 2 \end{equation} \emph{Step~3: $E_2$ collapse.} The $E_2$ page is concentrated in the strip $0 \leq p \leq 1$, exactly as for $\widehat{\mathfrak{sl}}_2$ (Theorem~\ref{thm:sl2-genus1-inversion}): \begin{equation} E_2^{p,q} = \begin{cases} \mathbb{C} & (p,q) = (0,0) \\ \mathrm{Vir}_c^* & (p,q) = (1,0) \\ \mathbb{C}\lambda & (p,q) = (0,2) \\ \mathrm{Vir}_c^* \cdot \lambda & (p,q) = (1,2) \\ 0 & \text{otherwise} \end{cases} \end{equation} where $\mathrm{Vir}_c^*$ denotes the linear dual of the one-dimensional space of generators (i.e., $\mathbb{C}$ for the Virasoro, since $T$ is the sole generator). All higher differentials vanish for degree reasons, so $E_2 = E_\infty$. \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras.tex:5200
STMT: \begin{theorem}[Finite termination for primitive archetypes; \ClaimStatusProvedHere] \label{thm:w-finite-termination} \index{shadow tower!finite termination} For the three frame families, the shadow obstruction tower terminates at finite degree: \begin{enumerate}[label=\textup{(\roman*)}] \item \textbf{Heisenberg:} $\mathrm{Sh}_r(\mathcal H)=0$ for all $r\ge 3$. The tower terminates at degree~$2$: it is exactly Gaussian. \item \textbf{Affine $\widehat{\mathfrak{sl}}_2$ \textup{(strict sector, minimal gauge):}} $\mathrm{Sh}_r(\mathrm{aff})=0$ for $r\ge 4$. The tower terminates at degree~$3$. \item \textbf{$\beta\gamma$ \textup{(weight-changing line):}} $\mathrm{Sh}_r(\beta\gamma)|_L=0$ for $r\ge 3$ by rank-one abelian rigidity. The tower terminates at degree~$4$ on the weight-changing line. \end{enumerate} Virasoro is the first genuinely infinite tower: $\mathrm{Sh}_r(\mathrm{Vir})\neq 0$ for all $r\ge 3$ for generic~$c$. \end{theorem} 
PROOF: \begin{proof} For each primitive archetype, finite termination follows from vanishing of all obstruction sources at the relevant degree. For the Heisenberg, all higher brackets vanish (the OPE is quadratic, so no composite fields appear). For affine $\widehat{\mathfrak{sl}}_2$, the Jacobiator vanishes and the quartic gauge freedom absorbs all remaining terms. For $\beta\gamma$, rank-one abelian rigidity (Theorem~\ref{thm:nms-rank-one-rigidity}) gives vanishing on the rank-one weight-changing line. For Virasoro, Theorem~\ref{thm:w-virasoro-quintic-forced} gives $\mathrm{Sh}_5\neq 0$. Then $\mathfrak o^{(6)}$ contains $\{\mathfrak C,\mathrm{Sh}_5\}\neq 0$, forcing $\mathrm{Sh}_6\neq 0$, and so on by induction: the cubic vertex $\mathfrak C=2x^3$ acts as a permanent source, and the non-polynomial character of the complementarity potential is established.\qedhere \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3039
STMT: \begin{theorem}[Shifted-prefundamental generation on the shifted envelope; \ClaimStatusProvedHere] \label{thm:shifted-prefundamental-generation} \index{shifted Yangian!prefundamental generation} \index{shifted envelope!prefundamental generation} \index{E1-chiral!thick generation} For $\mathfrak{g} = \mathfrak{sl}_N$ ($N \geq 2$), in the separated pro-completed shifted category $\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g})))$, every standard object of $\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g}))$ lies in the thick idempotent-complete closure of \[ \mathcal{G}_{\mathrm{shift}} \;:=\; \{V_{\omega_i}(a) \mid i = 1, \ldots, N{-}1,\; a \in \mathbb{C}\} \;\cup\; \{L^-_{i,a} \mid i = 1, \ldots, N{-}1,\; a \in \mathbb{C}\}, \] where $V_{\omega_i}(a)$ are the fundamental evaluation modules and $L^-_{i,a}$ are the negative prefundamental modules of Hern'andez--Jimbo~\cite{HJZ25}, one per node of the Dynkin diagram. In particular, the image of $D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g})))$ inside $\widehat{D}(\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g})))$ is contained in the localizing subcategory generated by $\mathcal{G}_{\mathrm{shift}}$. \end{theorem} 
PROOF: \begin{proof} Four steps. \smallskip\noindent\textit{Step~1 (Evaluation core).} By the proved finite-dimensional thick-generation theorem \textup{(}Proposition~\ref{prop:dk2-thick-generation-typeA}\textup{)}, the fundamental evaluation modules $\{V_{\omega_i}(a)\}$ compactly generate $\operatorname{Rep}_{\mathrm{fd}}(Y(\mathfrak{g}))$ at all~$N$. \smallskip\noindent\textit{Step~2 (Prefundamental stability on the Baxter hyperplane).} Fix a node $i \in \{1, \ldots, N{-}1\}$ of the $A_{N-1}$~Dynkin diagram and let $L^-_{i}(b)$ denote the corresponding negative prefundamental. The singular vector \begin{equation}\label{eq:baxter-sv-prefundamental} w_0 \;=\; v_{\omega_i} \otimes f_i \cdot v_0 \;\in\; V_{\omega_i}(a) \otimes L^-_i(b) \end{equation} (weight $\omega_i - \alpha_i$ in the first factor, weight $-\alpha_i$ in the second) is annihilated by $\Delta(E_j)$ for \emph{every} $j = 1, \ldots, N{-}1$ provided \[ b \;=\; a - \frac{1}{2}. \] Indeed: \begin{itemize}[nosep] \item $j = i$: Proposition~\ref{prop:baxter-yangian-equivariance} specialized to $\lambda = 0$ gives the actual spectral constraint $b = a - 1/2$, and on this hyperplane $\Delta(E_i)\cdot w_0 = 0$. \item $j \neq i$: the commutator $[e_j, f_i] = 0$ (Chevalley--Serre for distinct nodes in any simple Lie algebra), and $e_j \cdot v_{\omega_i} = 0$ (highest-weight property of $V_{\omega_i}$), so every term vanishes. \end{itemize} \noindent This is \textbf{rank-independent}: it uses only the Chevalley--Serre presentation of~$\mathfrak{g}$, not any $\mathfrak{sl}_2$-specific formula. The $\mathfrak{sl}_2$ Baxter sequence therefore survives at $\lambda = 0$ only on the hyperplane $b = a - 1/2$. For the actual shifted-prefundamental generation argument, one uses the generic-parameter exact triangles furnished by the type-$A$ Baxter package (Remark~\ref{rem:baxter-exact-triangles-typeA}), available on a cofinal family of spectral parameters. Thus the shifted prefundamental companions needed in the anti-dominant shifted envelope lie in the thick closure generated by evaluation modules and negative prefundamentals. \smallskip\noindent\textit{Step~3 (Verma from pro-completion).} Every Verma module $M(\lambda)$ of~$Y(\mathfrak{g})$ satisfies $M(\lambda) \simeq R\varprojlim_m W_m$, where the Weyl truncations~$W_m$ are finite-dimensional. The Mittag--Leffler condition holds ($R^1 \varprojlim = 0$; $344$~tests for $\mathfrak{sl}_2$), and each $W_m$ lies in $\operatorname{thick}\langle\{V_{\omega_i}\}\rangle$ by Step~1. The pro-Weyl argument is rank-independent: the transition maps $W_{m+1} \twoheadrightarrow W_m$ are surjective at each weight, independently of~$N$. \smallskip\noindent\textit{Step~4 ($E_1$~compatibility and passage to the shifted envelope).} The $E_1$-braiding $R(u)$ is preserved throughout: the $I$-adic filtration on~$Y(\mathfrak{g})$ is weight-graded (PBW level filtration), hence $R$-compatible. All convergence arguments (sectorwise spectral sequence stabilization, Theorem~\ref{thm:sectorwise-spectral-convergence}, and Mittag--Leffler vanishing) depend only on the weight filtration, not on the braiding data. Under Koszul duality, $R(u) \mapsto R(u)^{-1}$ ($E_1$~inversion, Remark~\ref{rem:yangian-e1-inversion}). \smallskip Since every standard object of $\mathcal{O}^{\mathrm{sh}}_{\leq 0}$ lies in $\widehat{D}(\operatorname{thick}\langle \mathcal{G}_{\mathrm{shift}}\rangle)$ by Steps~2--3, and every object of~$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$ has a finite filtration by standards (BGG), the image of $D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$ in the separated completion is contained in the localizing subcategory generated by $\mathcal{G}_{\mathrm{shift}}$. This is the generation statement proved here. The further passage from this shifted-envelope statement to an identification of the compact objects of the completed category is part of the remaining compact/completion packet; see Conjecture~\ref{conj:dk-compacts-completion}. \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3789
STMT: \begin{theorem}[Type-$A$ MC3 reduction to the compact-completion packet; \ClaimStatusProvedHere] \label{thm:mc3-type-a-resolution} \index{MC3!type-A resolution|textbf} \index{Drinfeld--Kohno!derived!type-A completion} \index{prefundamental!Clebsch--Gordan closure!type A} For $\mathfrak{g} = \mathfrak{sl}_N$ with $N \geq 2$, the old four-package MC3 extension problem is reduced to a single remaining compact-completion packet: \begin{enumerate}[label=\textup{(\roman*)},nosep] \item \emph{Baxter exact triangles.} The TQ relations lift from $K_0$ to derived exact triangles in the completed anti-dominant shifted envelope $\widehat{\mathcal{O}}^{\mathrm{sh}}_{\leq 0}$. The prefundamental Clebsch--Gordan closure $V_n \otimes L^- \cong \bigoplus_{j=0}^{n} L^-(n{-}2j)$ \textup{(}Proposition~\textup{\ref{prop:prefundamental-clebsch-gordan}}\textup{)} provides the structural input. \item \emph{Shifted-prefundamental generation.} Every standard object of $\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g}))$ lies in the thick idempotent-complete closure of $\{V_{\omega_i}(a)\} \cup \{L^-_{i,a}\}$ inside the separated completion, and hence the image of $D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0}(Y(\mathfrak{g})))$ is contained in the localizing subcategory they generate, \textup{(}Theorem~\textup{\ref{thm:shifted-prefundamental-generation}}\textup{)}, proved via the chromatic/conformal-weight filtration reducing to countable finite-dimensional strata. \item \emph{Pro-Weyl recovery.} Standards $M(\Psi)$ are recovered as $R\varprojlim_m W_m$ inside the separated completion, proved via Mittag--Leffler ($R^1\varprojlim = 0$) on Weyl module truncation towers. \item \emph{Remaining packet.} The unresolved step is precisely Conjecture~\ref{conj:dk-compacts-completion}: extending the evaluation-core DK equivalence to the compact shifted-prefundamental core and then comparing that compact-core equivalence with the desired completed/pro-nilpotent category. \end{enumerate} In particular, type~$A$ now leaves a single explicit gap beyond the evaluation-generated core rather than four independent unresolved packets. \end{theorem} 
PROOF: \begin{proof} The four packages are proved in the preceding material: \begin{enumerate}[label=(\roman*),nosep] \item The Baxter exact triangles follow from the categorical prefundamental Clebsch--Gordan decomposition (Proposition~\ref{prop:categorical-cg-typeA}), which upgrades the character-level identity (Proposition~\ref{prop:prefundamental-clebsch-gordan}) to a module-level splitting at generic spectral parameters via the block separation of shifted prefundamental modules. Combined with the rank-independent singular vector construction (Proposition~\ref{prop:baxter-yangian-equivariance}) and naturality on $\mathcal{O}_{\mathrm{poly}}$ (Theorem~\ref{thm:baxter-exact-triangles-opoly}), this gives derived exact triangles in $\widehat{\mathcal{O}}^{\mathrm{sh}}_{\leq 0}$ at a cofinal family of spectral parameters. \item Shifted-prefundamental generation on the shifted envelope is Theorem~\ref{thm:shifted-prefundamental-generation}, proved by the four-step argument: evaluation core (Step~1), Baxter-hyperplane control of the simple-root prefundamental companion together with the generic type-$A$ Baxter package (Step~2), pro-Weyl completion of Vermas (Step~3), and $E_1$-compatibility plus passage to the shifted envelope (Step~4). The further compact-object identification is the separate remaining packet in~(iv). \item Pro-Weyl recovery follows from Step~3 of the Theorem~\ref{thm:shifted-prefundamental-generation} proof: the Mittag--Leffler condition is verified (the transition maps $W_{m+1} \twoheadrightarrow W_m$ are surjective at each weight), and each $W_m$ lies in $\operatorname{thick}\langle\{V_{\omega_i}\}\rangle$ by the evaluation core (Theorem~\ref{thm:eval-core-identification}). \item After~(i)--(iii), the only remaining item from the original MC3 list is the compact/completed extension conjecture \textup{(}Conjecture~\textup{\ref{conj:dk-compacts-completion}}\textup{)}. No further independent type-$A$ obstruction remains on this surface. \end{enumerate} \end{proof} 
---
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:834
STMT: \begin{theorem}[$\Eone$ universality for CY$_3$ chiral algebras] \label{thm:e1-universality-cy3} \ClaimStatusProvedHere{} For any toric CY$_3$ category $\cC$ with $T^3$-equivariant $\Omega$-deformation ($\sigma_3 = h_1 h_2 h_3 \neq 0$, subject to $h_1 + h_2 + h_3 = 0$), the chiral algebra $A_\cC = \Phi(\cC)$ is natively $\Eone$. For compact CY$_3$ without a global torus action, the $\Eone$ nature is expected but requires a different argument; see Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}. Concretely: the $\bS^3$-framing obstruction vanishes topologically ($\pi_3(B\Sp(2m)) = 0$), but the chain-level BV trivialization via holomorphic CS is NOT $\Etwo$-equivariant. The $\Etwo$-braided structure is recovered \emph{only} through the Drinfeld center of the $\Eone$-monoidal representation category (Theorem~\textup{\ref{thm:c3-drinfeld-center}}). \end{theorem} 
exec
/bin/zsh -lc "sed -n '77,110p' /tmp/scope_candidates.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 34

/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:572
STMT: \begin{theorem}[Convergence of bar construction; \ClaimStatusProvedHere]\label{thm:bar-convergence} Let $\mathcal{A}$ be a chiral algebra and write $\bar{B}(\mathcal{A})=\bigoplus_{n\ge0}\bar{B}^n(\mathcal{A})$ with its bar-degree filtration $F_p:=\bigoplus_{n\le p}\bar{B}^n(\mathcal{A})$. Assume $\dim\bar{B}^n(\mathcal{A})<\infty$ for all $n$. Consider: \begin{enumerate} \item \emph{Convergence without completion:} the natural map $\bigoplus_n\bar{B}^n(\mathcal{A})\to\prod_n\bar{B}^n(\mathcal{A})$ is a quasi-isomorphism for the bar differential. \item \emph{Growth bound:} $\limsup_{n\to\infty}\dim(\bar{B}^n(\mathcal{A}))^{1/n}<\infty$. \item \emph{Filtration compatibility:} $d(F_p)\subseteq F_p$ and $d$ lowers bar degree by one on $\gr_F\bar{B}(\mathcal{A})$. \end{enumerate} Then \textup{(2)}$+$\textup{(3)} $\Rightarrow$ \textup{(1)}, and \textup{(1)} $\Rightarrow$ \textup{(3)}. If \textup{(2)} or \textup{(3)} fails, one must use the completed bar complex $\widehat{\bar{B}}(\mathcal{A})$. \end{theorem} 
PROOF: \begin{proof} \emph{(2)+(3) $\Rightarrow$ (1).} Condition (3) gives a filtered complex structure on the direct sum complex and the associated spectral sequence has \[ E_0^{p,\bullet}=\bar{B}^p(\mathcal{A}), \qquad d_0:\bar{B}^p\to\bar{B}^{p-1}. \] Because each $\bar{B}^p$ is finite-dimensional and condition (2) gives uniform at-most-exponential growth, each total degree receives only finite-dimensional contributions, so the filtered spectral sequence is well-defined and converges to $H^*(\bar{B}(\mathcal{A}))$. Thus no topological completion is required. Together with Theorem~\ref{thm:conilpotency-convergence}, this means every iterated coproduct/differential expression is finite on each element. \emph{(1) $\Rightarrow$ (3).} If convergence holds in the uncompleted direct sum, $d$ cannot create infinitely many bar-degree components from a single homogeneous input; equivalently, $d(F_p)\subseteq F_p$ and the induced differential on $\gr_F$ is degree $-1$. Otherwise $d$ is only defined in the product completion. \emph{Remark on the growth bound.} Condition~(2) is sufficient for~(1) given~(3), but not necessary in general: an algebra can converge without completion even when $\dim\bar{B}^n$ grows super-exponentially, provided the differential kills enough cohomology. Condition~(2) guarantees that the Mittag-Leffler condition holds for the tower $\{F_p\}_{p \geq 0}$, which by the Milnor exact sequence ensures $\mathrm{lim}^1 = 0$ and hence the comparison quasi-isomorphism. \emph{Quadratic finite-type case.} For $\mathcal{A}=T(V)/(R)$ with $V$ finite-dimensional, $\bar{B}^n(\mathcal{A})\cong (sV)^{\otimes n}$, so (2) holds with growth constant $\dim V$, and (3) holds by definition of the bar filtration. Therefore quadratic finite-type algebras converge without completion. \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:801
STMT: \begin{theorem}[Genus extension hierarchy; \ClaimStatusProvedHere] \label{thm:genus-extension-hierarchy} \index{genus extension hierarchy|textbf} \index{bar complex!genus extension levels} \index{Koszul locus!genus extension} \index{modular functor!genus extension level} The genus extension of the bar complex admits a five-level hierarchy of successively stronger structural conditions. Each level is strictly contained in the next, and the standard landscape satisfies all five. \begin{enumerate}[label=\textup{(\roman*)}] \item \emph{Algebraic \textup{(}bar $D^2=0$ at all genera\textup{)}.}\; For \emph{any} chiral algebra $\cA$, the bar differential satisfies $D_\cA^2 = 0$ at all genera, and the universal MC element $\Theta_\cA := D_\cA - d_0 \in \MC(\gAmod)$ exists unconditionally \textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}. No finiteness or Koszulness condition is required: $D^2 = 0$ is a formal consequence of $\partial^2 = 0$ on $\overline{\cM}_{g,n}$. \item \emph{Homotopical \textup{(}bar-cobar inversion in $D^{\mathrm{co}}$\textup{)}.}\; If $\cA$ has finite-dimensional weight spaces \textup{(}the positive-energy axiom\textup{)}, then the genus-$g$ bar-cobar adjunction $\barBch_g \dashv \Omegach_g$ extends to an equivalence in the coderived category $D^{\mathrm{co}}$ \textup{(}Appendix~\textup{\ref{app:coderived-models})}. The positive-energy condition ensures the weight-by-weight SDR exists and the homotopy transfer theorem produces the transferred $A_\infty$ structure on $H^*(\barBch(\cA))$ at each genus. \item \emph{Koszul \textup{(}chiral bar-cobar quasi-isomorphism\textup{)}.}\; If $\cA$ satisfies MK1 \textup{(}genus-$0$ Koszulness\textup{)}, equivalently the PBW spectral sequence collapses at $E_2$ \textup{(}Theorem~\textup{\ref{thm:koszul-equivalences-meta})}, then the counit $\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism in the ordinary derived category \textup{(}Theorem~\textup{\ref{thm:higher-genus-inversion})}. On the Koszul locus, the bar and cobar functors are inverse equivalences: the genus-$g$ bar complex is a resolution of~$\cA$, not merely a coderived model. \item \emph{Analytic \textup{(}convergent partition functions\textup{)}.}\; If $\cA$ satisfies the HS-sewing criterion (polynomial OPE growth and subexponential sector growth) then the genus-$g$ partition functions $Z_g(\cA)$ converge absolutely for all $g \geq 1$ \textup{(}Theorem~\textup{\ref{thm:general-hs-sewing})}. The sewing envelope $\cA^{\mathrm{sew}}$ carries the completed analytic bar coalgebra, and the shadow obstruction tower evaluates to convergent numerical invariants. \item \emph{Modular functor \textup{(}finite-dimensional conformal blocks\textup{)}.}\; If $\cA$ is $C_2$-cofinite in the sense of Zhu~\cite{Zhu96}, then the spaces of conformal blocks $\mathcal{V}_g(\cA)$ are finite-dimensional for all $g$, the modular group $\mathrm{SL}_2(\mathbb{Z})$ acts on characters, and $\cA$ defines a modular functor. This is the strongest condition; it implies all four preceding levels. \end{enumerate} The first four levels form a strict chain: $\textup{(iv)} \subsetneq \textup{(iii)} \subsetneq \textup{(ii)} \subsetneq \textup{(i)}$. Level~\textup{(v)} \textup{(}$C_2$-cofinite\textup{)} implies \textup{(iv)}, \textup{(ii)}, and \textup{(i)}, but its relation to \textup{(iii)} \textup{(}Koszul\textup{)} is not one of containment: $C_2$-cofinite simple quotients $L_k(\fg)$ at admissible level satisfy~\textup{(v)} but may not satisfy~\textup{(iii)}, while Koszul universal algebras $V^k(\fg)$ at generic level satisfy~\textup{(iii)} but not~\textup{(v)}. Every chiral algebra satisfies~\textup{(i)}. Every positive-energy chiral algebra satisfies \textup{(i)}--\textup{(ii)}. The standard landscape \textup{(}Heisenberg, affine Kac--Moody at non-critical level, $\cW$-algebras at generic central charge, $\beta\gamma$ and $bc$ systems\textup{)} satisfies levels \textup{(i)}--\textup{(iv)}; those that are also $C_2$-cofinite satisfy all five. \end{theorem} 
PROOF: \begin{proof} Level~(i) is Theorem~\ref{thm:mc2-bar-intrinsic}: $D_\cA^2=0$ holds universally because the bar differential is the Feynman-transform differential of a modular operad algebra, and $\partial^2=0$ on $\overline{\cM}_{g,n}$ implies $D^2=0$ by the codimension-$2$ boundary cancellation. Level~(ii): the positive-energy axiom gives $\cA = \bigoplus_{n \geq 0} \cA_n$ with $\dim \cA_n < \infty$. The weight-by-weight SDR (Cliff~\cite[Proposition~8.1]{Cliff19}) applies at each genus to produce the transferred structure in $D^{\mathrm{co}}$; the key input is that the homotopy transfer theorem requires only finite-dimensional weight spaces, not Koszulness. Level~(iii): MK1 (PBW collapse at $E_2$) implies diagonal Ext vanishing, which is the hypothesis of Theorem~\ref{thm:higher-genus-inversion}. On the Koszul locus, the curved bar complex $(\barBch(\cA), \dfib)$ and the flat model $(\barBch(\cA), \Dg{g})$ are linked by the coderived-to-derived comparison (Proposition~\ref{prop:gauss-manin-uncurving-chain}), and the counit is a quasi-isomorphism in the ordinary derived category. The passage from coderived to derived is the content of genus-$0$ Koszulness. Level~(iv): the HS-sewing criterion (Theorem~\ref{thm:general-hs-sewing}) is a growth condition on OPE coefficients, strictly weaker than $C_2$-cofiniteness. The standard families satisfy it because they have polynomial OPE growth (OPE coefficients are polynomial in conformal weights) and subexponential sector growth (the graded dimension $\dim \cA_n$ grows at most polynomially). Level~(v): $C_2$-cofiniteness implies, by Zhu's theorem~\cite{Zhu96}, that the space of genus-$g$ conformal blocks is finite-dimensional and carries a projectively flat connection. This implies convergent partition functions (hence level~(iv)), finite-dimensional weight spaces (hence level~(ii)), and $D^2=0$ (which is universal). Whether $C_2$-cofiniteness implies Koszulness \textup{(}level~\textup{(iii))} is a separate question: for simple quotients $L_k(\fg)$ at admissible level, $C_2$-cofiniteness holds but Koszulness is open for rank~$\geq 2$ \textup{(}Remark~\textup{\ref{rem:admissible-koszul-status})}. The inclusion \textup{(v)} $\subsetneq$ \textup{(iv)} is strict; the relation of \textup{(v)} to \textup{(iii)} is not one of containment. The inclusions are strict. For (i)$\neq$(ii): a chiral algebra with infinite-dimensional weight spaces (e.g.\ a vertex algebra without the positive-energy axiom) satisfies $D^2=0$ but lacks the SDR needed for homotopy transfer. For (ii)$\neq$(iii): a positive-energy chiral algebra that is not chirally Koszul (e.g.\ simple quotients at certain admissible levels where bar-Ext$\neq$ordinary-Ext) has the coderived model but not the derived quasi-isomorphism. For (iii)$\neq$(iv): the HS-sewing criterion (Theorem~\ref{thm:general-hs-sewing}) requires polynomial OPE growth, which is a growth-rate condition independent of Koszulness; a chirally Koszul algebra with super-polynomial OPE growth satisfies~(iii) but not~(iv). For (iv)$\neq$(v): the universal $\cW$-algebra $V^k(\fg)$ at generic irrational level satisfies HS-sewing (convergent partition functions) but is not $C_2$-cofinite (conformal blocks are infinite-dimensional). \end{proof} 
---
/Users/raeez/chiral-bar-cobar/chapters/theory/nilpotent_completion.tex:947
STMT: \begin{theorem}[Resonance completion; \ClaimStatusProvedHere] \label{thm:platonic-completion}% \index{platonic completion theorem|textbf}% \index{resonance rank!finiteness|textbf}% Every separated complete chiral $A_\infty$-algebra $\cA$ obtained by a weight-preserving homological transfer from a positive-energy chiral algebra admits a canonical decomposition \[ \cA \cong R_\cA \;\widehat{\oplus}\; \cA^+_\cA \] where $\cA^+_\cA$ satisfies stabilized completion \textup{(}Theorem~\textup{\ref{thm:stabilized-completion-positive})} and $R_\cA$ is finite-dimensional. The completed reduced bar coalgebra is then \[ \widehat{\bar B}(\cA) \simeq \widehat{\bar B}^{\mathrm{st}}(\cA^+_\cA) \;\widehat{\otimes}\; \bar B(R_\cA), \] and the completed cobar recovers~$\cA$. For $\mathcal{W}_{1+\infty}$, affine Yangians, and positive RTT towers, one has $R_\cA = 0$. For Virasoro and non-quadratic $\mathcal{W}$-families, one has $0 < \dim R_\cA < \infty$. The same-family shadow $\mathrm{Vir}_{26-c}$ is the image of the resonance truncation~$R_\cA$, while the genuine $\mathcal{W}_\infty$-type dual is recovered only from the full completed object. \end{theorem} 
PROOF: \begin{proof} Fix a positive-energy chiral algebra $\mathcal V$ whose weight-preserving transferred $A_\infty$-model is~$\cA$. Write \[ \mathcal V = \prod_{h \ge 0} V_h, \qquad H_h := H^*(V_h, m_1|_{V_h}), \qquad H := \prod_{h \ge 0} H_h. \] Choose a strong deformation retract on each weight space and assemble them into a weight-preserving SDR \[ (\mathcal V, H, p, \iota, h). \] By the homotopy transfer theorem \textup{(}Theorem~\ref{thm:htt}\textup{)}, $H$ inherits transferred operations $\tilde m_k$, and by construction $\cA = (H, \{\tilde m_k\})$. \emph{Step~1: Reduced weight is preserved on the positive sector.} For $x \in H_h$ with $h > 0$, define the reduced weight \[ \nu(x) := h - 1. \] The binary chiral product lowers conformal weight by exactly~$1$: if $a \in H_{h(a)}$ and $b \in H_{h(b)}$, then the residue product has weight $h(a) + h(b) - 1$. Each planar tree contributing to $\tilde m_k$ has $k-1$ internal vertices, so for homogeneous $x_i \in H_{h_i}$ one has \[ h\bigl(\tilde m_k(x_1, \ldots, x_k)\bigr) = \sum_{i=1}^k h_i - (k-1) \qquad (k \ge 2). \] Hence \[ \nu\bigl(\tilde m_k(x_1, \ldots, x_k)\bigr) = \sum_{i=1}^k \nu(x_i) \qquad (k \ge 2). \] Since $H$ is cohomology, the transferred differential vanishes: $\tilde m_1 = 0$. The transferred curvature $\tilde m_0$ has conformal weight~$0$. Set \[ R_\cA := H_0, \qquad \cA^+_\cA := \prod_{h > 0} H_h. \] Then $\cA = R_\cA \;\widehat{\oplus}\; \cA^+_\cA$. The formula above shows that $\cA^+_\cA$ is closed under all $\tilde m_k$ with $k \ge 1$, because if every input has conformal weight at least~$1$, then the output has conformal weight at least~$1$ as well. On $\cA^+_\cA$, the transferred curvature is zero, so the curvature clause in Theorem~\ref{thm:stabilized-completion-positive} is vacuous. Each reduced-weight truncation \[ (\cA^+_\cA)_{\le N}^{\nu} := \prod_{0 \le \nu \le N} (\cA^+_\cA)_\nu = \prod_{1 \le h \le N+1} H_h \] is finite-dimensional, hence lies in the finite-type bar-cobar regime. Therefore Theorem~\ref{thm:stabilized-completion-positive} applies to $\cA^+_\cA$ with respect to the reduced weight~$\nu$. \emph{Step~2: The resonance piece is finite-dimensional and curved.} By positive energy, each $V_h$ is finite-dimensional. Therefore each $H_h$ is finite-dimensional, in particular $R_\cA = H_0$ is finite-dimensional. If all inputs lie in $H_0$ and $k \ge 2$, then the conformal-weight formula from Step~1 gives \[ h\bigl(\tilde m_k(x_1, \ldots, x_k)\bigr) = -(k-1) < 0, \] which is impossible in a positive-energy theory. Hence \[ \tilde m_k|_{R_\cA^{\otimes k}} = 0 \qquad (k \ge 2). \] Since $\tilde m_1 = 0$ and $\tilde m_0 \in R_\cA$, the resonance piece is a finite-dimensional curved $A_\infty$-subalgebra. Its resonance rank is therefore \[ \rho(\cA) = \dim H^*(R_\cA, \tilde m_1) = \dim R_\cA < \infty. \] \emph{Step~3: The mixed differential is topologically nilpotent.} Consider the completed tensor product \[ \widehat{\bar B}^{\mathrm{res}}(\cA) = \widehat{\bar B}^{\mathrm{st}}(\cA^+_\cA) \;\widehat{\otimes}\; \bar B(R_\cA). \] For a bar word, define its \emph{positive conformal weight} $w_+$ to be the sum of the conformal weights of the $\cA^+_\cA$-entries. The differential splits as $D = D^+ + D_R + D_{\mathrm{mix}}$, where $D^+$ uses only operations on~$\cA^+_\cA$, $D_R$ uses only operations on $R_\cA$, and $D_{\mathrm{mix}}$ contains the remaining terms. If a mixed operation involves $r \ge 1$ positive inputs of weights $h_1, \ldots, h_r$ and $s \ge 1$ resonance inputs, then \[ h_{\mathrm{out}} = \sum_{i=1}^r h_i - (r+s-1) \le \sum_{i=1}^r h_i - 1. \] So any mixed operation with at least one resonance input lowers positive conformal weight by at least~$1$. If all inputs are positive, then $h_{\mathrm{out}} \ge 1$, so the output remains in $\cA^+_\cA$ and the term belongs to~$D^+$, not to $D_{\mathrm{mix}}$. Consequently $D_{\mathrm{mix}}$ lowers $w_+$ by at least~$1$ on every term to which it contributes. Therefore, for a bar chain of positive conformal weight~$w$, \[ D_{\mathrm{mix}}^n = 0 \qquad\text{for } n > w. \] This is the required topological nilpotence. The perturbation argument used in the proof of Theorem~\ref{thm:resonance-filtered-bar-cobar} depends only on that nilpotence, so it applies here with the decreasing filtration \[ \mathcal F^p := \{\text{bar chains of positive conformal weight } \le p\}. \] Combining this with Step~1 gives \[ \widehat{\bar B}(\cA) \simeq \widehat…3204 tokens truncated…ean Lagrangian intersection), so $r_{\max} = 2$ and the $A_\infty$-chiral structure is formal. Class~$\mathbf{L}$: $m_3 \ne 0$ from the Lie bracket but $m_{k \ge 4} = 0$ on cohomology (Jacobi closes the obstruction), so $r_{\max} = 3$ and the structure is formal. Class~$\mathbf{C}$: $m_4 \ne 0$ from the contact term but the tower terminates at $r_{\max} = 4$ by rank-one abelian rigidity, so the structure is formal. Class~$\mathbf{M}$: $m_k \ne 0$ for all $k \ge 3$ on cohomology (the quartic pole manufactures a propagating obstruction), so $r_{\max} = \infty$ and the $A_\infty$-chiral structure is \emph{non-formal}. \emph{Ordered Koszul duals.} For affine $\widehat{\mathfrak{g}}_k$: the ordered Koszul dual is the Yangian $Y_\hbar(\mathfrak{g})$ (Volume~II, Theorem~\ref*{thm:Koszul_dual_Yangian}). For Virasoro and $\mathcal{W}_N$: the ordered Koszul dual is the dg-shifted Yangian $Y^{\mathrm{dg}}$, a dg algebra with infinitely many cohomological generators reflecting non-formality (Volume~II, Part~VII). For $\beta\gamma$/$bc$: the Koszul duality exchanges statistics ($bc^! = \beta\gamma$, $\beta\gamma^! = bc$), so the line-side algebra is the dual free-field system. All entries are chirally Koszul (bar cohomology concentrated), as established by PBW universality (Volume~I) and the one-loop exactness criterion (Volume~II, Theorem~\ref*{thm:one-loop-koszul}). \end{proof} 
---
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex:768
STMT: \begin{theorem}[Class M reconstruction; \ClaimStatusProvedHere] % label removed: thm:class-m-reconstruction Let $\cA = \mathrm{Vir}_c$ be the universal Virasoro algebra at central charge $c$. Then: \begin{enumerate}[label=\textup{(\roman*)}] \item $r_{\max}(\mathrm{Vir}_c) = \infty$ (mixed/infinite shadow depth). \item The shadow jet space has infinite-dimensional fibers: $\dim \cA^{\mathrm{sh}}_{r,0} \geq 1$ for all $r \geq 2$. \item The jet data through degree $8$ is: \end{enumerate} \end{theorem} 
PROOF: \begin{proof}[Proof of {\textup{(iii)}}] We compute $J^r(\mathrm{Vir}_c)$ for $r = 2, \ldots, 8$. \medskip\noindent\textbf{Degree $2$ ($J^2$).} The curvature is $\kappa(\mathrm{Vir}_c) = c/2$. The quadratic jet is one-dimensional: \[ J^2(\mathrm{Vir}_c) = \C \cdot \kappa, \qquad \kappa = c/2. \] \medskip\noindent\textbf{Degree $3$ ($J^3$).} The cubic shadow $\mathfrak{C}(\mathrm{Vir}_c)$ is gauge-trivial: $[\mathfrak{C}] = 0 \in H^1(F^3/F^4, d_2)$. This follows from $H^1(F^3/F^4, d_2) = 0$ for Virasoro, which holds because the relevant Chevalley--Eilenberg cohomology of the Virasoro Lie algebra vanishes at the correct degree. After gauge transformation, the cubic contribution is absorbed. Thus: \[ J^3(\mathrm{Vir}_c) = J^2(\mathrm{Vir}_c), \qquad \cA^{\mathrm{sh}}_{3,0} = 0 \;\text{(after gauge)}. \] \medskip\noindent\textbf{Degree $4$ ($J^4$).} The quartic contact shadow is nonzero: \[ \mathfrak{Q}^{\mathrm{contact}}_{\mathrm{Vir}} = \frac{10}{c(5c+22)}. \] This is the canonical quartic class, independent of the gauge choice for the cubic term (Vol~I, Theorem~\ref*{thm:cubic-gauge-triviality}). The quartic jet is two-dimensional: \[ J^4(\mathrm{Vir}_c) = \C \cdot \kappa \oplus \C \cdot \mathfrak{Q}^{\mathrm{contact}}, \qquad \dim J^4 = 2. \] \medskip\noindent\textbf{Degree $5$ ($J^5$).} The quintic obstruction class $o_5(\mathrm{Vir}_c)$ is nonzero. This is the fundamental distinction between class~C and class~M: the Virasoro algebra has a nonvanishing quintic shadow. The proof is by direct computation: the cyclic contraction \[ o_5 = \sum_{\Gamma \in \mathsf{Gr}_5^{\mathrm{tree}}} \frac{1}{|\Aut(\Gamma)|}\, \Phi^{\mathrm{Vir}}_\Gamma \] sums over binary trees with five leaves, and at least one term is nonzero because the Virasoro composite $:(L_{-2})^2 L:$ generates a nonvanishing degree-$5$ cyclic trace. Therefore: \[ \dim \cA^{\mathrm{sh}}_{5,0} \geq 1, \qquad o_5 \neq 0. \] \medskip\noindent\textbf{Degree $6$ ($J^6$).} The degree-$6$ shadow receives contributions from two sources: trees with six leaves decorated by $m_2$ and $m_3$, and the first planted-forest correction at degree $6$. The dimension is $\dim \cA^{\mathrm{sh}}_{6,0} \geq 1$. \medskip\noindent\textbf{Degree $7$ ($J^7$).} Similar analysis: $\dim \cA^{\mathrm{sh}}_{7,0} \geq 1$. The degree-$7$ shadow is the first level at which a genuinely new geometric stratum (the codimension-$5$ boundary of $\ov{\M}_{0,8}$) contributes. \medskip\noindent\textbf{Degree $8$ ($J^8$).} At degree $8$, the shadow has $\dim \cA^{\mathrm{sh}}_{8,0} \geq 2$: the quartic-quartic interaction $\mathfrak{Q} \cdot \mathfrak{Q}$ generates a new independent shadow class beyond the cascading contributions from lower degrees. The dimension table is: \[ \renewcommand{\arraystretch}{1.3} \begin{array}{c|c|c|c|c|c|c|c} r & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ \hline \dim \cA^{\mathrm{sh}}_{r,0}(\mathrm{Vir}_c) & 1 & 0 & 1 & 1 & 1 & 1 & \geq 2 \\ \dim J^r(\mathrm{Vir}_c) & 1 & 1 & 2 & 3 & 4 & 5 & \geq 7 \end{array} \] \end{proof} 
---
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_fm_calculus_extensions.tex:1282
STMT: \begin{theorem}[$\mathcal{W}_3$ $\Ainf$ structure; \ClaimStatusProvedHere] % label removed: thm:w3-ainf Let $\mathcal{W}_3$ at central charge $c$ be generated by the stress tensor $T$ (weight $2$) and the primary $W$ (weight $3$), with $\lambda$-brackets \begin{align} \{T{}_\lambda T\} &= \partial T + 2T\lambda + \frac{c}{12}\lambda^3, % label removed: eq:w3-TT \\ \{T{}_\lambda W\} &= \partial W + 3W\lambda, % label removed: eq:w3-TW \\ \{W{}_\lambda W\} &= \partial\Lambda + 2\Lambda\lambda + \frac{c}{3\cdot 5!}\lambda^5 + \beta\!\left[\partial T + 2T\lambda + \frac{c}{12}\lambda^3\right] \cdot \lambda, % label removed: eq:w3-WW \end{align} where $\Lambda = \frac{2}{3}(T \cdot T - \frac{3}{10}\partial^2 T)$ is the quasiprimary composite field (the Zamolodchikov normal-ordered composite), $\beta = 16/(22 + 5c)$ is the Zamolodchikov coefficient, and the $\lambda^5$ term in the $W$-$W$ OPE corresponds to a sextic pole. Then: \begin{enumerate}[label=\textup{(\roman*)}] \item The binary operation on $(W, W)$ has leading term \begin{equation}% label removed: eq:w3-m2-WW m_2(W,W;\, \lambda) = \frac{c}{360}\lambda^5 + \beta\!\left[\frac{c}{12}\lambda^3 + 2T\lambda + \partial T\right] \cdot \lambda + 2\Lambda\lambda + \partial\Lambda. \end{equation} The sextic pole $c/(360)\,\lambda^5$ is the engine driving the extended tower. \item The ternary operation $m_3(W,W,W)$ is nonzero: the sextic pole generates a non-vanishing associator $A_3(W,W,W) \ne 0$ with leading term proportional to $c\,\lambda_1\lambda_2^5$ and $21$ sub-leading monomials in $\lambda_1, \lambda_2$. \item The quartic operation $m_4(W,W,W,W)$ is nonzero for generic $c$, with quartic contact invariant proportional to $1/(c(5c+22)(7c+68))$, involving the Kac determinant at level $6$. \item $m_k \ne 0$ for all $k \ge 3$ and generic $c$. Shadow depth $r_{\max} = \infty$ (mixed archetype), with the same qualitative behavior as Virasoro but higher-order pole structure. \end{enumerate} \end{theorem} 



thinking
**Evaluating theorem findings**

I'm considering if the higher genus foundations theorem is valid, but the ordered associative chiral kd frontier might not be solid. I’ve identified about six findings that seem relevant, including hdm-seven-way-master and general-bps. 

It could be worthwhile to include the higher genus foundations if there's a scope issue. The standard landscape proves the level IV families are satisfied, which seems fine. I’m also thinking about the universality of G since it emphasizes a broad assertion. More precise lines will be needed for clarity.
thinking
**Analyzing theorem references**

I'm considering if the thm: general-nahc and general-bps are in the same file and both clear. The thm: e1-universality-cy3 might be stronger since later remarks clarify specifics. I should reference the remark lines 909-913, as the problem seems grounded there. 

For clarity, I need a precise file:line format, and I could cite either the theorem line or relevant proof lines. I might want to use the starting line of the theorem and include where the critical proof sentence occurs for accuracy.
thinking
**Gathering proof segments**

I’m focused on the need for exact lines in the theorem and the example-only proof from the arithmetic shadows document. To do this effectively, I should use the `nl -ba` command around the candidate sections to identify the precise spots I need. It seems like a systematic approach to ensure I gather the necessary information accurately. Let’s get cracking on that!
codex
I’ve narrowed the report to findings with explicit textual evidence, not mere suspicion. Final pass now is line-accurate extraction so each finding lands with a concrete patch target instead of a vague chapter-level complaint.
exec
/bin/zsh -lc "nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '3996,4040p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '4716,4760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '722,752p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/arithmetic_shadows.tex | sed -n '5070,5130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex | sed -n '113,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '208,278p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '834,918p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3996	propagator is well-defined.
  3997	\end{proof}
  3998	
  3999	\begin{theorem}[General shadow triple]
  4000	\label{thm:general-nahc}
  4001	\ClaimStatusProvedHere
  4002	\index{shadow triple!general}
  4003	For \emph{every} chirally Koszul algebra~$\cA$ with $N$ strong
  4004	generators, the shadow tower carries a triple of compatible
  4005	structures $(\Theta_\cA,\, M_\cA,\, h_\cA)$:
  4006	\textup{(A)}~the MC element $\Theta_\cA$ with
  4007	$D_\Theta^2 = 0$ \textup{(}flat side\textup{)};
  4008	\textup{(B)}~the shadow Higgs field
  4009	$M_\cA(t_1,\dotsc,t_N)$, an $N \times N$ matrix whose spectral
  4010	variety is the shadow generating function's algebraic locus
  4011	\textup{(}Higgs side\textup{)};
  4012	\textup{(C)}~the Shapovalov form
  4013	$h_\cA = (\langle\bar{a}_i,\bar{a}_j\rangle)$ on
  4014	$H^*(\barB(\cA))$, whose inverse $P = h^{-1}$ is the
  4015	propagator \textup{(}harmonic side\textup{)}.
 succeeded in 53ms:
  4716	\end{remark}
  4717	
  4718	\begin{theorem}[General BPS spectrum of the shadow obstruction tower]
  4719	\label{thm:general-bps}
  4720	\ClaimStatusProvedHere
  4721	\index{BPS spectrum!general construction}
  4722	Let $\cA$ be a finitely strongly generated vertex algebra with
  4723	invariant bilinear form. The shadow tower defines a BPS spectrum
  4724	$\Omega_r(\cA) := S_r(\cA)$ whose plethystic logarithm
  4725	$\operatorname{PLog}(\sum \Omega_r t^r) = \sum p_r(\cA)\,t^r$
  4726	identifies the primitive BPS states: $p_r \neq 0$ iff the shadow
  4727	tower has an independent primitive at charge~$r$. The
  4728	construction requires only:
  4729	\textup{(a)}~$\Theta_\cA$ exists
  4730	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic}}\textup{)};
  4731	\textup{(b)}~an invariant bilinear form \textup{(}for the cyclic
  4732	structure on $\Defcyc$\textup{)};
  4733	\textup{(c)}~the transferred $A_\infty$ structure on
  4734	$H^*(\barB(\cA))$.
  4735	These hold for \emph{every} finitely strongly generated vertex
 succeeded in 53ms:
   722	\begin{theorem}[Seven-way master theorem; \ClaimStatusProvedHere]
   723	\label{thm:hdm-seven-way-master}
   724	\index{seven faces!master theorem|textbf}
   725	\index{collision residue!seven-way master|textbf}
   726	For every modular Koszul chiral algebra $\cA$, the seven faces
   727	$(\mathrm{F}1)$--$(\mathrm{F}7)$ of $r_\cA(z)$ are equal as elements
   728	of $\mathrm{End}_\cA(2)[\![z^{-1}]\!]$ after the standard
   729	normalization. Concretely, the master equation
   730	\begin{equation}\label{eq:hdm-master-equation}
   731	\boxed{\;
   732	r_\cA(z)
   733	\;=\;
   734	\pi_\cA
   735	\;=\;
   736	r^{\mathrm{DNP}}(z)
   737	\;=\;
   738	\sum_{n \geq 0} \frac{\mathrm{cl}(a_{(n)}b)}{z^{n+1}}
   739	\;=\;
   740	H_i^{\mathrm{GZ}}\bigr|_{j\textrm{-coeff}}
   741	\;=\;
 succeeded in 53ms:
  5070	measure~$\rho$ encodes the MC data of~$\Theta_\cA$, and $G$
  5071	is its moment generating function.
  5072	
  5073	\begin{theorem}[Universality of $G$]%
  5074	\label{thm:universality-of-G}%
  5075	\ClaimStatusProvedHere%
  5076	\index{shadow generating function!universal structure}
  5077	For any chirally Koszul algebra~$\cA$ with HS-sewing, the
  5078	connected genus-$1$ free energy admits the factorization
  5079	\begin{equation}\label{eq:universality-factorization}
  5080	 F_1^{\mathrm{conn}}(q;\,\cA)
  5081	 \;=\;
  5082	 G_\cA\!\bigl(t(q)\bigr),
  5083	 \qquad
  5084	 G_\cA(t)
  5085	 \;=\;
  5086	 \int\!\log(1 - \lambda\,t)\,d\rho_\cA(\lambda),
  5087	\end{equation}
  5088	where $G_\cA$ depends only on the spectral measure~$\rho_\cA$
  5089	\textup{(}determined by the algebraic data of~$\cA$: the OPE and
 succeeded in 53ms:
   208	\begin{theorem}[RTT R-matrices for all classical types; \ClaimStatusProvedHere]
   209	\label{thm:rtt-all-classical-types}
   210	\index{Yangian!RTT!all classical types}
   211	\index{R-matrix!all classical types}
   212	The RTT presentation extends to all classical Lie types
   213	$A_n, B_n, C_n, D_n$ via the collision residue
   214	$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
   215	of the bar-complex MC element. In each case, the $R$-matrix
   216	acts on $V \otimes V$ where $V$ is the fundamental representation,
   217	and the operators $P$, $Q$, $K$ satisfy the identities recorded below.
   218	\begin{enumerate}[label=\textup{(\roman*)}]
   219	\item \emph{Type $A_n$ $(\mathfrak{sl}_{n+1}$, $V = \bC^{n+1})$.}
   220	 The Yang $R$-matrix is
   221	 \begin{equation}\label{eq:rmatrix-type-a}
   222	 R(u) = u\, \mathbb{1} + P,
   223	 \end{equation}
   224	 where $P$ is the permutation operator on $V \otimes V$.
   225	 The corresponding Casimir is $\Omega = P - \mathbb{1}/N$
   226	 with $N = n+1$, so in the KZ normalisation the classical $r$-matrix at affine
   227	 level $k$ reads
 succeeded in 53ms:
   113	\begin{theorem}[CY complementarity at $d = 2$]
   114	\label{thm:cy-complementarity-d2}
   115	\ClaimStatusProvedHere
   116	Let $\cC$ be a smooth proper cyclic $A_\infty$-category of CY dimension $d = 2$ with Serre duality $\mathbb{S}_\cC \simeq [2]$, and let $A_\cC = \Phi(\cC)$ be its quantum chiral algebra (CY-A at $d = 2$, PROVED). Let $\cC^!$ denote the Koszul dual CY$_2$ category (for $\cC = D^b(\Coh(X))$ with $X$ a K3 surface, $\cC^! \simeq \Fuk(X)$ under homological mirror self-duality). Then:
   117	\begin{enumerate}[label=\textup{(C1$^{\mathrm{CY}}$)}]
   118	 \item \emph{Eigenspace complementarity.} For every genus $g \geq 1$ and every degree $n \geq 1$ with $2g - 2 + n > 0$, the genus-$g$ shadow complex satisfies
   119	 \[
   120	 Q_g^n(A_\cC) \;\oplus\; Q_g^n(A_{\cC^!})
   121	 \;\simeq\; H^\bullet\!\bigl(\overline{\cM}_{g,n},\, \cZ^{\mathrm{der}}_{\mathrm{ch}}(A_\cC)\bigr),
   122	 \]
   123	 as a direct sum of $\pm 1$ eigenspaces for the Verdier involution induced by Serre duality on $D^b(\Coh(\cC))$. This is unconditional in the CY$_2$ case.
   124	\end{enumerate}
   125	\begin{enumerate}[label=\textup{(C2$^{\mathrm{CY}}$)}]
   126	 \item \emph{Scalar complementarity} (\emph{} scope). Under the CY uniform-weight hypothesis (all generating fields of $A_\cC$ at equal conformal weight) \emph{and} in the free-field/lattice Koszul class (the KM/Heisenberg branch , where the Koszul conductor $K = c(A_\cC) + c(A_{\cC^!})$ vanishes),
   127	 \[
   128	 \kappa_{\mathrm{ch}}(A_\cC) \,+\, \kappa_{\mathrm{ch}}(A_{\cC^!}) \;=\; 0 \qquad \text{(free-field/KM class)}.
   129	 \]
   130	 Away from the free-field class, the sum equals the family-dependent Koszul conductor and is nonzero in general: for the Virasoro class the analogous sum is $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 13$ (not $0$), and for $\cW_N$ it equals $c \cdot (H_N - 1)$ where $H_N = \sum_{j=1}^{N} 1/j$. For $\cC = D^b(\Coh(K3))$ specifically, $\kappa_{\mathrm{ch}}(\cA_{K3}) = \chi^{\CY}(K3) = 2$ (Theorem~CY-D, \S\ref{sec:cy-trace-kappa}); the relevant chiral algebra is the $\widehat{\mathfrak{sl}}_2$ subalgebra at level $k = 1$ of the $\cN = 4$ superconformal algebra, which lies in the free-field/KM class with $K = 0$, so the Verdier involution induced by the Mukai pairing gives $\kappa_{\mathrm{ch}}' = -2$ and the scalar sum vanishes: $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ (K3 value, free-field/KM branch; NOT universal across all CY$_2$ categories).
   131	\end{enumerate}
   132	\end{theorem}
 succeeded in 50ms:
   834	\begin{theorem}[$\Eone$ universality for CY$_3$ chiral algebras]
   835	\label{thm:e1-universality-cy3}
   836	\ClaimStatusProvedHere{}
   837	For any toric CY$_3$ category $\cC$ with $T^3$-equivariant $\Omega$-deformation ($\sigma_3 = h_1 h_2 h_3 \neq 0$, subject to $h_1 + h_2 + h_3 = 0$), the chiral algebra $A_\cC = \Phi(\cC)$ is natively $\Eone$. For compact CY$_3$ without a global torus action, the $\Eone$ nature is expected but requires a different argument; see Conjecture~\textup{\ref{conj:cy-to-chiral-d3}}.
   838	
   839	Concretely: the $\bS^3$-framing obstruction vanishes topologically ($\pi_3(B\Sp(2m)) = 0$), but the chain-level BV trivialization via holomorphic CS is NOT $\Etwo$-equivariant. The $\Etwo$-braided structure is recovered \emph{only} through the Drinfeld center of the $\Eone$-monoidal representation category (Theorem~\textup{\ref{thm:c3-drinfeld-center}}).
   840	\end{theorem}
   841	
   842	\begin{proof}
   843	Four independent pillars, each sufficient to establish the $\Eone$ nature.
   844	
   845	\medskip
   846	\noindent\textbf{Pillar (a): Abelianity of the classical bracket.}
   847	By Theorem~\ref{thm:c3-abelian-bracket}, the $\GL(3)$-invariant Schouten--Nijenhuis brackets on $\PV^*(\C^3)$ all vanish. The classical Lie conformal algebra is therefore abelian: it carries no Lie bracket, and hence no classical braiding. The entire noncommutative structure of $A_\cC$ arises from quantization in the factorization envelope, not from a pre-existing bracket. This quantization introduces associativity ($\Eone$) through the extension correspondence (the CoHA multiplication), which is ordered: short exact sequences $0 \to V' \to V \to V'' \to 0$ have a preferred direction (sub before quotient). There is no natural isomorphism between the ``$V'$ sub, $V''$ quot'' and ``$V''$ sub, $V'$ quot'' correspondences; such an isomorphism would be the $R$-matrix, which requires the Drinfeld double.
   848	
   849	\medskip
   850	\noindent\textbf{Pillar (b): One-dimensional deformation space.}
   851	By Theorem~\ref{thm:c3-hochschild}, $\HH^2(\PV^*(\C^3)) = 1$: the deformation space is one-dimensional, spanned by $\sigma_3 = h_1 h_2 h_3$. An $\Eone$-algebra (associative) has a one-parameter deformation theory (the associator is a single scalar). An $\Etwo$-algebra would have a \emph{two}-dimensional deformation space, since Dunn additivity $\Etwo \simeq \Eone \otimes_{E_0} \Eone$ contributes one parameter per $\Eone$-factor. The fact that $\dim \HH^2 = 1$ is therefore diagnostic of $\Eone$, not $\Etwo$.
   852	
   853	This argument applies universally: for any toric CY$_3$ with $T^3$-equivariant $\Omega$-deformation, the equivariant deformation space is one-dimensional (spanned by $\sigma_3$), and the conclusion is $\Eone$.

thinking
**Figuring out theorems**

Alright, I’m focusing on a specific theorem, which is the universality of G. I think I’ve got the lines I need for that, but I might also want to consider including the RTT all classical types. It seems like I’ll need some extra proof lines after 278 as well, particularly for the NL-BA continuation around the proof. I just want to ensure everything is thorough, so I’ll keep that in mind as I work on this.
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '278,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   278	The RTT relation~\eqref{eq:rtt-relation} with the type-specific
   279	$R$-matrix defines $Y(\fg)$ for all classical~$\fg$.
   280	\end{theorem}
   281	
   282	\begin{proof}
   283	The proof proceeds in three steps.
   284	
   285	\emph{Step 1: Operator identities.}
   286	For types $B$ and $D$, the trace projection $Q$ satisfies $Q^2 = NQ$
   287	(where $N = \dim V$), $PQ = QP = Q$: these follow from
   288	$Q_{(ij),(kl)} = \delta_{ij}\delta_{kl}$, giving
   289	$(Q^2)_{(ij),(kl)} = \sum_{m,n} \delta_{ij}\delta_{mn}\delta_{mn}\delta_{kl}
   290	= N\,\delta_{ij}\delta_{kl}$.
   291	For type $C$, the symplectic contraction $K$ satisfies $K^2 = -NK$
   292	and $PK = KP = -K$: the sign difference from the orthogonal case
   293	arises because $J$ is skew-symmetric ($J^T = -J$), so
   294	$PK = -K$ rather than $PK = Q$.
   295	
   296	\emph{Step 2: YBE verification.}
   297	The Yang--Baxter equation is verified by expanding









thinking
**Evaluating theorem surfaces**

I’m looking to find the exact line for "universality-of-G." I might also consider checking Volume I for "higher_genus_foundations," though it’s not essential. I need to count how many I’ve checked. So far, it seems like I've verified around 11-12 theorem surfaces, with a total count of 16 checked. I’ll summarize: Checked: 16 | Findings: 7 | Verdict: FAIL. I’ll ensure I read the file contents of those surfaces accurately.
thinking
**Listing theorem blocks read**

I’ll list the substantive theorem and proof blocks I’ve gone through: 

1. general-nahc
2. general-bps
3. universality-of-G
4. hdm-seven-way-master
5. all-types-yangian-structure 
6. rtt-all-classical-types 
7. mc3-arbitrary-type 
8. y-algebra-koszulness 
9. PVA-descent-roadmap 
10. genus-g-formality 
11. universal-bulk (read but no proof)
12. cy-complementarity-d2 
13. e1-universality-cy3 
14. cy-modular-characteristic (theorem only)
15. face1-cy-bar-cobar 
16. face7-cy3-gaudin 
17. hc-census 
18. ent-landscape-census 
19. possibly Kac-Shapovalov criterion and c3-hochschild as dependencies 
20. maybe theorem registry/CLAUDE.

I’ve checked about 18 theorem surfaces and found 7. I need to assess the severity of each finding.
thinking
**Determining line numbers**

I need to figure out the exact line numbers using `nl -ba`. I think the problem might be around theorem start lines 4722 to 4739, with the proof at line 4751. I'm considering whether to reference file at line 4735 or 4747. I’m leaning towards formatting with proof line 4751 or theorem line 4735, but I need to double-check which makes more sense for clarity. It's a bit tricky!
thinking
**Considering proof coverage**

I'm thinking that the proof doesn't fully cover some specific cases; it clearly addresses type A while types B, C, and D are just sketched out, which isn't very strong. I could still mention [MEDIUM] as a possible inclusion. I'm wondering if the user asked for a specific fix. That's something I might want to clarify to ensure I provide the right answer!
thinking
**Labeling severity levels**

I need to assign severity labels like `[CRITICAL]` and others for categorization. It looks like I have five critical issues identified, and possibly two high ones. It’s important to make sure those labels are correct and align with our needs. I want to be thorough in this process to ensure nothing gets overlooked. Let’s make sure to clarify what each label means as I go along, so everything is well-organized and understood!
thinking
**Organizing theorem details**

I need to split the theorem by keeping type A as ProvedHere and moving B, C, and D to ClaimStatusProvedElsewhere with appropriate citations. Alternatively, I could provide the complete rank-n algebraic YBE expansion for B, C, and D while maintaining the all-types statement. I realized that file:line 303 is a proof line, not a theorem, which is acceptable. I'm considering using file 5102 as a theorem claim and referencing the proof found in lines 5119-5123.
thinking
**Summarizing findings**

I need to keep this concise, maybe using bullet points for clarity. I should highlight that I checked 18 items. My final summary might include seven bullet points, focusing on key findings without nesting. I want to ensure each line is clear, along with absolute file links. 

For instance, one finding could be: 

- [CRITICAL] [chapters/connections/arithmetic_shadows.tex:4003](/Users/.../chapters/connections/arithmetic_shadows.tex:4003) — This theorem claims a shadow triple for “every chirally Koszul algebra,” but lacks a robust argument for its proof. I'll suggest renaming the theorem for clarity.
thinking
**Clarifying findings**

I need to mention the Kac-Shapovalov criterion in line 4034, highlighting that it's broader, but line 4031 isn’t sufficient. 

I'll outline some critical issues:

- [CRITICAL] arithmetic_shadows.tex:4735 — The current statement suggests the BPS-spectrum construction applies to all finitely strongly generated vertex algebras, but the proof only covers specific examples. I'll recommend a conditional theorem instead, clarifying when the shadow coefficients apply.

- [CRITICAL] [chapters/connections/holographic_datum_master.tex:726] — The opening claim contradicts itself by limiting conditions for the seventh face, but the proof references it inaccurately.
thinking
**Revising the theorem**

I need to rewrite the theorem in a clearer structure. I'll frame it as a two-scope statement: “For every modular Koszul chiral algebra, Faces (F1) through (F4) coincide.” This should help clarify the relationships between the faces in the context of modular Koszul theories. It’s crucial to present this information accurately to avoid misunderstandings in the application of the theorem. I'll make sure the revision captures the intended meaning precisely.
codex
- [CRITICAL] [chapters/connections/holographic_datum_master.tex:726](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:726) — PROBLEM: The theorem opens with “for every modular Koszul chiral algebra” all seven faces coincide, but [line 750](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:750) immediately restricts the seventh equality to `\widehat{\fg}_k`, and the proof only imports Face 7 through the affine theorem. FIX: Replace the opening claim by “For every modular Koszul chiral algebra, Faces (F1)–(F4) coincide in the genus-zero two-point sector; for `\cA=\widehat{\fg}_k`, Faces (F5)–(F7) are additionally defined and coincide with the first four.”

- [CRITICAL] [chapters/connections/arithmetic_shadows.tex:4003](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4003) — PROBLEM: `thm:general-nahc` claims a shadow triple for “every chirally Koszul algebra,” but the proof at [4029-4034](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4029) only cites the Virasoro generating-function theorem and then handwaves “analogous finiteness” for standard families. FIX: Rename it to “Standard-landscape shadow triple” and change line 4003 to “For every chirally Koszul algebra `\cA` in the standard landscape with `N` strong generators, ...”.

- [CRITICAL] [chapters/connections/arithmetic_shadows.tex:4735](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4735) — PROBLEM: `thm:general-bps` enlarges the scope to every finitely strongly generated vertex algebra with invariant form, but the proof at [4748-4756](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:4748) only works out Virasoro and lattice examples and never proves the shadow tower exists in that larger class. FIX: Rewrite the theorem conditionally: “Assume (a)–(c). Then the shadow coefficients, when defined, determine a formal BPS spectrum...”; delete the sentences claiming this is established for every finitely strongly generated vertex algebra and for admissible/logarithmic/coset/orbifold theories.

- [CRITICAL] [chapters/connections/modular_koszul_bridge.tex:126](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:126) — PROBLEM: Item `(C2^{CY})` states a general CY\(_2\) scalar complementarity law, but [line 130](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:130) already concedes the displayed K3 computation is “NOT universal across all CY\(_2\) categories,” and the proof at [137](/Users/raeez/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex:137) only treats K3. FIX: Replace `(C2^{CY})` by a K3-only statement, e.g. “For `\cC=D^b(\Coh(K3))`, `\kappa_{\mathrm{ch}}(\cA_{K3})+\kappa_{\mathrm{ch}}(\cA_{K3}^!)=0`,” and move the general free-field/KM transport claim to a conjecture or remark.

- [HIGH] [chapters/theory/cy_to_chiral.tex:853](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:853) — PROBLEM: `thm:e1-universality-cy3` claims any toric CY\(_3\), but line 853 universalizes from the C\(^3\)-only theorem [thm:c3-hochschild](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:386); the later scope remark at [910-913](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:910) admits the pillars are geometry-specific. FIX: Change [line 837](/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:837) to “For `X=\C^3` with `T^3`-equivariant `\Omega`-deformation, the chiral algebra `A_{\C^3}` is natively `\Eone`,” or prove a toric-general `HH^2`/braiding argument before retaining toric-general scope.

- [HIGH] [chapters/connections/arithmetic_shadows.tex:5102](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5102) — PROBLEM: `thm:universality-of-G` says `\log(1+6t/c)` is universal across all single-generator vertex algebras, but the proof at [5118-5123](/Users/raeez/chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:5118) proves it only for standard families. FIX: Replace lines 5102-5104 by “universal across the standard-landscape single-generator families treated here at leading order in `1/c`,” or add a proof for arbitrary single-generator vertex algebras.

- [HIGH] [chapters/examples/yangians_foundations.tex:303](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:303) — PROBLEM: `thm:rtt-all-classical-types` advertises a proved-here all-classical result, but the proof computes type \(A\) explicitly at [299-302](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:299) and disposes of types \(B,C,D\) with “the same strategy”; the theorem text itself falls back to low-rank numerics at [274-276](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:274). FIX: Split the theorem: keep type \(A\) as `\ClaimStatusProvedHere`; move \(B,C,D\) to `\ClaimStatusProvedElsewhere` with Molev citations, or insert the full rank-\(n\) YBE expansion for \(B,C,D\) before keeping the current claim.

## Summary
Checked: 18 | Findings: 7 | Verdict: FAIL
tokens used
209,019
