# A2 pentagon loci audit

Target:
`standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
with inputs
`standalones/universal_anomaly_voa_explicit_supplement.tex` and
`standalones/universal_anomaly_local_global_arithmetic_supplement.tex`.

## 1. Common formal category

The five raw vertices do not honestly live in one category
`Pr^L_k`.  Vertex (i) is a vanishing condition for a cohomology class,
(ii) is a bar-cobar equivalence with a space of contracting homotopies,
(iii) is a parametrix/formality witness groupoid, (iv) is a
Mukai-specialised chiral bialgebra equivalence, and (v) is a trace
identity/anomaly functional.  These are not objects of `Pr^L_k`.

The correct common home is the category of derived loci over a base of
geometric data.  Let
`\mathcal B = \mathcal M_{\mathrm{cx}}^{\Sigma,C,L}(X)` be the derived
analytic/Kuranishi stack of complex structures on the fixed smooth
six-manifold together with the admissible two-stage datum
`(\Sigma_2,C,L)`, and let
`\pi : \mathcal X -> \mathcal B` be the universal family.  The universal
anomaly is a section of the obstruction complex
`\mathbb E := R\pi_*\Omega^1_{\mathcal X/\mathcal B}[2]`; on the
underived smooth stratum this is the sheaf
`R^2\pi_*\Omega^1_{\mathcal X/\mathcal B}`.  The honest vertex is the
derived zero locus
`\mathbf Z(\alpha) = \mathbf Z([m_3,B^{(2)}])` in
`\mathrm{dSt}_{/\mathcal B}` or equivalently in
`\mathrm{Shv}_{\mathrm{Spc}}(\mathcal B)`.

The repaired pentagon is therefore a diagram of derived substacks or
sheaves of witness spaces over `\mathcal B`:

```tex
\[
  \mathbf Z_{\alpha}
  \longrightarrow
  \mathbf Z_{\mathrm{BC}}
  \longrightarrow
  \mathbf Z_{\mathrm{FA}}
  \longrightarrow
  \mathbf Z_{\Delta_5}
  \longrightarrow
  \mathbf Z_{\mathrm{tr}} .
\]
```

Only after these derived loci are defined and proved equivalent may one
apply `QCoh` or `IndCoh` to obtain equivalent objects of `Pr^L_k`.
Thus `Pr^L_k` is at most a corollary category; it is not the native
category of the pentagon.

## 2. Fatal findings

CRITICAL: the main equality in `Pr^L_k` is not defined.
The abstract states that the five vertices equal a single object of
`Pr^L_k` and even equal the empty object off the locus
(`standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:85`,
`:90`, `:94`, `:98`).  The introduction repeats the claim
(`:109`, `:115`).  The theorem makes the same assertion in the theorem
header and body (`:685`, `:687`).  The lane-compatibility remark tries
to repair this by calling the vertices "canonical sub-infinity-stacks"
(`:759`, `:763`), which is close to the correct formulation, but this
is not what the theorem states.  Raw predicates, scalar identities, and
witness groupoids are not objects of `Pr^L_k`.

CRITICAL: hypothesis H1 and the return edge are impossible as written.
The theorem assumes injectivity
`H^2(X,\Omega^1_X) -> H^2(C,\Omega^1_C)` (`:687`), and the proof uses
vanishing in `H^2(C,\Omega^1_C)` to return to global vanishing
(`:705`, `:710`, `:726`).  For a smooth algebraic curve `C`, coherent
cohomology has dimension one: `H^2(C,F)=0` for every coherent sheaf
`F`, hence `H^2(C,\Omega^1_C)=0`.  The proposed map can be injective
only on the zero subspace.  It cannot detect a nonzero class in
`H^2(X,\Omega^1_X)`.

SERIOUS: the Hodge bidegree is reversed at several load-bearing points.
The manuscript identifies `H^2(X,\Omega^1_X)` with `H^{2,1}(X)`
(`:90`, `:92`, `:420`, `:442`, `:444`, `:780`, `:789`; supplement
`standalones/universal_anomaly_voa_explicit_supplement.tex:306`).  The
Dolbeault convention is `H^q(X,\Omega^p_X)=H^{p,q}(X)`, so
`H^2(X,\Omega^1_X)=H^{1,2}(X)`.  On a CY3 it is Serre-dual, and
dimension-equal, to `H^{2,1}(X)`, but it is not canonically the same
without choosing the CY volume and pairing.  This matters exactly at
the return edge, where the trace should be a dual functional.

SERIOUS: the Koszul locus is sign-reversed in the local-global
supplement.  The supplement says the relative cocycle defines a
coherent sheaf and that `\mathcal U^{\mathrm{adm}}(X)` is "the open
complement of its zero locus"
(`standalones/universal_anomaly_local_global_arithmetic_supplement.tex:32`,
`:36`).  If admissibility means `[m_3,B^{(2)}]=0`, then the locus is
the derived zero locus, not its complement.  Openness is also not
automatic for vanishing of a section of a coherent sheaf; one should
either work with the derived closed zero locus or prove a separate
open-stratum statement.

SERIOUS: the proof records implications as theorems without supplying
the necessary comparison maps of obstruction theories.  The displayed
cycle (`:701`-`:705`) and especially the step from bar-cobar
contracting homotopy to heat-kernel canonicality (`:713`) assert that
cyclic closedness/vanishing forces the cubic heat-kernel obstruction to
vanish.  Closedness of a cocycle does not imply vanishing of the cubic
Atiyah expression.  At most these are conditional identifications of
primary obstruction classes after a comparison theorem.

## 3. Repaired main theorem statement

```tex
\begin{theorem}[Universal anomaly vanishing loci; \ClaimStatusConditional]
\label{thm:main-repaired}
Let
\[
  \mathcal B=\mathcal M_{\mathrm{cx}}^{\Sigma,C,L}(X)
\]
be the derived analytic stack of smooth projective Calabi--Yau
threefolds deformation-equivalent to \(X\), equipped with a two-stage
factorisation datum \((\Sigma_2,C)\) and a Mukai lattice datum \(L\).
Let \(\pi:\mathcal X\to\mathcal B\) be the universal family and put
\[
  \mathbb E := R\pi_*\Omega^1_{\mathcal X/\mathcal B}[2].
\]
The negative-cyclic Massey--Connes construction defines a section
\[
  \alpha=[m_3,B^{(2)}]_{\mathcal X/\mathcal B}
  \in \Gamma(\mathcal B,\mathbb E)
\]
whose fibre at \(b\in\mathcal B\) is the class
\[
  [m_3,B^{(2)}]_{X_b}\in H^2(X_b,\Omega^1_{X_b})
  = H^{1,2}(X_b).
\]
Let \(\mathbf Z_\alpha\subset\mathcal B\) be its derived zero locus.

