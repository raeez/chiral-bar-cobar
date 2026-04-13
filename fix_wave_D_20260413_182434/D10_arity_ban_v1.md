# D10_arity_ban_v1 (395s)

- PROBLEM at [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2827): 9 remaining `arity` usages on the Swiss-cheese operation surface. Exact edit applied: `arity` -> `degree` in `mixed Swiss-cheese tree of arity~$r$`, `mixed Swiss-cheese arity-$r$ operation`, `mixed tree formulas stop at arity~$2$`, `operations of arity`, and `mixed arity-$r$ Massey` at lines 2827, 2859, 2920, 2926, 2928, 2954, 2964, 2972, 2974.

- PROBLEM at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3358): 11 remaining `arity` usages in the topologization obstruction discussion. Exact edit applied: `In arity~$n$` -> `In degree~$n$`; `through/in arity~$N{+}1$` -> `through/in degree~$N{+}1$`; `lowest-arity` -> `lowest-degree`; `corrected arity`/`higher arity` -> `corrected degree`/`higher degree`; `each arity`/`every arity` -> `each degree`/`every degree`; `arity-$N$ obstruction` -> `degree-$N$ obstruction`.

- PROBLEM at [chapters/theory/introduction.tex.bak](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak:46): backup surface still contained many `arity` phrases plus local ref/label names. Exact edit applied: `arity~$2/3/4$` -> `degree~$2/3/4$`; `largest arity` -> `largest degree`; `arity-by-arity` -> `degree-by-degree`; `all arities`/`all-arity` -> `all degrees`/`all-degree`; `arity cutoff` -> `degree cutoff`; `\ref{thm:e1-mc-finite-arity}` -> `\ref{thm:e1-mc-finite-degree}`; `\eqref{eq:e1-mc-arity3}` -> `\eqref{eq:e1-mc-degree3}`; `\ref{lem:arity-cutoff}` -> `\ref{lem:degree-cutoff}`; `\label{eq:all-arity-master-eq-intro}` -> `\label{eq:all-degree-master-eq-intro}`.

- PROBLEM at [chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:255): backup surface still contained 7 `arity` usages. Exact edit applied: `records the arity` -> `records the degree`; `arity~$1/2/3/4$` -> `degree~$1/2/3/4$`; `all-arity limit` -> `all-degree limit`; `for some arity~$n$`/`cochain of arity~$n$` -> `for some degree~$n$`/`cochain of degree~$n$`.

- PROBLEM at [standalone/N4_mc4_completion.tex](/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:419): one case-insensitive `ARITY` hit remained in a section comment. Exact edit applied: `THE ARITY CUTOFF LEMMA` -> `THE DEGREE CUTOFF LEMMA`.

- PROBLEM at [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:265): in-scope article defect after the terminology shift. Exact edit applied: `An degree-$3$` -> `A degree-$3$`.

Verification: `grep -rni '\barity\b' chapters/ appendices/ standalone/` returns no hits, and `grep -rniE '(^|[^[:alpha:]])an degree' chapters/ appendices/ standalone/` also returns no hits.


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
session id: 019d87bc-f5c5-7c00-9360-20c0fcb160bc
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


Remove ALL remaining 'arity' from Vol I (AP176).
grep -rni '\barity\b' chapters/ appendices/ standalone/
Must return ZERO hits. Replace with 'degree'. Fix article: 'an degree' -> 'a degree'.
mcp startup: no servers
codex
Scope is Vol I only: remove every remaining `arity` hit under `chapters/`, `appendices/`, and `standalone/`, then verify zero matches for `\barity\b`. I’m reading the required repo context first and locating the live hit surface before editing.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\barity\\b' chapters/ appendices/ standalone/" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:255:degree itself (tensor length minus one) records the arity.  The bar
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1069:cogenerator is concentrated in arity~$1$:
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:1815:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:2942:$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3118:braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3782:for some arity~$n$.  The Hochschild differential is
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:3787:a cochain of arity~$n$ is determined by
chapters/theory/en_koszul_duality.tex:3358:in the brace deformation complex. In arity~$n$, this means
chapters/theory/en_koszul_duality.tex:3373:Starting from $G_1$, a partial solution through arity~$N$
chapters/theory/en_koszul_duality.tex:3374:produces an obstruction cocycle in arity~$N{+}1$ of the same
chapters/theory/en_koszul_duality.tex:3474:  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
chapters/theory/en_koszul_duality.tex:3494:  so the corrected arity is removed and the defect is pushed to
chapters/theory/en_koszul_duality.tex:3495:  higher arity. This is the precise sense in which one tries to kill
chapters/theory/en_koszul_duality.tex:3850:obstruction at arity~$N{+}1$ to extending the Sugawara
chapters/theory/en_koszul_duality.tex:3856:applies: the only available harmonic insertions at each arity
chapters/theory/en_koszul_duality.tex:3859:at arity~$N{+}1$ is proportional to
chapters/theory/en_koszul_duality.tex:3865:Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
chapters/theory/en_koszul_duality.tex:3870:no new input beyond the identification of the arity-$N$ obstruction
chapters/theory/chiral_koszul_pairs.tex:2827:the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
chapters/theory/chiral_koszul_pairs.tex:2859:cases the mixed Swiss-cheese arity-$r$ operation is the open-colored


thinking
**Considering file edits**

I'm thinking about labels and whether they relate to environment names. I should also explore hidden backup files because I've found some hits in files like `.bak` and `.bak.abelian_cs_fix`. Editing those might be necessary. I wonder if I should delete backups, but the user specifically said to only edit assigned files. It seems like replacing words could be a minimal edit, especially given that user wants zero hits overall.
thinking
**Adjusting terminology**

I need to handle the "all-arity" aspect too. Using grep with the boundary `\barity\b` will match arity even in hyphenated compounds, so I must replace those instances. For example, "arity-$3$" should be changed to "degree-$3$." However, I wonder if "arity" in an operad context could sometimes be more precise than "degree." But since the user wants to remove all arity references from Volume I AP176, I'll replace them accordingly and check for improper articles like "an degree."
codex
The live surface is small but includes backup files that still count under the user’s grep. I’m narrowing the exact hit counts per file and then I’ll patch only those files with literal `arity` occurrences.
exec
/bin/zsh -lc "sed -n '3338,3885p' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2810,2995p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,3800p' chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix | rg -n '\\barity\\b|an degree|a degree'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,1820p' chapters/theory/introduction.tex.bak | rg -n '\\barity\\b|an degree|a degree'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -c '\\barity\\b' chapters/ appendices/ standalone/ --sort path" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
46:finer invariants: $\kappa$ at arity~$2$, a cubic
47:shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
48:at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
49:largest arity at which the shadow is nonzero; it equals
86:The genus and arity directions are orthogonal
95:Genus~$1$ sees only~$\kappa$ (arity~$2$).
96:Genus~$2$ first sees~$S_3$ (arity~$3$).
104:arity~$2$, $\Delta = 0$ stratum of this picture: the
159:The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
163:spectral scattering of~$\cA$.  The arity-$3$ component is the
164:\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
200:At arity~$2$, this projection records only one number: the
213:arity-by-arity image of
238:  is the arity-by-arity $\Sigma_n$-coinvariant image of the
245:  at arity~$3$ it contains the Drinfeld associator
278:(the genus-$0$, arity-$3$ MC equation;
279:Theorem~\ref{thm:e1-mc-finite-arity},
290:forces the arity-$3$ component of any lift to involve
330:$\Sigma_n$-coinvariants on each arity.  At the level of cofree
412:$\operatorname{av}(r(z))$ at arity~$2$.
 succeeded in 52ms:
16:degree itself (tensor length minus one) records the arity.  The bar
20:For a degree-$1$ element, the data is:
154:Here $\alpha(z_3) \otimes \eta_{23}$ is a degree-$1$
222:right-hand side of~\eqref{eq:frame-dres-deg2} is a degree-$1$
482:Each term is a degree-$2$ element, and from
492:\otimes \eta_{23} \wedge \eta_{34}$ is a degree-$2$ element
830:cogenerator is concentrated in arity~$1$:
1576:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
1815:three currents via a simple-pole extraction, producing a degree-$1$
2703:$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
2879:braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
3543:for some arity~$n$.  The Hochschild differential is
3548:a cochain of arity~$n$ is determined by
 succeeded in 52ms:
\end{tabular}
\end{center}

\medskip\noindent
\emph{Mechanism.}
For class~$G$\textup{:}
Heisenberg, lattice VOAs, and free fermions are Gaussian/free-field:
their ordered bar data is generated by the binary two-point kernel,
so every connected genus-$0$ tree with at least three external legs
factors through pairings and carries no primitive higher vertex.
Equivalently, the shadow tower truncates at degree~$2$:
$S_r(\cA)=0$ for $r \geq 3$
\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
lattices see Corollary~\ref{cor:lattice-postnikov-termination}\textup{)}.
Under the averaging map
$\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
\textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
shadow. Since there is no primitive tree for $r \geq 3$,
all higher mixed-sector operations vanish.
 succeeded in 52ms:
  \textup{(}Lurie~\cite{HA}\textup{)}.
\end{enumerate}
Steps~\textup{(i)}--\textup{(v)} prove the cohomological
$\Ethree^{\mathrm{top}}$ and therefore the chain-level model on
the zero-differential cohomology complex. The only missing
step for the original complex is an $A_\infty$-coherent
null-homotopy of holomorphic translation.

Choose a cofibrant brace/$A_\infty$ model
$m = (m_1, m_2, \ldots)$ for the closed
$\Etwo$-structure on
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$.
The unary operator $G_1$ coming from the Sugawara
antighost contraction kills $\partial_z$ only on
$Q$-cohomology. To kill it on the original complex, one must
extend $G_1$ to a degree-$(-1)$ family
$G = (G_1, G_2, \ldots)$ satisfying
\[
  [m, G] \;=\; \partial_z
\]
 succeeded in 51ms:
chapters/theory/chiral_koszul_pairs.tex:9
chapters/theory/en_koszul_duality.tex:11






thinking
**Analyzing output from rg**

I'm noticing that the `rg -c` output seems to show only non-backup files. Now, could it be that `rg -c` respects hidden files by default? It might not have shown backup files because of a `.gitignore` configuration that excludes `.bak` files. But if I use `grep -rni`, it should find everything, including those ignored files. So, I’ll need to run `grep -rni` to ensure nothing is missed and check for any zero hits.
thinking
**Investigating rg behavior**

I'm wondering if the reason I'm seeing only two files is because of a maximum output limit. It’s not likely since the counts seem small. Maybe `rg -c` is suppressing zero counts, only showing non-ignored files due to a pattern exclusion like `-g '!*.bak*'`. But, the initial `rg` still found backups, so that's puzzling. I should check what `rg -n` shows. The command I used did find backups, so it’s all a bit weird. Maybe `rg -c` counts lines only once?
thinking
**Planning follow-up searches**

I think I'll stick with the exact initial output and maybe rerun the command with `grep` after making the necessary edits. I should search for the phrase "an degree" after making replacements. However, I wonder if using `\bArity\b` is necessary since `grep` typically ignores case. It might be better to just perform a blanket replacement in lowercase. I also need to consider that labels like `lem:arity-cutoff` and `eq:all-arity-master-eq-intro` might not get matched by `grep`.
thinking
**Considering grep usage**

I'm thinking about cross-file references and whether a backup should stay isolated. I want to ensure if a label appears multiple times in the same file, I handle it carefully. Maybe I should only update that backup. There's a possibility of an ignore issue. Since the user specified using grep for final detection, I'll likely use it to find all relevant hits after edits. I need to figure out the right syntax, especially with the word boundary and macOS compatibility.
thinking
**Exploring grep command in zsh**

I’m considering the command `grep -rni '\barity\b'` in zsh on a Mac and how it might erroneously match something like `barityb`. I need to double-check that. Also, the initial output I’m thinking of might involve using `rg` from a different tool rather than `grep`. I realize the user may not expect the command to match in a specific way. I need to ensure clarity for the user’s needs.
thinking
**Testing grep functionality**

I'm looking at whether the command `rni '\barity\b'` will work to mirror something. I think it probably does in BSD grep, but then again, I've remembered that BSD grep actually uses `\<` and `\>` instead of `\b`. I wonder if `\b` represents a backspace? I could run the command to confirm. I also need to check if it might return zero results due to non-matching criteria before making any edits.
codex
The remaining work includes `.bak` surfaces because the user’s target grep traverses them. I’m checking the exact grep semantics in this shell before patching so the final zero-hit verification matches the requested command, not just `rg`.
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
import re
paths = [Path('chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix'), Path('chapters/theory/introduction.tex.bak'), Path('chapters/theory/en_koszul_duality.tex'), Path('chapters/theory/chiral_koszul_pairs.tex')]
pat = re.compile(r'\\barity\\b')
for p in paths:
    txt = p.read_text()
    hits = pat.findall(txt)
    print(f'{p}: {len(hits)}')
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "grep -rni '\\barity\\b' chapters/ appendices/ standalone/" in /Users/raeez/chiral-bar-cobar succeeded in 477ms:
chapters/theory/chiral_koszul_pairs.tex:2827:the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
chapters/theory/chiral_koszul_pairs.tex:2859:cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
chapters/theory/chiral_koszul_pairs.tex:2920:mixed tree formulas stop at arity~$2$, so
chapters/theory/chiral_koszul_pairs.tex:2926:Then every mixed Swiss-cheese operation of arity~$r \geq 3$
chapters/theory/chiral_koszul_pairs.tex:2928:The tree-shadow correspondence is operadic: the arity-$r$ mixed
chapters/theory/chiral_koszul_pairs.tex:2954:Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
chapters/theory/chiral_koszul_pairs.tex:2964:$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
chapters/theory/chiral_koszul_pairs.tex:2972:same transferred genus-$0$ tree that defines the mixed arity-$r$
chapters/theory/chiral_koszul_pairs.tex:2974:so that tree would determine a nontrivial mixed arity-$r$ Massey
chapters/theory/introduction.tex.bak:46:finer invariants: $\kappa$ at arity~$2$, a cubic
chapters/theory/introduction.tex.bak:47:shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
chapters/theory/introduction.tex.bak:48:at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
chapters/theory/introduction.tex.bak:49:largest arity at which the shadow is nonzero; it equals
chapters/theory/introduction.tex.bak:86:The genus and arity directions are orthogonal
chapters/theory/introduction.tex.bak:95:Genus~$1$ sees only~$\kappa$ (arity~$2$).
chapters/theory/introduction.tex.bak:96:Genus~$2$ first sees~$S_3$ (arity~$3$).
chapters/theory/introduction.tex.bak:104:arity~$2$, $\Delta = 0$ stratum of this picture: the
chapters/theory/introduction.tex.bak:159:The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
chapters/theory/introduction.tex.bak:163:spectral scattering of~$\cA$.  The arity-$3$ component is the
chapters/theory/introduction.tex.bak:164:\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$

thinking
**Considering file and plan updates**

I’m thinking I might not need any other files because the grep output seems exhaustive. Maybe I should back up the introduction and Heisenberg files, just in case. Should I prepare a plan? It might not be necessary, but an updated plan could be helpful. The task feels straightforward, but I could consider using update_plan with clear steps. The developer suggests that after reaching sufficient context, I can provide a longer plan, so a concise summary with statuses sounds good.
codex
I’ve confirmed the exact zero-hit target with the user’s `grep -rni` semantics. The patch set is confined to five files: two live chapter files, two backup chapter files that still count under the grep, and one standalone file with an uppercase comment hit.

PE-12 prose hygiene
```text
scope: chapters/theory/chiral_koszul_pairs.tex; chapters/theory/en_koszul_duality.tex; chapters/theory/introduction.tex.bak; chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix; standalone/N4_mc4_completion.tex
operation: replace every word-hit of arity/ARITY with degree/DEGREE; repair article if replacement yields "an degree"
line-of-fire check: only grep-positive files will be edited [Y]
semantic risk: local prose only; no theorem status / formula / label drift outside touched files [Y]
verification target: grep -rni '\\barity\\b' chapters/ appendices/ standalone/ returns zero
verdict: ACCEPT
```
Plan update
Patch only the grep-positive Vol I files, then re-run the exact grep to prove the surface is clean.
  ✓ Inspect the exact hit contexts in the five grep-positive files
  → Apply minimal replacements from arity to degree, including article fixes
  • Verify grep -rni '\barity\b' chapters/ appendices/ standalone/ returns zero



thinking
**Evaluating code edits**

I'm considering the standalone context and whether I need to check exact lines in backup files, though simple textual replacements might suffice. I need to be careful with labels. Using perl/sed for bulk replacements could work, but I should always apply patches for manual edits. I can possibly patch whole files with search and replace hunks. Automation might help generate patches, and I can use `grep -n -C` to check for occurrences. I'll ensure systematic replacements without mistakes!
thinking
**Planning replacements**

I need to generate exact replacements, thinking about each file specifically. For "chapters/theory/chiral_koszul_pairs.tex," there are 9 occurrences to address. For example, I can change "mixed Swiss-cheese tree of arity$r$" to "mixed Swiss-cheese tree of degree$r$." That seems less repetitive. I might also adjust phrases like "mixed Swiss-cheese arity-$r$ operation" to "mixed Swiss-cheese degree-$r$ operation." There’s a few more, like replacing "stop at arity$2$" with "degree$2$." I'll keep going through the file systematically!
thinking
**Considering minimal edits**

I'm thinking about making a minimal editing change to clarify the point about how the degree is recorded. It looks repetitive to say, "the degree itself (tensor length minus one) records the degree," but it’s okay. I could modify it to say, "the degree itself (tensor length minus one) records that grading." This change might help make the statement clearer without introducing too much complexity. Let's see how that flows in the overall context!
codex
I’m checking the backup file label/ref surface before editing. The user only asked for zero hits, but if a backup file contains local labels like `...arity...`, I need to rename those consistently inside that file rather than just changing a single reference.
exec
/bin/zsh -lc "grep -n 'arity' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '400,440p' standalone/N4_mc4_completion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'arity' chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
order $\le 2s$; and $V_\Lambda$ has weight-$1$ Cartan
generators together with vertex operators $e^\alpha$ of
weight $|\alpha|^2/2 \ge 1$.
\end{proof}

\begin{example}[Non-example: $\beta\gamma$-system with
conformal grading]
\label{ex:non-example}
The $\beta\gamma$-system has a weight-$\tfrac12$ grading that
refines the conformal grading. With respect to the
conformal-weight filtration alone, the strong filtration
axiom fails because the OPE
$\beta(z)\gamma(w) \sim 1/(z-w)$ produces a weight-zero
output from weight-$\tfrac12$ inputs, violating additivity.
The $\beta\gamma$-system is instead a strong completion
tower with respect to the fermion-number filtration.
\end{example}

% ================================================================
% 4. THE ARITY CUTOFF LEMMA
 succeeded in 51ms:
12:and the complementarity that balances quantum corrections against their
43:complementarity) reduces to $\kappa = k$ times a universal form.
105:unordered configurations, curvature, and complementarity are already
112:  (\S\ref{sec:frame-bar-deg1}--\S\ref{sec:frame-complementarity})
116:  complementarity of quantum corrections.  Every theorem of Part~I is
165:\textbf{C}~(\S\ref{sec:frame-complementarity}): $Q_g(\mathcal{H}_k) \oplus Q_g(\mathcal{H}_k^!) = H^*(\overline{\mathcal{M}}_g, \mathcal{Z}_{\mathcal{H}_k})$.
255:degree itself (tensor length minus one) records the arity.  The bar
1069:cogenerator is concentrated in arity~$1$:
1701:\section{Complementarity: Theorem C in action}
1702:\label{sec:frame-complementarity}
1710:\begin{theorem}[Quantum complementarity for Heisenberg; \ClaimStatusProvedHere]
1711:\label{thm:frame-complementarity}
1715:\begin{equation}\label{eq:frame-complementarity}
1736:The complementarity is controlled by Verdier duality on
1743:(Theorem~\ref{thm:quantum-complementarity-main})
1745:complementarity for all Koszul chiral algebra pairs, with the
1756:complementarity assemble into a characteristic hierarchy with three
1770:\item The \emph{proved ambient complementarity complex}
1777:  structure needed for complementarity
1778:  \textup{(}Theorem~\ref{thm:quantum-complementarity-main}\textup{)}.
 succeeded in 52ms:
46:finer invariants: $\kappa$ at arity~$2$, a cubic
47:shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
48:at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
49:largest arity at which the shadow is nonzero; it equals
70:its genus-$0$ component, and complementarity describes its Verdier
86:The genus and arity directions are orthogonal
95:Genus~$1$ sees only~$\kappa$ (arity~$2$).
96:Genus~$2$ first sees~$S_3$ (arity~$3$).
99:\emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
104:arity~$2$, $\Delta = 0$ stratum of this picture: the
159:The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
163:spectral scattering of~$\cA$.  The arity-$3$ component is the
164:\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
200:At arity~$2$, this projection records only one number: the
213:arity-by-arity image of
238:  is the arity-by-arity $\Sigma_n$-coinvariant image of the
245:  at arity~$3$ it contains the Drinfeld associator
278:(the genus-$0$, arity-$3$ MC equation;
279:Theorem~\ref{thm:e1-mc-finite-arity},
280:equation~\eqref{eq:e1-mc-arity3}).
exec
/bin/zsh -lc "grep -n 'e1-mc-arity3\\|e1-mc-finite-arity\\|arity-cutoff\\|all-arity' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'arity' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'arity' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'all-arity\\|arity-' chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
279:Theorem~\ref{thm:e1-mc-finite-arity},
280:equation~\eqref{eq:e1-mc-arity3}).
1322:all-genera modular envelope.  The all-arity master equation
1341:  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
1407:If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
1804:\phantomsection\label{eq:all-arity-master-eq-intro}%
 succeeded in 52ms:
353:\item \textup{(Singularity)}\quad
439:By the singularity condition (ii) of
649:The genus-$g$ quantum corrections (Theorem~B) and complementarity
2717: $\kappa(A)$ are related by complementarity
2718: (Theorem~\ref{thm:central-charge-complementarity}).  An SC-pair
3358:in the brace deformation complex. In arity~$n$, this means
3373:Starting from $G_1$, a partial solution through arity~$N$
3374:produces an obstruction cocycle in arity~$N{+}1$ of the same
3474:  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
3494:  so the corrected arity is removed and the defect is pushed to
3495:  higher arity. This is the precise sense in which one tries to kill
3850:obstruction at arity~$N{+}1$ to extending the Sugawara
3856:applies: the only available harmonic insertions at each arity
3859:at arity~$N{+}1$ is proportional to
3865:Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
3870:no new input beyond the identification of the arity-$N$ obstruction
4935:% At k=-h^v, r diverges (Sugawara singularity).
4963:singularity). Both limits are consistent with
5320:axioms (sesquilinearity, Leibniz, skew-symmetry, Jacobi);
5332:The $\cD$-linearity follows because the PVA
 succeeded in 52ms:
52:homotopy dual factorization algebra~$\cA^!_\infty$; (c)~produces Lagrangian complementarity
55:(Theorem~\ref{thm:quantum-complementarity-main}).
58:achieves (b) but has no bar-cobar content; complementarity (c)
112:Lagrangian complementarity between $\cA$ and $\cA^!$
113:(Theorem~\ref{thm:quantum-complementarity-main});
118:complementarity reduces to the genus-$0$ bar-cobar adjunction,
1307:nonlinearity of the bar differential at genus~$0$, while the shadows
2490:resolution, and the complementarity splitting
2496:(Theorem~\ref{thm:ambient-complementarity-fmp})
2497:makes these subspaces isotropic; the complementarity splitting
2827:the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
2835:the cubic shadow vanishes by weight parity of the $\gamma$
2859:cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
2876:Class~$C$: the cubic shadow vanishes by the parity obstruction on
2920:mixed tree formulas stop at arity~$2$, so
2926:Then every mixed Swiss-cheese operation of arity~$r \geq 3$
2928:The tree-shadow correspondence is operadic: the arity-$r$ mixed
2954:Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
2964:$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
2972:same transferred genus-$0$ tree that defines the mixed arity-$r$
 succeeded in 52ms:
1743:(Theorem~\ref{thm:quantum-complementarity-main})
1778:  \textup{(}Theorem~\ref{thm:quantum-complementarity-main}\textup{)}.
1815:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
2942:$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
3521:  (Theorem~\ref{thm:quantum-complementarity-main}):
exec
/bin/zsh -lc "grep -n '\\\\label{["'^}]*arity'"' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'thm:e1-mc-finite-arity\\|eq:e1-mc-arity3\\|lem:arity-cutoff\\|eq:all-arity-master-eq-intro' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
814:  \begin{equation}\label{eq:complementarity-intro}
989:\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
1804:\phantomsection\label{eq:all-arity-master-eq-intro}%
 succeeded in 50ms:
279:Theorem~\ref{thm:e1-mc-finite-arity},
280:equation~\eqref{eq:e1-mc-arity3}).
1341:  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
1407:If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
1804:\phantomsection\label{eq:all-arity-master-eq-intro}%

thinking
**Gathering context for patching**

I’m noticing a potential issue where `Theorem\ref{thm:e1-mc-finite-degree}` isn’t appearing anywhere else. I think it could be useful to search for `\bArity\b` in different cases. I might need to apply a huge hunk patch and include enough context. It seems I should open smaller segments around specific lines, like lines 40-110 and 150-250, to gather more context for easier patching. Using `sed -n` for specific ranges sounds like a good plan!
codex
I’m drafting the patch now. Before I write it, I’m pulling tight local context around the backup-file hits so I can change label/ref names and nearby prose in one pass instead of doing trial-and-error edits.
exec
/bin/zsh -lc "sed -n '36,110p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,340p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
trace on the open sector, and the \emph{modular
characteristic}~$\kappa(\cA)$ is the universal scalar
measuring this obstruction
(Theorem~\ref{thm:modular-characteristic}).
The bar construction on curves defines a
pronilpotent dg Lie algebra~$\gAmod$ (the modular
convolution algebra), whose Maurer--Cartan
element~$\Theta_\cA$ encodes the full genus expansion.
The finite-order projections $\Theta_\cA^{\leq r}$
(the shadow obstruction tower) extract successively
finer invariants: $\kappa$ at arity~$2$, a cubic
shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
largest arity at which the shadow is nonzero; it equals
the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
(Theorem~\ref{thm:shadow-formality-identification}).
The Heisenberg has $r_{\max} = 2$ (formal,
$\Delta = 0$); affine Kac--Moody algebras have
$r_{\max} = 3$; the $\beta\gamma$ system has
$r_{\max} = 4$; Virasoro and $\mathcal{W}$-algebras
exec
/bin/zsh -lc "sed -n '596,610p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1314,1412p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1798,1808p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1498,1508p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '926,936p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$F\!\Ass$ rather than the commutative cooperad
$\mathrm{Sym}^c$, houses the bar-intrinsic Maurer--Cartan element
\begin{equation}\label{eq:intro-theta-e1}
\Theta_\cA^{\Eone}
\;:=\;
D_\cA^{\Eone} - d_\cA^{(0)}
\;\in\;
\MC\!\bigl({\gAmod}^{\Eone}\bigr).
\end{equation}
The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
genus~$0$ is the \emph{classical $r$-matrix}
$r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
the meromorphic function whose residue at $z = 0$ controls the
spectral scattering of~$\cA$.  The arity-$3$ component is the
\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
components are the higher Yangian/braided coherences that satisfy
the boundary equations of Stasheff associahedra:
classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
quartic $R$-matrix identity for $r_4$, and so on
(Proposition~\ref{prop:e1-shadow-r-matrix}).
 succeeded in 51ms:
splits the genus-$g$ projection into complementary Lagrangians),
\emph{leading coefficient} (Theorem~D extracts the universal scalar
$\kappa(\cA)$), and \emph{coefficient ring} (Theorem~H identifies
$\ChirHoch^*(\cA)$ as the finite-dimensional coefficient space over which~$\Theta_\cA$ varies).
The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
$\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
consists of finite-order projections of this single element;
$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
arity-$3$ projection, and the quartic resonance class~$Q$ is the
arity-$4$ projection.

The element~$\Theta_\cA$ is itself the closed-sector projection
of a larger structure.
The \emph{open/closed MC element}
$\Theta^{\mathrm{oc}}_\cA = \Theta_\cA + \sum \mu^{M_j}$
 succeeded in 51ms:
algebra~$\gAmod$, whose $L_\infty$ structure comes
from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
finite-order projections of~$\Theta_\cA$:
$\kappa$ (arity~$2$),
$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
a projection of the next.  The weight filtration on~$\gAmod$
controls extension; each truncation
$\Theta_\cA^{\le r}$ is constructive without requiring the full
all-genera modular envelope.  The all-arity master equation
$D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
bar-intrinsic construction
(Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
is automatically Maurer--Cartan because $D_\cA^2 = 0$.

\emph{Ring~3: the physics-facing frontier.}
Three axes extend the proved core toward mathematical physics.
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{The $\mathcal W$-algebra axis.}
  Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
  at generic level is completed Koszul.  Strict Koszulity is
 succeeded in 50ms:
\hline
Lattice VOAs (Ch.~\ref{ch:lattice}) &
  $\kappa(V_\Lambda)=\operatorname{rank}(\Lambda)$; curvature-braiding orthogonality; screening operators \\
Free fields (Ch.~\ref{chap:free-fields}) &
  Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
$\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
Kac--Moody (Ch.~\ref{chap:kac-moody}) &
  $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
$\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
  DS reduction as Koszul functor; $\mathcal W_3$ composites; curved $A_\infty$ from higher poles \\
 succeeded in 50ms:
% ================================================================
% Stub labels for external cross-references from body chapters.
% These labels were defined in material that has been relocated
% from this introduction to the relevant body chapters.
% ================================================================
\phantomsection\label{def:modular-homotopy-theory-intro}%
\phantomsection\label{eq:all-arity-master-eq-intro}%
\phantomsection\label{eq:arnold-seed}%
\phantomsection\label{eq:bar-graded-object-intro}%
\phantomsection\label{eq:the-seed}%
\phantomsection\label{eq:universal-MC}%
 succeeded in 51ms:
  = H^*(\overline{\cM}_g,\, Z(\cA))$.

\item \emph{Leading coefficient}
  \textup{(}Theorem~D\textup{)}.
  $\Theta_\cA$ has \textbf{universal scalar projection}.
  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
  $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
  with $\kappa(\cA)$ universal and governed by the
  $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
  for all families.


thinking
**Modifying code patches**

I won't replace the `arity` substring globally; I need word-level replacements instead. For `apply_patch`, we can modify specific lines manually. Using `perl` is possible, but I'll stick to manual edits for snippets. It might be easier to use `apply_patch` with multiple file hunks around each cluster. I'll start with live files and then work on backups. I need to approach this carefully while keeping an eye on article issues like "an arity". Let's draft the patch!
codex
I’ve finished the local pass and I’m applying the replacements now. The only nontrivial part is the backup introduction file, where a few `...arity...` label/ref names also have to change locally to satisfy the zero-hit requirement.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
@@ -3357,3 +3357,3 @@
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
@@ -3372,4 +3372,4 @@
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
@@ -3473,3 +3473,3 @@
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
@@ -3493,4 +3493,4 @@
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
@@ -3504,3 +3504,3 @@
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
@@ -3849,3 +3849,3 @@
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
@@ -3855,6 +3855,6 @@
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
@@ -3864,3 +3864,3 @@
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
@@ -3869,3 +3869,3 @@
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
M /Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -254,3 +254,3 @@
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
@@ -1068,3 +1068,3 @@
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
@@ -1814,3 +1814,3 @@
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
@@ -2941,3 +2941,3 @@
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
@@ -3117,3 +3117,3 @@
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
@@ -3781,3 +3781,3 @@
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
@@ -3786,3 +3786,3 @@
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak
@@ -45,6 +45,6 @@
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
@@ -84,4 +84,4 @@
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
@@ -94,4 +94,4 @@
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
@@ -103,3 +103,3 @@
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
@@ -158,3 +158,3 @@
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
@@ -162,4 +162,4 @@
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
@@ -199,3 +199,3 @@
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
@@ -212,3 +212,3 @@
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
@@ -237,3 +237,3 @@
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
@@ -244,3 +244,3 @@
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
@@ -277,5 +277,5 @@
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
@@ -289,3 +289,3 @@
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
@@ -329,3 +329,3 @@
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
@@ -411,3 +411,3 @@
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
@@ -416,3 +416,3 @@
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
@@ -602,5 +602,5 @@
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
@@ -930,3 +930,3 @@
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
@@ -1316,4 +1316,4 @@
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
@@ -1321,3 +1321,3 @@
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
@@ -1334,4 +1334,4 @@
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
@@ -1339,4 +1339,4 @@
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
@@ -1406,3 +1406,3 @@
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
@@ -1503,3 +1503,3 @@
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
@@ -1803,3 +1803,3 @@
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
@@ -2826,3 +2826,3 @@
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
@@ -2858,3 +2858,3 @@
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
@@ -2919,3 +2919,3 @@
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
@@ -2925,5 +2925,5 @@
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
@@ -2953,3 +2953,3 @@
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
@@ -2963,3 +2963,3 @@
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
@@ -2971,5 +2971,5 @@
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
M /Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex
@@ -418,3 +418,3 @@
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
apply_patch(auto_approved=true) exited 0 in 50ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex
M /Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak
M /Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
M /Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}

file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}


thinking
**Verifying grep commands**

I need to verify the grep command for zero and search for "an degree." There could be remaining hits from eq:e1-mc-arity3 that haven’t been changed. We changed the reference, but maybe there are label definitions elsewhere that I missed.

I should run the exact grep command and also look for case-insensitive hits, just to be thorough. Let’s check if intro.bak still contains eq:e1-mc-arity3 or thm:e1-mc-finite-arity since not all occurrences might have been updated.
codex
The patch is in. I’m running the exact requested grep plus an article sanity check now; if anything survives, I’ll patch again before closing.
exec
/bin/zsh -lc 'git diff -- chapters/theory/chiral_koszul_pairs.tex chapters/theory/en_koszul_duality.tex chapters/theory/introduction.tex.bak chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix standalone/N4_mc4_completion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index a9e4256..d86001d 100644
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -567,7 +567,8 @@ duality theorem:
 \item \emph{$\mathrm{A}_2$}: geometric bar-cobar duality
  (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
  dual pair, applying Verdier duality to the bar coalgebra of one side
- produces the dual factorization algebra of the other.
+ and then reading the result on the post-Verdier side produces the
+ dual factorization algebra of the other.
 \end{itemize}
 $\mathrm{A}_0$ is the Koszul recognition theorem;
 $\mathrm{A}_1$ extracts the dual coalgebra;
@@ -2074,7 +2075,8 @@ them. Condition~\textup{(xii)} implies condition~\textup{(x)}
 \item[\textup{(vi)}] The Barr--Beck--Lurie comparison for the
  bar-cobar adjunction is an equivalence on the fiber over
  $\barBgeom(\cA)$.
-\item[\textup{(vii)}] Factorization homology concentration:
+\item[\textup{(vii)}] Genus-$0$ factorization homology concentration,
exec
/bin/zsh -lc "grep -rni 'an degree' chapters/ appendices/ standalone/" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rni '\\barity\\b' chapters/ appendices/ standalone/" in /Users/raeez/chiral-bar-cobar succeeded in 449ms:
chapters/examples/free_fields.tex:265:$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
appendices/branch_line_reductions.tex:188:\(\Theta^{\mathrm{sc}}_{\cA}\) has Maurer--Cartan degree~\(1\).
 exited 1 in 485ms:

file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}



thinking
**Determining scope of edits**

It seems that our patch didn't introduce "an degree." However, there is a pre-existing "An degree-3" that might stem from earlier changes. The user instructed to remove all remaining 'arity' from Volume I and fix related articles, but I'm questioning if this "assigned files" notion includes those outside the grep hits. Since the explicit task is to ensure no "arity" remains, I think free_fields is indeed within the assigned scope, even if it's not grep-positive.
thinking
**Finding and fixing occurrences**

I think the article fix should apply throughout the searched scope, so I’ll need to fix that file even if it’s not in the grep list. I also need to locate all case-insensitive occurrences of "an degree" in the chapters, appendices, and standalone sections. However, the previous grep gave a false positive because of "Cartan degree." I’m considering using a regex word boundary or something like `grep -rniE '(^|[^[:alpha:]])an degree'` to refine my search.
codex
The `arity` surface is already clean. There is one separate article defect in-scope, `An degree-3`, in `chapters/examples/free_fields.tex`; that wasn’t created by this patch, but it is part of the user’s requested cleanup, so I’m fixing it and then re-running both checks.
exec
/bin/zsh -lc "sed -n '255,272p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\eqref{item:fermion-kappa}:
The free fermion has central charge $c = 1/2$ (a single real
fermion of weight $h = 1/2$; standard from the Virasoro commutation
relations).
Then $\kappa = c/2 = 1/4$ by the universal formula
$\kappa = c \cdot \rho$ with $\rho = 1/2$ for single-generator algebras
(Theorem~\ref{thm:modular-characteristic}).

\eqref{item:fermion-S3}:
The cubic shadow $S_3$ is the degree-$3$ projection of
$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
element requires three fermion insertions on a three-point configuration
space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
is totally antisymmetric in labels. The cyclic permutation
$(123) \mapsto (231)$ on $\overline{C}_3(X)$ acts on the logarithmic
$2$-form space $\Omega^2_{\log}(\overline{C}_3)$ with eigenvalues
$\zeta_3, \zeta_3^2$ (primitive cube roots of unity). Compatibility
with the antisymmetric tensor factor forces the form to lie in the
exec
/bin/zsh -lc "grep -rniE '("'^|[''^[:alpha:]])an degree'"' chapters/ appendices/ standalone/" in /Users/raeez/chiral-bar-cobar succeeded in 641ms:
chapters/examples/free_fields.tex:265:$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
file update:
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}


thinking
**Updating plan and patching**

I need to apply the patch to the free_fields line, keeping it simple—maybe just one patch. After that, I’ll rerun the zero-hit and article grep to make sure everything’s functioning properly. It might also be important to review the plan step to verify any pending updates. So, I guess it’s time to get this patched up! Let's see how it goes.
codex
I’m making one final in-scope prose correction in `chapters/examples/free_fields.tex`: `An degree-$3$` becomes `A degree-$3$`. After that I’ll re-run the exact `arity` grep and the scoped article check together.
file update
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
@@ -264,3 +264,3 @@
 The cubic shadow $S_3$ is the degree-$3$ projection of
