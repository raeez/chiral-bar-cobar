# P17 report: Clemens, Strominger, and the H-twisted Courant-CDO lane

## Executive verdict

The Clemens/Strominger lane is not a proved extension of the
Atiyah-Connes obstruction.  In the present standalone it contains one
wrong geometric premise, one wrong differential, and one wrong CDO
existence claim.

The strongest true shape is smaller and better:

1. Clemens small resolutions are useful as non-Kahler tests for the
   analytic/factorisation part of the paper, not as automatic
   `\partial\bar\partial`-failure tests.
2. Failure of the `\partial\bar\partial`-lemma, when it is genuinely
   present, does not itself manufacture a Strominger flux, a square-zero
   `d^H`, or a Courant-CDO.
3. The heterotic replacement, if pursued, must be a conjectural bridge
   through a heterotic/transitive Courant algebroid and a neutralized
   CDO gerbe, not a theorem obtained by replacing `\bar\partial` with
   `d+H\wedge`.

## Audit surface

Target file:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`

Local anchors attacked:

- `...tex:160--163`: abstract-level Clemens/H-twisted claim.
- `...tex:986--997`: `prop:clemens-ddbar`.
- `...tex:998--1013`: `prop:clemens-explicit`.
- `...tex:1015--1021`: factorisation-algebra behaviour on non-Kahler
  CY3s.
- `...tex:1021--1028`: Courant/CDO and `d^H` assertions.
- `...tex:1023--1028`: `cor:strominger`, marked `ProvedElsewhere`.
- `...tex:1030--1044`: `thm:strominger-native`.
- `...tex:1045--1048`: "native heterotic stratum" remark.
- `...tex:1147--1156`: `thm:clemens-extension`.
- `...tex:1186--1192`: open `H`-twisted cocycle question.

Adjacent reports checked:

- P03 factorisation/hCS bridge.
- P06 architecture.
- P10 motivic/regulator.
- P12 status sync.
- A4 factorisation/hCS/Strominger warning.

## Findings

### CRITICAL 1: Clemens non-Kahler does not imply `\partial\bar\partial` failure

The statement

```tex
For Clemens' small-resolution threefolds \tilde Y, the Frolicher
spectral sequence is E_1-non-degenerate: there exists d_1^{0,3}\neq 0.
```

is not a consequence of Clemens or Friedman.  It is also the wrong
expectation for the usual small resolutions of projective nodal
threefolds.  A small resolution of a projective nodal threefold is
Moishezon, hence in Fujiki class C.  Compact complex manifolds in
Fujiki class C satisfy the `\partial\bar\partial`-lemma; equivalently,
their Hodge-to-de Rham/Frolicher sequence degenerates at `E_1`.

Therefore non-Kahlerness of the Clemens/Friedman examples tests the
absence of a Kahler form.  It does not test failure of Hodge-de Rham
degeneration, does not force a nonzero `d_1`, and does not force an
`H`-twisted replacement of the Dolbeault target.

Repair:

```tex
\begin{proposition}[Clemens small resolutions are non-Kahler but
not a \(\partial\bar\partial\)-failure input; \ClaimStatusProvedElsewhere]
Let \(\tilde Y\to Y\) be a Clemens--Friedman small resolution of a
projective nodal threefold.  Then \(\tilde Y\) is Moishezon, hence lies
in Fujiki class \(\mathcal C\).  By Deligne--Griffiths--Morgan--Sullivan,
\(\tilde Y\) satisfies the \(\partial\bar\partial\)-lemma and its
Frolicher spectral sequence degenerates at \(E_1\).  The non-Kahler
feature of \(\tilde Y\) obstructs Kahler-metric arguments; it does not
invalidate the ordinary Hodge/Dolbeault receptacle for the
Atiyah--Connes class.
\end{proposition}
```

Status recommendation:

- Replace `prop:clemens-ddbar`.
- Do not state `d_1^{0,3}\neq0` for Clemens without a specific
  non-class-C example and a computation.
- If the paper wants an actual `\partial\bar\partial`-failure witness,
  choose a different compact complex threefold and compute its
  Bott-Chern/Aeppli defect.

### CRITICAL 2: the displayed non-vanishing mechanism is formally false

`prop:clemens-explicit` claims that

```tex
[\partial\bar\partial\alpha\wedge\bar\partial\nabla]\neq 0
```

in Dolbeault cohomology.  This is not compatible with the differential.
If `\bar\partial\nabla` is `\bar\partial`-closed, then

```tex
\partial\bar\partial\alpha\wedge\bar\partial\nabla
 =
