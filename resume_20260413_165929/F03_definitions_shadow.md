# F03_definitions_shadow (765s)

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12193):12193, 12221, 13019, 14751, 31091 — PROBLEM: the shadow tower is not given a stable carrier. Definitions at 12193 and 12221 place the filtration and extension tower in `\mathfrak{g}^{\mathrm{amb}}_\cA` before that algebra is even defined at 31091, while 12169 says the filtration is on the modular convolution algebra, 13019 switches to `\gAmod`, and 14751 says the tower lives in `\mathfrak{g}^{\mathrm{mod}}_\cA`. This is a formal-definition failure, not a cosmetic one: the tower has no fixed home. FIX: rewrite 12176-12230 and 13014-13026 so the filtration, extension tower, and shadow obstruction tower all live in `\gAmod`; keep 31091 as a later graph-sum presentation only, and add one explicit comparison proposition after 31091 identifying the ambient presentation with `\gAmod`.

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14795):14795, 30888, 31873, 31949, 3778 — PROBLEM: `\Theta_\cA` is overloaded beyond repair. It denotes an arbitrary MC element at 14795, the bar-intrinsic positive-genus correction at 3778, the graph-sum object at 30888, and then a full genus expansion with nonzero `\Theta^{(0)}` at 31873/31949. Those are not the same object. FIX: reserve `\Theta_\cA` exclusively for the bar-intrinsic positive-genus correction of Theorem 3770; rename the generic MC variable in 14795 to `\alpha`, rename the genus-0 tree datum in 31873-31964 to `\tau_\cA`, and rename the graph-sum symbol in 30888-30916 to `\mathcal H_\cA^{\mathrm{mod}}` until a theorem identifies `\mathcal H_\cA^{\mathrm{mod}}=\Theta_\cA`.

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16594):16594, 16612, 16861, 134, 146 — PROBLEM: the G/L/C/M classification contradicts itself inside the same file. The opening at 134-146 says no other depths occur; 16594-16609 then says G/L/C/M are only a coarse classification and every finite depth occurs; 16612-16615 adds a fifth class `\mathbf W`; 16861-16863 goes back to “exactly one of G/L/C/M.” That destroys the theorem surface. FIX: delete 16594-16615 from this chapter and replace them with a single sentence after 16593: `The classes \mathbf G,\mathbf L,\mathbf C,\mathbf M are exhaustive and mutually exclusive on the proved surface of this monograph.` If higher-depth arithmetic refinements are wanted, move them to a separate conjectural remark in the arithmetic/frontier material with new notation that does not alter G/L/C/M.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:39):39, 41, 236, 255, 14795, 3770 — PROBLEM: the MC equation and the universal class are invoked before they are formally introduced in this file, and the first displayed formula is imprecise: `d_0 \Theta_\cA + \tfrac12[\Theta_\cA,\Theta_\cA]=0` omits the commutator interpretation later used at 3611-3613 and 4017-4028. FIX: insert a definition/notation block immediately after line 36:
  `\Theta_\cA:=D_\cA-\dzero`, `d_{\mathrm{Lie}}:=[\dzero,-]`, and `d_{\mathrm{Lie}}(\Theta_\cA)+\tfrac12[\Theta_\cA,\Theta_\cA]=0`.
  Then change line 41 to that exact formula and make early statements/proofs cite the new definition instead of a later theorem.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:30303):30303, 30566, 30598, 3611, 4017 — PROBLEM: the operator in the MC equation drifts. `D_\cA` is defined at 24-25 as the total bar differential, but 30303/30566/30598 write `D_\cA\Theta_\cA + \frac12[\Theta_\cA,\Theta_\cA]=0`, while the actual strict MC derivation later is `[ \dzero,\Theta_\cA ] + \frac12[\Theta_\cA,\Theta_\cA]=0`. With current notation, the displayed equations are wrong. FIX: enforce one notation rule globally: `D_\cA` means only the total bar differential; the dg-Lie differential is `d_{\mathrm{Lie}}=[\dzero,-]`. Replace every `D_\cA\Theta...` and `D_\cA\Theta^{\le r}...` by `d_{\mathrm{Lie}}(\Theta...)`.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12265):12265, 14816, 14977, 29698 — PROBLEM: the file repeatedly identifies the truncated MC element with its scalar projection: `\Theta_\cA^{\leq 2}=\kappa(\cA)`. That is type-incorrect. Later formulas bracket `\Theta^{\le2}`, and 29698 gives an actual tensor representative `\kappa\cdot\eta\otimes\Lambda`. FIX: replace every bare equality of that form by `\pi_{\mathrm{sc}}(\Theta_\cA^{\le2})=\kappa(\cA)`. Where scalar saturation is intended, write `\Theta_\cA^{\le2}=\kappa(\cA)\,\eta\otimes\Lambda` and explicitly tag the scope.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:180):180, 3836; [chapters/theory/e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:290):290 — PROBLEM: `\Theta_\cA^{E_1}` and `({\gAmod}^{E_1})` are used as if they were local objects, but this file never defines them; the actual definition lives in the separate `E_1` chapter. That is a hidden import on the foundational surface. FIX: before the first ordered mention, insert one explicit import sentence:
  `By Chapter~\ref{chap:e1-modular-koszul}, the ordered dg Lie algebra ${\gAmod}^{E_1}$ carries the bar-intrinsic class \Theta_\cA^{E_1}:=D_\cA^{E_1}-\dzero, and \operatorname{av}(\Theta_\cA^{E_1})=\Theta_\cA.`
  Then keep later uses tied to that import.

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14816):14816-14818 — PROBLEM: “The five main theorems are projections of the scalar level `\Theta_{\cA}^{\le2}=\kappa(\cA)`” is false even by the table that follows: rows A/B/C/H immediately use genus-0 twisting, involution, cross-polarization, and degree-preserving sub-MC data, not the scalar level. FIX: replace the lead sentence with:
  `The five main theorems are projections or consequences of the master MC element \Theta_\cA and its shadow tower; only Theorem D is the scalar level.`

## Summary
Checked: 24 | Findings: 8 | Verdict: FAIL


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
session id: 019d8774-0777-76e1-a53a-77d148852037
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


MISSION: FOUNDATION AUDIT of chapters/theory/higher_genus_modular_koszul.tex

Check: is the shadow tower Theta_A formally defined? Are G/L/C/M classes defined before use? Is the MC equation stated as a definition before being invoked in proofs? Is the convolution algebra g^{E1} and g^{mod} defined?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers



thinking
**Clarifying the audit process**

I need to audit a specific file, which means I should read the necessary constitutional documents before making any substantive edits. Even though the user asked for an audit, we might need to consider files like CLAUDE, concordance, theorem_registry, and red_team_summary. I'll probably use the deep-beilinson-audit skill for this, focusing on foundational definitions in one file. It’ll be important to announce in the commentary which skill I'm using and provide an update to the plan. Inspections need to ground every claim in what is actually read.
thinking
**Conducting an extensive audit**

I need to perform a thorough audit of the specified file, focusing on specific questions like whether Theta_A is formally defined and if classes G/L/C/M are established before their use. I also want to check if the MC equation is defined prior to being used in proofs, and whether convolution algebra g^{E1} and g^{mod} are defined. Every missing definition or unresolved reference counts as a finding, so I may need to read the entire file and check dependencies. Using a code explorer sub-agent might help locate relevant definitions across files.
thinking
**Preparing for the skill read**

I think it’s important to read the skill instructions first. I'll consider using the commentary tool with exec_command to access the skill file and its sections. It might be effective to use multi_tool_use.parallel to execute these read commands simultaneously. Before diving into this work, it’s necessary to start with a commentary update to keep track of what I’m doing. That way, I’m organized and ready for the task ahead.
codex
Using `deep-beilinson-audit` on `chapters/theory/higher_genus_modular_koszul.tex`. I’m reading the skill and the live claim surface first, then I’ll trace every cited definition and theorem boundary instead of treating local prose as self-sufficient.
exec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
Total output lines: 260

# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

 succeeded in 51ms:
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
Total output lines: 260

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

thinking
**Planning audit steps**

I need to prepare a summary for the red team and identify the exact target file. It seems like I'd need to read through large relevant sections, perhaps even the entire document. I might use a tool to locate important terms and dependencies like theorem labels and definitions referenced in the target file. There shouldn’t be any edits, just an audit of findings. I should also check the current claimed status of the audit surface and include that in my commentary. Let's start with the red team summary and target file, focusing on relevant searches.
codex
I have the constitutional surface and registry; now I’m pinning the exact loci inside `higher_genus_modular_koszul.tex` where the file claims to define or use `\Theta_\cA`, the family classes, the MC equation, and the two convolution algebras. Then I’ll read each cited dependency in context rather than trusting labels alone.
exec
/bin/zsh -lc "sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theta_|\\\\Theta|g\\"'^'"\\{E1\\}|g\\"'^'"\\{mod\\}|\\\\gAmod|Maurer|MC equation|G/L/C/M|class~G|class~L|class~C|class~M|convolution\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 exited 2 in 51ms:
rg: regex parse error:
    (?:Theta_|\Theta|g\^\{E1\}|g\^\{mod\}|\gAmod|Maurer|MC equation|G/L/C/M|class~G|class~L|class~C|class~M|convolution)
              ^^
error: unrecognized escape sequence
 succeeded in 50ms:
\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.

Bar-cobar inversion (Theorem~B) proves that
$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
The proof uses one fact: the bar differential squares to zero.
At genus~$g \geq 1$, this fact fails fiberwise.
The bar complex $\barB^{(g)}(\cA)$ acquires curvature
\[
 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
\]
%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
where $\omega_g = c_1(\lambda)$ is the Hodge class on
$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
The fiberwise differential no longer squares to zero; cobar inversion,
as stated, does not extend.


thinking
**Searching for relevant sections**

I'm looking for target files that include more relevant sections. I'll need to perform searches with fixed strings, possibly using a command like `rg -F` for simpler patterns and ensuring I get line numbers. It's crucial to locate definitions of relevant objects, which might be scattered within the file and elsewhere. There are specific items I need to read around, like definitions and theorems. So, I'll check if these definitions actually provide clear explanations or if they show up later on. I might also have to use `rg -n` to find labels and terms in the target file and address any regex issues. Finally, I'll pinpoint line numbers where these target items are located.
codex
The opening section already makes a strong foundational claim surface. I’m now checking ordering: whether the file invokes `\Theta_\cA`, the MC equation, and the class partition before the reader has a local or imported definition, and whether each import actually lands on the object the prose says it does.
exec
/bin/zsh -lc "rg -n -F \"Theta_\\cA\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "g''^{E1}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "g''^{mod}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 409

37:Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
41: d_0 \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0
46:$\Theta_\cA$ carries.
54:do not obstruct existence of~$\Theta_\cA$; they obstruct its
64:$\Theta_\cA^{\leq r}$ is a graph sum through degree~$r$, with vertex
70:Five constructions govern $\Theta_\cA$.
75: The MC element $\Theta_\cA$ lives in an infinite-dimensional
82: degree-$r$, genus-$g$ projections of~$\Theta_\cA$.
88: computes \emph{how}: $\Theta_\cA^{\leq r}$ is a sum over
94: The graph-sum formula produces $\Theta_\cA^{\leq r}$ but gives
98: (D_\cA\Theta_\cA^{\leq r}
99: + \tfrac12[\Theta_\cA^{\leq r},\Theta_\cA^{\leq r}])_{r+1}
113: $\Theta_\cA$ exists unconditionally by the bar-intrinsic
114: construction, and $\Theta_\cA^{\leq r}$ are its degree
121:The tower $\Theta_\cA$ forces three questions.
180:$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
251:$\Theta_\cA^{(g)} \in
 exited 1 in 51ms:

 exited 1 in 51ms:

exec
/bin/zsh -lc 'rg -n -F "Maurer--Cartan" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "subsec:two-level-convention" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"class~\\mathsf\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
62:(\S\ref{subsec:two-level-convention}). The weight filtration on
10824:\label{subsec:two-level-convention}
30733: \textup{(}\S\textup{\ref{subsec:two-level-convention}}\textup{)}.
30764:(\S\ref{subsec:two-level-convention}) establishes that
 exited 1 in 52ms:

 succeeded in 52ms:
39:$\Theta_\cA \in \gAmod$ satisfies the Maurer--Cartan equation
449:a genus-completed Maurer--Cartan datum~$\Theta_{\cA}$
486:The genus tower arises from a filtered Maurer--Cartan deformation
2642:\index{universal Maurer--Cartan class|textbf}
2646:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2658:\item The \emph{universal Maurer--Cartan class}
2748: is a filtered Maurer--Cartan deformation of the genus-$0$ bar object
3035:Maurer--Cartan element, or Theorem~\ref{thm:genus-universality}
3471:\index{Maurer--Cartan element!two projections}
3570:\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
3572:\index{universal Maurer--Cartan class|textbf}
3576:universal Maurer--Cartan class
3613:gives the Maurer--Cartan equation. See
3753:simultaneously. The Maurer--Cartan equation
3771:\index{universal Maurer--Cartan class!bar-intrinsic construction}
3801:\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
3922:$\Theta_\cA$ is automatically a Maurer--Cartan element.
4007:\emph{(i) Maurer--Cartan.}
4027:which is the Maurer--Cartan equation
4157:\index{Maurer--Cartan element!scattering-diagram construction}




thinking
**Assessing output issues**

I’m looking at the rg output, and it’s massive because of too many matches. I think I might need to focus on specific line regions, perhaps by using rg to find labels and then employing sed for adjustments. I need to conduct a foundational audit, aiming for exact lines with problems. The user wants an exhaustive review, so I'll dig deeper, especially considering potential findings in the opening section. I'll pay close attention to the first 200 lines and definitions later on.
thinking
**Reviewing definitions and fixes**

I need to check if the MC equation is defined before it's used in proofs, and also whether the convolution algebras g^{E1} and g^{mod} are properly defined. It’s crucial to see if imported labels have clear definitions in dependencies and if they align with the claims. I should also determine if the \gAmod macro isn’t expanded anywhere. The user is asking for specific fixes, so I’ll propose direct changes or structural moves, citing exact line references for any issues I find.
thinking
**Analyzing definitions and references**

I plan to use nl -ba and sed around specific lines, particularly from 1 to 140 and the definitions section at 3570. I also need to check the two-level convention section at around line 10800 and potentially later class definitions. I’ll utilize rg for searching label definitions like def:shadow-algebra and thm:recursive-existence to confirm if they provide necessary definitions. I’m aware that the user is looking for every missing definition, hidden import, unresolved reference, and unjustified step. This is quite a task!
thinking
**Assessing severity levels**

