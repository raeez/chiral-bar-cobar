# F09_prerequisites_thm_H (678s)

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:145-156 — PROBLEM: This file defines `C^n_{\text{chiral}}(\mathcal A)` as global sections on `\overline C_{n+2}(X)`, but the canonical Hochschild source already says this chapter should cite its definitions from `chapters/theory/hochschild_cohomology.tex:42-64,76-83,469-489`, and `chapters/theory/koszul_pair_structure.tex:259-295` gives yet another `A^e`/bar-resolution model. No comparison theorem is supplied, so “the chiral Hochschild complex” is ambiguous on the theorem-H surface. FIX: Delete the local redefinition at 145-156 and replace it by a citation to the canonical definition (`\ref{def:chiral-hochschild-derived}` or `\ref{thm:geometric-chiral-hochschild}`), then insert one explicit comparison proposition proving the model used here is quasi-isomorphic to that canonical model.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:145-149,362-372 — PROBLEM: The stated spectral sequence needs independent indices `(bar degree, sheaf-cohomology degree)`, but the local cochain definition hardwires degree `n` to `\Omega^n`, and the proof later invents `\ChirHoch^{m,*}` and a vertical `d_{\mathrm{sheaf}}` that were never defined. There is no actual bicomplex. FIX: Redefine the complex as either `C^{p,\bullet}_{\mathrm ch}(\mathcal A):=R\Gamma(\overline C_{p+2}(X),\mathcal F_p)` with `\mathcal F_p=j_*j^*\mathcal A^{\boxtimes(p+2)}\otimes\Omega^p_{\log}`, or as a genuine `C^{p,q}` bicomplex with explicit bidegrees and differentials; then restate Theorem `thm:hochschild-spectral-sequence` in that repaired model.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:324-358 — PROBLEM: `thm:hochschild-bar-cobar` does not prove what it claims. Step 3 says `\mathrm{Ext}^n_{\mathrm{ChirAlg}}(\mathcal A,\mathcal A)=\ChirHoch^n(\mathcal A)` “by definition,” but the loaded definitions in the files actually read define chiral Hochschild cohomology as `RHom_{\mathcal D_X}(\barBgeom(\mathcal A),M)` or `\mathrm{Ext}_{\mathcal A^e}`. FIX: Either insert a proved comparison theorem identifying `RHom_{\mathrm{ChirAlg}}(\Omega^{\mathrm ch}\bar B^{\mathrm ch}(\mathcal A),\mathcal A)` with the canonical Hochschild complex, or downgrade 324-358 from `\ClaimStatusProvedHere` to a remark/conjecture.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:583-585,623-635 — PROBLEM: Theorem H is stated for a single “chiral Koszul datum” via `def:chiral-koszul-morphism`, but the proof immediately uses Verdier-compatible identifications that only exist for a full chiral Koszul pair from `def:chiral-koszul-pair`. The statement is stronger than the proof. FIX: Change the theorem hypothesis to `Let (\cA,\cA^!) be a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair})`, or insert a prior proposition constructing such a pair from the stated datum and proving the needed Verdier compatibility.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:538-574 — PROBLEM: `lem:chirhoch-descent` is the linchpin of the first proof, but its proof never establishes `\ChirHoch^\bullet(\cA)\cong(\mathbb D_{\Ran}\bar B^{\mathrm ch}(\cA))_\Sigma`. The cited Theorem A (`chapters/theory/chiral_koszul_pairs.tex:3638-3685`) identifies `\mathbb D_{\Ran}\bar B_X(\cA_1)` with the opposite algebra in a Koszul pair, not with Hochschild self-Ext. FIX: Remove this lemma from the proof chain and replace it with a separate comparison theorem from the canonical Hochschild definition to the Verdier-dual bar model.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:497-500,599-603 — PROBLEM: The proof says bar concentration forces the surviving diagonal `p=q`, but the cited theorem says `H^{p,q}(\bar B^{\mathrm ch}(\cA_1))=0` for `q\neq 0` (`chapters/theory/chiral_koszul_pairs.tex:1120-1128`). That is the `q=0` axis, not the diagonal. FIX: Replace every `p=q` claim in the theorem-H lane by `q=0`, then redo the degree bookkeeping with total degree `p+q`.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:362-372,751-767 — PROBLEM: The file advertises a spectral-sequence route to Theorem H, but the actual `{0,1,2}` concentration proof never uses `thm:hochschild-spectral-sequence`; it is proved instead from negative `Ext` vanishing plus the already-established duality theorem. FIX: Either repair the spectral sequence and derive concentration from it, or rewrite the chapter so it no longer claims the spectral sequence is what proves concentration.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:596-604,778-785 — PROBLEM: `\ChirHoch^n(\cA)` is treated as a vector-space-valued cohomology theory throughout the file, but Theorem H tensors it with the line bundle `\omega_X`, and line 778 then treats that bundle as dimension-neutral. The object type changes mid-proof. FIX: Choose one model. If `\ChirHoch^n` is a complex of vector spaces, replace `\otimes\omega_X` by a one-dimensional dualizing vector space after taking global sections. If it is a `\mathcal D_X`-module, restate the theorem in that category and stop taking plain dimensions without applying `R\Gamma` or a fiber functor.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:674-691 — PROBLEM: The second proof invokes `thm:e1-module-koszul-duality`, but the source file explicitly says its extension to arbitrary chiral Koszul pairs is not proved (`chapters/theory/chiral_koszul_pairs.tex:5160-5169,5174-5188`). This proof uses it outside its proved scope. FIX: Delete the second proof, or rewrite it as a separately scoped proposition restricted to the complete/conilpotent `E_1` lane.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:4598-4718 — PROBLEM: The file reopens the theorem-H surface with a second incompatible setup: first `\mathrm{Hom}_{\mathsf{Alg}}(\Omega\bar B(\mathcal A),\mathcal A)`, then `\mathrm{Hom}_{\mathcal A^e}(\mathcal A^{\otimes n+2},\mathcal A)`, then a configuration-space formula with `\mathcal H om_{\mathcal D_X}`. None are compared to the earlier model. FIX: Delete 4598-4718 and replace it with cross-references to the canonical theorem surfaces, or add explicit comparison propositions and keep only one definition after those comparisons.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:716-729,742-747 — PROBLEM: The growth theorem takes `\dim Z(\cA)`, `\dim \ChirHoch^1(\cA)`, and a Hilbert series without assuming those spaces are finite-dimensional, then says the palindromic identity holds “unconditionally” even though it is derived from Theorem H on the quadratic Koszul locus. FIX: Add a finite-dimensionality hypothesis or reformulate the theorem in a Grothendieck/completed-character setting, and replace “unconditionally” by “under the hypotheses of Theorem~\ref{thm:main-koszul-hoch}”.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:282-289 — PROBLEM: The proof of `\{d_{\mathrm{fact}},d_{\mathrm{config}}\}=0` silently switches from logarithmic forms to a boundary-supported current identity for `d_{\mathrm{dR}}\eta_{12}` without defining a current model on `\overline C_{n+2}(X)` or proving the Stokes/residue formula it uses. FIX: Either work explicitly in currents and prove that boundary identity before invoking it, or remove this argument and build the vertical direction from derived global sections instead of `d_{\mathrm{dR}}`.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:642-646 — PROBLEM: The first proof assumes, without imported justification, that each bar summand is a perfect `\Sigma_n`-equivariant `\mathcal D`-module and that Verdier duality commutes with finite `\Sigma_n`-coinvariants. Those are hidden hypotheses, not proved inputs. FIX: Add a lemma proving holonomicity/perfection of the relevant bar summands and the duality/coinvariants interchange, or add them as explicit hypotheses to Theorem H.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:577-605,701-703 — PROBLEM: This file labels two local statements as “Theorem H”, but the concordance fixes Theorem H to `thm:w-algebra-hochschild`, `thm:virasoro-hochschild`, `thm:critical-level-cohomology`, and `prop:chirhoch1-affine-km` (`chapters/connections/concordance.tex:64-71`). The theorem surface is drifting. FIX: Either update the concordance so `thm:main-koszul-hoch` and `thm:hochschild-polynomial-growth` become the canonical theorem-H anchors, or stop calling these local statements “Theorem H”.

## Summary
Checked: 14 | Findings: 14 | Verdict: FAIL


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
session id: 019d83e2-7ffa-7b90-83f5-b403634f7122
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


MISSION: FOUNDATION AUDIT of chapters/theory/chiral_hochschild_koszul.tex

For Theorem H: trace every input. Is the bar-Hochschild complex properly defined? Is the spectral sequence from bar degree to Hochschild degree set up? Is concentration in {0,1,2} proved from the spectral sequence?

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers


thinking
**Auditing a specific file**

I need to conduct an audit of a specific file while following instructions from the agents. I'll be reading files like CLAUDE, theorem_registry, and others. It seems I'll likely use skills such as deep-beilinson-audit and maybe claim-surface-sync since the user asked about auditing theorem proof. I should probably spawn an explorer for context and ensure I'm announcing the skills used. I'll need to send a commentary update frequently and gather the necessary context from the agents.
thinking
**Planning theorem audit**

I need to run some checks around theorem H, focusing on the exact theorem, definitions, spectral sequences, and the bar-Hochschild complex. The user wants specific lines, so I need to be thorough in my findings document, possibly using the build-surface skill if necessary. I might also need to look at unresolved references and check logs. Since the focus is on the file contents, a targeted build could help. I’ll ensure to start with a commentary update mentioning my use of deep-beilinson-audit and initial reading materials.
codex
Auditing `chapters/theory/chiral_hochschild_koszul.tex` as a hostile proof surface. I’m starting with the required constitutional reads, then I’ll trace Theorem H’s local dependency chain and test whether the bar-Hochschild complex, spectral sequence, and `{0,1,2}` concentration are actually proved.
exec
/bin/zsh -lc "sed -n '1,240p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,240p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

codex
Using `deep-beilinson-audit` for this pass. I’ve loaded the required constitutional surfaces; next I’m locating Theorem H’s exact claim blocks, every local dependency it cites, and the places where the bar-Hochschild complex and spectral sequence are actually defined.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '261,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Theorem H|thm:w-algebra-hochschild|thm:virasoro-hochschild|thm:critical-level-cohomology|prop:chirhoch1-affine-km|ChirHoch|bar-Hochschild|spectral sequence|Hochschild degree|bar degree" chapters/theory/chiral_hochschild_koszul.tex' in /Users/raeez/chiral-bar-cobar succeeded in 152ms:
12:complex $\ChirHoch^*(\cA)$ is that tangent complex;
16:$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
21:refinement of $\ChirHoch^*(\cA)$.
136:$\ChirHoch^n(\cA)\cong \ChirHoch^{2-n}(\cA^!)^\vee\otimes\omega_X$
357:The left side is precisely $\ChirHoch^n(\mathcal{A})$ by definition.
360:\subsection{The spectral sequence}
362:\begin{theorem}[Hochschild spectral sequence; \ClaimStatusProvedHere]\label{thm:hochschild-spectral-sequence}
363:There exists a spectral sequence
365:E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes (n+2)} \otimes \Omega^n_{\log}) \Rightarrow \ChirHoch^{n+q}(\mathcal{A})
367:where $n$ is the bar degree (number of internal insertions) and $q$ is the sheaf cohomology degree, which are independent indices.
371:The chiral Hochschild complex $\ChirHoch^*(\mathcal{A})$ is a double complex with horizontal differential $d_{\mathrm{bar}}$ (the bar differential of Definition~\ref{def:bar-differential-complete}) and vertical differential $d_{\mathrm{sheaf}}$ (sheaf cohomology on configuration spaces). Filter by bar degree: $F^n = \bigoplus_{m \geq n} \ChirHoch^{m,*}$. The resulting spectral sequence has $E_0^{n,q} = \Gamma(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$ with $d_0 = d_{\mathrm{sheaf}}$, so $E_1^{n,q} = H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes(n+2)} \otimes \Omega^n_{\log})$. Convergence follows from the bounded-below hypothesis on $\mathcal{A}$ and the finite cohomological dimension of configuration spaces.
374:For the cyclic refinement relating Hochschild to cyclic homology via Connes' operator, see Theorem~\ref{thm:HC-spectral-sequence}. For formal chiral algebras (quasi-isomorphic to their cohomology), the spectral sequence above degenerates at $E_1$, giving:
376:\ChirHoch^k(\mathcal{A}) \cong \bigoplus_{n+q=k} H^q(\overline{C}_{n+2}(X), \mathcal{A}^{\boxtimes (n+2)} \otimes \Omega^n_{\log})
485:collapses to a uniform constant. More precisely, at bar degree~$p$
508:At bar degree~$p$, the Hochschild complex lives on the smooth proper
521:bar degree~$p$ is $(p+2) - p = 2$.
527:diagonal, bar degree~$p$ and cohomological degree~$q = 0$ give
541:The chiral Hochschild complex $\ChirHoch^{\bullet}(\cA)$ arises as
549:\ChirHoch^{\bullet}(\cA)
554:bar degree~$n$.
 succeeded in 181ms:
     1	\chapter{Chiral Hochschild cohomology and Koszul duality}
     2	\label{chap:deformation-theory}
     3	
     4	\index{deformation theory!chiral|textbf}
     5	\index{Hochschild cohomology!chiral|textbf}
     6	
     7	The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
     8	Koszul duality, but how rigid is the moduli it lives in? Without
     9	knowing the tangent complex to
    10	$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
    11	bulk-field coupling remains inaccessible. The chiral Hochschild
    12	complex $\ChirHoch^*(\cA)$ is that tangent complex;
    13	Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
    14	Koszul locus, so the MC moduli has cohomological
    15	amplitude~$[0,2]$, and the Koszul duality
    16	$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
    17	is Verdier duality on this tangent space.
    18	
    19	The cyclic deformation complex $\Defcyc(\cA)$
    20	(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic
 succeeded in 163ms:
   261	with three points $z_1, z_2, z_3$), the two compositions act
   262	as:
   263	\begin{align*}
   264	(d_{\text{config}} \circ d_{\text{fact}})(\phi)
   265	&= d_{\mathrm{dR}}\Bigl(
   266	 \mathrm{Res}_{z_1 = z_2}\bigl[a_1 a_2 \otimes a_3
   267	 \otimes \eta_{12}\bigr] \Bigr), \\
   268	(d_{\text{fact}} \circ d_{\text{config}})(\phi)
   269	&= \sum_{i<j}
   270	 \mathrm{Res}_{z_i = z_j}\bigl[a_1 \otimes a_2 \otimes a_3
   271	 \otimes d_{\mathrm{dR}}\eta_{12}\bigr].
   272	\end{align*}
   273	
   274	The key identity is Arnold's relation
   275	\cite{Arnold69}: for the logarithmic 1-forms
   276	$\eta_{ij} = d\log(z_i - z_j)$ on $C_3(X)$,
   277	\begin{equation}\label{eq:arnold-three-point}
   278	\eta_{12} \wedge \eta_{23}
   279	+ \eta_{23} \wedge \eta_{31}
   280	+ \eta_{31} \wedge \eta_{12} = 0.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '521,860p'" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
   521	bar degree~$p$ is $(p+2) - p = 2$.
   522	
   523	It remains to see that this uniform value persists after passing to
   524	cohomology. By Theorem~\ref{thm:bar-concentration}, the bar
   525	cohomology $H^{p,q}(\barB^{\mathrm{ch}}(\cA))$ vanishes for
   526	$q \neq 0$; only the $q = 0$ diagonal contributes. On this
   527	diagonal, bar degree~$p$ and cohomological degree~$q = 0$ give
   528	total degree~$p + 0 = p$ in the source and $p + 2$ in the target
   529	(after the Verdier shift). The difference $2$ is independent of~$p$,
   530	confirming the uniform shift.
   531	
   532	The $\omega_X$ factor: Serre duality on the one-dimensional base
   533	curve~$X$ contributes $\omega_X = \Omega^1_X$ as the dualizing sheaf.
   534	This twist is intrinsic to $\mathcal{D}$-module duality on~$X$ and
   535	independent of the configuration-space geometry.
   536	\end{proof}
   537	
   538	\begin{lemma}[Chiral Hochschild descent; \ClaimStatusProvedHere]
   539	\label{lem:chirhoch-descent}
   540	\index{chiral Hochschild!descent from bar}