\bar\partial(-\partial\alpha\wedge\bar\partial\nabla)
```

up to the Koszul sign.  Hence it is `\bar\partial`-exact.  If
`\bar\partial\nabla` is not `\bar\partial`-closed, then the displayed
expression does not define a Dolbeault class in the first place.

The line "the failure of the `\partial\bar\partial`-lemma is exactly
the statement that `\partial\bar\partial\alpha` can be a non-zero
Dolbeault class" reverses the lemma.  A `\partial\bar\partial`-exact
form is always `\partial`-exact and `\bar\partial`-exact.  Failure of
the lemma means that a form satisfying the appropriate closedness and
exactness hypotheses need not have a `\partial\bar\partial` primitive.

Repair:

```tex
\begin{proposition}[Metric dependence as a Bott--Chern obstruction;
\ClaimStatusConditional]
Let \(Y\) be a compact complex threefold for which the relevant
Bott--Chern to Dolbeault comparison map is not an isomorphism.  The
Dolbeault representative of the cyclic Atiyah expression is canonical
only after choosing a splitting of the Bott--Chern/Aeppli comparison
sequence.  Changing the Hermitian connection changes the representative
by a Bott--Chern boundary.  Its image in ordinary Dolbeault cohomology
is zero whenever the change is literally \(\partial\bar\partial\)-exact.
Non-trivial dependence can occur only in the Bott--Chern/Aeppli defect
group, not as the displayed Dolbeault class.
\end{proposition}
```

### CRITICAL 3: `d^H=d+H\wedge` is not square-zero in the Strominger system

For any odd 3-form `H`,

```tex
(d+H\wedge)^2 = dH\wedge(-).
```

The term `H\wedge H` vanishes by odd degree, and the two mixed
`H\wedge d` terms cancel.  Thus `d^H` is a differential only when
`dH=0`.

The Strominger system does not give `dH=0` in general.  The heterotic
Bianchi identity is

```tex
dH = \frac{\alpha'}{4}\left(\operatorname{tr} R\wedge R
      - \operatorname{tr} F\wedge F\right)
```

up to convention.  Before anomaly cancellation as an equality of forms,
the ordinary exact-Courant twist by a closed Severa 3-class is not the
right object.  One needs a heterotic/transitive Courant algebroid
carrying the gauge bundle and the connection data.

Repair:

```tex
\begin{question}[Heterotic Courant differential; \ClaimStatusOpen]
For a balanced \(SU(3)\)-manifold \(Y\) with gauge bundle \(E\),
connections \(A,\nabla\), and flux \(H\) satisfying the Strominger
Bianchi identity, construct the transitive heterotic Courant algebroid
\(\mathbb E_{Y,E,H}\).  Does its BRST/vertex-algebroid differential
give a square-zero replacement for the Dolbeault differential on the
cyclic Atiyah--Connes deformation complex?
\end{question}
```

Do not write that balancedness or the existence of an `SU(3)`-structure
implies `(d^H)^2=0`.

### CRITICAL 4: "every Courant algebroid has a CDO" is false

The GMS computation gives a gerbe of holomorphic CDOs with lien
`\Omega_X^{2,cl}` and class

```tex
c(\mathcal D_X^{ch}) = 2\,ch_2(T_X)
  \in H^2(X,\Omega_X^{2,cl}).
```

For a bundle-twisted version acting on `\Lambda E`, GMS compute

```tex
c(\mathcal D_{\Lambda E}^{ch})
 =