I'm thinking about the terms and whether they should be defined locally, maybe as low or medium? I need to carefully assess the severity. To do this, I should inspect the line-numbered opening section, focusing on the first 200 lines. This way, I can gather a better understanding of what I'm working with and make a more informed decision. Let's take a closer look!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '220,360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   220	\end{center}
   221	Horizontal maps restrict to degenerate curves in $\partial\overline{\mathcal{M}}_g$;
   222	vertical maps are bar-cobar inversion at each genus.
   223	
   224	\begin{definition}[Completed chiral algebra]\label{def:completed-chiral-algebra}
   225	\index{completed chiral algebra|textbf}
   226	The \emph{completed chiral algebra} is the inverse limit:
   227	\[
   228	\mathcal{A}_{\mathrm{complete}}
   229	= \varprojlim_g \mathcal{A}^{(g)},
   230	\]
   231	For the bookkeeping parameter $\hbar$ tracking genus,
   232	$\mathcal{A}_{\mathrm{complete}}$ is a $\mathbb{C}[\![\hbar]\!]$-module with
   233	$\mathcal{A}_{\mathrm{complete}} / \hbar^{g+1} = \bigoplus_{h=0}^{g} \mathcal{A}^{(h)}$.
   234	\end{definition}
   235	
   236	\begin{proposition}[MCG-equivariance of the genus tower; \ClaimStatusProvedHere]
   237	\label{prop:mcg-equivariance-tower}\label{prop:modular-invariance-tower}
   238	\index{mapping class group!equivariance of genus tower}
   239	\index{modular invariance!genus tower}
 succeeded in 51ms:
     1	\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
     2	
     3	%% DEFICIENCY OPENING: the genus-0 machine breaks at g >= 1.
     4	
     5	Bar-cobar inversion (Theorem~B) proves that
     6	$\Omegach(\barBch(\cA)) \to \cA$ is a quasi-isomorphism on the
     7	rational configuration space $\overline{C}_n(\mathbb{P}^1)$.
     8	The proof uses one fact: the bar differential squares to zero.
     9	At genus~$g \geq 1$, this fact fails fiberwise.
    10	The bar complex $\barB^{(g)}(\cA)$ acquires curvature
    11	\[
    12	 d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g \neq 0,
    13	\]
    14	%: d^2_bar = 0 always; d^2_fib = kappa*omega_g is FIBERWISE, g >= 1
    15	where $\omega_g = c_1(\lambda)$ is the Hodge class on
    16	$\overline{\mathcal{M}}_g$ and $\kappa(\cA)$ is the modular
    17	characteristic of~$\cA$ (Definition~\ref{def:modular-characteristic-package}).
    18	The fiberwise differential no longer squares to zero; cobar inversion,
    19	as stated, does not extend.
    20	



thinking
**Auditing foundation files**

I need to examine the foundation surface, possibly with a specific checklist for the entire file, even though it's really large at 35k lines. Focusing solely on the surface plus any secondary failures around it seems essential. The user requests a thorough audit, so I should summarize counts and be exact in my fixes. I have to check if line 37 provides a formal definition of Theta_A or if we should insert a definition environment nearby. It seems like the definition isn't formal.
thinking
**Verifying definitions and theorems**

I need to check if there's a formal definition or theorem related to the shadow tower label, likely around line 4831. I should read through the sections where `Theta_A` is defined and check the two-level convention near line 10824. I’ll also search for class definitions and relevant labels like `\mathsf{G}` and "Gaussian." 

I’m considering searching for formal definition environments for shadow classes, `four shadow classes`, or `class\\mathsf`. Additionally, I should look for `\gAmod` definitions using macros or explicit formulas and explore theorems around line 3570 and other relevant sections.
thinking
**Searching for definitions**

I need to look for definitions related to the two-level convention, particularly around line 10824. I think reading through the context surrounding that section will help clarify what it means. There might be important insights or definitions that I need to keep an eye on. Reading closely will also ensure I don’t miss anything relevant that could assist in understanding the larger context. Let’s dive into that section and figure it out!
codex
The initial section already uses `\gAmod`, `\Theta_\cA^{E_1}`, and the G/L/C/M partition as if they are settled objects. I’m reading the later theorem/definition blocks now to see whether those objects are ever formally introduced in this file or whether the chapter only gestures at them by name.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3560,3855p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"class~\\mathsf{G}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3870,4165p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10720,10890p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3560	K_0(\overline{\mathcal{M}}_g)$: $c_1(\det\mathcal{V})$
  3561	recovers~$\kappa$, $\operatorname{ch}(\mathcal{V})$
  3562	recovers~$\Delta_{\cA}$, and the holonomy recovers~$\Pi_{\cA}$.
  3563	See Remark~\ref{rem:structural-saturation}.
  3564	\end{remark}
  3565	
  3566	\begin{remark}[Shared discriminant, distinct sewing]\label{rem:shared-discriminant-sheet}
  3567	The algebras $\widehat{\mathfrak{sl}}_2$, $\mathrm{Vir}_c$, and~$\beta\gamma$ all share the spectral discriminant $\Delta_\cA(x) = (1-3x)(1+x)$, yet their sewing kernels~$K_\cA$ and Euler--Koszul classes~$\operatorname{ek}$ differ: $\operatorname{ek} = 0, 1, 0$ respectively (Theorem~\ref{thm:shadow-euler-independence}).
  3568	\end{remark}
  3569	
  3570	\begin{theorem}[Universal modular Maurer--Cartan class; \ClaimStatusProvedHere]
  3571	\label{thm:universal-theta}
  3572	\index{universal Maurer--Cartan class|textbf}
  3573	For every modular Koszul chiral algebra~$\cA$ on a smooth
  3574	projective curve~$X$ with non-degenerate invariant form,
  3575	there exists a cyclic $L_\infty$-algebra $\Defcyc(\cA)$ and a
  3576	universal Maurer--Cartan class
  3577	\[
  3578	\Theta_{\cA} \in
  3579	\operatorname{MC}\!\bigl(
 exited 1 in 51ms:

 succeeded in 51ms:
 10720	the Feynman transform.
 10721	
 10722	In particular, the bar-cobar adjunction of Theorem~A is a
 10723	\emph{quantum $L_\infty$ functor}: it intertwines the modular $L_\infty$
 10724	structures on both sides, so homotopy transfer yields the
 10725	correct genus-refined operations
 10726	$\ell_{g,n}$. The non-renormalization theorem
 10727	(Theorem~\ref{thm:non-renormalization-tree}) follows: tree-level
 10728	operations are exact because $L_\infty$ transfer preserves MC
 10729	elements, and loop corrections are absorbed into the genus-raising
 10730	BV operator~$\Delta$.
 10731	\end{remark}
 10732	
 10733	\begin{remark}[The two Maurer--Cartan equations]
 10734	\label{rem:two-mc-equations}
 10735	\index{Maurer--Cartan equation!strict vs $L_\infty$}
 10736	The universal MC element $\Theta_\cA$ satisfies two forms of the
 10737	Maurer--Cartan equation, one in each layer of the two-level
 10738	convention (Remark~\ref{rem:two-level-convention}).
 10739	
 succeeded in 51ms:
  3870	 fill=black!5, font=\footnotesize] (Theta) at (1.8,-0.3)
  3871	 {$\Theta_\cA = \displaystyle\sum_{g \geq 1}
  3872	 \hbar^g d_\cA^{(g)}$};
  3873	%
  3874	% ---- Implication arrow ----
  3875	\draw[maparrow] (3.8,-0.3) -- (5.3,-0.3);
  3876	\node[font=\scriptsize, anchor=south] at (4.55,-0.1)
  3877	 {$D_\cA^2 = 0$};
  3878	%
  3879	% ---- MC equation ----
  3880	\node[draw, very thick, rounded corners=4pt, fill=black!5,
  3881	 minimum width=3.8cm, minimum height=0.7cm,
  3882	 font=\footnotesize] (MC) at (7.2,-0.3)
  3883	 {$d_0\Theta + \Theta\,d_0 + \Theta^2 = 0$};
  3884	%
  3885	% ---- Labels ----
  3886	\node[font=\tiny, text=black!50, anchor=north] at (-1.5,-0.8)
  3887	 {genus-$0$ bar differential};
  3888	\node[font=\tiny, text=black!50, anchor=north] at (1.8,-0.8)
  3889	 {positive-genus correction};

thinking
**Searching for definitions**

I'm trying to figure out why my search in "rg for class" isn't yielding helpful results. It seems like the spacing might be causing issues as there's no exact string match. I need to locate formal class definitions, so I think searching for terms like “Gaussian,” “Lie,” “contact,” and “mixed” in a later file could be more productive. Let's see if that works out better!
exec
/bin/zsh -lc 'rg -n -F "Lie)" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "contact" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Gaussian" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "mixed" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "four-class" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "shadow classes" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
138: (class~$\mathsf{L}$, Lie).
 succeeded in 51ms:
140: depth~$4$ (class~$\mathsf{C}$, contact).
10672: the quartic contact invariant
10673: $\mathfrak{Q}^{\mathrm{contact}}_{\mathrm{Vir}}
12307:\item $S_4 = \mathfrak{Q}(\cA)$ is the quartic contact term: the
12350: quartic contact term \\
12362:contact vertex, after which stratum separation on
12447:class~$\mathbf{C}$ at~$4$ (quartic contact), class~$\mathbf{M}$
12527: \quad(the quartic shadow / contact invariant);
13834:The quartic contact invariant
14999:+ \mathfrak{Q}(\cA)$ (contact archetype: $\beta\gamma$).
15706:\textbf{C} (contact, $r_{\max} = 4$): &
16759: The quartic contact term from composite fields terminates
16894: Thus the charged quartic contact class is nonzero and is the last
16899: Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.
17061:class~$\mathbf{C}$ has a quartic contact invariant
17115: $m_4 \neq 0$ from the contact quartic, $m_k = 0$ for
17189: contact quartic, rank-$1$ rigidity \\
17224:identity kills the quartic contact
17228:stratum and $m_4^{\mathrm{SC}} \neq 0$ from the contact
17229:quartic invariant $Q^{\mathrm{contact}}$
 succeeded in 51ms:
136: (class~$\mathsf{G}$, Gaussian).
3423:the genus expansion of the Gaussian Unitary Ensemble at
3439:exactly compensates the non-Gaussian CEO, restoring the
3440:Gaussian answer at every genus.
3442:criticality: class~G is the Gaussian model (no potential
10657: shadow-tower termination at degree~$2$ (Gaussian archetype).
11810:Gaussian algebras (Heisenberg),
11990:\textbf{Heisenberg} (Gaussian)
14985:$\mathfrak{C}(\cA) = 0$ (Gaussian archetype: Heisenberg).
15700:\textbf{G} (Gaussian, $r_{\max} = 2$): &
16565:$\mathbf{G}$ & Gaussian &
16708: The shadow tower is a single Gaussian integral.
16748:the Coulomb branch produces $U(1)^r$ (the abelian/Gaussian sector)
16868:\item \emph{Gaussian \textup{(}$\mathbf{G}$,
16989: font=\footnotesize\scshape] at (0,5.5) {Gaussian ($\mathbf{G}$)};
17542:\begin{corollary}[Gaussian decomposition]
17545:\index{shadow metric!Gaussian decomposition}
17558:is the \emph{Gaussian envelope}: a perfect square, the shadow
17580:The Gaussian decomposition reduces the entire shadow tower to a
17638:is the Gaussian decomposition
 succeeded in 51ms:
17959:The Hankel data for the standard shadow classes:
21755:\index{tautological ring!shadow classes}
21876:\index{tautological ring!shadow classes|textbf}
 succeeded in 52ms:
154: obstructions at degrees $2$, $3$, $4$, and the four-class
16500:four-class partition
17098:is a strict four-class refinement of the binary formal/non-formal
19245:The four-class partition
 succeeded in 52ms:
144: (class~$\mathsf{M}$, mixed).
973:\label{lem:pbw-mixed-factorization}
974:\index{PBW spectral sequence!mixed map factorization|textbf}
975:\index{Whitehead lemma!mixed genus-0/genus-g factorization}
993:mixed genus-$0$/genus-$g$ contribution of $[\xi]$ on the $E_2$ page
995:Hence the mixed genus-$0$/genus-$g$ interaction is controlled by
1009:The mixed residue brackets the distinguished $\fg$-label with one of
1015:Chevalley--Eilenberg coboundary. Therefore the mixed $E_2$ class
1148:The mixed component is the degree-one part of the same diagonal
1149:$\fg$-action: by Lemma~\ref{lem:pbw-mixed-factorization}, every
1150:mixed class factors through $H^1(\fg, N_h^{n-1})$ for a
1169:By Lemma~\ref{lem:pbw-mixed-factorization}, the mixed
1176:the $E_2$ page through the mixed map.
1329:and the mixed genus-$0$/genus-$1$ map factors through
1331:\textup{(}Lemma~\textup{\ref{lem:pbw-mixed-factorization}}\textup{)}.
1471:Lemma~\ref{lem:pbw-mixed-factorization}, each basis vector of
1472:$H^{1,0}(\Sigma_g)$ produces the same mixed genus-$0$/genus-$g$
2084:is the first mixed genus-$1$ obstruction. Jordan blocks and
2145:mixed terms.}
2166:divisors). There are no mixed terms between core and
codex
I’ve confirmed the file eventually states a theorem for `\Theta_\cA`, but that does not yet answer the foundation question: the opening still may front-run its own objects, and the ordered/coinvariant algebra split may never get a clean local definition. I’m checking the later class tables and the E1/averaging language now.
exec
/bin/zsh -lc 'rg -n -F "averaging" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "ordered lift" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '15680,15740p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"E_1\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '19236,19270p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16490,16540p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3838:Chapter~\ref{chap:e1-modular-koszul}, and averaging sends
14863:and higher Yangian coherences that averaging discards
22966:\begin{remark}[Evidence for a motivic genus ladder in the averaging kernel]
22967:\label{rem:motivic-evidence-genus2-averaging-kernel}
22968:\index{averaging kernel!motivic evidence}
22977:$E_2^*, E_4, E_6$, and the genus-$1$ averaging kernel enlarges
23008:\begin{conjecture}[Motivic content of the genus-$2$ averaging kernel]
23009:\label{conj:motivic-content-genus2-averaging-kernel}
23011:\index{averaging kernel!motivic content conjecture|textbf}
23038:For general $g$, the genus-$g$ averaging kernel is governed by mixed
23058:\begin{remark}[Weight filtration on the averaging kernel]
23059:\label{rem:motivic-weight-filtration-averaging-kernel}
23062:of Conjecture~\ref{conj:motivic-content-genus2-averaging-kernel}.
32738:  the integrable quotient). The averaging map $\av_0$ is
32978:factorization, and the averaging map $\av_0$ at degree~$0$
33880:The averaging map $\av_2$ at degree~$2$ sends the
33885:genus~$0$ and genus~$1$: the averaging map is a local
 succeeded in 51ms:
 15680	Let $\mathfrak{h}$ be the minimal $L_\infty$-model
 15681	of $\Definfmod(\cA)$, i.e., the transferred structure
 15682	$(\cA^{\mathrm{sh}}, \{\ell_n^{\mathrm{sh}}\})$
 15683	of Proposition~\ref{prop:shadow-algebra-linfty}.
 15684	Then $\Definfmod(\cA)$ is \emph{formal} (quasi-isomorphic to
 15685	its cohomology with trivial differential and the descended
 15686	Lie bracket) if and only if $\ell_n^{\mathrm{sh}} = 0$ for all
 15687	$n \geq 3$. The shadow obstruction tower measures the
 15688	deviation from formality:
 15689	\[
 15690	\operatorname{Sh}_r(\cA)
 15691	\;=\;
 15692	\ell_r^{\mathrm{sh}}(\Theta^{\leq r-1}, \ldots,
 15693	\Theta^{\leq r-1})
 15694	\]
 15695	is the evaluation of the $r$-th transferred bracket on the
 15696	truncated MC element. The four shadow depth classes are:
 15697	\begin{center}
 15698	\small
 15699	\begin{tabular}{ll}
 succeeded in 51ms:
3835:The ordered lift
 succeeded in 51ms:
180:$R$-matrix as $\pi_{2,0}(\Theta_\cA^{E_1})$, the genus-$0$ binary
181:shadow of the $E_1$-framed MC element.
803:$E_1$ page splits as
805:E_1^{p,q}(g)
807:E_1^{p,q}(g{=}0) \oplus \mathcal{E}^{p,q}_g,
905:an $E_1$ statement. For non-semisimple symmetry, the obstruction is the
1049:\emph{Step~1: Decomposition of the $E_1$ page.}
1063:collision divisors. The $E_1$ page concentrates
1087:Hence the $E_1$ page decomposes:
1089:E_1^{p,q}(g{=}1) \;=\; E_1^{p,q}(g{=}0)
1092:where $E_1(g{=}0)$ is the concentrated genus-$0$
1113:\;\longrightarrow\; E_1^{n-1,h}(g{=}0)
1404:\emph{Step~1: $E_1$ decomposition at genus~$g$.}
1423:E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0)
1650:The genus-$g$ decomposition of the enriched $E_1$ page is identical to
1653:E_1^{p,q}(g) \;=\; E_1^{p,q}(g{=}0) \oplus \mathcal{E}^{p,q}_g,
1908:already accounted for on~$E_1$), while generators with $s < 2$
2058:$E_1$ statement. The affine KM proof gives the boundary example:
2062:$E_1$-collapse claim without adding a false statement.
2275: $E_1$ differentials as on~$\mathbb{P}^1$: the
 succeeded in 50ms:
 19236	lives in $\Defcyc^{(q)}$ with $q \neq 0$.
 19237	The self-bracket
 19238	$\Defcyc^{(q)} \otimes \Defcyc^{(q)} \to \Defcyc^{(2q)}$
 19239	has $\dim \Defcyc^{(2q)} = 0$ for rank-one systems:
 19240	the quartic pump does not activate, so $r_{\max} = 4$.
 19241	This is rank-one rigidity
 19242	(Theorem~\ref{thm:betagamma-rank-one-rigidity})
 19243	as stratum separation.
 19244	
 19245	The four-class partition
 19246	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
 19247	persists on multi-stratum systems.
 19248	The charge-graded master equation
 19249	$S_r^{(\mathbf{q})} =
 19250	-(P/(2r))\sum c_{jk}\,jk\,
 19251	S_j^{(\mathbf{q}_1)} S_k^{(\mathbf{q}_2)}$
 19252	(sum over $j+k=r{+}2$, $\mathbf{q}_1{+}\mathbf{q}_2 = \mathbf{q}$)
 19253	decomposes the obstruction by charge.
 19254	If $\alpha \neq 0$ on any sector $\Defcyc^{(\mathbf{q}_0)}$,
 19255	the adjoint $\mathrm{ad}_{S_3^{(\mathbf{q}_0)}}$ generates
 succeeded in 50ms:
 16490	\textup{(}Proposition~\textup{\ref{prop:shadow-formality-low-degree}},
 16491	degrees $2$--$4$\textup{)}, this gives the shadow--formality
 16492	identification constructively through degree~$7$: the
 16493	shadow obstruction tower, the $A_\infty$-formality obstruction tower,
 16494	and the $L_\infty$-formality obstruction tower coincide
 16495	through seven degrees, with the all-degree identification
 16496	proved non-constructively by induction
 16497	\textup{(}Theorem~\textup{\ref{thm:shadow-formality-identification}}\textup{)}.
 16498	
 16499	In the depth classification, this confirms that the
 16500	four-class partition
 16501	$\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$
 16502	is an operadic invariant: it measures the $L_\infty$-formality
 16503	level of $\gAmod$ simultaneously in the $A_\infty$
 16504	\textup{(}associative\textup{)} and $L_\infty$
 16505	\textup{(}Lie\textup{)} pictures. The agreement at
 16506	degrees $5$--$7$ for the Virasoro algebra is a nontrivial
 16507	check because the $A_\infty$ tree formula
 16508	\textup{(}$14 + 42 + 132$ trees at degrees $5$--$7$
 16509	via HPL\textup{)} and the $L_\infty$ stable-graph expansion

thinking
**Inspecting algebra concepts**

I need to take a closer look at something related to the number 31537, which might define an ordered ambient algebra. I'm curious about how this connects to g^{E1}. There seems to be a thread worth pulling to understand what it means and how everything fits together. Let’s explore the implications of this ordered structure and see if it leads me to any useful insights or conclusions!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31530,31610p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "def:modular-convolution-dg-lie" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14840,14875p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "def:shadow-algebra" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "def:shadow-postnikov-tower" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14070,14092p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 31530	Theorem~\ref{thm:ambient-d-squared-zero}: every
 31531	codimension-$2$ stratum appears in exactly two
 31532	codimension-$1$ strata with opposite orientations.
 31533	The ordering does not affect the orientation
 31534	cancellation.
 31535	\end{proof}
 31536	
 31537	\begin{corollary}[$E_1$ ambient $D^2 = 0$]
 31538	\label{cor:e1-ambient-d-squared-zero}
 31539	\ClaimStatusProvedHere
 31540	\index{differential!E1 ambient square-zero@$E_1$ ambient square-zero}
 31541	The five-component differential on the ordered ambient
 31542	algebra
 31543	\textup{(}Definition~\textup{\ref{def:ordered-ambient-algebra}}\textup{)}
 31544	satisfies $D^2 = 0$. For each stable pair $(g,n)$, its geometric
 31545	source is the ordered relative
 31546	Fulton--MacPherson space
 31547	$\operatorname{FM}^{\mathrm{ord}}_k(\cC_{g,n}/\overline{\cM}_{g,n})$
 31548	of the universal curve: the ordered collision faces give the
 31549	bar part, whose square vanishes by the ordered Arnold cancellation,
 succeeded in 51ms:
3964: (Definition~\ref{def:modular-convolution-dg-lie}).
4122: (Definition~\ref{def:modular-convolution-dg-lie},
8608: (Definition~\ref{def:modular-convolution-dg-lie}) on the arc space
10175:\label{def:modular-convolution-dg-lie}
10742:(Definition~\ref{def:modular-convolution-dg-lie}):
10838:Definition~\ref{def:modular-convolution-dg-lie} is its strict model.
10952:Definition~\ref{def:modular-convolution-dg-lie} is the strict
11438:(Definition~\ref{def:modular-convolution-dg-lie}) is the bar-side
12037:(Definition~\ref{def:modular-convolution-dg-lie}) induces a
13317:(Definition~\ref{def:modular-convolution-dg-lie}).
25470:(Definition~\ref{def:modular-convolution-dg-lie})
26519:convolution algebra (Definition~\ref{def:modular-convolution-dg-lie}):
30260:(Definition~\ref{def:modular-convolution-dg-lie}).
30771:(Definition~\ref{def:modular-convolution-dg-lie}).
31637:\textup{(}Definition~\textup{\ref{def:modular-convolution-dg-lie})},
 succeeded in 51ms:
 14840	 Degree-preserving sub-MC &
 14841	 Polynomiality from Koszul concentration \\
 14842	\bottomrule
 14843	\end{tabular}
 14844	\end{center}
 14845	\end{remark}
 14846	
 14847	\begin{remark}[The five theorems as coinvariant shadows of the $E_1$ theory]
 14848	\label{rem:five-theorems-as-av-images}
 14849	\index{main theorems!as av-images of E1@$E_1$ theory}
 14850	Each row of the table above is the $\Sigma_n$-coinvariant
 14851	image of a richer $E_1$ statement
 14852	(Theorem~\textup{\ref{thm:e1-primacy}}):
 14853	Theorem~A is the averaged form of the $E_1$ bar-cobar
 14854	adjunction on ordered configurations;
 14855	Theorem~B is the averaged form of the $E_1$~Quillen equivalence;
 14856	Theorem~C is the averaged form of complementarity in the ordered
 14857	convolution algebra;
 14858	Theorem~D extracts the scalar $\kappa = \operatorname{av}(r(z))$
 14859	from the spectral $r$-matrix;
 succeeded in 50ms:
101: (Definition~\ref{def:shadow-postnikov-tower}).
2819:(Definition~\ref{def:shadow-postnikov-tower};
3764:Definition~\ref{def:shadow-postnikov-tower}.
3925:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.}%
10161:(Definition~\ref{def:shadow-postnikov-tower}).
10593:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
12230:\label{def:shadow-postnikov-tower}
13168:(Definition~\ref{def:shadow-postnikov-tower}).
14819:(Definition~\ref{def:shadow-postnikov-tower}):
15286: \textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower})}.
15750: \textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower}}\textup{)}.
28494:(Definition~\ref{def:shadow-postnikov-tower}).
30595:\textup{(}Definition~\textup{\ref{def:shadow-postnikov-tower}}\textup{)}.
30881:(Definition~\ref{def:shadow-postnikov-tower}) is defined
 succeeded in 50ms:
80: (Definition~\ref{def:shadow-algebra})
4164:Definition~\ref{def:shadow-algebra}, graded by shadow degree, and
4316: Definition~\textup{\ref{def:shadow-algebra}}\textup{)}.
4330:(Definition~\ref{def:shadow-algebra}):
12483:\label{def:shadow-algebra}
30287: (Definition~\ref{def:shadow-algebra}).
 succeeded in 50ms:
 14070	 \textup{(}\S\textup{\ref{sec:concordance-non-principal-w})}:
 14071	 the DS functor acts on primitive kernels as
 14072	 $\mathfrak{K}_{\mathcal{W}_k(\mathfrak{g},f)}
 14073	 = \operatorname{DS}_f(\mathfrak{K}_{V_k(\mathfrak{g})})$
 14074	 in the proved corridor \textup{(}principal, hook-type in type~A\textup{)}.
 14075	 For non-principal $f$ outside this corridor, the obstruction is
 14076	 concentrated in the rigid cutting sector: $\operatorname{DS}_f$
 14077	 may fail to commute with the planted-forest corrections $R_\rho$.
 14078	\item \emph{$E_1$ ordered bar complex}
 14079	 \textup{(}Chapter~\textup{\ref{chap:e1-modular-koszul})}:
 14080	 the cofree-coderivation principle applied to $F\!\Ass$ gives an
 14081	 $E_1$ primitive kernel $\mathfrak{K}_\cA^{E_1}$ with
 14082	 $\operatorname{av}(\mathfrak{K}_\cA^{E_1}) = \mathfrak{K}_\cA$.
 14083	 The genus-$0$, degree-$2$ $E_1$ primitive corolla is the classical
 14084	 $r$-matrix: $K_{0,2}^{\cA,E_1} = r(z)$.
 14085	\end{enumerate}
 14086	\end{remark}
 14087	
 14088	%% ----------------------------------------------------------------
 14089	%% THE PRIMITIVE FLAT CONNECTION

thinking
**Researching definitions**

I’m looking into some definitions that involve the numbers 10175, 12230, and 12483. It seems important to get clarity on these terms. I’m curious about what they might relate to, whether they’re specific to a field or context. I'll gather information on each of these numbers to provide a clearer understanding. It feels like it'll be a small puzzle to piece together! Let's see what I find out!
exec
/bin/zsh -lc 'rg -n -F "theta tower" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"shadow obstruction tower\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12220,12520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '10160,10260p'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
151: genus-$0$ shadow obstruction tower coincides with the
2231:\text{Thm D, shadow obstruction tower}
2351:\item The shadow obstruction tower
2719:$\Defcyc^{\mathrm{mod}}(\cA)$, so the shadow obstruction tower
2818:(3)~shadow obstruction tower / full MC: $\Theta_{\cA}^{\leq r}$, $\Defcyc(\cA)$
4145:The shadow obstruction tower convergence
4360:\item the shadow obstruction tower $\Theta_\cA^{\leq r}$
4839:shadow obstruction tower
8327:shadow obstruction tower and by the spectral/periodic invariants.
10130:uniform-weight lane; the non-scalar shadow obstruction tower
10160:convolution dg~Lie algebra together with its shadow obstruction tower
10795: The shadow obstruction tower measures the
11067:the shadow obstruction tower ($o^{(r)}_{\mathrm{Vir}}\neq 0$ for all
11163:\item The full shadow obstruction tower
11264:%% algebra, E₁ shadow obstruction tower, and the five main theorems
12138:\subsection{The shadow obstruction tower}
12232:\index{shadow obstruction tower|textbf}
12233:\index{modular characteristic!shadow obstruction tower}
12234:The \emph{shadow obstruction tower} of $\cA$
12273:The shadow obstruction tower is the primary nonlinear object of
 succeeded in 51ms:
 10160	convolution dg~Lie algebra together with its shadow obstruction tower
 10161	(Definition~\ref{def:shadow-postnikov-tower}).
 10162	The five main theorems and the genus expansion descend from this tower;
 10163	Theorem~D extracts the scalar level~$\kappa(\cA)$, while the
 10164	cubic and quartic shadows are proved at finite order.
 10165	The all-degree limit is a Maurer--Cartan element
 10166	$\Theta_{\cA} \in \operatorname{MC}(\mathfrak{g}^{\mathrm{mod}}_{\cA})$,
 10167	constructed from the genus-completed bar differential
 10168	(Theorem~\ref{thm:mc2-bar-intrinsic}).
 10169	
 10170	\subsection{The modular convolution dg~Lie algebra}
 10171	\label{subsec:modular-convolution-algebra}
 10172	\index{modular convolution dg Lie algebra|textbf}
 10173	
 10174	\begin{definition}[Modular convolution dg~Lie algebra]
 10175	\label{def:modular-convolution-dg-lie}
 10176	Let $\cA$ be a cyclic chiral algebra on a smooth projective curve~$X$.
 10177	The following dg~Lie algebra is the strict model of the modular
 10178	quantum $L_\infty$-algebra of
 10179	Theorem~\ref{thm:modular-homotopy-convolution}.
 succeeded in 52ms:
 12220	\operatorname{MC}\bigl(
 12221	\mathfrak{g}^{\mathrm{amb}}_{\cA}/F^{N+1}
 12222	\bigr),
 12223	\qquad N \geq 1.
 12224	\end{equation}
 12225	A full lift is a compatible point of the inverse limit
 12226	$\Theta_{\cA} \in \varprojlim_N \mathcal{E}_{\cA}(N)$.
 12227	\end{definition}
 12228	
 12229	\begin{definition}[Shadow obstruction tower]
 12230	\label{def:shadow-postnikov-tower}
 12231	\ClaimStatusProvedHere
 12232	\index{shadow obstruction tower|textbf}
 12233	\index{modular characteristic!shadow obstruction tower}
 12234	The \emph{shadow obstruction tower} of $\cA$
 12235	\textup{(}Figure~\textup{\ref{fig:shadow-postnikov-tower})}
 12236	is the sequence of
 12237	finite-order truncations
 12238	\begin{equation}
 12239	\label{eq:shadow-postnikov-tower}
exec
/bin/zsh -lc 'rg -n -F "def:shadow-depth-classification" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"r_{\\max}\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16850,16920p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16540,16620p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2486:(Definition~\ref{def:shadow-depth-classification})
12334:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}
16542:\label{def:shadow-depth-classification}
16863:\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
17239:(Definition~\ref{def:shadow-depth-classification}).
17625:of Definition~\textup{\ref{def:shadow-depth-classification}}.
28467:(Definition~\textup{\ref{def:shadow-depth-classification}})
29772:(Definition~\ref{def:shadow-depth-classification}):
 succeeded in 52ms:
4550: $\boldsymbol\Theta^{\pm}_{\leq r_{\max}}
4589:for $r > r_{\max}$
4591:no bipartite graphs with more than $r_{\max}$ external legs
9491:$r_{\max} = \dim V$ on a Zariski-open subset of~$U$.
9494:E \;:=\; \bigl\{\, k \in U : \operatorname{rk} M(k) < r_{\max} \,\bigr\}
12342:\textbf{Class} & $r_{\max}$ & \textbf{Surviving corrections} &
12416: {$\mathbf{G}$: Heis, $r_{\max}\!=\!2$};
12419: {$\mathbf{L}$: aff, $r_{\max}\!=\!3$};
12422: {$\mathbf{C}$: $\beta\gamma$, $r_{\max}\!=\!4$};
12425: {$\mathbf{M}$: Vir, $r_{\max}\!=\!\infty$};
12609: Shadow depth $r_{\max} < \infty$ is equivalent to
12735:$\cA^{\mathrm{sh}}_{r,0} = 0$ for $r > r_{\max}(\cA)$.
12737:explicit bounds: $r_{\max} = 2$
15003:Repeat. Termination at degree~$r_{\max}$ means
15004:$\cA^{\mathrm{sh}}_{r,0} = 0$ for $r > r_{\max}$.
15028: & \emph{Class} & $r_{\max}$ & $\kappa(\cA)$
15079:\emph{Class} & $r_{\max}$
15269:$d_\infty(\hat{\mathfrak{g}}_k) = 3 = r_{\max}$.
15284: $r_{\max}(\cA) := \sup\{r \geq 2 :
15301:r_{\max}(\cA)
 succeeded in 51ms:
 16540	
 16541	\begin{definition}[Shadow depth classification]
 16542	\label{def:shadow-depth-classification}
 16543	\ClaimStatusProvedHere
 16544	\index{shadow depth|textbf}
 16545	\index{shadow depth!classification}
 16546	\index{shadow obstruction tower!depth classification}
 16547	Let $\cA$ be a modular Koszul chiral algebra with
 16548	obstruction classes $o_r(\cA)$ from
 16549	Construction~\ref{constr:obstruction-recursion}.
 16550	Define the \emph{shadow depth}
 16551	$\kappa_d(\cA) := r_{\max}(\cA) =
 16552	\sup\{r \geq 2 : \cA^{\mathrm{sh}}_{r,0} \neq 0\}$
 16553	(with the convention $\kappa_d = \infty$ if the tower
 16554	does not terminate).
 16555	The \emph{shadow depth class} of~$\cA$ is determined
 16556	by the vanishing pattern of obstruction classes:
 16557	\begin{center}
 16558	\small
 16559	\renewcommand{\arraystretch}{1.15}
 succeeded in 52ms:
 16850	
 16851	\begin{theorem}[Shadow archetype classification]
 16852	\label{thm:shadow-archetype-classification}
 16853	\ClaimStatusProvedHere
 16854	\index{shadow depth!classification theorem|textbf}
 16855	\index{shadow archetype classification|textbf}
 16856	Every chirally Koszul algebra in the standard landscape has algebraic
 16857	shadow depth
 16858	\[
 16859	 d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
 16860	\]
 16861	Equivalently, it belongs to exactly one of the shadow depth classes
 16862	$\mathbf{G}$, $\mathbf{L}$, $\mathbf{C}$, or $\mathbf{M}$
 16863	\textup{(}Definition~\textup{\ref{def:shadow-depth-classification}}).
 16864	The class is determined by the vanishing pattern of obstruction
 16865	classes at degrees~$3$, $4$, $5$, and the assignments for the
 16866	primitive archetypes are as follows:
 16867	\begin{enumerate}[label=\textup{(\roman*)}]
 16868	\item \emph{Gaussian \textup{(}$\mathbf{G}$,
 16869	$d_{\mathrm{alg}} = 0$, $r_{\max} = 2$\textup{)}:}



thinking
**Analyzing definitions and contradictions**

I'm noticing an interesting contradiction in the definitions involving finite depths and lattice vertex algebras. There's a mismatch with the AGENTS axiom regarding depths in {0,1,2,∞}, especially with the stated impossibility of a gap at 3. The user specifically asked to audit a file, but the definitions inside seem contradictory. I need to pinpoint the exact lines that reflect this conflict and see if there's a later theorem that clarifies the situation. It’s vital to verify this thoroughly.
thinking
**Identifying necessary changes**

I need to consider exact fixes related to specific lines in the document: deleting or downgrading lines 16594-16609 and 16611-16615. It's crucial to maintain a thorough four-class classification for families while potentially shifting any higher-depth lattice claims to a conjecture or remark section, away from foundational concepts. There are also contradictions I should inspect, particularly around the formal definition of Theta and its relationship to the shadow tower. It seems like the opening implies definitions that aren't formally established until later. I need to clarify these points!
thinking
**Considering definition order**

It seems like there’s an issue with the ordering in the document. The opening references Theta before its formal definition appears in theorem 3770. I think an exact fix would involve either moving that definition (lines 3776-3799) or at least inserting a forward reference definition around line 36. This could be classified as medium to high importance, depending on whether the later proofs rely on the formal definition established before theorem 3770. I need to clarify that!
exec
/bin/zsh -lc 'rg -n -F "def:completed-chiral-algebra" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "prop:mcg-equivariance-tower" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"thm:mc2-bar-intrinsic\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "thm:universal-theta" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
237:\label{prop:mcg-equivariance-tower}\label{prop:modular-invariance-tower}
 succeeded in 52ms:
224:\begin{definition}[Completed chiral algebra]\label{def:completed-chiral-algebra}
 succeeded in 52ms:
43:unconditionally (Theorem~\ref{thm:mc2-bar-intrinsic}).
255:\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})} is
293:(Theorem~\ref{thm:mc2-bar-intrinsic}) is the positive-genus
2350: \textup{(Theorem~\ref{thm:mc2-bar-intrinsic})}.
2648:symmetry by Theorem~\ref{thm:mc2-bar-intrinsic}), the
2705:is solved by Theorem~\ref{thm:mc2-bar-intrinsic}
2802:Theorem~\ref{thm:mc2-bar-intrinsic}; its clauses
2913:Theorem~\ref{thm:mc2-bar-intrinsic} constructs $\Theta_\cA$ and its
3614:Theorem~\ref{thm:mc2-bar-intrinsic} for the full construction.
3630:Theorem~\ref{thm:mc2-bar-intrinsic}(iv) for the full argument.
3770:\label{thm:mc2-bar-intrinsic}
3832:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
3840:Theorem~\ref{thm:mc2-bar-intrinsic} as the ordered $E_1$ statement is
4106:Theorem~\ref{thm:mc2-bar-intrinsic} to its roots, the complete
4161:Theorem~\ref{thm:mc2-bar-intrinsic}.
4244:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
4294:Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
4348:exists at all genera by Theorem~\ref{thm:mc2-bar-intrinsic},
4846:(Theorem~\ref{thm:mc2-bar-intrinsic};
5283:assembly in Theorem~\ref{thm:mc2-bar-intrinsic}. Consequently the
 succeeded in 51ms:
672:(Theorem~\ref{thm:universal-theta}).
2646:Maurer--Cartan class of Theorem~\ref{thm:universal-theta} is
2659: (Theorem~\ref{thm:universal-theta}):
2707:and~\ref{thm:universal-theta}).
2801:Theorem~\ref{thm:universal-theta}, made unconditional by
2820:Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
3571:\label{thm:universal-theta}
3646:Theorem~\ref{thm:universal-theta} extends the canonical twisting
4999:The proof of Theorem~\ref{thm:universal-theta} assembles:
5533:Theorem~\ref{thm:universal-theta}. Then:
8132:In particular, Theorem~\ref{thm:universal-theta}
8190:Theorem~\textup{\ref{thm:universal-theta}} with the stated scalar
8227: $\Theta_{\cA}$ of Theorem~\ref{thm:universal-theta};
8240:modular-operadic clutching identities. Theorem~\ref{thm:universal-theta}
8250:$\Theta_{\cA}$ (Theorems~\ref{thm:universal-theta}
10059:Theorem~\textup{\ref{thm:universal-theta}} \textup{(MC2)} holds
10127:(Theorem~\ref{thm:universal-theta}) is established
14298:(Theorem~\ref{thm:universal-theta}). By


thinking
**Evaluating theorem references**

I need to check the theorem `thm:mc2-bar-intrinsic` to see if it's circular with `thm:universal-theta`. I'll search for references in the proof of `thm:mc2-bar-intrinsic`. It seems I should audit whether the MC equation is defined before it's invoked in proofs. There's a remark about "two MC equations" and references to theorem 3770. The MC equation isn't formally given until theorem 3770. If the user asks about the definition, I can clarify it was first written inline, not as a formal definition.
thinking
**Examining theorem definitions**

I’m looking into theorem 3770, which proves existence, and I'm considering whether it should be defined as a theorem or not. A definition could introduce notation that assumes a later theorem. If existence is tautological from \(D^2=0\), maybe I can define it earlier, around `thm:bar-modular-operad`. I need to inspect definitions like `Defcyc^{\mathrm{mod}}(\cA)` and `\gAmod` in relation to the shadow tower. Checking if proofs use \(\cA^{sh}\) before it's defined is also essential, especially concerning any local definitions.
exec
/bin/zsh -lc "rg -n -F \"{\\gAmod}"'^{E_1}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "E_1-framed" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "mathfrak{g}''^{'"\\mathrm{mod}}\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
3837:\MC({\gAmod}^{E_1})$ is Theorem~\ref{thm:e1-mc-element} in
exec
/bin/zsh -lc "rg -n -F \"coinvariant\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4347:\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_\cA)$
10166:$\Theta_{\cA} \in \operatorname{MC}(\mathfrak{g}^{\mathrm{mod}}_{\cA})$,
11437:$\mathfrak{g}^{\mathrm{mod}}_\cA$
 exited 1 in 52ms:

 succeeded in 51ms:
3596:In this chapter, it is the coinvariant/symmetric MC2 statement; the
3798:coinvariant modular convolution algebra.
3801:\item \emph{Maurer--Cartan on the coinvariant algebra\/~$\gAmod$.}
3826:argument. The universal MC element on the coinvariant modular
3831:\index{MC2!coinvariant scope}
3832:Theorem~\ref{thm:mc2-bar-intrinsic} is the symmetric/coinvariant MC2
3968:\item \emph{$\Theta_\cA$ lies in the completed coinvariant algebra.}
4244:Theorem~\ref{thm:mc2-bar-intrinsic} resolves the coinvariant MC2
14847:\begin{remark}[The five theorems as coinvariant shadows of the $E_1$ theory]
14850:Each row of the table above is the $\Sigma_n$-coinvariant
16145:representation, so the coinvariant space
22970:$E_1$ data discarded by the coinvariant projection
23012:For the ordered $E_1$-to-coinvariant projection
23063:At degree~$n$, the kernel of the coinvariant projection
31382:\label{prop:planar-forest-coinvariant}
31383:\index{planar planted forest!coinvariant quotient}
31388:\label{eq:planar-forest-coinvariant}
31393:which is the $\Sigma$-coinvariant quotient: at each vertex with
31408:The coinvariant identification holds because
31410:setting, and the coinvariant quotient divides by exactly this

thinking
**Checking macro definitions**

It looks like the only occurrence of `{\gAmod}^{E_1}` is at 3837, so I need to verify if the `\gAmod` macro is defined earlier in the document. It could be a macro, but mathematically, the object is defined at 10174. However, line 39 references it before the definition, which raises questions. I might need to inspect the context around 11437 or 4347 to get a clearer picture of how it’s being used.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '11420,11450p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4338,4352p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"ClaimStatus\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 11420	\operatorname{End}_{\mathrm{Ch}_\infty}\!(A^{\mathrm{ch}}_\infty)
 11421	\Bigr)
 11422	\end{equation}
 11423	\cite[Theorem~5.1]{RNW19}, \cite[Theorem~2.1]{Val16},
 11424	with strict chart
 11425	\begin{equation}\label{eq:convstr-log}
 11426	\mathfrak{g}^{\mathrm{mod},\log}_{\cA}(\mathfrak{U})
 11427	\;:=\;
 11428	\Convstr\!\Bigl(
 11429	\cC^{\log\mathrm{FM}}_{\mathrm{mod}},\,
 11430	\operatorname{End}_{\mathrm{Ch}_\infty}\!(A^{\mathrm{ch}}_\infty)
 11431	\Bigr).
 11432	\end{equation}
 11433	The one-slot convention
 11434	(Corollary~\ref{cor:strictification-comparison}(vi)) fixes the
 11435	geometric cooperad; the chiral input varies by $\infty$-morphism.
 11436	The coderivation algebra
 11437	$\mathfrak{g}^{\mathrm{mod}}_\cA$
 11438	(Definition~\ref{def:modular-convolution-dg-lie}) is the bar-side
 11439	realisation with classical moduli coefficients
 succeeded in 52ms:
  4338	\label{rem:non-circular-logical-chain}
  4339	\index{logical foundation!non-circular chain}
  4340	The bar-intrinsic construction partitions the five main
  4341	theorems into two tiers by logical prerequisites.
  4342	
  4343	\smallskip\noindent
  4344	\emph{Tier~1: unconditional consequences of~$D_\cA^2 = 0$.}
  4345	The MC element
  4346	$\Theta_\cA := D_\cA - \dzero \in
  4347	\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}}_\cA)$
  4348	exists at all genera by Theorem~\ref{thm:mc2-bar-intrinsic},
  4349	with no Koszulity hypothesis beyond the existence of the
  4350	genus-completed bar differential~$D_\cA$. The following are
  4351	projections of this single element and require no additional
  4352	input:
 succeeded in 52ms:
236:\begin{proposition}[MCG-equivariance of the genus tower; \ClaimStatusProvedHere]
324:\begin{theorem}[Genus-graded Koszul duality; \ClaimStatusProvedHere]
355:\begin{lemma}[Genus-graded Koszul complex resolution; \ClaimStatusProvedHere]
686:\begin{proposition}[Free-field examples are modular pre-Koszul; \ClaimStatusProvedHere]
728:\begin{proposition}[Kac--Moody, Virasoro, and $\mathcal{W}$-algebras are modular Koszul; \ClaimStatusProvedHere]
770:\begin{theorem}[PBW concentration at all genera for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
913: \texorpdfstring{$\fg$}{g}-modules; \ClaimStatusProvedHere]
972: \texorpdfstring{$H^1(\fg,-)$}{H1(g,-)}; \ClaimStatusProvedHere]
1020:\begin{theorem}[PBW degeneration at genus~\texorpdfstring{$1$}{1} for Kac--Moody; \ClaimStatusProvedHere]
1338:\begin{corollary}[Unconditional modular Koszulity at genus~\texorpdfstring{$1$}{1}; \ClaimStatusProvedHere]
1363:\begin{theorem}[PBW degeneration at all genera for Kac--Moody; \ClaimStatusProvedHere]
1571:\begin{corollary}[Unconditional modular Koszulity for Kac--Moody; \ClaimStatusProvedHere]
1623:\begin{theorem}[PBW degeneration at all genera for Virasoro; \ClaimStatusProvedHere]
1723:\begin{corollary}[Unconditional modular Koszulity for Virasoro; \ClaimStatusProvedHere]
1773:\begin{corollary}[Unconditional modular Koszulity for principal finite-type \texorpdfstring{$\mathcal{W}$}{W}-algebras; \ClaimStatusProvedHere]
1835: algebras with conformal vector; \ClaimStatusProvedHere]
1996: \ClaimStatusProvedHere]
2089: \ClaimStatusProvedHere]\label{thm:pbw-propagation}
2248: \ClaimStatusProvedHere]\label{prop:collision-locality}
2335: \ClaimStatusProvedHere]\label{thm:three-tier-architecture}

thinking
**Inspecting shadow extraction**

I think I should take a closer look at the lines surrounding theorem 4404 to see how they relate to shadow extraction and define projections. It seems like this could be significant! I'll also search specifically for "shadow extraction" around the reference of 4289 to gather more information. This could potentially provide clarity or insights that I might be missing right now, so I want to make sure I'm thorough in my investigation!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4400,4475p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14740,14825p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '4288,4336p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4400	No step invokes the conclusion of a later step as input.
  4401	\end{remark}
  4402	
  4403	\begin{proposition}[Functoriality of the bar-intrinsic MC element;
  4404	\ClaimStatusProvedHere]
  4405	\label{prop:mc2-functoriality}
  4406	\index{MC2!functoriality|textbf}
  4407	\index{universal Maurer--Cartan class!functoriality}
  4408	The assignment $\cA \mapsto \Theta_\cA$ is functorial:
  4409	for every morphism $f\colon \cA \to \cB$ of modular Koszul
  4410	chiral algebras that is compatible with the augmentations,
  4411	invariant forms, and genus towers
  4412	\textup{(}i.e., a morphism of
  4413	$(\mathrm{D1})$--$(\mathrm{D6})$ data in
  4414	Definition~\textup{\ref{def:modular-koszul-chiral})}, the
  4415	induced map on convolution algebras
  4416	\begin{equation}\label{eq:mc2-functoriality}
  4417	f_*\colon
  4418	\mathfrak{g}_\cA^{\mathrm{mod}}
  4419	\;\longrightarrow\;
 succeeded in 51ms:
 14740	derived intersection of the two Lagrangians is identified with the
 14741	corresponding shifted critical locus.
 14742	\end{proof}
 14743	
 14744	\begin{remark}[The unifying principle]
 14745	\label{rem:unifying-principle}
 14746	\index{unifying principle|textbf}
 14747	\index{shadow obstruction tower!as primary object}
 14748	The \emph{shadow obstruction tower}
 14749	$\Theta_\cA^{\leq 2},\, \Theta_\cA^{\leq 3},\,
 14750	\Theta_\cA^{\leq 4},\, \ldots$
 14751	in the modular convolution algebra
 14752	$\mathfrak{g}_{\cA}^{\mathrm{mod}}$ is the
 14753	organizing structure from which all five main theorems, the
 14754	nonlinear shadow calculus, and the genus expansion descend.
 14755	Each finite truncation $\Theta_\cA^{\leq r}$ is \emph{proved}
 14756	constructively; the all-degree limit
 14757	$\Theta_\cA = \varprojlim_r \Theta_\cA^{\leq r}$ exists by the
 14758	bar-intrinsic construction
 14759	\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
 succeeded in 50ms:
  4288	
  4289	\begin{corollary}[Shadow extraction; \ClaimStatusProvedHere]
  4290	\label{cor:shadow-extraction}
  4291	\index{shadow extraction|textbf}
  4292	\index{universal Maurer--Cartan class!shadow extraction}
  4293	The bar-intrinsic MC element $\Theta_\cA$ of
  4294	Theorem~\textup{\ref{thm:mc2-bar-intrinsic}} has natural
  4295	projections recovering all named modular invariants:
  4296	\begin{enumerate}[label=\textup{(\roman*)}]
  4297	\item \emph{Scalar shadow:}
  4298	 $\pi_{\mathrm{sc}}(\Theta_\cA)
  4299	 = \sum_{g \geq 1} \kappa(\cA)\,\lambda_g$
  4300	 \textup{(}Theorem~D; uniform-weight; unconditional at $g{=}1$\textup{)}.
  4301	\item \emph{Spectral shadow:}
  4302	 $\pi_{\mathrm{br}}(\Theta_\cA) = T_{\mathrm{br},\cA}$,
  4303	 so $\Delta_\cA(x) = \det(1 - x\, T_{\mathrm{br},\cA})$
  4304	 whenever the spectral branch object exists
  4305	 \textup{(}Theorem~\textup{\ref{thm:spectral-characteristic}}\textup{)}.
  4306	\item \emph{Quartic shadow:}
  4307	 $\pi_4(\Theta_\cA)


thinking
**Evaluating modular chiral algebra**

I see there’s a definition for modular chiral algebra structure at 14795, specifically mentioning a Maurer-Cartan element in g^mod. The MC equation is formally stated there, which is nice. However, it defines this structure broadly without specifically mentioning the bar-intrinsic Theta_A, which isn't introduced until 3770. I might need to explore the shadow obstruction tower at 12229 and the remark at 14747 for clarity, as well as checking for possible contradictions in those definitions.
thinking
**Identifying object conflation**

I realize that \(\Theta^{\le2}\) should be a truncated MC element rather than a scalar. Equating the truncated MC element with a scalar invariant feels sloppy and indicates some object conflation. This is likely significant. In a figure caption at line 12440, it states each level \(\Theta^{≤r}\) is an MC element in a quotient, but earlier bullets at line 12265 conflate it with its scalar projection. I think I need to revise those lines to clarify this foundation issue and search for other possible conflations.
codex
A second-order issue surfaced: the file sometimes collapses the truncated MC element itself into its scalar projection, writing `\Theta^{\leq 2} = \kappa`. That is an object-level conflation, not just loose exposition, so I’m tracing every repeated occurrence before I finalize findings.
exec
/bin/zsh -lc "rg -n -F \"\\Theta_{\\cA}"'^{'"\\leq 2} = \\kappa\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\Theta_\\cA"'^{'"\\leq 2} = \\kappa\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"scalar level~\\Theta_{\\cA}"'^{'"\\leq 2} = \\kappa(\\cA)\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\Theta"'^{'"\\leq 2}\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
12265:\item $\Theta_{\cA}^{\leq 2} = \kappa(\cA)$
14817:level~$\Theta_{\cA}^{\leq 2} = \kappa(\cA)$ of the
14977:The unique solution is $\Theta_{\cA}^{\leq 2} = \kappa(\cA)$, the
 succeeded in 51ms:
29698:$\Theta_\cA^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
29742:$\Theta_\cA^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 exited 1 in 51ms:

 succeeded in 50ms:
3902: font=\tiny] at (-0.2,-2.4) {$\Theta^{\leq 2}\!:\,\kappa$};
12380: (L2) at (0,0) {$\Theta^{\leq 2}\!:\; \kappa(\cA)$};
14983:(D\Theta^{\leq 2} + \tfrac12[\Theta^{\leq 2},\Theta^{\leq 2}])_3$.
15404: = -h\bigl(\ell_3^{(0)}(\Theta^{\leq 2},
15405: \Theta^{\leq 2}, \Theta^{\leq 2})\bigr)$,
15438:= -h\bigl(\ell_3^{(0)}(\Theta^{\leq 2},\,
15439:\Theta^{\leq 2},\, \Theta^{\leq 2})\bigr).
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14968,14992p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '29688,29750p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 14968	
 14969	\smallskip
 14970	\noindent\textbf{Input}: a cyclic chiral algebra~$\cA$ with cyclic
 14971	deformation complex $\Defcyc(\cA)$, Hessian~$H_{\cA}$,
 14972	propagator~$P_{\cA}$.
 14973	
 14974	\smallskip
 14975	\noindent\textbf{Step~1} (Degree~$2$).
 14976	Solve the Maurer--Cartan equation at weight~$2$.
 14977	The unique solution is $\Theta_{\cA}^{\leq 2} = \kappa(\cA)$, the
 14978	modular characteristic (Theorem~D).
 14979	
 14980	\smallskip
 14981	\noindent\textbf{Step~2} (Degree~$3$).
 14982	Compute the obstruction $o_3(\cA) =
 14983	(D\Theta^{\leq 2} + \tfrac12[\Theta^{\leq 2},\Theta^{\leq 2}])_3$.
 14984	If $[o_3] = 0$ in $H^2(\cA^{\mathrm{sh}}_{3,0})$, the cubic shadow
 14985	$\mathfrak{C}(\cA) = 0$ (Gaussian archetype: Heisenberg).
 14986	If $[o_3] \neq 0$, define
 14987	$\Theta_{\cA}^{\leq 3} = \Theta_{\cA}^{\leq 2}
 succeeded in 51ms:
 29688	\item The Polyakov formula
 29689	\begin{equation}\label{eq:polyakov-formula}
 29690	 \log \frac{\det'{}_\zeta \Delta_{g_1}}{\det'{}_\zeta \Delta_{g_0}}
 29691	 \;=\;
 29692	 -\,\frac{\kappa}{6\pi}
 29693	 \int_{\Sigma_g}
 29694	 \bigl(|\nabla \sigma|^2 + R_{g_0}\,\sigma\bigr)\,
 29695	 d\mu_{g_0}
 29696	\end{equation}
 29697	is the evaluation of the degree-$2$ shadow
 29698	$\Theta_\cA^{\leq 2} = \kappa \cdot \eta \otimes \Lambda$
 29699	\textup{(}where $\eta$ is the cyclic pairing and $\Lambda$ the
 29700	modular graph class\textup{)} against the conformal
 29701	deformation~$\sigma$.
 29702	
 29703	\item The coefficient $\kappa/(6\pi)$ involves the modular
 29704	characteristic, \emph{not} the central charge: $\kappa/(6\pi)
 29705	\neq c/(6\pi)$ in general. The classical Polyakov coefficient
 29706	$1/(6\pi)$ for a single scalar field arises only for the
 29707	Heisenberg algebra at level $\kappa = 1$, where



thinking
**Searching for earlier proofs**

I need to find proofs that are earlier than line 12229, specifically searching for early uses in claims. There are many examples, like theorem 3570. It looks like line 10160 actually appears before 12229, with some reference to a convolution dg Lie algebra and its shadow obstruction tower. I should check for unresolved references and consider running a latex reference checker or a targeted build. The user asked about unresolved references, which may be crucial for the audit.
thinking
**Considering build options**

I’m thinking about whether I could run latexmk, but it seems like it might be enormous and expensive in terms of resources. Maybe using the build-surface skill would be a better option? The user did ask for a foundation audit, and if a build is possible, I could consider narrowing it down to a specific file. However, that might be tough since the whole document is included. So I’ll have to weigh the options carefully!
thinking
**Evaluating foundation labels**

I think I need to ground my thoughts a bit more. It seems I'm considering what to use for foundation labels. Is that the right approach? There could be options here, and I want to ensure I’m not missing anything important in this process. I'll have to take a closer look at various factors before making a decision, to make sure my choices align well with the goals I have in mind.
codex
I’ve moved from ordering to dependency integrity. The next pass is mechanical: every foundational label named in the opening block gets checked against the live tree so I can separate “defined later” from “not actually anchored.”
exec
/bin/zsh -lc "for label in def:modular-characteristic-package thm:bar-modular-operad thm:higher-genus-inversion thm:mc2-bar-intrinsic subsec:two-level-convention def:shadow-algebra def:modular-bar-hamiltonian def:shadow-postnikov-tower prop:master-equation-from-mc thm:recursive-existence thm:single-line-dichotomy prop:depth-gap-trichotomy thm:shadow-formality-identification thm:quantum-complementarity-main constr:dk-shadow-projections prop:e1-shadow-r-matrix thm:gz26-commuting-differentials thm:gaudin-yangian-identification thm:e1-mc-element; do rg -n -F \"\\\\label{"'$label}" chapters appendices metadata CLAUDE.md 2>/dev/null || echo "MISSING $label"; done' in /Users/raeez/chiral-bar-cobar succeeded in 87ms:
chapters/examples/yangians_drinfeld_kohno.tex:96:\label{constr:dk-shadow-projections}
chapters/theory/e1_modular_koszul.tex:767:\label{prop:e1-shadow-r-matrix}
chapters/connections/frontier_modular_holography_platonic.tex:1525:\label{thm:gz26-commuting-differentials}
chapters/connections/frontier_modular_holography_platonic.tex:1631:\label{thm:gaudin-yangian-identification}
chapters/theory/e1_modular_koszul.tex:291:\label{thm:e1-mc-element}

thinking
**Searching for definitions**

I’m thinking about whether I'm okay with the definition of the genus-g component. It might not be a finding, but I need to check if there’s a formal definition for `\Theta_A^{(g)}`. The theorem 3770 defines a sum but doesn't seem to state the notation `\Theta^{(g)}` explicitly until later, so I'll want to look for its definition and clarify that aspect. There's definitely something to consider here!
exec
/bin/zsh -lc "rg -n -F \"Theta_\\cA"'^{(g)}" chapters/theory/higher_genus_modular_koszul.tex | sed -n '"'1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
251:$\Theta_\cA^{(g)} \in
257:amplitude $Z_g(\cA) = \operatorname{Tr}^{\circ g}(\Theta_\cA^{(g)})$
297:$\Theta_\cA^{(g)} = d_\cA^{(g)} \in
310:\operatorname{Tr}^{\circ g}(\Theta_\cA^{(g)})$ is obtained
3664:\Theta_\cA^{(g)}
3669:$\Theta_\cA^{(g)}$ is the genus-$g$ component of the universal MC
14295:$\Theta_\cA^{(g)}$ is the genus-$g$ obstruction
14300:$\Theta_\cA^{(g)} =
14408:$F_g(\cA) = \operatorname{tr}_{\mathrm{cyc}}(\Theta_\cA^{(g)})$
31873:$\Theta_\cA = \sum_{g \geq 0} \hbar^g\,\Theta_\cA^{(g)}$
31880:For each $g \geq 1$, the genus-$g$ component $\Theta_\cA^{(g)}$

thinking
**Inspecting definitions and order issues**