thinking
**Reviewing foundation audit tasks**

The file is huge, and the user wants a focused audit on theorem H, tracing every input. I need to audit definitions, spectral sequences, and concentration proofs with precise file and line references. I should check cited dependencies like the bigraded Hochschild definition and various theorems. I’ll use tools like `rg` across the repository to locate labels and ensure proofs are justified. I might also run a latex build to catch any undefined references. The user wants a thorough audit, so I need to inspect all relevant definitions and theorem labels, ensuring nothing is overlooked.
thinking
**Checking for status mismatches**

I’m considering whether there might be a status mismatch with concordance regarding Theorem H. The content in this file differs from what's in concordance, so I really need to check. It could be important to find out if this file overclaims or has discrepancies. I should inspect the local references list and the theorem registry to see if theorem H is linked properly. Using `rg`, I’ll locate label definitions, especially around def:bigraded-hochschild, possibly near line 1930, to clarify these potential mismatches.
codex
The local theorem surface is already showing pressure points: multiple definitions are being used interchangeably, and the spectral-sequence proof is far thinner than the claim it supports. I’m now tracing every imported label in the theorem-H lane and checking whether the file’s internal definitions actually match the proof language.
exec
/bin/zsh -lc "rg -n \"label\\{(def:bigraded-hochschild|thm:bar-concentration|def:bar-differential-complete|thm:arnold-relations|def:chiral-koszul-morphism|def:chiral-koszul-pair|thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:kodaira-spencer-chiral-complete|lem:verdier-involution-moduli|thm:e1-module-koszul-duality|rem:nc-hodge-degeneration)\\}\" -g '*.tex'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\ref\\{(def:bigraded-hochschild|thm:bar-concentration|def:bar-differential-complete|thm:arnold-relations|def:chiral-koszul-morphism|def:chiral-koszul-pair|thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:kodaira-spencer-chiral-complete|lem:verdier-involution-moduli|thm:e1-module-koszul-duality|rem:nc-hodge-degeneration)\\}\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(def:bigraded-hochschild|def:chiral-koszul-morphism|def:chiral-koszul-pair|thm:bar-concentration|thm:bar-cobar-isomorphism-main|thm:higher-genus-inversion|thm:kodaira-spencer-chiral-complete|lem:verdier-involution-moduli|thm:e1-module-koszul-duality|def:bar-differential-complete|thm:arnold-relations|conv:regime-tags|def:cyclic-deformation-elementary|def:modular-cyclic-deformation-complex|rem:modular-cyc-strictification|thm:operadic-homotopy-convolution|thm:chiral-deligne-tamarkin|def:thqg-chiral-derived-center|sec:thqg-open-closed-realization|thm:mc2-bar-intrinsic|thm:thqg-annulus-trace|conv:higher-genus-differentials|rem:nc-hodge-degeneration)\\}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex chapters/examples/*.tex chapters/connections/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:2673:\label{def:bigraded-hochschild}
chapters/theory/chiral_koszul_pairs.tex:252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
chapters/theory/chiral_koszul_pairs.tex:625:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
chapters/theory/chiral_koszul_pairs.tex:1113:\label{thm:bar-concentration}
chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
chapters/theory/chiral_koszul_pairs.tex:5176:\label{thm:e1-module-koszul-duality}
chapters/theory/bar_construction.tex:501:\begin{definition}[Bar differential]\label{def:bar-differential-complete}%
chapters/theory/chiral_hochschild_koszul.tex:5011:\begin{remark}[Noncommutative Hodge degeneration]\label{rem:nc-hodge-degeneration}
chapters/theory/configuration_spaces.tex:733:\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-relations}
chapters/theory/higher_genus_complementarity.tex:1258:\label{thm:kodaira-spencer-chiral-complete}
chapters/theory/higher_genus_complementarity.tex:1447:\label{lem:verdier-involution-moduli}
chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
standalone/N1_koszul_meta.tex:365:\label{def:chiral-koszul-morphism}
 exited 1 in 51ms:

 succeeded in 52ms:
chapters/theory/chiral_hochschild_koszul.tex:1424:\label{def:cyclic-deformation-elementary}
chapters/theory/chiral_hochschild_koszul.tex:1832:\label{def:modular-cyclic-deformation-complex}
chapters/theory/chiral_hochschild_koszul.tex:1874:\label{rem:modular-cyc-strictification}
chapters/theory/chiral_hochschild_koszul.tex:5011:\begin{remark}[Noncommutative Hodge degeneration]\label{rem:nc-hodge-degeneration}
chapters/theory/higher_genus_modular_koszul.tex:3499:\label{thm:mc2-bar-intrinsic}
chapters/connections/thqg_open_closed_realization.tex:14:\label{sec:thqg-open-closed-realization}
chapters/connections/thqg_open_closed_realization.tex:290:\label{def:thqg-chiral-derived-center}
chapters/connections/thqg_open_closed_realization.tex:633:\label{thm:thqg-annulus-trace}
chapters/theory/higher_genus_complementarity.tex:1258:\label{thm:kodaira-spencer-chiral-complete}
chapters/theory/higher_genus_complementarity.tex:1447:\label{lem:verdier-involution-moduli}
chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
chapters/theory/chiral_hochschild_koszul.tex:1424:\label{def:cyclic-deformation-elementary}
chapters/theory/chiral_hochschild_koszul.tex:1832:\label{def:modular-cyclic-deformation-complex}
chapters/theory/chiral_hochschild_koszul.tex:1874:\label{rem:modular-cyc-strictification}
chapters/theory/chiral_hochschild_koszul.tex:5011:\begin{remark}[Noncommutative Hodge degeneration]\label{rem:nc-hodge-degeneration}
chapters/theory/chiral_center_theorem.tex:1300:\label{thm:chiral-deligne-tamarkin}
chapters/theory/higher_genus_foundations.tex:229:\begin{convention}[Higher-genus differentials]\label{conv:higher-genus-differentials}
chapters/theory/higher_genus_foundations.tex:2673:\label{def:bigraded-hochschild}
chapters/theory/chiral_koszul_pairs.tex:252:\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
chapters/theory/chiral_koszul_pairs.tex:625:\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
codex
I’ve identified the imported labels that actually carry the theorem-H proof burden. Next step is to read those exact source blocks in context, because several proof lines are currently leaning on labels whose statements may not say what this chapter needs them to say.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '240,340p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '610,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2650,2735p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '470,560p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1090,1165p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/configuration_spaces.tex | sed -n '720,790p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   240	coproduct. The MC equation $d\tau + \tau \star \tau = 0$ is
   241	\emph{equivalent} to $(d_\cA + d_\cC + d_\tau^L)^2 = 0$
   242	\textup{(}cf.\ \cite[Lemma~2.1.4]{LV12}\textup{)}: the twisting
   243	morphism condition is the nilpotence of the twisted differential.
   244	In the chiral setting, $\tau(c_{(1)})$ is the OPE extraction:
   245	the coproduct $\Delta(c) = \sum c_{(1)} \otimes c_{(2)}$ separates
   246	the coalgebra element, and $\tau$ evaluates $c_{(1)}$ against the
   247	propagator on~$\overline{C}_2(X)$ by residue at the collision
   248	divisor
   249	\textup{(}Proposition~\textup{\ref{prop:twisting-morphism-propagator})}.
   250	\end{remark}
   251	
   252	\begin{definition}[Chiral Koszul morphism]\label{def:chiral-koszul-morphism}
   253	\index{Koszul morphism!chiral|textbf}
   254	A chiral twisting datum $(\cA, \cC, \tau, F_\bullet)$ is
   255	\emph{Koszul} if:
   256	\begin{enumerate}
   257	\item both $K_\tau^L(\cA,\cC)$ and $K_\tau^R(\cC,\cA)$ are acyclic;
   258	\item the associated graded
   259	 $(\operatorname{gr}\cA, \operatorname{gr}\cC, \operatorname{gr}\tau)$
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '5160,5218p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '3610,3688p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   610	
   611	This is the chiral analogue of \textup{\cite[Theorem~2.4.1]{LV12}}.
   612	The proof transfers directly: filter both sides by bar degree, observe
   613	that $\mathrm{gr}(f)$ is an isomorphism (since $f$ is a quasi-isomorphism
   614	of coalgebras), and conclude by spectral sequence comparison.
   615	\end{theorem}
   616	
   617	\subsection{The concept of chiral Koszul pairs: precise formulation}
   618	
   619	To handle non-quadratic examples, we extend the notion of Koszul pairs
   620	beyond the quadratic setting. The defining property is a set of
   621	\emph{recognition criteria} (checkable conditions on the pair) from
   622	which the full bar-cobar identification follows as a theorem.
   623	No quasi-isomorphism statement is built into the definition itself.
   624	
   625	\begin{definition}[Chiral Koszul pair]\label{def:chiral-koszul-pair}
   626	\index{Koszul pair!chiral|textbf}
   627	A \emph{chiral Koszul pair} on a smooth projective curve~$X$
   628	is a pair of chiral Koszul data
   629	\textup{(}Definition~\textup{\ref{def:chiral-twisting-datum}},
 succeeded in 52ms:
  1090	Lie algebra $\fg_{<0} = \fg \otimes t^{-1}\bC[t^{-1}]$
  1091	and the chiral bar cohomology $H^*(\barBgeom(\cA))$ give
  1092	\emph{different} Betti sequences, though both compute from
  1093	the same underlying OPE data.
  1094	For the Witt algebra $\mathrm{Witt} = \mathrm{Der}(\bC((t)))$,
  1095	the negative-mode Lie algebra is the Lie algebra of
  1096	polynomial vector fields vanishing to order~$\geq 2$
  1097	at the origin, and its CE cohomology has
  1098	$\dim H^1_{\mathrm{CE}}(\mathrm{Witt}_{<0}) = 3$
  1099	(the three independent cocycles $L_{-1}^*, L_{-2}^*, L_{-3}^*$
  1100	on $\mathrm{span}\{L_{-1}, L_{-2}, L_{-3}\}$).
  1101	The chiral bar cohomology of the Virasoro algebra has
  1102	$\dim H^1(\barBgeom(\mathrm{Vir})) = 1$
  1103	(a single generator~$T$ of conformal weight~$2$).
  1104	The discrepancy $3 - 1 = 2$ quantifies the
  1105	Orlik--Solomon form contribution: the chiral bar differential
  1106	uses the full logarithmic residue $d\log(z_1 - z_2)$
  1107	(the Arnold relation on configuration space),
  1108	which collapses the three CE cocycles to the single
  1109	chiral primary.
 succeeded in 62ms:
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
  3620	of weight~$2$ and $g_r = p(r+1) - p(r)$ for all $r \geq 1$,
  3621	giving primitive defect $\Delta^{\mathrm{prim}}_{\mathrm{Vir}}(t)
  3622	= G_{\mathrm{Vir}}(t) - t$, which is nonzero starting at
  3623	$t^3$. This nonvanishing defect is the kinematic signature of
  3624	nonquadraticity and feeds directly into the MC4 completion
  3625	programme
  3626	(\S\textup{\ref{subsec:shadow-postnikov-tower}}).
  3627	\end{remark}
  3628	
  3629	\subsection{Geometric bar-cobar duality (Theorem~A)}
 succeeded in 98ms:
  2650	For a chiral Koszul pair $(\mathcal{A}, \mathcal{A}^!)$ on a smooth projective curve~$X$,
  2651	chiral Hochschild cohomology satisfies:
  2652	\begin{equation}\label{eq:hochschild-duality-canonical}
  2653	RHH_{\mathrm{chiral}}(\mathcal{A})
  2654	\;\simeq\;
  2655	R\mathrm{Hom}\bigl(RHH_{\mathrm{chiral}}(\mathcal{A}^!),\,
  2656	\omega_X[2]\bigr).
  2657	\end{equation}
  2658	On cohomology, the $[2]$-shift becomes degree reflection:
  2659	\begin{equation}\label{eq:hochschild-duality-groups}
  2660	\ChirHoch^n(\mathcal{A})
  2661	\;\cong\; \ChirHoch^{2-n}(\mathcal{A}^!)^{\vee}
  2662	\otimes \omega_X.
  2663	\end{equation}
  2664	\end{corollary}
  2665	
  2666	\begin{proof}
  2667	This is Theorem~\ref{thm:main-koszul-hoch} (Theorem~H), proved
  2668	independently in \S\ref{subsec:hochschild-duality} via
  2669	the bar-cobar quasi-isomorphism and Verdier duality on the Ran space.
 succeeded in 95ms:
   470	For $\mathbb{P}^1$, $\dim H^0(\overline{C}_2, \Omega^1(\log D)) = 1$ (only constant coefficient functions after fixing $\text{PSL}_2$).
   471	
   472	Hence $\dim \bar{B}^{(0),1}(\mathcal{A}) = N^2$.
   473	\end{example}
   474	
   475	\begin{example}[Genus zero, degree 2]\label{ex:bar-genus0-deg2}
   476	At genus 0, degree 2:
   477	\[\bar{B}^{(0),2}(\mathcal{A}) = \Gamma\left(\overline{C}_3(\mathbb{P}^1), j_*j^*(\mathcal{A}^{\boxtimes 3}) \otimes \Omega^2(\log D)\right)\]
   478	
   479	\emph{Configuration space.} $\overline{C}_3(\mathbb{P}^1)$ has $\dim_\mathbb{C} = 3$. Fixing the $\text{PSL}_2$ gauge (e.g., $z_3 = 0, z_2 = 1, z_1 = \infty$ for the normalization), the quotient $\overline{C}_3(\mathbb{P}^1)/\text{PSL}_2 \cong \overline{\mathcal{M}}_{0,4} \cong \mathbb{P}^1$ has $\dim_\mathbb{C} = 1$. The $\text{PSL}_2$-reduced configuration has one free cross-ratio parameter.
   480	
   481	\emph{Boundary divisor.} $D = D_{12} \cup D_{23} \cup D_{13}$ (three divisors, one for each pair of points colliding).
   482	
   483	\emph{Logarithmic 2-forms.} $\Omega^2(\log D)$ is spanned by:
   484	\[\eta_{12} \wedge \eta_{23}, \quad \eta_{23} \wedge \eta_{31}, \quad \eta_{31} \wedge \eta_{12}\]
   485	subject to Arnold relation:
   486	\[\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} = 0\]
   487	
   488	So the space of 2-forms is 2-dimensional (three generators, one relation).
   489	
 succeeded in 64ms:
   720	Therefore:
   721	\[d\omega = \frac{df}{f} \wedge d\alpha + d\beta\]
   722	
   723	Since $d\alpha$ and $d\beta$ are smooth, this is again a logarithmic form.
   724	
   725	\emph{Part 2: $d^2 = 0$.}
   726	This is the fundamental property of the de Rham differential, independent of logarithmic conditions.
   727	
   728	\emph{Part 3: Cohomology.}
   729	By the logarithmic Poincar\'{e} lemma (Deligne~\cite{Deligne71}), the logarithmic de~Rham complex $\Omega^\bullet(\log D)$ on $\overline{C}_n(\Sigma_g)$ computes the cohomology of the \emph{open} complement $\overline{C}_n(\Sigma_g) \setminus D = C_n(\Sigma_g)$:
   730	\[H^*(\overline{C}_n(\Sigma_g),\, \Omega^\bullet(\log D)) \cong H^*(C_n(\Sigma_g);\, \mathbb{C})\]
   731	\end{proof}
   732	
   733	\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-relations}
   734	\index{Arnold relations|textbf}
   735	\index{propagator!logarithmic|textbf}
   736	In the Heisenberg bar complex (\S\ref{sec:frame-bar-deg2}), the identity $d^2 = 0$ at degree~$2$ reduced to the three-term relation $\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} = 0$. We recognized it as the Arnold relation; here we develop it systematically.
   737	
   738	The logarithmic 1-forms $\eta_{ij} = d\log(z_i - z_j)$ satisfy fundamental relations:
   739	
 succeeded in 66ms:
  5160	is \emph{not} proved on this general surface. The earlier bar-cobar
  5161	machinery in Part~\ref{part:bar-complex} gives the intrinsic bar-coalgebra comparison, and
  5162	the manuscript's proved ordinary module-level statement is the later
  5163	$\Eone$ theorem
  5164	Theorem~\ref{thm:e1-module-koszul-duality}, restricted to the
  5165	quadratic genus-$0$ complete/conilpotent lane.
  5166	
  5167	Any extension of that package to arbitrary chiral Koszul pairs would
  5168	require extra hypotheses and a module-level comparison theorem beyond
  5169	what is currently established here.
  5170	\end{remark}
  5171	
  5172	\subsection{\texorpdfstring{$\Eone$-chiral module category Koszul duality}{E1-chiral module category Koszul duality}}
  5173	
  5174	\begin{theorem}[\texorpdfstring{$\Eone$}{E1}-module category Koszul duality;
  5175	\ClaimStatusProvedHere]
  5176	\label{thm:e1-module-koszul-duality}
  5177	\index{module Koszul duality|textbf}
  5178	Let $\mathcal{A}$ be a Koszul $\Eone$-chiral algebra with Koszul
  5179	dual bar coalgebra
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4990,5055p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  4990	
  4991	\begin{remark}[Beyond Gerstenhaber: full \texorpdfstring{$L_\infty$}{L-infinity}]\label{rem:L-infty-structure}
  4992	Configuration space geometry encodes a full $L_\infty$ structure
  4993	$\ell_n\colon \ChirHoch^*(\cA)^{\otimes n} \to \ChirHoch^{*+2-n}(\cA)$ via
  4994	\[
  4995	\ell_n(f_1, \ldots, f_n) = \int_{C_{n,1}(X)} f_1 \wedge \cdots \wedge f_n
  4996	\wedge K_n,
  4997	\]
  4998	where $K_n \in \Omega^{n-2}(\overline{C}_{n+1}(X), \mathrm{End}(\cA))$
  4999	is the propagator kernel ($K_2 = dz/(z_1-z_2)$ recovers the Gerstenhaber
  5000	bracket). Formal deformations are MC elements
  5001	$\gamma \in \ChirHoch^2(\cA)[[\hbar]]$ satisfying
  5002	$\sum_{n \geq 1} \frac{1}{n!}\ell_n(\gamma, \ldots, \gamma) = 0$.
  5003	\end{remark}
  5004	
  5005	\subsection{Computational strategy}
  5006	
  5007	\begin{remark}[Computing \texorpdfstring{$\ChirHoch^*$}{CH^*} in practice]\label{rem:compute-HH}
  5008	To compute $\ChirHoch^n(\mathcal{A})$ for a chiral algebra given by generators and OPE data, one proceeds as follows: (1) construct the bar complex $\bar{B}^n(\mathcal{A})$ using configuration space integrals; (2) build the cobar complex $\Omega(\bar{B}(\mathcal{A}))$ by inserting distributional duals; (3) form the Hom complex $\operatorname{Hom}(\Omega(\bar{B}(\mathcal{A})), \mathcal{A})$; (4) compute cohomology $\ker(d)/\operatorname{im}(d)$ at each degree. For Koszul algebras, the concentration of the bar coalgebra $\bar{B}(\mathcal{A})$ (whose dual is~$\mathcal{A}^!$) reduces the computation to lower-dimensional complexes.
  5009	\end{remark}

thinking
**Inspecting theorem relevance**

I need to check into the theorem `thm:spectral-sequence-collapse`, as it could be significant. There's a remark that references it, but it looks like the earlier theorem H doesn’t cite it, which might be important. I wonder if spectral sequence collapse is essential for the context. I'll search for the label to gather more information. It feels crucial to ensure I'm covering all the bases here!
exec
/bin/zsh -lc "rg -n \"label\\{thm:spectral-sequence-collapse\\}|label\\{thm:bar-cobar-spectral-sequence\\}|spectral-sequence-collapse|bar-cobar-spectral-sequence\" chapters/theory chapters/examples chapters/connections appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/combinatorial_frontier.tex:101:PBW spectral sequence collapse (Theorem~\ref{thm:spectral-sequence-collapse}),
appendices/combinatorial_frontier.tex:256:$\dim(\mathrm{Vir}_c^!)_n = M(n+1) - M(n)$ for all $n \geq 1$ (Theorem~\ref{thm:spectral-sequence-collapse}). The differences $M(n+1) - M(n)$ (OEIS~A002026) count $U$-initial Motzkin paths of length~$n+1$, i.e., Motzkin paths whose first step is an up step. This count has a direct representation-theoretic meaning: the bijection of Theorem~\ref{thm:motzkin-path-model} associates to each basis element of $H^n(\barBgeom(\mathrm{Vir}_c))$ a $U$-initial Motzkin path, with the three step types corresponding to the three singular terms in the Virasoro OPE $T(z)T(w)$.
chapters/connections/editorial_constitution.tex:2175:Theorem~\ref{thm:bar-cobar-spectral-sequence}. Part (iii)
chapters/connections/editorial_constitution.tex:2217:(Theorem~\ref{thm:bar-cobar-spectral-sequence}). The remaining
chapters/connections/genus_complete.tex:454:\item $d_r$ ($r \geq 4$): Higher obstruction classes. The differential $d_r\colon E_r^{p,q} \to E_r^{p+r,q-r+1}$ detects higher extension data in the sheaf cohomology of $\overline{\mathcal{M}}_g$. For Koszul algebras, the weight filtration forces these to vanish at bounded stage (Theorem~\ref{thm:bar-cobar-spectral-sequence})
chapters/theory/higher_genus_modular_koszul.tex:764:and~\ref{thm:bar-cobar-spectral-sequence};
chapters/theory/higher_genus_modular_koszul.tex:1672:and~\ref{thm:bar-cobar-spectral-sequence}.
chapters/theory/en_koszul_duality.tex:762:of Theorem~\ref{thm:bar-cobar-spectral-sequence}, reinterpreted as
chapters/theory/bar_cobar_adjunction_inversion.tex:28:property (Theorem~\ref{thm:spectral-sequence-collapse}),
chapters/theory/bar_cobar_adjunction_inversion.tex:1659: by the Koszul property (Theorem~\ref{thm:spectral-sequence-collapse})
chapters/theory/bar_cobar_adjunction_inversion.tex:1720:(Theorem~\ref{thm:spectral-sequence-collapse}) relies on
chapters/theory/bar_cobar_adjunction_inversion.tex:1812:Theorem~\ref{thm:bar-cobar-spectral-sequence}; collapse for Koszul input is
chapters/theory/bar_cobar_adjunction_inversion.tex:1813:Theorem~\ref{thm:spectral-sequence-collapse}.
chapters/theory/bar_cobar_adjunction_inversion.tex:2030:The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
chapters/theory/bar_cobar_adjunction_inversion.tex:2035:\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
chapters/theory/bar_cobar_adjunction_inversion.tex:2095:\begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
chapters/theory/bar_cobar_adjunction_inversion.tex:2102:strict square-zero surface of Theorem~\ref{thm:bar-cobar-spectral-sequence}, the spectral sequence from
chapters/theory/bar_cobar_adjunction_inversion.tex:2103:Theorem~\ref{thm:bar-cobar-spectral-sequence} collapses at the $E_2$ page:
chapters/theory/bar_cobar_adjunction_inversion.tex:2119:Theorems~\ref{thm:bar-cobar-spectral-sequence}
chapters/theory/bar_cobar_adjunction_inversion.tex:2120:and~\ref{thm:spectral-sequence-collapse} are statements about filtered
exec
/bin/zsh -lc "rg -n \"define.*ChirHoch|definition.*Chiral Hochschild|Chiral Hochschild complex|C\\"'^'"\\{\\\\bullet\\}_\\{\\\\mathrm\\{ch|C\\"'^'"\\\\bullet_\\{\\\\mathrm\\{ch|Ext\\"'^n_'"\\{\\\\text\\{ChirAlg\\}|RHH_\\{\\\\mathrm\\{ch|RHH_\\{\\\\mathrm\\{chiral|Hochschild cohomology.*by definition|precisely \\\\ChirHoch|\\\\ChirHoch\\"'^n'"\\(\\\\mathcal\\{A\\}\\) = H\\"'^n" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Hom_\\{\\\\text\\{ChirAlg\\}\\}|Ext\\"'^n_'"\\{\\\\text\\{ChirAlg\\}\\}|RHom_\\{\\\\mathrm\\{ChirAlg\\}\\}|derived category of augmented factorization algebras|D\\"'^b'"\\(\\\\mathrm\\{Fact\\}.*\\)\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(def:.*hochschild.*|def:.*chirhoch.*|def:.*RHH.*)\\}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:define.*ChirHoch|definition.*Chiral Hochschild|Chiral Hochschild complex|C\^\{\bullet\}_\{\mathrm\{ch|C\^\bullet_\{\mathrm\{ch|Ext\^n_\{\text\{ChirAlg\}|RHH_\{\mathrm\{ch|RHH_\{\mathrm\{chiral|Hochschild cohomology.*by definition|precisely \ChirHoch|\ChirHoch\^n\(\mathcal\{A\}\) = H\^n)
                                                                                                 ^^
