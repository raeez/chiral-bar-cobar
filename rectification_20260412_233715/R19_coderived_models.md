# R19_coderived_models (70s)



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
session id: 019d83b2-f126-74f0-a928-aea46af37160
--------
user
<task>
You are a RECTIFICATION agent for a research mathematics manuscript on operadic Koszul duality.
Your mission: fix the specific findings below with the STRONGEST technical choice.
Hierarchy: (1) strengthen proof > (2) add missing lemma > (3) narrow claim to match proof > (4) mark conditional.
NEVER weaken when you can strengthen. NEVER leave a gap unfixed.
</task>

<action_safety>
Only edit the specific file(s) assigned. Do not touch other files.
Make the MINIMUM truthful edit that resolves each finding.
After each edit, re-read surrounding context to verify coherence.
</action_safety>

<verification_loop>
After all edits, re-read the modified sections and verify:
1. Each finding is resolved
2. No new inconsistencies introduced
3. Theorem status tags match the actual proof status
4. All \ref and \label are valid
</verification_loop>

<completeness_contract>
Address EVERY finding listed. Do not stop at the first fix.
For each finding, state: FIXED (how) or CANNOT_FIX (why, what narrower claim survives).
</completeness_contract>

<structured_output_contract>
End with:
## Rectification Summary
- [FIXED] finding — what was done
- [NARROWED] finding — claim narrowed to X
- [CONDITIONAL] finding — marked conditional on Y
- [BLOCKED] finding — cannot fix because Z
</structured_output_contract>


TARGET: chapters/theory/coderived_models.tex

FINDINGS TO FIX:

1. [CRITICAL T12] Lines ~75, ~545: The coderived category is defined as Verdier quotient
   by coacyclic objects. But bv_brst.tex:1945 treats it as "boundaries mod Im(d)".
   FIX: Verify the definition here is correct and consistent. If it is, the bv_brst proof
   is using the wrong characterization.

2. [CRITICAL T02] Lines ~247-270: prop:coderived-adequacy(a) invokes thm:higher-genus-inversion,
   creating circular dependency.
   FIX: Break the circularity. Prove coderived-adequacy independently, or mark it conditional.

Read the file, verify both findings, fix.
mcp startup: no servers
codex
Using `beilinson-rectify` for the local theorem repair and `claim-surface-sync` only as a consistency check within the target file. I’m reading the required repo invariants first, then the assigned file and the cited dependency surface to verify both findings before I edit.
exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 succeeded in 50ms:
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
I have the repo invariants loaded. Next I’m reading the target file around the two flagged surfaces, plus the cited dependency blocks in `bv_brst.tex` and the inversion theorem, to decide whether this can be strengthened locally or must be marked conditional.
exec
/bin/zsh -lc "rg -n \"label\\{thm:higher-genus-inversion\\}|higher-genus-inversion|coderived-adequacy|coacyclic|coderived\" chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,360p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1900,1985p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"coderived|coacyclic|prop:coderived-adequacy|thm:higher-genus-inversion|Verdier quotient|boundaries mod|Im\\(d\\)\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,660p' chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/existence_criteria.tex:126:coderived/contraderived comparison
chapters/theory/chiral_modules.tex:510:case, the appropriate analogues live in Positselski's coderived/curved
chapters/theory/chiral_koszul_pairs.tex:274:provisional coderived category
chapters/theory/chiral_koszul_pairs.tex:276:(Appendix~\ref{sec:coderived-models}),
chapters/theory/chiral_koszul_pairs.tex:5964: (Theorem~\ref{thm:higher-genus-inversion}) is
chapters/theory/chiral_hochschild_koszul.tex:696:(Theorem~\ref{thm:higher-genus-inversion}) and the Kodaira--Spencer map
chapters/theory/chiral_hochschild_koszul.tex:3547: \textup{(}Theorem~\textup{\ref{thm:higher-genus-inversion})}.
chapters/theory/chiral_hochschild_koszul.tex:3600:(Theorem~\ref{thm:higher-genus-inversion}), which exchanges
chapters/theory/chiral_hochschild_koszul.tex:5357:(Theorem~\ref{thm:higher-genus-inversion}) and perfectness
chapters/theory/higher_genus_complementarity.tex:3390: coderived
chapters/theory/higher_genus_complementarity.tex:4130:\begin{theorem}[Higher genus inversion; \ClaimStatusProvedHere]\label{thm:higher-genus-inversion}
chapters/theory/higher_genus_complementarity.tex:4189:\begin{remark}[Off-locus coderived continuation kept separate]
chapters/theory/higher_genus_complementarity.tex:4199:coderived category
chapters/theory/higher_genus_complementarity.tex:4201:left to the separate coderived-model formalism
chapters/theory/higher_genus_complementarity.tex:4202:\textup{(}Definition~\textup{\ref{def:provisional-coderived}}\textup{)}
chapters/theory/higher_genus_complementarity.tex:4204:Theorem~\ref{thm:higher-genus-inversion}, so no circular dependence on
chapters/theory/higher_genus_complementarity.tex:4205:Proposition~\ref{prop:coderived-adequacy}(a) remains.
chapters/theory/higher_genus_complementarity.tex:4300:The replacement is the coderived factorization co-contra comparison on
chapters/theory/higher_genus_complementarity.tex:4448:(iii)~the coderived category
chapters/theory/higher_genus_complementarity.tex:5265:inversion (Theorem~\ref{thm:higher-genus-inversion}),
 succeeded in 51ms:
\[
 \delta_r^{\mathrm{harm}}
 \;=\;
 c_r(\cA) \cdot m_0^{\lfloor r/2 \rfloor - 1}
 \qquad\text{for every } r \geq 4;
\]
\item each~$f_g$ is a weak equivalence in the sense of
 Definition~\ref{def:curved-weak-equiv}.
\end{enumerate}
Then the genus-$g$ BV complex and bar complex become isomorphic in
the provisional coderived category
$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$, hence in the
coderived category $D^{\mathrm{co}}(\cA)$:
\[
 C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
 \;\simeq_{D^{\mathrm{co}}}\;
 B^{(g)}(\cA)
 \qquad\text{for all } g \geq 0.
\]
In particular, a proof of \textup{(i)} together with the coacyclicity
 succeeded in 51ms:
3:\label{app:coderived}
4:\index{coderived category|textbf}
10:Positselski's theory of coderived and contraderived
14:\S\ref{subsec:chiral-coderived-contraderived}.
17:\label{subsec:coderived-abstract}
20:(for the coderived case) or exact direct products
57:\label{def:coacyclic-contraacyclic}
58:\index{coacyclic object|textbf}
62:\item A CDG-comodule $M$ is \emph{coacyclic} if it belongs to the
76:\label{def:coderived-contraderived-abstract}
77:\index{coderived category!abstract definition|textbf}
79:The \emph{coderived category} and \emph{contraderived category}
80:of a CDG-coalgebra $(C, d, h)$ are the Verdier quotients:
85: \label{eq:coderived-abstract}\\
93:object is coacyclic (resp.\ contraacyclic), so there are natural
126:\index{conilpotent coalgebra!coderived reduction}
130:CDG-comodule is coacyclic, so the coderived category coincides
143:the coderived category reduces to the ordinary derived
149:\label{rem:coderived-bar-cobar}
150:\index{bar-cobar adjunction!coderived formulation}
 succeeded in 51ms:

\section{Coderived and contraderived categories}
\label{app:coderived}
\index{coderived category|textbf}
\index{contraderived category|textbf}

The bar-cobar adjunction at higher genus produces curved complexes
($d^2 \neq 0$), for which ordinary cohomological derived methods
are no longer the right invariant.
Positselski's theory of coderived and contraderived
categories~\cite{Positselski11} provides the correct
replacement. This appendix collects the definitions and key results
needed in this monograph; the chiral specialization appears in
\S\ref{subsec:chiral-coderived-contraderived}.

\subsection{Abstract definitions}
\label{subsec:coderived-abstract}

Let $\mathsf{A}$ be an abelian category with exact direct sums
(for the coderived case) or exact direct products
 succeeded in 51ms:
\index{contraacyclic object!factorization|textbf}
Let $(C, d, h)$ be a curved factorization coalgebra.
\begin{enumerate}[label=\textup{(\roman*)}]
\item A factorization CDG-comodule~$M$ is \emph{coacyclic} if it
 belongs to the minimal thick subcategory
 $\mathrm{Acycl}^{\mathrm{co}}_{\mathrm{fact}}$
 of the factorization homotopy category
 $\mathrm{Hot}(C\text{-}\mathrm{CoFact})$
 that contains the totalizations of all short exact sequences of
 factorization CDG-comodules and is closed under
 infinite direct sums.
