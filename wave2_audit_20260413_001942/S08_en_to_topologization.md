# S08_en_to_topologization (620s)

- [CRITICAL] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:5211) — PROBLEM: `prop:khan-zeng-topological` upgrades the chain-level chiral `\Ethree`-algebra `\CE^{\mathrm{ch}}_k(\fg)` itself to a topological `\Ethree` and even identifies `X\times\RR` with `\RR^3` at lines 5246-5249, but `thm:topologization` at 2967-2996 and `rem:topologization-chain-vs-cohomology` at 3159-3195 explicitly prove only a cohomological `\Ethree^{\mathrm{top}}` on `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)))`, with the chain-level lift left open. FIX: delete the proposition as a proved statement and replace it with a remark/conjecture saying: for affine KM at non-critical level, the Sugawara inner conformal vector yields `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)))` as an `\Ethree^{\mathrm{top}}`-algebra; no chain-level topological enhancement of `\CE^{\mathrm{ch}}_k(\fg)` is proved here; any such lift is `Conjecture~\ref{conj:topologization-general}`. If you keep a geometric identification, restrict it to the local flat case `X=\CC`, not arbitrary `X`.

- [CRITICAL] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3625) — PROBLEM: `thm:e3-identification` imports the inflated chain-level topologization in item `(iv)` and reuses it in the proof at 3734-3738, so a `\ClaimStatusProvedHere` theorem is leaning on a stronger statement than `thm:topologization` actually gives. FIX: rewrite item `(iv)` to: “After passing to BRST cohomology, the Sugawara inner conformal vector gives the cohomological `\Ethree^{\mathrm{top}}` of Theorem~\ref{thm:topologization}; no chain-level topological identification is claimed.” Then replace the proof sentence at 3734-3738 by the same cohomological qualifier.

- [HIGH] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3526) — PROBLEM: `thm:e3-cs(iv)` says the Sugawara element upgrades the holomorphic `\Etwo` to topological `\Etwo` and yields `\Ethree^{\mathrm{top}}` with no BRST/cohomology qualifier, contradicting 2967-2996 and 3159-3195. FIX: replace item `(iv)` with: “At non-critical level, the Sugawara inner conformal vector makes holomorphic translations `Q`-exact on BRST cohomology, so `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)))` carries `\Ethree^{\mathrm{top}}` by Theorem~\ref{thm:topologization}; a chain-level topological enhancement is not proved here.”

- [MEDIUM] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:23) — PROBLEM: the chapter roadmap widens `thm:topologization` to an unscoped chapter climax; the same scope loss recurs in the closing synthesis at 5445-5448. Both places omit that the theorem is affine-KM-only, non-critical, and cohomological. FIX: in both places, change the description to: “the cohomological topologization theorem for affine Kac--Moody at non-critical level, upgrading BRST cohomology of the derived center to `\Ethree^{\mathrm{top}}`; for general conformal-vector algebras the chain-level statement remains conjectural, see `Conjecture~\ref{conj:topologization-general}`.”

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2992) — PROBLEM: this remark identifies `\kappa(V_k(\fg))=\dim(\fg)(k+h^\vee)/(2h^\vee)` as “the Sugawara central charge,” but [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:5224) gives the actual Sugawara Virasoro central charge `c=k\dim(\fg)/(k+h^\vee)`, and 3116-3124 in the same file already decomposes `\kappa` as bare term plus Sugawara shift. The sentence also invokes Sugawara before imposing `k\neq-h^\vee`. FIX: replace lines 2992-2995 with: “At non-critical level the Sugawara element exists and has Virasoro central charge `c_{\mathrm{Sug}}=k\dim(\fg)/(k+h^\vee)`. The modular characteristic is instead `\kappa(V_k(\fg))=\dim(\fg)(k+h^\vee)/(2h^\vee)=\operatorname{av}(r(z))+\dim(\fg)/2`; it is this `\kappa`, not `c_{\mathrm{Sug}}`, that plays the holographic role here.”

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3016) — PROBLEM: the Virasoro remark states “The bulk theory is `3`d pure gravity” flatly, but [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3082) and 3145-3156 say the Virasoro topologization/BRST realization is still conjectural. FIX: change the first sentence to “The expected bulk theory is `3`d pure gravity,” and append: “The corresponding topologization statement is conjectural: one still needs the `3`d gravity BRST complex and the bulk identity `T=[Q,G]`; see `Conjecture~\ref{conj:topologization-general}`.”

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3041) — PROBLEM: the principal `\cW_N` remark likewise presents higher-spin gravity as settled with no status qualifier, but [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3095) and 3148-3156 explicitly leave the `\cW_N` topologization/BRST construction conjectural. FIX: change “The bulk theory is `\mathrm{SL}(N)` higher-spin gravity...” to “The expected bulk theory is `\mathrm{SL}(N)` higher-spin gravity...,” and add: “The corresponding topologization/BRST statement remains conjectural; see `Conjecture~\ref{conj:topologization-general}`.”

## Summary
Checked: 2 | Findings: 7 | Verdict: FAIL


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
session id: 019d83c7-8387-7281-a8a1-eddf02e834a3
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


MISSION: SEAM AUDIT between en_koszul_duality.tex and higher_genus_modular_koszul.tex.

E_n Koszul→Topologization. Check: (a) the topologization theorem scope is consistent between files, (b) chain-level vs cohomological status consistent, (c) Sugawara hypothesis present in all relevant statements

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers

thinking
**Considering the process**

I'm thinking about whether to mention the invariant lock. It seems like I should use the update_plan after checking the context, which I believe is important. So, probably yes to that! I guess the next step is to inspect the files to make sure everything is aligned and see if there are any adjustments needed based on what I find there. There’s definitely some method in this process to ensure clarity!
codex
Using `deep-beilinson-audit` for this seam audit. I’m pulling the live claim surface first: constitutional files, the two target chapters, and every `topologization`/`Sugawara`/`chain-level` occurrence that can affect the seam.
exec
/bin/zsh -lc "pwd && rg -n \"topologization|Sugawara|chain-level|cohomological|SC\\"'^'"\\{ch,top\\}|E_3-TOPOLOGICAL|E_3-chiral|derived center|conformal vector\" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md chapters -g 'en_koszul_duality.tex' -g 'higher_genus_modular_koszul.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
Total output lines: 382

/Users/raeez/chiral-bar-cobar
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
metadata/theorem_registry.md:230:| `thm:universal-sugawara-d1` | `theorem` | 6816 | Universal first mixed Sugawara differential |
metadata/theorem_registry.md:233:| `thm:sugawara-casimir-transgression` | `theorem` | 6918 | Sugawara Casimir transgression |
metadata/theorem_registry.md:336:| `prop:derived-center-explicit` | `proposition` | 1772 | Explicit derived center: Heisenberg, affine $\widehat{\mathfrak{sl}}_2$, Virasoro |
metadata/theorem_registry.md:791:| `prop:chain-level-curvature-operator` | `proposition` | 626 | Chain-level curvature operator |
metadata/theorem_registry.md:871:| `thm:pbw-universal-semisimple` | `theorem` | 1572 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
metadata/theorem_registry.md:1012:| `thm:shadow-cohft` | `theorem` | 20689 | Shadow cohomological field theory |
metadata/theorem_registry.md:1165:| `thm:ordered-HH-coHH-cohomology` | `theorem` | 2058 | Hochschild--coHochschild duality, cohomological version |
metadata/theorem_registry.md:1405:| `prop:betagamma-sugawara-class-c` | `proposition` | 2669 | Why $\beta\gamma$ is class~$\mathsf{C}$: Sugawara composite and stratum separation |
metadata/theorem_registry.md:2315:| `prop:chain-level-three-obstructions` | `proposition` | 1646 | Three chain-level obstructions |
CLAUDE.md:5:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
CLAUDE.md:7:**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
CLAUDE.md:13:**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:17:**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.
CLAUDE.md:154:Write this list before any paragraph mentioning "bar", "cobar", "Koszul dual", or "derived center":
CLAUDE.md:210:A (algebra) -- B(A) (bar coalgebra) -- A^i=H*(B(A)) (dual coalgebra) -- A^!=((A^i)^v) (dual algebra) -- Z^der_ch(A) (derived center = bulk). Omega(B(A))=A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.
 succeeded in 53ms:
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


thinking
**Clarifying audit scope**

