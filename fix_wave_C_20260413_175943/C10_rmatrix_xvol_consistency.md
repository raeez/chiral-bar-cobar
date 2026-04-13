# C10_rmatrix_xvol_consistency (1180s)

Writes were only permitted inside `~/chiral-bar-cobar`, so I patched Vol I directly, audited Vol II/III, and isolated the remaining Vol II fixes that are still live but blocked by the sandbox. Vol III’s live chapter surfaces did not show a KM/Heis/Vir `r`-matrix inconsistency in this sweep.

1. PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1431), [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1507), [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1645): Heisenberg was advertised as `k\,\Omega/z`, and the Virasoro tier summary used a non-canonical shorthand instead of `(c/2)/z^3 + 2T/z`. EXACT edit applied: replaced those surfaces with `r(z)=k/z`, `r_{\cH_k}(z)=k/z`, and `r(z)=(c/2)/z^3 + 2T/z`, and rewrote the surrounding prose so Heisenberg is explicitly scalar rather than Casimir-valued.

2. PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27801): the Virasoro self-duality paragraph inserted a fake Casimir, `r(z)=\kappa\,\Omega/z^3+2T/z`. EXACT edit applied: replaced it with `r(z)=\kappa/z^3+2T/z` and rewrote the explanation to say the cubic pole is already scalar.

3. PROBLEM at [yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:745), [yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:801), [yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:866): the file switched between KZ `\Omega/((k+h^\vee)z)` and trace-form `k\Omega/z` without stating the bridge, and a later confirmation line reverted to bare `k\Omega/z`. EXACT edit applied: inserted `k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)` at the theorem statement, rewrote the proof line as `r(z)=k\,\Omega_{\mathrm{tr}}/z=\Omega_\fg/((k+h^\vee)z)`, and rewrote the later `\mathfrak{sl}_2` confirmation the same way.

4. PROBLEM at [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:578), [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:595), [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:604): the Sklyanin face compared Drinfeld trace-form `k\Omega/z` to KZ-normalized collision residue `\Omega/((k+h^\vee)z)` without an explicit bridge. EXACT edit applied: normalized the Drinfeld side to `k\Omega_{\mathrm{tr}}/z` and inserted the bridge `k\,\Omega_{\mathrm{tr}}=\Omega/((k+h^\vee)z)` in both the theorem statement and proof.

5. PROBLEM at [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1713), [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4765): the file identified the collision residue once in KZ form and later again in trace-form without stating the equivalence. EXACT edit applied: rewrote both collision-residue displays as `\Omega/((k+h^\vee)z)=k\,\Omega_{\mathrm{tr}}/z` and added the normalization note at the later occurrence.

6. PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807): Vol II still says “Classical `r`-matrix: `r(z)=k/z^2`” immediately before `R(z)=\exp(k\hbar/z)`, so it conflates Laplace kernel with collision residue. EXACT edit blocked by sandbox: replace that bullet with `Laplace kernel: r^L(z)=k/z^2; collision residue: r^{\mathrm{coll}}(z)=k/z`, and replace the next sentence so `R(z)` exponentiates `r^{\mathrm{coll}}`, not `k/z^2`.

7. PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1529): Vol II switches from trace-form `k\,\Omega/z` to KZ `\Omega/(k+h^\vee)` with no bridge identity. EXACT edit blocked by sandbox: insert `On the affine Kac--Moody comparison surface, the same simple-pole term is written in KZ normalization as \Omega/((k+h^\vee)z); equivalently, k\,\Omega_{\mathrm{tr}}/z=\Omega/((k+h^\vee)z) at generic k.`

8. PROBLEM at [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:128): the Heisenberg verification line says `r(z)=k/z^2` while the Virasoro line in the same proof is correctly labeled as Laplace-vs-collision. EXACT edit blocked by sandbox: replace it with `Laplace kernel r^L(z)=k/z^2` and add `collision residue r^{\mathrm{coll}}(z)=k/z`.

9. PROBLEM at [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:319), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380): the Heisenberg proposition and remark call `k/z^2` the `r`-matrix even though the same proof derives `r^{\mathrm{coll}}(z)=k/z` at lines 350-356. EXACT edit blocked by sandbox: rename the statement to “OPE kernel and collision residue” and replace the formula by `r^L_{\cH_k}(z)=k/z^2`, `r^{\mathrm{coll}}_{\cH_k}(z)=k/z`, then rewrite the remark so the complete classical datum is `r^{\mathrm{coll}}(z)=k/z`, not `k/z^2`.

10. PROBLEM at [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:402), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:476), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:547), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:791): the affine subsection mixes a KZ simple pole, a trace-form CYBE check, and a Laplace table row without a single declared bridge. EXACT edit blocked by sandbox: rewrite the affine theorem as `r^L_{\widehat{\fg}_k}(z)=\Omega/((k+h^\vee)z)+k\kappa/z^2`, `r^{\mathrm{coll}}_{\widehat{\fg}_k}(z)=\Omega/((k+h^\vee)z)`, add `k\,\Omega_{\mathrm{tr}}=\Omega/((k+h^\vee)z)`, and normalize the `\mathfrak{sl}_2` remark/table to the same convention.

11. PROBLEM at [ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403): the genus-zero package says `r(z)=k/z^2` even though the same file identifies `r(z)` with `\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)` earlier at lines 2344-2345. EXACT edit blocked by sandbox: replace `r(z)=k/z^2` with `r(z)=k/z`.

12. PROBLEM at [ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309): same Heisenberg collision-residue bug as the retained mirror file. EXACT edit blocked by sandbox: replace `r(z)=k/z^2` with `r(z)=k/z`.

Verification: the negative grep for `Heisenberg.*Omega/z`, `r_{\cH_k}(z)=k\Omega/z`, and `\kappa\,\Omega/z^3` now returns no hits in the patched Vol I files. I did not run a TeX build; the cross-volume verification here was line-level source audit plus targeted grep.


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
session id: 019d87a1-8cfa-78e2-af98-c971e20a2c7a
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


Cross-volume r-matrix convention consistency.
For each family (KM, Heis, Vir): grep all three volumes for r-matrix formulas.
Verify: (a) level prefix present, (b) same convention (trace-form or KZ) within each file,
(c) bridge identity stated when conventions switch. Fix inconsistencies.
mcp startup: no servers
codex
Scope is the cross-volume `r`-matrix surface for KM, Heisenberg, and Virasoro. I’m reading the required constitutional files and locating every `r`-matrix occurrence across Volumes I–III before I patch anything.
exec
/bin/zsh -lc "sed -n '1,240p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 50ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3113 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2367 |
 succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 exited 1 in 51ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
 succeeded in 51ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits

 succeeded in 52ms:
 M CLAUDE.md
 M Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
 M Makefile
 M N1_koszul_meta.pdf
 M N2_mc3_all_types.pdf
 M N3_e1_primacy.pdf
 M N4_mc4_completion.pdf
 M N5_mc5_sewing.pdf
 M N6_shadow_formality.pdf
 M README.md
 M appendices/_sl2_yangian_insert.tex
 M appendices/ordered_associative_chiral_kd.tex
 M bibliography/references.tex
 M bp_self_duality.pdf
 M chapters/connections/bv_brst.tex
 D chapters/connections/casimir_divisor_core_transport.tex
 M chapters/connections/concordance.tex
 D chapters/connections/dg_shifted_factorization_bridge.tex
 M chapters/connections/editorial_constitution.tex
 M chapters/connections/frontier_modular_holography_platonic.tex
collab spawn_agent(call_r2xxWVbj8JnzlFPC849B5PFD, prompt="Audit the cross-volume r-matrix convention surface for KM, Heis, and Vir. Search Vol I at /Users/raeez/chiral-bar-cobar,…")
mcp startup: no servers
spawn_agent(call_r2xxWVbj8JnzlFPC849B5PFD, prompt="Audit the cross-volume r-matrix convention surface for KM, Heis, and Vir. Search Vol I at /Users/raeez/chiral-bar-cobar,…") pending init:
  agent: 019d87a1-de83-74c1-8295-501c295d3354
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
N3_e1_primacy.pdf
N4_mc4_completion.pdf
N5_mc5_sewing.pdf
N6_shadow_formality.pdf
README.md
appendices
archive
audit
audit_campaign_20260412_230832
audit_campaign_20260412_231034
audit_campaign_20260413_111534
audit_campaign_20260413_163450
exec
/bin/zsh -lc "sed -n '1,160p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
/bin/zsh -lc "sed -n '1,200p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: cross-volume-propagation
description: Use after any mathematical wording, status, label, terminology, or formula change that may recur across Volumes I, II, and III, compute layers, tests, notes, or superseded files. This is the Codex-native equivalent of `/propagate` from `CLAUDE.md`.
---

# Cross-Volume Propagation

This skill exists to stop local truth from coexisting with global drift.

## Sweep

Search all live surfaces that may still advertise the old claim:

- `~/chiral-bar-cobar`
- `~/chiral-bar-cobar-vol2`
- `~/calabi-yau-quantum-groups`
- `compute/`
- `compute/tests/`
- relevant notes, standalones, or superseded files if they still mislead future audits

codex
I’ve got the constitutional surface and the repo is dirty, so I’ll isolate edits carefully. The required red-team file wasn’t at the primary path; I’m locating the archive copy while the explorer builds the cross-volume hit list.
exec
/bin/zsh -lc "rg --files -g 'red_team_summary.md' -g '"'!**/.git/**'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups /Users/raeez/chiral-bar-cobar/archive" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/archive/raeeznotes/raeeznotes100/red_team_summary.md
collab wait(call_WasuM6UqiQagfEWSa260pqoo)
  receivers: 019d87a1-de83-74c1-8295-501c295d3354

thinking
**Evaluating skill usage and planning multi-volume search**

I'm weighing whether the user’s audit on cross-volume r-matrix surfaces requires skill use; it seems more like a search task than skill application, so I lean against using skills here. I’m preparing to run ripgrep searches for r-matrix formula references across several volume directories, aiming to find files with r(z) or r^{KM}, r^{Heis}, r^{Vir} patterns, noting line numbers and conventions to audit cross-volume consistency.
exec
/bin/zsh -lc "rg -n \"r\\"'^KM"' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
AGENTS.md:167:r^KM(z) = k*Omega/z           [trace-form]            # k=0→0; k=-h^v→finite
AGENTS.md:168:r^KM(z) = Omega/((k+h^v)*z)   [KZ]                    # k=0→Omega/(h^v*z)!=0; k=-h^v→diverges
scripts/healing_fortification_40.py:589:2. r^KM(z) = k*Omega/z — level prefix present
elite_rescue_20260413_141402/X02_formula_3vol.md:58:kappa(KM), kappa(Vir), kappa(Heis), kappa(W_N), r^KM(z), r^Vir(z),
relaunch_20260413_111534/XV10_convention_bridge.md:249:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
scripts/elite_rescue_40.py:148:1. Our R-matrix r^KM(z) = k*Omega/z: consistent with EF's KZ connection?
scripts/elite_rescue_40.py:318:kappa(KM), kappa(Vir), kappa(Heis), kappa(W_N), r^KM(z), r^Vir(z),
audit_campaign_20260412_231034/XV10_convention_bridge.md:198:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
elite_rescue_20260413_141402/L06_EF_comparison.md:59:1. Our R-matrix r^KM(z) = k*Omega/z: consistent with EF's KZ connection?
CLAUDE.md:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
audit_campaign_20260412_230832/F05_r_KM.md:54:CANONICAL: r^KM(z) = k*Omega/z [trace-form]
scripts/adversarial_campaign.py:172:    ("F05_r_KM", "r^KM(z) = k*Omega/z [trace-form]", "KM r-matrix", "grep -rn 'Omega.*z\\|r(z).*Omega' chapters/ | head -50", "k=0→0. WRONG: Omega/z (bare, AP126)"),
healing_20260413_130533/H27_cross_vol_formula_heal.md:64:2. r^KM(z) = k*Omega/z — level prefix present
healing_20260413_132214/H27_cross_vol_formula_heal.md:86:2. r^KM(z) = k*Omega/z — level prefix present
audit_campaign_20260412_231034/F05_r_KM.md:80:CANONICAL: r^KM(z) = k*Omega/z [trace-form]
audit_campaign_20260412_231034/F05_r_KM.md:150:CLAUDE.md:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
audit_campaign_20260412_231034/F05_r_KM.md:170:The canonical surface is consistent so far: `CLAUDE.md` explicitly records both conventions and the AP126 falsifier, namely `trace-form r^KM(z)=kΩ/z` with the mandatory `k=0 -> 0` check. Next I’m enumerating actual manuscript occurrences, including cases that may be hidden behind alternative notation (`r_k`, `r^{cl}`, `r_{KZ}`, `\hbar Ω/z`) rather than the exact string `kΩ/z`.
audit_campaign_20260412_231034/F02_kappa_Vir.md:247:CLAUDE.md:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
fix_wave_B_20260413_171623/B03_status_audit_theory_2.md:197:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
compute/lib/feynman_bar_matching_engine.py:59:    r^KM(z) = k * Omega / z
exec
/bin/zsh -lc "rg -n \"r\\"'^Heis"' in /Users/raeez/chiral-bar-cobar succeeded in 60ms:
compute/tests/test_rmatrix_landscape.py:1017:        """r^Heis(z) = k/z must vanish at k=0 (AP141)."""
wait(call_WasuM6UqiQagfEWSa260pqoo) timed out:
exec
/bin/zsh -lc "rg -n \"r\\"'^KM" chapters' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"r\\"'^{KM" -g"*.tex" -n' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:r\^{KM)
           ^
error: repetition quantifier expects a valid decimal
codex
Using `multi-path-verify` to check each family against independent conventions and `cross-volume-propagation` to sweep every live duplicate across the three volumes. Next I’m reading the archived red-team summary, then I’ll compare the explorer’s file map against direct grep results before I edit.
exec
/bin/zsh -lc "rg -n 'r\\"'^'"\\{KM\\}' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

Plan update
Cross-volume r-matrix audit needs a locked claim surface, a complete grep census, then minimal propagation edits with narrow verification.
  → Read required repo constitutions and canonical r-matrix references, including the archived red-team summary and live census files.
  • Enumerate every KM, Heis, and Vir r-matrix formula across Volumes I–III; classify convention use per file and identify missing level prefixes or missing bridge identities.
  • Apply minimum truthful edits only to files with inconsistencies, preserving each file’s chosen convention and adding the bridge identity where a file switches conventions.
  • Run cross-volume verification grep and targeted checks for forbidden bare formulas, then summarize findings and exact edits by file:line.
exec
/bin/zsh -lc "rg -n \"k\\*Omega/z\" -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'ls chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
connections
examples
frame
theory
exec
/bin/zsh -lc "rg -n \"r\\(z\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 505

chapters/examples/w_algebras_deep.tex:2753:$\mathfrak{T} = (\cA,\, \cA^!,\, r(z))$, where:
chapters/examples/w_algebras_deep.tex:2757:\item $r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
chapters/examples/w_algebras_deep.tex:2778:The modular Koszul triple $(\cA, \cA^!, r(z))$ is
chapters/examples/w_algebras_deep.tex:2788:= (\cA, \cA^!, C, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$
chapters/examples/w_algebras_deep.tex:2792:(\cA,\, \cA^!,\, r(z))
chapters/examples/lattice_foundations.tex:5003:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
chapters/examples/lattice_foundations.tex:5018:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
chapters/examples/lattice_foundations.tex:5022:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
chapters/examples/beta_gamma.tex:88:$r$-matrix $r(z)$ & $0$ (OPE simple pole absorbed by $d\log$) \\
chapters/examples/beta_gamma.tex:106:r(z) = 0\,\bigr).
chapters/examples/beta_gamma.tex:2787:explicit rational $r$-matrix $r(z)$. This subsection makes concrete,
chapters/examples/beta_gamma.tex:2820: r(z)
chapters/examples/beta_gamma.tex:2928: r(z) \;=\; \tau_z
chapters/examples/beta_gamma.tex:2932:In particular, the classical Yang--Baxter equation for $r(z)$ is a
chapters/examples/beta_gamma.tex:2978:$r(z) = \Theta_{\beta\gamma}\big|_{g=0,\,n=2,\,z}$.
chapters/examples/y_algebras.tex:621:r(z) \;=\;
chapters/examples/y_algebras.tex:631:$\mathrm{av}(r(z)) = \kappa = \Psi$, recovering the
chapters/examples/y_algebras.tex:854:$\cH(T) = (A, A^!, \mathfrak{C}, r(z), \Theta_A, \nabla^{\mathrm{hol}})$
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "rg -n \"r\\"'^'"\\{?(KM|Heis|Vir)|r\\"'^KM|r'"\\"'^Heis|r'"\\"'^Vir|k'"\\\\Omega/z|Omega/\\\\(\\\\(k\\+h\\"'^v'"\\\\)\\*z\\\\)|Omega/\\\\(\\(k\\+h\\"'^v'"\\)z\\)|\\\\Omega/z|k/z|c/2\\)/z\\"'^3|R-matrix|r-matrix|classical r-matrix" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups --glob '"'*.tex' --glob '*.md'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"C9|C10|C11|Bridge identity|k\\*Omega_tr|Omega/\\(\\(k\\+h\\"'^v'"\\)\\*z\\)|Omega/\\(\\(k\\+h\\"'^v'"\\)z\\)|r\\"'^KM|r'"\\"'^Heis|r'"\\"'^Vir" landscape_census.tex CLAUDE.md chapters -g '"'*.tex' -g '*.md'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:r\^\{?(KM|Heis|Vir)|r\^KM|r\^Heis|r\^Vir|k\Omega/z|Omega/\(\(k\+h\^v\)\*z\)|Omega/\(\(k\+h\^v\)z\)|\Omega/z|k/z|c/2\)/z\^3|R-matrix|r-matrix|classical r-matrix)
                                                 ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: landscape_census.tex: No such file or directory (os error 2)
CLAUDE.md:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
CLAUDE.md:237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
CLAUDE.md:239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
CLAUDE.md:241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
CLAUDE.md:290:- B2. `r^Vir(z) = (c/2)/z^4` (quartic). CORRECT: `(c/2)/z^3 + 2T/z`. AP19/AP21.
CLAUDE.md:291:- B3. `r^Vir(z) = (c/2)/z^2`. CORRECT: cubic + simple. AP19/AP27.
CLAUDE.md:666:convention:                [trace-form k*Omega/z / KZ Omega/((k+h^v)*z)]
CLAUDE.md:897:AP144: Convention coexistence without bridge. Different chapters independently develop conventions for the same object (r-matrix: trace-form k*Omega/z vs KZ Omega/((k+h^v)*z); kappa: several families). The conventions agree at generic parameter values but diverge at boundary values (k=0, k=-h^v). When multiple conventions coexist, a BRIDGE IDENTITY must be stated explicitly at every site, and boundary behavior must be checked in EACH convention separately. The r-matrix normalization issue (C9/C13/AP126 inconsistency, resolved April 2026) is the canonical example. After introducing ANY convention for a shared object, grep all three volumes for alternative conventions of the same object and install bridge identities.
CLAUDE.md:901:AP148: r-matrix normalization is convention-dependent (see corrected C9). Two conventions for affine KM: trace-form r(z)=k*Omega/z (AP126 k=0 check applies; av(r)=kappa_dp only; Sugawara shift dim(g)/2 needed for full kappa) and KZ r(z)=Omega/((k+h^v)*z) (k=0 gives nonzero for non-abelian; av not simply related to kappa). Bridge: k*Omega_tr = Omega/(k+h^v) at generic k. BEFORE writing any r-matrix formula for affine KM, state which convention and verify boundary behavior in that convention.
chapters/examples/landscape_census.tex:229:% Omega/((k+h^v)z) with Omega = sum kappa^{ab} I_a otimes I_b;
chapters/examples/landscape_census.tex:230:% the identification k*Omega_tr = Omega/(k+h^v) reconciles the two.
chapters/theory/derived_langlands.tex:71:% Two conventions: k*Omega_tr/z (finite at critical level, trace-form)
chapters/theory/derived_langlands.tex:72:% vs Omega/((k+h^v)*z) (diverges at critical level, KZ). Same physics.
chapters/theory/derived_langlands.tex:827:% In the trace-form convention: r = k*Omega_tr/z, finite at k=-h^v.
chapters/theory/en_koszul_duality.tex:4933:% AP126/AP148: KZ convention r(z) = Omega/((k+h^v)z).
collab wait(call_kGv650W3725ggsTCDDUR3ycX)
  receivers: 019d87a1-de83-74c1-8295-501c295d3354

thinking
**Planning detailed cross-volume r-matrix audit**

I'm working out a strategy to systematically find and catalog every file across Volumes I, II, and III that contains r-matrix formulas or bridging identities for KM, Heis, and Vir families. I want to identify which conventions each file uses, flag missing level prefixes, and note files that switch conventions without clear bridges—all while managing the potentially large number of matches by focusing on core canonical files and searching smartly with regex patterns and keyword filters.
exec
/bin/zsh -lc "rg -n \"k\\\\Omega/z\" -l chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:k\Omega/z)
        ^^
error: unrecognized escape sequence
wait(call_kGv650W3725ggsTCDDUR3ycX) timed out:
exec
/bin/zsh -lc "rg -n 'k\\\\Omega/z' -l chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex
chapters/examples/yangians_foundations.tex
chapters/examples/bar_complex_tables.tex
chapters/examples/yangians_drinfeld_kohno.tex
chapters/examples/yangians_computations.tex
chapters/examples/genus_expansions.tex
chapters/frame/preface_sections10_13_draft.tex
chapters/frame/preface_section1_v2.tex
chapters/connections/holographic_datum_master.tex
chapters/frame/preface_section1_draft.tex
chapters/frame/preface_sections5_9_draft.tex
chapters/connections/frontier_modular_holography_platonic.tex
chapters/theory/e1_modular_koszul.tex
chapters/theory/algebraic_foundations.tex
chapters/theory/introduction.tex
chapters/theory/chiral_koszul_pairs.tex
exec
/bin/zsh -lc "sed -n '70,140p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\bottomrule
\end{tabular}
\end{table}

\begin{table}[ht]
\centering
\small
\caption{Shadow archetype data for affine
Kac--Moody.}\label{tab:km-shadow-archetype}
\begin{tabular}{ll}
\toprule
\textbf{Invariant} & \textbf{Value} \\
\midrule
Class & L (Lie/tree) \\
Shadow depth $r_{\max}$ & $3$ \\
$\kappa(\widehat{\fg}_k)$ &
 $\dim(\fg)(k{+}h^\vee)/(2h^\vee)$ \\
Cubic shadow $\mathfrak{C}$ &
 $\kappa(x,[y,z])$ (Lie bracket) \\
Quartic $o_4$ & $0$ (Jacobi identity) \\
exec
/bin/zsh -lc "rg -n 'k\\\\Omega' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
765:same object in the equivalent form $k\Omega_{\mathrm{tr}}/z$, where
769:identification $k\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$.
exec
/bin/zsh -lc "sed -n '730,800p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{equation}\label{eq:km-rmatrix}
r^{\mathrm{KM}}_{\hat\fg_k}(z) = \frac{\Omega}{(k + h^\vee)\,z},
\qquad
\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b,
\end{equation}
which has a single simple pole, regardless of the rank of~$\fg$.
The factor $(k + h^\vee)^{-1}$ reflects the level-shifted
inverse Killing form; at the critical level $k = -h^\vee$,
the $r$-matrix degenerates (Sugawara singularity).

The $r$-matrix $r(z) = \Omega/((k{+}h^\vee)\,z)$ satisfies the classical
Yang--Baxter equation, which reduces via partial fractions to
the infinitesimal braid relation
$[\Omega_{ij}, \Omega_{ik} + \Omega_{jk}] = 0$
for all distinct triples $(i,j,k)$
(Proposition~\ref{prop:cybe-from-mc}).

