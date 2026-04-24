# P14: Vol II DVV / BPS-index / 3d-gravity lane

Scope: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
against `~/chiral-bar-cobar-vol2`, with P04 used for the
`\Delta_5` / `\Phi_{10}` normalization. Target TeX files were not
edited.

## Verdict

The Vol II lane supplies a real scalar theorem:
\[
  Z^{K3\times E}_{\mathrm{BPS}}(Z)
  =
  \Phi_{10}(Z)^{-1}
  =
  \Delta_5(Z)^{-2},
  \qquad Z\in\mathfrak H_2 .
\]
It is a protected BPS-index / second-quantised K3 elliptic-genus
identity. It may be cited as proved elsewhere.

It does not prove:

- an off-shell dynamical-metric 3d gravity path integral;
- an equality with the Maloney--Witten pure-gravity saddle sum;
- a chain-level identification of the ordered Virasoro bar trace with
  `\Phi_{10}^{-1}`;
- a proof that the Atiyah--Connes class `\alpha_X` vanishes;
- a construction of `\mathbf H_{\Delta_5}` as the compact
  `K3\times E` stage-two factorisation output without the
  Hall--Borcherds comparison.

The correct paper-level role is: `\Phi_{10}^{-1}` is a scalar witness
and a protected-index comparison target. It is not a gravity proof and
not an obstruction-vanishing proof.

## Local anchors

