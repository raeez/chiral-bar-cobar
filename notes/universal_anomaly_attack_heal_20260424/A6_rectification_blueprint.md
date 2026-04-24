# A6 rectification blueprint: universal anomaly standalone

Worker: A6, synthesis / rectification architect  
Target read-only surface: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex` plus `universal_anomaly_voa_explicit_supplement.tex` and `universal_anomaly_local_global_arithmetic_supplement.tex`  
Only file changed by A6: `notes/universal_anomaly_attack_heal_20260424/A6_rectification_blueprint.md`

## 1. New title and thesis

Proposed title:

```tex
\title[The Atiyah--Connes anomaly]{The Atiyah--Connes anomaly for chiral bar--cobar specialisation}
```

One-line thesis:

> The standalone should prove the existence, Hodge target, and first test cases of a global Atiyah--Connes obstruction class, then state the four-climax comparison as a conditional bridge and the pentagon as a conjectural frontier with named falsifiers.

The current paper contains a real nucleus: a cyclic-Hochschild / Atiyah-class obstruction, denoted
```tex
\alpha_X := [m_3,B^{(2)}]_X,
```
whose natural coherent-cohomology target is
```tex
H^2(X,\Omega^1_X) = H^{1,2}(X)
```
on a smooth projective complex threefold. If the manuscript wants the deformation-space convention, it must say explicitly:
```tex
H^2(X,\Omega^1_X) \cong H^{2,1}(X)^\vee
```
after Calabi--Yau duality / conjugation, not by equality of Hodge summands.

The invalid surface is the proved-here pentagon in `Pr^L_k`: ordinary restriction to a curve cannot close it, because for a smooth curve `C`,
```tex
H^2(C,\Omega^1_C)=0.
```
Thus the displayed map
```tex
H^2(X,\Omega^1_X) -> H^2(C,\Omega^1_C)
```
is the zero map, and cannot be injective unless the source class already vanishes for an independent reason.

## 2. Section architecture

Recommended replacement order:

1. **The Obstruction Class.** Define the cyclic Hochschild operation in its actual ambient: a cyclic / framed-`E_2` enhancement of the Hochschild cochains of a chosen dg enhancement. Construct `\alpha_X` as a global class, not as chart-local data.

2. **The Hodge Target.** Prove the target correction:
   ```tex
   \alpha_X \in H^2(X,\Omega^1_X)=H^{1,2}(X),
   ```
   and state the CY-dual `H^{2,1}` convention only as a dual/conjugate convention.

3. **The Curve Falsifier.** Put the curve cohomology fact before the main theorem:
   ```tex
   H^2(C,\Omega^1_C)=0.
   ```
   This kills the ordinary-restriction return edge. Any surviving bridge must use derived specialization / local cohomology / factorisation homology, not ordinary coherent restriction.

4. **Proved Core.** State only what the paper can honestly prove:
   the class exists in the chosen cyclic-HKR model; its target is corrected; local representatives are not the theorem; the curve restriction is void; the quintic and K3-product computations are evidence/falsifiers after correction.

5. **Compute-backed Evidence.** Keep the hand computations, but split what they prove:
   the quintic Jacobian count `101` and nonzero Yukawa are proved/primary-source backed; the equality of that Yukawa with `\alpha_X` is a comparison hypothesis. For `K3\times E`, the Kunneth target has dimension `21`, so vanishing must be a class calculation, not a dimension count.

6. **Conditional Bridge.** Rebuild the four climax comparisons as assumptions `(B1)--(B4)`:
   Positselski comparison, Costello--Li parametrix comparison, K3/Mukai/Bruinier specialization, derived-centre trace normalization.

7. **Conjectural Frontier.** Move motivic lift, graph weights, Malcev identification, Adler--Bardeen language, Strominger lift, all-loop closure, Verdier-dual decagon, and the five-vertex pentagon here unless another agent supplies a complete proof.

8. **Supplements as Inputs.** Keep the VOA and arithmetic supplements as evidence appendices with a status preface. They should not be cited as proofs of the main theorem unless their own hypotheses are imported.

### Cross-worker integration constraints

A1--A4 reports are compatible with this architecture and should be
merged before TeX repair:

- **A1 controls the cocycle/Hodge convention.** Use A1's corrected
  target and cyclic-chain/cochain warnings before rewriting the nucleus.
  In particular, `B^{(2)}` must be defined in one convention, not used
  simultaneously as ordinary Connes `B`, a higher Connes hierarchy
  operator, and a cochain degree-raising map.
- **A2 controls the common category.** The native object is a diagram
  of derived zero loci / witness sheaves over a base of geometric data,
  not raw equalities in `Pr^L_k`. `QCoh` or `IndCoh` may produce
  `Pr^L_k` objects only after equivalence of those loci is proved.
- **A3 controls the Theorem B edge.** Vanishing of the anomaly class
  can at most kill the first identified bar--cobar obstruction unless
  an independent Koszul/PBW/completed-Positselski collapse hypothesis is
  imported. Do not write "Positselski recursion kills all `obs_n`" as a
  theorem.
- **A4 controls the factorisation/hCS edge.** Real locally constant
  factorisation on a real six-manifold is `E_6`, not `E_3`; a
  holomorphic complex-threefold theory needs its own statement.
  `K3\times\mathbb C^2` is complex dimension four, so it cannot be the
  six-real-dimensional hCS target. Adler--Bardeen is a conditional
  analogy until a local BRST and non-renormalisation theorem is proved
  for the actual holomorphic BV theory.

## 3. Status table

`Preserve` means the surface can remain with the same mathematical role after local wording correction. `Demote` means the current status overclaims. `Split` means one part is proved and another part is conditional/frontier.

| Label / surface | Current status | New status | Action |
|---|---:|---:|---|
| `thm:climax-I` Chiral Positselski | ProvedElsewhere | ProvedElsewhere input | Preserve, but do not make it a consequence of `\alpha_X` without bridge `(B1)`. |
| `thm:climax-II` DVV partition function | ProvedElsewhere | ProvedElsewhere input, BPS-index scope | Preserve only as protected-index identity, not off-shell 3D gravity path integral. |
| `thm:dvv-physics` | ProvedHere | ProvedElsewhere / expository | Demote from theorem or retag as referenced physical dictionary. |
| `thm:dvv-as-boundary` | ProvedHere | Conditional | Demote; requires stage-two specialization and character comparison not proved in this standalone. |
| `thm:climax-III` `\bfH_{\Delta_5}` canonical | ProvedElsewhere | ProvedElsewhere input on its locus | Preserve; do not generalize from K3/Mukai locus to arbitrary CY3. |
| `thm:hdelta5-physics` | ProvedHere | Heuristic / Conditional | Demote; physical interpretation is not a proof of canonicality. |
| `thm:climax-IV` trace identity | Conditional | Conditional bridge | Preserve as bridge `(B4)`, not as proved edge. |
| `thm:three-scale` | ProvedHere | Heuristic / Conditional | Demote; RG-flow language is physical picture. |
| `constr:cocycle` | untagged construction | Proved core after target correction | Preserve as the nucleus, with precise cyclic-Hochschild ambient. |
| `prop:cocycle-rep` | ProvedHere | ProvedHere after repair | Preserve only with target `H^{1,2}` and explicit model dependence. |
| `cor:hodge` | ProvedHere | ProvedHere after correction | Replace `H^{2,1}` equality by `H^{1,2}` or CY-dual convention. |
| `prop:atiyah-cup-derivation` | ProvedHere | Proved core / Conditional details | Split: the Atiyah-Connes target is core; the ten-step source chain needs hypotheses per step. |
| `prop:motivic-lift` | ProvedHere | Conjectural | Demote; canonical higher-Chow representative is not proved. |
| `cor:motivic-vanish` | ProvedHere | Conditional / Conjectural | Demote; depends on motivic lift and injectivity. |
| `prop:wheel-graph` | ProvedHere | Conjectural / Computation pending | Demote; exact weights need independent computation. |
| `thm:formality-atiyah` | ProvedHere | Conditional bridge | Demote; equality with `U^3_{2,X}` is a comparison theorem not proved here. |
| `cor:strict-formality` | ProvedHere | Conjectural | Demote; `U_2=0` does not by itself kill all higher obstruction classes. |
| `thm:connes-motivic` | ProvedHere | Conjectural | Demote; motivic class for Connes `B` is not established. |
| `cor:motivic-rep` | ProvedHere | Conjectural | Demote with motivic lift. |
| `thm:hkr-duflo` | ProvedElsewhere | ProvedElsewhere background | Preserve, but keep the exact cited theorem statement faithful. |
| `prop:cocycle-duflo` | ProvedHere | Conditional | Demote; coefficient and target projection need a proof in the chosen normalization. |
| `cor:universal` | untagged | Conjectural | Add explicit status or remove from theorem lane. |
| `thm:malcev-quillen` | ProvedHere | Conditional / Conjectural | Demote; the configuration-space/Malcev comparison is not established here. |
| `cor:pi1-motivic` | ProvedHere | Conditional | Demote with `thm:malcev-quillen`. |
| `thm:main` | ProvedHere | Replace | Replace by split theorem: proved core + conditional bridge + conjectural pentagon. |
| `thm:adler-bardeen` | ProvedHere | Heuristic / Conditional | Demote; anomaly-matching dictionary is physical bridge, not a proved equality. |
| `prop:quintic-nonvanish` | ProvedHere | Split | Preserve `h^{2,1}=101` and nonzero Yukawa; make exact `\alpha_X` nonvanishing conditional on comparison. |
| `cor:quintic-fails` | ProvedHere | Proved falsifier / Conditional details | Preserve as falsifier of universal CY3 pentagon; do not derive from invalid main theorem. |
| `prop:k3e-vanish` | ProvedHere | Conditional | Demote; `H^2(K3\times E,\Omega^1)` has 21-dimensional Kunneth target. |
| `prop:k3e-kunneth-chain` | ProvedHere | Proved decomposition / Conditional vanishing | Split; correct the missing Kunneth summands before using it. |
| `cor:k3e-locus` | ProvedHere | Conditional | Demote; Humbert-complement locus needs separate proof. |
| `prop:clemens-ddbar` | ProvedElsewhere | ProvedElsewhere input | Preserve. |
| `prop:clemens-explicit` | ProvedHere | Conditional falsifier | Demote; metric-dependence mechanism is plausible but not proved as stated. |
| `cor:strominger` | ProvedElsewhere | ProvedElsewhere framework + conjectural climax lift | Split. |
| `thm:strominger-native` | ProvedHere | Heuristic / Conjectural | Demote. |
| `prop:strata` | Conditional | Conditional taxonomy | Preserve as taxonomy, not theorem proving the bridge. |
| `thm:two-loci` | Conditional | Conditional frontier | Preserve, move after bridge. |
| `prop:heegner` | Conditional | Conditional arithmetic refinement | Preserve with primary-source check by arithmetic agent. |
| `cor:bridgeland` | Conditional | Conditional frontier | Preserve. |
| `cor:m23` | Conditional | Open / Conditional frontier | Preserve as open frontier. |
| `thm:clemens-extension` | Conditional | Conditional frontier | Preserve. |
| `q:all-loop`, `q:unconditional Bridgeland`, `q:M23`, `q:H-twisted` | Open | Open | Preserve. |
| `prop:hand-summary` | ProvedHere | Evidence table | Demote; it summarizes an invalid main theorem. |
| VOA supplement `subsec:voa-H-Delta5-canonical` | implicit | Evidence / ProvedElsewhere inputs | Preserve as appendix evidence, not main proof. |
| VOA supplement `subsec:voa-hbar-K-universal-trace` | implicit | Conditional bridge evidence | Preserve, but fix K3 versus `K3\times E` target. |
| VOA supplement `subsec:voa-theorem-B-bar-cobar` | implicit | Proved examples | Preserve as toy-model computations. |
| VOA supplement `subsec:voa-dvv-symorbifold` | implicit | ProvedElsewhere BPS-index derivation | Preserve with BPS-index scope. |
| VOA supplement `subsec:voa-heegner-arithmetic` | implicit | Conditional arithmetic appendix | Preserve after arithmetic audit. |
| VOA supplement `subsec:voa-koszul-duals` | implicit | Conjectural / Conditional | Demote; the Verdier-dual decagon is frontier. |
| Local-global supplement `subsec:koszul-scope` | implicit | Needs correction | Fix "open complement of zero locus"; vanishing locus is not automatically an open complement. |

## 4. TeX replacement skeleton

### Replacement abstract

```tex
\begin{abstract}
We isolate the obstruction class which survives the current
four-climax comparison.  Let \(X\) be a smooth projective
Calabi--Yau threefold and let \(\cD^b_{\mathrm{dg}}(X)\) be a fixed
dg enhancement.  In the cyclic Hochschild complex of
\(\End^\bullet(T_X)\), the ternary \(A_\infty\)-operation \(m_3\)
and the bidegree-two Connes rotation \(B^{(2)}\) define a global
Atiyah--Connes class
\[
  \alpha_X := [m_3,B^{(2)}]_X \in H^2(X,\Omega^1_X).
\]
In Hodge notation the target is \(H^{1,2}(X)\); the frequently used
\(H^{2,1}(X)\)-language is the Calabi--Yau dual convention, not an
equality of Hodge summands.

