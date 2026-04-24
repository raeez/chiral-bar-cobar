# P07 hodge/quintic falsifier report

Date: 2026-04-24.

Owned file:

- `notes/universal_anomaly_platonic_swarm_20260424/P07_hodge_quintic_falsifier.md`

Target read-only surface:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`

No target TeX file was edited.

## Verdict

The quintic lane is a valid falsifier/evidence lane, not yet a proof of
non-vanishing of the Atiyah--Connes class.  The exact theorem-grade
content is:

1. for a smooth quintic threefold \(Q_f\subset \mathbb P^4\),
   \[
     H^2(Q_f,\Omega^1_{Q_f}) = H^{1,2}(Q_f)
   \]
   is the corrected obstruction target;
2. Griffiths' Jacobian-ring formula identifies this target with
   \(R_f^{10}\), where
   \[
     R_f=\mathbb C[x_0,\ldots,x_4]/(\partial_0f,\ldots,\partial_4f);
   \]
3. the deformation side \(H^{2,1}(Q_f)\cong H^1(Q_f,T_{Q_f})\) is
   \(R_f^5\), not \(R_f^{10}\);
4. \(\dim R_f^5=\dim R_f^{10}=101\), and the Yukawa tensor is the
   non-zero multiplication pairing
   \[
     R_f^5\otimes R_f^5\otimes R_f^5\longrightarrow R_f^{15}\cong\mathbb C;
   \]
5. this proves that the corrected target and its Yukawa detector are
   non-trivial; it does not prove
   \[
     \alpha_{Q_f}:=[m_3,B^{(2)}]_{Q_f}\ne 0.
   \]

The missing theorem is the comparison computation
\[
  \Psi_f(\alpha_{Q_f})\in R_f^{10},
\]
where \(\Psi_f:H^2(Q_f,\Omega^1_{Q_f})\xrightarrow{\sim}R_f^{10}\) is
the Griffiths residue identification with the cyclic-HKR normalisation
fixed.  Non-vanishing is then equivalent, by the Gorenstein pairing, to
the existence of \(\mu\in R_f^5\) such that
\[
  \operatorname{Soc}\bigl(\Psi_f(\alpha_{Q_f})\cdot \mu\bigr)\ne 0
  \quad\text{in }R_f^{15}\cong\mathbb C.
\]

## Local anchors

- Correct Hodge target:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:493-507`.
- Current quintic proposition:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:865-888`.
- Current generic-quintic corollary:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:890-903`.
- Hand computation:
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1207-1221`.
- Primary references already in the standalone:
  Griffiths 1969 at
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1434`,
  and Candelas--de la Ossa--Green--Parkes 1991 at
  `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1400`.

## Attacks

### Serious 1: the hand computation assigns \(R_f^{10}\) to the wrong Hodge side

The hand computation currently says Griffiths identifies the
"deformation-space piece \(H^{2,1}(Q_5)\), dual to the corrected
obstruction target \(H^{1,2}(Q_5)\), with the degree-\(10\) piece of
the Jacobian ring."

The correct Griffiths indexing for a degree-\(d\) smooth hypersurface
of dimension \(n\) is
\[
  H^{n-q,q}_{\mathrm{prim}}(X_f)\cong R_f^{(q+1)d-(n+2)}.
\]
For a quintic threefold, \(n=3\) and \(d=5\), so
\[
  H^{3,0}\cong R_f^0,\qquad
  H^{2,1}\cong R_f^5,\qquad
  H^{1,2}\cong R_f^{10},\qquad
  H^{0,3}\cong R_f^{15}.
\]
Thus \(R_f^{10}\) is exactly the corrected obstruction target
\(H^2(\Omega^1)=H^{1,2}\), while \(R_f^5\) is the deformation side
\(H^{2,1}\cong H^1(T)\).

This matters because the Yukawa tensor takes three inputs from the
deformation side \(R_f^5\), whereas the proposed obstruction class is a
single element of the dual target \(R_f^{10}\).

### Serious 2: non-zero Yukawa does not imply \(\alpha_{Q_f}\ne0\)

The non-zero Yukawa tensor proves that the cubic variation of Hodge
structure is non-trivial.  It also proves that there are non-zero
quadratic products in \(R_f^{10}\): if
\(\mu_1\mu_2\mu_3\ne0\) in the socle, then \(\mu_1\mu_2\ne0\) in
\(R_f^{10}\).

