# S06_intro_to_body (780s)

- [CRITICAL] chapters/theory/introduction.tex:2508 — PROBLEM: `\label{thm:modular-koszul-duality-main}` is only a `\phantomsection` stub, not a theorem environment or tagged claim. The concordance still cites it as “the flag theorem” at `chapters/connections/concordance.tex:77`, and body chapters cite nonexistent clause numbers at `chapters/theory/higher_genus_modular_koszul.tex:16686`, `21446`, `chapters/frame/heisenberg_frame.tex:4810`, and `chapters/connections/frontier_modular_holography_platonic.tex:4685`. FIX: either restore an actual theorem environment with numbered clauses and a claim-status tag at this anchor, or stop using the `thm:` label entirely: rename it to a non-theorem label and retarget every downstream citation to the concrete theorem labels that actually prove the cited claims.

- [HIGH] chapters/theory/introduction.tex:355 — PROBLEM: the introduction says Theorem C is the family-specific scalar sum rule `\kappa(\cA)+\kappa(\cA^!)=K_\cA`. That is false on the live theorem surface. The actual theorem C at `chapters/theory/higher_genus_complementarity.tex:458-528` is the Verdier eigenspace/Lagrangian decomposition, and its own remark at `434-451` says the scalar formulas are consequences of Theorem C plus Theorem D, not part of Theorem C itself. The same inflation repeats at `chapters/theory/introduction.tex:818-833`. FIX: rewrite both intro summaries so Theorem C states only complementarity/Lagrangian splitting; move the `\kappa`-sum formulas to Theorem D’s duality clause or the appropriate scalar theorem. If `thm:central-charge-complementarity` is cited, use it only for `c+c'`, not `\kappa+\kappa'`.

- [HIGH] chapters/theory/introduction.tex:606 — PROBLEM: this sentence makes two false upgrades. It presents the PTVV shifted-symplectic moduli statement as unconditional, and it says the `+1`/`-1` Verdier eigenspaces intersect in `Z(\cA)`. But the body theorem gives a direct-sum eigenspace decomposition `Q_g(\cA)\oplus Q_g(\cA^!)` at `chapters/theory/higher_genus_complementarity.tex:503-521`, so the `\pm1` eigenspaces intersect trivially in characteristic `0`; and the concordance explicitly marks the ambient shifted-symplectic upgrade as conditional at `chapters/connections/concordance.tex:46-47`. FIX: replace the sentence with the proved statement: for `g\ge1`, the Verdier pairing makes `Q_g(\cA)` and `Q_g(\cA^!)` complementary Lagrangians in a direct sum decomposition; the ambient shifted-symplectic upgrade remains conditional; at `g=0`, `Q_0(\cA)=H^0(\overline{\mathcal M}_0,\mathcal Z(\cA))` and `Q_0(\cA^!)=0`.

- [HIGH] chapters/connections/concordance.tex:65 — PROBLEM: the theorem H row is internally false. It advertises the universal Hilbert polynomial `P(t)=1+t^2`, but the same row also advertises `\ChirHoch^1(V_k(\fg))\cong\fg` at line 67, which forces a nonzero `t`-coefficient and total dimension `\dim(\fg)+2`. The actual general theorem H at `chapters/theory/chiral_hochschild_koszul.tex:715-747` gives `P_\cA(t)=\dim Z(\cA)+\dim\ChirHoch^1(\cA)t+\dim Z(\cA^!)t^2`. The row also cites `thm:critical-level-cohomology`, but that theorem is `\ClaimStatusProvedElsewhere` at `chapters/theory/hochschild_cohomology.tex:150`, and the concordance itself later says Theorem H does not apply at critical level (`chapters/connections/concordance.tex:7188-7194`). FIX: rewrite the row to state amplitude `{0,1,2}` and the general polynomial formula; split examples by family if desired; remove `thm:critical-level-cohomology` from the proved-here theorem-H cluster.

- [HIGH] chapters/theory/introduction.tex:678 — PROBLEM: the introduction claims a universal “total dimension at most four” bound for Theorem H. The body explicitly kills that claim: `\ChirHoch^1(V_k(\fg))\cong\fg` at `chapters/theory/chiral_center_theorem.tex:2008-2021`; `\widehat{\mathfrak{sl}}_2` already has total dimension `5` at `1876-1883`; and the remark at `2078-2089` says the old `\dim\le4` bound fails and is not the correct uniform statement. The same bad bound is repeated at `chapters/theory/introduction.tex:365` and `854-855`. FIX: replace all three occurrences with the true theorem surface: concentration in degrees `{0,1,2}` with polynomial Hilbert series, but no universal total-dimension bound; for generic affine KM, total dimension is `\dim(\fg)+2`.