I’m considering the audit and the idea of perhaps implementing a scope lock. It might be helpful to create a longer plan that outlines everything clearly. I should write a detailed commentary that specifies the exact scope and plan, and I think including the audit surface in that discussion would also be useful. That way, everything is organized, and I can keep track of what's necessary moving forward!
codex
Scope lock: `chapters/theory/en_koszul_duality.tex` `§sec:topologization` against the topologization seam in `chapters/theory/higher_genus_modular_koszul.tex`. I’m now reading the exact theorem/remark clusters and the concordance surface to see whether the status boundary widens, narrows, or silently shifts at the transition.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2938,3210p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4528,4588p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1660,1860p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba archive/raeeznotes/raeeznotes100/red_team_summary.md | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2938	$\FM_k(\bR^2)$ that are \emph{locally constant} (invariant
  2939	under continuous deformations). The holomorphic operations
  2940	from $\FM_k(\bC)$ are not locally constant: they depend on
  2941	the complex structure of the curve. To promote the
  2942	holomorphic $\Etwo$ to topological $\Etwo$, one must show
  2943	that the complex-structure dependence is homotopically
  2944	trivial.
  2945	
  2946	\begin{definition}[Inner conformal vector]
  2947	\label{def:inner-conformal-vector}
  2948	\index{conformal vector!inner}
  2949	Let $\cA$ be a chiral algebra and let $Q$ be a
  2950	BRST-type differential on the algebra of observables
  2951	of a holomorphic--topological theory~$T$ on
  2952	$\bC \times \bR$ whose boundary chiral algebra
  2953	is~$\cA$. An \emph{inner conformal vector} for
  2954	$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
  2955	central charge~$c$ that is $Q$-exact in the algebra
  2956	of bulk observables up to a $Q$-boundary: there exists
  2957	$G(z)$ such that $T(z) - [Q, G(z)]$ is $Q$-exact.
 succeeded in 52ms:
  4528	
  4529	\section{Bridges to Volume~II}
  4530	\label{sec:cross-volume-bridges}
  4531	\index{Volume II!bridges from Volume I}
  4532	
  4533	Volume~II develops the $A_\infty$-chiral Hochschild theory in
  4534	three space-time dimensions with the operad
  4535	$\mathrm{SC}^{\mathrm{ch,top}}$. Homotopy--Koszulity of
  4536	$\mathrm{SC}^{\mathrm{ch,top}}$ is proved in Volume~II
  4537	(via Kontsevich formality and transfer from the classical
  4538	Swiss--cheese operad), so the bar--cobar adjunction for
  4539	$\mathrm{SC}^{\mathrm{ch,top}}$-algebras is a Quillen
  4540	\emph{equivalence}. Volume~II has \emph{no remaining conjectural
  4541	algebraic inputs}; its only conditional inputs are the
  4542	standing analytic hypotheses (H1)--(H4).
  4543	Five bridges connect the two volumes:
  4544	
  4545	\begin{proposition}[Bar-cobar bridge; \ClaimStatusProvedElsewhere]
  4546	\label{prop:vol2-bar-cobar-bridge}%
  4547	The $\mathrm{SC}^{\mathrm{ch,top}}$ bar-cobar Quillen equivalence of
 succeeded in 52ms:
  1660	are unconditionally defined.
  1661	\end{enumerate}
  1662	This upgrades
  1663	Proposition~\textup{\ref{prop:conditional-modular-koszul}}
  1664	for the higher $\mathcal{W}_N$ family, and more generally for
  1665	principal finite-type $\mathcal{W}$-algebras,
  1666	from conditional to unconditional.
  1667	\end{corollary}
  1668	
  1669	\begin{proof}
  1670	MK1 (genus-$0$ Koszulity):
  1671	Theorems~\ref{thm:w-algebra-koszul-main}
  1672	and~\ref{thm:bar-cobar-spectral-sequence}.
  1673	MK2 (Verdier):
  1674	Theorem~\ref{thm:verdier-bar-cobar}.
  1675	MK3 (PBW concentration at all genera):
  1676	Theorem~\ref{thm:pbw-allgenera-principal-w}.
  1677	MK4 and MK5 follow from MK1--MK3 by
  1678	Theorems~\ref{thm:higher-genus-inversion}
  1679	and~\ref{thm:quantum-complementarity-main}.
 succeeded in 51ms:
     1	# Red-Team Summary of Vol1/Vol2 Claim Audit
     2	## Scope
     3	- Formal tagged claims catalogued: **4866**
     4	- Volume I formal claims: **2841**
     5	- Volume II formal claims: **2025**
     6	- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
     7	- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.
     8	
     9	## Status profile
    10	- ProvedHere: **3801**
    11	- Conjectured: **327**
    12	- Heuristic: **35**
    13	- ProvedElsewhere: **513**
    14	- Conditional: **116**
    15	- Open: **74**
    16	
    17	## Risk profile
    18	- medium: **1999**
    19	- low: **1913**
    20	- high: **807**
codex
The affine-only theorem surface in `en_koszul_duality.tex` is clear: proved for `V_k(\mathfrak g)` at non-critical level, cohomological only, chain-level open. I’m now sweeping `higher_genus_modular_koszul.tex` for every place that widens that statement, suppresses the Sugawara/non-critical hypothesis, or silently upgrades cohomology to cochains.
exec
/bin/zsh -lc "rg -n \"topologization|Sugawara|conformal vector|Ethree|E_3|E3|BRST cohomology|derived center|SC\\"'^'"\\{ch,top\\}|inner conformal vector|topological enhancement|holomorphic translations|Q-exact\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "topologization|Sugawara|Ethree|E_3|E3|conformal vector" chapters/connections/concordance.tex metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"topologization|Sugawara|conformal vector|Ethree|E_3|E3|BRST cohomology|derived center|SC\\"'^'"\\{ch,top\\}|inner conformal vector|topological enhancement|holomorphic translations|Q-exact\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
879:E_3^{*,h}(g)_{\mathrm{enr}} = 0
921:at~$E_3$ by the level-$k$ contraction\textup{)}.
1093:at~$E_3$.
1151: at $E_3$ by $d_2^{\mathrm{PBW}}$: the $(1)$-product
1236:\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
1547:$E_3$ page:
1549:E_3^{*,h}(g)_{\mathrm{enr}} = 0
1689: algebras with conformal vector; \ClaimStatusProvedHere]
1719:genus-enrichment is killed by the $E_3$ page. In particular, for
1722:after this $E_3$-page vanishing.
1764:on~$E_3$ or beyond).
1777:killing the entire genus-$g$ enrichment on the $E_3$ page.
1789:theorem proves only the common $E_3$-page vanishing mechanism.
1825:as proved above: the conformal vector is the unique weight-$2$
1829:$\fg$-invariant enrichment is killed at the $E_3$ page.
1836:at~$E_3$). No residual classes survive to later pages,
1838:is zero on the $E_3$ page. By bounded-below convergence
1994:killed on the $E_3$ page with no surviving kernel or
1999:After enrichment death, $E_3(g) = E_3(0)$ as bigraded
2992:Sugawara central charge of the boundary WZW model; it is also
 succeeded in 52ms:
23:$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
24:theorem (\S\ref{sec:topologization}), which upgrades the resulting
25:$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
26:conformal vector.
27:The topologization proof is made constructive by an explicit
29:$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
32:algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
1153:\begin{conjecture}[\texorpdfstring{$\mathsf{E}_3$}{E3} bar complex and Chern--Simons;
1248:$\mathsf{SC}^{\mathrm{ch,top}}$ emerges on the derived center]
1250:\index{Swiss-cheese operad!on derived center, NOT on bar}
1267:The derived center is the algebra of bulk observables of
1273:\item With an inner conformal vector at non-critical level,
1274:  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
1275:  topologization theorem
1276:  (Theorem~\textup{\ref{thm:topologization}}).
1277:\item Without a conformal vector,
1281:  strictly weaker than $\Ethree$.
1283:The passage from bar complex to derived center is
1286:computational engine; the derived center is the
1287:$\mathsf{SC}^{\mathrm{ch,top}}$ (or $\Ethree$) output.
 succeeded in 52ms:
metadata/theorem_registry.md:230:| `thm:universal-sugawara-d1` | `theorem` | 6816 | Universal first mixed Sugawara differential |
metadata/theorem_registry.md:233:| `thm:sugawara-casimir-transgression` | `theorem` | 6918 | Sugawara Casimir transgression |
metadata/theorem_registry.md:871:| `thm:pbw-universal-semisimple` | `theorem` | 1572 | Universal PBW enrichment-killing for chiral algebras with conformal vector |
metadata/theorem_registry.md:1405:| `prop:betagamma-sugawara-class-c` | `proposition` | 2669 | Why $\beta\gamma$ is class~$\mathsf{C}$: Sugawara composite and stratum separation |
chapters/connections/concordance.tex:7137: & Coderived $E_3$: $D^{\mathrm{co}}$-level $E_3$ on
chapters/connections/concordance.tex:7139: without conformal vector \textup{(}Conjecture\textup{)}
chapters/connections/concordance.tex:7147: & Sugawara antighost construction:
chapters/connections/concordance.tex:7148: conformal vector at non-critical level yields
chapters/connections/concordance.tex:7149: antighost field for topologization
chapters/connections/concordance.tex:7178: The topologization theorem
chapters/connections/concordance.tex:7179: (Theorem~\ref{thm:topologization}:
chapters/connections/concordance.tex:7180: $\SCchtop + \text{inner conformal vector} = E_3$)
chapters/connections/concordance.tex:7182: For general chiral algebras with conformal vector,
chapters/connections/concordance.tex:7183: topologization is conjectural
chapters/connections/concordance.tex:9533:SC self-duality retraction, topologization scoping, critical-level
chapters/connections/concordance.tex:9546:\item \textbf{FT-5} (topologization scope):
chapters/connections/concordance.tex:9548: ($\SCchtop + \text{conformal vector} = E_3$) is proved for
chapters/connections/concordance.tex:9747:& Coderived $E_3$ without conformal vector
codex
I’ve found the likely danger zone: `higher_genus_modular_koszul.tex` seems to carry both a general chain-level “chiral `E_3`” story and a later Sugawara “topological enhancement.” Those can coexist only if the file states very explicitly which `E_3` is algebraic/chiral and which is topological/cohomological. I’m reading those exact junctions now.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3488,3544p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3488	Every shadow invariant of the programme is a projection of
  3489	$\Theta_\cA$: the modular characteristic $\kappa$ at degree~$2$,
  3490	the cubic shadow $\mathfrak{C}$ at degree~$3$, the quartic
  3491	resonance $\mathfrak{Q}$ at degree~$4$, and all higher
  3492	obstructions in the Postnikov tower of
  3493	Definition~\ref{def:shadow-postnikov-tower}.
  3494	There is no separate construction for each invariant; there is
  3495	$\Theta_\cA$, and the invariants are what remain after
  3496	forgetting all but finitely many degrees.
  3497	
  3498	\begin{theorem}[Bar-intrinsic MC2; \ClaimStatusProvedHere]
  3499	\label{thm:mc2-bar-intrinsic}
  3500	\index{universal Maurer--Cartan class!bar-intrinsic construction}
  3501	\index{MC2!bar-intrinsic proof}
  3502	\index{MC2!full generality}
  3503	Let $\cA$ be a modular Koszul chiral algebra on a smooth
  3504	projective curve~$X$ with non-degenerate invariant form.
  3505	Write
  3506	$D_\cA = \sum_{g \geq 0} \hbar^g\, d_\cA^{(g)}$
  3507	for the genus-completed bar differential
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5438,5458p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '5198,5268p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4476,4568p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5198	Then:
  5199	\begin{enumerate}[label=\textup{(\alph*)}]
  5200	\item \emph{Genus filtration on $\Gmod$.}
  5201	 The modular graph coefficient algebra $\Gmod$
  5202	 \textup{(}Definition~\textup{\ref{def:modular-graph-algebra}}\textup{)}
  5203	 carries a complete descending genus filtration
  5204	 $G^m{\Gmod} := \prod_{g \geq m} {\Gmod}^{(g)}$
  5205	 with each genus-$g$ component ${\Gmod}^{(g)}$ finite-dimensional.
  5206	 The dg~Lie structure on $\Gmod$ respects the filtration:
  5207	 $[G^{m_1}, G^{m_2}] \subseteq G^{m_1+m_2}$ and
  5208	 $d(G^m) \subseteq G^m$.
  5209	
  5210	\item \emph{Convergent completed tensor product.}
  5211	 The pro-nilpotent completed tensor product
  5212	 \begin{equation}\label{eq:completed-tensor-gmod}
  5213	 \widehat{L}_{\Gmod}
  5214	 \;:=\;
  5215	 L \;\widehat{\otimes}\; \Gmod
  5216	 \;=\;
  5217	 \prod_{g \geq 0}\, L \otimes {\Gmod}^{(g)}
 succeeded in 50ms:
  4476	with obstruction classes
  4477	$o_{r+1}(\cA)$ at each level
  4478	(Appendix~\ref{app:nonlinear-modular-shadows});
  4479	the all-degree convergence of this tower is proved by the
  4480	bar-intrinsic construction
  4481	(Theorem~\ref{thm:mc2-bar-intrinsic};
  4482	Theorem~\ref{thm:recursive-existence}).
  4483	\end{remark}
  4484	
  4485	\begin{corollary}[Explicit modular package for all families;
  4486	\ClaimStatusProvedHere]\label{cor:explicit-theta-specializations}
  4487	\index{universal Maurer--Cartan class!specializations}
  4488	In the minimal model, the universal MC class for each family is
  4489	$\Theta^{\min}_{\cA} = \kappa(\cA) \cdot \eta \otimes \Lambda$
  4490	with $\Lambda = \sum_{g\geq 1}\lambda_g$, where:
  4491	\begin{center}
  4492	\begin{tabular}{llll}
  4493	\toprule
  4494	\emph{Chiral algebra} & $\mathfrak{g}$ &
  4495	$\kappa(\cA)$ & \emph{Genus-$1$ component} \\
 succeeded in 86ms:
  5438	statement: prove that the obstruction has the tautological boundary
  5439	profile and that the joint boundary/trace data separate the relevant
  5440	one-channel sector.
  5441	\end{proposition}
  5442	
  5443	\begin{proof}
  5444	Set
  5445	\[
  5446	\delta_g(\cA)
  5447	\;:=\;
  5448	o_g(\cA)-\kappa(\cA)\lambda_g \in U_g.
  5449	\]
  5450	Equation~\eqref{eq:taut-line-support-clutching} gives
  5451	\[
  5452	\mathrm{clut}_g\bigl(\delta_g(\cA)\bigr)
  5453	\;=\;
  5454	\mathrm{clut}_g\bigl(o_g(\cA)\bigr)
  5455	- \kappa(\cA)\,\mathrm{clut}_g(\lambda_g)
  5456	\;=\; 0,
  5457	\]



