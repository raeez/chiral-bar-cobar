# C19_bc_bg_swap_check (409s)

**Findings**

1. PROBLEM at [beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:315): the theorem surface stated the fermionic `bc` central charge only in the reduced form `-2(6\lambda^2 - 6\lambda + 1)`. That value is correct, but it is AP137-prone because it hides the canonical fermionic formula and makes bc/bg swaps easier. EXACT edit applied: changed
`$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.`
to
`$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.`

2. PROBLEM at [beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:635): the Koszul-complementarity equation had the same AP137-prone `bc`-only reduced form. EXACT edit applied: changed
`c_{bc} = -2(6\lambda^2 - 6\lambda + 1),`
to
`c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),`

3. PROBLEM at [genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2380): the genus-expansion summary led with the reduced `bc` polynomial instead of the canonical fermionic formula. EXACT edit applied: changed
`$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$`
to
`$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$`

Across the live source trees of Vol I, Vol II, and Vol III, I found no surviving swapped bc/bg formulas. Vol II and Vol III needed no live edits. The only remaining wrong-shape literals are in [wrong_formulas_blacklist_wave12.md](/Users/raeez/chiral-bar-cobar/compute/audit/wrong_formulas_blacklist_wave12.md:54), where they are intentionally recorded as `WRONG`.

Verification was grep plus direct value checks at `\lambda = 1/2, 1, 3/2, 2`, giving `(c_bc, c_bg) = (1,-1), (-2,2), (-11,11), (-26,26)`. I did not run a full TeX build.


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
session id: 019d87d0-38d8-76e1-9fce-70a593dd9294
--------
user
<task>
You are an adversarial auditor + fixer. Find issues AND fix them in one pass.
For each finding: PROBLEM at file:line, then the EXACT edit applied.
</task>
<action_safety>
Only edit the assigned files. Minimum truthful edits.
</action_safety>
<completeness_contract>
Be exhaustive within the assigned scope. Fix everything you find.
</completeness_contract>


Comprehensive bc/bg central charge audit across ALL volumes (AP137).
For every occurrence of c_bc or c_betagamma: verify the formula is correct.
c_bc(lambda) = 1 - 3(2lambda-1)^2 (fermionic).
c_bg(lambda) = 2(6lambda^2-6lambda+1) (bosonic).
c_bc + c_bg = 0. Fix any swaps.
mcp startup: no servers



thinking
**Planning codebase audit**

I need to perform a codebase audit for central charges across all volumes, following the AGENTS' instructions. The user wants a comprehensive audit, which means I’ll need to focus specifically on assigned files with potential issues. I want to ensure I read necessary documents like CLAUDE.md and the relevant dependencies first. It seems I'll need to use multi-path-verify and possibly cross-volume-propagation skills. I’ll announce these skills in my commentary while inspecting the workspace.
thinking
**Assessing write access in workspace**

I have read access in the workspace at /Users/raeez/chiral-bar-cobar, but editing might be restricted in sibling directories because they aren’t in writable roots. The user wants edits across all volumes, yet my current environment only allows me to write in this specific repository. I can likely read sibling files, but to edit outside these writable areas requires special approval, which seems unlikely. I’ll need to note any issues found in those other volumes since I can’t make changes there.
thinking
**Updating the process for exploration**

I need to start with a commentary update to acknowledge the user’s request and outline my first step. After assessing the context, I might adjust my plan as needed and ensure I provide frequent updates. I’ll use the "rg" tool and may spawn explorer agents since they are preferred for codebase inquiries. These explorers could help search different volumes in parallel, as the shared workspace might allow access to sibling directories. So, should I create explorer subagents for each volume or specific search tasks?
codex
Scope is the bc/bg central charge surface across Volumes I, II, and III. I’m reading the required constitutional files first, then I’ll grep every `c_bc` / `c_betagamma` occurrence, verify against the canonical formulas, and patch only the files that are actually wrong.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

 succeeded in 50ms:
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

thinking
**Considering formula adjustments**

I'm thinking that if we touch on Formula One, we might use the PE-8 cross-volume formula. I'm not sure if PE-12 prose hygiene is necessary. I'll need to address the mathematical changes regarding the cross-volume formula and make a note to fill in the commentary for PE-8 before making any edits. Perhaps we shouldn't focus on "kappa" either. Later, we should ensure to fill the cross-volume verification block with the formula information and my verdict.
codex
I’m using `multi-path-verify` first to enumerate and verify every bc/betagamma formula, then `cross-volume-propagation` to patch every genuine duplicate in one sweep. After the grep pass I’ll classify each hit as correct, swapped, or incomplete before touching files.
exec
/bin/zsh -lc "rg -n --hidden -S '1 - 3\\(2\\\\lambda-1\\)\\"'^2|1-3'"\\(2\\\\lambda-1\\)\\"'^2|2'"\\(6\\\\lambda\\"'^2-6'"\\\\lambda\\+1\\)|2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|1-3\\(2\\lambda-1\\)\\"'^2|2'"\\(6\\lambda\\"'^2-6'"\\lambda\\+1\\)' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:1 - 3\(2\\lambda-1\)\^2|1-3\(2\\lambda-1\)\^2|2\(6\\lambda\^2-6\\lambda\+1\)|2\(6\\lambda\^2 - 6\\lambda \+ 1\)|1-3\(2\lambda-1\)\^2|2\(6\lambda\^2-6\lambda\+1\))
                                                                                                                             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n --hidden -S 'c_bc|c_\\{bc\\}|c_betagamma|c_\\{betagamma\\}|c_\\\\beta\\\\gamma|c_\\{\\\\beta\\\\gamma\\}|beta-gamma|beta gamma|bc system|bc ghost|betagamma' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 471ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2397:invariant that measures the bc ghost central charge, not the kappa
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:3518:c_{\beta\gamma}^{(2,-1)} + c_{\beta\gamma}^{(3/2,-1/2)}
/Users/raeez/chiral-bar-cobar/elite_rescue_20260413_141402/H03_heal_platonic_P11_P16.md:59:P13 operadic SC-formality, P14 betagamma witness, P15 universal family,
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1:\chapter{\texorpdfstring{The $\beta\gamma$ system}{The beta-gamma system}}\label{chap:beta-gamma}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:30:(Theorem~\ref{thm:betagamma-fermion-koszul}), exchanging bosonic
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:43:$\lambda$.}\label{tab:betagamma-five-theorems}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:51: & Proved & Thm~\ref{thm:betagamma-bc-koszul} \\
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:55: & Proved & Thm~\ref{thm:betagamma-complete-bar} \\
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:62: & Proved & Rem~\ref{rem:betagamma-shadow-archetype-free} \\
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:74:$\beta\gamma$.}\label{tab:betagamma-shadow-archetype}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:101:\begin{equation}\label{eq:betagamma-triple-ch}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:110:(Theorem~\ref{thm:betagamma-bc-koszul}). The collision-residue
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:135:$\beta\gamma$]\label{rem:betagamma-master-mc}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:147:(Proposition~\ref{prop:betagamma-obstruction-coefficient});
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:156:\label{rem:betagamma-three-pillar}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:157:\index{beta-gamma@$\beta\gamma$!three-pillar interpretation}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:164:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}).
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:178:\label{rem:betagamma-genus-two-shells}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:179:\index{beta-gamma@$\beta\gamma$!genus-two shells}
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:188:(Corollary~\ref{cor:nms-betagamma-mu-vanishing}) implies no quartic

thinking
**Narrowing search parameters**

I’m finding the search output to be too large and truncated, so I need to narrow it down. I could consider using explorer agents to search and summarize effectively, or utilize shell commands like `rg` for specific files. Focusing on exact terms will help me manage the search better. I want to inspect occurrences of specific formula names, like `c_bc` and `c_{\beta\gamma}`. It seems like running explorers in parallel for each volume would be a solid approach.
codex
The first grep was too broad because it pulled every general betagamma mention. I’m narrowing to the actual central-charge notations now and splitting the audit by volume so I can verify each hit in context instead of skimming noisy matches.
collab spawn_agent(call_B0Hioh2bn7mjreM5xg4hOhvq, prompt="Search /Users/raeez/chiral-bar-cobar-vol2 for every occurrence of bc/betagamma central charge notation relevant to AP137…")
mcp startup: no servers
spawn_agent(call_B0Hioh2bn7mjreM5xg4hOhvq, prompt="Search /Users/raeez/chiral-bar-cobar-vol2 for every occurrence of bc/betagamma central charge notation relevant to AP137…") pending init:
  agent: 019d87d0-ff9f-7621-acbc-8d70c3f4a6e0
collab spawn_agent(call_UQfk2k6ZsdOh6wvZ6xyoXej9, prompt="Search /Users/raeez/chiral-bar-cobar for every occurrence of bc/betagamma central charge notation relevant to AP137. Inc…")
spawn_agent(call_UQfk2k6ZsdOh6wvZ6xyoXej9, prompt="Search /Users/raeez/chiral-bar-cobar for every occurrence of bc/betagamma central charge notation relevant to AP137. Inc…") pending init:
  agent: 019d87d0-ffa3-70b0-a3b6-89f43fb1c8a6
mcp startup: no servers
collab spawn_agent(call_ZeurULurNr9dawhaMBkMY7yw, prompt="Search /Users/raeez/calabi-yau-quantum-groups for every occurrence of bc/betagamma central charge notation relevant to A…")
mcp startup: no servers
spawn_agent(call_ZeurULurNr9dawhaMBkMY7yw, prompt="Search /Users/raeez/calabi-yau-quantum-groups for every occurrence of bc/betagamma central charge notation relevant to A…") pending init:
  agent: 019d87d0-ffbd-7bf3-b20e-44cc2ea632c0
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"c_bc|c\\\\_{bc}|c_bg|c\\\\_{bg}|c_betagamma|c\\\\_{betagamma}|c_\\\\\\\\beta\\\\\\\\gamma|beta-gamma central charge\"" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:c_bc|c\_{bc}|c_bg|c\_{bg}|c_betagamma|c\_{betagamma}|c_\\beta\\gamma|beta-gamma central charge)
                ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "c_bc"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md:671:c_bc(lambda) = 1 - 3(2*lambda-1)^2
AGENTS.md:673:c_bc + c_bg = 0
compute/lib/scattering_diagram_e1_mc.py:521:    mc_bch = sd.mc_equation_check()
compute/lib/scattering_diagram_e1_mc.py:563:        'mc_bch_holds': mc_bch['mc_holds'],
compute/lib/scattering_diagram_e1_mc.py:1523:            'mc_bch_holds': conifold['mc_bch_holds'],
compute/lib/scattering_diagram_e1_mc.py:1548:            conifold['mc_bch_holds']
compute/lib/shadow_tower_chart_gluing.py:1092:    quartic_bch = wall_quartic_correction_bch(
compute/lib/shadow_tower_chart_gluing.py:1100:        "path2_bch_expansion": quartic_bch,
compute/tests/test_cy3_modularity_constraints.py:805:    def test_quintic_bcov_c1(self):
compute/tests/test_scattering_diagram_e1_mc.py:909:        assert result['conifold']['mc_bch_holds']
compute/tests/test_scattering_diagram_e1_mc.py:1032:        assert result['mc_bch_holds']
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_bc\\b|c\\_{bc}\\b|c_betagamma\\b|c\\_{betagamma}\\b|c_\\\\beta\\\\gamma\\b\"" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:c_bc\b|c\_{bc}\b|c_betagamma\b|c\_{betagamma}\b|c_\beta\gamma\b)
                  ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "c_bc"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 537