\textup{(Proved/definitional part.)}
The following objects are well-defined derived substacks, or sheaves of
spaces, over \(\mathcal B\):
\[
\mathbf Z_\alpha,\quad
\mathbf Z_{\mathrm{BC}},\quad
\mathbf Z_{\mathrm{FA}},\quad
\mathbf Z_{\Delta_5},\quad
\mathbf Z_{\mathrm{tr}},
\]
where \(\mathbf Z_{\mathrm{BC}}\) is the sheaf of chain-level
bar--cobar contracting homotopies on \(C\),
\(\mathbf Z_{\mathrm{FA}}\) is the sheaf of stage-one
factorisation-algebra parametrices with contractible choice space,
\(\mathbf Z_{\Delta_5}\) is the Mukai-admissible sheaf of equivalences
\(\Phi_3(X_b)\simeq\mathbf H_{\Delta_5}\), and
\(\mathbf Z_{\mathrm{tr}}\) is the vanishing locus of the full trace
anomaly functional.

\textup{(Conditional comparison part.)}
Assume:
\begin{enumerate}[label=\textup{(C\arabic*)}]
\item the Positselski obstruction comparison identifies the primary
bar--cobar obstruction with \(\alpha\), and all higher Malcev
obstructions vanish functorially once \(\alpha=0\);
\item the Costello--Li parametrix obstruction for
\(\Phi^{\mathrm{FA}}_3\) is identified with the same section \(\alpha\);
\item the stage-two Fubini and Mukai--Bruinier comparison is defined on
the Mukai-admissible substack and identifies the stage-two output with
\(\mathbf H_{\Delta_5}\);
\item the Kontsevich--Vlassopoulos/Feigin--Fuchs trace anomaly is the
Serre-dual functional of \(\alpha\).
\end{enumerate}
Then there are equivalences of derived substacks over the common
domain of definition
\[
  \mathbf Z_\alpha
  \simeq
  \mathbf Z_{\mathrm{BC}}
  \simeq
  \mathbf Z_{\mathrm{FA}}
  \simeq
  \mathbf Z_{\Delta_5}
  \simeq
  \mathbf Z_{\mathrm{tr}}^{\mathrm{full}} .
\]
Applying \(\mathrm{QCoh}\) or \(\mathrm{IndCoh}\) to these equivalent
derived loci gives equivalent objects of \(\mathrm{Pr}^{\mathrm L}_k\).
The five original assertions themselves are not objects of
\(\mathrm{Pr}^{\mathrm L}_k\).

