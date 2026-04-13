# OA5_mc3_completion (408s)

- PROBLEM at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4320), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4375), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3758), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3986): part `(c)` is not proved from the stated hypotheses. `thm:pro-weyl-recovery` only identifies standards as `R\varprojlim W_m` inside the separated completion; it does not construct `\Phi` on an arbitrary `\mathcal D^{\mathrm{comp}}`, show `\Phi` commutes with those limits, or prove equivalence on the compact shifted-prefundamental core. The file itself still marks exactly that extension as conjectural in `conj:dk-compacts-completion` and as the “remaining packet” in `thm:mc3-type-a-resolution`. FIX: remove `(c)` from the proposition, or split the result into a proved proposition `(a)-(b)` plus a conditional/conjectural statement for DK extension. If `(c)` is kept, add an explicit extra hypothesis giving a colimit-preserving extension of `\Phi` to the compact core and prove its compatibility with the pro-Weyl limit construction.

- PROBLEM at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4355): Step 2 imports `thm:shifted-prefundamental-generation` from the separated completion and then concludes generation inside an arbitrary presentable completion `\mathcal D^{\mathrm{comp}}` without any comparison functor. The cited theorem proves the standard-object statement inside `\widehat D(\mathcal O^{\mathrm{sh}}_{\le 0})`, not inside every completion satisfying `(i)-(iii)`. FIX: after Step 1, cite the final conditional clause of `thm:shifted-prefundamental-generation` directly, since Step 1 already establishes its compact-object hypothesis; alternatively add a functor from the separated completion to `\mathcal D^{\mathrm{comp}}` that preserves the Baxter-generated thick subcategory.

- PROBLEM at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4393), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4425), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4433): the remark overstates both the “Ind-completion tautology” and the Mittag-Leffler reduction. Hypothesis `(i)` is stronger than “holds for `\operatorname{Ind}(D^b(\mathcal A))` by construction”; the text gives no reason that every weight piece of every ind-object has bounded cohomological amplitude. Likewise, the jump from compactness against filtered colimits to “equivalent to weightwise Ext stabilization” and then to a Mittag-Leffler condition on an inverse tower is asserted, not proved. FIX: rewrite this as a sufficient-criterion remark: `(ii)` and `(iii)` are tautological for Ind-completion, `(i)` needs separate verification or restriction to a weight-bounded subcategory, and the Francis-Gaitsgory discussion should be phrased as “if the completion is modeled by weightwise Mittag-Leffler towers, then compactness-preservation follows,” not as an equivalence.

Label check: `prop:completion-extension-weight-bounded` is unique across Vol I-III, and the `prop:` prefix matches the environment. No AP126, AP132, AP165, or AP113 issue appears in this inserted block. The status tag `\ClaimStatusProvedHere` is not defensible unless `(c)` is removed or downgraded.


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
session id: 019d8894-5186-7a53-b9cb-167da0f8ea4e
--------
user
<task>
You are a Beilinson rectification auditor. Read the RECENT changes to the assigned file.
These changes were written by automated mathematical research agents. Your job:
(1) Verify mathematical correctness of every new proposition and proof
(2) Check all labels are unique, environments match status tags
(3) Check no AP violations introduced (AP126, AP132, AP29, AP165, AP113)
(4) Flag any gaps, incorrect steps, or unjustified claims
For each finding: PROBLEM at file:line + FIX.
</task>
<grounding_rules>Ground every claim in the file contents you read.</grounding_rules>
<completeness_contract>Audit EVERY new proposition and proof in the file.</completeness_contract>


Audit prop:completion-extension-weight-bounded in chapters/examples/yangians_computations.tex. Verify: three hypotheses stated correctly, Neeman/BvdB argument, Ind-completion tautology, Mittag-Leffler reduction.
mcp startup: no servers

thinking
**Considering file exploration**

I think I need one explorer for recent file changes and another for ensuring label uniqueness. It seems like I could spawn parallel explorers for efficiency. However, I should still read the constitutional files myself. The instructions mention reading them before any substantive mathematical edits. Also, while the audit may not require changes, it still needs a review. So, it might be wise to use the explorer to summarize key files without re-reading code they cover.
codex
Using `deep-beilinson-audit` logic for this review. I’m first pulling the recent diff for [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex) and the required repo context files so the audit is grounded in the live claim surface, not memory.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
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


thinking
**Inspecting git changes**

I need to check the git diff result since I got no output from chunk ID f15f3e. It might be empty because the file is staged. I should consider using `git diff HEAD`. There’s a possibility of no unstaged changes if everything's been committed. I might inspect recent changes using `git log -p -n 1 -- file`. I need to find the proposition `prop:completion-extension-weight-bounded` in the file and examine surrounding lines. I might also use tools like rg and sed for this inspection.
codex
The worktree diff for this file is empty, so I’m treating “recent changes” as the latest committed edit to the target proposition and its proof. Next I’m reading the local block around `prop:completion-extension-weight-bounded`, then checking its label/status surface and any referenced lemmas/propositions it depends on.
exec
/bin/zsh -lc 'rg -n "completion-extension-weight-bounded|Mittag|Ind-completion|Neeman|Van den Bergh|BvdB|weight-bounded" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3188:Mittag--Leffler ($R^1 \varprojlim = 0$). Each $W_m$ lies in
3202:and Mittag--Leffler vanishing) depend only on the weight
3227:compact-generation mechanism of Neeman and Bondal--Van den Bergh; in
3724:inverse system is therefore Mittag--Leffler, so
3743:Mittag--Leffler condition: the transition maps
3815: $R\varprojlim W_m$, and R$^1$ vanishing via Mittag-Leffler.
3953: (3)~Mittag--Leffler ($R^1\varprojlim = 0$) on Weyl module
4019: separated completion, proved via Mittag--Leffler
4062: the Mittag--Leffler condition is verified (the transition maps
4274:\begin{proposition}[MC3 completion extension via weight-bounded
4276:\label{prop:completion-extension-weight-bounded}
4278:\index{compact generation!weight-bounded t-structure}
4346:Neeman~\cite[Thm.~2.1]{Neeman92}
4347:and Bondal--Van den Bergh~\cite[Cor.~3.1.2]{BondalVdB03}
4384:Ind-completion: a functor on compact objects extends uniquely,
4394:Ind-completion $\operatorname{Ind}(D^b(\mathcal{A}))$
4398:Ind-completion. The substantive content is
4403:For the Ind-completion
4409:This is the unconditional result: the Ind-completion of the shifted
4425:By the weight-bounded t-structure, this is equivalent to the statement
exec
/bin/zsh -lc "sed -n '4200,4385p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 55ms:
criterion for category~$\mathcal{O}$
\cite{Hernandez05, HJZ25}, and \textup{(c)}~the
Gautam--Toledano Laredo equivalence~\cite{GTL17}
identifying Drinfeld polynomial data between quantum
loop algebras and Yangians.
The new content is the observation
that these three inputs, combined with the character identity
(Proposition~\ref{prop:character-cg-all-types}), yield the
categorical CG decomposition for \emph{all} types, replacing
the minuscule hypothesis of
Proposition~\ref{prop:categorical-cg-typeA}.
The multiplicity-free property is not contained in a single
reference: for simply-laced types it follows from
$(q,t)$-character theory~\cite{Nakajima04}; for classical types
from explicit formulas~\cite{ChariMoura06}; for all types the
Frenkel--Mukhin algorithm~\cite{FrenkelMukhin01} computes the
$q$-character and confirms multiplicity-freeness.
The block criterion transfers from quantum affine to Yangian
because it is purely combinatorial, depending only on Drinfeld
polynomial data identified by~\cite{GTL17}.
exec
/bin/zsh -lc "rg -n \"label\\{prop:completion-extension-weight-bounded\\}\" /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git log --oneline --follow -- chapters/examples/yangians_computations.tex | head -n 12' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4276:\label{prop:completion-extension-weight-bounded}
 succeeded in 52ms:
a93cb61 MC3 completion extension: conditional proof via Neeman/BvdB compact generation (AP233 resolved)
eb521e0 Build artifacts, compute engines, audit reports, and standalone PDFs synchronised
56cd1ab Final sync: late-arriving frontier agent results
96e9a16 Session terminus: the 133-commit chiral quantum group programme
97bac39 Final wave 2 results: DS intertwining engine (57 tests), Miura universality at spin 4 (51 tests), quantum determinant centrality (74 tests), Z_3(k) closed form discovery, AP126 fix, conj:miura-cross-universality installed in standalone
95f2870 MC5 coderived rectification, Gerstenhaber brace fix, formula corrections (5 files)
ad75565 Standard landscape, Yangian-Drinfeld-Kohno synthesis, concordance constitution, and THQG degree normalisation (60 chapters)
02ce7e6 Yangian spectral parameter notation Y_hbar(g) -> Y_z^hbar(g), concordance micro-fix, build sync
c8116b5 Standard landscape: Yangian-Drinfeld-Kohno synthesis, Kac-Moody r-matrix normalisation, census fortification
b4eda52 Vol I mathematical content: AP142 local-global curve rectification, AP32 uniform-weight discipline, E1-first preface rewrite, bare kappa qualification across 55 chapters
137715e Vol I adversarial campaign: 513-agent audit, repair, and frontier expansion
65262ee Vol I theorem architecture: six load-bearing rewrites (A1-A6 + G7)
exec
/bin/zsh -lc "sed -n '4385,4465p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Lurie~\cite[Prop.~5.3.5.10]{HTT}\textup{)}.
\end{proof}

\begin{remark}[Characterization of the hypotheses]
\label{rem:completion-extension-hypotheses}
\index{MC3!completion extension!hypothesis analysis}
The three hypotheses isolate precisely the content of
Conjecture~\textup{\ref{conj:dk-compacts-completion}}.
Hypothesis~\ref{it:weight-compatible} is structural: it holds for the
Ind-completion $\operatorname{Ind}(D^b(\mathcal{A}))$
\textup{(}by construction\textup{)} and for any Francis--Gaitsgory
pro-nilpotent completion compatible with the weight grading.
Hypothesis~\ref{it:colimit-generation} holds by definition for any
Ind-completion. The substantive content is
hypothesis~\ref{it:compactness-preservation}: every bounded complex
with finite-length cohomology in~$\mathcal{A}$ must remain compact in
the chosen enhancement.

For the Ind-completion
$\mathcal{D}^{\mathrm{comp}} =
exec
/bin/zsh -lc "sed -n '4465,4545p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\medskip\noindent\emph{Channel~B \textup{(}Direct Baxter-locus
finiteness\textup{)}.}
On the Baxter locus $b = a - 1/2$, the short exact sequences from
the Baxter singular vectors give explicit filtrations.
Every compact object $C$ has bounded cohomological amplitude
\textup{(}by definition of compactness in a stable category with a
bounded t-structure, $C$ has finitely many nonzero cohomology
objects\textup{)}, and each cohomology object has a finite standard
filtration \textup{(}by the BGG theorem for highest-weight
categories\textup{)}. Each standard is resolved by a finite Baxter
filtration \textup{(}Step~2 of
Theorem~\ref{thm:shifted-prefundamental-generation}\textup{)}.
The composite filtration is therefore finite for every compact
object: the finiteness of the standard filtration at each
cohomological degree combines with the boundedness of the
cohomological amplitude to give a globally finite iterated filtration.