-$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
+$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 element requires three fermion insertions on a three-point configuration
apply_patch(auto_approved=true) exited 0 in 56ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 78818ea5fe1c0707bd17b31a0ddd9897dc6e7676..567ed860a8aa3d457f23c2ac4f995346bf7c54cb
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -262,7 +262,7 @@
 
 \eqref{item:fermion-S3}:
 The cubic shadow $S_3$ is the degree-$3$ projection of
-$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
+$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 element requires three fermion insertions on a three-point configuration
 space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
 is totally antisymmetric in labels. The cyclic permutation
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 78818ea5fe1c0707bd17b31a0ddd9897dc6e7676..567ed860a8aa3d457f23c2ac4f995346bf7c54cb
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -262,7 +262,7 @@
 
 \eqref{item:fermion-S3}:
 The cubic shadow $S_3$ is the degree-$3$ projection of
-$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
+$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 element requires three fermion insertions on a three-point configuration
 space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
 is totally antisymmetric in labels. The cyclic permutation
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}


thinking
**Running checks again**

I'm rerunning my checks now, and I wonder if I should specify "a degree-3 element" instead of just "a degree." I feel like I need to ensure I'm getting exact matches with grep, so I might need to look for zero matches. Maybe I should also check for "\barity\b," though I'm not sure if that'll yield anything either. Let's go ahead and run these searches and see what results come up!
exec
/bin/zsh -lc "grep -rniE '("'^|[''^[:alpha:]])an degree'"' chapters/ appendices/ standalone/" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -rni '\\barity\\b' chapters/ appendices/ standalone/" in /Users/raeez/chiral-bar-cobar exited 1 in 489ms:

 exited 1 in 689ms:

file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 78818ea5fe1c0707bd17b31a0ddd9897dc6e7676..567ed860a8aa3d457f23c2ac4f995346bf7c54cb
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -262,7 +262,7 @@
 
 \eqref{item:fermion-S3}:
 The cubic shadow $S_3$ is the degree-$3$ projection of
-$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
+$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 element requires three fermion insertions on a three-point configuration
 space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
 is totally antisymmetric in labels. The cyclic permutation
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}


thinking
**Considering findings organization**

The user is asking for a structured way to present findings on "remaining arity occurrence." It makes sense to group these by file, especially since they want to address issues and apply fixes all at once. I should also think about including a summary of the exact edits made—quoting the content before and after changes could be useful. Maybe I can list the changed tokens in bullet points for clarity. Let's make this as clear and helpful as possible!
Plan update
All in-scope `arity` hits were patched, the stray `An degree` article defect was fixed, and both verification greps now return no output.
  ✓ Inspect the exact hit contexts in the five grep-positive files
  ✓ Apply minimal replacements from arity to degree, including article fixes
  ✓ Verify grep -rni '\barity\b' chapters/ appendices/ standalone/ returns zero
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 78818ea5fe1c0707bd17b31a0ddd9897dc6e7676..567ed860a8aa3d457f23c2ac4f995346bf7c54cb
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -262,7 +262,7 @@
 
 \eqref{item:fermion-S3}:
 The cubic shadow $S_3$ is the degree-$3$ projection of
-$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
+$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 element requires three fermion insertions on a three-point configuration
 space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
 is totally antisymmetric in labels. The cyclic permutation
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}

exec
/bin/zsh -lc "grep -n 'mixed Swiss-cheese tree of degree\\|mixed Swiss-cheese degree-\\|mixed tree formulas stop at degree\\|mixed degree-' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2827:the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
2859:cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
2920:mixed tree formulas stop at degree~$2$, so
2972:same transferred genus-$0$ tree that defines the mixed degree-$r$
2974:so that tree would determine a nontrivial mixed degree-$r$ Massey
exec
/bin/zsh -lc "grep -n 'THE DEGREE CUTOFF LEMMA' standalone/N4_mc4_completion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'A degree-\\"'$3'"\\"'$'"' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'finer invariants: .*degree~\\"'$2'"\\|degree-by-degree image\\|thm:e1-mc-finite-degree\\|lem:degree-cutoff\\|all-degree master equation\\|shadow terminates at degree~\\"'$4'"\\|all-degree-master-eq-intro' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'records the degree\\|concentrated in degree~\\"'$1'"\\|through degree~\\"'$4'"\\|all-degree limit\\|degree-\\"'$3'"\\|for some degree~\\"'$n'"\\|cochain of degree~\\"'$n'"' chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'In degree~\\"'$n'"\\|through degree~\\"'$N'"\\|lowest-degree\\|corrected degree\\|each degree\\|every degree\\|degree-\\"'$N'"' chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
265:$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 succeeded in 52ms:
419:% 4. THE DEGREE CUTOFF LEMMA
 succeeded in 51ms:
46:finer invariants: $\kappa$ at degree~$2$, a cubic
213:degree-by-degree image of
279:Theorem~\ref{thm:e1-mc-finite-degree},
1322:all-genera modular envelope.  The all-degree master equation
1341:  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
1407:If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
1504:  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
1804:\phantomsection\label{eq:all-degree-master-eq-intro}%
 succeeded in 51ms:
255:degree itself (tensor length minus one) records the degree.  The bar
546:The degree-$3$ computation below is the first where the cancellation
550:\subsection{\texorpdfstring{Explicit degree-$3$ computation ($n = 3$, four points)}{Explicit degree-3 computation (n = 3, four points)}}
553:A degree-$3$ bar element lives on $\overline{C}_4(X)$ with four
821:The degree-$3$ computation reveals a structural feature.  For
1069:cogenerator is concentrated in degree~$1$:
1815:Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
2942:$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
3782:for some degree~$n$.  The Hochschild differential is
3787:a cochain of degree~$n$ is determined by
 succeeded in 51ms:
3358:in the brace deformation complex. In degree~$n$, this means
3373:Starting from $G_1$, a partial solution through degree~$N$
3474:  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
3494:  so the corrected degree is removed and the defect is pushed to
3856:applies: the only available harmonic insertions at each degree
3865:Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
3870:no new input beyond the identification of the degree-$N$ obstruction
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 78818ea5fe1c0707bd17b31a0ddd9897dc6e7676..567ed860a8aa3d457f23c2ac4f995346bf7c54cb
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -262,7 +262,7 @@
 
 \eqref{item:fermion-S3}:
 The cubic shadow $S_3$ is the degree-$3$ projection of
-$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
+$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 element requires three fermion insertions on a three-point configuration
 space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
 is totally antisymmetric in labels. The cyclic permutation
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}


thinking
**Refining labeling changes**

I noticed there's an additional label change at 1804 that’s not referenced in the link. I could consider linking to line 46 and mentioning the other specific edit names. That seems okay! Maybe I'll format this as a bullet list, starting each bullet with "PROBLEM at [file](...:line): ... Exact edit applied: ...”. It feels like a clean approach. Let's create something precise and concise!
codex
- PROBLEM at [chapters/theory/chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:2827): 9 remaining `arity` usages on the Swiss-cheese operation surface. Exact edit applied: `arity` -> `degree` in `mixed Swiss-cheese tree of arity~$r$`, `mixed Swiss-cheese arity-$r$ operation`, `mixed tree formulas stop at arity~$2$`, `operations of arity`, and `mixed arity-$r$ Massey` at lines 2827, 2859, 2920, 2926, 2928, 2954, 2964, 2972, 2974.

- PROBLEM at [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3358): 11 remaining `arity` usages in the topologization obstruction discussion. Exact edit applied: `In arity~$n$` -> `In degree~$n$`; `through/in arity~$N{+}1$` -> `through/in degree~$N{+}1$`; `lowest-arity` -> `lowest-degree`; `corrected arity`/`higher arity` -> `corrected degree`/`higher degree`; `each arity`/`every arity` -> `each degree`/`every degree`; `arity-$N$ obstruction` -> `degree-$N$ obstruction`.

- PROBLEM at [chapters/theory/introduction.tex.bak](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex.bak:46): backup surface still contained many `arity` phrases plus local ref/label names. Exact edit applied: `arity~$2/3/4$` -> `degree~$2/3/4$`; `largest arity` -> `largest degree`; `arity-by-arity` -> `degree-by-degree`; `all arities`/`all-arity` -> `all degrees`/`all-degree`; `arity cutoff` -> `degree cutoff`; `\ref{thm:e1-mc-finite-arity}` -> `\ref{thm:e1-mc-finite-degree}`; `\eqref{eq:e1-mc-arity3}` -> `\eqref{eq:e1-mc-degree3}`; `\ref{lem:arity-cutoff}` -> `\ref{lem:degree-cutoff}`; `\label{eq:all-arity-master-eq-intro}` -> `\label{eq:all-degree-master-eq-intro}`.

- PROBLEM at [chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix](/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:255): backup surface still contained 7 `arity` usages. Exact edit applied: `records the arity` -> `records the degree`; `arity~$1/2/3/4$` -> `degree~$1/2/3/4$`; `all-arity limit` -> `all-degree limit`; `for some arity~$n$`/`cochain of arity~$n$` -> `for some degree~$n$`/`cochain of degree~$n$`.

- PROBLEM at [standalone/N4_mc4_completion.tex](/Users/raeez/chiral-bar-cobar/standalone/N4_mc4_completion.tex:419): one case-insensitive `ARITY` hit remained in a section comment. Exact edit applied: `THE ARITY CUTOFF LEMMA` -> `THE DEGREE CUTOFF LEMMA`.

- PROBLEM at [chapters/examples/free_fields.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/free_fields.tex:265): in-scope article defect after the terminology shift. Exact edit applied: `An degree-$3$` -> `A degree-$3$`.