AGENTS.md:176:c_bc(lambda) = 1 - 3(2*lambda-1)^2                    # fermionic; lambda=1/2→1, lambda=2→-26
AGENTS.md:178:c_bc + c_bg = 0                                        # pointwise; verify at lambda=1: 2+(-2)=0
AGENTS.md:223:B6.  c_{bg} = 1-3(2L-1)^2              # that is c_bc — swapped
fix_wave_A_20260413_112727/A06_toroidal_v1.md:43:States c_betagamma = -2, c_bc = +2. Should be c_bc = -2, c_bg = +2.
fix_wave_A_20260413_112727/A06_toroidal_v1.md:44:Canonical: c_bc(lambda=1) = 1-3(1)^2 = -2. c_bg(lambda=1) = 2(1) = +2.
fix_wave_A_20260413_112727/A06_toroidal_v1.md:191:/bin/zsh -lc "rg -n \"c_\\\\beta\\\\gamma|c_\\\\{beta\\\\gamma\\\\}|c_\\\\{bc\\\\}|c_bc|c_bg|c_\\\\{bg\\\\}|beta\\\\gamma|\\\\bbc|\\\\bbg\" chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 54ms:
fix_wave_A_20260413_112727/A06_toroidal_v1.md:193:    (?:c_\beta\gamma|c_\{beta\gamma\}|c_\{bc\}|c_bc|c_bg|c_\{bg\}|beta\gamma|\bbc|\bbg)
CLAUDE.md:229:**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).
CLAUDE.md:231:**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).
CLAUDE.md:233:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
CLAUDE.md:423:**FM3. Bosonic/fermionic conformal-anomaly conflation.** `c_bg` and `c_bc` look structurally similar (both polynomial in lambda with centre at 1/2) and satisfy c_bg+c_bc=0. Opus swaps them under pressure. Counter: after writing any ghost central charge, substitute lambda=2 AND lambda=1 and verify c_bc(2)=-26, c_bg(2)=+26, sum=0 pointwise.
rectification_20260412_233715/R15_toroidal_elliptic_v1.md:60:   States c_betagamma = -2 and c_bc = +2 per complex dimension.
rectification_20260412_233715/R15_toroidal_elliptic_v1.md:61:   CANONICAL: c_bc(lambda=1) = 1-3(2*1-1)^2 = 1-3 = -2. c_bg(lambda=1) = 2(6-6+1) = +2.
rectification_20260412_233715/R15_toroidal_elliptic_v1.md:62:   So c_bc = -2, c_bg = +2. The file has them SWAPPED.
rectification_20260412_233715/R15_toroidal_elliptic_v1.md:63:   FIX: Swap the signs. c_bc = -2, c_betagamma = +2.
rectification_20260412_233715/R15_toroidal_elliptic_v1.md:92:/bin/zsh -lc 'rg -n "c_betagamma|c_bc|K3|CDR|beta.?gamma|bc system" chapters/examples/toroidal_elliptic.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
wave2_audit_20260413_001942/K06_free_fields_bg.md:54:CANONICAL DATA: c_bg=2(6lambda^2-6lambda+1), lambda=2→+26, c_bc+c_bg=0, class C
standalone/five_theorems_modular_koszul.tex:2184:% C5: c_bc(lambda) = 1 - 3(2*lambda-1)^2; lambda=1/2 -> 1; lambda=2 -> -26
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_bc\\b\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/ds_brst_sc_engine.py:536:            c_bc = -2 * (6 * d ** 2 - 6 * d + 1)
compute/lib/ds_brst_sc_engine.py:537:            c_ghost += n_pairs * c_bc
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "c_bg"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md:672:c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)
AGENTS.md:673:c_bc + c_bg = 0
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_\\{bc\\}\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex:363:The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.
chapters/connections/bv_brst.tex:743:$c_{bc} = 1 - 3(2{\cdot}2{-}1)^2 = -26$, $\kappa_{bc} = c_{bc}/2 = -13$);
chapters/connections/bv_brst.tex:759:$c_{bc}$ at the normalization ambiguity of the $bc$ system
chapters/connections/bv_brst.tex:771:with $c_{bc} = 1 - 3(2{\cdot}2 - 1)^2 = -26$ and
chapters/connections/bv_brst.tex:772:$\kappa_{bc} = c_{bc}/2 = -13$. The complementarity relation
chapters/connections/bv_brst.tex:2548:$c_{bc} = -26$ is a separate reparametrization contribution.
compute/lib/ds_brst_sc_engine.py:486:    Each pair at grade d has c_{bc} = -2(6d²-6d+1).
compute/lib/hochschild_bulk_bridge.py:180:    kappa(bc) = c_{bc}/2 = -2/2 = -1.
chapters/examples/rosetta_stone.tex:922:$K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda)
working_notes.tex:7184:c_{bc}(\lambda)
working_notes.tex:7190:Modular characteristics: $\kappa(bc) = c_{bc}/2 = -(6\lambda^2
working_notes.tex:7197:c_{bc}(\lambda) + c_{\beta\gamma}(\lambda) = 0,
working_notes.tex:7429:c_{bc}(2) &= -2(6 \cdot 4 - 6 \cdot 2 + 1) = -2 \cdot 13 = -26, \\
working_notes.tex:7451:c_{\mathrm{dual}} &= c_{\beta\gamma}(2) + c_{bc}(3/2)
working_notes.tex:7760:and $c_{bc}(1-\lambda) = c_{bc}(\lambda)$ (the formula is symmetric
working_notes.tex:7790:\item $bc_\lambda$: $K = c_{bc} + c_{\beta\gamma} = 0$
working_notes.tex:7792:\item $\beta\gamma_\mu$: $K = c_{\beta\gamma} + c_{bc} = 0$
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "betagamma"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 411

compute/lib/holomorphic_cs_chiral_engine.py:1442:# 10. E_3 bar complex for betagamma (class C, shadow depth 4)
compute/lib/holomorphic_cs_chiral_engine.py:1481:    r"""E_3 bar complex of the betagamma system, the simplest class C algebra.
compute/lib/holomorphic_cs_chiral_engine.py:1483:    CLASSIFICATION: The betagamma system (beta-gamma ghosts, bc system)
compute/lib/holomorphic_cs_chiral_engine.py:1495:    The betagamma system has TWO generators (beta, gamma) with conformal
compute/lib/holomorphic_cs_chiral_engine.py:1499:    As a Koszul algebra: the betagamma system is the Weyl algebra A_1 =
compute/lib/holomorphic_cs_chiral_engine.py:1524:    The reason: the betagamma charge grading (beta has charge +1, gamma has
compute/lib/holomorphic_cs_chiral_engine.py:1549:      Class C (betagamma, 2 gen):   H* = (1+t)^6 = H*(T^6),  dim 64 = 2^6
compute/lib/holomorphic_cs_chiral_engine.py:1554:    kappa_ch = -1/2 (from the conformal anomaly of the betagamma system
compute/lib/holomorphic_cs_chiral_engine.py:1557:    The Koszul dual of betagamma is the bc system (exterior algebra).
compute/lib/holomorphic_cs_chiral_engine.py:1570:        kappa_ch_val: kappa_ch = -1/2 (betagamma conformal anomaly, AP113)
compute/lib/holomorphic_cs_chiral_engine.py:1576:        """Initialize the betagamma E_3 bar complex.
compute/lib/holomorphic_cs_chiral_engine.py:1580:                Default: Q^contact = 1 for standard betagamma at c = -2.
compute/lib/holomorphic_cs_chiral_engine.py:1585:        # Q^contact = -24/(c*(5c+22)) for betagamma;
compute/lib/holomorphic_cs_chiral_engine.py:1588:        self.alpha = Rational(0)  # cubic shadow vanishes for betagamma
compute/lib/holomorphic_cs_chiral_engine.py:1624:        The betagamma charge grading (beta: +1, gamma: -1) forces d_4 = 0
compute/lib/holomorphic_cs_chiral_engine.py:1667:        The betagamma system is Koszul (Weyl algebra).  Its bar cohomology
compute/lib/holomorphic_cs_chiral_engine.py:1718:        """kappa_ch = -1/2 for the betagamma system."""
compute/lib/holomorphic_cs_chiral_engine.py:1725:        Actually: betagamma Koszul conductor is nonzero for class C.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"c_bc\\(lambda\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md:176:c_bc(lambda) = 1 - 3(2*lambda-1)^2                    # fermionic; lambda=1/2→1, lambda=2→-26
fix_wave_E_20260413_182434/E03_test_gaps_central.md:2242:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:2562:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:2950:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:3368:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:3762:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:4346:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:4761:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:5155:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:5672:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:6098:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
fix_wave_E_20260413_182434/E03_test_gaps_central.md:6516:+        # VERIFIED: [LT] CLAUDE.md C5 gives c_bc(lambda)=1-3(2lambda-1)^2.
CLAUDE.md:229:**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).
CLAUDE.md:233:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
rectification_20260412_233715/R15_toroidal_elliptic_v1.md:61:   CANONICAL: c_bc(lambda=1) = 1-3(2*1-1)^2 = 1-3 = -2. c_bg(lambda=1) = 2(6-6+1) = +2.
scripts/fix_campaign_100.py:171:Canonical: c_bc(lambda=1) = 1-3(1)^2 = -2. c_bg(lambda=1) = 2(1) = +2.
scripts/fix_campaign_100.py:487:c_bc(lambda) = 1 - 3(2lambda-1)^2 (fermionic).
audit_campaign_20260412_230832/F08_c_bc.md:54:CANONICAL: c_bc(lambda) = 1 - 3(2*lambda-1)^2
scripts/adversarial_campaign.py:175:    ("F08_c_bc", "c_bc(lambda) = 1 - 3(2*lambda-1)^2", "bc central charge", "grep -rn 'c_bc\\|c_{bc}\\|1.*3.*2.*lambda' chapters/ | head -30", "lambda=2→-26. WRONG: 2(6L^2-6L+1)"),
scripts/rectification_campaign.py:421:   CANONICAL: c_bc(lambda=1) = 1-3(2*1-1)^2 = 1-3 = -2. c_bg(lambda=1) = 2(6-6+1) = +2.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_betagamma\\b\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n --hidden -S '(bc|beta-gamma|betagamma).{0,80}(central charge|c\\s*=)| (central charge|c\\s*=).{0,80}(bc|beta-gamma|betagamma)' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_bc|c_\\{bc\\}|c_betagamma|c_\\{betagamma\\}|c_\\{\\\\beta\\\\gamma\\}|c_\\\\beta\\\\gamma' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2397:invariant that measures the bc ghost central charge, not the kappa
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1547:The ghost system ($bc$ at $c = -26$) is the physical implementation
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:363:The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:904:$\cA$ to $bc$-ghosts and requires $c = 26$ for $Q^2 = 0$
/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:194:\begin{theorem}[Arnold presentation {\cite{Arnold69}}; \texorpdfstring{$\bC \cong \bR^2$}{C = R2};
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:932:dual of the reparametrisation ghost $bc_2$ ($c = -26$) is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:3265:ghost $bc_2$ ($c = -26$) is the bosonic spin-$2$ system
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:363:The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex:904:$\cA$ to $bc$-ghosts and requires $c = 26$ for $Q^2 = 0$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_critical_string_dichotomy.tex:990:$\kappa_{bc} = -13$ at all central charges). Its vanishing
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:893:generic central charge, $\beta\gamma$ and $bc$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:647:ghost central charge of the bosonic string ($bc$-ghost system contributes
/Users/raeez/chiral-bar-cobar/chapters/examples/deformation_quantization_examples.tex:528:The symplectic fermion $\mathcal{SF}$ at $c = -2$ is the $bc$ system at $\lambda = 1$ (Section~\ref{sec:betagamma-koszul-dual}), with Koszul dual $\beta\gamma$ at $\lambda = 1$. The central charges $c(bc) = -2$ and $c(\beta\gamma) = 2$ follow from the Sugawara construction (or equivalently, from the conformal anomaly of the ghost number current); their sum $c + c' = 0$ is consistent with $bc$--$\beta\gamma$ complementarity.
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:906:For any central charge $c \in \bC$, the Virasoro vertex algebra
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:3984: central charge (Theorem~\ref{thm:betagamma-bc-koszul}),
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:713:\item \emph{Central charge non-cancellation.} Unlike the $\beta\gamma$/$bc$ pair (Proposition~\ref{prop:betagamma-bc-koszul-detailed}), the central charges satisfy $c(k) + c(-k-4) = 2\dim(\mathfrak{sl}_2) = 6$ rather than zero: curvature prevents cancellation.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_gravitational_s_duality.tex:1071:The central charge of $bc_\lambda$ is $c = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd.tex:2517:$bc$-pairs at heights $1$ and $2$). Central charge
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1728:which is the anticommutation relation for the $bc$ ghost system (two fermionic generators $b = \beta^*$, $c = \gamma^*$).
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:2903:The bar curvature $m_0$ is an element of the bar complex proportional to the central class: $m_0 = k \cdot c$ for $\cH_k$ (Theorem~\ref{thm:heisenberg-curved-structure}). Anomaly cancellation (Theorem~\ref{thm:anomaly-koszul}): $\barB^{\mathrm{ch}}(\cH^{26} \otimes bc)$ is uncurved because the total central charge $c_{\mathrm{eff}} = 26 \cdot 1 + (-26) = 0$ vanishes. This is an anomaly cancellation at the level of $c$, not~$\kappa$: the modular characteristic $\kappa(\cH_1) = 1$ differs from $c(\cH_1)/2 = 1/2$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_\\{betagamma\\}\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 1.00s:
/Users/raeez/chiral-bar-cobar/compute/lib/theorem_ainfty_nonformality_class_m_engine.py:445:    # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
/Users/raeez/chiral-bar-cobar/compute/lib/theorem_ainfty_nonformality_class_m_engine.py:453:        # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:411:                # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:418:                # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
/Users/raeez/chiral-bar-cobar/compute/lib/polyakov_effective_action.py:12:  - bc ghosts (bosonic string): c_bc = -26, kappa_bc = -13
/Users/raeez/chiral-bar-cobar/compute/lib/polyakov_effective_action.py:103:        c_bc = -26, c_{betagamma} = 11.
/Users/raeez/chiral-bar-cobar/compute/lib/factorization_homology_engine.py:257:        kappa = Fraction(1)  # AP137: c_bg(lambda=1) = +2, kappa = 1; was confused with c_bc = -2
/Users/raeez/chiral-bar-cobar/compute/lib/factorization_homology_engine.py:799:        c_val = Fraction(2)  # AP137: c_bg(lambda=1) = +2, kappa = 1; was confused with c_bc = -2
/Users/raeez/chiral-bar-cobar/compute/lib/factorization_homology_engine.py:800:        det_power = Fraction(1)  # AP137: c_bg(lambda=1) = +2, kappa = 1; was confused with c_bc = -2
/Users/raeez/chiral-bar-cobar/compute/lib/costello_bv_comparison_engine.py:1593:    c_bc = Rational(-26)
/Users/raeez/chiral-bar-cobar/compute/lib/costello_bv_comparison_engine.py:1594:    kappa_bc = c_bc / 2  # = -13
/Users/raeez/chiral-bar-cobar/compute/lib/costello_bv_comparison_engine.py:1601:    c_total = Rational(15) + c_bc + c_bg  # = 15 - 26 + 11 = 0
/Users/raeez/chiral-bar-cobar/compute/lib/costello_bv_comparison_engine.py:1608:        "c_bc": c_bc,
/Users/raeez/chiral-bar-cobar/compute/lib/theorem_si_li_bv_index_engine.py:214:    c_betagamma = 2(6*lam^2 - 6*lam + 1), kappa = c/2 = 6*lam^2 - 6*lam + 1.
/Users/raeez/chiral-bar-cobar/compute/lib/theorem_si_li_bv_index_engine.py:215:    AP137: sign was wrong (had -2 instead of +2, confusing c_bc with c_bg).
/Users/raeez/chiral-bar-cobar/compute/lib/theorem_si_li_bv_index_engine.py:239:      c_bc = 1-3(1)^2 = -2.  kappa = c/2 = -1 per pair.
/Users/raeez/chiral-bar-cobar/compute/lib/theorem_si_li_bv_index_engine.py:242:    Complementarity check: c_bg + c_bc = 2 + (-2) = 0.
/Users/raeez/chiral-bar-cobar/compute/lib/universal_shadow_tower_engine.py:185:def c_betagamma(lam: Union[int, Fraction]) -> Fraction:
/Users/raeez/chiral-bar-cobar/compute/lib/universal_shadow_tower_engine.py:186:    """c_{betagamma}(lambda) = 2(6*lambda^2 - 6*lambda + 1).
/Users/raeez/chiral-bar-cobar/compute/lib/universal_shadow_tower_engine.py:190:    Check: lambda=2 -> 2(24 - 12 + 1) = 26; c_bc(2) = 1 - 3*9 = -26; sum = 0.
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "c_betagamma"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/fukaya_shadow_tower.py:1754:            'c_betagamma_symplectic': cls.betagamma_c_at_weight(Fraction(1, 2)),
compute/tests/test_fukaya_shadow_tower.py:1120:        assert comp['c_betagamma_symplectic'] == comp['c_expected']
compute/tests/test_fukaya_shadow_tower.py:1122:        assert comp['c_betagamma_symplectic'] == Fraction(-1)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_\\\\beta\\\\gamma\"" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:c_\beta\gamma)
              ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"c_\\{betagamma\\}\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_\\{beta\\\\gamma\\}\"" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:c_\{beta\gamma\})
               ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "c_bc" chapters' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"c_\\\\beta\\\\gamma\"" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:c_\beta\gamma)
              ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"c_\\\\{\\\\\\\\beta\\\\\\\\gamma\\\\}\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/rosetta_stone.tex:922:$K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda)
working_notes.tex:7187:c_{\beta\gamma}(\mu)
working_notes.tex:7191:- 6\lambda + 1)$ and $\kappa(\beta\gamma) = c_{\beta\gamma}/2
working_notes.tex:7197:c_{bc}(\lambda) + c_{\beta\gamma}(\lambda) = 0,
working_notes.tex:7430:c_{\beta\gamma}(3/2) &= 2(6 \cdot 9/4 - 6 \cdot 3/2 + 1)
working_notes.tex:7451:c_{\mathrm{dual}} &= c_{\beta\gamma}(2) + c_{bc}(3/2)
working_notes.tex:7790:\item $bc_\lambda$: $K = c_{bc} + c_{\beta\gamma} = 0$
working_notes.tex:7792:\item $\beta\gamma_\mu$: $K = c_{\beta\gamma} + c_{bc} = 0$
chapters/connections/thqg_fm_calculus_extensions.tex:1259:$\kappa(\beta\gamma) = c_{\beta\gamma}/2$ introduces
chapters/connections/thqg_symplectic_polarization.tex:1851:& $c_{\beta\gamma}/2$ & C & $4$ & quartic & $\mathfrak{Q}_{\beta\gamma}$
chapters/connections/thqg_symplectic_polarization.tex:1918:$c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$ and
chapters/connections/thqg_symplectic_polarization.tex:1919:modular characteristic $\kappa(\beta\gamma) = c_{\beta\gamma}/2$
chapters/connections/bv_brst.tex:784:formula $c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)$ \[
chapters/connections/bv_brst.tex:785: c_{\beta\gamma}(\tfrac{3}{2})
chapters/connections/bv_brst.tex:792:hence $\kappa_{\beta\gamma} = c_{\beta\gamma}/2 = 11/2$, and the
chapters/connections/bv_brst.tex:2273: = 4 \cdot c_{\beta\gamma}(\lambda{=}1)
chapters/connections/bv_brst.tex:2275: using $c_{\beta\gamma}(1) = 2(6 - 6 + 1) = 2$;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '340,380p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\index{BRST operator|textbf}
The BRST operator $Q_{\mathrm{BRST}}$ arises from gauge fixing the BV action.
Choose a Lagrangian submanifold $\mathcal{L}$ of the total space of fields and
antifields:
\[
Q_{\mathrm{BRST}} = Q_{\mathrm{BV}}\big|_{\mathcal{L}}.
\]
In the chiral algebra context, the BRST charge decomposes by antighost number
(not ghost number):
\[
Q_{\mathrm{BRST}} = Q_0 + Q_1 + Q_2 + \cdots,
\]
where $Q_k$ has antighost number~$k$ and operator dimension~$k-1$.
The total BRST charge has definite ghost number~$+1$.
\end{definition}

\begin{theorem}[BRST cohomology = physical states; \ClaimStatusProvedElsewhere{} \cite{CG17}]
\label{thm:brst-physical-states}
The cohomology of $Q_{\text{BRST}}$ computes physical on-shell states:
\[H^*(Q_{\text{BRST}}) \cong \mathcal{A}_{\text{phys}}\]

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '720,780p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{proof}
By Theorem~D \textup{(}$\kappa$-additivity under tensor product of chirally
Koszul algebras, uniform-weight lane; see
Theorem~\ref{thm:explicit-theta}\textup{)},
$\kappa(\cA_{\mathrm{matter}}^! \otimes \widetilde{\cA}_{\mathrm{ghost}})
= \kappa(\cA_{\mathrm{matter}}^!) + \kappa(\widetilde{\cA}_{\mathrm{ghost}})$.
The free\slash Kac--Moody complementarity sum gives
$\kappa(\cA_{\mathrm{matter}}^!) = -\kappa(\cA_{\mathrm{matter}})$,
and the matching involution hypothesis gives
$\kappa(\widetilde{\cA}_{\mathrm{ghost}})
= -\kappa(\cA_{\mathrm{ghost}})$, hence the total is
$-\kappa_{\mathrm{tot}} = 0$. The genus-$0$ BRST cancellation then
follows from Corollary~\ref{cor:anomaly-physical-genus0} applied to
$\cA_{\mathrm{tot}}^{\vee}$.
\end{proof}

\begin{remark}[Scoping: why the ghost involution matters]
\label{rem:koszul-brst-scoping}
The hypothesis on $\widetilde{\cA}_{\mathrm{ghost}}$ is essential and
cannot be dropped. Consider the bosonic string:
thinking
**Summarizing formula occurrences and duplicates**

I'm gathering occurrences of the canonical formula `c_bc` and related functions across root Markdown and TeX files, focusing on actual formula definitions rather than generic mentions. I'll list key files with line numbers containing unique formula instances, acknowledge numerous duplicates mainly in audit and test logs, and clarify why including every duplicate wouldn't add value. This approach balances thoroughness with readability while answering the user's search request.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"c_bg\\(lambda\"" in /Users/raeez/chiral-bar-cobar succeeded in 65ms:
compute/lib/koszul_conductor_table_engine.py:25:  C6.  c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)
compute/lib/koszul_conductor_table_engine.py:26:  C7.  c_bc(lambda) + c_bg(lambda) = 0
compute/lib/koszul_conductor_table_engine.py:505:    """c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1).  (C6)
compute/lib/independent_conjectures.py:234:    # C7: c_bg(lambda) + c_bc(lambda) = 0 for all lambda.
compute/lib/cy_chiral_derham_k3_engine.py:31:  More precisely: locally, each beta-gamma pair gives c_bg(lambda = 1) = +2, so d pairs
compute/lib/cy_chiral_derham_k3_engine.py:555:        # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
compute/lib/betagamma_shadow_full.py:41:  c_bg(lambda) = +2(6*lambda^2 - 6*lambda + 1)
compute/lib/betagamma_genus2_cross_channel_engine.py:15:where kappa(lambda) = c_bg(lambda)/2 = 6*lambda^2 - 6*lambda + 1 and
compute/lib/betagamma_genus2_cross_channel_engine.py:83:    c_bg(lambda) = 2(6*lambda^2 - 6*lambda + 1)
compute/lib/betagamma_genus2_cross_channel_engine.py:84:    kappa(lambda) = c_bg(lambda)/2 = 6*lambda^2 - 6*lambda + 1
compute/lib/betagamma_genus2_cross_channel_engine.py:92:Symmetry: c_bg(lambda) = c_bg(1-lambda), kappa(lambda) = kappa(1-lambda).
compute/lib/betagamma_genus2_cross_channel_engine.py:95:Complementarity with bc: c_bg(lambda) + c_bc(lambda) = 0 (C7 census).
compute/lib/betagamma_genus2_cross_channel_engine.py:154:    c_bg(lambda) = 2(6*lambda^2 - 6*lambda + 1)
compute/lib/betagamma_genus2_cross_channel_engine.py:179:    kappa(lambda) = c_bg(lambda)/2 = 6*lambda^2 - 6*lambda + 1
compute/lib/shadow_l_function_engine.py:249:    # AP1/C6: c_bg(lambda) = 2(6*lambda^2 - 6*lambda + 1).
compute/lib/f2_kappa_verification_engine.py:78:    r"""kappa(betagamma_lambda) = c_bg(lambda)/2 = 6*lambda^2 - 6*lambda + 1.
compute/lib/f2_kappa_verification_engine.py:80:    c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1).  [C6: landscape_census.tex]
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"c = -1 \\+ 3\\(2\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/non_cy_local_surface_chiral.py:720:    or c = -1 + 3(2*0 - 1)^2 = -1 + 3 = 2 (as betagamma)
compute/lib/non_cy_local_surface_chiral.py:752:    c = -1 + 3(2*h_beta - 1)^2  (for betagamma/bosons)
compute/lib/three_d_n2_cy3_engine.py:504:    In this case c = -1 + 3(2*1/2 - 1)^2 = -1 + 0 = -1... no.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '760,820p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(}Remark~\textup{\ref{rem:ghost-superghost-koszul})}.
Without such a transport, matter Koszul duality alone does not
preserve the anomaly.
\end{remark}

\begin{computation}[Superstring ghost/superghost Koszul dual;
\ClaimStatusProvedHere]
\label{comp:superstring-ghost-koszul}
\index{superstring!ghost Koszul dual}
\index{$\beta\gamma$ system!superghost Koszul dual}
The bosonic string ghost system is the $bc$ pair at $\lambda = 2$
with $c_{bc} = 1 - 3(2{\cdot}2 - 1)^2 = -26$ and
$\kappa_{bc} = c_{bc}/2 = -13$. The complementarity relation
$\kappa + \kappa' = -26 \neq 13$ shows that the $bc$ system is
\emph{not} self-dual under the Virasoro self-duality locus
$c = 13$ \textup{(}Virasoro self-dual at
$\kappa + \kappa' = 13$\textup{)}: the $bc$ ghost is self-dual
under a different involution \textup{(}the one described in
Remark~\textup{\ref{rem:koszul-brst-scoping})} that fixes
the bilinear pairing but reverses the total $\kappa$.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"c = 2\\(6\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/non_cy_local_surface_chiral.py:520:    c = 2(6lambda^2 - 6lambda + 1) = -1 + 3(2lambda-1)^2
compute/tests/test_cross_volume_shadow_bridge.py:881:        """beta-gamma at lambda = 2: c = 2(6*4 - 12 + 1) = 2*13 = 26.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '1880,1945p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The genus-$1$ complementarity is the frame computation:
$Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$,
$Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda_1$.
At genus~$2$:
$\dim Q_2(\mathcal{H}_\kappa) + \dim Q_2(\mathcal{H}_\kappa^!)
= \dim H^*(\overline{\mathcal{M}}_2, Z(\mathcal{H}_\kappa))$,
verified computationally.

