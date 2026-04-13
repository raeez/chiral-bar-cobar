# A03_symplectic_polar (308s)

**Result**

`FIXED` finding 1 in [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:197): the Verdier involution construction now explicitly assumes the finite-dimensional fiber-cohomology hypothesis from `lem:perfectness-criterion(ii)`, and the `\mathrm{ev}` step is justified by choosing a bounded finite-dimensional model so `\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)`.

`FIXED` finding 2 in [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:484): the C1 theorem now carries the same hypothesis needed for `\sigma`, and its duality clause is restricted to `g \ge 1`, matching the existing genus-0 statement [later in the file](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:710). I also narrowed the Stage 4 proof sentence and the local hypothesis note so the surrounding logic stays coherent.

**Verification**

I re-read the edited regions and checked the corrected patterns with `rg`. `\ref`/`\label` usage on the touched surface remains unchanged. I did not run a TeX build.

One explicit pending propagation note: the same duality/genus-0 surface still appears in `~/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex`, but I left Vol II untouched because this task assigned only the Vol I file. One unrelated pre-existing forbidden-pattern hit remains in this file at lines 778-779 (`---` in a table), outside the audited surface.


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
session id: 019d862a-d9b3-7f13-ad4e-858c891e0667
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: chapters/connections/thqg_symplectic_polarization.tex

FINDINGS: C1 involution sigma uses ev: C_g(A)^{vv} -> C_g(A) without reflexivity.
At lines ~197, 220. The vv construction requires finite-dimensional fiber-cohomology.
Also: Q_g(A) ≅ Q_g(A^!)^v for all g>=0 contradicts Q_0(A^!)=0 at g=0 (lines ~476, 694).

FIXES:
1. Add reflexivity/perfectness hypothesis to the involution construction.
2. Add g>=1 hypothesis to the duality statement, or fix the genus-0 identifications.

Read lines 150-250 and 450-700. Make minimal fixes.
mcp startup: no servers


thinking
**Evaluating task requirements**

I need to assess the file contents and required documents, considering my instructions to prefer using the explorer for summaries over manual reading. There’s a possibility I might need to open a skill, but it’s not explicitly mentioned. I have to check if any paths match the task at hand. If the user asked for fixing audit findings, I’m not sure a skill is necessary unless it clearly applies. Frequent commentary seems helpful for keeping track. I should stick to applying changes only where needed.
thinking
**Checking for forbidden patterns**

After making the edits, I need to re-read the modified file and check for any forbidden patterns. I might run a command like `rg` to search for `Omega/z` and other possible patterns. The instructions specify that I should look for forbidden patterns only in modified files. It seems like I should focus on patterns relevant to the audit, like backticks or em dashes. Although checking all blacklisted patterns sounds extensive, I need to ensure I follow the guidelines about forbidden patterns in the modified files.
codex
I’m reading the required repo-level sources plus the target file sections the audit points to, then I’ll make the smallest edits that add the missing hypothesis and fix the genus-0 overclaim without disturbing the surrounding theorem lane.
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
 exited 1 in 51ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory
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
**Locating file sections**

I need to locate the archive path and read specific sections, like 150-250 and 450-700. I think I might use Explorer for this task. It’s important to find the context of audit findings and dependent labels. Maybe I’ll utilize parallel searches with rg for lines and look for red_team_summary in the archive. I'm considering whether to use claim-surface-sync, but it might not be necessary. Sticking with Explorer for the codebase search seems like the best option!
codex
The repo-level reads are in place; the notes file isn’t at the primary path, so I’m checking the archive copy and the exact target sections now. After that I’ll lock the minimal wording change and patch only this file.
collab spawn_agent(call_hsWdgB1UOZUxXigZTdJCKqbl, prompt="Inspect chapters/connections/thqg_symplectic_polarization.tex around lines 150-250 and 450-700. Identify the exact state…")
spawn_agent(call_hsWdgB1UOZUxXigZTdJCKqbl, prompt="Inspect chapters/connections/thqg_symplectic_polarization.tex around lines 150-250 and 450-700. Identify the exact state…") pending init:
  agent: 019d862b-5734-7281-bd36-7a4ad92b5dd6
mcp startup: no servers
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '450,700p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '150,250p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
 $\overline{\mathcal{M}}_g$.

\item \emph{Functoriality.}
 The assignment $(\cA, \cA^!) \mapsto \mathbf{C}_g(\cA)$
 is functorial in morphisms of Koszul pairs.
\end{enumerate}
\end{proposition}

\begin{proof}
\emph{Part (i).}
The cohomological dimension of $\overline{\mathcal{M}}_g$ is
$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
by Artin vanishing for proper DM stacks
\cite[\S4.1]{Olsson16}. The stalks of
$\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
(finite-dimensional fiber cohomology,
Lemma~\ref{lem:perfectness-criterion}(ii)).
By constructibility of $\mathcal{Z}(\cA)$
(Lemma~\ref{lem:quantum-ss-convergence}, condition (2)),
each cohomology sheaf $R^q\pi_{g*}\barB^{(g)}(\cA)$
 succeeded in 52ms:
is $\overline{\mathcal{M}}_{1,1}$, where the pairing has
degree~$0$. This is the reason genus~$1$ complementarity
has the simplest form:
$Q_1(\cA) \oplus Q_1(\cA^!) \cong H^*(\overline{\mathcal{M}}_{1,1},
\mathcal{Z}(\cA))$ with a classical (unshifted) pairing.
\end{remark}

% ======================================================================
%
% 2. THE UNCONDITIONAL EIGENSPACE DECOMPOSITION (C1)
%
% ======================================================================

\subsection{The unconditional eigenspace decomposition}
\label{subsec:thqg-III-eigenspace-decomposition}
\index{eigenspace decomposition!holographic|textbf}
\index{complementarity!C1 decomposition}

The eigenspace decomposition~(C1) holds unconditionally on the
Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '140,270p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 $Z(\cA) \cong Z(\cA^!)$
 (Lemma~\ref{lem:center-isomorphism}) induce a
 quasi-isomorphism of constructible sheaves on
 $\overline{\mathcal{M}}_g$:
 \begin{equation}\label{eq:thqg-III-verdier-self-duality}
 \mathcal{Z}(\cA)
 \xrightarrow{\;\sim\;}
 \mathbb{D}\,\mathcal{Z}(\cA)[3g - 3],
 \end{equation}
 where $\mathbb{D}$ denotes Verdier duality on
 $\overline{\mathcal{M}}_g$.

\item \emph{Functoriality.}
 The assignment $(\cA, \cA^!) \mapsto \mathbf{C}_g(\cA)$
 is functorial in morphisms of Koszul pairs.
