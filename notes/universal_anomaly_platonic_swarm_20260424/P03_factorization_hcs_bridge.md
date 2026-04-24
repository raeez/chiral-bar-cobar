# P03 factorisation / hCS bridge attack-heal report

Scope: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`,
with cross-volume checks against
`~/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`,
`~/calabi-yau-quantum-groups/chapters/theory/en_factorization.tex`, and
`~/calabi-yau-quantum-groups/chapters/theory/quantum_chiral_algebras.tex`.

Owned file: `notes/universal_anomaly_platonic_swarm_20260424/P03_factorization_hcs_bridge.md`.
No target TeX files were edited. No build was run.

## Claim Attacked

The B2 bridge in Theorem `thm:main`:

```tex
Assume (B2) the Costello--Li parametrix obstruction for
\Phi^{\mathrm{FA}}_3(X) is identified with \alpha_X in the same
normalisation and in the holomorphic factorisation ambient of
\S\ref{sub:fa-precision}. Then \alpha_X=0 implies stage-one
canonicality in that ambient.
```

Local anchor: `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:777`.

The intended bridge is real and worth developing, but the theorem-grade
surface must be narrower. The correct paper-level statement is not
"Costello--Li proves the B2 edge." It is:

> A chosen holomorphic factorisation model of the CY3 open-string/BV
> theory has a one-loop local obstruction. If a chain-level comparison
> identifies that obstruction, after HKR/cyclic trace normalisation, with
> the Atiyah--Connes class
> `\alpha_X=[m_3,B^{(2)}]_X in H^2(X,\Omega^1_X)`, and if the local
> BRST anomaly complex has no further independent obstruction in the
> relevant degree, then vanishing of `\alpha_X` cancels the B2 anomaly
> and gives stage-one canonicality relative to the chosen formality,
> propagator, descent, and compactness data.

That is a conditional theorem, not a proved edge.

## Verdict

Fatal to the old strong claim; survivable as a precise conditional
bridge.

The current standalone has already healed the most visible dimensional
error: it now says real locally constant factorisation on a real
6-manifold gives `E_6`, while the paper's `E_3` notation means a
holomorphic complex-threefold refinement
(`standalones/...tex:269-278`). That repair is correct.

The remaining problem is subtler. The text still overstates what is
actually known at four points:

1. Stage-one `\Phi^{FA}_3` is still written as a functor in
   `Pr^L_{k,st}` from `D^b_dg(X)` to `Fact^{E_3}_X`
   (`standalones/...tex:283`). Vol III itself says the d=3 construction
   is an object-level, witnessed assignment on verified loci, with
   arbitrary functoriality deferred
   (`cy_to_chiral.tex:49-52`, `cy_to_chiral.tex:278-313`).
2. The factorisation/hCS edge still uses "canonicality" too globally.
   Vol III insists that at d=3 the construction requires a fixed
   formality/associator point, chain-level framing, anomaly-cancellation
   witness, completion witnesses, and a witnessed specialisation datum
   (`cy_to_chiral.tex:24-43`, `cy_to_chiral.tex:327-338`,
   `cy_to_chiral.tex:378-389`).
3. The hCS anomaly statement remains too assertive inside a conditional
   theorem: the line asserting that the Adler--Bardeen descent from
   `ch_4(F)` "produces" the class and "this class is the cocycle"
   (`standalones/...tex:823`) should be moved into an explicit bridge
   hypothesis. Vol III's own anomaly surface says the compact CY3 hCS
   anomaly degree is quartic and the compact coefficient is not yet
   asserted (`quantum_chiral_algebras.tex:3954-3999`).
4. The non-Kahler/Clemens passage still smuggles false generalities:
   `(d^H)^2=0` from balancedness, "lifts verbatim", and "every Courant
   algebroid has a CDO" (`standalones/...tex:1021`,
   `standalones/...tex:1028`, `standalones/...tex:1047`). Those are not
   part of the clean B2 theorem and should be fenced as P17 territory.

## Correct Ambient

### Real locally constant ambient

On a real `6`-manifold, a locally constant factorisation algebra is an
`E_6`-algebra. The current standalone states this correctly:

```tex
On a contractible real chart U \cong R^6, locally constant
factorisation algebras on U are equivalent to E_6-algebras.
```

Anchor: `standalones/...tex:269-272`.

This is the topological locally constant statement. It is not the B2
ambient if B2 is meant to remember the complex structure of a CY3.

### Holomorphic CY3 ambient

The B2 bridge should live in the holomorphic factorisation category on
the complex threefold:

```tex
\mathrm{Fact}^{\mathrm{hol}}_{E_3}(X)
```

or, more invariantly, in the category of Costello--Gwilliam
holomorphic factorisation algebras whose local products vary
holomorphically on configuration spaces and whose underlying
prefactorisation algebra satisfies Weiss descent. The phrase
"holomorphic `E_3`" must not be read as real locally constant `E_3`.
It means complex dimension three, with Dolbeault dependence retained.

The safest ambient is therefore a two-layer object:

```tex
\Phi^{FA}_{3,F,P}(X)
  \in \mathrm{Fact}^{\mathrm{hol}}_{E_3}(X;\Omega_X,P,F),