thinking
**Debugging line numbers**

I think there was a mix-up with the line numbers when I requested a range. It might be that the line numbers shifted, causing me to reference the wrong section. The content at line 5200, which is about topological enhancement via Sugawara, doesn't match the lines I got earlier. The outputs are different, likely due to how the command was applied. Maybe the line numbers are from a different section or file? I need to figure out the source of this mismatch.
thinking
**Investigating file discrepancies**

I'm wondering if the issue might be related to how `rg -n` counts bytes or if there are duplicate files involved. I should check the actual `rg` output by inspecting surrounding lines, but it still shows the same values. Maybe there's another file with the same name in Volume II that I didn't target? I think I should test the `rg` command again with context lines. It's possible hidden control characters could be causing issues, but the line numbers are the same. I'll keep investigating!
thinking
**Refining the command**

Okay, I've confirmed the path and line. Now, I'll use the exact command to search for specific phrases: "The chiral \\\\Ethree-algebra is holomorphic," "Topological enhancement via Sugawara," and "The topologization theorem" in the file `higher_genus_modular_koszul.tex`. I want to make sure to get context lines around the matches, so I’ll include `-C 2` to see what's happening on both sides. Let's see what I find!
codex
I hit a line-number discontinuity in `higher_genus_modular_koszul.tex`: `rg` and `nl` are not landing on the same content around the later `E_3`/Sugawara section. I’m resolving that before I record anything, because I don’t want a single false line reference in the audit.
exec
/bin/zsh -lc "rg -n -C 3 \"The chiral \\\\Ethree-algebra is holomorphic|Topological enhancement via Sugawara|The topologization theorem|Sugawara Virasoro element at non-critical level\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'wc -l chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "awk 'NR>=5196 && NR<=5268 {print NR \":\" "'$0}'"' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:The chiral \Ethree-algebra is holomorphic|Topological enhancement via Sugawara|The topologization theorem|Sugawara Virasoro element at non-critical level)
                  ^^
error: unrecognized escape sequence
 succeeded in 51ms:
   33865 chapters/theory/higher_genus_modular_koszul.tex
 succeeded in 51ms:
5196:cyclic $L_\infty$-algebra as in
5197:Proposition~\textup{\ref{prop:genus-completed-mc-framework}}.
5198:Then:
5199:\begin{enumerate}[label=\textup{(\alph*)}]
5200:\item \emph{Genus filtration on $\Gmod$.}
5201: The modular graph coefficient algebra $\Gmod$
5202: \textup{(}Definition~\textup{\ref{def:modular-graph-algebra}}\textup{)}
5203: carries a complete descending genus filtration
5204: $G^m{\Gmod} := \prod_{g \geq m} {\Gmod}^{(g)}$
5205: with each genus-$g$ component ${\Gmod}^{(g)}$ finite-dimensional.
5206: The dg~Lie structure on $\Gmod$ respects the filtration:
5207: $[G^{m_1}, G^{m_2}] \subseteq G^{m_1+m_2}$ and
5208: $d(G^m) \subseteq G^m$.
5209:
5210:\item \emph{Convergent completed tensor product.}
5211: The pro-nilpotent completed tensor product
5212: \begin{equation}\label{eq:completed-tensor-gmod}
5213: \widehat{L}_{\Gmod}
5214: \;:=\;
5215: L \;\widehat{\otimes}\; \Gmod

thinking
**Exploring content mismatch**

I’m noticing a weird mismatch with line numbers. I wonder if the file changed, and that’s why `rg` line numbers seem off. Checking around line 5200 with `awk`, I see other content that might not belong. It’s possible that `rg` output is from a different file revision. But I’m scratching my head about hidden null bytes possibly causing issues. I think I’ll try searching for a simpler string with `rg` to troubleshoot further and see what I can find.
exec
/bin/zsh -lc 'rg -n -F -C 3 "The topologization theorem" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F -C 3 "Topological enhancement via Sugawara" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F -C 3 "The chiral E3-algebra is holomorphic" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 exited 1 in 51ms:

 exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n -C 3 \"topological enhancement|Topological enhancement|chiral \\\\Ethree-algebra|Sugawara element is undefined|upgrades the BRST cohomology\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -C 3 \"topological enhancement|Topological enhancement|chiral \\\\Ethree-algebra|Sugawara element is undefined|upgrades the BRST cohomology\" chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:topological enhancement|Topological enhancement|chiral \Ethree-algebra|Sugawara element is undefined|upgrades the BRST cohomology)
                                                              ^^
error: unrecognized escape sequence
 exited 2 in 52ms:
rg: regex parse error:
    (?:topological enhancement|Topological enhancement|chiral \Ethree-algebra|Sugawara element is undefined|upgrades the BRST cohomology)
                                                              ^^
error: unrecognized escape sequence

thinking
**Exploring patterns in regex**

I'm thinking I might need to use the `-F` flag, and maybe I can separate multiple patterns. It could be simpler to use `rg -n -F "topological enhancement"` along with `rg -n -F "chiral \\Ethree-algebra"`. Let’s see how that turns out! I want to ensure the patterns work well together in my command. I’m curious if this approach will give me the results I’m looking for!
exec
/bin/zsh -lc 'rg -n -F -C 3 "topological enhancement" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F -C 3 \"chiral \\\\Ethree-algebra\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n -F -C 3 "upgrades the BRST cohomology" chapters/theory/higher_genus_modular_koszul.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
chapters/theory/en_koszul_duality.tex-5443-$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
chapters/theory/en_koszul_duality.tex-5444-(Remark~\ref{rem:sc-higher-genus}).
chapters/theory/en_koszul_duality.tex-5445-The topologization theorem
chapters/theory/en_koszul_duality.tex:5446:(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
chapters/theory/en_koszul_duality.tex-5447-the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
chapters/theory/en_koszul_duality.tex-5448-conformal vector,
chapters/theory/en_koszul_duality.tex-5449-with an explicit antighost contraction $G(z)$

thinking
**Considering search methods**

I'm thinking about why the previous output might've had line numbers from another file, perhaps due to hidden macros. It seems like using `grep -n` could be a better approach instead of `rg`. I should also search for the simple phrase "Topological enhancement via Sugawara" with `grep`, to see if I can get cleaner results. It’s like troubleshooting my methods to get more precise output!
exec
/bin/zsh -lc "grep -n \"The topologization theorem\\|upgrades the BRST cohomology\\|chain-level \\\\Ethree\\|cohomological \\\\Ethree\" chapters/theory/en_koszul_duality.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5445:The topologization theorem
5446:(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
exec
/bin/zsh -lc "grep -n \"Topological enhancement via Sugawara\\|topological enhancement\\|The topologization theorem\\|Sugawara element is undefined\\|chiral \\\\Ethree-algebra\" chapters/theory/higher_genus_modular_koszul.tex | head -n 40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


thinking
**Searching for topologization details**

I need to focus on the user’s mission regarding a seam audit between en_koszul and higher_genus. It seems like higher_genus might use the topologization theorem based on references from en_koszul. I’ll look for specific references by searching for terms like `thm:topologization`, `rem:topologization`, `conj:topologization-general`, or the phrase "topologization theorem" within higher_genus. Let's see what I can find regarding those labels!
codex
The apparent later `E_3`/Sugawara material was all inside `en_koszul_duality.tex`; that was my own cross-read, not a seam hit. I’m narrowing to the genuine seam now: places in `higher_genus_modular_koszul.tex` that either cite `thm:topologization`/its hypotheses or introduce conformal-vector language that could be mistaken for a topologization claim.
exec
/bin/zsh -lc "rg -n \"thm:topologization|conj:topologization-general|rem:topologization|topologization|E_3-topological|Ethree\\"'^'"\\{\\\\mathrm\\{top\\}\\}|BRST cohomology|Q-exact|inner conformal vector|Sugawara element\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"conformal vector|Sugawara|weight-2|stress tensor|inner Virasoro|critical level|non-critical level\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:topologization|conj:topologization-general|rem:topologization|topologization|E_3-topological|BRST cohomology|Q-exact|inner conformal vector|Sugawara element" metadata/theorem_registry.md chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:thm:topologization|conj:topologization-general|rem:topologization|topologization|E_3-topological|Ethree\^\{\mathrm\{top\}\}|BRST cohomology|Q-exact|inner conformal vector|Sugawara element)
                                                                                                                  ^^
error: unrecognized escape sequence
 succeeded in 52ms:
187:At critical level $k = -h^\vee$, the scalar curvature $\kappa$
827:spanned by the stress tensor~$T$; every other homogeneous state has
847: weight-$2$ states, hence only from the stress tensor~$T$;
1236:\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
1689: algebras with conformal vector; \ClaimStatusProvedHere]
1691:\index{PBW spectral sequence!unique-weight-2 criterion|textbf}
1693:\index{modular Koszul chiral algebra!unique-weight-2 criterion|textbf}
1705: weight~$2$, namely the stress tensor~$T$, with
1754:weight by $s - 2$. By hypothesis~(b), the stress tensor~$T$
1825:as proved above: the conformal vector is the unique weight-$2$
1866:half-integer weights $\geq 3/2$, and the stress tensor~$T$ at
1868:The stress tensor~$T$ is the unique generator at weight~$2$: the
1918:weight-$2$ stress tensor\textup{)}.
2022:weight-$2$ stress tensor~$T$ with $T_{(1)} = L_0$.
2716: In particular, $\kappa = 0$ if and only if $\cA$ is at critical level.
2992:Sugawara central charge of the boundary WZW model; it is also
2994:Chern--Simons theory, obtained by the Sugawara construction of
2995:the boundary stress tensor from the bulk gauge field. Two
2997:conflated (the Wave 10-7 semantic trap). At critical level
3005:central charge is not zero: the residual Sugawara shift of
 succeeded in 51ms:
chapters/connections/concordance.tex:2754:via BRST cohomology: the DS reduction does not preserve~$\rho$,
chapters/connections/concordance.tex:7149: antighost field for topologization
chapters/connections/concordance.tex:7178: The topologization theorem
chapters/connections/concordance.tex:7179: (Theorem~\ref{thm:topologization}:
chapters/connections/concordance.tex:7180: $\SCchtop + \text{inner conformal vector} = E_3$)
chapters/connections/concordance.tex:7183: topologization is conjectural
chapters/connections/concordance.tex:9533:SC self-duality retraction, topologization scoping, critical-level
chapters/connections/concordance.tex:9546:\item \textbf{FT-5} (topologization scope):

thinking
**Searching for solutions**

I need to improve the regex, possibly by applying fixed strings or patterns. There's also the idea of using a higher genus search for `thm:topologization`, but I’m not sure if that will lead to any results. Using grep with a specific label might help too. I’ll have to analyze the patterns I have and see if running multiple fixed patterns could give me better outcomes. So many possibilities!
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7168,7188p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '9538,9554p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n \"thm:topologization\\|conj:topologization-general\\|rem:topologization\\|topologization\" chapters/theory/higher_genus_modular_koszul.tex | head -n 120" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  7168	 \textbf{SC self-duality retracted.}
  7169	 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
  7170	 \text{shuffle-mixed})$: the closed dimensions are
  7171	 $(n{-}1)!$ vs~$1$, so $\SCchtop$ is \emph{not}
  7172	 Koszul self-dual. The duality \emph{functor} is an
  7173	 involution; the \emph{operad} is not self-dual.
  7174	 See AP166/B57.} \\
  7175	\hline
  7176	\multicolumn{3}{p{13cm}}{%
  7177	 \textbf{Topologization scoped.}
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
 succeeded in 51ms:
  9538	 $E_1$ coassociative coalgebra over $(\mathrm{ChirAss})^!$,
  9539	 not an $\SCchtop$-coalgebra (AP165).
  9540	\item \textbf{FT-4} (Theorem~H generic-level requirement):
  9541	 \emph{passed}. At critical level $k = -h^\vee$,
  9542	 $\ChirHoch^0(V_{-h^\vee}(\fg))$ is infinite-dimensional
  9543	 (Feigin--Frenkel center); Theorem~H does not apply.
  9544	 For $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is
  9545	 $4$-periodic and unbounded.
  9546	\item \textbf{FT-5} (topologization scope):
  9547	 \emph{passed}. Topologization
  9548	 ($\SCchtop + \text{conformal vector} = E_3$) is proved for
  9549	 affine KM at non-critical level; conjectural in general.
  9550	\item \textbf{FT-9} (SC duality):
  9551	 \emph{partial pass}. SC self-duality is retracted:
  9552	 $(\SCchtop)^! \cong (\mathrm{Lie},\, \mathrm{Ass},\,
  9553	 \text{shuffle-mixed}) \not\cong \SCchtop$.
  9554	 The duality functor is an involution (passed);
 succeeded in 51ms:


thinking
**Exploring mathematical claims**

I'm considering a direct inquiry about L and the conformal vector, which could link to E3 operations. I think I need to gather more information on this to understand its relevance better. Additionally, I'll search for `BRST` in higher genus, specifically around 8341 and 8658, but I'm not sure if that relates to the seam. I should also check for `derived center` to see if any E3 claims show up, using the search function.
codex
`higher_genus_modular_koszul.tex` does not explicitly cite `thm:topologization`; the seam is indirect. I’m checking every indirect proxy now: any use of “conformal vector,” “derived center,” or `E_3` in the higher-genus chapter that could be read as importing the topologization theorem without its affine/non-critical/cohomological limits.
exec
/bin/zsh -lc "rg -n \"derived center|center.*E_3|E_3.*center|conformal vector.*E_3|E_3.*conformal vector|BRST|Q-exact|topological E_3|topological enhancement|locally constant|Dunn|Swiss|SC\\"'^'"\\{ch,top\\}|Sugawara\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '280,340p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '28190,28310p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1236:\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
2992:Sugawara central charge of the boundary WZW model; it is also
2994:Chern--Simons theory, obtained by the Sugawara construction of
3005:central charge is not zero: the residual Sugawara shift of
3110:\begin{remark}[Sugawara shift as holographic anomaly]
3112:\index{Sugawara construction!holographic shift}%
3113:\index{holographic anomaly!Sugawara shift}%
3133:shift} from Sugawara normal-ordering: it is the bulk one-loop
8081:via BRST reduction\textup{)}. This rigidity means the
8151:As a cross-check: the BRST pullback target
8341:$\mathcal{W}$-algebra as a BRST cohomology of a free-field
8345:(the BRST complex has no additional moduli), so the infinitesimal
8652:The BRST complex realizing DS reduction is
8653:$C^{\mathrm{BRST}} = V_k(\mathfrak{g})
8656:with differential $d_{\mathrm{BRST}}$ depending on~$k$
8658:The zeroth BRST cohomology
8659:$\mathcal{W}^k(\mathfrak{g},f) = H^0(C^{\mathrm{BRST}},
8660:d_{\mathrm{BRST}})$
8667:pulls back along the BRST projection to a cyclic $2$-cocycle
8820: $\dim H^2_{\mathrm{cyc}} = 1$ by the BRST pullback
 succeeded in 52ms:
   280	The boundary stratification of
   281	$\overline{\mathcal{M}}_{g,n}$ is defined by the
   282	topological type of the stable curve (dual graph), which is
   283	$\mathrm{MCG}(\Sigma_g)$-equivariant: the strata are
   284	indexed by stable graphs, and $\mathrm{MCG}(\Sigma_g)$
   285	permutes points within each stratum without changing the
   286	graph type. Therefore $d_\cA^{(g)}$ is
   287	$\mathrm{MCG}(\Sigma_g)$-equivariant as an operator on
   288	$C_*(\overline{\mathcal{M}}_{g,n}) \otimes
   289	\operatorname{End}(\cA^{\otimes n})$.
   290	
   291	\emph{Step~2: MCG-equivariance of the MC element.}
   292	The universal MC element $\Theta_\cA := D_\cA - d_0$
   293	(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
   294	part of the bar differential. Since each genus-$g$ component
   295	$d_\cA^{(g)}$ is $\mathrm{MCG}(\Sigma_g)$-equivariant by
   296	Step~1, so is
   297	$\Theta_\cA^{(g)} = d_\cA^{(g)} \in
   298	C_*(\overline{\mathcal{M}}_{g,n}) \otimes
   299	\operatorname{End}(\cA^{\otimes n})$.
 succeeded in 52ms:
 28190	\begin{remark}[Symmetric orbifold kappa: four independent verifications;
 28191	 \ClaimStatusProvedHere]%
 28192	\label{rem:symmetric-orbifold-kappa}%
 28193	\index{symmetric orbifold!kappa verification}%
 28194	\index{kappa@$\kappa$!symmetric orbifold verification}%
 28195	The linearity $\kappa(\operatorname{Sym}^N(\cA)) = N\cdot\kappa(\cA)$
 28196	of Proposition~\ref{prop:symn-kappa-linearity} is verified by four
 28197	genuinely independent paths: (1)~twist-sector decomposition
 28198	(twisted sectors have $h_{\mathrm{twist}} > 0$, hence are
 28199	exponentially suppressed at genus~$1$ and do not contribute
 28200	to~$\mathrm{obs}_1$); (2)~the DMVV/Borcherds product
 28201	formula~\cite{DMVV97}, extracting the $N$-linear piece of
 28202	$\log Z$ at leading $q$-order; (3)~Hecke operators (the $N$-th
 28203	Hecke transform multiplies the vacuum-sector genus-$1$
 28204	obstruction by~$N$); (4)~direct bar-complex decomposition into
 28205	$N$~independent copies at genus~$1$ (cross-copy propagators
 28206	require twisted-sector insertions at genus~$\geq 2$; the bar
 28207	propagator $d\log E(z,w)$ is weight~$1$ by
 28208	Remark~\ref{rem:propagator-weight-universality}).
 28209	The convergence of four independent methods on a single formula

thinking
**Investigating mathematical terms**

I need to check around 16900 for W-algebra conformal vectors; it seems a bit off though. I should search for `E_3` in higher genus, as it might lead me to a spectral sequence E3 page which could be irrelevant. Searching for `\Ethree` doesn't seem to yield results—maybe I need to try grepping `\\Ethree` in higher_genus. I have to be cautious since the dataset is large. Let's see if any true algebraic E3 claims show up in higher_genus.
exec
/bin/zsh -lc "rg -n -F \"\\\\Ethree\" chapters/theory/higher_genus_modular_koszul.tex | head -n 80" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc 'rg -n -F "derived center" chapters/theory/higher_genus_modular_koszul.tex | head -n 120' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "E_3" chapters/theory/higher_genus_modular_koszul.tex | head -n 80' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
879:E_3^{*,h}(g)_{\mathrm{enr}} = 0
921:at~$E_3$ by the level-$k$ contraction\textup{)}.
1093:at~$E_3$.
1151: at $E_3$ by $d_2^{\mathrm{PBW}}$: the $(1)$-product
1547:$E_3$ page:
1549:E_3^{*,h}(g)_{\mathrm{enr}} = 0
1719:genus-enrichment is killed by the $E_3$ page. In particular, for
1722:after this $E_3$-page vanishing.
1764:on~$E_3$ or beyond).
1777:killing the entire genus-$g$ enrichment on the $E_3$ page.
1789:theorem proves only the common $E_3$-page vanishing mechanism.
1829:$\fg$-invariant enrichment is killed at the $E_3$ page.
1836:at~$E_3$). No residual classes survive to later pages,
1838:is zero on the $E_3$ page. By bounded-below convergence
1994:killed on the $E_3$ page with no surviving kernel or
1999:After enrichment death, $E_3(g) = E_3(0)$ as bigraded
 succeeded in 52ms:

codex
I’m reading the only higher-genus passages that touch the same physical mechanism as topologization: the Chern–Simons/Sugawara discussion and the generic “conformal vector” theorems. If there is seam drift, it will be there, not in the purely modular-combinatorial parts.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2978,3148p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '8434,8460p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16938,16996p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  8434	\item \emph{\textup{(}Cyclic one-dimensionality\textup{)}}
  8435	 $\dim H^2_{\mathrm{cyc}}(\cA, \cA) = 1$;
  8436	\item \emph{\textup{(}Degree-$2$ formality\textup{)}}
  8437	 the cyclic deformation complex $\Defcyc(\cA)$ is
  8438	 formal in degree~$2$, with cohomology generated by a
  8439	 single class $\eta \in H^2$;
  8440	\item \emph{\textup{(}Deformation rigidity\textup{)}}
  8441	 every continuous deformation of\/~$\cA$ preserving
  8442	 conformal vector and Koszul property is induced by
  8443	 rescaling the level.
  8444	\end{enumerate}
  8445	\item All four conditions hold for every
  8446	 Koszul chiral algebra with simple~$\mathfrak{g}$
  8447	 at non-admissible, non-critical level
  8448	 \textup{(}Theorem~\textup{\ref{thm:cyclic-rigidity-generic}}\textup{)},
  8449	 for every algebra on the standard Lie-theoretic landscape
  8450	 \textup{(}Corollary~\textup{\ref{cor:effective-quadruple}}\textup{)},
  8451	 and at all non-critical levels for algebraic families
  8452	 with rational OPE coefficients
  8453	 \textup{(}Theorem~\textup{\ref{thm:algebraic-family-rigidity}}\textup{)}.
 succeeded in 52ms:
  2978	obstruction tower is flat and Heisenberg is the atom of the
  2979	single-generator ladder.
  2980	\end{remark}
  2981	
  2982	\begin{remark}[Affine Kac--Moody: non-abelian Chern--Simons]
  2983	\label{rem:kappa-holo-km}
  2984	\index{affine Kac--Moody!Brown--Henneaux}%
  2985	\index{non-abelian Chern--Simons!holographic central charge}%
  2986	For the affine Kac--Moody vertex algebra
  2987	$V_k(\fg)$ at level~$k$,
  2988	\begin{equation*}
  2989	\kappa(V_k(\fg)) \;=\; \frac{\dim(\fg)\,(k + h^\vee)}{2\,h^\vee},
  2990	\end{equation*}
  2991	where $h^\vee$ is the dual Coxeter number. This is the
  2992	Sugawara central charge of the boundary WZW model; it is also
  2993	the Brown--Henneaux coefficient of the bulk $G_k$
  2994	Chern--Simons theory, obtained by the Sugawara construction of
  2995	the boundary stress tensor from the bulk gauge field. Two
  2996	degenerations deserve explicit mention, and they must not be
  2997	conflated (the Wave 10-7 semantic trap). At critical level
 succeeded in 50ms:
 16938	\begin{remark}[Evidence]
 16939	\label{rem:ds-monotonicity-evidence}
 16940	\index{shadow depth!monotonicity evidence}%
 16941	Three independent lines of evidence support
 16942	Conjecture~\textup{\ref{conj:ds-shadow-depth-monotonicity}}.
 16943	
 16944	\emph{(a)~Principal reductions.}
 16945	Proposition~\textup{\ref{prop:shadow-depth-escalator}} proves
 16946	the conjecture for the principal nilpotent $f_{\mathrm{prin}}$
 16947	in every simple~$\mathfrak{g}$: the Sugawara construction
 16948	escalates the OPE pole order from~$2$ \textup{(}affine\textup{)} to~$4$
 16949	\textup{(}Virasoro subalgebra\textup{)}, creating
 16950	$S_4 \neq 0$ and hence $\Delta \neq 0$.
 16951	
 16952	\emph{(b)~Non-principal reductions in type~$A$.}
 16953	Systematic computation
 16954	\textup{(}\texttt{compute/lib/ds\_nonprincipal\_shadows.py},
 16955	function~\texttt{orbit\_shadow\_hierarchy}\textup{)}
 16956	verifies the conjecture for all nilpotent orbits of
 16957	$\mathfrak{sl}_N$ ($N = 3, 4, 5$) at multiple levels:

thinking
**Searching for theorems**

I'm looking to find titles or proofs related to 19110 and maybe 22407, but I'm thinking that "seam" might not be relevant. I'll focus on searching for labels with terms like "conformal vector" or "stress tensor" in theorem statements that are close to high-risk theorem surfaces. There seems to be a link between these concepts, and I want to gather more information to clarify everything!
codex
I’m not finding explicit `thm:topologization` imports in the higher-genus chapter. That makes the seam risk subtler: not contradiction by citation, but silent hypothesis drift in nearby theorem statements. I’m checking theorem/corollary surfaces that talk about conformal vectors or non-critical affine/W-data and deciding whether they are genuinely about topologization or only about PBW/Koszul mechanics.
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{theorem\\}|\\\\begin\\{proposition\\}|\\\\begin\\{corollary\\}|\\\\begin\\{remark\\}\" chapters/theory/higher_genus_modular_koszul.tex | rg \"conformal vector|Sugawara|stress tensor|non-critical level|BRST|Chern--Simons|gravity|higher-spin|topological|holomorphic-topological\"" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Conjecture~\\\\textup\\{\\\\ref\\{conj:topologization-general\\}\\}|Theorem~\\\\textup\\{\\\\ref\\{thm:topologization\\}\\}|Theorem~\\\\ref\\{thm:topologization\\}|conformal vector|inner conformal vector|Sugawara\" chapters/theory/en_koszul_duality.tex | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"conformal vector|Sugawara|critical level|non-critical level|inner conformal vector|BRST cohomology\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '120,260p'" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 51ms:
25:$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
26:conformal vector.
1273:\item With an inner conformal vector at non-critical level,
1277:\item Without a conformal vector,
2920:\index{Sugawara construction!topologization}
2921:\index{E3 algebra@$\Ethree$-algebra!from Swiss-cheese + conformal vector}
2946:\begin{definition}[Inner conformal vector]
2948:\index{conformal vector!inner}
2953:is~$\cA$. An \emph{inner conformal vector} for
2954:$(\cA, Q)$ is a conformal vector $T(z) \in \cA$ of
2960:the Sugawara element
2963:provides the inner conformal vector. For the
2974:The Sugawara element
2976:provides an inner conformal vector
2990:Here the inner conformal vector makes holomorphic
3004:The inner conformal vector identifies
3024:At critical level $k = -h^\vee$, the Sugawara denominator
3025:$2(k + h^\vee)$ diverges: the Sugawara element is undefined,
3036:conformal vector hypothesis.
3051:\begin{remark}[The conformal vector is necessary, not
 succeeded in 52ms:




thinking
**Investigating theorem connections**

The first command didn’t work because I was searching for the theorem with the wrong pattern. I’m considering listing theorem surfaces with conformal vector using a specific command to find relevant details. There's a focus on lines in the en_koszul output since they might reveal conceptual connections. The user is interested in seams between two files, but if higher_genus lacks topologization references, it could indicate missing cross-references. I’ll need to inspect these gaps precisely.
thinking
**Examining conjecture seams**

I think the seam may be critical because higher_genus has a conjecture about coderived E3 related to class M, possibly using an inner conformal vector. There seems to be a connection between en_koszul's conjecture on topologization and higher_genus's coderived E3. I found that `conj:coderived-e3` is indeed in en_koszul, which might align with the mapping of topologization to the coderived E3 conjecture. The user’s audit focuses specifically on the seam between these two, so I need to dig deeper to find any gaps or subtle mismatches.
thinking
**Evaluating Sugawara Denominator**

I'm noticing that the explicit T formula at 16983-16985 has the issue of lacking the condition `k != -h^\vee` before mentioning the Sugawara denominator. It seems that since this formula is undefined at the critical level, it would be better to state "at non-critical level." This point might be relevant to the Sugawara hypothesis. I’m curious how this will affect the understanding of Sugawara's work overall!
codex
I’m checking the second-order failure mode now: duplicated topologization statements inside `en_koszul_duality.tex` itself. If a later restatement silently upgrades cohomology to cochains, that changes what the seam *demands* from the higher-genus file, even without an explicit citation there.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3494,3534p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5438,5456p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5198,5268p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  5438	$\Sigma_n$-coinvariants and uses the coshuffle coproduct
  5439	instead. At higher genus the fibrewise differential
  5440	$\dfib$ is curved with $\dfib^{\,2}=\kappa(\cA)\cdot\omega_g$
  5441	but is \emph{not} a coderivation; flatness and the coderivation
  5442	property are restored only by the period-corrected differential
  5443	$\Dg{g}$ of Theorem~\ref{thm:quantum-diff-squares-zero}
  5444	(Remark~\ref{rem:sc-higher-genus}).
  5445	The topologization theorem
  5446	(Theorem~\ref{thm:topologization}) upgrades the BRST cohomology of
  5447	the $\Etwo$ center of $V_k(\fg)$ to $\Ethree$ via the Sugawara
  5448	conformal vector,
  5449	with an explicit antighost contraction $G(z)$
  5450	(Construction~\ref{constr:sugawara-antighost}) that makes
  5451	the proof constructive. For class~M algebras, where the
  5452	chain-level $\Ethree$ encounters obstructions from
  5453	step~(iv) of Remark~\ref{rem:topologization-chain-vs-cohomology},
  5454	a coderived refinement (Conjecture~\ref{conj:coderived-e3})
  5455	provides the conjectural alternative.
  5456	
 succeeded in 52ms:
  3494	
  3495	
  3496	
  3497	% ================================================================
  3498	
  3499	\begin{theorem}[The $\Ethree$-algebra and Chern--Simons]
  3500	\label{thm:e3-cs}
  3501	\ClaimStatusProvedElsewhere
  3502	Let $\fg$ be a simple finite-dimensional Lie algebra and
  3503	$V_k(\fg)$ the affine Kac--Moody vertex algebra at level~$k$.
  3504	\begin{enumerate}[label=\textup{(\roman*)}]
  3505	\item \textup{(The $\Ethree$ structure.)}
  3506	  The curve geometry provides the $\Etwo$ structure on
  3507	  $\BarSig(V_k(\fg))$. By the Higher Deligne Conjecture
  3508	  \textup{(}Lurie~\cite{HA}, Francis~\cite{Francis2013}\textup{)},
  3509	  the derived chiral centre
  3510	  $Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))
  3511	  = \HH^*(\BarSig(V_k(\fg)), \BarSig(V_k(\fg)))$
  3512	  carries a natural $\Ethree$-algebra structure
  3513	  \textup{(}$\Etwo + 1 = \Ethree$\textup{)}.
 succeeded in 51ms:
  5198	
  5199	% ----------------------------------------------------------------
  5200	\subsection{The Khan--Zeng topological enhancement}
  5201	\label{subsec:khan-zeng-enhancement}
  5202	
  5203	The chiral $\Ethree$-algebra is holomorphic: it depends on the
  5204	complex structure of $X$ through the KZ connection. At
  5205	non-critical level $k \neq -h^\vee$, the Sugawara Virasoro
  5206	element provides a homotopy between the holomorphic and
  5207	topological directions, upgrading the $\Ethree$ structure
  5208	from holomorphic to topological. At the critical level,
  5209	the Sugawara element is undefined and the enhancement fails.
  5210	
  5211	\begin{proposition}[Topological enhancement via Sugawara]
  5212	\label{prop:khan-zeng-topological}
  5213	\ClaimStatusProvedHere
  5214	At generic non-critical level $k \neq -h^\vee$, the affine
  5215	Kac--Moody vertex algebra $V_k(\fg)$ possesses a Sugawara
  5216	Virasoro element
  5217	\begin{equation}\label{eq:sugawara-element}