It does not identify the intrinsic Atiyah--Connes class
\(\alpha_{Q_f}\) with any such product.  There is no canonical pair of
deformation directions \((\mu_i,\mu_j)\) attached to a generic quintic,
and the class \(\alpha_{Q_f}\) is not the Yukawa cubic.  The generic
quintic has unobstructed complex deformations by Bogomolov--Tian--
Todorov, while its Yukawa tensor is non-zero; therefore non-zero Yukawa
cannot by itself be read as an obstruction class.

The only theorem-grade route is to compute the image of
\(\alpha_{Q_f}\) under the Griffiths residue isomorphism and then test
it against \(R_f^5\).

### Moderate 1: the current proposition correctly demotes the implication, but should be split

The current `prop:quintic-nonvanish` is already `Conditional`, and the
proof correctly says that Yukawa non-vanishing does not by itself
identify \(\alpha_{Q_5}\).  The mathematically cleaner surface is to
split it into two statements:

- a proved or proved-elsewhere proposition for the Hodge/Jacobian/Yukawa
  facts;
- a conditional or open question for the comparison
  \(\Psi_f(\alpha_{Q_f})\ne0\).

The title "Generic quintic falsifier" is still acceptable if the
falsified claim is precisely "universal Hodge-target collapse" or
"universal K3/Igusa vanishing on all CY3 geometries."  It is not a
proved falsifier of \(\alpha_{Q_f}=0\).

## Verified computation

Let \(f=x_0^5+\cdots+x_4^5\).  Since
\((\partial_i f)=(x_i^4)\) after removing non-zero scalar factors,
\[
  R_f=\mathbb C[x_0,\ldots,x_4]/(x_0^4,\ldots,x_4^4),
  \qquad
  \operatorname{Hilb}_{R_f}(t)=(1+t+t^2+t^3)^5.
\]
The socle degree is \(5(5-2)=15\), with
\[
  R_f^{15}=\mathbb C\cdot x_0^3x_1^3x_2^3x_3^3x_4^3.
\]

Degree \(5\):
\[
  \dim R_f^5
  =\binom{9}{4}-5\binom{5}{4}
  =126-25
  =101.
\]

Degree \(10\):
\[
  \dim R_f^{10}
  =\binom{14}{4}-5\binom{10}{4}+10\binom{6}{4}
  =1001-1050+150
  =101.
\]

The multiplication pairing \(R_f^k\otimes R_f^{15-k}\to R_f^{15}\) is
perfect for this Artinian Gorenstein ring.  In particular
\[
  R_f^{10}\otimes R_f^5\longrightarrow R_f^{15}\cong\mathbb C
\]
detects every non-zero element of the corrected obstruction target.

The explicit Yukawa witness in the current text is correct:
\[
  \mu_1=x_0^2x_1^2x_2,\quad
  \mu_2=x_0x_3^2x_4^2,\quad
  \mu_3=x_1x_2^2x_3x_4.
\]
Each \(\mu_i\in R_f^5\), and
\[
  \mu_1\mu_2\mu_3
  =x_0^3x_1^3x_2^3x_3^3x_4^3,
\]
the socle generator.  Hence the Yukawa tensor is non-zero at the
Fermat point, and therefore non-zero on a Zariski-open subset of the
smooth quintic moduli.

## Theorem-grade replacement surface

The following is the strongest statement this lane presently earns.

```tex
\begin{proposition}[Quintic Hodge target and Yukawa detector; \ClaimStatusProvedElsewhere]
\label{prop:quintic-hodge-yukawa-detector}
Let \(Q_f\subset\mathbb P^4\) be a smooth quintic threefold and
\[
  R_f=\mathbb C[x_0,\ldots,x_4]/(\partial_0 f,\ldots,\partial_4 f).
\]
Griffiths' residue theorem gives
\[
  H^{2,1}(Q_f)\cong R_f^5,\qquad
  H^2(Q_f,\Omega^1_{Q_f})=H^{1,2}(Q_f)\cong R_f^{10}.
\]
For the Fermat quintic, and hence generically,
\[
  \dim R_f^5=\dim R_f^{10}=101,
\]
and the Yukawa coupling is the non-zero socle multiplication
\[
  R_f^5\otimes R_f^5\otimes R_f^5\to R_f^{15}\cong\mathbb C.
\]
Consequently the generic quintic has a non-zero corrected obstruction
target and a non-degenerate detector
\[
  R_f^{10}\otimes R_f^5\to R_f^{15}\cong\mathbb C.
\]
\end{proposition}

\begin{question}[Atiyah--Connes/Jacobian comparison; \ClaimStatusOpen]
\label{q:quintic-atiyah-connes-jacobian-comparison}
Fix the cyclic-HKR normalisation of
\(\alpha_{Q_f}=[m_3,B^{(2)}]_{Q_f}\in H^2(Q_f,\Omega^1_{Q_f})\).
Compute
\[
  a_f:=\Psi_f(\alpha_{Q_f})\in R_f^{10}
\]
under Griffiths' residue identification.  Is there
\(\mu\in R_f^5\) such that
\[
  \operatorname{Soc}(a_f\mu)\ne0?
\]
Equivalently, is \(\alpha_{Q_f}\ne0\)?
\end{question}
```