\emph{Affine $\widehat{\mathfrak{g}}_k$.}
PBW filterability holds by the PBW theorem for vertex algebras
at non-critical level $k \ne -h^{\vee}$
(Proposition~\ref{V1-prop:pbw-universality}).
The bar complex has finite-dimensional fiber cohomology
because $\widehat{\mathfrak{g}}_k$ is Koszul
(Corollary~\ref{V1-cor:universal-koszul}).
Both (H1) and (H2) hold.
The cubic shadow $\mathfrak{C}_{\mathrm{aff}}$ is nonzero
(Theorem~\ref{V1-thm:nms-affine-cubic-normal-form}), but the
quartic shadow vanishes in minimal gauge:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"c_\\{bg\\}\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:


thinking
**Summarizing canonical formula findings**

I'm gathering key formula lines related to canonical expressions found across multiple files, noting many duplicates that restate the same core formula. I’m verifying algebraic equivalences, like the one in `betagamma_shadow_full.py` where `c_bc(lambda) = -2(6*lambda^2 - 6*lambda + 1)` matches the canonical form despite the negation. I’m planning to organize the answer around these patterns and mention the `c_betagamma` references as well.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "c_betagamma"' in /Users/raeez/chiral-bar-cobar succeeded in 63ms:
compute/lib/theorem_kappa_en_invariance_engine.py:188:    Source: genus3_landscape.py c_betagamma, genus4_landscape.py kappa_betagamma.
compute/lib/boundary_voa_koszul_engine.py:277:def c_betagamma_system(n_pairs: int, weight: Num = Fraction(1, 2)) -> Fraction:
compute/lib/boundary_voa_koszul_engine.py:634:    c = c_betagamma_system(n_pairs, Fraction(1, 2))
compute/lib/boundary_voa_koszul_engine.py:700:    c_dual = c_betagamma_system(n_pairs, Fraction(1, 2))
compute/lib/boundary_voa_koszul_engine.py:1565:assert c_betagamma_system(1, Fraction(1, 2)) == Fraction(-1)
compute/lib/genus3_arithmetic_shadow_engine.py:192:def c_betagamma(lam: int) -> Fraction:
compute/lib/genus3_arithmetic_shadow_engine.py:311:    c_val = c_betagamma(lam)
compute/lib/dmod_counterexample_search_engine.py:1042:    # Betagamma central charge: c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)
compute/lib/independent_conjectures.py:244:def bc_betagamma_central_charge_sum(lam) -> object:
compute/lib/independent_conjectures.py:284:def bc_betagamma_koszul_check(lam: int = 1, max_degree: int = 5) -> Dict[str, object]:
compute/lib/independent_conjectures.py:639:def verify_bc_betagamma_duality() -> Dict[str, bool]:
compute/lib/independent_conjectures.py:645:        s = bc_betagamma_central_charge_sum(lam)
compute/lib/independent_conjectures.py:650:    s = bc_betagamma_central_charge_sum(lam)
compute/lib/independent_conjectures.py:664:    check = bc_betagamma_koszul_check(lam=1, max_degree=5)
compute/lib/independent_conjectures.py:697:    for name, ok in verify_bc_betagamma_duality().items():
compute/lib/independent_conjectures.py:701:    kc = bc_betagamma_koszul_check(lam=1, max_degree=7)
compute/lib/cy_chiral_derham_k3_engine.py:545:    c_betagamma: int = 0  # set in post_init
compute/lib/cy_chiral_derham_k3_engine.py:556:        self.c_betagamma = 2 * d
compute/lib/cy_chiral_derham_k3_engine.py:558:        self.c_total = self.c_betagamma + self.c_bc  # = 0
compute/lib/cy_chiral_derham_k3_engine.py:1606:        'c_betagamma': cdr.c_betagamma,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '900,940p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
instance of a universal pattern for all free-field chiral
algebras. The $bc$ ghost system of conformal weights
$(\lambda, 1-\lambda)$ and the $\beta\gamma$ system of the same
weights are Koszul dual to each other:
\[
bc_\lambda^! \;=\; \beta\gamma_\lambda,
\qquad
\beta\gamma_\lambda^! \;=\; bc_\lambda.
\]
The mechanism is the chiral incarnation of classical
$\mathrm{Ext}/\mathrm{Sym}$ duality: $bc_\lambda$ is the
chiral exterior algebra $\bigwedge^{\mathrm{ch}}(V)$ on
$V = \bC b \oplus \bC c$ (fermionic), and its Koszul dual is the
chiral symmetric algebra $\mathrm{Sym}^{\mathrm{ch}}(V^*)$
(bosonic), which is precisely the $\beta\gamma$ system. The bar
complex has $m_2$ only (simple-pole OPE), confirming that both
systems are Koszul. Koszul duality exchanges statistics while
preserving conformal weights; it does \emph{not} exchange spins
$\lambda \mapsto 1 - \lambda$ (that is a relabelling, not a
dualisation).



thinking
**Inspecting potential issues**

I'm noticing there might be an issue with the formula in vol2 compute ds_brst_sc_engine, specifically -2(6d² - 6d + 1). It seems like the user might be looking at all volumes, not just specific chapters, so I need to verify every occurrence of c_bc or c_betagamma. That could be quite a few! Instead of being exhaustive, perhaps I can focus only on the problematic occurrences. I should consider using a scripted audit to help with this search across all relevant volumes.
thinking
**Identifying potential issues**

I've spotted a potential issue in `free_fields.tex`, specifically at lines 756-757 where beta-gamma is discussed alongside c_{bc}. I need to verify if this is within the appropriate context. There’s also a mention in `higher_genus_foundations.tex` that raises questions about c_bg being an alias for c_betagamma, which could complicate things. I should consider searching for c_bg formulas too. To conduct a manageable audit, perhaps I could use a script to classify formulas using regex, although I should stick to shell commands like grep and sed for this task.
thinking
**Listing files for inspection**

I think using `rg -l` is a good approach to list all files with the target notations. This way, I can identify and focus on the relevant contexts. It seems like I might need to search across all volumes, so using `rg -l` with exact patterns could help narrow things down effectively. Let’s proceed with getting that file list to ensure I’m covering everything I need to inspect!
thinking
**Analyzing canonical formula references**

I'm comparing formulas for c_bc in different files, checking whether the compute file’s formula matches the canonical one in AP137 notation by relating parameters d and λ, and planning to verify this by reviewing the compute file snippet around lines 450-560.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"1-3\\(2\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '450,560p' compute/lib/ds_brst_sc_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
            'ghost': '- (bc pair contributes -2)',
        },
        'mechanism': (
            'The quartic pole of the Virasoro OPE is manufactured from three sources: '
            '(1) the Sugawara construction, which generates quartic poles via both '
            'naive Wick contractions (Cartan) and cascading contractions (roots); '
            '(2) the ∂J^h improvement, whose NEGATIVE quartic pole overwhelms the '
            'Sugawara for large k; (3) the ghost system. The improvement sign arises '
            'from ∂_z∂_w[1/(z-w)²] = -6/(z-w)⁴ (the double derivative of the '
            'propagator is negative).'
        ),
    }


# =========================================================================
# 3b. GENERAL sl_N QUARTIC POLE AND DS CENTRAL CHARGE
# =========================================================================

def ds_central_charge_slN(N_val, k_val):
    r"""DS central charge for the principal W-algebra W_k(sl_N).
codex
I have the first pass classified: most hits are consistent, but there are a few likely swap surfaces and one compute-side formula in Vol II that needs context. I’m now reading only the candidate files around those lines so I can separate genuine errors from equivalent rewrites like `-2(6λ²-6λ+1)=1-3(2λ-1)^2`.
collab wait(call_FzBEFvb2pcveuEb7wSnwEKzs)
  receivers: 019d87d0-ffa3-70b0-a3b6-89f43fb1c8a6, 019d87d0-ff9f-7621-acbc-8d70c3f4a6e0, 019d87d0-ffbd-7bf3-b20e-44cc2ea632c0
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"1 - 3\\(2\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md:671:c_bc(lambda) = 1 - 3(2*lambda-1)^2
compute/lib/non_cy_local_surface_chiral.py:490:        c = 1 - 3(2n+1-1)^2 / (2n+1-1)  ... no, this is the wrong formula.
compute/lib/non_cy_local_surface_chiral.py:510:    c = 2 for the (1, 0) system: c = 1 - 3(2*1 - 1)^2 = 1 - 3 = -2?
compute/lib/non_cy_local_surface_chiral.py:513:    c = -2(6lambda^2 - 6lambda + 1) = 1 - 3(2lambda - 1)^2
compute/lib/non_cy_local_surface_chiral.py:719:    c = 1 - 3(2*0 - 1)^2 = 1 - 3 = -2 (as a bc system)
compute/lib/non_cy_local_surface_chiral.py:751:    c = 1 - 3(2*h_beta - 1)^2  (for bc/fermions)

thinking
**Organizing key formula references**

I'm putting together a clear summary highlighting main unique occurrences of canonical and variant formulas for central charges like c_bc and c_betagamma across key files such as AGENTS.md, CLAUDE.md, standalone theorems, and several compute/lib scripts. I plan to note exact line references with verification of formula equality, especially where expressions match the canonical forms despite notation differences, providing the user a manageable, insightful overview.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '140,190p' compute/lib/entanglement_entropy_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
      N=2: H_2-1 = 1/2, so kappa(W_2) = c/2 = kappa(Vir).  Correct.
      N=3: H_3-1 = 5/6, so kappa(W_3) = 5c/6.
    """
    h_n_minus_1 = harmonic_number(n) - 1
    return Fraction(c) * h_n_minus_1


def c_betagamma(lam: Any) -> Fraction:
    r"""c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1).  [C6]

    Checks: lambda=1/2 -> -1; lambda=2 -> 26.
    """
    lam = Fraction(lam)
    return 2 * (6 * lam**2 - 6 * lam + 1)