\end{enumerate}
\end{proposition}

\begin{proof}
\emph{Part (i).}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '440,730p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Serre duality on a smooth variety of dimension $3g - 3$.
The three cases follow by substituting $g = 0, 1, \ge 2$.
\end{proof}

\begin{remark}[Genus $1$ distinguished]
\label{rem:thqg-III-genus-1-special}
\index{genus 1!holographic pairing}
At genus~$1$, $\dim \overline{\mathcal{M}}_{1,1} = 1$
but $\dim \overline{\mathcal{M}}_1 = 0$ (a point for the
coarse moduli). The relevant moduli space for marked curves
is $\overline{\mathcal{M}}_{1,1}$, where the pairing has
degree~$0$. This is the reason genus~$1$ complementarity
has the simplest form:
$Q_1(\cA) \oplus Q_1(\cA^!) \cong H^*(\overline{\mathcal{M}}_{1,1},
\mathcal{Z}(\cA))$ with a classical (unshifted) pairing.
\end{remark}

% ======================================================================
%
% 2. THE UNCONDITIONAL EIGENSPACE DECOMPOSITION (C1)

thinking
**Adjusting inspection plans**

I see that I need to focus more on lines around 220 and 694; it seems like those sections may not have enough context. I might need to add more detail between those areas. I also need to wait for some explorer response that’s pending, which could affect my update plan with the necessary steps. This seems nontrivial, so I want to be thorough here to ensure everything is well-covered!
Plan update
Context is loaded. I’m locking the exact bad claims, then patching only the target file and verifying the modified surface plus the relevant forbidden-pattern grep.
  → Pin down the exact sigma/involution and genus-0 duality overclaims in the target file
  • Patch the target file with the smallest truthful hypothesis/scope edits
  • Re-read the edited region and grep the modified file for relevant forbidden patterns
collab wait(call_DUofFXBIDLsKycssjhPlsFup)
  receivers: 019d862b-5734-7281-bd36-7a4ad92b5dd6

thinking
**Summarizing minimal correction suggestions**

I’m outlining minimal truthful edits addressing two issues: first, the evaluation map’s definition requires adding a clear assumption on reflexivity or perfectness of the double dual object around lines 172–200 in `chapters/connections/thqg_symplectic_polarization.tex`, referencing an appropriate lemma or proposition to justify this; second, the duality statement in the theorem near line 520 should be restricted to genus g ≥ 1 to avoid the incorrect isomorphism at g = 0, noting the genus 0 complementarity proposition around line 640. I’ll also highlight that all label references should remain consistent while communicating these changes.
codex
- `chapters/connections/thqg_symplectic_polarization.tex:170-210`—Construction~\ref{constr:thqg-III-verdier-involution} currently composes through the evaluation map `\mathrm{ev}: \mathbf{C}_g(\cA)^{\vee\vee} \to \mathbf{C}_g(\cA)` without any comment that the ambient complex is reflexive/perfect (so that the double dual coincides with the original). Add a short sentence here referencing the finite-dimensionality/constructibility input (e.g., Proposition~\ref{prop:thqg-III-ambient-properties}(i) together with Lemma~\ref{lem:perfectness-criterion}(ii)) to justify the evaluation map. This keeps `\sigma` well defined and leaves the surrounding labels (`\mathrm{KS}`, `\mathbb{D}`) untouched.

- `chapters/connections/thqg_symplectic_polarization.tex:500-560`—The “Duality” clause of Theorem~\ref{thm:thqg-III-eigenspace-decomposition} currently asserts \(Q_g(\cA)\cong Q_g(\cA^!)^\vee\) for all \(g\ge 0\), but Proposition~\ref{prop:thqg-III-genus-0} shows \(Q_0(\cA^!)=0\) while \(Q_0(\cA)=Z(\cA)\), so the isomorphism fails at \(g=0\). Restrict the duality statement to \(g\ge 1\) (or add “for \(g\ge 1\)” with a parenthetical reference to Proposition~\ref{prop:thqg-III-genus-0}) so the theorem matches the later genus‑\(0\) complementarity resolution and keeps the label and equation \eqref{eq:thqg-III-C1-duality} intact.
wait(call_DUofFXBIDLsKycssjhPlsFup) 1 agents complete:
  019d862b-5734-7281-bd36-7a4ad92b5dd6 completed: "- `chapters/connections/thqg_symplectic_polarization.tex:170-210`—Construction~\ref{constr:thqg-III-verdier-involution} …"

thinking
**Inspecting proposition lines**

I need to take a closer look at the lines surrounding the proposition, particularly around line 694. There could be some important context or details that might clarify things for me. It’s always good to check the surrounding lines to understand the broader implications. I want to ensure I'm not missing anything crucial in my analysis, so I’ll focus on those sections now. Let's see what I can find there!
codex
I’ve isolated the two actual overclaims. One is purely a missing reflexivity justification in the `ev` step; the other is a scope leak in the theorem’s duality clause because genus `0` is handled differently later in the same file.
exec
/bin/zsh -lc "sed -n '700,760p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Q_g\\(\\\\cA\\).*Q_g\\(\\\\cA\\"'^!'"\\)|Q_0\\(\\\\cA\\"'^!'"\\)|eq:thqg-III-C1-duality|constr:thqg-III-verdier-involution|ev\\}|double dual|reflex\" chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '210,290p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:Q_g\(\cA\).*Q_g\(\cA\^!\)|Q_0\(\cA\^!\)|eq:thqg-III-C1-duality|constr:thqg-III-verdier-involution|ev\}|double dual|reflex)
            ^^
error: unrecognized escape sequence
 succeeded in 52ms:
\end{equation}
constructed as the composition:
\begin{equation}\label{eq:thqg-III-sigma-composition}
\begin{tikzcd}[column sep=large]
\mathbf{C}_g(\cA)
\arrow[r, "\mathbb{D}"]
&
\mathbf{C}_g(\cA^!)^{\vee}[{-(3g{-}3)}]
\arrow[r, "\mathrm{KS}^{\vee}"]
&
\mathbf{C}_g(\cA)^{\vee\vee}[{-(3g{-}3)}][{3g{-}3}]
\arrow[r, "\mathrm{ev}"]
&
\mathbf{C}_g(\cA)
\end{tikzcd}
\end{equation}
Here $\mathbb{D}$ is the Verdier duality map from
Corollary~\ref{cor:duality-bar-complexes-complete},
$\mathrm{KS}$ is the Koszul identification
$\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 succeeded in 52ms:
\[
Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
\]
\end{proposition}