error: unrecognized escape sequence
 exited 2 in 53ms:
rg: regex parse error:
    (?:Hom_\{\text\{ChirAlg\}\}|Ext\^n_\{\text\{ChirAlg\}\}|RHom_\{\mathrm\{ChirAlg\}\}|derived category of augmented factorization algebras|D\^b\(\mathrm\{Fact\}.*\))
                                                                   ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:299:\label{def:chiral-hochschild-cochain-brace}
chapters/theory/hochschild_cohomology.tex:77:\label{def:chiral-hochschild-derived}
chapters/theory/hochschild_cohomology.tex:470:\label{def:chiral-hochschild}
chapters/theory/higher_genus_foundations.tex:2673:\label{def:bigraded-hochschild}

thinking
**Simplifying searches**

I've realized I need to make my searches simpler. Sometimes I overthink the queries, and that makes things more complicated than they need to be. By focusing on clearer and more straightforward terms, I can streamline the process and get better results. It's about finding that balance between specificity and generality, so I don't end up with too much information or too little. I’m curious to see how this approach affects my outcomes!
exec
/bin/zsh -lc "rg -n \"Hom_\\{\\\\text\\{ChirAlg\\}\\}|RHom_\\{\\\\mathrm\\{ChirAlg\\}\\}|D\\"'^b'"\\(\\\\mathrm\\{Fact\\}|derived category of augmented factorization algebras|Ext\\"'^n_'"\\{\\\\mathrm\\{ChirAlg\\}|Ext\\"'^n_'"\\{\\\\text\\{ChirAlg\\}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '450,530p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Chiral Hochschild complex|Chiral Hochschild cohomology|derived chiral Hochschild|Ext\\"'^n|RHH_|precisely '"\\\\ChirHoch|by definition\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '60,140p'" in /Users/raeez/chiral-bar-cobar exited 2 in 53ms:
rg: regex parse error:
    (?:Hom_\{\text\{ChirAlg\}\}|RHom_\{\mathrm\{ChirAlg\}\}|D\^b\(\mathrm\{Fact\}|derived category of augmented factorization algebras|Ext\^n_\{\mathrm\{ChirAlg\}|Ext\^n_\{\text\{ChirAlg\})
                                       ^^
error: unrecognized escape sequence
 succeeded in 52ms:
   450	where $\beta_0, \gamma_0$ are zero modes. Cyclic homology adds periodicity:
   451	\[\text{HC}_*^{\text{ch}}(\beta\gamma) = \mathbb{C}[c] \otimes
   452	 \mathbb{C}[\beta_0^{-1}, \gamma_0^{-1}]_{\text{formal}}\]
   453	(the localization $\mathbb{C}[\beta_0, \gamma_0][\beta_0^{-1}, \gamma_0^{-1}]$ at the zero-mode variables, completed formally).
   454	
   455	The zero-mode periodicity in $\text{HC}_*^{\text{ch}}(\beta\gamma)$ reflects the symplectic pairing of the $\beta\gamma$ system: the localized zero modes span the deformation space of the Lagrangian splitting.
   456	\end{computation}
   457	
   458	\begin{remark}[Functoriality]
   459	The Hochschild-cyclic spectral sequence is functorial: a morphism
   460	$f\colon \cA \to \mathcal{B}$ induces $f_*\colon E_r(\cA) \to E_r(\mathcal{B})$,
   461	tensor products satisfy $E_r(\cA \otimes \mathcal{B}) \cong E_r(\cA) \otimes E_r(\mathcal{B})$
   462	up to higher structure, and Koszul duality gives $E_r(\cA^!) \cong E_r(\cA)^\vee$.
   463	The Hochschild complex represents the functor
   464	$\operatorname{Bimod}_{\cA} \ni M \mapsto \operatorname{Hom}_{\operatorname{Bimod}}(\operatorname{HH}(\cA), M)$.
   465	\end{remark}
   466	
   467	\subsection{Hochschild complex for chiral algebras}
   468	
   469	\begin{definition}[Chiral Hochschild complex]
 exited 2 in 52ms:
rg: regex parse error:
    (?:Chiral Hochschild complex|Chiral Hochschild cohomology|derived chiral Hochschild|Ext\^n|RHH_|precisely \ChirHoch|by definition)
                                                                                                              ^^
error: unrecognized escape sequence
 succeeded in 52ms:
    60	are all defined here and should be cited from here throughout the text.
    61	Other chapters that use Hochschild or cyclic invariants
    62	(the deformation theory and Poincar\'e duality chapters)
    63	reference these definitions rather than re-establishing them.
    64	\end{remark}
    65	
    66	\section{Classical to chiral}
    67	
    68	\subsection{Review of classical Hochschild}
    69	
    70	For an associative algebra $A$ over $\mathbb{C}$ and an $A$-bimodule~$M$, the Hochschild cohomology $HH^*(A, M) = \mathrm{Ext}^*_{A^e}(A, M)$ classifies the deformation theory of~$A$: $HH^0$ is the center, $HH^1$ classifies outer derivations, $HH^2$ classifies first-order deformations, and $HH^3$ contains the obstructions to extending them. The full structure is computed by the bar resolution $\cdots \to A^{\otimes(n+2)} \xrightarrow{b} A^{\otimes(n+1)} \to \cdots$ with differential $b(a_0 \otimes \cdots \otimes a_{n+1}) = \sum_{i=0}^n (-1)^i a_0 \otimes \cdots \otimes a_ia_{i+1} \otimes \cdots \otimes a_{n+1}$, and the resulting cohomology carries a Gerstenhaber bracket governing the Maurer--Cartan equation for formal deformations (Gerstenhaber~\cite{Ger63}).
    71	
    72	\subsection{Chiral enhancement}
    73	
    74	What replaces the bimodule $A \otimes A^{\mathrm{op}}$ when the algebra lives on a curve rather than a point? For chiral algebras, each ingredient of the classical theory acquires a geometric upgrade: the bimodule structure is replaced by the factorization structure on~$\operatorname{Ran}(X)$, the bar resolution becomes the geometric bar complex on Fulton--MacPherson configuration spaces, and the Gerstenhaber bracket lifts to a chiral bracket governed by the OPE. The result is a chiral Hochschild complex whose cohomology computes chiral deformations, obstructions, and the center of the chiral algebra simultaneously.
    75	
    76	\begin{definition}[Chiral Hochschild complex, derived-functor form]
    77	\label{def:chiral-hochschild-derived}
    78	For a chiral algebra $\mathcal{A}$ on $X$, the chiral Hochschild
    79	cohomology with coefficients in a chiral $\mathcal{A}$-module

thinking
**Confirming citation needs**

I see there’s another file, `chapters/theory/hochschild_cohomology.tex`, that has important definitions. I need to figure out if the section on chiral_hochschild_koszul should cite these definitions instead of repeating them. A remark points out that other chapters using Hochschild or cyclic invariants reference this instead of redefining. Since chiral_hochschild_koszul redefines them differently, it could be a critical finding. I should inspect the first 64 lines of that file.
exec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '1,90p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
     1	\chapter{Chiral Hochschild cohomology and deformation theory}
     2	
     3	\index{Hochschild cohomology!classical}
     4	\index{cyclic homology!chiral}
     5	
     6	The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ is the
     7	tangent complex to the MC moduli at~$\Theta_\cA$: the cohomology
     8	of the convolution $L_\infty$-algebra controlling deformations,
     9	obstructions, and bulk-field couplings.
    10	
    11	The chiral Hochschild complex carries a degree $-1$ Lie bracket
    12	(the chiral Gerstenhaber bracket, Theorem~\ref{thm:gerstenhaber-structure}),
    13	computed by OPE residues on FM configuration spaces.
    14	In the classical limit (fiber at a point), it recovers
    15	Gerstenhaber's bracket~\cite{Ger63} on associative Hochschild
    16	cochains. The chiral bracket is the strict shadow of a full
    17	$L_\infty$ bracket on the chiral Hochschild complex. In the strict model, $\mathrm{HH}^2$ classifies
    18	first-order deformations and $\mathrm{HH}^3$ contains obstructions;
    19	the $L_\infty$ extension records coherent homotopies governing
    20	convergence of formal deformations and transfer of Koszul properties

thinking
**Inspecting canonical sources**

I'm looking at the other chapter as a canonical source, but the target chapter redefines things differently without citing, which seems like it violates some important remarks. I need to take notes but the user is asking for a file audit, so I should definitely follow through on that. I also have to inspect the `bar-cobar_adjunction_inversion` spectral sequence theorem because it seems that local theorem 324, steps 1 and 2 rely on the bar-cobar quasi-isomorphism. I'll search around 2035 and 2095 for more clarity.
codex
There is already a canonical Hochschild chapter in the repo that says this deformation chapter should cite its definitions instead of rebuilding them. I’m checking that canonical surface now, because any mismatch between the two definitions turns Theorem H into a moving target rather than a theorem.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '4110,4175p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2028,2128p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1435,1475p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1240,1295p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
  4120	
  4121	\begin{proof}
  4122	Let $C=\operatorname{Cone}(f)$. It suffices to prove $C$ is acyclic.
  4123	From $j^*f$ and $i^*f$ quasi-isomorphisms, $j^*C$ and $i^*C$ are acyclic.
  4124	Apply the localization triangle
  4125	\[j_!j^*C \longrightarrow C \longrightarrow i_*i^*C \xrightarrow{+1}.\]
  4126	Both outer terms are acyclic, hence $C$ is acyclic. Therefore $f$ is a
  4127	quasi-isomorphism.
  4128	\end{proof}
  4129	
 succeeded in 52ms:
  2028	\[\text{Gr}^p = F^p / F^{p+1} = \Omega^p(\bar{B}^p(\mathcal{A}))\]
  2029	
  2030	The full differential on $\Omega(\bar{B}(\mathcal{A}))$ decomposes as $d = d_{\bar{B}} + d_{\text{cobar}}$, where $d_{\bar{B}} = d_{\text{internal}} + d_{\text{bar}}$ is the lift of the bar complex differential to each cobar tensor factor (preserving cobar degree~$p$), and $d_{\text{cobar}}$ is the comultiplication-induced part (raising cobar degree by~$1$). On the associated graded $\text{Gr}^p = F^p/F^{p+1}$, only the \emph{filtration-preserving} component survives: $d_{\text{cobar}}$ maps $F^p$ into $F^{p+1}$ and so vanishes on $\text{Gr}^p$. Thus $d_{\text{gr}} = d_{\bar{B}}$, which is the $d_0$ differential of the spectral sequence (cf.\ Theorem~\ref{thm:bar-cobar-spectral-sequence}).
  2031	\end{proof}
  2032	
  2033	\subsection{Spectral sequence construction}
  2034	
  2035	\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
  2036	\label{thm:koszul-spectral-sequence}
  2037	\textup{[Regime: square-zero total differential on the filtered
  2038	bar-cobar complex.]}
  2039	Assume the total differential on $\Omega(\bar{B}(\mathcal{A}))$
  2040	satisfies $d^2 = 0$ and preserves the filtration from
  2041	Definition~\ref{def:bar-cobar-filtration}. Then the filtration from
  2042	Definition~\ref{def:bar-cobar-filtration} induces a spectral
  2043	sequence:
  2044	\[E_0^{p,q} = \left(F^p / F^{p+1}\right)^{p+q} \implies H^{p+q}(\Omega(\bar{B}(\mathcal{A})))\]
  2045	converging to the cohomology of $\Omega(\bar{B}(\mathcal{A}))$. Here $p$ is the filtration degree (cobar degree) and $q$ is the complementary degree (from the internal and bar gradings), so the total degree is $p + q$.
  2046	
  2047	\emph{Explicit description of pages.}
 succeeded in 51ms:
  1435	This is computed via the Gauss--Manin connection: the central charge $\kappa$ pairs with
  1436	the KS class $\partial/\partial\tau$ to give $\lambda_1$ (Mumford isomorphism).
  1437	\end{proof}
  1438	
  1439	\emph{Step 8: Verdier involution and eigenspace decomposition.}
  1440	
  1441	The anti-commutativity~\eqref{eq:verdier-ks-anticommute} is the key to the
  1442	eigenspace decomposition. We construct a canonical involution on $H^*(\overline{
  1443	\mathcal{M}}_g, Z(\mathcal{A}))$ whose $\pm 1$ eigenspaces give $Q_g(\mathcal{A})$
  1444	and $Q_g(\mathcal{A}^!)$.
  1445	
  1446	\begin{lemma}[Verdier involution on moduli cohomology; \ClaimStatusProvedHere]
  1447	\label{lem:verdier-involution-moduli}
  1448	For a chiral Koszul pair $(\mathcal{A}, \mathcal{A}^!)$, Verdier duality on
  1449	$\overline{C}_n(X)$ together with the Koszul pairing $\mathcal{A} \otimes
  1450	\mathcal{A}^! \to \mathcal{O}_X$ induces an involution:
  1451	\begin{equation}
  1452	\sigma: H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) \xrightarrow{\sim}
  1453	H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A}))
  1454	\end{equation}
 succeeded in 51ms:
  1240	\bigoplus_{p+q=n} ((E_\infty^{p,d-q,g})_{\mathcal{A}^!})^\vee = Q_g(\mathcal{A}^!)^\vee
  1241	\end{equation}
  1242	\end{proof}
  1243	
  1244	This completes Step~II: Verdier duality on configuration spaces
  1245	induces a duality of spectral sequences and a perfect pairing
  1246	between $Q_g(\mathcal{A})$ and $Q_g(\mathcal{A}^!)$ for $g \geq 1$;
  1247	the genus-$0$ cohomological-shadow exception is recorded in
  1248	Theorem~\ref{thm:quantum-complementarity-main}.
  1249	\end{proof}
  1250	
  1251	\subsection{Step III: decomposition and complementarity}
  1252	
  1253	\begin{proof}[Step III: Steps 7-10]
  1254	
  1255	\emph{Step 7: Center action on moduli space cohomology.}
  1256	
  1257	\begin{theorem}[Kodaira--Spencer map for chiral algebras; \ClaimStatusProvedHere]
  1258	\label{thm:kodaira-spencer-chiral-complete}
  1259	\index{Kodaira--Spencer map|textbf}

