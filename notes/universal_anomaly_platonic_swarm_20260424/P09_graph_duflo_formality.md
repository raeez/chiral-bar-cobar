# P09 graph / Duflo / formality attack-heal report

## Scope

Assigned surface:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:564-584`
  (`prop:wheel-graph`, graph weights).
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:586-614`
  (`thm:formality-atiyah`, `cor:strict-formality`).
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:650-683`
  (`thm:hkr-duflo`, `prop:cocycle-duflo`, `cor:universal`).
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:712-730`
  (five-face table).
- Earlier dependency surface at
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:244`
  and `:248`, where the text transports `m_3` through formality and
  places `B^{(2)}` in the same framed Gerstenhaber/BV ambient.

The report attacks only the graph/Duflo/formality layer. I did not edit
the target TeX.

## Verdict

The graph/Duflo/formality surface is not theorem-grade as written.
It can support a strong frontier section and a conditional comparison
theorem. It cannot currently support numerical identities
`w_3=1/(2\pi^2)`, `w_3'=1/(4\pi^2)`, or
`[m_3,B^{(2)}]=1/12\,\at_X^{[2]}` as established facts.

The correct survivor is:

> `alpha_X` is a candidate first cyclic formality obstruction attached
> to a fixed cyclic-HKR datum and a fixed stable formality datum.
> Its graph and Duflo realisations are conditional comparison problems.
> Strict `E_3` formality requires vanishing of the full higher
> obstruction tower, not only vanishing of `alpha_X`.

## Findings

### CRITICAL 1: the numerical graph weights are not justified

Anchor: `standalones/...2026_04_22.tex:568-579`.

The proposition asserts
[
  [m_3,B^{(2)}]^{\mathrm{univ}}
  = w_3\Gamma_3^{\mathrm{tri}}+w_3'\Gamma_3^{\mathrm{wheel}},
  \qquad
  w_3={1\over 2\pi^2},\quad
  w_3'={1\over 4\pi^2}.
]

No cited source justifies these constants in this convention.

The standard Kontsevich admissible-graph weights already include the
normalising factor `(2*pi)^(-2n)` in the integral. In Van den Bergh's
wheel computation the wheel weights are expressed by modified Bernoulli
numbers; in the usual outward-spoke convention odd wheels vanish and
the first nonzero wheel coefficient is rational, e.g. `1/24` up to the
orientation/sign convention. This does not match a nonzero three-wheel
coefficient `1/(4*pi^2)`.

Primary anchors checked:

- Van den Bergh, *The Kontsevich weight of a wheel with spokes pointing
  outward*, arXiv:0710.2411. The abstract states the result is in terms
  of modified Bernoulli numbers; the paper defines the wheel integral
  with the `(2*pi)^(-2n)` normalisation and derives the generating
  function for `w_n`.
  Source: https://arxiv.org/abs/0710.2411 and
  https://documentserver.uhasselt.be/bitstream/1942/9843/1/vdb.pdf.
- Cattaneo-Felder 2001 is a globalization/Poisson-sigma-model paper.
  Its abstracted scope is globalization of Kontsevich's local formula,
  not the displayed `E_3` triangle/wheel coefficient computation.
  Source: https://arxiv.org/abs/hep-th/0111028.
- The local Vol I deformation-quantization chapter uses rational
  normalized Kontsevich coefficients at low order, not raw
  `pi^{-2}` constants:
  `chapters/examples/deformation_quantization.tex:891-904` and
  `:951-960`.

Heal: replace the displayed constants by formal scalars
`c_{\mathrm{tri}}(F)` and `c_{\mathrm{wheel}}(F)` depending on a chosen
stable formality morphism `F`, until the exact integral is computed in
the same graph complex and orientation convention used by the paper.

### CRITICAL 2: the Duflo coefficient `1/12` is not the stated Duflo coefficient

Anchor: `standalones/...2026_04_22.tex:654-674`.

The text asserts that Caldararu-Willerton/Calaque-Van den Bergh gives
[
  [m_3,B^{(2)}]_X
  =
  I_{\mathrm{HKR}}\left({B_2\over 2}\at_X^{[2]}\right)
  =
  {1\over 12}\at_X^{[2]}.
]