I think the statement might have been defined at 3669, but it was used much earlier in proposition 236. There seems to be an order issue I've noticed. I should check if line 31873 includes a sum from g ≥ 0, as the earlier Θ starts at g ≥ 1. This could definitely be an issue. I really need to take a closer look around line 31868 to clarify things!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31868,31890p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14288,14308p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31868	
 31869	The bar-intrinsic construction
 31870	(Theorem~\ref{thm:mc2-bar-intrinsic})
 31871	gives $\Theta_\cA$ at all genera simultaneously.
 31872	The genus expansion
 31873	$\Theta_\cA = \sum_{g \geq 0} \hbar^g\,\Theta_\cA^{(g)}$
 31874	decomposes the Maurer--Cartan equation genus by genus.
 31875	
 31876	\begin{theorem}[Inductive genus determination;
 31877	\ClaimStatusProvedHere]
 31878	\label{thm:inductive-genus-determination}
 31879	\index{genus determination!inductive|textbf}
 31880	For each $g \geq 1$, the genus-$g$ component $\Theta_\cA^{(g)}$
 31881	is the unique solution of
 31882	\begin{equation}\label{eq:genus-g-mc}
 31883	d_{\Theta^{(0)}}\bigl(\Theta^{(g)}\bigr)
 31884	\;=\;
 31885	-\mathrm{Ob}_g\bigl(\Theta^{(<g)}\bigr),
 31886	\end{equation}
 31887	where $d_{\Theta^{(0)}} := d_0 + [\Theta^{(0)},\, -]$ is the
 succeeded in 50ms:
 14288	 and the monodromy of $\nabla_\cA$ furnishes the
 14289	 bar-side comparison surface for the KZ/Hitchin package.
 14290	\end{enumerate}
 14291	\end{theorem}
 14292	
 14293	\begin{proof}
 14294	(i)~On the proved uniform-weight scalar lane, the cyclic trace of
 14295	$\Theta_\cA^{(g)}$ is the genus-$g$ obstruction
 14296	$\operatorname{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ by
 14297	Theorem~D
 14298	(Theorem~\ref{thm:universal-theta}). By
 14299	Theorem~\ref{thm:primitive-to-global-reconstruction},
 14300	$\Theta_\cA^{(g)} =
 14301	\operatorname{FT}^{\log}_{\mathrm{mod}}(\mathfrak{K}_\cA)^{(g)}$,
 14302	so $F_g = \operatorname{tr}_{\mathrm{cyc}}
 14303	(\operatorname{FT}^{\log}_{\mathrm{mod}}(\mathfrak{K}_\cA)^{(g)})
 14304	= \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}$.
 14305	
 14306	(ii)~This is Corollary~\ref{cor:free-energy-ahat-genus},
 14307	now seen as a consequence of (i) via the family index theorem

thinking
**Investigating theorems consistency**

I'm noticing a potential inconsistency with Theta terms. At 31873, the sum of Theta^{(g)} is non-negative, but earlier claims only consider positive genus. Could Theta^{(0)} be non-zero? The theorem states Theta = D - d0; if Theta^{(0)} isn't zero, this would create a contradiction with line 31887 defining d_{Theta^{(0)}}. I really need to examine the theorem around 31876 for clarity. Maybe Theta^{(0)} involves the tree-level MC element or something related to bar-cobar twisting? So, I'll dig deeper into the context!
codex
A more serious structural inconsistency is emerging around genus indexing: one section treats `\Theta_\cA` as the positive-genus correction `\sum_{g\ge1}\hbar^g d^{(g)}`, while another expands it from `g=0` and then uses a nonzero `\Theta^{(0)}` to twist the differential. I’m reading that block in context before deciding severity, because that can corrupt every later recursion formula.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31876,31940p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31876	\begin{theorem}[Inductive genus determination;
 31877	\ClaimStatusProvedHere]
 31878	\label{thm:inductive-genus-determination}
 31879	\index{genus determination!inductive|textbf}
 31880	For each $g \geq 1$, the genus-$g$ component $\Theta_\cA^{(g)}$
 31881	is the unique solution of
 31882	\begin{equation}\label{eq:genus-g-mc}
 31883	d_{\Theta^{(0)}}\bigl(\Theta^{(g)}\bigr)
 31884	\;=\;
 31885	-\mathrm{Ob}_g\bigl(\Theta^{(<g)}\bigr),
 31886	\end{equation}
 31887	where $d_{\Theta^{(0)}} := d_0 + [\Theta^{(0)},\, -]$ is the
 31888	tree-twisted differential and the genus-$g$ obstruction class is
 31889	\begin{equation}\label{eq:genus-obstruction}
 31890	\mathrm{Ob}_g\bigl(\Theta^{(<g)}\bigr)
 31891	\;:=\;
 31892	\sum_{\substack{g_1 + g_2 = g\\g_1,g_2 \geq 1}}
 31893	\tfrac{1}{2}[\Theta^{(g_1)},\, \Theta^{(g_2)}]
 31894	\;+\;
 31895	\Delta\bigl(\Theta^{(g-1)}\bigr)

thinking
**Verifying algebra concepts**

I'm questioning whether the definition of ambient algebra matches expectations. It seems like I need to inspect specific lines closely, particularly around 30260 and 31606, since there are potentially conflicting definitions regarding shadow tower and modular convolution algebra. The user is asking about certain variables, and I realize there’s some inconsistency in how different notations are used throughout the text. I need to clarify these definitions and search for "ambient-modular-complementarity-algebra" to get it right.
exec
/bin/zsh -lc 'rg -n -F "def:ambient-modular-complementarity-algebra" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "g''^{'"\\mathrm{amb}}\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30240,30320p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
31092:\label{def:ambient-modular-complementarity-algebra}
31324:Definition~\textup{\ref{def:ambient-modular-complementarity-algebra}}
31607:Definition~\textup{\ref{def:ambient-modular-complementarity-algebra}}
31653:\textup{(}Definition~\textup{\ref{def:ambient-modular-complementarity-algebra})},
 succeeded in 51ms:

 succeeded in 52ms:
 30240	
 30241	\subsubsection{The single master object}
 30242	
 30243	\begin{construction}[Shadow extraction maps]
 30244	\label{constr:shadow-extraction-explicit}
 30245	\ClaimStatusProvedHere
 30246	\index{shadow extraction!explicit maps|textbf}
 30247	\index{Chriss--Ginzburg principle!shadow extraction}
 30248	For each degree $r \geq 2$ and genus $g \geq 0$, the
 30249	\emph{shadow extraction map}
 30250	\begin{equation}\label{eq:shadow-extraction-map}
 30251	\pi_{r,g} \colon \gAmod
 30252	\longrightarrow
 30253	\operatorname{Hom}_{\Sigma_r}\!\bigl(
 30254	C_*(\overline{\mathcal{M}}_{g,r}),\;
 30255	\operatorname{End}_\cA(r)
 30256	\bigr)
 30257	\end{equation}
 30258	is the projection to the $(g,r)$-bigraded component of the
 30259	modular convolution algebra

thinking
**Exploring definitions**

I need to check the definition of ambient to see how it relates to my current thinking. It might also be enough to point out the inconsistency I noticed between using ambient and modular convolution algebras for the tower. But maybe this can be resolved later through some equivalence. I should also read around 31092, just to gather more information. Let’s see how that goes!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31088,31130p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31088	The graph sum~\eqref{eq:modular-bar-hamiltonian} lives in a specific
 31089	graded vector space.
 31090	
 31091	\begin{definition}[Ambient modular complementarity algebra]
 31092	\label{def:ambient-modular-complementarity-algebra}
 31093	The \emph{carrier} for the modular bar--Hamiltonian is the filtered
 31094	completed graded vector space
 31095	\begin{equation}
 31096	\label{eq:ambient-modular-complementarity-algebra}
 31097	\mathfrak{g}^{\mathrm{amb}}_{\cA}
 31098	:=
 31099	\bigl(L_{\cA} \oplus K_{\cA} \oplus L_{\cA^!}\bigr)
 31100	\widehat\otimes \mathbb{G}_{\mathrm{st}}
 31101	\widehat\otimes \mathbb{G}_{\mathrm{pf}},
 31102	\end{equation}
 31103	where $L_{\cA} := \operatorname{Def}_{\mathrm{cyc}}(\cA)$,
 31104	$K_{\cA} := (\cA^!\widehat\otimes\cA)[1]$,
 31105	$\mathbb{G}_{\mathrm{st}}$ is the completed stable-graph coefficient
 31106	algebra (connected stable graphs with genus/leg labels), and
 31107	$\mathbb{G}_{\mathrm{pf}}$ is the planted-forest coefficient algebra

thinking
**Exploring ambient algebra**

I'm noticing that ambient algebra seems distinct in this context. I need to consider if the tower defined within it makes the statement involving g^mod inconsistent. But maybe there’s a connection later between g^amb and g^mod? I want to search for the relation, particularly looking into `\mathfrak{g}^{\mathrm{amb}}_\cA \cong` and also explore the differences between `carrier` and `strict model`. I'll dig deeper to clarify these ideas!
exec
/bin/zsh -lc "rg -n -F \"\\mathfrak{g}"'^{'"\\mathrm{amb}}_\\cA\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
31058:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
31323:$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
31595:\mathfrak{g}^{\mathrm{amb}}_\cA.

thinking
**Inspecting algebra definitions**