```

where:

- `F in Form_3(Q)` is the chosen `E_3` formality / associator datum.
- `P` is the chosen Costello--Li heat-kernel/parametrix datum.
- `\Omega_X` is the holomorphic CY volume form.
- Weiss descent is part of the object, not automatic from local charts.

This agrees with Vol III:

- `cy_to_chiral.tex:24-37` says Stage 1 is assembled only after fixing
  formality/associator and d=3 witnesses.
- `cy_to_chiral.tex:278-313` says the two-stage factorisation is proved
  only on verified/witnessed loci, and beyond those loci
  pushforward/envelope commutation remains a proof obligation.
- `cy_to_chiral.tex:327-338` separates the three steps: point-level
  `E_d`-algebra, topological `E_d`-factorisation algebra, holomorphic
  `E_d`-factorisation algebra.
- `cy_to_chiral.tex:378-389` records the `GRT_1(Q)` torsor at d=3:
  before fixing the torsor point there is no canonical equality of
  Stage-1 outputs.

## Costello--Gwilliam Locality Hypotheses

The current standalone's Weiss-descent paragraph
(`standalones/...tex:263-267`) is close to the correct structure but
should not be treated as a proof of B2.

A theorem-grade B2 statement must require:

1. A prefactorisation algebra of quantum observables on `X`, defined on
   disjoint opens.
2. Weiss cosheaf descent for those observables.
3. Renormalised BV quantisation with compatible heat kernels on all
   opens in the Weiss site.
4. Compactness or a boundary condition:
   - compact projective CY3: heat kernels exist, but BV quantisation and
     anomaly cancellation still require a local cohomology computation;
   - noncompact CY3: cylindrical end, compact support, or another
     boundary condition must be stated;
   - non-Kahler small resolutions: holomorphic factorisation is not
     available without a separate twist/replacement theorem.
5. A compatibility map from the local observable factorisation algebra
   to the Hochschild/cyclic model used to define `\alpha_X`.

Primary anchors used:

- Costello--Gwilliam, *Factorization Algebras in Quantum Field Theory*
  Vols. I--II: prefactorisation/factorisation and Weiss descent.
- Costello--Li, *Twisted supergravity and its quantization*,
  arXiv:1606.00365: holomorphic/topological BV and twisted
  supergravity/hCS framework.
- Gwilliam--Williams, *Higher Kac-Moody algebras and symmetries of
  holomorphic field theories*, arXiv:1810.06534: holomorphic field
  theories and higher factorisation-algebra symmetries.

## Costello--Li Parametrix Obstruction

The phrase "Costello--Li parametrix obstruction" is not yet a named
class in the same complex as `\alpha_X`. It must be constructed.

The correct target is a local BRST/BV anomaly group:

```tex
H^1_{\mathrm{loc},BRST}
  \bigl(\mathrm{Obs}_{\mathrm{hCS}}(X,\End T_X)\bigr)