This is not a standard Duflo normalisation. The classical Duflo element is
controlled by
[
  j^{1/2}(x)=\det\nolimits^{1/2}
  \left({\sinh(\operatorname{ad}_x/2)\over
  \operatorname{ad}_x/2}\right),
]
whose logarithm has quadratic coefficient `1/48` in the usual trace
normalisation. Depending on whether the paper uses `td`, `sqrt(td)`,
`log sqrt(td)`, a contraction action on polyvectors, or an already
factorial-normalised `at_X^{[2]}`, the visible scalar can be `1/48`,
`1/24`, `1/12`, or another sign-normalised variant. The manuscript does
not declare the convention that makes `B_2/2` the correct scalar.

Calaque--Van den Bergh prove that the HKR morphism twisted by
`sqrt(td_X)` is compatible with the derived Gerstenhaber structure.
That is the right source for a corrected HKR product statement, but it
does not by itself identify the Atiyah-Connes cocycle with the scalar
`1/12` in `H^2(X,\Omega_X^1)`.

Primary anchor checked:

- Calaque--Van den Bergh, *Hochschild cohomology and Atiyah classes*,
  arXiv:0708.2725. The abstract states that HKR twisted by the square
  root of the Todd genus gives the Gerstenhaber algebra isomorphism.
  Source: https://arxiv.org/abs/0708.2725.

Heal: rename `prop:cocycle-duflo` to a conditional comparison theorem
with a scalar `c_{\mathrm{Duf}}` determined by the declared convention:
[
  \alpha_X =
  c_{\mathrm{Duf}}\,
  \pi_{\mathrm{cyc},\Omega}
  \bigl(\at_X^{[2]}\bigr)
  \in H^2(X,\Omega_X^1).
]
Only after the convention is fixed and the projection is computed may
the scalar be specialised.

### CRITICAL 3: `1/(4*pi^2)` cannot be converted into `1/12` by a Tate twist

Anchor: `standalones/...2026_04_22.tex:583` and `:673`.

The line
[
  {1\over 4\pi^2}
  =
  (2\pi i)^{-2}\cdot (-1)
]
is arithmetically false: `(2*pi*i)^(-2)=-1/(4*pi^2)`, hence
`-(2*pi*i)^(-2)=1/(4*pi^2)`. Even after correcting the sign, this is
only a period-normalisation identity. It does not turn a transcendental
period coefficient into the rational Bernoulli coefficient `1/12`.

Tate twists explain how powers of `2*pi*i` appear under Betti-de Rham
comparison. They do not identify a graph integral with a Duflo/Todd
coefficient without an explicit period comparison theorem.

Heal: remove the sentence equating the graph coefficient with `1/12`.
Replace it by: "The equality of the graph scalar and the Duflo/Todd
scalar is a convention-sensitive period comparison problem."

### CRITICAL 4: vanishing of `U_2` does not imply strict formality

Anchor: `standalones/...2026_04_22.tex:596` and `:603-610`.

The theorem says that on `\mathcal U^{adm}`, `U^3_{2,X}=0`; the same
line then says the formality morphism is strict. The proof of the
corollary says higher obstructions are iterated Massey brackets of the
second Taylor coefficient. This is false as a general statement.

An `L_\infty` quasi-isomorphism
[
  U=(U_1,U_2,U_3,\ldots)
]
does not become strict because `U_2=0`. Strictification is a separate
gauge problem in the deformation complex of the morphism. The obstruction
to killing `U_n` lives in the arity-`n` graded piece of the mapping
deformation complex, not in `U_2` alone.

Dolgushev's stable formality theorem reinforces the point: homotopy
classes of stable formality quasi-isomorphisms form a torsor under the
degree-zero cohomology of the directed graph complex. There is not a
canonical strict morphism forced by the vanishing of one Taylor
coefficient.

Primary anchor checked:

- Dolgushev, *Stable Formality Quasi-isomorphisms for Hochschild
  Cochains*, arXiv:1109.6031. The abstract states that homotopy classes
  of stable formality quasi-isomorphisms form a torsor for the group
  associated to `H^0` of the full directed graph complex.
  Source: https://arxiv.org/abs/1109.6031.

