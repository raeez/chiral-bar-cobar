# T17_chirhoch1_KM (448s, gpt-5.4)

[CRITICAL] [chapters/theory/chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2041) — The written proof of `prop:chirhoch1-affine-km` does not actually compute `\ChirHoch^1`. It replaces the full chiral Hochschild complex by a 3-term diagonal-bimodule resolution and treats a degree-1 cochain as just a unary map on generators. But the actual cochain definition in the same file is all-arity, not unary-only: see [definition of `C^\bullet_{\mathrm{ch}}`](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:299). The only general comparison theorem I found, [Hochschild via bar-cobar](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:324), gives `\ChirHoch \simeq \mathrm{Hom}(\Omega^{\mathrm{ch}}\bar B^{\mathrm{ch}}(\cA),\cA)`, not the specific finite resolution used here. So the jump to `\ChirHoch^1(V_k(\fg))\cong\fg` is a proof gap. The same unsupported reduction already appears in the claimed `\widehat{\mathfrak{sl}}_2` base case at [1947](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:1947).

[CRITICAL] [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:64) — The official Theorem H synopsis is internally inconsistent. It states `P(t)=1+t^2` and also `\ChirHoch^1(V_k(\fg))\cong\fg` at generic level. Those cannot both hold for any simple `\fg`. The manuscript itself later says generic affine `\widehat{\mathfrak{sl}}_2` has total dimension `1+3+1=5`, not `4`, in [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2072), and the preface writes `P_{V_k(\fg)}(t)=1+(\dim\fg)t+t^2` in [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1240) and [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3454). So the concordance theorem surface is false as written.

[HIGH] [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:675) — The introduction repeats the same contradiction in one paragraph: amplitude `[0,2]` and “total dimension at most four” are stated, then affine generic `\ChirHoch^1(V_k(\fg))\cong\fg` is appended immediately after. The actual theorem-H proof only gives amplitude plus the polynomial formula `P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)t+\dim Z(\cA^!)t^2`; see [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:694). So `\dim(\fg)+2` is being used as a total vector-space dimension claim, not as the amplitude bound. The stale “at most four” bound also remains in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:2771).

[HIGH] [chapters/theory/chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2004) — The proposition’s stated scope and its proof’s hypothesis surface do not match. The statement defines “generic level” as only `k\neq-h^\vee`, but the proof appeals to “Kac--Shapovalov determinant is nonvanishing” and absence of singular vectors at [2051](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2051) without citing a theorem that gives exactly that scope. Elsewhere the manuscript uses stricter genericity: [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:3764) defines generic for `\widehat{\mathfrak{sl}}_2` as `k\notin\mathbb{Q}_{\le 0}`, and [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:205) defines W-algebra genericity as “away from admissible and critical levels.” The nearby Kac--Shapovalov criterion is also framed as the “genuine content” for simple quotients, not the universal affine algebra, at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1418). So the written proof does not justify the exact `k\neq-h^\vee` statement it claims.

[MEDIUM] [chapters/theory/chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:737) — The theorem-H package cites `Proposition~\ref{prop:bar-resolution-chirhoch}` as the bridge from the algebraic cochain complex to `\mathrm{RHom}_{\mathsf{ChirAlg}}(A,A)`, but repo-wide search found no such label definition. That leaves a named proof dependency missing from the Hochschild infrastructure.

The manuscript’s own split is not “all `k`”: it treats the affine claim as generic/non-critical, while critical level is handled separately and becomes unbounded; see [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:150) and [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:163). Search output found no exact duplicate of this affine claim in Volumes II or III.

## Summary
Instances checked: 16 | Violations found: 5 | Verdict: FAIL


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
session id: 019d8393-7d23-7731-9180-1836c299235f
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: FALSIFY the proof of ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?

Search the chapters/ directory for the theorem. Read the full statement AND proof.
For EACH step of the proof:
1. Does this step follow logically from previous steps?
2. Are all cited lemmas/propositions actually proved?
3. Is the scope correct (genus, level, type, family)?
4. Are there hidden assumptions?
5. Could a counterexample exist at boundary values?

Look for: circular reasoning, scope inflation, missing hypotheses, conflation of distinct objects, convention errors, status inflation.
mcp startup: no servers
codex
Using `deep-beilinson-audit` and `multi-path-verify` for this turn: first I’m locating the exact theorem surface in `chapters/`, then I’ll read the statement, proof, cited dependencies, and boundary-value surfaces before reporting only verified discrepancies.
collab spawn_agent(call_Wd2yApisje4IgOAQoemYJX1E, prompt="Locate the theorem/proof surface in /Users/raeez/chiral-bar-cobar concerning `ChirHoch^1(V_k(g)) = g` and `total dim = d…")
spawn_agent(call_Wd2yApisje4IgOAQoemYJX1E, prompt="Locate the theorem/proof surface in /Users/raeez/chiral-bar-cobar concerning `ChirHoch^1(V_k(g)) = g` and `total dim = d…") pending init:
  agent: 019d8393-b473-7780-b1dd-dc6851035a6f
mcp startup: no servers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1" -n chapters' in /Users/raeez/chiral-bar-cobar
 succeeded in 51ms:
chapters/examples/kac_moody.tex:5215: $\ChirHoch^1(\widehat{\fg}_{-h^\vee})$ also jumps: at generic level it equals~$\fg$
chapters/connections/concordance.tex:67: $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
chapters/connections/concordance.tex:387: $\ChirHoch^1(V_k(\fg)) \cong \fg$
chapters/connections/concordance.tex:2430: $\ChirHoch^1 = \mathbb{C}$ (outer derivation survives because
chapters/connections/concordance.tex:2432: $\ChirHoch^1 = 0$ (all derivations inner).
chapters/connections/concordance.tex:7085: & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
chapters/connections/concordance.tex:9652:& $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
chapters/frame/heisenberg_frame.tex:2000: \ChirHoch^1(\cH_k) = \bC\cdot D,
chapters/frame/heisenberg_frame.tex:4877:\item $\ChirHoch^1 = \mathbb{C}$: the outer derivation
chapters/frame/heisenberg_frame.tex:4897:$\ChirHoch^1$ = derivations (one outer), $\ChirHoch^2$ =
chapters/theory/en_koszul_duality.tex:3156:  $\ChirHoch^1$ to the $\fsl_2$ Lie bracket
chapters/theory/en_koszul_duality.tex:5638:$\ChirHoch^1(V_k(\fsl_2)) \cong \fsl_2$, see
chapters/theory/chiral_center_theorem.tex:1857: $\xi_k \in \ChirHoch^1$ \textup{(}the level deformation
chapters/theory/chiral_center_theorem.tex:1871: \ChirHoch^1 \cong \mathfrak{sl}_2, \qquad
chapters/theory/chiral_center_theorem.tex:1879: The three-dimensional $\ChirHoch^1$ consists of the outer derivations
chapters/theory/chiral_center_theorem.tex:1900: \ChirHoch^1 = 0, \qquad
chapters/theory/chiral_center_theorem.tex:1955:$\ChirHoch^1 \cong V = \mathfrak{sl}_2$ (outer derivations: the space of
chapters/theory/chiral_center_theorem.tex:1991:$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
chapters/theory/chiral_center_theorem.tex:2008:\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
chapters/theory/chiral_center_theorem.tex:2012:\dim \ChirHoch^1(V_k(\fg)) = \dim(\fg),
thinking
**Considering additional resources**

I’m thinking I might need a second explorer for exploring the theorem_registry and checking the concordance. It’s important to look at cross-volume mentions too, since those could offer valuable insights. I want to make sure I’m thorough in my exploration to provide the user with the best information possible. Let’s explore this together and ensure all relevant areas are covered!
codex
I’m separating location from verification: a second pass will check whether the theorem’s stated scope and status agree with concordance/registry and whether boundary cases are advertised elsewhere more broadly than the proof supports.
collab spawn_agent(call_MxPyww6LulBS9995LKf88Ypu, prompt="Audit metadata/status surface for the claim about `ChirHoch^1(V_k(g)) = g` and `total dim = dim(g)+2` in /Users/raeez/ch…")
spawn_agent(call_MxPyww6LulBS9995LKf88Ypu, prompt="Audit metadata/status surface for the claim about `ChirHoch^1(V_k(g)) = g` and `total dim = dim(g)+2` in /Users/raeez/ch…") pending init:
  agent: 019d8393-c5b0-7723-b611-2e80f19bd76e
mcp startup: no servers
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2000,2140p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
The deformation space of $V_k(\fg)$ \emph{is}~$\fg$.

\begin{proposition}[Generic affine first chiral Hochschild group; \ClaimStatusProvedHere]
\label{prop:chirhoch1-affine-km}
Let $\fg$ be a simple Lie algebra and let $V_k(\fg)$ be the affine
vertex algebra at generic level~$k$ \textup{(}$k \neq -h^\vee$\textup{)}.
Then
\[
\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
\]
as $\fg$-modules. In particular,
\[
\dim \ChirHoch^1(V_k(\fg)) = \dim(\fg),
\qquad
\dim \ChirHoch^1(V_k(\mathfrak{sl}_N)) = N^2 - 1.
\]
\end{proposition}

\begin{proof}
The affine vertex algebra $V_k(\fg)$ is generated by weight-$1$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\\(g\\)\\)\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
AGENTS.md:153:Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.
audit_campaign_20260412_231034/T07_thm_H.md:173:CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
scripts/adversarial_campaign.py:142:    ("T17_chirhoch1_KM", "ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?"),
compute/lib/chirhoch_sl_n_outer_derivations_engine.py:15:       affine rule ChirHoch^1(V_k(g)) = dim(g).
audit_campaign_20260412_230832/T17_chirhoch1_KM.md:52:MISSION: FALSIFY the proof of ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?
compute/lib/gerstenhaber_sl2_bracket_engine.py:61:   falsifying the claim that ChirHoch^1(V_k(g)) carries the adjoint
compute/lib/gerstenhaber_sl2_bracket_engine.py:332:    For derivations D_X, D_Y in ChirHoch^1(V_k(g)):
compute/lib/ds_chirhoch_compatibility_engine.py:11:  (A) prop:chirhoch1-affine-km: ChirHoch^1(V_k(g)) = g (generic k).
compute/tests/test_chirhoch_dimension_engine.py:350:    """ChirHoch^1(V_k(g)) = dim(g) at generic level."""
compute/audit/compute_chirhoch_complete_sweep.md:155:dim ChirHoch^1(V_k(g))     = 0
compute/tests/test_ds_chirhoch_compatibility_engine.py:7:  (A) ChirHoch^1(V_k(g)) = g  (prop:chirhoch1-affine-km)
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(\\fg\\) \\+ 2\" -n chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1"' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 426

CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
AGENTS.md:153:Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.
AGENTS.md:559:| ChirHoch^1 KM | PROVED | = g; total dim = dim(g)+2 |
scripts/adversarial_campaign.py:142:    ("T17_chirhoch1_KM", "ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?"),
audit_campaign_20260412_231034/T07_thm_H.md:7:- [HIGH] `chapters/connections/concordance.tex:64` — The concordance records Theorem H as universally having Hilbert polynomial `P(t)=1+t^2`, but the actual theorem states the family-dependent formula `P_\mathcal A(t)=\dim Z(\mathcal A)+\dim \ChirHoch^1(\mathcal A)\,t+\dim Z(\mathcal A^!)\,t^2` (`chapters/theory/chiral_hochschild_koszul.tex:701`). This already conflicts inside Vol I with the Heisenberg computation `1+t+t^2` (`chapters/theory/hochschild_cohomology.tex:390`) and the generic affine formula `1+\dim(\mathfrak g)t+t^2` (`chapters/theory/koszul_pair_structure.tex:705`).
audit_campaign_20260412_231034/T07_thm_H.md:173:CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
audit_campaign_20260412_231034/T07_thm_H.md:1368:The family scope is narrower than the concordance summary. I’m checking the affine KM `\ChirHoch^1` proposition now, because the main-table statement folds it into H even though critical level is already treated separately as non-Koszul.
audit_campaign_20260412_231034/T07_thm_H.md:1373:chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
audit_campaign_20260412_231034/T07_thm_H.md:1375:chapters/connections/concordance.tex:67: $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
audit_campaign_20260412_231034/T07_thm_H.md:1378:chapters/connections/concordance.tex:387: $\ChirHoch^1(V_k(\fg)) \cong \fg$
audit_campaign_20260412_231034/T07_thm_H.md:1381:chapters/connections/concordance.tex:7085: & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
audit_campaign_20260412_231034/T07_thm_H.md:1383:chapters/connections/concordance.tex:9652:& $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
audit_campaign_20260412_231034/T07_thm_H.md:1485:chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
audit_campaign_20260412_231034/T07_thm_H.md:1486:chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
audit_campaign_20260412_231034/T07_thm_H.md:1538:$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
audit_campaign_20260412_231034/T07_thm_H.md:1555:\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
audit_campaign_20260412_231034/T07_thm_H.md:1568:\phi \;\in\; \ChirHoch^1(V_k(\fg))
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "total dim" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/free_fields.tex:2384:counts the total dimension $\sum_i \dim \mathrm{Ext}^i$
chapters/examples/bar_complex_tables.tex:586:(cf.\ Computation~\ref{comp:heisenberg-deg3-full}), the total dimension is
chapters/examples/bar_complex_tables.tex:3407:The total dimension $\dim \B^n(\mathcal{F}_2)$ for the two-generator
chapters/examples/bar_complex_tables.tex:4106:The PBW formula is exact for the total dimension of the bar complex,
chapters/examples/genus_expansions.tex:1692:(Poincar\'e polynomial $1 + 3t^2 + 3t^4 + t^6$, total dimension~$8$)
chapters/frame/heisenberg_frame.tex:1994:$P(t) = 1 + t + t^2$, hence total dimension~$3$. The
chapters/frame/heisenberg_frame.tex:2004:total dimension~$3$. The degree-$0$ class is the vacuum; the
chapters/theory/higher_genus_modular_koszul.tex:32258:The total dimension is $6 \cdot 3 = 18$.
chapters/connections/thqg_symplectic_polarization.tex:680:$g \ge 1$, the total dimension
chapters/theory/en_koszul_duality.tex:2772: degrees $\{0, 1, 2\}$ with total dimension at most four on
chapters/theory/en_koszul_duality.tex:3675:with total dimension $1 + 3 + 1 = 5$. Write $\mathbf{1}$
chapters/theory/bar_cobar_adjunction_inversion.tex:4119:$\dim E_1^{0,p}$ bounded by the total dimension at
chapters/theory/e1_modular_koszul.tex:967:degrees $\{0,1,2\}$ with total dimension~$3$).
chapters/theory/e1_modular_koszul.tex:1276:contributes the Arnold algebra of total dimension~$n!$.
chapters/theory/higher_genus_foundations.tex:2768:The universal family over $\overline{\mathcal{M}}_g$ with fiber $\overline{C}_n(\Sigma_g)$ has total dimension $(3g-3) + n$, which equals $\dim \overline{\mathcal{M}}_{g,n}$. Indeed, $\overline{\mathcal{M}}_{g,n}$ can be identified with this universal configuration space.
chapters/theory/configuration_spaces.tex:1641:The total dimension is
chapters/theory/chiral_center_theorem.tex:51:$\{0, 2\}$, with total dimension~$2$ and Hilbert series
chapters/theory/chiral_center_theorem.tex:1875: Thus the total dimension is~$5$. In particular, the older
chapters/theory/chiral_center_theorem.tex:1912: which is bounded in degrees $\{0, 2\}$ with total dimension~$2$.
chapters/theory/chiral_center_theorem.tex:1976:$P(t) = 1 + t^2$, giving total dimension~$2$:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(g\\)\\+2\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
AGENTS.md:153:Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.
AGENTS.md:559:| ChirHoch^1 KM | PROVED | = g; total dim = dim(g)+2 |
audit_campaign_20260412_231034/T07_thm_H.md:173:CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
audit_campaign_20260412_230832/T17_chirhoch1_KM.md:52:MISSION: FALSIFY the proof of ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?
scripts/adversarial_campaign.py:142:    ("T17_chirhoch1_KM", "ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?"),
compute/lib/chirhoch_dimension_engine.py:296:        total=dim_g + 2,  # VERIFIED: [DC] 1 + dim(g) + 1 = dim(g)+2; [CF] sl_2 -> 5 and sl_3 -> 10.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2140,2280p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(D_X \circ D_Y)(J^c)
\;=\;
\sum_{a,b} X^a\,Y^b\,f^{ab}_{\ c}\,|0\rangle
\;=\;
[X, Y]^c\,|0\rangle.
\]
The double-pole term $k\,\kappa^{ab}\,\lambda$ does not
contribute at $\lambda^0$; the bracket is therefore
independent of the level~$k$.

For degree-$1$ cochains, the shifted degrees
$|D_X| - 1 = 0$ and $|D_Y| - 1 = 0$ are both even, so the
Gerstenhaber bracket reduces to:
\[
[D_X, D_Y]
\;=\;
D_X \circ D_Y \;-\; D_Y \circ D_X
\;=\;
D_{[X,Y]_{\fg}} - D_{[Y,X]_{\fg}}
\;=\;
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:chirhoch1-affine-km" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
metadata/dependency_graph.dot:2321:  prop_chirhoch1_affine_km [label="prop:chirhoch1-affine-km\nproposition [Pr]\nGeneric affine first chiral Hochschild g...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:337:| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
metadata/label_index.json:24738:  "prop:chirhoch1-affine-km": {
metadata/claims.jsonl:2224:{"label": "prop:chirhoch1-affine-km", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 1924, "title": "Generic affine first chiral Hochschild group"}
compute/lib/ds_chirhoch_compatibility_engine.py:11:  (A) prop:chirhoch1-affine-km: ChirHoch^1(V_k(g)) = g (generic k).
compute/lib/ds_chirhoch_compatibility_engine.py:112:    prop:chirhoch1-affine-km (chiral_center_theorem.tex)
audit_campaign_20260412_231034/T07_thm_H.md:173:CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
audit_campaign_20260412_231034/T07_thm_H.md:272:/bin/zsh -lc "rg -n \"Theorem H|thm:virasoro-hochschild|thm:w-algebra-hochschild|prop:chirhoch1-affine-km|thm:critical-level-cohomology|ClaimStatus.*H|Hilbert polynomial|Hilbert series|concentrated in .*\\{0, ?1, ?2\\}|amplitude|vdim\" chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/koszul_pair_structure.tex chapters examples metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/T07_thm_H.md:458: Proposition~\ref{prop:chirhoch1-affine-km}).}
audit_campaign_20260412_231034/T07_thm_H.md:1372:/bin/zsh -lc "rg -n \"prop:chirhoch1-affine-km|Generic affine first chiral Hochschild group|ChirHoch\\"'^1'"\\(V_k\" chapters/theory/chiral_hochschild_koszul.tex metadata/theorem_registry.md chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
audit_campaign_20260412_231034/T07_thm_H.md:1373:chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
audit_campaign_20260412_231034/T07_thm_H.md:1374:metadata/theorem_registry.md:337:| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
audit_campaign_20260412_231034/T07_thm_H.md:1376:chapters/connections/concordance.tex:71: Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
audit_campaign_20260412_231034/T07_thm_H.md:1377:chapters/connections/concordance.tex:377: Proposition~\ref{prop:chirhoch1-affine-km}).}
audit_campaign_20260412_231034/T07_thm_H.md:1379:chapters/connections/concordance.tex:388: (Proposition~\ref{prop:chirhoch1-affine-km}).
audit_campaign_20260412_231034/T07_thm_H.md:1380:chapters/connections/concordance.tex:7084:\ref{prop:chirhoch1-affine-km}
audit_campaign_20260412_231034/T07_thm_H.md:1382:chapters/connections/concordance.tex:7086: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)}
audit_campaign_20260412_231034/T07_thm_H.md:1384:chapters/connections/concordance.tex:9653: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)} \\
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(\\\\fg\\) \\+ 2\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

codex
Plan:
1. Read the audit workflow and the repository’s live status surfaces relevant to this claim: `deep-beilinson-audit`, `multi-path-verify`, `CLAUDE.md`, `chapters/connections/concordance.tex`, and `metadata/theorem_registry.md`.
2. Read the exact theorem statement and proof in `chapters/`, then trace every cited dependency in proof order.
3. Pressure-test the claim against scope boundaries: level `k`, critical/non-critical behavior, whether `dim(g)+2` refers to total vector-space dimension or cohomological amplitude, and whether the proof actually establishes what the prose claims.
4. Check for downstream inflation or contradictory formulations in Vol I metadata and any genuine duplicates in Vol II/III.
5. Re-verify each candidate finding against the source lines and keep only real violations.
exec
/bin/zsh -lc "sed -n '1,240p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

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


thinking
**Gathering claim references and line numbers**

