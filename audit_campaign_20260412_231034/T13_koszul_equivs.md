# T13_koszul_equivs (634s, gpt-5.4)

Source intent: the theorem counts `(i)`–`(x)` as the `10` unconditional items; `(xi)` is the conditional `+1` (Lagrangian criterion); `(xii)` is the one-directional `+1` (`\mathcal D`-module purity). That count does not survive the source audit.

- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:1998-2004, 2108-2150 — Item `(vii)` is advertised inside the “unconditional equivalences,” but the proof explicitly scopes `(i) ⇔ (vii)` to the `g=0` specialization only, and the remark states the all-genera version is strictly stronger than Koszulness because Virasoro has nonzero `\delta F_g^{\mathrm{cross}}`. So `(vii)` is not one of the ten unconditional equivalences as written.
- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:2005-2008, 2065-2076; chapters/theory/chiral_hochschild_koszul.tex:576-605, 687-735 — Item `(viii)` is mis-stated. The cited Hochschild theorems prove duality, concentration in degrees `{0,1,2}`, and a polynomial Hilbert series; they do not prove that `\mathrm{ChirHoch}^*(\cA)` is a free polynomial algebra with generators in degrees `{0,1,2}`. The proof of `(viii) ⇒ (v)` uses that stronger unproved claim and also conflates cohomological degree with the second `Ext` grading.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_inversion.tex:2789-2808, 3015-3041; chapters/theory/chiral_koszul_pairs.tex:2020-2022, 2262-2291 — The `+1` Lagrangian lane is status-inflated. The underlying “Lagrangian characterization” is explicitly a conjecture, yet the “unconditional” corollary for the standard landscape proves itself by “apply the Lagrangian criterion” while citing that conjecture. The meta-theorem’s proof reuses the same conjectural argument as if it were established.
- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:1339-1399, 1970-2008; chapters/connections/concordance.tex:7188-7194 — The file itself records a critical-level affine KM boundary regime where PBW/`E_2` degeneration survives but diagonal `Ext` concentration and Theorem `H` fail. That is incompatible with an unqualified global equivalence chain `(i)`–`(x)`, and it directly conflicts with the nearby claim that `V_k(\mathfrak g)` is chirally Koszul at all levels.
- [HIGH] chapters/theory/chiral_koszul_pairs.tex:1277-1311, 2245-2259 — The converse “diagonal `Ext` vanishing ⇒ `E_2`-collapse” is not proved. The argument says diagonal abutment forces all higher differentials to vanish, but off-diagonal terms can be killed by higher differentials and still leave diagonal `E_\infty`. Both the standalone theorem and the meta-proof use this invalid spectral-sequence step.
- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:2518-2556, 2559-2605; chapters/theory/chiral_koszul_pairs.tex:2177-2203 — The Barr–Beck lane is not independently established. The inversion file first says the precise BBL locus is conjectural, then states a `ProvedHere` theorem under the standing hypotheses of bar-cobar inversion; as written those imported hypotheses come from a theorem whose first hypothesis is that `\cA` is Koszul. The meta-proof likewise reasons only “on the Koszul locus,” so `(vi)` is not proved as an independent characterization.
- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:2689-2725; chapters/theory/chiral_koszul_pairs.tex:2157-2174 — The FM-boundary equivalence is only asserted, not proved. The forward direction treats `i_S^!` as if it preserved degree-zero concentration (“restrictions of degree-0 objects remain in degree 0”), which is exactly the subtlety later outsourced to purity; the converse jumps from acyclicity on every stratum to injectivity of the PBW comparison map with no supporting argument.
- [MEDIUM] chapters/theory/chiral_koszul_pairs.tex:2036-2040; chapters/theory/chiral_koszul_pairs.tex:696-720, 873-993 — The proof cites `thm:pbw-koszulness-criterion` as if it directly identified chirally Koszul with `E_2`-collapse. It does not: the theorem is a one-way PBW sufficient criterion, while the actual `E_2`-collapse statement appears later in `cor:bar-cohomology-koszul-dual`. A load-bearing citation is therefore wrong.
- [LOW] chapters/connections/concordance.tex:1990-1992; chapters/connections/outlook.tex:233-234; chapters/connections/holographic_codes_koszul.tex:41-43 — The broken slogan “10 unconditional, 1 conditional, 1 one-directional” is propagated unchanged into programme-level summary files, so the local theorem defects already contaminate downstream overview surfaces.

## Summary
Instances checked: 23 | Violations found: 9 | Verdict: FAIL


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
session id: 019d8388-34be-78b0-a935-3a38d38e2961
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