\begin{proof}
Since $\overline{\mathcal{M}}_0$ is a point, the center
local system has a single stalk $Z(\cA)$. The bar complex
at genus~$0$ is uncurved (the curvature
$\dfib^{\,2} = \kappa(\cA) \cdot \omega_g$ vanishes
because $\omega_0 = 0$), so the Verdier involution acts on
the genus-$0$ center by the identity: bar cochains with
$j_*$-extension are all of $Z(\cA)$, and there are no
$j_!$-extended cochains (the configuration space has no
boundary at genus~$0$).
\end{proof}

\begin{proposition}[Genus-$1$ complementarity;
\ClaimStatusProvedHere]
\label{prop:thqg-III-genus-1}

thinking
**Searching for proofs**

I think I need to use fixed strings or ensure proper escaping, but maybe it's not necessary just yet. I should inspect the line around the involutivity proof, as it likely involves the use of "ev" again. Also, there's a sigma^2 proof that might require a mention of reflexivity. I'll search for occurrences of "ev" and consider using regular expressions for fixed strings. This feels like a logical approach to tackling the problem!
codex
I’ve confirmed the downstream genus-0 proposition already states the exceptional behavior explicitly. The theorem earlier is just outscoping itself, so the surgical fix is to narrow that clause rather than rework the later genus-0 lane.
exec
/bin/zsh -lc "rg -n -F 'Q_g(\\cA) \\;\\cong\\; Q_g(\\cA"'^!)''^{'"\\vee}' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Q_0(\\cA"'^!) = 0'"' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathrm{ev}' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
221:\arrow[r, "\mathrm{ev}"]
230:via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
268:= (\mathrm{ev} \circ \mathrm{KS}'^{\vee} \circ \mathbb{D})
270: (\mathrm{ev} \circ \mathrm{KS}^{\vee} \circ \mathbb{D})
 succeeded in 52ms:
701:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
 succeeded in 52ms:
510:Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
codex
I’m checking the precise nearby hypotheses before patching so the added sentence names an existing local source instead of inventing a new condition. That keeps the construction and proof wording aligned.
exec
/bin/zsh -lc "rg -n -F 'lem:thqg-III-nondegeneracy' -C 3 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'cor:quantum-dual-complete' -C 3 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'prop:thqg-III-ambient-properties' -C 4 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'lem:perfectness-criterion' -C 4 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
122-\end{remark}
123-
124-\begin{proposition}[Properties of the holographic ambient complex;
125-\ClaimStatusProvedHere]
126:\label{prop:thqg-III-ambient-properties}
127-\index{holographic ambient complex!properties}
128-The holographic ambient complex
129-$\mathbf{C}_g(\cA)$ satisfies:
130-\begin{enumerate}[label=\textup{(\roman*)}]
--
197-\begin{construction}[Verdier involution on the ambient complex]
198-\label{constr:thqg-III-verdier-involution}
199-\index{Verdier involution!construction|textbf}
200-The Verdier self-duality of
201:Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
202-the Koszul involutivity
203-$(\cA^!)^! \simeq \cA$
204-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
205-a cochain-level endomorphism
 succeeded in 52ms:
637-needed. The duality statement in Stage~4 uses
638-nondegeneracy but can also be obtained unconditionally from
639-spectral sequence duality
640:(Corollary~\ref{cor:quantum-dual-complete}).
641-
642-\emph{Functoriality.}
643-A morphism $f \colon (\cA, \cA^!) \to (\cB, \cB^!)$
 succeeded in 52ms:
385-
386-\begin{lemma}[Nondegeneracy of the holographic pairing;
387-\ClaimStatusProvedHere]
388:\label{lem:thqg-III-nondegeneracy}
389-\index{Verdier pairing!nondegeneracy}
390-When the relative bar family is perfect
391-\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})},
--
628-(isotropy from anti-symmetry of $\sigma$),
629-$v$ lies in the radical of the full pairing on
630-$\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
631:(Lemma~\ref{lem:thqg-III-nondegeneracy}).
632-
633-\emph{Note on unconditionality.}
634-Stages 1--3 use only $\sigma^2 = \id$ and the
--
939- \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
940-\item \emph{Nondegeneracy:} the holographic Verdier pairing
941- $\langle -, - \rangle_g$ is nondegenerate
942: \textup{(}Lemma~\textup{\ref{lem:thqg-III-nondegeneracy})}.
 succeeded in 51ms:
99-where $\mathcal{Z}(\cA)$ is the center local system on the
100-Deligne--Mumford--Knudsen compactification
101-$\overline{\mathcal{M}}_g$. When $g \ge 2$ and the relative bar
102-family is perfect
103:(Lemma~\ref{lem:perfectness-criterion}), the fiber--center
104-identification
105-(Theorem~\ref{thm:fiber-center-identification}) gives
106-\begin{equation}\label{eq:thqg-III-bar-center}
107-\mathbf{C}_g(\cA)
--
162-by Artin vanishing for proper DM stacks
163-\cite[\S4.1]{Olsson16}. The stalks of
164-$\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
165-(finite-dimensional fiber cohomology,
166:Lemma~\ref{lem:perfectness-criterion}(ii)).
167-By constructibility of $\mathcal{Z}(\cA)$
168-(Lemma~\ref{lem:quantum-ss-convergence}, condition (2)),
169-each cohomology sheaf $R^q\pi_{g*}\barB^{(g)}(\cA)$
170-is a constructible sheaf on the Noetherian stack
--

thinking
**Evaluating ambient properties**

I need to consider opening a proposition on ambient properties to determine if it mentions finite-dimensional aspects. This seems crucial for understanding any underlying concepts related to dimensions. I’m curious how finite-dimensional context might affect the proposition. It feels a bit abstract at the moment, but I'm eager to break it down further. Let’s approach this detail by detail to clarify what needs to be addressed regarding those properties.
exec
/bin/zsh -lc "sed -n '124,190p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{proposition}[Properties of the holographic ambient complex;
\ClaimStatusProvedHere]
\label{prop:thqg-III-ambient-properties}
\index{holographic ambient complex!properties}
The holographic ambient complex
$\mathbf{C}_g(\cA)$ satisfies:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{Finite-dimensionality.}
 For each $n \in \mathbb{Z}$,
 $H^n(\mathbf{C}_g(\cA))$ is finite-dimensional over
 $\mathbb{C}$, and is nonzero only for
 $0 \le n \le 6g - 6$.

\item \emph{Verdier self-duality.}
 The Koszul pairing
 $\cA \otimes \cA^! \to \omega_X$ and the center isomorphism
 $Z(\cA) \cong Z(\cA^!)$
 (Lemma~\ref{lem:center-isomorphism}) induce a
 quasi-isomorphism of constructible sheaves on
 $\overline{\mathcal{M}}_g$:

thinking
**Exploring finite-dimensional cohomology**

I’m considering whether I need to prove reflexivity in the context of finite-dimensional cohomology. I should start with a minimal truthful statement. However, I'm facing challenges with the evaluation map on the complex level compared to the cohomology level. Perhaps for the cochain-level endomorphism to be well-defined, I need to check if the ambient complex is perfect or find a suitable model. I should also look into the assumptions made when the relative bar family is perfect for g ≥ 2. I’ll review the earlier sections between lines 80-120 for additional context.
exec
/bin/zsh -lc "sed -n '80,130p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{subsec:thqg-III-ambient-complex}
\index{ambient complex|textbf}
\index{Verdier involution!on ambient complex}

The starting point is the datum of a chiral Koszul pair
$(\cA, \cA^!)$ on a smooth projective curve $X$ over $\mathbb{C}$.
The five main theorems (A--D+H) of Part~\ref{part:bar-complex} supply the following
chain of identifications.

\begin{definition}[Holographic ambient complex]
\label{def:thqg-III-holographic-ambient}
\index{holographic ambient complex|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair and let $g \ge 0$.
The \emph{holographic ambient complex} at genus~$g$ is the cochain
complex
\begin{equation}\label{eq:thqg-III-holographic-ambient}
\mathbf{C}_g(\cA)
:= \RGamma(\overline{\mathcal{M}}_g, \mathcal{Z}(\cA)),
\end{equation}
where $\mathcal{Z}(\cA)$ is the center local system on the

thinking
**Investigating construction definitions**

I’m thinking about how the concept of "cochain-level endomorphism" can be defined after selecting a finite-dimensional model. There might not be extra theorem hypotheses needed beyond the assumption of finite-dimensional fiber-cohomology. I need to check if there’s already an existing hypothesis in the file regarding the fibrous structure being finite-dimensional, especially near the start of the document. This will help me clarify the approach I should take next.
exec
/bin/zsh -lc "rg -n -F 'finite-dimensional fiber cohomology' -C 3 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
162-by Artin vanishing for proper DM stacks
163-\cite[\S4.1]{Olsson16}. The stalks of
164-$\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
165:(finite-dimensional fiber cohomology,
166-Lemma~\ref{lem:perfectness-criterion}(ii)).
167-By constructibility of $\mathcal{Z}(\cA)$
168-(Lemma~\ref{lem:quantum-ss-convergence}, condition (2)),
--
1768-PBW filterability holds by the PBW theorem for vertex algebras
1769-at non-critical level $k \ne -h^{\vee}$
1770-(Proposition~\ref{prop:pbw-universality}).
1771:The bar complex has finite-dimensional fiber cohomology
1772-because $\widehat{\mathfrak{g}}_k$ is Koszul
1773-(Corollary~\ref{cor:universal-koszul}).
1774-Both (H1) and (H2) hold.
exec
/bin/zsh -lc "rg -n -F 'Throughout' -C 2 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

codex
Before I patch, I’m resolving one local consistency point: if `sigma` only exists on a reflexive model, the theorem that uses it must at least phrase the duality/splitting relative to that model. I’m checking whether the file already packages finite-dimensionality as a standing property or whether I need one short qualifier in the theorem lead-in as well.
exec
/bin/zsh -lc "rg -n -F 'finite-dimensional by hypothesis' -C 3 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'eigenspace decomposition (C1) holds unconditionally' -C 3 chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\label{lem:perfectness-criterion}' -C 8 chapters/connections/thqg_symplectic_polarization.tex chapters/theory/*.tex appendices/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
161-$2 \dim_{\mathbb{C}} \overline{\mathcal{M}}_g = 2(3g - 3) = 6g - 6$
162-by Artin vanishing for proper DM stacks
163-\cite[\S4.1]{Olsson16}. The stalks of
164:$\mathcal{Z}(\cA)$ are finite-dimensional by hypothesis
165-(finite-dimensional fiber cohomology,
166-Lemma~\ref{lem:perfectness-criterion}(ii)).
167-By constructibility of $\mathcal{Z}(\cA)$
 exited 1 in 51ms:

 succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex-272-$C^{(g)}_X(\cA)\!\mid_\Sigma$, i.e.\ the bar complex of~$\cA$
chapters/theory/higher_genus_complementarity.tex-273-on the fixed curve~$\Sigma$ with the fiberwise curved
chapters/theory/higher_genus_complementarity.tex-274-differential~$\dfib$
chapters/theory/higher_genus_complementarity.tex-275-\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/higher_genus_complementarity.tex-276-\end{definition}
chapters/theory/higher_genus_complementarity.tex-277-
chapters/theory/higher_genus_complementarity.tex-278-\begin{lemma}[Perfectness criterion for the relative bar family;
chapters/theory/higher_genus_complementarity.tex-279-\ClaimStatusProvedHere]
chapters/theory/higher_genus_complementarity.tex:280:\label{lem:perfectness-criterion}
chapters/theory/higher_genus_complementarity.tex-281-\index{perfectness criterion|textbf}
chapters/theory/higher_genus_complementarity.tex-282-\index{bar complex!relative perfectness|textbf}
chapters/theory/higher_genus_complementarity.tex-283-Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
chapters/theory/higher_genus_complementarity.tex-284-curve~$X$, carrying a modular pre-Koszul datum
chapters/theory/higher_genus_complementarity.tex-285-\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_complementarity.tex-286-Suppose the following two conditions hold:
chapters/theory/higher_genus_complementarity.tex-287-\begin{enumerate}[label=\textup{(\roman*)}]
chapters/theory/higher_genus_complementarity.tex-288-\item \emph{PBW filterability.}

thinking
**Inspecting lemma criterion**

I see that I need to quickly check the lemma perfectness criterion along with its conditions. This is important for ensuring accuracy, but I'm wondering if I have all the necessary details and specific requirements at hand. Maybe I should outline what perfection looks like in this context to guide my inspection. Let’s get started on clarifying these conditions and ensure I have everything I need to proceed effectively!
exec
/bin/zsh -lc "sed -n '278,340p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{lemma}[Perfectness criterion for the relative bar family;
\ClaimStatusProvedHere]
\label{lem:perfectness-criterion}
\index{perfectness criterion|textbf}
\index{bar complex!relative perfectness|textbf}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
curve~$X$, carrying a modular pre-Koszul datum
\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
Suppose the following two conditions hold:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \emph{PBW filterability.}
 The genus-$g$ bar complex $\bar{B}^{(g)}(\cA)$ admits an
 exhaustive multiplicative filtration~$F_\bullet$ such that the
 associated graded $\operatorname{gr}_F \bar{B}^{(g)}(\cA)$
 sees only the genus-$0$ collision differential~$\dzero$ and is
 Koszul-acyclic \textup{(}axioms \textup{MK1} and
 \textup{MK3} of
 Definition~\textup{\ref{def:modular-koszul-chiral})}.

