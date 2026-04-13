# C01_bare_omega_v1 (356s)

Fixed the AP126 trace-form misses I found in the assigned Vol I chapter surface.

- PROBLEM at [preface_section1_v2.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:481): affine KM collision residue was written as `r(z)=\frac{\Omega}{z}`. EXACT edit applied: `r(z)=\frac{k\,\Omega}{z}`.

- PROBLEM at [preface_section1_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex:634): the same affine KM `R`-matrix draft lane omitted the level. EXACT edit applied: `r(z)=\frac{k\,\Omega}{z}`.

- PROBLEM at [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:542): the landscape table listed the affine KM `r(z)` entry as bare `\Omega/z`. EXACT edit applied: `k\Omega/z`.

- PROBLEM at [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:581): the Yangian row averaged a bare kernel as `\mathrm{av}(\Omega/z)`. EXACT edit applied: `\mathrm{av}(k\Omega/z)`.

- PROBLEM at [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:582): the Yangian row also listed bare `\Omega/z` in the `r(z)` column. EXACT edit applied: `k\Omega/z`.

- PROBLEM at [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4730): the D3 specialization exposed a bare equality `r(z)=k\Omega/z=\Omega/z`. EXACT edit applied: rewrote it to `r(z)=k\Omega/z`, with prose `at the D3 locus k=1 this specializes to the level-1 kernel`.

- PROBLEM at [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4764): the proof prose still exposed `1\cdot\Omega/z`. EXACT edit applied: rewrote it as `the level-1 specialization of k\Omega/z`.

Verification: `rg --pcre2` on the four touched files returned no remaining bare `\Omega/z`, `\frac{\Omega}{z}`, or `\mathrm{av}(\Omega/z)` spellings. I did not run a TeX build. The only remaining chapter-wide bare `\Omega/z` hits are the historical Drinfeld-normalization lane in [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:466) and [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:719), plus the separate `\Omega/z^3` Virasoro line in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27802).


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
session id: 019d8791-febc-7c61-a70c-24c57dfbe408
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


Fix ALL bare \Omega/z without level prefix in Vol I (AP126).
Run: grep -rn '\\Omega' chapters/ | grep -v 'k.*\\Omega\|level\|AP126' | head -40
For each: add the level prefix k. r(z) = k*\Omega/z, NOT \Omega/z.
mcp startup: no servers

thinking
**Clarifying prefix instructions**

The user asked me to add the level prefix `k*\Omega/z` carefully, as not all instances of \Omega/z should be changed depending on the KZ convention or quotient. However, the user specifically wants to fix bare instances of \Omega/z in Vol I AP126, particularly in trace-form sections. To proceed, I need to find all relevant occurrences using grep, verify the context to ensure I'm adding 'k' only where necessary, and read the relevant documentation first.
codex
I’m auditing the Vol I `\Omega/z` surface first, then I’ll patch only the offending chapter files with the minimum truthful `k\Omega/z` edits and verify no bare trace-form instances remain.
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2845 |
| Total tagged claims | 3673 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2845 |
 succeeded in 52ms:
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
**Announcing skill usage**

I think I need to announce that I'm using a specific skill. It seems like opening a multi-path verification skill might suffice for this task since it aligns well with the verification formula. I want to make sure I approach this correctly, so I'll go ahead and open the skill. This way, I can confirm that I'm on the right path for what needs to be done!
codex
Using `multi-path-verify` for this pass because the job is a formula-level audit with local proof-by-context before patching.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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


thinking
**Inspecting files and git status**

I need to inspect the grep results and the current git status since I suspect there might be some dirty files. I think it's important to check the relevant files carefully. The user asked for a specific search command, so I might need to run that exact grep command. I also want to be comprehensive, possibly using "rg" for searching Omega/z patterns. Checking the git status will help me identify any dirty files that might be relevant for the task.
codex
I’ve loaded the repo-level invariants and I’m on the exact AP126 surface now: find the bare trace-form `\Omega/z` hits, classify each by context, then patch only the true violations.
exec
/bin/zsh -lc "rg -n '\\\\Omega/z|\\\\Omega / z|\\\\frac\\{\\\\Omega\\}\\{z\\}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rn '\\\\Omega' chapters/ | grep -v 'k.*\\\\Omega\\|level\\|AP126' | head -40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
chapters/examples/w_algebras_deep.tex:2821: r^{\mathrm{KM}}(z) = k\,\Omega/z
chapters/examples/w_algebras_deep.tex:2867: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
chapters/examples/lattice_foundations.tex:5003:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
chapters/examples/lattice_foundations.tex:5018:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
chapters/examples/lattice_foundations.tex:5022:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
chapters/examples/bar_complex_tables.tex:3160: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
chapters/examples/bar_complex_tables.tex:3164: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
chapters/examples/free_fields.tex:444:$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
chapters/examples/genus_expansions.tex:76:%: canonical form r(z) = k\Omega/z; k=0 -> r=0
chapters/examples/genus_expansions.tex:80: k\Omega/z\bigr), \\
chapters/frame/preface_section1_v2.tex:481:r(z) \;=\; \frac{\Omega}{z}\,,
chapters/frame/preface_section1_v2.tex:491:\mathrm{av}\bigl(k\Omega/z\bigr)
chapters/frame/preface_section1_v2.tex:501:$r(z) = k\Omega/z$ to $\kappa(\widehat{\mathfrak g}_k)$ discards
chapters/frame/preface_sections5_9_draft.tex:542: & $\Omega/z$
chapters/frame/preface_sections5_9_draft.tex:581: & $\mathrm{av}(\Omega/z)$
chapters/frame/preface_sections5_9_draft.tex:582: & $\Omega/z$
chapters/frame/preface_sections5_9_draft.tex:608:poles. $R$-matrix: $r(z)=k\Omega/z$, the Casimir tensor of
chapters/frame/preface_sections5_9_draft.tex:683:the $R$-matrix $r(z)=k\Omega/z$ is the genus-$0$ binary shadow
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:779:\otimes \Omega^*_{\log})
chapters/theory/higher_genus_complementarity.tex:792:C}_n, \mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log}))
chapters/theory/higher_genus_complementarity.tex:863:\otimes \Omega^*_{\log})
chapters/theory/higher_genus_complementarity.tex:1037: \mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log}\bigr),
chapters/theory/higher_genus_complementarity.tex:1063:\omega \in \Omega^1_{\log}\bigl(\overline{C}_2(\Sigma_g)\bigr).
chapters/theory/higher_genus_complementarity.tex:1106:\mathcal{A}^{\boxtimes j} \otimes \Omega^*_{\log}\bigr).
chapters/theory/higher_genus_complementarity.tex:1198:\omega_{\overline{C}_n(X)} = K_{\overline{C}_n(X)} = \Omega^{n}_{\overline{C}_n(X)}
chapters/theory/higher_genus_complementarity.tex:1200:Here $\Omega^n_{\overline{C}_n(X)} = \bigwedge^n \Omega^1_{\overline{C}_n(X)}$ denotes the holomorphic line bundle of top-degree holomorphic forms (the canonical bundle), not the sheaf of smooth $n$-forms.
chapters/theory/higher_genus_complementarity.tex:1216:\emph{Logarithmic forms}: When we include logarithmic forms $\Omega^*_{\log}(
chapters/theory/higher_genus_complementarity.tex:1231:identifies $H^*(\Omega^*_{\log}(\overline{C}_n(X) \setminus D))
chapters/theory/higher_genus_complementarity.tex:1251:\Omega^*_{\log})\\
chapters/theory/higher_genus_complementarity.tex:1253:\otimes \Omega^*_{\log})
chapters/theory/higher_genus_complementarity.tex:1265:Combining with the Verdier pairing on $\Omega^*_{\log}$ from Theorem~\ref{thm:verdier-duality-config-complete}, we obtain:
chapters/theory/higher_genus_complementarity.tex:1409:R^q\pi_*^{\mathrm{ch}} \mathcal{A} \otimes \Omega^1_{\overline{\mathcal{M}}_g}(\log \partial)
chapters/theory/higher_genus_complementarity.tex:1420:\mathcal{A}|_{\Sigma_g} \otimes \Omega^1_{\Sigma_g} \to 0
chapters/theory/higher_genus_complementarity.tex:2356:\mathcal{A}^{\boxtimes (p+1)} \otimes \Omega^p(\log D))\]
chapters/theory/higher_genus_complementarity.tex:2882:\item Koszul dual algebra: $\mathcal{F}^! = \bar{B}(\mathcal{F})^\vee \cong \beta\gamma$ (linear dual of the bar coalgebra). Bar-cobar inversion gives $\Omega(\bar{B}(\mathcal{F})) \cong \mathcal{F}$ (recovers the fermion, not $\beta\gamma$).
chapters/theory/higher_genus_complementarity.tex:2990:\item Construct the bar complex $\bar{B}^{(g)}(\mathcal{A}) = \bigoplus_n \Gamma(\overline{C}_n(X_g), \mathcal{A}^{\boxtimes n} \otimes \Omega^*_{\log})$.
chapters/theory/higher_genus_complementarity.tex:3964:\[\text{DR}(\mathcal{M}) = R\Gamma(X, \Omega^\bullet_X \otimes_{\mathcal{D}_X} \mathcal{M})\]
chapters/theory/higher_genus_complementarity.tex:3986:&= R\Gamma(X, \Omega^\bullet_X \otimes_{\mathcal{D}_X} R\mathcal{H}om_{\mathcal{D}_X}(\mathcal{M}, \mathcal{D}_X \otimes \omega_X[d])) \\
 succeeded in 52ms:
 M CLAUDE.md
 M Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
 M N1_koszul_meta.pdf
 M N2_mc3_all_types.pdf
 M N3_e1_primacy.pdf
 M N4_mc4_completion.pdf
 M N5_mc5_sewing.pdf
 M N6_shadow_formality.pdf
 M bp_self_duality.pdf
 M chapters/connections/bv_brst.tex
 M chapters/connections/concordance.tex
 M chapters/connections/editorial_constitution.tex
 M chapters/theory/bar_cobar_adjunction_inversion.tex
 M chapters/theory/chiral_modules.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_foundations.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/introduction.tex
 M chapters/theory/ordered_associative_chiral_kd.tex
 M chiral_chern_weil.pdf

