# H18_remove_class_M_MC5 (509s)

Added a new research remark in [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2169) and synchronized the nearby class `M` status language. The chapter now says one consistent thing: naive strict chain-level MC5 is false for class `M`, the coderived theorem is the proved statement, and the open frontier is a filtered-completed refinement.

The new remark does four jobs: it explains the failure by the quartic non-coboundary plus the infinite shadow tower, formulates a spectral replacement using `prop:coderived-bar-degree-spectral-sequence`, formulates a completed replacement using `prop:standard-strong-filtration` and `thm:completed-bar-cobar-strong`, and isolates the strongest intermediate statement presently visible between raw chain level and bare coderived equivalence.

Local verification passed: label uniqueness, reference-surface grep, and banned-prose sweep. A full `latexmk` run was blocked by a pre-existing unrelated error in [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:677): undefined control sequence `\ord`.

## Fortification Report
- `thm:bv-bar-coderived`: PRIMARY PROOF `sound`; SECONDARY PROOF `written`; TECHNIQUE `primary proof by harmonic-discrepancy plus coacyclic-cone argument, secondary proof by operadic Swiss-cheese Koszul duality in rem:bv-bar-coderived-operadic; new research remark adds spectral and completed frontier lanes`; CONDITION STATUS `unconditional in D^{co}; naive strict chain-level statement false for class M; filtered-completed refinement remains open`; CONFIDENCE `medium`


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
session id: 019d86ac-97b7-7183-be24-b0f32ad2329e
--------
user
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.
Your mission is threefold:

1. HEAL: find remaining wounds (gaps, weaknesses, fragilities) and repair them
2. FORTIFY: for every main result, construct an ALTERNATIVE proof path that provides
   REDUNDANCY — if one proof fails, the other stands independently
3. UPGRADE: where a result is conditional, investigate whether the condition can be
   REMOVED by new mathematical insight, alternative technique, or reformulation

You have WRITE access. Make edits. Write new proofs. Add remarks.
The standard is: every theorem that can have two independent proofs MUST have two.
</task>

<action_safety>
Keep edits within assigned scope. After every substantial edit, re-read and verify.
New proofs must be mathematically rigorous — no hand-waving, no "by analogy."
If you cannot complete a proof: write a detailed proof SKETCH with the key steps
identified and the remaining gap precisely named.
</action_safety>

<completeness_contract>
For each theorem in your scope:
1. Verify the PRIMARY proof is now sound (after rectification)
2. Write or sketch a SECONDARY proof via a different technique
3. If conditional: investigate removing the condition
4. State confidence level for each proof path
</completeness_contract>

<structured_output_contract>
End with:
## Fortification Report
For each theorem:
  - PRIMARY PROOF: [sound/repaired/gap-remaining]
  - SECONDARY PROOF: [written/sketched/identified/blocked]
  - TECHNIQUE: [what alternative method]
  - CONDITION STATUS: [unconditional/conditional-on-X/research-programme-Y]
  - CONFIDENCE: [high/medium/low]
</structured_output_contract>


RESEARCH: Chain-level BV/bar for class M.

TARGET: chapters/connections/bv_brst.tex (add Research Remark)

MC5 chain-level is FALSE for class M (Virasoro). The coderived result holds.

INVESTIGATE:
1. WHY does chain-level fail for class M? The infinite shadow tower means infinitely
   many non-zero A-inf operations; the BV complex cannot capture them all at chain level.
2. Is there a SPECTRAL version of MC5 that works for class M? (A spectral sequence
   from the shadow tower filtration converging to the BV complex.)
3. What is the BEST chain-level statement? Perhaps: BV ≅ bar in a COMPLETED category
   (pro-completion by shadow tower degree)?
4. Can the coderived result be STRENGTHENED to something between coderived and chain-level?

Write a Research Remark with the spectral and completed approaches.
mcp startup: no servers

thinking
**Planning code exploration**

I need to possibly spawn an explorer agent to search the codebase. Maybe a worker too, but that likely isn't necessary. I can use exec_command to read files instead. Since I have to read CLAUDE and other files, it seems I should avoid using cat. For reading files, I'm thinking of using sed or nl, which sounds fine. I'll also need to apply patches for any edits, so checking the repo status is essential. I'll start with commentary first.
codex
Scope is `chapters/connections/bv_brst.tex`, with a research remark on class `M` chain-level BV/bar. I’m reading the constitutional files, the live theorem/status surface, and the exact chapter context before deciding the smallest truthful insertion and any propagation needed.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pwd && rg -n "MC5|class M|BV|coderived|shadow tower|Virasoro|Research Remark|research remark" chapters/connections/bv_brst.tex CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 exited 2 in 52ms:
Total output lines: 564