```

or, after Dolbeault/HKR comparison and trace projection,

```tex
H^2(X,\Omega^1_X).
```

The bridge is the map

```tex
\Theta_{\mathrm{BV/HKR}}\colon
H^1_{\mathrm{loc},BRST}
  \bigl(\mathrm{Obs}_{\mathrm{hCS}}(X,\End T_X)\bigr)
  \longrightarrow
H^2(X,\Omega^1_X),
```

with the theorem-grade hypothesis

```tex
\Theta_{\mathrm{BV/HKR}}(\mathfrak a_{\mathrm{hCS}}(X,P))
  = \alpha_X.
```

Here `\mathfrak a_{\mathrm{hCS}}(X,P)` is the one-loop obstruction
computed using the chosen parametrix `P`. The equality is not supplied
by Costello--Li alone. Costello--Li gives the BV/hCS framework and
parametrix technology; the comparison with this paper's cyclic
Hochschild commutator is a new theorem to prove.

The standalone currently says the bridge condition in Theorem
`thm:main`, but then the following hCS theorem slides back into
assertion. The sentence at `standalones/...tex:823` should be fenced:

```tex
Assume the Dolbeault-refined Bardeen--Zumino descent class of the
chosen hCS model is identified by \Theta_{\mathrm{BV/HKR}} with
\alpha_X.
```

not:

```tex
the descent produces ... and this class is the cocycle.
```

## BV Anomaly Comparison

The BV anomaly in holomorphic Chern--Simons on a complex threefold is a
local functional satisfying the quantum master equation obstruction
condition. It is not automatically the Atiyah--Connes class.

Vol III supplies the decisive warning. The corrected anomaly split
(`quantum_chiral_algebras.tex:3954-3999`) says:

- in complex dimension `d`, local holomorphic gauge anomaly degree is
  `d+1`;
- for `d=3`, the local cohomological anomaly is quartic;
- quadratic Casimir terms are wave-function renormalisation/BV-trivial
  counterterms, not anomaly classes;
- a compact CY3 quantisation theorem with the quartic coefficient fixed
  is not asserted.

Thus B2 cannot be proved by a triangle-diagram slogan. The standalone's
line

```tex
the Massey bracket m_3 is the triangle-diagram one-loop obstruction
```

at `standalones/...tex:823` is unsafe. The Atiyah--Connes class is a
secondary cyclic/Hochschild obstruction in `H^2(X,\Omega^1_X)`. The
hCS gauge anomaly is controlled locally by BRST cohomology and a
Chern--Weil descent class of degree four in curvature for complex
dimension three. The bridge is deep precisely because it must explain
why the quartic local anomaly, after CY trace/contraction and cyclic
HKR, has the Atiyah--Connes shadow. That is new work, not an imported
Adler--Bardeen theorem.

## False Residues Still Present

### CRITICAL: Stage one as a global `Pr^L` functor

Anchor: `standalones/...tex:283`.

The line says Stage one is a morphism

```tex
\Phi^{FA}_3 : \cD^b_{\mathrm{dg}}(X) \to \mathrm{Fact}^{E_3}_X
```

in `Pr^L_{k,st}` and is left adjoint in a colimit-preserving adjunction.
This is stronger than Vol III permits. Vol III says:

- d=3 is object-level and witnessed (`cy_to_chiral.tex:7-9`,
  `cy_to_chiral.tex:24-43`);
- arbitrary functoriality is deferred (`cy_to_chiral.tex:49-52`);
- exactness/functoriality of stage-two kernels requires witnessed
  properness, Tor-independence, Beck--Chevalley, compact-support, and
  completion cells (`cy_to_chiral.tex:305-313`).

Repair: write Stage one as a torsor-pointed assignment on verified
objects, not as a global colimit-preserving functor, unless the exact
kernel theorem is imported as a hypothesis.

### SERIOUS: Strict formality still follows from a second obstruction

Anchors: `standalones/...tex:596`, `standalones/...tex:603-609`.

The theorem is tagged conditional and the corollary conjectural, but
the proof still says vanishing of the second Taylor coefficient gives a
strict `E_3` isomorphism and kills higher obstructions. This is false
as a proof. Vanishing of `U_2` does not imply all higher `U_n` are
gauge removable.

Repair: replace the proof with an obstruction tower:

```tex
\mathfrak{o}_n(U^3_X)\in
H^{2-n}\bigl(\mathrm{Def}_{E_3}(\End^\bullet(T_X))\bigr),
\qquad n\ge 3.
```

Then strictness requires all `\mathfrak{o}_n=0`, or an independent
collapse theorem reducing the tower to `\alpha_X`.

### SERIOUS: The hCS theorem asserts the comparison inside a hypothesis

Anchor: `standalones/...tex:810-825`.

The theorem begins conditionally but the third bullet asserts the
descent-to-cocycle equality. That equality is exactly B2. It should be
an assumption, not a line in the proof.

Repair: list five hypotheses `(F1)--(F5)` and conclude from them.
See theorem below.

### SERIOUS: Anomaly matching remark is theorem-shaped

Anchor: `standalones/...tex:841`.

The line says the cocycle "is this descent class" and its vanishing is
renormalisation-invariant by anomaly matching. This is stronger than
what has been proved. `t Hooft matching can justify persistence of a
known anomaly class across RG flow; it does not identify a Dolbeault
cyclic-Hochschild class with a local BRST descent class.