thinking
**Considering k=1 nuances**

I’m thinking about how to address k=1 in my response. Maybe I could add `1\cdot \Omega/z` or phrase it as "at k=1, \Omega/z," but the user wants a level prefix. I need to inspect the contexts more carefully. It might be helpful to use the explorer agent to search for authoritative sources, but I could also do the searching myself. The developer had mentioned preferring explorer agents for codebase-related questions.
codex
The first sweep found a mixed surface: genuine AP126 misses, plus `\hbar\Omega/z`, fixed-level specializations, and unrelated `\Omega` uses. I’m reading only the files with truly bare `\Omega/z` to avoid corrupting KZ or special-value statements.
collab spawn_agent(call_e65nC04gSOu4SCqjMmwR3aAy, prompt="Find bare `\Omega/z` or `\frac{\Omega}{z}` occurrences in `chapters/` that lack an explicit level prefix (`k`, `\hbar`, …")
spawn_agent(call_e65nC04gSOu4SCqjMmwR3aAy, prompt="Find bare `\Omega/z` or `\frac{\Omega}{z}` occurrences in `chapters/` that lack an explicit level prefix (`k`, `\hbar`, …") pending init:
  agent: 019d8792-c49a-7b51-bc3c-1092a7a6d8f3
mcp startup: no servers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\Omega/z\" chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\Omega/z)
       ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\Omega/z' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
