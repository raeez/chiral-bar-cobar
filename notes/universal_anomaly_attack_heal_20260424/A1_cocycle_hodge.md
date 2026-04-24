# A1 cocycle/Hodge/negative-cyclic attack-heal report

Date: 2026-04-24.

Scope audited:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
- `standalones/universal_anomaly_voa_explicit_supplement.tex`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex`

Write scope respected: only this report was created.

## 1. Claim attacked

The paper claims that the ternary Massey operation and Connes bidegree-two cyclic shift define a proved chain-level cocycle
\[
  [m_3,B^{(2)}]_X=\operatorname{at}_X\cup B^{(2)}_{\mathrm{Connes}}
  \in H^2(X,\Omega_X^1)=H^{2,1}(X),
\]
and that its vanishing is equivalent to the five-vertex pentagon consisting of Theorem B, stage-one canonicity, \(\mathbf H_{\Delta_5}\)-canonicity, and \(\hbar^2K=-1\).

The nucleus is promising, but the proved surface does not survive as written. What survives is a conditional obstruction class targeted at coherent cohomology
\[
  \alpha_X^{\mathrm{cyc}}\in H^2(X,\Omega_X^1)\cong H^{1,2}(X),
\]
or its Serre/conjugate dual after an explicitly chosen Calabi--Yau volume form and polarization. The exact negative-cyclic construction and the comparison with the five climaxes remain proof obligations.

## 2. Findings

### FATAL 1: \(H^2(X,\Omega_X^1)\) is \(H^{1,2}(X)\), not \(H^{2,1}(X)\)

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:92`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:422`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:442`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:448`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:468`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:306`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:729`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:20`

Dolbeault theorem gives \(H^q(X,\Omega_X^p)\cong H^{p,q}(X)\). Hence \(H^2(X,\Omega_X^1)\cong H^{1,2}(X)\). On a Calabi--Yau threefold, \(h^{1,2}=h^{2,1}\), but equality of dimensions is not equality of Hodge summands. Any use of the \(H^{2,1}\) moduli tangent interpretation requires an explicit conjugation, polarization, or Serre-dual identification.

The paper's own line `372` says the chain-level Dolbeault output lies in \(H^{0,2}(X,\Omega_X^1)\), i.e. bidegree \((1,2)\), which confirms the correction.

### FATAL 2: the return edge through the reference curve is impossible as stated

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:687`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:705`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:710`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:726`

Hypothesis (H1) asks for injectivity of
\[
  H^2(X,\Omega_X^1)\to H^2(C,\Omega_C^1).
\]
For a smooth curve \(C\), coherent cohomology vanishes in degrees \(>1\), so \(H^2(C,\Omega_C^1)=0\). Thus (H1) is injective only when the relevant source subspace is already zero. The proof of \((v)\Rightarrow(i)\) is circular under H1 and absent without H1.

The repair is not a status downgrade. The returning edge must be replaced by a nonzero transgression/Gysin/residue target on the normal geometry of \(C\subset X\), or removed from the theorem.

### FATAL 3: Connes \(B\) is used with incompatible chain/cochain degrees, and \(B^{(2)}\) is not separated from the Connes hierarchy

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:167`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:177`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:202`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:394`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:396`
- `chapters/theory/hochschild_cohomology.tex:709`
- `chapters/theory/hochschild_cohomology.tex:712`
- `chapters/theory/hochschild_cohomology.tex:2660`
- `chapters/theory/hochschild_cohomology.tex:2669`
- `notes/first_principles_cache_comprehensive.md:34`
- `notes/first_principles_cache_comprehensive.md:35`
- `notes/cross_volume_aps.md:115`

The local Hochschild chapter states Connes \(B:\mathrm{CH}_n\to\mathrm{CH}_{n+1}\) on chains and the chiral cohomological lift \(\mathrm{ChirHoch}^n\to\mathrm{ChirHoch}^{n-1}\). The standalone instead declares a cochain operator \(B^{(2)}:\HH^2\to\HH^3\), then forms a degree-zero commutator with \(m_3\).

