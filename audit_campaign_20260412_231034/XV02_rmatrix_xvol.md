# XV02_rmatrix_xvol (459s, gpt-5.4)

[CRITICAL] Vol I `chapters/connections/holographic_datum_master.tex:578` — Core face-theorem surface is not convention-stable. The same chapter first derives the affine collision residue in KZ normalization as `\Omega/((k+h^\vee)z)` at `:522-530`, then states the Drinfeld/Sklyanin input as `k\Omega/z` at `:578-593`, then hybridizes them as `k\Omega/((k+h^\vee)z)` at `:601`, and finally places a bare `\Omega/z` in the seven-face master diagram at `:717`. These are not a single convention with an explicit bridge.

[CRITICAL] Vol I `chapters/connections/genus1_seven_faces.tex:395` — The genus-1/KZB lane imports the same hybrid formula `k\Omega/((k+h^\vee)z)` and then treats it as the KZ/KZB coefficient. The degeneration theorem repeats this at `:977`, `:1002`, `:1010`, and `:1013`, including the trace-form vanishing check `k=0` inside a KZ-normalized argument. This is a false theorem-level normalization, not just sloppy prose.

[HIGH] Vol II `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:404` — A proved theorem states the affine simple pole as `k\Omega/((k+h^\vee)z)` with a separate `k\kappa/z^2` term. The same file later switches to `R(z)=1+\hbar\,\Omega/((k+h^\vee)z)+O(\hbar^2)` at `:1198`, and then to genus-0 `r_0(z)=\Omega/((k+h^\vee)z)+k\kappa/z^2` at `:1498`. One file is using three incompatible affine normalizations.