Standalone:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:308-320`
  states the DVV lane as a 3dQG path integral and marks it
  `ProvedElsewhere`.
- `...:322-335` marks the physical identification of all DVV symbols as
  `ProvedElsewhere`.
- `...:337-340` correctly fences the result as a BPS Witten-index
  identity rather than an off-shell path integral.
- `...:342-349` makes the K3-boundary comparison conditional, but its
  proof still asserts the unproved stage-two/Fubini output
  `\int_{K3}\Phi^{FA}_3=\mathbf H_{\Delta_5}`.

Vol II:

- `/Users/raeez/chiral-bar-cobar-vol2/main.tex:1372-1401` says the
  `K3\times E` bridge has one proved scalar shadow and one chain-level
  residual; until the Hall--Borcherds lemma is proved, it is not a
  construction of the full 3d gravitational path integral.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:8335-8360`
  separates the BKM weight `5`, the scalar BPS index
  `1/\Phi_{10}=1/\Delta_5^2`, and the conjectural gravity-line
  identification.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:8363-8378`
  states the missing Hall--Borcherds comparison as
  `\ClaimStatusConjectured`.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex:11033-11100`
  proves only the Borcherds scalar shadow and explicitly says it proves
  neither the ordered Virasoro bar trace nor a Maloney--Witten equality.
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/twisted_holography_quantum_gravity.tex:2911-2952`
  gives the same split: scalar automorphic/BPS identity unconditional;
  character of the Hall--Borcherds boundary object conditional on the
  conjecture.

## Findings

### CRITICAL: the standalone inherits more than Vol II proves

The standalone line
\[
  Z^{\AdS_3\times K3}_{\mathrm{3dQG,BPS}}(Z)=\Phi_{10}(Z)^{-1}
\]
is safe only if the left-hand side is defined as the protected BPS
index / twisted-holography boundary character. Vol II does not prove an
off-shell path integral for dynamical 3d gravity. It explicitly says
the `K3\times E` scalar bridge is not a construction of the full
gravitational path integral.

Heal: rename the theorem to the scalar statement:

```tex
\begin{theorem}[K3 BPS scalar and the Igusa cusp form;
\ClaimStatusProvedElsewhere]
Let \(Z\in\mathfrak H_2\). The second-quantised \(K3\) elliptic-genus
index satisfies
\[
  Z^{K3\times E}_{\mathrm{BPS}}(Z)=\Phi_{10}(Z)^{-1}
  =\Delta_5(Z)^{-2}.
\]
This is the Dijkgraaf--Moore--Verlinde--Verlinde / DVV protected-index
identity. It is not an off-shell three-dimensional gravitational path
integral.
\end{theorem}
```

### CRITICAL: `thm:dvv-as-boundary` proof uses the missing conjecture

The statement is already conditional, but the proof at
`standalones/...tex:347-349` asserts:
\[
  \int_{K3}\Phi^{FA}_3=\mathbf H_{\Delta_5}.
\]
Vol II names exactly this as the residual Hall--Borcherds comparison:
the oriented `K3\times E` Hall comparison must extend through Drinfeld
doubling, completion, current enveloping on `E`, and commute with the
`\mathsf{SC}^{ch,top}` derived-centre trace.

Heal: replace the proof by a one-paragraph conditional reduction:
assuming the Hall--Borcherds gravity-line comparison and the
stage-two character comparison, the protected scalar character is the
Vol II scalar BPS index, hence `\Phi_{10}^{-1}`. Without those
hypotheses, the theorem has no proof.

### SERIOUS: `\Phi_{10}` is not a paramodular `\Gamma_{10}` form here

The standalone says `\Phi_{10}` is the unique cusp form of weight `10`
for the paramodular group `\Gamma_{10}`. In the Vol II and DVV lane,
`\Phi_{10}` is the Igusa cusp form on genus-two Siegel space, in the
`Sp_4(\mathbb Z)` convention, with
\[
  \Phi_{10}=\Delta_5^2.
\]
The paramodular phrasing risks mixing the Gritsenko programme
paramodular family with the classical Igusa form.

Heal: write "Igusa cusp form of weight `10` on `Sp_4(\mathbb Z)`" in
the DVV scalar theorem. Keep paramodular language only when a level is
explicitly part of the CHL/Gritsenko--Nikulin variant.

### SERIOUS: `\Delta_5` and `\Phi_{10}` must not be interchanged

Vol II and P04 agree:
\[
  \kappa_{\mathrm{BKM}}(\mathfrak g_{\Delta_5})=5,\qquad
  \Phi_{10}=\Delta_5^2,\qquad
  Z_{\mathrm{BPS}}=\Phi_{10}^{-1}=\Delta_5^{-2}.
\]
Thus:

- `\Delta_5` is the primitive BKM / Gritsenko--Nikulin denominator
  object, weight `5`;
- `\Phi_{10}^{-1}` is the scalar BPS partition/index, weight `-10`
  after inversion;
- a character statement for `\mathbf H_{\Delta_5}` needs a square,
  Fock, double, or trace construction.

The standalone should not write `\operatorname{ch}\mathbf H_{\Delta_5}
=1/\Phi_{10}` without the Hall--Borcherds/Fock-character hypothesis.

### SERIOUS: the `3dQG, BPS` notation is too compressed

The object on the DVV side is a protected index. The period matrix
variables should be treated as independent Siegel variables:
\[
  Z=\begin{pmatrix}\tau&z\\ z&\sigma\end{pmatrix},\qquad
  q=e^{2\pi i\tau},\quad y=e^{2\pi i z},\quad p=e^{2\pi i\sigma}.
\]
Writing `\bar q=e^{2\pi i\sigma}` suggests complex conjugation and
blurs the holomorphic Siegel character. Use `p`, not `\bar q`.

### MODERATE: "all orders in the low-energy expansion" is the wrong
kind of exactness

The protected index is exact as a BPS/symmetric-product automorphic
identity. It is not an all-orders low-energy gravitational expansion.
Logarithmic corrections and large-charge asymptotics are read from
Fourier coefficients; they do not turn the scalar into an off-shell
path integral.

Heal: replace the sentence by:

```tex
The equality is exact as a protected index. Its large-charge
Fourier-coefficient asymptotics reproduce the expected BPS black-hole
entropy terms, but that asymptotic reading is not an off-shell
gravitational path integral.
```

## What may be cited as proved elsewhere

1. The DMVV/DVV protected-index identity:
   \[
     Z_{\mathrm{BPS}}^{K3\times E}(Z)=\Phi_{10}(Z)^{-1}.
   \]
   Primary anchors: Dijkgraaf--Moore--Verlinde--Verlinde,
   *Elliptic genera of symmetric products and second quantized
   strings*; Dijkgraaf--Verlinde--Verlinde, *Counting dyons in
   \(N=4\) string theory*, arXiv:hep-th/9607026.
2. The Borcherds/Gritsenko--Nikulin product:
   \[
     \Phi_{10}=\Delta_5^2
   \]
   in the Igusa normalization, with `\Delta_5` weight `5`.
3. The physical protected-index dictionary with `1/4`-BPS dyon counts
   in the appropriate `K3\times T^2` / CHL frame, after wall-crossing
   chamber and contour choices are fixed.

## What is physical dictionary only

1. Calling the protected index a `3dQG` partition function.
2. Interpreting the three Siegel variables as thermal, angular
   momentum, and R-charge variables in an `AdS_3` boundary dictionary.
3. Reading the scalar as a boundary character of a Hall--Borcherds
   object before the gravity-line comparison is proved.
4. Using black-hole entropy / attractor geometry as evidence for the
   normalization. This is strong physics evidence, not a proof of
   the Atiyah--Connes obstruction bridge.

## What remains conjectural or conditional

1. The Hall--Borcherds gravity-line comparison
   `conj:gravity-line-hall-borcherds-comparison`.
2. The equality between a compact `K3\times E` stage-two factorisation
   output and `\mathbf H_{\Delta_5}`.
3. The character equality
   \[
     \mathrm{ch}(\mathbf H_{\Delta_5}\text{-Fock})
     =Z_{\mathrm{BPS}}^{K3\times E}.
   \]
4. Any implication from the BPS scalar to
   \[
     \alpha_{K3\times E}=0
   \]
   or to vanishing of `\alpha_X` on a K3/Mukai/Igusa locus. That is a
   separate cyclic-projection computation, and P08 shows the raw product
   has a surviving scalar line.

## Replacement theorem for the standalone

```tex
\begin{theorem}[The DVV scalar as a protected-index comparison target]
\label{thm:dvv-scalar-target}
\ClaimStatusProvedElsewhere
Let \(Z=(\tau,z,\sigma)\in\mathfrak H_2\). In the Igusa convention,
the Gritsenko--Nikulin square root \(\Delta_5\) of weight \(5\)
satisfies
\[
  \Phi_{10}(Z)=\Delta_5(Z)^2.
\]
The second-quantised \(K3\) elliptic-genus / \(1/4\)-BPS index is
\[
  Z_{\mathrm{BPS}}^{K3\times E}(Z)
  =
  \Phi_{10}(Z)^{-1}
  =
  \Delta_5(Z)^{-2}.
\]
This is an identity of protected indices. It supplies the scalar target
for the K3/Mukai/Igusa vertex of the Atiyah--Connes comparison.
\end{theorem}

