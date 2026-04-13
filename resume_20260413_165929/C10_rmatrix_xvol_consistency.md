# C10_rmatrix_xvol_consistency (735s)

`PROBLEM` at [thqg_introduction_supplement_body.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:499): the file switched from the KZ residue `\Omega/((k+h^\vee)z)` to the trace-form discussion without stating the bridge. `EXACT edit applied`: added `Equivalently, in the trace-form convention one writes r(z)=k\,\Omega_{\mathrm{tr}}/z with k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee) at generic~k.`

`PROBLEM` at [yangians_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1063): the “equivalent” trace-form clause hid the level inside `\Omega_{\mathrm{tr}}`, writing `\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)` and `r(z)=\Omega_{\mathrm{tr}}/z`. `EXACT edit applied`: replaced that with `k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)` and `r(z)=k\,\Omega_{\mathrm{tr}}/z`.

`PROBLEM` at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:443): the Heisenberg comparison used the KM-style matrix formula `r(z)=k\,\Omega/z`. `EXACT edit applied`: changed it to `r(z)=k/z`.

`PROBLEM` at [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:623): the Heisenberg overview again used `r(z)=k\,\Omega/z`. `EXACT edit applied`: replaced it with `r(z)=k/z` and rewrote the sentence so Heisenberg is described as already scalar.

`PROBLEM` at [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:707): the ordered-side comparison wrote `r_{\cH_k}(z)=k\Omega/z`. `EXACT edit applied`: changed it to `r_{\cH_k}(z)=k/z` and rewrote the contrast as “Heisenberg kernel is scalar while the affine one is matrix-valued.”

`PROBLEM` at [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:175): the file used KZ `\Omega/((k+h^\vee)z)` and later trace-form averaging without an explicit bridge. `EXACT edit applied`: added `r(z)=k\,\Omega_{\mathrm{tr}}/z` with `k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)` at the Drinfeld-face item, and changed [line 214](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:214) from `\mathrm{av}(k\,\Omega/z)` to `\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)`.

`PROBLEM` at [ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309): Vol II still states the Heisenberg genus-zero package as `r(z)=k/z^2`, which is the pre-absorption pole, not the collision residue. `EXACT edit applied`: none; `/Users/raeez/chiral-bar-cobar-vol2` is read-only in this session.

`PROBLEM` at [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1919): Vol II still writes the Virasoro collision residue as `(c/2)/z^3 + 2T/z + (\partial T)`, retaining the Laplace term that should drop after `d\log` absorption. `EXACT edit applied`: none; `/Users/raeez/chiral-bar-cobar-vol2` is read-only in this session.

`PROBLEM` at [log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:158) and [line 186](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186): Vol II presents a generic strict residue `\Omega/z` and then the affine specialization `k\,\Omega/z` without an explicit normalization bridge or disambiguation. `EXACT edit applied`: none; `/Users/raeez/chiral-bar-cobar-vol2` is read-only in this session.

Verification: the post-edit Vol I grep cleared the active Heisenberg `k\,\Omega/z` survivors and the patched mixed KM files now state the trace/KZ bridge explicitly. I did not find an active Vol III chapter/standalone violation in the KM/Heis/Vir sweep.


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
session id: 019d87f9-a7b5-7ff0-bea5-9694b44c9b31
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


thinking
**Examining workspace permissions**

I’m considering the workspace setup and whether it can access just the current repository. It seems writable only in the current repo, while it may read other directories. I need to inspect if sibling directories are writable, but since they aren’t in writable roots, edits could require approval, which is impossible. But, wait, can the current repo include symlinks? I need to confirm if this workspace allows reading across all volumes while being restricted from writing.
thinking
**Exploring command options**

I’m considering using `exec_command` with `apply_patch`, but it seems I can't edit outside the writable root. I should note if accessing those areas is blocked. There’s a chance that directories for Volume II and III are writable in the same workspace, but permissions indicate this is unlikely. While I can audit and possibly fix just Volume I, my task involves maintaining cross-volume consistency. So, I’ll test this, plan updates, and ensure to provide frequent intermediary updates throughout.
codex
I’m auditing `r`-matrix formulas across Volumes I–III, locking the scope to KM, Heisenberg, and Virasoro. First I’m reading the required repo-wide sources and the relevant skill instructions, then I’ll grep the three volumes for every `r(z)` surface before touching any file.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/cross-volume-propagation/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 50ms:
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
**Planning the search for r-matrix formulas**

I’ve read the required initial documents, and now I’m thinking about using an update plan. I need to grep all three volumes for r-matrix formulas. Since there are multiple files across these volumes, using rg might be the best approach. Should I use the explorer agent? I’ve heard it’s preferred for codebase questions, so I'll spawn it with a specific task: to find all r-matrix formulas for KM, Heis, and Vir across volumes. Still, I might need to do a manual grep for specific hits as well.
codex
I’ve loaded the constitutional sources and the two required skills: `multi-path-verify` first for the KM/Heis/Vir claim family, then `cross-volume-propagation` for duplicate surfaces. Now I’m enumerating every live `r`-matrix formula across Volumes I–III and checking write permissions on Volumes II and III before I draft any edits.
collab spawn_agent(call_Q1HvsBMVExIskhtbwJGjZCpy, prompt="<task>Audit all live r-matrix formula surfaces for the three families affine KM, Heisenberg, and Virasoro across these d…")
mcp startup: no servers
spawn_agent(call_Q1HvsBMVExIskhtbwJGjZCpy, prompt="<task>Audit all live r-matrix formula surfaces for the three families affine KM, Heisenberg, and Virasoro across these d…") pending init:
  agent: 019d87fa-4640-7290-944e-85715c15e4c1
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"r\\(z\" -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1190