If the programme wants a conditional theorem rather than an open
question, the exact hypothesis is:

```tex
\textup{(Q)}\quad
\Psi_f([m_3,B^{(2)}]_{Q_f})=
c\cdot\operatorname{CycSkew}_f(\mu_i\mu_j)
\text{ for explicitly named }\mu_i,\mu_j\in R_f^5
\text{ and }c\ne0.
```

Under (Q), the displayed Fermat monomials prove non-vanishing by
pairing with the remaining \(\mu_k\).

## Exact proof obligations

1. **Cyclic-HKR datum.**  Define the cochain-level \(B^{(2)}\), the
   negative-cyclic total degree, the HKR/Duflo normalisation, and the
   contraction \(H^2(\wedge^2T_{Q_f})\to H^2(\Omega^1_{Q_f})\).

2. **Residue comparison.**  Construct the map
   \[
     \Psi_f:H^2(Q_f,\Omega^1_{Q_f})\to R_f^{10}
   \]
   with the same normalisation used for the Yukawa socle pairing.

3. **Explicit class computation.**  Reduce the cyclic-skew
   Atiyah--Connes representative modulo
   \((\partial_0f,\ldots,\partial_4f)\) and record the polynomial
   \(a_f\in R_f^{10}\).

4. **Non-vanishing detector.**  Pair \(a_f\) with a basis of \(R_f^5\),
   or with one explicit \(\mu\), and prove
   \(\operatorname{Soc}(a_f\mu)\ne0\).  If every pairing is zero, then
   \(a_f=0\) by the perfect Gorenstein pairing.

5. **Genericity.**  If the computation is done at the Fermat point,
   prove the class varies algebraically in the smooth quintic family.
   Non-zero at one smooth point then gives non-zero on a Zariski-open
   subset.  Vanishing at Fermat would not decide the generic case.

## Status recommendations

- `cor:hodge`: keep as proved; its target is correct.
- `prop:quintic-nonvanish`: split into proved Hodge/Jacobian/Yukawa
  component plus conditional/open \(\alpha_{Q_f}\ne0\) component.
- `ex:hand-quintic`: correct the degree assignment:
  \(H^{2,1}\cong R_f^5\), \(H^{1,2}\cong R_f^{10}\).
- `cor:quintic-fails`: keep conditional unless the falsified claim is
  narrowed to "universal target collapse" or "universal K3/Igusa
  mechanism on all CY3s."

## Computations run

A direct monomial count checked:

- \(\dim R_f^5=101\);
- \(\dim R_f^{10}=101\);
- \(\dim R_f^{15}=1\);
- the displayed \(\mu_1,\mu_2,\mu_3\) multiply to
  \((3,3,3,3,3)\), the Fermat socle monomial.

No build was run.  No target TeX file was edited.

## Final split

- **Already proved or primary-source backed:** corrected Hodge target,
  Griffiths Jacobian-ring indexing, \(101\)-dimensional target, non-zero
  Yukawa tensor at Fermat and generically.
- **Conditionally reachable:** \(\alpha_{Q_f}\ne0\), once its
  Griffiths-residue image \(a_f\in R_f^{10}\) is computed and paired
  non-trivially with \(R_f^5\).
- **Still conjectural/open:** any claim that the generic quintic fails
  all four comparison vertices because \(\alpha_{Q_f}\ne0\).
- **Next decisive falsifier:** compute \(a_f=\Psi_f(\alpha_{Q_f})\) in
  the Fermat Jacobian ring and test it against the socle pairing.