- [HIGH] chapters/theory/introduction.tex:2016 — PROBLEM: `Theorem~\ref{thm:ds-hpl-transfer}` is a dead cross-reference in Volume I. The label does not exist anywhere in this repo’s `.tex` surface; it exists only in Volume II at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2652`. In a Vol I build, this ref cannot resolve. FIX: replace the `\ref` with plain text such as “the DS-HPL transfer theorem in Volume II,” or introduce an explicit cross-volume citation macro/stub that Volume I actually defines.

- [MEDIUM] chapters/theory/introduction.tex:380 — PROBLEM: the intro assigns the wrong job to Theorem A: “Theorem A constructs the arena `\gAmod`.” The actual theorem A at `chapters/theory/chiral_koszul_pairs.tex:3638-3685` is geometric bar-cobar duality. The existence of `\Theta_\cA` in the convolution algebra is handled by `thm:mc2-bar-intrinsic` at `chapters/theory/higher_genus_modular_koszul.tex:3498-3528`, not by Theorem A. The same misassignment repeats at `chapters/theory/introduction.tex:732-734`. FIX: rewrite both passages so Theorem A supplies the bar-cobar/Verdier apparatus, while the convolution/MC existence claims are attributed to the convolution definition and `Theorem~\ref{thm:mc2-bar-intrinsic}`.

- [MEDIUM] chapters/connections/concordance.tex:454 — PROBLEM: this role map is wrong. It says “Theorem C identifies its genus-`g` curvature; Theorem D computes its leading coefficient.” On the live theorem surface, Theorem C is the complementarity/Lagrangian theorem, while Theorem D is the modular-characteristic/obstruction-class theorem. FIX: rewrite the sentence so Theorem C handles the Verdier decomposition into complementary Lagrangians, and Theorem D handles the scalar curvature/obstruction package and its coefficient `\kappa`.

- [MEDIUM] chapters/theory/introduction.tex:564 — PROBLEM: the theorem B summary strips off the higher-genus scope boundary. It says simply “On the Koszul locus, the counit ... is an equivalence,” but the concordance records the actual seam at `chapters/connections/concordance.tex:36-45`: genus `0` is unconditional, while for arbitrary `\cA`, `g\ge1` is conditional on `\ref{MK:modular}` and only unconditional on the proved standard landscape with the stated PBW exceptions. FIX: import that qualification into the introduction: genus `0` unconditional; higher-genus inversion for arbitrary `\cA` only under the modular-pre-Koszul / PBW-propagation hypotheses.

## Summary
Checked: 15 | Findings: 9 | Verdict: FAIL


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
session id: 019d83c7-8314-7a70-a499-401692d67a6d
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


MISSION: SEAM AUDIT between introduction.tex and concordance.tex.

Introduction→Body. Check: (a) every theorem advertised in the introduction is actually proved in the body, (b) status claims match, (c) no scope inflation in the introduction vs actual theorems, (d) cross-references resolve

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers


thinking
**Planning an audit strategy**

I'm looking at the math audit in the repo, thinking maybe I'll use an explorer for a fast search. It sounds like I could use exec_command to spawn explorer. First, I should acknowledge the request and outline steps for commentary updates. I need to read relevant files, grep for theorems, and reference proofs. I should also check AGENTS/skills and possibly open SKILL.md. I’ll consider using explorer to improve searches and think about gathering precise line references. Using multi-tool execution could help parallelize commands for various files.
thinking
**Inspecting repo structure**

I want to use the command `rg --files introduction.tex` to inspect the repo structure. It seems like a good way to start identifying how the introduction file fits in. I’m curious about what other files might be relevant and how they’re organized. By doing this, I can gather more insights and ensure I’m looking in the right places for the information I need. Let's see what this command reveals!
codex
Using `deep-beilinson-audit` and `claim-surface-sync` for this seam check. I’m starting by locating the introduction surface, then reading the concordance and theorem registry so the audit is grounded in the live source rather than repo folklore.
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files | rg '("'^|/)introduction'"\\.tex"'$|concordance'"\\.tex"'$|theorem_registry'"\\.md"'$|red_team_summary'"\\.md"'$|CLAUDE'"\\.md"'$'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar
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

 succeeded in 52ms:
CLAUDE.md
metadata/theorem_registry.md
chapters/connections/master_concordance.tex
chapters/connections/concordance.tex
chapters/theory/introduction.tex
 succeeded in 51ms:
---
name: claim-surface-sync
description: Use when theorem labels, status tags, concordance text, theorem registry entries, metadata, or duplicated theorem surfaces may drift out of sync. Not for purely local wording edits that do not affect epistemic status.
---

# Claim-Surface Sync

Use this skill when a correction is not finished until the surrounding status surface agrees with it.

## Load first

- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- the relevant metadata files under `metadata/`
- the target `.tex` files
- any duplicated or cross-volume occurrences if available

## Sync protocol

1. Identify the canonical claim surface:
codex
I’ve confirmed the target surface is [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex) against [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex), with theorem registry as the status oracle. Next I’m reading those files in context and extracting every theorem/claim the introduction advertises before checking the body and cross-reference targets one by one.
exec
/bin/zsh -lc "if [ -f archive/raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; elif [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else echo 'red_team_summary.md not found'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 51ms:
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
     1	\chapter{Introduction}
     2	
     3	\section{From a point to a curve}
     4	\label{sec:volume-one-route}
     5	
     6	Koszul duality over a point terminates: a quadratic algebra~$A$ determines a dual coalgebra~$A^!$, the bar construction mediates between them, and no further structure appears. Over a curve, the theory does not terminate. The generators become sections of a $\mathcal{D}_X$-module, the relations become operator product expansions, the bar differential becomes an integral transform with logarithmic kernel, and the topology of higher-genus curves forces obstructions that have no classical analogue. The ordered bar complex $\barB^{\mathrm{ord}}_X(\cA) = T^c(s^{-1}\bar\cA)$, with its deconcatenation coproduct and its classical $R$-matrix $r_\cA(z)$, is the primitive object of this theory; the symmetric bar $\barB^\Sigma_X(\cA)$ is the $\Sigma_n$-coinvariant shadow that discards the $R$-matrix and retains only the scalar modular characteristic $\kappa(\cA) = \mathrm{av}(r_\cA(z))$. The problem is to build and control the ordered bar on algebraic curves at all genera. This monograph solves it.
     7	
     8	The organising principle is as follows. The geometry of the
     9	curve~$X$ determines an operad (the Fulton--MacPherson
    10	compactifications $\FM_n(X)$ with their boundary strata); the
    11	operad determines a bar complex (the cofree coalgebra
    12	$T^c(s^{-1}\bar\cA)$ with its residue-extraction differential);
    13	the bar complex computes the invariants (the modular
    14	characteristic~$\kappa$, the shadow obstruction tower, the
    15	chiral Hochschild cohomology $\ChirHoch^*$). At each step the
    16	passage is forced: one form ($\eta = d\log(z_1 - z_2)$), one
    17	relation (Arnold), one object ($\Theta_\cA$), one equation
    18	($D\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$).
    19	
    20	The obstruction is geometric. On an algebraic curve~$X$, the bar differential is an integral transform whose kernel is the logarithmic propagator $d\log(z_i - z_j)$ on Fulton--MacPherson compactifications of configuration spaces. Already at genus~$0$, chiral Koszul duality differs from its classical counterpart. Vertex algebras live on the formal disk~$D$, not on a bare point; the passage from~$D$ to a point discards the thickening data (completion, growth conditions) that the $\mathcal{D}$-module structure depends on. The affine line~$\mathbb{A}^1$ deformation-retracts onto a point, but this retraction is additional data: relating the bar construction on~$\mathbb{A}^1$ to the classical bar over a point requires specifying the retraction and its attendant homotopy transfer. Already on~$\mathbb{A}^1$, the configuration spaces $\mathrm{Conf}_n(\mathbb{A}^1)$ carry Fulton--MacPherson compactifications and the Arnol'd algebra $H^*(\mathrm{Conf}_n(\mathbb{A}^1))$, generated by the forms $\omega_{ij} = d\log(z_i - z_j)$ subject to the Arnold relation: these structures are entirely absent over a point. On~$\mathbb{P}^1 = \mathbb{A}^1 \cup \mathbb{A}^1$, compactness further changes the homotopy type of the configuration spaces. The classical theory embeds into this picture via the formal-disk restriction, but the embedding is not an equivalence: even at genus~$0$, the ordered-versus-unordered bar distinction and the configuration-space geometry are genuinely new. At genus~$g \geq 1$, the Hodge bundle $\mathbb{E}$ on~$\overline{\mathcal{M}}_g$ introduces curvature into the bar differential, producing central extensions, conformal anomalies, and curved $A_\infty$ structures that have no analogue over a point.
codex
The introduction is already surfacing a large advertised theorem cluster, not just the five main theorems. I’m enumerating every `\ref`/`\eqref` target in the introduction now, then I’ll separate pure navigation references from actual theorem advertisements so the seam audit hits the real risk surface.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '521,780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '261,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '781,1040p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\(Theorem|Proposition|Corollary|Lemma|Definition|Remark|Construction|Equation|Chapter|Part|Section|\\eqref\\{|\\ref\\{)' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   261	genus tower accepts.
   262	\end{remark}
   263	
   264	Five existing programmes address aspects of the problem.
   265	Beilinson--Drinfeld~\cite{BD04} construct the factorisation
   266	algebra on $\Ran(X)$ and prove chiral homology is well-defined,
   267	but do not treat bar-cobar inversion, complementarity, or the
   268	genus tower.
   269	Francis--Gaitsgory~\cite{FG12} establish chiral Koszul duality
   270	at genus~$0$ for Lie-type (coLie) bar complexes; their
   271	framework does not reach higher genera, the full tensor bar,
   272	or the shadow obstruction tower.
   273	Costello--Gwilliam~\cite{CG17} develop factorisation algebras
   274	as a framework for perturbative QFT and prove the
   275	$\mathsf{E}_3$-algebra structure of perturbative
   276	Chern--Simons theory; they do not treat Koszul duality,
   277	complementarity, or the modular characteristic.
   278	Gui--Li--Zeng~\cite{GLZ22} prove a quadratic duality for chiral
   279	algebras at the cochain level; their result is a genus-$0$,
   280	degree-$2$ theorem and does not address the shadow tower, higher
 succeeded in 51ms:
   521	coalgebras (the iterated reduced coproduct eventually
   522	vanishes).
   523	
   524	Each statement below is the av-image of a corresponding
   525	$\Eone$ statement on the ordered convolution algebra
   526	${\gAmod}^{\Eone}$
   527	(see~\S\ref{subsec:e1-as-primitive} for the averaging map
   528	$\operatorname{av}\colon{\gAmod}^{\Eone}\twoheadrightarrow\gAmod$
   529	and Chapter~\ref{chap:e1-modular-koszul} for the ordered
   530	counterparts $\mathrm{A}^{\Eone}$--$\mathrm{H}^{\Eone}$).
   531	The five theorems are the invariants that survive averaging.
   532	
   533	\begin{itemize}
   534	\item \emph{Theorem~A} (Geometric bar-cobar duality,
   535	 Theorem~\ref{thm:bar-cobar-isomorphism-main}).
   536	 The bar functor
   537	 \[
   538	 \bar{B}_X \colon
   539	 \operatorname{Alg}_{\mathrm{aug}}(\operatorname{Fact}(X))
   540	 \to
 succeeded in 51ms:
   781	holographic correction hierarchy, and the Drinfeld double
   782	$U_\cA = \cA \bowtie \cA^!$ is the universal boundary-bulk algebra
   783	that reconstructs the gravitational theory from the VOA.
   784	Each theorem corresponds to a single claim of the thesis.
   785	\begin{enumerate}[label=\textup{(\Alph*)}]
   786	\item \emph{Existence of the dual}
   787	 \textup{(}Theorem~A\textup{)}.
   788	 The existence of the Verdier dual $\cA^!$ is implicit in
   789	 Definition~\ref{def:chiral-koszul-pair} of a chiral Koszul
   790	 pair, which equips the pair
   791	 $(\cA_1, \cA_2)$ with Verdier-compatible identifications
   792	 $\mathbb{D}_{\mathrm{Ran}}(\cC_1) \simeq \cC_2$ from the
   793	 outset; Theorem~A part~(1), the bar-cobar adjunction, then
   794	 supplies the unit and counit quasi-isomorphisms
   795	 $\cC_i \simeq \barB_X(\cA_i)$ on the Koszul locus.
   796	 Part~(2), the Verdier intertwining
   797	 $\mathbb{D}_{\mathrm{Ran}}\barB_X(\cA_1) \simeq \barB_X(\cA_2)$,
   798	 then unpacks the Verdier clause of the definition by transport
   799	 across part~(1). This supplies the algebraic pair
   800	 $(\cA, \cA^!)$ on which the Drinfeld double $U_\cA$ is
 exited 2 in 51ms:
rg: regex parse error:
    (?:\\(Theorem|Proposition|Corollary|Lemma|Definition|Remark|Construction|Equation|Chapter|Part|Section|\eqref\{|\ref\{))
                                                                                                           ^^
error: unrecognized escape sequence
codex
The seam is broader than a single flag theorem. The introduction is advertising the five main theorems, three structure theorems, several corollaries/propositions as if they are settled, and a large set of navigation references. I’m splitting the audit into three checks now:

1. `Status seam`: introduction claims vs [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex) and [metadata/theorem_registry.md](/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md).
2. `Scope seam`: introduction paraphrase vs actual theorem statements in the body files for each advertised label.
3. `Reference seam`: every `\ref`/`\eqref` in [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex) checked for a live target, with special attention to transition points where the intro hands off to the body.
exec
/bin/zsh -lc "perl -ne 'while(/\\\\(?:Theorem|Theorems|Proposition|Propositions|Corollary|Corollaries|Lemma|Lemmas|Definition|Definitions|Remark|Remarks|Construction|Constructions|Principle|Conjecture|Chapter|Part|Section)~\\\\ref\\{(["'^}]+)'"\\}/g){print \""'$.:$1'"\\n\"}' chapters/theory/introduction.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'while(/\\\\(?:eq)?ref\\{(["'^}]+)'"\\}/g){print \""'$.:$1'"\\n\"}' chapters/theory/introduction.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{(thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:quantum-complementarity-main|thm:genus-universality|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|thm:modular-koszul-duality-main|thm:modular-characteristic|thm:riccati-algebraicity|thm:shadow-formality-identification|thm:single-line-dichotomy|prop:depth-gap-trichotomy|prop:sc-formal-iff-class-g|prop:free-field-scalar-exact|thm:mc2-bar-intrinsic|thm:bar-nilpotency-complete|prop:pole-decomposition|thm:fundamental-twisting-morphisms|thm:bar-concentration|thm:koszul-equivalences-meta|thm:universal-generating-function|thm:spectral-characteristic|thm:hochschild-polynomial-growth|lem:chirhoch-descent|thm:e1-primacy|thm:thqg-swiss-cheese|cor:shadow-visibility-genus|rem:two-orthogonal-axes|thm:central-charge-complementarity)\\}' chapters appendices metadata" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

 succeeded in 50ms:
42:ch:algebraic-foundations
42:sec:dictionary
57:thm:modular-characteristic
72:thm:shadow-formality-identification
82:thm:single-line-dichotomy
87:prop:depth-gap-trichotomy
91:prop:sc-formal-iff-class-g
96:prop:free-field-scalar-exact
103:def:generating-depth
108:thm:mc2-bar-intrinsic
110:thm:riccati-algebraicity
120:thm:shadow-formality-identification
124:rem:two-orthogonal-axes
126:cor:shadow-visibility-genus
137:thm:quantum-complementarity-main
149:sec:volume-one-route
171:thm:bar-nilpotency-complete
202:eq:borcherds-axiom
203:def:chiral-algebra
223:subsec:frame-sl2-bar-low-degree
 succeeded in 51ms:
chapters/connections/thqg_open_closed_realization.tex:382:\label{thm:thqg-swiss-cheese}
chapters/examples/genus_expansions.tex:1913:\begin{theorem}[Universal generating function; \ClaimStatusProvedHere]\label{thm:universal-generating-function}
chapters/theory/higher_genus_modular_koszul.tex:2660:\label{thm:modular-characteristic}
chapters/theory/higher_genus_modular_koszul.tex:3270:\label{thm:spectral-characteristic}
chapters/theory/higher_genus_modular_koszul.tex:3499:\label{thm:mc2-bar-intrinsic}
chapters/theory/higher_genus_modular_koszul.tex:15083:\label{thm:shadow-formality-identification}
chapters/theory/higher_genus_modular_koszul.tex:17051:\label{thm:riccati-algebraicity}
chapters/theory/higher_genus_modular_koszul.tex:17198:\label{prop:depth-gap-trichotomy}
chapters/theory/higher_genus_modular_koszul.tex:17987:\label{thm:single-line-dichotomy}
chapters/theory/higher_genus_modular_koszul.tex:21948:\label{prop:free-field-scalar-exact}
chapters/theory/higher_genus_modular_koszul.tex:24724:\label{cor:shadow-visibility-genus}
chapters/theory/higher_genus_modular_koszul.tex:24781:\label{rem:two-orthogonal-axes}
chapters/theory/hochschild_cohomology.tex:96:\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
chapters/theory/hochschild_cohomology.tex:150:\begin{theorem}[Critical level Lie algebra cohomology; \ClaimStatusProvedElsewhere]\label{thm:critical-level-cohomology}
chapters/theory/hochschild_cohomology.tex:205:\begin{theorem}[W-algebra Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:w-algebra-hochschild}
chapters/theory/bar_construction.tex:788:\begin{theorem}[Nilpotency of bar differential; \ClaimStatusProvedHere]\label{thm:bar-nilpotency-complete}
chapters/theory/bar_construction.tex:970:\begin{proposition}[Pole decomposition of the bar differential; \ClaimStatusProvedHere]\label{prop:pole-decomposition}
chapters/theory/chiral_hochschild_koszul.tex:539:\label{lem:chirhoch-descent}
chapters/theory/chiral_hochschild_koszul.tex:703:\label{thm:hochschild-polynomial-growth}
chapters/theory/higher_genus_foundations.tex:5298:\begin{theorem}[Genus universality; \ClaimStatusProvedHere]\label{thm:genus-universality}
exec
/bin/zsh -lc "perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/introduction.tex | sort -u > /tmp/intro_refs.txt && while IFS= read -r ref; do if "'! rg -n --fixed-strings "'"\\\\label{"'$ref}" chapters appendices frontmatter metadata >/dev/null; then echo "MISSING:$ref"; fi; done < /tmp/intro_refs.txt' in /Users/raeez/chiral-bar-cobar succeeded in 2.23s:
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:chiral-deformation
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:derived-langlands
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:en-koszul-duality
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:feynman
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:fourier-seed
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:genus-expansions
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:genus1-seven-faces
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:heisenberg-frame
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:holographic-datum-master
rg: frontmatter: No such file or directory (os error 2)
MISSING:ch:ht-boundary




thinking
**Evaluating label checks**

I'm realizing that our label check is missing because I'm only searching in the chapters, appendices, metadata, and front matter sections, which might not exist. I should consider using different label formats like “ch:” versus “chap” which might not be found because they could be defined in `main.tex` or in different directories. I need to search all `.tex` files for better results. The session is still running, so I'll see if there's more output.
thinking
**Checking chapter labels**

It looks like many chapter labels might be incorrectly defined as `ch:` instead of `\chapter{...}\label{chap:...}`, which could lead to broken references. That's definitely a major issue to investigate! To avoid false positives, I’ll need to do a systematic check. I wonder if any missing references relate to `\crefalias`. I plan to use grep to verify. The introduction refers to `Chapter\ref{ch:heisenberg-frame}`, so that’s worth checking too. I might need to use the build or aux files to resolve any discrepancies since the user needs these cross-references clarified!
thinking
**Considering resolution methods**

I’m thinking that resolving cross-references might be easiest through the LaTeX build of the introduction or the main document. But since it's a large book, it could be quite heavy and take time. I could use the command `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, which is possible but might take a while. It seems like targeting the introduction could help, especially by checking build warnings. If the build log is available, I might want to refer to that too!
thinking
**Auditing references and builds**

Since the user asked for no edits, only an audit, I can run a build, but I worry it might be too heavy for the system. Instead, I could check for undefined references in the latest logs, though verifying specific reference labels may be more efficient. I might look at the `.aux` file and identify all theorem statements in the document. It seems important to cross-reference missing labels and ensure actual unresolved items are found. I'll need to search the entire repository.
codex
The first hard seam break is already visible: the introduction references a large set of labels that do not trivially resolve by label search, so I’m now distinguishing true unresolved refs from labels that exist under variant chapter-prefix conventions. After that I’m checking the five main theorem summaries against the actual theorem statements, because that’s where scope inflation is most likely.
exec
/bin/zsh -lc "rg -n --fixed-strings '\\label{chap:bar-cobar}' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\label{ch:heisenberg-frame}' ." in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings '\\label{eq:intro-sugawara-kappa}' ." in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./chapters/theory/bar_construction.tex:2:\label{chap:bar-cobar}
./rectification_20260412_233715/R22_bar_construction.md:199:\label{chap:bar-cobar}
./rectification_20260412_233715/R22_bar_construction.md:366:\label{chap:bar-cobar}
 succeeded in 53ms:
./chapters/frame/heisenberg_frame.tex:1:\chapter{The Gaussian Archetype}\label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:120:\label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:152:/bin/zsh -lc "rg -n -C 2 -F '\\label{SA:completion}' -F '\\label{SA:convergence}' -F '\\label{SA:curves}' -F '\\label{SA:grading}' -F '\\label{SA:ground-field}' -F '\\label{app:typeA-baxter-rees-theta}' -F '\\label{ch:heisenberg-frame}' -F '\\label{ch:ht-boundary}' -F '\\label{ch:k3-times-e}' -F '\\label{ch:kontsevich-integral}' -F '\\label{ch:ordered-associative-chiral-kd}' -F '\\label{ch:ym-boundary-theory}' -F '\\label{ch:ym-higher-body-couplings}' -F '\\label{ch:ym-instanton-screening}' -F '\\label{chap:casimir-divisor}' -F '\\label{chap:dg-shifted-factorization}' -F '\\label{chap:physical-origins}' -F '\\label{chap:shifted-rtt-orthogonal-coideals}' -F '\\label{chap:toroidal-elliptic}' -F '\\label{comp:bulk-wn}' -F '\\label{comp:dybe-matrix-entries}' -F '\\label{comp:ell-bar-deg1}' -F '\\label{comp:ell-bar-deg2}' -F '\\label{comp:ell-curvature}' -F '\\label{comp:heisenberg-center}' -F '\\label{comp:shuffle-generators}' -F '\\label{comp:spectral-discriminants-standard}' -F '\\label{conj:ade-chart-k3}' -F '\\label{conj:ads-cft-bar}' -F '\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:158:rg: \label{ch:heisenberg-frame}: No such file or directory (os error 2)
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:176:/bin/zsh -lc "rg -n -C 2 -e '\\\\label{SA:completion}' -e '\\\\label{SA:convergence}' -e '\\\\label{SA:curves}' -e '\\\\label{SA:grading}' -e '\\\\label{SA:ground-field}' -e '\\\\label{app:typeA-baxter-rees-theta}' -e '\\\\label{ch:heisenberg-frame}' -e '\\\\label{ch:ht-boundary}' -e '\\\\label{ch:k3-times-e}' -e '\\\\label{ch:kontsevich-integral}' -e '\\\\label{ch:ordered-associative-chiral-kd}' -e '\\\\label{ch:ym-boundary-theory}' -e '\\\\label{ch:ym-higher-body-couplings}' -e '\\\\label{ch:ym-instanton-screening}' -e '\\\\label{chap:casimir-divisor}' -e '\\\\label{chap:dg-shifted-factorization}' -e '\\\\label{chap:physical-origins}' -e '\\\\label{chap:shifted-rtt-orthogonal-coideals}' -e '\\\\label{chap:toroidal-elliptic}' -e '\\\\label{comp:bulk-wn}' -e '\\\\label{comp:dybe-matrix-entries}' -e '\\\\label{comp:ell-bar-deg1}' -e '\\\\label{comp:ell-bar-deg2}' -e '\\\\label{comp:ell-curvature}' -e '\\\\label{comp:heisenberg-center}' -e '\\\\label{comp:shuffle-generators}' -e '\\\\label{comp:spectral-discriminants-standard}' -e '\\\\label{conj:ade-chart-k3}' -e '\\\\label{conj:ads-cft-bar}' -e '\\\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:178:    (?:\\label{SA:completion})|(?:\\label{SA:convergence})|(?:\\label{SA:curves})|(?:\\label{SA:grading})|(?:\\label{SA:ground-field})|(?:\\label{app:typeA-baxter-rees-theta})|(?:\\label{ch:heisenberg-frame})|(?:\\label{ch:ht-boundary})|(?:\\label{ch:k3-times-e})|(?:\\label{ch:kontsevich-integral})|(?:\\label{ch:ordered-associative-chiral-kd})|(?:\\label{ch:ym-boundary-theory})|(?:\\label{ch:ym-higher-body-couplings})|(?:\\label{ch:ym-instanton-screening})|(?:\\label{chap:casimir-divisor})|(?:\\label{chap:dg-shifted-factorization})|(?:\\label{chap:physical-origins})|(?:\\label{chap:shifted-rtt-orthogonal-coideals})|(?:\\label{chap:toroidal-elliptic})|(?:\\label{comp:bulk-wn})|(?:\\label{comp:dybe-matrix-entries})|(?:\\label{comp:ell-bar-deg1})|(?:\\label{comp:ell-bar-deg2})|(?:\\label{comp:ell-curvature})|(?:\\label{comp:heisenberg-center})|(?:\\label{comp:shuffle-generators})|(?:\\label{comp:spectral-discriminants-standard})|(?:\\label{conj:ade-chart-k3})|(?:\\label{conj:ads-cft-bar})|(?:\\label{conj:agt-bar-cobar})
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:187:/bin/zsh -lc "rg -F -n -C 2 -e '\\label{SA:completion}' -e '\\label{SA:convergence}' -e '\\label{SA:curves}' -e '\\label{SA:grading}' -e '\\label{SA:ground-field}' -e '\\label{app:typeA-baxter-rees-theta}' -e '\\label{ch:heisenberg-frame}' -e '\\label{ch:ht-boundary}' -e '\\label{ch:k3-times-e}' -e '\\label{ch:kontsevich-integral}' -e '\\label{ch:ordered-associative-chiral-kd}' -e '\\label{ch:ym-boundary-theory}' -e '\\label{ch:ym-higher-body-couplings}' -e '\\label{ch:ym-instanton-screening}' -e '\\label{chap:casimir-divisor}' -e '\\label{chap:dg-shifted-factorization}' -e '\\label{chap:physical-origins}' -e '\\label{chap:shifted-rtt-orthogonal-coideals}' -e '\\label{chap:toroidal-elliptic}' -e '\\label{comp:bulk-wn}' -e '\\label{comp:dybe-matrix-entries}' -e '\\label{comp:ell-bar-deg1}' -e '\\label{comp:ell-bar-deg2}' -e '\\label{comp:ell-curvature}' -e '\\label{comp:heisenberg-center}' -e '\\label{comp:shuffle-generators}' -e '\\label{comp:spectral-discriminants-standard}' -e '\\label{conj:ade-chart-k3}' -e '\\label{conj:ads-cft-bar}' -e '\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:233:\label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:277:LABEL \label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:284:/bin/zsh -lc "for l in '\\\\label{SA:completion}' '\\\\label{SA:convergence}' '\\\\label{SA:curves}' '\\\\label{SA:grading}' '\\\\label{SA:ground-field}' '\\\\label{ch:heisenberg-frame}' '\\\\label{comp:heisenberg-center}'; do
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:303:LABEL \\label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:304:chapters/frame/heisenberg_frame.tex:1:\label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:333:   2 \label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:353:/bin/zsh -lc "for l in '\\\\label{SA:completion}' '\\\\label{SA:convergence}' '\\\\label{SA:curves}' '\\\\label{SA:grading}' '\\\\label{SA:ground-field}' '\\\\label{ch:heisenberg-frame}' '\\\\label{comp:heisenberg-center}'; do
./audit_campaign_20260412_231034/AP15_duplicate_labels.md:377:LABEL \\label{ch:heisenberg-frame}
./audit_campaign_20260412_231034/XV09_label_unique_xvol.md:156:\label{ch:heisenberg-frame}
 succeeded in 61ms:
./audit_campaign_20260412_231034/F14_averaging.md:709:  1289	\begin{equation}\label{eq:intro-sugawara-kappa}
./chapters/theory/introduction.tex:1289:\begin{equation}\label{eq:intro-sugawara-kappa}
exec
/bin/zsh -lc "rg -n --fixed-strings '\\label{thm:bar-cobar-isomorphism-main}' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
./audit_campaign_20260412_231034/T01_thm_A.md:852:  3611	\label{thm:bar-cobar-isomorphism-main}
./audit_campaign_20260412_231034/XV08_thm_status_xvol.md:329:/Users/raeez/chiral-bar-cobar-vol2/main.tex:773:\phantomsection\label{thm:bar-cobar-isomorphism-main}%
./audit_campaign_20260412_231034/XV08_thm_status_xvol.md:510:3639:\label{thm:bar-cobar-isomorphism-main}
./rectification_20260412_233715/R02_higher_genus_complementarity.md:506:chapters/theory/chiral_koszul_pairs.tex:3611:\label{thm:bar-cobar-isomorphism-main}
./compute/audit/theorem_a_b_tautology_verification.md:21:\label{thm:bar-cobar-isomorphism-main}
./rectification_20260412_233715/R18_cobar_construction.md:448:chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
./rectification_20260412_233715/R22_bar_construction.md:335:\label{thm:bar-cobar-isomorphism-main}


thinking
**Resolving missing labels**

It seems the missing labels during the search were due to an aborted process, likely because I didn’t have the frontmatter directory. I need to create a robust label resolution by searching through all `.tex` files in the current repo, including `main.tex`. I’ll search using a command that excludes non-existent directories. I want to focus on cross-references in documents, ensuring that labels exist in included files. A script with a while loop will help compile a list of missing labels from the search.
thinking
**Checking reference targets**

I’m considering that some `\ref` commands might point to chapters in other volumes if those files are imported. However, the introduction in Volume I can’t resolve references to labels in Volume II unless those labels are compiled into the same document. That suggests they could end up broken unless the macros are imported, which is likely not the case. I need to identify which of the missing references are due to chapters that don’t have labels. Running a robust command will help with this.
exec
/bin/zsh -lc "perl -ne 'while(/\\\\(?:ref|eqref)\\{(["'^}]+)'"\\}/g){print \""'$1'"\\n\"}' chapters/theory/introduction.tex | sort -u > /tmp/intro_refs_unique.txt && while IFS= read -r ref; do if "'! rg -n --glob '"'*.tex' --fixed-strings \"\\\\label{"'$ref}" . >/dev/null; then echo "$ref"; fi; done < /tmp/intro_refs_unique.txt | sed -n '"'1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 2.60s:
thm:ds-hpl-transfer

thinking
**Verifying reference context**

I need to address the unresolved reference from the introduction, labeled `thm:ds-hpl-transfer`. It seems like I should verify its line and surrounding context. I found it at line 2016 in the introduction, but I want to dig deeper into the surrounding text for clarity. I’m also considering whether there might be cross-volume references or other related elements to inspect. Let’s check that out!
codex
I’ve reduced the reference seam to one live unresolved label so far: `thm:ds-hpl-transfer` from the introduction. I’m moving to the harder part now: reading the actual theorem statements behind A/B/C/D/H and matching them against the introduction’s summaries and the concordance table, because that’s where status drift and scope inflation usually hide.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3600,3695p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4100,4195p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '5260,5365p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '430,560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '680,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2620,2725p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4100	factorizes over nodal gluings into tensor products of lower-genus pieces.
  4101	Functoriality of bar-cobar inversion
  4102	(Theorem~\ref{thm:bar-cobar-inversion-functorial}) identifies
  4103	$\psi_g|_{D_\Gamma}$ with the corresponding tensor product of lower-genus inversion maps.
  4104	
  4105	Every vertex genus in $\Gamma$ is strictly smaller than $g$: in the separating case,
  4106	$g=g_1+g_2$ with $g_1,g_2 \geq 0$ and each $g_i < g$ (note: one component may have genus~$0$, which is the base case of the induction); in the non-separating case, the single vertex has genus $g-1 < g$. In either case, the induction hypothesis applies to each vertex. Tensor products of quasi-isomorphisms
  4107	are quasi-isomorphisms by the K\"unneth formula for factorization
  4108	algebras at nodes: the factorization tensor product at a node is
  4109	computed fiberwise over the normalization, reducing to the plain
  4110	tensor product of chain complexes over the ground field, which
  4111	preserves quasi-isomorphisms by K\"unneth. This yields the claim.
  4112	\end{proof}
  4113	
  4114	\begin{lemma}[Extension across boundary; \ClaimStatusProvedHere]\label{lem:extension-across-boundary-qi}
  4115	Let $X$ be a stack with open-closed decomposition $X = U \sqcup Z$ (with
  4116	$j:U\hookrightarrow X$, $i:Z\hookrightarrow X$). For a morphism of complexes
  4117	$f:K\to L$ on $X$, if $j^*f$ and $i^*f$ are quasi-isomorphisms, then $f$ is a
  4118	quasi-isomorphism.
  4119	\end{lemma}
 succeeded in 51ms:
  3600	$G_\cA = H_\cA/(1 + H_\cA)$, or at the level of formal power
  3601	series,
  3602	\[
  3603	G_\cA(t) \;=\; H_\cA(t) - G_\cA(t)\,H_\cA(t).
  3604	\]
  3605	Extracting the coefficient of $t^q$ gives
  3606	$g_q = h_q - \sum_{r=1}^{q-1} g_r\, h_{q-r} - g_q\, h_0$;
  3607	since $h_0 = 0$ (no nonempty words of weight~$0$), the formula
  3608	follows by induction on~$q$.
  3609	\end{proof}
  3610	
  3611	\begin{remark}[The primitive defect as a Koszulness probe]
  3612	\label{rem:primitive-defect-probe}
  3613	\index{primitive defect series!Koszulness probe}
  3614	
  3615	For a quadratic chiral algebra $\cA$ with generators of
  3616	weights $d_1, \ldots, d_s$, the PBW basis ensures that all
  3617	quasi-primaries are generated by the declared strong generators,
  3618	so $\Delta^{\mathrm{prim}}_\cA = 0$ identically. The
  3619	Virasoro algebra $\mathrm{Vir}_c$ has a single strong generator
 succeeded in 50ms:
  5260	$(\operatorname{obs}_g)^2 = \kappa^2 \cdot \lambda_g^2 = 0$
  5261	for \emph{all} $g \geq 1$, by Mumford's relation.
  5262	\end{example}
  5263	
  5264	\subsection{Summary table: obstruction classes for key examples}
  5265	\label{subsec:obstruction-summary-table}
  5266	
  5267	\begin{table}[ht]
  5268	\centering
  5269	\caption{Genus-$g$ obstruction classes For single-generator families, $\mathrm{obs}_g = \kappa \cdot \lambda_g$
  5270	 holds unconditionally at all genera. For multi-weight families
  5271	 \textup{(}$W_3$\textup{)}, the formula is unconditional at $g = 1$;
  5272	 at $g \geq 2$, a cross-channel correction
  5273	 $\delta F_g^{\mathrm{cross}} \neq 0$
  5274	 \textup{(all-weight, with cross-channel correction $\delta F_g^{\mathrm{cross}}$)} is present
  5275	 \textup{(}Theorem~\textup{\ref{thm:multi-weight-genus-expansion}}\textup{)}.}
  5276	\label{tab:obstruction-summary}
  5277	\begin{tabular}{|l|c|c|}
  5278	\hline
  5279	\textbf{Chiral Algebra} & \textbf{Obstruction $\text{obs}_g$} & \textbf{Physical Meaning} \\
 succeeded in 52ms:
  2620	and Verdier properties.
  2621	\end{proof}
  2622	
  2623	\begin{remark}[The modular characteristic hierarchy]
  2624	\label{rem:modular-characteristic-package}
  2625	\label{rem:characteristic-hierarchy}
  2626	\index{modular characteristic!hierarchy|textbf}
  2627	The package~$\mathcal{C}_{\cA}$ \eqref{eq:full-package-quintuple}
  2628	has three logarithmic levels:
  2629	(1)~scalar: $\kappa(\cA)$ (Theorem~\ref{thm:modular-characteristic}),
  2630	exponential $=$ modular period~$N$;
  2631	(2)~spectral: $\Delta_{\cA}(x)$
  2632	(Theorem~\ref{thm:spectral-characteristic}),
  2633	exponential $=$ periodicity profile~$\Pi_{\cA}$;
  2634	(3)~shadow obstruction tower / full MC: $\Theta_{\cA}^{\leq r}$, $\Defcyc(\cA)$
  2635	(Definition~\ref{def:shadow-postnikov-tower};
  2636	Theorems~\ref{thm:universal-theta} and~\ref{thm:mc2-full-resolution}
  2637	at scalar level),
  2638	exponential $=$ modular automorphy.
  2639	See Table~\ref{tab:master-invariants}.
 succeeded in 53ms:
   430	$\mathcal{Z}_{\cA}$ by the fiber-level identification
   431	from Step~3, which holds uniformly over the base.
   432	\end{proof}
   433	
   434	\begin{remark}[Theorem~C decomposition]\label{rem:theorem-C-decomposition}
   435	\index{Theorem C!decomposition}
   436	Theorem~C has three named pieces: $\mathrm{C}_0$ (fiber-center
   437	identification, this theorem) produces the ambient complex;
   438	$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
   439	gives the Verdier eigenspace decomposition and its Lagrangian
   440	splitting; $\mathrm{C}_2$
   441	(Theorem~\ref{thm:shifted-symplectic-complementarity}) is the
   442	conditional bar-side BV / shifted-symplectic upgrade.
   443	The chain-level mechanism for~$\mathrm{C}_1$ is the Verdier involution
   444	$\sigma$ exchanging the two eigenspaces; at the scalar level
   445	the complementarity formulas below are consequences of the
   446	$\mathrm{C}_1$ decomposition together with Theorem~D, and not a
   447	separate $\mathrm{C}_2$ label:
   448	$\kappa(\cA)+\kappa(\cA^!)=0$ for Kac--Moody and free-field pairs,
   449	while $\kappa(\cA)+\kappa(\cA^!)=\varrho\cdot K\neq 0$ for
 succeeded in 53ms:
   680	$\mathcal{Z}(\cA)$ and $\mathcal{Z}(\cA^!)$ via the canonical isomorphism
   681	$\mathcal{Z}(\cA) \cong \mathcal{Z}(\cA^!)$ of
   682	Theorem~\ref{thm:quantum-complementarity-main}(Step~7), one obtains
   683	a duality on the endomorphism complex
   684	$\mathrm{End}_{D(\mathrm{Mod}_{\cA})}(\cA) \cong
   685	\mathrm{End}_{D(\mathrm{Comod}_{\cA^!})}(\cA^!)^{\vee}$
   686	by the module Koszul duality equivalence
   687	(Theorem~\ref{thm:e1-module-koszul-duality}).
   688	Passing to cohomology, Lemma~\ref{lem:hochschild-shift-computation}
   689	computes the grading shift: the variable~$[n+2]$ collapses to the
   690	uniform~$[2]$. The $\omega_X$ twist comes from Serre duality on
   691	the underlying curve, yielding the result.
   692	\end{proof}
   693	
   694	\begin{remark}[Proof infrastructure]
   695	Both proofs use the bar-cobar quasi-isomorphism at all genera
   696	(Theorem~\ref{thm:higher-genus-inversion}) and the Kodaira--Spencer map
   697	for Koszul pairs
   698	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
   699	\end{remark}