Repair: change to "would be this descent class under hypothesis
`(F3)`; anomaly matching then says the resulting class is invariant
under admissible RG flow."

### SERIOUS: Compactness automatically gives all-loop BV existence

Anchor: `standalones/...tex:846`.

Compact projective CY3 gives a good elliptic analytic setting. It does
not by itself prove all-loop BV quantisation, anomaly cancellation, or
the hCS/HKR comparison. Costello's renormalisation framework is the
machine; the anomaly cohomology and counterterm choices remain input.

Repair: "compactness supplies the heat-kernel analytic background; the
quantum master equation and anomaly cancellation remain separate
hypotheses."

### CRITICAL: `d^H` square-zero and CDO existence in Clemens passage

Anchors: `standalones/...tex:1021`, `standalones/...tex:1028`,
`standalones/...tex:1047`.

For odd `H`,

```tex
(d+H\wedge)^2 = dH\wedge(-)
```

up to the usual sign simplification. In the Strominger system one has

```tex
dH = \mathrm{tr}(R\wedge R)-\mathrm{tr}(F\wedge F)
```

before anomaly cancellation. Balancedness does not imply `(d^H)^2=0`.
Exact Courant algebroids require a closed Severa class, and CDOs have
existence/choice/characteristic-class conditions. These statements
should be conditional/open and assigned to P17, not used by B2.

### SERIOUS: Costello--Li Proposition 5.2 is overused

Anchor: `standalones/...tex:1155`.

The line says Costello--Li 2016 Proposition 5.2 gives chart-local
parametrices on Kuranishi charts. I did not find a local source in the
repo proving that this proposition has that scope. Even if such
parametrices exist, they do not imply patching, uniqueness, or
one-dimensional counterterm ambiguity on Clemens strata.

Repair: make this an open proof obligation:

```tex
Assume a Costello--Li-type chart-local parametrix exists on each
Kuranishi chart and is compatible on overlaps up to a specified
BV-exact homotopy.
```

## Repaired Conditional Theorem

This is the theorem-grade B2 statement I recommend inserting when the
main thread edits the TeX.