I’m collecting line numbers and snippets related to the claim `ChirHoch^1(V_k(g)) = g` and the dimension formula from various metadata and chapter files, like theorem_registry.md, claims.jsonl, and chiral_center_theorem.tex, especially lines around 1980–2060, to check how the claim is documented and cross-referenced.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(\\\\fg\\)\\+2\" -n chapters" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1980,2065p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 51ms:
the deformation $c \mapsto c + \epsilon$.
The weight grading: $\Theta$ sits at conformal weight~$0$
because the deformation $c \mapsto c + \epsilon$ does not shift
conformal weights. The Virasoro Jacobi identity
(associativity of the OPE) forces all higher-weight deformations
within $\ChirHoch^2$ to vanish: there is no independent weight-$4$
deformation, no weight-$6$ deformation, etc.
\end{proof}

The $\mathfrak{sl}_2$ computation in Part~(ii) already exhibits the
essential phenomenon: the first chiral Hochschild group
$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
This is not a coincidence special to rank one. For any simple Lie
algebra, the affine vertex algebra $V_k(\fg)$ at generic level is
chirally Koszul with generating space $V = \fg$; the Koszul resolution
is a three-term complex whose degree-$1$ piece is $\fg$ itself.
Degree-$1$ Hochschild cochains are infinitesimal deformations of the
current algebra: maps $J^a \mapsto J^a + \epsilon\,\phi^a$ preserving
the OPE to first order. The space of such deformations is determined
by the generating space alone, and the generating space is~$\fg$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"total dimension.*dim\\\\\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:total dimension.*dim\)
    ^
error: unclosed group
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(\\fg\\)\\+2\" -n" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"total dimension.*dim\\\\(\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Locating theorem statements**

I need to check the red_team_summary first, as that's what skill says to do. I might only focus on the relevant sections, not the whole thing. If using the explorer takes too long, I can also locate the theorem statement manually. The developer mentions trusting the explorer, but since it hasn't returned anything yet, it seems reasonable to do a manual search. I could also use exec_command rg to get the theorem quickly. Let's hold off for a bit, though, and see if the explorer finishes soon.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(g\\)\\+2\" chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "total dim" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
AGENTS.md:153:Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.
AGENTS.md:559:| ChirHoch^1 KM | PROVED | = g; total dim = dim(g)+2 |
scripts/adversarial_campaign.py:142:    ("T17_chirhoch1_KM", "ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?"),
audit_campaign_20260412_230832/T17_chirhoch1_KM.md:52:MISSION: FALSIFY the proof of ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?
audit_campaign_20260412_231034/T07_thm_H.md:173:CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
audit_campaign_20260412_231034/T07_thm_H.md:2158:/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_drinfeld_double_wave11.md:34:At hochschild.tex:294-302, comp:tamarkin-e2-heisenberg computes `V_T = C^*(H_k, H_k) ≅ k[[κ]]` as a formal power series ring: INFINITE-dimensional as a graded vector space. At hochschild.tex:1691-1695, Part (c) invokes this exact computation then writes "truncated to the amplitude bound of Theorem H, the surviving piece is k<1,κ> with total dimension two." But Vol I Theorem H is a **theorem**, not a filter: it says `total_dim(ChirHoch*(A)) ≤ 4`, so if comp:tamarkin-e2-heisenberg is correct it already contradicts Theorem H, and the Drinfeld-center-equals-bulk base case (comp:drinfeld-center-heisenberg at 1685-1697) depends on this "truncation" to reach `Z(U_{H_k}) ≅ k<1, κ>` with dim 2. CLAUDE.md AP94-AP98 and the audit notes at compute/audit/complete_frontier_status_2026_04_08.md:290 already flag this exact inconsistency as a known issue ("polynomial" was corrected to "polynomial growth of Betti numbers, not a polynomial algebra"), but comp:tamarkin-e2-heisenberg was not updated in the sweep. Part (c) inherits the stale computation and papers over the contradiction by calling Theorem H a "truncation." Either comp:tamarkin-e2-heisenberg is wrong (it should be a finite complex of total dim ≤ 4), or Theorem H does not apply to H_k (class G), or the two objects are different. All three resolutions demand explicit statement; the current text contains a logical cycle.
audit_campaign_20260412_231034/T07_thm_H.md:2160:/Users/raeez/chiral-bar-cobar-vol2/compute/audit/beilinson_audit_drinfeld_double_wave11.md:221:1. **F-CRIT-1:** `comp:tamarkin-e2-heisenberg` says `V_T ≅ k[[κ]]` (infinite-dim) but Theorem H says total dim ≤ 4. Part (c) "truncates" to dim 2; Theorem H is not a truncation but a theorem. Internal Vol II contradiction that the Drinfeld-center-equals-bulk Heisenberg base case depends on.
audit_campaign_20260412_231034/T07_thm_H.md:2337: which is bounded in degrees $\{0, 2\}$ with total dimension~$2$.
audit_campaign_20260412_231034/T14_topologization.md:561:on the total dimension. The dimension of $\ChirHoch^1$ grows with
audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
audit_campaign_20260412_231034/T09_MC2_theta.md:938:Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
audit_campaign_20260412_231034/T09_MC2_theta.md:1676:   365	Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
compute/lib/cy_nc_deformation_k3e_engine.py:352:        dim_hh2: total dim HH^2 (first-order deformations of D^b(X))
chapters/examples/genus_expansions.tex:1692:(Poincar\'e polynomial $1 + 3t^2 + 3t^4 + t^6$, total dimension~$8$)
chapters/examples/free_fields.tex:2384:counts the total dimension $\sum_i \dim \mathrm{Ext}^i$
compute/lib/ds_chirhoch_compatibility_engine.py:373:    The total dimension drops by 3 = dim(sl_2), accounted for entirely
chapters/examples/bar_complex_tables.tex:586:(cf.\ Computation~\ref{comp:heisenberg-deg3-full}), the total dimension is
chapters/examples/bar_complex_tables.tex:3407:The total dimension $\dim \B^n(\mathcal{F}_2)$ for the two-generator
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "Theorem~H" -n chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1832:These computations verify the general structure of Theorem~H
2080:The correct uniform statement is Theorem~H: concentration in
codex
The live status surface already narrows one point: the concordance states `\ChirHoch^1(V_k(\fg))\cong\fg` only “at generic level,” not “for all k,” so the audit now turns on whether the chapter proof respects that narrower scope or silently inflates it.
exec
/bin/zsh -lc "sed -n '1,240p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:chirhoch1-affine-km|thm:critical-level-cohomology|thm:w-algebra-hochschild|thm:virasoro-hochschild" chapters metadata chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"ChirHoch\\"'^1|dim'"\\(g\\)\\+2|dim\\(\\\\fg\\)\\+2|total dim|generic level|critical level|affine-km\" chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
chapters/connections/concordance.tex:68: \textup{(}Thms~\ref{thm:w-algebra-hochschild},
chapters/connections/concordance.tex:69: \ref{thm:virasoro-hochschild},
chapters/connections/concordance.tex:70: \ref{thm:critical-level-cohomology};
chapters/connections/concordance.tex:71: Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
chapters/connections/concordance.tex:374: (Theorems~\ref{thm:w-algebra-hochschild},
chapters/connections/concordance.tex:375: \ref{thm:virasoro-hochschild},
chapters/connections/concordance.tex:376: \ref{thm:critical-level-cohomology};
chapters/connections/concordance.tex:377: Proposition~\ref{prop:chirhoch1-affine-km}).}
chapters/connections/concordance.tex:388: (Proposition~\ref{prop:chirhoch1-affine-km}).
chapters/connections/concordance.tex:3013:\item \emph{Critical level}: $V_{-h^\vee}(\fg)$ is uncurved ($\kappa=0$), self-dual under the Feigin--Frenkel involution ($k=-h^\vee$ is a fixed point of $k \mapsto -k-2h^\vee$), center~$= \mathfrak{z}(\widehat{\fg})$ (Theorem~\ref{thm:critical-level-cohomology}).
chapters/connections/concordance.tex:4565:(Theorem~\ref{thm:w-algebra-hochschild}) via dimensional
chapters/connections/concordance.tex:4716:$H$ & Chiral Hochschild: $\ChirHoch^n = 0$ for $n > 2$, $P(t) = 1+t^2$; & \textbf{Proved} (generic level, & Thms~\ref{thm:w-algebra-hochschild}, \\
chapters/connections/concordance.tex:4717: & concentration in $\{0,1,2\}$ (de~Rham bound on curve); & critical level: ProvedElsewhere) & \ref{thm:virasoro-hochschild}, \ref{thm:critical-level-cohomology}; \\
chapters/connections/concordance.tex:7084:\ref{prop:chirhoch1-affine-km}
chapters/connections/concordance.tex:7086: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)}
chapters/connections/concordance.tex:7962:Theorem~\ref{thm:critical-level-cohomology} belong to
chapters/connections/concordance.tex:9653: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)} \\
metadata/dependency_graph.dot:2321:  prop_chirhoch1_affine_km [label="prop:chirhoch1-affine-km\nproposition [Pr]\nGeneric affine first chiral Hochschild g...", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3208:  thm_virasoro_hochschild [label="thm:virasoro-hochschild\ntheorem [Pr]\nVirasoro Hochschild cohomology", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:3209:  thm_critical_level_cohomology [label="thm:critical-level-cohomology\ntheorem [Pr]\nCritical level Lie algebra cohomology", style=filled, fillcolor="#bbdefb"];
 succeeded in 51ms:
Total output lines: 805

chapters/examples/deformation_quantization.tex:1156:(Proposition~\ref{prop:km-bar-curvature}) measures the failure of the star product to extend to $E_\tau$. At critical level $k = -h^\vee$, $m_0 = 0$ and the extension is unobstructed. At generic level, the genus-1 correction involves $E_2(\tau)$ (Theorem~\ref{thm:elliptic-vs-rational}).
chapters/examples/w_algebras_deep.tex:118:At critical level $k = -h^\vee$, the W-algebra admits a resolution:
chapters/examples/w_algebras_deep.tex:163:\item At non-critical level, the comultiplication acquires quantum corrections:
chapters/examples/w_algebras_deep.tex:178:\emph{(2) Intersection pairing.} At critical level $k = -h^\vee$, chains on maps into $G/P_e$ are classified by the bar complex (Theorem~\ref{thm:w-cdr}). The coalgebra structure is Poincar\'e dual to the intersection product on $H^*(G/P_e)$: for $\alpha, \beta \in H^*(G/P_e)$, $\langle \alpha, \beta \rangle = \int_{G/P_e} \alpha \wedge \beta$.
chapters/examples/w_algebras_deep.tex:997:at generic level~$k$.
chapters/examples/w_algebras_deep.tex:1144:at generic level~$k$:
chapters/examples/w_algebras_deep.tex:1225:$\Einf$-Koszulness of each $W_N$ at generic level~$k$ is
chapters/examples/w_algebras_deep.tex:1427:$f = f_{\mathrm{prin}}$ and non-critical level $k \neq -h^\vee$,
chapters/examples/w_algebras_deep.tex:1938:\item $k = -3$ (critical level): the Sugawara construction is
chapters/examples/w_algebras_deep.tex:1940:$\mathcal{W}_3$ algebra at critical level is
chapters/examples/w_algebras_deep.tex:1958:to the affine Kac--Moody case where $m_0 = 0$ at the critical level
chapters/examples/w_algebras_deep.tex:2058: $\mathfrak{sl}_n$ at generic level admits a proved transport
chapters/examples/w_algebras_deep.tex:2072:For every nilpotent $f \in \fg$ at generic level, the natural
chapters/examples/w_algebras_deep.tex:2137: both r-matrices vanish; at $k = -h^\vee$ (critical level) the
chapters/examples/w_algebras_deep.tex:2178:Then at generic level $k \notin \mathbb{Q}_{<0}$:
chapters/examples/w_algebras_deep.tex:2575: $\mathfrak{sl}_n$ at generic level.
chapters/examples/w_algebras_deep.tex:2810:$f = f_{\mathrm{prin}}$ and non-critical level
chapters/examples/w_algebras_deep.tex:2984:$N = 2,\ldots,6$ at generic level~$k$. Write
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1760,1855p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
cochains are determined by their evaluations.

The additional feature in the chiral setting is the
\emph{spectral variables} $\lambda_1, \ldots, \lambda_{n-1}$,
which replace the real parameters of configuration-space
integrals. The block-substitution
rule~\eqref{eq:spectral-substitution} is the algebraic
encoding of the nested-collision geometry on
$\FM_n(\mathbb{C})$.
\end{remark}

\begin{remark}[Bridge to the global open/closed theory]
\label{rem:chiral-center-global-bridge}
\index{chiral center theorem!global bridge}
The chiral center theorem
(Theorem~\ref{thm:chiral-deligne-tamarkin}) governs the
\emph{local} theory: a single open disc with a single closed
disc. The \emph{global} theory on a tangential log curve
$(X, D, \tau)$ is developed in two directions:
\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
67: $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
387: $\ChirHoch^1(V_k(\fg)) \cong \fg$
7085: & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
9652:& $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1850,1990p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \bC & n = 1, \\
 \bC & n = 2, \\
 0 & n \geq 3.
 \end{cases}
 \]
 The generators are:
 $1 \in \ChirHoch^0$ \textup{(}the vacuum, center of~$\mathfrak{H}_k$\textup{)},
 $\xi_k \in \ChirHoch^1$ \textup{(}the level deformation
 $k \mapsto k + \epsilon$\textup{)}, and
 $\eta \in \ChirHoch^2$ \textup{(}the dual vacuum, the obstruction
 class of the Koszul dual
 $\mathfrak{H}_k^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$\textup{)}.
 All cohomology is concentrated at conformal weight~$0$.
 The total derived center is
 $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)
 \cong \bC \oplus \bC[-1] \oplus \bC[-2]$.

\item \textup{(Affine $\widehat{\mathfrak{sl}}_2$ at level~$k \neq -2$.)}
 At generic \textup{(}non-critical\textup{)} level:
 \[
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '40,110p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 genus~$0$ unconditional; for arbitrary~$\cA$,
 $g \geq 1$ is conditional on
 axiom~\ref{MK:modular}; unconditional on the
 CFT-type standard landscape except integer-spin
 $\beta\gamma$ by Theorem~\ref{thm:pbw-propagation}
 and Remark~\ref{rem:pbw-propagation-scope}
 & \ClaimStatusProvedHere \\
\textbf{C} & Complementarity
 & $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\mathcal{M}}_g, Z(\cA))$
 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)};
 Verdier-side Lagrangian splitting unconditional;
 ambient shifted-symplectic upgrade conditional on
 perfectness/nondegeneracy
 & \ClaimStatusProvedHere \\
\textbf{D} & Modular characteristic
 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
 for uniform-weight modular Koszul algebras
 \textup{(}Definition~\ref{def:scalar-lane}\textup{)}
 at all genera;
 genus~$1$ universal for all families;
thinking
**Targeting specific readings**

I’ve noticed that the rg output is quite extensive, so I should focus on targeted reads. I need to check the theorem or proof in the chapters related to `chiral_center_theorem.tex`, which has around 1924 lines and relevant dependencies. I should also consider looking at the introduction for insights on downstream propagation. It's essential to fully review the statement and proof, along with any definitions or lemmas in the same or related files. I’ll wait for exploration results before proceeding.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(g\\) \\+ 2\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '320,360p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
| `lem:residue-properties` | `lemma` | 1753 | Residue properties |
| `thm:three-bar-complexes` | `theorem` | 1825 | Three bar complexes and their inclusions |
| `thm:geometric-equals-operadic-bar` | `theorem` | 2035 | Geometric bar \texorpdfstring{$=$}{=} operadic bar |
| `thm:residue-formula` | `theorem` | 2110 | Residue formula |
| `thm:bar-uniqueness-functoriality` | `theorem` | 2182 | Uniqueness and functoriality |
| `thm:bar-chiral` | `theorem` | 2291 | Bar complex is chiral |

#### `chapters/theory/chiral_center_theorem.tex` (9)

| Label | Env | Line | Title |
|---|---|---:|---|
| `lem:partial-comp-assoc` | `lemma` | 194 | Associativity of partial compositions |
| `prop:pre-lie-chiral` | `proposition` | 499 | Pre-Lie relation for the single brace |
| `prop:full-brace-chiral` | `proposition` | 527 | Full brace identity |
| `thm:brace-dg-algebra` | `theorem` | 548 | Brace dg algebra |
| `thm:chiral-deligne-tamarkin` | `theorem` | 1232 | Chiral Deligne--Tamarkin |
| `prop:derived-center-explicit` | `proposition` | 1772 | Explicit derived center: Heisenberg, affine $\widehat{\mathfrak{sl}}_2$, Virasoro |
| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
| `prop:heisenberg-bv-structure` | `proposition` | 1957 | BV algebra structure on $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)$ |
| `prop:annulus-trace-standard` | `proposition` | 2055 | Annulus trace for standard families |
codex
The claim surface is now fixed: the actual proposition is `chapters/theory/chiral_center_theorem.tex` around `prop:chirhoch1-affine-km`, while the concordance and introduction already advertise it as a generic/non-critical statement. Next I’m checking whether the proof itself really earns that scope and whether “`dim(g)+2`” is being claimed as a total vector-space dimension rather than the cohomological amplitude bound.
exec
/bin/zsh -lc "sed -n '4720,4795p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,380p' chapters/theory/hochschild_cohomology.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1860,2145p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '640,720p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Therefore:
\[\ChirHoch^1(\mathcal{B}) = \text{Der}/\text{Inn} = \mathbb{C}/0 = \mathbb{C},\]
generated by the outer chiral derivation $D(\alpha) = \mathbf{1}$.

\begin{remark}[Classical vs.\ chiral Hochschild]
The classical Hochschild $\mathrm{HH}^1$ of the Weyl algebra (the mode algebra of~$\mathcal{B}$) is $0$ by Whitehead's theorem: every derivation of the Weyl algebra is inner. The discrepancy with $\ChirHoch^1(\mathcal{B}) = \mathbb{C}$ arises because the chiral inner derivations use the \emph{vertex algebra} zero mode $a_{(0)}$, not the \emph{associative algebra} commutator $[a, -]$. The zero mode $\alpha_{(0)}$ is central in the Heisenberg vertex algebra (it acts by the residue of the OPE, which has no first-order pole), while the mode $\alpha_{-1}$ is non-central in the Weyl algebra but does \emph{not} define a chiral inner derivation.
\end{remark}

\subsubsection{\texorpdfstring{Degree 2: $\ChirHoch^2(\mathcal{B})$}{Degree 2: HH 2(B)}}

$\ChirHoch^2$ classifies deformations of the chiral algebra structure.

A deformation is given by modifying the OPE:
\[\alpha(z_1) \times_t \alpha(z_2) = \alpha(z_1)\alpha(z_2) + t \cdot \phi(z_1, z_2) + O(t^2)\]

where $\phi$ is a 2-cocycle.

\emph{Cocycle condition.} Associativity to first order in $t$:
\[(\alpha \times_t \alpha) \times_t \alpha = \alpha \times_t (\alpha \times_t \alpha)\]

 succeeded in 51ms:
\chapter{Chiral Hochschild cohomology and deformation theory}

\index{Hochschild cohomology!classical}
\index{cyclic homology!chiral}

The chiral Hochschild cohomology $\ChirHoch^*(\cA)$ is the
tangent complex to the MC moduli at~$\Theta_\cA$: the cohomology
of the convolution $L_\infty$-algebra controlling deformations,
obstructions, and bulk-field couplings.

The chiral Hochschild complex carries a degree $-1$ Lie bracket
(the chiral Gerstenhaber bracket, Theorem~\ref{thm:gerstenhaber-structure}),
computed by OPE residues on FM configuration spaces.
In the classical limit (fiber at a point), it recovers
Gerstenhaber's bracket~\cite{Ger63} on associative Hochschild
cochains. The chiral bracket is the strict shadow of a full
$L_\infty$ bracket on the chiral Hochschild complex. In the strict model, $\mathrm{HH}^2$ classifies
first-order deformations and $\mathrm{HH}^3$ contains obstructions;
the $L_\infty$ extension records coherent homotopies governing
convergence of formal deformations and transfer of Koszul properties
 succeeded in 50ms:
 $\hat{A}$-genus
 \textup{(}Theorem~\textup{\ref{thm:universal-generating-function}}\textup{)}:
 \begin{equation}\label{eq:ahat-genus-generating-function-intro}
 \sum_{g \geq 1} F_g(\cA) \cdot \hbar^{2g}
 = \kappa(\cA) \cdot \bigl(\hat{A}(i\hbar) - 1\bigr).
 \end{equation}
 At genus~$1$ this reduces to $F_1(\cA) = \kappa(\cA)/24$ for every
 family.

 \emph{Theorem~D$_\Delta$} (Spectral characteristic,
 Theorem~\ref{thm:spectral-characteristic}):
 the spectral discriminant $\Delta_\cA(x)$ is a separately proved
 non-scalar invariant.

 $\kappa$ is the one-loop coefficient of the effective action;
 its vanishing removes the scalar genus-$1$ anomaly, while
 higher-genus multi-weight corrections are a separate issue.
 Together, $D_{\mathrm{scal}}$ and $D_\Delta$ are the
 characteristic classes of the factorization homology
 bundle $\int_{\Sigma_g}\!\cA$
 succeeded in 50ms:
 class of the Koszul dual
 $\mathfrak{H}_k^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$\textup{)}.
 All cohomology is concentrated at conformal weight~$0$.
 The total derived center is
 $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)
 \cong \bC \oplus \bC[-1] \oplus \bC[-2]$.