The cache also records a known error: the mixed-complex identity for ordinary \(B^{(0)}\) does not automatically extend to higher \(B^{(j)}\). The paper uses the notation \(B^{(2)}\) as if it were both ordinary Connes \(B\), a bidegree-two component, and an \(S^1\)/framed-\(E_2\) hierarchy operator. The negative-cyclic class \(\HC^{-,2}(\cdots)\) is therefore not defined with stable conventions.

### FATAL 4: the Dolbeault representative does not land in \(\Omega_X^1\) without an unprovided contraction/projection

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:427`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:429`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:431`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:435`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:464`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:467`

The displayed representative is
\[
  \bar\partial\nabla\wedge\bar\partial\nabla\in
  \Omega^{0,2}(X,\Omega_X^1\otimes\Omega_X^1),
\]
before even accounting for the two \(\operatorname{End}(T_X)\) factors. Cyclic-skew projection does not by itself produce a class with coefficients in \(\Omega_X^1\). A trace, contraction with the Calabi--Yau volume, or contraction using the Atiyah tensor must be specified and checked for degree and sign.

The independence-of-connection argument is also too fast. Difference of representatives is not simply killed by saying \(\bar\partial(\nabla-\nabla')\) is exact after wedging and projecting; the induced change of the quadratic expression has cross terms and must be computed in the chosen quotient complex.

### FATAL 5: the motivic/regulator lift is over-strong and presently false as a proved theorem

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:479`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:481`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:487`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:491`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:500`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:565`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:567`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:575`

The asserted canonical motivic lift via a "torsion tensor of the Chern connection" is not available. On a K\"ahler tangent bundle the Chern connection is torsion-free in the relevant sense, so a torsion-graph cycle cannot carry the claimed nonzero obstruction without further structure. The regulator from \(H^3_{\mathcal M}(X,\mathbb Q(2))\) lands in Deligne/intermediate-Jacobian data, not canonically in a single \(H^{2,1}\) summand, and regulator injectivity modulo torsion is not a theorem in this generality.

This whole face should be conjectural or conditional on construction of an algebraic cycle whose regulator is the corrected \(H^{1,2}\) obstruction.

### SERIOUS 1: the quintic non-vanishing argument proves the wrong implication

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:776`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:780`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:789`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1061`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1069`

The Jacobian-ring count \(R_f^{10}=101\) correctly counts \(h^{2,1}(Q_5)\). It does not prove that the corrected target class in \(H^2(Q_5,\Omega^1)=H^{1,2}(Q_5)\) is nonzero. Nonzero Yukawa \(\operatorname{at}^{\cup3}\) also does not imply that the quadratic cyclic-skew projection \([m_3,B^{(2)}]\) is nonzero. A separate map from the cubic Yukawa to the corrected negative-cyclic obstruction is needed.

### SERIOUS 2: the \(K3\times E\) vanishing mechanism is wrong as written

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:797`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:807`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:818`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:821`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1089`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1091`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:306`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:308`

Direct Kunneth count gives
\[
  \dim H^2(K3\times E,\Omega^1)=21,
\]
with nonzero summands \(H^1(K3,\Omega^1)\otimes H^1(E,\mathcal O_E)\) of dimension \(20\) and \(H^2(K3,\mathcal O_{K3})\otimes H^0(E,\Omega^1_E)\) of dimension \(1\). Thus the receptacle does not vanish. Also \(H^3(K3\times E,\Omega^3)\) is not zero on a compact Calabi--Yau threefold.

The possible vanishing of the specific obstruction class may still be true, but it requires an explicit computation of the projected class in these nonzero summands. It cannot be proved by receptacle vanishing.

### SERIOUS 3: Duflo, graph, and Malcev faces are asserted beyond the cited local evidence

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:511`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:515`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:519`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:597`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:606`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:608`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:632`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:634`

The exact coefficients \(1/(2\pi^2)\), \(1/(4\pi^2)\), the identification with the second Duflo coefficient \(1/12\), and the Malcev equality with \(H^3_{\mathcal M}(X,\mathbb Q(2))\) are not derived locally and are too strong as `ProvedHere`. They should be conditional on primary-source verification with conventions, or removed from the proof of the main theorem.

### MODERATE: the algebraic VOA examples live on a different surface

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1103`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1105`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1133`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:386`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:464`

The Heisenberg and \(V_1(\mathfrak{sl}_2)\) computations may be useful reference-curve shadows, but they do not verify the CY-threefold class target. They should be stated as algebraic vanishing tests for the chosen \(m_3/B\) conventions, not as evidence for the Hodge target until the chain/cochain cyclic operator is fixed.

## 3. Corrected theorem surface that survives

Surviving surface:

> Let \(X\) be smooth projective K\"ahler Calabi--Yau of dimension \(3\). Suppose a cyclic Hochschild/negative-cyclic cocycle \(\alpha_X^{\mathrm{cyc}}\) is constructed from the \(A_\infty\) ternary operation and a precisely specified cohomological cyclic operator, and suppose its HKR--Calabi--Yau image is the coherent class \(\alpha_X\in H^2(X,\Omega_X^1)\). Then \(\alpha_X\) has Hodge type \((1,2)\). Its vanishing is a necessary obstruction-vanishing condition for the bar--cobar and trace anomaly surfaces. Equivalence with the full pentagon is conditional on a nonzero return map replacing \(H^2(C,\Omega_C^1)\), on the Positselski higher-obstruction recursion, and on the Mukai/Bruinier comparison.

This is weaker but true-shaped. It keeps the cyclic-Massey nucleus and removes the false Hodge identification, the impossible curve restriction, and the unproved motivic/graph/Duflo/Malcev equivalences.

## 4. Exact TeX replacement snippets

### Cocycle target in the abstract

Replace the displayed target around line 92 by:

```tex
\[
  [m_3, B^{(2)}]_X
  \;=\; \alpha_X^{\mathrm{cyc}}
  \;\in\; H^2(X,\Omega^1_X)
  \;\cong\; H^{1,2}(X).
\]
The equality \(h^{1,2}(X)=h^{2,1}(X)\) is Hodge symmetry, not an
identification of Hodge summands; any \(H^{2,1}\)-valued avatar is the
Serre/conjugate dual after a chosen Calabi--Yau volume form and
polarisation.
```

### Construction target and status

Replace the target paragraph in Construction `constr:cocycle` by:

```tex
At chain level this is a candidate cyclic Hochschild cocycle in the
negative cyclic bicomplex, conditional on the chain/cochain convention
for the \(S^1\)-operator:
\[
  \alpha_X^{\mathrm{cyc}}
  \in
  \HC^{-}_{\mathrm{coh}}\!\bigl(\End(T_X),
  \End(T_X)\otimes\Omega^1_X\bigr).
\]
Under the HKR map, the Calabi--Yau pairing, and the explicit trace/
contraction map specified above, its image is a coherent cohomology
class
\[
  \operatorname{HKR}_{\mathrm{CY}}(\alpha_X^{\mathrm{cyc}})
  \in H^2(X,\Omega^1_X)\cong H^{1,2}(X).
\]
```

### Hodge corollary

Replace Corollary `cor:hodge` by:

```tex
\begin{corollary}[Hodge location; \ClaimStatusProvedElsewhere]
\label{cor:hodge}
For a smooth projective K\"ahler \(X\), Dolbeault comparison gives
\[
  H^2(X,\Omega^1_X)\;\cong\;H^{1,2}(X).
\]
Thus any cocycle whose HKR--Calabi--Yau image lies in
\(H^2(X,\Omega^1_X)\) has Hodge type \((1,2)\). The number of its
coordinates equals \(h^{1,2}(X)=h^{2,1}(X)\), but the class is not an
element of \(H^{2,1}(X)\) without an additional conjugation or duality
choice.
\end{corollary}
```

### Status tags for the attacked core

Use these status replacements until the missing maps are constructed:

```tex
\begin{proposition}[Explicit representative; \ClaimStatusConditional]
```

```tex
\begin{proposition}[Atiyah cup identity, conditional on the cyclic cochain convention; \ClaimStatusConditional]
```

```tex
\begin{proposition}[Motivic lift of the cocycle; \ClaimStatusConjectured]
```

```tex
\begin{corollary}[Vanishing at motivic level; \ClaimStatusConjectured]
```

```tex
\begin{proposition}[Wheel-graph representation; \ClaimStatusConditional]
```

```tex
\begin{theorem}[Atiyah class as \(E_3\)-formality obstruction; \ClaimStatusConditional]
```

```tex
\begin{theorem}[Connes \(B^{(2)}\) as motivic cyclic class; \ClaimStatusConjectured]
```

```tex
\begin{proposition}[Cocycle and Duflo coefficient comparison; \ClaimStatusConditional]
```

```tex
\begin{theorem}[Weight-\(3\) Malcev comparison; \ClaimStatusConditional]
```

```tex
\begin{theorem}[Main theorem: conditional obstruction pentagon; \ClaimStatusConditional]
```

### Main theorem replacement surface

Replace the first sentence and H1 in `thm:main` by:

```tex
Let \(X\) be a smooth projective Calabi--Yau threefold, and assume that
Construction~\ref{constr:cocycle} produces a well-defined class
\[
  \alpha_X\in H^2(X,\Omega^1_X)\cong H^{1,2}(X).
\]
Assume further:
\begin{enumerate}[label=\textup{(H\arabic*)}]
\item the Positselski obstruction tower for the reference-curve shadow
is functorially controlled by \(\alpha_X\);
\item the trace anomaly of the derived centre is paired nondegenerately
with \(\alpha_X\) through a specified Gysin/residue/transgression map
attached to \(C\subset X\), not through \(H^2(C,\Omega^1_C)\);
\item the Mukai--Bruinier admissibility condition holds for
\((\Sigma_2,C)\).
\end{enumerate}
Under \textup{(H1)--(H3)}, the vanishing of \(\alpha_X\) is a common
obstruction-vanishing condition for the five vertices. The equivalence
of the five vertices is conditional on these three comparison maps.
```

### K3 supplement replacement

Replace the K3 target sentence around
`universal_anomaly_voa_explicit_supplement.tex:305-309` by:

```tex
The sheaf group \(H^2(K3,\Omega^1_{K3})\) is
\(H^{1,2}(K3)\), hence vanishes by dimension. This proves only the
K3-only receptacle vanishing. For \(K3\times E\), the group
\(H^2(K3\times E,\Omega^1)\) is nonzero of dimension \(21\); vanishing
there must be a computation of the specific projected class, not
vanishing of the receptacle.
```

## 5. Conditional/open obligations

1. Define \(B^{(2)}\) unambiguously: ordinary Connes \(B^{(0)}\), a cohomological BV operator, or a higher \(S^1/fE_2\) hierarchy operator. State degree and sign.
2. Construct the negative-cyclic cocycle in a named complex with differential and total degree.
3. Specify the trace/contraction from the raw Dolbeault tensor with \(\End(T_X)\) and \(\Omega^1\otimes\Omega^1\) factors to \(\Omega^1\).
4. Replace \(H^2(C,\Omega^1_C)\) by a nonzero Gysin/residue/transgression target, or drop the return edge.
5. Reprove examples in the corrected target. Quintic: nonzero Yukawa does not by itself imply nonzero \(\alpha_X\). \(K3\times E\): receptacle is 21-dimensional, so vanishing must be class-specific.
6. Motive/regulator face: construct an actual higher-Chow cycle and prove its regulator is \(\alpha_X\). No regulator injectivity may be assumed.
7. Graph/Duflo/Malcev faces: verify coefficients and isomorphisms against primary sources with convention matching.

## 6. Files changed

- `notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md`

No target TeX files were edited.

`git status --short` showed
`standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
already modified in the shared worktree; that modification was not made
by this worker.

## 7. Commands run

```bash
sed -n '1,220p' repo-local instructions file
sed -n '221,520p' repo-local instructions file
sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md
sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md
wc -l chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_voa_explicit_supplement.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex
rg -n -i -F -e 'Atiyah' -e 'Step' -e 'cocycle' -e 'Hodge' -e 'negative' -e 'Connes' -e 'cyclic' -e 'Massey' -e 'motivic' -e 'regulator' -e 'graph' -e 'Duflo' -e 'Malcev' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
rg -n -F -e '\label{' -e '\section' -e '\subsection' -e '\begin{theorem}' -e '\begin{proposition}' -e '\begin{corollary}' -e '\begin{lemma}' -e '\begin{definition}' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
rg -n -F -e '\label{' -e '\section' -e '\subsection' -e '\begin{theorem}' -e '\begin{proposition}' -e '\begin{corollary}' -e '\begin{lemma}' -e '\begin{definition}' standalones/universal_anomaly_voa_explicit_supplement.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '80,120p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '139,184p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '368,475p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '477,650p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '651,725p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '725,760p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '767,825p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '839,899p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '929,990p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '998,1049p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '1056,1150p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '280,315p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '314,395p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '393,475p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '584,715p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '710,742p'
nl -ba standalones/universal_anomaly_local_global_arithmetic_supplement.tex | sed -n '15,40p'
nl -ba standalones/universal_anomaly_local_global_arithmetic_supplement.tex | sed -n '40,76p'
rg -n -F -e 'H^{2,1}' -e 'H^{1,2}' -e 'H^2(X, \Omega^1_X)' -e 'H^2(K3, \Omega^1' -e 'H^2(Q_5, \Omega^1' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_voa_explicit_supplement.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex
nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '709,766p'
nl -ba chapters/theory/hochschild_cohomology.tex | sed -n '2658,2686p'
nl -ba notes/first_principles_cache_comprehensive.md | sed -n '28,38p'
nl -ba notes/cross_volume_aps.md | sed -n '112,123p'
python3 - <<'PY'
from math import comb
count = 0
for a0 in range(4):
  for a1 in range(4):
    for a2 in range(4):
      for a3 in range(4):
        for a4 in range(4):
          if a0+a1+a2+a3+a4 == 10:
            count += 1
print('quintic_R10_count', count)
print('inclusion_exclusion', comb(14,4) - 5*comb(10,4) + 10*comb(6,4))
k3 = {(0,0):1,(1,0):0,(2,0):1,(0,1):0,(1,1):20,(2,1):0,(0,2):1,(1,2):0,(2,2):1}
e = {(0,0):1,(1,0):1,(0,1):1,(1,1):1}
total=0; terms=[]
for i in range(3):
  j=2-i
  for r in [0,1]:
    s=1-r
    val=k3.get((r,i),0)*e.get((s,j),0)
    if val:
      terms.append(((r,i),(s,j),val))
      total += val
print('dim H^2(K3xE,Omega^1)', total)
print('nonzero terms', terms)
print('dim H^2(K3,Omega^1)', k3.get((1,2),0), 'corresponds_to_H^{1,2}')
PY
ls -l notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md 2>/dev/null || true
LC_ALL=C rg -n "[^\x00-\x7F]" notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md || true
wc -l notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md
sed -n '260,430p' notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md
git status --short -- notes/universal_anomaly_attack_heal_20260424/A1_cocycle_hodge.md standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_voa_explicit_supplement.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex
```
