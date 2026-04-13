# D03_biconditional_drift (803s)

- [CRITICAL] /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1116 — PROBLEM: `thm:ks-mc-gauge` is tagged `\ClaimStatusProvedHere`, claims `(I)\leftrightarrow(II)` and `(II)\leftrightarrow(III)`, but there is no proof block; line 1116 is only a sketch, and line 1118 appeals to tests, not a proof. No converse is actually proved in-file. FIX: Downgrade the environment to `remark` unless a real proof is added; replace line 1110 with `the following three formulations of Donaldson--Thomas theory are related:` and replace line 1116 with `The ordered quantum dilogarithm product computes the character of the hocolim. When an MC element \Theta^{\Eone}_\cC exists, it packages the wall-crossing data encoded by the transition maps \(K_\cW\).`

- [CRITICAL] chapters/examples/free_fields.tex:5155 — PROBLEM: the theorem states modular invariance `if and only if` critical central charge, but the proof at 5165 explicitly says modular invariance only forces `c-\tilde c \equiv 0 \pmod{24}` and that `c=26,15` comes from Weyl-anomaly cancellation, a separate condition. The proof undercuts the stated equivalence. FIX: Replace the statement with `In the bosonic and superstring BRST constructions, anomaly cancellation requires \(c=26\) and \(c=15\) respectively. Separately, genus-1 modular covariance of the partition function requires \(c-\tilde c \equiv 0 \pmod{24}\).` and remove the `if and only if`.

- [HIGH] chapters/connections/ym_higher_body_couplings.tex:256 — PROBLEM: the preceding theorem only proves survival to the next page `iff` the class lies in `\ker[\kappa_{\mathrm{mix}},-]` (lines 238-251); the corollary sharpens this to `\kappa_{\mathrm{mix}}=0`, and the proof at 264 says `Immediate from Theorem...`. The converse is not proved. FIX: Replace lines 256-259 with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).` If an equivalence is intended, replace the RHS by `[\kappa_{\mathrm{mix}},-]=0` on `\widetilde Z_\infty(M_1)\widehat\otimes \widetilde Z_\infty(M_2)` and prove that criterion separately.

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_higher_body_couplings.tex:256 — PROBLEM: same propagated AP36 failure as the Vol I copy; the theorem above identifies survival with `\ker[\kappa_{\mathrm{mix}},-]`, but the corollary upgrades this to `\kappa_{\mathrm{mix}}=0` without proof. FIX: Replace the `iff` sentence with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).`

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex:767 — PROBLEM: same propagated AP36 failure; the proof at 775 still cites the previous theorem as if it implied `\kappa_{\mathrm{mix}}=0 \iff` survival, but it only gives the kernel criterion. FIX: Replace the `iff` sentence with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).`

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex:724 — PROBLEM: same propagated AP36 failure; the proof at 732 again says the first statement is immediate from the theorem, but the theorem does not prove the converse `survival => \kappa_{\mathrm{mix}}=0`. FIX: Replace the `iff` sentence with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).`

- [HIGH] /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1434 — PROBLEM: `prop:center-hocolim` proves `|I|=1 \Rightarrow \mathrm{Obs}=0` and then gives only the conifold as a multi-chart example. It does not prove the converse `\mathrm{Obs}=0 \Rightarrow |I|=1` for general atlases. FIX: Replace line 1434 with `is zero when \(\cC\) has a single stability chamber (\(|I|=1\)). For the conifold, \(\mathrm{Obs}=2\). More generally, multi-chart atlases can carry a nontrivial braiding obstruction.`

- [HIGH] chapters/examples/free_fields.tex:5296 — PROBLEM: `thm:modular-classification` claims a complete `iff` classification, but the proof only supplies sufficient mechanisms; the only actual equivalence proved is the integer-weight triviality at 5311. No converse from modular invariance to the four listed cases is proved. FIX: Rename the theorem to `Sufficient conditions for genus-1 modular invariance` and replace line 5296 with `A chiral algebra \(\mathcal{A}\) is modular invariant at genus 1 in each of the following situations:`.

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:2887 — PROBLEM: `thm:classification-shadow-depth` is tagged `\ClaimStatusProvedHere`, but the later `Evidence` remark only proves the forward implications `simple poles \Rightarrow \dalg=0` and `double poles with central residue \Rightarrow \dalg=1`. The `iff` directions at 2887-2888 are not established. FIX: Replace lines 2887-2889 with `\(\dalg(\cA)=0\) if all OPE poles are simple; \(\dalg(\cA)=1\) if the maximal pole order is \(2\) and the corresponding residue is a scalar multiple of the identity (central term).` If the converses are intended, mark them conjectural.

- [MEDIUM] chapters/theory/poincare_duality.tex:577 — PROBLEM: `prop:koszul-pair-NAP` states an `iff` and then an `Equivalent characterization (NAP)` with no proof block; the cited definition provides the antecedent data for the forward direction, but the converse reconstruction from the displayed quasi-isomorphisms is not shown here. FIX: Replace line 577 with `If two chiral algebras $(\mathcal{A}_1,\mathcal{A}_2)$ on $X$ form a chiral Koszul pair, then there exist quasi-isomorphisms of chiral coalgebras:` and replace `Equivalent characterization (NAP)` with `Consequent NAP expression.`

## Summary
Checked: 151 | Findings: 10 | Verdict: FAIL


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
session id: 019d8418-b5fe-7bc0-80e1-4b9d4046b783
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


MISSION: DEEP ANTI-PATTERN SWEEP.

Find ALL \iff or 'if and only if' in theorem environments (AP36). For each: is the converse actually proved? If only forward direction is proved: flag and provide fix (change to \implies).

Search ALL three volumes:
- ~/chiral-bar-cobar/chapters/
- ~/chiral-bar-cobar-vol2/chapters/
- ~/calabi-yau-quantum-groups/chapters/

For each finding: exact file:line, PROBLEM, and EXACT FIX.
mcp startup: no servers


thinking
**Planning exploration with tools**

I’m thinking about using explorer agents to search theorem environments with “iff.” I might also need to read different skills and consider using an update plan since the task seems complex. I should probably gather files without needing the web because I'll rely on a local repo. I might have to use commentary and plan updates along the way, especially with the potential to execute multiple operations in parallel. I’ll focus on the output format and ensure to ground my claims with the files I read.
thinking
**Searching for theorem environments**

I could use a search to find all theorem environments that contain “iff” or “if and only if.” I need to inspect the surrounding proof to check if the converse is proved since the user wants to find all occurrences. This means exhaustively exploring theorem environments across three volume chapters. I might automate the parsing of these environments with `rg` for specific commands. It seems important to identify instances of `\iff`, `iff`, and the phrase “if and only if” within these contexts.
codex
The audit surface is all theorem-like environments under the three `chapters/` trees, restricted to occurrences of `\iff` or `if and only if`. I’m loading the audit workflow and then I’ll enumerate every candidate occurrence before checking whether the converse is actually proved in context.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 50ms:
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
**Auditing theorem environments**

I’m considering how to audit theorem-like environments where "iff" occurs, including the various forms like theorems, propositions, lemmas, and corollaries. I’m wondering if conjectures should also be included, especially if they state "iff." The user asked specifically about theorem environments, so I want to focus on those that are proved or provable. I might mention the scope in my commentary and look into environments from the theorem registry and other common environments.
codex
I’ve loaded the repo’s audit constitution and the red-team workflow. Next I’m extracting every `\iff` and `if and only if` that sits inside theorem-like environments across the three `chapters/` trees, then I’ll read each surrounding proof block to decide whether the converse is actually established or merely asserted.
Plan update
Scope is now fixed: theorem-like environments in all three chapter trees containing `\iff` or `if and only if`, with proof-context verification of the converse for each occurrence.
  → Enumerate every theorem-like environment in the three chapter trees containing `\iff` or `if and only if`
  • Read each candidate statement and its local proof or cited justification to test whether the converse is actually proved
  • Re-verify findings, remove false positives, and produce exact file:line fixes

thinking
**Parsing environments for matches**

I'm thinking it might be simplest to get all environments that contain a match line by stepping upward to the nearest beginning. I could add a remark here. I need to verify if this is theorem-like. It's possible to find matches inside proof lines or displayed equations as well. I should probably parse the full environment. Let's run a search to list out the raw matches effectively!
exec
/bin/zsh -lc "rg -n --no-heading '\\\\iff|if and only if' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --no-heading '\\\\begin\\{(theorem|proposition|lemma|corollary|maintheorem|claim|conjecture|remark|computation|verification|calculation)\\}' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters | sed -n '1,400p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Total output lines: 368

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:1256:$\overline{C}_3(E_\tau)$ if and only if the $R$-matrix
/Users/raeez/calabi-yau-quantum-groups/chapters/connections/bar_cobar_bridge.tex:332:The quantity $\chi/24$ is an integer if and only if $12 \mid (h^{1,1} - h^{2,1})$. Among standard complete intersections:
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex:860:$K_N/c_N^* = 2(H_N - 1)$ equals~$1$ if and only if $N = 2$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/e1_chiral_algebras.tex:843: YBE if and only if spectral coassociativity holds
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1116:The equivalences (I)$\leftrightarrow$(II) and (II)$\leftrightarrow$(III) hold as follows. (I)$\leftrightarrow$(II): the ordered quantum dilogarithm product computes the character of the hocolim; the KS pentagon identity $E(X)E(Y) = E(Y)E(XY)E(X)$ ensures independence of chamber. \emph{Critical distinction}: the pentagon holds in the quantum torus; the Lie algebra BCH captures only leading-order commutator terms and does NOT reproduce the full pentagon. (II)$\leftrightarrow$(III): the transition maps $K_\cW$ satisfy the cocycle condition if and only if the MC equation holds; the equation $[\Theta, \Theta] = 0$ holds automatically by antisymmetry, and its content is $D^2 = 0$ in the bar complex (a theorem from $\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$). For the resolved conifold: KS gives $E(X)E(Y) = E(Y)E(XY)E(X)$ (exact); hocolim gives the $2$-chart diagram with transition $K_{(1,1)} = E(XY)$; MC gives $\Theta = L_{(1,0)} + L_{(0,1)}$ with $[\Theta,\Theta] = 0$.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1162:The Lie bracket $[\cdot,\cdot]$ on $\fg_\Gamma$ satisfies the Jacobi identity (from the bimultiplicativity of $\langle\cdot,\cdot\rangle$), so $D^2 = 0$. An element $\Theta = \sum_\gamma a_\gamma e_\gamma \in \fg_\Gamma \otimes \C[\![\Gamma^+]\!]$ satisfies MC if and only if for every pair $(\alpha,\beta)$ with $\alpha + \beta = \gamma$, the consistency relation $\sum_{\alpha+\beta=\gamma} \langle\alpha,\beta\rangle \, a_\alpha a_\beta = 0$ holds. This is precisely the content of the path-ordered product condition at each joint (Kontsevich--Soibelman 2006, \S 1.2; Gross--Pandharipande--Siebert 2010, Theorem~1.4). The iterative construction proceeds order by order in $\Gamma^+$-degree, which is the degree filtration.
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1434:is zero if and only if $\cC$ has a single stability chamber ($|I| = 1$). For the conifold: $\mathrm{Obs} = 2$ (the global center has dimension $1$, while the hocolim of local centers has dimension $3$, giving a braiding anomaly of $2/3$).
/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/rosetta_stone.tex:4483:is trivial (equal to~$1$) if and only if $k \in \Z$.
chapters/examples/w_algebras_deep.tex:512:m_0^{(s_r)})$, vanishing simultaneously if and only if $c = 0$.
chapters/examples/w_algebras_deep.tex:1952:Both curvature channels vanish simultaneously if and only if $c = 0$:
chapters/examples/w_algebras_deep.tex:1954:c = 0 \iff 12k^2 + 47k + 45 = 0 \iff k = -\tfrac{9}{4},\; -\tfrac{5}{3}
chapters/examples/w_algebras_deep.tex:3227:abelian if and only if $\lambda$ has \emph{distinct parts}:
chapters/examples/lattice_foundations.tex:384: if and only if $\varepsilon$ is symmetric.
chapters/examples/lattice_foundations.tex:546: Borcherds) if and only if $\varepsilon$ is symmetric;
chapters/examples/lattice_foundations.tex:576:Hence skew-symmetry holds if and only if $\varepsilon$ is symmetric.
chapters/examples/lattice_foundations.tex:1602:$\mathrm{SL}_2(\Z)$-invariance holds if and only if $d \equiv 0 \pmod{24}$.
chapters/examples/lattice_foundations.tex:1995:$\Vlat_\Lambda$ is Koszul self-dual if and only if $\Lambda$ is unimodular (i.e., $\Lambda = \Lambda^*$) and the FLM cocycle $\varepsilon$ is self-inverse up to coboundary. The even unimodular lattices in rank $d$ exist only for $d \equiv 0 \pmod{8}$; the count is $1$ for $d = 8$, $2$ for $d = 16$, $24$ for $d = 24$ (Niemeier lattices), and grows rapidly thereafter.
chapters/examples/lattice_foundations.tex:2230: if and only if $\zeta_N^{2q(\alpha,\beta)} = 1$ for all
 succeeded in 53ms:
Total output lines: 400

/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:42:\begin{proposition}[Semisimplicity dichotomy]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:114:\begin{proposition}[$R$-matrix from bar degree $(1,1)$]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:135:\begin{remark}[Three $r$-matrices]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:160:\begin{theorem}[Kazhdan--Lusztig]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:175:\begin{remark}[Bar-complex interpretation]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:186:\begin{proposition}[KL and the DK bridge]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:209:\begin{conjecture}[Quantum group realization: Conjecture CY-C]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:226:\begin{remark}[Status of Conjecture CY-C]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:255:\begin{proposition}[Yangian from collision residue]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:271:\begin{remark}[Three distinct operations]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:322:\begin{proposition}[CoHA as quantum group]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:339:\begin{remark}[Slab as bimodule]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:387:\begin{theorem}[Kontsevich--Soibelman wall-crossing formula]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:414:\begin{remark}[Motivic refinement]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:426:\begin{conjecture}[Wall-crossing and the bar complex]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:461:\begin{proposition}[$\kappa_{\mathrm{cat}}$ for quantum groups]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:493:\begin{remark}[$\kappa_{\mathrm{cat}}$ versus other invariants]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/quantum_group_reps.tex:515:\begin{proposition}[Complementarity for $\kappa_{\mathrm{cat}}$]

thinking
**Gathering environment names**