codex
A serious second-order issue surfaced in `en_koszul_duality.tex`: a later proposition rewrites the affine result as if the full `E_3` object itself becomes chain-level topological, which contradicts the earlier “cohomological only” theorem and remarks. I’m now checking whether `higher_genus_modular_koszul.tex` absorbs that inflated version anywhere, or whether it stays closer to the narrow theorem.
exec
/bin/zsh -lc "rg -n \"ClaimStatusProvedHere|ClaimStatusProvedElsewhere|ClaimStatusConjectured\" chapters/theory/en_koszul_duality.tex | sed -n '140,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "locally constant|topological direction|holomorphic and topological|BRST cohomology|inner conformal vector|antighost|Dunn|Sugawara.*upgrade|upgrade.*topological" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '28860,28924p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
8341:$\mathcal{W}$-algebra as a BRST cohomology of a free-field
8658:The zeroth BRST cohomology
16703:In their framework, a theory with topological direction
28873:$\cA^{\mathrm{sh}}$ is locally constant
 succeeded in 51ms:

 succeeded in 51ms:
 28860	independent of the global geometry of~$X$.
 28861	\end{proof}
 28862	
 28863	\begin{theorem}[Open-stratum curve-independence at
 28864	 higher genus]
 28865	\label{thm:open-stratum-curve-independence}
 28866	\ClaimStatusProvedHere
 28867	\index{curve-independence!open stratum|textbf}
 28868	\index{modular Koszulness!curve-independence}
 28869	Let $\cA$ be a chiral algebra on a smooth curve~$X$
 28870	of genus~$g$. On the open stratum
 28871	$\mathcal{M}_g$ of smooth curves, modular Koszulness
 28872	is constant: the shadow algebra
 28873	$\cA^{\mathrm{sh}}$ is locally constant
 28874	on~$\mathcal{M}_g$.
 28875	\end{theorem}
 28876	
 28877	\begin{proof}
 28878	The shadow algebra
 28879	$\cA^{\mathrm{sh}} = H_\bullet(\operatorname{Def}^{\mathrm{mod}}_{\mathrm{cyc}}(\cA))$

thinking
**Inspecting topological direction**

I need to take a closer look around 16703, perhaps focusing on the topological direction. I wonder what specifics I should investigate in that area. It seems essential to gather as much detail as possible to get a clearer picture. I might need to consider what kind of information would be most relevant for understanding the topology there. Let's brainstorm and see where this leads me!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16688,16720p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '20,34p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '1266,1284p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 16688	$\mathbb{D}$ is the Verdier involution. Since $\mathbb{D}$
 16689	is an automorphism of~$\gAmod$ respecting the weight
 16690	filtration, it bijects the obstruction classes:
 16691	$o_r(\cA) = 0$ if and only if $o_r(\cA^!) = 0$.
 16692	Hence $r_{\max}(\cA) = r_{\max}(\cA^!)$.
 16693	\end{proof}
 16694	
 16695	\begin{remark}[Shadow depth refines GKW formality]
 16696	\label{rem:shadow-depth-gkw-refinement}
 16697	\index{GKW formality!shadow depth refinement}
 16698	\index{Gaiotto--Kulp--Wu|see{GKW formality}}
 16699	\index{shadow depth!GKW refinement}
 16700	The $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ classification
 16701	is a strict four-class refinement of the binary formal/non-formal
 16702	dichotomy of Gaiotto--Kulp--Wu~\cite{GKW2025}.
 16703	In their framework, a theory with topological direction
 16704	$d' \geq 2$ is formal (all higher operations vanish),
 16705	while $d' = 1$ theories are generically non-formal.
 16706	The shadow depth resolves the $d' = 1$ non-formal class
 16707	into three distinct strata:
 succeeded in 52ms:
  1266	computed \emph{using} the bar complex as a resolution.
  1267	The derived center is the algebra of bulk observables of
  1268	the 3d HT theory on $X \times \bR$:
  1269	\begin{itemize}
  1270	\item It carries $\Etwo$ structure from
  1271	  $\FM_k(\bC)$ (the operadic center theorem,
  1272	  Theorem~\textup{\ref{thm:operadic-center-hochschild}}).
  1273	\item With an inner conformal vector at non-critical level,
  1274	  this $\Etwo$ upgrades on BRST cohomology to $\Ethree$ via the
  1275	  topologization theorem
  1276	  (Theorem~\textup{\ref{thm:topologization}}).
  1277	\item Without a conformal vector,
  1278	  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$ carries
  1279	  $\mathsf{SC}^{\mathrm{ch,top}}$ structure
  1280	  (holomorphic $\Etwo$ coupled to topological $\Eone$),
  1281	  strictly weaker than $\Ethree$.
  1282	\end{itemize}
  1283	The passage from bar complex to derived center is
  1284	where the $\mathsf{SC}^{\mathrm{ch,top}}$ structure
 succeeded in 52ms:
    20	The chapter culminates in the chiral center theorem
    21	(\S\ref{sec:operadic-center-theorem}), which identifies the chiral
    22	Hochschild cochain complex as the operadic center of an
    23	$\mathsf{SC}^{\mathrm{ch,top}}$-algebra, and in the topologization
    24	theorem (\S\ref{sec:topologization}), which upgrades the resulting
    25	$\Etwo$ center on BRST cohomology to~$\Ethree$ via the Sugawara
    26	conformal vector.
    27	The topologization proof is made constructive by an explicit
    28	antighost contraction $G(z)$ representing
    29	$T_{\mathrm{Sug}} = [Q, G]$ in BRST cohomology
    30	in the $3$d holomorphic Chern--Simons BV complex
    31	(Construction~\ref{constr:sugawara-antighost}). For class~M
    32	algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
    33	encounters obstructions from the infinite shadow tower, a coderived
    34	refinement provides an alternative path
exec
/bin/zsh -lc 'rg -n "topologization|khan-zeng-topological|coderived-e3|e3-cs" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3398,3468p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3608,3642p'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
  3398	 Conjecture~\textup{\ref{conj:topologization-general}}.
  3399	\end{enumerate}
  3400	\end{remark}
  3401	
  3402	\begin{conjecture}[Coderived $\Ethree$ for class~M; \ClaimStatusConjectured]
  3403	\label{conj:coderived-e3}%
  3404	\index{coderived category!E3 structure@$\Ethree$ structure|textbf}%
  3405	\index{topologization theorem!coderived refinement}%
  3406	\index{E3 algebra@$\Ethree$ algebra!coderived}%
  3407	Let $\cA$ be a chirally Koszul algebra with inner conformal vector
  3408	at non-critical level.
  3409	\begin{enumerate}[label=\textup{(\roman*)}]
  3410	\item \textup{(Coderived local constancy.)}
  3411	  The chiral factorization algebra $\cF_\cA$ on a curve~$X$,
  3412	  viewed in the coderived category $D^{\mathrm{co}}(\cA)$,
  3413	  is locally constant. Precisely: the
  3414	  $m_0$-curvature obstruction to local constancy at
  3415	  step~\textup{(iv)} of
  3416	  Remark~\textup{\ref{rem:topologization-chain-vs-cohomology}}
  3417	  lies in $\operatorname{Im}(d)$ in $D^{\mathrm{co}}$, by the
 succeeded in 50ms:
  3608	  $\mathrm{Fun}(\mathrm{Op}_{\fg^\vee}(D))$
  3609	  \textup{(}opers on the formal disk\textup{)}, not
  3610	  directly to $C^*(\fg)$. The isomorphism is
  3611	  perturbative: it holds in the formal neighbourhood
  3612	  of critical level, order by order in
  3613	  $\lambda = k + h^\vee$.
  3614	\item \textup{(Order-by-order uniqueness.)}
  3615	  For simple $\fg$, $H^3(\fg) \cong \CC$ is
  3616	  one-dimensional, so the deformation base is
  3617	  one-dimensional at each order in $\lambda$. The
  3618	  isomorphism~\eqref{eq:e3-families} is forced by
  3619	  the matching of associated graded algebras
  3620	  \textup{(}both $C^*(\fg)$\textup{)},
  3621	  matching $\Pthree$ brackets on the formal disk
  3622	  \textup{(}Theorem~\textup{\ref{thm:chiral-e3-cfg}(ii)}%
  3623	  \textup{)}, and the one-dimensionality of the
  3624	  obstruction space at each order.
  3625	\item \textup{(Sugawara constraint.)}
  3626	  The topological enhancement
  3627	  \textup{(}Theorem~\ref{thm:e3-cs}(iv)\textup{)} holds






thinking
**Fixing technical details**

I need to replace `CE^{ch}_k(g)` with `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)))`, focusing on local constancy regarding BRST cohomology, rather than just a sheaf of locally constant chains. The user prefers fixes over edits, so I should propose exact wording. I should include relevant line ranges, like starting at 5211 or citing lines 5230-5248, while clarifying the format for file and line. It seems listing specific lines could be more effective in conveying the issue.
thinking
**Exploring topologization theorem**

I'm assessing a statement regarding the topologization theorem, specifically how it elevates the Etwo center on BRST cohomology to E3 through the Sugawara conformal vector. It's intriguing to consider how these mathematical concepts interact. The transition from one structure to another might reveal deeper connections in the context of cohomology. I'll need to dive deeper into these concepts to fully grasp their implications and ensure clarity.
thinking
**Clarifying theorem scope**