Heal: keep `cor:strict-formality` conjectural, but replace its proof by
the actual obstruction tower:
[
  \mathfrak{o}_n(U)\in
  H^1\left(F^n\Def(U)/F^{n+1}\Def(U)\right),
  \qquad n\ge 3.
]
Strictness requires `\alpha_X=0` and `\mathfrak{o}_n(U)=0` for all
`n>=3`, or an independent collapse theorem proving that these classes
are functions of `\alpha_X`.

### SERIOUS 1: the graph complex is not specified

Anchor: `standalones/...2026_04_22.tex:564-578`.

The paper moves between at least four graph languages:

- Kontsevich admissible graphs on the upper half-plane for
  deformation quantization.
- Kontsevich graph complexes `GC_n`.
- Graph models for `E_d` operads.
- Feynman graphs for holomorphic/CY factorisation-algebra perturbation
  theory.

The displayed triangle and wheel are not meaningful until the graph
operad, differential, orientation line, arity, cohomological degree, and
target map are fixed. A "triangle graph over `Conf_3(R^3)`" is not the
same object as a two-dimensional Kontsevich wheel, and neither is
automatically the Stasheff `m_3` cell.

Heal: introduce a single graph model
`\mathsf{Graphs}_{E_3}` or `\mathsf{dGra}_3`, a fixed formality datum
`F`, and a map
[
  I_F:\mathsf{Graphs}_{E_3}\longrightarrow
  \End(C^\bullet(\Perf_{\mathrm{dg}}(X))).
]
Only then can `\Gamma_3^{tri}` and `\Gamma_3^{wheel}` be defined.

### SERIOUS 2: `B^{(2)}` is not yet a graph vertex

Anchor: `standalones/...2026_04_22.tex:248`, `:574`, `:578`, `:600`.

The current proof says the cyclic shift inserts a wheel vertex at the
triangle centre. This is a picture, not a construction. Connes' operator
is a mixed-complex operator on Hochschild chains; the paper uses a
cochain-side transported operator in a framed `E_2` ambient. A graph
vertex representing this transported operator must be produced by the
cyclic/Swiss-cheese/brace model, with signs and degree.

Shoikhet proves a formality morphism for Hochschild chains, and
Willwacher proves cyclic formality for chains. These are relevant, but
they do not state that the cochain operator `B^{(2)}` used here is a
central wheel insertion in the `E_3` graph operad.

Primary anchors checked:

- Shoikhet, *A proof of the Tsygan formality conjecture for chains*,
  arXiv:math/0010321. The abstract states the extension of Kontsevich
  formality to Hochschild chains by Kontsevich-type integrals.
  Source: https://arxiv.org/abs/math/0010321.
- Willwacher, *Formality of cyclic chains*, IMRN 2011. The abstract
  states that the `u`-linear extension of Shoikhet's morphism solves
  Tsygan's cyclic-chain conjecture.
  Source: https://academic.oup.com/imrn/article/2011/17/3939/734982.

Heal: phrase the graph statement as a conjectural cyclic formality
realisation of `B^{(2)}`, not as a proved insertion rule.

### MODERATE: the five-face table still displays unstable constants

Anchor: `standalones/...2026_04_22.tex:721-725`.

The table already says that faces 2--5 are comparison faces. It should
not display the unstable values as if they were computed:

- replace `w_3\Gamma_3^{tri}+w_3'\Gamma_3^{wheel}` by
  `c_{\mathrm{tri}}\Gamma_{\mathrm{tri}}+
   c_{\mathrm{wheel}}\Gamma_{\mathrm{wheel}}`;
- replace `(B_2/2)\at_X^{[2]}=1/12\at_X^{[2]}` by
  `c_{\mathrm{Duf}}\pi_{\mathrm{cyc},\Omega}(\at_X^{[2]})`.

## Corrected theorem / conjecture split

### Proved elsewhere

1. Kontsevich formality gives an `L_\infty` quasi-isomorphism from
   polyvector fields to polydifferential operators in the classical
   deformation-quantization setting.