def c_bc(lam: Any) -> Fraction:
    r"""c_bc(lambda) = 1 - 3*(2*lambda - 1)^2.  [C5]

    Checks: lambda=1/2 -> 1; lambda=2 -> -26.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"= 1-3\\(2\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba AGENTS.md | sed -n '160,190p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   160	# Kappa (C1-C4)
   161	kappa(H_k) = k                                       # Heisenberg; k=0→0, k=1→1
   162	kappa(Vir_c) = c/2                                    # Virasoro ONLY; c=0→0, c=13→13/2
   163	kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)                 # Affine KM; k=0→dim(g)/2 (NOT 0), k=-h^v→0
   164	kappa(W_N) = c*(H_N - 1), H_N = sum_{j=1}^N 1/j      # W_N; N=2: H_2-1=1/2 so kappa=c/2=Vir
   165	
   166	# r-matrix (C9-C11) — level prefix k MANDATORY (AP126, THE MOST VIOLATED AP)
   167	r^KM(z) = k*Omega/z           [trace-form]            # k=0→0; k=-h^v→finite
   168	r^KM(z) = Omega/((k+h^v)*z)   [KZ]                    # k=0→Omega/(h^v*z)!=0; k=-h^v→diverges
   169	r^Heis(z) = k/z                                       # k=0→0
   170	r^Vir(z) = (c/2)/z^3 + 2T/z                           # cubic+simple, NOT quartic. d-log absorbs one
   171	
   172	# Bridge: k*Omega_tr = Omega/(k+h^v) at generic k
   173	# Averaging (C13): av(r(z)) = kappa for abelian; av(r(z)) + dim(g)/2 = kappa for non-abelian KM
   174	
   175	# Central charges (C5-C7)
   176	c_bc(lambda) = 1 - 3(2*lambda-1)^2                    # fermionic; lambda=1/2→1, lambda=2→-26
   177	c_bg(lambda) = 2(6*lambda^2-6*lambda+1)               # bosonic; lambda=1/2→-1, lambda=2→+26
   178	c_bc + c_bg = 0                                        # pointwise; verify at lambda=1: 2+(-2)=0
   179	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/bv_brst.tex | sed -n '350,380p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   350	Q_{\mathrm{BRST}} = Q_0 + Q_1 + Q_2 + \cdots,
   351	\]
   352	where $Q_k$ has antighost number~$k$ and operator dimension~$k-1$.
   353	The total BRST charge has definite ghost number~$+1$.
   354	\end{definition}
   355	
   356	\begin{theorem}[BRST cohomology = physical states; \ClaimStatusProvedElsewhere{} \cite{CG17}]
   357	\label{thm:brst-physical-states}
   358	The cohomology of $Q_{\text{BRST}}$ computes physical on-shell states:
   359	\[H^*(Q_{\text{BRST}}) \cong \mathcal{A}_{\text{phys}}\]
   360	\end{theorem}
   361	
   362	\begin{example}[Free \texorpdfstring{$bc$}{bc} ghost system]
   363	The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.
   364	
   365	For the bosonic string, $\lambda = 2$ (so $b$ has weight~$2$ and $c$ has weight~$-1$), giving $c_{\text{ghost}} = 1 - 3(3)^2 = -26$ and ghost stress tensor $T_{\text{ghost}} = -2b\,\partial c - (\partial b)\,c$.
   366	
   367	On the relative complex $\ker(b_0) \cap \ker(L_0^{\mathrm{tot}})$,
   368	the BRST nilpotence condition is:
   369	\[
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba CLAUDE.md | sed -n '220,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   220	
   221	**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).
   222	
   223	**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
   224	
   225	**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).
   226	
   227	**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.
   228	
   229	**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).
   230	
   231	**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).
   232	
   233	**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
   234	
   235	**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).
   236	
   237	**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
   238	
   239	**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"c=1 - 3\\(\"" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/bv_brst.tex | sed -n '730,810p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   730	= -\kappa(\cA_{\mathrm{ghost}})$, hence the total is
   731	$-\kappa_{\mathrm{tot}} = 0$. The genus-$0$ BRST cancellation then
   732	follows from Corollary~\ref{cor:anomaly-physical-genus0} applied to
   733	$\cA_{\mathrm{tot}}^{\vee}$.
   734	\end{proof}
   735	
   736	\begin{remark}[Scoping: why the ghost involution matters]
   737	\label{rem:koszul-brst-scoping}
   738	The hypothesis on $\widetilde{\cA}_{\mathrm{ghost}}$ is essential and
   739	cannot be dropped. Consider the bosonic string:
   740	$\kappa(\cA_{\mathrm{matter}}) = 13$ ($26$ free scalars: each scalar
   741	contributes $\kappa = 1/2$, so the total is $13$);
   742	$\kappa(\cA_{\mathrm{ghost}}) = -13$ ($bc$ system at $\lambda = 2$,
   743	$c_{bc} = 1 - 3(2{\cdot}2{-}1)^2 = -26$, $\kappa_{bc} = c_{bc}/2 = -13$);
   744	total $\kappa_{\mathrm{tot}} = 13 + (-13) = 0$.
   745	Applying Koszul duality to the matter sector alone sends
   746	$\kappa(\cA_{\mathrm{matter}}) \mapsto -13$
   747	\textup{(}complementarity for the free\slash Heisenberg family,
   748	$\kappa(\mathcal{H}_\kappa) + \kappa(\mathcal{H}_\kappa^!) = 0$;
   749	this is the free branch of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '1880,1945p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba standalone/five_theorems_modular_koszul.tex | sed -n '2170,2210p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1880	
  1881	The genus-$1$ complementarity is the frame computation:
  1882	$Q_1(\mathcal{H}_\kappa) = \mathbb{C} \cdot \kappa$,
  1883	$Q_1(\mathcal{H}_\kappa^!) = \mathbb{C} \cdot \lambda_1$.
  1884	At genus~$2$:
  1885	$\dim Q_2(\mathcal{H}_\kappa) + \dim Q_2(\mathcal{H}_\kappa^!)
  1886	= \dim H^*(\overline{\mathcal{M}}_2, Z(\mathcal{H}_\kappa))$,
  1887	verified computationally.
  1888	
  1889	\emph{Affine $\widehat{\mathfrak{g}}_k$.}
  1890	PBW filterability holds by the PBW theorem for vertex algebras
  1891	at non-critical level $k \ne -h^{\vee}$
  1892	(Proposition~\ref{V1-prop:pbw-universality}).
  1893	The bar complex has finite-dimensional fiber cohomology
  1894	because $\widehat{\mathfrak{g}}_k$ is Koszul
  1895	(Corollary~\ref{V1-cor:universal-koszul}).
  1896	Both (H1) and (H2) hold.
  1897	The cubic shadow $\mathfrak{C}_{\mathrm{aff}}$ is nonzero
  1898	(Theorem~\ref{V1-thm:nms-affine-cubic-normal-form}), but the
  1899	quartic shadow vanishes in minimal gauge:
 succeeded in 51ms:
  2170	 & $\beta\gamma$ \\
  2171	M & $\neq 0$ & $\neq 0$ & $\neq 0$
  2172	 & Virasoro, $\cW_N$, Bershadsky--Polyakov \\
  2173	\bottomrule
  2174	\end{tabular}
  2175	\end{center}
  2176	
  2177	\subsection{Free-field central charges}
  2178	
  2179	The free-field families provide essential boundary data.
  2180	
  2181	\emph{Fermionic $bc$ ghosts} (conformal weights $\lambda$
  2182	and $1 - \lambda$):
  2183	\begin{equation}\label{eq:cbc}
  2184	% C5: c_bc(lambda) = 1 - 3(2*lambda-1)^2; lambda=1/2 -> 1; lambda=2 -> -26
  2185	c_{bc}(\lambda) \;=\; 1 - 3(2\lambda - 1)^2.
  2186	\end{equation}
  2187	At $\lambda = 1/2$: $c_{bc} = 1$ (a single Dirac fermion).
  2188	At $\lambda = 2$: $c_{bc} = -26$ (the reparametrization ghosts
  2189	of the bosonic string).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/examples/rosetta_stone.tex | sed -n '900,950p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   900	instance of a universal pattern for all free-field chiral
   901	algebras. The $bc$ ghost system of conformal weights
   902	$(\lambda, 1-\lambda)$ and the $\beta\gamma$ system of the same
   903	weights are Koszul dual to each other:
   904	\[
   905	bc_\lambda^! \;=\; \beta\gamma_\lambda,
   906	\qquad
   907	\beta\gamma_\lambda^! \;=\; bc_\lambda.
   908	\]
   909	The mechanism is the chiral incarnation of classical
   910	$\mathrm{Ext}/\mathrm{Sym}$ duality: $bc_\lambda$ is the
   911	chiral exterior algebra $\bigwedge^{\mathrm{ch}}(V)$ on
   912	$V = \bC b \oplus \bC c$ (fermionic), and its Koszul dual is the
   913	chiral symmetric algebra $\mathrm{Sym}^{\mathrm{ch}}(V^*)$
   914	(bosonic), which is precisely the $\beta\gamma$ system. The bar
   915	complex has $m_2$ only (simple-pole OPE), confirming that both
   916	systems are Koszul. Koszul duality exchanges statistics while
   917	preserving conformal weights; it does \emph{not} exchange spins
   918	$\lambda \mapsto 1 - \lambda$ (that is a relabelling, not a
   919	dualisation).
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '470,530p' compute/lib/non_cy_local_surface_chiral.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
For each mode n of the fiber coordinate y_a^n:
    field of "spin" or bundle degree: n*a  (section of O(na))
    ghost from d/dy_a at level n: section of O(na - a) = O((n-1)a)

The one-loop determinant is:

    Z_1 = prod_{n >= 0} [det(d-bar on O(na))]^{+1}  [bosonic: y_a^n]
        * prod_{n >= 0} [det(d-bar on O(na-a))]^{-1} [fermionic: y_a^n d/dy_a]
        * (same for b)
        * [det(d-bar on T_{P^1})]^{...}  [base contribution]

This product requires zeta-function regularization.

Instead of computing the full partition function, we extract kappa
from the ANOMALY of the regularized product:

    kappa(A_{a,b}) = (1/2) * [sum of effective central charges of all modes]

For the BETAGAMMA SYSTEM associated to a single line bundle O(n) on P^1:
    The betagamma system on P^1 of type O(n) has:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/betagamma_shadow_full.py | sed -n '30,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    30	CHARGED STRATUM (mixing T and weight-changing directions), and the
    31	quintic obstruction o_5 vanishes by stratum separation.
    32	
    33	CRITICAL DISTINCTION (AP19): The r-matrix has pole orders ONE LESS than
    34	the OPE. The beta-gamma OPE has a simple pole, so the r-matrix has NO
    35	pole: r(z) = constant. The nontrivial shadow structure comes from the
    36	STRESS TENSOR subalgebra (which has poles up to z^{-4} in the OPE,
    37	giving poles up to z^{-3} in the r-matrix).
    38	
    39	COMPLEMENTARITY (Theorem C):
    40	  (beta-gamma)^! = bc ghost system (statistics exchange, NOT weight exchange!)
    41	  c_bg(lambda) = +2(6*lambda^2 - 6*lambda + 1)
    42	  c_bc(lambda) = -2(6*lambda^2 - 6*lambda + 1)
    43	  kappa(bg) + kappa(bc) = 0  (exact complementarity, AP24 safe)
    44	
    45	NOTE ON KOSZUL DUALITY vs WEIGHT SYMMETRY:
    46	  The formula kappa = 6*lambda^2 - 6*lambda + 1 is symmetric under
    47	  lambda -> 1-lambda: kappa(lambda) = kappa(1-lambda). This is because
    48	  beta at weight lambda and gamma at weight 1-lambda produce the SAME
    49	  stress tensor (up to sign). But this is weight symmetry, NOT Koszul
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba compute/lib/ds_brst_sc_engine.py | sed -n '500,560p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   500	
   501	
   502	def ds_quartic_pole_slN(N_val, k_val):
   503	    r"""First-principles quartic pole decomposition for sl_N DS reduction.
   504	
   505	    Generalizes the sl₂ computation to all sl_N.
   506	
   507	    Parameters:
   508	        N_val: rank+1 (N ≥ 2)
   509	        k_val: level
   510	
   511	    Returns:
   512	        dict with complete decomposition
   513	    """
   514	    N = S(N_val)
   515	    k = S(k_val)
   516	    p = k + N  # k + h∨
   517	
   518	    # Sugawara: c_Sug/2
   519	    c_sug = k * (N ** 2 - 1) / p
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba compute/lib/entanglement_shadow_spectrum_engine.py | sed -n '120,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   120	    if lie_algebra not in LIE_ALGEBRA_DATA:
   121	        raise ValueError(f"unsupported Lie algebra: {lie_algebra}")
   122	    constants = LIE_ALGEBRA_DATA[lie_algebra]
   123	    return {
   124	        "dim": Fraction(constants["dim"]),
   125	        "h_dual": Fraction(constants["h_dual"]),
   126	    }
   127	
   128	
   129	def w_algebra_central_charge(c: Any) -> Fraction:
   130	    """Return the supplied principal W_N central charge parameter."""
   131	    return _as_fraction(c)
   132	
   133	
   134	def w_algebra_kappa(N: int, c: Any) -> Fraction:
   135	    """Return kappa(W_N) = c * (H_N - 1)."""
   136	    if N < 2:
   137	        raise ValueError("W_N requires N >= 2")
   138	    return _as_fraction(c) * (harmonic_number(N) - 1)
   139	
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba AGENTS.md | sed -n '660,680p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   660	
   661	```text
   662	kappa(H_k) = k
   663	kappa(Vir_c) = c/2
   664	kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)
   665	kappa(W_N) = c*(H_N - 1),  H_N = sum_{j=1}^N 1/j
   666	
   667	r^KM(z) = k*Omega/z
   668	r^Heis(z) = k/z
   669	r^Vir(z) = (c/2)/z^3 + 2T/z
   670	
   671	c_bc(lambda) = 1 - 3(2*lambda-1)^2
   672	c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)
   673	c_bc + c_bg = 0
   674	
   675	B(A) = T^c(s^{-1} A-bar),   A-bar = ker(epsilon)
   676	|s^{-1}v| = |v| - 1
   677	d_bar^2 = 0
   678	MC: d*Theta + (1/2)[Theta,Theta] = 0
   679	QME: hbar*Delta*S + (1/2){S,S} = 0
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba compute/lib/non_cy_local_surface_chiral.py | sed -n '480,540p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   480	
   481	This product requires zeta-function regularization.
   482	
   483	Instead of computing the full partition function, we extract kappa
   484	from the ANOMALY of the regularized product:
   485	
   486	    kappa(A_{a,b}) = (1/2) * [sum of effective central charges of all modes]
   487	
   488	For the BETAGAMMA SYSTEM associated to a single line bundle O(n) on P^1:
   489	    The betagamma system on P^1 of type O(n) has:
   490	        c = 1 - 3(2n+1-1)^2 / (2n+1-1)  ... no, this is the wrong formula.
   491	
   492	Let me use the concrete approach.
   493	
   494	CONCRETE COMPUTATION FOR KNOWN CASES
   495	======================================
   496	
   497	Case O(-1)+O(-1): the resolved conifold.
   498	
   499	The chiral algebra is the betagamma system: beta in O(-1), gamma in O(-1).

thinking
**Summarizing formula search results**

I’m gathering key hits for the user’s query about canonical formulas, including paths and line numbers for main occurrences like `AGENTS.md`, `compute/lib/entanglement_shadow`, and others, plus notes on canonical equivalences and variants. I’ll organize the info in a clear bullet list and note the abundance of similar duplicates mainly in audit and test files. This way, the user gets a concise but complete picture highlighting main formula references without overwhelming details.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba compute/lib/non_cy_local_surface_chiral.py | sed -n '700,770p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   700	    O(0)+O(-2) give CY3, but different geometries.
   701	
   702	For the resolved conifold O(-1)+O(-1):
   703	    The betagamma system: beta in O(-1), gamma in O(-1).
   704	    The pairing beta * gamma pairs via the CY form, valued in O(-2) = K.
   705	    This gives conformal weights (1, 0) for (beta, gamma).
   706	    c = 2, kappa = 1.
   707	
   708	For O(0)+O(-2):
   709	    phi_1 in O(0) = trivial, phi_2 in O(-2) = K_{P^1}.
   710	    The pairing phi_1 * phi_2 is in O(-2) = K. Good, still CY.
   711	    phi_1 has weight 0 (trivial bundle), phi_2 has weight 2 (from K).
   712	    ... Actually the conformal weights depend on the TWIST.
   713	    In the B-model twist: h(phi_1) = 0 (trivial), h(phi_2) = 2.
   714	    But h_1 + h_2 should equal 1 for a standard betagamma pair.
   715	    0 + 2 = 2 != 1.
   716	
   717	    This means O(0)+O(-2) does NOT give a standard betagamma system.
   718	    It gives a bc or betagamma system with anomalous weights.
   719	    c = 1 - 3(2*0 - 1)^2 = 1 - 3 = -2 (as a bc system)
codex
Found lots of hits (hundreds) once you include the audit/test logs, but the actual formula statements that define the bc/bg central charges all look like the canonical expressions; the most concise occurrences are below, and every repeated reference I checked (CLAUDE/AGENTS/engine docstrings/graphed tests) quotes the same polynomials or algebraically equivalent forms.

- `AGENTS.md:176-178` — `c_bc(lambda) = 1 - 3(2*lambda-1)^2` and `c_bg(lambda) = 2(6*lambda^2-6*lambda+1)` with the pointwise complementarity remark. Both match the canonical bc/bg formulas verbatim.  
- `CLAUDE.md:229-233` — the “C5/C6/C7” census entries lay out `c_bc(lambda) = 1 - 3(2*lambda-1)^2`, `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`, and `c_betagamma + c_bc = 0`; all three align exactly with the canonical definitions.  
- `standalone/five_theorems_modular_koszul.tex:2184-2203` — the free-field central-charge subsection states `c_{bc}(\lambda) = 1 - 3(2\lambda - 1)^2`, `c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)` and the complementarity equation; these are the same formulas written in LaTeX.  
- `compute/lib/entanglement_shadow_spectrum_engine.py:141-160` — the helper functions `bc_central_charge` and `betagamma_central_charge` document and return `c_bc(lambda) = 1 - 3*(2*lambda - 1)^2` and `c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)` respectively; the docstrings explicitly cite the C5/C6 census references.  
- `compute/lib/betagamma_shadow_full.py:39-43` — the complementarity summary writes `c_bg(lambda) = +2(6*lambda^2 - 6*lambda + 1)` and `c_bc(lambda) = -2(6*lambda^2 - 6*lambda + 1)`; the second line equals the canonical bc formula once you expand `1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)` so it’s algebraically equivalent.

Every other “hit” (audit notes, compute/test comments, and repeated checks) quotes or derives one of those same polynomials, so nothing deviates from the canonical expressions required by AP137.
wait(call_FzBEFvb2pcveuEb7wSnwEKzs) 1 agents complete:
  019d87d0-ffa3-70b0-a3b6-89f43fb1c8a6 completed: "Found lots of hits (hundreds) once you include the audit/test logs, but the actual formula statements that define the bc…"
exec
/bin/zsh -lc "rg -l --hidden -S 'c_bc|c_\\{bc\\}|c_betagamma|c_\\{betagamma\\}|c_\\{\\\\beta\\\\gamma\\}|c_\\\\beta\\\\gamma' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba compute/lib/three_d_n2_cy3_engine.py | sed -n '480,520p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   480	
   481	
   482	def ht_algebra_C3() -> HTChiralAlgebra:
   483	    r"""A^{HT}(T[C^3]) = beta-gamma system.
   484	
   485	    The HT twist of the free 3d N=2 chiral multiplet gives the
   486	    beta-gamma (bc) system with one pair of conjugate fields:
   487	      beta: conformal weight 1 (holomorphic 1-form component)
   488	      gamma: conformal weight 0 (scalar component)
   489	
   490	    OPE: beta(z) gamma(w) ~ 1/(z-w)
   491	
   492	    Central charge: c = 2 (one beta + one gamma).
   493	    Wait -- for beta-gamma with beta weight h and gamma weight 1-h:
   494	      c(beta-gamma) = -1 + 3(2h-1)^2 = -1 + 3(2*1-1)^2 = -1 + 3 = 2
   495	    Hmm, that formula is for bc ghosts. For the standard beta-gamma:
   496	      c(beta-gamma at h_beta=1, h_gamma=0) = 2.
   497	
   498	    Actually: c(beta-gamma) depends on the conformal weights.
   499	    For the STANDARD beta-gamma (beta of weight 1, gamma of weight 0):
 succeeded in 353ms:
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_cy_exchange_proof_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_independent_conjectures.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_genus4_landscape.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_genus3_landscape.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_factorization_homology_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_entanglement_shadow_spectrum_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_rectification_kappa_cross_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_physics_horizon.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_shadow_depth_cross_verification.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_genus3_arithmetic_shadow_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_literature_cross_check.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_f1_landscape.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_kappa_cross_family.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_discriminant_atlas.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_quantum_group_shadow.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_kontsevich_graph_complex.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_costello_2loop_qcd_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_extended_ferm_ghost.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_alpha_n_conductor_engine.py
/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_thm_c_cy_rectification_engine.py
codex
**Central Charges**
- `chapters/connections/bv_brst.tex:363` – “central charge \(c_{bc} = 1 - 3(2\lambda - 1)^2\)” appears inside the free \(bc\) ghost example. This is the canonical \(c_{bc}(\lambda)\) listed in AP137.  
- `chapters/connections/bv_brst.tex:743-785` – the bosonic string discussion reiterates \(c_{bc} = 1 - 3(2\cdot2 - 1)^2 = -26\) and shortly after defines \(c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)\) (with the \(\lambda = 3/2\) evaluation). Both formulas match the canonical AP137 prescriptions for \(bc\) and \(\beta\gamma\) central charge families.  
- `chapters/connections/thqg_symplectic_polarization.tex:1916-1920` – the \(\beta\gamma\) family is again stated as “\(c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)\)” with \(\kappa = c/2\), exactly the canonical form for \(c_{bg}\).  
- `chapters/examples/rosetta_stone.tex:921-924` – complementarity is written as \(K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda) = -2(6\lambda^2 - 6\lambda + 1) + 2(6\lambda^2 - 6\lambda + 1) = 0\). Both summands are the standard formulas above, so the vanishing is a direct consequence of the AP137 expressions.  
- `compute/lib/ds_brst_sc_engine.py:530-537` – “Each pair at grade \(d\) has \(c_{bc} = -2(6d^2 - 6d + 1)\)” appears in the DS ghost decomposition. Recognizing \(-2(6d^2 - 6d + 1) = 1 - 3(2d - 1)^2\), this is the canonical \(c_{bc}(\lambda)\) (with \(\lambda\) renamed \(d\)), so the implementation matches the AP137 formula.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba compute/tests/test_cross_volume_shadow_bridge.py | sed -n '860,910p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   860	        assert dim_g == 14
   861	        # VERIFIED [DC] structural property [CF] AP10
   862	        assert hv == 4
   863	
   864	
   865	# ==========================================================================
   866	# SECTION 14: MULTI-FAMILY KAPPA CONSISTENCY
   867	# ==========================================================================
   868	
   869	class TestKappaMultiFamily:
   870	    """Cross-family consistency checks (AP10: hardcoded wrong values detected
   871	    by cross-family relations, not by single-family tests)."""
   872	
   873	    def test_heisenberg_is_rank1_lattice(self):
   874	        """Heisenberg at level k = rank-1 lattice VOA kappa.
   875	        Actually: kappa(H_k) = k, kappa(lattice_rank) = rank.
   876	        At k = r: these should match."""
   877	        for r in [1, 2, 5]:
   878	            assert kappa_heisenberg(r) == kappa_lattice(r)
   879	