I need to focus on the environment names with optional arguments. It seems I'm primarily interested in the top-level theorem environment content. I think using regex to identify the beginning and end would be helpful. For each file, I'll read through the lines and track when I'm inside the target environment. I'll specifically record lines that include `\iff` or `if and only if`, making sure to exclude patterns like `\iffalse`. Finally, I'll output the candidate count using Python!
codex
The raw grep surface is much larger than the theorem surface because it includes remarks, prose, bullets, and proofs. I’m collapsing it to only theorem-like environments now so the audit is grounded on actual statement blocks rather than incidental `iff` in surrounding exposition.
exec
/bin/zsh -lc "python3 - <<'PY'
import re
from pathlib import Path
roots = [Path('chapters'), Path('/Users/raeez/chiral-bar-cobar-vol2/chapters'), Path('/Users/raeez/calabi-yau-quantum-groups/chapters')]
target_envs = {'maintheorem','theorem','proposition','lemma','corollary','claim'}
pat_begin = re.compile(r'\\\\begin\\{(' + '|'.join(sorted(target_envs)) + r')\\}')
pat_end = re.compile(r'\\\\end\\{(' + '|'.join(sorted(target_envs)) + r')\\}')
pat_match = re.compile(r'(?<"'!'"\\\\)if and only if|\\\\iff(?"'!alse)'"')
results = []
for root in roots:
    for path in sorted(root.rglob('*.tex')):
        try:
            lines = path.read_text().splitlines()
        except Exception:
            continue
        stack = []
        for i, line in enumerate(lines, start=1):
            m = pat_begin.search(line)
            if m:
                stack.append({'env': m.group(1), 'start': i, 'matches': [], 'path': str(path)})
            if stack and pat_match.search(line):
                stack[-1]['matches'].append((i, line.strip()))
            m2 = pat_end.search(line)
            if m2 and stack:
                top = stack.pop()
                if top['env'] "'!= m2.group(1):
                    pass
                if top['"'matches']:
                    results.append(top)
for item in results:
    print(f\"{item['path']}:{item['start']}:{item['env']}:{len(item['matches'])}\")
    for ln, txt in item['matches']:
        print(f\"  {ln}: {txt}\")
print('TOTAL', len(results))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 187ms:
chapters/connections/arithmetic_shadows.tex:1971:theorem:1
  1982: $m_n$ are nonzero if and only if their associated shadow
chapters/connections/arithmetic_shadows.tex:5440:proposition:1
  5448: if and only if the ratio
chapters/connections/arithmetic_shadows.tex:11377:proposition:1
  11386: $d - d\log\varphi(s)$ if and only if the frontier defect
chapters/connections/bv_brst.tex:463:lemma:1
  471: if and only if $c = 26$.
chapters/connections/bv_brst.tex:638:corollary:2
  648: if and only if $c(\cA) = 26$ \textup{(}Lemma~\textup{\ref{lem:brst-nilpotence})}.
  650: if and only if $\kappa_{\mathrm{tot}} = 0$, i.e., $c(\cA) = 26$
chapters/connections/casimir_divisor_core_transport.tex:1328:proposition:1
  1336: Then the \(L_2\)-transport sectors of \(A\) and \(B\) are similar, and the \(L_1\)-data coincide if and only if \(\kappa(A)=\kappa(B)\).
chapters/connections/dg_shifted_factorization_bridge.tex:748:theorem:1
  752: sectors if and only if
chapters/connections/dg_shifted_factorization_bridge.tex:1094:theorem:1
  1098: if and only if
chapters/connections/editorial_constitution.tex:1863:theorem:1
  1873: ($d_{\mathrm{bar}}^2 = 0$) if and only if
chapters/connections/frontier_modular_holography_platonic.tex:2440:theorem:1






thinking
**Categorizing theorem proofs**

I'm thinking of categorizing proofs by their patterns. Some statements like "if and only if" only show one direction in their proof, which makes me suspicious. I need to actually read the theorems and identify those that only prove “sufficiency” or “necessity.” Automated detection can help isolate the theorem block and proof, then search for key phrases. Since the user wants claims grounded in the actual file contents, we can use automation to inspect and verify findings. There might be duplicate files that need addressing.
thinking
**Considering changes to code**

I need to decide whether to change “iff” to “implies,” possibly including the full statement. However, I’m not sure if I should apply any changes without explicit instructions, especially with a harsh auditor. The user requested an audit, not edits, so it’s likely best to stick with auditing only. Still, I could create a local parsing script to organize findings, maybe outputting candidates with statement and proof blocks to a temp file for inspection. Using grep could help with that!
thinking
**Considering proof requirements**

It looks like if a theorem is ProvedElsewhere and the statement involves "if and only if," the converse might not be able to be locally proved because it relies on external sources. If the local file states "if and only if," but the proof does not support both directions, we may need to flag it. The user has requested actual file contents, so we can't make guesses or infer information. We must only use what we've read.
thinking
**Flagging proof validity**

I think I should only flag local AP36 if the local proof or cited justification only proves the forward direction or reduces to one implication. If a theorem is proved elsewhere with a citation and there's no local proof, we can't claim the converse is unproved as that goes beyond what's in the file. I'll need to be careful since the user instructed not to take anything at face value while grounding rules prevent guessing. Flagging should occur only when local contents show a clear one-way proof.
thinking
**Analyzing the theorem's proof status**

I need to examine whether the file contents establish both directions for the theorem labeled as `\ClaimStatusProvedElsewhere`. Since it cites a theorem but doesn’t provide a proof, the converse isn't confirmed based solely on this document. The user requested "no guesses," so I have to note that the local file only offers a citation without proof. Therefore, I must conclude that AP36 remains unresolved and focus on the available local proof blocks that clarify only the forward direction.
thinking
**Prioritizing theorem claims**

I think it might be a good idea to use claim status tags to prioritize those proved here. There’s a chance I could search just the proved-here theorem-like environments, but the task specifies all theorem environments. AP36 is particularly about an "if and only if" claim where the converse is also proved. If I see `ClaimStatusProvedElsewhere` without a proof, I can’t verify it, so I’ll treat it as a residual risk. I could also create a script to capture immediate proofs or remarks after identifying each candidate.
codex
I’ve reduced the audit to 151 theorem-like statement blocks with `\iff` or `if and only if`. The next pass is proof-context triage: I’m extracting each statement together with its immediate proof block so I can distinguish actual AP36 failures from statements that merely look suspicious in isolation.
exec
/bin/zsh -lc "python3 - <<'PY'
import re, json
from pathlib import Path
roots = [Path('chapters'), Path('/Users/raeez/chiral-bar-cobar-vol2/chapters'), Path('/Users/raeez/calabi-yau-quantum-groups/chapters')]
target_envs = {'maintheorem','theorem','proposition','lemma','corollary','claim'}
all_envs = target_envs | {'proof','remark','conjecture','definition','example','computation','verification','calculation'}
pat_begin = re.compile(r'\\\\begin\\{([A-Za-z*]+)\\}')
pat_end = re.compile(r'\\\\end\\{([A-Za-z*]+)\\}')
pat_match = re.compile(r'(?<"'!'"\\\\)if and only if|\\\\iff(?"'!alse)'"')
pat_label = re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
pat_status = re.compile(r'\\\\ClaimStatus([A-Za-z]+)')
out = []
for root in roots:
    for path in sorted(root.rglob('*.tex')):
        try:
            lines = path.read_text().splitlines()
        except Exception:
            continue
        i = 0
        while i < len(lines):
            m = pat_begin.search(lines[i])
            if not m or m.group(1) not in target_envs:
                i += 1
                continue
            env = m.group(1)
            start = i
            depth = 1
            i += 1
            matches = []
            label = None
            status = None
            body_lines = [lines[start]]
            while i < len(lines) and depth > 0:
                line = lines[i]
                body_lines.append(line)
                if label is None:
                    mm = pat_label.search(line)
                    if mm:
                        label = mm.group(1)
                if status is None:
                    ms = pat_status.search(line)
                    if ms:
                        status = ms.group(1)
                if pat_match.search(line):
                    matches.append((i+1, line.strip()))
                mb = pat_begin.search(line)
                if mb and mb.group(1) == env:
                    depth += 1
                me = pat_end.search(line)
                if me and me.group(1) == env:
                    depth -= 1
                i += 1
            if not matches:
                continue
            end = i
            # capture immediate proof if present before next target env and skipping blank/comments/status lines
            j = end
            while j < len(lines) and (lines[j].strip() == '' or lines[j].strip().startswith('%') or pat_status.search(lines[j])):
                j += 1
            proof = None
            proof_start = proof_end = None
            if j < len(lines):
                mb = pat_begin.search(lines[j])
                if mb and mb.group(1) == 'proof':
                    proof_start = j+1
                    depth2 = 1
                    proof_lines = [lines[j]]
                    j += 1
                    while j < len(lines) and depth2 > 0:
                        proof_lines.append(lines[j])
                        mb2 = pat_begin.search(lines[j])
                        if mb2 and mb2.group(1) == 'proof':
                            depth2 += 1
                        me2 = pat_end.search(lines[j])
                        if me2 and me2.group(1) == 'proof':
                            depth2 -= 1
                        j += 1
                    proof_end = j
                    proof = '\\n'.join(proof_lines)
            out.append({
                'path': str(path),
                'env': env,
                'start': start+1,
                'end': end,
                'label': label,
                'status': status,
                'matches': matches,
                'statement': '\\n'.join(body_lines),
                'proof_start': proof_start,
                'proof_end': proof_end,
                'proof': proof,
            })
Path('/tmp/iff_candidates.json').write_text(json.dumps(out, indent=2))
print(f'wrote {len(out)} candidates to /tmp/iff_candidates.json')
# quick summary by path prefix and proof availability
from collections import Counter
c = Counter((('proof' if x['proof'] else 'no_proof'), x['path'].split('/chapters/')[0].split('/')[-1] if '/chapters/' in x['path'] else 'vol1') for x in out)
for k,v in sorted(c.items()):
    print(k, v)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 247ms:
wrote 151 candidates to /tmp/iff_candidates.json
('no_proof', 'calabi-yau-quantum-groups') 1
('no_proof', 'chiral-bar-cobar-vol2') 4
('no_proof', 'vol1') 11
('proof', 'calabi-yau-quantum-groups') 2
('proof', 'chiral-bar-cobar-vol2') 48
('proof', 'vol1') 85

thinking
**Evaluating candidates for proofs**

I need to inspect candidates, considering their paths and statements. It might help to create a script that outputs a summary with labels and statuses. I could make a more readable list and prioritize those without proof—there's a count of 16. I'll look for important keywords that indicate potential failures in proofs, like "converse" or "if." A manual inspection will still be necessary, but using a script to classify proofs based on these markers could be beneficial. Let's look closely at proofs lacking proof or those with suspicious lengths.
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
for c in cands:
    proof=c['proof'] or ''
    markers=[]
    for name,pat in [
        ('converse', r'converse|Conversely'),
        ('onlyif', r'only if|\\\\implies|\\\\Rightarrow|necess'),
        ('iff', r'\\\\iff|if and only if|equivalent'),
        ('suff', r'suffic|necessary'),
    ]:
        if re.search(pat, proof): markers.append(name)
    plen=len(proof.splitlines()) if proof else 0
    print(f\"{c['path']}:{c['start']} env={c['env']} label={c['label']} status={c['status']} proof_lines={plen} markers={','.join(markers) or '-'}\")
    for ln,txt in c['matches']:
        print(f\"  match {ln}: {txt}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/arithmetic_shadows.tex:1971 env=theorem label=thm:ainfty-formality-depth status=ProvedHere proof_lines=15 markers=-
  match 1982: $m_n$ are nonzero if and only if their associated shadow
chapters/connections/arithmetic_shadows.tex:5440 env=proposition label=prop:koszul-field-criterion status=ProvedHere proof_lines=39 markers=onlyif,iff
  match 5448: if and only if the ratio
chapters/connections/arithmetic_shadows.tex:11377 env=proposition label=prop:gauge-criterion-scattering status=ProvedHere proof_lines=16 markers=onlyif,iff
  match 11386: $d - d\log\varphi(s)$ if and only if the frontier defect
chapters/connections/bv_brst.tex:463 env=lemma label=lem:brst-nilpotence status=None proof_lines=0 markers=-
  match 471: if and only if $c = 26$.
chapters/connections/bv_brst.tex:638 env=corollary label=cor:anomaly-physical-genus0 status=ProvedHere proof_lines=21 markers=-
  match 648: if and only if $c(\cA) = 26$ \textup{(}Lemma~\textup{\ref{lem:brst-nilpotence})}.
  match 650: if and only if $\kappa_{\mathrm{tot}} = 0$, i.e., $c(\cA) = 26$
chapters/connections/casimir_divisor_core_transport.tex:1328 env=proposition label=None status=ProvedHere proof_lines=4 markers=-
  match 1336: Then the \(L_2\)-transport sectors of \(A\) and \(B\) are similar, and the \(L_1\)-data coincide if and only if \(\kappa(A)=\kappa(B)\).
chapters/connections/dg_shifted_factorization_bridge.tex:748 env=theorem label=thm:adjacent-root-rigidity status=ProvedHere proof_lines=7 markers=-
  match 752: sectors if and only if
chapters/connections/dg_shifted_factorization_bridge.tex:1094 env=theorem label=thm:quadrilateral-rigidity status=ProvedHere proof_lines=12 markers=-
  match 1098: if and only if
chapters/connections/editorial_constitution.tex:1863 env=theorem label=thm:anomaly-koszul status=ProvedHere proof_lines=14 markers=onlyif,iff
  match 1873: ($d_{\mathrm{bar}}^2 = 0$) if and only if
chapters/connections/frontier_modular_holography_platonic.tex:2440 env=theorem label=thm:quartic-obstruction-linf status=ProvedHere proof_lines=15 markers=-




thinking
**Exploring theorem statements**

I need to inspect candidate theorem statements and proofs, especially those without proof markers. Some might still establish equivalence structurally, so I'll focus on heuristics to identify likely AP36 failures based on proof length and the absence of converse markers. I'll use scripts to open relevant sections and get exact line references for findings. It seems like there are many duplicates across volumes, which could help streamline the audit if handled correctly.
thinking
**Examining candidates and proofs**

I need to manually judge the candidates, but with 151, that's quite a lot. Some are likely not AP36 because they use standard equivalences or well-known theorems. To efficiently sift through, I could use heuristics to focus on those most likely to fail. However, the user wants an exhaustive review, so I should examine all candidate statements with scripts. I can algorithmically group duplicates based on labels or text, as many exist across volumes. I'll categorize potential findings, particularly looking at issues like proof directions and conditions.
thinking
**Finding AP36 issues**

The user is looking for a "maximally harsh adversarial auditor" and a "deep anti-pattern sweep" to locate AP36 issues. For exact fixes, I might consider replacing "if and only if" with just "if" or breaking it into one direction. A simpler principle could be useful: if a theorem proof doesn’t explicitly argue both directions but looks like an algebraic equivalence, we might not need to flag it. I'm realizing it’s essential to ground these assumptions in the file contents.
thinking
**Evaluating proof candidates**

I’m thinking about how to approach a proof, especially if it computes a quantity and disappears when the expression equals zero. Even without using "converse" wording, it should be clear enough. I need to establish whether the proof provides a formula that supports an "iff" condition. There are many candidate theorems, but some might need special attention. Perhaps I could create a script to highlight proofs that are suspicious, like those with fewer than ten proof lines. Let's summarize the findings.
codex
The candidate set splits cleanly now: many `iff` statements are backed by explicit formula computations, while a smaller subset has either no proof block or a proof too short to discharge both directions on its face. I’m reading that high-risk subset first, then I’ll come back through the longer proofs that still look one-directional.
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
for c in cands:
    plen=len((c['proof'] or '').splitlines()) if c['proof'] else 0
    if plen<=10 and c.get('status')"'!='"'ProvedElsewhere':
        print(f\"{c['path']}:{c['start']} env={c['env']} label={c['label']} status={c['status']} proof_lines={plen}\")
        for ln,txt in c['matches']:
            print(f\"  match {ln}: {txt}\")
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex:463 env=lemma label=lem:brst-nilpotence status=None proof_lines=0
  match 471: if and only if $c = 26$.
chapters/connections/casimir_divisor_core_transport.tex:1328 env=proposition label=None status=ProvedHere proof_lines=4
  match 1336: Then the \(L_2\)-transport sectors of \(A\) and \(B\) are similar, and the \(L_1\)-data coincide if and only if \(\kappa(A)=\kappa(B)\).
chapters/connections/dg_shifted_factorization_bridge.tex:748 env=theorem label=thm:adjacent-root-rigidity status=ProvedHere proof_lines=7
  match 752: sectors if and only if
chapters/connections/frontier_modular_holography_platonic.tex:3301 env=corollary label=cor:critical-dimensions status=ProvedHere proof_lines=4
  match 3306: $\barB(\cA^!)$ is uncurved if and only if
chapters/connections/genus_complete.tex:130 env=theorem label=None status=None proof_lines=0
  match 134: which vanishes if and only if $c = 0$ (as a cohomology class in $H^2$). The integrated obstruction is $(c/2)\int_{\overline{\mathcal{M}}_{1,1}}\lambda_1 = c/48$ on the stack, or $c/24$ on the coarse moduli space. Note: for $c \in 24\mathbb{Z}$, the monodromy $e^{-2\pi i c/24}$ is trivial, so individual characters can be scalar modular functions, but the factorization algebra still requires a twist by $\mathbb{E}^{c/2}$. The data determining this obstruction class are:
chapters/connections/genus_complete.tex:1970 env=theorem label=thm:euler-koszul-criterion status=None proof_lines=9
  match 1976: $D_\cA \equiv 1$ if and only if $w_i = 1$ for all~$i$.
chapters/connections/semistrict_modular_higher_spin_w3.tex:529 env=theorem label=thm:cubic-weight-recursion-chapter status=None proof_lines=7
  match 541: Then $\Theta\in \MC(L_{W_3}^{\modu})$ if and only if, for every $N\ge1$,
chapters/connections/thqg_perturbative_finiteness.tex:79 env=lemma label=lem:thqg-I-completeness status=None proof_lines=3
  match 82: $\mathcal{H}_q(\cA)$ is a separable Hilbert space for every $q \in (0,1)$. A Cauchy sequence $\{v^{(k)}\}_{k \geq 1}$ converges if and only if $\sum_{n \geq 0} q^n \|v^{(k)}_n - v^{(\ell)}_n\|^2 \to 0$ as $k, \ell \to \infty$.
chapters/connections/ym_higher_body_couplings.tex:224 env=theorem label=thm:first-correction-theorem status=None proof_lines=7
  match 238: the class of a naive quadratic mixed coupling survives to the next page if and only if it lies in the kernel of
chapters/connections/ym_higher_body_couplings.tex:254 env=corollary label=cor:persistence-criterion-quadratic-law status=None proof_lines=3
  match 256: The quadratic mixed-coupling law survives to first non-quadratic order if and only if


thinking
**Inspecting candidates for proof**

I’m dealing with multiple suspicious candidates here, and I need to inspect the text surrounding their proofs. I could use a script to extract context from a selected set. I want to focus on those with no proof or short proof first, but there are about 50 to choose from. I need to determine which are actual AP36 failures. Some might just involve algebra or definitions, so they could still be valid. The user wants all findings, not just candidates. I'll need roughly 20 findings, and a single script could help me print selected entries efficiently. Let's consider using Python for pretty-printing around the suspicious candidates, potentially organizing it in batches for inspection.
thinking
**Organizing inspection of candidates**

I think I should start by inspecting all suspicious candidates organized by file since some files have multiple related cases. It makes sense to read around those sections once for context. I need to identify duplicates and high-risk files—grouping by file seems the easiest way to manage this. I can use tools like `rg` or `sed` to target specific lines. There might be around 30 files to check, so parallel reads could help. I'll focus on extracting unique files from those cases with either no proof or up to 10 proofs.
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
files=[]
seen=set()
for c in cands:
    plen=len((c['proof'] or '').splitlines()) if c['proof'] else 0
    if plen<=10 and c.get('status')"'!='"'ProvedElsewhere' and c['path'] not in seen:
        seen.add(c['path'])
        files.append(c['path'])
for f in files:
    print(f)
print('count',len(files))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/connections/bv_brst.tex
chapters/connections/casimir_divisor_core_transport.tex
chapters/connections/dg_shifted_factorization_bridge.tex
chapters/connections/frontier_modular_holography_platonic.tex
chapters/connections/genus_complete.tex
chapters/connections/semistrict_modular_higher_spin_w3.tex
chapters/connections/thqg_perturbative_finiteness.tex
chapters/connections/ym_higher_body_couplings.tex
chapters/connections/ym_instanton_screening.tex
chapters/examples/deformation_quantization_examples.tex
chapters/examples/free_fields.tex
chapters/examples/kac_moody.tex
chapters/examples/landscape_census.tex
chapters/examples/w_algebras.tex
chapters/theory/bar_cobar_adjunction_curved.tex
chapters/theory/bar_cobar_adjunction_inversion.tex
chapters/theory/chiral_koszul_pairs.tex
chapters/theory/chiral_modules.tex
chapters/theory/configuration_spaces.tex
chapters/theory/higher_genus_modular_koszul.tex
codex
I’ve isolated the real risk surface: short or missing proofs on `iff` statements. I’m reading those sections file-by-file now, starting with the connection/frontier chapters where status drift and one-way arguments recur most often.
exec
/bin/zsh -lc "sed -n '440,490p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '740,1110p' chapters/connections/dg_shifted_factorization_bridge.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1320,1360p' chapters/connections/casimir_divisor_core_transport.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2428,2470p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\section{The genus-\texorpdfstring{$0$}{0} BRST-bar chain map}
\label{sec:brst-bar-chain-map}
\index{BRST!bar complex chain map|textbf}

\subsection{Setup: the BRST complex}

Let $\cA$ be a conformal vertex algebra of central charge~$c$ on
$X = \mathbb{P}^1$, and let $\cA_{\mathrm{gh}} = bc$ denote the
$bc$-ghost system of weights $(2, -1)$ with $c_{\mathrm{gh}} = -26$.
The \emph{BRST complex} of~$\cA$ is the vertex algebra
$\cA_{\mathrm{tot}} = \cA \otimes \cA_{\mathrm{gh}}$ equipped with
the BRST differential:
\begin{equation}\label{eq:brst-differential}
Q_{\mathrm{BRST}}
= \oint \! c(z)\Bigl(T_{\cA}(z) + \tfrac{1}{2}\,T_{\mathrm{gh}}(z)\Bigr)\,dz
= \sum_{n \in \mathbb{Z}} \Bigl(
 \sum_m L^{\cA}_m\, c_{n-m}
 + \tfrac{1}{2}\sum_{p+q=n}(p-q)\, {:}b_p\, c_q\, c_{n-p-q}{:}
\Bigr)
\end{equation}
 succeeded in 50ms:
uniform-weight lane (Definition~\ref{def:scalar-lane}),
\(\Gamma_A = \kappa(A)\Lambda\), but in general multi-weight
one-channel families this additional identification is open. The genuinely
non-scalar information begins at the spectral level \(\Delta_A\).
The present chapter refines that spectral level from a polynomial to an actual module.

This suggests the following conditional principle.

\begin{proposition}[The \(L_1\)--\(L_2\) package on the one-channel squarefree locus]
\ClaimStatusProvedHere
Assume:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \(A\) and \(B\) lie on a scalar-saturated one-channel locus, so their universal Maurer--Cartan classes are determined by \(\kappa(A)\) and \(\kappa(B)\);
\item \(\Delta_A=\Delta_B\);
\item \(\Delta_A\) is squarefree.
\end{enumerate}
Then the \(L_2\)-transport sectors of \(A\) and \(B\) are similar, and the \(L_1\)-data coincide if and only if \(\kappa(A)=\kappa(B)\).
Thus, on this locus, the realized \(L_1\)--\(L_2\) package is classified by the pair
\[
(\kappa(A),\Delta_A).
 succeeded in 51ms:
\[
\Pi_{\langle T_{ij}^{R},T_{ji}^{R}\rangle}
\big((\Delta_w\otimes\operatorname{id})X_{ij}^{23}(z)\big)
=
-\kappa_{ij}^{R}(w,z)T_{ij}^{R}+\kappa_{ji}^{R}(w,z)T_{ji}^{R}.
\]
\end{definition}

\begin{theorem}[Adjacent-root rigidity]
\ClaimStatusProvedHere
\label{thm:adjacent-root-rigidity}
The filtration-$2$ hexagon defect vanishes in the oriented triangle
sectors if and only if
\begin{align*}
\rho_{ij}(w)\kappa_{ij}^{L}(w,z)&=\frac12\rho_i(w)\rho_j(w+z),\\
\rho_{ij}(w)\kappa_{ji}^{L}(w,z)&=\frac12\rho_j(w)\rho_i(w+z),\\
\rho_{ij}(z)\kappa_{ij}^{R}(w,z)&=\frac12\rho_i(w+z)\rho_j(z),\\
\rho_{ij}(z)\kappa_{ji}^{R}(w,z)&=\frac12\rho_j(w+z)\rho_i(z).
\end{align*}
\end{theorem}
 succeeded in 51ms:
\begin{proof}
The Virasoro OPE gives the collision residue. The shadow
representation on primaries extracts the conformal Ward identity.
The infinite tower
(Theorem~\ref{thm:w-virasoro-mixed-shadow};
$r_{\max} = \infty$, Theorem~\ref{thm:w-virasoro-quintic-forced})
produces higher-order differential constraints that for degenerate
representations truncate to the finite-order BPZ null-vector equations.
\end{proof}

\subsubsection{The quartic obstruction theorem}

\begin{theorem}[Quartic obstruction = $L_\infty$ obstruction;
\ClaimStatusProvedHere]
\label{thm:quartic-obstruction-linf}
\index{quartic resonance class!equals L-infinity obstruction}
The obstruction to extending $\Theta_\cA^{\leq 3}$ to
$\Theta_\cA^{\leq 4}$ is
\begin{equation}\label{eq:quartic-obstruction-class}
[o_4(\cA)]
exec
/bin/zsh -lc "sed -n '2470,2505p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Standard $L_\infty$ obstruction theory
(Kontsevich~\cite{Kontsevich97}, Manetti~\cite{Manetti99}) applied to
$\gAmod$ with the weight filtration: the obstruction at weight~$r{+}1$
is the class of the MC failure projected to weight~$r{+}1$. At
weight~$4$, the clutching formula
$\xi^*\mathfrak{Q} = H \star \mathfrak{Q} +
\mathfrak{C} \star \mathfrak{C} + \mathfrak{Q} \star H$
identifies this with
$\mathfrak{R}^{\mathrm{mod}}_{4,g,n}(\cA)$. The class-by-class
vanishing follows from
Theorem~\ref{thm:heisenberg-exact-linearity} (class~$G$),
Corollary~\ref{cor:affine-postnikov-termination} (class~$L$), and
Theorem~\ref{thm:w-virasoro-quintic-forced} (class~$M$).
\end{proof}

\subsubsection{The collision-filtration spectral sequence}

\begin{construction}[Collision-filtration spectral sequence;
\ClaimStatusProvedHere]
\label{constr:holographic-spectral-sequence}
exec
/bin/zsh -lc "sed -n '120,170p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1960,1995p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '529,560p' chapters/connections/semistrict_modular_higher_spin_w3.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '220,290p' chapters/connections/ym_higher_body_couplings.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\hline
\end{tabular}
\end{center}

The bar complex calculation:
\[Z_\alpha = \int_{\overline{C}_*^{(1)}(E_\tau)} \exp\left(\sum_{i<j} \log\frac{\vartheta_\alpha(z_i - z_j|\tau)}{\vartheta_1(z_i - z_j|\tau)} \cdot \eta_{ij}^{(1)}\right)\]

The NS-NS sector vanishes: $\vartheta_1(0|\tau) = 0$ identically (the odd theta function vanishes at the origin), so $Z_{\mathrm{NS\text{-}NS}} = 0$. The other three sectors are non-vanishing.
\end{example}

\begin{theorem}[Extension obstruction; \ClaimStatusProvedElsewhere{} \cite{FBZ04,CG17}]\label{thm:extension-obstruction}
\index{extension obstruction!genus one}
A genus-zero chiral algebra $\mathcal{A}_0$ always extends to genus one as a \emph{projective} factorization algebra (i.e., twisted by a power of the Hodge line bundle). The obstruction to a \emph{strict} (untwisted) extension is measured by:
\[\mathrm{Obs}_1(\mathcal{A}_0) = \frac{c}{2}\,\lambda_1 \;\in\; H^2(\overline{\mathcal{M}}_{1,n},\, \mathcal{L}_{\mathcal{A}})\]
which vanishes if and only if $c = 0$ (as a cohomology class in $H^2$). The integrated obstruction is $(c/2)\int_{\overline{\mathcal{M}}_{1,1}}\lambda_1 = c/48$ on the stack, or $c/24$ on the coarse moduli space. Note: for $c \in 24\mathbb{Z}$, the monodromy $e^{-2\pi i c/24}$ is trivial, so individual characters can be scalar modular functions, but the factorization algebra still requires a twist by $\mathbb{E}^{c/2}$. The data determining this obstruction class are:
\begin{enumerate}
\item \emph{Central charge:} $c \in \mathbb{R}$ (any rational CFT extends to genus one; in critical string theory the matter central charge is $c_{\mathrm{matter}} = 26$ (bosonic) or $c_{\mathrm{matter}} = 15$ (superstring), chosen so that the total anomaly $c_{\mathrm{matter}} + c_{\mathrm{ghosts}} = 0$ cancels)
\item \emph{Modular invariance:} Characters $\chi_i(\tau)$ transform as vector-valued modular forms
\item \emph{Integrality:} Fusion rules $N_{ij}^k \in \mathbb{Z}_{\geq 0}$
\end{enumerate}
 succeeded in 52ms:
\frac{1}{r}\sum_{i=1}^r
\Bigl(1 - \frac{H_{w_i-1}(u)}{\zeta(u)}\Bigr)
\end{equation}
is a meromorphic function of~$u$ with poles only at zeros
of~$\zeta$.
The \emph{Euler--Koszul class}
$\operatorname{ek}(\cA) := \max_i(w_i - 1)$
is the maximal generator weight excess.
\end{definition}

\begin{theorem}[\ClaimStatusProvedHere]%
\label{thm:euler-koszul-criterion}%
\label{thm:euler-koszul-standard}%
\index{Euler--Koszul!criterion}%
\begin{enumerate}[label=\textup{(\roman*)}]
\item
$D_\cA \equiv 1$ if and only if $w_i = 1$ for all~$i$.
\item
$D_{\mathrm{Vir}}(u) = 1 - 1/\zeta(u)$; \quad
$D_{\cW_N}(u)
 succeeded in 50ms:
\begin{proof}
A filtered $A_\infty$ quasi-isomorphism between two transferred models intertwines their coderivations up to gauge equivalence in the Hochschild dg Lie algebra. The weight-one component of a gauge-equivalent coderivation changes by a relative Hochschild coboundary. Hence the cohomology class of $m^{(1)}$ is invariant.
\end{proof}

\begin{theorem}[First-correction theorem; \ClaimStatusProvedHere]
\label{thm:first-correction-theorem}
Equip $CC^\bullet_{\mathrm{rel}}(M_{12};M_1,M_2)$ with the filtration induced by mixed weight. Then the associated spectral sequence has
\[
E_1^0 \cong HH^0\bigl(\operatorname{gr} CC^\bullet_{\mathrm{rel}}\bigr),
\]
and the first differential is induced by the adjoint action of the mixed Kodaira--Spencer class:
\[
d_1[\phi] = [\kappa_{\mathrm{mix}},\phi].
\]
In particular, on the quadratic-limit term
\[
E_1^0 \cong \widetilde Z_\infty(M_1)\widehat\otimes \widetilde Z_\infty(M_2),
\]
the class of a naive quadratic mixed coupling survives to the next page if and only if it lies in the kernel of
\[
 succeeded in 50ms:
\begin{theorem}[Cubic weight recursion around the shadow base point \ClaimStatusProvedHere]
\label{thm:cubic-weight-recursion-chapter}
Write a putative modular lift in the form
\[
\Theta
=
\Theta_{W_3}^{\sh}+\alpha,
\qquad
\alpha=\sum_{N\ge1}\alpha_N,
\qquad
\alpha_N\in F^N/F^{N+1}.
\]
Then $\Theta\in \MC(L_{W_3}^{\modu})$ if and only if, for every $N\ge1$,
\begin{equation}
\label{eq:cubic-weight-recursion-chapter}
\ell_1(\alpha_N)
=
-\frac12\sum_{i+j=N}\pi_N\ell_2(\alpha_i,\alpha_j)
-\frac16\sum_{i+j+k=N}\pi_N\ell_3(\alpha_i,\alpha_j,\alpha_k),
\end{equation}

thinking
**Checking theorem proofs**

I’m looking at a theorem from a genus_complete context, and it seems like the first theorem has been proved elsewhere. That’s not very actionable for me. However, the second theorem lacks a proof snippet, possibly because it continues later? I could inspect the complete rest of the document, especially beyond line 1995, just to make sure nothing was missed by the parser if there's something significant later on.
exec
/bin/zsh -lc "sed -n '1995,2035p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\begin{proof}
(i)~$w_i = 1 \Leftrightarrow H_{w_i-1} = 0
\Leftrightarrow$ each summand in~\eqref{eq:euler-koszul-defect}
equals~$1$.
(ii)~Substitute $W = \{2\}$ and $\{2,\ldots,N\}$.
(iii)~$\cW_k(\fg)$ is strongly generated by $W$-currents
$W^{(d_i+1)}$ of conformal weight~$d_i + 1$;
substitute into Theorem~\ref{thm:dirichlet-weight-formula}.
\end{proof}

\begin{computation}[Euler--Koszul defect table for the standard landscape;
\ClaimStatusProvedHere]%
\label{comp:euler-koszul-defect-table}%
\index{Euler--Koszul defect!standard families|textbf}%
Substitute~\eqref{eq:dirichlet-standard}
into~\eqref{eq:euler-koszul-defect}:
\begin{center}
\renewcommand{\arraystretch}{1.35}
\begin{tabular}{lccccc}

thinking
**Investigating the theorem**

I need to check some other suspicious sections. I’m thinking about the `ym_instanton_screening` theorem, particularly the bullet point that states "module maps to zero iff screened." I wonder if this is coming directly from the theorem statement and its proof. There's definitely something to inspect there, and I need to see if I can clarify or confirm its accuracy. Let’s dive deeper into this!
codex
One actual AP36 problem has already surfaced: `cor:persistence-criterion-quadratic-law` claims an `iff` that the preceding theorem does not give. I’m checking the duplicated versions of that argument across Vol I and Vol II now, because this looks like a propagation bug rather than an isolated line-level mistake.
exec
/bin/zsh -lc "sed -n '320,355p' chapters/connections/ym_instanton_screening.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5150,5320p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2058,2090p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Assume $\mathcal A_{\mathrm{def}}$ is left noetherian.
Define the \emph{visible defect category}
\[
\mathsf{Def}_{\mathrm{vis}}(\mathcal B;\mathbf s)
:=S^{-1}\bigl(\mathcal A_{\mathrm{def}}\text{-}\mathrm{mod}_{\mathrm{fg}}\bigr),
\]
namely the exact central localization of finitely generated $\mathcal A_{\mathrm{def}}$-modules.
A finitely generated $\mathcal A_{\mathrm{def}}$-module $N$ is called \emph{screened} if every element of $N$
is annihilated by some element of $S$.
\end{definition}

\begin{theorem}[Central localization criterion for confinement; \ClaimStatusProvedHere]
\label{thm:central-localization-confinement}
Assume the hypotheses of Definition~\ref{def:visible-defect-category}.
Then:
\begin{enumerate}[label=(\alph*)]
\item a finitely generated module maps to zero in $\mathsf{Def}_{\mathrm{vis}}(\mathcal B;\mathbf s)$ if and only if it is screened;
\item if every nontrivial simple finitely generated $\mathcal A_{\mathrm{def}}$-module is screened and
$Z_{\mathrm{vis}}(\mathcal B;\mathbf s)\cong \mathbb C$, then $\mathsf{Def}_{\mathrm{vis}}(\mathcal B;\mathbf s)$ has a unique simple object,
namely the vacuum module.
 succeeded in 53ms:
(one generator per negative mode $t^{-m}$, $m \geq 1$).
The resulting bar cohomology at degree~$n$ and weight~$H$
counts the $\mathfrak{sl}_2$-invariant elements
in $\Lambda^n$ of the loop algebra restricted to
total weight~$H$; the net count is $2n+1$
(Computation~\ref{comp:sl2-ce-verification}).

The linear growth $\dim H^n = 2n+1$
supersedes the Riordan prediction
$\dim H^n = R(n+3)$ (OEIS~A005043), which gives the
correct value at $n = 1$ ($R(4) = 3$) but
fails at $n = 2$ ($R(5) = 6 \neq 5$) and
at $n = 3$ ($R(6) = 15 \neq 7$).
A detailed treatment of the three concentration mechanisms
(Whitehead vanishing, Casimir generation, and
weight-by-weight cancellation) appears in the
companion paper~\cite{Lor-GL}.
\end{remark}

\begin{corollary}[Sub-exponential growth characterizes free fields; \ClaimStatusProvedHere]
 succeeded in 53ms:

This gives the one-loop correction with modular invariance.
\end{example}

\begin{theorem}[Modular invariance and anomaly cancellation; \ClaimStatusProvedElsewhere]\label{thm:modular-anomaly}
The string amplitude is modular invariant if and only if the central charge satisfies the anomaly cancellation condition:

For bosonic strings: $c = 26$
For superstrings: $c = 15$

The modular anomaly is computed by:
\[\text{Anomaly} = \frac{c - c_{\text{crit}}}{24} \int_{\mathcal{M}_1} \omega_{\text{moduli}}\]
\end{theorem}

\begin{proof}
The genus-$1$ bar complex transforms covariantly under $\mathrm{SL}_2(\mathbb{Z})$ with weight $c/24$ (Theorem~\ref{thm:modular-invariance}). Modular invariance of the full partition function requires the left-right central charge difference $c - \tilde{c} = 0 \bmod 24$ (for single-valuedness of the phase $e^{2\pi i (c-\tilde{c})/24}$). For the bosonic string ($c = \tilde{c} = 26$) and the superstring ($c = \tilde{c} = 15$), conformal anomaly cancellation arises from Weyl invariance on the worldsheet, not from $c \bmod 24$ alone. This is the Belavin--Knizhnik theorem \cite{BK86}; see also Polchinski \cite[Ch.~5]{Pol98} for the standard textbook treatment.
\end{proof}


\subsection{\texorpdfstring{Modular invariance under $SL_2(\mathbb{Z})$}{Modular invariance under SL-2(Z)}}
exec
/bin/zsh -lc "sed -n '2280,2300p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
 increasingly complex OPE structure of higher $\mathcal{W}$-algebras.
\end{itemize}
\end{proof}

\begin{corollary}[Central charge complementarity sum for \texorpdfstring{$\mathcal{W}_N$}{WN}; \ClaimStatusProvedHere]
\label{cor:wn-complementarity}
Under the Feigin--Frenkel duality $k \mapsto k' = -k - 2N$:
\begin{equation}\label{eq:wn-kappa-sum}
\kappa(\mathcal{W}_N^k) + \kappa(\mathcal{W}_N^{k'})
= (H_N - 1) \cdot (c + c')
= (H_N - 1) \cdot 2(N{-}1)(2N^2{+}2N{+}1)
\end{equation}
In particular, $\kappa + \kappa' = 0$ if and only if $N = 1$
(the trivial case) or $c + c' = 0$ (which does not occur for
$\mathfrak{sl}_N$ with $N \geq 2$).
\end{corollary}

\begin{proof}
Since $\kappa = c \cdot (H_N - 1)$ and $\kappa' = c' \cdot (H_N - 1)$:
$\kappa + \kappa' = (H_N - 1)(c + c')$.

thinking
**Inspecting lines for issues**

I'm thinking about checking the `bar_cobar_adjunction_curved` for any problematic lines. It’s essential to make sure everything is functioning properly, and I want to take a close look at anything that seems suspicious. I’ll need to break it down line by line to identify potential issues. This will help ensure that it performs as expected. Let’s see what we find!
exec
/bin/zsh -lc "sed -n '4788,4905p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '305,330p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2648,2682p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2090,2130p' chapters/theory/chiral_modules.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\texorpdfstring{$W^{(3)}$}{W3}/\texorpdfstring{$W^{(4)}$}{W4}/\texorpdfstring{$W^{(5)}$}{W5}
pairing locus the stage-$5$ higher-spin problem closes once the
target-$4$ singleton \((3,5;4;0,4)\) is matched.
\end{proposition}

\begin{corollary}[Exact remaining stage-\texorpdfstring{$5$}{5} visible-pairing input
package; \ClaimStatusProvedHere]
\label{cor:winfty-stage5-exact-remaining-input}
Assume the hypotheses of
Corollary~\ref{cor:winfty-stage5-effective-independent-frontier}. Then
the full stage-$5$ higher-spin comparison on \(\mathcal{J}_5^{\mathrm{hs}}\)
closes on the full visible pairing locus if and only if the following
two inputs both hold:
\begin{enumerate}[label=\textup{(\roman*)}]
\item the packaged principal stage-$5$ one-coefficient normal form
 holds;
\item the target-$4$ singleton identity
 \[
 \mathsf{C}^{\mathrm{res}}_{3,5;4;0,4}(5)
 =
 succeeded in 52ms:
More generally, $X_V$ is a subvariety of the jet scheme
$J_\infty(\mathrm{Specm}\, A(V))$, where $A(V)$ is the Zhu algebra.
\end{definition}

\begin{theorem}[Arakawa's rationality criterion for admissible affine simples {\cite{Arakawa17,Zhu96}}; \ClaimStatusProvedElsewhere]
\label{thm:arakawa-rationality}
\index{Arakawa!rationality criterion}
\index{associated variety!rationality criterion}
Let $V$ be a vertex algebra satisfying Zhu's $C_2$-cofiniteness
condition \textup{(}$\dim V / C_2(V) < \infty$, where
$C_2(V) = \mathrm{span}\{a_{(-2)} b\}$\textup{)}. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $X_V = \{0\}$ if and only if $V$ is $C_2$-cofinite.
\item If $V$ is $C_2$-cofinite, then $V$ has finitely many simple
 modules \textup{(}Zhu~\cite{Zhu96}\textup{)}.
 \emph{Rationality} (that every grading-restricted module is
 completely reducible) is a strictly stronger condition; the
 triplet algebras $\mathcal{W}(p)$ are $C_2$-cofinite but
 \emph{not} rational
 \textup{(}see Example~\ref{ex:triplet-logarithmic}\textup{)}.
 succeeded in 52ms:
to strict chiral). Chiral Koszulness \emph{is} effective descent
for~$B_\kappa$: on the Koszul locus the cosimplicial bar-cobar
resolution converges and $\Phi$ is an equivalence; off it, passage to
the coderived category is required
(\S\ref{subsec:positselski-chiral-equivalence}).
\end{remark}

\medskip

\subsubsection{Factorization homology concentration}

Since the bar complex \emph{is} factorization homology
(Proposition~\ref{prop:bar-fh}), Koszulness acquires a homological
characterization.

\begin{theorem}[Factorization homology concentration;
\ClaimStatusProvedHere]\label{thm:fh-concentration-koszulness}
\index{Koszulness!factorization homology characterization}
\index{factorization homology!concentration and Koszulness}
Let $\cA$ be a chiral algebra on a smooth curve~$X$ satisfying the
 succeeded in 52ms:
the rows of the double complex are
$\cA \leftarrow \cA \otimes \cC \leftarrow \cA \otimes \cC^{\otimes 2}
\leftarrow \cdots$, which is the bar-type resolution of the
augmentation map. This is the chiral analogue of
\cite[Lemma~2.2.5]{LV12}.
\end{proof}

\begin{lemma}[Right twisted tensor product as mapping cone; \ClaimStatusProvedHere]
\label{lem:twisted-product-cone-unit}
\index{twisted tensor product!mapping cone}
Under the same hypotheses, there is a natural identification
\[
K_\tau^R(\cC,\cA) \;\simeq\; \operatorname{Cone}(\eta_\tau)[-1]
\]
where $\eta_\tau\colon \cC \to \bar{B}_X(\cA)$ is the canonical
unit. In particular, $K_\tau^R$ is acyclic if and only if
$\eta_\tau$ is a weak equivalence.
\end{lemma}

\begin{proof}

thinking
**Exploring mathematical concepts**

I’m looking into the bar cobar adjunction and its related theorems, specifically the necessity and sufficiency of certain conditions. I want to understand the inversion theorem's proof, but I feel like I might need more context or lines from the proof to fully grasp it. Let’s take some time to read through the remainder carefully to see if it clarifies the concepts further! There's definitely a lot to unpack here.
exec
/bin/zsh -lc "sed -n '2682,2725p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
$H^*(\int_{\Sigma_g}\cA)$ in degree~$0$.
Converse: at $g = 0$, concentration of
$\int_{\mathbb{P}^1}\cA \simeq |\barBgeom(\cA)|$
forces the bar spectral sequence to collapse, giving
Koszulness by Theorem~\ref{thm:pbw-koszulness-criterion}.
\end{proof}

\begin{remark}[Goodwillie filtration]\label{rem:goodwillie-tower-fh}
The factorization homology $\int_X \cA$ admits a Goodwillie-type filtration
by configuration number:
\[
 \textstyle\int_X \cA \;\simeq\;
 \cA \;\oplus\;
 \Conf_2(X) \otimes_{S_2} (s^{-1}\bar{\cA})^{\otimes 2}
 \;\oplus\;
 \Conf_3(X) \otimes_{S_3} (s^{-1}\bar{\cA})^{\otimes 3}
 \;\oplus\; \cdots
\]
The bar spectral sequence
(Theorem~\ref{thm:bar-cobar-inversion-qi}) \emph{is} the spectral



thinking
**Investigating theorem correctness**

I'm working through some theorems, particularly focusing on the chiral_koszul_pairs lemma, which seems fine. However, I suspect some examples could point to genuine issues. I noticed a potential problem in yi_higher_body_couplings and need to check for duplicates in the synthesis documents. I also came across the central localization criterion, which appears sound. While there are local proofs, they don’t confirm the converse. The user wants me to verify all claims in the file, so no assumptions can be made.
thinking
**Clarifying theorem proofs**

I see that the local proof establishes that trivial-weight, rational-CFT, and orbifold constructions create modular-invariant examples, but it doesn’t prove the converse. So, I should replace the theorem with one-way sufficient conditions or note "ProvedElsewhere" and remove the local proof sketch, pointing to the explicit citation instead. 

For the specific task about proving direction: since the local proof does only provide a forward direction, that's noted. The Arakawa rationality theorem suggests rationality according to a cited theorem but lacks a local proof. I think I should look for more issues in areas like deformation quantization examples and other listed topics.
thinking
**Evaluating proof strategies**

I’m thinking that while many proofs may be short, they might need to be more direct. I could use a heuristic: if the proof confirms equality \(d1 = [\kappa,-]\) and states survival if and only if the kernel is established, that should be direct. The corollary involving \(\kappa=0\) raises concerns. 

Additionally, the anomaly-physical genus zero corollary in bv_brst, which relies on a lemma and the equivalence between \(\kappa_{tot}=0\) and \(c=26\), seems like it might be direct based on the formula. That could potentially check out!
codex
I’m separating two failure modes. One is the strict AP36 case: a local proof only supports one direction. The other is a manuscript-surface failure: an `iff` claim sits in a theorem block with no proof or only a hand-wave, so the converse is not actually established on the page. I’m only turning these into findings when the file contents themselves make that deficiency explicit.
exec
/bin/zsh -lc "sed -n '2848,2905p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '820,870p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
Equivalently, $\dalg(\cA) = 0$ if $m_k = 0$ for all
$k \ge 3$ (formal); $\dalg(\cA) = 1$ if $m_3 \neq 0$ but
$m_k$ for $k \ge 4$ is determined by $m_2$ and $m_3$; and
$\dalg(\cA) \ge 2$ if independent higher operations exist
beyond~$m_3$.
\end{definition}

\begin{theorem}[Classification by shadow depth; \ClaimStatusProvedHere]
\label{thm:classification-shadow-depth}
\index{classification!by shadow depth|textbf}
\index{shadow depth!classification theorem|textbf}
Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra. The shadow
depth\/ $\dalg(\cA)$ classifies\/ $\cA$ into two proved types and
one open case:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textbf{Type~F} \textup{(}formal\textup{):}
 $\dalg(\cA) = 0$, equivalently $m_k = 0$ for all $k \ge 3$.
 The bar complex is the Chevalley--Eilenberg complex of the
 underlying Lie algebra. The $E_1$ dg coalgebra structure is
 formal. Examples: Heisenberg $H_\kappa$, abelian Chern--Simons.
 succeeded in 51ms:
\Theta_{<g}:=\Theta_0+\Theta_1+\cdots+\Theta_{g-1}
\]
solves the Maurer--Cartan equation modulo $F^gL$. Then the genus-$g$ forcing term
\[
R_g(\Theta_{<g})
:=
d_1\Theta_{g-1}
+\frac12\sum_{i=1}^{g-1}[\Theta_i,\Theta_{g-i}]
\]
is $d_0^{\Theta_0}$-closed and determines a canonical obstruction class
\[
\Ob_g(\Theta_{<g})
:=
[R_g(\Theta_{<g})]
\in
H^2\big((\gr_F^gL)^{\Theta_0},d_0^{\Theta_0}\big).
\]
It vanishes if and only if there exists $\Theta_g\in F^gL/F^{g+1}L$ such that
\[
\Theta_{\le g}:=\Theta_0+\cdots+\Theta_g
exec
/bin/zsh -lc "sed -n '1098,1130p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1758,1785p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\subsection{Linearized cocycles}

Let
\[
\delta_{P_c}Q:=[P_c,Q]
\]
be the linearized differential.

\begin{proposition}[Linearized cocycle equations; \ClaimStatusProvedHere]% label removed: prop:W3cocycles
A relevant cochain $Q$ of the form \eqref{eq:QTT}--\eqref{eq:QWW} is a cocycle if and only if
its coefficients satisfy
\begin{align}
r&=u=v=0,\qquad s=3b,\qquad w=b,% label removed: eq:rel1\\
p&=\frac c{24}E,\qquad q=E,% label removed: eq:rel2\\
B&=5C,% label removed: eq:rel3\\
a&=\frac c{12}b+\frac{5c}{4}C-\frac{5c^2}{384}D,% label removed: eq:rel4\\
A&=\frac c{12}C-\frac{c^2}{2304}D.% label removed: eq:rel5
\end{align}
Hence the cocycle space $Z^1_{\mathrm{rel}}(W_3)$ is $4$-dimensional with free parameters
\[
 succeeded in 51ms:
\[
 \mu_k^* \colon \CoHA(Q, W) \;\xrightarrow{\;\simeq_{E_1}\;}\; \CoHA(Q', W')
\]
is an $\Eone$ quasi-isomorphism of associative dg algebras. The proof has four steps: (a)~mutation is a derived equivalence $\Phi_k \colon D^b(\mathrm{Jac}(Q,W)) \xrightarrow{\sim} D^b(\mathrm{Jac}(Q',W'))$ (Keller--Yang); (b)~derived equivalences of CY$_3$ categories preserve the cyclic $\Ainf$-structure; (c)~the cyclic $\Ainf$-structure determines the $\Eone$-CoHA multiplication; (d)~therefore $\mu_k$ induces an $\Eone$-algebra quasi-isomorphism on critical cohomology. On the charge lattice $\Gamma = \Z^{Q_0}$, mutation acts by $\mu_k(e_i) = e_i$ for $i \neq k$ and $\mu_k(e_k) = -e_k + \sum_{i \to k} e_i$. BPS invariants transform as $\Omega(\gamma;\sigma_+) = \Omega(\mu_k(\gamma);\sigma_-)$. Mutation satisfies the involution $\mu_k^2 = \mathrm{id}$ and preserves the antisymmetry of the exchange matrix.

\noindent\textit{Verification}: 155 tests in \texttt{test\_mutation\_e1\_equivalence.py}, verifying 16 independent paths including: mutation involution, exchange matrix antisymmetry, derived equivalence functor, cyclic $\Ainf$-preservation, $\Eone$ product compatibility, BPS spectrum transformation, and explicit conifold/local-$\bP^2$/$\C^3/\Z_2{\times}\Z_2$ computations (\texttt{mutation\_e1\_equivalence.py}).
\end{proposition}


\begin{theorem}[KS wall-crossing $=$ homotopy colimit $=$ MC gauge equivalence]
\label{thm:ks-mc-gauge}
\ClaimStatusProvedHere{}
For a CY$_3$ category $\cC$ with charge lattice $\Gamma$ and central charge $Z$, the following three formulations of Donaldson--Thomas theory are equivalent:
\begin{enumerate}[label=\textup{(\Roman*)}]
 \item \textbf{KS wall-crossing.} The DT partition function $Z_{\DT}(\cC, \sigma)$ is computed by the ordered product $\prod_{\arg Z(\gamma) \downarrow} E(X^\gamma)^{\Omega(\gamma)}$ of quantum dilogarithm factors in the quantum torus, with transitions across walls governed by the Kontsevich--Soibelman pentagon identity.
 \item \textbf{$\Eone$ homotopy colimit.} The global algebra $A_\cC = \operatorname{hocolim}_{\mathrm{Stab}} \CoHA$ is the homotopy colimit of the CoHA diagram over the stability manifold, with transition maps $K_\cW$ for each wall~$\cW$.
 \item \textbf{$\Eone$ MC equation.} There exists $\Theta^{\Eone}_\cC \in \mathrm{MC}(\mathrm{Def}^{\Eone}_{\mathrm{cyc}}(\cC))$ satisfying $D \cdot \Theta + \frac{1}{2}[\Theta, \Theta] = 0$, encoding all chambers simultaneously.
\end{enumerate}
The equivalences (I)$\leftrightarrow$(II) and (II)$\leftrightarrow$(III) hold as follows. (I)$\leftrightarrow$(II): the ordered quantum dilogarithm product computes the character of the hocolim; the KS pentagon identity $E(X)E(Y) = E(Y)E(XY)E(X)$ ensures independence of chamber. \emph{Critical distinction}: the pentagon holds in the quantum torus; the Lie algebra BCH captures only leading-order commutator terms and does NOT reproduce the full pentagon. (II)$\leftrightarrow$(III): the transition maps $K_\cW$ satisfy the cocycle condition if and only if the MC equation holds; the equation $[\Theta, \Theta] = 0$ holds automatically by antisymmetry, and its content is $D^2 = 0$ in the bar complex (a theorem from $\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$). For the resolved conifold: KS gives $E(X)E(Y) = E(Y)E(XY)E(X)$ (exact); hocolim gives the $2$-chart diagram with transition $K_{(1,1)} = E(XY)$; MC gives $\Theta = L_{(1,0)} + L_{(0,1)}$ with $[\Theta,\Theta] = 0$.






thinking
**Evaluating theorem proof**

I'm considering the relative Feynman transform theorem, which has no available proof. The statement seems to rely on equivalences by definition, which raises some questions. The user asked if the converse is actually proven, but since there's no proof, it can’t be validated. I’m thinking that this might need to be downgraded to a proposition or remark. If no proof exists, I have to determine if adjustments should be made or if additional context could help.
thinking
**Analyzing proof flags**

I see there’s a potential for flagging issues. The user mentioned digging deeper after the first findings, which brings up the theorem with no proof. The structured output likely does need to incorporate this. I might want to identify more AP36 failures from longer proofs, as we've found at least one bug. It seems examining statements with short proofs is essential. Also, I’ll need to check for duplicates across files regarding the ym_higher_body_couplings corollary. Lastly, I should confirm if the modular_pva_quantization corollary follows by induction, even without a complete proof.
thinking
**Determining flagging criteria**

I’m contemplating whether to flag this since equivalence is standard from the iterative theorem. If there's no proof, maybe it's still acceptable? The user expects rigorous standards, but I wonder about flagging trivial induction omissions unless they aren't supported. Perhaps I could mention it as low risk? The task is to find all instances of “iff” in theorem environments where the converse isn't proved. Here, the converse is actually proven by multiple applications of a prior theorem that’s omitted. So, maybe we won’t flag it after all since it logically follows.
thinking
**Refining technical terms**

I’m thinking about replacing "equivalent" with "interrelated" and changing "if and only if" to just "if" for precision. There might be other similar terms to adjust. I could look for candidate proofs with words like "immediate" and "exactly," but we need actual findings. I noticed that `kac_moody.tex` doesn’t have a proof for its theorem, which might just be a literature statement. User specifically requested a deep anti-pattern sweep, focusing on claims without proof.
thinking
**Examining theorem details**

I need to inspect more suspicious sections to see if a theorem directly arises from a prior formula. The `free_fields` classification regarding modular invariance seems unsupported and could be a high severity issue. There’s a theorem about `modular invariance and anomaly cancellation`, which has a proof that distinguishes between c mod 24 and c = 26. The statement claims modular invariance only holds if the central charge meets the anomaly cancellation criteria, but the proof contradicts the theorem! This seems to go beyond just AP36.
exec
/bin/zsh -lc "sed -n '235,255p' chapters/examples/deformation_quantization_examples.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '560,595p' chapters/theory/poincare_duality.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '240,270p' chapters/theory/spectral_sequences.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2735,2760p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
supported on the diagonal strata $\{z_i = z_j\}$. The precise formulation
requires working with $\mathcal{D}$-modules or perverse sheaves on $C_3(X)$
rather than literal products of delta distributions (the naive products
$\delta(z_1{-}z_2)\delta(z_2{-}z_3)$, $\delta(z_2{-}z_3)\delta(z_3{-}z_1)$,
$\delta(z_3{-}z_1)\delta(z_1{-}z_2)$ are each well-defined as distributions on $\mathbb{C}^3$,
but they are all supported on the full diagonal $\{z_1=z_2=z_3\}$ and sum to
$3\delta_{123} \neq 0$, so the Arnold relation is \emph{not} preserved by naive Verdier duality
at the level of distributions).
The correct dual statement is that the Verdier dual of the Arnold relation,
viewed as a relation in $H^2(C_3(X))$, yields the corresponding relation in
the homology $H_{2n-2}$ of the Borel--Moore compactification.
\end{computation}

\section{Koszul pairs and symmetric duality}

\begin{proposition}[Chiral Koszul pair via NAP; \ClaimStatusProvedHere]\label{prop:koszul-pair-NAP}
\index{Koszul pair!via non-abelian Poincare duality}
Two chiral algebras $(\mathcal{A}_1, \mathcal{A}_2)$ on $X$ form a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair}) if and only if there exist quasi-isomorphisms of chiral coalgebras:
\begin{align}
\bar{B}^{\text{ch}}(\mathcal{A}_1) &\xrightarrow{\sim} (\mathcal{A}_2)^!\\
 succeeded in 52ms:
\end{enumerate}
The set of admissible weights at level~$k$ is denoted $\mathrm{Adm}_k$.
It is a finite set: $|\mathrm{Adm}_k| < \infty$
(Kac--Wakimoto~\cite{KW88}).
\end{definition}

\begin{theorem}[Representation theory at admissible level \cite{KW88, Arakawa17}; \ClaimStatusProvedElsewhere]
\label{thm:admissible-rep-theory}
\index{admissible level!representation theory}
Let $k = -h^\vee + p/q$ be an admissible level.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(}Kac--Wakimoto~\cite{KW88}\textup{)}
 For each $\Lambda \in \mathrm{Adm}_k$, the simple module
 $\mathcal{L}(\Lambda)$ is the unique irreducible quotient of
 the Verma module $\mathcal{M}(\Lambda)$. These are all the
 simple highest weight modules in the admissible category.
\item \textup{(}Arakawa~\cite{Arakawa17}\textup{)}
 The simple affine vertex algebra $L_k(\mathfrak{g})$ at
 admissible level is rational if and only if the admissible level
 is \emph{non-degenerate}, meaning $X_{L_k(\mathfrak{g})} = \{0\}$
 succeeded in 53ms:
differential.
\end{proof}

\begin{proposition}[Convergence for complete filtrations \cite{Weibel94, Boardman-conditional}; \ClaimStatusProvedElsewhere]
\label{prop:complete-filt-convergence}
Let $(C, F_\bullet)$ be a filtered complex with complete, exhaustive filtration 
bounded below in each degree. The spectral sequence converges to $H_*(C)$ 
(not just to $H_*(\widehat{C})$) if and only if the natural map:
\[
H_*(C) \to \varprojlim_p H_*(C / F_p C)
\]
is an isomorphism (i.e., $\varprojlim^1 H_*(C / F_p C) = 0$).
\end{proposition}


\section{The bar spectral sequence}
\label{sec:bar-spectral-sequence}


\begin{construction}[Bar filtration]
 succeeded in 53ms:
\begin{theorem}[MC elements and quantization; \ClaimStatusProvedElsewhere{} \cite{Kon03,KontsevichSoibelman}]\label{thm:mc-quantization}
Quantizations of $\mathcal{A}_0$ correspond to Maurer--Cartan elements in the 
deformation complex:
\[
\mathrm{Def}(\mathcal{A}_0) = (\mathcal{A}_0[[\hbar]] \otimes \mathfrak{g}_{\chirPois}, d + \hbar\{\alpha, -\})
\]
Two quantizations are gauge-equivalent if and only if their MC elements are related by the
gauge action.
\end{theorem}

\begin{computation}[MC equation in coordinates]\label{comp:mc-coords}
For the classical Heisenberg Poisson algebra with $\{p, q\} = 1$:

The Poisson bivector $\pi = \partial_p \wedge \partial_q$ is the leading-order MC element. The Kontsevich star product $f \star g = fg + \frac{\hbar}{2}\{f,g\} + O(\hbar^2)$ arises from the formal MC element $\alpha = \hbar\pi + O(\hbar^2)$ in the Hochschild cochain complex.

The MC equation $d\alpha + \frac{1}{2}[\alpha, \alpha] = 0$ at order $\hbar^2$ requires $\frac{1}{2}[\pi, \pi] = 0$, which is the Jacobi identity for the Poisson bracket. Since $\{p,q\} = 1$ is constant, $[\pi,\pi] = 0$ trivially, and $\alpha = \hbar\pi$ is an exact MC element giving the Weyl (Moyal) quantization.
\end{computation}


\section{Explicit deformation quantization computations}

thinking
**Exploring duality proofs**

I’m thinking about the Poincaré duality property and the fact that it doesn’t seem to have a proof. That’s kind of suspicious, right? I wonder if there’s a solid definition behind it. It’s possible that the theorem's equivalence stems from its definition. I should probably take the time to investigate the definition of a chiral Koszul pair and search for more information around this topic. There’s definitely more to uncover!
exec
/bin/zsh -lc 'rg -n "def:chiral-koszul-pair|Definition.*chiral Koszul pair" -n chapters/theory/poincare_duality.tex chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/poincare_duality.tex:492:$\mathcal{A}$ is Koszul (Definition~\ref{def:chiral-koszul-pair}),
chapters/theory/poincare_duality.tex:577:Two chiral algebras $(\mathcal{A}_1, \mathcal{A}_2)$ on $X$ form a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair}) if and only if there exist quasi-isomorphisms of chiral coalgebras:
chapters/theory/chiral_koszul_pairs.tex:140:pair (Definition~\ref{def:chiral-koszul-pair}) is then defined,
chapters/theory/chiral_koszul_pairs.tex:625:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:687:Definition~\ref{def:chiral-koszul-pair} yields the Koszul pair
chapters/theory/chiral_koszul_pairs.tex:1119:\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})}.
chapters/theory/chiral_koszul_pairs.tex:3654:the sense of Definition~\textup{\ref{def:chiral-koszul-pair}}.
chapters/theory/chiral_koszul_pairs.tex:3694:Definition~\ref{def:chiral-koszul-pair} identifies
chapters/theory/chiral_koszul_pairs.tex:5474:Definition~\ref{def:chiral-koszul-pair} axiomatises this
chapters/theory/chiral_koszul_pairs.tex:5487:(Definition~\ref{def:chiral-koszul-pair}) extracts exactly this
exec
/bin/zsh -lc "sed -n '625,680p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
\index{Koszul pair!chiral|textbf}
A \emph{chiral Koszul pair} on a smooth projective curve~$X$
is a pair of chiral Koszul data
\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
Definition~\textup{\ref{def:chiral-koszul-morphism})}
\[
(\cA_1, \cC_1, \tau_1, F_\bullet), \qquad
(\cA_2, \cC_2, \tau_2, F_\bullet)
\]
equipped with Verdier-compatible factorization-algebra
identifications
\[
\mathbb{D}_{\operatorname{Ran}}(\cC_1) \simeq \Omega_X(\cC_2),
\qquad
\mathbb{D}_{\operatorname{Ran}}(\cC_2) \simeq \Omega_X(\cC_1),
\]
compatible with the twisting morphisms and filtrations.
In this situation we write $\cA_2 \simeq \cA_1^!$ and
$\cA_1 \simeq \cA_2^!$.

thinking
**Investigating proof details**

I think I should focus on proofs that are only 3-7 lines long, avoiding direct equality in theorem statements. We already have some examples of those. 

Oh, there might be a bug in the proof related to `cor:winfty-stage5-one-defect-family`. It mentions subtracting the residue-side one-coefficient normal form from the principal-side, concluding the entire defect family vanishes if D5 equals zero. The explicit formulas indicate each defect equals zero or a scalar multiple of D5, which supports the "if and only if" statement. 

I should check the potential bugs from the `anomaly_completed_core` corollary and inspect the direct definition.
exec
/bin/zsh -lc "sed -n '242,261p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '236,255p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1795,1810p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '440,470p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\]
Any such \(h_{M}\) will be called a \emph{neutralization} of the \(\Theta\)-action on \(M\).
\end{definition}

\begin{corollary}[Obstruction class; \ClaimStatusProvedHere]
% label removed: cor:tholog-obstruction-class
A left dg \(B\)-module \(M\) is \(\Theta\)-neutralizable if and only if
\[
[\Theta_{M}]=0\in H^{2}\underline{\operatorname{End}}_{B}(M)
=\operatorname{Ext}^{2}_{B}(M,M).
\]
\end{corollary}

\begin{proof}
By definition, \(M\) is neutralizable if and only if \(\Theta_{M}\) is a coboundary in the dg algebra \(\underline{\operatorname{End}}_{B}(M)\).
\end{proof}

\begin{corollary}[Moduli of neutralizations; \ClaimStatusProvedHere]
% label removed: cor:tholog-moduli-neutralizations
If \(M\) is \(\Theta\)-neutralizable, then the set of homotopy classes of neutralizations of \(M\) is an affine space over
 succeeded in 53ms:
\[
d_{\underline{\operatorname{End}}}(h_{M})=\Theta_{M}.
\]
Any such \(h_{M}\) will be called a \emph{neutralization} of the \(\Theta\)-action on \(M\).
\end{definition}

\begin{corollary}[Obstruction class; \ClaimStatusProvedHere]
\label{cor:tholog-obstruction-class}
A left dg \(B\)-module \(M\) is \(\Theta\)-neutralizable if and only if
\[
[\Theta_{M}]=0\in H^{2}\underline{\operatorname{End}}_{B}(M)
=\operatorname{Ext}^{2}_{B}(M,M).
\]
\end{corollary}

\begin{proof}
By definition, \(M\) is neutralizable if and only if \(\Theta_{M}\) is a coboundary in the dg algebra \(\underline{\operatorname{End}}_{B}(M)\).
\end{proof}

\begin{corollary}[Moduli of neutralizations; \ClaimStatusProvedHere]
 succeeded in 53ms:
\end{proof}

\subsection{The holomorphic BF model on $S^3$}
\label{subsec:holomorphic-bf-model-on-s3}

Specialization to Zeng's holomorphic BF model on $S^3$ \cite{ZengTwistedHolography}.

\begin{definition}[The CR-cohomological boundary algebra]
\label{def:cr-cohomological-boundary-algebra}
Let
\[
A:=\Hb = H_b^{0,0}(S^3)\oplus H_b^{0,1}(S^3).
\]
By the harmonic decomposition of the tangential Cauchy--Riemann complex and the computation
of CR cohomology, one has
\[
H_b^{0,0}(S^3)\cong \C[w_1,w_2],
\qquad
H_b^{0,1}(S^3)\cong \C[\ov w_1,\ov w_2]\,\epsilon,
\]
 succeeded in 53ms:
Assume the modular deformation package of the holomorphic BF boundary algebra is
loop-generated, and fix a regularization scheme for which the completed one-wheel
representative $W_1(A_{\mathrm{BF}})$ is defined. Then the resulting cohomology
class $\mathfrak{W}(A_{\mathrm{BF}}) = [W_1(A_{\mathrm{BF}})]$ satisfies:
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\mathfrak{W}(A_{\mathrm{BF}})$ is a well-defined element of
 $H^2(\mathfrak{g}^{(1)}_{A_{\mathrm{BF}}}, d_\pi)$.
\item The first obstruction to genus-$1$ lifting is
 $\Obs_1(A_{\mathrm{BF}}) = \mathfrak{W}(A_{\mathrm{BF}})$.
\item A genus-$1$ lift exists if and only if $\mathfrak{W}(A_{\mathrm{BF}}) = 0$.
\end{enumerate}
\end{theorem}

\begin{proof}
Under the stated hypotheses, Theorem~\ref{thm:one-wheel-reduction} gives that the
chosen completed one-wheel representative $W_1(A_{\mathrm{BF}})$ is $d_\pi$-closed
exec
/bin/zsh -lc "sed -n '1810,1828p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_celestial_holography_extensions.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chosen completed one-wheel representative $W_1(A_{\mathrm{BF}})$ is $d_\pi$-closed
and that its cohomology class agrees with the first obstruction class. This gives
\textup{(i)} and \textup{(ii)}. Part \textup{(iii)} is then the genus-$1$
vanishing criterion from Corollary~\ref{cor:vanishing-criterion-and-additivity}.

No regularization-independence theorem for BF is proved in this chapter: the point
here is only that once a loop-generated regularization surface has been fixed and
$W_1(A_{\mathrm{BF}})$ is defined there, its cohomology class governs the genus-$1$
obstruction.
\end{proof}

\begin{conjecture}[BF modular lifting; \ClaimStatusConjectured]
\label{conj:bf-modular-lifting}
The holomorphic BF boundary algebra lifts to all genera: the full obstruction
tower vanishes, equivalently the boundary modular Maurer--Cartan problem admits
a full solution $\Pi(\h)$. In particular, the genus-$1$ obstruction
$\mathfrak{W}(A_{\mathrm{BF}})$ vanishes.
\end{conjecture}



thinking
**Evaluating the theorem and corollaries**

I'm considering the theorem and its corollary and whether the corollary provides an "if and only if" condition. I should inspect it closely. The proof snippet ends abruptly, leaving me curious if there's more. It seems the theorem states "Q is a cocycle iff coefficients satisfy relations" is likely okay if computations are complete. However, there's a potential issue since the `relative_feynman_transform` theorem lacks proof. I have to think about changing the theorem's classification or possibly omitting some details to avoid confusion.
thinking
**Inspecting propositions and proofs**

I think I need to take a closer look at the `cy_to_chiral` proposition, specifically the `prop:center-hocolim`, which has a proof that's only five lines long. I’m on the fence about whether it's solid or if there are issues that need addressing. It could be okay, but I want to make sure I thoroughly inspect it to avoid missing anything important. Let's see what I can find with a closer examination.
exec
/bin/zsh -lc "sed -n '1420,1445p' /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

The Drinfeld center does not commute with homotopy colimits. This failure is the categorical origin of the $\Eone$ structure.

\begin{proposition}[Center-hocolim non-commutation]
\label{prop:center-hocolim}
\ClaimStatusProvedHere{}
For a CY$_3$ category $\cC$ with multi-chart atlas $\cA = \{(Q_\alpha, W_\alpha)\}_{\alpha \in I}$, the canonical map
\[
 \operatorname{hocolim}_\alpha \, \cZ\bigl(\Rep^{\Eone}(\CoHA_\alpha)\bigr) \;\longrightarrow\; \cZ\bigl(\Rep^{\Eone}(\operatorname{hocolim}_\alpha \CoHA_\alpha)\bigr)
\]
is \emph{not} an equivalence in general. Its cofiber, the \emph{global braiding obstruction}
\[
 \mathrm{Obs}(\cC) \;:=\; \mathrm{cofib}\!\bigl(\operatorname{hocolim}_\alpha \cZ_\alpha \to \cZ_{\mathrm{global}}\bigr),
\]
is zero if and only if $\cC$ has a single stability chamber ($|I| = 1$). For the conifold: $\mathrm{Obs} = 2$ (the global center has dimension $1$, while the hocolim of local centers has dimension $3$, giving a braiding anomaly of $2/3$).
\end{proposition}

\begin{proof}
For $|I| = 1$ (single chart, e.g.\ $\C^3$): the hocolim is the identity, and both sides agree. For $|I| \geq 2$: the hocolim $A = \operatorname{hocolim}_\alpha A_\alpha$ identifies elements across charts via the wall-crossing automorphisms $K_{\alpha\beta}$. The global center $\cZ(\Rep^{\Eone}(A))$ consists of elements that commute with \emph{all} of $A$, including the gluing data. But the hocolim of local centers $\operatorname{hocolim}_\alpha \cZ(A_\alpha)$ contains elements that commute locally (within each chart) but may fail to commute with the transition maps. The difference is precisely the braiding data that lives on the walls.



thinking
**Evaluating theorem details**

I need to carefully consider the theorem and its proof, as there might not be a solid citation available. The statements regarding the shadow depth and pole structure seem significant. However, without proof, I can't confirm the converse, which may not fulfill the user’s request. I think I should focus on splitting the theorem into proven directions, or perhaps downgrading it to a heuristic. The user asked for an exact fix, so maybe I can propose replacing the final two sentences with clearer implications.
thinking
**Examining theorem accuracy**

I could phrase it like: "The shadow depth is determined by the pole structure of the OPE: if all OPE poles are simple, then d_alg=0; if the maximal pole order is 2 and the residue is scalar, then d_alg<=1." However, this might be more than just a simplification. I need to ensure I'm being precise. I think it would also be worthwhile to take a closer look at the common-sheet-law theorem, especially its 3-line proof, which feels a bit suspicious.
exec
/bin/zsh -lc "sed -n '33596,33622p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '20452,20478p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{proof}

\subsection{Quadratic sheet calculus}
\label{subsec:quadratic-sheet-calculus}
\index{quadratic spectral regime}

Let $L = F(u)$ with $u^2 = \Delta(x) \in F^\times$ and $\Delta$
not a square in~$F$. Every $y = a + bu \in L$ decomposes into an
even part~$a$ and an odd part~$bu$.

\begin{theorem}[Common-sheet multiplication law; \ClaimStatusProvedHere]
\label{thm:common-sheet-law}
For $y_1 = a_1 + b_1 u$ and $y_2 = a_2 + b_2 u$ on the same
quadratic sheet:
\[
y_1 y_2 = (a_1 a_2 + \Delta b_1 b_2)
 + (a_1 b_2 + a_2 b_1) u.
\]
In particular, $y_1 y_2 \in F$ if and only if
$a_1 b_2 + a_2 b_1 = 0$; if both factors are purely odd, then
exec
/bin/zsh -lc "sed -n '21798,21882p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\end{tabular}

\smallskip\noindent
{\small The self-dual central charge $K_N/2$ grows as
$2N^3$ for large~$N$.}
\end{center}


\begin{proposition}[Anomaly-free characterisation of the Koszul conductor]
\label{prop:koszul-conductor-anomaly-vanishing}
\ClaimStatusProvedHere
\index{Koszul conductor!anomaly-free characterisation|textbf}%
\index{gravitational anomaly!Koszul conductor}%
Let $\cA$ be a chirally Koszul chiral algebra in the standard landscape.
\begin{enumerate}[label=\textup{(\roman*)}]
\item $\kappa(\cA) + \kappa(\cA^!) = 0$ if and only if $\cA$
 belongs to an anomaly-free family: affine Kac--Moody $V_k(\fg)$,
 Heisenberg $\mathcal{H}_k$, free-field $\beta\gamma$/$bc$ pairs,
 or lattice algebras.
\item For the principal $\cW$-algebra
 succeeded in 51ms:
$\kappa(\cA) = \sum_{i=1}^r \kappa_i$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Per-channel universality.}
 The diagonal contribution to the genus-$g$ free energy satisfies
 \begin{equation}\label{eq:multi-weight-diagonal}
 F_g^{\mathrm{diag}}(\cA)
 \;=\;
 \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
 \end{equation}
 for all\/ $g \geq 1$, unconditionally.

\item \emph{Cross-channel decomposition.}
 The full genus-$g$ free energy decomposes as
 \begin{equation}\label{eq:multi-weight-decomposition}
 F_g(\cA)
 \;=\;
 \kappa(\cA) \cdot \lambda_g^{\mathrm{FP}}
 \;+\;
 \delta F_g^{\mathrm{cross}}(\cA),
 \end{equation}
exec
/bin/zsh -lc "sed -n '23394,23480p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\eta^{(j)(j)} = j/c$ and structure constants
$C^{\mathrm{grav}}_{(i)(j)(k)} = c\,\delta_{ijk}^{\mathrm{even}}$
\textup{(}nonzero only when the number of odd-weight indices
is even, reflecting the\/ $\mathbb{Z}_2$ parity of
odd-spin generators\textup{)}.
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Closed-form formula.}
 The genus-$2$ gravitational cross-channel correction is
 \begin{equation}\label{eq:universal-grav-cross-N}
 \boxed{
 \delta F_2^{\mathrm{grav}}(\cW_N, c)
 \;=\;
 \frac{(N{-}2)(N{+}3)}{96}
 \;+\;
 \frac{(N{-}2)(3N^3 + 14N^2 + 22N + 33)}{24c}.
 }
 \end{equation}
 Equivalently,
 \begin{equation}\label{eq:universal-grav-cross-N-combined}
 \delta F_2^{\mathrm{grav}}(\cW_N, c)