thinking
**Inspecting components**

I need to check the actual theorem H and other components in the file `hochschild_cohomology.tex`, which probably includes important information. I should also look closely at proposition `prop:chirhoch1-affine-km`. It seems like a good idea to inspect these elements later to ensure I understand everything clearly. I'll make a note to revisit this so I don't forget any details that could be relevant.
exec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '80,235p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    80	$\mathcal{M}$ is
    81	\[\ChirHoch^*(\mathcal{A}, \mathcal{M})
    82	= \operatorname{RHom}_{\mathcal{D}_X}(\barBgeom(\mathcal{A}), \mathcal{M}).\]
    83	The chain-level model is Definition~\ref{def:chiral-hochschild}.
    84	\end{definition}
    85	
    86	\begin{theorem}[Comparison with classical theory {\cite{BD04}}; \ClaimStatusProvedElsewhere]\label{thm:hochschild-classical-comparison}
    87	There is a spectral sequence:
    88	\[E_2^{p,q} = HH^p(\mathcal{A}_0, H^q(\Omega^*_X)) \Rightarrow \ChirHoch^{p+q}(\mathcal{A})\]
    89	where $\mathcal{A}_0$ is the fiber at a point.
    90	\end{theorem}
    91	
    92	\section{Periodicity phenomena}
    93	
    94	\subsection{Virasoro Hochschild cohomology}
    95	
    96	\begin{theorem}[Virasoro Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:virasoro-hochschild}
    97	For the Virasoro algebra at generic central charge $c$ (avoiding
    98	$c_{p,q} = 1 - 6(p-q)^2/(pq)$ and $c = 1$):
    99	\[\ChirHoch^n(\mathrm{Vir}_c) = \begin{cases}
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1980,2045p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Theorem~A|Theorem~B|Theorem~C|Theorem~D|Theorem~H|flag theorem|five main theorems' chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2480,2555p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'bar-cobar-isomorphism-main|higher-genus-inversion|quantum-complementarity-main|modular-characteristic|genus-universality|hochschild-polynomial-growth|w-algebra-hochschild|virasoro-hochschild|critical-level-cohomology|chirhoch1-affine-km|modular-koszul-duality-main' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1980	For the Virasoro algebra
  1981	(single generator of weight~$2$), the Hilbert series is
  1982	$P(t) = 1 + t^2$, giving total dimension~$2$:
  1983	one copy of~$\bC$ in degree~$0$ (the vacuum) and one copy
  1984	in degree~$2$ (the central charge deformation).
  1985	The degree-$2$ generator $\Theta$ represents
  1986	the deformation $c \mapsto c + \epsilon$.
  1987	The weight grading: $\Theta$ sits at conformal weight~$0$
  1988	because the deformation $c \mapsto c + \epsilon$ does not shift
  1989	conformal weights. The Virasoro Jacobi identity
  1990	(associativity of the OPE) forces all higher-weight deformations
  1991	within $\ChirHoch^2$ to vanish: there is no independent weight-$4$
  1992	deformation, no weight-$6$ deformation, etc.
  1993	\end{proof}
  1994	
  1995	The $\mathfrak{sl}_2$ computation in Part~(ii) already exhibits the
  1996	essential phenomenon: the first chiral Hochschild group
  1997	$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
  1998	This is not a coincidence special to rank one. For any simple Lie
  1999	algebra, the affine vertex algebra $V_k(\fg)$ at generic level is
 succeeded in 50ms:
chapters/connections/concordance.tex:7:disagree, this chapter governs. It records the five main theorems
chapters/connections/concordance.tex:23:\noindent\textbf{The five main theorems.}\quad
chapters/connections/concordance.tex:77:Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
chapters/connections/concordance.tex:121: modular Koszul algebras (Theorem~H).
chapters/connections/concordance.tex:160:complementarity (Theorem~C).
chapters/connections/concordance.tex:454:Theorem~A establishes $\tau$; Theorem~B inverts it;
chapters/connections/concordance.tex:455:Theorem~C identifies its genus-$g$ curvature; Theorem~D computes
chapters/connections/concordance.tex:564:Our Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the
chapters/connections/concordance.tex:587: with moduli space integrals and the Hodge bundle (Theorem~C)
chapters/connections/concordance.tex:596:Theorem~A produces two functors, not one:
chapters/connections/concordance.tex:601:The first recovers $\cA$ (bar-cobar inversion, Theorem~B);
chapters/connections/concordance.tex:858:\textup{(}Theorem~D\textup{)}, the cubic shadow
chapters/connections/concordance.tex:972: Lift the complementarity theorem (Theorem~C) to a statement
chapters/connections/concordance.tex:1365:The five main theorems~A--D,\,H and the bar-intrinsic MC
chapters/connections/concordance.tex:1398:is revised or retracted. The five main theorems~A--D,\,H and
chapters/connections/concordance.tex:1423: $D^2 = 0$ and all five main theorems unaffected \\
chapters/connections/concordance.tex:2037: Theorem~C from additive splitting to shifted-symplectic
chapters/connections/concordance.tex:2326:The five main theorems establish \emph{existence of duality}.
chapters/connections/concordance.tex:2335:\index{five main theorems!as MC projections}
chapters/connections/concordance.tex:3534:\index{five main theorems!E1@$E_1$ variant!concordance}
 succeeded in 51ms:
  2480	 that propagates $\Theta_\cA$ to Volume~II and Volume~III.
  2481	\end{enumerate}
  2482	
  2483	Thirty-two chapters, one protagonist. The five theorems A/B/C/D/H
  2484	and the four depth classes G/L/C/M mark its landmarks; the remainder
  2485	test, project, and extend it.
  2486	
  2487	The formal definitions of $\Einf$-chiral, $\Eone$-chiral, and $\Pinf$-chiral algebras, the four Koszul duality mechanisms, the anomaly ratio, the Koszul conductor, and the Koszul spectrum appear in Chapter~\ref{ch:algebraic-foundations}.
  2488	
  2489	% ================================================================
  2490	% Stub labels for external cross-references from body chapters.
  2491	% These labels were defined in material that has been relocated
  2492	% from this introduction to the relevant body chapters.
  2493	% ================================================================
  2494	\phantomsection\label{def:modular-homotopy-theory-intro}%
  2495	\phantomsection\label{eq:all-degree-master-eq-intro}%
  2496	\phantomsection\label{eq:arnold-seed}%
  2497	\phantomsection\label{eq:bar-graded-object-intro}%
  2498	\phantomsection\label{eq:the-seed}%
  2499	\phantomsection\label{eq:universal-MC}%
 succeeded in 51ms:
337:| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
351:| `thm:hochschild-polynomial-growth` | `theorem` | 689 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
420:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3394 | Geometric bar--cobar duality |
708:| `thm:quantum-complementarity-main` | `theorem` | 435 | Quantum complementarity as Lagrangian polarization |
761:| `thm:higher-genus-inversion` | `theorem` | 4082 | Higher genus inversion |
807:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2562 | Bar-cobar isomorphism, retained for equation labels |
827:| `thm:genus-universality` | `theorem` | 5243 | Genus universality |
878:| `thm:modular-characteristic` | `theorem` | 2543 | Modular characteristic |
1114:| `thm:virasoro-hochschild` | `theorem` | 104 | Virasoro Hochschild cohomology |
1115:| `thm:w-algebra-hochschild` | `theorem` | 188 | W-algebra Hochschild cohomology |
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2380,2495p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2380	 (Gaussian) for the heteromorphic sublattice.
  2381	
  2382	\item \emph{Free fields and Heisenberg} (Ch.~\ref{chap:free-fields}).
  2383	 Heisenberg, free fermion, Eisenstein genus expansion. Depth class
  2384	 G: the unique termination at $r_{\max} = 2$ with
  2385	 $\Theta_\cA$ scalar-saturated.
  2386	
  2387	\item \emph{$\beta\gamma$ system} (Ch.~\ref{chap:beta-gamma}).
  2388	 First non-abelian bar complex; $\mu_{\beta\gamma} = 0$; shadow
  2389	 terminates at degree~$4$. Depth class C (contact), the unique
  2390	 termination at $r_{\max} = 4$.
  2391	
  2392	\item \emph{Kac--Moody} (Ch.~\ref{chap:kac-moody}).
  2393	 $\widehat{\mathfrak{g}}_k$ bar complex; Feigin--Frenkel as
  2394	 Koszul duality; PBW at all genera. Depth class L (Lie/tree),
  2395	 $r_{\max} = 3$; $\Theta_\cA$ projects to $\kappa$ and the cubic
  2396	 shadow $\mathfrak C$, no higher.
  2397	
  2398	\item \emph{$\mathcal W$-algebras} (Ch.~\ref{chap:w-algebras}).
  2399	 Drinfeld--Sokolov reduction as a Koszul functor; $\mathcal{W}_3$



thinking
**Identifying inconsistencies in the theorem**

I’m noticing that the flag theorem stub is definitely an issue. I’ll need to inspect the concordance lines around 454-455 to see if there's a misstatement regarding theorem C and D. The user is interested in inconsistencies, particularly between the introduction summaries and the actual theorem statements. 

I’ll compare the summary in the introduction with the actual theorems to identify any mismatches. It seems there might be a false advertisement related to the theorem environment, which needs correcting.
thinking
**Proposing precise fixes for the theorem**

I’m considering a specific fix for the inconsistencies found. I could suggest replacing “Theorem\ref{thm:modular-koszul-duality-main} (the flag theorem)” with “The Introduction's synthesis around Theorems A–D and H,” unless a proper theorem environment is set up. Well, I think I need to go for the minimal truthful fix by saying either restore the theorem environment with a precise statement and claim status, or delete the relevant language from the concordance. 

It may also be important to include line numbers for reference in both files.
thinking
**Clarifying the findings**

I could mention both file lines in the problem and fix sections, referring to one file:line format. The issue could be identified at concordance line 77 or introduction line 2508. It might be helpful to separate this into two findings—one noting that the concordance mis-cites the theorem and the other highlighting that the introduction has a stub. However, since both are about the same seam, I’ll consider if presenting them together makes more sense.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '68,90p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '446,462p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '818,834p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '344,366p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4748,4768p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   818	\item \emph{Holographic sum rule}
   819	 \textup{(}Theorem~C\textup{)}.
   820	 For each standard family, the modular characteristic of the
   821	 boundary and its Koszul dual sum to a family-specific Koszul
   822	 conductor,
   823	 $\kappa(\cA) + \kappa(\cA^!) = K_\cA$:
   824	 $K = 0$ for Heisenberg and affine Kac--Moody at the linear
   825	 level, $K = 13$ for Virasoro (self-dual at $c = 13$), with
   826	 family-dependent nonzero values for the principal
   827	 $\mathcal{W}$-algebras
   828	 (Theorem~\ref{thm:central-charge-complementarity}). The
   829	 sum rule is a family-specific holographic conservation law,
   830	 not a universal constant. Theorem~C part~(1) (eigenspace
   831	 decomposition under the Verdier involution) is
   832	 unconditional; part~(2) (scalar sum rule) is proved on the
   833	 uniform-weight lane.
   834	
 succeeded in 51ms:
   446	\end{remark}
   447	
   448	\begin{remark}[The twisting morphism as organizing datum]
   449	\label{rem:tau-protagonist}
   450	\index{twisting morphism!as organizing datum}
   451	The canonical twisting morphism $\tau \colon \barB_X(\cA) \to \cA$
   452	underlies the four main theorems
   453	(Convention~\ref{conv:bar-coalgebra-identity}):
   454	Theorem~A establishes $\tau$; Theorem~B inverts it;
   455	Theorem~C identifies its genus-$g$ curvature; Theorem~D computes
   456	its leading coefficient.
   457	At higher genus, $\tau$ extends to a curved twisting cochain
   458	$\tau_{\mathrm{mod}} = \tau + \Theta_\cA$
   459	whose curvature $\kappa(\cA)\cdot\omega_g$ governs the entire
   460	modular deformation tower
   461	(Remark~\ref{rem:theta-modular-twisting}).
   462	\end{remark}
 succeeded in 51ms:
    68	 \textup{(}Thms~\ref{thm:w-algebra-hochschild},
    69	 \ref{thm:virasoro-hochschild},
    70	 \ref{thm:critical-level-cohomology};
    71	 Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
    72	 & \ClaimStatusProvedHere
    73	\end{tabular}
    74	\end{center}
    75	
    76	\noindent
    77	Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
    78	in the Introduction unifies them.
    79	
    80	\medskip\noindent
    81	All five descend from a single object. The modular $L_\infty$
    82	convolution algebra
    83	$\mathfrak{g}^{\mathrm{mod}}_\cA$ carries its $L_\infty$
    84	structure from the Feynman transform of the modular operad;
    85	the dg~Lie algebra of Definition~\ref{def:modular-convolution-dg-lie}
    86	is its strict model $\Convstr$, and the homotopy-invariant object
    87	is $\Definfmod(\cA)$
 succeeded in 51ms:
  4748	 & Chain-level modular functor & Structural \\
  4749	 & & (Thm~\ref{thm:chain-modular-functor}) & \\
  4750	\bottomrule
  4751	\end{tabular}
  4752	\end{center}
  4753	Theorem~D is the \emph{integrability condition}:
  4754	$\mathrm{obs}_g = \kappa \cdot \lambda_g$ is, for uniform-weight
  4755	algebras, a pure
  4756	tautological class, free of boundary or non-tautological
  4757	contributions, guaranteeing that the curvature of the genus-$g$
  4758	bar complex is absorbable by a period correction.
  4759	For arbitrary modular Koszul algebras, the unconditional part of
  4760	Theorem~D is the genus-$1$ identity
  4761	$\mathrm{obs}_1 = \kappa\lambda_1$; the scalar formula
  4762	\emph{fails} at $g \geq 2$ for multi-weight algebras
  4763	(Theorem~\ref{thm:multi-weight-genus-expansion}).
  4764	The corrected complex $(\barB^{(g)}, \Dg{g})$ with
  4765	$\Dg{g}^{\,2} = 0$ (Level~$1$) is the
  4766	\emph{derived fiber} of the factorization homology bundle
  4767	$\int_{\Sigma_g}\!\cA$ over~$\mathcal{M}_g$; its variation
 succeeded in 51ms:
   344	the shadow obstruction tower~$\{S_r(\cA)\}_{r \ge 2}$ is the holographic
   345	correction hierarchy; and the Drinfeld double
   346	$U_\cA = \cA \bowtie \cA^!$ is the universal boundary-bulk algebra.}
   347	The bar complex computes the boundary $\mapsto$ bulk transform; the
   348	cobar inverts it on the Koszul locus.
   349	Each theorem isolates one structural property of this transform.
   350	Theorem~A constructs the bar-cobar adjunction and its Verdier intertwining
   351	(Definition~\ref{def:chiral-koszul-pair}).
   352	Theorem~B inverts the transform: at genus~$0$ via chiral
   353	Koszulity (Theorem~\ref{thm:koszul-equivalences-meta}),
   354	at genus~$g \ge 1$ via the inductive genus step.
   355	Theorem~C constrains the Koszul dual pair by a family-specific sum rule:
   356	$\kappa(\cA) + \kappa(\cA^!) = K_\cA$, where $K = 0$ for affine
   357	Kac--Moody and free fields and $K = 13$ for Virasoro
   358	(self-dual at $c = 13$).
   359	Theorem~D identifies $\kappa$
   360	as the one-loop coefficient of the bulk partition
   361	function on the uniform-weight lane; the multi-weight
   362	correction $\delta F_g^{\mathrm{cross}}$ at $g \ge 2$ is a
   363	separate higher-loop contribution.


thinking
**Analyzing theorem misstatements**

I've noticed that the concordance lines misstate theorem C as genus-g curvature and theorem D as leading coefficient. Actually, theorem C should refer to Lagrangian decomposition, while theorem D involves curvature. The relation seems off too—line 455 suggests theorem C identifies genus-g curvature, but it doesn’t. I think I need to swap the theorem labels: “Theorem C splits the genus-g projection into complementary Lagrangians; Theorem D should identify the genus-g scalar curvature and its leading coefficient kappa.” I've also spotted a status mismatch with theorem H that needs attention!
thinking
**Reviewing Theorem H status**

The concordance table states that Theorem H includes the statement about `thm:critical-level-cohomology` being fully proved here, but it actually says `ClaimStatusProvedElsewhere` in a reference. This could mislead since it implies that Theorem H is completely proved here. I wonder if this theorem should actually reference another theorem that's cited elsewhere. The table summarizes theorem H in terms of polynomial growth, but it seems `thm:critical-level-cohomology` isn't part of it. I need to double-check the context around lines 62-71 for clarity!
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '7178,7198p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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



thinking
**Checking theorem statement**

I need to verify if the theorem statement matches the "iff Borcherds identity." I'm considering whether it aligns correctly. There’s a chance it could be a match, but I'm also wondering if it might not seem quite right. So, I'll take a closer look and see if there's any discrepancies or confirmations to make about this identity. It's essential to get this sorted out accurately!
thinking
**Evaluating theorem clarity**

I need to inspect the body of the theorem because it seems somewhat incomplete with its statement, particularly around "if and only if". The user mentioned that every theorem is advertised in the introduction, but I'm finding it doesn't quite match the labeling in the body. I should focus on the main theorem and any obvious discrepancies, perhaps looking for subtle issues with references and statuses. Also, I should check if the introduction's five theorems align with their respective labels in the body.
thinking
**Inspecting unresolved labels**

I need to take a closer look at the unresolved label `thm:ds-hpl-transfer`. It seems important, so I'll search through the introduction for context between 2008 and 2018. There might be crucial details there that could clarify things. I want to ensure I'm thorough; unexpected things often crop up in that timeframe. Let's see what I can find that helps make sense of this label and any related content.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '2002,2020p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2002	\begin{enumerate}[label=\textup{(\alph*)}]
  2003	\item \emph{The $\mathcal W$-algebra axis.}
  2004	 Completed Koszulity is ubiquitous: every affine $\mathcal W$-algebra
  2005	 at generic level is completed Koszul. Strict Koszulity is
  2006	 exceptional: the subregular family $\mathcal W_n^{(2)}$ has
  2007	 unbounded canonical homotopy degree, and the classical $W_3$ sector
  2008	 defines the first finite-degree modular higher-spin package.
  2009	 MC4 is proved: the strong completion-tower theorem
  2010	 (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
  2011	 completion-closed bar-cobar homotopy equivalence on $\CompCl(\Fft)$,
  2012	 with automatic continuity via the degree cutoff
  2013	 (Lemma~\ref{lem:degree-cutoff}) and coefficient-stability criterion
  2014	 (Theorem~\ref{thm:coefficient-stability-criterion}).
  2015	 The DS-HPL transfer theorem
  2016	 (Volume~II, Theorem~\ref{thm:ds-hpl-transfer}) closes the
  2017	 local nonlinear bridge from affine to $\mathcal{W}$-algebra
  2018	 data: homological perturbation through the BRST SDR transfers
  2019	 the full dg-shifted Yangian triple, with the gravitational
  2020	 coproduct proved strictly primitive at all degrees

thinking
**Evaluating mathematical theorem**

I’m looking at lines 47-57, where it says that \( (d_{fib}^{ord})^2 = r_A(z) \cdot \omega_g \) averages to \( d_{fib}^2 = \kappa(A) \cdot \omega_g \), which refers to the "Theorem modular-characteristic". However, the actual theorem doesn’t mention the matrix-valued ordered equation. It only covers scalars. I’m wondering if the ordered equation comes from the E1 theorem or a prelude. I should check to see if it's proven elsewhere, particularly in E1.
exec
/bin/zsh -lc "rg -n '\\\\label\\{op:multi-generator-universality\\}|multi-generator-universality' chapters/theory chapters/connections metadata | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_open_closed_realization.tex:1197: \textup{(}\textbf{op:multi-generator-universality}, resolved
chapters/connections/editorial_constitution.tex:2667:4 & Universal char.\ package & \textbf{Core proved with one repaired gap}: standard landscape (Cor.~\ref{cor:effective-quadruple}) gives the effective \(\Gamma\)-quadruple, generic cyclic rigidity (Thm~\ref{thm:cyclic-rigidity-generic}) and algebraic-family rigidity at all non-critical levels (Thm~\ref{thm:algebraic-family-rigidity}) give vanishing primitive tangent space and level-direction concentration, and the repaired equivalence (Prop.~\ref{prop:saturation-equivalence}) matches that weaker statement; the strong scalar identity $\Theta_{\cA}^{\min}=\kappa(\cA)\eta\otimes\Lambda$ is proved on the uniform-weight lane and \emph{fails} for multi-weight families: the genus-$g$ free energy receives a cross-channel correction (Theorem~\ref{thm:multi-weight-genus-expansion}, resolving Open Problem~\ref{op:multi-generator-universality} negatively); functoriality (Prop.~\ref{prop:saturation-functorial}) is one-channel generically and scalar only on the proved lane; $\Pi_{\cA}$ sharp open \\
chapters/theory/higher_genus_modular_koszul.tex:2686: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
chapters/theory/higher_genus_modular_koszul.tex:2701: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
chapters/theory/higher_genus_modular_koszul.tex:2737:Theorem~\ref{thm:multi-generator-universality}.
chapters/theory/higher_genus_modular_koszul.tex:2962:Theorem~\ref{thm:multi-generator-universality}.
chapters/theory/higher_genus_modular_koszul.tex:20505:Theorem~\textup{\ref{thm:multi-generator-universality}} is
chapters/theory/higher_genus_modular_koszul.tex:21786:\label{thm:multi-generator-universality}
chapters/theory/higher_genus_modular_koszul.tex:21874:Problem~\textup{\ref{op:multi-generator-universality}} in
chapters/theory/higher_genus_modular_koszul.tex:22122:Open Problem~\textup{\ref{op:multi-generator-universality}}
chapters/theory/higher_genus_modular_koszul.tex:24163:(Open Problem~\textup{\ref{op:multi-generator-universality}} is
chapters/theory/higher_genus_modular_koszul.tex:24880:(Open Problem~\ref{op:multi-generator-universality}, resolved
chapters/theory/higher_genus_modular_koszul.tex:25131:Problem~\textup{\ref{op:multi-generator-universality}} in
chapters/connections/genus_complete.tex:204:the Hodge class on $\overline{\mathcal{M}}_g$. For multi-weight algebras at $g \geq 2$, the identification $\Gamma_\cA = \kappa(\cA)\Lambda$ fails: the free energy receives a cross-channel correction (Theorem~\ref{thm:multi-weight-genus-expansion}, resolving Problem~\ref{op:multi-generator-universality} negatively). The full MC equation
chapters/theory/higher_genus_foundations.tex:598: \textup{(}Theorem~\textup{\ref{thm:multi-generator-universality})}.
chapters/theory/higher_genus_foundations.tex:5009:Open Problem~\textup{\ref{op:multi-generator-universality}} resolved
chapters/theory/higher_genus_foundations.tex:5041:Open Problem~\ref{op:multi-generator-universality} resolved
chapters/theory/higher_genus_foundations.tex:5045:% Open Problem~\ref{op:multi-generator-universality}.
chapters/theory/higher_genus_foundations.tex:5183:Theorem~\ref{thm:multi-generator-universality}.
chapters/theory/higher_genus_foundations.tex:5317:Theorem~\ref{thm:multi-generator-universality}.
codex
A deeper inconsistency just surfaced in Theorem H’s introduction prose. The intro says “total dimension at most four,” but the body also states `\ChirHoch^1(V_k(\mathfrak g)) \cong \mathfrak g`, which forces total dimension `\dim(\mathfrak g)+2` for affine KM, not `≤4`. I’m checking where that bad bound propagates so I can pin every seam break precisely.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '660,686p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'at most four|dim.*4|total dimension at most four|dim \\\\leq 4|dim\\\\leq 4' chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/chiral_center_theorem.tex chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4298,4320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'dim\\(g\\)\\+2|dim\\(\\\\fg\\)\\+2|total dim|ChirHoch\\"'^1'"\\(V_k|degree-1 group is identified with the Lie algebra' chapters/theory chapters/connections CLAUDE.md AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   660	 (Remark~\ref{rem:four-levels}); the bundle
   661	 itself (its fibers, flat connection, and modular
   662	 functor structure) is the full modular homotopy invariant
   663	 (Conjecture~\ref{conj:categorical-modular-kd}).
   664	
   665	\item \emph{Theorem~H} (Chiral Hochschild cohomology,
   666	 Theorem~\ref{thm:hochschild-polynomial-growth}).
   667	 The \emph{chiral Hochschild cohomology}
   668	 $\ChirHoch^*(\cA)$ is the cohomology of the complex
   669	 $\operatorname{CoDer}(\barB(\cA))$
   670	 (coderivations of the bar coalgebra, with differential
   671	 induced by the bar differential); it is canonically
   672	 identified with the chiral derived centre
   673	 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, the bulk algebra
   674	 of the boundary-bulk reconstruction.
   675	 On the Koszul locus,
   676	 $\ChirHoch^*(\cA)$ is polynomial and dual
   677	 to $\ChirHoch^*(\cA^!)$, with cohomological amplitude
   678	 $[0, 2]$ and total dimension at most four.
   679	 The concentration in degrees $\{0,1,2\}$ is the
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:2084:$\dim \ChirHoch^*(\cA) \leq 4$ (which holds for the Heisenberg and
chapters/theory/chiral_hochschild_koszul.tex:3890:Now $\dim V_{r,s,\,[k]}$ is the coefficient of $q^{h_{r,s} + k - c/24}$ in
chapters/theory/chiral_hochschild_koszul.tex:4123:$\dim H^n(\bar{B}^{\mathrm{ch}}_{[h+24]}) = \dim H^n(\bar{B}^{\mathrm{ch}}_{[h]})$
chapters/theory/introduction.tex:365:Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
chapters/theory/introduction.tex:678: $[0, 2]$ and total dimension at most four.
chapters/theory/introduction.tex:680: sharp statement; the bound $\dim \leq 4$ is a
chapters/connections/concordance.tex:4196:the sunset~$C$ (codim~$2$, weight~$S_4$),
chapters/connections/concordance.tex:6639: twist operator dimension (Calabrese--Cardy~\cite{Calabrese-Cardy04}).
chapters/connections/concordance.tex:8454:($\dim S_{12}(\mathrm{Sp}(4,\bZ)) = 1$, no ambiguity).
 succeeded in 50ms:
  4298	and $\ell_3^{(1)} \approx \kappa$ (approximate).
  4299	Full Pixton ideal generation at rank~$2$ requires
  4300	the strata algebra of $\overline{\mathcal{M}}_{2,1}$
  4301	at rank~$2$.
  4302	\end{remark}
  4303	
  4304	
  4305	\paragraph{Chiral Hochschild descent lemma.}
  4306	Lemma~\ref{lem:chirhoch-descent} records an explicit step
  4307	in the proof of Theorem~H: the chiral Hochschild complex
  4308	$\ChirHoch^{\bullet}(\cA)$ arises as the $\Sigma$-coinvariant
  4309	descent of the bar complex along Verdier intertwining,
  4310	$\ChirHoch^{\bullet}(\cA) \cong
  4311	(\mathbb{D}_{\Ran}\barB(\cA))_{\Sigma}$,
  4312	on the Koszul locus. This identification was implicit in
  4313	the original Theorem~H proof; the lemma makes it citable
  4314	as a primitive step (A2).
  4315	
  4316	\paragraph{Closure properties of chiral Koszulness.}
  4317	Proposition~\ref{prop:koszul-closure-properties} consolidates
 succeeded in 50ms:
AGENTS.md:153:Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.
AGENTS.md:559:| ChirHoch^1 KM | PROVED | = g; total dim = dim(g)+2 |
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
chapters/connections/thqg_symplectic_polarization.tex:680:$g \ge 1$, the total dimension
chapters/theory/higher_genus_modular_koszul.tex:32487:The total dimension is $6 \cdot 3 = 18$.
chapters/theory/en_koszul_duality.tex:2774: degrees $\{0, 1, 2\}$ with total dimension at most four on
chapters/theory/en_koszul_duality.tex:3813:with total dimension $1 + 3 + 1 = 5$. Write $\mathbf{1}$
chapters/theory/en_koszul_duality.tex:5805:$\ChirHoch^1(V_k(\fsl_2)) \cong \fsl_2$, see
chapters/theory/bar_cobar_adjunction_inversion.tex:4171:$\dim E_1^{0,p}$ bounded by the total dimension at
chapters/theory/higher_genus_foundations.tex:2759:The universal family over $\overline{\mathcal{M}}_g$ with fiber $\overline{C}_n(\Sigma_g)$ has total dimension $(3g-3) + n$, which equals $\dim \overline{\mathcal{M}}_{g,n}$. Indeed, $\overline{\mathcal{M}}_{g,n}$ can be identified with this universal configuration space.
chapters/theory/introduction.tex:365:Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
chapters/theory/introduction.tex:678: $[0, 2]$ and total dimension at most four.
chapters/theory/introduction.tex:684: algebra: $\ChirHoch^1(V_k(\fg)) \cong \fg$
chapters/theory/introduction.tex:854: has cohomological amplitude $[0, 2]$ and total dimension at
chapters/theory/e1_modular_koszul.tex:992:degrees $\{0,1,2\}$ with total dimension~$3$).
chapters/theory/e1_modular_koszul.tex:1301:contributes the Arnold algebra of total dimension~$n!$.
chapters/theory/chiral_hochschild_koszul.tex:4810:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
chapters/connections/concordance.tex:67: $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
chapters/connections/concordance.tex:387: $\ChirHoch^1(V_k(\fg)) \cong \fg$
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1870,2095p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
  1870	 $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)
  1871	 \cong \bC \oplus \bC[-1] \oplus \bC[-2]$.
  1872	
  1873	\item \textup{(Affine $\widehat{\mathfrak{sl}}_2$ at level~$k \neq -2$.)}
  1874	 At generic \textup{(}non-critical\textup{)} level:
  1875	 \[
  1876	 \ChirHoch^0 = \bC, \qquad
  1877	 \ChirHoch^1 \cong \mathfrak{sl}_2, \qquad
  1878	 \ChirHoch^2 = \bC, \qquad
  1879	 \ChirHoch^n = 0 \text{ for } n \geq 3.
  1880	 \]
  1881	 Thus the total dimension is~$5$. In particular, the older
  1882	 conjectural total bound~$4$ does not hold for affine
  1883	 $\widehat{\mathfrak{sl}}_2$; the uniform statement is the
  1884	 concentration in degrees $\{0,1,2\}$.
  1885	 The three-dimensional $\ChirHoch^1$ consists of the outer derivations
  1886	 of~$\widehat{\mathfrak{sl}}_{2,k}$:
  1887	 the current algebra deformations $J^a \mapsto J^a + \epsilon\, \phi^a$
  1888	 parametrized by $\mathfrak{sl}_2$ itself.
  1889	 The level-independence of these dimensions at generic~$k$
exec
/bin/zsh -lc "rg -n 'central-charge-complementarity' metadata/theorem_registry.md metadata/claims.jsonl metadata/label_index.json" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/theorem_registry.md:1132:| `thm:central-charge-complementarity` | `theorem` | 908 | Central charge complementarity |
metadata/label_index.json:45862:  "thm:central-charge-complementarity": {
metadata/claims.jsonl:503:{"label": "prop:virasoro-c26-selfdual", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/poincare_computations.tex", "line": 161, "title": "Virasoro NAP duality at \\texorpdfstring{$c=26$}{c=26}", "refs_in_block": ["thm:central-charge-complementarity"]}
metadata/claims.jsonl:1240:{"label": "thm:complementarity-root-datum", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/genus_expansions.tex", "line": 3099, "title": "Complementarity sum as root datum invariant", "labels_in_block": ["thm:complementarity-root-datum", "eq:wn-kappa-sum-general", "eq:general-w-kappa-sum"], "refs_in_block": ["thm:central-charge-complementarity"]}
metadata/claims.jsonl:1309:{"label": "prop:admissible-verlinde-bar", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/examples/kac_moody.tex", "line": 3117, "title": "Admissible \\texorpdfstring{$S$}{S}-matrix and Verlinde fusion package at \\texorpdfstring{$k=-1/2$}{k=-1/2}", "labels_in_block": ["prop:admissible-verlinde-bar", "eq:admissible-s-matrix", "eq:admissible-fusion"], "refs_in_block": ["thm:kw-bar-spectral", "thm:central-charge-complementarity"], "cites_in_block": ["KW88"]}
metadata/claims.jsonl:2432:{"label": "cor:level-shifting-part1", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/theory/cobar_construction.tex", "line": 2199, "title": "Level-shifting via Verdier duality", "labels_in_block": ["cor:level-shifting-part1", "eq:level-shifting-part1"], "refs_in_block": ["thm:bar-cobar-isomorphism-main", "conv:bar-coalgebra-identity", "prop:km-bar-curvature", "thm:central-charge-complementarity"]}
metadata/claims.jsonl:3117:{"label": "conj:boundary-bulk-thesis", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/theory/introduction.tex", "line": 648, "title": "The boundary-bulk reconstruction thesis", "refs_in_block": ["def:chiral-koszul-pair", "thm:koszul-equivalences-meta", "thm:central-charge-complementarity", "rem:two-critical-points", "ch:derived-langlands", "princ:five-facets"]}
metadata/claims.jsonl:3119:{"label": "thm:central-charge-complementarity", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/introduction.tex", "line": 908, "title": "Central charge complementarity", "refs_in_block": ["conv:regime-tags"]}



thinking
**Inspecting theorem discrepancies**

I need to check if the registry line numbers are matching with the current file due to shifts. It might be worthwhile to inspect the summary around theorem H for any contradictions. I see lines 64-71 could be relevant for citation. There's a potential inconsistency where the introduction states that theorem H applies to the "Koszul locus" at amplitude [0,2], but the theorem actually accommodates any chiral Koszul algebra, independent of a generic level. Interestingly, the intro mentions the generic-level qualifier earlier, but this is necessary for the affine KM proposition, not for theorem H itself.
thinking
**Clarifying theorem references**

I see a potential issue in the introduction where line 355 mentions Theorem C instead of D, which I've already caught. Then, in the concordance table, lines 47-58 reference `Definition\ref{def:scalar-lane}` for all genera, which seems correct. However, Theorem D says `obs_g = κ λ_g` for uniform-weight modular Koszul algebras and correctly aligns with the Faber-Pandharipande free-energy formula as stated. Then, line 606-607 of the introduction mentions that their intersection is the center Z(A), which also appears in actual Theorem C from lines 593-606. This overlap indicates coherence!
thinking
**Reviewing theorem C details**

I just realized that the actual body of Theorem C doesn’t say that the intersection is the center Z(A). Instead, it discusses cohomological shadows as eigenspaces of sigma and mentions the direct sum. This observation is crucial, as it highlights any misinterpretation I might have had. I need to make sure that the definitions and statements align correctly, especially when analyzing the concepts discussed in the theorem. It's a bit of a revelation!
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '586,608p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   586	 $Z(\cA|_{\Sigma_g})$ (the commutant of~$\cA$ acting on
   587	 itself via the chiral bracket).
   588	 The \emph{ambient complex}
   589	 $\mathbf{C}_g(\cA) := R\Gamma(\overline{\mathcal{M}}_g,
   590	 \mathcal{Z}_\cA)$
   591	 (derived global sections of this local system)
   592	 carries a shifted-symplectic pairing from Verdier duality.
   593	 The Verdier involution decomposes it
   594	 into \emph{complementary Lagrangians}
   595	 $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$:
   596	 the $+1$ and $-1$ eigenspaces of the involution
   597	 (Definition~\ref{def:complementarity-complexes}).
   598	 At the cohomological level,
   599	 \begin{equation}\label{eq:complementarity-intro}
   600	 Q_g(\cA) \oplus Q_g(\cA^!) \cong
   601	 H^*(\overline{\mathcal{M}}_g, \mathcal{Z}_\cA).
   602	 \end{equation}
   603	 The anomaly of one algebra is the ghost-number violation of
   604	 its dual.
   605	
codex
The theorem C surface has another subtle failure. The intro states that the `+1` and `-1` Verdier eigenspaces intersect in the center, but the body theorem presents them as a direct-sum eigenspace decomposition. In characteristic `0`, those eigenspaces intersect trivially, so I’m checking whether this bad “intersection = center” slogan appears anywhere else or is confined to the intro seam.
exec
/bin/zsh -lc "rg -n 'intersection is the center|Their intersection is the center|\\+1.*-1 eigenspaces.*center|eigenspaces.*center' chapters/theory/introduction.tex chapters/connections/concordance.tex chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\mathbf\\{Q\\}_g\\(\\\\cA\\) \\\\oplus \\\\mathbf\\{Q\\}_g\\(\\\\cA\\"'^!'"\\)|Q_g\\(\\\\cA\\) \\\\oplus Q_g\\(\\\\cA\\"'^!'"\\)|ker\\(\\\\sigma - \\\\mathrm\\{id\\}\\)|ker\\(\\\\sigma \\+ \\\\mathrm\\{id\\}\\)' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex:606: The shifted-symplectic structure is a $(-(3g{-}3))$-shifted symplectic form on the derived moduli of genus-$g$ bar families, in the sense of Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The complementary Lagrangians~$Q_g(\cA)$ and~$Q_g(\cA^!)$ are the $\pm 1$ eigenspaces of the Verdier involution~$\sigma = \mathbb{D}_{\operatorname{Ran}}$ acting on~$\mathbf{C}_g(\cA)$. Their intersection is the center~$Z(\cA)$; the ambient complex is the direct sum.
 succeeded in 51ms:
63:where $Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
64:$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$ are the eigenspaces of
237: $H^*(V) = \ker(\sigma - \mathrm{id}) \oplus \ker(\sigma + \mathrm{id})$.
513:$Q_g(\cA) = \ker(\sigma - \mathrm{id})$ and
514:$Q_g(\cA^!) = \ker(\sigma + \mathrm{id})$
2075: $C_g = Q_g(\cA) \oplus Q_g(\cA^!)$
2735:complementarity decomposition $Q_g(\cA) \oplus Q_g(\cA^!)
2994:$Q_g(\cA) \oplus Q_g(\cA^!)$ becomes a balanced decomposition
4530:$Q_g(\cA) \oplus Q_g(\cA^!) \cong H^*(\overline{\mathcal{M}}_g, Z(\cA))$.
5819: $\mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)
exec
/bin/zsh -lc "rg -n 'center local system|complementary Lagrangians|Verdier involution decomposes|Q_g\\(\\\\cA\\) \\oplus Q_g\\(\\\\cA\\"'^!'"\\)' chapters/connections/concordance.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:center local system|complementary Lagrangians|Verdier involution decomposes|Q_g\(\\cA\) \oplus Q_g\(\\cA\^!\))
                                                                                               ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1028,1072p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1028	\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]\label{thm:central-charge-complementarity}
  1029	\index{central charge!complementarity|textbf}
  1030	\textup{[Regime: curved-central on the Koszul locus
  1031	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1032	
  1033	For Koszul dual pairs related by the Feigin--Frenkel involution
  1034	$k \mapsto k' = -k - 2h^\vee$:
  1035	\begin{enumerate}
  1036	\item[\textup{(a)}] \emph{Affine Kac--Moody.}
  1037	 $c(\widehat{\mathfrak{g}}_k) + c(\widehat{\mathfrak{g}}_{k'})
  1038	 = 2 \dim \mathfrak{g}$.
  1039	\item[\textup{(b)}] \emph{Principal $\mathcal{W}$-algebras:}
  1040	 $c(\mathcal{W}^k(\mathfrak{g})) + c(\mathcal{W}^{k'}(\mathfrak{g}))
  1041	 = 2\operatorname{rank}(\mathfrak{g}) + 4h^\vee \dim \mathfrak{g}$.
  1042	\end{enumerate}
  1043	In particular, $\mathfrak{g} = \mathfrak{sl}_2$ in
  1044	part~\textup{(b)} gives $c + c' = 26$.
  1045	\end{theorem}
  1046	
  1047	\begin{proof}


thinking
**Evaluating central charge citations**

I realize the theorem on central-charge-complementarity is focused on central charges. In the boundary-bulk thesis, it seems that citing it for the kappa sum is inaccurate because it applies differently across various algebra families. Specifically, the kappa sum should be based on the root-datum theorem or the duality clause instead. I think a good fix would be to replace the citation with Theorem references and clarify that the main decomposition comes from Theorem D. It’s all connected, making me consider potential findings in the thesis.
thinking
**Clarifying theorem citations**

I noticed that part (a) of `thm:central-charge-complementarity` says `c+c'=2 dim g`, not zero, which is important because line 823 references kappa instead of c. Citing this theorem could be misleading. In potential finding 34, I see that the concordance table for theorem H mentions critical-level cohomology, which is noted as `ProvedElsewhere`, and it’s also clear that theorem H deals with generic-level, not critical-level. Moving on to potential finding 35, I’ll need to check the dimensions discussed in lines 365, 678, and 854-855.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '848,856p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   848	 stated form.
   849	
   850	\item \emph{Holographic tightness}
   851	 \textup{(}Theorem~H\textup{)}.
   852	 At generic level and on the Koszul locus, the bulk algebra
   853	 $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) = \ChirHoch^*(\cA)$
   854	 has cohomological amplitude $[0, 2]$ and total dimension at
   855	 most four. The generic-level hypothesis excludes the
   856	 critical level $k = -h^\vee$ for affine Kac--Moody, where
exec
/bin/zsh -lc "rg -n --fixed-strings '\\label{thm:ds-hpl-transfer}' /Users/raeez/chiral-bar-cobar-vol2 2>/dev/null | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2652:\ClaimStatusProvedHere]\label{thm:ds-hpl-transfer}

thinking
**Inspecting citation issues**

I'm noting that this is a cross-volume reference that isn't resolvable in Volume I. I need to find an exact fix, like using plain text or a dedicated citation scheme for cross-volume references. 

Then there's Potential Finding 45: it might be necessary to check the theorem registry to see if `thm:modular-koszul-duality-main` is missing. I should perform a search for that.
exec
/bin/zsh -lc "rg -n 'modular-koszul-duality-main' metadata/theorem_registry.md metadata/claims.jsonl metadata/label_index.json" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/claims.jsonl:2939:{"label": "thm:shadow-archetype-classification", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 16007, "title": "Shadow archetype classification", "refs_in_block": ["def:shadow-depth-classification", "cor:nms-betagamma-mu-vanishing", "thm:w-virasoro-quintic-forced", "prop:propagator-variance", "thm:modular-koszul-duality-main", "fig:shadow-archetype-classification", "thm:shadow-spectral-correspondence", "sec:higher-depths", "prop:free-interacting-dichotomy"]}
metadata/claims.jsonl:2973:{"label": "thm:shadow-tautological-ring", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 20460, "title": "Shadow classes in the tautological ring", "refs_in_block": ["thm:modular-koszul-duality-main", "prop:independent-sum-factorization"]}
metadata/label_index.json:48282:  "thm:modular-koszul-duality-main": {

thinking
**Inspecting label index**

I find the label index interesting and want to inspect a specific entry. Maybe it’s useful to check the file intro for context. It seems like it’s just an anchor, though, so I should mention that it’s not related to the theorem environment. I might need to confirm that the theorem registry or claims are missing this item, so I'll look for exact claims as my next step.
exec
/bin/zsh -lc "rg -n '\"label\": \"thm:modular-koszul-duality-main\"|modular-koszul-duality-main' metadata/claims.jsonl metadata/label_index.json | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
metadata/claims.jsonl:2939:{"label": "thm:shadow-archetype-classification", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 16007, "title": "Shadow archetype classification", "refs_in_block": ["def:shadow-depth-classification", "cor:nms-betagamma-mu-vanishing", "thm:w-virasoro-quintic-forced", "prop:propagator-variance", "thm:modular-koszul-duality-main", "fig:shadow-archetype-classification", "thm:shadow-spectral-correspondence", "sec:higher-depths", "prop:free-interacting-dichotomy"]}
metadata/claims.jsonl:2973:{"label": "thm:shadow-tautological-ring", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/higher_genus_modular_koszul.tex", "line": 20460, "title": "Shadow classes in the tautological ring", "refs_in_block": ["thm:modular-koszul-duality-main", "prop:independent-sum-factorization"]}
metadata/label_index.json:48282:  "thm:modular-koszul-duality-main": {

thinking
**Inspecting label index entry**

I need to check the label_index entry, but I'm not completely sure what type I'm supposed to be looking for. Am I inspecting the format, content, or something else? There seems to be a bit of uncertainty here. I wonder if there are any specific criteria or guidelines I should follow while doing this inspection. It might help to clarify the type before moving forward to prevent any confusion.
exec
/bin/zsh -lc "sed -n '48282,48292p' metadata/label_index.json" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  "thm:modular-koszul-duality-main": {
    "file": "chapters/theory/introduction.tex",
    "line": 2274
  },
  "thm:modular-mc-clutching": {
    "file": "chapters/theory/configuration_spaces.tex",
    "line": 2556
  },
  "thm:modular-propagator-existence": {
    "file": "chapters/theory/higher_genus_modular_koszul.tex",
    "line": 12697

thinking
**Analyzing potential inconsistencies**

I’m looking at a stale line in the label index that might be affected by an anchor movement. There's a theorem about the concordance that's cited that includes a statement regarding polynomial properties that seems inconsistent. It appears the theorem statement `P(t)=1+t^2` may not align with another proposition related to affine level. I'll need to examine the concordance table closely, especially lines 64-70, to see how those claims interact with each other and if I'm catching something inconsistent.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '60,72p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    60	 additivity and duality constraints;
    61	 Faber--Pandharipande free-energy formula
    62	 \textup{(}Thm~\ref{thm:genus-universality}\textup{)}
    63	 & \ClaimStatusProvedHere \\
    64	\textbf{H} & Chiral Hochschild
    65	 & $\ChirHoch^*(\cA)$ polynomial with Hilbert polynomial
    66	 $P(t)=1+t^2$, Koszul-functorial;
    67	 $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
    68	 \textup{(}Thms~\ref{thm:w-algebra-hochschild},
    69	 \ref{thm:virasoro-hochschild},
    70	 \ref{thm:critical-level-cohomology};
    71	 Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
    72	 & \ClaimStatusProvedHere


thinking
**Examining findings and inconsistencies**

I’m checking for clarity and accuracy in my work. For instance, the introduction line citing `Definition\ref{def:chiral-koszul-pair}` might not be the best reference for Theorem A. I should validate claims around `thm:modular-homotopy-convolution`. Then, I noticed a potential typo about the number of main theorems—it's listed as four when there are actually five. I’ll look closely at lines 451-456 to clarify that. Lastly, I need to verify the assignment of roles in Theorem C as well.
thinking
**Evaluating theorem assignments**

I’m looking into potential issues with Theorem A, specifically regarding how it constructs the arena gAmod. I noticed that `princ:five-facets` suggests that Theta arises automatically as `D_A - d_A^(0)`, but that seems to belong more properly to the bar-intrinsic theorem `thm:mc2-bar-intrinsic`. I’ll need to inspect the statement for `thm:mc2-bar-intrinsic` and possibly cite that correctly in my work. I should focus on the content around line 3499 in `higher_genus_modular_koszul.tex` for details.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '3488,3528p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc "rg -n 'constructs the arena|constructs the modular convolution algebra|arena.*Theorem~A|Theorem~A constructs' chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex:350:Theorem~A constructs the bar-cobar adjunction and its Verdier intertwining
chapters/theory/introduction.tex:380:\emph{Existence}: Theorem~A constructs the arena~$\gAmod$.
exec
/bin/zsh -lc "rg -n 'modular convolution algebra~\\\\gAmod|bar--cobar adjunction constructs the modular convolution algebra' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 61ms:

exec
/bin/zsh -lc "rg -n 'bar--cobar adjunction constructs|constructs the modular convolution|Theta_\\\\cA arises automatically' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
732: The bar--cobar adjunction constructs the modular convolution

thinking
**Searching for theorem references**

I'm checking out Potential finding 69 regarding `Theorem\ref{modular-koszul-duality-main}` and its references. I'm considering that if there's no theorem environment, cross-references may only point to section numbers, which could be confusing. I need to see if there are other instances of `Theorem\ref{thm:modular-koszul-duality-main}` beyond just concordance. Maybe this should include references from other files, given there may be numerous occurrences, especially in `higher_genus_modular_koszul`.
exec
/bin/zsh -lc "rg -n 'Theorem~\\\\ref\\{thm:modular-koszul-duality-main\\}|thm:modular-koszul-duality-main' chapters | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:77:Theorem~\ref{thm:modular-koszul-duality-main} (the flag theorem)
chapters/connections/frontier_modular_holography_platonic.tex:4685:(Theorem~\ref{thm:modular-koszul-duality-main})
chapters/theory/higher_genus_modular_koszul.tex:16523:\textup{(}Theorem~\textup{\ref{thm:modular-koszul-duality-main}}),
chapters/theory/higher_genus_modular_koszul.tex:16686:By Theorem~\ref{thm:modular-koszul-duality-main}(iv),
chapters/theory/higher_genus_modular_koszul.tex:16896:Theorem~\ref{thm:modular-koszul-duality-main}(ii)).
chapters/theory/higher_genus_modular_koszul.tex:21416: Theorem~\textup{\ref{thm:modular-koszul-duality-main}}\textup{(iv)}.
chapters/theory/higher_genus_modular_koszul.tex:21446:Theorem~\ref{thm:modular-koszul-duality-main}(iv):
chapters/frame/heisenberg_frame.tex:4811:Theorem~\ref{thm:modular-koszul-duality-main},
chapters/theory/introduction.tex:2508:\phantomsection\label{thm:modular-koszul-duality-main}%

thinking
**Inspecting file citations**

I need to check the files that cite parts (iv) and see if there’s a theorem environment. If there isn’t, those citations might be semantically broken and could lead to unresolved subparts. I should look into one body of usage to find out more. It seems like I might be expecting a theorem with enumerated clauses, so I'll search around to clarify how these parts are being referenced. Let's see what I can find!
codex
The “flag theorem” problem is larger than one bad sentence in the concordance. Other body chapters cite `Theorem~\ref{thm:modular-koszul-duality-main}(iv)` and similar clause references, but the live source only provides a phantom label in the introduction. I’m reading one of those downstream uses now to see how much of the manuscript is leaning on a theorem surface that no longer exists.
exec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex | sed -n '4804,4816p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '4678,4690p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '16676,16694p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '21438,21452p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4804	holomorphic-topological field theory.
  4805	
  4806	\section{The chiral center theorem for Heisenberg}
  4807	\label{sec:frame-center-theorem}
  4808	\index{center theorem!Heisenberg instantiation}
  4809	
  4810	The center theorem (item~(v) of
  4811	Theorem~\ref{thm:modular-koszul-duality-main},
  4812	\S\ref{sec:operadic-center-theorem}) identifies the chiral
  4813	Hochschild cochain complex $C^\bullet_{\mathrm{ch}}(\cA,\cA)$
  4814	as the operadic center of the $\mathsf{SC}^{\mathrm{ch,top}}$
  4815	structure on the derived center pair
  4816	$(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA)$. For the
 succeeded in 51ms:
 16676	\ClaimStatusProvedHere
 16677	\index{shadow depth!Koszul duality invariance}
 16678	\index{Koszul duality!preserves shadow depth}
 16679	Koszul duality preserves shadow depth:
 16680	$r_{\max}(\cA^!) = r_{\max}(\cA)$. In particular, the shadow
 16681	class $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ is an
 16682	invariant of the Koszul duality orbit.
 16683	\end{corollary}
 16684	
 16685	\begin{proof}
 16686	By Theorem~\ref{thm:modular-koszul-duality-main}(iv),
 16687	$\mathbb{D}(\Theta_\cA) = \Theta_{\cA^!}$, where
 16688	$\mathbb{D}$ is the Verdier involution. Since $\mathbb{D}$
 16689	is an automorphism of~$\gAmod$ respecting the weight
 16690	filtration, it bijects the obstruction classes:
 16691	$o_r(\cA) = 0$ if and only if $o_r(\cA^!) = 0$.
 16692	Hence $r_{\max}(\cA) = r_{\max}(\cA^!)$.
 16693	\end{proof}
 16694	
 succeeded in 51ms:
  4678	This matches
  4679	Proposition~\ref{prop:independent-sum-factorization}:
  4680	for $L = L_1 \oplus L_2$ with vanishing mixed OPE,
  4681	$\kappa$ is additive and $\Delta$ is multiplicative.
  4682	\item \emph{Genus expansion.}
  4683	The shadow genus expansion
  4684	$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$
  4685	(Theorem~\ref{thm:modular-koszul-duality-main})
  4686	reproduces the vacuum sector of the Nekrasov genus expansion
  4687	$F = \sum_{g \geq 0} \hbar^{2g-2} F_g(a,q)$
  4688	in the unrefined limit.
  4689	\end{enumerate}
  4690	Computational verification:
 succeeded in 51ms:
 21438	joining two external legs with a single genus-$g$ vertex.
 21439	The vertex weight is
 21440	$\operatorname{tr}_{\mathrm{cyc}}(\ell_2^{(g)}) = \kappa(\cA)$
 21441	by Theorem~\ref{thm:modular-characteristic}.
 21442	The stratum class is $\pi^*\lambda_g$.
 21443	
 21444	(iii)~The clutching compatibility is the scalar trace of the
 21445	MC factorization from
 21446	Theorem~\ref{thm:modular-koszul-duality-main}(iv):
 21447	the graph-sum formula is constructed from stable-graph
 21448	compositions, which are precisely the boundary maps
 21449	of~$\overline{\mathcal{M}}_{g,n+1}$.
 21450	
 21451	(iv)~Class~$\mathbf{G}$: all transferred operations
 21452	$\ell_k^{(g)} = 0$ for $k \geq 3$, so only degree-$2$




thinking
**Considering theorem references**

I'm noticing that the downstream uses of `Theorem... (iv)` are independent breakages. It seems like a good idea to list that separate finding at `chapters/theory/higher_genus_modular_koszul.tex:16686`, especially since it cites a clause `(iv)` from a theorem that doesn't exist. This feels like an important clarification to ensure everything aligns properly and prevents potential confusion later on. Let's make sure I keep this detail noted for future reference!
thinking
**Considering intersection meaning**

I’m looking at the introduction line 606 which mentions "Their intersection is the center Z(A)". There might be confusion here about whether they mean the intersection of complementary Lagrangians in shifted-symplectic derived moduli rather than eigenspaces. However, the sentence does explicitly say eigenspaces, which adds some clarity. It's interesting to consider how the intersection defined as zero might relate to char 0 and the strength of the statement being made.
thinking
**Considering the theorem verification issue**

I’m looking at the intro line 2418 that refers to "Verifies Theorem D scalar saturation family-by-family." I’m uncertain if it's completely clear or correct. It might be okay, but I have to check that the phrasing is precise and that it conveys the right meaning. I want to ensure that everything in the document is accurate, so I'll need to think through what it truly means and whether any adjustments are necessary.
thinking
**Clarifying theorem issues**

I'm examining the Concordance theorem, particularly the row that states universal `P(t)=1+t^2`, yet it also mentions `HH^1(V_k(g)) ≅ g`. This creates a contradiction regarding the nonzero t coefficient and total dimension of `dim(g)+2`. Moreover, it references `thm:critical-level-cohomology` which, while interesting, is marked as `ProvedElsewhere`. Additionally, the Concordance context later clarifies that Theorem H does not apply at the critical level, which adds to the confusion.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '562,571p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   562	\item \emph{Theorem~B} (Bar-cobar inversion,
   563	 Theorem~\ref{thm:higher-genus-inversion}).
   564	 On the Koszul locus, the counit
   565	 $\Omega_X \bar{B}_X(\cA) \xrightarrow{\sim} \cA$
   566	 is an equivalence; the spectral sequence collapses at~$E_2$.
   567	 Off the locus, the bar-cobar object persists but becomes curved;
   568	 the failure is measured by
   569	 $\Theta_\cA := D_\cA - d_\cA^{(0)}$
   570	 (Theorem~\ref{thm:mc2-bar-intrinsic}).
   571	 The BRST resolution is complete.


thinking
**Clarifying theorem process**

I'm considering how to handle theorem A and theorem B. I need to ensure I ground every claim in the file contents, avoiding guesses or presenting inferences as facts. Fix suggestions should be minimal and truthful. I should say, "A minimal truthful fix is..." to avoid overclaiming. It's okay to mention specific body lines as evidence. Reflecting on whether we've truly exhausted the audit surface is tricky, but I've checked 15 files and found 9 issues. Our verdict is a fail. I should label them as [CRITICAL]/[HIGH]/[MEDIUM]/[LOW].
thinking
**Organizing findings and format**

I need to count the checked items, which is 15 files in total. I have 9 findings, so I think the format should be "Checked: 15 files | Findings: 9 | Verdict: FAIL." The user requested a format that includes "Checked: N | Findings: N | Verdict: PASS/FAIL," so I’ll go with "Checked: 15 | Findings: 9 | Verdict: FAIL." Also, the developer prefers clickable markdown links for referencing local files, but the user wants a plain format: "file:line."
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '30,40p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    30	\hline
    31	\textbf{A} & Bar-cobar adjunction
    32	 & $\barBch \dashv \Omegach$ on $\Ran(X)$,
    33	 with Verdier intertwining
    34	 \textup{(}Thm~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
    35	 & \ClaimStatusProvedHere \\
    36	\textbf{B} & Bar-cobar inversion
    37	 & $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$
    38	 on the Koszul locus
    39	 \textup{(}Thm~\ref{thm:higher-genus-inversion}\textup{)};
    40	 genus~$0$ unconditional; for arbitrary~$\cA$,
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '40,45p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    40	 genus~$0$ unconditional; for arbitrary~$\cA$,
    41	 $g \geq 1$ is conditional on
    42	 axiom~\ref{MK:modular}; unconditional on the
    43	 CFT-type standard landscape except integer-spin
    44	 $\beta\gamma$ by Theorem~\ref{thm:pbw-propagation}
    45	 and Remark~\ref{rem:pbw-propagation-scope}






thinking
**Evaluating theorem bounds**

I'm noticing a potential issue with the line that states, "Theorem H bounds the bulk state space." This seems more like a top-level summary than a detailed explanation. I'm considering whether I should refer to line 364 instead of line 678 for clarity. There might be a more concise way to present this information, so I'll have to think through how to make my points more effectively. Let's see how that plays out!
thinking
**Evaluating theorem references**

I'm considering which line to choose for Theorem H, debating between line 364 and 678. I think 678 is the better choice since it’s more precise and leads directly into the KM contradiction noted later. However, line 365's summary is inaccurate as well. Also, I need to keep in mind the potential issues with other theorems like A and B, and there's something to note in `concordance.tex:455` with theorem C regarding curvature.
thinking
**Assessing theorem findings**

I could mention a minor point about Theorem H in the concordance not using the term "Hilbert polynomial" for the series P(t), but it's probably not a big issue. I need to confirm if the `thm:modular-koszul-duality-main` label is in the theorem registry or claims, and it looks like it’s not. There's a potential issue with cross-references in LaTeX, as they might lead to invalid semantics if they include appended labels. I'm noting the downstream citations are at specific lines, which might cover inconsistencies, so I’ll check any other unresolved references.
thinking
**Confirming theorem existence**

I should check if `thm:ds-hpl-transfer` exists in Volume II, and it appears that I’ve already done that! That's great. I was thinking about mentioning "Checked: 15" or "Checked: 15 files," along with noting all references from the introduction and downstream uses of the flag theorem. However, I realize the summary format should just be "Checked: N | Findings: N | Verdict: PASS/FAIL" to keep things clear and concise.
thinking
**Analyzing theorem adjustments**

I need to remove `thm:critical-level-cohomology` from the theorem-H cluster and instead treat the critical level in a separate contrasting sentence. There's a problem in the introduction where it claims a universal bound of "total dimension at most four" for Theorem H. It's important to clarify these points to ensure that the information is accurate and well-presented. I'll focus on making sure these adjustments accurately reflect the theory discussed.
thinking
**Addressing errors in citations**

Okay, I need to replace the phrase with plain text, like “the DS-HPL transfer theorem in Volume II,” or I could introduce a cross-volume citation macro to clarify that Volume I defines it. I see a problem in the introduction as well: it incorrectly assigns a job to Theorem A. It should be geometric bar-cobar duality, not what’s currently stated. This misassignment is repeated later, so I need to address that too.
codex
- [CRITICAL] chapters/theory/introduction.tex:2508 — PROBLEM: `\label{thm:modular-koszul-duality-main}` is only a `\phantomsection` stub, not a theorem environment or tagged claim. The concordance still cites it as “the flag theorem” at `chapters/connections/concordance.tex:77`, and body chapters cite nonexistent clause numbers at `chapters/theory/higher_genus_modular_koszul.tex:16686`, `21446`, `chapters/frame/heisenberg_frame.tex:4810`, and `chapters/connections/frontier_modular_holography_platonic.tex:4685`. FIX: either restore an actual theorem environment with numbered clauses and a claim-status tag at this anchor, or stop using the `thm:` label entirely: rename it to a non-theorem label and retarget every downstream citation to the concrete theorem labels that actually prove the cited claims.

- [HIGH] chapters/theory/introduction.tex:355 — PROBLEM: the introduction says Theorem C is the family-specific scalar sum rule `\kappa(\cA)+\kappa(\cA^!)=K_\cA`. That is false on the live theorem surface. The actual theorem C at `chapters/theory/higher_genus_complementarity.tex:458-528` is the Verdier eigenspace/Lagrangian decomposition, and its own remark at `434-451` says the scalar formulas are consequences of Theorem C plus Theorem D, not part of Theorem C itself. The same inflation repeats at `chapters/theory/introduction.tex:818-833`. FIX: rewrite both intro summaries so Theorem C states only complementarity/Lagrangian splitting; move the `\kappa`-sum formulas to Theorem D’s duality clause or the appropriate scalar theorem. If `thm:central-charge-complementarity` is cited, use it only for `c+c'`, not `\kappa+\kappa'`.

- [HIGH] chapters/theory/introduction.tex:606 — PROBLEM: this sentence makes two false upgrades. It presents the PTVV shifted-symplectic moduli statement as unconditional, and it says the `+1`/`-1` Verdier eigenspaces intersect in `Z(\cA)`. But the body theorem gives a direct-sum eigenspace decomposition `Q_g(\cA)\oplus Q_g(\cA^!)` at `chapters/theory/higher_genus_complementarity.tex:503-521`, so the `\pm1` eigenspaces intersect trivially in characteristic `0`; and the concordance explicitly marks the ambient shifted-symplectic upgrade as conditional at `chapters/connections/concordance.tex:46-47`. FIX: replace the sentence with the proved statement: for `g\ge1`, the Verdier pairing makes `Q_g(\cA)` and `Q_g(\cA^!)` complementary Lagrangians in a direct sum decomposition; the ambient shifted-symplectic upgrade remains conditional; at `g=0`, `Q_0(\cA)=H^0(\overline{\mathcal M}_0,\mathcal Z(\cA))` and `Q_0(\cA^!)=0`.

- [HIGH] chapters/connections/concordance.tex:65 — PROBLEM: the theorem H row is internally false. It advertises the universal Hilbert polynomial `P(t)=1+t^2`, but the same row also advertises `\ChirHoch^1(V_k(\fg))\cong\fg` at line 67, which forces a nonzero `t`-coefficient and total dimension `\dim(\fg)+2`. The actual general theorem H at `chapters/theory/chiral_hochschild_koszul.tex:715-747` gives `P_\cA(t)=\dim Z(\cA)+\dim\ChirHoch^1(\cA)t+\dim Z(\cA^!)t^2`. The row also cites `thm:critical-level-cohomology`, but that theorem is `\ClaimStatusProvedElsewhere` at `chapters/theory/hochschild_cohomology.tex:150`, and the concordance itself later says Theorem H does not apply at critical level (`chapters/connections/concordance.tex:7188-7194`). FIX: rewrite the row to state amplitude `{0,1,2}` and the general polynomial formula; split examples by family if desired; remove `thm:critical-level-cohomology` from the proved-here theorem-H cluster.

- [HIGH] chapters/theory/introduction.tex:678 — PROBLEM: the introduction claims a universal “total dimension at most four” bound for Theorem H. The body explicitly kills that claim: `\ChirHoch^1(V_k(\fg))\cong\fg` at `chapters/theory/chiral_center_theorem.tex:2008-2021`; `\widehat{\mathfrak{sl}}_2` already has total dimension `5` at `1876-1883`; and the remark at `2078-2089` says the old `\dim\le4` bound fails and is not the correct uniform statement. The same bad bound is repeated at `chapters/theory/introduction.tex:365` and `854-855`. FIX: replace all three occurrences with the true theorem surface: concentration in degrees `{0,1,2}` with polynomial Hilbert series, but no universal total-dimension bound; for generic affine KM, total dimension is `\dim(\fg)+2`.

- [HIGH] chapters/theory/introduction.tex:2016 — PROBLEM: `Theorem~\ref{thm:ds-hpl-transfer}` is a dead cross-reference in Volume I. The label does not exist anywhere in this repo’s `.tex` surface; it exists only in Volume II at `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:2652`. In a Vol I build, this ref cannot resolve. FIX: replace the `\ref` with plain text such as “the DS-HPL transfer theorem in Volume II,” or introduce an explicit cross-volume citation macro/stub that Volume I actually defines.

- [MEDIUM] chapters/theory/introduction.tex:380 — PROBLEM: the intro assigns the wrong job to Theorem A: “Theorem A constructs the arena `\gAmod`.” The actual theorem A at `chapters/theory/chiral_koszul_pairs.tex:3638-3685` is geometric bar-cobar duality. The existence of `\Theta_\cA` in the convolution algebra is handled by `thm:mc2-bar-intrinsic` at `chapters/theory/higher_genus_modular_koszul.tex:3498-3528`, not by Theorem A. The same misassignment repeats at `chapters/theory/introduction.tex:732-734`. FIX: rewrite both passages so Theorem A supplies the bar-cobar/Verdier apparatus, while the convolution/MC existence claims are attributed to the convolution definition and `Theorem~\ref{thm:mc2-bar-intrinsic}`.

- [MEDIUM] chapters/connections/concordance.tex:454 — PROBLEM: this role map is wrong. It says “Theorem C identifies its genus-`g` curvature; Theorem D computes its leading coefficient.” On the live theorem surface, Theorem C is the complementarity/Lagrangian theorem, while Theorem D is the modular-characteristic/obstruction-class theorem. FIX: rewrite the sentence so Theorem C handles the Verdier decomposition into complementary Lagrangians, and Theorem D handles the scalar curvature/obstruction package and its coefficient `\kappa`.

- [MEDIUM] chapters/theory/introduction.tex:564 — PROBLEM: the theorem B summary strips off the higher-genus scope boundary. It says simply “On the Koszul locus, the counit ... is an equivalence,” but the concordance records the actual seam at `chapters/connections/concordance.tex:36-45`: genus `0` is unconditional, while for arbitrary `\cA`, `g\ge1` is conditional on `\ref{MK:modular}` and only unconditional on the proved standard landscape with the stated PBW exceptions. FIX: import that qualification into the introduction: genus `0` unconditional; higher-genus inversion for arbitrary `\cA` only under the modular-pre-Koszul / PBW-propagation hypotheses.

## Summary
Checked: 15 | Findings: 9 | Verdict: FAIL
tokens used
159,927