I’m noticing a possible gap with the "topologization theorem" mentioned in the chapter intro. It talks about it generically, but it doesn’t specify "affine Kac-Moody at non-critical level" until later, which could lead to misunderstandings. I think it would be helpful to append that specific scope to make it clearer. The user mentioned the need for consistency between files, especially since the introduction might broaden the scope before higher-genus gets into specifics. I also see a relevant point in the lines regarding E2 and E3 upgrades via the theorem.
thinking
**Examining potential inconsistencies**

I’m flagging some remarks from higher_genus regarding the Vir/W bulk theories not having conjectural status. It seems these might need to be in separate mediums for clarity. There's also a potential inconsistency between higher_genus and en_koszul because it treats the critical level as bulk Chern-Simons coupling becoming pure gauge. The user wants me to ground claims based on the content read, and this suggests some tension in the physical description. I could clarify the scope fix and mention Sugawara's undefined status.
thinking
**Clarifying charges and formulas**

I find the claim about Sugawara's central charge to be potentially misleading. If I look closely, it seems like they're saying kappa equals the Sugawara central charge, but that's usually not true unless k is special. In higher_genus, they mention a formula that might confirm this, but I need to check if this conflates terms. It's also possible that "Brown-Henneaux coefficient" could relate somehow, but I need to make sure about their usage of 'central charge' for kappa.
thinking
**Evaluating topological consistency**

It looks like `kappa` in KM indeed includes the Sugawara shift, so it seems like the claim in line 2992 is not accurate. However, the user's focus is on seam auditing for topologization, not just formula audits. The Sugawara hypothesis and Brown-Henneaux interpretation are intertwined here, and I could see this as a potential issue. I've looked at CLAUDE's canonical formulas, and it seems that line 2992 is inconsistent. I can propose a correction to clarify the context better.
codex
I’m sweeping the remaining `Sugawara` mentions in the higher-genus file to see which ones actually touch the seam and which are just internal structural remarks. I’m only going to keep findings that materially change the topologization/conformal-vector boundary.
exec
/bin/zsh -lc "rg -n \"Sugawara\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12556,12572p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1228,1242p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1236:\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
2992:Sugawara central charge of the boundary WZW model; it is also
2994:Chern--Simons theory, obtained by the Sugawara construction of
3005:central charge is not zero: the residual Sugawara shift of
3110:\begin{remark}[Sugawara shift as holographic anomaly]
3112:\index{Sugawara construction!holographic shift}%
3113:\index{holographic anomaly!Sugawara shift}%
3133:shift} from Sugawara normal-ordering: it is the bulk one-loop
12564:$\operatorname{Sh}_3\big|_T = 2$ (the Sugawara normal-ordering
16947:in every simple~$\mathfrak{g}$: the Sugawara construction
16983:For the principal nilpotent, this is the Sugawara stress
 succeeded in 51ms:
  1228	\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
  1229	\label{thm:pbw-allgenera-km}
  1230	\index{PBW spectral sequence!all-genera degeneration|textbf}
  1231	\index{modular Koszul chiral algebra!unconditional all genera}
  1232	\textup{[Regime: curved-central
  1233	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1234	
  1235	This theorem does not use Theorem~\ref{thm:pbw-universal-semisimple}
  1236	\textup{(}the Sugawara stress tensor is a composite, not a generator\textup{)}.
  1237	Instead, the genus-enrichment block is eliminated by the Whitehead--Casimir--Killing
  1238	mechanism, and the absence of later differentials/extensions is supplied by the
  1239	family-specific argument below.
  1240	
  1241	For any simple Lie algebra~$\fg$, any genus~$g \geq 1$, and
  1242	generic level $k \notin \Sigma(\fg)$, the PBW spectral sequence
 succeeded in 51ms:
 12556	\end{remark}
 12557	
 12558	\begin{remark}[Universality of $\Delta^{(3,0)}\big|_T$ and the soft cubic]
 12559	\label{rem:delta3-universality}
 12560	\index{sigma-invariant shadow ring@$\sigma$-invariant shadow ring!cubic universality}
 12561	\index{soft graviton!cubic shadow}
 12562	\index{Lie bracket!determines cubic shadow}
 12563	On the Virasoro $T$-line, the cubic shadow coefficient is
 12564	$\operatorname{Sh}_3\big|_T = 2$ (the Sugawara normal-ordering
 12565	constant, independent of~$c$).
 12566	Therefore $\Delta^{(3,0)}\big|_T = 2 + 2 = 4$ for every
 12567	chirally Koszul algebra with a Virasoro subalgebra, including
 12568	all principal $\mathcal{W}_N$ ($N = 2, \ldots, 6$ verified) and the
 12569	non-principal Bershadsky--Polyakov algebra
 12570	(Computation~\ref{comp:bp-shadow-tower}).
 12571	This value $4$ is the second universal invariant of the
 12572	$\sigma$-invariant shadow ring, after


thinking
**Evaluating relevance in formulas**

I'm considering whether to include the explicit formula at 16984 since the concluding conjecture statement indicates a non-critical level. It might be categorized as LOW. We could decide to include it for exhaustiveness, but it doesn't align perfectly with the seam. Including the "Sugawara hypothesis" in relevant statements could work, but not every occurrence is necessary. I'll need to judge the relevance based on its support for the DS shadow-depth monotonicity evidence.
thinking
**Searching topological enhancement**

I want to explore mentions of "topological enhancement" in en_koszul. I'll search for "topological enhancement" and "topologization theorem" to inspect relevant findings. There are quite a few sections to look through, like 5200 subsection, 5211 prop, 5445 summary, and 3626 theorem proof. I might even check around 3734 for anything useful. It feels like there's a lot to dig into!
codex
The chain/cohomology drift is recurring, not isolated. I’m doing one last pass over every `topological enhancement` / `topologization theorem` summary line in `en_koszul_duality.tex` so I can separate the primary false theorem surface from the trailing summary sentences that also need tightening.
exec
/bin/zsh -lc "rg -n \"topological enhancement|topologization theorem|cohomological topologization|upgrades .* to .*Ethree|Ethree\\"'^'"\\{\\\\mathrm\\{top\\}\\}|inner conformal vector|chain-level .*Ethree|cohomological .*Ethree\" chapters/theory/en_koszul_duality.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3618,3634p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:topological enhancement|topologization theorem|cohomological topologization|upgrades .* to .*Ethree|Ethree\^\{\mathrm\{top\}\}|inner conformal vector|chain-level .*Ethree|cohomological .*Ethree)
                                                                                                                     ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3728,3740p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3618	  isomorphism~\eqref{eq:e3-families} is forced by
  3619	  the matching of associated graded algebras
  3620	  \textup{(}both $C^*(\fg)$\textup{)},
  3621	  matching $\Pthree$ brackets on the formal disk
  3622	  \textup{(}Theorem~\textup{\ref{thm:chiral-e3-cfg}(ii)}%
  3623	  \textup{)}, and the one-dimensionality of the
  3624	  obstruction space at each order.
  3625	\item \textup{(Sugawara constraint.)}
  3626	  The topological enhancement
  3627	  \textup{(}Theorem~\ref{thm:e3-cs}(iv)\textup{)} holds
  3628	  at generic $k$ but fails at $k = -h^\vee$, where
  3629	  the Sugawara element is undefined. The perturbative
  3630	  identification holds
  3631	  order by order in $(k + h^\vee)$, since the Sugawara
  3632	  element exists at any nonzero departure from critical
  3633	  level.
  3634	\end{enumerate}
 succeeded in 52ms:
  3728	The compatible family $\{\varphi_p\}_{p \geq 0}$
  3729	determines an isomorphism
  3730	$\varphi = \varprojlim_p\,\varphi_p$
  3731	of filtered $\Ethree$-algebras over
  3732	$\lambda\,H^3(\fg)[[\lambda]]$, completing the proof
  3733	of~\eqref{eq:e3-families}.
  3734	Part~(iv) is immediate: the topological enhancement
  3735	(Theorem~\ref{thm:e3-cs}(iv)) requires the Sugawara
  3736	element, which exists for $\lambda \neq 0$ and is
  3737	compatible with~$\varphi$ order by order
  3738	(the Sugawara element at order~$p$ depends only on the
  3739	data modulo~$\lambda^{p+1}$, where the two families
  3740	already agree).
exec
/bin/zsh -lc "grep -n \"topological enhancement\\|topologization theorem\\|cohomological topologization\\|inner conformal vector\\|chain-level\" chapters/theory/en_koszul_duality.tex | head -n 160" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n \"topological enhancement\\|topologization theorem\\|cohomological topologization\\|inner conformal vector\\|chain-level .*Ethree\\|cohomological .*Ethree\" chapters/theory/en_koszul_duality.tex | head -n 120" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
32:algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
645:\label{rem:chain-level-en}
647:Main Theorems~A, B, C are the chain-level refinement at $n = 2$:
689:\index{Ayala--Francis!chain-level refinement}
690:\index{Poincar\'e--Koszul duality!chain-level}
715:At $n = 2$, the chain-level bar complex
1179:What is conjectured is the full chain-level identification~(iii):
1273:\item With an inner conformal vector at non-critical level,
1275:  topologization theorem
1559:(Step~1), its chain-level computation (Step~2), the geometric
1788:\label{subsec:center-chain-level}
1789:\index{operadic center!chain-level realization}
1890:chain-level model for~$\FM_k(\bC)$, the $k$ copies of~$\cA$
1899:\S\ref{subsec:center-chain-level}).
2450:formula~\eqref{eq:center-equalizer}; the cochain-level model
2622:\item \emph{Steps 1--2} (algebraic/chain-level) are parallel to the
2919:\index{topologization theorem|textbf}
2953:is~$\cA$. An \emph{inner conformal vector} for
2963:provides the inner conformal vector. For the
2970:\index{topologization theorem!statement}
 succeeded in 51ms:
32:algebras (Virasoro, $\cW_N$), where the chain-level $\Ethree$
1273:\item With an inner conformal vector at non-critical level,
1275:  topologization theorem
2919:\index{topologization theorem|textbf}
2953:is~$\cA$. An \emph{inner conformal vector} for
2963:provides the inner conformal vector. For the
2970:\index{topologization theorem!statement}
2976:provides an inner conformal vector
2990:Here the inner conformal vector makes holomorphic
3004:The inner conformal vector identifies
3034:\index{topologization theorem!external inputs}
3072:\index{topologization theorem!scope}
3076:an explicit inner conformal vector and the $3$d
3079:cohomological $\Ethree$-algebra on BRST cohomology.
3110:\index{topologization theorem!general conjecture}
3114:a chain-level $\Ethree$-topological structure lifting the
3115:cohomological topologization of~\eqref{eq:topologization}.
3122:inner conformal vector in BRST cohomology, and (ii)~the
3130:cohomological $\Ethree$-structure.
3137:obstruct the cochain-level $\Ethree$ structure. The

thinking
**Examining theorem details**

I'm thinking that maybe the theorem on perturbative identification of E3-deformations relies on chain-level E3 structures, particularly with part (iv) as an additional condition. If part (iv) shifts to a cohomological perspective, I might need to adjust the theorem's proofs in lines 3626-3633 and 3734-3738 since they currently approach topological enhancement as chain-level order-by-order. This could be a substantial issue, so I really need to examine the theorem statement around line 3577 to clarify its focus on chain-level E3-deformations.
codex
I’m checking whether the later proof that cites the “topological enhancement” actually depends on the inflated chain-level version. If it does, that’s not just a wording problem; it contaminates a later theorem proof.
exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3718,3744p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3568,3640p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '5258,5270p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3568	perturbative Chern--Simons quantisation
  3569	(Theorem~\ref{thm:cfg}). Both are parametrised by
  3570	$(k+h^\vee)\,H^3(\fg)[[k+h^\vee]]$.
  3571	For simple~$\fg$, $\dim H^3(\fg) = 1$, so the
  3572	deformation base is one-dimensional at each order:
  3573	the two families must coincide.
  3574	
  3575	\begin{theorem}[Identification of $\Ethree$-deformation families]
  3576	\label{thm:e3-identification}
  3577	\ClaimStatusProvedHere
  3578	Let $\fg$ be a simple finite-dimensional Lie algebra and
  3579	$V_k(\fg)$ the affine Kac--Moody vertex algebra at
  3580	level~$k$.
  3581	Writing $\lambda = k + h^\vee$ for the departure from
  3582	critical level, the derived chiral centre
  3583	$Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg))$ of
  3584	Proposition~\textup{\ref{prop:e3-structure}} and the
  3585	CFG $\Ethree$-algebra $\cA^\lambda$ of
  3586	Theorem~\textup{\ref{thm:cfg}} are isomorphic as formal
  3587	deformation families of $\Ethree$-algebras:
 succeeded in 52ms:
  3718	the full $\Ethree$ deformation class
  3719	(biderivation property,
  3720	Lemma~\ref{lem:bv-p3-commutativity}, Step~2), and
  3721	the space of $\fg$-equivariant corrections at each order
  3722	is one-dimensional (spanned by the Killing-form pairing
  3723	$(a,b) \mapsto k\,(a,b)$), the two constructions agree
  3724	at order~$p+1$.
  3725	
  3726	\smallskip
  3727	\noindent\textit{Step 3: passage to the limit.}
  3728	The compatible family $\{\varphi_p\}_{p \geq 0}$
  3729	determines an isomorphism
  3730	$\varphi = \varprojlim_p\,\varphi_p$
  3731	of filtered $\Ethree$-algebras over
  3732	$\lambda\,H^3(\fg)[[\lambda]]$, completing the proof
  3733	of~\eqref{eq:e3-families}.
  3734	Part~(iv) is immediate: the topological enhancement
  3735	(Theorem~\ref{thm:e3-cs}(iv)) requires the Sugawara
  3736	element, which exists for $\lambda \neq 0$ and is
  3737	compatible with~$\varphi$ order by order
 succeeded in 51ms:
  5258	  (Warning~\ref{warn:e1-vs-e2-source}), but $\cA$
  5259	  itself retains essential dependence on the complex
  5260	  structure of~$X$.
  5261	  Without the Sugawara element, there is no homotopy
  5262	  between the holomorphic and topological directions,
  5263	  so the full structure is not topological $\Ethree$.
  5264	  Perturbatively, in the formal neighbourhood of critical level,
  5265	  the topological enhancement holds order-by-order in
  5266	  $(k + h^\vee)$ \textup{(}since $T_{\mathrm{Sug}}$ exists at
  5267	  any nonzero departure from critical level\textup{)}.
  5268	\end{enumerate}
  5269	\end{proposition}
  5270	




thinking
**Evaluating theorem claims**

I'm contemplating the e3-identification theorem, particularly the role of topological enhancement in its proof. If it's only cohomological, then maybe the theorem overclaims the canonicity of chain-level isomorphism. I'm considering whether the theorem's statement about E3-algebras requires rephrasing, especially concerning part (iv), which seems extra and just mentions the Sugawara constraint. If that enhancement doesn't significantly impact the isomorphism claims, then perhaps I should consider weakening or removing part (iv) for clarity.
thinking
**Analyzing theorem inconsistencies**

I'm examining proposition 5211, and it seems to be a false theorem that e3-identification reuses. It could be considered [HIGH] or [CRITICAL]. I’m not sure if we need to treat theorem e3-cs and e3-identification separately, but it looks like e3-identification relies on part (iv). My findings suggest that the topological enhancement in e3-identification remains a critical issue. I think we should amend or separate part (iv) for clarity, especially since it doesn't mention topological enhancement until that item.
thinking
**Evaluating mathematical findings**

I'm considering the potential finding regarding the en_koszul property. It seems that the statement "RR^3 \cong X \times RR (identifying X \cong C \cong R^2)" might actually be false for general X, which is intriguing! The exact fix may involve specifying a local statement, possibly on a disk or when X is exactly C. It feels good to think through these mathematical nuances and clarify them accurately.
thinking
**Clarifying DS reduction**

I'm wondering if this is really about seam surfaces. It feels more related to DS reduction and the Virasoro subalgebra, rather than topologization. Hmm, since an exhaustive seam surface might not be necessary here, maybe I can omit that to stay focused on the mission. Similarly, it seems like 1236/12564 doesn't relate to the concept of seam either. Let's keep that in mind as I move forward with this.
codex
- [CRITICAL] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:5211) — PROBLEM: `prop:khan-zeng-topological` upgrades the chain-level chiral `\Ethree`-algebra `\CE^{\mathrm{ch}}_k(\fg)` itself to a topological `\Ethree` and even identifies `X\times\RR` with `\RR^3` at lines 5246-5249, but `thm:topologization` at 2967-2996 and `rem:topologization-chain-vs-cohomology` at 3159-3195 explicitly prove only a cohomological `\Ethree^{\mathrm{top}}` on `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)))`, with the chain-level lift left open. FIX: delete the proposition as a proved statement and replace it with a remark/conjecture saying: for affine KM at non-critical level, the Sugawara inner conformal vector yields `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)))` as an `\Ethree^{\mathrm{top}}`-algebra; no chain-level topological enhancement of `\CE^{\mathrm{ch}}_k(\fg)` is proved here; any such lift is `Conjecture~\ref{conj:topologization-general}`. If you keep a geometric identification, restrict it to the local flat case `X=\CC`, not arbitrary `X`.