The two channels are independent and converge to the same conclusion.
Channel~A is categorical and type-independent once the hypotheses are
codex
I have the proposition block. Now I’m checking the exact statements of the four cited dependencies and the latest commit that introduced this block, because the proof’s validity hinges on whether those results actually provide compact generation, standard filtrations, and extension of `\Phi` on compacts.
collab spawn_agent(call_yEosX4lTZpGpbUxhoMRG6IdJ, prompt="Read the latest commit touching chapters/examples/yangians_computations.tex and inspect the block around prop:completion…")
mcp startup: no servers
spawn_agent(call_yEosX4lTZpGpbUxhoMRG6IdJ, prompt="Read the latest commit touching chapters/examples/yangians_computations.tex and inspect the block around prop:completion…") pending init:
  agent: 019d8895-1ebb-7053-b4bc-7ad8006448aa
exec
/bin/zsh -lc 'git show --stat --patch a93cb61 -- chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
commit a93cb61c827d9de3706c217075012e44bc5c2cb3
Author: Raeez Lorgat <raeez@momentum.inc>
Date:   Mon Apr 13 22:27:14 2026 +0200

    MC3 completion extension: conditional proof via Neeman/BvdB compact generation (AP233 resolved)
    
    prop:completion-extension-weight-bounded proves the MC3 completion extension
    (the passage from thick generation on bounded strata to compact generation of
    the completed Yangian category) conditional on three explicit, checkable hypotheses:
    
    (i) Weight-bounded t-structure: the weight decomposition extends to a right-bounded,
        weight-separated t-structure on D^comp.
    (ii) Colimit generation: D^comp generated under filtered colimits by im(D^b(A)).
    (iii) Compactness of image: bounded complexes with finite-length cohomology remain
         compact in D^comp.
    
    Under these: (a) compacts of D^comp = thick idempotent-complete closure of D^b(A),
    (b) D^comp = Loc<G_Bax> (localizing generation by Baxter seed), (c) DK functor
    extends to localizing equivalence.
    

Plan update
  → Identify latest commit touching chapters/examples/yangians_computations.tex and extract block around prop:completion-extension-weight-bounded for context
  • Locate statements for the referenced theorems/props elsewhere in repo to understand dependencies
  • Assess whether the proof of prop:completion-extension-weight-bounded is justified by those dependencies and summarize with citations
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && git log -n 1 --stat -- chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
commit a93cb61c827d9de3706c217075012e44bc5c2cb3
Author: Raeez Lorgat <raeez@momentum.inc>
Date:   Mon Apr 13 22:27:14 2026 +0200

    MC3 completion extension: conditional proof via Neeman/BvdB compact generation (AP233 resolved)
    
    prop:completion-extension-weight-bounded proves the MC3 completion extension
    (the passage from thick generation on bounded strata to compact generation of
    the completed Yangian category) conditional on three explicit, checkable hypotheses:
    
    (i) Weight-bounded t-structure: the weight decomposition extends to a right-bounded,
        weight-separated t-structure on D^comp.
    (ii) Colimit generation: D^comp generated under filtered colimits by im(D^b(A)).
    (iii) Compactness of image: bounded complexes with finite-length cohomology remain
         compact in D^comp.
    
    Under these: (a) compacts of D^comp = thick idempotent-complete closure of D^b(A),
    (b) D^comp = Loc<G_Bax> (localizing generation by Baxter seed), (c) DK functor
    extends to localizing equivalence.
    
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:completion-extension-weight-bounded" -n chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4276:\label{prop:completion-extension-weight-bounded}
4445:Proposition~\ref{prop:completion-extension-weight-bounded} converts
thinking
**Inspecting dependencies**

I need to inspect the dependency statements carefully. Maybe I could use the shell for parallel processing. I'll gather definitions around the referenced theorem labels and check their statuses. To do this effectively, I might want to use tools like `rg` and `sed`. It could also be useful to verify the exact line numbers for propositions, possibly using `nl -ba`. Let's gather all this information.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4200,4330p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
criterion for category~$\mathcal{O}$
\cite{Hernandez05, HJZ25}, and \textup{(c)}~the
Gautam--Toledano Laredo equivalence~\cite{GTL17}
identifying Drinfeld polynomial data between quantum
loop algebras and Yangians.
The new content is the observation
that these three inputs, combined with the character identity
(Proposition~\ref{prop:character-cg-all-types}), yield the
categorical CG decomposition for \emph{all} types, replacing
the minuscule hypothesis of
Proposition~\ref{prop:categorical-cg-typeA}.
The multiplicity-free property is not contained in a single
reference: for simply-laced types it follows from
$(q,t)$-character theory~\cite{Nakajima04}; for classical types
from explicit formulas~\cite{ChariMoura06}; for all types the
Frenkel--Mukhin algorithm~\cite{FrenkelMukhin01} computes the
$q$-character and confirms multiplicity-freeness.
The block criterion transfers from quantum affine to Yangian
because it is purely combinatorial, depending only on Drinfeld
polynomial data identified by~\cite{GTL17}.
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3320,3785p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "thm:eval-core-identification|thm:shifted-prefundamental-generation|prop:heart-capture-criterion|thm:pro-weyl-recovery|conj:dk-compacts-completion" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3320	type-$A$ statement on the Baxter-locus seed
  3321	$\{V_{\omega_i}(a)\}\cup\{L^-_{i,a-\frac{1}{2}}\}$.
  3322	The issue is therefore not set-theoretic coverage of the
  3323	prefundamental family: because $a \mapsto a-\tfrac{1}{2}$ is a
  3324	bijection, every negative prefundamental $L^-_{i,b}$ already appears
  3325	on that seed. The issue is the proof mechanism. Step~2 uses the
  3326	rank-$1$ singular vector on the hyperplane
  3327	\eqref{eq:baxter-spectral-constraint}; away from that hyperplane, the
  3328	present manuscript has no module-level replacement for the Baxter
  3329	companion.
  3330	
  3331	\smallskip\noindent\emph{Alternative generators and the deformation
  3332	route.}
  3333	The natural replacements are not new finite-dimensional modules, since
  3334	Corollary~\ref{cor:dk2-thick-generation-all-types} already shows that
  3335	fundamental evaluations generate only the evaluation core. The real
  3336	candidates are the asymptotic modules of the Kirillov--Reshetikhin
  3337	tower in the sense of \cite{HJZ25,Zhang24} and the Baxter--Rees family
  3338	$\mathcal{E}_i$ constructed later in this chapter.
  3339	Theorem~\ref{thm:yangian-generic-boundary-fibers} identifies its
 succeeded in 51ms:
2550:\label{prop:heart-capture-criterion}
2590:(Proposition~\ref{prop:heart-capture-criterion}) then gives
2769:\label{thm:eval-core-identification}
3072:\label{thm:shifted-prefundamental-generation}
3184:By Theorem~\ref{thm:pro-weyl-recovery}, every ordinary standard module
3237:Conjecture~\ref{conj:dk-compacts-completion}.
3258:\textup{(}Theorem~\textup{\ref{thm:shifted-prefundamental-generation}}\textup{)}
3272:Theorem~\ref{thm:shifted-prefundamental-generation} and
3288:Theorem~\ref{thm:shifted-prefundamental-generation} proves the
3302:\textup{(}Conjecture~\textup{\ref{conj:dk-compacts-completion}}\textup{)}.
3319:Theorem~\ref{thm:shifted-prefundamental-generation} proves the
3365:The completion step remains separate. Theorem~\ref{thm:shifted-prefundamental-generation}
3374:identification is exactly Conjecture~\ref{conj:dk-compacts-completion}.
3702:\label{thm:pro-weyl-recovery}
3717:evaluation core (Theorem~\ref{thm:eval-core-identification}).
3734:Theorem~\ref{thm:eval-core-identification}.
3740:Theorem~\ref{thm:pro-weyl-recovery} resolves the pro-Weyl packet.
3751:(Theorem~\ref{thm:eval-core-identification}).
3759:\label{conj:dk-compacts-completion}
3773:Conjecture~\ref{conj:dk-compacts-completion} remains the final
exec
/bin/zsh -lc 'rg -n "moreover|additionally|notably|crucially|remarkably|interestingly|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|landscape|journey|navigate|---|—" chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '4120,4465p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
4492:\label{sec:mc3-extension-landscape}
 succeeded in 51ms:
  4120	$q$-characters for all fundamental Kirillov--Reshetikhin
  4121	modules. For classical types, Chari--Moura~\cite{ChariMoura06}
  4122	give explicit closed-form $q$-character formulas confirming
  4123	multiplicity-freeness. For all types uniformly, the
  4124	Frenkel--Mukhin algorithm~\cite{FrenkelMukhin01} correctly
  4125	computes the $q$-character of every fundamental module
  4126	\textup{(}fundamental modules are \emph{special} in the sense
  4127	of~\cite{FrenkelMukhin01}, so the algorithm terminates with the
  4128	true $q$-character\textup{)}, and the output has all monomials
  4129	distinct.
  4130	
  4131	For the Yangian $Y_\hbar(\mathfrak{g})$, the analogous
  4132	multiplicity-free $\ell$-weight property follows from the
  4133	Gautam--Toledano Laredo equivalence~\cite{GTL17}
  4134	between the categories of finite-dimensional representations
  4135	of $U_q(\hat{\mathfrak{g}})$ and $Y_\hbar(\mathfrak{g})$.
  4136	This equivalence is an exact faithful functor sending simples to
  4137	simples, identifying $\ell$-weight decompositions on both sides
  4138	\textup{(}the Yangian Drinfeld generators correspond to
  4139	quantum loop Cartan generators under~\cite{GTL17}\textup{)},
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4330,4485p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\smallskip\noindent\textit{Step~1 \textup{(}Compact identification\textup{)}.}
By~\ref{it:colimit-generation}, every object of
$\mathcal{D}^{\mathrm{comp}}$ is a filtered colimit of objects
in~$\iota(D^b(\mathcal{A}))$.
By~\ref{it:compactness-preservation}, each such image object is
compact. If $C \in \mathcal{D}^{\mathrm{comp}}$ is compact, then
$\operatorname{id}_C$ factors through a finite stage of any
presenting filtered diagram, so $C$ is a retract of an object
in~$\iota(D^b(\mathcal{A}))$. Therefore
\[
(\mathcal{D}^{\mathrm{comp}})^{\omega}
\;=\;
\overline{\iota(D^b(\mathcal{A}))}^{\,\mathrm{thick,\, idemp}}.
\]
This is the standard argument of
Neeman~\cite[Thm.~2.1]{Neeman92}
and Bondal--Van den Bergh~\cite[Cor.~3.1.2]{BondalVdB03}
in the stable $\infty$-categorical form of
Lurie~\cite[Prop.~5.3.5.10, Prop.~5.5.7.8]{HTT}.

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:eval-core-identification" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 216