\textup{(Return-edge hypothesis.)}
The last equivalence uses the full anomaly-period family, not ordinary
coherent cohomology on the reference curve.  If
\[
  \tau_{\mathcal A}:\mathbb E\longrightarrow \mathcal L_{\mathcal A}
\]
is the trace/normal-function period map attached to the admissible
family of two-stage data and \(\tau_{\mathcal A}\) is conservative on
the cyclic-skew obstruction subbundle, then
\(\mathbf Z_{\mathrm{tr}}^{\mathrm{full}}\simeq\mathbf Z_\alpha\).
Without this conservativity one has only
\(\mathbf Z_\alpha\subseteq\mathbf Z_{\mathrm{tr}}\), and the pentagon
does not close.
\end{theorem}
```

## 4. Corrected return-edge mechanism

The curve group `H^2(C,\Omega^1_C)` must be removed.  The correct dual
target is global.  For a CY3,
```tex
\[
  H^2(X,\Omega^1_X)^\vee
  \cong H^1(X,T_X)
  \cong H^1(X,\Omega^2_X),
\]
```
using Serre duality and contraction with the holomorphic volume form.
Thus the trace anomaly should be a Serre-dual period of the global
obstruction class:

```tex
\[
  \operatorname{Anom}_{\Sigma,C}(\alpha_X)
  :=
  \langle \alpha_X,\nu_{\Sigma,C}\rangle_{\mathrm{Serre}}
  \in k,
  \qquad
  \nu_{\Sigma,C}\in H^1(X,T_X)\cong H^1(X,\Omega^2_X).
\]
```

Here `\nu_{\Sigma,C}` must be constructed from the two-stage datum as
an infinitesimal Abel--Jacobi normal function, Mukai-period class, or
equivalent trace kernel.  A single scalar period cannot imply
`\alpha_X=0`; the returning implication requires the family
`\{\nu_{\Sigma,C}\}` to separate the cyclic-skew obstruction subspace:

```tex
\[
  \bigcap_{(\Sigma,C)\in\mathcal A_X}
  \ker\bigl(\alpha\mapsto
  \langle\alpha,\nu_{\Sigma,C}\rangle_{\mathrm{Serre}}\bigr)
  =0
  \quad
  \text{on }
  H^2(X,\Omega^1_X)_{\mathrm{cyc-skew}} .
\]
```

If a curve-supported residue formulation is intended, the receptacle is
codimension-two local/extraordinary pullback data, for example a
purity target of the form
```tex
\[
  H^2_C(X,\Omega^1_X)
  \simeq
  H^0\!\left(C,Li^*\Omega^1_X\otimes\det N_{C/X}\right),
\]
```
after choosing a supported lift.  It is never
`H^2(C,\Omega^1_C)`.

## 5. Open proof obligations

1. Define the base stack `\mathcal B` and its universal family with the
two-stage datum `(Sigma_2,C,L)` included.  The theorem cannot quantify
over a bare `\mathcal U^{adm}(X)` before this base is fixed.

2. Construct the relative class
`[m_3,B^{(2)}]_{\mathcal X/\mathcal B}` as a section of
`R^2\pi_*\Omega^1` or of the full perfect complex
`R\pi_*\Omega^1[2]`, with HKR and negative-cyclic filtrations
compatible in families.

3. Correct the Hodge bidegree everywhere:
`H^2(X,\Omega^1_X)=H^{1,2}(X)`, with dual
`H^1(X,T_X)=H^{2,1}(X)` after the CY volume form.

4. Replace `\mathcal U^{adm}` as an "open complement" by the derived
zero locus of the anomaly section, or prove a separate open-stratum
statement if the desired locus is a smooth open piece inside that zero
locus.

5. Prove the Positselski comparison:
the bar--cobar obstruction complex on `C` has primary obstruction
equal to the image of the global anomaly, and higher Malcev
obstructions vanish functorially from that primary vanishing.

6. Prove the Costello--Li comparison:
the stage-one parametrix obstruction is the same class `alpha`, not
merely a related heat-kernel coefficient.  The current proof does not
show that vanishing of the cyclic square forces the cubic
Atiyah/Seeley--DeWitt obstruction to vanish.

7. Prove the Mukai/Bruinier stage-two comparison only on the
Mukai-admissible/K3-fibred substack, and state what replaces it on
generic CY3 components such as the quintic.

8. Construct the trace anomaly functional
`\tau_{\mathcal A}` and prove its identification with the
Kontsevich--Vlassopoulos/Feigin--Fuchs trace.  The output must be a
functional on `H^2(X,\Omega^1_X)`, not a class in curve coherent
cohomology.

9. Prove the return-edge conservativity condition.  Without a family of
periods or normal functions separating the cyclic-skew obstruction
subspace, `trace anomaly = 0` implies only membership in a kernel, not
global vanishing of `[m_3,B^{(2)}]_X`.

## 6. Files changed

Only this report was written:
`notes/universal_anomaly_attack_heal_20260424/A2_pentagon_loci.md`.

The target standalone was already modified in the worktree and was not
edited.

## 7. Commands run

Inspection only; no build and no tests.

```bash
sed -n '1,240p' repo-local instructions file
sed -n '1,220p' /Users/raeez/chiral-bar-cobar/.agents/skills/deep-beilinson-audit/SKILL.md
rg -n "thm:main|input\\{|include\\{|universal_anomaly|pentagon|Pr\\^L|Pr\\^L|H\\^2|Koszul loci|Koszul locus|loci" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
rg --files | rg '(^chapters/connections/concordance\\.tex$|^metadata/theorem_registry\\.md$|^archive/raeeznotes/raeeznotes100/red_team_summary\\.md$|universal_anomaly_four_climax|universal_anomaly|koszul|Koszul)'
find standalones -maxdepth 2 -type f | sort | rg 'universal_anomaly|anomaly|koszul|climax|supplement'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '70,130p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '120,240p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '380,475p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '670,770p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '760,845p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '845,925p'
nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '930,995p'
rg -n "Koszul|loci|locus|Pr\\^L|pentagon|H\\^2|return|thm:main|vanishing locus|admissible" standalones/universal_anomaly_local_global_arithmetic_supplement.tex standalones/universal_anomaly_voa_explicit_supplement.tex
rg -n "universal anomaly|m_3|B\\^\\{\\(2\\)\\}|thm:main|five vertices|pentagon|Pr\\^L|H\\^2\\(C|Koszul-admissible|admissible locus|Humbert" metadata/theorem_registry.md chapters/connections/concordance.tex archive/raeeznotes/raeeznotes100/red_team_summary.md
nl -ba standalones/universal_anomaly_local_global_arithmetic_supplement.tex | sed -n '1,90p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '1,70p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '270,320p'
nl -ba standalones/universal_anomaly_voa_explicit_supplement.tex | sed -n '710,780p'
ls -la notes/universal_anomaly_attack_heal_20260424
git status --short -- notes/universal_anomaly_attack_heal_20260424 standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex standalones/universal_anomaly_voa_explicit_supplement.tex
rg -n -F "H^2(C, \\Omega^1_C)" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex standalones/universal_anomaly_voa_explicit_supplement.tex
git status --short -- notes/universal_anomaly_attack_heal_20260424/A2_pentagon_loci.md standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex standalones/universal_anomaly_local_global_arithmetic_supplement.tex standalones/universal_anomaly_voa_explicit_supplement.tex
sed -n '1,260p' notes/universal_anomaly_attack_heal_20260424/A2_pentagon_loci.md
sed -n '260,520p' notes/universal_anomaly_attack_heal_20260424/A2_pentagon_loci.md
```

One preliminary `rg` command with an over-escaped regex failed and was
re-run with `-F`; it changed no files.
