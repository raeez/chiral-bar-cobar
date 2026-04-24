# P08: K3 x E cyclic-projection attack-heal report

Date: 2026-04-24.

Owned file:

- `notes/universal_anomaly_platonic_swarm_20260424/P08_k3e_cyclic_projection.md`

Target read-only surface:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
- `notes/universal_anomaly_platonic_swarm_20260424/P01_cyclic_hkr_core.md`
- `notes/universal_anomaly_platonic_swarm_20260424/P04_k3_mukai_igusa_trace.md`
- `notes/universal_anomaly_platonic_swarm_20260424/P06_architecture_voice.md`

No target TeX file was edited.

## Verdict

The raw product \(Y=S\times E\), with \(S\) a projective K3 surface and
\(E\) an elliptic curve, does not give an unconditional vanishing witness
for the Atiyah--Connes obstruction.

The exact first-principles result is smaller and sharper:

\[
H^2(Y,\Omega_Y^1)=
\underbrace{H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E)}_{20}
\oplus
\underbrace{H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1)}_{1}.
\]

The raw Atiyah square of \(Y\) has only K3 legs:

\[
\operatorname{at}_Y=\pi_S^*\operatorname{at}_S,\qquad
\operatorname{at}_Y^{\cup 2}=\pi_S^*(\operatorname{at}_S^{\cup 2}).
\]

Therefore any product-natural cyclic-HKR projection kills the
20-dimensional mixed summand. It has no \(E\)-cohomology class with
which to manufacture \(H^1(E,\mathcal O_E)\).

The remaining obstruction is a single scalar in the one-dimensional
line

\[
L_{K3,E}:=H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1).
\]

Under the standard Atiyah/Chern-Weil/Rozansky-Witten normalization this
scalar is expected to be non-zero, proportional to the K3 theta/Chern
number \(\int_S c_2(T_S)=24\). Until the paper fixes the exact
\(B^{(2)}\) cochain convention, the theorem-grade statement is:

\[
\alpha_{S\times E}=0
\quad\Longleftrightarrow\quad
\lambda_{\mathrm{Cyc}}(S,E,\mathfrak c)=0,
\]

where \(\mathfrak c\) is the chosen cyclic-HKR datum and
\(\lambda_{\mathrm{Cyc}}\) is the induced scalar on \(L_{K3,E}\).

Thus \(K3\times E\) should be retained as the decisive product test, not
as a proved zero example.

## Local anchors

- P04 isolated the blocker:
  \(\operatorname{Cyc}_3(\pi_S^*\operatorname{at}_S^{\cup 2})\) must be
  computed in the two Kunneth summands of
  \(H^2(K3\times E,\Omega^1)\).
- P01 fixed the correct cyclic-HKR route:
  \[
  \beta_X\in H^2(X,\wedge^2T_X),\qquad
  \alpha_X=\iota_{\beta_X}\Omega_X\in H^2(X,\Omega_X^1).
  \]
- The live standalone now states the product only conditionally:
  \(H^2(K3\times E,\Omega^1)\) has dimension \(21\), and vanishing is
  a cyclic-projection assertion.
- P06 correctly assigns \(K3\times E\) the role of product target test,
  not theorem-grade vanishing witness.

## First-principles decomposition

Let

\[
Y=S\times E,\qquad
\pi_S:Y\to S,\qquad
\pi_E:Y\to E.
\]

Then

\[
\Omega_Y^1=\pi_S^*\Omega_S^1\oplus\pi_E^*\Omega_E^1.
\]

By Kunneth,

\[
H^2(Y,\pi_S^*\Omega_S^1)
=
\bigoplus_{i+j=2}H^i(S,\Omega_S^1)\otimes H^j(E,\mathcal O_E).
\]

For a K3 surface,

\[
H^0(S,\Omega_S^1)=0,\qquad
\dim H^1(S,\Omega_S^1)=20,\qquad
H^2(S,\Omega_S^1)=H^{1,2}(S)=0.
\]

For an elliptic curve,

\[
H^0(E,\mathcal O_E)=\mathbb C,\qquad
H^1(E,\mathcal O_E)=\mathbb C,\qquad
H^2(E,\mathcal O_E)=0.
\]

Thus

\[
H^2(Y,\pi_S^*\Omega_S^1)
=H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E).
\]

Similarly,

\[
H^2(Y,\pi_E^*\Omega_E^1)
=
\bigoplus_{i+j=2}H^i(S,\mathcal O_S)\otimes H^j(E,\Omega_E^1).
\]

The only non-zero summand is

\[
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1),
\]

because

\[
H^1(S,\mathcal O_S)=0,\qquad
H^2(E,\Omega_E^1)=0.
\]

Therefore