thinking
**Considering explorer returns**

I noticed that only one explorer returned. I’m wondering if the other two might have timed out or if there's a reason for this status. It might be worth waiting again to see if they come back. I feel like it's really important to keep track of everything and not miss any opportunities just because I wasn't patient enough. Waiting a little longer could be the key!
thinking
**Evaluating audit needs**

I’m considering that we really need an actual audit and possibly some edits. The first explorer claims that there are none in Volume I definitions, but I’m thinking there could be subtle inaccuracies in the file where the beta-gamma section refers to c_bc. It seems we’ll need a direct inspection. Plus, not every occurrence may have the correct formula definitions. I guess we should wait for input from the other explorers before moving forward.
codex
Vol I’s main formula surfaces look consistent so far. I’m waiting on the Volume II and III scans, then I’ll inspect the two suspicious spots already visible: a Vol II DS/BRST compute formula and a few inherited prose lines that use the wrong symbol inside a beta-gamma sentence.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"-1 \\+ 3\\(2\"" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: unrecognized flag -1
collab wait(call_20XSVCY5UNZF6hXVqa3CzxSz)
  receivers: 019d87d0-ff9f-7621-acbc-8d70c3f4a6e0, 019d87d0-ffbd-7bf3-b20e-44cc2ea632c0
wait(call_20XSVCY5UNZF6hXVqa3CzxSz) 1 agents complete:
  019d87d0-ff9f-7621-acbc-8d70c3f4a6e0 completed: "**Central Charges**
- `chapters/connections/bv_brst.tex:363` – “central charge \(c_{bc} = 1 - 3(2\lambda - 1)^2\)” appea…"
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"\\\\-1 \\+ 3\\(2\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/non_cy_local_surface_chiral.py:520:    c = 2(6lambda^2 - 6lambda + 1) = -1 + 3(2lambda-1)^2
compute/lib/non_cy_local_surface_chiral.py:720:    or c = -1 + 3(2*0 - 1)^2 = -1 + 3 = 2 (as betagamma)
compute/lib/non_cy_local_surface_chiral.py:752:    c = -1 + 3(2*h_beta - 1)^2  (for betagamma/bosons)
compute/lib/three_d_n2_cy3_engine.py:494:      c(beta-gamma) = -1 + 3(2h-1)^2 = -1 + 3(2*1-1)^2 = -1 + 3 = 2
compute/lib/three_d_n2_cy3_engine.py:504:    In this case c = -1 + 3(2*1/2 - 1)^2 = -1 + 0 = -1... no.
collab wait(call_Mxam6QncjOnToRUUlXk2amvA)
  receivers: 019d87d0-ffbd-7bf3-b20e-44cc2ea632c0
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "6lambda"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/non_cy_local_surface_chiral.py:506:    c = -2(6lambda^2 - 6lambda + 1)
compute/lib/non_cy_local_surface_chiral.py:513:    c = -2(6lambda^2 - 6lambda + 1) = 1 - 3(2lambda - 1)^2
compute/lib/non_cy_local_surface_chiral.py:520:    c = 2(6lambda^2 - 6lambda + 1) = -1 + 3(2lambda-1)^2
wait(call_Mxam6QncjOnToRUUlXk2amvA) timed out:
exec
/bin/zsh -lc "rg -n --hidden -S 'beta\\\\gamma.*c_\\{bc\\}|c_\\{bc\\}.*beta\\\\gamma|\\\\beta\\\\gamma.*c_bc|c_bc.*\\\\beta\\\\gamma' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/standalone /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'bc.*c_\\{\\\\beta\\\\gamma\\}|c_\\{\\\\beta\\\\gamma\\}.*bc|bc.*c_betagamma|c_betagamma.*bc' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/standalone /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177:contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:922:$K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda)
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:637:c_{\beta\gamma} + c_{bc} = 0.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:642:The central charge of the $\beta\gamma$ system is computed from the stress tensor (Theorem~\ref{thm:beta-gamma-stress}). Replacing bosonic statistics by fermionic statistics negates the Virasoro central term: the commutator $[L_m, L_n]$ picks up a sign from the fermion loop, so $c_{bc} = -c_{\beta\gamma}$.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1235:$c_{bc} = -c_{\beta\gamma}$
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1777:exponents cancel because $c_{\beta\gamma} + c_{bc} = 0$.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1808:charge is $c_{bc}(\lambda) = -c_{\beta\gamma}(\lambda)$
/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:504:$c_{\beta\gamma} + c_{bc} = 0$; verify at $\lambda = 1$:
/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:505:$c_{\beta\gamma} = 2$, $c_{bc} = -2$.)
/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:922:By complementarity $c_{\beta\gamma} + c_{bc} = 0$:
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:756:$\beta\gamma$: a T-line (Virasoro subalgebra at $c_{bc}$, with
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:808: \qquad c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) \;=\; 0
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2434:$\lambda$ & System & $c_{bc}$ & $\kappa(bc)$ & $\kappa(\beta\gamma)$ \\
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4534:$c_{bc}(\lambda)=1-3(2\lambda-1)^2$, and $c_{\beta\gamma}+c_{bc}=0$
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4557:$c_{bc} + c_{\beta\gamma} = 0$ at $\lambda = 1$: $-2 + 2 = 0$;
/Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex:2203:c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) \;=\; 0
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:4542:central charge: $c_{bc}=-c_{\beta\gamma}$.
/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v3.tex:2075:$c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) = 0$
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3170:satisfying $c_{\beta\gamma} + c_{bc} = 0$ (verified at
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3171:$\lambda = 2$: $c_{\beta\gamma} = 26$, $c_{bc} = -26$; string
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:922:$K(bc_\lambda) = c_{bc}(\lambda) + c_{\beta\gamma}(\lambda)
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2177:contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:637:c_{\beta\gamma} + c_{bc} = 0.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:642:The central charge of the $\beta\gamma$ system is computed from the stress tensor (Theorem~\ref{thm:beta-gamma-stress}). Replacing bosonic statistics by fermionic statistics negates the Virasoro central term: the commutator $[L_m, L_n]$ picks up a sign from the fermion loop, so $c_{bc} = -c_{\beta\gamma}$.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1235:$c_{bc} = -c_{\beta\gamma}$
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1777:exponents cancel because $c_{\beta\gamma} + c_{bc} = 0$.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:1808:charge is $c_{bc}(\lambda) = -c_{\beta\gamma}(\lambda)$
/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:922:By complementarity $c_{\beta\gamma} + c_{bc} = 0$:
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:808: \qquad c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) \;=\; 0
/Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex:2202:% C7: c_betagamma + c_bc = 0 for all lambda
/Users/raeez/chiral-bar-cobar/standalone/five_theorems_modular_koszul.tex:2203:c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) \;=\; 0
/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:504:$c_{\beta\gamma} + c_{bc} = 0$; verify at $\lambda = 1$:
/Users/raeez/chiral-bar-cobar/standalone/survey_track_b_compressed.tex:505:$c_{\beta\gamma} = 2$, $c_{bc} = -2$.)
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4534:$c_{bc}(\lambda)=1-3(2\lambda-1)^2$, and $c_{\beta\gamma}+c_{bc}=0$
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality_v2.tex:4557:$c_{bc} + c_{\beta\gamma} = 0$ at $\lambda = 1$: $-2 + 2 = 0$;
/Users/raeez/chiral-bar-cobar/standalone/shadow_towers_v3.tex:2075:$c_{\beta\gamma}(\lambda) + c_{bc}(\lambda) = 0$
/Users/raeez/chiral-bar-cobar/standalone/survey_modular_koszul_duality.tex:4542:central charge: $c_{bc}=-c_{\beta\gamma}$.
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3170:satisfying $c_{\beta\gamma} + c_{bc} = 0$ (verified at
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3171:$\lambda = 2$: $c_{\beta\gamma} = 26$, $c_{bc} = -26$; string
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1039:$\kappa(\beta\gamma) = c_{\beta\gamma}/2 = 6\lambda^2 - 6\lambda + 1$ and $\kappa(bc) = -\kappa(\beta\gamma)$; the


thinking
**Investigating formula issues**

It looks like the search shows that free_fields might have the wrong symbol. I probably need to check other files in volumes II and III for the actual formulas. I should inspect the contexts around those suspicious lines to see what's going on. I can edit only in the current repository due to writing restrictions, but I wonder if there could be issues in volumes II and III that I can't edit. Let's focus on lines in volume II related to compute ds_brst_sc_engine and other candidates.
exec
/bin/zsh -lc "sed -n '744,816p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '526,545p' /Users/raeez/chiral-bar-cobar-vol2/compute/lib/ds_brst_sc_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2168,2188p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4168,4200p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\subsection{Chiral de~Rham complex on K3}
\label{subsec:cdr-k3}

\begin{remark}[CDR on K3]
\label{rem:cdr-k3}
\index{chiral de Rham complex!K3}
The chiral de~Rham complex $\Omega^{\mathrm{ch}}(K3)$ of
Malikov--Schechtman--Vaintrob is a sheaf of vertex
superalgebras on K3 with central charge $c = 0$ (the local
contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
complex dimension cancel globally). The CDR cohomology
recovers the K3 elliptic genus:
$\mathrm{ch}\bigl(H^*\bigl(K3, \Omega^{\mathrm{ch}}\bigr)\bigr)
= \mathrm{Ell}(K3; q, y) = 2\,\phi_{0,1}(\tau, z)$
(Borisov--Libgober).

On a hyperk\"ahler manifold (such as K3), the CDR carries
$\cN = 4$ superconformal symmetry at $c = 0$: the
topological $\cN = 4$ algebra, distinct from the physical
$\cN = 4$ at $c = 6$. Both give
 succeeded in 52ms:
    delta_c = -12 * K
    delta_c_half = delta_c / 2

    # Ghost: c_ghost/2
    # c_ghost = -2 · Σ_{d=1}^{N-1} (N-d)(6d²-6d+1)
    c_ghost = S.Zero
    N_int = int(N) if N.is_integer else None
    if N_int is not None:
        for d in range(1, N_int):
            n_pairs = N_int - d
            c_bc = -2 * (6 * d ** 2 - 6 * d + 1)
            c_ghost += n_pairs * c_bc
    else:
        # Symbolic: use the closed-form
        # Σ_{d=1}^{N-1} (N-d)(6d²-6d+1)
        # This has a closed form but we leave it symbolic for small N
        pass
    c_ghost_half = c_ghost / 2

    # Total
 succeeded in 51ms:
Arakelov $(1,1)$-form on $E_\tau$.
The total corrected differential $\Dg{1} = d_0 + F_1(\cA)\cdot d_1$, with
\textup{(g=1 only; all-weight at g=1 is unconditional)}
\[
F_1(\cA) = \kappa(\cA)\cdot\lambda_1^{FP} = \frac{\kappa(\cA)}{24},
\]
satisfies $\Dg{1}^{\,2} = 0$ by the same cancellation mechanism as in
Theorem~\textup{\ref{thm:genus1-d-squared}}.

Explicit values for the standard landscape:
\begin{center}
\begin{tabular}{lcccc}
\toprule
$\cA$ & $\kappa(\cA)$ & $\kappa(\cA^!)$ & $\kappa + \kappa^!$ & $F_1(\cA)$ \textup{(g=1 only; all-weight at g=1 is unconditional)} \\
\midrule
$\mathcal{H}_\kappa$ & $\kappa$ & $-\kappa$ & $0$ & $\kappa/24$ \\
$\widehat{\mathfrak{sl}}_2$ level $k$ & $\tfrac{3(k+2)}{4}$ & $-\tfrac{3(k+2)}{4}$ & $0$ & $\tfrac{k+2}{32}$ \\
$\mathrm{Vir}_c$ & $c/2$ & $(26-c)/2$ & $13$ & $c/48$ \\
$\mathcal{W}_3$ charge $c$ & $5c/6$ & $5(100-c)/6$ & $250/3$ & $5c/144$ \\
$bc_\lambda$ & $c_{bc}/2$ & $c_{bg}/2$ & $0$ & $c_{bc}/48$ \\
 succeeded in 52ms:


\subsection{\texorpdfstring{The $bc$ ghosts}{The bc ghosts}}
\index{$bc$ system|textbf}

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
thinking
**Summarizing formula occurrences with canonical matches**

I’ve gathered all relevant bc and betagamma central charge formulas found, noting for each the exact formula text, file and line, and whether it matches the canonical c_bc or c_bg expressions. This list highlights both correct and mismatched formulas, keeping clarity without nesting. Here are the key occurrences:

- `AGENTS.md:671` — "c_bc(lambda) = 1 - 3(2*lambda-1)^2" — matches canonical c_bc(lambda)=1-3(2lambda-1)^2 by definition.  
- `AGENTS.md:672` — "c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)" — matches canonical c_bg(lambda)=2(6lambda^2-6lambda+1).  
- `compute/lib/non_cy_local_surface_chiral.py:505` — "c = -2(6lambda^2 - 6lambda + 1)" (presented for betagamma but flagged in comments as incorrect) — does not match canonical c_bg due to negative sign; canonical is positive.  
- `compute/lib/non_cy_local_surface_chiral.py:513` — "c = -2(6lambda^2 - 6lambda + 1) = 1 - 3(2lambda - 1)^2" — matches canonical c_bc(lambda)=1-3(2lambda-1)^2.  
- `compute/lib/non_cy_local_surface_chiral.py:520` — "c = 2(6lambda^2 - 6lambda + 1) = -1 + 3(2lambda-1)^2" — matches canonical c_bg(lambda)=2(6lambda^2-6lambda+1).  
- `compute/lib/non_cy_local_surface_chiral.py:720` — "c = 1 - 3(2*0 - 1)^2 = 1 - 3 = -2 (as bc) or c = -1 + 3(2*0 - 1)^2 = -1 + 3 = 2 (as betagamma)" — matches canonical c_bc and c_bg formulas evaluated at λ=0.  
- `compute/lib/non_cy_local_surface_chiral.py:751` — "c = 1 - 3(2*h_beta - 1)^2 (for bc/fermions) and c = -1 + 3(2*h_beta - 1)^2 (for betagamma/bosons)" — general formulas matching canonical c_bc and c_bg.  
- `compute/lib/three_d_n2_cy3_engine.py:494` — "c(beta-gamma) = -1 + 3(2h-1)^2 = -1 + 3(2*1-1)^2 = -1 + 3 = 2" — matches canonical c_bg expression.  
- `compute/lib/three_d_n2_cy3_engine.py:504` — "c = -1 + 3(2*1/2 - 1)^2 = -1 + 0 = -1" — applies canonical form but evaluated value flagged as inconsistent with standard beta-gamma central charge.  
- `compute/tests/test_cross_volume_shadow_bridge.py:881` — "c = 2(6*4 - 12 + 1) = 26" — matches canonical c_bg formula evaluated at λ=2.  
- `compute/tests/test_cross_volume_shadow_bridge.py:886` — "c = 2(0 - 0 + 1) = 2" — matches canonical c_bg formula evaluated at λ=0.  

This captures all notable formula hits with clear status on their canonical matches or mismatches.
codex
Found the following cc/betagamma central-charge formulas in `/Users/raeez/calabi-yau-quantum-groups` with their canonical-status judgments:

- `AGENTS.md:671` — `"c_bc(lambda) = 1 - 3(2*lambda-1)^2"` — by construction this is the canonical `c_bc(lambda)=1-3(2lambda-1)^2`.  
- `AGENTS.md:672` — `"c_bg(lambda) = 2*(6*lambda^2 - 6*lambda + 1)"` — direct match to the canonical `c_bg(lambda)=2(6lambda^2-6lambda+1)`.  
- `compute/lib/non_cy_local_surface_chiral.py:505` — `"c = -2(6lambda^2 - 6lambda + 1)"` (presented for the betagamma system but flagged “no” in the surrounding text) — does **not** match canonical `c_bg` (should be `+2(6…)`).  
- `compute/lib/non_cy_local_surface_chiral.py:513` — `"c = -2(6lambda^2 - 6lambda + 1) = 1 - 3(2lambda - 1)^2"` — now recast as the canonical `c_bc(lambda)` after simplifying, so it matches `c_bc`.  
- `compute/lib/non_cy_local_surface_chiral.py:520` — `"c = 2(6lambda^2 - 6lambda + 1) = -1 + 3(2lambda-1)^2"` — matches canonical `c_bg(lambda)` (the alternate form `-1 + 3(2lambda-1)^2` is algebraically equivalent).  
- `compute/lib/non_cy_local_surface_chiral.py:720` — `"c = 1 - 3(2*0 - 1)^2 = 1 - 3 = -2 (as a bc system) or c = -1 + 3(2*0 - 1)^2 = -1 + 3 = 2 (as betagamma)"` — both evaluations are specializations of the canonical `c_bc` and `c_bg` formulas at λ=0.  
- `compute/lib/non_cy_local_surface_chiral.py:751` — `"c = 1 - 3(2*h_beta - 1)^2  (for bc/fermions)` and `c = -1 + 3(2*h_beta - 1)^2  (for betagamma/bosons)"` — restates the canonical bc/betagamma formulas in terms of the conformal weights.  
- `compute/lib/three_d_n2_cy3_engine.py:494` — `"c(beta-gamma) = -1 + 3(2h-1)^2 = -1 + 3(2*1-1)^2 = -1 + 3 = 2"` — uses the canonical `c_bg` expression (the comment even admits the same formula is used for bc ghosts).  
- `compute/lib/three_d_n2_cy3_engine.py:504` — `"In this case c = -1 + 3(2*1/2 - 1)^2 = -1 + 0 = -1..."` — the canonical `c_bg` formula evaluated at `h=1/2` gives `-1`, which the text flags as not the standard betagamma value, so note the result is consistent with the algebraic formula but not with the expected physical assignment.  
- `compute/tests/test_cross_volume_shadow_bridge.py:881` — `"beta-gamma at lambda = 2: c = 2(6*4 - 12 + 1) = 2*13 = 26."` — canonical `c_bg` evaluation at λ=2 yields 26 as expected.  
- `compute/tests/test_cross_volume_shadow_bridge.py:886` — `"beta-gamma at lambda = 0: c = 2(0 - 0 + 1) = 2."` — canonical `c_bg` evaluated at λ=0 gives 2, matching the standard formula.

Let me know if you’d like a follow-up pass flagging any of the mismatched references for correction (e.g., the `-2(6λ^2... )` betagamma line).
exec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{\\\\beta\\\\gamma\\}["'^'"\\n]{0,120}1\\s*-\\s*3\\s*\\(2\\\\lambda\\s*-\\s*1\\)\\"'^2|c_betagamma[''^'"\\n]{0,120}1\\s*-\\s*3\\s*\\(2\\*?lambda\\s*-\\s*1\\)\\"'^2|c_'"\\\\beta\\\\gamma["'^'"\\n]{0,120}1\\s*-\\s*3\\s*\\(2\\\\lambda\\s*-\\s*1\\)\\"'^2'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{bc\\}["'^'"\\n]{0,120}2\\s*\\(6\\\\lambda\\"'^2'"\\s*-\\s*6\\\\lambda\\s*\\+\\s*1\\)|c_bc["'^'"\\n]{0,120}2\\s*\\(6\\*?lambda\\"'^2'"\\s*-\\s*6\\*?lambda\\s*\\+\\s*1\\)|c_\\{bc\\}["'^'"\\n]{0,120}\\+2\\s*\\(6\\\\lambda\\"'^2'"\\s*-\\s*6\\\\lambda\\s*\\+\\s*1\\)' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{bc\\}["'^'"\\n]{0,120}-2\\s*\\(6\\\\lambda\\"'^2'"\\s*-\\s*6\\\\lambda\\s*\\+\\s*1\\)|c_bc["'^'"\\n]{0,120}-2\\s*\\(6\\*?lambda\\"'^2'"\\s*-\\s*6\\*?lambda\\s*\\+\\s*1\\)|c_\\{\\\\beta\\\\gamma\\}["'^'"\\n]{0,120}2\\s*\\(6\\\\lambda\\"'^2'"\\s*-\\s*6\\\\lambda\\s*\\+\\s*1\\)|c_betagamma["'^'"\\n]{0,120}2\\s*\\(6\\*?lambda\\"'^2'"\\s*-\\s*6\\*?lambda\\s*\\+\\s*1\\)' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 713ms:
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/R15_toroidal_elliptic_v1.md:405:- **Finding valid?** No — `chapters/examples/toroidal_elliptic.tex:2079-2090` already reports `c_{bc}=-2` and `c_{\beta\gamma}=+2` per complex dimension, which matches the canonical `c_{bc}=1-3(2\lambda-1)^2` and `c_{\beta\gamma}=2(6\lambda^2-6\lambda+1)` evaluations at the usual ghost weights; nothing is swapped.  
/Users/raeez/chiral-bar-cobar/compute/audit/wrong_formulas_blacklist_wave12.md:61:- WRONG:    `c_{\beta\gamma}(\lambda) = 1 - 3(2\lambda - 1)^2`
 succeeded in 686ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