\item \textup{(Affine $\widehat{\mathfrak{sl}}_2$ at level~$k \neq -2$.)}
 At generic \textup{(}non-critical\textup{)} level:
 \[
 \ChirHoch^0 = \bC, \qquad
 \ChirHoch^1 \cong \mathfrak{sl}_2, \qquad
 \ChirHoch^2 = \bC, \qquad
 \ChirHoch^n = 0 \text{ for } n \geq 3.
 \]
 Thus the total dimension is~$5$. In particular, the older
 conjectural total bound~$4$ does not hold for affine
 $\widehat{\mathfrak{sl}}_2$; the uniform statement is the
 concentration in degrees $\{0,1,2\}$.
 The three-dimensional $\ChirHoch^1$ consists of the outer derivations
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "total dimension.*ChirHoch" -n chapters' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_center_theorem.tex:2082:on the total dimension. The dimension of $\ChirHoch^1$ grows with
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2210,2245p' metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
{"label": "thm:diff-is-coderivation", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 1634, "title": "Differential is coderivation", "refs_in_block": ["conv:regime-tags", "chap:higher-genus"]}
{"label": "lem:orientation", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 1727, "title": "Orientation convention"}
{"label": "lem:residue-properties", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 1753, "title": "Residue properties"}
{"label": "thm:three-bar-complexes", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 1825, "title": "Three bar complexes and their inclusions", "labels_in_block": ["thm:three-bar-complexes", "eq:three-bar-inclusions", "eq:eulerian-bar-decomposition"], "refs_in_block": ["eq:three-bar-inclusions", "subsec:e1-as-primitive"]}
{"label": "thm:geometric-equals-operadic-bar", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 2035, "title": "Geometric bar \\texorpdfstring{$=$}{=} operadic bar", "refs_in_block": ["def:geometric-bar"], "cites_in_block": ["LV12"]}
{"label": "thm:residue-formula", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 2110, "title": "Residue formula", "refs_in_block": ["prop:pole-decomposition", "conv:product-vs-bracket", "rem:bicomplex-obstruction"], "cites_in_block": ["BD04"]}
{"label": "thm:bar-uniqueness-functoriality", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 2182, "title": "Uniqueness and functoriality"}
{"label": "thm:bar-chiral", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/bar_construction.tex", "line": 2291, "title": "Bar complex is chiral", "refs_in_block": ["thm:three-bar-complexes"]}
{"label": "lem:partial-comp-assoc", "env_type": "lemma", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 194, "title": "Associativity of partial compositions"}
{"label": "prop:pre-lie-chiral", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 499, "title": "Pre-Lie relation for the single brace"}
{"label": "prop:full-brace-chiral", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 527, "title": "Full brace identity", "refs_in_block": ["thm:brace-dg-algebra"]}
{"label": "thm:brace-dg-algebra", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 548, "title": "Brace dg algebra", "labels_in_block": ["thm:brace-dg-algebra", "eq:brace-identity", "eq:brace-identity-precise", "eq:brace-identity-sign", "eq:delta-brace"], "refs_in_block": ["eq:brace-sign-explicit"]}
{"label": "thm:chiral-deligne-tamarkin", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 1232, "title": "Chiral Deligne--Tamarkin", "refs_in_block": ["const:universal-pair", "rem:phi-koszul-sign"]}
{"label": "prop:derived-center-explicit", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 1772, "title": "Explicit derived center: Heisenberg, affine $\\widehat{\\mathfrak{sl}}_2$,\nVirasoro", "refs_in_block": ["thm:hochschild-polynomial-growth", "def:chiral-hochschild-cochain-brace"]}
{"label": "prop:chirhoch1-affine-km", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 1924, "title": "Generic affine first chiral Hochschild group"}
{"label": "prop:heisenberg-bv-structure", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 1957, "title": "BV algebra structure on $Z^{\\mathrm{der}}_{\\mathrm{ch}}(\\mathfrak{H}_k)$", "cites_in_block": ["Getzler94"]}
{"label": "prop:annulus-trace-standard", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 2055, "title": "Annulus trace for standard families", "refs_in_block": ["thm:thqg-annulus-trace", "def:complementarity-asymmetry"]}
{"label": "thm:chiral-hochschild-differential", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 173, "title": "The chiral Hochschild differential"}
{"label": "thm:hochschild-bar-cobar", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 324, "title": "Hochschild via bar-cobar", "refs_in_block": ["conv:regime-tags", "def:chiral-koszul-pair"]}
{"label": "thm:hochschild-spectral-sequence", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/theory/chiral_hochschild_koszul.tex", "line": 362, "title": "Hochschild spectral sequence"}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(g\\)\\+2\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
AGENTS.md:153:Delta = 8*kappa*S_4. Delta=0 ↔ finite tower. SC formality: A is SC-formal iff class G. Depth gap: d_alg in {0,1,2,inf}; gap at 3. ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2.
AGENTS.md:559:| ChirHoch^1 KM | PROVED | = g; total dim = dim(g)+2 |
audit_campaign_20260412_231034/T07_thm_H.md:173:CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
audit_campaign_20260412_231034/T09_MC2_theta.md:154:CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
audit_campaign_20260412_230832/T17_chirhoch1_KM.md:52:MISSION: FALSIFY the proof of ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?
scripts/adversarial_campaign.py:142:    ("T17_chirhoch1_KM", "ChirHoch^1(V_k(g)) = g with total dim dim(g)+2. Check: (a) is this for all k? non-critical? (b) why dim(g)+2? (c) is this amplitude or dimension?"),
compute/lib/chirhoch_dimension_engine.py:296:        total=dim_g + 2,  # VERIFIED: [DC] 1 + dim(g) + 1 = dim(g)+2; [CF] sl_2 -> 5 and sl_3 -> 10.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1860,1945p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 class of the Koszul dual
 $\mathfrak{H}_k^! = \operatorname{Sym}^{\mathrm{ch}}(V^*)$\textup{)}.
 All cohomology is concentrated at conformal weight~$0$.
 The total derived center is
 $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k)
 \cong \bC \oplus \bC[-1] \oplus \bC[-2]$.

\item \textup{(Affine $\widehat{\mathfrak{sl}}_2$ at level~$k \neq -2$.)}
 At generic \textup{(}non-critical\textup{)} level:
 \[
 \ChirHoch^0 = \bC, \qquad
 \ChirHoch^1 \cong \mathfrak{sl}_2, \qquad
 \ChirHoch^2 = \bC, \qquad
 \ChirHoch^n = 0 \text{ for } n \geq 3.
 \]
 Thus the total dimension is~$5$. In particular, the older
 conjectural total bound~$4$ does not hold for affine
 $\widehat{\mathfrak{sl}}_2$; the uniform statement is the
 concentration in degrees $\{0,1,2\}$.
 The three-dimensional $\ChirHoch^1$ consists of the outer derivations
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1990,2055p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1990	essential phenomenon: the first chiral Hochschild group
  1991	$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
  1992	This is not a coincidence special to rank one. For any simple Lie
  1993	algebra, the affine vertex algebra $V_k(\fg)$ at generic level is
  1994	chirally Koszul with generating space $V = \fg$; the Koszul resolution
  1995	is a three-term complex whose degree-$1$ piece is $\fg$ itself.
  1996	Degree-$1$ Hochschild cochains are infinitesimal deformations of the
  1997	current algebra: maps $J^a \mapsto J^a + \epsilon\,\phi^a$ preserving
  1998	the OPE to first order. The space of such deformations is determined
  1999	by the generating space alone, and the generating space is~$\fg$.
  2000	The deformation space of $V_k(\fg)$ \emph{is}~$\fg$.
  2001	
  2002	\begin{proposition}[Generic affine first chiral Hochschild group; \ClaimStatusProvedHere]
  2003	\label{prop:chirhoch1-affine-km}
  2004	Let $\fg$ be a simple Lie algebra and let $V_k(\fg)$ be the affine
  2005	vertex algebra at generic level~$k$ \textup{(}$k \neq -h^\vee$\textup{)}.
  2006	Then
  2007	\[
  2008	\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
  2009	\]
collab wait(call_byTmgfZsfefMlmuPJNL8OLcH)
  receivers: 019d8393-b473-7780-b1dd-dc6851035a6f, 019d8393-c5b0-7723-b611-2e80f19bd76e
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '2050,2095p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2050	\]
  2051	At generic level ($k \neq -h^\vee$), the Sugawara construction is
  2052	nondegenerate: the Segal--Sugawara vector is a well-defined conformal
  2053	vector, and the Kac--Shapovalov determinant is nonvanishing.
  2054	No singular vectors enter the generating filtration, and the
  2055	critical-level degeneration of $\ChirHoch^0$ (which would promote
  2056	the Feigin--Frenkel center into $\ChirHoch^1$) is absent.
  2057	
  2058	The surviving degree-$1$ classes are therefore parametrized by the
  2059	generating space alone. The cochains
  2060	$J^a \mapsto \epsilon\,\phi^a$ for $\phi \in \fg$ form exactly
  2061	one copy of the adjoint $\fg$-module, and the Koszul resolution
  2062	provides no further degree-$1$ terms. Hence
  2063	\[
  2064	\ChirHoch^1(V_k(\fg)) \;\cong\; \fg.
  2065	\]
  2066	For $\fg = \mathfrak{sl}_N$, $\dim(\fg) = N^2 - 1$.
  2067	\end{proof}
  2068	
  2069	\begin{remark}[The $\mathfrak{sl}_2$ test and the failure of the

thinking
**Verifying claim references across files and volumes**

I'm gathering evidence to confirm the claim about `ChirHoch^1(V_k(g)) = g` and total dimension 5 by searching concordance, theorem registries, chapter labels, and metadata entries, including relevant lines in `chiral_center_theorem.tex` and `chiral_hochschild_koszul.tex`. I’ll also check Volumes II and III directories to verify if the claim or stronger variants appear there, making sure to capture file paths, line numbers, and snippets to summarize findings clearly.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\\(g\\)\\)\" -n /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "prop:chirhoch1-affine-km" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
CLAUDE.md:913:**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).
metadata/dependency_graph.dot:2321:  prop_chirhoch1_affine_km [label="prop:chirhoch1-affine-km\nproposition [Pr]\nGeneric affine first chiral Hochschild g...", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:337:| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
metadata/label_index.json:24738:  "prop:chirhoch1-affine-km": {
metadata/claims.jsonl:2224:{"label": "prop:chirhoch1-affine-km", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/theory/chiral_center_theorem.tex", "line": 1924, "title": "Generic affine first chiral Hochschild group"}
audit_campaign_20260412_231034/T07_thm_H.md:173:CLAUDE.md:498:| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
audit_campaign_20260412_231034/T07_thm_H.md:272:/bin/zsh -lc "rg -n \"Theorem H|thm:virasoro-hochschild|thm:w-algebra-hochschild|prop:chirhoch1-affine-km|thm:critical-level-cohomology|ClaimStatus.*H|Hilbert polynomial|Hilbert series|concentrated in .*\\{0, ?1, ?2\\}|amplitude|vdim\" chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/koszul_pair_structure.tex chapters examples metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/T07_thm_H.md:458: Proposition~\ref{prop:chirhoch1-affine-km}).}
audit_campaign_20260412_231034/T07_thm_H.md:1372:/bin/zsh -lc "rg -n \"prop:chirhoch1-affine-km|Generic affine first chiral Hochschild group|ChirHoch\\"'^1'"\\(V_k\" chapters/theory/chiral_hochschild_koszul.tex metadata/theorem_registry.md chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
audit_campaign_20260412_231034/T07_thm_H.md:1373:chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
audit_campaign_20260412_231034/T07_thm_H.md:1374:metadata/theorem_registry.md:337:| `prop:chirhoch1-affine-km` | `proposition` | 1924 | Generic affine first chiral Hochschild group |
audit_campaign_20260412_231034/T07_thm_H.md:1376:chapters/connections/concordance.tex:71: Prop.~\ref{prop:chirhoch1-affine-km}\textup{)}
audit_campaign_20260412_231034/T07_thm_H.md:1377:chapters/connections/concordance.tex:377: Proposition~\ref{prop:chirhoch1-affine-km}).}
audit_campaign_20260412_231034/T07_thm_H.md:1379:chapters/connections/concordance.tex:388: (Proposition~\ref{prop:chirhoch1-affine-km}).
audit_campaign_20260412_231034/T07_thm_H.md:1380:chapters/connections/concordance.tex:7084:\ref{prop:chirhoch1-affine-km}
audit_campaign_20260412_231034/T07_thm_H.md:1382:chapters/connections/concordance.tex:7086: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)}
audit_campaign_20260412_231034/T07_thm_H.md:1384:chapters/connections/concordance.tex:9653: \textup{(}Proposition~\ref{prop:chirhoch1-affine-km}\textup{)} \\
audit_campaign_20260412_231034/T07_thm_H.md:1477:/bin/zsh -lc "rg -n \"label\\{prop:chirhoch1-affine-km\\}|prop:chirhoch1-affine-km\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
audit_campaign_20260412_231034/T07_thm_H.md:1480:chapters/theory/chiral_center_theorem.tex:2003:\label{prop:chirhoch1-affine-km}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\" /Users/raeez/chiral-bar-cobar-vol2" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\" /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4760,4795p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4760	\emph{Proof.} The Heisenberg algebra $\mathcal{B}$ is chiral Koszul (Theorem~\ref{thm:km-chiral-koszul}): its bar construction $\bar{B}(\mathcal{B})$ is quasi-isomorphic to $\mathrm{CE}(\mathfrak{h}_{-k})$, which is concentrated in bar degrees $\leq 2$ (the only generating relation is the quadratic OPE $\alpha(z)\alpha(w) \sim k/(z-w)^2$, involving exactly two fields). The Koszul resolution therefore has the form:
  4761	\[\mathcal{B} \otimes \mathcal{B}^! \otimes \mathcal{B} \;\xrightarrow{d_2}\; \mathcal{B} \otimes (s\alpha) \otimes \mathcal{B} \;\xrightarrow{d_1}\; \mathcal{B} \otimes \mathcal{B}\]
  4762	with $\mathcal{B}^! = \mathrm{CE}(\mathfrak{h}_{-k})$ generated by a single element $s\alpha$ in bar degree~1 and its square in bar degree~2. Applying $\mathrm{Hom}_{\mathcal{B}\text{-}\mathcal{B}}(-, \mathcal{B})$ to this length-2 resolution yields a cochain complex concentrated in degrees $0, 1, 2$. Hence $\ChirHoch^n(\mathcal{B}) = 0$ for $n \geq 3$.
  4763	
  4764	\subsubsection{Summary for Heisenberg}
  4765	
  4766	\[\ChirHoch^*(\mathcal{B}) = \begin{cases}
  4767	\mathbb{C} & n = 0 \text{ (center = scalars)}\\
  4768	\mathbb{C} & n = 1 \text{ (outer derivation } D(\alpha) = \mathbf{1}\text{)}\\
  4769	\mathbb{C} & n = 2 \text{ (level deformation)}\\
  4770	0 & n \geq 3 \text{ (Koszul resolution length 2)}
  4771	\end{cases}\]
  4772	
  4773	The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
  4774	\end{example}
  4775	
  4776	\subsection{Explicit computation: free fermion}
  4777	
  4778	\begin{example}[Hochschild of free fermion]\label{ex:HH-fermion-complete}
  4779	For the free fermion $\mathcal{F}$ with fields $\psi(z), \psi^*(z)$ and OPE:
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "cor:universal-koszul" -n chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1927:(Corollary~\ref{cor:universal-koszul}), and the bar cohomology is
2031:(Corollary~\ref{cor:universal-koszul}).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"label\\{cor:universal-koszul\\}\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
audit_campaign_20260412_231034/T07_thm_H.md:1832:  1341	\label{cor:universal-koszul}
audit_campaign_20260412_231034/T13_koszul_equivs.md:479:  1341	\label{cor:universal-koszul}
audit_campaign_20260412_231034/T13_koszul_equivs.md:1237:  1341	\label{cor:universal-koszul}
chapters/theory/chiral_koszul_pairs.tex:1341:\label{cor:universal-koszul}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1320,1355p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1320	admits strong generators $\{a^i\}_{i \in I}$ whose normally ordered
  1321	monomials
  1322	$:\!\partial^{n_1} a^{i_1} \cdots \partial^{n_r} a^{i_r}\!:$
  1323	form a PBW basis; equivalently,
  1324	$\operatorname{gr}_F \cA \cong \operatorname{Sym}^{\mathrm{ch}}(V)$
  1325	where $V$ is the $\cD_X$-module spanned by the generators.
  1326	
  1327	Every freely strongly generated vertex algebra is chirally Koszul.
  1328	\end{proposition}
  1329	
  1330	\begin{proof}
  1331	The three hypotheses of Theorem~\ref{thm:pbw-koszulness-criterion}
  1332	hold: (1)~flatness of $F_p/F_{p-1} \cong S^p(V)$ by the PBW basis;
  1333	(2)~classical Koszulness of $\operatorname{gr}_F \cA \cong
  1334	\operatorname{Sym}^{\mathrm{ch}}(V)$ by Priddy's theorem;
  1335	(3)~finite-dimensionality of bar chain groups in each bigrading by
  1336	the partition bound of Theorem~\ref{thm:km-chiral-koszul}.
  1337	\end{proof}
  1338	
  1339	\begin{corollary}[Universal vertex algebras are chirally Koszul;
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\\\\(\\\\fg\\\\)\\) \\cong \\\\fg\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:ChirHoch\^1\(V_k\(\fg\)\) \cong \fg)
                                 ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(\\fg\\)\" chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\\(\\\\fg\\)\\)\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^1'"\\(V_k\\(\\\\mathfrak\\{g\\}\\\\)\\)\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:ChirHoch\^1\(V_k\(\mathfrak\{g\}\)\))
                         ^^
error: unrecognized escape sequence
wait(call_byTmgfZsfefMlmuPJNL8OLcH) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'ChirHoch\\"'^1'"\\(V_k\\(\\\\fg\\)\\)' -n chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_center_theorem.tex:1991:$\ChirHoch^1(V_k(\fg))$ is the adjoint representation of~$\fg$.
chapters/theory/chiral_center_theorem.tex:2008:\ChirHoch^1(V_k(\fg)) \;\cong\; \fg
chapters/theory/chiral_center_theorem.tex:2012:\dim \ChirHoch^1(V_k(\fg)) = \dim(\fg),
chapters/theory/chiral_center_theorem.tex:2045:\phi \;\in\; \ChirHoch^1(V_k(\fg))
chapters/theory/chiral_center_theorem.tex:2064:\ChirHoch^1(V_k(\fg)) \;\cong\; \fg.
chapters/theory/chiral_center_theorem.tex:2110:\text{for all } X, Y \in \fg \cong \ChirHoch^1(V_k(\fg)).
chapters/theory/chiral_center_theorem.tex:2204:The Gerstenhaber Lie algebra $\ChirHoch^1(V_k(\fg)) \cong \fg$
chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
chapters/theory/introduction.tex:684: algebra: $\ChirHoch^1(V_k(\fg)) \cong \fg$
chapters/connections/concordance.tex:67: $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
chapters/connections/concordance.tex:387: $\ChirHoch^1(V_k(\fg)) \cong \fg$
chapters/connections/concordance.tex:7085: & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
chapters/connections/concordance.tex:9652:& $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/introduction.tex | sed -n '660,700p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\"'^0" chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1856: $1 \in \ChirHoch^0$ \textup{(}the vacuum, center of~$\mathfrak{H}_k$\textup{)},
1870: \ChirHoch^0 = \bC, \qquad
1890: $\ChirHoch^0$ becomes infinite-dimensional:
1891: $\ChirHoch^0 = \mathfrak{z}(\widehat{\mathfrak{g}}_{-h^\vee})$,
1899: \ChirHoch^0 = \bC, \qquad
1954:$\ChirHoch^0 = \bC$ (center = vacuum at generic level),
2055:critical-level degeneration of $\ChirHoch^0$ (which would promote
2074:$\ChirHoch^0 = \bC$ and $\ChirHoch^2 = \bC$ from
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '4740,4795p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  4740	This imposes:
  4741	\[d\phi = 0\]
  4742	(cohomological condition)
  4743	
  4744	\emph{Trivial cocycles.} If $\phi = d\psi$ for some $\psi$, the deformation is trivial
  4745	(comes from a redefinition of $\alpha$).
  4746	
  4747	\emph{Nontrivial deformations.} The only independent deformation is changing the level $k$:
  4748	\[\alpha(z_1)\alpha(z_2) \sim \frac{k + t}{(z_1-z_2)^2}\]
  4749	
  4750	This gives a 1-dimensional space:
  4751	\[\ChirHoch^2(\mathcal{B}) = \mathbb{C} \cdot [k].\]
  4752	
  4753	Here $[k]$ is the cohomology class of the level.
  4754	
  4755	\subsubsection{\texorpdfstring{Higher degrees: $\ChirHoch^n(\mathcal{B})$ for $n \geq 3$}{Higher degrees: HH n(B) for n >= 3}}
  4756	
  4757	For the Heisenberg algebra (free boson), all higher Hochschild cohomology vanishes:
  4758	\[\ChirHoch^n(\mathcal{B}) = 0 \quad \text{for } n \geq 3\]
  4759	
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2030,2090p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is quadratic and chirally Koszul
(Corollary~\ref{cor:universal-koszul}).

The Koszul resolution of the diagonal bimodule takes the form
\[
0 \longrightarrow
\cA \otimes \fg^* \otimes \cA \longrightarrow
\cA \otimes \fg \otimes \cA \longrightarrow
\cA \otimes \cA \longrightarrow
\cA \longrightarrow 0,
\]
a three-term complex with generating space $V = \fg$. A degree-$1$
Hochschild cochain is a $\fg$-equivariant map from the generating
currents to the algebra:
\[
\phi \;\in\; \ChirHoch^1(V_k(\fg))
\quad\Longleftrightarrow\quad
J^a \;\longmapsto\; J^a + \epsilon\,\phi^a,
\qquad
\phi^a \in V_k(\fg).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/connections/concordance.tex | sed -n '40,90p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    40	 genus~$0$ unconditional; for arbitrary~$\cA$,
    41	 $g \geq 1$ is conditional on
    42	 axiom~\ref{MK:modular}; unconditional on the
    43	 CFT-type standard landscape except integer-spin
    44	 $\beta\gamma$ by Theorem~\ref{thm:pbw-propagation}
    45	 and Remark~\ref{rem:pbw-propagation-scope}
    46	 & \ClaimStatusProvedHere \\
    47	\textbf{C} & Complementarity
    48	 & $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\mathcal{M}}_g, Z(\cA))$
    49	 \textup{(}Thm~\ref{thm:quantum-complementarity-main}\textup{)};
    50	 Verdier-side Lagrangian splitting unconditional;
    51	 ambient shifted-symplectic upgrade conditional on
    52	 perfectness/nondegeneracy
    53	 & \ClaimStatusProvedHere \\
    54	\textbf{D} & Modular characteristic
    55	 & $\mathrm{obs}_g(\cA)=\kappa(\cA)\lambda_g$
    56	 for uniform-weight modular Koszul algebras
    57	 \textup{(}Definition~\ref{def:scalar-lane}\textup{)}
    58	 at all genera;
    59	 genus~$1$ universal for all families;