thinking
**Investigating potential bugs**

I think there's a potential repeated propagation bug in Vol2, specifically in `ym_synthesis` and `ym_synthesis_core` that probably stems from the same corollary. I need to inspect those to confirm if they contain the same text. If they do, I might not need to make any changes. I should also check for similar propagation bugs around the `cy_to_chiral` theorem and possibly other copies. I’ll search the label `thm:ks-mc-gauge` across the repository to gather more information.
exec
/bin/zsh -lc "rg -n \"thm:ks-mc-gauge|Center-hocolim non-commutation|Persistence criterion for the quadratic law|central charge satisfies the anomaly cancellation condition|Classification by shadow depth;|\\"'$'"\\delta F_2\\"'^'"\\{\\mathrm\\{grav\\}\\}.*if and only if \\"'$N = 2|is zero if and only if '"\\\\cC has a single stability chamber\" chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:thm:ks-mc-gauge|Center-hocolim non-commutation|Persistence criterion for the quadratic law|central charge satisfies the anomaly cancellation condition|Classification by shadow depth;|$\delta F_2\^\{\mathrm\{grav\}\}.*if and only if $N = 2|is zero if and only if \cC has a single stability chamber)
                                                                                                                                                                                                             ^^
error: unrecognized escape sequence
codex
I’ve got three stronger failure clusters now: the mixed-coupling persistence corollaries, the CY `center-hocolim` obstruction theorem, and the free-fields modular-invariance theorems. I’m propagating those searches across duplicate files before I finalize the finding list so the report doesn’t miss mirror copies.
exec
/bin/zsh -lc "rg -n --fixed-strings 'is zero if and only if "'$'"\\cC"'$ has a single stability chamber'"' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'Persistence criterion for the quadratic law' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'The string amplitude is modular invariant if and only if the central charge satisfies the anomaly cancellation condition:' chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'A chiral algebra "'$'"\\mathcal{A}"'$ is modular invariant at genus 1 if and only if one of the following holds:'"' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/free_fields.tex:5155:The string amplitude is modular invariant if and only if the central charge satisfies the anomaly cancellation condition:
 succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1434:is zero if and only if $\cC$ has a single stability chamber ($|I| = 1$). For the conifold: $\mathrm{Obs} = 2$ (the global center has dimension $1$, while the hocolim of local centers has dimension $3$, giving a braiding anomaly of $2/3$).
 succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex:722:\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_higher_body_couplings.tex:254:\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex:765:\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