chapters/examples/w_algebras_deep.tex:2821: r^{\mathrm{KM}}(z) = k\,\Omega/z
chapters/examples/w_algebras_deep.tex:2867: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
chapters/examples/lattice_foundations.tex:5003:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
chapters/examples/lattice_foundations.tex:5018:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
chapters/examples/lattice_foundations.tex:5022:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
chapters/examples/free_fields.tex:444:$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
chapters/examples/yangians_foundations.tex:1139:$r(z) = k\Omega/z$ (the double pole $k\,g^{ab}/(z{-}w)^2$
chapters/examples/yangians_foundations.tex:1142:equation for $r(z) = k\Omega/z$ reduces to the infinitesimal braid
chapters/examples/yangians_foundations.tex:1198:$G_2$ ($V = \bC^{7}$). The classical $r$-matrix $r(z) = k\Omega/z$
chapters/examples/yangians_foundations.tex:1213:$R$-matrix $r(z) = k\Omega/z$ of
chapters/examples/toroidal_elliptic.tex:2526:$r(z) = k_{\mathrm{eff}}\Omega/z$ (Casimir, $24$-dim; the
chapters/examples/bar_complex_tables.tex:3160: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
chapters/examples/bar_complex_tables.tex:3164: & $1$ & $\{2\}$ & $\{1\}$ & $k\Omega/z$ \\
chapters/examples/yangians_computations.tex:799:$r(z) = k\Omega/z$
chapters/examples/yangians_computations.tex:862:$r(z) = k\Omega/z$ of
chapters/examples/yangians_drinfeld_kohno.tex:6386:and $r^{\mathrm{KM}}(z) = k'\Omega/z$ is the collision $r$-matrix
chapters/examples/yangians_drinfeld_kohno.tex:6856:$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
chapters/examples/yangians_drinfeld_kohno.tex:6874:giving $r(z) = \tau|_{\deg 2} = k\,\Omega/z$,
codex
I’m narrowing the edit set to the actual AP126 violations now. The next step is a context read around each candidate file before I touch anything.
exec
/bin/zsh -lc "sed -n '628,660p' chapters/frame/preface_section1_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '470,510p' chapters/frame/preface_section1_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nP '(?<"'![A-Za-z0-9])'"\\\\Omega/z|\\\\frac\\{\\\\Omega\\}\\{z\\}' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '534,590p' chapters/frame/preface_sections5_9_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '450,730p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
product contributes the curvature~$\kappa$. The coexistence of
both poles, absent in the pure second-order-pole Heisenberg case,
makes $\widehat{\mathfrak g}_k$ the first nontrivial example.

The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
\[
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\]
where $\Omega$ is the Casimir tensor of~$\mathfrak g$. This is
matrix-valued: $\Omega \in \mathfrak g \otimes \mathfrak g$
carries the full Lie-algebraic structure. Averaging collapses the
Casimir to its trace:
\[
\mathrm{av}\bigl(k\Omega/z\bigr)
\;=\;
\frac{\dim(\mathfrak g)\cdot(k+h^\vee)}{2h^\vee}
\;=\;
\kappa(\widehat{\mathfrak g}_k).
 succeeded in 50ms:
The Lie bracket drives the tree-level bar differential
(the combinatorics of the Chevalley--Eilenberg complex); the inner
product supplies the curvature~$\kappa$. The coexistence of both
poles, absent in the Heisenberg case, makes
$\widehat{\mathfrak g}_k$ the first nontrivial example.

\medskip
\noindent\textbf{The Casimir $R$-matrix.}\enspace
The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
collision residue
\begin{equation}\label{eq:pf1-km-rmatrix}
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\end{equation}
where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
tensor. This is matrix-valued: $\Omega$ carries the full
Lie-algebraic structure that was invisible in the Heisenberg
scalar~$k/z$. The averaging map collapses the Casimir to a
scalar:
 succeeded in 50ms:
chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
chapters/examples/w_algebras_deep.tex:2821: r^{\mathrm{KM}}(z) = k\,\Omega/z
chapters/examples/w_algebras_deep.tex:2867: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
chapters/examples/toroidal_elliptic.tex:2526:$r(z) = k_{\mathrm{eff}}\Omega/z$ (Casimir, $24$-dim; the
chapters/examples/yangians_drinfeld_kohno.tex:6386:and $r^{\mathrm{KM}}(z) = k'\Omega/z$ is the collision $r$-matrix
chapters/examples/yangians_drinfeld_kohno.tex:6856:$r_{\mathrm{KZ}}(z) = k\,\Omega/z$ of the KZ equation.
chapters/examples/yangians_drinfeld_kohno.tex:6874:giving $r(z) = \tau|_{\deg 2} = k\,\Omega/z$,
chapters/examples/yangians_drinfeld_kohno.tex:6879:$r$-matrix $r_{\mathrm{KZ}}(z) = k\,\Omega/z$, confirming the
chapters/frame/preface_section1_v2.tex:481:r(z) \;=\; \frac{\Omega}{z}\,,
chapters/frame/preface_section1_draft.tex:634:r(z) \;=\; \frac{\Omega}{z}\,,
chapters/examples/free_fields.tex:444:$r(z) = k\,\Omega/z$ (a simple pole after $d\log$ absorption).
chapters/frame/preface_sections5_9_draft.tex:542: & $\Omega/z$
chapters/frame/preface_sections5_9_draft.tex:581: & $\mathrm{av}(\Omega/z)$
chapters/frame/preface_sections5_9_draft.tex:582: & $\Omega/z$
chapters/frame/preface.tex:793:the passage from $r(z) = k\,\Omega/z$ to
chapters/frame/preface.tex:1219:affine Kac--Moody, $r(z) = k\,\Omega/z$ is matrix-valued; the
chapters/frame/preface.tex:3050:$R$-matrix $r(z) = k\,\Omega/z$ is matrix-valued: the Casimir
chapters/frame/preface.tex:3061:deconcatenation coproduct evaluated on $r(z) = k\,\Omega/z$.
chapters/frame/preface.tex:3276:$R$-matrix $r(z) = k\,\Omega/z$ as the genus-$0$ binary
 succeeded in 51ms:
 & $k/z$
 & $2$
 & G
 & $0$
 & Gaussian archetype\\[2pt]
$\widehat{\fg}_k$
 & $J^a$ (wt~$1$)
 & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\Omega/z$
 & $3$
 & L
 & $0$
 & FF center at $k{=}{-}h^\vee$\\[4pt]
$\mathrm{Vir}_c$
 & $T$ (wt~$2$)
 & $c/2$
 & $\frac{c/2}{z^3}+\frac{2T}{z}$
 & $\infty$
 & M
 & $13$
 succeeded in 51ms:
operators is governed by the collision depth, which equals
$p_{\max}(\cA) - 1$: trivial for $\beta\gamma$ ($k_{\max} = 0$),
multiplication operators for affine Kac--Moody and Heisenberg
($k_{\max} = 1$), and genuine differential operators of order
$\geq 2$ for Virasoro and $\Walg_N$ ($k_{\max} \geq 3$).

\section{Face 5: the Yangian $r$-matrix of Drinfeld}
\label{sec:hdm-face-5}

The original spectral $r$-matrix is Drinfeld's~\cite{Drinfeld85},
introduced in connection with the quantum Yang--Baxter equation and
the Yangian deformation $Y_\hbar(\fg)$ of the universal enveloping
algebra of a simple Lie algebra~$\fg$. The classical $r$-matrix
\begin{equation}\label{eq:hdm-drinfeld-rmatrix}
r^{\mathrm{Dr}}(z)
\;=\;
\frac{\Omega}{z}
\;\in\;
\fg \otimes \fg [\![z^{-1}]\!],
\qquad

thinking
**Inspecting code lines**

I need to take a closer look around line 719 and 976 in the code, particularly with the tables. There might be some issues or inconsistencies that need addressing. It’s possible there are more bare forms further down, but I want to focus on these lines first to see what I can find. Okay, let's dive in and see if there’s anything that stands out in those sections!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\frac\\{\\\\Omega\\}\\{z\\}' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/frame/preface_section1_v2.tex:481:r(z) \;=\; \frac{\Omega}{z}\,,
chapters/frame/preface_section1_draft.tex:634:r(z) \;=\; \frac{\Omega}{z}\,,
chapters/connections/holographic_datum_master.tex:466:\frac{\Omega}{z}
chapters/connections/holographic_datum_master.tex:719:& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
codex
The main ambiguous file is `holographic_datum_master.tex`: it mixes a historical Drinfeld normalization with the repo’s level-prefixed trace-form normalization. I’m reading those local passages before deciding whether to convert, restate, or leave them.
exec
/bin/zsh -lc "sed -n '960,1010p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,740p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4718,4770p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
We assemble the seven faces into a single equation. Let $\cA$ be a
modular Koszul chiral algebra, and let $r_\cA(z)$ be the collision
residue of $\Theta_\cA$. The seven-face master theorem asserts that
the following diagram commutes:
\begin{equation}\label{eq:hdm-master-diagram}
\xymatrix{
\pi_\cA \in \mathrm{Tw}(\barBch(\cA), \cA)
 \ar@{<->}[r]^-{\textrm{(F1)}}
 \ar@{<->}[d]_{\textrm{(F3)}}
& r^{\mathrm{DNP}}(z) \in \cA^! \otimes \cA^! [\![z^{-1}]\!]
 \ar@{<->}[d]^{\textrm{(F2)}}\\
\{\cdot_\lambda \cdot\}\;\textrm{(KZ25)}
 \ar@{<->}[r]
 \ar@{<->}[d]
& \{H_i^{\mathrm{GZ}}\}\;\textrm{(GZ26)}
 \ar@{<->}[d]^{\textrm{(F4)}}\\
\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
 \ar@{<->}[r]^-{\textrm{(F6)}}
& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
 succeeded in 52ms:
formal parameter~$\hbar$ that controls the deformation from
classical to quantum. In the present framework, $\hbar$ admits
three independent identifications, each corresponding to a different
face of the collision residue.

\begin{theorem}[Three-parameter $\hbar$ identification; \ClaimStatusProvedElsewhere]
\label{thm:hdm-hbar-three-identification}
\index{$\hbar$!three identifications|textbf}
For $\cA = \widehat{\fg}_k$, the formal parameter $\hbar$ that
deforms the Sklyanin Poisson bracket into the Yangian
$Y_\hbar(\fg)$ admits the following three identifications:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Inverse level:} $\hbar = 1/(k + h^\vee)$, where the
 $k \to \infty$ limit is the classical limit and the
 $k \to -h^\vee$ limit is the critical-level Gaudin limit.
\item \emph{Inverse spectral parameter:} $\hbar = 1/z$ in the formal
 expansion $r^{\mathrm{Dr}}(z) = k\Omega/z = k\Omega \cdot \hbar$
 (level-$k$ form, vanishing at $k=0$),
 with the $z \to \infty$ limit identifying classical with quantum
 at large separation.
 succeeded in 51ms:
\nabla^{\mathrm{hol}})
\]
is computed for two brane systems:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{D3 brane \textup{(}twisted $\mathcal{N} = 4$ SYM\textup{)}.}
 The boundary chiral algebra is affine
 $\mathfrak{gl}_N$ at level $k = 1$:
 \[
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '450,520p' chapters/frame/preface_section1_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
normalised so that long roots have squared length~$2$. Both poles
are present. The first-order pole carries the Lie bracket
$J^a_{(0)}J^b = f^{ab}{}_{c}J^c$; the second-order pole carries
the invariant inner product
$J^a_{(1)}J^b = k\,\kappa^{ab}\cdot\mathbf 1$.

The bar complex of $\widehat{\mathfrak g}_k$ has nontrivial
contributions at all tensor degrees: the first-order pole generates
structure constants from tree-level OPE contractions, and the
second-order pole contributes the metric data. The chiral bracket
decomposes:
\begin{equation}\label{eq:pf1-km-bracket}
\mu^{\mathrm{ch}}
\;=\;
\underbrace{f^{ab}{}_{c}\,J^c\cdot\eta_{12}}_{\text{Lie bracket
(first-order pole)}}
\;+\;
\underbrace{k\,\kappa^{ab}\cdot\mathbf 1\cdot
d\eta_{12}}_{\text{inner product (second-order pole)}}.
\end{equation}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '600,660p' chapters/frame/preface_section1_draft.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\frac{f^{ab}{}_{c}\,J^c(w)}{z-w}
\;+\;
\frac{k\,\kappa^{ab}}{(z-w)^2}\,,
\]
where $f^{ab}{}_{c}$ are the structure constants of the simple Lie
algebra~$\mathfrak g$ and $\kappa^{ab}$ is the Killing form
normalised so that long roots have squared length~$2$. Both poles
are present: the first-order pole carries the Lie bracket
$J^a_{(0)}J^b=f^{ab}{}_{c}J^c$; the second-order pole carries
the invariant inner product
$J^a_{(1)}J^b=k\,\kappa^{ab}\cdot\mathbf 1$. The bar complex
of $\widehat{\mathfrak g}_k$ has nontrivial contributions
at all tensor degrees: the first-order pole generates structure
constants at tensor degree~$n$ from tree-level OPE contractions,
and the second-order pole contributes the metric/curvature data.

The bracket and curvature decomposition:
\[
\mu^{\mathrm{ch}}
\;=\;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '430,500p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the $i$-th and $j$-th marked points: see~\eqref{eq:hdm-twisting-propagator}.
The summation over $j \neq i$ produces the Hamiltonian on the
$n$-point sphere because the modular shadow connection
$\nabla^{\mathrm{hol}}_{0,n} = d - \mathrm{Sh}_{0,n}(\Theta_\cA)$
is built precisely from these binary collision residues
(Theorem~\ref{thm:sphere-reconstruction}(i)). The commutativity
$[H_i^{\mathrm{GZ}}, H_j^{\mathrm{GZ}}] = 0$ is the flatness
$(\nabla^{\mathrm{hol}}_{0,n})^2 = 0$, which follows from the
infinitesimal braid relation
(Theorem~\ref{thm:collision-depth-2-ybe}) and the Arnold relation
on $\overline{\cM}_{0,n}$. The order $k_{\max}(\cA) - 1$ of
$H_i^{\mathrm{GZ}}$ as a differential operator is the operator-order
trichotomy of Chapter~\ref{ch:three-invariants}, controlled by the
collision depth.
\end{proof}

Face~4 is the second-order differential incarnation of the
collision residue: where Faces~1--3 produce algebraic objects
(morphisms, $r$-matrices, brackets), Face~4 produces commuting
differential operators on a moduli space. The order of these
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '700,740p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
We assemble the seven faces into a single equation. Let $\cA$ be a
modular Koszul chiral algebra, and let $r_\cA(z)$ be the collision
residue of $\Theta_\cA$. The seven-face master theorem asserts that
the following diagram commutes:
\begin{equation}\label{eq:hdm-master-diagram}
\xymatrix{
\pi_\cA \in \mathrm{Tw}(\barBch(\cA), \cA)
 \ar@{<->}[r]^-{\textrm{(F1)}}
 \ar@{<->}[d]_{\textrm{(F3)}}
& r^{\mathrm{DNP}}(z) \in \cA^! \otimes \cA^! [\![z^{-1}]\!]
 \ar@{<->}[d]^{\textrm{(F2)}}\\
\{\cdot_\lambda \cdot\}\;\textrm{(KZ25)}
 \ar@{<->}[r]
 \ar@{<->}[d]
& \{H_i^{\mathrm{GZ}}\}\;\textrm{(GZ26)}
 \ar@{<->}[d]^{\textrm{(F4)}}\\
\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
 \ar@{<->}[r]^-{\textrm{(F6)}}
& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
collab wait(call_ixwDex6gm1LQjlJdAouaBgYU)
  receivers: 019d8792-c49a-7b51-bc3c-1092a7a6d8f3
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\Omega/z' chapters | grep -v 'k\\\\Omega/z' | grep -v '\\\\hbar\\\\Omega/z' | grep -v '\\\\mathrm{av}(\\\\Omega/z)' | grep -v 'kappa'}" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:
zsh:1: parse error near `}'
wait(call_ixwDex6gm1LQjlJdAouaBgYU) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python - <<'PY'
import pathlib, re
root = pathlib.Path('chapters')
for path in sorted(root.rglob('*.tex')):
    text = path.read_text()
    for m in re.finditer(r'\\\\Omega/z', text):
        start = m.start()
        line_no = text.count('\\n', 0, start) + 1
        line = text.splitlines()[line_no-1]
        prefix = text[max(0, start-10):start]
        snippet = line.strip()
        print(f\"{path}:{line_no}:{snippet}\")
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 51ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import pathlib, re
root = pathlib.Path('chapters')
for path in sorted(root.rglob('*.tex')):
    text = path.read_text()
    for m in re.finditer(r'\\\\Omega/z', text):
        start = m.start()
        line_no = text.count('\\n', 0, start) + 1
        line = text.splitlines()[line_no-1]
        snippet = line.strip()
        print(f\"{path}:{line_no}:{snippet}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/arithmetic_shadows.tex:2847:$r(z) = k\,\Omega/z$ with
chapters/connections/arithmetic_shadows.tex:2885:The identification $r(z) = k\,\Omega/z$ with Casimir
chapters/connections/bv_brst.tex:2417:r^{\mathrm{KM}}(z) = k\,\Omega/z,
chapters/connections/frontier_modular_holography_platonic.tex:1680:level-$k$ rational $r$-matrix $r^{\mathrm{cl}}(z) = k\Omega/z$
chapters/connections/frontier_modular_holography_platonic.tex:4410:r-matrix $r(z) = k\Omega/z$
chapters/connections/frontier_modular_holography_platonic.tex:4731:$r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
chapters/connections/frontier_modular_holography_platonic.tex:4731:$r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
chapters/connections/frontier_modular_holography_platonic.tex:4732:$k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
chapters/connections/frontier_modular_holography_platonic.tex:4763:The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
chapters/connections/frontier_modular_holography_platonic.tex:4764:$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
chapters/connections/holographic_datum_master.tex:578:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
chapters/connections/holographic_datum_master.tex:592:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
chapters/connections/holographic_datum_master.tex:976:expansion $r^{\mathrm{Dr}}(z) = k\Omega/z = k\Omega \cdot \hbar$
chapters/connections/holographic_datum_master.tex:1000:$r^{\mathrm{Dr}}(z) = \hbar \Omega/z + \mathcal{O}(\hbar^2)$ in the
chapters/connections/holomorphic_topological.tex:469:\item $r_T(z) = k\,\Omega/z$ (rational $r$-matrix: level $k$ survives $d\log$ absorption).
chapters/connections/holomorphic_topological.tex:930:$r(z) = k\,\Omega/z$
chapters/connections/thqg_introduction_supplement_body.tex:487:algebra~$\mathfrak{g}$ at level~$k$ (that is, $r(z) = k\,\Omega/z$ where
chapters/connections/thqg_introduction_supplement_body.tex:1277:rational $r$-matrix $r(z) = k\,\Omega/z$ generates the RTT presentation
chapters/connections/thqg_preface_supplement.tex:1178:$r(z)=k\,\Omega/z$, the full Casimir element at level~$k$. For Virasoro:
chapters/connections/thqg_preface_supplement.tex:1549:$[r,r]=[k\,\Omega/z_1,k\,\Omega/z_2]$, which reduces to
codex
I’ve isolated the obvious draft-preface misses. I’m checking whether the remaining chapter hits are actual AP126 defects or deliberate fixed-level/historical normalizations that need a wording repair instead of a blind `k` insertion.
exec
/bin/zsh -lc "sed -n '520,615p' chapters/frame/preface_sections5_9_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\mathrm\\{av\\}\\(\\\\Omega/z\\)|\\\\frac\\{\\\\Omega\\}\\{z\\}|= \\\\Omega/z|& \\\\"'$'"\\\\Omega/z\\\\"'$'"' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nP '(?<"'![A-Za-z0-9])'"\\\\Omega/z(?"'![A-Za-z0-9])'"' chapters/connections/holographic_datum_master.tex chapters/frame/preface_section1_v2.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\small
\begin{tabular}{llcccccl}
\textbf{Family}
 & \textbf{Generators}
 & $\kappa$
 & $r(z)$
 & $r_{\max}$
 & \textbf{Class}
 & $\kappa+\kappa^!$
 & \textbf{Special}\\
\hline
$\cH_k$
 & $\alpha$ (wt~$1$)
 & $k$
 & $k/z$
 & $2$
 & G
 & $0$
 & Gaussian archetype\\[2pt]
$\widehat{\fg}_k$
 succeeded in 52ms:
chapters/frame/preface_section1_draft.tex:634:r(z) \;=\; \frac{\Omega}{z}\,,
chapters/frame/preface_sections5_9_draft.tex:581: & $\mathrm{av}(\Omega/z)$
chapters/theory/higher_genus_modular_koszul.tex:27802: the level-stripped form $r_0(z) = \Omega/z^3$ carries no
chapters/frame/preface_section1_v2.tex:481:r(z) \;=\; \frac{\Omega}{z}\,,
chapters/connections/holographic_datum_master.tex:466:\frac{\Omega}{z}
chapters/connections/holographic_datum_master.tex:719:& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
chapters/connections/frontier_modular_holography_platonic.tex:4731: $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
 succeeded in 52ms:
chapters/frame/preface_sections5_9_draft.tex:542: & $\Omega/z$
chapters/frame/preface_sections5_9_draft.tex:581: & $\mathrm{av}(\Omega/z)$
chapters/frame/preface_sections5_9_draft.tex:582: & $\Omega/z$
chapters/connections/holographic_datum_master.tex:1000:$r^{\mathrm{Dr}}(z) = \hbar \Omega/z + \mathcal{O}(\hbar^2)$ in the
chapters/connections/frontier_modular_holography_platonic.tex:4731: $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
chapters/connections/frontier_modular_holography_platonic.tex:4764:$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '500,620p' chapters/frame/preface_sections5_9_draft.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Every algebra in the standard landscape is either primitive
(Heisenberg, Virasoro, $\beta\gamma$) or built from primitive
pieces by direct sum plus extension. Drinfeld--Sokolov reduction
is the shadow-depth escalator: it sends class~L (finite towers)
to class~M (infinite towers). The nonlinearity of the Dirac
bracket on the Slodowy slice creates the quartic and all higher
shadows.


% ====================================================================
\section*{7.\quad The standard landscape}
% ====================================================================

The machine of Sections~1--6 accepts any chiral algebra. The
seven families below exhaust the standard Lie-theoretic landscape:
each realises a different depth class, curvature sign, and
genus-two shell profile.

\begin{center}
\renewcommand{\arraystretch}{1.2}
exec
/bin/zsh -lc "rg -n 'r\\"'^'"\\{\\\\mathrm\\{Dr\\}\\}|Drinfeld85|level-independent|k\\\\Omega/z|\\\\Omega/\\(\\(k \\+ h\\"'^'"\\\\vee\\)\\\\, z\\)|\\\\frac\\{\\\\Omega\\}\\{\\(k \\+ h\\"'^'"\\\\vee\\)\\\\, z\\}' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
16:spectral $r$-matrix of Drinfeld~\cite{Drinfeld85}; the classical
170: structure of Drinfeld~\cite{Drinfeld85};
459:The original spectral $r$-matrix is Drinfeld's~\cite{Drinfeld85},
464:r^{\mathrm{Dr}}(z)
475:$[r^{\mathrm{Dr}}_{12}(z), r^{\mathrm{Dr}}_{13}(z+w)]
476:+ [r^{\mathrm{Dr}}_{12}(z), r^{\mathrm{Dr}}_{23}(w)]
477:+ [r^{\mathrm{Dr}}_{13}(z+w), r^{\mathrm{Dr}}_{23}(w)] = 0$. This
480:$(\fg[\![z^{-1}]\!], r^{\mathrm{Dr}})$.
481:The Drinfeld $r$-matrix is level-independent: the
483:metric and the Sugawara shift, not through~$r^{\mathrm{Dr}}$ itself.
493:\frac{1}{k + h^\vee}\, r^{\mathrm{Dr}}(z)
495:\frac{\Omega}{(k + h^\vee)\, z}
505:The classical Yang--Baxter equation for $r^{\mathrm{Dr}}(z)$
578:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (vanishing at $k=0$) is the classical
585:Yangian coproduct of Drinfeld~\cite{Drinfeld85}.
592:$r^{\mathrm{cl}} = r^{\mathrm{Dr}} = k\Omega/z$ (level $k$, vanishing
595:which is the residue at $z = 0$ of $r^{\mathrm{Dr}}(z)$. The
662:residue~\eqref{eq:hdm-face-5}, leaving a level-independent
666:Face~4. The classical Yang--Baxter equation for $r^{\mathrm{Dr}}(z)$
719:& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import pathlib, re
root = pathlib.Path('chapters')
for path in sorted(root.rglob('*.tex')):
    text = path.read_text()
    for m in re.finditer(r'\\\\Omega/z', text):
        start = m.start()
        line_no = text.count('\\n', 0, start) + 1
        line = text.splitlines()[line_no-1]
        snippet = line.strip()
        if 'k' in snippet or 'hbar' in snippet or '1/z' in snippet:
            continue
        print(f\"{path}:{line_no}:{snippet}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/frame/preface_sections5_9_draft.tex:542:& $\Omega/z$
chapters/frame/preface_sections5_9_draft.tex:581:& $\mathrm{av}(\Omega/z)$
chapters/frame/preface_sections5_9_draft.tex:582:& $\Omega/z$
chapters/theory/derived_langlands.tex:858:The $r$-matrix $r(z) = -2\,\Omega/z$ is the degree-$2$ shadow of
chapters/theory/en_koszul_duality.tex:5066:$S(z) = \id + h_{\mathrm{KZ}}\,\Omega/z + O(z^{-2})$. Does
chapters/theory/higher_genus_modular_koszul.tex:3271:$r$-matrix is level-stripped, $r(z) = 0 \cdot \Omega/z = 0$,
chapters/theory/higher_genus_modular_koszul.tex:27802:the level-stripped form $r_0(z) = \Omega/z^3$ carries no


thinking
**Compiling AP126 violations for r-matrix levels**

After carefully filtering, I’m listing genuine AP126 violations—cases where `r(z)=\Omega/z` or its fraction form appears without the required level `k` prefix. These come mainly from three entries in the `chapters/frame/` preface drafts and tables referencing `\widehat{\mathfrak g}_k`. I’m excluding Drinfeld-level independent cases and average terms that don’t qualify as violations. I want to present their file paths, line numbers, and clear classifications to satisfy the user’s request precisely.
codex
- `chapters/frame/preface_section1_draft.tex:634` — affine Kac–Moody ordered-bar collision residue is written as `r(z)=\frac{\Omega}{z}` with no level coefficient; AP126 insists on the `k\,\Omega/z` form to make the $k=0$ vanishing manifest.  
- `chapters/frame/preface_section1_v2.tex:481` — the same affine Kac–Moody r-matrix passage in the alternate preface draft again omits `k` from `r(z)=\frac{\Omega}{z}`.  
- `chapters/frame/preface_sections5_9_draft.tex:542` — the “standard landscape” table entry for $\widehat{\mathfrak g}_k$ lists `r(z)=\Omega/z` instead of the level-prefixed `k\Omega/z` that the text itself (and AP126) requires.  

(Other bare `\Omega/z` mentions are either the Drinfeld level-independent Yangian residue or averaged/shadow quantities, so they were not flagged.)
thinking
**Exploring mathematical symbols**

I’m pondering a theorem that involves `Ω/((k+h^\vee)z)` under KZ. The term `Ω/z` in the Drinfeld context is historical, so I wonder if I can adjust the equation to `r^{Dr}_k(z)=k\Omega/z` since they want it in trace-form. But it seems like using the same symbol might cause confusion. I should probably avoid messing with forms that aren’t AP126, especially if they’re historically normalized. Still, the user wants all instances of `Ω/z` fixed in Vol I.
codex
I’ve narrowed the actual edit candidates to five chapter files. Before patching, I’m checking whether `holographic_datum_master.tex` can be made AP126-clean without breaking its KZ-normalized theorem lane.
exec
/bin/zsh -lc "sed -n '572,606p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '452,520p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '736,750p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\pi_\cA
\;=\;
r^{\mathrm{DNP}}(z)
\;=\;
\sum_{n \geq 0} \frac{\mathrm{cl}(a_{(n)}b)}{z^{n+1}}
\;=\;
H_i^{\mathrm{GZ}}\bigr|_{j\textrm{-coeff}}
\;=\;
\frac{r^{\mathrm{Dr}}(z)}{k + h^\vee}
\;=\;
\bigl\{\cdot,\cdot\bigr\}_{\mathrm{STS}}
\;=\;
\frac{H_i^{\mathrm{Gaudin}}}{k + h^\vee}\;}
\end{equation}
holds in the genus-zero, two-point sector of the modular cyclic
 succeeded in 51ms:
multiplication operators for affine Kac--Moody and Heisenberg
($k_{\max} = 1$), and genuine differential operators of order
$\geq 2$ for Virasoro and $\Walg_N$ ($k_{\max} \geq 3$).

\section{Face 5: the Yangian $r$-matrix of Drinfeld}
\label{sec:hdm-face-5}

The original spectral $r$-matrix is Drinfeld's~\cite{Drinfeld85},
introduced in connection with the quantum Yang--Baxter equation and
the Yangian deformation $Y_\hbar(\fg)$ of the universal enveloping
algebra of a simple Lie algebra~$\fg$. The classical $r$-matrix
\begin{equation}\label{eq:hdm-drinfeld-rmatrix}
r^{\mathrm{Dr}}(z)
\;=\;
\frac{\Omega}{z}
\;\in\;
\fg \otimes \fg [\![z^{-1}]\!],
\qquad
\Omega \;=\; \sum_a J^a \otimes J^a,
\end{equation}
 succeeded in 51ms:

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


thinking
**Evaluating inconsistencies in the file**

This file is definitely inconsistent. The task might not be to fully resolve that, but I want to consider some minimal edits. Possibly, we could change line 719 from bare `Ω/z` to `kΩ/z`, since that matches other places in the file. But, maybe I shouldn't touch theorem line 466. If I change the equation to `kΩ/z`, it might conflict with the theorem's behavior. I need to really think this through!
thinking
**Assessing proof adjustments**

I’m thinking about adjusting the proof text from k=0 to zero out, but that might change the theorem content significantly, possibly making it false in relation to KZ. The file might actually be interested in a trace form instead. I need to check theorem Face5 regarding how the collision residue relates to the Drinfeld r-matrix. If I skip hdm, is that okay? I should check if `holographic_datum_master.tex` is included in the main structure; it could be active. Consulting the explorer classification might help too!
collab wait(call_nGwpmnT5DzH3vOptZr2uSiVQ)
  receivers: 019d8792-c49a-7b51-bc3c-1092a7a6d8f3
wait(call_nGwpmnT5DzH3vOptZr2uSiVQ) 1 agents complete:
  019d8792-c49a-7b51-bc3c-1092a7a6d8f3 completed: "- `chapters/frame/preface_section1_draft.tex:634` — affine Kac–Moody ordered-bar collision residue is written as `r(z)=\…"


thinking
**Considering frontier fixes**

I’m thinking the frontier can be fixed, and it may not be necessary, but it could be helpful. Also, there's a thought about possibly editing the `holographic_datum_master` at line 719 in the master diagram. I wonder if that change would contribute positively. It's a bit unclear, but I want to make sure I’m considering all options to get the best outcome. Let’s see how to proceed from here!
thinking
**Verifying templates and formats**

I want to check if there are any bare `\frac{\Omega}{z}` elements in the frame or preface. But it seems like there aren't any. I should also consider creating a pre-edit verification template in the commentary section. I might mention the files too. Perhaps I can put together a generic template specifically for the affine KM trace-form. Of course, I'll include a verdict of ACCEPT, but I should do this before editing anything.
codex
```text
family: [affine KM]  r(z): [k\,\Omega/z]  level param: [k]  OPE pole: [double + simple]  r pole: [z^-1]
convention: [trace-form]
AP126 (trace-form): r|_{k=0} = [0]  expected: 0  match? [Y]
AP141 grep: bare \Omega/z in scope: [N after planned edits on the trace-form surface]  allowed? N
critical-level (KM): r|_{k=-h^v} = [-h^v\,\Omega/z]
source: [CLAUDE.md / AGENTS.md canonical formula census; trace-form lane]
verdict: ACCEPT
```

thinking
**Making edits**

I need to perform edits with apply_patch, focusing only on the files that have been touched. It’s important to accurately edit the frontier, so that’s my priority. I should open the exact sections that need attention. I'll have to ensure that I double-check everything to avoid missing key details, as clarity in these edits will be crucial for the overall project. Let’s get started on this!
codex
I’ve locked the affine KM trace-form convention. I’m patching the obvious AP126 misses now: two preface draft equations, the landscape table entries, and the level-1 specialization sentence that still exposed a bare `\Omega/z`.
exec
/bin/zsh -lc "sed -n '630,648p' chapters/frame/preface_section1_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '472,490p' chapters/frame/preface_section1_v2.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '536,586p' chapters/frame/preface_sections5_9_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4726,4736p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
makes $\widehat{\mathfrak g}_k$ the first nontrivial example.

The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
\[
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\]
where $\Omega$ is the Casimir tensor of~$\mathfrak g$. This is
matrix-valued: $\Omega \in \mathfrak g \otimes \mathfrak g$
carries the full Lie-algebraic structure. Averaging collapses the
Casimir to its trace:
\[
\mathrm{av}\bigl(k\Omega/z\bigr)
\;=\;
\frac{\dim(\mathfrak g)\cdot(k+h^\vee)}{2h^\vee}
\;=\;
\kappa(\widehat{\mathfrak g}_k).
\]
 succeeded in 51ms:
product supplies the curvature~$\kappa$. The coexistence of both
poles, absent in the Heisenberg case, makes
$\widehat{\mathfrak g}_k$ the first nontrivial example.

\medskip
\noindent\textbf{The Casimir $R$-matrix.}\enspace
The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
collision residue
\begin{equation}\label{eq:pf1-km-rmatrix}
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\end{equation}
where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
tensor. This is matrix-valued: $\Omega$ carries the full
Lie-algebraic structure that was invisible in the Heisenberg
scalar~$k/z$. The averaging map collapses the Casimir to a
scalar:
\begin{equation}\label{eq:pf1-km-kappa}
 succeeded in 51ms:
 & G
 & $0$
 & Gaussian archetype\\[2pt]
$\widehat{\fg}_k$
 & $J^a$ (wt~$1$)
 & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\Omega/z$
 & $3$
 & L
 & $0$
 & FF center at $k{=}{-}h^\vee$\\[4pt]
$\mathrm{Vir}_c$
 & $T$ (wt~$2$)
 & $c/2$
 & $\frac{c/2}{z^3}+\frac{2T}{z}$
 & $\infty$
 & M
 & $13$
 & self-dual at $c{=}13$\\[4pt]
$\cW_3{}_c$
 succeeded in 50ms:
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

thinking
**Applying a patch**

I see that I need to apply a patch and it looks like I should update the row in table Y(g). It’s important to ensure that the patch is correctly applied. I’ll focus on making the necessary changes, but I want to double-check for any potential issues that might arise in this process. Let’s make sure everything goes smoothly so the system operates optimally!
file update
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex
@@ -480,3 +480,3 @@
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex
@@ -633,3 +633,3 @@
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex
@@ -541,3 +541,3 @@
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
@@ -580,4 +580,4 @@
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4729,5 +4729,6 @@
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
apply_patch(auto_approved=true) exited 0 in 40ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex
M /Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..0fa88227c19ca16793a332cc8afd0d18644c5f84
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---

file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..0fa88227c19ca16793a332cc8afd0d18644c5f84
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---

codex
The trace-form edits are in. I’m verifying two things now: the four touched files are clean, and the only remaining bare `\Omega/z` in `chapters/` are the historical/KZ-normalized lanes I intentionally did not rewrite.
exec
/bin/zsh -lc "rg -n '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\mathrm\\{av\\}\\(\\\\Omega/z\\)|(?<"'![A-Za-z0-9])'"\\\\Omega/z(?"'![A-Za-z0-9])'"' chapters/frame/preface_section1_v2.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -nP '(?<"'![A-Za-z0-9])'"\\\\Omega/z(?"'![A-Za-z0-9])|'"\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\mathrm\\{av\\}\\(\\\\Omega/z\\)' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/frame/preface_section1_v2.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/connections/frontier_modular_holography_platonic.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\frac\{\\Omega\}\{z\}|\\mathrm\{av\}\(\\Omega/z\)|(?<![A-Za-z0-9])\\Omega/z(?![A-Za-z0-9]))
                                                          ^^^^
error: look-around, including look-ahead and look-behind, is not supported

Consider enabling PCRE2 with the --pcre2 flag, which can handle backreferences
and look-around.
 succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
chapters/examples/w_algebras_deep.tex:2821: r^{\mathrm{KM}}(z) = k\,\Omega/z
chapters/examples/w_algebras_deep.tex:2867: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
chapters/frame/preface.tex:793:the passage from $r(z) = k\,\Omega/z$ to
chapters/frame/preface.tex:1219:affine Kac--Moody, $r(z) = k\,\Omega/z$ is matrix-valued; the
chapters/frame/preface.tex:3050:$R$-matrix $r(z) = k\,\Omega/z$ is matrix-valued: the Casimir
chapters/frame/preface.tex:3061:deconcatenation coproduct evaluated on $r(z) = k\,\Omega/z$.
chapters/frame/preface.tex:3276:$R$-matrix $r(z) = k\,\Omega/z$ as the genus-$0$ binary
chapters/frame/preface.tex:3333: & $k\,\Omega/z$
chapters/frame/preface.tex:3381: & $k\,\Omega/z$
chapters/frame/preface.tex:4431:$r(z)=k\,\Omega/z$ (Yang's solution of the CYBE, level-prefixed),
chapters/connections/thqg_introduction_supplement_body.tex:487:algebra~$\mathfrak{g}$ at level~$k$ (that is, $r(z) = k\,\Omega/z$ where
chapters/connections/thqg_introduction_supplement_body.tex:1277:rational $r$-matrix $r(z) = k\,\Omega/z$ generates the RTT presentation
chapters/frame/heisenberg_frame.tex:3565:$d\log$, and any formula with a bare $1/z$ or $\Omega/z$ without a
chapters/frame/heisenberg_frame.tex:3978:For the rational $r$-matrix $r(z) = k\,\Omega/z$
chapters/frame/heisenberg_frame.tex:4027:$r(z) = k\,\Omega/z$,
chapters/frame/heisenberg_frame.tex:4072:is \emph{irrecoverable}: $r(z) = k\,\Omega/z$ carries the
chapters/frame/heisenberg_frame.tex:4123: & $k\,\Omega/z$
chapters/frame/heisenberg_frame.tex:4127: & $1 + k\hbar\,\Omega/z + \cdots$
 succeeded in 51ms:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c845..0fa8822 100644
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@ is computed for two brane systems:
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4d..0d9b01e 100644
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..0fa88227c19ca16793a332cc8afd0d18644c5f84
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---


thinking
**Rerunning confirmation check**

I need to consider rerunning the regex grid (rg) with the `--pcre2` option on the files I've touched. This way, I can confirm that there are no bare matches. It’s essential to double-check everything to ensure accuracy. I think that by using this option, I’ll strengthen my search results. It’s important to verify things carefully, so let's see if that confirms the situation!
exec
/bin/zsh -lc "rg --pcre2 -n '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\mathrm\\{av\\}\\(\\\\Omega/z\\)|(?<"'![A-Za-z0-9])'"\\\\Omega/z(?"'![A-Za-z0-9])'"' chapters/frame/preface_section1_v2.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/frontier_modular_holography_platonic.tex:4765:$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..0fa88227c19ca16793a332cc8afd0d18644c5f84
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---


thinking
**Revising coefficients in equations**

I see that touched files still include a `1 \cdot \Omega/z` line, where the coefficient is explicitly one. Regex catches this due to the negative lookbehind. I’m considering whether to leave it as is or rewrite it as `k\Omega/z|_{k=1}` for clarity. The user prefers all bare forms, and since `1 \cdot` isn't bare, it may be better to adjust it. Maybe changing to `k\Omega/z$ evaluated at $k=1` could work better. I'll inspect the context further.
codex
One touched file still has a level-1 specialization written as `1 \cdot \Omega/z`. I’m removing that last exposed bare kernel so the edited surface is uniformly level-prefixed.
exec
/bin/zsh -lc "sed -n '4760,4768p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\kappa(\mathfrak{u}(1), k) = k$
(the authoritative formulas from
Theorem~\ref{thm:modular-characteristic}).

The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
the current algebra OPE
$J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
f^c_{ab}J_c/(z{-}w)$
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..0fa88227c19ca16793a332cc8afd0d18644c5f84
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---


thinking
**Revising specialization expression**

I’m thinking about how to express this concept more clearly. I could rewrite it as "this gives the level-1 specialization of \(k\Omega/z\)." It feels like a simple adjustment that could enhance understanding. Still, I want to ensure I’m patching it appropriately to keep it coherent and informative for anyone looking at it. Getting the wording right is important! Let’s see how else I can refine this.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4764,3 +4764,3 @@
 The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
+$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
 the current algebra OPE
apply_patch(auto_approved=true) exited 0 in 58ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..8739eb505f7ca1d78a01e0a7d8c046b1d2c0c1f2
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
@@ -4761,7 +4762,7 @@
 Theorem~\ref{thm:modular-characteristic}).
 
 The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
+$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---

file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..8739eb505f7ca1d78a01e0a7d8c046b1d2c0c1f2
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
@@ -4761,7 +4762,7 @@
 Theorem~\ref{thm:modular-characteristic}).
 
 The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
+$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---


thinking
**Verifying files**

I see that I need to check whether the touched files are clean. It's important to ensure everything is in order and no unnecessary changes have been made. I want to make sure that I do this thoroughly, so I’m going to take the time needed and confirm that everything is exactly as it should be. I don’t want any surprises later! So, let’s make that verification a priority.
exec
/bin/zsh -lc "rg --pcre2 -n '\\\\frac\\{\\\\Omega\\}\\{z\\}|\\\\mathrm\\{av\\}\\(\\\\Omega/z\\)|(?<"'![A-Za-z0-9])'"\\\\Omega/z(?"'![A-Za-z0-9])'"' chapters/frame/preface_section1_v2.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..8739eb505f7ca1d78a01e0a7d8c046b1d2c0c1f2
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
@@ -4761,7 +4762,7 @@
 Theorem~\ref{thm:modular-characteristic}).
 
 The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
+$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---

codex
The edited files are clean. I’m doing one last repository-wide spot check for the specific bare spellings I targeted, so I can separate true remaining AP126 debt from historical normalization text.
exec
/bin/zsh -lc "nl -ba chapters/frame/preface_section1_v2.tex | sed -n '478,486p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface_sections5_9_draft.tex | sed -n '538,584p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface_section1_draft.tex | sed -n '632,640p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '4728,4767p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\frac\\{\\\\Omega\\}\\{z\\}|& \\"'$'"\\\\Omega/z\\"'$|'"\\\\mathrm\\{av\\}\\(\\\\Omega/z\\)|= \\\\Omega/z' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   478	The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
   479	collision residue
   480	\begin{equation}\label{eq:pf1-km-rmatrix}
   481	r(z) \;=\; \frac{k\,\Omega}{z}\,,
   482	\qquad
   483	\Omega \;=\; \sum_a J^a \otimes J_a\,,
   484	\end{equation}
   485	where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
   486	tensor. This is matrix-valued: $\Omega$ carries the full
 succeeded in 51ms:
   538	 & Gaussian archetype\\[2pt]
   539	$\widehat{\fg}_k$
   540	 & $J^a$ (wt~$1$)
   541	 & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
   542	 & $k\Omega/z$
   543	 & $3$
   544	 & L
   545	 & $0$
   546	 & FF center at $k{=}{-}h^\vee$\\[4pt]
   547	$\mathrm{Vir}_c$
   548	 & $T$ (wt~$2$)
   549	 & $c/2$
   550	 & $\frac{c/2}{z^3}+\frac{2T}{z}$
   551	 & $\infty$
   552	 & M
   553	 & $13$
   554	 & self-dual at $c{=}13$\\[4pt]
   555	$\cW_3{}_c$
   556	 & $T,W$ (wt~$2,3$)
   557	 & $5c/6$
 succeeded in 51ms:
   632	The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
   633	\[
   634	r(z) \;=\; \frac{k\,\Omega}{z}\,,
   635	\qquad
   636	\Omega \;=\; \sum_a J^a \otimes J_a\,,
   637	\]
   638	where $\Omega$ is the Casimir tensor of~$\mathfrak g$. This is
   639	matrix-valued: $\Omega \in \mathfrak g \otimes \mathfrak g$
   640	carries the full Lie-algebraic structure. Averaging collapses the
 succeeded in 51ms:
  4728	 \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  4729	 \]
  4730	 The holographic R-matrix is
  4731	 $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
  4732	 $k=1$ this specializes to the level-$1$ kernel, while the
  4733	 level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  4734	 $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  4735	 twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  4736	 The anomaly matching condition
  4737	 $\kappa_{\mathrm{eff}}
  4738	 = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$
  4739	 is a consistency check.
  4740	
  4741	\item \emph{Sphere reconstruction.}
  4742	 The genus-$0$, $n$-point shadow amplitudes
  4743	 $\mathrm{Sh}_{0,n}(\Theta_\cA)$ are the Witten
  4744	 diagram amplitudes of the holomorphic twist. The
  4745	 commuting differentials of Gaiotto--Zinenko~\cite{GZ26}
  4746	 are the scalar shadow of $\mathrm{Sh}_{0,n}$.
  4747	\end{enumerate}
 succeeded in 52ms:
chapters/connections/holographic_datum_master.tex:466:\frac{\Omega}{z}
chapters/connections/holographic_datum_master.tex:719:& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
chapters/theory/higher_genus_modular_koszul.tex:27802: the level-stripped form $r_0(z) = \Omega/z^3$ carries no
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..8739eb505f7ca1d78a01e0a7d8c046b1d2c0c1f2
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
@@ -4761,7 +4762,7 @@
 Theorem~\ref{thm:modular-characteristic}).
 
 The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
+$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---


thinking
**Finalizing edits and findings**

I want to keep the final output concise while still covering my findings and exact edits. Maybe no tests are needed, but I could mention verification with `grep` or possibly use `rg`. I already ran checks, so perhaps running tests isn't necessary. I should include a final list of problem lines and applied edits, which could be presented as bullet points. Here are five key findings I’ll include:

1. Update `\frac{\Omega}{z}` to `\frac{k\,\Omega}{z}` at `chapters/frame/preface_section1_v2.tex:481`.
2. The same update at `chapters/frame/preface_section1_draft.tex:634`.
3. Change table entry `\Omega/z` to `k\Omega/z` at `chapters/frame/preface_sections5_9_draft.tex:542`.
4. Update `\mathrm{av}(\Omega/z)` to `\mathrm{av}(k\Omega/z)` and `\Omega/z` to `k\Omega/z` at `chapters/frame/preface_sections5_9_draft.tex:581-582`.
codex
Fixed the AP126 trace-form misses I found in the assigned Vol I chapter surface.

- PROBLEM at [preface_section1_v2.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_v2.tex:481): affine KM collision residue was written as `r(z)=\frac{\Omega}{z}`. EXACT edit applied: `r(z)=\frac{k\,\Omega}{z}`.

- PROBLEM at [preface_section1_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_section1_draft.tex:634): the same affine KM `R`-matrix draft lane omitted the level. EXACT edit applied: `r(z)=\frac{k\,\Omega}{z}`.

- PROBLEM at [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:542): the landscape table listed the affine KM `r(z)` entry as bare `\Omega/z`. EXACT edit applied: `k\Omega/z`.

- PROBLEM at [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:581): the Yangian row averaged a bare kernel as `\mathrm{av}(\Omega/z)`. EXACT edit applied: `\mathrm{av}(k\Omega/z)`.

- PROBLEM at [preface_sections5_9_draft.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface_sections5_9_draft.tex:582): the Yangian row also listed bare `\Omega/z` in the `r(z)` column. EXACT edit applied: `k\Omega/z`.

- PROBLEM at [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4730): the D3 specialization exposed a bare equality `r(z)=k\Omega/z=\Omega/z`. EXACT edit applied: rewrote it to `r(z)=k\Omega/z`, with prose `at the D3 locus k=1 this specializes to the level-1 kernel`.

- PROBLEM at [frontier_modular_holography_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex:4764): the proof prose still exposed `1\cdot\Omega/z`. EXACT edit applied: rewrote it as `the level-1 specialization of k\Omega/z`.

Verification: `rg --pcre2` on the four touched files returned no remaining bare `\Omega/z`, `\frac{\Omega}{z}`, or `\mathrm{av}(\Omega/z)` spellings. I did not run a TeX build. The only remaining chapter-wide bare `\Omega/z` hits are the historical Drinfeld-normalization lane in [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:466) and [holographic_datum_master.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:719), plus the separate `\Omega/z^3` Virasoro line in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:27802).
file update:
diff --git a/chapters/connections/frontier_modular_holography_platonic.tex b/chapters/connections/frontier_modular_holography_platonic.tex
index 731c84555c66ae66e5a5bcf98a7f1c1d34e389be..8739eb505f7ca1d78a01e0a7d8c046b1d2c0c1f2
--- a/chapters/connections/frontier_modular_holography_platonic.tex
+++ b/chapters/connections/frontier_modular_holography_platonic.tex
@@ -4727,9 +4727,10 @@
  \;=\;
  \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
  \]