The proved core of the paper is the construction of \(\alpha_X\), the
target correction, and the first falsifiers.  For every smooth curve
\(C\), \(H^2(C,\Omega^1_C)=0\), so ordinary restriction
\(H^2(X,\Omega^1_X)\to H^2(C,\Omega^1_C)\) cannot close a pentagon.
The generic quintic has \(h^{1,2}=101\) and non-zero Yukawa coupling,
so any universal K3/Igusa conclusion is false off its admissible
locus.  On \(K3\times E\), the Kunneth target is \(21\)-dimensional;
vanishing is a class calculation, not a dimension count.

The bridges from \(\alpha_X\) to chiral Positselski inversion,
stage-one \(E_3\)-factorisation canonicality, the K3 bialgebra
\(\mathbf H_{\Delta_5}\), and the trace identity
\(\hbar^2K=-1\) are stated with explicit comparison hypotheses.
Under those hypotheses the four vertices form a conditional diagram.
The former five-vertex pentagon is retained as a conjectural frontier,
with the curve-\(H^2\), Hodge-target, quintic, and \(K3\times E\)
tests as its falsifiers.
\end{abstract}
```

### Replacement main theorem skeleton

```tex
\begin{theorem}[Atiyah--Connes obstruction and conditional bridge]
\label{thm:atiyah-connes-bridge}
Let \(X\) be a smooth projective Calabi--Yau threefold over
\(\mathbb C\), equipped with a cyclic dg enhancement of
\(D^b(\Coh X)\).  Let
\[
  \alpha_X := [m_3,B^{(2)}]_X
\]
be the cyclic Hochschild commutator class defined from the ternary
\(A_\infty\)-operation and Connes' bidegree-two rotation.