Verification: `grep -rni '\barity\b' chapters/ appendices/ standalone/` returns no hits, and `grep -rniE '(^|[^[:alpha:]])an degree' chapters/ appendices/ standalone/` also returns no hits.
file update:
diff --git a/chapters/examples/free_fields.tex b/chapters/examples/free_fields.tex
index 78818ea5fe1c0707bd17b31a0ddd9897dc6e7676..567ed860a8aa3d457f23c2ac4f995346bf7c54cb
--- a/chapters/examples/free_fields.tex
+++ b/chapters/examples/free_fields.tex
@@ -262,7 +262,7 @@
 
 \eqref{item:fermion-S3}:
 The cubic shadow $S_3$ is the degree-$3$ projection of
-$\Theta_{\mathcal{F}}$ in the modular convolution algebra. An degree-$3$
+$\Theta_{\mathcal{F}}$ in the modular convolution algebra. A degree-$3$
 element requires three fermion insertions on a three-point configuration
 space. By fermionic antisymmetry, $\psi_1 \otimes \psi_2 \otimes \psi_3$
 is totally antisymmetric in labels. The cyclic permutation
diff --git a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
index 35268cd9afb7fcc164fc52b08126d5c3c4c7ef9e..65cee60eb99d11add7451146de7bb27f5f556dbe
--- a/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
+++ b/chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix
@@ -252,7 +252,7 @@
 and an $n$-form in the log-FM sense) carries bar degree~$n$ in
 the bar complex grading.  The logarithmic forms $\eta_{ij}$
 carry form-degree~$1$ but cohomological degree~$0$; the bar
-degree itself (tensor length minus one) records the arity.  The bar
+degree itself (tensor length minus one) records the degree.  The bar
 differential has $|d_{\mathrm{res}}| = +1$ in cohomological degree,
 reducing bar degree by~$1$ (see Appendix~\ref{app:signs}).
 
@@ -1066,7 +1066,7 @@
 image of the operad component $\mathrm{Lie}(n)$ under the
 one-dimensional representation, not the operad component itself,
 which has dimension $(n{-}1)!$.)  Dually, the cofree Lie coalgebra on one
-cogenerator is concentrated in arity~$1$:
+cogenerator is concentrated in degree~$1$:
 \[
 \mathrm{coLie}^{\mathrm{ch}}(V^*) \;\cong\; V^*
 \quad\text{as a graded vector space.}
@@ -1812,7 +1812,7 @@
 
 \begin{remark}[Hierarchy and status]%
 \label{rem:frame-kappa-not-fundamental}
-Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through arity~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-arity limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
+Definition~\ref{def:frame-modular-package} is a hierarchy: items~(1)--(3) are proved (Theorems~\ref{thm:modular-characteristic}, \ref{thm:quantum-complementarity-main}, \ref{thm:spectral-characteristic}); item~(4), the shadow obstruction tower $\Theta_{\mathcal{A}}^{\leq r}$ (Definition~\ref{def:shadow-postnikov-tower}), is proved at finite order through degree~$4$, with one-channel line concentration of the minimal class on the simple-Lie-symmetry locus (Corollary~\ref{cor:scalar-saturation}) and scalar saturation only on the proved scalar lane (Definition~\ref{def:scalar-lane}); the all-degree limit exists by the bar-intrinsic construction (Theorem~\ref{thm:mc2-bar-intrinsic}).  The genus-$1$ coefficient $\kappa(\mathcal{A})$ ($= k$ for Heisenberg, $c/2$ for Virasoro, $(k+h^\vee)\dim(\mathfrak{g})/(2h^\vee)$ for KM) is the scalar level $\Theta_{\mathcal{A}}^{\leq 2}$ of the tower, not the fundamental object.
 \end{remark}
 
 \begin{remark}[The shadow metric for Heisenberg]%
@@ -2939,7 +2939,7 @@
 the fundamental relation among the logarithmic
 $1$-forms $\omega_{ij} = d\log(z_i - z_j)$ on
 $\mathrm{FM}_3(\bC)$.  At the bar-complex level,
-$d^2 = 0$ on the arity-$3$ component of $\barB^{\mathrm{ord}}(A)$
+$d^2 = 0$ on the degree-$3$ component of $\barB^{\mathrm{ord}}(A)$
 reduces precisely to the Arnold
 relation~\eqref{eq:rosetta-arnold-pf} tensored with the Jacobi
 identity for the Lie bracket.
@@ -3115,7 +3115,7 @@
 In each case, the \emph{ordered} bar complex $\barB^{\mathrm{ord}}(A)$
 on the tensor coalgebra $T^c(s^{-1}\bar{A})$ is the primitive
 object: its deconcatenation coproduct encodes the non-cocommutative
-braiding, and $r(z)$ lives at arity~$2$ in its convolution algebra
+braiding, and $r(z)$ lives at degree~$2$ in its convolution algebra
 $\fg^{\Eone}_A$.  The \emph{symmetric} bar
 $\barB^{\Sigma}(A)$ on $\mathrm{Sym}^c(s^{-1}\bar{A})$
 is the $\Sigma_n$-coinvariant quotient, and the modular
@@ -3779,12 +3779,12 @@
 \mathcal{H}_k)$ is a map
 $f \colon \mathcal{H}_k^{\otimes n} \to
 \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$
-for some arity~$n$.  The Hochschild differential is
+for some degree~$n$.  The Hochschild differential is
 $\delta(f) = [m, f]$, where $m$ is the $A_\infty$-structure
 (for Heisenberg: $m_2$ is the OPE, $m_k = 0$ for $k \geq 3$).
 
 Since $\mathcal{H}_k$ is generated by a single current~$\alpha$,
-a cochain of arity~$n$ is determined by
+a cochain of degree~$n$ is determined by
 $f(\alpha, \ldots, \alpha; \lambda_1, \ldots, \lambda_{n-1})
 \in \mathcal{H}_k((\lambda_1))\cdots((\lambda_{n-1}))$.
 
diff --git a/chapters/theory/chiral_koszul_pairs.tex b/chapters/theory/chiral_koszul_pairs.tex
index 4de065a89f850d6a84b354d1f7e9b16c36aec04a..d86001d4e216490c00fe113f2af7b20b76193353
--- a/chapters/theory/chiral_koszul_pairs.tex
+++ b/chapters/theory/chiral_koszul_pairs.tex
@@ -2824,7 +2824,7 @@
 Under the averaging map
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)},
-the mixed Swiss-cheese tree of arity~$r$ projects to the degree-$r$
+the mixed Swiss-cheese tree of degree~$r$ projects to the degree-$r$
 shadow. Since there is no primitive tree for $r \geq 3$,
 all higher mixed-sector operations vanish.
 For class~$L$\textup{:} the affine KM OPE has at most a double pole; the
@@ -2856,7 +2856,7 @@
 Wick's theorem gives Pfaffian factorization by the basic contraction
 $\psi(z)\psi^*(w) \sim (z-w)^{-1}$, so again no connected tree with
 $r \geq 3$ survives after extracting the binary pairings. In all three
-cases the mixed Swiss-cheese arity-$r$ operation is the open-colored
+cases the mixed Swiss-cheese degree-$r$ operation is the open-colored
 lift of the same genus-$0$ tree sum whose closed projection is
 $S_r(\cA)$; equivalently,
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
@@ -2917,15 +2917,15 @@
 Proposition~\ref{prop:swiss-cheese-nonformality-by-class}:
 the class-$G$ row consists of the Gaussian families Heisenberg,
 lattice VOA, and free fermion, and in each case the genus-$0$
-mixed tree formulas stop at arity~$2$, so
+mixed tree formulas stop at degree~$2$, so
 $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$.
 This uses the same operadic/Wick-factorization argument in all three
 families and does not appeal to any invariant bilinear form.
 
 For the converse, suppose~$\cA$ is SC-formal.
-Then every mixed Swiss-cheese operation of arity~$r \geq 3$
+Then every mixed Swiss-cheese operation of degree~$r \geq 3$
 vanishes in the Swiss-cheese structure with open colour~$\cA$.
-The tree-shadow correspondence is operadic: the arity-$r$ mixed
+The tree-shadow correspondence is operadic: the degree-$r$ mixed
 tree and the degree-$r$ shadow are produced by the same genus-$0$
 tree-transfer formula, with the same propagator on internal edges;
 the only difference is the output colour, and passage to the
@@ -2951,7 +2951,7 @@
 
 For the forward direction, class~$G$ is the Gaussian locus where the
 genus-$0$ transfer is generated by the binary two-point kernel alone.
-Every connected Swiss-cheese tree of arity $r \geq 3$ therefore
+Every connected Swiss-cheese tree of degree $r \geq 3$ therefore
 factors through binary pairings and carries no primitive higher
 vertex, so the mixed operations vanish:
 $m_k^{\mathrm{SC}} = 0$ for all $k \geq 3$.
@@ -2961,7 +2961,7 @@
 
 For the converse, assume that~$\cA$ is SC-formal. Then the minimal
 $\mathrm{SC}^{\mathrm{ch,top}}$-model on the pair
-$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of arity
+$(\ChirHoch^*(\cA,\cA), \cA)$ has no mixed operations of degree
 $k \geq 3$. If some $S_r(\cA)$ with $r \geq 3$ were nonzero, then
 Theorem~\ref{thm:shadow-formality-identification},
 Proposition~\ref{prop:shadow-tower-three-lenses}, and the averaging
@@ -2969,9 +2969,9 @@
 $\operatorname{av}(\Theta_\cA^{\Eone}) = \Theta_\cA$
 \textup{(}Theorem~\ref{thm:e1-primacy}\textup{)}
 would identify $S_r(\cA)$ with the closed-color projection of the
-same transferred genus-$0$ tree that defines the mixed arity-$r$
+same transferred genus-$0$ tree that defines the mixed degree-$r$
 operation. A nonzero closed projection cannot come from the zero tree,