```tex
\begin{theorem}[Conditional factorisation--hCS bridge; \ClaimStatusConditional]
\label{thm:conditional-factorisation-hcs-bridge}
Let \(X\) be a smooth projective Calabi--Yau threefold with
holomorphic volume form \(\Omega_X\), and fix:
\[
  F\in \mathrm{Form}_3(\mathbb Q),\qquad
  P\in \mathrm{Param}_{\mathrm{hCS}}(X),
\]
where \(F\) is an \(E_3\)-formality/associator datum and \(P\) is a
Costello--Li heat-kernel parametrix for the holomorphic BV model of
hCS on \(X\) with gauge dg Lie algebra \(\End(T_X)\). Let
\(\Phi^{FA}_{3,F,P}(X)\) denote the resulting holomorphic
prefactorisation algebra of observables.

Assume:
\begin{enumerate}[label=\textup{(F\arabic*)}]
\item \textup{(Weiss descent)} \(\Phi^{FA}_{3,F,P}(X)\) satisfies
Costello--Gwilliam Weiss descent, hence is a holomorphic factorisation
algebra on \(X\). On non-compact targets this includes the stated
cylindrical-end or compact-support boundary condition.
\item \textup{(Torsor fixed)} The \(GRT_1(\mathbb Q)\)-formality torsor
has been fixed by \(F\), so canonicality is relative to \(F\), not
absolute.
\item \textup{(BV/HKR comparison)} There is a chain map
\[
  \Theta_{\mathrm{BV/HKR}}\colon
  H^1_{\mathrm{loc},BRST}
  \bigl(\Obs_{\mathrm{hCS}}(X,\End T_X;P)\bigr)
  \longrightarrow H^2(X,\Omega^1_X)
\]
which sends the one-loop local BV anomaly class
\(\mathfrak a_{\mathrm{hCS}}(X,P)\) to the Atiyah--Connes class
\[
  \Theta_{\mathrm{BV/HKR}}(\mathfrak a_{\mathrm{hCS}}(X,P))
  =
  \alpha_X=[m_3,B^{(2)}]_X.
\]
\item \textup{(Local BRST generation)} In the relevant ghost number and
form degree, the local BRST cohomology is generated by
\(\mathfrak a_{\mathrm{hCS}}(X,P)\) together with BV-exact
counterterms.
\item \textup{(Non-renormalisation / closure)} Higher-loop anomaly
classes either vanish or are functorially determined by the one-loop
class under the quantum master equation in this holomorphic BV model.
\end{enumerate}
Then \(\alpha_X=0\) cancels the hCS anomaly represented by
\(\mathfrak a_{\mathrm{hCS}}(X,P)\). If the remaining higher
obstruction classes in the \(E_3\)-formality tower vanish, the
stage-one object \(\Phi^{FA}_{3,F,P}(X)\) is canonical relative to
\((F,P,\Omega_X)\). Without \textup{(F3)--(F5)}, this is an
anomaly-matching programme, not a theorem.
\end{theorem}
```

Proof sketch:

1. `(F1)` places the observables in the Costello--Gwilliam
   holomorphic factorisation category; the real locally constant shadow
   is `E_6`, but the retained Dolbeault structure gives the holomorphic
   complex-threefold `E_3`-type object.
2. `(F2)` removes the `GRT_1` ambiguity documented in Vol III.
3. `(F3)` identifies the local BV anomaly with the cyclic HKR class
   that this paper constructs.
4. `(F4)` rules out an independent anomaly class in the same degree.
5. `(F5)` is the holomorphic analogue of the Adler--Bardeen
   non-renormalisation input; it cannot be imported from Adler--Bardeen
   1969 without proof.
6. With these hypotheses, `\alpha_X=0` kills the local anomaly class.
   Canonicality of the stage-one output then follows only relative to
   the fixed formality/parametrix data and after the higher
   `E_3`-strictification tower is separately closed.

## Proof Obligations

1. **Construct the BV anomaly class.** Define
   `\mathfrak a_{\mathrm{hCS}}(X,P)` in a local BRST complex for hCS on
   a compact CY3 with gauge dg Lie algebra `End(T_X)`. Specify ghost
   number, cohomological degree, and density/form degree.
2. **Compute the anomaly degree.** Reconcile the cyclic-Hochschild
   class in `H^2(X,\Omega^1_X)` with the quartic Chern--Weil local
   anomaly degree recorded in Vol III
   (`quantum_chiral_algebras.tex:3954-3999`). This is the central
   mathematical problem of B2.