\begin{enumerate}[label=\textup{(\alph*)}]
\item \textup{(proved core)} The HKR--Atiyah image of \(\alpha_X\)
lies in
\[
  H^2(X,\Omega^1_X)=H^{1,2}(X).
\]
If it is written as an \(H^{2,1}\)-class, this means the
Calabi--Yau-dual or conjugate class.

\item \textup{(curve falsifier)} For a smooth algebraic curve \(C\),
\[
  H^2(C,\Omega^1_C)=0.
\]
Hence no non-zero class in \(H^2(X,\Omega^1_X)\) can be detected by
ordinary restriction to \(H^2(C,\Omega^1_C)\).  Any return edge from a
curve-side trace identity to \(\alpha_X=0\) must factor through a
different receptacle, such as derived specialization, local
cohomology with support near \(C\), or factorisation homology.

\item \textup{(conditional Positselski bridge)} Assume \textup{(B1)}
there is a comparison map
\[
  \operatorname{sp}_{\Sigma,C}\colon H^2(X,\Omega^1_X)\to
  \Ob_{\mathrm{bar\text{-}cobar}}(A_X|_C)
\]
identifying \(\operatorname{sp}_{\Sigma,C}(\alpha_X)\) with the first
non-trivial obstruction to the chiral bar--cobar counit.  Then
\(\alpha_X=0\), together with vanishing of the higher obstruction
classes or an induction reducing them to \(\alpha_X\), implies
\[
  \Omega_C^{\mathrm{ch}}B_C^{\mathrm{ch}}(A_X|_C)\simeq A_X|_C .
\]