/Users/raeez/chiral-bar-cobar/relaunch_20260413_111534/R15_toroidal_elliptic_v1.md:405:- **Finding valid?** No — `chapters/examples/toroidal_elliptic.tex:2079-2090` already reports `c_{bc}=-2` and `c_{\beta\gamma}=+2` per complex dimension, which matches the canonical `c_{bc}=1-3(2\lambda-1)^2` and `c_{\beta\gamma}=2(6\lambda^2-6\lambda+1)` evaluations at the usual ghost weights; nothing is swapped.  
/Users/raeez/chiral-bar-cobar/fix_wave_E_20260413_182434/E03_test_gaps_central.md:453:- [MEDIUM] [chapters/examples/beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:315) — The theorem surface uses only the non-canonical rewrite `c_{bc}=-2(6\lambda^2-6\lambda+1)`; the same drift recurs at line 635. Expansion shows it is equivalent to the canonical `1-3(2\lambda-1)^2`, so this is notation drift, not a false value. The same file’s line 321 uses the canonical form, so the file is internally inconsistent.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC05_c_26.md:1930:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/BC05_c_26.md:1972:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:7:- [MEDIUM] [chapters/examples/beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:315) — The theorem surface uses only the non-canonical rewrite `c_{bc}=-2(6\lambda^2-6\lambda+1)`; the same drift recurs at line 635. Expansion shows it is equivalent to the canonical `1-3(2\lambda-1)^2`, so this is notation drift, not a false value. The same file’s line 321 uses the canonical form, so the file is internally inconsistent.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:136:chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:140:chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:345:chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:347:chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:413:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:465:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:627:I’m looking into various findings, starting with checking for formula mismatches. There might be differences in notation, like the canonical `c_bc(lambda)=1 - 3(2lambda-1)^2` versus the equivalent `-2(6lambda^2 - 6lambda +1)`, which isn’t canonical. The user wants me to flag even minor discrepancies, so I can classify these as LOW/MEDIUM.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:723:chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:988:chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:990:chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:996:chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/F08_c_bc.md:1013:chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
 succeeded in 477ms:
/Users/raeez/chiral-bar-cobar/compute/lib/betagamma_shadow_full.py:42:  c_bc(lambda) = -2(6*lambda^2 - 6*lambda + 1)
/Users/raeez/chiral-bar-cobar/compute/lib/betagamma_shadow_full.py:678:      c_bc = -2(6*lambda^2 - 6*lambda + 1)
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:20075:$c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$ and
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:78059:-$c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$ and
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:119396:-$c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$ and
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:160752:-$c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$ and
/Users/raeez/chiral-bar-cobar/fix_wave_B_20260413_171623/B11_orphaned_chapters.md:202133:-$c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)$ and
/Users/raeez/chiral-bar-cobar/compute/lib/bv_brst_chain_level.py:598:    # c_bc = -2(6*lambda^2 - 6*lambda + 1) for lambda=2: c = -2(24-12+1) = -26
/Users/raeez/chiral-bar-cobar/compute/lib/dmod_counterexample_search_engine.py:1042:    # Betagamma central charge: c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)
/Users/raeez/chiral-bar-cobar/compute/audit/latex_pitfall_blacklist_wave12.md:295:- Failure mode: `c_{\beta\gamma}(\lambda) = 2(6\lambda^2-6\lambda+1)` and
/Users/raeez/chiral-bar-cobar/compute/audit/true_formula_census_draft_wave12.md:54:$$c_{\beta\gamma}(\lambda) \;=\; 2(6\lambda^2 - 6\lambda + 1).$$
/Users/raeez/chiral-bar-cobar/compute/audit/wrong_formulas_blacklist_wave12.md:55:- CORRECT:  `c_{bc}(\lambda) = 1 - 3(2\lambda - 1)^2`; separately `c_{\beta\gamma}(\lambda) = 2(6\lambda^2-6\lambda+1)`
/Users/raeez/chiral-bar-cobar/compute/audit/wrong_formulas_blacklist_wave12.md:62:- CORRECT:  `c_{\beta\gamma}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)`
/Users/raeez/chiral-bar-cobar/compute/tests/test_literature_cross_check.py:267:        """c_bc(lambda) = -2(6*lambda^2 - 6*lambda + 1) = 1 - 3(2*lambda-1)^2."""
exec
/bin/zsh -lc "sed -n '2168,2186p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2068,2094p' chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{\\\\beta\\\\gamma\\}|c_\\{bc\\}|beta-gamma|bc' chapters/examples/toroidal_elliptic.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
sed: chapters/examples/toroidal_elliptic.tex: No such file or directory
 succeeded in 51ms:
\subsection{Chiral de~Rham complex on K3}
\label{subsec:cdr-k3}

\begin{remark}[CDR on K3]
\label{rem:cdr-k3}
\index{chiral de Rham complex!K3}
The chiral de~Rham complex $\Omega^{\mathrm{ch}}(K3)$ of
Malikov--Schechtman--Vaintrob is a sheaf of vertex
superalgebras on K3 with central charge $c = 0$ (the local
contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
complex dimension cancel globally). The CDR cohomology
recovers the K3 elliptic genus:
$\mathrm{ch}\bigl(H^*\bigl(K3, \Omega^{\mathrm{ch}}\bigr)\bigr)
= \mathrm{Ell}(K3; q, y) = 2\,\phi_{0,1}(\tau, z)$
(Borisov--Libgober).

On a hyperk\"ahler manifold (such as K3), the CDR carries
$\cN = 4$ superconformal symmetry at $c = 0$: the
topological $\cN = 4$ algebra, distinct from the physical
 exited 2 in 52ms:
Total output lines: 108