\begin{theorem}[DVV boundary character, conditional form]
\label{thm:dvv-boundary-character-conditional}
\ClaimStatusConditional
Assume the Hall--Borcherds gravity-line comparison of Vol.~II
Conjecture~\ref{conj:gravity-line-hall-borcherds-comparison}, and
assume the stage-two character comparison identifies the protected
Fock character of the \(K3\times E\) boundary object with the
Atiyah--Connes witness locus. Then the K3-boundary character in the
comparison diagram is
\[
  \mathrm{ch}_{\mathrm{BPS}}
  =
  Z_{\mathrm{BPS}}^{K3\times E}
  =
  \Phi_{10}^{-1}.
\]
No off-shell gravitational path integral and no vanishing of
\(\alpha_X\) follow from this scalar identity.
\end{theorem}
```

## Concrete next proof step

The decisive missing lemma is not another citation to DVV. It is the
Vol II conjecture:
\[
\widehat{\mathrm{CoHA}}^{\mathrm{red}}(K3\times E)
\longrightarrow
\widehat{U^{\mathrm{ch}}(\mathfrak n_+(\mathfrak g_{\Delta_5}))}
\]
must extend through Drinfeld doubling/current enveloping and commute
with the `\mathsf{SC}^{ch,top}` derived-centre trace. Only after that
can the scalar `\Phi_{10}^{-1}` become a character of the chiral
boundary object. A still separate computation must then compare that
character condition with the Atiyah--Connes obstruction class
`\alpha_X`.

## Verification

- Read the standalone DVV section at lines `308-349`.
- Read Vol II abstract scalar split at `main.tex:1372-1401`.
- Read Vol II Hall--Borcherds conjecture at
  `3d_gravity.tex:8335-8378`.
- Read Vol II scalar theorem and caveat at
  `3d_gravity.tex:11033-11100`.
- Read Vol II twisted-holography scalar theorem at
  `twisted_holography_quantum_gravity.tex:2911-2952`.
- Checked primary web anchors for DVV / DMVV / Gritsenko--Nikulin:
  arXiv `hep-th/9607026`, DMVV symmetric-product theorem, Sen dyon
  counting literature, and the Gritsenko--Nikulin Igusa product lane.
- No target TeX files were edited. No build was run.