chapters/connections/ym_higher_body_couplings.tex:254:\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
 succeeded in 53ms:
chapters/examples/free_fields.tex:5296:A chiral algebra $\mathcal{A}$ is modular invariant at genus 1 if and only if one of the following holds:


thinking
**Evaluating implications and conditions**

I’m considering the implications of the relationship between statements (I) and (II). I think the transition maps satisfy the cocycle condition if the MC equation holds. If the MC equation reduces to D^2=0, there might be a possibility for both directions. It seems like the cocycle condition could be encoded by the MC equation, but I’m realizing I don’t have a proof for that yet, which leaves me pondering the details.
thinking
**Searching proofs**

I'm thinking it might be a good idea to search for proofs that contain the term "Forward:" while specifically avoiding any that include "Converse:". It seems like that could help streamline the relevant results. So, I'll move on and get to scripting this search! Let's see where this leads me!
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
for c in cands:
    proof=c['proof'] or ''
    if 'Forward:' in proof and 'Converse:' not in proof and 'converse' not in proof:
        print(f\"{c['path']}:{c['start']} {c['label']} {c['env']}\")
        for ln,txt in c['matches']:
            print(' ',ln,txt)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:


thinking
**Exploring proof patterns**

I’m considering the possibility that proofs may exhibit different patterns. I think I should search specifically for proofs related to "sufficiency" or "necessity" to see what I can find. This could help me categorize or understand different proof approaches. I wonder what insights I'll gain from examining these more focused aspects. Let's see what results I can dig up!
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
for c in cands:
    proof=c['proof'] or ''
    low=proof.lower()
    if ('sufficiency' in low or 'necessity' in low or 'necessary' in low or 'sufficient' in low) and ('converse' not in low and 'iff' not in low and 'if and only if' not in low):
        print(f\"{c['path']}:{c['start']} {c['label']} {c['env']}\")
        for ln,txt in c['matches']:
            print(' ',ln,txt)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_curved.tex:4793 cor:winfty-stage5-exact-remaining-input corollary
  4799 closes on the full visible pairing locus if and only if the following

thinking
**Exploring proofs**

I'm looking into the bar-cobar corollary and how it relates to necessity and sufficiency — no issues found there. I could search for proofs associated with "Immediate from Theorem" after the theorem-level iff. I've discovered the ym corollary but suspect there could be more dubious ones out there. I'll script a list of proofs with "Immediate" and their corresponding statements to clarify everything!
exec
/bin/zsh -lc "python3 - <<'PY'
import json,re
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
for c in cands:
    proof=c['proof'] or ''
    if re.search(r'Immediate|immediate', proof):
        print(f\"{c['path']}:{c['start']} {c['label']} {c['env']}\")
        for ln,txt in c['matches']:
            print(' ',ln,txt)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/ym_higher_body_couplings.tex:254 cor:persistence-criterion-quadratic-law corollary
  256 The quadratic mixed-coupling law survives to first non-quadratic order if and only if
chapters/theory/higher_genus_modular_koszul.tex:18636 cor:discriminant-atlas corollary
  18703 $\Delta = 0 \iff S_4 = 0$ \textup{(}given $\kappa \neq 0$\textup{)},
chapters/theory/ordered_associative_chiral_kd.tex:508 sec:r-matrix-descent-vol1 proposition
  529 it factors through $\Sigma_n$ if and only if~$R$
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer.tex:1201 None proposition
  1208 if and only if there exist unique scalars $a,b\in\mathbb{C}$ such that
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer_core.tex:1190 prop:cbt-first-order-homogeneous proposition
  1197 if and only if there exist unique scalars $a,b\in\mathbb{C}$ such that
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography.tex:451 None corollary
  454 \item A genus-$1$ modular lift exists if and only if $\mathfrak W(A)=0$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_core.tex:421 cor:vanishing-criterion-and-additivity corollary
  424 \item A genus-$1$ modular lift exists if and only if $\mathfrak W(A)=0$.
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:817 None theorem
  837 It vanishes if and only if there exists $\Theta_g\in F^gL/F^{g+1}L$ such that
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:1551 None theorem
  1571 It vanishes if and only if there exists $\Theta_g\in F^gL/F^{g+1}L$ such that
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_higher_body_couplings.tex:254 cor:persistence-criterion-quadratic-law corollary
  256 The quadratic mixed-coupling law survives to first non-quadratic order if and only if

thinking
**Inspecting celestial theories**

I’m considering the celestial_holography corollary, which states a genus-1 lift exists if W(A)=0. The proof seems to come from a previous theorem, so I think I'm okay there. I might want to check the mod_pva theorem as it could provide an immediate criterion from the equation d0 Theta_g = -R_g. I don’t have any issues, but I’ll look for proofs that end with "the vanishing criterion is immediate." I’ll continue inspecting; this is interesting!
exec
/bin/zsh -lc "sed -n '430,460p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_holography_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1190,1220p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/celestial_boundary_transfer_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '810,845p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1500,1602p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\begin{proposition}[homogeneous first-order operators on $\mathbb{C}\lbrack t\rbrack$]
\label{prop:cbt-first-order-homogeneous}
\ClaimStatusProvedHere
Fix an integer $d\ge0$. A linear operator $Q:\mathbb{C}[t]\to\mathbb{C}[t]$ is a first-order differential operator homogeneous of degree $d$, in the sense that
\[
Q(t^B)\in \mathbb{C}\, t^{B+d}\qquad\text{for all }B\ge0,
\]
if and only if there exist unique scalars $a,b\in\mathbb{C}$ such that
\[
Q=a\,t^{d+1}\partial_t+b\,t^d.
\]
Equivalently,
\[
Q(t^B)=(aB+b)t^{B+d}\qquad (B\ge0).
\]
\end{proposition}

\begin{proof}
A first-order differential operator on $\mathbb{C}[t]$ has the form
\[
 succeeded in 53ms:
 This is the codimension-two cancellation axiom
 (Definition~\ref{def:modular-bar-datum}(3)), transported to
 coderivations.
\end{enumerate}
\end{proposition}

\begin{proof}
Part~(i): $\delta_\cA$ is a coderivation
of~$\Bmod$, so it satisfies the Leibniz rule
$\Delta_{\mathrm{sep}} \circ \delta = (\delta \otimes \id +
\id \otimes \delta) \circ \Delta_{\mathrm{sep}}$
with respect to the separating coproduct. Projecting to
genus~$g$ and using genus-additivity across the separating edge
gives the factorisation formula.

Part~(ii): the non-separating clutching map pairs two legs on
a genus-$(g{-}1)$ surface; on $\Bmod$, this is
$D_{\mathrm{nsep}}$, whose coderivation incarnation is
$\Delta_{\mathrm{cyc}}$. The MC equation at genus~$g$
(Theorem~\ref{thm:Obg}) gives
 succeeded in 53ms:
\mathfrak W(A)=\mathfrak W(A_1)\oplus\mathfrak W(A_2).
\]
\end{enumerate}
\end{corollary}

\begin{proof}
Parts \textup{(i)} and \textup{(ii)} are immediate from Theorems
\ref{thm:first-modular-obstruction} and \ref{thm:one-wheel-reduction}. For
\textup{(iii)}, the cyclic pairing and all transferred products split block-diagonally, so every
one-wheel contraction is supported on exactly one summand.
\end{proof}

\subsection{The holomorphic BF model on $S^3$}
\label{subsec:holomorphic-bf-model-on-s3}

Specialization to Zeng's holomorphic BF model on $S^3$ \cite{ZengTwistedHolography}.

\begin{definition}[The CR-cohomological boundary algebra]
\label{def:cr-cohomological-boundary-algebra}
Let
 succeeded in 51ms:
\begin{theorem}[Universal genus-one obstruction; \ClaimStatusProvedHere]\label{thm:Ob1}
Let $\Theta_0\in \MC(\gr_F^0L)$. Then the class
\[
\Ob_1(\Theta_0):=[d_1\Theta_0]
\in
H^2\big((\gr_F^1L)^{\Theta_0},d_0^{\Theta_0}\big),
\qquad
d_0^{\Theta_0}(x):=d_0x+[\Theta_0,x],
\]
is well-defined. The obstruction vanishes,
\[
\Ob_1(\Theta_0)=0
\iff
\exists\,\Theta_1\in F^1L/F^2L
\text{ such that }
\Theta_0+\Theta_1
\]
solves the Maurer--Cartan equation modulo $F^2L$.
\end{theorem}






thinking
**Evaluating proof status**

I need to adjust the last two sentences so they reflect one-way implications or are marked as conjectures since there’s no proof in the excerpt. I should check if there’s a proof hidden further down or if it's all conjectural. It looks like there’s no proof right away, so I can flag this as [HIGH] or [CRITICAL] due to the `ClaimStatusProvedHere` without any supporting evidence.
thinking
**Revising implications**

I’m looking at how to revise a specific sentence, aiming to replace "equivalences" with "implications." However, I'm going back and forth about whether those directions are clearly explained. A possible fix could be: "The three formulations are related as follows. (I) supplies the character of (II); (III) packages the wall data encoded in (II)." But I need to be cautious about asserting implications that aren't rigorously proven. I need to really consider the phrasing and the context before finalizing anything.
thinking
**Refining wording for clarity**

I’m considering another fix to remove the term "equivalence" entirely. For instance, I could say: "The three formulations are compatible: (I) determines the character of (II), and (III) packages the same wall-crossing data when such an MC element exists." This keeps me from asserting unsupported if-and-only-if statements, which is crucial since the user requested a precise fix. I also see that terms like "prop:center-hocolim" lack proof for the converse, so I should choose my wording carefully here.
thinking
**Considering theorem adjustments**

I think the exact fix might involve removing the `iff` clauses or possibly downgrading the theorem. It doesn't seem like a duplicate issue, so that's a good sign! I'm just trying to ensure I’m making the right adjustments while keeping things clear and effective. There’s always a bit of a puzzle when I tweak these things, and I want to make sure it's all working smoothly!
thinking
**Investigating classification duplicates**

I’m noticing that `shadow-depth` is only in Volume 2. I should check if there are other files that might have the same classification theorem. It seems important to search for any duplicates. I want to make sure everything is organized and correctly categorized, so looking into this will help keep things tidy and accurate. Let's explore this further!
exec
/bin/zsh -lc "rg -n --fixed-strings 'The shadow depth is determined by the pole structure of the OPE:' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'The string amplitude is modular invariant if and only if the central charge satisfies the anomaly cancellation condition:' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'The equivalences (I)"'$'"\\leftrightarrow"'$(II) and (II)$'"\\leftrightarrow"'$(III) hold as follows.'"' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'A chiral algebra "'$'"\\mathcal{A}"'$ is modular invariant at genus 1 if and only if one of the following holds:'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:2886:The shadow depth is determined by the pole structure of the OPE:
 succeeded in 51ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1116:The equivalences (I)$\leftrightarrow$(II) and (II)$\leftrightarrow$(III) hold as follows. (I)$\leftrightarrow$(II): the ordered quantum dilogarithm product computes the character of the hocolim; the KS pentagon identity $E(X)E(Y) = E(Y)E(XY)E(X)$ ensures independence of chamber. \emph{Critical distinction}: the pentagon holds in the quantum torus; the Lie algebra BCH captures only leading-order commutator terms and does NOT reproduce the full pentagon. (II)$\leftrightarrow$(III): the transition maps $K_\cW$ satisfy the cocycle condition if and only if the MC equation holds; the equation $[\Theta, \Theta] = 0$ holds automatically by antisymmetry, and its content is $D^2 = 0$ in the bar complex (a theorem from $\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$). For the resolved conifold: KS gives $E(X)E(Y) = E(Y)E(XY)E(X)$ (exact); hocolim gives the $2$-chart diagram with transition $K_{(1,1)} = E(XY)$; MC gives $\Theta = L_{(1,0)} + L_{(0,1)}$ with $[\Theta,\Theta] = 0$.
 succeeded in 51ms:
chapters/examples/free_fields.tex:5296:A chiral algebra $\mathcal{A}$ is modular invariant at genus 1 if and only if one of the following holds:
 succeeded in 51ms:
chapters/examples/free_fields.tex:5155:The string amplitude is modular invariant if and only if the central charge satisfies the anomaly cancellation condition:
exec
/bin/zsh -lc "rg -n --fixed-strings 'thm:classification-shadow-depth' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2856:\label{thm:classification-shadow-depth}
2974:Theorem~\ref{thm:classification-shadow-depth} provides a complete
3008:By Theorem~\ref{thm:classification-shadow-depth}, this central
3202:Theorem~\ref{thm:classification-shadow-depth}, the central double
3246:Theorems~\ref{thm:classification-shadow-depth}

thinking
**Inspecting proof candidates**

I'm thinking about a potential lack of proof for some claims. It seems like I need to examine a theorem, maybe look into conjectures followed by examples. Then I wonder if there are other candidates with the `ClaimStatusProvedHere` designation that also relate to "if and only if." To dig deeper, I'll probably need to search for those and use a script to assist with the analysis!
exec
/bin/zsh -lc "python3 - <<'PY'
import json
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
for c in cands:
    if not c['proof'] and c.get('status')=='ProvedHere':
        print(f\"{c['path']}:{c['start']} {c['env']} {c['label']}\")
        for ln,txt in c['matches']:
            print(' ',ln,txt)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1107 theorem thm:ks-mc-gauge
  1116 The equivalences (I)$\leftrightarrow$(II) and (II)$\leftrightarrow$(III) hold as follows. (I)$\leftrightarrow$(II): the ordered quantum dilogarithm product computes the character of the hocolim; the KS pentagon identity $E(X)E(Y) = E(Y)E(XY)E(X)$ ensures independence of chamber. \emph{Critical distinction}: the pentagon holds in the quantum torus; the Lie algebra BCH captures only leading-order commutator terms and does NOT reproduce the full pentagon. (II)$\leftrightarrow$(III): the transition maps $K_\cW$ satisfy the cocycle condition if and only if the MC equation holds; the equation $[\Theta, \Theta] = 0$ holds automatically by antisymmetry, and its content is $D^2 = 0$ in the bar complex (a theorem from $\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$). For the resolved conifold: KS gives $E(X)E(Y) = E(Y)E(XY)E(X)$ (exact); hocolim gives the $2$-chart diagram with transition $K_{(1,1)} = E(XY)$; MC gives $\Theta = L_{(1,0)} + L_{(0,1)}$ with $[\Theta,\Theta] = 0$.
exec
/bin/zsh -lc "sed -n '2853,2862p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\end{definition}

\begin{theorem}[Classification by shadow depth; \ClaimStatusProvedHere]
\label{thm:classification-shadow-depth}
\index{classification!by shadow depth|textbf}
\index{shadow depth!classification theorem|textbf}
Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra. The shadow
depth\/ $\dalg(\cA)$ classifies\/ $\cA$ into two proved types and
one open case:
\begin{enumerate}[label=\textup{(\roman*)}]

thinking
**Identifying proof issues**

I’m thinking about the parser issue; it may have missed the status that's on the same line as the begin tag. We only search subsequent lines, not the initial one, so that could explain the oversight. This is another case for the "no-proof provedHere" theorem, so I should make sure to include that. Maybe the script could be adjusted for other potential candidates that are missing. I’ll update quickly to ensure we're thorough!
exec
/bin/zsh -lc "python3 - <<'PY'
import re, json
from pathlib import Path
cands=json.loads(Path('/tmp/iff_candidates.json').read_text())
pat_status = re.compile(r'\\\\ClaimStatus([A-Za-z]+)')
for c in cands:
    if not c['status']:
        m=pat_status.search(c['statement'])
        if m: c['status']=m.group(1)
for c in cands:
    if not c['proof'] and c.get('status')=='ProvedHere':
        print(f\"{c['path']}:{c['start']} {c['env']} {c['label']}\")
        for ln,txt in c['matches']:
            print(' ',ln,txt)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/poincare_duality.tex:575 proposition None
  577 Two chiral algebras $(\mathcal{A}_1, \mathcal{A}_2)$ on $X$ form a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair}) if and only if there exist quasi-isomorphisms of chiral coalgebras:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex:855 corollary None
  860 exists if and only if
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex:1589 corollary None
  1594 exists if and only if
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:2855 theorem thm:classification-shadow-depth
  2887 $\dalg(\cA) = 0$ if and only if all OPE poles are simple\textup{;}
  2888 $\dalg(\cA) = 1$ if and only if the maximal pole order is $2$
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1107 theorem thm:ks-mc-gauge
  1116 The equivalences (I)$\leftrightarrow$(II) and (II)$\leftrightarrow$(III) hold as follows. (I)$\leftrightarrow$(II): the ordered quantum dilogarithm product computes the character of the hocolim; the KS pentagon identity $E(X)E(Y) = E(Y)E(XY)E(X)$ ensures independence of chamber. \emph{Critical distinction}: the pentagon holds in the quantum torus; the Lie algebra BCH captures only leading-order commutator terms and does NOT reproduce the full pentagon. (II)$\leftrightarrow$(III): the transition maps $K_\cW$ satisfy the cocycle condition if and only if the MC equation holds; the equation $[\Theta, \Theta] = 0$ holds automatically by antisymmetry, and its content is $D^2 = 0$ in the bar complex (a theorem from $\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$). For the resolved conifold: KS gives $E(X)E(Y) = E(Y)E(XY)E(X)$ (exact); hocolim gives the $2$-chart diagram with transition $K_{(1,1)} = E(XY)$; MC gives $\Theta = L_{(1,0)} + L_{(0,1)}$ with $[\Theta,\Theta] = 0$.

thinking
**Inspecting corollary**

I need to take a look at the modular_PVA corollary, even though there's no proof for it at the moment. It likely follows by induction from the theorem just above it. I’m wondering if I should flag it at all, since maybe the local theorem is sufficient for this situation. It’ll be important to thoroughly inspect the corollary to confirm everything aligns.
exec
/bin/zsh -lc "sed -n '852,866p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1586,1600p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_core.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '571,585p' chapters/theory/poincare_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{computation}

\section{Koszul pairs and symmetric duality}

\begin{proposition}[Chiral Koszul pair via NAP; \ClaimStatusProvedHere]\label{prop:koszul-pair-NAP}
\index{Koszul pair!via non-abelian Poincare duality}
Two chiral algebras $(\mathcal{A}_1, \mathcal{A}_2)$ on $X$ form a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair}) if and only if there exist quasi-isomorphisms of chiral coalgebras:
\begin{align}
\bar{B}^{\text{ch}}(\mathcal{A}_1) &\xrightarrow{\sim} (\mathcal{A}_2)^!\\
\bar{B}^{\text{ch}}(\mathcal{A}_2) &\xrightarrow{\sim} (\mathcal{A}_1)^!
\end{align}

where $\mathcal{A}_i^!$ is defined via Verdier duality as in Construction \ref{const:A-dual-intrinsic}.

\emph{Equivalent characterization (NAP).}
 succeeded in 53ms:
criterion is immediate.
\end{proof}

\begin{corollary}[Full modular lift criterion; \ClaimStatusProvedHere]
A full modular Maurer--Cartan lift
\[
\Theta=\Theta_0+\Theta_1+\Theta_2+\cdots\in \MC(L)
\]
exists if and only if
\[
\Ob_g(\Theta_{<g})=0
\qquad\text{for all }g\ge 1.
\]
\end{corollary}

 succeeded in 53ms:
criterion is immediate.
\end{proof}

\begin{corollary}[Full modular lift criterion; \ClaimStatusProvedHere]
A full modular Maurer--Cartan lift
\[
\Theta=\Theta_0+\Theta_1+\Theta_2+\cdots\in \MC(L)
\]
exists if and only if
\[
\Ob_g(\Theta_{<g})=0
\qquad\text{for all }g\ge 1.
\]
\end{corollary}






thinking
**Considering definitions and direction**

I’m thinking about how definitions can provide forward direction in understanding concepts, maybe guiding our thought processes. But I'm also wondering about the idea that conversing might not always lead to concrete proof. It's curious how certain discussions can illuminate or complicate ideas! So, I'm contemplating the nuances here, trying to piece together the significance in both definitions and conversations. There’s a lot to unpack!
thinking
**Searching for theorems and proofs**

I'm looking for theorem statements that use "is zero if and only if" and find proofs containing examples like "For the conifold." It’s interesting that I might also consider candidates like "Landscape census" or "subexp free-field," which could involve table enumeration. I noticed that my "thm:classification-shadow-depth" doesn't have a proof, which is a bit disappointing, but it's good to keep track of these things!
thinking
**Evaluating theorem status**

I'm examining a pure mathematical theorem that seems suspect. For AP36, the equivalence directions haven't been locally proven, so I might need to downgrade it to a proposition or remark with conditional phrasing. The content has a theorem body but lacks a proof, which is an issue. I’m considering whether the "ks-mc-gauge" theorem's proof might link to the cocycle condition, but it’s not adequately demonstrated. I need to pinpoint specific references for clarity.
thinking
**Exploring equivalency in equations**

I’m considering whether `[\Theta,\Theta]=0` is automatic and how it relates to the content `D^2=0` in the bar complex. If D is defined from transition maps, could it mean that `D^2=0` is equivalent to satisfying the cocycle condition? It's an interesting thought, but I realize this hasn’t been formalized yet. I need to be careful about making assumptions without proper proof or clarification.
thinking
**Adjusting wording for clarity**

I'm thinking about fixing my phrasing by replacing "if and only if" with "then," especially after a proposition. That feels more grounded. Now, let’s check if the proposition ended without proof and if the next theorem follows. Oh yes, it did end! So, I’m feeling good about this change and ready to move forward. Sometimes a little tweak can make a big difference in clarity!
codex
I’ve now re-read the strongest candidate failures in context. The remaining work is converting them into a clean, source-grounded finding list with exact weakening text, and I’m doing one last pass for duplicates so the final report doesn’t miss propagated copies.
exec
/bin/zsh -lc "rg -n --fixed-strings 'KS wall-crossing "'$=$ homotopy colimit $=$ MC gauge equivalence'"' /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'Two chiral algebras "'$('"\\mathcal{A}_1, \\mathcal{A}_2)"'$ on $X$ form a chiral Koszul pair'"' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'The shadow depth is determined by the pole structure of the OPE:' chapters /Users/raeez/chiral-bar-cobar-vol2/chapters /Users/raeez/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'A left dg \\(B\\)-module \\(M\\) is \\(\\Theta\\)-neutralizable if and only if' /Users/raeez/chiral-bar-cobar-vol2/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/poincare_duality.tex:577:Two chiral algebras $(\mathcal{A}_1, \mathcal{A}_2)$ on $X$ form a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair}) if and only if there exist quasi-isomorphisms of chiral coalgebras:
 succeeded in 52ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1107:\begin{theorem}[KS wall-crossing $=$ homotopy colimit $=$ MC gauge equivalence]
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_core.tex:244:A left dg \(B\)-module \(M\) is \(\Theta\)-neutralizable if and only if
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/anomaly_completed_topological_holography.tex:248:A left dg \(B\)-module \(M\) is \(\Theta\)-neutralizable if and only if
 succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:2886:The shadow depth is determined by the pole structure of the OPE:

thinking
**Analyzing anomaly data**

I think the corollary regarding the anomaly seems acceptable, so there's no need for immediate concern. I should focus on gathering exact line numbers using the `nl -ba` command for each finding. It might be better to handle this in batches to stay organized and efficient. That way, I can keep track of everything more clearly and ensure I'm not missing anything important. Let's get started on that!
exec
/bin/zsh -lc "nl -ba chapters/connections/ym_higher_body_couplings.tex | sed -n '248,262p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_higher_body_couplings.tex | sed -n '248,262p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex | sed -n '761,773p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex | sed -n '718,730p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   248	\[
   249	d = [m,-] = [m^{(0)},-] + [m^{(1)},-] + [m^{(2)},-] + \cdots.
   250	\]
   251	The zeroth differential on the associated graded is therefore $d_0=[m^{(0)},-]$, and the first derived differential is induced by the next term $[m^{(1)},-]$. By Definition~\ref{def:mixed-kodaira-spencer-class}, the cohomology class of $m^{(1)}$ is precisely $\kappa_{\mathrm{mix}}$, so on the $E_1$-page the first differential is the adjoint action of $\kappa_{\mathrm{mix}}$.
   252	\end{proof}
   253	
   254	\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
   255	\label{cor:persistence-criterion-quadratic-law}
   256	The quadratic mixed-coupling law survives to first non-quadratic order if and only if
   257	\[
   258	\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0.
   259	\]
   260	More generally, if the mixed coderivation components $m^{(1)},\dots,m^{(r)}$ vanish in relative Hochschild cohomology, then the mixed-weight spectral sequence degenerates through $E_{r+1}$.
   261	\end{corollary}
   262	
 succeeded in 51ms:
   248	\[
   249	d = [m,-] = [m^{(0)},-] + [m^{(1)},-] + [m^{(2)},-] + \cdots.
   250	\]
   251	The zeroth differential on the associated graded is therefore $d_0=[m^{(0)},-]$, and the first derived differential is induced by the next term $[m^{(1)},-]$. By Definition~\ref{def:mixed-kodaira-spencer-class}, the cohomology class of $m^{(1)}$ is precisely $\kappa_{\mathrm{mix}}$, so on the $E_1$-page the first differential is the adjoint action of $\kappa_{\mathrm{mix}}$.
   252	\end{proof}
   253	
   254	\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
   255	\label{cor:persistence-criterion-quadratic-law}
   256	The quadratic mixed-coupling law survives to first non-quadratic order if and only if
   257	\[
   258	\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0.
   259	\]
   260	More generally, if the mixed coderivation components $m^{(1)},\dots,m^{(r)}$ vanish in relative Hochschild cohomology, then the mixed-weight spectral sequence degenerates through $E_{r+1}$.
   261	\end{corollary}
   262	
 succeeded in 50ms:
   718	\]
   719	The zeroth differential on the associated graded is therefore $d_0=[m^{(0)},-]$, and the first derived differential is induced by the next term $[m^{(1)},-]$. By Definition~\ref{def:mixed-kodaira-spencer-class}, the cohomology class of $m^{(1)}$ is precisely $\kappa_{\mathrm{mix}}$, so on the $E_1$-page the first differential is the adjoint action of $\kappa_{\mathrm{mix}}$.
   720	\end{proof}
   721	
   722	\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
   723	\label{cor:persistence-criterion-quadratic-law}
   724	The quadratic mixed-coupling law survives to first non-quadratic order if and only if
   725	\[
   726	\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0.
   727	\]
   728	More generally, if the mixed coderivation components $m^{(1)},\dots,m^{(r)}$ vanish in relative Hochschild cohomology, then the mixed-weight spectral sequence degenerates through $E_{r+1}$.
   729	\end{corollary}
   730	
 succeeded in 52ms:
   761	\]
   762	The zeroth differential on the associated graded is therefore $d_0=[m^{(0)},-]$, and the first derived differential is induced by the next term $[m^{(1)},-]$. By Definition~\ref{def:mixed-kodaira-spencer-class}, the cohomology class of $m^{(1)}$ is precisely $\kappa_{\mathrm{mix}}$, so on the $E_1$-page the first differential is the adjoint action of $\kappa_{\mathrm{mix}}$.
   763	\end{proof}
   764	
   765	\begin{corollary}[Persistence criterion for the quadratic law; \ClaimStatusProvedHere]
   766	% label removed: cor:persistence-criterion-quadratic-law
   767	The quadratic mixed-coupling law survives to first non-quadratic order if and only if
   768	\[
   769	\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0.
   770	\]
   771	More generally, if the mixed coderivation components $m^{(1)},\dots,m^{(r)}$ vanish in relative Hochschild cohomology, then the mixed-weight spectral sequence degenerates through $E_{r+1}$.
   772	\end{corollary}
   773	