\[
H^2(Y,\Omega_Y^1)=U_{20}\oplus L_1
\]

with

\[
U_{20}:=H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E),
\qquad
L_1:=H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1).
\]

This proves the \(20+1\) target, with no dimension-vanishing escape.

## Raw Atiyah-square components

The tangent bundle splits:

\[
T_Y=\pi_S^*T_S\oplus\pi_E^*T_E.
\]

Atiyah classes are additive under direct sums and functorial for
pullback:

\[
\operatorname{at}_Y=
\operatorname{at}_{\pi_S^*T_S}\oplus
\operatorname{at}_{\pi_E^*T_E}
=\pi_S^*\operatorname{at}_S+\pi_E^*\operatorname{at}_E.
\]

Since \(T_E\simeq\mathcal O_E\),

\[
\operatorname{at}_E=0.
\]

Thus

\[
\operatorname{at}_Y=\pi_S^*\operatorname{at}_S.
\]

Before any cyclic-HKR projection, the square lies in the K3-only
tensor component:

\[
\operatorname{at}_Y^{\cup2}
\in
H^2\!\left(
Y,
\pi_S^*\bigl(
\operatorname{End}(T_S)^{\otimes2}
\otimes(\Omega_S^1)^{\otimes2}
\bigr)
\right).
\]

Equivalently,

\[
\operatorname{at}_Y^{\cup2}
\in
H^2\!\left(
S,
\operatorname{End}(T_S)^{\otimes2}
\otimes(\Omega_S^1)^{\otimes2}
\right)
\otimes H^0(E,\mathcal O_E).
\]

There is no \(H^1(E,\mathcal O_E)\)-factor in the raw square.

## The cyclic-HKR contraction

Fix a holomorphic symplectic form

\[
\sigma_S\in H^0(S,\Omega_S^2)
\]

and a holomorphic one-form

\[
\eta_E\in H^0(E,\Omega_E^1).
\]

The Calabi--Yau volume form is

\[
\Omega_Y=\pi_S^*\sigma_S\wedge\pi_E^*\eta_E.
\]

The polyvector component used by P01 is

\[
\beta_Y\in H^2(Y,\wedge^2T_Y),
\qquad
\alpha_Y=\iota_{\beta_Y}\Omega_Y.
\]

Now

\[
\wedge^2T_Y=
\pi_S^*\wedge^2T_S
\oplus
\left(\pi_S^*T_S\otimes\pi_E^*T_E\right),
\]

since \(\wedge^2T_E=0\). These two summands contract with
\(\Omega_Y\) as follows:

\[
\pi_S^*\wedge^2T_S
\xrightarrow{\ \iota_{(-)}\Omega_Y\ }
\pi_E^*\Omega_E^1,
\]

and

\[
\pi_S^*T_S\otimes\pi_E^*T_E
\xrightarrow{\ \iota_{(-)}\Omega_Y\ }
\pi_S^*\Omega_S^1.
\]

Therefore:

- a class in \(H^2(S,\wedge^2T_S)\otimes H^0(E,\mathcal O_E)\)
  lands in \(L_1\);
- a class in
  \(H^1(S,T_S)\otimes H^1(E,T_E)\) lands in \(U_{20}\).

The raw Atiyah square has no \(T_E\) and no \(H^1(E,\mathcal O_E)\)
factor. Hence a product-natural projection of
\(\pi_S^*(\operatorname{at}_S^{\cup2})\) cannot produce the mixed
summand \(U_{20}\).

This is the main healing: the real obstruction is not 21-dimensional.
It is one-dimensional.

## Attack on possible vanishing mechanisms

### 1. Dimension does not kill the class

The old dimension argument is false because \(L_1\neq0\). The line

\[
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1)
\]

is exactly the target produced by contracting a K3 bivector class with
\(\sigma_S\wedge\eta_E\).

### 2. Product naturality kills only the 20-dimensional summand

Any local, holomorphic, product-natural cyclic-HKR projection preserves
the \(E\)-cohomological degree of the raw class. Since the raw square
has \(H^0(E,\mathcal O_E)\), it cannot create
\(H^1(E,\mathcal O_E)\). Thus the mixed component \(U_{20}\) vanishes.

This vanishing is theorem-grade once the paper states product
naturality as part of the cyclic-HKR datum.

### 3. The one-dimensional summand is not killed canonically

On \(S\), the trace of the Atiyah square gives the second Chern
character/Chern class. Since

\[
\int_S c_2(T_S)=24,
\]

the standard Chern-Weil scalar attached to
\(\operatorname{at}_S^{\cup2}\) is non-zero. Kapranov's
holomorphic-symplectic Atiyah construction packages the same
phenomenon as the K3 theta/Rozansky-Witten class.