\item A factorization CDG-contramodule~$P$ is
 \emph{contraacyclic} if it belongs to the minimal thick
 subcategory
 $\mathrm{Acycl}^{\mathrm{ctr}}_{\mathrm{fact}}$
 with the dual closure: totalizations of exact triples and
 infinite direct products.
\end{enumerate}
This is the factorization analogue of
Definition~\ref{def:coacyclic-contraacyclic}. The factorization

thinking
**Inspecting theorem remarks**

I need to look into the higher_genus_complementarity theorem. It seems I should pay special attention to the part that states no circular dependence remains. Maybe the remark is stale and needs further investigation. I’ll take a closer look at both the theorem and the remark to clarify any misunderstandings. It’s important to ensure I fully grasp the implications here! So, let’s dive deeper into this!
codex
The local definition surface is consistent so far: `coderived_models.tex` defines coderived categories as Verdier quotients by coacyclics in both abstract and factorization versions. I’m now checking whether the target already has enough independent material to break the `prop:coderived-adequacy` cycle, or whether the honest fix is a conditional/local weakening.
exec
/bin/zsh -lc "sed -n '4110,4210p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1160,1205p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"boundary|Im\\(d\\)|boundaries mod|coacyclic injective|contractibility of coacyclic injectives|coacyclic if and only if\" chapters/connections/bv_brst.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '960,1210p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{align*}
where the last step uses the CDG relation $d^2 = h \ast (-)$ on
$M$ and~$N$. When $M = N$, this is $[h_M, f]$, which vanishes
on central endomorphisms.
\end{proof}