codex
I’ve read the proposition surface and its local proof. The main risk is already visible: the proof jumps from “quadratic + chirally Koszul” to a specific three-term Hochschild resolution and then to `HH^1 ≅ g` without citing or proving the missing comparison steps that would justify those reductions for affine vertex algebras.
exec
/bin/zsh -lc 'rg -n "thm:hochschild-polynomial-growth|cor:universal-koszul|thm:main-koszul-hoch|lem:chirhoch-descent|def:chiral-hochschild-cochain-brace|prop:model-independence|thm:bar-concentration|prop:pbw-universality|thm:affine-periodicity-critical" chapters/theory chapters/examples chapters/connections' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:5038:and Proposition~\ref{prop:pbw-universality} gives chiral
chapters/examples/w_algebras_deep.tex:5039:Koszulness via Corollary~\ref{cor:universal-koszul}.
chapters/examples/w_algebras_deep.tex:5051:Corollary~\ref{cor:universal-koszul}.
chapters/examples/w_algebras_deep.tex:5063:Corollary~\ref{cor:universal-koszul}.
chapters/examples/w_algebras_deep.tex:5247:PBW universality \textup{(}Proposition~\textup{\ref{prop:pbw-universality}}\textup{)}
chapters/connections/thqg_open_closed_realization.tex:260:Definition~\ref{def:chiral-hochschild-cochain-brace}).
chapters/connections/thqg_open_closed_realization.tex:274:(Theorem~\ref{thm:hochschild-polynomial-growth}) gives
chapters/examples/symmetric_orbifolds.tex:230:Theorem~\ref{thm:hochschild-polynomial-growth}, with degree
chapters/examples/symmetric_orbifolds.tex:309:(Proposition~\textup{\ref{prop:pbw-universality}}), then the
chapters/examples/symmetric_orbifolds.tex:320:universality (Proposition~\ref{prop:pbw-universality}) applies to
chapters/connections/thqg_symplectic_polarization.tex:1770:(Proposition~\ref{prop:pbw-universality}).
chapters/connections/thqg_symplectic_polarization.tex:1773:(Corollary~\ref{cor:universal-koszul}).
chapters/examples/beta_gamma.tex:65: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/y_algebras.tex:56: Cor~\ref{cor:universal-koszul} \\
chapters/examples/y_algebras.tex:66: & Proved & Thm~\ref{thm:hochschild-polynomial-growth} \\
chapters/examples/y_algebras.tex:671:Proposition~\ref{prop:pbw-universality} gives chiral Koszulness
chapters/examples/y_algebras.tex:672:via Corollary~\ref{cor:universal-koszul}.
chapters/theory/higher_genus_modular_koszul.tex:2172: Theorem~\textup{\ref{thm:main-koszul-hoch}}\textup{)}:
chapters/theory/higher_genus_modular_koszul.tex:3945: (Theorem~\ref{thm:main-koszul-hoch}), using Theorem~A
chapters/theory/higher_genus_modular_koszul.tex:16489:Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1910,2085p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Sugawara construction is nondegenerate|Kac--Shapovalov determinant is nonvanishing|no singular vectors enter the generating filtration|outer derivations|degree-1 classes are therefore parametrized by the generating space alone|three-term" chapters/theory/chiral_center_theorem.tex chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/introduction.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Theorem~H|Chiral Hochschild cohomology|polynomial growth|Hilbert polynomial|amplitude \\[0, 2\\]|total dimension at most four\" chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/introduction.tex chapters/theory/en_koszul_duality.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1910	 (Gel'fand--Fuchs cohomology) is infinite-dimensional; it is a
  1911	 \emph{different object} from $\ChirHoch^*(\mathrm{Vir}_c)$,
  1912	 which is bounded in degrees $\{0, 2\}$ with total dimension~$2$.
  1913	 The former is computed from the topological Lie algebra of
  1914	 smooth vector fields on~$S^1$ (no central charge, no chiral
  1915	 structure); the latter is computed from the vertex algebra
  1916	 $\mathrm{Vir}_c$ on a formal disc via the chiral Hochschild
  1917	 complex of Definition~\ref{def:chiral-hochschild-cochain-brace}.
  1918	\end{enumerate}
  1919	\end{proposition}
  1920	
  1921	\begin{proof}
  1922	\textbf{Part~(i).}
  1923	The Heisenberg algebra $\mathfrak{H}_k$ is generated by a single
  1924	weight-$1$ field $a(z)$ with OPE $a(z)\, a(w) \sim k/(z-w)^2$.
  1925	Since $\mathfrak{H}_k$ is quadratic (only binary OPE), it is
  1926	chirally Koszul
  1927	(Corollary~\ref{cor:universal-koszul}), and the bar cohomology is
  1928	$H^*(B(\mathfrak{H}_k)) = \operatorname{Sym}^{\mathrm{ch}}(V^*[1])$,
  1929	concentrated in bar degree~$1$.
 succeeded in 52ms:
chapters/theory/introduction.tex:323:(the log FM compactifications of~\cite{Mok25}), and Theorem~H requires the chiral
chapters/theory/introduction.tex:364:Theorem~H bounds the bulk state space: at generic level on the
chapters/theory/introduction.tex:365:Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
chapters/theory/introduction.tex:384:\emph{Coefficient ring}: Theorem~H identifies $\ChirHoch^*(\cA)$ as the finite-dimensional space over which~$\Theta_\cA$ varies.
chapters/theory/introduction.tex:497:\noindent\textbf{Theorem~H (chiral Hochschild).}\enspace
chapters/theory/introduction.tex:665:\item \emph{Theorem~H} (Chiral Hochschild cohomology,
chapters/theory/introduction.tex:678: $[0, 2]$ and total dimension at most four.
chapters/theory/introduction.tex:692: The primitive step is a descent lemma (Lemma~\ref{lem:chirhoch-descent}): on the Koszul locus, $\ChirHoch^*(\cA) \cong (\mathbb{D}_{\operatorname{Ran}} \barB(\cA))_{\Sigma}$, reducing Theorem~H to Theorem~A's Verdier intertwining.
chapters/theory/introduction.tex:705:Koszul locus (Theorem~H).
chapters/theory/introduction.tex:761: \textup{(}Theorem~H\textup{)}.
chapters/theory/introduction.tex:851: \textup{(}Theorem~H\textup{)}.
chapters/theory/introduction.tex:2192: Chiral Koszul pairs; chiral modules; \textbf{Theorem~H} ($\ChirHoch^*$ polynomial, Koszul-functorial) \\
chapters/theory/introduction.tex:2336: \textbf{Theorem~H}: $\ChirHoch^*(\cA)$ polynomial of amplitude
chapters/theory/en_koszul_duality.tex:2757: explicitly (Theorem~H), and the unit $\eta_B$ is an
chapters/theory/en_koszul_duality.tex:2771: Theorem~H shows $\ChirHoch^*(\cA)$ is concentrated in
chapters/theory/en_koszul_duality.tex:2772: degrees $\{0, 1, 2\}$ with total dimension at most four on
chapters/theory/chiral_center_theorem.tex:1832:These computations verify the general structure of Theorem~H
chapters/theory/chiral_center_theorem.tex:1833:(polynomial growth) and provide concrete generators, products,
chapters/theory/chiral_center_theorem.tex:2080:The correct uniform statement is Theorem~H: concentration in
chapters/theory/chiral_center_theorem.tex:2081:degrees $\{0, 1, 2\}$ with polynomial growth, but no universal bound
 succeeded in 52ms:
chapters/theory/en_koszul_duality.tex:232:three-term relation on $\Conf_k(\bC)$. By contrast, $n = 1$ is the
chapters/theory/en_koszul_duality.tex:243:relations among these pullbacks are generated by the three-term
chapters/theory/en_koszul_duality.tex:2098: Arnold relations (three-term identity on residues) replace the
chapters/theory/en_koszul_duality.tex:3679:(outer derivations: infinitesimal level-preserving
chapters/theory/chiral_center_theorem.tex:1879: The three-dimensional $\ChirHoch^1$ consists of the outer derivations
chapters/theory/chiral_center_theorem.tex:1937:by the three-term resolution
chapters/theory/chiral_center_theorem.tex:1955:$\ChirHoch^1 \cong V = \mathfrak{sl}_2$ (outer derivations: the space of
chapters/theory/chiral_center_theorem.tex:1961:three-term Koszul resolution.
chapters/theory/chiral_center_theorem.tex:1995:is a three-term complex whose degree-$1$ piece is $\fg$ itself.
chapters/theory/chiral_center_theorem.tex:2041:a three-term complex with generating space $V = \fg$. A degree-$1$
chapters/theory/chiral_center_theorem.tex:2053:vector, and the Kac--Shapovalov determinant is nonvanishing.
chapters/theory/chiral_center_theorem.tex:2210:$\mathrm{DS}_*$ kills all three outer derivations of
chapters/theory/chiral_center_theorem.tex:2229:is zero.  Concretely, the three outer derivations
chapters/theory/chiral_center_theorem.tex:2345:The $N^2 - 1$ outer derivations decompose into three strata:
chapters/theory/chiral_hochschild_koszul.tex:880:argument (cf.\ \cite{LV12}, \S10.3) applied to the three-term
chapters/theory/chiral_hochschild_koszul.tex:2314:$\vartheta$ of any odd characteristic, and the three-term relation
chapters/theory/chiral_hochschild_koszul.tex:4078:\ChirHoch^1 &= 0 & & \text{(no outer derivations)}, \\
chapters/theory/chiral_hochschild_koszul.tex:4082:The deformation in $\ChirHoch^2$ corresponds to the level family $k \mapsto k + t$; the vanishing $\ChirHoch^1 = 0$ reflects rigidity (no outer derivations).
chapters/theory/chiral_hochschild_koszul.tex:4773:The Poincar\'e polynomial is $P_{\mathcal{B}}(t) = 1 + t + t^2$. For algebras whose OPE among generators has \emph{no simple pole} (i.e., the zero mode $a_{(0)}$ is central), all outer derivations survive and $\ChirHoch^1 = \mathbb{C}^d$ where $d$ is the number of strong generators. The Heisenberg ($d = 1$, double pole only) is the prototypical case. For algebras with simple poles, the structure of $\ChirHoch^1$ depends on the family: for affine Kac--Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km}), reflecting the $\dim(\fg)$-dimensional space of current-algebra deformations; for the $bc$ and $\beta\gamma$ systems, the simple-pole sector is one-dimensional and $\ChirHoch^1 = \mathbb{C}$ (Remark~\ref{rem:boson-fermion-hochschild-comparison}).
chapters/theory/hochschild_cohomology.tex:70:For an associative algebra $A$ over $\mathbb{C}$ and an $A$-bimodule~$M$, the Hochschild cohomology $HH^*(A, M) = \mathrm{Ext}^*_{A^e}(A, M)$ classifies the deformation theory of~$A$: $HH^0$ is the center, $HH^1$ classifies outer derivations, $HH^2$ classifies first-order deformations, and $HH^3$ contains the obstructions to extending them. The full structure is computed by the bar resolution $\cdots \to A^{\otimes(n+2)} \xrightarrow{b} A^{\otimes(n+1)} \to \cdots$ with differential $b(a_0 \otimes \cdots \otimes a_{n+1}) = \sum_{i=0}^n (-1)^i a_0 \otimes \cdots \otimes a_ia_{i+1} \otimes \cdots \otimes a_{n+1}$, and the resulting cohomology carries a Gerstenhaber bracket governing the Maurer--Cartan equation for formal deformations (Gerstenhaber~\cite{Ger63}).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5190,5235p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathrm{Crit}(S)$ is therefore $\{a : [a,a] = 0\}$, the
Maurer--Cartan locus. Any relation to critical opers is indirect
and mediated by the separate bar-cohomological theorem
Theorem~\ref{thm:oper-bar-h0}; the present conjecture does not
identify the Maurer--Cartan locus with the oper space.
\end{remark}

\begin{conjecture}[SC deformation complex at critical level;
\ClaimStatusConjectured]\label{conj:sc-deformation-critical}
\index{critical level!SC deformation complex}
\index{Swiss-cheese!critical level deformation}
At the critical level $k = -h^\vee$ for $\fg$ simple of rank~$r$
with exponents $m_1 \le \cdots \le m_r$, the SC deformation complex
governing the chiral Swiss-cheese pair
$\bigl(\ChirHoch^*(\widehat{\fg}_{-h^\vee}),\, \widehat{\fg}_{-h^\vee}\bigr)$
exhibits the following structure:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(Degree-$0$ jump)}\quad
 $\ChirHoch^0(\widehat{\fg}_{-h^\vee})
 = \mathfrak{z}(\widehat{\fg}_{-h^\vee})
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"dim\\(g\\)\\+2\" chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Summarizing dimension remarks with file references**

I'll gather precise file paths and line numbers with brief snippets highlighting the total dimension formula for `ChirHoch^1` and its relationship to `dim(g)`, referencing key remarks and propositions mainly around `chapters/theory/chiral_center_theorem.tex` lines 2008-2060, plus additional confirmations from `chiral_hochschild_koszul.tex`, concordance files, metadata entries, CLAUDE.md, and Vol II/III searches to show this dimension formula is established, with snippets confirming `ChirHoch^0 = C` and `ChirHoch^2 = C` and that `ChirHoch^1` grows with `dim(g)`.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2066,2086p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
For $\fg = \mathfrak{sl}_N$, $\dim(\fg) = N^2 - 1$.
\end{proof}

\begin{remark}[The $\mathfrak{sl}_2$ test and the failure of the
 na\"{\i}ve dimension bound]
\label{rem:sl2-chirhoch-dim5}
At $\fg = \mathfrak{sl}_2$, the proposition gives
$\dim \ChirHoch^1 = 3$. Combined with the one-dimensional groups
$\ChirHoch^0 = \bC$ and $\ChirHoch^2 = \bC$ from
Proposition~\ref{prop:derived-center-explicit}(ii), the total
dimension of $\ChirHoch^*(V_k(\mathfrak{sl}_2))$ is
$1 + 3 + 1 = 5$, not~$4$. The older conjectural bound
$\dim \ChirHoch^*(\cA) \leq 4$ (which holds for the Heisenberg and
Virasoro algebras) fails at the first non-abelian example.
The correct uniform statement is Theorem~H: concentration in
degrees $\{0, 1, 2\}$ with polynomial growth, but no universal bound
on the total dimension. The dimension of $\ChirHoch^1$ grows with
$\dim(\fg)$: it is $8$ for $\mathfrak{sl}_3$, $15$ for
$\mathfrak{sl}_4$, $248$ for type $E_8$.
\end{remark}
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '520,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '2170,2365p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/bar_construction.tex | sed -n '1438,1488p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1048,1415p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   520	by the shift~$[-p]$, so the combined grading contribution at
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
 succeeded in 52ms:
  1438	$\mathcal{D}$-module map), with the residue differential ($f$
  1439	preserves the chiral product), and does not affect the de~Rham
  1440	component, $\bar{B}^{\mathrm{geom}}(f)$ commutes with
  1441	$d = d_{\mathrm{int}} + d_{\mathrm{res}} + d_{\mathrm{dR}}$.
  1442	
  1443	\emph{Coalgebra morphism.}\label{lem:bar-induced-coalgebra}
  1444	The coproduct $\Delta$ is defined by restricting to collision
  1445	divisors; since $f$ acts on algebra factors and $\Delta$ acts
  1446	on the indexing set,
  1447	$\Delta \circ \bar{B}(f) = (\bar{B}(f) \otimes \bar{B}(f))
  1448	\circ \Delta$. The counit compatibility and preservation of
  1449	identities and composition are immediate from the definition.
  1450	\end{proof}
  1451	
  1452	\begin{corollary}[Natural transformation property; \ClaimStatusProvedHere]\label{cor:bar-natural}
  1453	\label{cor:why-functoriality}
  1454	A commutative diagram of chiral algebras induces a commutative diagram of bar complexes: if $k \circ f = g \circ h$ in $\mathsf{ChirAlg}_X$, then $\bar{B}(k) \circ \bar{B}(f) = \bar{B}(g) \circ \bar{B}(h)$ in $\mathsf{dgCoalg}_X$. This is immediate from functoriality.
  1455	\end{corollary}
  1456	
  1457	\begin{proposition}[Model independence; \ClaimStatusProvedHere]
 succeeded in 52ms:
  2170	the bracket becomes $[X,Y]_\fg$. Therefore
  2171	\[
  2172	[D_X, D_Y] \;=\; D_{[X,Y]_{\fg}}.
  2173	\]
  2174	Substituting the $\mathfrak{sl}_2$ structure constants
  2175	$[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$ gives the three
  2176	displayed relations.
  2177	
  2178	\medskip\noindent
  2179	\textit{Verification by compute engine.}
  2180	The engine
  2181	\texttt{gerstenhaber\_sl2\_bracket\_engine.py}
  2182	builds the structure-constant tensor $f^{ab}_{\ c}$, computes
  2183	the chiral brace and Gerstenhaber bracket on all nine pairs
  2184	of basis derivations, and verifies graded antisymmetry and
  2185	the Jacobi identity on all $27$ triples.
  2186	All $49$ tests pass.
  2187	\end{proof}
  2188	
  2189	\begin{remark}[First non-abelian $E_3$ structure verification]
 succeeded in 52ms:
  1048	(the three independent cocycles $L_{-1}^*, L_{-2}^*, L_{-3}^*$
  1049	on $\mathrm{span}\{L_{-1}, L_{-2}, L_{-3}\}$).
  1050	The chiral bar cohomology of the Virasoro algebra has
  1051	$\dim H^1(\barBgeom(\mathrm{Vir})) = 1$
  1052	(a single generator~$T$ of conformal weight~$2$).
  1053	The discrepancy $3 - 1 = 2$ quantifies the
  1054	Orlik--Solomon form contribution: the chiral bar differential
  1055	uses the full logarithmic residue $d\log(z_1 - z_2)$
  1056	(the Arnold relation on configuration space),
  1057	which collapses the three CE cocycles to the single
  1058	chiral primary.
  1059	\end{remark}
  1060	
  1061	\begin{theorem}[Bar concentration for Koszul pairs; \ClaimStatusProvedHere]
  1062	\label{thm:bar-concentration}
  1063	\index{bar complex!concentration}
  1064	\textup{[Regime: quadratic on the Koszul locus
  1065	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
  1066	
  1067	Let $(\cA_1, \cA_2)$ be a chiral Koszul pair
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'dim\\(\\\\mathfrak\\{g\\}\\) \\+ 2' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2085,2145p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{proposition}[Gerstenhaber bracket on
$\ChirHoch^1(V_k(\mathfrak{sl}_2))$; \ClaimStatusProvedHere]
\label{prop:gerstenhaber-sl2-bracket}
\index{Gerstenhaber bracket!affine sl2@affine $\mathfrak{sl}_2$|textbf}
Let $V_k(\mathfrak{sl}_2)$ be the affine vertex algebra at generic
level~$k$ \textup{(}$k \neq -2$\textup{)}.
The Gerstenhaber bracket of degree~$-1$ on
$\ChirHoch^*(V_k(\mathfrak{sl}_2))$
restricts on $\ChirHoch^1 \times \ChirHoch^1 \to \ChirHoch^1$ to
the $\mathfrak{sl}_2$ Lie bracket:
\begin{align}
[D_e,\, D_f] &= D_h, \label{eq:gerst-ef}\\
[D_h,\, D_e] &= 2\,D_e, \label{eq:gerst-he}\\
[D_h,\, D_f] &= -2\,D_f, \label{eq:gerst-hf}
\end{align}
where $D_X \in \ChirHoch^1(V_k(\mathfrak{sl}_2)) \cong
\mathfrak{sl}_2$
\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '492,710p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '760,835p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1800,1915p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:derived-center-explicit|derived-center-explicit" chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/introduction.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   760	$n \notin \{0, 1, 2\}$.\footnote{This is the chiral analogue
   761	of Brylinski's theorem: for $\mathcal{D}_X$ on a smooth
   762	variety of dimension~$d$,
   763	$\mathrm{HH}^n(\mathcal{D}_X)
   764	\cong H^{2d-n}_{\mathrm{dR}}(X)$,
   765	which vanishes for $n \notin \{0, \ldots, 2d\}$.}
   766	
   767	Part~(b): concentration in the range $\{0, 1, 2\}$ means
   768	$P_\cA(t)$ is a polynomial of degree at most~$2$.
   769	Identifying $\ChirHoch^0(\cA) = Z(\cA)$ (the center) and
   770	$\ChirHoch^2(\cA) \cong \ChirHoch^0(\cA^!)^\vee \otimes \omega_X$
   771	(by Theorem~\ref{thm:main-koszul-hoch} with $n = 2$) gives
   772	$\dim \ChirHoch^2(\cA) = \dim Z(\cA^!)$.
   773	
   774	Part~(c) follows from applying~(b) to both $\cA$ and $\cA^!$ and
   775	using the duality of Theorem~\ref{thm:main-koszul-hoch}.
   776	\end{proof}
   777	
   778	\begin{remark}[Geometric substrate (Volume~II)]
   779	\label{rem:theorem-h-lagrangian}
 succeeded in 52ms:
   492	$Z_{\mathrm{ch}} = 1/\eta(\tau)$ gives
   493	$F_1 = \kappa(\cH_k)/24 = k/24$
   494	as the genus-$1$ free energy on~$\overline{\cM}_{1,1}$.)
   495	
   496	\smallskip
   497	\noindent\textbf{Theorem~H (chiral Hochschild).}\enspace
   498	$\ChirHoch^*(\cH_k) = (\C, \C, \C)$ concentrated in degrees
   499	$\{0, 1, 2\}$: the class in degree~$0$ is the center (scalars),
   500	the class in degree~$1$ is the outer chiral derivation
   501	$D(\alpha) = \mathbf{1}$ (non-inner because $\alpha_{(0)} = 0$
   502	when the OPE has no simple pole), and the class in degree~$2$ is
   503	the level deformation (double-pole OPE datum).
   504	The Koszul resolution has length~$2$, so
   505	$\ChirHoch^n = 0$ for $n \ge 3$; Hilbert series $1 + t + t^2$,
   506	the rank-$1$ case of the polynomial-growth theorem.
   507	
   508	The full computation appears in Chapter~\ref{ch:heisenberg-frame}.
   509	
   510	\subsection{The general theorems}
   511	\label{subsec:five-theorems-general}
 succeeded in 52ms:
  1800	 $C^\bullet_{\mathrm{ch}}(\cA, \cA)$.
  1801	
  1802	\item \emph{Modular.}
  1803	 The open/closed MC element $\Theta^{\mathrm{oc}}_\cA$
  1804	 (Construction~\ref{constr:thqg-oc-mc-element}) packages the
  1805	 bar-intrinsic MC element $\Theta_\cA$ with the boundary
  1806	 $A_\infty$-module data. Its shadow obstruction tower projections
  1807	 recover the nonlinear modular shadows
  1808	 $(\kappa, \mathfrak{C}, \mathfrak{Q}, \ldots)$ in the
  1809	 closed sector and boundary corrections in the open sector.
  1810	\end{enumerate}
  1811	In the language of this section: every global observable on
  1812	$(X, D, \tau)$ restricts, via the local-global bridge, to an
  1813	element of the universal pair $U(\cA)$. The chiral center
  1814	theorem guarantees this restriction is unique.
  1815	\end{remark}
  1816	
  1817	
  1818	%% ===========================================================
  1819	%% EXPLICIT DERIVED CENTER COMPUTATIONS
 succeeded in 50ms:
chapters/theory/chiral_center_theorem.tex:1823:\label{subsec:derived-center-explicit}
chapters/theory/chiral_center_theorem.tex:1838:\label{prop:derived-center-explicit}
chapters/theory/chiral_center_theorem.tex:2075:Proposition~\ref{prop:derived-center-explicit}(ii), the total
chapters/theory/chiral_center_theorem.tex:2264:\textup{(}Proposition~\textup{\ref{prop:derived-center-explicit}(iii))}.
chapters/theory/chiral_center_theorem.tex:2314:(Proposition~\ref{prop:derived-center-explicit}(iii)),
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\dim\\\\(\\\\fg\\\\)\\\\+2' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\dim \\\\fg \\+ 2' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Inspecting mathematical proof**

I need to look into the derived-center-explicit proof, as it might rely on some prior issues. I want to find the exact line of concern. I’ve read some related material before, like the label prop:bar-resolution-chirhoch and def:chiral-hochschild-cochain-brace, to understand what the actual object is. The proposition states that a "degree-1 cochain is an equivariant map," but I need to verify if that's from the definition or not. Let's dive deeper into this!
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'dim\\(g\\)\\+2' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "total dimension.*dim" chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2082:on the total dimension. The dimension of $\ChirHoch^1$ grows with
codex
I’m now tracing the exact proof infrastructure beneath the proposition rather than just the proposition itself. The critical question is whether the manuscript actually proves that the chiral Hochschild complex for `V_k(g)` collapses to a length-2 Koszul bimodule computation, or whether that is asserted by analogy with classical quadratic algebras.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '260,420p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:bar-resolution-chirhoch|def:bigraded-hochschild|def:chiral-hochschild|def:chiral-hochschild-cochain-brace|hochschild-bar-cobar" chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Kac--Shapovalov criterion|vacuum module is Verma with no null vectors|generic level|nonvanishing determinant|bar-relevant range" chapters/theory/chiral_koszul_pairs.tex chapters/examples/kac_moody.tex chapters/theory/chiral_center_theorem.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   260	of~$g$, then substitutes the result into the $i$-th
   261	slot of~$f$. At the level of spectral variables,
   262	both sides perform the same three-level block
   263	substitution:
   264	\[
   265	\lambda^{(f)}_{\cdot}
   266	\;\leftarrow\;
   267	\lambda^{(f)}_{\cdot}(\nu^{(g)}_{\cdot})
   268	\;\leftarrow\;
   269	\lambda^{(f)}_{\cdot}(\nu^{(g)}_{\cdot}(\rho^{(h)}_{\cdot})),
   270	\]
   271	and the Koszul signs are identical because the
   272	suspended degree of $(g \circ_j h)$ equals
   273	$\|g\| + \|h\|$ and the elements past which the
   274	operations must be commuted are the same on both sides.
   275	
   276	For~(a) (sequential associativity): the two substitutions
   277	act on disjoint slots of~$f$, so the spectral variables
   278	are independent. The sign $(-1)^{\|g\| \cdot \|h\|}$
   279	arises from interchanging the order in which $g$
 succeeded in 52ms:
chapters/theory/chiral_center_theorem.tex:36:(Definition~\ref{def:chiral-hochschild-cochain-brace},
chapters/theory/chiral_center_theorem.tex:299:\label{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:349:Definition~\ref{def:chiral-hochschild-cochain-brace}
chapters/theory/chiral_center_theorem.tex:1917: complex of Definition~\ref{def:chiral-hochschild-cochain-brace}.
chapters/theory/hochschild_cohomology.tex:53: (Definition~\ref{def:chiral-hochschild}),
chapters/theory/hochschild_cohomology.tex:77:\label{def:chiral-hochschild-derived}
chapters/theory/hochschild_cohomology.tex:83:The chain-level model is Definition~\ref{def:chiral-hochschild}.
chapters/theory/hochschild_cohomology.tex:470:\label{def:chiral-hochschild}
chapters/theory/chiral_hochschild_koszul.tex:324:\begin{theorem}[Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
chapters/theory/chiral_hochschild_koszul.tex:484:\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})}
chapters/theory/chiral_hochschild_koszul.tex:587:\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})} satisfies
chapters/theory/chiral_hochschild_koszul.tex:737:The derived chiral Hochschild complex $\mathrm{RHH}_{\mathrm{ch}}(A)$ is computed by the algebraic cochain complex $C^*_{\mathrm{ch}}(A, A)$ of Definition~\ref{def:chiral-hochschild-cochain-brace} (\texttt{chiral\_center\_theorem.tex}), which in turn is identified with $\mathrm{RHom}_{\mathsf{ChirAlg}}(A, A)$ via the bar resolution (Proposition~\ref{prop:bar-resolution-chirhoch}).
chapters/theory/chiral_hochschild_koszul.tex:740:Part~(a): by Theorem~\ref{thm:hochschild-bar-cobar},
 succeeded in 52ms:
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
 succeeded in 51ms:
chapters/connections/concordance.tex:67: $\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level
chapters/connections/concordance.tex:378: For the principal $\Walg$-algebra $\Walg^k(\fg)$ at generic level:
chapters/connections/concordance.tex:385: Rank $r \geq 2$: $P(t) = 1 + t^2$ at generic level.
chapters/connections/concordance.tex:386: For affine Kac--Moody at generic level:
chapters/connections/concordance.tex:2210: $\mathcal{W}$-algebra at generic level); strict Koszulity is
chapters/connections/concordance.tex:2435: Kac--Shapovalov: $\det G_h \neq 0$ in the bar-relevant range
chapters/connections/concordance.tex:2479:\item \emph{Kac--Shapovalov criterion}
chapters/connections/concordance.tex:2481: $\det G_h \neq 0$ in the bar-relevant range.
chapters/connections/concordance.tex:2484: bar-relevant range and this route is blocked.
chapters/connections/concordance.tex:3010:\item \emph{Kac--Shapovalov}: $\det G_h \neq 0$ in bar-relevant range $\Leftrightarrow$ Koszul (Theorem~\ref{thm:kac-shapovalov-koszulness}); proved for $V_k(\fg)$ (Proposition~\ref{prop:pbw-universality}). For simple admissible quotients $L_k(\fg)$ this route is blocked by null vectors in the bar-relevant range.
chapters/connections/concordance.tex:3366: \cW_k(\mathfrak{sl}_3, f_{\mathrm{min}})$ is chirally Koszul at generic level ($k \neq -3$),
chapters/connections/concordance.tex:3378: $\mathrm{Par}(N)$ at generic level.
chapters/connections/concordance.tex:3454:affine $\cW$-algebras in type~$A$ at generic level
chapters/connections/concordance.tex:4080:This covers the entire standard landscape at generic levels:
chapters/connections/concordance.tex:4331:at generic level: PBW-filtration strictness~(ii) $\iff$
chapters/connections/concordance.tex:4716:$H$ & Chiral Hochschild: $\ChirHoch^n = 0$ for $n > 2$, $P(t) = 1+t^2$; & \textbf{Proved} (generic level, & Thms~\ref{thm:w-algebra-hochschild}, \\
chapters/connections/concordance.tex:4811:These coincide for Heisenberg ($\kappa = k$), Virasoro ($\kappa = c/2$), and affine KM at generic level ($\kappa = \dim(\mathfrak{g})(k{+}h^\vee)/(2h^\vee)$). They diverge for K3-fibered CY$_3$ (where (ii) and (iv) differ by a factor of $5/0 = \infty$) and for non-compact toric CY$_3$ (where (ii) and (iii) differ by a factor of $12$). The modular characteristic $\kappa(\cA)$ in the sense of (i) is the intrinsic invariant; the others are geometric proxies valid in restricted contexts.
chapters/connections/concordance.tex:7085: & $\ChirHoch^1(V_k(\fg)) \cong \fg$ at generic level
chapters/connections/concordance.tex:7193: generic level. For $\widehat{\fsl}_2$ at critical level,
chapters/connections/concordance.tex:7965:Theorem~H (chiral Hochschild) connects them: at generic level,


exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'ChirHoch\\"'^2'"\\(V_k\\(\\\\fg\\)\\)' -n chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Summarizing claim audit details**

I'll organize a thorough audit listing key sources—proposition and remark in the chiral center theorem, the chiral hochschild koszul reference, concordance and CLAUDE summary entries, metadata registry and claims, plus a search confirming no duplicates found in Vol II/III—each with precise paths, line numbers, and brief snippets supporting the dimension claim.
codex
**Claim Audit**
- `chapters/theory/chiral_center_theorem.tex:2008-2075` proves `\ChirHoch^1(V_k(\fg)) ≅ \fg` at generic level via `prop:chirhoch1-affine-km` and the following remark notes `\ChirHoch^0 = \mathbb{C}` and `\ChirHoch^2 = \mathbb{C}`, so the sl₂ test gives total dimension `1+3+1=5` and, more generally, the combination `1 + \dim(\fg) + 1 = \dim(\fg)+2` holds.
- `chapters/theory/chiral_hochschild_koszul.tex:4760-4774` reiterates the same claim in the Hochschild examples section, stating “for affine Kac–Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition~\ref{prop:chirhoch1-affine-km})”.
- `chapters/connections/concordance.tex:64-75` lists Theorem H with “$\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level,” and `CLAUDE.md:498`’s table row for “ChirHoch^1 KM” says “ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km)”.
- `metadata/theorem_registry.md:337` records label `prop:chirhoch1-affine-km` with title “Generic affine first chiral Hochschild group,” and `metadata/claims.jsonl:2224` marks the same label as `ProvedHere` pointing to `chapters/theory/chiral_center_theorem.tex` line 1924.
- Searches for `ChirHoch^1(V_k(g))` (and the same total-dimension phrasing) in `~/chiral-bar-cobar-vol2` and `~/calabi-yau-quantum-groups` returned no hits, so Volumes II/III do not duplicate or strengthen the claim.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'dim g \\+ 2' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Inspecting Kac-Shap criterion**

I need to take a closer look at the Kac-Shap criterion, especially around the relevant lines. It seems important to understand how it relates to some propositions about the generic level and the absence of nulls. I wonder if I should involve some examples or applications to clarify its implications. Let’s figure out how to break this down and make it more comprehensible for understanding potential outcomes related to the theorem.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '1405,1458p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '5200,5235p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_koszul_pairs.tex | sed -n '2628,2735p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '60,75p;370,390p;4708,4722p;7078,7090p;9647,9658p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1405	\begin{theorem}[Kac--Shapovalov criterion for simple quotients;
  1406	\ClaimStatusProvedHere]
  1407	\label{thm:kac-shapovalov-koszulness}
  1408	\index{Koszul property!Kac--Shapovalov criterion}
  1409	\index{Kac determinant!Koszulness criterion}
  1410	\index{Shapovalov form!Koszulness criterion}
  1411	
  1412	Let $\cA$ be a conformal vertex algebra with Shapovalov form on the
  1413	vacuum module. The \emph{bar-relevant range} is the set of conformal
  1414	weights~$h$ with $\barBgeom^n_h(\cA) \neq 0$ for some $n > 0$.
  1415	Then $\cA$ is chirally Koszul if and only if the Kac--Shapovalov
  1416	determinant $\det G_h \neq 0$ for all~$h$ in the bar-relevant range.
  1417	
  1418	For universal algebras this holds unconditionally
  1419	(Corollary~\ref{cor:universal-koszul}). The genuine content is for
  1420	simple quotients: $L_k(\fg)$ has null vectors at
  1421	$h = h_{\mathrm{sing}}(k)$ by the Kac--Kazhdan theorem; at admissible
  1422	levels $k + h^\vee = p/q$, $(p,q)=1$, these lie in the bar-relevant
  1423	range and Koszulness may fail. For the Virasoro algebra, the Kac
  1424	determinant $\det G_h = \prod_{rs \leq h}(h - h_{r,s}(c))^{p(h-rs)}$
 succeeded in 50ms:
  2628	Zero counterexamples have been found: across all tested
  2629	families, null vectors simultaneously create off-diagonal
  2630	bar cohomology \emph{and} mixed Hodge extensions.
  2631	For the affine Kac--Moody lineage, the converse of~\textup{(xii)}
  2632	is a theorem; the open case is the non-affine lineage
  2633	(Virasoro, $\cW$-algebras), where the key missing ingredient
  2634	is a Hodge-theoretic interpretation of the BPZ differential
  2635	equations.
  2636	\end{remark}
  2637	
  2638	\begin{proposition}[$\cD$-module purity for affine Kac--Moody algebras]
  2639	\label{prop:d-module-purity-km}
  2640	\ClaimStatusProvedHere
  2641	\index{D-module purity!affine Kac--Moody|textbf}
  2642	For $\cA = V_k(\fg)$ at generic level~$k$,
  2643	$\barBgeom_n(\cA)$ is pure of weight~$n$ as a mixed Hodge
  2644	module on $\FM_n(X)$. The proof uses chiral localization
  2645	\textup{(}Frenkel--Gaitsgory\textup{)} to identify
  2646	$\barBgeom_n$ with a $\cD$-module on the affine
  2647	Grassmannian, where purity follows from the Hitchin
 succeeded in 50ms:
  5200	\index{Swiss-cheese!critical level deformation}
  5201	At the critical level $k = -h^\vee$ for $\fg$ simple of rank~$r$
  5202	with exponents $m_1 \le \cdots \le m_r$, the SC deformation complex
  5203	governing the chiral Swiss-cheese pair
  5204	$\bigl(\ChirHoch^*(\widehat{\fg}_{-h^\vee}),\, \widehat{\fg}_{-h^\vee}\bigr)$
  5205	exhibits the following structure:
  5206	\begin{enumerate}[label=\textup{(\roman*)}]
  5207	\item \textup{(Degree-$0$ jump)}\quad
  5208	 $\ChirHoch^0(\widehat{\fg}_{-h^\vee})
  5209	 = \mathfrak{z}(\widehat{\fg}_{-h^\vee})
  5210	 \cong \mathrm{Fun}(\mathrm{Op}_{\fg^\vee}(D))
  5211	 \cong \bC[\Theta_1, \ldots, \Theta_r]$,
  5212	 jumping from $\bC$ at generic level to
  5213	 the infinite-dimensional Feigin--Frenkel center.
  5214	\item \textup{(Degree-$1$ jump)}\quad
  5215	 $\ChirHoch^1(\widehat{\fg}_{-h^\vee})$ also jumps: at generic level it equals~$\fg$
  5216	 \textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km}}\textup{)};
  5217	 at critical level the Beilinson--Drinfeld comparison
  5218	 \textup{(}Theorem~\textup{\ref{thm:affine-periodicity-critical}}\textup{)}
  5219	 gives the full odd-degree Gelfand--Fuchs component
 succeeded in 50ms:
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
    73	\end{tabular}
    74	\end{center}
    75	
   370	 This gives a vertex-algebraic chain model interfacing with the
   371	 oper side of the geometric Langlands programme.
   372	
   373	\item \emph{Chiral Hochschild cohomology
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\\\"'^0.*V_k" -n chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'ChirHoch\\"'^2'"\\(V_k\\(\\\\fg\\)\\)' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\label\\{thm:hochschild-polynomial-growth\\}\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{thm:hochschild-polynomial-growth\})
       ^^
error: unrecognized escape sequence

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n '\\\\label\\{thm:hochschild-polynomial-growth\\}' -n chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:689:\label{thm:hochschild-polynomial-growth}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '640,720p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   640	Applying this on $\overline{C}_{n+2}(X)$ with
   641	$\mathcal{M} = \mathrm{Hom}(\mathcal{A}^!, \mathcal{A})$:
   642	the Koszul pairing identifies
   643	\[
   644	\mathbb{D}(\mathrm{Hom}(\mathcal{A}^!, \mathcal{A}))
   645	\cong \mathrm{Hom}(\mathcal{A}, \mathcal{A}^!)
   646	\otimes \omega_{\overline{C}_{n+2}}.
   647	\]
   648	By Lemma~\ref{lem:hochschild-shift-computation}, the variable
   649	Verdier shift~$[n+2]$ at bar degree~$n$ collapses to the uniform
   650	constant~$[2]$ after totalization and Koszul concentration: the
   651	totalization contributes $[-n]$, giving net shift $(n+2)-n = 2$
   652	independent of~$n$. The $\omega_X$ twist encodes
   653	$\mathcal{D}$-module duality on the base curve. Consequently,
   654	\[
   655	\ChirHoch^n(\mathcal{A})
   656	\cong \ChirHoch^{2-n}(\mathcal{A}^!)^{\vee} \otimes \omega_X.
   657	\]
   658	The full details are given in the second proof below.
   659	