Therefore a cyclic projection that agrees with the standard
Atiyah-Chern normalization should send the K3 square to a non-zero
multiple of

\[
[\bar\sigma_S]\otimes\eta_E\in
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1).
\]

The exact multiple depends on the not-yet-fixed \(B^{(2)}\) convention.
The non-vanishing should not be advertised until that convention is
fixed, but neither may the paper claim canonical vanishing.

### 4. A forced skew-three projection would be a different obstruction

One could define an operation that requires a \(\wedge^3T_Y\) component
or an Atiyah leg in the elliptic direction. That operation would vanish
on \(S\times E\), because \(\operatorname{at}_E=0\) and
\(\wedge^3T_S=0\).

But that is not the P01 obstruction. The P01 obstruction uses
\[
H^2(Y,\wedge^2T_Y)\xrightarrow{\iota_{(-)}\Omega_Y}H^2(Y,\Omega_Y^1).
\]
Changing to a \(\wedge^3T_Y\) obstruction changes the theorem.

### 5. A primitive or trace-free quotient could kill the scalar, but it
must be declared

If the cyclic projection first takes a primitive/trace-free quotient
that annihilates the K3 Chern-number line, then
\(\alpha_{S\times E}\) vanishes. This is a legitimate narrower datum,
not a consequence of the canonical Atiyah class.

The cost is mathematical: the trace bridge
\(\hbar^2K=-1\), the Mukai conductor \(K=8\), and the Igusa current
edge all use trace information. A projection that kills the trace line
may also kill the arithmetic signal one wants to preserve.

## Smallest true theorem

The following is the theorem P08 recommends as the exact replacement
for any statement that \(K3\times E\) is an automatic zero witness.

```tex
\begin{theorem}[Product reduction of the K3 x E obstruction]
Let \(S\) be a projective K3 surface, let \(E\) be an elliptic curve,
and set \(Y=S\times E\). Fix
\[
  \Omega_Y=\pi_S^*\sigma_S\wedge\pi_E^*\eta_E
\]
with \(\sigma_S\in H^0(S,\Omega_S^2)\) and
\(\eta_E\in H^0(E,\Omega_E^1)\). Assume the chosen cyclic-HKR datum is
product-natural and sends the Atiyah--Connes commutator to a class
\[
  \beta_Y\in H^2(Y,\wedge^2T_Y)
\]
whose K3 product component is induced by
\(\pi_S^*(\operatorname{at}_S^{\cup2})\). Then
\[
  \alpha_Y=\iota_{\beta_Y}\Omega_Y
  \in H^2(Y,\Omega_Y^1)
\]
has zero projection to
\[
  H^1(S,\Omega_S^1)\otimes H^1(E,\mathcal O_E).
\]
Consequently
\[
  \alpha_Y=
  \lambda_{\mathrm{Cyc}}(S,E,\mathfrak c)\,
  [\bar\sigma_S]\otimes\eta_E
  \in
  H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1)
\]
for a scalar \(\lambda_{\mathrm{Cyc}}\) determined by the cyclic-HKR
datum \(\mathfrak c\). Hence
\[
  \alpha_Y=0
  \quad\Longleftrightarrow\quad
  \lambda_{\mathrm{Cyc}}(S,E,\mathfrak c)=0.
\]
Under the standard Atiyah-Chern normalization the scalar is proportional
to the K3 class \(\int_Sc_2(T_S)=24\); with that normalization the raw
product is not a vanishing witness.
\end{theorem}
```

The proof is exactly the Kunneth decomposition and the contraction
calculation above. The only conditional phrase is the identification of
the scalar with the standard Chern-Weil normalization; that waits on
the global \(B^{(2)}\) definition.

## Correct locus

The admissible product locus is not the full \(K3\times E\) locus. It is
the derived zero locus of the scalar obstruction:

\[
\mathcal Z_{K3,E}^{\mathrm{Cyc}}
=
\left\{
(S,E,\mathfrak c)\;:\;
\lambda_{\mathrm{Cyc}}(S,E,\mathfrak c)=0
\right\}.
\]

If the cyclic datum is the standard trace/Chern-Weil/Rozansky-Witten
datum, the expected value is non-zero and this locus is empty on the
raw product family. If the cyclic datum is trace-free or quotient
modified, the locus may be non-empty, but then the trace and Igusa
edges must be reproved with that modified datum.

## Replacement witnesses

### 1. Rigid Calabi--Yau threefolds

If \(X\) is a smooth projective rigid Calabi--Yau threefold with

\[
h^{1,2}(X)=0,
\]

then

\[
H^2(X,\Omega_X^1)=0,
\]