rg: chapters/examples/toroidal_elliptic.tex: No such file or directory (os error 2)
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:74:seeks genuine surface-factorization objects on $\bC^* \times \bC^*$,
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:87:surface-factorization object on $\bC^* \times \bC^*$. Only
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:220:$\bC^* \times \bC^*$, with one direction encoding the spectral
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:228:Conjecture~\ref{conj:toroidal-e1} is conjectural (\ClaimStatusConjectured): a complete proof requires verifying associativity of the $\Eone$-chiral product directly from the OPE relations, since the BD locality approach applies only to commutative chiral algebras. The $\bC^* \times \bC^*$ realization (Conjecture~\ref{conj:toroidal-surface-factorization}) is a separate surface-factorization problem within the MC4 elliptic/double-affine extension problem.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:259:Set $\tau = \log t / \log q$ and let $E_\tau = \bC^*/q^{\bZ}$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:261:on $\bC^*$ with quasi-periodicity $e_i(qz) = q^{d_i} e_i(z)$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:268:\emph{Step~4: Surface-factorization horizon on $\bC^* \times \bC^*$.}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:271:Together they give fields on $\bC^*_u \times \bC^*_z$ with the
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:285:$\bC^* \times \bC^*$ surface track belongs instead to
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:337:This is the algebraic incarnation of the exchange of the two $\bC^*$
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:338:factors in the torus $\bC^* \times \bC^*$ underlying the double loop.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:728:linearly independent over~$\bC$), and the $E_\infty$ terms in
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:790:We work on $E_\tau = \bC / (\bZ + \tau\bZ)$ with the elliptic
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:910:on $\bC$ versus $E_\tau$; on $\bC$ the propagator
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:961:reflects that the Heisenberg algebra on $\bC$ (genus~$0$)
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:963:$1/z$ is strictly periodic on $\bC$ (there is no $B$-cycle).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1034:over $\bC$. The decomposition~\eqref{eq:ell-bar-decomp}
exec
/bin/zsh -lc "rg -n --hidden -S 'AP137|bc/betagamma|beta.?gamma.*swap|swap.*beta.?gamma|c_\\{\\\\beta\\\\gamma\\}=-2|c_\\{bc\\}=\\+2|c_\\{\\\\beta\\\\gamma\\}\\s*=\\s*-2|c_\\{bc\\}\\s*=\\s*\\+2' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{\\\\beta\\\\gamma\\}["'^'"\\n]{0,120}=\\s*-2|c_\\{bc\\}["'^'"\\n]{0,120}=\\s*\\+2|c_betagamma["'^'"\\n]{0,120}=\\s*-2|c_bc["'^'"\\n]{0,120}=\\s*\\+2' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 817ms:
/Users/raeez/chiral-bar-cobar/compute/lib/extended_ferm_ghost.py:85:    # AP137: c_bc + c_bg = 0; verified at lambda=2: -26+26=0.
/Users/raeez/chiral-bar-cobar/compute/lib/extended_ferm_ghost.py:106:    # AP137: c_bc + c_bg = 0; verified at lambda=2: -26+26=0.
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P13_SC_formality_upgrade.md:254:**ratios/reciprocals** (AP129, AP137): AP129: When a formula involves a/b, the most common transcription error is b/a. ALWAYS substitute a known numerical value to verify. AP137: Bosonic c_{βγ} and fermionic c_{bc} satisfy c_{βγ}+c_{bc}=0. They look similar but have opposite signs. VERIFY: check c_total=0.
/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:411:                # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
/Users/raeez/chiral-bar-cobar/compute/lib/bc_mzv_shadow_engine.py:418:                # AP137: c_bg(lambda=1) = +2, c_bc(lambda=1) = -2
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U10_missing_computations.md:227:233:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U10_missing_computations.md:388:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U10_missing_computations.md:1164:233:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U10_missing_computations.md:3003:**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U10_missing_computations.md:4204:   233	**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).
/Users/raeez/chiral-bar-cobar/compute/audit/hook_enhancements_wave12.md:81:6. **Bosonic/fermionic partner sign** (AP137): `c_{\beta\gamma}` vs `c_{bc}`. No check.
/Users/raeez/chiral-bar-cobar/compute/audit/hook_enhancements_wave12.md:425:#### H11. AP137 -- Bosonic/fermionic partner sanity
/Users/raeez/chiral-bar-cobar/compute/audit/hook_enhancements_wave12.md:432:# AP137: bosonic/fermionic partner sanity check
/Users/raeez/chiral-bar-cobar/compute/audit/hook_enhancements_wave12.md:435:  WARNINGS="${WARNINGS}AP137: ghost central-charge partners detected. VERIFY c_{beta gamma} + c_{bc} = 0. At lambda=1: c_{beta gamma}=2, c_{bc}=-2. c_{beta gamma}(lambda)=2(6 lambda^2 - 6 lambda + 1), c_{bc}(lambda)=1-3(2 lambda - 1)^2. Lines: ${MATCHES}\n"
/Users/raeez/chiral-bar-cobar/compute/audit/hook_enhancements_wave12.md:441:**Expected APs prevented:** AP137.
/Users/raeez/chiral-bar-cobar/compute/audit/hook_enhancements_wave12.md:710:| 14 | H11 AP137 ghost partners | AP137 | WARN | 2-3 | LOW | LOW |
/Users/raeez/chiral-bar-cobar/compute/audit/beilinson_audit_vol1_preface_wave11.md:184:### Attempt 3.5 -- $\beta\gamma$ vs $bc$ partner sign (AP137)
/Users/raeez/chiral-bar-cobar/compute/audit/beilinson_audit_vol1_preface_wave11.md:185:**Verdict**: PASS. "Koszul dual: $bc$ ghosts" (line 2452). Opposite-statistics partners. AP137
/Users/raeez/chiral-bar-cobar/compute/audit/beilinson_audit_vol1_preface_wave11.md:450:| AP137 | $\beta\gamma$ vs $bc$ partner sign | PASS |
/Users/raeez/chiral-bar-cobar/compute/audit/platonic_rewrite_2026_03_28/13_FINAL_SYNTHESIS.md:103:| bc/betagamma | 0 | 0 |
 succeeded in 811ms:
/Users/raeez/chiral-bar-cobar/scripts/fix_campaign_100.py:170:States c_betagamma = -2, c_bc = +2. Should be c_bc = -2, c_bg = +2.
/Users/raeez/chiral-bar-cobar/scripts/fix_campaign_100.py:171:Canonical: c_bc(lambda=1) = 1-3(1)^2 = -2. c_bg(lambda=1) = 2(1) = +2.
/Users/raeez/chiral-bar-cobar/scripts/rectification_campaign.py:420:   States c_betagamma = -2 and c_bc = +2 per complex dimension.
/Users/raeez/chiral-bar-cobar/scripts/rectification_campaign.py:421:   CANONICAL: c_bc(lambda=1) = 1-3(2*1-1)^2 = 1-3 = -2. c_bg(lambda=1) = 2(6-6+1) = +2.
/Users/raeez/chiral-bar-cobar/scripts/rectification_campaign.py:422:   So c_bc = -2, c_bg = +2. The file has them SWAPPED.
/Users/raeez/chiral-bar-cobar/scripts/rectification_campaign.py:423:   FIX: Swap the signs. c_bc = -2, c_betagamma = +2.
/Users/raeez/chiral-bar-cobar/scripts/rectification_campaign.py:433:   c_betagamma = -2, c_bc = +2 stated. Should be c_bc = -2, c_bg = +2.
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:518:$c_{\beta\gamma} = 2$, $c_{bc} = -2$.)
/Users/raeez/chiral-bar-cobar/tmp_standalone_audit/wrap_survey_track_b_fixed.tex:518:$c_{\beta\gamma} = 2$, $c_{bc} = -2$.)
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:4:`c_{bc} = -2` and `c_{\beta\gamma} = +2`.
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:6:I re-read the surrounding remark to confirm the `c=0` cancellation sentence still reads coherently. I also grepped the rest of `chapters/examples/toroidal_elliptic.tex` for `c_{bc}` / `c_{\beta\gamma}` sign drift; this was the only occurrence. Forbidden literal checks on the modified file passed: no `c_{bc} = +2` and no `c_{\beta\gamma} = -2` remain. No `\ref` or `\label` changes were needed.
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:43:States c_betagamma = -2, c_bc = +2. Should be c_bc = -2, c_bg = +2.
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:44:Canonical: c_bc(lambda=1) = 1-3(1)^2 = -2. c_bg(lambda=1) = 2(1) = +2.
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:189:Using `multi-path-verify` for the CDR central-charge sentence. I’ve confirmed the local surface: the K3 CDR remark currently states the per-dimension contributions as `c_{\beta\gamma}=+2`, `c_{bc}=-2`; I’m checking the rest of `toroidal_elliptic.tex` for any other `bc/bg` sign drift before making a one-line correction.
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:209:2085:contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:211:2085:contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:216:2085:contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:220:2085:contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:304:claim: In the K3 CDR remark, the per-complex-dimension free-field contributions at λ=1 are c_{bc}=-2 and c_{\beta\gamma}=+2.
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A06_toroidal_v1.md:315:-contributions $c_{\beta\gamma} = +2$ and $c_{bc} = -2$ per


thinking
**Considering file editing guidelines**

I'm trying to clarify the action safety guideline that states I should only edit assigned files. But what exactly does "assigned files" mean? It seems to refer to the comprehensive central charge audit across all volumes, suggesting I should fix any wrong occurrences in files that have issues. However, I'm questioning whether editing internal audit note documents is necessary since they may contain historical findings. Should I only focus on the current live repository, or do I address archival notes? It's a bit unclear!
thinking
**Clarifying auditing scope**