standalone/theorem_index.tex:1801:theorem & \detokenize{thm:eval-core-identification} & \detokenize{Evaluation-generated core identification, type~\texorpdfstring{$A$}{A}} & \texttt{ProvedHere} & \detokenize{chapters/examples/yangians_computations.tex:2767}\\
rectification_20260412_233715/R07_yangians_computations.md:591:2764:\label{thm:eval-core-identification}
rectification_20260412_233715/R07_yangians_computations.md:629:  3539	(Theorem~\ref{thm:eval-core-identification}).
rectification_20260412_233715/R07_yangians_computations.md:2077: \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:2609: evaluation core (Theorem~\ref{thm:eval-core-identification}).
rectification_20260412_233715/R07_yangians_computations.md:2905: \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:3788:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:3988:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:4188:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:4413:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:4641:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:4903:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:5168:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:5453:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:5741:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:6050:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:6236: \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
rectification_20260412_233715/R07_yangians_computations.md:6433:  \textup{(}Theorem~\ref{thm:eval-core-identification}\textup{)};
thinking
**Investigating file sections**

I’m checking a file and it seems that the term "landscape" matched the section label, but the output only gave me the label itself. I’ll need to dig deeper into the new block since there’s no issue Likely. There’s a specific line related to "prop:heart-capture-criterion," so I’ll inspect the lines around 2480-2565 and also look at "thm:shifted-prefundamental-generation" around 3000. Let’s see what’s going on there!
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2740,3215p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '2470,2615p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2470	\end{equation}
  2471	where $u = a - b$ and $P$ is the transposition.
  2472	The eigenvalues of~$P$ on $V_1 \otimes V_1 \cong V_2 \oplus V_0$
  2473	are $+1$ (on $\mathrm{Sym}^2(V_1) = V_2$) and $-1$
  2474	(on $\Lambda^2(V_1) = V_0$), giving
  2475	\[
  2476	R(u)\big|_{V_2} = \frac{u+1}{u+1} = 1, \qquad
  2477	R(u)\big|_{V_0} = \frac{u-1}{u+1}.
  2478	\]
  2479	The unique pole is at $u = -1$ (i.e.\ $a = b - 1$), with residue
  2480	projecting onto the $V_0$ summand.
  2481	
  2482	\emph{Step~2: The extension at the pole.}
  2483	At $a - b = -1$, the intertwiner
  2484	$R_{V_1,V_1}(-1)\colon V_1(b-1) \otimes V_1(b) \to
  2485	V_1(b) \otimes V_1(b-1)$
  2486	has a pole. The residue
  2487	\[
  2488	\Res_{u = -1} R(u) = \frac{-\mathrm{id} + P}{1}
  2489	\bigg|_{\text{pole}} = \pi_{V_0}
 succeeded in 51ms:
  2740	\begin{itemize}
  2741	\item Manuscript tables for $\mathfrak{sl}_2$, $\mathfrak{sl}_3$,
  2742	 $\mathfrak{sp}_4$ reproduced exactly through $p = 9$;
  2743	\item At $p = 200$: $\dim E_1^{0,200}(\mathfrak{sl}_2) = 159{,}733$,
  2744	 $\dim E_1^{0,200}(\mathfrak{sl}_3) = 98{,}874{,}604$
  2745	 (not polynomial);
  2746	\item Observed growth constants converge to $\pi\sqrt{r/12}$
  2747	 within $8\%$ at $p = 500$ for all types including the
  2748	 exceptional algebras $G_2$, $F_4$, $E_{6,7,8}$;
  2749	\item Same-rank algebras ($A_2$, $B_2$, $G_2$: all rank~$2$)
  2750	 confirm identical leading constant, different subleading;
  2751	\item Departure points from $A_1$: $p = 5$ for $A_2$,
  2752	 $p = 7$ for $C_2$, $p = 11$ for $G_2$ (matching manuscript).
  2753	\end{itemize}
  2754	Sectorwise finiteness for all simply-laced lattice
  2755	VOAs ($A_1$--$A_3$, $D_4$--$D_5$, $E_6$--$E_8$) is verified at the
  2756	lattice-bar sector level ($93$~tests,
  2757	\texttt{compute/lib/sectorwise\_finiteness.py}),
  2758	and the sub-exponential vs.\ exponential growth discrimination is
  2759	checked via least-squares fitting of $\log d_n$ to both $c \cdot n$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2700,2850p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\]