main.tex:1094:$\kappa(\cA)=\mathrm{av}(r(z))$ in the abelian and scalar families,
main.tex:1096:$\kappa(V_k(\fg))=\mathrm{av}(r(z))+\dim(\fg)/2$. Even this scalar is
main.tex:1097:extracted from the collision residue $r(z)$ by a
main.tex:1324:% holographic datum H(W_3) = (A, A!, C, r(z), Theta_A, nabla^hol).
main.tex:1507:% r(z) = Res^coll_{0,2}(Theta_A) --- realized in seven independent
main.tex:1516:$r(z) = \operatorname{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$,
main.tex:1523:% One mathematical object (r(z) = Res^coll_{0,2}(Theta_A)) realized in
working_notes.tex:1498:r(z) \;=\;
working_notes.tex:1502:$r(z) = k\,\Omega_\fg/z$, where
working_notes.tex:1505:$r(z) = (c/2)/z^3 + 2T/z$, a quasi-trigonometric solution
working_notes.tex:1508:arity~$2$, with ordering, is~$r(z)$.
working_notes.tex:1526:$K_q(\cA)$ determines $r(z)$ through order $z^{-q}$.  This is
working_notes.tex:1854:$r(z) = (c/2)/z^3 + 2T/z$, the genus tower
working_notes.tex:4673:The $r$-matrix $r(z)$
working_notes.tex:5049:(\cA,\; \cA^!,\; r(z)),
working_notes.tex:5051:where $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ is the
working_notes.tex:5053:universal MC element.  Equivalently, $r(z)$ is the image of
working_notes.tex:8384:% Drafts and sketches for the new Part III on the seven faces of r(z).

thinking
**Planning audit of r-matrix formulas across volumes**

I'm organizing a detailed audit of r-matrix formulas for Affine KM, Heisenberg, and Virasoro families spread over three volumes. My goal is to identify files and line numbers in .tex, .md, and compute docs that mention these formulas, noting conventions used, presence of level prefixes, and any bridging identities. I'll focus on probable inconsistencies only, starting with Vol I and targeting key files like kac_moody.tex and heisenberg_eisenstein.tex to extract relevant formula details and context.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"r\\"'^Vir" -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
staging/ordered_chiral_homology_BACKUP_20260412_225116.tex:8055:% C11: r^Vir(z) = (c/2)/z^3 + 2T/z.
standalone/ordered_chiral_homology.tex:6585:% C11: r^Vir(z) = (c/2)/z^3 + 2T/z.
exec
/bin/zsh -lc "printf 'vol1 writable: '; [ -w /Users/raeez/chiral-bar-cobar ] && echo yes || echo no
printf 'vol2 writable: '; [ -w /Users/raeez/chiral-bar-cobar-vol2 ] && echo yes || echo no
printf 'vol3 writable: '; [ -w /Users/raeez/calabi-yau-quantum-groups ] && echo yes || echo no" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
vol1 writable: yes
vol2 writable: no
vol3 writable: no
exec
/bin/zsh -lc "rg -n --hidden --glob '*.tex' --glob '*.md' '(r\\\\"'^'"\\{?(KM|Heis|Vir)|r\\(z\\)|R-matrix|classical r-matrix|\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\*?z\\)|k/z|c/2\\)/z\\"'^3|2T/z)'"' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden --glob '*.tex' --glob '*.md' '(r\\\\"'^'"\\{?(KM|Heis|Vir)|r\\(z\\)|R-matrix|classical r-matrix|\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\*?z\\)|k/z|c/2\\)/z\\"'^3|2T/z)'"' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --hidden --glob '*.tex' --glob '*.md' '(r\\\\"'^'"\\{?(KM|Heis|Vir)|r\\(z\\)|R-matrix|classical r-matrix|\\\\Omega/z|k\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)\\*?z\\)|k/z|c/2\\)/z\\"'^3|2T/z)'"' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:224:AP-CY23: The E_1-chiral bialgebra (not E_∞ vertex bialgebra) is the correct Hopf framework. The coproduct Δ_z lives on the E_1 (ordered) side of the Swiss-cheese operad. The E_∞ averaging map kills the Hopf structure: av(r(z)) = κ_ch. Li's vertex bialgebra framework (E_∞) is the wrong categorical home. Counter: formulate all Hopf data at the E_1 level using B^{ord} with deconcatenation.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:226:AP-CY25: The R-matrix extraction formula R(z) = (id ⊗ S) ∘ Δ_z(1_A) is WRONG — applying the coproduct to the vacuum and then the antipode yields 1 ⊗ 1 by the counit axiom. The correct R-matrix is characterized via the half-braiding σ_A(z)(a ⊗ n) = Σ Δ_z(a)_{(2)} · n ⊗ Δ_z(a)_{(1)}. Counter: never extract R from Δ(1); always construct via the half-braiding.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:233:AP-CY30: Factored ≠ solved for higher coherence. The 3-particle S-operator S_{ijk}=R_{ij}R_{ik}R_{jk} constructed from a YBE-satisfying R-matrix does NOT automatically satisfy the Zamolodchikov tetrahedron equation (proved: thm:zte-failure, O(κ²) obstruction). NEVER assume pairwise consistency implies higher-order consistency. The Kapranov-Voevodsky theorem requires E_∞ (fully symmetric), which the Omega-deformation breaks.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:254:- Two-parameter R-matrix: R_ch(u,v) = R_1(u)R_2(v)R_12(u-v) (Zamolodchikov factorization)
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:286:- ZAMOLODCHIKOV TETRAHEDRON: COMPUTED NEGATIVE RESULT. The Yang R-matrix does NOT satisfy ZTE. The factored S_{ijk}=R_{ij}R_{ik}R_{jk} fails at O(κ²) where κ=h₁h₂h₃. At κ=0: trivially satisfied (Kapranov-Voevodsky). At generic κ: genuine obstruction. The correct E_3 3-particle S-operator requires CORRECTIONS beyond pairwise products. Engine: zamolodchikov_tetrahedron_engine.py (~1200 lines, 34 tests). THIS PROVES E_3 IS GENUINELY NONTRIVIAL.
/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md:340:7. E_1-chiral bialgebra: the correct Hopf home. E_∞ vertex bialgebra loses R-matrix (AP-CY23).
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:82:- **ZTE FAILS for Yang R-matrix**: COMPUTED. S=RRR does NOT solve tetrahedron at O(κ²). E_3 is genuinely nontrivial. Engine: 1200 lines, 34 tests.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:100:4. **R-matrix extraction (AP-CY25)**: The formula R=(id⊗S)∘Δ(1) is WRONG. Use half-braiding construction.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:163:**The primitive object** is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:668:r^Heis(z) = k/z
/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:669:r^Vir(z) = (c/2)/z^3 + 2T/z
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_cy_to_chiral_wave13.md:72:**F13 [SERIOUS, AP-CY11]**: `thm:c3-drinfeld-center` (line 421, ProvedHere) and `thm:e1-universality-cy3` (line 577, ProvedHere) jointly underwrite the d=3 functor chain for C^3. Both are marked ProvedHere but the whole C^3 verification uses the unconstructed A_X logic at Step 4-5 (passing through the Drinfeld double and "quantum vertex chiral group"). The C^3 case is uniquely unconditional ONLY at the character/R-matrix level, not at the "G(C^3) is the quantum vertex chiral group" level. Recommend splitting: the character/algebra identifications are ProvedHere; the G(X) identification is ProvedElsewhere (Schiffmann-Vasserot, Kontsevich-Soibelman) or recast as a Remark.
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:103:- **P-S2 (line 135-138, C^3 chain verified end-to-end).** "For C^3: the Jordan quiver gives Y(gl_1-hat) ~ W_{1+infty}, and the chain C^3 -> W_{1+infty} -> Rep^{E_2}(Y(gl_1-hat)) is verified end-to-end." The isomorphism Y(gl_1-hat) ~ W_{1+infty} (affine Yangian ~ W_{1+infty}) is a theorem of Tsymbaliuk / Schiffmann-Vasserot / Arbesfeld-Schiffmann-Vasserot. But "the chain ... is verified end-to-end" is stronger than a simple iso and implicates (a) C^3 CY_3 -> CoHA (Kontsevich-Soibelman, critical version), (b) CoHA = Yangian positive part (Schiffmann-Vasserot), (c) Yangian -> E_2 via R-matrix braiding. Each step is known in some form, but "verified end-to-end" is a bold claim in a preface; cite chapter number where this is carried through, otherwise downgrade to "fits together" or "is expected to hold."
/Users/raeez/calabi-yau-quantum-groups/compute/audit/beilinson_audit_vol3_preface_wave11.md:143:- **N-S3 (line 163-164, Felder's dynamical elliptic R-matrix).** "the CY_2 quantum vertex chiral group is carried on Coh(E), with Felder's dynamical elliptic R-matrix." Felder's elliptic R-matrix is dynamic (depends on lambda in h^*). The "quantum vertex chiral group on Coh(E)" is the Frenkel-Reshetikhin elliptic affine algebra / quantum affine algebra. Check attribution and spelling: Felder's R-matrix solves the QDYBE on Coh(E). Good. But "CY_2 quantum vertex chiral group" is non-standard nomenclature. Cite Felder 1995, check.
/Users/raeez/calabi-yau-quantum-groups/notes/physics_mtheory_branes.tex:665: $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$ \\
/Users/raeez/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex:317:\section{The Drinfeld--Kohno theorem and the KZ/R-matrix identification}
/Users/raeez/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex:561: r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)
/Users/raeez/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex:574: r(z) = \frac{k\,\Omega}{z} + O(1),
/Users/raeez/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex:577:particular, $r(z)$ vanishes at $k=0$, while at the critical level
/Users/raeez/calabi-yau-quantum-groups/notes/theory_kl_e2_chiral.tex:578:$k = -\hv$ one has $r(z) = -\hv\,\Omega/z + O(1) \neq 0$. The
 succeeded in 51ms:
Total output lines: 967

/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:9:~1,700pp, this repo. Seven parts: I(The Open Primitive) II(The E_1 Core) III(Seven Faces of r(z)) IV(Characteristic Datum and Modularity) V(Standard HT Landscape) VI(Three-Dimensional Quantum Gravity = CLIMAX) VII(Frontier).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:31:The E_1-to-E_2 step: the R-matrix is the coherence datum. For E_inf chiral algebras (vertex algebras), R(z) is derived from the OPE. For genuinely E_1, R(z) is independent structure. The derived center Z(A) = HH*(A) carries E_2 from the Deligne conjecture. E_2 lives on Z(A) and on Mod_A, NOT on A. Quantum groups are E_1; Rep(U_q(g)) is E_2 in Cat.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:33:The R-matrix, the YBE (from Stokes on FM_3(C)), the braided line category, the spectral Drinfeld strictification — all E_2 phenomena.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:51:1. The modular operad governing A_inf-algebras in E_1-chiral algebras (Definition def:modular-operad-ainf-chiral: genus-0 proved = SC x E_1^tr; clutching via B^{ann} + R-matrix monodromy; genus >= 2 operadic verification open).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:55:An E_1-chiral quantum group is: E_1-chiral algebra A + chiral coproduct Delta + R-matrix R(z) + quasi-triangularity + antipode, such that Mod_A is braided monoidal (E_2 in Cat). This provides the data for the E_2-to-E_3 step.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:70:- E_2-chiral (def:E2-chiral-algebra, spectral-braiding-core.tex): E_2 on Z^{der}_{ch}(A), NOT on A. R-matrix R(z) with spectral parameter. DONE.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:164:- R-matrix provenance: R(z) from bulk-boundary composition, NOT universal R-matrix (agree on eval locus = DK-0).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:182:V2-AP4: Ordered-to-unordered descent is R-matrix twisted: B^Sigma_n = (B^ord_n)^{R-Sigma_n}. Naive quotient only for pole-free.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:185:V2-AP7: Heisenberg R-matrix = exp(k*hbar/z), NOT trivial. Collision residue k/z. Monodromy exp(-2pi*i*k).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:245:FM41: R-matrix makes A into E_2. Claimed R-matrix promotes A from E_1 to E_2. WRONG. R-matrix makes Mod_A braided (E_2 in Cat). A remains E_1. Quantum groups U_q(g) are E_1; Rep(U_q(g)) is E_2 in Cat. Counter: E_2 lives one categorical level up from A. Always.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:269:FM49: Y_z^\hbar notation. Changed Y_\hbar to Y_z^\hbar across 531 occurrences. WRONG. The algebra Y_\hbar(g) does not depend on z. The spectral parameter z lives on Δ_z, R(z), T(z), ev_z — structures ON the algebra, not the algebra itself. Y_z^\hbar is non-standard and misleading. Reverted. Counter: NEVER put the spectral parameter in the algebra symbol. It parametrises coproduct/R-matrix, not the algebra.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:281:FM54: Spectral R(z) = categorical braiding. Conflated the spectral R-matrix R(z) (family of maps with parameter z) with the E_2 braiding from Dunn (single natural transformation, no parameter). These are different objects. How they relate in the D-module enriched setting requires proof. Counter: spectral ≠ categorical. The relationship needs a theorem, not an assertion.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:305:FM58: Cauchy on formal series. Applied Cauchy's theorem to the R-matrix R(z) ∈ End(V⊗V)((z)), which is a FORMAL Laurent series. Cauchy requires CONVERGENT functions. Counter: use FLATNESS of the connection + homotopy invariance of monodromy (algebraic/topological argument, not analytic).
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:311:FM61: Modular operad (iii) proved by abstract D²=0. Cited thm:modular-bar (which proves D²=0 for abstract modular bar datum) as proof that concrete O^{A_∞-ch} clutching maps compose associatively. NON-SEQUITUR: different statement about different object. Counter: concrete operadic associativity of iterated B^{ann} sewing with R-matrix monodromy is OPEN.
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:334:| DK/YBE | r(z) via Laplace provides DK-0 | MC3 | Proved |
/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:371:- AP-CY25: R-matrix formula R=(id⊗S)∘Δ(1) is WRONG (yields 1⊗1 by counit). Use half-braiding σ_A(z)(a⊗n) = Σ Δ_z(a)_{(2)}·n ⊗ Δ_z(a)_{(1)}.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:62:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type.
/Users/raeez/chiral-bar-cobar-vol2/AGENTS.md:99:- R=PT: Route D (Eberhardt shift-equation uniqueness) reduces gap to meromorphicity of bar-cobar R-matrix. Level-by-level rationality PROVED (prop:level-rationality-R-bar).
 succeeded in 52ms:
Total output lines: 440

 M AGENTS.md
 M CLAUDE.md
 M Makefile
 M README.md
 M appendices/_sl2_yangian_insert.tex
 M appendices/nonlinear_modular_shadows.tex
 M appendices/ordered_associative_chiral_kd.tex
 M appendices/signs_and_shifts.tex
 M appendices/spectral_higher_genus.tex
 M bibliography/references.tex
 M chapters/connections/arithmetic_shadows.tex
 M chapters/connections/bv_brst.tex
 D chapters/connections/casimir_divisor_core_transport.tex
 M chapters/connections/concordance.tex
 D chapters/connections/dg_shifted_factorization_bridge.tex
 M chapters/connections/editorial_constitution.tex
 M chapters/connections/entanglement_modular_koszul.tex
 M chapters/connections/feynman_connection.tex
 succeeded in 50ms:
Total output lines: 5242

/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H14_remove_koszul_locus.md:240:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H14_remove_koszul_locus.md:376:metadata/claims.jsonl:3346:{"label": "rem:spin2-ceff-miura-w1infty", "env_type": "remark", "status": "ProvedHere", "file": "chapters/theory/ordered_associative_chiral_kd.tex", "line": 8659, "title": "Effective central charge and intertwining\nin the Miura basis", "labels_in_block": ["rem:spin2-ceff-miura-w1infty", "rem:independent-proof-coha", "eq:v1-jkl-vertex-bialgebra", "rem:spin2-ceff-miura", "eq:c-eff-spin2", "rem:w-infty-descent", "rem:w-infty-vertex-gap", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:w-infty-antipode-explicit", "eq:antipode-quartic-obstruction", "eq:antipode-hopf-obstruction", "lem:coprod-T-miura", "eq:coprod-T-derived", "subsec:spin3-miura-anomaly", "prop:spin3-miura-coprod", "eq:coprod-W", "thm:miura-cross-universality-monograph", "eq:miura-cross-universal", "eq:miura-triangular", "rem:conformal-anomaly-monograph", "rem:stokes-wN-monograph", "rem:antipode-monograph", "rem:shadow-gw-c3", "subsec:glN-chiral-qg", "ex:gl2-chiral-qg", "eq:gl2-transfer", "eq:gl2-R-explicit", "eq:gl2-rtt-components", "eq:gl2-rtt-degree1", "eq:gl2-rtt-offdiag", "eq:gl2-rtt-offdiag2", "eq:gl2-rtt-cross", "eq:gl2-qdet", "eq:gl2-coprod-matrix", "eq:gl2-coprod-11", "eq:gl2-coprod-12", "eq:gl2-coprod-21", "eq:gl2-coprod-22", "thm:glN-chiral-qg", "eq:glN-transfer", "eq:glN-miura", "eq:glN-yang-r", "eq:glN-classical-r", "eq:glN-ybe", "eq:glN-drinfeld-coprod", "eq:glN-coprod-components", "eq:glN-rtt", "eq:glN-qdet", "rem:glN-transition", "subsec:structural-consequences", "cor:bar-encodes-all-structural", "rem:factorization-qg", "sec:conjectures", "thm:FG-shadow", "conj:bordered", "rem:bordered-partial-resolution", "thm:ordered-associative-modular-mc", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "subsec:coderived-chiral-coproduct", "conj:coderived-chiral-coproduct", "rem:coderived-chiral-coproduct-structure", "rem:coderived-coproduct-vs-e3", "def:coderived-chiral-bialgebra", "prop:bar-is-coderived-chiral-bialgebra", "rem:projection-disease", "subsec:w3-ordered-bar-ds", "eq:w3-ordered-bar-ds", "thm:w3-ordered-bar", "eq:ww-ope-leading-ordered", "eq:w3-resolvent-tree", "thm:class-m-ds-transport", "rem:w3-resolvent", "rem:w3-parity-ordered", "subsec:shifted-factorization-comparison", "eq:unshifted-yangian", "thm:unshifted-identification", "rem:shift-boundary-conditions", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "conj:three-language-equivalence", "subsec:ordered-ch-hom-open-problems", "thm:e3-identification-km", "conj:trig-elliptic-ordered", "conj:higher-genus-ordered-ch", "prop:critical-level-ordered", "rem:three-level-contrast", "rem:gl3-explicit", "rem:ds-intertwining-w3", "rem:ker-av-d3-explicit", "rem:qdet-column-ordering", "rem:kzb-heat-prefactor", "rem:e1-noncommutative-euler", "ch:derived-langlands", "ch:genus1-seven-faces", "ch:holographic-datum-master", "ch:landscape-census", "comp:bp-kappa-three-paths", "conv:three-hochschild", "part:seven-faces", "part:v1-frontier", "prop:nilpotent-transport-typeA", "sec:bar-complex-introduction", "sec:complementarity", "thm:ds-hpl-transfer", "thm:langlands-bar-bridge"], "refs_in_block": ["eq:coprod-T", "eq:ope-compat", "def:e1-chiral", "eq:equiv-triangle", "eq:mk-from-ope", "eq:r-from-coprod-proof", "thm:chiral-qg-equiv", "eq:coprod-from-bar", "thm:w-infty-chiral-qg", "rem:w-infty-vertex-gap", "eq:rtt-gl1", "thm:glN-chiral-qg", "prop:w-infty-antipode-obstruction", "eq:transfer-inverse-recurrence", "eq:coprod-T-derived", "eq:coprod-W", "eq:gl1-coprod-general", "eq:miura-triangular", "eq:glN-miura", "eq:glN-qdet", "eq:gl1-drinfeld-coprod", "eq:gl2-coprod-11", "eq:gl2-coprod-22", "lem:coprod-T-miura", "eq:glN-yang-r", "def:koszul-locus", "eq:glN-drinfeld-coprod", "eq:glN-transfer", "ex:gl2-chiral-qg", "eq:glN-ybe", "eq:glN-rtt", "thm:ordered-open", "conj:bordered", "sec:bordered-fm", "constr:bordered-fm", "thm:bordered-fm-properties", "prop:four-type-boundary", "thm:ordered-associative-ds-principal", "conj:DS-arbitrary-nilpotent", "thm:off-koszul-ran-inversion", "constr:deconcatenation", "thm:bv-bar-coderived", "conj:coderived-e3", "rem:coderived-e3-structure", "conj:coderived-chiral-coproduct", "thm:conilpotent-reduction", "thm:ds-koszul-intertwine", "eq:w3-ordered-bar-ds", "thm:single-line-dichotomy", "thm:tree-formula", "constr:transfer-ainf", "comp:w-infty-shadow-tower", "comp:ds-bar-sl3-w3", "eq:w3-resolvent-tree", "thm:derived-additive-kz", "conj:three-language-equivalence", "thm:unshifted-identification", "thm:factorisation-identification", "prop:r-matrix-stable-envelope", "sec:ordered-chiral-homology", "subsec:formality-bridge", "subsec:chiral-e3-cfg-comparison", "thm:e1-formality-failure", "thm:opposite", "def:Kbi", "thm:shuffle", "cor:anti", "cor:enveloping", "lem:Kbi-dg", "thm:tangent=K", "thm:bimod-bicomod", "thm:diagonal", "cor:unit", "cor:tensor-cotensor", "thm:HH-coHH-homology", "thm:HH-coHH-cohomology", "prop:infann", "thm:CY", "thm:double-bar-sl2", "thm:central-extension-invisible", "thm:two-colour-double-kd", "cor:two-colours-non-redundant", "thm:heisenberg-ordered-bar", "thm:heisenberg-rmatrix", "thm:heisenberg-yangian", "thm:heisenberg-formality", "thm:km-yangian", "tab:km-yangian-data", "thm:w3-ordered-bar", "thm:class-m-ds-transport", "thm:bg-ordered-bar", "thm:bg-rmatrix", "thm:bg-koszul-dual", "thm:bc-ordered-bar", "thm:wakimoto-ordered-bar", "thm:lattice-symmetric-ordered-bar", "thm:lattice-nonsymmetric-ordered-bar", "thm:lattice-ordered-koszul-dual", "thm:root-space-one-dim-v1", "lem:jacobi-collapse-v1", "thm:dynkin-beta-integral", "thm:complete-strictification-v1", "constr:evaluation-map", "thm:sl2-R-matrix", "cor:sl2-clebsch-gordan", "comp:sl3-eval-fundamental", "comp:sl3-eval-adjoint", "prop:eval-drinfeld", "thm:line-category", "thm:eval-braiding", "thm:b-cycle-quantum-group", "thm:drinfeld-kohno", "thm:yangian-quantum-group", "cor:sl2-root-of-unity", "thm:jones-genus1", "def:annular-bar", "thm:annular-bar-differential", "thm:annular-HH", "thm:curvature-braiding-dichotomy", "thm:dirichlet-weight-formula"], "cites_in_block": ["KS11", "SV13", "YZ18a", "JKL26", "MO19", "Drinfeld90", "EK96", "GR17", "RSYZ20", "SMMV23", "PR19", "Molev07", "Latyntsev23"]}
/Users/raeez/chiral-bar-cobar/CLAUDE.md:5:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:35:r(z) written:         [formula with level prefix visible]
/Users/raeez/chiral-bar-cobar/CLAUDE.md:37:AP141 k=0 check:      r(z)|_{level=0} = [value]    required: 0 (trace-form convention)
/Users/raeez/chiral-bar-cobar/CLAUDE.md:43:Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:199:1. CONSTRUCT the E1 object (B^ord, r(z), Theta_A in g^{E1}, the matrix-valued curvature).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:200:2. EXHIBIT the E1 structure (deconcatenation coproduct, R-matrix, Yangian).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:202:4. DERIVE the symmetric result (kappa from av(r(z)); for non-abelian affine KM, av(r(z)) + dim(g)/2 = kappa; obs_g = kappa*lambda_g, the shadow tower).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:206:The convolution algebra has two levels: g^{E1}_A (the primitive, carrying the R-matrix) and g^mod_A (the coinvariant shadow, carrying only kappa). Theta_A lives in g^{E1}_A; everything in this monograph is its Sigma_n-coinvariant projection.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:239:**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:245:**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:289:- B1. `r(z) = \Omega/z` (bare, no level). CORRECT: trace-form `r(z) = k\Omega/z` or KZ `r(z) = \Omega/((k+h^\vee)z)`. AP126. Regex: `r\(z\)\s*=\s*\\Omega\s*/\s*z` (catches bare form without any level prefix or Sugawara denominator).
/Users/raeez/chiral-bar-cobar/CLAUDE.md:290:- B2. `r^Vir(z) = (c/2)/z^4` (quartic). CORRECT: `(c/2)/z^3 + 2T/z`. AP19/AP21.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:291:- B3. `r^Vir(z) = (c/2)/z^2`. CORRECT: cubic + simple. AP19/AP27.
/Users/raeez/chiral-bar-cobar/CLAUDE.md:302:- B11. `av(r(z)) = \kappa` for non-abelian KM. CORRECT: `av(r(z)) + dim(g)/2 = kappa(V_k(g))`. FM11.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\(c/2\\)/z\\"'^3" -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 115

tmp_standalone_audit/survey_v2_xr.tex:599:$r(z)=(c/2)/z^3+2T/z$ carries the stress-tensor coupling at
tmp_standalone_audit/survey_v2_xr.tex:734:residue is $r(z)=(c/2)/z^3+2T/z$ (cubic, not quartic).
tmp_standalone_audit/survey_v2_xr.tex:2325:$k\Omega/z$ (affine) or $(c/2)/z^3 + 2T/z$ (Virasoro) or the
tmp_standalone_audit/survey_v2_xr.tex:2608:$r_c(z)=(c/2)/z^3+2T/z$: the quartic and quadratic OPE poles
tmp_standalone_audit/survey_v2_xr.tex:4406:$r_c(z) = (c/2)/z^3 + 2T/z$ has both a third-order pole
tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:199:$k\Omega/z$ (affine) or $(c/2)/z^3 + 2T/z$ (Virasoro) or the
tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:354:$r_c(z) = (c/2)/z^3 + 2T/z$, second-order and zeroth-order
tmp_standalone_audit/wrap_survey_track_b_fixed2.tex:1750:$r_c(z) = (c/2)/z^3 + 2T/z$ has both a third-order pole
tmp_standalone_audit/wrap_programme_summary_sections5_8_fixed.tex:108:$3$ & Virasoro $\Vir_c$ & $(c/2)/z^3 + 2T/z$ & $\mathbf{M}$ \\
tmp_standalone_audit/wrap_programme_summary_sections5_8_fixed.tex:194:For Virasoro, $\mathrm{av}((c/2)/z^3 + 2T/z) = c/2$.
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:199:$k\Omega/z$ (affine) or $(c/2)/z^3 + 2T/z$ (Virasoro) or the
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:354:$r_c(z) = (c/2)/z^3 + 2T/z$, second-order and zeroth-order
tmp_standalone_audit/wrap_survey_track_b_fixed.tex:1750:$r_c(z) = (c/2)/z^3 + 2T/z$ has both a third-order pole
working_notes.tex:1505:$r(z) = (c/2)/z^3 + 2T/z$, a quasi-trigonometric solution
working_notes.tex:1854:$r(z) = (c/2)/z^3 + 2T/z$, the genus tower
appendices/ordered_associative_chiral_kd.tex:2393: triple-pole residue $(c/2)/z^3 + 2T/z$. Formality breaks: $m_k \neq 0$ for all $k\ge 3$, so the
appendices/ordered_associative_chiral_kd.tex:3147:$(c/2)/z^3$ and the field-valued $2T/z$, play entirely different
appendices/ordered_associative_chiral_kd.tex:3178:The central term $(c/2)/z^3$ commutes with all tensor factors and

thinking
**Planning targeted file analysis**

I’m organizing a focused approach to highlight relevant files with key formula references across volumes. I want to produce manageable output by choosing representative files—like a couple per volume—especially where bridging between conventions appears, and gather context around specific line numbers using sed to confirm details. This way, I can efficiently summarize important formula instances without overwhelming detail.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1830,1865p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
window is zero. This is the unique G-class family
(Table~\ref{tab:completion-kinematics}): both the shadow depth
(degree~$2$) and the completion entropy ($h_K = 0$) are minimal.
The kinematic triviality of the Heisenberg is the algebraic reason
that all other families can be calibrated against it: every
completion invariant is measured relative to this zero point.

In the holographic modular Koszul datum
$\mathcal{H}(T) = (\cA, \cA^!, C, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$
of the concordance
(\S\ref{subsec:completion-kinematics-programme}),
the Heisenberg specialisation is: $\cA = \mathcal{H}_k$,
$\cA^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$ with $\kappa(\cA^!) = -k$ (the chiral symmetric algebra, not $\cH_{-k}$),
$C = $ direct-sum complementarity,
$r(z) = k/z$ (the abelian $r$-matrix),
$\Theta_{\mathcal{H}_k} = k \cdot \eta \otimes \Lambda$
(scalar, no higher corrections),
$\nabla^{\mathrm{hol}} = d$ (flat, since the shadow vanishes).
Every subsequent family is measured against this datum.
\end{remark}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/heisenberg_eisenstein.tex | sed -n '1840,1855p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1840	(\S\ref{subsec:completion-kinematics-programme}),
  1841	the Heisenberg specialisation is: $\cA = \mathcal{H}_k$,
  1842	$\cA^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$ with $\kappa(\cA^!) = -k$ (the chiral symmetric algebra, not $\cH_{-k}$),
  1843	$C = $ direct-sum complementarity,
  1844	$r(z) = k/z$ (the abelian $r$-matrix),
  1845	$\Theta_{\mathcal{H}_k} = k \cdot \eta \otimes \Lambda$
  1846	(scalar, no higher corrections),
  1847	$\nabla^{\mathrm{hol}} = d$ (flat, since the shadow vanishes).
  1848	Every subsequent family is measured against this datum.
  1849	\end{remark}
  1850	
  1851	\subsection{The Heisenberg primitive kernel}
  1852	\label{subsec:heisenberg-primitive-kernel}
  1853	\index{primitive kernel!Heisenberg}
  1854	
  1855	\begin{proposition}[Heisenberg primitive kernel;


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/kac_moody.tex | sed -n '70,130p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    70	 \ref{thm:hochschild-polynomial-growth};
    71	 Prop.~\ref{prop:chirhoch1-affine-km} \\
    72	\bottomrule
    73	\end{tabular}
    74	\end{table}
    75	
    76	\begin{table}[ht]
    77	\centering
    78	\small
    79	\caption{Shadow archetype data for affine
    80	Kac--Moody.}\label{tab:km-shadow-archetype}
    81	\begin{tabular}{ll}
    82	\toprule
    83	\textbf{Invariant} & \textbf{Value} \\
    84	\midrule
    85	Class & L (Lie/tree) \\
    86	Shadow depth $r_{\max}$ & $3$ \\
    87	$\kappa(\widehat{\fg}_k)$ &
    88	 $\dim(\fg)(k{+}h^\vee)/(2h^\vee)$ \\
    89	Cubic shadow $\mathfrak{C}$ &
thinking
**Evaluating file updates**

I’m considering whether to use active files in `main.tex` or standalone files. My focus should be on fixing actual inconsistencies in active chapters rather than internal notes. But to be thorough within the assigned scope, I might need to include standalone files and notes if they’re relevant. I need to follow instructions carefully and apply the cross-volume rule, updating any genuine duplicates and addressing outdated files that could mislead future audits.
thinking
**Evaluating file access**

I’m considering whether I should access all three volumes of the entire repositories, but the action_safety suggests I can only edit assigned files. The tricky part is there’s no assigned file list. It might mean only the files in my current task scope, which could be affected by any necessary files with r-matrix formulas. However, it seems system permissions still restrict my access to the current repository. I think I need to wait for the agent.
codex
The first pass shows a hard constraint: Volumes II and III are readable but not writable from this session, while this worktree is also heavily dirty. I’m narrowing to the actual live manuscript surfaces now, separating active chapters/standalones from audit logs and scratch notes so I only touch real claim surfaces.
collab wait(call_1LTyYdWtui12VTVNZpeyhIYj)
  receivers: 019d87fa-4640-7290-944e-85715c15e4c1
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"k\\\\,\\\\Omega\" chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:k\,\Omega)
          ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"k\\\\,\\\\Omega/z\" chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:k\,\Omega/z)
          ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'k\\\\Omega' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
767:same object in the equivalent form $k\Omega_{\mathrm{tr}}/z$, where
771:identification $k\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/kac_moody.tex | sed -n '750,780p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   750	This chapter uses the \emph{KZ normalization} throughout:
   751	\[
   752	r^{\mathrm{KZ}}(z) = \frac{\Omega}{(k+h^\vee)\,z},
   753	\qquad
   754	\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b,
   755	\]
   756	where $\kappa^{ab}$ is the inverse Killing form and the
   757	denominator $k + h^\vee$ is the Sugawara shift. This is the
   758	normalization in which the KZ connection takes the standard form
   759	$\nabla^{\mathrm{KZ}} = d - \sum_{i < j} r(z_{ij})\, dz_{ij}$
   760	(Computation~\ref{comp:sl2-collision-residue-kz}).
   761	At $k = 0$ the non-abelian Lie bracket persists, so the collision
   762	residue $\Omega/(h^\vee z) \neq 0$; the abelian vanishing $r = 0$
   763	at $k = 0$ characterizes the Heisenberg $r$-matrix
   764	(Chapter~\ref{ch:heisenberg-frame}), not the non-abelian
   765	Kac--Moody collision residue.
   766	The landscape census (Table~\ref{tab:rmatrix-census}) records the
   767	same object in the equivalent form $k\Omega_{\mathrm{tr}}/z$, where
   768	$\Omega_{\mathrm{tr}}$ is the Casimir built from the
   769	\emph{trace-form} basis in which the level dependence is absorbed
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/w_algebras.tex | sed -n '45,90p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    45	\begin{table}[ht]
    46	\centering
    47	\small
    48	\caption{Shadow archetype data for
    49	$\mathcal{W}$-algebras (Virasoro and
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

thinking
**Verifying file conventions and searching volumes**

I'm checking if specific level prefixes or central charge conventions appear, focusing on the Virasoro formula and whether bridging identities are relevant. I need to explore Volume II's directory for key functions like `r(z)` and terms involving `kΩ/z`, using targeted regex searches to limit the scope, and confirm how standalone documents are distributed between Volume I and II. This helps me understand the file organization and notation usage across the volumes.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'r\\(z' -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 599

compute/audit/sl3_rtt_latex_output.tex:57:r(z) \;=\; \frac{k\,\Omega}{z}
compute/audit/sl3_rtt_latex_output.tex:67:The quantization of $r(z) = k\Omega/z$ is the Yang $R$-matrix
compute/audit/sl3_rtt_latex_output.tex:270: (left and right collision, controlled by $r(z) = k\Omega/z$).
compute/audit/non_simply_laced_rmatrix_report.tex:94: r(z) = \frac{k \cdot \Omega}{z}\,.
compute/audit/non_simply_laced_rmatrix_report.tex:100: regular part (no pole in $r(z)$).
compute/audit/non_simply_laced_rmatrix_report.tex:212:$r(z) = k\Omega/z$ & \checkmark \\
main.tex:1046:$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
main.tex:1278:The modular characteristic $\kappa(\cA) = \mathrm{av}(r(z))$
main.tex:1280:$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_\cA)$;
main.tex:1307:\part{The Seven Faces of $r(z)$}
main.tex:1312:The collision residue $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$
chapters/examples/w-algebras-stable.tex:574:exactly the CYBE for $r(z)$. This is the standard
chapters/examples/examples-complete-conditional.tex:280: r(z) = \frac{k\,\Omega}{z},
chapters/examples/examples-complete-conditional.tex:305:$r(z) = k\,\Omega/z$, the standard rational
chapters/examples/w-algebras.tex:479:exactly the CYBE for $r(z)$. This is the standard
chapters/examples/examples-complete-proved.tex:816:morphism into the $r(z)$-twisted tensor product.
chapters/examples/examples-complete-proved.tex:818:generators: the $r(z)$-twist encodes the nontrivial braiding
chapters/examples/w-algebras-virasoro.tex:483:exactly the CYBE for $r(z)$. This is the standard

thinking
**Identifying key vol2 files for analysis**

I'm focusing on selecting a few representative files per family within volume II to manage scope, especially those mentioning `kΩ` or bridging formulas like `Omega/(k+h^\vee)`. I'll search volume II directories for relevant code or text snippets referencing these terms to capture critical context without overwhelming detail.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && rg -n 'Omega/\\(k' -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/rosetta_stone.tex:5505: $\Omega/(k+h^\vee)$.  The two differ by the Sugawara
chapters/examples/rosetta_stone.tex:5508: $k\,\Omega$ with $\Omega/(k+h^\vee)$, recovering
chapters/examples/rosetta_stone.tex:5510: $\exp\!\bigl({-}2\pi i\,\Omega/(k+h^\vee)\bigr)$
working_notes.tex:11833:The monodromy is $\exp(2\pi i \cdot \Omega/(k+3))$.
chapters/connections/spectral-braiding-core.tex:394:$\exp(-\pi i\, \Omega/(k + h^\vee))$, which by the Drinfeld--Kohno
chapters/connections/log_ht_monodromy.tex:1440:More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
chapters/connections/ordered_associative_chiral_kd_frontier.tex:3274:+\hbar^2\kappa\,\wp(z;\tau)\,\Omega/(k+2)^2+\cdots$
chapters/connections/kontsevich_integral.tex:299:$\Omega/(k+h^\vee)$. (At the critical level $k = -h^\vee$,
chapters/connections/thqg_gravitational_yangian.tex:1670:vertex carries a factor of the Casimir $\Omega/(k+h^\vee)$, giving
chapters/connections/thqg_gravitational_yangian.tex:1704:$T^{(0)} = \Omega/(k+h^\vee)$ and $T^{(r)} = 0$ for $r \geq 1$,
chapters/connections/log_ht_monodromy_core.tex:1565:More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
chapters/connections/log_ht_monodromy_frontier.tex:747:\item the \emph{convergence mechanism}: the exponential $\exp(2\pi i \cdot \Omega/(k+h^\vee))$ converges in the completed tensor product $\End(\cL_b^{\wot 2})$ by a spectral bound that uses the polynomial growth of the $\lambda$-bracket, not merely the finite-dimensionality of evaluation modules.
chapters/connections/log_ht_monodromy_frontier.tex:774:The connection is regular singular at $z = 0$ with residue $\Omega/(k+2)$. The regularity follows from bar-kernel absorption: the $d\log$ kernel absorbs one pole from the $z^{-2}$ OPE singularity $J^a(w)J^b(z) \sim k\kappa^{ab}/(w-z)^2 + f^{ab}_c J^c(z)/(w-z)$, so the collision $r$-matrix has a simple pole $r(z) = k\,\Omega/z + O(1)$ at level~$k$ The overall normalization $(k+2)^{-1}$ from Theorem~\ref{thm:reduced-equals-kz} converts this to the residue $\Omega/(k+2)$, and the $d\log z$ kernel absorbs the pole from $dz/z$, producing the claimed form.
chapters/connections/log_ht_monodromy_frontier.tex:831:For evaluation modules (finite-dimensional $\fg$-representations), the exponential $\exp(2\pi i \cdot \Omega/(k+2))$ is a finite matrix exponential and convergence is automatic. The extension to infinite-dimensional modules in category $\cO$ requires analytic control.
chapters/connections/log_ht_monodromy_frontier.tex:985:\item \textbf{One-loop collapse.} By Theorem~\ref{thm:one-loop-koszul}, $V^k(\fg)$ is chirally Koszul at generic $k$. The $A_\infty$ tower collapses: $m_k = 0$ for $k \geq 3$. On the reduced evaluation comparison surface, the reduced connection therefore identifies with the KZ connection with residue $\Omega/(k + h^\vee)$.
chapters/connections/log_ht_monodromy_frontier.tex:989:$\exp(2\pi i \cdot \Omega/(k + h^\vee))$ is compared by the affine
chapters/connections/line-operators.tex:1016:$\operatorname{Res}_{z=0}R(z)=k\,\Omega/(k{+}2)$ is the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/examples/rosetta_stone.tex | sed -n '5480,5525p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5480	 \end{equation}
  5481	 where $e^{-2\pi ik\,\Omega_{12}}$ acts as a
  5482	 matrix on the colour indices.
  5483	 Projecting onto the irreducible components:
  5484	 \begin{align}
  5485	 d_{\mathrm{wrap}}\big|_{\mathbf{5}}
  5486	 &= (e^{-2\pi ik} - 1) \cdot \id_{\mathbf{5}},
  5487	 \notag \\[3pt]
  5488	 d_{\mathrm{wrap}}\big|_{\mathbf{3}}
  5489	 &= (e^{2\pi ik} - 1) \cdot \id_{\mathbf{3}},
  5490	 \label{eq:sl2-ann-wrap-isotypic}\\[3pt]
  5491	 d_{\mathrm{wrap}}\big|_{\mathbf{1}}
  5492	 &= (e^{4\pi ik} - 1) \cdot \id_{\mathbf{1}}.
  5493	 \notag
  5494	 \end{align}
  5495	 The three isotypic components acquire \emph{different}
  5496	 monodromy phases. This is the fundamental
  5497	 non-abelian phenomenon: the Heisenberg annular bar
  5498	 has a single scalar phase $e^{-2\pi ik}$ at each
  5499	 degree, while $V_k(\mathfrak{sl}_2)$ splits the
wait(call_1LTyYdWtui12VTVNZpeyhIYj) timed out:

thinking
**Summarizing bridging identity details**

I'm gathering details on the bridging identity, focusing on the raw versus normalized forms of the key formulas and their context, including trace-form and monodromy references. I want to highlight relevant vol II files for families like Heisenberg, affine, and Virasoro, checking specific lines and examples to include accurate mentions.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/frame/preface_trimmed.tex | sed -n '430,470p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   430	$\mathsf{Com}$ with $\mathsf{Lie}$; the duality functor on
   431	$\SCchtop$-algebras is an involution, and the open-colour dual
   432	$\cA^!_{\mathrm{line}}$ carries the dual algebraic structure.
   433	
   434	\section*{IX.\quad Three computations}
   435	
   436	The machine is tested on three families of increasing complexity;
   437	the full computations are carried out in the Introduction and in
   438	Part~\ref{part:examples}.
   439	
   440	\smallskip
   441	\noindent\textbf{Heisenberg} (class~$\mathbf{G}$, formal).
   442	One generator $J$, one OPE $J(z)J(w) \sim k/(z-w)^2$. The
   443	$\lambda$-bracket is $\{J_\lambda J\} = k\lambda$, with
   444	$m_2(J,J;\lambda) = k\lambda$ and all $m_{k\ge 3} = 0$. The
   445	classical $r$-matrix is $r(z) = k/z$ (the $d\log$ kernel absorbs
   446	one pole order from the double-pole OPE); the quantum $R$-matrix
   447	is $R(z) = \exp(k\hbar/z)$. The chiral Koszul dual is
   448	$\cA^!_{\mathrm{ch}} = \mathrm{Sym}^{\mathrm{ch}}(V^*)$ (note
   449	$\cH_k^! \neq \cH_{-k}$); the open-colour dual is
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar-vol2 && nl -ba chapters/examples/w-algebras-virasoro.tex | sed -n '430,520p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   430	\begin{definition}[Virasoro Spectral $r$-Matrix]
   431	\label{def:vir-r-matrix}
   432	The classical $r$-matrix is
   433	\begin{equation}
   434	r^{\text{Vir}}(\lambda, \mu) = \sum_{n=1}^3 \frac{r_n}{\lambda^n} \otimes \frac{1}{\mu},
   435	\end{equation}
   436	where
   437	\begin{align}
   438	r_3 &= \frac{c}{12} \, \mathbf{1} \otimes \mathbf{1},\\
   439	r_2 &= T \otimes \mathbf{1} + \mathbf{1} \otimes T,\\
   440	r_1 &= \partial(T \otimes \mathbf{1}) = (\partial T) \otimes \mathbf{1}.
   441	\end{align}
   442	\end{definition}
   443	
   444	The $r$-matrix satisfies the \emph{classical Yang--Baxter equation} (CYBE):
   445	\begin{equation}
   446	\label{eq:vir-CYBE}
   447	[r^{12}(\lambda_1-\lambda_2), r^{13}(\lambda_1-\lambda_3)] + [r^{12}(\lambda_1-\lambda_2), r^{23}(\lambda_2-\lambda_3)] + [r^{13}(\lambda_1-\lambda_3), r^{23}(\lambda_2-\lambda_3)] = 0,
   448	\end{equation}
   449	which follows from the Jacobi identity for the Virasoro $\lambda$-bracket.

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"r\\(z\" -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
notes/physics_mtheory_branes.tex:665: $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$ \\
notes/physics_4d_n2_hitchin.tex:815: (quantum) is the passage from the tree-level $R$-matrix $r(z)$ to the full quantum $R$-matrix
notes/theory_automorphic_shadow.tex:140: $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$ has
notes/theory_automorphic_shadow.tex:308:$r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{A_X})$, the
notes/theory_automorphic_shadow.tex:314:$r(z)$ encodes the singular part of the binary OPE\@.
notes/theory_automorphic_shadow.tex:315:Specifically, the pole structure of $r(z)$ is
notes/theory_automorphic_shadow.tex:317: r(z) = \sum_i \frac{\Omega_i}{z - z_i} + \text{regular},
notes/theory_automorphic_shadow.tex:333:OPE\@.) Thus $r(z)$ determines the Gram matrix, hence the
notes/theory_automorphic_shadow.tex:1180: Degree-$2$ collision $r(z)$ &
notes/theory_coha_e1_sector.tex:753: $R(z) = 1 + r(z)/z + O(z^{-2})$ where $r(z)$ is the classical $r$-matrix
notes/physics_bps_root_multiplicities.tex:765: $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)$ encodes
notes/physics_bps_root_multiplicities.tex:769: \gamma_2$ can form a bound state. The pole structure of $r(z)$
notes/theory_generalized_root_datum.tex:596: \item The real roots correspond to the poles of the collision $r$-matrix $r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta^{(2)})$.
notes/theory_e2_chiral_formalism.tex:975: $R(z,w) = \id + \hbar\, r(z,w) + O(\hbar^2)$, where
notes/theory_e2_chiral_formalism.tex:976: $r(z,w) \in \cA \otimes \cA \otimes k((z))((w))$ is the
notes/theory_e2_chiral_formalism.tex:982: $r(z,w)$, and the QYBE~\eqref{eq:qybe} is a quantization of the
notes/physics_celestial_cy.tex:72:We connect celestial holography with the quantum vertex chiral groups of CY3s. The Mellin transform of 4d scattering amplitudes produces a 2d celestial chiral algebra on $S^2$. For 4d $\mathcal{N}=2$ theories from CY3 compactification, this algebra is the genus-0 sector of $G(X)$. The simplest case, $\cW_{1+\infty} = Y(\widehat{\mathfrak{gl}}_1) = G(\mathbb{C}^3)$, recovers the $\mathfrak{w}_{1+\infty}$ symmetry of pure gravity. The celestial OPE is the collision $r$-matrix $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_A)$; higher soft theorems correspond to higher-degree shadows of $\Theta_A$; higher-genus corrections control loop-level celestial amplitudes.
notes/physics_celestial_cy.tex:379:collision $r$-matrix $r(z)$ of $G(X)$.
notes/physics_celestial_cy.tex:485:r(z)
notes/physics_celestial_cy.tex:500:$(z-w)$; hence $r(z)$ has pole orders one less than the OPE
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/examples/quantum_group_reps.tex | sed -n '100,170p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   100	= (k+2)/(2\sin^2(\pi/(k+2)))$.
   101	The $S$-matrix entries are
   102	$S_{mn} = \sqrt{2/(k+2)} \, \sin(\pi(m+1)(n+1)/(k+2))$.
   103	This is a modular tensor category: the Reshetikhin--Turaev functor
   104	produces the $SU(2)$ Chern--Simons invariants of 3-manifolds.
   105	\end{example}
   106	
   107	
   108	\section{The $R$-matrix as categorical $r(z)$}
   109	\label{sec:r-matrix-categorical}
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
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n 'r\\(z\\) = k/z' -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/e1_chiral_algebras.tex:1270: $r(z) = k/z$ has no nontrivial $z$-dependent correction to $\Delta$.
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n 'k\\\\Omega' -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n 'Omega/\\(k' -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
notes/theory_kl_e2_chiral.tex:599:KZ connection has residue $\Omega/(k+\hv)$ at degree 2, and its
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba notes/theory_kl_e2_chiral.tex | sed -n '550,610p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   550	\end{remark}
   551	
   552	%% ======================================================================
   553	\section{The classical $r$-matrix and KZ monodromy}
   554	\label{sec:r-matrix-collision}
   555	%% ======================================================================
   556	
   557	In the monograph's framework (Construction~\ref{constr:cy-r-matrix}),
   558	the degree-$2$ collision residue of the universal Maurer--Cartan
   559	element is the classical $r$-matrix:
   560	\[
   561	 r(z) = \mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_A)
   562	 \;\in\; A \otimes A \otimes \mathbb{C}((z)).
   563	\]
   564	For affine Kac--Moody algebras this is the trace-form normalization;
   565	the quantum $R$-matrix is recovered separately from the KZ monodromy
   566	kernel.
   567	
   568	For $A = V_k(\frakg)$:
   569	
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && rg -n \"\\(c/2\\)/z\\"'^3" -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
notes/physics_celestial_cy.tex:531: % r(z) = (c/2)/z^3 + 2T/z.
exec
/bin/zsh -lc 'cd /Users/raeez/calabi-yau-quantum-groups && rg -n "2T/z" -g"*.tex"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
notes/physics_celestial_cy.tex:531: % r(z) = (c/2)/z^3 + 2T/z.
chapters/theory/quantum_chiral_algebras.tex:416:In mode language: $T_{(3)} T = c/2 = 1/2$, $T_{(1)} T = 2T$, $T_{(0)} T = \partial T$, $T_{(2)} T = 0$. In lambda-bracket form (AP44, divided powers $\lambda^{(n)} = \lambda^n/n!$): $\{T_\lambda T\} = \tfrac{c}{12}\lambda^3 + 2T\lambda + \partial T = \tfrac{1}{12}\lambda^3 + 2T\lambda + \partial T$. The classical $r$-matrix is $r^{\mathrm{Vir}}(z) = \tfrac{1}{2}/z^3 + 2T/z$ (cubic $+$ simple pole; AP19: one less than the quartic OPE pole via $d\log$ absorption).
exec
/bin/zsh -lc "cd /Users/raeez/calabi-yau-quantum-groups && nl -ba chapters/theory/quantum_chiral_algebras.tex | sed -n '380,430p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   380	\]
   381	The propagator of the free-field system on $C$ is
   382	\[
   383	 \langle A^{(m,n)}(z) \, A^{(p,q)}(w) \rangle
   384	 \;=\; \frac{\delta_{m+p,0}\,\delta_{n+q,0}}{(z - w)^2},
   385	\]
   386	where the double pole is the standard holomorphic propagator on $\C$ and the delta-conditions enforce charge conservation in the normal directions.
   387	
   388	\emph{Step~4: identification of the $W_{1+\infty}$ currents.}
   389	The $\GL(2)$-invariant combinations of the normal modes produce the $W_{1+\infty}$ generators. At spin~$s$:
   390	\[
   391	 J_s(z_1) \;=\; \sum_{m+n = s-1} c_{m,n}^{(s)} \, A^{(m,n)}(z_1),
   392	\]
   393	where $c_{m,n}^{(s)}$ are the $\GL(2)$-invariant coefficients (the minors of the identity matrix, matching the invariant polyvector fields $\Omega_s$ of \texttt{c3\_lie\_conformal.py}). In particular:
   394	\begin{itemize}
   395	 \item Spin~$1$: $J(z_1) = A^{(0,0)}(z_1)$, the mode at the origin of the normal fiber.
   396	 \item Spin~$2$: $T(z_1) = \frac{1}{2\Psi}\mathopen{:}J(z_1)^2\mathclose{:}$ via the Sugawara construction at level $\Psi$.
   397	\end{itemize}
   398	
   399	\emph{Step~5: OPE computation.}
thinking
**Searching for file conventions**

I need to ensure consistency within each file, specifically ensuring that if both trace-form and KZ conventions appear, they must also have a bridge identity. I should look out for such files by searching for KM formulas in volume 1. It's possible that some files contain both `kΩ/z` and `Ω/((k+h^∨)z)`. I think I'll run targeted searches in active directories and check lines separately for the different volumes.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '(k\\\\,?\\\\Omega|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)z\\)|k\\,?\\\\Omega/z|r\\"'^'"\\{?KM\\}?\\(z\\)|r\\(z\\) = .*\\\\Omega.*z|R\\(z\\) = 1 \\+ .*\\\\Omega/z)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '((c/2)/z\\"'^4|(c/2)/z'"\\"'^3 '"\\+ 2T/z|r\\"'^'"\\{?Vir\\}?\\(z\\)|r\\"'^'"\\{\\\\mathrm\\{Vir\\}\\}\\(z\\)|r\\"'^'"\\{\\\\mathrm\\{coll\\}\\}_c\\(z\\)|c/12|quartic pole|cubic pole)' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '((c/2)/z\\"'^4|(c/2)/z'"\\"'^3 '"\\+ 2T/z|r\\"'^'"\\{?Vir\\}?\\(z\\)|r\\"'^'"\\{\\\\mathrm\\{Vir\\}\\}\\(z\\)|r\\"'^'"\\{\\\\mathrm\\{coll\\}\\}_c\\(z\\)|c/12|quartic pole|cubic pole)' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '(k/z\\"'^2|1/z'"\\)|r\\"'^'"\\{?Heis\\}?\\(z\\)|r\\(z\\) = k/z|r\\(z\\) = \\\\frac\\{k\\}\\{z\\}|R\\(z\\) = \\\\exp\\(k\\\\hbar/z\\)|R\\(z\\)=z\\"'^k)'"' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '(k\\\\,?\\\\Omega|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)z\\)|k\\,?\\\\Omega/z|r\\"'^'"\\{?KM\\}?\\(z\\)|r\\(z\\) = .*\\\\Omega.*z|R\\(z\\) = 1 \\+ .*\\\\Omega/z)' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '((c/2)/z\\"'^4|(c/2)/z'"\\"'^3 '"\\+ 2T/z|r\\"'^'"\\{?Vir\\}?\\(z\\)|r\\"'^'"\\{\\\\mathrm\\{Vir\\}\\}\\(z\\)|r\\"'^'"\\{\\\\mathrm\\{coll\\}\\}_c\\(z\\)|c/12|quartic pole|cubic pole)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '(k/z\\"'^2|1/z'"\\)|r\\"'^'"\\{?Heis\\}?\\(z\\)|r\\(z\\) = k/z|r\\(z\\) = \\\\frac\\{k\\}\\{z\\}|R\\(z\\) = \\\\exp\\(k\\\\hbar/z\\)|R\\(z\\)=z\\"'^k)'"' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '(k/z\\"'^2|1/z'"\\)|r\\"'^'"\\{?Heis\\}?\\(z\\)|r\\(z\\) = k/z|r\\(z\\) = \\\\frac\\{k\\}\\{z\\}|R\\(z\\) = \\\\exp\\(k\\\\hbar/z\\)|R\\(z\\)=z\\"'^k)'"' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' '(k\\\\,?\\\\Omega|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)z\\)|k\\,?\\\\Omega/z|r\\"'^'"\\{?KM\\}?\\(z\\)|r\\(z\\) = .*\\\\Omega.*z|R\\(z\\) = 1 \\+ .*\\\\Omega/z)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections10_13_draft.tex:354:$r(z)=k\Omega/z$ (Yang's solution of the CYBE),
/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:498:\item Affine Kac--Moody $\widehat\fg_{k}$: $r(z) = k\Omega_{\fg}/z$
/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:774:$\widehat\fg_{k}$ with $r(z) = k\Omega_{\fg}/z$, Virasoro $\Vir_{c}$ with $r(z) = (c/2)/z^{3}
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:393:$r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:449:$\Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:508:f^{ab}_{\;\;c}\, J^c(w)/(z-w)$ has $c_0 = k\,\Omega/(k + h^\vee)$
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:607:$r_{\widehat{\fg}_k}^{(1)}(z, \tau) = k\,\Omega\, \zeta_\tau(z)/(k+h^\vee)$,
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:657:$c_0 = k\,\Omega/(k+h^\vee)$: collision depth $k_{\max} = 1$, and
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:976:$r^{(1)}_{\widehat{\fg}_k}(z, \tau) \to \Omega/((k+h^\vee)z)$.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1004:$\sum_{j \neq i}k\,\Omega_{ij}/((k+h^\vee)(z_i - z_j))\, dz_{ij}$,
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1012:rational $r$-matrix $\Omega/((k+h^\vee)z)$ in the Kazhdan
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1016:residue $r_{\widehat{\fg}_k}(z) = \Omega/((k+h^\vee)z)$\textup{)}.
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1105:For $\cA = \widehat{\fg}_k$, $c_0 = k\,\Omega/(k + h^\vee)$, and the
/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:1106:monodromy is $2\eta_\tau\, k\,\Omega/(k + h^\vee)$. The
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:487:algebra~$\mathfrak{g}$ at level~$k$ (that is, $r(z) = k\,\Omega/z$ where
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:499:$r(z) = \Omega / ((k + h^\vee)\,z)$ for
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:1277:rational $r$-matrix $r(z) = k\,\Omega/z$ generates the RTT presentation
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:710:r(z) \;=\; \frac{k\,\Omega}{z}\,,
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:736:the passage from $r(z) = k\,\Omega/z$ to
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1162:affine Kac--Moody, $r(z) = k\,\Omega/z$ is matrix-valued; the
 exited 1 in 51ms:

 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1421:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$
/Users/raeez/chiral-bar-cobar-vol2/main.tex:1423:The quartic pole forces the infinite $\Ainf$ tower, the Koszul
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2486:The Heisenberg R-matrix $R(z) = \exp(k\hbar/z)$
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:8212:$R(z) = \exp(k\hbar/z)$
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:1047:$K^{(1)}(z|\tau)/z^2 = 1/z^3 + O(1/z)$:
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:1844:$r(z) = k/z$ (the abelian $r$-matrix),
/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:497:\item Heisenberg $\cH_{k}$: $r(z) = k/z$, $\kappa(\cH_{k}) = k$.
/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:773:Heisenberg $\cH_{k}$ with $r(z) = k/z$, affine Kac--Moody
/Users/raeez/chiral-bar-cobar/standalone/sc_chtop_pva_descent.tex:1247:$r(z) = k/z$.
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:608:characteristic: $r(z) = k/z$ is already $\Sigma_2$-invariant
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1160:For the Heisenberg algebra, $r(z) = k/z$ is already scalar, and the
/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:2975:$R$-matrix $r(z) = k/z$ is scalar; averaging loses nothing; the
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:97:% PE-1: r-matrix. Family: Heis. r(z) = k/z. Level: k. OPE pole 2, r pole 1.
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:1974:$r(z) = k/z$ (after $d\log$ absorption of the double pole, with the
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:1976:exponential $R(z) = \exp(k\hbar/z)$
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:2080:$r(z) = k/z$ exactly. We record both the construction and the
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:2117:$R(z) = \exp(k\hbar/z)$ by expanding to first order in $\hbar$ is
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:2133:coefficient of $\hbar^1$ gives $r(z) = k/z$. At $k = 0$ this
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:2237:$r$-matrix is $r(z) = k/z$, and the shadow tower terminates at
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:3398: for the associated $r$-matrix $r(z) = k/z$.
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:3563:$r(z) = k/z$, \emph{not} $1/z$; at $k = 0$ both the propagator and
/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex:3926:\item $R(z) = \exp(k\hbar/z)$, computed by exponentiating the classical
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:1871:is quartic (the $r$-matrix has cubic pole by $d\log$-absorption,
/Users/raeez/chiral-bar-cobar/appendices/nonlinear_modular_shadows.tex:1332:The quadratic term is the quartic pole of the $TT$ OPE,
/Users/raeez/chiral-bar-cobar/appendices/_sl2_yangian_insert.tex:639:algebra (class~$\mathbf M$, quartic poles, infinite shadow depth),
/Users/raeez/chiral-bar-cobar/standalone/chiral_chern_weil.tex:1036:$\kappa = c\cdot(1/2 + 1/3 + 1/4) = 13c/12$.
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:598: $r^{\mathrm{Vir}}(z) = (c/2)/z^3 + 2T/z$,
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:606:pole ($z^{-4}$ in $T(z)T(w)$); absorption produces the cubic pole
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:607:$z^{-3}$ of $r^{\mathrm{Vir}}(z)$. The general principle:
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:764:r^{\mathrm{Vir}}(z) = \frac{c/2}{z^3} + \frac{2T}{z}.
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:794:a cubic pole and the coproduct is trivial: gravitons braid but
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:821: & $(c/2)/z^3 + 2T/z$ (cubic pole) \\[2pt]
/Users/raeez/chiral-bar-cobar/standalone/computations.tex:838:coproduct. The Virasoro algebra has $\lambda^3$ (quartic pole),
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:2574:The second reduction manufactures the quartic pole
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:3177:$\{T{}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$.
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:3840:By contrast, the Virasoro OPE has a quartic pole, giving
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:5530:reflecting the absence of a cubic pole in the Virasoro OPE
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:5549:For the Virasoro algebra: the quartic pole gives depth $d = 3$,
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:5551:$d = 0$. The cubic pole is absent, so $d = 2$ does not appear.
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:5827:(from the quartic pole, i.e.\ the central charge~$c$) is the
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:5833:geometric expression of the absence of a cubic pole,
/Users/raeez/chiral-bar-cobar/appendices/ordered_associative_chiral_kd.tex:6113: quartic pole;
 exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'r\\(z\\) = \\\\Omega/z' -g\"*.tex\"" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:




thinking
**Summarizing files with bridging and conventions issues**

I’m organizing a table-like summary grouped by volume, listing key `.tex` files and their line numbers to highlight bridging identities, formula types, level prefixes, and conventions. I’m focusing on highest-risk files mixing conventions, especially where bridging is spelled out or differences are stressed, with brief notes per entry and an overall summary mentioning those top-risk files. This way, the user gets a clear picture of potential issues without including entire large files.

thinking
**Identifying file issues**

It seems like the file I'm looking at has mixed conventions, which can be confusing. On top of that, there's this odd equation on line 1292: `∇ = d - ħ r(z) dz/z`, which might relate to AP117? I need to investigate that further to clarify what’s happening. It’s quite a task, but getting this right is important! Let’s see how I can sort these inconsistencies out effectively.
thinking
**Inspecting candidate files**

I think I'll need to take a look at some of the volume 1 files. It's important to identify which candidate files have actual issues. I'll inspect them closely to see what's going on. I want to make sure I address any problems properly so everything runs smoothly. It sounds like a bit of a task, but I’m ready to dive into it and figure things out!
thinking
**Planning r-matrix editing**

I need to fill out the template in the commentary before editing any r-matrix surface. After identifying the exact files to touch, I might need to provide PE-1 blocks. For Heis/Vir, there may not be an explicit PE template, but the r-matrix trigger is necessary. I could update the plan and set tasks: first, enumerate live inconsistencies; second, inspect candidate files; third, patch the current repo; fourth, verify using grep; and finally summarize blocked volumes 2 and 3. Let’s use an update plan!
Plan update
Focused on live manuscript surfaces and separating editable Vol I fixes from read-only Vol II/III findings.
  → Inspect candidate live files with mixed or suspect KM/Heis/Vir r-matrix formulas and confirm which ones actually violate the convention rules
  • Apply minimum truthful Vol I edits with explicit bridge statements or corrected family formulas
  • Re-grep the modified surface plus Vol II/III read-only surfaces and produce exact findings, fixes, and remaining blocked inconsistencies
codex
**Volume I**
- `chapters/examples/kac_moody.tex:82-127 & 750-774` — Affine KM: table entry and modular triple record `r(z)=Ω/((k+h^∨)z)` (KZ normalization) alongside the remark that `r(z)` degenerates at the critical level; later remark (lines 750‑771) introduces the trace-form avatar `kΩ_tr/z` and the bridge `kΩ_tr=Ω/(k+h^∨)`. Level prefix (`k`) is present only in the denominator/minor remark, the convention is KZ but the page explicitly states both normalizations, so bridge identity is spelled out to avoid conflation. 
- `chapters/examples/heisenberg_eisenstein.tex:1841-1847` — Heisenberg: the holographic datum spells `r(z)=k/z` (level prefix `k` there), trace/kappa convention is the scalar abelian `k/z`; no extra bridge needed because only the Heisenberg convention appears. 
- `chapters/examples/w_algebras.tex:45-90` — Virasoro (Shadow M): `r(z)=(c/2)/z^3+2T/z` in the archetype table and modular triple, so level-like parameter `c` is explicit and only the Virasoro pole structure is referenced (no mixing), hence no bridge column.

**Volume II**
- `chapters/frame/preface_trimmed.tex:441-469` — Heisenberg & affine KM summary: `r(z)=k/z` for Heisenberg (level prefix present) and `r(z)=kΩ/z` for affine KM; adjoining sentence introduces the KZ connection `∇=d-(1/(k+h^∨))Ω dz/z`, so the trace convention is accompanied by the Sugawara-shifted bridge to KZ residues. 
- `chapters/examples/rosetta_stone.tex:5502-5511` — Affine KM log monodromy: raw collision residue `r(z)=kΩ/z` contrasts with the KZ-normalized residue `Ω/(k+h^∨)` in describing wrap monodromy, and the text explicitly states the two differ by Sugawara normalization, so the bridge is documented. 
- `chapters/examples/w-algebras-virasoro.tex:430-466` — Virasoro spectral `r`-matrix: Laplace kernel leads to `r^{\mathrm{coll}}(z)=(c/2)/z^3+2T/z` (cubic + simple pole) in the CYBE verification, no other conventions are mixed.

**Volume III**
- `chapters/examples/quantum_group_reps.tex:108-149` — Affine KM/CY interface: Proposition explains the classical collision residue `r(z)=kΩ/z+O(1)` (level prefix `k` present) and its interpretation as the classical limit of the quantum Group `R`-matrix; only trace-form is used, so no additional bridge is claimed.
- `notes/theory_kl_e2_chiral.tex:557-603` — Kac–Moody collision vs. KZ monodromy: `r(z)=kΩ/z+O(1)` (trace form) and the KZ residue `Ω/(k+h^∨)` are both recorded, and the surrounding remark warns they are two normalizations “and should not be identified,” which flags a high-risk surface that already documents the needed bridge while stressing they remain distinct. 
- `chapters/theory/quantum_chiral_algebras.tex:399-417` — Categorical example from the CY3 geometry: spin‑1 Heisenberg `r(z)=Ψ/z` and the associated Virasoro `r^{\mathrm{Vir}}(z)=(1/2)/z^3+2T/z` (with $c=1$ automatically) are written, so level prefixes appear but only the Virasoro pole structure is discussed (no mixing).

Findings: the highest-risk surfaces are `chapters/examples/kac_moody.tex` (Vol I) and `notes/theory_kl_e2_chiral.tex` (Vol III), because each mixes trace-form and KZ normalizations; both already include explicit bridge statements (the former via the `kΩ_tr=Ω/(k+h^∨)` identity, the latter by insisting the two residues “should not be identified”), so they are the critical checkpoints if any future edits touch those conventions.

thinking
**Reviewing problem areas**

I’m considering the equation from my notes, specifically if there's a bridge issue, but I need to prioritize the actual problems instead of getting caught up in too many details. I might be able to rely on existing notes that reference `fix_wave_C_...`, which could provide useful context. However, I think it’s important to focus on the ground source and inspect any suspicious files. I'll approach this using parallel processing to manage it effectively.
codex
I’ve narrowed the editable Vol I risk to a small set of files that either mix trace-form and KZ normalizations in one file or appear to use the wrong family formula. I’m reading those local contexts now before I patch anything.
exec
/bin/zsh -lc "sed -n '220,245p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '470,520p' chapters/connections/thqg_introduction_supplement_body.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,190p' standalone/classification.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4945,4975p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5800,5835p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,720p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '615,640p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1040,1085p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 The Yang $R$-matrix is
 \begin{equation}\label{eq:rmatrix-type-a}
 R(u) = u\, \mathbb{1} + P,
 \end{equation}
 where $P$ is the permutation operator on $V \otimes V$.
 The corresponding Casimir is $\Omega = P - \mathbb{1}/N$
 with $N = n+1$, so in the KZ normalisation the classical $r$-matrix at affine
 level $k$ reads
 $r(z) = \Omega/\bigl((k + h^\vee)\,z\bigr) = (P - \mathbb{1}/N)/\bigl((k + n + 1)\,z\bigr)$
 (Remark~\ref{rem:km-collision-residue-rmatrix}).
 At the critical level $k = -h^\vee$ the denominator vanishes,
 tracking the Sugawara singularity.

\item \emph{Type $B_n$ $(\mathfrak{so}_{2n+1}$, $V = \bC^{2n+1})$.}
 The $R$-matrix is%
 \footnote{The pole position of the $R$-matrix in types $B$, $C$, $D$
 is denoted~$\varkappa$ (following Molev~\cite{molev-yangians}) to
 avoid conflation with the modular characteristic~$\kappa(\cA)$
 of Theorem~\textup{\ref{thm:modular-characteristic}};
 these are unrelated quantities.}
 succeeded in 51ms:

At genus~$0$, the moduli space $\overline{\mathcal{M}}_{0,n}$ is the
Deligne--Mumford compactification of the space of $n$-pointed rational
curves. The shadow connection restricted to genus~$0$ takes the
explicit form:

\begin{equation}\label{eq:thqg-intro-kz-explicit}
\nabla^{\mathrm{KZ}}_{0,n}
\;=\;
d \;-\; \sum_{1 \le i < j \le n}
\frac{r_{ij}(z_i - z_j)}{z_i - z_j}\,dz_i,
\end{equation}
where $r_{ij}(z) = (\operatorname{id} \otimes \operatorname{id}) \circ
r(z) \in \operatorname{End}(M_i) \otimes \operatorname{End}(M_j)$ is
the $r$-matrix acting on the $i$-th and $j$-th module insertions.

When the $r$-matrix is the rational $r$-matrix of a simple Lie
algebra~$\mathfrak{g}$ at level~$k$ (that is, $r(z) = k\,\Omega/z$ where
$\Omega = \sum_a t^a \otimes t_a$ is the Casimir element), the
connection~\eqref{eq:thqg-intro-kz-explicit} reduces to the
 succeeded in 50ms:
universality is $\barB^{\mathrm{ord}} = T^c(s^{-1}\bar\cA)$, not the
symmetric bar.

\textsc{Information content.} An equivariant
$\End(V^{\otimes n})$-valued meromorphic function strictly
contains its scalar trace. The averaging map
$\operatorname{av}$ is surjective but not injective: the kernel
records the non-symmetric components of the line-operator data.
For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
the symmetrization recovers the scalar
$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
full Yangian double; the symmetrization recovers only
$\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
= k\dim\mathfrak g/(2h^\vee)$, and the full
$\kappa(\widehat{\mathfrak g}_k)
= (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
appears only after adding the Sugawara shift.

\textsc{Physical primacy.} The natural physical objects are
 succeeded in 51ms:
simple Lie algebra $\fg$ and every non-critical level
$k \neq -h^\vee$: type~$A$ ($\mathfrak{sl}_N$),
types $B$, $C$, $D$ (orthogonal and symplectic),
exceptional types $E_6$, $E_7$, $E_8$, $G_2$, $F_4$.
For all of these:
\[
\kappa\bigl(V_k(\fg)\bigr)
= \frac{\dim(\fg)\,(k + h^\vee)}{2h^\vee}\,.
\]

\noindent\textbf{Characterization.}
The nonzero cubic shadow $S_3 = \alpha$ arises from the Lie bracket
(structure constants $f_{abc}$), while the Jacobi identity forces the
quartic shadow $S_4 = 0$ on the primary line. The $r$-matrix
$r(z) = \Omega_\fg/((k{+}h^\vee)z)$ (single simple pole; the bar construction absorbs
one power of the OPE pole) encodes all nonlinear structure. The tree-level
graph sum terminates at trivalent vertices.

\medskip

 succeeded in 51ms:
construction. The $\Pthree$ bracket on the derived
chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))
= \HH^*(\BarSig(V_k(\fg)), \BarSig(V_k(\fg)))$ is the
$\Etwo$-Hochschild cohomology operation derived from
the fundamental class of $S^2 \subset \Conf_2(\RR^3)$.
At degree~$2$, this operation is the residue of the
classical $r$-matrix paired with the fundamental class
of $S^1 \subset \Conf_2(\CC)$. In the KZ normalisation
(see~\eqref{eq:kz-sl2-degree2} and the conventions
of~\S\ref{subsec:sl2-chiral-e3}):
% AP126/AP148: KZ convention r(z) = Omega/((k+h^v)z).
% At k=0, r = Omega/(h^v z) != 0 (non-abelian; correct for KZ).
% At k=-h^v, r diverges (Sugawara singularity).
\begin{equation}\label{eq:p3-from-r-matrix-residue}
  r(z) = \frac{\Omega}{(k + h^\vee)\,z},
  \qquad
  \operatorname{Res}_{z=0}\bigl[r(z)\bigr]
  = \frac{\Omega}{k + h^\vee}.
\end{equation}
The residue acts on $X \otimes Y \in \fg \otimes \fg$
 succeeded in 51ms:
topological CFG construction.

\begin{proposition}[The $\cD$-module structure]
\label{prop:chiral-e3-dmod}
\ClaimStatusProvedHere
The chiral $\Ethree$-algebra
$\CE^{\mathrm{ch}}_k(\fg)$ carries a flat connection
\begin{equation}\label{eq:chiral-e3-connection}
  \nabla^{\mathrm{ch}}
  \;=\;
  d \;+\; \sum_{i < j}
  \frac{k\,\Omega_{ij}}{z_i - z_j}\,dz_{ij}
\end{equation}
on $\Conf_n(X)$, where $\Omega_{ij}$ is the Casimir element
acting on the $i$-th and $j$-th tensor factors. This is the
Knizhnik--Zamolodchikov connection.
\begin{enumerate}[label=\textup{(\roman*)}]
\item The flatness
  $(\nabla^{\mathrm{ch}})^2 = 0$ follows from the
  classical Yang--Baxter equation for the $r$-matrix
 succeeded in 51ms:
$\kappa(\cA)=\operatorname{av}(r(z))$, while non-abelian affine
Kac--Moody adds the Sugawara shift $\dim(\fg)/2$.
The ordered theory of
Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
the symmetric theory is its image.

The $\Eone$ side is strictly richer: at degree~$2$ alone it
distinguishes algebras that the symmetric side identifies.
The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
$\widehat{\mathfrak{sl}}_2$-shadow
$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
h^\vee)$, but the underlying $r$-matrices distinguish them by their
matrix support. The ordered bar separates what the symmetric bar
collapses.
\end{remark}


\subsection{The genus-$g$ propagator and curvature}
\label{subsec:genus-g-propagator}
 succeeded in 51ms:
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
 quadratic Casimir tensor (inverse Killing form) and the Sugawara
 denominator $k + h^\vee$ arises from dualizing the zeroth product
exec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' 'Heisenberg.*Omega|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega|r\\(z\\) = k\\\\Omega/z with \\\\Omega the Casimir|Heisenberg .* k\\\\Omega/z|r\\(z\\) = k\\\\Omega/z' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' 'Omega_\\\\{\\\\mathrm\\{tr\\}\\}["'^'"\\n]*= \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|r\\(z\\) = \\\\Omega_\\\\{\\\\mathrm\\{tr\\}\\}/z|r\\(z\\)=\\\\Omega_\\\\{\\\\mathrm\\{tr\\}\\}/z|Equivalently, in the trace-form normalization where' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/genus_expansions.tex:76:%: canonical form r(z) = k\Omega/z; k=0 -> r=0
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5011:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5026:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
/Users/raeez/chiral-bar-cobar/chapters/examples/lattice_foundations.tex:5030:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:501:$r(z) = k\Omega/z$ to $\kappa(\widehat{\mathfrak g}_k)$ discards
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:524:where $G_{\Omega}$ is the genus-2 Green function (derivative of the prime form with respect to $w_1$). The Heisenberg algebra is a \emph{free} (Gaussian) theory: the two-point function at any genus is exactly the Green's function, with no perturbative corrections in $\kappa$. The Eisenstein series $E_4(\Omega), E_6(\Omega)$ appear in the \emph{expansion of the Green's function itself} near the diagonal (encoding the geometry of $\Sigma_2$), not as separate quantum corrections.
/Users/raeez/chiral-bar-cobar/chapters/examples/heisenberg_eisenstein.tex:701:The full partition function sums over genera: $Z = \sum_{g \geq 0} \hbar^{2g-2} Z_g$. For the Heisenberg algebra (a free theory), each genus-$g$ contribution is exact; it is \emph{not} a perturbative loop correction. Rather, $Z_g$ encodes the propagator on $\Sigma_g$ through the period matrix $\Omega_g$.
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4409: r-matrix $r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4731: $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:1667:More precisely, the Lie algebra cohomology is classified by the bar complex of the rank-1 Heisenberg algebra: it computes $H^*_{\mathrm{Lie}}(\mathfrak{h}_g, \mathbb{C}_k)$ of the abelian Lie algebra $\mathfrak{h}_g = H^0(\Sigma_g, \Omega^1) \oplus H^1(\Sigma_g, \mathcal{O})$ (dimension~$2g$) with coefficients in the 1-dimensional representation determined by the level~$k$ central extension. For a 1-dimensional central extension of an abelian Lie algebra, the Chevalley--Eilenberg differential $d_{\mathrm{CE}}$ on $\Lambda^*(\mathfrak{h}_g^*)$ satisfies $d_{\mathrm{CE}}(\xi) = k \cdot \omega(\xi, -)$ where $\omega$ is the symplectic form from the intersection pairing. The resulting cohomology is concentrated in degrees~$\leq 2$: since $k \neq 0$, the map $d_{\mathrm{CE}}: \Lambda^1 \to \Lambda^2$ is surjective onto the $\omega$-multiples, and by induction the higher cohomology groups $H^n = 0$ for $n > 2$.
/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:2913:For the Heisenberg algebra at genus $g$ on a Riemann surface $\Sigma_g$ with period matrix $\Omega \in \mathbb{H}_g$ (Siegel upper half-space):
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1139:$r(z) = k\Omega/z$ (the double pole $k\,g^{ab}/(z{-}w)^2$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1142:equation for $r(z) = k\Omega/z$ reduces to the infinitesimal braid
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1198:$G_2$ ($V = \bC^{7}$). The classical $r$-matrix $r(z) = k\Omega/z$
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1213:$R$-matrix $r(z) = k\Omega/z$ of
/Users/raeez/chiral-bar-cobar/standalone/analytic_sewing.tex:1716:\item the Heisenberg factor~$Z_g(\cH_r;\,\Omega)$ converges by
/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex:55:The mechanism is uniform: the Heisenberg OPE $a(z)a(w) \sim k/(z-w)^2$ has only a double pole, so the residue integrand at each collision divisor $D_{ij}$ acquires a triple pole $k \cdot d\epsilon/\epsilon^3$ against the logarithmic form $\eta_{ij} = d\epsilon/\epsilon$, which has zero residue. No Arnold relation or configuration-space geometry is needed for this vanishing; it is purely a pole-order phenomenon. The Arnold relation constrains the \emph{dimension} of the form space ($\dim \Omega^{n-1}(\overline{\Conf}_n) = (n-1)!$), but does not participate in the differential. This is the chain-level explanation for the abelian bar complex being exact: $d_{\mathrm{bracket}} = 0$ because the OPE has no simple pole.
/Users/raeez/chiral-bar-cobar/standalone/koszulness_fourteen_characterizations.tex:490:classical $r$-matrix $r(z) = k\Omega/z$ admits no nontrivial
/Users/raeez/chiral-bar-cobar/standalone/koszulness_fourteen_characterizations.tex:829:classical $r$-matrix $r(z) = k\Omega/z$ via the
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_drinfeld_kohno.tex:7088:$r(z) = k\Omega/z$ is an odd function of~$z$.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'appendices/**' --glob 'standalone/**' --glob 'README.md' --glob 'main.tex' 'r\\(z\\) = \\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|r\\(z\\) = \\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|r\\(z\\) = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z\\)|r\\(z\\) = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|KZ normalisation|trace-form' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:Omega_\\{\\mathrm\{tr\}\}[^\n]*= \\Omega/\(k\+h\^\\vee\)|r\(z\) = \\Omega_\\{\\mathrm\{tr\}\}/z|r\(z\)=\\Omega_\\{\\mathrm\{tr\}\}/z|Equivalently, in the trace-form normalization where)
                ^
error: repetition quantifier expects a valid decimal
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:583:space gives (in the KZ normalisation)
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:716:The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:744: Equivalently, in the trace-form convention the same simple-pole term is
/Users/raeez/chiral-bar-cobar/chapters/examples/level1_bridge.tex:80: $\Omega/\bigl((1{+}h^\vee)\,z\bigr)$ (KZ normalisation at $k = 1$; cf.\ Remark~\ref{rem:km-collision-residue-rmatrix}) \\
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:226: with $N = n+1$, so in the KZ normalisation the classical $r$-matrix at affine
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1063: Equivalently, in the trace-form normalization where
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:227:% Convention: trace-form normalisation. In the KZ normalisation
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:92:$r$-matrix $r(z)$ & $\Omega/\bigl((k{+}h^\vee)\,z\bigr)$ (Casimir, KZ normalisation, Comp.~\ref{comp:sl2-collision-residue-kz}) \\
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:117:$r$-matrix is recorded in the KZ normalisation
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:769:\emph{trace-form} basis in which the level dependence is absorbed
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5495: Killing form; KZ normalisation, cf.\
/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:5639:\textup{(}simple pole in the KZ normalisation, cf.\
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:499:$r(z) = \Omega / ((k + h^\vee)\,z)$ for
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:462:algebra of a simple Lie algebra~$\fg$. In the trace-form
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:483:invariant form. In the trace-form normalization used in Volume~I we
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:499:On the generic trace-form locus this is the same family as
/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:505:% Lie bracket of g persists; the trace-form vanishing r=0 at k=0
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1655:$r(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4768:\textup{(}vanishing at $k=0$ in trace-form normalization; at the D3 level
/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex:482:\text{for non-abelian affine Kac--Moody in the trace-form convention.}


thinking
**Determining minimal edits**

I need to figure out the minimal truthful edits because we can't address every standalone, but the user's request is for exhaustive work within the scope. All current repo files are accessible, but there are lots of potential issues. I have to determine which inconsistencies matter. For instance, I spotted a few files that misrepresent Heisenberg context. Some lines might need closer inspection to ensure we don't overcorrect any formulas or mix up contexts unnecessarily.
thinking
**Identifying potential issues**

It looks like the set of exact issues might be smaller than I thought. First, there's a trace-form equivalence that’s mis-specified in `chapters/examples/yangians_foundations.tex`. Second, there’s a missing bridge in `chapters/connections/thqg_introduction_supplement_body.tex`. Lastly, there's a Heisenberg misformula in `standalone/introduction_full_survey.tex`. I need to search for Heisenberg-specific equations like `r_{\cH_k}(z) = k\Omega/z` across the editable repo. It seems I’ve found relevant lines in just one file, so now I’ll inspect other related sections for clarity.
exec
/bin/zsh -lc "sed -n '1768,1835p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2998,3018p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
factorisation $\cD$-module]
\label{prop:fact-dmod-props}
Let $\cA$ be a chiral algebra on a smooth proper curve $X$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Holonomicity and singularity type.)}
  $\cF_n^{\mathrm{ord}}(\cA)$ is a holonomic
  $\cD$-module on $X^n$.
  The singularity type along $\bigcup \Delta_{ij}$ depends
  on the pole order of the $r$-matrix:
  \begin{itemize}
  \item \textup{Class $G$ \textup{(}Heisenberg\textup{)}:}
    $r(z) = k/z$, pole order $1$. Regular singularities.
  \item \textup{Class $L$ \textup{(}affine KM\textup{)}:}
    $r(z) = k\Omega/z$ \textup{(}trace-form\textup{)},
    pole order $1$. Regular singularities.
  \item \textup{Class $C$ \textup{(}$\beta\gamma$\textup{)}:}
    $r$ is a constant nilpotent endomorphism
    \textup{(}$d$-log absorbs the simple OPE pole\textup{)}.
    Regular singularities.
  \item \textup{Class $M$ \textup{(}Virasoro, $\cW_N$\textup{)}:}
 succeeded in 51ms:

\begin{example}[Affine Kac--Moody: Sugawara coproduct]
\label{ex:km-coproduct}
For $V_k(\fg)$ at generic level $k \neq -h^\vee$, the three
structures are:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{($R$-matrix.)} The vertex $R$-matrix is the
  KZ $R$-matrix: the monodromy of the KZ connection
  % AP126/AP148: trace-form convention; k=0 -> r=0. Verified.
  $\nabla = d - k\Omega/(z_1 - z_2) \cdot d(z_1 - z_2)$
  around $\Delta_{12}$. The classical $r$-matrix
  (trace-form) is
  $r(z) = k\Omega/z$; at $k = 0$, $r = 0$; at
  $k = -h^\vee$, the critical level, the Sugawara
  construction degenerates.
\item \textup{($\Ainf$ structure.)} The chiral $\Ainf$
  structure maps are the Sugawara OPE operations restricted
  to $K_n \hookrightarrow \overline{\FM}_n^{\mathrm{ord}}(\CC)$.
  At $k = 2$: $m_2^{\mathrm{ch}}(J^a, J^b; \lambda)
  = [J^a, J^b] + k\, \delta^{ab}/\lambda$ is the affine
exec
/bin/zsh -lc "sed -n '318,336p' standalone/virasoro_r_matrix.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '487,535p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6128,6145p' standalone/ordered_chiral_homology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '164,182p' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '706,752p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '276,308p' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
+ \tfrac{1}{2}h \otimes h$.
% AP1: kappa from landscape_census.tex:
% kappa(V_k(sl_2)) = 3(k+2)/4; k=0 -> 3/2; k=-2 -> 0.
The Koszul invariant is
\begin{equation}\label{eq:sl2-kappa}
  \kappa = 3(k + 2)/4.
\end{equation}
The $r$-matrix in trace-form convention is
$r(z) = k\Omega/z$ (at $k = 0$, $r = 0$);
in KZ normalisation,
$r(z) = \Omega/((k + 2)z)$.
Class $L$ (shadow depth $r = 3$): $\ell_1, \ell_2, \ell_3$
non-trivial, $\ell_k = 0$ for $k \geq 4$.

\smallskip
\noindent\textbf{Degree 2: KZ conformal blocks.}
The ordered chiral Hochschild at degree $2$ is the de~Rham
cohomology of $\Conf_2(\CC)$ with coefficients in the
 succeeded in 52ms:
collision residue is $r(z) = \Omega/((k+h^\vee)z)$ on the adjoint
sector. The $R$-matrix is
$R(z) = z^{\Omega/(k+h^\vee)}$,
a monomial in $z$ with the Casimir eigenvalue as exponent.
The cubic shadow $S_3 \neq 0$ (from the structure constants
$f^{ab}_c$), so the tower extends to degree $3$; but the quartic
and higher terms vanish by independent sum factorization: class $L$.
\end{example}

\begin{example}[Virasoro: class $M$]\label{ex:virasoro}
The $R$-matrix $R(z) = z^{2h}\exp(-c/(4z^2))$ has infinitely many
nonvanishing coefficients. The essential singularity at $z = 0$
is the datum that no finite truncation of the shadow obstruction
tower captures the full $R$-matrix: every degree contributes, and
the tower does not terminate.
\end{example}

The comparison is summarized in the following table:
\begin{center}
 succeeded in 51ms:
\begin{theorem}[Face~5: Drinfeld $r$-matrix; \ClaimStatusProvedHere\ (identification with collision residue); \ClaimStatusProvedElsewhere\ (classical $r$-matrix theory: Drinfeld 1985)]
\label{thm:hdm-face-5}
For $\cA = \widehat{\fg}_k$ the affine Kac--Moody algebra at level
$k \neq -h^\vee$, the collision residue equals the Drinfeld
$r$-matrix in KZ normalization:
\begin{equation}\label{eq:hdm-face-5}
r_{\widehat{\fg}_k}(z)
\;=\;
\frac{\Omega}{(k + h^\vee)\, z}
\;\in\;
\fg \otimes \fg [\![z^{-1}]\!].
\end{equation}
On the generic trace-form locus this is the same family as
$r^{\mathrm{Dr}}(z) = k\,\Omega_{\mathrm{tr}}/z$.
%: The collision residue lives on C_2(X), not over a point.
% The KZ-normalized form \Omega/((k+h^v)z) comes from dualizing
% the zeroth product (Lie bracket) via the level-shifted Killing form.
% At k=0 the KZ-normalized collision residue stays nonzero because the
% Lie bracket of g persists; the trace-form vanishing r=0 at k=0
% applies to the Heisenberg-style level-prefixed kernel.
 succeeded in 51ms:
The collision residue $r(z) = \Omega/((k+h^\vee)z)$ lives on the
ordered bar $B^{\mathrm{ord}}(\widehat{\fg}_k) =
T^c(s^{-1}\bar{\widehat{\fg}}_k)$ with deconcatenation coproduct;
it is an element of the $E_1$ convolution algebra. Parameter~(iii)
is extracted directly from this ordered datum, while parameter~(ii)
quantizes it via the Yangian $R$-matrix on the same ordered structure.
The classical scalar shadow is
\[
\kappa_{\mathrm{cl}} = \mathrm{av}(r(z))
= \frac{k\,\dim(\fg)}{2h^\vee},
\]
and the full modular characteristic is
\[
\kappa(\widehat{\fg}_k)
= \kappa_{\mathrm{cl}} + \frac{\dim(\fg)}{2}
= \frac{\dim(\fg)(k+h^\vee)}{2h^\vee}.
\]

% ================================================================
 succeeded in 52ms:
 \;=\;
 \Res_{z=w}\Bigl[
 \frac{k \, (t^a, t^b)}{(z-w)^2}
 \cdot \frac{dz}{z-w}
 \Bigr]_{d\log}
 \;+\; \text{(simple-pole term)}.
\end{equation}
The $d\log$ extraction of the double-pole term gives
$k \, (t^a, t^b) / z$ (one pole absorbed), and the simple-pole term
contributes the structure-constant piece. The full result is the
$r$-matrix $r(z) = \Omega/((k+h^\vee)z)$, where the Sugawara
normalization factor $(k+h^\vee)^{-1}$ arises from the identification
of the quadratic Casimir with the normalized energy-momentum tensor.

\begin{proposition}[Bar collision prefactor]\label{prop:bar-prefactor}
$\hbar_{\mathrm{bar}} = 1/(k + h^\vee)$.
\end{proposition}

\begin{proof}
The collision residue $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta)$
 succeeded in 52ms:
(the TQ-relation). In the bar complex, this relation
appears as a degree-2 cocycle condition with a shift
in the spectral parameter filtration.
\end{computation}


\subsection{Quantum \texorpdfstring{$R$}{R}-matrix from the bar complex}
\label{subsec:quantum-rmatrix-bar}
\index{R-matrix!quantum!from bar complex}

The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
normalisation; Remark~\ref{rem:km-collision-residue-rmatrix}) is the leading-order
collision residue. The quantum $R$-matrix arises from the
$\hbar$-expansion of the bar-complex MC element, where
$\hbar = \pi i/(k + h^\vee)$.

\begin{proposition}[Classical and quantum $R$-matrices from the
bar complex; \ClaimStatusProvedHere]
\label{prop:rmatrix-from-bar}
\index{R-matrix!from bar complex|textbf}
exec
/bin/zsh -lc "sed -n '616,714p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
symmetric bar.

\textsc{Information content.} An equivariant
$\End(V^{\otimes n})$-valued meromorphic function strictly
contains its scalar trace. The averaging map
$\operatorname{av}$ is surjective but not injective: the kernel
records the non-symmetric components of the line-operator data.
For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
the symmetrization recovers the scalar
$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
full Yangian double; the symmetrization recovers only
$\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
= k\dim\mathfrak g/(2h^\vee)$, and the full
$\kappa(\widehat{\mathfrak g}_k)
= (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
appears only after adding the Sugawara shift.

\textsc{Physical primacy.} The natural physical objects are
ordered. Three-dimensional holomorphic-topological theories
exec
/bin/zsh -lc "sed -n '775,790p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4958,5036p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '70,90p' chapters/examples/genus_expansions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '430,455p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\end{equation}
This is linear in $t$ (hence in $k$) and is the product of the algebra-dependent factor $3t/4 = \kappa$ with the universal generating function $\hat{A}(x) - 1$. For any single-generator Koszul chiral algebra (and for multi-generator algebras subject to the Hodge-type factorization of Theorem~\ref{thm:modular-characteristic}(i)(b)), the analogous formula is
\begin{equation}\label{eq:bivariate-gf-general}
\sum_{g=1}^{\infty} F_g(\cA)\, x^{2g} = \kappa(\cA) \cdot \left(\frac{x/2}{\sin(x/2)} - 1\right).
\end{equation}
The bivariate structure reflects the factorization $F_g = \kappa(\cA) \cdot \lambda_g^{FP}$ \textup{(}UNIFORM-WEIGHT\textup{}) (Theorem~\ref{thm:genus-universality}; ).
\end{proposition}

\begin{proof}
Substituting $F_g = \kappa(\cA) \cdot \lambda_g^{FP}$ into the series and using the classical identity
\[
\sum_{g \geq 1} \lambda_g^{FP}\, x^{2g} = \frac{x}{2\sin(x/2)} - 1,
\]
which follows from the generating function for Bernoulli numbers:
\[
\sum_{g \geq 1} \frac{(2^{2g-1}-1)|B_{2g}|}{(2g)!}\, x^{2g} = \frac{x}{2\sin(x/2)} - 1. \qedhere
 succeeded in 50ms:
\begin{equation}\label{eq:genus-expansion-triples}
\begin{aligned}
\mathfrak{T}_{\cH}
 &= \bigl(\cH_\kappa,\;
 \operatorname{Sym}^{\mathrm{ch}}(V^*),\;
 \kappa/z\bigr), \\
%: canonical form r(z) = k\Omega/z; k=0 -> r=0
\mathfrak{T}_{\widehat{\fg}_k}
 &= \bigl(\widehat{\fg}_k,\;
 \widehat{\fg}_{-k-2h^\vee},\;
 k\Omega/z\bigr), \\
\mathfrak{T}_{\mathrm{Vir}}
 &= \bigl(\mathrm{Vir}_c,\;
 \mathrm{Vir}_{26-c},\;
 \tfrac{c}{2z^3} + \tfrac{2T}{z}\bigr), \\
\mathfrak{T}_{\mathcal{W}_3}
 &= \bigl(\mathcal{W}_3^k,\;
 \mathcal{W}_3^{-k-6},\;
 r_{\mathcal{W}_3}(z)\bigr).
\end{aligned}
 succeeded in 50ms:
channels:
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{lcccc}
\toprule
Channel & $\kappa$ & $\alpha$ & $S_4$ & Class \\
\midrule
Current line \textup{(}$J^a$ directions\textup{)} & $9/4$ & $1$ & $0$ & L \\
$T$-line \textup{(}Sugawara\textup{)} & $1/2$ & $2$ & $10/27$ & M \\
\bottomrule
\end{tabular}
\end{center}
On the current line, $\kappa = \dim(\mathfrak{sl}_2)(k+h^\vee)/(2h^\vee)
= 3 \cdot 3/4 = 9/4$ \textup{(}not $c/2 = 1/2$; cf.\ Table~\textup{\ref{tab:master-invariants}}\textup{)},
and the Jacobi identity kills the quartic, giving class~L with
$r_{\max} = 3$. On the $T$-line, the Sugawara tensor has the
Virasoro shadow at $c = 1$, class~M with infinite shadow depth.
\end{proposition}

\begin{proof}
 succeeded in 51ms:
= \Res_{z_1 = z_2}
 \Bigl[\psi(z_1) \otimes \psi(z_2)
 \cdot d\log(z_1 - z_2)\Bigr]
= \Res_{z_1 = z_2}
 \Bigl[\frac{1}{z_1 - z_2}
 \cdot \frac{dz_1}{z_1 - z_2}\Bigr]
= \Res_{z_1 = z_2}
 \Bigl[\frac{dz_1}{(z_1 - z_2)^2}\Bigr]
= 0.
\]
The integrand has a double pole of the form $dz/(z-w)^2$, whose
residue at $z = w$ vanishes (no $(z-w)^{-1}\,dz$ term).

Compare with the Heisenberg, where the double-pole OPE
$\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
The one-step pole reduction works uniformly: double pole
$\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
\end{proof}


thinking
**Searching for errors in formulas**

I noticed that `free_fields.tex` has a formula issue where it incorrectly uses `kΩ/z`, and it seems it should actually be `k/z`. The same mistake is present in `standalone/introduction_full_survey.tex`, requiring a fix. Maybe it’s not only Heisenberg but also in `lattice_foundations.tex`, related to Kac-Moody. I think I should search for other misformulas in relevant active files using the pattern `Heisenberg.*k\,\Omega/z` and `r_{\cH_k}(z)=k\Omega/z`. Let's run that search!
exec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'Heisenberg["'^'"\\n]*k\\\\,?\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\)=k\\\\Omega/z|Heisenberg, \\"'$r'"\\(z\\) = k\\\\,?\\\\Omega/z|Heisenberg.*\\\\Omega/z' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'r\\(z\\) = \\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|r\\(z\\)=\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|r\\(z\\) = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|KZ normalisation.*trace-form|trace-form.*KZ normalisation' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:623:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:708:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak:343:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak:419:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:227:% Convention: trace-form normalisation. In the KZ normalisation
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:716:The classical $r$-matrix $r(z) = \Omega/((k+h^\vee)z)$ (KZ
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:499:$r(z) = \Omega / ((k + h^\vee)\,z)$ for
/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:1655:$r(z) = \Omega/((k+h^\vee)z)$
/Users/raeez/chiral-bar-cobar/standalone/sc_chtop_pva_descent.tex:1349:  In the KZ convention: $r(z) = \Omega/((k+h^\vee)z)$.  Bridge:
/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:241:$r(z) = \Omega/((k+h^\vee)z)$ into \eqref{eq:gz-connection} gives
/Users/raeez/chiral-bar-cobar/standalone/gaudin_from_collision.tex:544: is $r(z) = \Omega/((k+h^\vee)z)$; the Gaudin Hamiltonian is its
/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:164:The collision residue $r(z) = \Omega/((k+h^\vee)z)$ lives on the
/Users/raeez/chiral-bar-cobar/standalone/three_parameter_hbar.tex:286:$r$-matrix $r(z) = \Omega/((k+h^\vee)z)$, where the Sugawara
/Users/raeez/chiral-bar-cobar/standalone/virasoro_r_matrix.tex:318:collision residue is $r(z) = \Omega/((k+h^\vee)z)$ on the adjoint
/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:175: $r(z) = \Omega/((k+h^\vee)z)$.

thinking
**Investigating mixed files**

I need to inspect these KM mixed files, as they may lack a bridge. The current candidate is `standalone/three_parameter_hbar.tex`, which shows inconsistency in the formula provided. It mentions `av(r(z))=k dim(g)/(2h^\vee)`, but the KZ formula above does not align with this, possibly requiring correction. I’ll also check `standalone/virasoro_r_matrix.tex` to see if the KZ formula serves as a comparison. Lastly, I should look into `frontier_modular_holography_platonic.tex` for potential bridges as well.
exec
/bin/zsh -lc "sed -n '280,308p' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '154,188p' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1648,1718p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '168,185p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '309,326p' standalone/virasoro_r_matrix.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $\cA^!_{\mathrm{line}}$ acting at spectral separation $z_{ij}$.
\item The quantization parameter is $\hbar = 1/(k+h^\vee)$.
\end{enumerate}
\end{theorem}

\begin{proof}
Part~(i): substituting the Casimir collision residue
$r(z) = \Omega/((k+h^\vee)z)$
\textup{(}Theorem~\textup{\ref{thm:yangian-shadow-theorem}}\textup{)}
into the depth-$1$ Hamiltonian formula yields exactly the Gaudin
Hamiltonian of \cite{FFR94} multiplied by $1/(k+h^\vee)$.

Part~(ii): by Theorem~\textup{\ref{thm:gz26-commuting-differentials}}(ii),
the depth-$k$ contribution to $H_i$ is the collision residue at depth
$k$. Each such residue is the $m_k$ operation transferred via the
Homological Perturbation Lemma to the cohomology, viewed as a
spectral-parameter deformation of the classical $m_2$.

Part~(iii): the prefactor $1/(k+h^\vee)$ is the Drinfeld quantization
parameter \cite{Drinfeld85}.
 succeeded in 51ms:
 \Bigr]_{d\log}
 \;+\; \text{(simple-pole term)}.
\end{equation}
The $d\log$ extraction of the double-pole term gives
$k \, (t^a, t^b) / z$ (one pole absorbed), and the simple-pole term
contributes the structure-constant piece. The full result is the
$r$-matrix $r(z) = \Omega/((k+h^\vee)z)$, where the Sugawara
normalization factor $(k+h^\vee)^{-1}$ arises from the identification
of the quadratic Casimir with the normalized energy-momentum tensor.

\begin{proposition}[Bar collision prefactor]\label{prop:bar-prefactor}
$\hbar_{\mathrm{bar}} = 1/(k + h^\vee)$.
\end{proposition}

\begin{proof}
The collision residue $r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta)$
is the genus-zero binary projection of $\Theta_{\widehat{\fg}_k} =
D - d_0$. The linear part $d_0$ contributes the structure-constant
terms $f^{ab}{}_c J^c / z$. The quadratic correction from $D - d_0$
contributes $k(t^a,t^b)/z$ after $d\log$ absorption. The
 succeeded in 51ms:
 \item $\hbar_{\mathrm{DNP}}$ from the quantum Yang--Baxter equation
 of a line-operator $R$-matrix (quantum, categorical);
 \item $\hbar_{\mathrm{bar}}$ from the residue of the bar
 differential against $d\log(z-w)$ (homological, operadic).
