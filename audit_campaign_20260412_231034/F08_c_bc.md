# F08_c_bc (441s, gpt-5.4)

- [CRITICAL] [chapters/examples/toroidal_elliptic.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:2085) — The K3 CDR remark reverses the local free-field signs: it states `c_{\beta\gamma}=-2` and `c_{bc}=+2` per complex dimension. The canonical source [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:76) gives `c_{bc}(\lambda)=1-3(2\lambda-1)^2`; at `\lambda=1` this is `-2`, while `c_{\beta\gamma}=+2`.

- [CRITICAL] [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177) — Vol III duplicates the same K3 CDR sign reversal: `c_{\beta\gamma}=-2`, `c_{bc}=+2`. This disagrees with the canonical `\lambda=1` boundary values `c_{bc}=-2`, `c_{\beta\gamma}=+2`.

- [MEDIUM] [chapters/examples/beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:315) — The theorem surface uses only the non-canonical rewrite `c_{bc}=-2(6\lambda^2-6\lambda+1)`; the same drift recurs at line 635. Expansion shows it is equivalent to the canonical `1-3(2\lambda-1)^2`, so this is notation drift, not a false value. The same file’s line 321 uses the canonical form, so the file is internally inconsistent.

- [MEDIUM] [chapters/connections/thqg_gravitational_s_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_s_duality.tex:1148) — Vol I states the `bc_\lambda` central charge only as `-2(6\lambda^2-6\lambda+1)`; the duplicate in Vol II at [thqg_gravitational_s_duality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1071) does the same. Boundary checks `\lambda=2,-26`, `\lambda=1,-2`, `\lambda=\tfrac12,1` confirm correctness, but both surfaces drift from the canonical form.

- [MEDIUM] [chapters/examples/rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3191) — The explicit `bc` central-charge discussion uses only the non-canonical quadratic form; the same drift recurs at lines 923 and 3245. Values are correct after expansion and boundary checks, but the formula surface does not match the canonical source.

- [MEDIUM] [chapters/examples/w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:928) — The spin-`s` ghost formula is written in non-canonical form `-2(6s^2-6s+1)` here and in sibling files [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:957), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:281), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:793), and [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:355). This is equivalent to `1-3(2s-1)^2`; checks at `s=2,3,4` give `-26,-74,-146`, so the values are right but the notation is non-canonical throughout the Vol II cluster.

- [LOW] [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:794) — The file gives the canonical formula at line 793, then immediately appends the non-canonical rewrite `=-2(6\lambda^2-6\lambda+1)`. This is correct but still drifts from the canonical presentation.

- [LOW] [chapters/examples/genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2380) — The line leads with the non-canonical quadratic form before giving the canonical form. The value is correct, but the ordering still departs from the canonical source.

All other checked `c_{bc}`/ghost-value surfaces matched the canonical formula after direct expansion and boundary evaluation.

## Summary
Instances checked: 57 | Violations found: 8 | Verdict: FAIL


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
session id: 019d8393-7e27-76a1-ac32-daa5af85ae2b
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


MISSION: Verify every instance of bc central charge across all .tex files.

CANONICAL: c_bc(lambda) = 1 - 3(2*lambda-1)^2
CHECKS: lambda=2→-26. WRONG: 2(6L^2-6L+1)

STEPS:
1. Run: grep -rn 'c_bc\|c_{bc}\|1.*3.*2.*lambda' chapters/ | head -30
2. Also search in Vol II: grep -rn similar patterns ~/chiral-bar-cobar-vol2/chapters/ | head -30
3. Also search in Vol III: grep -rn similar patterns ~/calabi-yau-quantum-groups/chapters/ | head -30
4. For EACH hit, verify the formula matches the canonical form
5. Check boundary values
6. Flag ANY discrepancy, even minor notation differences
7. Also check landscape_census.tex for the canonical source
mcp startup: no servers
codex
I’m treating this as a cross-volume falsification audit on every `bc` central charge occurrence in `.tex` sources. First I’m loading the relevant verification workflow and the canonical source surface, then I’ll enumerate every hit in Volumes I–III and check each against the stated formula and boundary values.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

exec
/bin/zsh -lc "rg -n --glob '*.tex' 'c_bc|c_\\{bc\\}|1\\s*-\\s*3\\s*\\(2\\s*\\\\lambda\\s*-\\s*1\\)\\"'^2|1'"\\s*-\\s*3\\s*\\(2\\s*L\\s*-\\s*1\\)\\"'^2|2'"\\s*\\(6\\s*L\\"'^2'"\\s*-\\s*6\\s*L\\s*\\+\\s*1\\)|2\\s*\\(6\\s*\\\\lambda\\"'^2'"\\s*-\\s*6\\s*\\\\lambda\\s*\\+\\s*1\\)' chapters landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 exited 2 in 50ms:
rg: landscape_census.tex: No such file or directory (os error 2)
chapters/examples/beta_gamma.tex:312:c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:321:Fermionic $bc$ system ($c_{bc} = 1 - 3(2\lambda-1)^2$):
chapters/examples/beta_gamma.tex:326:Bosonic $\beta\gamma$ system ($c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1)$):
chapters/examples/beta_gamma.tex:633:c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
chapters/examples/beta_gamma.tex:637:c_{\beta\gamma} + c_{bc} = 0.
chapters/examples/beta_gamma.tex:642:The central charge of the $\beta\gamma$ system is computed from the stress tensor (Theorem~\ref{thm:beta-gamma-stress}). Replacing bosonic statistics by fermionic statistics negates the Virasoro central term: the commutator $[L_m, L_n]$ picks up a sign from the fermion loop, so $c_{bc} = -c_{\beta\gamma}$.
chapters/examples/beta_gamma.tex:1111:where $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$ is the
chapters/examples/beta_gamma.tex:1190:$c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$, and the genus-$1$
chapters/examples/beta_gamma.tex:1217:$\kappa(bc) = c_{bc}/2 = -(6\lambda^2 - 6\lambda + 1)$ is the
chapters/examples/beta_gamma.tex:1235:$c_{bc} = -c_{\beta\gamma}$
chapters/examples/beta_gamma.tex:1769: 2(6\lambda^2 - 6\lambda + 1).
chapters/examples/beta_gamma.tex:1777:exponents cancel because $c_{\beta\gamma} + c_{bc} = 0$.
chapters/examples/beta_gamma.tex:1791:Hence $e(\lambda) + e(1-\lambda) = 2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:1793:$\lambda$ is $c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$
chapters/examples/beta_gamma.tex:1808:charge is $c_{bc}(\lambda) = -c_{\beta\gamma}(\lambda)$
chapters/examples/beta_gamma.tex:2339:$c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/free_fields.tex:708:Central charge $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$.


thinking
**Verifying formulas and discrepancies**

I'm tasked with verifying formulas against a canonical source. If the formula is mathematically equivalent but not in the exact canonical notation, I wonder if I should flag that. The user's emphasizing any minor discrepancies, so I think any non-canonical version should be flagged regardless of severity. I need to categorize these instances and ensure I'm identifying all relevant errors, checking for boundary values, and potentially expanding my search beyond just initial patterns mentioned by the user. It's really crucial to be thorough!
thinking
**Searching formulas in .tex files**

I think I need to use `rg` to search through all the .tex files for terms like `c_{bc}`, `c_bc`, and `bc`. It's possible that using regex could help me find `c = -2...` within `bc` paragraphs. I'll want to search for `bc` in contexts like `central charge` or similar formulas. I should employ diverse search strategies and directly reference the canonical source from landscape_census.tex. Plus, I might need to check algebraic identities and boundary values, so keeping line references in mind is essential!
codex
The first pass already shows mixed representations in Volume I, including both the canonical `1-3(2\\lambda-1)^2` form and the equivalent but non-canonical `-2(6\\lambda^2-6\\lambda+1)` form. I’m now loading the audit prerequisites from the repo constitution and doing a complete cross-volume sweep, not just the initial `head -30` sample.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

thinking
**Searching for file paths**