MISSION: FALSIFY the proof of 10+1+1 Koszul equivalences. Find and audit each. Are there really 10 unconditional? What are the +1+1?

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.
mcp startup: no servers
codex
Using `deep-beilinson-audit` for a proof-surface falsification pass. I’m locating the `10+1+1` Koszul equivalence theorem, then I’ll read the governing concordance/registry surfaces and audit the statement and proof step by step against cited dependencies and scope boundaries.
exec
/bin/zsh -lc "pwd && rg -n \"10\\+1\\+1|10\\s*\\+\\s*1\\s*\\+\\s*1|Koszul equivalence|Koszul equivalences|10 unconditional|\\+1\\+1\" chapters CLAUDE.md metadata theorem_registry.md chapters/connections/concordance.tex .agents/skills/deep-beilinson-audit/SKILL.md 2>/dev/null" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md:493:| Koszul | 10+1+1 | 10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir) |
chapters/connections/concordance.tex:1991:(10 unconditional, 1 conditional, 1 one-directional;
metadata/dependency_graph.dot:3264:  thm_koszul_equivalence_categories [label="thm:koszul-equivalence-categories\ntheorem [Pr]\nKoszul equivalence of categories {\cite{...", style=filled, fillcolor="#bbdefb"];
metadata/claims.jsonl:3146:{"label": "thm:koszul-equivalence-categories", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/theory/koszul_pair_structure.tex", "line": 1230, "title": "Koszul equivalence of categories {\\cite{BGS96}}", "cites_in_block": ["BGS96"]}
chapters/theory/higher_genus_modular_koszul.tex:33481:chiral algebras up to Koszul equivalence. The target is not
chapters/theory/higher_genus_modular_koszul.tex:33487:be determined, up to Koszul equivalence, by its shadow data
chapters/theory/chiral_koszul_pairs.tex:70:one-directional implication. The count is exact: $10 + 1 + 1$.
chapters/theory/chiral_koszul_pairs.tex:3117:ten unconditional Koszul equivalences lose force simultaneously.
chapters/theory/koszul_pair_structure.tex:1242:\begin{theorem}[Koszul equivalence of categories {\cite{BGS96}}; \ClaimStatusProvedElsewhere]
chapters/theory/bar_cobar_adjunction_inversion.tex:1889:cites no bar-cobar theorem and no Koszul equivalence. The
chapters/connections/outlook.tex:191:Koszulness characterization programme (10 unconditional + 1 conditional
chapters/connections/holographic_codes_koszul.tex:42:Theorem~\ref{thm:koszul-equivalences-meta}: 10 unconditionally
chapters/connections/concordance.tex:1991:(10 unconditional, 1 conditional, 1 one-directional;
chapters/connections/genus_complete.tex:1655:Assume an analytic Koszul equivalence
codex
The theorem surface is in [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex), with supporting status text in concordance and metadata. Next I’m reading the audit skill plus the theorem statement/proof and its registry/concordance surfaces, then I’ll walk the cited dependencies item by item and test whether the “10 unconditional + 1 conditional + 1 one-directional” count survives contact with the source.

PE-10:
```text
genus: all? to be checked from theorem statement
degree: all? to be checked from theorem statement
AP32 weight tag: NA
AP139 free-var audit: pending until theorem text is read
AP36: implies/iff pending
verdict: ACCEPT
```
Plan update
  → Read the audit skill and the live theorem surfaces: theorem statement/proof, concordance entry, registry/metadata references
  • Enumerate the 10+1+1 equivalences from source and classify each as unconditional, conditional, or one-directional
  • Trace every proof step to cited lemmas/propositions/literature and test for missing hypotheses, scope inflation, object conflation, and boundary failures
  • Re-verify each candidate finding against actual file contents and produce a severity-ordered audit report with counts and verdict
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
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

exec
/bin/zsh -lc "sed -n '1,160p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '450,540p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md 2>/dev/null || sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1960,2025p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 Pillar~C (Mok's log-smooth degeneration) provides additional
 inductive structure via rigid special-fibre decomposition.
 \emph{Arithmetic connection}: the sewing--Selberg formula
 (Theorem~\ref{thm:sewing-selberg-formula}) identifies
 $\int_{\cM_{1,1}}\log\det(1{-}K)\cdot E_s\,d\mu
 = -2(2\pi)^{-(s-1)}\Gamma(s{-}1)\zeta(s{-}1)\zeta(s)$;
 the Fredholm determinant of the HS-sewing theorem is the
 same $\det(1{-}K_q)$ whose divisor-sum decomposition
 encodes $\zeta(s)\zeta(s{+}1)$
 (Chapter~\ref{chap:arithmetic-shadows}).
\end{itemize}
\end{remark}

\section{The three concentric rings}
\label{sec:three-rings}
\index{three concentric rings|textbf}
\index{nonlinear characteristic layer|textbf}

The monograph is organized in three concentric rings.

 succeeded in 52ms:
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
 succeeded in 52ms:
(1) WRONG: "The bar differential is the closed/holomorphic color of SC." TRUTH: The bar differential d_B comes from the chiral product (OPE residues at FM boundary strata). It is the differential of a dg coalgebra over (ChirAss)^!, NOT a "color" of SC. Having operations that USE FM_k(C) geometry does not make d_B an "E_2 color" — it is a single degree-1 map, not a parametrized family of operations.

(2) WRONG: "The deconcatenation coproduct is the open/topological color of SC." TRUTH: Deconcatenation is the cofree tensor coalgebra structure on T^c(V). It is coassociative. This makes B(A) an E_1-coassociative coalgebra. It is NOT a separate "color" of a two-colored operad.

(3) WRONG: "Together, d_B and Delta make B(A) an SC-coalgebra." TRUTH: A dg coassociative coalgebra (differential + coproduct) is a SINGLE-colored E_1 dg coalgebra. Having two structures does not make it two-colored. SC is two-colored (bulk + boundary); B(A) is one object, not a pair.

(4) WRONG: "The SC structure on B(A) is dual to the SC structure on (Z^{der}(A), A)." TRUTH: B(A) is an INPUT to the Hochschild computation. The derived center C^bullet_ch(A,A) is computed FROM B(A) via the convolution Hom(B(A), A). The SC structure emerges in the OUTPUT (the derived center pair), not on the INPUT (the bar complex). The passage B(A) → C^bullet_ch(A,A) is the Hochschild construction, not an operadic duality.

(5) WRONG: "E_1-chiral = E_1-topological (on R)." TRUTH: E_1-chiral means operations from ordered configurations on a CURVE (2-real-dimensional, holomorphic structure). E_1-topological means operations from Conf_k(R) (1-real-dimensional). A chiral algebra on a curve X is a factorization algebra on a real 2-manifold sensitive to holomorphic structure. Calling the bar complex "E_1" without "chiral" conflates these. The bar complex is over (ChirAss)^!, NOT (Ass)^!.

(6) WRONG: "The Steinberg analogy: B(A) presents SC as the Steinberg variety presents the Hecke algebra." TRUTH: Retired. The Steinberg variety is a geometric object in the representation theory of reductive groups. The bar complex is a coalgebra computing the derived center. These are unrelated constructions at different categorical levels.

Counter: NEVER write B(A) and SC^{ch,top} in the same sentence attributing SC to B(A). The SC structure lives on (C^bullet_ch(A,A), A). The bar complex is over (ChirAss)^!, single-colored, E_1-chiral-coassociative.

**FM26. False operad self-duality claim.** Opus claimed "(SC^{ch,top})^! ~ SC^{ch,top}" (Koszul self-dual) in thm:SC-self-duality, misciting Livernet [Liv06] (which proves Koszulity, not self-duality). The manuscript's OWN compute engine (sc_koszul_dual_cooperad_engine.py) computes SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!, manifestly different from SC = (Com, Ass) with closed dim = 1. The error: confusing "the duality FUNCTOR is an involution on SC-algebras" with "the OPERAD is self-dual." These are different: (P^!)^! ~ P (tautological for Koszul operads) does NOT mean P^! ~ P. Counter: before claiming any operad is self-dual, verify dim P(n) = dim P^!(n) at all degrees.

**FM27. Scope inflation in metadata.** Opus inflated concrete computational results into universal claims in CLAUDE.md/MEMORY.md. Example: "chiral QG equivalence for all four families" when the paper only verifies concretely for sl_2 Yangian + affine KM. The abstract theorem is proved on the Koszul locus, but concrete verification requires explicit computation at each family. Counter: metadata claims must carry explicit scope qualifiers matching the actual verification level.

**FM29. RETRACTED.** The arity→degree rename was correct and intentional. "Arity" is banned from the manuscript (AP176 CONSTITUTIONAL). "Degree" is the universal term for all index-counting contexts. The rename was NOT an error.

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

thinking
**Searching for theorems**

I'm looking to locate a specific theorem or proof related to chiral Koszul pairs. It seems like I should search for any labels associated with the theorem. I want to ensure I’m reading the relevant lines carefully in order to fully grasp the theorem and its proof. I'll make sure to use the appropriate labels, like "rg," to narrow down my search effectively!
codex
The concordance confirms the intended count but not the proof quality. I’m moving onto the theorem surface itself now: extracting the exact 12 items, then tracing whether the proof really establishes 10 unconditional biconditionals plus a conditional item and a one-directional item, or whether the count is inflated by scope or dependency leakage.
exec
/bin/zsh -lc "sed -n '1200,1305p' chapters/theory/koszul_pair_structure.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"koszul-equivalences-meta|10 \\+ 1 \\+ 1|Lagrangian|D-mod purity|conditional|one-directional|Koszulness characterization programme\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/koszul_pair_structure.tex chapters/connections/holographic_codes_koszul.tex chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{theorem}

\begin{conjecture}[Gaiotto-Witten S-duality, general case; \ClaimStatusConjectured]\label{conj:gw-s-duality}
For general $\mathfrak{g}$ and nilpotent $f$, there exists a duality:
\[
\mathcal{W}^k(\mathfrak{g}, f) \longleftrightarrow \mathcal{W}^{k^L}(\mathfrak{g}^L, f^L)
\]
where:
\begin{itemize}
\item $k^L = -h^{\vee}(\mathfrak{g}^L) + r^{\vee}/(k + h^{\vee}(\mathfrak{g}))$, where $r^{\vee}$ is the lacing number of $\mathfrak{g}$
\item $f^L$ is the Spaltenstein dual nilpotent
\end{itemize}
\end{conjecture}

\begin{remark}[Scope]
The principal simply-laced case is Feigin--Frenkel
\cite{Feigin-Frenkel} (proved). In type~$A$, the hook-type
network supplies structured evidence and a proved transport
mechanism, but the manuscript keeps the full hook-type duality
statement conditional on hook-wide DS/bar compatibility
 succeeded in 51ms:
\chapter{Chiral Koszul duality}
\label{chap:koszul-pairs}

\index{chiral Koszul duality|textbf}
\index{twisting morphism!chiral|textbf}
\index{Francis--Gaitsgory|textbf}

Classical Koszul duality, in the sense of
Priddy~\cite{Priddy70} and
Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
algebras over a field: the bar complex is a tensor coalgebra on a
finite-dimensional vector space, the cobar functor inverts it
when bar cohomology is concentrated in degree one, and the
duality exchanges quadratic algebras with quadratic coalgebras.
Three features of chiral algebras on algebraic curves defeat
this framework simultaneously. First, chiral algebras are
\emph{curved}: the bar differential on the genus expansion
satisfies $d^2_{\mathrm{fib}} = \kappa(\cA) \cdot \omega_g$
rather than $d^2 = 0$, so the classical bar-cobar adjunction,
which requires strict nilpotence, does not apply beyond genus
 succeeded in 51ms:
chapters/connections/outlook.tex:35: genus~$0$ unconditional; for arbitrary~$\cA$,
chapters/connections/outlook.tex:36: $g \geq 1$ is conditional on
chapters/connections/outlook.tex:37: axiom~\ref{MK:modular}; unconditional on the
chapters/connections/outlook.tex:45: Verdier-side Lagrangian splitting unconditional;
chapters/connections/outlook.tex:46: ambient shifted-symplectic upgrade conditional on
chapters/connections/outlook.tex:52: genus-$1$ unconditional for all families;
chapters/connections/outlook.tex:73:$\Theta_\cA \in \MC(\gAmod)$ exists unconditionally by the bar-intrinsic
chapters/connections/outlook.tex:191:Koszulness characterization programme (10 unconditional + 1 conditional
chapters/connections/outlook.tex:192:+ 1 partially proved, Theorem~\ref{thm:koszul-equivalences-meta}).
chapters/connections/outlook.tex:204:(MC4 proved unconditionally), Yangian/RTT axis (MC3 proved on the evaluation-generated core for all
chapters/connections/outlook.tex:229:\section{Koszulness characterization programme}
chapters/connections/outlook.tex:233:The meta-theorem (Theorem~\ref{thm:koszul-equivalences-meta}) lists
chapters/connections/outlook.tex:234:twelve characterizations of chiral Koszulness: ten unconditional equivalences, one conditional on perfectness/nondegeneracy, and one partially proved (D-module purity, forward direction only).
chapters/connections/outlook.tex:264:chain-level false), and the tree-level amplitude pairing is conditional.
chapters/connections/outlook.tex:335:is conditional on the explicit charged quartic jet conjecture
chapters/connections/outlook.tex:601:equivariance and splitting unconditionally, but the flat identity
chapters/connections/outlook.tex:603:space~$V$. The rank-$1$ string equation is proved unconditionally via
chapters/connections/holographic_codes_koszul.tex:5:% from Lagrangian isotropy, resolves
chapters/connections/holographic_codes_koszul.tex:11:% Symplectic code structure from Lagrangian isotropy (Theorem)
chapters/connections/holographic_codes_koszul.tex:35:reconstruction.} The Lagrangian structure provides a

thinking
**Seeking theorems**

I’m looking for a theorem from around 1965 onward. My plan is to read a substantial chunk that includes both the theorem and its proof. This should help me grasp the context and the implications better. I think that going through the details step by step will make it easier to understand. It’s all about breaking it down so I can really get the concepts. Let’s see what I can dig up!
exec
/bin/zsh -lc "sed -n '1935,2325p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{remark}

\begin{remark}[Comparison with the Kac--Shapovalov criterion]
\label{rem:li-bar-vs-kac-shapovalov}
\index{Li filtration!comparison with Kac--Shapovalov}

Theorem~\ref{thm:associated-variety-koszulness} refines
Theorem~\ref{thm:kac-shapovalov-koszulness} as follows.
The Shapovalov form~$G_h$ detects null vectors weight by weight.
The Li filtration organizes these null vectors \emph{geometrically}:
a null vector at weight~$h$ in the vacuum module corresponds
to a relation in $R_V = \operatorname{gr}^F V$ at Li
filtration level~$p$, and the Poisson bracket determines
whether this relation propagates to the bar complex via~$d_1$.
The Shapovalov criterion asks: are there null vectors in the
bar-relevant range? The Li--bar criterion asks: does the
\emph{geometry} of the associated variety~$X_V$ force those
null vectors to produce off-diagonal bar cohomology?

The gain is maximal when $X_V \neq \{0\}$ and one can


thinking
**Analyzing theorem proof**

I’m diving into the audit of a theorem and the proof it presents. I need to understand dependencies for each step and check any cited theorems or definitions. It seems essential to look for full statements of the dependencies and verify if they're proven correctly or based on hidden assumptions. Also, I need to clarify the exact conditions mentioned and determine whether the theorem truly holds unconditional equivalences across all cases. It looks like there's a discrepancy, which may be significant.
thinking
**Examining theorem consistency**

I need to carefully analyze theorem item (vii) since it includes a caveat. The statement about factorization homology mentions conditions for different values of g, implying a relationship between unconditional concentration for g=0 and conditional for g≥1. However, there's a contradiction since later parts of the proof suggest that the equivalence only holds for g=0. This discrepancy seems significant, indicating possible overstatements in the theorem's scope. I should gather evidence and line numbers to clarify this further.
codex
A first crack is already visible: item `(vii)` is declared part of the unconditional equivalence block, but the proof itself later narrows the equivalence to the `g=0` specialization only. I’m now checking whether that is the only leak or whether other links in the chain also rely on unpublished scope reductions, unproved auxiliary claims, or imported hypotheses that the theorem statement never names.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1958,2315p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(def:chiral-koszul-morphism|thm:pbw-koszulness-criterion|prop:ainfty-formality-implies-koszul|thm:ainfty-koszul-characterization|thm:bar-cobar-inversion-qi|thm:main-koszul-hoch|thm:bar-concentration|lem:twisted-product-cone-counit|prop:shadow-formality-low-degree|prop:bar-fh|thm:kac-shapovalov-koszulness|prop:lagrangian-perfectness|thm:ambient-complementarity-fmp|rem:d-module-purity-content|thm:quillen-equivalence-chiral|thm:quantum-complementarity-main)\\}\" chapters metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\"label\": \"(def:chiral-koszul-morphism|thm:pbw-koszulness-criterion|prop:ainfty-formality-implies-koszul|thm:ainfty-koszul-characterization|thm:bar-cobar-inversion-qi|thm:main-koszul-hoch|thm:bar-concentration|lem:twisted-product-cone-counit|prop:shadow-formality-low-degree|prop:bar-fh|thm:kac-shapovalov-koszulness|prop:lagrangian-perfectness|thm:ambient-complementarity-fmp|rem:d-module-purity-content|thm:quillen-equivalence-chiral|thm:quantum-complementarity-main)\"' metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1958	test case where the reduced geometry suggests concentration, but
  1959	an unconditional Koszul theorem still requires the extra
  1960	reducedness and reduced Li--bar concentration hypotheses recorded in
  1961	Corollary~\ref{cor:minimal-orbit-koszul}.
  1962	\end{remark}
  1963	
  1964	\begin{theorem}[Equivalences of chiral Koszulness; \ClaimStatusProvedHere]
  1965	\label{thm:koszul-equivalences-meta}
  1966	\index{Koszul property!equivalences of characterizations|textbf}
  1967	
  1968	Let $\cA$ be a chiral algebra on a smooth projective curve~$X$
  1969	with PBW filtration $F_\bullet$.
  1970	Conditions \textup{(i)--(x)} below are equivalent.
  1971	Under the additional perfectness and non-degeneracy hypotheses on the
  1972	ambient tangent complex, condition~\textup{(xi)} is also equivalent to
  1973	them. Condition~\textup{(xii)} implies condition~\textup{(x)}
  1974	(Remark~\ref{rem:d-module-purity-content}); the converse is open.
  1975	
  1976	\smallskip
  1977	\noindent\textbf{Unconditional equivalences:}
 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:14932:\label{prop:shadow-formality-low-degree}
chapters/theory/bar_cobar_adjunction_inversion.tex:1604:\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
chapters/theory/bar_cobar_adjunction_inversion.tex:2881:\label{prop:lagrangian-perfectness}
chapters/theory/bar_cobar_adjunction_inversion.tex:3414:\label{prop:bar-fh}
chapters/theory/higher_genus_complementarity.tex:456:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:4639:\label{thm:ambient-complementarity-fmp}
chapters/theory/bar_cobar_adjunction_curved.tex:6228:\label{thm:quillen-equivalence-chiral}
chapters/theory/chiral_hochschild_koszul.tex:578:\label{thm:main-koszul-hoch}
chapters/theory/chiral_koszul_pairs.tex:248:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
chapters/theory/chiral_koszul_pairs.tex:282:\label{lem:twisted-product-cone-counit}
chapters/theory/chiral_koszul_pairs.tex:697:\label{thm:pbw-koszulness-criterion}
chapters/theory/chiral_koszul_pairs.tex:1062:\label{thm:bar-concentration}
chapters/theory/chiral_koszul_pairs.tex:1174:\label{prop:ainfty-formality-implies-koszul}
chapters/theory/chiral_koszul_pairs.tex:1208:\label{thm:ainfty-koszul-characterization}%
chapters/theory/chiral_koszul_pairs.tex:1407:\label{thm:kac-shapovalov-koszulness}
chapters/theory/chiral_koszul_pairs.tex:2576:\label{rem:d-module-purity-content}
 succeeded in 50ms:
2107:{"label": "thm:quillen-equivalence-chiral", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/theory/bar_cobar_adjunction_curved.tex", "line": 6226, "title": "Bar-cobar as Quillen equivalence", "refs_in_block": ["def:chiral-koszul-pair"], "cites_in_block": ["Val16"]}
2138:{"label": "thm:bar-cobar-inversion-qi", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 1604, "title": "Bar-cobar inversion is quasi-isomorphism", "refs_in_block": ["conv:regime-tags", "sec:frame-inversion", "def:koszul-chiral-algebra", "sec:i-adic-completion", "MK:modular", "def:modular-koszul-chiral", "thm:pbw-allgenera-km", "thm:pbw-allgenera-principal-w", "rem:qi-vs-homology-iso", "thm:spectral-sequence-collapse", "rem:sl2-admissible", "rem:virasoro-module-koszul-minimal", "cor:bar-cobar-inverse"]}
2154:{"label": "prop:lagrangian-perfectness", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 2823, "title": "Perfectness for the standard landscape", "labels_in_block": ["prop:lagrangian-perfectness", "item:perf-fingen", "item:perf-nondeg", "item:perf-dual"], "refs_in_block": ["item:perf-fingen", "item:perf-nondeg", "def:ambient-complementarity-datum"]}
2156:{"label": "prop:bar-fh", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 3340, "title": "Bar construction as factorization homology", "refs_in_block": ["def:bar-differential-complete"], "cites_in_block": ["AF15", "BD04"]}
2232:{"label": "thm:main-koszul-hoch", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 578, "title": "Koszul duality for Hochschild cohomology\n\\textup{(}Theorem~H\\textup{)}", "labels_in_block": ["thm:main-koszul-hoch", "eq:hochschild-H-derived"], "refs_in_block": ["conv:regime-tags", "def:chiral-koszul-morphism", "def:bigraded-hochschild", "thm:bar-concentration", "rem:hochschild-shift-origin"]}
2286:{"label": "lem:twisted-product-cone-counit", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 267, "title": "Left twisted tensor product as mapping cone"}
2293:{"label": "thm:pbw-koszulness-criterion", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 682, "title": "PBW criterion for chiral Koszulness", "labels_in_block": ["thm:pbw-koszulness-criterion", "item:pbw-flat", "item:pbw-classical-koszul", "item:pbw-bounded"], "refs_in_block": ["conv:regime-tags"]}
2297:{"label": "thm:bar-concentration", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 1047, "title": "Bar concentration for Koszul pairs", "refs_in_block": ["conv:regime-tags", "def:chiral-koszul-pair", "conv:bar-coalgebra-identity"]}
2298:{"label": "prop:ainfty-formality-implies-koszul", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 1159, "title": "Formality implies chiral Koszulness", "cites_in_block": ["Kad82", "LPWZ09"]}
2299:{"label": "thm:ainfty-koszul-characterization", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 1193, "title": "Converse: chiral Koszulness implies formality", "refs_in_block": ["prop:ainfty-formality-implies-koszul"]}
2303:{"label": "thm:kac-shapovalov-koszulness", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_koszul_pairs.tex", "line": 1350, "title": "Kac--Shapovalov criterion for simple quotients", "refs_in_block": ["cor:universal-koszul"]}
2644:{"label": "thm:quantum-complementarity-main", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 435, "title": "Quantum complementarity as Lagrangian polarization", "labels_in_block": ["thm:quantum-complementarity-main", "thm:quantum-complementarity", "eq:complementarity-decomp", "eq:verdier-symplectic-pairing", "eq:quantum-duality"], "refs_in_block": ["conv:regime-tags", "thm:chiral-koszul-duality", "def:complementarity-complexes", "lem:involution-splitting"], "cites_in_block": ["BD04"]}
2708:{"label": "thm:ambient-complementarity-fmp", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_complementarity.tex", "line": 4620, "title": "Ambient complementarity as shifted symplectic formal\nmoduli problem", "refs_in_block": ["thm:ambient-complementarity-tangent"]}



thinking
**Evaluating theorem proofs**

I need to focus on reading the definitions and proofs of cited dependencies, potentially using multiple read windows. I'm especially looking for the statuses and ensuring the theorem applies them correctly. It seems theorem (viii) implies (v), but it might rely on (iv) implying (i), which hasn't been established beforehand—this could be circular reasoning. At line 2074, it references (iv) before it’s proved later. I need to verify if (iv) is proven earlier or if it's indeed a circular dependency. This seems potentially critical.
thinking
**Assessing proof structure**

If (iv) implying (i) can be proven later, then the proof might not be circular if the overall theorem can utilize those later subproofs. In mathematics, parts of a proof can be presented in any order as long as the structure is clear. Usually, labeling something as "already established" is incorrect, but the proof can still hold if the later proof is independent. I need to check if the later proof of (iv) imposing (i) uses (viii) implying (v) and it doesn't. I think the proof can be salvaged, though it mislabels a forward reference. Severity looks like LOW to MEDIUM. But I should inspect the definitions and conditions further, maybe using an explorer tool, although subagents aren't an option right now.
thinking
**Reading relevant materials**

I need to dive into the manual for the chiral Koszul pairs, focusing on the definition, lemma, PBW criterion, bar concentration, A∞ theorems, and Kac-Shapovalov. I should also include the bar-cobar inversion theorem. Since there are a lot of sections to consider, I’ll read around the exact lines using rg/nl for context. It might be helpful to organize my approach with parallel execution commands to keep things efficient. This way, I can gather comprehensive insights!
codex
I’m drilling into the dependencies now. The main questions are whether the theorem imports the right hypotheses from its own supporting results, and whether any of the advertised biconditionals quietly become one-way implications once the cited statements are read in full.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '230,330p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '660,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1340,1435p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1150,1248p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1588,1668p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1035,1098p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   660	Consider the chiral Koszul pair $(\mathcal{BC}, \mathcal{BG})$ where:
   661	\begin{itemize}
   662	\item $\mathcal{BC}$ is the $bc$ ghost system with fermionic fields $b(z), c(z)$ and OPE $b(z)c(w) \sim \frac{1}{z-w}$
   663	\item $\mathcal{BG}$ is the $\beta\gamma$ system with bosonic fields $\beta(z), \gamma(z)$ and OPE $\beta(z)\gamma(w) \sim \frac{1}{z-w}$
   664	\end{itemize}
   665	
   666	The bar-cobar isomorphism manifests as:
   667	
   668	\emph{Algebra to coalgebra:}
   669	\begin{align*}
   670	\text{$bc$ OPE: } b(z)c(w) &\sim \frac{1}{z-w} \quad \text{(fermionic, $\Lambda^*$ structure)} \\
   671	\text{$\beta\gamma$ OPE: } \beta(z)\gamma(w) &\sim \frac{1}{z-w} \quad \text{(bosonic, $\mathrm{Sym}^*$ structure)}
   672	\end{align*}
   673	
   674	\emph{Generators to Relations (Ext--Sym duality).}
   675	\begin{itemize}
   676	\item $\mathcal{BC}$: two fermionic generators $b, c$, with $b^2 = c^2 = 0$ (exterior algebra structure)
   677	\item $\mathcal{BG}$: two bosonic generators $\beta, \gamma$, with no nilpotency (symmetric algebra structure)
   678	\end{itemize}
   679	This is the chiral manifestation of classical $\Lambda^* \leftrightarrow \mathrm{Sym}^*$ Koszul duality.
 succeeded in 51ms:
   230	\begin{equation}\label{eq:chiral-twisted-differential-R}
   231	d_\tau^R(c \otimes a)
   232	\;=\;
   233	\sum (-1)^{|c|}\, c_{(1)} \otimes \tau(c_{(2)}) \cdot a,
   234	\end{equation}
   235	where $\Delta(c) = \sum c_{(1)} \otimes c_{(2)}$ is the factorization
   236	coproduct. The MC equation $d\tau + \tau \star \tau = 0$ is
   237	\emph{equivalent} to $(d_\cA + d_\cC + d_\tau^L)^2 = 0$
   238	\textup{(}cf.\ \cite[Lemma~2.1.4]{LV12}\textup{)}: the twisting
   239	morphism condition is the nilpotence of the twisted differential.
   240	In the chiral setting, $\tau(c_{(1)})$ is the OPE extraction:
   241	the coproduct $\Delta(c) = \sum c_{(1)} \otimes c_{(2)}$ separates
   242	the coalgebra element, and $\tau$ evaluates $c_{(1)}$ against the
   243	propagator on~$\overline{C}_2(X)$ by residue at the collision
   244	divisor
   245	\textup{(}Proposition~\textup{\ref{prop:twisting-morphism-propagator})}.
   246	\end{remark}
   247	
   248	\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
   249	\index{Koszul morphism!chiral|textbf}
 succeeded in 52ms:
  1150	one-directional (D-module purity, forward direction established)), each
  1151	reading~$\Theta_\cA^{(0)}$ through a different invariant
  1152	of the convolution algebra.
  1153	
  1154	\begin{remark}[One-loop exactness]
  1155	\label{rem:one-loop-exactness}
  1156	\index{PBW filtration!one-loop exactness}
  1157	\index{one-loop exactness}
  1158	
  1159	The PBW spectral sequence
  1160	(Corollary~\ref{cor:bar-cohomology-koszul-dual}) admits a sharp
  1161	physics interpretation. The $E_0$ page is the tree-level bar complex
  1162	$\barBgeom(\operatorname{Sym}^{\mathrm{ch}}(V))$, with cohomology
  1163	$\Lambda^{\mathrm{c}}(V^*)$ by Priddy's theorem. The $d_1$
  1164	differential is the Chevalley--Eilenberg differential extracted from
  1165	the simple-pole OPE $a_{(0)}b$: a single operator collision.
  1166	Collapse $E_2 = E_\infty$ means that no multi-particle collisions
  1167	(the higher poles $a_{(n)}b$, $n \geq 2$, generating $d_r$ for
  1168	$r \geq 2$) contribute additional cohomology. Chiral Koszulness is
  1169	therefore \emph{one-loop exactness}: the Lie-algebraic data from the
 succeeded in 52ms:
  1340	\ClaimStatusProvedHere]
  1341	\label{cor:universal-koszul}
  1342	\index{Koszul property!universal algebras}
  1343	
  1344	The following are chirally Koszul:
  1345	\begin{enumerate}
  1346	\item $V_k(\fg)$ at all levels~$k$ \textup{(}including $k = -h^\vee$\textup{)},
  1347	 since its vacuum module is Verma with no null vectors.
  1348	\item $\mathrm{Vir}_c$ as the universal vertex algebra at all~$c$,
  1349	 since the vacuum Verma module is freely strongly generated.
  1350	\item $\mathcal{W}^k(\fg)$ obtained by Drinfeld--Sokolov reduction,
  1351	 by the Feigin--Frenkel theorem \textup{(}the Miura images freely
  1352	 generate\textup{)}.
  1353	\end{enumerate}
  1354	
  1355	\noindent\textbf{The universal vs.\ simple distinction.}
  1356	The universal algebra $V_k(\fg)$ is always chirally Koszul.
  1357	The simple quotient $L_k(\fg) = V_k(\fg)/I_k$ may fail Koszulness
  1358	at levels where the singular vector lies in the bar-relevant range
  1359	; the precise criterion is
 succeeded in 51ms:
  1588	%================================================================
  1589	
  1590	\section{Bar-cobar inversion}
  1591	\label{sec:bar-cobar-inversion-quasi-iso}
  1592	
  1593	The comodule-contramodule correspondence of the preceding section
  1594	provides the categorical framework in which bar-cobar inversion
  1595	lives: at genus~$0$ the coderived category reduces to the
  1596	ordinary derived category, and the inversion theorem is a
  1597	quasi-isomorphism in the classical sense; at genus~$g \geq 1$
  1598	the curvature forces passage to the coderived setting, and the
  1599	inversion theorem becomes a statement about coderived equivalences.
  1600	We now prove the central result of this chapter.
  1601	
  1602	\subsection{Statement of the main result}
  1603	
  1604	\begin{theorem}[Bar-cobar inversion is quasi-isomorphism; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
  1605	\textup{[Regime: quadratic at genus~$0$; curved-central at genus~$g \geq 1$
  1606	on the Koszul locus; filtered-complete off it
  1607	\textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}
 succeeded in 50ms:
  1035	\index{bar complex!vs CE cohomology}%
  1036	\index{Witt algebra!CE vs bar}%
  1037	\index{Orlik--Solomon form!contribution to discrepancy}%
  1038	The Chevalley--Eilenberg cohomology of the negative-mode
  1039	Lie algebra $\fg_{<0} = \fg \otimes t^{-1}\bC[t^{-1}]$
  1040	and the chiral bar cohomology $H^*(\barBgeom(\cA))$ give
  1041	\emph{different} Betti sequences, though both compute from
  1042	the same underlying OPE data.
  1043	For the Witt algebra $\mathrm{Witt} = \mathrm{Der}(\bC((t)))$,
  1044	the negative-mode Lie algebra is the Lie algebra of
  1045	polynomial vector fields vanishing to order~$\geq 2$
  1046	at the origin, and its CE cohomology has
  1047	$\dim H^1_{\mathrm{CE}}(\mathrm{Witt}_{<0}) = 3$
  1048	(the three independent cocycles $L_{-1}^*, L_{-2}^*, L_{-3}^*$
  1049	on $\mathrm{span}\{L_{-1}, L_{-2}, L_{-3}\}$).
  1050	The chiral bar cohomology of the Virasoro algebra has
  1051	$\dim H^1(\barBgeom(\mathrm{Vir})) = 1$
  1052	(a single generator~$T$ of conformal weight~$2$).
  1053	The discrepancy $3 - 1 = 2$ quantifies the
  1054	Orlik--Solomon form contribution: the chiral bar differential

thinking
**Looking into theorem proofs**

I need to find more proofs for these theorems, like the bar concentration proof that continues after 1098. I should read the rest of that proof, along with the Kac-Shapovalov proof. There's also theorem H that I want to check out. Additionally, I need to look at the status and hypotheses of the Quillen theorem, and take a look at proposition bar-fh, Lagrangian perfectness, complementarity theorem, and ambient complementarity.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1094,1128p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1429,1498p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1094	\begin{proof}
  1095	Filter $\bar{B}^{\mathrm{ch}}(\cA_1)$ by bar degree.
  1096	By the PBW criterion (Theorem~\ref{thm:pbw-koszulness-criterion}),
  1097	the associated graded is the classical Koszul complex of
  1098	$\operatorname{gr}_F \cA_1$, which is acyclic in positive
  1099	degrees by hypothesis.
  1100	Corollary~\ref{cor:bar-cohomology-koszul-dual} then gives
  1101	$\dim H^n = \dim (\cA_2^!)_n$.
  1102	It remains to show that $H^0(\bar{B}^{\mathrm{ch}}(\cA_1))
  1103	\cong \cA_2^!$ as coalgebras, not merely as graded vector spaces.
  1104	The twisting morphism
  1105	$\tau\colon \bar{B}^{\mathrm{ch}}(\cA_1) \to \cA_2$
  1106	satisfies the Maurer--Cartan equation $\partial(\tau) + \tau \star \tau = 0$
  1107	in the chiral convolution algebra
  1108	$\mathrm{Hom}(\bar{B}^{\mathrm{ch}}(\cA_1), \cA_2)$
  1109	(Definition~\ref{def:chiral-koszul-morphism}), so the
  1110	twisted tensor products
  1111	$K_\tau^L(\cA_1, \cC_1)$ and $K_\tau^R(\cC_1, \cA_1)$
  1112	are well-defined chain complexes (twisted differentials square to
  1113	zero by the MC equation).
 succeeded in 51ms:
  1429	\begin{proof}
  1430	Forward: Koszulness gives $E_2$-collapse, hence the PBW
  1431	filtration on the vacuum module is strict:
  1432	$\operatorname{gr}_F M_0(\cA) \cong
  1433	\operatorname{Sym}^{\mathrm{ch}}(V)$. Strictness implies the
  1434	Shapovalov form~$G_h$ is non-degenerate in the bar-relevant
  1435	range (a degenerate $G_h$ would give a null vector in the
  1436	PBW-associated graded, contradicting strictness).
  1437	
  1438	Converse: $\det G_h \neq 0$ in the bar-relevant range means the
  1439	PBW-to-bar comparison map
  1440	$\operatorname{Sym}^{\mathrm{ch}}(V)_h \to \barBgeom_h(\cA)$ is
  1441	injective at every bar-relevant weight. Injectivity forces
  1442	$E_2$-collapse: a nonzero differential $d_r$ with $r \geq 2$ would
  1443	kill an element that pairs nontrivially with the Shapovalov form
  1444	(since the element is nonzero in $\operatorname{gr}_F$ and $G_h$ is
  1445	non-degenerate), contradicting the $d_r$-exactness.
  1446	\end{proof}
  1447	
  1448	\begin{remark}[Rationality is not, by itself, a Koszul criterion]
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '560,670p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1668,1768p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4615,4688p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2820,2898p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3335,3418p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '430,540p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2820	
  2821	Converse: transverse Lagrangians in a $(-1)$-shifted symplectic
  2822	space have derived intersection of expected dimension~$0$. This
  2823	derived intersection is the twisted tensor product
  2824	$K_\tau(\cA, \cA^!)$; its acyclicity is Koszulness.
  2825	\end{remark}
  2826	
  2827	\begin{remark}[PTVV interpretation]\label{rem:lagrangian-ptvv}
  2828	In the PTVV framework~\cite{PTVV13}, the derived intersection
  2829	$\mathcal{M}_\cA \times^h_{\mathcal{M}_{\mathrm{comp}}}
  2830	\mathcal{M}_{\cA^!}$ computes the twisted tensor product
  2831	$K_\tau(\cA, \cA^!)$; its acyclicity (equivalent to Koszulness) is
  2832	precisely the transversality of the two Lagrangians.
  2833	The proved linear shadow is Theorem~C:
  2834	$Q_g(\cA) \oplus Q_g(\cA^!) \cong
  2835	H^*(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA))$.
  2836	\end{remark}
  2837	
  2838	\begin{remark}[Conditional hypotheses and their verification]
  2839	\label{rem:lagrangian-conditional}
 succeeded in 51ms:
   430	
   431	\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
   432	\index{Theorem C!decomposition}
   433	Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
   434	identification, this theorem) produces the ambient complex;
   435	$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
   436	gives the Verdier eigenspace decomposition and its Lagrangian
   437	splitting; $\mathrm{C}_2$
   438	(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
   439	conditional bar-side BV / shifted-symplectic upgrade.
   440	The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
   441	$\sigma$ exchanging the two eigenspaces; at the scalar level
   442	the complementarity formulas below are consequences of the
   443	$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
   444	separate $\mathrm{C}_2$ label:
   445	$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
   446	while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
   447	$\mathcal{W}$-algebras (Theorem~\ref{thm:complementarity-root-datum};
   448	Table~\ref{tab:complementarity-landscape}).
   449	\end{remark}
 succeeded in 52ms:
   560	$\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)$ on $\Ran(X)$ computes
   561	the dual coalgebra image of the bar complex; passage from the
   562	ordered bar $\bar{B}^{\mathrm{ord}}(\cA)$ to the symmetric bar
   563	$\bar{B}^{\Sigma}(\cA)$ is by $\Sigma_n$-coinvariants in each bar
   564	degree. On the Koszul locus, Theorem~\ref{thm:bar-concentration}
   565	collapses $\bar{B}^{\mathrm{ch}}(\cA)$ to its cohomological
   566	diagonal; applying $\mathbb{D}_{\Ran}$ and taking totalized
   567	$\Sigma$-coinvariants identifies the result with the chiral
   568	Hochschild complex computed via bar-cobar resolution
   569	$\mathrm{Hom}(\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA)), \cA)$.
   570	The bar-cobar quasi-isomorphism
   571	(Theorem~\ref{thm:bar-cobar-isomorphism-main}) then identifies
   572	this with $\mathrm{RHom}_{\mathrm{ChirAlg}}(\cA, \cA) =
   573	\ChirHoch^{\bullet}(\cA)$, giving~\eqref{eq:chirhoch-descent}.
   574	\end{proof}
   575	
   576	\begin{theorem}[Koszul duality for Hochschild cohomology
   577	\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
   578	\label{thm:main-koszul-hoch}
   579	\index{Hochschild cohomology!Koszul duality|textbf}
 succeeded in 52ms:
  1668	
  1669	\begin{example}[Admissible-level failure of bar-cobar inversion]
  1670	\label{ex:admissible-sl2-failure}
  1671	\index{admissible level!bar-cobar inversion failure}
  1672	\index{bar-cobar inversion!admissible-level counterexample}
  1673	Consider $L_{-1/2}(\mathfrak{sl}_2)$, the simple affine vertex algebra
  1674	at the admissible level $k = -1/2$ for $\widehat{\mathfrak{sl}}_2$
  1675	(here $h^\vee = 2$, so $k + h^\vee = 3/2$; the admissible
  1676	parametrization is $k = -h^\vee + p/q$ with $p = 3$, $q = 2$).
  1677	This algebra is excluded from the Koszul locus of
  1678	Theorem~\ref{thm:bar-cobar-inversion-qi}, and we now explain the
  1679	concrete mechanism by which bar-cobar inversion fails.
  1680	
  1681	\emph{Singular vector in the bar-relevant range.}
  1682	The vacuum Verma module $M(k\Lambda_0)$ at $k = -1/2$ has a
  1683	singular vector at conformal weight $(p-1)q = 2 \cdot 2 = 4$,
  1684	produced by the Kac--Kazhdan root $\beta_{q,-} = q\delta - \alpha$
  1685	at KK value $j = p - 1 = 2$
  1686	(Kac--Wakimoto~\cite{KW88};
  1687	cf.\ Remark~\ref{rem:sl2-admissible}).
 succeeded in 52ms:
  3335	(Verdier), and the cobar functor translates back. Every other
  3336	duality in the programme, whether Poincar\'e--Koszul on manifolds,
  3337	Serre on moduli, or the $c \mapsto 26 - c$ involution on the Virasoro
  3338	line, is a specialization of this single adjunction acting on
  3339	different geometric inputs.
  3340	\end{remark}
  3341	
  3342	\begin{remark}[Curvature and coderived categories]\label{rem:curvature-coderived}
  3343	\index{coderived category!bar-cobar}
  3344	\index{curvature!coderived category}
  3345	When curvature is present, i.e., when the genus-$1$ obstruction
  3346	$m_0^{(1)} = \kappa(\cA) \cdot \lambda_1 \neq 0$ (as it is for all
  3347	Koszul chiral algebras with $\kappa(\cA) \neq 0$; see
  3348	Theorem~\ref{thm:genus-universality}), the bar complex satisfies
  3349	$\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \mathrm{id}$ rather than $\dfib^{\,2} = 0$
  3350	(see Convention~\ref{conv:higher-genus-differentials} for the notation).
  3351	The ordinary derived category of $\cA$-modules is then the wrong
  3352	quotient: it erases the distinction between ``acyclic because of
  3353	$\dfib^{\,2} \neq 0$'' and ``acyclic because of genuine exactness.''
  3354	
 succeeded in 52ms:
  4615	\end{theorem}
  4616	
  4617	\begin{proof}
  4618	The degree $-1$ pairing on $T_{\mathrm{comp}}(\cA)$ is induced from the
  4619	cyclic pairing on the direct sum by passage to the homotopy fiber.
  4620	Because the total differential is skew-adjoint, the pairing descends to
  4621	cohomology and is compatible with the differential.
  4622	
  4623	For the one-sided tangent complex $T_{\cA}$, the pullback of the ambient
  4624	pairing reduces to the quadratic term in the differentiated
  4625	Maurer--Cartan equation for the universal kernel. That quadratic term
  4626	vanishes because the Maurer--Cartan equation is exactly the isotropy
  4627	condition for the graph of the one-sided variation. The same argument
  4628	applies to $T_{\cA^!}$.
  4629	
  4630	If the cyclic pairing is perfect and bar--cobar duality identifies the
  4631	normal complex to one side with the shifted dual tangent complex of the
  4632	other, maximal isotropicity follows. This is the derived form of the
  4633	slogan that the two sides are opposite polarizations of a single
  4634	symplectic deformation problem.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4685,4728p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4685	For the Lagrangian structure: under the perfectness hypothesis,
  4686	the one-sided tangent complexes $T_\cA$ and $T_{\cA^!}$ are
  4687	complementary Lagrangians in $T_{\mathrm{comp}}(\cA)$
  4688	(Theorem~\ref{thm:ambient-complementarity-tangent}(iii)).
  4689	By the PTVV Lagrangian correspondence, isotropic sub-dg-Lie
  4690	algebras whose tangent complexes are Lagrangian
  4691	integrate to Lagrangian maps of formal moduli problems.
  4692	\end{proof}
  4693	
  4694	\subsection{The complementarity potential: direct definition}
  4695	\label{subsec:cotangent-normal-form}
  4696	
  4697	The complementarity potential is the generating function of one
  4698	Lagrangian in the cotangent chart centered at the other. We define
  4699	it directly from the cyclic deformation data and then prove its
  4700	existence via the cotangent normal form.
  4701	
  4702	\begin{definition}[Complementarity potential: direct construction]
  4703	\label{def:complementarity-potential}
  4704	Let $V_{\cA} \subset H^*(\operatorname{Def}_{\mathrm{cyc}}(\cA))$
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3412,3488p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3412	\begin{proposition}[Bar construction as factorization homology;
  3413	\ClaimStatusProvedHere]
  3414	\label{prop:bar-fh}
  3415	\index{factorization homology!bar construction}
  3416	\index{bar construction!as factorization homology}
  3417	Let $\cA$ be an augmented $\Eone$-chiral algebra on a smooth
  3418	curve~$X$, and let $\overline{\cA} = \ker(\epsilon \colon \cA \to k)$
  3419	be the augmentation ideal. Then there is a natural equivalence
  3420	\[
  3421	\Bbar^{\mathrm{geom}}_X(\cA)
  3422	\;\simeq\;
  3423	\int_X \overline{\cA}^{\mathrm{Lie}}
  3424	\]
  3425	where $\overline{\cA}^{\mathrm{Lie}}$ denotes $\overline{\cA}$ viewed as
  3426	an $\Eone$-Lie algebra via the commutator bracket, and the right-hand
  3427	side is factorization homology in the sense of
  3428	\textup{\cite{AF15, BD04}}. More precisely:
  3429	\begin{enumerate}[label=(\roman*)]
  3430	\item \textbf{Finite approximations}: For each $n \geq 1$,
  3431	the degree-$n$ piece $\Bbar^n_X(\cA) =
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2880,2978p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2880	\begin{proposition}[Perfectness for the standard landscape]
  2881	\label{prop:lagrangian-perfectness}
  2882	\ClaimStatusProvedHere
  2883	\index{Lagrangian!perfectness verification}
  2884	\index{perfectness!cyclic pairing on complementarity datum}
  2885	Let $\cA$ satisfy the standing hypotheses and the following:
  2886	\begin{enumerate}[label=\textup{(P\arabic*)}]
  2887	\item\label{item:perf-fingen}
  2888	 \textup{(Finite weight spaces)}\quad
  2889	 The conformal weight spaces $\cA_n$ are finite-dimensional for
  2890	 all~$n$, and $\cA_n = 0$ for $n \ll 0$.
  2891	\item\label{item:perf-nondeg}
  2892	 \textup{(Nondegenerate invariant form)}\quad
  2893	 The invariant bilinear form
  2894	 $\langle{-},{-}\rangle \colon \cA \otimes \cA \to \omega_X$
  2895	 restricts to a nondegenerate pairing on each weight space~$\cA_n$.
  2896	\item\label{item:perf-dual}
  2897	 \textup{(Dual regularity)}\quad
  2898	 The Koszul dual $\cA^!$ also satisfies
  2899	 \textup{(P\ref{item:perf-fingen})} and
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2978,3048p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2978	pairing is nondegenerate.
  2979	
  2980	\smallskip\noindent
  2981	\emph{Step~3: skew-adjointness of the differential.}
  2982	The differential $d = d_{\mathrm{int}} + d_{\mathrm{sew}}$
  2983	on~$\fg$ is skew-adjoint with respect to~$\omega$:
  2984	\[
  2985	\omega(d\alpha, \beta)
  2986	\;+\; (-1)^{|\alpha|}\,\omega(\alpha, d\beta)
  2987	\;=\; 0.
  2988	\]
  2989	This is the defining property of an invariant pairing on a
  2990	dg~Lie algebra and follows from
  2991	$\omega([\Theta, \alpha], \beta)
  2992	= \omega(\alpha, [\Theta, \beta])$
  2993	applied to the Maurer--Cartan element~$\Theta_\cA$ that
  2994	twists the differential.
  2995	
  2996	\smallskip\noindent
  2997	\emph{Step~4: perfectness.}

thinking
**Exploring mathematical claims**

I’m looking at the Lagrangian-unconditional claims that apply to every algebra in the standard landscape, particularly at non-critical, non-degenerate levels. However, there's this item in the meta theorem that suggests it's conditional. I'll need to read up on the Quillen equivalence theorem as well. I should also check the theorem's status since it's been proved elsewhere. It’ll be important to look into the statement to clarify its hypotheses.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '6218,6268p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6218	cohomology by genus) is a formal corollary of the bar complex being an
  6219	$\mathsf{F}\mathrm{Com}$-algebra.
  6220	The $\mathsf{F}\mathrm{Com}$-algebra structure is the strict
  6221	incarnation of the homotopy modular coalgebra on $\barB(\cA)$;
  6222	the Feynman transform provides the homotopy-invariant formulation
  6223	(Getzler--Kapranov~\cite[\S5]{GetzlerKapranov98}).
  6224	\end{remark}
  6225	
  6226	\begin{theorem}[Bar-cobar as Quillen equivalence;
  6227	\ClaimStatusProvedElsewhere]
  6228	\label{thm:quillen-equivalence-chiral}
  6229	\index{Quillen equivalence!bar-cobar|textbf}
  6230	\index{bar-cobar!Quillen equivalence}
  6231	\index{model structure!conilpotent coalgebras}
  6232	For a Koszul chiral algebra~$\cA$
  6233	\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})},
  6234	the bar-cobar adjunction
  6235	\[
  6236	B_\kappa\colon \mathrm{dg}\text{-}\mathrm{Ch\text{-}alg}
  6237	\;\rightleftarrows\;

thinking
**Exploring the pbw theorem**

I’m noticing that the pbw theorem doesn't mention E2-collapse directly; it only implies Koszulness based on certain assumptions. I wonder if there might be more insight in the corollaries related to this? It seems like I should dive deeper into the subsequent proof, especially around page 760 and onwards. Let’s figure out what further details are available in the proof about the pbw criterion and perhaps even the corollary concerning bar cohomology.
codex
I’m now checking whether the cited labels actually prove the implications claimed, not just nearby statements with similar rhetoric. The first pressure point is the PBW theorem: the meta-proof treats it as an exact equivalence with `E_2`-collapse, so I’m reading whether the cited theorem genuinely says that or only provides a one-way filtered criterion.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '720,835p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '835,1015p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"E_2-collapse|collapse at E_2|PBW spectral sequence|E_2 = E_\\infty|cor:bar-cohomology-koszul-dual|classically Koszul\" chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   720	\end{theorem}
   721	
   722	\begin{proof}
   723	Equip the Koszul complex $K = \barBgeom(\cA) \otimes_\tau \cA$ with
   724	the filtration induced by $F$:
   725	\[
   726	F_p K^n = \sum_{i+j = n} F_i \barBgeom(\cA) \otimes_\tau F_j \cA.
   727	\]
   728	This is a bounded-below, exhaustive filtration compatible with the
   729	differential (the bar differential and the twisting morphism $\tau$
   730	both respect $F$ since they are defined by the OPE, which respects
   731	conformal weight). The resulting spectral sequence has:
   732	\[
   733	E_0^{p,q} = \operatorname{gr}^p_F K^{p+q},
   734	\qquad
   735	d_0 = \operatorname{gr}_F(d_K).
   736	\]
   737	By flatness~\ref{item:pbw-flat}, the associated graded of $K$ is
   738	the Koszul complex of $\operatorname{gr}_F \cA$:
   739	\[
 exited 2 in 51ms:
rg: regex parse error:
    (?:E_2-collapse|collapse at E_2|PBW spectral sequence|E_2 = E_\infty|cor:bar-cohomology-koszul-dual|classically Koszul)
                                                                  ^^
error: unrecognized escape sequence
 succeeded in 51ms:
   835	For any central charge $c \in \bC$, the Virasoro vertex algebra
   836	$\mathrm{Vir}_c$ is chiral Koszul.
   837	\end{theorem}
   838	
   839	\begin{proof}
   840	The PBW filtration on $\mathrm{Vir}_c$ is defined by the
   841	number of Virasoro mode applications:
   842	\[
   843	F_p = \operatorname{span}\{L_{-n_1} \cdots L_{-n_r}
   844	|0\rangle : r \leq p,\; n_i \geq 2\}.
   845	\]
   846	
   847	\emph{Hypothesis~\ref{item:pbw-flat}.}
   848	Each $F_p/F_{p-1} \cong S^p(V)$ where
   849	$V = \bigoplus_{n \geq 2} \bC \cdot L_{-n}$
   850	(the Virasoro generators modulo vacuum), which is
   851	free of finite rank in each conformal weight.
   852	
   853	\emph{Hypothesis~\ref{item:pbw-classical-koszul}.}
   854	$\operatorname{gr}_F \mathrm{Vir}_c

thinking
**Searching for definitions**

I think item (i) could be problematic if it refers to the morphism or datum definition instead of focusing on the algebra property. It might be better to look up the definition for "chiral Koszul pair" since they mention it's defined later in the introduction. I should go ahead and search for that! It feels like I'm on the right track by clarifying this term before proceeding.
exec
/bin/zsh -lc "rg -n \"label\\{def:(chiral-koszul-pair|koszul-chiral-algebra|modular-koszul-chiral)\\}|Chiral Koszul pair|Koszul chiral algebra\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:584:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:627:Koszul chiral algebra in the sense of
chapters/theory/chiral_koszul_pairs.tex:3302:Let $\cA$ be a chirally Koszul chiral algebra. Then:
chapters/theory/bar_cobar_adjunction_inversion.tex:767:For a Koszul chiral algebra $\cA$ on $X$:
chapters/theory/bar_cobar_adjunction_inversion.tex:1422:weight spaces (which includes all Koszul chiral algebras arising in
chapters/theory/bar_cobar_adjunction_inversion.tex:1444:For a Koszul chiral algebra $\cA$ on a smooth curve $X$ with
chapters/theory/bar_cobar_adjunction_inversion.tex:1502:Koszul chiral algebra~$\cA$, and assume we are on a flat finite-type
chapters/theory/bar_cobar_adjunction_inversion.tex:1609:The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.
chapters/theory/bar_cobar_adjunction_inversion.tex:1916:For an arbitrary Koszul chiral algebra not on this list,
chapters/theory/bar_cobar_adjunction_inversion.tex:1963:into a complete derived invariant: two Koszul chiral algebras
chapters/theory/bar_cobar_adjunction_inversion.tex:2085:For a Koszul chiral algebra $\mathcal{A}$ (Remark~\ref{rem:koszul-chiral}), the spectral sequence from
chapters/theory/bar_cobar_adjunction_inversion.tex:2106:Let $\mathcal{A}$ be a Koszul chiral algebra satisfying the hypotheses of
chapters/theory/bar_cobar_adjunction_inversion.tex:3347:Koszul chiral algebras with $\kappa(\cA) \neq 0$; see
chapters/theory/bar_cobar_adjunction_inversion.tex:5793:Let $\cA$ be a modular Koszul chiral algebra in the
chapters/theory/bar_cobar_adjunction_inversion.tex:6223:For every modular Koszul chiral algebra~$\cA$, there exists a

thinking
**Exploring chiral-koszul-pair**

I need to read more about the definition of chiral-koszul-pair to understand it better. Also, I might want to make some comments about algebra in relation to this topic. It's important to grasp how these concepts interconnect, especially if I plan to explain them later. I'll take notes so I can refer back and really get a solid understanding. Let's dive in and see what I can find!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '560,640p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   560	$\alpha = \beta \circ f$. Then the induced map on twisted tensor
   561	products
   562	\[
   563	\mathrm{id}_\cA \otimes f \colon
   564	\cA \otimes_\alpha C \;\xrightarrow{\;\sim\;}\; \cA \otimes_\beta C
   565	\]
   566	is a quasi-isomorphism. In particular, if
   567	$\cA \otimes_\alpha C$ is acyclic, then so is
   568	$\cA \otimes_\beta C$.
   569	
   570	This is the chiral analogue of \textup{\cite[Theorem~2.4.1]{LV12}}.
   571	The proof transfers directly: filter both sides by bar degree, observe
   572	that $\mathrm{gr}(f)$ is an isomorphism (since $f$ is a quasi-isomorphism
   573	of coalgebras), and conclude by spectral sequence comparison.
   574	\end{theorem}
   575	
   576	\subsection{The concept of chiral Koszul pairs: precise formulation}
   577	
   578	To handle non-quadratic examples, we extend the notion of Koszul pairs
   579	beyond the quadratic setting. The defining property is a set of

thinking
**Checking citation details**

I noticed there’s a definition for "koszul-chiral-algebra" that I haven’t read yet. However, there’s a mis-citation regarding theorem item (i), which seems to incorrectly reference "chiral-koszul-morphism" when it should actually cite "koszul-chiral-algebra." Hmm, that might not be a strong connection. I think I’ll search for the definition of "koszul-chiral-algebra" to clarify things. Let’s see what I find!
exec
/bin/zsh -lc "rg -n \"label\\{def:koszul-chiral-algebra\\}|begin\\{definition\\}\\[.*Koszul chiral algebra|Koszul locus\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:7:%% Omega(barB(A)) -> A is a quasi-isomorphism on the Koszul locus.
chapters/theory/bar_cobar_adjunction_inversion.tex:22:answer: on the Koszul locus
chapters/theory/bar_cobar_adjunction_inversion.tex:30:bar degree. Off the Koszul locus, inversion persists in
chapters/theory/bar_cobar_adjunction_inversion.tex:689:The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
chapters/theory/bar_cobar_adjunction_inversion.tex:1606:on the Koszul locus; filtered-complete off it
chapters/theory/bar_cobar_adjunction_inversion.tex:1677:This algebra is excluded from the Koszul locus of
chapters/theory/bar_cobar_adjunction_inversion.tex:1727:level $k = -1/2$ lies outside the Koszul locus because the
chapters/theory/bar_cobar_adjunction_inversion.tex:1810:\index{Koszul locus!derived wall}
chapters/theory/bar_cobar_adjunction_inversion.tex:2080:\textup{[Regime: quadratic, Koszul locus
chapters/theory/bar_cobar_adjunction_inversion.tex:2103:\textup{[Regime: curved-central on the Koszul locus
chapters/theory/bar_cobar_adjunction_inversion.tex:2303:Koszul locus of finite-type chiral algebras. The programmatic regime
chapters/theory/bar_cobar_adjunction_inversion.tex:2525:satisfies these conditions precisely on the Koszul locus.
chapters/theory/bar_cobar_adjunction_inversion.tex:2561:On the Koszul locus, bar-cobar inversion
chapters/theory/bar_cobar_adjunction_inversion.tex:2600:and totalization preservation of $B_\kappa$ on the Koszul locus
chapters/theory/bar_cobar_adjunction_inversion.tex:2615:for~$B_\kappa$: on the Koszul locus the cosimplicial bar-cobar
chapters/theory/bar_cobar_adjunction_inversion.tex:2811:Forward: on the Koszul locus, the bar-cobar adjunction gives a
chapters/theory/bar_cobar_adjunction_inversion.tex:3072: On the Koszul locus, the twisted tensor product
chapters/theory/bar_cobar_adjunction_inversion.tex:3685:$\Omega(\barB(\cA)) \xrightarrow{\sim} \cA$ on Koszul locus
chapters/theory/bar_cobar_adjunction_inversion.tex:3691:Koszul locus: $E_2$~degeneration
chapters/theory/bar_cobar_adjunction_inversion.tex:3760:\item The chiral algebra~$\cA$ lies on the \emph{Koszul locus}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '676,726p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   676	bar-complex cohomology collapses on the higher-genus bar-object
   677	surface
   678	\textup{(}Proposition~\ref{prop:curved-bar-acyclicity}\textup{)},
   679	and a richer homological algebra is needed.
   680	
   681	The chiral analogues of Positselski's coalgebra homological
   682	algebra~\cite{Positselski11} replace the ground field~$k$ by
   683	$\mathcal{D}_X$ and the tensor product by $\chirtensor$; all
   684	exactness properties are inherited from configuration space geometry.
   685	
   686	\begin{remark}[The coderived category: status and the genus-$0$/genus-$g$ distinction]%
   687	\label{rem:coderived-status}%
   688	\index{coderived category!status}%
   689	The Koszul locus is a genus-$0$ condition on the algebra~$\cA$:
   690	bar cohomology $H^*(\barB(\cA))$ is concentrated in bar degree~$1$,
   691	the PBW spectral sequence collapses at~$E_2$, and the bar-cobar counit
   692	$\Omega(\barB(\cA)) \to \cA$ is a quasi-isomorphism
   693	(Theorem~\ref{thm:higher-genus-inversion}). On this locus, the coderived
   694	and ordinary derived categories coincide.
   695	
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2568,2830p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2568	nondegeneracy of~$\kappa$ converts a vanishing condition on
  2569	shadows ($S_3 = 0$) into a structural condition on the bracket
  2570	($[-,-] = 0$). Classes~$L$, $C$, and~$M$ all have nonzero
  2571	brackets; SC-formality is incompatible with each. The only
  2572	algebra whose bracket is already zero is Heisenberg.
  2573	\end{proof}
  2574	
  2575	\begin{remark}[D-module purity: reduction to a single gap]
  2576	\label{rem:d-module-purity-content}
  2577	\index{D-module purity!reduction to Saito weight}
  2578	\index{Saito weight filtration!and PBW filtration}
  2579	The converse direction of condition~\textup{(xii)} (Koszulness
  2580	$\Longrightarrow$ D-module purity of~$\barBgeom_n(\cA)$) admits
  2581	a five-step proof strategy. Steps~1--3 are established; step~4
  2582	is the single remaining gap.
  2583	
  2584	\begin{enumerate}[label=\textup{Step \arabic*.}]
  2585	\item
  2586	The PBW filtration $F_\bullet^{\mathrm{PBW}}$ on
  2587	$\barBgeom_n(\cA)$ is a filtration by $\cD$-submodules on
exec
/bin/zsh -lc 'rg -n "Barr--Beck|BBL|comparison functor|monadicity|fiber over|bar-cobar adjunction is a Quillen equivalence on the Koszul locus|monadic descent" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:2514:\subsubsection{Barr--Beck--Lurie characterization}
chapters/theory/bar_cobar_adjunction_inversion.tex:2516:Lurie's $\infty$-categorical Barr--Beck theorem~\cite[Theorem~4.7.3.5]{HA}
chapters/theory/bar_cobar_adjunction_inversion.tex:2523:mathematical content (unit, counit, Barr--Beck conditions on
chapters/theory/bar_cobar_adjunction_inversion.tex:2527:\begin{theorem}[Barr--Beck--Lurie characterization of chiral Koszulness;
chapters/theory/bar_cobar_adjunction_inversion.tex:2529:\index{Koszulness!Barr--Beck--Lurie characterization}
chapters/theory/bar_cobar_adjunction_inversion.tex:2530:\index{bar-cobar adjunction!Barr--Beck--Lurie conditions}
chapters/theory/bar_cobar_adjunction_inversion.tex:2534:Barr--Beck--Lurie conditions:
chapters/theory/bar_cobar_adjunction_inversion.tex:2544: $\cA$ is chirally Koszul if and only if the Barr--Beck--Lurie
chapters/theory/bar_cobar_adjunction_inversion.tex:2545: comparison functor
chapters/theory/bar_cobar_adjunction_inversion.tex:2554:in conilpotent comodules over the bar coalgebra. The comparison functor
chapters/theory/bar_cobar_adjunction_inversion.tex:2582:\mathcal{F}_n)$. On each fiber over a stratum of
chapters/theory/bar_cobar_adjunction_inversion.tex:2601:imply that the comparison functor~$\Phi$ is an equivalence.
chapters/theory/bar_cobar_adjunction_inversion.tex:2609:The three BBL conditions align with the three-pillar architecture
chapters/theory/bar_cobar_adjunction_inversion.tex:3159: The Barr--Beck--Lurie comparison functor for
chapters/theory/chiral_koszul_pairs.tex:1995:\item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
chapters/theory/chiral_koszul_pairs.tex:1996: bar-cobar adjunction is an equivalence on the fiber over
chapters/theory/chiral_koszul_pairs.tex:2177:\textsc{Barr--Beck--Lurie monadicity}
chapters/theory/chiral_koszul_pairs.tex:2181:The Barr--Beck--Lurie theorem (\cite[Theorem~4.7.3.5]{HA}) states
chapters/theory/chiral_koszul_pairs.tex:2182:that the comparison functor $\Phi$ is an equivalence if and only if
chapters/theory/chiral_koszul_pairs.tex:2191:BBL conditions because the Quillen-equivalence comparison functor
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2516,2610p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2516	Lurie's $\infty$-categorical Barr--Beck theorem~\cite[Theorem~4.7.3.5]{HA}
  2517	characterizes (co)monadic adjunctions by conservativity and totalization
  2518	preservation. We conjecture that $B_\kappa \dashv \Omega_\kappa$%
  2519	\footnote{Following Remark~\ref{rem:adjunction-direction-convention},
  2520	the canonical direction is $\Omega_\kappa \dashv B_\kappa$
  2521	(cobar left adjoint to bar). The notation $B_\kappa \dashv
  2522	\Omega_\kappa$ used here lists the right adjoint first; the
  2523	mathematical content (unit, counit, Barr--Beck conditions on
  2524	$B_\kappa$) is the same.}
  2525	satisfies these conditions precisely on the Koszul locus.
  2526	
  2527	\begin{theorem}[Barr--Beck--Lurie characterization of chiral Koszulness;
  2528	\ClaimStatusProvedHere]\label{thm:barr-beck-lurie-koszulness}
  2529	\index{Koszulness!Barr--Beck--Lurie characterization}
  2530	\index{bar-cobar adjunction!Barr--Beck--Lurie conditions}
  2531	Let $\cA$ be a chiral algebra on a smooth curve~$X$ satisfying the
  2532	standing hypotheses of Theorem~\textup{\ref{thm:bar-cobar-inversion-qi}}.
  2533	The bar-cobar adjunction $B_\kappa \dashv \Omega_\kappa$ satisfies the
  2534	Barr--Beck--Lurie conditions:
  2535	\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Examining theorem validity**

I’m thinking this could be a significant finding since item (vi) of the meta theorem relies on a theorem or proof route that assumes Koszulness. However, the meta proof doesn’t reference theorem 2527; instead, it cites BBL and the Quillen equivalence. That makes me question the reliability of the internal dedicated theorem. There's definitely more to explore here!
codex
The Barr–Beck lane is looking structurally weaker than advertised. The proof repeatedly reasons “on the Koszul locus” or under inversion/quasi-equivalence hypotheses that already amount to item `(i)`, so I’m checking whether `(vi)` is actually an independent characterization or a reformulation that only works after Koszulness has already been assumed.
exec
/bin/zsh -lc "rg -n \"FM boundary|boundary acyclicity|i_S\\"'^!|deepest stratum|binary collision|residues exact|PBW condition|d_1'"\\(e_i\\)=0|FM stratum\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:1219:computed fiberwise on each FM stratum
chapters/theory/chiral_koszul_pairs.tex:2013: $i_S^!\,\barB_n(\cA)$ to every FM boundary stratum~$S$ is
chapters/theory/chiral_koszul_pairs.tex:2025: with characteristic variety aligned to FM boundary strata.
chapters/theory/chiral_koszul_pairs.tex:2097:each FM stratum (Proposition~\ref{prop:shadow-formality-low-degree});
chapters/theory/chiral_koszul_pairs.tex:2153:\textsc{FM boundary acyclicity}
chapters/theory/chiral_koszul_pairs.tex:2158:Each FM boundary stratum $S_T \cong \prod_{v \in V(T)}
chapters/theory/chiral_koszul_pairs.tex:2168:At the deepest stratum $S = D_{\{1,2\}} \cong X \times
chapters/theory/chiral_koszul_pairs.tex:2169:\overline{\operatorname{Conf}}_{n-1}(X)$ (binary collision), the
chapters/theory/chiral_koszul_pairs.tex:2170:restriction $i_S^!\,\barB_n(\cA)$ computes the bar-complex
chapters/theory/chiral_koszul_pairs.tex:2172:Acyclicity of $i_S^!$ at all strata forces the residues at every
chapters/theory/chiral_koszul_pairs.tex:2173:collision to be exact, which is the PBW condition:
chapters/theory/chiral_koszul_pairs.tex:2596:strata of the FM boundary, each pure of weight determined
chapters/theory/chiral_koszul_pairs.tex:2691:filtration, and Saito strictness gives FM stratum
chapters/theory/chiral_koszul_pairs.tex:3349:constraint (the pentagon identity on five FM boundary
chapters/theory/chiral_koszul_pairs.tex:5899:Kac--Shapovalov determinants, FM boundary acyclicity. Two
chapters/theory/bar_cobar_adjunction_inversion.tex:2502:of this condition (descent, factorization homology, FM boundary
chapters/theory/bar_cobar_adjunction_inversion.tex:2683:\subsubsection{Fulton--MacPherson boundary acyclicity}
chapters/theory/bar_cobar_adjunction_inversion.tex:2689:\begin{theorem}[FM boundary acyclicity;
chapters/theory/bar_cobar_adjunction_inversion.tex:2691:\index{Koszulness!FM boundary acyclicity}
chapters/theory/bar_cobar_adjunction_inversion.tex:2692:\index{Fulton--MacPherson compactification!boundary acyclicity}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2683,2778p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2683	\subsubsection{Fulton--MacPherson boundary acyclicity}
  2684	
  2685	The bar complex lives on $\overline{\Conf}_n(X)$; restriction to
  2686	boundary strata encodes OPE residues. Koszulness should be equivalent
  2687	to acyclicity of all such restrictions.
  2688	
  2689	\begin{theorem}[FM boundary acyclicity;
  2690	\ClaimStatusProvedHere]\label{thm:fm-boundary-acyclicity}
  2691	\index{Koszulness!FM boundary acyclicity}
  2692	\index{Fulton--MacPherson compactification!boundary acyclicity}
  2693	Let $\cA$ be a chiral algebra on~$X$ satisfying the standing hypotheses.
  2694	Then $\cA$ is chirally Koszul if and only if for all $n \geq 2$ and every
  2695	boundary stratum $S \subset \partial \overline{\Conf}_n(X)$ with inclusion
  2696	$i_S \colon S \hookrightarrow \overline{\Conf}_n(X)$:
  2697	\[
  2698	 H^k\bigl(i_S^!\, \barBch_n(\cA)\bigr) = 0
  2699	 \quad \text{for all } k \neq 0.
  2700	\]
  2701	In words: the restriction of the $n$-th bar component to every boundary
  2702	stratum of the Fulton--MacPherson compactification is cohomologically
exec
/bin/zsh -lc "rg -n \"Theorem~H|hochschild-polynomial-growth|polynomial algebra with generators concentrated in degrees \\{0, 1, 2\\}|amplitude \\{0,1,2\\}|ChirHoch\\"'^'"\\*\\(.*\\) is a polynomial\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:1396:Theorem~H
chapters/theory/chiral_koszul_pairs.tex:1397:\textup{(Theorem~\ref{thm:hochschild-polynomial-growth})}
chapters/theory/chiral_koszul_pairs.tex:1402:Theorem~H at critical level.
chapters/theory/chiral_koszul_pairs.tex:2007: \textup{(}Theorem~H,
chapters/theory/chiral_hochschild_koszul.tex:13:Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
chapters/theory/chiral_hochschild_koszul.tex:577:\textup{(}Theorem~H\textup{)}; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:688:\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
chapters/theory/chiral_hochschild_koszul.tex:689:\label{thm:hochschild-polynomial-growth}
chapters/theory/chiral_hochschild_koszul.tex:847:By Theorem~\ref{thm:hochschild-polynomial-growth},
chapters/theory/chiral_hochschild_koszul.tex:884:\begin{remark}[What $\Etwo$-formality adds beyond Theorem~H]
chapters/theory/chiral_hochschild_koszul.tex:886:Theorem~\ref{thm:hochschild-polynomial-growth} gives concentration.
chapters/theory/chiral_hochschild_koszul.tex:2669:Theorem~H (ChirHoch$^*(\cA)$ polynomial on the Koszul locus) is a
chapters/theory/chiral_hochschild_koszul.tex:4084:vanishes for $n > 2$ by Theorem~\ref{thm:hochschild-polynomial-growth})
chapters/theory/chiral_hochschild_koszul.tex:4267:Theorem~\textup{\ref{thm:hochschild-polynomial-growth}}; the periodicity
chapters/examples/symmetric_orbifolds.tex:230:Theorem~\ref{thm:hochschild-polynomial-growth}, with degree
chapters/examples/beta_gamma.tex:65: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/y_algebras.tex:66: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/yangians_foundations.tex:1012:ring (Theorem~H). Their $\Eone$ formulations require the following
chapters/examples/moonshine.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/bershadsky_polyakov.tex:45: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '680,760p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   680	\begin{remark}[Proof infrastructure]
   681	Both proofs use the bar-cobar quasi-isomorphism at all genera
   682	(Theorem~\ref{thm:higher-genus-inversion}) and the Kodaira--Spencer map
   683	for Koszul pairs
   684	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
   685	\end{remark}
   686	
   687	\begin{theorem}[Polynomial growth of chiral Hochschild cohomology
   688	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
   689	\label{thm:hochschild-polynomial-growth}
   690	\index{Hochschild cohomology!polynomial growth|textbf}
   691	\textup{[Regime: quadratic on the Koszul locus
   692	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   693	
   694	Let $\cA$ be a chiral Koszul algebra on a smooth projective curve~$X$,
   695	and let $\cA^!$ denote its Koszul dual. Then:
   696	\begin{enumerate}[label=\textup{(\alph*)}]
   697	\item \emph{Concentration.}\;
   698	 $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
   699	 The nonvanishing range is $0 \leq n \leq 2$.

thinking
**Evaluating the theorem's clarity**

I’m noticing that this theorem only provides concentration and polynomial Hilbert series, and it doesn’t cover “polynomial algebra with generators concentrated in degrees {0,1,2}.” So, it could be that meta theorem item (viii) is stated too strongly compared to theorem H. I need to check if there’s another theorem confirming that chirHoch is indeed a polynomial algebra. I’ll search for that exact phrase to clarify things!
exec
/bin/zsh -lc "rg -n \"polynomial algebra with generators|is a polynomial algebra|ChirHoch\\"'^'"\\*\\(\\\\cA\\) is a polynomial|Hochschild complex.*polynomial algebra\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:polynomial algebra with generators|is a polynomial algebra|ChirHoch\^\*\(\cA\) is a polynomial|Hochschild complex.*polynomial algebra)
                                                                                ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n -F "polynomial algebra with generators" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_koszul_pairs.tex && rg -n -F "is a polynomial algebra" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_koszul_pairs.tex:2066:If $\ChirHoch^*(\cA)$ is a polynomial algebra with generators
chapters/theory/chiral_center_theorem.tex:1965:which is a polynomial algebra on $\operatorname{rank}(\mathfrak{g})$
chapters/theory/chiral_koszul_pairs.tex:771:For Kac--Moody and Virasoro algebras, $\operatorname{gr}_F \cA$ is a polynomial algebra (Koszul by Priddy's theorem); semisimplicity of $\mathfrak{g}$ is not required.
chapters/theory/chiral_koszul_pairs.tex:806:This is a polynomial algebra on the generators
chapters/theory/chiral_koszul_pairs.tex:856:is a polynomial algebra (the OPE reduces to a commutative
chapters/theory/chiral_koszul_pairs.tex:2005:\item[\textup{(viii)}] $\mathrm{ChirHoch}^*(\cA)$ is a polynomial algebra
chapters/theory/chiral_koszul_pairs.tex:2066:If $\ChirHoch^*(\cA)$ is a polynomial algebra with generators


thinking
**Evaluating theorem discrepancies**

I’m considering that the chiral center theorem might only apply to a specific family rather than generally. Item (viii) could be overreaching. I should check Theorem H to see if it involves polynomial algebra, though it cites other theorems that don't explicitly mention it. This discrepancy may indicate a critical issue, as the proof may rely on stronger assumptions than stated. I need to verify the proofs and assumptions of the relevant theorems to clarify this.
thinking
**Investigating theorem gaps**

I’m looking at the theorem main-koszul-hoch, which shows duality but doesn’t involve "polynomial algebra." It also seems like I need line numbers for clarity. Item (v) to (viii) might indicate free resolution, suggesting polynomial vanishing, but that’s not explicitly stated. I need to assess whether the proof relies on condition (viii) as an algebra structure. There’s a genuine gap here since there’s no supporting theorem. I should also check item (iv) on Ext diagonal vanishing and its connections.
codex
A second hard failure has appeared: item `(viii)` is written as “`\mathrm{ChirHoch}^*(\cA)` is a polynomial algebra with generators in degrees `{0,1,2}`,” but the cited Hochschild theorems I’ve read only give concentration and a polynomial Hilbert series, not freeness as a polynomial algebra. I’m checking whether there is any other theorem in scope that supplies the missing algebra-structure claim; if not, the `(viii)` equivalence chain is materially overstated.
exec
/bin/zsh -lc 'rg -n "bar resolution computes Ext|bar-computes-ext|Ext.*bar resolution|bar resolution.*Ext|Ext''^{p,q}|ChirHoch'"\\"'^'"\\*\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:bar resolution computes Ext|bar-computes-ext|Ext.*bar resolution|bar resolution.*Ext|Ext^{p,q}|ChirHoch\^\*)
                                                                                                 ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc 'rg -n -F "bar resolution computes Ext" chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex
rg -n -F "bar-computes-ext" chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex
rg -n -F "Ext''^{p,q}" chapters/theory/chiral_koszul_pairs.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
chapters/theory/chiral_koszul_pairs.tex:1304:the diagonal $p = q$; since the bar resolution computes Ext,
chapters/theory/chiral_koszul_pairs.tex:2241:$p = q$; the bar resolution computes Ext, so
chapters/theory/chiral_koszul_pairs.tex:1459:\textup{(}Corollary~\ref{cor:bar-computes-ext}\textup{)}.
exec
/bin/zsh -lc "rg -n \"label\\{cor:bar-computes-ext\\}|bar computes Ext\" chapters/theory/chiral_koszul_pairs.tex chapters/theory/*" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_curved.tex:6440: \ClaimStatusProvedElsewhere]\label{cor:bar-computes-ext}
chapters/theory/bar_cobar_adjunction.aux:527:\newlabel{cor:bar-computes-ext}{{8.2.22}{490}{Bar cohomology computes Ext; \ClaimStatusProvedElsewhere }{corollary.8.2.22}{}}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '6428,6465p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  6428	bar differential with the standard one.
  6429	
  6430	The Costello--Gwilliam MC equation $\delta I + \frac{1}{2}\{I,I\} = 0$
  6431	for the quantum effective action~$I$~\cite[Definition~3.2.1.1]{CG-vol2}
  6432	is equation~\eqref{eq:mc-equation} in the field theory context:
  6433	central charges in QFT correspond to central curvature in chiral
  6434	algebras, and both ensure that quantum corrections do not destroy
  6435	associativity.
  6436	
  6437	\subsection{Computational corollaries}
  6438	
  6439	\begin{corollary}[Bar cohomology computes Ext;
  6440	 \ClaimStatusProvedElsewhere]\label{cor:bar-computes-ext}
  6441	For a chiral algebra $\mathcal{A}$ with central curvature,
  6442	the bar construction computes self-Ext of the vacuum module:
  6443	\begin{equation}
  6444	H^*(\bar{B}(\mathcal{A}), d_{\text{bar}}) =
  6445	\operatorname{Ext}_{\mathcal{A}}^*(\omega_X, \omega_X).
  6446	\end{equation}
  6447	This is the chiral analogue of the classical bar-Ext

thinking
**Evaluating contradictions in theorems**

I'm noticing a direct contradiction within the same file — one part states that chirally Koszul holds at all levels, while another remark indicates that full Koszulness fails at a critical point. It's like, how can both be true? The meta theorem claiming ten unconditional equivalences might be picking up on this confusion. I need to dig deeper to clarify these concepts and make sense of them!
codex
A much stronger crack just opened. In the same file, the manuscript says both “`V_k(\mathfrak g)` is chirally Koszul at all levels, including `k=-h^\vee`” and, a few lines later, that at critical level only PBW degeneration survives while “full Koszulness … fails.” If that survives re-reading, it gives an explicit boundary regime where the advertised unconditional equivalence chain breaks.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1338,1403p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7178,7200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "critical level" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex chapters/theory/hochschild_cohomology.tex | head -n 80' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1338	
  1339	\begin{corollary}[Universal vertex algebras are chirally Koszul;
  1340	\ClaimStatusProvedHere]
  1341	\label{cor:universal-koszul}
  1342	\index{Koszul property!universal algebras}
  1343	
  1344	The following are chirally Koszul:
  1345	\begin{enumerate}
  1346	\item $V_k(\fg)$ at all levels~$k$ \textup{(}including $k = -h^\vee$\textup{)},
  1347	 since its vacuum module is Verma with no null vectors.
  1348	\item $\mathrm{Vir}_c$ as the universal vertex algebra at all~$c$,
  1349	 since the vacuum Verma module is freely strongly generated.
  1350	\item $\mathcal{W}^k(\fg)$ obtained by Drinfeld--Sokolov reduction,
  1351	 by the Feigin--Frenkel theorem \textup{(}the Miura images freely
  1352	 generate\textup{)}.
  1353	\end{enumerate}
  1354	
  1355	\noindent\textbf{The universal vs.\ simple distinction.}
  1356	The universal algebra $V_k(\fg)$ is always chirally Koszul.
  1357	The simple quotient $L_k(\fg) = V_k(\fg)/I_k$ may fail Koszulness
 succeeded in 50ms:
  7178	 The topologization theorem
  7179	 (Theorem~\ref{thm:topologization}:
  7180	 $\SCchtop + \text{inner conformal vector} = E_3$)
  7181	 is proved for affine Kac--Moody at non-critical level.
  7182	 For general chiral algebras with conformal vector,
  7183	 topologization is conjectural
  7184	 (Conjecture~\ref{conj:coderived-e3} gives the
  7185	 $D^{\mathrm{co}}$-level upgrade).} \\
  7186	\hline
  7187	\multicolumn{3}{p{13cm}}{%
  7188	 \textbf{Critical level: Theorem~H does NOT apply.}
  7189	 At the critical level $k = -h^\vee$ for affine KM,
  7190	 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
  7191	 (Feigin--Frenkel center). Theorem~H (polynomial Hilbert
  7192	 series, cohomological degrees $\{0,1,2\}$) requires
  7193	 generic level. For $\widehat{\fsl}_2$ at critical level,
  7194	 $\ChirHoch^*$ is unbounded and $4$-periodic.} \\
  7195	\end{tabular}
  7196	\end{center}
  7197	
 succeeded in 50ms:
chapters/connections/concordance.tex:239:at the critical level $k = \critLevel$, where $\kappa = 0$
chapters/connections/concordance.tex:359: At the critical level $k = -h^\vee$, the bar complex is uncurved
chapters/connections/concordance.tex:389: At critical level $k = \critLevel$:
chapters/connections/concordance.tex:439:$\barB(\widehat{\fg}_{-h^\vee})$ at critical level is a
chapters/connections/concordance.tex:2169: and all non-critical levels, $S_3$ doubles ($1 \to 2$),
chapters/connections/concordance.tex:3085:(iii)~the critical level $k = -h^\vee$ does not break Koszulness of the
chapters/connections/concordance.tex:3318:rational~$k$ (admissible/critical levels), where vacuum null
chapters/connections/concordance.tex:3468: proved elsewhere): DS reduction at non-critical level =
chapters/connections/concordance.tex:3642: Volume~II principal-case theorem for DS reduction at non-critical level.
chapters/connections/concordance.tex:4160:This includes: all principal $\cW_N$ at non-critical levels,
chapters/connections/concordance.tex:4717: & concentration in $\{0,1,2\}$ (de~Rham bound on curve); & critical level: ProvedElsewhere) & \ref{thm:virasoro-hochschild}, \ref{thm:critical-level-cohomology}; \\
chapters/connections/concordance.tex:4791:$\mathfrak{sl}_2$ at degree~$2$: $\Sigma_2 = \{0\}$ (critical level
chapters/connections/concordance.tex:5403:all non-critical levels including admissible ones.
chapters/connections/concordance.tex:5889:(critical level $k=-2$, where the center acquires opers).
chapters/connections/concordance.tex:7148: conformal vector at non-critical level yields
chapters/connections/concordance.tex:7181: is proved for affine Kac--Moody at non-critical level.
chapters/connections/concordance.tex:7189: At the critical level $k = -h^\vee$ for affine KM,
chapters/connections/concordance.tex:7193: generic level. For $\widehat{\fsl}_2$ at critical level,
chapters/connections/concordance.tex:7874:\index{critical level!orthogonal axis|textbf}
chapters/connections/concordance.tex:7875:\index{shadow tower!orthogonal to critical level|textbf}

thinking
**Inspecting theorem contradictions**

I’m noticing an explicit contradiction related to the critical level and the Koszulness of the bar-cobar inversion theorem. I think it would be worthwhile to inspect line 3085 of the concordance for more details. There could be a conflict, but maybe this issue lies outside the theorem itself. I wonder if I should mention the propagation drift across the concordance as well while I search around line 3085 for clarity.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '3076,3092p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3076	range; $L_k(\mathfrak{sl}_3)$ at admissible $q \geq 3$:
  3077	$\mathrm{rk}(\mathfrak{sl}_3) = 2$ Cartan classes survive in
  3078	$H^2(\barB)$), 2 open ($L_1(\mathfrak{sl}_2)$ and triplet $\cW(2)$).
  3079	Five corrections to initial expectations:
  3080	(i)~the symplectic fermion IS Koszul (class~C, PBW universality;
  3081	logarithmic phenomena affect the module category, not the bar complex;
  3082	Remark~\ref{rem:symplectic-logarithmic});
  3083	(ii)~quotient of a Koszul algebra need not be Koszul
  3084	($L_1(\mathfrak{sl}_2)$: null at $h=2$ in bar range);
  3085	(iii)~the critical level $k = -h^\vee$ does not break Koszulness of the
  3086	universal algebra $V_k(\fg)$;
  3087	(iv)~admissible Koszulness for simple quotients is
  3088	\emph{rank-dependent}: $L_k(\mathfrak{sl}_2)$ is Koszul at all
  3089	admissible levels, but $L_k(\mathfrak{sl}_3)$ at $q \geq 3$ is not,
  3090	with the obstruction coming from the abelian Cartan subalgebra
  3091	(Remark~\ref{rem:admissible-koszul-status},
  3092	Conjecture~\ref{conj:admissible-koszul-rank-obstruction});




thinking
**Analyzing theorem proof issues**

Concordance seems to indicate the critical level doesn't disrupt Koszulness, which conflicts with what I've noted. Since the user wants the proof for the audit theorem, cross-propagation is important. I might need to dive into details about status drift and consider cross-volume effects. I must check if concordance restricts Theorem H generically. I could cite both concepts. However, I am concerned about whether the theorem's definitions and conditions are adequately stated or missing certain critical aspects.
thinking
**Identifying hidden assumptions**

I need to pinpoint some serious hidden assumptions here. For example, the lemma regarding the twisted-product-cone-counit needs a specific chiral twisting datum, not just any arbitrary A. The meta theorem mentions this after item (v) referencing the bar-cobar counit quasi-isomorphism and how it leads to the twisted tensor product K_tau^L being acyclic, which is crucial for the chiral-Koszul-morphism definition. Yet, the theorem doesn’t clarify any C or tau, which might be a problem if it assumes there's an implicit canonical bar twisting datum. There’s also a lack of specifics regarding conilpotence or completeness in other theorems. This could definitely be a significant oversight.
thinking
**Evaluating bigrading conventions**

I need to examine bigrading conventions more closely. It seems like the E_r differential of degree (r,1-r) moves from row q to q-r+1. If the abutment focuses on the diagonal p=q, then off-diagonal classes could diminish due to differentials. It doesn't appear to contradict anything, which indicates that the proof from (iv) to (i) doesn't hold up. I’m curious to figure this out more!
thinking
**Searching for theorems**

I’m looking to find out if there's another theorem that establishes the Ext diagonal equivalent to Koszulness, maybe similar to the BGS-type theorem. I should check the file to see if any information is present there. It's important to gather all relevant information about this topic to ensure I can provide a solid answer. I'll keep digging until I find something helpful or conclusive!
codex
The Ext-diagonal lane is also under pressure. The current proof argues that if the abutment is diagonal then all higher differentials must vanish, but that is not how spectral sequences work in general: off-diagonal terms can die by higher differentials and still leave a diagonal `E_\infty`. I’m checking whether there is a separate BGS-style theorem in the manuscript that really proves `(iv) ⇒ (i)`; absent that, this implication is a genuine gap.
exec
/bin/zsh -lc 'rg -n "diagonal Ext|Ext diagonal|diagonal concentration|BGS|Beilinson--Ginzburg--Soergel|Koszul if and only if.*Ext|Ext.*iff" chapters/theory/chiral_koszul_pairs.tex chapters/theory/*' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/algebraic_foundations.tex:322:\begin{theorem}[Classical Koszul pairs; \ClaimStatusProvedElsewhere{} \cite{Priddy70,BGS96,LV12}]
chapters/theory/algebraic_foundations.aux:39:\citation{BGS96}
chapters/theory/algebraic_foundations.aux:50:\@writefile{loe}{\contentsline {theorem}{\ifthmt@listswap Theorem~3.1.11\else \numberline {3.1.11}Theorem\fi \thmtformatoptarg {Classical Koszul pairs; {} \cite  {Priddy70,BGS96,LV12}}}{228}{theorem.3.1.11}\protected@file@percent }
chapters/theory/algebraic_foundations.aux:51:\newlabel{thm:quadratic-koszul}{{3.1.11}{228}{Classical Koszul pairs; \ClaimStatusProvedElsewhere {} \cite {Priddy70,BGS96,LV12}}{theorem.3.1.11}{}}
chapters/theory/chiral_modules.aux:247:\citation{BGS96}
chapters/theory/chiral_modules.aux:576:\citation{BGS96}
chapters/theory/chiral_modules.aux:577:\citation{BGS96}
chapters/theory/chiral_modules.aux:578:\citation{BGS96}
chapters/theory/chiral_modules.aux:588:\@writefile{loe}{\contentsline {proposition}{\ifthmt@listswap Proposition~15.10.6\else \numberline {15.10.6}Proposition\fi \thmtformatoptarg {Affine Hecke algebra and Koszul duality {\cite  {BGS96}}; }}{1265}{proposition.15.10.6}\protected@file@percent }
chapters/theory/chiral_modules.aux:589:\newlabel{prop:affine-hecke-kd}{{15.10.6}{1265}{Affine Hecke algebra and Koszul duality {\cite {BGS96}}; \ClaimStatusProvedElsewhere }{proposition.15.10.6}{}}
chapters/theory/chiral_koszul_pairs.tex:10:Beilinson--Ginzburg--Soergel~\cite{BGS96}, works for graded
chapters/theory/chiral_koszul_pairs.tex:35:admit a quadratic presentation, and the BGS theory does not see
chapters/theory/chiral_koszul_pairs.tex:1277:\begin{theorem}[Ext diagonal vanishing criterion; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:1291:Beilinson--Ginzburg--Soergel criterion for $\operatorname{Zhu}(\cA)$
chapters/theory/chiral_koszul_pairs.tex:1292:\cite{BGS96}.
chapters/theory/chiral_koszul_pairs.tex:1307:Converse: diagonal concentration forces all PBW differentials
chapters/theory/chiral_koszul_pairs.tex:1363:\begin{remark}[Critical level: PBW degeneration vs diagonal Ext concentration]
chapters/theory/chiral_koszul_pairs.tex:1386:diagonal concentration is lost.
chapters/theory/chiral_koszul_pairs.tex:1393:\textup{(}diagonal Ext concentration\textup{)}
chapters/theory/chiral_koszul_pairs.tex:1739:\item \emph{Sufficiency from diagonal concentration of the
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1270,1320p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1270	cohomology has off-diagonal bigraded classes, the homotopy Koszul
  1271	dual $\cA^!_\infty$ carries genuine higher chiral operations
  1272	measuring non-formality. The shadow obstruction tower
  1273	(Remark~\ref{rem:ainfty-genus0-shadow}) is the all-genera lift of
  1274	this phenomenon.
  1275	\end{example}
  1276	
  1277	\begin{theorem}[Ext diagonal vanishing criterion; \ClaimStatusProvedHere]
  1278	\label{thm:ext-diagonal-vanishing}%
  1279	\index{Koszul property!Ext criterion}
  1280	\index{Ext algebra!diagonal vanishing}
  1281	
  1282	Define the \emph{chiral Ext algebra}
  1283	$\operatorname{Ext}^{*,*}_\cA(\omega_X, \omega_X)
  1284	= \bigoplus_{p,q} \operatorname{Ext}^{p,q}_\cA(\omega_X, \omega_X)$,
  1285	bigraded by cohomological degree~$p$ and conformal weight~$q$.
  1286	Then $\cA$ is chirally Koszul if and only if
  1287	$\operatorname{Ext}^{p,q}_\cA(\omega_X, \omega_X) = 0$ for $p \neq q$.
  1288	
  1289	\smallskip\noindent\textbf{Classical precedent.}






thinking
**Reviewing logic flaws**

I'm realizing that the theorem contains flawed converse logic. The item (iv) mentions the Ext diagonal, making it necessary to reference theorem 1277 as flawed proof. I should cross-check for counterexamples, particularly since there's a critical remark pointing to a possible PBW degeneration at E2, but the diagonal fails. The critical level indicates that item (ii) is true and item (iv) is false, which disproves the "if and only if." This means theorem 1277, as stated, is likely false unless critical levels are excluded.
thinking
**Analyzing Theorem 1277**

I'm noticing that theorem 1277 mentions a chirally Koszul condition being equivalent to the Ext diagonal. However, the critical level suggests that V_{-h∨} might not fit this criterion. There's a corollary that indicates universal Koszulness, but the remark points out that full Koszulness fails. This leads me to wonder if the manuscript treats chirally Koszul as full Koszulness or as PBW degeneration. There's a lack of clarity, especially with the explicit remark clarifying that there's a distinction between the two concepts. This shows some instability in how "chirally Koszul" is defined.
thinking
**Reviewing the theorem**

I think I can reference object/status/scope drift as a critical point because it undermines the theorem's meta proof. That's important! I might also consider examining condition (iii) with A∞ at the critical level, although maybe that's not necessary. I've already gathered several strong findings that support my analysis, which should provide a solid foundation for my conclusions. I just need to be careful in how I present this information to ensure clarity and accuracy.
thinking
**Considering factorization homology**

I think there's a possible issue regarding how the prop bar-fh identifies bar construction. It seems to interpret it as factorization homology of the augmentation ideal, which is framed as a Lie algebra. But wait, is it distinguishing this from factorization homology ∫_Σg A over the surface Σ_g? I wonder how this impacts the overall understanding of the concepts at play. It might need further observation to clarify these differences.
thinking
**Evaluating mathematical proofs**

I need to check item (vii) regarding the use of Goodwillie filtration and how "bar complex is factorization homology" relates, though it lacks citation to genus. But I wonder if that’s acceptable. Additionally, I should look into theorem xii, which might just be a partial theorem. Hmm, it seems to be okay, but I’ll make sure to keep my eye on it to see if further clarification is needed.
thinking
**Considering the inversion theorem**

I’m trying to see if the inversion theorem applies generally. The theorem from 1604 speaks of a Koszul chiral algebra, which might include some critical aspects. However, the scope excludes simple quotients and minimal models, which raises the question of whether this means it's not critical universal. It specifically mentions excluding simple admissible-level quotients and minimal-model central charges, which is an interesting detail to ponder.
exec
/bin/zsh -lc 'rg -n -F "critical level" chapters/theory/bar_cobar_adjunction_inversion.tex | head -n 80' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1768:non-Koszul (critical level, no finite collapse).
1913:for Heisenberg, affine Kac--Moody at non-critical level, Virasoro,
1972:When $K = 0$ (affine Kac--Moody at non-critical level, Heisenberg,
3033:$\mathcal{W}$-algebras at non-critical level, and all free-field
3110:form degenerates: at the critical level $k = -h^\vee$ for
4662:The Whitehead decomposition applies at all non-critical levels, so
4781:Virasoro Koszul self-dual point ($c=13$) is \emph{not} at critical level.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3098,3122p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3098	(P\ref{item:perf-nondeg}): the invariant form is the Killing
  3099	form (nondegenerate at $k \neq -h^\vee$ for Kac--Moody), the
  3100	Shapovalov form (nondegenerate at generic~$c$ for Virasoro),
  3101	or the canonical pairing for free fields.
  3102	(P\ref{item:perf-dual}): Koszul duality preserves the positive-energy
  3103	grading and finite-dimensionality of weight spaces; the dual
  3104	pairing inherits nondegeneracy from the original.
  3105	\end{proof}
  3106	
  3107	\begin{remark}[Scope and degeneration locus]
  3108	\label{rem:lagrangian-degeneration-locus}
  3109	The Lagrangian criterion degenerates precisely where the invariant
  3110	form degenerates: at the critical level $k = -h^\vee$ for
  3111	Kac--Moody, and at central charges where the Kac determinant
  3112	$\det G_h(c)$ vanishes (admissible levels for Virasoro).
  3113	At these points, the cyclic pairing develops a kernel and
  3114	perfectness fails, so the formal moduli problem
  3115	$\cM_{\mathrm{comp}}$ may not carry a well-defined
  3116	$(-1)$-shifted symplectic structure. This degeneration locus
  3117	is the same locus where the Shapovalov form degenerates
exec
/bin/zsh -lc "rg -n \"label\\{conj:lagrangian-koszulness\\}|Lagrangian criterion|transverse Lagrangians|derived intersection computes the twisted tensor product|Conjecture.*lagrangian-koszulness\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:2781:\subsubsection{Lagrangian criterion in the shifted-symplectic deformation space}
chapters/theory/bar_cobar_adjunction_inversion.tex:2791:\label{conj:lagrangian-koszulness}%
chapters/theory/bar_cobar_adjunction_inversion.tex:2794:\index{shifted-symplectic!Lagrangian criterion for Koszulness}
chapters/theory/bar_cobar_adjunction_inversion.tex:2821:Converse: transverse Lagrangians in a $(-1)$-shifted symplectic
chapters/theory/bar_cobar_adjunction_inversion.tex:2876:Lagrangian criterion to an unconditional equivalence for the
chapters/theory/bar_cobar_adjunction_inversion.tex:3015:\begin{corollary}[Unconditional Lagrangian criterion for the
chapters/theory/bar_cobar_adjunction_inversion.tex:3019:\index{Koszulness!Lagrangian criterion unconditional}
chapters/theory/bar_cobar_adjunction_inversion.tex:3021:Under hypotheses \textup{(P1)--(P3)}, the Lagrangian criterion
chapters/theory/bar_cobar_adjunction_inversion.tex:3040:apply the Lagrangian criterion
chapters/theory/bar_cobar_adjunction_inversion.tex:3109:The Lagrangian criterion degenerates precisely where the invariant
chapters/theory/bar_cobar_adjunction_inversion.tex:3134:This does \emph{not} render the Lagrangian criterion~(K11) fully
chapters/theory/chiral_koszul_pairs.tex:1149:perfectness/nondegeneracy (K11, the Lagrangian criterion), and one
chapters/theory/chiral_koszul_pairs.tex:2020:\item[\textup{(xi)}] The Lagrangian criterion: $\cM_\cA$ and
chapters/theory/chiral_koszul_pairs.tex:2021: $\cM_{\cA^!}$ are transverse Lagrangians in the $(-1)$-shifted
chapters/theory/chiral_koszul_pairs.tex:2262:\textsc{Lagrangian criterion}
chapters/theory/chiral_koszul_pairs.tex:2283:If $\cM_\cA$ and $\cM_{\cA^!}$ are transverse Lagrangians,
chapters/theory/chiral_koszul_pairs.tex:5900:characterizations remain partially open: the Lagrangian criterion
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2784,2826p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2784	(Conjecture~\ref{conj:ambient-complementarity},
  2785	Theorem~\ref{thm:ambient-complementarity-fmp}) equips the modular
  2786	deformation space with a $(-1)$-shifted symplectic structure.
  2787	Koszulness should be Lagrangian transversality.
  2788	
  2789	\begin{conjecture}[Conditional Lagrangian characterization of chiral Koszulness;
  2790	\ClaimStatusConjectured]%
  2791	\label{conj:lagrangian-koszulness}%
  2792	\index{Koszulness!Lagrangian characterization}
  2793	\index{Lagrangian!transversality and Koszulness}
  2794	\index{shifted-symplectic!Lagrangian criterion for Koszulness}
  2795	Suppose the ambient complementarity tangent complex $T_{\mathrm{comp}}(\cA)$
  2796	carries a $(-1)$-shifted symplectic structure~$\omega$ \textup{(}as in
  2797	Theorem~\textup{\ref{thm:ambient-complementarity-fmp})}, and the
  2798	one-sided deformation maps
  2799	\[
  2800	 i_{\cA} \colon \mathcal{M}_{\cA} \longrightarrow \mathcal{M}_{\mathrm{comp}},
  2801	 \qquad
  2802	 i_{\cA^!} \colon \mathcal{M}_{\cA^!} \longrightarrow \mathcal{M}_{\mathrm{comp}}
  2803	\]

thinking
**Identifying the Lagrangian criterion**

Okay, I've realized that the underlying Lagrangian criterion is actually just a conjecture! But there's this corollary, "lagrangian-unconditional," at 3015 claiming some kind of unconditional equivalence based on hypotheses by applying the conjecture from lines 3040-3041. I definitely need to read the proof from lines 3037-3041 onward for clarification. It's shaping up to be an interesting exploration!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3036,3060p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3036	
  3037	\begin{proof}
  3038	We verify the three hypotheses of
  3039	Theorem~\ref{thm:ambient-complementarity-fmp} and then
  3040	apply the Lagrangian criterion
  3041	(Theorem~\ref{conj:lagrangian-koszulness}).
  3042	
  3043	\smallskip\noindent
  3044	\emph{(1) Formal moduli problem with $(-1)$-shifted symplectic
  3045	structure.}
  3046	The dg~Lie algebra $\fg := \Defcyc^{\mathrm{mod}}(\cA)$ is
  3047	complete and filtered (by genus). By the Lurie--Pridham
  3048	correspondence \cite{LurieDAGX, Pridham17}, $\fg$ integrates
  3049	to a formal moduli problem $\cM_{\mathrm{comp}}(\cA)$ with
  3050	tangent complex $\fg[1]$.
  3051	Proposition~\ref{prop:lagrangian-perfectness} gives perfectness
  3052	of the degree~$-1$ invariant pairing on~$\fg$
  3053	under~(P1)--(P3).
  3054	By the PTVV/Kontsevich--Pridham principle \cite{PTVV13,Pridham17},
  3055	a perfect invariant pairing of degree~$-1$ on a dg~Lie algebra






thinking
**Checking theorem xii**

I need to check if Theorem XII's one-directional implication is valid. There might not be any issues, but I’m not sure if the proof for item XII is included here—only a remark about D-module purity. The theorem claims that XII implies X, which suggests it’s a one-directional statement. There’s also a conjecture in inversion file 2736 that involves an 'if and only if' condition, but the meta theorem only asserts that XII leads to X.
thinking
**Evaluating polynomial examples**

I think some examples might illustrate that specific algebra is polynomial, but there doesn’t seem to be a general theorem backing it up. To be thorough, I should search for something like "thm:chirhoch-polynomial" in related documents. I didn’t find much support aside from examples, which suggests that item (viii) is unsupported. I should also check if item (iii) has any issues with its direction. Overall, I need to weigh the findings carefully, especially since the user wants a complete resolution.
thinking
**Analyzing polynomial structure**

I see a potential issue in lines 2065-2076 where item (viii) states that "bar resolution computes Ext by Beilinson-Drinfeld comparison," claiming that the polynomial structure forces diagonal concentration due to generators of degrees 0, 1, and 2. However, having generators of these degrees doesn’t automatically imply that Ext maintains bigrading on the diagonal unless the internal weights match the cohomological degrees perfectly. It seems they assume that generator degrees correspond to q equaling p, but item (viii) only mentions cohomological degrees, not conformal weight.
thinking
**Checking proof justification**

I need to inspect line 2157 onward because the statement "restrictions of degree-0 objects remain in degree 0" might not be properly justified. I could mention that the i^! shifts by codimension, which seems important. I want to make sure that i^! indeed refers to the !-restriction of D-modules here, as that adds strength to the argument. It's essential I clarify this for accuracy.
thinking
**Counting checked instances**

I need to define the number of theorem or proof surfaces that I've checked, since the user is asking for instances. I might count 12 equivalence items checked or number of proof steps. It could make sense to say "Instances checked: 12 conditions + 11 cited dependency surfaces = 23." Being accurate is essential, so I should track everything I read. I might also mention that I need to count significant surfaces read to keep everything clear.
thinking
**Evaluating theorem and slogans**

I’m thinking about mentioning how the concordance, outlook, and holographic codes repeat the 10+1+1 slogan. But it seems the theorem proof itself might not support that. Maybe we could search to see if we need all the lines. Also, I realize we already have a concordance entry from back in 1991 that may be useful. Let’s clarify these points, as they could be crucial in making the argument.
codex
I’ve confirmed the critical-level contradiction locally in `chiral_koszul_pairs.tex`. I’m doing one last propagation pass across the summary surfaces now, so the final report distinguishes “the theorem is broken locally” from “the same broken count is also advertised elsewhere.”
exec
/bin/zsh -lc "nl -ba chapters/connections/outlook.tex | sed -n '229,238p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1988,1995p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2516,2556p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_codes_koszul.tex | sed -n '40,44p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1988	Conjecture~\ref{conj:rank-independence-step2}; residual DK-4/5 downstream\textup{)},
  1989	DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
  1990	and the Koszulness characterization programme
  1991	(10 unconditional, 1 conditional, 1 one-directional;
  1992	Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
  1993	appendices touches it except to cross-reference from it.
  1994	
  1995	\subsection*{Ring~2: The nonlinear characteristic layer}
 succeeded in 52ms:
   229	\section{Koszulness characterization programme}
   230	\label{sec:concordance-koszulness-programme}
   231	\index{Koszulness!characterization programme|textbf}
   232	
   233	The meta-theorem (Theorem~\ref{thm:koszul-equivalences-meta}) lists
   234	twelve characterizations of chiral Koszulness: ten unconditional equivalences, one conditional on perfectness/nondegeneracy, and one partially proved (D-module purity, forward direction only).
   235	Shadow depth $r_{\max}$ classifies the \emph{complexity} of Koszul
   236	algebras ($\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classes),
   237	not Koszulness itself. The single-line dichotomy
   238	(Theorem~\ref{thm:single-line-dichotomy}) proves that on any
 succeeded in 52ms:
    40	\noindent
    41	The characterizations of Koszulness (K1--K12,
    42	Theorem~\ref{thm:koszul-equivalences-meta}: 10 unconditionally
    43	equivalent, 1~conditional on perfectness, 1~one-directional) yield
    44	corresponding conditions for the holographic code to admit exact recovery.
 succeeded in 52ms:
  2516	Lurie's $\infty$-categorical Barr--Beck theorem~\cite[Theorem~4.7.3.5]{HA}
  2517	characterizes (co)monadic adjunctions by conservativity and totalization
  2518	preservation. We conjecture that $B_\kappa \dashv \Omega_\kappa$%
  2519	\footnote{Following Remark~\ref{rem:adjunction-direction-convention},
  2520	the canonical direction is $\Omega_\kappa \dashv B_\kappa$
  2521	(cobar left adjoint to bar). The notation $B_\kappa \dashv
  2522	\Omega_\kappa$ used here lists the right adjoint first; the
  2523	mathematical content (unit, counit, Barr--Beck conditions on
  2524	$B_\kappa$) is the same.}
  2525	satisfies these conditions precisely on the Koszul locus.
  2526	
  2527	\begin{theorem}[Barr--Beck--Lurie characterization of chiral Koszulness;
  2528	\ClaimStatusProvedHere]\label{thm:barr-beck-lurie-koszulness}
  2529	\index{Koszulness!Barr--Beck--Lurie characterization}
  2530	\index{bar-cobar adjunction!Barr--Beck--Lurie conditions}
  2531	Let $\cA$ be a chiral algebra on a smooth curve~$X$ satisfying the
  2532	standing hypotheses of Theorem~\textup{\ref{thm:bar-cobar-inversion-qi}}.
  2533	The bar-cobar adjunction $B_\kappa \dashv \Omega_\kappa$ satisfies the
  2534	Barr--Beck--Lurie conditions:
  2535	\begin{enumerate}[label=\textup{(\roman*)}]






thinking
**Reviewing theorem lines**

I’m checking if theorem meta proof lines 2107-2150 explicitly states the g0 scope. I might want to search for the bar-cobar inversion main label versus inversion qi, though it could be unnecessary. I'll read the specific line numbers for theorem BBL proof on comparison equivalence and conversativity, as I already have lines 2559-2605. I might need to look into theorem xi (conditional Lagrangian) and see if it aligns with the conjecture's lines 2789-2808.
thinking
**Inspecting theorems and corollaries**

I think I should note that xii is the +1 partial and it seems consistent with the remark about d-module purity content. It’s not a concrete finding, but it might be worth mentioning in the summary. I need to check cor universal-Koszul against the theorem regarding E2 collapse. The critical remark points out that while PBW degeneration endures, full Koszulness doesn't. This suggests that theorem item (ii) isn't equivalent to (iv)/(viii) for all k. I might report on this with lines 1344-1399 and theorem lines 1970-2008.
thinking
**Inspecting theorem x usage**

I should check if theorem x's item forward uses i_S^! on degree 0 objects, which seems to fail because of exceptional pullback shifts. To avoid making assumptions about D-module formalism, I might refer to theorem 2690, which uses similar notation, and the xii remark concerning the need for purity. It looks like xii to x employs purity specifically to manage the i^! degrees. This connection could be crucial for my analysis!
thinking
**Verifying findings**

I'm thinking about how to present my findings effectively, particularly if I should mention whether there are really ten unconditional results. It seems I might be better off placing any summary after the main findings. I need to double-check that I have eight genuine violations, examining specific instances carefully for verification. I’ll ensure I correlate each finding with evidence from the text, particularly regarding any claims of overcounting or conjectures addressed in previous lines.
thinking
**Clarifying proof steps**

I'm considering how to articulate the claim that "the proof step does not follow." The idea is that diagonal abutment alone does not necessarily require that d_r=0. It’s important to point out that this can actually be achieved through non-zero differentials which eliminate off-diagonal terms. So, I’ll need to ensure that this distinction is clear when presenting my argument to maintain the integrity of my reasoning.
thinking
**Considering downstream propagation**

I’m thinking about how to add insights into my summary. I could incorporate findings related to concordance and holographic codes, especially since the user is interested in downstream propagation. It seems useful to add this low finding. I already have information on cross-propagation surfaces, and I could include something related to the year 1991 as well. It feels like a good addition!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5894,5902p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5894	vertex algebras (Proposition~\ref{prop:pbw-universality}). The
  5895	twelve characterizations of
  5896	Theorem~\ref{thm:koszul-equivalences-meta} read the same
  5897	genus-$0$ formality condition through distinct invariants: bar
  5898	concentration, Ext diagonal vanishing, factorization homology,
  5899	Kac--Shapovalov determinants, FM boundary acyclicity. Two
  5900	characterizations remain partially open: the Lagrangian criterion
  5901	awaits perfectness verification in general, and D-module purity
  5902	awaits the converse direction. The $\Eone$-chiral Koszul duality

thinking
**Analyzing theorems and conjectures**

Okay, the findings show more than just two partially open theorems: xi and xii. I might mention propagation drift, but it's not crucial. I need to check if theorem xi's condition only awaits perfectness verification generally. There's a potential concern with Theorem 2790 being conjectural. It seems like corollary 3015 could prove it under certain hypotheses, but that might not hold since the theorem is conjectured. I also need to ensure I follow file modification guidelines and update the plan accordingly.
codex
The local theorem is not just underproved; several of its advertised equivalence lanes are internally contradicted by nearby remarks or by the exact supporting surfaces it cites. I’m doing a final consistency pass now so the report only keeps findings that survive against the source and distinguishes theorem-local failures from slogan-level propagation.
Plan update
  ✓ Read the audit skill and the live theorem surfaces: theorem statement/proof, concordance entry, registry/metadata references
  ✓ Enumerate the 10+1+1 equivalences from source and classify each as unconditional, conditional, or one-directional
  ✓ Trace every proof step to cited lemmas/propositions/literature and test for missing hypotheses, scope inflation, object conflation, and boundary failures
  → Re-verify each candidate finding against actual file contents and produce a severity-ordered audit report with counts and verdict

thinking
**Searching for theorem confirmations**

I need to double-check a couple of findings related to theorem H and the growth theorem. I think I’ve already done that. I want to re-verify the proof phrase for item vii, and I’ve done that too. I could look for any other theorems in the entire repository that mention generic polynomial algebra. Using a simple search across the repo might not be enough, but I’ll definitely check for "ChirHoch^* polynomial algebra" to ensure rigor.
exec
/bin/zsh -lc 'rg -n -F "ChirHoch''^*('"\\cA) is a polynomial algebra\" chapters metadata || true
rg -n -F \"is a polynomial algebra with generators concentrated in degrees\" chapters metadata || true
rg -n -F \"polynomial Hilbert series\" chapters/theory/chiral_hochschild_koszul.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Searching for the theorem**

I’m thinking about whether there's a theorem that establishes if a derived intersection equals a twisted tensor product. It seems like an interesting area of exploration! I should search through relevant mathematical literature and resources to find information related to this. It’s crucial to understand this concept, so I really want to make sure I’m getting accurate results. Let’s see what I can find.
exec
/bin/zsh -lc 'rg -n -F "derived intersection computes the twisted tensor product" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/*' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n "derived intersection|twisted tensor product" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/chiral_koszul_pairs.tex | head -n 80' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:2822:space have derived intersection of expected dimension~$0$. This
chapters/theory/bar_cobar_adjunction_inversion.tex:2823:derived intersection is the twisted tensor product
chapters/theory/bar_cobar_adjunction_inversion.tex:2828:In the PTVV framework~\cite{PTVV13}, the derived intersection
chapters/theory/bar_cobar_adjunction_inversion.tex:2830:\mathcal{M}_{\cA^!}$ computes the twisted tensor product
chapters/theory/bar_cobar_adjunction_inversion.tex:2850:globally Lagrangian are equivalent when the derived intersection is
chapters/theory/bar_cobar_adjunction_inversion.tex:3072: On the Koszul locus, the twisted tensor product
chapters/theory/bar_cobar_adjunction_inversion.tex:3082: intersection~\cite{PTVV13}. The derived intersection
chapters/theory/bar_cobar_adjunction_inversion.tex:3087: deformation problems is the twisted tensor product).
chapters/theory/chiral_koszul_pairs.tex:65:$k \geq 3$, acyclicity of the twisted tensor product
chapters/theory/chiral_koszul_pairs.tex:99:the twisted tensor product $K_\tau^L(\cA, \cC)$, the defining
chapters/theory/chiral_koszul_pairs.tex:165:\item The twisted tensor product
chapters/theory/chiral_koszul_pairs.tex:174:These two properties (acyclicity of twisted tensor products and
chapters/theory/chiral_koszul_pairs.tex:212:Associated to $\tau$ are the \emph{twisted tensor products}
chapters/theory/chiral_koszul_pairs.tex:222:\index{twisted tensor product!differential formula}
chapters/theory/chiral_koszul_pairs.tex:281:\begin{lemma}[Left twisted tensor product as mapping cone; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:283:\index{twisted tensor product!mapping cone}
chapters/theory/chiral_koszul_pairs.tex:308:\begin{lemma}[Right twisted tensor product as mapping cone; \ClaimStatusProvedHere]
chapters/theory/chiral_koszul_pairs.tex:310:\index{twisted tensor product!mapping cone}
chapters/theory/chiral_koszul_pairs.tex:338:\item both twisted tensor products $K_\tau^L$ and $K_\tau^R$ are
chapters/theory/chiral_koszul_pairs.tex:351:associated graded twisted tensor products. Strong convergence
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '3068,3090p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3068	\smallskip\noindent
  3069	\emph{(3) Equivalence.}
  3070	\begin{itemize}
  3071	\item \emph{Forward} (Koszul $\Rightarrow$ Lagrangian).
  3072	 On the Koszul locus, the twisted tensor product
  3073	 $K_\tau(\cA, \cA^!)$ is acyclic. The complementarity
  3074	 splitting (Theorem~C) gives a direct-sum decomposition
  3075	 $T_{\mathrm{comp}} \simeq T_\cA \oplus T_{\cA^!}$:
  3076	 the one-sided tangent complexes are complementary subspaces.
  3077	 By~(2) they are isotropic; by complementarity they are
  3078	 half-dimensional. Isotropic + half-dimensional = Lagrangian.
  3079	\item \emph{Converse} (Lagrangian $\Rightarrow$ Koszul).
  3080	 Transverse Lagrangians in a $(-1)$-shifted symplectic
  3081	 formal moduli problem have discrete derived
  3082	 intersection~\cite{PTVV13}. The derived intersection
  3083	 $\cM_\cA \times^h_{\cM_{\mathrm{comp}}} \cM_{\cA^!}$
  3084	 computes $K_\tau(\cA, \cA^!)$
  3085	 (this is the formal content of the ambient complementarity
  3086	 construction: the derived fiber product of the two one-sided
  3087	 deformation problems is the twisted tensor product).

thinking
**Updating mathematical plan**

I’m noticing a potential issue with the universal-Koszul, specifically with V_k at all levels. There’s a remark I need to retract, so I want to mention the propagation to the corollary. That's good to keep in mind. I think I might need to update my overall plan after I compose everything. Before I finalize anything, I definitely want to ensure that my plan is complete and thoroughly checked.
Plan update
  ✓ Read the audit skill and the live theorem surfaces: theorem statement/proof, concordance entry, registry/metadata references
  ✓ Enumerate the 10+1+1 equivalences from source and classify each as unconditional, conditional, or one-directional
  ✓ Trace every proof step to cited lemmas/propositions/literature and test for missing hypotheses, scope inflation, object conflation, and boundary failures
  ✓ Re-verify each candidate finding against actual file contents and produce a severity-ordered audit report with counts and verdict

thinking
**Crafting with care**

I want to make sure that my responses are concise yet detailed enough to be helpful. It’s a balancing act! I think providing the right amount of information is key. Too little might leave the user confused, while too much could overwhelm them. I’ll focus on clarity and brevity, ensuring that every word counts. It's all about delivering value in a way that's easily digestible for the user! Let’s keep refining this approach.
codex
Source intent: the theorem counts `(i)`–`(x)` as the `10` unconditional items; `(xi)` is the conditional `+1` (Lagrangian criterion); `(xii)` is the one-directional `+1` (`\mathcal D`-module purity). That count does not survive the source audit.

- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:1998-2004, 2108-2150 — Item `(vii)` is advertised inside the “unconditional equivalences,” but the proof explicitly scopes `(i) ⇔ (vii)` to the `g=0` specialization only, and the remark states the all-genera version is strictly stronger than Koszulness because Virasoro has nonzero `\delta F_g^{\mathrm{cross}}`. So `(vii)` is not one of the ten unconditional equivalences as written.
- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:2005-2008, 2065-2076; chapters/theory/chiral_hochschild_koszul.tex:576-605, 687-735 — Item `(viii)` is mis-stated. The cited Hochschild theorems prove duality, concentration in degrees `{0,1,2}`, and a polynomial Hilbert series; they do not prove that `\mathrm{ChirHoch}^*(\cA)` is a free polynomial algebra with generators in degrees `{0,1,2}`. The proof of `(viii) ⇒ (v)` uses that stronger unproved claim and also conflates cohomological degree with the second `Ext` grading.
- [CRITICAL] chapters/theory/bar_cobar_adjunction_inversion.tex:2789-2808, 3015-3041; chapters/theory/chiral_koszul_pairs.tex:2020-2022, 2262-2291 — The `+1` Lagrangian lane is status-inflated. The underlying “Lagrangian characterization” is explicitly a conjecture, yet the “unconditional” corollary for the standard landscape proves itself by “apply the Lagrangian criterion” while citing that conjecture. The meta-theorem’s proof reuses the same conjectural argument as if it were established.
- [CRITICAL] chapters/theory/chiral_koszul_pairs.tex:1339-1399, 1970-2008; chapters/connections/concordance.tex:7188-7194 — The file itself records a critical-level affine KM boundary regime where PBW/`E_2` degeneration survives but diagonal `Ext` concentration and Theorem `H` fail. That is incompatible with an unqualified global equivalence chain `(i)`–`(x)`, and it directly conflicts with the nearby claim that `V_k(\mathfrak g)` is chirally Koszul at all levels.
- [HIGH] chapters/theory/chiral_koszul_pairs.tex:1277-1311, 2245-2259 — The converse “diagonal `Ext` vanishing ⇒ `E_2`-collapse” is not proved. The argument says diagonal abutment forces all higher differentials to vanish, but off-diagonal terms can be killed by higher differentials and still leave diagonal `E_\infty`. Both the standalone theorem and the meta-proof use this invalid spectral-sequence step.
- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:2518-2556, 2559-2605; chapters/theory/chiral_koszul_pairs.tex:2177-2203 — The Barr–Beck lane is not independently established. The inversion file first says the precise BBL locus is conjectural, then states a `ProvedHere` theorem under the standing hypotheses of bar-cobar inversion; as written those imported hypotheses come from a theorem whose first hypothesis is that `\cA` is Koszul. The meta-proof likewise reasons only “on the Koszul locus,” so `(vi)` is not proved as an independent characterization.
- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:2689-2725; chapters/theory/chiral_koszul_pairs.tex:2157-2174 — The FM-boundary equivalence is only asserted, not proved. The forward direction treats `i_S^!` as if it preserved degree-zero concentration (“restrictions of degree-0 objects remain in degree 0”), which is exactly the subtlety later outsourced to purity; the converse jumps from acyclicity on every stratum to injectivity of the PBW comparison map with no supporting argument.
- [MEDIUM] chapters/theory/chiral_koszul_pairs.tex:2036-2040; chapters/theory/chiral_koszul_pairs.tex:696-720, 873-993 — The proof cites `thm:pbw-koszulness-criterion` as if it directly identified chirally Koszul with `E_2`-collapse. It does not: the theorem is a one-way PBW sufficient criterion, while the actual `E_2`-collapse statement appears later in `cor:bar-cohomology-koszul-dual`. A load-bearing citation is therefore wrong.
- [LOW] chapters/connections/concordance.tex:1990-1992; chapters/connections/outlook.tex:233-234; chapters/connections/holographic_codes_koszul.tex:41-43 — The broken slogan “10 unconditional, 1 conditional, 1 one-directional” is propagated unchanged into programme-level summary files, so the local theorem defects already contaminate downstream overview surfaces.

## Summary
Instances checked: 23 | Violations found: 9 | Verdict: FAIL
tokens used
159,914