I’m noticing that the statement about the tower at 12245 is calling for a solution using ambient algebra quotient, but then it refers to the tower in \gAmod, which seems inconsistent. I think I should check the definition of the extension-tower around the 121xx area to figure out the type of algebra being used. There’s definitely something worth investigating further here!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12190,12232p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 12190	The stability condition $2g - 2 + n > 0$ ensures $w \geq 1$.
 12191	The \emph{weight filtration} is the descending filtration
 12192	\[
 12193	F^N\mathfrak{g}^{\mathrm{amb}}_{\cA}
 12194	\;:=\;
 12195	\bigl\{\varphi \in \mathfrak{g}^{\mathrm{amb}}_{\cA}
 12196	\;:\; \varphi_{g,r;d} = 0 \;\text{for all}\;
 12197	(g,r,d) \;\text{with}\; w(g,r,d) < N\bigr\}.
 12198	\]
 12199	This filtration is \emph{exhaustive}
 12200	($\mathfrak{g}^{\mathrm{amb}} = F^1$),
 12201	\emph{separated}
 12202	($\bigcap_{N} F^N = 0$),
 12203	\emph{complete} (the completion
 12204	$\widehat{\mathfrak{g}}^{\mathrm{amb}}
 12205	= \varprojlim_N \mathfrak{g}^{\mathrm{amb}}/F^{N+1}$
 12206	equals the product of weight-$w$ components), and
 12207	\emph{pronilpotent}
 12208	($[F^{N_1}, F^{N_2}] \subseteq F^{N_1 + N_2 - 2}$;
 12209	the shift $-2$ is from degree reduction upon gluing two

thinking
**Assessing algebraic structures**

I'm realizing that the tower is defined in ambient algebra, but there's a reference to it being related to modular convolution algebra as indicated by 14748. I need to dig deeper into this. Could it be that the ambient algebra is later tied to the modular one? I should look for specific identifications between them. I wonder if the term "ambient" might serve as a carrier for the bar-Hamiltonian, though they aren’t the same. It seems crucial to find direct equivalences.
exec
/bin/zsh -lc 'rg -n -F "g''^{'"\\mathrm{amb}}_\\cA\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc "rg -n -F \"amb}}_\\cA\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
31058:\item \emph{Koszul duality}: twisting the ambient algebra $\mathfrak{g}^{\mathrm{amb}}_\cA$ by the scalar MC data gives the bar complex $\barB(\cA)$ as a twisted differential;
31323:$\mathfrak{g}^{\mathrm{amb}}_\cA$ of
31595:\mathfrak{g}^{\mathrm{amb}}_\cA.
exec
/bin/zsh -lc "rg -n \"ambient.*convolution|convolution.*ambient|g\\"'^'"\\{amb\\}.*g\\"'^'"\\{mod\\}|g\\"'^'"\\{mod\\}.*g\\"'^'"\\{amb\\}|ambient algebra.*modular convolution\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Inspecting graph-sum formula**

I don’t see any obvious issues with identification, so I think it’s a good finding. I need to check if `def:modular-bar-hamiltonian` at 30889 defines the graph-sum formula correctly. The opening line mentions that it computes Theta^{≤r} as a sum over connected cross-polarized stable graphs of weight at most r, but I’m wondering if the actual definition differs—like if it includes the full ambient bar-Hamiltonian rather than just truncations. I need to inspect this further.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30884,30935p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 30884	The following graph sum realizes
 30885	each truncation $\Theta_\cA^{\leq r}$ as a sum over
 30886	cross-polarized stable graphs of weight at most~$r$.
 30887	
 30888	\begin{definition}[The modular bar--Hamiltonian]
 30889	\label{def:modular-bar-hamiltonian}
 30890	Let $\cA$ be a cyclic chiral algebra with Koszul dual $\cA^!$,
 30891	cyclic minimal models $(V_{\cA}, \ell_n^{\mathrm{tr}})$ and
 30892	$(V_{\cA^!}, \ell_n^{!\,\mathrm{tr}})$, Hessian
 30893	$H_{\cA}\colon V_{\cA} \xrightarrow{\sim} V_{\cA}^*[-1]$,
 30894	propagator $P_{\cA} := H_{\cA}^{-1}$, and universal twisting
 30895	kernel $\tau_{\cA} \in \operatorname{MC}(\cA^!\widehat\otimes\cA)$.
 30896	The \emph{modular bar--Hamiltonian} is the connected graph sum
 30897	\begin{equation}
 30898	\label{eq:modular-bar-hamiltonian}
 30899	\Theta_{\cA}
 30900	\;:=\;
 30901	\sum_{\substack{
 30902	\Gamma\;\text{connected}\\
 30903	\text{stable, cross-polarized}}}



thinking
**Examining definitions in mathematics**

I'm finding it interesting that the `def:modular-bar-hamiltonian` uses the \Theta_A notation to define Theta as a sum over connected graphs. It seems like this might be a consistent approach, though the object being defined comes up multiple times. Line 30899 defines full Theta instead of a truncation. I also noticed that there might be a need to check if `\gAmod` macro is used beforehand. It’s a lot to consider, but I'm keeping a close eye on everything!
thinking
**Analyzing class definitions in the theorem**

I think I should look for theorems or proofs before line 16542 that involve depth classes, which are defined later on. Lines 136-144 already reference these classes, so it might be okay, but there could be an actual theorem that uses G/L/C/M before their definitions. I'll need to search for instances of `\mathbf{G}` or `\mathsf{G}` before line 16542 in the theorems and propositions to ensure consistency. It’s crucial to clarify the definition placement or create a brief definition table for better structure.
thinking
**Identifying class discrepancies**

I’m noticing a subtlety regarding classes G/L/C/M defined in AGENTS, and later, the file introduces class W. This could create a contradiction that's quite critical. I need to pay attention to lines 16611-16615, as they introduce the fifth regime, `\mathbf{W}`, which conflicts with the earlier mention of only having one of the four classes. It’s essential that I clarify how these classes interact and ensure consistency in definitions throughout the document.
codex
The classification lane is now materially worse than a simple ordering problem. The same file gives four mutually exclusive shadow classes in the opening, then later reintroduces arbitrary finite depths and even a fifth class `W`; that is not just exposition drift, it changes the theorem’s content. I’m checking the imported `E_1` theorem next so I can distinguish “defined elsewhere and imported badly” from “not defined at all.”
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '270,330p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "g''^{E_1}" chapters/theory/e1_modular_koszul.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "g''^{'"\\mathrm{mod},E_1}\" chapters/theory/e1_modular_koszul.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "averaging sends" chapters/theory/e1_modular_koszul.tex chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   270	\;\twoheadrightarrow\;
   271	\gAmod,
   272	\qquad
   273	\operatorname{av}(\phi)(g,n)
   274	\;:=\;
   275	\frac{1}{n!}\sum_{\sigma \in \Sigma_n}
   276	\sigma \cdot
   277	\bigl(\phi(g,n) \circ \iota^{\mathrm{rib}}_{g,n}\bigr)
   278	\end{equation}
   279	takes external $\Sigma_n$-coinvariants after pullback along a choice
   280	of section $\iota^{\mathrm{rib}}_{g,n}\colon \cM_\Com(g,n) \to
   281	\cM_\Ass(g,n)$ of the ribbon-forgetting quotient
   282	(Theorem~\ref{thm:fcom-coinvariant-fass}). The result is
   283	$\Sigma_n$-invariant by construction and independent of the section
   284	up to boundary. The map $\operatorname{av}$ is a surjective dg~Lie
   285	morphism: the symmetrization converts $T^c$-convolution to
   286	$\mathrm{Sym}^c$-convolution, which is exactly the passage from ordered
   287	ribbon combinatorics to commutative modular combinatorics.
   288	\end{definition}
   289	
 succeeded in 52ms:
30:$\mathrm{av}\colon \fg^{E_1} \to \fg^{\mathrm{mod}}$ provably does
2185:& $Q_g^{E_1} + Q_g^{!,E_1}
 exited 1 in 51ms:

 succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:3838:Chapter~\ref{chap:e1-modular-koszul}, and averaging sends

thinking
**Inspecting definitions**

I need to check the `e1_modular_koszul` file, specifically lines 1 to 40, to look at the definitions of `fg^{E1}` and `fg^{mod}`. It seems like this section could give me clarity on these terms and how they're being used. I’m hoping I can find the information I need to understand the context and implications better. Alright, let's see what those definitions look like!
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	%% ════════════════════════════════════════════════════════════════════════
     2	%% E₁ MODULAR KOSZUL DUALITY
     3	%%
     4	%% The ordered (associative) parallel to the commutative modular
     5	%% Koszul theory. Extracted to a standalone chapter so that the
     6	%% E₁/E_∞ parallelism is architecturally visible.
     7	%% ════════════════════════════════════════════════════════════════════════
     8	
     9	\chapter{\texorpdfstring{$E_1$}{E1} Modular Koszul Duality}
    10	\label{chap:e1-modular-koszul}
    11	
    12	The scalar curvature $\kappa(\cA)$ is a single number: the
    13	$\Sigma_2$-coinvariant of a meromorphic function $r(z)$ that records
    14	the full spectral scattering of the algebra. The cubic shadow
    15	$\mathfrak{C}(\cA)$ is the $\Sigma_3$-coinvariant of the Drinfeld
    16	associator $\Phi_{\mathrm{KZ}}$. At every degree the $E_\infty$
    17	invariant is a scalar projection of an ordered object that carries
    18	strictly more information, and the data killed by the coinvariant
    19	projection is the associative factorization pattern governed by
    20	Stasheff associahedra rather than symmetric groups.
exec
/bin/zsh -lc "rg -n -F \"P_\\cA := H_\\cA"'^{-1}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F \"P_\\cA\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
66:by the complementarity propagator $P_\cA = H_\cA^{-1}$.
91: and edge contractions by $P_\cA = H_\cA^{-1}$.
3946: the propagator~$P_\cA$.
4494:complementarity propagator $P_\cA = H_\cA^{-1}$ is
4618:\bigotimes_{e \in E(\Gamma)} P_\cA$
11381:contract each internal edge with the cyclic kernel~$P_\cA$.
11497:complementarity propagator $P_\cA = H_\cA^{-1}$,
11805:P_\cA\circ \alpha\circ \delta^{\mathrm{ns}}\bigr).
13402: via the cyclic Verdier kernel $P_\cA$;
13443:P_\cA \;:=\; h,
13448:The propagator $P_\cA$ is unique up to filtered gauge equivalence:
13449:if $P_\cA'$ arises from a different cyclic retract, then
13450:$P_\cA - P_\cA'$ is exact in the filtered cyclic deformation complex.
14367: -P_\cA \circ \Delta_{\mathrm{ns}}(K_{0,3}^\cA),
14370: and $P_\cA$ as propagator. For Heisenberg
14382: -P_\cA \circ \Bigl(
14392: $\sum R_\rho(K_{0,2})$, each contracted with~$P_\cA$.
14396: contracted by~$P_\cA$, loops produced by
14415:from~$P_\cA$, and stratum weights from log-FM chains.
14432:$K_{1,1} = -P_\cA \circ \Delta_{\mathrm{ns}}(K_{0,3})$.


thinking
**Evaluating mathematical definitions**

I think theorem 3570 might be a redundant summary before the detailed proof. I need to check if the definition of `modular chiral algebra structure` at 14795 uses `\Theta_A` in the same way as the canonical bar-intrinsic universal class. This could be creating ambiguity with symbols. I should search for multiple definitions of Theta_A in various lines. The user asked about the formal definition of Theta_A, noting that there are competing definitions, which is crucial to clarify.
thinking
**Inspecting stable-graph decomposition**

I'm thinking about needing to inspect around 30512 for stable-graph decomposition. There’s probably a lot to consider here, such as what the specific requirements are or what kind of analysis will be involved. I want to ensure I’m clear on the objectives and what I need to look for. Let’s dive in and gather all relevant details to have a thorough understanding of this decomposition method.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '30508,30620p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 30508	%%-------------------------------------------------------------
 30509	
 30510	\subsubsection{The stable-graph decomposition}
 30511	
 30512	\begin{construction}[Stable-graph decomposition of $\Theta_\cA$]
 30513	\label{constr:stable-graph-decomposition}
 30514	\ClaimStatusProvedHere
 30515	\index{stable graph!decomposition of MC element|textbf}
 30516	\index{Chriss--Ginzburg principle!graph decomposition}
 30517	The master MC element decomposes as a weighted sum
 30518	over stable graphs.
 30519	For each pair $(g,n)$ with $2g - 2 + n > 0$, the
 30520	$(g,n)$-component is
 30521	\begin{equation}\label{eq:stable-graph-decomposition}
 30522	\Theta_\cA^{(g,n)}
 30523	\;=\;
 30524	\sum_{\Gamma \in \mathsf{Gr}^{\mathrm{st}}_{g,n}}
 30525	\frac{1}{|\operatorname{Aut}(\Gamma)|}
 30526	\cdot W_\Gamma(\cA),
 30527	\end{equation}

thinking
**Evaluating the theorem inconsistencies**

I'm noticing there are many constructions to consider. I need to check if theorem 30587 uses \gAmod in relation to the shadow tower defined in the ambient algebra at 12245. There's another inconsistency! The obstruction recursion theorem mentions F^{r+1}\gAmod quotient instead of ambient, suggesting that the file switches carriers. This indicates I need to choose one or prove a comparison, which could be very important. I should find the references to ensure consistency.
exec
/bin/zsh -lc 'rg -n -F "constr:obstruction-recursion" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4284:(Construction~\ref{constr:obstruction-recursion}).
10814:(Construction~\ref{constr:obstruction-recursion}). The $L_\infty$
11605:(Construction~\ref{constr:obstruction-recursion}) factorises by
11955:(Construction~\ref{constr:obstruction-recursion}). The scalar,
12051: (Construction~\ref{constr:obstruction-recursion});
12073:Construction~\ref{constr:obstruction-recursion},
12732:(Construction~\ref{constr:obstruction-recursion})
12984:\label{constr:obstruction-recursion}
13020: Construction~\textup{\ref{constr:obstruction-recursion}}
13092:Construction~\ref{constr:obstruction-recursion} vanishes for
14934:\textup{(}Construction~\textup{\ref{constr:obstruction-recursion}}):
14965:(Construction~\ref{constr:obstruction-recursion}) for a concrete
15243:(Construction~\ref{constr:obstruction-recursion})
15571:recursion (Construction~\ref{constr:obstruction-recursion}):
16549:Construction~\ref{constr:obstruction-recursion}.
25490:(Construction~\ref{constr:obstruction-recursion}).
26051:(Construction~\ref{constr:obstruction-recursion}) rather than
28534:(Construction~\ref{constr:obstruction-recursion}),
30883:(Construction~\ref{constr:obstruction-recursion}).
30975:extension tower (Construction~\ref{constr:obstruction-recursion}).
codex
The Maurer–Cartan equation itself is also not stable in notation: one part of the file correctly derives it from `[d_0,\Theta] + 1/2[\Theta,\Theta]=0`, while other parts write `D_\cA\Theta_\cA + 1/2[\Theta_\cA,\Theta_\cA]=0` even though `D_\cA` was already defined as the total bar differential `d_0+\Theta_\cA`. I’m tracing those collisions now, because that can turn tautologies into nonsense identities.
exec
/bin/zsh -lc "rg -n \"D_\\\\cA ?\\\\Theta_\\\\cA|D\\\\Theta_\\\\cA|D_\\\\cA\\\\Theta_\\\\cA|D\\\\Theta\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:D_\cA ?\Theta_\cA|D\Theta_\cA|D_\cA\Theta_\cA|D\Theta)
         ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F \"D_\\cA\\Theta_\\cA\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"[\\dzero, \\Theta_\\cA]\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"D\\Theta_\\cA\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"D_\\cA \\Theta_\\cA\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"D\\Theta\" chapters/theory/higher_genus_modular_koszul.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"d_0 \\Theta_\\cA\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
98: (D_\cA\Theta_\cA^{\leq r}
30605: := (D_\cA\Theta_\cA^{\leq r}
 succeeded in 51ms:
3612:= [\dzero, \Theta_\cA] + \tfrac12[\Theta_\cA,\Theta_\cA]$
4017:+ [\dzero, \Theta_\cA]
4023:[\dzero, \Theta_\cA]
4141:$[\dzero, \Theta_\cA] + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
13077:MC equation $[\dzero, \Theta_\cA]
13153: $[\dzero, \Theta_\cA]
 succeeded in 51ms:
10744:D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0,
11846:The MC equation $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA]
12020:Curvature & $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ \\
12145:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ by
22181:The MC equation $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA]
24900:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$,
24937:$(D\Theta_\cA)_{g,n}
25468:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
26095:The MC equation $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
 succeeded in 51ms:
3478:$D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$
3494:full MC equation $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$
10744:D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0,
11846:The MC equation $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA]
12020:Curvature & $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ \\
12145:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA] = 0$ by
13735:$D\Theta + \tfrac{1}{2}[\Theta, \Theta] = 0$
14983:(D\Theta^{\leq 2} + \tfrac12[\Theta^{\leq 2},\Theta^{\leq 2}])_3$.
14994:(D\Theta^{\leq 3} + \tfrac12[\Theta^{\leq 3},\Theta^{\leq 3}])_4$.
22181:The MC equation $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA,\Theta_\cA]
24900:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$,
24937:$(D\Theta_\cA)_{g,n}
25468:$D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
26095:The MC equation $D\Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
26321:$D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ at $(g,n)$
26341:$\bigl\{(D\Theta + \tfrac{1}{2}[\Theta,\Theta])_{g,n}\bigr\}_{r \to \infty}$
26440:$D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$
26451:D\Theta_g
26565:$D\Theta_3 + [\Theta_1,\Theta_2]
26895:the MC equation $D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ is
 succeeded in 50ms:
41: d_0 \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0
 succeeded in 51ms:
30303:$D_\cA \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
30566:$D_\cA \Theta_\cA + \tfrac{1}{2}[\Theta_\cA, \Theta_\cA] = 0$
30568:The linear term $D_\cA \Theta_\cA$ collects boundary
30598: $D_\cA \Theta_\cA^{\leq r}



thinking
**Reviewing notational issues**

I need to inspect line 12145 for context, particularly regarding the definition of D. It seems there might be a notational collision, where D could represent a differential in dg Lie algebra, while \(D_\cA\) refers to the total differential. Line 30303 uses \(D_\cA\), which feels wrong or ambiguous. I should cite lines 30303 and 30566, and ensure the derivations in 4017-4028 align with the initial definitions. It’s essential to clarify that D denotes the dg-Lie differential and not the total bar differential \(D_\cA\). This could be critical for the proof's integrity.
thinking
**Inspecting line 41 for completeness**

I need to check line 41 where it states \(d_0 \Theta_A + \frac{1}{2}[...] = 0\). It could be missing a bracket or commutator because, in dg Lie algebra, the equation should use \([d_0, \Theta]\) instead of the left composition \(d_0 \Theta\). Line 3612 uses the correct commutator, indicating line 41 needs precision. There’s also a question about whether omitting the \(\Theta d_0\) term leads to inconsistency. Overall, I note that the first displayed MC equation appears syntactically incomplete unless \(d_0\Theta\) is intended to represent a commutator, though it’s not defined.
thinking
**Inspecting definitions**

I need to check line 16618 in the remark class W to understand the non-Koszul boundary better. There might be a missing local definition for `\Theta_\cA^{(g)}` and `\Theta^{(0)}` in proposition 236 and theorem 31876. I'll search to see if `Theta^{(0)}` is defined anywhere. I think I should use rg for this task. It feels like there’s enough to consider here, but more clarity would help!
exec
/bin/zsh -lc "rg -n -F \"\\Theta"'^{(0)}" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
31883:d_{\Theta^{(0)}}\bigl(\Theta^{(g)}\bigr)
31887:where $d_{\Theta^{(0)}} := d_0 + [\Theta^{(0)},\, -]$ is the
31913:$H^*(\gAmod,\, d_{\Theta^{(0)}})$ for all~$g$, and
31925:d_0(\Theta^{(g)}) + [\Theta^{(0)}, \Theta^{(g)}]
31928:The left side is $d_{\Theta^{(0)}}(\Theta^{(g)})$.
31932:The ambiguity lies in $\ker(d_{\Theta^{(0)}}|_{\text{genus }g})$
31934:$(\gAmod, d_{\Theta^{(0)}})$.
31949:\Theta^{(0)} = \text{the $\mathrm{Ch}_\infty$-structure maps},
31950:\quad d_0\Theta^{(0)} + \tfrac{1}{2}[\Theta^{(0)},\Theta^{(0)}] = 0.
31953:d_{\Theta^{(0)}}(\Theta^{(1)})
31954:= -\Delta(\Theta^{(0)}) - d_{\mathrm{sew}}^{(1)},
31960:d_{\Theta^{(0)}}(\Theta^{(2)})
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '31940,31968p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 31940	$\Theta^{(g)} = (D_\cA - d_0)^{(g)}$ is the unique representative
 31941	characterised by the property $D_\cA^2 = 0$; it is the canonical
 31942	element selected by the differential rather than by a gauge choice.
 31943	\end{proof}
 31944	
 31945	\begin{corollary}[Base cases; \ClaimStatusProvedHere]
 31946	\label{cor:genus-base-cases}
 31947	\begin{align*}
 31948	g = 0{:}&\quad
 31949	\Theta^{(0)} = \text{the $\mathrm{Ch}_\infty$-structure maps},
 31950	\quad d_0\Theta^{(0)} + \tfrac{1}{2}[\Theta^{(0)},\Theta^{(0)}] = 0.
 31951	\\[4pt]
 31952	g = 1{:}&\quad
 31953	d_{\Theta^{(0)}}(\Theta^{(1)})
 31954	= -\Delta(\Theta^{(0)}) - d_{\mathrm{sew}}^{(1)},
 31955	\quad
 31956	\Theta^{(1)}|_{(1,1)}
 31957	= [\delta_{\mathrm{irr}}]\otimes\Delta.
 31958	\\[4pt]
 31959	g = 2{:}&\quad