\item \emph{Finite-dimensional fiber cohomology.}


thinking
**Considering cohomology properties**

I realize Proposition (i) yields finite-dimensional cohomology, meaning any bounded complex of finite-dimensional cohomology over a field is quasi-isomorphic to a bounded finite-dimensional complex. This should be sufficient for reflexivity, right? But wait—Proposition (i) is unconditional, even if its proof relies on a finite-dimensional hypothesis. Hm, it seems a bit sloppy; the audit finding points out that `vv` needs finite-dimensional fiber-cohomology, implying they want an explicit hypothesis after all.
thinking
**Considering template requirements**

I think there’s no need to change the proposition statement. I might want to include the PE-10 template in the commentary, especially since we're addressing the scope quantifier theorem. I’ll need to fill PE-10 and potentially PE-2, but not kappa. Following AGENTS' guidelines, since we're touching a hot zone, I should run the pre-edit verification protocol. We should end with a commentary fenced block and accept any necessary changes for the duality statement.
codex
```text
genus: [g>=1 for the duality clause; g=0 handled separately in Proposition~\ref{prop:thqg-III-genus-0}]
degree: [all cohomological degrees]
AP32 weight tag: [NA]
tagged? [Y]
AP139 free-var audit: LHS vars:{g,\cA} RHS vars:{g,\cA} LHS⊇RHS? [Y]
AP36: [implies]  if iff, converse proved same thm? [NA]
verdict: ACCEPT
```
codex
I’m patching three tight spots in the same theorem lane: the construction sentence that creates `ev`, the theorem lead-in so it matches that construction, and the duality clause/proof note so genus `0` is excluded where the file itself later excludes it.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex
@@ -203,3 +203,5 @@
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
@@ -230,3 +232,9 @@
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
@@ -467,4 +475,6 @@
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
@@ -477,2 +487,6 @@
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
@@ -506,3 +520,3 @@
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
@@ -620,4 +634,5 @@
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
@@ -632,7 +647,8 @@
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).

file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).


thinking
**Verifying theorem coherence**

I need to re-read the edited sections to verify their coherence. I’m wondering if the theorem statement is now consistent with proposition genus0, but it still mentions g≥0 and has an assumption. The duality clause refers to g≥1, while the S-level decomposition remains for g≥0. I should check if the "finite-dimensional fiber-cohomology hypothesis" of the lemma in the theorem introduction is valid for all g≥0, but I might be overthinking it. Time for a re-read.
exec
/bin/zsh -lc "sed -n '197,245p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '468,646p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '694,710p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{construction}[Verdier involution on the ambient complex]
\label{constr:thqg-III-verdier-involution}
\index{Verdier involution!construction|textbf}
The Verdier self-duality of
Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
the Koszul involutivity
$(\cA^!)^! \simeq \cA$
(Theorem~\ref{thm:chiral-koszul-duality}), under the
finite-dimensional fiber-cohomology hypothesis of
Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
a cochain-level endomorphism
\begin{equation}\label{eq:thqg-III-sigma-def}
\sigma
\colon
\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)
\end{equation}
constructed as the composition:
\begin{equation}\label{eq:thqg-III-sigma-composition}
\begin{tikzcd}[column sep=large]
\mathbf{C}_g(\cA)
 succeeded in 52ms:
%
% ======================================================================

\subsection{The unconditional eigenspace decomposition}
\label{subsec:thqg-III-eigenspace-decomposition}
\index{eigenspace decomposition!holographic|textbf}
\index{complementarity!C1 decomposition}

Under the finite-dimensional fiber-cohomology hypothesis needed
for Construction~\ref{constr:thqg-III-verdier-involution}, the
eigenspace decomposition~(C1) holds on the Koszul locus without
any additional nondegeneracy hypothesis.
We give a self-contained proof in the holographic setting.

\begin{theorem}[Holographic eigenspace decomposition (C1);
\ClaimStatusProvedHere]
\label{thm:thqg-III-eigenspace-decomposition}
\index{Lagrangian!eigenspace decomposition!holographic}
Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
 succeeded in 51ms:
\label{cor:thqg-III-dimension-parity}
For a Koszul self-dual chiral algebra $\cA \cong \cA^!$ and
$g \ge 1$, the total dimension
$\dim \mathcal{H}_g(\cA)$ is even.
\end{corollary}

\begin{proof}
Self-duality gives $Q_g(\cA) \cong Q_g(\cA^!)$, so
$\dim Q_g(\cA) = \dim Q_g(\cA^!)$ and
$\dim \mathcal{H}_g(\cA)
= 2 \dim Q_g(\cA)$
(Theorem~\ref{thm:self-dual-halving}).
\end{proof}

\begin{proposition}[Genus-$0$ complementarity;
\ClaimStatusProvedHere]
\label{prop:thqg-III-genus-0}
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).

exec
/bin/zsh -lc "sed -n '646,656p' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Lemma~\ref{lem:thqg-III-nondegeneracy}).

\emph{Note on hypotheses.}
Stages 1--3 use only $\sigma^2 = \id$ and the
identification of $\sigma$-eigenspaces with $j_*/j_!$
extensions once $\sigma$ is defined on a reflexive model.
No additional nondegeneracy hypothesis is needed. The duality
statement in Stage~4 for $g \ge 1$ uses
nondegeneracy but can also be obtained unconditionally from
spectral sequence duality
(Corollary~\ref{cor:quantum-dual-complete}).
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).

codex
The patch is in. I’m doing the hostile reread now and then a grep pass on the modified file: one pass for the two corrected claim patterns, one pass for local prose/forbidden-pattern regressions.
exec
/bin/zsh -lc "rg -n -F 'Q_g(\\cA) \\;\\cong\\; Q_g(\\cA"'^!)''^{'"\\vee}' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '\\mathrm{ev}' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Q_0(\\cA"'^!) = 0'"' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -i 'moreover|additionally|notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|delve|leverage|tapestry|cornerstone|journey|navigate|---|—' chapters/connections/thqg_symplectic_polarization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
223:\arrow[r, "\mathrm{ev}"]
232:via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
276:= (\mathrm{ev} \circ \mathrm{KS}'^{\vee} \circ \mathbb{D})
278: (\mathrm{ev} \circ \mathrm{KS}^{\vee} \circ \mathbb{D})
 succeeded in 51ms:
524:Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
 succeeded in 51ms:
717:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
 succeeded in 52ms:
778:Obstruction & $\kappa$ & --- \\
779:Deformation & --- & $\lambda_1$ \\
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).