[HIGH] Vol II `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:183` — It says `r(z)=k\,\Omega/z` is “exactly the classical rational KZ connection,” which is the trace-form coefficient mislabeled as KZ. The same file then oscillates between an absorbed-residue bare expansion `R(z)=1+\Omega/z+\cdots` at `:1561`, an explicit `R(z)=1+k\Omega/z+\cdots` at `:1574`, and a hybrid `k\Omega/((k+h^\vee)z)` at `:1736-1744`. The non-core duplicate repeats the KZ mislabel at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186`.

[HIGH] Vol I `chapters/examples/yangians_drinfeld_kohno.tex:6856` — A proposition identifies `r_{\mathrm{KZ}}(z)=k\,\Omega/z` as the KZ equation’s classical `r`-matrix, and the proof repeats that at `:6879`. Later the same chapter derives the actual KZ coefficient `1/(k+h^\vee)` only by dividing the trace-form residue by `\kappa` at `:7547-7552`. That is an unannounced convention swap.

[HIGH] Vol I `chapters/connections/frontier_modular_holography_platonic.tex:1680` — This downstream frontier surface repeats the core drift: it uses the trace-form `k\Omega/z` for the “level-k rational `r`-matrix,” but the same theorem immediately sets the collision-residue prefactor equal to `1/(k+h^\vee)` at `:1692` and writes `r(z)=\Omega/((k+h^\vee)z)` at `:1713`. Later it reverts to `k\Omega/z` again at `:4763`. The propagation failure is cross-section, not isolated.

[MEDIUM] Vol III `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:111` — This remark explicitly adopts the trace-form convention `r(z)=k\,\Omega/z`, but its critical-level check at `:117` says the `R`-matrix “degenerates,” which is KZ critical-level behavior, not trace-form behavior. The cross-volume checker is itself mixing the two conventions.

[MEDIUM] Vol III `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38` — The sentence says “(level-stripped `r`-matrix)” and immediately writes the level-prefixed trace-form `r(z)=k\,\Omega/z`; it then argues that at `k=-h^\vee` the collision `r`-matrix is no longer the surviving structure. That imports KZ/`kappa`-collapse logic into a trace-form sentence and is locally self-contradictory.

## Summary
Instances checked: 22 | Violations found: 8 | Verdict: FAIL


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
session id: 019d83b2-cc1f-7ac3-97d9-7683e793067e
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


MISSION: Cross-volume consistency check for r-matrix conventions.

Are r-matrix conventions consistent? Check trace-form vs KZ, level prefix presence, across all 3 repos.

Search across ALL three repos:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding, note: which volume, file:line, the inconsistency, and severity.
mcp startup: no servers

thinking
**Planning file operations**

I’m considering using commentary, then maybe calling multiple tools in parallel to read files. I need to ensure local file reads are in order, perhaps using `sed -n`. Since shell outputs won’t be visible to the user, that’s fine. I think I’ll use exec_command to carry out the reading. It feels like a solid plan; just need to make sure everything works as expected!
codex
Using `deep-beilinson-audit` for an adversarial cross-volume formula audit, and `multi-path-verify` for the specific `r`-matrix convention checks. First step is to load the repo’s live convention sources and then grep the three chapter trees for every `r`-matrix occurrence.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 220

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
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

 succeeded in 52ms:
Total output lines: 240

# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

 succeeded in 52ms:
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
codex
I’ve loaded the repo’s governing convention surface. Next I’m enumerating every chapter-level `r`-matrix occurrence in all three volumes, then I’ll classify them against the canonical split: trace-form `k\Omega/z` versus KZ `\Omega/((k+h^\vee)z)`, with bare `\Omega/z` treated as a violation unless explicitly converted.
Plan update
Cross-volume adversarial audit for r-matrix conventions. No file edits; only evidence gathering and verification.
  → Search all three chapter trees for r-matrix and related level-prefix formulas
  • Read each candidate in context and classify against canonical trace-form vs KZ conventions
  • Re-verify surviving discrepancies and produce severity-ordered findings


thinking
**Planning regex searches**

I'm considering running `rg` across multiple repositories, using patterns in each repo to compile a candidate list. Since the output may be large, I wonder if I should store it in temp files. However, the user mentioned not to modify any files, so maybe it’s best to avoid writing anything at all. 

I could use process substitution or pipes for output without writing, but I can still pull large data directly from `rg` while keeping my search systematic across specific chapters and patterns related to `\Omega` and `z`.
thinking
**Targeting searches effectively**

I'm concerned that I might miss multiline formulas, so I think about searching specifically for `\Omega` and inspect its context in relevant files. Aiming to use `rg -n --glob '*.tex' "\\\\Omega"` seems reasonable, but I worry about unrelated results. Instead, I should focus on lines with `r(z` or `R-matrix` to identify suitable candidate files. That way, I can run a more targeted search and inspect the relevant sections without getting lost in unrelated output.
exec
/bin/zsh -lc "rg -n --glob '*.tex' -e 'r-matrix' -e 'R-matrix' -e 'classical r' -e 'KZ normalization' -e 'trace-form' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' -e 'r\\"'^'"\\{?KM\\}?\\(z\\)' -e 'r\\"'^'"\\{?Heis\\}?\\(z\\)' -e 'r\\"'^'"\\{?Vir\\}?\\(z\\)' -e 'r\\(z\\)' -e 'R\\(z\\)' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' -e '\\\\Omega/z' -e '\\\\frac\\{\\\\Omega\\}\\{z\\}' -e 'k\\\\Omega/z' -e '\\\\frac\\{k\\\\Omega\\}\\{z\\}' -e '\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' -e '\\\\frac\\{\\\\Omega\\}\\{\\(k\\+h\\"'^'"\\\\vee\\)z\\}' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 690

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:109:\label{sec:r-matrix-categorical}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:115:\label{prop:r-matrix-bar}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:131:%: the r-matrix has pole orders ONE LESS than the OPE.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:132:%: affine KM r-matrix at level k is k*Omega/z, not Omega/z.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:550:\label{prop:shadow-depth-r-matrix}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:567:%: av is lossy. The R-matrix r(z) has more information than kappa.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:569:% p_max = 2 (OPE poles z^{-2}, z^{-1}), k_max = 1 (r-matrix pole z^{-1}),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:49:\phantomsection\label{eq:M2-r-matrix}%
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:100:\index{R-matrix!rational, trigonometric, elliptic}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:434:\item The dynamical R-matrix $R(u, \lambda)$ depending on spectral parameter $u$ 
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:443:\begin{definition}[Elliptic R-matrix]\label{def:elliptic-r}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:444:The elliptic R-matrix for $\mathfrak{sl}_2$ is:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1083:\begin{equation}\label{eq:sl2-r-matrix-entries}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5903:(Vol~II, eq.~\eqref{eq:M2-r-matrix})
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5972:(Vol~II, eq.~\eqref{eq:M2-r-matrix}) is manifestly symmetric
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:6005:\label{constr:elliptic-r-matrix-sklyanin}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex:1064: $R^{\mathrm{MO}}(z)$ of Section~\ref{sec:mo-r-matrix},
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:424:%% SECTION 5: Face 4 -- Maulik-Okounkov R-matrix
 succeeded in 51ms:
Total output lines: 1473

/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:574:exactly the CYBE for $r(z)$. This is the standard
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:78:\paragraph{Bulk-to-boundary and $R(z)$.}
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:81:R(z)\cdot (v_{q_1}\otimes v_{q_2}) \;=\; \exp\!\Bigl( \hbar\, \frac{q_1 q_2}{z} \Bigr) \,(v_{q_2}\otimes v_{q_1}),
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:83:up to normalization (in perturbation theory). The classical $r(z)=\frac{q_1 q_2}{z}$ satisfies CYBE.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:87:For abelian Chern--Simons with HT boundary condition, conditional on Theorem~\ref{thm:physics-bridge}, the boundary category of line operators is braided by $R(z)$, with classical limit $r(z)=\frac{k}{z}$ (after normalization). The bulk chiral Hochschild cochains produce the same $r(z)$ via the Laplace transform of the bulk $\lambda$-bracket kernel as in Proposition~\ref{prop:field-theory-r}.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:129:$r(z) = k/z^2$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:136:For $\beta\gamma$/$bc$: $\{b_\lambda c\} = 1$ gives $r(z) = 1/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1197:r(z)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:1244: $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2492: r(z)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2729:$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2860: $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3150:\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3280: $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3394: $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:2759:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:5993:The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:524:$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3438: via the collision residue $r(z) = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3467:classical limit: $r(z) = k\,\Omega/z$ is the classical
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:3569:Collision residue & $k\,\Omega/z$ & $k\,\Omega/z$ (same) \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex:4594:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete.tex:722:$k\,\delta^{ab}/z^2$ gives, after $d\log$ absorption, the collision $r$-matrix $r(z) = k\,\Omega/z$, the standard rational
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:305:$r(z) = k\,\Omega/z$, the standard rational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:795:The collision residue $k\,\Omega/z$ satisfies the CYBE:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:802:This is the standard rational CYBE (the common factor $k^2$ cancels); the solution $k\,\Omega/z$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:966: & $k\,\Omega/z$ (classical rational affine residue)
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:1841: ($R = 1 + k\Omega/z + \cdots$), Virasoro, $\cW_3$, symplectic
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2256:$r(z) = k\,\Omega/z$ (with $\Omega$ the Casimir





thinking
**Analyzing inconsistencies in outputs**

I see that the search results are quite extensive, and it’s important for me to identify genuine inconsistencies, as there might be many. The user is asking for a cross-volume consistency check specifically for the r-matrix conventions between trace-form and KZ. I’ll need to read contexts carefully to avoid false positives. I need to emphasize actual inconsistencies, such as the presence of a level prefix and correct usage of naming conventions. I should assess according to established canon.
thinking
**Evaluating r-matrix conventions**

When I consider evaluation modules of \(V_k(\mathfrak{sl}_2)\), I might present them as \(1 + \hbar k \Omega / z\) or possibly KZ's form, `1 + \hbar \Omega/((k+h^\vee)z)`. The user is asking for a cross-volume consistency check on r-matrix conventions. Some inconsistencies to note include the absence of a level prefix with bare Ω/z and potential mislabeling of conventions. Additionally, mixing KZ and trace-form in the same file could present issues, and I need to evaluate whether `κ_ch` is consistently used as a level prefix in Volume III.
thinking
**Inspecting file contents**

I need to read the context to determine if there's an error or if it's okay. In Volume II at a specific line, it mentions a term that looks mixed up with an incorrect prefactor. I should inspect the context further. There’s another line that might be fine, but then another term indicates possible inconsistency in using certain expressions. It seems like I need to check if the file inconsistently applies these terms across its content.
thinking
**Considering findings and processes**

I’m thinking about how to organize findings by severity, possibly including a low severity draft. I should count the instances checked, maybe computing N to track candidate occurrences or files accurately. I need a systematic approach for this. Using certain detection patterns could help identify violations related to specific quantum group contexts. It sounds important to search for relevant terms around "affine" and related concepts in the materials for a thorough audit.
thinking
**Identifying unique files and references**

I’m considering that I don’t need a complete list of every mention if there are many duplicates. Instead, I should gather enough evidence to address the user’s request. They want to cross-check across all three repositories, which could involve a lot of work. I need to focus on identifying unique problematic files and line references, making sure not to overwhelm with redundancy but still being thorough.
codex
The broad grep surfaced the expected safe cluster and a narrower problematic cluster. I’m now reading only the high-risk contexts: hybrid formulas like `k\Omega/((k+h^\vee)z)`, bare `\Omega/z` in affine/KZ discussions, and places that explicitly call a trace-form expression “KZ”.
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)z\\)|k\\\\,?\\\\Omega/\\(\\(k\\+2\\)z\\)|k\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\Omega/\\(\\(k\\+h\\"'^v'"\\)z\\)' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'r_\\{?KZ\\}?\\(z\\).*k\\\\,?\\\\Omega/z|KZ["'^'"\\n]{0,120}k\\\\,?\\\\Omega/z|k\\\\,?\\\\Omega/z["'^'"\\n]{0,120}KZ' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' '(affine|Kac--Moody|KZ|Kazhdan|V_k\\(|\\\\widehat\\{\\\\f?g\\}_k|critical level)["'^'"\\n]{0,240}(\\\\Omega/z|\\\\frac\\{\\\\Omega\\}\\{z\\})|(\\\\Omega/z|\\\\frac\\{\\\\Omega\\}\\{z\\})["'^'"\\n]{0,240}(affine|Kac--Moody|KZ|Kazhdan|V_k\\(|\\\\widehat\\{\\\\f?g\\}_k|critical level)' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/genus1_seven_faces.tex:395:$r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$
chapters/connections/genus1_seven_faces.tex:450:$k\,\Omega/((k+h^\vee)z)$
chapters/connections/genus1_seven_faces.tex:977:$r^{(1)}_{\widehat{\fg}_k}(z, \tau) \to k\,\Omega/((k+h^\vee)z)$.
chapters/connections/genus1_seven_faces.tex:1010:rational $r$-matrix $k\,\Omega/((k+h^\vee)z)$ in the Kazhdan
chapters/connections/genus1_seven_faces.tex:1013:propagator $r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$\textup{)}.
chapters/connections/holographic_datum_master.tex:601:residue $r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$ becomes the
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:412:$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1736:$\wp$-function. = k\,\Omega/((k+h^\vee)z)$; the intrinsic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1744:rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic
 succeeded in 51ms:
chapters/examples/yangians_drinfeld_kohno.tex:6856:$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
chapters/examples/yangians_drinfeld_kohno.tex:6879:$r$-matrix $r_{\mathrm{KZ}}(z) = k\,\Omega/z$, confirming the
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5111: $r(z) = k\,\Omega/z$, not the KZ-normalised coefficient
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:3032:For $G = SL_2$: $\Bbound = \widehat{\mathfrak{sl}}_2{}_k$, $\cA^!_{\mathrm{ch}} = \widehat{\mathfrak{sl}}_2{}_{-k-4}$, $r(z) = k\,\Omega/z$ (vanishing at $k = 0$ satisfied). The KZ connection is the degree-$(2,0)$ projection of $\alpha_T$; on evaluation modules, the reduced HT spectral $R$-matrix agrees with the quantum-group $R$-matrix of $U_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$ (Theorem~\ref{thm:affine-monodromy-identification}). Line category:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:183:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
 succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:48:For $V_k(\mathfrak{sl}_2)$, the collision residue is $r(z) = k\,\Omega/z$, where $\Omega = \sum e_a \otimes e^a \in \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$ is the Casimir tensor. Again $k=0$ gives $r=0$. At leading order, $R(z) = 1 + \hbar\, k\,\Omega/z + \cdots$ is the Yang $R$-matrix. The YBE at order $\hbar^2$ reduces to the infinitesimal braid relation $[\Omega_{12},\, \Omega_{13} + \Omega_{23}] = 0$, which is the Jacobi identity on $\mathfrak{sl}_2$. This is class~L: depth $1$, the $r$-matrix carries non-trivial Lie structure, but the twisted coproduct $\Delta_z$ on the Koszul dual is still cocommutative at the classical level.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:563:\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:792:$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:1568:$r^{\mathrm{coll}}(z) = k\,\Omega/z$ (affine).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:2518:$R(z) = 1 + k\Omega/z$ of $V_k(\mathfrak{sl}_2)$
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:5111: $r(z) = k\,\Omega/z$, not the KZ-normalised coefficient
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2721:HPL correction replaces $k\,\Omega/z$ (the affine Casimir)
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:4800:the affine Casimir $k\,\Omega/z$ to the gravitational
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-complete-proved.tex:966: & $k\,\Omega/z$ (classical rational affine residue)
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:791:$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1420:Equivalently: $K_\cA(z) = 1$ iff the boundary coproduct is primitive iff the shadow tower terminates at depth zero. This is the $K$-matrix shadow of the pole-order hierarchy summarised in Table~\ref{tab:two-colour-koszul-duals} and in the shadow-depth discussion of Volume~I. It is not an $r$-matrix statement: the $K$-matrix modifies the coproduct, not the product, and the level-$k$ vanishing check does not apply directly; the corresponding $r$-matrix check is the one already recorded in the Volume~II affine constructions (classical $r$-matrix $k\,\Omega/z$ vanishes at $k=0$, in which case $\cA = \cH_0$ collapses to the trivial Heisenberg and $K_\cA(z) = 1$, consistent with class~$\mathbf{G}$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6206:$r_{V_k(\mathfrak{sl}_2)}(z) = k\,\Omega/z$, which at
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:183:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:3032:For $G = SL_2$: $\Bbound = \widehat{\mathfrak{sl}}_2{}_k$, $\cA^!_{\mathrm{ch}} = \widehat{\mathfrak{sl}}_2{}_{-k-4}$, $r(z) = k\,\Omega/z$ (vanishing at $k = 0$ satisfied). The KZ connection is the degree-$(2,0)$ projection of $\alpha_T$; on evaluation modules, the reduced HT spectral $R$-matrix agrees with the quantum-group $R$-matrix of $U_q(\mathfrak{sl}_2)$ at $q = e^{i\pi/(k+2)}$ (Theorem~\ref{thm:affine-monodromy-identification}). Line category:
chapters/examples/yangians_drinfeld_kohno.tex:6856:$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
chapters/examples/yangians_drinfeld_kohno.tex:6879:$r$-matrix $r_{\mathrm{KZ}}(z) = k\,\Omega/z$, confirming the

thinking
**Searching specific volumes**

I need to search specifically for Volume III related to KZ and hbar. It seems like using a targeted approach might be the best strategy here. I’ll make sure to focus my search to get the most relevant information about those topics. Let’s see what I can find that fits those criteria! That should help clear things up.
exec
/bin/zsh -lc "sed -n '960,1025p' chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1188,1210p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '510,735p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1428,1455p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '380,470p' chapters/connections/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '160,210p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1490,1508p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '390,430p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6820,6895p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\wp(z, \tau) \to \pi^2/\sin^2(\pi z) \to 1/z^2 + O(1)$, and
$\wp^{(m)}(z, \tau) \to (-1)^m(m+1)!/z^{m+2} + O(z^{-m})$ at leading
order.

\item \textup{(}KZB $\to$ KZ.\textup{)}
The $dz$-component of the KZB connection degenerates to the KZ
connection: $\zeta_\tau(z_{ij}) \to 1/(z_{ij})$. The
$d\tau$-component vanishes because the modulus $\tau$ is not a
parameter at genus~$0$.

\item \textup{(}Elliptic $r$-matrix $\to$ rational $r$-matrix.\textup{)}
The Belavin $r$-matrix degenerates to the classical rational Casimir
kernel $r^{\mathrm{rat}}_\fg(z)$, through the
intermediate trigonometric $r$-matrix:
$r^{\mathrm{ell}} \to r^{\mathrm{trig}} \to r^{\mathrm{rat}}$.
The collision residue~\eqref{eq:g1sf-elliptic-rmatrix} inherits
the level normalization:
$r^{(1)}_{\widehat{\fg}_k}(z, \tau) \to k\,\Omega/((k+h^\vee)z)$.
At the critical level $k = -h^\vee$ the normalized rational
$r$-matrix is singular; at $k = 0$ the collision residue
 succeeded in 52ms:
\index{Yangian!classical as genus-0 truncation}
The classical Yangian $Y(\fg)$ is the genus-$0$ truncation of
$Y_T^{\mathrm{mod}}$: the quotient
$Y_T^{\mathrm{mod}} / G^1 Y_T^{\mathrm{mod}}$ retains only the
tree-level (genus-$0$) contribution. The classical $r$-matrix
$r(z) = r_{T,0}(z)$ is the unique Maurer--Cartan element at this
truncation level.

For $\cA = \widehat{\fg}_k$: the classical Yangian $Y(\fg)$ is
recovered from the genus-$0$ projection of $Y_T^{\mathrm{mod}}$.
The $R$-matrix $R(z) = 1 + \hh\, \Omega/((k+h^\vee)z)
+ O(\hh^2)$ deforms to the quantum Yangian $R$-matrix
$R^{\mathrm{qu}}(z) = (z + \hh\,P)/(z - \hh)$ by resumming the
genus expansion to all orders.
\end{corollary}

\begin{proof}
The genus filtration $G^\bullet$ on $Y_T^{\mathrm{mod}}$ has
$\gr^G_0$ consisting of tree-level graphs only. The MC equation
at genus $0$ is $d\, r_0 + \frac{1}{2}[r_0, r_0] = 0$, the
 succeeded in 51ms:
\end{theorem}

\begin{proof}
The Kac--Moody OPE
$J^a(z)\, J^b(w) \sim k\,\delta^{ab}/(z-w)^2 + f^{ab}_{\;\;c}\,
J^c(w)/(z-w)$ has poles of order~$2$ and~$1$. The bar propagator
$d\log(z-w)$ absorbs one power, so the collision residue
extracts the simple-pole coefficient: the zeroth product
$a_{(0)}b = f^{ab}_{\;\;c} J^c$ (the Lie bracket). The double-pole
term $k\,\delta^{ab}$ contributes to the curvature~$m_0$, not to
the collision residue
(Computation~\ref{comp:sl2-collision-residue-kz}, Step~2).
Dualizing via the level-shifted Killing form $(k+h^\vee)\kappa$
(the Sugawara normalization) gives the Casimir $r$-matrix
$\Omega/((k+h^\vee)z)$, which is~\eqref{eq:hdm-face-5}.
At the critical level $k = -h^\vee$ the denominator vanishes,
tracking the Sugawara singularity.
At $k = 0$ the collision residue is $\Omega/(h^\vee z) \neq 0$:
the Lie bracket of~$\fg$ persists at vanishing level, so the
abelian vanishing $r = 0$ that characterizes the Heisenberg
 succeeded in 51ms:
\;=\;
-\sum_{j \neq i}
\partial_z \bigl[r_{\widehat{\fg}_k}^{(1)}(z_{ij}, \tau)\bigr]_{ij}.
\end{equation}
The modular Hamiltonian is the $z$-derivative of the collision
residue: $\wp(z, \tau) = -\zeta_\tau'(z)$.
\end{enumerate}
\end{theorem}

\begin{proof}
\textbf{Part (i).} The affine Kac--Moody collision residue at
genus~$1$ is
$r_{\widehat{\fg}_k}^{(1)}(z, \tau) = k\,\Omega\, \zeta_\tau(z)/(k + h^\vee)$,
by Theorem~\ref{thm:g1sf-elliptic-regularization} applied to the
genus-$0$ collision residue
$r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$
(Theorem~\ref{thm:hdm-face-5}). Since affine Kac--Moody has
$p_{\max} = 2$ and $k_{\max} = 1$ (the OPE has poles of order
$2$ and $1$; the bar propagator absorbs one order), the
collision expansion has $c_0 = k\,\Omega/(k+h^\vee)$ and $c_n = 0$ for
 succeeded in 51ms:
$\widehat{\mathfrak{sl}}_2$ level-$1$ WZW fusion rules.
\end{computation}

\begin{computation}[Formal $R$-matrix expansion; \ClaimStatusProvedHere]
% label removed: comp:formal-R-expansion
\index{R-matrix@$R$-matrix!formal expansion}
The formal monodromy operator, equivalently the asymptotic $R$-matrix,
admits the $z^{-1}$-expansion
\begin{equation}% label removed: eq:R-formal-expansion
 R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots
 \;=\; \exp\!\Bigl(\frac{\Omega}{z}\Bigr)\quad (\text{leading order}).
\end{equation}
More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
and corrections of order $O(z^{-3})$ arise from the non-abelian exponentiation
(Magnus series). On $V\otimes V$ one can diagonalize:
\[
 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
 \qquad
 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
\]
 succeeded in 52ms:
 \item the parameter-dependent classical Yang-Baxter equation
 \[
 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
 \]
\end{enumerate}
\end{definition}

The datum $(Y,r,T)$ is the strict shadow of the full $A_\infty$ structure treated later.

\section{The strict logarithmic theory: the shifted KZ/FM connection}% label removed: sec:strict

We begin with the strict theory because it exposes the geometric heart of the subject with maximal clarity: pairwise collisions, logarithmic poles, and Yang-Baxter flatness.

\subsection{Construction}
Let $(Y,r,T)$ be a strict rational dg-shifted Yangian and let $V_1,\dots,V_n$ be strict left $Y$-modules. Write $z_{ij}:=z_i-z_j$. On the trivial vector bundle over $\Conf_n(\AA^1)$ with fiber $V_1\otimes\cdots\otimes V_n$, define
\[
 \nabla_n^Y
 :=
 d-\sum_{1\le i<j\le n}\rho_{ij}(r(z_{ij}))\,d(z_{ij}),
\]
 succeeded in 51ms:
zeta and $\wp$-functions with periods $1, \tau$. This is the
elliptic $r$-matrix of~\eqref{eq:elliptic-r-matrix} specialized
to $\widehat{\fg}_k$.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:elliptic-spectral-dichotomy}, the genus-$1$
$r$-matrix is obtained from the genus-$0$ $r$-matrix
$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
rational kernel functions by their elliptic counterparts:
$1/z \leadsto \zeta(z|\tau)$ and $1/z^2 \leadsto \wp(z|\tau)$.

The Bergman kernel on $E_\tau$ is
$B(z, w|\tau) = \wp(z-w|\tau)\, dz\, dw + 2\eta_1\, dz\, dw$,
where the correction $2\eta_1$ is the Legendre constant ensuring
the normalization $\int_{A} B(z, w) = 0$ (integration over the
$A$-cycle in either variable). The one-particle restriction
operator (Volume~I, \S\ref*{sec:heisenberg-one-particle-sewing})
has eigenvalues $\wp^{(n)}(z|\tau)$ acting on the $n$-th
 succeeded in 50ms:
\end{proposition}

\begin{proof}
The CG apparatus (Proposition~\ref{prop:chriss-ginzburg-structure})
realizes the bar differential on
$\overline{C}_2^{\mathrm{ord}}(\bC)$ as $d_{\mathrm{bar}} =
d_{\mathrm{int}} + [\tau, -]$, where $\tau$ is the MC element in
the convolution algebra $\operatorname{Conv}(\bar B(\cA), \cA^!)$ and the bracket
action is contraction with the propagator
$\eta_{12} = d\log(z_1 - z_2)$
on internal edges. For the Heisenberg algebra $\cH_k$, the OPE
$J(z)J(w) \sim k/(z{-}w)^2$ has a double pole. The $d\log$ kernel
absorbs one pole order: $z^{-2} \to z^{-1}$, giving
$r(z) = \tau|_{\deg 2} = k/z$.
For the $\beta\gamma$ system, the mixed OPE
$\beta(z)\gamma(w) \sim 1/(z{-}w)$ has only a simple pole;
after $d\log$ absorption the result is regular, so
$r^{\beta\gamma}(z) = 0$.
\end{proof}

 succeeded in 51ms:
\index{affine Kac--Moody!classical r-matrix|textbf}
\index{classical r-matrix!affine}
\index{Casimir element!in r-matrix}

\begin{theorem}[Affine $r$-matrix from collision residue;
\ClaimStatusProvedHere]
% label removed: thm:affine-r-matrix
For the affine Kac--Moody algebra $\widehat{\fg}_k$ at level $k$
(with $k + h^\vee \ne 0$), the classical $r$-matrix is
\begin{equation}
% label removed: eq:affine-r-explicit
\boxed{
r_{\widehat{\fg}_k}(z)
\;=\;
\frac{k\,\Omega}{(k + h^\vee)\, z}
\;+\;
\frac{k\, \kappa}{z^2},
}
\end{equation}
where $\Omega = \sum_a t^a \otimes t_a \in \fg \otimes \fg$ is the
codex
The first context pass confirms genuine drift, not just grep noise. I’ve verified one strong cluster already: Volume I has both a KZ-style `\Omega/((k+h^\vee)z)` explanation and a trace-form `k\Omega/z` explanation for the same affine collision residue, with a hybrid `k\Omega/((k+h^\vee)z)` formula in the same lane. Now I’m re-reading the remaining candidates with line-numbered context so the final report contains only verified discrepancies.
exec
/bin/zsh -lc "sed -n '140,195p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'KZ|Kazhdan|k\\+h\\"'^'"\\\\vee|h_\\{?KZ\\}?|Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\Omega/z' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

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
/bin/zsh -lc "sed -n '1,140p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1728,1750p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '104,122p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '500,540p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2748,2770p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
7:identifies the monodromy representation of the KZ connection on
29:The classical Kazhdan--Lusztig and Kazhdan
88:DK compares geometric braid monodromy (from KZ/configuration
106:DK-$2/3$ & $\pi_{3,0}(\Theta^{\Eone}_\cA)$ & Generated-core comparison (CYBE, KZ associator) \\
141:shadow recovers the KZ associator. The quartic projection
185:where the vertical arrows are the Kazhdan--Lusztig equivalences
217:monodromy of the KZ connection on conformal blocks. By the
224:$\gamma_{12}$, so the KZ monodromy around $\gamma_{12}$ is sent to
251:\textbf{Left/Right}: & KZ monodromy $=$ quasi-$R$-matrix
267:\item KZ monodromy of $\nabla^{\mathrm{KZ}}$,
277:The parameter $u_D = \cot(\pi/(k+2))$ is real, not imaginary. The Hecke braiding eigenvalues ($q$ and $-q^{-1}$) are distinct from the KZ monodromy eigenvalues ($q^{1/2}$ and $-q^{-3/2}$).
308:and fits into the same square as the Kazhdan equivalence
349:Under the Kazhdan identification $\Phi_K$, this becomes the
361:\emph{Step~1: The Kazhdan equivalence.}
362:The Kazhdan functor~\cite{Drinfeld85}
408:The Kazhdan functor identifies $R_Y(u)$ with $R_q(e^u)$,
422:the Kazhdan equivalence.
549:This is the factorization-level Kazhdan bridge beyond the evaluation
573:KZ_{\mathrm{fact}}^{\mathrm{gen}}\colon
639:\item construction of the ordered factorization Kazhdan transport on
 succeeded in 51ms:
Total output lines: 140

\chapter{Geometric Langlands and CY Quantum Groups}
\label{ch:geometric-langlands}

The functor $\Phi$ of \ref{part:bridge} sends a Calabi--Yau category to an $\Etwo$-chiral algebra; the bar complex of the output (Volume~I, Theorem~A) is the factorization invariant on which geometric Langlands is ultimately a statement. This chapter traces the thread. At the critical level the Feigin--Frenkel theorem identifies the chiral center with the algebra of $G^L$-opers; the Verdier intertwining of Volume~I Theorem~A then relates local geometric Langlands to the four-functor picture (bar, cobar, Verdier, derived center). For Calabi--Yau input, the analogue is conjectural: a Langlands dual of a CY $d$-category should realize the mirror of its $\Phi$-image. The chapter is entirely FRONTIER material. Every formal statement uses \texttt{\textbackslash{}begin\{conjecture\}} unless it is a literal citation of Feigin--Frenkel (1992) or Frenkel--Gaitsgory (2006), in which case it is tagged \ClaimStatusProvedElsewhere.


% ============================================================
\section{The Feigin--Frenkel center at the critical level}
\label{sec:feigin-frenkel}
% ============================================================

Let $\frakg$ be a simple finite-dimensional complex Lie algebra and $\hat{\frakg}_k$ its affine Kac--Moody algebra at level $k$. The vacuum vertex algebra $V_k(\frakg)$ is the universal chiral algebra generated by the currents $J^a(z)$ with the Kac--Moody OPE. The \emph{critical level} is $k_c = -h^\vee$, where $h^\vee$ is the dual Coxeter number.

\begin{theorem}[Feigin--Frenkel, 1992]
\label{thm:feigin-frenkel-center}
\ClaimStatusProvedElsewhere{}
At the critical level $k = -h^\vee$, the center of the vacuum vertex algebra is canonically isomorphic to the algebra of functions on the space of $G^L$-opers on the formal disk:
\[
 succeeded in 51ms:
 = \frac{k\,\Omega}{(k+2)z}
 - \frac{k\,\Omega}{k+2}\sum_{n=1}^{\infty}2\,
 \frac{q^{2n}}{1-q^{2n}}\cdot 2\pi i\cos(2\pi nz)
 = \frac{k\,\Omega}{(k+2)z}
 + \frac{k\,\Omega}{k+2}\bigl(2G_2(\tau)-\wp(z;\tau)-\pi^2/3\bigr),
\]
where the Eisenstein correction $G_2(\tau)$ accounts for the
(conditionally convergent) sum and $\wp$ is the Weierstrass
$\wp$-function. = k\,\Omega/((k+h^\vee)z)$; the intrinsic
KZB connection~\eqref{eq:kzb-connection} retains the standard
Sugawara normalization $(k+h^\vee)^{-1}$, so the identification of
$r_1$ with the connection form carries the rescaling factor
$k/(k+h^\vee)$. At $k=0$ both the connection trivializes in the
collision sector and $r_1$ vanishes, consistent with
Theorem~\ref{thm:affine-monodromy-identification}.) Thus the
genus-$1$ $R$-matrix is the genus-$0$
rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic
Weierstrass function, exactly as predicted by the shadow obstruction tower:
the genus-$1$ period correction to the Casimir is controlled by
$G_2(\tau)$ and reproduces the curvature $\kappa\cdot\omega_1$
 succeeded in 53ms:
Drinfeld, ``Hamiltonian structures on Lie groups, Lie bialgebras and the geometric meaning of classical Yang--Baxter equations'' (Soviet Math.\ Dokl.\ 1983); Drinfeld (1986), Theorem~3.
\end{proof}

\begin{remark}[cross-volume check: level-stripped $r$-matrix]
\label{rem:qgf-ap126-level-check}
Passing from $U_q(\frakg)$ (finite type) to the affine quantum group $U_q(\hat{\frakg})$ at level $k$, Proposition~\ref{prop:qgf-classical-limit-r} acquires a level prefix: the classical limit produces
\begin{equation}
 r(z) = k \cdot \frac{\Omega_{\frakg}}{z} + O(\hbar, z^0),
 \label{eq:qgf-r-level-k}
\end{equation}
matching the Vol~I and Vol~II convention. Two sanity checks, mandatory after writing any $r$-matrix formula:
\begin{enumerate}[label=(\alph*)]
 \item At $k = 0$: the level-zero limit collapses the affine algebra to a loop algebra whose invariant form is identically zero, the classical $r$-matrix vanishes ($r(z) = 0$), and the universal $R$-matrix reduces to the identity $\cR(z) = 1$. This matches $\kappa_{\mathrm{ch}}^{\mathrm{KM}} = \dim(\frakg)(k + h^\vee)/(2 h^\vee) |_{k=0} = \dim(\frakg)/2$ reflected through the residue at $k = 0$ of the coefficient.
 \item At $k = -h^\vee$ (the critical level): $\kappa_{\mathrm{ch}}^{\mathrm{KM}}$ vanishes, the $R$-matrix degenerates, and the quantum group collapses to the classical enveloping algebra of the loop algebra. This is the Feigin--Frenkel regime.
\end{enumerate}
This principle caught repeated level-stripped affine pole terms; both (a) and (b) must be verified whenever an affine $r$-matrix is written.
\end{remark}

The spectral-parameter version extends Proposition~\ref{prop:qgf-qybe} to a family.
 succeeded in 52ms:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lll}
 \toprule
 Bar complex & Group action & Shadow data \\
 \midrule
 $B_{E_1}$ (ordered) & trivial ($1$) & full $R$-matrix $\cR(z)$, Yangian \\
 $B_{E_2}$ (braided) & braid group $B_n$ & $B_n$-equivariant tower, quantum group \\
 $B_{E_\infty}$ (symmetric) & symmetric $S_n$ & scalar $\kappa_{\mathrm{cat}}$, genus tower \\
 \bottomrule
\end{tabular}
\end{center}
Each tier retains strictly less information than the one above.
The averaging map $\mathrm{av}$ is the $B_n \twoheadrightarrow S_n$
projection applied to each degree. It is lossy: the $R$-matrix is
forgotten, and only its $S_2$-coinvariant $\kappa_{\mathrm{cat}}$
survives.
\end{remark}

\begin{example}[Braided structure for $K3$]
 succeeded in 51ms:
negative~$\kappa_{\mathrm{ch}}$.
\end{warning}

\begin{remark}[Holographic modular Koszul datum]
\label{rem:holo-koszul-k3xe}
\index{holographic modular Koszul datum!K3 x E}
$H(K3 \times E) = (A, A^!, C, r(z), \Theta_A,
\nabla^{\mathrm{hol}})$ with
$A = A_E$ ($c = 24$, $\kappa_{\mathrm{ch}} = 24$),
$A^! = A_E^!$ ($\kappa_{\mathrm{ch}} = -24$),
$C = Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ (universal bulk),
$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
$\Theta_A$ (bar-intrinsic MC element),
$\nabla^{\mathrm{hol}}$ (shadow connection, class~G).
\end{remark}

\begin{proposition}[Boundary-to-sigma ratio;
\ClaimStatusProvedHere]
\label{prop:boundary-sigma-ratio}
\index{modular characteristic!boundary vs sigma model}
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'KZ|Kazhdan|Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega/z|\\\\Omega/z' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '32,46p' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --glob '*.tex' 'k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega/\\(\\(k\\+2\\)z\\)|r_\\{?KZ\\}?\\(z\\).*k\\\\,?\\\\Omega/z|classical rational KZ connection|level-stripped' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:693:\item the boundary coupling $\hbar^{\mathrm{KZ}}$ in the Knizhnik--Zamolodchikov
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:702:The identification $\hbar^{\mathrm{KZ}} = \hbar^{\mathrm{DNP}} =
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:712:$1/n!$. In particular, the KZ parameter is conventionally normalized
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:933:generator, classical $r$-matrix, KZ connection, Gaudin model, Bethe
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex:1004:The genus-$1$ extension, identifying the KZB connection with the
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex:435: \item The Etingof--Kazhdan quantum vertex algebra (the genuinely
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:142:For each simply-laced Lie algebra $\mathfrak{g}$ of type $X_N \in \{A_N, D_N, E_6, E_7, E_8\}$, the Vol~III chiral algebra of the stabilized ADE Landau--Ginzburg model is isomorphic to the principal $\cW$-algebra of $\mathfrak{g}$ at a distinguished level $k_{\mathrm{ADE}}$ determined by the Kazhdan--Lusztig boundary of the semiclassical locus:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/matrix_factorizations.tex:173:On the $\cW$-algebra side, the principal $\cW$-algebra of $\mathfrak{sl}_2$ is the Virasoro vertex algebra at central charge $c(k) = 1 - 6(k+1)^2/(k+2)$ via the Drinfeld--Sokolov formula. The level $k_{A_1}$ distinguished by the Vol~III Kazhdan--Lusztig boundary of the semiclassical locus is the unique level for which the Virasoro output matches the modular characteristic $\kappa_{\mathrm{ch}} = \mu = 1$. Substituting $\kappa_{\mathrm{ch}}^{\mathrm{Vir}} = c/2$ (the Virasoro entry of the Vol~I kappa table) and $\kappa_{\mathrm{ch}} = 1$ forces $c = 2$ on the nominal Vir side; the semiclassical limit on the LG side is instead the free-fermion normalization $c = 1/2$, whose Vir-kappa is $1/4$ and whose two Clifford states account for the factor of two in Example~\ref{ex:mf-quadratic}. The two normalizations differ by a factor attributable to the Clifford stabilization, and Conjecture~\ref{conj:ade-w-algebra} for $A_1$ asserts their equality up to this normalization: the Vol~III chiral algebra is the free fermion at $c = 1/2$, i.e.\ the Ising chiral algebra in its free-fermion presentation, with two Clifford states matching the two-dimensional endomorphism algebra of Example~\ref{ex:mf-quadratic}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:9:%% $R$-matrix, the quantum Yang--Baxter equation, and the Kazhdan--Lusztig
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:37:under the Kazhdan--Lusztig equivalence (Theorem~\ref{thm:qgf-kazhdan-lusztig}).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:423: should recover $\Uq(\frakg)$ via the Kazhdan--Lusztig equivalence
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:493:At degree $3$: $\mathrm{av}(\Phi_{KZ}) = C$ (the cubic shadow of
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:524:$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/braided_factorization.tex:566:inversion, so $q \mapsto q^{-1}$. For the Kazhdan--Lusztig
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:6:Vol~III reads this material backwards. Instead of deforming $U(\frakg)$ first and discovering braiding later, it treats $U_q(\frakg)$ as an \emph{output} of the CY-to-chiral functor applied to a CY category whose Drinfeld center recovers the modular tensor category of conformal blocks. Everything below is classical and due to Drinfeld, Jimbo, Lusztig, Reshetikhin--Turaev, and Kazhdan--Lusztig; the Vol~III content is the organization around $\Phi$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:160:At generic $q$, the category $\Rep_q(\frakg)$ is equivalent as a braided monoidal category to the category $\Rep(\frakg)$ of finite-dimensional $\frakg$-modules equipped with the Drinfeld associator (built from the KZ connection) and the braiding induced by the classical $r$-matrix of Proposition~\ref{prop:qgf-classical-limit-r}.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:179:\begin{theorem}[Kazhdan--Lusztig equivalence]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:191:Kazhdan--Lusztig, ``Tensor structures arising from affine Lie algebras'' (I--IV, J.\ Amer.\ Math.\ Soc.\ 1993--1994); Finkelberg, ``An equivalence of fusion categories'' (GAFA 1996), closing the positive-level case. AP-CY5: the equivalence requires $q$ at a root of unity; at generic $q$ the two sides are no longer equivalent (the affine side does not even make sense as a finite modular category).
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
 succeeded in 56ms:
 \item Verdier duality $D_{\mathrm{Ran}}$ applied to the bar, producing the linear-dual algebra denoted $A^!$.
 \item Inversion, returning the original algebra up to quasi-isomorphism on the Koszul locus.
 \item The derived chiral center $Z^{\mathrm{der}}_{\mathrm{ch}}$, computed as chiral Hochschild cochains; this is the bulk.
\end{enumerate}
Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.

At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.

\begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
\label{conj:critical-self-dual}
Let $A = V_{-h^\vee}(\frakg)$ and write $A^!$ for the Verdier-dual chiral algebra $D_{\mathrm{Ran}}(B(A))$ of Volume~I Theorem~A. At the critical level the chiral-algebra inclusion $\mathfrak{z}(\hat{\frakg}) \hookrightarrow A$, combined with the Feigin--Frenkel isomorphism of Theorem~\ref{thm:feigin-frenkel-center}, implies (does not iff) the existence of a factorization-coalgebra map $\mathrm{Fun}(\mathrm{Op}_{G^L}(D)) \to B(A^!)$ on $\mathrm{Ran}(X)$. The conjecture is that this map is a quasi-isomorphism on the Volume~I Koszul locus. This is a statement about the Verdier leg of the four-functor picture, not about the inversion leg $\Omega \circ B$.
\end{conjecture}

The forward implication (Feigin--Frenkel implies a bar-coalgebra map) follows from Theorem~\ref{thm:feigin-frenkel-center} and the factorization construction of $\mathrm{Op}_{G^L}$. The converse (that the map is a quasi-isomorphism) is open.

 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:107:\begin{remark}[cross-volume check: level-stripped $r$-matrix]
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:119:This principle caught repeated level-stripped affine pole terms; both (a) and (b) must be verified whenever an affine $r$-matrix is written.
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.

thinking
**Inspecting geometric inconsistencies**

I'm thinking Vol III is mostly consistent, but there's a garbled sentence in geometric_langlands that stands out. I don't necessarily think it's a convention inconsistency. I might need to take a closer look at `cy_holographic_datum_master`, particularly around line 693, to see if it uses the KZ parameter differently. I'm curious whether a targeted search for `Omega/((k+h^\vee)z)` might clarify things. I'll dig into that next!
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|k\\\\,?\\\\Omega/z|r_\\{?KZ\\}?\\(z\\)|classical rational KZ connection|k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)' /Users/raeez/calabi-yau-quantum-groups/chapters/connections/cy_holographic_datum_master.tex /Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:




thinking
**Assessing inconsistencies**

I don't see any matches, which is likely okay. I might need to compute line numbers precisely using `nl -ba` for each issue. The candidate findings could be between 8 to 12, and I should read the exact line numbers, possibly checking for duplicates. Since the user wants inconsistencies across three repositories, I should report any duplicates I find. 

In Vol III, there aren't confirmed formula violations, just one critical descriptor issue. I’ll decide whether to include that inconsistency. I’ll also note if no strong findings exist. It’ll be vital to mention that there’s no direct trace-form mismatch in Vol III apart from one prose glitch, if included.
thinking
**Analyzing geometric discrepancies**

I’m noticing a genuine discrepancy in the geometric Langlands sentence. It mentions "(level-stripped r-matrix)" right before presenting the level-prefixed trace-form `kΩ/z`, which creates a local self-contradiction about the convention. I should classify this as LOW or MEDIUM severity. 

I’ll need to examine Vol III for any mention of `classical rational KZ connection`, but I couldn’t find it. I might also check `cy_holographic_datum_master` around line 693 for any related KZ parameters. The question seems to be about the consistency of r-matrix conventions, which probably fails due to Vol I and II, while Vol III is mostly consistent. I should inspect Vol II for potential issues as well, particularly in `ht_bulk_boundary_line_core.tex:3032`, where it discusses the trace-form and doesn’t equate the KZ connection directly with the coefficient.
thinking
**Considering KZ connection evaluation**

I'm pondering whether `The KZ connection` from evaluation modules could have `q = e^{iπ/(k+2)}` and if that creates a direct inconsistency. It might not need reporting after all. 

I should check `thqg_spectral_braiding_extensions.tex` around line 412 and the surrounding text. There’s a theorem presenting a hybrid formula with a double pole, which could be critical if it's a proven theorem. It's worth taking a closer look at that to clarify its implications.
exec
/bin/zsh -lc "sed -n '780,798p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1488,1505p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\index{classical r-matrix!pole structure comparison}
The pole structure of $r(z)$ at $z = 0$ encodes the conformal
spin content of the chiral algebra:
\begin{center}
\small
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{llll}
\textbf{Family} & \textbf{Highest pole} & \textbf{Source} &
\textbf{Shadow class} \\
\hline
$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
$\beta\gamma_\lambda$ & $1/z$ [Laplace] & contact OPE & $C$ \\
$\mathrm{Vir}_c$ & $c/(2z^4)$ [Laplace] & conformal anomaly $\lambda^3$ & $M$ \\
$\mathcal{W}_N$ & $c_{W_N}/z^{2N}$ [Laplace] & spin-$N$ self-OPE & $M$ \\
\end{tabular}
\end{center}
The pole order determines the leading behavior of the spectral
$R$-matrix near the collision singularity. The shadow class
exec
/bin/zsh -lc "sed -n '470,510p' chapters/connections/thqg_introduction_supplement_body.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '238,245p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '590,610p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '710,722p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7484,7554p' chapters/examples/yangians_drinfeld_kohno.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{equation}
where $\zeta(z|\tau)$ and $\wp(z|\tau)$ are the Weierstrass
zeta and $\wp$-functions with periods $1, \tau$. This is the
elliptic $r$-matrix of~\eqref{eq:elliptic-r-matrix} specialized
to $\widehat{\fg}_k$.
\end{theorem}

\begin{proof}
By Theorem~\ref{thm:elliptic-spectral-dichotomy}, the genus-$1$
$r$-matrix is obtained from the genus-$0$ $r$-matrix
$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
rational kernel functions by their elliptic counterparts:
$1/z \leadsto \zeta(z|\tau)$ and $1/z^2 \leadsto \wp(z|\tau)$.

The Bergman kernel on $E_\tau$ is
$B(z, w|\tau) = \wp(z-w|\tau)\, dz\, dw + 2\eta_1\, dz\, dw$,
where the correction $2\eta_1$ is the Legendre constant ensuring
the normalization $\int_{A} B(z, w) = 0$ (integration over the
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
 succeeded in 53ms:
$r^{\mathrm{cl}}\colon \fg \to \fg$ with antisymmetric part
$\Omega^{\mathrm{cl}} \in \fg \wedge \fg$. For
$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
at $k=0$) the antisymmetric
part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
Sklyanin Poisson structure on $\fg^*$ is then the Lie--Poisson
bracket twisted by~$\Omega$. Under the classical limit
$\mathrm{cl}\colon \cA \to \mathrm{gr}^{\mathrm{Li}}(\cA)$ of
Face~3, the chiral OPE pole structure of $\widehat{\fg}_k$ becomes
the Lie--Poisson bracket on $\fg^*$, and the binary collision
residue $r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$ becomes the
Lie--Poisson bracket twisted by $\Omega$. This is the Sklyanin
bracket up to the level normalization. The $\hbar \to 0$ statement
is Drinfeld's classical-limit theorem: the Yangian
$Y_\hbar(\fg) = \mathcal{U}(\fg[\![z^{-1}]\!])\otimes\mathbb{C}[\![\hbar]\!]$
quantizes the Sklyanin bracket, and the leading term in $\hbar$ of
the coproduct commutator recovers the Sklyanin bracket as a
classical Poisson structure on the dual. This is part~(i) of the
three-parameter $\hbar$ identification
 succeeded in 53ms:
MC element restricted to the genus-zero, two-point collision stratum
recovers the universal twisting morphism, with the geometric
realization~\eqref{eq:hdm-twisting-propagator}. The Koszul-dual
passage and the Yang--Baxter equation are
Theorem~\ref{thm:collision-residue-twisting}(ii) and
Theorem~\ref{thm:collision-depth-2-ybe}, respectively.
\end{proof}

 succeeded in 51ms:
 \ar@{<->}[r]
 \ar@{<->}[d]
& \{H_i^{\mathrm{GZ}}\}\;\textrm{(GZ26)}
 \ar@{<->}[d]^{\textrm{(F4)}}\\
\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
 \ar@{<->}[r]^-{\textrm{(F6)}}
& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
 \ar@{<->}[u]^{\textrm{(F5--F7)}}
}
\end{equation}

\begin{theorem}[Seven-way master theorem; \ClaimStatusProvedHere]
 succeeded in 52ms:
the open stratum $\mathrm{Conf}_n(\mathbb{P}^1) \subset
\overline{\mathcal{M}}_{0,n}$ as
\begin{equation}\label{eq:kz-from-shadow}
\nabla^{\mathrm{KZ}}
= d - \frac{1}{k + h^\vee}
 \sum_{1 \le i < j \le n}
 \Omega_{ij}\, d\log(z_i - z_j)
\end{equation}
after choosing an affine coordinate on $\mathbb{P}^1$ and
fixing $z_n = \infty$. Here $\Omega_{ij} = \sum_a T^a_i \otimes (T_a)_j$
is the Casimir operator acting on the $i$-th and $j$-th tensor factors
of $V_1 \otimes \cdots \otimes V_{n-1}$.

The KZ equation $\nabla^{\mathrm{KZ}} F = 0$ is therefore the
genus-$0$ flat-section equation of the shadow connection,
restricted to configuration space and evaluated in the representation
$V_1 \otimes \cdots \otimes V_n$ of $\fg^{\oplus n}$.

For $n = 4$ with all external legs in the fundamental representation
$V_{1/2}$ of $\mathfrak{sl}_2$, the KZ equation reduces to the

thinking
**Inspecting potential issues**

I think I need to report both because of a propagation failure. It might be a good idea to inspect `frontier_modular_holography_platonic` around key lines to figure out if any issues persist. My search shows both KZ and trace-form, and there might be some equality at k=1. It could be explicit bridging, or maybe I’m just getting confused. I'll definitely need to check between lines 1655-1713 and around 4731.
exec
/bin/zsh -lc "sed -n '1648,1718p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4404,4414p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4726,4770p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 indexed by the internal edges of the tree~$T$.

\item \emph{Color decoration via the R-matrix.}
 Passing from the free theory to an interacting
 chiral algebra~$\cA$ at level~$k$ dresses the
 bar-complex combinatorics with the classical
 r-matrix $r(z) = k\Omega/z$
 (which vanishes at $k = 0$, recovering the free case).
 The ordered bar $B^{\mathrm{ord}}(\cA)$ with its
 R-matrix twist encodes color-dressed amplitudes;
 the symmetric bar $B^{\Sigma}(\cA)$
 succeeded in 51ms:
 \kappa(\mathfrak{gl}_N,\, k{=}1)
 \;=\;
 \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
 \]
 The holographic R-matrix at level $k=1$ is
 $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
 $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
 $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
 twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
 The anomaly matching condition
 $\kappa_{\mathrm{eff}}
 = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$
 is a consistency check.

\item \emph{Sphere reconstruction.}
 The genus-$0$, $n$-point shadow amplitudes
 $\mathrm{Sh}_{0,n}(\Theta_\cA)$ are the Witten
 diagram amplitudes of the holomorphic twist. The
 commuting differentials of Gaiotto--Zinenko~\cite{GZ26}
 are the scalar shadow of $\mathrm{Sh}_{0,n}$.
exec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '390,405p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '6848,6884p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '575,606p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '714,719p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '520,540p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/genus1_seven_faces.tex | sed -n '973,1015p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_drinfeld_kohno.tex | sed -n '7542,7554p'" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
   390	\textbf{Part (i).} The affine Kac--Moody collision residue at
   391	genus~$1$ is
   392	$r_{\widehat{\fg}_k}^{(1)}(z, \tau) = k\,\Omega\, \zeta_\tau(z)/(k + h^\vee)$,
   393	by Theorem~\ref{thm:g1sf-elliptic-regularization} applied to the
   394	genus-$0$ collision residue
   395	$r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$
   396	(Theorem~\ref{thm:hdm-face-5}). Since affine Kac--Moody has
   397	$p_{\max} = 2$ and $k_{\max} = 1$ (the OPE has poles of order
   398	$2$ and $1$; the bar propagator absorbs one order), the
   399	collision expansion has $c_0 = k\,\Omega/(k+h^\vee)$ and $c_n = 0$ for
   400	$n \geq 1$. The
   401	elliptic regularization~\eqref{eq:g1sf-elliptic-expansion} therefore
   402	gives $r_{\widehat{\fg}_k}^{(1)} = c_0\, \zeta_\tau(z)$.
   403	Substituting into the Gaiotto--Zeng formula~\eqref{eq:hdm-face-4}
   404	of Face~4 produces~\eqref{eq:g1sf-kzb-z-component}, which is the
   405	$dz$-component of the KZB
 succeeded in 52ms:
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
   536	(Theorem~\ref{thm:shadow-connection-kz}).
   537	\end{proof}
   538	
   539	Face~5 is the historical face: the original spectral $r$-matrix that
 succeeded in 57ms:
  6848	\;\in\;
  6849	\mathfrak{g} \otimes \mathfrak{g}(z^{-1})
  6850	\;\subset\;
  6851	\cA^! \otimes \cA^!(z^{-1}),
  6852	\]
  6853	where $\Omega = \sum_a I^a \otimes I_a$ is the quadratic Casimir
  6854	tensor. Under the Kazhdan equivalence, this is identified with
  6855	the classical $r$-matrix
  6856	$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
  6857	\end{proposition}
  6858	
  6859	\begin{proof}
  6860	The CG structure on the bar complex of
  6861	$\hat{\mathfrak{sl}}_2$ at level~$k$ gives
  6862	$d_{\mathrm{bar}} = d_{\mathrm{int}} + [\tau, -]$ on
  6863	$\overline{C}_2^{\mathrm{ord}}(\bC)$, where the MC element~$\tau$
  6864	acts through the propagator $\eta_{12} = d\log(z_1 - z_2)$
  6865	tensored with the Lie-algebraic pairing.
  6866	The OPE
  6867	$J^a(z_1) J^b(z_2) \sim k\delta^{ab}/(z_1-z_2)^2
 succeeded in 60ms:
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
   592	$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
   593	at $k=0$) the antisymmetric
   594	part is the symmetric Casimir $\Omega = \sum_a J^a \otimes J^a$,
 succeeded in 53ms:
   973	intermediate trigonometric $r$-matrix:
   974	$r^{\mathrm{ell}} \to r^{\mathrm{trig}} \to r^{\mathrm{rat}}$.
   975	The collision residue~\eqref{eq:g1sf-elliptic-rmatrix} inherits
   976	the level normalization:
   977	$r^{(1)}_{\widehat{\fg}_k}(z, \tau) \to k\,\Omega/((k+h^\vee)z)$.
   978	At the critical level $k = -h^\vee$ the normalized rational
   979	$r$-matrix is singular; at $k = 0$ the collision residue
   980	$r^{(1)}_{\widehat{\fg}_k}$ vanishes identically \item \textup{(}Elliptic Gaudin $\to$ rational Gaudin.\textup{)}
   981	$H_i^{\mathrm{ell}} \to H_i^{\mathrm{Gaudin}}$, the standard rescaled
   982	Gaudin Hamiltonian of Theorem~\ref{thm:hdm-face-7}.
   983	\end{enumerate}
   984	In particular, the genus-$1$ master
   985	equation~\eqref{eq:g1sf-master-equation} degenerates to the genus-$0$
   986	master equation~\eqref{eq:hdm-master-equation} in the limit
   987	$q \to 0$.
   988	\end{theorem}
   989	
   990	\begin{proof}
   991	As $\operatorname{Im}(\tau) \to \infty$, $q = e^{2\pi i\tau} \to 0$,
   992	and the Weierstrass functions have the standard degenerations. The
 succeeded in 58ms:
   714	\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
   715	 \ar@{<->}[r]^-{\textrm{(F6)}}
   716	& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
   717	& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
   718	 \ar@{<->}[u]^{\textrm{(F5--F7)}}
   719	}
 succeeded in 58ms:
  7542	$A_{ij} = \Omega_{ij}/(k + h^\vee)$.
  7543	
  7544	The factor $1/(k + h^\vee)$ arises as follows. The bar propagator
  7545	$\eta_{ij} = d\log(z_i - z_j)$ enters the MC element $\Theta_\cA$
  7546	at degree~$2$, and the collision residue
  7547	$r(z) = k\Omega/z$ (Proposition~\ref{prop:affine-propagator-matching})
  7548	carries a factor of~$k$. The shadow connection divides by the
  7549	modular characteristic $\kappa = \dim(\fg)(k+h^\vee)/(2h^\vee)$ to
  7550	normalize to a flat connection; for the KZ connection the
  7551	conventional normalization is $1/(k + h^\vee)$, which follows from
  7552	the relation $r(z)/\kappa = \Omega/(z(k+h^\vee))$ after
  7553	accounting for the $\dim(\fg)/(2h^\vee)$ factor in the Casimir
  7554	normalization.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '150,190p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1554,1577p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '790,796p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '396,418p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '1732,1746p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   150	
   151	\begin{definition}[Strict rational dg-shifted Yangian]% label removed: def:strict-yangian
   152	A \emph{strict rational dg-shifted Yangian} consists of the following data:
   153	\begin{enumerate}[label=\textup{(\alph*)}]
   154	 \item an associative dg algebra $Y$;
   155	 \item a degree-zero derivation $T$ (the translation operator);
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
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '1194,1203p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex | sed -n '1432,1450p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex | sed -n '1494,1501p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex | sed -n '150,190p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1554	\begin{computation}[Formal $R$-matrix expansion; \ClaimStatusProvedHere]
  1555	\label{comp:formal-R-expansion}
  1556	\index{R-matrix@$R$-matrix!formal expansion}
  1557	The formal monodromy operator, equivalently the asymptotic $R$-matrix,
  1558	admits the $z^{-1}$-expansion (with $\Omega$ denoting the Sugawara-normalized
  1559	residue tensor $k\,\Omega_{\mathrm{Cas}}/(k+h^\vee)$ absorbing the level prefix and the level-explicit form at~\eqref{eq:R-level-explicit} below)
  1560	\begin{equation}\label{eq:R-formal-expansion}
  1561	 R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots
  1562	 \;=\; \exp\!\Bigl(\frac{\Omega}{z}\Bigr)\quad (\text{leading order}).
  1563	\end{equation}
  1564	More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
  1565	and corrections of order $O(z^{-3})$ arise from the non-abelian exponentiation
  1566	(Magnus series). On $V\otimes V$ one can diagonalize:
  1567	\[
  1568	 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
  1569	 \qquad
  1570	 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
  1571	\]
  1572	The leading-order formula
  1573	\begin{equation}\label{eq:R-level-explicit}
 succeeded in 51ms:
   790	$\cH_k$ & $k/z^2$ [Laplace] & $\lambda$-bracket $k\lambda$ & $G$ \\
   791	$\widehat{\fg}_k$ & $k\,\Omega/z + k\kappa/z^2$ [Laplace] & structure constants $f^{ab}_c$ & $L$ \\
   792	$\beta\gamma_\lambda$ & $1/z$ [Laplace] & contact OPE & $C$ \\
   793	$\mathrm{Vir}_c$ & $c/(2z^4)$ [Laplace] & conformal anomaly $\lambda^3$ & $M$ \\
   794	$\mathcal{W}_N$ & $c_{W_N}/z^{2N}$ [Laplace] & spin-$N$ self-OPE & $M$ \\
   795	\end{tabular}
   796	\end{center}
 succeeded in 51ms:
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
   414	contribution.
   415	\end{theorem}
 succeeded in 51ms:
  1732	 + \frac{k\,\Omega}{k+2}\bigl(2G_2(\tau)-\wp(z;\tau)-\pi^2/3\bigr),
  1733	\]
  1734	where the Eisenstein correction $G_2(\tau)$ accounts for the
  1735	(conditionally convergent) sum and $\wp$ is the Weierstrass
  1736	$\wp$-function. = k\,\Omega/((k+h^\vee)z)$; the intrinsic
  1737	KZB connection~\eqref{eq:kzb-connection} retains the standard
  1738	Sugawara normalization $(k+h^\vee)^{-1}$, so the identification of
  1739	$r_1$ with the connection form carries the rescaling factor
  1740	$k/(k+h^\vee)$. At $k=0$ both the connection trivializes in the
  1741	collision sector and $r_1$ vanishes, consistent with
  1742	Theorem~\ref{thm:affine-monodromy-identification}.) Thus the
  1743	genus-$1$ $R$-matrix is the genus-$0$
  1744	rational $R$-matrix $k\,\Omega/((k+2)z)$ dressed by the elliptic
  1745	Weierstrass function, exactly as predicted by the shadow obstruction tower:
  1746	the genus-$1$ period correction to the Casimir is controlled by
 succeeded in 51ms:
  1432	% label removed: comp:formal-R-expansion
  1433	\index{R-matrix@$R$-matrix!formal expansion}
  1434	The formal monodromy operator, equivalently the asymptotic $R$-matrix,
  1435	admits the $z^{-1}$-expansion
  1436	\begin{equation}% label removed: eq:R-formal-expansion
  1437	 R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots
  1438	 \;=\; \exp\!\Bigl(\frac{\Omega}{z}\Bigr)\quad (\text{leading order}).
  1439	\end{equation}
  1440	More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
  1441	and corrections of order $O(z^{-3})$ arise from the non-abelian exponentiation
  1442	(Magnus series). On $V\otimes V$ one can diagonalize:
  1443	\[
  1444	 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
  1445	 \qquad
  1446	 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
  1447	\]
  1448	The leading-order formula $R(z)=1+k\,\Omega/z+O(z^{-2})$
  1449	at level~$k$ identifies $k\,\Omega$ as the collision residue, consistent with
  1450	Lemma~\ref{lem:inf-braid}.
 succeeded in 51ms:
  1194	truncation level.
  1195	
  1196	For $\cA = \widehat{\fg}_k$: the classical Yangian $Y(\fg)$ is
  1197	recovered from the genus-$0$ projection of $Y_T^{\mathrm{mod}}$.
  1198	The $R$-matrix $R(z) = 1 + \hh\, \Omega/((k+h^\vee)z)
  1199	+ O(\hh^2)$ deforms to the quantum Yangian $R$-matrix
  1200	$R^{\mathrm{qu}}(z) = (z + \hh\,P)/(z - \hh)$ by resumming the
  1201	genus expansion to all orders.
  1202	\end{corollary}
  1203	
 succeeded in 51ms:
  1494	
  1495	\begin{proof}
  1496	By Theorem~\ref{thm:elliptic-spectral-dichotomy}, the genus-$1$
  1497	$r$-matrix is obtained from the genus-$0$ $r$-matrix
  1498	$r_0(z) = \Omega/((k+h^\vee)z) + k\kappa/z^2$ by replacing the
  1499	rational kernel functions by their elliptic counterparts:
  1500	$1/z \leadsto \zeta(z|\tau)$ and $1/z^2 \leadsto \wp(z|\tau)$.
  1501	
 succeeded in 51ms:
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
   160	 \]
   161	\end{enumerate}
   162	\end{definition}
   163	
   164	The datum $(Y,r,T)$ is the strict shadow of the full $A_\infty$ structure treated later.
   165	
   166	\section{The strict logarithmic theory: the shifted KZ/FM connection}\label{sec:strict}
   167	
   168	We begin with the strict theory because it exposes the geometric heart of the subject with maximal clarity: pairwise collisions, logarithmic poles, and Yang-Baxter flatness.
   169	
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex | sed -n '34,42p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex | sed -n '107,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    34	 \item The derived chiral center $Z^{\mathrm{der}}_{\mathrm{ch}}$, computed as chiral Hochschild cochains; this is the bulk.
    35	\end{enumerate}
    36	Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
    37	
    38	At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
    39	
    40	\begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
    41	\label{conj:critical-self-dual}
    42	Let $A = V_{-h^\vee}(\frakg)$ and write $A^!$ for the Verdier-dual chiral algebra $D_{\mathrm{Ran}}(B(A))$ of Volume~I Theorem~A. At the critical level the chiral-algebra inclusion $\mathfrak{z}(\hat{\frakg}) \hookrightarrow A$, combined with the Feigin--Frenkel isomorphism of Theorem~\ref{thm:feigin-frenkel-center}, implies (does not iff) the existence of a factorization-coalgebra map $\mathrm{Fun}(\mathrm{Op}_{G^L}(D)) \to B(A^!)$ on $\mathrm{Ran}(X)$. The conjecture is that this map is a quasi-isomorphism on the Volume~I Koszul locus. This is a statement about the Verdier leg of the four-functor picture, not about the inversion leg $\Omega \circ B$.
 succeeded in 52ms:
   107	\begin{remark}[cross-volume check: level-stripped $r$-matrix]
   108	\label{rem:qgf-ap126-level-check}
   109	Passing from $U_q(\frakg)$ (finite type) to the affine quantum group $U_q(\hat{\frakg})$ at level $k$, Proposition~\ref{prop:qgf-classical-limit-r} acquires a level prefix: the classical limit produces
   110	\begin{equation}
   111	 r(z) = k \cdot \frac{\Omega_{\frakg}}{z} + O(\hbar, z^0),
   112	 \label{eq:qgf-r-level-k}
   113	\end{equation}
   114	matching the Vol~I and Vol~II convention. Two sanity checks, mandatory after writing any $r$-matrix formula:
   115	\begin{enumerate}[label=(\alph*)]
   116	 \item At $k = 0$: the level-zero limit collapses the affine algebra to a loop algebra whose invariant form is identically zero, the classical $r$-matrix vanishes ($r(z) = 0$), and the universal $R$-matrix reduces to the identity $\cR(z) = 1$. This matches $\kappa_{\mathrm{ch}}^{\mathrm{KM}} = \dim(\frakg)(k + h^\vee)/(2 h^\vee) |_{k=0} = \dim(\frakg)/2$ reflected through the residue at $k = 0$ of the coefficient.
   117	 \item At $k = -h^\vee$ (the critical level): $\kappa_{\mathrm{ch}}^{\mathrm{KM}}$ vanishes, the $R$-matrix degenerates, and the quantum group collapses to the classical enveloping algebra of the loop algebra. This is the Feigin--Frenkel regime.
   118	\end{enumerate}
   119	This principle caught repeated level-stripped affine pole terms; both (a) and (b) must be verified whenever an affine $r$-matrix is written.
   120	\end{remark}
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex | sed -n '84,90p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    84	\label{rem:level-prefixed-r-matrix}
    85	The classical $r$-matrix attached to an affine Kac-Moody $E_1$-chiral algebra at level $k$ is
    86	\[
    87	 r(z) = \frac{k\,\Omega}{z},
    88	\]
    89	not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
    90	\end{remark}
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'k\\\\,?\\\\Omega/\\(\\(k\\+h\\"'^'"\\\\vee\\)z\\)|r_\\{?KZ\\}?\\(z\\) = k\\\\,?\\\\Omega/z|classical rational KZ connection' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '1652,1715p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '4728,4766p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:183:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1736:$\wp$-function. = k\,\Omega/((k+h^\vee)z)$; the intrinsic
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:412:$k\,\Omega/((k+h^\vee)z)$ carries the Lie-algebraic data; the double
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186:When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
chapters/connections/holographic_datum_master.tex:601:residue $r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$ becomes the
chapters/connections/genus1_seven_faces.tex:395:$r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$
chapters/connections/genus1_seven_faces.tex:450:$k\,\Omega/((k+h^\vee)z)$
chapters/connections/genus1_seven_faces.tex:977:$r^{(1)}_{\widehat{\fg}_k}(z, \tau) \to k\,\Omega/((k+h^\vee)z)$.
chapters/connections/genus1_seven_faces.tex:1010:rational $r$-matrix $k\,\Omega/((k+h^\vee)z)$ in the Kazhdan
chapters/connections/genus1_seven_faces.tex:1013:propagator $r_{\widehat{\fg}_k}(z) = k\,\Omega/((k+h^\vee)z)$\textup{)}.
 succeeded in 53ms:
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
  1668	\end{proof}
  1669	
  1670	\begin{theorem}[Three-parameter identification of $\hbar$;
  1671	\ClaimStatusProvedHere{} on the new three-parameter identification;
 succeeded in 51ms:
  4728	 \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  4729	 \]
  4730	 The holographic R-matrix at level $k=1$ is
  4731	 $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
  4732	 $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  4733	 $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  4734	 twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  4735	 The anomaly matching condition
  4736	 $\kappa_{\mathrm{eff}}
  4737	 = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$
  4738	 is a consistency check.
  4739	
  4740	\item \emph{Sphere reconstruction.}
  4741	 The genus-$0$, $n$-point shadow amplitudes
  4742	 $\mathrm{Sh}_{0,n}(\Theta_\cA)$ are the Witten
  4743	 diagram amplitudes of the holomorphic twist. The
  4744	 commuting differentials of Gaiotto--Zinenko~\cite{GZ26}
  4745	 are the scalar shadow of $\mathrm{Sh}_{0,n}$.
  4746	\end{enumerate}
  4747	\end{theorem}





thinking
**Inspecting findings and context**

I'm reviewing Volume III which shows medium to high findings. I need to check the exact wording around lines 116-117 in `quantum_groups_foundations`. I might also search for instances of `critical level` after examining trace form—using regex could be unnecessary. Additionally, I want to verify if `quantum_groups_foundations` explicitly mentions trace form and critical-level. I also should look at lines 693 and 717 in `cy_holographic_datum_master` for context. There's a possible inconsistency in diagram conventions that I'll note.
thinking
**Clarifying data on surfaces**

I’m considering how to relay information about the suspect surfaces. The user probably isn’t looking for fine details on semantics, so I could simplify it. I think saying "Instances checked: 18 unique suspect surfaces" might be most effective. It feels necessary to be honest, yet I want to make it easier to defend my count. So, unique suspect surfaces might indeed be 18.
thinking
**Checking unique suspect surfaces**

I'm calculating the actual unique suspect surfaces based on the formula-related issues. I've identified 22 instances, including various diagrams, constructions, and theorems. I think it's important to confirm if there are duplicates in previous volumes, just to be thorough. The output from searching indicates some hybrid patterns, like genus1_seven_faces and log_ht_monodromy_core. Also, there might be some mislabeling in the KZ, so I'll need to look into that further.
thinking
**Exploring possible searches**

I’m considering whether to ignore `ht_bulk_boundary_line_core` since there aren't any formula misstatements. I think it could be useful to search for files containing `classical rational KZ connection` and `Ω/z`. I already have `log_ht_monodromy` as part of my focus. It might also make sense to check Volumes I and II for the exact phrase `r_KZ = kΩ/z`, as I only found it in ydk so far. This might help clarify things further.
thinking
**Considering search options**

I’m thinking that I might not need to do this, but it could be helpful to run a more targeted search on Vol III, specifically for terms like "critical level," "r(z) = kΩ/z," or "level-stripped." I wonder if there's more information available using these focused keywords. Maybe I should try using `rg` to aid in my search as well. It feels like a more efficient approach, but do I really need to?
exec
/bin/zsh -lc "rg -n --glob '*.tex' '(critical level|level-stripped|kappa_\\{?ch\\}?|kappa_\\{?\\mathrm\\{ch\\}\\}?)["'^'"\\n]{0,200}(r\\(z\\) = k|Omega/z)|(r\\(z\\) = k|Omega/z)["'^'"\\n]{0,200}(critical level|level-stripped|kappa_\\{?ch\\}?|kappa_\\{?\\mathrm\\{ch\\}\\}?)' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:(critical level|level-stripped|kappa_\{?ch\}?|kappa_\{?\mathrm\{ch\}\}?)[^\n]{0,200}(r\(z\) = k|Omega/z)|(r\(z\) = k|Omega/z)[^\n]{0,200}(critical level|level-stripped|kappa_\{?ch\}?|kappa_\{?\mathrm\{ch\}\}?))
                                                              ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n --glob '*.tex' 'critical level|level-stripped|kappa_\\{\\\\mathrm\\{ch\\}\\}|kappa_\\{ch\\}|kappa_\\{\\\\mathrm\\{ch\\}\\}' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 634

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:283: algebras; at the critical level $k = -h^\vee$, this produces
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:500: \item $\kappa_{\mathrm{ch}}$: the modular characteristic computed
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:507: both $\kappa_{\mathrm{cat}}$ and $\kappa_{\mathrm{ch}}$).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:511:$\kappa_{\mathrm{ch}} = 3$, $\kappa_{\mathrm{BKM}} = 5$,
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:527:$\kappa_{\mathrm{ch}} + \kappa_{\mathrm{ch}}' = 0$ for KM/free fields (Volume~I, Theorem~C).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:137: \kappa_{\mathrm{ch}}(\text{conifold}) = 1.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:144:The conifold quiver has a single pair of bifundamental arrows. The OPE of the associated chiral algebra has poles of maximal order $2$ (simple pole in the $r$-matrix after the $d\log$ absorption ), so $S_r = 0$ for $r \geq 3$. The modular characteristic is $\kappa_{\mathrm{ch}} = \DT_{(1,0)} = 1$ (the single compact curve class).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:159: \item $\kappa_{\mathrm{ch}}(\text{local } \bP^2) = 3/2 = \chi(\bP^2)/2$, where $\chi(\bP^2) = 3$ is the topological Euler characteristic of the compact base.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:167:(i) The compact base $\bP^2$ contributes $\chi(\bP^2) = 3$ independent curve classes. The standard genus-$0$ DT computation gives $\kappa_{\mathrm{ch}} = \chi/2 = 3/2$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:189:\noindent\textit{Verification}: 77 tests in \texttt{local\_p2\_coha.py} covering $\kappa_{\mathrm{ch}}$-computation (3 paths), GV growth rate through degree $d = 15$, McKay quiver structure, and loop correction.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:199: \item $\kappa_{\mathrm{ch}}(\text{local } \bP^1 \times \bP^1) = 2 = \chi(\bP^1 \times \bP^1)/2$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:208:(i) The compact base $\bP^1 \times \bP^1$ has $\chi(\bP^1 \times \bP^1) = 4$ (each factor contributes $\chi(\bP^1) = 2$), so $\kappa_{\mathrm{ch}} = \chi/2 = 2$ by the general local-surface formula (Remark~\ref{rem:toric-structural-patterns}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:215:\noindent\textit{Verification}: 84 tests in \texttt{local\_p1p1\_coha.py} covering $\kappa_{\mathrm{ch}}$, diagonal shadow metric, symmetric/anti-symmetric depth classification, and GV invariants through bi-degree $(6,6)$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:279:\section{The $\kappa_{\mathrm{ch}}$-table for toric CY3}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:282:\begin{proposition}[$\kappa_{\mathrm{ch}}$-values for the standard toric CY3 family]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:288:Geometry & Quiver & $\kappa_{\mathrm{ch}}$ & Class & $r_{\max}$ \\
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:301:\begin{remark}[Patterns in the $\kappa_{\mathrm{ch}}$-table]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex:305: \item \emph{$\kappa_{\mathrm{ch}}$ from the compact base}: for local CY3 geometries of the form $X = \mathrm{Tot}(K_S \to S)$ over a smooth projective surface $S$, the modular characteristic is $\kappa_{\mathrm{ch}} = \chi(S)/2$, giving $\kappa_{\mathrm{ch}}(\text{local } \bP^2) = 3/2$ ($\chi(\bP^2) = 3$) and $\kappa_{\mathrm{ch}}(\text{local } \bP^1 \times \bP^1) = 2$ ($\chi(\bP^1 \times \bP^1) = 4$). For geometries not of the form $\mathrm{Tot}(K_S)$, the value is computed from DT invariants directly: $\kappa_{\mathrm{ch}}(\C^3) = 1$ (from the MacMahon plethystic logarithm) and $\kappa_{\mathrm{ch}}(\text{conifold}) = 1$ (from the single compact curve class). Note: the conifold is $\mathrm{Tot}(\cO(-1)^{\oplus 2} \to \bP^1)$, which is \emph{not} $\mathrm{Tot}(K_{\bP^1}) = \mathrm{Tot}(\cO(-2) \to \bP^1)$, so the $\chi(S)/2$ formula does not apply to it directly. %: this is chi(S)/2, NOT c/2 of the Virasoro subalgebra.


thinking
**Structuring the report**

I’m checking the violations and instances. It looks like I found 8 out of 22 instances needing a FAIL verdict. I think it's crucial to mention line numbers precisely. I’ll include the volume description, kind of like `[CRITICAL] Vol I chapters/...:578`. I might consider ordering by severity, with 2 CRITICAL, 4 HIGH, and 2 MEDIUM findings. Also, I’ll note that I only read and didn’t edit any files. To sum up, I’d say: `Instances checked: 22 | Violations found: 8 | Verdict: FAIL`.
thinking
**Summarizing key points**

In summary, Vol III's main theory files are consistent, though two frontier slips remain. The output contract doesn't limit us. I could mention that the most direct formula in Vol III aligns with the trace-form note in `e1_chiral_algebras.tex`. The failures noted are about local prose and critical-level drift, not a complete reversal of the formula. We should keep the final summary concise and state that 22 suspect surfaces were checked in context, without needing to define them. Good.
codex
[CRITICAL] Vol I `chapters/connections/holographic_datum_master.tex:578` — Core face-theorem surface is not convention-stable. The same chapter first derives the affine collision residue in KZ normalization as `\Omega/((k+h^\vee)z)` at `:522-530`, then states the Drinfeld/Sklyanin input as `k\Omega/z` at `:578-593`, then hybridizes them as `k\Omega/((k+h^\vee)z)` at `:601`, and finally places a bare `\Omega/z` in the seven-face master diagram at `:717`. These are not a single convention with an explicit bridge.

[CRITICAL] Vol I `chapters/connections/genus1_seven_faces.tex:395` — The genus-1/KZB lane imports the same hybrid formula `k\Omega/((k+h^\vee)z)` and then treats it as the KZ/KZB coefficient. The degeneration theorem repeats this at `:977`, `:1002`, `:1010`, and `:1013`, including the trace-form vanishing check `k=0` inside a KZ-normalized argument. This is a false theorem-level normalization, not just sloppy prose.

[HIGH] Vol II `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_spectral_braiding_extensions.tex:404` — A proved theorem states the affine simple pole as `k\Omega/((k+h^\vee)z)` with a separate `k\kappa/z^2` term. The same file later switches to `R(z)=1+\hbar\,\Omega/((k+h^\vee)z)+O(\hbar^2)` at `:1198`, and then to genus-0 `r_0(z)=\Omega/((k+h^\vee)z)+k\kappa/z^2` at `:1498`. One file is using three incompatible affine normalizations.

[HIGH] Vol II `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:183` — It says `r(z)=k\,\Omega/z` is “exactly the classical rational KZ connection,” which is the trace-form coefficient mislabeled as KZ. The same file then oscillates between an absorbed-residue bare expansion `R(z)=1+\Omega/z+\cdots` at `:1561`, an explicit `R(z)=1+k\Omega/z+\cdots` at `:1574`, and a hybrid `k\Omega/((k+h^\vee)z)` at `:1736-1744`. The non-core duplicate repeats the KZ mislabel at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy.tex:186`.

[HIGH] Vol I `chapters/examples/yangians_drinfeld_kohno.tex:6856` — A proposition identifies `r_{\mathrm{KZ}}(z)=k\,\Omega/z` as the KZ equation’s classical `r`-matrix, and the proof repeats that at `:6879`. Later the same chapter derives the actual KZ coefficient `1/(k+h^\vee)` only by dividing the trace-form residue by `\kappa` at `:7547-7552`. That is an unannounced convention swap.

[HIGH] Vol I `chapters/connections/frontier_modular_holography_platonic.tex:1680` — This downstream frontier surface repeats the core drift: it uses the trace-form `k\Omega/z` for the “level-k rational `r`-matrix,” but the same theorem immediately sets the collision-residue prefactor equal to `1/(k+h^\vee)` at `:1692` and writes `r(z)=\Omega/((k+h^\vee)z)` at `:1713`. Later it reverts to `k\Omega/z` again at `:4763`. The propagation failure is cross-section, not isolated.

[MEDIUM] Vol III `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/quantum_groups_foundations.tex:111` — This remark explicitly adopts the trace-form convention `r(z)=k\,\Omega/z`, but its critical-level check at `:117` says the `R`-matrix “degenerates,” which is KZ critical-level behavior, not trace-form behavior. The cross-volume checker is itself mixing the two conventions.

[MEDIUM] Vol III `/Users/raeez/calabi-yau-quantum-groups/chapters/connections/geometric_langlands.tex:38` — The sentence says “(level-stripped `r`-matrix)” and immediately writes the level-prefixed trace-form `r(z)=k\,\Omega/z`; it then argues that at `k=-h^\vee` the collision `r`-matrix is no longer the surviving structure. That imports KZ/`kappa`-collapse logic into a trace-form sentence and is locally self-contradictory.

## Summary
Instances checked: 22 | Violations found: 8 | Verdict: FAIL
tokens used
157,469