2\,ch_2(T_X)-2\,ch_2(E).
```

Thus a CDO is not attached to an arbitrary Courant algebroid without a
neutralization/trivialization of the obstruction gerbe.  The chiral de
Rham complex exists more generally, but it is not the same object as an
unconditional holomorphic CDO carrying the asserted heterotic
worldsheet algebra.

This is exactly where the heterotic geometry becomes mathematically
interesting.  The right condition is not "there is an H-flux"; it is a
string/vertex-algebroid anomaly cancellation condition, morally

```tex
2\,ch_2(T_Y) = 2\,ch_2(E)
```

together with a differential-form representative compatible with the
Strominger Bianchi identity.

Repair:

```tex
\begin{question}[Heterotic CDO neutralisation; \ClaimStatusOpen]
Let \(Y\) be a compact complex threefold with trivial canonical bundle,
and let \(E\to Y\) be the heterotic gauge bundle.  Suppose the GMS gerbe
\(\mathcal D_{\Lambda E}^{ch}\) is neutral, i.e.
\[
  2ch_2(T_Y)-2ch_2(E)=0
  \quad\text{in }H^2(Y,\Omega_Y^{2,cl}),
\]
and choose a trivialisation compatible with a Strominger solution
\((\omega,H,A,\nabla)\).  Does the resulting heterotic CDO carry a
canonical cyclic deformation complex whose first obstruction is the
H-twisted Atiyah--Connes class?
\end{question}
```

### SERIOUS 5: `H^2(Y,\Omega^1_Y)_H` is not a defined target

The open question writes

```tex
[m_3,B^{(2)}]^H_{\tilde Y}\in H^2(\tilde Y,\Omega^1_{\tilde Y})_H.
```

There is no defined cohomology theory with this notation in the paper.
The operator `d+H\wedge` changes ordinary form degree by both `+1` and
`+3`, does not preserve Dolbeault bidegree, and does not act on
`\Omega^1_Y` as a sheaf differential.  A coherent target must be one of
the following:

- Bott-Chern/Aeppli defect cohomology, for genuine
  `\partial\bar\partial`-failure;
- hypercohomology of the vertex-algebroid/CDO deformation complex;
- local BRST cohomology of the heterotic BV theory;
- cohomology of a transitive Courant/string algebroid complex.

Recommended target:

```tex
\alpha^H_{Y,E}
  \in