thinking
**Inspecting definitions and connections**

I need to focus my attention on the `def:bigraded-hochschild` around line 2677, which seems to involve RHom_D( A^⊗(p+2), ω ) in the context of configuration space. This definition doesn't clearly align with the local geometric definition using `Γ(...A^{⊗}⊗Ω^n(log D))`. I should also look for any theorems that might connect these concepts. Searching for `eq:chirhoch-descent` seems like a good start. I also need to check if `RHH_ch` is defined elsewhere in the documents, particularly `hochschild_cohomology.tex`.
exec
/bin/zsh -lc "rg -n \"label\\{thm:hochschild-bar-cobar\\}|label\\{thm:hochschild-spectral-sequence\\}|label\\{thm:main-koszul-hoch\\}|label\\{thm:hochschild-polynomial-growth\\}\" metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"bigraded-hochschild|RHH_\\{\\\\mathrm\\{ch\\}\\}|CH\\"'^{p,'"\\\\bullet}_\\{\\\\mathrm\\{ch\\}\\}\" chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"RHH_\\{|bigraded chiral Hochschild complex|CH\\"'^{p,'"\\\\bullet}_\\{\\\\mathrm\\{ch\\}\\}|ChirHoch\\"'^'"\\*\\(\\\\cA, \\\\mathcal\\{M\\}\\)|derived-functor form|Hom\\(\\\\Omega\\"'^'"\\{\\\\mathrm\\{ch\\}\\}|\\(\\\\mathbb\\{D\\}_\\\\{\\\\Ran\\}\\\\bar\\{B\\}.*\\\\)_\\\\{\\\\Sigma\\\\}|bar-Hochschild|descent\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:

 exited 2 in 53ms:
rg: regex parse error:
    (?:bigraded-hochschild|RHH_\{\mathrm\{ch\}\}|CH\^{p,\bullet}_\{\mathrm\{ch\}\})
                                 ^^
error: unrecognized escape sequence
 exited 2 in 91ms:
rg: regex parse error:
    (?:RHH_\{|bigraded chiral Hochschild complex|CH\^{p,\bullet}_\{\mathrm\{ch\}\}|ChirHoch\^\*\(\cA, \mathcal\{M\}\)|derived-functor form|Hom\(\Omega\^\{\mathrm\{ch\}\}|\(\mathbb\{D\}_\{\Ran\}\bar\{B\}.*\)_\{\Sigma\}|bar-Hochschild|descent)
                                                      ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n -F \"RHH_{\\mathrm{ch}}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "bigraded chiral Hochschild complex" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/higher_genus_foundations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"(\\mathbb{D}_{\\Ran}\\bar{B}"'^{'"\\mathrm{ch}}(\\cA))_{\\Sigma}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/higher_genus_foundations.tex:2684:RHH_{\mathrm{ch}}(\cA) :=
chapters/theory/chiral_hochschild_koszul.tex:493: $RHH_{\mathrm{ch}}(\cA) := \mathrm{Tot}\bigl(
chapters/theory/chiral_hochschild_koszul.tex:590:RHH_{\mathrm{ch}}(\cA)
chapters/theory/chiral_hochschild_koszul.tex:592:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr).
chapters/theory/chiral_hochschild_koszul.tex:615:RHH_{\mathrm{ch}}(\cA)
chapters/theory/chiral_hochschild_koszul.tex:619:RHH_{\mathrm{ch}}(\cA^!)
chapters/theory/chiral_hochschild_koszul.tex:652:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr)
chapters/theory/chiral_hochschild_koszul.tex:661:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr)
chapters/theory/chiral_hochschild_koszul.tex:665:RHH_{\mathrm{ch}}(\cA),
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:2675:The \emph{bigraded chiral Hochschild complex} of a chiral
 exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '486,500p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   486	the three grading contributions are:
   487	\begin{enumerate}[label=\textup{(\roman*)}]
   488	\item \emph{Verdier shift:} $[p+2]$, from
   489	 $\dim_{\mathbb{C}} \overline{C}_{p+2}(X) = p + 2$
   490	 \textup{(}the FM compactification of $p+2$ points on a curve
   491	 has complex dimension $p+2$\textup{)};
   492	\item \emph{Totalization shift:} $[-p]$, from the convention
   493	 $RHH_{\mathrm{ch}}(\cA) := \mathrm{Tot}\bigl(
   494	 \bigoplus_{p \geq 0} CH^{p,\bullet}_{\mathrm{ch}}(\cA)[-p]\bigr)$;
   495	\item \emph{Net shift:} $(p+2) + (-p) = 2$, independent of~$p$.
   496	\end{enumerate}
   497	Koszul concentration
   498	\textup{(}Theorem~\textup{\ref{thm:bar-concentration})}
   499	forces $H^{p,q} = 0$ for $q \neq 0$, so only the diagonal $p = q$
   500	survives. The variable bar-degree index~$p$ thereby drops out of

thinking
**Inspecting theorem registry**

I need to check the local theorem registry for specific labels, as they might be missing due to their status, but I'm thinking that’s unlikely. It could be possible that the theorem labels are not present in the registry because they haven't been scanned yet. I think a good approach would be to search for metadata lines related to these theorem labels. Maybe using fixed strings in the search will help clarify things!
exec
/bin/zsh -lc 'rg -n -F "thm:main-koszul-hoch" metadata/theorem_registry.md && rg -n -F "thm:hochschild-polynomial-growth" metadata/theorem_registry.md && rg -n -F "thm:hochschild-bar-cobar" metadata/theorem_registry.md && rg -n -F "thm:hochschild-spectral-sequence" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
350:| `thm:main-koszul-hoch` | `theorem` | 578 | Koszul duality for Hochschild cohomology \textup{(}Theorem~H\textup{)} |
351:| `thm:hochschild-polynomial-growth` | `theorem` | 689 | Polynomial growth of chiral Hochschild cohomology \textup{(}Theorem~H, growth clause\textup{)} |
346:| `thm:hochschild-bar-cobar` | `theorem` | 324 | Hochschild via bar-cobar |
347:| `thm:hochschild-spectral-sequence` | `theorem` | 362 | Hochschild spectral sequence |

thinking
**Clarifying the mathematical proof**

I need to focus on the exact findings related to the Hochschild polynomial growth theorem. It specifically deduces vanishing for n>2 from Theorem H duality and negative Ext vanishing, not from the spectral sequence. I'm noticing that the spectral sequence from pages 362-372 isn’t utilized at all, which is a problem. This is high severity, especially since the user was looking for that proof regarding concentration that isn't delivered in the file.
codex
The theorem-H lane is mixing at least three non-equivalent models: global sections on configuration spaces, `RHom` of bar objects, and a bigraded `RHom` on configuration spaces. I’m checking whether the file ever proves these models agree, because right now the proof appears to jump between them without a comparison theorem.
exec
/bin/zsh -lc "rg -n -F \"\\omega_X\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/higher_genus_foundations.tex:2656:\omega_X[2]\bigr).
chapters/theory/higher_genus_foundations.tex:2662:\otimes \omega_X.
chapters/theory/hochschild_cohomology.tex:847:The SBI exact sequence (Corollary~\ref{cor:connes-SBI}) relates $\mathrm{HH}_*$ and $\mathrm{HC}_*$ via the periodicity operator $S$. The Koszul duality for Hochschild cohomology (Theorem~\ref{thm:main-koszul-hoch}) gives $\mathrm{HH}^n(\mathcal{A}) \cong \mathrm{HH}^{2-n}(\mathcal{A}^!)^\vee \otimes \omega_X$. Inserting this into the SBI sequence for $\mathcal{A}$ and comparing with the SBI sequence for $\mathcal{A}^!$: the periodicity operator $S$ shifts degree by $-2$ on both sides, so the duality on $\mathrm{HH}_*$ descends to periodic cyclic homology as stated. The shift by~$2$ in the Hochschild duality is absorbed by the periodicity $S$, yielding the unshifted duality~\eqref{eq:cyclic-duality} on $\mathrm{HP}_* = \varprojlim_S \mathrm{HC}_{*+2k}$.
chapters/theory/hochschild_cohomology.tex:869:For a Koszul pair $(\mathcal{A}, \mathcal{A}^!)$, let $\Theta \in CH^2(\mathcal{A})$ be a periodicity class \textup{(}as in Theorem~\textup{\ref{thm:virasoro-periodicity})}. Under the Koszul duality isomorphism $CH^n(\mathcal{A}) \cong CH^{2-n}(\mathcal{A}^!)^\vee \otimes \omega_X$ \textup{(}Theorem~\textup{\ref{thm:main-koszul-hoch})}, the cup product with $\Theta$ corresponds to the cup product with the dual class $\Theta' \in CH^2(\mathcal{A}^!)$ up to sign:
chapters/theory/hochschild_cohomology.tex:885:\otimes \omega_X$ maps $\Theta \mapsto -\Theta'$ (up to the
chapters/theory/hochschild_cohomology.tex:886:$\omega_X$ twist), where the sign comes from the Verdier
chapters/theory/chiral_hochschild_koszul.tex:16:$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
chapters/theory/chiral_hochschild_koszul.tex:136:$\ChirHoch^n(\cA)\cong \ChirHoch^{2-n}(\cA^!)^\vee\otimes\omega_X$
chapters/theory/chiral_hochschild_koszul.tex:413:\item $\mathcal{V}^* = \mathcal{H}om_{\mathcal{O}_X}(\mathcal{V}, \omega_X)$ is the dual shifted by the canonical bundle
chapters/theory/chiral_hochschild_koszul.tex:502:\emph{uniform constant}~$[2]$. The remaining $\omega_X$ twist
chapters/theory/chiral_hochschild_koszul.tex:504:the dualizing object for right $\mathcal{D}_X$-modules is~$\omega_X$.
chapters/theory/chiral_hochschild_koszul.tex:532:The $\omega_X$ factor: Serre duality on the one-dimensional base
chapters/theory/chiral_hochschild_koszul.tex:533:curve~$X$ contributes $\omega_X = \Omega^1_X$ as the dualizing sheaf.
chapters/theory/chiral_hochschild_koszul.tex:592:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr).
chapters/theory/chiral_hochschild_koszul.tex:596:\ChirHoch^n(\mathcal{A}) \cong \ChirHoch^{2-n}(\mathcal{A}^!)^{\vee} \otimes \omega_X.
chapters/theory/chiral_hochschild_koszul.tex:604:The $\omega_X$ twist encodes the dualizing sheaf.
chapters/theory/chiral_hochschild_koszul.tex:650:base-curve twist~$\omega_X$. Therefore
chapters/theory/chiral_hochschild_koszul.tex:652:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr)
chapters/theory/chiral_hochschild_koszul.tex:661:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr)
chapters/theory/chiral_hochschild_koszul.tex:671:\ChirHoch^{2-n}(\cA^!)^{\vee} \otimes \omega_X.
exec
/bin/zsh -lc "rg -n -F \"RHom_{\\mathcal{D}_X}(\\barBgeom(\\mathcal{A}), \\mathcal{M})\" chapters/theory/hochschild_cohomology.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\mathrm{Hom}_{\\text{ChirAlg}}(\\Omega"'^{'"\\text{ch}}(\\overline{B}"'^{'"\\text{ch}}(\\mathcal{A})), \\mathcal{A})\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"\\mathbb{D}_{\\Ran}\\bar{B}"'^{'"\\mathrm{ch}}(\\cA)\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 52ms:

 succeeded in 53ms:
chapters/theory/chiral_hochschild_koszul.tex:551:\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma},
chapters/theory/chiral_hochschild_koszul.tex:560:$\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)$ on $\Ran(X)$ computes
chapters/theory/chiral_hochschild_koszul.tex:617:\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma},
chapters/theory/chiral_hochschild_koszul.tex:628:\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)
chapters/theory/chiral_hochschild_koszul.tex:663:\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma}
chapters/theory/chiral_hochschild_koszul.tex:551:\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma},
chapters/theory/chiral_hochschild_koszul.tex:560:$\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)$ on $\Ran(X)$ computes
chapters/theory/chiral_hochschild_koszul.tex:617:\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma},
chapters/theory/chiral_hochschild_koszul.tex:628:\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)
chapters/theory/chiral_hochschild_koszul.tex:663:\bigl(\mathbb{D}_{\Ran}\bar{B}^{\mathrm{ch}}(\cA)\bigr)_{\Sigma}
exec
/bin/zsh -lc "rg -n -F \"Hom_{\\text{ChirAlg}}(\\Omega"'^{'"\\text{ch}}(\\overline{B}"'^{'"\\text{ch}}(\\mathcal{A})), \\mathcal{A})\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F \"Hom_{\\text{ChirAlg}}\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Exploring file usage**