\begin{corollary}[Contractibility of coacyclic injectives; \ClaimStatusProvedHere]
\label{cor:coacyclic-injective-contractible}
\index{coacyclic!contractibility criterion|textbf}
Let $(C, d, h)$ be a conilpotent chiral CDG-coalgebra with
finite-dimensional graded pieces, and let $M$ be a chiral
CDG-comodule with injective underlying graded $C^{\#}$-comodule.
Then $M$ is coacyclic if and only if it admits a
\emph{contracting homotopy}: a degree~$-1$ graded
$C^{\#}$-comodule endomorphism $s \colon M \to M$ satisfying
\begin{equation}\label{eq:contracting-homotopy-cdg}
d_M \circ s + s \circ d_M \;=\; \mathrm{id}_M.
\end{equation}
\end{corollary}

 succeeded in 51ms:
tensor product of chain complexes over the ground field, which
preserves quasi-isomorphisms by K\"unneth. This yields the claim.
\end{proof}

\begin{lemma}[Extension across boundary; \ClaimStatusProvedHere]\label{lem:extension-across-boundary-qi}
Let $X$ be a stack with open-closed decomposition $X = U \sqcup Z$ (with
$j:U\hookrightarrow X$, $i:Z\hookrightarrow X$). For a morphism of complexes
$f:K\to L$ on $X$, if $j^*f$ and $i^*f$ are quasi-isomorphisms, then $f$ is a
quasi-isomorphism.
\end{lemma}

\begin{proof}
Let $C=\operatorname{Cone}(f)$. It suffices to prove $C$ is acyclic.
From $j^*f$ and $i^*f$ quasi-isomorphisms, $j^*C$ and $i^*C$ are acyclic.
Apply the localization triangle
\[j_!j^*C \longrightarrow C \longrightarrow i_*i^*C \xrightarrow{+1}.\]
Both outer terms are acyclic, hence $C$ is acyclic. Therefore $f$ is a
quasi-isomorphism.
\end{proof}

 succeeded in 51ms:
chapters/connections/bv_brst.tex:29:the bar differential collects OPE residues along FM boundary strata.
chapters/connections/bv_brst.tex:65:iterated residues on FM boundary strata
chapters/connections/bv_brst.tex:1259:The physical content (Gaiotto's framework, boundary chiral
chapters/connections/bv_brst.tex:1260:algebras, HT boundary conditions, W-algebras from Higgs branches)
chapters/connections/bv_brst.tex:1267:\label{rem:boundary-chiral-algebra-bv}%
chapters/connections/bv_brst.tex:1268:\label{rem:bar-cobar-ht-boundary}%
chapters/connections/bv_brst.tex:1844:non-separating boundary divisor
chapters/connections/bv_brst.tex:1872:\kappa / \operatorname{Im}(\tau)$ is not a coboundary
chapters/connections/bv_brst.tex:2002:using the bulk propagator, while the boundary theory is computed
chapters/connections/bv_brst.tex:2003:by the bar complex using the boundary OPE. The mismatch between
chapters/connections/bv_brst.tex:2004:bulk and boundary propagators at one loop ($g = 1$) is the
chapters/connections/bv_brst.tex:2035:and the algebraic bar construction of the boundary vertex algebra
chapters/connections/bv_brst.tex:2048:The holomorphic-topological boundary VOAs of twisted supergravity
chapters/connections/bv_brst.tex:2059:The boundary VOA of the Burns space consists of four $\beta\gamma$
chapters/connections/bv_brst.tex:2141:The boundary VOAs of twisted supergravity on the non-Calabi--Yau
chapters/connections/bv_brst.tex:2146: $H^{2}(\mathbb{F}_n, \mathbb{Z})$ has rank~$2$, so the boundary
chapters/connections/bv_brst.tex:2153: number of $\beta\gamma$ pairs in the boundary VOA, giving
chapters/connections/bv_brst.tex:2159: and the K3 boundary VOA carries $\kappa(\mathrm{K3}) = 24$
chapters/theory/bar_cobar_adjunction_inversion.tex:1166:\begin{corollary}[Contractibility of coacyclic injectives; \ClaimStatusProvedHere]
chapters/theory/bar_cobar_adjunction_inversion.tex:1172:Then $M$ is coacyclic if and only if it admits a
 succeeded in 52ms:
adjunction (which holds for holonomic $\mathcal{D}_X$-modules
by~\cite[Proposition~3.4.6]{BD04}), $\tilde{f}$ corresponds to a map
$M \to \mathrm{Hom}_{\mathcal{D}_X}(N, V)$ that is
$C$-colinear, i.e., an element of
$\mathrm{Cohom}_C^{\mathrm{ch}}(M, \mathrm{Hom}_{\mathcal{D}_X}(N, V))$.
The second isomorphism is analogous.
\end{proof}

\subsection{Coderived and contraderived categories}
\label{subsec:chiral-coderived-contraderived}

\begin{definition}[Coderived and contraderived categories]
\label{def:chiral-coderived}
\index{coderived category!chiral|textbf}
\index{contraderived category!chiral|textbf}
Let $(C, d, h)$ be a chiral CDG-coalgebra.

\emph{Exact triples.}
An exact triple of left chiral CDG-comodules is a short sequence
$0 \to L \to M \to N \to 0$ that is exact in the abelian category
codex
I found the cycle source: `higher_genus_complementarity.tex` already states the off-locus coderived upgrade is intentionally separate from `thm:higher-genus-inversion`. That means `prop:coderived-adequacy(a)` is stale and can be repaired locally without touching the theorem file. I’m checking the BV/BRST passage now to see whether it merely uses a null-homotopy criterion on injectives or actually misdefines the coderived category.
exec
/bin/zsh -lc "nl -ba chapters/connections/bv_brst.tex | sed -n '1930,1965p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1930	provisional coderived category:
  1931	Definition~\ref{def:curved-weak-equiv} identifies weak equivalences
  1932	as the morphisms inverted in
  1933	Definition~\ref{def:provisional-coderived}. Hence each~$f_g$
  1934	becomes an isomorphism in
  1935	$\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)$.
  1936	Proposition~\ref{prop:provisional-embedding} then identifies this
  1937	with an isomorphism in the full coderived category on the bounded-below
  1938	PBW-filtered surface treated in this chapter.
  1939	
  1940	Assumption~\textup{(i)} records the missing class~$\mathsf{M}$
  1941	mechanism isolated by
  1942	Proposition~\ref{prop:chain-level-three-obstructions}: it is the
  1943	candidate factorization that would allow one to verify
  1944	assumption~\textup{(ii)} from the harmonic-propagator analysis.
  1945	The chapter does not prove \textup{(i)} or the resulting
  1946	coacyclicity statement, so the coderived comparison remains
  1947	conditional.
  1948	\end{proof}
  1949	
exec
/bin/zsh -lc "rg -n \"Im\\(d\\)|\\\\operatorname\\{Im\\}\\(d\\)|boundaries|coboundary|cohomology class|homotopy category|coderived category\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1860,1955p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:Im\(d\)|\operatorname\{Im\}\(d\)|boundaries|coboundary|cohomology class|homotopy category|coderived category)
               ^^
error: unrecognized escape sequence
 succeeded in 51ms:
 & genus-$0$ chain; all-genera scalar & no interaction vertices \\
$\mathsf{L}$ \textup{(}affine KM\textup{)}
 & obstruction analysis favorable & Jacobi kills the cubic harmonic term \\
$\mathsf{C}$ \textup{(}$\beta\gamma$\textup{)}
 & genus-$1$ scalar obstruction analysis & harmonic decoupling \textup{(}Remark~\ref{rem:bv-bar-class-c-proof}\textup{)} \\
$\mathsf{M}$ \textup{(}Virasoro, $\cW_N$\textup{)}
 & unresolved at chain level & harmonic correction survives \\
\bottomrule
\end{tabular}
\end{center}
For class~$\mathsf{M}$, the quartic discrepancy
$\delta_4^{\mathrm{harm}} \propto Q^{\mathrm{contact}} \cdot
\kappa / \operatorname{Im}(\tau)$ is not a coboundary
in the ordinary chain complex. A coderived upgrade requires the
conditional package of Theorem~\ref{thm:bv-bar-coderived} below:
one must prove the curvature-factorization formula for the full
harmonic discrepancy and then prove that the resulting BV/bar
comparison map has coacyclic cone in the sense of
Definitions~\ref{def:coacyclic-fact} and~\ref{def:curved-weak-equiv}.
\end{remark}
codex
I’ve isolated the technical choice. The definition in `coderived_models.tex` is the standard Positselski one and matches the chiral definition in `bar_cobar_adjunction_inversion.tex`; the only “boundaries” criterion I can justify is the special injective/null-homotopy test, not a general definition. I’m reading the later uses of `prop:coderived-adequacy` now so I can patch the cycle without leaving stale downstream prose in this file.
exec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '660,720p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/coderived_models.tex | sed -n '780,920p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"prop:coderived-adequacy|Proposition~\\\\ref\\{prop:coderived-adequacy\\}|coderived-adequacy\" chapters/theory/coderived_models.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   660	\[
   661	\iota \colon
   662	\mathsf{D}^{\mathrm{co}}_{\mathrm{prov}}(X)
   663	\hookrightarrow
   664	D^{\mathrm{co}}(C\text{-}\mathrm{CoFact}).
   665	\]
   666	The essential image of~$\iota$ consists of those objects
   667	admitting a bounded-below filtration~$\mathcal{F}$ with
   668	$(\operatorname{gr}^0_{\mathcal{F}} d)^2 = 0$.
   669	\end{proposition}
   670	
   671	\begin{proof}
   672	\emph{Well-definedness.}
   673	A provisional weak equivalence
   674	(Definition~\ref{def:curved-weak-equiv}(i)) induces a
   675	quasi-isomorphism on associated graded. For bounded-below
   676	filtrations, this implies the cone is coacyclic on each
   677	stratum~$\operatorname{Ran}_n$ by
   678	Positselski~\cite[Proposition~3.5]{Positselski11} (a
   679	bounded-below spectral sequence with acyclic associated graded
 succeeded in 52ms:
243:\label{prop:coderived-adequacy}
695:(Proposition~\ref{prop:coderived-adequacy}(b)) provides the
 succeeded in 52ms:
   780	\Phi_{C_{U_1}}(M_1) \otimes \Phi_{C_{U_2}}(C_{U_2})
   781	\;\simeq\;
   782	\Phi_{C_{U_1}}(M_1),
   783	\]
   784	where the second isomorphism uses
   785	$\Phi_C(C) \simeq k$ (the endomorphisms of the regular comodule
   786	reduce to the ground field via the coaugmentation). The same
   787	holds for $\Psi$ by
   788	Lemma~\ref{lem:Phi-Psi-properties}(b)--(c). Hence the
   789	stratum-by-stratum equivalences~\eqref{eq:stratum-co-contra} are
   790	compatible with the factorization isomorphisms.
   791	
   792	\emph{Step~3: Assembly.}
   793	The factorization-compatible functors $\Phi$ and $\Psi$ preserve
   794	coacyclic and contraacyclic objects (since they do so on each
   795	stratum), hence descend to functors between the Verdier
   796	quotients~\eqref{eq:coderived-fact}--\eqref{eq:contraderived-fact}.
   797	The unit $\Psi \circ \Phi \to \mathrm{id}$ and counit
   798	$\Phi \circ \Psi \to \mathrm{id}$ restrict to isomorphisms on
   799	each stratum (by the chain-level theorem), hence are global
ERROR: exceeded retry limit, last status: 429 Too Many Requests, request id: 838b2739-62e0-425c-8fce-d178d615c8b2
tokens used
71,759