The user mentioned needing a comprehensive review across all volumes for occurrences of c_bc or c_betagamma. This means I should verify the formula even in audit notes. However, editing all historical notes could be overwhelming and might distort history. If those statements are false now but were accurate in the past, maybe we don't need to change them. It's tricky! I think the task likely focuses on live code rather than archived logs, so I’ll need to define what "occurrence" means here.
codex
I’ve narrowed the live-source surface further. Most of the remaining “hits” are historical rectification notes that intentionally quote old errors; I’m excluding those from the live manuscript/code audit and checking the actual source trees for only two things: swapped formulas and stale sign assignments that still survive in editable source.
exec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{bc\\}\\s*=\\s*\\+2|c_\\{\\\\beta\\\\gamma\\}\\s*=\\s*-2|c_bc\\s*=\\s*\\+2|c_betagamma\\s*=\\s*-2|c_\\{bc\\}\\(["'^)]*'"\\)\\s*=\\s*2\\(6\\\\lambda\\"'^2|c_'"\\{\\\\beta\\\\gamma\\}\\(["'^)]*'"\\)\\s*=\\s*1\\s*-\\s*3\\(2\\\\lambda\\s*-\\s*1\\)\\"'^2'"' chapters standalone compute /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/compute /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/compute" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{bc\\}\\s*=\\s*-2\\(6\\\\lambda\\"'^2'"\\s*-\\s*6\\\\lambda\\s*\\+\\s*1\\)|c_bc\\s*=\\s*-2 \\* \\(6 \\* .*lambda.*- 6 \\* .*lambda.*\\+ 1\\)|c_bc\\s*=\\s*-2\\*\\(6\\*lambda\\"'^2 - 6'"\\*lambda \\+ 1\\)' chapters standalone compute /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/compute /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/compute" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{\\\\beta\\\\gamma\\}\\s*=\\s*\\+2\\(6\\\\lambda\\"'^2'"\\s*-\\s*6\\\\lambda\\s*\\+\\s*1\\)|c_betagamma\\s*=\\s*2\\*\\(6\\*lambda\\"'^2 - 6'"\\*lambda \\+ 1\\)|c_bg\\s*=\\s*2\\*\\(6\\*lambda\\"'^2 - 6'"\\*lambda \\+ 1\\)' chapters standalone compute /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/compute /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/compute" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/audit/wrong_formulas_blacklist_wave12.md:54:- WRONG:    `c_{bc}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)`
compute/audit/wrong_formulas_blacklist_wave12.md:61:- WRONG:    `c_{\beta\gamma}(\lambda) = 1 - 3(2\lambda - 1)^2`
 succeeded in 50ms:
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
 succeeded in 50ms:
chapters/examples/beta_gamma.tex:312:c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
chapters/examples/beta_gamma.tex:326:Bosonic $\beta\gamma$ system ($c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1)$):
chapters/examples/beta_gamma.tex:633:c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
compute/tests/test_kappa_literature_crosscheck.py:352:       And c_betagamma = 2*(6*lambda^2 - 6*lambda + 1). Confirm.)

thinking
**Considering organization of content**

I’m thinking about whether I should reorder things to maintain consistency, particularly for the canonical structure. It might help, but it may not be necessary. I also noticed that in `beta_gamma.tex`, the summary list from lines 312 to 315 and theorems or propositions could benefit from canonicalization as well. I'm wondering if there might be other live surfaces that have non-canonical formulas. A search only turned up those three lines along with a computation formula from volume 2.
exec
/bin/zsh -lc "sed -n '304,332p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '628,640p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2374,2388p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
\label{thm:beta-gamma-ope-complete}
Fermionic $bc$ system ($c_{bc} = 1 - 3(2\lambda-1)^2$):
$\lambda = 2$: $c = -26$ (string theory ghosts);
$\lambda = 1$: $c = -2$;
 succeeded in 51ms:
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

 succeeded in 50ms:
\section{Free fermion genus expansion}\label{sec:fermion-genera}
\index{free fermion!genus expansion}
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
exec
/bin/zsh -lc "sed -n '34,48p' compute/lib/betagamma_shadow_full.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '670,686p' compute/lib/betagamma_shadow_full.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '590,604p' compute/lib/bv_brst_chain_level.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the OPE. The beta-gamma OPE has a simple pole, so the r-matrix has NO
pole: r(z) = constant. The nontrivial shadow structure comes from the
STRESS TENSOR subalgebra (which has poles up to z^{-4} in the OPE,
giving poles up to z^{-3} in the r-matrix).

COMPLEMENTARITY (Theorem C):
  (beta-gamma)^! = bc ghost system (statistics exchange, NOT weight exchange!)
  c_bg(lambda) = +2(6*lambda^2 - 6*lambda + 1)
  c_bc(lambda) = -2(6*lambda^2 - 6*lambda + 1)
  kappa(bg) + kappa(bc) = 0  (exact complementarity, AP24 safe)

NOTE ON KOSZUL DUALITY vs WEIGHT SYMMETRY:
  The formula kappa = 6*lambda^2 - 6*lambda + 1 is symmetric under
  lambda -> 1-lambda: kappa(lambda) = kappa(1-lambda). This is because
  beta at weight lambda and gamma at weight 1-lambda produce the SAME
 succeeded in 51ms:
# =========================================================================
# 12. Comparison with bc ghost system (from quintic_shadow_engine.py)
# =========================================================================

def bc_ghost_1d_data(lam_val=None):
    r"""Shadow data for the bc ghost system on its T-line.

    The bc system at weight lambda has:
      c_bc = -2(6*lambda^2 - 6*lambda + 1)
      kappa_bc = -kappa_bg = -(6*lambda^2 - 6*lambda + 1)

    The bc T-line shadow data is the Virasoro data at c = c_bc.
    In particular, at lambda = 1 (c_bc = -2):
      kappa = -1, S_3 = 2, S_4 = 10/((-2)(5*(-2)+22)) = 10/(-24) = -5/12.

    On the 1D metric, the bc tower does NOT terminate (class M in 1D).
    True depth = 4 by the same stratum separation as for bg.
 succeeded in 51ms:
    # kappa(H_1) = 1 (the level parameter IS the modular characteristic)
    # See master table in landscape_census.tex and genus_expansions.tex
    c_per_boson = Rational(1)
    kappa_per_boson = Rational(1)
    c_matter = n_bosons * c_per_boson
    kappa_matter = n_bosons * kappa_per_boson

    # bc ghost system at weights (2, -1):
    # c_bc = -2(6*lambda^2 - 6*lambda + 1) for lambda=2: c = -2(24-12+1) = -26
    c_ghost = Rational(-26)
    kappa_ghost = c_ghost / 2  # = -13

    c_total = simplify(c_matter + c_ghost)
    kappa_total = simplify(kappa_matter + kappa_ghost)
    # Anomaly cancellation is about CENTRAL CHARGE, not kappa



thinking
**Evaluating compute docstrings**

I see that the compute docstrings and comments use noncanonical formulas, but they’re still correct. Since the user asked about every occurrence of c_bc or c_betagamma, I’ll need to verify and determine if we should patch the manuscript. Maybe it’s just a notation drift issue. Editing only those comments might be more extensive, but any noncanonical formulas could be seen as an issue. If the user's looking for edits, I'll ensure a minimum of truthful changes.
thinking
**Verifying formulas and aliases**

I need to ensure that the term 'd' is not confused with lambda, but it's not incorrect. I should check for instances of the `c_bg` alias in the live source, even though the user specifically asked about c_bc or c_betagamma. I'll verify that the usage of `c_bg` is also consistent, possibly by examining a table. To be cautious, I’ll note that `higher_genus_foundations.tex:4187` uses `c_{bg}/2` as shorthand for `c_{\beta\gamma}/2`, which is accurate and doesn’t require edits. For further verification, I might consider using symbolic computation in Python or simple shell, depending on what's necessary.
thinking
**Exploring direct evaluations**

To satisfy the need for multi-path verification, I might want to compute direct evaluations at λ=1/2, 1, and 2. I could use shell commands with Python or even `bc` for these direct calculations, though it might not be strictly necessary. Still, it could be beneficial to run a quick script or employ `sympy` to compute the differences. I can use `python - <<'PY'` for computations without file reading, which seems acceptable. Let’s proceed with direct evaluations to ensure formula equality at those lambda values.
codex
I’ve isolated the live issues as AP137 notation drift, not live sign swaps: a small set of theorem/proposition surfaces still present the fermionic `bc` charge only in the reduced `-2(6λ²-6λ+1)` form. I’m doing one direct symbolic check now, then I’ll patch those surfaces to put the canonical `1-3(2λ-1)^2` first and leave the equivalent expanded form visible where helpful.
exec
/bin/zsh -lc "python - <<'PY'
from fractions import Fraction
for lam in [Fraction(1,2), Fraction(1), Fraction(2), Fraction(3,2)]:
    c_bc = 1 - 3*(2*lam-1)**2
    c_bg = 2*(6*lam*lam - 6*lam + 1)
    print(lam, c_bc, c_bg, c_bc + c_bg)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '72,82p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{bc\\}\\s*=\\s*-2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|c_\\{bc\\}\\s*=\\s*-2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\),' chapters/examples/beta_gamma.tex chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
 succeeded in 51ms:
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
 succeeded in 51ms:
chapters/examples/beta_gamma.tex:315:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
chapters/examples/beta_gamma.tex:635:c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
chapters/examples/genus_expansions.tex:2380:$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
codex
The symbolic check command failed because this shell only has `python3`. I already have the canonical source open in `landscape_census.tex`, so I’m re-running the direct value check with `python3` and then patching the three live theorem-surface lines that still invite AP137 confusion.
exec
/bin/zsh -lc "sed -n '308,318p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '632,638p' chapters/examples/beta_gamma.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from fractions import Fraction
for lam in [Fraction(1,2), Fraction(1), Fraction(2), Fraction(3,2)]:
    c_bc = 1 - 3*(2*lam-1)**2
    c_bg = 2*(6*lam*lam - 6*lam + 1)
    print(f'lambda={lam}: c_bc={c_bc}, c_bg={c_bg}, sum={c_bc+c_bg}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 50ms:
\begin{equation}\label{eq:bg-bc-koszul}
c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
\qquad
c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
\qquad
c_{\beta\gamma} + c_{bc} = 0.
\end{equation}
 succeeded in 52ms:
lambda=1/2: c_bc=1, c_bg=-1, sum=0
lambda=1: c_bc=-2, c_bg=2, sum=0
lambda=2: c_bc=-26, c_bg=26, sum=0
lambda=3/2: c_bc=-11, c_bg=11, sum=0

thinking
**Reviewing edits and updates**

I need to inspect genus expansions around 2378, which I've already done. I think I should patch these three lines and focus on ordering as well. Before making the edits, I'll provide an update explaining what I'm changing. I also want to consider filling in the PE-8 cross-volume formula block since there's a shared formula that needs to be addressed. I'll make sure to do this in the commentary for clarity.
codex
```text
formula: bc/bg central charges
Vol I: live hits verified in chapters/standalone/compute; only notation drift on theorem surfaces in beta_gamma.tex and genus_expansions.tex
Vol II: live hits in bv_brst.tex, rosetta_stone.tex, thqg_symplectic_polarization.tex, ds_brst_sc_engine.py; all match canonical formulas or algebraically equivalent rewrites
Vol III: live hit in chapters/examples/toroidal_elliptic.tex; sign assignment is correct (+2 for beta-gamma, -2 for bc at lambda=1)
consistent? Y
canonical vol I, others updated same session? Y/NA
convention conversion: NA
verdict: ACCEPT
```

I’m applying a minimum patch now: only the live Vol I theorem/proposition surfaces that still write `c_{bc}` solely in the reduced `-2(6λ²-6λ+1)` form will be rewritten to show the canonical fermionic formula first. No code path or theorem status is changing.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex
@@ -2379,3 +2379,3 @@
 is a fermionic chiral algebra with central charge
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
+$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
 (Computation~\ref{comp:beta-gamma-central-charges}).
M /Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex
@@ -314,3 +314,3 @@
 For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
+$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
 \end{theorem}
@@ -634,3 +634,3 @@
 \qquad
-c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
+c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
 \qquad
apply_patch(auto_approved=true) exited 0 in 30ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex
M /Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex
file update:
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index e5c67c3ab9f095d38a8bd29ab55ab6162bd881ad..179b335ff6db32ae029d5905213ff6b8b013f161
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -312,7 +312,7 @@
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
 \]
 For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
+$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
 \end{theorem}
 
 \begin{computation}[Central charges for special cases]
@@ -632,7 +632,7 @@
 \begin{equation}\label{eq:bg-bc-koszul}
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
 \qquad
-c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
+c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
 \qquad
 c_{\beta\gamma} + c_{bc} = 0.
 \end{equation}
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0..1f631b671c5b6bc1cba834870c39f00281ea0a67
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -2377,7 +2377,7 @@
 
 The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
 is a fermionic chiral algebra with central charge
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
+$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
 (Computation~\ref{comp:beta-gamma-central-charges}).
 Its Koszul dual is the bosonic $\beta\gamma$-system at the same
 weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)

file update:
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index e5c67c3ab9f095d38a8bd29ab55ab6162bd881ad..179b335ff6db32ae029d5905213ff6b8b013f161
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -312,7 +312,7 @@
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
 \]
 For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
+$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
 \end{theorem}
 
 \begin{computation}[Central charges for special cases]
@@ -632,7 +632,7 @@
 \begin{equation}\label{eq:bg-bc-koszul}
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
 \qquad
-c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
+c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
 \qquad
 c_{\beta\gamma} + c_{bc} = 0.
 \end{equation}
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0..1f631b671c5b6bc1cba834870c39f00281ea0a67
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -2377,7 +2377,7 @@
 
 The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
 is a fermionic chiral algebra with central charge
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
+$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
 (Computation~\ref{comp:beta-gamma-central-charges}).
 Its Koszul dual is the bosonic $\beta\gamma$-system at the same
 weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)


thinking
**Searching for patterns**

I’m considering searching in chapters or standalone files, specifically in volumes 2 and 3, to check for wrong swap patterns. If I don’t find any, that would be great! I should also look at changed files for additional context. It feels like I’m covering all my bases here, which is reassuring. I'll make sure to keep an eye on everything as I navigate through those files!
codex
The patch is in. I’m doing the hostile reread now: targeted greps for swapped formulas across live source trees, then a narrow diff on the two edited TeX files to confirm I changed only the AP137-risk lines.
exec
/bin/zsh -lc 'git diff -- chapters/examples/beta_gamma.tex chapters/examples/genus_expansions.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '310,317p' chapters/examples/beta_gamma.tex && sed -n '632,638p' chapters/examples/beta_gamma.tex && sed -n '2378,2384p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden -S 'c_\\{bc\\}\\(.*\\)\\s*=\\s*2\\(6\\\\lambda\\"'^2 - 6'"\\\\lambda \\+ 1\\)|c_\\{\\\\beta\\\\gamma\\}\\(.*\\)\\s*=\\s*1 - 3\\(2\\\\lambda - 1\\)\\"'^2|c_'"\\{bc\\}\\s*=\\s*\\+2|c_\\{\\\\beta\\\\gamma\\}\\s*=\\s*-2' chapters standalone compute /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/chiral-bar-cobar-vol2/compute /Users/raeez/calabi-yau-quantum-groups/chapters /Users/raeez/calabi-yau-quantum-groups/compute" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index a6c6213..179b335 100644
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -1,5 +1,5 @@
 \chapter{\texorpdfstring{The $\beta\gamma$ system}{The beta-gamma system}}\label{chap:beta-gamma}
-% Regime I --- Quadratic (Convention~\ref{conv:regime-tags}).
+% Regime I: quadratic (Convention~\ref{conv:regime-tags}).
 
 A chiral algebra with a weight-zero generator violates every
 positive-grading hypothesis standard in the theory of vertex
@@ -60,7 +60,7 @@ D (modular char.) &
  $\kappa(\beta\gamma)
  = c/2 = 6\lambda^2{-}6\lambda{+}1$
  & Proved & Rem~\ref{rem:betagamma-shadow-archetype-free} \\
-H (Hochschild) &
+H (chiral Hochschild) &
  ChirHoch${}^*(\beta\gamma)$ polynomial
  & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
 \bottomrule
 succeeded in 52ms:
This generates the Virasoro algebra with central charge:
\[
c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
\]
For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
\end{theorem}

\begin{equation}\label{eq:bg-bc-koszul}
c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
\qquad
c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
\qquad
c_{\beta\gamma} + c_{bc} = 0.
\end{equation}
The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
is a fermionic chiral algebra with central charge
$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
(Computation~\ref{comp:beta-gamma-central-charges}).
Its Koszul dual is the bosonic $\beta\gamma$-system at the same
 succeeded in 51ms:
compute/audit/wrong_formulas_blacklist_wave12.md:54:- WRONG:    `c_{bc}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)`
compute/audit/wrong_formulas_blacklist_wave12.md:61:- WRONG:    `c_{\beta\gamma}(\lambda) = 1 - 3(2\lambda - 1)^2`
file update:
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index e5c67c3ab9f095d38a8bd29ab55ab6162bd881ad..179b335ff6db32ae029d5905213ff6b8b013f161
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -312,7 +312,7 @@
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
 \]
 For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
+$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
 \end{theorem}
 
 \begin{computation}[Central charges for special cases]
@@ -632,7 +632,7 @@
 \begin{equation}\label{eq:bg-bc-koszul}
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
 \qquad
-c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
+c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
 \qquad
 c_{\beta\gamma} + c_{bc} = 0.
 \end{equation}
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0..1f631b671c5b6bc1cba834870c39f00281ea0a67
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -2377,7 +2377,7 @@
 
 The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
 is a fermionic chiral algebra with central charge
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
+$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
 (Computation~\ref{comp:beta-gamma-central-charges}).
 Its Koszul dual is the bosonic $\beta\gamma$-system at the same
 weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)

codex
The live-source grep is clean: the only remaining wrong-shape matches are in the blacklist audit file, where they are explicitly marked `WRONG`. I’m extracting exact line numbers from the patched sources now so the final report can list each problem and the exact edit applied, and I’ll call out separately that Vol II and Vol III required no live fixes.
exec
/bin/zsh -lc "nl -ba chapters/examples/genus_expansions.tex | sed -n '2378,2384p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '310,317p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/beta_gamma.tex | sed -n '632,638p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2378	The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
  2379	is a fermionic chiral algebra with central charge
  2380	$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
  2381	(Computation~\ref{comp:beta-gamma-central-charges}).
  2382	Its Koszul dual is the bosonic $\beta\gamma$-system at the same
  2383	weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)
  2384	= -c_{bc}$, and the underlying operadic duality is
 succeeded in 52ms:
   310	This generates the Virasoro algebra with central charge:
   311	\[
   312	c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
   313	\]
   314	For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
   315	$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
   316	\end{theorem}
   317	
 succeeded in 52ms:
   632	\begin{equation}\label{eq:bg-bc-koszul}
   633	c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
   634	\qquad
   635	c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
   636	\qquad
   637	c_{\beta\gamma} + c_{bc} = 0.
   638	\end{equation}
file update:
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index e5c67c3ab9f095d38a8bd29ab55ab6162bd881ad..179b335ff6db32ae029d5905213ff6b8b013f161
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -312,7 +312,7 @@
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
 \]
 For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
+$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
 \end{theorem}
 
 \begin{computation}[Central charges for special cases]
@@ -632,7 +632,7 @@
 \begin{equation}\label{eq:bg-bc-koszul}
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
 \qquad
-c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
+c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
 \qquad
 c_{\beta\gamma} + c_{bc} = 0.
 \end{equation}
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0..1f631b671c5b6bc1cba834870c39f00281ea0a67
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -2377,7 +2377,7 @@
 
 The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
 is a fermionic chiral algebra with central charge
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
+$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
 (Computation~\ref{comp:beta-gamma-central-charges}).
 Its Koszul dual is the bosonic $\beta\gamma$-system at the same
 weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)






thinking
**Addressing git diffs**

I noticed that `git diff` showed unrelated pre-existing changes in the same files, which is important to clarify. I left those untouched to avoid confusion. It's not clear if those diffs were there before my changes. I should mention that both edited files had unrelated pre-existing changes and I only modified the three central charge lines. The user asked for a format like "PROBLEM at file:line," so I plan to format a list for clarity in reporting the adjustments made.
thinking
**Detailing edits and verifications**

I specifically changed the equation from `$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$` to `$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$`, and I made similar changes to the other two lines. I should mention that across the live Vol II/III sources, no swapped formulas remained. I verified the values at λ=1/2, 1, 3/2, and 2, which gave (1,-1), (-2,2), (-11,11), and (-26,26). I need to keep this concise for clarity.
thinking
**Organizing audit findings**

I want to clarify that there are no live edits in Vol II/III. I should mention the deliberate exclusion of audit and blacklist historical files. A grep search found only the wrong-shape matches in `compute/audit/wrong_formulas_blacklist_wave12.md`, which are correctly marked as WRONG. It might be helpful to state: “No live AP137 swap survived in Vol II/III." 

Considering verification, I've searched through all three volumes, confirming the only remaining wrong-shape matches are in the audit blacklist.
thinking
**Structuring file findings**

I need to remember that local file links require an absolute path, so I’ll organize my findings into three bullets. For example, I could format it like this:

- PROBLEM at [beta_gamma.tex](/Users/.../beta_gamma.tex:315): the theorem surface gives `c_{bc}` only as `-2(6λ²-6λ+1)`, which is algebraically correct but can confuse AP137 by obscuring the canonical fermionic form. 
  EXACT edit applied: changed `$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$` to `$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$`.

I’ll avoid nested bullets and could present each finding as a numbered list with two separate lines for clarity.
thinking
**Checking verification process**

I need to clarify that I didn’t run a full TeX build; instead, I verified things by using grep and direct value checks. If I didn't run tests, I should definitely inform the user. Yes, that’s a good point. Also, I should make sure the final message doesn’t start with “Done.” It might be better to begin with something like "Findings." That seems like a more engaging way to present the information!
codex
**Findings**

1. PROBLEM at [beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:315): the theorem surface stated the fermionic `bc` central charge only in the reduced form `-2(6\lambda^2 - 6\lambda + 1)`. That value is correct, but it is AP137-prone because it hides the canonical fermionic formula and makes bc/bg swaps easier. EXACT edit applied: changed
`$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.`
to
`$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.`

2. PROBLEM at [beta_gamma.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/beta_gamma.tex:635): the Koszul-complementarity equation had the same AP137-prone `bc`-only reduced form. EXACT edit applied: changed
`c_{bc} = -2(6\lambda^2 - 6\lambda + 1),`
to
`c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),`

3. PROBLEM at [genus_expansions.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:2380): the genus-expansion summary led with the reduced `bc` polynomial instead of the canonical fermionic formula. EXACT edit applied: changed
`$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$`
to
`$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$`

Across the live source trees of Vol I, Vol II, and Vol III, I found no surviving swapped bc/bg formulas. Vol II and Vol III needed no live edits. The only remaining wrong-shape literals are in [wrong_formulas_blacklist_wave12.md](/Users/raeez/chiral-bar-cobar/compute/audit/wrong_formulas_blacklist_wave12.md:54), where they are intentionally recorded as `WRONG`.

Verification was grep plus direct value checks at `\lambda = 1/2, 1, 3/2, 2`, giving `(c_bc, c_bg) = (1,-1), (-2,2), (-11,11), (-26,26)`. I did not run a full TeX build.
file update:
diff --git a/chapters/examples/beta_gamma.tex b/chapters/examples/beta_gamma.tex
index e5c67c3ab9f095d38a8bd29ab55ab6162bd881ad..179b335ff6db32ae029d5905213ff6b8b013f161
--- a/chapters/examples/beta_gamma.tex
+++ b/chapters/examples/beta_gamma.tex
@@ -312,7 +312,7 @@
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1) \quad \text{(bosonic $\beta\gamma$)}
 \]
 For the \emph{fermionic} $bc$ system with the same conformal weights, the sign reverses:
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1)$.
+$c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1)$.
 \end{theorem}
 
 \begin{computation}[Central charges for special cases]
@@ -632,7 +632,7 @@
 \begin{equation}\label{eq:bg-bc-koszul}
 c_{\beta\gamma} = +2(6\lambda^2 - 6\lambda + 1),
 \qquad
-c_{bc} = -2(6\lambda^2 - 6\lambda + 1),
+c_{bc} = 1 - 3(2\lambda - 1)^2 = -2(6\lambda^2 - 6\lambda + 1),
 \qquad
 c_{\beta\gamma} + c_{bc} = 0.
 \end{equation}
diff --git a/chapters/examples/genus_expansions.tex b/chapters/examples/genus_expansions.tex
index c7ab514fe66fbefcfdbee3da4d15e9cb6d08eba0..1f631b671c5b6bc1cba834870c39f00281ea0a67
--- a/chapters/examples/genus_expansions.tex
+++ b/chapters/examples/genus_expansions.tex
@@ -2377,7 +2377,7 @@
 
 The $bc$ system at conformal weights $(\lambda, 1-\lambda)$
 is a fermionic chiral algebra with central charge
-$c_{bc} = -2(6\lambda^2 - 6\lambda + 1) = 1 - 3(2\lambda-1)^2$
+$c_{bc} = 1 - 3(2\lambda-1)^2 = -2(6\lambda^2 - 6\lambda + 1)$
 (Computation~\ref{comp:beta-gamma-central-charges}).
 Its Koszul dual is the bosonic $\beta\gamma$-system at the same
 weights, with $c_{\beta\gamma} = 2(6\lambda^2 - 6\lambda + 1)

tokens used
157,523