thinking
**Verifying total dimension formula**

I'm connecting the formula for total dimension to the centers of the algebras involved, noting both centers are essentially the complex numbers, which keeps the polynomial degree terms consistent. I want to reference propositions and theorems supporting the dimension count for the generic `V_k(g)`, especially highlighting that the center is just scalars. To do that, I'll search the codebase for mentions of the center in the relevant files, aiming to cite the right results precisely.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'Z\\(V_k\\(\\\\fg\\)\\)' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Exploring vertex algebras**

I’m considering universal V^k(g) as the vacuum Weyl module, which has singular vectors for specific k values. However, simple quotient L_k(g) removes these singular vectors. Wait—universal vertex algebra isn’t simple. Does it have a PBW basis? Yes, it’s induced from the vacuum representation, making it a module over U(g[t^{-1}]t^{-1}). There are singular vectors at special levels as submodules, but the module does contain highest weight vectors generated by negative modes that meet the conditions for positive mode annihilation.
exec
/bin/zsh -lc "rg -n \"dim\\(\\fg\\)\\+2|\\dim\\(\\\\fg\\)\\+2|total dimension.*dim\\(\\\\fg\\)|total dimension.*N\\"'^2 - 1|1 '"\\+ 3 \\+ 1 = 5|dim\\s*\\ChirHoch\\"'^'"\\*.*5|ChirHoch\\"'^1'"\\(V_k\\(\\\\fg\\)\\).*fg\" chapters/theory chapters/examples chapters/connections" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '3658,3692p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '2098,2155p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '1238,1254p;3453,3467p'" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:dim\(\fg\)\+2|\dim\(\fg\)\+2|total dimension.*dim\(\fg\)|total dimension.*N\^2 - 1|1 \+ 3 \+ 1 = 5|dim\s*\ChirHoch\^\*.*5|ChirHoch\^1\(V_k\(\fg\)\).*fg)
                                                                                                                ^^
error: unrecognized escape sequence
 succeeded in 50ms:
  3658	\medskip
  3659	\noindent
  3660	\textbf{The underlying graded vector space.}
  3661	By Proposition~\ref{prop:e3-structure} and the chiral
  3662	Hochschild computation of
  3663	Example~\ref{ex:km}, the derived chiral centre of
  3664	$V_k(\mathfrak{sl}_2)$ at generic level
  3665	$k \neq -2$ is the graded vector space
  3666	\begin{equation}\label{eq:e3-graded-space}
  3667	  Z^{\mathrm{der}}_{\mathrm{ch}}(V_k(\mathfrak{sl}_2))
  3668	  \;=\;
  3669	  \underbrace{\CC}_{=\, \HH^0}
  3670	  \;\oplus\;
  3671	  \underbrace{\mathfrak{sl}_2[-1]}_{=\, \HH^1}
  3672	  \;\oplus\;
  3673	  \underbrace{\CC[-2]}_{=\, \HH^2},
  3674	\end{equation}
  3675	with total dimension $1 + 3 + 1 = 5$. Write $\mathbf{1}$
  3676	for the generator of $\HH^0 = \CC$ (the vacuum),
  3677	$\{e, f, h\}$ for the standard basis of
 succeeded in 51ms:
  2098	[D_e,\, D_f] &= D_h, \label{eq:gerst-ef}\\
  2099	[D_h,\, D_e] &= 2\,D_e, \label{eq:gerst-he}\\
  2100	[D_h,\, D_f] &= -2\,D_f, \label{eq:gerst-hf}
  2101	\end{align}
  2102	where $D_X \in \ChirHoch^1(V_k(\mathfrak{sl}_2)) \cong
  2103	\mathfrak{sl}_2$
  2104	\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
  2105	is the outer derivation parametrized by $X \in \mathfrak{sl}_2$.
  2106	More generally, for any simple~$\fg$ at generic level:
  2107	\[
  2108	[D_X,\, D_Y] \;=\; D_{[X,Y]_{\fg}}
  2109	\qquad
  2110	\text{for all } X, Y \in \fg \cong \ChirHoch^1(V_k(\fg)).
  2111	\]
  2112	In particular, the Gerstenhaber bracket on~$\ChirHoch^1$ is
  2113	independent of the level~$k$.
  2114	\end{proposition}
  2115	
  2116	\begin{proof}
  2117	We compute the bracket from the chiral brace product on the
 succeeded in 52ms:
  1238	degrees $\{0,1,2\}$ with an explicit Hilbert polynomial
  1239	$P_\cA(t)=\sum_n\dim\,\operatorname{ChirHoch}^n(\cA)\cdot t^n$
  1240	determined by the family: $P_{V_k(\fg)}(t)=1+(\dim\fg)\,t+t^2$
  1241	for affine Kac--Moody at generic level,
  1242	$P_{\cH_k}(t)=1+t+t^2$ for Heisenberg,
  1243	$P_{\mathrm{Vir}_c}(t)=1+t^2$ for Virasoro.
  1244	The degree-$1$ group recovers the classical Lie algebra:
  1245	$\operatorname{ChirHoch}^1(V_k(\fg))\cong\fg$
  1246	(Proposition~\ref{prop:chirhoch1-affine-km}).
  1247	The degree-$2$ group is one-dimensional, generated by the
  1248	level deformation $k\mapsto k+\epsilon$.
  1249	This is the deformation ring of~$\cA$ at generic level, and the
  1250	concentration is Koszul-functorial. At critical level $k=-h^\vee$ the bound fails
  1251	(the Feigin--Frenkel centre is infinite-dimensional), so the
  1252	concentration statement is conditional on staying away from the
  1253	critical locus.
  1254	\medskip
  3453	
  3454	The Hilbert polynomial $P_\cA(t) = \sum_n \dim\,\mathrm{ChirHoch}^n(\cA)\cdot t^n$
  3455	is an explicit invariant of each family.

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\\\"'^0 = '"\\\\bC\" -n chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

thinking
**Running corrected regex**