\mathbb H^2\!\left(
  Y,\Def_{\mathrm{VA}}\bigl(\mathcal D^{ch,H}_{Y,E}\bigr)
\right),
```

with a comparison map to `H^2(Y,\Omega_Y^1)` only after choosing the
neutralisation and setting `H=0`.

### SERIOUS 6: non-Kahler CY3 is not automatically a heterotic vacuum

The remark

```tex
every non-Kahler CY-3 is a candidate heterotic-with-torsion vacuum;
every such vacuum has an H-flux; every H-flux has a Courant avatar;
every Courant algebroid has a CDO
```

should be deleted.  A Strominger vacuum requires substantially more:
a holomorphic volume form, a conformally balanced Hermitian metric,
a gauge bundle satisfying the Hermitian-Yang-Mills equations, a choice
of connection on `TY`, and the Bianchi/anomaly-cancellation equation.
Non-Kahlerness is not enough.

The safe sentence is:

```tex
Non-Kahler Calabi--Yau threefolds are the natural geometric place to
ask for heterotic-with-torsion refinements, but the Strominger system is
extra structure, not a consequence of non-Kahlerness.
```

### MODERATE 7: factorisation language is over-specified

The object

```tex
\mathrm{Fact}^{E_3,H}_{\tilde Y}
```

is not defined.  The current paragraph asserts a topological `E_3`
factorisation algebra on a real 6-manifold, but previous agents already
found that locally constant factorisation algebras on a real
6-manifold are `E_6`, while holomorphic complex dimension 3 requires
holomorphic factorisation language.  The Clemens lane should not carry
the burden of fixing this.  Refer back to P03:

- compact smooth real 6-manifold gives analytic background for BV
  fields;
- holomorphic/CY factorisation needs a separate holomorphic theorem;
- the heterotic Courant/CDO object, if constructed, is a vertex
  algebroid or holomorphic factorisation algebra in complex dimension
  one after worldsheet descent, not an undefined `E_3,H` category.

## What actually follows from `\partial\bar\partial` failure

If a compact complex threefold genuinely fails the
`\partial\bar\partial`-lemma, the following consequences are valid.

Proved consequences:

- Bott-Chern, Aeppli, Dolbeault, and de Rham representatives need not
  be interchangeable.
- The ordinary proof that a Dolbeault representative is independent of
  Hermitian choices can fail.
- A class written in `H^q(Y,\Omega_Y^p)` need not be a pure de Rham
  Hodge summand unless an additional degeneration/purity statement is
  supplied.
- Massey-type secondary operations may survive; DGMS formality is no
  longer available.

Non-consequences:

- It does not imply a nonzero specific Frolicher differential.
- It does not imply `d_1^{0,3}\neq0`.
- It does not imply existence of a balanced metric.
- It does not imply a Strominger solution.
- It does not imply a closed `H`.
- It does not imply a Courant algebroid with Severa class `[H]`.
- It does not imply CDO existence.
- It does not make `\partial\bar\partial\alpha` nonzero in Dolbeault
  cohomology.

## Survivor theorem ladder

### Proved/elsewhere input

1. Clemens/Friedman small resolutions give non-Kahler compact complex
   threefolds in the usual projective nodal setting.
2. Moishezon/Fujiki-class-C manifolds satisfy the
   `\partial\bar\partial`-lemma; hence Clemens small resolutions are
   not automatic `\partial\bar\partial`-failure witnesses.
3. Exact Courant algebroid twists by a 3-form require closed `H`.
4. GMS compute the CDO gerbe obstruction as `2ch_2(T_X)`, and the
   `\Lambda E` version as `2ch_2(T_X)-2ch_2(E)`.
5. Gorbounov--Gwilliam--Williams identify CDOs with the factorisation
   algebra of the curved `\beta\gamma` system after the `ch_2`
   obstruction is trivialized.

### Conditional bridge

For a non-Kahler compact complex threefold `Y` with trivial canonical
bundle, gauge bundle `E`, and Strominger data
`(\omega,H,A,\nabla)`, assume:

- (H1) the Bianchi identity is solved by a transitive heterotic
  Courant/string algebroid `\mathbb E_{Y,E,H}`;
- (H2) the GMS CDO gerbe attached to `(Y,E)` is neutral and a
  trivialisation is fixed;
- (H3) the BV quantisation/factorisation algebra of the heterotic
  curved `\beta\gamma` or hCS model exists in the required analytic
  category;
- (H4) a twisted cyclic-HKR comparison identifies its first BRST
  anomaly with a class in the vertex-algebroid deformation complex;
- (H5) specialization to `H=0` recovers the ordinary Atiyah-Connes
  class `\alpha_X`.

Then the phrase "H-twisted Atiyah-Connes obstruction" has a coherent
meaning as

```tex
\alpha^H_{Y,E}
  \in