/Users/raeez/chiral-bar-cobar
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
CLAUDE.md:11:**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
CLAUDE.md:15:**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
CLAUDE.md:93:- W_N: `kappa(W_N) = c*(H_N - 1)` where `H_N = 1 + 1/2 + ... + 1/N`. NOT `H_{N-1}`. Verify at N=2: H_2=3/2, H_2-1=1/2, so kappa(W_2)=c/2 matches Virasoro.
CLAUDE.md:202:4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower).
CLAUDE.md:204:NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" — they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.
CLAUDE.md:223:**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).
CLAUDE.md:235:**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).
CLAUDE.md:241:**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).
CLAUDE.md:279:**C30. Delta discriminant.** `Delta = 8*kappa*S_4`. Finite tower iff Delta=0; for kappa!=0 iff S_4=0. LINEAR in kappa (NOT quadratic, AP21). Heis: S_4=0, Delta=0, class G. Vir: S_4!=0, Delta!=0, class M.
CLAUDE.md:299:- B8. `\kappa = c/2` unqualified. CORRECT: specify family; `c/2` is Virasoro ONLY. AP1/AP39.
CLAUDE.md:358:- B43. `d_alg(Vir) = 3`. CORRECT: `d_gen(Vir) = 3`, `d_alg(Vir) = inf` (class M). AP131/FM18.
CLAUDE.md:387:- B62. `S_2 = c/12` for Virasoro. CORRECT: `S_2 = \kappa = c/2`. The c/12 is the lambda-bracket divided-power coefficient (c/2)/3!, NOT the shadow invariant. AP177.
CLAUDE.md:393:- B68. "S_2 = c/12, which is the Virasoro central charge itself." DOUBLE ERROR: S_2 = c/2 (not c/12), and the central charge is c (not c/12). AP177.
CLAUDE.md:438:**FM18. Generating-depth vs algebraic-depth conflation.** `d_gen(Vir) = 3` (m_3 generates recursively) but `d_alg(Vir) = inf` (class M). Counter: every depth statement carries the subscript `gen` or `alg`. Refuse bare `d(...)`.
CLAUDE.md:474:**FM30. Lambda-bracket divided-power coefficient conflation.** Opus wrote the lambda-bracket coefficient c/12 where the shadow invariant S_2 = c/2 was required. The lambda-bracket {T_λ T} = (c/12)λ^3 uses divided powers (T_{(3)}T/3! = (c/2)/6 = c/12). Opus confused the PRESENTATION-DEPENDENT coefficient c/12 with the PRESENTATION-INDEPENDENT invariant S_2 = κ = c/2. The error was compounded by writing "which is the Virasoro central charge itself" (c/12 is NOT c). Counter: shadow invariants S_r are NUMBERS (family invariants), not convention-dependent coefficients. S_2 = κ ALWAYS. After writing any S_r value, verify against Vol I census: S_2(Vir) = c/2.
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 52ms:
\chapter{BV-BRST formalism and Gaiotto's perspective}
\label{ch:bv-brst}
\index{Batalin--Vilkovisky|see{BV algebra}}

The physicist's BRST cohomology and the algebraist's bar resolution
are not analogous: they are the same computation. The BV formalism
is a machine for computing derived functors; the bar complex is a
machine for computing derived functors; at genus~$0$, they are the
same machine applied to the same input. Costello's formulation of
perturbative QFT as the theory of derived moduli problems makes the
identification inevitable: the BRST operator computes the derived
space of gauge-equivalence classes, which is what the bar differential
computes on the algebraic side. What requires proof is not the
coincidence but the precise scope of the agreement.

The BV Laplacian and the sewing operator agree at genus~$0$. The
quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
the BV formalism coincides on $\mathbb{P}^1$ with the bar
differential $d_{\mathrm{bar}}$ of the chiral algebra: the
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
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
codex
I’ve confirmed the scope boundary: `MC5` is already recorded as coderived-proved and chain-level false for class `M`, both in `CLAUDE.md` and the concordance. Next I’m reading the class-by-class BV/bar obstruction section and the relevant theory files on coderived and completed filtrations so the new remark can say the strongest truthful thing and cite the right local infrastructure.
exec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/frontier-research/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1600,2095p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
---
name: beilinson-rectify
description: Use when the user asks to rectify, fortify, rewrite, tighten, or structurally repair a mathematical chapter, proof, or claim surface in this repository. Not for isolated formula checks better handled by multi-path-verify.
---

# Beilinson Rectify

This is the heavy rectification workflow. Use it when the task is not just to patch a claim, but to make a chapter or proof lane truer, tighter, and harder to break.

It is also the Codex-side home of the lighter `/rectify` and `/beilinson-rectify` workflows from `CLAUDE.md`.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the full target file
- the directly cited dependencies

 succeeded in 52ms:
---
name: frontier-research
description: Use for new theorem architecture, research synthesis, or frontier programme design. Keep work local by default. Delegate or swarm only when the user explicitly authorizes it. This is the Codex-native equivalent of the frontier and research-swarm workflows from `CLAUDE.md`.
---

# Frontier Research

Frontier work is allowed only after the proved core, the conditional bridge, and the conjectural extension are separated sharply.

## Workflow

1. Partition the topic into:
   proved core,
   compute-backed evidence,
   conditional bridge,
   conjectural extension,
   heuristic picture.
2. Read the live theorem surface before synthesizing new structure.
3. Name the exact blocker for every missing implication.
4. Prefer the strongest narrower programme statement that survives hostile rereading.
 succeeded in 51ms:
  1600	
  1601	\medskip
  1602	\noindent\textbf{Path \textup{(d)}: numerical verification.}
  1603	\index{multi-path verification!Heisenberg BV/bar}
  1604	At each genus $g = 1, \ldots, 15$, three independent
  1605	implementations produce the same rational number $\lambda_g^{\mathrm{FP}}$:
  1606	\begin{enumerate}[label=\textup{(\roman*)},nosep]
  1607	\item the Bernoulli formula
  1608	 $\lambda_g^{\mathrm{FP}}
  1609	 = \frac{(2^{2g-1}-1)\,|B_{2g}|}{2^{2g-1}\,(2g)!}$;
  1610	\item the Taylor extraction of the $\hat{A}$-series
  1611	 $(\hbar/2)/\sin(\hbar/2) - 1
  1612	 = \sum_{g \geq 1} \lambda_g^{\mathrm{FP}}\,\hbar^{2g}$;
  1613	\item a direct computation of the Faber--Pandharipande
  1614	 intersection integral on $\overline{\mathcal{M}}_{g,1}$
  1615	 via the string/dilaton equation and Witten's conjecture.
  1616	\end{enumerate}
  1617	All three agree at every genus tested. Sample values:
  1618	$\lambda_1^{\mathrm{FP}} = 1/24$,
  1619	$\lambda_2^{\mathrm{FP}} = 7/5760$,
exec
/bin/zsh -lc 'rg -n "shadow tower|completed|completion|spectral sequence|coderived|coacyclic|harmonic|class M|Virasoro|MC5|chain-level false|chain-level open|completed category|pro-completion|filtered|filtration" chapters/theory chapters/connections | head -n 400' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/typeA_baxter_rees_theta.tex:6:% completion formalism used in the MC4 proof and sharpens the DK
chapters/connections/typeA_baxter_rees_theta.tex:8:% Appendices~\ref{app:nilpotent-completion} and~\ref{app:coderived}.
chapters/connections/typeA_baxter_rees_theta.tex:19:type-$A$ derived Drinfeld--Kohno problem. The weight filtration on the
chapters/connections/typeA_baxter_rees_theta.tex:23:strict regime it forces all higher-point corrections. At the completion
chapters/connections/typeA_baxter_rees_theta.tex:44:completion formalism developed in this appendix is part of the proof.
chapters/connections/typeA_baxter_rees_theta.tex:52:Drinfeld--Kohno square, the infinite-generator completion boundary, and
chapters/connections/typeA_baxter_rees_theta.tex:54:completion appendices already explain that any genuine extension beyond
chapters/connections/typeA_baxter_rees_theta.tex:55:the compact finite-type regime must pass through completed and, in the
chapters/connections/typeA_baxter_rees_theta.tex:56:curved case, coderived categories; see
chapters/connections/typeA_baxter_rees_theta.tex:57:Appendices~\ref{app:nilpotent-completion} and~\ref{app:coderived}.
chapters/connections/typeA_baxter_rees_theta.tex:63:presentation introduces a natural filtration on the convolution dg~Lie
chapters/connections/typeA_baxter_rees_theta.tex:65:observation is that this filtration makes completion automatic: the
chapters/connections/typeA_baxter_rees_theta.tex:66:inverse system stabilizes weightwise, so the completed bar complex is
chapters/connections/typeA_baxter_rees_theta.tex:71:\text{weightwise completion} \quad \longrightarrow \quad
chapters/connections/typeA_baxter_rees_theta.tex:75:the binary MC element $r(z)$ on the polynomial core, the completion is
chapters/connections/typeA_baxter_rees_theta.tex:77:neighborhood of the MC element in the completed moduli space.
chapters/connections/typeA_baxter_rees_theta.tex:91: associators for completed triple tensor products
chapters/connections/typeA_baxter_rees_theta.tex:95: extension to the completed/coderived Baxter envelope becomes formal.
chapters/connections/typeA_baxter_rees_theta.tex:389:The next scale is the completion boundary. For
chapters/connections/typeA_baxter_rees_theta.tex:391:forced by the mode filtration of the RTT presentation.
codex
The local obstruction lane is clear now: there is already one proof path for coderived BV=`bar` and an operadic alternative, but there is no explicit research remark spelling out the class `M` frontier. I’m pulling the exact statements on completion and coderived spectral sequences so the new remark can connect the existing proofs to a plausible spectral/completed strengthening without overstating it.
collab spawn_agent(call_9uW5xqOFtgzhvzwU9sAkHBuJ, prompt="Inspect the repository for theorem/definition statements most relevant to a research remark in chapters/connections/bv_b…")
spawn_agent(call_9uW5xqOFtgzhvzwU9sAkHBuJ, prompt="Inspect the repository for theorem/definition statements most relevant to a research remark in chapters/connections/bv_b…") pending init:
  agent: 019d86ad-48e2-7f53-a913-2d9f01425160
mcp startup: no servers
exec
/bin/zsh -lc "nl -ba chapters/connections/editorial_constitution.tex | sed -n '430,540p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '900,2065p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '1,420p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   430	Yangian reduction chain is detailed in \S\ref{sec:infty-cat-factorization-kd}.
   431	\end{remark}
   432	
   433	\begin{conjecture}[BV/BRST/bar identification]
   434	\label{conj:v1-master-bv-brst}
   435	\ClaimStatusConjectured{}
   436	For a holomorphic field theory on a Riemann surface, the BV/BRST
   437	complex coincides with the bar complex of the associated chiral algebra,
   438	at all genera.
   439	
   440	\emph{Resolved in $D^{\mathrm{co}}$}
   441	\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
   442	the BV and bar complexes are quasi-isomorphic in the coderived category
   443	for all chirally Koszul algebras, including class~M.
   444	The chain-level identification holds for classes~G, L, C but
   445	\emph{fails} for class~M
   446	\textup{(}quartic harmonic obstruction\textup{)}.
   447	
   448	\emph{This is the mathematical-physics bridge. It is
   449	downstream of Theorem~\textup{\ref{thm:master-pbw}},
 succeeded in 51ms:
   900	\[
   901	\cA = F^0\cA \supset F^1\cA \supset F^2\cA \supset \cdots,
   902	\qquad
   903	\textstyle\bigcap_{N \ge 0} F^{N+1}\cA = 0,
   904	\]
   905	such that:
   906	\begin{enumerate}
   907	\item $\cA$ is separated and complete:
   908	 $\cA \cong \varprojlim_N \cA_{\le N}$, where
   909	 $\cA_{\le N} := \cA/F^{N+1}\cA$;
   910	\item every quotient $\cA_{\le N}$ is finite type and lies in the proved
   911	 bar-cobar regime;
   912	\item $\bar\cA = F^1\cA$ (the augmentation ideal is the first filtration
   913	 piece); and
   914	\item all chiral $\Ainf$-operations are filtration-nondecreasing:
   915	 \begin{equation}\label{eq:strong-filtration-condition}
   916	 \mu_r(F^{i_1}\cA, \dots, F^{i_r}\cA)
   917	 \subset F^{i_1+\cdots+i_r}\cA.
   918	 \end{equation}
   919	\end{enumerate}
 succeeded in 51ms:
     1	
     2	\section{Coderived and contraderived categories}
     3	\label{app:coderived}
     4	\index{coderived category|textbf}
     5	\index{contraderived category|textbf}
     6	
     7	The bar-cobar adjunction at higher genus produces curved complexes
     8	($d^2 \neq 0$), for which ordinary cohomological derived methods
     9	are no longer the right invariant.
    10	Positselski's theory of coderived and contraderived
    11	categories~\cite{Positselski11} provides the correct
    12	replacement. This appendix collects the definitions and key results
    13	needed in this monograph; the chiral specialization appears in
    14	\S\ref{subsec:chiral-coderived-contraderived}.
    15	
    16	\subsection{Abstract definitions}
    17	\label{subsec:coderived-abstract}
    18	
    19	Let $\mathsf{A}$ be an abelian category with exact direct sums
    20	(for the coderived case) or exact direct products
exec
/bin/zsh -lc pwd in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
AGENTS.md
CLAUDE.md
COMMIT_MESSAGE.txt
Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
FRONTIER.md
Makefile
N1_koszul_meta.pdf
N2_mc3_all_types.pdf
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
bibliography
bp_self_duality.pdf
exec
/bin/zsh -lc "rg -n \"bv_brst\" -n chapters/connections -g'*'" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "sed -n '1,200p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{BV-BRST formalism and Gaiotto's perspective}
\label{ch:bv-brst}
\index{Batalin--Vilkovisky|see{BV algebra}}

The physicist's BRST cohomology and the algebraist's bar resolution
are not analogous: they are the same computation. The BV formalism
is a machine for computing derived functors; the bar complex is a
machine for computing derived functors; at genus~$0$, they are the
same machine applied to the same input. Costello's formulation of
perturbative QFT as the theory of derived moduli problems makes the
identification inevitable: the BRST operator computes the derived
space of gauge-equivalence classes, which is what the bar differential
computes on the algebraic side. What requires proof is not the
coincidence but the precise scope of the agreement.

The BV Laplacian and the sewing operator agree at genus~$0$. The
quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
the BV formalism coincides on $\mathbb{P}^1$ with the bar
differential $d_{\mathrm{bar}}$ of the chiral algebra: the
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
exec
/bin/zsh -lc 'rg -n "coderived" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 6547

healing_20260413_132214/H04_thm_D_alt_proof.md:36:  coderived proven independently (Thm B), curved C0 in D^co unconditional (Thm C0), genus-0
healing_20260413_132214/H04_thm_D_alt_proof.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H10_depth_gap_alt.md:36:  coderived proven independently (Thm B), curved C0 in D^co unconditional (Thm C0), genus-0
healing_20260413_132214/H10_depth_gap_alt.md:39:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H10_depth_gap_alt.md:371:coderived_models.tex
healing_20260413_132214/H07_MC5_alt_approach.md:3:Updated [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2029). The operadic remark now states the alternative MC5 route in the corrected two-colour form: `\Delta_{\mathrm{BV}}` is the closed-colour Swiss-cheese contraction, `d_{\bar B}` is the open-colour coderivation, the relevant `SC^{\mathrm{ch,top}}` object is the pair `\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA),\cA\bigr)` rather than `B(A)` itself, the coderived comparison is presented as the coloured Koszul bar-cobar correspondence, and the class `\mathsf{M}` chain-level gap is isolated as non-formality of the explicit transferred model rather than a failure of coderived duality.
healing_20260413_132214/H07_MC5_alt_approach.md:8:For `thm:bv-bar-coderived`:
healing_20260413_132214/H07_MC5_alt_approach.md:15:For `thm:bv-bar-coderived` upgrade status:
healing_20260413_132214/H07_MC5_alt_approach.md:43:  coderived proven independently (Thm B), curved C0 in D^co unconditional (Thm C0), genus-0
healing_20260413_132214/H07_MC5_alt_approach.md:46:- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
healing_20260413_132214/H07_MC5_alt_approach.md:111:   which identifies SC-algebras with SC^!-coalgebras in the coderived category.
healing_20260413_132214/H07_MC5_alt_approach.md:116:coderived BV/bar identification from GENERAL operadic theory, not case-by-case analysis.
healing_20260413_132214/H07_MC5_alt_approach.md:128:I need to determine if the requested content conflicts with AGENTS. The user mentioned a technique involving SC^ch,top Koszul duality, which connects SC-algebras with SC^!-coalgebras in the coderived category. This seems to be automatically derived from Livernet Koszulity and the general bar-cobar construction. However, AGENTS states that SC^{ch,top} isn't related to B(A), which is an E1 coalgebra, while SC is defined on the pair (C_ch^\bullet(A,A),A).
healing_20260413_132214/H07_MC5_alt_approach.md:232:/bin/zsh -lc "rg -n \"MC5|BV|bar identification|coderived|harmonic|Swiss|Koszul dual|SC\\"'^'"\\{ch,top\\}|BV/bar\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
healing_20260413_132214/H07_MC5_alt_approach.md:282:32:all-genera coderived comparison of
healing_20260413_132214/H07_MC5_alt_approach.md:283:33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
healing_20260413_132214/H07_MC5_alt_approach.md:332:becomes an isomorphism in the coderived quotient
healing_20260413_132214/H07_MC5_alt_approach.md:339:of Definition~\ref{def:coderived-fact}. This is the required
exec
/bin/zsh -lc 'rg -n "coderived" chapters -n | head' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/typeA_baxter_rees_theta.tex:8:% Appendices~\ref{app:nilpotent-completion} and~\ref{app:coderived}.
chapters/connections/typeA_baxter_rees_theta.tex:56:curved case, coderived categories; see
chapters/connections/typeA_baxter_rees_theta.tex:57:Appendices~\ref{app:nilpotent-completion} and~\ref{app:coderived}.
chapters/connections/typeA_baxter_rees_theta.tex:95: extension to the completed/coderived Baxter envelope becomes formal.
chapters/connections/typeA_baxter_rees_theta.tex:772:Let $\widehat{\mathcal O}$ be a completed or coderived enhancement of the
chapters/connections/typeA_baxter_rees_theta.tex:1315:package should extend that equivalence to the completed/coderived ambient.
chapters/connections/typeA_baxter_rees_theta.tex:1370: The completed or coderived Yangian category satisfies the hypotheses
chapters/connections/typeA_baxter_rees_theta.tex:1382:equivalence on the completed/coderived Baxter envelope. Under this
chapters/connections/typeA_baxter_rees_theta.tex:1393:then extends the compact-core equivalence to the completed/coderived
chapters/connections/typeA_baxter_rees_theta.tex:1411: \item verify the Baxter-envelope hypotheses on the completed/coderived
codex
I now have the main support theorems: the coderived bar-degree spectral sequence gives the clean spectral surrogate, and the strong completion/weight-cutoff package gives the clean completed-category surrogate. I’m checking one more ingredient: the local theorem surface that explicitly says class `M` has infinite shadow depth, because the remark needs to tie the failure mechanism to an already-proved structural source, not just prose.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '1680,1765p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"infinite shadow|shadow obstruction tower is infinite|d_alg = \\\\infty|class~M|r_{\\\\max} = \\\\infty|Postnikov|nontermination|Virasoro.*infinite|W_N.*infinite\" chapters/examples chapters/connections chapters/theory | head -n 200" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_holographic_reconstruction.tex | sed -n '1620,1775p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1680	\subsection{Gravitational Yangian for Virasoro}
  1681	\label{subsec:thqg-V-virasoro-yangian}
  1682	\index{Virasoro!gravitational Yangian|textbf}
  1683	\index{gravitational Yangian!Virasoro}
  1684	
  1685	The Virasoro algebra is the simplest class-$M$ algebra: its shadow
  1686	tower is infinite, the $r$-matrix has higher-order poles, and the
  1687	genus-zero gravitational Yangian exhibits the richest explicit binary
  1688	collision data among the standard test cases. This subsection
  1689	computes the explicit gravitational $r$-matrix, the three-graviton
  1690	vertex, and the representation-theoretic data.
  1691	
  1692	
  1693	\subsubsection{The gravitational $r$-matrix}
  1694	
  1695	\begin{construction}[Explicit gravitational $r$-matrix for Virasoro;
  1696	\ClaimStatusProvedHere]
  1697	\label{constr:thqg-V-vir-r-explicit}
  1698	\index{Virasoro!r-matrix@$r$-matrix!explicit}
  1699	\index{r-matrix@$r$-matrix!Virasoro!explicit construction}
 succeeded in 51ms:
  1620	
  1621	% ================================================================
  1622	% 9.8.14: THE POSTNIKOV FILTRATION
  1623	% ================================================================
  1624	
  1625	\subsection{Obstruction tower and Postnikov filtration}
  1626	\label{subsec:obstruction-tower}
  1627	\index{obstruction tower|textbf}
  1628	\index{Postnikov filtration!shadow tower}
  1629	
  1630	\begin{definition}[Postnikov $k$-invariant of the
  1631	shadow obstruction tower]
  1632	\label{def:shadow-k-invariant}
  1633	\index{Postnikov $k$-invariant!shadow tower}
  1634	The \emph{$r$-th $k$-invariant} of the shadow obstruction tower is
  1635	the obstruction class
  1636	\begin{equation}\label{eq:shadow-k-invariant}
  1637	k_r(\cA) := o_{r+1}(\cA) \in H^2(J^{r+1}(\cA), d_2).
  1638	\end{equation}
  1639	The shadow obstruction tower is
 succeeded in 51ms:
rg: regex parse error:
    (?:infinite shadow|shadow obstruction tower is infinite|d_alg = \infty|class~M|r_{\max} = \infty|Postnikov|nontermination|Virasoro.*infinite|W_N.*infinite)
                                                                    ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc 'rg -n "shadow tower" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 5056

healing_20260413_132214/H04_thm_D_alt_proof.md:3:I updated the existing GRR remark in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:3030). The revised block now gives the alternative proof in the form you asked for: it starts from the bar family `\eqref{eq:bar-family}`, identifies the Hodge bundle `\mathbb E`, uses Hilbert-series control of the scalar fiber ranks, applies GRR on the universal curve, and extracts the codimension-`g` Hodge term as `\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g` on the uniform-weight lane. It now states explicitly that this route does not use the shadow tower, `\Theta_\cA`, or `Theorem~\ref{thm:genus-universality}` as input.
healing_20260413_132214/H04_thm_D_alt_proof.md:97:The primary proof routes through the shadow tower. Write an ALTERNATIVE:
healing_20260413_132214/H04_thm_D_alt_proof.md:105:5. This is INDEPENDENT of the shadow tower — it uses only the fiber-bundle structure
healing_20260413_132214/H04_thm_D_alt_proof.md:117:I’m locking the Theorem D claim surface in `chapters/theory/higher_genus_modular_koszul.tex` and reading the required constitutional files first. I’ll verify the current theorem statement and nearby conventions, then draft a GRR-based alternative proof path that is genuinely independent of the shadow tower route.
healing_20260413_132214/H04_thm_D_alt_proof.md:152:**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
healing_20260413_132214/H04_thm_D_alt_proof.md:255:  • Draft and insert a GRR/Hodge-theoretic remark that is independent of the shadow tower route and consistent with current theorem scope
healing_20260413_132214/H04_thm_D_alt_proof.md:476:/bin/zsh -lc "rg -n 'Alternative proof via GRR|Step~A|Step~B|Step~C|family-index|already constructed scalar obstruction|shadow tower' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
healing_20260413_132214/H04_thm_D_alt_proof.md:477:2912:The non-circular anchor is the bar-intrinsic shadow tower.
healing_20260413_132214/H04_thm_D_alt_proof.md:480:2996:\Theta_\cA \text{ and its shadow tower}
healing_20260413_132214/H04_thm_D_alt_proof.md:481:3004:The bar-intrinsic shadow tower is the common source.
healing_20260413_132214/H04_thm_D_alt_proof.md:488:3034:Theorem~D which does not use the shadow tower or the
healing_20260413_132214/H04_thm_D_alt_proof.md:489:3414:\index{random matrix theory!shadow tower}
healing_20260413_132214/H04_thm_D_alt_proof.md:495:12314:\index{Brown--Henneaux!shadow tower reading}
healing_20260413_132214/H04_thm_D_alt_proof.md:496:12995:\index{inverse limit!shadow tower}
healing_20260413_132214/H04_thm_D_alt_proof.md:573:\index{inverse limit!shadow tower}
healing_20260413_132214/H04_thm_D_alt_proof.md:614:3034:Theorem~D which does not use the shadow tower or the
healing_20260413_132214/H04_thm_D_alt_proof.md:921:-Theorem~D which does not use the shadow tower or the
healing_20260413_132214/H04_thm_D_alt_proof.md:923:+Theorem~D which does not use the shadow tower, the
exec
/bin/zsh -lc 'rg -n "coderived spectral" chapters -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:1666: coderived spectral sequence of
exec
/bin/zsh -lc "sed -n '1600,1750p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
the curvature forces passage to the coderived setting, and the
inversion theorem becomes a statement about coderived equivalences.
The central result of this chapter is the following.

\subsection{Statement of the main result}

\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
\textup{[Regime: quadratic on the strict lane; curved-central and
filtered-complete on the coderived lane
\textup{(}cf.\ Convention~\textup{\ref{conv:regime-tags})}.]}

The Heisenberg inversion $\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{H}_k)) \xrightarrow{\sim} \mathcal{H}_k$ (\S\ref{sec:frame-inversion}) generalizes to all Koszul chiral algebras.