I need to locate the landscape_census file path using `rg` files. The user has asked for grep commands to display the first 30 lines from each volume. I should ensure we cover all instances of the bc central charge across all .tex files, including Volumes II and III. I’ll use `rg` to search comprehensively for these patterns, starting with the initial head-30 for compliance, but running their grep commands might be a good plan too. I’ll get started on locating that file!
codex
I’ve loaded the repo’s audit prerequisites and the risk map. Next I’m locating the canonical `landscape_census.tex`, running the user-specified cross-volume greps, and then a broader sweep to catch nonstandard phrasings like `c = -2(6\\lambda^2-6\\lambda+1)` that the initial pattern might miss.
exec
/bin/zsh -lc "grep -rn 'c_bc\\|c_{bc}\\|1.*3.*2.*lambda' /Users/raeez/calabi-yau-quantum-groups/chapters/ | head -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn 'c_bc\\|c_{bc}\\|1.*3.*2.*lambda' /Users/raeez/chiral-bar-cobar-vol2/chapters/ | head -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn 'c_bc\\|c_{bc}\\|1.*3.*2.*lambda' chapters/ | head -30" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:226:The shuffle algebra presentation of $Y^+(\widehat{\fgl}_1)$ has structure function $g(z) = (z - h_1)(z - h_2)(z - h_3)/((z + h_1)(z + h_2)(z + h_3))$. A natural attempt extracts a $\lambda$-bracket from the shuffle product via $z \mapsto \lambda$. This fails: $g(0) = -1$ (regular, not singular), so the shuffle product does not produce a distribution-valued bracket. The envelope step (Step~2 $\to$ Step~3) replaces the algebraic $g(z)$ by the \emph{vertex operator} OPE, where the $\delta$-function singularity of the state-field correspondence generates the $\lambda$-bracket. The passage shuffle $\to$ vertex algebra is the step where locality enters.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:196:Vol~III writes classical shadow operations in lambda-bracket notation with divided powers: $\{T_\lambda T\} = (c/12)\,\lambda^3$. The divided-power prefactor $1/3! = 1/6$ absorbs the OPE mode coefficient into the lambda-bracket rewrite: starting from the OPE mode $T_{(3)}T$ and dividing by $3!$ yields the stated $c/12$ at order $\lambda^3$. Every formula imported from Vol~I (which uses OPE mode notation) must be converted before appearing in Vol~III. The CY-to-chiral functor $\Phi$ is agnostic to the choice of convention, but its computed values of $\kappa_{\mathrm{ch}}$ are convention-dependent at the level of integral prefactors, and a Vol~I formula transplanted without conversion will produce a wrong $\kappa_{\mathrm{ch}}$ by exactly a factor of $6$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177:contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
exec
/bin/zsh -lc "find . -name 'landscape_census.tex' -o -path './*landscape_census.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 157ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:412:&\quad + m_2(m_2(a,b),c;\,\Lambda_{\{1,2\}},\lambda_3) + (-1)^{|a|} m_2(a,m_2(b,c);\,\lambda_1,\Lambda_{\{2,3\}}).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:420:Points 2,3 collide. Inner operation: $m_2(b,c;\lambda_2)$; outer: $m_2(a,\bullet;\lambda_1)$ with the merged slot carrying effective parameter $\Lambda_{\{2,3\}} = \lambda_2$ (since point 3 is the rightmost reference, the inner parameter $\lambda_2 = z_2 - z_3$ is the only inner spectral variable). The Koszul sign is $(-1)^{\epsilon(1,2)} = (-1)^{|a|}$ (inner $m_2$ passes $a$). Contribution: $(-1)^{|a|}\,m_2(a,m_2(b,c))$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-calculus.tex:961:More precisely, the meromorphic expression $\frac{1}{(z_1-z_2)(z_2-z_3)(z_3-z_1)}$ is the \emph{kernel} of $m_3$ as a function of the external spectral parameters $\lambda_1 = z_1 - z_2$, $\lambda_2 = z_2 - z_3$; it is not a definite integral but rather the integral kernel that must be integrated against the inputs over an appropriate cycle. After fixing coordinates $\lambda_1, \lambda_2$ on the reduced configuration space, writing $\lambda_j = r_j e^{i\theta_j}$ and using the dilation quotient to fix $r_1 = 1$, the integrand involves the logarithmic $2$-form $d\log\lambda_1 \wedge d\log\lambda_2 = (d\log r_1 + i\,d\theta_1)\wedge(d\log r_2 + i\,d\theta_2)$. On the $3$-dimensional quotient (parametrized by $\theta_1, r_2, \theta_2$), the relevant top-degree form is $d\theta_1 \wedge d\log r_2 \wedge d\theta_2$, which arises as the imaginary part of $d\log\lambda_1 \wedge d\log\lambda_2$ wedged with $d\log r_2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:79:\Res_{D_{\{1,2\}}}(\omega_3) \;\longleftrightarrow\; m_2\bigl(m_2(a, b;\, \lambda),\, c;\, \mu\bigr).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:109:After setting $\varepsilon_{23} = 0$, the outer spectral parameter becomes $\lambda = z_1 - z_3 = w_1$. This is the same as $\lambda_1 + \lambda_2$ in the original notation (where $\lambda_1 = z_1 - z_2$ and $\lambda_2 = z_2 - z_3 = \mu$), consistent with the spectral substitution rule: the inner block $\{2,3\}$ is replaced by the sum $\Lambda_{\{2,3\}} = \lambda_2 \to \mu$, and the outer parameter for slot 1 relative to the collapsed slot is $\lambda_1 + \mu$. The composed operation is
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:220:\Res_{D_{\{1,2\}}}(\omega_4) \;\longleftrightarrow\; m_3\bigl(m_2(a_1, a_2;\, \lambda_1),\, a_3,\, a_4;\, \Lambda_{\{1,2\}}, \lambda_2, \lambda_3\bigr),
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:228:\Res_{D_{\{2,3\}}}(\omega_4) \;\longleftrightarrow\; (-1)^{|a_1|}\, m_3\bigl(a_1,\, m_2(a_2, a_3;\, \lambda_2),\, a_4;\, \lambda_1 + \Lambda_{\{2,3\}}, \lambda_3\bigr),
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:236:\Res_{D_{\{3,4\}}}(\omega_4) \;\longleftrightarrow\; (-1)^{|a_1|+|a_2|}\, m_3\bigl(a_1,\, a_2,\, m_2(a_3, a_4;\, \lambda_3);\, \lambda_1, \lambda_2 + \Lambda_{\{3,4\}}\bigr),
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:250:\Res_{D_{\{1,2,3\}}}(\omega_4) \;\longleftrightarrow\; m_2\bigl(m_3(a_1, a_2, a_3;\, \lambda_1, \lambda_2),\, a_4;\, \Lambda_{\{1,2,3\}}, \lambda_3\bigr),
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/fm-proofs.tex:262:\Res_{D_{\{2,3,4\}}}(\omega_4) \;\longleftrightarrow\; (-1)^{|a_1|}\, m_2\bigl(a_1,\, m_3(a_2, a_3, a_4;\, \lambda_2, \lambda_3);\, \lambda_1 + \Lambda_{\{2,3,4\}}\bigr),
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:639:$m_2(T,T;\lambda) = (c/12)\lambda^3 + 2T\lambda + \partial T$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface_trimmed.tex:472:= (c/12)\lambda^3 + 2T\lambda + \partial T$, and $m_3$, $m_4$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:2778:At the Virasoro self-duality point $c = 13$ (where $\mathrm{Vir}_c^! \cong \mathrm{Vir}_{26-c} = \mathrm{Vir}_{13}$), the modular characteristic is $\kappa = 13/2$ and the shadow free energies are $F_g = (13/2)\lambda_g^{\mathrm{FP}}$. This is NOT the special central charge $c = 26$ where the bosonic string becomes critical; $c = 13$ is distinguished by the property that the Koszul dual is isomorphic to the original algebra. The free energies at $c = 13$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:3627:At genus $6$: $|B_{12}| = 691/2730$, $12! = 479001600$, $(2^{11}-1)/2^{11} = 2047/2048$. $\lambda_6^{\mathrm{FP}} = \frac{2047}{2048} \cdot \frac{691}{2730 \cdot 479001600}$. Computing: $2730 \cdot 479001600 = 1307614368000$. $\frac{691}{1307614368000} = \frac{691}{1307614368000}$. $\frac{2047 \cdot 691}{2048 \cdot 1307614368000} = \frac{1414477}{2678117105664000}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:275:$-c\,\lambda_{12}\lambda_{23}(\lambda_{12}+\lambda_{23})$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:277:becomes $-(26-c)\,\lambda_{12}\lambda_{23}(\lambda_{12}+\lambda_{23})$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1311:= -c\,\lambda_{12}\lambda_{23}(\lambda_{12}+\lambda_{23})$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1321:-c\,\lambda_{12}\lambda_{23}(\lambda_{12}+\lambda_{23}),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1406:= -c\,\lambda_{12}\lambda_{23}(\lambda_{12}+\lambda_{23})$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:1204:$\frac{13}{2}\lambda_g^{\mathrm{FP}}$ \\
 succeeded in 325ms:
chapters/theory/ordered_associative_chiral_kd.tex:3083:\tfrac{c}{12}\,\lambda_{23}^3\,(2\lambda_{12} + \lambda_{23})
chapters/theory/ordered_associative_chiral_kd.tex:3086:The scalar contact term $\frac{c}{12}\lambda_{23}^3(2\lambda_{12}
chapters/theory/ordered_associative_chiral_kd.tex:3151:$F_g(\mathrm{Vir}_{13}) = \frac{13}{2}\lambda_g^{\mathrm{FP}}
chapters/theory/ordered_associative_chiral_kd.tex:6572:and $K(bc_\lambda) = c_{bc}(\lambda)+c_{\beta\gamma}(\lambda) = 0$.
chapters/theory/chiral_center_theorem.tex:2505:c_{bc} = 0$ per complex dimension), and the Witten genus of~$X$
chapters/theory/chiral_modules.tex:4900:$\lambda + 1 - 1 + \tfrac{3}{2} = \lambda + \tfrac{3}{2}$.
chapters/theory/higher_genus_foundations.tex:4173:$bc_\lambda$ & $c_{bc}/2$ & --- & --- & $c_{bc}/48$ \\
chapters/theory/higher_genus.aux:552:\@writefile{loe}{\contentsline {theorem}{\ifthmt@listswap Theorem~13.12.4\else \numberline {13.12.4}Theorem\fi \thmtformatoptarg {Faber--Pandharipande $\lambda _g$ formula {\cite  {FP03}}; }}{755}{theorem.13.12.4}\protected@file@percent }
chapters/theory/higher_genus.aux:553:\newlabel{thm:mumford-formula}{{13.12.4}{755}{Faber--Pandharipande $\lambda _g$ formula {\cite {FP03}}; \ClaimStatusProvedElsewhere }{theorem.13.12.4}{}}
chapters/theory/higher_genus.aux:555:\newlabel{eq:faber-pandharipande}{{13.12.4}{755}{Faber--Pandharipande $\lambda _g$ formula {\cite {FP03}}; \ClaimStatusProvedElsewhere }{theorem.13.12.4}{}}
chapters/theory/higher_genus_modular_koszul.tex:3019:$bc$, $\kappa(bc) = c_{bc}/2 = -(6\lambda^2 - 6\lambda + 1)$.
chapters/theory/higher_genus_modular_koszul.tex:20417:$c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) = 0$ gives
chapters/frame/preface.tex:2952:$c_{bc}(\lambda) = 1 - 3(2\lambda{-}1)^2$ and
chapters/frame/preface.tex:2954:satisfying $c_{\beta\gamma} + c_{bc} = 0$ (verified at
chapters/frame/preface.tex:2955:$\lambda = 2$: $c_{\beta\gamma} = 26$, $c_{bc} = -26$; string
chapters/connections/thqg_perturbative_finiteness.tex:2217:At the Virasoro self-duality point $c = 13$ (where $\mathrm{Vir}_c^! \cong \mathrm{Vir}_{26-c} = \mathrm{Vir}_{13}$), the modular characteristic is $\kappa = 13/2$ and the shadow free energies are $F_g = (13/2)\lambda_g^{\mathrm{FP}}$. This is NOT the special central charge $c = 26$ where the bosonic string becomes critical; $c = 13$ is distinguished by the property that the Koszul dual is isomorphic to the original algebra. The free energies at $c = 13$:
chapters/connections/thqg_perturbative_finiteness.tex:2318:At genus $6$: $|B_{12}| = 691/2730$, $12! = 479001600$, $(2^{11}-1)/2^{11} = 2047/2048$. $\lambda_6^{\mathrm{FP}} = \frac{2047}{2048} \cdot \frac{691}{2730 \cdot 479001600}$. Computing: $2730 \cdot 479001600 = 1307614368000$. $\frac{691}{1307614368000} = \frac{691}{1307614368000}$. $\frac{2047 \cdot 691}{2048 \cdot 1307614368000} = \frac{1414477}{2678117105664000}$.
chapters/connections/thqg_critical_string_dichotomy.tex:1174:$\frac{13}{2}\lambda_g^{\mathrm{FP}}$ \\
chapters/connections/thqg_critical_string_dichotomy.tex:1296:= \frac{13}{2} \cdot \lambda_g^{\mathrm{FP}},
chapters/connections/bv_brst.tex:359:The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.
 succeeded in 1.28s:
./chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a074cd40/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-adfdf072/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-aaa0b7c9/.claude/worktrees/agent-a0064e24/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ab4d244b/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-a7a899b6/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ad4860d3/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-abc99e5a/chapters/examples/landscape_census.tex
./.claude/worktrees/agent-ab0fb328/chapters/examples/landscape_census.tex
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
./.claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/chapters/examples/landscape_census.tex

thinking
**Refining search strategies**

I’m reflecting on the grep head results; they're not great since they matched a lot of irrelevant lambda lines in Volumes II and III. I probably need a broader, more focused search strategy. Additionally, I still need to locate the landscape_census from session 40270, which is still running. I think it’s time to do a quick poll to gather more insights. Let’s keep moving towards those next steps!
codex
The initial `grep | head -30` results are noisy in Volumes II–III because the regex also catches unrelated `lambda`-bracket formulas. I’m narrowing the surface to actual `bc` central-charge mentions by scanning every `*.tex` for `c_{bc}`/`c_bc`, then separately hunting unlabeled `bc` formulas and boundary-value statements like `\\lambda=2 \\mapsto -26`.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'c_\\{bc\\}|c_bc' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'c_\\{bc\\}|c_bc|1 - 3\\(2\\\\lambda-?1\\)\\"'^2|1 - 3'"\\(2\\\\lambda - 1\\)\\"'^2|2'"\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'central charge["'^'"\\n]*bc|bc["'^'"\\n]*central charge|ghost["'^'"\\n]*-26|\\blambda\\s*=\\s*2["'^'"\\n]*c_\\{bc\\}|\\blambda\\s*=\\s*2["'^'"\\n]*-26|c\\s*=\\s*-2\\(6\\\\lambda\\"'^2'"\\s*-\\s*6\\\\lambda\\s*\\+\\s*1\\)' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177:contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:922:$K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda)
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:321:Fermionic $bc$ system ($c_{bc} = 1 - 3(2\lambda-1)^2$):
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
chapters/examples/beta_gamma.tex:637:c_{\beta\gamma} + c_{bc} = 0.
chapters/examples/beta_gamma.tex:642:The central charge of the $\beta\gamma$ system is computed from the stress tensor (Theorem~\ref{thm:beta-gamma-stress}). Replacing bosonic statistics by fermionic statistics negates the Virasoro central term: the commutator $[L_m, L_n]$ picks up a sign from the fermion loop, so $c_{bc} = -c_{\beta\gamma}$.
chapters/examples/beta_gamma.tex:1217:$\kappa(bc) = c_{bc}/2 = -(6\lambda^2 - 6\lambda + 1)$ is the
chapters/examples/beta_gamma.tex:1235:$c_{bc} = -c_{\beta\gamma}$
chapters/examples/beta_gamma.tex:1777:exponents cancel because $c_{\beta\gamma} + c_{bc} = 0$.
chapters/examples/beta_gamma.tex:1808:charge is $c_{bc}(\lambda) = -c_{\beta\gamma}(\lambda)$
chapters/examples/free_fields.tex:752:$\beta\gamma$: a T-line (Virasoro subalgebra at $c_{bc}$, with
chapters/examples/free_fields.tex:753:$S_3 = 2$ and $S_4 = 10/[c_{bc}(5c_{bc}+22)]$) and a
chapters/examples/free_fields.tex:765:Modular characteristic $\kappa(bc) = c_{bc}/2 = -(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/free_fields.tex:767:$c_{bc} = -26$, $\kappa(bc) = -13$.
chapters/examples/free_fields.tex:793: c_{bc}(\lambda) \;=\; 1 - 3(2\lambda - 1)^2
chapters/examples/free_fields.tex:797:$\kappa(bc_\lambda) = c_{bc}(\lambda)/2 = -(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/free_fields.tex:804: \qquad c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) \;=\; 0
chapters/examples/free_fields.tex:816:at $\lambda = 2$ (standard $bc$), $c_{bc} = 1 - 3 \cdot 9 = -26$ and
chapters/examples/free_fields.tex:818:at $\lambda = 1/2$ (self-dual weight), $c_{bc} = 1$ and
 exited 1 in 50ms:

 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/derived_categories_cy.tex:183:A \emph{Bridgeland stability condition} on a triangulated category $\cC$ is a pair $\sigma = (Z, \cP)$, where $Z \colon K_0(\cC) \to \C$ is a group homomorphism (the \emph{central charge}) and $\cP = \{\cP(\phi)\}_{\phi \in \bR}$ is a slicing of $\cC$ into full additive subcategories (the \emph{semistable objects of phase $\phi$}), subject to: (i) for $0 \neq E \in \cP(\phi)$, $Z(E) = m(E) \exp(i \pi \phi)$ with $m(E) > 0$; (ii) $\cP(\phi + 1) = \cP(\phi)[1]$; (iii) Harder--Narasimhan filtrations exist (Bridgeland 2007).
chapters/examples/w_algebras_deep.tex:2396:invariant that measures the bc ghost central charge, not the kappa
chapters/examples/beta_gamma.tex:322:$\lambda = 2$: $c = -26$ (string theory ghosts);
chapters/examples/beta_gamma.tex:642:The central charge of the $\beta\gamma$ system is computed from the stress tensor (Theorem~\ref{thm:beta-gamma-stress}). Replacing bosonic statistics by fermionic statistics negates the Virasoro central term: the commutator $[L_m, L_n]$ picks up a sign from the fermion loop, so $c_{bc} = -c_{\beta\gamma}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:625:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:538:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:938:c_{\mathrm{ghost}}^{\mathrm{Vir}} &= -26, &
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:530:because the ghost determinant contributes $c_{\text{gh}} = -26$,
chapters/examples/landscape_census.tex:3984: central charge (Theorem~\ref{thm:betagamma-bc-koszul}),
chapters/examples/kac_moody.tex:711:\item \emph{Central charge non-cancellation.} Unlike the $\beta\gamma$/$bc$ pair (Proposition~\ref{prop:betagamma-bc-koszul-detailed}), the central charges satisfy $c(k) + c(-k-4) = 2\dim(\mathfrak{sl}_2) = 6$ rather than zero: curvature prevents cancellation.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:263:c_{\mathrm{ghost}}^{\mathrm{Vir}} &= -26, &
chapters/examples/free_fields.tex:816:at $\lambda = 2$ (standard $bc$), $c_{bc} = 1 - 3 \cdot 9 = -26$ and
chapters/examples/free_fields.tex:2875:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
chapters/examples/free_fields.tex:4553:The $bc$ ghost system of central charge $c_{\mathrm{ghost}} = -26$
chapters/examples/free_fields.tex:4937:\emph{(1) Anomaly cancellation:} The integrand on $\overline{\mathcal{M}}_{g,n}$ involves $\det(\operatorname{Im} \Omega)^{-c/2}$; for the Belavin--Knizhnik anomaly to cancel, $c_{\mathrm{total}} = 0$. Hence $c_{\mathrm{matter}} = 26$ (bosonic, $c_{\mathrm{ghost}} = -26$) or $c_{\mathrm{matter}} = 15$ (super, $c_{\mathrm{ghost}} = -15$).
chapters/examples/free_fields.tex:5569:At the physical point $\lambda = 2$: $\kappa(bc) = -13$, $c_{bc} = -26$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2236:with $c_{\mathrm{ghost}} = -26$ and curvature
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:6548:\kappa(\mathrm{ghost}) = c/2 - 13 = (c-26)/2$ gives the effective
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:932:dual of the reparametrisation ghost $bc_2$ ($c = -26$) is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3192:At $\lambda = 2$: $c = -26$ (reparametrisation ghosts).

thinking
**Exploring command issues**

I'm noticing that the third command may not match due to formatting issues. It might be helpful to look into the landscape of the census entries around "bc." I think searching within the file for "bc" might yield better results, as it seems more generic and could help clarify any missed matches. I need to check how I can refine my approach with the commands to get accurate outcomes.
codex
I have enough candidate surfaces now. The main failure mode is already clear: multiple chapters state the mathematically equivalent `-2(6\\lambda^2-6\\lambda+1)` form instead of the canonical `1-3(2\\lambda-1)^2`, and I still need to determine whether any instance is actually wrong rather than merely non-canonical. I’m opening each candidate cluster in context, starting from the canonical census and then the cross-volume duplicate surfaces.
exec
/bin/zsh -lc "sed -n '300,340p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'bc|c_\\{bc\\}|ghost|beta\\\\gamma' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '788,820p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2376,2440p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\end{align}
The commutation relations are $[\beta_m, \gamma_n] = \delta_{m+n,0}$.
\end{proposition}

\begin{theorem}[Stress tensor and central charge \cite{FBZ04}; \ClaimStatusProvedElsewhere]
\label{thm:beta-gamma-stress}
The stress-energy tensor is:
\[
T^{\beta\gamma}(z) = (1-\lambda) \normord{\beta(z)\partial\gamma(z)} - \lambda \normord{\partial\beta(z)\gamma(z)}
\]
This generates the Virasoro algebra with central charge:
\[
c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
\]
For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
\end{theorem}

\begin{computation}[Central charges for special cases]
\label{comp:beta-gamma-central-charges}
 succeeded in 50ms:
9:$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$, three
76:$bc$ ghosts (weight $\lambda$)
77: & $\beta\gamma$ system (weight $\lambda$)
198:$\beta\gamma$, and lattice~$V_\Lambda$
235:\mathfrak{T}_{\beta\gamma}
236: &= \bigl(\beta\gamma_\lambda,\;
237: bc_\lambda,\;
290:$\beta\gamma$ system & C & 4 & $Q^{\mathrm{contact}}$; $\mu_{\beta\gamma}=0$ & \S\ref{chap:beta-gamma} \\
292:$bc$ ghosts & C & 4 & $Q^{\mathrm{contact}}$; stratum separation & \S\ref{chap:free-fields} \\
294:Symplectic boson ($\beta\gamma$ at $\lambda=1/2$, $c=-1$) & C & 4 & $Q^{\mathrm{contact}}$ in $\mathbb{Z}_2$-graded bar & \S\ref{sec:symplectic-boson-bar} \\
432:$\beta\gamma$ ($\beta\gamma$, $\gamma\beta$)
437:$bc$ ghosts ($bc$)
442:$\beta\gamma$ (diagonal)
603:$bc$ ghosts ($\lambda{=}0$) & $-1$ & $-\tfrac{1}{24}$ & $-\tfrac{7}{5760}$ & scalar \\
605:$\beta\gamma$ ($\lambda{=}1$) & $1$ & $\tfrac{1}{24}$ & $\tfrac{7}{5760}$ & multi \\
607:$\beta\gamma$ ($\lambda{=}\tfrac{1}{2}$) & $-\tfrac{1}{2}$ & $-\tfrac{1}{48}$ & $-\tfrac{7}{11520}$ & scalar \\
693:$bc$ ($\lambda$) & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
699:$\beta\gamma_\lambda$ & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
720:${}^\dagger$For $\beta\gamma$ and $bc$: $\Delta = 0$ and $\rho = 0$ on the primary
1127:$\beta\gamma$ ($\lambda=1$) & \checkmark & (ii) & PBW universality \\
 succeeded in 52ms:
$R_{bc_\lambda} = b \otimes c + c \otimes b$. For every $\lambda \in
\mathbb{C}$, the bar complex of $bc_\lambda$ has shadow depth exactly
$r_{\max} = 4$ (class~C, contact/quartic archetype), with Virasoro
subalgebra central charge
\[
 c_{bc}(\lambda) \;=\; 1 - 3(2\lambda - 1)^2
 \;=\; -2(6\lambda^2 - 6\lambda + 1),
\]
and modular characteristic
$\kappa(bc_\lambda) = c_{bc}(\lambda)/2 = -(6\lambda^2 - 6\lambda + 1)$.
The shadow coefficient depends only on $\lambda$, not on any level
parameter: the $bc$ system has no continuous level, only the discrete
weight datum $\lambda$. Koszul complementarity with $\beta\gamma_\lambda$
holds for every $\lambda$:
\[
 \kappa(\beta\gamma_\lambda) + \kappa(bc_\lambda) \;=\; 0,
 \qquad c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) \;=\; 0
 \;\; \]
\end{proposition}

 succeeded in 52ms:
\index{bc system@$bc$ system!genus expansion}

The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
is a fermionic chiral algebra with central charge
$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
(Computation~\ref{comp:beta-gamma-central-charges}).
Its Koszul dual is the bosonic $\beta\gamma$-system at the same
weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)
= -c_{bc}$, and the underlying operadic duality is
$\mathrm{Ext} \leftrightarrow \mathrm{Sym}$
(Theorem~\ref{thm:fermion-boson-koszul}).

\begin{theorem}[Free fermion free energy at all genera;
\ClaimStatusProvedHere]\label{thm:fermion-all-genera}
\index{free fermion!obstruction coefficient}
For the $bc$ system at conformal weights $(\lambda, 1-\lambda)$,
the genus-$g$ free energy is
\begin{equation}\label{eq:fermion-Fg}
F_g(bc_\lambda) = \kappa(bc_\lambda) \cdot
\frac{2^{2g-1}-1}{2^{2g-1}} \cdot

thinking
**Searching for canonical source lines**

I need to find the canonical source lines in landscape_census. I should search for relevant entries, particularly the bc entries and possibly some formulas. Lines around 1200 and 1280 seem crucial, so I need to check those specifically. It might also be helpful to use a search tool like "rg" for terms such as "central charge" to track down what I'm looking for. Time to dig in and gather those details!
exec
/bin/zsh -lc "sed -n '1268,1292p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3968,3990p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2748,2832p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item \emph{Complementarity.}
 Every $c + c'$ entry is independent of the level~$k$: it depends
 only on the root datum of~$\fg$.
 This is the content of Theorem~\ref{thm:central-charge-complementarity}.
\item \emph{Critical level.}
 Setting $\kappa(\cA) = 0$ (i.e., $t = k + h^\vee = 0$)
 simultaneously forces $\operatorname{obs}_g = 0$
 for all genera: the bar complex becomes \emph{uncurved}, and
 the Feigin--Frenkel center $\mathfrak{z}(\widehat{\fg}_{-h^\vee})$
 emerges as the degree-zero cohomology.
\item \emph{Free fields.}
 The exact Koszul dualities ($\psi \leftrightarrow \gamma$,
 $bc \leftrightarrow \beta\gamma$) satisfy
 $\kappa(\cA) + \kappa(\cA^!) = 0$
 (Theorem~\ref{thm:fermion-all-genera};
 not to be confused with bosonization,
 Remark~\ref{rem:bosonization-not-koszul}): the individual
 obstruction coefficients $\kappa(\psi) = \tfrac{1}{4}$,
 $\kappa(bc) = c/2$ are nonzero (they measure the
 Virasoro subalgebra curvature), but the tensor product
 succeeded in 51ms:
\begin{remark}[Locating the computations]\label{rem:cross-ref-guide}
Each row of the Master Table~\textup{\ref{tab:master-invariants}} is
computed in the following locations.
\begin{enumerate}
\item \emph{Free fermion}:
 bar complex (Theorem~\ref{thm:fermion-bar-coalg}),
 Koszul dual $\mathrm{Sym}^{\mathrm{ch}}(\gamma)$
 (Theorem~\ref{thm:betagamma-bc-koszul}),
 $\kappa = \tfrac{1}{4}$ (Table~\ref{tab:master-invariants}),
 three-theorem synthesis
 (Remark~\ref{rem:free-field-three-theorems}).
\item \emph{$bc$--$\beta\gamma$}:
 bar complex (Theorem~\ref{thm:betagamma-bar-complex}),
 Koszul duality
 (Proposition~\ref{prop:bc-betagamma-orthogonality},
 Theorem~\ref{thm:betagamma-bc-koszul}),
 central charge (Theorem~\ref{thm:betagamma-bc-koszul}),
 detailed computation (\S\ref{sec:betagamma-koszul-dual}).
\item \emph{Heisenberg}:
 bar complex (Theorem~\ref{thm:heisenberg-bar}),
 succeeded in 51ms:
 & rational
 & \checkmark
 & proved \\[6pt]
\hline
$\mathrm{Vir}_c$
 & $x \cdot M(x)^2$\textsuperscript{$\dagger$}
 & $\sim 3^n / n^{3/2}$
 & alg.\ deg $2$
 & \checkmark
 & proved \\[4pt]
\hline
$\beta\gamma$
 & $\sqrt{(1+x)/(1-3x)}$
 & $\sim 3^n / n^{1/2}$
 & alg.\ deg $2$
 & \checkmark
 & proved \\[4pt]
\hline
\multicolumn{6}{|c|}{\textit{Fermionic: $bc$ ghosts}} \\
\hline
exec
/bin/zsh -lc "rg -n '1 - 3\\(2\\\\lambda|6\\\\lambda\\"'^2 - 6'"\\\\lambda|c_\\{bc\\}|ghosts \\(weight \\\\lambda\\)|String ghosts' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '580,620p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '680,706p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
78: & $1 - 3(2\lambda{-}1)^2$ & $0$
 succeeded in 52ms:
odd-order poles from composite fields, and even-order $r$-matrix
poles are generically present.
\end{remark}

\begin{table}[ht]
\centering
\caption{Free energies $F_1 = \kappa/24$ and $F_2 = 7\kappa/5760$ for $21$ standard families}
\label{tab:free-energy-landscape}
\index{free energy!landscape table}
\renewcommand{\arraystretch}{1.5}
{\small
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Algebra $\cA$}
 & $\boldsymbol{\kappa}$
 & $\boldsymbol{F_1 = \kappa/24}$
 & $\boldsymbol{F_2 = 7\kappa/5760}$
 & \textbf{Lane} \\
\hline
\multicolumn{5}{|c|}{\textit{Free Fields}} \\
 succeeded in 51ms:
\hline
\textbf{Algebra $\cA$}
 & \textbf{Class}
 & $\boldsymbol{S_3}$
 & $\boldsymbol{S_4}$
 & $\boldsymbol{\Delta = 8\kappa S_4}$
 & $\boldsymbol{\rho}$
 & $\boldsymbol{\kappa{+}\kappa'}$ \\
\hline
$\mathcal{H}_k$ & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
Free fermion & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
$bc$ ($\lambda$) & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
\hline
$V_\Lambda$ (rank $d$) & G & $0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
$\widehat{\fg}_k$ & L & $\neq 0$ & $0$ & $0$ & $0$ & $0$ \\
\hline
$\beta\gamma_\lambda$ & C & $0$ & $\neq 0$ & $0^\dagger$ & $0^\dagger$ & $0$ \\
exec
/bin/zsh -lc "sed -n '70,84p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\multicolumn{6}{|c|}{\textit{Free Fields}} \\
\hline
Free fermion $\psi$
 & $\mathrm{Sym}^{\mathrm{ch}}(\gamma)$
 & $\tfrac{1}{2}$ & $0$ & $\tfrac{1}{4}$ & PH \\
\hline
$bc$ ghosts (weight $\lambda$)
 & $\beta\gamma$ system (weight $\lambda$)
 & $1 - 3(2\lambda{-}1)^2$ & $0$
 & $c/2$ & PH \\
\hline
\multicolumn{6}{|c|}{\textit{Heisenberg \textup{(}curved abelian\textup{)}}} \\
\hline
Heisenberg $\mathcal{H}_\kappa$
 & $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ (curved)


thinking
**Searching for occurrences**

I’m working on enumerating occurrences across different volumes. I could use the output from rg to pinpoint candidate files, as I need the contexts for each relevant occurrence. I’ll search through Vol II and III for duplicates, specifically looking for `c_{bc}`. In Vol II, the rosetta_stone has `c_bc`, while Vol III contains toroidal_elliptic. I need to check for other mentions of bc central charge using `c_ghost` as well. 

I’ll also look for `c_{\mathrm{ghost}}`, `bc_2`, and similar terms in Vol II. It might be useful to collect all unique files and lines that relate to bc central charge and be mindful of classification.
thinking
**Investigating findings**

I’m looking into various findings, starting with checking for formula mismatches. There might be differences in notation, like the canonical `c_bc(lambda)=1 - 3(2lambda-1)^2` versus the equivalent `-2(6lambda^2 - 6lambda +1)`, which isn’t canonical. The user wants me to flag even minor discrepancies, so I can classify these as LOW/MEDIUM.

Additionally, there’s a potential issue with an incorrect table in toroidal_elliptic showing `c_{bc} = +2`. I'll need context around whether bc weights relate to λ=0 or 1, particularly near lines 2085 in Vol 1 and 2177 in Vol 3. I should verify this further.
codex
I’ve found the canonical source in [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:76): it records the `bc` row as `1 - 3(2\\lambda{-}1)^2`, with `\\kappa = c/2`. I’m now checking every downstream occurrence against that source, and a few hits already look suspicious enough to require context rather than regex-only judgment.
exec
/bin/zsh -lc "sed -n '2076,2092p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1142,1164p' chapters/connections/thqg_gravitational_s_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1064,1080p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2170,2184p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\subsection{Chiral de~Rham complex on K3}
\label{subsec:cdr-k3}

\begin{remark}[CDR on K3]
\label{rem:cdr-k3}
\index{chiral de Rham complex!K3}
The chiral de~Rham complex $\Omega^{\mathrm{ch}}(K3)$ of
Malikov--Schechtman--Vaintrob is a sheaf of vertex
superalgebras on K3 with central charge $c = 0$ (the local
contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
complex dimension cancel globally). The CDR cohomology
recovers the K3 elliptic genus:
$\mathrm{ch}\bigl(H^*\bigl(K3, \Omega^{\mathrm{ch}}\bigr)\bigr)
= \mathrm{Ell}(K3; q, y) = 2\,\phi_{0,1}(\tau, z)$
(Borisov--Libgober).

On a hyperk\"ahler manifold (such as K3), the CDR carries
 succeeded in 51ms:
\qquad
K = 0.
\end{equation}
\end{proposition}

\begin{proof}
The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
The $bc$ system has a single generator pair $(b, c)$ of conformal weights
$(\lambda, 1 - \lambda)$; the double-pole coefficient is $1/(z-w)^1$
(first-order pole only for $\lambda \neq 1$), but the genus-$1$
curvature receives a contribution from the period matrix of the
fermion determinant, giving $\kappa = c/2 = -(6\lambda^2 - 6\lambda + 1)$.

The Koszul dual of $bc_\lambda$ is $\beta\gamma_\lambda$: the
$\mathrm{Ext}/\mathrm{Sym}$ duality (exterior $\leftrightarrow$
symmetric) negates the central charge, giving
$c(\beta\gamma_\lambda) = 2(6\lambda^2 - 6\lambda + 1)$ and
$\kappa(\beta\gamma_\lambda) = 6\lambda^2 - 6\lambda + 1$.
Therefore $K = 0$.

 succeeded in 51ms:

\begin{remark}[CDR on K3]
\label{rem:cdr-k3}
\index{chiral de Rham complex!K3}
The chiral de~Rham complex $\Omega^{\mathrm{ch}}(K3)$ of
Malikov--Schechtman--Vaintrob is a sheaf of vertex
superalgebras on K3 with central charge $c = 0$ (the local
contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
complex dimension cancel globally). The CDR cohomology
recovers the K3 elliptic genus:
$\mathrm{ch}\bigl(H^*\bigl(K3, \Omega^{\mathrm{ch}}\bigr)\bigr)
= \mathrm{Ell}(K3; q, y) = 2\,\phi_{0,1}(\tau, z)$
(Borisov--Libgober).

On a hyperk\"ahler manifold (such as K3), the CDR carries
 succeeded in 51ms:
\kappa(\beta\gamma_\lambda) = 6\lambda^2 - 6\lambda + 1,
\qquad
K = 0.
\end{equation}
\end{proposition}

\begin{proof}
The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
The $bc$ system has a single generator pair $(b, c)$ of conformal weights
$(\lambda, 1 - \lambda)$; the double-pole coefficient is $1/(z-w)^1$
(first-order pole only for $\lambda \neq 1$), but the genus-$1$
curvature receives a contribution from the period matrix of the
fermion determinant, giving $\kappa = c/2 = -(6\lambda^2 - 6\lambda + 1)$.

The Koszul dual of $bc_\lambda$ is $\beta\gamma_\lambda$: the
$\mathrm{Ext}/\mathrm{Sym}$ duality (exterior $\leftrightarrow$
symmetric) negates the central charge, giving

thinking
**Using shell commands**

I'm thinking that it might be best to use a shell command to gather all the candidate lines together into one cohesive list. This way, I'd be able to organize them efficiently. I want to make sure I’m using the most effective method here, and a shell command seems like a solid approach. Let’s see how I can implement that!
codex
A genuine formula error has now surfaced: the K3 chiral de Rham remarks in both Volumes I and III reverse the `bc` and `\\beta\\gamma` signs at weight `\\lambda=1`. I’m finishing the sweep so the final report distinguishes true mathematical errors from merely non-canonical rewrites.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'c_\\{bc\\}|c_bc' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'The central charge of \\"'$bc_'"\\\\lambda\\"'$ is|central charge '"\\"'$c_'"\\{bc\\} = 1 - 3\\(2\\\\lambda - 1\\)\\"'^2|c = -2'"\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|1 - 3\\(2\\\\lambda-1\\)\\"'^2|1 - 3'"\\(2\\\\lambda - 1\\)\\"'^2'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'c_\\{(text|mathrm)\\{ghost\\}\\}|c_\\{(text|mathrm)\\{gh\\}\\}|ghost["'^'"\\n]*c\\s*=\\s*-26|bc_[0-9]+["'^'"\\n]*c\\s*=\\s*-26|reparametrisation ghosts|ghost determinant contributes' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
      44
 succeeded in 50ms:
chapters/examples/beta_gamma.tex:321:Fermionic $bc$ system ($c_{bc} = 1 - 3(2\lambda-1)^2$):
chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
chapters/examples/free_fields.tex:793: c_{bc}(\lambda) \;=\; 1 - 3(2\lambda - 1)^2
chapters/connections/bv_brst.tex:359:The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.
chapters/connections/thqg_gravitational_s_duality.tex:1148:The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1071:The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:625:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:963:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:530:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:935:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:287:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:538:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:932:dual of the reparametrisation ghost $bc_2$ ($c = -26$) is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3192:At $\lambda = 2$: $c = -26$ (reparametrisation ghosts).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3264:ghost $bc_2$ ($c = -26$) is the bosonic spin-$2$ system
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:503:sector, but the ghost sector contributes $c = -26$, giving total
chapters/connections/thqg_introduction_supplement_body.tex:1547:The ghost system ($bc$ at $c = -26$) is the physical implementation



thinking
**Inspecting occurrences of c_bc**

I need to inspect all occurrences of `c_{bc}`, which are about 44 but may include some duplicates or cross-references rather than central charge formulas. It’s important to verify everything line by line. I could use regex output and generate a complete list with line numbers and a brief classification. The user doesn’t need every instance detailed, just the findings summarized. Counting occurrences, there seem to be about 54 candidate surfaces to verify, including mentions of central charge without `c_bc`.
thinking
**Inspecting additional files**

I need to inspect a range of files for specific occurrences. This includes `ordered_associative_chiral_kd.tex` at line 6572, `frame/preface.tex` at lines 2848, 2952-2955, 3209, and 3218, as well as `editorial_constitution.tex` at line 1893. I also have to check `higher_genus_foundations.tex`, `cobar_construction.tex`, `concordance.tex`, and several others for key instances. I’ll pay special attention to potential mentions of the bc ghost central charge to see if there are any errors.
thinking
**Investigating file discrepancies**

I think it might be easier to analyze each file cluster using a command line tool like `sed`. I want to focus on the potentially problematic lines related to noncanonical formulas and incorrect signs. Sure, I can confirm the correct canonical lines generally, but to ensure a complete audit, I should specify how many discrepancies I found, ideally saying something like, "I checked 44 explicit hits, discovered 8 discrepancies," and count the ghost mentions too. I'll need to avoid double counting while creating a list of unique lines.
codex
I’m at the classification stage now. The audit surface splits into three buckets: exact canonical matches, mathematically correct but non-canonical rewrites, and true sign/value errors; I’m consolidating the union of all candidate lines so the final counts reflect the full read-only sweep rather than just the `c_{bc}` subset.
exec
/bin/zsh -lc "python - <<'PY'
import subprocess, shlex
patterns = [
    r\"c_\\{bc\\}|c_bc\",
    r\"c_\\{(text|mathrm)\\{ghost\\}\\}|c_\\{(text|mathrm)\\{gh\\}\\}|ghost["'^'"\\n]*c\\s*=\\s*-26|bc_[0-9]+["'^'"\\n]*c\\s*=\\s*-26|reparametrisation ghosts|ghost determinant contributes|The central charge of \\"'$bc_'"\\\\lambda\\"'$ is|c = -2'"\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)\"
]
roots = ['chapters', '/Users/raeez/chiral-bar-cobar-vol2/chapters', '/Users/raeez/calabi-yau-quantum-groups/chapters']
seen = {}
for pat in patterns:
    cmd = ['rg','-n','--glob','*.tex',pat,*roots]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()
    for line in out:
        if not line.strip():
            continue
        parts = line.split(':',2)
        if len(parts) < 3:
            continue
        path, lineno, text = parts
        key = (path, int(lineno))
        seen[key] = text
for (path, lineno), text in sorted(seen.items()):
    print(f\"{path}:{lineno}:{text}\")
print('TOTAL', len(seen))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "python3 - <<'PY'
import subprocess
patterns = [
    r\"c_\\{bc\\}|c_bc\",
    r\"c_\\{(text|mathrm)\\{ghost\\}\\}|c_\\{(text|mathrm)\\{gh\\}\\}|ghost["'^'"\\n]*c\\s*=\\s*-26|bc_[0-9]+["'^'"\\n]*c\\s*=\\s*-26|reparametrisation ghosts|ghost determinant contributes|The central charge of \\"'$bc_'"\\\\lambda\\"'$ is|c = -2'"\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)\"
]
roots = ['chapters', '/Users/raeez/chiral-bar-cobar-vol2/chapters', '/Users/raeez/calabi-yau-quantum-groups/chapters']
seen = {}
for pat in patterns:
    cmd = ['rg','-n','--glob','*.tex',pat,*roots]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()
    for line in out:
        if not line.strip():
            continue
        parts = line.split(':',2)
        if len(parts) < 3:
            continue
        path, lineno, text = parts
        key = (path, int(lineno))
        seen[key] = text
for (path, lineno), text in sorted(seen.items()):
    print(f\"{path}:{lineno}:{text}\")
print('TOTAL', len(seen))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177:contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_bv_ht_extensions.tex:503:sector, but the ghost sector contributes $c = -26$, giving total
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1071:The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:922:$K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:932:dual of the reparametrisation ghost $bc_2$ ($c = -26$) is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3192:At $\lambda = 2$: $c = -26$ (reparametrisation ghosts).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3264:ghost $bc_2$ ($c = -26$) is the bosonic spin-$2$ system
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:287:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:625:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-virasoro.tex:538:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:963:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:530:because the ghost determinant contributes $c_{\text{gh}} = -26$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:935:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
chapters/connections/bv_brst.tex:359:The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.
chapters/connections/bv_brst.tex:739:$c_{bc} = 1 - 3(2{\cdot}2{-}1)^2 = -26$, $\kappa_{bc} = c_{bc}/2 = -13$);
chapters/connections/bv_brst.tex:755:$c_{bc}$ at the normalization ambiguity of the $bc$ system
chapters/connections/bv_brst.tex:767:with $c_{bc} = 1 - 3(2{\cdot}2 - 1)^2 = -26$ and
chapters/connections/bv_brst.tex:768:$\kappa_{bc} = c_{bc}/2 = -13$. The complementarity relation
chapters/connections/bv_brst.tex:2352:$c_{bc} = -26$ is a separate reparametrization contribution.
chapters/connections/thqg_gravitational_s_duality.tex:1148:The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
exec
/bin/zsh -lc "sed -n '744,770p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{remark}[Shadow archetype: contact/quartic, Koszul dual of $\beta\gamma$]
\label{rem:bc-shadow-archetype}
\index{$bc$ system!shadow archetype}
Shadow depth $r_{\max} = 4$ (class~C), the same as its Koszul dual
$\beta\gamma$. The $bc$ system has two fermionic generators ($b$ of
weight $\lambda$, $c$ of weight $1 - \lambda$) and a single
simple-pole OPE, giving it the same deformation-complex structure as
$\beta\gamma$: a T-line (Virasoro subalgebra at $c_{bc}$, with
$S_3 = 2$ and $S_4 = 10/[c_{bc}(5c_{bc}+22)]$) and a
weight-changing line (cubic vanishes by rank-one abelian rigidity).
The quartic contact shadow lives on the charged stratum mixing the
two directions, and the quintic obstruction vanishes by stratum
separation, exactly as for $\beta\gamma$.

This should not be confused with the single-generator free fermion
$\mathcal{F}$ (class~G, $r_{\max} = 2$), where fermionic
antisymmetry on a single generator kills all higher bar cohomology.
The $bc$ system has two generators, so the antisymmetry argument
does not apply.
exec
/bin/zsh -lc "sed -n '2496,2512p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '890,906p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2948,2960p' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
archetypal class~C algebra: contact structure from a non-metric
source.

The Koszul dual is the $bc$-ghost system, with
$c_{bc}(\lambda) = 1 - 3(2\lambda{-}1)^2$ and
$c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$
satisfying $c_{\beta\gamma} + c_{bc} = 0$ (verified at
$\lambda = 2$: $c_{\beta\gamma} = 26$, $c_{bc} = -26$; string
ghost cancellation). The complementarity sum
$\kappa(\beta\gamma) + \kappa(bc) = 0$: the free-field
sum rule.

The cross-channel correction vanishes at all genera:
 succeeded in 52ms:
Hochschild--Kostant--Rosenberg theorem, and the chiral
analogue replaces the exterior algebra of polyvector fields
with the vertex algebra of chiral differential forms.
The Hochschild--Kostant--Rosenberg quasi-isomorphism in the
chiral setting is established in~\cite{MSV99} via the local
coordinate presentation and \v{C}ech descent.

When $X$ is Calabi--Yau of dimension~$d$, the central charge
of $\Omega^{\mathrm{ch}}(X)$ vanishes ($c_{\beta\gamma} +
c_{bc} = 0$ per complex dimension), and the Witten genus of~$X$
coincides with the graded character of
$H^*(X, \Omega^{\mathrm{ch}})$. The modular
characteristic in this case is $\kappa^{\mathrm{ch}} =
\dim_\bC(X)$; see
Remark~\ref{rem:cdr-k3} for the K3 example.
\end{remark}

 succeeded in 52ms:
not satisfy~\textup{(iii)}, while Koszul universal algebras
$V^k(\fg)$ at generic level satisfy~\textup{(iii)} but
not~\textup{(v)}.
Every chiral algebra satisfies~\textup{(i)}.
Every positive-energy chiral algebra satisfies
\textup{(i)}--\textup{(ii)}.
The standard landscape \textup{(}Heisenberg, affine
Kac--Moody at non-critical level, $\cW$-algebras at
generic central charge, $\beta\gamma$ and $bc$
systems\textup{)} satisfies levels
\textup{(i)}--\textup{(iv)}; those that are also
$C_2$-cofinite satisfy all five.
\end{theorem}

\begin{proof}
Level~(i) is Theorem~\ref{thm:mc2-bar-intrinsic}: $D_\cA^2=0$ holds
universally because the bar differential is the Feynman-transform
exec
/bin/zsh -lc "sed -n '914,936p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3186,3198p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(bosonic), which is precisely the $\beta\gamma$ system. The bar
complex has $m_2$ only (simple-pole OPE), confirming that both
systems are Koszul. Koszul duality exchanges statistics while
preserving conformal weights; it does \emph{not} exchange spins
$\lambda \mapsto 1 - \lambda$ (that is a relabelling, not a
dualisation).

The complementarity constant vanishes:
$K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda)
= -2(6\lambda^2 - 6\lambda + 1) + 2(6\lambda^2 - 6\lambda + 1)
= 0$
for all $\lambda$. This extends to tensor products: for mutually
regular Koszul algebras,
$(\cA \otimes \cB)^! \simeq \cA^! \otimes \cB^!$,
so $K = 0$ for any tensor product of Heisenberg, $bc$, and
$\beta\gamma$ systems.

At the string-theory point $\lambda = 2$, $\mu = 3/2$: the Koszul
dual of the reparametrisation ghost $bc_2$ ($c = -26$) is the
bosonic spin-$2$ system $\beta\gamma_2$ ($c = +26$). A spin-$2$
exec
/bin/zsh -lc "sed -n '3258,3270p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\qquad
b(z)\,b(w) \sim 0,
\qquad
c(z)\,c(w) \sim 0.
\end{equation}
Central charge $c(bc) = -2(6\lambda^2 - 6\lambda + 1)$.
At $\lambda = 2$: $c = -26$ (reparametrisation ghosts).

\smallskip
\noindent
\emph{Operations.}
The nonvanishing operation is
$m_2(b,c;\,\lambda) = 1$ (simple-pole residue).
exec
/bin/zsh -lc "sed -n '956,968p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$2$ & $-26$ & reparametrisation ghost & $\beta\gamma_2$ (graviton) \\
$5/2$ & $-47$ & spin-$5/2$ ghost & $\beta\gamma_{5/2}$ \\
\bottomrule
\end{tabular}
\end{center}
At $\lambda = 2$: the Koszul dual of the reparametrisation
ghost $bc_2$ ($c = -26$) is the bosonic spin-$2$ system
$\beta\gamma_2$ ($c = +26$). A spin-$2$ boson is a
symmetric tensor field, a graviton.

\smallskip
\noindent
\emph{Complementarity.}
 succeeded in 52ms:
so that $\cA_c^! = \cA_{\alpha - c}$ and the self-dual point is $c = \alpha/2$.
Each generator of spin~$s$ contributes a ghost system with $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$;
the complementarity constant is $\alpha = -c_{\mathrm{gh}}^{\mathrm{total}}$.
For Virasoro ($s=2$): $\alpha = 2(24 - 12 + 1) = 26$, self-dual at $c = 13$. For $W_3$ ($s=2,3$): $\alpha = 26 + 2(54 - 18 + 1) = 26 + 74 = 100$, self-dual at $c = 50$. For $W_4$ ($s=2,3,4$): $\alpha = 100 + 2(96 - 24 + 1) = 100 + 146 = 246$, self-dual at $c = 123$.
\end{theorem}

\begin{proof}[Proof sketch]
Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
\end{proof}

\subsubsection{Quantum $r$-Matrices}

The quantized $r$-matrices take the form:



thinking
**Analyzing discrepancies**

I’m working on evaluating the noncanonical aspects of the rosetta_stone/w-algebras. The user wants me to flag any discrepancies, no matter how minor, which indicates several potential issues. I need to report all the distinct occurrences, likely by severity, while ensuring manageable output. There could be around 14 lines related to noncanonical formulas. I don’t have to list every correct instance but should include the significant ones, especially with wrong signs. I’ll search for all exact occurrences.
thinking
**Evaluating canonical vs. noncanonical**

I’m examining which lines are marked as canonical among various files. For instance, several files like beta_gamma.tex and genus_expansions.tex have specific canonical notations. However, some expressions in thqg_gravitational_s_duality are noncanonical. The user wants me to flag even minor discrepancies. I need to decide if terms like `-c_{\beta\gamma}` count as discrepancies since they don't match the canonical form. They mentioned verifying each hit against the canonical form, so I have to consider the context of each statement carefully.
thinking
**Assessing discrepancies in relations**

I’m considering whether the relation `c_{bc} = -c_{βγ}` should be flagged as a discrepancy. While it doesn't match the canonical formula, it may still be correct. The user seems to want to flag any differences, even in notation, but I think not every relational mention should be flagged. I want to focus on auditing central charge formula statements. If a line references a complementarity relation without a formula, I'll verify against upstream sources but won’t flag it unless there’s a clear error.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\-2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|\\-2\\(6s\\"'^2 - 6s '"\\+ 1\\)|1 - 3\\(2\\\\lambda\\{-\\}1\\)\\"'^2|1 - 3'"\\(2\\\\lambda-1\\)\\"'^2|1 - 3'"\\(2\\\\lambda - 1\\)\\"'^2'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'c_\\{bc\\}\\s*=\\s*\\+2|c_\\{bc\\}\\s*=\\s*-2|c_\\{bc\\}\\s*=\\s*0|c\\(bc\\)\\s*=\\s*-2|c\\(bc\\)\\s*=\\s*-26|c_\\{text\\{ghost\\}\\}\\(s\\)\\s*=\\s*-2\\(6s\\"'^2 - 6s '"\\+ 1\\)|c_\\{text\\{gh\\}\\}\\s*=\\s*-26|c_\\{mathrm\\{ghost\\}\\}\\s*=\\s*-26|c_\\{mathrm\\{gh\\}\\}\\s*=\\s*-26' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:321:Fermionic $bc$ system ($c_{bc} = 1 - 3(2\lambda-1)^2$):
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:793:$c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:885:$c_s = -2(6s^2 - 6s + 1)$. Summing:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1188:spin~$s$ is $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$
chapters/examples/free_fields.tex:793: c_{bc}(\lambda) \;=\; 1 - 3(2\lambda - 1)^2
chapters/examples/free_fields.tex:794: \;=\; -2(6\lambda^2 - 6\lambda + 1),
chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:957:Each generator of spin~$s$ contributes a ghost system with $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:963:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1194:spin~$s$ is $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:928:$c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$, so
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:935:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:281:Each generator of spin~$s$ contributes a ghost system with $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:287:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:923:= -2(6\lambda^2 - 6\lambda + 1) + 2(6\lambda^2 - 6\lambda + 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3191:Central charge $c(bc) = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3245:$c(\lambda) = -2(6\lambda^2 - 6\lambda + 1)$ is a quadratic
chapters/examples/landscape_census.tex:78: & $1 - 3(2\lambda{-}1)^2$ & $0$
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177:contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3191:Central charge $c(bc) = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/frame/preface.tex:2954:satisfying $c_{\beta\gamma} + c_{bc} = 0$ (verified at
chapters/frame/preface.tex:2955:$\lambda = 2$: $c_{\beta\gamma} = 26$, $c_{bc} = -26$; string
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
chapters/examples/beta_gamma.tex:637:c_{\beta\gamma} + c_{bc} = 0.
chapters/examples/beta_gamma.tex:1777:exponents cancel because $c_{\beta\gamma} + c_{bc} = 0$.
chapters/examples/free_fields.tex:767:$c_{bc} = -26$, $\kappa(bc) = -13$.
chapters/examples/free_fields.tex:5569:At the physical point $\lambda = 2$: $\kappa(bc) = -13$, $c_{bc} = -26$.
chapters/examples/toroidal_elliptic.tex:2085:contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
chapters/theory/chiral_center_theorem.tex:2505:c_{bc} = 0$ per complex dimension), and the Witten genus of~$X$
chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
chapters/examples/deformation_quantization_examples.tex:528:The symplectic fermion $\mathcal{SF}$ at $c = -2$ is the $bc$ system at $\lambda = 1$ (Section~\ref{sec:betagamma-koszul-dual}), with Koszul dual $\beta\gamma$ at $\lambda = 1$. The central charges $c(bc) = -2$ and $c(\beta\gamma) = 2$ follow from the Sugawara construction (or equivalently, from the conformal anomaly of the ghost number current); their sum $c + c' = 0$ is consistent with $bc$--$\beta\gamma$ complementarity.
chapters/connections/bv_brst.tex:2352:$c_{bc} = -26$ is a separate reparametrization contribution.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'c_\\{\\beta\\\\gamma\\}\\s*=\\s*-2|c_\\{bc\\}\\s*=\\s*\\+2|c_\\{\\beta\\\\gamma\\}\\s*=\\s*\\+2|c_\\{bc\\}\\s*=\\s*-2' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177:contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
chapters/examples/free_fields.tex:767:$c_{bc} = -26$, $\kappa(bc) = -13$.
chapters/examples/free_fields.tex:5569:At the physical point $\lambda = 2$: $\kappa(bc) = -13$, $c_{bc} = -26$.
chapters/examples/toroidal_elliptic.tex:2085:contributions $c_{\beta\gamma} = -2$ and $c_{bc} = +2$ per
chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
chapters/connections/bv_brst.tex:2352:$c_{bc} = -26$ is a separate reparametrization contribution.
chapters/frame/preface.tex:2955:$\lambda = 2$: $c_{\beta\gamma} = 26$, $c_{bc} = -26$; string

thinking
**Searching for mathematical context**

I'm considering searching for `c_{βγ}=+2`, but I wonder if there aren't many outputs because it might be escaped. I need to double-check the signs, particularly for the toroidal elliptic context. That could be good! I also need to look into the beta-gamma lines around 635 to 646, perhaps linked to a theorem. It seems like there's quite a bit to inspect and explore!
exec
/bin/zsh -lc "sed -n '628,646p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20396,20422p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1798,1812p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3012,3024p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{statistics exchange!bosonic vs.\ fermionic}
\index{central charge!complementarity}
The Koszul duality $(\beta\gamma)^! \simeq bc$ of Theorem~\ref{thm:betagamma-fermion-koszul}
has a sharp central charge consequence:
\begin{equation}\label{eq:bg-bc-koszul}
c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
\qquad
c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
\qquad
c_{\beta\gamma} + c_{bc} = 0.
\end{equation}
\end{proposition}

\begin{proof}
The central charge of the $\beta\gamma$ system is computed from the stress tensor (Theorem~\ref{thm:beta-gamma-stress}). Replacing bosonic statistics by fermionic statistics negates the Virasoro central term: the commutator $[L_m, L_n]$ picks up a sign from the fermion loop, so $c_{bc} = -c_{\beta\gamma}$.

This exact cancellation is specific to the Sym/Ext exchange.
For general Koszul dual pairs the central charges need not sum to zero:
affine Kac--Moody algebras satisfy
 succeeded in 52ms:
The $\kappa$-conductor $\kappa(\cA) + \kappa(\cA^!)$ measures the
obstruction to extending complementarity
\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}
from genus~$0$ to higher genus without correction: the
cross-channel correction $\delta F_g^{\mathrm{cross}}$
\textup{(all-weight)} of
Theorem~\textup{\ref{thm:multi-generator-universality}} is
controlled by $\kappa + \kappa'$ and vanishes identically when
$\kappa + \kappa' = 0$. The full census of $\kappa$-conductor
values appears in~\S\textup{\ref{sec:landscape-census}}.
\end{proposition}

\begin{proof}
Clause~(i): for affine Kac--Moody $V_k(\fg)$, the Feigin--Frenkel
involution $k \mapsto -(k + 2h^\vee)$ sends
$\kappa = \dim(\fg)(k + h^\vee)/(2h^\vee)$ to
$\kappa' = \dim(\fg)(-(k + 2h^\vee) + h^\vee)/(2h^\vee)
= -\kappa$, giving $\kappa + \kappa' = 0$.
For Heisenberg: $\kappa(\mathcal{H}_k) = k$,
$\kappa(\mathcal{H}_{-k}) = -k$, so $\kappa + \kappa' = 0$.
 succeeded in 52ms:
At $\lambda = 1$: $e(1) = 6 - 6 + 1 = 1$ and $e(0) = 1$, so
$e(1) + e(0) = 2 = c_{\beta\gamma}(1)$.

\item \emph{Determinant-line cancellation.}
The Mumford isomorphism gives
$\det R\Gamma(\Sigma_g, K^n) \simeq \lambda_1^{e(n)}$
where $\lambda_1 = \det R\Gamma(\Sigma_g, K)$ is the Hodge
determinant. The $\beta\gamma$ determinant line at weight $\lambda$
has total exponent $-(e(\lambda) + e(1-\lambda)) = -c_{\beta\gamma}(\lambda)$.
For the $bc$ system at the \emph{same} weight parameter, the central
charge is $c_{bc}(\lambda) = -c_{\beta\gamma}(\lambda)$
\textup{(}fermionic sign\textup{)}. Therefore
\[
 \det(\beta\gamma)_\lambda \otimes \det(bc)_\lambda
 \;\simeq\;
 succeeded in 51ms:
\begin{remark}[$\beta\gamma$ and $bc$: ghost slabs]
\label{rem:kappa-holo-bcbetagamma}
\index{beta-gamma system@$\beta\gamma$ system!Brown--Henneaux}%
\index{bc system@$bc$ system!Brown--Henneaux}%
For the $\beta\gamma$ system of conformal weight~$\lambda$,
$\kappa(\beta\gamma) = c_{\beta\gamma}/2
= 6\lambda^2 - 6\lambda + 1$; for its fermionic partner
$bc$, $\kappa(bc) = c_{bc}/2 = -(6\lambda^2 - 6\lambda + 1)$.
The free-field complementarity statement
$\kappa_{\mathrm{tot}}(\beta\gamma\,{\otimes}\,bc) = 0$
(the Koszul conductor for this specific free-field pair,
which must be distinguished from the principal Virasoro
Koszul conductor $13$ and from the non-abelian Kac--Moody



thinking
**Considering notation flags**

I’m thinking about whether to flag the noncanonical but correct notation in the beta_gamma file mentioned by the user. Since there are multiple instances, grouping them by file seems sensible. For example, in beta_gamma.tex, I notice two explicit cases at lines 315 and 635, plus some relational uses. I could report one finding like this: `chapters/examples/beta_gamma.tex:315,635` while noting that central charge appears in a noncanonical form. I’ll keep it concise while mentioning duplicates. I'll need to do something similar for rosetta_stone as well.
thinking
**Evaluating report clusters**

I’m considering how to report clusters of noncanonical instances. For example, in beta_gamma.tex at lines 315 and 635, and in free_fields.tex at 793-794, I wonder if the latter should be flagged as a low issue since it includes both canonical and noncanonical forms. If there's an equivalent form present, it complicates things further. As for critical issues, I think I should flag actual mathematical errors, like the sign reversals in toroidal_elliptic across volumes. I might note duplicates per report as needed.
thinking
**Clarifying central charge context**

I'm considering whether to search for cases where c_bc equals zero in complex dimensions. I realize that's actually a sum to zero, which isn't wrong. I noticed in `thqg_critical_string_dichotomy.tex:995` there's a mention of `κ_bc = -13 at all central charges`, which feels a bit odd since that's about kappa, not directly related to central charge formulas. I think I can ignore it unless there's a misrepresentation of the bc central charge, so maybe additional context isn't necessary.
codex
The only outright falsehood I’ve found so far is the sign reversal in the K3 CDR remarks. The remaining discrepancies are mostly canonicalization drift: formulas written as `-2(6\\lambda^2-6\\lambda+1)` or its `s`-ghost analogue instead of the repo’s canonical `1-3(2\\lambda-1)^2`. I’m checking the full duplicate set now so the final report groups them cleanly rather than treating one line as representative of many unchecked copies.
exec
/bin/zsh -lc "sed -n '348,360p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '786,798p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '276,290p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '922,938p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{center}
The identity $c_{\mathrm{pair}}^{(N)} = \alpha_N$%
\index{ghost central charge!WN@$\mathcal{W}_N$ identity}%
{} is not a coincidence: it is the ghost central
charge.\label{prop:ghost-identity-alphaN-active}
The $\cW_N$ ghost system consists of $bc$-pairs of spins
$s = 2, 3, \ldots, N$, each contributing
$c_s = -2(6s^2 - 6s + 1) = -(3(2s-1)^2 - 1)$, so
\[
c_{\mathrm{ghost}}(\cW_N)
\;=\; \sum_{s=2}^{N} c_s
\;=\; -2(N{-}1)(2N^2{+}2N{+}1)
\;=\; -\alpha_N
 succeeded in 51ms:
\begin{equation}
% label removed: eq:central-charge-shift
\alpha = \sum_{i=1}^n 2(6s_i^2 - 6s_i + 1),
\end{equation}
so that $\cA_c^! = \cA_{\alpha - c}$ and the self-dual point is $c = \alpha/2$.
Each generator of spin~$s$ contributes a ghost system with $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$;
the complementarity constant is $\alpha = -c_{\mathrm{gh}}^{\mathrm{total}}$.
For Virasoro ($s=2$): $\alpha = 2(24 - 12 + 1) = 26$, self-dual at $c = 13$. For $W_3$ ($s=2,3$): $\alpha = 26 + 2(54 - 18 + 1) = 26 + 74 = 100$, self-dual at $c = 50$. For $W_4$ ($s=2,3,4$): $\alpha = 100 + 2(96 - 24 + 1) = 100 + 146 = 246$, self-dual at $c = 123$.
\end{theorem}

\begin{proof}[Proof sketch]
Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
\end{proof}

\subsubsection{Quantum $r$-Matrices}
 succeeded in 51ms:
equivalently the one-loop central-charge shift is
\[
\Delta c = \frac{\alpha}{2}
= \sum_{i=1}^n (6s_i^2 - 6s_i + 1).
\]
Each generator of spin~$s$ contributes a ghost system with
$c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$, so
$\alpha = -c_{\mathrm{gh}}^{\mathrm{total}}$.
For Virasoro ($s=2$): $\alpha = 26$ and $\Delta c = 13$.
For $W_3$ ($s=2,3$): $\alpha = 100$ and $\Delta c = 50$.
\end{theorem}

\begin{proof}[Proof sketch]
Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
\end{proof}

\subsubsection{Quantum $r$-Matrices}
 succeeded in 51ms:
to $\beta'_0 = 16/(522 - 5c)$.
\end{theorem}

\begin{proof}
Each generator of $\mathcal{W}_3$ contributes a $bc$-ghost system
upon BV-BRST quantization of the Khan--Zeng 3D HT action.
The ghost central charge for spin~$s$ is
$c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$:
\[
c_{\mathrm{gh}}(2) = -26, \qquad
c_{\mathrm{gh}}(3) = -74, \qquad
c_{\mathrm{gh}}^{\mathrm{total}} = -100.
\]
exec
/bin/zsh -lc "python3 - <<'PY'
import subprocess, re
pat = r'-2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|-2\\(6s\\"'^2 - 6s '"\\+ 1\\)|-\\(3\\(2s-1\\)\\"'^2 - 1'"\\)'
cmd = ['rg','-n','--glob','*.tex',pat,'chapters','/Users/raeez/chiral-bar-cobar-vol2/chapters','/Users/raeez/calabi-yau-quantum-groups/chapters']
out = subprocess.run(cmd,capture_output=True,text=True).stdout.splitlines()
for l in out:
    print(l)
print('TOTAL', len(out))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
TOTAL 0

thinking
**Resolving quoting issues**

I’m noticing a pattern with the quoting issue I’m facing. It might be worthwhile to try using a simpler method with shell regular expressions instead. I think that could potentially solve the problem. It really seems like simplifying the approach might just get me where I need to go! Let me check how I want to format this and if it aligns with what I'm trying to achieve.
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\-2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|\\-2\\(6s\\"'^2 - 6s '"\\+ 1\\)|\\-\\(3\\(2s-1\\)\\"'^2 - 1'"\\)' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
      20
exec
/bin/zsh -lc "rg -n --glob '*.tex' '\\-2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|\\-2\\(6s\\"'^2 - 6s '"\\+ 1\\)|\\-\\(3\\(2s-1\\)\\"'^2 - 1'"\\)' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:793:$c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:885:$c_s = -2(6s^2 - 6s + 1)$. Summing:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:1188:spin~$s$ is $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:957:Each generator of spin~$s$ contributes a ghost system with $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:963:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1194:spin~$s$ is $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:928:$c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$, so
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:935:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:281:Each generator of spin~$s$ contributes a ghost system with $c_{\mathrm{gh}}(s) = -2(6s^2 - 6s + 1)$;
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:287:Each spin-$s$ generator contributes a $(b,c)$ ghost system of conformal weights $(s, 1-s)$ upon BRST quantization. The ghost central charge for such a system is $c_{\text{ghost}}(s) = -2(6s^2 - 6s + 1)$ (see, e.g., \cite{FMS86,Pol98}). In the BV-BRST framework of the 3D holomorphic-topological theory, the 1-loop vacuum bubble diagram produces a shift $\Delta c = |c_{\text{ghost}}(s)|/2 = 6s^2 - 6s + 1$ per generator. This factor of $\tfrac{1}{2}$ arises because the 3D theory computes the \emph{chiral half} of the full ghost determinant (the $\bar\partial$-direction ghost determinant contributes the conjugate half; the factorization is a consequence of the holomorphic-topological splitting). The total shift is obtained by summing over all generators.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:355:$c_s = -2(6s^2 - 6s + 1) = -(3(2s-1)^2 - 1)$, so
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:923:= -2(6\lambda^2 - 6\lambda + 1) + 2(6\lambda^2 - 6\lambda + 1)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3191:Central charge $c(bc) = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3245:$c(\lambda) = -2(6\lambda^2 - 6\lambda + 1)$ is a quadratic
chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
chapters/examples/free_fields.tex:794: \;=\; -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1071:The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/connections/thqg_gravitational_s_duality.tex:1148:The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.

thinking
**Checking noncanonical formulas**

I'm reviewing 20 noncanonical explicit formula lines to see if I've captured all variants, like `-c_{βγ}` or `c = -26`. These values are derived, not just rewritten formulas. I should check boundary values at λ=2, λ=1, and λ=1/2 using direct computation based on canonical formulas. I need to mention in the final summary that boundary checks pass, except for the incorrect K3 sign. I might compute this in the shell using Python or bc for ease.
exec
/bin/zsh -lc "python3 - <<'PY'
from fractions import Fraction
for lam in [2,1,Fraction(1,2),0]:
    val = 1 - 3*(2*lam - 1)**2
    print(lam, val)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2 -26
1 -2
1/2 1
0 -2

thinking
**Checking algebraic identity**

I need to perform a direct check of the algebraic identity `1 - 3(2λ-1)^2 = -2(6λ^2 - 6λ + 1)`. This could be done by expanding each side, which might involve a bit of symbolic computation. I could look into using some expansion methods or tools to make sure both sides are equal. It's a matter of confirming the identity accurately. Let's see how this works step by step!
exec
/bin/zsh -lc "python3 - <<'PY'
import sympy as s
lam=s.symbols('lam')
expr = s.expand(1 - 3*(2*lam - 1)**2)
print(expr)
print(s.simplify(expr + 2*(6*lam**2 - 6*lam + 1)))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 143ms:
-12*lam**2 + 12*lam - 2
0

thinking
**Calculating with formula**

I think I need to directly check the formula and compute the value at s=2. That seems like a straightforward approach. I should probably confirm that I have the right formula in mind and then make the necessary calculations. It’s important to ensure everything is accurate, so I’ll proceed with calculating and see what results I get. If anything seems off, I can always double-check!
exec
/bin/zsh -lc "python3 - <<'PY'
for s in [2,3,4]:
    val = 1 - 3*(2*s - 1)**2
    print(s, val)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2 -26
3 -74
4 -146



thinking
**Evaluating candidate lines**

I need to work with the candidate list, which has 57 lines. I should focus on the actual file contexts around clusters, but for some lines, just the line itself might be enough for value statements. I have to ensure there aren't any false positives, especially for specific cases like the rosetta_stone 922, which uses the correct formula. After checking, it looks like I might have found 11 violations. For my summary, I could say, "Instances checked: 57 | Violations found: 11."
thinking
**Deciding findings list**

I need to finalize the exact findings list. First off, I have a critical issue: in the file chapters/examples/toroidal_elliptic.tex at line 2085, there’s a remark about K3 CDR that reverses the signs. It states `c_{βγ}=-2` and `c_{bc}=+2` per complex dimension, but with the canonical `λ=1`, I get `c_{βγ}=+2` and `c_{bc}=-2`. I should definitely highlight this discrepancy in the findings.
thinking
**Checking file paths and line numbers**

I'm focusing on keeping things concise for the user. I think they might be looking for a specific `file:line` format, like using a clickable path. For example, - [CRITICAL] [toroidal_elliptic.tex](/Users/.../chapters/examples/toroidal_elliptic.tex:2085) could work. I should check the line numbers for free_fields at 794 and genus_expansions at 2380. Also, I want to ensure that the central charge formula is around line 3245. So, I'll inspect that next.
exec
/bin/zsh -lc "sed -n '3240,3248p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\smallskip
\noindent
\emph{Weight-$\lambda$ landscape.}
The central charge
$c(\lambda) = -2(6\lambda^2 - 6\lambda + 1)$ is a quadratic
in~$\lambda$ with roots at $\lambda = (3 \pm \sqrt{3})/6$.
Key specialisations:
\begin{center}






thinking
**Evaluating formula context**

I'm searching for any canonical formulas in Volume II that might differ from the non-canonical ones used in Rosetta. I already reviewed some aspects of the gravitational duality proof. There's a potential issue with `rosetta_stone.tex:3245`, which discusses roots at `(3 ± sqrt3)/6`, but this seems correct if the formula is zero. I might need to check the w-algebra contexts across multiple files and watch for duplicate formulas. It might be better to choose a representative line from each file while noting duplicates within those files for clarity.
thinking
**Counting findings per file**

I’m counting findings across various files, identifying them based on their criticality levels: high, medium, and low. It looks like I might have 13 findings overall, which seems reasonable. I’ll have to ensure the final count is around 50-70 lines, which includes a summary. I’ve noted potential non-canonical formulas in the beta_gamma file and duplicated lines. For the rosetta_stone file, I could focus on the first significant formula line, while also mentioning complementary occurrences for clarity. This approach applies to other files too, like w-algebras.
thinking
**Organizing findings efficiently**

The user asked me to verify each instance and report my findings, but I think grouping similar issues across related files would be more useful. For example, I could categorize W-algebra ghost drift into one "MEDIUM" finding with several file references. I can narrow it down to eight total findings, with detailed descriptions for clarity while still adhering to the contract requirements. I think this approach will keep everything clear and concise!
thinking
**Determining inclusion criteria**

I need to decide if the beta_gamma medium includes 315 and 635 — and I believe it does. I think clarifying this inclusion is essential for accurately representing the findings. It’s quick, but ensuring I’m on the right path is crucial. I want to make sure I'm capturing all relevant factors here and providing clear guidance on what should be included in that medium classification. So, yes, I’ll include them!
thinking
**Checking value consistency**

I've confirmed that the values are correct through an expansion check, but I noticed that the notation diverges from the canonical source. It might be worth mentioning that line 321 in the same file does follow the canonical form. The MEDIUM thqg_grav_s_duality cluster shows that in both Volume I and the duplicate Volume II, line 1071 uses a noncanonical quadratic rewrite. While the values seem valid, the formula's presentation shifts away from what’s considered standard.
thinking
**Drafting census verification summary**

I’m looking to verify the `bc` row in landscape_census, particularly lines 76 to 78 for the canonical formula. In the summary, I’ll note that the canonical source is `landscape_census.tex:76-78`. I should mention that there are 57 instances checked, which include 44 `c_bc` hits and 13 auxiliary ghost-value surfaces. I think summarizing with "57 unique candidate lines" is enough, and there are no high findings. I’ll aim for a concise bullet list with 8 findings and a summary.
codex
- [CRITICAL] [chapters/examples/toroidal_elliptic.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/toroidal_elliptic.tex:2085) — The K3 CDR remark reverses the local free-field signs: it states `c_{\beta\gamma}=-2` and `c_{bc}=+2` per complex dimension. The canonical source [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:76) gives `c_{bc}(\lambda)=1-3(2\lambda-1)^2`; at `\lambda=1` this is `-2`, while `c_{\beta\gamma}=+2`.

- [CRITICAL] [chapters/examples/toroidal_elliptic.tex](/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177) — Vol III duplicates the same K3 CDR sign reversal: `c_{\beta\gamma}=-2`, `c_{bc}=+2`. This disagrees with the canonical `\lambda=1` boundary values `c_{bc}=-2`, `c_{\beta\gamma}=+2`.

- [MEDIUM] [chapters/examples/beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:315) — The theorem surface uses only the non-canonical rewrite `c_{bc}=-2(6\lambda^2-6\lambda+1)`; the same drift recurs at line 635. Expansion shows it is equivalent to the canonical `1-3(2\lambda-1)^2`, so this is notation drift, not a false value. The same file’s line 321 uses the canonical form, so the file is internally inconsistent.

- [MEDIUM] [chapters/connections/thqg_gravitational_s_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_gravitational_s_duality.tex:1148) — Vol I states the `bc_\lambda` central charge only as `-2(6\lambda^2-6\lambda+1)`; the duplicate in Vol II at [thqg_gravitational_s_duality.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1071) does the same. Boundary checks `\lambda=2,-26`, `\lambda=1,-2`, `\lambda=\tfrac12,1` confirm correctness, but both surfaces drift from the canonical form.

- [MEDIUM] [chapters/examples/rosetta_stone.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3191) — The explicit `bc` central-charge discussion uses only the non-canonical quadratic form; the same drift recurs at lines 923 and 3245. Values are correct after expansion and boundary checks, but the formula surface does not match the canonical source.

- [MEDIUM] [chapters/examples/w-algebras.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex:928) — The spin-`s` ghost formula is written in non-canonical form `-2(6s^2-6s+1)` here and in sibling files [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:957), [w-algebras-conditional.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex:281), [w-algebras-stable.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:793), and [w-algebras-frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-frontier.tex:355). This is equivalent to `1-3(2s-1)^2`; checks at `s=2,3,4` give `-26,-74,-146`, so the values are right but the notation is non-canonical throughout the Vol II cluster.

- [LOW] [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:794) — The file gives the canonical formula at line 793, then immediately appends the non-canonical rewrite `=-2(6\lambda^2-6\lambda+1)`. This is correct but still drifts from the canonical presentation.

- [LOW] [chapters/examples/genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2380) — The line leads with the non-canonical quadratic form before giving the canonical form. The value is correct, but the ordering still departs from the canonical source.

All other checked `c_{bc}`/ghost-value surfaces matched the canonical formula after direct expansion and boundary evaluation.

## Summary
Instances checked: 57 | Violations found: 8 | Verdict: FAIL
tokens used
101,316