- The holographic R-matrix at level $k=1$ is
- $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
- $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
+ The holographic R-matrix is
+ $r(z) = k\Omega/z$ (classical Yang--Baxter; at the D3 locus
+ $k=1$ this specializes to the level-$1$ kernel, while the
+ level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  The anomaly matching condition
@@ -4761,7 +4762,7 @@
 Theorem~\ref{thm:modular-characteristic}).
 
 The R-matrix $r(z) = k\Omega/z$ at level $k$ is the collision residue
-$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives $1 \cdot \Omega/z$):
+$\mathrm{Res}^{\mathrm{coll}}_{0,2}(\Theta_\cA)$ (vanishing at $k=0$; at the D3 level $k=1$ this gives the level-$1$ specialization of $k\Omega/z$):
 the current algebra OPE
 $J_a(z)J_b(w) \sim k\delta_{ab}/(z{-}w)^2 +
 f^c_{ab}J_c/(z{-}w)$
diff --git a/chapters/frame/preface_section1_draft.tex b/chapters/frame/preface_section1_draft.tex
index 6d9db4df8f493dfbabe8ac4cb46cc2cd45b53550..0d9b01e640e935b1aeae1f31882648c1efedbf4d
--- a/chapters/frame/preface_section1_draft.tex
+++ b/chapters/frame/preface_section1_draft.tex
@@ -631,7 +631,7 @@
 
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
 \[
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \]
diff --git a/chapters/frame/preface_section1_v2.tex b/chapters/frame/preface_section1_v2.tex
index 7314e55e250ef64deec7ab3d0de7fb7f1fe494ea..9eb8a9e07585e33c8417e7bc7df295e8f61402f5
--- a/chapters/frame/preface_section1_v2.tex
+++ b/chapters/frame/preface_section1_v2.tex
@@ -478,7 +478,7 @@
 The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
 collision residue
 \begin{equation}\label{eq:pf1-km-rmatrix}
-r(z) \;=\; \frac{\Omega}{z}\,,
+r(z) \;=\; \frac{k\,\Omega}{z}\,,
 \qquad
 \Omega \;=\; \sum_a J^a \otimes J_a\,,
 \end{equation}
diff --git a/chapters/frame/preface_sections5_9_draft.tex b/chapters/frame/preface_sections5_9_draft.tex
index c656be065493f667595a0cd9bdd4413ea17766b8..415966f7e343e404023667e3b5cce647dacda6e3
--- a/chapters/frame/preface_sections5_9_draft.tex
+++ b/chapters/frame/preface_sections5_9_draft.tex
@@ -539,7 +539,7 @@
 $\widehat{\fg}_k$
  & $J^a$ (wt~$1$)
  & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
- & $\Omega/z$
+ & $k\Omega/z$
  & $3$
  & L
  & $0$
@@ -578,8 +578,8 @@
  & arithmetic from~$q$\\[2pt]
 $Y(\fg)$
  & line operators
- & $\mathrm{av}(\Omega/z)$
- & $\Omega/z$
+ & $\mathrm{av}(k\Omega/z)$
+ & $k\Omega/z$
  & $3$
  & L
  & ---

tokens used
85,912