Let $\mathcal{A}$ be a complete augmented chiral algebra on a
Riemann surface~$X$, with
$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ conilpotent or $\mathcal{A}$
complete with respect to its augmentation ideal
\textup{(}\S\ref{sec:i-adic-completion}\textup{)}, and with
finite-dimensional graded bar pieces whenever the coderived clause
below is invoked. The bar-cobar counit

thinking
**Rerunning with corrections**

I need to rerun the command, ensuring that I'm using the correct escaping. It's important that I get the relevant lines this time. I want to make sure I don’t miss anything crucial, so I’ll be careful with my syntax. Alright, let's go through the steps again, double-checking my inputs to achieve the best output. I’m eager to get this right!
exec
/bin/zsh -lc 'rg -n "completion" chapters -n | head' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'shadow tower is infinite|infinite shadow|nontermination|r_\\{\\\\max\\} = \\\\infty|d_alg|class-\\"'$M'"\\"'$|class~'"\\\\mathsf\\{M\\}|Virasoro.*infinite|W_N.*infinite' chapters/examples chapters/connections chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:43:the strong completion-tower framework
chapters/examples/w_algebras_deep.tex:48:by the pro-nilpotent completion of the convolution algebra, and the
chapters/examples/w_algebras_deep.tex:889:colimit involves analytic subtleties (completions, convergence of
chapters/examples/w_algebras_deep.tex:897:\begin{remark}[$\mathcal{W}_{1+\infty}$ completion data and the
chapters/examples/w_algebras_deep.tex:899:\label{rem:winfty-completion}
chapters/examples/w_algebras_deep.tex:900:\index{W1infinity@$\mathcal{W}_{1+\infty}$!completion data}
chapters/examples/w_algebras_deep.tex:906:enters the strong completion-tower theorem
chapters/examples/w_algebras_deep.tex:972:of a \emph{positive completion tower}: the infinite number of
chapters/examples/w_algebras_deep.tex:1392:(proved by the strong completion-tower theorem (Theorem~\ref{thm:completed-bar-cobar-strong}))
chapters/examples/w_algebras_deep.tex:3215:completion theorem applied to the $\mathcal{W}_N$ tower.
 succeeded in 51ms:
chapters/connections/thqg_gravitational_yangian.tex:335:$M$ & $r_{\max} = \infty$ & no finite collapse & Virasoro, $\mathcal{W}_N$ \\
chapters/connections/thqg_gravitational_yangian.tex:1685:The Virasoro algebra is the simplest class-$M$ algebra: its shadow
chapters/connections/thqg_gravitational_yangian.tex:1867:for class-$M$ algebras, the binary $r$-matrix must be supplemented
chapters/connections/thqg_gravitational_yangian.tex:2377:boundary operators. Its infinite shadow obstruction tower mirrors the expected
chapters/connections/thqg_gravitational_yangian.tex:2451: poles encoding the infinite shadow obstruction tower; the quartic contact
chapters/examples/deformation_quantization.tex:117:\item The Jacobi identity of the PVA ensures vanishing of $o_3$ (the cubic quantization obstruction). Higher obstructions $o_r$ for $r \geq 4$ are governed by the shadow obstruction tower of the quantized algebra and do not automatically vanish. (Koszulness of the quantized algebra is a separate property from shadow obstruction tower termination; both finite and infinite shadow depth algebras can be Koszul.)
chapters/connections/thqg_holographic_reconstruction.tex:233:If $r_{\max} = \infty$, then
chapters/connections/thqg_holographic_reconstruction.tex:288:\emph{Part~(ii): infinite shadow depth implies non-stabilization.}
chapters/connections/thqg_holographic_reconstruction.tex:289:Suppose $r_{\max} = \infty$. Then there exist
chapters/connections/thqg_holographic_reconstruction.tex:392:($r_{\max} = \infty$) are all chirally Koszul
chapters/connections/thqg_holographic_reconstruction.tex:899:$r_{\max} = \infty$. The quintic obstruction is
chapters/connections/thqg_holographic_reconstruction.tex:1722:for $r_{\max} = \infty$, it is a genuine formal scheme
chapters/connections/thqg_holographic_reconstruction.tex:1757: $r_{\max} = \infty$: the sequence
chapters/connections/thqg_holographic_reconstruction.tex:2118:boundaries carry an infinite shadow obstruction tower.
chapters/connections/thqg_open_closed_realization.tex:1389:$r_{\max} = \infty$). The quartic contact invariant
chapters/connections/editorial_constitution.tex:40:Virasoro/$\mathcal{W}_N$ infinite
chapters/connections/thqg_symplectic_polarization.tex:1717:For the Virasoro algebra, the shadow obstruction tower is infinite
chapters/connections/thqg_symplectic_polarization.tex:2084:The Virasoro shadow obstruction tower being infinite reflects the
chapters/examples/w_algebras_deep.tex:11:by the Jacobi identity) to class~M ($r_{\max} = \infty$, every
chapters/examples/w_algebras_deep.tex:940:Every finite stage $\mathcal{W}_N$ is class~M (infinite shadow
exec
/bin/zsh -lc 'rg -n "prop:coderived" -n chapters/theory' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:3815:(Proposition~\ref{prop:coderived-adequacy}(b)), so this
chapters/theory/bar_cobar_adjunction_inversion.tex:1667: Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}. Its
chapters/theory/bar_cobar_adjunction_inversion.tex:1839:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
chapters/theory/bar_cobar_adjunction_inversion.tex:1921:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
chapters/theory/bar_cobar_adjunction_inversion.tex:2302:Proposition~\ref{prop:coderived-bar-degree-spectral-sequence},
chapters/theory/coderived_models.tex:251:\label{prop:coderived-adequacy}
chapters/theory/coderived_models.tex:316:\label{prop:coderived-bar-degree-spectral-sequence}
chapters/theory/coderived_models.tex:787:(Proposition~\ref{prop:coderived-adequacy}(b)) provides the
chapters/theory/coderived_models.tex:1035: \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
chapters/theory/higher_genus_complementarity.tex:4499:Proposition~\ref{prop:coderived-adequacy}(a) remains.
exec
/bin/zsh -lc "sed -n '280,380p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\Omega_X \barB_X(\cA)$ and~$\cA$ is bounded below, exhaustive, and
preserved by~$\varepsilon$. Hence $K$ inherits a bounded-below
filtration. Its filtration-preserving differential is the strict
Chevalley--Cousin differential: the curved correction inserts at
least one diagonal contraction, so it lands in $F^1$ and disappears
from $\operatorname{gr}^0 K$. Thus each graded piece of
$\operatorname{gr} K$ is the cone of the strict
Chevalley--Cousin bar-cobar counit. Beilinson--Drinfeld's
Cousin-filtration argument gives that strict counit as a
quasi-isomorphism~\cite[Theorem~3.7.11]{BD04}, so the $E_1$ page of
the filtered cone vanishes. This proof is independent of
Theorem~\ref{thm:higher-genus-inversion}: it uses only the strict
curvature-zero Cousin model together with Positselski's filtered
coacyclicity criterion. By
\cite[Proposition~3.5]{Positselski11}, a bounded-below filtered
curved object with acyclic associated graded is coacyclic.
Therefore $K$ lies in the thick subcategory generated by
totalizations of short exact sequences and infinite direct sums, so
$\varepsilon$ is a coacyclic-equivalence and hence an isomorphism in
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
exec
/bin/zsh -lc 'rg -n "completed-bar-cobar-strong" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 679

healing_20260413_132214/H02_thm_B_alt_proof.md:354:Thm~\ref{thm:completed-bar-cobar-strong}) &
healing_20260413_132214/H02_thm_B_alt_proof.md:392:Quadratic algebras correspond to free field theories (Heisenberg $\leftrightarrow$ free boson, Kac--Moody $\leftrightarrow$ WZW). Curved algebras correspond to interacting theories with anomalies (Virasoro, with central charge $c$ measuring quantum breaking of scale invariance). Filtered algebras correspond to theories with composite operators ($W_3$ and Toda field theory). General algebras correspond to non-local theories ($W_\infty$), where the MC4 structural package is proved (Theorem~\ref{thm:completed-bar-cobar-strong}); the residual H-level comparison is example-specific.
appendices/nonlinear_modular_shadows.tex:3228:(Theorem~\ref{thm:completed-bar-cobar-strong}): the coefficient-stability
appendices/nonlinear_modular_shadows.tex:3479:(Theorem~\ref{thm:completed-bar-cobar-strong}) is established.
metadata/dependency_graph.dot:2073:  thm_completed_bar_cobar_strong [label="thm:completed-bar-cobar-strong\ntheorem [Pr]\nMC element lifts to the completed convol...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:131:| `thm:completed-bar-cobar-strong` | `theorem` | 946 | MC element lifts to the completed convolution algebra |
scripts/fix_campaign_100.py:146:Search for 'mc2-bar-intrinsic' and 'completed-bar-cobar-strong'. Fix cross-references.""")
wave2_audit_20260413_001942/C17_concordance.md:1937:  2010	 (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
wave2_audit_20260413_001942/F12_hidden_imports_cobar.md:1221:  1926	stable. Theorem~\ref{thm:completed-bar-cobar-strong} then applies.
metadata/label_index.json:47974:  "thm:completed-bar-cobar-strong": {
wave2_audit_20260413_001942/S06_intro_to_body.md:925:  2010	 (Theorem~\ref{thm:completed-bar-cobar-strong}) gives a
metadata/claims.jsonl:173:{"label": "cor:anomaly-duality-w", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/bv_brst.tex", "line": 1195, "title": "Curvature complementarity for principal \\texorpdfstring{$\\mathcal{W}$}{W}-algebra pairs", "refs_in_block": ["thm:wn-obstruction", "thm:quantum-complementarity-main", "thm:w-algebra-koszul-main", "thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:285:{"label": "conj:v1-master-infinite-generator", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 317, "title": "H-level target identification for standard infinite towers", "refs_in_block": ["thm:completed-bar-cobar-strong", "thm:coefficient-stability-criterion", "def:finite-window"]}
metadata/claims.jsonl:774:{"label": "cor:shadow-asymptotic-decay", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/connections/thqg_holographic_reconstruction.tex", "line": 1396, "title": "Asymptotic shadow decay", "labels_in_block": ["cor:shadow-asymptotic-decay", "eq:shadow-asymptotic"], "refs_in_block": ["thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:1684:{"label": "comp:wn-stabilization-windows", "env_type": "computation", "status": "ProvedHere", "file": "chapters/examples/w_algebras_deep.tex", "line": 3149, "title": "Coefficient stabilization windows for $\\mathcal{W}_N$", "refs_in_block": ["thm:coefficient-stability-criterion", "thm:completed-bar-cobar-strong", "lem:degree-cutoff"]}
metadata/claims.jsonl:1811:{"label": "cor:completed-bar-cobar-yangian", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 2064, "title": "Completed bar-cobar equivalence for Yangians", "refs_in_block": ["thm:completed-bar-cobar-strong"]}
metadata/claims.jsonl:1854:{"label": "cor:yangian-hlevel-comparison-criterion", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 4880, "title": "H-level comparison criterion for dg-shifted Yangians", "refs_in_block": ["prop:yangian-canonical-hlevel-target", "thm:completed-bar-cobar-strong", "thm:coefficient-stability-criterion"]}
metadata/claims.jsonl:1935:{"label": "cor:shifted-rtt-tower-convergence", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_foundations.tex", "line": 2969, "title": "Automatic tower convergence", "refs_in_block": ["thm:completed-bar-cobar-strong", "thm:coefficient-stability-criterion", "cor:yangian-bar-cobar"]}
exec
/bin/zsh -lc "nl -ba chapters/examples/w_algebras.tex | sed -n '5250,5315p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3260,3445p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  5250	\begin{tabular}{llll}
  5251	\toprule
  5252	\emph{Archetype} & \emph{Termination degree} &
  5253	\emph{Obstruction mechanism} & \emph{Tower type} \\
  5254	\midrule
  5255	Heisenberg & $2$ (Gaussian) & no higher operations &
  5256	exact quadratic \\
  5257	Affine & $3$ (Lie) & Jacobi identity &
  5258	quadratic + cubic \\
  5259	$\beta\gamma$ & $4$ (contact) & rank-one rigidity &
  5260	quartic on weight line \\
  5261	Virasoro/$\mathcal{W}_N$ & $\infty$ & permanent cubic source &
  5262	non-polynomial \\
  5263	\bottomrule
  5264	\end{tabular}
  5265	\end{center}
  5266	For the infinite-tower families, $\Theta_\cA = \varprojlim_r
  5267	\Theta_\cA^{\leq r}$
  5268	(Theorem~\ref{thm:recursive-existence}) is genuinely
  5269	infinite-order: the complementarity potential is non-polynomial.
 succeeded in 51ms:
  3260	Kac--Moody uses only two inputs: (i)~the existence of an
  3261	inner conformal vector in BRST cohomology, and (ii)~the
  3262	$Q$-exactness of holomorphic translations on $Q$-cohomology.
  3263	Both inputs are cohomological: the argument shows that the
  3264	factorization algebra becomes locally constant
  3265	\emph{on $Q$-cohomology} when applied to the original
  3266	complex. For affine Kac--Moody, the Sugawara mechanism
  3267	therefore gives two unconditional outputs:
  3268	\begin{enumerate}[label=\textup{(\roman*)}]
  3269	\item the cohomological $\Ethree^{\mathrm{top}}$ on
  3270	  $H_Q^\bullet(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA))$;
  3271	\item the chain-level $\Ethree^{\mathrm{top}}$ model on the
  3272	  zero-differential cohomology complex, which is
  3273	  quasi-isomorphic as a chain complex to the original
  3274	  derived center.
  3275	\end{enumerate}
  3276	What is not proved is the removal of the correction terms on
  3277	the \emph{original} cochain complex by an
  3278	$A_\infty$-coherent gauge homotopy. That is the exact gap
  3279	between parts~\textup{(ii)} and~\textup{(iii)} of
collab wait(call_X4rCQmLLQl3N4NFUC8NCWqz9)
  receivers: 019d86ad-48e2-7f53-a913-2d9f01425160
exec
/bin/zsh -lc 'rg -n "thm:bv-bar-coderived" -n chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
33:Theorem~\ref{thm:bv-bar-coderived}. Beyond genus~$0$, the
1853:Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
1861:curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
1908:powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
1917:\label{thm:bv-bar-coderived}%
2012:Theorem~\ref{thm:bv-bar-coderived}. The proof has two inputs:
2034:Theorem~\ref{thm:bv-bar-coderived}. By
2074:Theorem~\ref{thm:bv-bar-coderived} is the Swiss-cheese instance of the
2116:$d^2 = m_0 \cdot \mathrm{id}$ enters the picture. Theorem~\ref{thm:bv-bar-coderived}
2130:strict differential. Theorem~\ref{thm:bv-bar-coderived} shows that
2153:comparison map of Theorem~\ref{thm:bv-bar-coderived} becomes an
exec
/bin/zsh -lc "sed -n '1860,2200p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
shows that the full harmonic discrepancy still factors through the
curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
class~$\mathsf{M}$ BV and bar models in the coderived category even
though the strict chain-level comparison remains open.
\end{remark}

\begin{remark}[BV sewing at the chain level: class-by-class status;
 \ClaimStatusProvedHere]%
\label{rem:bv-sewing-chain-level-classes}%
\index{BV algebra!sewing operator identification|textbf}%
\index{sewing operator!BV Laplacian identification}%
\index{Bergman kernel!sewing contraction}%
The identification $\Delta_{\mathrm{BV}} = d_{\mathrm{sew}}$ at
the chain level asserts that the BV Laplacian and the bar sewing
operator agree as $(g,n) \to (g{+}1,n{-}2)$ operations on the
modular convolution algebra~$\gAmod$: both contract a pair of
inputs through the Bergman kernel $d\log E(z,w)$ along the
non-separating boundary divisor
$\delta^{\mathrm{ns}}\colon
\overline{\mathcal{M}}_{g,n+2} \to
exec
/bin/zsh -lc "rg -n -n \"tower.*converg\" chapters -g'*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/examples/w_algebras_deep.tex:4289:tower converges faster than the T-line (the
chapters/examples/yangians_foundations.tex:2967:\begin{corollary}[Automatic tower convergence;
chapters/examples/yangians_foundations.tex:2969:\label{cor:shifted-rtt-tower-convergence}
chapters/examples/yangians_foundations.tex:2983:\label{rem:shifted-rtt-tower-convergence-jet}
chapters/examples/yangians_foundations.tex:2984:Corollary~\ref{cor:shifted-rtt-tower-convergence} gives the proved
chapters/examples/kac_moody.tex:1756:shadow obstruction tower converges absolutely at all non-critical
chapters/examples/kac_moody.tex:1759:tower at generic levels (convergent only for
chapters/examples/genus_expansions.tex:1544:The scalar tower $F_g^{\mathrm{scal}} = \kappa(\cA)\,\lambda_g^{\mathrm{FP}}$ converges (Gevrey-$0$, $\hat{A}$-algebraicity). The cross-channel
chapters/examples/yangians_drinfeld_kohno.tex:6702:MC tower $\{\tau_N\}_N$ to converge in the completed convolution
chapters/examples/w_algebras.tex:2345:For $\mathfrak{g} = \mathfrak{sl}_N$ (exponents $1, 2, \ldots, N-1$), $\varrho = H_N - 1$, recovering Theorem~\ref{thm:wn-obstruction}. The non-monotonicity in rank (e.g., $\varrho(E_8) < \varrho(E_6)$) reflects the spacing of the exponents: $E_8$ has large exponents ($29, 23, \ldots$) giving small $1/(m_i + 1)$ contributions. The isomorphism $B_2 \cong C_2$ ($\mathfrak{so}_5 \cong \mathfrak{sp}_4$) gives identical exponents and anomaly ratios; both have $h^\vee = 3$ (not $h = 4$), and the level shift $k' = -k - 2h^\vee = -k - 6$ uses the dual Coxeter number. Among the non-simply-laced types, $G_2$ has the lowest anomaly ratio ($2/3$) and $F_4$ the highest ($7/8$); both are less than $1$, so the associated $\mathcal{W}$-algebra shadow obstruction towers converge.
chapters/examples/w_algebras.tex:4499:The tower converges ($\rho < 1$) for $N \geq 4$ at this level.
chapters/connections/typeA_baxter_rees_theta.tex:486:For the principal RTT tower the correct convergence notion is
chapters/frame/guide_to_main_results.tex:118: The full shadow obstruction tower converges:
chapters/connections/thqg_holographic_reconstruction.tex:1414:\item For $|c| > 6$: the shadow obstruction tower converges
chapters/connections/thqg_holographic_reconstruction.tex:1426:\index{analytic sewing!shadow tower convergence}
chapters/connections/thqg_holographic_reconstruction.tex:1433:tower must converge in an appropriate operator norm to
chapters/connections/thqg_holographic_reconstruction.tex:1512:The shadow obstruction tower converges rapidly.
chapters/connections/thqg_holographic_reconstruction.tex:2019:The shadow obstruction tower converges rapidly. The Koszul dual
chapters/connections/editorial_constitution.tex:133:\emph{does the modular extension tower of\/~$\cA$ converge?}
chapters/connections/concordance.tex:2753:$c > c_\star$ the tower converges ($\rho < 1$), for
exec
/bin/zsh -lc "sed -n '12980,13050p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
the specific representation theory of~$\fg$ enters.
\end{remark}

\begin{construction}[Obstruction recursion]
\label{constr:obstruction-recursion}
Suppose a truncated solution $\Theta_{\cA}^{\leq N}$ has been
constructed through weight $N$. Its next obstruction is
\begin{equation}
\label{eq:next-obstruction}
\mathfrak{o}_{N+1}
:=
\Bigl(
D_{\cA}\Theta_{\cA}^{\leq N}
+ \tfrac12[\Theta_{\cA}^{\leq N},
\Theta_{\cA}^{\leq N}]
\Bigr)_{N+1}.
\end{equation}
If $[\mathfrak{o}_{N+1}] \in H^2(F^{N+1}/F^{N+2})$ vanishes,
choose a contracting homotopy $h$ and define
$\Theta_{\cA,N+1} := -h(\mathfrak{o}_{N+1})$.
exec
/bin/zsh -lc "rg -n \"class~\\\\mathsf\\{M\\}\" -n chapters/theory" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:class~\mathsf\{M\})
             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n 'class~\\\\mathsf\\{M\\}' chapters -n" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "infinite shadow" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 757

healing_20260413_132214/H10_depth_gap_alt.md:840: all nonzero & infinite shadow tower \\
healing_20260413_132214/H08_topol_alt_proof.md:1927:+  the infinite shadow tower produces genuine higher chain-level terms
healing_20260413_132214/H08_topol_alt_proof.md:2139:+  the infinite shadow tower produces genuine higher chain-level terms
scripts/healing_fortification_40.py:448:1. WHY does chain-level fail for class M? The infinite shadow tower means infinitely
appendices/_sl2_yangian_insert.tex:639:algebra (class~$\mathbf M$, quartic poles, infinite shadow depth),
appendices/combinatorial_frontier.tex:480:dimensions is a consequence of the infinite shadow obstruction tower
appendices/ordered_associative_chiral_kd.tex:3236:\textup{(}infinite shadow depth\textup{)}.
appendices/ordered_associative_chiral_kd.tex:3816:a triple-pole collision residue and class~M (infinite shadow
audit_campaign_20260412_231034/BC05_c_26.md:1457:\item $\Theta_c$ has infinite shadow depth (mixed archetype);
tmp_standalone_audit/wrap_programme_summary_sections5_8_fixed.tex:120:poles (class~$\mathbf{M}$) have infinite shadow towers and
audit_campaign_20260412_231034/BC03_c_zero.md:375:22:forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
audit_campaign_20260412_231034/F20_WN_weights.md:584:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:684:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
tmp_standalone_audit/wrap_programme_summary_sections9_14_fixed.tex:194: infinite shadow tower from finite data.
audit_campaign_20260412_231034/AP16_arity_banned.md:614:to all arities, and the infinite shadow depth (class~M) means the tower
audit_campaign_20260412_231034/F04_kappa_WN.md:236:/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:684:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
audit_campaign_20260412_231034/F04_kappa_WN.md:548:The $\cW_{1+\infty}$ algebra has generators at each spin $s = 1, 2, 3, \ldots$, giving per-channel modular characteristics $\kappa_s = 1/s$. The total $\kappa_{\mathrm{ch}} = \sum_{s=1}^{N} \kappa_s = H_N$ (the $N$-th harmonic number, divergent as $N \to \infty$). The effective $\kappa_{\mathrm{ch}}$ per MacMahon level is $1$ (constant): the $n$-fold multiplicity of degree-$n$ BPS states exactly compensates the $1/n$ suppression. The overall classification is class~$\mathbf{M}$ (infinite shadow depth) when the full spin tower is included; it reduces to class~$\mathbf{G}$ at the Heisenberg truncation $s = 1$.
audit_campaign_20260412_231034/F04_kappa_WN.md:1696:The non-scalar corrections from $Q^{\mathrm{contact}} = 10/(c(5c+22))$ and the infinite shadow obstruction tower encode the genuinely nonlinear aspects of the gravitational theory, suppressed by $1/c^2$ relative to the scalar contribution.
audit_campaign_20260412_231034/CE08_stokes.md:971:     7	generates the infinite shadow obstruction tower of W_N.
exec
/bin/zsh -lc "rg -n \"class~\\\\mathsf\\{M\\}\" chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:class~\mathsf\{M\})
             ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n 'class~\\\\mathsf\\{M\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

wait(call_X4rCQmLLQl3N4NFUC8NCWqz9) timed out:
exec
/bin/zsh -lc "rg -n '\\\\mathsf\\{M\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
144: (class~$\mathsf{M}$, mixed).
155: partition $\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ is the
4554: For class~$\mathsf{M}$ (Virasoro, $\mathcal{W}_N$), the
17802:$\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$ are not an
25220: Class~$\mathsf{C}$ ($r_{\max} = 4$) and class~$\mathsf{M}$
25295: Class~$\mathsf{M}$ (Virasoro):
26289: ($\mathsf{G}/\mathsf{L}/\mathsf{C}/\mathsf{M}$) \\
26358:\textup{(3)}~For class-$\mathsf{M}$ algebras, does the
26458:For class~$\mathsf{M}$ $($Virasoro$)$: $S_3 = 2$, $\kappa = c/2$,
26544:$\mathsf{M}$ & Virasoro & all $S_r$
26549:semisimple locus, the MC tower from class-$\mathsf{M}$ algebras
26629:$\mathsf{M}$ smooth genus-$0$ curve.
26902:$\mathsf{M}$: all codimensions.
26968:Let $\cA$ be a chirally Koszul algebra of class~$\mathsf{M}$ with
27063:algebras of class~$\mathsf{M}$.
27374:\textup{(}class~$\mathsf{M}$, uniform-weight~$h = 2$\textup{)}.
27548:\item \emph{Class~$\mathsf{M}$
27567:class~$\mathsf{M}$ requires the full infinite tower.
27622: & Irreducibility of $Q_L$ (class~$\mathsf{M}$)
27630:of class~$\mathsf{M}$, is a theorem of the quadratic
exec
/bin/zsh -lc "sed -n '27530,27680p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 The non-perturbative completion is exact.

\item \emph{Classes~$\mathsf{L}$ and~$\mathsf{C}$
 \textup{(}affine Kac--Moody, $\beta\gamma$\textup{)}.}\enspace
 The shadow obstruction tower terminates at finite depth
 \textup{(}$r_{\max} = 3$ for class~$\mathsf{L}$,
 $r_{\max} = 4$ for class~$\mathsf{C}$\textup{)},
 but the genus expansion is an infinite series with
 Gevrey-$1$ factorial divergence. The Borel
 transform has isolated singularities at $\xi_n = n^2(2\pi)^2$,
 and the transseries~\eqref{eq:shadow-transseries} has
 instanton sectors with fluctuation coefficients determined
 entirely by the \emph{finite} shadow data
 $\{S_2 = \kappa(\cA),\, S_3,\, \ldots,\, S_{r_{\max}}\}$.
 The finitely many shadow invariants should determine the
 full resurgent structure: alien derivatives, Stokes
 automorphisms, and median resummation.

\item \emph{Class~$\mathsf{M}$
 \textup{(}Virasoro, $\cW_N$\textup{)}.}\enspace
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2140,2265p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
  2140	squares to zero regardless of curvature), so $B(\cA)$ lives
  2141	natively in $D^{\mathrm{co}}$. The BV complex, with its
  2142	$d^2_{\mathrm{BV}} = \kappa \cdot \omega_g$ at genus~$g$,
  2143	satisfies the same curved relation. The coderived
  2144	category is the minimal ambient in which both objects are
  2145	well-defined. The ordinary derived
  2146	category, which requires $d^2 = 0$, is too restrictive: it
  2147	forces a choice of ``strictification'' (lifting the curvature
  2148	into the differential via a Maurer--Cartan twist), and different
  2149	choices produce inequivalent chain complexes. The coderived
  2150	category avoids this choice. By
  2151	Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
  2152	curved objects are not set to zero in this localization; the
  2153	comparison map of Theorem~\ref{thm:bv-bar-coderived} becomes an
  2154	isomorphism precisely because its cone is coacyclic.
  2155	
  2156	The upshot: the BV quantisation of the worldsheet sigma model
  2157	and the algebraic bar construction of the boundary vertex algebra
  2158	live naturally in the same curved homological framework. The
  2159	chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
exec
/bin/zsh -lc "sed -n '1820,1895p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
The chiral-envelope functor produces compatible quotients recovering the principal stages; Proposition~\ref{prop:winfty-quotient-system-criterion} applies.
\end{proof}

%% Completion closure theory (raeeznotes85 absorption)

\begin{definition}[Completion closure of the finite-type regime]
\label{def:completion-closure}
\index{completion closure|textbf}
Let $\Fft$ denote the class of finite-type augmented curved chiral
$\Ainf$-algebras for which the finite-stage bar-cobar theorem is proved.
The \emph{completion closure} $\CompCl(\Fft)$ is the class of strong
completion towers $\cA = \varprojlim_N \cA_{\le N}$ with every quotient
$\cA_{\le N} \in \Fft$.

Dually, define $\Cstr$ to be the class of separated complete pronilpotent
curved dg chiral coalgebras $C = \varprojlim_N C_{\le N}$ such that each
$C_{\le N}$ lies in the finite-stage essential image.
\end{definition}

\begin{corollary}[Homotopy-categorical equivalence on the completion



thinking
**Organizing key references for spectral sequences and convergence**

I'll compile a minimal, well-structured list of relevant lemmas, theorems, corollaries, and remarks with their file paths and brief explanations—focusing on coderived spectral sequences, completion theorems, filtered/weight/shadow tower convergence, plus any remarks about class M infinite shadow tower or completed convergence. I also need to verify precise remark labels mentioning completion near key theorems.
exec
/bin/zsh -lc "rg -n \"Remark\\[.*completed\" chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc "rg -n \"Remark\\[.*completion\" -n" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

thinking
**Considering research insertion**

I need to search for remarks in en_koszul_duality or similar topics. It seems sensible to place the new research remark after "Why the coderived category is inevitable" at sections 2093-2164. I'll likely label it with a prefix like `rem:` and consider if it should include `\ClaimStatusOpen` since it's about ongoing research.

The user's question about "MC5 chain-level is FALSE for class M (Virasoro)" needs to be reflected in the remark, and I must keep it mathematically rigorous!
thinking
**Clarifying chain-level identification**

I can likely state that "The strict chain-level identification of Conj... is false in class M" when interpreting it in the uncompleted chain category using the explicit BV and bar models. However, I'm not certain we have proof of this falsehood since the file indicates "open," while editorial_constitution states it fails. 

Sources like concordance and CLAUDE indicate it's false for class M. I might summarize the status without adding a new theorem, but I need to ensure it doesn't contradict existing items in the document. The remark can highlight that the quartic discrepancy obstructs an unfiltered chain isomorphism!
thinking
**Aligning with user statement**

The user has explicitly stated that "MC5 chain-level is FALSE for class M (Virasoro)." Since this is a specific task, I think I should align my local remark with that statement. It might be helpful to create a research remark saying "the naive chain-level statement is false" and provide some explanations. 

However, I need to ensure this is supported by existing documentation, as editorial_constitution lines 444-446 indicate that the chain-level holds for G/L/C but fails for M due to the quartic harmonic obstruction.
exec
/bin/zsh -lc 'rg -n "remark.*class.*M" chapters/theory/higher_genus_modular_koszul.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '300,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   300	
   301	For (b): the PBW filtration by conformal weight is exhaustive,
   302	decreasing, preserved by all three components of the bar differential,
   303	and satisfies $m_0^{(g)} \in F^1$ because the curvature involves at
   304	least one OPE contraction. At associated graded level, the
   305	differential reduces to $\dzero$, which is strict.
   306	
   307	For (c): Verdier duality preserves the PBW filtration
   308	(it exchanges weight~$n$ generators with weight~$n$ cogenerators in
   309	the Koszul dual) and commutes with the bar differential. Hence it
   310	descends to $\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$ and the
   311	eigenspace decomposition is well-defined.
   312	\end{proof}
   313	
   314	\begin{proposition}[Coderived bar-degree spectral sequence;
   315	\ClaimStatusProvedHere]
   316	\label{prop:coderived-bar-degree-spectral-sequence}
   317	\index{coderived category!bar-degree spectral sequence|textbf}
   318	\index{bar-cobar inversion!coderived filtration}
   319	Let
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1620,1770p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1620	\[
  1621	\psi \colon \Omega(\bar{B}(\mathcal{A})) \longrightarrow \mathcal{A}
  1622	\]
  1623	is the adjunction counit and hence a canonical morphism of chiral
  1624	algebras. Its strongest proved form is:
  1625	\begin{enumerate}
  1626	\item \emph{Strict Koszul lane.}
  1627	 If $\mathcal{A}$ is Koszul
  1628	 \textup{(}Definition~\ref{def:koszul-chiral-algebra}; equivalently,
  1629	 $\cA \in \operatorname{Kosz}(X)$\textup{)}, then the genus-$0$
  1630	 counit
  1631	 \[
  1632	 \psi_0 \colon \Omega_0(\bar{B}_0(\mathcal{A})) \longrightarrow \mathcal{A}
  1633	 \]
  1634	 is a quasi-isomorphism of chiral algebras.
  1635	 If, in addition, $\mathcal{A}$ lies on the higher-genus Koszul locus
  1636	 of Theorem~\ref{thm:higher-genus-inversion}
  1637	 \textup{(}for the standard landscape, by
  1638	 Theorems~\ref{thm:pbw-allgenera-km}--\ref{thm:pbw-allgenera-principal-w}\textup{)},
  1639	 then each genus component
codex
Plan for the scoped edit:

1. Re-read the end of the coderived-comparison lane in [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex) and place a new research remark where it clarifies, rather than duplicates, the existing theorem/remarks.
2. State the negative result sharply but locally: why naive ordinary chain-level BV=`bar` fails for class `M`, using the quartic non-coboundary and the infinite shadow tower.
3. Fortify the frontier with two replacement lanes:
   - a spectral statement grounded in [chapters/theory/coderived_models.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/coderived_models.tex) via the coderived bar-degree spectral sequence;
   - a completed statement grounded in [chapters/theory/bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex) via the strong completion / weight-cutoff theorems.
4. Verify the new remark against nearby status language, grep for label uniqueness and banned prose, and run the narrowest TeX/grep checks I can do locally.

I’m checking the dirty surface now, then I’ll patch the chapter.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M chapters/theory/chiral_koszul_pairs.tex
 M chapters/theory/higher_genus_complementarity.tex
 M main.log
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '900,1020p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   900	\[
   901	\cA = F^0\cA \supset F^1\cA \supset F^2\cA \supset \cdots,
   902	\qquad
   903	\textstyle\bigcap_{N \ge 0} F^{N+1}\cA = 0,
   904	\]
   905	such that:
   906	\begin{enumerate}
   907	\item $\cA$ is separated and complete:
   908	 $\cA \cong \varprojlim_N \cA_{\le N}$, where
   909	 $\cA_{\le N} := \cA/F^{N+1}\cA$;
   910	\item every quotient $\cA_{\le N}$ is finite type and lies in the proved
   911	 bar-cobar regime;
   912	\item $\bar\cA = F^1\cA$ (the augmentation ideal is the first filtration
   913	 piece); and
   914	\item all chiral $\Ainf$-operations are filtration-nondecreasing:
   915	 \begin{equation}\label{eq:strong-filtration-condition}
   916	 \mu_r(F^{i_1}\cA, \dots, F^{i_r}\cA)
   917	 \subset F^{i_1+\cdots+i_r}\cA.
   918	 \end{equation}
   919	\end{enumerate}
exec
/bin/zsh -lc "rg -n '\\\\label\\{rem:bv-bar-class-m' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{rem:bv-bar-coderived' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 142ms:

 succeeded in 154ms:
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H07_MC5_alt_approach.md:345:\label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H07_MC5_alt_approach.md:719:\label{rem:bv-bar-coderived-operadic}%
/Users/raeez/chiral-bar-cobar/healing_20260413_132214/H07_MC5_alt_approach.md:1304:  2030	\label{rem:bv-bar-coderived-operadic}%
/Users/raeez/chiral-bar-cobar/fix_wave_A_20260413_112727/A12_fix_broken_refs_v1_rest.md:1014:chapters/connections/bv_brst.tex:1951:\label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/S11_bv_brst_to_body.md:382:1951:\label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U09_missing_examples.md:1224:chapters/connections/bv_brst.tex:1951:\label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/U09_missing_examples.md:1226:chapters/connections/bv_brst.tex:1973:\label{rem:bv-bar-coderived-why}
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:1070: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:1478: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:1895: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:2368: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:2812: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:3233: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:3667: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:4091: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:4541: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:4608:\label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:4975: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:5392: \label{rem:bv-bar-coderived-higher-genus}%
/Users/raeez/chiral-bar-cobar/platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:5474:  2006	\label{rem:bv-bar-coderived-higher-genus}%
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_curved.tex | sed -n '1830,1875p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1830	The \emph{completion closure} $\CompCl(\Fft)$ is the class of strong
  1831	completion towers $\cA = \varprojlim_N \cA_{\le N}$ with every quotient
  1832	$\cA_{\le N} \in \Fft$.
  1833	
  1834	Dually, define $\Cstr$ to be the class of separated complete pronilpotent
  1835	curved dg chiral coalgebras $C = \varprojlim_N C_{\le N}$ such that each
  1836	$C_{\le N}$ lies in the finite-stage essential image.
  1837	\end{definition}
  1838	
  1839	\begin{corollary}[Homotopy-categorical equivalence on the completion
  1840	closure; \ClaimStatusProvedHere]
  1841	\label{cor:completion-closure-equivalence}
  1842	\index{completion closure!homotopy equivalence}
  1843	If one localizes strong completion towers and objects in $\Cstr$ by
  1844	quotientwise quasi-isomorphisms, then
  1845	\[
  1846	\widehat{\bar B}^{\mathrm{ch}} \;\dashv\; \widehat\Omega^{\mathrm{ch}}
  1847	\]
  1848	induces an equivalence of homotopy categories. That is,
  1849	Theorem~\textup{\ref{thm:completed-bar-cobar-strong}} gives quasi-inverse
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '13000,13080p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 13000	Then $\Theta_{\cA}^{\leq N+1} := \Theta_{\cA}^{\leq N}
 13001	+ \Theta_{\cA,N+1}$ solves the Maurer--Cartan equation through
 13002	weight $N+1$.
 13003	\end{construction}
 13004	
 13005	\begin{theorem}[Recursive existence and shadow obstruction tower convergence;
 13006	\ClaimStatusProvedHere]
 13007	\label{thm:recursive-existence}
 13008	\index{recursive existence!proved}
 13009	\index{shadow obstruction tower!convergence}
 13010	\index{inverse limit!shadow tower}
 13011	Let $\cA$ be a modular Koszul chiral algebra.
 13012	\begin{enumerate}[label=\textup{(\roman*)}]
 13013	\item \emph{Recursive lift.}
 13014	 All obstruction classes in the extension tower
 13015	 $\{\mathcal{E}_{\cA}(N)\}_{N \geq 1}$
 13016	 \textup{(}Definition~\textup{\ref{def:extension-tower})}
 13017	 vanish: for every $N \geq 1$, the class
 13018	 $[\mathfrak{o}_{N+1}] \in
 13019	 H^2(F^{N+1}\gAmod / F^{N+2}\gAmod)$ of

exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '27480,27590p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 27480	$\kappa(\cA)$. The effective anomaly cancellation
 27481	$\kappa_{\mathrm{eff}} = \kappa(\mathrm{matter}) +
 27482	\kappa(\mathrm{ghost}) = 0$ at $c = 26$
 27483	manifests as a vanishing of the \emph{sum} of leading Stokes
 27484	multipliers $\mathfrak{S}_1(\cA) + \mathfrak{S}_1(\cA_{\mathrm{ghost}})$
 27485	at the critical dimension.
 27486	\end{remark}
 27487	
 27488	\begin{remark}[Cross-channel instanton action exceeds the scalar]
 27489	\label{rem:cross-channel-instanton-heavier}
 27490	\index{instanton action!cross-channel}
 27491	\index{resurgence!cross-channel}
 27492	The scalar instanton action $A_{\mathrm{scal}} = (2\pi)^2$
 27493	governs the large-order asymptotics of the scalar free energy
 27494	$F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$. For multi-weight
 27495	algebras ($\cW_3$, $\cW_4$, \ldots), the cross-channel correction
 27496	$\delta F_g^{\mathrm{cross}}$ has its own large-order behaviour.
 27497	Unlike the scalar series, the polynomial degree of
 27498	$\delta F_g^{\mathrm{cross}}$ in~$c$ grows with genus
 27499	(degree~$0$ at $g = 2$, degree~$1$ at $g = 3$), so the
thinking
**Choosing a new label**

I need to pick a new, unique label, possibly something like `rem:bv-bar-class-m-research` or `rem:bv-bar-class-m-frontier`. I want to make sure it’s distinctive. I think using a simple command with the path `/Users` would work well, but I might need to wait for the explorer's results before finalizing anything. Let’s keep it straightforward and see what the explorer reveals!
collab wait(call_3zQJ2riM7nmvszPUdL7PNZOw)
  receivers: 019d86ad-48e2-7f53-a913-2d9f01425160
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '27588,27660p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 27588	
 27589	\begin{observation}[Two towers, two Borel types]
 27590	\label{obs:two-borel-types}
 27591	\index{Borel transform!genus tower vs.\ shadow tower}%
 27592	\index{Gevrey class!shadow obstruction tower}%
 27593	\index{resurgence!two-tower dichotomy}
 27594	The MC element $\Theta_\cA = \sum_{g,r}
 27595	\Theta_r^{(g)}\,\hbar^{2g}\,t^r$ is a double series
 27596	whose two marginal expansions have incompatible
 27597	analytic behaviour.
 27598	\begin{center}
 27599	\small
 27600	\renewcommand{\arraystretch}{1.15}
 27601	\begin{tabular}{@{}lll@{}}
 27602	 & \textbf{Genus tower $F_g$}
 27603	 & \textbf{Shadow obstruction tower $S_r$} \\
 27604	\hline
 27605	Growth
 27606	 & $O((2\pi)^{-2g})$, exponential decay
 27607	 & $O(\rho^r)$, geometric growth \\[3pt]

thinking
**Organizing minimal reference list for spectral and convergence results**

I'm gathering exact label names, file locations with line numbers, and concise summaries for key results related to coderived spectral sequences, completion theorems, filtered or shadow tower convergence, and observations on class M infinite towers. I plan to structure the final answer as a grouped bullet list highlighting the minimal set of references that directly answer the user's question.
codex
- **Coderived spectral sequence**  
  * `Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}` (`chapters/theory/coderived_models.tex:314-342`) – The bar-degree filtration on any filtered curved factorization cone produces an $E_1$ spectral sequence whose vanishing is equivalent to the associated-graded map being a strict quasi-isomorphism; Positselski’s bounded-below criterion then implies the cone is coacyclic, so the comparison becomes an isomorphism in $D^{\mathrm{co}}$.  
  * `Theorem~\ref{thm:bar-cobar-inversion-qi}` (`chapters/theory/bar_cobar_adjunction_inversion.tex:1620-1701`) – In the non-Koszul regime, the same filtration is invoked to show the bar–cobar counit is coacyclic via the coderived spectral sequence, so the graded differential absorbs the curvature and the coderived equivalence survives even though the ordinary spectral sequence may carry higher differentials (the strict collapse only reappears when the spectral sequence degenerates, e.g., class~$G/L$).

- **Completion theorems**  
  * `Theorem~\ref{thm:completed-bar-cobar-strong}` (`chapters/theory/bar_cobar_adjunction_curved.tex:944-1014`) – For any strong completion tower (MC4 hypothesis), the completed bar/cobar constructions exist, their limit twisting morphism is acyclic, and completed bar/cobar form quasi-inverse equivalences; the Milnor/Mittag‑Leffler input guarantees the completed MC equation converges.  
  * `Corollary~\ref{cor:completion-closure-equivalence}` (`chapters/theory/bar_cobar_adjunction_curved.tex:1839-1851`) – Localizing strong towers and their coalgebra duals by quotientwise quasi-isomorphisms yields a homotopy-category equivalence, so the completed category described in `bv_brst` really carries the same homotopy type as the inverse-limit bar/cobar data.

- **Filtered/weight/shadow tower convergence**  
  * `Theorem~\ref{thm:recursive-existence}` (`chapters/theory/higher_genus_modular_koszul.tex:13005-13032`) – The weight filtration on $\gAmod$ is exhaustive, complete and pronilpotent, hence every obstruction in the extension tower vanishes and the inverse limit $\Theta_\cA=\varprojlim\Theta^{\leq N}_\cA$ exists in the weight completion; this provides the convergence of the modular (shadow) tower needed to speak meaningfully about the completed MC element, matching the “completed convergence” remark in `bv_brst`.

- **Existing remark on class~$\mathsf{M}$ infinite shadow tower**  
  * `Observation~\ref{obs:two-borel-types}` (`chapters/theory/higher_genus_modular_koszul.tex:27589-27639`) – The double-series data clearly separates the convergent genus tower from the divergent shadow tower: for class~$\mathsf{M}$ the shadow tower grows like $\rho^r$, its $Q_L$-irreducibility forces finite radius, and the shadow direction therefore carries the infinite obstruction tower mentioned in `bv_brst`, so any future chain-level lift must address that infinite-resurgence structure.
wait(call_3zQJ2riM7nmvszPUdL7PNZOw) 1 agents complete:
  019d86ad-48e2-7f53-a913-2d9f01425160 completed: "- **Coderived spectral sequence**  
  * `Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}` (`chapters/theor…"
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1580,1715p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1580	 finite-dimensional graded pieces, which is
  1581	 needed for the duality between contramodules and complete modules
  1582	 (Remark~\ref{rem:chiral-contramodules}).
  1583	\end{enumerate}
  1584	These geometric inputs are specific to the chiral setting and have
  1585	no analogue in Positselski's ground-field framework.
  1586	\end{remark}
  1587	
  1588	%================================================================
  1589	% SECTION: BAR-COBAR INVERSION - COMPLETE QUASI-ISOMORPHISM
  1590	%================================================================
  1591	
  1592	\section{Bar-cobar inversion}
  1593	\label{sec:bar-cobar-inversion-quasi-iso}
  1594	
  1595	The comodule-contramodule correspondence of the preceding section
  1596	provides the categorical framework in which bar-cobar inversion
  1597	lives: at genus~$0$ the coderived category reduces to the
  1598	ordinary derived category, and the inversion theorem is a
  1599	quasi-isomorphism in the classical sense; at genus~$g \geq 1$

thinking
**Searching for research remarks**

I need to find if there's a "Research Remark" style label in the file. It seems I could add a comment without a status, maybe titled "Research direction: classM between coderived and chain-level". I should search for existing "Research direction" patterns. I’m thinking of mimicking the en_koszul_duality research direction. The title might be `[Research direction: class$\mathsf{M}$ spectral and completed BV/bar comparison]`, with a status of either none or `\ClaimStatusOpen`. I'll check how other research remarks are formatted using rg.
exec
/bin/zsh -lc 'rg -n "Research direction|Research remark|research direction|research remark" chapters/connections/bv_brst.tex chapters/theory/en_koszul_duality.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/coderived_models.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:3391:\begin{remark}[Research direction: chain-level topologization]
chapters/theory/en_koszul_duality.tex:3393:\index{topologization theorem!chain-level research direction}%
exec
/bin/zsh -lc 'rg -n "ClaimStatusOpen" chapters/connections chapters/theory | head -n 80' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/arithmetic_shadows.tex:10417:\ClaimStatusOpen%
chapters/connections/arithmetic_shadows.tex:11089:\ClaimStatusOpen%
chapters/theory/ordered_associative_chiral_kd.tex:6463:\ClaimStatusOpen
chapters/connections/concordance.tex:8174:\ClaimStatusOpen{}
chapters/connections/concordance.tex:8211:\ClaimStatusOpen{}
chapters/connections/concordance.tex:8246:\ClaimStatusOpen{}
chapters/connections/concordance.tex:10044:\ClaimStatusOpen{}
chapters/connections/semistrict_modular_higher_spin_w3.tex:746:\begin{problem}[One-loop quantization of the semistrict $W_3$ package \ClaimStatusOpen]


thinking
**Exploring coderived concepts**

I’m considering whether coderived results can be enhanced to create an intermediate level between coderived and chain-level. I could propose ideas like a "provisional coderived category of filtered curved models" or a "completion closure localized by quotientwise quasi-isomorphisms" as possible intermediates. This seems like a complex but intriguing path to explore! There’s definitely a lot to unpack here, and I can’t wait to see where this thinking leads!
thinking
**Assessing proof soundness**

I think we need to mention in the final report that we have primary proof sound and secondary proof written as the existing operadic route, using the technique of operadic Koszul duality. The condition status is unconditional in coderived, although chain-level is false for class M. 

I should verify if the primary proof is sound. Assessing that might be useful, so maybe I can say yes, but with a caveat to consider.
codex
PE-7: label creation

```text
environment: remark
label: \label{rem:bv-bar-class-m-frontier}
prefix match (AP125): Y
AP124 duplicate check: Vol I:0 Vol II:0 Vol III:0 total before:0 after:1 delta=1? Y
verdict: ACCEPT
```

I’m editing [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex) next. The insertion will sit after the coderived-inevitability remark and will do four things in one place: state why naive class-`M` chain level fails, formulate the spectral replacement, formulate the completed replacement, and isolate the filtered-completed strengthening between raw chain level and bare coderived equivalence.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -2165,2 +2165,75 @@
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
apply_patch(auto_approved=true) exited 0 in 34ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}


thinking
**Verifying inserted text**

I need to verify the inserted text and check for any banned terms. I should label the uniqueness and reference if they exist. It might be helpful to compile or at least grep for the labels. I’ll read through the inserted section carefully and consider running a quick search for banned words, including "remarkably," in the modified file. Also, I need to gauge if TeX syntax is acceptable for this task. I’ll utilize exec_commands to assist with this.
codex
The remark is in place. I’m re-reading the inserted block now for local mathematical coherence, then I’ll run narrow checks: label uniqueness, reference existence, and a banned-prose sweep on the touched file.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2148,2248p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2148	into the differential via a Maurer--Cartan twist), and different
  2149	choices produce inequivalent chain complexes. The coderived
  2150	category avoids this choice. By
  2151	Definitions~\ref{def:coacyclic-fact} and~\ref{def:coderived-fact},
  2152	curved objects are not set to zero in this localization; the
  2153	comparison map of Theorem~\ref{thm:bv-bar-coderived} becomes an
  2154	isomorphism precisely because its cone is coacyclic.
  2155	
  2156	The upshot: the BV quantisation of the worldsheet sigma model
  2157	and the algebraic bar construction of the boundary vertex algebra
  2158	live naturally in the same curved homological framework. The
  2159	chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
  2160	signal that the coderived category is unnecessary; it is the reason
  2161	the coderived category is the correct ambient. What remains open is
  2162	the stronger strict chain-level comparison in class~$\mathsf{M}$ and
  2163	the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
  2164	\end{remark}
  2165	
  2166	\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
  2167	\label{rem:bv-bar-class-m-frontier}
exec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{rem:bv-bar-class-m-frontier\\}|\\\\ref\\{prop:chain-level-three-obstructions\\}|\\\\ref\\{cor:virasoro-postnikov-nontermination\\}|\\\\ref\\{prop:coderived-bar-degree-spectral-sequence\\}|\\\\ref\\{prop:standard-strong-filtration\\}|\\\\ref\\{thm:completed-bar-cobar-strong\\}|\\\\ref\\{def:curved-weak-equiv\\}|\\\\ref\\{def:provisional-coderived\\}' chapters/connections/bv_brst.tex chapters/theory/coderived_models.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_curved.tex:78: MC4 completion (proved; Theorem~\ref{thm:completed-bar-cobar-strong}).
chapters/theory/bar_cobar_adjunction_curved.tex:325:(Theorem~\ref{thm:completed-bar-cobar-strong}), which upgrades the
chapters/theory/bar_cobar_adjunction_curved.tex:741:At the M/S level, the completed dual has infinitely many primitive cumulants ($\Delta_{\mathrm{Vir}}(t) = t^3 + 2t^5 + \cdots$; Definition~\ref{def:primitive-defect-series}). The MC4 structural framework is proved (Theorem~\ref{thm:completed-bar-cobar-strong}); the residual H-level target identification is the subject of Example~\ref{ex:winfty-completion-frontier}.
chapters/theory/bar_cobar_adjunction_curved.tex:857:(Theorem~\ref{thm:completed-bar-cobar-strong}) resolves this:
chapters/theory/bar_cobar_adjunction_curved.tex:1849:Theorem~\textup{\ref{thm:completed-bar-cobar-strong}} gives quasi-inverse
chapters/theory/bar_cobar_adjunction_curved.tex:1855:Theorem~\ref{thm:completed-bar-cobar-strong}(3)--(4). Both pass to
chapters/theory/bar_cobar_adjunction_curved.tex:1907:\item Theorem~\textup{\ref{thm:completed-bar-cobar-strong}} applies.
chapters/theory/bar_cobar_adjunction_curved.tex:1926:stable. Theorem~\ref{thm:completed-bar-cobar-strong} then applies.
chapters/theory/bar_cobar_adjunction_curved.tex:1974:Theorem~\ref{thm:completed-bar-cobar-strong} applies.
chapters/theory/bar_cobar_adjunction_curved.tex:2000:bar complex. Theorem~\ref{thm:completed-bar-cobar-strong} then applies
chapters/theory/bar_cobar_adjunction_curved.tex:2006:Theorem~\ref{thm:completed-bar-cobar-strong} together with the
chapters/theory/bar_cobar_adjunction_curved.tex:3481:(Theorem~\ref{thm:completed-bar-cobar-strong}). The
chapters/theory/bar_cobar_adjunction_curved.tex:3501:(Theorem~\ref{thm:completed-bar-cobar-strong}).
chapters/theory/bar_cobar_adjunction_curved.tex:5602:(Theorem~\ref{thm:completed-bar-cobar-strong}).
chapters/theory/coderived_models.tex:247:equivalences of Definition~\ref{def:curved-weak-equiv}.
chapters/theory/coderived_models.tex:419:(Definition~\ref{def:provisional-coderived}) embeds into
chapters/theory/coderived_models.tex:766:(Definition~\ref{def:curved-weak-equiv}(i)) induces a
chapters/theory/coderived_models.tex:1035: \textup{(}Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}\textup{)}
chapters/connections/bv_brst.tex:1235: (MC4 closed; Vol~I Theorem~\ref{thm:completed-bar-cobar-strong}).
chapters/connections/bv_brst.tex:1859:identity. Proposition~\ref{prop:chain-level-three-obstructions}
exec
/bin/zsh -lc "rg -n '\\\\label\\{rem:bv-bar-class-m-frontier\\}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2167:\label{rem:bv-bar-class-m-frontier}
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}



thinking
**Exploring LaTeX build options**

I’m considering using `latexmk` for a targeted verification, although the command is getting lengthy. Perhaps using `rg` for missing labels isn’t sufficient. I could try `perl -ne` or `sed -n` as alternatives. Since the user is asking for an end-to-end build when feasible, it seems right to run at least a targeted LaTeX build, especially since I’ve modified the main document. I'll take into account potential dirty files during this process too.
thinking
**Considering targeted build options**

I think running a targeted build using `latexmk` seems like a good idea. I want to set the `max_output` to maybe 12000 to give it enough room for generating the output without running into issues. This way, I can ensure that all necessary details are captured. It feels like the right approach to keep everything organized and effective, making sure I address any potential problems along the way. Let's proceed with this plan!
codex
The text is locally consistent and the reference surface resolves. I’m running a LaTeX build now to catch any syntax or cross-reference break introduced by the new remark; if the full build is too noisy, I’ll still extract the first real failure point.
exec
/bin/zsh -lc 'latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex' in /Users/raeez/chiral-bar-cobarfile update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}


thinking
**Waiting on build status**

I'm currently waiting for the build to complete, but I'm aware that it might not finish within the token limit. I think I might need to poll for the status a bit more since it seems there are quite a few undefined references due to the initial lack of auxiliary support. I guess I should be patient and see how it plays out. Let's wait and see!
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}

 exited 12 in 11.37s:
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (TeX Live 2025) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./main.tex
LaTeX2e <2024-11-01> patch level 2
L3 programming layer <2025-01-18>
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/memoir.cls
Document Class: memoir 2025/03/06 v3.8.3 configurable book, report, article doc
ument class
(/usr/local/texlive/2025/texmf-dist/tex/latex/xpatch/xpatch.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3kernel/expl3.sty
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def))
(/usr/local/texlive/2025/texmf-dist/tex/latex/l3packages/xparse/xparse.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/etoolbox/etoolbox.sty))
(/usr/local/texlive/2025/texmf-dist/tex/generic/iftex/iftex.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/memoir/mem11.clo)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/array.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/dcolumn.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/delarray.sty)
(/usr/local/texlive/2025/texmf-dist/tex/latex/tools/tabularx.sty)

thinking
**Checking output status**

I need to assess whether the output is still running or if it has halted. It looks like the first run didn't encounter any errors, just some undefined references since there was no auxiliary. My goal is to get confirmation on whether it will eventually stop with an actual error. Maybe poll after a bit to gather more information. I just want to make sure things are proceeding as expected!
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}



thinking
**Analyzing build errors**

I'm looking into a build failure due to an unrelated error in the file `higher_genus_complementarity.tex`. This means my edits aren't the cause of the failure. I’m considering if I can compile just the target chapter, though it's not straightforward. It’s clear that the full build is blocked by this pre-existing issue. I might need to check references with `rg`. If I run `latexmk`, there's a chance it won’t reach my chapter, but local verification of references in the build is already done. I should also think about doing a local TeX parse with `kpsewhich`.
thinking
**Reviewing build process**

I'm considering whether to use `pdflatex` with a minimal wrapper around just the target chapter. It might be a bit much, though. Perhaps using `texfot` isn’t necessary either. I think it would be wise to run `rg` to check line 677 in the file that’s causing the error to confirm it’s unrelated. Since the build is blocked by this other file that also appears in the git status, I should probably run `git diff -- chapters/connections/bv_brst.tex` to review it.
codex
The full build is blocked by a pre-existing unrelated error in [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:677): undefined control sequence `\ord`. I’m doing one final diff/readback on [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex) so the close-out is based on the exact inserted text, not the blocked global build.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '668,684p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   668	
   669	\begin{remark}[Alternative approach via shifted symplectic geometry]
   670	The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
   671	this chapter is bar-first: it constructs the ambient complex from the
   672	fiber bar family and then splits it by the Verdier involution. There is
   673	also a second route, conditional on the same perfectness and
   674	nondegeneracy package that later yields
   675	Theorem~\ref{thm:ambient-complementarity-fmp} and
   676	Proposition~\ref{prop:ptvv-lagrangian}. Start with the ordered bar
   677	resolution $B^{\ord}(\cA)$ together with its cyclic pairing. On the
   678	perfect duality locus of chiral Koszul pairs, that pairing identifies
   679	the tangent complex of the ambient moduli problem
   680	$\mathcal{M}_{\mathrm{comp}}(\cA)$ with its shifted dual, hence gives a
   681	canonical $(-1)$-shifted symplectic structure in the sense of
   682	Pantev--To\"en--Vaqui\'e--Vezzosi~\cite{PTVV13}. The one-sided loci
   683	$\mathcal{M}_{\cA}$ and $\mathcal{M}_{\cA^!}$ are then Lagrangian maps
   684	into the same ambient formal moduli problem.
 succeeded in 50ms:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab62017..7ebccfb 100644
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@ the stronger strict chain-level comparison in class~$\mathsf{M}$ and
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}

codex
I found one nearby inconsistency created by the new remark: the chapter still had older wording that called the class `M` strict chain-level comparison “open.” I’m tightening those local sentences now so the file says one consistent thing: naive strict chain level is false for class `M`; the open frontier is the filtered-completed refinement.
exec
/bin/zsh -lc "rg -n \"class~\\\\mathsf\\{M\\}.*open|strict chain-level comparison|chain-level open|remaining open question|open for class~\\\\mathsf\\{M\\}|ordinary chain-level comparison remains open\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:class~\mathsf\{M\}.*open|strict chain-level comparison|chain-level open|remaining open question|open for class~\mathsf\{M\}|ordinary chain-level comparison remains open)
             ^^
error: unrecognized escape sequence
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}

exec
/bin/zsh -lc "rg -n 'strict chain-level comparison|chain-level open|remaining open question|ordinary chain-level comparison remains open|class~\\\\mathsf\\{M\\}' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'fails for class~M|quartic harmonic obstruction|class~M' chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1716: the ordinary chain-level comparison remains open, but the
1863:though the strict chain-level comparison remains open.
1899: & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
1910:Definition~\ref{def:coacyclic-fact}. The remaining open question is
1911:the stronger strict chain-level comparison for class~$\mathsf{M}$ and
2162:the stronger strict chain-level comparison in class~$\mathsf{M}$ and
 succeeded in 51ms:
chapters/connections/editorial_constitution.tex:443:for all chirally Koszul algebras, including class~M.
chapters/connections/editorial_constitution.tex:445:\emph{fails} for class~M
chapters/connections/editorial_constitution.tex:446:\textup{(}quartic harmonic obstruction\textup{)}.
chapters/connections/concordance.tex:271:class~M (intrinsically non-formal, $r_{\max} = \infty$).
chapters/connections/concordance.tex:375: $\kappa = 12$, class~M, Niemeier discrimination
chapters/connections/concordance.tex:725: class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
chapters/connections/concordance.tex:1987: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
chapters/connections/concordance.tex:1989: conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
chapters/connections/concordance.tex:2680:while class~M algebras arising from DS reduction (Virasoro,
chapters/connections/concordance.tex:2864:class~M systems (gravity) have an infinite $\Ainf$ tower but
chapters/connections/concordance.tex:3035:(Proposition~\ref{prop:moonshine-kappa}), class~M
chapters/connections/concordance.tex:3380: (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
chapters/connections/concordance.tex:3383: (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
chapters/connections/concordance.tex:4442:(class~M). Bare $d(\cA)$ without subscript is forbidden.
chapters/connections/concordance.tex:7069: the chain-level identification fails for class~M.
chapters/connections/concordance.tex:7196: & depth decomposition $+$ class~M tower non-termination \\
chapters/connections/concordance.tex:7745: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
chapters/connections/concordance.tex:9833: chain-level false for class~M;
chapters/connections/concordance.tex:10232: all genera. The key mechanism for class~M: the degree-$r$
chapters/connections/concordance.tex:10261: For class~M, the chain-level identification \emph{fails}:
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}

exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1708,1915p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1708	 Although the quartic interaction vertex is nonzero
  1709	 \textup{(}shadow depth $r_{\max} = 4$\textup{)},
  1710	 the harmonic-propagator correction vanishes once the
  1711	 harmonic term factors through the composite free-field sector
  1712	 by the three-mechanism argument
  1713	 \textup{(}Remark~\textup{\ref{rem:bv-bar-class-c-proof}}\textup{)}.
  1714	 \item \emph{Class~M}
  1715	 \textup{(}Virasoro, $\cW_N$\textup{)}:
  1716	 the ordinary chain-level comparison remains open, but the
  1717	 quartic and higher interaction vertices produce a harmonic
  1718	 discrepancy that factors through the curvature:
  1719	 \[
  1720	 \delta_r^{\mathrm{harm}}
  1721	 \;=\;
  1722	 c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
  1723	 \qquad\text{for every } r \geq 4.
  1724	 \]
  1725	 Hence the class~$\mathsf{M}$ obstruction is curvature-divisible
  1726	 even when it does not vanish chainwise.
  1727	 \end{itemize}
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..7ebccfb29cf609a7de41b08e5f1ec835b516a329
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -2163,6 +2163,79 @@
 the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
 
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
+\end{remark}
+
 \section{Non-Calabi--Yau local surfaces and the Burns datum}
 \label{sec:non-cy-local-surfaces}
 \index{Burns space|textbf}


thinking
**Patching revisions**

I need to make some updates. At 1716, I'm replacing "the ordinary chain-level comparison remains open, but..." with "the naive ordinary chain-level comparison fails, but..." I’ll do the same at 1863. For Table 1899, I'll change it to `coderived equivalence; naive chain level false`. Between 1910-1912, I'm updating "open question" to "filtered-completed refinement" for class M, and for all-genera harmonic decoupling for C. The same goes for 2161-2163. I'm also considering whether to maintain line length. Let's patch these!
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1715,3 +1715,3 @@
  \textup{(}Virasoro, $\cW_N$\textup{)}:
- the ordinary chain-level comparison remains open, but the
+ the naive ordinary chain-level comparison fails, but the
  quartic and higher interaction vertices produce a harmonic
@@ -1862,3 +1862,4 @@
 class~$\mathsf{M}$ BV and bar models in the coderived category even
-though the strict chain-level comparison remains open.
+though the naive strict chain-level comparison fails on the
+uncompleted models.
 \end{remark}
@@ -1898,3 +1899,3 @@
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
+ & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
 \bottomrule
@@ -1909,5 +1910,6 @@
 resulting comparison cone is coacyclic in the sense of
-Definition~\ref{def:coacyclic-fact}. The remaining open question is
-the stronger strict chain-level comparison for class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
+Definition~\ref{def:coacyclic-fact}. The remaining open questions are
+the filtered-completed refinement for class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
 \end{remark}
@@ -2161,4 +2163,5 @@
 the coderived category is the correct ambient. What remains open is
-the stronger strict chain-level comparison in class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+the filtered-completed refinement in class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
 \end{remark}
apply_patch(auto_approved=true) exited 0 in 20ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..e4df175dbf71b9839f605a72128879eb8a36ec78
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1713,7 +1713,7 @@
  \textup{(}Remark~\textup{\ref{rem:bv-bar-class-c-proof}}\textup{)}.
  \item \emph{Class~M}
  \textup{(}Virasoro, $\cW_N$\textup{)}:
- the ordinary chain-level comparison remains open, but the
+ the naive ordinary chain-level comparison fails, but the
  quartic and higher interaction vertices produce a harmonic
  discrepancy that factors through the curvature:
  \[
@@ -1860,7 +1860,8 @@
 shows that the full harmonic discrepancy still factors through the
 curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
 class~$\mathsf{M}$ BV and bar models in the coderived category even
-though the strict chain-level comparison remains open.
+though the naive strict chain-level comparison fails on the
+uncompleted models.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1896,7 +1897,7 @@
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
  & chain-level under harmonic decoupling & composite free-field factorization \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
+ & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
 \bottomrule
 \end{tabular}
 \end{center}
@@ -1907,9 +1908,10 @@
 shows that the full harmonic discrepancy is a sum of curvature
 powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
 resulting comparison cone is coacyclic in the sense of
-Definition~\ref{def:coacyclic-fact}. The remaining open question is
-the stronger strict chain-level comparison for class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
+Definition~\ref{def:coacyclic-fact}. The remaining open questions are
+the filtered-completed refinement for class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
 \end{remark}
 
 \begin{theorem}[BV$=$bar in the coderived category;
@@ -2159,8 +2161,82 @@
 chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
 signal that the coderived category is unnecessary; it is the reason
 the coderived category is the correct ambient. What remains open is
-the stronger strict chain-level comparison in class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+the filtered-completed refinement in class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+\end{remark}
+
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..e4df175dbf71b9839f605a72128879eb8a36ec78
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1713,7 +1713,7 @@
  \textup{(}Remark~\textup{\ref{rem:bv-bar-class-c-proof}}\textup{)}.
  \item \emph{Class~M}
  \textup{(}Virasoro, $\cW_N$\textup{)}:
- the ordinary chain-level comparison remains open, but the
+ the naive ordinary chain-level comparison fails, but the
  quartic and higher interaction vertices produce a harmonic
  discrepancy that factors through the curvature:
  \[
@@ -1860,7 +1860,8 @@
 shows that the full harmonic discrepancy still factors through the
 curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
 class~$\mathsf{M}$ BV and bar models in the coderived category even
-though the strict chain-level comparison remains open.
+though the naive strict chain-level comparison fails on the
+uncompleted models.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1896,7 +1897,7 @@
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
  & chain-level under harmonic decoupling & composite free-field factorization \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
+ & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
 \bottomrule
 \end{tabular}
 \end{center}
@@ -1907,9 +1908,10 @@
 shows that the full harmonic discrepancy is a sum of curvature
 powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
 resulting comparison cone is coacyclic in the sense of
-Definition~\ref{def:coacyclic-fact}. The remaining open question is
-the stronger strict chain-level comparison for class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
+Definition~\ref{def:coacyclic-fact}. The remaining open questions are
+the filtered-completed refinement for class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
 \end{remark}
 
 \begin{theorem}[BV$=$bar in the coderived category;
@@ -2159,8 +2161,82 @@
 chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
 signal that the coderived category is unnecessary; it is the reason
 the coderived category is the correct ambient. What remains open is
-the stronger strict chain-level comparison in class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+the filtered-completed refinement in class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+\end{remark}
+
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

codex
I’ve aligned the nearby class-`M` status language. The chapter no longer says “open” where the live theorem surface says “false”; the open frontier is now the filtered-completed refinement.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1712,1916p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '2156,2240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1712	 by the three-mechanism argument
  1713	 \textup{(}Remark~\textup{\ref{rem:bv-bar-class-c-proof}}\textup{)}.
  1714	 \item \emph{Class~M}
  1715	 \textup{(}Virasoro, $\cW_N$\textup{)}:
  1716	 the naive ordinary chain-level comparison fails, but the
  1717	 quartic and higher interaction vertices produce a harmonic
  1718	 discrepancy that factors through the curvature:
  1719	 \[
  1720	 \delta_r^{\mathrm{harm}}
  1721	 \;=\;
  1722	 c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
  1723	 \qquad\text{for every } r \geq 4.
  1724	 \]
  1725	 Hence the class~$\mathsf{M}$ obstruction is curvature-divisible
  1726	 even when it does not vanish chainwise.
  1727	 \end{itemize}
  1728	\end{enumerate}
  1729	\end{proposition}
  1730	
  1731	\begin{proof}
 succeeded in 50ms:
  2156	isomorphism precisely because its cone is coacyclic.
  2157	
  2158	The upshot: the BV quantisation of the worldsheet sigma model
  2159	and the algebraic bar construction of the boundary vertex algebra
  2160	live naturally in the same curved homological framework. The
  2161	chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
  2162	signal that the coderived category is unnecessary; it is the reason
  2163	the coderived category is the correct ambient. What remains open is
  2164	the filtered-completed refinement in class~$\mathsf{M}$
  2165	\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
  2166	all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
  2167	\end{remark}
  2168	
  2169	\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
  2170	\label{rem:bv-bar-class-m-frontier}
  2171	\index{BV algebra!class M frontier|textbf}%
  2172	\index{coderived category!filtered-completed refinement}%
  2173	Theorem~\ref{thm:bv-bar-coderived} and
  2174	Proposition~\ref{prop:chain-level-three-obstructions} already isolate
  2175	the exact failure mechanism for class~$\mathsf{M}$. The quartic
 exited 1 in 51ms:

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..e4df175dbf71b9839f605a72128879eb8a36ec78
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1713,7 +1713,7 @@
  \textup{(}Remark~\textup{\ref{rem:bv-bar-class-c-proof}}\textup{)}.
  \item \emph{Class~M}
  \textup{(}Virasoro, $\cW_N$\textup{)}:
- the ordinary chain-level comparison remains open, but the
+ the naive ordinary chain-level comparison fails, but the
  quartic and higher interaction vertices produce a harmonic
  discrepancy that factors through the curvature:
  \[
@@ -1860,7 +1860,8 @@
 shows that the full harmonic discrepancy still factors through the
 curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
 class~$\mathsf{M}$ BV and bar models in the coderived category even
-though the strict chain-level comparison remains open.
+though the naive strict chain-level comparison fails on the
+uncompleted models.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1896,7 +1897,7 @@
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
  & chain-level under harmonic decoupling & composite free-field factorization \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
+ & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
 \bottomrule
 \end{tabular}
 \end{center}
@@ -1907,9 +1908,10 @@
 shows that the full harmonic discrepancy is a sum of curvature
 powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
 resulting comparison cone is coacyclic in the sense of
-Definition~\ref{def:coacyclic-fact}. The remaining open question is
-the stronger strict chain-level comparison for class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
+Definition~\ref{def:coacyclic-fact}. The remaining open questions are
+the filtered-completed refinement for class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
 \end{remark}
 
 \begin{theorem}[BV$=$bar in the coderived category;
@@ -2159,8 +2161,82 @@
 chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
 signal that the coderived category is unnecessary; it is the reason
 the coderived category is the correct ambient. What remains open is
-the stronger strict chain-level comparison in class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+the filtered-completed refinement in class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+\end{remark}
+
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}


thinking
**Evaluating status phrases**

I’m considering whether to phrase "naive chain level false" to fit the style appropriately. I think it might be helpful to run a search for open phrases again to make sure there are no contradictory statements left hanging. However, the search result may still show none except for open frontier. I’ll run the search anyway, even though I’m unsure if it’s necessary, but I want to be thorough!
exec
/bin/zsh -lc "rg -n 'chain-level open|strict chain-level comparison|ordinary chain-level comparison remains open|naive chain level false|filtered-completed refinement' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1863:though the naive strict chain-level comparison fails on the
1900: & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
1912:the filtered-completed refinement for class~$\mathsf{M}$
2164:the filtered-completed refinement in class~$\mathsf{M}$
2172:\index{coderived category!filtered-completed refinement}%
2238:passage. At present this filtered-completed refinement is the most
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..e4df175dbf71b9839f605a72128879eb8a36ec78
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1713,7 +1713,7 @@
  \textup{(}Remark~\textup{\ref{rem:bv-bar-class-c-proof}}\textup{)}.
  \item \emph{Class~M}
  \textup{(}Virasoro, $\cW_N$\textup{)}:
- the ordinary chain-level comparison remains open, but the
+ the naive ordinary chain-level comparison fails, but the
  quartic and higher interaction vertices produce a harmonic
  discrepancy that factors through the curvature:
  \[
@@ -1860,7 +1860,8 @@
 shows that the full harmonic discrepancy still factors through the
 curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
 class~$\mathsf{M}$ BV and bar models in the coderived category even
-though the strict chain-level comparison remains open.
+though the naive strict chain-level comparison fails on the
+uncompleted models.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1896,7 +1897,7 @@
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
  & chain-level under harmonic decoupling & composite free-field factorization \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
+ & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
 \bottomrule
 \end{tabular}
 \end{center}
@@ -1907,9 +1908,10 @@
 shows that the full harmonic discrepancy is a sum of curvature
 powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
 resulting comparison cone is coacyclic in the sense of
-Definition~\ref{def:coacyclic-fact}. The remaining open question is
-the stronger strict chain-level comparison for class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
+Definition~\ref{def:coacyclic-fact}. The remaining open questions are
+the filtered-completed refinement for class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
 \end{remark}
 
 \begin{theorem}[BV$=$bar in the coderived category;
@@ -2159,8 +2161,82 @@
 chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
 signal that the coderived category is unnecessary; it is the reason
 the coderived category is the correct ambient. What remains open is
-the stronger strict chain-level comparison in class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+the filtered-completed refinement in class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+\end{remark}
+
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}




thinking
**Evaluating build process**

I need to run `git diff -- chapters/connections/bv_brst.tex` to see if that’s enough. I should note the global build failure was pre-existing, and maybe I could include a line reference to an unrelated error in the final report. Only one file changed, and I should clarify that we didn't touch any other dirty files.

I want to inspect if the `main.log` file was modified by the build since we didn't edit anything, but it shows the build touched `main.log`. I might consider updating the plan to show completed steps, though it's not essential. Lastly, I could mention the theorem fortification report.
thinking
**Assessing proof status**

I'm looking at the condition status of the coderived chain for class M, which is false. My confidence is medium-high, but since the build wasn't fully completed due to an unrelated error, I need to be cautious not to overstate soundness. I could say it's "sound on the local theorem surface" rather than claiming full validation.

I want to note the edited path in [bv_brst.tex] and the added remark about the naive class-M chain being false, alongside the spectral MC5 formulation and another completed formulation. Also, I synchronized nearby status lines to clarify the class M status.
thinking
**Verifying references and errors**

I'm verifying that the label is unique and that references are resolved locally using grep. I've cleaned things up with a banned-prose sweep. However, full `latexmk` is blocked by an unrelated error in `higher_genus_complementarity.tex`. It seems to be an undefined control sequence issue.

I should mention that I didn’t touch any dirty files. For the final report, I'll keep it concise with two short sections and include a fortification report to wrap things up nicely.
codex
Added a new research remark in [chapters/connections/bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:2169) and synchronized the nearby class `M` status language. The chapter now says one consistent thing: naive strict chain-level MC5 is false for class `M`, the coderived theorem is the proved statement, and the open frontier is a filtered-completed refinement.

The new remark does four jobs: it explains the failure by the quartic non-coboundary plus the infinite shadow tower, formulates a spectral replacement using `prop:coderived-bar-degree-spectral-sequence`, formulates a completed replacement using `prop:standard-strong-filtration` and `thm:completed-bar-cobar-strong`, and isolates the strongest intermediate statement presently visible between raw chain level and bare coderived equivalence.

Local verification passed: label uniqueness, reference-surface grep, and banned-prose sweep. A full `latexmk` run was blocked by a pre-existing unrelated error in [chapters/theory/higher_genus_complementarity.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:677): undefined control sequence `\ord`.

## Fortification Report
- `thm:bv-bar-coderived`: PRIMARY PROOF `sound`; SECONDARY PROOF `written`; TECHNIQUE `primary proof by harmonic-discrepancy plus coacyclic-cone argument, secondary proof by operadic Swiss-cheese Koszul duality in rem:bv-bar-coderived-operadic; new research remark adds spectral and completed frontier lanes`; CONDITION STATUS `unconditional in D^{co}; naive strict chain-level statement false for class M; filtered-completed refinement remains open`; CONFIDENCE `medium`
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index ab620174ca3edc46292e38cd335626afb0450e38..e4df175dbf71b9839f605a72128879eb8a36ec78
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1713,7 +1713,7 @@
  \textup{(}Remark~\textup{\ref{rem:bv-bar-class-c-proof}}\textup{)}.
  \item \emph{Class~M}
  \textup{(}Virasoro, $\cW_N$\textup{)}:
- the ordinary chain-level comparison remains open, but the
+ the naive ordinary chain-level comparison fails, but the
  quartic and higher interaction vertices produce a harmonic
  discrepancy that factors through the curvature:
  \[
@@ -1860,7 +1860,8 @@
 shows that the full harmonic discrepancy still factors through the
 curvature, so Theorem~\ref{thm:bv-bar-coderived} identifies the
 class~$\mathsf{M}$ BV and bar models in the coderived category even
-though the strict chain-level comparison remains open.
+though the naive strict chain-level comparison fails on the
+uncompleted models.
 \end{remark}
 
 \begin{remark}[BV sewing at the chain level: class-by-class status;
@@ -1896,7 +1897,7 @@
 $\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
  & chain-level under harmonic decoupling & composite free-field factorization \\
 $\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
- & coderived equivalence; chain-level open & harmonic correction survives but is curvature-divisible \\
+ & coderived equivalence; naive chain level false & harmonic correction survives but is curvature-divisible \\
 \bottomrule
 \end{tabular}
 \end{center}
@@ -1907,9 +1908,10 @@
 shows that the full harmonic discrepancy is a sum of curvature
 powers, and Theorem~\ref{thm:bv-bar-coderived} proves that the
 resulting comparison cone is coacyclic in the sense of
-Definition~\ref{def:coacyclic-fact}. The remaining open question is
-the stronger strict chain-level comparison for class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
+Definition~\ref{def:coacyclic-fact}. The remaining open questions are
+the filtered-completed refinement for class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling verification for class~$\mathsf{C}$.
 \end{remark}
 
 \begin{theorem}[BV$=$bar in the coderived category;
@@ -2159,8 +2161,82 @@
 chain-level discrepancy for class~$\mathsf{M}$ is therefore not a
 signal that the coderived category is unnecessary; it is the reason
 the coderived category is the correct ambient. What remains open is
-the stronger strict chain-level comparison in class~$\mathsf{M}$ and
-the all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+the filtered-completed refinement in class~$\mathsf{M}$
+\textup{(}Remark~\ref{rem:bv-bar-class-m-frontier}\textup{)} and the
+all-genera harmonic-decoupling statement in class~$\mathsf{C}$.
+\end{remark}
+
+\begin{remark}[Research direction: class~$\mathsf{M}$ between coderived and chain level]
+\label{rem:bv-bar-class-m-frontier}
+\index{BV algebra!class M frontier|textbf}%
+\index{coderived category!filtered-completed refinement}%
+Theorem~\ref{thm:bv-bar-coderived} and
+Proposition~\ref{prop:chain-level-three-obstructions} already isolate
+the exact failure mechanism for class~$\mathsf{M}$. The quartic
+harmonic discrepancy is not a coboundary in the ordinary chain
+complex, and the higher discrepancies satisfy
+\[
+\delta_r^{\mathrm{harm}}
+\;=\;
+c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
+\qquad (r \geq 4).
+\]
+For Virasoro and principal $\cW_N$,
+Corollary~\ref{cor:virasoro-postnikov-nontermination} shows that the
+shadow obstruction tower does not terminate. The naive chain-level
+form of Conjecture~\ref{conj:v1-master-bv-brst} is therefore false in
+class~$\mathsf{M}$ on the explicit uncompleted models: one is not
+facing a single quartic defect, but an infinite family of nonvanishing
+higher corrections regenerated by the permanent cubic source.
+
+A spectral replacement is still plausible. Filter the comparison cone
+$K_g = \operatorname{cone}(f_g)$ by bar degree, total conformal
+weight, or any compatible shadow-window filtration.
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence} then
+supplies a coderived spectral sequence whose $E_1$ page is computed
+from the strict associated-graded differential, because the curvature
+lies in positive filtration. For class~$\mathsf{M}$, each finite
+window sees only finitely many operations, so the associated-graded
+comparison is a finite problem. The research target is a spectral form
+of MC5: construct a class~$\mathsf{M}$ filtration for which the
+higher differentials record exactly the harmonic classes
+$c_r(\cA)$ and the spectral sequence converges to a coacyclic cone.
+This would replace a false strict chain identity by a filtered
+comparison that measures the failure page by page.
+
+The best chain-level statement is likely completed rather than strict.
+Proposition~\ref{prop:standard-strong-filtration} and
+Theorem~\ref{thm:completed-bar-cobar-strong} show that the standard
+class~$\mathsf{M}$ families already carry the weight-completion
+package on the bar side. Since the full Maurer--Cartan class satisfies
+$\Theta_\cA = \varprojlim_r \Theta_\cA^{\le r}$ in the completed
+convolution algebra, the correct BV analogue should also live in a
+completion. One should therefore seek a continuous comparison
+\[
+\widehat f_g \colon
+\widehat C^{\bullet}_{\mathrm{BV}}(\cA,\Sigma_g)
+\longrightarrow
+\widehat B^{(g)}(\cA),
+\]
+where the hats denote compatible inverse limits of finite shadow or
+weight truncations. The conjectural assertion is not that the raw
+direct-sum complexes are quasi-isomorphic, but that every finite
+quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
+inverse limit is continuous. This is the strongest chain-level
+statement presently visible for class~$\mathsf{M}$.
+
+Between ordinary chain level and bare coderived equivalence lies a
+stronger filtered-completed statement. One can ask that
+$\widehat f_g$ be a weak equivalence of filtered curved models in the
+sense of Definition~\ref{def:curved-weak-equiv}, or equivalently an
+isomorphism already in the provisional coderived category of
+Definition~\ref{def:provisional-coderived}. This is stronger than
+Theorem~\ref{thm:bv-bar-coderived}, because it remembers the
+filtration and every finite truncation; it is weaker than an ordinary
+chain-level quasi-isomorphism, because it allows the infinite residual
+class~$\mathsf{M}$ discrepancy to die only after filtered coderived
+passage. At present this filtered-completed refinement is the most
+plausible strengthening of the coderived theorem.
 \end{remark}
 
 \section{Non-Calabi--Yau local surfaces and the Burns datum}

tokens used
393,735