2. Tamarkin/Kontsevich formality gives rational operadic formality for
   `E_d` in the appropriate operadic setting.
3. Calaque--Van den Bergh prove that HKR twisted by `sqrt(td_X)` is a
   derived Gerstenhaber algebra isomorphism.
4. Van den Bergh computes standard outward wheel weights in terms of
   modified Bernoulli numbers.
5. Shoikhet and Willwacher give chain/cyclic-chain formality results
   relevant to transporting Connes' operator.
6. Stable formality morphisms carry a graph-complex/GRT torsor
   ambiguity.

### Conditional theorem-grade statement

```tex
\begin{theorem}[Conditional graph--Duflo realisation of the
Atiyah--Connes class; \ClaimStatusConditional]
Let \(X\) be a smooth projective Calabi--Yau threefold equipped with
a cyclic-HKR datum, a stable \(E_3\)-formality datum \(F\), and a
cyclic graph representative
\[
  \gamma_{\mathrm{AC}}
  =
  c_{\mathrm{tri}}(F)\Gamma_{\mathrm{tri}}
  +
  c_{\mathrm{wheel}}(F)\Gamma_{\mathrm{wheel}}
  \in \mathsf{Graphs}_{E_3}.
\]
Assume:
\begin{enumerate}[label=\textup{(GD\arabic*)}]
\item the graph integral \(I_F(\gamma_{\mathrm{AC}})\) is defined with
the same orientation and propagator convention as the cyclic-HKR datum;
\item \(I_F(\gamma_{\mathrm{AC}})\) equals the transported commutator
\([m_3,B^{(2)}]\) in the negative-cyclic Hochschild model;
\item the corrected HKR map \(I_{\mathrm{HKR}}\circ\iota_{\sqrt{\td_X}}\)
projects this commutator to
\[
  c_{\mathrm{Duf}}\,
  \pi_{\mathrm{cyc},\Omega}(\at_X^{[2]})
  \in H^2(X,\Omega_X^1);
\]
\item \(c_{\mathrm{Duf}}=
c_{\mathrm{tri}}(F)+c_{\mathrm{wheel}}(F)\) after the declared
period convention.
\end{enumerate}
Then the graph and Duflo realisations define the same class
\[
  \alpha_X=[m_3,B^{(2)}]_X\in H^2(X,\Omega_X^1).
\]
\end{theorem}
```

This is the strongest honest theorem surface until the constants are
computed.

### Conjectural frontier statements

1. There exists a canonical graph cycle `gamma_AC` whose image is
   `alpha_X`.
2. In the correct convention, the graph scalar equals the Duflo/Todd
   scalar.
3. The Atiyah-Connes zero locus is the same as the vanishing locus of
   the first cyclic formality obstruction.
4. Strict `E_3` formality holds on the admissible locus.
5. The graph weights are motivic periods compatible with the proposed
   motivic lift.

## Exact proof obligations

1. **Graph model.** Define the precise graph dg operad:
   `Graphs_{E_3}`, `dGra_3`, or another model. Give arity, degree,
   differential, orientation line, and sign convention.
2. **Formality datum.** Fix the stable formality morphism or
   associator. State the dependence on the `GRT_1` torsor.
3. **Graph representatives.** Define `Gamma_tri` and `Gamma_wheel` as
   elements of that graph complex. Prove they are cycles or compute
   their boundaries.
4. **Coefficient computation.** Compute the normalized configuration
   integrals in the chosen convention. Do not import two-dimensional
   Kontsevich wheel constants into an `E_3` graph operad without a
   comparison theorem.
5. **Cyclic operator transport.** Build the cochain-side operator
   `B^{(2)}` from the mixed complex or framed `E_2` action and prove it
   corresponds to the claimed graph insertion.
6. **HKR/Todd convention.** State whether the comparison uses bare HKR,
   `td_X`, `sqrt(td_X)`, `log sqrt(td_X)`, or a Duflo exponential.
   Define `at_X^{[2]}` including all factorials and traces.
7. **Projection to `Omega^1`.** Write the actual map
   `H^2(X,\wedge^2T_X) -> H^2(X,\Omega_X^1)` induced by the CY volume
   form and cyclic trace. Prove it is the projection used by
   `alpha_X`.