exec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '1107,1122p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/free_fields.tex | sed -n '5150,5318p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '1426,1440p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex | sed -n '2855,2893p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1107	\begin{theorem}[KS wall-crossing $=$ homotopy colimit $=$ MC gauge equivalence]
  1108	\label{thm:ks-mc-gauge}
  1109	\ClaimStatusProvedHere{}
  1110	For a CY$_3$ category $\cC$ with charge lattice $\Gamma$ and central charge $Z$, the following three formulations of Donaldson--Thomas theory are equivalent:
  1111	\begin{enumerate}[label=\textup{(\Roman*)}]
  1112	 \item \textbf{KS wall-crossing.} The DT partition function $Z_{\DT}(\cC, \sigma)$ is computed by the ordered product $\prod_{\arg Z(\gamma) \downarrow} E(X^\gamma)^{\Omega(\gamma)}$ of quantum dilogarithm factors in the quantum torus, with transitions across walls governed by the Kontsevich--Soibelman pentagon identity.
  1113	 \item \textbf{$\Eone$ homotopy colimit.} The global algebra $A_\cC = \operatorname{hocolim}_{\mathrm{Stab}} \CoHA$ is the homotopy colimit of the CoHA diagram over the stability manifold, with transition maps $K_\cW$ for each wall~$\cW$.
  1114	 \item \textbf{$\Eone$ MC equation.} There exists $\Theta^{\Eone}_\cC \in \mathrm{MC}(\mathrm{Def}^{\Eone}_{\mathrm{cyc}}(\cC))$ satisfying $D \cdot \Theta + \frac{1}{2}[\Theta, \Theta] = 0$, encoding all chambers simultaneously.
  1115	\end{enumerate}
  1116	The equivalences (I)$\leftrightarrow$(II) and (II)$\leftrightarrow$(III) hold as follows. (I)$\leftrightarrow$(II): the ordered quantum dilogarithm product computes the character of the hocolim; the KS pentagon identity $E(X)E(Y) = E(Y)E(XY)E(X)$ ensures independence of chamber. \emph{Critical distinction}: the pentagon holds in the quantum torus; the Lie algebra BCH captures only leading-order commutator terms and does NOT reproduce the full pentagon. (II)$\leftrightarrow$(III): the transition maps $K_\cW$ satisfy the cocycle condition if and only if the MC equation holds; the equation $[\Theta, \Theta] = 0$ holds automatically by antisymmetry, and its content is $D^2 = 0$ in the bar complex (a theorem from $\partial^2 = 0$ on $\overline{\mathcal{M}}_{g,n}$). For the resolved conifold: KS gives $E(X)E(Y) = E(Y)E(XY)E(X)$ (exact); hocolim gives the $2$-chart diagram with transition $K_{(1,1)} = E(XY)$; MC gives $\Theta = L_{(1,0)} + L_{(0,1)}$ with $[\Theta,\Theta] = 0$.
  1117	
  1118	\noindent\textit{Verification}: 117 tests in \texttt{test\_ks\_hocolim\_equivalence.py}, verifying all three equivalences by 10 independent paths including: quantum torus pentagon (exact), MC equation antisymmetry, Jacobi$\Rightarrow D^2 = 0$ chain, DT partition function numerics, MacMahon leading terms, A${}_3$ quiver hexagon, bar complex dimension comparison, transition map invertibility, fermionic pentagon, and charge-graded hocolim decomposition (\texttt{ks\_hocolim\_equivalence.py}).
  1119	\end{theorem}
  1120	
  1121	
  1122	\begin{proposition}[Flop $=$ $\Eone$ Koszul duality]
 succeeded in 52ms:
  2855	\begin{theorem}[Classification by shadow depth; \ClaimStatusProvedHere]
  2856	\label{thm:classification-shadow-depth}
  2857	\index{classification!by shadow depth|textbf}
  2858	\index{shadow depth!classification theorem|textbf}
  2859	Let\/ $\cA$ be a logarithmic\/ $\SCchtop$-algebra. The shadow
  2860	depth\/ $\dalg(\cA)$ classifies\/ $\cA$ into two proved types and
  2861	one open case:
  2862	\begin{enumerate}[label=\textup{(\roman*)}]
  2863	\item \textbf{Type~F} \textup{(}formal\textup{):}
  2864	 $\dalg(\cA) = 0$, equivalently $m_k = 0$ for all $k \ge 3$.
  2865	 The bar complex is the Chevalley--Eilenberg complex of the
  2866	 underlying Lie algebra. The $E_1$ dg coalgebra structure is
  2867	 formal. Examples: Heisenberg $H_\kappa$, abelian Chern--Simons.
  2868	\item \textbf{Type~V} \textup{(}Virasoro-type\textup{):}
  2869	 $\dalg(\cA) = 1$, equivalently $m_3 \neq 0$ but $m_k$ for
  2870	 $k \ge 4$ is determined by $m_2$ and $m_3$ via the Stasheff
  2871	 relations. The first non-formal operation arises from double
  2872	 poles in the OPE. Examples: Virasoro $\mathrm{Vir}_c$,
  2873	 $\mathcal{W}_3$.
  2874	\item \textbf{Type~H} \textup{(}higher, open\textup{):}
 succeeded in 52ms:
  1426	For a CY$_3$ category $\cC$ with multi-chart atlas $\cA = \{(Q_\alpha, W_\alpha)\}_{\alpha \in I}$, the canonical map
  1427	\[
  1428	 \operatorname{hocolim}_\alpha \, \cZ\bigl(\Rep^{\Eone}(\CoHA_\alpha)\bigr) \;\longrightarrow\; \cZ\bigl(\Rep^{\Eone}(\operatorname{hocolim}_\alpha \CoHA_\alpha)\bigr)
  1429	\]
  1430	is \emph{not} an equivalence in general. Its cofiber, the \emph{global braiding obstruction}
  1431	\[
  1432	 \mathrm{Obs}(\cC) \;:=\; \mathrm{cofib}\!\bigl(\operatorname{hocolim}_\alpha \cZ_\alpha \to \cZ_{\mathrm{global}}\bigr),
  1433	\]
  1434	is zero if and only if $\cC$ has a single stability chamber ($|I| = 1$). For the conifold: $\mathrm{Obs} = 2$ (the global center has dimension $1$, while the hocolim of local centers has dimension $3$, giving a braiding anomaly of $2/3$).
  1435	\end{proposition}
  1436	
  1437	\begin{proof}
  1438	For $|I| = 1$ (single chart, e.g.\ $\C^3$): the hocolim is the identity, and both sides agree. For $|I| \geq 2$: the hocolim $A = \operatorname{hocolim}_\alpha A_\alpha$ identifies elements across charts via the wall-crossing automorphisms $K_{\alpha\beta}$. The global center $\cZ(\Rep^{\Eone}(A))$ consists of elements that commute with \emph{all} of $A$, including the gluing data. But the hocolim of local centers $\operatorname{hocolim}_\alpha \cZ(A_\alpha)$ contains elements that commute locally (within each chart) but may fail to commute with the transition maps. The difference is precisely the braiding data that lives on the walls.
  1439	
  1440	For the conifold: $\cZ(\Rep^{\Eone}(\CoHA_{\mathrm{I}}))$ has dimension $2$ (the unit and the supertrace), $\cZ(\Rep^{\Eone}(\CoHA_{\mathrm{II}}))$ has dimension $3$, and their hocolim has dimension $3$ (Morita embedding). The global center $\cZ(\Rep^{\Eone}(A_{\text{conifold}}))$ has dimension $1$ (only the unit commutes with the wall-crossing $K_{(1,1)}$, since $K_{(1,1)}$ does not preserve the supertrace). The obstruction is $3 - 1 = 2$.
 succeeded in 52ms:
  5150	
  5151	This gives the one-loop correction with modular invariance.
  5152	\end{example}
  5153	
  5154	\begin{theorem}[Modular invariance and anomaly cancellation; \ClaimStatusProvedElsewhere]\label{thm:modular-anomaly}
  5155	The string amplitude is modular invariant if and only if the central charge satisfies the anomaly cancellation condition:
  5156	
  5157	For bosonic strings: $c = 26$
  5158	For superstrings: $c = 15$
  5159	
  5160	The modular anomaly is computed by:
  5161	\[\text{Anomaly} = \frac{c - c_{\text{crit}}}{24} \int_{\mathcal{M}_1} \omega_{\text{moduli}}\]
  5162	\end{theorem}
  5163	
  5164	\begin{proof}
  5165	The genus-$1$ bar complex transforms covariantly under $\mathrm{SL}_2(\mathbb{Z})$ with weight $c/24$ (Theorem~\ref{thm:modular-invariance}). Modular invariance of the full partition function requires the left-right central charge difference $c - \tilde{c} = 0 \bmod 24$ (for single-valuedness of the phase $e^{2\pi i (c-\tilde{c})/24}$). For the bosonic string ($c = \tilde{c} = 26$) and the superstring ($c = \tilde{c} = 15$), conformal anomaly cancellation arises from Weyl invariance on the worldsheet, not from $c \bmod 24$ alone. This is the Belavin--Knizhnik theorem \cite{BK86}; see also Polchinski \cite[Ch.~5]{Pol98} for the standard textbook treatment.
  5166	\end{proof}
  5167	
  5168	
  5169	\subsection{\texorpdfstring{Modular invariance under $SL_2(\mathbb{Z})$}{Modular invariance under SL-2(Z)}}