Okay, the failed regex isn't critical, which is a relief. I think we have sufficient information for now. It might be a good idea to run the corrected regex for "dim(g)+2" mentions just to ensure everything's aligned. I’m making a note to tackle that to confirm accuracy as we move forward. It's always better to double-check! I’ll stay focused on getting this right for the best outcome.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "center" chapters/theory/chiral_center_theorem.tex | head' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
7:\section{The chiral endomorphism operad and the chiral center theorem}
8:\label{sec:chiral-center-theorem}
10:\index{chiral center theorem|textbf}
14:The center of a chiral algebra is too small. For the
16:the ordinary center $Z(\mathrm{Vir}_c)$ is one-dimensional:
20:to the center because the center sees only degree-$0$
28:algebra, and neither the center nor the tangent complex
31:The resolution is the chiral derived center
46:Every bulk action factors uniquely through the derived center.
1296:\index{chiral center theorem|see{Deligne--Tamarkin}}
codex
A second issue has appeared on the propagation surface: several overview passages still package Theorem H as “total dimension at most four,” while later local text says the `sl_2` affine example has total dimension `5` and general affine `V_k(g)` has Hilbert polynomial `1 + (dim g)t + t^2`. That inconsistency needs to be pinned down precisely before it goes into the report.
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '356,370p;674,688p;848,863p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '684,720p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '2069,2084p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'total dimension at most four|dim <= 4|bound~4|bound 4|not~4|1 \\+ 3 \\+ 1 = 5|P_\\{V_k\\(\\\\fg\\)\\}\\(t\\)=1\\+\\(\\\\dim\\\\fg\\)\\\\,t\\+t\\"'^2|P'"\\(t\\)=1\\+\\(\\\\dim\\(\\\\mathfrak\\{g\\}\\)\\)t\\+t\\"'^2|P'"\\(t\\)=1\\+\\\\dim\\(\\\\mathfrak\\{g\\}\\)\\\\,t\\+t\\"'^2'"' chapters/theory chapters/frame chapters/connections chapters/examples" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2069	\begin{remark}[The $\mathfrak{sl}_2$ test and the failure of the
  2070	 na\"{\i}ve dimension bound]
  2071	\label{rem:sl2-chirhoch-dim5}
  2072	At $\fg = \mathfrak{sl}_2$, the proposition gives
  2073	$\dim \ChirHoch^1 = 3$. Combined with the one-dimensional groups
  2074	$\ChirHoch^0 = \bC$ and $\ChirHoch^2 = \bC$ from
  2075	Proposition~\ref{prop:derived-center-explicit}(ii), the total
  2076	dimension of $\ChirHoch^*(V_k(\mathfrak{sl}_2))$ is
  2077	$1 + 3 + 1 = 5$, not~$4$. The older conjectural bound
  2078	$\dim \ChirHoch^*(\cA) \leq 4$ (which holds for the Heisenberg and
  2079	Virasoro algebras) fails at the first non-abelian example.
  2080	The correct uniform statement is Theorem~H: concentration in
  2081	degrees $\{0, 1, 2\}$ with polynomial growth, but no universal bound
  2082	on the total dimension. The dimension of $\ChirHoch^1$ grows with
  2083	$\dim(\fg)$: it is $8$ for $\mathfrak{sl}_3$, $15$ for
  2084	$\mathfrak{sl}_4$, $248$ for type $E_8$.
 succeeded in 51ms:
   356	$\kappa(\cA) + \kappa(\cA^!) = K_\cA$, where $K = 0$ for affine
   357	Kac--Moody and free fields and $K = 13$ for Virasoro
   358	(self-dual at $c = 13$).
   359	Theorem~D identifies $\kappa$
   360	as the one-loop coefficient of the bulk partition
   361	function on the uniform-weight lane; the multi-weight
   362	correction $\delta F_g^{\mathrm{cross}}$ at $g \ge 2$ is a
   363	separate higher-loop contribution.
   364	Theorem~H bounds the bulk state space: at generic level on the
   365	Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
   366	
   367	\medskip\noindent
   368	All five theorems are $\Sigma_n$-coinvariant projections of a single
   369	$E_1$ object.
   370	The ordered bar differential $D_\cA^{\Eone}$ on
   674	 of the boundary-bulk reconstruction.
   675	 On the Koszul locus,
   676	 $\ChirHoch^*(\cA)$ is polynomial and dual
   677	 to $\ChirHoch^*(\cA^!)$, with cohomological amplitude
   678	 $[0, 2]$ and total dimension at most four.
 succeeded in 51ms:
   684	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
   685	\end{remark}
   686	
   687	\begin{theorem}[Polynomial growth of chiral Hochschild cohomology
   688	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
   689	\label{thm:hochschild-polynomial-growth}
   690	\index{Hochschild cohomology!polynomial growth|textbf}
   691	\textup{[Regime: quadratic on the Koszul locus
   692	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   693	
   694	Let $\cA$ be a chiral Koszul algebra on a smooth projective curve~$X$,
   695	and let $\cA^!$ denote its Koszul dual. Then:
   696	\begin{enumerate}[label=\textup{(\alph*)}]
   697	\item \emph{Concentration.}\;
   698	 $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
   699	 The nonvanishing range is $0 \leq n \leq 2$.
   700	
   701	\item \emph{Polynomial growth.}\;
   702	 The Hochschild--Hilbert series
   703	 \[
 succeeded in 51ms:
chapters/frame/preface.tex:1240:determined by the family: $P_{V_k(\fg)}(t)=1+(\dim\fg)\,t+t^2$
chapters/frame/preface.tex:3462:$P_{V_k(\fg)}(t)=1+(\dim\fg)\,t+t^2$;
chapters/theory/en_koszul_duality.tex:2772: degrees $\{0, 1, 2\}$ with total dimension at most four on
chapters/theory/en_koszul_duality.tex:3675:with total dimension $1 + 3 + 1 = 5$. Write $\mathbf{1}$
chapters/theory/introduction.tex:365:Koszul locus, $\ChirHoch^*(\cA)$ has total dimension at most four.
chapters/theory/introduction.tex:678: $[0, 2]$ and total dimension at most four.
chapters/theory/chiral_center_theorem.tex:2077:$1 + 3 + 1 = 5$, not~$4$. The older conjectural bound
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"Z\\(V_k\\(\\\\fg\\\\)\\)\" chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/en_koszul_duality.tex | sed -n '2768,2780p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\begin\\{proof\\}|prop:chirhoch1-affine-km|Generic affine first chiral Hochschild group' metadata/claims.jsonl metadata/dependency_graph.dot chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2768	 of~$\mathrm{HH}^\bullet(A, A)$.
  2769	
  2770	\item \emph{Finite-dimensionality of ChirHoch.}
  2771	 Theorem~H shows $\ChirHoch^*(\cA)$ is concentrated in
  2772	 degrees $\{0, 1, 2\}$ with total dimension at most four on
  2773	 the Koszul locus. This severe rigidity constrains the space
  2774	 of possible closed-sector algebras: any $B$ acting on~$A$
  2775	 must map into a target of dimension at most four, leaving
  2776	 little room for the unit to fail surjectivity.
  2777	\end{enumerate}
  2778	\end{remark}
  2779	
  2780	\begin{remark}[Failure off the Koszul locus]
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:250:\begin{proof}
chapters/theory/chiral_center_theorem.tex:572:\begin{proof}
chapters/theory/chiral_center_theorem.tex:603:\begin{proof}
chapters/theory/chiral_center_theorem.tex:726:\begin{proof}[Proof of \textup{(B1)}: the brace identity]
chapters/theory/chiral_center_theorem.tex:907:\begin{proof}[Proof that $\delta^2 = 0$]
chapters/theory/chiral_center_theorem.tex:991:\begin{proof}[Proof of \textup{(B2)}]
chapters/theory/chiral_center_theorem.tex:1084:\begin{proof}[Proof of \textup{(B3)} and \textup{(B4)}]
chapters/theory/chiral_center_theorem.tex:1357:\begin{proof}[Proof of Theorem~\textup{\ref{thm:chiral-deligne-tamarkin}}]
chapters/theory/chiral_center_theorem.tex:1686:\begin{proof}
chapters/theory/chiral_center_theorem.tex:1723:\begin{proof}
chapters/theory/chiral_center_theorem.tex:1921:\begin{proof}
chapters/theory/chiral_center_theorem.tex:2002:\begin{proposition}[Generic affine first chiral Hochschild group; \ClaimStatusProvedHere]
chapters/theory/chiral_center_theorem.tex:2003:\label{prop:chirhoch1-affine-km}
chapters/theory/chiral_center_theorem.tex:2018:\begin{proof}
chapters/theory/chiral_center_theorem.tex:2104:\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
chapters/theory/chiral_center_theorem.tex:2116:\begin{proof}
chapters/theory/chiral_center_theorem.tex:2232:\textup{(}Proposition~\textup{\ref{prop:chirhoch1-affine-km})}
chapters/theory/chiral_center_theorem.tex:2267:\begin{proof}
chapters/theory/chiral_center_theorem.tex:2310:(Proposition~\ref{prop:chirhoch1-affine-km}), the
chapters/theory/chiral_center_theorem.tex:2424:\begin{proof}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'dim\\\\mathfrak\\\\{g\\\\}\\\\+2' chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:dim\\mathfrak\\{g\\}\\+2)
                       ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n --fixed-strings 'dim(g)+2' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"ChirHoch\\\\"'^0" chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1856: $1 \in \ChirHoch^0$ \textup{(}the vacuum, center of~$\mathfrak{H}_k$\textup{)},
1870: \ChirHoch^0 = \bC, \qquad
1890: $\ChirHoch^0$ becomes infinite-dimensional:
1891: $\ChirHoch^0 = \mathfrak{z}(\widehat{\mathfrak{g}}_{-h^\vee})$,
1899: \ChirHoch^0 = \bC, \qquad
1954:$\ChirHoch^0 = \bC$ (center = vacuum at generic level),
2055:critical-level degeneration of $\ChirHoch^0$ (which would promote
2074:$\ChirHoch^0 = \bC$ and $\ChirHoch^2 = \bC$ from

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1920,1970p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{proof}
\textbf{Part~(i).}
The Heisenberg algebra $\mathfrak{H}_k$ is generated by a single
weight-$1$ field $a(z)$ with OPE $a(z)\, a(w) \sim k/(z-w)^2$.
Since $\mathfrak{H}_k$ is quadratic (only binary OPE), it is
chirally Koszul
(Corollary~\ref{cor:universal-koszul}), and the bar cohomology is
$H^*(B(\mathfrak{H}_k)) = \operatorname{Sym}^{\mathrm{ch}}(V^*[1])$,
concentrated in bar degree~$1$.

The chiral Hochschild cohomology $\ChirHoch^n(\mathfrak{H}_k,
\mathfrak{H}_k)$ for a chirally Koszul algebra with one
weight-$1$ generator is computed by the standard Ext argument:
$\ChirHoch^n = \operatorname{Ext}^n_{\cA\text{-bimod}}(\cA, \cA)$.
For the polynomial vertex algebra on one generator, the bimodule
Ext groups are $\bC$ in degrees $0$, $1$, $2$ and zero thereafter,
by the three-term resolution
$0 \to \cA \otimes V^* \otimes \cA \to \cA \otimes V \otimes \cA
\to \cA \otimes \cA \to \cA \to 0$


thinking
**Outlining detailed response and references**

I’m planning a thorough final answer that points to precise file locations and line numbers for the proposition and its proof, including excerpts about the Koszul resolution and chiral Koszul properties. I’ll also mention duplicated references and remarks about dimension formulas, linking relevant theorems and corollaries with evidence from multiple chapters to clarify the structure and general expectations.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "center = vacuum at generic level" -n' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/lib/derived_center_explicit.py:273:    HH^0 = Z(hat{g}_k) = C (center = vacuum at generic level)
chapters/theory/chiral_center_theorem.tex:1954:$\ChirHoch^0 = \bC$ (center = vacuum at generic level),
compute/lib/theorem_open_closed_rectification_engine.py:303:        Z^0 = 1 (center = vacuum at generic level)
thinking
**Clarifying proof scope**

I'm looking at the proposition's scope, specifically `k != -h∨`, and noticing that it's broader than nearby uses of "generic level." For instance, there's something like `k \notin Q_{\le 0}`. It seems the proof doesn't clarify admissible or nonpositive non-critical levels. I might need to find the line in the introduction or check other theorems to see how they exclude these admissible levels, which feels important for the argument.
thinking
**Investigating the theorem's proof**

I see that the theorem is established with classical references, but it mentions chiral Hochschild and cites some older works, which seems a bit suspicious. It might not be necessary to focus on those in my proof, but I should mention them as a hidden assumption and look for direct evidence. The existence of the theorem appears in `hochschild_cohomology.tex:340-347`. However, the proposition doesn’t cite it, meaning there could be a hidden assumption there. I'll need to check the definitions and related theorems for proof of the Hom complex length.
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '320,380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '336,348p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "prop:bar-resolution-chirhoch|bar-resolution-chirhoch" chapters/theory' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\ChirHoch\\"'^1'"\\(.*\\)=.*0|classifies \\\\emph\\{outer derivations\\}|outer derivations' chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   336	
   337	\subsection{Infinitesimal deformations}
   338	
   339	\begin{theorem}[Deformation classification {\cite{Ger63,Loday98}}; \ClaimStatusProvedElsewhere]\label{thm:deformation-classification}
   340	\begin{enumerate}
   341	\item $\ChirHoch^1(\mathcal{A})$ classifies \emph{outer derivations} $\mathrm{Der}(\mathcal{A})/\mathrm{Inn}(\mathcal{A})$ (not infinitesimal automorphisms, which are all derivations).
   342	\item $\ChirHoch^2(\mathcal{A})$ classifies first-order deformations.
   343	\item $\ChirHoch^3(\mathcal{A})$ contains the primary obstructions to extending deformations.
   344	\item Unobstructed deformations correspond to marginal operators in CFT.
   345	\end{enumerate}
   346	\end{theorem}
   347	
   348	\begin{example}[Marginal deformations of beta-gamma]
 succeeded in 51ms:
   320	\section{Computing cohomology via bar-cobar resolution}
   321	
   322	\subsection{The resolution strategy}
   323	
   324	\begin{theorem}[Hochschild via bar-cobar; \ClaimStatusProvedHere]\label{thm:hochschild-bar-cobar}
   325	\textup{[Regime: quadratic on the Koszul locus
   326	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   327	
   328	For any chiral Koszul algebra $\mathcal{A}$
   329	\textup{(}Definition~\textup{\ref{def:chiral-koszul-pair})},
   330	there is a quasi-isomorphism
   331	\[
   332	C^{\bullet}_{\text{chiral}}(\mathcal{A}) \simeq \text{Hom}_{\text{ChirAlg}}(\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A})), \mathcal{A})
   333	\]
   334	where $\Omega^{\text{ch}}(\overline{B}^{\text{ch}}(\mathcal{A}))$ is the cobar construction of the bar complex.
   335	\end{theorem}
   336	
   337	\begin{proof}
   338	The proof has three steps:
   339	
 succeeded in 51ms:
chapters/theory/chiral_hochschild_koszul.tex:737:The derived chiral Hochschild complex $\mathrm{RHH}_{\mathrm{ch}}(A)$ is computed by the algebraic cochain complex $C^*_{\mathrm{ch}}(A, A)$ of Definition~\ref{def:chiral-hochschild-cochain-brace} (\texttt{chiral\_center\_theorem.tex}), which in turn is identified with $\mathrm{RHom}_{\mathsf{ChirAlg}}(A, A)$ via the bar resolution (Proposition~\ref{prop:bar-resolution-chirhoch}).
 succeeded in 51ms:
chapters/theory/chiral_center_theorem.tex:1879: The three-dimensional $\ChirHoch^1$ consists of the outer derivations
chapters/theory/chiral_center_theorem.tex:1955:$\ChirHoch^1 \cong V = \mathfrak{sl}_2$ (outer derivations: the space of
chapters/theory/chiral_center_theorem.tex:2210:$\mathrm{DS}_*$ kills all three outer derivations of
chapters/theory/chiral_center_theorem.tex:2229:is zero.  Concretely, the three outer derivations
chapters/theory/chiral_center_theorem.tex:2345:The $N^2 - 1$ outer derivations decompose into three strata:
chapters/theory/hochschild_cohomology.tex:70:For an associative algebra $A$ over $\mathbb{C}$ and an $A$-bimodule~$M$, the Hochschild cohomology $HH^*(A, M) = \mathrm{Ext}^*_{A^e}(A, M)$ classifies the deformation theory of~$A$: $HH^0$ is the center, $HH^1$ classifies outer derivations, $HH^2$ classifies first-order deformations, and $HH^3$ contains the obstructions to extending them. The full structure is computed by the bar resolution $\cdots \to A^{\otimes(n+2)} \xrightarrow{b} A^{\otimes(n+1)} \to \cdots$ with differential $b(a_0 \otimes \cdots \otimes a_{n+1}) = \sum_{i=0}^n (-1)^i a_0 \otimes \cdots \otimes a_ia_{i+1} \otimes \cdots \otimes a_{n+1}$, and the resulting cohomology carries a Gerstenhaber bracket governing the Maurer--Cartan equation for formal deformations (Gerstenhaber~\cite{Ger63}).
chapters/theory/hochschild_cohomology.tex:101:0 & n = 1 \text{ (no outer derivations at generic $c$)}, \\
chapters/theory/hochschild_cohomology.tex:243:and hence no outer derivations.
chapters/theory/hochschild_cohomology.tex:321:$\ChirHoch^1 = 0$ (no outer derivations), $\ChirHoch^2 = \bC$
chapters/theory/hochschild_cohomology.tex:341:\item $\ChirHoch^1(\mathcal{A})$ classifies \emph{outer derivations} $\mathrm{Der}(\mathcal{A})/\mathrm{Inn}(\mathcal{A})$ (not infinitesimal automorphisms, which are all derivations).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_center_theorem.tex | sed -n '1930,1970p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1930	
  1931	The chiral Hochschild cohomology $\ChirHoch^n(\mathfrak{H}_k,
  1932	\mathfrak{H}_k)$ for a chirally Koszul algebra with one
  1933	weight-$1$ generator is computed by the standard Ext argument:
  1934	$\ChirHoch^n = \operatorname{Ext}^n_{\cA\text{-bimod}}(\cA, \cA)$.
  1935	For the polynomial vertex algebra on one generator, the bimodule
  1936	Ext groups are $\bC$ in degrees $0$, $1$, $2$ and zero thereafter,
  1937	by the three-term resolution
  1938	$0 \to \cA \otimes V^* \otimes \cA \to \cA \otimes V \otimes \cA
  1939	\to \cA \otimes \cA \to \cA \to 0$
  1940	(the Koszul resolution of the diagonal bimodule).
  1941	The weight-$0$ concentration follows from the fact that the
  1942	generating space $V = \bC\cdot a$ is one-dimensional: all
  1943	cocycles are scalar multiples of the identity, level, and
  1944	obstruction cocycles.
  1945	
  1946	\textbf{Part~(ii).}
  1947	Affine $\widehat{\mathfrak{sl}}_{2,k}$ is generated by three
  1948	weight-$1$ fields $J^a$ ($a = +, -, 0$) with OPE
  1949	$J^a(z)\, J^b(w) \sim k\,\delta^{ab}/(z-w)^2 +
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "center = vacuum" chapters/theory/chiral_center_theorem.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1954:$\ChirHoch^0 = \bC$ (center = vacuum at generic level),
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "center" chapters/theory/chiral_koszul_pairs.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1896:\begin{center}
1915:\end{center}
2424:\begin{center}
2456:\end{center}
2854:\centering
3031:\begin{center}
3044:\end{center}
3074:\begin{center}
3087:\end{center}
4622:\centering
4702:\centering
5052:\begin{center}
5061:\end{center}
5099:center~$Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A})$ is the
5737:\begin{center}
5749:\end{center}
5918: (Theorem~\ref{thm:fiber-center-identification}).
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'Z\\(V_k' -n" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/audit/overclaims_from_first_principles.md:17:- HH^*(V_k(g), V_k(g)) → Z(V_k(g)-mod) (Keller's identification, requires compact generation)
compute/audit/overclaims_from_first_principles.md:18:- Z(V_k(g)-mod) → Verlinde ring (at integrable levels, the module category is semisimple)
compute/tests/test_theorem_linshaw_rigidity_engine.py:193:        """For V_k(g), ChirHoch^2 = C = dim Z(V_k^!).
compute/tests/test_theorem_linshaw_rigidity_engine.py:200:            # ChirHoch^2(V_k) should equal dim Z(V_k^!)
compute/tests/test_theorem_linshaw_rigidity_engine.py:202:            assert v.dim_H2 == 1, "Z(V_k!) = C => ChirHoch^2 = C"
compute/tests/test_theorem_linshaw_rigidity_engine.py:523:        For V_k (universal): Z(V_k!) = C (level direction) => ChirHoch^2 = C.
compute/tests/test_level_rank_complementarity.py:4:  Q_g(V_k(g)) + Q_g(V_{-k-2h^vee}(g)) = H*(M_bar_g, Z(V_k(g)))
compute/tests/test_level_rank_complementarity.py:385:    """H*(M_bar_g, Z(V_k(g))) factorization tests."""
compute/lib/theorem_linshaw_rigidity_engine.py:867:            'and rigidity. For UNIVERSAL algebras V_k, the center Z(V_k!) is '
compute/lib/level_rank_complementarity.py:7:  Q_g(V_k(g)) + Q_g(V_{-k-2h^vee}(g)) = H*(M_bar_g, Z(V_k(g)))
compute/lib/level_rank_complementarity.py:437:    """Dimension of the Zhu algebra Z(V_k(g)) at positive integer level.
compute/lib/level_rank_complementarity.py:440:      Z(V_k(g)) = direct sum of End(L_lambda) over integrable L_lambda
compute/lib/level_rank_complementarity.py:447:    For the CENTER Z(V_k(g)) (used in complementarity):
compute/lib/level_rank_complementarity.py:454:    """Check that H*(M_bar_g, Z(V_k(g))) has the expected dimension.
compute/lib/level_rank_complementarity.py:457:    - Z(V_k(g)) is a direct sum of copies of C (one per integrable rep)
compute/lib/level_rank_complementarity.py:463:      Q_g(V_k) + Q_g(V_{-k-2h^vee}) = H*(M_bar_g, Z(V_k))
compute/lib/level_rank_complementarity.py:468:        # At generic level, Z(V_k(g)) = C (one-dimensional center)
compute/lib/oper_from_bar.py:620:    The center Z(V_k(g)) at critical level k = -h^v is:
compute/lib/oper_from_bar.py:1264:    The center Z(V_k(g)) at critical level k = -h^v is:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1,80p' chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
%% ============================================================
%% CHIRAL CENTER THEOREM
%% Object M3 in the programme
%% Self-contained module: definitions, brace algebra, Deligne--Tamarkin
%% ============================================================

\section{The chiral endomorphism operad and the chiral center theorem}
\label{sec:chiral-center-theorem}

\index{chiral center theorem|textbf}
\index{brace algebra!chiral|textbf}
\index{Deligne--Tamarkin!chiral|textbf}

The center of a chiral algebra is too small. For the
Virasoro algebra $\mathrm{Vir}_c$ at generic central charge,
the ordinary center $Z(\mathrm{Vir}_c)$ is one-dimensional:
it contains only the vacuum. Yet the algebra \emph{has}
deformations: the central charge itself can be varied,
$c \mapsto c + \epsilon$. This deformation is invisible
to the center because the center sees only degree-$0$
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'vacuum Verma' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:3794:Virasoro vacuum Verma module has a two-dimensional basis
chapters/examples/n2_superconformal.tex:296:vacuum Verma module at generic level).
chapters/examples/kac_moody.tex:3062:irreducible: for the vacuum Verma module $\mathcal{M}(0)$, the
chapters/examples/kac_moody.tex:3810:coprime, the vacuum Verma module develops singular vectors in the
chapters/examples/level1_bridge.tex:110:(no null vectors in the vacuum Verma module), so
chapters/theory/chiral_modules.tex:3385:sends the vacuum Verma to a cofree comodule that, after the graded-dual
chapters/theory/chiral_modules.tex:3387:\cong \widehat{\mathfrak{sl}}_{2,-k-4}$, becomes the vacuum Verma at
chapters/theory/chiral_modules.tex:3422:The vacuum Verma module is the \emph{free} module on the vacuum
chapters/theory/chiral_modules.tex:3432:More precisely: the bar construction of the vacuum Verma is
chapters/theory/chiral_modules.tex:3454:At conformal weight $h = 1$, the vacuum Verma
chapters/theory/chiral_modules.tex:3539:\begin{proposition}[Non-vacuum Verma modules under the module bar functor on the finite-type \texorpdfstring{$\Eone$}{E1} lane; \ClaimStatusProvedHere]
chapters/theory/chiral_modules.tex:3541:\index{module Koszul duality!non-vacuum Verma}
chapters/theory/chiral_modules.tex:4790:For a non-vacuum Verma module $\mathcal{M}(\lambda)_k$
chapters/theory/chiral_koszul_pairs.tex:1349: since the vacuum Verma module is freely strongly generated.
chapters/theory/computational_methods.tex:851:Basis of the weight-$4$ vacuum Verma module:
chapters/connections/outlook.tex:439:vacuum Verma module acquires a singular vector at
chapters/connections/thqg_holographic_reconstruction.tex:1146:in the Virasoro vacuum Verma module is the
chapters/connections/thqg_holographic_reconstruction.tex:1160:each factor is a state in the vacuum Verma module at
chapters/connections/thqg_holographic_reconstruction.tex:1203:vacuum Verma module is
chapters/connections/thqg_holographic_reconstruction.tex:1939:At conformal weight~$6$, the Virasoro vacuum Verma module
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'generic level' chapters/examples/kac_moody.tex | head" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
40:$\widehat{\fg}_k$ at generic level
106:Kac--Moody algebra at generic level $k \neq -h^\vee$ is
131:($r_{\max} = 4$). At generic level $k \neq -h^\vee$, the
165:For $\widehat{\mathfrak{g}}_k$ at generic level, the shadow
943:rise to two spectral sequences for each generic level~$k$:
997:generic level equal those at every other generic level.
1047:at generic level~$k$ carries a natural
1759:tower at generic levels (convergent only for
3045:(Theorem~\ref{thm:weyl-kac-geometric}) to non-generic level.
3055:is the affine Weyl group. At generic level, all Verma modules
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'singular vector' chapters/examples/kac_moody.tex | head" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3073:Each vanishing produces a singular vector in $\mathcal{M}(w \cdot 0)$,
3079:These singular vector embeddings are precisely the $d_1$
3081:non-degenerate admissible level, the singular vectors organize
3123:$d_1$ & $0$ (Verma modules irreducible) & $\neq 0$ (singular vectors) \\
3502:admissible subcategory because the singular vectors in
3810:coprime, the vacuum Verma module develops singular vectors in the

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1690,1750p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
bar-relevant range begins at conformal weight~$2$
(bar degree~$\geq 2$), so this singular vector at weight~$4$
lies squarely in the bar-relevant range.

\emph{Effect on the bar complex.}
Passing to the simple quotient $L_{-1/2}(\mathfrak{sl}_2)$ kills
this singular vector, introducing an extra relation not present at
generic level. In the bar complex
$\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2))$,
this relation produces bar cohomology off the Koszul diagonal:
at generic level $k$, the Koszul property concentrates
$H^n(\bar{B}^{\mathrm{ch}}(V_k(\mathfrak{sl}_2)))$ in internal
degree~$n$ (the ``Koszul diagonal''), whereas at $k = -1/2$ the
null vector at weight~$4$ generates an off-diagonal class that
persists in $H^\bullet(\bar{B}^{\mathrm{ch}})$.

\emph{Spectral sequence non-collapse.}
The bar-cobar spectral sequence of
Theorem~\ref{thm:bar-cobar-inversion-qi}(4)
(Theorem~\ref{thm:spectral-sequence-collapse}) relies on
thinking
**Analyzing mathematical contradictions**

I'm noticing that examples often exclude admissibility due to ambiguity or inconsistent conventions. I should reference specific file lines, like potentially using line 2435, and I need to focus on the generic level along with the Kac-Shap criterion. I see a contradiction concerning total dimension on the Koszul locus. Theorems indicate a maximum dimension of four, yet another theorem suggests it could be five, which creates a severe conflict. The user is asking whether this relates to amplitude or dimension.
thinking
**Tracking claims and surfaces**

I might need to keep track of the unique file or claim surfaces I've inspected. I've read at least 11 files and many loci, but perhaps "instances checked" should refer to the explicitly checked claims or surfaces. I could count unique theorem or claim surfaces relevant to my work, which seems to add up to 15. I'll note: Instances checked: 15 | Violations found: 4. It might help to mention that this count includes theorem, proof, and summary metadata.
collab wait(call_WW8ePEgc6VJYF6n5Jt40lCU5)
  receivers: 019d8393-b473-7780-b1dd-dc6851035a6f, 019d8393-c5b0-7723-b611-2e80f19bd76e
wait(call_WW8ePEgc6VJYF6n5Jt40lCU5) 1 agents complete:
  019d8393-c5b0-7723-b611-2e80f19bd76e completed: "**Claim Audit**
- `chapters/theory/chiral_center_theorem.tex:2008-2075` proves `\ChirHoch^1(V_k(\fg)) ≅ \fg` at generic …"
collab wait(call_PxLenSqbEdN65TKIX7rqpBHQ)
  receivers: 019d8393-b473-7780-b1dd-dc6851035a6f
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n 'ChirHoch\\\\"'^'"\\*.*total' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n -U 'dim\\(\\\\fg\\).+\\+.+2' chapters" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:1155:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$
chapters/examples/w_algebras_deep.tex:2142: $\kappa^{\mathrm{KM}} = \dim(\fg)(k + h^\vee)/(2h^\vee)$
chapters/examples/kac_moody.tex:86: $\dim(\fg)(k{+}h^\vee)/(2h^\vee)$ \\
chapters/examples/kac_moody.tex:1309:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k + h^\vee)/(2h^\vee)$
chapters/examples/kac_moody.tex:1318:$\kappa' = \dim(\fg)(-k - 2h^\vee + h^\vee)/(2h^\vee)
chapters/examples/kac_moody.tex:1319:= -\dim(\fg)(k + h^\vee)/(2h^\vee) = -\kappa$.
chapters/examples/kac_moody.tex:1343:\dim(\fg)(k + h^\vee)/(2h^\vee)$
chapters/examples/kac_moody.tex:1366:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k+h^\vee)/(2h^\vee)$]
chapters/examples/kac_moody.tex:4554:gives $\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$.
chapters/examples/kac_moody.tex:5367:$\kappa = \dim(\fg)(k+h^\vee)/(2h^\vee)$:
chapters/examples/kac_moody.tex:5377:by~$\kappa = \dim(\fg)(k+h^\vee)/(2h^\vee)$.
chapters/examples/kac_moody.tex:5456:formula $\kappa = \dim(\fg)(k+h^\vee)/(2h^\vee)$. The Coxeter
chapters/examples/kac_moody.tex:5735:\;=\; \frac{\dim(\fg)(1 + h^\vee)}{2h^\vee}
chapters/examples/level1_bridge.tex:152:= \frac{\dim(\fg)\,(k + h^\vee)}{2h^\vee}.
chapters/examples/level1_bridge.tex:216:and not $\dim(\fg)(1+h^\vee)/(2h^\vee)$. The generic-level
chapters/examples/level1_bridge.tex:249:$\kappa^{\mathrm{KM}} = \dim(\fg)(k+h^\vee)/(2h^\vee)$
chapters/examples/level1_bridge.tex:466:$\kappa = \dim(\fg)(1+h^\vee)/(2h^\vee)$ is the full
chapters/examples/yangians_drinfeld_kohno.tex:7480:$\kappa = \kappa(\hat\fg_k) = \dim(\fg) \cdot (k + h^\vee)/(2h^\vee)$
chapters/examples/yangians_drinfeld_kohno.tex:7549:modular characteristic $\kappa = \dim(\fg)(k+h^\vee)/(2h^\vee)$ to
chapters/frame/preface.tex:2785:$\kappa(\widehat{\fg}_k) = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$.
wait(call_PxLenSqbEdN65TKIX7rqpBHQ) timed out:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '90,130p' chapters/examples/kac_moody.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$r$-matrix $r(z)$ & $\Omega/\bigl((k{+}h^\vee)\,z\bigr)$ (Casimir, KZ normalisation, Comp.~\ref{comp:sl2-collision-residue-kz}) \\
Koszul dual & $\mathrm{CE}^{\mathrm{ch}}(\widehat{\fg}_{-k-2h^\vee})$
 (sharing $\kappa$ with $\widehat{\fg}_{-k-2h^\vee}$) \\
Complementarity & $\kappa + \kappa' = 0$ (affine KM) \\
Critical level & $k = -h^\vee$: uncurved,
 FF center \\
$L_\infty$-formality &
 Strictly formal
 (Thm~\ref{thm:km-strictification}) \\
\bottomrule
\end{tabular}
\end{table}

\noindent
The modular Koszul triple
(Definition~\ref{def:modular-koszul-triple}) of the affine
Kac--Moody algebra at generic level $k \neq -h^\vee$ is
\begin{equation}\label{eq:km-triple}
\mathfrak{T}_{\widehat{\fg}_k}
\;=\;

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '680,730p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   680	\begin{remark}[Proof infrastructure]
   681	Both proofs use the bar-cobar quasi-isomorphism at all genera
   682	(Theorem~\ref{thm:higher-genus-inversion}) and the Kodaira--Spencer map
   683	for Koszul pairs
   684	(Theorem~\ref{thm:kodaira-spencer-chiral-complete}).
   685	\end{remark}
   686	
   687	\begin{theorem}[Polynomial growth of chiral Hochschild cohomology
   688	\textup{(}Theorem~H, growth clause\textup{)}; \ClaimStatusProvedHere]
   689	\label{thm:hochschild-polynomial-growth}
   690	\index{Hochschild cohomology!polynomial growth|textbf}
   691	\textup{[Regime: quadratic on the Koszul locus
   692	\textup{(}Convention~\textup{\ref{conv:regime-tags})}.]}
   693	
   694	Let $\cA$ be a chiral Koszul algebra on a smooth projective curve~$X$,
   695	and let $\cA^!$ denote its Koszul dual. Then:
   696	\begin{enumerate}[label=\textup{(\alph*)}]
   697	\item \emph{Concentration.}\;
   698	 $\ChirHoch^n(\cA) = 0$ for $n < 0$ and $n > 2$.
   699	 The nonvanishing range is $0 \leq n \leq 2$.
thinking
**Evaluating proof references**

This is important because that paragraph talks about the algebraic cochain complex being identified through derived RHom via bar resolution, which is relevant to the proof infrastructure. I should check if the reference is unresolved, which seems likely. The severity could be medium. There may also be another missed reference regarding `Theorem\ref{thm:hochschild-bar-cobar}` and `Theorem\ref{thm:bar-concentration}`. Additionally, there's a metadata drift where the wrong file line is recorded. However, since the user is focusing on the mathematical proof, I wonder if all of this detail is necessary.
thinking
**Considering proposition details**

I might mention that the proposition is the first local statement of the claim and that its proof faces the same issue from lines 1947 to 1961. This could add clarity and context to the discussion, helping anyone reviewing the proof understand potential problems in those specific lines. It seems essential to highlight any inconsistencies or gaps, especially where they impact the overall understanding of the proposition and its proof.
exec
/bin/zsh -lc "rg -n '\\\\label\\{prop:bar-resolution-chirhoch\\}|prop:bar-resolution-chirhoch' ." in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./audit_campaign_20260412_231034/T07_thm_H.md:11:- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:737` — The theorem-H package cites `Prop.~\ref{prop:bar-resolution-chirhoch}` immediately after the theorem statement, but repo-wide search finds no such label. A named dependency used to source the `RHH_{\mathrm{ch}}(A)\simeq \mathrm{RHom}_{\mathsf{ChirAlg}}(A,A)` identification is missing.
./audit_campaign_20260412_231034/T07_thm_H.md:1192:/bin/zsh -lc "rg -n \"def:bigraded-hochschild|ChirHoch\\"'^'"\\*\\(|RHH_ch|RHom|Ext\\"'^n_'"\\{\\\\mathrm\\{ChirAlg\\}\\}|Definition~\\\\ref\\{def:bigraded-hochschild\\}|def:chiral-hochschild-cochain-brace|prop:bar-resolution-chirhoch\" chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/koszul_pair_structure.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
./audit_campaign_20260412_231034/T07_thm_H.md:1197:    (?:def:bigraded-hochschild|ChirHoch\^\*\(|RHH_ch|RHom|Ext\^n_\{\mathrm\{ChirAlg\}\}|Definition~\ref\{def:bigraded-hochschild\}|def:chiral-hochschild-cochain-brace|prop:bar-resolution-chirhoch)
./audit_campaign_20260412_231034/T07_thm_H.md:2295:I want to be careful not to make claims unsupported by the entire repository, especially regarding the proposition bar-resolution-chirhoch. I realize I haven't read it yet. The user asked for each step of the proof and its direct dependencies. Maybe I should inspect `prop:bar-resolution-chirhoch` closely. I need to search and see if it discusses the actual complex `C^*_ch(A,A)` computed by bar resolution across degrees 0 to 2. It's better to be thorough to avoid any false positives.
./audit_campaign_20260412_231034/T07_thm_H.md:2300:/bin/zsh -lc 'rg -n "prop:bar-resolution-chirhoch|bar resolution.*chirhoch|chiral-hochschild-cochain-brace" chapters/theory/chiral_center_theorem.tex chapters/theory/*.tex' in /Users/raeez/chiral-bar-cobarexec
./audit_campaign_20260412_231034/T07_thm_H.md:2327:chapters/theory/chiral_hochschild_koszul.tex:737:The derived chiral Hochschild complex $\mathrm{RHH}_{\mathrm{ch}}(A)$ is computed by the algebraic cochain complex $C^*_{\mathrm{ch}}(A, A)$ of Definition~\ref{def:chiral-hochschild-cochain-brace} (\texttt{chiral\_center\_theorem.tex}), which in turn is identified with $\mathrm{RHom}_{\mathsf{ChirAlg}}(A, A)$ via the bar resolution (Proposition~\ref{prop:bar-resolution-chirhoch}).
./audit_campaign_20260412_231034/T07_thm_H.md:2357:I see that this isn't directly repairing the theorem H proof. I’m thinking I should check `prop:bar-resolution-chirhoch`, which I can't find. Maybe the relevant file continues after 1908 or the proposition comes after that? I need to search for the exact label, but I'm not entirely sure I'd still find it. So, I'll go ahead and do another search to see if I can locate the right information.
./audit_campaign_20260412_231034/T07_thm_H.md:2360:chapters/theory/chiral_hochschild_koszul.tex:737:The derived chiral Hochschild complex $\mathrm{RHH}_{\mathrm{ch}}(A)$ is computed by the algebraic cochain complex $C^*_{\mathrm{ch}}(A, A)$ of Definition~\ref{def:chiral-hochschild-cochain-brace} (\texttt{chiral\_center\_theorem.tex}), which in turn is identified with $\mathrm{RHom}_{\mathsf{ChirAlg}}(A, A)$ via the bar resolution (Proposition~\ref{prop:bar-resolution-chirhoch}).
./audit_campaign_20260412_231034/T07_thm_H.md:2407:- [MEDIUM] `chapters/theory/chiral_hochschild_koszul.tex:737` — The theorem-H package cites `Prop.~\ref{prop:bar-resolution-chirhoch}` immediately after the theorem statement, but repo-wide search finds no such label. A named dependency used to source the `RHH_{\mathrm{ch}}(A)\simeq \mathrm{RHom}_{\mathsf{ChirAlg}}(A,A)` identification is missing.
./chapters/theory/chiral_hochschild_koszul.tex:737:The derived chiral Hochschild complex $\mathrm{RHH}_{\mathrm{ch}}(A)$ is computed by the algebraic cochain complex $C^*_{\mathrm{ch}}(A, A)$ of Definition~\ref{def:chiral-hochschild-cochain-brace} (\texttt{chiral\_center\_theorem.tex}), which in turn is identified with $\mathrm{RHom}_{\mathsf{ChirAlg}}(A, A)$ via the bar resolution (Proposition~\ref{prop:bar-resolution-chirhoch}).

thinking
**Summarizing proof structure and dimension reasoning**

I’m gathering textual evidence and line references to show that for universal vertex algebras \(V_k(\mathfrak{g})\) at generic level, the center is one-dimensional (spanned by the vacuum), the chiral Hochschild 1st cohomology corresponds to \(\mathfrak{g}\), and the dual center is also one-dimensional. This supports the total dimension formula \(\dim(\mathfrak{g}) + 2\) from Theorem H. I’ll include key snippets, path and line citations for the proposition, duplicates in chapters, and the main corollary used in the proof to build a clear, referenced final explanation.
codex
**Main surface**
- `chapters/theory/chiral_center_theorem.tex:2002-2015` states Proposition \ref{prop:chirhoch1-affine-km}: “Let $V_k(\fg)$ be the affine vertex algebra at generic level. Then $\ChirHoch^1(V_k(\fg)) \cong \fg$ as $\fg$-modules, so $\dim \ChirHoch^1(V_k(\fg)) = \dim(\fg)$ and $\dim \ChirHoch^1(V_k(\mathfrak{sl}_N)) = N^2-1$.” 
- The proof lives immediately after (same file, lines 2018‑2067). It explains that $V_k(\fg)$ has quadratic OPEs, is chirally Koszul, and its three-term Koszul resolution $0 \to \cA\otimes\fg^*\otimes\cA \to \cA\otimes\fg\otimes\cA \to \cA\otimes\cA \to \cA \to 0$ leaves only one copy of the adjoint module in degree 1. The construction also notes that the Sugawara/Segal–Shapovalov data remain nondegenerate at generic $k$, so no extra cochains survive.

**Total dimension**
- Theorem H (Theorem \ref{thm:hochschild-polynomial-growth}) in `chapters/theory/chiral_hochschild_koszul.tex:687-718` shows the Hochschild Hilbert series is $P_{\cA}(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)\,t+\dim Z(\cA^!)\,t^2$ and that $\ChirHoch^n(\cA)$ vanishes outside degrees $\{0,1,2\}$. For universal affine algebras $V_k(\fg)$ (Corollary~\ref{cor:universal-koszul}), the only degree‑0 central element is the vacuum, so $\dim Z(V_k(\fg))=1$ and the Koszul dual center is likewise one-dimensional. Together with Proposition \ref{prop:chirhoch1-affine-km}, this yields 
  \[
  \dim \ChirHoch^*(V_k(\fg)) = \underbrace{1}_{\ChirHoch^0} + \underbrace{\dim(\fg)}_{\ChirHoch^1} + \underbrace{1}_{\ChirHoch^2} = \dim(\fg)+2.
  \]

**Duplicated statements in `chapters/`**
- `chapters/theory/introduction.tex:682-688` recounts the same proposition: “For affine Kac–Moody algebras $V_k(\fg)$ at generic level, the degree‑1 group is identified with the Lie algebra: $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition \ref{prop:chirhoch1-affine-km}).”
- `chapters/theory/chiral_hochschild_koszul.tex:4773-4774` (Example discussion) states “For affine Kac–Moody $V_k(\fg)$ at generic level, $\ChirHoch^1(V_k(\fg)) \cong \fg$ (Proposition \ref{prop:chirhoch1-affine-km})” while explaining the surviving outer derivations in families with simple poles.
- `chapters/connections/concordance.tex:64-72` reprises the summary table entry for Theorem H, noting “$\ChirHoch^1(V_k(\fg))\cong\fg$ at generic level (Thms…; Proposition \ref{prop:chirhoch1-affine-km}).”
- `chapters/examples/kac_moody.tex:5215-5224` remarks within Conjecture \ref{conj:sc-deformation-critical} that “$\ChirHoch^1(\widehat{\fg}_{-h^\vee})$ also jumps: at generic level it equals~$\fg$ (Proposition \ref{prop:chirhoch1-affine-km}); at critical level the Beilinson–Drinfeld comparison … gives the infinite-dimensional piece,” so the same affine statement is cited in an application context.

**Direct references cited in the proof**
- `Corollary~\ref{cor:universal-koszul}` (`chapters/theory/chiral_koszul_pairs.tex:1330-1353`) is invoked to assert that $V_k(\fg)$ is chirally Koszul (generic and even critical levels). The text lists the universal vertex algebras—affine $V_k(\fg)$ being the first item—and explains that they are chirally Koszul because their vacuum Verma modules are freely strongly generated, so the bar resolution used in the proof is valid.
Plan update
The theorem surface, proof, supporting infrastructure, and propagation summaries have been checked. I’m on the final re-verification pass, keeping only discrepancies backed by the source lines.
  ✓ Read audit workflow and live status surfaces for the claim
  ✓ Read the exact theorem statement and proof in chapters/ and trace direct dependencies
  ✓ Pressure-test scope boundaries: level k, critical/non-critical behavior, amplitude vs dimension
  ✓ Check downstream summaries and duplicates for inflation or contradiction
  → Re-verify each candidate finding against source lines and prepare final report

thinking
**Inspecting proposition consistency**

I need to check whether the proof of the degree-1 cochain as a g-equivariant map could fit with a reduced complex after the finite resolution. There’s still a gap since no reduction is cited. I wonder if theorem H, related to Hochschild via bar-cobar, might not be sufficient. Maybe there's a proposition regarding the resolution of the diagonal in the bar construction? It could be worth searching for "diagonal bimodule" for more insight.
exec
/bin/zsh -lc "nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '200,214p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'generic level \\(i\\.e\\.,|away from admissible and critical levels|generic level.*Q_\\\\{\\\\leq 0\\\\}|k \\\\notin \\\\mathbb\\{Q\\}_\\{\\\\leq 0\\\\}|k \\+ 3 \\\\notin \\\\mathbb\\{Q\\}_\\{\\\\leq 0\\\\}' chapters/examples/kac_moody.tex chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'diagonal bimodule|Koszul resolution of the diagonal bimodule|A \\otimes \\\\fg\\"'^'"\\* \\\\otimes A|A \\\\otimes V\\"'^'"\\* \\\\otimes A|three-term complex with generating space V = \\\\fg|length-2 resolution' chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   200	
   201	\subsection{W-algebra Hochschild cohomology}
   202	
   203	For W-algebras at generic level, Theorem~H gives concentration in $\{0, 1, 2\}$:
   204	
   205	\begin{theorem}[W-algebra Hochschild cohomology; \ClaimStatusProvedHere]\label{thm:w-algebra-hochschild}
   206	For the principal W-algebra $\Walg^k(\mathfrak{g}) = \Walg^k(\mathfrak{g}, f_{\mathrm{prin}})$ at generic level $k$
   207	(away from admissible and critical levels), the chiral Hochschild cohomology
   208	is concentrated in degrees $\{0, 1, 2\}$:
   209	\[\ChirHoch^n(\Walg^k(\mathfrak{g})) = 0 \quad \text{for } n \notin \{0, 1, 2\}.\]
   210	The nonvanishing degrees are:
   211	\begin{enumerate}[label=\textup{(\roman*)}]
   212	\item $\ChirHoch^0(\Walg^k(\mathfrak{g})) = Z(\Walg^k(\mathfrak{g})) = \mathbb{C}$
   213	 \textup{(}the center at generic~$k$ is one-dimensional\textup{)};
   214	\item $\ChirHoch^1(\Walg^k(\mathfrak{g})) = 0$ at generic~$k$
 exited 2 in 52ms:
rg: regex parse error:
    (?:diagonal bimodule|Koszul resolution of the diagonal bimodule|A \otimes \\fg\^\* \\otimes A|A \\otimes V\^\* \\otimes A|three-term complex with generating space V = \\fg|length-2 resolution)
                                                                      ^^
error: unrecognized escape sequence
 exited 2 in 52ms:
rg: regex parse error:
    (?:generic level \(i\.e\.,|away from admissible and critical levels|generic level.*Q_\\{\\leq 0\\}|k \\notin \\mathbb\{Q\}_\{\\leq 0\\}|k \+ 3 \\notin \\mathbb\{Q\}_\{\\leq 0\\})
                                                                                            ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n 'diagonal bimodule|Koszul resolution of the diagonal bimodule|three-term complex with generating space|length-2 resolution' chapters/theory/chiral_center_theorem.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'generic level \\(i\\.e\\.|away from admissible and critical levels|Q_\\{\\\\leq 0\\\\}|Q_\\{<0\\\\}' chapters/examples/kac_moody.tex chapters/theory/hochschild_cohomology.tex chapters/theory/chiral_center_theorem.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/hochschild_cohomology.tex:1033:\begin{corollary}[Identity functor $=$ diagonal bimodule]
chapters/theory/hochschild_cohomology.tex:1038:corresponds to the diagonal bimodule ${}_A A_A$.
chapters/theory/hochschild_cohomology.tex:1045:right multiplication. This is the diagonal bimodule.
chapters/theory/hochschild_cohomology.tex:1103:is the diagonal bimodule. Therefore:
chapters/theory/hochschild_cohomology.tex:1418:diagonal bimodule ${}_A A_A$. Similarly for $\mathcal{F}(U_-)$, where
chapters/theory/chiral_hochschild_koszul.tex:4762:with $\mathcal{B}^! = \mathrm{CE}(\mathfrak{h}_{-k})$ generated by a single element $s\alpha$ in bar degree~1 and its square in bar degree~2. Applying $\mathrm{Hom}_{\mathcal{B}\text{-}\mathcal{B}}(-, \mathcal{B})$ to this length-2 resolution yields a cochain complex concentrated in degrees $0, 1, 2$. Hence $\ChirHoch^n(\mathcal{B}) = 0$ for $n \geq 3$.
chapters/theory/chiral_center_theorem.tex:1940:(the Koszul resolution of the diagonal bimodule).
chapters/theory/chiral_center_theorem.tex:2033:The Koszul resolution of the diagonal bimodule takes the form
chapters/theory/chiral_center_theorem.tex:2041:a three-term complex with generating space $V = \fg$. A degree-$1$
 succeeded in 51ms:
chapters/theory/hochschild_cohomology.tex:207:(away from admissible and critical levels), the chiral Hochschild cohomology

thinking
**Looking for examples**

I need to search for cases where "k not in Q <= 0" appears in earlier examples. It seems we already have line 3764 from a previous large output, which I can cite. It might be helpful to gather the exact lines surrounding that to provide more context. This way, I can ensure I’m being thorough and clear about where this concept appears!
exec
/bin/zsh -lc "nl -ba chapters/examples/kac_moody.tex | sed -n '3760,3768p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  3760	\subsection{Spectral sequence and bar-cobar inversion}
  3761	
  3762	\begin{theorem}[Genus-1 bar-cobar inversion for \texorpdfstring{$\widehat{\mathfrak{sl}}_{2,k}$}{sl-hat_2,k}; \ClaimStatusProvedHere]
  3763	\label{thm:sl2-genus1-inversion}
  3764	For generic level $k$ (i.e., $k \notin \mathbb{Q}_{\leq 0}$, avoiding the admissible levels where null vectors appear), the genus-1 bar-cobar adjunction map:
  3765	\begin{equation}
  3766	\Omega\bigl(\barB^{(1)}(\widehat{\mathfrak{sl}}_{2,k})\bigr) \xrightarrow{\;\sim\;} \widehat{\mathfrak{sl}}_{2,k}
  3767	\end{equation}
  3768	is a quasi-isomorphism. The spectral sequence computing $H^*(\barB^{(1)})$ has:




thinking
**Identifying proof gaps**

I’m listing potential critical findings here. First, in the proof of the chiral center theorem, there’s a significant gap. It misidentifies a degree-1 chiral Hochschild cochain as just a unary map on generators, which isn’t accurate due to the defining complex's all-arities involvement. The claim that `HH^1(V_k(g)) ≅ g` isn't supported by the argument presented. Additionally, the synopsis of theorem-H in the concordance chapter has inconsistencies regarding the Hilbert polynomial and the equivalence statement.
thinking
**Counting inspection details**

I’m reviewing some inspection data and thinking about how to reference lines 2041-2062, even though the file only has 2041. That’s manageable, I suppose! I should check the instances recorded. It might be helpful to count the unique surfaces inspected, which I think is around 15, and it looks like there are 5 violations found. It’s good to keep this organized for clarity!
thinking
**Considering summary structure**

I think it’s essential to have a brief introductory paragraph before the summary, though the user requested an exact severity list followed by the summary. It might be better to incorporate the answer within the findings and summary. I could add a sentence that touches on the source's treatment of dimensions and amplitude. Still, I want to be careful not to violate any agreements. A final summary line could be concise, listing the instances checked and violations found.
thinking
**Clarifying manuscript details**

The manuscript claims \dim(g)+2 as a total dimension, while the proved theorem only discusses amplitude in the range of [0,2] with a polynomial form. This is a high-level point, so I could express it in about two sentences. I should also mention that no exact duplicate of this claim appeared in Vol II or III after the findings. Though the user asked for downstream propagation, maybe I can weave that into the summary without adding extra sections.
codex
[CRITICAL] [chapters/theory/chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2041) — The written proof of `prop:chirhoch1-affine-km` does not actually compute `\ChirHoch^1`. It replaces the full chiral Hochschild complex by a 3-term diagonal-bimodule resolution and treats a degree-1 cochain as just a unary map on generators. But the actual cochain definition in the same file is all-arity, not unary-only: see [definition of `C^\bullet_{\mathrm{ch}}`](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:299). The only general comparison theorem I found, [Hochschild via bar-cobar](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:324), gives `\ChirHoch \simeq \mathrm{Hom}(\Omega^{\mathrm{ch}}\bar B^{\mathrm{ch}}(\cA),\cA)`, not the specific finite resolution used here. So the jump to `\ChirHoch^1(V_k(\fg))\cong\fg` is a proof gap. The same unsupported reduction already appears in the claimed `\widehat{\mathfrak{sl}}_2` base case at [1947](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:1947).

[CRITICAL] [chapters/connections/concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:64) — The official Theorem H synopsis is internally inconsistent. It states `P(t)=1+t^2` and also `\ChirHoch^1(V_k(\fg))\cong\fg` at generic level. Those cannot both hold for any simple `\fg`. The manuscript itself later says generic affine `\widehat{\mathfrak{sl}}_2` has total dimension `1+3+1=5`, not `4`, in [chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2072), and the preface writes `P_{V_k(\fg)}(t)=1+(\dim\fg)t+t^2` in [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:1240) and [preface.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:3454). So the concordance theorem surface is false as written.

[HIGH] [chapters/theory/introduction.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex:675) — The introduction repeats the same contradiction in one paragraph: amplitude `[0,2]` and “total dimension at most four” are stated, then affine generic `\ChirHoch^1(V_k(\fg))\cong\fg` is appended immediately after. The actual theorem-H proof only gives amplitude plus the polynomial formula `P_\cA(t)=\dim Z(\cA)+\dim \ChirHoch^1(\cA)t+\dim Z(\cA^!)t^2`; see [chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:694). So `\dim(\fg)+2` is being used as a total vector-space dimension claim, not as the amplitude bound. The stale “at most four” bound also remains in [en_koszul_duality.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:2771).

[HIGH] [chapters/theory/chiral_center_theorem.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2004) — The proposition’s stated scope and its proof’s hypothesis surface do not match. The statement defines “generic level” as only `k\neq-h^\vee`, but the proof appeals to “Kac--Shapovalov determinant is nonvanishing” and absence of singular vectors at [2051](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex:2051) without citing a theorem that gives exactly that scope. Elsewhere the manuscript uses stricter genericity: [kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:3764) defines generic for `\widehat{\mathfrak{sl}}_2` as `k\notin\mathbb{Q}_{\le 0}`, and [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:205) defines W-algebra genericity as “away from admissible and critical levels.” The nearby Kac--Shapovalov criterion is also framed as the “genuine content” for simple quotients, not the universal affine algebra, at [chiral_koszul_pairs.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex:1418). So the written proof does not justify the exact `k\neq-h^\vee` statement it claims.

[MEDIUM] [chapters/theory/chiral_hochschild_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex:737) — The theorem-H package cites `Proposition~\ref{prop:bar-resolution-chirhoch}` as the bridge from the algebraic cochain complex to `\mathrm{RHom}_{\mathsf{ChirAlg}}(A,A)`, but repo-wide search found no such label definition. That leaves a named proof dependency missing from the Hochschild infrastructure.

The manuscript’s own split is not “all `k`”: it treats the affine claim as generic/non-critical, while critical level is handled separately and becomes unbounded; see [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:150) and [hochschild_cohomology.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/hochschild_cohomology.tex:163). Search output found no exact duplicate of this affine claim in Volumes II or III.

## Summary
Instances checked: 16 | Violations found: 5 | Verdict: FAIL
tokens used
154,229