8. **Period comparison.** If pi-powers are retained, prove the
   Betti-de Rham/Tate normalisation relating the graph period to the
   rational Duflo/Todd coefficient.
9. **Strictness obstruction tower.** Define
   `Def(U)` and the classes
   `o_n(U) in H^1(F^n Def(U)/F^{n+1} Def(U))`. Prove all vanish, or
   state strictness as conjectural.
10. **Gauge invariance.** Show that `alpha_X` is invariant under changing
    the stable formality representative, or state the formality datum as
    part of the input.

## Textual repairs recommended

Replace:

```tex
with weights \(w_3 = 1/(2\pi^2)\), \(w_3'=1/(4\pi^2)\)
```

by:

```tex
with coefficients \(c_{\mathrm{tri}}(F)\) and
\(c_{\mathrm{wheel}}(F)\) determined by the chosen stable formality
datum \(F\). Their numerical values are a separate graph-integral
calculation.
```

Replace:

```tex
\([m_3,B^{(2)}]_X = (B_2/2)\at_X^{[2]} = \tfrac{1}{12}\at_X^{[2]}\)
```

by:

```tex
\([m_3,B^{(2)}]_X =
c_{\mathrm{Duf}}\,
\pi_{\mathrm{cyc},\Omega}(\at_X^{[2]})\),
where \(c_{\mathrm{Duf}}\) is fixed by the declared
\(\sqrt{\mathrm{td}}\)/Duflo convention.
```

Replace the proof of `cor:strict-formality` by:

```tex
Vanishing of \(U_{2,X}^3\) kills only the first displayed obstruction.
Strictness requires the vanishing of the higher obstruction classes
\[
  \mathfrak{o}_n(U)\in
  H^1(F^n\Def(U)/F^{n+1}\Def(U)),\qquad n\ge 3.
\]
No collapse theorem reducing these classes to
\([m_3,B^{(2)}]_X\) is used here.
```

## What survives

Proved/source-backed:

- corrected HKR/Todd-Duflo is the right language for product
  compatibility;
- graph-integral formality is the right language for a realisation of
  the obstruction;
- cyclic-chain formality is the right source family for transporting
  Connes' operator;
- strict formality is a full obstruction-tower problem.

Conditional:

- `alpha_X` is the first cyclic formality obstruction;
- `alpha_X` is a graph-cycle integral;
- `alpha_X` is a Duflo/Todd coefficient;
- the graph scalar equals the Duflo/Todd scalar.

Conjectural:

- the numerical values `1/(2*pi^2)`, `1/(4*pi^2)`, `1/12` in the
  specific comparison claimed by the standalone;
- strict `E_3` formality from the admissible-locus condition;
- motivic-period interpretation of the graph constants.

## Commands and checks

Read-only local checks:

- `rg -n -F "Duflo" ...`
- `rg -n -F "wheel" ...`
- `rg -n -F "triangle" ...`
- `rg -n -F "1/12" ...`
- `rg -n -F "formality" ...`
- `nl -ba standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex | sed -n '540,690p'`
- `nl -ba chapters/examples/deformation_quantization.tex | sed -n '826,970p'`
- targeted cache read:
  `sed -n '6788,6826p' notes/first_principles_cache_comprehensive.md`

Primary web sources checked:

- Van den Bergh, arXiv:0710.2411:
  https://arxiv.org/abs/0710.2411
- Van den Bergh author-version PDF:
  https://documentserver.uhasselt.be/bitstream/1942/9843/1/vdb.pdf
- Calaque--Van den Bergh, arXiv:0708.2725:
  https://arxiv.org/abs/0708.2725
- Cattaneo--Felder, arXiv:hep-th/0111028:
  https://arxiv.org/abs/hep-th/0111028
- Shoikhet, arXiv:math/0010321:
  https://arxiv.org/abs/math/0010321
- Dolgushev, arXiv:1109.6031:
  https://arxiv.org/abs/1109.6031
- Willwacher, IMRN 2011 cyclic chains:
  https://academic.oup.com/imrn/article/2011/17/3939/734982

Files changed: this report only.