thinking
**Searching for Poincaré duality proof**

I'm considering checking into Poincaré duality and seeing if there's a way to prove the absence of lines related to it. There seems to be a lot of mathematical depth here, and I'm curious about the implications and theorems surrounding that topic. I want to ensure I gather accurate information, so I'll look into reliable sources that discuss both the duality concept and the absence of lines, and see how they interconnect!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex | sed -n '730,736p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex | sed -n '773,779p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/poincare_duality.tex | sed -n '575,590p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/ym_higher_body_couplings.tex | sed -n '262,268p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   730	
   731	\begin{proof}
   732	The first statement is immediate from Theorem~\ref{thm:first-correction-theorem}. The second follows from the same filtered-complex argument: if all differential pieces up to mixed weight $r$ are cohomologically trivial, then all differentials $d_1,\dots,d_r$ vanish.
   733	\end{proof}
   734	
   735	\begin{theorem}[Universal interaction brackets on mixed couplings; \ClaimStatusProvedHere]
   736	\label{thm:universal-interaction-brackets}
 succeeded in 51ms:
   262	
   263	\begin{proof}
   264	Immediate from Theorem~\ref{thm:first-correction-theorem}. For the second statement, if all differential pieces up to mixed weight $r$ are cohomologically trivial, then $d_1,\dots,d_r$ all vanish.
   265	\end{proof}
   266	
   267	\begin{theorem}[Universal interaction brackets on mixed couplings; \ClaimStatusProvedHere]
   268	\label{thm:universal-interaction-brackets}
 succeeded in 51ms:
   575	\begin{proposition}[Chiral Koszul pair via NAP; \ClaimStatusProvedHere]\label{prop:koszul-pair-NAP}
   576	\index{Koszul pair!via non-abelian Poincare duality}
   577	Two chiral algebras $(\mathcal{A}_1, \mathcal{A}_2)$ on $X$ form a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair}) if and only if there exist quasi-isomorphisms of chiral coalgebras:
   578	\begin{align}
   579	\bar{B}^{\text{ch}}(\mathcal{A}_1) &\xrightarrow{\sim} (\mathcal{A}_2)^!\\
   580	\bar{B}^{\text{ch}}(\mathcal{A}_2) &\xrightarrow{\sim} (\mathcal{A}_1)^!
   581	\end{align}
   582	
   583	where $\mathcal{A}_i^!$ is defined via Verdier duality as in Construction \ref{const:A-dual-intrinsic}.
   584	
   585	\emph{Equivalent characterization (NAP).}
   586	\[\int_X \mathcal{A}_1 \simeq \mathbb{D}\left(\int_{-X} \mathcal{A}_2\right)\]
   587	
   588	with $\int_X$ the factorization homology, $-X$ the orientation reversal, and $\mathbb{D}$ Verdier duality.
   589	\end{proposition}
   590	
 succeeded in 51ms:
   773	
   774	\begin{proof}
   775	The first statement is immediate from Theorem~\ref{thm:first-correction-theorem}. The second follows from the same filtered-complex argument: if all differential pieces up to mixed weight $r$ are cohomologically trivial, then all differentials $d_1,\dots,d_r$ vanish.
   776	\end{proof}
   777	
   778	\begin{theorem}[Universal interaction brackets on mixed couplings; \ClaimStatusProvedHere]
   779	% label removed: thm:universal-interaction-brackets
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_higher_body_couplings.tex | sed -n '262,266p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   262	
   263	\begin{proof}
   264	Immediate from Theorem~\ref{thm:first-correction-theorem}. For the second statement, if all differential pieces up to mixed weight $r$ are cohomologically trivial, then $d_1,\dots,d_r$ all vanish.
   265	\end{proof}
   266	