-so that tree would determine a nontrivial mixed arity-$r$ Massey
+so that tree would determine a nontrivial mixed degree-$r$ Massey
 product, contradicting SC-formality. Hence
 $S_r(\cA) = 0$ for every $r \geq 3$.
 
diff --git a/chapters/theory/en_koszul_duality.tex b/chapters/theory/en_koszul_duality.tex
index 880a4e2fb68efaa3624880b0fdde2b4f1ce91703..a343ff696342697b3bd0b77158d74a65f2cf571f
--- a/chapters/theory/en_koszul_duality.tex
+++ b/chapters/theory/en_koszul_duality.tex
@@ -3355,7 +3355,7 @@
 \[
   [m, G] \;=\; \partial_z
 \]
-in the brace deformation complex. In arity~$n$, this means
+in the brace deformation complex. In degree~$n$, this means
 \[
   \partial_z m_n
   \;=\;
@@ -3370,8 +3370,8 @@
 the Stasheff coherence equations for an
 $A_\infty$-derivation homotopy.
 
-Starting from $G_1$, a partial solution through arity~$N$
-produces an obstruction cocycle in arity~$N{+}1$ of the same
+Starting from $G_1$, a partial solution through degree~$N$
+produces an obstruction cocycle in degree~$N{+}1$ of the same
 deformation complex. Vanishing of this entire tower is
 equivalent to the original-complex lift of
 Theorem~\ref{thm:topologization}\textup{(iii)}.
@@ -3471,7 +3471,7 @@
   compositions, $D^{(1)}$ is $d_m := [m,-]$-closed, so the first
   obstruction is a genuine deformation-cohomology class.
 
-  If the lowest-arity component of $D^{(r)}$ is $d_m$-exact and one
+  If the lowest-degree component of $D^{(r)}$ is $d_m$-exact and one
   can choose a translation-invariant primitive $\eta_r$ for that
   component, then after the standard suspension that identifies the
   brace deformation complex with its controlling dg Lie algebra,
@@ -3491,8 +3491,8 @@
     \;=\;
     \exp(\operatorname{ad}_{h_r})\,D^{(r)},
   \]
-  so the corrected arity is removed and the defect is pushed to
-  higher arity. This is the precise sense in which one tries to kill
+  so the corrected degree is removed and the defect is pushed to
+  higher degree. This is the precise sense in which one tries to kill
   the $Q$-exact term by a gauge transformation.
 
   The open affine problem is therefore not whether one can write down
@@ -3502,7 +3502,7 @@
   depth, and the harmonic cubic obstruction already vanishes by
   Jacobi
   \textup{(}Proposition~\textup{\ref{prop:chain-level-three-obstructions}}\textup{)}.
-  These facts suggest that only finitely many arities need
+  These facts suggest that only finitely many degrees need
   correction in the affine case. What remains to prove is that the
   higher defect classes in the affine brace deformation complex are
   exhausted by this finite Jacobi-controlled list.
@@ -3847,27 +3847,27 @@
 the infinite coherence tower
 $[m, G] = \partial_z$ of
 Remark~\ref{rem:topologization-chain-vs-cohomology}: the
-obstruction at arity~$N{+}1$ to extending the Sugawara
+obstruction at degree~$N{+}1$ to extending the Sugawara
 null-homotopy $G = (G_1, \ldots, G_N)$ lands in the brace
 deformation complex. For class~M, this obstruction
 does not vanish on the nose.
 The same harmonic-factorisation mechanism of
 Theorem~\ref{thm:bv-bar-coderived}(iv)
-applies: the only available harmonic insertions at each arity
+applies: the only available harmonic insertions at each degree
 pass through the curvature direction
 $m_0 = \kappa(\cA) \cdot \omega_g$, so the obstruction cocycle
-at arity~$N{+}1$ is proportional to
+at degree~$N{+}1$ is proportional to
 $m_0^{\lfloor (N+1)/2 \rfloor}$. In the coderived category
 $D^{\mathrm{co}}$, every $m_0$-power-torsion object is
 coacyclic
 (Positselski~\cite[Proposition~3.5]{Positselski11}; the same
 bounded-below filtered criterion used in the proof of
-Theorem~\ref{thm:bv-bar-coderived}). Hence every arity
+Theorem~\ref{thm:bv-bar-coderived}). Hence every degree
 obstruction is absorbed, and the full coherence tower collapses
 in~$D^{\mathrm{co}}$.
 
 This step is a direct consequence of proved results and requires
-no new input beyond the identification of the arity-$N$ obstruction
+no new input beyond the identification of the degree-$N$ obstruction
 with an $m_0$-power, which follows from the proof of
 Proposition~\ref{prop:chain-level-three-obstructions}.
 
diff --git a/chapters/theory/introduction.tex.bak b/chapters/theory/introduction.tex.bak
index 21846962efd7427a1352cdc4370649c3f1a21b23..92761a997edbef5dfaa64cdbb452c60e372ade7c
--- a/chapters/theory/introduction.tex.bak
+++ b/chapters/theory/introduction.tex.bak
@@ -43,10 +43,10 @@
 element~$\Theta_\cA$ encodes the full genus expansion.
 The finite-order projections $\Theta_\cA^{\leq r}$
 (the shadow obstruction tower) extract successively