Plan update
The target file is patched and re-read. Verification grep confirmed the corrected claim patterns; the only forbidden-pattern hit was an unrelated pre-existing `---` table placeholder later in the file, outside the audited surface.
  ✓ Pin down the exact sigma/involution and genus-0 duality overclaims in the target file
  ✓ Patch the target file with the smallest truthful hypothesis/scope edits
  ✓ Re-read the edited region and grep the modified file for relevant forbidden patterns
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).


thinking
**Clarifying theorem edits**

I need to perform more grep searches to ensure the theorem clause has g≥1 without any overclaims in the edited sections. I might search specifically for `Q_g(\cA) \cong`, which could be enough. I'll also run `rg -n -F 'unconditionally on the Koszul locus'` since the phrase may have changed. Inspecting exact line numbers after edits might be necessary, and I can use nl -ba for that. Additionally, I'll mention any blocked or fixed lines and ensure I get the line references right in the final output.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '197,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '490,650p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_symplectic_polarization.tex | sed -n '710,720p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   197	\begin{construction}[Verdier involution on the ambient complex]
   198	\label{constr:thqg-III-verdier-involution}
   199	\index{Verdier involution!construction|textbf}
   200	The Verdier self-duality of
   201	Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
   202	the Koszul involutivity
   203	$(\cA^!)^! \simeq \cA$
   204	(Theorem~\ref{thm:chiral-koszul-duality}), under the
   205	finite-dimensional fiber-cohomology hypothesis of
   206	Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
   207	a cochain-level endomorphism
   208	\begin{equation}\label{eq:thqg-III-sigma-def}
   209	\sigma
   210	\colon
   211	\mathbf{C}_g(\cA) \longrightarrow \mathbf{C}_g(\cA)
   212	\end{equation}
   213	constructed as the composition:
   214	\begin{equation}\label{eq:thqg-III-sigma-composition}
   215	\begin{tikzcd}[column sep=large]
   216	\mathbf{C}_g(\cA)
 succeeded in 51ms:
   490	Construction~\ref{constr:thqg-III-verdier-involution} is defined
   491	on a reflexive model of $\mathbf{C}_g(\cA)$.
   492	
   493	\smallskip\noindent
   494	\textbf{H-level.}\;
   495	The Verdier involution $\sigma$ of
   496	Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
   497	splits the ambient complex:
   498	\begin{equation}\label{eq:thqg-III-C1-homotopy}
   499	\mathbf{C}_g(\cA)
   500	\;\simeq\;
   501	\mathbf{Q}_g(\cA) \;\oplus\; \mathbf{Q}_g(\cA^!),
   502	\end{equation}
   503	where
   504	$\mathbf{Q}_g(\cA) := \operatorname{fib}(\sigma - \id)$ and
   505	$\mathbf{Q}_g(\cA^!) := \operatorname{fib}(\sigma + \id)$
   506	are the homotopy eigenspaces.
   507	
   508	\smallskip\noindent
   509	\textbf{S-level.}\;
 succeeded in 51ms:
   710	\label{prop:thqg-III-genus-0}
   711	\index{complementarity!genus 0}
   712	At genus~$0$, $\overline{\mathcal{M}}_0 = \mathrm{pt}$ and
   713	$\mathcal{H}_0(\cA) = Z(\cA)$.
   714	The Verdier involution $\sigma$ acts as $+\id$ on $Z(\cA)$,
   715	giving:
   716	\[
   717	Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
   718	\]
   719	\end{proposition}
   720	
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).




thinking
**Evaluating theorem construction**

I’m thinking maybe I need to add line numbers around the theorem introduction. I wonder if the construction statement at line 204 adequately captures the finite-dimensional fiber-cohomology hypothesis of the lemma that combines to produce sigma. 

Actually, for a bounded finite-dimensional model, we don't necessarily need PBW filterability, which is interesting. I’m also considering how citing part (ii) is acceptable because it’s merely stating finite-dimensional fiber cohomology. I think that’s okay then!
thinking
**Applying AGENTS cross-volume rule**

I'm considering the AGENTS cross-volume rule, which states that when a task interacts with shared formulas, theorem statuses, definitions, notation, bridge claims, chapter references, or hardcoded expected values, I need to grep before and after editing. I suspect that the theorem in question may be duplicated in volume 2. 

Since I'm addressing theorem wording, I should check for files like `thqg_symplectic_polarization.tex` in that volume. The user has only targeted one file, but the cross-volume rule requires mentioning any pending note for untouched collisions.
thinking
**Searching for duplicates**

I need to grep before and after editing to ensure I'm checking across volumes for any duplicate labels or identical statements. Since I skipped this step before, I should search for the same labels in volume 2 now. 

I'll look for `constr:thqg-III-verdier-involution`, `eq:thqg-III-C1-duality`, `thm:thqg-III-eigenspace-decomposition`, and possibly `Q_0(\cA^!) = 0`. If I find any duplicates in volume 2, I should add an explicit pending note because the action safety rules prevent editing other files. Let's get started on that search!
codex
I’m doing one last propagation check across the three-volume surface for the exact labels and formulas I touched. If a duplicate exists outside the assigned file, I’ll leave it as an explicit pending collision rather than silently drifting it.
exec
/bin/zsh -lc "rg -n -F 'Q_0(\\cA"'^!) = 0'"' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'constr:thqg-III-verdier-involution' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Q_g(\\cA) \\;\\cong\\; Q_g(\\cA"'^!)''^{'"\\vee}' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'thm:thqg-III-eigenspace-decomposition' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:510:Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:524:Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
 succeeded in 55ms:
/Users/raeez/chiral-bar-cobar-vol2/main.tex:795:\phantomsection\label{V1-constr:thqg-III-verdier-involution}%
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:242:/bin/zsh -lc 'rg -n "constr:thqg-III-verdier-involution|prop:thqg-III-involutivity|lem:eigenspace-decomposition-complete|lem:quantum-from-ss|cor:quantum-dual-complete|lem:thqg-III-nondegeneracy|thm:thqg-III-eigenspace-decomposition|Holographic eigenspace decomposition" chapters metadata' in /Users/raeez/chiral-bar-cobarexec
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:278:metadata/label_index.json:3570:  "constr:thqg-III-verdier-involution": {
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:285:metadata/claims.jsonl:904:{"label": "prop:thqg-III-involutivity", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 237, "title": "Involutivity and anti-symmetry", "labels_in_block": ["prop:thqg-III-involutivity", "eq:thqg-III-anti-symmetry"], "refs_in_block": ["constr:thqg-III-verdier-involution"]}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:742:   482	Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:911:   240	Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:955:   198	\label{constr:thqg-III-verdier-involution}
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R11_thqg_symplectic_polarization.md:380:Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:198:\label{constr:thqg-III-verdier-involution}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:248:Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:477:for Construction~\ref{constr:thqg-III-verdier-involution}, the
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:490:Construction~\ref{constr:thqg-III-verdier-involution} is defined
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:496:Construction~\textup{\ref{constr:thqg-III-verdier-involution}}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:612:(Construction~\ref{constr:thqg-III-verdier-involution}),
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:3570:  "constr:thqg-III-verdier-involution": {
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl:904:{"label": "prop:thqg-III-involutivity", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 237, "title": "Involutivity and anti-symmetry", "labels_in_block": ["prop:thqg-III-involutivity", "eq:thqg-III-anti-symmetry"], "refs_in_block": ["constr:thqg-III-verdier-involution"]}
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl:908:{"label": "thm:thqg-III-eigenspace-decomposition", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 474, "title": "Holographic eigenspace decomposition (C1)", "labels_in_block": ["thm:thqg-III-eigenspace-decomposition", "eq:thqg-III-C1-homotopy", "eq:thqg-III-C1-shadow", "eq:thqg-III-C1-duality"], "refs_in_block": ["constr:thqg-III-verdier-involution"]}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:194:% label removed: constr:thqg-III-verdier-involution
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:236:Construction~\textup{\ref{V1-constr:thqg-III-verdier-involution}}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:482:Construction~\textup{\ref{V1-constr:thqg-III-verdier-involution}}
 succeeded in 56ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:701:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:717:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:1112:   701	Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:1156:chapters/connections/thqg_symplectic_polarization.tex:701:Q_0(\cA) = Z(\cA), \qquad Q_0(\cA^!) = 0.
 succeeded in 56ms:
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:940:  thm_thqg_III_eigenspace_decomposition [label="thm:thqg-III-eigenspace-decomposition\ntheorem [Pr]\nHolographic eigenspace decomposition (C1...", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/metadata/theorem_registry.md:3065:| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:127:metadata/dependency_graph.dot:940:  thm_thqg_III_eigenspace_decomposition [label="thm:thqg-III-eigenspace-decomposition\ntheorem [Pr]\nHolographic eigenspace decomposition (C1...", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:130:metadata/theorem_registry.md:3065:| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:209:| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:242:/bin/zsh -lc 'rg -n "constr:thqg-III-verdier-involution|prop:thqg-III-involutivity|lem:eigenspace-decomposition-complete|lem:quantum-from-ss|cor:quantum-dual-complete|lem:thqg-III-nondegeneracy|thm:thqg-III-eigenspace-decomposition|Holographic eigenspace decomposition" chapters metadata' in /Users/raeez/chiral-bar-cobarexec
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:268:metadata/dependency_graph.dot:940:  thm_thqg_III_eigenspace_decomposition [label="thm:thqg-III-eigenspace-decomposition\ntheorem [Pr]\nHolographic eigenspace decomposition (C1...", style=filled, fillcolor="#c8e6c9"];
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:277:metadata/theorem_registry.md:3065:| `thm:thqg-III-eigenspace-decomposition` | `theorem` | 474 | Holographic eigenspace decomposition (C1) |
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:284:metadata/label_index.json:49730:  "thm:thqg-III-eigenspace-decomposition": {
/Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/T04_thm_C1.md:734:   474	\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:49730:  "thm:thqg-III-eigenspace-decomposition": {
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl:908:{"label": "thm:thqg-III-eigenspace-decomposition", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/connections/thqg_symplectic_polarization.tex", "line": 474, "title": "Holographic eigenspace decomposition (C1)", "labels_in_block": ["thm:thqg-III-eigenspace-decomposition", "eq:thqg-III-C1-homotopy", "eq:thqg-III-C1-shadow", "eq:thqg-III-C1-duality"], "refs_in_block": ["constr:thqg-III-verdier-involution"]}
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R11_thqg_symplectic_polarization.md:430:474:\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/rectification_20260412_233715/R11_thqg_symplectic_polarization.md:436:1016:(Theorem~\ref{thm:thqg-III-eigenspace-decomposition}), the
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:484:\label{thm:thqg-III-eigenspace-decomposition}
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:1032:(Theorem~\ref{thm:thqg-III-eigenspace-decomposition}), the
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_entanglement_programme.tex:168:(Theorem~\ref{thm:thqg-III-eigenspace-decomposition}).
/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_entanglement_programme.tex:517:(Theorem~\ref{thm:thqg-III-eigenspace-decomposition}).
/Users/raeez/chiral-bar-cobar-vol2/main.tex:973:\phantomsection\label{V1-thm:thqg-III-eigenspace-decomposition}%
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex:474:% label removed: thm:thqg-III-eigenspace-decomposition
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).


thinking
**Considering metadata updates**

I’m noticing that there's a cross-volume duplicate in vol2. The action safety guideline says I should only edit what's assigned, and I need to add an explicit pending note. That sounds good! I’m thinking about the metadata—maybe it needs fixing? But no user asked for that, just the file itself. The theorem_registry metadata might now have stale line numbers since we didn’t regenerate them, though I wonder if it's really necessary to address that. Running `git diff -- chapters/...` for a summary could be useful.
exec
/bin/zsh -lc 'git diff -- chapters/connections/thqg_symplectic_polarization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).


thinking
**Investigating git status**

I’m pondering why the git diff might show empty output. Could it be that the repository isn’t under git or that the file is untracked? I notice that apply_patch changed the file, so that’s interesting. I wonder if the CRLF could affect the output. If the repository isn’t in git, that might explain things. Checking the status seems necessary, especially since maybe the file is already committed, but I’ll confirm with git status -sb.
codex
I found a genuine cross-volume collision surface: the same genus-0 formula and duality line still appear in `~/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex`. The current task only assigned the Vol I file, so I’m leaving that as an explicit pending propagation note rather than drifting Vol II silently.
exec
/bin/zsh -lc 'git rev-parse --is-inside-work-tree' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short -- chapters/connections/thqg_symplectic_polarization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
true
 succeeded in 51ms:

file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).


thinking
**Considering test structure**

I need to mention if no tests are run. Perhaps saying something like, "No TeX build run; command-level verification only" would be good. I want to make sure there are no nested bullets in the output. Keeping it concise with 2-3 sections seems like a solid plan. This approach should help maintain clarity while ensuring the information is easily digestible for the user. Let's focus on getting this right!
codex
**Result**

`FIXED` finding 1 in [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:197): the Verdier involution construction now explicitly assumes the finite-dimensional fiber-cohomology hypothesis from `lem:perfectness-criterion(ii)`, and the `\mathrm{ev}` step is justified by choosing a bounded finite-dimensional model so `\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)`.

`FIXED` finding 2 in [thqg_symplectic_polarization.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:484): the C1 theorem now carries the same hypothesis needed for `\sigma`, and its duality clause is restricted to `g \ge 1`, matching the existing genus-0 statement [later in the file](/Users/raeez/chiral-bar-cobar/chapters/connections/thqg_symplectic_polarization.tex:710). I also narrowed the Stage 4 proof sentence and the local hypothesis note so the surrounding logic stays coherent.

**Verification**

I re-read the edited regions and checked the corrected patterns with `rg`. `\ref`/`\label` usage on the touched surface remains unchanged. I did not run a TeX build.

One explicit pending propagation note: the same duality/genus-0 surface still appears in `~/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex`, but I left Vol II untouched because this task assigned only the Vol I file. One unrelated pre-existing forbidden-pattern hit remains in this file at lines 778-779 (`---` in a table), outside the audited surface.
file update:
diff --git a/chapters/connections/thqg_symplectic_polarization.tex b/chapters/connections/thqg_symplectic_polarization.tex
index 194ef8b73df038275fd676cc19903cfbaa67d0e9..1af3c51d050035b7b5d8c1b3dec86cb9f75511f6
--- a/chapters/connections/thqg_symplectic_polarization.tex
+++ b/chapters/connections/thqg_symplectic_polarization.tex
@@ -201,7 +201,9 @@
 Proposition~\ref{prop:thqg-III-ambient-properties}(ii) and
 the Koszul involutivity
 $(\cA^!)^! \simeq \cA$
-(Theorem~\ref{thm:chiral-koszul-duality}) combine to produce
+(Theorem~\ref{thm:chiral-koszul-duality}), under the
+finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), combine to produce
 a cochain-level endomorphism
 \begin{equation}\label{eq:thqg-III-sigma-def}
 \sigma
@@ -228,7 +230,13 @@
 $\mathrm{KS}$ is the Koszul identification
 $\mathbf{C}_g(\cA) \xrightarrow{\sim} \mathbf{C}_g(\cA^!)$
 via Lemma~\ref{lem:center-isomorphism}, and $\mathrm{ev}$
-is the evaluation map. The shifts cancel, and the composition
+is the evaluation map. Under the same finite-dimensional
+fiber-cohomology hypothesis,
+Proposition~\ref{prop:thqg-III-ambient-properties}(i) gives
+finite-dimensional cohomology for $\mathbf{C}_g(\cA)$, so we may
+choose a bounded finite-dimensional model and hence identify
+$\mathbf{C}_g(\cA)^{\vee\vee} \cong \mathbf{C}_g(\cA)$.
+The shifts cancel, and the composition
 is well-defined as a cochain map of degree zero.
 \end{construction}
 
@@ -465,8 +473,10 @@
 \index{eigenspace decomposition!holographic|textbf}
 \index{complementarity!C1 decomposition}
 
-The eigenspace decomposition~(C1) holds unconditionally on the
-Koszul locus, requiring no perfectness or nondegeneracy hypotheses.
+Under the finite-dimensional fiber-cohomology hypothesis needed
+for Construction~\ref{constr:thqg-III-verdier-involution}, the
+eigenspace decomposition~(C1) holds on the Koszul locus without
+any additional nondegeneracy hypothesis.
 We give a self-contained proof in the holographic setting.
 
 \begin{theorem}[Holographic eigenspace decomposition (C1);
@@ -475,6 +485,10 @@
 \index{Lagrangian!eigenspace decomposition!holographic}
 Let $(\cA, \cA^!)$ be a chiral Koszul pair on a smooth projective
 curve $X$ over $\mathbb{C}$, and let $g \ge 0$.
+Assume the finite-dimensional fiber-cohomology hypothesis of
+Lemma~\ref{lem:perfectness-criterion}(ii), so that
+Construction~\ref{constr:thqg-III-verdier-involution} is defined
+on a reflexive model of $\mathbf{C}_g(\cA)$.
 
 \smallskip\noindent
 \textbf{H-level.}\;
@@ -504,7 +518,7 @@
 $Q_g(\cA^!) = \ker(\sigma + \id)$.
 
 \smallskip\noindent
-\textbf{Duality.}\;
+\textbf{Duality for $g \ge 1$.}\;
 The Verdier pairing restricts to a perfect duality
 \begin{equation}\label{eq:thqg-III-C1-duality}
 Q_g(\cA) \;\cong\; Q_g(\cA^!)^{\vee}.
@@ -618,8 +632,9 @@
 = H^*(\mathbf{C}_g^+) \oplus H^*(\mathbf{C}_g^-)
 = Q_g(\cA) \oplus Q_g(\cA^!).
 \]
-The duality $Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from
-the Verdier pairing. For $v \in Q_g(\cA)$ and
+For $g \ge 1$, the duality
+$Q_g(\cA) \cong Q_g(\cA^!)^{\vee}$ follows from the Verdier
+pairing. For $v \in Q_g(\cA)$ and
 $w \in Q_g(\cA^!)$, the pairing $\langle v, w \rangle_g$
 is nondegenerate: if $\langle v, w \rangle_g = 0$ for all
 $w \in Q_g(\cA^!)$, then $v$ lies in the radical of the
@@ -630,11 +645,12 @@
 $\mathcal{H}_g(\cA)$, which is zero by nondegeneracy
 (Lemma~\ref{lem:thqg-III-nondegeneracy}).
 
-\emph{Note on unconditionality.}
+\emph{Note on hypotheses.}
 Stages 1--3 use only $\sigma^2 = \id$ and the
 identification of $\sigma$-eigenspaces with $j_*/j_!$
-extensions. No perfectness or nondegeneracy hypothesis is
-needed. The duality statement in Stage~4 uses
+extensions once $\sigma$ is defined on a reflexive model.
+No additional nondegeneracy hypothesis is needed. The duality
+statement in Stage~4 for $g \ge 1$ uses
 nondegeneracy but can also be obtained unconditionally from
 spectral sequence duality
 (Corollary~\ref{cor:quantum-dual-complete}).

tokens used
118,895