thinking
**Clarifying proof lines for theorems**

I need to gather proof lines for the modular classification theorem, which should be enough. I'm looking for the exact line for proof absence in relative Feynman transform and Poincaré duality; I can note that no proof follows. It might be useful to reference line 2855 and indicate that the next environment is conjecture or discussion, not proof. I'll consider a snippet around lines 2890-2898 to show that the next environment is conjecture. Let’s get those line numbers sorted!
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex | sed -n '2890,2900p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/poincare_duality.tex | sed -n '589,596p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex | sed -n '1118,1123p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2890	\textup{(}central term\textup{)}.
  2891	
  2892	The classification presupposes chiral Koszulness \textup{(}bar spectral
  2893	sequence collapse at~$E_2$\textup{)}. Beyond the Koszul boundary lies
  2894	class~$\mathbf{W}$ \textup{(}wild\textup{)}: algebras for which the bar
  2895	spectral sequence does not collapse at any finite page and the shadow depth
  2896	is undefined. The Kronecker quiver $K_m$ for $m \geq 3$ provides the
  2897	standard example
  2898	\textup{(}Volume~I, Remarks~\textup{\ref*{V1-rem:wild-quiver-class}}
  2899	and~\textup{\ref*{V1-rem:wild-quiver-boundary}}\textup{)}.
  2900	\end{theorem}
 succeeded in 52ms:
   589	\end{proposition}
   590	
   591	\begin{theorem}[Symmetric Koszul duality; \ClaimStatusProvedHere]\label{thm:symmetric-koszul}
   592	\textup{[Regime: quadratic on the Koszul locus
   593	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   594	
   595	If $(\mathcal{A}_1, \mathcal{A}_2)$ is a Koszul pair, then:
   596	\begin{align}
 succeeded in 52ms:
  1118	\noindent\textit{Verification}: 117 tests in \texttt{test\_ks\_hocolim\_equivalence.py}, verifying all three equivalences by 10 independent paths including: quantum torus pentagon (exact), MC equation antisymmetry, Jacobi$\Rightarrow D^2 = 0$ chain, DT partition function numerics, MacMahon leading terms, A${}_3$ quiver hexagon, bar complex dimension comparison, transition map invertibility, fermionic pentagon, and charge-graded hocolim decomposition (\texttt{ks\_hocolim\_equivalence.py}).
  1119	\end{theorem}
  1120	
  1121	
  1122	\begin{proposition}[Flop $=$ $\Eone$ Koszul duality]
  1123	\label{prop:flop-koszul-duality}

thinking
**Considering theorem structure**

I’m thinking it would be good to include a line after the relative theorem to indicate there’s no proof, followed by the next conjecture. I just noticed that between 2890-2900, I've only included the theorem ending. It makes sense to add the subsequent lines starting from 2901. Let's keep things clear as I work through this! I want to ensure everything flows properly and is well-organized.
exec
/bin/zsh -lc "nl -ba /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex | sed -n '2900,2910p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  2900	\end{theorem}
  2901	
  2902	\begin{conjecture}[Existence of Type~H algebras]
  2903	\label{conj:type-H-existence}
  2904	\ClaimStatusOpen.
  2905	There exist logarithmic $\SCchtop$-algebras with shadow depth $\dalg(\cA) \geq 2$: algebras whose $\Ainf$ operations $m_k$ for $k \geq 4$ are not determined by $m_2$ and $m_3$ alone. Candidates include non-affine-lineage algebras with OPE poles of order $\geq 3$ and non-central higher residues.
  2906	\end{conjecture}
  2907	
  2908	\begin{remark}[Evidence]
  2909	We prove each case and then establish the OPE characterisation.
  2910	

thinking
**Evaluating theorem proof**

I'm examining line 2909, which mentions proving cases and establishing the OPE characterization. I wonder if the proof is deferred to later subsections? It’s possible that later sections might offer those proofs without a clear `proof` environment. I should be cautious, as the theorem could still be supported in subsequent parts of the text. I need to search for phrases like "OPE characterization" throughout the file and look into the subsections to clarify.
codex
The deferred-proof cases need one more check. A missing immediate `proof` block is not enough by itself if the chapter carries the proof in subsequent subsections, so I’m verifying those two cases explicitly before I keep them as findings.
exec
/bin/zsh -lc "rg -n --fixed-strings 'all OPE poles are simple' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'maximal pole order is "'$2$'"' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'Type~F' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n --fixed-strings 'OPE characterisation' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
2887:$\dalg(\cA) = 0$ if and only if all OPE poles are simple\textup{;}
 succeeded in 52ms:
2909:We prove each case and then establish the OPE characterisation.
2955:\emph{OPE characterisation:}
3201:(a c-number). By the OPE characterisation of
 succeeded in 53ms:
2863:\item \textbf{Type~F} \textup{(}formal\textup{):}
2912:\emph{Type~F ($\dalg = 0$):}
2978:$m_2$ (Type~F) or by $m_2$ and $m_3$ (Type~V). The case
2994:\begin{remark}[The affine lineage is uniformly Type~F]
3014:vertex algebras are Type~F (formal). The non-trivial genus
3068: Shadow depth $\dalg = 0$ \textup{(}Type~F\textup{)}.
3149: is Type~F \textup{(}formal\textup{)}.
3274:a one-parameter family of Type~F algebras with explicitly
 succeeded in 53ms:
2888:$\dalg(\cA) = 1$ if and only if the maximal pole order is $2$
2960:is non-zero: $\dalg = 0$. If the maximal pole order is $2$ with
exec
/bin/zsh -lc "sed -n '2910,2970p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:

\smallskip\noindent
\emph{Type~F ($\dalg = 0$):}
If $m_k = 0$ for all $k \ge 3$, then $\cA$ is a strict dg Lie
algebra (the $\Ainf$ structure is strictly quadratic). The bar
complex $\barB(\cA)$ is the classical Chevalley--Eilenberg
complex $C^\bullet(\fg_\cA)$, and the $E_1$ dg coalgebra
structure is formal in the sense that the $\Ainf$ homotopy
transfer data (Kadeishvili) produces no higher corrections.
This is the definition of formality for $\Ainf$ algebras.

\smallskip\noindent
\emph{Type~V ($\dalg = 1$):}
Suppose the maximal pole order in the OPE is $2$ and the
second-order residue is central (a scalar multiple of the
identity). The degree-$3$ operation $m_3$ is the integral of
this second-order residue against the FM$_3$ propagator: by
the bar differential formula
(Theorem~\ref{thm:recognition-relative-ft}), the degree-$k$
operation $m_k$ extracts the coefficient of the $(k-1)$-st










thinking
**Evaluating the theorem's implications**

I'm noticing that the theorem's statement at lines 2887-2888 uses "iff," but the evidence only proves the forward implications. So, a good fix would be to change "iff" to "if," or to mark the converse as open. That's a high-severity issue since the claim status is only partially proven. I should also check the `poincare_duality` proposition for any similar situations, as it might follow directly from the definition.
thinking
**Clarifying quasi-isomorphism definitions**

I’m realizing that saying "iff there exist quasi-isomorphisms of chiral coalgebras" might be more like a definition. The current definition involves a pair of chiral Koszul data with Verdier-compatible factorization-algebra identifications, but it doesn't mention bar coalgebras, which uses a different theorem and isn't straightforward. I think an exact fix would be to revise this to "If ... form a chiral Koszul pair, then there exist ...". I should also look for other candidates that might lack an immediate proof.
thinking
**Investigating proof sufficiencies**

I could search for lines after the theorem where it says, "We prove each case," to check if converses are unproven. It seems we already have one case. I wonder if there are other examples, like the "Complete modular invariance classification," which might only prove sufficiency. The `ks-mc-gauge` theorem appears to involve verification tests without a full proof, which is quite strong. I should check whether there's a later remark about proof sketches, but it looks like there isn't one for the next proposition.
thinking
**Considering theorem adjustments**

The user is asking about the forward direction being proved and suggests providing a fix if not. I’m contemplating the idea of downgrading the theorem to a remark or conjecture until a proof is established. This feels like a grounded approach since the local file doesn’t prove the converse or any direction effectively. It’s a tricky situation, but I think this adjustment makes sense!
thinking
**Evaluating theorem adjustments**

I’m thinking through how every finding doesn’t always imply exact fixes. I might need to adjust the relative Feynman transform theorem to clarify its implications. For instance, I could replace "if and only if" with just "if" in specific lines to better align with the proof. I also consider changing the title for clarity. There’s a similar idea for the Poincaré duality proposition where I could make it more direct. Overall, these adjustments seem minimal, and I’m curious if there’s more I can find to strengthen my argument.
thinking
**Assessing theorem classification**

I’m exploring whether the `center-hocolim` is significant enough, along with the classification of `free_fields` and modular anomalies. I note that I’ve checked 151 theorem-like blocks across three volumes, leading to 10 findings, resulting in a verdict of FAIL. I want to ensure accuracy in my reporting. I’m thinking about establishing a severity order for the findings, classifying some theorems as critical or high priority while considering duplicates. I'll need to standardize the severity for each duplicate, too.
thinking
**Determining Exact Fixes**

The user needs an exact fix for the statement. I think the minimal adjustment is to replace "if and only if ...=0" with "whenever ...=0." However, this change does create a more sufficient condition rather than an equivalence. So, the exact fix is to use "whenever." I need to ensure my final output follows the structured format while summarizing findings. I may mention "Checked: 151 | Findings: 10 | Verdict: FAIL," keeping the findings as a bullet list without nesting.
thinking
**Clarifying File Paths**

I need to determine whether file paths should be absolute or repo-relative since the user is asking for exact file and line information. Using relative paths for the current repo and absolute paths for other volumes could work well. The final output should avoid markdown links unless necessary, adhering to the plain format of `file:line`.

I might also want to include relevant findings, perhaps around 10, and consider line items like `free_fields` theorem as critical. However, I need to be cautious about including items without proper proof to avoid false positives.
thinking
**Considering theorem structure and paths**

For the modular-anomaly theorem, I’m thinking that it could work as a proposition with separate conditions. I might want to change the title to "Critical-dimension anomaly cancellation in string BRST models." I need to be cautious about using absolute paths since the user preferred a plain `file:line` format, avoiding markdown links. So, I might use absolute paths for external volumes and relative for the current repository to maintain clarity. However, using absolute paths for everything may provide more precision.
thinking
**Resolving file reference formats**

The final instructions prefer clickable file links for local files, but the structured output contract specifies using `file:line`. To preserve the exact format, I might avoid markdown links and just stick with plain text paths. Also, I need to provide summary counts: Checked 151, Findings 10, Verdict FAIL. I’m considering using theorem-like environments for clarity, potentially using `\iff` or "if and only if." Before finalizing, I might update the plan to ensure everything is completed correctly.
Plan update
All 151 theorem-like `iff` candidates were enumerated and re-checked against their local proof surfaces. Remaining findings are the cases where the converse is not established on the page, or the local proof explicitly supports only a weaker one-way statement.
  ✓ Enumerate every theorem-like environment in the three chapter trees containing `\iff` or `if and only if`
  ✓ Read each candidate statement and its local proof or cited justification to test whether the converse is actually proved
  ✓ Re-verify findings, remove false positives, and produce exact file:line fixes




thinking
**Crafting Concise Findings**

I need to ensure my final output is concise but detailed enough. I’m thinking maybe I could include 10 bullet points without any nested bullets. It would be good to start with findings sorted by severity and to include specific citations in the format of file:line, noting multiple line numbers for any recurring issues. I should separate each duplicate bullet and mention the summary as specified. Time to craft the bullets carefully!
thinking
**Identifying Necessary Fixes**

I need to downgrade the environment to `remark` until a real proof is added. For line 1110, I'll change “the following three formulations ... are equivalent” to “the following three formulations are related.” Also, I’ll revise line 1116 to clarify the quantum dilogarithm product. Additionally, I should mention line 1110, but citing file:line at 1116 might be enough. 

I also need to address a critical problem at line 5155 regarding modular invariance and its contradictions in the proof. I’ll replace the theorem statement to reflect the necessary conditions for anomaly cancellation.
thinking
**Clarifying Theorem Statement**

I need to clarify that genus-1 modular covariance of the partition function requires \(c-\tilde c \equiv 0 \pmod{24}\). I should also remove the “if and only if” phrase to simplify the statement. This change should make it clearer and more precise. Keeping things straightforward will help avoid confusion in the overall discussion. Let's aim for a concise representation that effectively communicates the essential requirements of the modular covariance.
thinking
**Crafting clear styles**

I'm thinking about how the style could use bullet points, but I want to keep it concise. Maybe each bullet could be two lines long and utilize semicolons for clarity. I should aim for minimalism while ensuring everything is still clear and easy to follow. Using code in backticks might be useful, but I don't want to overdo it. Overall, I’m focused on creating something simple yet effective. Let's produce something great!
codex
- [CRITICAL] /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1116 — PROBLEM: `thm:ks-mc-gauge` is tagged `\ClaimStatusProvedHere`, claims `(I)\leftrightarrow(II)` and `(II)\leftrightarrow(III)`, but there is no proof block; line 1116 is only a sketch, and line 1118 appeals to tests, not a proof. No converse is actually proved in-file. FIX: Downgrade the environment to `remark` unless a real proof is added; replace line 1110 with `the following three formulations of Donaldson--Thomas theory are related:` and replace line 1116 with `The ordered quantum dilogarithm product computes the character of the hocolim. When an MC element \Theta^{\Eone}_\cC exists, it packages the wall-crossing data encoded by the transition maps \(K_\cW\).`

- [CRITICAL] chapters/examples/free_fields.tex:5155 — PROBLEM: the theorem states modular invariance `if and only if` critical central charge, but the proof at 5165 explicitly says modular invariance only forces `c-\tilde c \equiv 0 \pmod{24}` and that `c=26,15` comes from Weyl-anomaly cancellation, a separate condition. The proof undercuts the stated equivalence. FIX: Replace the statement with `In the bosonic and superstring BRST constructions, anomaly cancellation requires \(c=26\) and \(c=15\) respectively. Separately, genus-1 modular covariance of the partition function requires \(c-\tilde c \equiv 0 \pmod{24}\).` and remove the `if and only if`.

- [HIGH] chapters/connections/ym_higher_body_couplings.tex:256 — PROBLEM: the preceding theorem only proves survival to the next page `iff` the class lies in `\ker[\kappa_{\mathrm{mix}},-]` (lines 238-251); the corollary sharpens this to `\kappa_{\mathrm{mix}}=0`, and the proof at 264 says `Immediate from Theorem...`. The converse is not proved. FIX: Replace lines 256-259 with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).` If an equivalence is intended, replace the RHS by `[\kappa_{\mathrm{mix}},-]=0` on `\widetilde Z_\infty(M_1)\widehat\otimes \widetilde Z_\infty(M_2)` and prove that criterion separately.

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_higher_body_couplings.tex:256 — PROBLEM: same propagated AP36 failure as the Vol I copy; the theorem above identifies survival with `\ker[\kappa_{\mathrm{mix}},-]`, but the corollary upgrades this to `\kappa_{\mathrm{mix}}=0` without proof. FIX: Replace the `iff` sentence with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).`

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis.tex:767 — PROBLEM: same propagated AP36 failure; the proof at 775 still cites the previous theorem as if it implied `\kappa_{\mathrm{mix}}=0 \iff` survival, but it only gives the kernel criterion. FIX: Replace the `iff` sentence with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).`

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex:724 — PROBLEM: same propagated AP36 failure; the proof at 732 again says the first statement is immediate from the theorem, but the theorem does not prove the converse `survival => \kappa_{\mathrm{mix}}=0`. FIX: Replace the `iff` sentence with `The quadratic mixed-coupling law survives to first non-quadratic order whenever \(\kappa_{\mathrm{mix}}(M_{12};M_1,M_2)=0\).`

- [HIGH] /Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:1434 — PROBLEM: `prop:center-hocolim` proves `|I|=1 \Rightarrow \mathrm{Obs}=0` and then gives only the conifold as a multi-chart example. It does not prove the converse `\mathrm{Obs}=0 \Rightarrow |I|=1` for general atlases. FIX: Replace line 1434 with `is zero when \(\cC\) has a single stability chamber (\(|I|=1\)). For the conifold, \(\mathrm{Obs}=2\). More generally, multi-chart atlases can carry a nontrivial braiding obstruction.`

- [HIGH] chapters/examples/free_fields.tex:5296 — PROBLEM: `thm:modular-classification` claims a complete `iff` classification, but the proof only supplies sufficient mechanisms; the only actual equivalence proved is the integer-weight triviality at 5311. No converse from modular invariance to the four listed cases is proved. FIX: Rename the theorem to `Sufficient conditions for genus-1 modular invariance` and replace line 5296 with `A chiral algebra \(\mathcal{A}\) is modular invariant at genus 1 in each of the following situations:`.

- [HIGH] /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/relative_feynman_transform.tex:2887 — PROBLEM: `thm:classification-shadow-depth` is tagged `\ClaimStatusProvedHere`, but the later `Evidence` remark only proves the forward implications `simple poles \Rightarrow \dalg=0` and `double poles with central residue \Rightarrow \dalg=1`. The `iff` directions at 2887-2888 are not established. FIX: Replace lines 2887-2889 with `\(\dalg(\cA)=0\) if all OPE poles are simple; \(\dalg(\cA)=1\) if the maximal pole order is \(2\) and the corresponding residue is a scalar multiple of the identity (central term).` If the converses are intended, mark them conjectural.

- [MEDIUM] chapters/theory/poincare_duality.tex:577 — PROBLEM: `prop:koszul-pair-NAP` states an `iff` and then an `Equivalent characterization (NAP)` with no proof block; the cited definition provides the antecedent data for the forward direction, but the converse reconstruction from the displayed quasi-isomorphisms is not shown here. FIX: Replace line 577 with `If two chiral algebras $(\mathcal{A}_1,\mathcal{A}_2)$ on $X$ form a chiral Koszul pair, then there exist quasi-isomorphisms of chiral coalgebras:` and replace `Equivalent characterization (NAP)` with `Consequent NAP expression.`

## Summary
Checked: 151 | Findings: 10 | Verdict: FAIL
tokens used
192,533