I'm thinking that the file might use `\\text{Hom}_{\\text{ChirAlg}}`. So I need to search for `ChirAlg` specifically and see where it may be fixed or referenced. It seems like there might be some additional context or corrections that I need to figure out. Let's see how the usage connects to the content! I want to ensure I’m accurate and thorough while I’m checking this out.
exec
/bin/zsh -lc 'rg -n -F "ChirAlg" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
chapters/theory/chiral_hochschild_koszul.tex:332:C^{\bullet}_{\text{chiral}}(\mathcal{A}) \simeq \text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A})), \mathcal{A})
chapters/theory/chiral_hochschild_koszul.tex:355:\text{Ext}^n_{\text{ChirAlg}}(\mathcal{A}, \mathcal{A}) = H^n(\text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A})), \mathcal{A}))
chapters/theory/chiral_hochschild_koszul.tex:572:this with $\mathrm{RHom}_{\mathrm{ChirAlg}}(\cA, \cA) =
chapters/theory/chiral_hochschild_koszul.tex:756:\mathrm{Ext}^n_{\mathrm{ChirAlg}(X)}(\cA, \cA),
chapters/theory/fourier_seed.tex:894:\mathrm{ChirAlg}(X) \arrow[r, "\barB_X"]
chapters/theory/bar_construction.tex:1044:\mathsf{ChirAlg}_X^{\mathrm{aug}} \to
chapters/theory/bar_construction.tex:1431:\[\bar{B}^{\text{geom}}: \mathsf{ChirAlg}_X^{\mathrm{aug}} \to \mathsf{dgCoalg}_X\]
chapters/theory/bar_construction.tex:1469:A commutative diagram of chiral algebras induces a commutative diagram of bar complexes: if $k \circ f = g \circ h$ in $\mathsf{ChirAlg}_X$, then $\bar{B}(k) \circ \bar{B}(f) = \bar{B}(g) \circ \bar{B}(h)$ in $\mathsf{dgCoalg}_X$. This is immediate from functoriality.
chapters/theory/bar_construction.tex:2214:\[\bar{B}_{geom}: \text{ChirAlg}_X \to \text{dgCoalg}\]
chapters/theory/higher_genus_complementarity.tex:3932:For $\mathcal{A} \in \text{ChirAlg}(X)$, view it as a $D$-module on $\text{Ran}(X)$. Then:
chapters/theory/koszul_pair_structure.tex:936:\text{Hom}_{\text{ChirAlg}}(\mathcal{A}, B) \cong \text{MC}(\mathcal{A}^! \otimes B)
chapters/theory/configuration_spaces.tex:3269:\item This defines a fully faithful functor $\text{ChirAlg}(X) \to \text{FactAlg}(X)$
chapters/theory/configuration_spaces.tex:3292:\[\text{ChirAlg}(X) \hookrightarrow \text{FactAlg}(X)\]
chapters/theory/configuration_spaces.tex:3299:For the embedding $\mathrm{ChirAlg}(X) \hookrightarrow \mathrm{FactAlg}(X)$: given a chiral algebra $\mathcal{A}$, define $\mathcal{F}_{\mathcal{A}}(S) = j_{S*}j_S^*\mathcal{A}^{\boxtimes S}$ for finite $S$, with factorization isomorphisms coming from the chiral product (Beilinson--Drinfeld~\cite{BD04}, Theorem~3.4.9). Fully faithfulness follows because chiral algebras are determined by their factorization data on pairs of points (the chiral product $\mu$).
chapters/theory/configuration_spaces.tex:4832:\[\text{ChirAlg}(M) \simeq \text{D-mod}_{\text{fact}}(\text{Ran}(M))\]
chapters/theory/configuration_spaces.tex:4929:\textbf{D-modules} & $\text{ChirAlg}(M) \simeq \text{D-mod}_{\text{fact}}(\text{Ran}(M))$ \\
chapters/theory/chiral_hochschild_koszul.tex:332:C^{\bullet}_{\text{chiral}}(\mathcal{A}) \simeq \text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A})), \mathcal{A})
chapters/theory/chiral_hochschild_koszul.tex:355:\text{Ext}^n_{\text{ChirAlg}}(\mathcal{A}, \mathcal{A}) = H^n(\text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A})), \mathcal{A}))
chapters/theory/chiral_hochschild_koszul.tex:572:this with $\mathrm{RHom}_{\mathrm{ChirAlg}}(\cA, \cA) =
chapters/theory/chiral_hochschild_koszul.tex:756:\mathrm{Ext}^n_{\mathrm{ChirAlg}(X)}(\cA, \cA),
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_foundations.tex | sed -n '2035,2085p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2035	
  2036	\subsubsection{Resolution at chain level}
  2037	
  2038	\begin{theorem}[Cobar resolution on the Koszul locus {\cite{LV12}}; \ClaimStatusProvedElsewhere]
  2039	\label{thm:cobar-resolution-scoped}
  2040	For any augmented chiral algebra $\mathcal{A}$, the bar construction
  2041	$\bar{B}^{\mathrm{ch}}(\mathcal{A})$ and cobar construction
  2042	$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\mathcal{A}))$ exist as objects.
  2043	When the canonical twisting morphism is Koszul
  2044	\textup{(}Definition~\textup{\ref{def:chiral-koszul-morphism})},
  2045	the cobar of the bar provides a free resolution:
  2046	\begin{multline*}
  2047	\cdots \to \Omega^2_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
  2048	\to \Omega^1_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))\\
  2049	\to \Omega^0_{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(\cA))
  2050	\xrightarrow{\epsilon} \cA \to 0
  2051	\end{multline*}
  2052	Off the Koszul locus, the bar-cobar object persists only in the
  2053	completed coderived category
  2054	\textup{(}Appendix~\textup{\ref{sec:coderived-models})}.
exec
/bin/zsh -lc "rg -n -F \"def:chiral-hochschild-derived\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/hochschild_cohomology.tex:77:\label{def:chiral-hochschild-derived}

thinking
**Investigating unresolved references**

I’m considering how to catch unresolved references in a file since the user has specifically mentioned it. Maybe I could use `latexmk` to grep logs, but that might be too heavy. Instead, I could apply `rg` to look for `\ref{...}` labels and check what's missing. I want to inspect labels, focusing on those cited in “theorem H.” I think I can confirm that the major labels are present, but maybe there's an issue with understanding a specific reference.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '20,70p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
    20	
    21	\bigskip
    22	
    23	\noindent\textbf{The five main theorems.}\quad
    24	The algebraic engine rests on five theorems, all proved.
    25	
    26	\begin{center}
    27	\renewcommand{\arraystretch}{1.3}
    28	\begin{tabular}{clp{7.5cm}l}
    29	& \textbf{Theorem} & \textbf{Statement} & \textbf{Status} \\
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

thinking
**Considering local theorems**

I might want to mention that local theorem H isn't aligned with concordance. It feels like there's a gap there that I can address, so I’ll probably look into continuing lines 70 to 72. Those lines could provide some important context or clarifications that would really help in understanding the situation better. It’s key to ensure everything fits together logically! I'm curious to see how it all connects.
exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '64,74p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    64	\textbf{H} & Chiral Hochschild
    65	 & $\ChirHoch^*(\cA)$ polynomial with Hilbert polynomial
    66	 $P(t)=1+t^2$, Koszul-functorial;
    67	 $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
    68	 \textup{(}Thms~\ref{thm:w-algebra-hochschild},
    69	 \ref{thm:virasoro-hochschild},
    70	 \ref{thm:critical-level-cohomology};
    71	 Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
    72	 & \ClaimStatusProvedHere
    73	\end{tabular}
    74	\end{center}
exec
/bin/zsh -lc "rg -n -F \"RHH_{\\mathrm{ch}}\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/ym_boundary_theory.tex:362:\tau_{\ge 1} RHH_{\mathrm{ch}}(\cA_{\cB})[1],
chapters/connections/ym_boundary_theory.tex:364:where $RHH_{\mathrm{ch}}(\cA_{\cB})$ carries the shifted dg~Lie structure of the chiral Hochschild complex, a strict model of the deformation $L_\infty$-algebra (Remark~\ref{rem:conv-strict-vs-homotopy}). Its Maurer--Cartan functor governs formal boundary deformations of~$\cA_{\cB}$.
chapters/theory/higher_genus_foundations.tex:2684:RHH_{\mathrm{ch}}(\cA) :=
chapters/theory/chiral_hochschild_koszul.tex:493: $RHH_{\mathrm{ch}}(\cA) := \mathrm{Tot}\bigl(
chapters/theory/chiral_hochschild_koszul.tex:590:RHH_{\mathrm{ch}}(\cA)
chapters/theory/chiral_hochschild_koszul.tex:592:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr).
chapters/theory/chiral_hochschild_koszul.tex:615:RHH_{\mathrm{ch}}(\cA)
chapters/theory/chiral_hochschild_koszul.tex:619:RHH_{\mathrm{ch}}(\cA^!)
chapters/theory/chiral_hochschild_koszul.tex:652:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr)
chapters/theory/chiral_hochschild_koszul.tex:661:R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr)
chapters/theory/chiral_hochschild_koszul.tex:665:RHH_{\mathrm{ch}}(\cA),

thinking
**Inspecting theorem definitions**

I need to check if the local theorem 145 definition really uses “one output, n inputs, one evaluation point,” since that seems unusual. If the overall model is invalid, it could be low-level. I might also search for a proper definition for “bar-Hochschild complex” in the file, specifically around lines 4604. There could be a more formal definition later, so I should look closely between lines 4600 and 4660 because I came across a formula that needs review.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4588,4668p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  4588	boundary (Costello--Li). The relation $c_{\text{bulk}} +
  4589	c_{\text{boundary}} = 26$ has no known proof from Koszul duality alone.
  4590	(Contributing to Conjecture~\ref{conj:master-bv-brst}.)
  4591	\end{remark}
  4592	
  4593	Three pieces of evidence: the central charges satisfy
  4594	$c_{\mathrm{bulk}} + c_{\mathrm{boundary}} = 26$, the Hochschild
  4595	cohomologies are Koszul dual, and the twisting morphism exhibits
  4596	the formal pattern of the conjectural holographic dictionary.
  4597	
  4598	\section{Computing Hochschild cohomology via bar-cobar resolution}
  4599	\label{sec:hochschild-via-bar-cobar-complete}
  4600	
  4601	\subsection{The bar-cobar resolution strategy}
  4602	
  4603	The bar-cobar approach computes Hochschild cohomology via the quasi-isomorphism
  4604	$\ChirHoch^n(\mathcal{A}) = H^n\bigl(\mathrm{Hom}_{\mathsf{Alg}}(\Omega(\bar{B}(\mathcal{A})),
  4605	\mathcal{A})\bigr)$,
  4606	using the cofree coalgebra resolution $\bar{B}(\mathcal{A})$ and the free algebra resolution $\Omega(\bar{B}(\mathcal{A}))$.
  4607	


thinking
**Reviewing theorem H findings**

I notice there's a later section that seems to replicate earlier results with possibly more complete formulas. Since the user's mission is specifically about auditing the foundation of chapters related to theorem H, I think I should inspect lines starting from 4598 for more complete proof. It's possible there's duplication causing some drift, as the file has repeated surfaces. The later theorem seems to provide differing proofs, including configurations that might repeat earlier definitions. I need to read more around those keys to understand the context better.
thinking
**Investigating potential duplicates**

I think it's important to closely inspect lines 4657 to 4685, and possibly even beyond, to check for any duplicates with earlier claims. This could help me understand if there are inconsistencies or repeated information that may lead to confusion or inaccuracies in the findings. I want to ensure I capture the relevant context surrounding these lines to discern any potential overlaps with previous sections accurately. It’s definitely a critical step in the auditing process!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4655,4725p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4655	\subsection{Hochschild cohomology formula}
  4656	
  4657	\begin{theorem}[HH* via configuration spaces; \ClaimStatusProvedHere]\label{thm:HH-config-space-formula}
  4658	The Hochschild cohomology of a chiral algebra $\mathcal{A}$ is computed by:
  4659	\[\ChirHoch^n(\mathcal{A}) = H^n\left(\Gamma\left(\overline{C}_{n+2}(X), 
  4660	\text{Hom}_{\mathcal{D}_X}(\mathcal{A}^{\boxtimes n+2}, \mathcal{A}) \otimes \Omega^n(\log D)\right), d_{\text{Hoch}}\right)\]
  4661	
  4662	where the Hochschild differential $d_{\text{Hoch}}$ has three components:
  4663	\begin{align}
  4664	d_{\text{Hoch}} &= d_{\text{internal}} + d_{\text{factor}} + d_{\text{form}} \label{eq:d-Hoch-decomposition}
  4665	\end{align}
  4666	
  4667	\emph{Component descriptions.}
  4668	\begin{enumerate}
  4669	\item $d_{\text{internal}}$: Internal differential on $\mathcal{A}$-factors
  4670	\item $d_{\text{factor}}$: Factorization using chiral product (OPE collisions)
  4671	\item $d_{\text{form}}$: de Rham differential on configuration space forms
  4672	\end{enumerate}
  4673	\end{theorem}
  4674	


thinking
**Examining definitions in cochain spaces**

I’m noticing this section duplicates earlier content and is inconsistent. There are conflicting definitions within the same file. For instance, the earlier definition uses `j_*j^*A^{\boxtimes (n+2)} \otimes Ω^n`, while a later theorem utilizes `Hom_{D_X}(A^{\boxtimes n+2},A)\otimes Ω^n`. They describe different cochain spaces. It seems the file contains at least three incompatible definitions of the cochain object. The best approach may be to choose one canonical definition and remove the duplicates.
thinking
**Addressing theorems and findings**

I see that I need to either delete the theorem or demote it to a heuristic remark. If I choose to keep it, I should first define the enveloping chiral algebra and the bimodule category before proving the equivalence with the factorization-space model. Also, I might want to inspect if the later section contains theorem H computations, which could duplicate earlier findings. The user is asking for an exhaustive audit, ideally with about 10-15 clear findings, including exact fixes and line references for any duplicates.
exec
/bin/zsh -lc "rg -n -F \"perfect \\Sigma_n-equivariant\" -g '*.tex' && rg -n -F \"holonomic D-modules on configuration\" -g '*.tex' && rg -n -F \"Verdier duality commutes with finite \\Sigma_n-coinvariants\" -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Evaluating theorem references**