-finer invariants: $\kappa$ at arity~$2$, a cubic
-shadow~$C$ at arity~$3$, a quartic resonance class~$Q$
-at arity~$4$.  The shadow depth $r_{\max}(\cA)$ is the
-largest arity at which the shadow is nonzero; it equals
+finer invariants: $\kappa$ at degree~$2$, a cubic
+shadow~$C$ at degree~$3$, a quartic resonance class~$Q$
+at degree~$4$.  The shadow depth $r_{\max}(\cA)$ is the
+largest degree at which the shadow is nonzero; it equals
 the $L_\infty$ formality level of the genus-$0$ part of $\gAmod$
 (Theorem~\ref{thm:shadow-formality-identification}).
 The Heisenberg has $r_{\max} = 2$ (formal,
@@ -82,8 +82,8 @@
 (Theorem~\ref{thm:shadow-formality-identification}):
 the genus-$0$ shadow obstruction tower coincides with the $L_\infty$
 formality obstruction tower of the convolution algebra
-at all arities; genus $g \geq 1$ corrections form a separate layer.
-The genus and arity directions are orthogonal
+at all degrees; genus $g \geq 1$ corrections form a separate layer.
+The genus and degree directions are orthogonal
 (Remark~\ref{rem:two-orthogonal-axes}).
 The \emph{visibility formula}
 (Corollary~\ref{cor:shadow-visibility-genus})
@@ -92,8 +92,8 @@
 g_{\min}(S_r) \;=\; \lfloor r/2 \rfloor + 1
 \qquad (r \geq 3).
 \end{equation}
-Genus~$1$ sees only~$\kappa$ (arity~$2$).
-Genus~$2$ first sees~$S_3$ (arity~$3$).
+Genus~$1$ sees only~$\kappa$ (degree~$2$).
+Genus~$2$ first sees~$S_3$ (degree~$3$).
 Genus~$3$ first sees~$S_4$ and~$S_5$ (arities~$4$,~$5$).
 In general, two new shadow coefficients enter at each genus.
 \emph{Complementarity} (Theorem~\ref{thm:quantum-complementarity-main}):
@@ -101,7 +101,7 @@
 a Lagrangian decomposition that constrains the Koszul
 dual pair.
 Classical Koszul duality over a point is the genus~$0$,
-arity~$2$, $\Delta = 0$ stratum of this picture: the
+degree~$2$, $\Delta = 0$ stratum of this picture: the
 formal, Gaussian case where the tower terminates
 immediately.  Everything beyond this stratum is new.
 
@@ -156,12 +156,12 @@
 \;\in\;
 \MC\!\bigl({\gAmod}^{\Eone}\bigr).
 \end{equation}
-The arity-$2$ component of $\Theta_\cA^{\Eone}$ at
+The degree-$2$ component of $\Theta_\cA^{\Eone}$ at
 genus~$0$ is the \emph{classical $r$-matrix}
 $r(z) \in \End(V^{\otimes 2}) \otimes \cO(*\Delta)$,
 the meromorphic function whose residue at $z = 0$ controls the
-spectral scattering of~$\cA$.  The arity-$3$ component is the
-\emph{KZ associator} $r_3(z_1, z_2)$, and the arity-$\ge 4$
+spectral scattering of~$\cA$.  The degree-$3$ component is the
+\emph{KZ associator} $r_3(z_1, z_2)$, and the degree-$\ge 4$
 components are the higher Yangian/braided coherences that satisfy
 the boundary equations of Stasheff associahedra:
 classical Yang--Baxter for $r(z)$, the pentagon for $r_3$, the
@@ -197,7 +197,7 @@
 \;=\;
 \Theta_\cA.
 \end{equation}
-At arity~$2$, this projection records only one number: the
+At degree~$2$, this projection records only one number: the
 $\Sigma_2$-coinvariant of the residue of $r(z)$ at $z = 0$ is the
 modular characteristic
 \begin{equation}\label{eq:intro-kappa-from-r}
@@ -210,7 +210,7 @@
 where the trace is the cyclic trace on $\End(V^{\otimes 2})$.  The
 shadow obstruction tower
 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ is the
-arity-by-arity image of
+degree-by-degree image of
 $(r(z), r_3, r_4, \ldots)$ under~$\operatorname{av}$
 (Proposition~\ref{prop:e1-shadow-r-matrix}).  The $\Eone$ side
 contains the matrix-valued meromorphic function; the $\Einf$ side
@@ -235,14 +235,14 @@
   \textup{(}\eqref{eq:intro-av-theta}\textup{)}.
   In particular, the shadow obstruction tower
   $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$
-  is the arity-by-arity $\Sigma_n$-coinvariant image of the
+  is the degree-by-degree $\Sigma_n$-coinvariant image of the
   $R$-matrix tower $(r(z), r_3, r_4, \ldots)$.
 \item \textup{(Bracket preservation.)}
   $\operatorname{av}$ preserves the dg~Lie bracket
   by $\Sigma_n$-equivariance of the operad composition maps.
 \item \textup{(Non-splitting.)}
   The kernel\/ $\ker(\operatorname{av})$ is non-trivial:
-  at arity~$3$ it contains the Drinfeld associator
+  at degree~$3$ it contains the Drinfeld associator
   $\Phi_{\mathrm{KZ}}(\cA)$, which is
   annihilated by\/ $\operatorname{av}$ but satisfies the
   pentagon equation in\/~${\gAmod}^{\Eone}$.
@@ -275,9 +275,9 @@
 For (iv), the Drinfeld associator
 $\Phi_{\mathrm{KZ}}(\cA) \in \ker(\operatorname{av})_{0,3}$
 satisfies the pentagon equation in ${\gAmod}^{\Eone}$
-(the genus-$0$, arity-$3$ MC equation;
-Theorem~\ref{thm:e1-mc-finite-arity},
-equation~\eqref{eq:e1-mc-arity3}).
+(the genus-$0$, degree-$3$ MC equation;
+Theorem~\ref{thm:e1-mc-finite-degree},
+equation~\eqref{eq:e1-mc-degree3}).
 Its $\Sigma_3$-symmetrization vanishes because the
 pentagon identity is antisymmetric under transposition
 of the two internal edges.
@@ -287,7 +287,7 @@
 Such a section would lift the commutative MC element
 $\Theta_\cA$ to an ordered element in the image of~$s$;
 but the pentagon constraint on $\ker(\operatorname{av})$
-forces the arity-$3$ component of any lift to involve
+forces the degree-$3$ component of any lift to involve
 $\Phi_{\mathrm{KZ}}$, which does not lie in the image
 of any linear section.
 \end{proof}
@@ -327,7 +327,7 @@
 $\Eone = \mathrm{Ass}$ is the primitive associative operad and
 $\Einf = \Com$ arises from it as the colimit
 $\Com = \colim_n E_n$ or, equivalently, by
-$\Sigma_n$-coinvariants on each arity.  At the level of cofree
+$\Sigma_n$-coinvariants on each degree.  At the level of cofree
 coalgebras, Stasheff's theorem identifies $T^c$ (deconcatenation)
 as the universal cofree conilpotent coalgebra; the symmetric
 cooperad $\mathrm{Sym}^c$ is recovered from $T^c$ by external
@@ -409,12 +409,12 @@
 algebra $\gAmod$ is now read as $\operatorname{av}({\gAmod}^{\Eone})$, the
 universal MC element $\Theta_\cA$ as $\operatorname{av}(\Theta_\cA^{\Eone})$,
 and the modular characteristic $\kappa(\cA)$ as
-$\operatorname{av}(r(z))$ at arity~$2$.
+$\operatorname{av}(r(z))$ at degree~$2$.
 The ordered theory of
 Chapter~\ref{chap:e1-modular-koszul} is the upstream object;
 the symmetric theory is its image.
 
-The $\Eone$ side is strictly richer: at arity~$2$ alone it
+The $\Eone$ side is strictly richer: at degree~$2$ alone it
 distinguishes algebras that the symmetric side identifies.
 The Heisenberg $\Eone$-shadow $r_{\cH_k}(z) = k\Omega/z$ and the
 $\widehat{\mathfrak{sl}}_2$-shadow
@@ -600,9 +600,9 @@
 The shadow obstruction tower $\Theta_\cA^{\leq 2}$,
 $\Theta_\cA^{\leq 3}$, $\Theta_\cA^{\leq 4}$, \ldots{}
 consists of finite-order projections of this single element;
-$\kappa$ is the arity-$2$ projection, the cubic shadow~$C$ is the
-arity-$3$ projection, and the quartic resonance class~$Q$ is the
-arity-$4$ projection.
+$\kappa$ is the degree-$2$ projection, the cubic shadow~$C$ is the
+degree-$3$ projection, and the quartic resonance class~$Q$ is the
+degree-$4$ projection.
 
 The element~$\Theta_\cA$ is itself the closed-sector projection
 of a larger structure.
@@ -928,7 +928,7 @@
 \item \emph{Leading coefficient}
   \textup{(}Theorem~D\textup{)}.
   $\Theta_\cA$ has \textbf{universal scalar projection}.
-  On the uniform-weight lane, the arity-$2$ genus-$g$ component is
+  On the uniform-weight lane, the degree-$2$ genus-$g$ component is
   $\mathrm{obs}_g(\cA) = \kappa(\cA)\,\lambda_g$ at all genera,
   with $\kappa(\cA)$ universal and governed by the
   $\hat{A}$-genus.  At genus~$1$ this holds unconditionally
@@ -1314,12 +1314,12 @@
 algebra~$\gAmod$, whose $L_\infty$ structure comes
 from the Feynman transform of the modular operad; $\Convstr$ is its strict model.  The shadow obstruction tower consists of
 finite-order projections of~$\Theta_\cA$:
-$\kappa$ (arity~$2$),
-$\mathfrak{C}$ (arity~$3$), $\mathfrak{Q}$ (arity~$4$), each
+$\kappa$ (degree~$2$),
+$\mathfrak{C}$ (degree~$3$), $\mathfrak{Q}$ (degree~$4$), each
 a projection of the next.  The weight filtration on~$\gAmod$
 controls extension; each truncation
 $\Theta_\cA^{\le r}$ is constructive without requiring the full
-all-genera modular envelope.  The all-arity master equation
+all-genera modular envelope.  The all-degree master equation
 $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is proved by the
 bar-intrinsic construction
 (Theorem~\ref{thm:mc2-bar-intrinsic}): $\Theta_\cA := D_\cA - \dzero$
@@ -1332,13 +1332,13 @@
   Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
   at generic level is completed Koszul.  Strict Koszulity is
   exceptional: the subregular family $\mathcal W_n^{(2)}$ has
-  unbounded canonical homotopy arity, and the classical $W_3$ sector
-  defines the first finite-arity modular higher-spin package.
+  unbounded canonical homotopy degree, and the classical $W_3$ sector
+  defines the first finite-degree modular higher-spin package.
   MC4 is proved: the strong completion-tower theorem
   (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
   completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
-  with automatic continuity via the arity cutoff
-  (Lemma~\ref{lem:arity-cutoff}) and coefficient-stability criterion
+  with automatic continuity via the degree cutoff
+  (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
   (Theorem~\ref{thm:coefficient-stability-criterion}).
   The DS-HPL transfer theorem
   (Volume~II, Theorem~thm:ds-hpl-transfer) closes the
@@ -1404,7 +1404,7 @@
 
 \smallskip
 \noindent\emph{Mechanism~1: strong filtration.}
-If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the arity cutoff (Lemma~\ref{lem:arity-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
+If the algebra~$\cA$ carries a filtration satisfying the strong axiom $\mu_r(F^{i_1}\cA,\dots,F^{i_r}\cA) \subset F^{i_1+\cdots+i_r}\cA$, the degree cutoff (Lemma~\ref{lem:degree-cutoff}) makes continuity and Mittag--Leffler automatic.  The completion closure $\CompCl(\Fft)$ then carries a quasi-inverse bar-cobar homotopy equivalence (Corollary~\ref{cor:completion-closure-equivalence}), stable under MC twisting (Theorem~\ref{thm:mc-twisting-closure}), with completed twisting representability (Theorem~\ref{thm:completed-twisting-representability}).  This applies to: $V_k(\mathfrak g)$ (non-critical), $\mathrm{Vir}_c$ (all~$c$), $\mathcal{W}^k(\mathfrak g, f_{\mathrm{prin}})$ (non-critical), lattice algebras (Proposition~\ref{prop:standard-strong-filtration}).
 
 \smallskip
 \noindent\emph{Mechanism~2: weight cutoff.}
@@ -1501,7 +1501,7 @@
 Free fields (Ch.~\ref{chap:free-fields}) &
   Heisenberg, free fermion; Eisenstein genus expansion; periodic table of the volume \\
 $\beta\gamma$ system (Ch.~\ref{chap:beta-gamma}) &
-  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at arity~$4$ \\
+  First nonabelian computation; $\mu_{\beta\gamma}=0$ (rank-one rigidity); shadow terminates at degree~$4$ \\
 Kac--Moody (Ch.~\ref{chap:kac-moody}) &
   $\widehat{\mathfrak g}_k$ bar complex; Feigin--Frenkel = Koszul duality; PBW at all genera \\
 $\mathcal W$-algebras (Ch.~\ref{chap:w-algebras}) &
@@ -1801,7 +1801,7 @@
 % from this introduction to the relevant body chapters.
 % ================================================================
 \phantomsection\label{def:modular-homotopy-theory-intro}%
-\phantomsection\label{eq:all-arity-master-eq-intro}%
+\phantomsection\label{eq:all-degree-master-eq-intro}%
 \phantomsection\label{eq:arnold-seed}%
 \phantomsection\label{eq:bar-graded-object-intro}%
 \phantomsection\label{eq:the-seed}%
diff --git a/standalone/N4_mc4_completion.tex b/standalone/N4_mc4_completion.tex
index 20ec3ce436edec8824a0a32db8ba502c7a819228..07f556005d81499f09a4862aadb38f14028fc487
--- a/standalone/N4_mc4_completion.tex
+++ b/standalone/N4_mc4_completion.tex
@@ -416,7 +416,7 @@
 \end{example}
 
 % ================================================================
-% 4. THE ARITY CUTOFF LEMMA
+% 4. THE DEGREE CUTOFF LEMMA
 % ================================================================
 
 \section{The degree cutoff lemma}

tokens used
142,499