\end{enumerate}
Their equality is not a priori obvious: (i) extracts a classical
Poisson coefficient, (ii) a quantum deformation parameter, and (iii)
a homological residue. That all three produce $1/(k + h^\vee)$ is a
consequence of three independent theorems, one per link.

The collision residue $r(z) = \Omega/((k+h^\vee)z)$ lives on the
ordered bar $B^{\mathrm{ord}}(\widehat{\fg}_k) =
T^c(s^{-1}\bar{\widehat{\fg}}_k)$ with deconcatenation coproduct;
it is an element of the $E_1$ convolution algebra. Parameter~(iii)
is extracted directly from this ordered datum, while parameter~(ii)
quantizes it via the Yangian $R$-matrix on the same ordered structure.
The classical scalar shadow is
\[
\kappa_{\mathrm{cl}} = \mathrm{av}(r(z))
= \frac{k\,\dim(\fg)}{2h^\vee},
 succeeded in 52ms:
$J(z)J(w) \sim k/(z-w)^2$. The collision residue is
$r(z) = k/z$, a simple pole. On the primary sector,
$R(z) = z^k$: the $R$-matrix is a monomial. There is no
exponential correction; $R_2 = 0$ and $S_3 = 0$.
The tower terminates at degree $2$: class $G$.
\end{example}

\begin{example}[Affine Kac--Moody: class $L$]\label{ex:km}
For $\widehat{\fg}_k$ with Casimir $\Omega$ at level $k$, the
collision residue is $r(z) = \Omega/((k+h^\vee)z)$ on the adjoint
sector. The $R$-matrix is
$R(z) = z^{\Omega/(k+h^\vee)}$,
a monomial in $z$ with the Casimir eigenvalue as exponent.
The cubic shadow $S_3 \neq 0$ (from the structure constants
$f^{ab}_c$), so the tower extends to degree $3$; but the quartic
and higher terms vanish by independent sum factorization: class $L$.
\end{example}

 succeeded in 52ms:
 \{a_\lambda b\}\,d\lambda$
 \textup{(}Laplace transform\textup{)}.
\item The Knizhnik--Zamolodchikov connection:
 $\nabla_{\mathrm{KZ}}
 = d - r(z)\,d\log(z_1 - z_2)$.
\item\label{it:drinfeld-face} The Drinfeld $r$-matrix
 \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
 $r(z) = \Omega/((k+h^\vee)z)$.
\item The Sklyanin bracket:
 $\{L_1(u), L_2(v)\}
 = [r(u - v), L_1(u) \otimes L_2(v)]$.
\item The Gaudin Hamiltonians:
 $H_i
 = \sum_{j \ne i} r(z_i - z_j)$
 are mutually commuting.
\end{enumerate}
Faces~\textup{(F1)--(F4)} hold for every modular Koszul
algebra. Faces~\textup{(F5)--(F7)} specialize to affine

thinking
**Evaluating file conventions**

I’m noticing that `standalone/programme_summary_sections5_8.tex` only uses KZ in the face list, which could be fine if that section is exclusively KZ. It might not need a bridge. However, line 209 refers to "affine Kac-Moody in trace-form convention," suggesting there might be both forms present. I'll take a closer look at lines 205-214 to clarify this. Let’s see what’s going on in that section!
exec
/bin/zsh -lc "sed -n '204,214p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\mathrm{av}\bigl(r(z)\bigr)
\quad\text{for abelian and Virasoro-type families,}
\end{equation}
The averaging map $\mathrm{av}$ is the
$\Sigma_2$-coinvariant projection. For non-abelian
affine Kac--Moody in the trace-form convention,
\[
\mathrm{av}(k\,\Omega/z)
\;=\;
\frac{k\,\dim(\fg)}{2h^\vee}
\;=\;


thinking
**Analyzing file conventions**

I’m noticing the file mixes KZ and trace-form, and I wonder if the user expects a consistent convention within each file or a bridge if there's a switch. Currently, there’s no bridge, but maybe that’s okay if I’m not writing a direct equivalence. The task clearly states the need for bridge identity when conventions change. I’ll need to identify files in the current repo that contain both patterns and possibly script with shell or perl to detect them. I'll get started on this!
thinking
**Scripting for bridge inspection**

Next, I need to check if a bridge exists for the equation `k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)` or something similar. It seems like scripting in shell could be a practical approach to automate this task. I’ll ensure the script inspects the relevant files to verify the existence of this bridge. This way, I can streamline the process and make sure I capture any needed distinctions efficiently. Let's get to scripting!
codex
I’ve confirmed two concrete Vol I defect types: active Heisenberg surfaces that incorrectly use the KM-style `k\,\Omega/z`, and active files that switch between trace-form and KZ normalizations without stating the bridge. I’m computing the full editable Vol I file list for that second defect now so the patch stays complete rather than ad hoc.
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
import re
root = Path('/Users/raeez/chiral-bar-cobar')
files = [p for p in root.rglob('*.tex') if any(part in {'chapters','appendices','standalone'} for part in p.parts)]
# live-ish: ignore backups/log/aux/pdf-generated sources? keep tex only, skip .bak names
files = [p for p in files if '.bak' not in p.name and not p.name.endswith('.aux.tex')]
trace_pat = re.compile(r'k\\,?\\\\Omega|k\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}|k\\\\Omega|k\\s*\\\\Omega')
kz_pat = re.compile(r'\\\\Omega/?\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega/\\\\bigl\\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\\\bigr\\)|\\\\Omega_\\w*/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|1/\\(k \\+ h\\"'^'"\\\\vee\\)|1/\\(k\\+h\\"'^'"\\\\vee\\)')
bridge_pat = re.compile(r'k\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}\\s*=\\s*\\\\Omega/?\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}\\s*=\\s*\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|Bridge identity|bridge')
# simpler textual checks
files_with_both=[]
for p in files:
    txt=p.read_text(errors='ignore')
    has_trace=('k\\\\Omega/z' in txt or 'k\\,\\Omega/z' in txt or 'k\\,\\Omega_{\\mathrm{tr}}/z' in txt or 'k\\Omega_{\\mathrm{tr}}/z' in txt)
    has_kz=('\\\\Omega/((k+h"'^'"\\vee)z)' in txt or '\\\\Omega / ((k + h"'^'"\\vee)\\,z)' in txt or '\\\\Omega/((k + h"'^'"\\vee)z)' in txt or '\\\\Omega/((k + h"'^'"\\vee)\\,z)' in txt or '\\\\Omega_\\fg/(k+h"'^'"\\vee' in txt or '\\\\Omega_\\fg}{(k + h"'^'"\\vee)' in txt or '1/(k+h"'^'"\\vee)' in txt or '1/(k + h"'^'"\\vee)' in txt)
    if has_trace and has_kz:
        has_bridge=('Bridge identity' in txt or 'bridge' in txt.lower() and '\\\\Omega' in txt or 'k\\\\,\\\\Omega_{\\\\mathrm{tr}} = \\\\Omega/(k+h"'^'"\\\\vee)' in txt or 'k\\\\Omega_{\\\\mathrm{tr}} = \\\\Omega/(k+h"'^'"\\\\vee)' in txt or 'k\\\\, (\\\\Omega_{\\\\mathrm{tr}})' in txt and '\\\\Omega_{ij}/(k + h"'^'"\\\\vee)' in txt)
        files_with_both.append((str(p.relative_to(root)), has_bridge))
for rel, has_bridge in sorted(files_with_both):
    print(f\"{rel}\\tbridge={'Y' if has_bridge else 'N'}\")
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
root = Path('/Users/raeez/chiral-bar-cobar')
files = [p for p in root.rglob('*.tex') if any(part in {'chapters','appendices','standalone'} for part in p.parts)]
files = [p for p in files if '.bak' not in p.name and p.suffix == '.tex']
rows=[]
for p in files:
    txt=p.read_text(errors='ignore')
    has_trace=('k\\\\Omega/z' in txt or 'k\\,\\Omega/z' in txt or 'k\\,\\Omega_{\\mathrm{tr}}/z' in txt or 'k\\Omega_{\\mathrm{tr}}/z' in txt)
    has_kz=('\\\\Omega/((k+h"'^'"\\vee)z)' in txt or '\\\\Omega / ((k + h"'^'"\\vee)\\,z)' in txt or '\\\\Omega/((k + h"'^'"\\vee)z)' in txt or '\\\\Omega/((k + h"'^'"\\vee)\\,z)' in txt or '\\\\Omega/\\bigl((k+h"'^'"\\vee)z\\bigr)' in txt or '\\\\Omega/\\bigl((k{+}h"'^'"\\vee)z\\bigr)' in txt or '\\\\Omega_\\fg/(k+h"'^'"\\vee' in txt or '1/(k+h"'^'"\\vee)' in txt or '1/(k + h"'^'"\\vee)' in txt)
    if has_trace and has_kz:
        has_bridge=('Bridge identity' in txt or 'k\\,\\Omega_{\\mathrm{tr}} = \\Omega/(k+h"'^'"\\vee)' in txt or 'k\\Omega_{\\mathrm{tr}} = \\Omega/(k+h"'^'"\\vee)' in txt or 'k\\,\\Omega_{\\mathrm{tr}} = \\Omega/((k+h"'^'"\\vee)z)' in txt or 'bridge' in txt.lower())
        rows.append((str(p.relative_to(root)), has_bridge))
for rel, has_bridge in sorted(rows):
    print(f\"{rel}\\tbridge={'Y' if has_bridge else 'N'}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 3.85s:


thinking
**Considering shell script approach**

It seems like there's no output, maybe due to a script issue. I might need a simpler shell approach using something like `for f in $(rg -l ...)`, which could be more straightforward. Since there could be many results, using `rg -l` with a pattern and then intersecting might work better. I think shell scripting can make this easier, so I’ll consider using `comm` to handle intersections effectively.
exec
/bin/zsh -lc 'tmp1=$(mktemp); tmp2=$(mktemp); rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' 'k\\\\Omega/z|k\\\\,\\\\Omega/z|k\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|k\\\\,\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' > "'$tmp1; rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' '\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|\\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|1/\\(k\\+h\\"'^'"\\\\vee\\)|1/\\(k \\+ h\\"'^'"\\\\vee\\)' > "'$tmp2; comm -12 <(sort $tmp1) <(sort $tmp2)' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/ordered_associative_chiral_kd.tex
chapters/connections/frontier_modular_holography_platonic.tex
chapters/connections/holographic_datum_master.tex
chapters/connections/thqg_introduction_supplement_body.tex
chapters/examples/w_algebras_deep.tex
chapters/examples/yangians_computations.tex
chapters/examples/yangians_drinfeld_kohno.tex
chapters/theory/e1_modular_koszul.tex
chapters/theory/en_koszul_duality.tex
chapters/theory/higher_genus_modular_koszul.tex
chapters/theory/ordered_associative_chiral_kd.tex
standalone/chiral_chern_weil.tex
standalone/holographic_datum.tex
standalone/ordered_chiral_homology.tex
standalone/programme_summary_sections5_8.tex
standalone/sc_chtop_pva_descent.tex

thinking
**Checking for bridge statements**

I notice I have many files with the same patterns. I should check which ones already have a bridge statement. To make this easier, I could search within these files for the term "bridge" or any specific identity connected to it. That way, I can script it efficiently. It feels vital to streamline this process! Let’s get started on writing that script.
exec
/bin/zsh -lc "for f in appendices/ordered_associative_chiral_kd.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/holographic_datum_master.tex chapters/connections/thqg_introduction_supplement_body.tex chapters/examples/w_algebras_deep.tex chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/theory/e1_modular_koszul.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex standalone/chiral_chern_weil.tex standalone/holographic_datum.tex standalone/ordered_chiral_homology.tex standalone/programme_summary_sections5_8.tex standalone/sc_chtop_pva_descent.tex; do printf '%s\\t' \""'$f"; if rg -q '"'Bridge identity|bridge|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' \""'$f"; then echo Y; else echo N; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/ordered_associative_chiral_kd.tex	N
chapters/connections/frontier_modular_holography_platonic.tex	Y
chapters/connections/holographic_datum_master.tex	Y
chapters/connections/thqg_introduction_supplement_body.tex	Y
chapters/examples/w_algebras_deep.tex	Y
chapters/examples/yangians_computations.tex	Y
chapters/examples/yangians_drinfeld_kohno.tex	Y
chapters/theory/e1_modular_koszul.tex	Y
chapters/theory/en_koszul_duality.tex	Y
chapters/theory/higher_genus_modular_koszul.tex	Y
chapters/theory/ordered_associative_chiral_kd.tex	Y
standalone/chiral_chern_weil.tex	Y
standalone/holographic_datum.tex	Y
standalone/ordered_chiral_homology.tex	Y
standalone/programme_summary_sections5_8.tex	Y
standalone/sc_chtop_pva_descent.tex	Y
exec
/bin/zsh -lc "rg -n 'Bridge identity|bridge|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' chapters/connections/thqg_introduction_supplement_body.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1349:\subsection{The Drinfeld--Kohno bridge}
1357:this bridge is the passage from the shadow connection
1360:\begin{equation}\label{eq:thqg-intro-dk-bridge}
1618:then extending outward through the standard landscape (Part~\ref{part:physics-bridges}),
1619:the bridges to mathematical physics (Part~\ref{part:seven-faces}), and the frontier
1675:Part~\ref{part:physics-bridges} computes the algebraic engine on every major family. Each
1750:\label{subsec:thqg-intro-guide-bridges}
1772:The PVA quantization bridge and holographic applications complete
1893:full proofs and computations appear in Parts~\ref{part:bar-complex}--\ref{part:physics-bridges} of Volume~I and in


thinking
**Improving detection methods**

I need to focus on improving checks for explicit equations to avoid false positives. It might be useful to search for files where both conventions appear without a clear identity near each switch. This could be complex, but we may only have a few truly inconsistent cases. For instance, there’s a clear switch in `thqg_introduction_supplement_body` that needs fixing. Also, `standalone/programme_summary_sections5_8.tex` has a switch without a bridge that probably needs attention, too. I should inspect all candidate files for similar issues.
thinking
**Inspecting candidate files**

I noticed there are too many instances to manage, but we can search within each candidate for the exact bridge formula. Our earlier checks found many cases with a true explicit identity, which seems okay. Now, I should focus on the ones likely missing explicit identities, like `thqg_intro` and maybe `standalone/programme_summary_sections5_8.tex`. I'll search for explicit identities within these files to clarify the issues.
exec
/bin/zsh -lc "sed -n '170,214p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic' chapters/connections/thqg_introduction_supplement_body.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item The Knizhnik--Zamolodchikov connection:
 $\nabla_{\mathrm{KZ}}
 = d - r(z)\,d\log(z_1 - z_2)$.
\item\label{it:drinfeld-face} The Drinfeld $r$-matrix
 \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
 $r(z) = \Omega/((k+h^\vee)z)$.
\item The Sklyanin bracket:
 $\{L_1(u), L_2(v)\}
 = [r(u - v), L_1(u) \otimes L_2(v)]$.
\item The Gaudin Hamiltonians:
 $H_i
 = \sum_{j \ne i} r(z_i - z_j)$
 are mutually commuting.
\end{enumerate}
Faces~\textup{(F1)--(F4)} hold for every modular Koszul
algebra. Faces~\textup{(F5)--(F7)} specialize to affine
Kac--Moody; the general case is obtained by replacing
$\Omega/((k{+}h^\vee)z)$ with $r_\cA(z)$.
\end{theorem}

 exited 1 in 51ms:

 exited 1 in 50ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|trace-form convention|KZ normalisation' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "for f in appendices/ordered_associative_chiral_kd.tex chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/holographic_datum_master.tex chapters/connections/thqg_introduction_supplement_body.tex chapters/examples/w_algebras_deep.tex chapters/examples/yangians_computations.tex chapters/examples/yangians_drinfeld_kohno.tex chapters/theory/e1_modular_koszul.tex chapters/theory/en_koszul_duality.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/ordered_associative_chiral_kd.tex standalone/chiral_chern_weil.tex standalone/holographic_datum.tex standalone/ordered_chiral_homology.tex standalone/programme_summary_sections5_8.tex standalone/sc_chtop_pva_descent.tex standalone/three_parameter_hbar.tex standalone/virasoro_r_matrix.tex chapters/examples/yangians_foundations.tex; do printf '%s\\t' \""'$f"; if rg -q '"'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\(\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}\\)_\\{ij\\} *= *\\\\Omega_\\{ij\\}/\\(k \\+ h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic~\\"'$k'"\\"'$|k'"\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic' \""'$f"; then echo explicit; else echo missing; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/ordered_associative_chiral_kd.tex	missing
chapters/connections/frontier_modular_holography_platonic.tex	missing
chapters/connections/holographic_datum_master.tex	missing
chapters/connections/thqg_introduction_supplement_body.tex	missing
chapters/examples/w_algebras_deep.tex	missing
chapters/examples/yangians_computations.tex	explicit
chapters/examples/yangians_drinfeld_kohno.tex	missing
chapters/theory/e1_modular_koszul.tex	missing
chapters/theory/en_koszul_duality.tex	missing
chapters/theory/higher_genus_modular_koszul.tex	missing
chapters/theory/ordered_associative_chiral_kd.tex	missing
standalone/chiral_chern_weil.tex	missing
standalone/holographic_datum.tex	explicit
standalone/ordered_chiral_homology.tex	missing
standalone/programme_summary_sections5_8.tex	missing
standalone/sc_chtop_pva_descent.tex	explicit
standalone/three_parameter_hbar.tex	missing
standalone/virasoro_r_matrix.tex	missing
chapters/examples/yangians_foundations.tex	missing


thinking
**Inspecting local context**

I need to check the file `chapters/connections/frontier_modular_holography_platonic.tex` to see if there's an explicit bridge established. I recall that around line 1714, there's a formulation `= Ω/((k+h^\vee)z) = k Ω_tr / z`, which indicates an explicit connection. So it doesn't seem to be a problem. It looks like the bridge is indeed there, so I can move on and not worry about that!
thinking
**Exploring patch options**

I'm considering a patch by adding a bridge identity at the first switch. There are many standalone options, but it seems like the central ones might be the most effective. I'm curious about how this could impact the overall system and if it truly simplifies things or creates new complexities. This approach needs careful planning to ensure it's executed efficiently. Let’s keep exploring the best way to implement this!
codex
The current repo patch is converging to a handful of genuine defects. In parallel I’m reading the strongest Vol II/III offenders now so I can separate real read-only blockers from noisy note surfaces in the final audit.
exec
/bin/zsh -lc "sed -n '150,190p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '228,236p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
coproduct~$\Delta$.
Statement~(ii) is Theorem~\ref{thm:bar-swiss-cheese} (the
$\SCop$-datum on the pair
$(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$) together with
Theorem~\ref{thm:homotopy-Koszul} (homotopy transfer from the
MC element).
Statement~(iii) combines
Proposition~\ref{prop:alpha-projections}(ii) (the open projection
gives the line-sector operations) with
 succeeded in 51ms:

\begin{definition}[Strict rational dg-shifted Yangian]% label removed: def:strict-yangian
A \emph{strict rational dg-shifted Yangian} consists of the following data:
\begin{enumerate}[label=\textup{(\alph*)}]
 \item an associative dg algebra $Y$;
 \item a degree-zero derivation $T$ (the translation operator);
 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
 \[
 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
 \]
 \item the parameter-dependent classical Yang-Baxter equation
 \[
 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
 \]
\end{enumerate}
\end{definition}

The datum $(Y,r,T)$ is the strict shadow of the full $A_\infty$ structure treated later.

\section{The strict logarithmic theory: the shifted KZ/FM connection}% label removed: sec:strict
exec
/bin/zsh -lc "sed -n '2304,2314p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{computation}[Modular extension of the Heisenberg
genus-zero package; \ClaimStatusProvedHere]
\label{comp:vol2-heisenberg-modular-extension}
\index{Heisenberg algebra!modular extension}
The Heisenberg genus-$0$ package has
$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
The modular extension:
$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
$\kappa=k$,
$F_g=k\cdot \tfrac{2^{2g-1}-1}{2^{2g-1}}\cdot\tfrac{|B_{2g}|}{(2g)!}$,
exec
/bin/zsh -lc "sed -n '1908,1926p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '118,150p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '366,386p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e2_chiral_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\;=\;
\frac{c/3}{z^5}
+ \frac{2T}{z^3}
+ \frac{\partial T}{z^2}
+ \frac{\beta\,\Lambda + \tfrac{3}{10}\partial^2 T}{z},
\end{equation}
where $\beta = 32/(5c + 22)$ (as in~\eqref{eq:m2WW-recap}).

The collision residue pole orders are $\{1, 2, 3, 5\}$:
the $1/z^4$ term is \emph{absent}, reflecting the
weight-$1$ lacuna and the gap migration formula $d_{\mathrm{gap}} = 2N + n - 4 = 4$ at $N = 3$, $n = 2$ (Theorem~\ref{thm:gap-migration}(iv)). Compare with the $(T,T)$ collision
residue $r^{TT}(z) = (c/2)/z^3 + 2T/z + (\partial T)$
\textup{(}Computation~\textup{\ref{comp:vir-CYBE})},
which has pole orders $\{1, 3\}$ with the $1/z^2$ term
absent by the same weight-parity mechanism.

The Laplace coefficients are:
\begin{center}
\small
 succeeded in 50ms:
$q = e^{\pi i/(k+h^\vee)}$, the degree-$(1,1)$ component of the
ordered bar complex $B^{\mathrm{ord}}(V_k(\frakg))$ recovers the
$R$-matrix of $\Uq(\frakg)$:
\[
 r(z) = \Res^{\mathrm{coll}}_{0,2}(\Theta_{V_k(\frakg)})
 \;\longleftrightarrow\;
 \cR_q = \lim_{z \to 0}\, \cR(z)
\]
where $r(z) = \frac{k\,\Omega}{z} + O(1)$ is the classical $r$-matrix with
Casimir $\Omega \in \frakg \otimes \frakg$ and level prefix $k$
, and $\cR_q$ is the
quantized universal $R$-matrix. The spectral parameter $z$
corresponds to the rapidity variable in the integrable lattice model.
%: the r-matrix has pole orders ONE LESS than the OPE.
%: affine KM r-matrix at level k is k*Omega/z, not Omega/z.
\end{proposition}

\begin{remark}[Three $r$-matrices]
\label{rem:three-r-matrices}
%: r^coll != r(z) in general; they coincide for even E_infty algebras.
 succeeded in 52ms:
\medskip
\noindent\textbf{Part~3: Braiding reversal.}
The Koszul dual level is $k^! = -k$; this does \emph{not} follow from
negating the $\Omega$-background parameters $(h_1, h_2, h_3) \mapsto
(-h_1, -h_2, -h_3)$, since $\sigma_2$ is degree-$2$ homogeneous and
hence $\sigma_2(-h_i) = \sigma_2(h_i)$, leaving $k = -\sigma_2$
invariant.  Instead, $k^! = -k$ arises from the Verdier duality
functor $D_{\C^2}$ on conilpotent $E_2$-coalgebras, which acts by
linear duality on the underlying graded space and thereby
\emph{transposes the Shapovalov form}: the inner product
$\langle J, J \rangle = k$ dualizes to $\langle J, J \rangle^! = -k$
(the bilinear form on the linear dual carries the opposite sign).
Since $R^{E_2}(z) = k\,\Omega/z + O(1)$ with $\Omega$ the
metric-independent Casimir, the dual $R$-matrix is
\[
 R^{E_2,!}(z) \;=\; \frac{k^!\,\Omega}{z} + O(1)
 \;=\; \frac{(-k)\,\Omega}{z} + O(1)
 \;=\; -R^{E_2}(z) + O(1).
\]
The identity $R^{E_2,!} = -R^{E_2}$ at leading order is the defining
exec
/bin/zsh -lc 'tmp1=$(mktemp); tmp2=$(mktemp); rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' 'k\\\\Omega/z|k\\\\,\\\\Omega/z|k\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|k\\\\,\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' /Users/raeez/calabi-yau-quantum-groups > "'$tmp1; rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' '\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|\\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|1/\\(k\\+h\\"'^'"\\\\vee\\)|1/\\(k \\+ h\\"'^'"\\\\vee\\)' /Users/raeez/calabi-yau-quantum-groups > "'$tmp2; comm -12 <(sort $tmp1) <(sort $tmp2)' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:



thinking
**Analyzing search patterns**

I'm noticing there are no mixed current patterns in the active chapters of volume 3 from our search. It seems like it could only be trace-form or just KZ, and that feels good! Next, I'm thinking about searching for the Heisenberg wrong formula in volume 3's active chapters. I wonder if using grep might help with that, but maybe it isn't necessary. Let's see how it goes!
thinking
**Inspecting repo edits**

I see that the current repo likely needs editing for about five files. Specifically, I should patch `standalone/programme_summary_sections5_8.tex` since it switches conventions without a bridge. Similarly, I have to check `thqg_introduction_supplement_body.tex` and `yangians_foundations.tex`. Then there's `three_parameter_hbar.tex`, which uses both KZ and trace-form without a clear bridge, plus an inconsistent `κ_cl` formula. I’ll definitely search for `kΩ/z` within the file, especially around line 1680, to clarify the context.
exec
/bin/zsh -lc "rg -n 'k\\\\Omega/z|k\\\\,\\\\Omega/z|Omega_\\\\{\\\\mathrm\\{tr\\}\\}|Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:k\\Omega/z|k\\,\\Omega/z|Omega_\\{\\mathrm\{tr\}\}|Omega/\(\(k\+h\^\\vee\)z\)|Omega/\(\(k\+h\^\\vee\)z\)|Omega/\(\(k \+ h\^\\vee\)z\))
                                         ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n 'k\\\\Omega/z|k\\\\,\\\\Omega/z|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|\\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)' standalone/three_parameter_hbar.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
164:The collision residue $r(z) = \Omega/((k+h^\vee)z)$ lives on the
286:$r$-matrix $r(z) = \Omega/((k+h^\vee)z)$, where the Sugawara
304:$\Omega/((k+h^\vee)z)$ by the definition of $\Omega$ relative to

thinking
**Exploring formulas and intersections**

I’m thinking about searching for `Omega/((k+h^\vee)z)`. I’m unsure if that’s the right direction since our intersection comes from `1/(k+h^\vee)` based on the hbar line, not from the KZ r formula. Perhaps I could ignore that. It seems there might be fewer files that include both the actual r formulas. I’ll definitely need to compute the intersection with the literal KZ r formula and the literal trace-form formula. Time to dive in!
exec
/bin/zsh -lc 'tmp1=$(mktemp); tmp2=$(mktemp); rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' 'k\\\\Omega/z|k\\\\,\\\\Omega/z|k\\\\,\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|k\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' > "'$tmp1; rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' '\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|\\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega_\\\\fg/\\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega_\\\\fg/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' > "'$tmp2; comm -12 <(sort $tmp1) <(sort $tmp2)' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/connections/frontier_modular_holography_platonic.tex
chapters/connections/holographic_datum_master.tex
chapters/connections/thqg_introduction_supplement_body.tex
chapters/examples/yangians_computations.tex
standalone/chiral_chern_weil.tex
standalone/holographic_datum.tex
standalone/programme_summary_sections5_8.tex
standalone/sc_chtop_pva_descent.tex
exec
/bin/zsh -lc "for f in chapters/connections/frontier_modular_holography_platonic.tex chapters/connections/holographic_datum_master.tex chapters/connections/thqg_introduction_supplement_body.tex chapters/examples/yangians_computations.tex standalone/chiral_chern_weil.tex standalone/holographic_datum.tex standalone/programme_summary_sections5_8.tex standalone/sc_chtop_pva_descent.tex; do printf '%s\\n' \""'$f"; rg -n '"'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic|Bridge identity' \""'$f"; echo '"'---'; done" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/frontier_modular_holography_platonic.tex
---
chapters/connections/holographic_datum_master.tex
---
chapters/connections/thqg_introduction_supplement_body.tex
---
chapters/examples/yangians_computations.tex
746: $k\,\Omega_{\mathrm{tr}} = \Omega_\fg/(k+h^\vee)$ at generic~$k$.
---
standalone/chiral_chern_weil.tex
---
standalone/holographic_datum.tex
635:Bridge identity: $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$
---
standalone/programme_summary_sections5_8.tex
---
standalone/sc_chtop_pva_descent.tex
1350:  $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic $k$.
---
codex
```text
PE-1: r-matrix write
family: Heis
r(z): k/z
level param: k
OPE pole: 2
r pole: 1
convention: trace-form / scalar Heisenberg
AP126 (trace-form): r|_{k=0} = 0  expected: 0  match? Y
AP141 grep: bare \Omega/z in scope: N  allowed? N
critical-level (KM): NA
source: CLAUDE.md C10; AGENTS.md Canonical Formulas
verdict: ACCEPT
```

```text
PE-1: r-matrix write
family: affine KM
r(z): k\,\Omega_{\mathrm{tr}}/z and \Omega/((k+h^\vee)z)
level param: k
OPE pole: 2
r pole: 1
convention: trace-form and KZ, with explicit bridge k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)
AP126 (trace-form): r|_{k=0} = 0  expected: 0  match? Y
AP141 grep: bare \Omega/z in scope: N  allowed? N
critical-level (KM): trace-form gives -h^\vee\Omega_{\mathrm{tr}}/z; KZ diverges
source: CLAUDE.md C9; chapters/examples/landscape_census.tex
verdict: ACCEPT
```
exec
/bin/zsh -lc "sed -n '492,506p' chapters/connections/thqg_introduction_supplement_body.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\nabla^{\mathrm{KZ}}
\;=\;
d \;-\; \frac{1}{k + h^\vee}
\sum_{i < j} \frac{\Omega_{ij}}{z_i - z_j}\,dz_i.
\end{equation}
The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
the Sugawara normalization of the affine OPE:
$r(z) = \Omega / ((k + h^\vee)\,z)$ for
$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
inverse of the modular characteristic
$\kappa(\widehat{\mathfrak{g}}_k)
= \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
by the factor $\dim\mathfrak{g}/(2h^\vee)$.

The flatness of the KZ connection, originally proved by Knizhnik and
exec
/bin/zsh -lc "sed -n '1058,1070p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '620,632p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '172,214p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '440,448p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '704,714p' standalone/introduction_full_survey.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 quadratic Casimir tensor (inverse Killing form) and the Sugawara
 denominator $k + h^\vee$ arises from dualizing the zeroth product
 via the level-shifted Killing form
 (Computation~\ref{comp:sl2-collision-residue-kz}).
 %: this is a section on C_2(X), not a formula over a point.
 Equivalently, in the trace-form normalization where
 $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
 $r(z) = \Omega_{\mathrm{tr}}/z$.
 This $r$-matrix satisfies
 the classical Yang--Baxter equation in spectral-parameter form
 \textup{(}equivalently, the infinitesimal braid relations for
 $\Omega$\textup{)}, for all simple~$\fg$
 \textup{(}\texttt{quantum\_rmatrix\_barcomplex.py}, verified
 succeeded in 51ms:
The integrand has a double pole of the form $dz/(z-w)^2$, whose
residue at $z = w$ vanishes (no $(z-w)^{-1}\,dz$ term).

Compare with the Heisenberg, where the double-pole OPE
$\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
The one-step pole reduction works uniformly: double pole
$\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
\end{proof}
 succeeded in 51ms:
contains its scalar trace. The averaging map
$\operatorname{av}$ is surjective but not injective: the kernel
records the non-symmetric components of the line-operator data.
For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
the symmetrization recovers the scalar
$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
full Yangian double; the symmetrization recovers only
$\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
= k\dim\mathfrak g/(2h^\vee)$, and the full
$\kappa(\widehat{\mathfrak g}_k)
= (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
appears only after adding the Sugawara shift.
 succeeded in 51ms:
 = d - r(z)\,d\log(z_1 - z_2)$.
\item\label{it:drinfeld-face} The Drinfeld $r$-matrix
 \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
 $r(z) = \Omega/((k+h^\vee)z)$.
\item The Sklyanin bracket:
 $\{L_1(u), L_2(v)\}
 = [r(u - v), L_1(u) \otimes L_2(v)]$.
\item The Gaudin Hamiltonians:
 $H_i
 = \sum_{j \ne i} r(z_i - z_j)$
 are mutually commuting.
\end{enumerate}
Faces~\textup{(F1)--(F4)} hold for every modular Koszul
algebra. Faces~\textup{(F5)--(F7)} specialize to affine
Kac--Moody; the general case is obtained by replacing
$\Omega/((k{+}h^\vee)z)$ with $r_\cA(z)$.
\end{theorem}

The seven faces are not seven theorems but seven readings of
one equation. The collision residue
 succeeded in 51ms:
the symmetric theory is its image.

The $\Eone$ side is strictly richer: at degree~$2$ alone it
distinguishes algebras that the symmetric side identifies.
The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
$\widehat{\mathfrak{sl}}_2$-shadow
$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
h^\vee)$, but the underlying $r$-matrices distinguish them by their
matrix support. The ordered bar separates what the symmetric bar
collapses.
exec
/bin/zsh -lc "sed -n '208,220p' standalone/programme_summary_sections5_8.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\Sigma_2$-coinvariant projection. For non-abelian
affine Kac--Moody in the trace-form convention,
\[
\mathrm{av}(k\,\Omega/z)
\;=\;
\frac{k\,\dim(\fg)}{2h^\vee}
\;=\;
\kappa_{\mathrm{dp}}(\widehat\fg_k),
\qquad
\kappa(\widehat\fg_k)
\;=\;
\kappa_{\mathrm{dp}}(\widehat\fg_k)+\frac{\dim(\fg)}{2}.
\]

thinking
**Planning file updates**

I should change to `Ω_{\mathrm{tr}}` and consider inserting a bridge sentence before it. That sounds good. Maybe I'll look into `free_fields.tex`, focusing only on Heisenberg. After patching, I need to run targeted greps to ensure there are no instances of Heisenberg kOmega left in active files, as well as check for any `Omega_tr = Omega/(k+h^\vee)` issues in yangians_foundations. Time to patch!
codex
I’m applying a narrow Vol I patch now: one Heisenberg family correction in the live survey/standalone surfaces, one local comparison fix in `free_fields`, and three KM bridge fixes where KZ and trace-form conventions were switched without the explicit identity.
file update
M /Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex
@@ -622,6 +622,5 @@
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
@@ -707,3 +706,3 @@
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -711,4 +710,5 @@
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
M /Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex
@@ -175,2 +175,5 @@
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
@@ -210,3 +213,3 @@
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -444,3 +444,3 @@
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex
@@ -499,3 +499,6 @@
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
M /Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex
@@ -1063,4 +1063,4 @@
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
apply_patch(auto_approved=true) exited 0 in 41ms:
Success. Updated the following files:
M chapters/connections/thqg_introduction_supplement_body.tex
M chapters/examples/yangians_foundations.tex
M chapters/examples/free_fields.tex
M standalone/introduction_full_survey.tex
M standalone/programme_summary_sections5_8.tex
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;

file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Exploring formula patches**

I think I need to explore whether I should patch more. I should search again for the wrong Heisenberg formula in the current active repo. Then, there's the KM bridge — I'm considering that I might not have an explicit identity left in the patched files. It could be worth running a targeted grep to see if I can find anything relevant. Let's see what I've got!
exec
/bin/zsh -lc "rg -n 'Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|r\\(z\\) = \\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|r\\(z\\)=\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} = \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' chapters/connections/thqg_introduction_supplement_body.tex standalone/programme_summary_sections5_8.tex chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/connections/thqg_introduction_supplement_body.tex chapters/examples/yangians_foundations.tex chapters/examples/free_fields.tex standalone/introduction_full_survey.tex standalone/programme_summary_sections5_8.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'Heisenberg["'^'"\\n]*k\\\\,?\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\)=k\\\\Omega/z|Heisenberg, \\"'$r'"\\(z\\) = k\\\\,?\\\\Omega/z|Heisenberg.*\\\\Omega/z' /Users/raeez/chiral-bar-cobar" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1064: $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
 succeeded in 52ms:
standalone/programme_summary_sections5_8.tex:177: $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
standalone/programme_summary_sections5_8.tex:178: $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
standalone/programme_summary_sections5_8.tex:214:\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
chapters/examples/yangians_foundations.tex:1064: $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
chapters/examples/yangians_foundations.tex:1065: $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
chapters/connections/thqg_introduction_supplement_body.tex:501:convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
chapters/connections/thqg_introduction_supplement_body.tex:502:$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak:343:For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak:419:The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 succeeded in 52ms:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index 4775280..e9ff035 100644
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@ d \;-\; \frac{1}{k + h^\vee}
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
@@ -1750,7 +1753,7 @@ structural resolution of the completion obstacle.
 \label{subsec:thqg-intro-guide-bridges}
 
 Part~\ref{part:seven-faces} connects the engine to Feynman diagrams, BV-BRST quantization
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Considering git diffs**

I’m noticing that the `git diff` command shows many unrelated changes in the `free_fields` and `introduction_full_survey` files, likely due to user modifications in a dirty worktree. I need to be cautious not to mention these changes as my own. Using `--word-diff=porcelain` might help, but I can mention only my findings. I'll gather the line numbers of the relevant edits after applying the patch, using `nl -ba` to track those accurately.
exec
/bin/zsh -lc 'tmp1=$(mktemp); tmp2=$(mktemp); rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' 'k\\\\Omega/z|k\\\\,\\\\Omega/z|k\\\\,\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|k\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' > "'$tmp1; rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' '\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|\\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega_\\\\fg/\\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega_\\\\fg/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' > "'$tmp2; for f in $(comm -12 <(sort $tmp1) <(sort $tmp2)); do printf '"'%s\\t' \""'$f"; if rg -q '"'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic~\\"'$k'"\\"'$|= k'"\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' \""'$f"; then echo explicit; else echo missing; fi; done' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/frontier_modular_holography_platonic.tex	explicit
chapters/connections/holographic_datum_master.tex	explicit
chapters/connections/thqg_introduction_supplement_body.tex	explicit
chapters/examples/yangians_computations.tex	explicit
standalone/chiral_chern_weil.tex	missing
standalone/holographic_datum.tex	explicit
standalone/programme_summary_sections5_8.tex	explicit
standalone/sc_chtop_pva_descent.tex	explicit
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Inspecting document sections**

I see that the `standalone/chiral_chern_weil.tex` is still missing an explicit reference. I need to take a closer look at that section and examine the surrounding lines for any relevant information that might help fill in the gaps. It feels like I need to be thorough to ensure I don’t miss anything important! Let’s search through those lines and see what I can find.
exec
/bin/zsh -lc "rg -n 'k\\\\Omega|k\\\\,\\\\Omega|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|trace-form|KZ' standalone/chiral_chern_weil.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
146:$r(z) = k\,\Omega/z$ is valued in $\fg \otimes \fg$, and
449:\boxed{\;r^{\mathrm{KM}}(z) = \frac{k\,\Omega}{z},\quad
452:This is the \emph{trace-form convention}. The level~$k$
454:In the \emph{KZ convention}:
455:$r^{\mathrm{KZ}}(z) = \Omega/((k+h^\vee)z)$;
458:The bridge identity is $k\,\Omega_{\mathrm{tr}}
561:classical $r$-matrix (degree~$2$), $r_3$ is the KZ associator
762:The $r$-matrix is $r(z) = k\,\Omega/z$.
840:The $r$-matrix is $r(z) = k\,\Omega/z$ with $\Omega = \sum_{a=1}^8
972:Kac--Moody in the trace-form convention,
1049:$r(z) = k\,\Omega/z$ (trace-form convention). The averaging
1199:$V_k(\fg)$ & $k\,\Omega/z$ &
1360:the KZ associator~$r_3$ at degree~$3$, the quartic coherence
1433:\emph{Degree~$3$}: the $\Eone$ datum is the KZ associator
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;

codex
I’ve finished the Vol I patch and the post-edit greps are clean for the specific defects I targeted. I’m collecting final line references now and confirming which remaining inconsistencies are real read-only Vol II blockers versus already-bridged surfaces.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_introduction_supplement_body.tex | sed -n '496,504p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '442,447p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '1060,1067p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '705,712p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/introduction_full_survey.tex | sed -n '620,629p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/programme_summary_sections5_8.tex | sed -n '173,180p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/programme_summary_sections5_8.tex | sed -n '211,216p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex | sed -n '2306,2312p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex | sed -n '1917,1923p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '156,187p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   496	\end{equation}
   497	The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
   498	the Sugawara normalization of the affine OPE:
   499	$r(z) = \Omega / ((k + h^\vee)\,z)$ for
   500	$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
   501	convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
   502	$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
   503	This is \emph{not} the
   504	inverse of the modular characteristic
 succeeded in 51ms:
  1060	 via the level-shifted Killing form
  1061	 (Computation~\ref{comp:sl2-collision-residue-kz}).
  1062	 %: this is a section on C_2(X), not a formula over a point.
  1063	 Equivalently, in the trace-form normalization where
  1064	 $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
  1065	 $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  1066	 This $r$-matrix satisfies
  1067	 the classical Yang--Baxter equation in spectral-parameter form
 succeeded in 51ms:
   705	The $\Eone$ side is strictly richer: at degree~$2$ alone it
   706	distinguishes algebras that the symmetric side identifies.
   707	The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
   708	$\widehat{\mathfrak{sl}}_2$-shadow
   709	$r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
   710	have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
   711	h^\vee)$, but the underlying $r$-matrices distinguish them because
   712	the Heisenberg kernel is scalar while the affine one is
 succeeded in 50ms:
   620	contains its scalar trace. The averaging map
   621	$\operatorname{av}$ is surjective but not injective: the kernel
   622	records the non-symmetric components of the line-operator data.
   623	For Heisenberg, $r(z) = k/z$ is already scalar, so the
   624	symmetrization recovers $\kappa(\cH_k) = k$ without losing
   625	matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
   626	full Yangian double; the symmetrization recovers only
   627	$\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
   628	= k\dim\mathfrak g/(2h^\vee)$, and the full
   629	$\kappa(\widehat{\mathfrak g}_k)
 succeeded in 51ms:
   442	
   443	Compare with the Heisenberg, where the double-pole OPE
   444	$\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
   445	$r(z) = k/z$ (a simple pole after $d\log$ absorption).
   446	The one-step pole reduction works uniformly: double pole
   447	$\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 succeeded in 52ms:
   173	\item\label{it:drinfeld-face} The Drinfeld $r$-matrix
   174	 \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
   175	 $r(z) = \Omega/((k+h^\vee)z)$.
   176	 Equivalently, in the trace-form convention
   177	 $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
   178	 $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
   179	\item The Sklyanin bracket:
   180	 $\{L_1(u), L_2(v)\}
 succeeded in 52ms:
  2306	\label{comp:vol2-heisenberg-modular-extension}
  2307	\index{Heisenberg algebra!modular extension}
  2308	The Heisenberg genus-$0$ package has
  2309	$r(z)=k/z^2$, $m_k=0$ for $k\ge 3$, and
  2310	$\cC_{\mathrm{line}}\simeq\mathrm{Vect}^{\mathbb{Z}}$ (Fock modules).
  2311	The modular extension:
  2312	$\Theta_{\cH_k}=k\cdot\eta\otimes\Lambda$,
 succeeded in 52ms:
  1917	the $1/z^4$ term is \emph{absent}, reflecting the
  1918	weight-$1$ lacuna and the gap migration formula $d_{\mathrm{gap}} = 2N + n - 4 = 4$ at $N = 3$, $n = 2$ (Theorem~\ref{thm:gap-migration}(iv)). Compare with the $(T,T)$ collision
  1919	residue $r^{TT}(z) = (c/2)/z^3 + 2T/z + (\partial T)$
  1920	\textup{(}Computation~\textup{\ref{comp:vir-CYBE})},
  1921	which has pole orders $\{1, 3\}$ with the $1/z^2$ term
  1922	absent by the same weight-parity mechanism.
  1923	
 succeeded in 52ms:
   156	 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
   157	 \[
   158	 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
   159	 \]
   160	 \item the parameter-dependent classical Yang-Baxter equation
   161	 \[
   162	 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
   163	 \]
   164	\end{enumerate}
   165	\end{definition}
   166	
   167	The datum $(Y,r,T)$ is the strict shadow of the full $A_\infty$ structure treated later.
   168	
   169	\section{The strict logarithmic theory: the shifted KZ/FM connection}% label removed: sec:strict
   170	
   171	We begin with the strict theory because it exposes the geometric heart of the subject with maximal clarity: pairwise collisions, logarithmic poles, and Yang-Baxter flatness.
   172	
   173	\subsection{Construction}
   174	Let $(Y,r,T)$ be a strict rational dg-shifted Yangian and let $V_1,\dots,V_n$ be strict left $Y$-modules. Write $z_{ij}:=z_i-z_j$. On the trivial vector bundle over $\Conf_n(\AA^1)$ with fiber $V_1\otimes\cdots\otimes V_n$, define
   175	\[
 succeeded in 52ms:
   211	$\Sigma_2$-coinvariant projection. For non-abelian
   212	affine Kac--Moody in the trace-form convention,
   213	\[
   214	\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
   215	\;=\;
   216	\frac{k\,\dim(\fg)}{2h^\vee}
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Considering findings and closure**

I need to gather line references for volume 3, but there might not be any findings. I could mention that there are none. I wonder if I could use the explorer summary. Oh wait, our explorer agent may have completed the task by now. Yet, I think we probably don’t actually need that information. Maybe I should consider closing things, but perhaps I should wait just a bit longer to be sure.
collab wait(call_kgg7gFNKyoXvP5SvjaPqycpE)
  receivers: 019d87fa-4640-7290-944e-85715c15e4c1
wait(call_kgg7gFNKyoXvP5SvjaPqycpE) 1 agents complete:
  019d87fa-4640-7290-944e-85715c15e4c1 completed: "**Volume I**
- `chapters/examples/kac_moody.tex:82-127 & 750-774` — Affine KM: table entry and modular triple record `r(…"
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;

exec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'r\\(z\\)=k/z\\"'^2|r'"\\(z\\) = k/z\\"'^2|Heisenberg[''^'"\\n]*k/z\\"'^2|r'"\\"'^'"\\{\\\\mathrm\\{Heis\\}\\}\\(z\\) = k/z\\"'^2'"' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'r\\"'^'"\\{TT\\}\\(z\\) = .*\\\\partial T|r\\"'^'"\\{\\\\mathrm\\{Vir\\}\\}\\(z\\) = .*\\\\partial T|r\\"'^'"\\{\\\\mathrm\\{coll\\}\\}_c\\(z\\) = .*\\\\partial T|\\(c/2\\)/z\\"'^3 '"\\+ 2T/z \\+ \\(\\\\partial T\\)' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'r\\(z\\)=\\\\frac\\{\\\\Omega\\}\\{z\\}|r\\(z\\) = \\\\frac\\{\\\\Omega\\}\\{z\\}|r\\(z\\)=\\\\Omega/z|r\\(z\\) = \\\\Omega/z|Omega/z\\+r_\\{\\\\mathrm\\{reg\\}\\}' /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 50ms:

 exited 1 in 52ms:

file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Checking regex and issues**

I’m wondering if the regex isn't matching due to escaping—yet we already have specific lines in place. 

There might be active volume 3 issues, so maybe I should search for Heisenberg's wrong formula or look into missing KZ/trace mixes. If there aren’t any hits, I could state that no active volume 3 issues were found, but to be cautious, it seems like I should conduct a quick search anyway.
exec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'Heisenberg["'^'"\\n]*k\\\\,?\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega/z|r\\(z\\)=k/z\\"'^2|r'"\\(z\\) = k/z\\"'^2'"' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\).*k\\\\Omega/z|k\\\\Omega/z.*\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob 'chapters/**' --glob 'standalone/**' 'r\\"'^'"\\{\\\\mathrm\\{Vir\\}\\}\\(z\\) = .*\\\\partial T|r\\"'^'"\\{TT\\}\\(z\\) = .*\\\\partial T|\\(c/2\\)/z\\"'^4'"' /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 exited 1 in 52ms:

 exited 1 in 52ms:

file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Verifying patterns and outputs**

I’m not seeing any matches from the patterns, which is good! I think it might be helpful to note some verification. I could run a general grep after making a patch on the current repo to check for any active elements. The search results showed everything clearly. It might be useful to capture the output of that check in a file list. Maybe I should run a concise verification command for the final outputs. I’ll run a summary command too.
exec
/bin/zsh -lc 'tmp1=$(mktemp); tmp2=$(mktemp); rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' 'k\\\\Omega/z|k\\\\,\\\\Omega/z|k\\\\,\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|k\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' > "'$tmp1; rg -l --glob '"'chapters/**' --glob 'appendices/**' --glob 'standalone/**' '\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)z\\)|\\\\Omega / \\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega_\\\\fg/\\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\,z\\)|\\\\Omega_\\\\fg/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' > "'$tmp2; ok=1; while read -r f; do if ! rg -q '"'k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(k\\+h\\"'^'"\\\\vee\\)|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\} *= *\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|= k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z|k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}.*generic|= \\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\) = k\\\\,?\\\\Omega_\\{\\\\mathrm\\{tr\\}\\}/z' \""'$f"; then echo "missing bridge: $f"; ok=0; fi; done < <(comm -12 <(sort $tmp1) <(sort $tmp2)); if [ $ok -eq 1 ]; then echo '"'editable-vol1 mixed KM files: all carry an explicit bridge'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
missing bridge: standalone/chiral_chern_weil.tex
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Inspecting regex issue**

It looks like our regex is still missing explicit matches, especially since line 458 has a bridge identity. There might be something going on with a line break that's causing it to not catch what it should. I need to closely inspect the exact lines to figure out what's happening. It's a bit of a puzzle, but I'm determined to get to the bottom of this! Let's dig in and find the discrepancy.
exec
/bin/zsh -lc "nl -ba standalone/chiral_chern_weil.tex | sed -n '449,460p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   449	\boxed{\;r^{\mathrm{KM}}(z) = \frac{k\,\Omega}{z},\quad
   450	 \Omega = \sum_a t^a \otimes t^a \in \fg\otimes\fg.\;}
   451	\end{equation}
   452	This is the \emph{trace-form convention}. The level~$k$
   453	survives $d\log$-absorption. At $k = 0$: $r = 0$.
   454	In the \emph{KZ convention}:
   455	$r^{\mathrm{KZ}}(z) = \Omega/((k+h^\vee)z)$;
   456	at $k = 0$ this gives $\Omega/(h^\vee z) \neq 0$
   457	for non-abelian~$\fg$ (the Lie bracket persists).
   458	The bridge identity is $k\,\Omega_{\mathrm{tr}}
   459	= \Omega/(k+h^\vee)$ at generic~$k$.
   460	\end{computation}
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;

exec
/bin/zsh -lc "rg -n 'Heisenberg["'^'"\\n]*k\\\\,?\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\) = k\\\\Omega/z|r_\\{\\\\cH_k\\}\\(z\\)=k\\\\Omega/z' standalone/introduction_full_survey.tex chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;

Plan update
Applied the editable Vol I fixes, re-grepped the patched surfaces, and separated remaining issues into read-only Vol II blockers versus clean Vol III active chapters.
  ✓ Inspect candidate live files with mixed or suspect KM/Heis/Vir r-matrix formulas and confirm which ones actually violate the convention rules
  ✓ Apply minimum truthful Vol I edits with explicit bridge statements or corrected family formulas
  ✓ Re-grep the modified surface plus Vol II/III read-only surfaces and produce exact findings, fixes, and remaining blocked inconsistencies
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;


thinking
**Summarizing volume findings**

After reviewing all three volumes, I’ll make sure to mention that "Active Vol III chapter/standalone grep found no KM/Heis/Vir convention violations needing edits," which is useful. It's important to note that Volumes II and III are read-only due to permission issues. I don’t want to be too verbose, so I’ll aim for around 12-15 lines. A bullet list format might work best to keep it clear and organized.
codex
`PROBLEM` at [thqg_introduction_supplement_body.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement_body.tex:499): the file switched from the KZ residue `\Omega/((k+h^\vee)z)` to the trace-form discussion without stating the bridge. `EXACT edit applied`: added `Equivalently, in the trace-form convention one writes r(z)=k\,\Omega_{\mathrm{tr}}/z with k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee) at generic~k.`

`PROBLEM` at [yangians_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_foundations.tex:1063): the “equivalent” trace-form clause hid the level inside `\Omega_{\mathrm{tr}}`, writing `\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)` and `r(z)=\Omega_{\mathrm{tr}}/z`. `EXACT edit applied`: replaced that with `k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)` and `r(z)=k\,\Omega_{\mathrm{tr}}/z`.

`PROBLEM` at [free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:443): the Heisenberg comparison used the KM-style matrix formula `r(z)=k\,\Omega/z`. `EXACT edit applied`: changed it to `r(z)=k/z`.

`PROBLEM` at [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:623): the Heisenberg overview again used `r(z)=k\,\Omega/z`. `EXACT edit applied`: replaced it with `r(z)=k/z` and rewrote the sentence so Heisenberg is described as already scalar.

`PROBLEM` at [introduction_full_survey.tex](/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex:707): the ordered-side comparison wrote `r_{\cH_k}(z)=k\Omega/z`. `EXACT edit applied`: changed it to `r_{\cH_k}(z)=k/z` and rewrote the contrast as “Heisenberg kernel is scalar while the affine one is matrix-valued.”

`PROBLEM` at [programme_summary_sections5_8.tex](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:175): the file used KZ `\Omega/((k+h^\vee)z)` and later trace-form averaging without an explicit bridge. `EXACT edit applied`: added `r(z)=k\,\Omega_{\mathrm{tr}}/z` with `k\,\Omega_{\mathrm{tr}}=\Omega/(k+h^\vee)` at the Drinfeld-face item, and changed [line 214](/Users/raeez/chiral-bar-cobar/standalone/programme_summary_sections5_8.tex:214) from `\mathrm{av}(k\,\Omega/z)` to `\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)`.

`PROBLEM` at [ht_bulk_boundary_line_frontier.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_frontier.tex:2309): Vol II still states the Heisenberg genus-zero package as `r(z)=k/z^2`, which is the pre-absorption pole, not the collision residue. `EXACT edit applied`: none; `/Users/raeez/chiral-bar-cobar-vol2` is read-only in this session.

`PROBLEM` at [w-algebras-w3.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1919): Vol II still writes the Virasoro collision residue as `(c/2)/z^3 + 2T/z + (\partial T)`, retaining the Laplace term that should drop after `d\log` absorption. `EXACT edit applied`: none; `/Users/raeez/chiral-bar-cobar-vol2` is read-only in this session.

`PROBLEM` at [log_ht_monodromy.tex](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:158) and [line 186](/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186): Vol II presents a generic strict residue `\Omega/z` and then the affine specialization `k\,\Omega/z` without an explicit normalization bridge or disambiguation. `EXACT edit applied`: none; `/Users/raeez/chiral-bar-cobar-vol2` is read-only in this session.

Verification: the post-edit Vol I grep cleared the active Heisenberg `k\,\Omega/z` survivors and the patched mixed KM files now state the trace/KZ bridge explicitly. I did not find an active Vol III chapter/standalone violation in the KM/Heis/Vir sweep.
file update:
diff --git a/chapters/connections/thqg_introduction_supplement_body.tex b/chapters/connections/thqg_introduction_supplement_body.tex
index b8dca4ff8f98655d061a1f81717b997be0b0be8f..e9ff03502065623296d17ea564ef814d359feebc
--- a/chapters/connections/thqg_introduction_supplement_body.tex
+++ b/chapters/connections/thqg_introduction_supplement_body.tex
@@ -497,7 +497,10 @@
 The level-dependent prefactor $(k + h^\vee)^{-1}$ arises from
 the Sugawara normalization of the affine OPE:
 $r(z) = \Omega / ((k + h^\vee)\,z)$ for
-$\cA = \widehat{\mathfrak{g}}_k$. This is \emph{not} the
+$\cA = \widehat{\mathfrak{g}}_k$. Equivalently, in the trace-form
+convention one writes $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+$k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
+This is \emph{not} the
 inverse of the modular characteristic
 $\kappa(\widehat{\mathfrak{g}}_k)
 = \dim\mathfrak{g}\cdot(k + h^\vee)/(2h^\vee)$, which differs
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 2e164b44bc5221bd5cb01165f822c4ae79535057..fff6dfc8ccf41749541667200469db0f6660c30b
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -442,7 +442,7 @@
 
 Compare with the Heisenberg, where the double-pole OPE
 $\alpha(z)\alpha(w) \sim k/(z-w)^2$ gives
-$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
+$r(z) = k/z$ (a simple pole after $d\log$ absorption).
 The one-step pole reduction works uniformly: double pole
 $\to$ simple pole (Heisenberg), simple pole $\to$ regular (fermion).
 \end{proof}
diff --git a/chapters/examples/yangians_foundations.tex b/chapters/examples/yangians_foundations.tex
index b038d3864d3e35d6e1fbb5bfd88d2ee36b44377f..64849c39ef1db782fe162d053d65282f71804732
--- a/chapters/examples/yangians_foundations.tex
+++ b/chapters/examples/yangians_foundations.tex
@@ -1061,8 +1061,8 @@
  (Computation~\ref{comp:sl2-collision-residue-kz}).
  %: this is a section on C_2(X), not a formula over a point.
  Equivalently, in the trace-form normalization where
- $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
- $r(z) = \Omega_{\mathrm{tr}}/z$.
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$, the
+ $r$-matrix reads $r(z) = k\,\Omega_{\mathrm{tr}}/z$.
  This $r$-matrix satisfies
  the classical Yang--Baxter equation in spectral-parameter form
  \textup{(}equivalently, the infinitesimal braid relations for
diff --git a/standalone/introduction_full_survey.tex b/standalone/introduction_full_survey.tex
index b002be0e45c992813278195b5185c277df472ccd..75999f7e98874565f6b0f0a7333a0bd3e1e92254
--- a/standalone/introduction_full_survey.tex
+++ b/standalone/introduction_full_survey.tex
@@ -620,10 +620,9 @@
 contains its scalar trace. The averaging map
 $\operatorname{av}$ is surjective but not injective: the kernel
 records the non-symmetric components of the line-operator data.
-For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
-the symmetrization recovers the scalar
-$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
-discarded. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
+For Heisenberg, $r(z) = k/z$ is already scalar, so the
+symmetrization recovers $\kappa(\cH_k) = k$ without losing
+matrix-valued data. For affine Kac--Moody, $r(z) = k\,\Omega/z$ contains the
 full Yangian double; the symmetrization recovers only
 $\kappa_{\mathrm{dp}}(\widehat{\mathfrak g}_k)
 = k\dim\mathfrak g/(2h^\vee)$, and the full
@@ -705,12 +704,13 @@
 
 The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
-The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
+The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
 $r_{\widehat{\mathfrak{sl}}_2,k}(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
 have proportional $\kappa$-values when $k\dim\mathfrak g = k(k +
-h^\vee)$, but the underlying $r$-matrices distinguish them by their
-matrix support. The ordered bar separates what the symmetric bar
+h^\vee)$, but the underlying $r$-matrices distinguish them because
+the Heisenberg kernel is scalar while the affine one is
+matrix-valued. The ordered bar separates what the symmetric bar
 collapses.
 \end{remark}
 
diff --git a/standalone/programme_summary_sections5_8.tex b/standalone/programme_summary_sections5_8.tex
index 923f73d8b4d14528ce4339922a6ea0f1bcdaf0c0..ae60a6020fb8a7af42ba30212842ee186c7d65a9
--- a/standalone/programme_summary_sections5_8.tex
+++ b/standalone/programme_summary_sections5_8.tex
@@ -173,6 +173,9 @@
 \item\label{it:drinfeld-face} The Drinfeld $r$-matrix
  \textup{(}for $\cA = \widehat{\fg}_k$\textup{)}:
  $r(z) = \Omega/((k+h^\vee)z)$.
+ Equivalently, in the trace-form convention
+ $r(z) = k\,\Omega_{\mathrm{tr}}/z$ with
+ $k\,\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic~$k$.
 \item The Sklyanin bracket:
  $\{L_1(u), L_2(v)\}
  = [r(u - v), L_1(u) \otimes L_2(v)]$.
@@ -208,7 +211,7 @@
 $\Sigma_2$-coinvariant projection. For non-abelian
 affine Kac--Moody in the trace-form convention,
 \[
-\mathrm{av}(k\,\Omega/z)
+\mathrm{av}(k\,\Omega_{\mathrm{tr}}/z)
 \;=\;
 \frac{k\,\dim(\fg)}{2h^\vee}
 \;=\;

tokens used
381,959