\item \textup{(conditional factorisation bridge)} Assume \textup{(B2)}
the Costello--Li parametrix obstruction for \(\Phi^{\mathrm{FA}}_3(X)\)
is identified with \(\alpha_X\) in the same normalization.  Then
\(\alpha_X=0\) implies stage-one canonicality in the stated
factorisation-algebra ambient.

\item \textup{(conditional K3/trace bridge)} Assume \textup{(B3)} the
stage-two specialization lands on the Mukai-admissible K3 locus and
\textup{(B4)} the derived-centre trace is normalized by the
Bruinier--Mukai identity \(K=2c_+(L)\).  Then the K3 vertex
\(\mathbf H_{\Delta_5}\) and the scalar trace identity
\(\hbar^2K=-1\) follow on that locus.
\end{enumerate}

Consequently the four-climax diagram is a theorem only under
\textup{(B1)--(B4)} and the higher-obstruction closure hypothesis.
Without these hypotheses it is a conjectural comparison diagram, not
a commutative pentagon of equalities in \(\mathrm{Pr}^L_k\).
\end{theorem}
```

Optional frontier statement:

```tex
\begin{conjecture}[Five-vertex anomaly pentagon]
\label{conj:atiyah-connes-pentagon}
Under \textup{(B1)--(B4)} and all-loop obstruction closure, the
vanishing of \(\alpha_X\) is equivalent to the four climax statements
on the admissible locus.  The conjecture is false with ordinary curve
restriction in place of \(\operatorname{sp}_{\Sigma,C}\).
\end{conjecture}
```

## 5. Explicit falsifiers to keep in the paper

1. **Curve `H^2` falsifier.**
   ```tex
   H^2(C,\Omega^1_C)=0
   ```
   for every smooth curve. This kills the current return edge.

2. **Hodge-target falsifier.**
   ```tex
   H^2(X,\Omega^1_X)=H^{1,2}(X)
   ```
   not `H^{2,1}(X)`. The dimensions may match on CY3, but the Hodge summands are not the same object.

3. **`K3\times E` Kunneth falsifier.**
   ```tex
   \dim H^2(K3\times E,\Omega^1_{K3\times E})=21.
   ```
   The current dimension-vanishing proof is false. Vanishing, if true, must identify the actual class and show its components vanish.

4. **Generic quintic falsifier.** The Jacobian-ring count gives `101`; the Yukawa coupling is non-zero generically. The universal K3/Igusa output cannot hold on generic quintics.

5. **Strictness falsifier.** Vanishing of a second Taylor coefficient does not imply strict `E_3` formality without killing higher obstruction classes.

## 6. Integration order for the main thread

1. Collect A1--A5 reports and merge by mathematical obligation, not by majority.
2. Replace title and abstract first, because the current title asserts the false conclusion.
3. Replace `thm:main` with `thm:atiyah-connes-bridge` plus `conj:atiyah-connes-pentagon`.
4. Globally correct the Hodge target in the standalone and supplements: `H^2(X,\Omega^1_X)=H^{1,2}(X)`, with `H^{2,1}` only as CY-dual/conjugate.
5. Insert the curve `H^2` falsifier before any theorem using the reference curve.
6. Replace the `Pr^L_k` equality by A2's derived-zero-locus / witness-sheaf formulation; mention `Pr^L_k` only after applying `QCoh` or `IndCoh`.
7. Demote the theorem surfaces in the status table above before repairing prose. This prevents the proof from continuing to cite false proved-here claims.
8. Replace the Theorem B edge by A3's verified Positselski-surface formulation.
9. Replace the factorisation/hCS edge by A4's conditional bridge; correct `E_3`/`E_6` and `K3\times\mathbb C^2` dimension errors.
10. Correct the `K3\times E` Kunneth decomposition. Do not claim vanishing by dimension.
11. Move motivic, graph, Malcev, Adler--Bardeen, Strominger, all-loop, and decagon material to a frontier section unless another worker supplies a proof.
12. Keep the VOA supplement as evidence, with a status preface separating proved toy computations from conditional K3/Mukai and conjectural decagon material.
13. Keep the arithmetic supplement, but correct the Koszul-locus language and keep Chenevier/MGSL material conditional.
14. Run only targeted `rg` checks after edit. Build only at session end on user opt-in, per repo doctrine.

## 7. Files changed

Only this report:

```text
notes/universal_anomaly_attack_heal_20260424/A6_rectification_blueprint.md
```

No target TeX files were edited.

## 8. Commands run

Key commands run by A6:

```bash
sed -n '1,220p' repo-local instructions file
sed -n '221,618p' repo-local instructions file
sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md
sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md
sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md
wc -l repo-local instructions file standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md
sed -n '1,260p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
sed -n '261,620p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
sed -n '621,980p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
sed -n '981,1435p' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
rg -n -e '\\title\\{' -e '\\begin\\{abstract\\}' -e '\\section\\{' -e '\\begin\\{theorem\\}' -e '\\begin\\{proposition\\}' -e 'ClaimStatus' -e 'Hodge' -e 'pentagon' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_voa_explicit_supplement.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex
wc -l standalones/universal_anomaly_voa_explicit_supplement.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex
sed -n '1,220p' standalones/universal_anomaly_voa_explicit_supplement.tex
sed -n '221,520p' standalones/universal_anomaly_voa_explicit_supplement.tex
sed -n '521,820p' standalones/universal_anomaly_voa_explicit_supplement.tex
sed -n '1,130p' standalones/universal_anomaly_local_global_arithmetic_supplement.tex
sed -n '1,140p' archive/raeeznotes/raeeznotes100/red_team_summary.md
rg -n -C 10 'lem:curve-H20-vanishing|H\\^2\\(C, \\\\Omega\\^1_C\\)|H\\^2\\(C,\\\\Omega\\^1_C\\)' chapters appendices standalones metadata/theorem_registry.md
rg -n -C 4 'kernel\\(H\\^2|restriction injectivity|H\\^2\\(X, \\\\Omega\\^1_X\\).*H\\^2\\(C|regular embedding.*C|C \\\\hookrightarrow X' standalones chapters appendices notes metadata -g '!notes/repo_instructions_legacy_20260418.md' -g '!notes/agents_instructions_legacy_20260418.md' -g '!notes/first_principles_cache_comprehensive.md'
ls -la notes/universal_anomaly_attack_heal_20260424
find notes/universal_anomaly_attack_heal_20260424 -maxdepth 1 -type f -print
git status --short notes/universal_anomaly_attack_heal_20260424 standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_voa_explicit_supplement.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A2_pentagon_loci.md
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A3_bar_cobar_positselski.md
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A4_factorization_hcs_adler.md
```

No build or test command was run.