The user mentioned specific references like `hochschild-bar-cobar` or `main-koszul-hoch`, but they're asking about theorem H, which isn't necessary. I might need to run a static analysis for unresolved references in the file using `rg -o "\\ref{[^}]+}"` to compare to labels. Since the file is large, perhaps focusing on local theorem H references makes sense. I already found that `thm:quantum-complementarity-main(Step 7)` exists, so that's good news. I'll also need to consider the status of other theorems and provide an updated plan.
codex
Current attack surface is narrower now: the failure is not a missing citation here or there, it is that the theorem-H lane slides between incompatible definitions and then asks a spectral sequence to do work on a bicomplex that has not been built. I’m locking the remaining checks to: model comparison, hypothesis scope, and whether any line actually proves the `{0,1,2}` concentration from the stated spectral sequence.
Plan update
Audit plan for the theorem-H foundation surface in chapters/theory/chiral_hochschild_koszul.tex
  ✓ Map the theorem-H lane and every local dependency/imported label
  → Check whether the Hochschild/bar models used in the file are consistently defined and compared
  • Test the bar-degree spectral sequence setup: bicomplex, filtration, differentials, convergence
  • Check whether concentration in {0,1,2} actually follows from the stated spectral sequence
  • Assemble only findings that survive re-verification against exact lines and state exact fixes

thinking
**Searching for definitions**

I need to check for duplicates related to theorem 4610 and might want to look into definitions for `A^e`, `bimodule`, and `A^{\boxtimes n+2}`. I can't find a local definition for chiral bimodule or `A^e`, which is a bit concerning. If the theorem references any undefined concepts, that could be a problem! I should search the file or the project to see if `A^e` is defined anywhere.
exec
/bin/zsh -lc "rg -n -F \"\\mathcal{A}"'^e" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Theorem H" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"bimodule\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/chiral_hochschild_koszul.tex:817:\index{Lagrangian self-intersection!Theorem H}
 succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:4679:\[C^n_{\text{Hoch}}(\mathcal{A}) = \text{Hom}_{\mathcal{A}^e}(\mathcal{A}^{\otimes n+2}, \mathcal{A})\]
chapters/theory/chiral_hochschild_koszul.tex:4681:An $\mathcal{A}^e$-linear map must commute with the bimodule structure, which for chiral
chapters/theory/chiral_hochschild_koszul.tex:4679:\[C^n_{\text{Hoch}}(\mathcal{A}) = \text{Hom}_{\mathcal{A}^e}(\mathcal{A}^{\otimes n+2}, \mathcal{A})\]
chapters/theory/chiral_hochschild_koszul.tex:4681:An $\mathcal{A}^e$-linear map must commute with the bimodule structure, which for chiral
chapters/theory/koszul_pair_structure.tex:169:\mathcal{A}^e = \mathcal{A} \boxtimes_{\mathcal{D}_X} \mathcal{A}^{\text{op}}
chapters/theory/koszul_pair_structure.tex:181:Equivalently, $\mathcal{M}$ is a module for the chiral enveloping algebra $\mathcal{A}^e$.
chapters/theory/koszul_pair_structure.tex:194:\item \emph{Locality}: If $\mathcal{A}$ satisfies locality, so does $\mathcal{A}^e$.
chapters/theory/koszul_pair_structure.tex:199:For (2): The chiral multiplication on $\mathcal{A}^e$ is given by:
chapters/theory/koszul_pair_structure.tex:216:To compute chiral Hochschild cohomology, we need a projective resolution of $\mathcal{A}$ as an $\mathcal{A}^e$-module.
chapters/theory/koszul_pair_structure.tex:234:The chiral bar complex is exact, providing a free resolution of $\mathcal{A}$ as an $\mathcal{A}^e$-module.
chapters/theory/koszul_pair_structure.tex:262:\ChirHoch^n(\mathcal{A}, M) = \text{Ext}^n_{\mathcal{A}^e}(\mathcal{A}, M)
chapters/theory/koszul_pair_structure.tex:267:To compute this explicitly, we apply $\text{Hom}_{\mathcal{A}^e}(-, M)$ to the bar resolution:
chapters/theory/koszul_pair_structure.tex:300:\emph{Step 1}: An $\mathcal{A}^e$-linear map $f: \mathcal{A}^{\otimes n+1} \to \mathcal{A}$ must satisfy:
 succeeded in 51ms:
chapters/theory/chiral_modules.tex:4224: (Soergel bimodule algebra), which computes the
chapters/theory/chiral_modules.tex:4598:bimodule. Theorem~\ref{thm:ds-koszul-intertwine} proves the
chapters/theory/chiral_center_theorem.tex:1941:For the polynomial vertex algebra on one generator, the bimodule
chapters/theory/chiral_center_theorem.tex:1946:(the Koszul resolution of the diagonal bimodule).
chapters/theory/chiral_center_theorem.tex:2039:The Koszul resolution of the diagonal bimodule takes the form
chapters/theory/chiral_hochschild_koszul.tex:81:is a $\mathcal{D}_X$-bimodule map.
chapters/theory/chiral_hochschild_koszul.tex:4681:An $\mathcal{A}^e$-linear map must commute with the bimodule structure, which for chiral
chapters/theory/e1_modular_koszul.tex:2117:For every genus~$g$ and complete $\cA$-bimodule~$M$, the
chapters/theory/e1_modular_koszul.tex:2138:perturbation preserves the bimodule-bicomodule equivalence.
chapters/theory/en_koszul_duality.tex:1585: right module over $\cO^{\mathsf{c}}$ and a bimodule over the
chapters/theory/en_koszul_duality.tex:1736:$\cO^{\mathsf{o}}$-bimodule via the mixed composition maps.
chapters/theory/en_koszul_duality.tex:1763:\textup{(}b\textup{)} $\cO^{\mathsf{o}}$-bimodule equivariance
chapters/theory/en_koszul_duality.tex:1860:further closed inputs) and open-sector bimodule equivariance
chapters/theory/en_koszul_duality.tex:1872:$\FM_k(\bC)$ of such $E_1$-endomorphisms. The open-sector bimodule
chapters/theory/en_koszul_duality.tex:1900:The open-sector bimodule condition ensures that the evaluation
chapters/theory/en_koszul_duality.tex:2540:bimodules), $\varphi(b) = \varphi'(b)$ for all $b$,
chapters/theory/koszul_pair_structure.tex:174:\begin{definition}[Chiral bimodule]\label{def:chiral-bimodule}
chapters/theory/koszul_pair_structure.tex:175:An \emph{$\mathcal{A}$-bimodule} (in the chiral sense) is a $\mathcal{D}_X$-module $\mathcal{M}$ equipped with a left chiral action $\mu_L\colon j_*j^*(\mathcal{A} \boxtimes \mathcal{M}) \to \Delta_! \mathcal{M}$ and a right chiral action $\mu_R\colon j_*j^*(\mathcal{M} \boxtimes \mathcal{A}) \to \Delta_! \mathcal{M}$ satisfying the associativity and compatibility conditions:
chapters/theory/koszul_pair_structure.tex:260:The \emph{chiral Hochschild cohomology} of $\mathcal{A}$ with coefficients in an $\mathcal{A}$-bimodule $M$ is:
chapters/theory/koszul_pair_structure.tex:1837:equipped with its coproduct on both sides) as the slab bimodule

thinking
**Inspecting definitions in document**

I noticed that there are definitions in `koszul_pair_structure.tex` that I should look into. I'll focus on lines 169-267, where I can find the definition of chiral bimodule and chiral HH as Ext^n_{A^e}(A,M). This might help salvage part of theorem 4657 later on. I think I should dig into it a bit more to see how it all connects!
exec
/bin/zsh -lc "nl -ba chapters/theory/koszul_pair_structure.tex | sed -n '160,272p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   160	% ================================================================
   161	
   162	\section{Chiral Hochschild cohomology: construction from first principles}
   163	
   164	\subsection{The chiral enveloping algebra}
   165	
   166	\begin{definition}[Chiral enveloping algebra]
   167	For a chiral algebra $\mathcal{A}$ on a smooth curve $X$, the \emph{chiral enveloping algebra} is:
   168	\[
   169	\mathcal{A}^e = \mathcal{A} \boxtimes_{\mathcal{D}_X} \mathcal{A}^{\text{op}}
   170	\]
   171	where $\boxtimes_{\mathcal{D}_X}$ is the chiral tensor product over the sheaf of differential operators and $\mathcal{A}^{\text{op}}$ has the opposite chiral multiplication $Y^{\text{op}}(a,b) = Y(b,a)$.
   172	\end{definition}
   173	
   174	\begin{definition}[Chiral bimodule]\label{def:chiral-bimodule}
   175	An \emph{$\mathcal{A}$-bimodule} (in the chiral sense) is a $\mathcal{D}_X$-module $\mathcal{M}$ equipped with a left chiral action $\mu_L\colon j_*j^*(\mathcal{A} \boxtimes \mathcal{M}) \to \Delta_! \mathcal{M}$ and a right chiral action $\mu_R\colon j_*j^*(\mathcal{M} \boxtimes \mathcal{A}) \to \Delta_! \mathcal{M}$ satisfying the associativity and compatibility conditions:
   176	\begin{enumerate}
   177	\item Left associativity: $\mu_L \circ (\mathrm{id}_\mathcal{A} \boxtimes \mu_L) = \mu_L \circ (\mu_\mathcal{A} \boxtimes \mathrm{id}_\mathcal{M})$ (as chiral operations on $\mathcal{A} \boxtimes \mathcal{A} \boxtimes \mathcal{M}$);
   178	\item Right associativity (analogously);
   179	\item Left-right compatibility: $\mu_L \circ (\mathrm{id}_\mathcal{A} \boxtimes \mu_R) = \mu_R \circ (\mu_L \boxtimes \mathrm{id}_\mathcal{A})$.

thinking
**Inspecting theorem continuation**

I think I need to dig into the theorem continuation between sections 269 to 300. It's important to ensure I understand the connections and implications of these sections correctly. There might be nuances and details that could change my perspective or understanding. I'll take a closer look to clarify everything. I want to make sure I'm on the right track as I analyze this information!
exec
/bin/zsh -lc "nl -ba chapters/theory/koszul_pair_structure.tex | sed -n '269,330p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
   269	\begin{theorem}[Chiral Hochschild complex; \ClaimStatusProvedHere]
   270	\label{thm:chiral-hochschild-complex}
   271	The chiral Hochschild cohomology is computed by the complex:
   272	\[
   273	0 \to \text{Hom}_{\mathcal{D}_X}(\mathcal{A}, M) \xrightarrow{\delta_0} \text{Hom}_{\mathcal{D}_X}(\mathcal{A}^{\otimes 2}, M) \xrightarrow{\delta_1} \text{Hom}_{\mathcal{D}_X}(\mathcal{A}^{\otimes 3}, M) \to \cdots
   274	\]
   275	where the differential $\delta_n$ is:
   276	\begin{align}
   277	(\delta_n f)(a_0, \ldots, a_{n+1}) = &Y(a_0, f(a_1, \ldots, a_{n+1})) \\
   278	&+ \sum_{i=1}^n (-1)^i f(a_0, \ldots, Y(a_i, a_{i+1}), \ldots, a_{n+1}) \\
   279	&+ (-1)^{n+1} Y(f(a_0, \ldots, a_n), a_{n+1})
   280	\end{align}
   281	\end{theorem}
   282	\begin{proof}
   283	Apply $\mathrm{Hom}_{\mathcal{D}_X}(-, \mathcal{A})$ to the bar resolution (Theorem~\ref{thm:chiral-bar-resolution-exact}); the stated differentials $\delta_n$ are the induced maps on $\mathrm{Hom}$ spaces.
   284	\end{proof}
   285	
   286	\subsection{Geometric realization via configuration spaces}
   287	
   288	\begin{theorem}[Geometric model of chiral Hochschild cohomology; \ClaimStatusProvedHere]

thinking
**Clarifying degree relationships**

I’m thinking about how the degree p corresponds to p+1 factors, and I'm considering the configuration space, which might be \overline C_{p+1}. However, theorem H seems to involve p+2, which feels like another off-by-one issue. I guess I need to reconcile these relationships carefully since they might influence how I interpret the overall context. Just trying to piece together these mathematical concepts accurately!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1100,1120p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1100	\end{conjecture}
  1101	
  1102	\begin{remark}[Identifying the obstruction space]
  1103	\label{rem:mc-smoothness-pbw}
  1104	The twisted cohomology
  1105	$H^2(\gAmod, \operatorname{ad}(\Theta_{\cA}))$ admits a direct
  1106	identification.
  1107	At genus~$0$, the $(g,n) = (0,3)$ component of the
  1108	$\operatorname{ad}(\Theta_{\cA})$-twisted complex is
  1109	$\ChirHoch^2(\cA)$
  1110	(Corollary~\ref{cor:def-obs-exchange-genus0}), and for a
  1111	Koszul algebra this equals
  1112	$Z(\cA^!)^\vee \otimes \omega_X$: a finite-dimensional space
  1113	completely controlled by the Koszul dual.
  1114	
  1115	At genus~$g \geq 1$, the contributions come from the modular bar
  1116	complex. The modular Koszulness axiom MK3 forces the bar spectral
  1117	sequence to collapse at~$E_1$ in all bidegrees, which kills the
  1118	higher-genus components of
  1119	$H^2(\gAmod, \operatorname{ad}(\Theta_{\cA}))$.












thinking
**Fixing mathematical arguments**

I'm sorting through some mathematical proofs and realizing that I need to either work on currents and demonstrate the Stokes/residue identity or just eliminate that argument. For the convergence claim regarding the Hochschild spectral sequence, it lacks essential filtration hypotheses. I need to add a theorem to prove the required properties or restrict the framework. There’s also a need to address claim-surface drift with concordance, maybe by revisiting the labeling of local theorems. This is definitely relevant.
thinking
**Verifying references in theorems**