\emph{Convention.}
This chapter uses the \emph{KZ normalization} throughout:
\[
exec
/bin/zsh -lc "sed -n '20,80p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ \\
\textbf{Central charge} & $c = 1$ \\
\textbf{Shadow archetype} & G (Gaussian), $r_{\max} = 2$ \\
\textbf{Modular characteristic} & $\kappa(\cH_\kappa) = \kappa$ \\
\textbf{Koszul dual} & $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$,
$\kappa(\cH_\kappa^!) = -\kappa$ \\
\textbf{Complementarity} & $\kappa_{\mathrm{Heis}}(\cH_\kappa) + \kappa_{\mathrm{Heis}}(\cH_\kappa^!) = 0$ \textup{(}free-field type~I\textup{)} \\
\textbf{$r$-matrix} & $r(z) = \kappa/z$ (single pole, no Lie bracket) \\
\textbf{Genus expansion} & $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ GF $= (\kappa/\hbar^2)(\hat{A}(i\hbar) - 1)$
\end{tabular}
\end{center}

\noindent
The modular Koszul triple
(Definition~\ref{def:modular-koszul-triple}) of the Heisenberg
algebra is
\begin{equation}\label{eq:heisenberg-triple}
\mathfrak{T}_{\cH}
\;=\;
\bigl(\,\cH_\kappa,\;\;
codex
The initial grep needs a narrower pass; I’m splitting it by family and by convention so I can classify each file cleanly instead of mixing prose mentions with formulas. I’ll also pull the live census lines from `chapters/examples/landscape_census.tex`, since that is the canonical local source for the KM bridge.
exec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -e 'r\\"'^Heis'"' -e 'k/z' -e 'Heisenberg classical r-matrix' -e 'Heisenberg.*R-matrix' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -e 'r\\"'^Vir'"' -e '\\(c/2\\)/z\\"'^3'"' -e '2T/z' -e 'Virasoro.*r-matrix' -e 'Virasoro.*R-matrix' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' --glob '*.md' -e 'k\\*\\\\Omega' -e '\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\*?z\\)' -e 'r\\"'^KM'"' -e 'classical r-matrix' -e 'R-matrix' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 913

/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:668:r^Heis(z) = k/z
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:185:V2-AP7: Heisenberg R-matrix = exp(k*hbar/z), NOT trivial. Collision residue k/z. Monodromy exp(-2pi*i*k).
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:500:The bar-theoretic collision residue is $r^{\mathrm{coll}}(z) = k/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2026:$r^L(z)$\,$^*$ & $k/z^2$ & $1/z^2$ & n/a & $k/z^2$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/standalone/preface_full_survey.tex:439:(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1192:The collision residue is $r^{\mathrm{coll}}(z) = k/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1195:\leadsto k/z$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1335:The collision residue is $r^{\mathrm{coll}}(z) = k/z$ (the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1337:$k/(z-w)^2 \cdot d\log(z-w) \leadsto k/z$). The
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1746: $R(z) = \exp(k\hbar/z)$ with collision residue $k/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5330: while Heisenberg has $R(z) = e^{k/z}$ (scalar).
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:14085:  + \tfrac{1}{2}(3\hbar k/z)^2\,\Omega^2
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:14090:integrating $(3\hbar k/z)^2\,\Omega^2/2$ over the
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:15673:Contrast: Heisenberg $R = \exp(k/z)$ (full exponential);
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:16376:L & Heisenberg & $0$ & Decoupled & $Z = \eta^{-k}$, $R = e^{k/z}$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:3174: free field, $r = k/z$ \\[2pt]
 succeeded in 51ms:
Total output lines: 865

/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:669:r^Vir(z) = (c/2)/z^3 + 2T/z
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:713:(c/2)/z^4                             # Virasoro quartic r-matrix term
/Users/raeez/chiral-bar-cobar-vol2/compute/audit/linear_read_notes.md:1203:   Verification: the Virasoro IS chirally Koszul (confirmed in `preface.tex:835`, `examples-worked.tex:160`); both duals coincide because the Virasoro Laplace kernel has higher-order poles incompatible with a simple-pole Yangian r-matrix.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_celestial_cy.tex:531: % r(z) = (c/2)/z^3 + 2T/z.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:504:% Collision residue: r^{coll}(z) = (c/2)/z^3 + 2T/z (poles at odd orders).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:544:The collision residue $r^{\mathrm{coll}}(z) = (c/2)/z^3\,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:545:\mathbf{1}\otimes\mathbf{1} + 2T/z\otimes\mathbf{1}$ has pole
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:567:$r$-matrix & $\Omega_\fg/z$ & $(c/2)/z^3 + 2T/z$ \\[3pt]
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:576:$r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$.  The coproduct carries
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:606:$\infty$.  $r$-matrix: $r(z) = (c/2)/z^3 + 2T/z$ (two poles,
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:758:$R(z) = 1 + \hbar\,((c/2)/z^3 + 2T/z) + O(\hbar^2)$.
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1348:r(z) \;=\; (c/2)/z^3 + 2T/z.
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1598:The $r$-matrix $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$ carries
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1777:$r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$ controls BTZ
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:1780:order in $1/G$.  The subleading $2T/z$ is state-dependent braiding:
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3536:$r(z) = (c/2)/z^3 + 2T/z$ carries all scattering.
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:3768:The $r$-matrix $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$
/Users/raeez/chiral-bar-cobar-vol2/working_notes.tex:9067:$r^{\mathrm{Lap}}(z) = \partial T/z + 2T/z^2 + (c/2)/z^4$.
 succeeded in 51ms:
Total output lines: 3607

/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:226:AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:233:AP-CY30: Factored ≠ solved for higher coherence. The 3-particle S-operator S_{ijk}=R_{ij}R_{ik}R_{jk} constructed from a YBE-satisfying R-matrix does NOT automatically satisfy the Zamolodchikov tetrahedron equation (proved: thm:zte-failure, O(κ²) obstruction). NEVER assume pairwise consistency implies higher-order consistency. The Kapranov-Voevodsky theorem requires E_∞ (fully symmetric), which the Omega-deformation breaks.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:254:- Two-parameter R-matrix: R_ch(u,v) = R_1(u)R_2(v)R_12(u-v) (Zamolodchikov factorization)
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:286:- ZAMOLODCHIKOV TETRAHEDRON: COMPUTED NEGATIVE RESULT. The Yang R-matrix does NOT satisfy ZTE. The factored S_{ijk}=R_{ij}R_{ik}R_{jk} fails at O(κ²) where κ=h₁h₂h₃. At κ=0: trivially satisfied (Kapranov-Voevodsky). At generic κ: genuine obstruction. The correct E_3 3-particle S-operator requires CORRECTIONS beyond pairwise products. Engine: zamolodchikov_tetrahedron_engine.py (~1200 lines, 34 tests). THIS PROVES E_3 IS GENUINELY NONTRIVIAL.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:340:7. E_1-chiral bialgebra: the correct Hopf home. E_∞ vertex bialgebra loses R-matrix (AP-CY23).
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:82:- **ZTE FAILS for Yang R-matrix**: COMPUTED. S=RRR does NOT solve tetrahedron at O(κ²). E_3 is genuinely nontrivial. Engine: 1200 lines, 34 tests.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:100:4. **R-matrix extraction (AP-CY25)**: The formula R=(id⊗S)∘Δ(1) is WRONG. Use half-braiding construction.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:163:**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:667:r^KM(z) = k*Omega/z
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_cy_to_chiral_wave13.md:72:**F13 [SERIOUS, AP-CY11]**: `thm:c3-drinfeld-center` (line 421, ProvedHere) and `thm:e1-universality-cy3` (line 577, ProvedHere) jointly underwrite the d=3 functor chain for C^3. Both are marked ProvedHere but the whole C^3 verification uses the unconstructed A_X logic at Step 4-5 (passing through the Drinfeld double and "quantum vertex chiral group"). The C^3 case is uniquely unconditional ONLY at the character/R-matrix level, not at the "G(C^3) is the quantum vertex chiral group" level. Recommend splitting: the character/algebra identifications are ProvedHere; the G(X) identification is ProvedElsewhere (Schiffmann-Vasserot, Kontsevich-Soibelman) or recast as a Remark.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:31:The E_1-to-E_2 step: the R-matrix is the coherence datum. For E_inf chiral algebras (vertex algebras), R(z) is derived from the OPE. For genuinely E_1, R(z) is independent structure. The derived center Z(A) = HH*(A) carries E_2 from the Deligne conjecture. E_2 lives on Z(A) and on Mod_A, NOT on A. Quantum groups are E_1; Rep(U_q(g)) is E_2 in Cat.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:33:The R-matrix, the YBE (from Stokes on FM_3(C)), the braided line category, the spectral Drinfeld strictification — all E_2 phenomena.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:51:1. The modular operad governing A_inf-algebras in E_1-chiral algebras (Definition def:modular-operad-ainf-chiral: genus-0 proved = SC x E_1^tr; clutching via B^{ann} + R-matrix monodromy; genus >= 2 operadic verification open).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:55:An E_1-chiral quantum group is: E_1-chiral algebra A + chiral coproduct Delta + R-matrix R(z) + quasi-triangularity + antipode, such that Mod_A is braided monoidal (E_2 in Cat). This provides the data for the E_2-to-E_3 step.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:70:- E_2-chiral (def:E2-chiral-algebra, spectral-braiding-core.tex): E_2 on Z^{der}_{ch}(A), NOT on A. R-matrix R(z) with spectral parameter. DONE.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:164:- R-matrix provenance: R(z) from bulk-boundary composition, NOT universal R-matrix (agree on eval locus = DK-0).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:182:V2-AP4: Ordered-to-unordered descent is R-matrix twisted: B^Sigma_n = (B^ord_n)^{R-Sigma_n}. Naive quotient only for pole-free.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:185:V2-AP7: Heisenberg R-matrix = exp(k*hbar/z), NOT trivial. Collision residue k/z. Monodromy exp(-2pi*i*k).
collab wait(call_tjpukx0eLDR23BO7Wg1rHw7p)
  receivers: 019d87a1-de83-74c1-8295-501c295d3354
exec
/bin/zsh -lc "sed -n '50,110p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathcal{W}_3$).}\label{tab:w-shadow-archetype}
\begin{tabular}{lll}
\toprule
\textbf{Invariant} & \textbf{Virasoro} & \textbf{$\mathcal{W}_3$} \\
\midrule
Class & M (mixed/infinite) & M (mixed/infinite) \\
Shadow depth $r_{\max}$ & $\infty$ & $\infty$ \\
$\kappa$ &
 $c/2$ & $5c/6$ \\
Cubic shadow $\mathfrak{C}$ &
 Nonzero & Nonzero \\
Quartic $Q^{\mathrm{contact}}$ &
 $10/[c(5c{+}22)]$ &
 Multi-channel \\
Quintic $o_5$ & $\neq 0$ (forced) & $\neq 0$ \\
$r$-matrix $r(z)$ & $(c/2)/z^3 + 2T/z$ &
 Three channels \\
Koszul dual & $\mathrm{Vir}_{26-c}$
 & $\mathcal{W}_3^{-k-6}$ \\
Complementarity &
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n \"r\\(z\\)\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 856

CLAUDE.md:9:~1,700pp, this repo. Seven parts: I(The Open Primitive) II(The E_1 Core) III(Seven Faces of r(z)) IV(Characteristic Datum and Modularity) V(Standard HT Landscape) VI(Three-Dimensional Quantum Gravity = CLIMAX) VII(Frontier).
CLAUDE.md:334:| DK/YBE | r(z) via Laplace provides DK-0 | MC3 | Proved |
compute/free_fermion_ordered_bar.py:487:        r(z) = Σ_{n≥1} cₙ · z^{-(n-1)}
compute/free_fermion_ordered_bar.py:675:        # this is the coefficient of z⁰ in r(z), which comes from the
compute/free_fermion_ordered_bar.py:1515:    # Heisenberg at level k: double pole k/(z-w)² → r(z) = k/z
compute/genus1_e1_ordered_shadow_all_families.py:156:    # r(z) = k/z^2, giving genus-1 r = k*wp(z), R^(1) = k[wp-1/z^2].
compute/genus1_e1_ordered_shadow_all_families.py:157:    # In the bar-complex convention (post-d-log), H_k has r(z) = k/z,
compute/genus_tower_catalan.py:657:    # spectral parameter. The r-matrix r(z) is related to m_2 by:
compute/genus_tower_catalan.py:658:    #   r(z) = sum_n c_n / z^{n+1}  (pre-d-log)
compute/genus_tower_catalan.py:664:    #   r(z) = c_0/z + c_1/z^2 + c_3/z^4  (genus-0 Virasoro r-matrix)
compute/genus_tower_catalan.py:787:    r_bar(λ) is obtained by Laplace transform of r(z):
compute/genus_tower_catalan.py:788:      r_bar(λ) = integral_0^∞ r(z) e^{-λz} dz
main.tex:1046:$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
main.tex:1278:The modular characteristic $\kappa(\cA) = \mathrm{av}(r(z))$
main.tex:1280:$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$;
main.tex:1307:\part{The Seven Faces of $r(z)$}
main.tex:1312:The collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
README.md:32:- **III. The Seven Faces of r(z)**: Collision residue as R-matrix, Yangian, Sklyanin, Drinfeld-Kohno, celestial OPE, holographic map
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '30,80p' chapters/connections/dnp_identification_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(}Vol~I, Theorem~\textup{\ref{V1-thm:mc2-bar-intrinsic}}\textup{)}, whose
binary collision residue is the central object of this chapter:
\begin{equation}\label{eq:dnp-master-collision-residue}
r(z)
\;:=\;
\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
\;\in\;
\bar{\cA}\,\widehat{\otimes}\,\bar{\cA}((z^{-1})).
\end{equation}
By the $\mathrm d\log$ absorption \textup{(}AP\textup{19}: the bar
propagator $\mathrm d\log(z-w)$ absorbs one power of $(z-w)$\textup{)}, the
maximal pole order of $r(z)$ is $k_{\max}(\cA) = p_{\max}(\cA) - 1$, where
$p_{\max}$ is the maximal OPE pole among generating fields
\textup{(}Vol~I, Definition~\textup{\ref{V1-def:p-max}}\textup{)}. For the standard
landscape:
\begin{itemize}
\item Heisenberg: $p_{\max}=2$, so $r(z) = k/z$ (single pole).
\item Affine $\widehat{\fg}_k$: $p_{\max}=2$, so
 $r(z) = k\Omega/((k+h^\vee) z)$ (single pole, Casimir numerator). %: at k=0, r(z) = 0. Verified.
\item $\beta\gamma$: $p_{\max}=1$, so $r(z) = 0$ in the classical sense

thinking
**Analyzing normalization formulas and bridging identity mentions**

I'm examining the formula conventions used, noting this snippet references KZ normalization without bridging identity or trace form mentions. I want to verify if other parts of the file switch conventions and plan to inspect key files and specific line ranges that might clarify bridging identity usage.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '140,230p' chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\subsection{Strict rational dg-shifted Yangians}
The full notion of dg-shifted Yangian belongs to a broader program \cite{DNP25}. For the strict rational theory developed below we isolate only the structure used.

\begin{definition}[Strict rational dg-shifted Yangian]\label{def:strict-yangian}
A \emph{strict rational dg-shifted Yangian} consists of the following data:
\begin{enumerate}[label=\textup{(\alph*)}]
 \item an associative dg algebra $Y$;
 \item a degree-zero derivation $T$ (the translation operator);
 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
 \[
 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
 \]$, the residue element absorbs
 the level $k$, so the affine realization reads
 $r(z)=k\,\Omega_{\mathrm{aff}}/z$ with $\Omega_{\mathrm{aff}}$ the
 quadratic Casimir tensor of $\mathfrak g$, vanishing at $k=0$, cf.\
 the affine specialization at the start of Section~\ref{sec:strict}.)
 \item the parameter-dependent classical Yang-Baxter equation
 \[
 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'Omega/\\(\\(k' chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1736:$\wp$-function. (The genus-$0$ collision residue is $r(z) = k\,\Omega/((k+h^\vee)z)$; the intrinsic
1744:rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '1710,1765p' chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
On the Clebsch--Gordan components:
\[
 M_B\big|_{V_1} = e^{\pi i\tau/(k+2)}\cdot e^{-\pi i/(k+2)}
 = e^{\pi i(\tau-1)/(k+2)},
 \qquad
 M_B\big|_{V_0} = e^{-3\pi i\tau/(k+2)}\cdot e^{3\pi i/(k+2)}
 = e^{-3\pi i(\tau-1)/(k+2)}.
\]

\medskip\noindent\textbf{Modular $R$-matrix.}\;
Define the genus-$1$ $R$-matrix as the ratio of the connection
form~\eqref{eq:kzb-connection} to its genus-$0$ counterpart:
\begin{equation}\label{eq:genus1-r-matrix}
 r_1(z;\tau) \;:=\; \frac{k}{k+2}\,\Omega\cdot \partial_z\!\log\theta_1(z;\tau).
\end{equation}
Expanding in $z$:
\[
 r_1(z;\tau)
 = \frac{k\,\Omega}{(k+2)z}
 - \frac{k\,\Omega}{k+2}\sum_{n=1}^{\infty}2\,
wait(call_tjpukx0eLDR23BO7Wg1rHw7p) timed out:
exec
/bin/zsh -lc "sed -n '210,260p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
(Theorem~\ref{thm:mc2-bar-intrinsic}). The scalar $\kappa(\cA)$ is
the degree-$2$ projection; the complementarity sum $c + c'$ is the
ambient shadow at genus~$0$; the Koszul dual is obtained via
Verdier duality on the bar coalgebra.
The seed datum for each family is its modular Koszul triple
$\mathfrak{T} = (\cA, \cA^!, r(z))$
(Definition~\ref{def:modular-koszul-triple}):
\begin{equation}\label{eq:census-triples}
\begin{aligned}
\mathfrak{T}_{\cH}
 &= \bigl(\cH_\kappa,\;
 \operatorname{Sym}^{\mathrm{ch}}(V^*),\;
 \kappa/z\bigr), &
\mathfrak{T}_{\cF}
 &= \bigl(\cF,\;
 \operatorname{Sym}^{\mathrm{ch}}(\gamma),\;
 0\bigr), \\
% Convention: trace-form normalisation. In the KZ normalisation
% (Chapter~\ref{chap:kac-moody-koszul}), this reads
% Omega/((k+h^v)z) with Omega = sum kappa^{ab} I_a otimes I_b;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && sed -n '2195,2245p' chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\dim\Barch_n = \binom{d+n-1}{n} = \binom{n+2}{n}$
(unordered multisets, via the symmetric bar).
At $n = 2$: $9$ vs $6$, surplus $= 3 = \dim(\mathfrak{sl}_2)$,
the adjoint representation, spanned by the
antisymmetric tensors $e_I\otimes e_J - R(z)\,e_J\otimes e_I$
that the $\Sigma_2$-quotient kills.
At $n = 3$: $27$ vs $10$, surplus $= 17$, decomposing into
irreducible $B_3$-representations that carry the
degree-$3$ Vassiliev data. At $n = 4$: $81$ vs $15$,
surplus $= 66$.

For Virasoro ($d = 1$, single generator of weight~$2$):
$\dim\Barchord_n = 1 = \dim\Barch_n$
at each tensor degree (one ordered sequence and one
unordered multiset of length~$n$ from a single generator).
The surplus is \emph{not} in raw dimensions but in the
\emph{spectral asymmetry}: the ordered bar differential
$d_{\mathrm{res}}$ on
$\Barchord_n(\mathrm{Vir})$
retains the spectral-parameter dependence
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"r\\(z\\)\"" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md:224:AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
AGENTS.md:669:r^Vir(z) = (c/2)/z^3 + 2T/z
compute/lib/e2_bar_complex.py:257:        """Classical r-matrix r(z) in End(V tensor V) tensor k((z)).
compute/lib/e2_bar_complex.py:421:        """Classical r-matrix r(z) = Omega/(k+h^v) * 1/z.
compute/lib/local_p2_e1_chain.py:569:        The R-matrix r(z) = Res^{coll}_{0,2}(Theta) is the collision residue
compute/lib/local_p2_e1_chain.py:588:            "Its collision residue r(z) = Res^{coll}(Theta) gives the "
compute/lib/local_p2_e1_chain.py:615:      G(K_{P^2}) = (A_{LP2}, A^!_{LP2}, C, r(z), Theta_{LP2}, nabla^{hol})
compute/lib/local_p2_e1_chain.py:621:      r(z) = the R-matrix (collision residue of Theta)
compute/lib/cross_volume_shadow_bridge.py:563:    Vol I: r(z) = Omega/(2z) where Omega is the Casimir (from KZ connection).
compute/lib/cross_volume_shadow_bridge.py:583:      r(z) = (c/2)/z^3 + 2T/z
compute/lib/hcs_codim2_defect_ope.py:193:        (AP126, C10), the classical r-matrix is r(z) = Psi/z.
compute/lib/hcs_codim2_defect_ope.py:464:        # The classical r-matrix has cubic pole: r^Vir(z) = (c/2)/z^3 + 2T/z.
compute/lib/hcs_codim2_defect_ope.py:487:            "virasoro_r_matrix": f"r^Vir(z) = ({c}/2)/z^3 + 2T/z = {t3t}/z^3 + 2T/z",
compute/lib/affine_yangian_e1_cy3.py:75:       r(z) = Res^{coll}_{0,2}(Theta^{E_1}_{W_{1+inf}})
compute/lib/affine_yangian_e1_cy3.py:90:       r(z) = phi_3 / z^3 + phi_5 / z^5 + ... (odd poles only)
compute/lib/affine_yangian_e1_cy3.py:164:   Its arity-2 projection is the classical r-matrix r(z) = r_{12}(z1-z2).
compute/lib/affine_yangian_e1_cy3.py:175:   For the affine Yangian, r(z) = phi_3/z^3 + phi_5/z^5 + ... satisfies the
compute/lib/affine_yangian_e1_cy3.py:194:  - r(z): classical r-matrix = singular part of g(z)
compute/lib/affine_yangian_e1_cy3.py:252:    r"""Classical r-matrix r(z) = sum_{k>=1, k odd} r_k z^{-k}.
compute/lib/affine_yangian_e1_cy3.py:255:      r(z) = g(z) - 1

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n 'r\\(z\\) = k/z'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/lib/celestial_cy3_e1_engine.py:690:      r-matrix: r(z) = k/z (single pole, AP19: 2 -> 1)
compute/lib/drinfeld_center_heisenberg_bulk.py:430:    # Drinfeld side: r(z) = k/z, coefficient = k
compute/lib/drinfeld_center_heisenberg_bulk.py:646:        "level_prefix_present": True,  # r(z) = k/z has explicit k
compute/lib/drinfeld_center_heisenberg_bulk.py:801:        J(z)J(w) ~ k/(z-w)^2.  The d-log extraction gives r(z) = k/z.
compute/lib/drinfeld_center_heisenberg_bulk.py:813:    # r(z) = k/z, av(k/z) = k for abelian
chapters/theory/e1_chiral_algebras.tex:1259: $r(z) = k/z$ has no nontrivial $z$-dependent correction to $\Delta$.
compute/tests/test_drinfeld_center_heisenberg_bulk.py:7:    (3) R-matrix r(z) = k/z matches Gerstenhaber bracket {J,J} = k (THEOREM).
compute/tests/test_drinfeld_center_heisenberg_bulk.py:322:        # VERIFIED: [DC] r(z) = k/z (Drinfeld center side).
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '1180,1305p' chapters/theory/e1_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(contractible associahedron $K_n \simeq \ast$).
Applied to $n = 3$, the two binary decompositions
$(S_1 \sqcup S_2) \sqcup S_3$ and
$S_1 \sqcup (S_2 \sqcup S_3)$
are connected by the unique path in $K_3 = \ast$.
Hence the two iterated factorization isomorphisms
agree, which is coassociativity.
\end{proof}

\subsection{The Drinfeld center recovers $E_2$}
\label{subsec:drinfeld-recovers-e2}

The $E_1$-chiral bialgebra $A$ is ordered and non-braided. The braided
($E_2$) structure is recovered by the Drinfeld center.

\begin{proposition}[$R$-matrix from the Drinfeld center]
\label{prop:r-matrix-from-drinfeld}
\ClaimStatusProvedHere
Let $(A, \mu, \Delta_z, \varepsilon, \eta, S)$ be an $E_1$-chiral Hopf
algebra. The Drinfeld center
thinking
**Clarifying manuscript scope**

I need to verify a few things: first, if the level prefix is present, then check if the same convention (either trace-form or KZ) is used in each file, and ensure that bridge identity is mentioned when conventions change. I suspect this involves all three volumes and potentially active manuscript .tex files. Alternatively, "volumes" may refer to chapter files from the three repositories, which requires careful interpretation. I should be exhaustive within the defined scope, so perhaps I can summarize relevant files using an explorer. Maybe I should wait a bit longer—around 60 seconds.
codex
The raw grep confirms there is live drift, especially in Vol II’s Heisenberg/KM seam. I’m waiting on the explorer’s file classification now so I can patch only the genuinely active files instead of chasing archived audit artifacts.
collab wait(call_w7JzODDDrNggCAuLZQkN9Aqf)
  receivers: 019d87a1-de83-74c1-8295-501c295d3354
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n '(c/2)/z"'^3'"'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n 'r\\"'^Vir'"'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md:669:r^Vir(z) = (c/2)/z^3 + 2T/z
compute/lib/hcs_codim2_defect_ope.py:464:        # The classical r-matrix has cubic pole: r^Vir(z) = (c/2)/z^3 + 2T/z.
compute/lib/hcs_codim2_defect_ope.py:487:            "virasoro_r_matrix": f"r^Vir(z) = ({c}/2)/z^3 + 2T/z = {t3t}/z^3 + 2T/z",
compute/tests/test_hcs_codim2_defect_ope.py:234:        C11: r^Vir(z) = (c/2)/z^3 + 2T/z.
compute/tests/test_hcs_codim2_defect_ope.py:328:        # VERIFIED [DC] AP19 [LT] C11: r^Vir(z) = (c/2)/z^3 + 2T/z
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '100,180p' chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
= (k+2)/(2\sin^2(\pi/(k+2)))$.
The $S$-matrix entries are
$S_{mn} = \sqrt{2/(k+2)} \, \sin(\pi(m+1)(n+1)/(k+2))$.
This is a modular tensor category: the Reshetikhin--Turaev functor
produces the $SU(2)$ Chern--Simons invariants of 3-manifolds.
\end{example}


\section{The $R$-matrix as categorical $r(z)$}
\label{sec:r-matrix-categorical}

The $R$-matrix of $\Uq(\frakg)$ is the categorical incarnation of
the collision residue $r(z)$ from the Volume~I bar complex.

\begin{proposition}[$R$-matrix from bar degree $(1,1)$]
\label{prop:r-matrix-bar}
\ClaimStatusProvedElsewhere
For the affine vertex algebra $V_k(\frakg)$ at level $k$ with
$q = e^{\pi i/(k+h^\vee)}$, the degree-$(1,1)$ component of the
ordered bar complex $B^{\mathrm{ord}}(V_k(\frakg))$ recovers the
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n '2T/z'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
AGENTS.md:669:r^Vir(z) = (c/2)/z^3 + 2T/z
compute/lib/cross_volume_shadow_bridge.py:583:      r(z) = (c/2)/z^3 + 2T/z
compute/lib/cross_volume_shadow_bridge.py:585:    NOT (c/2)/z^4 + 2T/z^2 + dT/z (that's the OPE, not the r-matrix).
compute/lib/cross_volume_shadow_bridge.py:589:        "r_matrix": f"({c}/2)/z^3 + 2T/z",
compute/lib/hcs_codim2_defect_ope.py:331:            3: c / 2,         # AP19: Virasoro r-matrix (c/2)/z^3 + 2T/z
compute/lib/hcs_codim2_defect_ope.py:464:        # The classical r-matrix has cubic pole: r^Vir(z) = (c/2)/z^3 + 2T/z.
compute/lib/hcs_codim2_defect_ope.py:487:            "virasoro_r_matrix": f"r^Vir(z) = ({c}/2)/z^3 + 2T/z = {t3t}/z^3 + 2T/z",
compute/lib/celestial_cy3_e1_engine.py:1190:      r-matrix: (c/2)/z^3 + 2T/z (AP19: poles 4,2,1 -> 3,1)
compute/lib/celestial_cy3_e1_engine.py:1210:        "note": "r(z) = (c/2)/z^3 + 2T/z (AP19)",
notes/physics_celestial_cy.tex:531: % r(z) = (c/2)/z^3 + 2T/z.
chapters/theory/quantum_chiral_algebras.tex:416:In mode language: $T_{(3)} T = c/2 = 1/2$, $T_{(1)} T = 2T$, $T_{(0)} T = \partial T$, $T_{(2)} T = 0$. In lambda-bracket form (AP44, divided powers $\lambda^{(n)} = \lambda^n/n!$): $\{T_\lambda T\} = \tfrac{c}{12}\lambda^3 + 2T\lambda + \partial T = \tfrac{1}{12}\lambda^3 + 2T\lambda + \partial T$. The classical $r$-matrix is $r^{\mathrm{Vir}}(z) = \tfrac{1}{2}/z^3 + 2T/z$ (cubic $+$ simple pole; AP19: one less than the quartic OPE pole via $d\log$ absorption).
compute/tests/test_hcs_codim2_defect_ope.py:234:        C11: r^Vir(z) = (c/2)/z^3 + 2T/z.
compute/tests/test_hcs_codim2_defect_ope.py:328:        # VERIFIED [DC] AP19 [LT] C11: r^Vir(z) = (c/2)/z^3 + 2T/z
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && sed -n '390,450p' chapters/theory/quantum_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[
 J_s(z_1) \;=\; \sum_{m+n = s-1} c_{m,n}^{(s)} \, A^{(m,n)}(z_1),
\]
where $c_{m,n}^{(s)}$ are the $\GL(2)$-invariant coefficients (the minors of the identity matrix, matching the invariant polyvector fields $\Omega_s$ of \texttt{c3\_lie\_conformal.py}). In particular:
\begin{itemize}
 \item Spin~$1$: $J(z_1) = A^{(0,0)}(z_1)$, the mode at the origin of the normal fiber.
 \item Spin~$2$: $T(z_1) = \frac{1}{2\Psi}\mathopen{:}J(z_1)^2\mathclose{:}$ via the Sugawara construction at level $\Psi$.
\end{itemize}

\emph{Step~5: OPE computation.}
\emph{Spin~$1$}: From the propagator in Step~3, the contraction of two spin-$1$ modes gives
\[
 J(z) J(w) \;=\; \langle A^{(0,0)}(z)\, A^{(0,0)}(w) \rangle + \mathopen{:}J(z) J(w)\mathclose{:}
 \;=\; \frac{\Psi}{(z - w)^2} + \mathopen{:}J(z) J(w)\mathclose{:},
\]
where the coefficient $\Psi = -\sigma_2 = -(h_1 h_2 + h_1 h_3 + h_2 h_3)$ arises from the equivariant normalization of the propagator: the Omega-background twists the inner product on $\fgl_1$ by $-\sigma_2$ (which is the Kac--Moody level of the 5d theory on $\C^2 \times \R$, as in Costello~2013). In mode language: $J_{(1)} J = \Psi$, all other modes vanish. The classical $r$-matrix is $r^{\mathrm{Heis}}(z) = \Psi/z$ (C10; level prefix $\Psi$ mandatory, AP126). At $\Psi = 0$: the $r$-matrix vanishes (AP141).

\emph{Spin~$2$}: The Sugawara construction $T = \frac{1}{2\Psi}\mathopen{:}J^2\mathclose{:}$ at level $\Psi$ for the abelian algebra $\fgl_1$ (with $h^\vee = 0$) produces a Virasoro with central charge
\[
 c \;=\; \frac{\Psi \cdot \dim(\fgl_1)}{\Psi + h^\vee} \;=\; \frac{\Psi \cdot 1}{\Psi + 0} \;=\; 1,
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n 'Omega/z' chapters/theory/quantum_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '70,110p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    70	\bottomrule
    71	\end{tabular}
    72	\end{table}
    73	
    74	\begin{table}[ht]
    75	\centering
    76	\small
    77	\caption{Shadow archetype data for affine
    78	Kac--Moody.}\label{tab:km-shadow-archetype}
    79	\begin{tabular}{ll}
    80	\toprule
    81	\textbf{Invariant} & \textbf{Value} \\
    82	\midrule
    83	Class & L (Lie/tree) \\
    84	Shadow depth $r_{\max}$ & $3$ \\
    85	$\kappa(\widehat{\fg}_k)$ &
    86	 $\dim(\fg)(k{+}h^\vee)/(2h^\vee)$ \\
    87	Cubic shadow $\mathfrak{C}$ &
    88	 $\kappa(x,[y,z])$ (Lie bracket) \\
    89	Quartic $o_4$ & $0$ (Jacobi identity) \\
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '720,780p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   720	The bar complex propagator $d\log(z_1 - z_2)$ absorbs one pole
   721	order from the OPE (Proposition~\ref{prop:rmatrix-pole-landscape}).
   722	For the OPE
   723	$J^a(z)J^b(w) \sim k\,\kappa(a,b)/(z{-}w)^2 + f^{ab}{}_{c}J^c/(z{-}w)$,
   724	the collision residue extracts the zeroth product $a_{(0)}b = f^{ab}{}_{c}J^c$
   725	(the Lie bracket). The double-pole term
   726	$k\,\kappa(a,b)/(z{-}w)^2$ contributes the curvature~$m_0$, not the
   727	$r$-matrix (Computation~\ref{comp:sl2-collision-residue-kz},
   728	Step~2). Dualising the Lie-bracket residue via the
   729	level-shifted Killing form gives the Casimir $r$-matrix:
   730	\begin{equation}\label{eq:km-rmatrix}
   731	r^{\mathrm{KM}}_{\hat\fg_k}(z) = \frac{\Omega}{(k + h^\vee)\,z},
   732	\qquad
   733	\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b,
   734	\end{equation}
   735	which has a single simple pole, regardless of the rank of~$\fg$.
   736	The factor $(k + h^\vee)^{-1}$ reflects the level-shifted
   737	inverse Killing form; at the critical level $k = -h^\vee$,
   738	the $r$-matrix degenerates (Sugawara singularity).
   739	
exec
/bin/zsh -lc "nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '10,90p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    10	the complementarity potential is exactly quadratic, and the full open/closed
    11	MC element reduces to the scalar modular characteristic~$\kappa$.
    12	All five main theorems (A through~D and~H) are immediate. The genus
    13	expansion is controlled entirely by~$\kappa$ and assembles into the
    14	$\hat{A}$-genus.
    15	
    16	\begin{center}
    17	\renewcommand{\arraystretch}{1.3}
    18	\begin{tabular}{ll}
    19	\textbf{Algebra} & Heisenberg~$\cH_\kappa$, rank~$1$,
    20	OPE $J(z)\,J(w) \sim \kappa/(z{-}w)^2$ \\
    21	\textbf{Central charge} & $c = 1$ \\
    22	\textbf{Shadow archetype} & G (Gaussian), $r_{\max} = 2$ \\
    23	\textbf{Modular characteristic} & $\kappa(\cH_\kappa) = \kappa$ \\
    24	\textbf{Koszul dual} & $\cH_\kappa^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$,
    25	$\kappa(\cH_\kappa^!) = -\kappa$ \\
    26	\textbf{Complementarity} & $\kappa_{\mathrm{Heis}}(\cH_\kappa) + \kappa_{\mathrm{Heis}}(\cH_\kappa^!) = 0$ \textup{(}free-field type~I\textup{)} \\
    27	\textbf{$r$-matrix} & $r(z) = \kappa/z$ (single pole, no Lie bracket) \\
    28	\textbf{Genus expansion} & $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ GF $= (\kappa/\hbar^2)(\hat{A}(i\hbar) - 1)$
    29	\end{tabular}
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '50,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    50	$\mathcal{W}_3$).}\label{tab:w-shadow-archetype}
    51	\begin{tabular}{lll}
    52	\toprule
    53	\textbf{Invariant} & \textbf{Virasoro} & \textbf{$\mathcal{W}_3$} \\
    54	\midrule
    55	Class & M (mixed/infinite) & M (mixed/infinite) \\
    56	Shadow depth $r_{\max}$ & $\infty$ & $\infty$ \\
    57	$\kappa$ &
    58	 $c/2$ & $5c/6$ \\
    59	Cubic shadow $\mathfrak{C}$ &
    60	 Nonzero & Nonzero \\
    61	Quartic $Q^{\mathrm{contact}}$ &
    62	 $10/[c(5c{+}22)]$ &
    63	 Multi-channel \\
    64	Quintic $o_5$ & $\neq 0$ (forced) & $\neq 0$ \\
    65	$r$-matrix $r(z)$ & $(c/2)/z^3 + 2T/z$ &
    66	 Three channels \\
    67	Koszul dual & $\mathrm{Vir}_{26-c}$
    68	 & $\mathcal{W}_3^{-k-6}$ \\
    69	Complementarity &
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/dnp_identification_master.tex | sed -n '30,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    30	\textup{(}Vol~I, Theorem~\textup{\ref{V1-thm:mc2-bar-intrinsic}}\textup{)}, whose
    31	binary collision residue is the central object of this chapter:
    32	\begin{equation}\label{eq:dnp-master-collision-residue}
    33	r(z)
    34	\;:=\;
    35	\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
    36	\;\in\;
    37	\bar{\cA}\,\widehat{\otimes}\,\bar{\cA}((z^{-1})).
    38	\end{equation}
    39	By the $\mathrm d\log$ absorption \textup{(}AP\textup{19}: the bar
    40	propagator $\mathrm d\log(z-w)$ absorbs one power of $(z-w)$\textup{)}, the
    41	maximal pole order of $r(z)$ is $k_{\max}(\cA) = p_{\max}(\cA) - 1$, where
    42	$p_{\max}$ is the maximal OPE pole among generating fields
    43	\textup{(}Vol~I, Definition~\textup{\ref{V1-def:p-max}}\textup{)}. For the standard
    44	landscape:
    45	\begin{itemize}
    46	\item Heisenberg: $p_{\max}=2$, so $r(z) = k/z$ (single pole).
    47	\item Affine $\widehat{\fg}_k$: $p_{\max}=2$, so
    48	 $r(z) = k\Omega/((k+h^\vee) z)$ (single pole, Casimir numerator). %: at k=0, r(z) = 0. Verified.
    49	\item $\beta\gamma$: $p_{\max}=1$, so $r(z) = 0$ in the classical sense
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/log_ht_monodromy_core.tex | sed -n '140,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   140	
   141	\subsection{Strict rational dg-shifted Yangians}
   142	The full notion of dg-shifted Yangian belongs to a broader program \cite{DNP25}. For the strict rational theory developed below we isolate only the structure used.
   143	
   144	\begin{definition}[Strict rational dg-shifted Yangian]\label{def:strict-yangian}
   145	A \emph{strict rational dg-shifted Yangian} consists of the following data:
   146	\begin{enumerate}[label=\textup{(\alph*)}]
   147	 \item an associative dg algebra $Y$;
   148	 \item a degree-zero derivation $T$ (the translation operator);
   149	 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
   150	 \[
   151	 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
   152	 \]$, the residue element absorbs
   153	 the level $k$, so the affine realization reads
   154	 $r(z)=k\,\Omega_{\mathrm{aff}}/z$ with $\Omega_{\mathrm{aff}}$ the
   155	 quadratic Casimir tensor of $\mathfrak g$, vanishing at $k=0$, cf.\
   156	 the affine specialization at the start of Section~\ref{sec:strict}.)
   157	 \item the parameter-dependent classical Yang-Baxter equation
   158	 \[
   159	 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/log_ht_monodromy_core.tex | sed -n '1710,1770p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1710	On the Clebsch--Gordan components:
  1711	\[
  1712	 M_B\big|_{V_1} = e^{\pi i\tau/(k+2)}\cdot e^{-\pi i/(k+2)}
  1713	 = e^{\pi i(\tau-1)/(k+2)},
  1714	 \qquad
  1715	 M_B\big|_{V_0} = e^{-3\pi i\tau/(k+2)}\cdot e^{3\pi i/(k+2)}
  1716	 = e^{-3\pi i(\tau-1)/(k+2)}.
  1717	\]
  1718	
  1719	\medskip\noindent\textbf{Modular $R$-matrix.}\;
  1720	Define the genus-$1$ $R$-matrix as the ratio of the connection
  1721	form~\eqref{eq:kzb-connection} to its genus-$0$ counterpart:
  1722	\begin{equation}\label{eq:genus1-r-matrix}
  1723	 r_1(z;\tau) \;:=\; \frac{k}{k+2}\,\Omega\cdot \partial_z\!\log\theta_1(z;\tau).
  1724	\end{equation}
  1725	Expanding in $z$:
  1726	\[
  1727	 r_1(z;\tau)
  1728	 = \frac{k\,\Omega}{(k+2)z}
  1729	 - \frac{k\,\Omega}{k+2}\sum_{n=1}^{\infty}2\,
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '2205,2255p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2205	
  2206	For Virasoro ($d = 1$, single generator of weight~$2$):
  2207	$\dim\Barchord_n = 1 = \dim\Barch_n$
  2208	at each tensor degree (one ordered sequence and one
  2209	unordered multiset of length~$n$ from a single generator).
  2210	The surplus is \emph{not} in raw dimensions but in the
  2211	\emph{spectral asymmetry}: the ordered bar differential
  2212	$d_{\mathrm{res}}$ on
  2213	$\Barchord_n(\mathrm{Vir})$
  2214	retains the spectral-parameter dependence
  2215	$r(z) = (c/2)/z^3 + 2T/z$ (the collision residue of
  2216	the quartic-pole OPE, after $d\log$ absorption), while
  2217	the symmetric bar sees only the $\Sigma_n$-invariant
  2218	part. The directed spectral flow (the fact that
  2219	$r(z) \ne r(-z)$ due to the odd-power term
  2220	$2T/z$) is the surplus datum, invisible at the
  2221	level of dimensions but controlling the higher
  2222	$\Ainf$ operations $m_k$ ($k \ge 3$) that characterise
  2223	class~$\mathbf{M}$.
  2224	\end{computation}
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/examples/quantum_group_reps.tex | sed -n '110,190p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   110	
   111	The $R$-matrix of $\Uq(\frakg)$ is the categorical incarnation of
   112	the collision residue $r(z)$ from the Volume~I bar complex.
   113	
   114	\begin{proposition}[$R$-matrix from bar degree $(1,1)$]
   115	\label{prop:r-matrix-bar}
   116	\ClaimStatusProvedElsewhere
   117	For the affine vertex algebra $V_k(\frakg)$ at level $k$ with
   118	$q = e^{\pi i/(k+h^\vee)}$, the degree-$(1,1)$ component of the
   119	ordered bar complex $B^{\mathrm{ord}}(V_k(\frakg))$ recovers the
   120	$R$-matrix of $\Uq(\frakg)$:
   121	\[
   122	 r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{V_k(\frakg)})
   123	 \;\longleftrightarrow\;
   124	 \cR_q = \lim_{z \to 0}\, \cR(z)
   125	\]
   126	where $r(z) = \frac{k\,\Omega}{z} + O(1)$ is the classical $r$-matrix with
   127	Casimir $\Omega \in \frakg \otimes \frakg$ and level prefix $k$
   128	, and $\cR_q$ is the
   129	quantized universal $R$-matrix. The spectral parameter $z$
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '1210,1335p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1210	\end{equation}
  1211	where $\tau$ is the transposition of tensor factors.
  1212	The $R$-matrix lives in $\cZ(\Rep^{E_1}(A))$, not in $A \otimes A$
  1213	directly: it is the half-braiding data encoding the obstruction to
  1214	commutativity of the ordered tensor product. This resolves the
  1215	apparent paradox that the $R$-matrix ``lives in $A \otimes A$''
  1216	(which is ordered and has no braiding): the $R$-matrix is a morphism
  1217	in the Drinfeld center, which IS braided.
  1218	\end{proposition}
  1219	
  1220	\begin{proof}
  1221	The Drinfeld center $\cZ(\Rep^{E_1}(A))$ consists of pairs $(M, \sigma_M)$
  1222	where $M$ is an $A$-module and $\sigma_M \colon M \otimes_{E_1} N
  1223	\xrightarrow{\sim} N \otimes_{E_1} M$ is a half-braiding natural in $N$.
  1224	For $M = A$ (the regular module), the half-braiding is constructed from
  1225	the spectral coproduct: define
  1226	$\sigma_A(z)(a \otimes n)
  1227	= \sum \Delta_z(a)_{(2)} \cdot n \otimes \Delta_z(a)_{(1)}$
  1228	(using Sweedler notation for $\Delta_z$). The naturality of $\sigma_A$
  1229	in the second slot follows from the bialgebra compatibility (axiom~(iii)
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/theory/quantum_chiral_algebras.tex | sed -n '400,460p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   400	\emph{Spin~$1$}: From the propagator in Step~3, the contraction of two spin-$1$ modes gives
   401	\[
   402	 J(z) J(w) \;=\; \langle A^{(0,0)}(z)\, A^{(0,0)}(w) \rangle + \mathopen{:}J(z) J(w)\mathclose{:}
   403	 \;=\; \frac{\Psi}{(z - w)^2} + \mathopen{:}J(z) J(w)\mathclose{:},
   404	\]
   405	where the coefficient $\Psi = -\sigma_2 = -(h_1 h_2 + h_1 h_3 + h_2 h_3)$ arises from the equivariant normalization of the propagator: the Omega-background twists the inner product on $\fgl_1$ by $-\sigma_2$ (which is the Kac--Moody level of the 5d theory on $\C^2 \times \R$, as in Costello~2013). In mode language: $J_{(1)} J = \Psi$, all other modes vanish. The classical $r$-matrix is $r^{\mathrm{Heis}}(z) = \Psi/z$ (C10; level prefix $\Psi$ mandatory, AP126). At $\Psi = 0$: the $r$-matrix vanishes (AP141).
   406	
   407	\emph{Spin~$2$}: The Sugawara construction $T = \frac{1}{2\Psi}\mathopen{:}J^2\mathclose{:}$ at level $\Psi$ for the abelian algebra $\fgl_1$ (with $h^\vee = 0$) produces a Virasoro with central charge
   408	\[
   409	 c \;=\; \frac{\Psi \cdot \dim(\fgl_1)}{\Psi + h^\vee} \;=\; \frac{\Psi \cdot 1}{\Psi + 0} \;=\; 1,
   410	\]
   411	independent of $\Psi$ (a feature of $\fgl_1$; for non-abelian $\frakg$, $c$ depends on the level). The Virasoro OPE is
   412	\[
   413	 T(z)\,T(w) \;=\; \frac{c/2}{(z - w)^4} + \frac{2T(w)}{(z - w)^2} + \frac{\partial T(w)}{z - w}
   414	 \;=\; \frac{1/2}{(z - w)^4} + \frac{2T(w)}{(z - w)^2} + \frac{\partial T(w)}{z - w}.
   415	\]
   416	In mode language: $T_{(3)} T = c/2 = 1/2$, $T_{(1)} T = 2T$, $T_{(0)} T = \partial T$, $T_{(2)} T = 0$. In lambda-bracket form (AP44, divided powers $\lambda^{(n)} = \lambda^n/n!$): $\{T_\lambda T\} = \tfrac{c}{12}\lambda^3 + 2T\lambda + \partial T = \tfrac{1}{12}\lambda^3 + 2T\lambda + \partial T$. The classical $r$-matrix is $r^{\mathrm{Vir}}(z) = \tfrac{1}{2}/z^3 + 2T/z$ (cubic $+$ simple pole; AP19: one less than the quartic OPE pole via $d\log$ absorption).
   417	
   418	The $T$--$J$ OPE confirms that $J$ is a primary of conformal weight~$1$: $T(z)\,J(w) = J(w)/(z - w)^2 + \partial J(w)/(z - w)$, i.e.\ $T_{(1)}J = J$, $T_{(0)}J = \partial J$.
   419	

thinking
**Summarizing volume classifications and bridging details**

I’m organizing a clear summary of the classification and bridging identities across volumes, noting formula types (Heis, Vir, KM), line numbers, and level prefixes present. I’m including flagged issues like missing bridging or inconsistent conventions and ensuring to highlight where bridging identities appear, especially for mixed convention files. I’ll format per volume with bullet points referencing line ranges and classification, while confirming no missing level prefixes or unflagged convention switches exist.
codex
**Volume I**
- `chapters/examples/kac_moody.tex:70-110,730-770` (KM): the shadow table/profile lays out the affine triple and records `r(z)=Ω/((k+h^∨)z)` with the Sugawara denominator (KZ normalization) and the Feigin–Frenkel involution remark; the later remark explicitly rewrites the same data as `kΩ_tr/z` and explains the bridge `kΩ_tr = Ω/(k+h^∨)` plus the `k=0` vs. `k≠0` checks, so both conventions coexist with the required level prefix and bridge identity.  
- `chapters/examples/heisenberg_eisenstein.tex:16-42` (Heis): the archetype table and triple define `r(z)=κ/z`, scalar trace-form data where the level prefix `κ` appears everywhere and the vanishing-at-κ=0 sanity check is stated, so no prefix is missing.  
- `chapters/examples/w_algebras.tex:50-102` (Vir): the Virasoro row and modular triple give `r(z)=(c/2)/z³+2T/z`; the central-charge coefficient carries the level prefix, and the write-up stresses the cubic+simple pole ordering after `d\log` absorption.

**Volume II**
- `chapters/connections/dnp_identification_master.tex:30-55` (Heis/KM/Vir): the landscape list tabulates the same three formulas (Heis `k/z`, affine `kΩ/((k+h^∨)z)`, Vir `(c/2)/z³+2T/z`) with the indicated pole orders; the affine entry uses the KZ denominator, the Heisenberg and Vir lines stay trace-form, and every formula includes its level parameter.  
- `chapters/connections/log_ht_monodromy_core.tex:141-186,1710-1749` (KM): the strict Yangian definition and shifted KZ connection refer to `r(z)=kΩ/z`, and the genus-1 computation repeatedly cites the KZB normalization `r(z)=kΩ/((k+h^∨)z)` plus the extra rescaling factor `k/(k+h^∨)` (lines 1736‑1749), so the cross-convention bridge is spelled out as part of the modular correction; no extra action needed.  
- `chapters/connections/ordered_associative_chiral_kd_core.tex:2206-2223` (Vir): the Virasoro computation highlights the spectral asymmetry carried by `r(z)=(c/2)/z³+2T/z` and contrasts it with the symmetric bar (only the `Σ_n`-invariant part), so the level `c` occurs naturally and the odd-term `2T/z` is exactly why `r ≠ r(-z)`.

**Volume III**
- `chapters/examples/quantum_group_reps.tex:114-150` (KM): the categorical proposition states `r(z)=kΩ/z+O(1)` as the classical limit of the quantum group R-matrix, explicitly mentions the level prefix `k`, and reminds the reader that the collision residue vanishes at `k=0`, so the trace-form convention stays consistent with Vol. I.  
- `chapters/theory/e1_chiral_algebras.tex:1250-1266` (Heis): the Heisenberg $E_1$ bialgebra example shows $\Delta_z$ primitive because `r(z)=k/z` has no extra $z$ dependence, the level prefix `k` is part of the OPE, and the Drinfeld-center braiding reproduces the expected $\mathrm{av}(R(z))=k$.  
- `chapters/theory/quantum_chiral_algebras.tex:400-417` (Heis+Vir): the codimension‑two derivation revisits the same Heisenberg kernel `r^{\mathrm{Heis}}(z)=Ψ/z` (with vanishing at Ψ=0) and then spells out the Virasoro OPE plus the classical `r^{\mathrm{Vir}}(z)=(c/2)/z³+2T/z` arising after the Sugawara construction, so both level prefixes (`Ψ`, `c/2`) are present.

All surveyed files carry the required level prefixes and, whenever both trace-form and KZ normalizations appear (Vol I’s KM chapter and Vol II’s `log_ht_monodromy_core.tex`), the bridge identities are documented. No file was found to switch conventions without stating the bridge, so no additional flags are necessary.
wait(call_w7JzODDDrNggCAuLZQkN9Aqf) 1 agents complete:
  019d87a1-de83-74c1-8295-501c295d3354 completed: "**Volume I**
- `chapters/examples/kac_moody.tex:70-110,730-770` (KM): the shadow table/profile lays out the affine tripl…"
codex
The first explorer pass covered obvious chapter anchors but missed several active Vol II files that still look inconsistent from the grep. I’m sending a targeted follow-up on those live surfaces before I edit, because the Heisenberg/Laplace-vs-collision seam is exactly where false positives and real bugs get mixed.
collab send_input(call_U9c7RLGcH9kRjRQeSz3Ugi5g, prompt="Do a second pass on the active files below and classify each one precisely: is the file internally consistent, or does i…")
  receiver: 019d87a1-de83-74c1-8295-501c295d3354
send_input(call_U9c7RLGcH9kRjRQeSz3Ugi5g, prompt="Do a second pass on the active files below and classify each one precisely: is the file internally consistent, or does i…") completed: "**Volume I**
- `chapters/examples/kac_moody.tex:70-110,730-770` (KM): the shadow table/profile lays out the affine tripl…":
  receiver: 019d87a1-de83-74c1-8295-501c295d3354

Plan update
  → Inspect each target file for KM/Heis/Vir r-matrix entries and note conventions/bridges
exec
/bin/zsh -lc "sed -n '1200,1360p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
spectral parameter:
\begin{equation}
\label{eq:intro-CYBE}
[r_{12}(z_{12}),\, r_{13}(z_{13})] +
[r_{12}(z_{12}),\, r_{23}(z_{23})] +
[r_{13}(z_{13}),\, r_{23}(z_{23})] \;=\; 0.
\end{equation}
The proof: Laplace-transform each term of the PVA Jacobi identity.
The substitution $\mu = \lambda_2$, $\lambda = \lambda_1$ becomes
$z_{13} = z_{12} + z_{23}$ under Laplace, and the three terms of
the Jacobi identity map exactly to the three commutators of the
CYBE. The constraint $z_{13} = z_{12} + z_{23}$ is the spectral
parameter identity, the Laplace shadow of the additivity of
$\lambda$-parameters under operadic composition.

\subsection*{The quantum $R$-matrix}

The quantum $R$-matrix $R(z)$ is constructed from the
bulk-to-boundary OPE of line operators. Given two parallel
boundary lines $L_1(z_1)$ and $L_2(z_2)$ in the 3d HT theory
exec
/bin/zsh -lc "rg -n \"r\\(z\" /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
170:$\kappa(\cA) = \mathrm{av}(r(z))$ at degree~$2$, and the shadow
1189:r(z) \;=\; \int_0^\infty e^{-\lambda z}\,
1196:$r(z)(a \otimes b) = \sum_{n \geq 0} c_n / z^{n+1}$.
1229:Its semiclassical limit is $R(z) = \id + \h\, r(z) + O(\h^2)$,
1252:$r(z)$ is the semiclassical limit of the YBE for $R(z)$: both
1374: $r(z) \in \mathcal{Y} \widehat{\otimes}\,
1378: \mathcal{Y} \otimes_{r(z)} \mathcal{Y}[[z^{-1}, z]]$;
1385:r_{23}(z) + (\id \otimes \Delta_z)(r(z+w))
1387:r_{12}(w) + (\Delta_w \otimes \id)(r(z)).
1532:for $r(z) = k\,\Omega/z$.
1807:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
1835:\item Classical $r$-matrix: $r(z) = k\,\Omega / z$, where
2195:\noindent\textbf{Part~\ref{part:bbl-core}: The Seven Faces of $r(z)$}
2197:The collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
2391:Part~\ref{part:bbl-core} exhibits the seven faces of the collision residue $r(z)$:
thinking
**Inspecting suspect files**

I’m thinking maybe we should inspect the suspect files ourselves. I realize I’ll probably need to make some edits eventually, so I'll start by reading relevant snippets. I could use a command like `sed` around those lines, and perhaps I’d also want to run `rg -n` within those files for better insight. It feels like a productive plan, so I’m going to dive into that now!
exec
/bin/zsh -lc "sed -n '300,420p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1760,1885p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,90p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '110,155p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2285,2335p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2380,2460p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '27770,27825p' /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

Five families beyond the Heisenberg, ordered by increasing complexity:

\subsection*{Free multiplet}

The free multiplet, a chiral algebra generated by a free boson
$\phi$ with OPE $\phi(z) \phi(w) \sim -\log(z - w)$, has
$m_{k \geq 3} = 0$: no higher $\Ainf$ operations. The bar
complex is strictly coassociative, the Swiss-cheese algebra is
\emph{formal} (quasi-isomorphic to its cohomology as an operad
algebra), and the $\R$-factorisation is exact. The PVA is
polynomial: $\{\phi {}_\lambda \phi\} = \lambda$. The spectral
$R$-matrix $R(z) = \exp(\hbar/z)$ is the universal abelian solution.
All higher structure is trivial.

\subsection*{Landau--Ginzburg: the first genuine $\Ainf$ correction}

A Landau--Ginzburg model with cubic superpotential
$W = \phi^3/3$ produces the first nontrivial~$m_3$. The
$\Ainf$ chiral algebra has:
 succeeded in 52ms:
evaluating the collision residue integral
$\Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$. In each case, the
computation reduces to extracting the singular part of the
$\lambda$-bracket via the Laplace formula of
Proposition~\ref{prop:field-theory-r}.

\subsubsection{Heisenberg $\cH_k$: the Gaussian $r$-matrix}
% label removed: subsubsec:heisenberg-r-matrix
\index{Heisenberg algebra!classical r-matrix|textbf}
\index{classical r-matrix!Heisenberg}

\begin{proposition}[Heisenberg $r$-matrix from collision residue;
\ClaimStatusProvedHere]
% label removed: prop:heisenberg-r-matrix
For the Heisenberg algebra $\cH_k$ at level $k$, the classical
$r$-matrix is
\begin{equation}
% label removed: eq:heisenberg-r-explicit
\boxed{
r_{\cH_k}(z) \;=\; \frac{k}{z^2}\, J \otimes J,
 succeeded in 51ms:
\providecommand{\HH}{\operatorname{HH}}
\providecommand{\Har}{\operatorname{Har}}

\section{Bulk--boundary functoriality and spectral $R(z)$}
\label{sec:bulk-boundary-R}
\label{sec:spectral_braiding}
\label{sec:spectral-braiding}
\label{chap:spectral-braiding}
\label{sec:bulk-boundary}

The Yangian $Y(\fg)$ is the universal quantization of the classical $r$-matrix $r(z) = k\,\Omega/z$. Yet the RTT formalism that defines it treats the spectral parameter $z$ as a formal variable, the Hopf coproduct as a given axiom, and the Yang--Baxter equation as a constraint to be verified. None of these are \emph{explained}: the spectral parameter has no geometric origin, the Hopf coproduct has no universal property, and the YBE is an identity without a cause.

The $E_1$ bar construction resolves all three deficiencies at once. The ordered bar coalgebra $B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ with its deconcatenation coproduct \emph{is} the Yangian's coproduct: the spectral parameter is the coordinate on $\C$ (the holomorphic direction), the coproduct arises from the $E_1$-factorization along the topological half-line $\R_{\ge 0}$, and the Yang--Baxter equation is Stokes' theorem on the Fulton--MacPherson compactification $\FM_3(\C)$. The $\SCchtop$ structure emerges not on $B(A)$ itself but on the chiral derived center: the pair $(C^\bullet_{\mathrm{ch}}(A,A),\, A)$ of chiral Hochschild cochains and boundary algebra is the $\SCchtop$ datum. The symmetric bar $B^\Sigma$ is the $\Sigma_n$-coinvariant shadow; $R$-matrix descent relates $B^{\mathrm{ord}}$ to $B^\Sigma$.

The spectral $R$-matrix $R(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta^{\mathrm{oc}})$ is the genus-$0$, degree-$2$ collision residue of the open/closed MC element, extracted from the bulk-to-boundary composition of two parallel line operators. It equals the Laplace transform of the chiral $\lambda$-bracket (Proposition~\ref{prop:field-theory-r}), placing the RTT relation, the Sklyanin bracket, the Drinfeld presentation, and the PVA descent on a single geometric footing.

\subsection{Boundary data and factorization module structure}
\label{subsec:boundary-module}
The geometric content enters through the boundary. Let $A=(A_{\mathsf{ch}},A_{\mathsf{top}})$ be a $C_\ast\!\bigl(W(\mathsf{SC}^{\mathrm{ch,top}})\bigr)$-algebra.
A topological boundary condition along $t=0$ is a \emph{right $W(\mathsf{SC}^{\mathrm{ch,top}})$-module} $M$ supported on $\C\times \R_{\ge 0}$: a prefactorization algebra $\mathsf{Obs}^{\partial}$ on half-rectangles with actions
 succeeded in 51ms:
\item \emph{The shadow obstruction tower.}
 $\Theta_\cA^{\le 2}\to\Theta_\cA^{\le 3}\to\cdots$:
 finite-order projections carrying nonlinear
 information invisible at genus~$0$.
\item \emph{The shadow connection.}
 $\nabla^{\mathrm{hol}}_{g,n}=d-\mathrm{Sh}_{g,n}(\Theta_\cA)$:
 the flat connection on the derived coinvariant /
 protected-state package, specializing on benchmark
 comparison surfaces to the corresponding derived
 conformal-block package. At
 $g=0$ this is the corresponding system of differential equations
 on those comparison surfaces (KZ on the affine Kac--Moody
 comparison surface; the Virasoro conformal Ward connection on the
 Virasoro comparison surface; BPZ on the Virasoro
 degenerate-representation comparison surface);
 at $g\ge 1$ it acquires curvature $\kappa\cdot\omega_g$.
\end{enumerate}
\end{construction}

\begin{computation}[Modular extension of the Heisenberg
 succeeded in 51ms:
  \sum_{n \geq 0}
  c_n^{ab} \cdot \frac{n!}{z^{n+1}},
  \qquad
  \text{where }
  \{a_\lambda b\} = \sum_{n \geq 0} c_n^{ab}\, \lambda^n.
\]
The modular characteristic $\kappa(\cA) + \kappa(\cA^!)$
is a constant independent of the level/charge parameter for each family,
and Koszul duality acts on the chiral Hochschild complex as predicted by
Theorem~H of Volume~I (at generic level; the critical level $k = -h^\vee$
is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I
Remark~\ref*{rem:critical-level-lie-vs-chirhoch}).
\end{proposition}

\begin{proof}
Direct computation on each family.  The Laplace identity
is Proposition~\ref{prop:field-theory-r} specialized to explicit
$\lambda$-bracket data.
For Heisenberg: $\{a_\lambda a\} = k\lambda$ gives
$r(z) = k/z^2$.
 succeeded in 51ms:
 on those comparison surfaces (KZ on the affine Kac--Moody
 comparison surface; the Virasoro conformal Ward connection on the
 Virasoro comparison surface; BPZ on the Virasoro
 degenerate-representation comparison surface);
 at $g\ge 1$ it acquires curvature $\kappa\cdot\omega_g$.
\item \emph{The critical discriminant.}
 $\Delta=8\kappa S_4$
 (Vol~I, Theorem~\ref*{V1-thm:single-line-dichotomy}):
 $\Delta = 0$ iff the shadow obstruction tower terminates (classes
 $\mathbf{G}$, $\mathbf{L}$); $\Delta\neq 0$ iff it
 is infinite (class~$\mathbf{M}$).
 For the Heisenberg holographic system:
 $\Delta=0$; for the Virasoro:
 $\Delta=40/(5c{+}22)\neq 0$.
 The multi-channel shadow connection has curvature equal to the propagator variance $\delta_{\mathrm{mix}} = \operatorname{Var}_\kappa(f)$ (Theorem~10.22.30 of Vol~I), a Cauchy--Schwarz gap vanishing at enhanced symmetry loci.
\end{enumerate}
\end{construction}

\begin{computation}[Modular extension of the Heisenberg
genus-zero package; \ClaimStatusProvedHere]
 succeeded in 51ms:
\begin{proposition}[Full tower self-duality at $c = 13$;
\ClaimStatusProvedHere]
\label{prop:c13-full-self-duality}
\index{Virasoro algebra!self-duality at $c=13$|textbf}
\index{shadow obstruction tower!self-duality}
\index{Feigin--Frenkel involution!fixed point $c=13$}%
At the Virasoro self-dual point $c = 13$
\textup{(}the unique fixed point of the Feigin--Frenkel Koszul
involution $c \mapsto 26 - c$ on the one-parameter family
$\{\mathrm{Vir}_c\}_c$:, and with complementarity sum
$\kappa + \kappa' = 13$ on this family\textup{)}, so that
$\mathrm{Vir}_{13}^! = \mathrm{Vir}_{13}$,
the modular Koszul datum is self-dual at every level of the
bar-intrinsic tower. Explicitly:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Scalar characteristic.}\enspace
 $\kappa(\mathrm{Vir}_{13}) = 13/2
 = \kappa(\mathrm{Vir}_{26 - c}) \big|_{c = 13}
 = \kappa(\mathrm{Vir}_{13}^!)$;
 both values coincide with $(26 - c)/2 \big|_{c = 13} = 13/2$.
exec
/bin/zsh -lc "sed -n '1160,1245p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
poles along boundary divisors\textup{)}.
Then $H^\bullet(\cA, Q)$ carries the
structure of a $(-1)$-shifted Poisson vertex algebra
(the $\lambda$-bracket has cohomological degree~$+1$;
equivalently, the underlying Lie bracket lives on $A[1]$):
\begin{enumerate}[label=\textup{(\roman*)}]
\item the commutative product is the regular part of $m_2$;
\item the $\lambda$-bracket is the singular part of $m_2$;
\item all higher operations $m_{k \geq 3}$ vanish on cohomology.
\end{enumerate}
The PVA axioms (sesquilinearity, skew-symmetry, Jacobi, Leibniz,
vacuum) are proved by Stokes' theorem on $\FM_n(\C)$ and
contractibility of $\Conf_k^{<}(\R)$.
\end{maintheorem}

The PVA is the classical shadow. It remembers the commutative product and the singular OPE, but forgets the chain-level homotopies $m_3, m_4, \ldots$ that measure the failure of strict associativity. What structure does the PVA carry beyond the Lie bracket?

\section*{The spectral $R$-matrix from the $\lambda$-bracket}

The $\lambda$-bracket encodes the classical braiding of line
exec
/bin/zsh -lc "rg -n \"Omega/\\(\\(k\" /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n \"k\\\\,?\\\\Omega\" -n /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:k\,?\Omega)
           ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"k\\\\Omega\" /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:k\Omega)
        ^^
error: unrecognized escape sequence

exec
/bin/zsh -lc 'grep -n "k.*Omega" /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1529:$\alpha_T^{\mathrm{mix}} = k\,\Omega/z$, the level-weighted split Casimir; the
1532:for $r(z) = k\,\Omega/z$.
1535:$\nabla = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$.
1835:\item Classical $r$-matrix: $r(z) = k\,\Omega / z$, where
2027: $k\,\Omega/z$ &

thinking
**Analyzing formulas in suspect files**

I'm thinking about how I need to search each suspect file for relevant formulas and classify the issues I find. For instance, in `vol2 chapters/theory/introduction.tex`, Heisenberg uses a classical r-matrix formula but might reference collision residue differently. I need to check specific lines for clarity.

Then in `vol2 chapters/connections/thqg_spectral_braiding_extensions.tex`, it might use multiple terms interchangeably without clear transitions, and similar inconsistencies appear in `ht_bulk_boundary_line`. I’ll note the lines for deeper inspection later.
thinking
**Clarifying formula usage**

I'm thinking that if a file uses `r(z)=k/z^2` and later switches to `r^{coll}`, there might be some mixing happening in the terminology. I need to examine the context and check if they refer to the same thing or if they're distinct concepts. Clear terminology is crucial here since it could lead to confusion in interpretation. It's all about ensuring consistency in how these formulas are presented throughout the document!
exec
/bin/zsh -lc "sed -n '1500,1555p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 + \tfrac{1}{2}[\alpha_T^{\mathrm{cl}},
 \alpha_T^{\mathrm{cl}}] &&= 0, \\
\label{eq:intro-mc-mixed}
&d_{\Theta}\,\alpha_T^{\mathrm{mix}} &&= 0, \\
\label{eq:intro-mc-open}
&d_{\Theta}\,\alpha_T^{\mathrm{op}}
 + [\alpha_T^{\mathrm{mix}},
 \alpha_T^{\mathrm{op}}]
 + \tfrac{1}{2}[\alpha_T^{\mathrm{mix}},
 \alpha_T^{\mathrm{mix}}]_{\mathrm{op}}
 + \tfrac{1}{2}[\alpha_T^{\mathrm{op}},
 \alpha_T^{\mathrm{op}}] &&= 0,
\end{alignat}
where $\Theta_\cA := \alpha_T^{\mathrm{cl}}$ is the closed-colour component and
$d_\Theta = D + [\Theta_\cA, -]$ is the
$\Theta_\cA$-twisted differential.

Equation~\eqref{eq:intro-mc-closed} is the modular MC equation
of Vol~I\@.
Equation~\eqref{eq:intro-mc-mixed} says that the classical
codex
I have concrete suspects now: Vol II’s introduction and several connection chapters are still collapsing Laplace kernels and collision residues, and Vol I has a live Virasoro/Casimir conflation. I’m pulling exact line-numbered contexts so I can patch the smallest truthful statements and keep each file on one declared convention.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '124,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1800,1878p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '318,405p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2300,2318p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '780,810p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2398,2448p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex | sed -n '27796,27812p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   124	\begin{proof}
   125	Direct computation on each family.  The Laplace identity
   126	is Proposition~\ref{prop:field-theory-r} specialized to explicit
   127	$\lambda$-bracket data.
   128	For Heisenberg: $\{a_\lambda a\} = k\lambda$ gives
   129	$r(z) = k/z^2$.
   130	For $\widehat{\mathfrak{sl}}_2$: all $9$ bracket pairs
   131	$(J^a, J^b)$ verify.
   132	For Virasoro: $\{T_\lambda T\} = \partial T + 2T\lambda
   133	+ (c/12)\lambda^3$ gives Laplace kernel $r^L(z) = \partial T/z + 2T/z^2
   134	+ (c/2)/z^4$, matching the OPE
   135	(the collision residue is $r^{\mathrm{coll}}(z) = (c/2)/z^3 + 2T/z$).
   136	For $\beta\gamma$/$bc$: $\{b_\lambda c\} = 1$ gives $r(z) = 1/z$.
   137	For $\mathcal{W}_3$: all three bracket pairs verify.
   138	Complementarity constants: $0$ (Heisenberg, $\mathfrak{sl}_2$,
   139	$bc$), $13$ (Virasoro), $250/3$ ($\mathcal{W}_3$; principal
   140	$W$-algebras have $\kappa + \kappa' = \varrho \cdot K_N$
 succeeded in 51ms:
  1800	Abelian $U(1)$ Chern--Simons theory at level~$k$ with a boundary
  1801	condition along $\C \times \{0\}$ produces:
  1802	\begin{itemize}
  1803	\item Boundary vertex algebra: $\widehat{\mathfrak{u}(1)}_k$,
  1804	 the Heisenberg algebra at level~$k$.
  1805	\item $\lambda$-bracket:
  1806	 $\{J {}_\lambda J\} = k\lambda$.
  1807	\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
  1808	 transform of $k\lambda$).
  1809	\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
  1810	 Yang--Baxter trivially (abelian).
  1811	\item Line operators:
  1812	 $\cC_{\mathrm{line}} \simeq
  1813	 Y(\mathfrak{u}(1))\text{-mod}
  1814	 \simeq \widehat{\mathfrak{u}(1)}_{-k}\text{-mod}$,
  1815	 the semisimple Fock sector.
  1816	\end{itemize}
  1817	The Yang--Baxter equation is verified directly from $\FM_3(\C)$:
  1818	the abelian case is exact (no loop corrections), and the
  1819	$R$-matrix is the exponential of the classical $r$-matrix. This
 succeeded in 50ms:
   318	\boxed{
   319	r_{\cH_k}(z) \;=\; \frac{k}{z^2}\, J \otimes J,
   320	}
   321	\end{equation}
   322	where $J$ is the Heisenberg current. This is a scalar $r$-matrix:
   323	it acts diagonally in the one-dimensional current space.
   324	\end{proposition}
   325	
   326	\begin{proof}
   327	\noindent\textbf{Step 1: The $\lambda$-bracket.}
   328	The Heisenberg $\lambda$-bracket is
   329	$\{J {}_\lambda J\} = k\lambda$
   330	(Section~\ref{sec:rosetta-stone}). The coefficients in the
   331	expansion $\{J {}_\lambda J\} = c_0 + c_1 \lambda + c_2 \lambda^2
   332	+ \cdots$ are $c_0 = 0$, $c_1 = k$, $c_n = 0$ for $n \ge 2$.
   333	
   334	\medskip
   335	\noindent\textbf{Step 2: The Laplace integral.}
   336	By Proposition~\ref{prop:field-theory-r}, the classical
   337	$r$-matrix is the Laplace transform of the $\lambda$-bracket
 succeeded in 50ms:
  2300	 at $g\ge 1$ it acquires curvature $\kappa\cdot\omega_g$.
  2301	\end{enumerate}
  2302	\end{construction}
  2303	
  2304	\begin{computation}[Modular extension of the Heisenberg
  2305	genus-zero package; \ClaimStatusProvedHere]
  2306	\label{comp:vol2-heisenberg-modular-extension}
  2307	\index{Heisenberg algebra!modular extension}
  2308	The Heisenberg genus-$0$ package has
  2309	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
  2310	$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
  2311	The modular extension:
  2312	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
  2313	$\kappa=k$,
  2314	$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
  2315	$\nabla^{\mathrm{hol}}_{0,n}
  2316	=d-k\sum_{i<j}q_iq_j\,d\log(z_i-z_j)$
  2317	(flat at all genera).
  2318	Shadow obstruction tower terminates at degree~$2$; all nonlinear
 succeeded in 51ms:
   780	 r_{mn} \;=\; k\,\kappa^{IJ}\,\delta_{m+n,0},
   781	\end{equation}
   782	where $\kappa^{IJ}$ is the inverse Killing form normalised by
   783	$\kappa^{IJ}\kappa_{JK} = \delta^I_K$, and
   784	$\Omega = \kappa^{IJ}\, t_I \otimes t_J$ is the Casimir tensor.
   785	\end{proposition}
   786	
   787	\begin{proof}
   788	The invariant bilinear form at level $k$ on $\fg$ is
   789	$(\cdot,\cdot)_k = k\,\kappa(\cdot,\cdot)$. The associated
   790	Casimir tensor is $\Omega_k = k\,\kappa^{IJ}\,t_I \otimes t_J
   791	= k\,\Omega$. The standard rational solution of the CYBE for
   792	$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
   793	This is confirmed by the Laplace transform
   794	\textup{(}Proposition~\textup{\ref{prop:field-theory-r}}\textup{)}:
   795	the $\lambda$-bracket $\{J^I{}_\lambda\, J^J\}
   796	= f^{IJ}{}_K\, J^K + k\,\kappa^{IJ}\,\lambda$ gives
   797	the Laplace kernel
   798	\[
   799	 r^L(z) \;=\; \frac{f^{IJ}{}_K\,J^K}{z}
 succeeded in 50ms:
  2398	\begin{computation}[Modular extension of the Heisenberg
  2399	genus-zero package; \ClaimStatusProvedHere]
  2400	% label removed: comp:vol2-heisenberg-modular-extension
  2401	\index{Heisenberg algebra!modular extension}
  2402	The Heisenberg genus-$0$ package has
  2403	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
  2404	The modular extension:
  2405	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
  2406	$\kappa=k$,
  2407	$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
  2408	$\nabla^{\mathrm{hol}}_{0,n}
  2409	=d-k\sum_{i<j}q_iq_j\,d\log(z_i-z_j)$
  2410	(flat at all genera).
  2411	Shadow obstruction tower terminates at degree~$2$; all nonlinear
  2412	shadows vanish.
  2413	\end{computation}
  2414	
  2415	\begin{computation}[Modular extension of the affine
  2416	genus-zero package; \ClaimStatusProvedHere]
  2417	% label removed: comp:vol2-affine-modular-extension
 succeeded in 51ms:
 27796	 its Koszul dual $B^{\mathrm{ord}}(\mathrm{Vir}_{13}^!)
 27797	 = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
 27798	 differential graded $E_1$-coalgebras, via the identity
 27799	 coming from the Feigin--Frenkel isomorphism
 27800	 $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
 27801	 $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
 27802	 the level-stripped form $r_0(z) = \Omega/z^3$ carries no
 27803	 $k$-dependence to correct and the scalar pole coefficient
 27804	 $\kappa = 13/2$ equals its dual partner.
 27805	\item \emph{Shadow obstruction tower \textup{(}rationality part,
 27806	 all degrees\textup{)}.}\enspace
 27807	 $S_r(\mathrm{Vir}_{13}) = S_r(\mathrm{Vir}_{13}^!)$ for all
 27808	 $r \geq 2$, as an identity of rational functions of~$c$
 27809	 evaluated at the fixed point of $c \mapsto 26 - c$.
 27810	\item \emph{Shadow trace formula \textup{(}low-degree, verified
 27811	 range\textup{)}.}\enspace
 27812	 The residue trace formula $\mathrm{RTF}(f) = 0$ vanishes for

thinking
**Analyzing bridging between r-matrix and KZ connection**

I'm examining whether the text explicitly connects the r-matrix form `kΩ/z` with the KZ connection denominator form `Ω/(k+h^∨)z`. While the source references both, it stops short of a direct bridging formula, suggesting an implicit identification. I'll verify if this counts as acceptable bridging or represents a mixing without explicit linkage, then continue checking other files for similar patterns.
exec
/bin/zsh -lc "rg -n \"r\\(z\" /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
83:up to normalization (in perturbation theory). The classical $r(z)=\frac{q_1 q_2}{z}$ satisfies CYBE.
87:For abelian Chern--Simons with HT boundary condition, conditional on Theorem~\ref{thm:physics-bridge}, the boundary category of line operators is braided by $R(z)$, with classical limit $r(z)=\frac{k}{z}$ (after normalization). The bulk chiral Hochschild cochains produce the same $r(z)$ via the Laplace transform of the bulk $\lambda$-bracket kernel as in Proposition~\ref{prop:field-theory-r}.
129:$r(z) = k/z^2$.
136:For $\beta\gamma$/$bc$: $\{b_\lambda c\} = 1$ gives $r(z) = 1/z$.
1197:r(z)
1244:  $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
2492:  r(z)
2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
2729:$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
2860:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
3150:\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
3280:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
3397:  $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
3441:  via the collision residue $r(z) = k\,\Omega/z$.
3470:classical limit: $r(z) = k\,\Omega/z$ is the classical
3744:  $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
3796:$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
4689:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
4759:\underset{\text{$r$-matrix}}{r(z)},\;\;
exec
/bin/zsh -lc "sed -n '60,120p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{proposition}[PVA for LG-cubic; \ClaimStatusConditional]
\label{prop:PVA-LG}
For the HT Landau--Ginzburg cubic model, conditional on Theorem~\ref{thm:physics-bridge}, $H^\bullet(A,Q)$ is a $(-1)$-shifted PVA with nontrivial bracket $\{\phi_\lambda \phi\}\sim \lambda\, \lambda^0$ (up to normalization), while $m_{k\ge3}$ vanish in cohomology.
\end{proposition}

\begin{proof}
The bracket originates from the singular residue of $m_2$; $m_3$ contributes homotopies only. Computation follows from the standard $\FM_3(\C)$ integral and the LG interaction vertex.
\end{proof}

\subsection{Abelian Chern--Simons with boundary}
\label{subsec:CS-abelian}
Let $A$ be abelian Chern--Simons theory on a half-space with HT boundary condition. The boundary algebra contains a current $J(z)$ with OPE
\[
J(z)J(w) \;\sim\; \frac{k}{(z-w)^2} + \text{regular},
\]
at level $k$ determined by the CS coupling.

\paragraph{Bulk-to-boundary and $R(z)$.}
Place two line operators of charges $q_1,q_2$ at $z_1,z_2$ on the boundary. The bulk-to-boundary kernel yields a spectral braiding
exec
/bin/zsh -lc "rg -n \"r\\(z\" /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
33:r(z) \;:=\; \lim_{\hh \to 0} \frac{R(z) - \id}{\hh}
39:$R(z) = \id + \hh\, r(z) + O(\hh^2)$.
50:r(z) \;=\; \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA),
70:Let $R(z) = \id + \hh\, r(z) + \hh^2\, s(z) + O(\hh^3)$ satisfy the
78:Then $r(z)$ satisfies the classical Yang--Baxter equation
90:by $r(z)$.
247:\begin{proposition}[Antisymmetry and unitarity of $r(z)$;
255:$r_{12}(z) + r_{21}(-z) = 0$, i.e., $r(-z) = -P \cdot r(z)
258:$r_{12}(z) + r_{12}(-z) = 0$ if $r(z)$ is skew-symmetric
259:($r_{12} = -r_{21}$), i.e., $r(z)$ is an odd function of~$z$.
261:If $r(z) = k\,\Omega/z + (\text{regular at } z = 0)$ with
281:= r_{12}(z)$, so $r_{12}(-z) = r_{12}(z)$. Combined: $r(z)$ is
283:$r_{21}(z) = P \cdot r(z) \cdot P$, the condition
340:r(z) = \int_0^\infty d\lambda\; e^{-\lambda z}\,
347:$r(z) = k\, (J \otimes J)/z^2$.
365:The CYBE~\eqref{eq:cybe-proved} for $r(z) = k\, (J \otimes J)/z^2$
380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
385:by its binary projection $r(z)$.
430:r(z) &= \int_0^\infty d\lambda\; e^{-\lambda z}\,
476:We verify~\eqref{eq:cybe-proved} for $r(z) = k\,\Omega/z$
exec
/bin/zsh -lc 'grep -n "Omega" /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
261:If $r(z) = k\,\Omega/z + (\text{regular at } z = 0)$ with
262:$\Omega = \Omega_{21}$ symmetric (e.g., $\Omega$ is a Casimir)
285:$k\,\Omega/z$ (level $k$) forces oddness if $\Omega$ is symmetric and
286:$r - k\,\Omega/z$ is regular.
288:(iii) Write $r_{12}(z) = k\,\Omega/z + r_{\mathrm{reg}}(z)$
289:at level $k$ Then $r_{21}(-z) = k\,\Omega_{21}/(-z) + r_{\mathrm{reg},21}(-z)
290:= -k\,\Omega/z + r_{\mathrm{reg},21}(-z)$ (using
291:$\Omega = \Omega_{21}$). The antisymmetry condition
404:\frac{k\,\Omega}{(k + h^\vee)\, z}
409:where $\Omega = \sum_a t^a \otimes t_a \in \fg \otimes \fg$ is the
412:$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
440:$\Omega/((k + h^\vee)z)$ at the classical level (the factor
446:tensor notation, $\sum_{a,b} f^{ab}_c\, t_a \otimes t_b = [\Omega,
448:with $\Omega/((k + h^\vee)z)$ follows from the defining property
451:property of $\Omega$.
476:We verify~\eqref{eq:cybe-proved} for $r(z) = k\,\Omega/z$
481:For $r_{ij} = k\,\Omega_{ij}/z_{ij}$, the CYBE reads
484:\frac{[\Omega_{12}, \Omega_{13}]}{z_{12}\, z_{13}}
485:+ \frac{[\Omega_{12}, \Omega_{23}]}{z_{12}\, z_{23}}
486:+ \frac{[\Omega_{13}, \Omega_{23}]}{z_{13}\, z_{23}}

exec
/bin/zsh -lc "sed -n '360,460p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
of a first-order OPE pole means $r^{\mathrm{coll}}$ has no
regular ($z^0$) term.

\medskip
\noindent\textbf{Step 4: CYBE verification.}
The CYBE~\eqref{eq:cybe-proved} for $r(z) = k\, (J \otimes J)/z^2$
reads
\[
\frac{k^2}{z_{12}^2 z_{13}^2}\, [J_1 J_2, J_1 J_3]
+ \frac{k^2}{z_{12}^2 z_{23}^2}\, [J_1 J_2, J_2 J_3]
+ \frac{k^2}{z_{13}^2 z_{23}^2}\, [J_1 J_3, J_2 J_3] = 0.
\]
Since $J$ is abelian (all commutators $[J_i, J_j] = 0$ as
operators in the classical limit), every commutator vanishes
identically. The Heisenberg satisfies the CYBE trivially: the
Gaussian $r$-matrix is an abelian solution.
\end{proof}

\begin{remark}[Shadow depth interpretation]
% label removed: rem:heisenberg-r-shadow-depth
exec
/bin/zsh -lc "rg -n \"r\\(z\" /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2229:$r(z) \in A^! \widehat\otimes A^!(\!(z^{-1})\!)$
2327:$\mathcal H(T)=(\cA,\cA^!_{\mathrm{line}},\cC,r(z),\Theta_\cA,
2345: & $r(z)=\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ \\
2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
2420:package has $r(z)=k\,\Omega/z$, $m_3\neq 0$ (cubic from Jacobi),
2901:$r(z)=k\,\Omega_{\mathfrak{sl}_3}/z$,
2941:$r(z)=(\beta\otimes\gamma'+\gamma\otimes\beta')/z$,
exec
/bin/zsh -lc "sed -n '2220,2445p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
are produced at all classical orders by homotopy transfer, and
boundary conditions identify the boundary chiral algebra with the
universal defect chiral algebra \textup{(Zeng)}.
\item Higher operations are computed by regularized Feynman diagrams
and satisfy quadratic consistency relations interpretable as higher
Wess--Zumino conditions \textup{(Gaiotto--Kulp--Wu)}.
\item The category of perturbative lines is equivalent to modules
for a Koszul-dual $A_\infty$-algebra $A^!$, and the OPE of lines
is controlled by a dg-shifted Yangian with Maurer--Cartan kernel
$r(z) \in A^! \widehat\otimes A^!(\!(z^{-1})\!)$
solving an $A_\infty$-Yang--Baxter equation
\textup{(Dimofte--Niu--Py)}.
\item In twisted holography, Costello's $11$-dimensional
$\Omega$-background admits a five-dimensional noncommutative
Chern--Simons realization, and in the $M2$-brane example the
large-$K$ operator algebra is Koszul dual to the bulk algebra
and becomes a quantum double-loop algebra \textup{(Costello)}.
\end{enumerate}
\end{theorem}

exec
/bin/zsh -lc "rg -n \"r\\(z\" /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2145: $r(z) \in \cA^!_{\mathrm{line}} \widehat\otimes
2243:$\mathcal H(T)=(\cA,\cA^!_{\mathrm{line}},\cC,r(z),\Theta_\cA,
2261: & $r(z)=\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ \\
2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
2327:package has $r(z)=k\,\Omega/z$, $m_3\neq 0$ (cubic from Jacobi),
2838:$r(z)=k\,\Omega_{\mathfrak{sl}_3}/z$,
2878:$r(z)=(\beta\otimes\gamma'+\gamma\otimes\beta')/z$,
thinking
**Clarifying user needs**

I see the user wants to focus on finding issues and fixing them in one go, rather than getting every file correct. It feels essential to keep this broad scope in mind for a thorough approach rather than digging into each file individually. I want to ensure I’m addressing their needs efficiently while still being comprehensive, so I’ll think about how to balance thoroughness with the specific request.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' 'k/z\\"'^2'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\Omega/z\\"'^3|'"\\\\kappa\\\\,\\\\Omega/z\\"'^3|'"\\\\Omega/z\\"'^4'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**/*.tex' '\\\\Omega/z' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "zsh -lc 'comm -12 <(rg -l --glob \"chapters/**/*.tex\" \"k["'^[:alpha:]]*'"\\\\Omega/z|k\\\\,\\\\Omega/z|k\\\\Omega/z\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | sort) <(rg -l --glob \"chapters/**/*.tex\" \"\\\\Omega/\\\\(\\\\(k\\\\+h\\"'^v'"\\\\)\\\\*?z\\\\)|\\\\Omega/\\\\(\\\\(k\\\\+h\\\\"'^'"\\\\vee\\\\)\\\\*?z\\\\)|\\\\Omega/\\\\(k\\\\+h\\\\"'^'"\\\\vee\\\\)\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | sort)'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27801: $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27802: the level-stripped form $r_0(z) = \Omega/z^3$ carries no
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:2363:$k/z^2$ and hence a wrong pole structure.
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:1687: $r^{\mathrm{L}}(z) = k/z^2$ \\
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2821: r^{\mathrm{KM}}(z) = k\,\Omega/z
/Users/raeez/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex:2867: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5003:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5018:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5022:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:3600:$r^{\mathrm{cl}}(z) = k\Omega/z$ of an affine algebra
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:3617:$r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$ has vanishing second
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3271:$r$-matrix is level-stripped, $r(z) = 0 \cdot \Omega/z = 0$,
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3399:$r$-matrix $k\,\Omega/z$ must vanish at zero level. The second
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27801: $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27802: the level-stripped form $r_0(z) = \Omega/z^3$ carries no
/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex:1074:$k\,\Omega/z$ with a single pole. For the Virasoro OPE with $z^{-4},
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1094:\emph{At $k = 0$} the $r$-matrix $r_k(z) = k\,\Omega/z$ vanishes
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1285:where $r_k(z) = k\,\Omega/z$ is the level-$k$ classical $r$-matrix
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1431:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1434:discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1508:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1647:the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
 succeeded in 50ms:
rg: regex parse error:
    (?:k[^[:alpha:]]*\Omega/z|k\,\Omega/z|k\Omega/z)
                     ^^
error: unrecognized escape sequence
rg: regex parse error:
    (?:\Omega/\(\(k\+h\^v\)\*?z\)|\Omega/\(\(k\+h\^\vee\)\*?z\)|\Omega/\(k\+h\^\vee\))
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"r\\(z\" /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
11:The Yangian $Y(\fg)$ is the universal quantization of the classical $r$-matrix $r(z) = k\,\Omega/z$. Yet the RTT formalism that defines it treats the spectral parameter $z$ as a formal variable, the Hopf coproduct as a given axiom, and the Yang--Baxter equation as a constraint to be verified. None of these are \emph{explained}: the spectral parameter has no geometric origin, the Hopf coproduct has no universal property, and the YBE is an identity without a cause.
40:For $\cH_k$ at level $k$: the OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole; the $d\log$ kernel absorbs one power ($\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$), so the collision residue is $r(z) = k/z$. At $k=0$ the $r$-matrix vanishes: the abelian limit produces the trivial braiding. For $k\ne 0$, the spectral braiding is
42:R(z) = e^{r(z)} = e^{k\hbar/z},
48:For $V_k(\mathfrak{sl}_2)$, the collision residue is $r(z) = k\,\Omega/z$, where $\Omega = \sum e_a \otimes e^a \in \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$ is the Casimir tensor. Again $k=0$ gives $r=0$. At leading order, $R(z) = 1 + \hbar\, k\,\Omega/z + \cdots$ is the Yang $R$-matrix. The YBE at order $\hbar^2$ reduces to the infinitesimal braid relation $[\Omega_{12},\, \Omega_{13} + \Omega_{23}] = 0$, which is the Jacobi identity on $\mathfrak{sl}_2$. This is class~L: depth $1$, the $r$-matrix carries non-trivial Lie structure, but the twisted coproduct $\Delta_z$ on the Koszul dual is still cocommutative at the classical level.
165:\subsection{Classical limit and the infinitesimal $r(z)$}
167:The quantum $R(z)$ carries the full braiding; the classical $r(z)$ carries the infinitesimal data that determines it. Let $\hbar$ denote the loop parameter of the perturbative HT theory.
170:R(z) \;=\; \mathrm{id} \,+\, \hbar\, r(z) \,+\, O(\hbar^2)
173:The order-$\hbar^2$ term of the YBE forces $r(z)$ to satisfy the classical Yang--Baxter equation with spectral parameter:
179:The field-theoretic content of $r(z)$ is sharper: it is the Laplace transform of the $\lambda$-bracket.
181:\begin{proposition}[Field-theoretic expression for $r(z)$;
187:r(z) \;=\; \int_{0}^{\infty} \! \mathrm{d}\lambda\ \mathrm{e}^{-\lambda z}\ \bigl\{\; \cdot {}_\lambda \cdot \;\bigr\},
197:Write $R(z) = \id + \hh\, r(z) + O(\hh^2)$ in $\End(L_1 \otimes L_2)$. At tree level ($\hh^0$), line operators compose freely and $R = \id$. The first quantum correction $r(z)$ is computed by a single bulk-to-boundary propagator exchange: a bulk operator propagates from position $z_1$ on line $L_1$ to position $z_2$ on line $L_2$ (with $z = z_1 - z_2$) through the half-space $\C \times \R_{\geq 0}$.
215:The first-order braiding $r(z)$ is obtained by evaluating the single-exchange diagram. Performing the $t$-integration with the exponential weight $e^{-zt}$ from the spectral parameter gives
217:r(z) = \int_0^\infty d\lambda\; e^{-\lambda z}\, \{\ \cdot{}_\lambda \cdot\ \}.
226:For the free propagator $K(z,t) = \Theta(t)/(2\pi z)$, the $\lambda$-bracket is $\lambda$-independent and the Laplace integral evaluates to $r(z) \sim 1/z$ (consistent with the abelian CS result of Example~\ref{ex:Heisenberg_Yangian}).
230:The formula $r(z) = \int_0^\infty e^{-\lambda z} \{\cdot{}_\lambda \cdot\}\, d\lambda$ is the passage between the PVA world (spectral variable~$\lambda$) and the $R$-matrix world (position variable~$z$): the two colours of the Swiss-cheese operad made analytic. The $\lambda$-bracket encodes holomorphic (closed-colour) singularities; $R(z)$ encodes topological (open-colour) braiding. The topological direction supplies the integration contour; the holomorphic direction supplies the meromorphic structure. Under DK-0, the Laplace transform recovers the classical $r$-matrix from the $\lambda$-bracket at the evaluation locus. The Laplace transform \emph{is} the spectral duality of the HT theory.
247:Substituting $R(z) = \id + \hh\, r(z) + O(\hh^2)$ into the quantum YBE (Theorem~\ref{thm:YBE}), expanding to order $\hh^2$, and using $R_{ij} R_{ik} R_{jk} = R_{jk} R_{ik} R_{ij}$:
272:Let $\mathcal C_{\partial}$ be the derived category of boundary line operators with the tensor structure induced by the $W$-module structure of~$M$. Then $R(z)$ defines a meromorphic braiding on $\mathcal C_{\partial}$, and the classical limit $r(z)$ integrates to a filtered quasi-triangular structure on~$\mathcal H$.
296:The classical $r$-matrix $r(z)$ defines an element $r(z) \in \mathcal{H} \widehat{\otimes}\, \mathcal{H}((z^{-1}))$ satisfying:
300:\item The intertwining property $r(z)\,\Delta(x) - \Delta^{\mathrm{op}}(x)\,r(z) = 0$ at leading order in $\hh$, which follows directly from defining $\Delta$ by the two-line OPE and $R(z)$ by the braiding that exchanges the two line factors.
exec
/bin/zsh -lc "sed -n '392,420p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:affine-monodromy-identification} verifies that
the half-monodromy equals
$\exp(-\pi i\, \Omega/(k + h^\vee))$, which by the Drinfeld--Kohno
theorem is the quantum group $R$-matrix of $U_q(\fg)$ at
$q = e^{i\pi/(k+h^\vee)}$.  This is the content of the classical
Drinfeld--Kohno theorem, recast here as an instance of
Proposition~\ref{prop:spectral-to-categorical}: the spectral
$R$-matrix is the KZ connection form, and the categorical braiding
is its monodromy.

For non-Koszul algebras (class~$M$: $m_k \neq 0$ for $k \geq 3$),
the resolution hypothesis may fail, and the reduced braiding
receives contributions from the full $A_\infty$ tower.  The
spectral-to-categorical passage in this regime requires the
$A_\infty$ Yang--Baxter defect to vanish after projection
(Theorem~\ref{thm:first-obstruction}), and is the subject of
Conjecture~\ref{conj:rmatrix}.
\end{remark}

\begin{remark}[The $r$-matrix and the chiral coproduct]
exec
/bin/zsh -lc "rg -n \"r\\(z\" /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3211:$\kappa(\cA) = \operatorname{av}(r(z))$, and the right-hand
3271:$r$-matrix is level-stripped, $r(z) = 0 \cdot \Omega/z = 0$,
3385:\operatorname{av}(r(z))
3395:$\operatorname{av}(r(z)) = \dim(\fg)\,k/(2 h^\vee)$ is the
14071: the dg-shifted Yangian $r(z)$ is the genus-$0$, degree-$2$ primitive
14098: $r$-matrix: $K_{0,2}^{\cA,E_1} = r(z)$.
14480:$K_{0,2}^{\cA,E_1} = r(z)$ is the classical $r$-matrix,
14872:Theorem~D extracts the scalar $\kappa = \operatorname{av}(r(z))$
27801: $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
28785:$\Theta_2 \mapsto r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
33611:%   r(z,w) = hbar * S_2(z,w) * Omega (KZ convention).
exec
/bin/zsh -lc "sed -n '33560,33640p' /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Koszulness of $V_k(\mathfrak{sl}_2)$
(equation~\eqref{eq:bar-degree1-yangian}). The de~Rham
Betti numbers of $\Sigma_2$ are $(1, 4, 1)$, and
the K\"unneth formula gives $6 = 1 + 4 + 1$ copies of
$s^{-1}\mathfrak{sl}_2$.
\end{proof}

\begin{remark}[Comparison with genus~$0$ and genus~$1$]
At genus~$0$, the degree-$1$ cohomology is
$3$-dimensional ($1$ copy of $s^{-1}\mathfrak{sl}_2$
from $H^0(D^\times)$, with additional degree-$1$
contribution from the circle). At genus~$1$, the Betti
numbers $(1,2,1)$ give $12 = 4 \cdot 3$. At genus~$2$,
the Betti numbers $(1,4,1)$ give $18 = 6 \cdot 3$. The
pattern at genus~$g$ is
$\dim H^*(\cC_1^{\mathrm{ord}}) = 3(2g + 2)$ from
$\dim H^*(\Sigma_g) = 2 + 2g$, reflecting the $2g$
extra $1$-cycles on $\Sigma_g$.
\end{remark}

exec
/bin/zsh -lc "rg -n -P --glob 'chapters/**/*.tex' 'Heisenberg.*k/z\\"'^2|r_'"\\{\\\\cH_k\\}\\(z\\)\\s*=\\s*\\\\frac\\{k\\}\\{z\\"'^2'"\\}|r\\(z\\)=k/z\\"'^2'"' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -l -P --glob 'chapters/**/*.tex' '\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\*?z\\)|\\\\Omega/\\(\\(k\\+2\\)z\\)|\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | sort" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -l -P --glob 'chapters/**/*.tex' 'k\\s*\\\\Omega/z' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups | sort" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections10_13_draft.tex
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex
/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex
/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
exec
/bin/zsh -lc "rg -n \"k \\+ h\" /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
535:The \emph{modular characteristic} $\kappa(\cA)$ (Volume~I, Theorem~D) is the unique scalar such that the bar differential satisfies $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \geq 1$, where $\omega_g = c_1(\lambda) \in H^2(\overline{\cM}_g, \Z)$ is the first Chern class of the Hodge bundle. For $\cA = \cH_k$: $\kappa(\cH_k) = k$. For $\cA = \hat{\fg}_k$ with simple~$\fg$: $\kappa(\hat{\fg}_k) = \dim\fg \cdot (k + h^\vee)/(2h^\vee)$.

Plan update
Reviewed the requested files and captured the relevant r-matrix statements; no conflicts found.
  ✓ Inspect each target file for KM/Heis/Vir r-matrix entries and note conventions/bridges
thinking
**Analyzing Heisenberg results**

I'm thinking about the absence of Heisenberg k/z^2 results related to the regex. It could be due to the lack of spaces or something else. My best guess is to search for simpler queries within volume 2 of my findings. I want to make sure I’m thorough, so I’ll explore every possible angle to understand why those results aren’t showing. Let's keep investigating!
exec
/bin/zsh -lc "rg -n 'k/z\\"'^2'"' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k/z\\"'^2'"' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2026:$r^L(z)$\,$^*$ & $k/z^2$ & $1/z^2$ & n/a & $k/z^2$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:790:$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2026:$r^L(z)$\,$^*$ & $k/z^2$ & $1/z^2$ & n/a & $k/z^2$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:790:$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1495,1545p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1495	The MC equation
  1496	$D\alpha_T + \tfrac{1}{2}[\alpha_T, \alpha_T] = 0$ decomposes as
  1497	\begin{alignat}{2}
  1498	\label{eq:intro-mc-closed}
  1499	&D\alpha_T^{\mathrm{cl}}
  1500	 + \tfrac{1}{2}[\alpha_T^{\mathrm{cl}},
  1501	 \alpha_T^{\mathrm{cl}}] &&= 0, \\
  1502	\label{eq:intro-mc-mixed}
  1503	&d_{\Theta}\,\alpha_T^{\mathrm{mix}} &&= 0, \\
  1504	\label{eq:intro-mc-open}
  1505	&d_{\Theta}\,\alpha_T^{\mathrm{op}}
  1506	 + [\alpha_T^{\mathrm{mix}},
  1507	 \alpha_T^{\mathrm{op}}]
  1508	 + \tfrac{1}{2}[\alpha_T^{\mathrm{mix}},
  1509	 \alpha_T^{\mathrm{mix}}]_{\mathrm{op}}
  1510	 + \tfrac{1}{2}[\alpha_T^{\mathrm{op}},
  1511	 \alpha_T^{\mathrm{op}}] &&= 0,
  1512	\end{alignat}
  1513	where $\Theta_\cA := \alpha_T^{\mathrm{cl}}$ is the closed-colour component and
  1514	$d_\Theta = D + [\Theta_\cA, -]$ is the
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '70,110p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    70	\subsection{Abelian Chern--Simons with boundary}
    71	\label{subsec:CS-abelian}
    72	Let $A$ be abelian Chern--Simons theory on a half-space with HT boundary condition. The boundary algebra contains a current $J(z)$ with OPE
    73	\[
    74	J(z)J(w) \;\sim\; \frac{k}{(z-w)^2} + \text{regular},
    75	\]
    76	at level $k$ determined by the CS coupling.
    77	
    78	\paragraph{Bulk-to-boundary and $R(z)$.}
    79	Place two line operators of charges $q_1,q_2$ at $z_1,z_2$ on the boundary. The bulk-to-boundary kernel yields a spectral braiding
    80	\[
    81	R(z)\cdot (v_{q_1}\otimes v_{q_2}) \;=\; \exp\!\Bigl( \hbar\, \frac{q_1 q_2}{z} \Bigr) \,(v_{q_2}\otimes v_{q_1}),
    82	\]
    83	up to normalization (in perturbation theory). The classical $r(z)=\frac{q_1 q_2}{z}$ satisfies CYBE.
    84	
    85	\begin{proposition}[Boundary Kac--Moody and spectral $R$; \ClaimStatusConditional]
    86	\label{prop:CS-R}
    87	For abelian Chern--Simons with HT boundary condition, conditional on Theorem~\ref{thm:physics-bridge}, the boundary category of line operators is braided by $R(z)$, with classical limit $r(z)=\frac{k}{z}$ (after normalization). The bulk chiral Hochschild cochains produce the same $r(z)$ via the Laplace transform of the bulk $\lambda$-bracket kernel as in Proposition~\ref{prop:field-theory-r}.
    88	\end{proposition}
    89	

exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '398,440p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   398	(with $k + h^\vee \ne 0$), the classical $r$-matrix is
   399	\begin{equation}
   400	% label removed: eq:affine-r-explicit
   401	\boxed{
   402	r_{\widehat{\fg}_k}(z)
   403	\;=\;
   404	\frac{k\,\Omega}{(k + h^\vee)\, z}
   405	\;+\;
   406	\frac{k\, \kappa}{z^2},
   407	}
   408	\end{equation}
   409	where $\Omega = \sum_a t^a \otimes t_a \in \fg \otimes \fg$ is the
   410	quadratic Casimir (with $t^a$ dual to $t_a$ under the Killing form
   411	$\kappa$), and $h^\vee$ is the dual Coxeter number. The simple pole
   412	$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
   413	pole $k\kappa/z^2$ is the Heisenberg-type (abelian Cartan)
   414	contribution.
   415	\end{theorem}
   416	
   417	\begin{proof}
thinking
**Inspecting theorem updates**

I need to check the file switches since there's already a bridge partially present in Step 3. I'll probably update the theorem or remark related to CYBE as well. I want to inspect more of the file and consider the affine theorem. The theorem seems to have mixed simple and double poles, creating some confusion around conventions. The user specifically mentioned cross-volume consistency, so I need to stay focused on that and follow the same conventions throughout. It's a real concern, so I should look at more lines after 400 to clarify.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2320,2360p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2320	\begin{construction}[From genus-zero package to holographic
  2321	modular Koszul datum; \ClaimStatusProvedHere]
  2322	% label removed: constr:genus-zero-to-hmkd
  2323	\index{holographic modular Koszul datum!from genus-zero package}
  2324	On that same scoped locus, the genus-zero package
  2325	$G_0(\mathcal T;B)$ embeds into the
  2326	holographic modular Koszul datum
  2327	$\mathcal H(T)=(\cA,\cA^!_{\mathrm{line}},\cC,r(z),\Theta_\cA,
  2328	\nabla^{\mathrm{hol}})$
  2329	of Vol~I (Definition~\ref*{V1-def:holographic-modular-koszul-datum})
  2330	by the following identifications:
  2331	\begin{center}
  2332	\renewcommand{\arraystretch}{1.15}
  2333	\begin{tabular}{ll}
  2334	\textbf{Genus-$0$ package} & \textbf{Holographic datum} \\
  2335	\hline
  2336	$V_\mathcal T$ (bulk chiral)
  2337	 & $\cA$ \\
  2338	$V_{\partial,\mathcal T}(B)$ (boundary)
  2339	 & $\cA$ restricted to $\{0\}\times X$ \\
codex
I have a definite active issue cluster now: several Vol II files still advertise Heisenberg `r(z)=k/z^2` as the `r`-matrix even when the same file elsewhere uses or derives the collision residue `k/z`, and Vol I’s Virasoro self-duality paragraph still carries a fake Casimir `\Omega`. I’m checking whether the affine theorem in the same Vol II chapter is also internally mixed before I patch the whole cluster.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '394,470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2230,2270p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   394	\begin{theorem}[Affine $r$-matrix from collision residue;
   395	\ClaimStatusProvedHere]
   396	% label removed: thm:affine-r-matrix
   397	For the affine Kac--Moody algebra $\widehat{\fg}_k$ at level $k$
   398	(with $k + h^\vee \ne 0$), the classical $r$-matrix is
   399	\begin{equation}
   400	% label removed: eq:affine-r-explicit
   401	\boxed{
   402	r_{\widehat{\fg}_k}(z)
   403	\;=\;
   404	\frac{k\,\Omega}{(k + h^\vee)\, z}
   405	\;+\;
   406	\frac{k\, \kappa}{z^2},
   407	}
   408	\end{equation}
   409	where $\Omega = \sum_a t^a \otimes t_a \in \fg \otimes \fg$ is the
   410	quadratic Casimir (with $t^a$ dual to $t_a$ under the Killing form
   411	$\kappa$), and $h^\vee$ is the dual Coxeter number. The simple pole
   412	$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
   413	pole $k\kappa/z^2$ is the Heisenberg-type (abelian Cartan)
exec
/bin/zsh -lc "rg -n 'Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)|Omega/\\(\\(k\\+2\\)|k\\\\,?\\\\Omega/z|k\\\\Omega/z' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  2230	two-leg projection is the modular expansion of
  2231	$r_{\mathcal{T}}(z)$, and whose generating Maurer--Cartan element
  2232	is precisely $\Theta_{\mathcal{A}}$ for the ambient
  2233	complementarity algebra attached to $A_{\partial,\mathcal{T}}$.
  2234	\end{conjecture}
  2235	
  2236	\begin{construction}[From genus-zero package to holographic
  2237	modular Koszul datum; \ClaimStatusProvedHere]
  2238	\label{constr:genus-zero-to-hmkd}
  2239	\index{holographic modular Koszul datum!from genus-zero package}
  2240	On that same scoped locus, the genus-zero package
  2241	$G_0(\mathcal T;B)$ embeds into the
  2242	holographic modular Koszul datum
  2243	$\mathcal H(T)=(\cA,\cA^!_{\mathrm{line}},\cC,r(z),\Theta_\cA,
  2244	\nabla^{\mathrm{hol}})$
  2245	of Volume~I
  2246	by the following identifications:
  2247	\begin{center}
  2248	\renewcommand{\arraystretch}{1.15}
  2249	\begin{tabular}{ll}
 succeeded in 50ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2327:package has $r(z)=k\,\Omega/z$, $m_3\neq 0$ (cubic from Jacobi),
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2420:package has $r(z)=k\,\Omega/z$, $m_3\neq 0$ (cubic from Jacobi),
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1529:$\alpha_T^{\mathrm{mix}} = k\,\Omega/z$, the level-weighted split Casimir; the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1532:for $r(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2027: $k\,\Omega/z$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:261:If $r(z) = k\,\Omega/z + (\text{regular at } z = 0)$ with
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:285:$k\,\Omega/z$ (level $k$) forces oddness if $\Omega$ is symmetric and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:286:$r - k\,\Omega/z$ is regular.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:288:(iii) Write $r_{12}(z) = k\,\Omega/z + r_{\mathrm{reg}}(z)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:290:= -k\,\Omega/z + r_{\mathrm{reg},21}(-z)$ (using
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:412:$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:476:We verify~\eqref{eq:cybe-proved} for $r(z) = k\,\Omega/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:531:for $r(z) = k\,\Omega/z$ at level $k$ follows: the three terms in the CYBE
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:791:$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1198:The $R$-matrix $R(z) = 1 + \hh\, \Omega/((k+h^\vee)z)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1498:$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3399:$r$-matrix $k\,\Omega/z$ must vanish at zero level. The second
collab wait(call_7weUiEpp0oCa2JTr1Soa3LyT)
  receivers: 019d87a1-de83-74c1-8295-501c295d3354
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '36,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    36	Two examples fix the picture.
    37	
    38	\medskip
    39	\noindent\textbf{Heisenberg.}
    40	For $\cH_k$ at level $k$: the OPE $J(z)J(w) \sim k/(z-w)^2$ has a double pole; the $d\log$ kernel absorbs one power ($\mathrm{pole}_r = \mathrm{pole}_{\mathrm{OPE}} - 1$), so the collision residue is $r(z) = k/z$. At $k=0$ the $r$-matrix vanishes: the abelian limit produces the trivial braiding. For $k\ne 0$, the spectral braiding is
    41	\[
    42	R(z) = e^{r(z)} = e^{k\hbar/z},
    43	\]
    44	scalar, and the Yang--Baxter equation holds tautologically. This is class~G: depth $0$, formal, all higher operations zero.
    45	
    46	\medskip
    47	\noindent\textbf{Affine $\mathfrak{sl}_2$.}
    48	For $V_k(\mathfrak{sl}_2)$, the collision residue is $r(z) = k\,\Omega/z$, where $\Omega = \sum e_a \otimes e^a \in \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$ is the Casimir tensor. Again $k=0$ gives $r=0$. At leading order, $R(z) = 1 + \hbar\, k\,\Omega/z + \cdots$ is the Yang $R$-matrix. The YBE at order $\hbar^2$ reduces to the infinitesimal braid relation $[\Omega_{12},\, \Omega_{13} + \Omega_{23}] = 0$, which is the Jacobi identity on $\mathfrak{sl}_2$. This is class~L: depth $1$, the $r$-matrix carries non-trivial Lie structure, but the twisted coproduct $\Delta_z$ on the Koszul dual is still cocommutative at the classical level.
    49	
    50	\medskip
    51	The pattern is uniform: the spectral parameter is the holomorphic coordinate $z$, the pole structure encodes the shadow class, and the $k=0$ collapse is the sanity check. The general definition is:
    52	
    53	\begin{definition}[Spectral braiding]
    54	\label{def:spectral-braiding}
    55	The \emph{spectral braiding} (or \emph{spectral $R$-matrix}) is the family of isomorphisms
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex | sed -n '168,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   168	Expand
   169	\[
   170	R(z) \;=\; \mathrm{id} \,+\, \hbar\, r(z) \,+\, O(\hbar^2)
   171	\]
   172	in endomorphisms of $L_1\otimes L_2$.
   173	The order-$\hbar^2$ term of the YBE forces $r(z)$ to satisfy the classical Yang--Baxter equation with spectral parameter:
   174	\[
   175	[ r_{12}(z_{12}), r_{13}(z_{13}) ] + [ r_{12}(z_{12}), r_{23}(z_{23}) ] + [ r_{13}(z_{13}), r_{23}(z_{23}) ] \;=\; 0.
   176	\]
   177	The CYBE is not an independent axiom; it is a theorem, inherited from Stokes on $\FM_3(\C)$.
   178	
   179	The field-theoretic content of $r(z)$ is sharper: it is the Laplace transform of the $\lambda$-bracket.
   180	
   181	\begin{proposition}[Field-theoretic expression for $r(z)$;
   182	\ClaimStatusProvedHere]
   183	\label{prop:field-theory-r}
   184	Let $A$ be a logarithmic $\SCchtop$-algebra.
   185	Let $\{\cdot{}_\lambda \cdot\}$ be the bulk $(-1)$-shifted $\lambda$-bracket on cohomology (Section~\ref{sec:Ainfty-to-PVA}). The infinitesimal spectral $r$-matrix is
   186	\[
   187	r(z) \;=\; \int_{0}^{\infty} \! \mathrm{d}\lambda\ \mathrm{e}^{-\lambda z}\ \bigl\{\; \cdot {}_\lambda \cdot \;\bigr\},
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex | sed -n '33580,33640p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 33580	% ----------------------------------------------------------------
 33581	\subsection{Degree $2$: the genus-$2$ KZB local system}
 33582	\label{subsec:g2-degree2}
 33583	
 33584	At degree~$2$, the configuration space
 33585	$\Conf_2^{\mathrm{ord}}(\Sigma_2) = \Sigma_2^2 \setminus
 33586	\Delta$ carries the KZB connection with non-trivial
 33587	pairwise interaction. After separating the
 33588	centre-of-mass coordinate (translation on $\Sigma_2$ via
 33589	the Jacobian $\mathrm{Jac}(\Sigma_2) =
 33590	\CC^2/(\ZZ^2 + \Omega\,\ZZ^2)$, which has dimension~$2$),
 33591	the relative configuration is a punctured
 33592	genus-$2$ surface:
 33593	the KZB local system lives on $\Sigma_2 \setminus \{0\}$,
 33594	a genus-$2$ surface with one puncture.
 33595	
 33596	The ordered chiral chain complex at degree~$2$ is
 33597	\begin{equation}\label{eq:g2-degree2-cx}
 33598	  \cC_2^{\mathrm{ord}}(\Sigma_2, Y_\hbar)
 33599	  = \Bigl(

thinking
**Summarizing classification and bridging details**

I’m putting together a final response that summarizes the classification for each file with clear bullet points referencing specific line ranges, highlighting how each file consistently uses bridging concepts like KZ normalization without mixing conventions. I’ll note no issues were found and provide concise file-by-file evidence as the developer requested.
codex
- `chapters/theory/introduction.tex:1499-1545` – internally consistent: the affine-KM segment lays out the MC split so `α_T^{\mathrm{mix}}=kΩ/z` is the r-matrix and immediately ties that component to the KZ connection `∇=d−Ω/(k+h^∨)d log z`, while the Virasoro paragraph explicitly flags the Laplace kernel `r^L(z)=(c/2)/z^4+…` and its collision shadow `(c/2)/z^3+2T/z`. No unbridged convention jumps occur.  
- `chapters/examples/examples-worked.tex:78-110` – consistent: the abelian CS example spells out that the boundary `R(z)` braiding is recovered by Laplace-transforming the bulk λ-bracket, and Proposition 2.2.5 then globally states the DK‑0 Laplace bridge between each λ-bracket and its classical `r(z)` for the five families.  
- `chapters/connections/thqg_spectral_braiding_extensions.tex:398-440` – consistent: the affine KM computation derives `r(z)=kΩ/((k+h^∨)z)+kκ/z^2` via the Laplace integral, so both the trace-form numerator and the Sugawara-shifted denominator appear together in the same derivation rather than being mixed without comment.  
- `chapters/connections/ht_bulk_boundary_line.tex:2324-2356` – consistent: the genus-zero package → holographic datum table identifies each line-OPE kernel with the collision residue `r(z)=Res_{0,2}Θ_A`, so the spectral `r(z)` inherits the collision convention by construction.  
- `chapters/connections/ht_bulk_boundary_line_frontier.tex:2240-2265` – consistent for the same reason; the same table is repeated with the collision-residue identification explicitly written, so there is no lurking mix of conventions.  
- `chapters/connections/spectral-braiding-core.tex:39-49,168-220` – consistent: the Heisenberg/Affine `r(z)=k/z` and `r(z)=kΩ/z` appear alongside the Laplace-transform formula `r(z)=∫_0^∞ e^{−λz}{·}_λ{·} dλ`, making the Laplace/collision relationship manifest and tying the spectral parameter to the underlying λ-bracket.  
- `chapters/theory/higher_genus_modular_koszul.tex:33581-33626` – consistent: the genus‑2 section spells out `r^{(g=2)} = ħS_2(z_i,z_j)Ω = (1/(k+h^∨)) d log E(z_i,z_j) Ω`, so the KZ-normalized denominator is present with the Casimir and the level shift noted, preventing any accidental mixing.

All files consistently document the relevant `r(z)` conventions and the bridges (Laplace vs. collision or trace-form vs. KZ) wherever the families are discussed, so no outstanding mixing issues were found.
wait(call_7weUiEpp0oCa2JTr1Soa3LyT) 1 agents complete:
  019d87a1-de83-74c1-8295-501c295d3354 completed: "- `chapters/theory/introduction.tex:1499-1545` – internally consistent: the affine-KM segment lays out the MC split so `…"

thinking
**Evaluating file consistency**

The explorer pointed out that some files are consistent, but there’s confusion with the thqg_spectral_braiding_extensions. The theorem's label mentions "from collision residue," yet the formula uses a Laplace mixture. I think the explorer might have misread this. We should exercise judgment here; while the system says to trust the explorer's results, I feel we need to verify them. There's direct evidence of inconsistency in the files, so I need to read more around the definitions to clarify the situation.
codex
The explorer is treating a few of these as “consistent” because the bridge exists somewhere nearby, but the local statements are still wrong on their own terms. I’m re-reading the exact package definitions in the Vol II connection chapters now; if a paragraph says “collision residue” and then writes `k/z^2`, that stays a live defect even if the file later explains the bridge.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2324,2360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2240,2268p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '780,798p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '2018,2032p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2324	On that same scoped locus, the genus-zero package
  2325	$G_0(\mathcal T;B)$ embeds into the
  2326	holographic modular Koszul datum
  2327	$\mathcal H(T)=(\cA,\cA^!_{\mathrm{line}},\cC,r(z),\Theta_\cA,
  2328	\nabla^{\mathrm{hol}})$
  2329	of Vol~I (Definition~\ref*{V1-def:holographic-modular-koszul-datum})
  2330	by the following identifications:
  2331	\begin{center}
  2332	\renewcommand{\arraystretch}{1.15}
  2333	\begin{tabular}{ll}
  2334	\textbf{Genus-$0$ package} & \textbf{Holographic datum} \\
  2335	\hline
  2336	$V_\mathcal T$ (bulk chiral)
  2337	 & $\cA$ \\
  2338	$V_{\partial,\mathcal T}(B)$ (boundary)
  2339	 & $\cA$ restricted to $\{0\}\times X$ \\
  2340	$A^!_\mathcal T$ (Koszul dual)
  2341	 & $\cA^!_{\mathrm{line}}$ \\
  2342	$\cC_\mathcal T$ (line category)
  2343	 & $\cC$ \\
 succeeded in 51ms:
  2240	On that same scoped locus, the genus-zero package
  2241	$G_0(\mathcal T;B)$ embeds into the
  2242	holographic modular Koszul datum
  2243	$\mathcal H(T)=(\cA,\cA^!_{\mathrm{line}},\cC,r(z),\Theta_\cA,
  2244	\nabla^{\mathrm{hol}})$
  2245	of Volume~I
  2246	by the following identifications:
  2247	\begin{center}
  2248	\renewcommand{\arraystretch}{1.15}
  2249	\begin{tabular}{ll}
  2250	\textbf{Genus-$0$ package} & \textbf{Holographic datum} \\
  2251	\hline
  2252	$V_\mathcal T$ (bulk chiral)
  2253	 & $\cA$ \\
  2254	$V_{\partial,\mathcal T}(B)$ (boundary)
  2255	 & $\cA$ restricted to $\{0\}\times X$ \\
  2256	$A^!_\mathcal T$ (Koszul dual)
  2257	 & $\cA^!_{\mathrm{line}}$ \\
  2258	$\cC_\mathcal T$ (line category)
  2259	 & $\cC$ \\
 succeeded in 51ms:
   780	\index{classical r-matrix!pole structure comparison}
   781	The pole structure of $r(z)$ at $z = 0$ encodes the conformal
   782	spin content of the chiral algebra:
   783	\begin{center}
   784	\small
   785	\renewcommand{\arraystretch}{1.15}
   786	\begin{tabular}{llll}
   787	\textbf{Family} & \textbf{Highest pole} & \textbf{Source} &
   788	\textbf{Shadow class} \\
   789	\hline
   790	$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
   791	$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
   792	$\beta\gamma_\lambda$ & $1/z$ [Laplace] & contact OPE & $C$ \\
   793	$\mathrm{Vir}_c$ & $c/(2z^4)$ [Laplace] & conformal anomaly $\lambda^3$ & $M$ \\
   794	$\mathcal{W}_N$ & $c_{W_N}/z^{2N}$ [Laplace] & spin-$N$ self-OPE & $M$ \\
   795	\end{tabular}
   796	\end{center}
   797	The pole order determines the leading behavior of the spectral
   798	$R$-matrix near the collision singularity. The shadow class
 succeeded in 51ms:
  2018	 \textbf{LG} & \textbf{CS} &
  2019	 \textbf{$\widehat{\fg}_k$} &
  2020	 \textbf{$\operatorname{Vir}_c$} \\
  2021	\hline
  2022	$m_{\geq 3}$ & $= 0$ & $= 0$ & finite & $= 0$ &
  2023	 $\neq 0$ & $\neq 0$, $\infty$ \\
  2024	PVA type & poly & poly & poly & poly &
  2025	 Lie & nonlinear \\
  2026	$r^L(z)$\,$^*$ & $k/z^2$ & $1/z^2$ & n/a & $k/z^2$ &
  2027	 $k\,\Omega/z$ &
  2028	 $\frac{c/2}{z^4} + \frac{2T}{z^2} + \frac{\partial T}{z}$ \\
  2029	$R(z)$ & $e^{k\hbar/z}$ & $e^{\hbar/z}$ & trivial & $e^{k\hbar/z}$ &
  2030	 Drinfeld & exp.\ model via fusion kernel \\
  2031	$\kappa$ & $k$ & $1$ & $0$ & $k$ &
  2032	 $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$ & $c/2$ \\

thinking
**Reviewing the formula**

I need to look at the wording regarding the collision residue and see if it can be adjusted minimally. It might also be important to state both the Laplace kernel and the collision residue in the affine theorem. I should inspect the lines starting from 467 to understand the exact final formula. There’s a bit more reading to do here to get it all right!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '467,540p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   467	The Laplace kernel~\eqref{eq:affine-r-explicit} reproduces these
   468	OPE poles. The bar-theoretic collision residue absorbs the
   469	$d\log$ measure, reducing pole orders by one: the double-pole
   470	term $k\kappa^{ab}/w^2$ becomes a simple pole in
   471	$r^{\mathrm{coll}}$, and the simple-pole structure-constant term
   472	becomes a regular contribution.
   473	
   474	\medskip
   475	\noindent\textbf{Step 4: CYBE verification.}
   476	We verify~\eqref{eq:cybe-proved} for $r(z) = k\,\Omega/z$
   477	at level $k$ suppressing the overall $(k+h^\vee)^{-1}$ and the double-pole term, which
   478	satisfies the CYBE independently by the abelian argument of
   479	Proposition~\ref{V1-prop:heisenberg-r-matrix}.
   480	
   481	For $r_{ij} = k\,\Omega_{ij}/z_{ij}$, the CYBE reads
   482	\[
   483	k^2\left(
   484	\frac{[\Omega_{12}, \Omega_{13}]}{z_{12}\, z_{13}}
   485	+ \frac{[\Omega_{12}, \Omega_{23}]}{z_{12}\, z_{23}}
   486	+ \frac{[\Omega_{13}, \Omega_{23}]}{z_{13}\, z_{23}}
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '539,575p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   539	\begin{remark}[The classical $r$-matrix for $\widehat{\mathfrak{sl}_2}_k$]
   540	% label removed: rem:sl2-r-matrix-explicit
   541	\index{classical r-matrix!$\mathfrak{sl}_2$}
   542	For $\fg = \mathfrak{sl}_2$ with standard generators $e, f, h$
   543	and Killing form $\kappa(h,h) = 2$, $\kappa(e,f) = 1$, the Casimir
   544	is $\Omega = h \otimes h/2 + e \otimes f + f \otimes e$. The
   545	$r$-matrix is
   546	\[
   547	r_{\widehat{\mathfrak{sl}_2}_k}(z)
   548	= \frac{1}{(k+2)z}
   549	\left(\frac{h \otimes h}{2} + e \otimes f + f \otimes e\right)
   550	+ \frac{k}{z^2}\,\kappa,
   551	\]
   552	where $h^\vee = 2$ for $\mathfrak{sl}_2$. This is the rational
   553	$r$-matrix of the Yangian $Y(\mathfrak{sl}_2)$, recovered from the
   554	collision residue of the OPE
   555	$J^a(z_1)\, J^b(z_2) \sim f^{ab}_c\, J^c/(z_1 - z_2) +
   556	k\,\kappa^{ab}/(z_1 - z_2)^2$.
   557	\end{remark}
   558	

thinking
**Evaluating inconsistencies**

I'm noticing that this chapter has some significant inconsistencies. I think I need to address the theorem and the remarks that could be confusing. It seems like it might be more than what the user can handle right now. I wonder if the introduction might also have similar issues, especially for affine topics. Perhaps I should look around pages 1499-1545 to find more context. I’ll read through it to identify potential inconsistencies.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1498,1545p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1498	\label{eq:intro-mc-closed}
  1499	&D\alpha_T^{\mathrm{cl}}
  1500	 + \tfrac{1}{2}[\alpha_T^{\mathrm{cl}},
  1501	 \alpha_T^{\mathrm{cl}}] &&= 0, \\
  1502	\label{eq:intro-mc-mixed}
  1503	&d_{\Theta}\,\alpha_T^{\mathrm{mix}} &&= 0, \\
  1504	\label{eq:intro-mc-open}
  1505	&d_{\Theta}\,\alpha_T^{\mathrm{op}}
  1506	 + [\alpha_T^{\mathrm{mix}},
  1507	 \alpha_T^{\mathrm{op}}]
  1508	 + \tfrac{1}{2}[\alpha_T^{\mathrm{mix}},
  1509	 \alpha_T^{\mathrm{mix}}]_{\mathrm{op}}
  1510	 + \tfrac{1}{2}[\alpha_T^{\mathrm{op}},
  1511	 \alpha_T^{\mathrm{op}}] &&= 0,
  1512	\end{alignat}
  1513	where $\Theta_\cA := \alpha_T^{\mathrm{cl}}$ is the closed-colour component and
  1514	$d_\Theta = D + [\Theta_\cA, -]$ is the
  1515	$\Theta_\cA$-twisted differential.
  1516	
  1517	Equation~\eqref{eq:intro-mc-closed} is the modular MC equation
codex
I’ve confirmed one more class of issue: some files are not numerically wrong, but they do switch between trace-form `k\,\Omega/z` and KZ `\Omega/((k+h^\vee)z)` without stating the bridge identity the repo requires. I’m sampling the small set of live chapter files that contain both forms so I can patch only the actual misses.
exec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\\\*?z\\)|k\\\\Omega_tr|Omega_tr' /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\\\*?z\\)|k\\\\Omega_tr|Omega_tr' /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\\\*?z\\)|k\\\\Omega_tr|Omega_tr' /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex /Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\\\*?z\\)|k\\\\Omega_tr|Omega_tr' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1655:$r(z) = \Omega/((k+h^\vee)z)$
1680:level-$k$ rational $r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$
1713:$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
4410: r-matrix $r(z) = k\Omega/z$
4731: $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
4733: level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
4764:The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
4765:$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1139:$r(z) = k\Omega/z$ (the double pole $k\,g^{ab}/(z{-}w)^2$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1142:equation for $r(z) = k\Omega/z$ reduces to the infinitesimal braid
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1198:$G_2$ ($V = \bC^{7}$). The classical $r$-matrix $r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1213:$R$-matrix $r(z) = k\Omega/z$ of
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:717:The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:799:$r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:862:$r(z) = k\Omega/z$ of
 succeeded in 52ms:
524:$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
578:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
592:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
601:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
672:$r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
780:$\Omega/((k+h^\vee)z) \mapsto r_\cA(z)$, which is the first term of
976: expansion $r^{\mathrm{Dr}}(z) = k\Omega/z = k\Omega \cdot \hbar$
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:261:If $r(z) = k\,\Omega/z + (\text{regular at } z = 0)$ with
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:285:$k\,\Omega/z$ (level $k$) forces oddness if $\Omega$ is symmetric and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:286:$r - k\,\Omega/z$ is regular.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:288:(iii) Write $r_{12}(z) = k\,\Omega/z + r_{\mathrm{reg}}(z)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:290:= -k\,\Omega/z + r_{\mathrm{reg},21}(-z)$ (using
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:412:$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:476:We verify~\eqref{eq:cybe-proved} for $r(z) = k\,\Omega/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:531:for $r(z) = k\,\Omega/z$ at level $k$ follows: the three terms in the CYBE
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:791:$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1198:The $R$-matrix $R(z) = 1 + \hh\, \Omega/((k+h^\vee)z)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:1498:$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1529:$\alpha_T^{\mathrm{mix}} = k\,\Omega/z$, the level-weighted split Casimir; the
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1532:for $r(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2027: $k\,\Omega/z$ &
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:183:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:226:If $r(z)=k\,\Omega/z+O(1)$ at level~$k$ near $z=0$ and $\Omega_{ij}$ denotes the action of $\Omega$ in factors $i,j$, then
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:273:with $u_{ij}$ a unit. Since $r(z)=k\,\Omega/z+O(1)$ at level~$k$ one has
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1574: R(z)=1+k\,\Omega/z+O(z^{-2})
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1736:$\wp$-function. (The genus-$0$ collision residue is $r(z) = k\,\Omega/((k+h^\vee)z)$; the intrinsic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1914:$r(z) = k\,\Omega/z$ at level~$k$ up to scalars.

thinking
**Inspecting file issues**

I see that the output mentions files in vol1, indicating there's a concern about the forms and possibly missing a bridge. I’ll need to check the specific files: frontier_modular_holography_platonic, holographic_datum_master, and yangians_computations. Since the user requested all three volumes, I might need to implement a patch. I should figure out if a bridge is genuinely missing in these files, so I'll start by looking at snippets around the relevant occurrences. I'll use sed to analyze the lines.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1648,1720p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex | sed -n '516,610p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex | sed -n '708,808p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1648	 $\cA^!_{\mathrm{line}}$ acting at spectral separation $z_{ij}$.
  1649	\item The quantization parameter is $\hbar = 1/(k+h^\vee)$.
  1650	\end{enumerate}
  1651	\end{theorem}
  1652	
  1653	\begin{proof}
  1654	Part~(i): substituting the Casimir collision residue
  1655	$r(z) = \Omega/((k+h^\vee)z)$
  1656	\textup{(}Theorem~\textup{\ref{thm:yangian-shadow-theorem}}\textup{)}
  1657	into the depth-$1$ Hamiltonian formula yields exactly the Gaudin
  1658	Hamiltonian of \cite{FFR94} multiplied by $1/(k+h^\vee)$.
  1659	
  1660	Part~(ii): by Theorem~\textup{\ref{thm:gz26-commuting-differentials}}(ii),
  1661	the depth-$k$ contribution to $H_i$ is the collision residue at depth
  1662	$k$. Each such residue is the $m_k$ operation transferred via the
  1663	Homological Perturbation Lemma to the cohomology, viewed as a
  1664	spectral-parameter deformation of the classical $m_2$.
  1665	
  1666	Part~(iii): the prefactor $1/(k+h^\vee)$ is the Drinfeld quantization
  1667	parameter \cite{Drinfeld85}.
 succeeded in 50ms:
   516	$d\log(z-w)$ absorbs one power, so the collision residue
   517	extracts the simple-pole coefficient: the zeroth product
   518	$a_{(0)}b = f^{ab}_{\;\;c} J^c$ (the Lie bracket). The double-pole
   519	term $k\,\delta^{ab}$ contributes to the curvature~$m_0$, not to
   520	the collision residue
   521	(Computation~\ref{comp:sl2-collision-residue-kz}, Step~2).
   522	Dualizing via the level-shifted Killing form $(k+h^\vee)\kappa$
   523	(the Sugawara normalization) gives the Casimir $r$-matrix
   524	$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
   525	At the critical level $k = -h^\vee$ the denominator vanishes,
   526	tracking the Sugawara singularity.
   527	At $k = 0$ the collision residue is $\Omega/(h^\vee z) \neq 0$:
   528	the Lie bracket of~$\fg$ persists at vanishing level, so the
   529	abelian vanishing $r = 0$ that characterizes the Heisenberg
   530	$r$-matrix does not hold for non-abelian Kac--Moody.
   531	The Yang--Baxter equation is then the IBR of
   532	Theorem~\ref{thm:collision-depth-2-ybe} after evaluation against
   533	the Casimir, which is the pure algebraic content of the Arnold
   534	relation tensored with the structure constants of~$\fg$. The full
   535	derivation is the shadow/KZ comparison theorem
 succeeded in 51ms:
   708	appears as a degree-2 cocycle condition with a shift
   709	in the spectral parameter filtration.
   710	\end{computation}
   711	
   712	
   713	\subsection{Quantum \texorpdfstring{$R$}{R}-matrix from the bar complex}
   714	\label{subsec:quantum-rmatrix-bar}
   715	\index{R-matrix!quantum!from bar complex}
   716	
   717	The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
   718	normalisation; Remark~\ref{rem:km-collision-residue-rmatrix}) is the leading-order
   719	collision residue. The quantum $R$-matrix arises from the
   720	$\hbar$-expansion of the bar-complex MC element, where
   721	$\hbar = \pi i/(k + h^\vee)$.
   722	
   723	\begin{proposition}[Classical and quantum $R$-matrices from the
   724	bar complex; \ClaimStatusProvedHere]
   725	\label{prop:rmatrix-from-bar}
   726	\index{R-matrix!from bar complex|textbf}
   727	\index{bar complex!R-matrix extraction}

thinking
**Inspecting search lines**

I'm noticing that the search lines show explicit KZ and trace forms. I think I need to consider adding a bridge in one or two sentences to connect my thoughts better. So, I'll take a moment to inspect the occurrences to see how they mix together. There seems to be a lot here to dive into, so I want to make sure I'm thorough in my analysis.
codex
I’ve reduced it to two kinds of live defects: outright wrong formulas (`k/z^2` advertised as a collision `r`-matrix, and `\kappa\,\Omega/z^3` in Virasoro) and unbridged KZ/trace switches in a few affine chapters. I’m reading the mixed affine passages now so I can decide whether a one-line bridge is enough or whether the local formula itself is wrong.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1708,1720p;4758,4768p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex | sed -n '733,745p;792,802p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex | sed -n '572,604p;1710,1715p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1708	sigma-model coupling on $\bC\times\bR_{\geq 0}$ is fixed by gauge
  1709	invariance to $1/(k+h^\vee)$ \textup{(\cite[\S\,2.2]{KhanZeng25})}.
  1710	The DNP\textup{25} perturbative expansion of line-operator OPE is organized
  1711	by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
  1712	The collision residue
  1713	$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
  1714	inherits its prefactor from the bar-complex normalization on
  1715	$\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
  1716	
  1717	The three independent constructions agree because they measure the
  1718	same algebraic datum: the level $k$ controls the normalization of the
  1719	chiral bracket $J^a_{(1)}J^b = k\delta^{ab}$, which propagates through
  1720	the Sugawara construction to the bar complex on our side, the 1-loop
  4758	with $\kappa(\mathfrak{sl}_N, k)
  4759	= (N^2{-}1)(k{+}N)/(2N)$ and
  4760	$\kappa(\mathfrak{u}(1), k) = k$
  4761	(the authoritative formulas from
  4762	Theorem~\ref{thm:modular-characteristic}).
  4763	
  4764	The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
 succeeded in 52ms:
   733	 The genus-$0$ binary collision residue of the bar-complex MC
   734	 element is
   735	 \begin{equation}\label{eq:classical-r-from-bar}
   736	 r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
   737	 = \frac{\Omega_\fg}{(k + h^\vee)\,z}
   738	 \;\in\; \fg \otimes \fg \otimes z^{-1}\bC[z^{-1}],
   739	 \end{equation}
   740	 where $\Omega_\fg = \sum_a \kappa^{ab}\, I_a \otimes I_b$ is the quadratic
   741	 Casimir tensor \textup{(}$\kappa^{ab}$ is the inverse Killing form\textup{)}
   742	 and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
   743	 product via the level-shifted Killing form
   744	 \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
   745	 In the fundamental representation of $\mathfrak{sl}_N$:
   792	Part~(i): The bar propagator
   793	$\eta_{12} = d\log(z_1 - z_2)$ absorbs one pole order from the
   794	affine OPE. The double pole $k\,g^{ab}/(z{-}w)^2$
   795	shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
   796	$f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
   797	absorption and drops. The degree-$2$ projection of the MC element
   798	therefore extracts only the Casimir part:
 succeeded in 52ms:
   572	
   573	\begin{theorem}[Face~6: Sklyanin bracket; \ClaimStatusProvedHere\ (identification with classical limit of collision residue); \ClaimStatusProvedElsewhere\ (Sklyanin bracket: Semenov-Tian-Shansky 1983)]
   574	\label{thm:hdm-face-6}
   575	For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
   576	$\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
   577	level-$k$ Drinfeld rational $r$-matrix
   578	$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
   579	limit of the collision residue $r_\cA(z)$ in the sense that the
   580	Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
   581	agrees with the leading-order term of $r_\cA(z)$ under the classical
   582	limit functor of Face~3 (genus~$0$ only). Equivalently, the Sklyanin bracket is the
   583	$\hbar \to 0$ limit of the Yangian quantum bracket
   584	$[\Delta_\hbar(x), y \otimes 1]/\hbar$, where $\Delta_\hbar$ is the
   585	Yangian coproduct of Drinfeld~\cite{Drinfeld85}.
   586	\end{theorem}
   587	
   588	\begin{proof}
   589	The Sklyanin bracket is constructed from a classical $r$-matrix
   590	$r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
   591	$\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For

thinking
**Inspecting code details**

I think I need to create minimal bridge statements for some parts. It seems like `log_ht_monodromy_core` might have both forms with a bridge, and I remember the explorer saying yes to that. There's something about line 1736 mentioning genus-0 collision residue with that formula, but it isn't entirely clear. I should check the code sections around lines 1728-1740 and 183 to gain better insight.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '176,186p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1728,1742p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   176	\]
   177	where $\rho_{ij}$ acts in factors $i$ and $j$ and trivially elsewhere.
   178	
   179	\begin{definition}[Shifted KZ/FM connection]
   180	The connection $\nabla_n^Y$ is called the \emph{shifted KZ/FM connection} attached to $Y$.
   181	\end{definition}
   182	
   183	When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
   184	
   185	\subsection{Flatness and residues}
   186	
 succeeded in 52ms:
  1728	 = \frac{k\,\Omega}{(k+2)z}
  1729	 - \frac{k\,\Omega}{k+2}\sum_{n=1}^{\infty}2\,
  1730	 \frac{q^{2n}}{1-q^{2n}}\cdot 2\pi i\cos(2\pi nz)
  1731	 = \frac{k\,\Omega}{(k+2)z}
  1732	 + \frac{k\,\Omega}{k+2}\bigl(2G_2(\tau)-\wp(z;\tau)-\pi^2/3\bigr),
  1733	\]
  1734	where the Eisenstein correction $G_2(\tau)$ accounts for the
  1735	(conditionally convergent) sum and $\wp$ is the Weierstrass
  1736	$\wp$-function. (The genus-$0$ collision residue is $r(z) = k\,\Omega/((k+h^\vee)z)$; the intrinsic
  1737	KZB connection~\eqref{eq:kzb-connection} retains the standard
  1738	Sugawara normalization $(k+h^\vee)^{-1}$, so the identification of
  1739	$r_1$ with the connection form carries the rescaling factor
  1740	$k/(k+h^\vee)$. At $k=0$ both the connection trivializes in the
  1741	collision sector and $r_1$ vanishes, consistent with
  1742	Theorem~\ref{thm:affine-monodromy-identification}.) Thus the

thinking
**Considering formulas and tasks**

I'm thinking about the explanation for the rescaling factor. The log_ht_monodromy_core seems okay, but I need to look at volume 1's introduction regarding the Heisenberg formula and the flagged kΩ/z in the audit. The user’s task involves reviewing Heis/KM/Vir r-matrix formulas across all three volumes. This is a current issue in volume 1 that hasn't been addressed yet. I should inspect the actual lines, especially line 1431 from our earlier search. I need to read through that carefully.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex | sed -n '1426,1450p;1504,1524p;1642,1652p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1426	\textsc{Information content.} An equivariant
  1427	$\End(V^{\otimes n})$-valued meromorphic function strictly
  1428	contains its scalar trace. The averaging map
  1429	$\operatorname{av}$ is surjective but not injective: the kernel
  1430	records the non-symmetric components of the line-operator data.
  1431	For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
  1432	the symmetrization recovers the scalar
  1433	$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
  1434	discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
  1435	full Yangian double; the symmetrization recovers
  1436	$\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
  1437	and discards the entire Drinfeld--Jimbo deformation.
  1438	
  1439	\textsc{Physical primacy.} The natural physical objects are
  1440	ordered. Three-dimensional holomorphic-topological theories
  1441	have line operators along the topological direction $\R_t$
  1442	(Costello--Gaiotto~\cite{CostelloGaiotto2020}); these line operators
  1443	form the ordered convolution algebra ${\gAmod}^{\Eone}$ on
  1444	$\C_z \times \R_t$, and their fusion is the
  1445	$\Eone$-multiplication. Open-string field theory and


thinking
**Fixing Heisenberg References**

I realize the introduction in volume 1 has a mistake regarding Heisenberg. To address this, I’ll need to perform a cross-volume search specifically for Heisenberg in the intro. I might use a command to find relevant mentions like `rg -n "Heisenberg.*Omega/z"`. There’s also a potential issue with a formula presented in the intro that diverges slightly from the canonical form. I’ll need to decide if that shorthand is acceptable or if it requires correction, especially since the user requested exact family formulas.
thinking
**Adjusting Formulas and Patches**

I’m considering adjusting line 1650 to use the explicit formula since the introduction has exact formulas in other places. This means changing it to `r(z) = (c/2)/z^3 + 2T/z`. I also want to review the Heisenberg references. I found several areas in volume 1 that need attention, including some shorthand formulas I should clarify. Additionally, I need to check other files for correctness regarding the conventions and bridges, especially if phrasing like "equivalently" is present.
exec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\\\*?z\\)|k/z\\"'^2|'"\\\\kappa\\\\,\\\\Omega/z\\"'^3|'"\\\\Omega/z\\"'^3'"' /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\\\*?z\\)|k/z\\"'^2|'"\\\\kappa\\\\,\\\\Omega/z\\"'^3|'"\\\\Omega/z\\"'^3'"' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:6051:The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. In the AP126 trace-form convention the classical $r$-matrix is still $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ it is $-h^\vee\,\Omega/z$, not $0$. The critical phenomenon is the vanishing of $\kappa_{\mathrm{ch}}$ and the resulting shadow/center degeneration encoded by $\Theta_A$, not a level-stripped disappearance of the affine collision residue.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex:377:Since $R^{E_2}(z) = k\,\Omega/z + O(1)$ with $\Omega$ the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1077: $z$-dependent $R$-matrix $r(z) = k\,\Omega/z$ is replaced by its
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:1360:$R$-matrix & $r(z) = k\,\Omega/z + \cdots$ & $R^{E_2}(z)$ (half-braiding) & $\mathrm{av}(r(z)) = \kappa_{\mathrm{ch}}$ (scalar) \\
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:524:$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:578:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:592:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:601:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:672:$r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:780:$\Omega/((k+h^\vee)z) \mapsto r_\cA(z)$, which is the first term of
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:976: expansion $r^{\mathrm{Dr}}(z) = k\Omega/z = k\Omega \cdot \hbar$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1655:$r(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1680:level-$k$ rational $r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1713:$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4410: r-matrix $r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4731: $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4733: level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4764:The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4765:$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:717:The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:799:$r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:862:$r(z) = k\Omega/z$ of
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1094:\emph{At $k = 0$} the $r$-matrix $r_k(z) = k\,\Omega/z$ vanishes
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1285:where $r_k(z) = k\,\Omega/z$ is the level-$k$ classical $r$-matrix
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex | sed -n '3388,3405p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3388	\;=\;
  3389	\kappa(V_k(\fg))
  3390	\;=\;
  3391	\frac{\dim(\fg)\,(k + h^\vee)}{2\,h^\vee}
  3392	\end{equation}
  3393	splits the holographic central charge into two pieces with
  3394	distinct bulk interpretations. The first summand
  3395	$\operatorname{av}(r(z)) = \dim(\fg)\,k/(2 h^\vee)$ is the
  3396	\emph{bare} boundary coupling: it is the level-dependent piece
  3397	seen directly by the $r$-matrix, and at $k = 0$ it vanishes,
  3398	consistent with the AP\textup{126} mandate that a level-stripped
  3399	$r$-matrix $k\,\Omega/z$ must vanish at zero level. The second
  3400	summand $\tfrac{1}{2}\dim(\fg)$ is the \emph{holographic anomaly
  3401	shift} from Sugawara normal-ordering: it is the bulk one-loop
  3402	renormalization of the stress tensor, independent of level, and
  3403	it records the quantum correction that promotes the classical
  3404	Chern--Simons action to its quantum counterpart. The sum is
  3405	the total holographic central charge~$\kappa(V_k(\fg))$.
exec
/bin/zsh -lc "rg -n 'Heisenberg.*Omega/z|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega/z|Heisenberg \\\\cH_k.*k\\\\,\\\\Omega/z|Heisenberg \\\\cH_k.*k\\\\Omega/z' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1431:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1508:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1647:the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
codex
I’m moving to edits. Before patching the hot-zone `r`-matrix surface, I’m locking the three family conventions explicitly so the fixes stay local and falsifiable.

```text
family: Heis  r(z): k/z  level param: k  OPE pole: 2  r pole: 1
convention: trace-form / collision residue
AP126 (trace-form): r|_{k=0} = 0  expected: 0  match? Y
AP141 grep: bare \Omega/z in scope: N  allowed? N
critical-level (KM): n/a
source: chapters/examples/landscape_census.tex:220-236; CLAUDE.md C10
verdict: ACCEPT
```

```text
family: affine KM  r(z): k\Omega_tr/z  level param: k  OPE pole: 2 and 1  r pole: 1
convention: trace-form, with KZ bridge \Omega/((k+h^\vee)z)
AP126 (trace-form): r|_{k=0} = 0  expected: 0  match? Y
AP141 grep: bare \Omega/z in scope: N  allowed? N
critical-level (KM): r|_{k=-h^\vee} = -h^\vee \Omega_tr/z in trace-form; KZ form diverges
source: chapters/examples/landscape_census.tex:225-230; CLAUDE.md C9
verdict: ACCEPT
```

```text
family: Vir  r(z): (c/2)/z^3 + 2T/z  level param: c  OPE pole: 4 and 2  r pole: 3 and 1
convention: collision residue after dlog absorption
AP126 (trace-form): n/a
AP141 grep: bare \Omega/z in scope: N  allowed? N
critical-level (KM): n/a
source: chapters/examples/landscape_census.tex:463-468; CLAUDE.md C11
verdict: ACCEPT
```


thinking
**Clarifying mathematical distinctions**

I’m making some adjustments to the text. I’ll modify the original statement about Heisenberg and sl2 shadows to clarify that while they have the same scaling in k, their support differs. The Heisenberg E1-shadow is scalar, and the sl2 shadow is matrix-valued. I’ll also note that the original claim about proportional κ-values might not hold accurately due to shifts. So, I can conclude by emphasizing the nonzero nature at genus 0 for both.
thinking
**Weighing kappa comparisons**

I think I might want to keep the comparison of kappa values, but I'll aim for a minimal edit for accuracy. I could simply replace the Heisenberg formula and clarify "matrix support." This way, I can maintain the essence of the original text without overcomplicating the message. It's all about being truthful and clear in the distinctions while still reflecting the mathematical relationships. I'll ensure the edit feels cohesive and straightforward!
codex
I’ve finished the read-through and I’m patching now. The edits are narrowly scoped: fix the Heisenberg collision-residue drift, remove the fake Virasoro Casimir, and insert explicit KZ/trace bridge identities exactly where a file switches normalization.

thinking
**Planning small patches**

It seems like the patch failed possibly due to an escaped foreground star. I think breaking the patch into smaller chunks could help. Also, applying the patch in parallel didn't work, which is essential to note. I might need to inspect the exact text with specific symbols on the same line. It seems we should patch carefully using smaller hunks, starting with specific files that are straightforward to modify.

thinking
**Troubleshooting patch issues**

It seems like the patch didn’t apply, possibly because the whole patch didn’t work as none of it was applied. I might need to create smaller, file-by-file patches, focusing on exact lines. I think using the exact context from the file could help, since spaces and newlines might differ. I'll try patching with less context or target specific lines. Starting with the vol1 intro or higher genus/yangians might be a good approach, but the patch aborted. So, I’ll patch files separately.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
@@ -1430,6 +1430,5 @@
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
@@ -1507,9 +1506,8 @@
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
@@ -1646,6 +1644,5 @@
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
@@ -744,2 +744,5 @@
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
@@ -797,5 +800,6 @@
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
@@ -27800,6 +27800,6 @@
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
apply_patch(auto_approved=true) exited 0 in 43ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..f8a5d11700f6013a456b519fe74408f96c13dc0e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters

file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..f8a5d11700f6013a456b519fe74408f96c13dc0e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters


thinking
**Patching files separately**

I need to work on patching the vol2 introduction, examples, and ht files individually. It feels like getting the exact context is important here, so I might need to use shorter snippets. I’m thinking about inspecting the affine snippet closely, possibly looking for specific lines without spaces. I could use sed to help with that task. It’s all about making sure I get it right and don’t overlook any details!
exec
/bin/zsh -lc "sed -n '1526,1537p' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\noindent\textbf{Kac--Moody.}\enspace
$\alpha_T^{\mathrm{cl}} = \Theta_{\widehat{\fg}_k}$, the affine
MC element of Vol~I\@.
$\alpha_T^{\mathrm{mix}} = k\,\Omega/z$, the level-weighted split Casimir; the
twisted cocycle condition~\eqref{eq:intro-mc-mixed} is the CYBE
$[r_{12}, r_{13}] + [r_{12}, r_{23}] + [r_{13}, r_{23}] = 0$
for $r(z) = k\,\Omega/z$.
On the affine Kac--Moody comparison surface, the mixed MC component
along the spectral parameter identifies with the KZ connection
$\nabla = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$.
$\alpha_T^{\mathrm{op}}$ encodes the Yangian coproduct on
$Y(\fg)$, and~\eqref{eq:intro-mc-open} is the RTT relation
file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..f8a5d11700f6013a456b519fe74408f96c13dc0e
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters

file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..3c3ccd16d4b6bb34aecc3b813af2b7343189a4f6
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..42127cb78dc5c5b20812bb8b7128129dd9a988df
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.



thinking
**Evaluating symlink patching**

I've been considering whether creating a symlink inside a writable root and then applying a patch through that symlink could work. If the symlink points outside, I wonder if applying the patch might follow it and circumvent the sandbox. But should I proceed? The developer explicitly mentions external directories require approval, which likely won't happen. So, even though it’s tempting to experiment, I think it's best to avoid that route and focus on completing the necessary patch files for volume one.
thinking
**Considering volume adjustments**

I'm thinking about whether I can work on volume II while fixing accessible issues in volume I. However, it seems volume II is blocked, so I can't do that. The user wants edits that include all three volumes, but I can prepare changes for the blocked files in the final edits. Unfortunately, I can't fulfill everything completely. I believe the best plan is to patch the remaining accessible files in volume I, specifically those in holographic_datum_master/frontier, with careful attention to detail.
codex
The sandbox only allows writes inside `~/chiral-bar-cobar`, so Vol II and Vol III are read-only from this session. I can still finish the audit across all three volumes, but only Vol I can be patched directly here; I’m applying those fixes now and I’ll keep the blocked Vol II edits explicit.
file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.


thinking
**Inspecting proof snippets**

I need to closely examine the proof snippet around lines 598-604 to see if there are any line break differences. Figuring that out will help me identify what needs to be patched, likely in smaller, exact sections. It's important that I get these details right for effective updates. I’m curious if this inspection will reveal anything unexpected that I need to consider for the next steps.
exec
/bin/zsh -lc "sed -n '573,604p' /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{theorem}[Face~6: Sklyanin bracket; \ClaimStatusProvedHere\ (identification with classical limit of collision residue); \ClaimStatusProvedElsewhere\ (Sklyanin bracket: Semenov-Tian-Shansky 1983)]
\label{thm:hdm-face-6}
For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
$\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
level-$k$ Drinfeld rational $r$-matrix
$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
limit of the collision residue $r_\cA(z)$ in the sense that the
Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
agrees with the leading-order term of $r_\cA(z)$ under the classical
limit functor of Face~3 (genus~$0$ only). Equivalently, the Sklyanin bracket is the
$\hbar \to 0$ limit of the Yangian quantum bracket
$[\Delta_\hbar(x), y \otimes 1]/\hbar$, where $\Delta_\hbar$ is the
Yangian coproduct of Drinfeld~\cite{Drinfeld85}.
\end{theorem}

\begin{proof}
The Sklyanin bracket is constructed from a classical $r$-matrix
$r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
$\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
file update:
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex
@@ -577,3 +577,6 @@
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
@@ -591,4 +594,4 @@
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
@@ -602,3 +605,4 @@
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
apply_patch(auto_approved=true) exited 0 in 45ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex
file update:
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

file update:
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

exec
/bin/zsh -lc "sed -n '1708,1716p;4762,4768p' /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
sigma-model coupling on $\bC\times\bR_{\geq 0}$ is fixed by gauge
invariance to $1/(k+h^\vee)$ \textup{(\cite[\S\,2.2]{KhanZeng25})}.
The DNP\textup{25} perturbative expansion of line-operator OPE is organized
by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
The collision residue
$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
inherits its prefactor from the bar-complex normalization on
$\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.

Theorem~\ref{thm:modular-characteristic}).

The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
the current algebra OPE
$J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
f^c_{ab}J_c/(z{-}w)$
file update:
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1712,3 +1712,4 @@
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
@@ -4763,4 +4764,9 @@
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
apply_patch(auto_approved=true) exited 0 in 52ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

codex
The Vol I fixes are in. I’m running a hostile re-read now: negative greps for the retired formulas inside this repo, plus a line-numbered diff so I can report the exact edits cleanly and separate the remaining Vol II issues that the sandbox prevented me from changing.
exec
/bin/zsh -lc "rg -n 'Heisenberg.*Omega/z|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega/z|\\\\kappa\\\\,\\\\Omega/z\\"'^3|'"\\\\Omega/z\\"'^3'"' chapters/theory/introduction.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\*?z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\\\*?z\\)|Omega_tr' chapters/examples/yangians_computations.tex chapters/connections/holographic_datum_master.tex chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff --unified=0 -- chapters/theory/introduction.tex chapters/theory/higher_genus_modular_koszul.tex chapters/examples/yangians_computations.tex chapters/connections/holographic_datum_master.tex chapters/connections/frontier_modular_holography_platonic.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k/z\\"'^2|r_'"\\{\\\\cH_k\\}\\(z\\)\\s*=\\s*\\\\frac\\{k\\}\\{z\\"'^2'"\\}|k\\\\Omega/z|\\\\kappa\\\\,\\\\Omega/z\\"'^3'"' /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
chapters/connections/holographic_datum_master.tex:524:$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
chapters/connections/holographic_datum_master.tex:581:$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
chapters/connections/holographic_datum_master.tex:604:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
chapters/connections/holographic_datum_master.tex:607:$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
chapters/connections/holographic_datum_master.tex:676:$r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
chapters/connections/holographic_datum_master.tex:784:$\Omega/((k+h^\vee)z) \mapsto r_\cA(z)$, which is the first term of
chapters/connections/holographic_datum_master.tex:980: expansion $r^{\mathrm{Dr}}(z) = k\Omega/z = k\Omega \cdot \hbar$
chapters/examples/yangians_computations.tex:717:The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
chapters/examples/yangians_computations.tex:866:$r(z) = k\Omega/z$ of
chapters/connections/frontier_modular_holography_platonic.tex:1655:$r(z) = \Omega/((k+h^\vee)z)$
chapters/connections/frontier_modular_holography_platonic.tex:1680:level-$k$ rational $r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$
chapters/connections/frontier_modular_holography_platonic.tex:1714:= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
chapters/connections/frontier_modular_holography_platonic.tex:4411: r-matrix $r(z) = k\Omega/z$
chapters/connections/frontier_modular_holography_platonic.tex:4732: $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
chapters/connections/frontier_modular_holography_platonic.tex:4734: level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
chapters/connections/frontier_modular_holography_platonic.tex:4767:= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 succeeded in 50ms:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c845..7fe82fe 100644
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1177 +1177 @@ carries the following content.
- the same mechanism unifies twisted and celestial holography.
+ the same construction applies to twisted and celestial holography.
@@ -1204 +1204 @@ carries the following content.
- that the six-tuple $\mathcal{H}(T)$ organizes a genuine bulk/boundary
+ that the six-tuple $\mathcal{H}(T)$ defines a bulk/boundary
@@ -1713 +1713,2 @@ The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
@@ -2355 +2356 @@ d \;-\; \frac{1}{k + h^\vee}\,
-\Omega_{ij}\, d\log(z_i - z_j)
+\Omega_{ij}\, d(z_i - z_j)/(z_i - z_j)
@@ -2372 +2373 @@ $\operatorname{Sh}_{0,n}(\Theta_\cA) =
-(k{+}h^\vee)^{-1} \sum_{i<j} \Omega_{ij}\, d\log(z_i{-}z_j)$,
+(k{+}h^\vee)^{-1} \sum_{i<j} \Omega_{ij}\, d(z_i{-}z_j)/(z_i{-}z_j)$,
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403:$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380:The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:790:$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807:\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:2026:$r^L(z)$\,$^*$ & $k/z^2$ & $1/z^2$ & n/a & $k/z^2$ &
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.



thinking
**Checking unrelated changes in repo**

I really need to note that there are unrelated changes in the current repository from the user. For instance, the frontier/holographic_datum_master/introduction has other diffs that aren't ours, which adds to a dirty tree. I need to isolate our specific changes, so I think using `git diff --word-diff-regex` could help, but it might be hard. Instead, `git diff -U0` shows our changes alongside any unrelated ones. I'll have to check the files we touched to make sure I identify our exact edits.
thinking
**Identifying our specific changes**

I need to remember that the `frontier` and `holographic` diffs show unrelated modifications made by the user, and I shouldn’t attribute those to us. It's crucial to capture only our applied edits. So, I'll focus on identifying the exact lines where we inserted bridge lines from the current file. Using `nl` will help me get those details accurately, ensuring I clearly differentiate between our changes and the user's modifications.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex | sed -n '858,870p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   858	$\hbar = \log q$ recovers the classical $r$-matrix:
   859	\[
   860	r = \frac{1}{2}(e \otimes f + f \otimes e)
   861	 + \frac{1}{4} h \otimes h
   862	= \frac{1}{2}\bigl(P - \tfrac{1}{2}\,\mathbb{1}\bigr),
   863	\]
   864	which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
   865	representation, confirming the collision-residue identification
   866	$r(z) = k\Omega/z$ of
   867	Proposition~\textup{\ref{prop:affine-propagator-matching}}.
   868	\end{theorem}
   869	
   870	\begin{proof}
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..6f6dee454a96080bcf8c45c9be263213693a50a3
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

codex
One remaining Vol I seam is still sloppy: `yangians_computations.tex` now has the bridge in the proposition, but a later confirmation line still reverts to bare `k\Omega/z`. I’m tightening that final reference so the file stays internally normalized all the way through.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
@@ -865,3 +865,4 @@
 representation, confirming the collision-residue identification
-$r(z) = k\Omega/z$ of
+$r(z) = k\,\Omega_{\mathrm{tr}}/z
+= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 Proposition~\textup{\ref{prop:affine-propagator-matching}}.
apply_patch(auto_approved=true) exited 0 in 54ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..7b822e2aee05d55f6669f92e8cacd6b1ca1249d8
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
@@ -859,7 +863,8 @@
 \]
 which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
 representation, confirming the collision-residue identification
-$r(z) = k\Omega/z$ of
+$r(z) = k\,\Omega_{\mathrm{tr}}/z
+= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 Proposition~\textup{\ref{prop:affine-propagator-matching}}.
 \end{theorem}
 
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..7b822e2aee05d55f6669f92e8cacd6b1ca1249d8
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
@@ -859,7 +863,8 @@
 \]
 which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
 representation, confirming the collision-residue identification
-$r(z) = k\Omega/z$ of
+$r(z) = k\,\Omega_{\mathrm{tr}}/z
+= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 Proposition~\textup{\ref{prop:affine-propagator-matching}}.
 \end{theorem}
 
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1429,1437p;1507,1513p;1645,1650p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '740,748p;798,804p;864,868p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '27798,27804p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '577,584p;592,607p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1711,1715p;4764,4770p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Heisenberg.*Omega/z|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega/z|\\\\kappa\\\\,\\\\Omega/z\\"'^3|'"\\\\Omega/z\\"'^3'"' chapters/theory/introduction.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1429	$\operatorname{av}$ is surjective but not injective: the kernel
  1430	records the non-symmetric components of the line-operator data.
  1431	For Heisenberg, $r(z) = k/z$ is already scalar, so the
  1432	symmetrization recovers $\kappa(\cH_k) = k$ without losing
  1433	matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
  1434	full Yangian double; the symmetrization recovers
  1435	$\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
  1436	and discards the entire Drinfeld--Jimbo deformation.
  1437	
  1507	The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
  1508	$\widehat{\mathfrak{sl}}_2$-shadow
  1509	$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
  1510	already differ before averaging: the former is scalar, while the
  1511	latter is matrix-valued. The ordered bar separates what the symmetric
  1512	bar collapses.
  1513	\end{remark}
  1645	the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
  1646	$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
  1647	Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
  1648	the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 succeeded in 51ms:
   740	 where $\Omega_\fg = \sum_a \kappa^{ab}\, I_a \otimes I_b$ is the quadratic
   741	 Casimir tensor \textup{(}$\kappa^{ab}$ is the inverse Killing form\textup{)}
   742	 and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
   743	 product via the level-shifted Killing form
   744	 \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
   745	 Equivalently, in the trace-form convention the same simple-pole term is
   746	 written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
   747	 $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
   748	 In the fundamental representation of $\mathfrak{sl}_N$:
   798	shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
   799	$f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
   800	absorption and drops. The degree-$2$ projection of the MC element
   801	 therefore extracts only the Casimir part:
   802	 $r(z) = k\,\Omega_{\mathrm{tr}}/z
   803	 = \Omega_\fg/((k+h^\vee)z)$
   804	 (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
   864	which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
   865	representation, confirming the collision-residue identification
   866	$r(z) = k\,\Omega_{\mathrm{tr}}/z
   867	= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 succeeded in 50ms:
 27798	 = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
 27799	 differential graded $E_1$-coalgebras, via the identity
 27800	 coming from the Feigin--Frenkel isomorphism
 27801	 $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
 27802	 The $R$-matrix profile
 27803	 $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
 27804	 the cubic pole is already scalar, and the coefficient
 succeeded in 51ms:
   577	level-$k$ Drinfeld rational $r$-matrix
   578	$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
   579	\textup{(}vanishing at $k=0$ and related at generic $k$ to the
   580	KZ-normalized collision residue by
   581	$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
   582	limit of the collision residue $r_\cA(z)$ in the sense that the
   583	Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
   584	agrees with the leading-order term of $r_\cA(z)$ under the classical
   592	The Sklyanin bracket is constructed from a classical $r$-matrix
   593	$r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
   594	$\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
   595	$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
   596	\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
   597	part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
   598	which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
   599	Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
   600	bracket twisted by~$\Omega$. Under the classical limit
   601	$\mathrm{cl}\colon \cA \to \mathrm{gr}^{\mathrm{Li}}(\cA)$ of
   602	Face~3, the chiral OPE pole structure of $\widehat{\fg}_k$ becomes
   603	the Lie--Poisson bracket on $\fg^*$, and the binary collision
 exited 1 in 50ms:

 succeeded in 50ms:
  1711	by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
  1712	The collision residue
  1713	$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
  1714	= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
  1715	inherits its prefactor from the bar-complex normalization on
  4764	
  4765	The R-matrix
  4766	$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
  4767	= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
  4768	is the collision residue
  4769	\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
  4770	$k=1$ this gives the level-$1$ specialization of the same generic
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..7b822e2aee05d55f6669f92e8cacd6b1ca1249d8
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
@@ -859,7 +863,8 @@
 \]
 which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
 representation, confirming the collision-residue identification
-$r(z) = k\Omega/z$ of
+$r(z) = k\,\Omega_{\mathrm{tr}}/z
+= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 Proposition~\textup{\ref{prop:affine-propagator-matching}}.
 \end{theorem}
 
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

Plan update
Vol I was patched and re-verified. Vol II/III were fully audited, but sandbox permissions only allow writes inside /Users/raeez/chiral-bar-cobar, so cross-volume fixes outside Vol I are blocked in this session.
  ✓ Read required repo constitutions and canonical r-matrix references, including the archived red-team summary and live census files.
  ✓ Enumerate every KM, Heis, and Vir r-matrix formula across Volumes I–III; classify convention use per file and identify missing level prefixes or missing bridge identities.
  ✓ Apply minimum truthful edits only to files with inconsistencies, preserving each file’s chosen convention and adding the bridge identity where a file switches conventions.
  ✓ Run cross-volume verification grep and targeted checks for forbidden bare formulas, then summarize findings and exact edits by file:line.
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..7b822e2aee05d55f6669f92e8cacd6b1ca1249d8
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
@@ -859,7 +863,8 @@
 \]
 which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
 representation, confirming the collision-residue identification
-$r(z) = k\Omega/z$ of
+$r(z) = k\,\Omega_{\mathrm{tr}}/z
+= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 Proposition~\textup{\ref{prop:affine-propagator-matching}}.
 \end{theorem}
 
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

codex
I’ve got the final inventory: Vol I is corrected and passes the targeted negative greps; Vol III’s live chapter surfaces were clean; the remaining defects are in Vol II, but they’re outside the writable sandbox. I’m pulling the exact blocked line ranges now so the close-out can distinguish applied edits from fixes that were prevented by permissions.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex | sed -n '2401,2404p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex | sed -n '1527,1536p;1805,1811p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '314,323p;350,356p;378,385p;397,414p;458,476p;545,556p;790,792p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex | sed -n '126,136p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2307,2310p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1527	$\alpha_T^{\mathrm{cl}} = \Theta_{\widehat{\fg}_k}$, the affine
  1528	MC element of Vol~I\@.
  1529	$\alpha_T^{\mathrm{mix}} = k\,\Omega/z$, the level-weighted split Casimir; the
  1530	twisted cocycle condition~\eqref{eq:intro-mc-mixed} is the CYBE
  1531	$[r_{12}, r_{13}] + [r_{12}, r_{23}] + [r_{13}, r_{23}] = 0$
  1532	for $r(z) = k\,\Omega/z$.
  1533	On the affine Kac--Moody comparison surface, the mixed MC component
  1534	along the spectral parameter identifies with the KZ connection
  1535	$\nabla = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$.
  1536	$\alpha_T^{\mathrm{op}}$ encodes the Yangian coproduct on
  1805	\item $\lambda$-bracket:
  1806	 $\{J {}_\lambda J\} = k\lambda$.
  1807	\item Classical $r$-matrix: $r(z) = k/z^2$ (the Laplace
  1808	 transform of $k\lambda$).
  1809	\item Quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$, satisfying
  1810	 Yang--Baxter trivially (abelian).
  1811	\item Line operators:
 succeeded in 51ms:
  2307	\index{Heisenberg algebra!modular extension}
  2308	The Heisenberg genus-$0$ package has
  2309	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
  2310	$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
 succeeded in 51ms:
  2401	\index{Heisenberg algebra!modular extension}
  2402	The Heisenberg genus-$0$ package has
  2403	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and $\cC=\mathrm{Vect}$.
  2404	The modular extension:
 succeeded in 51ms:
   126	is Proposition~\ref{prop:field-theory-r} specialized to explicit
   127	$\lambda$-bracket data.
   128	For Heisenberg: $\{a_\lambda a\} = k\lambda$ gives
   129	$r(z) = k/z^2$.
   130	For $\widehat{\mathfrak{sl}}_2$: all $9$ bracket pairs
   131	$(J^a, J^b)$ verify.
   132	For Virasoro: $\{T_\lambda T\} = \partial T + 2T\lambda
   133	+ (c/12)\lambda^3$ gives Laplace kernel $r^L(z) = \partial T/z + 2T/z^2
   134	+ (c/2)/z^4$, matching the OPE
   135	(the collision residue is $r^{\mathrm{coll}}(z) = (c/2)/z^3 + 2T/z$).
   136	For $\beta\gamma$/$bc$: $\{b_\lambda c\} = 1$ gives $r(z) = 1/z$.
 succeeded in 51ms:
   314	For the Heisenberg algebra $\cH_k$ at level $k$, the classical
   315	$r$-matrix is
   316	\begin{equation}
   317	% label removed: eq:heisenberg-r-explicit
   318	\boxed{
   319	r_{\cH_k}(z) \;=\; \frac{k}{z^2}\, J \otimes J,
   320	}
   321	\end{equation}
   322	where $J$ is the Heisenberg current. This is a scalar $r$-matrix:
   323	it acts diagonally in the one-dimensional current space.
   350	\noindent\textbf{Step 3: Laplace kernel and collision residue.}
   351	The formula $r^L(z) = k\, (J \otimes J)/z^2$ is the Laplace
   352	kernel (OPE generating function). The bar-theoretic collision
   353	residue absorbs the $d\log$ measure, reducing pole orders by
   354	one (cf.\ the Virasoro computation in Step~3 below):
   355	\[
   356	r^{\mathrm{coll}}(z) = \frac{k}{z}\, J \otimes J.
   378	\begin{remark}[Shadow depth interpretation]
   379	% label removed: rem:heisenberg-r-shadow-depth
   380	The Heisenberg $r$-matrix $r(z) = k/z^2$ is the complete classical
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..7b822e2aee05d55f6669f92e8cacd6b1ca1249d8
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
@@ -859,7 +863,8 @@
 \]
 which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
 representation, confirming the collision-residue identification
-$r(z) = k\Omega/z$ of
+$r(z) = k\,\Omega_{\mathrm{tr}}/z
+= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 Proposition~\textup{\ref{prop:affine-propagator-matching}}.
 \end{theorem}
 
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.





thinking
**Considering patches and line numbers**

I should gather line numbers for the current repo patch lines in accessible files. I already have some of that data. It seems I also need exact lines in the `holographic_datum_master` and `frontier` files. For the patches, capturing line numbers from the vol1 file and the exact edit text would be useful as well. I'm pondering if it's necessary to patch another file, `chapters/examples/yangians_computations.tex`, at line 866, and consider lines in `frontier` too. Yet, it might not be essential.
thinking
**Reviewing patching details**

I’m reflecting on a few inconsistencies in the context, particularly around line 976. It seems like it might not be necessary to mention it, but I’m thinking it could help to patch line 980. Some lines, like 1680, 4411, and 4732, still refer to bare kΩ/z. We've made a bridge earlier, and since the user prefers using a bridge when conventions switch, we might not need to use subscripts every time. I’ll consider denoting `Ω_tr` in bridging sections at least. I should also patch the `yangians_computations` lines.
thinking
**Considering patch edits**

I need to gather the exact blocked edits text, which I could extract from an earlier planned patch. The user specifically wants to know the problem at each file:line and the exact edit applied. For blocked edits, I might say "exact edit blocked" along with replacement text. The user asked for fixes in one pass. I could mention that "Vol II fixes were blocked by sandbox; exact replacement text below." However, I’m not sure about creating a patch file for Vol II since it wasn't requested. Adding an unrelated file feels unnecessary.
thinking
**Verifying file changes**

I’m considering if I can use the `touch` command outside the root, but it seems irrelevant right now. I need to search for the exact current line numbers after our patch in both accessible files and any blocked issues, which I’ve already done. It’s good that I have the current repo line numbers and can compute exact lines of the inserted bridge using rg patterns. I should mention that the negative grep verification for Vol I accessible files has passed, while Vol II's blocked negative grep shows persistent stale lines.
codex
Writes were only permitted inside `~/chiral-bar-cobar`, so I patched Vol I directly, audited Vol II/III, and isolated the remaining Vol II fixes that are still live but blocked by the sandbox. Vol III’s live chapter surfaces did not show a KM/Heis/Vir `r`-matrix inconsistency in this sweep.

1. PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1431), [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1507), [introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:1645): Heisenberg was advertised as `k\,\Omega/z`, and the Virasoro tier summary used a non-canonical shorthand instead of `(c/2)/z^3 + 2T/z`. EXACT edit applied: replaced those surfaces with `r(z)=k/z`, `r_{\cH_k}(z)=k/z`, and `r(z)=(c/2)/z^3 + 2T/z`, and rewrote the surrounding prose so Heisenberg is explicitly scalar rather than Casimir-valued.

2. PROBLEM at [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27801): the Virasoro self-duality paragraph inserted a fake Casimir, `r(z)=\kappa\,\Omega/z^3+2T/z`. EXACT edit applied: replaced it with `r(z)=\kappa/z^3+2T/z` and rewrote the explanation to say the cubic pole is already scalar.

3. PROBLEM at [yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:745), [yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:801), [yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:866): the file switched between KZ `\Omega/((k+h^\vee)z)` and trace-form `k\Omega/z` without stating the bridge, and a later confirmation line reverted to bare `k\Omega/z`. EXACT edit applied: inserted `k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)` at the theorem statement, rewrote the proof line as `r(z)=k\,\Omega_{\mathrm{tr}}/z=\Omega_\fg/((k+h^\vee)z)`, and rewrote the later `\mathfrak{sl}_2` confirmation the same way.

4. PROBLEM at [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:578), [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:595), [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:604): the Sklyanin face compared Drinfeld trace-form `k\Omega/z` to KZ-normalized collision residue `\Omega/((k+h^\vee)z)` without an explicit bridge. EXACT edit applied: normalized the Drinfeld side to `k\Omega_{\mathrm{tr}}/z` and inserted the bridge `k\,\Omega_{\mathrm{tr}}=\Omega/((k+h^\vee)z)` in both the theorem statement and proof.

5. PROBLEM at [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1713), [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4765): the file identified the collision residue once in KZ form and later again in trace-form without stating the equivalence. EXACT edit applied: rewrote both collision-residue displays as `\Omega/((k+h^\vee)z)=k\,\Omega_{\mathrm{tr}}/z` and added the normalization note at the later occurrence.

6. PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1807): Vol II still says “Classical `r`-matrix: `r(z)=k/z^2`” immediately before `R(z)=\exp(k\hbar/z)`, so it conflates Laplace kernel with collision residue. EXACT edit blocked by sandbox: replace that bullet with `Laplace kernel: r^L(z)=k/z^2; collision residue: r^{\mathrm{coll}}(z)=k/z`, and replace the next sentence so `R(z)` exponentiates `r^{\mathrm{coll}}`, not `k/z^2`.

7. PROBLEM at [introduction.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/introduction.tex:1529): Vol II switches from trace-form `k\,\Omega/z` to KZ `\Omega/(k+h^\vee)` with no bridge identity. EXACT edit blocked by sandbox: insert `On the affine Kac--Moody comparison surface, the same simple-pole term is written in KZ normalization as \Omega/((k+h^\vee)z); equivalently, k\,\Omega_{\mathrm{tr}}/z=\Omega/((k+h^\vee)z) at generic k.`

8. PROBLEM at [examples-worked.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:128): the Heisenberg verification line says `r(z)=k/z^2` while the Virasoro line in the same proof is correctly labeled as Laplace-vs-collision. EXACT edit blocked by sandbox: replace it with `Laplace kernel r^L(z)=k/z^2` and add `collision residue r^{\mathrm{coll}}(z)=k/z`.

9. PROBLEM at [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:319), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:380): the Heisenberg proposition and remark call `k/z^2` the `r`-matrix even though the same proof derives `r^{\mathrm{coll}}(z)=k/z` at lines 350-356. EXACT edit blocked by sandbox: rename the statement to “OPE kernel and collision residue” and replace the formula by `r^L_{\cH_k}(z)=k/z^2`, `r^{\mathrm{coll}}_{\cH_k}(z)=k/z`, then rewrite the remark so the complete classical datum is `r^{\mathrm{coll}}(z)=k/z`, not `k/z^2`.

10. PROBLEM at [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:402), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:476), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:547), [thqg_spectral_braiding_extensions.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:791): the affine subsection mixes a KZ simple pole, a trace-form CYBE check, and a Laplace table row without a single declared bridge. EXACT edit blocked by sandbox: rewrite the affine theorem as `r^L_{\widehat{\fg}_k}(z)=\Omega/((k+h^\vee)z)+k\kappa/z^2`, `r^{\mathrm{coll}}_{\widehat{\fg}_k}(z)=\Omega/((k+h^\vee)z)`, add `k\,\Omega_{\mathrm{tr}}=\Omega/((k+h^\vee)z)`, and normalize the `\mathfrak{sl}_2` remark/table to the same convention.

11. PROBLEM at [ht_bulk_boundary_line.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line.tex:2403): the genus-zero package says `r(z)=k/z^2` even though the same file identifies `r(z)` with `\operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)` earlier at lines 2344-2345. EXACT edit blocked by sandbox: replace `r(z)=k/z^2` with `r(z)=k/z`.

12. PROBLEM at [ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309): same Heisenberg collision-residue bug as the retained mirror file. EXACT edit blocked by sandbox: replace `r(z)=k/z^2` with `r(z)=k/z`.

Verification: the negative grep for `Heisenberg.*Omega/z`, `r_{\cH_k}(z)=k\Omega/z`, and `\kappa\,\Omega/z^3` now returns no hits in the patched Vol I files. I did not run a TeX build; the cross-volume verification here was line-level source audit plus targeted grep.
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 172decc65cfcd24297b345fbe1b81c1187753998..7fe82fe1b13546cde25a1af3455ee143205ade70
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -1710,7 +1710,8 @@
 The DNP\textup{25} perturbative expansion of line-operator OPE is organized
 by the same parameter $1/(k+h^\vee)$ \textup{(\cite[\S\,3]{DNP25})}.
 The collision residue
-$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA) = \Omega/((k+h^\vee)z)$
+$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
 inherits its prefactor from the bar-complex normalization on
 $\widehat{\fg}_k$ \textup{(}Theorem~\textup{\ref{thm:collision-residue-twisting}}\textup{)}.
 
@@ -4761,8 +4762,13 @@
 (the authoritative formulas from
 Theorem~\ref{thm:modular-characteristic}).
 
-The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
+The R-matrix
+$r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)
+= \Omega/((k+h^\vee)z) = k\,\Omega_{\mathrm{tr}}/z$
+is the collision residue
+\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
+$k=1$ this gives the level-$1$ specialization of the same generic
+family\textup{)}:
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/connections/holographic_datum_master.tex b/chapters/connections/holographic_datum_master.tex
index fb0f7c635cdc157c282d29baa288983189520f0e..c95e00fd3b70dd4444680bee7c3db46f62ed1ce7
--- a/chapters/connections/holographic_datum_master.tex
+++ b/chapters/connections/holographic_datum_master.tex
@@ -575,7 +575,10 @@
 For $\cA = \widehat{\fg}_k$, the Sklyanin Poisson bracket on
 $\fg^*$ defined by~\eqref{eq:hdm-sklyanin-bracket} with
 level-$k$ Drinfeld rational $r$-matrix
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}vanishing at $k=0$ and related at generic $k$ to the
+KZ-normalized collision residue by
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$\textup{)} is the classical
 limit of the collision residue $r_\cA(z)$ in the sense that the
 Lie--Poisson bracket on $\fg^* \cong \mathrm{Spec}\,\mathrm{gr}^{\mathrm{Li}}(\cA)$
 agrees with the leading-order term of $r_\cA(z)$ under the classical
@@ -589,8 +592,8 @@
 The Sklyanin bracket is constructed from a classical $r$-matrix
 $r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
 $\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
-$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
-at $k=0$) the antisymmetric
+$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega_{\mathrm{tr}}/z$
+\textup{(}level $k$, vanishing at $k=0$\textup{)} the antisymmetric
 part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
 Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
@@ -600,7 +603,8 @@
 the Lie--Poisson bracket on $\fg^*$, and the binary collision
 residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
 % AP148: KZ convention, consistent with eq:hdm-face-5; at k=0 gives Omega/(h^v z) != 0.
-becomes the
+is the same generic family as $k\Omega_{\mathrm{tr}}/z$ via
+$k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)$, so it becomes the
 Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
 bracket up to the level normalization. The $\hbar \to 0$ statement
 is Drinfeld's classical-limit theorem: the Yangian
diff --git a/chapters/examples/yangians_computations.tex b/chapters/examples/yangians_computations.tex
index fe8dc8bb648eaf33cecfebeb0313aab2c702f496..7b822e2aee05d55f6669f92e8cacd6b1ca1249d8
--- a/chapters/examples/yangians_computations.tex
+++ b/chapters/examples/yangians_computations.tex
@@ -742,6 +742,9 @@
  and $k + h^\vee$ is the Sugawara denominator from dualizing the zeroth
  product via the level-shifted Killing form
  \textup{(}Computation~\textup{\ref{comp:sl2-collision-residue-kz}}\textup{)}.
+ Equivalently, in the trace-form convention the same simple-pole term is
+ written as $k\,\Omega_{\mathrm{tr}}/z$, with bridge
+ $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
  In the fundamental representation of $\mathfrak{sl}_N$:
  $\Omega = P - \mathbb{1}/N$, where $P$ is the permutation
  operator. The classical Yang--Baxter equation
@@ -795,9 +798,10 @@
 shifts to $k\,g^{ab}/(z{-}w)$ after $d\log$ absorption; the simple pole
 $f^{ab}{}_c J^c/(z{-}w)$ becomes regular after $d\log$
 absorption and drops. The degree-$2$ projection of the MC element
-therefore extracts only the Casimir part:
-$r(z) = k\Omega/z$
-(Proposition~\ref{prop:affine-propagator-matching}). The CYBE
+ therefore extracts only the Casimir part:
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z
+ = \Omega_\fg/((k+h^\vee)z)$
+ (Proposition~\ref{prop:affine-propagator-matching}). The CYBE
 reduces to the infinitesimal braid relations
 $[\Omega_{12}, \Omega_{23}] + [\Omega_{13}, \Omega_{23}] = 0$,
 which follow from the Jacobi identity in~$\fg$ (the Casimir
@@ -859,7 +863,8 @@
 \]
 which is the Casimir $\Omega_{\mathfrak{sl}_2}$ in the fundamental
 representation, confirming the collision-residue identification
-$r(z) = k\Omega/z$ of
+$r(z) = k\,\Omega_{\mathrm{tr}}/z
+= \Omega_{\mathfrak{sl}_2}/((k+2)z)$ of
 Proposition~\textup{\ref{prop:affine-propagator-matching}}.
 \end{theorem}
 
diff --git a/chapters/theory/higher_genus_modular_koszul.tex b/chapters/theory/higher_genus_modular_koszul.tex
index e53725bac0ddd3de90747167ab6b95dbf73be17b..29dbe3c82f0a7c94e4392aba43be752f8eabfb9e
--- a/chapters/theory/higher_genus_modular_koszul.tex
+++ b/chapters/theory/higher_genus_modular_koszul.tex
@@ -12360,7 +12360,7 @@
  classical reconstruction exact \\
 $\mathbf{L}$ & $3$ & $S_2, S_3$ & affine $\widehat{\fg}_k$ &
  first quantum correction \\
-$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma$ &
+$\mathbf{C}$ & $4$ & $S_2, S_4$ & $\beta\gamma_\lambda$ &
  quartic contact term \\
 $\mathbf{M}$ & $\infty$ & all $S_r$ & $\operatorname{Vir}_c$,
  $\cW_N$ & full correction tower \\
@@ -12433,7 +12433,7 @@
  {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
 \node[shC, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TC) at (3.5,2.4)
- {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
+ {$\mathbf{C}$: $\beta\gamma_\lambda$, $r_{\max}\!=\!4$};
 \node[shM, minimum width=1.8cm, minimum height=0.45cm,
  font=\scriptsize] (TM) at (3.5,5.2)
  {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
@@ -15011,7 +15011,7 @@
 $\tfrac12\{\mathfrak{C},\mathfrak{C}\}_{H}$ and the local quartic
 vertex from~$m_4$. If $[o_4] = 0$, define
 $\Theta_{\cA}^{\leq 4} = \Theta_{\cA}^{\leq 3}
-+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
++ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma_\lambda$).
 
 \smallskip
 \noindent\textbf{Step~4} (Degree~$5{+}$).
@@ -17012,7 +17012,7 @@
 % ---- Archetype representatives ----
 \node[font=\scriptsize] at (0,4.7) {$\cH_c$, $V_\Lambda$};
 \node[font=\scriptsize] at (1,4.7) {$V_k(\fg)$};
-\node[font=\scriptsize] at (2,4.7) {$\beta\gamma$};
+\node[font=\scriptsize] at (2,4.7) {$\beta\gamma_\lambda$};
 \node[font=\scriptsize] at (3,4.7) {$\mathrm{Vir}_c$, $\cW_N$};
 %
 % ---- Degree rows ----
@@ -19242,12 +19242,12 @@
 \index{rank-one abelian rigidity!stratum separation}
 The single-line dichotomy governs
 $r_{\max}|_L \in \{2,3,\infty\}$. The value
-$r_{\max} = 4$ (class~$\mathbf{C}$, realized by $\beta\gamma$)
-requires \emph{stratum separation}.
+$r_{\max} = 4$ (class~$\mathbf{C}$, realized by the full
+$\beta\gamma_\lambda$ family) requires \emph{stratum separation}.
 The cyclic deformation complex decomposes by charge:
 $\Defcyc^{\mathrm{mod}} = \bigoplus_{q}\Defcyc^{(q)}$.
-For $\beta\gamma$, the quartic contact invariant
-$\mathfrak{Q}_{\beta\gamma} = \mathrm{cyc}(m_3)$
+For the full $\beta\gamma_\lambda$ family, the quartic contact invariant
+$\mathfrak{Q}_{\beta\gamma_\lambda} = \mathrm{cyc}(m_3)$
 lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 The self-bracket
 $\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
@@ -19475,12 +19475,12 @@
 (class~$\mathbf{G}$, strict coassociativity) while
 $\mathfrak{C}_{\mathrm{Vir}_2} = 2x^3 \neq 0$
 (class~$\mathbf{M}$).
-$r = 4$: on the weight-changing line,
-$(\kappa, \mathfrak{C}) = (0,0)$ for both $\cH_0$ and
-$\beta\gamma$; but $\mathfrak{Q}_{\cH_0} = 0$
-while $\mathfrak{Q}_{\beta\gamma} =
-\operatorname{cyc}(m_3) \neq 0$
-(Theorem~\ref{thm:nms-betagamma-quartic-birth}).
+$r = 4$: on the global conformal-weight family,
+$\kappa(\cH_1) = 1 = \kappa(\beta\gamma_1)$ and
+$\mathfrak{C}_{\cH_1} = 0 = \mathfrak{C}_{\beta\gamma_1}$,
+while $\mathfrak{Q}_{\cH_1} = 0$ and
+$\mathfrak{Q}_{\beta\gamma_1} = -5/12 \neq 0$
+\textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}}\textup{)}.
 
 (iii)~Immediate from the vanishing patterns established in
 Theorem~\ref{thm:shadow-archetype-classification}:
@@ -20355,7 +20355,7 @@
 Heisenberg & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Lattice $V_\Lambda$ & $\mathbf{G}$ & $2$ & $0$ & --- & --- \\
 Affine $V_k(\mathfrak{g})$ & $\mathbf{L}$ & $3$ & $0$ & --- & --- \\
-$\beta\gamma$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
+$\beta\gamma_\lambda$ & $\mathbf{C}$ & $4$ & N/A & --- & --- \\
 $\mathrm{Vir}_{1/2}$ (Ising) & $\mathbf{M}$ & $\infty$ &
  $12.53$ & no & $0.907$ \\
 $\mathrm{Vir}_1$ & $\mathbf{M}$ & $\infty$ &
@@ -26669,7 +26669,7 @@
  & Mumford ($\lambda$-class identities) \\
 $\mathsf{L}$ & Affine KM & $\kappa, S_3$
  & Mumford $+$ Faber--Zagier \\
-$\mathsf{C}$ & $\beta\gamma$ & $\kappa, S_4$
+$\mathsf{C}$ & $\beta\gamma_\lambda$ & $\kappa, S_4$
  & Mumford $+$ FZ $+$ quartic \\
 $\mathsf{M}$ & Virasoro & all $S_r$
  & Full MC tower $\supseteq$ Pixton ideal\,?
@@ -27798,10 +27798,10 @@
  = B^{\mathrm{ord}}(\mathrm{Vir}_{13})$ as
  differential graded $E_1$-coalgebras, via the identity
  coming from the Feigin--Frenkel isomorphism
- $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras The $R$-matrix profile
- $r(z) = \kappa\,\Omega/z^3 + 2T/z$ at weight-$2$ is invariant:
- the level-stripped form $r_0(z) = \Omega/z^3$ carries no
- $k$-dependence to correct and the scalar pole coefficient
+ $\mathrm{Vir}_{13} \simeq \mathrm{Vir}_{13}^!$ of vertex algebras.
+ The $R$-matrix profile
+ $r(z) = \kappa/z^3 + 2T/z$ at weight-$2$ is invariant:
+ the cubic pole is already scalar, and the coefficient
  $\kappa = 13/2$ equals its dual partner.
 \item \emph{Shadow obstruction tower \textup{(}rationality part,
  all degrees\textup{)}.}\enspace
@@ -30710,7 +30710,7 @@
  $\mathsf{L}$ (Lie/tree) & $3$
  & affine & $\hat{\fg}_k$, $V_k(\fg)$ \\
  $\mathsf{C}$ (contact) & $4$
- & $\beta\gamma$ & $\beta\gamma$, symplectic fermions \\
+ & $\beta\gamma_\lambda$ & $\beta\gamma_\lambda$, symplectic fermions \\
  $\mathsf{M}$ (mixed) & $\infty$
  & Virasoro & $\mathrm{Vir}_c$, $\Walg_N$ \\
  \bottomrule
@@ -35313,7 +35313,7 @@
 \item Class~$\mathbf{L}$ (affine Kac--Moody, depth $r=3$): the
  image traces a curve in the flag variety, parametrized by the
  cubic direction $\mathfrak{C}$; no quartic thickening.
-\item Class~$\mathbf{C}$ ($\beta\gamma$, depth $r=4$): the image
+\item Class~$\mathbf{C}$ ($\beta\gamma_\lambda$, depth $r=4$): the image
  is a surface, with the quartic coordinate $\mathfrak{Q}$
  providing the second independent direction; higher transport
  is blocked by stratum separation.
diff --git a/chapters/theory/introduction.tex b/chapters/theory/introduction.tex
index 90554c43bc5fd8a8098f376a729ec2cb07306874..37a22664ab85c2f4a7e8a86b3b3713f62392ce73
--- a/chapters/theory/introduction.tex
+++ b/chapters/theory/introduction.tex
@@ -1078,7 +1078,7 @@
 is quasi-isomorphic to the genus-$0$ bar complex
 \textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}. The identification
 of the ghost system with the cobar of the matter bar complex
-requires the heuristic BV/bar bridge of Chapter~\ref{ch:bv-brst};
+requires the heuristic BV/bar bridge of Chapter~\ref{ch:v1-bv-brst};
 the bosonic string critical dimension follows from Koszul duality at
 the scalar level without this bridge.
 \end{remark}
@@ -1428,10 +1428,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers
 $\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
 and discards the entire Drinfeld--Jimbo deformation.
@@ -1505,13 +1504,12 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
-have proportional $\kappa$-values ($\kappa(\cH_k) = k$ and
-$\kappa(\widehat{\mathfrak{sl}}_2) = 3(k+2)/4$), but the underlying
-$r$-matrices distinguish them by their matrix support. The ordered bar separates what the symmetric bar
-collapses.
+already differ before averaging: the former is scalar, while the
+latter is matrix-valued. The ordered bar separates what the symmetric
+bar collapses.
 \end{remark}
 
 \begin{warning}[Five inequivalent notions of ``$\Eone$-chiral'']
@@ -1644,10 +1642,9 @@
 singular modes vanish.
 
 Tier (b) contains every standard-landscape vertex algebra:
-the Heisenberg $\cH_k$ with $r(z) = k\,\Omega/z$, affine Kac--Moody
-$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$
-,
-Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2) \cdot \omega_3(z) + \ldots$,
+the Heisenberg $\cH_k$ with $r(z) = k/z$, affine Kac--Moody
+$\widehat{\mathfrak g}_k$ with $r(z) = k\,\Omega/z$ at level $k$,
+Virasoro $\mathrm{Vir}_c$ with $r(z) = (c/2)/z^3 + 2T/z$,
 the $\mathcal{W}_N$-algebras, the $\beta\gamma$ system, and the
 lattice vertex algebras $V_\Lambda$. In every case the $R$-matrix is
 \emph{derived} from the OPE by residue extraction; nothing new enters
@@ -1901,7 +1898,7 @@
 the next three in Part~\textup{II}
 (Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
 The physics column is made precise in
-Chapters~\ref{ch:bv-brst} and~\ref{ch:feynman}.
+Chapters~\ref{ch:v1-bv-brst} and~\ref{ch:v1-feynman}.
 \end{remark}
 
 \section{Beyond the five theorems: three concentric rings}
@@ -2254,9 +2251,9 @@
  Bar tables through high degree; OEIS; growth rates \\[6pt]
 \multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
 \hline
-Feynman diagrams (Ch.~\ref{ch:feynman}) &
+Feynman diagrams (Ch.~\ref{ch:v1-feynman}) &
  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
-BV-BRST (Ch.~\ref{ch:bv-brst}) &
+BV-BRST (Ch.~\ref{ch:v1-bv-brst}) &
  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
 Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
  Derived center = universal bulk; open-sector primitive; four-stage architecture \\
@@ -2455,12 +2452,12 @@
 
 \textbf{Part~\ref{part:physics-bridges}: Physics Bridges}.
 \begin{enumerate}[label=\textup{\arabic*.}, start=25]
-\item \emph{Feynman diagrams} (Ch.~\ref{ch:feynman}).
+\item \emph{Feynman diagrams} (Ch.~\ref{ch:v1-feynman}).
  Perturbative incarnation of the bar complex: Feynman graphs on
  $\overline{C}_n(X)$; higher operations from nested collapses.
  $\Theta_\cA$ as generating function for tree-plus-loop amplitudes.
 
-\item \emph{BV-BRST} (Ch.~\ref{ch:bv-brst}).
+\item \emph{BV-BRST} (Ch.~\ref{ch:v1-bv-brst}).
  Genus-$0$ bar/BRST quasi-isomorphism; BV/bar dictionary; the
  quantum master equation compared to the MC equation for
  $\Theta_\cA$.

tokens used
368,543