- [CRITICAL] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3625) — PROBLEM: `thm:e3-identification` imports the inflated chain-level topologization in item `(iv)` and reuses it in the proof at 3734-3738, so a `\ClaimStatusProvedHere` theorem is leaning on a stronger statement than `thm:topologization` actually gives. FIX: rewrite item `(iv)` to: “After passing to BRST cohomology, the Sugawara inner conformal vector gives the cohomological `\Ethree^{\mathrm{top}}` of Theorem~\ref{thm:topologization}; no chain-level topological identification is claimed.” Then replace the proof sentence at 3734-3738 by the same cohomological qualifier.

- [HIGH] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3526) — PROBLEM: `thm:e3-cs(iv)` says the Sugawara element upgrades the holomorphic `\Etwo` to topological `\Etwo` and yields `\Ethree^{\mathrm{top}}` with no BRST/cohomology qualifier, contradicting 2967-2996 and 3159-3195. FIX: replace item `(iv)` with: “At non-critical level, the Sugawara inner conformal vector makes holomorphic translations `Q`-exact on BRST cohomology, so `H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\fg)))` carries `\Ethree^{\mathrm{top}}` by Theorem~\ref{thm:topologization}; a chain-level topological enhancement is not proved here.”

- [MEDIUM] [chapters/theory/en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:23) — PROBLEM: the chapter roadmap widens `thm:topologization` to an unscoped chapter climax; the same scope loss recurs in the closing synthesis at 5445-5448. Both places omit that the theorem is affine-KM-only, non-critical, and cohomological. FIX: in both places, change the description to: “the cohomological topologization theorem for affine Kac--Moody at non-critical level, upgrading BRST cohomology of the derived center to `\Ethree^{\mathrm{top}}`; for general conformal-vector algebras the chain-level statement remains conjectural, see `Conjecture~\ref{conj:topologization-general}`.”

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:2992) — PROBLEM: this remark identifies `\kappa(V_k(\fg))=\dim(\fg)(k+h^\vee)/(2h^\vee)` as “the Sugawara central charge,” but [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:5224) gives the actual Sugawara Virasoro central charge `c=k\dim(\fg)/(k+h^\vee)`, and 3116-3124 in the same file already decomposes `\kappa` as bare term plus Sugawara shift. The sentence also invokes Sugawara before imposing `k\neq-h^\vee`. FIX: replace lines 2992-2995 with: “At non-critical level the Sugawara element exists and has Virasoro central charge `c_{\mathrm{Sug}}=k\dim(\fg)/(k+h^\vee)`. The modular characteristic is instead `\kappa(V_k(\fg))=\dim(\fg)(k+h^\vee)/(2h^\vee)=\operatorname{av}(r(z))+\dim(\fg)/2`; it is this `\kappa`, not `c_{\mathrm{Sug}}`, that plays the holographic role here.”

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3016) — PROBLEM: the Virasoro remark states “The bulk theory is `3`d pure gravity” flatly, but [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3082) and 3145-3156 say the Virasoro topologization/BRST realization is still conjectural. FIX: change the first sentence to “The expected bulk theory is `3`d pure gravity,” and append: “The corresponding topologization statement is conjectural: one still needs the `3`d gravity BRST complex and the bulk identity `T=[Q,G]`; see `Conjecture~\ref{conj:topologization-general}`.”

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3041) — PROBLEM: the principal `\cW_N` remark likewise presents higher-spin gravity as settled with no status qualifier, but [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:3095) and 3148-3156 explicitly leave the `\cW_N` topologization/BRST construction conjectural. FIX: change “The bulk theory is `\mathrm{SL}(N)` higher-spin gravity...” to “The expected bulk theory is `\mathrm{SL}(N)` higher-spin gravity...,” and add: “The corresponding topologization/BRST statement remains conjectural; see `Conjecture~\ref{conj:topologization-general}`.”

## Summary
Checked: 2 | Findings: 7 | Verdict: FAIL
tokens used
113,094