Hence $\dim E_1^{0,p}$ equals the number of subsets~$S$ of
$\{(i,n) : 1 \le i \le r,\, n \ge 0\}$ satisfying
$\sum_{(i,n) \in S} (2e_i + 1 + 2n) = p$.
The generating function is
\[
P_{\mathfrak{g}}(q)
= \sum_{p \ge 0} \dim E_1^{0,p}\, q^p
= \prod_{i=1}^{r} \prod_{n=0}^{\infty}
 \bigl(1 + q^{2e_i + 1 + 2n}\bigr).
\]
Each factor $\prod_{n=0}^{\infty}(1 + q^{a_i + 2n})$ with
$a_i = 2e_i + 1$ counts partitions into distinct parts of an
arithmetic progression with common difference~$2$. Applying
the saddle-point method, the logarithmic singularity at
$q = 1$ gives
\[
\log P_{\mathfrak{g}}(e^{-t})
\;\sim\; \frac{r\pi^2}{24\,t}
\qquad (t \to 0^+),
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3215,3268p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3215	$D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$ in the separated
  3216	completion is contained in the localizing subcategory generated by
  3217	$\mathcal{G}_{\mathrm{Bax}}$.
  3218	
  3219	\smallskip\noindent\textit{Conditional completion extension.}
  3220	Assume now that $\mathcal{D}^{\mathrm{comp}}$ is a presentable stable
  3221	completed enhancement whose compact objects are the thick
  3222	idempotent-complete closure of the image of
  3223	$D^b(\mathcal{O}^{\mathrm{sh}}_{\leq 0})$. Then the compact part of
  3224	$\mathcal{D}^{\mathrm{comp}}$ is already generated by
  3225	$\mathcal{G}_{\mathrm{Bax}}$, and the whole category is the localizing
  3226	subcategory generated by its compact objects. This is the classical
  3227	compact-generation mechanism of Neeman and Bondal--Van den Bergh; in
  3228	the stable $\infty$-categorical form used here it is the ind-completion
  3229	formalism of Lurie~\cite[Prop.~5.3.5.10, Prop.~5.5.7.8]{HTT}. Hence
  3230	$\mathcal{D}^{\mathrm{comp}} = \operatorname{Loc}\langle
  3231	\mathcal{G}_{\mathrm{Bax}}\rangle$.
  3232	
  3233	This proves the unconditional Baxter-locus generation statement on the
  3234	shifted envelope. The remaining compact/completion packet is the
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:shifted-prefundamental-generation" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 1043

appendices/nonlinear_modular_shadows.tex:80:Theorem~\ref{thm:shifted-prefundamental-generation}), the
standalone/theorem_index.tex:1805:theorem & \detokenize{thm:shifted-prefundamental-generation} & \detokenize{Shifted-prefundamental generation on the shifted envelope} & \texttt{ProvedHere} & \detokenize{chapters/examples/yangians_computations.tex:3070}\\
metadata/dependency_graph.dot:1249:  thm_shifted_prefundamental_generation [label="thm:shifted-prefundamental-generation\ntheorem [Pr]\nShifted-prefundamental generation on the...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:2003:| `thm:shifted-prefundamental-generation` | `theorem` | 3072 | Shifted-prefundamental generation on the shifted envelope |
metadata/label_index.json:43414:  "thm:shifted-prefundamental-generation": {
metadata/claims.jsonl:1203:{"label": "thm:shifted-prefundamental-generation", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/yangians_computations.tex", "line": 3072, "title": "Shifted-prefundamental generation on the shifted envelope", "cites_in_block": ["HJZ25"]}
metadata/claims.jsonl:1204:{"label": "conj:rank-independence-step2", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/yangians_computations.tex", "line": 3242, "title": "Lift-and-lower \\textup{(}Lemma~L\\textup{)}", "refs_in_block": ["thm:categorical-cg-all-types", "thm:shifted-prefundamental-generation", "prop:prefundamental-clebsch-gordan"], "cites_in_block": ["HJZ25"]}
metadata/claims.jsonl:1211:{"label": "thm:mc3-type-a-resolution", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/yangians_computations.tex", "line": 3987, "title": "Type-$A$ MC3 reduction to the compact-completion packet", "refs_in_block": ["prop:prefundamental-clebsch-gordan", "thm:shifted-prefundamental-generation", "conj:dk-compacts-completion"]}
metadata/claims.jsonl:1213:{"label": "cor:mc3-all-types", "env_type": "corollary", "status": "ProvedHere", "file": "chapters/examples/yangians_computations.tex", "line": 4224, "title": "Three-layer MC3 status after categorical CG closure", "refs_in_block": ["thm:categorical-cg-all-types", "cor:dk23-all-types", "thm:shifted-prefundamental-generation", "conj:rank-independence-step2"]}
metadata/claims.jsonl:1232:{"label": "thm:derived-dk-yangian", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 283, "title": "Derived Drinfeld--Kohno on the evaluation-generated subcategory", "labels_in_block": ["thm:derived-dk-yangian", "eq:dk-square-yangian"], "refs_in_block": ["thm:derived-dk-affine", "conj:dk-fd-typeA", "thm:shifted-prefundamental-generation", "prop:yangian-module-koszul"], "cites_in_block": ["Drinfeld85"]}
metadata/claims.jsonl:1247:{"label": "conj:mc3-formal-moduli-reformulation", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/examples/yangians_drinfeld_kohno.tex", "line": 1748, "title": "Formal moduli reformulation of MC3", "refs_in_block": ["thm:baxter-exact-triangles", "thm:shifted-prefundamental-generation", "thm:pro-weyl-recovery", "conj:dk-compacts-completion"]}
appendices/combinatorial_frontier.tex:283: (Theorem~\ref{thm:shifted-prefundamental-generation}, Step~2).
scripts/rectification_campaign.py:271:1. [CRITICAL T10] Line ~3071: Step 2 of thm:shifted-prefundamental-generation claims lambda=0
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:17:`thm:shifted-prefundamental-generation`
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:283:3041:\label{thm:shifted-prefundamental-generation}
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:284:3180:\textup{(}Theorem~\textup{\ref{thm:shifted-prefundamental-generation}}\textup{)}
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:285:3194:Theorem~\ref{thm:shifted-prefundamental-generation} and
platonic_rectification_20260413_114523/P09_MC3_baxter_upgrade.md:286:3210:Theorem~\ref{thm:shifted-prefundamental-generation} proves the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3030,3235p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
defines a natural exact sequence of functors on
$\mathcal{O}_{\mathrm{poly}}(Y(\mathfrak{sl}_2))$.
\end{corollary}

\begin{proof}
On $\mathcal{O}_{\mathrm{poly}}$, Verma modules are the simple
objects and $\Hom(M(\lambda), M(\mu)) = 0$ for $\lambda \neq \mu$,
$\End(M(\lambda)) = \mathbb{C}$. Since all Hom spaces are at most
$1$-dimensional, naturality of the SES maps with respect to
morphisms in $\mathcal{O}_{\mathrm{poly}}$ is automatic from the
existence of the $Y(\mathfrak{sl}_2)$-equivariant SES at each
weight
(Proposition~\ref{prop:baxter-yangian-equivariance}).
\end{proof}

\begin{remark}[From R-matrix poles to Baxter equivariance]
\label{rem:rmatrix-baxter-connection}
\index{Baxter relation!R-matrix connection}
The spectral constraint $b = a - (\lambda+1)/2$ is the
\emph{Verma module analogue} of the R-matrix pole condition
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:heart-capture-criterion" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/dependency_graph.dot:1238:  prop_heart_capture_criterion [label="prop:heart-capture-criterion\nproposition [Pr]\nHeart-capture criterion", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:1995:| `prop:heart-capture-criterion` | `proposition` | 2550 | Heart-capture criterion |
metadata/label_index.json:22542:  "prop:heart-capture-criterion": {
rectification_20260412_233715/R07_yangians_computations.md:816:I’m planning to search the file for mentions of Francis–Gaitsgory or pro-nilpotent completion. There might be earlier propositions about localizing generation and compacts around lines 3600-3700, specifically looking for labels like `cor:sectorwise-localizing-generation`, `prop:heart-capture-criterion`, and `prop:standard-capture-criterion`. It could be helpful to cite these in Step 4 to connect the standards to compacts. I’ll closely inspect the area around these propositions for relevant information.
rectification_20260412_233715/R07_yangians_computations.md:823:2545:\label{prop:heart-capture-criterion}
rectification_20260412_233715/R07_yangians_computations.md:825:2585:(Proposition~\ref{prop:heart-capture-criterion}) then gives
rectification_20260412_233715/R07_yangians_computations.md:905:  2545	\label{prop:heart-capture-criterion}
standalone/theorem_index.tex:1797:proposition & \detokenize{prop:heart-capture-criterion} & \detokenize{Heart-capture criterion} & \texttt{ProvedHere} & \detokenize{chapters/examples/yangians_computations.tex:2549}\\
metadata/claims.jsonl:1194:{"label": "prop:heart-capture-criterion", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/examples/yangians_computations.tex", "line": 2550, "title": "Heart-capture criterion"}
audit_campaign_20260412_231034/T10_MC3_thickgen.md:606:/bin/zsh -lc "rg -n \"label\\{prop:heart-capture-criterion\\}|label\\{prop:standard-capture-criterion\\}|label\\{cor:sectorwise-localizing-generation\\}|label\\{lem:fd-thick-closure\\}|label\\{rem:fd-thick-closure-implications\\}\" chapters/examples/yangians_computations.tex -n -S" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/T10_MC3_thickgen.md:619:2545:\label{prop:heart-capture-criterion}
chapters/examples/yangians_computations.tex:2550:\label{prop:heart-capture-criterion}
chapters/examples/yangians_computations.tex:2590:(Proposition~\ref{prop:heart-capture-criterion}) then gives
chapters/examples/yangians_computations.tex:3935: \textup{(}Propositions~\textup{\ref{prop:heart-capture-criterion}}
chapters/examples/yangians_computations.tex:4363:\textup{(}Proposition~\ref{prop:heart-capture-criterion}\textup{)},
healing_20260413_132214/H11_SC_formal_alt.md:8642:\newlabel{prop:heart-capture-criterion}{{O.9.38}{2284}{Heart-capture criterion; \ClaimStatusProvedHere }{proposition.O.9.38}{}}
healing_20260413_132214/H11_SC_formal_alt.md:19808:-\newlabel{prop:heart-capture-criterion}{{O.9.38}{2284}{Heart-capture criterion; \ClaimStatusProvedHere }{proposition.O.9.38}{}}
healing_20260413_132214/H11_SC_formal_alt.md:30972:-\newlabel{prop:heart-capture-criterion}{{O.9.38}{2284}{Heart-capture criterion; \ClaimStatusProvedHere }{proposition.O.9.38}{}}
healing_20260413_132214/H11_SC_formal_alt.md:42137:-\newlabel{prop:heart-capture-criterion}{{O.9.38}{2284}{Heart-capture criterion; \ClaimStatusProvedHere }{proposition.O.9.38}{}}
healing_20260413_132214/H11_SC_formal_alt.md:53302:-\newlabel{prop:heart-capture-criterion}{{O.9.38}{2284}{Heart-capture criterion; \ClaimStatusProvedHere }{proposition.O.9.38}{}}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2500,2585p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
of $V_1(b-1) \otimes V_1(b)$ at the specialization $a = b - 1$.
This gives
\begin{equation}\label{eq:sl2-ext1}
\dim \operatorname{Ext}^1_{\mathcal{O}}(V_2(c),\, V_0(c)) = 1
\end{equation}
for all~$c$: a single extension class, classified by the
R-matrix pole.

\emph{Step~3: Higher representations.}
For $V_n(a) \otimes V_m(b)$ with $n + m \le 2$, the
$R$-matrix poles occur at $a - b \in \{0, \pm 1\}$ (for
$\mathfrak{sl}_2$, the only fundamental is $V_1$, and the
general R-matrix factors through fundamental $R$-matrices).
The tensor product decomposition
$V_n(a) \otimes V_1(b)$ at the pole $a - b = -(n+1)/2$
produces
\[
0 \to V_{n-1}(c') \to V_n(a) \otimes V_1(b)\big|_{a = b - (n+1)/2}
\to V_{n+1}(c'') \to 0
\]
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "thm:pro-weyl-recovery" -n chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3184:By Theorem~\ref{thm:pro-weyl-recovery}, every ordinary standard module
3702:\label{thm:pro-weyl-recovery}
3740:Theorem~\ref{thm:pro-weyl-recovery} resolves the pro-Weyl packet.
3782: \textup{(}Theorem~\ref{thm:pro-weyl-recovery}\textup{)}.
3798:\ref{thm:pro-weyl-recovery}, and
3917: \textup{(}Theorem~\textup{\ref{thm:pro-weyl-recovery}}\textup{)}:
4379:\textup{(}Theorem~\ref{thm:pro-weyl-recovery}\textup{)}
4434:\textup{(}Theorem~\ref{thm:pro-weyl-recovery}\textup{)}: the

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3650,3815p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Since $V_{\omega_i}$ is minuscule for $\mathfrak{sl}_N$
(all weights have multiplicity~$1$), these embeddings give a
filtration
$0 = F_0 \subset F_1 \subset \cdots \subset F_d
= V_{\omega_i}(a) \otimes L^-_i(b)$
(where $d = \dim V_{\omega_i}$) with successive quotients
$F_j / F_{j-1} \cong L^-_i(\mathrm{shift} = \mu_j)$ for
some ordering of the weights.

\emph{Step~2: Block separation.}
Each summand $L^-_i(\mathrm{shift} = \mu)$ carries a distinct
$\ell$-highest weight $\Psi^-_{i,\mu}$ encoding the full
weight vector~$\mu$. For $\mu \neq \nu$ in
$\operatorname{wt}(V_{\omega_i})$, the $\ell$-weight ratio
$\Psi^-_{i,\mu} / \Psi^-_{i,\nu}$ is a monomial~$x^{\mu - \nu}$
with $\mu - \nu \neq 0$ in the weight lattice.
By the block criterion for category~$\mathcal{O}^{\mathrm{sh}}$
\cite{Hernandez05, HJZ25}: two simple highest-$\ell$-weight
modules lie in the same block only if their $\ell$-weight ratio
is a product of shifted simple root contributions. For

thinking
**Assessing proof justification and citations**

I’m evaluating whether the proof steps for the extension and bounded weight argument are properly justified by the referenced theorems and propositions, especially focusing on Step2 using shifted prefund generation near lines 3036-3189, heart capture at line 2550, evaluation core identification at 2769, pro-Weyl recovery around 3702, and colimit generation near 4330. I’m preparing to confirm the logical flow aligns with cited dependencies and provide line-based citations in the requested format.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '3020,3250p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3020	\end{proof}
  3021	
  3022	\begin{corollary}[Naturality on
  3023	$\mathcal{O}_{\mathrm{poly}}$; \ClaimStatusProvedHere]
  3024	\label{cor:baxter-naturality-opoly}
  3025	Under the spectral
  3026	constraint~\eqref{eq:baxter-spectral-constraint}, the
  3027	assignment
  3028	$M(\lambda) \mapsto
  3029	[\textup{SES}~\eqref{eq:baxter-ses-yangian}]$
  3030	defines a natural exact sequence of functors on
  3031	$\mathcal{O}_{\mathrm{poly}}(Y(\mathfrak{sl}_2))$.
  3032	\end{corollary}
  3033	
  3034	\begin{proof}
  3035	On $\mathcal{O}_{\mathrm{poly}}$, Verma modules are the simple
  3036	objects and $\Hom(M(\lambda), M(\mu)) = 0$ for $\lambda \neq \mu$,
  3037	$\End(M(\lambda)) = \mathbb{C}$. Since all Hom spaces are at most
  3038	$1$-dimensional, naturality of the SES maps with respect to
  3039	morphisms in $\mathcal{O}_{\mathrm{poly}}$ is automatic from the
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '2530,2595p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2530	
  2531	\emph{Step~4: Finiteness for $\mathfrak{sl}_2$.}
  2532	For $\mathfrak{sl}_2$, each step reduces the highest weight of the
  2533	kernel by exactly~$2$ (one $R$-matrix pole). A Verma module
  2534	$M(\lambda, a)$ at dominant integral weight~$\lambda$ therefore
  2535	admits a resolution of length exactly $\lambda + 1$ (the length of
  2536	the Weyl group orbit), recovering the classical BGG resolution
  2537	enriched with spectral parameters.
  2538	
  2539	For non-integral $\lambda$, the chain of spectral parameter
  2540	extensions does not terminate after finitely many steps: there is no
  2541	lowest weight in the $\mathfrak{sl}_2$ Verma module when $\lambda$
  2542	is not a non-negative integer. This exhibits the precise
  2543	obstruction: Strategy~I succeeds exactly on the dominant integral
  2544	(= polynomial) subcategory, consistent with the proved
  2545	Theorem~\ref{thm:catO-thick-generation} for
  2546	$\mathcal{O}_{\mathrm{poly}}$.
  2547	\end{computation}
  2548	
  2549	\begin{proposition}[Heart-capture criterion; \ClaimStatusProvedHere]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '3670,3755p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3670	generic spectral parameters (avoiding a discrete resonance set
  3671	where $\mu - \nu$ aligns with the normalized $R$-matrix
  3672	denominator), the monomial~$x^{\mu - \nu}$ admits no such
  3673	factorization, so $L^-_i(\mathrm{shift} = \mu)$ and
  3674	$L^-_i(\mathrm{shift} = \nu)$ lie in \emph{distinct} blocks.
  3675	Hence
  3676	\[
  3677	\operatorname{Ext}^1_{\mathcal{O}^{\mathrm{sh}}}
  3678	\!\bigl(L^-_i(\mathrm{shift} = \mu),\;
  3679	 L^-_i(\mathrm{shift} = \nu)\bigr) = 0
  3680	\qquad (\mu \neq \nu,\;\text{generic}).
  3681	\]
  3682	
  3683	\emph{Step~3: Splitting.}
  3684	The filtration from Step~1 has successive quotients in
  3685	pairwise distinct blocks (Step~2). Each extension
  3686	$0 \to F_{j-1} \to F_j \to
  3687	L^-_i(\mathrm{shift} = \mu_j) \to 0$
  3688	therefore splits: the right-hand term lies in a block disjoint
  3689	from all composition factors of~$F_{j-1}$, so


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '4330,4435p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4330	
  4331	\smallskip\noindent\textit{Step~1 \textup{(}Compact identification\textup{)}.}
  4332	By~\ref{it:colimit-generation}, every object of
  4333	$\mathcal{D}^{\mathrm{comp}}$ is a filtered colimit of objects
  4334	in~$\iota(D^b(\mathcal{A}))$.
  4335	By~\ref{it:compactness-preservation}, each such image object is
  4336	compact. If $C \in \mathcal{D}^{\mathrm{comp}}$ is compact, then
  4337	$\operatorname{id}_C$ factors through a finite stage of any
  4338	presenting filtered diagram, so $C$ is a retract of an object
  4339	in~$\iota(D^b(\mathcal{A}))$. Therefore
  4340	\[
  4341	(\mathcal{D}^{\mathrm{comp}})^{\omega}
  4342	\;=\;
  4343	\overline{\iota(D^b(\mathcal{A}))}^{\,\mathrm{thick,\, idemp}}.
  4344	\]
  4345	This is the standard argument of
  4346	Neeman~\cite[Thm.~2.1]{Neeman92}
  4347	and Bondal--Van den Bergh~\cite[Cor.~3.1.2]{BondalVdB03}
  4348	in the stable $\infty$-categorical form of
  4349	Lurie~\cite[Prop.~5.3.5.10, Prop.~5.5.7.8]{HTT}.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '2755,2815p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2755	VOAs ($A_1$--$A_3$, $D_4$--$D_5$, $E_6$--$E_8$) is verified at the
  2756	lattice-bar sector level ($93$~tests,
  2757	\texttt{compute/lib/sectorwise\_finiteness.py}),
  2758	and the sub-exponential vs.\ exponential growth discrimination is
  2759	checked via least-squares fitting of $\log d_n$ to both $c \cdot n$
  2760	and $C \cdot \sqrt{n}$ models.
  2761	\end{computation}
  2762	
  2763	\end{remark}
  2764	
  2765	\subsubsection*{Resolution: the evaluation-generated core}
  2766	
  2767	\begin{theorem}[Evaluation-generated core identification, type~\texorpdfstring{$A$}{A};
  2768	\ClaimStatusProvedHere]
  2769	\label{thm:eval-core-identification}
  2770	\index{thick generation!evaluation-generated core|textbf}
  2771	\index{Drinfeld--Kohno!derived!evaluation-generated core}
  2772	For $\fg = \mathfrak{sl}_N$ with $N \ge 2$, the thick triangulated
  2773	subcategory of $D^b(\mathcal{O}_{Y_\hbar(\mathfrak{sl}_N)})$
  2774	generated by evaluation modules satisfies
thinking
**Considering filtered colimits**

I’m thinking about the statement that “every object is a filtered colimit of objects in the image.” This might imply that the objects are generated as a closure under colimits, extensions, cofibres, and retracts. In a stable presentable category, localizing a subcategory generated by a set suggests closure under all colimits and finite limits. However, the hypothesis says it's generated under filtered colimits, not localizing generated sets. This makes it intriguing, especially if every object doesn’t require triangles or extensions.
thinking
**Analyzing a mathematical theorem**

I'm looking at a theorem related to standard objects and their placement within various categories. It shifts a focus towards how every standard object of A exists in the thick closure of G_Bax inside the separated completion, but not necessarily in an arbitrary category (Dcomp). I see a proposed step that transfers this idea without supplying a functor linking the two. I realize that this conclusion seems unjustified since the theorem is about a specific completion type, while the proposition mentions a more general one.
thinking
**Clarifying propositions in a theorem**

I'm examining the proposition and noticing it doesn't clearly state that G_Bax objects are part of Dcomp. However, since iota embeds D^b(A) and G_Bax are part of A, their images must be in Dcomp. The theorem indicates that in the separated completion, each standard object exists in the thick closure of G_Bax within the image of D^b(A). Actually, the theorem emphasizes that every standard object of A lies in the thick idempotent closure of G_Bax specifically in that separated completion.

thinking
**Summarizing final proof justification with references**

I'll outline the proof’s key steps with line references, highlighting how Step 2 shows compact thick closure via the theorem and proposition, Step 3 uses the evaluation core and pro-Weyl to extend equivalence, and confirm all dependencies are covered—concluding the proof is justified. I'll keep the summary concise with bullet points and tie up plan statuses.
codex
The main pressure point is Step 3. I’m now checking whether any earlier result in this file actually proves `\Phi` is continuous on the pro-Weyl inverse-limit construction or even defined on the arbitrary completion `\mathcal D^{\mathrm{comp}}`; without that, the “extends to a localizing equivalence” conclusion is too strong for the stated hypotheses.
exec
/bin/zsh -lc 'rg -n "BondalVdB03|Neeman92" chapters/examples/yangians_computations.tex bibliography.bib references.bib *.bib' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"extends.*Phi|Phi.*extends|localizing equivalence|compact-core equivalence|Ind-completion|continuity.*Phi|pro-Weyl.*Phi|R\\\\varprojlim.*Phi|DK on compacts|Phi.*standard|dual standard|commutes with inverse limits\" chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarPlan update
  ✓ Identify latest commit touching chapters/examples/yangians_computations.tex and extract block around prop:completion-extension-weight-bounded for context
  ✓ Locate statements for the referenced theorems/props elsewhere in repo to understand dependencies
  ✓ Assess whether the proof of prop:completion-extension-weight-bounded is justified by those dependencies and summarize with citations
 exited 1 in 50ms:
zsh:1: no matches found: *.bib
 succeeded in 51ms:
3758:\begin{conjecture}[DK on compacts and completion extension; \ClaimStatusConjectured]
3763:$\Phi$~\eqref{eq:dk-eval-core} extends from the finite-dimensional
3769:\begin{remark}[Type-A status of DK on compacts]
3921: \item \emph{DK on compacts, extended by completion}
4026: that compact-core equivalence with the desired
4270:that the required compact-core equivalence or the needed completion
4322: localizing equivalence
4380:extends~$\Phi$ to standards, and by Step~2 to all compact objects.
4384:Ind-completion: a functor on compact objects extends uniquely,
4394:Ind-completion $\operatorname{Ind}(D^b(\mathcal{A}))$
4398:Ind-completion. The substantive content is
4403:For the Ind-completion
4409:This is the unconditional result: the Ind-completion of the shifted
4461:The Ind-completion $\operatorname{Ind}(D^b(\mathcal{A}))$ is the
4519:passage from a compact-core equivalence to the chosen completed
codex
- Step 2 of `prop:completion-extension-weight-bounded` invokes `thm:shifted-prefundamental-generation` to show every standard of the shifted heart lies in `\mathrm{thick}\langle\mathcal{G}_{\mathrm{Bax}}\rangle` and then applies `prop:heart-capture-criterion` (plus the BGG filtration) to force the entire derived heart, hence the compact core, into that thick closure; see `chapters/examples/yangians_computations.tex:3070-3231` for the shifted-generation argument and `chapters/examples/yangians_computations.tex:2550-2556` for the heart-capture criterion. 
- Step 3 then rests on `thm:eval-core-identification` and `thm:pro-weyl-recovery`: the bar-cobar functor is an equivalence on the evaluation core, the pro-Weyl towers jibe with that equivalence to place every standard (and hence every compact by the previous step) in its domain, and the universal property of Ind-completion promotes the compact equivalence to the whole presentable enhancement; see `chapters/examples/yangians_computations.tex:2769-2790`, `3701-3734`, and `4375-4385`. 
- Because the proposition’s three steps therefore rest directly on these proved inputs, the proof is mathematically justified from the cited dependencies.
exec
/bin/zsh -lc 'rg -n "BondalVdB03|Neeman92" /Users/raeez/chiral-bar-cobar' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar/bibliography/references.tex:196:\bibitem{BondalVdB03}
/Users/raeez/chiral-bar-cobar/bibliography/references.tex:1034:\bibitem{Neeman92}
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4346:Neeman~\cite[Thm.~2.1]{Neeman92}
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4347:and Bondal--Van den Bergh~\cite[Cor.~3.1.2]{BondalVdB03}
/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4458:Bondal--Van den Bergh~\cite[Cor.~3.1.2]{BondalVdB03}: for a
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3890,4045p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3890	 Corollary~\ref{cor:dk23-all-types}. On that restricted core
  3891	 surface, the remaining ladder proceeds directly to DK-4.
  3892	\item If one wishes to include infinite-dimensional
  3893	 modules \textup{(}prefundamental representations, asymptotic
  3894	 modules in the sense of Hernandez--Zhang~\cite{HJZ25}\textup{)}, then
  3895	 a completed, coderived, or ind-completed enhancement
  3896	 $\widehat{D}(\mathcal{O})$ is required
  3897	 \textup{(}Remark~\textup{\ref{rem:fd-thick-closure-implications}(b)}\textup{)},
  3898	 and the generation mechanism shifts from thick closure to
  3899	 localizing subcategories with compact generation. The
  3900	 structural input for this extension is organized by four
  3901	 packages, three of which are resolved in type~$A$ and the
  3902	 fourth of which remains open:
  3903	 \begin{enumerate}[label=\textup{(\roman*)}]
  3904	 \item \emph{Baxter exact triangles}
  3905	 \textup{(}Theorem~\textup{\ref{thm:baxter-exact-triangles}}\textup{)}:
  3906	 the decategorified TQ relations of Zhang~\cite{Zhang24}
  3907	 lift to distinguished triangles in the anti-dominant shifted
  3908	 envelope~$\mathcal{O}^{\mathrm{sh}}_{\leq 0}$, with
  3909	 finite-dimensional companion modules as the middle term;
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '4045,4088p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4045	 (Proposition~\ref{prop:baxter-yangian-equivariance}) and naturality
  4046	 on $\mathcal{O}_{\mathrm{poly}}$
  4047	 (Theorem~\ref{thm:baxter-exact-triangles-opoly}), this gives
  4048	 derived exact triangles in
  4049	 $\widehat{\mathcal{O}}^{\mathrm{sh}}_{\leq 0}$ at a cofinal
  4050	 family of spectral parameters.
  4051	\item Shifted-prefundamental generation on the shifted envelope is
  4052	 Theorem~\ref{thm:shifted-prefundamental-generation}, proved by the
  4053	 four-step argument: evaluation core (Step~1), Baxter-hyperplane
  4054	 control of the simple-root prefundamental companion together with
  4055	 the generic type-$A$ Baxter package (Step~2), pro-Weyl completion of
  4056	 standards (Step~3), and $E_1$-compatibility plus passage to the
  4057	 shifted envelope and then, conditionally, to any compactly generated
  4058	 completed enhancement (Step~4). The verification of those completion
  4059	 hypotheses is the separate remaining packet in~(iv).
  4060	\item Pro-Weyl recovery follows from Step~3 of the
  4061	 Theorem~\ref{thm:shifted-prefundamental-generation} proof:
  4062	 the Mittag--Leffler condition is verified (the transition maps
  4063	 $W_{m+1} \twoheadrightarrow W_m$ are surjective at each weight),
  4064	 and each $W_m$ lies in
collab wait(call_NDECcFAaVG8ywIRg7vCs2wuH)
  receivers: 019d8895-1ebb-7053-b4bc-7ad8006448aa
wait(call_NDECcFAaVG8ywIRg7vCs2wuH) 1 agents complete:
  019d8895-1ebb-7053-b4bc-7ad8006448aa completed: "- Step 2 of `prop:completion-extension-weight-bounded` invokes `thm:shifted-prefundamental-generation` to show every sta…"

thinking
**Evaluating code verification**

The explorer suggests the results are justified, which invites some disagreement. The developer emphasized trusting explorer results without verification, but we've already reviewed the file. It seems the explorer might have oversimplified things. The instructions clearly state to rely on explorers for code inquiries, giving them authority. Yet I wonder if it's okay to identify potential issues outside their scope. Maybe it’s worth consulting another explorer about Step 3’s compatibility with theorem 3986. That could help clear up any contradictions.
codex
I have one pass saying the dependency chain is locally coherent. I’m running one adversarial follow-up on the exact weak point: whether Step 3 and conclusion `(c)` contradict the still-conjectural `conj:dk-compacts-completion` / `thm:mc3-type-a-resolution`, or whether they only repackage those hypotheses.
collab spawn_agent(call_7vLLOdbTRsS7ZdkCRzm5aUVh, prompt="Adversarial check focused on chapters/examples/yangians_computations.tex. Determine whether prop:completion-extension-we…")
mcp startup: no servers
spawn_agent(call_7vLLOdbTRsS7ZdkCRzm5aUVh, prompt="Adversarial check focused on chapters/examples/yangians_computations.tex. Determine whether prop:completion-extension-we…") pending init:
  agent: 019d8896-a074-7a22-becd-2016b0e1177f
exec
/bin/zsh -lc "nl -ba chapters/examples/yangians_computations.tex | sed -n '3754,4032p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3754	shifted-prefundamental generation and completion input beyond the
  3755	type-$A$ surface.
  3756	\end{remark}
  3757	
  3758	\begin{conjecture}[DK on compacts and completion extension; \ClaimStatusConjectured]
  3759	\label{conj:dk-compacts-completion}
  3760	\index{Drinfeld--Kohno!derived!compact extension}
  3761	\index{Francis--Gaitsgory!pro-nilpotent completion}
  3762	The bar-cobar Koszul duality equivalence
  3763	$\Phi$~\eqref{eq:dk-eval-core} extends from the finite-dimensional
  3764	evaluation core to the full completed shifted-prefundamental core
  3765	$\mathcal{G}_{\mathrm{shift}}$, and then by pro-nilpotent completion
  3766	in the sense of Francis--Gaitsgory to the completed Yangian category.
  3767	\end{conjecture}
  3768	
  3769	\begin{remark}[Type-A status of DK on compacts]
  3770	\label{rem:dk-compacts-completion-typeA}
  3771	In type~$A$ ($\mathfrak{sl}_N$ for all $N \geq 2$),
  3772	packages~(i)--(iii) of the old MC3 list are resolved, but
  3773	Conjecture~\ref{conj:dk-compacts-completion} remains the final

thinking
**Preparing adversarial verification plan**

I’m gathering instructions and considering the deep-beilinson skill to audit or verify the proposition requested. Since the task is complex, I’ll create a multi-step plan following the guidelines. Next, I’ll open relevant files and use the plan tool for a structured approach.
Plan update
  → Review AGENTS/CLAUDE context and identify exact surfaces: prop:completion-extension-weight-bounded, conj:dk-compacts-completion, thm:mc3-type-a-resolution in yangians_computations.tex
  • Read and analyze the relevant sections of yangians_computations.tex and any referenced definitions or hypotheses; note potential inconsistencies or missing assumptions
  • Summarize adversarial findings with citations and report sufficiency of hypothesis for extending bar-cobar functor Phi
collab wait(call_WH7wZaKMKxm1TDF6xf0bV6Ba)
  receivers: 019d8896-a074-7a22-becd-2016b0e1177f
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && cat .agents/skills/deep-beilinson-audit/SKILL.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && cat CLAUDE.md | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && grep -n "completion" -n chapters/connections/concordance.tex | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
798:and modular completion.
959:\index{factorization envelope!functorial completion}
1078: cyclic pairing plus pronilpotent completion.
1562:Conj~\ref{conj:analytic-completion-programme}
1563: (analytic completion programme)
1648: (\S\ref{subsec:concordance-holographic-completion})
1882:compact-completion packet
1890:extension and completion beyond the evaluation core and its compact
1892:\textup{(}Conjecture~\ref{conj:dk-compacts-completion}\textup{)},
1928:to compact-completion of full category) remains open.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3700,3805p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{theorem}[Pro-Weyl recovery of ordinary standards in type~$A$; \ClaimStatusProvedHere]
\label{thm:pro-weyl-recovery}
\index{Weyl module!pro-Weyl tower}
\index{standard module!pro-Weyl recovery}
For $\fg = \mathfrak{sl}_N$ with $N \ge 2$ and a rational highest
$\ell$-weight~$\Psi$, let
$\Psi_{\leq m}$ denote its truncation to finite Drinfeld divisor
data and $W_m := W(\Psi_{\leq m})$ the local Weyl module.
Then the ordinary standard module is recovered as a derived
inverse limit
\[
M(\Psi) \;\simeq\; R\varprojlim_m\, W_m
\]
inside a separated completion of~$\mathcal{O}$.
Each $W_m$ is universal finite-dimensional highest-weight, hence lies
in $\operatorname{thick}\langle \mathrm{Ev} \rangle$ by the proved
evaluation core (Theorem~\ref{thm:eval-core-identification}).
\end{theorem}

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '3980,4055p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:mc3-type-a-resolution} proves packages~(i)--(iii)
and isolates Conjecture~\ref{conj:dk-compacts-completion} as the last
step needed to reach the entire completed shifted-prefundamental
category.
\end{remark}

\begin{theorem}[Type-$A$ MC3 reduction to the compact-completion packet; \ClaimStatusProvedHere]
\label{thm:mc3-type-a-resolution}
\index{MC3!type-A resolution|textbf}
\index{Drinfeld--Kohno!derived!type-A completion}
\index{prefundamental!Clebsch--Gordan closure!type A}
For $\mathfrak{g} = \mathfrak{sl}_N$ with $N \geq 2$, the old
four-package MC3 extension problem is reduced to a single remaining
compact-completion packet:
\begin{enumerate}[label=\textup{(\roman*)},nosep]
\item \emph{Baxter exact triangles.}
 The TQ relations lift from $K_0$ to derived exact triangles in the
 completed anti-dominant shifted envelope
 $\widehat{\mathcal{O}}^{\mathrm{sh}}_{\leq 0}$.
 The prefundamental Clebsch--Gordan closure
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4055,4180p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 the generic type-$A$ Baxter package (Step~2), pro-Weyl completion of
 standards (Step~3), and $E_1$-compatibility plus passage to the
 shifted envelope and then, conditionally, to any compactly generated
 completed enhancement (Step~4). The verification of those completion
 hypotheses is the separate remaining packet in~(iv).
\item Pro-Weyl recovery follows from Step~3 of the
 Theorem~\ref{thm:shifted-prefundamental-generation} proof:
 the Mittag--Leffler condition is verified (the transition maps
 $W_{m+1} \twoheadrightarrow W_m$ are surjective at each weight),
 and each $W_m$ lies in
 $\operatorname{thick}\langle\{V_{\omega_i}\}\rangle$ by the
 evaluation core (Theorem~\ref{thm:eval-core-identification}).
\item After~(i)--(iii), the only remaining item from the original MC3
 list is the compact/completed extension conjecture
 \textup{(}Conjecture~\textup{\ref{conj:dk-compacts-completion}}\textup{)}.
 No further independent type-$A$ obstruction remains on this
 surface.
\end{enumerate}
\end{proof}

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && head -n 40 metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2369 |
| Total tagged claims | 3114 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2369 |
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && head -n 40 archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4200,4405p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
criterion for category~$\mathcal{O}$
\cite{Hernandez05, HJZ25}, and \textup{(c)}~the
Gautam--Toledano Laredo equivalence~\cite{GTL17}
identifying Drinfeld polynomial data between quantum
loop algebras and Yangians.
The new content is the observation
that these three inputs, combined with the character identity
(Proposition~\ref{prop:character-cg-all-types}), yield the
categorical CG decomposition for \emph{all} types, replacing
the minuscule hypothesis of
Proposition~\ref{prop:categorical-cg-typeA}.
The multiplicity-free property is not contained in a single
reference: for simply-laced types it follows from
$(q,t)$-character theory~\cite{Nakajima04}; for classical types
from explicit formulas~\cite{ChariMoura06}; for all types the
Frenkel--Mukhin algorithm~\cite{FrenkelMukhin01} computes the
$q$-character and confirms multiplicity-freeness.
The block criterion transfers from quantum affine to Yangian
because it is purely combinatorial, depending only on Drinfeld
polynomial data identified by~\cite{GTL17}.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4405,4520p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\operatorname{Ind}(D^b(\mathcal{A}))$,
all three hypotheses hold tautologically and the proposition gives
$\operatorname{Ind}(D^b(\mathcal{A})) =
\operatorname{Loc}\langle \mathcal{G}_{\mathrm{Bax}} \rangle$.
This is the unconditional result: the Ind-completion of the shifted
category is generated by the Baxter-locus seed.

For the Francis--Gaitsgory pro-nilpotent completion, the issue is that
the completion functor $D^b(\mathcal{A}) \to \widehat{D}_{FG}$ may
fail to preserve compactness if the pro-nilpotent tower introduces
non-bounded inverse systems.
Concretely, hypothesis~\ref{it:compactness-preservation} reduces to:
for every finite-length $M \in \mathcal{A}$ and every filtered system
$\{N_\alpha\}$ in~$\widehat{D}_{FG}$,
\[
\varinjlim_\alpha \operatorname{Hom}(\iota(M), N_\alpha)
\;\xrightarrow{\;\sim\;}\;
\operatorname{Hom}\bigl(\iota(M),
\varinjlim_\alpha N_\alpha\bigr).
\]

thinking
**Evaluating proposition's assumptions and extensions**

I'm carefully scrutinizing whether the proposition's hypotheses truly suffice to define and extend the bar-cobar functor \(\Phi\) to the completed category \(D^{comp}\), or if additional continuity or comparison assumptions are needed. I’m tracking how the functor extends from the evaluation core through pro-Weyl recovery to compact objects and then to Ind completions, and considering if the steps rely on implicit or missing conditions about colimit preservation, presentability, and target dual categories. It’s a puzzle connecting the universal properties, generated objects, and uniqueness of extensions to confirm the proposition’s claims don’t overreach or contradict related conjectures and theorems.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "op,dual" -n chapters/examples/yangians_computations.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
4324: (\mathcal{D}^{\mathrm{comp}})^{\mathrm{op,dual}}$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '4200,4505p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4200	criterion for category~$\mathcal{O}$
  4201	\cite{Hernandez05, HJZ25}, and \textup{(c)}~the
  4202	Gautam--Toledano Laredo equivalence~\cite{GTL17}
  4203	identifying Drinfeld polynomial data between quantum
  4204	loop algebras and Yangians.
  4205	The new content is the observation
  4206	that these three inputs, combined with the character identity
  4207	(Proposition~\ref{prop:character-cg-all-types}), yield the
  4208	categorical CG decomposition for \emph{all} types, replacing
  4209	the minuscule hypothesis of
  4210	Proposition~\ref{prop:categorical-cg-typeA}.
  4211	The multiplicity-free property is not contained in a single
  4212	reference: for simply-laced types it follows from
  4213	$(q,t)$-character theory~\cite{Nakajima04}; for classical types
  4214	from explicit formulas~\cite{ChariMoura06}; for all types the
  4215	Frenkel--Mukhin algorithm~\cite{FrenkelMukhin01} computes the
  4216	$q$-character and confirms multiplicity-freeness.
  4217	The block criterion transfers from quantum affine to Yangian
  4218	because it is purely combinatorial, depending only on Drinfeld
  4219	polynomial data identified by~\cite{GTL17}.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '3660,3805p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3660	Each summand $L^-_i(\mathrm{shift} = \mu)$ carries a distinct
  3661	$\ell$-highest weight $\Psi^-_{i,\mu}$ encoding the full
  3662	weight vector~$\mu$. For $\mu \neq \nu$ in
  3663	$\operatorname{wt}(V_{\omega_i})$, the $\ell$-weight ratio
  3664	$\Psi^-_{i,\mu} / \Psi^-_{i,\nu}$ is a monomial~$x^{\mu - \nu}$
  3665	with $\mu - \nu \neq 0$ in the weight lattice.
  3666	By the block criterion for category~$\mathcal{O}^{\mathrm{sh}}$
  3667	\cite{Hernandez05, HJZ25}: two simple highest-$\ell$-weight
  3668	modules lie in the same block only if their $\ell$-weight ratio
  3669	is a product of shifted simple root contributions. For
  3670	generic spectral parameters (avoiding a discrete resonance set
  3671	where $\mu - \nu$ aligns with the normalized $R$-matrix
  3672	denominator), the monomial~$x^{\mu - \nu}$ admits no such
  3673	factorization, so $L^-_i(\mathrm{shift} = \mu)$ and
  3674	$L^-_i(\mathrm{shift} = \nu)$ lie in \emph{distinct} blocks.
  3675	Hence
  3676	\[
  3677	\operatorname{Ext}^1_{\mathcal{O}^{\mathrm{sh}}}
  3678	\!\bigl(L^-_i(\mathrm{shift} = \mu),\;
  3679	 L^-_i(\mathrm{shift} = \nu)\bigr) = 0
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/examples/yangians_computations.tex | sed -n '3950,4050p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  3950	 (2)~the chromatic/conformal-weight filtration reduces
  3951	 shifted-prefundamental generation to countable finite-dimensional
  3952	 strata;
  3953	 (3)~Mittag--Leffler ($R^1\varprojlim = 0$) on Weyl module
  3954	 truncation towers recovers standards as derived inverse limits;
  3955	 (4)~spectral sequence degeneration on weight strata, together
  3956	 with the Francis--Gaitsgory pro-nilpotent completion formalism,
  3957	 isolates the last remaining compact/completed comparison problem:
  3958	 one still needs the compact-core extension of the bar-cobar
  3959	 equivalence and its comparison with the desired completed
  3960	 category.
  3961	 %
  3962	 For arbitrary simple~$\mathfrak{g}$,
  3963	 Theorem~\ref{thm:categorical-cg-all-types} supplies the
  3964	 all-types categorical Clebsch--Gordan input, while the later
  3965	 post-core pro-Weyl / completion argument becomes
  3966	 type-independent only conditionally, once the shifted-
  3967	 prefundamental, pro-Weyl, and compact-completion packets of
  3968	 Proposition~\ref{conj:mc3-automatic-generalization} are
  3969	 separately supplied in that type.

thinking
**Summarizing relation among conjecture, theorem, and proposition**

I’m organizing a clear final message referencing specific line citations from `chapters/examples/yangians_computations.tex`, aligning the conjecture, theorem, proposition, and remarks on hypotheses and extensions. The summary will highlight that the proposition’s part (c) is consistent, conditional, and not contradictory to the existing conjecture and theorem, while carefully noting relevant file lines for each key point as the user requested. I’ll ensure bullet points emphasize severity and cite each main observation precisely.
Plan update
  ✓ Review AGENTS/CLAUDE context and identify exact surfaces: prop:completion-extension-weight-bounded, conj:dk-compacts-completion, thm:mc3-type-a-resolution in yangians_computations.tex
  ✓ Read and analyze the relevant sections of yangians_computations.tex and any referenced definitions or hypotheses; note potential inconsistencies or missing assumptions
  ✓ Summarize adversarial findings with citations and report sufficiency of hypothesis for extending bar-cobar functor Phi

thinking
**Summarizing audit findings**

I'll prepare a final message with a concise header "Proposition vs Conjecture" and three clear bullet points summarizing key remarks, each citing exact file paths and line ranges as per instructions. This will ensure the message is precise, references only what’s requested, and wraps with a suitable closing statement.
codex
**Audit Findings**
- Conjecture \ref{conj:dk-compacts-completion} still singles out the compact/core plus pro-nilpotent extension as the last unresolved packet, and Theorem \ref{thm:mc3-type-a-resolution} makes the same identification in type A, so Proposition \ref{prop:completion-extension-weight-bounded} is not contradicting any higher-level claim but rather isolates that gap for further hypotheses to check (chapters/examples/yangians_computations.tex:3758-3790, 3986-4032).  
- Part (c) of the proposition is derived by extending \(\Phi\) from the evaluation core to standards via pro-Weyl recovery and then using the universal property of Ind to extend any localizing functor that is already an equivalence on compacts; Step 3 spells out exactly this passage and therefore does not overclaim insofar as the stated hypotheses guarantee a colimit-preserving localizing functor on \(\mathcal{D}^{\mathrm{comp}}\) (chapters/examples/yangians_computations.tex:4274-4385).  
- The subsequent remark makes explicit that hypotheses (i)‑(iii) are the needed weight-bounded, colimit-generation, and compactness-preservation conditions equivalent to the pro-nilpotent stability envisioned in the conjecture, so there are no hidden continuity/comparison hypotheses beyond verifying the weightwise Mittag–Leffler behavior of the completion tower (chapters/examples/yangians_computations.tex:4388-4440).
wait(call_WH7wZaKMKxm1TDF6xf0bV6Ba) 1 agents complete:
  019d8896-a074-7a22-becd-2016b0e1177f completed: "**Audit Findings**
- Conjecture \ref{conj:dk-compacts-completion} still singles out the compact/core plus pro-nilpotent …"











thinking
**Analyzing conjectures and hypotheses**

I’m pondering whether there’s a contradiction with the conjecture since the hypotheses of the proposition might be stronger or involve hidden comparison conditions. However, the proposition doesn’t explicitly state anything about comparison or continuity. With the hypotheses focusing on weight-bounded t-structure, colimit generation, and image compacts—and none mentioning \Phi—I realize that the conclusion can’t be drawn just from these alone. I’m curious if there’s a Dcomp that satisfies those points yet has false arbitrary self-duality.
thinking
**Assessing theorems on D^b(A)**

I'm examining whether we have Phi on D^b(A). It seems the theorem regarding evaluation core identification applies only to finite-dimensional evaluation-generated cores, not all of D^b(A). In Step 3, it claims that pro-Weyl recovery extends Phi to standards, and then to all compact objects in Step 2. They aim to build an exact functor from standards, but I still need to show it preserves exact triangles and is fully faithful. I sense there's a real gap here.
thinking
**Verifying hypotheses**

I’m considering how to approach verifying that the object is indeed a filtered colimit of compact objects. It seems like a straightforward task, but I need to ensure that the three hypotheses are stated correctly. I wonder if there could be any subtleties involved that I might be overlooking. It’s sometimes tricky to navigate these details, but I should take a careful look to confirm everything aligns as it should!
thinking
**Rethinking stabilization concepts**

I’m noticing that "stabilization" seems too strong and perhaps it doesn't match what’s being discussed. They mention something about pro-nilpotent completion and how it relates to inverse systems, which makes me think there might be nuances with filtered colimits that I need to consider. It's interesting how these concepts interconnect and complicate things. I’ll have to explore this more deeply to understand the precise relationships between them.
thinking
**Reviewing mathematical conditions**

I think I've identified a potential issue with this equivalence; it might not hold as stated. The discussion revolves around the Mittag-Leffler condition, but there's a conceptual mismatch between filtered systems and inverse limit towers. To clarify, I need to focus on the compactness of images within pro-nilpotent completions, as the obstruction originates from how Hom interacts with filtered colimits. It's crucial that I ensure everything aligns with the user's request to verify the Mittag-Leffler reduction. Let's scrutinize this further!
thinking
**Analyzing pro-Weyl recovery**

The theorem about pro-Weyl recovery tells us that a specific inverse system, W_m, is Mittag-Leffler (ML). However, the remark suggests that this is sufficient only if the pro-nilpotent completion is constructed from similar towers. I see this as more of a heuristic or conjecture rather than a proven equivalence. I should check if there's an established theorem regarding Ind-completion tautology, as it seems that for Ind-completion, all hypotheses hold tautologically. Let's look into that!
thinking
**Evaluating tautology claims**

The proposition assumes itself, so I think the statement can work as a hypothesis. However, the remark that claims it’s a tautology seems wrong. The user specifically asked about “Ind-completion tautology” for verification. So, yes: the assertion that all three hypotheses hold tautologically for Ind(D^b(A)) is false. At least hypothesis (i) does not seem tautological and could potentially fail. Great!
thinking
**Evaluating theorem steps**

I'm analyzing the theorem's steps, specifically Step 3, which uses derived inverse limits instead of finite cones in D^b(A), which suggests a gap in Step 2. The theorem states that if Dcomp compacts form a thick closure, it must equal Loc<G_Bax>. This adds clarity for Step 1. I might need to cite the theorem's final clause to ensure rigor in the proof. I'm also considering including low-severity AP29 details, while avoiding AP126, AP132, AP165, and AP113 in the audit block.
thinking
**Reviewing potential violations**

I'm assessing if there are any violations for AP126, AP132, AP165, and AP113, but it seems none were found. I need to mention that findings pertain only to problems since the user requested specifics. I might note that the unique environment/status seems okay, and think about AP29 if it's violated.

Next, I’m checking if title line 4492 is part of the recent commit. The diff review indicates that this heading was not inserted recently, meaning AP29 likely isn't introduced by changes, so no need to flag it.
thinking
**Checking for recent changes**

I’m focusing on recent changes, which is good! I should look at the git diff context to determine if the heading was newly added. Since the diff starts with an insertion before the subsection, it indicates that the heading already existed, so no new AP29 violations. I don't see any AP29s within the inserted block, and it seems like there are also no violations for AP126, AP132, AP165, or AP113. I'll check the final line numbers for propositions starting from line 4274.
thinking
**Revising hypotheses clarity**

I’m noticing that my remark about "all three hypotheses hold tautologically" is actually incorrect. I should think about how to strengthen my argument by providing an example from the same category, like considering the direct sum of one simple shifted to all degrees. That might help make the concept clearer and more convincing. I'll have to be precise and thoughtful with my wording to avoid confusion.
codex
- PROBLEM at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4320), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4375), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3758), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:3986): part `(c)` is not proved from the stated hypotheses. `thm:pro-weyl-recovery` only identifies standards as `R\varprojlim W_m` inside the separated completion; it does not construct `\Phi` on an arbitrary `\mathcal D^{\mathrm{comp}}`, show `\Phi` commutes with those limits, or prove equivalence on the compact shifted-prefundamental core. The file itself still marks exactly that extension as conjectural in `conj:dk-compacts-completion` and as the “remaining packet” in `thm:mc3-type-a-resolution`. FIX: remove `(c)` from the proposition, or split the result into a proved proposition `(a)-(b)` plus a conditional/conjectural statement for DK extension. If `(c)` is kept, add an explicit extra hypothesis giving a colimit-preserving extension of `\Phi` to the compact core and prove its compatibility with the pro-Weyl limit construction.

- PROBLEM at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4355): Step 2 imports `thm:shifted-prefundamental-generation` from the separated completion and then concludes generation inside an arbitrary presentable completion `\mathcal D^{\mathrm{comp}}` without any comparison functor. The cited theorem proves the standard-object statement inside `\widehat D(\mathcal O^{\mathrm{sh}}_{\le 0})`, not inside every completion satisfying `(i)-(iii)`. FIX: after Step 1, cite the final conditional clause of `thm:shifted-prefundamental-generation` directly, since Step 1 already establishes its compact-object hypothesis; alternatively add a functor from the separated completion to `\mathcal D^{\mathrm{comp}}` that preserves the Baxter-generated thick subcategory.

- PROBLEM at [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4393), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4425), [chapters/examples/yangians_computations.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/yangians_computations.tex:4433): the remark overstates both the “Ind-completion tautology” and the Mittag-Leffler reduction. Hypothesis `(i)` is stronger than “holds for `\operatorname{Ind}(D^b(\mathcal A))` by construction”; the text gives no reason that every weight piece of every ind-object has bounded cohomological amplitude. Likewise, the jump from compactness against filtered colimits to “equivalent to weightwise Ext stabilization” and then to a Mittag-Leffler condition on an inverse tower is asserted, not proved. FIX: rewrite this as a sufficient-criterion remark: `(ii)` and `(iii)` are tautological for Ind-completion, `(i)` needs separate verification or restriction to a weight-bounded subcategory, and the Francis-Gaitsgory discussion should be phrased as “if the completion is modeled by weightwise Mittag-Leffler towers, then compactness-preservation follows,” not as an equivalence.

Label check: `prop:completion-extension-weight-bounded` is unique across Vol I-III, and the `prop:` prefix matches the environment. No AP126, AP132, AP165, or AP113 issue appears in this inserted block. The status tag `\ClaimStatusProvedHere` is not defensible unless `(c)` is removed or downgraded.
tokens used
101,702