3. **Build the BV/HKR chain map.** Produce an actual chain map from
   local BV observables to cyclic Hochschild cochains, preserving
   differentials and signs, and prove that the chosen trace/contraction
   lands in `H^2(X,\Omega^1_X)`.
4. **Normalize signs and constants.** Fix the Bochner--Martinelli /
   heat-kernel normalisation, the CY trace normalisation, the HKR
   convention, and the Connes `B^{(2)}` cochain convention. The equality
   with `\alpha_X` is meaningless before these are fixed.
5. **Prove Weiss descent.** For compact projective `X`, state the exact
   Costello--Gwilliam theorem used. For noncompact `K3 x C`, give
   cylindrical-end hypotheses. For Clemens strata, do not claim a
   holomorphic factorisation algebra without a replacement theorem.
6. **Close local BRST cohomology.** Show that the relevant local BRST
   cohomology group is one-dimensional/generated by the displayed
   anomaly, or list the other generators and include them in B2.
7. **Prove non-renormalisation in this model.** Either prove an
   Adler--Bardeen analogue for six-real-dimensional holomorphic BV hCS
   with gauge `End(T_X)`, or keep `(F5)` as a named hypothesis.
8. **Separate strictness.** The B2 anomaly cancellation does not imply
   strict `E_3` formality. A separate obstruction tower for higher
   Taylor coefficients must vanish.
9. **Fence the 5D route.** Vol III's 5D hCS/Yangian results are not a
   proof of the compact 6D CY3 B2 bridge. They can supply examples and
   local models, not the global CY3 comparison.
10. **Fence Clemens.** Require closed `H`, `(d^H)^2=0`, exact Courant
    existence, CDO existence, and a twisted BV/HKR comparison before any
    non-Kahler B2 analogue is stated.

## What Survives

Proved or source-backed:

- Real locally constant factorisation on a real six-manifold gives
  `E_6`; the holomorphic complex-threefold theory is a separate
  holomorphic `E_3`-type refinement.
- Costello--Gwilliam is the correct formalism for observables as
  factorisation algebras and for Weiss descent.
- Costello--Li is the correct provenance for holomorphic BV/hCS
  parametrix technology.
- Vol III already has the correct d=3 warning: Stage 1 is witnessed,
  torsor-pointed, and conditional outside verified loci.

Conditional:

- `\alpha_X` is the B2 hCS anomaly class.
- Vanishing of `\alpha_X` gives stage-one canonicality.
- hCS non-renormalisation in this precise holomorphic BV model.
- Strict `E_3` formality from vanishing of the second obstruction.

Conjectural/frontier:

- A canonical, model-independent functor
  `D^b_dg(X) -> Fact^{E_3,hol}_X` for arbitrary smooth projective CY3.
- The full five-vertex pentagon.
- Clemens/Strominger twisted B2.
- All-loop closure of `[m_n,B^{(n-1)}]` from `[m_3,B^{(2)}]`.

## Commands Run

No build. No tests. Read/audit commands only:

- `sed -n '1,220p' CLAUDE.md`
- `sed -n '1,240p' .agents/skills/deep-beilinson-audit/SKILL.md`
- `sed -n '1,220p' .agents/skills/beilinson-rectify/SKILL.md`
- `sed -n '1,220p' .agents/skills/frontier-research/SKILL.md`
- `sed -n` / `nl -ba` on the target standalone around the B2 and hCS
  surfaces.
- `rg` over the standalone and supplements for `Phi`, `factorisation`,
  `hCS`, `Costello`, `Adler`, `BV`, `E_3`, `E_6`, `parametrix`,
  `all-loop`, `d^H`, and related residues.
- `sed -n` / `nl -ba` on Vol III
  `chapters/theory/cy_to_chiral.tex`,
  `chapters/theory/en_factorization.tex`, and
  `chapters/theory/quantum_chiral_algebras.tex`.
- Web/source lookup for Costello--Gwilliam factorisation algebras,
  Costello--Li twisted supergravity/quantisation, and
  Gwilliam--Williams holomorphic field theories/higher Kac--Moody.

## Files Changed

Only this report file.