thinking
**Identifying symbol inconsistencies**

I'm noticing an issue with the usage of Theta^{(0)} in this context. It serves as Ch_infty structure maps but differs from earlier Theta positive-genus corrections. This really confuses things! The main problem is that sometimes Theta involves genus 0 structure maps and other times it focuses solely on positive-genus corrections. I’ll need to clarify this by designating `\Theta_\cA` for positive-genus correction and introducing a new symbol for genus-0 structure maps, ensuring consistency.
thinking
**Clarifying symbol usage**

I need to check if theorem 31876 utilizes `d_{\Theta^{(0)}}` and `Ob_g` in H^*(gAmod,d_{Theta^{(0)}}). It seems like the tree-twisted differential might be better represented as `d_\pi` or `[\dzero,-]` instead of using `\Theta^{(0)}`. I should also review if `Definition [Modular chiral algebra structure]` at line 14795 is using a generic `\Theta` and how `Theorem\ref{thm:mc2-bar-intrinsic}` relates to this. It’s becoming clear that `\Theta_\cA` is overloaded in incompatible ways, so I’ll need to reserve symbols strictly and rename others for clarity.
thinking
**Confirming MC Equation Definition**

Okay, the user is asking if the MC equation is defined before it's used in proofs. My answer is no, it's not stated as a definition prior to invocation. I'll note to report this [HIGH] at line 236 or maybe 239. I want to ensure I'm getting all the details right for the user! I’ll keep an eye on this as I progress.
thinking
**Clarifying definitions**

I need to check if g^{mod} is defined before using it. It seems like I should define both `\mathfrak g_\cA^{E_1}` and `\mathfrak g_\cA^{mod}` at the same time, closer to the beginning. Later, I could reference 10174 for full proof or definition. I also consider that lines 59-62 mention `\gAmod` before it's defined in 10174. This looks like a separate medium to review.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12160,12218p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 12160	be nonzero without generating a cubic obstruction, as happens for
 12161	Heisenberg; a cubic shadow can be nonzero without generating a quartic
 12162	obstruction, as happens for affine Kac--Moody at generic level. The
 12163	discriminant $\Delta := 8\kappa S_4$ is not an independent invariant
 12164	but a specific quadratic combination of the degree-$2$ and degree-$4$
 12165	shadows that governs whether the tower terminates or extends to
 12166	infinity. The tower structure encodes the nonlinear constraint
 12167	that no individual shadow records.
 12168	
 12169	Three formal objects are needed to make this precise: a weight
 12170	filtration on the modular convolution algebra (to give the Lie
 12171	algebra its pronilpotent completion), an extension tower (to define
 12172	the MC locus at each finite truncation order), and the shadow
 12173	obstruction tower itself (the sequence of truncated MC elements
 12174	whose inverse limit is~$\Theta_\cA$).
 12175	
 12176	\begin{definition}[Weight filtration]
 12177	\label{def:weight-filtration-tower}
 12178	\index{weight filtration!definition|textbf}
 12179	Each component of the modular convolution algebra carries a
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '12984,13036p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 12984	\label{constr:obstruction-recursion}
 12985	Suppose a truncated solution $\Theta_{\cA}^{\leq N}$ has been
 12986	constructed through weight $N$. Its next obstruction is
 12987	\begin{equation}
 12988	\label{eq:next-obstruction}
 12989	\mathfrak{o}_{N+1}
 12990	:=
 12991	\Bigl(
 12992	D_{\cA}\Theta_{\cA}^{\leq N}
 12993	+ \tfrac12[\Theta_{\cA}^{\leq N},
 12994	\Theta_{\cA}^{\leq N}]
 12995	\Bigr)_{N+1}.
 12996	\end{equation}
 12997	If $[\mathfrak{o}_{N+1}] \in H^2(F^{N+1}/F^{N+2})$ vanishes,
 12998	choose a contracting homotopy $h$ and define
 12999	$\Theta_{\cA,N+1} := -h(\mathfrak{o}_{N+1})$.
 13000	Then $\Theta_{\cA}^{\leq N+1} := \Theta_{\cA}^{\leq N}
 13001	+ \Theta_{\cA,N+1}$ solves the Maurer--Cartan equation through
 13002	weight $N+1$.
 13003	\end{construction}
exec
/bin/zsh -lc "rg -n -F \"\\Theta_\\cA :=\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
37:Define $\Theta_\cA := D_\cA - d_0$, the positive-genus part of the
292:The universal MC element $\Theta_\cA := D_\cA - d_0$
2348: $\Theta_\cA := D_\cA - \dzero
3609:Define $\Theta_\cA := D_\cA - \dzero$. Since
3749:The element $\Theta_\cA := D_\cA - \dzero$ is the positive-genus
4346:$\Theta_\cA := D_\cA - \dzero \in
4448:$\Theta_\cA := D_\cA - d_0^{(\cA)}$ and
4940:element $\Theta_\cA := D_\cA - d_0$ does not vanish;
13150: $\Theta_\cA := \varprojlim_N \Theta_\cA^{\leq N}$
13179:element $\Theta_\cA := D_\cA - d_0$ lives in this completed space
13217:$\Theta_\cA := D_\cA - \dzero$
31919:The bar-intrinsic element $\Theta_\cA := D_\cA - d_0$ satisfies




thinking
**Assessing foundation audit**

The user is requesting a foundation audit for the entire file. That suggests early chapters might build on some undefined foundations, which sounds important. I see that item 5 is covered, but I should ensure that all relevant areas are thoroughly checked. It’s crucial to address any inconsistencies or gaps to provide a comprehensive evaluation. Let’s dive into this and get it right for the user!
thinking
**Counting distinct items**

I’m considering whether I should count the number of distinct items. After going through many sections, I could summarize with something like: Checked: 27 | Findings: 8 | Verdict: FAIL. But should I count the labels or blocks I examined? I wonder if I need an exact count or if an approximation would suffice. It might just be better to count the lines or blocks to keep it accurate!
thinking
**Analyzing modular convolution algebra**

I’m looking at some details about weight filtration on modular convolution algebra, particularly from sections 12169 to 12174. It's noted that the extension tower in `\mathfrak g^{amb}_A` is defined between 12193 and 12221, and there are concerns about undefined symbols later. I need to decide that the carrier is `\gAmod`. I should make the necessary replacements and define everything carefully. Additionally, there's an inconsistency with the theta symbol and genus-zero issues to resolve.
thinking
**Inspecting theorems in the table**

I’m considering whether the table accurately maps all five theorems to the scalar level. There’s a chance I could be mistaken in my assessment. It could be a bit too much information to absorb all at once. If needed, I might add a [MEDIUM] for clarity. I should focus on the lines from 14816 onwards because the table might misstate Theorem H and potentially others. A closer inspection sounds like a good plan!
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '14813,14840p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 14813	\begin{remark}[Five theorems from the shadow obstruction tower]
 14814	\label{rem:five-from-one}
 14815	\index{main theorems!from shadow obstruction tower}
 14816	The five main theorems are projections of the scalar
 14817	level~$\Theta_{\cA}^{\leq 2} = \kappa(\cA)$ of the
 14818	shadow obstruction tower
 14819	(Definition~\ref{def:shadow-postnikov-tower}):
 14820	\begin{center}
 14821	\small
 14822	\renewcommand{\arraystretch}{1.2}
 14823	\begin{tabular}{lll}
 14824	\toprule
 14825	\emph{Theorem} & \emph{Projection} & \emph{MC content} \\
 14826	\midrule
 14827	A (bar-cobar adjunction) &
 14828	 $\Theta|_{\hbar=0}$ &
 14829	 Genus-$0$ MC $= $ bar-cobar twisting morphism $\tau$ \\
 14830	B (inversion) &
 14831	 $\mathrm{FT}^2 \simeq \mathrm{id}$ &
 14832	 Getzler--Kapranov involution on MC elements \\

thinking
**Preparing final report**

I’m checking the line references to ensure they're exact. For finding 1, I might use 12193 due to undefined ambient algebra issues. I should note lines 12169-12227 for fixes and include citation file 12193. To highlight inconsistencies, I’ll mention 13019, 14751, and 31091 in the problem text. We’ll format it as `file:12193,12221,13019,14751,31091`. I want to keep line numbers ordered and prepare the final document in a flat bullet format, along with a summary header and no fluff.
codex
- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12193):12193, 12221, 13019, 14751, 31091 — PROBLEM: the shadow tower is not given a stable carrier. Definitions at 12193 and 12221 place the filtration and extension tower in `\mathfrak{g}^{\mathrm{amb}}_\cA` before that algebra is even defined at 31091, while 12169 says the filtration is on the modular convolution algebra, 13019 switches to `\gAmod`, and 14751 says the tower lives in `\mathfrak{g}^{\mathrm{mod}}_\cA`. This is a formal-definition failure, not a cosmetic one: the tower has no fixed home. FIX: rewrite 12176-12230 and 13014-13026 so the filtration, extension tower, and shadow obstruction tower all live in `\gAmod`; keep 31091 as a later graph-sum presentation only, and add one explicit comparison proposition after 31091 identifying the ambient presentation with `\gAmod`.

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14795):14795, 30888, 31873, 31949, 3778 — PROBLEM: `\Theta_\cA` is overloaded beyond repair. It denotes an arbitrary MC element at 14795, the bar-intrinsic positive-genus correction at 3778, the graph-sum object at 30888, and then a full genus expansion with nonzero `\Theta^{(0)}` at 31873/31949. Those are not the same object. FIX: reserve `\Theta_\cA` exclusively for the bar-intrinsic positive-genus correction of Theorem 3770; rename the generic MC variable in 14795 to `\alpha`, rename the genus-0 tree datum in 31873-31964 to `\tau_\cA`, and rename the graph-sum symbol in 30888-30916 to `\mathcal H_\cA^{\mathrm{mod}}` until a theorem identifies `\mathcal H_\cA^{\mathrm{mod}}=\Theta_\cA`.

- [CRITICAL] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:16594):16594, 16612, 16861, 134, 146 — PROBLEM: the G/L/C/M classification contradicts itself inside the same file. The opening at 134-146 says no other depths occur; 16594-16609 then says G/L/C/M are only a coarse classification and every finite depth occurs; 16612-16615 adds a fifth class `\mathbf W`; 16861-16863 goes back to “exactly one of G/L/C/M.” That destroys the theorem surface. FIX: delete 16594-16615 from this chapter and replace them with a single sentence after 16593: `The classes \mathbf G,\mathbf L,\mathbf C,\mathbf M are exhaustive and mutually exclusive on the proved surface of this monograph.` If higher-depth arithmetic refinements are wanted, move them to a separate conjectural remark in the arithmetic/frontier material with new notation that does not alter G/L/C/M.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:39):39, 41, 236, 255, 14795, 3770 — PROBLEM: the MC equation and the universal class are invoked before they are formally introduced in this file, and the first displayed formula is imprecise: `d_0 \Theta_\cA + \tfrac12[\Theta_\cA,\Theta_\cA]=0` omits the commutator interpretation later used at 3611-3613 and 4017-4028. FIX: insert a definition/notation block immediately after line 36:
  `\Theta_\cA:=D_\cA-\dzero`, `d_{\mathrm{Lie}}:=[\dzero,-]`, and `d_{\mathrm{Lie}}(\Theta_\cA)+\tfrac12[\Theta_\cA,\Theta_\cA]=0`.
  Then change line 41 to that exact formula and make early statements/proofs cite the new definition instead of a later theorem.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:30303):30303, 30566, 30598, 3611, 4017 — PROBLEM: the operator in the MC equation drifts. `D_\cA` is defined at 24-25 as the total bar differential, but 30303/30566/30598 write `D_\cA\Theta_\cA + \frac12[\Theta_\cA,\Theta_\cA]=0`, while the actual strict MC derivation later is `[ \dzero,\Theta_\cA ] + \frac12[\Theta_\cA,\Theta_\cA]=0`. With current notation, the displayed equations are wrong. FIX: enforce one notation rule globally: `D_\cA` means only the total bar differential; the dg-Lie differential is `d_{\mathrm{Lie}}=[\dzero,-]`. Replace every `D_\cA\Theta...` and `D_\cA\Theta^{\le r}...` by `d_{\mathrm{Lie}}(\Theta...)`.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:12265):12265, 14816, 14977, 29698 — PROBLEM: the file repeatedly identifies the truncated MC element with its scalar projection: `\Theta_\cA^{\leq 2}=\kappa(\cA)`. That is type-incorrect. Later formulas bracket `\Theta^{\le2}`, and 29698 gives an actual tensor representative `\kappa\cdot\eta\otimes\Lambda`. FIX: replace every bare equality of that form by `\pi_{\mathrm{sc}}(\Theta_\cA^{\le2})=\kappa(\cA)`. Where scalar saturation is intended, write `\Theta_\cA^{\le2}=\kappa(\cA)\,\eta\otimes\Lambda` and explicitly tag the scope.

- [HIGH] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:180):180, 3836; [chapters/theory/e1_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex:290):290 — PROBLEM: `\Theta_\cA^{E_1}` and `({\gAmod}^{E_1})` are used as if they were local objects, but this file never defines them; the actual definition lives in the separate `E_1` chapter. That is a hidden import on the foundational surface. FIX: before the first ordered mention, insert one explicit import sentence:
  `By Chapter~\ref{chap:e1-modular-koszul}, the ordered dg Lie algebra ${\gAmod}^{E_1}$ carries the bar-intrinsic class \Theta_\cA^{E_1}:=D_\cA^{E_1}-\dzero, and \operatorname{av}(\Theta_\cA^{E_1})=\Theta_\cA.`
  Then keep later uses tied to that import.

- [MEDIUM] [chapters/theory/higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:14816):14816-14818 — PROBLEM: “The five main theorems are projections of the scalar level `\Theta_{\cA}^{\le2}=\kappa(\cA)`” is false even by the table that follows: rows A/B/C/H immediately use genus-0 twisting, involution, cross-polarization, and degree-preserving sub-MC data, not the scalar level. FIX: replace the lead sentence with:
  `The five main theorems are projections or consequences of the master MC element \Theta_\cA and its shadow tower; only Theorem D is the scalar level.`

## Summary
Checked: 24 | Findings: 8 | Verdict: FAIL
tokens used
322,775