\mathbb H^2\!\left(
  Y,\Def_{\mathrm{VA}}(\mathcal D^{ch,H}_{Y,E})
\right).
```

This conditional class can be asked to gate the H-twisted Positselski
and factorisation comparison loci.  It cannot yet gate the K3/Igusa or
trace vertices without separate automorphic and derived-centre
comparisons.

### Conjectural frontier

The right conjecture is:

```tex
\begin{conjecture}[Heterotic Atiyah--Connes obstruction;
\ClaimStatusConjectured]
Let \(Y\) be a compact complex threefold with trivial canonical bundle
and let \((E,\omega,H,A,\nabla)\) solve the Strominger system.  Suppose
the associated heterotic Courant/string algebroid exists and the GMS
gerbe \(\mathcal D_{\Lambda E}^{ch}\) is neutralized.  Then the
heterotic CDO deformation complex carries a canonical cyclic class
\[
  \alpha^H_{Y,E}\in
  \mathbb H^2\!\left(
    Y,\Def_{\mathrm{VA}}(\mathcal D^{ch,H}_{Y,E})
  \right)
\]
whose specialization at \(H=0\) is the ordinary Atiyah--Connes class
\(\alpha_X\in H^2(X,\Omega_X^1)\).  Vanishing of
\(\alpha^H_{Y,E}\) is the first obstruction to the H-twisted
bar--cobar/Positselski comparison for the resulting chiral algebra.
\end{conjecture}
```

The "four climaxes lift verbatim" sentence should not survive.  At
most, the paper may ask whether the four comparison vertices admit
heterotic analogues after this class is constructed.

## Replacement for the standalone

The Clemens section should become:

1. `Clemens small resolutions and non-Kahler analytic stress`.
2. `Bott-Chern defect and the failure mode of the Dolbeault model`
   only for actual non-`ddbar` examples.
3. `Heterotic Courant-CDO conjecture`.

The status line should read:

```tex
Clemens small resolutions are non-Kahler tests for the analytic
factorisation bridge.  The H-twisted Courant-CDO replacement is
conjectural and requires a heterotic Courant/string algebroid,
GMS gerbe neutralisation, and a twisted cyclic-HKR comparison.
```

## Primary/source anchors checked

- Clemens 1983 and Friedman 1986, as cited in the standalone, for the
  non-Kahler small-resolution surface.
- Deligne--Griffiths--Morgan--Sullivan 1975, already in the
  standalone bibliography, for the `\partial\bar\partial`/formality
  machine; modern summaries cite the class-C consequence.
- Gorbounov--Malikov--Schechtman, "Gerbes of chiral differential
  operators", arXiv:math/9906117:
  https://arxiv.org/abs/math/9906117
- Gorbounov--Malikov--Schechtman, "Gerbes of chiral differential
  operators. III", arXiv:math/0005201:
  https://arxiv.org/abs/math/0005201
- Gorbounov--Gwilliam--Williams, "Chiral differential operators via
  Batalin-Vilkovisky quantization", arXiv:1610.09657:
  https://arxiv.org/abs/1610.09657
- Witten, "Two-Dimensional Models With (0,2) Supersymmetry:
  Perturbative Aspects", arXiv:hep-th/0504078:
  https://arxiv.org/abs/hep-th/0504078
- Strominger, "Superstrings with torsion", Nucl. Phys. B 274 (1986),
  DOI 10.1016/0550-3213(86)90286-5:
  https://www.sciencedirect.com/science/article/pii/0550321386902865
- Fu--Yau, "The theory of superstring with flux on non-Kahler
  manifolds and the complex Monge-Ampere equation",
  arXiv:hep-th/0604063:
  https://arxiv.org/abs/hep-th/0604063
- Gualtieri, "Generalized complex geometry", Annals of Mathematics
  174 (2011), arXiv:math/0703298:
  https://arxiv.org/abs/math/0703298
- Baraglia--Hekmati, "Transitive Courant Algebroids, String
  Structures and T-duality", arXiv:1308.5159:
  https://arxiv.org/abs/1308.5159

## Files changed

- `notes/universal_anomaly_platonic_swarm_20260424/P17_clemens_strominger_htwist.md`

No target TeX file was edited.

## Commands run

- `sed -n` on `CLAUDE.md`, `deep-beilinson-audit/SKILL.md`,
  `frontier-research/SKILL.md`.
- `rg -n` for Clemens/Strominger/H-twist/Courant/CDO occurrences in
  the standalone and swarm reports.
- `sed -n` on the relevant standalone anchors and adjacent reports P03,
  P06, P10, P12, A4.
- Web/source checks for GMS, GGW, Witten, Strominger, Fu--Yau,
  Gualtieri, Baraglia--Hekmati.
- `pdftotext` checks of GMS and GGW PDFs to verify the CDO obstruction
  formulas.

## Remaining proof obligations

1. Decide whether the paper keeps Clemens as a non-Kahler analytic test
   or replaces it with a genuine non-`ddbar` compact complex threefold.
2. If Clemens remains, rewrite `prop:clemens-ddbar` as a class-C
   `ddbar`-positive proposition.
3. Build or cite the heterotic/transitive Courant algebroid attached to
   the chosen Strominger data.
4. Prove neutralisation of the relevant GMS gerbe.
5. Construct the heterotic CDO deformation complex and define
   `\alpha^H_{Y,E}` in its hypercohomology.
6. Prove the specialization map `\alpha^H_{Y,E}|_{H=0}=\alpha_X`.
7. Only after 1--6: ask whether vanishing of `\alpha^H_{Y,E}` controls
   the H-twisted Positselski/factorisation comparison.