I’m reviewing theorem references, particularly the Hochschild-Bar-Cobar citation, which cites the wrong definition for a single chiral Koszul algebra. I’ll need to correct this by citing the appropriate definition. I wonder if larger findings might already address this, so I might combine it with the scope mismatch. I should check specific lines around the theorem to see if there are any duplicate labels or unresolved references. It’s essential to ensure there are no false positives in my findings.
thinking
**Identifying definition conflicts and issues**

I'm finding incompatible definitions in my work. For instance, I see local definitions for chiral algebra and differing terms in theorem references. The canonical sources also present variations in how chirality is expressed, which raises questions about consistency.

Additionally, there’s an issue with the spectral sequence not being constructed properly, as definitions use degree n cochains, but related theorems suggest a double complex that doesn't align. I think I should clarify these discrepancies thoroughly to ensure accurate interpretations.
thinking
**Determining file count**

I need to confirm how many files I've read. I’m considering saying something like “Checked: 12” to indicate the count, but I might want to get an exact number if that's available. It could be helpful to clarify and ensure the user knows precisely what I’ve counted. Keeping it exact sounds better, so I’ll adjust my approach if necessary! It’s all about providing the user with accurate and clear information.
thinking
**Considering theorem adjustments**

I'm looking at the bar-cobar resolution with duplicate theorem surfaces 324 and 4610. I need to check if `ClaimStatusProvedHere` on the `hochschild-spectral-sequence` theorem should be downgraded. Since the user wants an exact fix, if the proposition isn't supported, I might suggest replacing `\begin{theorem}` with `\begin{remark}` and removing `\ClaimStatusProvedHere`, or adding something like "Assume a comparison quasi-isomorphism" to clarify the fix. I'll keep it concise and actionable!
thinking
**Clarifying theorem modifications**

I can provide concrete changes. For the spectral sequence, I need to replace lines 145-156 with `C^{p,\bullet}_{ch}(A):=RΓ(\overline C_{p+2}(X), \mathcal F_p)` where \mathcal F_p involves some other components, and I’ll rewrite theorems 362-372 accordingly. For the theorem H statement, I should change the hypothesis to specify that we're dealing with a chiral Koszul pair. I also need to mention deleting lines 607-691 from the second proof as an exact fix, which is straightforward! For `ω_X`, I need to replace `⊗ω_X` everywhere in the theorem regarding vector-space values.
thinking
**Organizing findings by severity**

I want to make sure the findings are ordered by severity, and I think I should compress from 15 to 12 to avoid having too many. My goal is to keep the final count under 70 lines, which feels manageable with 12 findings.

I’ll consider the following potential findings: critical ambiguities, unsupported definitions, concentration issues, and mismatches in theorems. It seems I might combine some claims, like the surface drift with the unconditional claim. I just need to keep refining this until it’s clear!
thinking
**Refining findings for clarity**

I'm thinking it might be better to include concordance drift instead of just "unconditional," since that feels more severe—especially with the theorem H alias mismatch. The user asked specifically for a theorem H audit. 

I could potentially combine "unconditional" into finding 11. This would look like: a medium finding about the growth theorem overstating palindromic duality. For finding 12, I should tackle theorem-H alias drift and possibly add the current-model issue. However, the latter might be more relevant, so I need to make a decision!
thinking
**Planning detailed findings**

Since the user mentioned that everything missing—like definitions and unresolved references—counts as a finding, I realize that the claim-surface drift feels less foundational. I need to include the current-model issue, and perhaps I could mention concordance drift in the summary.

They asked for specific findings, but since I might still manage 13, I think it could work! With each finding being around 3-5 lines, totaling about 60 lines sounds reasonable. I'll focus on producing those 13 findings.
thinking
**Evaluating proof issues**

I'm noticing a problem in the proof involving the identity `\{d_{\mathrm{fact}},d_{\mathrm{config}}\}=0`. It seems to switch from logarithmic forms to a boundary-supported current identity for `d_{\mathrm{dR}}\eta_{12}` without clearly defining the current model on `\overline C_{n+2}(X)` or proving the Stokes/residue formula that it references. I need to either work with currents explicitly and establish the boundary identity beforehand or eliminate this argument and reconstruct the spectral sequence from derived global sections, adjusting the vertical differential accordingly.
thinking
**Organizing findings for clarity**

I think I can keep both hidden perfection and concordance drift. I realize I need to summarize my findings from 14 and check those specific lines: 145-149 and 360-372 for any formatting issues. The verdict is a fail, but I want to make it clear. I plan to use flat bullets for the findings, and I could bold the summary header. It looks like a structured approach with simple bullet points will work best here.
thinking
**Auditing results clearly**

I'm thinking the audit results are inherently list-shaped, so using bullets makes sense. I might mention that not all issues are independent since many collapse under a canonical definition, but each finding is distinct. It might not be necessary, though. I need to ensure that I avoid ungrounded claims, like labeling something a "false theorem"; I can call it "unsupported" based on the contents. Before finalizing, I could consider updating the plan.
codex
The re-verification pass is done. The surviving findings are the ones where the file demonstrably changes models or hypotheses without a comparison theorem, or where the cited source says something different from what this proof claims.
Plan update
  ✓ Map the theorem-H lane and every local dependency/imported label
  ✓ Check whether the Hochschild/bar models used in the file are consistently defined and compared
  ✓ Test the bar-degree spectral sequence setup: bicomplex, filtration, differentials, convergence
  ✓ Check whether concentration in {0,1,2} actually follows from the stated spectral sequence
  ✓ Assemble only findings that survive re-verification against exact lines and state exact fixes
codex
- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:145-156 — PROBLEM: This file defines `C^n_{\text{chiral}}(\mathcal A)` as global sections on `\overline C_{n+2}(X)`, but the canonical Hochschild source already says this chapter should cite its definitions from `chapters/theory/hochschild_cohomology.tex:42-64,76-83,469-489`, and `chapters/theory/koszul_pair_structure.tex:259-295` gives yet another `A^e`/bar-resolution model. No comparison theorem is supplied, so “the chiral Hochschild complex” is ambiguous on the theorem-H surface. FIX: Delete the local redefinition at 145-156 and replace it by a citation to the canonical definition (`\ref{def:chiral-hochschild-derived}` or `\ref{thm:geometric-chiral-hochschild}`), then insert one explicit comparison proposition proving the model used here is quasi-isomorphic to that canonical model.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:145-149,362-372 — PROBLEM: The stated spectral sequence needs independent indices `(bar degree, sheaf-cohomology degree)`, but the local cochain definition hardwires degree `n` to `\Omega^n`, and the proof later invents `\ChirHoch^{m,*}` and a vertical `d_{\mathrm{sheaf}}` that were never defined. There is no actual bicomplex. FIX: Redefine the complex as either `C^{p,\bullet}_{\mathrm ch}(\mathcal A):=R\Gamma(\overline C_{p+2}(X),\mathcal F_p)` with `\mathcal F_p=j_*j^*\mathcal A^{\boxtimes(p+2)}\otimes\Omega^p_{\log}`, or as a genuine `C^{p,q}` bicomplex with explicit bidegrees and differentials; then restate Theorem `thm:hochschild-spectral-sequence` in that repaired model.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:324-358 — PROBLEM: `thm:hochschild-bar-cobar` does not prove what it claims. Step 3 says `\mathrm{Ext}^n_{\mathrm{ChirAlg}}(\mathcal A,\mathcal A)=\ChirHoch^n(\mathcal A)` “by definition,” but the loaded definitions in the files actually read define chiral Hochschild cohomology as `RHom_{\mathcal D_X}(\barBgeom(\mathcal A),M)` or `\mathrm{Ext}_{\mathcal A^e}`. FIX: Either insert a proved comparison theorem identifying `RHom_{\mathrm{ChirAlg}}(\Omega^{\mathrm ch}\bar B^{\mathrm ch}(\mathcal A),\mathcal A)` with the canonical Hochschild complex, or downgrade 324-358 from `\ClaimStatusProvedHere` to a remark/conjecture.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:583-585,623-635 — PROBLEM: Theorem H is stated for a single “chiral Koszul datum” via `def:chiral-koszul-morphism`, but the proof immediately uses Verdier-compatible identifications that only exist for a full chiral Koszul pair from `def:chiral-koszul-pair`. The statement is stronger than the proof. FIX: Change the theorem hypothesis to `Let (\cA,\cA^!) be a chiral Koszul pair (Definition~\ref{def:chiral-koszul-pair})`, or insert a prior proposition constructing such a pair from the stated datum and proving the needed Verdier compatibility.

- [CRITICAL] chapters/theory/chiral_hochschild_koszul.tex:538-574 — PROBLEM: `lem:chirhoch-descent` is the linchpin of the first proof, but its proof never establishes `\ChirHoch^\bullet(\cA)\cong(\mathbb D_{\Ran}\bar B^{\mathrm ch}(\cA))_\Sigma`. The cited Theorem A (`chapters/theory/chiral_koszul_pairs.tex:3638-3685`) identifies `\mathbb D_{\Ran}\bar B_X(\cA_1)` with the opposite algebra in a Koszul pair, not with Hochschild self-Ext. FIX: Remove this lemma from the proof chain and replace it with a separate comparison theorem from the canonical Hochschild definition to the Verdier-dual bar model.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:497-500,599-603 — PROBLEM: The proof says bar concentration forces the surviving diagonal `p=q`, but the cited theorem says `H^{p,q}(\bar B^{\mathrm ch}(\cA_1))=0` for `q\neq 0` (`chapters/theory/chiral_koszul_pairs.tex:1120-1128`). That is the `q=0` axis, not the diagonal. FIX: Replace every `p=q` claim in the theorem-H lane by `q=0`, then redo the degree bookkeeping with total degree `p+q`.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:362-372,751-767 — PROBLEM: The file advertises a spectral-sequence route to Theorem H, but the actual `{0,1,2}` concentration proof never uses `thm:hochschild-spectral-sequence`; it is proved instead from negative `Ext` vanishing plus the already-established duality theorem. FIX: Either repair the spectral sequence and derive concentration from it, or rewrite the chapter so it no longer claims the spectral sequence is what proves concentration.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:596-604,778-785 — PROBLEM: `\ChirHoch^n(\cA)` is treated as a vector-space-valued cohomology theory throughout the file, but Theorem H tensors it with the line bundle `\omega_X`, and line 778 then treats that bundle as dimension-neutral. The object type changes mid-proof. FIX: Choose one model. If `\ChirHoch^n` is a complex of vector spaces, replace `\otimes\omega_X` by a one-dimensional dualizing vector space after taking global sections. If it is a `\mathcal D_X`-module, restate the theorem in that category and stop taking plain dimensions without applying `R\Gamma` or a fiber functor.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:674-691 — PROBLEM: The second proof invokes `thm:e1-module-koszul-duality`, but the source file explicitly says its extension to arbitrary chiral Koszul pairs is not proved (`chapters/theory/chiral_koszul_pairs.tex:5160-5169,5174-5188`). This proof uses it outside its proved scope. FIX: Delete the second proof, or rewrite it as a separately scoped proposition restricted to the complete/conilpotent `E_1` lane.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:4598-4718 — PROBLEM: The file reopens the theorem-H surface with a second incompatible setup: first `\mathrm{Hom}_{\mathsf{Alg}}(\Omega\bar B(\mathcal A),\mathcal A)`, then `\mathrm{Hom}_{\mathcal A^e}(\mathcal A^{\otimes n+2},\mathcal A)`, then a configuration-space formula with `\mathcal H om_{\mathcal D_X}`. None are compared to the earlier model. FIX: Delete 4598-4718 and replace it with cross-references to the canonical theorem surfaces, or add explicit comparison propositions and keep only one definition after those comparisons.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:716-729,742-747 — PROBLEM: The growth theorem takes `\dim Z(\cA)`, `\dim \ChirHoch^1(\cA)`, and a Hilbert series without assuming those spaces are finite-dimensional, then says the palindromic identity holds “unconditionally” even though it is derived from Theorem H on the quadratic Koszul locus. FIX: Add a finite-dimensionality hypothesis or reformulate the theorem in a Grothendieck/completed-character setting, and replace “unconditionally” by “under the hypotheses of Theorem~\ref{thm:main-koszul-hoch}”.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:282-289 — PROBLEM: The proof of `\{d_{\mathrm{fact}},d_{\mathrm{config}}\}=0` silently switches from logarithmic forms to a boundary-supported current identity for `d_{\mathrm{dR}}\eta_{12}` without defining a current model on `\overline C_{n+2}(X)` or proving the Stokes/residue formula it uses. FIX: Either work explicitly in currents and prove that boundary identity before invoking it, or remove this argument and build the vertical direction from derived global sections instead of `d_{\mathrm{dR}}`.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:642-646 — PROBLEM: The first proof assumes, without imported justification, that each bar summand is a perfect `\Sigma_n`-equivariant `\mathcal D`-module and that Verdier duality commutes with finite `\Sigma_n`-coinvariants. Those are hidden hypotheses, not proved inputs. FIX: Add a lemma proving holonomicity/perfection of the relevant bar summands and the duality/coinvariants interchange, or add them as explicit hypotheses to Theorem H.

- [MEDIUM] chapters/theory/chiral_hochschild_koszul.tex:577-605,701-703 — PROBLEM: This file labels two local statements as “Theorem H”, but the concordance fixes Theorem H to `thm:w-algebra-hochschild`, `thm:virasoro-hochschild`, `thm:critical-level-cohomology`, and `prop:chirhoch1-affine-km` (`chapters/connections/concordance.tex:64-71`). The theorem surface is drifting. FIX: Either update the concordance so `thm:main-koszul-hoch` and `thm:hochschild-polynomial-growth` become the canonical theorem-H anchors, or stop calling these local statements “Theorem H”.

## Summary
Checked: 14 | Findings: 14 | Verdict: FAIL
tokens used
155,201