so every Atiyah--Connes class with the P01 target vanishes. This is the
cleanest strict CY3 zero witness. It does not carry the K3/Mukai/Igusa
arithmetic by itself.

### 2. K3-only reduced witness

For a K3 surface \(S\),

\[
H^2(S,\Omega_S^1)=H^{1,2}(S)=0.
\]

Any genuinely K3-two-dimensional version of the obstruction landing in
that group vanishes by dimension. This is true and useful, but it is not
a CY3 theorem and must not be used as a statement about \(S\times E\).

### 3. Abelian threefolds and complex tori

For an abelian threefold \(A\),

\[
T_A\simeq\mathcal O_A^{\oplus3},
\qquad
\operatorname{at}_A=0.
\]

Thus the obstruction vanishes before projection. This is a trivial
flat witness and violates the strict \(h^{1,0}=0\) CY3 hypothesis used
in the standalone, so it is useful only as a convention check.

### 4. Higher-order K3 x E automorphic quotients

Let \(g_S\) be a non-symplectic automorphism of a K3 surface with

\[
g_S^*\sigma_S=\zeta\sigma_S,
\]

and let \(g_E\) be an automorphism of \(E\) with

\[
g_E^*\eta_E=\zeta^{-1}\eta_E.
\]

Then \(g_S\times g_E\) preserves the CY3 form
\(\sigma_S\wedge\eta_E\). The obstruction line

\[
L_1=H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1)
\]

has character

\[
\zeta^{-1}\cdot \zeta^{-1}=\zeta^{-2}.
\]

If \(\zeta^2\neq1\), the product obstruction line has no invariant
descendant on the quotient. This is a serious replacement for
Borcea--Voisin order \(2\): the order \(2\) case has
\(\zeta=-1\), hence \(\zeta^{-2}=1\), so it does not kill \(L_1\).

The theorem-grade statement still requires:

- existence of the crepant resolution or stacky CY quotient in the
  chosen category;
- computation of the exceptional-sector contribution to
  \(H^2(\Omega^1)\);
- proof that no new exceptional Atiyah--Connes component replaces the
  killed product line;
- verification that the Mukai/Igusa trace bridge descends through the
  quotient.

This is the best K3-flavoured replacement witness P08 sees.

## Proved / conditional / conjectural split

**Proved from first principles in this report.**

- \(H^2(S\times E,\Omega^1)\) decomposes as \(20+1\).
- \(\operatorname{at}_{S\times E}=\pi_S^*\operatorname{at}_S\).
- The raw square \(\operatorname{at}_{S\times E}^{\cup2}\) has no
  \(H^1(E,\mathcal O_E)\) factor.
- Any product-natural cyclic-HKR projection of the raw K3 square has
  zero \(20\)-dimensional mixed component.
- The only possible product-natural obstruction is the scalar line
  \(H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1)\).
- Order \(2\) Borcea--Voisin symmetry does not kill that scalar line;
  higher-order non-symplectic quotients with \(\zeta^2\neq1\) do kill
  the raw product line before exceptional-sector corrections.

**Conditional.**

- Non-vanishing of \(\lambda_{\mathrm{Cyc}}\) for the paper's
  obstruction, because \(B^{(2)}\) and the cyclic-HKR scalar
  normalization are not yet fixed.
- Identification of \(\lambda_{\mathrm{Cyc}}\) with the standard K3
  Chern-Weil/Rozansky-Witten scalar proportional to
  \(\int_Sc_2(T_S)=24\).
- Any K3/Igusa bridge after replacing \(S\times E\) by a quotient.

**Conjectural / open.**

- The raw \(K3\times E\) product lies in the zero locus.
- The higher-order quotient has no exceptional-sector obstruction.
- The same quotient preserves the Mukai conductor and Igusa current
  interpretation without changing the trace normalization.

## Next proof step

Fix the cyclic-HKR datum \(\mathfrak c\) and compute the scalar

\[
\lambda_{\mathrm{Cyc}}(S,E,\mathfrak c)
\]

by pairing

\[
\operatorname{Cyc}_3(\pi_S^*\operatorname{at}_S^{\cup2})
\]

with the dual generator of

\[
H^2(S,\mathcal O_S)\otimes H^0(E,\Omega_E^1).
\]

If the result is proportional to \(\int_Sc_2(T_S)=24\), the raw product
is definitively removed as a vanishing witness and the paper should move
to either rigid CY3 witnesses or higher-order K3 x E quotient witnesses.
If the scalar is zero, the paper has a real K3-product theorem, but the
proof must explain why the cyclic projection kills the Chern-Weil/RW
line without destroying the trace edge.

## Files changed

- `notes/universal_anomaly_platonic_swarm_20260424/P08_k3e_cyclic_projection.md`

No target TeX files were edited. No build was run.
